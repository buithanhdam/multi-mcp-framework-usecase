from mcp.server.fastmcp import FastMCP
from src.base_mcp_sdk.server.tools import _get_location, _get_weather, _get_statistics, _get_user, _get_config
from src.base_mcp_sdk.server.tool_models import WeatherData, LocationInfo, UserProfile, UntypedConfig
from mcp.server.fastmcp.prompts import base
from src.base_mcp_sdk.server.prompts import _greet_user, _write_story, _review_code, _debug_error
# Create an MCP server
mcp = FastMCP(
    name = "Demo",
    host= "127.0.0.1",
    port = 8765,
)

# Add an addition tool
@mcp.tool()
def get_weather(city: str) -> WeatherData:
    """Get weather for a city - returns structured data."""
    # Simulated weather data
    return _get_weather(city)


@mcp.tool()
def get_location(address: str) -> LocationInfo:
    """Get location coordinates"""
    return _get_location(address)

@mcp.tool()
def get_statistics(data_type: str) -> dict[str, float]:
    """Get various statistics"""
    return _get_statistics(data_type)

@mcp.tool()
def get_user(user_id: str) -> UserProfile:
    """Get user profile - returns structured data"""
    return _get_user(user_id)

@mcp.tool()
def get_config() -> UntypedConfig:
    """This returns unstructured output - no schema generated"""
    return _get_config()

# Lists and other types are wrapped automatically
@mcp.tool()
def list_cities() -> list[str]:
    """Get a list of cities"""
    return ["London", "Paris", "Tokyo"]
    # Returns: {"result": ["London", "Paris", "Tokyo"]}

@mcp.tool()
def get_temperature(city: str) -> float:
    """Get temperature as a simple float"""
    return 22.5
    # Returns: {"result": 22.5}

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"


# Add a prompt
@mcp.prompt()
def greet_user(name: str) -> str:
    """Generate a greeting prompt"""
    return _greet_user(name)

@mcp.prompt()
def write_story(input: str) -> str:
    """Generate a story writing prompt"""
    return _write_story(input)
@mcp.prompt()
def review_code(code: str) -> str:
    """Generate a code review prompt"""
    return _review_code(code)
@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    """Generate a debugging prompt"""
    return _debug_error(error)

if __name__ == "__main__":
    mcp.run(transport="sse")