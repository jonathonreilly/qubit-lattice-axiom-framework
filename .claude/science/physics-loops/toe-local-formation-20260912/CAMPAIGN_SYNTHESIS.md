# TOE derivation campaign: results and remaining connections

The campaign produced six review PRs containing conditional mathematical
constructions. Its strongest advances are a positive native star coefficient
with controlled low-energy behavior, an informative native Record instrument
with exact disturbance and energy formulas, and finite projector histories
whose first data event occurs at a fixed site under one explicit local content
law. These results do not yet form a connected TOE. No result in this campaign
forces an axiom change.

The authorized window is **2026-09-12 23:38:24 UTC to 2026-09-13 11:38:24 UTC**.
This synthesis was prepared during its final minutes. Actual completion and
continuation shutdown are recorded in [STATE.yaml](STATE.yaml) and
[HANDOFF.md](HANDOFF.md). The initial review used the requested Astra-low
readers; all campaign execution after design was personal, without subagents.
Analytical derivations led the work. Small exact calculations and deliberately
altered formulas challenged the derivations; they are author checks, not
independent scientific review.

Main was synchronized before design to
`cda8b1445e21b3908a0a520710e0dae57b7bc3a3` and again during finalization to
`b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf`. The latter change only advances the
audit dispatcher's date. Scientific inputs did not change. Milestone branches
remain based on the original main. Planning instructions were pinned at
`9cff766069e8f66b4cc5c36888b1e71600b8888e`; that separate branch was not merged.
Exact PR heads, source hashes, cache identities and worktree states are in the
[final source index](FINAL_SOURCE_INDEX.json).

The review covered the current axioms and approved primitives, decisive main
sources, an inventory of 74 open proposals and full primary reading of nine
selected proposals. It was a relevant-source review, not a transitive proof
audit of the repository or a review of every open proposal. The original
[campaign design](CAMPAIGN.md) preserves the selection and its limits.

## Reviewable results

All six PRs were open, non-draft and awaiting review at the final source
snapshot. None has been landed by the author or granted retained status.

| Review unit | Result under its stated hypotheses | Principal remaining premise |
|---|---|---|
| [PR 8084: finite feedback apparatus](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8084) | Explicit finite collision/battery resources and error control for the supplied native feedback model; failures and interleaved hopping are retained | Ready preparation, controls, clock and occurrence law are supplied |
| [PR 8085: exact Regge reduction and tensor transfer](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8085) | Exact finite Hessian reduction, source comparison and a positive tensor transfer kernel | Regge action, sign, restricted section, source and physical time identification are supplied |
| [PR 8086: positive native star and low energy](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8086) | Positive coefficient, one-particle infrared dominance and an operator estimate with energy projections on both sides | Specified full cubic free Hamiltonian, vacuum and defect/star construction; no full interacting phase |
| [PR 8087: growing formation and current](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8087) | An increasing finite-carrier family with permanent Records, supplied formation clocks and surviving protected hopping/current on controlled windows | Protected-edge Hamiltonian, current state, local program, fuel and clock are supplied |
| [PR 8088: projector histories with local Record laws](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8088) | Two explicit all-finite-horizon constructions; the second uses one local law for a fixed first-event data target | Quantum probabilities and preparations are programmed; physical calibration and causal implementation remain open |
| [PR 8089: informative native Records](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8089) | Protected native effects produce actual edge Records, with exact information, disturbance, current, energy and finite-history formulas | The effect/pulse and Born instrument are supplied; complete neighboring-Record factorization is not yet implemented |

### Positive native coefficient and low-energy control

For the specified nonlinear odd star, Ward identities, exact moments and
positive remainder bounds yield **7 < h² alpha < 330**. This replaces an
undecided scalar sign with an explicit positive bound in that model. The
one-particle spectral mass is

`mu_1([0,E]) = alpha² E³/(6 pi² h³) + O(E⁴)`,

while the higher odd sectors have an explicit `O(E⁹)` upper bound. A separate
operator argument controls `P_E (O_zeta - alpha g) P_E` by an `O(E^(5/2))`
remainder against the `E^(3/2)` leading norm, uniformly over the allowed soft
particle sectors. Both energy projections are essential. The estimates do
not control unrestricted high-energy leakage, an extensive sum of stars or
the interacting thermodynamic phase.

The earlier complete finite sixth-order return contains a linear infrared
pole proportional to `alpha² h(k)/omega(k)²`. This identifies a channel that
cannot be omitted. It is not, by itself, a fixed-coupling phase or a justified
resummation. The finite filled-state counterexample to global linearity
remains in the campaign evidence.

### Native matter information, disturbance and continuing formation

Let `E` be a full-carrier positive effect in the protected native algebra.
With a ready cycle `S`, Record readout `Z`, and

`a = (sqrt(E) + sqrt(I-E))/sqrt(2)`,
`b = (sqrt(E) - sqrt(I-E))/sqrt(2)`,

the explicit full unitary `U = a + b Z S` implements the decoded binary
Lüders instrument at the physical edge Record. Protected operators commute
with `Z,S`; the code intertwiner supplies the decoding. A generic protected
effect can have extensive support. The vertex-parity specialization has
bounded plaquette/star support, but its pulse is still an input control.

For contrast `kappa = sin(theta)` and `eta = cos(theta)`, the parity
instrument has effects `(I ± kappa B_v)/2` and nonselective channel
`c² rho + s² B_v rho B_v`. Incident currents attenuate by `eta`. Mean matter
energy changes by `-(1-eta)<H_inc,v>`, with absolute bound `6t(1-eta)`.
The full diamond-norm disturbance obeys the sharp information bound
`epsilon >= 1-sqrt(1-D²)` and this instrument saturates it when the code
contains both parity sectors. Conditioning can reweight total-number
sectors; sharp-number branches and the nonselective number distribution
are preserved. Even pure-Slater histories have an exact covariance update.

The final [assembly derivation](BLOCK20_ASSEMBLY_DERIVATION.md) adds explicitly
supplied absorbing fuel. Jump operators `L_ez = sqrt(gamma_e) K_ez a_e`
satisfy `sum_z L_ez† L_ez = gamma_e n_e` on the full carrier. Thus waiting
clocks can be matter independent while marks remain informative. On legal
ready branches,

`|mean E(T)-mean E(0)| <= 6t sum_e (1-eta_e) Pr(e forms by T)`.

The energy identity requires incoming-code compression: a nonzero
full-carrier cross term is retained in the checker. The bound prices mean
matter energy, not the controller or battery. Geometry-only activation can
retain its site process; mark-dependent activation need not. A complete
finite collision map uses a two-qubit environment, without claiming an
energy-conserving extension or a uniform finite-step approximation.

A final [instrument-precision derivation](BLOCK21_INSTRUMENT_PRECISION_DERIVATION.md)
controls the complete outcome-and-poststate map: changing a supplied pulse
angle by `delta` changes the instrument by exactly `2 sin(|delta|/2)` in
full diamond norm when both parity sectors exist. Adaptive history errors
telescope without dividing by rare-branch probabilities. Contrast error
`epsilon` has the sharp worst-case bound `sqrt(2 epsilon)` near a projective
endpoint. This distinguishes outcome-probability accuracy from physical
instrument accuracy; the controller and program decoder remain supplied.
The proof uses the pure-state diamond-norm characterization in
[Watrous, Theorem 3.51](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf#page=183),
with its finite-space hypotheses checked, and a 50-check exact matrix comparator.

### Local Record programs and finite quantum histories

The first construction uses empirical neighboring contents, supported copy
paths and a supplied trace-weighted occurrence kernel. It prepares `24N+16`
Records and finishes with at most `56N+16`; its first data locations depend
on the outcome, with later fixed terminals copying those commitments.

The second construction supplies a different fixed local law. A program
`X=(2+p)I+P` next to trigger `10I` makes the first event at a fixed data site
draw `P` with probability `p` and `I-P` with probability `1-p`. Elsewhere,
the law is empirical copying. Hermitian rank-one `P` supplies quantum
projector data. A physical bank and supported nearest-neighbor paths route
the program using prior Records only. This proves arbitrary finite binary
history trees with initial `2(2^N-1)+2N+8` and final at most
`5(2^N-1)+5N+8` Records. The law is fixed across horizons; preparations are
nested. It does not construct an infinite future from one finite preparation.

Supplied quantum conditional probabilities reproduce the declared quantum
cylinders, including complex and repeated projector histories and Bell,
product and no-signaling comparisons. This is a conditional representation,
not a derivation of Born probabilities. The second wing's program may depend
on the first wing's distant outcome; no spacelike causal implementation is
claimed. Program/setting metadata are not additional projector events of
the quantum state. Scalar rounding has an on-code data-history error bound;
an explicit off-code matrix perturbation makes the local output laws disjoint.
No general matrix-noise robustness is claimed.

## What still prevents a connected theory

1. **The native content-law interface.** For a fixed nonzero parity contrast,
   the native event probability depends on `m(h)=<B_v>_h`. On a finite or
   countable declared ready family it factors through the complete local
   Record condition exactly when `m` is constant on every equal-condition
   fiber. An uncountable family also needs measurable factorization. The
   abstract probability program supplies no physical native dictionary or
   mechanism that maintains this condition under hopping and conditioning.
2. **One Hamiltonian across growth and infrared analysis.** The protected
   graph of PR 8087 deletes candidate hopping edges. PR 8086 analyzes a
   different, full translation-invariant cubic Hamiltonian. Its infrared
   theorem cannot be transferred by identifying their notation. A common
   carrier with a proved spectrum/defect bound remains necessary.
3. **Selection and resources.** The successful models still supply event
   pulses, controls, ready states, rates and probability programs. Permanent
   Records and a finite unitary dilation do not select those ingredients or
   price their entire preparation and energy ledger.
4. **Reciprocal gravity.** Exact Regge reduction and positive transfer do not
   derive their source, physical clock, action sign or restricted section
   from native matter. A common source normalization and both directions of
   response remain open. The restricted nonlinear scalar-source failures
   are preserved; they are not failures of every geometry or matter source.
5. **Later physical identification.** An interacting phase, physical matter
   content, chirality/anomalies, limiting-speed universality and calibrated
   empirical predictions have not been derived here.

These are separate obligations. The final assembly proves a limited
compatibility result and explicitly leaves the other connections open.

## Axiom pressure and the next decisive work

No axiom was changed. The supplied scale, kinetic-isotropy and realized-state
primitives were respected; they are not relabeled as absent premises. They
also do not select a contingent probability tree, apparatus state or pulse.

The campaign establishes neither that the present axioms are sufficient for
observed physics nor that every model satisfying them fails. A failed
apparatus, a restricted scalar ansatz or an off-code instability rejects
only the corresponding construction or claim. Several constructive
same-axiom alternatives were explicitly developed. An axiom-forcing result
would need a necessary physical target and a contradiction covering every
allowed implementation under separately justified auxiliary assumptions.

The most useful next derivation is a **physical sufficient-condition
interface for PR 8089**. Specify one native preparation/control domain and
actual neighboring Records; prove that its parity mean is a function of
those Records through every allowed dwell and event. Otherwise exhibit two
reachable, positive-weight histories in that same domain with identical
complete neighboring conditions and different native probabilities. The
measurable-factor criterion gives a precise success or failure test. A
collision alone would not exclude a causal program route or different ready
family. [NEXT_DECISIVE_TESTS.md](NEXT_DECISIVE_TESTS.md) states the bounded
tests and their stopping conditions.

Next in rank is a common protected/growing Hamiltonian with analytically
controlled low-energy star response. The positive scalar and spectral proof
machinery now give a starting point; the changed graph must be derived
afresh. Reciprocal sourcing follows a common carrier, rather than treating
separate conditional matter and Regge results as an already connected model.

## Evidence and disposition

Nine primary milestone runners have fresh source-bound caches at the final
snapshot. Their checks use exact matrices, CAR constructions, symbolic
geometry, conditional histories and analytical bounds as appropriate. The
mutation packets show actual failed assertions after deliberate changes to
load-bearing formulas. Check counts overlap and are not an independent
confidence score. The separate 21-check assembly comparator represents its
abstract cycle algebra; it is not a new native spatial embedding.

Recovery paths preserve initial failures and corrections. Material examples
include the growing-current margin correction from `1/6912` to `1/8192`, the
radical-program equality bug, the uncountable measurable-factor qualification,
the on-code precision domain, and mutations that initially raised a library
exception before reaching the intended assertion. Their original sources
and outputs remain alongside the final results. No failed mathematical
claim was repaired by increasing a numerical tolerance.

Focused branch checks, changed Python compilation, source bindings, links,
vocabulary and whitespace checks were completed at each source milestone.
Independent source review remains pending. The exact combined current-main
integration pipeline, strict lint and changed-evidence ledger gate remain
pending before landing. The branch citation manifests must be regenerated
on the eventual combined integration state. No audit verdict was applied,
no science was merged into main, and no editable prompt file was changed.

The full campaign archive additionally retains original Markdown trailing
spaces and an end blank line in four pinned Block05 source snapshots. Those
bytes were left intact to preserve their source identity. The new synthesis
commit and the campaign diff excluding that source-snapshot directory pass
whitespace checks; [the diagnostic](CAMPAIGN_ARCHIVE_WHITESPACE_CHECK.txt)
records the distinction. This does not change the six source PR checks.
