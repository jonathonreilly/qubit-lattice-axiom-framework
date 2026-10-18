# Scale-ladder gravity probes (2026-10-17/18)

Probe workspace for the gravity rung of the scale ladder (PR #9702), from one session (Claude Opus 5.5).
Valid results are in open PRs #9708 (metric universality, common cone, fifth null direction, pullback
Newtonian rung) and #9714 (hidden curvature in orthoscheme carriers; the D4 cone and its conformal partner).
Everything here is supplied-model floating-point probe work, not reviewed.

- GOAL.md: the 12-hour goal and milestones.
- FINDINGS.md: findings F1-F18, including the corrections made along the way.
- scratch/: probe scripts. regge_generic.py is the generic Bloch Regge builder (Kuhn, barycentric, D4 cone,
  P1 scalar). Scripts expect the repo scripts/ directory on sys.path; some import the PR #9708 runner.

Open items: a carrier with no non-metric soft modes (or a lattice-diffeo-preserving local mass for them);
a site-matter Ward identity on the D4 cone; the mechanism of the exact Kuhn shell at b = 0; a proof of the
D4 graviton splitting law c^2 = [(1 - S2)^2 - 12 T]/144.
