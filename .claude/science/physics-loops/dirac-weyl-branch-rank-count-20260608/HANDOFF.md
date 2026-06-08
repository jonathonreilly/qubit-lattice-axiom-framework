# Handoff

This branch repairs the Dirac/Weyl conditional by changing the load-bearing
surface from physical label products to direct branch ranks.

What changed:

- Dirac count is now `2+2=4` across massive positive- and negative-energy
  branches.
- Weyl count is now `1+1=2` for a fixed chirality across massless positive-
  and negative-energy branches.
- R1/R3 spin and particle-antiparticle labels are retained as context only.

What remains open:

- Physical derivation of the Dirac equation.
- Physical Wick/sign selection.
- Parent inventory premises outside P4 numeric counts.
- Parent label wording as a physical interpretation bridge.

Recommended reviewer action:

1. Inspect the branch-rank proof-walk and runner updates.
2. Confirm the note does not claim physical label derivation.
3. If accepted, queue the row for re-audit; do not apply an audit verdict in
   this PR.
