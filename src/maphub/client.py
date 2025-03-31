import uuid
from typing import Dict, Any
import requests


class MapHubClient:
    def __init__(self, api_key: str | None, base_url: str = "https://api.maphub.co"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

        if self.api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {self.api_key}"
            })

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
        response = self.session.request(
            method,
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )
        response.raise_for_status()
        return response.json()

    def get_map(self, map_id: uuid.UUID) -> Dict[str, Any]:
        return self._make_request("GET", f"/maps/{map_id}")
