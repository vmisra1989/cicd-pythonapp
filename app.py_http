
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
resource = Resource.create({
    "service.name": "py-app",
    "service.version": "1.0.0",
    "deployment.environment": "dev"
})

from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import logging
logging.basicConfig(level=logging.DEBUG)

from opentelemetry.sdk.resources import Resource

resource= Resource.create({
"service.name": "py-app",
"service.version": "1.0.0",
"deployment.environment": "dev"

})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://elastic-apm-server.elastic-system.svc:8200/v1/traces",  # no http:// prefix for gRPC
    headers={"Authorization": "Bearer Wl9sQ0xKZ0JWNlJDY3RrRTlvY0U6cWZ4X0lxX0dwQXE2TGptdkFNWEpnQQ=="},
)
print("Using OTLP endpoint:", otlp_exporter._endpoint)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

with tracer.start_as_current_span("example-span"):
    print("Sending trace to Elastic APM Server directly via OTLP http")


with tracer.start_as_current_span("example-transaction", kind=trace.SpanKind.SERVER) as span:
    span.set_attribute("http.method", "GET")
    span.set_attribute("http.url", "/example")
    print("Sending trace to Elastic APM Server directly via OTLP http")


# Keep the app alive
while True:
    time.sleep(60)

