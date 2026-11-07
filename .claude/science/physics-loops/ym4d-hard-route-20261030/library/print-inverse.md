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
### 3.3 Operators

At a G^c-valued configuration U on the bonds read: D_U is the covariant site difference and
D_U^T its bilinear transpose (CMP 99b (3.3), (3.8)); Delta(U) is the operator of the second
variation of the Wilson action, CMP 99b (3.10), with its curvature part Delta' (so Delta(1) is
the compressed curl form); Q(U) is the field-row map, the linear part of Balaban's averaging
(CMP 99b (3.14)-(3.16), CMP 98 (89)-(92), (124)) with the symmetric contours of CMP 109, the
same map as in `library/b109.md` P15; Q'(U) is the site-row map (CMP 99b (3.18)-(3.19)). All act
on the Dirichlet spaces of Omega_0 (flat-port §8). Put a := l^{-2} on field rows, K := m Q
(dimensionless rows, counting pairing), so that K^T = Q^T m^{-3}, and

  A_s := D_U^T D_U + Q'^T m^{-2} Q',     B_v := Delta(U) + D_U D_U^T + Q^T a Q.

On X = (A, h, lambda, mu, nu) (fine bond field, two fine site fields, site-row multiplier with
top pairing, field-row multiplier with counting pairing) let

           | B_v      -D_U    0      0      -K^T |
           | -D_U^T    I      A_s    0       0   |
  M_5(U) = | 0         A_s    0     -Q'^T    0   |       (flat-port (8.1) and §9.2; b109 (66))
           | 0         0     -Q'     0       0   |
           | -K        0      0      0       0   |

M_4 := rows and columns 1-4 (flat-port (8.1)), M_3 := rows and columns 2-4 (the scalar saddle
system), M_1 := A_s. The account's objects (CA-I 13583-13595, 13552-13571), at complex U by
analytic continuation from the real ones: G' = (Delta_U + Q'^T alpha Q')^{-1} for a positive scalar
mass alpha, R := I - G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G', Delta_a := Delta + D_U R D_U^T + Q^T a Q,
G_0 := Delta_a^{-1}, q_0 := (Q G_0 Q^T)^{-1}. At real U, R is the orthogonal projection onto
Delta_U N(Q') (CMP 99b (3.21), (3.25)); it does not depend on alpha, because for lambda in N(Q')
one has (Delta_U + Q'^T alpha Q') lambda = Delta_U lambda. By analytic continuation the same holds at
complex U. We use alpha = m^{-2}, so G' = A_s^{-1}.

### 3.4 Norms

flat-port (8.3) with the row multiplier of §9.2, with differences covariant at the real part U_r
and zero extension at the Dirichlet boundary, physical L^2 norms (weight eta^4):

  ||X||_X^2 = ||∇A||^2 + ||m^{-1}A||^2 + ||h||^2 + ||m^{-2}lambda||^2 + ||m^{-1}D lambda||^2
              + sum_{alpha,beta} ||D_alpha D_beta lambda||^2 + ||m^2 mu||_top^2 + ||nu||_count^2.

X^* is the dual norm for the bilinear pairing. The norms of M_r are the restrictions to the
variables of M_r. On a local model (§4) the same formula on its geometry defines X_tau. Every
term is a sum of local terms, so on fields supported where a model and the actual geometry
agree, the two norms coincide. Since ||nu||_count is a component, for every operator W one has

  (E)  |W_{nu nu}(c,c')| <= ||W||_{X^* -> X}     (c, c' field rows; norm on the colour block),

because the unit source at c' in the nu slot has dual norm <= 1 and the nu component at c of
an element of X is bounded by its X norm.

### 3.5 Constants and their order

All depend only on N and L (d = 4), and are chosen in this order.
1. From the flat package [F] (§4.1): its tile size M_F and separation rho_F (multiples of
   powers of L), the bound B_F >= 1, the commutator constant C_{8.8} of flat-port (8.8), and the
   cutoff constant c_h (multiplication by a cutoff obeying flat-port (8.6) is bounded by c_h on
   X and on X^*). Put rho'_F := M_F ceil(rho_F / M_F).
2. From the comparison [C] (§4.2): e_C > 0, C_C, and the constant C_S of (4.4). Put
   C_K := 3 C_{8.8} (Lemma 5.1) and the overlap number D_* := 2 (16 L)^d (§4.3).
3. The tile size M_t, a power of L, a multiple of L M_F, with M_t >= max{2 rho'_F, c_r L, C_d}
   (c_r the read enlargement of a row in P15, C_d the seam-rounding constant of §4.3) and
   theta := 3 B_F c_h^2 C_K / M_t <= 1/(16 D_*^2). Every larger power of L is also allowed.
4. r_N := 7 M_t, and D_X := 16 d L M_t (a bound for Balaban-diameters of model read sets, §4.3).
5. delta_q := log(1/theta) / (7 D_X) > 0.
6. Floors: M_b a multiple of M_t with 2 r_N L + 1 <= 11 M_b; R_1 >= 12 sqrt(d) with
   R_1 M_b >= max{rho'_F, 2 sqrt(d) L r_N + 1, 3 log L / delta_q}.
7. e_L := min{e_C, 1/(8 B_F C_C), C_{8.8} / (2 c_h C_C M_t)}, and radii a_0^*, a_1^* with
   C_S (L^2 a_0^* + a_1^*) <= e_L. (The radii shrink like 1/M_t. With M_t fixed by L they are
   still constants depending on N and L. A sharper commutator estimate, sketched after
   Lemma 5.1 and not proved here, would remove the factor 1/M_t.)
8. C_q := 4 D_* B_F c_h^2 L theta^{-1/2}.

Nothing here depends on k, eta, the volume, the tower, or U. The account's floors on M_b and
R_1 M_b ("sufficiently large", CA-I 12665-12672, 13414-13428) are lower bounds of the same kind,
so they can be taken together with item 6. The rate delta_q differs from Balaban's delta_0; see §8.

### 3.6 The theorem

**Theorem PI.** Fix the constants of §3.5. For every k >= 0, every finite periodic fine box of
physical side at least 2 r_N L + 2 (so that no box N(x) wraps), every admissible tower with
R >= R_1, and every U = e^{i eta a} U_r satisfying (S1-loc) with
a_0 <= a_0^* and (S2) with a_1 <= a_1^*:

(a) *Existence.* M_1 = A_s, M_3, M_4 and M_5 are invertible. Hence Q'G'^2Q'^T, R, Delta_a, G_0
and q_0 exist. Each is holomorphic in a on {N_{U_r}(a) < a_1^*}, is Balaban's operator at real
points (a G-valued), and q_0^T = q_0. Moreover q_0 = -m^{-3} [M_5^{-1}]_{nu nu} m.

(b) *(3.132).* For field rows y in Lambda_j and y' in Lambda_{j'},

  |q_0(y,y')| <= C_q l_j^{-2} l_{j'}^{-4} e^{-delta_q d(y,y')}.

(c) *Walk expansion.* q_0 = sum_omega q_omega over walks omega = (tau_0, ..., tau_n), n >= 0, of
tiles (§5.1) with X_{tau_{m-1}} ∩ X_{tau_m} nonempty, absolutely convergent at each (y, y'). Each
q_omega is a holomorphic function of a that depends on U only through its restriction to the hull
X(omega) := X_{tau_0} ∪ ... ∪ X_{tau_n}; two settings whose towers agree on N_{tau_0} ∪ ... ∪
N_{tau_n} and whose configurations agree on X(omega) give the same q_omega. With |omega| := n,

  |q_omega(y,y')| <= C_q l_j^{-2} l_{j'}^{-4} theta^{|omega|/2} e^{-3 delta_q D_X (|omega|+1)},

q_omega(y,y') = 0 unless y lies in X_{tau_0} and y' in X_{tau_n}, and then
d(omega,y,y') <= D_X (|omega|+1) for Balaban's walk distance (3.93) with intermediate points in
the sets X_{tau_m}. For every tile tau the walks starting at tau satisfy
sum theta^{|omega|/2} <= 2, and so do the walks ending at tau.

(d) *Type (3.99).* theta = C_theta / M_t with C_theta := 3 B_F c_h^2 C_K. So theta^{|omega|/2}
splits as (theta^{1/4})^{|omega|} (walk summation) times (theta^{1/4})^{|omega|} (spare), and
e^{-3 delta_q D_X(|omega|+1)} <= e^{-delta_q d(omega,y,y')} e^{-2 delta_q Lambda} for every length
Lambda <= D_X(|omega|+1): one exponential for decay and two spare ones. The tile size M_t may be
any allowed power of L. With M_t of order M_b the per-step factor is O(M_b^{-1}), the order of
Balaban's O(M^{-1/2})^{|omega|} M^{-|omega|/2} in (3.99), with (L^j eta)^{-4} replaced by (L^j eta)^{-2};
but then, by item 7 of §3.5, the radii shrink like 1/M_b, and delta_q is of order log M_b / M_b.
The default is M_t fixed by L, with theta a fixed number <= 1/(16 D_*^2).

Part (a) uses no walk bound. Part (b) follows from (c) by summation (§7).

## 4. Inputs and local models

### 4.1 The flat input [F] (`library/flat-port.md`, checked)

Call a geometry G' *admitted* if it is a nested sequence Omega'_0 ⊃ Omega'_1 ⊃ ... ⊃ Omega'_k of
site sets of the fine box (some possibly empty), Omega'_n a union of blocks of side M_F l_n of the
level-n grid, with l_n^{-1} dist(Omega'_n^c, Omega'_{n+1}) >= rho_F, the default conventions of §3.1,
and Dirichlet conditions outside Omega'_0. Here M_F, rho_F are the tile size and separation of
flat-port §8.2 (functions of L; "Take the separation larger than a fixed L-dependent multiple
of M", flat-port.md:550).

**[F].** There is B_F >= 1, depending on L, such that on every admitted geometry the flat systems
M_r(1), r in {1, 3, 4, 5}, are invertible with ||M_r(1)^{-1}||_{X^* -> X} <= B_F.

Source: flat-port (8.10) (flat-port.md:586) for M_4; "the same construction, omitting the first row
and column of (8.1), applies to the scalar saddle system" and "applying the construction directly
to A_s" (flat-port.md:588) for M_3 and M_1; §9.2, "the entire construction (8.7)-(8.10) applies to
this enlarged system" (flat-port.md:666), for M_5; uniformity in depth, mesh, volume and shape of
the layers, flat-port §12 (flat-port.md:816-818). At U = 1 the compressed Wilson Hessian is the compressed curl
form, so M_r(1) is literally the flat-port matrix. Standing: checked by Claude, first failing
step none, repairs W1-W3 not affecting these statements (`gates/flat-port-gate.md:8`).

### 4.2 The complex comparison [C] (`library/b109.md` P15-P17, unchecked; re-derived here)

For an admitted geometry with local scale m (note m <= l_k = 1) and a g^c-valued bond field B on
its read set, put e(B) := max (m|B| + m^2 |∂B|), with ∂ the flat first differences.

**Lemma 4.1 [C].** There are e_C > 0 and C_C, depending on N and L, such that if e(B) <= e_C then
(i) every coefficient of M_r(e^{i eta B}), r in {1,3,4,5}, is defined and holomorphic in B;
(ii) ||M_r(e^{i eta B}) - M_r(1)||_{X^0 -> X^0*} <= C_C e(B), where X^0 is the flat norm of §3.4;
(iii) if B is real, the norm with differences covariant at e^{i eta B} lies between
(1 + C_C e(B))^{-1} and (1 + C_C e(B)) times the flat norm.

*Proof.* Each estimate is local. A field row or site row of level n reads a fixed enlargement
c_r l_n of its double block (P15, last paragraph), where m >= l_n / L. Rescaling that box by l_n
turns it into P15's unit-scale setting with potential l_n B, of size <= L e(B). P15 (71) then
gives, for the physical rows, row sums <= C e(B) and column sums <= C e(B) (eta / l_n)^4 for
Q(U) - Q(1) and Q'(U) - Q'(1); P15's proof is a contraction for the straightened recursion with
the geometric bootstrap |b_m| <= 2 e s_m and the telescoping (79), so the constant does not grow
with the number of levels; I read it as an input here and found no failing step. Weighted
Cauchy-Schwarz (P17 (92)-(94)) converts these sums into
||(K(U) - K(1)) v||_count <= C e(B) ||m^{-1} v||_2 and
||m^{-2} (Q'(U) - Q'(1)) lambda||_top <= C e(B) ||m^{-2} lambda||_2; the column factor (eta / l_n)^4
cancels the fine measure. The two mass terms follow by writing X^T a X - X_1^T a X_1 =
(X - X_1)^T a X + X_1^T a (X - X_1) and using ||m^{-1} Q v||_top <= C ||m^{-1} v||_2.
For the differences, D_U - D_1 is a shift followed by multiplication by
c_mu = eta^{-1}(Ad e^{i eta B_mu} - I), with |c_mu| <= C|B| <= C e/m and |∂ c_mu| <= C e/m^2 (P16,
exponential series; a difference of B^q telescopes). The product rule then gives
||(D_U^T D_U - D_1^T D_1) lambda||_2 <= C e (||m^{-2}lambda|| + ||m^{-1} D lambda||) and
|<v, (D_U D_U^T - D_1 D_1^T) w>| <= C e ||v||_E ||w||_E (P16 (84)-(85) with the weights m).
For the Wilson Hessian, P16 (86)-(88): per plaquette the form is the square of the transported
curl plus a remainder bounded by C |P - I| eta^4 |v| |w|, with |P - I| <= C eta^2 e / m^2; the
transported curl differs from the flat one by a multiplication of size C e / m. Summing over
plaquettes with bounded incidence gives |<v, (Delta(U) - Delta(1)) w>| <= C e ||v||_E ||w||_E,
curvature term included. At the bare level-0 band the rows are identities and do not vary; at
the Dirichlet edge zero extensions are used, as in P17. Adding the finitely many blocks gives
(ii). Part (iii) is the same multiplication estimate for covariant minus flat differences.
Part (i): the coefficients are finitely many convergent analytic formulas of the bond values. ∎

### 4.3 Tiles, cutoffs and local models

**Tiles.** For each level j, tile the layer Omega_j \ Omega_{j+1} by cubes of side M_t l_j of the
level-j grid; this is possible because Omega_j and Omega_{j+1} are unions of blocks of sides M_b l_j
and M_b l_{j+1}, and M_t divides M_b. If Omega_0 is not the whole box, add level-0 tiles covering
the initial points of the bonds of Omega_0 outside it (flat-port.md:543, "include a bare tiling
outside Omega_0"). A tile tau has level j_tau
and centre site x_tau (M_t L^j is odd). Its bump b_tau is a sampled smooth function equal to 1 on
tau, supported in the concentric cube of side 2 M_t l_{j_tau}, with |∂b| <= C/(M_t l_{j_tau}) and
|∂^2 b| <= C/(M_t l_{j_tau})^2; h_tau := b_tau / (sum_sigma b_sigma^2)^{1/2}. A bond component uses the
value at its initial point, a row component the value at its reference point. Then
sum_tau h_tau^2 = 1 on every component, the denominator is >= 1, and the h_tau obey flat-port (8.6)
with M = M_t (adjacent levels differ by the factor L, absorbed in C).

**Models.** Let N_tau := N(x_tau), the box of half-width r_N l_{j_tau} = 7 M_t l_{j_tau}. By step (1)
of Proposition 3.1 (which uses only (T) and R_1 M_b > 2 sqrt(d) L r_N), the levels met by N_tau
lie in {i, i+1} with i = i_tau the least one, and j_tau is i or i+1. Let C_tau be the smallest cube
aligned with the grid of spacing M_F l_{i+1} that contains the box of half-width 4 M_t l_{j_tau}
about x_tau; rounding adds at most M_F l_{i+1} <= M_t l_{j_tau}. Put K_n := C_tau for n >= i+1 and,
for n <= i, K_n := C_tau enlarged on each side by sum_{p=n}^{i} rho'_F l_p. Each K_n is aligned with
the level-n grid of spacing M_F l_n, and the total enlargement is at most
rho'_F l_i L/(L-1) <= 2 rho'_F l_{j_tau} <= M_t l_{j_tau}. The model geometry G_tau is

  Omega^tau_n := Omega_n ∩ K_n  (0 <= n <= k),   Dirichlet conditions outside Omega^tau_0.

It is admitted: the sets are nested and are unions of level-n blocks of side M_F l_n (M_F divides
M_b); and dist((Omega^tau_n)^c, Omega^tau_{n+1}) >= min{dist(Omega_n^c, Omega_{n+1}), dist(K_n^c, K_{n+1})},
which is >= min{R M_b, rho'_F} l_n >= rho_F l_n for n <= i, while Omega^tau_n is empty for n >= i+2.
Its outer layer is at level 0 (a point of K_0 \ K_1 has model level 0). The systems M_{r,tau}(U)
are those of §3.3 built on G_tau; their read set X_tau is the set of bonds and plaquettes their
coefficients read. Since K_0 lies in the box of half-width 6 M_t l_{j_tau} and a row of level
<= i+1 reads at most c_r L l_{j_tau} <= M_t l_{j_tau} beyond its double block, X_tau ⊂ N_tau.

*Agreement.* On C_tau the model level of every site equals its actual level (a site of C_tau lies
in every K_n). Hence every coefficient of M_{r,tau} and of M_r whose stencil or row read set lies
in the box A_tau of half-width 3 M_t l_{j_tau} about x_tau is the same function of U. The support of
h_tau, together with every stencil and row read set meeting it, lies in A_tau.

*Diameter.* Any two points of X_tau are joined by an admissible contour of cost at most
D_X = 16 d L M_t: take a coordinate staircase inside N_tau; its Euclidean length is at most
14 d M_t l_{j_tau} <= 14 d L M_t l_i, which costs at most 14 d L M_t at scale l_i; each segment
crosses the boundary of the level-(i+1) region, a union of aligned cubes of side M_b l_{i+1}, at
most 2(14 M_t / M_b + 1) <= 10 times, and each crossing costs at most a fixed C_d to reach the
coarse lattice; M_t >= C_d gives the bound. *Overlap.* If N_sigma meets N_tau then
|j_sigma - j_tau| <= 1 (two levels differing by 2 would lie within the gap), so the number of tiles
sigma with X_sigma ∩ X_tau nonempty is at most D_* := 2 (16 L)^d, independent of M_t.

**Lemma 4.2 (local inverses).** Assume (S1-loc) with a_0 <= a_0^* and (S2) with a_1 <= a_1^*. For
every tile tau and r in {1, 3, 4, 5}, M_{r,tau}(U) is invertible and

  ||M_{r,tau}(U)^{-1}||_{X_tau^* -> X_tau} <= 3 B_F.

Its entries are holomorphic functions of a and depend only on U restricted to X_tau and on the
tower inside N_tau (not on a gauge, the box, or anything outside N_tau).

*Proof.* (S1-loc) at x_tau gives a G-valued u on the bonds of N_tau ⊃ X_tau with U_r^u = e^{i eta A}
and l_{lambda(z)}|A| <= L^2 a_0, l_{lambda(z)}^2 |∇A| <= L^2 a_0. The model scale m never exceeds the
actual scale l_{lambda(z)} (they agree on C_tau; on the collar the model level is lower). The twist
transforms as a^u(b) = Ad u(b_-) a(b), and (S2) gives m|a^u| < a_1 and m^2 |∇_{e^{i eta A}} a^u|
= m^2 |(∇_{U_r} a)^u| < a_1. Let B := (i eta)^{-1} log(e^{i eta a^u} e^{i eta A}) bondwise. P16 (81),
read with the weight m on differences (the algebra norm |V| + m|∂V| is submultiplicative by the
product rule with one shifted factor, and covariant minus flat differences of a^u are bounded by
C |A| |a^u|), gives

  (4.4)   e(B) <= C_S (L^2 a_0 + a_1) <= e_L.

Let 𝒰 act by Ad u on every component at its reference point. The covariance identities
CMP 99b (3.31)-(3.34) for D_U, Delta(U), Q(U), Q'(U) are identities between finite formulas and
hold at complex U (for the rows by the exact covariance of the straightened construction, P15
(74)); so M_{r,tau}(U^u) = 𝒰 M_{r,tau}(U) 𝒰^{-1}, and 𝒰 maps the norm covariant at U_r onto the
norm covariant at e^{i eta A}. By [F], ||M_{r,tau}(1)^{-1}||_{X^0} <= B_F. By Lemma 4.1 (ii),
||M_{r,tau}(e^{i eta B}) - M_{r,tau}(1)|| <= C_C e_L <= 1/(8 B_F); the identity
M(U)^{-1} = [I + M(1)^{-1}(M(U) - M(1))]^{-1} M(1)^{-1} (b109 (69)) and its geometric series give
invertibility with flat norm bound (8/7) B_F. By Lemma 4.1 (iii) with C_C e_L <= 1/8 the
covariant norms are within the factor 9/8 of the flat ones, so the bound in X_tau is at most
(9/8)^2 (8/7) B_F < 3 B_F. Conjugating back by 𝒰 changes nothing. The entries of M_{r,tau}(U) are
holomorphic in a (Lemma 4.1 (i)); the determinant does not vanish; Cramer's rule gives
holomorphic entries of the inverse. The gauge was used only for the bound. ∎

## 5. Assembly and patch words

Throughout this section U is as in Lemma 4.2, and r in {1, 3, 4, 5} is fixed; we drop r. A field
supported in A_tau is identified with a model field and back ("transplant"); by the agreement
property both norms coincide there.

**Lemma 5.1 (commutators).** For every tile tau and every Y in the model space,
[M_tau(U), h_tau] Y is supported in A_tau and depends only on Y on the read closure of
supp h_tau; it equals [M(U), h_tau] Y~ for every global field Y~ that agrees with Y on A_tau; and

  ||[M_tau(U), h_tau] Y||_{X_tau^*} <= (C_K / M_t) ||Y||_{X_tau},   C_K = 3 C_{8.8}.

*Proof.* [M_tau, h_tau] Y = M_tau(h_tau Y) - h_tau M_tau Y reads Y only near supp h_tau, and its
output lies in the read closure of supp h_tau; the rest is the agreement property (§4.3). For the bound, conjugate by
𝒰 as in Lemma 4.2; h_tau is scalar and evaluated at the same reference points, so it commutes
with 𝒰. Then [M_tau(U^u), h] = [M_tau(1), h] + [V, h] with V := M_tau(e^{i eta B}) - M_tau(1).
flat-port (8.8) (flat-port.md:571; h obeys (8.6) with M = M_t) gives
||[M_tau(1), h] Y||_{X^0*} <= (C_{8.8}/M_t) ||Y||_{X^0}. By Lemma 4.1 (ii),
||[V, h] Y|| <= ||V (h Y)|| + ||h V Y|| <= 2 c_h C_C e(B) ||Y|| <= 2 c_h C_C e_L ||Y|| <=
(C_{8.8}/M_t) ||Y||, by the choice of e_L. Passing between flat and covariant norms costs at most
(9/8)^2 (Lemma 4.2). So the constant is at most (81/64) 2 C_{8.8} < 3 C_{8.8}. ∎

*Remark (a sharper commutator; not proved here, not used).* Every block of V has range at most
c_r L m. The commutator replaces a zeroth-order coefficient V(x,x') by V(x,x')(h(x') - h(x)),
with |h(x') - h(x)| <= C c_r L / M_t, and in a difference block it moves one difference onto h,
with |∂h| <= C/(M_t m). Repeating the proof of Lemma 4.1 with these coefficients should give
||[V, h]|| <= C e(B) / M_t. That would make e_L, and so the radii, independent of M_t.

**Lemma 5.2 (parametrix).** Put S_tau := h_tau M_tau(U)^{-1} h_tau and
T_tau := [M_tau(U), h_tau] M_tau(U)^{-1} h_tau (model operators, transplanted: the first h_tau
cuts a global source into A_tau, and the outputs lie in A_tau), B := sum_tau S_tau and
R := sum_tau T_tau. Then

  M(U) B = I + R,   ||S_tau||_{X^* -> X} <= 3 B_F c_h^2,   ||T_tau||_{X^* -> X^*} <= theta,
  ||R||_{X^* -> X^*} <= D_* theta <= 1/2,

so M(U) is invertible and M(U)^{-1} = B sum_{n >= 0} (-R)^n, the series converging in norm.

*Proof.* Identity: let F be a source and Z := M_tau^{-1} h_tau F (a model field). Then h_tau Z is
supported in supp h_tau, so M(h_tau Z) = M_tau(h_tau Z) = h_tau M_tau Z + [M_tau, h_tau] Z =
h_tau^2 F + T_tau F. Summing over tau and using sum h_tau^2 = 1 gives M B = I + R.
Bounds: cutoff multiplication is bounded by c_h on X and X^*, and Lemma 4.2 bounds the local
inverse by 3 B_F; this gives the bound on S_tau. For T_tau, pair with Y in X. The element [M_tau, h_tau] Z, Z := M_tau^{-1} h_tau F, is
supported in A_tau, so <T_tau F, Y> = <[M_tau, h_tau] Z, chi_tau Y>, where chi_tau is a cutoff
obeying flat-port (8.6), equal to 1 on the read closure of supp h_tau and supported in A_tau. By
Lemmas 5.1 and 4.2, |<T_tau F, Y>| <= (C_K/M_t) 3 B_F ||h_tau F||_{X_tau^*} ||chi_tau Y|| <=
(3 B_F c_h^2 C_K / M_t) ||F|| ||Y|| = theta ||F|| ||Y||. For R use the same pairing and Cauchy-Schwarz over tau, with the
two overlap inequalities (flat-port (8.9) and the paragraph after it)

  sum_tau ||chi_tau Y||^2 <= c_h^2 D_* ||Y||^2,   sum_tau ||h_tau F||_{X_tau^*}^2 <= c_h^2 D_* ||F||_{X^*}^2.

The first holds because ||.||^2 is a sum of local terms and a point lies in at most D_* of the
supports. For the second, choose Z_tau with ||Z_tau|| = t_tau := ||h_tau F||_{X_tau^*} and
<F, h_tau Z_tau> = t_tau^2; then sum t_tau^2 = <F, sum h_tau Z_tau> <= ||F|| c_h D_*^{1/2}
(sum t_tau^2)^{1/2}. So ||R|| <= (3 B_F C_K / M_t) c_h^2 D_* = D_* theta <= 1/(16 D_*) <= 1/2. Then
(I + R) sum (-R)^n = I, so B sum (-R)^n is a right inverse of the square matrix M, hence its
inverse. ∎

**Lemma 5.3 (patch words).** For a walk omega = (tau_0, ..., tau_n) put
W_omega := S_{tau_0} (-T_{tau_1}) ... (-T_{tau_n}). Then:
(i) M(U)^{-1} = sum_omega W_omega; at each n the sum over walks of length n is finite and equals
B(-R)^n;
(ii) W_omega = 0 unless supp h_{tau_{m-1}} meets the read closure of supp h_{tau_m} for every m; in
particular X_{tau_{m-1}} ∩ X_{tau_m} is nonempty;
(iii) ||W_omega||_{X^* -> X} <= 3 B_F c_h^2 theta^n;
(iv) W_omega F is supported in supp h_{tau_0} and depends only on F on supp h_{tau_n};
(v) every matrix entry of W_omega is a holomorphic function of a that depends only on U restricted
to X(omega) = X_{tau_0} ∪ ... ∪ X_{tau_n}, on the tower inside N_{tau_0} ∪ ... ∪ N_{tau_n}, and on the
cutoffs h_{tau_m}.

*Proof.* (i) (-R)^n is the finite sum of the products (-T_{tau_1}) ... (-T_{tau_n}) over all
n-tuples of tiles; B is the finite sum of the S_tau. (ii) The rightmost factor h_{tau_{m-1}} of
T_{tau_{m-1}} (or of S_{tau_0}) multiplies the output of [M, h_{tau_m}], which lies in the read
closure of supp h_{tau_m}. Both sets lie in the X's. (iii) Product of the bounds of Lemma 5.2.
(iv) Leftmost and rightmost cutoffs. (v) Each factor is built from M_tau(U)^{-1} (Lemma 4.2),
the coefficients of M near supp h_tau (which read X_tau) and h_tau; products of finitely many
holomorphic matrices are holomorphic. ∎

*Remark (by-products).* The same words for r = 4 give G_0 = [M_4^{-1}]_{AA} as a sum of local
words in the energy norms of flat-port (8.3); for r = 3 they give P and (Q'G'^2Q'^T)^{-1}.
These are energy-norm statements; they are not Balaban's pointwise and Holder bounds (3.42)-(3.47)
for G_0, which this note does not prove.

## 6. Identification of q_0 (proof of part (a))

**Lemma 6.1 (Schur chain; b109 P1 and flat-port (8.2), (8.4), (9.2), reproved).** Let U be any
configuration at which A_s, M_3, M_4 and M_5 are invertible. Put G' := A_s^{-1}. Then
(i) Q'G'^2Q'^T is invertible and [M_3^{-1}]_{hh} = P := G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G';
(ii) T := B_v - D_U P D_U^T = Delta(U) + D_U R D_U^T + Q^T a Q = Delta_a, with R := I - P, is
invertible and T^{-1} = [M_4^{-1}]_{AA};
(iii) Gamma := K T^{-1} K^T is invertible and Gamma^{-1} = -[M_5^{-1}]_{nu nu};
(iv) Q G_0 Q^T = m^{-1} Gamma m^3 and q_0 = m^{-3} Gamma^{-1} m = -m^{-3} [M_5^{-1}]_{nu nu} m.

*Proof.* We use one fact: if M = [[X, Y], [Z, W]] with W invertible, then
M = [[I, Y W^{-1}], [0, I]] [[S, 0], [0, W]] [[I, 0], [W^{-1} Z, I]] with S := X - Y W^{-1} Z; the
outer factors are invertible, so M is invertible if and only if S is, and then
(M^{-1})_{11} = S^{-1}.
(i) The source (g, 0, 0) for M_3 (unknowns h, lambda, mu) gives h + A_s lambda = g,
A_s h - Q'^T mu = 0, Q' lambda = 0. If Q'G'^2Q'^T mu_0 = 0 with mu_0 ≠ 0, then
(G'Q'^T mu_0, -G'^2 Q'^T mu_0, mu_0) is a nonzero solution with g = 0, which is impossible. So the
square matrix Q'G'^2Q'^T is invertible. Then h = G'Q'^T mu, lambda = G'(g - h), and
Q'G'g = Q'G'^2Q'^T mu give mu = (Q'G'^2Q'^T)^{-1} Q'G' g and h = P g.
(ii) Apply the fact to M_4 with W = M_3, X = B_v, Y = (-D_U, 0, 0), Z = Y^T: S = B_v - D_U P D_U^T
by (i). And B_v - D_U P D_U^T = Delta + D_U (I - P) D_U^T + Q^T a Q.
(iii) Apply it to M_5 with W = M_4 and X = 0 (the nu-nu block), Y = (-K, 0, 0, 0), Z = Y^T:
S = -K T^{-1} K^T = -Gamma.
(iv) K = m Q and K^T = Q^T m^{-3} (§3.3) give Gamma = m Q G_0 Q^T m^{-3}. ∎

*Proof of Theorem PI (a).* Lemma 5.2 gives invertibility of A_s, M_3, M_4, M_5 for every
admitted U, and Lemma 6.1 gives the rest of the formulas. The entries are holomorphic in a by
Lemma 5.3 (v) and uniform convergence (Lemma 5.2); equivalently, by Cramer's rule, since the
determinants do not vanish on the domain. At real points (a G-valued) the matrices are real
symmetric and the formulas are Balaban's: G' is his (Delta'_a)^{-1} up to the scalar mass, which
R does not depend on (§3.3), and Delta_a, G_0 are CMP 99b (3.26)-(3.27); Q G_0 Q^T is (3.132)'s
operator. The domain {N_{U_r}(a) < a_1^*} is convex, and holomorphic functions on it agreeing
on its real points agree everywhere; so our operators are the analytic continuations that the
account calls G_0 and q_0 (CA-I 13552-13571). Symmetry: Delta(U), D_U R D_U^T and Q^T a Q are
symmetric for the bilinear pairing, so G_0^T = G_0 and q_0^T = q_0. ∎

## 7. The bound (3.132) and the walk bounds (proof of parts (b)-(d))

Let y in Lambda_j and y' in Lambda_{j'} be field rows. By Lemma 6.1 (iv) and Lemma 5.3 (i),

  q_0(y, y') = sum_omega q_omega(y, y'),   q_omega(y, y') := -l_j^{-3} l_{j'}^{-3} (W^{(5)}_omega)_{nu nu}(y, y'),

as a density for the top pairing: (J psi)(y) = sum_{y'} l_{j'}^4 J(y,y') psi(y') and the counting
entry of m^{-3} Gamma^{-1} m is l_j^{-3} Gamma^{-1}(y,y') l_{j'}; dividing by l_{j'}^4 gives the factor
l_j^{-3} l_{j'}^{-3}.

*Each term.* By (E) and Lemma 5.3 (iii), |(W_omega)_{nu nu}(y,y')| <= 3 B_F c_h^2 theta^n, n = |omega|.
By Lemma 5.3 (iv) the entry vanishes unless y is in supp h_{tau_0} ⊂ X_{tau_0} and y' in
supp h_{tau_n} ⊂ X_{tau_n}. Then, choosing y_m in X_{tau_{m-1}} ∩ X_{tau_m} and using the diameter
bound of §4.3 on each X_{tau_m}, d(omega, y, y') <= D_X (n+1), and d(y,y') <= d(omega,y,y') by the
triangle inequality. Write l_j^{-3} l_{j'}^{-3} = l_j^{-2} l_{j'}^{-4} (l_{j'}/l_j). By (SD),
l_{j'}/l_j <= L^{|j-j'|} <= L exp((log L / (R M_b)) d(y,y')) <= L exp((delta_q/3) D_X (n+1)), since
R M_b >= R_1 M_b >= 3 log L / delta_q. Finally theta^n = theta^{-1/2} theta^{n/2} theta^{(n+1)/2} and
theta^{(n+1)/2} = exp(-(7/2) delta_q D_X (n+1)) by the choice delta_q = log(1/theta)/(7 D_X). Hence

  |q_omega(y,y')| <= 3 B_F c_h^2 L theta^{-1/2} l_j^{-2} l_{j'}^{-4} theta^{n/2} e^{-3 delta_q D_X (n+1)},

which is part (c) since 3 B_F c_h^2 L theta^{-1/2} <= C_q. Locality and holomorphy of q_omega are
Lemma 5.3 (v) for the nu-nu entries.

*Walk sums.* From a fixed tile there are at most D_*^n walks of length n (Lemma 5.3 (ii) and the
overlap count), and D_* theta^{1/2} <= 1/4, so sum_{omega: tau_0 = tau} theta^{|omega|/2} <=
sum_n 4^{-n} <= 4/3; the same holds for walks ending at tau.

*(3.132).* At most D_* tiles tau_0 have y in supp h_{tau_0}. For nonzero terms
e^{-3 delta_q D_X(n+1)} <= e^{-3 delta_q d(y,y')}. Summing the term bound over walks,

  |q_0(y,y')| <= D_* (4/3) 3 B_F c_h^2 L theta^{-1/2} l_j^{-2} l_{j'}^{-4} e^{-3 delta_q d(y,y')}
              <= C_q l_j^{-2} l_{j'}^{-4} e^{-delta_q d(y,y')}.

The series converges absolutely, uniformly in a; this is part (b). In the kernel classes of
CA-I 13402-13410: for f supported on the rows of one block y', |q_0 f| <= C_q c_b l_j^{-2}
e^{-delta_q d(y,y')} sup|f| on the rows of y, with c_b the number of field rows of a block (d per
block), so q_0 is in K_{-2} with constant c_b C_q and rate delta_q.

*(d).* theta = C_theta / M_t is the definition. For any length Lambda <= D_X (n+1) and since
d(omega,y,y') <= D_X(n+1): e^{-3 delta_q D_X(n+1)} <= e^{-delta_q d(omega,y,y')} e^{-2 delta_q Lambda}. ∎

This completes the proof of Theorem PI.

## 8. Use by use: what each consumer reads, and whether Theorem PI supplies it

Account lines are CA-I unless marked II or III, at commit 31a47c543775 (hashes as in
`library/prior/print-inverse.md` §0; checked again here). "Yes" means the read is a conclusion of
Theorem PI under (S1-loc) and (S2), with the rate delta_q of §3.5 in place of Balaban's delta_0.

| Lines | What is read | Supplied? |
|---|---|---|
| 13143-13173 | the remark itself: (3.132) and walks of type (3.98)-(3.99), hull locality, (3.108)-type bounds, for every U in S1-S2 | Yes, under (S1-loc) (Prop. 3.1 gives it from S1 on thick towers). Parts (b), (c), (d). |
| 13589, 13624-13627 | q_0 in K_{-2} and has a walk expansion, at complex U | Yes: (b) and the K_{-2} sentence of §7; (c). |
| 13640-13665 | H_0 = G_0Q^T q_0 l^{-1}, P_0 = I - G_0Q^T q_0 Q; QH_0 = l^{-1}, QP_0 = 0, P_0^TQ^T = 0, Delta_a G~_0 = P_0^T: invertibility and bilinear symmetry | Yes: (a) gives existence of G_0, q_0 and q_0^T = q_0; the identities are then algebra. |
| 13675 | N_beta(H_0 B) <= B_0|B|, N_beta(G~_0 f) <= B'_0|f|_{(-3)}, P_0^T in K_0 | Partly. q_0 in K_{-2} is supplied. These bounds also need Balaban's pointwise and Holder bounds for G_0 (CMP 99b (3.42)-(3.45) via Theorems 3.3-3.4), registry rows B99b-T33, B99b-T34, not proved here. |
| 13683; 19583-19600 | lemma and theorem hypotheses "assume the bounds and the walk expansion of q_0" | Yes, as hypotheses: Theorem PI discharges the BP07 bullet only; the other bullets (averaging analyticity BP09, C_H, ...) stay. |
| 13766 (J3) | q_J in K_{-2}, from q_J = (I + q_0 Q(G^J_pi - G_0)Q^T)^{-1} q_0 with C_J a_gamma <= 1/2 | Yes for the q_0 input: a K_{-2} constant c_b C_q and rate delta_q depending on d, L. The kernel algebra's conditions (13413-13428) become lower bounds on R_1 M_b in terms of delta_q, compatible with item 6 of §3.5. |
| 13787-13793, 13974-13975 (J8) | a walk family for q_0 "with bounds of the type of (3.108) and (1.7)", terms local in their domains, not re-summed | Yes: (c)-(d). The q_0 walks are words over tiles; their domains are the hulls X(omega). |
| 13915-13918 (J4) | H^J decomposition using q_J - q_0 and the H_0 bound | q_0 part yes; the H_0 bound as in row 13675. |
| 14377-14476 | chart definition and representation: inserts Q^T(q_0 - a)B~ and Q^T q_0 B~ | Yes (algebra and existence). |
| 14655 | analyticity of q_0 on the full admitted complex domain | Yes: (a), holomorphic on the whole ball N_{U_r}(a) < a_1^*. |
| 14715-14774 (K3) | |Q^T(q_0 - a)B~|_{(-3)} <= C'|B~|_{(-1)} with C' = C'(d,L) | Yes: q_0 in K_{-2} and kernel algebra (i) give |q_0 B~|_{(-3)} <= C|B~|_{(-1)}; |a B~|_{(-3)} = |B~|_{(-1)}; Q^T is block-local with bounded coefficients and keeps the level weight up to L. |
| 14831 | Q^T(q_0 - a) l^{-1} v in the first variation, weighted decay | Yes, same as K3 with the weights rho of CA-I 12750, since q_0's rate delta_q exceeds the weight rate kappa when kappa <= delta_q / 2. |
| 15271-15348 (K10) | per walk: factors summable by B_0, and two spare exponentials e^{-delta_0 |omega|_{y,y'}} in the anchored tree length; terms analytic and local, so that zero switches separate | Yes, with delta_0 read as delta_q / (1 + 2^d): a tree through y, y' and one point of each X_{tau_m} has length <= D_X(n+1); each X_{tau_m} meets at most 2^d cubes of sigma_0 (side M >> diam X_tau), and a branch to each costs <= D_X; so |omega|_{y,y'} <= (1 + 2^d) D_X (n+1), and (d) applies with Lambda = |omega|_{y,y'}/(1 + 2^d). Summability: (c). Locality: hulls. |
| 15770-15796 | P_0^T Delta_a = Delta_a - Q^T q_0 Q, real minimiser, then complex B | Yes (algebra; existence from (a)). |
| 19744-19750 | operator-bounds theorem: imports J2-J8, K10 | Yes for its q_0 inputs, as above. |
| 5307-5308, 5702 (f4) | ordered word families; entry bound |K_omega(y,y')| <= kappa_omega term by term for coarse operators; (C1) absolute convergence of restricted operators | Yes for q_0: the term bound of (c) is an entry bound term by term, and restriction to any set of walks keeps absolute convergence. |
| 13323 | the near bound frame: the remark "stands under" CMP 109 (3.31)-(3.32) | No new estimate is read. Theorem PI needs (S1-loc), (S2) only. |
| II 54465-54622 (5.8:prop-local-decay) | real backgrounds with (3.35); C_Q = q_0 with factor e^{-8 delta_1 d}, delta_1 = delta_0/32; asserts that within one layer (3.132)'s exponential "does not depend on d(y,y')" | Yes, if delta_0 is the common rate of all the listed operators, as Balaban defines it ("a common, best possible, decay rate", quoted at II 54617-54620), so delta_0 <= delta_q. The within-layer sentence misreads (3.132): the printed bound decays in d(y,y') for all pairs (page image, §1), and so does (b). The lemma on the local decay of C_Q that II builds for this is then not needed for C_Q. |
| II 60313 | list entry for (3.132)-(3.133) | (3.132): yes. (3.133) needs G_0's bounds (row 13675). |
| III 36352-36364 | (3.132) for (QG_1Q^T)^{-1}, G_1 current-corrected, on (3.37)-(3.38) | Not supplied: G_1 is not G_0. The account's (J7) route builds (QG_1Q^T)^{-1} from q_0 by a Neumann series; that series needs G_1 - G_0 small (Theorem 3.12), not proved here. |
| 166593-166594, III 111329 | status lists: "printed without proof; cited as printed" | Would read: proved in this note under (S1-loc), (S2), not yet checked by the other model. |

Two global points for every consumer. (1) Rate: Theorem PI's delta_q is a constant of N, L, fixed
before M_b and R_1; consumers that write Balaban's delta_0 should read the common rate
min{delta_0, delta_q}, which is how Balaban defines delta_0. Every condition we found that ties a
rate to other constants (CA-I 13413-13428; K10's delta_1 M >= kappa_1 with M the CMP 116 cube
side, chosen later) is a lower bound on a later constant, so it survives. (2) Hypothesis: the
remark says "every U satisfying (S1), (S2)"; Theorem PI needs (S1-loc), which (S1) gives on
thick towers (Prop. 3.1). For a thin tower the printed class does not reach the axis of a thin
finger (remark after Prop. 3.1), so neither the remark nor this proof covers it as stated.
