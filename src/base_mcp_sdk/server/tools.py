from src.base_mcp_sdk.server.tool_models import WeatherData, LocationInfo, UserProfile, UntypedConfig

def _get_weather(city:str) -> WeatherData:
    return WeatherData(
        temperature=72.5,
        humidity=45.0,
        condition="sunny",
        wind_speed=5.2,
    )
def _get_location(address: str) -> LocationInfo:
    """Get location coordinates"""
    return LocationInfo(latitude=51.5074, longitude=-0.1278, name="London, UK")

def _get_statistics(data_type: str) -> dict[str, float]:
    """Get various statistics"""
    return {"mean": 42.5, "median": 40.0, "std_dev": 5.2}

def _get_user(user_id: str) -> UserProfile:
    """Get user profile - returns structured data"""
    return UserProfile(name="Alice", age=30, email="alice@example.com")


def _get_config() -> UntypedConfig:
    """This returns unstructured output - no schema generated"""
    return UntypedConfig("value1", "value2")


# Lists and other types are wrapped automatically
def _list_cities() -> list[str]:
    """Get a list of cities"""
    return ["London", "Paris", "Tokyo"]