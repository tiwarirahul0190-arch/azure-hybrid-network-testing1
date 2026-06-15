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


---

## Remote State Planning

Currently using local state file.

Planning to migrate state storage into Azure Storage Account after core networking validation is completed.

Need to review:
- state locking options
- storage account access controls
- backup strategy