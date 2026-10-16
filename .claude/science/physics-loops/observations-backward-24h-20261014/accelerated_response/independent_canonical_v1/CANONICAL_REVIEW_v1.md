# Canonical M6 source correspondence and complete scoped check

Reviewer `/root/force_energy_bridge_check`; root remains scientific author.
This is a focused complete reading of the seven-file canonical scientific unit,
not a formal audit, a new independent derivation, or publication/landing approval.
No author source, branch, index, lock, campaign state or external observation was
modified. All new review files are confined to `independent_canonical_v1`.

**Result:** no unresolved mathematical or implementation discrepancy was found
in this source unit at the identities below. The retained qualifications are
material: the construction is conditional on the supplied field/action,
trajectory, clock and ideal link models. It does not establish an empirical
scalar residual, an energy upper budget, actual calibration, a selected state,
a positive-mass accelerated theorem or a TOE.

## Exact reviewed unit and execution evidence

All seven files were read completely. Their current hashes match
`CANONICAL_SOURCE_FREEZE_v1.json` and the fresh canonical runner summary:

| Canonical source | SHA-256 |
|---|---|
| docs/SCALAR_ACCELERATED_COHERENT_COUNT_BOUNDED_THEOREM_NOTE_2026-10-15.md | 72113d39011cd2a29beb3355edae2d122549f0369769fdb59b51594f48a9e711 |
| scripts/scalar_accelerated_coherent_count_check.py | b03883fbaafd9adc1bf7a849051ffa35c9dbd233c925e798f555f60eabfef7b9 |
| scripts/scalar_accelerated_gram_controls.py | 49a1ac95f7126e1c83aabecf009e0d5947ad92039f9caa9e352441fe12e1376d |
| scripts/scalar_proper_count_controls.py | 9f141f9048fcc75b00d83164fbf3c2d58f70db3d3db12d187ebe57cbbf5c528d |
| scripts/scalar_count_adjoint_controls.py | 0c4576f8dee284d8dfa6bd01fc72d50f30a2a0f5a570b390323ab954fb52876f |
| scripts/scalar_coherent_count_controls.py | e72e5c4a71068beddbd6933a7cba0d41f60e909cb45a11b742aa25f7a57c4c1a |
| scripts/scalar_coherent_exact_energy_controls.py | 6925adf6599f7df586810b4b6e7bae61368399953edb2a517cd492b3d422dc2f |

The runner cache hash is
`96b0ba40a1f81a4d9251fb65aaafbf2b6d6cdb1163f17a33925f682e89c2a54c`.
I recomputed the declared-input fingerprint from the repository's documented
length-delimited byte scheme, obtaining
`48819f0cd3f6f011b4d4523a0d30e15f278503ad46528b920303b31f03759bb0`,
matching the cache. Its source identity matches the primary runner; its JSON
stdout equals the saved summary; stderr is empty. Recorded exit code is zero,
elapsed time 22.59 seconds, and timeout 180 seconds. All six scripts declare the
same 180-second cap.

Each product's bytes match its hash in the summary. Every scientific result
value is identical to the corresponding frozen working result after excluding
only source/helper hashes, timestamps and context/status metadata. The count is
15 Gram controls + 9 proper-endpoint controls + 22 one-way adjoint controls +
14 coherent-link controls + 15 exact composition controls = **75 author controls**.
These were not rerun by this reviewer. This is identity/freshness validation and
result correspondence, not 75 new independent numerical executions.

## Scientific adaptation check

I independently generated the five complete working-to-canonical diffs. For
each helper, every non-entry scientific function has an identical Python AST.
The calculation bodies of working `main` and canonical `run_checks`, before
result assembly, are also AST-identical. This covers formulas, fixtures,
quadrature resolution, finite-difference steps, rank thresholds, assertions and
tolerances, rather than relying on a prose claim that adaptation was harmless.

Changes are the declared timeout, helper filenames, entry function names,
returning result dictionaries, removing timestamps and local result writes,
and printing returned results in direct execution. The Gram helper additionally
renames its result context from a `status` string to `check_context`; no numerical
calculation changes. The new primary runner orchestrates these five helpers,
writes their products under the requested output directory, hashes all seven
scientific sources and records the disclosed conditional scope. It reads no
external scientific input or observation.

One historical provenance mismatch was reported to root: the original
`CANONICAL_ADAPTATION_v1.json` lists the intermediate Gram helper hash beginning
`e4e5f494`, while the final source freeze and cache correctly bind `49a1ac95`.
The final exact diffs and source hashes in this review resolve which code was
checked. The old adaptation file should remain historical, with a final
identity supplement if it is used as current delivery evidence. This does not
invalidate the correctly bound final source or cache and is not a mathematics
failure. The current review does not rewrite that author-owned record.

## New self-contained proof paragraphs

The supplied test-body action -m integral A sqrt(1-u^2) ds yields
d_s(A gamma u)=-grad A/gamma. Inverting the resulting velocity rank-one matrix
gives -(1-u^2)[grad log A+u partial_s log A], with the partial derivative at fixed
position. The added paragraph is correct and keeps the distinction between this
coordinate force and an independently specified proper/external force. It does
not derive the action itself. The nonlinear synthetic external-force source
implements the particular additive coordinate prescription declared by the note.

The real positive-frequency convention is consistent. The explicit conjugate
already imposes reality, so a(k) remains arbitrary complex; an additional
a(-k)=conjugate(a(k)) restriction would be incorrect here. The two initial-data
terms give norm squared 4 integral |k|^2 |a|^2. Real duality consequently gives
the radial/angular factor (2pi)^(-3) for the squared response coefficient.
Half-line Parseval for the real arrival coefficient then gives 1/(8pi^2),
matching the joint Gram. No factor two or rest-frame energy substitution is
introduced by the new paragraph.

For the bounded finite real-Hilbert observation map B, G=BB* is positive
semidefinite and range(G)=range(B). Thus feasibility requires r in range(G),
and B*G^+r has squared norm r^T G^+r. Orthogonal kernel decomposition proves
E_min=r^T G^+r/2, since the Hilbert norm is 2E. The minimum is in the stated
energy completion; smooth compact initial data are the dense defining class,
not a separately proved exact-attainment class. A pseudoinverse without the
range condition would not prove feasibility. The canonical paragraph includes
that condition and keeps errors/nuisance in the residual before applying it.

The calibration/nuisance leakage statement is also correct: if
C_hat^T t=0, the actual leakage is t^T(C-C_hat)theta, bounded by
M||(C-C_hat)^T t|| only when ||theta||<=M is supplied. A nonzero modeling error
does not give a uniform cancellation for unbounded unknown amplitudes. This
qualification properly prevents floating nullspaces from being promoted into
an exact observable cancellation for real tracking data.

## Full proof and code correspondence

### Proper endpoints, clocks and adjoints

The one-way endpoint equations retain both proper-clock variations, the
receiver-coordinate displacement at fixed proper labels and the retarded
emitter position. The normalized count denominator is a fixed proper interval.
The augmented state contains position, velocity and proper clock with the
correct -A_b gamma u velocity-to-clock row, alpha force injection and alpha ell
direct-clock injection. The code's rows touch positions/clocks only and keep
their distinct coordinate event times.

The backward jump sign, terminal T+ convention and explicit initial-atom
qualification match the independently frozen adjoint derivation. Initial-state
and instrument contrasts use the full actual column span. With L2 distributed
readouts and bounded dynamics, position/clock atoms do not jump the velocity
adjoint; final zero and exact initial-state cancellation give zero force traces.
Thus W is compact H1 and c is compact L2. The velocity-atom exception remains
explicit. The previously missing L2 premise is retained in the canonical note.

The b0 column is derived from the direct clock weights. It correctly measures
the response to a spacetime constant scalar perturbation, which gives no force.
The code constructs it from the adjoint and checks it against a constant-forcing
forward solve. My earlier post-source closed clock calculation matches the
working column to 5.15e-15 and carries over because the scientific source and
result values are unchanged. The canonical 3.24e-8 summary now matches the
stored 3.241919514954966e-8 floating residual. Exact b0 cancellation removes
observable sensitivity, not the background value or a physical initial state.

### Accelerated common-field Gram

The phase map s-n.x is monotone under the uniform timelike margin. The compact
H1 force coefficient and L2 direct coefficient generate H=S-partial_tau R.
Its relative sign, normalization, acceleration derivative and common-arrival
cross-path summation agree with the original independent massless derivation.
The canonical helper calculates the original laboratory wave amplitude
separately from the transformed density and includes discriminating wrong-sign,
omitted-acceleration and incorrect multipath controls.

The sufficient b and b' estimates, Minkowski envelope and shared energy budget
are consistent. The explicit velocity-bump counterexample is a valid C2 path:
velocity and acceleration vanish at its joins. Its window derivative lives on
stationary ramps and its acceleration contribution on the moving plateau, so
the missing positive term cannot be absorbed by an instantaneous W'-only
formula. This rejects the proposed substitution, not scalar dynamics generally.

The anchored homogeneous-H1/L6 domain and alternative exact constant-response
quotient are both stated. No arbitrary pointwise trace is presumed on all
finite-energy fields. No accelerated positive-mass extension is claimed.

### Ideal coherent composition

The multileg recurrence has the correct preceding-leg product order. Repeated
visits to one body use one shared state and clock. The exact ideal instantaneous
phase multiplier explains the absence of an intermediate spacecraft oscillator
row; the additional clock-independent external dynamics explain why its direct
clock adjoint remains zero. These are explicit premises. They do not remove
the spacecraft position or force response.

The coherent helper retains the station clock at separate emission/reception
times, both body force responses, the composed light-time factors and proper
count normalization. Its nonlinear controls use the same declared dynamics and
shared clock model; their finite-step convergence is not an empirical or uniform
nonlinear error certificate. Clock-dependent controls, noncoherent electronics
or finite delays would need another response operator, as the note says.

### Exact stationary count-to-energy fixture

The stationary phase expression, moment cancellation, compact triangular force
weights and direct clock derivative are mutually consistent. The spacecraft
arrival shift is -Lz relative to its coordinate window and must remain in the
common phase amplitude. The canonical exact helper integrates interval overlaps
and original harmonic endpoint-pair absolute separations independently.

Both yield

    G = [[3064,-1871],[-1871,3064]]/(1620 pi).

The positive eigenvalues 1193/(1620pi) and 4935/(1620pi) agree with the independent
report's equivalent 1193/(1620pi) and 329/(108pi). The independent exact report
also checks the original forced-body/clock/null-leg integral rather than only
reusing the compact weights. Its exact matrix and scope match the canonical
fixture. The omitted-clock and equal-coordinate variants have the displayed
nonzero rational differences. This fixture avoids numerical-nullspace ambiguity
for its exact stipulated model; it does not certify an accelerating data design.

## Reused independent evidence and preserved limits

I read the original reports themselves, not only a status summary:

* `independent_massless_v1/INDEPENDENT_REVIEW_v1.md`: 18 pure-force and 27 joint
  controls with prior independent derivations; scope is massless prescribed-path
  mathematics, not a count model.
* Its `AUTHOR_SOURCE_COMPARISON_v1.md` and `V3_AFFECTED_CONFIRMATION_v1.md`:
  source correspondence, 38 narrow implementation checks, and the constant-
  offset/L2 qualifications; no transfer to massive or empirical claims.
* `independent_massless_v1/COHERENT_TWO_LEG_REVIEW_v1.md`, exact hash
  `2347cde604f7b7d7b31523fb28d107053b3670a51d36ff8e7db8661f81b34aa0`:
  61 exact/synthetic controls for the specific stationary coherent Gram.
* `independent_proper_count_v1/PROPER_COUNT_REVIEW_v1.md`: 179 independent
  proper-count/clock/dynamics controls; its general metric probes are kinematic
  controls and are not all KG energy states.
* Its `COHERENT_REVIEW_v1.md`: 150 independent coherent transfer controls,
  including shared-clock and intermediate-clock distinctions; no Gram claim.
* This reviewer's unchanged independent adjoint report and two source
  correspondence reports: 163 pre-source synthetic adjoint controls and 53
  explicitly post-source composition checks, with their actual exposure recorded.

Their hashes are recorded in `CACHE_AND_EVIDENCE_CHECK_v1.json`. None of those
counts is presented as independent observations or rerun here. Report scopes
are combined only where the canonical sources and assumptions are unchanged.
Preserved author/reviewer failures remain in their original records, including
quadrature resolution, finite-difference truncation, serialization and two
arbitrary signal thresholds. No failure was silently converted into success.

## Delivery boundary

The proof is self-contained at the level of its displayed premises; prior
campaign notes are provenance rather than unmerged authority used to fill a
missing proof step. The primary explicitly reports conditional-support and
zero observational tests, fits and physical energy estimates. Boundary cases
alpha=0, empty contrast space, singular Gram/range, lightlike limits, velocity
atoms and uncertain calibration are retained.

The meaningful result is a derived finite-count response and a checked
massless energy operator under the supplied model. The remaining physical
suppliers are openly listed. Mutation, packet, publication and landing checks
remain with root and the separately assigned review scope. This report does
not apply an audit verdict or authorize framework promotion.

Exact source copies, complete independent adaptation diffs, canonical output
copies and manifests are in this directory. `CANONICAL_REVIEW_IDENTITY_v1.json`
binds the full reviewed artifact set and this report.
