import uuid
from typing import Dict, Any, List
import requests


class MapHubClient:
    def __init__(self, api_key: str | None, base_url: str = "https://api-main-432878571563.europe-west4.run.app"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()

        if self.api_key:
            self.session.headers.update({
                "X-API-Key": f"{self.api_key}"
            })

    def _make_request(self, method: str, endpoint: str, **kwargs):
        response = self.session.request(
            method,
            f"{self.base_url}/{endpoint.lstrip('/')}",
            **kwargs
        )
        try:
            response.raise_for_status()
        except:
            raise Exception(f"Status code {response.status_code}: {response.text}")

        return response.json()

    # Project endpoints
    def get_project(self, project_id: uuid.UUID) -> Dict[str, Any]:
        return self._make_request("GET", f"/projects/{project_id}")

    def get_projects(self) -> List[Dict[str, Any]]:
        return self._make_request("GET", "/projects")

    def create_project(self, project_name: str) -> Dict[str, Any]:
        return self._make_request("POST", "/projects", json={"project_name": project_name})

    # Map endpoints
    def get_map(self, map_id: uuid.UUID) -> Dict[str, Any]:
        return self._make_request("GET", f"/maps/{map_id}")

    def get_tiler_url(self, map_id: uuid.UUID, version_id: uuid.UUID = None, alias: str = None) -> str:
        params = {}

        if version_id is None:
            params["version_id"] = version_id

        if alias is None:
            params["alias"] = alias

        return self._make_request("GET", f"/maps/{map_id}/tiler_url", params=params)

    def upload_map(self, map_name: str, project_id: uuid.UUID, public: bool, path: str):
        params = {
            "project_id": str(project_id),
            "map_name": map_name,
            "public": public,
            # "colormap": "viridis",
            # "vector_lod": 8,
        }

        with open(path, "rb") as f:
            return self._make_request("POST", f"/maps", params=params, files={"file": f})

    def download_map(self, map_id: uuid.UUID, path: str):
        response = self.session.get(f"{self.base_url}/maps/{map_id}/download")
        with open(path, "wb") as f:
            f.write(response.content)