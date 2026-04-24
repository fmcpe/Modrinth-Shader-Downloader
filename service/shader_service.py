import asyncio, aiohttp

from api.modrinth_client import ModrinthClient
from core.selector import ShaderSelector
from core.namer import FileNamer
from core.downloader import Downloader

class ShaderDownloadService:
    def __init__(self, game_version, shader_limit, limit, concurrency, output_dir):
        self.game_version = game_version
        self.shader_limit = shader_limit
        self.limit = limit
        self.downloaded = 0

        self.connector = aiohttp.TCPConnector(limit=concurrency)

        self.selector = ShaderSelector(game_version)
        self.downloader = Downloader(output_dir)
        self.lock = asyncio.Lock()

    def can_download(self):
        return self.shader_limit < 0 or self.downloaded < self.shader_limit

    async def _process_project(self, client, project):
        async with self.lock:
            if not self.can_download():
                return
            self.downloaded += 1

        versions = await client.get_versions(project["project_id"])
        selected = self.selector.select(versions)

        if not selected or not selected.get("files"):
            return

        file = selected["files"][0]
        filename = FileNamer.build(project["title"])

        await self.downloader.download(
            client.session,
            file["url"],
            filename
        )

    async def run(self):
        async with aiohttp.ClientSession(connector=self.connector) as session:
            client = ModrinthClient(session)
            offset = 0

            while self.can_download():
                data = await client.search_shaders(
                    self.game_version,
                    self.limit,
                    offset
                )

                projects = data.get("hits", [])
                if not projects:
                    break

                await asyncio.gather(*[
                    self._process_project(client, p)
                    for p in projects
                ])

                offset += self.limit

                if offset >= data.get("total_hits", 0):
                    break