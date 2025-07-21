
import json
import time
import uuid
import requests

# Configuration
USE_LOCALHOST = True  # Set to False to use the Kubernetes service endpoint

# Define the endpoint based on configuration
endpoint = "http://localhost:8200/v1/traces" if USE_LOCALHOST else "http://elastic-apm-server.elastic-system.svc:8200/v1/traces"

# Generate a sample trace payload in OTLP format (simplified)
trace_id = uuid.uuid4().hex
span_id = uuid.uuid4().hex[:16]
start_time = int(time.time() * 1e9)
end_time = start_time + 5000000  # 5ms duration

trace_data = {
    "resourceSpans": [
        {
            "resource": {
                "attributes": [
                    {"key": "service.name", "py-app": {"stringValue": "example-service"}}
                ]
            },
            "scopeSpans": [
                {
                    "scope": {
                        "name": "example-tracer",
                        "version": "1.0.0"
                    },
                    "spans": [
                        {
                            "traceId": trace_id,
                            "spanId": span_id,
                            "name": "example-operation",
                            "startTimeUnixNano": str(start_time),
                            "endTimeUnixNano": str(end_time),
                            "attributes": [
                                {"key": "http.method", "value": {"stringValue": "GET"}},
                                {"key": "http.url", "value": {"stringValue": "http://example.com"}}
                            ]
                        }
                    ]
                }
            ]
        }
    ]
}

# Send the trace data to Elastic APM
headers = {
    "Content-Type": "application/json"
}

response = requests.post(endpoint, headers=headers, data=json.dumps(trace_data))

# Output the response
print(f"Status Code: {response.status_code}")
print(f"Response Body: {response.text}")

