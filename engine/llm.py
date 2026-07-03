from config import MODEL
from schemas.tools import TOOLS
from utils.client import client
from typing import List, Dict, Any

class LLMClient:
    def get_completion(self, messages: List[Dict[str, Any]]):
        """Sends conversation payload to the remote host server."""
        return client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )
