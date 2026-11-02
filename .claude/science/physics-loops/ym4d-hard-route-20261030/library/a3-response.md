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

Status: in progress; sections are written as they close.

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
V_0 = 1, B = 0, in local L^2 form; the pointwise form needs in addition the
single-scale local regularity of Section 5 (LR), which has no depth in it.

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
