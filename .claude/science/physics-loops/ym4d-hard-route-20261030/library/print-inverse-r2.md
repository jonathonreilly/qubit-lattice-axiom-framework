lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T20:25Z

# PRINT-INVERSE, round 2: the theorem on Balaban's literal rows, with the gate's repairs

Queue row 428 (`pi-r2`). Checkout 3dc1c1a46. Proved by Claude (claude-opus-5-5, max effort),
not yet checked by the other model. Not an audit; it grants no status.

Kind: proof of a step the account cites as printed without proof (CA-I 13144-13178,
4.5:rem-covariance-inverse-walks; registry row PRINT-INVERSE; tree node BP07), now for the
literal rows of the target. Also two counterexamples to the remark's hypothesis, each on a
stated class (Propositions 3.2 and 3.3).

This note replaces `library/print-inverse.md` (round 1, here "r1") in full. It does not depend
on r1. It applies every verdict of `gates/pi-gate.md` (Codex, one line-by-line check of r1).

**Credit.** The operators and the method are Tadeusz Balaban's: CMP 95 §1, CMP 96 §2, CMP 98
§§A-C and E, CMP 99b §3 (Theorems 3.2, 3.9, 3.10 and the sentence before (3.132)). The target,
its consumers, the class S1-S2 and the tower class are from the complete account of Ethan
Sussman and Levent Alpoge (Claude and Codex as authors of their text), commit 31a47c543775. The
exterior convention for distances is the outline's (SA 10113-10127). Library inputs:
`library/flat-port.md` (Codex; checked by Claude, `gates/flat-port-gate.md`) for the flat
inverse; `library/b109.md` P15 (Codex) only for the remark on the symmetric rows (§3.7). The
repairs of `gates/pi-gate.md` (Codex) are used with credit at each use.

**Duplicate check (FINISH rule 0a).** `library/open-core.md` and `library/l17c.md` have no entry
for PRINT-INVERSE, BP07, (3.132), the remark label, the row convention, boundary gluing or
plaquettes outside Omega_0. `library/open-registry.md:428` assigns PRINT-INVERSE to this lane
family, and FINISH row 428 is this item. Row 429 (`b98p5-r2`) attacks lemma (D) of B98-P5, a
different statement, and leaves PRINT-INVERSE to this row.

**Sources.** Balaban's papers in `~/ym4d-papers/` (CMP 95 p.17, 96 p.223, 98 p.17, 99b p.389),
read from page images rendered with PyMuPDF; journal page = (first page - 1) + PDF page. The
account (CA-I) and the outline (SA) were fetched at 31a47c543775 into a scratch folder. Their
SHA-256 (d7f77d4d...d4b6f for SA, 4cb5cb5e...10e6e93 for CA-I) equal the identities in
`library/prior/print-inverse.md:21-26`. No computation is used: every step is a written
argument, and finite arithmetic is displayed.

## 0. The gate's verdicts, and where each is met

| pi-gate verdict | Where it is met here |
|---|---|
| §1 REVISE: bare versus corrected operator at (3.132) | §1.1; Theorem PI(b) is a bound of the displayed scale and decay form for the bare q_0 |
| §2 BLOCK: symmetric rows are not the literal rows | §§4.1-4.4 prove the theorem for Balaban's literal rows; the symmetric rows are a remark (§3.7) |
| §3.1 ADVANCE on interior scope (Prop. 3.1) | kept; boundary points need (S1-loc); Prop. 3.3 shows that (S1) cannot give it there |
| §3.2 BLOCK: "Balaban's Theorem 3.3 fails" | removed; this note makes no claim about Balaban's Theorem 3.3 |
| §3.2 REVISE: exact account claim, size constant | §2 fixes one reading; Prop. 3.2 is stated on that class, for every size constant >= 10 |
| §3.3-3.6 REVISE: variable tile size | §3.3 item 3: one fixed M_t; no uniformity in M_t is claimed |
| §4.2 REVISE: plaquette remainder normalisation | Lemma 5.1, Hessian part |
| §4.3 REVISE: overlap arithmetic | §5.2, Overlap |
| §4.3 REVISE: boundary tiles with exterior centres | §5.2, Exterior tiles; Lemma 5.3 |
| §5 BLOCK: two-settings tower locality | Theorem PI(e) and §9: footprints of half-width (2L+2)M_t l and an explicit assignment |
| §6 REVISE: "a G-valued" | §7 |
| §6 BLOCK: last identification with Balaban's operator | §7: with the literal rows the operators are Balaban's by definition |
| §7 REVISE: part (d) | Theorem PI(d): theta <= (4D_*)^-4, summation factor theta^{n/4}, spare factor theta^{n/4}; no O(M_b^-1) claim |
| §8 consumer table | §11 |

## 1. What was read from the page images

### 1.1 The target displays

**(3.132)**, CMP 99b p.422 (PDF 34): "|(QGQ*)^{-1}(y,y')| <= O(1) (L^j eta)^{-2} (L^{j'} eta)^{-d}
e^{-delta_1 d(y,y')} for y in Lambda_j, y' in Lambda_{j'}, and the same for the operator with G_1
instead of G." The preceding sentence is the one the account quotes. On p.421 Balaban renames
the operator of the earlier sections: "Let us denote for a moment the operator we have
investigated in previous sections by G_0, i.e. G_0 = (Delta + DRD* + Q*aQ)^{-1}", and
introduces the corrected G = G_0(I - Delta'_pi G_0)^{-1} (3.130). So (3.132) is printed for the
corrected G. The account's q_0 uses the bare G_0 (CA-I 13150-13152). Following pi-gate §1, this
note proves for the bare q_0 a bound **of the displayed scale and spatial-decay form**; it does
not identify the bare operator with the printed one. The first line of p.421 ("We have to
investigate also the operator (QGQ*)^{-1}") is written before the renaming, so for the bare G.

**(3.98)-(3.99)**, p.413 (PDF 25), Theorem 3.9: walks omega = ((0,X_0),(alpha_1,X_1),...,
(alpha_n,X_n)) with X_{i-1} ∩ X_i nonempty; a term "depends on U restricted to X~_0^5 ∪ ... ∪
X~_n^5"; its bound is O(1)(L^j eta)^{-4}(L^{j'} eta)^{-d} O(M^{-1/2})^{|omega|} M^{-|omega|/2}
e^{-(1/2) delta_0 d(omega,y,y')}. **(3.93)**, p.410 (PDF 22): d(omega,y,y') = inf over (y_1,...,y_n),
y_i in □_i ∩ 𝔅, of d(y,y_1) + d(y_1,y_2) + ... + d(y_n,y'). **(3.107)-(3.108)**, p.416 (PDF 28):
the walk expansion of G with the bound O(1)(L^j eta)^2 O(M^{-1/2})^{|omega|} M^{-|omega|/2}
e^{-(1/2)delta_0 d(omega,y,y')}|J|, "and the corresponding inequalities for norms on the left-hand
sides of (3.42)-(3.47). The constant O(1) depends on d and L only." These agree with r1 §1.

**The distance**, CMP 96 (2.46), p.231 (PDF 9): d(y,y') = inf over contours Gamma from y to y' of
sum_j (L^j eta)^{-1} |Gamma ∩ B^j(Lambda_j)|, for y, y' in 𝔅 = ∪_j Lambda_j; the contours are
those whose part in B^j(Lambda_j) "consists of bonds of the lattice Lambda_j", and |Gamma| is
the length. In CMP 96 the lowest layer is Lambda_0 = Omega_1^c.

### 1.2 Balaban's averaging, literally (the rows of the target)

The account's Q is "the averaging operator of [CMP 99b §3] in the background U" (CA-I 13149).
CMP 99b p.392: "the averaging operation used here is the operation Ū^j defined by the formulas
(89)-(92) of that paper [CMP 98]. We replace U_0 by U in these definitions, and we have for the
function Q_j(U, eta A) = (1/i) log (exp i eta A)‾^j (3.13)." Then (3.14): (L^j eta)^{-1}
Q_j(U, eta A) = Q_j(U)A + (L^j eta)^{-1} C_j(U, L^j eta A), with Q_j(U)A the linear part, and
(3.15): Q_j(U) = Q(Ū^{j-1}) ... Q(Ū)Q(U), "where Q(V) is given by the explicit formula (124) in
[5]". p.393: "These definitions extend straightforwardly to configurations U, A with values in
the complexified group G^c and algebra g^c." The site rows are (3.18)-(3.19):
(Q'_j(U) lambda)(y) = sum_{x in B^j(y)} L^{-jd} R(U(Gamma^{(j)}_{y,x})) lambda(x).

The ingredients, all read from the page images:

- **Blocks** (CMP 95 (1.6), CMP 98 (2)): B(y) = {x : y_mu <= x_mu < y_mu + L (lattice units),
  mu = 1,...,d}. The base point y is the **lower corner** of its block.
- **Axial contours** (CMP 95 (1.7)): Gamma_{y,x} = [y,(y_1,...,y_{d-1},x_d)] ∪ ... ∪
  [(y_1,x_2,...,x_d), x]; the coordinates change in the order d, d-1, ..., 1.
- **Coarse-bond contours** (CMP 98 p.19): for a coarse bond c = <c_-, c_+> in direction mu and
  x in B(c_-), Gamma_{c,x} := Gamma_{c_-,x} ∪ [x, x(c)] ∪ Gamma_{x(c),c_+}, with x(c) = x + L e_mu.
- **One-step absolute average** (CMP 98 (42)): Ū_c = exp[ i sum_{x in B(c_-)} L^{-d} (1/i)
  log U(Gamma_{c,x}) U(c)^{-1} ] U(c), where U(c) is the product along the straight path from c_-
  to c_+. The k-fold average is the iterate (43). p.24: Ū^k_c "depends only on the bond variables
  U_b for b ⊂ B^k(c_-) ∪ B^k(c_+)", and (Ū^u)_c = u(c_-) Ū_c u^{-1}(c_+).
- **Relative average** (CMP 98 (58)-(63)): with V = V'V_0, V' = V_1^v, the gauge v fixed by the
  axial conditions (58) and the conditions (61), (62) gives
  v(y) = exp[ -i sum_{x in B(y)} L^{-d} (1/i) log (R_{0,y}V_1)(Gamma_{y,x}) ], and (63):
  Vbar_c (V̄_0)_c^{-1} = v(c_-) (V_1V_0)‾_c (V̄_0)_c^{-1} R̄_{0,c} v^{-1}(c_+), R̄_{0,c} = R((V̄_0)_c).
  Here (R_{0,y}V_1)(Gamma_{y,x}) = prod_{b ⊂ Gamma_{y,x}} R(V_0(Gamma_{y,b_-})) V_{1,b} (58).
- **Iterated relative average** (CMP 98 (89)-(91)): Ū_1 = (R(U_0)U_1)‾, Ū_1^{j+1} =
  (R(Ū_0^j) Ū_1^j)‾, "a composition of the operation (89) for V_0 = Ū_0^j".
- **Contour variables** (CMP 98 p.29): U_0(Gamma^{(j)}_{x_j,x}) = Ū_0^{j-1}(Gamma_{x_j,x_{j-1}})
  ... Ū_0(Gamma_{x_2,x_1}) U_0(Gamma_{x_1,x}).
- **The explicit linear form** (CMP 98 (124)-(125), p.36): its main term is (Q_0A)_c =
  sum_{x in B(c_-)} L^{-(d+1)} (R_{0,c_-}A)([x,x']); the four other terms carry factors
  g(-i ad_Y)g^{-1}(-i ad_{Y_x}) - 1 and similar, which vanish at Y = Y_x = 0.

So the literal rows are **one-contour** averages over **corner** blocks, composed at the
successive **averaged backgrounds**. They are not the symmetric straightened rows of CMP 109
used by `b109.md` P15; SA 10287 makes the same distinction ("Statements 3-8 concern different
operators, built from the rows of M").

### 1.3 The regularity class

CMP 99b p.396 (PDF 8): "For each cube □ of this class there exists a unique index j, 0 <= j <= k,
such that □ ⊂ B^j(Lambda_j) ∪ B^{j+1}(Lambda_{j+1}), □ ∩ B^j(Lambda_j) ≠ ∅, and □ is a union of
several big blocks of the lattice T_{L^{-j}}, which implies that its size in the lattice T_eta
is O(1)ML^j eta. Here O(1) will mean a number >= 10. The set Lambda_0 ... Lambda_0 = Omega_0 \
Omega_1, where Omega_0 = {a union of big blocks of the lattice T_1, such that their distances to
Omega_1 are <= RM}." Condition (3.35) asks, on each such cube, for a gauge u on □ with U^u =
e^{i eta A} and |A| < O(1)M alpha_0 (L^j eta)^{-1}, |∇A| < O(1)M alpha_0 (L^j eta)^{-2} on □.
"These regularity conditions do not impose any constraints on U outside the domain Omega_0."

CA-I 12712-12724 (towers): each Omega_j is a union of blocks of side 𝔐 L^j eta with
(L^j eta)^{-1} dist(Omega_j^c, Omega_{j+1}) > R𝔐, R >= R_1; "With each Omega_j one associates
the set of bonds having at least one end-point in Omega_j"; Omega_0 := X for localised terms.
CA-I 12697-12699: Balaban's block M is read as 𝔐 (here M_b). CA-I 12943-12973, (S1): U =
e^{i eta 𝔞}U_r, U_r satisfies (3.35) on "the cubes ... of size O(1)𝔐 in level-j units. By
[CMP 99b p.409] the number O(1) may be taken equal to 12", with l_j|A| < a_0, l_j^2|∇A| < a_0;
(S2): N_{U_r}(𝔞) < a_1. Then: "Conditions (S1) and (S2) give, at level j, |∂U - 1| <=
4(a_0 + a_1) eta^2 l_j^{-2}."

## 2. The reading fixed here (item 2)

**2.1 Lattices and towers.** d = 4. G = SU(N), with Lie algebra 𝔤 written as Hermitian
traceless matrices (U = e^{iX}), 𝔤^c = sl(N,C), G^c = SL(N,C); tr is normalised, tr 1 = 1. L is
odd, L >= 3; eta = L^{-k}; l_j = L^j eta; T^{(j)} = l_j Z^4 ∩ T_eta, where T_eta is a periodic
fine box whose side is a multiple of M_b l_k. Blocks are Balaban's **corner** blocks:
B^j(y) = {x in T_eta : y_mu <= x_mu < y_mu + l_j} for y in T^{(j)}; one-step blocks B(y) on
T^{(m)} are the same with l_{m+1} and T^{(m)}. Level-j big blocks are the cubes
y + [0, M_b l_j)^4, y in M_b l_j Z^4, with M_b a power of L. A **tower** is the account's
(CA-I 12712-12724): Omega_0 ⊃ ... ⊃ Omega_k, Omega_j a union of level-j big blocks,

  (T)  l_j^{-1} dist(Omega_j^c, Omega_{j+1}) > R M_b,   R >= R_1,   Omega_{k+1} := ∅,

with Omega_0 any such union (Omega_0 = T_eta allowed). Balaban's restriction of Omega_0 to the
RM-neighbourhood of Omega_1 (p.396) is **not** imposed. Lambda_j := T^{(j)} ∩ (Omega_j \
Omega_{j+1}). The **level** of a site is lambda(x) := max{j : x in Omega_j} for x in Omega_0,
and lambda(x) := 0 for x outside Omega_0 (pi-gate §4.3: level extended by zero).

**2.2 The cube class.** 𝒞_j is the set of cubes □ that are unions of level-j big blocks, have
side exactly 12 M_b l_j, satisfy □ ⊂ Omega_j \ Omega_{j+2}, and meet Omega_j \ Omega_{j+1}. The
**bonds of □** are the fine bonds with both end-points in □. This is p.396 with its size number
read as 12 (the account's choice, CA-I 12951-12953) and M read as M_b. Balaban's text allows "a
number >= 10"; Proposition 3.2 holds for every reading in which the class cubes of level 0 have
side at least 10 M_b l_0, and Proposition 3.1 uses only cubes of side 12 M_b l_j.

**2.3 Fields, rows and the boundary.** Field variables are fine bonds with at least one
end-point in Omega_0 (CA-I 12721-12722); scalar variables are sites of Omega_0; everything is
extended by zero (Dirichlet). A **row of level j** is a positively oriented bond c of T^{(j)}
with an end-point in Omega_j and no end-point in Omega_{j+1} (for j = 0 the rows are the fine
field bonds with no end-point in Omega_1). This is the difference convention of CA-I 12721 and
of `flat-port.md` §2.1 (the default, no-inward convention, SA 10113-10127). Its **base point**
y_c is the end-point of c in Omega_j \ Omega_{j+1} (c_- if both are). A **site row** of level j
is a point of Lambda_j (for j = 0: a site of Omega_0 \ Omega_1). The Wilson Hessian is the
second variation of the full action restricted to the field variables; it reads U on every
plaquette that contains a field bond, also where such a plaquette leaves Omega_0 (as SA 10287
states for G_0). So U is needed on the bonds of Omega_0^+ := {x : dist_inf(x, Omega_0) <= 2 eta}.

**2.4 Hypotheses.** (S1), (S2) are the account's, with the class of 2.2. (S2) is read on the
bonds of the hierarchy; on the bonds of Omega_0^+ that have an end-point outside Omega_0 it is
read at level 0 (eta|𝔞| < a_1, eta^2 |∇_{U_r}𝔞| < a_1); call this (S2+). The theorem uses the
local form

**(S1-loc)** for every site x of Omega_0, with j = lambda(x) and N(x) the closed l^inf box of
half-width r_N l_j about x, there is a G-valued gauge u on the sites of N(x) such that, on the
bonds of N(x), U_r^u = e^{i eta A} with l_{lambda(z)}|A| <= L^2 a_0 and l_{lambda(z)}^2 |∇A| <=
L^2 a_0 at every point z of N(x) (lambda extended by zero).

Here ∇ is the flat forward difference and |.| the operator norm. r_N is fixed in §3.3.

**2.5 Distance.** d is Balaban's CMP 96 (2.46) for the tower in which Omega_0 is replaced by
T_eta (lowest layer Omega_1^c, as in CMP 96 itself): contours on T_eta whose part in
B^n(Lambda_n) consists of bonds of T^{(n)}, length counted in units l_n there and in units eta
outside Omega_1. For Omega_0 = T_eta this is Balaban's distance of the tower; otherwise it is
the gate's exterior convention (pi-gate §4.3; SA 10113-10127 with lattice contours). It is
defined on the tops of that tower, which include every base point y_c and every site row.

**2.6 What each result covers.** Theorem PI holds on every tower of 2.1 under (S1-loc), (S2),
(S2+). Proposition 3.1 derives (S1-loc) from (S1) at the sites x with N(x) ⊂ Omega_0 of a tower
with thick levels. Propositions 3.2 and 3.3 show that (S1), (S2) as fixed here do not give the
remark's conclusion on the account's tower class: 3.2 with a thin remote finger, 3.3 at a
single bond leaving any proper Omega_0. Neither is a claim about Balaban's p.396 class or about
his Theorem 3.3, whose boundary conventions the printed page does not fix.

## 3. Operators, norms, constants, and the statements

### 3.1 Operators

Let U be a G^c-valued configuration on the bonds of Omega_0^+. D_U is the covariant site
difference, (D_U lambda)(b) = eta^{-1}(R(U_b) lambda(b_+) - lambda(b_-)), R(X)Y = XYX^{-1}, and
D_U^T its bilinear transpose; at unitary U this is CMP 99b (3.8). Delta(U) is the operator of
the second variation of the Wilson action at U, CMP 99b (3.10), continued holomorphically
(U* replaced by U^{-1}); at U = 1 it is the compressed curl form. Q(U) and Q'(U) are the
**literal** field and site rows of Definition 4.3 (CMP 99b (3.13)-(3.19)). All act on the
Dirichlet spaces of 2.3.

Pairings (CA-I 12756-12759): eta^4 sum tr on fine objects; l_j^4 sum tr on rows of level j (the
top pairing); sum tr on rows (the counting pairing, used for the multiplier nu). ^T is the
bilinear transpose. m is the local scale: l_j on rows of level j, l_{lambda(x)} at a site, and
on a fine bond the larger end-point scale. Put a := l^{-2} on field rows (CA-I 13593), and
K := mQ, a map into rows with the counting pairing. Then K^T = Q^T m^{-3} and K^T K = Q^T a Q.
Put

  A_s := D_U^T D_U + Q'^T m^{-2} Q',     B_v := Delta(U) + D_U D_U^T + Q^T a Q,

and, on X = (A, h, lambda, mu, nu),

           | B_v      -D_U    0      0      -K^T |
           | -D_U^T    I      A_s    0       0   |
  M_5(U) = | 0         A_s    0     -Q'^T    0   |      (flat-port (8.1) and §9.2)
           | 0         0     -Q'     0       0   |
           | -K        0      0      0       0   |

M_4 := rows and columns 1-4; M_3 := rows and columns 2-4; M_1 := A_s. Every coefficient is a
finite stencil or a single row: the projection R and the propagator G_0 are not coefficients.
When the inverses exist put G' := A_s^{-1}, P := G'Q'^T(Q'G'^2Q'^T)^{-1}Q'G', R := I - P,
Delta_a := Delta(U) + D_U R D_U^T + Q^T a Q, G_0 := Delta_a^{-1}, q_0 := (Q G_0 Q^T)^{-1}.
For real U, R is the orthogonal projection onto Delta_U N(Q'), and it does not depend on the
mass in G': for lambda in N(Q'), (Delta_U + Q'^T alpha Q')lambda = Delta_U lambda for every
alpha > 0. So R, Delta_a and G_0 are those of CMP 99b (3.21)-(3.27) and of CA-I 13583-13595.

### 3.2 Norms

As `flat-port.md` (8.3) with the row multiplier of its §9.2. Differences are covariant at the
real part U_r, extended by zero at the Dirichlet boundary; L^2 norms carry eta^4:

  ||X||_X^2 = ||∇A||^2 + ||m^{-1}A||^2 + ||h||^2 + ||m^{-2}lambda||^2 + ||m^{-1}D lambda||^2
              + sum_{alpha,beta} ||D_alpha D_beta lambda||^2 + ||m^2 mu||_top^2 + ||nu||_count^2.

For r = 3, 4, 5 the source space Y_r is the dual X_r^*; for r = 1 it is Y_1 := L^2, with A_s
read as a map H^2_m -> L^2 (flat-port.md:588). The norms of M_r are the restrictions to its
variables. On a local model (§5.2) the same formula on its geometry defines X_tau. Each norm is
a sum of local terms, so on fields supported where a model and the actual geometry agree the
two norms coincide. Since ||nu||_count is a component,

  (E)   |W_{nu nu}(c,c')| <= ||W||_{Y -> X}   for field rows c, c' and every operator W,

where the left side is the norm of the colour block; the unit source at c' in the nu slot has
dual norm 1, and the nu component of an element of X is bounded by its norm.

### 3.3 Constants and their order

All depend only on N and L, and are fixed in this order.

1. From the flat input [F] (§4.4): the tile size M_F and separation rho_F of flat-port §8.2,
   the bound B_F >= 1, the commutator constant C_88 of flat-port (8.8), and c_h >= 1, a bound
   for multiplication by a cutoff obeying flat-port (8.6) on X and on Y. Put
   rho'_F := M_F ceil(rho_F / M_F).
2. From §4: the one-step radius r_1 := 1/(500 L) and the constants e_R, C_R of Lemma 4.4. From
   §5: e_C, C_C of Lemma 5.1 and C_S of (5.4). Put C_K := 3 C_88 and D_* := 3 (20 L)^4.
3. One tile size M_t: a power of L, a multiple of L M_F, with M_t >= max{2 rho'_F, 4L} and
   theta := 3 B_F c_h^2 C_K / M_t <= (4 D_*)^{-4}. (Every later constant is computed from this
   M_t. Another admissible M_t gives the theorem again with all of items 4-8 recomputed; no
   statement uniform in M_t is made; pi-gate §3.3.)
4. r_N := 7 M_t, r^ := (2L + 2) M_t, D_X := 24 L^2 M_t.
5. delta_q := log(1/theta) / (7 D_X) > 0.
6. Floors: M_b a power of L and a multiple of M_t with 2 r_N L + 1 <= 11 M_b; R_1 >= 24 with
   R_1 M_b >= max{rho'_F, 4L(r^ + L) + 1, 3 log L / delta_q}.
7. e_L := min{e_C, 1/(8 B_F C_C), C_88 / (2 c_h C_C M_t)}, and radii a_0^*, a_1^* in (0, 1]
   with C_S (L^2 a_0^* + a_1^*) <= e_L.
8. C_q := 4 D_* B_F c_h^2 L theta^{-1/2}.

Nothing here depends on k, eta, the volume, the tower or U. The account's floors on M_b and
R_1 M_b (CA-I 12671-12683; its kernel algebra 13413-13428) are lower bounds of the same kind.
They must be imposed at the rate delta_q, or at the smaller common rate a consumer uses,
before the kernel algebra is applied (pi-gate §§3.3, 7).

### 3.4 The theorem

A **tile** is a cube of side M_t l_j of the level-j tile grid (corners in M_t l_j Z^4) that lies
in Omega_j \ Omega_{j+1}; if Omega_0 ≠ T_eta, an **exterior tile** is a cube of the level-0 tile
grid disjoint from Omega_0 that contains the initial point of a field bond (§5.2). A tile tau has
a level j_tau (0 for exterior tiles) and a centre x_tau (a site, since M_t is odd). Its
**footprint** F_tau is the closed l^inf cube of half-width r^ l_{j_tau} about x_tau. A **walk**
is a sequence omega = (tau_0, ..., tau_n), n = |omega| >= 0, of tiles in which the boxes of
half-width r_N l_{j} about consecutive centres meet. Its footprint is
|omega| := F_{tau_0} ∪ ... ∪ F_{tau_n}. A **setting** s = (tower, U) on the box T_eta consists of
a tower of 2.1 and a configuration U on the bonds of Omega_0^+. Two settings **agree on** a set W
if Omega_n ∩ W = Omega'_n ∩ W for every n and U_b = U'_b for every bond b with both end-points
in W.

**Theorem PI.** Fix the constants of §3.3. Let k >= 0, let T_eta be a periodic fine box of side at
least (2 r^ + 2) l_k, let the tower satisfy 2.1 with R >= R_1, and let U = e^{i eta 𝔞} U_r satisfy
(S1-loc) with a_0 <= a_0^*, and (S2), (S2+) with a_1 <= a_1^*. The rows are Balaban's literal
rows (Definition 4.3).

(a) *Existence and identification.* M_1 = A_s, M_3, M_4 and M_5 are invertible. Hence
Q'G'^2Q'^T, R, Delta_a, G_0 and q_0 exist; q_0 = -m^{-3} [M_5^{-1}]_{nu nu} m and q_0^T = q_0. Each
is holomorphic in 𝔞 on the set where the hypotheses hold (for fixed U_r), and for 𝔞 with values
in 𝔤 (so U is G-valued) each is the operator of CMP 99b §3 built with Balaban's averaging, the
conventions of §2 and the mass a = l^{-2} of CA-I 13593.

(b) *Bound of the form of (3.132).* For field rows c of level j and c' of level j',

  |q_0(c,c')| <= C_q l_j^{-2} l_{j'}^{-4} e^{-delta_q d(y_c, y_{c'})},

as a density for the top pairing. For f supported on the rows with base point y',
sup_{rows at y} |q_0 f| <= 2·4 C_q l_j^{-2} e^{-delta_q d(y,y')} sup|f|.

(c) *Walk expansion, at a fixed setting.* q_0 = sum_omega q_omega over walks, absolutely
convergent at every (c,c'). Each q_omega is holomorphic in 𝔞 and depends on U only through
its values on X(omega) := X_{tau_0} ∪ ... ∪ X_{tau_n}, where X_tau ⊂ F_tau is the read set of the
local model (§5.2). q_omega(c,c') = 0 unless the base point y_c lies in the support of the
cutoff h_{tau_0} and y_{c'} in that of h_{tau_n}; then d(omega, y_c, y_{c'}) <= D_X (|omega| + 1),
with d(omega,·,·) the distance (3.93) whose intermediate points y_m are tops in F_{tau_m}; and

  |q_omega(c,c')| <= C_q l_j^{-2} l_{j'}^{-4} theta^{|omega|/2} e^{-3 delta_q D_X (|omega| + 1)}.

(d) *Majorants.* theta^{|omega|/2} = theta^{|omega|/4} · theta^{|omega|/4}. For every tile tau,
sum theta^{|omega|/4} <= 4/3 over the walks starting at tau, and also over the walks ending at
tau (summation factor); the second factor is a spare factor (4 D_*)^{-|omega|} at most. For every
Lambda <= D_X(|omega| + 1),

  e^{-3 delta_q D_X(|omega|+1)} <= e^{-delta_q d(omega, y_c, y_{c'})} e^{-2 delta_q Lambda}.

This is a geometric walk majorant at the one fixed tile size M_t, with two spare exponentials.

(e) *Setting-compatible assignment.* Let s, s' be settings that satisfy the hypotheses, and let
omega be a walk of s. If s and s' agree on |omega|, then omega is a walk of s' and
q_omega^s = q_omega^{s'}. Hence, for every closed W ⊂ T_eta on which s and s' agree, the
restricted sums q_0^W := sum over walks with |omega| ⊂ W of q_omega are equal for s and s'
(the same index set and the same terms). The support of q_omega lies at l^inf distance at least
(2L + 1) M_t l_{j_{tau_0}} from the boundary of |omega| at the first end, and the same at the last.

Part (a) uses no walk bound; (b) follows from (c) and (d); the field read in (c) is not enlarged
by (e), which concerns only the tower read (pi-gate §5).

### 3.5 Proposition 3.1 ((S1) gives (S1-loc) at interior points of thick towers)

Assume the constants of §3.3 and (Thick): each Omega_i is a union of cells of a grid of spacing
s_i that is aligned with the level-i big-block grid, with s_i a multiple of M_b l_i and
s_i >= 12 M_b l_i. Then (S1) with the class 𝒞 of 2.2 implies (S1-loc) at every site x of Omega_0
with N(x) ⊂ Omega_0; in particular at every site when Omega_0 = T_eta.

At a site x with N(x) ⊄ Omega_0, (S1-loc) is an additional hypothesis. Proposition 3.3 shows that
(S1), (S2) cannot replace it there.

### 3.6 Propositions 3.2 and 3.3 (the hypothesis (S1) is not enough on the account's towers)

**Proposition 3.2 (thin remote finger).** Let G = SU(2). Read the cube class as in 2.2, or with
any size number >= 10 in place of 12. Let Omega_0 contain a finger F: a box of w x w x w x l
level-0 big blocks with w <= 9 and l >= 200, attached at one end to the rest of Omega_0, every
point of it at distance greater than (R + 24) M_b eta from Omega_1. Then there is a real U with
𝔞 = 0 that satisfies (S1) and (S2), at which Delta_a is singular; so G_0 and q_0 do not exist.
There is also a real U' with 𝔞 = 0 that satisfies (S1) and (S2) and has |∂U' - 1| = 2 at six
plaquettes, so the plaquette bound of CA-I 12968-12973 fails when a_0 + a_1 < 1/2.

**Proposition 3.3 (a single bond leaving Omega_0).** Let G = SU(2) and let Omega_0 ≠ T_eta, with
the conventions of 2.2-2.3. Then there is a real U with 𝔞 = 0 that satisfies (S1) and (S2), at
which Delta_a is singular. U differs from 1 on one field bond that has an end-point outside
Omega_0, so (S1-loc) fails at that bond's inner end.

Proposition 3.2 is excluded by Balaban's p.396 restriction (every big block of Omega_0 within
R M_b l_0 of Omega_1). Proposition 3.3 uses the account's convention that field bonds touch
Omega_0 (CA-I 12721-12722) and that the cube test concerns bonds inside a cube. Under a
convention in which fields and plaquettes are those inside Omega_0, its mechanism does not
apply. Neither proposition is a claim about Balaban's Theorem 3.3.

### 3.7 Remark: the symmetric straightened rows

The proof below uses the rows only through Lemma 4.4 (locality, holomorphy, covariance, flat
value, depth-uniform comparison). `library/b109.md` P15 (71), (74) gives the same properties for
the symmetric straightened rows of CMP 109 (SA (PX141)), with a read enlargement c_r of a double
block; pi-gate §4.2 checked those steps. With Lemma 4.4 replaced by P15 and M_t >= 2 c_r L,
Theorem PI holds verbatim for those rows (the operators "built from the rows of 𝓜" in SA
10287). Those are not the target's rows; the target is the statement above.
