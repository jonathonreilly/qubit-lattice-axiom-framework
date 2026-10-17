# Source review of the calibration corroboration runner

## Finding

The source is consistent with its stated narrow role: exact local algebra and rational budget corroboration for the PR9667 preparation-calibration theorem. I found no formula/sign mismatch in its implemented checks against the pinned theorem and bookkeeping report. It is **not yet an integrated executable artifact**: its input declaration is intentionally a manifest-only placeholder, while verify_inputs requires at least one frozen file and complete declaration closure. The adaptation note correctly assigns final input binding, syntax/import checks, bounded execution, mutations and cache creation to integration.

This is a read-only source review. No runner execution, import, compilation, syntax check, mutation or scientific computation was performed. There is no new PASS count or independent proof of the calibrated output theorem. No source or previous report was changed.

## Exact source identities and exposure

All paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934/`.

| Source | Bytes | SHA256 |
|---|---:|---|
| calibration_runner_draft/preparation_calibration_2026_10_17.py | 10529 | 6605413b5a4ea701cd69c2d30cf426bafcae1543ca6c7cc14aaf8eff6304bf49 |
| calibration_runner_draft/ADAPTATION_REVIEW.md | 5747 | f3d3c3c64d4c9399e934cce1b2d71ea86589fcff035b8626e6194f90b76c2b28 |
| calibration_bookkeeping_independent_check/REPORT.md | 16796 | 20a59e0add0183e14237a59ae9b6b6b07f05e880fae629e73102c671e41e7c4c |
| preparation_calibration_publication_draft/THEOREM_NOTE.md | 23314 | 2ab90129937c61c3255db5c93dc9af838a6249d11a16628c674b919ab54d85f2 |
| preparation_calibration_publication_draft/SOURCE_IDENTITY_AND_DEPENDENCIES.json | 5510 | 339e47ec599b4d4979def5fabd24075cab5b48e6cfbddc56c9ff4dc94cd41777 |

The complete runner (238 lines) and adaptation note (91 lines) were read. The theorem, dependency inventory and this reviewer's bookkeeping report were read during the immediately preceding task and verified unchanged by hash here. Those verified reads were reused. The prior report pins the exact PR9667 canonical source at cbd23228ffb0b70f6b86f7d9ea03261fa6fb51f7, including its two original preserved bodies. No PR9668 formula or apparatus premise was used.

This reviewer authored the pinned bookkeeping report. The present check is therefore implementation source review against an already reconstructed analytical result, not a new independent mathematical check or blind/model-diverse review. Governing reviewer/workflow instructions remain the previously verified source revision. No inherited scientific executable or author output was opened.

## Implemented checks and their limits

### Local positive blocks and scalar retention, lines 105–131

The occupation, annihilation and creation matrices produce Q(h) by Kronecker products. The real outer-product construction has the correct one-excitation vector (0,1,sign(h),0) and |11> coefficient 2|h|. The complement uses 2|h|I-Q and the opposite exchange sign together with |00>. Its normalized trace is |h|, and both calibration endpoints scale the entire complement, including its identity coefficient. `outer` does not conjugate, which is appropriate for these explicitly real vectors.

The unequal values 3/7 and -5/11 test both signs and nonunit magnitudes. They are local examples, not a proof for every real hopping or a matrix construction of the full apparatus. The adaptation note states this limitation; the analytical Gram proof remains the quantified premise. The current checks do not establish spectra by a numerical eigensolver or pretend to do so.

### Projection, monotonicity and preserved counterexample, lines 133–154

Polynomial coefficients are manipulated exactly with Fraction arithmetic. From trace d and determinant -d(1-d), the discriminant is 4d-3d^2. Subtracting (3d-2)^2 produces 4(1-d)(3d-1), matching the complete-g monotonicity factorization. The separate real normalized vector (3/5,4/5) tests an actual projected-density difference and its determinant/discriminant. This independently constructed instance is useful corroboration of the matrix interpretation but does not replace the general purification/contractivity proof.

The squared comparison at d=2/3 against epsilon=1 correctly preserves the counterexample to monotonicity of the isolated projection term. Global sign reasoning, partial-trace contractivity and actual-deficiency ordering are explicitly left analytical. The code does not silently use the false projection-only substitution.

### Profiles, coupling endpoint and isolation, lines 156–179

The ramp/pulse coefficients match the theorem. Integration and polynomial differentiation are exact. The pulse endpoint values/slopes, ramp endpoint slopes, pulse midpoint value and derivative factorization match the stated profiles. The code uses equal ramp areas to account for the upward and downward ramps; for this exact ramp integral 1/2, the downward area is also 1/2. It does not construct or test a general changed downward schedule.

The embedded J and q0 match the exact source, and c,s,E0 are formed algebraically from that q0. kappa=10^-8 is the prescribed upper endpoint. The pin-positivity and positive coupling slope checks justify evaluating the affine Aiso ceiling at that endpoint, conditional on the analytical interval argument. Eight explicit edge magnitudes plus one pin reproduce the isolation norm and identity sums. No large matrix is allocated.

Global pulse maxima, global slope maxima and nominal supported preparation remain analytical premises. The midpoint and factorization checks alone are not falsely presented as an exhaustive global optimization.

### Pulse budgets, work and trace arithmetic, lines 180–208

The five pulse channels use areas (1/4,1/4,1/2,1/2,1/2) in units of pi, norms (2,1,2,1,1) and identity coefficients (1,1/2,1,1/2,1/2). Their sums give 11pi/4 and 11pi/8, consistent with the theorem. The non-strict zero-calibration check correctly uses `le`; replacing it with a strict inequality would fail at zero.

Peak load uses the maximum over the three disjoint windows, while work sums twice the peaks of every channel. The slew check correctly squares the positive 10pi sqrt(3)/3 bound. The rounded 9.001, 20.001 and 33.001 ceilings use eta=10^-5. The nominal sqrt(2)kappa contribution is compared by squaring positive quantities; the trace conversion retains the factor two, and the epsilon ceiling uses 9epsilon<10^-8 to justify the coarse 10^-4 contribution.

These are rational substitutions in the analytical Duhamel, work and channel/seed bounds. They do not compute unitary evolutions, establish the nominal runtime error, or prove g(epsilon)<=3sqrt(epsilon) by sampling. The source and adaptation note appropriately distinguish those roles.

### Resource and energy checks, lines 209–215

The expression for M is ceil(50T), and at the selected upper coupling it matches 5e17. The qubit formula matches 2M+6. Fourteen preparation channels are assembled as nine isolation channels plus the five listed pulse channels. The all-occupied clock expression counts two rails' M-1 bonds, each of expectation 2J, and four endpoint occupations, producing 4JM.

The runtime term `2*M+28` is an embedded previously derived count. The runner does not reconstruct its two-body/onsite decomposition, and `2*M+6` similarly uses the known qubit formula. These checks are accounting substitutions at the displayed endpoint, not an independent graph enumeration. The clock expression is only the clock part of the energy witness.

## Material coverage limits relative to the bookkeeping report

The following correct analytical formulas from the theorem/report are **not computed by this runner**:

1. The full expanded alpha_R, including source, vacancy, endpoint and emitter contributions.
2. The five separate pulse coefficients and nine separate isolation sensitivities in delta_theta under independently chosen xi_a. The runner verifies the aggregate 11/8 coefficient and isolation identity sum; permutations or compensating errors preserving those totals are not ruled out by that aggregate test alone.
3. Full E_good and E_bad, their exact difference, the cancellation of kappa d_c in that difference, or the mixture variance identity. Only the 4JM clock contribution is checked.
4. The literal source/old incident-load decimals or the decomposition 2M+12 two-body plus 16 onsite runtime blocks.
5. The complete full-space Duhamel theorem, correlated-seed lemma, nominal preparation/scattering theorem, output embedding, old-aging/scalar comparator, and all-state modeled-work identity.

These are coverage boundaries, not newly discovered defects in those formulas. The pinned analytical bookkeeping report covers items 1–4, and the parent/calibration proofs cover item 5. The adaptation note expressly says no whole-device operator or energy expectation is computed. Keep this division in the canonical evidence description. A summary calling this runner a full energy/variance or channelwise delta_theta verifier would overstate its tests.

## Input integrity and integration requirements

`read_regular` rejects absolute, noncanonical and parent-traversing relative paths, symlink files and symlink ancestors below the chosen repository root, and non-files. `verify_inputs` rejects duplicate or undeclared manifest rows, checks exact byte lengths/SHA256 values, and requires nonempty set closure against the literal declaration. These are integrity checks only.

The current AUDIT_INPUT_PATHS contains only the manifest path. Therefore a well-formed nonempty manifest cannot pass this draft without the declared integration step, and an empty manifest also fails. This is the expected unfinished placeholder, not evidence of a baseline run or an undisclosed failure. Root must expand the tuple with every frozen file and bind the canonical source, manifest and frozen evidence in its envelope. The manifest itself is not a frozen row; the external envelope must pin it and the runner.

The repository-root expression `Path(__file__).resolve().parents[1]` is suitable when the canonical file is directly under the repository's scripts directory. It does not automatically identify a repository from an arbitrary scratch layout. Execution and mutation staging must preserve that layout or deliberately adapt the root policy, and such an adaptation needs source review. The timeout constant is declared, not enforced inside this runner; the external envelope owns actual timeout/resource caps and their receipts.

By inspection, import defines constants/functions and imports only standard-library modules; the main guard contains the IO and execution. That supports the stated import-inert design, but no import/syntax test was performed here. Test predicates use explicit conditional raises, not `assert` statements, so Python optimization should not remove them; the intended python -O behavior still needs the actual integration run. The emitted largest dense dimension 4 matches the literal local matrices in the inspected source.

## Suggested mutation families

The adaptation note's proposed families are meaningful in the inspected source. The following focused set should run only later on scratch copies with source/output receipts and expected family-specific failure locations. No mutation result is claimed here.

| Family | Suggested change | Expected detector |
|---|---|---|
| Full local sector | Drop half of the |11> Gram term | Q Gram mismatch, including the sector absent in one-head-only checks |
| Complement/scalar | Use |h|I-Q instead of 2|h|I-Q; separately omit xi in scaled identity expectation | Complement Gram or scaled identity mismatch |
| Projection algebra | Flip the determinant sign; separately change the actual 2x2 difference's diagonal | Discriminant polynomial versus independent projector realization |
| Monotonicity/counterexample | Change 3d-1 factor; separately replace d=2/3 by zero | Factorization or retained squared counterexample |
| Profile | Change quartic coefficient 30 to 29 | Unit area or endpoint/factorization family |
| Isolation count | Remove one kappa*c edge | Explicit channel-sum equality |
| Pulse norm/identity | Change a norm 2 to 1; separately change a spectator identity 1/2 to 1 | 11/4 norm or 11/8 identity aggregate |
| eta=0 boundary | Replace the zero-calibration `le` call with `lt` | Exact zero boundary failure |
| Peak versus work | Double peak values after area tests; separately increase work's total-variation factor | Peak or work ceiling, without treating nonoverlapping peaks as simultaneous |
| Slew | Replace 10 by 12 in the squared expression | Squared 20 ceiling |
| Trace/error box | Drop factor two on trace-conversion LHS; separately increase epsilon to 10^-8 | Trace equality or seed squared ceiling |
| Counts/clock endpoint | Change nine isolation channels to eight; separately remove an endpoint occupation | Channel identity or 4JM equality |
| Integrity | Tamper frozen bytes, remove/duplicate/undeclare a row, or replace same-byte file/ancestor with a symlink | Failure before arithmetic, reported separately from mathematical coverage |

These mutations test the implemented families only. A mutation to an absent alpha_R, full energy or individual delta_theta formula cannot be credited as detected by this runner. If integration adds those formulas or tests, inspect that changed content separately rather than claiming the present review covers it. Mutations that change both sides of an equality consistently may preserve it; independent analytical reconstruction and the second construction in the local/projection families are still essential.

## Disposition and limits

The current source is suitable for the declared next integration steps with its narrow corroboration scope and unfinished input binding stated explicitly. No source fix is required by this review, and no successful execution is inferred. Freeze the integrated final bytes, check syntax/import behavior, run bounded baseline and family-specific scratch mutations, inspect complete outputs, then create the canonical cache/envelope. Those are remaining actions, not completed verification.

No W, Git state, checkpoint, runner, adaptation note, theorem, prior report, prompt or audit record was modified. The only output is this review. The source hashes above, rather than an unpinned later adaptation, delimit its coverage.
