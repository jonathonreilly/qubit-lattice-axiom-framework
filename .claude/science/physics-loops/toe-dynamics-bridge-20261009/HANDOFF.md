# Current recovery checkpoint

Regular review PR: [#9473](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9473); open against `main`, not a draft.

Source base: `17a95e60d85afc246fc7c163adef8869ab3f4194`.
Standing instructions: `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`.
Branch: `physics-loop/toe-dynamics-bridge-20261009`.

Active objective: deliver regular review PRs for actual checked mathematical
progress toward microscopic-to-macroscopic dynamics. New math is authorized;
no author merge or retained-status audit is authorized by this work.

The source proves the second-corrector O(epsilon²) finite acoustic-time bound,
O(delta) linear diffusive-time Stokes/heat limit, exact constitutive coefficients,
and a finite nonlinear heat-flux witness. The microscopic note proves the
local quantum channel/counting/rapid-mixing theorem and factorial equilibrium.
The notes do not yet compose into a spatial microscopic-to-fluid limit.

Frozen SHA-256 identities, also checked by the independent reviewer:

- Kinetic note: `038e1ed6942d79720aa1dd7360d90f9fa1067016940ceb3554efeb99c21ed0c1`.
- Kinetic runner: `a02ce74dc191cd926fd85525eb863a9e1e3d0eda031e8baa5d21ed5a76142861`.
- Microscopic note: `b607e16371688f2d8d71268bd13d642f2ed8ed4f5e02332cd1eb3147b8d40c2a`.
- Microscopic runner: `1cd57938685e59608cfafcac1cfdecde5f28a9596c0b738ee971db1918368afb`.

The independent analytical review found no material defect. Its separate
checker has 24 passing checks; primary runners have 18 and 4 passing groups.
`INDEPENDENT_REVIEW.txt`, `independent_check.py` and `RUNNER_MUTATIONS.txt`
preserve review coverage, source identities, full independent logs and the
resolved initial-preparation instrumentation failure. Canonical cached stdout
co-lands with the source. No Lean or retained-status audit has been performed.

Next integration action: independent review/landing of the regular PR with
combined current-main validation. Next scientific decision: construct spatial
occupation/vacancy or multi-particle cells, velocity-dependent streaming and
local collision mixing, with an explicit relation between channel, mixing,
particle-count and kinetic scales. Then test a native carrier and nonlinear
thermal closure; the exact current heat-moment witness is 2/5. Do not infer the
missing interface from graph adjacency or globally mixed occupation counts.

Local scratch evidence is preserved outside the worktree under the task's
`research_evidence/` directory, with a path/hash recovery map. The self-contained
proofs and checked artifacts here are the review deliverable. The separate
photon reference-form continuation has its own branch and recovery packet.
