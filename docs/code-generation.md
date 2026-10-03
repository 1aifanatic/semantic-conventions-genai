# Generating language artifacts

GenAI semantic conventions have their own versioning and schema URL. Language
maintainers should generate a separate GenAI artifact rather than add these
definitions to an artifact versioned with the core semantic conventions.
The package name and distribution mechanism can follow the language's existing
conventions.

This guidance records the recommendations in [#247](https://github.com/open-telemetry/semantic-conventions-genai/issues/247).
The [federated schema proposal](https://github.com/open-telemetry/opentelemetry-specification/pull/4815)
describes registries, dependencies, and schema URLs.

## Registry and dependency versions

Use [model/manifest.yaml](../model/manifest.yaml) as the entry point for
generation. It identifies this registry's schema URL and pins the core semantic
conventions dependency. Resolve that dependency when generating definitions
that reference core attributes.

Publish the GenAI artifact on its own release schedule. Document which registry
revision and core dependency produced it, so users can reproduce the generated
definitions and compare changes. A core artifact version does not identify a
GenAI registry version.

Where the language supports dependencies between generated artifacts, reuse
core definitions through that dependency. Follow the language's compatibility
and version-resolution rules; do not silently overwrite a core definition with
a second generated copy.

## Schema URL

Expose the GenAI schema URL separately from the core schema URL. Instrumentation
emitting GenAI spans or metrics uses the GenAI schema URL, even when those
signals also carry core attributes such as `server.address` and `error.type`.
Choose the URL by the signal definition, not by individual attribute names.

Take the URL from the registry revision used for generation. Do not substitute
the core dependency's URL or invent a release URL from the language package's
version. The manifest's development URL identifies development conventions;
it is not a promise of a stable release.

## Migrating from core-generated constants

Older core artifacts may still contain deprecated GenAI constants. They can
support instrumentation that continues to implement that older convention
version, but they do not cover attributes added or renamed in this registry.

Before switching artifacts, compare the emitted attribute names, signal
definitions, and schema URL against the targeted GenAI revision. A matching
constant name alone does not establish compatibility. For example,
`gen_ai.usage.cache_creation.input_tokens` was renamed to
`gen_ai.usage.cache_write.input_tokens`; continuing to import the old constant
does not implement the new convention.
