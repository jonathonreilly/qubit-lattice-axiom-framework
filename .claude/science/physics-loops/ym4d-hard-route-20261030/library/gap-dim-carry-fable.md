lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-23T00:40Z

# gap-dim-carry-fable: the four-dimensional carry (queue row 1390)

Research-stage working state. Nothing here is a public claim. Pinned at commit a1f83f4da on branch
`claude/ym4d-hard-route`. Worker: Claude Fable 5.2 (high), one session, no subagents. Started 2026-11-22T12:40Z (date -u).

## 0. Plan (written first, before reading the inputs in full)

Target of the row: (M-neutral) of row 1367, with the checked chain to the mass gap (rows 1342, 1349, 1356, 1359).
State handed over by the row: every surviving fact separates SU(2) from compact U(1); none separates d = 4 from
d = 5 at the scales of the band. Missing: a carry over the scales of the band that uses d = 4 (requirement (b) of
row 1386, section 4.3).

Steps, each appended to this file as it is done:

1. Read rows 1379 to 1389 and their files; restate (M-neutral), the band, the filter (t1) to (t5), Remark PAIR,
   and requirement (b). Section 1.
2. List candidate carries that use d = 4, run the filter and the five-dimensional test on each, and grep
   `library/open-core.md`, `library/gap-*.md` and the FINISH rows for each before calling it new. Section 2.
3. Attack the surviving candidate: a first exact lemma, proved in full, or a quantified obstruction for a named
   class of carries. Sections 3 onward.
4. End with the next two rows and their decisive outcomes, and the RESULT line.

Status log (times from date -u):

- 2026-11-22T12:40Z file created with the plan; nothing derived yet.
- 13:05Z read: FINISH.md L1-84 and L299-360; GOAL.md; rows 1378 to 1391 in full; RESULT parts of rows 708, 977, 996,
  1025, 1128, 1141, 1332; `gap-mech-direction2-fable.md` in full; `gap-mech-direction-fable.md` L155-300
  (mechanism families M-A to M-F, Remark TAD); `prior/gap-outside-read-opus.md` L479-531 (flow monotones);
  `gap-afield-b-max.md` L180-192 (B10, B11); `gap-outside-box-max.md` L150-158 (I14 to I16). Not read in full:
  the check files of rows 1381, 1384, 1385, 1387, 1389 (RESULT parts only) and `gap-layer-force-cov-fable.md`.

## 1. The target and the hand-over, as read

**Target.** (M-neutral), `gap-seed-astra62.md` L11 (gpt-6.2-astra, row 1367; Lemma M1 and Corollary M2 are Claude
Fable's row 1356, checked by row 1359): one physical side L on the trajectory, n_j = L/a_j, 4 | n_j, beta_0 <=
beta_j <= B_0 log n_j; in the range of P_0 put s_(n,beta)(t) = sum over a >= 1 of (lambda_a/lambda_0)^t; wanted
s_(n_j,beta_j)(2 w_j) <= 4/21 at every late cutoff, w_j = floor(n_j/1024).

**Where the carry sits.** Theorem T of row 1332 (Claude Fable; check 1335): one finite inequality, (A1) the
ultraviolet carry (row 1391 runs in parallel), (A2) the infrared carry: a seed at a window coupling beta_w gives a
seed at every larger coupling at a size at most C exp(c beta), c below about 4.0 (GUIDE), against 3 pi^2/11 = 2.69
at one loop. (A2) is the band. Row 1386 4.1 writes it per doubling as (STEP), with delta > 0.173 against the
one-loop 0.2575.

**Hand-over (rows 1379 to 1389).** Every surviving proved fact separates SU(2) from compact U(1) and none separates
d = 4 from d = 5 at the scales of the band. Remark PAIR (row 1386 4.2, credited there to row 1128): a mechanism
is a local gain that reads the group times a carry that reads the dimension, x(2L) = 2^(d-4) x(L) - g_G; the lane
holds gains and no carry with a sign. Requirement (b) (row 1386 4.3): the carry uses d = 4 through the exact
classical factor over all scales of the band, not through local counts. The filter (row 1386 4.5): (t1) compact
U(1); (t2) SU(2) in d = 5, applied to the step; (t3) SU(3); (t4) the hypothesis fails as beta grows at a fixed
lattice; (t5) not the target renamed: name the method.

**Kind of result of this file (stated first).** I found no carry with a sign that reaches (M-neutral). The file
gives: (i) the list of the exact ways in which d = 4 can enter a statement about the lattice law, each with its
match on file (Section 2); (ii) proofs that close one class that was not on file by name, the grid (metric,
dilation) carries: Lemma CW, Proposition REF, Corollary MKO, Remark NOSIGN (Section 3); (iii) the candidate that
survives the filter best, with what it lacks (Section 4); (iv) the next two rows (Section 5).

## 2. The exact ways d = 4 can enter, each with its match on file

"Exact" means: an identity or an inequality of the lattice model at every coupling. Repo search for this section:
one loop of `grep -l -i -F` over `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md` (counts of
files in brackets); `library/open-core.md` has no line on a carry, on the marginal dimension or on five
dimensions (grep for carry, "d = 4", "five dim", marginal: no hit).

| # | How d = 4 enters | Exact lattice form | On file | Step-level test in d = 5 | Verdict |
|---|---|---|---|---|---|
| D1 | Marginality under coarsening: a block plaquette is 2^2 plaquettes in series in its plane and 2^(d-2) in parallel across it | bond moving and decimation; exact as an inequality for Z only | rows 1025 (Tomboulis's line; Propositions BR, SIGN, Lemma FAC, Identity MOV), 1128 (G1); Migdal-Kadanoff [41], Tomboulis [117] | the factor is 2^(d-4) by construction | no sign on a quotient (row 1025); Section 3 re-derives the inequality by a trace inequality and adds the order of the two operations plane by plane |
| D2 | Conformal weight: the plaquette weight of a diagonal metric, w_(mu nu) = prod over rho not in {mu, nu} of a_rho / (a_mu a_nu), has degree d - 4 | Lemma CW below | anisotropic couplings [111], Karsch [17]; "soft dilation", "dilation move", "anisotropy field", "conformal factor": no hit | degree 1: a dilation is a first-order change of every coupling | new by name; closed in Section 3: in d = 4 a dilation is not a move of the lattice law, and the grid refinements that remain are D1 |
| D3 | Self-duality of 2-forms and of the centre: electric and magnetic flux are both 3-vectors; Z_2 and Villain U(1) gauge theory are self-dual | 't Hooft's twist relations on a symmetric torus; Wegner duality of the Z_2 part of the SO(3) x Z_2 form | twists throughout the lane; Wegner [9]; Kramers [5]; electric-magnetic [9] | the twist relation Z(n_(1d)) = Z(n_(12)) holds in every d; the self-dual form does not | serves the flux half only (rows 1175, 1177, as quoted in row 1380 M-B); the Z_2 part is ordered at the lattice scale in the window. Not a carry |
| D4 | Topology: pi_3(SU(2)) = Z, the twist n_12 = n_34 = 1 has charge 1/2 and a scale-free classical action pi^2 beta | Z_kappa/Z_0 is an exact lattice quotient; its classical value is exact only as beta grows at a fixed lattice | fractional instanton [13], instanton [46], n_12 = n_34 [10 or more], `gap-kappa-order.md`; B10 of row 1005's line (Chern-Simons form) | cost pi^2 beta n: grows | a coupling in a twist scheme: passes (t1) to (t4), reads the flux half, and its carry is (K-flow) renamed (t5) |
| D5 | The logarithmic bubble, sum over x of G(x)^2 | the marginal method of Aizenman and Duminil-Copin needs a current representation with positivity | `prior/gap-lit-marginal.md` (row 885): no gauge transfer; Aizenman [37], random current [12] | no logarithm | no positivity for SU(2) (row 737's negative term); proves triviality-type bounds, the wrong direction |
| D6 | Borderline monotonicity: r^(4-d) times the energy in a ball (Price), the Yang-Mills heat flow (Hamilton; Struwe), t^2 <E(t)> | per configuration the flowed action decreases; under a translation-invariant law that is all it says | B11 of `gap-afield-b-max.md`; I15 of `gap-outside-box-max.md`; `prior/gap-outside-read-opus.md` F1 to F6 | exponent d/2 against 2 (Section 4.1) | exact identity for the flow-scheme beta function (Section 4.1); no monotonicity theorem and no consumer (I15) |

**What the table says.** There are two exact dimension-reading inequalities at every coupling: the bond-moving
bound of D1 and, in the same family, the refinement bound of D2. Both bound a partition function and neither
bounds a quotient. D3 to D6 are identities or schemes: each gives a running coupling whose monotonicity is the
missing carry, not a proof of it.

- 13:12Z Sections 1 and 2 written. Next: Section 3, the grid class.

## 3. The grid class (dilations as moves): closed

**Why this class.** The lane's soft moves need a colour frame, and no frame is soft on typical fields (Remark TAD
of row 1380; Theorem C1; row 1141 (2)). A dilation needs no frame, and classically it costs nothing in d = 4 and
only there. So "soft dilation moves" is the one blind candidate for a carry that meets requirement (b) by its
definition. It is not on file by name (Section 2, D2). This section shows what it is on the lattice.

**Class GRID (definition).** A product grid on the d-torus assigns a spacing a_mu(x_mu) > 0 to each layer of
links of direction mu. Its plaquette weight is the classical one,

  w_(mu nu)(x) = prod over rho not in {mu, nu} of a_rho(x_rho) / (a_mu(x_mu) a_nu(x_nu)),

and the model is the gauge model with plaquette weights f^(w), or with the series and parallel powers below. A
grid carry is a relation between the partition functions, or the transfer-operator spectra, of one weight family
on two product grids of one torus.

**Lemma CW (conformal weight; PROVED, one line).** Under a_mu -> lam a_mu for all mu, with one lam > 0,
w_(mu nu) -> lam^(d-4) w_(mu nu). So in d = 4 the weights of a grid do not change when every spacing is multiplied
by one factor, and for d = 4 the three products w_12 w_34, w_13 w_24, w_14 w_23 are 1.
Proof. The numerator has d - 2 factors and the denominator has 2. In d = 4 the numerator of w_12 is a_3 a_4, the
denominator of w_34. QED.

Consequences (PROVED, immediate).
- (a) In d = 4 a dilation of the whole grid is the identity map on lattice laws. It is not a move. The only
  lattice form of "the same physics at the doubled scale" is a change of the number of sites, that is a block map.
- (b) In d = 5 the same dilation multiplies every coupling by lam. Its first-order cost is lam' beta times the
  sum of the plaquette means, of the order of the volume. This is the exact form of the factor 2^(d-4) of Remark
  PAIR, and it is the (t2) verdict for the class: no softness in d = 5.
- (c) What is left in d = 4 is the shape of the grid: the refinement of one direction at a time.

**Proposition REF (refinement of one direction; PROVED GIVEN Weyl's majorant theorem, cited and not rebuilt; the
statement is the one-direction form of the bond-moving bound of Migdal, Kadanoff and Tomboulis, on file in row 1025;
the route by a trace inequality is item B6 of `gap-constraints-max.md` L265, RECALLED there).**
Let G be a compact group, Lam a finite spatial lattice (any dimension), H = L^2(G^(links of Lam)). Let p_o > 0 be
continuous class functions, one for each orientation o of a spatial plaquette, and k_nu continuous class functions
of positive type, one for each spatial direction nu. Put P = multiplication by the product of p_o(U_q) over the
spatial plaquettes q, and A = K_0 Pi, K_0 = the tensor product over the links of the convolutions by k_nu, Pi = the
mean over the gauge maps. Then A >= 0 (K_0 >= 0 commutes with the projection Pi, because each k_nu is a class
function), A is trace class, and the partition function of Lam times M periodic time steps is Z_M(p, k) =
Tr (P^(1/2) A P^(1/2))^M. Write F = P^(1/2) A P^(1/2) (the fine step) and C = P A^2 P = (P^2)^(1/2) A^2 (P^2)^(1/2), which is the step
with weights (p^2, k * k) (the coarse step), since A^2 = (K_0)^2 Pi is the convolution step with k * k. Then

  (i)   lambda_0(F)^2 <= lambda_0(C);
  (ii)  prod over i < m of lambda_i(F)^2 <= prod over i < m of lambda_i(C) for every m >= 1;
  (iii) Tr F^(2q) <= Tr C^q for every real q > 0, so Z_(2N)(p, k) <= Z_N(p^2, k * k);
  (iv)  (i) to (iii) hold in each common eigenspace of the centre operators (each electric sector), and for each
        spatial twist.

Proof. (i) lambda_0(F) = norm of A^(1/2) P A^(1/2) = spectral radius of A P (the non-zero spectra of XY and YX
agree) <= norm of A P = lambda_0(P A^2 P)^(1/2). (ii) Apply (i) to the m-th antisymmetric powers of A and P, which
are positive, and for which the m-th power of F is P_m^(1/2) A_m P_m^(1/2) with top eigenvalue the product of the
first m eigenvalues of F. (iii) By (ii) the sequence lambda_i(F)^2 is weakly log-majorized by lambda_i(C); Weyl's
majorant theorem gives the sum of phi over the first sequence at most the sum over the second for every phi with
phi(e^s) convex and increasing; take phi(x) = x^q. (iv) A and P commute with the centre operators, and a spatial
twist changes signs inside P only; restrict A and P to the sector and repeat. In infinite dimension A is trace
class and P is bounded, so F and C are positive and trace class and the eigenvalue sequences are well defined. QED.

**Corollary MKO (the classical factor, plane by plane; PROVED GIVEN REF for the inequality; the stiffness count
is ARGUED and uses Proposition G1 of row 1128).** Let w be a positive continuous class function of positive type.
Apply REF to the directions 1, ..., d in turn on the torus (2n)^d. Pointwise squares of positive-type functions are
of positive type (Schur), convolution squares of positive functions are positive, so every step is admitted. Then

  Z_((2n)^d)(w) <= Z_(n^d)({w_(mu nu)}),   w_(mu nu) = T_d ... T_1 w,   T_rho = S (convolution square) if rho is
  mu or nu, and T_rho = Q (pointwise square) otherwise.

Each orientation gets exactly two S and d - 2 Q. With s = - (log w)''(0): Q doubles s exactly, and S halves it and
subtracts a constant (G1). So every orientation has the classical factor 2^(d-2) 2^(-2) = 2^(d-4), exactly as in
Lemma CW, and the two operations do not commute: in d = 4 the plane (12) gets Q Q S S w and the plane (34) gets
S S Q Q w, with different gains. This is Remark PAIR as an exact inequality on the true lattice, for Z.

**Remark NOSIGN (the quotient has no sign; PROVED by an explicit example).** (M-neutral) reads the quotient
sum over i >= 1 of (lambda_i/lambda_0)^t. Log-majorization, even with equal determinants, fixes no sign for it.
Take A = diag(2, 1) and P = [[2, 1], [1, 2]]. Then F^2 has the eigenvalues of (A P)^2, which are f = 12 + 6 sqrt 3
= 22.39 and 12 - 6 sqrt 3 = 1.608, and C = P A^2 P = [[17, 10], [10, 8]] has c = (25 + sqrt 481)/2 = 23.47 and
(25 - sqrt 481)/2 = 1.534. (Check: both products are 36; (12 sqrt 3 - 1)^2 = 433 - 24 sqrt 3 < 481.) So the fine
operator has the smaller gap: f_1/f_0 = 0.0718 > c_1/c_0 = 0.0654. Now add one commuting level: A' = A + (a), P' =
P + (b) as direct sums, with a^2 b^2 = e. Both F'^2 and C' get the eigenvalue e. For e = 100 the top level is e
in both, and the fine operator has the larger gap: f_0/e = 0.224 < c_0/e = 0.235. Both signs occur. A small
perturbation that couples the blocks keeps both strict inequalities (the eigenvalues are continuous), so
irreducibility does not help.

**Verdict on the class GRID.** In d = 4 a dilation is not a move (Lemma CW). The grid relations that remain are
refinements, and they are the bond-moving bound (REF, MKO). They bound each sector trace and each product of top
eigenvalues from above. They give no sign on a quotient (NOSIGN; Proposition SIGN and Identity MOV of row 1025
for the twist quotient; item B6 with (VAC-SUB) for the seed). **The class is closed.** New here against the file:
Lemma CW and the reduction of "dilation moves" to bond moving; the proof of REF by antisymmetric powers (B6 has it
RECALLED); the order of S and Q plane by plane; the explicit example NOSIGN. None of this moves (M-neutral).

- 13:15Z Section 3 written (Lemma CW, Proposition REF, Corollary MKO, Remark NOSIGN; two wording repairs in place).
  Next: Section 4.

## 4. What survives the filter, and what each survivor lacks

### 4.1 The variable of a carry must be a coupling, and every coupling has the same carry

**Remark RAD (elementary for the free field; ARGUED for its use).** The thermal sum of (M-neutral) has no
classical factor. For a free massless field on a box of side L in any dimension d the levels are 2 pi |k| / L,
so at the time c L the sum over levels of exp(- c L E) does not depend on L. So s itself is scale-free in d = 4
and in d = 5 alike, and the factor 2^(d-4) of requirement (b) can only enter through a variable x(L) that is an
inverse coupling at the scale L. A mechanism then has three obligations, not two:

- (O1) a coupling x(L) with an exact definition on the lattice law, read on typical fields;
- (O2) the carry: x(2L) <= 2^(d-4) x(L) - g at every scale of the band, with g at least 0.173 in d = 4
  (row 1386 4.1, row 1332 (A3), GUIDE);
- (O3) a consumer: x(L) below a named value gives s <= 4/21 at that L. By Remark FI of row 1386 (HOLDS AFTER
  CORRECTION in check 1387) a consumer needs a clause that excludes a mixture; a first-order point of a
  nearest-neighbour model is such a mixture (K7, belief grade, `parts/gap.md` L28-30).

**Three couplings with an exact lattice definition (O1).**

| Coupling | Definition | Classical factor | (t1) U(1) | (t2) d = 5 | (t3) SU(3) | (t4) | On file |
|---|---|---|---|---|---|---|---|
| x_kap, twist scheme | - log(Z_kappa/Z_0)/pi^2 on the torus n^4, twist n_12 = n_34 = 1 | pi^2 beta n^(d-4): the action of the constant abelian field with plaquette angle pi/n^2 in the planes 12 and 34 is 2 n^d beta (1 - cos(pi/n^2)) <= pi^2 beta n^(d-4), by 1 - cos u <= u^2/2 (elementary GIVEN the standard constant-flux configuration on the twisted torus, not written out; the matching lower bound is the continuum bound of 't Hooft and is not rebuilt) | flux sectors, constant cost: zero gain | grows like n | twists mod 3 exist (RECALLED) | fails as beta grows: yes | D4; step scaling and twist ratios, row 720 Part 2 and H16 of row 1002 (as cited in `gap-crux-exercise3-max.md` L438 and `prior/gap-outside-read-opus.md` F1) |
| x_fl, flow scheme | 1/(t^2 e(t)), e(t) the mean Wilson action per site of the field flowed for the time t | Identity FLOW below: exponent d/2 against 2 | Gaussian: zero gain | exponent 5/2: x grows | same definition | yes | D6; I15; B11; F1 to F6 of row 1005 |
| x_adj, blocked roughness | 1/q_k, q_k the mean lowest eigenvalue of the adjoint covariant Laplacian of the k times blocked field on a block cell of fixed side | block-plaquette variance 2^(4-d) per step for a Gaussian field (ARGUED) | q_k = 0 identically (a constant section) | q_k falls like 2^(-k) (ARGUED) | same definition | yes | the unblocked form is row 1141 (2) (gpt-6.2-astra; check 1142), which holds in d = 5 because it reads the fine field; the blocked form is not on file by name and nothing is proved for it here |

**Identity FLOW (PROVED, two lines; the definition of the scheme, not a monotone).** Let V_t be the Wilson flow
of U, dV_t/dt = - grad S(V_t), S = sum over p of (1 - x_p), and e(t) = E S(V_t) per site under any law. Then
de/dt = - E |grad S(V_t)|^2 per site, so

  d log x_fl / d log t = R(t) - 2,   R(t) = t E |grad S(V_t)|^2 / E S(V_t).

For the free lattice field in d dimensions, with the flow normalized as theta' = - d* d theta, each transverse
mode has the same mean energy and decays like exp(- 2 t phat^2), so e(t) is a constant times (e^(-4t) I_0(4t))^d and R(t) = 4 d t (1 -
I_1(4t)/I_0(4t)) = d/2 + d/(32 t) + O(t^(-2)). So the carry in this scheme is the inequality R(t) <= 2 - g' in
d = 4. The free value is 2 from above (a lattice term d/(32t)), and 5/2 in d = 5. No bound on R is proved here;
B11 and I15 already record that no monotone is known.

**Proposition SCHEME (logic only; the perturbative input is RECALLED and is a gap).** Each coupling above has
the classical factor 2^(d-4), and for a scheme that is regular in perturbation theory the one-loop gain is the
universal 0.2575 per doubling for SU(2). So at weak coupling (O2) is one statement in all schemes, and in the
band two schemes differ by a map between couplings of order one that nothing on file controls. Naming another
scheme is therefore not a candidate: by (t5) the candidate is a method for (O2), and by Remark RAD a second
method for (O3).

### 4.2 The methods with a sign, and where each stops

| Method | Sign it gives | Reads d = 4 | Stops at | Source |
|---|---|---|---|---|
| Soft moves in a colour frame | disorder, at the classical cost | yes, if the cost is a curl form | no frame is soft on typical fields: lab frame (Theorem C1), pin-measurable site frames (Theorem BD), field-built frames (row 1141 (2), (9)-(13)); dressed moves are a renormalization step | rows 1034, 1141, 1380, 1381 |
| Dilations and grids | none on a quotient | yes, exactly (Lemma CW) | not a move in d = 4; refinements are bond moving | Section 3 (new by name) |
| Bond moving and decimation | upper bound on Z, on each sector trace, on products of top eigenvalues | yes, 2^(d-2) 2^(-2), plane by plane | no sign on a quotient | row 1025; B6; Section 3 |
| Data processing under an exact block map (Proposition LIFT) | disorder: the cost of a block move is at most the cost of any lift | only through the lift | the lift with the classical cost is a soft move (first line); the variance term is a dressed lift (Lemma BOG) | rows 1383, 1385 |
| Correlation inequalities, current representations | either | yes, through the bubble | no positive representation for SU(2) | row 885; row 737 |
| Flows (Wilson flow, Langevin) | the action falls along the flow | exponent d/2 (Identity FLOW) | no monotone for a ratio; no consumer | B11, I15, row 1005 |
| Entropic monotones (a-theorem) | the ends of the flow only | yes | an end with free photons is allowed | row 1002 (`gap-compact-rigidity-max.md` L35); row 975 |
| The account's renormalization step | both, with constants | yes | running coupling at most gamma | row 1012; `parts/gap.md` L46-48 |

**Judgement (mine; ARGUED).** The exact inequalities with the classical factor all have the sign of order or
bound Z alone. The one exact relation with the sign of disorder, Proposition LIFT, has the classical factor only
for a soft lift, and SU(2) has none without dressing. So requirement (b) and a sign are met together only by a
dressed step, which is a renormalization step at a coupling of order one (K-II of row 1386 4.4). I found no
statement of kind K-I. This agrees with row 1386 and adds one closed class to it.

