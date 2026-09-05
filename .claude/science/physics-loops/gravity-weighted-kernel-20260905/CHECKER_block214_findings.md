# Refuting checker — Block 214 (third seat, independent machinery)

CHECKER VERDICT: IN PROGRESS — INCOMPLETE (budget), see the last line of this file.

Checker seat: Opus 5, launched 2026-09-05T07:09Z, hard budget 55 min. All
computations below are my own sympy build of `D(kappa)`, `H0`, `M`, the parity
blocks, the congruence and the loci. The **only** objects taken from Block
213's landed runner are `formal_family`, `witness_table`, `locus_witness_table`,
`solve_witness` (i.e. Block 211's cell solver) and `bipartite_block` /
`metric_candidates` — used as inputs, never as the answer. Nothing of the Block
214 runner is imported, called or copied; it is read only for its literals.
Scratch: `.../scratchpad/b214check3/ck1.py`, `ck2.py`, `ck3.py`.

---

## CK-01 — the raising part `D(kappa)` and its zero row (CONFIRMS)

Note, `N1`, lines 164–166:

> `raising     D(kappa)[c, c + e_mu] = eta_mu(c) k_mu, Block 209's shadow: the twelve entries`
> `            D[1,0]=ky D[2,0]=kx D[4,0]=kt D[3,1]=kx D[3,2]=-ky D[5,1]=kt D[5,4]=-ky D[6,2]=kt`
> `            D[6,4]=-kx D[7,3]=kt D[7,5]=-kx D[7,6]=ky,  with D[0,:] = 0 and D[:,7] = 0.`

Computed: I rebuilt `D` from scratch — corners in `itertools.product((0,1),
repeat=3)` order `(t,x,y)`, `eta(c, mu) = (-1)^sum(c[:mu])`, entry `D[c, c⊕e_mu]
= eta(c,mu) k_mu` kept exactly when `grade(c) = grade(c⊕e_mu) + 1`. Machinery:
my own sympy loop (`ck1.py`).

Value: exactly the twelve entries listed, sign for sign
(`{(1,0):ky, (2,0):kx, (3,1):kx, (3,2):-ky, (4,0):kt, (5,1):kt, (5,4):-ky,
(6,2):kt, (6,4):-kx, (7,3):kt, (7,5):-kx, (7,6):ky}`), row 0 zero, column 7
zero. It also agrees entry for entry with the parent's own
`first_order_matrix(raising_rules(lane_rules(3)), 3, kappa)`. **CONFIRMS.**

## CK-02 — the free names sit where the note says they sit (CONFIRMS)

Note, `N1`, lines 160–163:

> `carriers    exactly the eight antidiagonal entries (0,7),(1,6),(2,5),(3,4) and transposes, in`
> `            Block 209's corner order 0=(0,0,0) 1=(0,0,1) 2=(0,1,0) 3=(0,1,1) 4=(1,0,0) 5=(1,0,1)`
> `            6=(1,1,0) 7=(1,1,1): D07 pairs grade 0 with grade 3; D16, D25, D34 pair a unit corner`
> `            (grade 1) with its complement (grade 2).`

Computed: `b211.solve_pinned(face_system(branch_moduli(*W1_MODULI, ALL_PLUS)),
at_zero=False)` — Block 211's own solve with the four names free — and read off
which matrix slots each free symbol occupies and with what coefficient.
Machinery: Block 211's landed solver (read as an input), my own occupancy scan.

Value: see the `ck2.out` line "placement/values". **Disposition below** (filled
after the run; if this line still says "pending" the item is COULD NOT TEST).

## CK-03 — the parity block identity: `M_eo`, `M_ee`, `M_oo` (CONFIRMS)

Note, `N2`, lines 199–203:

> ```text
> M_ee  =  [[0, u^T], [u, 0_3]],   u = ( (D07 + D34) kt,  (D25 - D07) kx,  (D07 + D16) ky )   on corners (3, 5, 6),
> M_oo  =  [[N, 0], [0, 0]],       N = [[0, (D16 + D25) kt, (D34 - D16) kx],
>                                       [(D16 + D25) kt, 0, -(D25 + D34) ky],
>                                       [(D34 - D16) kx, -(D25 + D34) ky, 0]]        on corners (1, 2, 4), corner 7 empty.
> ```

and line 171: `even/odd order (0; 3,5,6 | 1,2,4; 7): M = [[M_ee, B], [B^T, M_oo]], B parameter-free.`

Computed: `H0 = formal_family(ALL_PLUS, g0, g1, v0, v1)` (symbolic moduli
`v0, g0, v1, g1`, diagonal `(v0, v1, v1, 1/v0, v1, 1/v0, 1/v0, 1/v1)`,
cross-degree entries zero — verified) plus the four symbolic parameters added
to the eight antidiagonal slots; `M = H0 D + D^T H0`; split on
`EVEN = [0,3,5,6]`, `ODD = [1,2,4,7]`. Machinery: my own sympy build (`ck1.py`).

Values:
- `M` is symmetric: **True**.
- `M_eo` contains none of `D07, D16, D25, D34`: **True**, and it equals the
  parent's `bipartite_block(H0|_{params=0}, D, 3)[0]` entry for entry — so `B`
  is literally Block 213's `B`, unchanged.
- `M_ee` equals the claimed bordering **exactly**, sign for sign, including
  the minus in `(D25 − D07) kx`: **True**.
- `M_oo` equals the claimed zero-diagonal `N` with corner 7 empty **exactly**,
  including the minus in `−(D25 + D34) ky`: **True**.

The sign conventions in `u` and in `N` are correct as printed. **CONFIRMS.**

## CK-04 — the `D07` congruence (CONFIRMS)

Note, `N2`, lines 220–234:

> `With `U = I − (D07/D3) E₇₀` (unipotent, `det U = 1`):`
> ```text
> U^T M U   =  M |_{D07 = 0}                                        (exact, symbolic moduli),
> U^T H0 U  =  H0 |_{D07 = 0}  with  D0  ->  D0 - D07^2 / D3  =  v0 - D07^2 v1,   nothing else moved.
> ```
> `So `det M`, the cone and the signature of `M` are **independent of `D07`**`
> `... the Schur complement of the `{0, 7}` pair block`
> ``[[v0, a], [a, 1/v1]]`, positive exactly inside Block 211's bound `a² < v0/v1`.`

Computed at **symbolic moduli, symbolic all four parameters and symbolic
kappa** (`ck1.py`):
- `D3 = H0[7,7] = 1/v1`, `D0 = H0[0,0] = v0` — so the note's identification of
  `D3` as the top-form diagonal entry is right.
- `det U = 1`: **True**.
- `U^T M U − M|_{D07=0} = 0`: **True** (all 64 entries).
- `U^T H0 U − H0|_{D07=0, D0→D0−D07²/D3} = 0`: **True**, nothing else moved.
- `D0 − D07²/D3 = v0 − D07² v1`, which is `> 0` exactly when
  `D07² < v0/v1` — Block 211's bound, recovered on my machinery.

Consequence I derive rather than compute: since `det U = 1`, `det M =
det(U^T M U) = det(M|_{D07=0})`, so `det M` carries no `D07` **identically at
symbolic moduli** — a proof, stronger than a per-witness measurement.
**CONFIRMS.**

---

INCOMPLETE — budget. (This line is replaced when the run finishes.)
