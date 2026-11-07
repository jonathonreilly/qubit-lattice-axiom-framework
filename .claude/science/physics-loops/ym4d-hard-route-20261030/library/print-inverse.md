lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:00Z

# PRINT-INVERSE: bounds and walk expansion of q_0 = (Q G_0 Q^*)^{-1}

Queue row 424. Commit 03ffc2764. Proved by Claude, not yet checked by the other model.
Work in progress; sections are written as they close.

Credit. The construction is Tadeusz Balaban's (CMP 96 Proposition 2.7 and §2; CMP 99b
§3, Theorems 3.2, 3.9, 3.10). The target statement, its consumers and the class S1-S2
are from the complete account of Ethan Sussman and Levent Alpoge (Claude and Codex as
authors of their text), commit 31a47c543775, CA-I 13144-13178. The prior-work digest is
`library/prior/print-inverse.md` (Codex). Duplicate check (FINISH rule 0a): `library/open-core.md`
and `library/l17c.md` have no match for PRINT-INVERSE, BP07, (3.132) or the remark label;
`library/open-registry.md:428` assigns PRINT-INVERSE to this row only.

## 1. The three damaged displays, read from the page images

Read from `~/ym4d-papers/balaban_cmp99_389.pdf`, rendered with PyMuPDF (journal page =
388 + PDF page). Quoted in the repository's notation; d is the dimension.

**(3.99)**, journal p. 413 (PDF page 25), Theorem 3.9, hypothesis (3.35), M large:
(Q'G'^2Q'^*)^{-1} = sum_omega R'_0(X_0) R'_{a_1}(X_1) ... R'_{a_n}(X_n)  (3.98), walks with
X_{i-1} ∩ X_i ≠ ∅; a term depends on U restricted to X~_0^5 ∪ ... ∪ X~_n^5, and

  |(R'_0(X_0) R'_{a_1}(X_1) ... R'_{a_n}(X_n))(y,y')|
     <= O(1) (L^j eta)^{-4} (L^{j'} eta)^{-d} O(M^{-1/2})^{|omega|} M^{-|omega|/2} e^{-(1/2) delta_0 d(omega,y,y')},
  y ∈ Λ_j, y' ∈ Λ_{j'}.

"The distance d(omega,y,y') is defined by (3.93), but the infimum is taken over y_i ∈ X_i ∩ B."

**(3.108)**, journal p. 416 (PDF page 28), Theorem 3.10 (hypothesis printed "(3.95)", read as (3.35)):
G = sum_omega R_0(X_0) R_{a_1}(X_1) ... R_{a_n}(X_n)  (3.107); a term depends on U restricted to
X~_0^5 ∪ ... ∪ X~_n^5 and

  |(R_0(X_0) ... R_{a_n}(X_n) J)(x)| <= O(1) (L^j eta)^2 O(M^{-1/2})^{|omega|} M^{-|omega|/2}
                                          e^{-(1/2) delta_0 d(omega,y,y')} |J|,
  x ∈ Δ(y), y ∈ Λ_j, supp J ⊂ Δ(y'),

"and the corresponding inequalities for norms on the left-hand sides of (3.42)-(3.47). The
constant O(1) depends on d and L only."

**(3.132)**, journal p. 422 (PDF page 34), after "let us write only bounds. We have":

  |(QGQ^*)^{-1}(y,y')| <= O(1) (L^j eta)^{-2} (L^{j'} eta)^{-d} e^{-delta_1 d(y,y')},  y ∈ Λ_j, y' ∈ Λ_{j'},

"and the same for the operator with G_1 instead of G." This agrees with the visual reading
in `library/b99.md:123-129` (there with d = 4). The model it is "analyzed in the same way
as" is Theorem 3.2, (3.48), journal p. 398:
|(Q'G'^2Q'^*)^{-1}(y,y')| <= B_0 (L^j eta)^{-4} (L^{j'} eta)^{-d} e^{-delta_0 d(y,y')}.

So the target bounds are (3.132) and the walk bound (3.99) with the scale factor
(L^j eta)^{-4} replaced by (L^j eta)^{-2}; that replacement is Balaban's own instruction
for the field Gram in CMP 96 (OCR 1198-1203: "we replace +4 and -4 in (2.83) by +2 and -2").

## 2. Route, and why it is not Balaban's letter-for-letter route

Balaban's Theorem 3.9 inverts the Gram matrix directly: local Gram inverses C_box on cubes,
the parametrix sum h C_box h, and then the walk expansion of the global propagator inside the
residual, with domain-change estimates for the terms without separation (CMP 99b pp. 411-413).
Done for QG_0Q^T, that route reads Balaban's walk expansion of G_0 (Theorem 3.10) and his
domain-change estimates. In our registry those are separate OPEN rows (B99b-T310, B99b-T33,
B99b-T34, B99b-C36; `library/open-registry.md:134-148`, owner none).

We use the same method (local inverses on cubes, a squared partition of unity, a Neumann
series expanded into words over walks of overlapping cubes) on a **local** operator whose
inverse contains q_0 as one block: the five-block mixed matrix of `library/flat-port.md`
(8.1) and §9.2, which is `library/b109.md` (66) in layered form. Every coefficient of that
matrix is a finite stencil or a finite averaging row; the projection R and the propagator
G_0 are not coefficients. So the parametrix residual is a sum of commutators only, and no
walk expansion of G_0, no domain-change estimate and no Theorem 3.10 is read. The walk
expansion of G_0 itself, in energy norms, comes out as another block of the same inverse.
The resulting expansion of q_0 has the structure of (3.98): words of local factors over
walks of overlapping cubes, each term reading U only on the hull of its walk.

What is reused, with its standing:
- `library/flat-port.md` §§8, 9.2, 11 (Codex): the flat (U = 1) inverse bounds of the four
  systems below on every separated layered geometry, uniform in depth, mesh, volume and
  shape. Checked line by line by Claude, first failing step none (`gates/flat-port-gate.md:8`).
- `library/b109.md` P15, P16 (Codex): the comparison of the actual complex rows and blocks
  with the flat ones in a supplied small gauge; P17: intrinsic local models with a graded
  collar; P18: the uniform-layer assembly. Not checked by the other model (t0-tree row
  B109-PART). This note re-derives the parts it uses in §§4-5 and states where it changes them.
- `library/b109.md` P1, P4 (Schur algebra, words): reproved below where used.

## 3. Setting, hypotheses and the theorem

### 3.1 Geometry

d = 4, G = SU(N), and L is the block factor of the account (odd, as the symmetric contours of
CMP 109 used by P15 require). Fine spacing eta = L^{-k}, l_j = L^j eta. The fine lattice is a
finite periodic box. A tower {Omega_j}_{0<=j<=k} is admissible as in CA-I 12695-12710
(CMP 102b (1)): Omega_j is a union of blocks of side M_b l_j of the level-j block grid (the
grids are nested), and

  (T)   l_j^{-1} dist(Omega_j^c, Omega_{j+1}) > R M_b,   R >= R_1.

Here M_b is the account's block size of the propagator papers (written \mathfrak M there;
Balaban's M in CMP 99b). The level of a site x in Omega_0 is lambda(x) = max{j : x in Omega_j};
layer j is Omega_j \ Omega_{j+1} = B^j(Lambda_j). Bond sets, layer bond sets, rows at seams and
the Dirichlet compression to Omega_0 follow the default convention of `library/flat-port.md`
§§2-3: the bond set of Omega_j is the set of bonds with an end point in Omega_j (CA-I 12707),
and layer bond sets are differences. A level-j field row c is a bond of the level-j coarse
lattice in Lambda_j; a level-j site row is a point of Lambda_j. The local scale m is l_j on
level-j objects (on a fine bond, the larger end-point scale, as in flat-port (8.3)).

Pairings (CA-I 12740-12745): eta^4 sum tr on fine objects, l_j^4 sum tr on level-j rows
(the "top" pairing); ^T is the bilinear transpose. Kernels of row operators are densities
for the top pairing: (T psi)(y) = sum_{y'} l_{j'}^4 T(y,y') psi(y').

**Distance.** d(y,y') is Balaban's (CMP 96 (2.46)): the infimum over admissible contours from
y to y' of sum_j l_j^{-1} |Gamma ∩ B^j(Lambda_j)|, where the part of Gamma in B^j(Lambda_j) uses
bonds of the level-j lattice. It satisfies the triangle inequality (CMP 96 (2.54)), and

  (SD)  d(y,y') >= R M_b (|j - j'| - 1)   for y in Lambda_j, y' in Lambda_{j'}, |j - j'| >= 1.

*Proof of (SD).* Let j' >= j + 2 (the case |j - j'| = 1 is trivial). For each n with
j < n < j', a contour from y (not in Omega_{j+1}, so not in Omega_n) to y' (in Omega_{j'}, so in
Omega_{n+1}) leaves Omega_n^c for the last time and then reaches Omega_{n+1}; that stretch lies
in Omega_n \ Omega_{n+1} = B^n(Lambda_n) and has length > R M_b l_n by (T). Its cost is > R M_b.
The j' - j - 1 stretches are disjoint. ∎

### 3.2 Regularity hypotheses

(S1) and (S2) are those of CA-I 12943-12968: U = e^{i eta a} U_r, U_r G-valued; for every j and
every cube of Balaban's class C_j (CMP 99b p. 396: side 12 M_b l_j, a union of level-j blocks,
contained in B^j(Lambda_j) ∪ B^{j+1}(Lambda_{j+1}), meeting B^j(Lambda_j)) there is a G-valued gauge
u on the cube with U_r^u = e^{i eta A}, l_j|A| < a_0 and l_j^2|∇A| < a_0 there; and
N_{U_r}(a) < a_1, that is |a| < a_1 l_n^{-1} and |∇_{U_r} a| < a_1 l_n^{-2} on bonds of layer n.

The proof uses (S1) through the following local form. Let r_N > 0 be the radius fixed in §3.5.

**(S1-loc)** For every site x of Omega_0, with j = lambda(x) and N(x) the l^∞ box of half-width
r_N l_j about x, there is a G-valued gauge u on the bonds of N(x) such that U_r^u = e^{i eta A}
with l_{lambda(z)}|A| <= L^2 a_0 and l_{lambda(z)}^2 |∇A| <= L^2 a_0 at every point z of N(x).
(The local models of §4 read U only inside such boxes: r_N is chosen so.)

**Proposition 3.1 ((S1) gives (S1-loc) on thick towers).** Suppose 2 r_N L + 1 <= 11 M_b,
R_1 >= 12 sqrt(d), R_1 M_b > 2 sqrt(d) L r_N, and (Thick): each Omega_i is a union of cells of a
grid of spacing s_i, aligned with the level-i block grid, with s_i a multiple of M_b l_i and
s_i >= 12 M_b l_i. Then (S1) implies (S1-loc) at every x with N(x) ⊂ Omega_0 (so at every x
when Omega_0 is the whole periodic box).

*Proof.* Fix x, j = lambda(x), N = N(x). Distances are Euclidean; diam N = 2 sqrt(d) r_N l_j.
(1) The levels met by N lie in {i, i+1} for some i in {j-1, j}. A site of level <= j - 2 lies
outside Omega_{j-1}, and x lies in Omega_j, so by (T) they are more than R M_b l_{j-1} =
R M_b l_j / L > sqrt(d) r_N l_j apart. A site of level >= j + 2 lies in Omega_{j+2}, and x lies
outside Omega_{j+1}, so they are more than R M_b l_{j+1} apart. Sites of levels j - 1 and j + 1
are more than R M_b l_j > diam N apart. Let i be the least level met by N.
(2) Every site of N has level >= i, so N ⊂ Omega_i. The side of N is 2 r_N l_j <= 2 r_N L l_i
< s_i, so the grid cells meeting N form a product of at most two cells in each direction, and
each of them lies in Omega_i. Their union is a box of side s_i or 2 s_i in each direction that
contains N. In each coordinate take an interval of length 12 M_b l_i aligned with the level-i
block grid that contains the projection [beta, beta + w) of N, where w <= 2 r_N L l_i <= 11 M_b l_i
- l_i: round beta down to the grid (this adds less than M_b l_i); if the interval then passes the
right end of the cell box, take instead the aligned interval of length 12 M_b l_i that ends
there (its left end is >= the left end of the cell box, since the cell box has length >= 12 M_b
l_i, and it is <= beta). The product is a cube Q of side 12 M_b l_i, a union of level-i blocks,
with N ⊂ Q ⊂ Omega_i.
(3) Q contains a site of level i, which is outside Omega_{i+1} and so at distance > R M_b l_{i+1}
>= 12 sqrt(d) M_b l_i from Omega_{i+2} (as R >= 12 sqrt(d)); hence Q avoids Omega_{i+2}. So
Q ⊂ Omega_i \ Omega_{i+2} = B^i(Lambda_i) ∪ B^{i+1}(Lambda_{i+1}) and Q meets B^i(Lambda_i): Q is in C_i.
(4) (S1) gives u on Q with l_i|A| < a_0 and l_i^2|∇A| < a_0. At z in N, lambda(z) <= i + 1, so
l_{lambda(z)} <= L l_i. ∎

*Remark (the printed class does not reach thin layers).* Without (Thick), a layer may contain a
finger one block of side M_b l_j wide and many blocks long, far from Omega_{j+1}. No cube of C_j
fits in it, and for L >= 25 no cube of C_{j-1} (side 12 M_b l_{j-1}) reaches a site on its axis.
Then (S1) puts no condition on U_r near that axis, and the averaging rows of level j there are
unconstrained. The theorem below assumes (S1-loc); for the account's towers this holds when
they are thick (for instance unions of cubes of side M_1 l_j with M_1 = R'_* M_b >= 12 M_b,
CA-I 12672-12680, if R_1 >= 12), and at the boundary of a proper Omega_0 when (S1) is read on
the plaquettes the Dirichlet compression reads. This is a hypothesis gap in the remark as
printed, not a counterexample; we do not claim the bounds fail on thin towers.
