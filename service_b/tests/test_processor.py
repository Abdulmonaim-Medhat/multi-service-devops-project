from processor import process_users
from unittest.mock import patch

@patch('processor.requests.get')
def test_process_users(mock_get):
    mock_get.return_value.json.return_value = {"users": ["Alice"]}
    result = process_users()
    assert result["count"] == 1