# Firewall Testing Notes

## Current Testing
- spoke to spoke traffic inspection
- outbound filtering
- route propagation
- policy hit validation

## Observations

### Observation 1
Firewall logs delayed for few minutes during high traffic testing.

### Observation 2
Few sessions bypassed inspection before UDR update completed.

### Observation 3
Need to test application rule collctions separately from network rules.

## Next Steps
- enable diagnostic logs
- validate SNAT working
- test deny rule hit number