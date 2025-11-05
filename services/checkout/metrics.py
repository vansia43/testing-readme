"""
Checkout Service Metrics
Emits performance and business metrics for the checkout service.
"""
import os
from datadog import statsd

# Service configuration
SERVICE_NAME = "checkout"
ENV = os.getenv("ENV", "prod")
REGION = os.getenv("REGION", "us-east-1")

def emit_transaction_started():
    """Emit metric when a transaction is started"""
    statsd.increment(
        "app.checkout.transaction_started",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}"]
    )

# REMOVED: Unused metric identified by Vantage cost analysis
# Last queried: >30 days ago | Related assets: None | Indexed volume: 12.4 MB
# Estimated monthly savings: ~$108
# def emit_transaction_time(duration_ms):
#     """Emit metric for transaction processing time"""
#     statsd.histogram(
#         "app.checkout.transaction_time",
#         duration_ms,
#         tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}"]
#     )

def emit_transaction_completed(status):
    """Emit metric when a transaction is completed"""
    statsd.increment(
        "app.checkout.transaction_completed",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"status:{status}"]
    )

def emit_payment_processed(amount, currency):
    """Emit metric for payment processing"""
    statsd.gauge(
        "app.checkout.payment_amount",
        amount,
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"currency:{currency}"]
    )
