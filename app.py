
import time
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
import logging
logging.basicConfig(level=logging.DEBUG)

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://elastic-apm-server.elastic-system.svc:8200",  # no http:// prefix for gRPC
    headers={"Authorization": "Bearer N3Rha0daZ0J5Z0RILVBja1d1Z3Q6U1NYU0RHU3B0RXYwNUowdTY3RTVldw=="},
)
print("Using OTLP endpoint:", otlp_exporter._endpoint)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

with tracer.start_as_current_span("example-span"):
    print("Sending trace to Elastic APM Server directly via OTLP http")

# Keep the app alive
while True:
    time.sleep(60)

