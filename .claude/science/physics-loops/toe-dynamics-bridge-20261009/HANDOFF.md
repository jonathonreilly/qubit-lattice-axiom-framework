# Current recovery checkpoint

Regular review PR: [#9473](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/9473).
Branch: physics-loop/toe-dynamics-bridge-20261009. Original base:
17a95e60d85afc246fc7c163adef8869ab3f4194. Continuation begins at
b178e3a5d4c1d1301255596d10ac4e1bc2aeb192. Refreshed selection main:
d9b869b97944676aaa759915462c529dc276a04c; standing instructions:
3a4b2c66a1ead7a1c48b4359627e968f681e3c39.

The user requested continuing the next highest-leverage derivations. The missing
spatial composition has now been proved for a specified supplied model:

- Local particle transport/collisions converge to a nonlinear fixed-velocity
  kinetic equation on its explicit classical lifetime, with quantitative bounds.
- Marked position/velocity quantum jumps close populations for arbitrary
  coherences and give exact local count rates. A fresh-ancilla schedule has an
  explicit diamond error; the finite schedule has a recorded count-lumping
  counterexample that the approximation handles.
- A near-equilibrium stopped energy argument composes population, mesh,
  vanishing-amplitude and linear-fluid scales. One conservative simultaneous
  schedule gives O(delta) classical path error and O(delta^2) failure probability.
  The quantum transfer gives the analogous fixed-time measurement bound.

All three final arguments/runners have selective independent checks. No
consequential mathematical defect was found. Small endpoint/scope clarifications
and source identities are recorded in the three INDEPENDENT_REVIEW reports.
SPATIAL_SOURCE_IDENTITIES.json binds final sources, copied reports and raw
review evidence. SPATIAL_RUNNER_MUTATIONS.txt records 22 deliberate primary
mutations, all rejected. The three new canonical caches are ok/fresh.

The prior kinetic and graph-mixing notes/runners are unchanged from b178e3a;
their previous INDEPENDENT_REVIEW.txt and RUNNER_MUTATIONS.txt remain valid at
their recorded hashes. The new spatial model supplies the conditional bridge;
the old graph-slot model is not retroactively assigned a streaming coordinate.
The collision parent remains provisional/unaudited at the identified main.

Supplied physical choices remain: particle-register encoding, local instruments,
directed transport, collision rates, Gibbs/initial preparation, ancillary
resources, clock and schedule. This is a vanishing-amplitude linear-fluid limit,
not a nonlinear fluid theorem or empirical transport prediction. Next highest
leverage: derive a native carrier-to-population dynamics approximation with
quantified local decoding error. Lean targets are scoped in the notes; no Lean
execution, audit verdict or framework premise adoption is claimed.

Current stage: source, cache, graph and evidence-compatibility checks complete;
regular PR #9473 carries the continuation for independent integration.
No author merge is authorized. Exact source/evidence links are in this sole
current checkpoint pack. Original author drafts/raw reviews remain recoverable
in the task directory spatial_continuation; final proofs and checks are carried
in the branch. No editable prompt/skill or platform instruction was changed.

The dedicated worktree is used under the /pstack lock exception: root is the
sole repository writer, workers wrote distinct external paths. No shared-main
checkout was modified. The separate photon PR #9474 is unchanged. PR #9475
contains unrelated law-value work and supplies no premise here.
