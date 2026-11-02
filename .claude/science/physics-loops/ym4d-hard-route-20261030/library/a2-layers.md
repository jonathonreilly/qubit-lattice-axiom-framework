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
side at most c_g M_1 xi_j inside L_j ∪ L_{j+1} a real gauge U = e^{i eta A} with
xi_j|A|, xi_j^2|nabla A| <= alpha_0 (the outline's "cubes of side O(M_1 xi_j)", with the bound
alpha_0 on the whole cube, L10137). J is an independent variable; on shell means J = J(U)
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

## 4. The weighted graph estimate on separated sequences

Fix L and a patch parameter R >= 10 (chosen in 4.3 as a function of L only). Require

    rho > 16 R L,        c_g M_1 >= 8 R L,        alpha_0 <= a_1(L)/(2L^2),        (4.0)

with a_1(L) fixed in 4.2. The first makes every one-wall patch below meet one seam only and
stay away from Omega_0^c; the second puts every patch, with its read set, inside one gauge
cube of the regular-pair class.

**4.1 Patches.** A *one-wall patch* at the seam j/(j+1) (0 <= j < k) is a set of
sup-diameter at most 2R xi_{j+1} lying within 3R xi_{j+1} of the boundary of Omega_{j+1}. Its
read set (the patch enlarged by 4 xi_{j+1}, which contains the double blocks of every row
reading it) lies in L_j ∪ L_{j+1}, at distance > rho xi_j - 4R xi_{j+1} > 0 from Omega_j^c and
> rho xi_{j+1} - 4R xi_{j+1} from Omega_{j+2}. On it the outline's rows are exactly those of the §3 model with h = xi_j,
S = xi_{j+1}: level-j bonds with both ends outside Omega_{j+1} join two level-j tops of L_j
(interior rows); level-(j+1) bonds with an end in Omega_{j+1} have that end in L_{j+1} and no
end in Omega_{j+2} (interior or outward rows); inward level-j bonds carry none; no row of
another level reads the read set. Leaves are the level-j pillars outside Omega_{j+1} and the
level-(j+1) pillars inside. For the model torus take a cube of side about 12 R xi_{j+1}, a
union of S-blocks centred at the patch, with Y = Omega_{j+1} ∩ cube, and identify opposite
faces. Its points lie within 15 R xi_{j+1} < rho xi_j of the seam (by (4.0)), so the cube minus Y
lies in L_j and no other seam enters; H is supported in the patch, at distance >= 4 R xi_{j+1}
from the cube's faces, so the artificial faces read zero.

An *interior patch* of layer j >= 1 is a set of sup-diameter at most 2R xi_j at distance
>= 2R xi_j from the boundary of Omega_j and >= 2R xi_{j+1} from that of Omega_{j+1}, so its read
set lies in the interior of L_j; its model is the uniform
torus of `a2-curved` §10 at scale xi_j. In L_0 no patch is needed: bare rows are the
identity on bonds with both ends in L_0, so on such bonds eta^-2 ||H||^2 = ||QH||_row^2 and
||nabla H||^2 <= 16 eta^-2 ||H||^2 directly; the Dirichlet boundary and the plaquettes that
stick out of Omega_0 lie there and are never used.

**4.2 Curved patch estimates.** In the gauge of the cube containing a patch's read set,
xi_j|A| <= alpha_0 and xi_j^2|nabla A| <= alpha_0; measured in the scale of a level-(j+1) row this
is at most a := 2L^2 alpha_0. For every row whose dependence cube lies there, the recursion
`a2-curved` (8.4)–(8.7) gives row and column sums of the actual straightened coefficients
within C_L a of the flat ones, relative to the flat sums, with no depth factor; PX47 gives
the pillar transports within C_L a of 1; the connection factors of D_U, d_U, nabla_U are
1 + O(eta a/xi). Hence, for H supported in the patch and written in that gauge,

    ||(Q - Q^0)H||_row + ||(P - P^0)D^*H|| + ||(d_U - d)H|| + ||(D_U^* - D^*)H||
         + | ||nabla_U H|| - ||nabla H|| | <= C_L a ( ||H||_mass + ||nabla H|| ),        (4.1)

and ||H||_mass <= L S^-1 ||H|| on a one-wall patch. Insert (4.1) into Corollary 1' (or its
single-scale version) for the gauge-transformed field; gauge covariance preserves every norm.
Choosing a_1(L) so that 6 C_1'(L) (C_L a_1 L)^2 <= 1/2 and absorbing gives, with
C_P := max{4C_1', 4C_T', 17}:

    s_P^-2 ||H||^2 + ||nabla_U H||^2 <= C_P ( ||d_U H||^2 + ||P D_U^*H||^2 + ||QH||_row^2 )   (4.2)

for H supported in a patch of scale s_P (S for one-wall patches, xi_j for interior ones,
eta in L_0). The same comparison turns Lemma M into its curved form with the transported
own-pillar mean (PX31) and constant 2K_m, once C_L a <= 1/4. Outward rows enter (4.1)–(4.2)
through their straightened linear part (PX37–PX38), with the outer node factor removed
exactly by straightening, so the outward datum jets are kept, not dropped.

**4.3 Localization.** Let Theta_j = clamp(3 - dist_inf(x, ∂Omega_{j+1})/(R xi_{j+1}), 0, 1); the
supports of different Theta_j are disjoint by (4.0). Put Theta = sum_j Theta_j,
N = (Theta^2 + (1-Theta)^2)^{1/2} >= 2^{-1/2}, chi_seam = Theta/N, chi_int = (1-Theta)/N, so
chi_seam^2 + chi_int^2 = 1 and |nabla chi_seam| + |nabla chi_int| <= C/(R xi_{j+1}) near seam j/(j+1).
Multiply chi_seam near seam j/(j+1) by a squared partition of unity of tents of scale
R xi_{j+1}, and chi_int on L_j by one of scale R xi_j (sum of squares one, overlap at most 2^4,
slopes C/(R·scale)). The support of every product chi_i (not merely its tent cube) is a
patch of 4.1, of scale s_i, because Theta_j = 1 within 2R xi_{j+1} of the seam; and
sum_i chi_i^2 = 1. Define the patch scale s(x) = xi_{j+1} for x in L_j within 4R xi_{j+1} of
Omega_{j+1}, and s(x) = the own layer scale otherwise, and

    ||H||_s^2 = sum_b eta^4 s(b)^-2 |H_b|^2,   s(b) = max over the ends of b.

Then M(x) := sum_i s_i^-2 chi_i(x)^2 >= s(x)^-2, and, because the interior tents' slopes come
multiplied by chi_int,

    sum_i |nabla chi_i|^2 <= 2|nabla chi_seam|^2 + 2|nabla chi_int|^2 + C R^-2 sum_i s_i^-2 chi_i^2
                          <= C' R^-2 M.                                                  (4.3)

This is the point where the scale change costs nothing: the fine-scale slopes C/(R xi_j)
occur only with the factor chi_int^2, which carries the fine mass xi_j^-2.

Apply (4.2) to each chi_i H. The commutators are: d_U(chi H) = chi d_U H + O(|nabla chi||H|) and
D_U^*(chi H) = chi D_U^* H + O(|nabla chi||H|) by the discrete Leibniz rule; on a leaf B,
[P, chi]phi = P((chi - chi_B) c_B) - (1 - P)((chi - chi_B) P phi), so by curved Lemma M
||[P, chi]phi||_B <= 2K_m |nabla chi| ||H||_{B+} + (2K_m + 1) sigma_B |nabla chi| ||P phi||_B, with
sigma_B |nabla chi| <= 1/R; and ||[Q, chi]H||_row <= C||(nabla chi)H|| because a row's carrier has
diameter <= 2 xi_c. Since nabla_U(chi_i H) = chi_i(·+eta e) nabla_U H + (nabla chi_i)H, also
sum_i ||nabla_U(chi_i H)||^2 >= (1/2)||nabla_U H||^2 - sum_i ||(nabla chi_i)H||^2. Summing (4.2) over i and
using (4.3):

    ||H||_M^2 + (1/2)||nabla_U H||^2 - C' R^-2 ||H||_M^2
         <= C_P [ (2 + C R^-2) E(H) + C C' R^-2 ||H||_M^2 ],
    E(H) := ||d_U H||^2 + ||P D_U^* H||^2 + ||QH||_row^2.

Choose R = R(L) with R^2 >= 8C'(1 + C C_P). This proves:

**Theorem 2 (weighted graph estimate, P-form).** Under (4.0), for every real regular U on
every separated sequence and every fine H on the bonds of Omega_0,

    ||H||_s^2 + ||nabla_U H||^2 <= C_2(L) ( ||d_U H||^2 + ||P D_U^* H||^2 + ||QH||_row^2 ),   C_2 = 6 C_P,

and ||H||_mass^2 <= L^2 ||H||_s^2, so ||H||_X^2 <= L^2 C_2 E(H). All constants depend on L only:
not on depth, eta, volume, the number of layers, or the shapes of the regions. ∎

This is the weighted version of `a2-curved` (10.4) for the actual pruned rows on arbitrary
separated layers. It uses neither stationarity nor the current.

## 5. Scalar estimates, the Landau gauge, and the fine precisions

Sites are those of Omega_0; Q' = Q'_pill is the transported own-pillar mean (PX31),
Z = ker Q', sigma(x) the scale of the pillar of x, and Delta_U = D_U^T D_U. Bare tops are
single sites, so every z in Z vanishes on L_0, hence near the Dirichlet boundary.

**5.1 Slowly varying weights.** Call theta *tau-Lipschitz* if
|theta(x) - theta(x')| <= tau d_B(x, x') for all x, x' (d_B the outline's layer metric, L10114).
Every pillar, row carrier and plaquette has d_B-diameter <= 4L, and a fine bond at a top of
scale sigma has d_B-length <= L eta/sigma. Mere slowness on balls would not do: across one fine
bond the weight must change by O(tau eta/sigma), or the commutator with a difference costs
tau eta^-1 instead of tau sigma^-1 and depth uniformity is lost. For tau-Lipschitz theta and
each local operator O among D_U, D_U^T, d_U, nabla_U, Q, Q', Q'^T, E_pill (PX32) and
multiplication by a function constant on pillars, e^{theta} O e^{-theta} - O is O itself with
each coefficient multiplied by e^{theta(x) - theta(x')} - 1, of size <= 8L tau on carriers and
<= 2L tau eta/sigma across a bond, for tau <= 1/(8L); hence, in the scaled norms used below,

    || e^{theta} O e^{-theta} - O || <= C_L tau ||O||_abs,                               (5.1)

where ||O||_abs is the same norm of the operator with absolute coefficients, bounded by the
scale counts of `a2-curved` (8.6)–(8.7), PX33 and PX113. For differences the factor sits on
the shifted term, so (5.1) produces sigma^-1 times the field, which the mass part of each norm
controls. Two weights are used: *scale weights* zeta = e^{-2psi}, with
psi(x) = min_x' { log sigma(x') + kappa d_B(x, x') }, so -2psi is 2kappa-Lipschitz and
sigma^-2 <= zeta <= L^2 sigma^-2 once kappa rho >= 2 log L (by PX4, d_B >= rho(|i-j|-1)_+ between
layers i, j); and *decay weights* e^{-varsigma min(d_B(·, c), M)}, which are varsigma-Lipschitz.

**Lemma CT.** Let k be a real bounded form on a finite-dimensional Hilbert space V with
k(v, v) >= c||v||^2, and theta a weight with |k(e^theta u, e^-theta v) - k(u, v)| <= beta||u|| ||v||,
beta <= c/2. Then the operator K of k satisfies ||e^theta K^-1 e^-theta||_{V*->V} <= 2/c and
||e^theta K^-1 e^-theta - K^-1|| <= 2beta/c^2. *Proof.* The form (u, v) -> k(e^theta u, e^-theta v)
has real part >= (c/2)||u||^2 on the diagonal, so its operator e^theta K e^-theta is invertible with
inverse norm <= 2/c (Lax–Milgram in finite dimension); its inverse is e^theta K^-1 e^-theta; the
difference follows from A^-1 - B^-1 = A^-1(B - A)B^-1. ∎

**5.2 Lemma S (scalar estimates on Z).** Under (4.0) and alpha_0 <= a_2(L), for z in Z,

    ||sigma^-2 z|| + ||D_U z||_mass + ||nabla_U D_U z|| <= C_S(L) ||Delta_U z||.

*Proof.* (i) Pillar Poincaré: in a gauge on the pillar's neighbourhood, PX47 puts the
transports within C_L alpha_0 of 1, so |flat mean of z| <= C_L alpha_0 |B|^-1/2 ||z||_B, and the
variance bound gives ||z||_B <= 2 sqrt(d) sigma_B ||D_U z||_B after absorption. (ii) With a scale
weight zeta (kappa = kappa(L) small), summation by parts gives
||zeta^1/2 D_U z||^2 = <zeta Delta_U z, z> + O(kappa) <zeta sigma^-1 |D_U z|, |z|>; by (i) applied with zeta
(nearly constant on pillars), ||zeta^1/2 sigma^-1 z|| <= 3 sqrt(d) ||zeta^1/2 D_U z||, and Cauchy gives
||zeta^1/2 D_U z|| <= 8 sqrt(d) ||zeta^1/2 sigma Delta_U z|| <= 8 sqrt(d) L ||Delta_U z|| for kappa small. Since
xi_b^-2 <= zeta and the bond and site weights are comparable, this bounds the first two terms.
(iii) PX119 on the region (z vanishes near the boundary) gives
||nabla_U D_U z||^2 <= ||d_U D_U z||^2 + ||Delta_U z||^2 + C_L alpha_0 ||D_U z||_mass^2, and d_U D_U z is the
commutator of z with the plaquette holonomy, so ||d_U D_U z|| <= C alpha_0 ||sigma^-2 z||. ∎

**5.3 Theorem 3 (graph estimate, Landau form).** Under (4.0) and alpha_0 <= a_3(L), at
every real regular U, for every fine H,

    ||H||_X^2 <= C_3(L) ( ||d_U H||^2 + ||R D_U^T H||^2 + ||QH||_row^2 ).

*Proof.* P Delta_U P is positive definite on Z (by 5.2(i)), so H = H_P + D_U z with z in Z and
P D_U^T H_P = 0. By PX38, Q D_U z = D_ext Q' z = 0, so Q H_P = Q H. Since Delta_U Z is the range
of R, R D_U^T D_U z = Delta_U z, so Delta_U z = R D_U^T H - R D_U^T H_P and
||Delta_U z|| <= ||R D_U^T H|| + 2||H_P||_X. Theorem 2 for H_P, with
||d_U H_P|| <= ||d_U H|| + C alpha_0 ||sigma^-2 z||, and Lemma S give
||H_P||_X^2 <= 2L^2 C_2 ( ||d_U H||^2 + ||QH||_row^2 ) + 2L^2 C_2 C^2 alpha_0^2 C_S^2 ||Delta_U z||^2.
Insert the bound for ||Delta_U z||, absorb (16 L^2 C_2 C^2 alpha_0^2 C_S^2 <= 1/2), and use
||H||_X <= ||H_P||_X + C_S ||Delta_U z||. ∎

This replaces `a2-curved` §4 on layers. It needs no null identity: the gauge part is
estimated through the curvature commutator, so it holds off shell.

**5.4 The fine precisions.** (a) *Real regular pairs.* By PX118 (inner plaquettes, the same
ones that enter Theorem 3), <h, Delta_U^W h> >= (1 - C_L alpha_0)||d_U h||^2 - C_L alpha_0 ||h||_mass^2. Hence
for alpha_0 <= a_4(L),

    c_W ||h||_X^2 <= <h, G_0^-1 h> <= C_up ||h||_X^2,     c_W = 1/(2C_3),               (5.2)

the upper bound from ||d_U h||, ||D_U^T h|| <= 2||nabla_U h|| and PX113. So G_0 exists and
G_0 > 0 on every separated sequence; this is the positive G_00 that `a3-balaban.md` F3
records as not supplied, now at every real regular background. Neither stationarity nor
the current enters.

(b) *Physical pairs.* At a physical critical U with J = J(U), outline Theorem 1 gives
|J| <= C eps_1 xi^-3, and `a2-curved` §9 gives the multiplier omega = H^T J with
sup_c xi_c^3 |omega_c| <= C_L C eps_1. By PX95, G_1^-1 = S^T beta S + D_U R D_U^T + Q^T a Q =: K_phys with
beta = Delta^W - Delta^(2)[omega] (PX94). For h, S h = h - D_U z' with z' in Z and
Delta_U z' = R D_U^T h (since G' Delta_U z' = z' on Z), so S h is the Landau part of h. By PX118 and
`a2-curved` (8.10),
beta[Sh] >= (1 - C alpha_0)||d_U Sh||^2 - C_L (alpha_0 + eps_1)||Sh||_mass^2, and Theorem 3 applies to Sh
(R D_U^T Sh = 0, Q Sh = Qh). With ||h||_X <= ||Sh||_X + C_S ||R D_U^T h||, this gives

    <h, K_phys h> >= c_K ||h||_X^2,   c_K = min(1, c_W)/(2(1 + C_S^2)),                (5.3)

for alpha_0, eps_1 <= a_5(L). This is `a2-curved` (10.1) and (12.5) on arbitrary separated
layers, in the weighted norm.

(c) *A right inverse of the rows with an energy bound.* Place two-moment bumps (as in
Corollary 1') at every level in an endpoint pillar of each row, the inner one for outward
rows. A bump of level j is read only by the incident level-j rows (exactly, by the moments)
and by level-(j+1) outward rows whose outer block contains its pillar, as in `a2-curved`
§9. So Q E^0 = 1 + N + T with N strictly raising the level by one,
||Xi^-1 N Xi|| <= C L^-1 in row norm (weights at most L^-4, sum at most one, against
xi_{j+1}^2 = L^2 xi_j^2: outline mechanism (d)), and ||T|| <= C_L alpha_0 from (4.1). For L large and
alpha_0 small the Neumann series gives E = E^0 (1 + N + T)^-1 with Q E = 1 and
||E psi||_X <= K_E(L) ||psi||_row. With (5.2) this gives the row Gram bound: for psi on rows,
<psi, Q G_0 Q^T psi> >= c_W C_up^-2 K_E^-2 ||psi||_{row*}^2, where ||psi||_{row*}^2 = sum_c xi_c^6 |psi_c|^2 is the
dual norm for the physical row pairing. ∎

## 6. The coarse form and A on the next fibre

Top units: xi_k = 1. Let iota inject the level-k rows touching Omega_{k+1}; they are interior
rows at distance > rho from Omega_k^c, and by 2.3 the reduced datum is the identity on them to
second order (PX100), so the outward datum jets do not enter A.

**Lemma F (coarse value bound).** Let F be a real symmetric form on fine fields with

    F[h] >= (1 - delta)(||d_U h||^2 + ||R D_U^T h||^2) - delta ||h||_X^2,    F + Q^T a Q >= c ||·||_X^2.

Then for b = iota b,
<b, [(Q(F + Q^T a Q)^-1 Q^T)^-1 - a] b> = min_{Qh = b} F[h] >= c_0(L) ||d_V b||^2 - C_L (delta + alpha_0) ||b||^2
once delta, alpha_0 <= a_6(L). *Proof.* The equality is completion of the square for the
positive form F + Q^T a Q on the affine fibre (`a2-curved` §6). On the fibre, Theorem 3 gives
||h||_X^2 <= C_3 (||d_U h||^2 + ||R D_U^T h||^2 + ||b||^2), so for delta(1 + C_3) <= 1/2,
F[h] >= (1/2)(||d_U h||^2 + ||R D_U^T h||^2) - delta C_3 ||b||^2. The comparison `a2-curved` (11.2) is local: on the
dependence cube of a coarse plaquette near Omega_{k+1} (inside L_k, far from every seam),
d_V Q h = T_n d_U h + R h with ||T_n|| <= 1 and ||R h|| <= C_L alpha_0 ||h||; summing with bounded
overlap, ||d_V b||^2 <= C_L (||d_U h||^2 + alpha_0^2 ||h||_X^2)
<= C_L(1 + C_3)(||d_U h||^2 + ||R D_U^T h||^2) + C_L C_3 alpha_0^2 ||b||^2. Combine, with
c_0 = 1/(2 C_L (1 + C_3)). ∎

**Lemma N (next fibre, including the boundary of Omega_{k+1}).** There are A'_L and
eps'_L > 0 such that if every level-k plaquette near Omega_{k+1} has |V_p - 1| <= eps'_L, then
for every B on the level-k bonds touching Omega_{k+1} (zero elsewhere) with K_V B = 0 on all
rows of Gamma_{k+1}, interior and outward,

    ||B||^2 <= A'_L ( ||d_V B||^2 + ||G_V B||^2 ),

with d_V over all level-k plaquettes and G_V over the internal contours of the blocks of
Omega_{k+1}. *Proof.* `a2-curved` §5 proves this from local injectivity on the 3^4-block
rectangle around each block, compactness of the unit sphere of that finite space, a
block-constant gauge and the finite-stencil perturbation. Only injectivity depends on which
of the 81 blocks lie in Omega_{k+1}; there are finitely many such patterns, including faces,
edges, vertices and contacts of the cubes of Omega_{k+1}. Fix one, and let B be flat-null: zero
curl, zero internal contour sums, zero rows. Inside each block of Omega_{k+1} the internal bonds
vanish (§5 there). A bond touching Omega_{k+1} is either internal to such a block or crosses a
face of it. If the face is shared with a block B_2 outside Omega_{k+1}, the internal bonds of
B_2 are not variables (they touch no site of Omega_{k+1}), so each face plaquette equates two
neighbouring crossing values; the transverse face grid is connected; every segment of the
outward row crosses the face once and otherwise uses internal bonds; so the row equals the
common value, which therefore vanishes. Faces between two blocks of Omega_{k+1} are the
interior case of §5 there. So the flat map is injective on every pattern, and A'_L is the
largest of finitely many constants. ∎

The next-level plaquettes obey |V_p - 1| <= C_L alpha_0 by `a2-curved` (8.4)–(8.5), so Lemma N
applies once alpha_0 <= eps'_L/C_L.

**Theorem 4 (A2 on separated layers at physical critical backgrounds).** Under (4.0)
and alpha_0, eps_1 <= a_7(L), at every physical critical pair on every separated sequence of depth
k+1, with V block axial on Omega_{k+1},

    <u, A u> >= c_L ||u||^2,   c_L = min(c_0, 1)/(2A'_L),

and the same for chi_Y A chi_Y on every conditioning set Y.

*Proof.* Take F = S^T beta S + D_U R D_U^T, so F + Q^T a Q = K_phys = G_1^-1 (PX95), coercive by
(5.3). For the first hypothesis of Lemma F write S h = h - D_U z' as in 5.4(b):
||d_U D_U z'|| <= C alpha_0 ||sigma^-2 z'|| <= C alpha_0 C_S ||R D_U^T h|| and ||Sh||_X <= (1 + 2C_S)||h||_X, so
F[h] = beta[Sh] + ||R D_U^T h||^2 satisfies it with delta = C_L (alpha_0 + eps_1). Lemma F bounds
the compression of Delta_k + a - E^(2) to the active rows below by
c_0 ||d_V b||^2 - C_L(alpha_0 + eps_1)||b||^2. At a physical pair H_1^T J = omega (J = Q^T omega and
Q H_1 = 1), so the next-constraint term obeys |<b, E^(2)[omega] b>| <= C_L eps_1 ||b||^2
(`a2-curved` §11, last step: one-step derivative bounds, inverse pivot bound, (9.2)). The
axial gauge Hessian is exactly ||G_V b||^2. Put b = C_V u; then K_V b = 0 and ||b|| >= ||u||, and
Lemma N gives <u, A u> >= [min(c_0, 1)/A'_L - C_L(alpha_0 + eps_1)] ||b||^2. Conditioning is
`a2-curved` (2.1). ∎

This closes the first half of row 90: real A2 on arbitrary separated layers with seams,
non-Lipschitz contacts and outward rows, at physical critical backgrounds, every depth,
uniformly in the regions, the torus and the number of layers.

## 7. The independent current: H^T J without stationarity

Here (U, J) is a real regular pair and J is arbitrary with |J| < gamma_0 xi^-3; U need not be
critical, and its own current J(U) may be large (outline mechanism (e)). It enters nowhere
below.

**7.1 The current correction is a bounded form.** Since R D_U^T A lies in the range of R,
which is Delta_U Z, there is a unique z_A in Z with Delta_U z_A = R D_U^T A, and
G'^-1 z_A = Delta_U z_A because Q' z_A = 0. Hence

    lambda_A := G' R D_U^T A = z_A,      ||sigma^-2 lambda_A|| + ||D_U lambda_A||_mass <= 2 C_S ||nabla_U A||   (7.1)

by Lemma S. Each of the six terms of the bilinear formula for Delta'_pi[J] (outline
L10172–10190) pairs J with a product of lambda_A or lambda_A^+ (a one-bond shift, transported)
and C or D_U lambda_C, or the same with A and C exchanged. With |J_b| <= gamma_0 xi_b^-3 and
xi_b^-3 <= sigma^-2 xi_b^-1 at either end of b, Cauchy and (7.1) give

    |<A, Delta'_pi[J] C>| <= C_7 gamma_0 ||A||_X ||C||_X,     C_7 = 12 C_S (1 + 2C_S).      (7.2)

Only |J| enters: no derivative of the current is taken. The obstacle recorded in
`a3-balaban.md` §14 concerns operator bounds for Delta'_pi, which A2 does not need. With
(5.2), for gamma_0 <= c_W/(2C_7),

    (c_W/2) ||h||_X^2 <= <h, G^-1 h> <= (C_up + C_7 gamma_0) ||h||_X^2,   G^-1 = G_0^-1 - Delta'_pi[J].   (7.3)

So G exists and G > 0 at every real regular pair, on or off shell. Also
||S h||_X <= (1 + 2C_S)||h||_X, since S h = h - D_U lambda_h.

**7.2 Conjugation bounds.** Let theta be tau-Lipschitz (5.1). Then, for tau <= tau_0(L):

(i) *Scalar inverse.* G'^-1 = Delta_U + Q'^T a Q' is local, and the pillar Poincaré with its mean
term gives <lambda, G'^-1 lambda> >= c_s (||sigma^-1 lambda||^2 + ||D_U lambda||^2), c_s = 1/(8d + 2). By (5.1) its
conjugation error is C_L tau in that norm, so Lemma CT applies to G'. Applied with the two
scale weights sigma^{±1} (made slow as in 5.1), it also gives the scale-invariant bounds
||sigma^-2 G' g|| + ||G' sigma^-2 g|| <= C ||g||.

(ii) *Normalized site Gram.* Put F = G' Q'^T Xi^-2 (Xi = xi_y on tops) and N = F^T F. Then
||F|| <= C by (i) and the isometry PX33. For the lower bound let E_s put on each pillar a smooth
bump with transported mean one (`a2-curved` §12: interior support, two bounded differences
on the pillar's scale; the identity on bare pillars), so Q' E_s = 1 and
||G'^-1 E_s Xi^2 psi|| <= C_E ||psi|| pillar by pillar. Then
<F psi, G'^-1 E_s Xi^2 psi> = <Xi^-2 psi, Q' E_s Xi^2 psi> = ||psi||^2, so ||F psi|| >= C_E^-1 ||psi|| and
N >= C_E^-2. The conjugated N_theta differs from N by C tau, so N_theta^-1 is bounded, and

    R = 1 - F N^-1 F^T   gives   || e^theta R e^-theta - R || <= C_R tau.                  (7.4)

(iii) *Fine inverses.* The conjugation error of G_0^-1 is <= C_L tau ||u||_X ||v||_X: for Delta^W use the
plaquette form PX114, where the weight varies by O(tau) across a plaquette; for Q^T a Q use (5.1);
for D_U R D_U^T write <R D_U^T(e^theta u), R D_U^T(e^-theta v)> and use (5.1) for D_U^T and (7.4) for R.
For Delta'_pi[J], conjugate lambda = G' R D_U^T factor by factor using (i), (7.4), (5.1); the pairing with
J is a multiplication, unchanged except for the one-bond shift in lambda^+. By Lemma CT and (7.3),

    || e^theta G e^-theta ||_{X*->X} <= 4/c_W,   || e^theta G e^-theta - G ||_{X*->X} <= C_G tau.          (7.5)

(iv) *Row Gram.* W = Q G Q^T obeys <psi, W psi> >= c_Gram ||psi||_{row*}^2, with
c_Gram = (c_W/2)(C_up + C_7 gamma_0)^-2 K_E^-2, by the duality argument of 5.4(c) with G in place
of G_0. With (5.1) for Q and (7.5), W_theta - W = O(tau) from row* to row, and Lemma CT gives
||e^theta W^-1 e^-theta||_{row->row*} <= 2/c_Gram.

**7.3 Theorem 5 (the off-shell multiplier).** Under (4.0), alpha_0 <= a_4(L),
gamma_0 <= c_W/(2C_7), and rho >= rho_1(L) := 8 log L / tau_0(L), at every real regular pair,

    sup_c xi_c^3 |(H^T J)(c)| <= C_omega(L) gamma_0,     H = G Q^T W^-1.

*Proof.* H^T J = W^-1 Q G J, as G and W are symmetric. Fix a row c_0, put
varsigma = tau_0 and theta = -varsigma min(d_B(·, c_0), M) for a cap M; theta is
tau_0-Lipschitz, equals 0 at c_0, and is <= 0. Then
e^theta H^T J = W_theta^-1 Q_theta G_theta (e^theta J), so by 7.2

    xi_{c_0}^3 |(H^T J)(c_0)| <= ||e^theta H^T J||_{row*} <= (2/c_Gram) C_Q (4/c_W) ||e^theta J||_{X*},

and ||e^theta J||_{X*} <= gamma_0 (sum_b eta^4 xi_b^-4 e^{-2 varsigma d_B(b, c_0)})^{1/2} by Cauchy against
||h||_mass. The sum is at most 8 e^{8L varsigma} sum_y e^{-2 varsigma d_B(y, c_0)} over pillar
centres y (a pillar carries at most 4(xi_y/eta)^4 bonds). For the count, a path of d_B-length
<= r from c_0 (layer j) crosses at most 1 + r/rho layers (PX4), so it stays in scales
<= L^{2 + r/rho} xi_j and has physical length <= r L^{2+r/rho} xi_j; a level-i grid has at most
C(1 + r)^4 L^{4(3 + 2r/rho)} points in that ball, since xi_j/xi_i <= L^{1+r/rho}; summing over
at most 3 + 2r/rho levels,
#{y : d_B(y, c_0) <= r} <= C_L (1 + r)^5 L^{8r/rho}. So the sum is at most
C_L sum_m (2 + m)^5 exp[(8 log L/rho - 2 varsigma) m], finite and independent of everything but
L once varsigma rho >= 8 log L. The cap M is removed because nothing depends on it. ∎

The same proof at physical pairs gives back `a2-curved` (9.2), now without the identity
J = Q^T omega.

**7.4 G_1 and H_1^T J.** By Theorem 5 and `a2-curved` (8.10),
|<A, S^T Delta^(2)[H^T J] S A'>| <= C_L C_omega gamma_0 (1 + 2C_S)^2 ||A||_X ||A'||_X, so for
gamma_0 <= a_8(L), G_1^-1 = G^-1 - S^T Delta^(2)[H^T J] S satisfies (c_W/4)||·||_X^2 <= G_1^-1 <= 2C_up. The
conjugation error of S is O(tau) by (i), (7.4), (5.1), and that of Delta^(2)[omega] by the
coefficient bound `a2-curved` (8.3) and (5.1) (row-scale carriers). Repeating 7.2(iv) and
Theorem 5 with G_1 gives sup_c xi_c^3 |(H_1^T J)(c)| <= C_omega1(L) gamma_0.

**7.5 Theorem A (A2 on separated layers at every real regular pair).** Under (4.0), with
alpha_0, gamma_0 <= a_*(L) := min of the ceilings above and rho >= rho_*(L) := max{16RL, rho_1,
2 log L/kappa}, the conclusion of Theorem A in §1 holds. *Proof.* Take
F = G_1^-1 - Q^T a Q = Delta^W + D_U R D_U^T - Delta'_pi[J] - S^T Delta^(2)[H^T J] S. By PX118, (7.2) and 7.4,
F[h] >= (1 - C_L alpha_0)||d_U h||^2 + ||R D_U^T h||^2 - C_L(alpha_0 + gamma_0)||h||_X^2, and
F + Q^T a Q = G_1^-1 is coercive, so Lemma F bounds the compression of
(Q G_1 Q^T)^-1 - a to the active rows by c_0 ||d_V b||^2 - C_L(alpha_0 + gamma_0)||b||^2. The term
E^(2)[H_1^T J] is bounded by C_L C_omega1 gamma_0 ||b||^2 (as in Theorem 4, with 7.4 in place of
(9.2)), the axial gauge Hessian is ||G_V b||^2, and Lemma N finishes as in Theorem 4. All
inverses in the definition of A exist (7.3, 7.4, 7.2(iv)); G_0, G, G_1 > 0. ∎

The constants c_L, a_*, M_* = 8RL/c_g and rho_* depend on L only. The ceilings precede M_1.
