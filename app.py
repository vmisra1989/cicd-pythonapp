
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://elastic-apm-server.elastic-system.svc.cluster.local:8200/intake/v2/events",  # Replace with actual APM server URL
    headers={"Authorization": "Bearer SSXSDGSptEv05J0u67E5ew"}
)

trace.get_tracer_provider().add_span_processor(
    BatchSpanProcessor(otlp_exporter)
)

with tracer.start_as_current_span("minikube-span"):
    print("Hello from Minikube!")

