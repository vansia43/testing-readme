"""
Notifications Service Metrics
Emits metrics for notification delivery and processing.
"""
import os
from datadog import statsd

# Service configuration
SERVICE_NAME = "notifications"
ENV = os.getenv("ENV", "prod")
REGION = os.getenv("REGION", "us-east-1")

# REMOVED: Unused metric identified by Vantage cost analysis
# Last queried: >30 days ago | Related assets: None | Indexed volume: 7.5 MB
# Estimated monthly savings: ~$79
# def emit_notification_delivered(notification_type):
#     """Emit metric for delivered notifications"""
#     statsd.increment(
#         "app.notifications.delivered",
#         tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"type:{notification_type}"]
#     )

def emit_notification_queued(notification_type):
    """Emit metric when a notification is queued"""
    statsd.increment(
        "app.notifications.queued",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"type:{notification_type}"]
    )

def emit_notification_sent(channel, success):
    """Emit metric when a notification is sent"""
    statsd.increment(
        "app.notifications.sent",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"channel:{channel}", f"success:{success}"]
    )

def emit_notification_failed(channel, error_code):
    """Emit metric for failed notification delivery"""
    statsd.increment(
        "app.notifications.failed",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"channel:{channel}", f"error:{error_code}"]
    )
