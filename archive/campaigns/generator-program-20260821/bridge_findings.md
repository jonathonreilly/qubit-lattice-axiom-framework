# Bridge-transport ablation

All arithmetic below is exact SymPy arithmetic over \(\mathbb Q(i)\). The
inertia convention is \((n_+,n_-,n_0)\). Hermiticity means the exact identity
\(K=K^\dagger\), with no numerical tolerance.

The two supplied anchors are reproduced: b185 has inertia \((8,0,0)\) and all
eight leading principal minors are strictly positive; b186 has inertia
\((6,6,4)\).

## Hybrid table

Notation: `K` is the staggered \(d_K\) family with its seam-inclusive \(A\) and
real completion; `C` is chart \(d_{00}\) with its internal-half \(A'\) and
complex completion. `S` is the odd-step geometry and `L` is the landed-field
geometry with the explicit shear-flipped P4 image, the prescribed seam block
\(B\), and the one-step \(x\)-average. The reflection shown is used in both the
glue \(D=A_+-R A_+R\) and the transported Gram
\(K_{ab}=\overline{(G R)_{ba}}\).

| Differential | Geometry | Reflection | Span | Hermitian? | Exact inertia / defect |
|---|---|---|---|---|---|
| K | S | \(P_0\) | 2-slice | yes | **\((8,0,0)\)** (b185) |
| C | S | \(P_0\) | 2-slice | yes | \((0,0,8)\); Gram is exactly zero |
| K | L | \(P_0\) | 2-slice | no | —; \(\operatorname{rank}(K-K^\dagger)=8\) |
| K | S | \(P_x\) | 2-slice | no | —; \(\operatorname{rank}(K-K^\dagger)=8\) |
| K | S | \(P_0\) | full-half | yes | \((8,8,0)\) |
| K | S | \(P_x\) | full-half | no | —; \(\operatorname{rank}(K-K^\dagger)=16\) |
| K | L | \(P_0\) | full-half | no | —; \(\operatorname{rank}(K-K^\dagger)=16\) |
| K | L | \(P_x\) | 2-slice | yes | \((4,4,0)\) |
| K | L | \(P_x\) | full-half | yes | **\((8,8,0)\)** (reverse ablation) |
| C | S | \(P_0\) | full-half | yes | \((0,0,16)\); Gram is exactly zero |
| C | S | \(P_x\) | 2-slice | yes | \((0,0,8)\); Gram is exactly zero |
| C | S | \(P_x\) | full-half | yes | \((0,0,16)\); Gram is exactly zero |
| C | L | \(P_0\) | 2-slice | no | —; \(\operatorname{rank}(K-K^\dagger)=8\) |
| C | L | \(P_0\) | full-half | no | —; \(\operatorname{rank}(K-K^\dagger)=16\) |
| C | L | \(P_x\) | 2-slice | yes | \((4,4,0)\) |
| C | L | \(P_x\) | full-half | yes | **\((6,6,4)\)** (b186) |

The first five rows are b185 followed by its four one-group swaps. The ninth
row is the required reverse ablation: the b186 geometry, dressing, and
full-half span retained, with the staggered family substituted for chart
\(d_{00}\).

## Positivity-carrying ingredients

No pair search is needed: strict positivity is already destroyed by either of
two single swaps that remain Hermitian.

1. Swapping only the differential family, K \(\to\) C, annihilates the
   2-slice transported Gram exactly, changing \((8,0,0)\) to \((0,0,8)\).
   Thus the staggered seam-carrying differential is what supplies a nonzero
   positive bridge on this geometry.
2. Swapping only the span, 2-slice \(\to\) full-half, exposes an equally sized
   negative sector, changing \((8,0,0)\) to \((8,8,0)\). Thus the restricted
   two-slice carrier is independently essential for definiteness.

The geometry and reflection are a compatibility bundle rather than isolated
positivity mechanisms. Replacing only S by L with \(P_0\), or only \(P_0\) by
\(P_x\) with S, loses Hermiticity. Replacing both restores Hermiticity but is
already indefinite: K/L/\(P_x\)/2-slice has \((4,4,0)\). On the b186 side,
putting K back removes the four null directions but yields \((8,8,0)\), so the
staggered differential alone cannot rescue positivity on the landed/full-half
carrier.

## Method and adaptations

- The staggered edge orientation was fixed by the stated b185 certificate:
  forward matrix entries are \(+1/2\), with the forward \(t=3\) entry multiplied
  by \(-1\); the reconstructed baseline then has all eight exact positive
  leading minors.
- “Shear-flipped P4-image” must include an explicit \(s\mapsto-s\) before P4
  conjugation. P4 conjugation without that flip makes b186 non-Hermitian; the
  explicit flip reproduces \((6,6,4)\) exactly.
- The landed geometry uses \(B=I+(E_{02}+E_{20})/5\) at \(t=3,7\) and
  \((H+U_x^T H U_x)/2\). In the geometry-only ablation this prescribed seam
  modulus does not repair the \(P_0\) incompatibility. Removing it or changing
  its sign also leaves the 2-slice anti-Hermitian defect at rank 8.
- The chart/P0 and chart/Px glue variants requested in part (b) were both
  tested. On the odd-step geometry both are exactly Hermitian but give the zero
  Gram on either span; dressing is therefore not needed merely to make that
  particular hybrid Hermitian.
- Every displayed inertia was computed by exact Hermitian congruence: rational
  1-by-1 Schur pivots contribute according to their exact sign, and a zero
  diagonal with a nonzero off-diagonal uses a 2-by-2 Hermitian pivot of inertia
  \((1,1,0)\). The remaining zero block gives \(n_0\). No eigenvalue
  approximation or floating-point sign decision is used.

## Ten-line summary

1. Exact SymPy reconstructs b185 as Hermitian with inertia \((8,0,0)\).
2. Its eight leading principal minors are all exactly positive.
3. Exact SymPy reconstructs b186 as Hermitian with inertia \((6,6,4)\).
4. Chart \(d_{00}\) alone changes the b185 2-slice Gram to the exact zero matrix.
5. Full-half span alone changes b185 to the indefinite inertia \((8,8,0)\).
6. Landed geometry alone is non-Hermitian with defect rank 8 on the 2-slice.
7. \(P_x\) dressing alone is likewise non-Hermitian with defect rank 8.
8. Swapping landed geometry and \(P_x\) together restores Hermiticity but gives \((4,4,0)\).
9. The reverse staggered-on-b186 ablation has inertia \((8,8,0)\), not positivity.
10. Positivity is carried jointly by nonzero staggered bridge transport and the restricted 2-slice span.
