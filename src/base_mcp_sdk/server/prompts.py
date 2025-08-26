from mcp.server.fastmcp.prompts import base
STORY_WRITER_PROMPT = """
You are a story writer.
Write a short story based on the following input.
Input: {input}
Story:
"""

GREETING_PROMPT = """
You are a friendly and engaging chatbot. Greet the user warmly and ask how you can assist them today.
User name: {name}
Greeting:
"""
def _review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"

def _write_story(input: str) -> str:
    return STORY_WRITER_PROMPT.format(input=input)

def _debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]
def _greet_user(name: str) -> str:
    """Generate a greeting prompt"""
    return GREETING_PROMPT.format(name=name)