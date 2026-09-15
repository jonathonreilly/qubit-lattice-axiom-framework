---
claim_id: native_l6_nonlinear_star_vertex_note_2026-09-09
claim_type: bounded_theorem
claim_scope: "Supplied canonical U0 L6 model: the third-order singleton-star vacuum image has positive distance from the full 108-mode linear Majorana vacuum-action space."
upstream_dependencies:
  - native_dynamical_cycle_fermion_z2_dictionary_note_2026-09-08
  - native_zero_penalty_endpoint_note_2026-09-08
  - native_l6_sixth_prefix_gap_certificate_note_2026-09-08
  - native_third_order_star_vertex_note_2026-09-08
runner: scripts/native_l6_nonlinear_star_vertex_2026_09_09.py
---

# A nonlinear third-order star vacuum image on the native L6 torus

**Type:** bounded_theorem. **Status:** conditional-support.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: "Supplied full native U0 model, canonical L6 flux and physical parity, and stated floating-operation error model."
trace_class: frontier_discovery
reachability_to_target: unknown_frontier
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

The prerequisites are the [whole-carrier dictionary](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md), [U0 endpoint](NATIVE_ZERO_PENALTY_ENDPOINT_NOTE_2026-09-08.md), [exact L6 prefix denominator certificate](NATIVE_L6_SIXTH_PREFIX_GAP_CERTIFICATE_NOTE_2026-09-08.md), and [third-order star theorem, current reviewed source](NATIVE_THIRD_ORDER_STAR_VERTEX_NOTE_2026-09-08.md). The original branch used a pinned8058 snapshot; its mathematical body agrees with the linked current reviewed parent. The snapshot remains exactly recoverable as historical provenance, and the current parent is explicitly source-pinned.

## Statement and normalization

Fix the supplied uniform native Hamiltonian at U=0 on the periodic6³ torus, canonical pi-flux signs, Kij=-2t xiij, and the physical active parity. Let Ω be the normalized canonical active vacuum. Write χ=O0(E0)Ω for the third-order singleton-star active vertex, stripping the three powers of the electric coupling. Set |t|=1. The six incident insertions each contribute1/2; the resulting normalization is1/8. It is not the special L4 vacuum-linearity coefficient.

Let a1,…,a108 be the full canonical complex annihilation modes. Then the saved-candidate certificate gives the strict bounds

    0.001921920169 < inf_L ||(O0(E0)-L)Ω||² < 0.001921920178,
    0.04383 < inf_L ||(O0(E0)-L)Ω|| < 0.04384,

where L ranges over every linear Majorana operator on the full216-real-dimensional active carrier. The infimum is the distance to the full108-complex-dimensional one-particle vacuum-image space. The certified three-, five- and seven-particle weights are individually positive. No claim that all higher weights vanish is made.

These decimal endpoints are exact rational comparison targets, not rounded binary64 evidence. The primary compares them to the full rational interval in the accepted output. The canonical replay is a separate verification of saved candidates; it does not generate new solutions. The accepted original computation and independent replay already discharge the numerical premise; the proposed portable replay remains subject to its own source/resource review.

## Exact finite reduction and four solves

The canonical one-particle matrix is reconstructed directly on the216 vertices. With A=-K², its star-relevant spectral values are12,24,36,48. Apply the rational projectors ∏μ≠λ(A-μI)/(λ-μ) to the six signed neighbor coordinate vectors. The exact sector ranks are6,6,6,3. For every nonzero real projected vector r of norm d in sectorλ, pair r/√d with Kr/√(λd). They form42 orthonormal real directions, or21 complex modes. The center and all six neighbors lie in this span, as checked by the exact identity

    e_v = Σr r r_v/d + Σr Kr (Kr)_v/(λd).

This K-invariant space contains every changed-edge endpoint. Its orthogonal complement is unchanged and remains in its vacuum. Thus the reduction does not discard potentially excited bath modes.

In each of the first three sectors the adapted representation is A1g⊕Eg⊕T1u, and in the last it is A1g⊕Eg. The48 signed coordinate automorphisms fix the center and preserve K. Their exact exterior lifts fix Ω. The15 incident-edge pairs have two orbits:12 perpendicular pairs and3 opposite pairs. The frozen ledger specifies every representative-to-target map before solution data.

For an initial pair A let x_A=(H_A-E0)^(-1)Ω. For a last pair C let

    y_C=(H_C-E0)^(-1) γ0 Σ_{A disjoint C} x_A,    χ=(1/8)Σ_C y_C.

Each sum has six predecessors. A perpendicular C has five perpendicular and one opposite predecessor; an opposite C has four perpendicular and two opposite predecessors. Exact transport therefore requires only two x representatives and two y representatives. The ledger reconstructs12 first-stage source transports and15 final transports. The two negative resolvent signs in the original Feshbach expression cancel. In the real adapted implementation γ0=iB, so the stored source, second-stage and final real arrays carry a global physical factor i; first-stage arrays are real. Every saved real NPY is bridged bit-for-bit to interleaved complex raw data with this phase convention.

All relevant proper two-edge masks are covered by the imported exact prefix theorem, with H_mask-E0≥1/3 in the applicable parity. The inverse norm bound is3. This is a fixed finite-model input, not an assumed CG convergence rate or a spectral estimate from the candidate diagonalization.

## Fresh residual certificate

The four direct Gaussian candidates are arbitrary real binary64 vectors for certification purposes. Their SVD accuracy is not used to establish the theorem. For each saved vector x, independently reconstruct the original Hamiltonian action and a fresh residual against its saved source. Exact dyadic squared norms and explicit outward rational arithmetic bound the residual, including coefficient-enclosure error and floating-operation error. The active coefficients are independently reconstructed from rational projected columns and100-bit square-root intervals.

For a first stage the solution error is at most3ρ. At second stage the source-error bound is added once to the fresh residual before applying the inverse bound. Source bounds include each transported first-stage error, four Eg-block transport errors, addition error and center-Majorana error. The final bound includes12 perpendicular and3 opposite second-stage errors, all15 transport errors, sum error and1/8 scaling. The accepted result is

    ||χ-χ_hat|| ≤ Eχ < 0.00000000004825.

The floating certificate assumes binary64 round-to-nearest/ties-to-even, gradual underflow, the explicitly ordered separate operations and finite intermediates. It does not assume an eigensolver or BLAS accuracy guarantee. Same-process environment checks support this declared arithmetic boundary; they are not a theorem about arbitrary compilers or hardware. Full equations and exact constants are preserved in the bound source below.

For any orthogonal particle projector P, the reverse triangle inequality gives

    max(0,||Pχ_hat||-Eχ)² ≤ ||Pχ||² ≤ (||Pχ_hat||+Eχ)².

The scanner accumulates binary64 squares exactly with denominator2^2148, including the implicit top parity bit. The replay checks all odd buckets1,…,21, not only the three positive low buckets. Seven vectors, four fresh residuals,27 transports and nine exact norm scans are required by explicit coverage guards.

## Distance proof on all108 modes

Every linear Majorana vacuum action is a one-particle vector because annihilation parts kill Ω. Conversely every complex one-particle coefficient can be generated by a Hermitian real Majorana combination, using the two real quadratures per mode. Hence these images are exactly ran P1. Orthogonal projection gives

    inf_L ||χ-LΩ||² = ||(1-P1)χ||² = ||P_{≥3}χ||².

The state χ has no excited modes outside the21-mode invariant star space. Allowing all remaining87 complex modes in L adds orthogonal one-particle directions, so it cannot lower this distance. This proves the full-carrier statement rather than merely a distance within the reduced frame. A simultaneous Gaussian change of vacuum, operator and canonical basis preserves the statement. Arbitrary nonlinear dressings are outside its scope. If O0 is defined as a bounded full operator, this vacuum distance is also a lower bound for its operator-norm distance to linear operators; it is not an equality of operator distances.

Restoring |t| scales χ by |t|^-2 and the squared distance by |t|^-4 under the stated electric-insertion convention. The result neither evaluates the complete sixth-order operator nor rules out cancellations between its distinct middle sectors. It supplies no bulk limit, uniform-in-L nonlinearity, phase, deconfinement or Hamiltonian-selection conclusion.

## Evidence and execution boundary

The [accepted result](../outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/RESULT.json), [independent replay](../outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/INDEPENDENT_REVIEW.json) and [whole-run acceptance](../outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/accepted/ROOT_ACCEPTANCE.json) preserve the exact rational values and source bindings. The accepted attempt charged35.85 seconds including14 prior seconds and reached338542592 bytes whole-tree peak. The earlier CG memory failure remains a closed failed attempt; this direct architecture is separately preregistered evidence, not a silent retry.

The [vector manifest](../outputs/native_l6_nonlinear_star_vertex_2026_09_09_inputs/VECTOR_MANIFEST.json) binds compressed and uncompressed bytes for all seven NPY/raw pairs. The primary replays these candidates without solving or applying a new physical approximation. It verifies source bytes, exact geometry and coefficient inputs, raw phase bridges, fresh residuals, source reconstructions, final weights and rounded inequalities. The canonical isolated replay has180 seconds and384MiB; an external process watchdog enforces the whole supervisor/worker tree. The final capture receipt records actual execution; earlier accepted receipts remain historical evidence.

## Complete imported proof records

The following source proofs are included byte-for-byte and remain distinguishable from this note: [projection theorem](work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-projection-e801411de605cecc.md), [independent projection review](work_history/repo/review_feedback/pr8061-proof-sources/README.md), [adapted-frame construction](work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-adapted_frame-4eb81c02792f3306.md), [four-solve identity](work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-four_solve-eff578cafd7f48f7.md), [real sign convention](work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_sign-c2692f5746303191.md), and [full arithmetic envelope](work_history/repo/review_feedback/pr8061-proof-sources/kept/pr8061-proof-real_error-57d49d5cf78c0e3e.md). Historical words such as “candidate” or “unlaunched” in these preserved sources describe their original stage. They do not constitute current review authority or replace the full current replay and independent source review. The port author participated in the original candidate and packaging implementation; the independent replay and cold reviews retain their separate authorship.


## Current execution and historical provenance

The canonical default runner performs the full saved-vector replay under isolated Python, disabled bytecode and single-thread numerical libraries. It does not solve for new vectors. The accepted status fields and old receipts are historical integrity checks, not a current review verdict. The original8058 snapshot and projection cold review remain exactly recoverable in the [proof-source mapping](work_history/repo/review_feedback/pr8061-proof-sources/README.md); the linked current8058 theorem is the actual parent. The five linked mathematical proof fragments remain current scientific inputs, byte-identical to the originals.

[Canonical cache](../logs/runner-cache/native_l6_nonlinear_star_vertex_2026_09_09.txt).

## No-Go Discipline Gate

**N1 — Counterroutes.** ATTEMPTED — the full108-mode linear vacuum-action space is compared with the reduced21-mode computation using the explicit projection proof. ATTEMPTED — all odd particle buckets are retained rather than inferring linearity from a few low sectors. ATTEMPTED — source error is propagated once with the declared1/8 factor and global phase convention. ATTEMPTED — the87 complementary modes are shown not to lower the distance. ATTEMPTED — nonlinear dressings, omitted mixed channels and full sixth-order cancellations are outside the claimed obstruction. These are analytical/source controls and preserved historical attempts, not five new numerical campaigns.

**N2 — One obstruction.** The certified positive distance is one finite vacuum-image obstruction to a linear Majorana representation in the stated reference. The individual positive particle buckets are not independent universal walls.

**N3 — Premises.** The supplied finite canonical L6 Hamiltonian, physical parity, fixed-parity prefix gap and explicit floating-operation assumptions remain premises. The full-carrier projection and error-envelope mathematics are stated imports; no physical parameter is selected.

**N4 — Scope of support.** The prefix denominator theorem supports the four residual certificates. It does not by itself establish a nonlinear vertex or the full effective Hamiltonian.

**N5 — Actual coverage.** TOTAL8 counts terminal claims assertions. The subordinate replay includes7 full vectors,4 fresh residuals,27 transports and9 exact norm scans; those counts are not added to8. Full108-carrier projection is analytical, not an executed108-mode Fock-space enumeration. Larger volumes are unexecuted.

**N6 — Escapes.** Nonlinear state/readout dressing, a different reference or interactions, and full mixed-channel cancellation lie beyond this fixed-reference linear-image exclusion. No universal no-go or new-axiom necessity follows.

**N7 — Strongest remaining route.** The omitted mixed-middle sixth-order histories/channels (648 orders in the8058 decomposition) remain separate obligations. The singleton-star certificate does not preclude those routes.

**N8 — Historical resolution.** The finite L4 vacuum-linearity result does not imply L6 linearity. The explicit L6 projection and replay address that narrower uncertainty while preserving the original failed candidate-generation attempts as history.
