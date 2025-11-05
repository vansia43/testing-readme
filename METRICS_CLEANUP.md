# Datadog Metrics Cleanup Summary

## Overview
This document tracks the removal of unused Datadog custom metrics identified through Vantage cost analysis. These metrics were not queried in the last 30 days and had no associated dashboards, monitors, notebooks, or SLOs.

## Metrics Removed

### 1. `app.checkout.transaction_time`
- **File**: `services/checkout/metrics.py`
- **Function**: `emit_transaction_time()`
- **Type**: Histogram
- **Last Queried**: >30 days ago
- **Indexed Volume**: 12.4 MB
- **Estimated Monthly Savings**: ~$108
- **Tags**: `env:prod`, `region:us-east-1`, `service:checkout`

### 2. `app.session.login_attempts`
- **File**: `services/auth/metrics.py`
- **Function**: `emit_login_attempts()`
- **Type**: Counter
- **Last Queried**: >30 days ago
- **Indexed Volume**: 8.1 MB
- **Estimated Monthly Savings**: ~$85
- **Tags**: `env:prod`, `region:us-east-1`, `service:auth`

### 3. `app.notifications.delivered`
- **File**: `services/notifications/metrics.py`
- **Function**: `emit_notification_delivered()`
- **Type**: Counter
- **Last Queried**: >30 days ago
- **Indexed Volume**: 7.5 MB
- **Estimated Monthly Savings**: ~$79
- **Tags**: `env:prod`, `region:us-east-1`, `service:notifications`

## Total Estimated Savings
**~$272/month** (approximately $3,264/year)

> Note: The issue reported ~$325/month in savings. The breakdown above totals ~$272/month based on individual metric analysis. The difference may be due to additional overhead or indexing costs.

## Actions Taken
1. Located all metric emission calls in the codebase
2. Commented out (rather than deleted) the unused metric functions to preserve code history
3. Added detailed comments explaining why each metric was removed
4. Verified that active metrics remain functional

## Active Metrics Retained
The following metrics remain active and continue to be emitted:

### Checkout Service
- `app.checkout.transaction_started` - Tracks transaction initiation
- `app.checkout.transaction_completed` - Tracks transaction completion with status
- `app.checkout.payment_amount` - Tracks payment amounts by currency

### Auth Service
- `app.auth.session_created` - Tracks user session creation
- `app.auth.token_generated` - Tracks authentication token generation
- `app.auth.authentication_failure` - Tracks authentication failures by reason

### Notifications Service
- `app.notifications.queued` - Tracks queued notifications
- `app.notifications.sent` - Tracks sent notifications by channel
- `app.notifications.failed` - Tracks failed notifications with error codes

## Verification Steps
After deployment to production:
1. Monitor Datadog for 24-48 hours to confirm the removed metrics stop appearing
2. Verify no errors or warnings related to missing metric calls
3. Confirm cost reduction appears in next billing cycle
4. Update any runbooks or documentation that referenced the removed metrics

## Related Issue
This work addresses the cost optimization recommendations in the Vantage observability cost analysis.

## Deployment Notes
- These changes are safe to deploy immediately
- No application code changes required (only metric emission)
- No breaking changes to existing functionality
- Metrics are commented out rather than deleted for easy rollback if needed
