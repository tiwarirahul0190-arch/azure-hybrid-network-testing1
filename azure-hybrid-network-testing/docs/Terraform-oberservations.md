# Terraform Observations

## Current State

Deployment currently using local state file only.

Need to move state storage to Azure Storage Account after testing completed.

---

## Issues Faced

### Authentication Timeout
Azure CLI session expired during terraform apply.

### Resource Naming
Hit duplicate naming issue during repeated deployment testing.

### State Drift
Few resources modified manually from portal during troubleshooting.

Need to avoid this moving forward.