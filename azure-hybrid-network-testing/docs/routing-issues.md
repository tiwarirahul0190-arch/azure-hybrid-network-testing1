
# Routing Issues Observed

## Issue 1
Traffic from app spoke was bypassing firewall.

Cause:
UDR associated with incorrect subnet.

Fix:
Re-associated route table and validated effective routes.

---

## Issue 2
VPN tunnel up but no traffic flow.

Cause:
Missing return route from on-prem firewall.

---

## Issue 3
DNS resolution inconsistent between spokes.

Still investigating if issue related to custom DNS forwarding delays.
