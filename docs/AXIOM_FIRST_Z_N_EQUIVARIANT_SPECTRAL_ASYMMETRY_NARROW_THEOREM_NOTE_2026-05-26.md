# Finite Z_N Spectral-Asymmetry Weight-Sum Theorem (Bounded)

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set, predict, or estimate any audit verdict. Effective status is
pipeline-derived after independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py`](../scripts/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.py)
**Cached log:**
[`logs/runner-cache/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.txt`](../logs/runner-cache/frontier_z_n_equivariant_spectral_asymmetry_narrow_verifier.txt)
(PASS=33 FAIL=0)

## 2026-06-03 Scope Repair: admissible weights

The local weight-sum statement is restricted to **admissible transverse
weights**: each `a_j` is a unit modulo `N`, equivalently
`gcd(a_j, N) = 1`. This is the exact condition that prevents a denominator
`zeta_N^(k a_j) - 1` from vanishing for some `1 <= k <= N-1`.

The earlier broad phrase "nonzero modulo `N`" is correct only when `N` is
prime. For composite `N`, a nonzero nonunit weight can make the local
expression singular; for example `N=4`, `a=2`, and `k=2` gives
`zeta_4^(k a) = zeta_4^4 = 1`. Those non-admissible tuples are now explicitly
outside this theorem's finite local-weight-sum claim.

The load-bearing `N=3` calculation is unchanged: modulo 3, the
nonzero weights `1` and `2` are units, so `(1,2)`, `(1,1)`, and `(2,2)` are
all admissible.

## Review-Loop Boundary

This note is the salvageable algebraic core from PR #1961. The
submitted branch framed the result as an internal derivation of the APS
equivariant eta fixed-point formula. Review-loop narrows that claim:
the landed theorem is a finite-dimensional spectral-asymmetry and
cyclotomic weight-sum calculation. It does **not** prove the continuum
APS formula, does **not** derive the fixed-point denominator from a
framework Dirac operator, and does **not** retire any textbook APS
import by itself.

The useful bounded content is still real: the finite eta trace is a
well-defined algebraic object, and the C3 transverse-weight sum
`(1,2;3)` evaluates exactly to `2/9`.

## Framework Boundary

The framework baseline is
[`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md):
one qubit at every site of the Z3 spatial substrate. This note does
not introduce a new axiom, substrate, dynamics rule, or physical
identification.

The only framework-side structural input used for the N=3 weight choice
is the retained-bounded C3 circulant/parity surface
[`NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md`](NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md),
which supplies the body-diagonal C3 character pattern `(1, omega,
omega^2)` as bounded support. Downstream physics that identifies this
weight sum with a charged-lepton phase remains separate and unaudited
unless independently proved.

## Statement

Let `H` be finite-dimensional over C, let `g` be unitary with `g^N =
1`, and let `T` be self-adjoint with `[T,g]=0`.

1. The finite equivariant spectral asymmetry
   `eta_g(T) = sum_{lambda != 0} sign(lambda) tr(g | ker(T-lambda))`
   is well-defined and lies in `Z[zeta_N]`.
2. If a continuous self-adjoint path `T(s)` commutes with `g` and has
   no zero crossing, then `eta_g(T(s))` is constant along the path.
3. For a specified admissible transverse weight tuple
   `a = (a_1,...,a_n)` with every `gcd(a_j,N)=1`, define the finite local
   weight sum
   `L_N(a) = (1/N) sum_{k=1}^{N-1} prod_j 1/(zeta_N^(k a_j)-1)`.
   This is a finite cyclotomic expression. This note evaluates it; it
   does not prove that every physical fixed-point problem reduces to it.
4. For `N=3` and the C3-compatible transverse weights `(1,2)`,
   `L_3(1,2) = 2/9` exactly. The alternative repeated weights
   `(1,1)` and `(2,2)` evaluate to `1/9`.

## Proof Sketch

Since `[T,g]=0`, every nonzero eigenspace of `T` is `g`-invariant.
The trace of `g` on such an eigenspace is a finite sum of N-th roots of
unity, hence an element of `Z[zeta_N]`; the sum defining `eta_g(T)` is
finite. Along a path with no zero crossing, the sign of each spectral
block cannot change, and the finite character trace is locally constant.

For the local weight sum, the expression is finite for admissible weights
because no denominator `zeta_N^(k a_j)-1` vanishes when
`1 <= k <= N-1` and `gcd(a_j,N)=1`: if `zeta_N^(k a_j)=1`, then
`N` divides `k a_j`; since `a_j` is a unit modulo `N`, `N` divides `k`,
contradicting `1 <= k <= N-1`. Conversely, if `a_j` is a nonzero nonunit
modulo composite `N`, then `k=N/gcd(a_j,N)` gives `1 <= k <= N-1` and
`N | k a_j`, so the corresponding denominator vanishes. Thus the finite
local-weight claim is exactly the unit-weight/admissible case. At `N=3`,
write `omega = zeta_3`. Then

```text
(omega - 1)(omega^2 - 1)
  = omega^3 - omega^2 - omega + 1
  = 2 - (omega + omega^2)
  = 3
```

using `1 + omega + omega^2 = 0`. Therefore

```text
L_3(1,2)
  = (1/3) [1/((omega-1)(omega^2-1))
          + 1/((omega^2-1)(omega^4-1))]
  = (1/3) [1/3 + 1/3]
  = 2/9.
```

The paired runner verifies these identities numerically and, when
SymPy is available, symbolically in `Q[omega]/(omega^2+omega+1)`.

## Honest Residuals

- No continuum APS eta invariant on a real lens space is proved.
- No Atiyah-Patodi-Singer fixed-point theorem is derived from the
  framework.
- No proof is given that a concrete framework Dirac operator produces
  the local denominator `prod_j (zeta_N^(k a_j)-1)^(-1)`.
- No finite local-weight claim is made for non-admissible/nonunit weights
  modulo composite `N`; those tuples can have vanishing denominators.
- No identification with `delta_Brannen`, Koide phases, masses, or
  phenomenology is claimed.
- No existing audit row is edited, retired, or promoted by this note.

## External Context

APS, Donnelly, Hirzebruch-Zagier, Atiyah-Singer, and Atiyah-Bott
explain why this finite cyclotomic expression is the right sidecar
object to carry. They are context only. A successor that wants to
retire a textbook APS import must prove the missing fixed-point and
operator-realization bridge explicitly.

## Audit Handoff

This source note requests independent audit of the bounded finite
spectral-asymmetry and weight-sum theorem above. It does not apply
audit results, edit existing audit rows, set `audit_status`, set
`effective_status`, or request promotion of any downstream source note.
