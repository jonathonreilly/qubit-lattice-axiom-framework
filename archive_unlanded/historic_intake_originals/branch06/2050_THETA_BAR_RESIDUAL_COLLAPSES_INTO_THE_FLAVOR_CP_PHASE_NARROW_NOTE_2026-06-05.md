# The Strong-CP Angle's Physical Residual Collapses Into the Flavor-CP Phase (θ̄ = θ_QCD + arg det M_q; the Hermitian Circulant Is the CP-Conserving Default)

**Date:** 2026-06-05
**Type:** narrow_theorem
**Claim type:** narrow_theorem (structural, computable-side) — the physical strong-CP angle
`θ̄ = θ_QCD + arg det(M_q)` is, on the framework's real-Wilson gauge action (`θ_QCD = 0`), equal to
the **generation mass-matrix phase** `arg det(M_q)`, a CP-odd phase of the *same* mass matrices whose
CP-odd phase is the Koide flavor phase `δ`. The framework's generation Yukawa is the **Hermitian**
C₃-circulant `M = aI + bC + b̄C²`, whose determinant is **real** (`arg det = 0`): the CP-conserving
default at which `θ̄ = 0` **and** `δ = 0` coincide. So the strong-CP residual is **not an independent
input** from the flavor-CP phase — it lives in the same reality-breaking already admitted as part of
`AC_φλ`.
**Claim scope:** a **bookkeeping collapse** of the θ admission's physical residual into the flavor
sector. This is **not a strong-CP solution**: it does **not** derive `θ̄ ≈ 0`; the controlled
smallness (`θ̄ ≈ 0` while the CKM phase is `O(1)`) is exactly the **Nelson-Barr** problem, also
unsolved in the Standard Model. It does **not, by itself, reduce the Tier-A count to 1**: the
gauge-side real-Wilson selection (`θ_QCD = 0`) remains, and reflection positivity provably cannot
force it ([`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)).
**Status:** review-loop source proposal. This note writes no audit verdict and supplies no direct
effective-status change; independent audit required.
**Runner:** [`scripts/audit_companion_theta_bar_residual_collapses_into_flavor_cp_phase_exact.py`](./../scripts/audit_companion_theta_bar_residual_collapses_into_flavor_cp_phase_exact.py)

## The identity and the framework's default

The physical, basis-invariant strong-CP angle is

> `θ̄ = θ_QCD + arg det(M_u M_d)`

(standard: a chiral rotation shifts `θ_QCD` by the anomaly and `arg det M` oppositely, leaving `θ̄`
invariant — runner check (2)). Two facts about the framework then fix where `θ̄` lives:

1. **Gauge side — `θ_QCD = 0` by the real-Wilson selection.** The framework's gauge action is the
   real Wilson action; it carries **no `θ` slot**. This is the repo's already-selected surface
   ([`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md), an *action-surface selection*,
   not a forced no-go — RP cannot forbid an added `θ` term, the 2026-05-16 no-go). On this surface the
   pure-gauge contribution to `θ̄` vanishes.
2. **Matter side — the generation Yukawa is the Hermitian C₃-circulant.** `M = aI + bC + b̄C²` is
   Hermitian (check (1)), so `det M` is **real** and `arg det M = 0` (check (1b)). This is the
   framework's **CP-conserving default**: the *same* real/Hermitian point at which the Koide phase
   `δ = 0` (the δ-admission note's modulus extrema) and `θ̄ = 0`.

Therefore, on the framework's surface, **the entire physical `θ̄` is the matter-side phase
`arg det(M_q)`** — a CP-odd phase of the generation mass matrices.

## The collapse: θ̄ and δ are one reality-breaking

Breaking the Hermitian/reality structure is what turns on **both** CP-odd quantities:

- a non-Hermitian (CP-violating) deformation `M' = aI + bC + cC²` with `c ≠ b̄` gives
  `arg det M' ≠ 0` (check (3)) → a nonzero contribution to `θ̄`;
- the *same* departure from the real circulant is what gives the flavor phase `δ = arg b` its
  physical, non-degenerate value (the δ-admission note).

So `θ̄` (strong-CP) and `δ` (flavor-CP) are **the same CP-odd content** — both zero at the
Hermitian/real default, both switched on by one reality-breaking. The strong-CP angle is **not an
independent admission** from the flavor-CP phase: it is the overall phase of the generation mass
matrices the framework already admits (`AC_φλ`). In Standard-Model language this is precisely the
**Nelson-Barr** identity `θ̄ = arg det M_q`: the strong-CP problem **is** the flavor-CP problem.

## What this is, and what it is not

| | statement | status |
|---|---|---|
| identity | `θ̄ = θ_QCD + arg det(M_q)` (basis-invariant) | standard (check (2)) |
| gauge side | `θ_QCD = 0` on the real-Wilson action | repo-selected surface (not RP-forced) |
| matter default | Hermitian circulant → `arg det = 0` → `θ̄ = 0 = δ` | exact (checks (1),(1b)) |
| collapse | physical `θ̄ = arg det(M_q)` = the flavor-CP phase sector (`AC_φλ`) | **this note** |
| **not** a solution | `θ̄ ≈ 0` with `CKM ≠ 0` (controlled smallness) | **open — Nelson-Barr, SM-unsolved** |
| **not** a count reduction | the gauge-side real-Wilson selection `θ_QCD = 0` remains | RP cannot force it (2026-05-16) |

**Net.** The framework's real/Hermitian structure makes CP-conservation its *default* (`θ̄ = 0`,
`δ = 0` at the same point), and the physical CP violation is **one** reality-breaking shared by the
strong-CP angle and the flavor phase. This **collapses** the strong-CP residual into the flavor-CP
sector (`AC_φλ`) — tightening the Tier-A bookkeeping by showing `θ̄` is not an independent input — but
it is **not** a strong-CP solution and does not by itself reduce the admission count to one. The
controlled pattern (CP-odd in flavor, CP-even in the θ-vacuum) remains the Nelson-Barr admission,
which the Standard Model also does not derive.

## Forbidden-import / reprove-and-cite discipline

- The identity `θ̄ = θ_QCD + arg det M_q` and all algebra are **reproven** in the runner from the
  C₃-circulant primitive and the chiral-rotation bookkeeping (sympy/numpy, 5/5 exact). No literature
  value is used as a derivation input.
- Nelson (PLB 136, 1983), Barr (PRL 53, 1984), and Vafa-Witten (PRL 53, 1984) are **comparators**
  only — the Nelson-Barr identity and the `θ=0 ⟹ positivity` direction are cited as cross-checks, not
  imported as premises.
- No PDG values appear. `δ ≈ 2/9` and the CKM phase are named only as the *empirical targets* the
  collapse does **not** derive.

## Dependencies (citation-graph visible)

- [`MINIMAL_AXIOMS_2026-06-04.md`](./MINIMAL_AXIOMS_2026-06-04.md)
- [`STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md`](./STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md)
- [`STRONG_CP_THETA_ZERO_NOTE.md`](./STRONG_CP_THETA_ZERO_NOTE.md)
- [`STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md`](./STRONG_CP_RP_HALF_CANNOT_FORBID_CP_ODD_IMAGINARY_NO_GO_NOTE_2026-05-16.md)
- [`KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md`](./KOIDE_PHASE_DELTA_IS_ALSO_AN_ADMISSION_CLEAN_MODULUS_HAS_ONLY_DEGENERATE_STATIONARY_POINTS_NARROW_NO_GO_NOTE_2026-06-04.md)

**Independent audit required.** This note asserts no effective-status change.
