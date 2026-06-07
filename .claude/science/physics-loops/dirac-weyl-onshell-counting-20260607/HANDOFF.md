# Handoff

This stacked branch repairs the remaining Q2 source import in the Dirac/Weyl
dof bridge. It adds an executable finite-rank certificate:

- massive rest branch: `rank(gamma.p - m)=2`, `dim_C ker=2`;
- massive moving branch `(E,p,m)=(5,4,3)`: same rank/nullity;
- negative-energy branch: same rank/nullity;
- off-shell contrast: full rank;
- massless branch: two-dimensional Dirac kernel split one-and-one by chirality.

Keep the boundary: this proves the on-shell count, not the Dirac equation,
physical Wick rotation, or parent thermal inventory. Reviewer/auditor decides
any status effect; this PR edits no audit results.
