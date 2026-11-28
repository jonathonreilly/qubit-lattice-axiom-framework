# New mathematics for the gap: working file of FINISH.md row 1655

Author: Claude Fable 5.2 (max effort), one session, 2026-11-27/28.
Brief: FINISH.md row 1655 (the text of `brief-newmath-fable-max.txt`).
Status of this file: working record, written stage by stage. No statement
here is checked by a second reader. Labels: PROVED (complete proof in this
file), ARGUED, GUESSED, ON FILE (with the row).

## Stage 0. Reading record

(Appended as I read. Each entry names the primary file that I read, not
only the RESULT text.)

Outcome letters. The brief asks the RESULT to name the outcome "(a), (b),
(c), (d) or none" and does not define the letters. I fix them from the
task sentence of the brief, in its order: (a) a proof of the seed (PUR-io);
(b) a proof of another statement that gives the gap through a consumer on
file; (c) a new consumer with its input proved; (d) a disproof of a step of
the lane's reduction, or an obstruction theorem with explicit quantifiers
for a class of methods. "None" means none of these.

Read in full (primary files, 2026-11-27/28):

- The brief (FINISH.md row 1655 text); GOAL.md.
- `library/gap-k2-tool-design-fable.md` (row 1468): the consumer 3.1 (Fact
  PUR, the sixteen masses), the map Q2, Lemma TW, Theorem K2, Proposition GA,
  the filter 4.5, the sizing 5, the obstructions 6.
- `library/gap-direction8-fable.md` (row 1643): the tables 1.1 A to H, the
  scope note 1.5 on the Lean chain, Proposition COOL, the nine candidates of
  2.1.
- `library/gap-mech-direction2-fable.md` (row 1386): inventory F1 to F8,
  (SV-Z), Lemma GRP, Proposition NEG, Remark STAB, Remark PAIR, requirements
  (a) to (i), kinds K-I to K-III, filter (t1) to (t5), Remark FI.
- `library/gap-mech-direction4-fable.md` (row 1553): steps 1 to 17, the
  definition of an input, Lemma ALG, tests (g1) to (g6), the engine map 3.1,
  the triggers 3.3.
- `library/gap-mech-direction-fable.md` (row 1380): Lemma H, Remark TAD,
  mechanisms M-A to M-F, Lemma SP, Lemma BR, Theorem C1, Lemma PIN, Lemma H'.
- `library/prior/gap-2don-proofs-read-opus.md` (row 1007) and
  `library/prior/gap-o4-pinned-cell-read-opus.md` (row 1009): the lane's
  digests of the posted two-dimensional proofs (OpenAI; Ding, Huang and
  Yang). I did not read the preprints themselves. Everything I say below
  about those proofs rests on these two digests.

Read in part: `library/gap-mech-direction3-fable.md` L120 to L175 (the
Durhuus-Froehlich item and its withdrawal); the RESULT text of row 1383
(`library/gap-short-step-variance-fable.md`: Proposition LIFT, Lemma THIN,
Theorem U1, Lemma BOG).

What I take from the reading (each line ON FILE at the row named):

1. The seed is an infrared statement. With n = 512 u it says that the
   neutral thermal sum at temperature 1/u on the cube of side n is at most
   4/21 (Fact PUR, row 1468 3.1). Lemma FLOOR (row 988) and Remark STAB (row
   1386) say it fails in small physical boxes. No route avoids the band of
   order-one effective coupling (row 1442 (1); row 1643 2.2 (c)).
2. Two proved engines cross the same band in two dimensions (rows 1007,
   1009): a flow of an upper bound on a twist stiffness (needs a continuous
   global symmetry that acts on what the consumer reads), and a dilution by
   exchangeable copies (needs a ferromagnetic conditional model). Row 1553
   3.1 lists why neither has a gauge form on file: every continuous twist of
   gauge-invariant boundary data is a gauge map (step 13 (a)); lab-frame
   moves have site-local cost (Theorem C1 of row 1380); covariant frames fail
   on typical fields beyond ultraviolet scales (rows 1141, 1530, 1532, 1538).
3. The open triggers in component form are (T-copy), (T-ineq), (T-dual),
   (T-mix), (T-budget) (row 1553 3.3), with (R1) to (R12).

Also read in full after the first pass: `library/gap-crux-restate.md` L1
to L260 (row 697: Lemma A, Theorem D, Lemmas K, X, E, E', Theorem S,
Corollaries S2, S3'); `library/gap-solve9-astra62.md` L1 to L232 (row 1161:
(1) to (16) and the section "An explicit aspect for the one-cube test");
`library/gap-mech-direction4-check-astra62.md` sections (v) to (viii)
(check 1556); `library/gap-afield-b-max.md` B8 to B12.

## Stage 1. Screening: lines derived blind in this session, and where each is on file

Method. For each line I wrote the first exact statement before any search,
then searched `library/`, `library/prior/` and `parts/` (grep -l -i -F),
then opened the hit that the table names. "Opened" means I read the passage.
A grep count alone is marked "grep".

| # | Line, as I derived it | First exact statement | Where it is on file (opened unless marked) | Standing there |
|---|---|---|---|---|
| 1 | Stiffness flow of the 2D proofs with gauge moves. Lab-frame left translations of links have a second-order cost of mass type (the tadpole), so softness is lost above wavelength sqrt(beta). | cost of a one-colour move of profile f is beta abs(df)^2 + c abs(f)^2 with c of order one | row 1380: Lemma H, Lemma H', Remark TAD, Theorem C1 | closed for lab-frame moves; covariant frames blocked (rows 1141, 1530, 1532, 1538) |
| 2 | A relative colour rotation of two pinned sets is a gauge map unless a pinned path joins them. With a pinned flat 2-plane as the join, the links that leave the plane are a 2D O(4) model with right twists only, so the 2D theorems apply to them. | twist cost of the join is at most C beta t^2 / log(R_out/R_in) | row 1016 Lemma REM (`gap-global-reform-max.md` L497 to L604); row 1011 Lemma EMB, as listed in `gap-mini-solve-c-fable.md` L80 | gives charged decay only, weaker than the perimeter bound; no consumer |
| 3 | Freeze every (0,1)-plane (beta_L infinite): the 4D theory is a 2D sigma model with target SU(2)^E and the transverse gauge group as global symmetry; then descend in beta_L. | gap(beta_L) >= gap(infinity) | BR-2 with (MON-L), (SING): `parts/gap.md` L160 to L177, L239; rows 1072 to 1115 (RESULT texts) | blocked at (SING) and (MON-L) |
| 4 | The 2D O(4) rate pi is inside the budget c < 4.03 of Theorem T, so a comparison with sheets that loses the difference pi - 3 pi^2/11 would be enough. | seed size at most exp((pi + o(1)) beta) | remark COMB of row 1542, as read in row 1553 step 11; check 1556 (viii) | needs (A1) at rate p = 2 and (MON-L); check 1556 (viii) holds the algebra after correction (a drift fraction above 2/3 at p = 2) |
| 5 | Gribov region: the Faddeev-Popov operator is affine in the links and positive, so the ghost propagator is a submartingale under any filtration (operator Jensen), with increments that are conditional variances. | E[M^(-1)] >= (E M)^(-1); E[M^(-1) (-Lap) M^(-1)] >= ... | `gap-afield-b-max.md` B8, B9 (one-step form) | consumer: none found (Zwanziger's inequality has the wrong direction) |
| 6 | Reflection positivity makes time covariances of a slab observable non-negative, so a stiffness is bounded above by the seagull term minus static covariances. | F'' <= -<S''> - N Var(V_0) | `gap-mini-solve-ar-opus.md` Lemma PV | found again there; no 4D consumer |
| 7 | Hamilton's matrix Harnack inequality for the kinetic step: -Hess log(K psi) <= beta for every positive psi; harmonic-sum rule for stiffness. | Hess log u_t >= -1/(2t) | `gap-mini-solve-j-fable.md` L46; Corollary LD-2 of row 1460 (as cited in row 1468) | blind; the magnetic Hessian in lab directions is not a curl form |
| 8 | The Hamiltonian is formally a Witten Laplacian of the Chern-Simons functional. | H = (1/2) Q* Q, Q = g d/dA + B/g | `gap-afield-b-max.md` B10 | formal; (CS-lat) open |
| 9 | Class angles of plaquettes as a positive model on a polytope. | density sin(theta) exp(beta cos theta), log-concave iff beta <= 3 sqrt(3)/2 | `gap-afield-b-max.md` B12 | (LC-rho) open |
| 10 | Hopf coordinates: the W-hopping terms of adjacent like-oriented links carry a minus sign that no pi-shift of phases removes. | cross-ratio of Fourier coefficients negative | check 1556 (vi), Cartan-coset paragraph (a stronger form: all rephasings) | no ferromagnetic copy |
| 11 | A product of fundamental plaquette traces over an embedded lattice projective plane has negative Haar mean (Frobenius-Schur indicator -1), so no Griffiths or Ginibre inequality holds uniformly in plaquette coupling fields. | mean of the product = -2 d^(-...) < 0 | rows 737, 744 (Corollary NS0, a 92-plaquette plane), rows 754, 756 (Theorem EP-NO), as listed in `gap-brainstorm-max.md` L39 to L41 and `gap-loop-eq-opus.md` L119 to L135 | on file, checked |
| 12 | Virial form: in Kogut-Susskind variables d m / d g^2 is the electric minus the magnetic part of the excitation energy; the gap needs electric dominance with a rate. | Delta K - Delta V >= kappa m | H8 of row 1643 (rows 1645 to 1648); registry VIR-DOWN | no sign proved at any cold band point |
| 13 | Thermodynamic form: the seed is "pressure over T^4 below 1.3e-9 at aspect 512"; equivalently an exponentially small Casimir term. | log(1 + s) = V_4 (e(cube) - e(slab)) + crossed thermal sum | Lemma X of row 697 (the exact crossing identity); grep "Casimir" 163 files, "pressure" 204 files | restates the seed |
| 14 | Zero-momentum sector seed; sheared tori (the full lattice modular group). | thermal sum of translation-invariant neutral states | grep: "zero momentum" 54 files; sheared tori at `gap-band-fresh-fable.md` L104 | gains a factor about 2 in box size by my estimate; not pursued |
| 15 | Centre twist as the end point of a circle generated by electric fields; class-averaged it is the family Z(theta) with -Z''(0)/Z(0) = beta rho n^2. | Tr(D(theta) T^v), D = prod chi_j(theta)/d_j | M-B of row 1380 (C2 of row 1013, Corollary WN2); check 1556 (v) (a covariant circle that reaches the twist) | area-law barrier; rows 1557 to 1596 |
| 16 | Deconfinement obstruction: a step-scaling in one compact direction with periodic conditions crosses the finite-temperature transition, where the neutral length diverges for SU(2). | none (an obstruction) | not searched by name | not used; the seed's aspect keeps T below T_c when l is large |

Result of the screening. Sixteen lines; every one that I could turn into an
exact statement is on file, most of them with a check. This agrees with
rows 1386, 1442, 1553, 1643. By check 1443 it is not evidence that no
mechanism exists. I record it and do not count it as a result.

## Stage 2. A second reading of the node W7 of the reduction (row 1161, "An explicit aspect for the one-cube test")

Why. Row 1643 3.2 re-derived the eleven numerical lines of this section and
left three structural points untested: the bound 3/2 for every sector, the
zero slope of the vanishing crossed coefficients, and the passage from the
160 h comparison to "all seven top weights take the same side". Row 1643
2.3 reports that row 1457 5.3 calls this node the most likely place of a
real gap (I did not open row 1457). The author of row
1161 is gpt-6.2-astra, so this is a cross-provider reading. It is a reading
of L48 to L63, L120 to L135 and L213 to L227 of `gap-solve9-astra62.md`,
with (3), (4), (5), (9), (10) as stated there. I did not re-read rows 1157,
1158 or `gap-transfer-twisted.md`, which (3) cites.

Verdict: HOLDS at this reading level. No wrong line found. Each point:

1. **The bound 3/2 for every sector.** It is (3): X_(m,q)(u) <= X_(m,0)(u)
   <= X_(0,0)(u) = 1 + s(u). First inequality: X_(m,q) is (1/8) of a signed
   sum of the eight twisted integrals with static part m, each positive, and
   X_(m,0) is the unsigned sum. Second: three uses of "removing a seam
   involution that commutes with a positive operator does not lower the
   trace", one in each spatial frame. With s(u) <= 1/2 every sector trace at
   period u is at most 3/2. Used in the section only through sum of
   x^(u/n) <= 3/2 per sector, which is this bound. HOLDS given (3).
2. **Second derivatives.** For s >= 1/2 and u <= n/512: x^s (log x)^2 =
   x^(u/n) x^(s - u/n) (log x)^2 with s - u/n > 1/4, and z^2 e^(-z/4) <=
   64/e^2. So each sector trace has second derivative at most 96, I at most
   768, and H, an average of eight values of I, at most 768. HOLDS.
3. **Zero slope at finite cutoff.** H_(i,c,q)(s) is defined for real s by
   finite Fourier inversion of the interpolated I(s, B). At s = 1 +- r with
   (1 +- r) n an integer it equals a sector trace of the frame-i transfer
   operator on the box n x n x (1 +- r) n over time n, divided by
   lambda_0^((1 +- r) n) > 0. So H(1 +- r) >= 0. At s = 1 the box is the
   same cube, the frame-i neutral bound is the hypothesis itself, and (4)
   gives 0 <= H(1) <= h for M_i q not 0. Taylor with abs(H'') <= 768 gives
   abs(H'(1)) <= h/r + 384 r. HOLDS. The inversion formula
   I(s, B_i(c, e)) = sum over q of (-1)^(q.e) H_(i,c,q)(s) is an identity
   for all real s, because H is defined by the inverse transform; so the
   basis additions of (5) may be done on the interpolated functions and on
   their derivatives. Each addition changes the sign of at most four
   coefficients with M_i q not 0, so I changes by at most 8 h and I' by at
   most 8 x 2^(-59); twenty additions give 160 h and less than 2^(-51).
   HOLDS.
4. **The derivative identity.** The mean over the seven non-zero temporal
   twists of I(s, (0, e)) is X_(0,0)(s) - (1/7) sum over q not 0 of
   X_(0,q)(s), because the sum over e not 0 of (-1)^(q.e) is 7 for q = 0 and
   -1 otherwise. Its slope at 1 is -U_N + U_C. A purely spatial twist (m, 0)
   has I = sum over q of X_(m,q), slope -U_M. Both kinds have rank two. So
   U_C + U_M < 2^(-51) + U_N < 2^(-50). HOLDS.
5. **Same side.** For distinct non-zero q, q' the difference X_(0,q)(1) -
   X_(0,q')(1) is (1/8) times a sum over the four seams e with (q + q').e =
   1 of +-2 I(1, (0, e)), two of each sign; all four seams are non-zero, so
   each I is within 160 h of one reference value and the difference is at
   most 160 h. The tails are at most h each, so the top weights differ by at
   most 162 h < 2^(-160), while each top weight lies in [0, 2^(-46)] or in
   [1 - 2^(-46), 1]. So all seven lie on one side. HOLDS.
6. **Both branches.** Small side: S_per(n/2) <= 7 (2^(-23) + 2^(-84)) +
   2^(-84). For m not 0 the two aligned top weights A >= C satisfy A + C in
   [1 - 2^(-44), 1 + 2^(-44)], so A is large and C <= 2^(-46); S_kappa(n/2)
   < 2^(-19). Large side: each purely magnetic trace at s = 1 is below
   2^(-45), so X_(m,0)(n/2) <= 2^(-22) + 2^(-84) and S_kappa <= S_full <
   2^(-18); the 56 twisted integrals with a non-zero transverse restriction
   are each below 2^(-18). HOLDS.

What this reading does not cover: the proofs of (3) and of the even
multiplicity for M q not 0 (compensated translations; rows 1157 and
`gap-channel-astra.md`), Theorem S-w (the consumer of S_kappa), and the
passage from S_kappa to the gap of the limit. Label: a reading, not a check
row; HOLDS for the six points above.

## Stage 3. Two blind re-derivations that agree with the file, and three readings

Items 1 and 3 were derived here before I found them on file. Items 2, 4
and 5 are readings of on-file proofs. Agreement of an independent
derivation is weak evidence for the on-file statement. None of this is a
check row. Items 1 and 2 are cross-provider (the on-file authors are
gemini-4-neon and gpt-6.2-astra); items 3 to 5 are same-provider.

1. **Fixed lattice, beta to infinity: the purity tends to zero like
   beta^(-3/2)/log beta.** My count: a torus of V sites has 12 V link
   dimensions, gauge orbits of dimension 3 V - 3 at central torons, and 12
   toron directions, so 9 V - 9 Gaussian directions; with the four-holonomy
   integral of order s^(-3) log s this gives Z(V) of order
   beta^(-(9V-9)/2) (beta V)^(-3) log(beta V), hence Z(2V)/Z(V)^2 of order
   beta^(-3/2)/log beta. With lambda_0^(2u) <= Z_+(2u) (Lemma A (b)) the
   neutral thermal sum obeys 1 + s(u) >= P^(-1/2), so the neutral seed fails
   at a fixed lattice for large beta. ON FILE: Theorem 3 of row 1526
   (`gap-agy-seed-approaches-neon.md` 2.4), check 1527 (iii), with the same
   exponent and the same logarithm. My count is ARGUED (I did not bound the
   remainders); the on-file proof is the authority.
2. **The explicit aspect node W7.** Stage 2 above.
3. **(KP) of row 731.** I found that the pattern "ratio 1 on twists of rank
   at most two, 0 on rank four" satisfies sector positivity in every frame
   and invariance under all changes of basis, and violates (KP) (36 against
   8). For independent planes with one ratio x per twisted coordinate plane,
   the defect is D(x) = 6x + 9x^2 - 4x^3 - 9x^4 + 6x^5 - x^6 - 7 =
   -(1 - x)^2 (x^4 - 4x^3 + 8x + 7), which is at most 0 on [0, 1] because
   x^4 - 4x^3 >= -3 there. (Weights: 6, 12, 8, 3, 6 twists of rank two with
   1, 2, 3, 4, 5 twisted planes; 3, 12, 12, 1 of rank four with 2, 3, 4, 6.)
   ON FILE: row 733, Proposition ND and Lemma PD (RESULT text read; I did
   not open the proofs, so I do not know that the polynomial is the same).
4. **Lemma HS of row 1600** (unchecked there, row 1643 1.2). Read line by
   line (`gap-wmix-solve-fable.md` L28 to L38): A = B/sqrt(Z_+(v)) has
   Hilbert-Schmidt norm 1 and eigenvalues sqrt(w_i); the marginal is nu =
   sum of w_i psi_i^2; g -> g/sqrt(nu) is unitary from L^2(dx) to L^2(nu)
   and carries A to H; BC = <1, H 1>. Upper bound by the norm, lower bound
   by the top term with <1, phi_0> >= sqrt(w_0). Both arithmetic
   consequences hold (483 <= 484; (21/25)^(3/2) = 0.7699). HOLDS. Same
   provider as the author, so this is a second reading and not a
   cross-provider check.
5. **Proposition CL and Theorem S-w of row 731** (`gap-flux-exercise.md`
   8.3, 8.4), read once: Proposition CL (a) and (b) Steps 1 to 4, Lemma W
   and the transfer of Lemmas K, X, E, E' followed step by step; the index
   algebra in the proof of Lemma CL1 read but not redone, and its identity
   tested by hand on the rank pattern of item 3 at x = 0 and at x = (0, 0,
   m_3, m_4) (both sides agree: 1 and 1/2). No wrong line found. Same
   provider as the author.

## Stage 4. The crux: what I tried, and the first failing step each time

Each line below was worked by hand to its first failing step. None is new
to the file; the anchors are in Stage 1. I keep one paragraph each, as the
brief asks for dead lines.

**4.1 A one-sided flow for a boundary stiffness with no tadpole in the
direct term. Dead at the Fisher information.** Take the transfer kernel
between two constant abelian slice fields with holonomy angles 0 and theta
(Schroedinger-functional data). The twist commutes with the pins, so the
direct term of the second derivative reads only the last layer of time-like
plaquettes and is at most a constant times beta n (3 n^3 plaquettes, each
with a twist angle theta/n), with no mass term.
The exact stiffness is this direct term minus the variance of the total
electric flux along the pin colour at the boundary layer. An upper bound on
the stiffness needs a lower bound on that variance. A Cramer-Rao bound with
a one-colour move in the interior has a mass term in its denominator. For
a field-independent move the Fisher information is exactly site-local, a
multiple of beta times the squared reduced field (Lemma SP and Theorem C1
of row 1380). For a move along a covariant frame it is bounded below by a
mass term on typical fields (row 1141 (2), as cited in row 1380). So the
bound is sharp at most up to wavelength sqrt(beta). Moving the tadpole from the direct
term to the denominator changes nothing. ON FILE: Remark TAD and Lemma H'
of row 1380. One remark that I did not find written in these words
(ARGUED): the flow needs the tadpole cancelled exactly, not bounded. If the
exact variance is T + G (T the part that cancels the mass term, G the gain)
and a lower bound keeps only a fraction theta of it, the bound on the
stiffness is the classical term plus (1 - theta) T - theta G, and T/G grows
like wavelength^2/log. So a lossy variance bound is useless beyond a fixed
wavelength, however close theta is to 1. The two-dimensional proofs have
T = 0 by symmetry; that is why they may lose a factor (the O(3) text loses
a factor 2 in the rate, row 1009).

**4.2 A pinned flat plane as the carrier of a colour frame. Dead: no
consumer.** With the links of one coordinate 2-plane pinned to the trivial
connection, the links that leave the plane are two-dimensional chiral
fields with an exact global left symmetry and right twists only, which is
the class of the O(4) text. A spin wave along the plane bounds the cost of
a relative colour rotation of two pinned bodies joined by the plane by
C beta t^2 / log(R_out/R_in). This is exact softness, and it reads the
group (for U(1) the rotation is trivial). It is blind to the dimension, it
concerns a set of measure zero, and the decay it gives is weaker than the
perimeter decay of thin loops. ON FILE: Lemma REM (row 1016), Lemma EMB
(row 1011).

**4.3 Operator Jensen along a filtration. A small proved remark; no
consumer.** See Remark SM below.

**4.4 The virial sign. Dead: no method, and the smallest model has the
abelian sign.** In Kogut-Susskind form the lattice mass falls with beta
exactly when the excitation is electric-dominated. For one plaquette the
gauge-invariant problem is the odd Mathieu problem, whose anharmonic term is the
softening term of the cosine; at weak coupling its level spacing rises to
the harmonic value as g^2 falls (ARGUED: first-order perturbation theory).
So the one-plaquette model has the sign of compact U(1), and the
non-abelian sign must come from the commutator terms of several
plaquettes. ON FILE: rows 1645 to 1648, registry VIR-DOWN.

**4.5 Comparison with the frozen-plane sheets. Dead at (MON-L).** The
one-loop rate of four-dimensional SU(2), 0.3715 per unit of log scale in
beta, is larger than the O(4) sheet rate 1/pi = 0.318, and pi is inside
the budget 4.03 of Theorem T. So the needed comparison has the Griffiths
direction (lowering the in-plane coupling from infinity does not order the
system). Theorem EP-NO (rows 754, 756) excludes any such inequality that is
uniform in plaquette coupling fields; the homogeneous statement is open and
has no method. ON FILE: BR-2, (MON-L), remark COMB.

**4.6 A soft argument from boundedness of the dimensionless neutral gap.
Dead: no exclusion principle.** By row 1161 the gap follows from a count
bound and the unboundedness of z_+(L) = L m_+(L) over physical sizes. If
z_+ stayed bounded, a limit of rescaled boxes would be a scale-invariant
theory with levels proportional to 1/L. I know no theorem that excludes
such a limit for the Wilson trajectory; a free photon phase is compatible
with every monotone quantity I tried (a-theorem counting, positivity of the
pressure). ON FILE in kind: candidate 8 of row 1643 2.1.

**Remark SM (the ghost and matter propagators are submartingales; PROVED
here; it extends item B9 of `gap-afield-b-max.md` from one step to a
filtration; consumer: none).** Let H be a finite-dimensional Hilbert space,
V a real vector space, and M an affine map from V to the self-adjoint
operators on H. Let U be a bounded random element of V with m <= M(U) <=
Lambda almost surely, 0 < m <= Lambda. Let F_0 in F_1 in ... in F_J be a
filtration, U_j = E[U | F_j], M_j = M(U_j), G_j = M_j^(-1), D_j = M_(j+1) -
M_j. Then m <= M_j <= Lambda, and

    E[G_(j+1) - G_j | F_j] = G_j E[D_j G_(j+1) D_j | F_j] G_j
                           >= Lambda^(-1) G_j E[D_j^2 | F_j] G_j >= 0.

So G_j is a submartingale in the operator order, and with F_0 trivial and
U measurable for F_J,

    E[M(U)^(-1)] - M(E U)^(-1) = sum over j of E[G_j D_j G_(j+1) D_j G_j].

Proof. M is affine, so M_j = E[M(U) | F_j]; a conditional expectation keeps
the two operator bounds (test on a countable dense set of vectors). The
resolvent identity in its two orders gives G_(j+1) - G_j = - G_j D_j G_j +
G_j D_j G_(j+1) D_j G_j. G_j is measurable for F_j and E[D_j | F_j] = 0, so
the first term drops. D_j G_(j+1) D_j >= Lambda^(-1) D_j^2 because G_(j+1)
>= Lambda^(-1). Sum over j and take expectations. QED

Where it applies. The covariant Laplacian of a fundamental scalar plus a
mass is affine in the link quaternions, and the lattice Faddeev-Popov
operator is affine in the links on the Gribov region (B8, B9). The
increments are conditional variances of the link field in the shell that
F_(j+1) adds to F_j. For U(1) the Faddeev-Popov operator does not depend on
the field, so every increment is zero. Why it is not an input: the
enhancement of the ghost propagator has no consumer (Zwanziger's inequality
bounds the Wilson potential from above by the Coulomb potential, the wrong
direction; B9 says the same), and a lower bound on the shell variances by
Cramer-Rao meets 4.1 again. I did not test it against (g1) to (g6) beyond
this, because a fact with no consumer gets no test (row 1553 1.3).

## Stage 5. One external check

Two web searches on 2026-11-27 (general terms only; no file downloaded, no
preprint read): no posted method for the order-one band appeared. The
searches returned the two-dimensional texts that the lane already holds
(arXiv:2611.04908, arXiv:2611.01532, arXiv:2610.41256) and several
unrefereed self-published claims, which I did not open and do not assess.
This is a guide only; the lane's literature rows (1531, 1545, 1604, 1623,
1645) are the record.

## Labels

| Statement | Label |
|---|---|
| Stage 1 table | ON FILE at the anchors given; my own derivations of each line are ARGUED and were not written out |
| Stage 2, six points on the node W7 of row 1161 | a cross-provider reading: HOLDS at the level read; inputs (3), (4) used as stated |
| Stage 3 item 1 (exponent -3/2 and logarithm) | ARGUED here; PROVED ON FILE (row 1526 Theorem 3, check 1527) |
| Stage 3 item 3 (the rank pattern; D(x) and its factorization) | PROVED here (finite arithmetic, by hand); the statements are ON FILE (row 733) |
| Stage 3 items 4, 5 (Lemma HS; Proposition CL, Theorem S-w) | same-provider readings: HOLD |
| 4.1 remark on exact cancellation | ARGUED |
| 4.2 spin-wave bound on a pinned flat plane | ARGUED here (not written out); ON FILE in kind (Lemmas REM, EMB) |
| 4.4 sign for one plaquette | ARGUED |
| Remark SM | PROVED here; extends B9; no consumer |
| (PUR-io), (K-I), (K-II), (MON-L), (SING), (A1), (VIR-down), (HOT), the mass gap | OPEN |

Not done. No numeric run, no Lean. I did not read rows 1157, 1158, 1179,
1356, 1461, 1462, 1465 beyond what Stage 0 lists, so the chain from the
kappa-seed to the gap of the limit is not covered by Stage 2. I did not
read the two-dimensional preprints. I opened no file whose name begins
with `gap-newmath` other than this one.

Credits. Balaban. Sussman and Alpoge, with Claude and Codex as authors of
their text. The OpenAI authors of the two-dimensional texts; Ding, Huang
and Yang. Osterwalder and Seiler; 't Hooft; Tomboulis and Yaffe; Mack and
Petkova; Durhuus and Froehlich; Gribov; Zwanziger; Hamilton; Hansen and
Pedersen (operator Jensen). The lane's rows by gpt-6.2-astra,
gemini-4-neon, Claude Fable and Claude Opus, named at each use.

Provenance: Claude Fable 5.2 (claude-fable-5-2), max effort, laptop
subagent of the lead session; author only, checked by no one; hand
arguments only; nothing committed, pushed or posted; no other file written.

RESULT: Row 1655 (Claude Fable 5.2 max; author only, unchecked; no numeric run, no Lean). Outcome: NONE of (a) a proof of (PUR-io), (b) a proof of another input of a consumer on file, (c) a new consumer with its input, (d) a disproof of a reduction step or a new obstruction theorem. The mass gap is not proved and nothing is disproved.
Sixteen lines of attack were derived blind and then searched; every one is on file with its first failing step (Stage 1). Two blind re-derivations agree with on-file results: the fixed-lattice purity decay beta^(-3/2)/log beta (row 1526 Theorem 3) and the two facts on (KP) (row 733).
Readings: the three structural points of the explicit-aspect node W7 of row 1161 that row 1643 left untested HOLD on a cross-provider reading (six points, Stage 2); Lemma HS of row 1600 HOLDS on a same-provider reading, and I found no wrong line in Proposition CL and Theorem S-w of row 731.
PROVED here: Remark SM (for an affine positive operator-valued function of the links and any filtration, the inverse is an operator submartingale with increments G_j E[D_j G_(j+1) D_j] G_j; it extends B9 and has no consumer); the factorization D(x) = -(1-x)^2 (x^4 - 4x^3 + 8x + 7) for (KP) on independent planes.
ARGUED: a one-sided stiffness flow for a gauge field needs the tadpole cancelled exactly, since a variance bound that loses any fixed fraction fails beyond a fixed wavelength (4.1); this is why the two-dimensional engines, which have no tadpole, may lose a factor and a gauge port may not.
Open, unchanged: (PUR-io), (K-I), (K-II), (MON-L), (SING), (A1), (VIR-down), (HOT). I name no next band row: I found no first lemma with a method.
