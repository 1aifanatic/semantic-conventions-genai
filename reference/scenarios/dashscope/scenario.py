"""Capture a real DashScope Generation.call against the local mock server."""

import json
import os

import dashscope
from opentelemetry.trace import SpanKind, StatusCode
from reference_shared import flush_and_shutdown, mock_server_host_port, reference_tracer, setup_otel


def main():
    tp, lp, mp = setup_otel()
    dashscope.base_http_api_url = os.environ["MOCK_LLM_URL"] + "/api/v1"
    model = "qwen-plus"
    messages = [{"role": "user", "content": "Say hello."}]
    host, port = mock_server_host_port(dashscope.base_http_api_url)
    attributes = {
        "gen_ai.operation.name": "chat",
        "gen_ai.provider.name": "alibaba.dashscope",
        "gen_ai.request.model": model,
        "server.address": host,
        "server.port": port,
    }
    with reference_tracer().start_as_current_span(f"chat {model}", kind=SpanKind.CLIENT, attributes=attributes) as span:
        span.set_attribute(
            "gen_ai.input.messages",
            json.dumps([{"role": m["role"], "parts": [{"type": "text", "content": m["content"]}]} for m in messages]),
        )
        response = dashscope.Generation.call(
            model=model, messages=messages, result_format="message", api_key="mock-key"
        )
        span.set_attribute("gen_ai.response.id", response.request_id)
        if response.status_code != 200:
            span.set_attribute("error.type", response.code or str(response.status_code))
            span.set_status(StatusCode.ERROR)
        else:
            choices = response.output.choices
            span.set_attribute("gen_ai.response.finish_reasons", [choice.finish_reason for choice in choices])
            span.set_attribute("gen_ai.usage.input_tokens", response.usage.input_tokens)
            span.set_attribute("gen_ai.usage.output_tokens", response.usage.output_tokens)
            span.set_attribute(
                "gen_ai.output.messages",
                json.dumps(
                    [
                        {"role": c.message.role, "parts": [{"type": "text", "content": c.message.content}]}
                        for c in choices
                    ]
                ),
            )
    flush_and_shutdown(tp, lp, mp)


if __name__ == "__main__":
    main()
