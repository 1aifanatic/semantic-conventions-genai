# dashscope

The DashScope SDK calls Alibaba Cloud Model Studio directly. This scenario
captures its text-generation message API; tool execution remains application code.

| Operation | Should be instrumented here | Status |
| --- | --- | --- |
| inference (`chat`) | Yes, `Generation.call` calls the model | Implemented |
| embeddings | Yes, the SDK provides embedding APIs | Not implemented |
| execute_tool | No, generation returns tool requests without executing them | Not instrumentable |

The SDK sends a real HTTP request to a local fixture server. Span values come
from the request arguments, the SDK endpoint, and the parsed response. The
response has no model identifier, so `gen_ai.response.model` is omitted.
