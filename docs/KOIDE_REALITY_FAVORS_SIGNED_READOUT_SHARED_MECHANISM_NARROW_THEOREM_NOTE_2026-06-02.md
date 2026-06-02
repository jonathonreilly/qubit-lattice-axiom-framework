# Reality Favors the Signed Readout, and Shares a Phase-Collapse Mechanism With the Records Side

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only; effective status is
pipeline-derived after audit.
**Primary runner:** [`scripts/frontier_koide_reality_favors_signed_shared_mechanism.py`](../scripts/frontier_koide_reality_favors_signed_shared_mechanism.py)

## Context

Two open pins of the charged-lepton program were conjectured to converge under
one principle: the records-side positive real branch-coherence condition
(with `U = I` as a sufficient canonical realization; companion note
[`KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED...2026-06-02`](KOIDE_HERMITIAN_RECORDS_IMPORT_REQUIRED_NARROW_THEOREM_NOTE_2026-06-02.md)) and the value-side
signed-vs-singular Koide readout (the Brannen/det_R closure needs `sqrt(m)` to
be SIGNED). The conjecture: a CPT / reality condition on the emergent-time
generator forces both. This note records what is actually true.

## Claim

The reality of the emergent-time generator
(`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`,
**retained_bounded**: the staggered hopping `D` is real anti-Hermitian, so
`H = iD` is Hermitian) **places the native Koide mass operator on the SIGNED
side** of the readout dichotomy, and is the same kind of structural mechanism
needed on the records side: self-adjointness collapses a continuous eigenphase
to a real sign/positive-real coherence condition. But the two act on DIFFERENT
tensor factors (generation `C^3` vs site qubit `C^2`). So it is a shared
**mechanism**, not a single shared **object**: one reality principle favors the
signed readout but does not collapse both pins into one discharge.

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
continuous phase to a sign on the generation mass operator, and what the
records route analogously needs to convert branch coherence into a positive
real transfer.

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

A correction this depends on:
`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`
has a source repair landed for the boundary-wording defect in one corollary
(the equality window at `theta = pi/12` should be closed, not open), but it
still needs independent re-audit before serving as retained support. The signed
VALUE itself still rests independently on the retained
`koide_circulant_q_two_thirds_algebraic` theorem.

## Verified tiers (origin/main audit ledger)

| claim_id | effective status |
|---|---|
| [`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) | retained_bounded |
| [`physical_hermitian_hamiltonian_and_sme_bridge_note_2026-04-30`](PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md) | retained_bounded |
| [`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md) | retained |
| [`koide_circulant_character_bridge_narrow_theorem_note_2026-05-09`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) | retained |
| [`yt_lsp_signed_record_source_readout_support_note_2026-05-24`](YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md) | retained_bounded |
| [`koide_readout_lane_demarcation_note_2026-05-30`](KOIDE_READOUT_LANE_DEMARCATION_NOTE_2026-05-30.md) | unaudited |
| [`koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md) | source repair landed; re-audit pending |

## Non-circularity

`Q = 2/3` is used only as the target to check against; nothing assumes it as an
input to a forcing argument. The signed-vs-singular computation and the
eigen-phase collapse are direct spectral facts.

## No-Go Discipline Gate

- **N1 alternative routes:** signed spectrum, singular-value readout, records
  branch coherence, records-as-`H=iD`, and one-qubit/generation carrier bridge
  routes are separated.
- **N2 wall independence:** the records-side import, the signed-readout
  identification, and the one-qubit/generation bridge do not imply one another.
- **N3 hidden walls:** "reality favors signed" is tied to a Hermitian operator
  spectrum; it does not assume that the records channel is the Koide operator.
- **N4 residual matching:** the records residual targets transfer positivity;
  the value residual targets which square root enters `Q`; the note does not
  merge them into one object.
- **N5 rhetoric audit:** "shared mechanism" is used instead of "shared object"
  or "single principle closes both."
- **N6 partial-closure scan:** auditing the readout demarcation, deriving
  records-as-`H=iD`, and building the carrier bridge are preserved as distinct
  partial-closure paths.
- **N7 steelman:** a reviewer can accept self-adjoint signed spectra while
  denying that this selects the physical `sqrt(m)` readout; the note leaves that
  internal identification unaudited.
- **N8 cross-cycle echo:** prior signed-vs-singular and records-phase walls have
  repeatedly split mechanism from object identity; this note follows that split.

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
