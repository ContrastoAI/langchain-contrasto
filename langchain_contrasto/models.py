from typing import Protocol, runtime_checkable

from pydantic import BaseModel, Field


@runtime_checkable
class TrustableClient(Protocol):
    """
    Protocol defining the interface for Contrasto clients.
    Can be implemented by remote API clients or local containerized solutions.
    """

    def check_inject(self, input: str) -> str | Exception:
        """
        Detect if the input is an injection.

        Args:
            input: The string to check for injection attempts

        Returns:
            str | Exception: The result of the injection check
        """
        ...


class LangchainInjectDetectToolInput(BaseModel):
    """
    A model that detect if the input is an injection.
    """

    prompt: str = Field(
        description="The whole user prompt input to detect if it is an injection."
    )
