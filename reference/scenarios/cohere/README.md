# cohere

The `cohere` client is a **model-call boundary**: it calls the model directly,
so it owns inference and embeddings. Tool calling is supported, with the tool
itself running in application code.

Both non-streaming chat calls record the per-operation input and output token
histograms from `response.usage.billed_units`, matching the convention's billable
token preference. Each available count is recorded once, including zero; missing
counts are omitted. The metric attributes match the operation, provider, model,
and server on the corresponding span. Embeddings do not emit inference metrics.

| Operation | Should be instrumented here | Status |
| --- | --- | --- |
| inference (`chat`) | Yes — calls the model directly | ✅ Implemented |
| embeddings | Yes — calls the model directly | ✅ Implemented |
| execute_tool | No — the client returns tool calls but doesn't execute them; the tool runs in app code | ➖ Not instrumentable |
