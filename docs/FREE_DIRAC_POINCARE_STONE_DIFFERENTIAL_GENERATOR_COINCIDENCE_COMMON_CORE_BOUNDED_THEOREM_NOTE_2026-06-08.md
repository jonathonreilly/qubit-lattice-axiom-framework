---
claim_id: free_dirac_poincare_stone_differential_generator_coincidence_common_core_bounded_theorem_note_2026-06-08
claim_type: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Free Dirac Poincaré: Stone Generators Coincide with the Differential Generators on a Common Core

**Date:** 2026-06-08
**Type:** bounded_theorem
**Role:** direct-support bridge (closes a named audit dependency edge)
**Claim type:** bounded_theorem
**Primary runner:**
[`scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py`](../scripts/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.txt`](../logs/runner-cache/frontier_wigner_core_coincidence_poincare_generators_2026_06_08.txt)

## Scope

This bridge supplies the **second half** of the dependency edge requested by the audit of
[`FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)
(audited `audited_conditional`). The audit named the missing piece:

```text
requires a retained-grade proof that the full Wigner mass-shell formula is a
strongly continuous Poincare representation AND that its Stone generators coincide
with the claimed differential generators on the relevant cores.
```

The **first** conjunct (strongly continuous unitary representation; Stone ⇒ self-adjoint
generators exist) is already supplied by
[`FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`](FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md)
(`retained_bounded`). The differential generators and the Poincaré algebra are supplied by
[`FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md)
(`retained_bounded`). This note supplies the **remaining** conjunct: the **common-core
coincidence** — the Stone generators *equal* the differential generators because they agree
on a common core. Runner **21 PASS / 0 FAIL**.

**Bounded scope.** This is the **free one-particle** Wigner representation on the supplied
continuum positive-mass mass-shell carrier (`m>0`, spin `1/2`). It does **not** derive the
carrier from the baseline lattice axioms, does **not** prove spin-statistics, and does
**not** close an interacting theory. It promotes no audit status.

## Carrier and generators

```text
H_m^+ = {p : E=sqrt(m^2+|p|^2) > 0},   dmu = d^3p/(2E),   H_1 = L^2(H_m^+, dmu; C^2).
```

Differential Poincaré generators (the representation note's data):

```text
H = E (multiplication),     P_i = p_i (multiplication),
J_i = L_i + S_i             (orbital L_i = -i eps_{ijk} p_j d/dp_k ; spin S_i = sigma_i/2),
K_i = -i E d/dp_i           (orbital = full-line momentum in rapidity) + bounded Wigner spin term.
```

Common core: `D = C_c^inf(H_m^+; C^2)` (smooth, compactly supported spinor wavefunctions).

## The coincidence theorem (runner 21/21)

**(A) The measure `d^3p/(2E)` is boost-invariant.** A boost gives `dp'_1/dp_1 = E'/E`, so
`(dp'_1/dp_1)·(E/E') = 1` (verified symbolically and numerically).

**(B) Coincidence: `d/dt U(t)ψ|_{t=0} = -i A_diff ψ` on `D`.**
- *Rotation:* `d/dt U_{R_z}(t)ψ|_0 = -i J_z ψ` with `J_z = L_z + S_z` — verified **with the
  full orbital+spin structure** (symbolic).
- *Boost:* `d/dt ψ(Λ_x(-t)p)|_0 = -E ∂ψ/∂p_1`, i.e. the orbital boost generator is
  `K_x^{orb} = -i E ∂/∂p_1` (the full-line rapidity momentum, `E d/dp = d/dζ`).
  The Wigner spin multiplier is also checked from the cocycle, not asserted
  only as a bounded add-on: with the canonical `SL(2,C)` boost
  `B(p)=sqrt((E+m)/(2m)) (I + p·σ/(E+m))`, differentiating
  `W(A_x(t),p)=B(A_x(t)p)^(-1) A_x(t) B(p)` gives
  `dW/dt|_0 = i(p_2 σ_3 - p_3 σ_2)/(2(E+m))`, equivalently the
  self-adjoint boost spin multiplier `(S × p)_x/(E+m)` under the representation
  convention. The runner verifies this derivative numerically from the displayed
  canonical-boost matrices with max error `< 1e-8`.
- *Translation:* the generator is `P_i = p_i` (real multiplication).

So `D ⊂ D(A_Stone)` and `A_Stone|_D = A_diff` for each of the ten generators.

**(C) The Poincaré algebra closes on `D` and the mass Casimir is `m^2`.** Spot-checks:
`[J_z,P_x]=iP_y`, `[J_z,P_y]=-iP_x`, `[K_x^{orb},H]=-iP_x`, and `P^2 = H^2-|p|^2 = m^2`
(symbolic). The full bracket set is the representation note's retained content.

**(D) `D` is `U(g)`-invariant for all `g`.** Translations act by a unit-modulus phase
(support unchanged); rotations preserve compact support; a boost maps a compact mass-shell
set to a compact one (the Lorentz image of a compact set is compact — verified numerically)
and the smooth Wigner cocycle `D(W)` preserves smoothness. Hence `U(g)D ⊆ D`.

**(E) The boost generator is essentially self-adjoint on `D`.** `K^{orb}=-iE d/dp_i` is
symmetric with respect to `d^3p/(2E)` because the `E`-weight cancels the `1/(2E)` measure,
reducing it to the full-line momentum operator `-i d/dζ` in rapidity (the parent #3015
repair; the half-line control leaks norm, so this is a genuine full-line/global fact). Its
**deficiency indices are `(0,0)`**: the solutions of `(-i d/dζ ∓ i)φ = 0` are `φ = e^{±ζ}`,
neither in `L²(ℝ)` (the runner exhibits `‖e^{ζ}‖²_{[-L,L]} → ∞`), so by von Neumann/Cayley
`K^{orb}` is essentially self-adjoint on `D`. The cocycle derivative above supplies the
Wigner spin term, and that term is a bounded matrix-field multiplication of operator norm
`‖S‖·|p|/(E+m) ≤ 1/2`, so `K = K^{orb} + (\text{bounded
symmetric})` is essentially self-adjoint on the **same** core `D` by **Kato–Rellich**
(relative bound `0`). `H, P_i` are real multiplication
(self-adjoint, `D` a core); `J_i` is orbital + bounded spin.

**(F) Common core ⇒ coincidence (Reed–Simon Vol I, Thm VIII.11).** A dense, `U(t)`-invariant
subspace contained in `D(A)` is a **core** for the Stone generator `A`. Premises (A1)/(F1)
density, (D) invariance, (B) `D ⊆ D(A)` hold for each one-parameter subgroup. Therefore `D`
is a **common core** for all ten Stone generators, and since `A_Stone|_D = A_diff` on the
core, the **self-adjoint closures coincide**: `A_Stone = \overline{A_diff|_D}`.

## Conclusion (the audit gap, closed)

> On the common core `C_c^inf(H_m^+; C^2)`, the ten Stone generators of the strongly
> continuous unitary Wigner representation **coincide** with the differential Poincaré
> generators `(H, P_i, J_i, K_i)`; each is essentially self-adjoint on that core (boosts by
> the rapidity full-line reduction + Kato–Rellich for the bounded Wigner spin term), the
> Poincaré algebra closes, and the mass Casimir is `m^2`.

This is the **direct-integrability** route (Reed–Simon core lemma + the explicit unitary
mass-shell action); it does **not** use the rejected common-Gaussian/Hermite analytic-vector
route (correctly removed by the parent #3015 repair). Together with the strong-continuity
bridge and the representation note, it closes the named audit conjunct, exposing the
dependency edge for the essential-self-adjointness note to re-audit.

## Reprove-and-cite

All carrier-specific facts are reproven from the explicit mass-shell carrier in
the runner (sympy + numpy, 21/21):
boost-invariance of `d^3p/(2E)`; the strong-derivative coincidence for rotations (full
orbital+spin), boosts including the Wigner-cocycle derivative, and translations; the
algebra spot-checks; `P^2=m^2`; `C_c^inf` boost-invariance; the boost `E`-weight
cancellation and the `|p|/(E+m)<1` spin bound.

Standard functional analysis is used only after those premises are checked:
Reed-Simon Vol I, Thm VIII.11 supplies the core lemma, and Kato-Rellich supplies
the bounded-perturbation step. Wigner (1939) and Mackey induced-representation
theory are context comparators, not empirical inputs. No PDG values.

## Dependencies

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
- [`FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md)
- [`FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`](FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md)
- [`FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)

## What this note does NOT claim

- It does **not** derive the free Dirac mass-shell carrier from the baseline lattice axioms.
- It does **not** prove spin-statistics, nor close an interacting theory.
- It does **not** address the `m=0` (helicity) case; the scope is `m>0`, spin `1/2`.
- It does **not** set or change any audit status; the independent audit lane is the only
  authority. **No** new axiom, primitive, or repo vocabulary; no PDG input.

**Independent audit required.** This note asserts no effective-status change.
