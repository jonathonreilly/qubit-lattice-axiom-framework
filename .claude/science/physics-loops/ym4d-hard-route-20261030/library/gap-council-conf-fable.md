# Gap council: lattice gauge theory and confinement (FINISH row 1130)

Member: Claude Fable 5.2 max, laptop subagent. Background taken: lattice gauge
theory and the physics of confinement (centre vortices, 't Hooft twisted
boundary conditions, electric and magnetic flux free energies, Mack-Petkova,
Tomboulis, Polyakov loops, dualities, the order-one crossover of SU(2) and of
its finite subgroups).

Status of this file: complete (five steps, RESULT line at the end). Outcome:
all three attacks were found to be on file already (Step 4).
No mass-gap claim is made anywhere in this file.

Marks used: PROVED (a proof is written here or a named theorem is cited with
its hypothesis checked), ARGUED (a physics argument, not a proof), GUIDE (a
numeric or heuristic indication only), OPEN (not known).

## Plan (five steps)

1. Read `library/gap-council-brief.md` in full. State the obstacle of its
   Section 3 in the terms of this field: the object, the nearest known
   theorem, the line where that theorem stops.
2. Propose at most three attacks, ranked. For each: mechanism; exact first
   statement with quantifiers; the line where it fails for compact U(1), for
   a product with a massless factor, and for frozen Q_8 or the binary
   tetrahedral group; nearest item of Section 5 and the difference; cheapest
   decisive test.
3. Attempt the first statement of the top attack: a proof, a counterexample,
   or a named line where it fails.
4. Only then read `parts/gap.md` (crux section, route registry, test table,
   methods set aside 1 to 34) and the FINISH RESULT lines it cites. Mark each
   attack new or already tried, with its row.
5. End with one RESULT line.

## Step 1. The obstacle of Section 3 in the terms of this field

Source read: `library/gap-council-brief.md` only. Papers below are cited from
memory. None was re-read in this row. No proof step in this file rests on one
of them. The proofs in Step 3 use only (TM) and (TM-c) of the brief.

### 1.1 The object

The object is the pair of 't Hooft flux free energies of the periodic torus
('t Hooft 1979, Nucl. Phys. B153).

Notation. Fix a 4D periodic box with sides (L_1, L_2, L_3, L_4). Z^+ is the
periodic partition function. Z^- is the same integral with the sign of beta
flipped on one stack of (1,2)-plaquettes, the plaquettes at one fixed position
in the (1,2)-plane and at all positions (x_3, x_4). This is the centre twist in
the (1,2)-plane. The stack is the vortex sheet. It spans directions 3 and 4.

- x = Z^-/Z^+. Vortex (magnetic flux) free energy: F_v = -log x.
- Electric flux free energy: exp(-F_e) = (Z^+ - Z^-)/(Z^+ + Z^-).
- With T the transfer operator along direction 1 and Theta the centre flip of
  the 2-links through one plane (brief, (TM), (TM-c)): Z^+ = Tr T^{L_1},
  Z^- = Tr(T^{L_1} Theta). So exp(-F_e) = Tr_odd T^{L_1} / Tr_even T^{L_1}.
  F_e is the free energy of the flux sectors that are odd in direction 2.
- Duality (PROVED, one line of algebra, Step 3 item F4):
  sinh(F_e) sinh(F_v) = 1. This is the Kramers-Wannier form of 't Hooft's
  Z_2 Fourier relation.

The wall (W) of the brief, in these words, has two halves.

- (W-flux) The flux half. For every flux sector e != 0, the gap times the side
  is at least F_e - D (PROVED, Step 3 item F1; D is the excess free energy of
  the brief). So the flux half of (Z-UNB) holds when F_e(L) is large. That is
  the statement that the centre-vortex free energy of the symmetric torus is
  tiny: F_v(L) below about 2 exp(-(256 D_0 + 30)).
- (W-0) The zero-flux half. The first excited state of the zero-flux sector
  (the glueball) must also have gap times side above 256 D_0 + 30. Flux
  free energies do not see this half. A product with a massless factor has
  the flux half and not this half.

The expected flow of x with the physical side L (none of this is proved):

- Small L (weak coupling). ARGUED: the periodic torus has a 4-parameter family
  of flat connections with a U(1) stabilizer (torons). The twisted torus has
  an isolated flat connection, the twist eater (holonomies i sigma_1,
  i sigma_2). Counting Gaussian modes gives x of order g(L)^3. So F_v is about
  3 log(1/g(L)) and falls slowly as L grows. The classical cost of the twist
  is zero. (Small-volume work: Luscher 1983; Coste, Gonzalez-Arroyo,
  Jurkiewicz, Korthals Altes 1985; Gonzalez-Arroyo and coworkers on twisted
  boxes.)
- Large L. GUIDE (numerics: Kovacs-Tomboulis 2000; de Forcrand-von Smekal
  2002): F_v falls like L_3 L_4 exp(-sigma L_1 L_2) and F_e grows like
  sigma L_1 L_2, with sigma the string tension.
- So x(L) is believed to rise from about g^3 to 1. The band of the brief is
  the range of L where x crosses the self-dual value x* = sqrt(2) - 1
  (F_e = F_v = log(1 + sqrt 2) = 0.881).

The comparison models in the same words:

- Coulomb phase (compact U(1) at weak coupling; ARGUED from the Gaussian flux
  model, computed in Step 3 item C1): the flux weights are exp(-e^2/(2 beta r))
  with r = L_3 L_4/(L_1 L_2). On the symmetric torus x is a constant below 1.
  It does not run. The flux energy spreads over the cross-section.
- Frozen finite group (Q_8, binary tetrahedral; PROVED at beta = infinity by
  counting, Step 3 item C2): x tends to a ratio of counts of flat connections.
  The twist eater exists in Q_8 (i and j anticommute), so x does not tend to
  0. It tends to a constant below 1. The flux sectors hold degenerate ground
  states. This is topological order.
- Product with a massless factor: x is the SU(2) value. The flux half is true.
  The zero-flux half is false.

### 1.2 The nearest known theorems

1. 't Hooft 1979. Exact duality between electric and magnetic flux free
   energies. With a mass gap assumed, it gives a dichotomy: one of the two
   fluxes is heavy.
2. Tomboulis-Yaffe 1985 (Comm. Math. Phys. 100). Reflection positivity
   (chessboard) gives: a Wilson loop of area A in the (mu,nu)-plane of the
   box is at most exp(-F_e) to the power A/(L_mu L_nu). So growth of F_e
   like the area gives the area law.
3. Mack-Petkova 1979 and Frohlich 1979. Comparison with Z_2: the SU(2) Wilson
   loop is bounded by the Z_2 Wilson loop at the same beta. This confines for
   beta below the Z_2 transition (self-dual point 0.4407).
4. Mack-Petkova 1980. Vortex containers: a sufficient condition for the area
   law from the twist free energy of thick tubes, uniform over the boundary
   condition of the tube.
5. Munster 1981. At strong coupling the vortex free energy is of order
   exp(-sigma A), by a convergent expansion.
6. Tomboulis 2007 (arXiv:0707.2179). An attempt to carry the twist ratio from
   weak to strong coupling with Migdal-Kadanoff bounds. Ito-Seiler 2007
   (arXiv:0711.4930) found the gap: the interpolation parameter is not shown
   to be the same for Z^+ and Z^-.

### 1.3 The line where the theorems stop

- Items 1, 2 and 4 transport a flux free energy. They move it between
  observables (twist to Wilson loop) or assume the gap. They do not create
  growth of F_e.
- Items 3 and 5 create it, only below beta about 0.44 (item 3) or in the
  convergence region of the expansion (item 5). Item 3 is uniform over the
  plaquette couplings K_p = beta |tr U_p|/2. That is the failed kind "uniform
  over plaquette coupling fields" of Section 5.
- Item 4 needs a supremum over boundary conditions. That is the failed kind
  "uniform over pins".
- Item 6 is the one attempt at a (K-flow). It stops at the Ito-Seiler line.
  Its recursion is the same for U(1), so it is group-blind (Section 5,
  route RG).

One sentence. The field has exact tools that transport flux free energies
and no tool that makes F_e grow at order-one coupling.

### 1.4 The selective inequality in the words of this field

ARGUED. Let E_e(L_2; L_3, L_4) be the lowest energy of the sectors with odd
flux along direction 2. Doubling the length of the tube at least doubles the
energy, up to a Casimir term (PROVED, Step 3 item F2). So

  z_e(2L) >= 4 kappa z_e(L) - (Casimir term),

where kappa is the factor kept when both transverse sides are doubled:
E_e(L; 2L, 2L) = kappa E_e(L; L, L). For a free photon kappa = 1/4 exactly
(Gauss law, the flux spreads). The flux half of the stuck step is

  kappa > 1/4 at every size of the band, with a fixed margin.

This is antiscreening. ARGUED: at weak coupling z_e grows like a positive
power of g^2(L) (Luscher's small-volume value is g^(2/3)), so 4 kappa exceeds
1 by an amount of order g^2(L), by asymptotic freedom (the vacuum is a colour
paramagnet: Nielsen 1981, Hughes 1981). The exact power is not needed here. At large size kappa tends to 1 (the flux tube has a fixed width). In
a frozen group kappa is not the issue: the flux energy is exponentially
small at every size. The exact form of "kappa stays away from 1/4" is the
statement (VEXT) of Step 2: the vortex free energy is extensive in the
sheet. In the Coulomb phase it obeys a square-root law instead (Step 3,
item C1).

## Step 2. Three attacks, ranked

Scope note. The twist tools of this field address the flux half (W-flux).
Attack 1 is for that half only. Attack 2 is an exact flow that covers both
halves. Attack 3 is for the zero-flux half (W-0) only. At the seed size the
zero-flux half is the binding one (GUIDE: with m about 3.5 sqrt(sigma), the
flux value sigma L^2 exceeds m L once L sqrt(sigma) is above about 3.5).

Notation for boxes: (L_1, L_2, L_3, L_4), twist in the (1,2)-plane, sheet
along 3 and 4. "Plane doubling" doubles L_1 or L_2. "Sheet doubling" doubles
L_3 or L_4.

### Attack 1 (top). The duality ladder for the flux half

Mechanism. Three exact facts hold for every box (Step 3, F2 to F4). (a) Plane
doubling at least doubles F_e, minus a Casimir term: two flux tubes end to end
cost at least twice one. This is trace positivity only. (b) Sheet doubling
changes F_v by an identity with two doubling defects, of the periodic and of
the twisted transfer operator along the sheet. (c) sinh F_e sinh F_v = 1. In a
phase with a finite correlation length the vortex free energy is extensive in
the sheet, so sheet doubling multiplies F_v by about 2. By (c) a bounded factor
in F_v is only an additive loss in F_e. So above an order-one threshold F_e
grows by a factor 4 per doubling of the box, minus constants. In a Coulomb
phase the step (b) follows a square-root law instead, F_v(doubled) about
2 sqrt(F_v), and the ladder stalls. That law is the spreading of the flux.

First statement, with quantifiers. (VEXT): there are v_0 > 0, M < infinity
and sizes L_* < L_s such that for every cutoff index j and every dyadic
physical size L with L_* <= L <= L_s, and for each of the two boxes
B = (2L, 2L, L, L) and B = (2L, 2L, 2L, L): if F_v(B) <= v_0, then
F_v(B') <= M F_v(B), where B' is B with its shortest sheet side doubled.

The other inputs. (FSEED): F_e(L_*^4) >= 2 D_* + (2/3) log M + 1.1.
(BDD-2): the even-sector excess D_even is at most D_* on the boxes (L,L,L,L)
and (2L,L,L,L) of the range. Given the three, Step 3 item LAD proves
F_e((2^k L_*)^4) - c >= 4^k (F_e(L_*^4) - c), with
c = 2 D_* + (2/3) log M + 0.1, and then the flux half of (Z-UNB) by F1.

Where it fails for the comparison models.

- Compact U(1) at weak coupling: at (VEXT). In the Gaussian flux model the
  odd-flux weight goes from q to sqrt(q) under sheet doubling, so
  F_v(B')/F_v(B) = q^(-1/2), unbounded as q tends to 0 (Step 3, C1). At weak
  coupling (FSEED) fails too: F_e is of order exp(-pi^2 beta/2).
- Product with a massless factor: nowhere. Its flux half is true. The proof
  of the wall fails at (W-0), which this attack does not claim. So Attack 1
  alone can never give the gap.
- Frozen Q_8 and binary tetrahedral group: at (FSEED). At beta = infinity,
  F_e <= D_even always (Step 3, C2): Q_8 has F_e = 0.262 against
  D_even = 3.95; the binary tetrahedral group has F_e = 0.033 against 4.82.
  The cause is the degenerate flat connections, the same count that inflates
  D. (VEXT) holds there with M = 1, so the seed is the selective line.

Nearest item of Section 5. "Contraction or sign statements proved by
class-wide tools (routes RA, RB): their terminal obligation is the target."
Steps (a) and (c) are class-wide. The difference: the terminal obligation is
not the target. It is (VEXT), a one-sided gluing statement with any finite
constant M, and an order-one seed in place of z > 256 D_0 + 30. It is also not
a block criterion: the twist has no corners.

Cheapest decisive test. GUIDE, numerics: measure x on (2L,2L,L,L),
(2L,2L,2L,L) and (2L)^4 at beta 2.3 to 2.5 for L = 4 and 6 (the "snake"
method of de Forcrand, D'Elia and Pepe 2001 gives twist ratios directly).
Read two things. First, the ratio F_v(B')/F_v(B) once F_v < 0.3: about 2
supports (VEXT); growth like F_v^(-1/2) kills it. Second, the size at which
F_e passes 2 D_* + 1.8. Published twist data (Kovacs-Tomboulis 2000;
de Forcrand-von Smekal 2002) may already decide the first point.

### Attack 2. Thermodynamic integration in the bare coupling (an exact K-flow)

Mechanism. Fix the number of sites n and move beta. For any two partition
functions on fixed lattices, d/d beta of log Z is minus the mean action. So

  F_v(n, beta_j) = F_v(n, beta_fp) - integral_{beta_j}^{beta_fp} DA d beta,
  Phi_4(n, beta_j) = Phi_4(n, beta_fp) - integral_{beta_j}^{beta_fp} S d beta,

with DA(n, beta) = <A>^-_{n^4} - <A>^+_{n^4} (twisted minus periodic mean
total action) and S(n, beta) = <A>_{(2n)^4} - 16 <A>_{n^4} (the finite-size
shift of the mean action). These are identities (PROVED, calculus). Take
n = n_j = L/a_j. Let beta_fp(n) be the coupling at which n sites span the
first-passage size. Along the path the lattice stays fine and the physical
side grows from L_fp to L. The start is first-passage data from the account
(Balaban; Sussman-Alpoge), on a small box. The path is short: ARGUED from
asymptotic freedom, beta_fp - beta_j is about 0.37 log(L/L_fp). The input is
a difference of two means of the action in the law of the model. The
consumer is an identity. No clause of type (L3) is needed.

First statement, with quantifiers. (RESP): there are sizes L_fp < L_s, a
number n_0 and s_0 > 0 such that for all n >= n_0 and all beta with
L_fp <= n a(beta) <= L_s: S(n, beta) >= s_0, and
s_0 (beta_fp(n) - beta_s(n)) >= Phi_fp - Phi_s, where Phi_fp bounds
Phi_4 at first passage and Phi_s is the value that the seed needs. The twist
form (RESP-tw) is the same with DA >= a_0 and v_fp - v_0. It gives (FSEED)
of Attack 1.

Weak-coupling value. ARGUED (count of Gaussian modes, torons excluded):
log Z^+(n^4) = -((9 n^4 - 3)/2) log beta + const, so S = 45/(2 beta) and
Phi_4 = (45/2) log beta + const; DA = 3/(2 beta). So at weak coupling both
flows have the right sign and the defect falls like (45/2) log of the
effective coupling. The band needs the same sign with a size.

Where it fails for the comparison models.

- Compact U(1) at weak coupling: at the first line. The identities hold, but
  the path is empty: the bare coupling does not move with the cutoff, and
  "n a(beta) between L_fp and L_s" has no meaning.
- Product with a massless factor: at "s_0 (beta_fp - beta_s) >= Phi_fp -
  Phi_s". S is the SU(2) value, but Phi_4 keeps a floor that does not depend
  on beta. (RESP-tw) holds for the product; the flux half is true there.
- Frozen Q_8, binary tetrahedral: at "S >= s_0" and "DA >= a_0". In the
  frozen phase the responses are exponentially small while Phi_4 and F_v
  stay at the counting constants. At the first-order point the mean action
  jumps and the flow lands in the frozen phase.
- Positive-character weights at their first-order coupling: the identity
  holds; (RESP) fails because Phi_4 >= log 2 at coexistence.

Nearest item of Section 5. "Criteria in the law of the model for pinned
cells: one-sample means need a uniqueness clause." The difference: no pins,
tori only, and the consumer is an exact identity, so no uniqueness clause
is needed. It is also near "sign statements": the sign S >= 0 alone gives
only monotonicity. The size s_0 is the open part. It is the wall in
differential form.

Cheapest decisive test. By hand: the one-loop constant of Phi_4 against the
floor 17.04 of row 988 (same mode count, U(1) has 15 x 1 in place of
15 x 3). GUIDE, numerics: mean plaquette on n^4 and (2n)^4 for n = 4, 6 at
beta from 2.2 to 2.8, with and without twist; integrate S and DA over beta.

### Attack 3. The Higgs bridge for the zero-flux half

Mechanism. Add a fundamental Higgs field of fixed length with hopping
kappa. The model stays gauge invariant and reflection positive. For kappa
above some kappa_0(beta) a convergent expansion gives a gap at any beta,
including the window (Osterwalder-Seiler 1978; Fradkin-Shenker 1979; cited
from memory, hypotheses not checked). Fradkin-Shenker complementarity says
that the Higgs region and the confinement region are one phase. GUIDE
(numerics, Bonati-Cossu-D'Elia-Di Giacomo 2010): for beta below about 2.7
the path in kappa crosses only a crossover. So integrate in kappa at fixed
beta from the proved massive anchor kappa_0 down to kappa = 0, with the
same calculus identity as in Attack 2.

First statement, with quantifiers. (HB): for every beta in the window there
are kappa_0 and n_0 such that for all n >= n_0:
Phi_4(n; beta, 0) <= Phi_4(n; beta, kappa_0) + integral_0^{kappa_0}
|S_kappa(n; beta, kappa)| d kappa, and the integral is at most eps(n) with
eps(n) tending to 0. S_kappa is the finite-size shift of the mean hopping
energy.

Where it fails. U(1) with a charge-one Higgs: the path at large beta crosses
the Higgs-Coulomb transition; the integral does not tend to 0. Product with
a massless factor: at the anchor; the Higgs field does not gap the other
factor. Frozen Q_8 and binary tetrahedral: the zero-flux half is true there;
at kappa = 0 the centre symmetry returns and the flux sectors are
degenerate, so the bridge cannot give the flux half. It is a partner of
Attack 1, not a rival.

Nearest item of Section 5. "An anisotropic bridge from the beta_L = infinity
face (BR-2), blocked at (SING)." The difference: the anchor is at the same
beta, in another coupling, and it is a convergent-expansion regime. The
weakness is the same: no carrying inequality is known near kappa = 0. Ranked
last for that reason.

Cheapest decisive test. By hand: find how far down in kappa the
Osterwalder-Seiler expansion reaches at beta 2.3. If its radius stays far
from 0, as expected, the bridge needs a new step and should be dropped.

## Step 3. Attempt at the first statement of Attack 1

Outcome in one line. The consumer of (VEXT) is PROVED (items F1 to F4 and
LAD). (VEXT) itself is OPEN. The attempt stops at the named line V4. (VEXT)
is PROVED false in the Coulomb flux model (C1), and the seed is PROVED to
fail for frozen Q_8 and the binary tetrahedral group at beta = infinity (C2).

### 3.0 What is used

Only this, from the brief: for each box and each direction there is a positive
trace-class transfer operator T with Z^+ = Tr T^n, n the length along that
direction (TM); the centre flip Theta of the links of one other direction
through one plane commutes with T, Theta^2 = 1, and Z^- = Tr(T^n Theta) for
the twist in the plane of the two directions (TM-c). Also: Z^- > 0, because
the twisted weight is positive.

Flag. The identity Z^- = Tr(T^n Theta) is the standard one (the flip at one
time step is the sign change of beta on the stack of plaquettes). It was
not matched line by line to the lane's (TM-c).

One more use, flagged. Item F3 needs (TM) for the twisted weight along a sheet
direction: Z^- = Tr T_-^n with T_- positive. The flipped plaquettes are
spatial for that direction, so the standard form exp(-V/2) K exp(-V/2) with
a real V gives it. This was not checked against the lane's text of (TM).

Notation along direction 1: P_+ and P_- project on Theta = +1 and -1;
a_+(n) = Tr(T^n P_+), a_-(n) = Tr(T^n P_-). Then Z^+ = a_+ + a_-,
Z^- = a_+ - a_-, exp(-F_e) = a_-/a_+. The eigenvalues of T on each sector
are non-negative. lambda_0 is the top eigenvalue of the even sector and
mu the top eigenvalue of the odd sector. D_even(n) = log(a_+(n)/lambda_0^n).

F0 (PROVED). mu <= lambda_0 and 0 < F_e < infinity. Proof: a_+(n) - a_-(n) =
Z^-(n) > 0 for every n. If mu > lambda_0 the left side is negative for large
n. a_- > 0 because T is positive and the odd sector is not empty.

### 3.1 The exact items

F1 (PROVED), flux gaps from F_e. Let E_odd = log(lambda_0/mu). For every n:
n E_odd >= F_e(n) - D_even(n). For every s <= n:
F_e(n) >= (n - s) E_odd - D_even(s).
Proof. a_-(n) >= mu^n and a_+(n) = lambda_0^n exp(D_even(n)) give the first.
Each odd eigenvalue is at most mu, so a_-(n) <= mu^(n-s) a_-(s); with
a_+(n) >= lambda_0^n and a_-(s) <= a_+(s) this gives the second.
Use. Every flux sector e != 0 is odd in some direction. So its gap times the
side is at least F_e - D_even for the twist plane of that direction. Large
F_e on the symmetric torus is the flux half of (Z-UNB).

F2 (PROVED), plane doubling. F_e(2n) >= 2 F_e(n) - delta_even(n), where
delta_even(n) = 2 log a_+(n) - log a_+(2n) and 0 <= delta_even(n) <=
2 D_even(n).
Proof. For non-negative numbers, sum of squares is at most the square of the
sum. So a_-(2n) <= a_-(n)^2 and a_+(2n) <= a_+(n)^2, which is
delta_even >= 0. Also a_+(2n) >= lambda_0^(2n), which is the upper bound.
Divide. The same holds along direction 2, by the symmetry of the twist plane.
Remark. In the limit of infinite time the same step reads
E_odd(2 L_2) >= 2 E_odd(L_2) for the absolute sector energies. The loss term
is then the ground-state deficit of the lane's Lemma K.

F3 (PROVED, with the flag of 3.0), sheet doubling. Let T_+ and T_- be the
transfer operators along a sheet direction without and with the twist,
lambda_+ and lambda_- their top eigenvalues, f = log(lambda_+/lambda_-),
R_+(n) = Tr T_+^n/lambda_+^n - 1 and the same for R_-. Then f >= 0 and

  F_v(n) = n f + log(1 + R_+(n)) - log(1 + R_-(n)),
  F_v(2n) = 2 F_v(n) + delta_-(n) - delta_+(n),
  F_v(2n) <= 2 F_v(n) + 2 R_-(n) + R_+(2n),

with delta_+ and delta_- the doubling defects 2 log Tr T^n - log Tr T^(2n) of
T_+ and T_-, both non-negative.
Proof. f >= 0 because Z^-(n) <= Z^+(n) for all n. The first two lines are
the definitions. For the third: n f <= F_v(n) + R_-(n), and
F_v(2n) <= 2 n f + R_+(2n).

F4 (PROVED), duality. With x = exp(-F_v): exp(-F_e) = (1 - x)/(1 + x) =
tanh(F_v/2), and sinh F_e = 2x/(1 - x^2) = 1/sinh F_v.
Two bounds used below: F_e >= -log(F_v/2), and F_v <= (8/3) exp(-F_e) when
F_e >= log 2 (from artanh y <= y/(1 - y^2) <= (4/3) y for y <= 1/2).

LAD (PROVED, conditional). Let B_0 = (L,L,L,L), B_1 = (2L,L,L,L),
B_2 = (2L,2L,L,L), B_3 = (2L,2L,2L,L), B_4 = (2L)^4. Assume
(i) D_even <= D_* for B_0 along direction 1 and for B_1 along direction 2;
(ii) (VEXT) for B_2 and B_3 with constants v_0, M;
(iii) 4 F_e(B_0) - 6 D_* >= log(8M/(3 v_0)) and v_0 <= 1.
Then F_e(B_4) >= 4 F_e(B_0) - 6 D_* - 2 log M - log(4/3).
Proof. F2 twice: F_e(B_2) >= 2(2 F_e(B_0) - 2 D_*) - 2 D_* =
4 F_e(B_0) - 6 D_*. By (iii) and F4, F_v(B_2) <= (8/3) exp(-F_e(B_2)) <=
v_0/M. (VEXT) twice: F_v(B_3) <= M F_v(B_2) <= v_0 and F_v(B_4) <=
M^2 F_v(B_2). F4: F_e(B_4) >= -log(F_v(B_4)/2) >= F_e(B_2) - log(4 M^2/3).
Corollary. Put c = 2 D_* + (2/3) log M + (1/3) log(4/3). If (i), (ii) hold
at the sizes L_*, 2 L_*, ..., and F_e(L_*^4) >= c + 1 and (iii) holds at
L_*, then F_e((2^k L_*)^4) - c >= 4^k (F_e(L_*^4) - c) for all k in the
range. With F1 the flux sectors satisfy gap times side >= 4^k + c - D_*.
Correction to Step 2: the seed (FSEED) must also satisfy (iii). For v_0 not
below exp(-3.4 - 2 D_*) M^(-5/3) this is implied by F_e >= c + 1.
Number of steps. From an order-one seed to 256 D_0 + 30 takes at most
about log_4(256 D_0 + 30) doublings, 5 for D_0 = 1. (VEXT) is needed on that
bounded range only. Above it the lane's Theorem S takes over.

GUIDE (numerics, scratch script, not a proof): F1 and F2 were tested on
20000 random non-negative spectra with no violation; F4 to 12 digits.

### 3.2 The comparison models

C1 (PROVED for the model; ARGUED as the weak-coupling form of compact U(1),
theorems of Guth and of Frohlich-Spencer not re-checked). Gaussian flux
model: the electric flux through the cross-section is an integer e with
weight q^(e^2), q = exp(-L_1 L_2/(2 beta L_3 L_4)). The Z_2 twist ratio is
x = theta_4(q)/theta_3(q) = 1 - 4q + O(q^2), so F_v = 4q + O(q^3). Sheet
doubling replaces q by sqrt(q). So F_v(B') = 2 sqrt(F_v(B)) to leading order
and F_v(B')/F_v(B) = q^(-1/2). No M works. Numbers: q = 1e-4 gives the ratio
100; q = 1e-8 gives 10^4. On the symmetric torus at beta = 1, 2, 4:
F_e = 0.029, 0.0002, below 1e-6. So both (VEXT) and (FSEED) fail.

C2 (PROVED by a hand count; the script agrees). Frozen limit: the weight is
the indicator that every plaquette is 1 (with the twist: -1 on the sheet).
Then x = N_tw/N_per for every box, where N_per counts commuting 4-tuples of
the group and N_tw counts 4-tuples with g_1 g_2 = -g_2 g_1 and all other
pairs commuting.
- Q_8: N_per = 2 x 176 + 6 x 64 = 736. N_tw = 24 x 4 = 96 (24 ordered
  anticommuting pairs; the other two entries are central). x = 0.1304.
- Binary tetrahedral: N_per = 2 x 1008 + 6 x 64 + 16 x 216 = 5856.
  N_tw = 96 (the anticommuting pairs lie in Q_8). x = 0.0164.
- The twist in two orthogonal planes, (1,2) and (3,4), has no flat
  connection in either group: count 0.
The transfer operator is a projector. The even and odd ground spaces have
dimensions (N_per + N_tw)/(2|G|) and (N_per - N_tw)/(2|G|): 52 and 40 for
Q_8, 124 and 120 for the binary tetrahedral group. So F_e = log(52/40) =
0.262 and log(124/120) = 0.033, while D_even = log 52 = 3.95 and
log 124 = 4.82. In general F_e = log(dim_even/dim_odd) <= D_even there. The
seed needs F_e >= 2 D_* + 1.1. It fails at every size. At large finite beta
in the frozen phase the same holds up to Peierls corrections (ARGUED).

Product with a massless factor. x, F_e and F_v are those of SU(2). LAD
applies and its conclusion is true for the product. This is consistent: LAD
concerns flux sectors only.

### 3.3 The attempt at (VEXT) for Wilson SU(2)

V1 (PROVED), equivalent forms. By F3, (VEXT) with M = 2 + eps is
delta_-(n) - delta_+(n) <= eps F_v(n). In the electric picture let
w(n) = Z_odd(n)/Z^+(n) = (1 - x(n))/2 be the odd-flux weight of the box
with sheet side n. For two decoupled boxes the odd-flux weight is
(1 - x(n)^2)/2. So (VEXT) is the gluing statement

  (GLUE)  1 - x(2n) <= C (1 - x(n)^2),  M about 2C:

gluing two boxes along a face transverse to the flux raises the odd-flux
weight by at most a constant factor. With C = 1 it reads x(2n) >= x(n)^2.
In terms of the normalized second exterior powers
l_+ = Tr Lambda^2(T_+^n)/(Tr T_+^n)^2 and l_- (the same for T_-), the
doubling defects are delta = -log(1 - 2 l), so C = 1 is l_- <= l_+.

V2 (PROVED, not sufficient). F3 gives F_v(2n) <= 2 F_v(n) + 2 R_-(n) +
R_+(2n). The term R_+(2n) is the excess of the periodic box. It contains the
flux weights of that same box, about 3 exp(-F_e(B_4)) on the symmetric
torus. So this bound returns F_e(B_4) >= F_e(B_4) - log 3 at best. It is
circular. A proof must bound the difference D_+ - D_-, not each term.

V3 (PROVED), trace positivity is not enough. For positive operators with
Tr B^k <= Tr A^k for all k, (GLUE) can fail: A with the single eigenvalue 1
and B with two eigenvalues (1 - eta)/2 have x(n) = 1 - eta and
x(2n) = (1 - eta)^2/2, so 1 - x(2n) is about 1/2 while 1 - x(n)^2 is about
2 eta. The pattern is a twisted operator with two near-degenerate top states
over a periodic one with a single top state.

V4 (the named line where the attempt stops). By V1, (VEXT) with
M = 2 + eps is exactly

  log[(1 - 2 l_+)/(1 - 2 l_-)] <= eps F_v(n),

and l_- <= l_+ suffices (M = 2). To first order in small l this is
l_- <= l_+ + (eps/2) F_v(n). In words: the twisted cross-section must have
no low-lying two-state weight that the periodic one lacks. The Coulomb phase has one, the spreading mode, and fails by the
square-root law. I have no proof of this line for Wilson SU(2) at order-one
coupling and no counterexample. Every tool I know for it (thick 't Hooft
loops with chessboard bounds; Mack-Petkova containers) loses a perimeter
term or a supremum over boundary conditions. ARGUED: it holds whenever the
flux tube has formed, since then the odd-flux weight is extensive in the
cross-section.

### 3.4 What this step establishes

- PROVED: F0 to F4, LAD and its corollary, C1 (model), C2 (frozen limit),
  V1 to V3.
- OPEN: (VEXT) on the range from L_* to the seed size; (FSEED), an
  order-one seed for the flux half; (BDD-2).
- Not addressed: (W-0). The ladder is silent on the zero-flux sector.
- Net: the flux half of the wall follows from an order-one flux seed plus a
  gluing bound with any constant, in place of z > 256 D_0 + 30 for the flux
  sectors. The selective content is isolated in (GLUE): constant factor
  (massive) against square-root law (Coulomb).

## Step 4. New or already tried

Read at this step, and not before: `parts/gap.md` (state of attack, routes
tried, methods set aside 19 to 34 as listed there, route registry, test
table, exact price); methods 1 to 18 in `library/gap-crux-exercise2-max.md`
6a (L392-416), with the Route E lines of that file found by search
(L448-523, first 300 to 500 characters of each line only); the FINISH RESULT
lines of rows 878, 1004, 1018 and 1025 in full; keyword context only in rows
731, 744, 754, 789, 792, 800, 899, 923, 936, 996, 1016 and 1076. Rows named
below with "by search" were not read.

Verdict. All three attacks are already on file. None is new.

### 4.1 Attack 1: already tried, row 878 (Route E), found again almost line for line

- Row 878 (`library/gap-crux-exercise2-max.md`, Step 8.1; check row 884) has
  the same ladder. Its Lemma WS (found again there) is F2 here. Its Lemma TD,
  q(2n) <= 2 (1 + S)^2 (q(n) + S_v/2) with the exact free law
  q -> 2q/(1 + q^2), is F3 with V2 here. Its statement (TS-theta), "when both
  transverse sides double, the flux free energy falls by a factor below 4",
  is the selective step. Its Theorem E gives geometric growth above an
  order-one seed. Its fact tests are C1 and C2 here: U(1) Coulomb has
  theta = 4 exactly from the theta sums; frozen groups pass (TS-theta) and
  fail the seed.
- Difference. (VEXT) is the case theta = 1 of (TS-theta) with an additive
  constant, written in the dual variable F_v. So (VEXT) asks more than
  (TS-theta), and LAD is a special case of Theorem E. This is no gain.
- The stop is the same. Row 878: "one needs that the vortex energy (the
  shift between the spectra of T_0 and T_v) is nearly the same in the excited
  states as in the ground state. That is a locality statement". Here: V4.
  The form with normalized second exterior powers (V1, V4) is a restatement.
- Other rows of the same family. Row 744 (Theorem R, a finite quantitative
  form of 't Hooft's duality; prior work 't Hooft 1979, Nguyen-Tanizaki-Unsal
  2023). Row 731 (Theorem S-w with the twisted transfer operator of rows 698
  and 716; the open piece is (EV-STEP)). Row 1004 (Lemma TW; Theorem TW-T is the input (TM-tw) that my
  item F3 flagged). Row 1018 ((T-vor): vortex containers, Lemma PAR,
  Corollary MP of Mack and Petkova; open (SER), (SPR)). Row 1025 (the
  Tomboulis-Kanazawa line; its one open inequality (TB)_n; Lemma FAC: the
  line reads one factor, so it gives the flux half only). Row 1052 (Lemma
  FLUX-W: (W) is the gap plus an unbroken-centre statement on tori). Row 1051
  with its checks 1056 and 1057 (Lemma K4: the classical cost of the centre
  twist is zero). Row 1127
  (surface sums for the twist deficit pay a volume-exponential cost; it does
  not bind transfer-positivity bounds such as F2).
- Methods set aside that Step 1 and Step 2 touched without knowing: method
  13 (flux half from glue half by clustering; re-judged in row 878 6d, which
  is where (TS-theta) comes from); method 14 (thin Z_2 lift with Griffiths
  inequalities, "mean coupling 1.5 against 0.44"; this is item 3 of 1.2
  here); method 17 (thick vortex by field-independent spreading, refuted as a
  method); method 18 (Migdal-Kadanoff, group-blind; item 6 of 1.2 here).
- Possibly not on file (by search of FINISH only; not checked further): the
  hand counts of C2 for Q_8 and the binary tetrahedral group (736, 96; 5856,
  96; ground-space dimensions 52, 40 and 124, 120). Their conclusion is on
  file (row 878 fact tests; row 884).

### 4.2 Attack 2: already tried, route RB (rows 754, 996), twist form row 800

- Route RB of the registry: "the plaquette shift on fixed boxes; a sign in
  beta; (MON') / Theorem D (f)", "same as RA in the coupling variable"
  (row 998 7.3). Status there: blocked-equivalent, "a sign with no small
  number; false in the class".
- Row 754 (keyword context only): "delta = 48 a^4 times the integral of the
  finite-size shift of the ground-state plaquette". I read this as the same
  calculus identity. It also has Proposition VB (volume blindness, argued):
  local loop equations with reflection positivity cannot bound these shifts.
- Method 4 of the set-aside list: "one-way step for a torus quantity;
  step-scaling couplings: each step as hard as the seed; fails where two
  confining phases coexist". The flow of the twist ratio in Attack 2 is of
  this kind.
- Row 996 lists the finite-size plaquette shift of Theorem D (f) among the
  three path statements already in the lane.
- The twist form (RESP-tw) appears to be (K-RESP) of row 800 (Kanazawa's
  line: "a bound on the original Wilson twist score at order one with all
  normalizers"; file not read), with Proposition KR of row 1025.
- What Step 2 adds is only a size: the path in beta has length about
  0.37 log(L/L_fp), and the ARGUED weak-coupling values S = 45/(2 beta) and
  DA = 3/(2 beta). These are not a mechanism. Not compared with the start
  values of rows 1058 to 1060.

### 4.3 Attack 3: already tried, rows 905, 908, 923

- Row 923 (THERM-DI-pin): "the pinned model is exactly the fixed-length
  fundamental SU(2) gauge-Higgs model with kappa = h". It stays OPEN: no
  uniform rate on the pin path; an operator inequality on the vacuum
  complement cannot be box-uniform once the vacuum moves. Row 923 cites the
  same numerics (Bonati, Cossu, D'Elia, Di Giacomo 2010). Row 1076 lists
  "the fundamental Higgs path" as on file. Row 1016 lists the frozen
  fundamental Higgs form among ten exact reformulations that fail.
- Same stop as in Step 2: no carrying inequality toward kappa = 0.

### 4.4 What this says

- A blind pass from the confinement side re-derived three lines that the
  lane already holds, and stopped at the lines the lane names: (TS-theta)
  with its locality statement (row 878), the sign with no size of route RB,
  and THERM-DI-pin (row 923). This agrees with the saturation reading of
  rows 878 and 998.
- The record already holds the standard tools of this field: 't Hooft
  duality, Tomboulis-Yaffe, Mack-Petkova, Tomboulis with the Ito-Seiler gap
  and Kanazawa, Durhuus-Frohlich, Borgs-Seiler, Luscher's small volume, the
  Schrodinger functional, Gopfert-Mack, Tanizaki-Unsal (by search of FINISH,
  rows not read: among them 656, 661, 688, 702, 711, 744, 784, 797, 800,
  1005, 1011, 1012).
- Advice from this field, ARGUED. Centre-twist tools read one factor (Lemma
  FAC of row 1025; the product test). They can give the flux half and never
  the zero-flux half. At the seed size the zero-flux half is the binding one
  (GUIDE). So no further row should be spent on a twist-only line unless it
  comes with a step for the even sector, which is the registry's reopen
  condition for route RE.
- Two words absent from FINISH by search, offered as readings and not as
  attacks: (a) (TS-theta) is antiscreening, and its margin 4 - theta starts
  positive at first passage (order g^2, ARGUED), where compact U(1) has
  exactly zero; so (TS-theta) is a (K-flow) quantity with a start value, not
  a (K-one) number. (b) The order-one seed of Theorem E is the statement that
  the symmetric box of side L_* lies on the confined side of the
  finite-volume deconfinement crossover (the Svetitsky-Yaffe reading; row
  1063 places the N_t = 4 deconfinement coupling at the lower edge of the
  band). Neither changes a verdict.

## Step 5. RESULT

RESULT: Row 1130 (Claude Fable 5.2 max, laptop subagent, council member for lattice gauge theory and confinement; checked by no one; one small guide script, no literature search, papers cited from memory). No new attack, and the wall (W) does not move. In the terms of this field the obstacle is the pair of 't Hooft flux free energies of the symmetric torus: the flux half of (W) is the growth of the electric flux free energy F_e (equivalently a tiny centre-vortex free energy F_v, with sinh F_e sinh F_v = 1), the zero-flux half is the glueball gap, and the nearest theorems ('t Hooft duality, Tomboulis-Yaffe, Mack-Petkova, Munster, Tomboulis with the Ito-Seiler gap) transport flux free energies but do not create growth at order-one coupling. Three attacks were proposed blind and all three are ALREADY TRIED: (1) the duality ladder for the flux half = row 878 Route E (Lemma WS, Lemma TD, (TS-theta), Theorem E; check 884), found again almost line for line, with my hypothesis (VEXT) only the case theta = 1 of (TS-theta); (2) thermodynamic integration in the bare coupling = route RB (rows 754, 996; Theorem D (f)) and, in twist form, (K-RESP) of row 800; (3) the Higgs bridge = THERM-DI-pin of rows 905, 908, 923. PROVED here by hand (unchecked; found again from row 878 except the counts): F1 (flux gaps are at least F_e minus the even excess), F2 (plane doubling at least doubles F_e minus a Casimir term), F3 (sheet doubling identity and a bound with an additive thermal term), F4 (duality), LAD (conditional growth F_e(2L) >= 4 F_e(L) - 6 D_* - 2 log M - log(4/3) above an order-one seed), C1 (the Gaussian flux model obeys a square-root law, so (VEXT) fails in a Coulomb phase), C2 (frozen limit by hand count: Q_8 has x = 96/736, binary tetrahedral 96/5856, and F_e <= D_even, so the seed fails), V3 (trace positivity alone does not give the sheet step). OPEN, at the same line as row 878: the sheet step for Wilson SU(2) (V4, a locality statement for the excited states of the twisted against the periodic sheet operator), the order-one flux seed, and all of the zero-flux half. ARGUED advice: centre-twist tools read one factor and give at most the flux half, which is not the binding half at the seed size; spend no further row on a twist-only line without an even-sector step. No mass-gap claim.
