import asyncio

from config import GAME_VERSION, LIMIT, CONCURRENCY, OUTPUT_DIR, SHADER_LIMIT
from service.shader_service import ShaderDownloadService

async def main():
    service = ShaderDownloadService(
        game_version=GAME_VERSION,
        shader_limit=SHADER_LIMIT,
        limit=LIMIT,
        concurrency=CONCURRENCY,
        output_dir=OUTPUT_DIR
    )
    await service.run()


if __name__ == "__main__":
    asyncio.run(main())
