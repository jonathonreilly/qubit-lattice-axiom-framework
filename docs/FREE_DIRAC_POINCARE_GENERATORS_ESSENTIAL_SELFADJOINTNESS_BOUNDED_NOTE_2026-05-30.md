# Free Dirac Poincare Generators: Direct Integrability Repair

**Date:** 2026-05-30; repaired 2026-06-06; bridge wired 2026-06-08
**Claim type:** bounded_theorem
**Actual current-surface status:** bounded-support/direct-integrability source
repair with explicit Wigner strong-continuity bridge wired into the restricted
packet; independent audit owns any effective status movement.
**Primary runner:**
`scripts/free_dirac_poincare_generators_selfadjointness_2026-05-30.py`
(SCORECARD PASS=7 FAIL=0).
**Cached runner output:**
`logs/runner-cache/free_dirac_poincare_generators_selfadjointness_2026-05-30.txt`
**Runner JSON:**
`outputs/free_dirac_poincare_generators_selfadjointness_2026_05_30.json`

## Repair Summary

The previous packet tried to close the full Poincare integration step by
exhibiting rapidity Gaussian/Hermite vectors as common analytic vectors for all
ten generators and for a Nelson Laplacian. That route is not correct. In
rapidity coordinates,

```text
E = M_perp cosh(zeta),        p_parallel = M_perp sinh(zeta),
```

so Gaussian moments of `E^n` or `p^n` grow like `exp(c n^2)`, faster than
`R^n n!` for any fixed `R`. The repaired runner checks this obstruction
directly by showing that
`log(||H^n psi||/n!)/n` increases across the tested moments. The Nelson/common
Gaussian claim is therefore removed, not patched.

This note uses the alternate route named by the audit blocker: direct
integrability from the explicit unitary mass-shell/Wigner action supplied by
the companion free-Dirac Poincare packet.

## Inputs

This repair consumes, as bounded upstream context, the companion packet's
explicit free one-particle Poincare representation data:

- positive-energy mass shell `H_m^+`;
- Lorentz-invariant mass-shell measure `d^3p/(2E)`;
- real multiplication generators `H=E(p)` and `P^i=p^i`;
- orbital rotation/boost vector fields and bounded spin/Wigner carrier terms;
- the verified Poincare algebra formulas on the Schwartz mass-shell core.

The concrete companion source packet is:

- note:
  [`FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md);
- runner:
  [`scripts/free_dirac_poincare_representation_2026-05-30.py`](../scripts/free_dirac_poincare_representation_2026-05-30.py);
- cached output:
  [`logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt`](../logs/runner-cache/free_dirac_poincare_representation_2026-05-30.txt).

The functional-analytic bridge requested by the later audit is now an explicit
dependency of this parent packet:

- bridge note:
  [`FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md`](FREE_DIRAC_WIGNER_ACTION_STRONG_CONTINUITY_BRIDGE_NOTE_2026-06-07.md);
- bridge runner:
  [`scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py`](../scripts/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.py);
- bridge cached output:
  [`logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt`](../logs/runner-cache/audit_companion_free_dirac_wigner_action_strong_continuity_bridge_2026_06_07.txt)
  (`SCORECARD PASS=48 FAIL=0`).

This bridge supplies the restricted-packet proof that the displayed
mass-shell/Wigner action is a strongly continuous unitary representation and
that Stone's theorem supplies the one-parameter self-adjoint generators. It
also verifies the companion representation cache as SHA-fresh before running
its own continuity, Wigner-carrier, semidirect-product, and firewall checks.

The paired runner verifies these source anchors before running the direct
integrability checks. This source repair exposes the dependency edge for
independent audit; it does not assert an audit status for the companion or
bridge rows.

This repair does not derive the free Dirac carrier from baseline axioms, does
not prove spin-statistics, and does not claim an interacting theory result.

## Direct Route

For a fixed boost direction and transverse momentum, set

```text
p_parallel = M_perp sinh(zeta),        E = M_perp cosh(zeta).
```

Then

```text
dp_parallel/(2E) = dzeta/2,
E d/dp_parallel = d/dzeta,
K_orb = -i E d/dp_parallel = -i d/dzeta.
```

Thus each one-parameter boost generator is the full-line momentum operator in
rapidity, plus the bounded Hermitian spin/Wigner multiplication term. The
runner checks the rapidity identity, Hermiticity of the full-line boost proxy,
the Cayley/full-range self-adjointness signature, and a half-line control that
fails because norm leaks at the boundary.

The integration step is not Nelson's theorem. It is the direct unitary action:

```text
(U(a,Lambda) psi)(p) =
  exp(i a.p) D(W(Lambda,p)) psi(Lambda^{-1} p).
```

The mass-shell measure is invariant, the translation factor has unit modulus,
and the Wigner carrier is unitary. The companion packet supplies the mass-shell
and carrier/cocycle checks, while the 2026-06-07 Wigner bridge supplies the
functional-analytic consequence: the displayed action is a strongly continuous
unitary representation, and Stone's theorem supplies the self-adjoint
one-parameter generators.

## What Is Proved Here

- Each translation generator is handled as real multiplication on the
  mass-shell Hilbert space.
- Each boost generator is handled one-parameter-at-a-time by the rapidity
  full-line momentum reduction plus bounded spin term.
- Rotations are compact one-parameter unitary flows with the standard
  skew-adjoint orbital plus Hermitian spin generator.
- The group representation is integrated directly by the explicit unitary
  mass-shell action, not by a common Nelson analytic core.

## What Is Not Claimed

- No common Gaussian/Hermite analytic-vector theorem for `H`, `P`, `J`, and
  `K`.
- No Nelson Laplacian essential-self-adjointness claim.
- No claim that this packet proves the full Wigner induced-representation
  theorem from scratch; it consumes the companion packet's explicit carrier and
  cocycle checks.
- No effective retained status before independent audit.

## Runner Checks

The paired runner checks:

- `S1`-`S10`: the parent packet cites the companion representation note/cache
  and the Wigner strong-continuity bridge note/runner/cache, and both caches are
  present, passing, and SHA-fresh.
- `D1`: `K_orb=-i d/dzeta` is Hermitian on the full rapidity line.
- `D2`: the exact identity `E d/dp = d/dzeta` on rapidity test functions.
- `D3`: the boost flow is a strongly continuous unitary one-parameter group.
- `D4`: translation generators act by unit-modulus mass-shell phases.
- `D5`: the old Gaussian Nelson route fails for `H/P`.
- `D6`: the boost Cayley/deficiency finite proxy has the self-adjoint
  full-line signature.
- `D7`: the half-line control is not unitary, so the self-adjointness checks are
  discriminating.

Current output:

```text
SCORECARD PASS=7 FAIL=0
```

No `docs/audit/**` file is edited by this source repair.
