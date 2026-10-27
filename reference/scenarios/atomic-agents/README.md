# atomic-agents

Atomic Agents provides native OpenTelemetry instrumentation for agent runs and
tool runs. This scenario uses its instrumentor and disables the framework's LLM
attempt spans so inference remains the responsibility of the provider client.
Atomic Agents tools are standalone components, so the scenario runs one through
its public `run()` method.

| Operation | Should be instrumented here | Status |
| --- | --- | --- |
| inference (`chat`) | No — delegates to the OpenAI client | ✅ Correctly not emitted |
| invoke_agent (internal) | Yes — `AtomicAgent.run` | ✅ Implemented |
| execute_tool | Yes — `BaseTool.run` | ✅ Implemented |
