lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T05:44Z

# A2 on separated layers with seams and nodes (queue row 90)

Pinned at commit 8ff6bd92a, branch claude/ym4d-hard-route. Research-stage working
state, no status. Written section by section; sections below are filled in as the
work proceeds.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max as configured for
this worker (Mac mini); repository commit 8ff6bd92a; Sussman–Alpoge outline
`YM4_sketch_500.tex` at commit 31a47c543775, fetched by URL into a scratch folder and not
committed; Balaban's CMP 99 (389–434) read from `~/ym4d-papers/cmp99b.txt` (OCR, outside
git). Research text by one model, not an audit, not a gate; it grants no status. No step
below rests on a computation; no numerical job was run.

**Credit.** The target A2, the operator definitions ((3.1) below, outline L10138–10208),
the layered geometry (L10106–10127), the flat layered Feynman gap PX107–PX113, the Wilson
form estimate PX114–PX118, the seam intertwining PX31–PX38, the reduced datum
PX98–PX100, the next-fibre formula PX101–PX104 and the Combes–Thomas mechanism (a)
(L10504) are Ethan Sussman and Levent Alpoge's outline, with Claude and Codex as authors
of their text. Tadeusz Balaban supplies the programme: the background-field propagators
and their positivity (CMP 99 (389–434), Theorem 3.11 and (3.157)–(3.158), which reduce
positivity of the fluctuation operator to the flat case of CMP 96 Lemma 2.4 "by
localizing"), and the independent current (CMP 109, (1.10)–(1.14)). The flat inputs and the
one-jump gauge-decomposition argument are this checkout's `c0-loc.md` §§5–6 (flat part
from `fan-ext.md`), gated there; the curved uniform-torus A2 and the second-jet and
on-shell multiplier estimates are `a2-curved.md` (Codex, ungated).

## 0. Disposition (provisional; revised in §9 at the end)

Counterexample first (§2): none found at seams, non-Lipschitz contacts, nodes or
outward rows; each candidate is killed by an explicit argument. Proof plan executed below:
flat one-jump coercivity for the outline's pruned rows on every seam shape (§3, new: zero
extension replaces the brick-fan reflection), curved patch estimates and localization on
arbitrary separated sequences (§4), Landau transfer and the fine precisions (§5), the
coarse form and A on the next fibre (§6), and the independent current by a Combes–Thomas
argument that needs only the coercivity just proved (§7).

## 1. The statement attacked

Notation is the outline's (L10106–10208) unless stated. L is odd; M_1, R_1 are powers of
L; rho := R_1 M_1. A separated sequence Omega_0 ⊃ ... ⊃ Omega_{k+1} has each Omega_j a union
of M_1-cubes of level j and dist_inf(Omega_j^c, Omega_{j+1}) > rho xi_j, with
xi_j = L^{j-k}, eta = xi_0. Layers L_j, tops, pillars B^j(y) of side xi_j, and rows
Gamma_j (interior, and for j >= 1 outward; inward bonds carry no row) are as in the outline;
for the fine problem the sequence is cut at depth k (so L_k = Omega_k), and Omega_{k+1} is
the next step's region. Fine fields live on the bonds with both ends in Omega_0 (Dirichlet
outside); Delta^W is the Hessian of the inner-plaquette action. Pairings are physical:
eta^4 per fine bond or site, xi_c^4 per row, xi_y^4 per top. Norms (PX109):

    ||h||_mass^2 = sum_b eta^4 xi_b^-2 |h_b|^2      (xi_b = larger endpoint pillar scale),
    ||psi||_row^2 = sum_c xi_c^2 |psi_c|^2,           ||h||_X^2 = ||h||_mass^2 + ||nabla_U h||^2.

So <h, Q^T a Q h> = a_0 ||Qh||_row^2 with a = a_0 xi_c^-2 on rows; a_0 = 1 below.

A real regular pair (U, J) for (Omega_j)_{j<=k+1} (outline L10128–10138) has, on L_j:
|dU - 1| < alpha_0 eta^2 xi_j^-2 on plaquettes, |J| < gamma_0 xi_j^-3, and on every cube of
side c_g M_1 xi_j inside L_j ∪ L_{j+1} a real gauge U = e^{i eta A} with
xi_j|A|, xi_j^2|nabla A| <= alpha_0. J is an independent variable; on shell means J = J(U)
at bonds touching Omega_1, and physical means U is a regular critical point of its datum
(outline Theorem 1) with J = J(U). The operators G', R, S, G_0, G, H, G_1, H_1, Delta_k
and A = C_V^T (G^(2)_V + Delta_k) C_V are those of outline L10142–10208, with
V = M^k U, the fluctuation on the level-k bonds touching Omega_{k+1}, and the pivot bonds
eliminated. As in the outline's physical convention (PX104 and the sentence after it),
U is taken in a gauge in which V is block axial on Omega_{k+1}; gauge covariance of all
operators makes this a normalization, not a restriction.

**Theorem A (target).** There is an absolute L_0 and, for odd L >= L_0, constants
c_L > 0, M_*(L), rho_*(L) and a_*(L) > 0 such that: if M_1 >= M_*, rho >= rho_*,
alpha_0, gamma_0 <= a_*, then for every separated sequence of depth k+1, every compatible
torus, and every real regular pair (U, J), on shell or not, all inverses in the definition
of A exist, G_0, G, G_1 > 0, and

    <u, A u> >= c_L ||u||^2    on the free coordinates u (counting norm, xi_k = 1),

and the same bound holds for chi_Y A chi_Y on every conditioning set Y (`a2-curved` (2.1)).
The ceilings a_* and the constant c_L depend on L only, so they are fixed before M_1, as
the outline's statement 4 requires (L10335).

The complex half-gap of A2 is not part of Theorem A; §8 records exactly what the
argument of `a2-curved` §12 needs on layers.

## 2. Counterexample tests (done before the proofs)

**2.1 Seam-concentrated fields.** The attempted failure: a fine field H near the seam
between L_j (fine side, leaf scale h = xi_j) and L_{j+1} (coarse side, S = L h) that is
invisible to every actual row, has small curl and small projected divergence, yet has
large mass. Inward level-j bonds carry no row, and on the fine side there are no
level-(j+1) rows except the outward ones, so the natural place to hide is the strip of
fine-side level-(j+1) blocks next to Omega_{j+1}. It fails, for a structural reason. Every
level-(j+1) bond with both ends outside Omega_{j+1} has its double block inside L_j, and
every level-j bond read by its straight average joins two level-j tops of L_j, hence is an
interior row; on full grids Q^0_{j+1} = Q^0_L Q^0_j (digit count, `a2-curved` §9). So all
level-(j+1) averages vanish on the whole seam neighbourhood once the actual rows do:
interior rows of L_{j+1}, outward rows, and these compositions. The coarse-scale torus
estimate then applies across the seam, and only the leaf-scale part of the divergence
remains, which the fine rows control (§3). Qualitatively there is no zero mode: if U = 1,
all actual rows of H vanish, dH = 0 and P D^*H = 0, then H = d phi on the patch, Q'phi
takes one value c at all tops of both levels (QD = D_ext Q', PX38, with the outer-end
average PX34), and D^*H = Delta phi is constant on every pillar, so
||H||^2 = <phi - c, Delta phi> = sum_y xi_y^4 (Delta phi)_y (Q'phi(y) - c) = 0.

**2.2 Non-Lipschitz contacts.** The outline allows any union of M_1-cubes, so two cubes of
Omega_{j+1} may meet only along a 2-face, an edge or a vertex, and the fine side is then not
Lipschitz there. The brick-fan reflection of `fan-ext.md` §3 and `c0-loc.md` §6 covers only
the brick patterns it lists, and an H^1 extension across a codimension-2 contact in four
dimensions costs a logarithm. This is the candidate most likely to break a constant. It
does not: the one-jump argument needs to extend only a function u with zero mean on every
coarse block of the fine side, and for such u the zero extension costs a factor 1 + 80L,
whatever the shape (Lemma Z, §3). The constant depends on L, which A2 allows.

**2.3 Nodes and outward data.** In the next step, no block B(y), y in T^(k+1) ∩ Omega_{k+1},
contains a node other than y (outline L9783), because inward bonds are omitted. The A2
mask varies only level-k data on bonds touching Omega_{k+1}, which lie at distance
> rho xi_k from Omega_k^c, so they are interior rows. The reduced datum then satisfies
PX100 there: Db(0)iota = iota and D^2 b(0)[iota·, iota·] = 0, because the outer factor v_z
of every outward row depends only on lower-level data, which the mask fixes at zero
(PX99). So outward datum jets enter A only through the fine problem's rows, which §§3–4
keep. At the boundary of Omega_{k+1}, including contacts, the next-step injectivity is
checked in §6.2.

**2.4 Independent current.** Without stationarity the multiplier H^T J has no algebraic
formula, and the worry is that it is not O(gamma_0 xi^-3) uniformly. At U = 1, H is the
flat constrained readout, which decays (outline statement 1), so no counterexample exists
there. The large actual current J(U) of a non-critical regular U (the staggered field of
outline mechanism (e)) enters neither the coercivity (PX118 uses only plaquettes) nor
H^T J. The uniform bound is proved in §7.

No counterexample was found. The proofs follow.

## 3. Flat one-jump coercivity for the pruned rows, on every seam shape

**Model.** T is a periodic fine lattice of spacing eta, h = L^i eta (i >= 0) and S = L h;
T is a union of centred S-blocks. Y (coarse side) is a union of S-blocks and F = T \ Y
(fine side) is too. Leaves are the h-blocks of F and the S-blocks of Y; r_N is the leaf
mean, P_N = 1 - r_N^* r_N, phi := D^*H. At U = 1 the actual rows are: *fine rows*, the
h-bonds with both ends in F; *coarse rows*, the S-bonds with at least one end in Y. On each
the row map Q^0 is the straight per-length average PX107 at that scale (at U = 1 it is the
straightened row, outline statement 2, last sentence). This is the outline's row set on a
one-wall patch: with F ⊂ L_j, Y ⊂ Omega_{j+1}, h = xi_j, fine rows are the interior
level-j rows, coarse rows are the interior and outward level-(j+1) rows, and the inward
level-j bonds (F to Y) carry nothing. Section 4 places every one-wall patch so that this
identification holds on it and on its read sets. h = eta (bare fine side) is included: then
fine rows are the bare bonds and Q^0 = 1 on them.

**Lemma C (composition).** If H has vanishing fine rows, then Q^0_S H(c) = 0 for every
S-bond c with both ends in F. *Proof.* On full grids Q^0_S = Q^0_L Q^0_h, because the
start digits and segment positions enumerate each finer start and segment position once,
with the per-length normalization (`a2-curved` §9; direct from PX107). The h-bonds read by
Q^0_L at c join h-sites of the double block of c, which lies in F; so they are fine rows. ∎

So all S-averages of H vanish on T: on coarse rows by hypothesis, on the others by Lemma C.

**Lemma Z (zero extension; any shape).** Let u be a function on the h-sites of F with zero
mean on every S-block of F, and v = u on F, v = 0 on Y. Then

    ||D_h v||^2 <= (1 + 80 L) ||D_h u||_F^2,

where ||D_h u||_F^2 sums h^4 |D_h u|^2 over h-bonds with both ends in F.
*Proof.* Only h-bonds from F to Y are new; each contributes h^4 |u(x)/h|^2 at its F end x.
Such an x lies on a face, adjacent to Y, of an S-block P ⊂ F (F and Y are unions of
S-blocks). On the line of P through x normal to that face (L sites), Cauchy gives
|u(x)|^2 <= 2|u(x')|^2 + 2L sum_line h^2 |D_h u|^2 for each x' on the line; averaging over
x' and summing over the face,
sum_face h^2 |u|^2 <= (2/(L h^2)) ||u||_P^2 + 2L ||D_h u||_P^2. The zero mean on P and the
coordinate-path variance bound (`c0-loc` §6) give ||u||_P^2 <= d S^2 ||D_h u||_P^2 with
d = 4, and 1/(L h^2) = L/S^2. So one face costs at most 2L(d+1)||D_h u||_P^2 = 10L||D_h u||_P^2,
and P has at most 2d = 8 faces. ∎

No reflection, fan pattern or Lipschitz property of the seam is used. Two cubes of Y
touching along a 2-face, an edge or a vertex are covered.

**Lemma M (leaf mean of the divergence).** For a leaf B of side sigma = n eta and
c_B = r_B phi,

    |B| |c_B|^2 <= K_m^2 ( sigma^-2 ||H||_{B+}^2 + ||P_N phi||_B^2 ),   K_m^2 = 2·486^2,

where B+ is the set of bonds with both ends in B if n >= 3, and of bonds touching the site
if n = 1. *Proof.* Leaf sides are 1 or odd powers of L >= 3. For n = 1,
|phi(x)|^2 <= 8 eta^-2 sum_{b∋x} |H_b|^2. For n = 2r+1 >= 3 put
tau(m) = min(m, n-1-m), m = 0..n-1, so mean tau = r^2/n, sup tau/mean tau <= 3, and
1/mean tau <= 9/n. The tensor tent p_B = prod_mu tau(m_mu)/mean tau has mean one,
sup <= 81, |D_mu p_B| <= 243/sigma, and vanishes on the boundary sites of B. With
g = sigma^2 c_B p_B, summation by parts and r_B g = sigma^2 c_B give exactly
|B| sigma^2 |c_B|^2 = <Dg, H> - <P_N g, P_N phi>. Since ||Dg|| <= 486 sigma |B|^{1/2}|c_B| and
||g|| <= 81 sigma^2 |B|^{1/2}|c_B|, dividing gives
|B|^{1/2}|c_B| <= 486 sigma^-1 ||H||_{B+} + 81 ||P_N phi||_B; square. ∎ (This is the flat
case of `c0-loc` (5.5), with explicit tents.)

Summing over leaves, each bond in at most two B+, and sigma >= h = S/L for every leaf of
the model:

    ||(1 - P_N) phi||^2 <= K_m^2 ( 2 L^2 S^-2 ||H||^2 + ||P_N phi||^2 ).              (3.1)

**Theorem 1 (flat one-jump coercivity).** If all actual rows of H vanish, then

    S^-2 ||H||^2 + ||nabla H||^2 <= C_1(L) ( ||dH||^2 + ||P_N D^*H||^2 ),
    C_1(L) = C_F + 1 + K_m^2 + 2 K_m^2 L^2 C_F,
    C_F = max{ 2d+1, (1 + a_0^2 + 2a_1 + 2a_1^2) C_T },  a_0 = J_0 sqrt(d),  a_1 = J_1 sqrt(1+80L).

C_T is the flat torus constant of `c0-loc` (6.4) (re-derived in `a2-curved` §10), and
J_0, J_1 are the lift constants of `c0-loc` (6.3); all three are absolute. C_1 is of order
L^3.

*Proof.* Work in units S = 1; the mass rescales by S^-2 and the energies are unchanged.

(a) By Lemma C and the hypothesis, Q^0_S H = 0 on every S-bond of T.

(b) Let omega minimize ||H - D omega||^2 over site functions with zero S-block means
(r_0 omega = 0); the block variance bound makes this quadratic positive definite. Put
H_s = H - D omega, x = ||D omega||, y = ||H_s||, p = ||P_N phi||. The normal equation gives
<H_s, D omega'> = 0 for all such omega', so P_0 D^*H_s = 0 and x^2 + y^2 = ||H||^2. Also
dH_s = dH, and Q^0_S H_s = Q^0_S H - D_S r_0 omega = 0 (QD = D'r at U = 1). The torus
estimate `c0-loc` (6.4) gives y^2 + ||nabla H_s||^2 <= C_T ||dH||^2, and the block variance
bound gives ||omega|| <= sqrt(d) x.

(c) Let u = r_h omega on the h-sites of F. On a fine row c, Q^0_h D omega = D_h r_h omega, so
D_h u = -Q^0_h H_s there. The counting kernel w_cb of Q^0_h has row sum one and column
sum exactly n^-4 = (eta/h)^4 at each fine bond (the transverse box sums to one on the
h-grid; longitudinally, a residue class mod n of a convolution of two length-n boxes sums
to n, and the weight is n^-5). So sum_c h^4 w_cb = eta^4, and Jensen gives
||D_h u||_F <= y. The S-block means of u on F
are those of omega, hence zero.

(d) Let v be the zero extension of u (Lemma Z): ||D_h v||^2 <= (1+80L) y^2 and
||v|| <= ||u|| <= sqrt(d) y by the parent variance bound. Let w = J v be the lift of
`c0-loc` (6.3): its h-block means are v, ||w|| <= J_0 ||v|| <= a_0 y and
||Dw|| <= J_1 ||D_h v|| <= a_1 y. Then omega - w has zero mean on every leaf: on h-leaves of F
both means are u; on S-leaves of Y both are zero (v = 0 there and r_0 omega = 0).

(e) Hence omega - w lies in the range of P_N, and
x^2 = <D omega, H> = <omega - w, P_N phi> + <Dw, H>. So
x^2 <= (sqrt(d) x + a_0 y) p + a_1 y (x + y). Young's inequality in the form
sqrt(d) x p <= x^2/4 + d p^2, a_1 x y <= x^2/4 + a_1^2 y^2, a_0 y p <= p^2/2 + a_0^2 y^2/2 gives
x^2 <= (2d+1) p^2 + (a_0^2 + 2a_1^2 + 2a_1) y^2, hence
||H||^2 <= C_F (||dH||^2 + p^2).

(f) On the periodic lattice ||nabla H||^2 = ||dH||^2 + ||phi||^2 exactly (Fourier component
identity |delta|^2 I = delta delta^* + (delta∧)^*(delta∧), `c0-loc` (6.4)). Split
||phi||^2 = p^2 + ||(1-P_N)phi||^2 and use (3.1) and (e). ∎

**Corollary 1' (rows on the right).** For every H on the model,

    S^-2 ||H||^2 + ||nabla H||^2 <= C_1'(L) ( ||dH||^2 + ||P_N D^*H||^2 + ||Q^0 H||_row^2 ),
    C_1' = 4C_1 + 32 C_1 K_B^2 + 2 K_B^2,

with K_B the constant of the following exact lift. *Two-stage lift.* For each fine row put a
two-moment bump in one endpoint fine pillar, separating the two incident longitudinal rows
(the tents of `a2-curved` §10 for n >= 128, the profiles (9.3) there for 3 <= n < 128, the
identity for n = 1). A fine pillar's bumps are read only by its incident fine rows, so this
B_1 is exact on fine rows. Then lift the coarse residual q_coarse - Q^0 B_1 q_fine by the
same bumps at scale S placed in an endpoint pillar lying in Y (the inner end of an outward
row). No fine row reads Y, so B q = B_1 q_fine + B_2(q_coarse - Q^0 B_1 q_fine) satisfies
Q^0 B q = q exactly; no Neumann series and no smallness in L is needed. Amplitudes are
O(|q_c|) and slopes O(|q_c|/xi_c) on volume xi_c^4, and the coarse residual of B_1 is at most
C L^-1 ||q_fine||_row in row norm, so S^-2||Bq||^2 + ||nabla Bq||^2 <= K_B^2 ||q||_row^2 with K_B
absolute. Apply Theorem 1 to H - B Q^0 H and use ||dV||, ||D^*V|| <= 2||nabla V||. ∎

The uniform single-scale case (Y empty or F empty) is `a2-curved` (10.2) with its
inhomogeneous version (constant C_T' there).
