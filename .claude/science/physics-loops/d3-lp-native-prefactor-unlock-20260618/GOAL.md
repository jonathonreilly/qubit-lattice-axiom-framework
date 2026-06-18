# Goal

Repair the audited-conditional D3 orbital-response decomposition source packet
without editing audit-owned surfaces.

The concrete blocker is that the D3 note used the standard Landau-Peierls
single-band formula and its `-1/12` spinless unit-flux normalization as a
theory input. This block makes the scalar dependency explicit and executable:
the D3 runner now imports the native-prefactor companion runner, checks its
symbolic residuals, and uses the returned rational for the D3 integral.

Independent review and audit still decide whether the companion packet and
the D3 consumer packet are accepted.
