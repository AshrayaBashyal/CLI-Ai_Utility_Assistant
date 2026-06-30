import json

from config import MODEL
from dispatcher.dispatcher import dispatch
from schemas.tools import TOOLS
from utils.client import client


class ToolCallingEngine:
    def __init__(self):
        self.messages = []

    def chat(self, user_message: str) -> str:
        # Add the user's message to the conversation
        self.messages.append(
            {
                "role": "user",
                "content": user_message,
            }
        )

        while True:
            response = client.chat.completions.create(
                model=MODEL,
                messages=self.messages,
                tools=TOOLS,
            )

            message = response.choices[0].message

            # Base case - no tool call
            if not message.tool_calls:
                self.messages.append(
                    {
                        "role": "assistant",
                        "content": message.content,
                    }
                )

                return message.content

            # Store the assistant message containing the tool call -> convert chatcompletion object(Pydantic object) into dict
            self.messages.append(message.model_dump(exclude_none=True))

            # Execute every requested tool.
            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name

                arguments = json.loads(tool_call.function.arguments)

                result = dispatch(tool_name, arguments)

                # Add tool output to the conversation
                self.messages.append(
                    {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result),
                    }
                )