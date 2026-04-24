import os
import aiohttp

class Downloader:
    def __init__(self, directory: str):
        self.directory = directory
        os.makedirs(directory, exist_ok=True)

    async def download(self, session: aiohttp.ClientSession, url: str, filename: str):
        path = os.path.join(self.directory, filename)

        if os.path.exists(path):
            print(f"Skipping: {filename}")
            return False

        print(f"Downloading: {filename}")

        async with session.get(url) as res:
            res.raise_for_status()
            with open(path, "wb") as f:
                while chunk := await res.content.read(8192):
                    f.write(chunk)

        return True