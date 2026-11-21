lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T07:39Z

# Check of row 1013 (`gap-invent-selective-max`): work items W1 and W2

Row 1015 (`gap-invent-selective-check-opus`), queued 2026-11-15 19:39Z on Mac mini worker 3.
Checker: Claude Opus 5.5, max effort. Author of the checked file: Claude Fable 5.2 (row 1013).
Same provider, so this is a second reading, not an independent check in the sense of the working
rules; where a step below uses a different derivation from the author's, it says so.
Source pinned: branch `claude/ym4d-hard-route` at commit b9125417f.
Checked file: `library/gap-invent-selective-max.md` (row 1013), section 7.3, work items W1 and W2.
W2 is read against `library/gap-pinned-cell-gauge-max.md` (row 1011).
No new attack (row text). Marks: PROVED, ARGUED, OPEN, FAILS; for a checked claim:
CONFIRMED, CONFIRMED WITH CORRECTION, NOT CONFIRMED, FALSE.

## Plan (at most eight steps; one step per response, result appended before the next)

1. Read FINISH.md rules for this row, row 1013 section 7.3 (W1, W2, stop rule) and the statements
   and proofs of Lemma WN, Corollaries WN1-WN3, Lemmas TWIST, JEN, SLAB. Record the exact
   checklist here.
2. W1 tests (a)-(e), as written in 7.3, before any proof reading.
3. Lemma WN (i)-(iii) and Corollaries WN1-WN3: line-by-line check, own derivation where possible.
4. Lemma TWIST: line-by-line check.
5. Lemmas JEN and SLAB: line-by-line check.
6. The two ARGUED remarks of W1; apply the stop rule.
7. W2 against row 1011: its three answers.
8. Verdict table, what stays open, RESULT line.

## Progress log

Status: COMPLETE. All eight steps are written below; the verdicts and the RESULT line are in Section 8.

- File created and plan written shortly after 19:39:43Z (date -u at the session start). Step 1 next.

## 1. Step 1 result: inputs, repo search, checklist

**Read in full.** `GOAL.md`; `FINISH.md` L1-84, L299-351, rows 1013, 1015, 1016 (L1094-1097);
`library/gap-invent-selective-max.md` L1-112 and L128-299 (plan, Sections 1-2, candidates C1-C3 and
C8, Sections 4-8). The rest of Section 3 (C4-C7, C9) is not read; W1 does not ask for it.

**Repo search** (grep over this folder for `Lemma WN`, `Lemma JEN`, `Lemma SLAB`,
`gap-invent-selective`, `corner graph`). No earlier check of row 1013 exists. One name clash:
`library/gap-direction2-max.md` L162 (row 970) has a different "Lemma SLAB" (transfer matrix,
infinite time extent). In this file "Lemma SLAB" always means row 1013 Section 5.2.

**Duplicate check (rule 0a).** This row checks proofs; it attacks no open lemma, so there is
nothing to match against `library/open-core.md`. W1's stop rule: no new attack.

**Checklist (W1 exactly as written in row 1013 7.3).**

- Tests first: (a) the sign rule of WN (i) for a link traversed backward; (b) one plaquette,
  density exp(beta x) on SU(2): (beta/3) E(1 - x^2) = E x by one integration by parts with weight
  (2/pi) sqrt(1 - x^2), so rho = 0; (c) in WN (iii), the gauge average at one free site kills each
  cross term, and the closed word passes that site once (sides at least 3); (d) the count "three"
  in WN1; (e) in JEN (ii), the averages at the four corner sites may be taken one after the other.
- Then line by line: Lemma WN (i)-(iii), Corollaries WN1-WN3, Lemma TWIST, Lemma JEN (i)-(ii),
  Lemma SLAB (identity).
- Then judge two ARGUED remarks: "the best lab-frame bound is of order beta eta^2 R" (5.1) and
  Proposition LOC (4.3).
- Report the first failing step, or none.

**W2** (row 1013 7.3): read row 1013 5.1-5.2, then answer for row 1011's construction
(`library/gap-pinned-cell-gauge-max.md`): (1) its blind bound on the stiffness of a cell of side R,
beta or beta R, and if beta, what supplies it; (2) does its class contain two pinned parallel
hyperplanes at distance below beta, or non-cubic cells; (3) does its iteration run at one fixed bare
coupling without the account's effective actions. Row 1015 puts the three answers in this file.

**Conventions fixed for the check** (from row 1013 4.1). SU(2) as unit quaternions,
U = x + i y.sigma, x = (1/2) tr U, c = i sigma_3, c^2 = -1. Then (1/2) tr(c U) = -y_3 and
(1/2) tr(c^2 U) = -x (checked: (1/2) tr(i sigma_3 (x + i y.sigma)) = (1/2) tr(i x sigma_3 - y_3) = -y_3).
The weight is exp(H), H = sum_p beta_p x_p, x_p = (1/2) tr U_p.

- step 1 done. (time not measured) Step 2 (tests (a)-(e)) next.

## 2. Step 2 result: W1 tests (a)-(e), each redone by hand

Notation. A plaquette p is a closed path x_1 -> x_2 -> x_3 -> x_4 -> x_1 with four distinct sites;
V_i is the factor of the link between x_i and x_(i+1): V_i = U_l if l runs from x_i to x_(i+1),
V_i = U_l^(-1) if l runs from x_(i+1) to x_i; U_p = V_1 V_2 V_3 V_4. tau_t sends
U_l -> e^(t F(l,s) c) U_l e^(-t F(l,e) c), s and e the start and end of l.

**(a) Sign rule for a backward link: PASSES.** If p runs along l from e to s (backward), its factor
is U_l^(-1), and tau_t sends it to e^(t F(l,e) c) U_l^(-1) e^(-t F(l,s) c). The left exponential
carries F at e, the site where p leaves along l; the right one carries F at s, where p arrives. For
a forward link the same holds with s and e exchanged. So at a corner x_i, arriving by l and leaving
by l', the two adjacent exponentials are e^(-t F(l,x_i) c) e^(+t F(l',x_i) c) = e^(t theta_i c),
theta_i = F(l',x_i) - F(l,x_i), since both lie on the axis c. The pair at x_1 is split between
the two ends of the word and joins by cyclicity of the trace. Reversing the orientation of p sends
every theta_i to -theta_i and the word to its inverse; since tr U = tr U^(-1) on SU(2), the value
is unchanged, so the choice of orientation is immaterial.

**(b) One plaquette: PASSES.** Under Haar measure on SU(2) = S^3 the law of x = (1/2) tr U has
density (2/pi) sqrt(1 - x^2) on [-1, 1] (the slice at fixed x is a 2-sphere of area
4 pi (1 - x^2), and the arc element is dx/sqrt(1 - x^2); the integral of sqrt(1 - x^2) is pi/2).
With the weight e^(beta x):
 0 = integral over [-1,1] of d/dx [ e^(beta x) (1 - x^2)^(3/2) ] dx
   = beta * int e^(beta x) (1 - x^2) sqrt(1 - x^2) dx - 3 * int x e^(beta x) sqrt(1 - x^2) dx,
the boundary terms being 0. Divide by int e^(beta x) sqrt(1 - x^2) dx: beta E(1 - x^2) = 3 E x.
So rho = E x - (beta/3) E(1 - x^2) = 0 for a single plaquette of free links. Second derivation (a
different route, used as a cross-check): for one plaquette, W(t) = E exp(beta [x(e^(t theta c) U) - x(U)])
= 1 for all t by left invariance of the Haar law of U_p, so -W''(0) = 0, which is WN2's formula
theta^2 beta [E x - (beta/3) E(1 - x^2)] = 0. Both agree.

**(c) Cross terms in WN (iii): PASSES.** The cross term of corners i < j is
(1/2) tr(c P_ij c P_ji), P_ij = V_i ... V_(j-1), P_ji = V_j ... V_(i-1), P_ij P_ji the holonomy
based at x_i. Let x_i be free (the case x_j free is the mirror image). The gauge map at the one
site x_i, V_(i-1) -> V_(i-1) h^(-1), V_i -> h V_i (true for forward and backward links by (a)),
touches only integrated links (x_i is free), keeps Haar measure and every x_q. Because the four
sites of p are distinct, the word passes x_i once, so P_ij -> h P_ij and P_ji -> P_ji h^(-1), and
the term becomes (1/2) tr(h^(-1) c h P_ij c P_ji). Average over h (Fubini; the trace is linear in
the inserted matrix): int h^(-1) c h dh is an Ad-invariant element of su(2), hence 0 (Schur). So
each cross term has mean 0. Distinct sites need only sides at least 2; the file's "at least 3" is
sufficient, not a defect.

**(d) The count "three" in WN1: PASSES.** For p = (x; mu, nu), mu < nu, traversed x, x+mu,
x+mu+nu, x+nu: links l_1 = (x,mu) forward, l_2 = (x+mu,nu) forward, l_3 = (x+nu,mu) backward,
l_4 = (x,nu) backward. With F = f at starts and 0 at ends the corners are:
x: f(x,mu) - f(x,nu); x+mu: f(x+mu,nu) - 0; x+mu+nu: 0 - 0 (end of l_2, end of l_3);
x+nu: 0 - f(x+nu,mu) (leave by l_4 at its end, arrive by l_3 at its start). This matches the file.
A link of direction d is the second link of the d - 1 plaquettes with mu < d = nu, and the third
link of the 4 - d plaquettes with d = mu < nu: d - 1 + 4 - d = 3. So the form is at least
3 |f|_2^2. The same count for first and fourth positions gives the upper bound: the form is at
most 2*3 + 3 = 9 times |f|_2^2. In dimension D the two counts are D - 1 each.

**(e) JEN (ii), corner averages one after the other: PASSES.** The sites of p are distinct, so
the gauge maps at the free corner sites with theta not zero act on disjoint sets of factors:
the map at x_i conjugates only the insertion at x_i, e^(eta theta_i c) -> h_i^(-1) e^(eta theta_i c) h_i.
Each map keeps the measure E_u (the site is free; no pinned link moves). Average at the first
site: by linearity of the trace in that insertion and int h^(-1) (cos + sin c) h dh = cos, the
insertion becomes the scalar cos(eta theta_i). A scalar commutes with all factors, so the next
site's average sees the same form. After all sites, E_u[x_p o tau_eta] = prod cos(eta theta_i) E_u[x_p];
corners with theta = 0 contribute cos 0 = 1. (One may also average over independent h_i at once.)

**Summary of step 2.** Tests (a)-(e) pass. One imprecision found on the way, recorded for step 3:
WN1 writes one number xbar = E x_p for all plaquettes; on a torus with unequal sides E x_p can
depend on the plane (mu, nu). With equal sides (hypercubic symmetry) it is one number.

- step 2 done. (time not measured) Step 3 (WN (i)-(iii), WN1-WN3 line by line) next.

## 3. Step 3 result: Lemma WN (i)-(iii) and Corollaries WN1-WN3, line by line

**WN (i): CONFIRMED.** Redone in test (a). The identity is algebraic and holds for every real
link-end field F (pinned ends included); the orientation of p does not matter.

**WN (ii): CONFIRMED.** U -> a U b with fixed a, b keeps Haar measure on SU(2) (bi-invariance);
F = 0 on pinned ends, so tau_t moves only integrated links, one link at a time. Hence
int exp(H o tau_t) = int exp(H), i.e. E exp(H o tau_t - H) = 1.

**WN (iii): CONFIRMED.** With g(t) = H o tau_t - H, (ii) gives E e^(g(t)) = 1. The integrand is
smooth on a compact product of groups, so differentiation under the integral is allowed:
E[g'(0)] = 0 and E[g''(0) + g'(0)^2] = 0, i.e. E[D] + E[X^2] = 0. The second derivative of
(1/2) tr(prod e^(t theta_i c) V_i) at 0 is sum_i theta_i^2 (1/2) tr(c^2 U_p) plus
sum over i != j of theta_i theta_j (1/2) tr(c P_ij c P_ji), and c^2 = -1. This is the file's D.
The cross terms vanish in mean by test (c). The hypothesis of (iii) is exactly what (c) needs.

**WN1: CONFIRMED, with one precision.** Corner values and the count 3: test (d). Second
derivation (different route, not in the file). The corner sum equals, site by site, the Laplacian
form of the corner graph at that site: in 4D a site has 8 link-ends (x, +mu) (starts) and
(x, -mu) (ends), and a corner joins two link-ends of different directions, so the graph is
K_(2,2,2,2) with 24 edges, one per plaquette through x. Its Laplacian spectrum is 0 (once),
6 (four times, vectors (1, -1) on one pair {+mu, -mu}), 8 (three times). For a left-translation
field the values at x are f(x, mu) on the four starts and 0 on the four ends. So
|F - mean|^2 = sum_mu f(x,mu)^2 - (sum_mu f(x,mu))^2/8 >= (1/2) sum_mu f(x,mu)^2 by Cauchy-Schwarz,
and the form at x is at least 6 * (1/2) sum_mu f(x,mu)^2 = 3 sum_mu f(x,mu)^2. Summed over sites:
the file's bound 3 |f|_2^2, and an upper bound 8 |f|_2^2. **New: the constant 3 is attained**, by
every f with f(x, mu) = a_x independent of mu (then F - mean is (a_x/2)(1, -1) on each pair, an
eigenvector for 6, and Cauchy-Schwarz is an equality). Precision: E x_p is one number xbar only
when the torus has equal sides (hypercubic symmetry); otherwise read xbar as the plane-dependent
mean and the bound with its minimum. xbar >= 0 is not an extra assumption: E[X(f)^2] >= 0 and the
form is positive for f != 0, so beta xbar >= 0 follows from the identity.

**WN2: CONFIRMED.** W(t) is no longer constant (theta need not be delta F). W'(0) = E[X] with
X = sum beta_p theta_(p,x) (1/2) tr(c U_(p,x)) = -sum beta_p theta_(p,x) y_3(U_(p,x)), U_(p,x) the
holonomy of p based at x. The gauge map at the free site x sends U_(p,x) -> h U_(p,x) h^(-1), so
y(U_(p,x)) -> R(h) y(U_(p,x)), R(h) in SO(3) Haar-distributed; hence E[X] = 0. W''(0) = E[D] + E[X^2].
Cross terms of D (two non-zero corners of one plaquette, distinct free sites): mean 0 by test (c).
Cross terms of E[X^2] at distinct sites x != x': the gauge map at x rotates y(U_(p,x)) and leaves
U_(p',x') unchanged (a holonomy based at x' != x sees h^(-1) h at x), so the mean is 0. Diagonal:
the Haar average over SO(3) of (R y)_3^2 is |y|^2/3, and |y|^2 = 1 - x_p^2. So
-W''(0) = sum theta^2 [beta_p E x_p - (beta_p^2/3) E(1 - x_p^2)], as stated. The hypothesis
"pairwise distinct free sites" is used twice: at most one non-zero corner per site (for E[X^2]),
and freeness (for E[X] and the cross terms).

**WN3: CONFIRMED (identity), same precision as WN1.** F = 1 at the start s of l, 0 elsewhere:
each of the six plaquettes through l, oriented to leave s along l, has theta = 1 at s (leave by l:
F = 1; arrive by a link whose end at s carries 0) and theta = 0 at its other corners. (iii) gives
E[X^2] = 6 beta xbar, X = -beta sum_q y_3(U_(q,l)), so E[(sum_q y_3)^2] = 6 xbar/beta. All six
holonomies are based at s; the gauge map at s rotates their sum Y by one R(h), so
E|Y|^2 = 3 E[Y_3^2] = 18 xbar/beta. Subtract the diagonal sum_q E(1 - x_q^2) = 6 E(1 - x^2)
(equal sides) and multiply by beta/18: rho = (beta/18) sum_(q != q') E[y_q . y_q'].

**On the ARGUED remarks inside WN3 (not on W1's list; consistency only).** (1) The free-field
count is right: in the Gaussian limit each of the 3(d - 1) physical modes per site carries 1/2 of
action and a site has d(d - 1)/2 plaquettes, so beta E(1 - x_p) -> 3/d, i.e. 3/(4 beta) in d = 4
and 3/(2 beta) for one plaquette (3 modes). With 1 - x^2 ~ 2(1 - x), rho -> 1 - (2 beta/3)(3/(d beta))
= 1 - 2/d: 1/2 in d = 4, and 0 in d = 2, where a planar gauge field with free boundary is a product of
independent plaquettes, so rho = 0 exactly. Consistent. (2) Wording: WN3 says a proof of rho > 0
at large beta "needs E(1 - x_p) < 3/(2 beta)". From 1 + x <= 2, rho >= 1 - (1 + 2 beta/3) E(1 - x),
so the sufficient condition is E(1 - x_p) < 3/(3 + 2 beta), as 7.3 writes; 3/(2 beta) is only its
leading order and is not sufficient by itself. Not used by any PROVED statement.

- step 3 done. (time not measured) Step 4 (Lemma TWIST) next.

## 4. Step 4 result: Lemma TWIST, line by line

**CONFIRMED, and it holds more generally than stated.** Let Omega~ = Omega on the sites that carry
a pinned link and 1 elsewhere. The gauge map U_l -> Omega~(s) U_l Omega~(e)^(-1) is, on each
integrated link, a left and a right translation by fixed elements, so it keeps the Haar measure of
the integrated links. It sends the pinned data u to u^Omega, and it keeps every plaquette trace.
Hence Z(u) = int exp H(u, U) dU = int exp H(u^Omega, U^Omega~) dU = Z(u^Omega). Nothing in the proof
uses the shape of the region, the choice of the pinned set, or continuity of Omega~ at the
boundary: an integrated link whose two ends are both boundary sites (a chord) is also moved by fixed
translations. (In a lattice cube every link between two boundary sites lies in a face, so no chord
occurs there.) Stronger form, same proof: the conditional law given u^Omega is the image of the law
given u under Omega~, so every gauge-invariant conditional expectation is unchanged too.

**Consequences in the file: CONFIRMED.** Z of a pinned cell depends on the gauge orbit of the data
only; no winding label of Omega is visible to Z, so C3 as written (Z_k against Z_0) is void. What
TWIST does not say: with an admissibility constraint on plaquettes (as in Luscher's admissible
fields) sectors exist, and a small-curvature extension of winding data can still be obstructed.
That concerns the refilling test K8 and row 1013 6.3, which W1 does not ask me to check.

- step 4 done. (time not measured) Step 5 (Lemmas JEN, SLAB) next.

## 5. Step 5 result: Lemma JEN (i)-(ii) and Lemma SLAB, line by line

**JEN (i): CONFIRMED.** Apply tau_eta to all links. On a pinned link l it gives
e^(eta a_l c) u_l e^(0) = u^(eta)_l, because F = a_l at the start and 0 at the end. On integrated
links it is a Haar-preserving translation. So
Z(u^(eta)) = int exp H(u^(eta), U) dU = int exp H(u^(eta), tau_eta U') dU' = Z(u) E_u exp(H o tau_eta - H),
where H o tau_eta is H after tau_eta on every link. Jensen (exp convex, Z(u) > 0) gives the bound.
The proof needs Lemma WN (i) only as an identity for each plaquette; WN (i) holds for any F.

**JEN (ii): CONFIRMED.** Test (e). It needs the four sites of p distinct and every corner with
theta != 0 at a free site; corners with theta = 0 give cos 0 = 1 whatever their site.

**"What it gives": CONFIRMED as a reading of (i)-(ii), with one remark.** For plaquettes whose
non-zero corners are all free, E_u[x_p - x_p o tau_eta] = E_u[x_p](1 - prod cos(eta theta)), which is
(eta^2/2) E_u[x_p] sum theta^2 + O(eta^4). The other plaquettes ("at pinned sites") can carry a
first-order term; their sum is -eta E_u[X] = -eta (d/d eta) log Z(u^(eta)) at 0, so it vanishes
exactly when u is a critical point of the twist. For u = 1 it vanishes plaquette by plaquette (the
constant gauge map by i sigma_1 keeps the data 1 and sends y_3 -> -y_3). Step 6 uses this.

**SLAB (identity): CONFIRMED.** Region {0, 1} x B, links of both slices pinned. A plaquette that
contains an integrated link g(y) = U_4(0, y) is a (mu, 4) plaquette at time 0; going
(0,y) -> (0,y+mu) -> (1,y+mu) -> (1,y) -> (0,y) its factors are A_mu(y), g(y+mu), A'_mu(y)^(-1),
g(y)^(-1), so x_p = (1/2) tr(A_mu(y) g(y+mu) A'_mu(y)^(-1) g(y)^(-1)), as stated. In-slice plaquettes
are constants. For A = A' = 1, (1/2) tr(g h^(-1)) = q_g . q_h (unit quaternions as vectors of R^4),
so the law is the O(4) model exp(beta sum q_y . q_(y+mu)). The same identity holds when the two
slices sit inside a larger lattice: every plaquette that contains U_4(0, y) is a (mu, 4) plaquette at
time 0, so given the two slices the links between them decouple from the rest.

**SLAB (consequence): the ARGUED step is sound as written.** With A = A' = 1 the loop "up at y,
along slice 1, down at y', back along slice 0" has trace (1/2) tr(g(y) g(y')^(-1)) = q_y . q_y'. On a
3D torus B, Frohlich, Simon and Spencer (1976; RECALLED, not rebuilt) give long-range order of the
O(4) model at large beta. So a class that contains these pins at weak coupling has no uniform
mixing. The pins are atypical (data 1); that is enough against a statement uniform over pins, and
it says nothing about typical data, as the file's wording already implies.

- step 5 done. (time not measured) Step 6 (the two ARGUED remarks) next.

## 6. Step 6 result: the two ARGUED remarks of W1

### 6.1 "The best lab-frame bound is of order beta eta^2 R" (row 1013 5.1): CONFIRMED at the trivial pin, second order in eta, with the minimisation now written out

The file leaves the minimisation over F unwritten. Here it is, for the cube c = {0..R}^4, R >= 3,
pin u = 1, small eta, axis c fixed (the lab frame). Notation as in Section 2 of this file.

**Step A (where the non-free corners sit).** A site is free iff it is interior. For a plaquette p in
the plane (mu, nu) whose two other coordinates are interior, the four sites and links are a unit
square inside [0, R]^2: a corner of it is a boundary site iff it lies on an edge of the square that
lies on the boundary of [0, R]^2 (R >= 2). So the non-free corners of p form an arc joined by pinned
links: none, one pinned edge (two corners), or two pinned edges at a corner of [0, R]^2 (three
corners). If another coordinate is 0 or R, p lies in a face: all four links pinned.

**Step B (the second derivative, exactly).** Let D_p be the second t-derivative of x_p o tau_t at 0.
Cross terms with a free corner have mean 0 (test (c)). For two non-free corners i, j, one of P_ij,
P_ji runs along the pinned arc, so it is 1, and (1/2) tr(c P_ij c P_ji) = (1/2) tr(c^2 P) = -x_p. Hence
 -E_1[D_p] = E_1[x_p] [ sum over free corners theta^2 + (sum over non-free corners theta)^2 ].
The first-order terms vanish plaquette by plaquette (Section 5, the i sigma_1 symmetry of the pin 1).
So the Jensen exponent of JEN (i) is (eta^2/2) J(F) + O(eta^3), J(F) = sum_p beta_p (-E_1 D_p).

**Step C (the minimisation decouples).** A corner value theta is a difference of two link-end
values at one site, and each link-end belongs to one site. So the free corners use only the values
at free sites, the non-free corners only the values at boundary sites. The free part is minimised,
to 0, by F constant at each free site (for instance F = 0 on every link-end at a free site). For the
non-free part: a fully pinned p contributes beta_p ((da)_p)^2, fixed (the sum of theta around p is
the oriented sum of F(l,s) - F(l,e) = a_l). A plaquette with one pinned edge l contributes
beta_p E_1[x_p] (a_l + phi(head of l) - phi(tail of l))^2 (l traversed forward), where phi(z) is the
value on the integrated link-end of p at the end z of l. At a boundary site interior to a 3-face there is exactly one integrated link-end
(the inward link), so phi is one function on those sites and the term is (a + d phi)_l^2. The way a_l
is split between the two ends of l does not enter.

**Step D (the size).** Let c_* = min of E_1[x_p] over all plaquettes of c, assumed > 0 (then every term of J is >= 0,
and the terms not used below may be dropped). Then
 min over F of J >= c_* beta * min over phi of sum over face-interior boundary links (a + d phi)_l^2,
and J at F = 0 on every link-end of an integrated link is at most beta (sum over pinned-face plaquettes ((da)_p)^2 +
C |a|^2), C an absolute constant (a pinned link lies in at most a fixed number of plaquettes with a
pinned edge). Take a = delta psi on the grid of face-interior sites of one face (psi a 2-cochain on
that grid, a bump of height 1 vanishing near the edge of the face; a = 0 on the other faces). Then
delta a = 0 on that grid, so <a - d phi, a> = |a|^2 for every phi, and the minimum is at least
|a|^2, which is of order R^3 * R^-2 = R; da is of order R^-2, not 0. The upper side is also of
order R. So the best lab-frame bound is of order c_* beta eta^2 R, while the classical action of
the smooth extension is of order beta eta^2 (field strength eta/R^2 on R^4 plaquettes). The factor R
is confirmed.

**Limits of this confirmation.** (1) The pin is 1. For a non-abelian pin the arcs carry products of
u, the cross terms are no longer -x_p, and the fixed axis c fits even worse; not computed.
(2) c_* > 0 is not proved here (expected near 1 at large beta). (3) "curl not zero" in the file must
be read as "a smooth profile whose non-gradient part is of size 1/R on a positive fraction of the
boundary"; a curl supported on one plaquette gives an O(1/R^2) bound, not R. (4) Only axis-c fields;
su(2)-valued field-independent F gives the same structure (free corners decouple by the same gauge
average), not written out. (5) Second order in eta only.

**Agreement with row 1011 (a different construction, same provider; not an independent check).**
Row 1011 Proposition A (ii) writes the stiffness as a direct term minus Var X; dropping Var X is the
second-order Jensen step, so its direct term is J above. Row 1011 Proposition SEAG finds the
direct term of a curl-free interior field is 36 b E[t_p], not 0: the white-noise term of Lemma WN.
Row 1011 4.2 (reading) finds the class supremum at least of order b S times the classical action.
Step D is the fixed-pin counterpart: even at the pin 1 the lab-frame bound carries the factor R.

**The consequence drawn in 5.1 ("even the blind first step needs the account's effective
actions"): stays ARGUED.** What is shown is that no field-independent axis-c move does better than
beta eta^2 R. Field-dependent moves (C8) and other inequalities are not covered; the file's reason
against C8 (frames decohere after a length of order beta, RECALLED) is a heuristic. Row 1011 SEAG
calls the bound "H_c(1; a theta) <= b times the classical action" OPEN, which is the same gap.

### 6.2 Proposition LOC (row 1013 4.3): ARGUED stands as a summary; two corrections; not a classification theorem

- Item 1 (moves that keep the action are gauge maps): **CONFIRMED for field-independent moves.**
  For two-sided translations U_l -> L_l U_l R_l^(-1) the plaquette word gets one insertion G_i per
  corner. If tr(G_1 V_1 ... G_4 V_4) = tr(V_1 ... V_4) for all V_i, then with V_2 = V_3 = V_4 = 1 the
  product of the G's is 1 (unit quaternions span H), and then tr(V G_2 W G_2^(-1)) = tr(V W) for all
  V, W forces G_2 central; likewise each G_i. So every corner insertion is +1 or -1: the move is a
  gauge transformation times a closed centre field. Row 1011 Lemma CEN proves the one-sided case and
  Corollary CEN2 every compact group. Field-dependent maps that keep the action and Haar measure
  (field-dependent gauge maps with a triangular dependence) are not covered by item 1; they act
  trivially on gauge-invariant observables, so the item's conclusion "no signal" still holds for them.
- Item 2 (link-end translations have a corner-diagonal cost): **CONFIRMED** (Lemma WN; free sites).
- Item 3 (a): **CONFIRMED** given WN2: for the co-closed sheet on a torus every site is free and the
  base corners are distinct, so -W''(0) = beta rho A. Also any C^2 path g_t = exp(t xi + t^2 zeta/2 + ...)
  gives the same W''(0): the zeta term enters as (1/2) tr(zeta U_(p,x)), mean 0 at a free site. The
  smeared twist has the same W(t) exactly (axis-c insertions commute, tau keeps Haar). The kill of C2
  still needs rho > 0, which stays ARGUED.
- Item 3 (b): **CONFIRMED** by Lemma TWIST.
- Item 4 and the one-sentence reason: **ARGUED, with a wording correction.** "Its only global symmetry
  on link variables is the centre" is false as written: constant gauge maps U_l -> h U_l h^(-1) are a
  continuous non-abelian global symmetry of the link variables (and lattice symmetries exist too).
  They do not move gauge-invariant observables. Correct form, as row 1016 already states it: no
  continuous non-abelian group acts globally on the integration variables and moves gauge-invariant
  observables. "Can be filled in these ways only" has no defined class of moves: it holds for
  field-independent moves by items 1-3; for field-dependent moves it rests on C8 and the RECALLED
  decoherence length, so it is not a theorem.

### 6.3 Stop rule

W1 says: no new attack. Steps A-D above only write out the minimisation that 5.1 marks as not
written out; they claim nothing beyond the remark. No numeric run was made (none was needed: every
check above is a hand computation).

- step 6 done. (time not measured) Step 7 (W2 against row 1011) next.

## 7. Step 7 result: W2, the three answers for row 1011's construction

Read: row 1013 5.1-5.2 (Section 5 of this file checks them); row 1011
(`library/gap-pinned-cell-gauge-max.md`) 3.1-3.2, 4.1-4.5, 4.7, 7.1-7.5; the RESULT line of its
check, row 1014 (`library/gap-pinned-cell-gauge-check-opus.md` L534). Row 1014 does not hold these
three answers. Row 1013 7.3 asks for them "in the check file of row 1011"; row 1015's brief puts
them here, and this row edits no other file. The lead may copy them.

**(1) Blind bound on the stiffness of a cell of side R: it scales like beta R, not beta.**
Row 1011's blind bound is the direct term of its Proposition A (ii), the stiffness with Var X
dropped (the 2D start bound "H <= b"). For a fixed-colour field B = a theta this is the
second-order lab-frame Jensen exponent J of Section 6.1 of this file, with F(l, head) = 0. Its
size: (i) at the trivial pin, of order c_* beta eta^2 R for a smooth non-gradient boundary profile
(Section 6.1 here; second order; c_* > 0 assumed); (ii) at every pin, a curl-free interior field
already has direct term 36 b E[t_p], not 0 (row 1011 SEAG, confirmed by row 1014); (iii) over the
class, sup over pins is at least of order b S times the classical action (row 1011 B'; proved by
row 1014 only for boundary-only strengths, ARGUED for homogeneous strengths). No covariant
representative or theorem of the account supplies a bound of order beta in row 1011. Its
"H_c(1; a theta) <= b times the classical action of the harmonic extension" is OPEN (row 1011 4.4,
Meaning; row 1014: still OPEN). Lemma FR says every colour frame costs at least NA(omega)/6. The
supply it names, (N1)-(N2) of 7.4, is a ring-measurable covariant frame with small defect and a
controlled Ward identity about it (in the continuum, background gauge invariance). Row 1011 does
not cite the one candidate row 1013 5.1 names, Balaban's Ward-identity extraction of
(1/g_k^2) A(U_k(V)) on small fields (CMP 109 (0.22), Theorem 1; row 1012 B1).

**(2) Yes: the class contains non-cubic cells, and two pinned parallel hyperplanes at distance 1.**
Row 1011's cells are boxes, products of intervals {0..S_mu}, with cubes a special case (3.1). The
box {0..S}^3 x {0, 1} pins both slices x_4 = 0 and x_4 = 1 and the lateral faces. Its integrated
links are the temporal links over the open square; the plaquettes that contain them are not
boundary plaquettes, so w_p = 1. With every pin equal to 1 and strength b, this member is exactly
the 3D O(4) model of row 1013 Lemma SLAB, with fixed boundary spins instead of a torus. So SLAB's
consequence applies to C_b with one extra step: the order of the boundary-pinned 3D O(4) model at
large b (RECALLED in kind, not checked here; Frohlich-Simon-Spencer is a torus statement). Row 1011
4.5 itself embeds OpenAI's 2D class through the thin box {0,1,2} x {0,1} x {0..S}^2 (Lemma EMB,
confirmed by row 1014) and says that cubes with boundary pins only do not contain such sheets. Row
1011's failure verdict 4.7 does not use thin boxes: Propositions B, B', SEAG and Lemma CEN hold for
every box, cubes included.

**(3) It is posed at one fixed bare coupling with no effective actions, and no iteration runs.**
The class C_b uses bare Wilson cells with strengths in [0, b] (or |beta_p| <= b): one bare coupling,
no RG, no effective action. The iteration fails at its first piece: (M2), a twist with classical
direct cost, and (M3), the free start bound, FAIL for SU(2) (row 1011 4.7, 7.1; row 1014: 4.7
stands, no WRONG). The only repair row 1011 names, (N1)-(N3) of 7.4, reads typical fields of the
Wilson measure at small effective coupling. Row 1011 7.4 classes this as the (K-flow) kind with
first-passage data, and as a reading it says the repair does not cross the band by itself. This
agrees with row 1013 5.1's ARGUED consequence. Both files are by one provider in one session
family, so the agreement is not an independent check.

- step 7 done. (time not measured) Step 8 (verdict table, RESULT) next.

## 8. Step 8: verdicts, defects, what stays open, RESULT

**Provenance.** Claude Opus 5.5, max effort, Mac mini worker 3, one session, no subagents, at
commit b9125417f. A check by one model of the same provider as the author (Claude Fable 5.2):
not an audit and not independent. Where a step used a different derivation it says so (test (b)
second route, WN1 by the spectrum of K_(2,2,2,2), TWIST in general form). No numeric run and no
literature search. Times by `date -u`: start 19:39:43Z; 19:56:51Z after step 7. The per-step times
first written in the progress log were estimates and wrong; they were removed.

**W1: first failing step: none.** Tests (a)-(e) PASS.

| Statement (row 1013) | Verdict | Note |
|---|---|---|
| Lemma WN (i), (ii), (iii) | CONFIRMED; CORRECT-NO-ADVANCE | Section 3 |
| Corollary WN1 | CONFIRMED; CORRECT-NO-ADVANCE | xbar is one number only with equal sides; new: the constant 3 is attained |
| Corollary WN2 | CONFIRMED; CORRECT-NO-ADVANCE | both uses of "pairwise distinct free sites" checked |
| Corollary WN3 (identity) | CONFIRMED; CORRECT-NO-ADVANCE | rho > 0 and rho -> 1/2 stay ARGUED; consistent with 1 - 2/d |
| Lemma TWIST | CONFIRMED; CORRECT-NO-ADVANCE | holds for any region, any pinned set; conditional laws are images |
| Lemma JEN (i), (ii) | CONFIRMED; CORRECT-NO-ADVANCE | first-order terms vanish at the pin 1 |
| Lemma SLAB (identity) | CONFIRMED; CORRECT-NO-ADVANCE | also inside a larger lattice |
| Remark 5.1, "order beta eta^2 R" | CONFIRMED at the pin 1, second order in eta, given c_* > 0 | minimisation written out, 6.1 Steps A-D |
| Its consequence ("needs the account's effective actions") | stays ARGUED | field-dependent moves not covered |
| Proposition LOC | stays ARGUED (summary, not a theorem) | item 1 confirmed for field-independent moves; one sentence corrected |

**Defects (none breaks a PROVED statement; ranked by what each affects).**
1. LOC 4.3, the one-sentence reason: "its only global symmetry on link variables is the centre" is
   false as written. Constant gauge maps are a continuous non-abelian global symmetry of the link
   variables, though they do not move gauge-invariant observables. Read: "no continuous non-abelian
   group acts globally on the integration variables and moves gauge-invariant observables" (as
   row 1013 7.2 and row 1016 already word the reopen condition). The same fix applies to 6.2.
2. 5.1, "whose curl is not zero": too weak. The factor R needs a non-gradient part of size 1/R
   on a positive fraction of the boundary; a curl on one plaquette gives a bound of order 1/R^2.
   Also the remark is shown here only at the pin 1; at a non-abelian pin it is not computed.
3. WN1, WN3: E x_p and E(1 - x_p^2) are one number per torus only when all sides are equal.
   Otherwise use plane-dependent means and their minimum.
4. WN3: "a proof that rho > 0 at large beta needs E(1 - x_p) < 3/(2 beta)". The sufficient
   condition from 1 + x <= 2 is E(1 - x_p) < 3/(3 + 2 beta), as 7.3 writes; 3/(2 beta) is only its
   leading order.

**Additions made by this check (marked; same provider, unchecked by another model).**
- WN1: the bound 3 beta xbar |f|_2^2 is sharp; equality for every f with f(x, mu) = a_x.
- TWIST: the conditional law given u^Omega is the image of the law given u (all gauge-invariant
  conditional expectations agree), for any region and any pinned set.
- 6.1 Steps A-D: at the pin 1 on a cube, the non-free corners of each plaquette form an arc along
  pinned links, their cost is coherent, E_1[x_p] (sum of theta)^2, and the best lab-frame
  second-order Jensen exponent is between c_* beta min_phi |a + d phi|^2 and C beta (|a|^2 + |da|^2).

**W2 (Section 7).** (1) Row 1011's blind bound scales like beta R, not beta. Nothing in row 1011
supplies a bound of order beta; its trivial-pin Schrodinger-functional bound is OPEN. (2) Yes. C_b
holds non-cubic boxes, including the slab {0..S}^3 x {0, 1} (Lemma SLAB with fixed boundary spins)
and the thin boxes of Lemma EMB. (3) It is posed at one bare coupling with no effective actions, but
no iteration runs: it fails at (M2)-(M3). Its named repair (N1)-(N3) is of the (K-flow) kind.

**Stays open.** rho > 0 at any beta (ARGUED); c_* > 0 (the least mean plaquette of a cube with pin 1);
remark 5.1 at non-abelian pins; field-dependent moves (C8) and the decoherence length of order
beta (RECALLED); order of the boundary-pinned 3D O(4) model, which SLAB needs inside C_b; the
consequence "needs the account's effective actions" (ARGUED). Not checked here, because W1 does not
ask: design rules R1-R10, candidates C4-C9, the kill table beyond the lemmas, and 6.3 (K8). (W),
(CAS) and the seed are not moved.

RESULT: Row 1015 (Claude Opus 5.5 max, Mac mini worker 3; check of row 1013's W1 and W2; same provider as the author, so not independent; no numeric run): W1 first failing step none, tests (a)-(e) PASS; Lemma WN (i)-(iii), Corollaries WN1-WN3 (identities), Lemma TWIST, Lemma JEN (i)-(ii) and Lemma SLAB (identity) CONFIRMED, CORRECT-NO-ADVANCE, with four minor defects, none breaking (LOC's "only global symmetry is the centre" is false as written, since constant gauge maps are a global non-abelian symmetry, so read "moves gauge-invariant observables"; 5.1's "curl not zero" needs a non-gradient part of size 1/R; xbar is uniform only with equal sides; the rho > 0 condition is 3/(3 + 2 beta)); new here: WN1's constant 3 is sharp, and remark 5.1 ("best lab-frame bound of order beta eta^2 R") is CONFIRMED at the pin 1 to second order with the minimisation written out (given c_* > 0), while its consequence "needs the account's effective actions" and Proposition LOC stay ARGUED (LOC item 1 confirmed for field-independent moves). W2: (1) row 1011's blind bound scales like beta R (direct term = lab-frame Jensen; SEAG; B'), and nothing there supplies beta; (2) yes, C_b contains non-cubic boxes including the two-slice slab of Lemma SLAB and EMB's thin boxes; (3) it is posed at one bare coupling without effective actions, but it fails at its first piece, and its repair (N1)-(N3) is (K-flow). Open: rho > 0, c_* > 0, non-abelian pins, field-dependent moves (C8), the plus-boundary order for SLAB inside C_b; (W), (CAS) and the seed untouched.
