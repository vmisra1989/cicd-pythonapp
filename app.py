
import time
import logging
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

# Configure logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

resource = Resource.create({
    "service.name": "pyapp",
    "service.version": "1.0.0",
    "deployment.environment": "dev"
})

trace.set_tracer_provider(TracerProvider(resource=resource))


# Set up tracer provider and exporter
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="elastic-apm-server.elastic-system.svc:8200",
    headers={"authorization": "Bearer Wl9sQ0xKZ0JWNlJDY3RrRTlvY0U6cWZ4X0lxX0dwQXE2TGptdkFNWEpnQQ=="},
    insecure=True
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

logging.info("Starting to send one span every minute to Elastic APM...")

# Loop to send one span every minute
while True:
    with tracer.start_as_current_span("example-span"):
        logging.info("Sent a span to Elastic APM via OTLP gRPC")
    time.sleep(60)

