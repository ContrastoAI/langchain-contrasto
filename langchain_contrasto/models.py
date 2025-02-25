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


# Langchain tool input models
class LangchainInjectDetectToolInput(BaseModel):
    """
    A model that detect if the input is an injection.
    """

    prompt: str = Field(
        description="The whole user prompt input to detect if it is an injection."
    )


# Injection API response models
class GenericInjectionResponse(BaseModel):
    message: str = Field(description="The message from the API")


class ContrastoMessageResponse(GenericInjectionResponse):
    label: str = Field(
        description="The label of the injection. Can be 'injection' or 'safe'."
    )
    confidence: float = Field(
        description="The confidence of the injection. Can be a value between 0 and 1."
    )


class ContrastoInjectionResponse(GenericInjectionResponse):
    prompt: str = Field(description="The prompt that was checked.")
    message: ContrastoMessageResponse = Field(description="The message from the API.")
