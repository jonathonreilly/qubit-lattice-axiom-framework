# Spatial `SO(3)` Casimir Decomposition on `Sym^2(R^4)`

**Claim type:** positive_theorem
**Status authority:** source-note proposal only; audit verdict and effective
status are set by the independent audit lane.
**Date:** 2026-04-14
**Updated:** 2026-07-10 (restricted-packet closure: explicit complement
generator matrices, Casimir multiplication, and polynomial projectors)
**Role:** neutral finite-dimensional representation theorem on a stipulated
`R + R^3` decomposition
**Primary runner:** [`scripts/frontier_universal_gr_casimir_block_localization.py`](../scripts/frontier_universal_gr_casimir_block_localization.py)
**Cached runner output:** [`logs/runner-cache/frontier_universal_gr_casimir_block_localization.txt`](../logs/runner-cache/frontier_universal_gr_casimir_block_localization.txt)
(`runner_sha256 = 5f4a8545b623e294b886754017fbe9b3e666a26fc474b215daf6fc738f2a322e`; `exit_code = 0`; `status = ok`; `PASS=8 FAIL=0 TOTAL=8`).

## Claim (neutral representation theorem)

Let `V := Sym^2(R^4)` be the real 10-dimensional space of symmetric `4 x 4`
real matrices in coordinate order `(t, x, y, z)`, equipped with the
Frobenius inner product `<a, b> := sum_{i,j} a_{ij} b_{ij}`. Let `SO(3)` act
on the right of `V` by `rho(R) h := R^T h R` with `R = diag(1, R_3)` and
`R_3 in SO(3)`, i.e. the spatial-block action holding the temporal index
fixed.
Let `B := (e_0, e_1, ..., e_9)` be the orthonormal frame on `V` defined in
[Representation Fixed in the Packet](#representation-fixed-in-the-packet)
below.

Define the rank-2 projector

```
Pi_lapse_trace := diag(1, 0, 0, 0, 1, 0, 0, 0, 0, 0)
                                                       (matrix on V in basis B)
```

onto `(h_tt, (h_xx + h_yy + h_zz)/sqrt(3))`, and let
`Pi_perp := I - Pi_lapse_trace` be the rank-8 complement projector. Let
`G_x, G_y, G_z` be the infinitesimal generators of `rho` on `V` in basis
`B`, restricted to the complement, and define the Casimir operator

```
C := G_x^2 + G_y^2 + G_z^2  on  range(Pi_perp).
```

Define `P_lapse, P_shift, P_trace, P_shear` to be the spectral projectors
of `C` together with the trivial-irrep refinement on
`range(Pi_lapse_trace)`:

- `P_lapse := diag(1, 0, 0, 0, 0, 0, 0, 0, 0, 0)`
- `P_trace := diag(0, 0, 0, 0, 1, 0, 0, 0, 0, 0)`
- `P_shift := lift_to_V(Pi_{C = -2} on range(Pi_perp))`
- `P_shear := lift_to_V(Pi_{C = -6} on range(Pi_perp))`

**Theorem (spatial `SO(3)` Casimir decomposition).** With definitions as above, the following
exact identities hold over `Q[sqrt 2, sqrt 3, sqrt 6]` SymPy radicals:

1. **(T1) Basis is orthonormal.** The Gram matrix `(<e_i, e_j>)_{i,j}` of
   `B` is the `10 x 10` identity.
2. **(T2) Generators close the opposite `so(3)` convention exactly.** For
   the fixed action and axis matrices, `[G_a, G_b] = -epsilon_{abc} G_c`
   for `(a, b, c) in {(x, y, z), (y, z, x), (z, x, y)}`, computed
   entrywise. The uniform minus sign occurs because `h -> R^T h R` is an
   anti-representation for the chosen composition order; replacing every
   `G_a` by `-G_a` gives the standard positive-sign convention and leaves
   `C` unchanged.
3. **(T3) `Pi_lapse_trace` is `SO(3)`-invariant.**
   `Pi_lapse_trace G_a Pi_perp = 0` and
   `Pi_perp G_a Pi_lapse_trace = 0` for each `a in {x, y, z}`.
   Equivalently, `range(Pi_lapse_trace)` and its orthogonal complement are
   each `so(3)`-stable.
4. **(T4) Complement Casimir spectrum.** In the displayed complement
   ordering `(h_{tx}, h_{ty}, h_{tz}, q_1, q_2, h_{xy}, h_{xz}, h_{yz})`
   with `q_1 := (h_{xx} - h_{yy})/sqrt 2`,
   `q_2 := (h_{xx} + h_{yy} - 2 h_{zz})/sqrt 6`,
   the complement Casimir is diagonal:
   `diag(C) = (-2, -2, -2, -6, -6, -6, -6, -6)`,
   off-diagonal entries identically zero. Hence the spectrum is `-2` with
   multiplicity `3` and `-6` with multiplicity `5`.
5. **(T5) Rank table.** `rank(P_lapse) = 1`, `rank(P_shift) = 3`,
   `rank(P_trace) = 1`, `rank(P_shear) = 5`.
6. **(T6) Projector algebra.** `{P_lapse, P_shift, P_trace, P_shear}` is
   exact, mutually orthogonal, idempotent, and complete (sums to `I_10`).
7. **(T7) Equivariance.** `[P_block, G_a] = 0` for each
   `P_block in {P_lapse, P_shift, P_trace, P_shear}` and each
   `a in {x, y, z}`.
8. **(T8) Coordinate landing.** In basis `B`, `P_shift` projects exactly
   onto the shift coordinates `(h_{tx}, h_{ty}, h_{tz})` and `P_shear`
   projects exactly onto the traceless-symmetric spatial coordinates
   `(q_1, q_2, h_{xy}, h_{xz}, h_{yz})`.

**Neutral representation interpretation.** With the real anti-Hermitian convention used here, the
eigenvalues `-2` and `-6` are `-j(j+1)` for `j = 1` and `j = 2`. So the
complement decomposes representation-theoretically as a `j = 1` mixed
time-space block plus a `j = 2` traceless-spatial block, and the rank-two
trivial block decomposes into `h_tt` and spatial trace. Conventional ADM names
and the possible Universal-GR interpretation are separated into
`UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_CONTEXT_NOTE_2026-07-11.md`; they are not
part of this theorem's claim surface.

## Scope and audit boundary

This is a representation-level decomposition theorem on
`V = Sym^2(R^4)` with the spatial-block right `SO(3)` action
`rho(R) h = R^T h R`, `R = diag(1, R_3)`. Relative to the stipulated
temporal line, Euclidean spatial complement, and Frobenius metric, the note
proves the four-block decomposition
`V = range(P_lapse) (+) range(P_shift) (+) range(P_trace) (+) range(P_shear)`
with explicit ranks, exact projector algebra, and exact `so(3)`-equivariance.
The `j=1`/`j=2` split is canonical on `range(Pi_perp)` because its two pieces
are distinct Casimir eigenspaces. The lapse/trace split is canonical only
relative to the stipulated `R e_0 (+) R^3` temporal/spatial decomposition;
`SO(3)` alone cannot distinguish the two trivial irreducible summands.

It does **not** prove a preferred frame inside either irreducible eigenspace,
or any spacetime, Hessian, connection, dynamics, or physical-observable
identification. Those interpretations are outside the neutral theorem and are
listed only in the separate meta context note.

## Standard finite-dimensional mathematical inputs

Every step in the proof-walk below relies only on the elementary
linear-algebra facts collected here. These are standard mathematical inputs,
not physical admissions and not new repo axioms.

- **(BA-1) Real linear algebra on `Sym^2(R^4)`.** Frobenius inner product
  `<a, b> = sum_{i,j} a_{ij} b_{ij}`, additivity, and standard matrix
  arithmetic over `R`.
- **(BA-2) Orthogonality of `SO(3)`.** For `R_3 in SO(3)`,
  `R_3^T R_3 = R_3 R_3^T = I_3` and `det(R_3) = 1`. Hence
  `R = diag(1, R_3)` satisfies `R^T R = I_4` and `det(R) = 1`.
- **(BA-3) `so(3)` Lie algebra structure constants.** The three real
  antisymmetric `3 x 3` generators `(A_x, A_y, A_z)` defined by
  `(A_a)_{ij} = -epsilon_{aij}` (matching the runner's
  `so3_generator`) satisfy `[A_a, A_b] = epsilon_{abc} A_c`. The induced
  matrices for `h -> R^T h R` satisfy `[G_a,G_b] = -epsilon_{abc}G_c`
  because this action has the opposite composition order.
- **(BA-4) Exact arithmetic in
  `K := Q[sqrt 2, sqrt 3, sqrt 6]`.** All entries appearing in
  `B`, `Pi_lapse_trace`, the lifted generators, the Casimir, and its spectral
  projectors lie in `K`. Equality `sp.simplify(expr) == 0` over `K` is
  decidable in SymPy; the runner uses this decision procedure for every
  check.
- **(BA-5) Spectral theorem in finite dimensions.** A self-adjoint
  (symmetric in real basis) linear operator on a finite-dimensional inner
  product space has a unique decomposition into orthogonal projectors onto
  its eigenspaces. Specialization: a real diagonal matrix has spectral
  projectors equal to the indicator diagonals on its eigenvalues.

(BA-1) through (BA-5) are the only mathematical inputs. No physical input is
load-bearing in the present theorem.

## Representation fixed in the packet

Coordinate order is `(t, x, y, z)`. The orthonormal polarization frame `B`
on `V = Sym^2(R^4)` (Frobenius inner product) is:

1. `e_0 = h_tt`                          (lapse)
2. `e_1, e_2, e_3 = h_tx, h_ty, h_tz`   (shift)
3. `e_4 = (h_xx + h_yy + h_zz) / sqrt 3` (spatial trace)
4. `e_5 = (h_xx - h_yy) / sqrt 2`        (shear `q_1`)
5. `e_6 = (h_xx + h_yy - 2 h_zz) / sqrt 6` (shear `q_2`)
6. `e_7, e_8, e_9 = h_xy, h_xz, h_yz`   (shear off-diagonal)

with the off-diagonal symmetric tensors normalized as
`(E_{ab} + E_{ba}) / sqrt 2`. Spatial rotations act on the right by
`rho(R) h := R^T h R` with `R = diag(1, R_3)`, `R_3 in SO(3)`. The
infinitesimal generators on `V` are

```
(G_a)_{ij} := <e_i, A_a^T e_j + e_j A_a>,         a in {x, y, z},
```

where `A_a` is the embedded skew `4 x 4` generator
`A_a := diag(0, 0, 0, 0) +` (the canonical `3 x 3` axis rotation `A_a^{3D}`
embedded in indices `(1, 2, 3)`), per the runner constructor
`so3_generator` and `lifted_generator`.

## Explicit complement calculation (restricted-packet closure)

This section contains the load-bearing calculation in the note itself, so it
does not require the auditor to follow a runner link.  Write the complement
in the fixed order

```
S := (h_tx, h_ty, h_tz, q_1, q_2, h_xy, h_xz, h_yz).
```

For the spatial-axis matrices fixed above, differentiating
`rho(exp(theta A_a))h` at `theta = 0` gives
`L_a(h) = A_a^T h + h A_a`.  Taking the ten Frobenius coefficients
`<e_i,L_a(e_j)>` and deleting the lapse/trace rows and columns gives the
following three matrices on `S`.  Thus every entry below follows directly
from the displayed basis tensors and the displayed differential action; no
representation label or Casimir eigenvalue is used as an input.

```
G_x =
[ 0  0  0 |  0       0  0  0  0 ]
[ 0  0  1 |  0       0  0  0  0 ]
[ 0 -1  0 |  0       0  0  0  0 ]
-------------+----------------------
[ 0  0  0 |  0       0  0  0 -1 ]
[ 0  0  0 |  0       0  0  0  sqrt(3) ]
[ 0  0  0 |  0       0  0  1  0 ]
[ 0  0  0 |  0       0 -1  0  0 ]
[ 0  0  0 |  1 -sqrt(3)  0  0  0 ]

G_y =
[ 0  0 -1 |  0       0  0  0  0 ]
[ 0  0  0 |  0       0  0  0  0 ]
[ 1  0  0 |  0       0  0  0  0 ]
-------------+----------------------
[ 0  0  0 |  0       0  0 -1  0 ]
[ 0  0  0 |  0       0  0 -sqrt(3)  0 ]
[ 0  0  0 |  0       0  0  0 -1 ]
[ 0  0  0 |  1  sqrt(3)  0  0  0 ]
[ 0  0  0 |  0       0  1  0  0 ]

G_z =
[ 0  1  0 |  0  0  0  0  0 ]
[-1  0  0 |  0  0  0  0  0 ]
[ 0  0  0 |  0  0  0  0  0 ]
-------------+-----------------
[ 0  0  0 |  0  0  2  0  0 ]
[ 0  0  0 |  0  0  0  0  0 ]
[ 0  0  0 | -2  0  0  0  0 ]
[ 0  0  0 |  0  0  0  0  1 ]
[ 0  0  0 |  0  0  0 -1  0 ]
```

The vertical/horizontal separators only display the `3 + 5` coordinate
split; they are not additional assumptions.  Ordinary exact matrix
multiplication now gives

```
G_x^2 + G_y^2 + G_z^2
  = diag(-2, -2, -2, -6, -6, -6, -6, -6) =: C.
```

For example, the only nonzero off-diagonal terms in the `q_1,q_2` corner
of the three squares are `+sqrt(3)` from `G_x^2` and `-sqrt(3)` from
`G_y^2`; they cancel.  All other off-diagonal terms vanish separately or
cancel in the same displayed multiplication.  Therefore

```
det(lambda I_8 - C) = (lambda + 2)^3 (lambda + 6)^5,
(C + 2 I_8)(C + 6 I_8) = 0.
```

Because the two roots are distinct, Lagrange interpolation constructs the
two spectral projectors from `C` alone:

```
P_shift^perp = (C + 6 I_8) / 4
              = diag(1, 1, 1, 0, 0, 0, 0, 0),
P_shear^perp = -(C + 2 I_8) / 4
              = diag(0, 0, 0, 1, 1, 1, 1, 1).
```

The factorization immediately gives idempotence, orthogonality, and
`P_shift^perp + P_shear^perp = I_8`; the displayed diagonals give ranks
three and five.  Lifting these two matrices by zero on `(e_0,e_4)` and
adjoining `P_lapse = e_0 e_0^T`, `P_trace = e_4 e_4^T` proves the four
projectors and their coordinate landing. The runner-facing names *shift* and
*shear* are coordinate mnemonics only: they select `h_ti` and traceless
spatial `h_ij`. No ADM, Universal-GR, Einstein/Regge, or preferred-frame
interpretation is part of the positive theorem.

## Proof-walk

Each step is a class-(A) algebraic identity reducible to (BA-1)–(BA-5). The
runner executes the corresponding check at exact precision in
`K = Q[sqrt 2, sqrt 3, sqrt 6]`. Step numbers are aligned to the
theorem-statement parts (T1)–(T8) above and to the eight `record(...)` calls
in
[`scripts/frontier_universal_gr_casimir_block_localization.py`](../scripts/frontier_universal_gr_casimir_block_localization.py).

| Step | Claim (T#) | Reduction | Runner check |
|---|---|---|---|
| 1 | (T1) `Gram(B) = I_10` | (BA-1): direct Frobenius pairing of each `(e_i, e_j)` reduces to a `K`-rational sum; off-diagonal pairings vanish by mutual support / sign cancellation; diagonal pairings normalize by construction. | `basis_orthonormal == True` |
| 2 | (T2) `[G_a, G_b] = -epsilon_{abc} G_c` | (BA-3) gives the positive-sign bracket on the embedded `A_a`. Direct expansion of `L_A(h)=A^T h+hA` gives `[L_A,L_B]=-L_[A,B]` for the chosen right-action composition order. The runner checks the same uniform minus sign for all three cyclic pairs entrywise. | `so3_closure_exact == True` |
| 3 | (T3) `Pi_lapse_trace G_a Pi_perp = Pi_perp G_a Pi_lapse_trace = 0` | (BA-2): the spatial trace `tr(h_{ij})` is `SO(3)`-invariant under `R_3 in SO(3)` because `tr(R_3^T h_{ij} R_3) = tr(h_{ij})` (cyclic trace plus `R_3 R_3^T = I_3`). The lapse `h_tt` is trivially invariant because `R` fixes the `t` index. Thus `rho(R)` preserves `range(Pi_lapse_trace) = span(e_0,e_4)` and its orthogonal complement, so both off-diagonal generator blocks vanish. | `lapse_trace_complement_mixing_zero == True` |
| 4 | (T4) `diag(C) = (-2, -2, -2, -6, -6, -6, -6, -6)`, off-diagonal zero | The preceding restricted-packet calculation displays all three `G_a` matrices. Their ordinary exact squared sum is the displayed diagonal `C`; hence its characteristic polynomial is `(lambda+2)^3(lambda+6)^5` and its minimal polynomial is `(lambda+2)(lambda+6)`. No `j` label is used to obtain either eigenvalue. | `G_{x,y,z} complement rows = ...`; `Casimir complement rows = ...`; `Casimir polynomial identity (C+2I)(C+6I) zero = True` |
| 5 | (T5) ranks `(1, 3, 1, 5)` | The explicit Lagrange formulas `P_shift^perp=(C+6I)/4` and `P_shear^perp=-(C+2I)/4` give complementary indicator diagonals of ranks 3 and 5. The trivial-irrep refinement on `range(Pi_lapse_trace)` splits into `range(P_lapse)` (rank 1, `e_0`) and `range(P_trace)` (rank 1, `e_4`). | `spectral projector polynomial formulas exact = True`; `ranks = {lapse: 1, shift: 3, trace: 1, shear: 5}` |
| 6 | (T6) projector algebra exact | The four projectors are diagonal in basis `B` with disjoint support, so orthogonality `P_i P_j = 0 (i != j)` and idempotence `P_i^2 = P_i` are entrywise identities; completeness follows from the union of their supports covering `{0, 1, ..., 9}`. (BA-1), (BA-5). | `projector complete = True`; `projector orthogonal = True`; `projector idempotent = True` |
| 7 | (T7) `[P_block, G_a] = 0` | Each spectral projector commutes with the operator whose eigenspace it projects onto (BA-5). For `C`-eigenprojectors `P_shift` and `P_shear`, this gives `[P_shift, C] = [P_shear, C] = 0`. The stronger statement `[P_shift, G_a] = [P_shear, G_a] = 0` follows because each `G_a` preserves each `C`-eigenspace (consequence of (T3) plus the fact that `[G_a, C] = 0` on the complement by Casimir-element centrality in `U(so(3))`). For `P_lapse` and `P_trace`, equivariance is the trivial-irrep statement: lapse and spatial-trace channels carry the trivial representation and are pointwise fixed by `rho(R)`; infinitesimally, `G_a` acts as zero on `range(P_lapse)` and on `range(P_trace)`. | `commutes: lapse=True, trace=True, shift=True, shear=True` |
| 8 | (T8) coordinate-landing diagonals | By the definition of the projectors as spectral projectors of the diagonal Casimir on the complement in basis `B`, `P_shift = diag(1, 1, 1, 0, 0, 0, 0, 0)` on the complement (selecting `(h_{tx}, h_{ty}, h_{tz})`) and `P_shear = diag(0, 0, 0, 1, 1, 1, 1, 1)` on the complement (selecting `(q_1, q_2, h_{xy}, h_{xz}, h_{yz})`). | `diag P_shift on complement = [1, 1, 1, 0, 0, 0, 0, 0]`; `diag P_shear on complement = [0, 0, 0, 1, 1, 1, 1, 1]` |

Every load-bearing input above is in (BA-1)–(BA-5). Chain closes from the
standard finite-dimensional linear-algebra package alone. No retained-grade
upstream theorem is invoked as a premise for the block-localization claim
on the abstract pair `(V, rho)`; the cluster's upstream notes (listed in
[Provenance and non-dependencies](#provenance-and-non-dependencies)) supply
context that motivates the choice of representation and the physical block
labels, but are not load-bearing for the algebraic theorem itself.

## Cached runner output

The runner is fully reproducible and self-contained (imports `sympy` only;
constructs every check from scratch). Cached output is at
[`logs/runner-cache/frontier_universal_gr_casimir_block_localization.txt`](../logs/runner-cache/frontier_universal_gr_casimir_block_localization.txt)
with `runner_sha256 = 5f4a8545b623e294b886754017fbe9b3e666a26fc474b215daf6fc738f2a322e`
and `exit_code = 0`. Key cached values:

```text
basis_orthonormal = True
so3_closure_exact = True
lapse_trace_complement_mixing_zero = True
G_x complement rows = [['0', '0', '0', ...], ...]
G_y complement rows = [['0', '0', '-1', ...], ...]
G_z complement rows = [['0', '1', '0', ...], ...]
Casimir complement rows = [['-2', '0', ...], ..., ['0', ..., '-6']]
Casimir diagonal on complement = [-2, -2, -2, -6, -6, -6, -6, -6]
Casimir off-diagonal zero on complement = True
Casimir polynomial identity (C+2I)(C+6I) zero = True
spectral projector polynomial formulas exact = True
ranks = {'lapse': 1, 'shift': 3, 'trace': 1, 'shear': 5}
projector complete = True
projector orthogonal = True
projector idempotent = True
commutes: lapse=True, trace=True, shift=True, shear=True
diag P_shift on complement = [1, 1, 1, 0, 0, 0, 0, 0]
diag P_shear on complement = [0, 0, 0, 1, 1, 1, 1, 1]

[EXACT] PASS: the displayed 10D polarization basis is exactly orthonormal
[EXACT] PASS: the lifted spatial generators close the SO(3) Lie algebra exactly
[EXACT] PASS: Pi_lapse_trace is invariant and its complement is an invariant subrepresentation
[EXACT] PASS: the complement Casimir has exactly the j=1 and j=2 split
[EXACT] PASS: the spectral projectors define a canonical shift/shear split on the complement
[EXACT] PASS: the four block projectors are exact, orthogonal, and complete
[EXACT] PASS: the block projectors commute with the universal SO(3) generators
[EXACT] PASS: in the displayed fixed basis the Casimir projectors land on the expected coordinates

PASS=8 FAIL=0 TOTAL=8
```

## Verification

Re-run from a clean working tree with:

```bash
PYTHONPATH=scripts python3 scripts/frontier_universal_gr_casimir_block_localization.py
```

Expected (matches cache):

```text
PASS=8 FAIL=0 TOTAL=8
```

All checks are class-(A) exact algebraic identities over
`K = Q[sqrt 2, sqrt 3, sqrt 6]` decided by `sp.simplify(...) == 0`. The
runner has no random sampling, no numeric tolerance, and no fitted
constants.

## Provenance and non-dependencies

The theorem closes from (BA-1)–(BA-5) plus the explicit construction of
`(B, Pi_lapse_trace, G_a, C, P_block)` in the runner. Universal-GR, ADM,
Hessian, spacetime-background, and Einstein/Regge interpretation is moved in
full to `UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_CONTEXT_NOTE_2026-07-11.md` and is
not a load-bearing dependency. The live dependency arrows of this note are
only to its exact runner and cached output.

## Forbidden-imports check

- No PDG observed values consumed.
- No literature numerical comparators consumed.
- No fitted selectors consumed.
- No admitted unit conventions are load-bearing on retention.
- No same-surface family arguments.
- No new axioms introduced — the theorem is on abstract `Sym^2(R^4)` with
  a generic spatial-block `SO(3)` action. The framework `MINIMAL_AXIOMS_2026-06-29`
  baseline is named in plain text only as the broader cluster context and
  is not load-bearing for the block-localization claim.
- Runner-facing block identifiers are coordinate mnemonics; their ADM names
  carry no theorem content.
- Runner imports: `sympy` only. No `numpy`, no I/O, no external data.

## What this theorem does NOT close

- No preferred basis is chosen inside the degenerate `j = 1` shift block
  or the `j = 2` shear block. These are irreducible `SO(3)`
  representations; no canonical internal frame exists without an external
  selector.
- No spacetime, Hessian, connection, Universal-GR, or Einstein/Regge
  identification is claimed; those interpretations are outside this theorem.
