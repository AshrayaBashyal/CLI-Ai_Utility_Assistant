import json
from typing import Any
from dispatcher.dispatcher import dispatch
from engine.conversation import ConversationManager
from engine.llm import LLMClient

class ToolCallingEngine:
    def __init__(self):
        self.conversation = ConversationManager()
        self.llm = LLMClient()

    def chat(self, user_message: str) -> str:
        self.conversation.add_user_message(user_message)

        while True:
            # -Generate text turn via LLM wrapper
            response = self.llm.get_completion(self.conversation.get_history())
            message = response.choices[0].message

            # Base case: Response contains text and no requests
            if not message.tool_calls:
                self.conversation.add_assistant_message(message.content)
                return message.content

            # Parse and store the assistant message data dict
            if isinstance(message, dict):
                self.conversation.append_raw_message(message)
            else:
                self.conversation.append_raw_message(message.model_dump(exclude_none=True))

            # -Iterate through requested tool chains concurrently
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)

                # Execute target function
                result = dispatch(tool_name, arguments)

                # Store outcome block straight into manager history
                self.conversation.add_tool_message(
                    tool_call_id=tool_call.id,
                    content=json.dumps(result)
                )

    def reset_history(self) -> None:
        """Call this from app.py when '/clear' text matches."""
        self.conversation.clear()
