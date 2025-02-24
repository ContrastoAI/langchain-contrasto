import pytest
from contrasto import TrustableClient


@pytest.fixture
def mocked_client() -> TrustableClient:
    """
    Fixture that provides a TrustableClient instance for testing.
    """
    class MockClient:
        """
        A mock client for the Contrast API.
        """

        def check_inject(self, input: str) -> str | Exception:
            return ValueError(input)
    return MockClient() 