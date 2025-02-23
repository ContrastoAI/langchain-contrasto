from typing import Type

from langchain_core.tools import BaseTool
from pydantic import BaseModel, ConfigDict, Field

from contrasto import TrustableClient


class LangchainInjectDetectToolInput(BaseModel):
    """
    A model that detect if the input is an injection.
    """

    input: str = Field(description="The input to detect if it is an injection.")


class LangchainInjectDetectTool(BaseTool):
    """
    A tool that detect if the input is an injection.
    """

    name: str = "detect_inject"
    description: str = "Detect if the input is an injection."
    args_schema: Type[BaseModel] = LangchainInjectDetectToolInput
    return_direct: bool = False

    contrasto_client: TrustableClient

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    def _validate_input(self, raw_input: str) -> LangchainInjectDetectToolInput:
        try:
            return LangchainInjectDetectToolInput.model_validate({"input": raw_input})
        except Exception as e:
            raise ValueError(f"Invalid input format: {e}")

    def _run(self, input: str) -> str:
        validated_input = self._validate_input(input)

        try:
            output = self.contrasto_client.check_inject(validated_input)
            if isinstance(output, Exception):
                raise output
            return output
        except Exception as e:
            raise ValueError(f"Injection check failed: {e}")

    async def _arun(self, input: str) -> str:
        validated_input = self._validate_input(input)

        try:
            output = await self.contrasto_client.check_inject(validated_input)
            if isinstance(output, Exception):
                raise output
            return output
        except Exception as e:
            raise ValueError(f"Injection check failed: {e}")
