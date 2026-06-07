---
claim_id: free_dirac_wigner_action_strong_continuity_bridge_note_2026-06-07
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Free Dirac Wigner Action Strong-Continuity Bridge

**Date:** 2026-06-07
**Type:** bounded theorem / direct-support bridge
**Primary runner:**
[`scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py`](../scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py)
**Cached runner output:**
[`logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt`](../logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt)

## Scope

This bridge supplies the dependency edge requested by the audit of
`docs/FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`:

```text
missing_dependency_edge: cite and include the companion free-Dirac Poincare
representation packet, with its retained status and the carrier/cocycle/
strong-continuity proof, or replace the import with a self-contained derivation
in this packet.
```

The bridge uses the second option at bounded-free-field scope. It gives the
direct derivation, on the explicit one-particle mass-shell carrier used by the
free Dirac packet, that the displayed Wigner action is a strongly continuous
unitary representation. The companion packet is still cited in parallel for the
finite Poincare-algebra, mass-shell, invariant-measure, and Wigner-rotation
checks.

This bridge does not derive the free Dirac carrier from the baseline lattice
axioms, does not prove spin-statistics, does not close an interacting theory,
and does not promote any audit status.

## 2026-06-07 dependency authority repair

The 2026-06-07 audit marked this bridge conditional because the restricted
packet did not include the full companion free-Dirac Poincare representation packet/cache
as an explicit dependency authority:

```text
missing_dependency_edge: include the full companion free-Dirac Poincare
representation packet/cache as a cited authority, or replace it with a
self-contained derivation of invariant d^3p/(2E), Wigner cocycle/SU(2) carrier
continuity, and full 3+1 mass-shell action facts.
```

This source repair keeps the claim bounded to the supplied continuum
mass-shell carrier and makes the companion authority packet explicit:

| Role | Path | Certificate |
| --- | --- | --- |
| companion representation note | [`docs/FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md) | bounded free Dirac/Poincare algebra and positive-energy support |
| companion representation runner | [`scripts/free_dirac_poincare_representation_2026-05-30.py`](../scripts/free_dirac_poincare_representation_2026-05-30.py) | primary runner for the companion packet |
| SHA-pinned companion cache | [`logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt`](../logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt) | `SCORECARD PASS=8 FAIL=0` |

The companion cache is load-bearing for:

- positive-energy mass shell preservation;
- Lorentz-invariant `d^3p/(2E)` measure preservation;
- Wigner little-group rotation and `SU(2)` carrier checks;
- finite Poincare-algebra sign and bracket checks.

The bridge runner now verifies that this companion cache is SHA-fresh, has
`status: ok`, exits zero, and contains the `P5`, `P6`, and
`SCORECARD PASS=8 FAIL=0` certificates before checking the bridge's own
strong-continuity and firewall claims.

## Carrier And Action

Let

```text
H_m^+ = {p=(E,p_vec): E=sqrt(m^2+|p_vec|^2), E>0}
dmu(p) = d^3p/(2E)
H_1 = L^2(H_m^+, dmu; C^2)
```

On the dense carrier `C_c^\infty(H_m^+; C^2)`, define

```text
(U(a,Lambda) psi)(p)
  = exp(i a.p) D(W(Lambda,Lambda^{-1}p)) psi(Lambda^{-1}p),
```

where `D` is the spin-1/2 unitary little-group carrier and

```text
W(Lambda,p) = L(Lambda p)^(-1) Lambda L(p).
```

The companion free-Dirac representation packet verifies, at runner level, the
positive-energy mass shell, invariant `d^3p/(2E)` measure, Poincare algebra
signs, and SU(2) Wigner-rotation carrier checks. This note adds the explicit
functional-analytic bridge:

1. **Unitary:** the translation factor has modulus one, `dmu` is invariant under
   the mass-shell change of variables, and `D(W)` is unitary fiberwise.
2. **Group law:** the Wigner cocycle
   `W(Lambda_1 Lambda_2,p) =
   W(Lambda_1,Lambda_2 p) W(Lambda_2,p)` gives
   `U(a_1,Lambda_1)U(a_2,Lambda_2)
   = U(a_1 + Lambda_1 a_2, Lambda_1 Lambda_2)` on the dense carrier.
3. **Strong continuity on the dense carrier:** for compactly supported smooth
   `psi`, the phase, Lorentz pullback, and SU(2) carrier vary pointwise
   continuously near the identity and are dominated on a common compact
   support; dominated convergence gives
   `||U(a,Lambda)psi - psi|| -> 0`.
4. **Extension to all `H_1`:** unitary operators extend the dense-carrier strong
   continuity to the Hilbert-space completion by the standard epsilon/3 density
   argument.
5. **Stone consequence:** each one-parameter subgroup has a self-adjoint
   generator. This is the direct integrability route; it does not use the
   rejected Gaussian Nelson/common-analytic-vector route.

## Runner Certificate

The runner checks:

- source anchors in this bridge, the parent generator note, and the companion
  representation note/cache;
- exact `1+1` mass-shell semidirect product law in rapidity coordinates,
  including the translation-vector transform;
- boost-shift unitarity and strong-continuity proxy on the rapidity dense
  carrier;
- translation phase unitarity and strong-continuity proxy;
- SU(2) Wigner carrier unitarity, same-axis group law, and continuity at the
  identity;
- density-extension guard and firewall flags.

Expected output:

```text
SCORECARD PASS=48 FAIL=0
```

## Status Certificate

```yaml
actual_current_surface_status: exact-support
trace_class: direct_blocker_closure
reachability_to_target: closes
conditional_surface_status: "bounded free one-particle Wigner action on the supplied continuum mass-shell carrier"
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This closes a dependency edge for re-audit; it does not set audit status or derive lattice Lorentz symmetry."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
