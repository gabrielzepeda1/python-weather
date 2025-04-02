from src.main import get_coordinates, get_weather
from unittest.mock import patch


def test_get_coordinates():
    mock_response = {
        "results": [{"name": "London", "latitude": 51.5074, "longitude": -0.1278}]
    }

    with patch("src.main.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        latitude, longitude = get_coordinates("London")
        assert latitude == 51.5074
        assert longitude == -0.1278


def test_get_weather():
    mock_response = {"current_weather": {"temperature": 22.5}}

    with patch("src.main.requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_response

        temp = get_weather(51.5074, -0.1278) 
        assert temp == 22.5
