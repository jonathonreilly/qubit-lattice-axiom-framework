# Source-only spectral reflection and the full-affine boundary

**Type:** bounded_theorem

**Date:** 2026-04-17; scope correction 2026-10-21
**Scope:** exact source-only similarity; no general selector-impossibility claim
**Script:** `scripts/frontier_dm_neutrino_source_surface_microscopic_polynomial_impossibility_theorem.py`

The legacy filename is retained. The former microscopic-silence impossibility
claim is withdrawn. Its runner tested source-only matrices but the statement
extended that result to the full affine family and to all microscopic
polynomials. Those extensions do not follow and one is explicitly false.
No audit ledger or verdict is modified by this source correction.

## Exact statement and proof

Use the matrices in the
[active affine chart](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md):

```
T_m = [[1,0,0],[0,0,1],[0,1,0]],
T_delta = [[0,-1,1],[-1,1,0],[1,0,-1]],
T_q = [[0,1,1],[1,0,1],[1,1,0]].
```

For real `m,d,q`, set `H_src=m T_m+d T_delta+q T_q`, **without H_base**.
Let R exchange basis vectors 2 and 3. Direct multiplication gives
`R T_m R^T=T_m`, `R T_q R^T=T_q`, and `R T_delta R^T=-T_delta`.
Since `R^T R=I`,

```
R H_src(m,d,q) R^T = H_src(m,-d,q).
```

Consequently all spectral functions of H_src agree at d and -d. In particular,
trace powers, characteristic coefficients, determinant, the minimum absolute
eigenvalue, and `tr exp(-t H_src^2)` for `t>0` are even in d. Polynomial
spectral invariants therefore depend on `(m,d^2,q)`. For example,
`tr(H_src^2)=3m^2+6d^2+6q^2+4mq`.
This proof uses an explicit reflection similarity, not a general assertion
that cyclic-doublet invariants can only depend on a magnitude.

## Full-affine counterexample

The actual affine matrix is `H=H_base+H_src`, where

```
H_base = [[0,E1,-E1-i/2],[E1,0,-E2],[-E1+i/2,-E2,0]],
E1=sqrt(8/3), E2=sqrt(8)/3.
```

Exact expansion gives

```
tr(H(m,d,q)^2)-tr(H(m,-d,q)^2) = -32 sqrt(6) d/3.
```

This is nonzero for d nonzero, despite trace-square being invariant under
unitary conjugation on the ambient matrix space. Keeping H_base fixed is not
the same as conjugating the entire matrix. Dropping H_base is a change of
family, not a scalar baseline subtraction.

Furthermore Z3 invariance alone permits cubic doublet contractions:
`Re((x+i y)^3)=x^3-3xy^2` is invariant under a 120-degree rotation and is odd
on the line y=0. Thus no general magnitude-only polynomial theorem follows
from cyclic symmetry. The source-only reflection above is the required extra
algebraic fact.

## What the result does and does not select

Source-only spectral functions cannot distinguish d from -d when both points
are in the considered domain. The chamber `q>=E1-d` is not itself invariant
under this reflection. On a prescribed d>=0 branch, evenness places no
obstruction to selecting a magnitude or a unique point. Even a polynomial
such as `(d^2-a^2)^2+(q-b)^2` has a unique minimum at `(a,b)` on d>=0 for
supplied a>0,b; this is a logical counterexample to the parity inference,
not a proposed physical selector.

Neither finite lists of candidate functionals nor the coordinate count prove
that all microscopic content is exhausted. Schur scalarity fixes an operator
form conditional on commutation; it does not fix the scalar's value, and
`m T_m` must not be identified with `m I` without a separate bridge. No chiral
Ward identity or physical gauge equivalence is established by spectral
reflection alone. Source parameters that change observables cannot simply be
called gauge freedoms on the basis of this calculation.

A physical source-selection rule remains to be justified. This result neither
derives one nor rules out local, nonlocal, variational, or dynamical routes.
The [information-geometric calculation](DM_NEUTRINO_SOURCE_SURFACE_INFO_GEOMETRIC_SELECTION_OBSTRUCTION_NOTE_2026-04-17.md)
is likewise a conditional local expansion, not an exhaustive no-go.

## Verification

Run the named script. It checks exact generator conjugations, source-only
similarity, full-affine trace-square difference, and the cyclic cubic example,
while comparing exact matrices against the production chart helpers.
These replace the previous random-sample extrapolations and literal-True
impossibility assertions. The previous 35-PASS receipt is superseded.
