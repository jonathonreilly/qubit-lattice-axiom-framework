# Check of gap-solve4-astra62.md (FINISH row 1150)

Checker: Claude Opus 5.5 (max effort), FINISH row 1150, line-by-line hand check.
File under check: `library/gap-solve4-astra62.md` (481 lines, row 1149, by gpt-6.2-astra).
Builds on: `library/gap-solve3-astra62.md` (row 1147), its check
`library/gap-solve3-check-opus.md`, and `library/gap-solve2-astra62.md` (row 1145).
Setting: `library/gap-council-brief.md`.
Status: done (Steps 1-8). Verdict table and RESULT line at the end.

## Plan (at most eight steps)

1. Read the setting (`library/gap-council-brief.md`), the file under check in
   full, and the cited parts of rows 1145 and 1147 and the row 1147 check.
2. Check Section 5: (12)-(15), the box-gap scale, the monotone path.
3. Check Section 8: the one-step reduction (20)-(22).
4. Check Section 12 (the expansion) and Section 13 (the projected
   restoration (33)).
5. Check Sections 1-4.
6. Check Sections 6-7 and 9-11: (16)-(19).
7. Check Section 14: (34) and the obstructions.
8. Verdict table and RESULT line.

## Log

- Step 1 done. Read `library/gap-council-brief.md` (all). Read
  `library/gap-solve4-astra62.md` L1-481 in four ranges. Read row 1147,
  `library/gap-solve3-astra62.md`, L1-411 (all): the open-box estimates
  (1)-(2), (4), (8), (15), (20), Sections 10-12 with (27)-(30). Read its check
  `library/gap-solve3-check-opus.md` L1-328 and L456-624: 45 statements, all
  HOLD, one precision note (small boxes need the projected gap (2) with (8),
  then (15)). Read row 1145, `library/gap-solve2-astra62.md`, L1-55 and
  L198-444: (1), (2), (16)-(19), (21), (22), Sections 7-12 with (25)-(26).

Notation. "L" means a line of `library/gap-solve4-astra62.md`. "Row 1147 (k)"
means equation (k) of `library/gap-solve3-astra62.md`; "row 1145 (k)" means
equation (k) of `library/gap-solve2-astra62.md`. a(u) = 1 - (1/2) tr u =
|1-u|^2/2. a_beta(d) = I_d(beta)/I_1(beta). r_beta = a_beta(2). b_beta =
1 + 6 beta. u_* is row 1147 (27); D_j, h, b, m are those of row 1147 Section 12
(m = floor(n/(H log n)), h = 1 + mH). Sigma_1 is the set of ordinary
(single-crossing) faces of row 1147 Section 11.

## Step 2. Section 5: (12)-(15), the box-gap scale, the monotone path (L166-211)

Section 5 uses three inputs from this file: the relative mixing (3)-(4) of
Section 2, the coarse deficit c B^(-2) and (10) of Section 4, and the
time-block expansion behind (5). They are checked in Step 5. The verdicts
below are given on the assumption that they hold, and Step 5 confirms them.

**Geometry and (12), L168-172. HOLDS.** Old intervals per circle: q ~ n/b.
Groups have k_g + 1 old intervals, k_g in {k, k+1}, k = floor(B/(3(b+1))).
With G = floor(q/(k+1)) groups the remainder is < k+1 <= G once
q >= (k+1)^2, which holds since q/k^2 ~ 9n(b+1)^2/(bB^2) -> infinity for
B << n^(1/3). New open boxes: products of three nonguard unions, side between
kb and (k+1)(b+1), comparable to B. A plaquette of Sigma_1 lies in a new box
unless a vertex coordinate is in a guard interval or its crossing is next to a
guard. Count of Sigma' (crossing in direction i): about 2 x (3n/B) admissible
x_i per circle times n^2 times 6 orientations, plus (n/b) tops x C n(b+1)/B
guard coordinates x n. Both are <= C n^3/B. Lower bound: 12-faces with x_1 at a
top (about n/(b+1) values), x_2 not a top, x_3 free give >= c n^3/b. The list
count is consistent: O((n/B)^3) macroscopic cells, C k^2 old cells near guard
layers in each, <= 6(b+1)^2 faces in each old cell, total C n^3 k^2 (b+1)^2/B^3
<= C n^3/B. Two adjacent old cells that both avoid guard layers lie in one
group in every direction, so their shared faces lie in one new box.

**Factor structure, L174. HOLDS.** With Sigma' at zero the unprojected
transfer M C^(tensor E) M factors over the components of the graph on edges
joined by an on plaquette. Every plaquette with four vertices in a new box is
internal (old box), in Sigma_1 inside the box (restored) or in Sigma_2, so the
new box is a full open box at coupling beta. A plaquette with edges inside and
outside a new box is in Sigma' (off) unless it is a Sigma_2 plaquette of a
small crossing box, and such a box then joins the large factor. The
crossing-link graph is the Cartesian product of three graphs of isolated
vertices and disjoint edges, so small components are full boxes with one or
two vertices per direction (row 1147 Section 11). A small box spans at most two
consecutive coordinates, so it cannot meet two new boxes (any guard width >= 1
suffices; the file's "exceeds two" is more than needed). Old boxes in guard
cells are separate factors: their outer plaquettes are in Sigma' or are
Sigma_2 plaquettes made of crossing links only. Components that share only a
vertex do not interact in the unprojected kernel. Every on plaquette lies in
one factor. The global vertex projection commutes with every factor and goes
into the rest kernel, as in row 1147 Section 3.

**(9) for the large factors, L176. HOLDS.** On the core any fixed comb
works: a 2-chord is joined to the tree by <= b_1 12-plaquettes with tree
1-links, a 3-chord by <= b_1 13-plaquettes and <= b_2 23-plaquettes, all
distinct. Cauchy-Schwarz gives |1-U_e|^2 <= (chain length) x 2A <= 4BA. On an
attached small box (it shares at least an edge with the core, so an outside
vertex has at most two outside coordinates) the clamping forest adds only
edges with an outside endpoint. The small boxes are vertex-disjoint, so the
union is a spanning tree of diameter O(B). A chord of a small box closes a
loop with its clamped edge (or a point) inside a box of side <= 2. The loop is
contracted by a bounded number of squares of that box. These squares are
Sigma_2 plaquettes, so they are on. Then
|1-U_e| <= |1-U_clamped| + sum_(<=6) |1-U_p|, using |1-gh| <= |1-g| + |1-h|
and conjugation invariance. Squaring gives |1-U_e|^2 <= 2CBA + 24A. Edge count
O(B^3), degree <= 6 and bounded plaquette incidence hold.

**Box-gap scale, L178. HOLDS.** kappa = min ||dY||^2/||Pi Y||^2 over
non-gradient cochains Y (each class has one representative I X; the curl is
gauge invariant). Lower bound: the linear form of row 1147 (1) on the core
(gauge the 1-links, the plane-r 2-links and one line of 3-links to zero; choose
r with plane 23-curl <= mean) gives sum_e |Y'_e|^2 <= C B^2 ||dY||^2. The
clamping extension bounds each small-box link by its clamped core edge plus a
bounded number of local curls. Each core edge and each square is charged a
bounded number of times, since small boxes are vertex-disjoint and of bounded
size. The minimal-norm (orthogonal) representative does no worse, so
kappa >= c/B^2. Upper bound: Y = d^* Phi with Phi a rescaled product bump on
12-plaquettes inside the core is orthogonal to gradients
(<d^* Phi, grad q> = <Phi, d grad q> = 0). ||Y||^2 ~ B^3 B^(-2) = B,
||dY||^2 <= B^3 (C/B^2)^2 = C/B. So kappa <= C/B^2. With (10),
omega = arcosh(1 + kappa/2) ~ sqrt(kappa) and beta^(-1/10) << 1/B for
B <= beta^(1/1000), so 1 - lambda_1/lambda_0 lies in [c/B, C/B].

**Parameters, L195. HOLDS.** From row 1147 (27),
beta u_* <= C beta/[(1+beta)(b+1)^5 e^(C(b+1)^5)] <= C (2+beta)^(-C gamma^5),
using b + 1 >= gamma (log(2+beta))^(1/5); so c_* = C gamma^5 (the constant in
the exponent of H). Inverse projected deficits: <= C B^2 for the large factors
and the guard boxes by Section 4 (the guard boxes satisfy (9) with B := b+1,
which is <= beta^(1/1000)); bounded for small boxes; a chordless component has
one physical state. In (3)-(4), (9) summed over <= CB^3 edges replaces
B_0^2 H_0 by C B^4 H_0. With E <= CB^3, H_0 = beta^(1/4) (>= 2C_0E + 2 log 8
eventually, since 3 theta < 1/4) and eta = c(B+2)^(-q):
k ~ C beta^(3/4) B^3 and the rest of (4) is C B^2 [B^4 beta^(1/4) +
B^3 log(2+beta) + q log(B+2)]. Both are o(beta) for theta < 1/1000, so they are
<= H_2 eventually. Unprojection, by row 1147 (15) on the factor:
(1 + C(B+2)^(-C/42))^(CB^3) - 1 = O((B+2)^(-q)) once C/42 >= q + 3. Factors per
macroscopic cell: one large factor, C k^2 guard boxes and
<= C k^3 (b+1)^2 <= C B^3 small boxes. The product relative error is <= sigma
for q >= 4 and large B.

**(13)-(14), L180-193, L202. HOLDS.** Sigma' faces per macroscopic cell:
<= C k^2 (b+1)^2 <= C B^2. A group reads factors of a bounded set of
neighbouring macroscopic cells, and each factor is read by a bounded number of
groups. So the label graph (electric label per cell and block, magnetic label
per group and block) has an absolute degree bound. For |v| <= v_2 = c/(H_2 B^2)
the magnetic labels obey |e^(v Y) - 1| <= e^(Cc) - 1 <= sigma. The
Kotecky-Preiss step and the end cancellation of row 1147 (28) give
Delta <= C n^3 m_2 e^(-m_2) <= C n^(-9) log n with m_2 = ceil(12 log n). The
rank-one comparison against any nonnegative rest kernel, once and twice, gives
|J'(v)| <= 4 Delta. Ratio:
v_2/u_* >= c beta^(c_* - 2 theta)/log(2+beta) -> infinity, since
theta < c_*/4. h_2 = 1 + m_2 H_2 = O(beta log B log n) = polylog(n), while
row 1147 Section 12 has h ~ n/log n. So D'_j is a sub-slab.

**Monotone path, L204. HOLDS.** Both reserved intervals fit in the h layers.
Interval 1 (1 + H_1 ceil(12 log n) layers, Sigma_1 at u_*): u_* << u_1 (since
H >> (1+beta) log(b+2)), so the proof of (5) makes its open kernel separable
to e^(+/- o(1)) for every nonnegative repeated exterior. Leg 1 changes only
interval 2 (u_* up to beta on restored faces, u_* up to v_2 on Sigma'; note
v_2 > u_*). Leg 2 keeps interval 2 at the (13) pattern, which is separable by
the proof of (14), and raises every other coupling to beta. Every coupling is
nondecreasing and the end point is the (14) schedule. The signed cost of each
leg equals the change of J, which is o(1) at both ends.

**(15), L206-211. HOLDS.** d/dv log Z_i = -i|D'_j|(1 - w'_i), so
dJ'/dv = 2|D'_j|(w'_1 - w'_2). J'(beta) is the homogeneous J and J'(v_2) = o(1)
by (14), so (15) <=> limsup J(beta) < log(1651/1650) <=> (30). Size:
|D'_j| = h_2 |Sigma'| <= C (n^3/B)(1+beta) log(B+2) log n. Spatial fraction
|Sigma'|/|Sigma_1| <= C b/B -> 0. The closing caveat (no bound on the original
common-u integrand beyond (5)) is correct.

## Step 3. Section 8: the one-step reduction (20)-(22) (L266-300)

**Set-up, L268. HOLDS.** One electric seam per period: N longitudinal links at
beta, 2N transverse links at v. In temporal gauge each seam link carries one
temporal plaquette, so exactly 2N = 2n^3 temporal plaquettes change. The
normalized convolutions commute with P, so the kernel of P C P is
int C(x, g.y) dg (one gauge average).

**Circle masses, L276. HOLDS.** At v = 0 the transverse factors are 1 and the
gauge integral factors over the n^2 longitudinal circles. On a circle, the
substitutions g_(i+1) -> (fixed left factor) g_(i+1) (fixed right factor)
turn the factors c_beta(x_i g_(i+1) y_i^(-1) g_i^(-1)) (class function) into an
n-step C_beta walk closed by a left-right twist. So
z_circ = int p_n(h^(-1) X h Y^(-1)) dh = sum_d a_beta(d)^n chi_d(X) chi_d(Y)^*,
with X, Y the circle holonomies of x, y. The d = 1 term is 1, and the rest is
<= sum_(d>=2) d^2 a_beta(d)^n <= eta(n/(1+beta)) <= C e^(-n/(1+beta)) by
row 1145 (1) at s = beta (the proof there gives I_d(s)/I_1(s) <=
e^(-(d-1)/(1+s))). Product over n^2 circles: |log| = O(n^2 e^(-cn/(1+beta))).

**Two circles, L278-283. HOLDS.** A transverse link factor is
e^(v w)/int e^(v w) with w = (1/2) tr(A g_z B g_w^(-1)), |w| <= 1, and Haar mean
zero in each variable. H = C_beta (x) C_beta has top vector 1 and norm
a_beta(2) <= e^(-1/(1+beta)) on the complement, so d_0 >= c/(1+beta). For
S = H^(1/2) e^(tf) H^(1/2): <1,S1> = E e^(tf) <= 1 + Ct^2 (E f = 0);
|<b,S1>| = |<H^(1/2) b, e^(tf) - 1>| <= C|t| ||b||; <b,Sb> <= e^(|t|)(1-d_0)||b||^2
<= (1 - d_0/2)||b||^2 for |t| <= d_0/4. The stated AM-GM step gives
||S|| <= 1 + Ct^2 + C t^2/d_0 <= 1 + C(1+beta)t^2. S <= e^(|t|) H gives
mu_1(S) <= 1 - d_0/2 by min-max, and Tr S <= e^(|t|) (Tr C_beta)^2 =
e^(|t|) c_beta(1)^2 <= C beta^3. Hence Tr S^n <= mu_0^n + mu_1^(n-1) Tr S, which is
the display. The two-circle integral is Tr(W prod_i e^(tf_i) H). W is a left-right
translation, so it commutes with H. Cyclic regrouping gives
Tr(W S_1 ... S_n), and Schatten-Hoelder (sum of 1/n = 1, ||W|| = 1) gives
prod (Tr S_i^n)^(1/n). log(e^a + b) <= a + b and z_circ = 1 + o(1) give the
normalized bound.

**(20), L285. HOLDS.** The transverse two-torus of circles has degree 4, so each
neighbour pair meets <= 6 others and greedy edge colouring uses <= 7 colours.
Each colour is a matching. Hoelder over 7 colours at t = 7v and independence of
distinct circles under the product circle law give
log E <= (2n^2/7)[49 C n(1+beta) v^2 + C(1+beta)^3 e^(-cn/(1+beta))]. This needs
7v <= c'/(1+beta), which is the stated range. Lower bound: flipping all spins of
one circle preserves its law and reverses each insertion, so E f = 0 and
Jensen gives log E >= 0. Normalizers: int e^(vw) dg in [1, e^(Cv^2)], 2N of
them. Together: |log K_v| <= C N(1+beta)v^2 + C n^2(1+beta)^3 e^(-cn/(1+beta)),
which is stronger than (20). Rank-one comparison with the constant kernel,
inserted once and twice against any nonnegative rest, gives |J| <= 4 sup|log K_v|.
On the trajectory n/(1+beta) >> log N, so the second term tends to zero.

**(21) and necessity, L287-291. HOLDS.** A q x 1 rectangle in a (1,2) plane has
2q links at beta and 2 at v, each used once. Its fundamental character is
gauge invariant, with eigenvalue a_beta(2)^(2q) a_v(2)^2. Distinct (base, q) with
q < n/3 have distinct edge sets. An unpaired link integrates to zero and the
character of a Haar holonomy has norm one, so the family is orthonormal and
orthogonal to 1. For q <= c beta, a_beta(2)^(2q) >= (1 - C/beta)^(2c beta) >=
const. a_v(2) = I_2(v)/I_1(v) ~ v/4 at 0 and is increasing (proof of (16)), so
a_v(2) >= c min(v,1). The diagonal sum over an orthonormal family is <= the
trace of a positive operator, which gives (21). K_v >= 0, ||K_v|| <= 1 and
K_v 1 = 1, so Tr K_v^2 <= Tr K_v and the identity-rest defect is
2 log Tr K_v - log Tr K_v^2 >= log Tr K_v. C_s^(tensor 3N) commutes with K_v and
its multipliers tend to 1 as s -> infinity. Dominated convergence
(sum of eigenvalues = Tr K_v < infinity) carries the defect to the identity
rest. So an exterior-uniform o(1) defect forces N beta v^2 -> 0, and with (20)
the scale is sharp.

**Retained fraction, L293. HOLDS.** Boxes of side s, s+1 cut <= 3N/s edges. For
s >= 6/eps the retained internal edges number >= N + eps N/2, so the total
excess sum_box (|R_box| - |V_box|) is >= eps N/2. A box with positive excess has
a cycle (|E| > |V|) of length <= (s+1)^3 and excess <= 3(s+1)^3. This gives
c_eps N vertex-disjoint short retained cycles. Products of their characters are
orthonormal invariant eigenfunctions, so
Tr >= [1 + a_beta(2)^((s+1)^3)]^(c_eps N) -> infinity. With exactly N
longitudinal links the only retained cycles are the circles of length n, which
is consistent with (20).

**(22), L295-300. HOLDS.** v_0 = [sqrt(N(1+beta)) log(2+n)]^(-1) gives
N(1+beta) v_0^2 = 1/log^2(2+n) -> 0 and v_0 <= c/(1+beta), so J(v_0) = o(1)
against the actual Wilson rest by (20). With normalized convolutions the
-i 2N log I(v) terms cancel in J. d/dv log Z_i = 2iN(wbar_i - 1), so
dJ/dv = 4N(wbar_1 - wbar_2). At v = beta the cylinder is homogeneous. So (22)
<=> limsup J(beta) < log(1651/1650) <=> (30) <=> (15).

## Step 4. Sections 12 and 13: the two-stage expansion, (30a) and (33) (L408-465)

**Bookkeeping estimate, L417-421. HOLDS.** Expanding prod(1 + f_i) and grouping
labels into overlap-connected polymers gives activities with
|z_X| <= prod_(i in X) w_i. Polymers with disjoint supports are independent
under the reference. Tree count: the children of i are labels j with S_j meeting
S_i, and sum_j w_j e^((a+3)|S_j|) <= |S_i| delta_0. By induction the trees above
a root are bounded by e^(|S_i|) (for delta_0 <= 1). So the polymer mass through a
site, weighted by e^((a+2) sum |S_i|), is <= delta_0. Then
sum_(Y incompatible with X) |z_Y| e^(a(Y)) <= delta_0 a(X) with
a(X) = sum_(i in X) |S_i|, which is the Kotecky-Preiss condition with spare
weight. The rooted log-series bound follows. The seed representation of
bridges (seed plus two endpoints) is standard.

**First integration and (31), L423-428. HOLDS.** Given the large-box paths,
the small components are independent unprojected chains coupled only by the
face insertions. Each Sigma_1 face has two crossing links and two non-crossing
links, the latter in the two adjacent old boxes. Its two crossing links lie in
different small components, because the transverse step of a single-crossing
face is not a crossing edge (L388). A small box has <= 12 edges, so the label
graph has bounded degree. Section 11's bridge bound at r = C(1+beta) (bounded
E, absolute projected deficit by row 1147 (2), (4) needs only O(beta^(3/4)),
then row 1147 (15) with <= 8 vertices) makes D_(l,c) - 1 as small as wanted.
|e^(zY_p) - 1| <= e^(2r|z|) - 1 is small for |z| <= c_0/r. The bookkeeping
estimate gives (31), uniformly in the prescribed paths and endpoints.

**Interior zero, L430. HOLDS.** At z = 0 every magnetic factor minus one
vanishes. A first-order term has exactly one magnetic label p, linear in Y_p,
in one polymer; the other polymers of the list are purely electric. Choose a
crossing component c of p whose variables in the term include no fixed slab
endpoint, and apply the centre element -1 as a gauge at an endpoint v of p's
link in c, to all of c's variables. Then mu_c, the bridge laws, the electric
labels D_(l,c)(x,y) and the internal Sigma_2 actions are invariant. p contains
exactly one link of c (its other links are in c' != c or in large boxes), so
w_p changes sign. The coefficient is therefore zero. With |L_gamma| <= a_gamma
on |z| <= z_0, the Schwarz-lemma step gives |L_gamma(u)| <= a_gamma (u/z_0)^2.
Electric-only terms read no large path.

**Boundary terms, L432. HOLDS.** Tail beyond R = ceil(C_2 log n):
<= C n^3 h C_(A_0) e^(-A_0 R) = o(n^(-5)). A truncated list spans <= C R fine
blocks, which is <= (R+3)k fine blocks once k >= C. So every term that reads a
fixed endpoint lies in its guard. These terms are exponentiated into positive
guard weights. No retained list reaches both ends.

**Second integration, (32), L434-440. HOLDS.** For a side-b box, (4) at length
kr needs only O(beta^(3/4) polylog(beta)) (projected deficit
>= (1+beta)^(-1/2) by row 1147 (20)). Row 1147 (15) with (b+1)^3 vertices gives
(b+1)^3 e^(-kr/(7(1+6 beta))) <= sigma when kr >= AC(1+beta) log(b+2) with A
large. The padded coarse support of a fine term has size <= C_3 s_gamma, and
x in S_gamma forces a fine label of gamma within bounded distance of x. There
are <= C(b+1)^2 k such labels. With A_0 > C_3(a+4), (31) and
|e^L - 1| <= C|L| give (32). (32) <= delta_0 is exactly
u <= c/[(1+beta)(b+1) sqrt(log(b+2))] = u_int.

**Separation, L442. HOLDS.** A list that depends on both guard histories has
padded support across all m middle blocks, so its weight is paid by e^(-am).
The error is C n^3 h e^(-c'm) with m ~ n/polylog(n), so it is o(1). The two
guard integrations then separate. All weights are positive and errors are
uniform multiplicative factors, so K(x,y) = e^(+/- o(1)) f(x) g(y). Inserting
K once and twice against the nonnegative Wilson rest gives J_D(u) = o(1). This
proves (30a).

**Projected representation, L456. HOLDS.** P commutes with M and C and
P^2 = P, so P may be inserted at every step. With (g.U)_e = g_v U_e g_w^(-1) and
k_(t+1) = k_t g_t, the substitution Y_t = k_t^(-1).Y'_t turns
c_beta(Y_(t,e)((g_t.Y_(t+1))_e)^(-1)) into a conjugate of
c_beta(Y'_(t,e) Y'_(t+1,e)^(-1)) (class function). It keeps Haar measure and
the gauge-invariant Sigma_2 actions, fixes Y_0 (k_0 = 1) and rotates the right
end to k_end.Y_end. Applying k_t to a whole face trace shows that the large
links enter as k_t.X_t. So the expansion (31) applies verbatim, conditional
on (X, g). psi_c is gauge invariant, so the vacuum end factors do not see k_end.

**Locality, L458. HOLDS.** For a fixed time-independent gauge q, applying q to
the large arguments and to all small variables and fixed ends read by a term
leaves its value unchanged: mu_c is invariant, bridges are covariant, D_(l,c)
is jointly invariant, and face traces are invariant because q acts at all four
vertices of each face (these are the endpoints of its two crossing links, which
lie in small components). With q = k_s^(-1) the large arguments become
(g_s ... g_(i-1)).X_i. A term at the left end has s = 0. A term at the right
end reads (g_s ... g_(end-1)).Y_end.

**Connected support, L460. HOLDS.** For one component c, the run variables
(endpoints inside the run and bridge seeds) have a law invariant under a
time-independent gauge at c's vertices. Distinct runs share no endpoint and
are independent. Replace c's run variables by k_(s_1)^(-1) applied to them, and
apply k_i^(-1) to the whole trace. The face at time i then reads X_i
unchanged and the two small links transported by
k_i^(-1) k_(s_j) = (g_(s_j) ... g_(i-1))^(-1), which I rechecked with the
convention above. These strings use only blocks of the run, and each block of
the run carries a label of the term on c. The gauges g_(t,v) at a crossing-link
vertex v belong to the old cell of v. So the padded coarse support is connected
and of size <= C s_gamma, also for k = 1.

**Factorization of (X, g), L462. HOLDS.** After the substitution only the
large-box electric factors contain g, and each vertex lies in exactly one old
cell. So the (X, g) measure is a product over boxes and steps of the
conditional laws of g_(t,B). Integrating g_(t,B) gives the projected box
kernel. The projected box chain at length r = C(1+beta) satisfies (4) (the
requirement is O(beta^(3/4) polylog)), so (15) is not needed.

**(33), L449-454 and L464. HOLDS.** With k = 1, a guard of C'R fine blocks
(C' absolute) contains every truncated end term. A neighbourhood of a coarse
site holds O((b+1)^2) fine labels, so (32) becomes C(b+1)^2 (ur/c_0)^2 <= delta_0,
that is u <= c/[(1+beta)(b+1)] = u_phys. The centre-flip zero holds with (X, g)
prescribed, since -1 is central and commutes with the frames. The two real
integrations give separability of the projected short kernel, and the
nonnegative rest gives (33). The signed integral from u_* to u_phys therefore
tends to zero.

**Cost of the uniform prescription, L444 (and its k = 1 form in L464).
HOLDS.** For one marked face with isolated crossing links and internal links
equal to 1, w_p = (1/2) tr(Y_e Y_e'^(-1)) with independent stationary links.
Its mean is 0, its variance 1/4 and its lag-d covariance a_beta(2)^(2d)/4, so
Var(sum_(t<H) w_p) >= cH beta for H >= beta. With one internal link equal to
(-1)^t, the lag sum is (1/4)[H + 2 sum_(d>=1) (-1)^d (H-d) a^(2d)]. This is
alternating with decreasing magnitudes and begins with a negative term, so it
is <= H/4. Cauchy on |z| <= c_0/r with modulus <= CH/r bounds the cubic remainder
by C(H/r)(|u|r/c_0)^3. For |u|r <= c_3 this is <= (c/4) u^2 H beta, since
r ~ beta. Summing over m_0 >= cb^2 independent pairs gives the difference
>= c_4 b^2 k (u beta)^2 (H ~ rk). With k = 1 this is c b^2 (u beta)^2, which is of
order one at u ~ u_phys. The statement is correctly scoped: it does not
address the true law of the large-box histories or cancellation between
subfamilies.

## Step 5. Sections 1-4 (L19-163)

**(1), L21-26. HOLDS.** Tr(BC) = Tr(F^(T-1) MCM) = Tr F^T and
Tr(BCBC) = Tr F^(2T), so Tr rho^2 = Z_2/Z_1^2 = e^(-J). C commutes with P, and
the normalizing scalars cancel. J < log(1651/1650) <=> 1 - Tr rho^2 < 1/1651.

**(2), L28-37. HOLDS.** Each link's d-isotypic projection commutes with left and
right multiplication, so Q_l commutes with P and C Q_l = c_l Q_l. Then
p_l = c_l Tr(B Q_l)/Z, B^(1/2) C B^(1/2) = Z sum_l p_l tau_l, and
X = B^(1/2) C^(1/2) gives X X^* = B^(1/2) C B^(1/2) and X^* X = Z rho. So
Tr(sum p tau)^2 = Tr rho^2, and sum p_l = 1 gives (2). Each term is >= 0 since
0 <= tau <= I. **L39. HOLDS:** replacing C by tensor_e C_(v_e) changes only the
multipliers prod_e a_(v_e)(d_e), with a_0(d) = 1_(d=1) (Haar projection).

**Section 2 set-up, L44-50. HOLDS.** D_r is a reversible Markov density for
mu = psi^2 dU. inf K/sup K >= e^(-C(1+beta)E) (a <= 2 in the electric and
magnetic weights), the Perron equation and sup psi >= 1 give
inf psi >= e^(-C(1+beta)E). Then
D_1 <= U_0/(lambda inf psi^2) <= e^(C_1(1+beta)E), and
D_(r+1)(x,y) = int D_1(x,z) D_r(z,y) mu(dz) <= sup D_1.

**(3), L52-56. HOLDS.** ||1_(G_0^c) K|| <= ||1_(G_0^c) M|| <= e^(-C_0E)/8, so
||1_(G_0^c) psi|| <= 1/8. Row 1147 (1) on z in G and w in G_0 gives
sum |1 - .|^2 <= C B_0^2 H_0/beta. Restricted gauges then give an electric
exponent >= -C(B_0^2 H_0 + E), magnetic factors >= e^(-H_0), and
(c beta^(3/2))^E (c beta^(-3/2))^(V-1) >= e^(-CE). (The file's
e^(-CE log(2+beta)) is a valid weaker bound.) Then
psi(z) >= inf_(GxG_0) K int_(G_0) psi and int_(G_0) psi >= (63/64) lambda/U_0
bound inf_G psi from below. Finally
K^r - lambda^r psi psi = <K(x,.), R^(r-2) K(.,y)> with
||R|| <= lambda(1-delta) and row norms <= U_0, which gives (3).

**(4), L58-68. HOLDS.** On {sigma > k} the internal factors M(x_i)^2 =
e^(-beta A(x_i)) <= e^(-H_0) for i = 1..k-1, the electric rows integrate to one,
and the vacuum transform telescopes. This gives the displayed tail. With
H_0 >= 2C_0E the tail is <= exp[C(1+beta)E + C_0 E - (k-1)H_0/2], which is
<= eta e^(-C_1(1+beta)E)/8 for the stated k. The strong Markov property at the
two bounded stopping times and symmetry give
D_r(x,y) = E[D_(r-tau-tau')(X_tau, Y_tau')] for r >= 2k+2. A miss costs
<= 2 (eta e^(-C_1(1+beta)E)/8)(e^(C_1(1+beta)E) + 1) <= eta/2, and two visits
cost <= eta/2 under (4) by (3). With delta >= (1+beta)^(-1/2) (row 1147 (20)) and
eta = c(b+2)^(-q): k = O(beta^(3/4) (log beta)^(3/5)), and the delta^(-1) term is
O(beta^(3/4) polylog). Both are o(beta).

**(5), L71-83. HOLDS.** A cell is one old box plus <= C(b+1)^2 small
components. (4) at r >= H_1 gives eta = sigma/(K(b+2)^q). Row 1147 (15) gives
(1 + C(b+2)^(-A/42))^((b+1)^3) - 1 <= eta for A/42 >= q + 3. The product over a
cell is within C(b+1)^2 eta <= sigma of 1. Magnetic labels:
2C H_1 (b+1)^2 u_1 = 2CAc, which is small. With
m_1 = floor((h-1)/H_1) ~ n/polylog(n), the cross ratio is
<= C n^3 m_1 e^(-m_1) -> 0. u_1/u_* = H/[(1+beta) log(b+2)] up to constants,
which tends to infinity.

**Scalar estimates, L95-104. HOLDS.** Shifting the contour by i/sqrt(beta)
gives |I_d(beta)| <= e^(-d/sqrt(beta)) I_0(beta cosh(1/sqrt(beta))) <=
e^(1/2 + o(1)) e^(-d/sqrt(beta)) I_0(beta), using I_0(x+y) <= e^y I_0(x).
I_1/I_0 is increasing (derivative = variance) and I_1(1)/I_0(1) > 0, so
a_beta(d) <= C e^(-(d-1)/sqrt(beta)). (This is consistent with
I_d/I_1 ~ e^(-(d^2-1)/(2 beta)), since x^2/2 - x >= -1/2.) The generating sum is
sum_(d>=1) r^d sin(dt)/sin t = r/(1 - 2r cos t + r^2), and its r-derivative is
the displayed W_r > 0. W_r(0) = (1+r)/(1-r)^3 <= C beta^(3/2). For one
dimension: sup <= a d^2 <= C beta, and L^1 <= L^2 = a d <= C sqrt(beta).

**(7), L106-111. HOLDS.** I checked the file's shelling case by case with
this tree: 1-links with x_1 <= n-2, 2-links at x_1 = 0 with x_2 <= n-2, and
3-links at x_1 = x_2 = 0 with x_3 <= n-2. That is N - 1 links. The kept chords
are the wraps at (n-1,0,0), (0,n-1,0) and (0,0,n-1). An interior 2-pivot or
3-pivot moves one step in a lower direction through a plaquette whose other
links are tree links or earlier pivots. A wrapping pivot moves one step in its
first nonzero transverse coordinate. Its plaquette uses two tree or interior
links and an earlier wrap (or a kept one). For example, the wrapping 2-link at
(0, n-1, x_3) uses the 23-plaquette at (0, n-1, x_3 - 1), with the tree 3-link
at (0,0,x_3-1) and the interior 3-pivot at (0,n-1,x_3-1). Each pivot's
plaquette holds only earlier links besides the pivot, so the D-3 = 2N-2
plaquettes are distinct and each transport is Haar given the earlier
variables. Hence int e^(-beta A) <= z_beta^(D-3) <= (C beta^(-3/2))^(D-3).
Norm: the ball trial gives
|S| inf_(SxS) F >= (c beta^(-3/2))^E (c beta^(3/2))^E e^(-CE). The unprojected
vacuum is gauge invariant, so it is also the projected vacuum.

**(6), L113-117. HOLDS.** p(Q_S) <= lambda^(-1) Tr(M C Q_S M) from
0 <= F^(T-1) <= lambda^(T-1) and Z >= lambda^T. The multipliers satisfy
a_beta(d) <= C r^(d-1), so C_beta <= C W_r in operator order, and tensor
products and M . M preserve the order. Edge-transitive averaging gives a tree
with t <= |S|(N-1)/E <= |S|/3 specified edges. Diagonal of the projected kernel:
chords by sup norm (C beta^(3/2), or C beta if specified), tree edges by L^1 from
the leaves (1, or C sqrt(beta) if specified). This gives
C^E beta^(3D/2 - (|S|-t)/2 + t/2). With (7):
e^(CE) beta^(9/2 - |S|/2 + t) <= e^(CE) beta^(9/2 - |S|/6).

**(8), L119-125. HOLDS.** Condition on k, take a union over at most 2^E subsets
and apply (6). Widths w = O(beta^(1/6 - xi)) cost w^(eps E), which is beaten by
beta^(-eps E/6). Deleting the close pairs changes the purity by at most their
probability, since Tr(tau tau) <= 1.

**(9) and coordinates, L130-146. HOLDS.** The tree gauge with g_root = 1 is
unique. Chords are independent Haar given the tree transports. The rooted kernel
is M M int prod c_beta(x_e (g.y)_e^(-1)) dg over nonroot gauges. Its electric
part is a compression of a contraction. Its top state is invariant. The ball
trial gives lambda_0 >= e^(-CE).

**Coercivity, L148. HOLDS.** For U = exp(tIX), |1 - e^(tX_e)|^2 = t^2|X_e|^2 +
O(t^3) and A = (t^2/2)||dIX||^2 + O(t^3). So (9) gives
max |X_e|^2 <= (C_0 B/2)||dIX||^2, and with <= CB^3 chords, V >= cB^(-4). For
rooted q, |q_v| <= sqrt(C_0 B) ||(IX - grad q)|_tree||. Summing the chord
inequalities gives ||X|| <= CB^2 ||IX - grad q||, hence Q >= cB^(-4); Q <= 1 is
clear.

**Gaussian comparison, L150-161. HOLDS.** Exponential coordinates
u = exp(Z/sqrt(beta)) with Haar density h_0 beta^(-3/2) (sin t/t)^2,
h_0 = 1/(2 pi^2) = 1/vol(S^3). Constant: (h_0 beta^(-3/2))^(chords + v - 1) /
z_beta^E = b_beta, since chords + (v-1) = E. Endpoint tails: if
max |X_e| > P_0 then (9) and |1 - e^u| >= 2|u|/pi give beta A >= c P_0^2/B.
Gauge tails: Cauchy-Schwarz along a tree path of length <= C_0 B gives
beta sum a >= c R_0^2/B. Gaussian prefactors: the tree gradient block is square
with determinant +-1, so det(grad^* grad) >= 1, and the q-integral is <= e^(CE).
The convolution norm is int e^(-<Z,QZ>/2) dZ <= e^(CE log(2+B)) since
Q >= cB^(-4). With E <= C_0 beta^(3/1000), P_0^2/B >= beta^(1/15 - 1/1000) and
R_0^2/B >= beta^(1/5 - 1/1000), all tails are o(e^(-CE)/beta). Pointwise: a word
of <= 4 factors with |Z_i| <= R_0 has
beta a(word) = |sum +-Z_i|^2/2 + O(R_0^3/sqrt(beta)), and each Jacobian has log
error O(R_0^2/beta). So eps_beta <= C E beta^(-1/5) = O(beta^(-197/1000)), which
is <= beta^(-19/100). For positive kernels, |K - G| <= (e^eps - 1) G pointwise
gives the norm bound. ||G|| <= 2 lambda_0 follows from the same inequality, so
||F - G|| <= C beta^(-19/100) lambda_0 <= C beta^(-1/10) lambda_0.

**(10), L163. HOLDS.** After integrating q the kernel is
exp[-<X,VX>/4 - <Y,VY>/4 - <X-Y, Q(X-Y)>/2]. The unitary change X -> Q^(-1/2) X
and an orthogonal change (the same in each colour) give scalar modes
exp[-s(x^2+y^2)/2 + xy] with s = 1 + v_0/2. The vacuum is e^(-d_0 x^2/2),
d_0^2 = s^2 - 1. The vacuum chain has mean x/(s+d_0) = e^(-omega) x, so the
spectrum is prod e^(-k_j omega_j). Degree one carries SO(3) vectors only. The
softest mode's centred |x|^2 is invariant with ratio e^(-2 omega), and all other
invariant ratios are <= e^(-2 omega). Weyl's inequality for compact self-adjoint
operators on the invariant subspace gives (10). The deficit follows from
kappa >= lambda_min(V)/||Q|| >= cB^(-4), e^omega >= 1 + sqrt(kappa) and
beta^(-1/10) << B^(-2) for B <= beta^(1/1000).

So the inputs that Step 2 assumed ((3)-(4), (5) and (10) with its coarse
deficit) hold. The Section 5 verdicts stand.

## Step 6. Sections 6-7 and 9-11: (16)-(19), (23)-(29) (L214-405)

**(16), L216-222. HOLDS.** int_(-1)^1 e^(vx)(1-x^2)^(j-1/2) dx is a positive
multiple of v^(-j) I_j(v) (Poisson integral). Its log-derivative is
I_j'/I_j - j/v = I_(j+1)/I_j, which is also the tilted mean of x, and the
derivative of that mean is a variance. So each I_(j+1)/I_j increases, a_v(d)
increases in v, and C_(beta/2) <= C_beta. Multiplying the weight by
e^((beta/2) a) on marked links gives (z_(beta/2)/z_beta) C_(beta/2) there, and
<psi, M C' M psi> <= lambda. This proves the moment bound;
z_(beta/2)/z_beta -> 2^(3/2), and Jensen gives the second inequality. For a
positive rest R, Tr(M(C - C')M R) >= 0.

**Disjoint residual faces, L224. HOLDS.** In a guard layer normal to axis 3,
a 12-face between two consecutive guard cells, with x_2, x_2+1 inside an old
interval and x_3 inside the guard interval, has two isolated one-link crossing
factors and two links in the two guard boxes. It lies in Sigma'. One face per
separated macroscopic group gives M_0 >= c(n/B)^3 faces with disjoint factors.

**(17), L226-231. HOLDS.** The pair law (U, U') of each factor is invariant
under the same vertex gauge at both times. V (x) V^* is irreducible for left and
right multiplication, so E[U_e (x) U'_e] = r_e E_Haar[U (x) U] and
<2w_p Psi, (G/Lambda) 2w_p Psi> = prod_(e in p) r_e >= 1 - C'/beta by (16).
Products over subsets are orthonormal physical vectors with quotients
prod_p prod_e r_e. Jensen for x^s on spectral measures in [0,1] gives (17).
J_alone >= log Tr(G/Lambda)^s. The sum diverges for s = o(beta log M_0).

**Marked expansion fails, L233. HOLDS.** This is the argument of row 1147
Section 10 (checked there), now with the stationary correlation
>= (1 - C'/beta)^d/4, an endpoint density loss bounded by a constant, and
H_2 >= c beta. For the spanning polymer, fix all other components' endpoints:
the rectangular difference is then (positive constant) x (rectangular
difference of the free link's D), which is nonzero.

**(18) lower bound, L238-243, L255. HOLDS.** The central gauge at a vertex acts
by prod (-1)^(eta_e) and is trivial on physical states. So eta lies in the
Z_2 cycle space, of dimension E - N + 1 = 2N + 1, and
max p_eta >= 2^(-(2N+1)).

**(19), L245-253. HOLDS.** U_s commutes with C^(1/2), so
W(s) = Tr(F^(T-1) M C U_s M)/Z, a positive position integral. Telescoping:
2 = |1 - (-1)| <= |1 - U_p(x)| + |U_p(x) - U_p(s.y)| + |1 - U_p(y)|. Squaring and
summing (each edge in <= 4 plaquettes) shows a fixed fraction (<= 1/2) of the
exponents pays c beta m(s), for any common gauge on y. The rest is
(z_(beta/2)/z_beta)^E times a positive kernel of norm <= e^(CE). Then
|Tr(F^(T-1) X)| <= ||Y|| Tr F^(T-1), Z_(T-1)/Z_T <= Tr F/lambda^2 (T >= 2), and
Tr F <= z_beta^(D-3) (C beta^(3/2))^D = e^(CE) beta^(9/2).

**(18) upper bound, L255. HOLDS.** ker(delta) on Z_2^E is the flat sign
connections, of size 2^(N-1+3), so the image has 2^(2N-2) elements. The
fraction with m(s) <= N/sqrt(beta) is <= 2^(-(2N-2)) N (3e sqrt(beta))^(N/sqrt(beta))
= 2^(-2N+o(N)). For the other s, (19) gives e^(3CN - c sqrt(beta) N) = o(2^(-2N)).
Fourier inversion with W >= 0 gives p_eta <= 2^(-E) sum_s W(s).

**Centre average, L257-263. HOLDS.** B_av is physical, positive and has a
nonnegative kernel. U_s commutes with C_v and Q_l, so all one-period traces
and isotypic weights are unchanged. Since C^(1/2) commutes with U_s,
C^(1/2) B_av C^(1/2) is the pinching of Z rho onto the parity sectors. Its purity
is sum_eta Tr(Pi_eta rho Pi_eta rho) <= sum p_eta^2 <= max p_eta. The
rank-one vacuum rest B_inf = |M psi><M psi| is the T -> infinity limit
(simple top eigenvalue), gives Tr(B_inf C) = lambda and purity one, and
satisfies the same frustration bound.

**(23), L307-317. HOLDS.** Removing marked temporal couplings gives
C_0 <= C_t <= C_beta, so 0 <= F_t <= F, and trace Hoelder with min-max gives
|Tr prod F_t| <= Tr F^h. The normalizations give z_beta^(-|S|). Any k spatial
plaquettes have >= 2k/3 containing one common direction (the three direction
counts sum to 2k). The homogeneous isotropic torus allows that direction as
time. Markov's inequality on that subset gives the display.

**(24), L319-325. HOLDS.** P(bad) <= 2^m (C beta^(3/2) e^(-beta/32))^(m/6) by
(23) (a union over the subsets of m/4 frustrated faces). Write A = C^(1/2) M and
R = F^(T-1). Then Tr(R D A^* U_s A) = <A D R^(1/2), U_s A R^(1/2)>_HS <=
(Tr R D F D)^(1/2) Z^(1/2), using A^* A = F, and Tr(RDFD)/Z is a two-time
periodic probability <= P(bad). On good x good, >= m/2 frustrated faces have
|1 - U_p| <= 1/4 at both ends, so sum_(e in p) |x_e - s_e y_e| >= 3/2 and, by
incidence, sum_(S_e) a >= c_1 m with |S_e| <= 4m. Half of these exponents pay
e^(-c_1 beta m/2). The rest is (z_(beta/2)/z_beta)^(4m) times a positive
twisted trace with C' <= C_beta, and |Tr(X U_s)| <= Tr X <= Tr(MRMC) = Z. The sum
of the three parts is <= e^(-c beta m) for beta >= beta_0, uniformly in volume and
T >= 2.

**(25), L327-331. HOLDS.**
p_eta <= 2^(-3N) |ker delta| sum_omega e^(-c beta |omega|) <=
2^(-3N) 2^(N+2) (1 + e^(-c beta))^(3N).

**Local coherences, L333. HOLDS.** Tr sigma^2 = Tr rho^2. The one-mark (23)
gives P(tr U_p < 0) <= e^(-beta)/z_beta. F_2-independent boundary rows give
masks flipping exactly one S_i. These are commuting involutions that anticommute
with their own S_i, so H = (C^2)^(tensor k) (x) H_+. Off-diagonal blocks have
trace norm <= ||P_+ sigma^(1/2)||_2 ||sigma^(1/2) P_+^perp||_2 =
sqrt(eps(1-eps)), so the state is within O(sqrt(eps)) of a product, and
|Tr sigma^2 - Tr sigma_+^2| <= 2 ||sigma - sigma_+||_1.

**Freezing all signs, L336. HOLDS, with the one-loop step conditional as
labelled.** The conditional law is e^(t h.u) with t <= 6 beta, and marked links
share no plaquette. The ball centred at cos(2r) u_0 - sin(2r) q lies in
{q.u < 0} (angular distance 2r from the equator) and has h.u >= -3r. So
p_* >= c r^3 e^(-3rt - t) >= c(1+beta)^(-3) e^(-6 beta). With
log(1/a) ~ beta/(8 b_0), b_0 = 11/(24 pi^2), one gets log n/beta -> 3 pi^2/11 =
2.69 > 2, and then N p_* = e^(3 log n - 6 beta) poly -> infinity. This uses the
account's additional one-loop hypotheses, which the file states.

**Equal-time dephasing, L338. HOLDS.** Y is gauge invariant, centre-flip
invariant and atomless (U_p is Haar after integrating one link). The Gaussian
average of e^(isY) sigma e^(-isY) with Var s = 2t has kernel
e^(-t(Y(x)-Y(y))^2) sigma(x,y). It keeps the diagonal, positivity and all
expectations of positions and centre flips, and its Hilbert-Schmidt norm tends to
zero by dominated convergence.

**(26), L346-351. HOLDS.** Reducing marked temporal couplings to beta - 3t
gives C_(beta-3t) <= C_beta and the factor z_(beta-3t)/z_beta per face. Then
log(z_(beta-3t)/z_beta) = int E_s a ds <= 3t C/(1 + beta/2) for t <= beta/6.
Hoelder over three direction classes on the homogeneous torus gives
0 <= log E e^(t sum_S a) <= C|S|t/beta for one and for two repeats. The remark on
witness sizes is conditional on the witness, as the file says.

**Chart failure, L353. HOLDS.** A flat field with a nontrivial winding has
A = 0 and is not gauge-equivalent to 1, so (9) fails on the torus. A fixed tree
has a fundamental cycle with winding, of length >= n. It has >= n/19 links with
no shared plaquette (conflict degree <= 6 x 3), and row 1145 (2) makes its
holonomy density within eta(n/(19(1+6beta))) = o(1) of Haar. The same argument on
a length-B rectangle of an open core gives failure when B/beta -> infinity.

**Scalar model, L356-366. HOLDS.** For t = 0 the 1D Poincare inequality with the
retained boundary diagonal gives stiffness >= c/B^2. The bond form is
(1-t)(x_i^2 + x_l^2) + t(x_i - x_l)^2, so the stiffness is >= c(1-t)/B^2. The
r-step mode kernel has A = sinh(omega) coth(r omega), D = sinh(omega)/sinh(r omega)
(at r = 1 these are cosh(omega) and 1), and D/A = 1/cosh(r omega) <= 2e^(-r omega).
The bound |Dxy| <= (D/A) A(x^2+y^2)/2 is <= eps times the total endpoint form, and
the Gaussian factors (1 +/- eps)^(-dim/2) give |J| <= C N eps. With h = h_2 and
1 - t = 1/log(2+beta), h sqrt(1-t)/(B log n) ~ beta^(1-theta) -> infinity, so the
cylinder is cold. At t = 1 a mode with q = e^(-T omega_0) contributes
log((1+q)/(1-q)), which diverges since T omega_0 <= T mu_j = L a_j/2 -> 0. The
other modes contribute >= 0.

**(27)-(29), L371-403. HOLDS.** (1 + E_r)^(*k) = 1 + E_r^(*k), because E_r has
zero means in both variables, and the sup norm is submultiplicative. Bridge
means: D_i, D_(H-i), D_H = 1 + O(e^(-c./r)) give |E f_i| <= C(e^(-ci/r) +
e^(-c(H-i)/r)). Skeleton rows dominate (1/3) of a common probability, so the
Doeblin coupling fails with probability <= (2/3)^i. A Doob-martingale increment
has range <= 4r + 4r x 3, and Hoeffding's lemma iterated over <= H/r segments gives
(28). A face reads the product chain of two distinct small components, which has
the same bound with a slightly larger tolerance, and a bounded colouring gives (29).
The L^q bound follows from the sub-Gaussian tail. With H = O((1+beta) log(b+2)) both
scales are <= C(1+beta)(b+1)^2. Conditional Hoelder over colours of magnetic
groups gives |E prod (F_i - 1)| <= sigma^(|X|), since electric factors are
constants given endpoints. The connected lists are unchanged. This proves (27).

**Boundary limit, L405. HOLDS.** A conjugation-invariant bridge from 1 to 1 has
E U_i = s_i 1. For i <= c_0 beta, s_i >= a_beta(2)^i - o(1) >= c_1/2. With the
internal links equal to 1, the face mean is s_i^2 >= 0. Summing over cb^2 faces and
i <= c_0 beta gives E Y_c >= c_2 b^2 beta, and Jensen gives the bound. Continuity
and positive bridge densities pass this to positive-probability neighbourhoods.

## Step 7. Section 14, (34), the scope remarks, OPEN and RESULT (L467-481)

**(34), L469-475. HOLDS.** The 2N-2 shelling plaquettes of (7) have
F_2-independent boundaries. By (23), each is negative with probability <= q in
the T- and the 2T-period states. Markov's inequality gives
P(more than sqrt(q)(2N-2) negatives) <= sqrt(q). Tr(P_g sigma P_g sigma) =
Tr(P_g F^T P_g F^T)/Z_T^2, and dividing by Tr sigma^2 = Z_2T/Z_T^2 gives
P_2T(g at 0 and T). So the ratio is P_2T(g, g)/P_T(g)^2, which lies in
[1 - 2 sqrt(q), (1 - sqrt(q))^(-2)]. The retained sign dimension is
sum_(i <= 2N sqrt(q)) C(2N-2, i) = exp(o(N)) since q -> 0. P_g is a position
multiplication, so it commutes with e^(isY) and the Section 9 dephasing applies
inside it.

**Scope, L477. HOLDS.** Traces of a product transfer factor, so J adds over
factors. For U(1) the linear modes carry no SO(3), so the degree-one ratio
e^(-omega) survives, and the open-box deficit is still ~ sqrt(kappa) ~ 1/B.
Finite groups have no continuous chart near 1. The final clause uses row 865's
W-phys-CA (conditional on its premises, as "on witness sizes" says): with the
identity rest, J >= log Tr(K_h/lambda^h) >= log(1 + e^(-M_K a_j h)) -> log 2.

**OPEN paragraphs (L17, L211, L295-300, L479). They claim nothing beyond the
proved statements.** L479's restatement of the target as
limsup E[1 - Tr(tau_l tau_k)] < 1/1651 is (1)-(2). The list of what defeats each
method matches Sections 3, 7, 9, 12 and 13.

**GUIDE paragraphs (L3, L5, L7, L11, L305). Not proof steps.** L11 matches
row 1147 Section 12: J_D(beta) - J_D(u_*) is the signed integral,
J_D(u_*) -> 0 by row 1147 (27)-(28), and h = 1 + H floor(n/(H log n)). L7's
remark that the one-loop coefficient is conditional where it is used matches
L336. I did not open the external links.

**Summaries L13, L15 and RESULT line L481. HOLD.** They state (33), the Section 5
restoration with |Sigma'| <= C n^3/beta^theta per layer over a slab with
a_j h_2 -> 0, and (20)-(22) with the sharp scale n^3 beta v^2 = o(1) (from
(20)-(21)). (15), (W) and the gap are marked OPEN. "Pending independent check":
this file is that check.

GUIDE run (pure Python, standard library, script `guide.py` in this session's
scratchpad folder `row1150`, not kept in the repository; peak memory a few MB).
1. The W_r generating function: max relative error 1.3e-11 on 200 random
(r, t). 2. max_d a_beta(d) e^((d-1)/sqrt(beta)) = 1.08, 1.37, 1.50, 1.57 at
beta = 4, 25, 100, 400, so bounded (it tends to e^(1/2) = 1.65).
2b. (1 - r_beta) beta = 1.37 to 1.50, so 1 - r_beta <= C/beta. 3. Alternating lag
sum / (H/4) <= 0.632 on the tested (a, H). 4. Mehler composition: A_r, D_r match
sinh(omega) coth(r omega) and sinh(omega)/sinh(r omega) to 1e-15. 5.
3 pi^2/11 = 2.69 > 2. 6. 1/(s + d_0) = e^(-omega) to 1e-15. 7.
1 - e^(-log(1651/1650)) = 1/1651. 8. I_(j+1)/I_j is increasing on a grid
(j = 1..5). 9. z_(beta/2)/z_beta -> 2^(3/2). All agree with the hand arguments.
They are a guide only.

## Step 8. Verdict table and result

Precision notes (none changes a constant that matters or a conclusion).
(a) L52: the ball and normalizer cost is in fact e^(-CE), since the powers of
beta combine to beta^(3d/2) >= 1. The file's e^(-CE log(2+beta)) is a valid
weaker bound. (b) L174: any guard width >= 1 already keeps a small box from
meeting two large boxes. (c) (20): the proof gives the second term as
C n^2 (1+beta)^3 e^(-cn/(1+beta)), which is smaller than the stated
C N (1+beta)^3 e^(-cn/(1+beta)). (d) L195: for the large factors the box-gap scale
(L178) gives inverse deficit <= CB. The file uses the weaker CB^2, which is
enough.

Scope remarks (not corrections). (a) (15) and (22) are exact restatements of
(30), and so of row 1145 (24) and of (W) through row 720. They carry no estimate
of their own. (b) The positive estimates ((5), (14), (20), (27), (30a), (33))
are small-coupling or cold-seam statements on modified cylinders. They are not
selective in the sense of the brief, Section 4, and the file says so at L477.
(c) The statements that use row 865's W-phys-CA (L351, the last clause of
L477) or the account's one-loop coefficient (L336) are conditional on those
premises, as the file labels them.

| # | Statement (line in `gap-solve4-astra62.md`) | Verdict |
|---|---|---|
| 1 | (1), purity identity (L21-26) | HOLDS |
| 2 | (2), two-replica expression (L28-37) | HOLDS |
| 3 | Seam interpolation weights prod a_(v_e)(d_e) (L39) | HOLDS |
| 4 | Section 2 set-up: reversible D_r, sup D_r <= e^(C_1(1+beta)E) (L44-50) | HOLDS |
| 5 | (3) (L52-56) | HOLDS (precision note a) |
| 6 | (4), stopping argument, cost o(beta) (L58-68) | HOLDS |
| 7 | (5), interval up to u_1 (L71-83) | HOLDS |
| 8 | a_beta(d) <= C e^(-(d-1)/sqrt(beta)), W_r, one-dimension norms (L95-104) | HOLDS |
| 9 | (7) (L106-111) | HOLDS |
| 10 | (6) (L88-93, L113-117) | HOLDS |
| 11 | (8) and the close-pair remark (L119-125) | HOLDS |
| 12 | Section 4 setting, (9), rooted coordinates, lambda_0 >= e^(-CE) (L130-146) | HOLDS |
| 13 | Linear coercivity V, Q >= cB^(-4) (L148) | HOLDS |
| 14 | (11) and b_beta (L150-155) | HOLDS |
| 15 | Endpoint and gauge tails, t_beta (L157-159) | HOLDS |
| 16 | Pointwise comparison, norm bound C beta^(-1/10) lambda_0 (L161) | HOLDS |
| 17 | (10) and deficit >= cB^(-2) (L134-142, L163) | HOLDS |
| 18 | (12) and the grouping geometry (L168-172) | HOLDS |
| 19 | Factor structure with all double crossings kept (L174) | HOLDS (precision note b) |
| 20 | (9) for the large factors (L176) | HOLDS |
| 21 | Box-gap scale kappa in [c/B^2, C/B^2], deficit in [c/B, C/B] (L178) | HOLDS |
| 22 | c_*, theta, mixing cost o(beta), unprojection, cell error <= sigma (L195-200) | HOLDS (precision note d) |
| 23 | (13)-(14), v_2/u_* -> infinity, h_2 = polylog(n) (L180-193, L202) | HOLDS |
| 24 | Monotone restoration path (L204) | HOLDS |
| 25 | (15) <=> (30), size of D'_j, fraction O(b/B) (L206-211) | HOLDS |
| 26 | (16) (L216-222) | HOLDS |
| 27 | M_0 >= c(n/B)^3 residual faces with disjoint factors (L224) | HOLDS |
| 28 | (17) and the time cost of order beta log n (L226-231) | HOLDS |
| 29 | Marked expansion fails for v sqrt(H_2 beta) >= C (L233) | HOLDS |
| 30 | (18) (L238-243, L255) | HOLDS |
| 31 | (19) (L245-253) | HOLDS |
| 32 | Centre-averaged rest and rank-one vacuum rest (L257-263) | HOLDS |
| 33 | (20) and the exterior-uniform conclusion (L268-285) | HOLDS (precision note c) |
| 34 | (21) and necessity of N beta v^2 -> 0 (L287-291) | HOLDS |
| 35 | Retained fraction 1/3 for one-step estimates (L293) | HOLDS |
| 36 | (22) <=> (30) (L295-300) | HOLDS |
| 37 | (23) (L307-317) | HOLDS |
| 38 | (24) (L319-325) | HOLDS |
| 39 | (25) (L327-331) | HOLDS |
| 40 | Local coherences, k = o(e^beta/beta^(3/2)) (L333) | HOLDS |
| 41 | Freezing all signs fails (L336) | HOLDS, the one-loop step conditional as labelled |
| 42 | Equal-time dephasing (L338) | HOLDS |
| 43 | (26) (L346-351) | HOLDS, the witness remark conditional as labelled |
| 44 | Chart failure on the torus and on long open cores (L353) | HOLDS |
| 45 | Scalar comparison model (L356-366) | HOLDS |
| 46 | Bridge estimate ||D_s - 1|| <= Ce^(-cs/r) (L378) | HOLDS |
| 47 | (28) (L380-386) | HOLDS |
| 48 | (29) and the L^q bound (L388-401) | HOLDS |
| 49 | (27) and the conditional activity bound (L371-376, L403) | HOLDS |
| 50 | Boundary limit of (29) (L405) | HOLDS |
| 51 | Bookkeeping estimate (L417-421) | HOLDS |
| 52 | First integration, (31) (L423-428) | HOLDS |
| 53 | Interior double zero (L430) | HOLDS |
| 54 | Boundary terms and guards (L432) | HOLDS |
| 55 | Second integration, (32) (L434-440) | HOLDS |
| 56 | Separation and (30a) (L410-415, L442) | HOLDS |
| 57 | Cost of the uniform prescription (L444) | HOLDS |
| 58 | Projected representation with frames k_t (L456) | HOLDS |
| 59 | Locality in the temporal gauges (L458) | HOLDS |
| 60 | Connected support after removing frames (L460) | HOLDS |
| 61 | Factorization of the (X, g) measure, projected bridges (L462) | HOLDS |
| 62 | (33) and the k = 1 variance test (L449-454, L464) | HOLDS |
| 63 | (34) (L469-475) | HOLDS |
| 64 | Scope of the obstructions (L477) | HOLDS, the last clause conditional on W-phys-CA |
| 65 | Summaries L13 and L15 | HOLDS |
| 66 | RESULT line (L481) | HOLDS |

No statement FAILS. No correction is needed. Four precision notes, none of
which changes a conclusion. No mass gap is claimed by the file or by this check.

RESULT: HOLDS — check of row 1149 (`library/gap-solve4-astra62.md`), checked line by line by hand by Claude Opus 5.5 (max effort), positive claims first: the full-strength restoration of Section 5 ((12)-(15), the box-gap scale c/B to C/B, the monotone path), with its inputs (3)-(4), (5) and the Gaussian operator comparison (10); the one-step reduction (20)-(22); the two-stage expansion of Section 12 and the projected restoration (33) of Section 13 — all HOLD, as do (1)-(2), (6)-(8), (16)-(19), (23)-(29), (34) and every obstruction (those using W-phys-CA or the one-loop coefficient conditionally, as labelled); 66 statements, 0 FAILS, 0 corrections, 4 precision notes; (15) and (22) are exact restatements of (30) with no estimate of their own, and the strict bound in (15), (W) and the four-dimensional SU(2) mass gap stay OPEN.
