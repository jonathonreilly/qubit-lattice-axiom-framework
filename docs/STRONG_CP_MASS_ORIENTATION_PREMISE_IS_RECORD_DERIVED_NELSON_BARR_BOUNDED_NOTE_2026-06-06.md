# The Strong-CP Mass-Orientation Premise Is Record-Derived, Not Selected (Nelson-Barr, Record-Native) — Bounded Note

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — **discharges one named premise** of the parent strong-CP admission. The parent
[`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md) runs a bounded Vafa-Witten closure (Legs A–D),
but its 2026-04-28 audit flagged **two underived premises**, and its "Path A future work" item 2 asks for
*"a registered positive real quark-mass orientation / `arg det(M_u M_d) = 0` theorem as a dependency."* This note
shows the record-native result
[`STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md`](./STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md)
(PR #2932) **is** that theorem: the parent's *accepted surface premise* is **record-derived**.
**Claim scope:** this is **not a strong-CP solution** and **not a Tier-A retirement**. It discharges **one** of the
parent's two flagged premises (the mass orientation). It does **not** discharge: **(Path-A-item-1)** the gauge-side
*"no bare θ slot"* (RP provably cannot force it — `strong_cp_rp_half` no-go; action-form uniqueness blocked); and
the **Vafa-Witten limitation** — Leg D gives `|Z(θ)| ≤ Z(0)` so θ=0 is the free-energy *minimum* and strong CP is
not *spontaneously* broken, but it does **not dynamically select** the θ *parameter*. The staggered-Dirac
realization underlying Leg A is itself the **other** Tier-A admission (`AC_φλ`).
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_strong_cp_mass_orientation_record_derived_exact.py`](./../scripts/audit_companion_strong_cp_mass_orientation_record_derived_exact.py)

## The premise, and why it was the live gap

The physical strong-CP angle is `θ̄ = θ_QCD + arg det(M_u M_d)`. The parent closure neutralises the mass term by
**assuming** a *"positive real quark-mass orientation"* (`arg det(M_u M_d) = 0`) as part of the selected action
surface. The audit verdict named this precisely: the runner *"uses an explicit positive real quark-mass surface
for `arg det(M_u M_d) = 0`"* but *"[does] not derive ... [that the action] fixes the real-mass orientation."* So
the orientation was a **selected input**, and Path-A-item-2 asks for it to become a **derived dependency**.

**The Record axiom supplies exactly that derivation.** A recorded observable registers the `K`/CPT orbit = the
**signed real eigenvalue** (PR #2921), so a recorded mass operator is **Hermitian**. Then (runner 8/8):

1. **Reality is record-forced.** Hermitian ⟹ real spectrum ⟹ `det M` real ⟹ `arg det M ∈ {0, π}`. The
   *discreteness* the parent assumed (no continuous mass phase) is **derived**, not selected. (Runner (1a),(1b).)
2. **The orientation is the registered positive sector.** For a positive-definite (physical, all-positive-mass)
   recorded mass, `arg det M = 0` — exactly the parent's *"positive real quark-mass orientation."* (Runner (1c).)
3. **The discharge is logically exact.** Parent surface premise (`arg det(M_u M_d) = 0`) **=** the record-derived
   result of #2932. The premise is **discharged**, not assumed. (Runner (4).)

## The structure is Nelson-Barr — and it corrects an over-conservative caveat

#2932 carried a conservative caveat that "the quark/CKM sector needs a non-Hermitian structure that breaks the
`{0, π}` quantization." **That is too strong, and the runner corrects it.** General Hermitian (non-circulant)
up/down masses with **misaligned eigenbases** give:

- a **unitary CKM** `V = U_u† U_d` with `|det V| = 1` and a **non-zero Jarlskog invariant** (CP violation in the
  weak sector), while
- `arg det(M_u M_d)` stays **real, in `{0, π}`** (strong-CP-safe), because `det` is basis-invariant under the
  unitary diagonalisations. (Runner (2a),(2b).)

This is exactly the **Nelson-Barr** structure — Hermitian masses make the strong sector CP-safe (`arg det ∈ {0, π}`)
while weak CP violation survives through up/down misalignment — and here it is **record-derived rather than
imposed**. (Only the `C₃`-*circulant* special case is degenerate: circulants share the Fourier eigenbasis, giving
no mixing; physical CKM comes from the `C₃`-breaking, which is the separate `AC_φλ` flavor input.)

## What this changes, and the two residuals it does NOT close

| | statement | status |
|---|---|---|
| mass orientation `arg det(M_u M_d) = 0` | **record-derived** (recorded ⟹ Hermitian ⟹ real; positive ⟹ 0) | **discharged** (runner 8/8) |
| strong-CP-safe + weak CP coexist | Nelson-Barr: `arg det ∈ {0,π}` with CP-violating CKM from misalignment | **derived** |
| Vafa-Witten Leg A/D | `det(D+m) = Π(m²+λ²) > 0` ⟹ `Z_Q ≥ 0` ⟹ `|Z(θ)| ≤ Z(0)` (θ=0 minimum) | **re-confirmed on a record-derived orientation** |
| **(Path-A-item-1)** "no bare θ slot" | the gauge action-class restriction | **open** — RP cannot force it; action-form uniqueness blocked |
| θ *parameter* selection | Vafa-Witten bounds `|Z(θ)| ≤ Z(0)`, does not pick the parameter | **open** — the residual naturalness statement |
| staggered-Dirac (Leg A) | the anti-Hermitian ε-graded operator | **the other Tier-A admission** (`AC_φλ`) |

**Net.** The parent strong-CP closure had **two** load-bearing surface premises. The **mass-orientation** one is
now **record-derived** (the recorded mass is Hermitian ⟹ `arg det ∈ {0, π}` ⟹ positive-orientation `= 0`), and the
Hermitian structure is the Nelson-Barr mechanism that keeps the strong sector CP-safe while preserving weak CKM CP.
This converts the mass half of the closure from *selected surface* to *derived dependency* — precisely Path-A-item-2.
It is **not** a strong-CP solution: the gauge-side *"no bare θ slot"* (Path-A-item-1) is untouched, and Vafa-Witten
bounds the free energy at θ=0 without selecting the θ parameter.

## No-go discipline / steelman

**Strongest objection (you only did the easy half).** Correct, and stated plainly: the strong-CP angle has a gauge
piece `θ_QCD` and a mass piece `arg det(M)`. This note record-derives **only** the mass piece. The gauge piece —
why the admissible action carries no bare `θ`-slot — is the genuinely hard half, and the `strong_cp_rp_half` no-go
shows reflection positivity cannot force it. **Second objection (Vafa-Witten ≠ selection).** Also granted: `Z_Q ≥ 0`
gives `|Z(θ)| ≤ Z(0)` (θ=0 is the energy minimum, no *spontaneous* strong-CP breaking), which is a statement about
the *parameter's* energetics, not a dynamical choice of the parameter. **Third objection (Leg-A conditionality).**
The Dirac-determinant positivity rests on the staggered/Kähler-Dirac realization, which is the **other** Tier-A
admission; so the closure is conditional on it. All three are accommodated by the explicit residual table; the
mass-orientation discharge (Parts 1–3) stands regardless.

## Forbidden-import / reprove-and-cite

All facts (Hermitian ⟹ `arg det ∈ {0,π}`; positive-definite ⟹ `0`; misaligned Hermitian masses ⟹ CP-violating
unitary CKM with strong-CP-safe `arg det`; ε-graded anti-Hermitian `D` ⟹ `det(D+m) = Π(m²+λ²) > 0`; `Z_Q ≥ 0` ⟹
`|Z(θ)| ≤ Z(0)`) are **reproven** from the `C₃`/Clifford and staggered primitives in the runner (numpy/sympy, 8/8).
Vafa-Witten (PRL 53, 535) and the Nelson-Barr Hermitian-mass mechanism are **comparators** only — never derivation
inputs. No PDG values; `θ̄ ≈ 0` named only as the target whose mass half this note discharges.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md`](./STRONG_CP_THETA_BAR_MASS_SIDE_IS_RECORD_QUANTIZED_TO_Z2_BOUNDED_NOTE_2026-06-06.md)
- [`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md)
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)

**Independent audit required.** This note asserts no effective-status change and changes no Tier-A registry entry.
