"""Reference implementation for Atomic Agents' native OpenTelemetry instrumentation."""

import os

import instructor
import openai
from atomic_agents import (
    AgentConfig,
    AtomicAgent,
    BaseIOSchema,
    BaseTool,
    BaseToolConfig,
    BasicChatInputSchema,
    BasicChatOutputSchema,
)
from atomic_agents.observability import AtomicAgentsInstrumentor
from pydantic import Field
from reference_shared import flush_and_shutdown, setup_otel

MOCK_BASE_URL = os.environ["MOCK_LLM_URL"] + "/v1"


class LookupInput(BaseIOSchema):
    """Input for the fixed lookup tool."""

    query: str = Field(..., description="A short lookup query.")


class LookupOutput(BaseIOSchema):
    """Result returned by the fixed lookup tool."""

    result: str = Field(..., description="The lookup result.")


class LookupToolConfig(BaseToolConfig):
    """Configuration for the reference lookup tool."""


class LookupTool(BaseTool[LookupInput, LookupOutput]):
    """Return a fixed result for a lookup request."""

    def __init__(self, config: LookupToolConfig | None = None):
        super().__init__(config or LookupToolConfig())

    def run(self, params: LookupInput) -> LookupOutput:
        return LookupOutput(result=f"Result for: {params.query}")


def main():
    print("=== Reference Implementation: Atomic Agents ===")
    tracer_provider, logger_provider, meter_provider = setup_otel()
    instrumentor = AtomicAgentsInstrumentor()
    instrumentor.instrument(tracer_provider=tracer_provider)

    client = instructor.from_openai(openai.OpenAI(base_url=MOCK_BASE_URL, api_key="mock-key"))
    agent = AtomicAgent[BasicChatInputSchema, BasicChatOutputSchema](
        config=AgentConfig(
            client=client,
            model="gpt-4o-mini",
            name="reference-agent",
        )
    )
    response = agent.run(BasicChatInputSchema(chat_message="Say hello in one sentence."))
    print(f"  [invoke_agent] -> {response.chat_message[:60]}")

    lookup = LookupTool(config=LookupToolConfig(title="lookup"))
    result = lookup.run(LookupInput(query="reference scenario"))
    print(f"  [execute_tool] -> {result.result}")

    instrumentor.uninstrument()
    flush_and_shutdown(tracer_provider, logger_provider, meter_provider)


if __name__ == "__main__":
    main()
