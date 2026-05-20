
# VPN Testing

Current testing:
- site-to-site VPN
- route propagation
- intermittent failover behavior

Observed few packet drops during route updates.

Need additional testing after enabling BGP.


## Additional Observation

During failover testing, tunnel recovered successfully but few active sessions dropped.

Need to validate:
- session persistence
- route convergence timing
- firewall session handling

Testing done with simulated traffic only.
