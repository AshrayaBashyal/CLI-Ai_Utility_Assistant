from typing import List, Dict, Any

class ConversationManager:
    def __init__(self):
        # structural rules directly inside the baseline history memory
        self.messages: List[Dict[str, Any]] = [
            {
                "role": "system",
                "content": (
                    "You are an AI Orchestrator running a multi-turn tool system. "
                    "Follow these rules blindly:\n\n"
                    "1. NEVER GUESS EMAIL ADDRESSES. If a user asks to email a person by name, "
                    "you MUST always call the 'get_contact' tool first to find their actual email address. "
                    "Do not make up patterns like 'name@gmail.com'.\n\n"
                    "2. HANDLE AMBIGUITY SAFELY. If 'get_contact' returns multiple matches (e.g., two people "
                    "named John), you are STRICTLY FORBIDDEN from sending emails to all of them. Stop immediately, "
                    "display the available choices to the user, and ask them to clarify which specific person "
                    "they want to contact.\n\n"
                    "3. ACCURATE MESSAGES. When generating the body text of an email, ensure all details requested "
                    "by the user (like currency conversions or weather reports) are completely processed and "
                    "spelled out inside the body text parameter before hitting send."
                )
            }
        ]


    def add_user_message(self, content: str) -> None:
        self.messages.append({"role": "user", "content": content})


    def add_assistant_message(self, content: str) -> None:
        self.messages.append({"role": "assistant", "content": content})


    def add_tool_message(self, tool_call_id: str, content: str) -> None:
        self.messages.append({
            "role": "tool",
            "tool_call_id": tool_call_id,
            "content": content
        })

    
    # Store the assistant message containing the tool call
    def append_raw_message(self, message_dict: Dict[str, Any]) -> None:
        self.messages.append(message_dict)


    def get_history(self) -> List[Dict[str, Any]]:
        return self.messages


    def clear(self) -> None:
        # Keep system prompt but drop user/assistant history turns
        self.messages = [self.messages[0]]
