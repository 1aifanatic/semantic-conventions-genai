# Client Inference Operation Input Tokens Metric

> **[Semantic Convention](../../docs/gen-ai/gen-ai-token-metrics.md#metric-gen_aiclientinferenceoperationinput_tokens)**

## Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.operation.name | [anthropic], [cohere], [google-genai], [openai] |
| gen_ai.provider.name | [anthropic], [cohere], [google-genai], [openai] |

## Conditionally Required

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.request.model | [anthropic], [cohere], [google-genai], [openai] |
| server.port | [anthropic], [cohere], [openai] |

## Recommended

| Attribute | Supporting Libraries |
| --- | --- |
| gen_ai.response.model | [anthropic], [google-genai], [openai] |
| server.address | [anthropic], [cohere], [openai] |

[anthropic]: ../scenarios/anthropic/scenario.py
[cohere]: ../scenarios/cohere/scenario.py
[google-genai]: ../scenarios/google-genai/scenario.py
[openai]: ../scenarios/openai/scenario.py
