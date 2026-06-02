# Reality Favors the Signed Readout, and Is a Shared Mechanism (Not a Shared Object) With the Records-Side U = I

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_reality_favors_signed_shared_mechanism.py`](../scripts/frontier_koide_reality_favors_signed_shared_mechanism.py)

## Context

Two open pins of the charged-lepton program were conjectured to converge under
one principle: the records-side `U = I` (no relative branch phase, needed for
transfer positivity -> CAR; companion note
`KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED...2026-06-02`) and the value-side
signed-vs-singular Koide readout (the Brannen/det_R closure needs `sqrt(m)` to
be SIGNED). The conjecture: a CPT / reality condition on the emergent-time
generator forces both. This note records what is actually true.

## Claim

The reality of the emergent-time generator
(`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`,
**retained_bounded**: the staggered hopping `D` is real anti-Hermitian, so
`H = iD` is Hermitian) **places the native Koide mass operator on the SIGNED
side** of the readout dichotomy, and is the SAME structural mechanism that would
force the records-side `U = I` -- but the two act on DIFFERENT tensor factors
(generation `C^3` vs site qubit `C^2`). So it is a shared **mechanism**, not a
single shared **object**: one reality principle favors the signed readout but
does not collapse both pins into one discharge.

### A. Reality makes the spectrum real and signed

The Koide mass operator is the circulant `H = a I + b C + bbar C^2 = iD` on the
generation triplet. For real `a` it is Hermitian (the reality of `D`), with real
signed spectrum

```text
lambda_k = a + 2|b| cos(theta + 2 pi k/3),   which can be negative.
```

(verified: at `r = |b|^2/a^2 = 1/2`, `theta = 0.9`, spectrum
`{-0.399, 1.520, 1.879}`).

### B. Reality places the native operator on the signed side

The SIGNED readout `sqrt(m_k) = lambda_k` -- the operator's OWN spectrum -- gives
`Q = 2/3` theta-INDEPENDENTLY at `r = 1/2` (max deviation `3e-16`), the retained
value `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`
(**retained**). The SINGULAR-VALUE readout `sqrt(m_k) = |lambda_k|` requires an
EXTRA modulus step -- passing to the positive Yukawa `Y = sqrt(H^2) = |H|`, which
is NOT the spectrum of `H` -- and gives a theta-DEPENDENT `Q <= 2/3`
(`Q_singular in [0.409, 0.667]`). Both readouts give the same masses
`m_k = lambda_k^2`; they differ ONLY in the `sqrt(m)` sign. So a genuine
self-adjoint operator (reality) makes the signed reading the native one and the
singular reading the one needing added structure.

### C. The shared mechanism: self-adjointness collapses the eigen-phase to a sign

Self-adjointness (reality) gives a real spectrum, so each eigen-phase
`arg(lambda_k)` is `0` or `pi` -- a `Z_2` SIGN, not a continuous `U(1)` phase. A
non-self-adjoint operator has complex spectrum with continuous eigen-phases
(verified). This is the operator form of CPT and is exactly what reduces a
continuous phase to a sign -- on BOTH the generation mass operator and a qubit
record observable.

### D. But different factors: not one shared object

The retained records-side signed object is the Pauli record `sigma_z`
(eigenvalue `+-1`,
`yt_lsp_signed_record_source_readout_support_note_2026-05-24`,
**retained_bounded**) on the SITE qubit `C^2`. The `sqrt(m)` sign lives on the
GENERATION `C^3` (the `C_3` circulant index). They are the same TYPE (the signed
eigenvalue of a Hermitian operator) but DIFFERENT operators on DIFFERENT tensor
factors. Bridging `C^2` (site) to `C^3` (generation) is the open
generation-identification gate (the obvious transport route has a retained
no-go). So a single reality condition does not make the two signs one object's
eigen-phase.

## Disposition

Reality (retained) is a shared mechanism that FAVORS the signed readout, not a
single principle discharging both pins. Residuals, named and NOT adopted:

- **records-side:** "the records/decoherence channel's pointer observable is
  `H = iD`" is an IMPORT -- no ledger row identifies the decoherence channel with
  `H = iD` or the mass operator; the framework's records lanes dephase in a
  record basis, not the `H`-eigenbasis. (The records-side `U` object itself is
  unbuilt on main.)
- **readout-side:** the last step "feed the signed `lambda_k` to `Q`, not
  `+|lambda_k|`" is an UNAUDITED internal identification
  (`koide_readout_lane_demarcation_note_2026-05-30`, **unaudited**), natural from
  self-adjointness but not yet retained -- it is NOT a foreign import.
- **the bridge:** `C^2` (site) to `C^3` (generation) is the open
  generation-identification gate.

A correction this surfaced:
`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`
is `audited_failed` only for a boundary-wording defect in one corollary (the
equality window at `theta = pi/12` should be closed, not open); its core
mechanism is sound and the signed VALUE rests independently on the retained
`koide_circulant_q_two_thirds_algebraic` theorem.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| `cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10` | retained_bounded |
| `physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30` | retained_bounded |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | retained |
| `koide_circulant_character_bridge_narrow_theorem_note_2026-05-09` | retained |
| `yt_lsp_signed_record_source_readout_support_note_2026-05-24` | retained_bounded |
| `koide_readout_lane_demarcation_note_2026-05-30` | unaudited |
| `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29` | audited_failed |

## Non-circularity

`Q = 2/3` is used only as the target to check against; nothing assumes it as an
input to a forcing argument. The signed-vs-singular computation and the
eigen-phase collapse are direct spectral facts.

## Next paths this opens

- Audit `koide_readout_lane_demarcation` (the "native readout is signed/forced"
  claim) toward retained -- this is the readout-side internal identification, not
  an import, and is the smallest step that would put the signed value on fully
  retained ground.
- Probe the `C^2` (site) to `C^3` (generation) factor bridge -- the same gate the
  generation-identification question already names. If a reality-respecting
  bridge exists, the qubit `sigma_z` sign and the generation `sqrt(m)` sign would
  become one operator's eigen-phase, and the shared mechanism would upgrade to a
  shared object.
- The records-side import ("records are of `H = iD`") and the action-native
  two-step transfer-positivity route are independent ways to the same
  `T`-positivity target; either discharges the CAR half without the other.

This is a localization that turns the convergence conjecture into a precise
shared-mechanism statement and names the three residuals; it is not a closure.
