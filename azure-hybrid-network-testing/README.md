
# Azure Hybrid Network Testing

Repository used for testing Azure hybrid networking, routing validation, VPN failover scenarios and Terraform-based infrastructure deployment.

Main focus areas:
- Hub-spoke topology
- Azure Firewall routing
- VPN gateway testing
- UDR validation
- NSG testing
- Terraform deployments
- Basic firewall automation

Some configurations are intentionally simplified for isolated testing scenarios.

---

# Current Environment

| Component | CIDR |
|---|---|
| Hub VNet | 10.0.0.0/16 |
| App Spoke | 10.1.0.0/16 |
| DB Spoke | 10.2.0.0/16 |
| VPN Gateway Subnet | 10.0.254.0/24 |

---

# Testing Scope

## Networking
- VNet peering
- Route propagation
- Forced tunneling
- Effective route validation

## Security
- NSG filtering
- Azure Firewall routing
- Traffic segmentation

## Connectivity
- Site-to-site VPN
- Failover behavior
- DNS resolution

## Automation
- Terraform deployment testing
- Firewall backup automation
- Route validation scripts

---

# Issues Observed During Testing

## Routing Issue
Traffic bypassed firewall due to route table attached to incorrect subnet.

Initially checked NSGs and firewall logs before validating effective routes.

---

## DNS Resolution Issue
Custom DNS server missing forwarder entry for spoke network.

---

## VPN Instability
Tunnel was established but intermittent traffic drops observed during route propagation updates.

Still testing this behavior.

---

# Planned Improvements
- Azure Bastion
- Firewall Premium testing
- BGP route testing
- GitHub Actions
- Multi-region failover
- Private DNS zones
- Terraform remote state testing
- Storage account access validation


