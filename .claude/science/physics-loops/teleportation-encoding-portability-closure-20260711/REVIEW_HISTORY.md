# Review History

## Iteration 1 — fixes required

The physics/import review passed the bounded claim and found no hidden input.
Code/math review found that the first runner certificate derived its expected
totals from observed enumeration, allowed an empty survey to pass, and checked
the exact obstruction values only through aggregate maxima. Governance review
found the source `Type` phrase was not the canonical audit enum.

Fixes:

- compute expected totals analytically from the valid geometry list and compare
  every per-axis observed total;
- require nonempty coverage;
- certify zero restriction, `sqrt(2)` leakage, and both `1/4` projector defects
  on every non-last-axis case;
- normalize the source metadata to `Type: bounded_theorem` with an explicit
  proposed-status/audit firewall.

## Iteration 2 — pass with bounded claim

Focused code re-review confirmed default `1330/470/860` coverage, `860/860`
exact obstruction certificates, exit `0` for the default surface, and exit `1`
for an empty out-of-scope survey. Governance re-review passed the note and loop
metadata. Final consolidated disposition: code/runner `PASS`; physics boundary
`BOUNDED`; imports `CLEAN`; retention `BOUNDED`; labeling `PASS`; governance
`PASS`; no-go discipline not applicable. Independent audit remains required.
