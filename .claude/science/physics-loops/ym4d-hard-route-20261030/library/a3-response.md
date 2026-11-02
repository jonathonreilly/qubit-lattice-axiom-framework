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

## 6. The curved linear response at a regular background (implication from one named algebraic input)

**Setting.** U_0 real on Omega_0, *regular at radius eps* in local units:
|dU_0(p) - 1| <= eps xi(p)^-2 and |J(U_0)(b)| <= eps xi(b)^-3 (fine units; outline (1b)(i)),
xi the finest pillar side at the corners. Work in the straightened chart of the
Landau pair: the linearised rows K := K_(U_0) (path averages with the transports
of U_0, the outline's K_0), restricted gauge directions D mu := D_(U_0) mu with
r_(U_0) mu = 0 (transported pillar means), Pi_(U_0) the projection onto ker r_(U_0)
(block-diagonal), and the response form Q(h) := ||D_(U_0) h||^2 + <h, R h>, the second
variation of the Lagrangian, R local.

**Input (W) (gap: algebraic, the outline's 1b.3; not checked here).**
(W1) K D mu = 0 when r_(U_0) mu = 0 (the outline states it: "one has K_0 D lambda = 0
whenever the pillar averages of lambda vanish"); (W2) Q(h + D mu, h') = Q(h, h') for such
mu (the Ward identity; the proof of Lemma Inv of `fibre-propagator.md` gives it
as soon as the straightened Lagrangian is invariant under a group action whose
linearisation is mu -> D mu on ker r); (W3) |<h, R h>| <= c_W eps sum_P xi_P^-2 ||h||_P^2
(curvature and multiplier terms; follows from regularity once the multiplier
is O(eps), which the outline's Theorem 4 bounds).

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

**6.1 Hostile check of (W3): it is the hard part, and it is about Example E
again (derivation at the level of each term; not a theorem).** (W3) asks that
the multiplier term <omega_0, D^2 Q^st(h, h)> be O(eps) on the graph norm. The
straightened average strips the site factors, e^(i Q^st) = v(c_-)^-1 M v(c_+), and at
a top y the site factor is the product over all levels of the block factors
at the same site, v_j(y) = v_(j-1)(y) v-block_(j-1)(y), with log v-block_m(y) = phi_m(y) to
first order, phi_m the level-m term of Lemma 1 of `rel-phi-c.md`, so that the
linear part is Phi(h)(y) = sum_m phi_m(y). Second order, by BCH:
- *pure node terms* (1/2) sum_(m < m') [phi_m(y), phi_m'(y)] enter as
  sum_y (delta' omega_0)(y) (...), and **delta' omega_0 = 0** exactly: gauge invariance of
  the action gives <omega_0, K^st D mu> = <omega_0, d'(r mu)> = 0 for every mu. So these drop.
- *cross-node terms*: on ker K^st (Q_path h = 0) the cross terms of
  log(v_-^-1 M v_+) leave (1/2) sum_c <omega_0(c), [Phi(h)(c_-), Phi(h)(c_+)]>, which is
  not of divergence form (the second-order part of log M itself may add or
  cancel node-concentrated terms; I did not compute it).
On the graph norm, Phi(h)(y) is not bounded uniformly in depth even on the
local Landau slice: a transverse field whose energy E is spread evenly over the
n L-adic shells about y has, by the fourth-order Taylor term of the averaged
staircases (the second-order term is proportional to div A and vanishes),
|Phi(h)(y)| of order sum over shells of E_shell^(1/2), i.e. n^(1/2) E^(1/2) (Lemma A
and Corollary A1 of `rel-phi-c.md` give n^(3/4) as the upper bound). So the
cross-node term can be of size eps n E, not eps E. At the depths of the
construction (eps about g_k (log x_k)^q, n up to k), eps n is not small.
**Consequence:** Theorem CL holds as stated if (W3) holds, but (W3) is not a
consequence of regularity in L^2 norms; it needs either a cancellation of the
cross-node commutators against the second-order part of log M, or a mixed-norm
argument in which the response itself is shown to have bounded contour
averages (Theorem E is the flat case of that). Balaban's sup-norm setting
bounds Phi by sup |h| in local units, which is why the issue is invisible
there; but the response of the flat problem to the forcing that this term
produces is a gradient of a logarithmic profile about y (Example E's shape,
|Sol| ~ 1/r), whose own contour average is of order n, so even there the
iteration closes only if this term cancels. **The smaller inequality to
decide is (NC-comm):** on ker K^st, in the local Landau slice,

    | sum_c <omega_0(c), [Phi(h)(c_-), Phi(h)(c_+)]> + (node-concentrated part of <omega_0, D^2 log M(h, h)>) |
        <= eta (Q(h) + ||Pi D^* h||^2),   eta < 1/(8 C_C), uniformly in depth,

or an explicit regular background, multiplier and field violating it.

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
| Theorem CL (curved linear response at regular backgrounds, decay, exactness) | implication from (W); (W3) contains the cross-node term of 6.1, not shown small uniformly in depth |
| (L) of `sa-2.8.md` | implication from CL, (U) = outline Theorem 1, chart bounds; pillar-averaged; one plaquette needs (LR) |

**Open, hardest first.**
1. *(NC-comm) of 6.1*, the part of (W3) that can fail: the cross-node
   commutators of composite contour averages in the multiplier term of the
   curved Hessian. Uniform-in-depth curved response (Theorem CL, hence (L) and
   the outline's Theorem 4 at curved points) needs it or a cancellation.
   (W1), (W2) are algebra: (W2) follows from the exact Ward identity of the
   M-chart (Lemma Inv of `fibre-propagator.md`) once the straightening is the
   gauge shift by the site factors, because the linearised site factor of a
   gauge direction is exactly mu(y) - r mu(y) (mean of the contour-variable changes).
2. *Nonlinear Theorem E:* the interior estimate of 5.1 steps (1)-(3) for the
   class minimiser relative to the iterated trial, in a local Landau gauge
   relative to T. With it, 5.3 closes (REL-Phi) and (REL-D) for (REL).
3. *(LR) curved, pointwise:* one cube, one scale.
4. *(U):* uniqueness of regular critical points (the outline's Theorem 1).
5. Balaban's own gauge R delta A = 0 (fourth-order analogue of Lemma S), only if a
   consumer needs that gauge rather than the local Landau one.

The rates here depend on L (seams cost L-powers through Lemmas P and S). The
outline's Theorem 4 allows that. The mapped consumers that want an absolute
fast rate (`fd-local.md` 6) get one inside each layer (Lemma S has an absolute
rate; Lemma P's chains have absolute length away from seams), but this note
does not prove an absolute rate across seams.
