from typing import List, Dict, Optional

class ShaderSelector:
    def __init__(self, game_version: str):
        self.game_version = game_version

    def select(self, versions: List[Dict]) -> Optional[Dict]:
        compatible = [
            v for v in versions
            if self.game_version in v.get("game_versions", [])
        ]

        if not compatible:
            return None

        compatible.sort(key=lambda v: v["date_published"], reverse=True)

        return next(
            (v for v in compatible if v.get("featured")),
            compatible[0]
        )