# Gauge-Vacuum Plaquette First-Sector Minimal-Bulk Completion Principle

**Date:** 2026-04-19 (originally); 2026-07-27 (finite-cone proof completed)
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py`](../scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py)

## Claim

Let

```text
W_5 = {(p,q): 0 <= p,q <= 5}
R   = {(0,0), (1,0), (0,1), (1,1)}
```

be the 36-slot dominant-weight box and retained support used by the runner.
Fix the displayed nonnegative conjugation-symmetric retained packet
`rho_ret` on `R`, and let `E(rho_ret)` be the set of all **full packets on
this finite box** that are nonnegative, conjugation-symmetric, and restrict
to `rho_ret` on `R`.  The phrase "full packet" below means all slots of
`W_5`; no claim about an infinite dominant-weight lattice is made.

Let `rho_0` equal `rho_ret` on `R` and zero off `R`.  Then:

1. `rho_0` is the unique least element of `E(rho_ret)` in coefficient
   order.
2. Every coefficient-order-monotone bulk-tail functional is minimized at
   `rho_0`.  The minimizer is unique for every functional that is strictly
   positive on every nonzero admissible tail.  This class includes positive
   weighted tail mass, positive weighted `p`-mass for every `p > 0`, and
   positive weighted support size; hence it includes all four functionals
   printed by the runner.
3. In the finite canonical factorized model

   ```text
   T(rho) = M D_loc diag(rho) M,
   M = exp(beta J / 2),
   ```

   where the runner verifies that `M` is real symmetric and invertible and
   that `D_loc` is strictly positive diagonal, `T(rho_0)` is the unique
   least element of `{T(rho): rho in E(rho_ret)}` in Loewner order.

Thus coefficient minimality, functional minimality, and finite-box Loewner
minimality are separate consequences of one explicit tail-cone
decomposition.  They are not asserted as definitionally equivalent.

## Proof

Write `tau(p,q) = (q,p)`.  The non-retained slots split into disjoint
`tau`-orbits.  For each such orbit `O`, let `g_O` be its indicator.  If
`rho` is in `E(rho_ret)`, then

```text
delta = rho - rho_0 = sum_O a_O g_O,       a_O >= 0.                 (1)
```

Indeed, `delta` vanishes on `R`, is nonnegative, and is constant on every
conjugation orbit.  Conversely every sum in (1) is an admissible tail.
Because the orbit supports are disjoint, the coefficients `a_O` are unique.

Equation (1) gives `rho_0 <= rho` coefficientwise for every admissible
extension.  If another extension were also a least element, it would be at
most `rho_0`; equality on `R` and nonnegativity off `R` then force it to be
`rho_0`.  This proves item 1 without a randomized or finite-witness
inference.

If `F` is coefficient-order-monotone, item 1 gives
`F(rho_0) <= F(rho)`.  If in addition

```text
F(rho_0 + delta) > F(rho_0)
```

for every nonzero admissible `delta`, the minimizer is unique.  In
particular, for weights `c_w > 0`, the functionals

```text
F_{c,p}(rho_0 + delta) = sum_{w off R} c_w delta_w^p,   p > 0,
S_c(rho_0 + delta)     = sum_{w off R} c_w 1[delta_w > 0]
```

vanish at `delta = 0` and are strictly positive for every nonzero
nonnegative tail.  Total tail mass has `c_w = 1, p = 1`; dimension-weighted
mass has `c_w = dim(w), p = 1`; squared `l2` mass has `c_w = 1, p = 2`; and
support size has `c_w = 1` in `S_c`.  This proves item 2.  Merely
nonnegative weights would not ensure uniqueness, which is why strict
positivity on every tail slot is part of the statement.

Finally, put `A_O = D_loc diag(g_O)`.  Since both factors are diagonal,
`A_O` is nonnegative diagonal.  For an arbitrary admissible tail, linearity
and (1) give

```text
T(rho_0 + delta) - T(rho_0)
  = M D_loc diag(delta) M
  = sum_O a_O M A_O M.                                      (2)
```

For every real vector `x`, symmetry of `M` gives

```text
x^T M D_loc diag(delta) M x
  = (M x)^T D_loc diag(delta) (M x) >= 0,
```

so (2) is positive semidefinite for **every** admissible tail, not only the
two old witnesses.  If `delta` is nonzero, strict positivity of the diagonal
of `D_loc` makes `D_loc diag(delta)` nonzero.  Invertibility of `M` makes
congruence by `M` injective, so the increment in (2) is nonzero.  Hence no
other admissible extension has the same transfer, and `T(rho_0)` is the
unique Loewner-least transfer.  The nonzero increment need not be positive
definite; nonzero positive semidefiniteness is the exact conclusion.

## Scope and boundaries

The theorem is universal over the admissible nonnegative
conjugation-symmetric tails on `W_5`.  It is not inferred from 64 random
tails or from the two named tails A and B; those are retained only as
regression examples in the runner.

The theorem does not address an infinite-weight completion, convergence of
an infinite transfer operator, signed tails, a non-diagonal local factor, or
selection of the actual framework-point Wilson environment packet.  It
adds no physical selector axiom.

The Loewner conclusion uses the displayed factorization and the explicit
finite-box hypotheses `M = M^T`, `M` invertible, and `D_loc > 0`.  It is not
a consequence of coefficient order for an arbitrary transfer map.

## Dependency closure

The proof above is a finite-dimensional conditional algebra theorem for the
packet and matrices constructed by the primary runner.  It does not import a
universal minimality conclusion from upstream prose.  The concrete packet and
local-factor inputs do come through the linked in-tree helper chain, so those
sources remain explicit audit-graph dependencies.  The runner directly
verifies every hypothesis used by the new arbitrary-tail step:

- the retained packet is finite, normalized, nonnegative, and
  conjugation-symmetric;
- the orbit generators partition every non-retained slot;
- `M` is symmetric and nonsingular on `W_5`;
- every diagonal entry of `D_loc` is strictly positive;
- every tail-orbit generator produces a nonzero PSD congruence increment.

The source notes for the retained packet and finite factorized model are:

- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TRUNCATED_ENVIRONMENT_PACKET_NOTE_2026-04-19.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_TRUNCATED_ENVIRONMENT_PACKET_NOTE_2026-04-19.md)
- [GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_ZERO_EXTENSION_FACTORIZED_CLASS_THEOREM_NOTE_2026-04-19.md](GAUGE_VACUUM_PLAQUETTE_FIRST_SECTOR_ZERO_EXTENSION_FACTORIZED_CLASS_THEOREM_NOTE_2026-04-19.md)

Their audit status is owned by the independent audit lane; this note does
not promote either row, and its own retained-grade propagation remains
conditional on the audit graph.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_gauge_vacuum_plaquette_first_sector_minimal_bulk_completion_principle_theorem_2026_04_19.py
```

Expected:

```text
PASS=8 FAIL=0
```

The analytic proof above establishes the arbitrary-tail implication.  The
runner checks its finite-box hypotheses and exhausts the finitely many
conjugation-orbit generators of the tail cone.
