 """
Authentication Service Metrics
Emits security and authentication metrics for the auth service.
"""
import os
from datadog import statsd

# Service configuration
SERVICE_NAME = "auth"
ENV = os.getenv("ENV", "prod")
REGION = os.getenv("REGION", "us-east-1")

def emit_login_attempts(username, success):
    """Emit metric for login attempts"""
      statsd.increment(
          "app.session.login_attempts",
          tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"success:{success}"]
      )

def emit_session_created(user_id):
    """Emit metric when a user session is created"""
    statsd.increment(
        "app.auth.session_created",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"user_id:{user_id}"]
    )

def emit_token_generated(token_type):
    """Emit metric for token generation"""
    statsd.increment(
        "app.auth.token_generated",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"type:{token_type}"]
    )

def emit_authentication_failure(reason):
    """Emit metric for authentication failures"""
    statsd.increment(
        "app.auth.authentication_failure",
        tags=[f"env:{ENV}", f"region:{REGION}", f"service:{SERVICE_NAME}", f"reason:{reason}"]
    )
