# Check of row 1119 (gap-resp-in-law-sheet): FINISH row 1120

Written by Claude Opus 5.5, reasoning effort max, as a laptop Claude subagent.
This is a same-provider check. The writer of row 1119 is Claude Fable 5.2
medium. The check is not independent of provider.

No mass gap is claimed here. A run may only guide or refute.

## Plan

1. Read `library/gap-resp-in-law-sheet.md` in full.
2. Read the lane sources it cites at the named lines: row 1018 L83-134,
   rows 1096 and 1099 and their checks (1097/1098, 1100 and any others).
3. Find the OpenAI O(4) LaTeX source used by row 1078 (scratch copy), or
   download the preprint openly into a new empty scratch directory. Read
   the equations the sheet uses: (3.14), (3.54), (3.55) and its proof,
   (3.61), and any others it names.
4. Check line by line, in order: K_c, R_c and (1.3); (2.0) and identity
   2.1; trivial bound (2.1) and the rough-profile energy bound; Lemma GB;
   Lemma IBP and (2.2)-(2.3); (2.4) from OpenAI (3.14), (3.54), (3.55);
   Lemmas LOW, SR; Lemma CH; Lemmas CH2, CH3, DEEP (use of (3.61));
   Lemmas TS, TS2; (4.1)-(4.2) and Lemma CO.
5. Judge the stop by the third rule, the distinctness of the three ways,
   and whether Lemma TS2 makes (H-two) in total variation circular for
   (CONV); give the weakest form of (H-two) that avoids this.
6. Write the verdict table and one RESULT line.

## Progress log

(Each step appends its result below.)

### Step 1 result: the sheet, read in full

- `library/gap-resp-in-law-sheet.md`: 309 lines, read in full. Its writer line
  says Claude Fable 5.2, reasoning effort medium.
- The row's FINISH entry (row 1119) and the rows it serves were read at their
  statements: row 1118 (CONV-two), row 1115 sections 3.4, 3.5, 6.2 and 6.3.
  Row 1115 3.4 defines (H-two) in words: "Draw two pins independently from
  the ring law. Ask that the interior laws of one cell under the two pins are
  close, in mean." The stop rule of rows 1118 and 1119 has three branches;
  the third is "one named step that failed in three written ways, each
  written out". Row 1119 adds: "The six routes of row 1096 and the three
  ports of row 1084 do not count among the three ways of the stop rule."
- Row 1018 L83-134 (`library/gap-short-step-max.md`) read: the 4D objects
  K_c, R_c, Rbar, Lemma CHAIN and the size argument (l^2 l^6 beta^2 l^(-8)).

### Step 2 result (part 1): the OpenAI source

- No new download. I read row 1078's earlier scratch copy of OpenAI's
  `preliminary.tex` (Section 3 of *Sharp mass bounds for the two-dimensional
  O(4) model*). Its SHA-256 begins `15daad11` and ends `a7a379b`, the value
  that check 1100 records for its own copy at commit `4eaee875`. It has 1284
  lines. Read by me: lines 1-260 (Theorem 3.1, Sections 3.1-3.3) and
  833-1060 (Sections 3.8-3.11.1).
- Equation numbers, checked by script: the source has 70 `equation`
  environments, 70 labels `eq:pre:*`, and no `align`, `\nonumber` or `\tag`.
  `main.tex` sets `\numberwithin{equation}{section}`, inputs `preliminary`
  third, and gives theorems their own counter. So the n-th display of Section
  3 is (3.n). The map of the sheet's 1.2 is right: (3.6) = `1-3`, (3.10) =
  `2-2`, (3.11) = `2-3`, (3.12) = `2-4`, (3.13)-(3.16) = `3-1`..`3-4`, (3.54) =
  `8-2`, (3.55)-(3.58) = `9-1`..`9-4`, (3.61) = `10-3`, (3.62) = `10-4`.
- The quotes of 1.2 match the source: the end of 3.10 ("Right twists and
  signed couplings are still allowed in this step; no association is being
  used yet") and the start of 3.11 ("This restriction is essential").
- Facts used below, read at the source. (3.12) is the transverse-current
  bound on a buffered patch; its proof rotates in a colour perpendicular to
  the extracted current, so it uses three colours. (3.14) bounds
  H_c(F,G) - F_c H_c G_c by P(B)[D_c(F)N_c(G) + N_c(F)D_c(G)], with constants
  "independent of pins". (3.16) is the exact Hessian identity
  D_u^2 S_g = L^(-2) sum_c H_c(a d_S u, a d_S u) for one fixed axis. (3.54)
  is H_{R_*} <= B^(-D) I "uniformly over the signed/twisted/pinned class".
  (3.55) is stated for profiles "supported on a fixed number of coarse
  cells"; its proof subdivides into side-R_* squares and uses only (3.54),
  (3.14) and "conditional variance subtraction".

### Step 2 result (part 2): the lane sources

- `library/gap-sheet-field.md` (row 1096): read in full (281 lines). Lemma CO
  is at L133-137: "a pinned square with couplings b_e in [-beta, beta]",
  pins omega^j, d > 2s(w+2), remainder 2^(4+w) |A| ||O|| exp(-(log 2) d/(2s)).
  Its statement names signed couplings and pins; it does not name twists.
  Row 1096 5.3, last bullet: Var(E[F | ring spins]) <= C poly(l) L_F^2
  e^(-c d/Xi) from Theorem 3.1.
- `library/gap-sheet-field-check-opus.md` (check 1097): step 7 and the
  verdict table read. Lemma CO: "HOLDS given (I1)-(I3)".
- `library/gap-sheet-field-check-astra.md` (check 1098): sections 6 and 7
  read. Lemma CO: "HOLDS AFTER specifying the common ring-coordinate space;
  its 'neutral quasi-local' interpretation is unsupported". The quote of the
  sheet's 1.5 is at its section 6 and is exact.
- `library/gap-pinu-ev-check-opus.md` (check 1100): the class of (3.61) read
  at its L81 and L124: "Q(S) = {0,...,S}^2 with all boundary spins fixed";
  d_pin is the distance to that boundary; a pinned inner layer is outside it.
- `library/gap-pinu-ev.md` (row 1099): L1-60 and Lemma W (L142) read. Lemma W
  is a zero-field wall-monotonicity step that fails on one site.
- `library/gap-checkerboard-singlet-astra.md` (row 1084): its three failed
  singlet ports are the three attempts of its Step 5 (two-circle amplitude
  association; conditional ferromagnetic signs; the auxiliary-spin port).
- `library/gap-sing-direction-fable.md` (row 1115): 3.4, 3.5, 6.2, 6.3 read.

## Step 3 result: the verdicts, line by line

Notation as in the sheet. "Sheet" means `library/gap-resp-in-law-sheet.md`.

### 3.1 Definitions: K_c, R_c, (1.3), (i), (ii)

**K_c and N_y (1.3): HOLDS.** For the bond e(y) with t_e + s_e =
q_y U_e q_x^(-1), the rotation q_y -> e^(ta) q_y gives d t_e/dt = -a.s_e
at t = 0. So D_{y,a}(b t_e) = -a.N_y, "up to sign" as the sheet says. Under
a common left rotation k of the ring, the interior law moves by q -> kq.
So N_y moves to Ad(k) N_y in law, K moves to Ad(k) K Ad(k)^T, and |K|_HS is
invariant. This holds with right twists and signed couplings.

**The normalisation R_c^2 = l^2 sum |K|_HS^2 (1.3): HOLDS (argued, as the
sheet marks it).** In two dimensions the free-field kernel between opposite
faces has size b l^(-2), there are about l^2 pairs, so sum |K|^2 is of order
b^2 l^(-2) and R_c^2 of order b^2. The guide run of Step 4 agrees: for the
lattice Gaussian sheet R_c^2 / b^2 tends to about 0.0746.

**(i) "the mean square of an entry must be o(l^-4)": HOLDS** as a statement
about the average over the (l-1)^2 pairs.

**(ii) as fixed in 1.3: HOLDS as a definition, with one remark.** The
single-cell tail clause P(d > eta^(1/2)) <= eta^(1/2) follows from the mean
by Markov's inequality, so it adds nothing. Row 1118 asks for "a stated tail
bound for the bad cells". A joint tail over several separated cells does not
follow from the mean bound. Row 1115 3.4 places the possible circularity
there. See Step 5.

### 3.2 (2.0) and the identity 2.1

**(2.0): HOLDS.** With S the log-density, F_c = -log Z_c, X = D_{f,a} A_c
and Y = D_{g,a'} A_c: D_g D_f F_c = E[D_g X] - Cov(X, Y). Here D_g X = 0,
because X depends on F_- and the interior and g moves F_+ only. The ring-ring
bond terms are constants of the interior integral and no bond joins the two
faces. So D_f D_g F_c = -K_c[fa, ga'].

**Identity 2.1: HOLDS.** E over the signs gives
sum_{y,y'} (a.K(y,y')a')^2; the mean over a, a' in an orthonormal basis gives
(1/9) sum |K(y,y')|_HS^2. The sheet writes E_theta; the mean is over theta,
theta', a and a'.

### 3.3 The trivial bound (2.1) and the energy of rough extensions

**(2.1): HOLDS.** |Cov(U,V)|_HS^2 <= E|U-EU|^2 E|V-EV|^2 entrywise by
Cauchy-Schwarz. |N_y| <= b because |s_e| <= 1 and |b_e| <= b. A face has at
most l non-corner sites. So sum |K|^2 <= b^4 l^2 and R_c^2 <= b^4 l^4.

**The energy lower bound for rough profiles: HOLDS AFTER CORRECTION.** As
written ("every extension of a profile of independent signs has energy at
least c l") it holds only for typical sign profiles: the constant profile
has extensions of energy zero. Corrected text, now proved:

> For consecutive non-corner sites y, y+1 of F_- and any extension F of
> theta, the path y, x(y), x(y+1), y+1 gives
> (theta_{y+1} - theta_y)^2 <= 3[(theta_y - F_{x(y)})^2 +
> (F_{x(y)} - F_{x(y+1)})^2 + (F_{x(y+1)} - theta_{y+1})^2]. Each bond of
> the right side occurs in at most two such paths. So every extension has
> E(F) >= (1/6) sum_y (theta_{y+1} - theta_y)^2. For fair independent signs
> the products theta_y theta_{y+1} are independent fair signs, so the sum has
> mean 2(l-2) and the right side has mean (l-2)/3; it is at least (l-2)/4
> with probability at least 1 - e^(-c l) (Hoeffding).

The rest of way 1 (a variance of order b l per face; a mean square response
of order b^2 l^2; a miss by l^4) HOLDS at the "argued" grade the sheet uses.

### 3.4 Lemma GB

**The computation: HOLDS.** For the Gaussian sheet F_c(Omega) =
(b/2) Omega.Lambda Omega + const. The gradient of the minimal energy in
Omega_y is 2(Omega_y - h(x(y))), with h the harmonic extension. So
Lambda(y,y') = -H(x(y), y') for y' not y, with H the exit law of the simple
random walk. Direct check: N_y = b(Omega_y - phi_{x(y)}) up to sign, and
Cov(phi_x, phi_x') = G_D(x,x')/b with G_D = (4 - A)^(-1) the Dirichlet Green
function. So K(y,y') = b G_D(x(y), x(y')) = b H(x(y), y') = -b Lambda(y,y')
>= 0, for every pin. Symmetry of Lambda gives the sheet's form
P_{x(y')}(exit through y).

**The random-walk estimate: HOLDS (standard; argued, as marked).** In
continuous time the two coordinates of the walk are independent. From
distance 1 of F_+, the normal coordinate reaches depth l/4 before 0 with
probability 4/l; given this, it does so by time C l^2 with probability at
least 1/2 for C large (Markov's inequality on the conditioned hitting time).
The tangential coordinate stays within l/4 up to time C l^2 with probability
c(C) > 0. From depth l/4 near the centre line, the exit law of F_- is bounded
below by the invariance principle. So P >= c_0/l for y' in the middle half.
The guide run of Step 4 gives min over the middle half of l P = 0.2454 at
l = 256, so c_0 can be taken near 0.24.

**"Every tool of way 1 holds for the Gaussian sheet": HOLDS AFTER
CORRECTION.** Item by item, read at the source:
- (3.6): holds in its abelian form, t_e = 1, s_e.a replaced by
  phi_y - phi_x. The bound |w_e t_e| <= b, which (3.11) uses, holds.
- (3.11): holds with equality at every pin. The mean of D_f A is
  b <dh, df> = 0 because h is harmonic and f vanishes on the pins; the
  variance is b E(f).
- (3.12): the source states it "independent of pins". For the Gaussian sheet
  it fails at unbounded pins: pins K x_1 give a current mean of size b K d on
  a patch of side d. It holds, with a constant that depends on the range,
  for pins in a bounded interval (the harmonic extension then has gradient
  O(range/d) on the patch) and in the Gaussian ring law. The posted proof of
  (3.12) uses a colour perpendicular to the extracted current; the scalar
  field has no such colour, so only the statement transfers, not the proof.
- The pointwise bound |N_y| <= b, used by (2.1), fails for the Gaussian
  sheet. The conclusion of (2.1) still holds there:
  sum |K|^2 = b^2 sum H^2 <= b^2 sum H <= b^2 l, since H(x, .) is a
  probability.
- The Markov property, the Cauchy-Schwarz inequality and the discrete trace
  bound of 3.3 hold. Lemma IBP has its Lebesgue form for a normalisable
  Gaussian ring law (one far site fixed, or a small mass).

Corrected text for the sentence "All of them hold for the Gaussian sheet ...
where (i) is false":

> Take the Gaussian sheet with pins in a bounded interval (or drawn from its
> own ring law). It satisfies (3.6) in abelian form, (3.11) with equality,
> (3.12) in moment form, the Markov property and the Cauchy-Schwarz
> inequality, and R_c^2 >= b^2 c_0^2/4 at every l and every pin. So no
> argument that uses only these statements, and no pointwise bound on a
> single current, proves (i). An argument that uses |N_y| <= b pointwise,
> the bracket term of (3.7), the three colours of (3.12), or the Haar
> measure is not excluded by this model. The compact U(1) sheet would test
> the first of these; it is recalled only (Frohlich and Spencer).

With this scope the exclusion is proved. Lemma GB is the sheet's only
proved exclusion, as its 6.3 says.

### 3.5 Lemma IBP, (2.2), (2.3)

**HOLDS.** The flow q_y -> e^(t eta_y) q_y is left multiplication at each
site, so it preserves product Haar measure at every t. Differentiate
integral u(phi_t q) e^(-F_tot(phi_t q)) dq = const at t = 0. Since
e^(s eta_y) e^(t eta_y) = e^((s+t) eta_y), D_eta^2 is the second t-derivative.
u = D_eta F_tot gives (2.2); u = G D_g G gives (2.3). (2.2) is the identity
part of the paper's (3.56). Nothing uses the sign or twist of a bond.

### 3.6 (2.4): uniform in l, after a correction of its hypotheses

The row asks whether (2.4) follows from (3.14), (3.54) and the proof of
(3.55) at the scale l, uniformly in l, or only at cells comparable to s.

**Verdict: HOLDS AFTER CORRECTION, uniformly in l >= s.** The proof of (3.55)
is local: it bounds the Hessian by a sum over side-R_* squares, and each
square's cost needs only (3.54) and (3.14) for that square. The restriction
"supported on a fixed number of coarse cells" in the statement of (3.55) is
not used by that bound. So the bound runs at every scale l >= s with the
same B^(-D). The sheet's route through coarse cells of side s gives the same
count: (l/s)^2 coarse cells, each costing C (s/l)^2 [B^(-D) + P(B)/M_*].

Two hypotheses must be corrected. (a) "f, g restrictions to the middle
halves ... of functions phi(./l)" allows a jump at the ends of the middle
half, where f stops. The proof of (3.55) needs profiles that are
"continuous across cells" with "uniformly bounded cellwise C^2 extensions",
and an extension that vanishes on every other l-ring site; a jump has
neither. With a jump the two tangent bonds at the jump alone add 2 b t_e to
D_f^2 F_tot, of order b at aligned rings; I did not bound the cell terms
from below, so I claim no counterexample, only that the proof does not
apply. (b) The (3.14) remainder D_c(F) = L^(-1) N_c(grad F) involves one
more derivative of the test field, so phi should be C^3 (or the direct
Lipschitz bound that the source allows after (3.14) should be invoked).

Corrected statement and proof (bookkeeping written here; mark: proved given
OpenAI's (3.14), (3.16), (3.54), unrefereed; checked by me, same provider):

> Let l >= s be a multiple of s = R_* M_*, and let the torus sides be at
> least 3l. Put coordinates with F_- = {x_1 = 0} and F_+ = {x_1 = l}. Let
> phi_1, phi_2 be C^3 functions with C^3 norm at most 1 and support in
> (1/4, 3/4), and put f(0, j) = phi_1(j/l), g(l, j) = phi_2(j/l). Then at
> every ring configuration, D_eta^2 F_tot, D_{f,a}^2 F_tot and
> D_{g,a'}^2 F_tot are at most C_1 B^(-D), with C_1 depending only on the
> paper's fixed choices.
>
> Proof. (1) Extend: Phi_1(z) = phi_1(z_2) chi(z_1) and
> Phi_2(z) = phi_2(z_2) chi(z_1 - 1) in macroscopic coordinates z = x/l,
> with chi in C^3, chi(0) = 1, support in (-1/4, 1/4). Phi_i equals f (or g)
> on its face and vanishes on every other l-ring site. The two supports are
> at lattice distance at least l/2 > 2 R_* + 2.
> (2) For each of the three l-cells that meet a support, tile it by
> (l/R_*)^2 squares Q of side R_*. The half allocation of tangent edges
> (source, Section 3.1) gives F_cell(Omega) = -log integral
> exp(-sum_Q F_Q) d omega_in over the inner rings. Change variables
> omega_in -> e^(t eta~) omega_in with eta~ = Phi_1 a + Phi_2 a' (Haar
> preserving). With G_t = sum_Q F_Q(e^(t eta~) omega), the second derivative
> is E[G''] - Var(G') <= sup over omega_in of sum_Q D_{eta~}^2 F_Q.
> (3) Each Q meets at most one support, so the flow is one-axis on Q. For
> one cell the identity behind (3.16) reads D_u^2 F_Q = L^(-2) H_Q(a d_S u,
> a d_S u) with S = l, L = l/R_* (differentiate -log Z_Q along the rotation
> of its ring and interior; (3.6)). By (3.14) and (3.54), at every pin of Q:
> H_Q(F,F) <= B^(-D) |F_Q|^2 + 2 P(B) D_Q(F) N_Q(F), with N_Q <= C and
> D_Q <= C/L for F = a d_S u, since the C^3 norm of Phi_i is at most C.
> (4) Sum over the at most 2 L^2 squares in the supports:
> sum_Q L^(-2)[B^(-D) |grad u(z_Q)|^2 + C P(B)/L]
> <= B^(-D) (integral |grad u|^2 + o(1)) + 2 C P(B)/L. Since
> L >= M_* = ceil(B^(D + C_0)), the choice of C_0 in the proof of (3.55)
> makes P(B)/L <= B^(-D). Summing over the three cells gives C_1 B^(-D). QED

So (2.4) is not limited to cells of side comparable to s. It is limited to
smooth profiles at the scale l (or at any scale lambda between s and l, by
the same count), and its gain stays B^(-D) at every scale: the paper stops
its iteration at B^(-D) under the premise (3.9), as the sheet says.

### 3.7 Lemma LOW

**HOLDS given (2.4) as corrected in 3.6, with two notes.** D_eta = D_f + D_g
as vector fields and the two commute (disjoint sites), so
D_f D_g = (D_eta^2 - D_f^2 - D_g^2)/2. Only the cell c contains both
supports, provided the torus sides are at least 3l (on a torus of side 2l
the cells c_- and c_+ coincide and contain both faces too). For each h,
E|X| = 2 E[X_+] - E[X] <= 2 C_1 eps by (2.4) and (2.2). Adding gives
3 C_1 eps.

Note on the reading. Lemma LOW bounds E_mu |K_c[fa, ga']|, a first moment.
The term of E_mu R_c^2 is the mean of the square. Its bound needs, in
addition, a pointwise bound on |K_c[fa, ga']|; none is written. Corrected
sentence: "every fixed low-low response has mean modulus at most 3 C_1 eps".

### 3.8 Lemma SR

**The lemma: HOLDS given (2.4).** Checked: D_g G = -kappa (only c contains
y' and the support of f); |D_g F_tot| <= 4b (two cell bonds and two
tangent bonds of total weight b each); the third derivative is
kappa_3(X,Y,Y) - Cov(X, D_g Y), from d/dt Cov(X,Y) = Cov(X, d_t Y) -
kappa_3(X,Y,Y); kappa_3(X,Y,Y) = E[X~ Y~^2] is a third central moment, so
|D_g^2 G| <= (4 b^2 + b) E|X~|. (2.3) and Cauchy-Schwarz give
x^2 <= (C_1 eps)^(1/2) (4 b x + (b + 4 b^2) sigma_f), and x <= A + C^(1/2)
for x^2 <= A x + C gives (2.6).

**The reading: HOLDS AFTER CORRECTION.** The reason given, "l >= s >
eps^(-1/4)", is not the comparison that matters. Corrected text: "The first
term of (2.6) is 4 b (C_1 eps)^(1/2). Since s >= M_* >= B^D = 1/eps, the
Gaussian size b/l is at most b eps, which is below 4 b (C_1 eps)^(1/2) when
eps <= 16 C_1. So the right side of (2.6) is never below the Gaussian size."

### 3.9 Where way 2 stops

**HOLDS AFTER CORRECTION.** The failing line itself holds: (2.2) and (2.4)
hold with the same eps for bumps of every width between s and l (3.6, step
4, with l replaced by lambda) and contain no distance. The sentence "(i)
needs the bound eps to be replaced by o(lambda lambda'/l^2)" overstates what
(i) needs. Corrected text: "(i) implies, by Cauchy-Schwarz,
E_mu |K_c[f_lambda a, g_lambda' a']| <= (E_mu R_c^2)^(1/2) (lambda
lambda')^(1/2) / l, that is o((lambda lambda')^(1/2)/l). A bound uniform in
the distance meets this for no lambda, lambda' <= l. A proof bump by bump
would need o(lambda lambda'/l^2), the Gaussian size." The symbol M in
"l^2 - M^2 other blocks" is not defined; read "all blocks except a fixed
number of low modes".

### 3.10 Lemma CH

**HOLDS** (for l >= 4, so that x(y) and x(y') are off the chord Gamma).
Removing Gamma disconnects the two halves of the interior; with
nearest-neighbour bonds they are independent given Omega and sigma_Gamma.
N_y depends on q_y and q_{x(y)}, N_y' on q_y' and q_{x(y')}. So
E[N_y (x) N_y' | sigma_Gamma, Omega] = alpha_y (x) alpha'_y', and (3.1)
follows by the tower property.

### 3.11 Lemma CH2, and the class of (3.61)

**HOLDS given (3.61), used inside its stated class.** B is a translate of
Q(2r), r = floor(l/2) - 1. Conditioning mu on all spins outside the interior
of B fixes every spin of the boundary of B. The interior of B holds no pin:
mu is unpinned, and on a free subgraph B lies in G because c is at distance
at least l from its boundary. The tangent edges of the boundary of B are
constants. So the conditional law is a square "with all boundary spins
fixed", the class of check 1100. The components of N_y have zero
common-left average because the Haar mean of Ad(k) is the zero matrix (the
adjoint representation is irreducible and not trivial). d_pin =
dist({y, x(y)}, boundary of B) = r - 1 = floor(l/2) - 2. N_y' is measurable
outside the interior of B (x(y') is at distance l - 1 > r). Apply (3.61) to
each component (a factor 3 at most in the HS norm), multiply by N_y' and
average. The exponent is c (floor(l/2) - 2)/s; the sheet's (l/2 - 2) differs
by a constant only.

### 3.12 Corollary CH3

**HOLDS given (3.61).** On an unpinned torus or free subgraph mu is invariant
under a common left rotation (also with right twists and signed couplings),
so E_mu N_y = Ad(k) E_mu N_y for all k, hence 0. Then (3.3) is
E_mu[N (x) N'] - E_mu[Nbar (x) Nbar'] with the first term bounded by (3.2).

### 3.13 Lemma DEEP

**HOLDS given (3.61), inside its class.** B is a closed square inside c, so
its interior lies in the interior of c and holds no pin. Its boundary may
contain ring sites; they are fixed by Omega and the class allows this.
Conditioning (c, Omega) on the spins outside the interior of B gives a
square with all boundary spins fixed. The bound on Cov follows from
|E[OG]| + |E O| |E G|.

### 3.14 The failing lines of way 3

**Failing line 1: HOLDS AFTER CORRECTION.** The two-copy formula is right:
|E[alpha (x) alpha' | Omega]|_HS^2 = E[(alpha(sigma^1).alpha(sigma^2))
(alpha'(sigma^1).alpha'(sigma^2))] with two copies given Omega. The
sentence "its ring weight is Z_c(Omega)^2 Z_ext(Omega)/Z_c(Omega)" does not
say what is meant: that expression equals Z_c Z_ext, the ring weight of mu
itself. Corrected text: "The joint weight of (sigma^1, sigma^2, Omega) is
proportional to exp(S_c(sigma^1, Omega) + S_c(sigma^2, Omega)) Z_ext(Omega)
/ Z_c(Omega). The factor 1/Z_c(Omega) is a non-local function of the ring,
so the two-copy law is not a nearest-neighbour Gibbs law of the class." The
size claims (|Nbar_y| of order b^(1/2)) stay argued.

**Failing line 2: HOLDS** as an argued reading: a set that separates F_-
from F_+ in the cell must join the top and bottom sides, and (3.61) gives
nothing at distance of order 1 from pins.

### 3.15 Lemmas TS and TS2

**Lemma TS: HOLDS.** Convexity of the total variation distance in one
argument gives the lower bound, the triangle inequality the upper bound.
Since the joint law of (core, ring) and the product of its marginals have
the same ring marginal, their distance is E_mu d(m_Omega, mbar). By the
Markov property this is also the distance for (core, outside).

**Lemma TS2: HOLDS, with constant 2 in place of 4.** Cov_mu(F, G) =
E_mu[(m_Omega(F) - mbar(F)) G] and |m_Omega(F) - mbar(F)| <=
2 ||F|| d(m_Omega, mbar). So |Cov| <= 2 ||F|| ||G|| beta_mix. The stated 4
is weaker and also true.

**The two consequences after TS2.** The first ("a proof of (ii) in the class
... is a proof of neutral mixing in that class"; the paper "declines that
claim") HOLDS as a reading; the quote is exact. The second HOLDS AFTER
CORRECTION. "(ii) ... already contains the conclusion of (CONV) at one
scale. Row 1118 could only improve the rate" overstates it. TS2 gives a
covariance bound 2 eta at one separation (l/3), with no decay. (CONV) asks
for decay at every separation, at rate c/l, for every limit state of a
class. Conversely, decay at rate c/l gives C e^(-c/3) at separation l/3,
which need not be below eta. Corrected text: "(ii) is a one-scale mixing
statement: the core and the outside of one cell are eta-close to
independent, for all bounded observables. (CONV) from (ii) would be a
bootstrap from one-scale mixing to exponential decay at all separations; it
would not turn a response bound into mixing."

### 3.16 (4.1), (4.2) and the use of Lemma CO

**(4.1): HOLDS given Lemma CO at zero field.** Lemma CO is stated for "a
pinned square" with two pin sets; the cell c with pins Omega^1, Omega^2 is
such a square, and H^1 = H^2 = 0. Check 1097 found CO to hold; check 1098
found it to hold "AFTER specifying the common ring-coordinate space" (the
free ring coordinates omega~_Rf, with the two pin sets inserted
separately). The sheet cites both checks as "holds"; it should cite check
1098's specification. Psi = nu^1_{omega~}(O*) depends on Omega^1 and
|Psi| <= ||O||. Lemma CO names signed couplings and pins, not twists; the
sheet uses (4.1) only for the untwisted sheet, so this costs nothing here,
but (4.1) is not a step verified in the class of fixed twists.

**(4.2): HOLDS given (4.1).** |integral Psi d(m~ - m~')| <= 2 ||Psi||
d(m~, m~') on the free ring coordinates. Since |Psi| <= ||O|| and the bound
on Rem are uniform in O, the supremum over O can go inside the mean. So
E d(m_Omega, m_Omega') <= 2 E d(m~_Omega, m~_Omega') + C l^2 e^(-c l/(3s)),
which is the sheet's "(ii) follows from the same two-sample statement for
the gauge-fixed rings".

**Way 4's failing line: HOLDS** at the argued grade, with one correction.
"Functions of omega-tilde are neutral" needs scope. At zero field
Phi(kg) = k Phi(g) on coarse edges with free ends, so omega~ is invariant
under the joint rotation (omega, g) -> (k omega, k g) away from the pins.
But omega~ is a function of (omega, g), not of the spins, and (3.61) is a
statement about functions of the spins. Check 1098 found the "neutral
quasi-local" reading of Psi unsupported (in a field). Corrected text:
"Functions of omega~ are invariant under the joint common rotation of rings
and orientations away from the pins; (3.61), a statement about functions of
the spins, does not apply to them as written."

### 3.17 The next decision (N-CH)

**HOLDS AFTER CORRECTION.** By Lemma CH, Cov_{c,Omega}(alpha_y, alpha'_y') =
K_c(Omega)(y, y') exactly. So (N-CH) ("the covariance under (c, Omega) of the
two half fluxes ... has mean square o(l^-4)") is the entrywise form of (i),
word for word after (3.1). It is not a smaller statement. Corrected text:
"By Lemma CH, (i) in its entrywise form is the statement (N-CH) about the
two half fluxes of a chord. The row isolates no statement smaller than (i);
it isolates the chord as the carrier of the correlation."

### 3.18 Step 5 of the sheet (the tests)

**HOLDS AFTER CORRECTION** in one sentence: "(2.0), 2.1, (2.1), Lemma IBP,
Lemma CH, Lemma TS and Lemma TS2 hold for every group and every coupling"
should read "for every compact group with bounded bond terms; for the
Gaussian sheet their Lebesgue analogues hold, and (2.1) holds there in the
form sum |K|^2 <= b^2 l (3.4 above)". With that, "these blind statements
cannot be combined into (i)" follows from Lemma GB as corrected. The other
test sentences hold. The sheet uses no monotonicity, association or
positivity of a correlation (the positivity of a Gaussian kernel in Lemma
GB and of a second moment in Lemma LOW are not of that kind), so Lemmas W,
P1, A1, G1 and G2 are not contradicted.

## Step 4 result: one guide run for Lemma GB (guide only; it proves nothing)

One serial pure-Python job (no numerical library; one thread), in the
session scratch area; a copy is in `runs/gap-resp-in-law-sheet-check-opus/`. It computes, for the lattice
square {0,...,l}^2, the Gaussian kernel K(y,y')/b = G_D(x(y), x(y')) between
the two faces in two independent ways: the sine eigenbasis of the Dirichlet
Laplacian, and Gauss-Jordan inversion of the full interior matrix (small l
only). The two agree to 1.4e-17 at l = 6 and l = 8.

| l | sum of K/b | R_c^2 / b^2 | min over middle half of l P(exit through F_-) |
|---|---|---|---|
| 8 | 0.22662 | 0.08323 | 0.2558 |
| 16 | 0.22218 | 0.07665 | 0.2480 |
| 32 | 0.22102 | 0.07507 | 0.2460 |
| 64 | 0.22073 | 0.07468 | 0.2455 |
| 128 | 0.22066 | 0.07459 | 0.2454 |
| 256 | 0.22064 | 0.07456 | 0.2454 |

Every entry is positive. The run agrees with Lemma GB: R_c^2 is bounded
below (near 0.0746 b^2, above the proved b^2 c_0^2/4), and the random-walk
estimate holds with c_0 near 0.245.

## Step 5 result: the stop rule, the three ways, and (H-two)

### 5.1 The stop by the third rule

The rule (row 1119): "one named step that failed in three written ways, each
written out"; "the six routes of row 1096 and the three ports of row 1084 do
not count".

**The named step needs a correction.** As written, (C-E) derives the bound
"from the two outputs of the posted engine, (E-smooth) and (E-charged), with
the Markov property and Haar integration by parts". Way 1 uses neither
output. It uses the inputs (3.6), (3.11) and (3.12). So, as written, way 1
is not an attempt at (C-E). Corrected text:

> (C-E): from the posted engine, that is its inputs (3.6), (3.11), (3.12)
> and its outputs (E-smooth) (here (2.4), the scale-l form of (3.54)-(3.56))
> and (E-charged) ((3.61)-(3.62)), with the Markov property and Haar
> integration by parts, derive in the ring law E_mu |K_c(Omega)(y,y')|_HS^2
> = o(l^-4) for y, y' on opposite faces.

**The three ways are distinct.**

| Way | Tools | Pins | Failing line |
|---|---|---|---|
| 1 | (3.11), (3.12), (2.1), Cauchy-Schwarz | every pin | rough extensions have energy of order l; proved barrier for group-blind tools (Lemma GB as corrected) |
| 2 | Lemma IBP, (2.4) | ring law | (2.2), (2.4) hold with one eps at every width and contain no distance; third derivatives are not small |
| 3 | Markov chord, (3.61) | both | the second moment is a two-copy neutral function; (3.61) is silent at the ends of every separating chord |

They use different inputs and stop at different lines. None is among the
excluded routes: the seven bullets of row 1096 5.3 treat PIN-U and EV, which
are uniform in the pins; the three ports of row 1084 (its Step 5, Attempts
1-3) are singlet ports of Section 3.11. None of these is in the ring law and
none treats K_c. Each way is written out in the sheet.

**Verdict: the stop is valid, after the correction of (C-E).** Two limits.
The failing lines of ways 2 and 3 are argued, not impossibility proofs; the
rule asks only for written failing lines. The stop concerns (i). For (ii)
the sheet has one way (way 4) and Lemma TS2. The rule needs one named step
for the row, so this suffices, but (ii) is not stopped by three ways of its
own.

### 5.2 Does Lemma TS2 make (H-two) in total variation circular for (CONV)?

First a converse of TS2, which settles the weakest forms.

**Lemma TS3 (proved here).** Let F be a bounded function of the core spins
and alpha_F = E_mu |m_Omega(F) - mbar(F)|. Then
(a) sup { |Cov_mu(F, G)| : G a function of the spins outside the interior
of c, ||G|| <= 1 } = alpha_F;
(b) alpha_F <= E |m_Omega(F) - m_Omega'(F)| <= 2 alpha_F, for Omega, Omega'
independent with the ring law.

Proof. Cov_mu(F, G) = E_mu[(m_Omega(F) - mbar(F)) G] <= alpha_F, with
equality for G = sign(m_Omega(F) - mbar(F)), a function of the ring. For
(b), mbar(F) = E' m_Omega'(F), so Jensen's inequality gives the lower bound
and the triangle inequality the upper bound. QED

**Answer: not circular as an implication; but (H-two) is a mixing
hypothesis, not a response hypothesis.**
- Not circular. TS2 gives |Cov| <= 2 eta at one separation (core against
  outside, distance l/3), with no decay. (CONV-two) asks for exponential
  decay at every separation, at rate c/l, for every limit state of a class.
  So the conclusion is not contained in the hypothesis. Nor is the converse:
  decay at rate c/l gives only C e^(-c/3) at separation l/3. (CONV-two) from
  (H-two) is a bootstrap from one scale to all scales, and the obstacles of
  row 1115 3.4 (bad cells, mixtures) remain its content.
- Conclusion-shaped. By TS and TS3, E d(m_Omega, m_Omega') is within a factor
  2 of the beta-mixing coefficient of core and outside. A supplier of (ii)
  must prove one-scale singlet mixing in the law of the model. The sheet's
  conclusion "(ii) is not a weaker supplier" holds, with the wording of 3.15.

### 5.3 The weakest form of (H-two) that avoids this

By TS3, any two-sample form "E Phi(m_Omega, m_Omega') <= eta" that tests a
class Cl of core observables with a small constant is, within a factor 2,
the one-scale covariance coefficient of Cl against the whole outside. So the
one-scale mixing content cannot be removed by weakening the distance (total
variation, a transport distance, one observable at a time). It can be
removed only by shrinking Cl to exclude neutral observables, or by giving up
the small constant. Each such form fails a test that (CONV) must pass:
- Charged observables only. For the O(4) sheet this form holds for every
  pair of pins by (3.61): |m_Omega(F)| <= C |core| ||F|| e^(-c l/(3s)). So it
  is no hypothesis there. It cannot exclude a neutral first-order point
  with unbroken symmetry (model B of row 1115; argued there, belief grade
  here).
- Local neutral observables only. For the compact U(1) sheet at large
  coupling the conditional mean of a local neutral observable at depth l/3
  depends on the ring through gradients of order 1/l (spin-wave picture;
  argued). So the form holds with eta(l) tending to 0, while neutral
  correlations decay only as a power. It fails the U(1) test.
- No small constant (an overlap form, P(d <= 1 - delta) >= 1 - eta). TS2
  then gives only 2(1 - delta + eta). For the neutral data of the Gaussian
  sheet (differences of field values) the law of d does not depend on b
  (proved: the field rescales by b^(1/2), and the distance is invariant
  under a common bijection), and it tends to an l-independent law inside
  (0, 1) (argued). So the neutral overlap form holds at every scale. It
  fails the massless test in its Gaussian form; for the compact U(1) sheet
  the same is expected from the spin-wave picture (belief grade).

**So no two-sample form avoids one-scale mixing of its tested class and
still passes the tests.** The weakest form that passes them is

> (H-two-N1)(l, eta): for every bounded neutral function F of the core spins
> (non-local functions allowed), E |m_Omega(F) - m_Omega'(F)| <= eta ||F||.

It is weaker than (H-two) in total variation (the supremum over F stands
outside the mean). With the charged bound of (3.61) it gives the
one-observable form for all bounded F: split F into its common-left average
and a charged rest. By TS3 it is equivalent, within a factor 2, to a
covariance bound: (H-two-N1)(eta) gives |Cov_mu(F, G)| <= eta ||F|| ||G|| for
neutral core F and all outside G, and that bound gives (H-two-N1)(2 eta). It
is not circular for (CONV), for the reason of 5.2, and it is still a
one-scale singlet mixing statement. It passes the two tests (argued): for
compact U(1) the indicator of a large relative twist between two blocks of
the core has a conditional mean that moves by order one with the ring; at
coexistence the core order parameter does. Whether (CONV) can be proved from
(H-two-N1), rather than from total variation, is open; couplings use total
variation.

**The bad-cell tail.** The circularity that row 1115 3.4 names sits in the
tail, not in the mean. The tail clause of the sheet's 1.3 follows from the
mean and adds nothing. A joint tail over k separated cells does not follow
from (H-two) and is itself a decorrelation statement about ring events in
the law of the model. The non-circular pattern is the paper's own:
"All estimates are uniform under conditioning outside the collar" (after
(3.58)), and then "Iterated conditioning gives" the joint bound (3.60). The
two-sample form in that pattern is

> (H-two-col)(l, eta): for every cell c and every configuration tau outside
> the concentric box Q_c of side 3l, if Omega, Omega' are drawn
> independently from the ring law of c under mu( . | tau), then
> E[d(m_Omega, m_Omega') | tau] <= eta.

It refers to the specification only, not to the state. TS2 inside Q_c gives
one-scale mixing given tau, uniformly in tau: a one-scale weak-mixing
condition in a finite box, with a supremum over the far boundary only. It is
weaker than (H-sup) and not comparable with (H-two). Its bad-cell events
are still not local, so iterated conditioning needs a local bad event in
addition; I did not write one. Whether Proposition B', Theorem D2 or Lemma
SHEET reach (H-two-col) in four dimensions is not checked here. Marks: TS3
proved; the three test failures and the claims on (H-two-N1) and
(H-two-col) argued.

## Step 6 result: verdict table, limits, who checked what

### 6.1 Verdict table (sheet line numbers)

| Item (sheet lines) | Verdict | Note |
|---|---|---|
| K_c, N_y (L43-44) | HOLDS | Ad-covariance; twists allowed |
| R_c, normalisation (1.3) (L45-49) | HOLDS (argued) | guide: R_c^2/b^2 near 0.0746 for the Gaussian sheet |
| (i), (ii) as fixed (L50-51) | HOLDS | the single-cell tail clause adds nothing to the mean |
| (2.0) (L73-75) | HOLDS | |
| Identity 2.1 (L79) | HOLDS | the mean is over theta, theta', a, a' |
| Trivial bound (2.1) (L83-87) | HOLDS | |
| Energy of rough extensions (L87) | HOLDS AFTER CORRECTION | in mean or with high probability; proved with constant 1/6 (3.3) |
| Lemma GB: computation, random walk (L89-91) | HOLDS | guide: c_0 near 0.245 |
| Lemma GB: "every tool holds for the Gaussian sheet" (L89, L93) | HOLDS AFTER CORRECTION | (3.12) fails at unbounded pins; no pointwise bound on N_y; text in 3.4 |
| Lemma IBP, (2.2), (2.3) (L99-104) | HOLDS | |
| (2.4) (L106-110) | HOLDS AFTER CORRECTION | uniform in l at least s; C^3 bumps vanishing near the ends; proof in 3.6, given (3.14), (3.16), (3.54) |
| Lemma LOW (L112-118) | HOLDS given (2.4) | torus sides at least 3l; it bounds a first moment (3.7) |
| Lemma SR (L120-126) | HOLDS given (2.4); its reading HOLDS AFTER CORRECTION | the comparison uses s at least B^D (3.8) |
| Where way 2 stops (L128) | HOLDS AFTER CORRECTION | what (i) implies, by Cauchy-Schwarz (3.9) |
| Lemma CH (L140-144) | HOLDS | l at least 4 |
| Lemma CH2 (L146-150) | HOLDS given (3.61) | used inside its class (3.11) |
| Corollary CH3 (L152-156) | HOLDS given (3.61) | |
| Lemma DEEP (L158-160) | HOLDS given (3.61) | used inside its class (3.13) |
| Failing line 1 of way 3 (L166-170) | HOLDS AFTER CORRECTION | the two-copy weight sentence (3.14) |
| Failing line 2 of way 3 (L172) | HOLDS (argued) | |
| Lemma TS (L184-190) | HOLDS | |
| Lemma TS2 (L192-194) | HOLDS | constant 2 suffices |
| Consequences of TS2 (L196-199) | first HOLDS; second HOLDS AFTER CORRECTION | one-scale mixing, not the conclusion of (CONV) (3.15) |
| (4.1) (L205-209) | HOLDS given Lemma CO | cite check 1098's specification; twists not covered by CO's statement |
| (4.2) (L211-215) | HOLDS given (4.1) | |
| Way 4's failing line (L217-222) | HOLDS AFTER CORRECTION | scope of "functions of omega-tilde are neutral" (3.16) |
| (N-CH) (L275) | HOLDS AFTER CORRECTION | by Lemma CH it is (i) itself (3.17) |
| Step 5 tests (L230-253) | HOLDS AFTER CORRECTION | "every compact group with bounded bond terms" (3.18) |
| Stop by the third rule (L261-269) | valid AFTER CORRECTION | the named step must list the inputs (3.6), (3.11), (3.12) (5.1) |
| The three ways distinct | yes | different inputs and failing lines; none excluded (5.1) |
| TS2 and circularity for (CONV) | not circular as an implication | (H-two) is one-scale beta-mixing; weakest test-passing form (H-two-N1); collar-conditional tail (5.2, 5.3) |

No item FAILS. No counterexample to a proved statement of the sheet was
found.

### 6.2 Limits

- Same provider as the writer. Not formalized in Lean. Every check is by
  hand; the one run is a guide.
- OpenAI's paper is unrefereed. (3.14), (3.16), (3.54) and (3.61) are taken
  as stated. I read Sections 3.1-3.3 and 3.8-3.11.1 of the source; Sections
  3.4-3.7 (the stiffness gain itself) were not read, as in the sheet.
- I used row 1078's copy of the source; its SHA-256 matches check 1100's
  record for its own copy at the pin. I did not fetch the pin again.
- Pei's paper and Ding, Huang and Yang's paper were not opened. Lemma CO
  enters through row 1096 and checks 1097 and 1098 only.
- Of the check files I read check 1097 step 7 and its table, check 1098
  sections 6 and 7, and check 1100 at its statements on the class of
  (3.61). Of row 1099 I read the start and Lemma W.
- The test-model claims of 5.3 (U(1), Gaussian, model B) are argued, except
  the exact b-independence of the Gaussian two-sample law.
- Files changed: this file only. No commit, no push, no post. One guide run
  (pure Python, one thread, in the session scratch area).

### 6.3 Who checked what

Claude Opus 5.5, reasoning effort max (this laptop subagent, row 1120),
checked every item of 6.1 by hand against the sheet, the lane files named in
Step 2 and OpenAI's source at the cited lines. The writer of row 1119 is
Claude Fable 5.2 medium, the same provider. Credits as in the sheet's 6.4:
OpenAI's authors for (3.6), (3.11)-(3.16), (3.54)-(3.62); Yan Ru Pei for the
coarse-orientation transfer behind Lemma CO; Jacob van den Berg and
Christian Maes for disagreement percolation; Roland Dobrushin and Senya
Shlosman for the mixing conditions; Jurg Frohlich and Thomas Spencer
(recalled). Ethan Sussman and Levent Alpoge, and Tadeusz Balaban, for the
account that the lane serves; neither is an input of this check.

RESULT: row 1119 HOLDS AFTER CORRECTION and no item FAILS (Claude Opus 5.5 max, by hand, same provider as the writer Claude Fable 5.2 medium; OpenAI Section 3 source read at the cited equations in row 1078's copy, whose hash matches check 1100; one pure-Python guide run): the definitions of K_c, R_c and (1.3), (2.0), the identity 2.1, the trivial bound (2.1), Lemma IBP with (2.2)-(2.3), Lemmas LOW and SR given (2.4), Lemma CH, Lemmas CH2, CH3 and DEEP given (3.61), each use inside its class (a square whose boundary spins are all fixed by conditioning), Lemmas TS and TS2 (constant 2 suffices) and (4.1)-(4.2) given Lemma CO hold; (2.4) holds uniformly in l at least s, not only at cells comparable to s, once its profiles are C^3 bumps that vanish near the ends of the middle halves (bookkeeping written here, proved given OpenAI (3.14), (3.16), (3.54)); corrections: the rough-profile energy bound holds in mean or with high probability (proved here with constant 1/6), Lemma GB's tools clause holds only for pins of bounded range and with no pointwise current bound (the Gaussian sheet fails (3.12) at unbounded pins and the bound on N_y; guide run gives R_c^2/b^2 near 0.0746 and c_0 near 0.245), the two-copy weight sentence, the reasons in the readings of Lemma SR and of the way-2 stop, the first-moment scope of Lemma LOW, the scope of the neutrality of the gauge-fixed rings, and (N-CH), which by Lemma CH is (i) itself; the stop by the third rule is valid once the named step lists the inputs (3.6), (3.11), (3.12) that way 1 uses, and the three ways are distinct and none is an excluded route; Lemma TS2 does not make (H-two) in total variation circular as a hypothesis for (CONV), since it gives a bound with no decay at one separation, but with its converse proved here (Lemma TS3) every two-sample form with a small constant is one-scale mixing of the class it tests, so the weakest form that still passes the U(1) and first-order tests is (H-two-N1), one bounded neutral core observable at a time, which is still a one-scale singlet mixing statement, and a non-circular bad-cell tail must be conditional outside a collar as in OpenAI (3.58)-(3.60) (argued); not formalized, no mass gap claimed.
