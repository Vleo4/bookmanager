import pytest
from unittest.mock import MagicMock
from dao.book_dao import BookDAO

@pytest.fixture
def mock_dao():
    return MagicMock(spec=BookDAO)