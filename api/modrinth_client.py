import aiohttp

class ModrinthClient:
    BASE_URL = "https://api.modrinth.com"

    def __init__(self, session: aiohttp.ClientSession):
        self.session = session

    async def _get(self, endpoint: str, params: dict = None):
        url = f"{self.BASE_URL}{endpoint}"
        async with self.session.get(url, params=params) as res:
            res.raise_for_status()
            return await res.json()

    async def search_shaders(self, version: str, limit: int, offset: int):
        params = {
            "limit": limit,
            "offset": offset,
            "facets": f'[["versions:{version}"],["project_type:shader"]]'
        }
        return await self._get("/v2/search", params)

    async def get_versions(self, project_id: str):
        return await self._get(
            f"/v3/project/{project_id}/version",
            {"include_changelog": "false"}
        )
