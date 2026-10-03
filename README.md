# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45"> OpenTelemetry GenAI Semantic Conventions

Semantic Conventions for Generative AI (GenAI), including spans, metrics,
and events for GenAI clients, MCP (Model Context Protocol), and
provider-specific conventions (OpenAI, etc.).

This repository extends the
[OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions)
with GenAI-specific conventions, using
[Weaver](https://github.com/open-telemetry/weaver) to manage dependencies
on the core semantic conventions.

## Schema URL

Use the schema URL of the registry that defines the emitted signal. GenAI
spans and metrics use the GenAI schema URL, including when they reference core
attributes such as `server.address` or `error.type`. The current development
schema URL and core dependency are declared in [the registry manifest](model/manifest.yaml).

Language maintainers should see [Generating language artifacts](docs/code-generation.md)
for packaging and versioning recommendations.

## Read the docs

The human-readable version of the semantic conventions resides in the
[docs](docs/) folder. Major parts of these Markdown documents are generated
from the YAML definitions located in the [model](model/) folder.

Reference implementations and their tooling live under [reference](reference/).
For the Python reference compliance matrix and per-signal support reports, see
[reference/README.md](reference/README.md).
For contribution guidance specific to that project, see
[reference/CONTRIBUTING.md](reference/CONTRIBUTING.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
