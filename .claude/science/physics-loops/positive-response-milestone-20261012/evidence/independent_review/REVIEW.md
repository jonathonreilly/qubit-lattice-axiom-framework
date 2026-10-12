# Independent positive-response source review

2026-10-12. Reviewer: the existing independent `neutrino_candidate` agent,
same session for initial reading and correction confirmation. This report
does not infer a model configuration from an agent name; actual dispatch
metadata belongs to the coordinator's receipt.

**Source disposition: PASS WITH BOUNDED CLAIMS, for the three source files
below.** No remaining material mathematical, normalization, physical-scope or
runner error was found. The result is conditional mathematics for supplied
canonical free scalar dynamics, spectral measure, vacuum, profiles and
couplings. This is an author milestone review, not a formal audit, retained
status, empirical validation, or the coordinator's combined integration gate.

## Frozen source and complete scope

Author worktree: `/private/tmp/observations-positive-response-20261012`.
Base and reviewed `origin/main`: `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`.
All three assigned paths are new relative to that base; no prior content in
these paths was deleted or inherited. The full final note, runner and contract
were read. The runner has no local helper imports beyond these declared data;
its external numerical dependencies and versions are recorded below.

| Final source | SHA256 | Disposition |
|---|---|---|
| `docs/POSITIVE_MEDIATOR_FORCE_NOISE_AND_SOURCE_INVERSION_BOUNDED_THEOREM_NOTE_2026-10-12.md` | `0e5527ca53a44b9e081868d46793d7c827d08a960203ad74ed891a4747a1ec77` | Accept stated conditional theorem and explicit limitations |
| `scripts/positive_mediator_inverse_2026_10_12.py` | `8ca06b17acada71896f816825c80b3e2769c039d2cf9f5dfe5026e6c85f1feb9` | Accept fixed diagnostic contract, including corrected shape guard |
| `scripts/data/positive_mediator_inverse_2026_10_12.json` | `a359f8300f84e297d1a838e6e20a85d2267f0f14f50da74f73123a9a484b05db` | Accept as declared synthetic inputs, not observations |

Initial runner SHA256 was
`202fb03cf29836953f11fc4af7c6c5ea6cbf66c9bf8f42a66d976b6aa6b70790`.
The only correction adds an explicit rejection of `source_geometry.shape != 1`
before evaluating the specialized source kernel. The initial contract already
used one, so no reported numerical result changed. The correction was read,
diffed, executed and challenged in this same reviewer session. One minor
runner-contract finding, fixed; zero unresolved findings. No author files were
edited by this reviewer and no commits were made.

The coordinator later split the note's first combined `Date`, `Claim type`
and `Status` line into three lines so the graph extractor sees the declared
claim type. I confirmed that exact metadata-only diff in this same session;
the mathematical body is byte-identical. Its prior note hash was
`67ce5a832e6b1110700bd0cd184645f208e72bbec9c94194bce6e5716047836d`.
Previous source and receipts remain preserved. This adds no scientific finding
or change of claim strength. The coordinator regenerates the note-input-bound
cache; no new mathematical execution or mutation series is warranted.

The current axiom memo, registry and all three primitive source notes were
read along with applicable review-loop criteria at the reviewed main revision.
They do not supply the alternative action, state or measure used here; the note
correctly declares those as additional conditional physical premises. Earlier
`agents/gravity_finite/DERIVATION.md`, `SOURCE_PROFILE_INDEPENDENT.md` and its
receipt were read as provenance. Their older source coverage was not used as
automatic coverage of this final milestone. The final note contains the
needed proof rather than relying on those unpublished working notes.

## Consequential mathematics

The following checks reconstruct the mathematical chain, rather than treating
a passing runner as a proof.

1. With signature `(-,+,+,+)`, the supplied action gives
   `(partial_t^2 - Laplacian + mu^2) phi = J`, positive free kinetic energy,
   and retarded denominator `k^2+mu^2-(omega+i0)^2`. Its static Green function
   is `exp(-mu r)/(4 pi r)`. Coupling two charges gives the displayed attractive
   potential and inward-force factor `(1+mu r)exp(-mu r)` with the stated sign.
   Independent angular integration of the actual point-force projection
   confirms the spherical-shell force factor, including the massless and
   central-point limits.
2. The on-shell radial measure is `k^2 dk/(4 pi^2 sqrt(k^2+mu^2))`.
   Changing variable to frequency gives exactly `k d omega/(4 pi^2)`.
   The Gaussian occurs squared, as `exp(-a^2 k^2)`. As an independent factor
   check, the massless equal-time integral is `1/(8 pi^2 a^2)`.
   The gamma low-frequency beta-function coefficient is also correct.
3. For `s>0, N>=1`, the positive normalized Laguerre rule and monic norm give
   the Hermite bounds in equation (5). The force derivative is
   `t^(2N)[tx-(2N-1)]exp(-tx)`; its absolute supremum is `2N-1` times
   `t^(2N)`. The force error need not have a fixed sign. The pointwise
   remainder bound is integrable on the unbounded domain. The note claims
   finite-window absolute bounds, not convergence of that particular
   high-order bound at every fixed large radius.
4. For equation (6), the potential and force kernels have mass derivatives
   bounded by `R` and `R/e`. Matched tail masses give a difference at most
   `p`, not `2p`. Writing `F(u)=u exp(-a^2 u^2)` gives `|F'|<=1`, and
   `sqrt((omega^2-mu^2)_+)` is bounded in difference by
   `sqrt(2 omega |mu-eta|)`. These yield the stated midpoint noise bound even
   when a bin crosses a mode threshold. A tail atom strictly above `M` gives
   zero noise contribution for `omega<=M`. A finite first mass moment is
   unnecessary when an arbitrary tail atom is used. Normalization one is
   load-bearing for the displayed coefficients; scaling total weight scales
   the responses and bounds.
5. Ordered radial supports make the two positively tilted averages of
   `u coth(mu u)-1/mu` strictly ordered. Thus `F_C/F_M` strictly decreases
   with positive mass, and its value at zero is one. At strictly exterior
   radii, exponential separation supplies domination for differentiation,
   including arbitrary finite heavy-tail measures. The score
   `-r mu^2/(1+r mu)` strictly decreases on nonnegative masses. The
   independent-copy covariance identity therefore gives a strictly positive
   derivative for every non-singleton positive spectral measure, including
   one with a zero-mass atom. This yields `D<0` with the note's orientation.
   The displayed inverse has the correct source-fraction denominators.
6. An independent symbolic expansion of the two kernel columns through
   fourth order gives
   `D = -(a2_M-a2_C)(r2^2-r1^2)(E[mu^4]-E[mu^2]^2)/12 + higher orders`.
   Gamma moments give `2s(s+1)(2s+3)/ell^4`. Since the weighted matrix tends
   to two identical rows `(f_C,f_M)`, its largest singular value squared
   tends to `2(f_C^2+f_M^2)`; division by its determinant gives exactly the
   coefficient in equation (12). The fixed-support gamma tail justifies this
   asymptotic expansion. The first tabulated range is correctly evaluated
   exactly, not replaced by its inaccurate asymptotic approximation.
7. Expanding `0F1(;5/2;mu^2 R^2/4)` and integrating gamma moments gives both
   hypergeometric terms in equation (13). Separately integrating a shell over
   mass gives the `atanh(v)/v` and `1/(1-v^2)` expression. The mantle's volume
   subtraction and mass fractions have distinct, correctly applied roles.

There is no terminal lemma equivalent to the target left unproved in this
chain. The conditional mathematical proof closes under its hypotheses.
Adopting the action, spectral measure or source-current identification as
physics remains outside that conclusion.

## Actual execution and independent checks

The final author runner executes successfully: **10 check families passed,
zero failed**. The first actual run of the earlier runner and the final run
are both preserved. Source hashes were checked before and after execution;
the note at that execution has the pre-metadata hash recorded above, while
runner and contract bytes are final. Output reproduces the displayed response pair and
the condition numbers through `1.6004181665822e26` at `ell=1e13 m`.

The separate [independent checker](independent_checks.py) imports no author
helpers: **8 checks passed, zero failed**. It covers 24 direct angular-force
samples (largest absolute discrepancy `7.78e-62` at 60-digit precision), an
arbitrary ordered discrete core/mantle pair with a mass-zero atom, exact
single-mass/equal-profile/coincident-radius controls, direct-force charge
reconstruction, symbolic determinant and derivative checks, massless vacuum
normalization, and bin bounds on atomic and infinite-first-moment measures.
The nondegenerate discrete determinant is `-0.02571417369394395`; all three
degenerate controls give zero. Finite tests support the proof; they are not
interval-arithmetic certification of every printed digit or exhaustive tests
of every admissible measure.

The first independent symbolic run failed because this reviewer's sequential
substitution replaced the fourth moment by the squared second moment. The
failed code, stdout, result and correction explanation are retained under
runtime `independent_attempt_1/`. Simultaneous exact monomial replacement fixes
that checker error and confirms the source coefficient. It was not a source
finding and has not been erased from the evidence.

All ten author mutation source hashes and actual failure logs were checked.
Each exact mutation was then independently replayed on a local copy of the
final three-file packet: every intended check failed with nonzero exit status.
An isolated contract with `source_geometry.shape=2` is rejected by the new
explicit guard. These are adversarial sensitivity checks, not proof that a
finite test suite detects every possible code defect.

Runtime: Python 3.12.8, NumPy 2.4.1, SciPy 1.17.0, mpmath 1.3.0 and SymPy
1.14.0. Numerical threads were limited to one. The first author run used
about 85 MB peak child RSS and finished in under one second; independent
checks and each replay are similarly small. All raw stdout/stderr, source
snapshots, mutation copies, versions and receipts are preserved under
`neutrino/positive_milestone_review/` in the campaign runtime.

For portable reproduction, the coordinator subsequently requested removal of
only the review checker's fixed campaign runtime path, stop markers and expiry
guard. Original checker bytes and this report's original receipt are preserved
under runtime `portability_correction_original/`. The numerical code is
unchanged, and the portable checker was re-executed: **8 passed, zero failed**.
This checker correction did not alter canonical science. Supply
any writable new file path to `python3 independent_checks.py --output PATH`.

## Physical and integration limits

The common measure relates the stipulated static response, retarded response
and **specified vacuum** correlation. Static observations alone do not select
the state, spectral family, coupling normalization or apparatus current. Mass
decay does not regulate high spatial momentum. The profile, switching,
backgrounds and detector transfer remain necessary for an actual observable.
No temperature or classical-noise alternative is ruled out by this note.

The inverse requires known common measure, ordered normalized radial profiles,
mass fractions, nonzero known probe coupling and separation of the scalar
acceleration from other forces. Unknown probe coupling leaves product
degeneracies; zero differential probe contrast leaves no differential signal.
Finite exact rank gives no usable experimental precision by itself. The
table's enormous condition numbers depend on its parameter and row scaling;
noise whitening and source/nuisance uncertainty remain absent. The source
surface example is justified for gamma tails and is explicitly separated
from the general theorem's strict `r>R` domain.

The fixed runner is not a general validated source-inference API. Its source
example uses `s=1`; other shapes now fail explicitly. Its finite sampling and
floating arithmetic do not prove uniform error bounds, which instead rest
on the analytic arguments. No measured datum was fitted or used as a test.

Applicable review conclusions: code/runner PASS; proof CLOSED under declared
hypotheses; physical scope CONDITIONAL; imports DISCLOSED; no retained-grade
claim; algebraic content rather than a labeling convention; no broad no-go
claim requiring a separate route-exhaustion argument. Source-level
propose/ratify separation is clean. All four source-note links resolve.

Full pipeline, strict audit lint, changed-evidence readiness, final tree
inventory, current-main preservation and administrative-packet integration
remain coordinator responsibilities and were not run by this constrained
reviewer. No verdict, audit-state edit, GitHub action or landing was performed.
This source confirmation covers only the exact science bytes above and their
declared inputs. A changed source, premise, input or semantic interaction
reopens its affected conclusion.
