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

The account's Q is "the averaging operator of [CMP 99b §3] in the background U" (CA-I 13150).
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
read as 12 (the account's choice, CA-I 12953-12955) and M read as M_b. Balaban's text allows "a
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
field bonds. On the bonds of Omega_0^+ with no end-point in Omega_0 (they are read only through
plaquettes) it is read at level 0: eta|𝔞| < a_1 and eta^2 |∇_{U_r}𝔞| < a_1, for differences
between bonds of Omega_0^+; call this (S2+). The theorem uses the local form

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
on a fine bond the larger end-point scale. Put a := l^{-2} on field rows (CA-I 13585), and
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
level-0 big blocks with w <= 9 and l >= 200, attached at one end to the rest of Omega_0, with
Omega_0 equal to F within distance 31 M_b eta of the middle cross-section of F, and every point of
F at distance greater than (R + 24) M_b eta from Omega_1. Then there is a real U with
𝔞 = 0 that satisfies (S1) and (S2), at which Delta_a is singular; so G_0 and q_0 do not exist.
There is also a real U' with 𝔞 = 0 that satisfies (S1) and (S2) and has |∂U' - 1| = 2 at six
plaquettes, so the plaquette bound of CA-I 12968-12973 fails when a_0 + a_1 < 1/2.

**Proposition 3.3 (a single bond leaving Omega_0).** Let G = SU(2) and let Omega_0 ≠ T_eta, with
the conventions of 2.2-2.3. Then there is a real U with 𝔞 = 0 that satisfies (S1) and (S2), at
which Delta_a is singular. U differs from 1 only on one field bond that has an end-point
outside Omega_0. By Theorem PI, (S1-loc) with a_0 <= a_0^* must fail at U, at a site whose box
N(x) contains that bond.

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

## 4. Balaban's literal rows (item 1)

This section proves for the literal rows the properties that the rest of the proof reads. It
replaces r1's use of `b109.md` P15 (pi-gate §2). The method is P15's (straighten, bootstrap,
telescope), applied to Balaban's own one-contour construction; credit `b109.md` P15 and SA
(PX141)-(PX149) for the method and Balaban for the construction.

### 4.1 Analytic facts

|X| is the operator norm of an N x N matrix; for a configuration b, |b| := max over its bonds.

**Lemma 4.1.** (i) |e^X - 1| <= e^{|X|} - 1, which is <= 2|X| when |X| <= 1.
(ii) If |H| <= 1/2, log(1 + H) := sum_{k>=1} (-1)^{k+1} H^k / k converges absolutely,
|log(1 + H)| <= 2|H| and exp(log(1 + H)) = 1 + H. If |X| <= 1/4 then log(e^X) = X. If g is
invertible and |gHg^{-1}| <= 1/2, then log(1 + gHg^{-1}) = g log(1 + H) g^{-1}.
(iii) |X_1 ... X_n - 1| <= prod_i (1 + |X_i - 1|) - 1.
(iv) Let f be holomorphic on {|z| < r} in a finite-dimensional space with the norm |z|, with
values in a normed space, and |f| <= K. For |z| <= r/2: |f(z) - f(0)| <= 2K|z|/r and
|f(z) - f(0) - Df(0)z| <= 2K|z|^2/r^2. If f(z, w) is holomorphic on {|z| < r, |w| < r} with
|f| <= K, then for |z| <= r/2: |D_w f(z,0)w - D_w f(0,0)w| <= 2K|z||w|/r^2.

*Proof.* (i), (ii), (iii): multiply and compare the absolutely convergent power series; the
identities in (ii) are identities of one-variable power series, valid in the commutative algebra
generated by H or X, and the last one holds term by term. (iv): for z ≠ 0 put s = |z| and
g(t) := f(tz/s), holomorphic and bounded by K on |t| < r. Cauchy's estimate gives
|g^{(n)}(0)/n!| <= K r^{-n}, and f(z) = g(s); sum the tails with s/r <= 1/2. For the second
statement put G(t,u) := f(tz/s, uw/|w|) on |t|, |u| < r. Cauchy's estimate in u gives
|∂_u G(t,0)| <= K/r; apply the first statement to t ↦ ∂_u G(t,0). ∎

### 4.2 Balaban's one-step maps

Work on one step, from T^{(m)} to T^{(m+1)}, in units l_m = 1; blocks have side L. For a bond c of
T^{(m+1)} in direction mu let D(c) := B(c_-) ∪ B(c_+), and E(c) the bonds of T^{(m)} with both
end-points in D(c). W(Gamma) is the ordered product along a contour, (V_1V_0)_b := (V_1)_b(V_0)_b,
and W^g_b := g(b_-) W_b g(b_+)^{-1}.

**Definition 4.2 (CMP 98 (42), (58)-(63)).**
  𝒜(W)_c := exp[ sum_{x in B(c_-)} L^{-4} log(W(Gamma_{c,x}) W(c)^{-1}) ] W(c),
  z_W(y) := exp[ sum_{x in B(y)} L^{-4} log W(Gamma_{y,x}) ]     (y a site of T^{(m+1)}),
  v(y) := exp[ - sum_{x in B(y)} L^{-4} log((V_1V_0)(Gamma_{y,x}) V_0(Gamma_{y,x})^{-1}) ],
  𝓡(V_0; V_1)_c := v(c_-) 𝒜(V_1V_0)_c v(c_+)^{-1} 𝒜(V_0)_c^{-1}.

This is Balaban's relative average: the product (58) telescopes,
prod_{b ⊂ Gamma_{y,x}} R(V_0(Gamma_{y,b_-})) V_{1,b} = (V_1V_0)(Gamma_{y,x}) V_0(Gamma_{y,x})^{-1},
so v is (62); and R̄_{0,c} v^{-1}(c_+) = (V̄_0)_c v^{-1}(c_+) (V̄_0)_c^{-1}, so 𝓡 is the right side
of (63). For V_0 = e^{ib} put F(b)_c := (1/i) log[z(c_-)^{-1} 𝒜(e^{ib})_c z(c_+)] with
z := z_{e^{ib}}, and Phi(b, a)_c := (1/i) log 𝓡(e^{ib}; e^{ia})_c. Let S be the straight map,
(Sb)_c := sum_{x in B(c_-)} L^{-4} sum_{t=0}^{L-1} b(x + t e_mu, x + (t+1) e_mu).

**Lemma 4.2.** Put r_1 := 1/(500 L). Let b, a be 𝔤^c-valued on E(c) with |b|, |a| < r_1.
(i) Every logarithm in Definition 4.2, at V_0 = e^{ib}, V_1 = e^{ia}, W = e^{ib}, has its argument
within 1/2 of 1; F, Phi, z are holomorphic; |F| <= 1, |Phi| <= 1 and |z^{±1} - 1| <= 1/50.
(ii) F(0) = 0, z(0) = 1, Phi(b, 0) = 0, Phi(0, a) = F(a); hence DF(0) = D_a Phi(0, 0) = S.
(iii) Covariance. If g is a G-valued site function on D(c), or a G^c-valued one with
|g^{±1} - 1| <= 1/10, then 𝒜(W^g)_c = g(c_-) 𝒜(W)_c g(c_+)^{-1} and
𝓡(V_0^g; Ad_g V_1)_c = g(c_-) 𝓡(V_0; V_1)_c g(c_-)^{-1}, where (Ad_g V_1)_b := g(b_-) V_{1,b} g(b_-)^{-1}.
(iv) For |b| <= r_1/2: |F(b) - Sb| <= 2|b|^2/r_1^2 and |z^{±1} - 1| <= |b|/r_1. Let Q^ang(e^{ib})
be the linear map a ↦ D_a Phi(b,0)a; each of its entries (the linear map 𝔤^c -> 𝔤^c from a_{b'}
to the c-component) differs from that of S by at most 2|b|/r_1^2 in operator norm.
(v) S has row sum L and column sum L^{-3} (sums of its scalar entries). A row of Q^ang reads at
most 8L^4 bonds; a bond is read by at most 16 rows.
(vi) 𝒜(W)_c, F(b)_c and Phi(b,a)_c read only the bonds of E(c); z(y) reads only those in B(y).

*Proof.* (i) Gamma_{c_-,x} and Gamma_{x(c),c_+} have at most 4(L-1) bonds each, [x, x(c)] and the
straight path of c have L. So W(Gamma_{c,x})W(c)^{-1} is a product of at most 10L factors
e^{±ib}; by Lemma 4.1 (i), (iii) it lies within e^{10 L r_1} - 1 = e^{1/50} - 1 < 0.021 of 1.
Its logarithm has norm < 0.042 (Lemma 4.1 (ii)), and so has the mean; so |𝒜(W)_c - 1| <=
e^{0.042} e^{L r_1} - 1 < 0.046. The arguments in v are products of at most 12L factors of the
form e^{±ia}, e^{±ib}, so they lie within e^{24 L r_1} - 1 < 0.05 of 1, and |v^{±1} - 1| < 0.11.
The product V_1V_0 has |e^{ia}e^{ib} - 1| <= e^{2r_1} - 1, so as for 𝒜, |𝒜(V_1V_0)_c - 1| < 0.09.
Hence |𝓡 - 1| <= (1.11)^2 (1.09)(1.046) - 1 < 0.41 and |Phi| <= 0.82. z: at most 4L factors,
|z^{±1} - 1| <= e^{0.018} - 1 < 1/50; and |z(c_-)^{-1} 𝒜 z(c_+) - 1| < (1.02)^2 (1.046) - 1 < 0.09,
so |F| < 0.18. Every map is a finite composition of convergent power series in the entries of
b and a, hence holomorphic.
(ii) At b = 0 all factors are 1. At V_1 = 1, v = 1 and 𝓡 = 𝒜(V_0)𝒜(V_0)^{-1} = 1. At V_0 = 1,
v = z_{V_1}^{-1} and 𝒜(V_0) = 1, so 𝓡(1; V_1)_c = z_{V_1}(c_-)^{-1} 𝒜(V_1)_c z_{V_1}(c_+), whose
logarithm is F(a). To first order, log W(Gamma) = i b(Gamma) + O(|b|^2), with b(Gamma) the
signed sum along Gamma. So the exponent of z(c_-)^{-1}𝒜 z(c_+) is, to first order,
i sum_{x in B(c_-)} L^{-4}[ -b(Gamma_{c_-,x}) + b(Gamma_{c_-,x}) + b([x,x(c)]) - b(Gamma_{c_+,x(c)}) ]
+ i sum_{x' in B(c_+)} L^{-4} b(Gamma_{c_+,x'}) = i (Sb)_c,
because x ↦ x(c) = x + L e_mu maps the corner block B(c_-) onto B(c_+).
(iii) W^g(Gamma_{c,x}) W^g(c)^{-1} = g(c_-)[W(Gamma_{c,x})W(c)^{-1}]g(c_-)^{-1} is a closed loop at c_-;
and (Ad_g V_1 · V_0^g) = (V_1V_0)^g, so the argument in v becomes g(y)[...]g(y)^{-1}. For unitary
g conjugation keeps operator norms; for |g^{±1} - 1| <= 1/10 it multiplies them by at most
(1.1)^2, and the margins in (i) stay below 1/2. Lemma 4.1 (ii) moves g through each logarithm,
and the exponentials and products give the two formulas.
(iv) Lemma 4.1 (iv) with K = 1 and r = r_1: for F with (ii); for z^{±1} - 1 with K = 1/50 (giving
|z^{±1} - 1| <= |b|/(25 r_1)); for the entries with the mixed statement applied to Phi(b, u w e_{b'}),
|w| <= 1. (v) Row sum L^{-4} · L^4 · L; a fine bond in direction mu lies on [x, x(c)] for exactly
L sites x on its line, each in one block, each fixing one c: L · L^{-4}. E(c) has at most
4 · 2L^4 bonds; a bond lies in E(c) for at most 2 · 2 · 4 rows c. (vi) By inspection. ∎

### 4.3 The literal rows and their comparison

**Definition 4.3 (CMP 99b (3.13)-(3.19); CMP 98 (43), (89)-(91), p.29).** For a configuration U,
put Ū^0 := U and Ū^{m+1} := 𝒜(Ū^m), and 𝓡^0(U; V_1) := V_1, 𝓡^{m+1}(U; V_1) := 𝓡(Ū^m;
𝓡^m(U; V_1)). For a field row c of level j >= 1 and a fine potential A,

  Q_j(U)A_c := l_j^{-1} (d/ds)|_{s=0} (1/i) log 𝓡^j(U; e^{i s eta A})_c,

and Q_0 := I. For a site row y of level j >= 1,
(Q'_j(U)lambda)(y) := sum_{x in B^j(y)} L^{-4j} R(U(Gamma^{(j)}_{y,x})) lambda(x), with the contour
variable U(Gamma^{(j)}_{y,x}) := Ū^{j-1}(Gamma_{x_j,x_{j-1}}) ... Ū^1(Gamma_{x_2,x_1}) U(Gamma_{x_1,x}),
x_j := y and x_m the corner of the level-m block that contains x; Q'_0 := I.

Since 𝓡(V_0; 1) = 1, the chain rule gives Balaban's (3.15): Q_j(U) = L^{-j} Q^ang(Ū^{j-1}) ...
Q^ang(Ū^0), each factor the one-step linear map of Lemma 4.2 at its level, read in that level's
units; Balaban writes it in the potential normalisation as (124), whose main term (125) is
L^{-1} S. The definition at complex U is the "straightforward" extension of CMP 99b p.393.

**Lemma 4.4 (literal rows).** There are e_R in (0, r_1/3] and C_R, depending only on N and L,
such that the following holds. Let c be a field row of level j >= 1 with double block
D := B^j(c_-) ∪ B^j(c_+), and E the fine bonds with both end-points in D. Let U = (e^{i eta B})^u on
E, with u a G-valued gauge on D and eps := l_j max_E |B| <= e_R. Then:
(i) every logarithm in Q_j(U)_c and in Q'_j(U) at the site rows whose blocks lie in D has its
argument within 1/2 of 1; these rows are holomorphic in B and read U only on E (on the bonds
inside B^j(y) for the site row y);
(ii) Q_j(U^g) = Ad_{g} Q_j(U) Ad_g^{-1} and Q'_j(U^g) = Ad_g Q'_j(U) Ad_g^{-1} for every G-valued g,
with Ad_g acting on a fine bond component and on a field row at its initial point (c_- for the
row c), and on a site or a site row at that site;
(iii) Q_j(1)A_c = L^{-5j} sum_{x in B^j(c_-)} sum_{t=0}^{L^j - 1} A_mu(x + t eta e_mu), which is
`flat-port.md` (2.1) with P_- = B^j(c_-), and (Q'_j(1)lambda)(y) = L^{-4j} sum_{x in B^j(y)} lambda(x);
(iv) for u = 1: sum_{b'} |Q_j(U)(c,b') - Q_j(1)(c,b')| <= C_R eps, and
sum_x |Q'_j(U)(y,x) - Q'_j(1)(y,x)| <= C_R eps; and if the same holds for every row of a set 𝒮
of level-j field rows (resp. site rows) with one B on the union of their read sets, then for every
fine bond b' (resp. site x) the sums over c in 𝒮 (resp. y in 𝒮) of the same differences are at
most C_R eps (eta/l_j)^4.
Entries are linear maps of 𝔤^c, normed by the trace norm |X|_2 = (tr X*X)^{1/2}.

*Proof.* (ii) and the reduction to u = 1. Lemma 4.2 (iii) with unitary g, and induction on m,
give (Ū^m(U^g)) = (Ū^m(U))^{g|} and 𝓡^m(U^g; Ad_g V_1) = Ad_{g|} 𝓡^m(U; V_1), with g| the
restriction to T^{(m)}. Differentiation gives (ii) for Q_j. Each factor of the contour variable
is a contour product of Ū^m between consecutive points x_{m+1}, x_m, so
U^g(Gamma^{(j)}_{y,x}) = g(y) U(Gamma^{(j)}_{y,x}) g(x)^{-1}, which gives (ii) for Q'_j. Unitary
conjugation keeps the distance of each logarithm's argument to 1, so (i) at U follows from (i) at
e^{i eta B}. From now on u = 1.

*Units and bootstrap.* Take l_j = 1, so level m has spacing s_m := L^{m-j}. Put b_0 := eta B (the
fine angles), so |b_0| <= eps s_0. For 0 <= m < j define, on the level-(m+1) bonds and sites in D,
  b_{m+1} := F(b_m),  z_m := z_{e^{i b_m}},  t_0 := 1,  t_{m+1} := t_m z_m  (t_m(y) = z_0(y)...z_{m-1}(y)).
Let C_F := 4/(L r_1^2) and P_m := prod_{i<m}(1 + C_F eps s_i). Require
  (e1) e_R <= r_1/3,  (e2) C_F e_R <= (L - 1) log(3/2),  (e3) e_R <= r_1 (L - 1)/30.
Claim: for 0 <= m <= j, (A_m) |b_m| <= eps s_m P_m and P_m <= 3/2; (B_m) |t_m^{±1} - 1| <=
3 eps/(r_1 (L - 1)) <= 1/10; (C_m) Ū^m = (e^{i b_m})^{t_m} on the level-m bonds in D.
For m = 0 all three hold. Assume them at m. Then |b_m| <= (3/2) e_R <= r_1/2, so Lemma 4.2 (iv),
(v) give |b_{m+1}| <= |S b_m| + 2|b_m|^2/r_1^2 <= L|b_m|(1 + 2|b_m|/(L r_1^2)) <= L eps s_m P_m
(1 + C_F eps s_m) = eps s_{m+1} P_{m+1}, and P_{m+1} <= exp(C_F eps sum_i s_i) <= exp(C_F eps/(L-1))
<= 3/2 by (e2). Next |z_i^{±1} - 1| <= |b_i|/r_1 <= (3/2) eps s_i / r_1, so by Lemma 4.1 (iii)
|t_{m+1}^{±1} - 1| <= exp((3/2)(eps/r_1) sum_i s_i) - 1 <= exp(3 eps/(2 r_1 (L-1))) - 1 <=
3 eps/(r_1 (L - 1)) <= 1/10, by (e3) and Lemma 4.1 (i). Finally, by Lemma 4.2 (iii) with g = t_m
(complex, |t_m^{±1} - 1| <= 1/10) and the definition of F,
  Ū^{m+1} = 𝒜((e^{i b_m})^{t_m}) = (𝒜(e^{i b_m}))^{t_m} = ((e^{i b_{m+1}})^{z_m})^{t_m} = (e^{i b_{m+1}})^{t_{m+1}},
using 𝒜(e^{ib})_c = z(c_-) e^{iF(b)_c} z(c_+)^{-1} and (W^z)^t = W^{tz}. This proves the claim. All
logarithms met are those of Lemma 4.2 (i) at |b_m| < r_1, conjugated by t_m; so (i) holds.

*Field rows (iv).* By Lemma 4.2 (iii), Q^ang((e^{ib})^t) = Ad_{t} Q^ang(e^{ib}) Ad_t^{-1}, where
the left Ad_t acts at the sites of the coarser level and the right one at those of the finer.
At level-m sites t_m^{-1} t_{m-1} = z_{m-1}^{-1}. So
  L^j Q_j(U) = Ad_{t_{j-1}} A_{j-1} ... A_0,   A_m := Q^ang(e^{i b_m}) Ad_{z_{m-1}^{-1}}  (A_0 := Q^ang(e^{i b_0})),
where Ad_{z_{m-1}^{-1}} acts on level-m fields; while L^j Q_j(1) = S ... S (j factors). Let ||.||_row (||.||_col) be the largest row (column) sum
of entry norms. By Lemma 4.2 (iv), (v) and |Ad_z - 1| <= C_N(|z - 1| + |z^{-1} - 1|),
  ||A_m - S||_row <= C_1 L eps s_m,   ||A_m - S||_col <= C_1 L^{-3} eps s_m,
with C_1 depending on N and L (it contains 8L^4 · 3/r_1^2 and C_N/(L r_1)). Row norms are
submultiplicative (sum the last index first), column norms too (sum the first index first). For
any matrices, prod A - prod S = sum_q A_{j-1}...A_{q+1}(A_q - S)S^q. Hence, if also
(e4) C_1 e_R <= (L - 1) log(3/2),
  ||prod A - S^j||_row <= sum_q (3/2) L^{j-q-1} · C_1 L eps s_q · L^q <= (3/2) C_1 eps L^j/(L - 1),
and the same with L^{-3j} for columns. The factor Ad_{t_{j-1}} adds at most
C_N (6 eps/(r_1(L-1))) (3/2) L^j. Multiplying by L^{-j}: the row sum of Q_j(U) - Q_j(1) is at
most C_R eps, and the column sum at most C_R eps L^{-4j} = C_R eps (eta/l_j)^4. The column
statement is the same computation on the union of the read sets of 𝒮, where the bootstrap holds
with the same eps. (iii) is the case B = 0: the composition of one-step straight means is the
long straight mean, because B^{m+1}(y) is the union of the level-m blocks B^m(y'') of the points
y'' of B(y), B^m(y'' + t' l_m e_mu) = B^m(y'') + t' l_m e_mu, and t' L^m + t, with 0 <= t' < L and
0 <= t < L^m, runs once through 0, ..., L^{m+1} - 1.

*Site rows (iv).* With W_m := e^{i b_m}(Gamma_{x_{m+1},x_m}) and (C_m), the middle factors of the
contour variable telescope, t_m(x_m)^{-1} t_{m-1}(x_m) = z_{m-1}(x_m)^{-1}:
  U(Gamma^{(j)}_{y,x}) = t_{j-1}(y) W_{j-1} z_{j-2}(x_{j-1})^{-1} W_{j-2} ... z_0(x_1)^{-1} W_0.
Each W_m is a product of at most 4L factors, |W_m - 1| <= 8L|b_m| <= 12 L eps s_m, so by
Lemma 4.1 (iii) |U(Gamma^{(j)}_{y,x}) - 1| <= C eps, and |R(X) - 1| <= C_N|X - 1| for
|X - 1| <= 1/2. The weights L^{-4j} sum to 1 over a block, and each site lies in one block of
level j: this gives the row and column sums. Enlarge C_R to cover both cases, and let e_R be the
largest number satisfying (e1)-(e4) and the analogous smallness for the site rows. ∎

### 4.4 The flat input and the corner blocks

**Lemma 4.5 (corner and centred blocks).** For odd L, the translation tau(x) := x - ((L^k - 1)/2)
eta (1,1,1,1) maps every corner block B^j(y), 0 <= j <= k, onto the centred block of side l_j about
y' := y - l_j ((L^{k-j} - 1)/2)(1,1,1,1), and T^{(j)} onto itself.

*Proof.* (L^k - 1)/2 = L^j (L^{k-j} - 1)/2 + (L^j - 1)/2, and (L^{k-j} - 1)/2 is an integer since
L^{k-j} is odd. So tau(y + eta{0,...,L^j - 1}^4) = y' + eta{-(L^j-1)/2, ..., (L^j-1)/2}^4. ∎

**[F]** (`library/flat-port.md` (8.10), §9.2, §12; checked by Claude, first failing step none,
`gates/flat-port-gate.md:8`). There is B_F >= 1, depending on L, such that on every admitted
geometry the flat systems M_r(1), r in {1, 3, 4, 5}, are invertible with
||M_r(1)^{-1}||_{Y -> X} <= B_F. Also the flat Schur complement is positive, flat-port (8.12). An
**admitted** geometry is a nested family Omega'_0 ⊃ ... ⊃ Omega'_k (some possibly empty), Omega'_n
a union of level-n blocks of side M_F l_n of a nested block grid, l_n^{-1} dist((Omega'_n)^c,
Omega'_{n+1}) >= rho_F, the conventions of §2, Dirichlet conditions outside Omega'_0.

By Lemma 4.4 (iii) the literal flat rows are flat-port's straight averages (2.1) and block means
on Balaban's corner family. flat-port fixes no origin for its grids (its (2.1) names only the
block P_- of a row), and every norm, pairing and flat operator in [F] is covariant under
translations of T_eta. So [F] holds on the corner family; if flat-port is read with centred
blocks, Lemma 4.5 carries it to the corner family with the same constants. Sources: flat-port.md
:586 for M_4; :588 for M_3 and M_1; :666 for M_5; :816-818 for uniformity in depth, mesh, volume
and the shape of the layers. The constants C_88 and c_h are those of flat-port (8.8), (8.6); B_F,
C_88 and c_h are taken to cover all four systems, including the K blocks of §9.2 (pi-gate §4.1).

## 5. Local models

### 5.1 Comparison of all blocks

On an admitted geometry with local scale m (note m <= l_k = 1), let B be a 𝔤^c-valued bond field on
the read set of its systems, and e(B) := max (m|B| + m^2|∂B|), with ∂ the flat forward differences.

**Lemma 5.1.** There are e_C > 0 and C_C, depending on N and L, such that if e(B) <= e_C:
(i) every coefficient of M_r(e^{i eta B}), r in {1,3,4,5}, is defined and holomorphic in B;
(ii) ||M_r(e^{i eta B}) - M_r(1)||_{X^0 -> Y^0} <= C_C e(B), where X^0, Y^0 are the norms of §3.2 with
flat differences;
(iii) for every 𝔤-valued A' with e(A') <= e_C, the norms with differences covariant at e^{i eta A'}
lie between (1 + C_C e(A'))^{-1} and (1 + C_C e(A')) times the flat ones.

*Proof.* *Rows.* A field row of level j >= 1 reads its double block, which lies in the layers
j - 1 and j, where m >= l_j/L. So l_j max|B| <= L e(B), and Lemma 4.4 applies with eps = L e(B)
when L e_C <= e_R. Let T := Q(U) - Q(1) on the rows of level j. By Cauchy-Schwarz with the weights
|T(c,b')|, then Lemma 4.4 (iv),
  ||K(U)v - K(1)v||_count^2 = sum_c l_j^2 |(Tv)_c|_2^2 <= l_j^2 ||T||_row sum_{b'} (sum_c |T(c,b')|) |v_{b'}|_2^2
     <= (C_R L e)^2 l_j^2 (eta/l_j)^4 sum_{b'} |v_{b'}|_2^2 <= (C_R L e)^2 ||m^{-1} v||_2^2,
using eta^4 l_j^{-2} <= eta^4 m(b')^{-2} on the double block. A fine bond is read by rows of at
most two levels (its own layer's and the next outward ones), which costs a factor 2. Site rows
of level j have their blocks in layer j, where m = l_j; the same computation gives
||m^{-2}(Q'(U) - Q'(1))lambda||_top <= C_R L e ||m^{-2}lambda||_2. The mass blocks are
K(U)^T K(U) - K(1)^T K(1) = (K(U) - K(1))^T K(U) + K(1)^T (K(U) - K(1)), and the same for
Q'^T m^{-2} Q'; one factor is bounded as above, the other by the flat counts of flat-port §3
(||K(1)v||_count <= C ||m^{-1}v||_2, by Jensen), and transposes have the same bounds by duality.
Rows of level 0 are identities and do not vary.

*Differences.* (D_U - D_1)lambda(b) = c_b lambda(b_+) with c_b := eta^{-1}(Ad e^{i eta B_b} - 1).
Since X ↦ Ad e^{iX} - 1 vanishes at 0 and has bounded derivative on |X| <= 1, |c_b| <= C|B_b| <=
C e/m and |∂c| <= C|∂B| <= C e/m^2. The product rule then gives
||(D_U^T D_U - D_1^T D_1)lambda||_2 <= C e (||m^{-2}lambda||_2 + ||m^{-1} D lambda||_2) (note
||m^{-1}lambda|| <= ||m^{-2}lambda|| as m <= 1), |<v, (D_U D_U^T - D_1 D_1^T)w>| <= C e ||v||_E ||w||_E,
and the same bound for the blocks -D_U, -D_U^T between h and A.

*Wilson Hessian.* Fix a plaquette p with holonomy P := U(∂p) from its base point. For a field v let
v'_1, ..., v'_4 be its values on the four bonds of ∂p, each transported to the base point along
∂p and signed by orientation, and X_v := sum_k v'_k. Expanding tr(2 - W - W^{-1})/2 with
W = E(s)P and E(s) the ordered product of the e^{i s eta v'_k} gives, for the second variation,
  Psi_p(v, w) = (eta^2/2) tr(X_v X_w (P + P^{-1})) + (eta^2/4) tr(sum_{k<l} ([v'_k, w'_l] + [w'_k, v'_l])(P - P^{-1})),
which is CMP 99b (3.10) per plaquette, and is eta^2 tr(X^1_v X^1_w) = eta^4 tr((dv)(p)(dw)(p)) at
U = 1, X^1 being the untransported sum. Write P + P^{-1} = 2 + (P - 1)^2 P^{-1}. Since U = e^{i eta B},
|P - 1| <= C eta^2 (|∂B| + |B|^2) <= C eta^2 e/m^2. So the remainder per plaquette is at most
C |P - 1| eta^2 |v||w| <= C e eta^4 m^{-2} |v||w| (this is pi-gate §4.2's corrected normalisation:
the raw remainder carries eta^2, not eta^4). The transports differ from 1 by at most C eta e/m,
so |X_v - X^1_v| <= C eta e m^{-1}|v| and |X^1_v| = eta|(dv)(p)|. Summing over plaquettes, each bond
lying in six, |<v, (Delta(U) - Delta(1)) w>| <= C e ||v||_E ||w||_E, the curvature term included.
At the Dirichlet edge zero extensions are used; the plaquettes that leave Omega_0 read U on
Omega_0^+, where B is defined.

Adding the finitely many blocks gives (ii). (iii) is the bound |(∇_{e^{i eta A'}} - ∂)f| <=
C|A'||f|, and its second-order analogue with |∂A'|, for each covariant difference in the norm.
(i): the rows are holomorphic by Lemma 4.4 (i); the other coefficients are polynomials in the
entries of e^{±i eta B}. ∎

### 5.2 Tiles, cutoffs, footprints and models

**Tiles.** For each level j, the layer Omega_j \ Omega_{j+1} is a union of cubes of the level-j
tile grid (side M_t l_j, corners in M_t l_j Z^4), because Omega_j and Omega_{j+1} are unions of big
blocks of sides M_b l_j and M_b l_{j+1} and M_t divides M_b. These cubes are the tiles of level j.
**Exterior tiles** (pi-gate §4.3): if Omega_0 ≠ T_eta, the cubes of the level-0 tile grid that are
disjoint from Omega_0 and contain the initial point b_- of a field bond b (then b_+ is in Omega_0).
For such a tile take the first such bond in a fixed order (lexicographic in b_-, then in the
direction) and put z_tau := b_+, a site of Omega_0 with
|z_tau - x_tau|_inf <= (M_t - 1)eta/2 + eta. The level of an exterior tile is 0, as is the
extended level of its sites. Since M_t L^j is odd, the centre x_tau of a tile is a site.

**Cutoffs.** Fix phi: R^4 -> [0,1] smooth, equal to 1 on [-1/2, 1/2]^4 and supported in [-1,1]^4.
Put b_tau(x) := phi((x - x_tau)/(M_t l_{j_tau})) and h_tau := b_tau / (sum_sigma b_sigma^2)^{1/2}. A
bond component uses the value at its initial point, a site component at its site, a row at its
base point. Every reference point lies in a tile (exterior tiles cover the outer initial points),
where its own bump is 1; so the denominator is >= 1 and sum_tau h_tau^2 = 1 on every component.
Bumps that overlap have levels differing by at most one: if j_sigma >= j_tau + 2, then sigma ⊂
Omega_{j_sigma} and tau ⊄ Omega_{j_sigma - 1}, so by (T) the tiles are more than R M_b l_{j_sigma - 1} >=
M_t l_{j_sigma} apart, while the supports reach at most M_t(l_{j_sigma} + l_{j_tau})/2 beyond them.
Hence the h_tau obey flat-port (8.6) with M = M_t and constants depending on L.

**Footprints and two levels.** F_tau is the closed l^inf cube of half-width r^ l_{j_tau} about x_tau,
and F^+_tau the one of half-width (r^ + L) l_{j_tau}. F^+_tau meets at most two levels {i, i+1}, and
j_tau is i or i+1. Indeed points of F^+_tau are within Euclidean distance 2(r^ + L) l_{j_tau} of
x_tau. A site of level <= j_tau - 2 lies outside Omega_{j_tau - 1}, at distance > R M_b l_{j_tau}/L >
2(r^ + L) l_{j_tau} from x_tau in Omega_{j_tau}, by (T) and the floor R_1 M_b >= 4L(r^ + L) + 1. A site
of level >= j_tau + 2 lies in Omega_{j_tau + 2}, at distance > R M_b l_{j_tau + 1} from x_tau, which is
outside Omega_{j_tau + 1}. Sites of levels j_tau - 1 and j_tau + 1 are more than R M_b l_{j_tau} >
4(r^ + L) l_{j_tau} apart, more than the diameter. For exterior tiles x_tau is outside Omega_0, and
the same argument excludes the levels >= 2.

**Models** (r1 §4.3, ADVANCE in pi-gate §4.3, with the exterior repair). N_tau := the l^inf box of
half-width r_N l_{j_tau} about x_tau (inside F_tau). Let i = i_tau be the least level met by N_tau.
C_tau is the smallest cube aligned with the grid of spacing M_F l_{i+1} that contains the box of
half-width 4 M_t l_{j_tau} about x_tau; rounding adds at most M_F l_{i+1} <= M_t l_{j_tau}. Put
K_n := C_tau for n >= i + 1, and for n <= i let K_n be C_tau enlarged on each side by
sum_{p=n}^{i} rho'_F l_p <= 2 rho'_F l_{j_tau} <= M_t l_{j_tau}. So K_n ⊂ the box of half-width
6 M_t l_{j_tau}. The model geometry 𝒢_tau is Omega^tau_n := Omega_n ∩ K_n, with Dirichlet conditions
outside Omega^tau_0. It is admitted: the sets are nested unions of level-n blocks of side M_F l_n,
and dist((Omega^tau_n)^c, Omega^tau_{n+1}) >= min{dist(Omega_n^c, Omega_{n+1}), dist(K_n^c, K_{n+1})} >=
min{R M_b, rho'_F} l_n >= rho_F l_n for n <= i, while Omega^tau_n = ∅ for n >= i + 2. For an exterior
tile the model is bare. M_{r,tau}(U) are the systems of §3.1 on 𝒢_tau, with the literal rows of the
model. Their **read set** X_tau consists of the bonds read by their coefficients: the field bonds
of the model, the bonds of the plaquettes through them (within 2 eta of K_0), and the double
blocks of the model rows (rows of level <= i + 1 touching K_n, so within 2 l_{i+1} <= 2L l_{j_tau}
of K_n). Hence X_tau ⊂ the box of half-width (6 M_t + 2L + 1) l_{j_tau}, which lies in N_tau since
M_t >= 4L. For an exterior tile, X_tau ⊂ the box of half-width 6 M_t eta + 2 eta about x_tau,
which lies in N(z_tau) since 6 M_t + 2 + M_t/2 + 1 <= 7 M_t.

**Agreement.** On C_tau the model level of every site equals its actual level. So every coefficient
whose stencil or row read set lies in A_tau := the box of half-width 3 M_t l_{j_tau} about x_tau is
the same function of U in the model and in the actual system: a row's membership depends on the
levels of its end-points, its value on its double block. The support of h_tau lies in the box of
half-width M_t l_{j_tau}, and every stencil and row read set meeting it lies in the box of
half-width (M_t + 2L) l_{j_tau} ⊂ A_tau.

**Diameter.** Any two tops p, p' (of the tower with Omega_0 replaced by T_eta) in F_tau satisfy
d(p, p') <= D_X = 24 L^2 M_t. Proof: by the two-level property only the layers i, i+1 occur in
F^+_tau. If p has level i, the level-(i+1) block containing p is a union of level-i blocks disjoint
from Omega_{i+1}, hence in layer i; go from p to its corner p_1 along the axial contour with bonds
of T^{(i)}: at most 4(L - 1) bonds, cost at most 4(L - 1). If p has level i + 1, put p_1 = p. Do
the same for p'. Join p_1 to p'_1 by a coordinate staircase of bonds of T^{(i+1)}. Each such bond
lies, except for one end-point, in one block of level i + 1, hence in one layer; in layer i + 1 it
is a bond of that layer's lattice, in layer i it is a union of L bonds of T^{(i)}. So the staircase
is admissible for (2.46), stays in F^+_tau, and costs at most l_i^{-1} times its length, which is
at most 4(2 r^ l_{j_tau} + l_{i+1}) <= 4L(2 r^ + 1) l_i. In total d(p,p') <= 8(L - 1) + 4L(2r^ + 1)
<= 16 L(L + 1) M_t + 12L <= 24 L^2 M_t for L >= 3 and M_t >= 2.

**Overlap.** If N_sigma meets N_tau then |j_sigma - j_tau| <= 1, by the argument above. The centres
are then within l^inf distance 7 M_t (l_{j_sigma} + l_{j_tau}) of each other. Counting the grid
points per coordinate gives at most 29 for j_sigma = j_tau, at most 15 + 14/L for j_sigma =
j_tau + 1, and at most 14 L + 15 for j_sigma = j_tau - 1 (pi-gate §4.3); each is <= 20 L. So at
most D_* = 3 (20 L)^4 tiles sigma have N_sigma ∩ N_tau ≠ ∅, and each point lies in at most D_* of
the boxes N_tau. Consecutive footprints of a walk meet in a set that contains a top: their
centres are within l^inf distance 7 M_t(l_{j_sigma} + l_{j_tau}), so F_sigma ∩ F_tau contains a cube
of side (2L + 2 - 7) M_t (l_{j_sigma} + l_{j_tau}) >= M_t l_i >= l_{i+1} (L >= 3, M_t >= L). That
cube contains a point of T^{(i+1)}, which is a top of level i or i + 1.

### 5.3 Local inverses

**Lemma 5.2 (the gauge estimate).** Assume (S1-loc), (S2), (S2+) with L^2 a_0, a_1 <= 1/8. For a
tile tau let z := x_tau (z := z_tau for an exterior tile) and u the gauge of (S1-loc) on N(z),
U_r^u = e^{i eta A}. Then U^u = e^{i eta B} on X_tau with B := (i eta)^{-1} log(e^{i eta 𝔞^u} e^{i eta A}),
𝔞^u(b) := Ad u(b_-) 𝔞(b), and, with the model scale m,

  (5.4)   e(B) <= C_S (L^2 a_0 + a_1),   e(A) <= 2 L^2 a_0.

*Proof.* U^u_b = u(b_-) e^{i eta 𝔞_b} U_{r,b} u(b_+)^{-1} = e^{i eta 𝔞^u_b} U^u_{r,b}. The model scale never
exceeds the actual (extended) scale: they agree on C_tau, the model level is lower on the collar,
and both are eta outside Omega_0. So (S1-loc) gives m|A| <= L^2 a_0, m^2|∂A| <= L^2 a_0. (S2), (S2+)
give m|𝔞^u| < a_1 and m^2 |∇_{e^{i eta A}} 𝔞^u| = m^2 |(∇_{U_r} 𝔞)^u| < a_1, by covariance of the
covariant difference; and |∂𝔞^u| <= |∇_{e^{i eta A}} 𝔞^u| + C|A||𝔞^u|. Let rho(X,Y) := log(e^X e^Y) - X - Y on
|X|, |Y| <= 1/8. It is holomorphic, vanishes when X = 0 or Y = 0, so by Lemma 4.1 (iv) applied to
its partial derivatives |rho(X,Y)| <= C|X||Y| and |rho(X',Y') - rho(X,Y)| <= C(|X' - X||Y'| + |X||Y' - Y|).
With X = i eta 𝔞^u and Y = i eta A: |B| <= |𝔞^u| + |A| + C eta|𝔞^u||A| and |∂B| <= |∂𝔞^u| + |∂A| +
C eta(|∂𝔞^u||A| + |𝔞^u||∂A|). Multiply by m and m^2 and use eta <= m. ∎

**Lemma 5.3 (local inverses).** Assume (S1-loc) with a_0 <= a_0^*, and (S2), (S2+) with a_1 <= a_1^*.
For every tile tau (exterior tiles included) and r in {1,3,4,5}, M_{r,tau}(U) is invertible and
||M_{r,tau}(U)^{-1}||_{Y_tau -> X_tau} <= 3 B_F. Its entries are holomorphic in 𝔞 and depend only on U
restricted to X_tau and on 𝒢_tau, hence on the tower inside N_tau.

*Proof.* Take z and u as in Lemma 5.2; for an exterior tile the gauge sits at z_tau, not at the
exterior centre (pi-gate §4.3). Let 𝒰 act by Ad u on each bond component and field row at its
initial point and on each site and site row at that site. D_U, D_U^T and Delta(U) are covariant
by their finite formulas (CMP 99b (3.31)-(3.34)); the rows by Lemma 4.4 (ii). So
M_{r,tau}(U^u) = 𝒰 M_{r,tau}(U) 𝒰^{-1}, and 𝒰 maps the norm covariant at U_r onto the norm covariant
at e^{i eta A}. By (5.4) and §3.3 item 7, e(B) <= e_L <= e_C. By [F], ||M_{r,tau}(1)^{-1}|| <= B_F on
the admitted 𝒢_tau. By Lemma 5.1 (ii), ||M_{r,tau}(e^{i eta B}) - M_{r,tau}(1)|| <= C_C e_L <= 1/(8 B_F),
and the Neumann series for [I + M(1)^{-1}(M(U) - M(1))]^{-1} M(1)^{-1} gives invertibility with flat
bound (8/7) B_F. By Lemma 5.1 (iii) with e(A) <= e_L and C_C e_L <= 1/8, the covariant norms are
within the factor 9/8 of the flat ones, so the bound is at most (9/8)^2 (8/7) B_F < 3 B_F.
Conjugating back by 𝒰 changes nothing. The entries are holomorphic in 𝔞 by Lemma 5.1 (i), and the
determinant does not vanish; Cramer's rule gives holomorphic entries of the inverse. ∎

## 6. Assembly and patch words

Throughout U is as in Lemma 5.3 and r in {1,3,4,5} is fixed; r is dropped. A field supported in
A_tau is identified with a model field and back ("transplant"); by Agreement both norms coincide
there. Lemmas 6.1-6.3 are r1's Lemmas 5.1-5.3, checked ADVANCE in pi-gate §5, with the tower
locality moved to §9.

**Lemma 6.1 (commutators).** For every tile tau and every Y in the model space, [M_tau(U), h_tau]Y
is supported in A_tau and depends only on Y on the read closure of supp h_tau; it equals
[M(U), h_tau]Y~ for every global Y~ that agrees with Y on A_tau; and
||[M_tau(U), h_tau] Y||_{Y_tau} <= (C_K / M_t) ||Y||_{X_tau}, with C_K = 3 C_88.

*Proof.* [M_tau, h_tau]Y = M_tau(h_tau Y) - h_tau M_tau Y reads Y only near supp h_tau, and its output
lies in the read closure of supp h_tau; the rest is Agreement. For the bound conjugate by 𝒰 as in
Lemma 5.3; h_tau is scalar and evaluated at the same reference points, so it commutes with 𝒰. Then
[M_tau(U^u), h] = [M_tau(1), h] + [V, h] with V := M_tau(e^{i eta B}) - M_tau(1). flat-port (8.8)
(flat-port.md:571; h obeys (8.6) with M = M_t) gives ||[M_tau(1), h]Y|| <= (C_88/M_t)||Y|| in the flat
norms. By Lemma 5.1 (ii), ||[V, h]Y|| <= ||V(hY)|| + ||hVY|| <= 2 c_h C_C e_L ||Y|| <= (C_88/M_t)||Y||,
by the choice of e_L. Passing between flat and covariant norms costs at most (9/8)^2. So the
constant is at most (81/64) 2 C_88 < 3 C_88. ∎

**Lemma 6.2 (parametrix).** Put S_tau := h_tau M_tau(U)^{-1} h_tau and T_tau := [M_tau(U), h_tau]
M_tau(U)^{-1} h_tau (model operators, transplanted: the first h_tau cuts a global source into A_tau,
and the outputs lie in A_tau), Par := sum_tau S_tau and Res := sum_tau T_tau. Then

  M(U) Par = I + Res,   ||S_tau||_{Y -> X} <= 3 B_F c_h^2,   ||T_tau||_{Y -> Y} <= theta,
  ||Res||_{Y -> Y} <= D_* theta <= 1/2,

so M(U) is invertible and M(U)^{-1} = Par sum_{n >= 0} (-Res)^n, converging in norm.

*Proof.* Identity: for a source F let Z := M_tau^{-1} h_tau F. Then h_tau Z is supported in
supp h_tau, so M(h_tau Z) = M_tau(h_tau Z) = h_tau M_tau Z + [M_tau, h_tau]Z = h_tau^2 F + T_tau F. Sum over
tau and use sum h_tau^2 = 1. Bounds: cutoff multiplication is bounded by c_h on X and Y, and
Lemma 5.3 bounds the local inverse by 3 B_F; this bounds S_tau. For T_tau pair with a test field
Y' in the dual of Y. Since [M_tau, h_tau]Z is supported in A_tau, <T_tau F, Y'> = <[M_tau, h_tau]Z,
chi_tau Y'>, where chi_tau is a cutoff obeying flat-port (8.6), equal to 1 on the read closure of
supp h_tau and supported in A_tau. By Lemmas 6.1 and 5.3, |<T_tau F, Y'>| <= (C_K/M_t) 3 B_F
||h_tau F|| ||chi_tau Y'|| <= theta ||F|| ||Y'||. For Res use the same pairing and Cauchy-Schwarz over tau,
with sum_tau ||chi_tau Y'||^2 <= c_h^2 D_* ||Y'||^2 (the squared norm is a sum of local terms and a
point lies in at most D_* of the sets A_tau) and sum_tau ||h_tau F||^2 <= c_h^2 D_* ||F||^2 (choose Z_tau
with ||Z_tau|| = t_tau := ||h_tau F|| and <F, h_tau Z_tau> = t_tau^2; then sum t_tau^2 = <F, sum h_tau Z_tau>
<= ||F|| c_h D_*^{1/2} (sum t_tau^2)^{1/2}). So ||Res|| <= D_* theta <= D_* (4 D_*)^{-4} <= 1/2. Then
(I + Res) sum (-Res)^n = I, so Par sum (-Res)^n is a right inverse of the finite square matrix M,
hence its inverse. No sharp multiplier on H^2 is used. ∎

**Lemma 6.3 (patch words).** For a sequence omega = (tau_0, ..., tau_n) of tiles put
W_omega := S_{tau_0} (-T_{tau_1}) ... (-T_{tau_n}). Then:
(i) M(U)^{-1} = sum_omega W_omega; for each n the sum over sequences of length n is finite and
equals Par (-Res)^n;
(ii) W_omega = 0 unless supp h_{tau_{m-1}} meets the read closure of supp h_{tau_m} for every m; in
particular N_{tau_{m-1}} ∩ N_{tau_m} ≠ ∅, so only walks contribute;
(iii) ||W_omega||_{Y -> X} <= 3 B_F c_h^2 theta^n;
(iv) W_omega F is supported in supp h_{tau_0} and depends on F only on supp h_{tau_n};
(v) every entry of W_omega is holomorphic in 𝔞 and depends only on U on X(omega), on the model
geometries 𝒢_{tau_m} and on the cutoffs h_{tau_m}.

*Proof.* (i) Expand the finite sums. (ii) The rightmost factor h_{tau_{m-1}} of T_{tau_{m-1}} (or of
S_{tau_0}) multiplies the output of [M_{tau_m}, h_{tau_m}], which lies in the read closure of
supp h_{tau_m}; both sets lie in the boxes N. (iii) Product of the bounds of Lemma 6.2. (iv) The
leftmost and rightmost cutoffs. (v) Each factor is built from M_tau(U)^{-1} (Lemma 5.3), the
coefficients of M_tau near supp h_tau (which read X_tau) and h_tau. ∎

*Remark (by-products, not used).* The same words for r = 4 give G_0 = [M_4^{-1}]_{AA} as a sum of
local words in the energy norms of flat-port (8.3); for r = 3 they give P and (Q'G'^2Q'^T)^{-1}.
These are energy-norm statements, not Balaban's pointwise and Hölder bounds (3.42)-(3.47) for G_0.

## 7. The Schur chain and the identification (proof of part (a))

**Lemma 7.1 (Schur chain; `b109.md` P1 and flat-port (8.2), (8.4), (9.2), reproved; ADVANCE in
pi-gate §6).** Let U be a configuration at which A_s, M_3, M_4 and M_5 are invertible, and put
G' := A_s^{-1}. Then
(i) Q'G'^2Q'^T is invertible and [M_3^{-1}]_{hh} = P;
(ii) T := B_v - D_U P D_U^T = Delta(U) + D_U R D_U^T + Q^T a Q = Delta_a is invertible and
T^{-1} = [M_4^{-1}]_{AA};
(iii) Gamma := K T^{-1} K^T is invertible and Gamma^{-1} = -[M_5^{-1}]_{nu nu};
(iv) Q G_0 Q^T = m^{-1} Gamma m^3 and q_0 = m^{-3} Gamma^{-1} m = -m^{-3} [M_5^{-1}]_{nu nu} m.

*Proof.* We use one fact: if M = [[X11, X12], [X21, W]] with W invertible, then M = [[I, X12 W^{-1}],
[0, I]] [[S, 0], [0, W]] [[I, 0], [W^{-1} X21, I]] with S := X11 - X12 W^{-1} X21; the outer factors are
invertible, so M is invertible if and only if S is, and then (M^{-1})_{11} = S^{-1}.
(i) For M_3 (unknowns h, lambda, mu) the source (g, 0, 0) gives h + A_s lambda = g, A_s h - Q'^T mu = 0,
Q' lambda = 0. If Q'G'^2Q'^T mu_0 = 0 with mu_0 ≠ 0, then (G'Q'^T mu_0, -G'^2 Q'^T mu_0, mu_0) is a
nonzero solution with g = 0, which is impossible. So Q'G'^2Q'^T is invertible. Then h = G'Q'^T mu,
lambda = G'(g - h), and Q'G'g = Q'G'^2Q'^T mu give mu = (Q'G'^2Q'^T)^{-1}Q'G'g and h = Pg.
(ii) Apply the fact to M_4 with W = M_3, X11 = B_v, X12 = (-D_U, 0, 0), X21 = X12^T: S = B_v - D_U P D_U^T
by (i), and this equals Delta + D_U(I - P)D_U^T + Q^T a Q.
(iii) Apply it to M_5 with W = M_4, X11 = 0, X12 = (-K, 0, 0, 0), X21 = X12^T: S = -K T^{-1} K^T = -Gamma.
(iv) K = mQ and K^T = Q^T m^{-3} (§3.1) give Gamma = m Q G_0 Q^T m^{-3}. ∎

*Proof of Theorem PI (a).* Lemma 6.2 gives the invertibility of A_s, M_3, M_4 and M_5, and Lemma 7.1
gives the rest of the formulas. The entries are holomorphic in 𝔞 by Lemma 6.3 (v) and uniform
convergence (Lemma 6.2), or by Cramer's rule since the determinants do not vanish. Symmetry:
Delta(U), D_U R D_U^T and Q^T a Q are symmetric for the bilinear pairing, so G_0^T = G_0 and q_0^T = q_0.

*Identification* (pi-gate §6). Let 𝔞 be 𝔤-valued, so U is G-valued (pi-gate's wording). Every
coefficient of M_5(U) is then Balaban's: D_U and Delta(U) of CMP 99b (3.8), (3.10), and the rows Q,
Q' of CMP 99b (3.13)-(3.19) by Definition 4.3, which is built from CMP 98 (42)-(43), (58)-(63),
(89)-(91) and the contour variables of CMP 98 p.29. So G' is Balaban's (Delta'_a)^{-1} up to the
positive mass, which R does not see (§3.1), and Delta_a, G_0 are CMP 99b (3.26)-(3.27) with the
account's a = l^{-2}. For complex 𝔞 the same finite formulas are Balaban's extension (CMP 99b
p.393). They are holomorphic in 𝔞 on the convex open set where (S2), (S2+) hold with a_1^*, and
any holomorphic continuation from the real points of that set (as the account defines G_0 and q_0,
CA-I 13552-13571) equals them. No step here identifies two different row conventions, and G_0 is
the bare operator, not the corrected G of CMP 99b (3.130). ∎

## 8. The bounds (proof of parts (b), (c), (d))

Let c be a field row of level j and c' one of level j'. By Lemma 7.1 (iv) and Lemma 6.3 (i),

  q_0(c,c') = sum_omega q_omega(c,c'),   q_omega(c,c') := -l_j^{-3} l_{j'}^{-3} (W^{(5)}_omega)_{nu nu}(c,c'),

as a density for the top pairing: (q_0 psi)(c) = sum_{c'} l_{j'}^4 q_0(c,c') psi(c'), and the counting
entry of m^{-3} Gamma^{-1} m is l_j^{-3} Gamma^{-1}(c,c') l_{j'}, which divided by l_{j'}^4 gives
l_j^{-3} l_{j'}^{-3} (ADVANCE in pi-gate §7).

**(SD).** For tops y of level j and y' of level j' with |j - j'| >= 1, d(y,y') >= R M_b (|j - j'| - 1).
Let j' >= j + 2. For each n with j < n < j', a contour from y (outside Omega_n) to y' (in
Omega_{n+1}) leaves Omega_n^c for the last time and then reaches Omega_{n+1}; that stretch lies in
Omega_n \ Omega_{n+1} and, by (T), has length > R M_b l_n, so its cost is > R M_b. The stretches are
disjoint. (The lowest layer of 2.5 is Omega_1^c, so this holds also when y lies outside Omega_0.)

**Each term.** By (E) and Lemma 6.3 (iii), |(W_omega)_{nu nu}(c,c')| <= 3 B_F c_h^2 theta^n, n = |omega|.
By Lemma 6.3 (iv) the entry vanishes unless y_c is in supp h_{tau_0} ⊂ F_{tau_0} and y_{c'} in
supp h_{tau_n} ⊂ F_{tau_n}. Then choose tops y_m in F_{tau_{m-1}} ∩ F_{tau_m} (§5.2, Overlap); each
consecutive pair lies in one footprint, so by Diameter d(omega, y_c, y_{c'}) <= D_X (n + 1), and
d(y_c, y_{c'}) <= d(omega, y_c, y_{c'}) by the triangle inequality. Write l_j^{-3} l_{j'}^{-3} =
l_j^{-2} l_{j'}^{-4} (l_{j'}/l_j). By (SD), l_{j'}/l_j <= L^{|j - j'|} <= L exp((log L/(R M_b))
d(y_c, y_{c'})) <= L exp((delta_q/3) D_X (n + 1)), since R M_b >= 3 log L/delta_q. Finally
theta^n = theta^{-1/2} theta^{n/2} theta^{(n+1)/2} and theta^{(n+1)/2} = exp(-(7/2) delta_q D_X (n + 1)). Hence

  |q_omega(c,c')| <= 3 B_F c_h^2 L theta^{-1/2} l_j^{-2} l_{j'}^{-4} theta^{n/2} e^{-3 delta_q D_X (n+1)},

which is (c), as 3 B_F c_h^2 L theta^{-1/2} <= C_q. Locality and holomorphy are Lemma 6.3 (v); the
walks are those of §3.4 by Lemma 6.3 (ii).

**(d).** From a fixed tile there are at most D_*^n walks of length n (Lemma 6.3 (ii) and Overlap),
and D_* theta^{1/4} <= D_* (4 D_*)^{-1} = 1/4 by §3.3 item 3. So sum_{omega from tau} theta^{|omega|/4} <=
sum_n 4^{-n} = 4/3, and the same for walks ending at tau; the other factor theta^{|omega|/4} <=
(4D_*)^{-|omega|} is spare. For Lambda <= D_X(n+1), since d(omega, y_c, y_{c'}) <= D_X(n+1),
e^{-3 delta_q D_X(n+1)} <= e^{-delta_q d(omega, y_c, y_{c'})} e^{-2 delta_q Lambda}. This corrects r1's
part (d) as pi-gate §7 asks: the summation factor is theta^{n/4} under the stronger choice
theta <= (4D_*)^{-4}, and no O(M_b^{-1}) per-step comparison or variable-M_t asymptotics is claimed.

**(b).** At most D_* tiles tau_0 have h_{tau_0}(y_c) ≠ 0. For nonzero terms
e^{-3 delta_q D_X(n+1)} <= e^{-3 delta_q d(y_c, y_{c'})}. Summing the term bound over walks with
theta^{n/2} <= theta^{n/4},

  |q_0(c,c')| <= D_* (4/3) 3 B_F c_h^2 L theta^{-1/2} l_j^{-2} l_{j'}^{-4} e^{-3 delta_q d} <= C_q l_j^{-2} l_{j'}^{-4} e^{-delta_q d(y_c, y_{c'})}.

The series converges absolutely, uniformly in 𝔞. For f supported on the at most 8 rows with base
point y', |(q_0 f)(c)| <= sum_{c'} l_{j'}^4 |q_0(c,c')| |f(c')| <= 8 C_q l_j^{-2} e^{-delta_q d(y_c, y')} sup|f|. So
q_0 is in the class K_{-2} of CA-I 13402-13410 with constant 8 C_q and rate delta_q, once the
kernel algebra's floors (CA-I 13413-13428) are imposed at that rate (pi-gate §7). ∎

## 9. The setting-compatible assignment (part (e); item 4)

**What r1 got wrong.** r1's Theorem PI(c) said that two settings whose towers agree on
N_{tau_0} ∪ ... ∪ N_{tau_n} give the same q_omega. pi-gate §5 refutes this: the denominator of
h_tau reads coarse bumps whose tiles lie outside N_tau. Its example: L = 27, a level-0 tile, a
level-1 half-space starting about 8 M_t eta to its right; the first coarse tile (side 27 M_t eta)
has a bump that reaches 13.5 M_t eta past its face and changes h_tau, while that tile lies
outside N_tau (half-width 7 M_t eta). Compared with the tower with Omega_1 = ∅, at U = 1, the
one-letter word h_tau(y)^2 [M_{5,tau}^{-1}]_{nu nu}(y,y) differs. Locality in U is not affected.

**The assignment.** The index set is the set of walks of tiles of the fixed tile grids (§3.4).
The letters are the factors S_tau and T_tau of Lemma 6.2, built by fixed rules: the bump profile
phi, the model construction of §5.2, and the order that picks z_tau for an exterior tile. The
footprint of a walk is |omega| = F_{tau_0} ∪ ... ∪ F_{tau_n}, with F_tau of half-width
r^ l_{j_tau} = (2L + 2) M_t l_{j_tau}. (pi-gate §5 proposes the half-width (2L + 2) M_t l_{j_tau};
it is used here.) Each F_tau is a closed cube, the closure of its interior, and consecutive
footprints share a cube of positive side (§5.2, Overlap); so |omega| is the closure of an open
set with connected interior, as CA-I 5126-5130 asks of a footprint.

*Proof of (e).* Let s = (tower, U) and s' = (tower', U') satisfy the hypotheses of Theorem PI, let
omega = (tau_0, ..., tau_n) be a walk of s, and let s, s' agree on |omega|.

(1) *Index set.* Whether a cube tau of the level-j tile grid is a tile of level j is decided by
the tower on tau (tau ⊂ Omega_j \ Omega_{j+1}); whether it is an exterior tile is decided by Omega_0
on tau and on the sites at distance eta from it, and z_tau by the same data. These sets lie in
F_tau. The walk condition (the boxes N meet) is geometric. So omega is a walk of s'.

(2) *Cutoffs.* On supp b_tau, h_tau = b_tau (sum_sigma b_sigma^2)^{-1/2}, and only tiles sigma with
supp b_sigma ∩ supp b_tau ≠ ∅ contribute. By §5.2 their levels differ from j_tau by at most one,
so |x_sigma - x_tau|_inf <= M_t(l_{j_sigma} + l_{j_tau}) <= (L + 1) M_t l_{j_tau}, and sigma lies in the
box of half-width (L + 1 + L/2) M_t l_{j_tau} ⊂ F_tau. By (1) applied to these cubes, s and s'
have the same such tiles. So h_tau is the same function (in both settings the level-adjacency
holds because both towers satisfy (T)).

(3) *Models.* i_tau is the least level met by N_tau ⊂ F_tau; C_tau and K_n are fixed by x_tau,
j_tau, i_tau; Omega^tau_n = Omega_n ∩ K_n with K_n ⊂ F_tau. So 𝒢_tau is the same, and M_{r,tau}(U)
reads U only on X_tau ⊂ N_tau ⊂ F_tau, where U = U'. So the local inverses coincide.

(4) *Transplants.* The global components with reference points in A_tau, and the coefficients of
M near supp h_tau, are fixed by the tower and U on A_tau and its read closure, inside F_tau. So
S_tau and T_tau agree as kernels on the components inside F_tau.

Hence W_omega has the same kernel in both settings; it is supported in supp h_{tau_0} x supp h_{tau_n}
by Lemma 6.3 (iv), and q_omega^s = q_omega^{s'}. For a closed W on which s and s' agree, every walk
of s with |omega| ⊂ W is a walk of s' with the same term, and conversely by symmetry: this is the
equality of the restricted sums. The support statement holds because supp h_tau lies in the box
of half-width M_t l_{j_tau} and F_tau has half-width (2L + 2) M_t l_{j_tau}. ∎

**Who needs it.** The ordered word families of CA-I 5293-5470 (steps (e)-(g): "the cubes and
partitions that can occur in omega are the same for s and for s'", "every letter of omega has the
same value", support away from the boundary of the footprint) and (C1) at 5702-5712; and K10 at
CA-I 15266-15490 (the factor prod s(Delta) over the decoupling cubes met by the localisation
domains, and the zero-switch separation). For both, the footprint above is the localisation
domain of a term. The field read X(omega) is not enlarged; only the tower read is.

## 10. Proofs of Propositions 3.1, 3.2 and 3.3

*Proof of Proposition 3.1* (r1's proof, ADVANCE in pi-gate §3.1 on its interior scope). Fix x with
N := N(x) ⊂ Omega_0 and j = lambda(x). Euclidean distances; points of N are within 2 r_N l_j of x.
(1) The levels met by N lie in {i, i+1} for some i in {j-1, j}: a site of level <= j - 2 is outside
Omega_{j-1}, so more than R M_b l_j/L > 2 r_N l_j from x; a site of level >= j + 2 is in Omega_{j+2},
so more than R M_b l_{j+1} from x; sites of levels j - 1 and j + 1 are more than R M_b l_j > 4 r_N l_j
apart (floors of §3.3 item 6). Let i be the least level met by N.
(2) Every site of N has level >= i, so N ⊂ Omega_i. The side of N is 2 r_N l_j <= 2 r_N L l_i <
11 M_b l_i < s_i, so N meets at most two cells of the s_i-grid in each direction; each cell meeting
N meets Omega_i, hence lies in Omega_i, and their union is a box containing N. In each coordinate,
round the left end beta of the projection of N down to the grid of spacing M_b l_i (this adds less
than M_b l_i; the projection has length at most (11 M_b - 1) l_i), and take the aligned interval of
length 12 M_b l_i from there; if it passes the right end of the cell box, take instead the aligned
interval of length 12 M_b l_i that ends there, which still starts at or before beta and not before
the box's left end. The product Q is a cube of side 12 M_b l_i, a union of level-i big blocks, with
N ⊂ Q ⊂ Omega_i.
(3) Q contains a site of level i, which is outside Omega_{i+1} and so more than R M_b l_{i+1} >=
24 M_b l_i (R >= 24) from Omega_{i+2}; the diameter of Q is 24 M_b l_i, so Q ∩ Omega_{i+2} = ∅.
Thus Q is in 𝒞_i.
(4) (S1) gives a G-valued u on Q with U_r^u = e^{i eta A}, l_i|A| < a_0 and l_i^2|∇A| < a_0 on the
bonds of Q, which include those of N. At z in N, lambda(z) <= i + 1, so l_{lambda(z)} <= L l_i. ∎

*Proof of Proposition 3.2.* With l >= 200 the middle cross-section of F is at least 100 blocks from
both ends of F, and by hypothesis Omega_0 equals F within 31 M_b eta of it.
(1) Let b_0 be a bond in the middle cross-section with its six plaquettes in F, and p any end-point
of a bond of those plaquettes (within 2 eta of the cross-section). A class cube of level 0 with side
s >= 10 M_b eta containing p lies in Omega_0. On the line through p in a direction transverse to F,
the cube contains a segment of length min{s, 30 M_b eta} >= 10 M_b eta that contains p and lies within
30 M_b eta of p, hence in Omega_0 within 31 M_b eta of the cross-section, hence in F; but the
transverse width of F is less than w M_b eta <= 9 M_b eta. So no class cube of level 0 contains p.
Class cubes of level >= 1 lie in Omega_1, far away. So (S1) puts no condition on these bonds.
(2) Let U_t(b_0) := exp(i pi t sigma_3) and U_t := 1 on every other bond, t in [0,1], and 𝔞 := 0. Each
U_t is G-valued and satisfies (S1) (gauge u = 1, A = 0 on every class cube), (S2) and (S2+). The
level-0 rows are identities; the rows of level >= 1 read only bonds within 2 l_1 of Omega_1, where
U_t = 1. A_s(U_t) is positive definite: <lambda, A_s lambda> = ||D_U lambda||^2 + ||m^{-1} Q' lambda||^2,
and if both vanish then lambda = 0 at the level-0 sites (Q'_0 = I) and, by D_U lambda = 0 along bonds
and the zero extension, on every component of Omega_0. Q' is onto (its blocks are disjoint and the
transports invertible), so Q'G'^2Q'^T is positive definite, and R(U_t) is an orthogonal projection
depending continuously on t.
(3) At t = 0, Delta_a(1) is positive definite (flat-port (8.12); the tower is admitted).
(4) At t = 1 let A := alpha sigma_3 on b_0 (alpha real) and 0 elsewhere; ||A||^2 = eta^4 alpha^2 since
tr sigma_3^2 = 1. Each of the six plaquettes through b_0 has P = -1, so by the formula of Lemma 5.1
Psi_p(A, A) = (eta^2/2) tr(X^2(P + P^{-1})) = -eta^2 tr X^2 = -eta^{-2} ||A||^2, the commutator term being
absent for a one-bond field; the flat value is +eta^{-2}||A||^2. So <A, Delta(U_1) A> = -6 eta^{-2}||A||^2.
Next <A, D_U R D_U^T A> <= ||D_U^T A||^2 = 2 eta^{-2} ||A||^2 (two end-points; Ad(-1) = I), and
<A, Q^T a Q A> = eta^{-2} ||A||^2 (the level-0 row b_0; no other row reads b_0). So
<A, Delta_a(U_1) A> <= -3 eta^{-2} ||A||^2 < 0.
(5) The least eigenvalue of the real symmetric matrix Delta_a(U_t) is continuous in t, positive at 0
and negative at 1. With t_* := min{t : it is <= 0}, it vanishes at t_*, so Delta_a(U_{t_*}) is
singular. This is an explicit path and an existence argument; no value of t_* is computed.
(6) U' := U_1 satisfies (S1), (S2) and has |∂U' - 1| = |-1 - 1| = 2 at the six plaquettes, while the
bound of CA-I 12968-12973 at level 0 is 4(a_0 + a_1) < 2 when a_0 + a_1 < 1/2. ∎

*Proof of Proposition 3.3.* Since Omega_0 ≠ T_eta, some site x_0 of Omega_0 has a neighbour x_0 ± eta e_mu
outside Omega_0; let b_0 be the positively oriented bond between them. It is a field bond with one
end-point outside Omega_0. It is a row of level 0, since Omega_1 is more than R M_b eta from Omega_0^c.
No class cube contains b_0, because class cubes lie in Omega_0 and the bonds of a cube have both
end-points in it. Take U_t and 𝔞 = 0 as in the previous proof; (S1), (S2), (S2+) hold, the rows of
level >= 1 do not read b_0, and steps (2), (3) and (5) are unchanged. At t = 1, with A on b_0: the six
plaquettes through b_0 are read by the Hessian (2.3) and all have P = -1, giving -6 eta^{-2}||A||^2;
D_U^T A lives on the sites of Omega_0, where only x_0 contributes, so ||D_U^T A||^2 = eta^{-2}||A||^2;
the row mass is eta^{-2}||A||^2. So <A, Delta_a(U_1) A> <= -4 eta^{-2} ||A||^2 < 0. ∎

*Remark.* The mechanism in Proposition 3.3 is the plaquettes that leave Omega_0, which SA 10287
includes explicitly ("for G_0 this includes the plaquettes that stick out of Omega_0") and which
(S1) does not test. Under (S1-loc) and (S2+), as in Theorem PI, U is controlled on those bonds.

## 11. Use by use

Account lines are CA-I unless marked II or III, at 31a47c543775 (hashes as in
`library/prior/print-inverse.md:21-26`, rechecked here for all four files). "PI" is Theorem PI
above: literal rows, the reading of §2, hypotheses (S1-loc), (S2), (S2+), rate delta_q, bare G_0.
Every entry needs, for a proper Omega_0, (S1-loc) at the boundary and (S2+): Proposition 3.3 shows
that (S1), (S2) do not give them. A consumer that writes Balaban's delta_0 reads the common rate
min{delta_0, delta_q} (Balaban's own definition of delta_0 as "a common, best possible, decay rate",
quoted at II 54617-54620), and fixes its later floors, ceilings and decoupling sizes at that rate.

| Lines | What is read | Supplied by PI? |
|---|---|---|
| 13143-13173 | the remark: (3.132), walks of type (3.98)-(3.99) with hull locality and (3.108)-type bounds, for every U in (S1), (S2) | **Not as stated**: Props. 3.2 and 3.3 are counterexamples on the account's tower class (thin remote finger; one bond leaving any proper Omega_0). **Supplied** under (S1-loc), (S2), (S2+), on every tower, for the literal rows: (b) a bound of the scale and decay form of (3.132) for the bare q_0, (c)-(d) walks with hull locality and majorants, (e) setting compatibility. (S1) gives (S1-loc) at interior points of thick towers (Prop. 3.1), and everywhere when Omega_0 = T_eta. |
| 13589, 13624-13627 | q_0 in K_{-2}; a walk expansion at complex U | Supplied: (b) with constant 8 C_q and rate delta_q, once the floors 13413-13428 are imposed at that rate; (c). |
| 13640-13665 | H_0 = G_0 Q^T q_0 l^{-1}, P_0 = I - G_0 Q^T q_0 Q and their identities | Supplied: (a) gives G_0, q_0 and q_0^T = q_0; the identities are then algebra. |
| 13675 | N_beta(H_0 B) <= B_0 |B|, N_beta(G~_0 f) <= B'_0 |f|_{(-3)}, P_0^T in K_0 | Partly: q_0 in K_{-2} is supplied. The pointwise and Hölder bounds of G_0 (CMP 99b (3.42)-(3.45); rows B99b-T33, B99b-T34) are separate inputs; the energy-norm words (Remark after Lemma 6.3) do not give them. |
| 13683; 19583-19600 | hypotheses "assume the bounds and the walk expansion of q_0" | Supplies the q_0 inverse input for the literal rows under the hypotheses above (pi-gate §8 REVISE: not "discharges BP07"). Every other hypothesis remains. |
| 13766, 13899-13909 (J3) | q_J in K_{-2}, from q_J = (I + q_0 Q (G^J_pi - G_0) Q^T)^{-1} q_0 with C_J a_gamma <= 1/2 | Supplied for the q_0 input. Impose all of 13413-13428 at the rate used, and choose the current ceiling from the resulting kernel constants. |
| 13787-13798, 13966-13979 (J8) | a walk family for q_0 "with bounds of the type of (3.108) and (1.7)", terms local, not re-summed | Supplied for q_0: (c)-(e); words local and holomorphic, absolute majorant, summation and spare factors, two spare exponentials. The differentiated vector norms and the current-insertion families remain separate. |
| 13915-13923 (J4) | H^J decomposition using q_J - q_0 and the H_0 bound | The q_0 part is supplied; the H_0 bound as in row 13675. |
| 14377-14476 | chart definition and representation; inserts Q^T(q_0 - a)B~ and Q^T q_0 B~ | Supplied for the inverse factors and the algebra. Chart existence and its fixed-point estimates remain inputs (pi-gate §8 REVISE). |
| 14655 | analyticity of q_0 on the admitted complex domain | Supplied on the PI ball {N_{U_r}(𝔞) < a_1^*} with (S2+); the consumer's domain must lie in it by its radius choice. |
| 14715-14774 (K3) | |Q^T(q_0 - a)B~|_{(-3)} <= C'|B~|_{(-1)} | Supplied for this estimate: q_0 in K_{-2}, the physical column bound of Q^T (Lemma 4.4 (iii), (iv)) and the kernel algebra (i). The rest of K3 is not proved here. |
| 14831 | Q^T(q_0 - a) l^{-1} v in the first variation, with weights | Supplied at weight rates kappa <= delta_q/2. A first variation, not a second-response estimate. |
| 15266-15490 (K10) | per walk: summable factors, two spare exponentials in the anchored tree length, analytic local terms, separation at zero switches | Supplied for q_0 with: the summation factor theta^{n/4} and the spare factor of (d); the localisation domains of a term are its footprints F_tau (full cubes, including parts where nothing depends); the decoupling cube side must exceed the footprint side 2 r^ l (then each footprint meets at most 2^4 cubes, an anchored tree through y, y' and the footprints has length at most (1 + 2^4) D_X (n+1), and (d) with Lambda := that length/(1 + 2^4) gives two spare exponentials at rate delta_q/(1 + 2^4)); separation at zero switches by (e). |
| 15770-15796 | P_0^T Delta_a = Delta_a - Q^T q_0 Q; real minimiser, then complex B | Supplied for the inverse algebra. Real-minimiser identification, chart uniqueness and continuation in the datum remain the consumer's premises. |
| 19744-19750 | operator-bounds theorem, importing J2-J8 and K10 | PI contributes only the q_0 inputs listed in this table (pi-gate §8 REVISE). |
| 5293-5470, 5702-5712 (f4 ordered words; (C1)) | index set, letter values and supports equal in two settings agreeing on a footprint; absolute convergence of restricted operators | Supplied for the q_0 entry by the assignment of §9 (walks of fixed tile grids, letters S_tau and T_tau, footprints |omega|). Entrywise majorants and restricted sums converge by (c)-(d). Not supplied: the account's D, D', D'' families for the other operators of its table. |
| 13323 | near bound frame: the remark "stands under" CMP 109 (3.31)-(3.32) | Attribution only; no inverse estimate is read. PI does not construct the frame. |
| II 54464-54635 (5.8:prop-local-decay) | real backgrounds under (3.35); C_Q = q_0 with factor e^{-8 delta_1 d} | Supplied for C_Q on the literal rows at the common rate, under (S1-loc) (for (3.35)-backgrounds: at interior points of thick towers, Prop. 3.1). No bound for the other listed operators. II 54617-54620 says the exponential of (3.132) "does not depend on d(y,y')" within one layer; the page image of (3.132) decays in d(y,y') for all pairs, and so does (b). The discrepancy is recorded, not resolved here. |
| II 60313 | list entry for (3.132)-(3.133) | (3.132) in the bare form above; (3.133) needs G_0's pointwise bounds (row 13675). |
| III 36352-36370 | (3.132) for (Q G_1 Q^T)^{-1}, G_1 current-corrected, on (3.37)-(3.38) | Not supplied. G_1 is not G_0; a controlled perturbation argument (Balaban's Theorem 3.12) is needed. |
| 166593-166594; III 111329 | status lists: "printed without proof; cited as printed" | No status is granted here. The proposed text for the lead: proved by Claude under (S1-loc), (S2), (S2+) for the literal rows, not yet checked by the other model; the remark as printed fails on the account's tower class (Props. 3.2, 3.3). |

## 12. Standing, what changed, and what stays open

**Kind and standing.** Proof of a step the account cites as printed without proof (CA-I
13164-13173, 166593-166594), on the literal rows of its target, under the local hypothesis
(S1-loc) and (S2), (S2+); and correction of the remark's hypothesis on the account's tower class
(Propositions 3.2, 3.3). Proved by Claude, not yet checked by the other model. It is an
implication from:
- [F], `library/flat-port.md` §§8, 9.2, 12: checked by Claude, first failing step none;
- Balaban's definitions, read from the page images (§1), and Lemma 4.1 (elementary analysis).
It no longer reads `library/b109.md` P15-P17: the row comparison is Lemma 4.4, and the other block
comparisons (P16, P17) are proved in Lemma 5.1. P15 enters only the remark on the symmetric rows
(§3.7). No computation was used; finite arithmetic is displayed where it occurs.

**What changed from r1.** (1) The rows are Balaban's literal one-contour rows on corner blocks,
composed at the averaged backgrounds (Definition 4.3), and Lemma 4.4 proves their depth-uniform
complex comparison by straightening Balaban's own relative average (CMP 98 (63)); the symmetric
rows are a remark. (2) The class is fixed (§2): cubes of side 12 M_b l_j of p.396, cube bonds inside
the cube, the account's towers, touching bonds, difference rows, level extended by zero, Balaban's
CMP 96 distance with lowest layer Omega_1^c. (3) Every REVISE is applied: the eta^2 remainder
(Lemma 5.1), the overlap count 20L (§5.2), the variable-tile claim removed (§3.3 item 3), exterior
tiles with the gauge at z_tau (§5.2, Lemma 5.3), (S2+). (4) The two-settings clause is replaced by
the assignment of §9 with footprints of half-width (2L + 2) M_t l. (5) Part (d) is narrowed and
proved with theta <= (4D_*)^{-4}. (6) The exterior-centre boundary case is treated. (7) Proposition 3.2
is stated on the class where it is checked (size number >= 10, remote finger), every claim that
Balaban's Theorem 3.3 fails is removed, and Proposition 3.3 is added on the same terms.
(8) Proposition 3.1 keeps its interior qualification.

**Where it could still fail.** The new load-bearing step is Lemma 4.4: the bootstrap for the
literal rows needs the covariance of Balaban's relative average under complex gauges near 1
(Lemma 4.2 (iii)) and the margins of Lemma 4.2 (i). Propositions 3.2 and 3.3 rest on the
conventions stated with them (cube bonds inside the cube; field bonds touching Omega_0; the Hessian
of the full action on those fields); under other conventions they may not apply, and they say
nothing about Balaban's restricted class or his Theorem 3.3.

**Not proved here (separate rows or consumer obligations).**
- Balaban's pointwise and Hölder bounds (3.42)-(3.47) for G_0 at complex U (rows B99b-T33,
  B99b-T34), needed for H_0 and (3.133).
- (3.132) for the current-corrected G_1 (III 36352-36364) and Balaban's Theorem 3.12.
- The analytic averaging derivatives of CMP 98 §E (4.5:rem-averaging-analyticity, B98-P5; row 429).
- (S1-loc) and (S2+) at the boundary of a proper Omega_0: each consumer with Omega_0 = X must supply
  them from the regularity of U near the boundary of X; (S1) does not (Proposition 3.3).
- A gauge-gluing lemma deriving (S1-loc) at reentrant boundary points from a stronger, boundary-aware
  hypothesis; and the analogue of Proposition 3.1 on Balaban's restricted class.
- A commutator estimate making the radii independent of M_t (not used).

**For the lead (suggested; not edited here).** Registry PRINT-INVERSE / tree node BP07: "proved by
Claude for the literal CMP 99b rows under (S1-loc), (S2), (S2+), not checked; the remark as printed
fails on the account's tower class (thin finger; one bond leaving any proper Omega_0)". The check
this needs is one line-by-line reading by Codex of §§2-10, starting with Lemma 4.4 and
Proposition 3.3. As an outward contribution it has two candidate parts: the theorem for the
literal rows, and the correction of the remark's hypothesis. Both must pass the five checks of
FINISH "How we work" item 6; the second fails the account's statement as written only with the
conventions of §2, which are the account's own (CA-I 12721-12722, 12953-12955).
