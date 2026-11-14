lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T00:15Z

# A3: uniform multiscale background response (queue row 77)

Pinned at commit `7cd8b4f0f`, branch `claude/ym4d-hard-route`. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work: not
gated, not an audit, no status.

Sources read: outline `YM4_sketch_500.tex` at `31a47c543775` (SHA-256 matches
`library/sa-2.8.md`), (1b) l. 9583-9800 and A3 l. 3864-3896; Dimock arXiv
1712.10029 (source, Section 3, l. 2004-3160 of `QEDjmp.tex`, not committed);
`library/lit-large-field.md` 3, `sa-2.8.md` 9, `rel-phi-c.md`,
`seam-nonlinear-c.md` 4, `fibre-propagator.md`, `fd-local.md` 5, 8,
`curl-poincare-exterior.md` Lemma 1, `lattice_gehring_hls.md`.

Credit: T. Balaban (CMP 95, 96, 98, 99, 102) for the multiscale averages, the
gauges and the statement; J. Dimock (arXiv 1712.10029) for the exposition used
to locate it; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for the outline's (1b) setting, the straightened average and its
factorisation, the Landau pair and the formulation of A3; the block-diagonal
gauge term is from `fibre-propagator.md`, Example E and Lemmas 1, A, A2 from
`rel-phi-c.md`, the Green's function bound from `lattice_gehring_hls.md`.
Kill test: `checks/a3/fl_killtest.py` (7b), PASS.

Status: finished 2026-11-02. **Flat linear statement PROVED (Theorem FL,
hand proofs: curvature and potential in local L^2, curvature pointwise by
Lemma LR). Example E question ANSWERED at the flat linear
level (Theorem E: in the local Landau gauge the contour averages and the (REL-D)
shell sums are bounded uniformly in depth). Curved linear response (Theorem
CL) derived at the level of each step from one-step inputs (analyticity and
Cauchy bounds of the one-step straightened average, an implicit-function step
for the straightened gauge directions, |omega_0| <= C eps): the depth uniformity
comes from the exact factorisation of the straightened average (6.1). (L) of
`sa-2.8.md`: implication from CL, uniqueness (U), and, for one plaquette, local
regularity (LR).**

## 0. What Dimock 3.7 actually contains (finding, before any port)

Dimock's Section 3.7 is a summary, not a proof. It opens "We quote some results
... from Balaban [Bal84a], [Bal84b], [Bal85b]". The three load-bearing steps are
quoted: the local inverse bounds for G_{k,Omega}(box) ("the global results of
[Bal84a]"), the case of a box crossing a seam ("requires some rather extensive
modifications. See [Bal84b] for the full treatment"), and the commutator bound
(day0) ("One shows that [Bal84b]"); the local inverses N_{k,Omega}(box) likewise
("see Balaban [Bal84b] for details"). So porting 3.7 to d = 4 would port
citations, not a proof. In the source fetched (the version of 2020-03-03) the
kernel bounds that `lit-large-field.md` calls (301)-(303) are labelled
`standard3`, `standard3.5`, `standard4` (equations 318-320 by my count).

Instead, Section 2 below proves the flat linear statement directly, by a route
that needs no random walk: a local curl-Poincare inequality on boxes, a patching
of local gauges normalised by pillar means, an explicit local right inverse of
the multiscale average, and a hole-filling (Widman) iteration. The operators,
the multiscale geometry and the statement are Balaban's (CMP 95, 96), in the
form Dimock writes (Lemma 14 and (292) of the source); the use of a
block-diagonal gauge term follows `library/fibre-propagator.md`.

## 1. Setting and the flat statement

**Units and lattice.** Fine units: the fine lattice is a torus of Z^4 with unit
spacing (multiply lengths by eta = L^-k for the outline's level-k units; the
energy below is dimensionless in d = 4 and does not change). L odd, L >= 3,
s_j := L^j. Level-j sites are s_j Z^4, the level-j block of a level-j site y is
B^j(y) := y + {-m_j, ..., m_j}^4, m_j := (s_j - 1)/2. Blocks nest.

**Sequence (outline (1b)(i), with Balaban's averages).** Omega_0 ⊃ ... ⊃ Omega_k,
Omega_j a union of level-j blocks, Omega_(k+1) = empty, separated:
dist_inf(Omega_j^c, Omega_(j+1)) > rho s_j with rho >= 3L. (The outline's cubes of
side M xi_j and gap R_1 M are a special case.) Layer j := Omega_j \ Omega_(j+1);
tops of level j = level-j sites in layer j; their blocks are the *pillars*,
which partition Omega_0; xi_P := s_j is the side of a pillar P of layer j
(layer-0 pillars are single sites). Gamma_j := level-j bonds with both ends in
Omega_0, an end in Omega_j and none in Omega_(j+1); **B** := union of the Gamma_j
(no inward bonds, as in the outline). For c = (y, y + s_j e_mu) in Gamma_j,

    q_c(A) := s_j^-4 sum_(x in B^j(y)) A(Gamma_(x, x + s_j e_mu)) = sum_b rho_c(b) A(b),

the straight path average (Dimock's Q_k, (moonshine); the outline's straightened
average Q^st at V_0 = 1, see 3.1). Here rho_c(b) = s_j^-4 tau(b_mu - y_mu) on
direction-mu bonds b with transverse position in y_perp + {-m_j..m_j}^3, with the
tent tau(u) = s_j - |u - m_j| for -m_j <= u <= 3 m_j, peaked at the face bond
(u = m_j). So ||rho_c||_2^2 <= (2/3) s_j^-2 and the support of rho_c lies in the
*double block* D(c) := B^j(c_-) u B^j(c_+). At level 0, q_c(A) = A(c).

**Problem.** E(A) := sum_(p ⊂ Omega_0) |dA(p)|^2, A real on the bonds of Omega_0
(one colour component: at V_0 = 1 the linearisation of SU(2) Wilson action and
averages is three copies of this). Datum B on **B**; A_B := a minimiser of E on
{q(A) = B}. *Restricted gauges* (Balaban): lambda with Av_P lambda = 0 on every
pillar P. Then q_c(d lambda) = Av_(B(c_+)) lambda - Av_(B(c_-)) lambda = 0 for every
c in **B**, because the block of an outer end is a union of pillars of the next
finer layer. *Distance*: d_B(x, x') := inf over paths of sum_j s_j^-1 (fine length
in layer j), the outline's d_**B** in fine units; it is 1/s_j-Lipschitz along
a fine bond of layer j.

**Theorem FL (flat multiscale response).** There are m(L) > 0 and C(L), free
of k, of the torus, of the regions, of the support S of B and of B, such that,
with psi(x) := d_B(x, union_(c in S) D(c)):

(a) (curvature) for every t >= 0,
    sum_(p : psi(p) >= t) |dA_B(p)|^2 <= C(L) e^(-2 m t) ||B||^2,  ||B||^2 := sum_c |B(c)|^2;

(b) (potential) there is a restricted gauge in which A~ := A_B - d lambda obeys,
    for every pillar P,
    xi_P^-2 ||A~||^2_(L^2(P)) <= C(L) e^(-2 m psi(P)) ||B||^2.

dA_B is unique. Inside one layer every constant is absolute; only the seam
transitions bring in L (Lemma P, case (c)). In the outline's units (a) and (b)
say: the response to a unit datum e at a bond c has, over each top y, energy in
its pillar at most C e^(-2m d_B(y, y_c)) |e|^2 and potential in L^2 of the
pillar, in local units, of the same size. This is Theorem 4 of (1b) at
V_0 = 1, B = 0, in local L^2 form; the pointwise curvature form follows by
Lemma LR (5.4), which has no depth in it.

## 2. Four lemmas (discharged, hand proofs)

From here on rho >= 3L^2 (used only to keep each cube D_P below inside Omega_0
and meeting at most two consecutive layers). For a pillar P of layer j let D_P
be the cube of side 5 s_(j+1) = 5L xi_P with the centre of P. Norms are plain
l^2 sums over the fine bonds or plaquettes of the set named.

**Lemma 1 (curl-Poincare on a box; after `curl-poincare-exterior.md` Lemma 1,
Iwaniec-Lutoborski averaging).** On a box D of the fine lattice with sides at
most l, every 1-form A has a scalar omega with ||A - d omega||_D <= 1.23 l ||dA||_D.

*Proof.* Gamma(y, x): the path from y to x changing coordinates in the order
1, 2, 3, 4. omega(x) := Av_(y in D) A(Gamma(y, x)). For b = (x, x + e_i),
A(b) - d omega(b) = Av_y A(lambda_y), lambda_y = Gamma(y, x) b Gamma(y, x + e_i)^-1.
The two paths agree up to the point a = (x_1..x_i, y_(i+1)..y_4); after it they
run parallel at distance one in direction i, so lambda_y bounds a strip S_y(b)
of at most 3l plaquettes and |A(lambda_y)| <= sum_(S_y(b)) |dA|. Cauchy-Schwarz:
|A - d omega|^2(b) <= 3l Av_y sum_(p in S_y(b)) |dA(p)|^2. A plaquette p in the
(i, j) plane, i < j, at base z lies in S_y(b) only if x agrees with z in the
coordinates < j, y agrees with z in the coordinates > j, and the step of z_j
lies between y_j and x_j: at most |D| l/2 pairs (x, y). Summing,
||A - d omega||^2 <= 3l (l/2) ||dA||^2. QED

**Lemma 2 (scalar Poincare).** On a box D with sides at most l,
||f - Av_D f||_D <= 1.42 l ||df||_D. *Proof.* |f(x) - f(y)|^2 <= 4l sum_(Gamma(y,x)) |df|^2,
each bond lies on at most |D| l/2 of the paths, and
sum_x |f - Av f|^2 <= |D|^-1 sum_(x,y) |f(x) - f(y)|^2. QED

**Lemma 3 (links).** If omega is defined on D(c), c in Gamma_j, then
Av_(B(c_+)) omega - Av_(B(c_-)) omega = q_c(d omega), hence

    |Av_(B(c_+)) omega - Av_(B(c_-)) omega - q_c(A)| <= 0.82 s_j^-1 ||A - d omega||_(D(c)).

*Proof.* The first identity is the telescoping of d omega along each line; the
bound is Cauchy-Schwarz with ||rho_c||_2^2 <= (2/3) s_j^-2. QED

**Lemma T (local right inverse).** There is a linear T with q(T beta) = beta for
every datum beta, E(T beta) <= C_T ||beta||^2 with C_T absolute, and T beta
supported in the union of D(c) and of the double blocks of the outward bonds
of the next coarser level that meet D(c), over c in supp beta.

*Proof.* Level j >= 1, c = (y, y + s e_mu), s = s_j, m = m_j, W := floor((s-1)/4).
Profile along mu, in w := b_mu - y_mu - m (w = 0 is the face): g(0) = 1,
g(+-w) = 1 for 1 <= w <= W, g(+-w) = -(W+1)/(3W+1) for W < w <= 2W, else 0.
Each half has zero first moment, sum_(w>0) w g = 0, and sum g >= 1 + W.
Transverse profile h(z_perp) = prod_nu (m + 1 - |z_nu - y_nu|)/(m + 1) on the
transverse box. phi_c := N_c g h on direction-mu bonds, N_c chosen so that
q_c(phi_c) = 1. On the support of g the three rows along the mu-line have
weights s^-4 (s - |w|), s^-4 max(w, 0), s^-4 max(-w, 0) (the tents of c and of
its two neighbours); the zero half moments give q_(c +- s e_mu)(phi_c) = 0 and
q_c(phi_c) = s^-3 N_c (sum h)(sum g), so N_c <= 8/(1 + W). Rows of other
directions read no mu-bond; transverse neighbours have disjoint boxes. So
q_(c')(phi_c) = delta_(cc') for all level-j rows. The curl of a direction-mu
field sees only its transverse differences, |d phi_c| <= N_c/(m+1), on at most
3 s (s+2)^3 plaquettes, so E(phi_c) <= 12288 x 7. Level 0: phi_c := 1 on c.

*Seams.* For an outward bond c' in Gamma_(j+1) (outer end z in layer j) use the
one-sided profile g(w) = 0 for w > 0 (support on the side of the coarse
pillar, inside Omega_(j+1)), with the same zero moment on w < 0; then no
level-j row reads phi_(c'), since Omega_(j+1) carries no level-j row. A coarse
outward row reads a fine phi_c (c in Gamma_j near B(z)) with
|q_(c')(phi_c)| <= s_(j+1)^-3 ||phi_c||_1 <= 24 L^-3, and at most 4 L^4 fine bumps
meet one coarse row. No other cross-level reading occurs: rows of interior
coarse bonds lie in Omega_(j+1), and bumps of level j + 1 near Omega_(j+2) lie
far from Omega_(j+1)^c. So the system is triangular with one step:
T beta := sum_c beta(c) phi_c + sum_(c' outward) beta~(c') phi_(c'),
beta~(c') := beta(c') - sum_(c fine) beta(c) q_(c')(phi_c), |beta~ - beta| <= 48 L^-1 ||beta||_loc,
and q(T beta) = beta. At most 8 bumps meet a plaquette, so
E(T beta) <= 8 x 86016 (1 + 48 L^-1)^2 ||beta||^2 <= 10^7 ||beta||^2. QED

**Lemma P (normalised patching).** Put, for touching pillars P, P',
Theta(P, P') := ||dA||_(D_P u D_P') + max{|q_c(A)| : D(c) ⊂ D_P u D_P'}. There is a
restricted gauge lambda (Av_P lambda = 0 for every pillar P) such that for every
pillar P_0

    xi_(P_0)^-2 ||A - d lambda||^2_(P_0) <= C_P(L) max_(P, P' touching P_0 or = P_0) Theta(P, P')^2,

with C_P(L) <= 10^16 L^12, free of k, the regions, the torus and A.

*Proof.* (i) *Local gauges.* For each pillar P of a layer >= 1, Lemma 1 on D_P
gives omega_P with a_P := ||A - d omega_P||_(D_P) <= 6.2 L xi_P ||dA||_(D_P);
subtract a constant so that Av_P omega_P = 0. For a layer-0 pillar (a site)
put omega_P := 0.

(ii) *Pillar means of a local gauge (chains).* Let P, P' touch, xi_P <= xi_P'.
Then P ⊂ D_P', and D_P' meets only two consecutive layers. Inside D_P' there is a
chain from P' to P of at most 40 L links, each a row c with D(c) ⊂ D_P': rows
between pillars of one layer; outward rows from a coarse pillar to a level-(j+1)
block of layer j, whose mean is the mean of its L^4 pillars; and, inside such a
block, at most 8L rows between its pillars (the chain never enters the interior
of a coarse pillar, where no row of the finer level exists; this is why D_P'
has side 5 s_(j+1), so that the coarse detour around a corner fits). By Lemma 3,
each link changes the mean of omega_P' by at most 0.82 s_c^-1 a_P' + |q_c(A)|
<= 5.1 L^2 ||dA||_(D_P') + |q_c(A)|. Since Av_P' omega_P' = 0,
|Av_P omega_P'| <= 204 L^3 Theta(P, P').

(iii) *Transitions.* delta := omega_P - omega_P' on Q := P^(+ xi_P/2) ⊂ D_P n D_P'
(the box of side 2 xi_P about P). ||d delta||_Q <= a_P + a_P' <= 8.3 L^2 xi_P ||dA||.
Lemma 2 on Q and on P, and Av_P delta = -Av_P omega_P', give
||delta||_Q <= 900 L^3 xi_P^2 Theta(P, P').

(iv) *Partition of unity.* w_P := (1/4) min of the sides of P and of the
pillars touching P; theta_P := max(0, 1 - dist_inf(., P)/w_P); chi_P := theta_P / sum theta.
supp chi_P meets only P and pillars touching P; at most 32 of the chi are
non-zero at a point; |d chi_P(b)| <= 530 L / xi(b), xi(b) the side of the
pillar containing b_-. lambda_0 := sum_P chi_P omega_P. With P_b the pillar of b_-,
the discrete product rule and sum_P d chi_P = 0 give

    (A - d lambda_0)(b) = sum_P chi_P(b_+) (A - d omega_P)(b) - sum_P (d chi_P)(b) (omega_P - omega_(P_b))(b_-).

Every term involves P_b and a pillar touching it, so (i) and (iii) bound
||A - d lambda_0||_(P_0) by sums over pillars touching P_0, at most 81 L^4 of them.

(v) *Exact restriction.* lambda := lambda_0 - sum_P (Av_P lambda_0) b_P, with b_P the
product bump on P of mean one, |b_P| <= 16, Lipschitz 32/xi_P, zero off P.
|Av_P lambda_0| = |Av_P sum_P' chi_P' (omega_P' - omega_P)| <= xi_P^-2 sum ||delta||_Q
<= 900 L^3 x 81 L^4 max Theta, and ||d b_P|| <= 1.2 x 10^3 xi_P. On a layer-0 site the
bump is the indicator, so lambda vanishes there. Collecting (i)-(v) with the
counts above gives the bound with C_P(L) <= 10^16 L^12 (crude). QED

The constant is poor and only its independence of depth, regions and volume
matters. Inside one layer, with no seam within D_P', the chains have absolute
length and every L above becomes an absolute constant.

## 3. Proof of Theorem FL (discharged, given Section 2)

*Existence, uniqueness of dA_B.* {q(A) = B} is a non-empty affine space (Lemma
T), E is a convex quadratic bounded below, so a minimiser exists in finite
dimension. If A_1, A_2 minimise, E((A_1 + A_2)/2) = (E(A_1) + E(A_2))/2 - E(A_1 - A_2)/4,
so d(A_1 - A_2) = 0. And E(A_B) <= E(T B) <= C_T ||B||^2.

*Geometry in d_B.* A pillar has d_B-diameter at most 4; the set
N(P_0) := union of D_P, D_P' over P, P' touching or equal to P_0, has d_B-diameter
at most c_N := 60 L^2 (it lies in two consecutive layers, the finer one costing
at most L times the coarser). So Lemma P at P_0 reads only plaquettes and rows
within d_B-distance c_N of P_0.

*Cut-off.* Fix t > c_0 := 3 c_N and let chi := phi(psi), phi = 1 on (-inf, t],
linear on [t, t + 1], 0 on [t + 1, inf). |d chi(b)| <= 1/s_j on a bond of
layer j. Let A~ := A_B - d lambda with lambda from Lemma P. The zone
Z := {plaquettes and rows within d_B-distance c_N of {t <= psi <= t + 1}} has
psi >= t - c_N > 0, so B = 0 on its rows and q_c(A~) = q_c(A_B) = 0 there
(restricted gauges keep every row).

*Competitor.* beta(c) := q_c(chi A~) for the rows c meeting {t < psi < t + 1}, else 0,
and A' := chi A~ - T beta. On rows inside {chi = 1}, q(A') = q(A~) = B; on rows in
{chi = 0}, q(A') = 0 = B; on the rows of beta, q(A') = beta - beta = 0. So A' is
admissible, and dA' = dA_B where chi = 1 and T beta = 0, dA' = 0 where chi = 0
and T beta = 0. Off the zone nothing else happens, so E(A_B) <= E(A') gives

    E(A_B; psi > t + 1 + c_N) <= E(A'; Z).                                    (3.1)

*Zone bound.* With (chi A~)(b) := chi(b_-) A~(b), on a plaquette p of layer j,
|d(chi A~)(p) - chi(x_p) dA~(p)| <= (2/s_j) sum_(b in p) |A~(b)|; and
|beta(c)| = |q_c((chi - chi(x_c)) A~)| <= 0.82 ||xi^-1 A~||_(D(c)), since
0 <= chi <= 1 and xi <= s_c on D(c). By Lemma T and Lemma P (the energy and
rows it reads are within c_N of Z, where B = 0),

    E(A'; Z) <= 4 E(A_B; Z) + 384 sum_(P meets Z) xi_P^-2 ||A~||^2_P + 2 C_T ||beta||^2
             <= C_1(L) E(A_B; Z^+),   C_1(L) := 4 + 10^10 C_P(L),                (3.2)

Z^+ := plaquettes within d_B-distance 2 c_N of {t <= psi <= t + 1}.

*Iteration.* f(t) := E(A_B; psi > t). By (3.1), (3.2), with Delta := 1 + 6 c_N,
f(t + 1 + 3 c_N) <= C_1 (f(t - 2 c_N) - f(t + 1 + 2 c_N)) <= C_1 (f(t - 2c_N) - f(t + 1 + 3c_N)),
so f(t' + Delta) <= theta f(t'), theta := C_1/(1 + C_1), for every t' >= c_N. Hence

    f(t) <= theta^-2 e^(-2m t) E(A_B) <= theta^-2 C_T e^(-2m t) ||B||^2,
    m := log(1 + 1/C_1) / (2 Delta)  (about 1/(10^11 C_P(L) L^2)).

This is (a). (b): Lemma P with the bound (a) on N(P), and |B(c)| entering
Theta only for P within c_N of S. QED

**What this settles.** The flat linear response of (1b) is exponentially local
in d_B at a rate depending on L alone, with constants free of the depth k, the
number and shape of the regions (no condition on connectivity, pinches or
corners: the patching is local and the zero means kill every flat
non-exact field), and the volume. Inside a layer the rate is absolute; the
L-dependence comes only from seam transitions (Lemma P (ii)). No Fourier
analysis, no random walk, no local inverse on a box is used.

## 4. The gauge part, and weighted coercivity with a local gauge term (discharged)

The curved case (Section 5) cannot use a gauge-invariant energy: at a curved
background D_U D_U lambda = [F, lambda] is not zero, so local energies change
under gauge. It needs a gauge-fixed functional that is a sum of local terms.
Following `fibre-propagator.md`, use the block-diagonal gauge term. Let Pi be
the orthogonal projection of scalars on Omega_0 onto ran Pi := {lambda : Av_P lambda = 0
for every pillar P} (on a pillar, lambda -> lambda - Av_P lambda; zero on layer 0).

**Lemma S (the scalar gauge problem).** For data f (sites), g (bonds), let
lambda in ran Pi minimise F(lambda) := ||d lambda||^2 - 2<lambda, f> + 2<d lambda, g>
over ran Pi (equivalently Pi Delta lambda = Pi f - Pi delta g). Then

(i) ||d lambda|| <= 1.42 (sum_P xi_P^2 ||f||_P^2)^(1/2) + ||g||;

(ii) with psi_S := d_B(., supp f u supp g): ||d lambda||^2_(psi_S > t) <= 2 x 10^7 e^(-2 m_s t) ||d lambda||^2,
     m_s := 1/(7 x 10^8), an absolute rate;

(iii) if rho >= 8 (log L)/m_s, then
     sum_P xi_P^-2 ||d lambda||_P^2 <= C_S(L) (sum_P ||f||_P^2 + sum_P xi_P^-2 ||g||_P^2),  C_S(L) <= 10^90 L^6.

*Proof.* (i) Test the equation with lambda; Lemma 2 on each pillar gives
||lambda||_P <= 1.42 xi_P ||d lambda||_P because Av_P lambda = 0.
(ii) Hole-filling, as in Section 3, with the competitor
lambda' := chi lambda - sum_P m_P b_P, m_P := Av_P(chi lambda), b_P the bump of Lemma P (v).
lambda' lies in ran Pi, equals lambda where chi = 1 on a whole pillar and 0
where chi = 0, so F(lambda) <= F(lambda') gives ||d lambda||^2 beyond the zone at most
||d lambda'||^2 on it. |m_P| <= xi_P^-2 ||lambda||_P and ||d b_P||^2 <= 1.3 x 10^6 xi_P^2,
so with Lemma 2 on pillars, ||d lambda'||^2_Z <= 10^7 ||d lambda||^2_(Z+), Z+ within d_B-distance 9
of the zone. *The smooth bump is what avoids a trace*: correcting the pillar
means with indicators would put |m_P| on the ~xi_P^3 face bonds of each
pillar and cost a factor xi_P. Iterating with step 19 gives (ii).
(iii) Split the data by pillars, (f, g) = sum_P' (f_P', g_P'), and use (i), (ii)
for each piece: xi_P^-1 ||d lambda||_P <= C sum_P' e^(-m_s d_B(P, P')) (xi_P'/xi_P) beta_P',
beta_P' := ||f||_P' + xi_P'^-1 ||g||_P'. Schur test for the kernel
e^(-m_s d) xi_P'/xi_P: pillars of the same layer within d_B-distance n number at
most (2n + 1)^4; pillars of the next finer layer within n of a coarse one at
most C L^3 n^4, with ratio 1/L; of the next coarser layer at most C n^4, with
ratio L; i layers away, ratio at most L^i at distance at least (i - 1) rho, which
the separation beats. Both Schur sums are at most C L^3 m_s^-5. QED

**Lemma C (flat coercivity with the local gauge term).** If rho is as in Lemma S
(iii), then for every A in ker q,

    sum_P xi_P^-2 ||A||_P^2 <= C_C(L) (||dA||^2 + ||Pi delta A||^2),   C_C(L) <= 2 C_S(L) (1 + C'_P(L)),

with the sharp local weight xi^-2 and C'_P(L) := 81 L^4 C_P(L).

*Proof.* Lemma P gives A = A~ + d lambda with lambda in ran Pi and
sum_P xi_P^-2 ||A~||_P^2 <= C'_P ||dA||^2 (B = 0). Then lambda is the minimiser of Lemma S with
f := Pi delta A, g := A~ (both sides give Pi Delta lambda = Pi delta A - Pi delta A~, and Pi Delta Pi
is positive definite on ran Pi). Lemma S (iii) bounds the weighted norm of
d lambda; add. QED

So the saddle-point operator Sad := [[delta d + d Pi delta, q^T], [q, 0]] of the
flat problem is invertible on the weighted graph norm
||A||_X^2 := sum_P xi_P^-2 ||A||_P^2 + ||dA||^2 + ||Pi delta A||^2 times l^2(**B**), with a bound
depending on L only: coercivity on ker q is Lemma C, inf-sup is Lemma T
(||T beta||_X <= C ||beta||, the bumps having ||xi^-1 phi_c|| and ||Pi delta phi_c|| bounded as
well), and |q_c(A)| <= 0.82 ||xi^-1 A||_(D(c)) (Lemma 3) gives boundedness. Its
solution at datum (0, B) is the minimiser A_B in the *local Landau gauge*
Pi delta A = 0 (test with d mu, mu in ran Pi: Pi Delta Pi is invertible). This is the
gauge of Theorem F in `fibre-propagator.md`. Balaban's gauge R delta A = 0 is
reached from it by d mu, mu in ran Pi with Pi Delta^2 Pi mu = -Pi Delta delta A, a
fourth-order analogue of Lemma S that is not written here (label: gap, not
needed below).

## 5. Example E and the gauge: contour averages are bounded in the local Landau gauge (flat linear: discharged)

**5.1 Where Example E lives.** At V_0 = 1 the outline's actual average M has
the linearisation K_M = Q_path - d' Phi (`rel-phi-c.md` 2), and its restricted
gauges are lambda = 0 at the nodes (G^res). The straightened average of the
Landau pair is Q^st = Q_path (Section 1), with restricted gauges of pillar mean
zero, and the two charts differ by the site factors: the outline's Theorem 3
has u_B v_j[H] = 1 at the tops, v_j = exp(block means of contour variables),
so at linear order log u(y) = -Phi(H)(y), the contour average of the Landau
potential at the top. Example E is a G^res gauge direction (lambda_E = 0 at the
nodes), so it lies in the kernel of K_M and costs no energy; what it shows is
that K_M is not bounded on the natural norm. Scaling check (constants not
tracked): with mu := a sum over the even tops y of a smooth radial version of
1 - phi_y (logarithmic profile, radius R ~ B/4), theta := d mu has dtheta = 0,
||xi^-1 theta||^2 ~ a^2/log^2 B and ||Pi delta theta||^2 = ||Pi Delta mu||^2 ~ a^2/log B per even
block, while Phi(theta) is about a at even tops and 0 at odd ones, so
|K_M theta(c)| ~ a on the coarse bonds between them: ||K_M|| >= c (log B)^(1/2) from
the graph norm X to l^2, uniformly in nothing. (A sup-norm radial profile
does not work here: its second differences on the edges of the sup-spheres are
first order and give ||Delta mu||^2 ~ a^2 R/log^2 R.) So a saddle point in the
M-chart cannot have a depth-free bound; in the straightened chart
|q_c(A)| <= 0.82 ||xi^-1 A||_(D(c)) (Lemma 3). That is the reason for Balaban's
straightening, and it moves the contour averages into the gauge factor at the
tops, where they must be bounded separately. Theorem E says they are.

**Theorem E (flat linear).** Single lattice of depth n (one layer, pillars =
top blocks of side B = L^n, rows of level n only, as for the class in (REL)).
Let A_L be the minimiser of Section 1 in the local Landau gauge (Pi delta A_L = 0),
for any datum. For every top centre y, with N_y := the 3^4 top blocks about y,
H := B A_L in top normalisation and Lemma A's annuli A_j(y),

    sum_(j=1)^n ||H||_(L^4(A_j(y))) + |Phi_n(A_L)(y)| <= C(L) ( ||dA_L||_(N_y) + B^-1 ||A_L||_(N_y) ),

with C(L) free of n and of the volume. Combined with Lemma C (or the decay of
Section 3), the right side is at most C(L) times the local energy and datum.

*Proof.* (1) *Equation near the centre.* delta d A_L = q^T omega (stationarity on
ker q) and Pi delta A_L = 0, so delta A_L is constant on each top block and
d delta A_L = 0 on bonds inside it. On the flat lattice delta d + d delta is the
componentwise scalar Laplacian (the identity behind ||grad b||^2 = ||db||^2 + ||delta b||^2,
`lattice_sobolev_box_gauge.md` 2). So on the box Q of side B/2 about y,
Delta A_L = q^T omega. Testing delta d A_L = q^T omega with phi_c of Lemma T gives
omega(c) = <dA_L, d phi_c>, |omega(c)| <= 300 ||dA_L||_(D(c)); at most 16 rows reach a bond near
the centre, each with weight <= B^-3, so |q^T omega| <= 4800 B^-3 ||dA_L||_(N_y) on Q.
(2) *Particular part.* v := the solution of Delta v = q^T omega on Q, v = 0 on the
boundary. Comparing with (sup |q^T omega|/8)(B^2/4 - |x - y|_2^2), which has Laplacian
-sup |q^T omega| (Delta |x|^2 = 8 in d = 4), the maximum principle gives
|v| <= 150 B^-1 ||dA_L||_(N_y) on Q: in top units, |B v| <= 150 ||dA_L||.
(3) *Harmonic part.* h := A_L - v is harmonic on Q, and so is each difference
of it. Caccioppoli on the lattice (test Delta h = 0 with eta^2 h): for a cut-off
eta with |d eta| <= 8/r, sum eta^2 |dh|^2 <= 64 sum |d eta|^2 |h|^2. Twice, with Lemma 1 of
`lattice_sobolev_box_gauge.md` (||u||_4 <= 1.5 ||grad u||_2 on Z^4) applied to
cut-offs of h and of its differences, on boxes Q_r of side r = B/2 shrinking by
halves: ||h||_(l^4(Q_(r/8))) <= C r^-1 ||h||_(l^2(Q_r)) and ||grad h||_(l^4(Q_(r/8))) <= C r^-2 ||h||_(l^2(Q_r)).
*Gagliardo-Nirenberg at p = 3 on Z^4* (from the same Loomis-Whitney step with
w := |u|^9, since |a^9 - b^9| <= 9 |a - b| (a^8 + b^8) and Hoelder with 8/12 + 1/3 = 1):
||u||_12 <= 18 ||grad u||_3 for finitely supported u. With Hoelder on Q_(r/8),
||h||_(l^12(Q_(r/16))) <= C r^-(5/3) ||h||_(l^2(Q_r)). In top units this reads
||Bh||_(L^12(Q_(r/16))) <= C B^-1 ||h||_(l^2(Q)) <= C (B^-1 ||A_L||_(N_y) + ||dA_L||_(N_y)).
(4) *Shells.* Corollary A2 of `rel-phi-c.md` with p = 12 bounds the sum of
||H||_(L^4(A_j)) over the annuli inside Q_(r/16) by C(L) ||H||_(L^12) (each gains
L^(-(n-j)(2/3))); the at most 4 outer annuli, out to radius 5B/6, are bounded
by ||H||_(L^4(N_y)) <= C (||dA_L||_(N_y) + ||delta A_L||_(N_y) + B^-1 ||A_L||_(N_y)) (Sobolev with a
cut-off and the identity in (1)), and ||delta A_L|| = ||(1 - Pi) delta A_L|| is bounded by
B^-1 ||A_L|| with the bump test of Lemma S. Lemma A of `rel-phi-c.md`
(|Phi_n theta(y)| <= (3.4L + 1) times the shell sum) gives the bound on Phi_n. QED

Lemma A and Corollary A2 are discharged in `rel-phi-c.md` (same model, not
gated); everything else above is proved here.

**5.2 What this answers (queue row: "whether Balaban's multiscale Landau gauge
keeps the contour averages of Example E bounded").** Yes, at the flat linear
level, in the local Landau gauge Pi delta A = 0 of Section 4 (the block-diagonal
form of Balaban's gauge): the contour averages at every top centre, and the
l^1 shell sum of (REL-D), are bounded by C(L) times the local energy and
datum, uniformly in depth. Example E cannot occur there: the local Landau
condition makes delta A constant on each top block, so near the centre the field
solves Poisson's equation with a bounded right side and has no logarithmic
spike. The spikes of Example E come only from imposing g = 1 *pointwise* at the
centres.

**5.3 Consequence for (REL) of `seam-nonlinear-c.md` (implication at the flat
linear level; the nonlinear step named).** Start from the local Landau field
H_L and make it admissible with the point bumps of `rel-phi-c.md` 6.1,
lambda_b := -sum_y kappa(y) (1 - phi_y), R = floor(B^(1/2)), with amplitude
kappa(y) := -Psi_L(y)/(1 - c_R). Then the admissible field has Psi = 0 exactly
(Lemma 2 there), (REL-2) and (REL-4) change by at most 13 B^-(1/2) |kappa| and
4.25 |kappa| / log^(3/4)(1 + R) ((E3), (E4) there), and the shell sum of (REL-D)
changes by at most 4 |kappa| (log L)^-(3/4) (the log profile puts L^4 mass about
|kappa|^4 log L / log^4(1+R) in each of log_L R shells). Theorem E gives
|kappa| <= C(L) times the local energy. **So the amplitudes are O(1), not
O(n^(3/4)) as in Lemma CAP**, and the two nonlinear obstructions of `rel-phi-c.md`
4.2 become small: the twist is C f |kappa| relative, and the scrambling is at most
min(2, |kappa|) times the shell sum, which (REL-D) for H_L bounds. What is not done
here is the nonlinear form of Theorem E: the class minimiser U relative to the
iterated trial T, in a local Landau gauge relative to T, must satisfy the
interior estimate of steps (1)-(3) with the quadratic terms of the
Yang-Mills equation and the curvature of T as perturbations (an elliptic
bootstrap with smallness, f and the L^4 norm small). That is the first step of
(REL-Phi) at the nonlinear level that this note does not carry.

**5.4 Pointwise bounds: local regularity (LR), flat (discharged, given one
library lemma).**

**Lemma H (interior bound for lattice harmonic functions, Z^4).** If Delta h = 0 on
the box Q_(2r) (side 2r) then |h(x)| <= C_H r^-2 ||h||_(l^2(Q_(2r))) for x in Q_r, C_H absolute.
*Proof.* (i) One variable: on {0, ..., r - 1}, f(x) = f(t) + (differences between t
and x), so averaging over t, |f(x)| <= r^-1 sum_t |f(t)| + sum_t |f(t + 1) - f(t)|. Applied in
each coordinate in turn (the differences of t -> sum |g| are at most the sums of
|differences of g|): |f(x)| <= sum_(S ⊂ {1..4}) r^-(4 - |S|) sum_Q |d_S f|, d_S the mixed difference
in the directions of S. (ii) Cauchy-Schwarz: sum_Q |d_S f| <= r^2 ||d_S f||_(l^2(Q)).
(iii) Differences of h are harmonic; Caccioppoli (test Delta g = 0 with eta^2 g)
four times on nested boxes gives ||d_S h||_(l^2(Q_r)) <= (C/r)^|S| ||h||_(l^2(Q_(2r))).
Collect: |h(x)| <= C sum_S r^-(4-|S|) r^2 r^-|S| ||h|| = C' r^-2 ||h||. QED
(This replaces step (3) of Theorem E by a pointwise bound; Corollary A2 then
applies with p = infinity.)

**Lemma LR (flat pointwise curvature).** For the flat minimiser A_B and a
plaquette p of a layer >= 1, at distance >= xi_p from layer 0, with xi_p the
finest pillar side at its corners,

    |dA_B(p)| <= C(L) xi_p^-2 ( E(A_B; N_p) + sum_(c: D(c) meets N_p) |B(c)|^2 )^(1/2),

N_p the plaquettes within d_B-distance c_N of p. With Theorem FL (a):
|dA_B(p)| <= C(L) xi_p^-2 e^(-m psi(p)) ||B||: the pointwise curvature form of (1b)
Theorem 4 at V_0 = 1.
*Proof.* F := dA_B obeys dF = 0 and delta F = q^T omega on the free bonds, so
Delta F = d(q^T omega) (on the flat lattice the Hodge Laplacian of 2-forms is the
componentwise scalar one). |omega(c)| <= C_T^(1/2) ||dA_B||_(supp T delta_c) + |B(c)|-terms (test
with T delta_c, Lemma T), and at most C rows of each of the two levels present
reach a bond, with weights <= s_c^-3, so |q^T omega| <= C xi_p^-3 (local energy + datum)^(1/2) on the
cube Q_p of side xi_p/2 about p. Put F_1 := d G_T (eta q^T omega), with G_T the
mean-zero torus Green's function and eta a cut-off on Q_p: Lemma 2b of
`lattice_gehring_hls.md` (|grad G_T(x)| <= C (1 + |x|)^-3, proved there) gives
|F_1| <= C xi_p^-3 (..)^(1/2) sum_(|z| <= xi_p) (1 + |z|)^-3 <= C xi_p^-2 (..)^(1/2). F - F_1 is harmonic on
Q_p/2 componentwise; Lemma H with ||F - F_1||_(l^2) <= (local energy)^(1/2) + C (..)^(1/2) ends
it. QED

The same argument gives the potential in the local Landau gauge pointwise
away from pillar faces (Theorem E). Near pillar edges the local Landau
potential's gradient may lose a logarithm (delta A is pillar-constant, and
grad A is a second derivative of a Newtonian potential of a piecewise-constant
function); the curvature bound above does not see this.

## 6. The curved linear response at a regular background (derived at the level of each step, from one-step inputs)

**Setting.** U_0 real on Omega_0, *regular at radius eps* in local units:
|dU_0(p) - 1| <= eps xi(p)^-2 and |J(U_0)(b)| <= eps xi(b)^-3 (fine units; outline (1b)(i)),
xi the finest pillar side at the corners. Work in the straightened chart of the
Landau pair: the linearised rows K := K_(U_0) (path averages with the transports
of U_0, the outline's K_0), restricted gauge directions D mu := D_(U_0) mu with
r_(U_0) mu = 0 (transported pillar means), Pi_(U_0) the projection onto ker r_(U_0)
(block-diagonal), and the response form Q(h) := ||D_(U_0) h||^2 + <h, R h>, the second
variation of the Lagrangian, R local.

**Input (W) (derived in 6.1 from the exact factorisation, given one-step
inputs).** (W1) K D mu = 0 when r_(U_0) mu = 0 (the outline: "one has K_0 D lambda = 0
whenever the pillar averages of lambda vanish"); (W2) Q(h + D mu, h') = Q(h, h') for such
mu (Ward identity); (W3) |<h, R h>| <= c_W(L) eps ||h||_X^2 (curvature terms, and the
multiplier term, bounded through L^4 with a depth-free constant).

**Theorem CL.** There are eps_0(L), m'(L) > 0 and C'(L) such that, for eps <= eps_0,
Sad_(U_0) := [[Q + D Pi D^*, K^T], [K, 0]] is invertible on X x l^2(**B**) (X the
covariant graph norm of Section 4) with bound C'(L), and its solution at datum
beta supported on S obeys

    sum_P e^(2 m' psi(P)) ( xi_P^-2 ||h||_P^2 + ||D_(U_0) h||_P^2 ) <= C'(L) ||beta||^2.

Given (W), h is the response of the critical point, in the covariant local
Landau gauge Pi_(U_0) D^* h = 0.

*Proof (at the level of each step).*
(a) *Local flatness (discharged).* On a cube Q of side l whose finest scale is
s, the comb (axial) gauge from a corner gives |U_0^g(b) - 1| <= 3 l eps s^-2 on every
bond of Q: the loop closing the two comb paths bounds a strip of at most 3l
plaquettes, and |XY - 1| <= |X - 1| + |Y - 1| for unitaries with conjugation
invariance (non-abelian Stokes on a strip). On a patch of side R_0 xi# (xi# the
coarser scale within R_0 L xi of a seam, the local scale elsewhere) every
covariant operator above (D, D^*, K, r, Pi, the bumps of Lemma T) differs from
its flat version in this gauge by at most C R_0 L^2 eps, relative, in the
weighted norms.
(b) *Coercivity on ker K.* IMS with a partition sum_i eta_i^2 = 1 into such patches:
sum_i [Q + ||Pi D^* .||^2](eta_i h) <= (1 + kappa)[Q + ||Pi D^* .||^2](h) + (C/kappa) R_0^-2 sum_P xi_P^-2 ||h||_P^2
(the commutators with eta_i have size 1/(R_0 xi#) <= 1/(R_0 xi); block means of
D^* h are bounded by the graph norm through the bump test of Lemma S). For each
patch, transport eta_i h to the flat gauge, correct it into ker q with Lemma T
(the defect is [K, eta_i] h + (q - K^g) eta_i h, of size (C/R_0 + C R_0 L^2 eps) ||xi^-1 h||),
and apply Lemma C. With (W3): Q(h) + ||Pi D^* h||^2 >= (4 C_C)^-1 sum_P xi_P^-2 ||h||_P^2 on
ker K, once R_0^2 >= 16 C C_C and C R_0 L^2 eps + c_W eps <= (16 C_C)^-1.
(c) *Inf-sup and size.* Transported bumps phi_c^(U_0) satisfy
K phi_c^(U_0) = delta_c + E, ||E|| <= C L^2 eps, local; T_(U_0) := T~ (1 + E)^-1 by a
Neumann series (exponentially local, which Combes-Thomas allows). K is
bounded on X by Lemma 3 with transports.
(d) *Decay.* Brezzi's bound gives ||Sad^-1|| <= C'(L). For psi Lipschitz in d_B,
e^(m psi) Sad e^(-m psi) - Sad has norm at most C L m on X x l^2 for m <= 1/(10L): rows
have d_B-diameter at most 4L + 4, the commutator of Pi with e^(m psi) is bounded by m
times the block means of D^* h (bump test again). Take m' := 1/(2 C L C'(L)).
(e) *Exactness.* Test the first row with D mu, mu in ker r: by (W1), (W2),
<Pi D^* h, Pi D^* D Pi mu> = 0 for all mu, and Pi D^* D Pi is invertible on ker r, so
Pi D^* h = 0 and h is stationary for Q on {K h = beta}. QED (given (W))

**6.1 The input (W) from the exact factorisation (derived at the level of each
step).** Notation of the outline (1a, l. 7092, 7397, 7782; 1c statement 3): the
one-step straightened average and block factor of e^(ia) W_0 are defined by
M(e^(ia) W_0) = (e^(i Q1(a)) M(W_0))^(u(a)), with u acting at the coarse sites.

*Factorisation (exact, by covariance M(U^g) = M(U)^(g|coarse)).*
M^2(e^(ia) W_0) = M((e^(i Q1(a)) M W_0)^u) = M(e^(i Q1(a)) M W_0)^(u|coarse)
= (e^(i Q1'(Q1(a))) M^2 W_0)^(u' . u|coarse), with Q1' the one-step map at the
level-1 background M W_0. By induction the n-fold straightened average is the
composition Q^st_n = Q1^(n-1) o ... o Q1^(0) of one-step maps, each relative to its
own level's background, and v_n accumulates the block factors. (The outline
states this: "averaging of order k amounts to composing the straightened
one-step averages k times".)

*(W3).* Hence D^2 Q^st_n(h, h) = sum_m [D Q^st_(m+1 -> n)] D^2 Q1^(m)(X_m, X_m) exactly (chain
rule for a composition), X_m := D Q^st_m h, the straight path average with transports (no contour
term). Each one-step D^2 Q1^(m) is a bilinear form on the O(L^5) level-m bonds of
one double block, bounded by C(L) (Cauchy bounds of the analytic one-step
map near flat fields, outline 1b.2), so |D^2 Q1^(m)(X, X)(c')| <= C(L) sum_(D(c')) |X|^2.
|X_m(b)| <= 2^(3/4) ||h||_(l^4(S(b))) (`rel-phi-c.md` Lemma 4). The linear map from
level m + 1 to the top weights one bond by at most L^-3 per level (row sums
<= L, column sums <= L^-3 per step, outline (e)), and a top double block holds
about L^(4(n-m)) level-m bonds; by Hoelder the level-m term at a top row is at
most C(L) L^-(n-m) ||h||^2_(L^4(top neighbourhood)). Summing the geometric series,

    |<omega_0, D^2 Q^st_n(h, h)>| <= C(L) |omega_0| ||h||^2_(L^4) <= C'(L) eps ||h||_X^2

(Sobolev on Z^4 with a cut-off, and ||D^* h|| controlled by the graph norm through
the bump test). The curvature terms of the Hessian are pointwise O(eps xi^-2).
This is (W3). It is the mapped route's AN1 form (`seam-nonlinear-c.md` 4.2: a
remainder C_AN(L) e_j^2 with e_j an L^4 norm), here derived from the composition.

*(W1).* Along a gauge direction D mu, the change of the contour variables
W(y, x) is mu(y) - Ad(W(y, x)) mu(x); its mean over the block is mu(y) - Q' mu(y). So the
linearised block factor is mu(y) - Q' mu(y), and the covariance identity
differentiates to Q^sharp D mu = D-bar (Q' mu): the rows kill D mu when Q' mu = 0 (the
outline's "Q D = D-bar Q'", 1c (e)).

*(W2).* For a near 0 and a fine gauge g, Q^st(a^g) = Q^st(a) exactly when the
coarse values satisfy g|coarse = u(a)^-1 u(a^g) (compare the two expressions for
M((e^(ia) W_0)^g)). By the implicit function theorem (the linearised condition at
a = 0 is Q' mu = 0, and Q' is onto the tops), these g form, for each a, a smooth
family whose tangent at 1 is {D mu : Q'_a mu = 0}, smooth in a. Along it the action
is invariant and Q^st is constant, so the straightened Lagrangian is
invariant, and differentiating D L^st(a)[X_mu(a)] = 0 at the critical point a = 0
gives Hess L^st(h, D mu) = 0 for Q' mu = 0 (the argument of Lemma Inv of
`fibre-propagator.md`). The IFT step is written only to this level here.

*A tempting expansion that is wrong to stop at.* Expanding log(v(c_-)^-1 M^n v(c_+))
by BCH with v(y) the product over all levels of block factors at the same top
y produces cross-node commutators (1/2)[Phi(h)(c_-), Phi(h)(c_+)] of the multi-level
contour averages, whose size on the graph norm grows with depth (a transverse
field with energy spread over the n shells about y has Phi of order
n^(1/2) E^(1/2)). By the factorisation they cancel exactly against node terms of
log M^n; the pure node terms also pair to zero with omega_0 because gauge
invariance of the action gives delta' omega_0 = 0. (An earlier draft of this
section stopped here; the factorisation removes the stop.)

This is the outline's Theorem 4 at real points of the polydisc, in local
L^2 form, with the local Landau gauge in place of R D^T H = 0; and it is Theorem F
of `fibre-propagator.md` at a regular background in the multiscale geometry of
(1b), which is the input that `seam-nonlinear-c.md` 4.1 and `rel-phi-c.md` 6.3
name ("Sad#(T) invertible with exponential decay"). The iterated trial T of
(REL) is regular in this sense ((TOP-tr): pointwise fine curvature at most
C_7 B^-2 f), so at T Theorem CL needs only (W) and f <= eps_0(L).

## 7. Stop (L) of `sa-2.8.md`: the response between two critical backgrounds (implication)

**Reduction.** Let P be the prepared background (determining set D_p) and P_X
the localised one (joined sequence: the same rows away from the collar, finer
collar rows carrying the lift). Put Delta v := (lift data) - (the collar
averages of P itself) on the collar rows, in the straightened log chart; it is
O(eps) per row, eps = C_0 a_k in local units. Consider the joined problem with
collar data v_P + t Delta v, t in [0, 1].
- t = 0: P satisfies these rows by construction and is critical for its own,
  larger, constraint set, hence for the smaller one; so P(0) = P, given
  uniqueness of regular critical points of the joined problem (U).
- Continuation: the linearisation along the path is Sad_(P(t)) of Theorem CL,
  invertible with bound C'(L); the implicit function theorem continues P(t) while
  it stays regular, and the a priori bound int |P'| <= C'(L) sup|Delta v| keeps it
  regular at radius C eps <= eps-bar for small eps (open-closed argument). This
  also needs the smoothness bounds of the chart (outline 1b.2), not rebuilt.
- t = 1: P(1) = P_X by (U).
- P'(t) is the response to Delta v, supported on the collar rows C_X. By
  Theorem CL, its energy in the pillar of p is at most
  C'(L) (sum over collar rows c of e^(-m' d_B(p, c)) |Delta v(c)|)^2 <= C(L) eps^2 e^(-m' D_p),
  the sum over the collar costing only a power of D_p, absorbed by halving m'.

So the relative field of P_X against P, in the local Landau gauges along the
path, has energy at most C(L) eps^2 e^(-m' D_p) in the pillar of p, and the
plaquette holonomies there differ by that much in pillar l^2. With
|a(G) - a(H)| <= r |G - H|, r <= C_0 a_k eta^2 (`sa-2.8.md` 9), this is (L) with
m = m'(L)/2 in pillar-averaged form, from: Theorem CL (hence (W)), (U) (the
outline's Theorem 1, cited there to Balaban CMP 102 Prop. 8, not rebuilt), the
chart bounds of 1b.2, and, for one plaquette rather than a pillar average,
local regularity (LR): an interior pointwise bound for the curved linear
system on one cube, single scale, no depth in it. Steps (1)-(3) of Theorem E
are the flat version of (LR) for the potential in L^12; the pointwise curvature
bound needs one more difference (Caccioppoli on D h, then the same chain to
L^infinity via W^(1,12)), which I did not write.

**What this does not cover.** The ten-term remainder of 2.8, the complex
continuation (the outline's polydisc), and the shell variable conflation
recorded in `sa-findings.md` are outside A3 and untouched.

## 7b. Kill test (guidance only; discharges nothing)

`checks/a3/fl_killtest.py`, criteria registered in its header before the first
run; d = 2 (the proofs of Sections 2-4 are dimension-free in structure), torus
81 x 81, L = 3, two layers (level-1 rows outside, level-2 rows on a 27 x 27 union
of level-2 blocks), the actual tent rows, the bumps of Lemma T with one-sided
outward bumps and the one-step triangular correction, and the saddle system
of Section 4 with the block-diagonal gauge term. Under the numeric lock, 60
percent memory free, 2.5 s, 0.5 GB. Results (`checks/a3/fl_killtest_results.json`):
T1 same-level biorthogonality 4.4e-16; T2b every one of the 72 cross-level
readings is a fine bump read by an outward coarse row (triangularity as
claimed); T2 right inverse 2.2e-15; T4 local Landau exactness 3.5e-16 and rows
1.6e-15; T3 energy beyond d_B-distance t decays as exp(-2.9 t) with R^2 > 0.999
for data on a fine row, a coarse interior row and an outward seam row, the
energy beyond half the maximal distance being 2e-13 to 3e-12 of the total.
**PASS on all criteria.** The observed rate (about 1.45 per local unit for the
field) is far better than the crude m(L) of Section 3. One seam, d = 2, one size:
this cannot test uniformity in depth or in d = 4.

## 8. Verdicts, what stays open

| Statement | Label |
|---|---|
| Dimock 1712.10029 Section 3.7 as a proof to port | not a proof: quotes Balaban for the local inverses, the seam boxes and (day0) (Section 0) |
| Lemmas 1, 2, 3 (box curl-Poincare, scalar Poincare, links) | discharged, hand |
| Lemma T (exact local right inverse of the multiscale average, triangular at seams, E(T beta) <= 10^7 ||beta||^2) | discharged, hand |
| Lemma P (normalised patching of local gauges, any separated geometry, rho >= 3L^2) | discharged, hand; C_P(L) <= 10^16 L^12 |
| **Theorem FL (flat multiscale response: curvature and restricted-gauge potential decay in d_B, uniform in depth, regions, volume)** | **discharged, hand (hole-filling); L^2-local form** |
| Lemma S (scalar gauge problem: absolute decay rate; weighted bound) | discharged, hand |
| Lemma C (flat coercivity with the block-diagonal gauge term, sharp weights) | discharged, hand, given Lemma S (rho >= 8 log L / m_s) |
| K_M (outline's actual average, pointwise node gauge) unbounded on the graph norm, ratio >= c (log B)^(1/2) | scaling computation, constants not tracked; not load-bearing |
| **Theorem E (flat, local Landau gauge: contour averages and the (REL-D) shell sum bounded at every top centre, uniformly in depth)** | **discharged, hand**, using Lemma A and Corollary A2 of `rel-phi-c.md` |
| Admissible gauge from the local Landau one with O(1) bumps: (REL-Phi) = 0, (REL-2), (REL-4), (REL-D) kept | discharged at the flat linear level (5.3) |
| (W1), (W3): row covariance Q^sharp D = D-bar Q', multiplier term <= C(L) eps ||h||^2 in L^4, uniformly in depth | derived (6.1) from the exact factorisation of the straightened average; one-step Cauchy bounds and |omega_0| <= C eps are inputs |
| (W2): Ward identity of the straightened Lagrangian on ker Q' | derived to the level of an implicit-function step (6.1) |
| Theorem CL (curved linear response at regular backgrounds, decay, exactness) | implication from (W); depth-uniform |
| Lemma H (lattice harmonic interior bound, elementary) and Lemma LR (flat pointwise curvature of the response, with FL: C xi^-2 e^(-m psi) ||B||) | discharged, hand, given Lemma 2b of `lattice_gehring_hls.md` |
| (L) of `sa-2.8.md` | implication from CL, (U) = outline Theorem 1, chart bounds; one plaquette from curved (LR) |

**Open, hardest first.**
1. *Nonlinear Theorem E:* the interior estimate of 5.1 steps (1)-(3) for the
   class minimiser relative to the iterated trial, in a local Landau gauge
   relative to T (elliptic bootstrap with the quadratic Yang-Mills terms and the
   curvature of T as perturbations). With it, 5.3 closes (REL-Phi) and (REL-D)
   for (REL) of `seam-nonlinear-c.md`; Theorem CL at T supplies the decay.
2. *(LR) curved:* Lemma LR at a regular background. In a local axial gauge the
   curved system is the flat one plus terms of relative size C R_0 L^2 eps with
   one derivative fewer; Caccioppoli absorbs them for eps small, and Lemma H
   then applies to the flat part. Written only to this level.
3. *(U):* uniqueness of regular critical points (the outline's Theorem 1). With
   Theorem CL the implicit function theorem gives uniqueness in a small ball
   about the background; what is missing is the outline's Theorem 2 (the
   "halving": a regular critical point has curvature controlled by the
   data's, exponentially localised), which puts every regular critical point
   in that ball. **The nonlinear Theorem E (item 1) reduces to the same
   Theorem 2** plus a non-abelian patching of local gauges (the role of
   `lattice-uhlenbeck.md`): pointwise local potentials of size eps/xi in local
   gauges give |Phi| <= C eps directly (Corollary A2 with p = infinity), and 5.3 then
   makes the gauge admissible. So the outline's Theorem 2, a nonlinear form of
   FL + LR, is the common next target of both routes at this position.
4. *One-step inputs of 6.1:* Cauchy bounds of the one-step straightened map on
   a polydisc of radius r_L, |omega_0| <= C eps, and the implicit-function step
   of (W2), all single-block, finite-dimensional, with no depth in them.
5. Balaban's gauge R delta A = 0 (fourth-order analogue of Lemma S), only if a
   consumer needs it.

The rates here depend on L (seams cost L-powers through Lemmas P and S). The
outline's Theorem 4 allows that. The mapped consumers that want an absolute
fast rate (`fd-local.md` 6) get one inside each layer (Lemma S has an absolute
rate; Lemma P's chains have absolute length away from seams), but this note
does not prove an absolute rate across seams.
