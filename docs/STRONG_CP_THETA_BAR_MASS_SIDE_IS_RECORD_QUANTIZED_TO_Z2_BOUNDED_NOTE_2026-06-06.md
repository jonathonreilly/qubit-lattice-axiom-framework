# The Mass-Side Strong-CP Phase Is Record-Quantized to a Z₂ Sign {0, π} — the Continuous-Naturalness Half Dissolves

**Date:** 2026-06-06
**Type:** bounded_theorem
**Claim type:** bounded_theorem — a **record-native quantization** of the mass-side strong-CP phase. The
physical strong-CP angle is `θ̄ = θ_QCD + arg det(M_q)`. This note shows that the **mass-side** term
`arg det(M_q)` is **record-quantized to a Z₂ sign `{0, π}`** — *not* a continuous angle — as a corollary of the
signed-readout result ([the recorded readout is self-adjoint, PR #2921](./MINIMAL_AXIOMS_2026-06-05.md)) applied
under the sharpened
[`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`](./RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md).
**Claim scope:** this is **not a strong-CP solution**. It dissolves only the **continuous-mass-phase** half of
the naturalness problem (there is no continuous `arg det` to tune against `θ_QCD`). It does **not** discharge:
(a) the gauge `θ_QCD` (the framework's real-Wilson default is a *selection*, **not** record-forced — RP
provably cannot force it, the `strong_cp_rp_half` no-go); (b) the **`{0, π}` sign selection** (which of the two
Z₂ values — the registered determinant sign = the positive-mass orientation — is a *registered pattern*, like
`r = 1/2`, not derived); (c) the **quark/CKM** sector (physical CKM mixing needs a non-Hermitian /
non-circulant mass structure that breaks the `{0, π}` quantization; the native quantization is exact on the
recorded/Hermitian sector — sharpest for the leptons).
**Status authority:** independent audit lane only. No effective-status change; **Independent audit required.**
**Runner:** [`scripts/audit_companion_strong_cp_theta_bar_record_quantized_z2_exact.py`](./../scripts/audit_companion_strong_cp_theta_bar_record_quantized_z2_exact.py)

## The problem and the resolution

The strong-CP problem is a **continuous-naturalness** problem: `θ̄ = θ_QCD + arg det(M_q)` is, in the Standard
Model, a sum of two *continuous* parameters that must cancel to `|θ̄| ≲ 10⁻¹⁰`. The continuous tuning is the
puzzle. The mass-side term `arg det(M_q)` is, in the SM, the overall phase of a general complex Yukawa matrix —
a continuous knob.

**Under the Record axiom that knob does not exist.** The sharpened record-outcome principle plus the
signed-readout result give:

1. **A recorded observable is self-adjoint.** The record registers the `K`/CPT orbit of the realized sector =
   the **signed real eigenvalue** (PR #2921: "signed-vs-singular is record-forced-given-Hermitian"). A recorded
   mass operator is therefore **Hermitian**. (Runner (1): the recorded `C₃` mass `M = aI + bC + b̄C²` is
   Hermitian.)
2. **Hermitian ⟹ real spectrum ⟹ the determinant phase is a Z₂ sign.** Real eigenvalues give a **real**
   determinant, so `arg det(M) ∈ {0, π}` — and concretely `arg det = π·(#negative eigenvalues mod 2)`, the
   **parity of the negative signed eigenvalues**. (Runner (2),(3).)
3. **So the mass-side phase is record-quantized.** `θ̄_mass = arg det(M_q) ∈ {0, π}` is a **discrete Z₂**, not a
   continuous angle. The continuous knob the strong-CP problem worries about **is not in the recorded theory.**
4. **The contrast is exact.** A *non-recorded* (non-self-adjoint) mass — a general complex `M = aI + bC + cC²`
   with `c ≠ b̄` — has a **continuous** `arg det` (the SM case). The quantization is a property of the
   record-forced self-adjointness, nothing else. (Runner (4).)
5. **The registered value is 0 for physical masses.** For all-positive masses (the physical charged leptons,
   Foot's 45° positive octant) `#negative = 0`, so the registered determinant sign is `+` and
   `θ̄_mass = 0`. (Runner (5).)

## What this is, and the three residuals it does NOT close

| | statement | status |
|---|---|---|
| mass-side phase `arg det(M_q)` | **record-quantized to a Z₂ `{0, π}`** (self-adjoint ⟹ real spectrum) | **derived** (runner 7/7) |
| continuous-mass-phase naturalness | **dissolved** — no continuous `arg det` to tune against `θ_QCD` | **derived** |
| registered value (physical masses) | `θ̄_mass = 0` (positive-det / `+` orientation) | **registered pattern**, not derived |
| (a) gauge **`θ_QCD`** | real-Wilson default is a *selection*; RP cannot force it (`strong_cp_rp_half`) | **open — separate admission** |
| (b) the **`{0, π}` sign** | which Z₂ value = registered det sign = positive-mass orientation | **open — registered, like `r=1/2`** |
| (c) **quark/CKM** sector | CKM needs non-Hermitian structure that breaks the `{0, π}` quantization | **open — exact on the recorded/Hermitian (lepton) sector** |

**Net.** The strong-CP problem has two halves: *why is `θ̄` not a generic continuous O(1) number*, and *why
exactly is it ≈ 0*. The Record axiom answers the **first** for the mass-side term: `arg det(M_q)` is **not a
continuous parameter at all** — a recorded mass is self-adjoint, so its determinant phase is a Z₂ sign `{0, π}`.
The continuous-mass-phase tuning that makes strong-CP a *naturalness* problem is **dissolved** on the recorded
sector. The **second** half survives as a discrete `{0, π}` selection (the registered det sign, a *registered
pattern* exactly parallel to `r = 1/2`) plus the independent gauge `θ_QCD` admission. This is **not** a
strong-CP solution — it is a sharp reduction of the mass-side from *continuous* to *Z₂*, the first genuinely new
movement on the `θ` Tier-A item via the sharpened Record principle.

## No-go discipline / steelman

**Strongest objection (the gauge term is the real strong-CP problem).** Granted: the neutron-EDM `θ̄` is
dominated by the QCD vacuum angle `θ_QCD`, which this note does **not** force (the real-Wilson choice is a
selection; the `strong_cp_rp_half` no-go shows reflection positivity cannot forbid the topological term). The
claim here is **only** about the mass-side `arg det` term, and only that it is **discrete, not continuous** — a
naturalness statement, not a value derivation. **Second objection (quarks are not Hermitian).** Correct, and
load-bearing: physical CKM mixing requires a non-Hermitian / non-circulant quark mass, which **breaks** the
`{0, π}` quantization. The result is therefore **exact on the recorded/Hermitian sector** — cleanest for the
charged leptons, where the `C₃` circulant is Hermitian and `θ̄_lepton = 0` is record-forced; for the quark
sector it is a statement about the recorded (self-adjoint) part only, with the CKM-carrying non-Hermitian
remainder a separate structure. **Third objection (Z₂ still allows π).** Yes — `θ̄_mass = π` is CP-violating;
the quantization dissolves the *continuous* problem, not the *sign* selection, which stays a registered pattern.
All three objections are accommodated by the conditional scope; the quantization (Parts 1–4) stands regardless.

## Forbidden-import / reprove-and-cite

All algebra (the recorded `C₃` mass is Hermitian; real spectrum; `arg det = π·(#neg mod 2) ∈ {0, π}`; the
non-self-adjoint contrast gives continuous `arg det`; all-positive ⟹ `arg det = 0`) is **reproven** from the
`C₃` / Clifford primitives in the runner (sympy/numpy, 7/7). The basis-invariant decomposition
`θ̄ = θ_QCD + arg det M_q`, the Nelson-Barr Hermitian-mass strong-CP-evasion idea, and reflection-positivity /
`θ`-term facts are **comparators** only — never derivation inputs. No PDG values; `θ̄ ≈ 0` named only as the
target this note's mass-side half advances (not the full solution).

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-05.md`](./MINIMAL_AXIOMS_2026-06-05.md)
- [`RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md`](./RECORD_OUTCOME_OBSERVABLE_PRINCIPLE_CANONICAL_PROPOSAL_NOTE_2026-06-05.md)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](./STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)

**Independent audit required.** This note asserts no effective-status change.
