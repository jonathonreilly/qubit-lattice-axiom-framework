---
claim_id: free_dirac_poincare_representation_bounded_note_2026-05-30
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Free Dirac Poincare Algebra and Positive-Energy Support (Bounded)

**Date:** 2026-05-30
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note sets source
claim metadata only; it does not quote, set, or predict audit outcomes.
**Primary runner:** [`scripts/free_dirac_poincare_representation_2026-05-30.py`](../scripts/free_dirac_poincare_representation_2026-05-30.py)

## 0. Scope

This note records bounded support for the free massive Dirac boost/Poincare
sector. It verifies explicit algebraic pieces of the textbook free-field
construction:

- spinor Lorentz generators close `so(3,1)` with the non-compact
  boost-boost sign `[K^i,K^j] = -i eps^{ijk} J^k`;
- the ten generators close `iso(3,1)` in the finite defining representation;
- the scalar orbital mass-shell differential operators close the boost-containing
  brackets on a Gaussian Schwartz core;
- boosts preserve the positive mass shell and the measure `d^3p/(2E)`;
- the free Dirac Hamiltonian has the standard `{+E,+E,-E,-E}` spectrum and the
  CAR-relabelled free Fock Hamiltonian is bounded below;
- the bispinor numerator transforms covariantly under the standard spinor boost.

This is bounded support for a later free-field reconstruction lane. It is not a
proof of the abstract OS-to-Wightman reconstruction theorem, not a proof of
essential self-adjointness of all unbounded generators, not a derivation of a
unitary Poincare group representation from the lattice framework, and not a
spin-statistics theorem.

## 1. Algebraic Content

Using mostly-minus Minkowski gamma matrices,

```text
{gamma^mu, gamma^nu} = 2 eta^{mu nu},    eta = diag(+,-,-,-),
Sigma^{mu nu} = (i/4) [gamma^mu, gamma^nu],
J^i = (1/2) eps^{ijk} Sigma^{jk},        K^i = Sigma^{0i},
```

the spinor generators satisfy

```text
[J^i,J^j] = i eps^{ijk} J^k,
[J^i,K^j] = i eps^{ijk} K^k,
[K^i,K^j] = -i eps^{ijk} J^k.
```

The last sign is the load-bearing Lorentz sign. The runner includes controls
showing that the compact Euclidean sign `[K,K]=+i eps J` and a wrong boost sign
fail.

The finite defining representation check verifies all `iso(3,1)` brackets for
`H`, `P^i`, `J^i`, and `K^i`, including

```text
[H,K^i] = i P^i,
[P^i,K^j] = i delta^{ij} H,
[J^i,P^j] = i eps^{ijk} P^k.
```

These finite-dimensional algebra checks are exact matrix checks. They establish
the signs and convention coherence; they do not by themselves prove a Hilbert
space group representation.

## 2. Mass-Shell Operator Support

On the positive mass shell `E(p)=sqrt(|p|^2+m^2)`, the runner checks the scalar
orbital differential operators

```text
H psi = E(p) psi,
P^i psi = p^i psi,
J^i psi = -i eps^{ijk} p^j d_k psi,
K^i psi = -i E(p) d_i psi
```

on Gaussian Schwartz test functions, using analytic derivatives rather than
finite differences. The checked brackets are

```text
[H,K^i] = i P^i,
[P^i,K^j] = i delta^{ij} H,
[J^i,K^j] = i eps^{ijk} K^k,
[K^i,K^j] = -i eps^{ijk} J^k.
```

This is a core-level algebra check. The spin/Wigner part is checked separately
through the finite spinor Lorentz algebra and Wigner little-group rotation tests;
the runner does not prove the full domain theorem for the momentum-dependent
spin-tensored boost generator.

## 3. Positive Energy, Measure, and Bispinor Covariance

The runner verifies:

- a Lorentz boost maps a point on `H_m^+` to another point on `H_m^+`;
- the induced little-group matrix is a spatial rotation and its `SU(2)` carrier
  is unitary;
- the boost vector field preserves `d^3p/(2E)`, while flat `d^3p` fails the same
  divergence check;
- the free Dirac Hamiltonian has eigenvalues `{+E,+E,-E,-E}`, and after the
  standard CAR particle/antiparticle relabelling the finite-mode free Fock
  Hamiltonian is bounded below by zero;
- the bispinor numerator `p_slash + m` transforms covariantly under the standard
  spinor boost representation.

These are textbook free-field checks. They are useful for making the boost lane
explicit, but they do not derive Lorentz symmetry from the discrete lattice and
do not replace the independent audit of the upstream covariance or mode-algebra
rows.

## 4. What This Claims

- The runner-backed algebraic signs and finite checks for the free massive Dirac
  Poincare sector are internally consistent.
- The explicit free one-particle algebra has the correct non-compact boost sign,
  invariant mass shell, invariant measure, and positive-energy spectrum.
- This packet can serve as bounded support for a later reconstruction theorem
  that separately supplies the OS reconstruction, self-adjointness/domain, and
  statistics-selection steps.

## 5. What This Does Not Claim

- It does not close any downstream reconstruction target unconditionally.
- It does not prove essential self-adjointness, Nelson analytic-vector
  integrability, or exponentiation to a unitary Poincare group representation.
- It does not prove OS-to-Wightman reconstruction, microcausality, or full field
  covariance.
- It does not select CAR statistics or prove spin-statistics.
- It does not derive Lorentz symmetry from the lattice framework; it uses the
  textbook continuum free Dirac/Poincare construction as methodology.
- It does not make an interacting `SU(3)`/`U(1)` claim.
- It adds no axiom, Tier-A admission, fitted value, measured input, or audit
  status.

## 6. Runner

```bash
python3 scripts/free_dirac_poincare_representation_2026-05-30.py
```

Expected result: `SCORECARD PASS=8 FAIL=0`.

The runner checks:

- spinor Lorentz algebra and the `[K,K] = -i eps J` sign;
- full finite defining-representation `iso(3,1)` brackets;
- wrong-sign and Euclidean-sign controls;
- orbital mass-shell bracket closure on Gaussian Schwartz tests;
- mass-shell preservation and Wigner rotation;
- invariant measure preservation;
- positive-energy Dirac spectrum and finite-mode Fock lower bound;
- bispinor covariance under finite boosts.

## 7. Methodology and Dependencies

This note is primarily a textbook-methodology packet for the continuum free Dirac
representation. The runner mirrors conventions used by the existing free Dirac
mode-algebra and free staggered covariance notes, but those rows are not promoted
by this note.

Textbook methodology used as non-graph context: Wigner induced representations,
Dirac spinor calculus, the Poincare Lie algebra, the Lorentz-invariant mass-shell
measure, CAR Fock relabelling of the negative-energy branch, and standard domain
theorems for free-field generators.
