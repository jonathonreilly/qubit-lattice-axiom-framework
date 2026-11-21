lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T17:12Z

# gap-mini-nphys-fable (queue row 1354)

Started 2026-11-21T05:12Z (date -u), Mac mini Claude worker 2, pinned at commit 33f734aed on branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim.

Item: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap in the sense of Jaffe and Witten, building on the neutral twist-averaged seed (N-phys) reduction of row 1342 (checked by row 1349) and rows 1341, 1345, 1348, 1351.

Labels used below: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Orientation

Written 2026-11-21T05:18Z (date -u). Read so far, statements only unless a proof is named:

- `GOAL.md` (whole); `FINISH.md` L1-84, L299-360 and the rows 1326, 1331, 1332, 1335, 1340-1354 (RESULT lines).
- `library/gap-seed-audit-fable.md` (row 1342, whole): (N-phys), its two-period form (T-N), Theorem O,
  Proposition C, the model ST_q. Check row 1349 read in the RESULT line only at this point.
- `parts/gap.md` L1-104 (state of attack) and L213-322 (route registry, test table, the exact price).
- This worker's notes on the three route-screening tables (rows 1189, 1194, 1199), on row 1200 and on the
  prior-identity list. They say: about 32 route families derived from scratch are on file already.

The target of this row, in the form this file uses (PROVED GIVEN on file, row 1342 Section 6, check row 1349):

**(T-N).** One admissible physical side L. For all late j (n_j = L/a_j, 4 | n_j, n_j >= 2^70) there is an
integer u_j with 3 <= u_j <= n_j/512 and Z_+(2u_j)/Z_+(u_j)^2 >= 2/3. Here Z_+(v) is the mean, over the eight
temporal twists, of the Wilson partition functions of the torus v x n_j^3 at the coupling beta_j. It equals
Tr(P_0 T^v), with P_0 the projection on the sector of zero electric flux.

What every earlier row found, in one sentence: a proof needs one selective step at a coupling of order one
(false for a massless factor), and no row has one. New inputs named by the queue row: the neutral target, the
rule that an exact computation checked in Lean is a proof step, the block maps and the end class of rows 1341,
1345, 1348, 1351.

Rule 0a for this row: row 1353 (queued in parallel, Mac mini worker 1) owns the statement "carry the Wilson
trajectory through mass-preserving block steps into the neutral end class of row 1351". Its output file is not
on disk at this pin. This row does not read it and chooses its own attack in Step 1.

## Step 1. How best to attack it (written 2026-11-21T06:08Z, date -u)

Also read for this step: row 1332 Sections 1 and 6 (`library/gap-shrink-box-fable.md`, Proposition CH); row 1351
(`library/gap-blockstep4-astra62.md`) L5-47, L75-136, L196-228, L304-355; the headings of row 1345
(`library/gap-blockstep2-astra62.md`). Check row 1352 of row 1351 is not on disk at this pin.

**1.1 What the target says (GUIDE; the thermal reading is on file: `gap-crux-skeleton-max.md` L82,
`gap-constraints-max.md` L81, rows 720 and 1180).** Z_+(v) = Tr(P_0 T^v), and Z_+(2u)/Z_+(u)^2 is the purity of
the neutral thermal state at the inverse temperature u. (T-N) says that the box n^3 holds less than about one
half of a thermal excitation at the temperature 512/L. So (T-N) is a statement at a size of about 10^4
correlation lengths. No small box and no perturbative computation contains it.

**1.2 The architecture that is left (ARGUED; it agrees with row 1332 6.3 and row 1351 "Outstanding block
induction").** A proof of (T-N) for all late j has three parts. (i) A carry from the bare lattice through the
range of small effective coupling. This is the account's renormalization, and it stops at the first passage.
(ii) A fixed number of steps at an effective coupling of order one. (iii) An end class with a hand proof of the
two-period bound. A finite computation can enter only in (ii), and only as an inequality inside a theorem about
a class of measures. I found no way around this structure, and no step of kind (ii). This row does not solve
the problem.

**1.3 What this row does instead.** It tests the one new object that the queue names as a candidate landing
place: the neutral end class of row 1351. The test asks which of the two alternatives of row 1161 (9) the class
forces on a measure that lands in it. The answer (Step 2) changes what steps (ii) and (iii) must aim at.

## Step 2. The neutral end class of row 1351 forces alternative II (written 2026-11-21T06:10Z, date -u)

**Rule 0a.** Searched before writing: `grep -i` for "branch", "alternative II", "deconfin", "twist ratio",
"near 8" in `library/gap-blockstep4-astra62.md`, `gap-blockstep2-astra62.md`, `gap-blockstep2-check-opus.md`,
`gap-seed-audit-check-astra.md`; `library/open-core.md` has no line on the end class. Row 1351's file names the
branch only twice, both times to say that the periodic seed would need branch information in addition. It does
not say which alternative its own end class forces. Nearest statements on file: the two alternatives, row 1161
(9); frozen and finite Z_2 as a model with the neutral seed in alternative II, check 1349 L76-80; row 1345
L105 and L190 (the periodic mass needs the sector fraction pi_0). Credit: G. 't Hooft for the electric flux
free energy; G. Mack and V. Petkova for the centre split; gpt-6.2-astra for rows 1345 and 1351, whose
expansion is used below.

**2.1 Setting (from row 1351 (7), (10), (11); author-labelled PROVED there, check row 1352 not on file).**
Coarse torus T_t = (t, m, m, m), v = t m^3 sites, min(t, m) >= 16, j_0 = floor(min(t, m)/8). Independent link
variables x with a product reference law. Each plaquette p has a scalar a_p > 0 and two functions of its four
links, 1 + h_p(x) > 0 and v_p(x) > 0, with (10): ||h_p||_6 <= 1/4096 and ||v_p||_6 <= 1/40. A closed
two-cochain z with values in F_2 has the weight prod over p of a_p (1 + h_p) if z_p = 0 and a_p v_p if z_p = 1.
H^2(T_t; F_2) has 64 classes. For a class c put

    M_c = sum over closed F with [F] = c of E[ prod_{p in F} v_p  prod_{p not in F} (1 + h_p) ]  >= 0.

The neutral mass of row 1351 is the sum of M_c over the eight classes with zero spatial periods, times scalars.

**2.2 Lemma B0 (all 64 characters; PROVED GIVEN row 1351's proof of (11), L124-136).** For a character omega
of H^2(T_t; F_2) put Q^omega = sum over c of omega(c) M_c. There is a real number Lambda such that for all 64
characters Q^omega > 0 and

    | log Q^omega - Lambda | <= tau,      tau = (12 v / 256) 2^(-j_0).

Proof. Row 1351 proves this for the eight characters chi that are trivial on the temporal periods. Its proof
uses four properties of the factor chi([F]): it has modulus one; it is real; it is multiplicative over
disjoint closed pieces; it equals one on every closed F inside a box of radius at most j_0. The first three
hold for every character of an F_2 group. The fourth holds for all six periods, because j_0 is at most
min(t, m)/8, so such a box does not wrap in any of the four directions and a closed cochain inside it is
exact. So the bound (12) of row 1351, the deletion induction (|log Q^omega_T(s)| <= 6v/256 on |s| <= 2), the
equality of the coefficients of degree below j_0, the Cauchy tail (12 v/256) 2^(-j_0) at s = 1 and the
positivity of Q^omega(1) hold with omega in place of chi, word for word. Lambda is the common truncated
logarithm. QED

I read L124-136 and checked that each step is indifferent to the character. I did not re-derive the constants
41, 5^(k-1) and (12) of row 1351.

**2.3 Proposition B (the coherent class has one heavy class; PROVED GIVEN Lemma B0).** In the setting of 2.1,
for every class c != 0:

    M_c <= delta M_0,      delta = e^tau (e^tau - 1).

Proof. By Fourier inversion on F_2^6, M_c = (1/64) sum over omega of omega(c) Q^omega. For c != 0 the sum of
omega(c) over omega is zero, so M_c = (1/64) sum of omega(c) (Q^omega - e^Lambda), and
|Q^omega - e^Lambda| <= e^Lambda (e^tau - 1). For c = 0, M_0 = (1/64) sum of Q^omega >= e^(Lambda - tau). QED

Size: with t = floor(m/512), tau is below 1/100 for m above about 3 x 10^5 (GUIDE arithmetic: v = m^4/512,
j_0 about m/4096). So delta tends to zero on the large common coarse cubes where row 1351 uses (11).

**2.4 Corollary B1 (what landing in the class proves about Wilson; PROVED GIVEN Proposition B).** Let
T_u = (u, n, n, n) be a fine torus with the Wilson transfer operator T of the box n^3, and Z^h(T_u) the
partition function with the temporal twist h in F_2^3. Assume a twist-wise exact representation in the class:
there are a model of 2.1 on some T_t and one K > 0 with Z^h(T_u) = K M_{c(h)} for all eight h, where c(h) is
the class with temporal periods h and zero spatial periods. Then:

- (a) Z^h(T_u) <= delta Z^0(T_u) for h != 0;
- (b) for each electric class e, the sector trace Tr_e T^u = (1/8) sum over h of (-1)^(h.e) Z^h lies between
  (1 - 7 delta)/8 and (1 + 7 delta)/8 times Z^0. So the electric flux free energies of 't Hooft,
  F_e = - log(Tr_e T^u / Tr_0 T^u), obey |F_e| <= log((1 + 7 delta)/(1 - 7 delta));
- (c) the periodic thermal sum obeys S_per(u) >= 8/(1 + 7 delta) - 1, and
  Z^0(T_u)^2 / Z^0(T_2u) >= 8 (1 + 7 delta)^(-2) Z_+(T_u)^2 / Z_+(T_2u) >= 8 (1 + 7 delta)^(-2).

So the periodic two-period test fails at this torus by a factor near 8, and the torus is in alternative II of
row 1161 (9): the neutral sector passes, and the seven flux sectors weigh as much as the neutral one.

Proof. (a) is Proposition B. (b) is the inverse of Z^h = sum over e of (-1)^(h.e) Tr_e T^u. (c): the vacuum is
neutral, so lambda_0^u <= Tr_0 T^u = Z_+(T_u) <= (1 + 7 delta) Z^0/8, and 1 + S_per(u) = Z^0/lambda_0^u. For
the ratio use Z^0(T_u) >= 8 Z_+(T_u)/(1 + 7 delta), Z^0(T_2u) <= 8 Z_+(T_2u) and Z_+(T_2u) <= Z_+(T_u)^2. QED

**2.5 The exact Wilson step has this form (READ in row 1345 (1)-(3) and row 1351 L26; not re-derived).** Row
1345 writes the Wilson mass as the integral over a(dy) of the mean over fair link signs s of
exp(sum_p J_p(y) (ds)_p), and its block step keeps this form on the coarse lattice. A temporal twist h changes
the sign of the plaquettes of three stacks, which are lifted to coarse packets. So for each h the twisted
mass is the same integral with (ds)_P replaced by (-1)^((Sh)_P) (ds)_P, with the same a and the same J. In
additive notation z = d xi + S h runs over one class of closed cochains with zero spatial periods, and all
classes have the same number of preimages. So every representation that these maps produce is twist-wise
exact with one K, and Corollary B1 applies to it as soon as its weights satisfy (10).

**2.6 What follows for the chain (the rigorous part is 2.4; the physics is GUIDE).**

1. (PROVED GIVEN 2.4 and 2.5.) Carrying the Wilson trajectory by the maps of rows 1345 and 1351 into the end
   class (10), at the torus of (N-phys), proves more than (N-phys). It proves that the electric flux free
   energies vanish at that torus, at every late cutoff. This is the statement that the theory does not
   confine at the temperature 512/L in a box of side L. It also proves that (PS) fails there.
2. (GUIDE.) For SU(2) the belief is the opposite. At a torus where the neutral seed holds, the time side is
   above about 21 correlation lengths, which is about four times the inverse deconfinement temperature
   (m/T_c about 5.3, `gap-hcrate-read-opus.md` L156), and F_e is of order sigma times the area n u a^2, a
   number above 10^4. Below the deconfinement temperature the flux sectors are heavy; above it the neutral
   sector is a hot plasma and has no seed. So no scale is expected at which Wilson SU(2) has both the neutral
   seed and alternative II. No checked statement on file excludes alternative II for Wilson (row 1342 5.3).
3. (ARGUED from 1 and 2.) The end class (10), and the stable form (23)-(24) built on it, is the landing class
   of a theory with a gapped neutral sector and deconfined centre flux, such as Z_2 gauge theory at large
   coupling. It is not the landing class of a confining theory. The step that row 1351 leaves open, and that
   the queue gives to row 1353 with this class as its candidate, is then expected to be false for Wilson
   SU(2) as long as the maps are twist-wise exact. The stable form inherits Lemma B0 (2.7 below).
4. (PROVED, elementary; "confining at the torus" means alternative I there: Tr_e T^u is small against
   Tr_0 T^u for every e != 0.) Then every Z^h, a signed sum of the eight sector traces, is within a factor
   close to one of Tr_0 T^u. So a class in which such a theory lands by a twist-wise exact map must have all
   eight class masses M_{c(h)} nearly equal. Z_+ and Z^0 agree up to that factor at both periods, and the
   neutral two-period bound and the periodic one are the same statement up to that factor.
   So for a confining theory the neutral target does not open a landing class that the periodic target
   lacks. The landing class is centre-disordered. The one such class with an end theorem on file is the
   strong-coupling class (row 785 Theorem DOB, row 701).

What this step does not show: that Wilson SU(2) confines (that is the belief used in item 2); that no map
outside the twist-wise exact kind can reach the class (a map that preserves only the mean over the twists is
not covered).

**2.7 The stable class (23)-(24) (added 2026-11-21T06:15Z, date -u; PROVED GIVEN row 1351's proof of (24), L321-330).**
Row 1351's proof of (24) is the expansion of (11) with window factors. Its text uses the same four properties
of the character: "Closure and coefficients, including a character of the three periods, factor on distinct
components", and a connected term of degree below j_0 "fits in a lifted box". A window factor reads the
curvature only inside its own component. The windows have length at most half the period, so the lifted box
does not wrap in time. So Lemma B0 holds in the class (23) for all 64 characters with
tau' = 2 v e^(-theta j_0) in place of tau, and Proposition B and Corollary B1 hold with
delta' = e^tau' (e^tau' - 1). I read L321-336 for this and did not re-derive the constants.

## Step 3. The dual class: where a confining theory can land (written 2026-11-21T06:15Z, date -u)

**3.1 Statement.** Keep the setting of 2.1, with one change of the hypothesis. Write the two plaquette weights
as a_p (alpha_p(x) + beta_p(x) (-1)^(z_p)), that is alpha_p = (w_p(0) + w_p(1))/(2 a_p) and
beta_p = (w_p(0) - w_p(1))/(2 a_p). Assume, under the product reference, on every plaquette

    (10*)    || alpha_p - 1 ||_6 <= 1/4096,      || beta_p ||_6 <= 1/40.

In the exact Wilson form of 2.5, alpha_p = cosh J_p / a_p and beta_p = sinh J_p / a_p. So (10*) says that the
centre couplings J_p(y) are small, where (10) says that they are large and positive.

**Theorem E (PROVED GIVEN row 1351's proof of (11), L124-136, read with primal surfaces).** In the class
(10*) on T_t = (t, m, m, m), min(t, m) >= 16, with tau = (12 v/256) 2^(-j_0):

- (a) the eight twisted masses Z^h (the masses of the eight classes with zero spatial periods) are positive
  and lie within the factor e^(2 tau) of each other;
- (b) the neutral mass and the periodic mass Z^0 both obey the two-period bound of (11):
  |2 log Z(T_t) - log Z(T_2t)| <= (48 v/256) 2^(-j_0), for Z = Z_+ and for Z = Z^0;
- (c) so a model with a twist-wise exact representation in the class is in alternative I: for e != 0 the
  sector trace Tr_e T^u is at most e^tau (e^tau - 1) times Tr_0 T^u.

Proof. Fourier transform on F_2. Let V be the space of closed cochains with zero spatial periods,
V = d C^1 + span(S_1, S_2, S_3), with S_i the three temporal stacks. For fixed x,

    2^(-dim V) sum over z in V of prod_p (alpha_p + beta_p (-1)^(z_p))
        = sum over S in V-perp of prod_{p in S} beta_p prod_{p not in S} alpha_p,

because the sum over z in V of (-1)^(<S, z>) is |V| if S is orthogonal to V and zero if not. Here S runs
over sets of plaquettes. S is orthogonal to d C^1 exactly when its boundary is zero (every link lies in an
even number of plaquettes of S). A cycle S is orthogonal to S_i exactly when its homology class has no
component on the two-torus of the plane (0, i). For one fixed twist h the same computation on the coset
d C^1 + S h gives the sum over all cycles S of chi_h([S]) times the same product, where chi_h is the
character of H_2(T_t; F_2) that pairs with the class c(h).

Now write alpha_p = 1 + h_p and expand the factors alpha_p outside S on sets X disjoint from S. The
coefficient of a pair (S, X) is E[prod_S beta_p prod_X h_p]. This is the expansion of row 1351 with the
closed dual surface F replaced by the primal cycle S, v_p by beta_p, and the character of the periods of F
by a character of the homology class of S. Each step of row 1351's proof holds for it. The Hoelder bound
u^|S| eps^|X| uses only that a link is read by at most six plaquette functions; beta_p may have either sign,
and the bounds are absolute. A minimal nonempty cycle through a plaquette has at most 5^(k-1) forms at area
k, because a link lies in six plaquettes; it has area at least 6 by the same projection argument (the
lattice of primal plaquettes and links is the dual picture of the lattice of dual plaquettes and
three-cubes). Components joined by a common link or a common three-cube have independent reads and separate
closure equations. A cycle inside a box that does not wrap is a boundary, so every character is one on it.
The time cover doubles the coefficients of degree below j_0. Each sum is real and positive at s = 1.
So Lemma B0 holds here for all 64 characters omega of H_2: |log Q^omega - Lambda| <= tau.

(a) Z^h is the scalar prod a_p times Q^(chi_h). (b) Z^0 is the case h = 0, and Z_+ is the mean of the eight;
the two-period bound for each is the last paragraph of row 1351's proof of (11). (c) Tr_e T^u is the mean
over h of (-1)^(h.e) Z^h, and for e != 0 the common part e^Lambda cancels, as in Proposition B. QED

I did not re-derive row 1351's constants. Theorem E has the same standing as (11): it rests on that proof,
whose check (row 1352) is not on file at this pin.

**3.2 Reading (ARGUED).**

1. (10) and (10*) are the two sides of 't Hooft's alternative in one framework. In (10) the centre curvature
   is ordered, the closed surfaces of the expansion are the rare frustrated ones, every nonzero class is
   suppressed (Proposition B), the periodic test fails and the neutral test passes. In (10*) the centre
   curvature is disordered, the surfaces are those of the strong-coupling expansion, all classes weigh the
   same, and the periodic and the neutral tests pass together.
2. Plain Wilson is in (10*) for small beta: there alpha_p = cosh(beta q) and beta_p = sinh(beta q) with
   |q| <= 1, so (10*) holds for beta <= 1/46 (cosh(1/46) - 1 < 1/4096, sinh(1/46) < 1/40). This is inside
   the range of the strong-coupling seeds already on file (row 785, 9 beta/2 < 1), so it adds no range.
3. In the representation of row 1345 the Wilson trajectory at a late cutoff is in neither class. By row 1345
   (3), J_P (dt)_P is beta times the sum of the B^2 plaquette traces of the packet, which is of order
   B^2 beta, so (10*) fails; and the sign of J_P(y) alone is not coherent under the reference, so (10) fails
   (row 1351 L142-146). The centre signs carry no free energy of their own there. Everything is in the
   angular environment, which no step on file integrates at an effective coupling of order one.

## Step 4. Consequences, a rigorous instance, and one guide check (written 2026-11-21T06:21Z, date -u)

**4.1 Remark R (one-sided transport is enough; PROVED, elementary).** Corollary B1 needs less than equality.
Assume Z^h(T_u) <= K M_{c(h)} for h != 0 and Z^0(T_u) >= K M_0/(1 + eps_0). Then Z^h <= delta (1 + eps_0) Z^0,
and (b), (c) of Corollary B1 hold with delta (1 + eps_0) in place of delta. This covers the positive
enlargement of row 1351 (8) (READ at L88-93, not re-derived): there the mass with the temporal twist h is
Y^h = Z^h + sum over nonzero cosets of lambda^(t k) Z^(b, h), with 0 <= Z^(b, h) <= Z^0, so Z^h <= Y^h and
Y^0 <= (1 + eps_0) Z^0 with eps_0 = (1 + lambda^t)^(N+3) - 1.

**4.2 Corollary B2 (a rigorous instance; PROVED GIVEN Proposition B and Theorem E).** Let beta <= 1/46, and
let the fine torus have all sides at least 16, with its own tau. The Wilson model has no twist-wise exact
representation in the class (10) on a coarse torus whose delta is below e^(-2 tau). Reason: by 3.2 item 2
and Theorem E (a) its twisted masses agree within e^(2 tau); by Proposition B a representation in (10)
would make them differ by the factor delta. The same
holds at every coupling and torus where the periodic thermal sum S_per(u) is below 6 and delta is below
1/49, by Corollary B1 (c) (then 8/(1 + 7 delta) - 1 > 6). So at a coupling with a periodic seed at some size,
the class (10) is closed to twist-wise exact maps on every larger torus on which the engine keeps S_per
small (rows 697, 705, 731; for the shape u = n/512 see check 1349 L80). The periodic programme of rows 1323
to 1339 and a landing in (10) exclude each other.

Published context (recalled, not re-read, unchecked): alternative I is a theorem for Wilson SU(2) at small
beta (Osterwalder and Seiler, area law). Alternative II in the form of a non-decaying Polyakov-loop
correlation is a theorem at high temperature, beta above a multiple of the time extent (Borgs and Seiler,
CMP 91, 1983). Neither covers the seed torus of the trajectory, where the time extent grows like a power of
e^beta.

**4.3 What a twist-wise exact chain proves (ARGUED from 2.4, 3.1 and 4.2).** The eight twisted masses at the
two periods are invariants of such a chain. An end class with a hand proof must give the neutral two-period
bound for every member. The two classes with such a proof, (10) of row 1351 and (10*) of this file, each fix the alternative:
II and I. So a chain of this kind cannot prove (N-phys) and leave the branch open. For a confining theory
it must land in a class of the kind (10*), and then it proves the periodic bound as well. The neutral target
of row 1342 remains correct as logic: the gap clause needs (N-phys) only. It does not make the landing easier.

**4.4 The same end theorem, the other variable (ARGUED).** Row 1351's end theorem is the right theorem for a
confining theory when it is applied to the Fourier-dual centre variable. In words: the object that must be
rare on the coarse lattice is the electric centre sheet (the cycle S of 3.1, the surface of the
strong-coupling expansion), not the frustrated magnetic surface F. The weight of a sheet is the product of
beta_p = sinh J_p / a_p. In row 1345's representation |tanh J_P| is close to one at every late cutoff, so the
sheets are not rare pointwise. They can be rare only after the angular environment is integrated, by
cancellation of the signs of sinh J_P. Row 1351's proof uses the hypothesis (10) only through the moment
bound |E[prod_F v_p prod_X h_p]| <= u^|F| eps^|X| and the independence of distant reads. So a class defined
by that moment bound for the pairs (S, X), in place of the norm bound (10*), has the same end theorem and
admits signed weights (ARGUED; I did not write this variant out). This matches the lesson of method 35 in
`parts/gap.md`: a proof must cancel before it bounds.

**4.5 Guide check (exact, small, no proof step).** The identity at the start of the proof of Theorem E was
checked with exact fractions on the three-dimensional torus 2 x 2 x 2 (24 plaquettes, dim d C^1 = 14, two
stacks, dim V = 16, random rational alpha_p in [0.5, 1.5] and beta_p in [-0.45, 0.45]): both sides agree for
V, and for each of the four cosets with the character. One run of seconds under the numeric lock (memory free
68 percent at the start); the script is a scratch file outside the repository.

**4.6 For the lead (proposals; no file other than this one was edited).**

1. Tell row 1353: by Corollary B1 a landing in the class of row 1351 is a proof of alternative II at the seed
   torus, which the belief in confinement excludes; the candidate with the opposite alternative is (10*) of
   3.1, with the same proof.
2. A check of Lemma B0 needs only row 1351 L124-136 and L321-330: confirm that each step is indifferent to
   the character, for all six periods. Theorem E needs the same lines read with links in place of
   three-cubes.

## Step 5. The soft stratified model: the open item of row 1342 (written 2026-11-21T06:26Z, date -u)

Why here. Step 4.3 says the neutral target does not ease the landing. The other way to ease the target is
to drop the count and keep a gap only. Row 1342 showed with ST_q that this is wrong in the class of Theorem
S, and left open whether a strictly positive kernel repairs it ("a soft version", its 4.5; check 1349 lists
it as OPEN). This step answers that item for the natural soft model. Rule 0a: `grep -i` for "soft version",
"order by disorder", "unpaired" in `library/*.md` finds only row 1342 and its check.

**5.1 The model.** SST_q(eps), 0 < eps < 1: q-state spins on the sites of a four-dimensional torus, weight
eps^(U(sigma)), where U is the number of plaquettes that are not paired (row 1342 4.1). At eps = 0 it is
ST_q. The weight is a product over plaquettes of a strictly positive function of four spins. The model is
local and hypercubic.

**Lemma SST0 (reflection positivity; PROVED).** SST_q(eps) is reflection positive at mirrors through sites
and at mirrors that bisect links.
Proof. Site mirror: every plaquette lies on one closed side, so the weight is a product F(left) F(right)
with the mirror spins shared (the positive weight of a plaquette inside the mirror is split into two square
roots). Link mirror, in the direction mu: a crossing plaquette has the corners a, c
on the left and b, d on the right, with the mu-bonds (a, b) and (c, d). Its weight is
eps + (1 - eps) 1[paired], and
1[paired] = 1[a = c] 1[b = d] + sum over k != l of 1[a = k, c = l] 1[b = k, d = l].
(The first term is the case that both nu-bonds are satisfied. The second is the case that both mu-bonds are
satisfied and the nu-bonds are not; the two cases are disjoint.) Each term is a function of the left pair
times the same function of the mirrored right pair, with a positive coefficient. Products of such sums are
again such sums. QED

So the transfer matrix of a box is symmetric, entrywise positive and positive semi-definite, and the model
has every property of the class of Theorem S that row 1342 4.4 (a) lists, with a strictly positive kernel.

**Lemma SST1 (the cheapest excitations; (a) to (d) PROVED by counting; the enumeration of 5.3 agrees).**
Take a stratified ground state sigma(x) = xi(x_mu) and change the spins on a set R of sites. The cost is the
number of plaquettes that are no longer paired.

- (a) A plaquette with exactly one changed corner is not paired. So one changed site costs 24, in every
  ground state and for each of the q - 1 new values.
- (b) Two changed sites at the ends of a bond cost 36 if the two sites had equal spins before and get equal
  spins after, and 42 if not. (They share six plaquettes. In the first case each of the six has its two
  bonds parallel to the pair satisfied before and after.)
- (c) The two sites of a bond in a direction nu != mu always had equal spins. The two sites of a bond in the
  direction mu had equal spins exactly when the two layers are equal.
- (d) Let R not wrap the torus. Then the cost is at least 4 times the sum, over the six plane orientations,
  of the number of planes of that orientation that meet R. So a set R of cost at most 41 is one site, or two
  sites on one coordinate line; and then it is one site (24) or a pair of (b) with cost 36.
- (e) (Enumeration only, q = 3, side 4.) Two changed sites on a diagonal of a plaquette cost 46 or 47. Three
  changed sites that are connected through plaquettes cost at least 48. A straight line of k equal changes
  costs 12 k + 12, a 2 x 2 square 52, a 2^4 block 96 (hand counts in the constant ground state).

Proof of (a). Let the plaquette be paired through its nu-bonds, and change the corner x to a. The nu-bond at
x is now unsatisfied. For the mu-bonds to be satisfied, a must equal the spin at x + mu, and the opposite
mu-bond must be satisfied; with the old nu-bonds this gives old(x) = old(x + mu) = a, against a != old(x).
(b) and (c) are direct.
(d) Take a plane that meets R, and in it the site x of R that is lowest in the second coordinate and, among
those, lowest in the first. The plaquette of this plane with x as its upper right corner has no other corner
in R, so it is not paired, by (a). The three other extreme sites give three more plaquettes, with the site
of R at a different corner each time. Different planes give different plaquettes. If R has two values of a
coordinate kappa, the three orientations that do not contain kappa have at least two planes each, so the cost
is at least 4 (3 . 2 + 3) = 36. If R has two values in each of two coordinates, five orientations have at
least two planes, and the cost is at least 44. If R lies on a line and has k sites, the cost is at least
12 k + 12, which is 48 for k = 3. Two sites of a line that are not neighbours share no plaquette and cost
48. QED

**5.2 Reading (ARGUED: a low-temperature expansion around each ground state, not written as a proof; the
ground states are infinitely degenerate at eps = 0, so a proof needs a restricted-ensemble argument that I
did not write).**

1. By Lemma SST1 (d), through the order eps^41 the only excitations are single sites, with the same count in
   every ground state, and the pairs of (b), (c) with cost 36. So an interface of cross-section A between
   two adjacent layers carries the factor exp(K A) if the layers are equal and 1 if not, with
   K = (q - 1) eps^36 + O(eps^42). Equal layers are favoured. This is order by disorder.
2. So the entropy of the layer patterns does not survive. Row 1342 4.5 argued that the balance of its (c)
   "would persist whenever that entropy is positive"; in SST_q the entropy is lifted at the order eps^36.
3. Two ranges of the side n. For K n^3 well below one the model behaves like ST_q: the vacuum branch has the
   eigenvalue ratio about q over each of the about q^n static layer patterns of each space direction, so
   the gap is about log q and no shape with a space side longer than the time has a seed. For K n^3 well
   above one the q constant states dominate and are degenerate up to exp(- K n^3): the full transfer matrix
   has no uniform gap, and the sector invariant under the permutations of the q values has a seed.
4. Consequences. (i) SST_q is not a strictly positive counterexample to "a uniform gap on all cubes gives a
   seed": it loses the premise at large sides. That statement stays OPEN for strictly positive kernels, as
   row 1342 left it. (ii) No theorem of the class can give a seed from a gap with a size that depends on
   the gap alone: with the gap near log q the first seed size of SST_q is of the order eps^(-12). A size
   bound must depend on the positivity constant of the kernel. (iii) For Wilson the positivity constant of
   one plaquette is e^(-2 beta), so a bound of this kind could not hold the seed size fixed in physical
   units, where the side grows like e^(2.69 beta) (one loop). This agrees with Proposition LS of row 1234:
   the bounded seed size is a separate clause.

**5.3 Guide run (exact, small, no proof step).** On the torus 4^4 with q = 3, all sets of at most three
changed sites that contain a fixed site and are connected through plaquettes, with all new values, in three
ground states (constant; layers 0,1,2,1; layers 0,0,1,2). Lowest costs and the number of rooted
configurations: size one 24 (2, 2, 2); size two 36 (16, 12, 14), then 42 (16, 20, 18), then 47 or 46; size
three 48 (24, 18, 18). The counts 16, 12, 14 are 2 (q - 1) times the number of directions with an equal
neighbour: 8, 6, 7. One run of seconds under the numeric lock (memory free 66 percent); scratch file
outside the repository.

## Step 6. The first failing step, three ways (written 2026-11-21T06:29Z, date -u)

**6.1 The step, as one statement (OPEN).** (BS*) There are a block side B, a coupling above the hand range,
and a twist-wise exact representation of the Wilson masses of the tori (Bt, Bm, Bm, Bm) and (2Bt, Bm, Bm, Bm)
as the masses of one model on the coarse tori whose electric sheets are rare: a model of 3.1, or of its
moment form (4.4), with the common-cover rule of row 1351. By Theorem E this gives the periodic and the
neutral two-period bounds at that coupling. The statement for the trajectory needs (BS*) for every late
cutoff with one margin, at one physical coarse mesh. This is the block step of row 1332 6.5 with the end
class corrected by Steps 2 and 3. Rows 1340, 1341, 1345, 1348 and 1351 attacked it and left it open.

**6.2 Three ways tried here, and where each stops.**

1. *Centre signs alone (the map of row 1345, read in the dual variable).* The coarse sheet weight is the
   integral over the environment of prod cosh J'_P times prod over the sheet of tanh J'_P, and by Fourier
   inversion it is 2^(-P') times the sum over the sign patterns tau' of the coarse packets of
   (prod_{S'} tau') Z_(tau'), with Z_(tau') > 0 the Wilson mass with signed packets (row 1345 L73). (PROVED,
   elementary; the same computation as in Theorem E.) So rare sheets mean that the mass is nearly
   independent of the packet signs. For closed patterns this is exact. For patterns with coarse centre
   monopoles it is the vanishing of a thick-monopole free energy at the scale B. Classically that free
   energy is of order beta and does not depend on B (the action is scale invariant in four dimensions), so
   no bound comes from the action; it is a statement about the measure at the scale B. And this half
   controls the flux sectors only: the two-period defect of the untwisted mass Z^0, which is the neutral
   content, is not touched by any centre computation. Stops at: the integral over the angular environment.
2. *Positive bounds on the unblocked sheets.* For free links the chessboard norm of sinh(beta q) is
   2 I_2(beta)/beta and that of cosh(beta q) is 2 I_1(beta)/beta (ARGUED: the product over all plaquettes
   of one orientation is a product of two-dimensional torus sums, whose leading coefficients are these).
   So a sheet costs at most t(beta) = I_2(beta)/I_1(beta) per plaquette, for every beta, and this is sharp
   for simple surfaces. The expansion then converges while t times the surface entropy is below one. With
   the count of five continuations at a link this is t < 1/5, beta below about 0.8, the order of the
   ceilings already on file (`parts/gap.md` test table: 1/3, 2/3, 0.775, 1.0109; I did not check which
   family each ceiling belongs to). At beta = 2.3, t is 0.48. A bound in absolute value cannot do better, since simple sheets have exactly this
   weight; the true string tension is far below -log t there because of signed terms. Stops at: the
   lesson of method 35.
3. *Integrate one colour, then test (row 1351's strip elimination).* The elimination is exact and its tail
   is summable. Along the trajectory it is uniform in the cutoff because the one-step ratio is
   R = e^(2 beta) and the one-loop slope beta/log n = 11/(3 pi^2) = 0.3715 is below 1/2 (row 1351 L212). For
   the next colour the generated factors add an oscillation of order 2 beta for each of the four plaquettes
   that the link shares with eliminated columns, so the worst-case ratio is of order e^(10 beta), and
   10 x 0.3715 is above one. (GUIDE arithmetic; row 1351 states the obstruction without the number.) A
   bound in the law of the model is needed from the second colour on. Stops at: the same place as rows
   1340 and 1351.

**6.3 What a finite computation could certify (ARGUED).** Nothing found in this row. After Steps 2 to 4 the
hypothesis of a block-step theorem is a bound on signed coarse sheet moments after the angular integration,
at a block side of several correlation lengths (GUIDE: sigma B^2 above about 3.7 for the constant 1/40 of
(10*), that is B about 6 at beta = 2.3). That is an integral over a block of about 6^4 sites. Row 1341's
enclosure covers eight links.

## Step 7. Summary

**Solved?** No. The mass gap is not proved. (N-phys) is not proved. No step of the chain is disproved.

**PROVED here, given row 1351's expansion (author-labelled PROVED by gpt-6.2-astra; its check, row 1352, was
not on file at this pin; I verified only that each step is indifferent to the character, not the constants).**

- Lemma B0, Proposition B, 2.7: in the neutral end class (10) of row 1351, and in its stable form (23)-(24),
  every nonzero class of centre curvature has relative mass at most e^tau (e^tau - 1).
- Corollary B1, Remark R: a twist-wise exact carry of Wilson into that class gives vanishing electric flux
  free energies and S_per(u) >= 8/(1 + 7 delta) - 1 at that torus. The class is an alternative-II class.
- Theorem E: the Fourier-dual class (10*) has the same end theorem with the surfaces of the strong-coupling
  expansion; there all twisted masses agree, and the periodic and neutral two-period bounds hold together.
- Corollary B2: Wilson at beta <= 1/46, and at any coupling and torus with S_per below 6, has no twist-wise
  exact representation in (10).

**PROVED here, elementary.** Lemma SST0 (the soft stratified model is reflection positive, with a strictly
positive kernel). Lemma SST1 (its excitations of cost at most 41 are single sites, cost 24, and pairs with
equal spins before and after, cost 36).

**ARGUED here.** 2.6 and 4.3: for a confining theory the neutral target opens no landing class that the
periodic target lacks; the candidate of rows 1351 and 1353 is expected to be unreachable for Wilson SU(2).
4.4: the end theorem holds in a moment form that admits signed weights. 5.2: the soft stratified model
orders by disorder at the order eps^36; it behaves like ST_q below a side of the order eps^(-12) and loses
the uniform gap above it, so it is not a strictly positive counterexample, and a seed size cannot be bounded
by the gap alone.

**GUIDE.** The belief that Wilson SU(2) is in alternative I at every torus where the neutral seed holds; the
sizes in 2.3, 2.6 and 6.3; two exact enumerations of seconds each (4.5, 5.3).

**OPEN.** (BS*) of 6.1 at any coupling above the hand range; its form uniform in the cutoff; the base of the
chain with numbers; whether alternative II can be excluded for Wilson by proof; "a uniform gap on all cubes
gives a seed" for strictly positive kernels; (N-phys); the mass gap.

**Not done.** I did not read the output of row 1353 or the check of row 1351. I did not re-derive row 1351's
constants. I did not search origin/main or the open PR branches (this checkout has no such refs). I read no
published paper; the two cited theorems of 4.2 are recalled.

RESULT: Row 1354 (Claude Fable 5.2 max, Mac mini worker 2; author only, checked by no one; two exact guide enumerations of seconds each under the numeric lock, no large computation). NOT solved: the mass gap and (N-phys) are not proved, and no finite computation is specified. Main finding, PROVED GIVEN row 1351's expansion (unchecked at this pin): the neutral end class (10) of row 1351, and its stable form (23)-(24), is an alternative-II class. Every nonzero class of centre curvature has relative mass at most e^tau (e^tau - 1) (Lemma B0 for all 64 characters, Proposition B), so a twist-wise exact carry of Wilson into it makes the eight twisted masses unequal by that factor, the electric flux free energies vanish, and the periodic thermal sum is at least 8/(1 + 7 delta) - 1 at that torus (Corollary B1, Remark R). The maps of rows 1345 and 1351 are twist-wise exact (read, not re-derived). So the landing that row 1351 leaves open, and that row 1353 has as its candidate, would prove that SU(2) does not confine at the seed torus; it is excluded at beta <= 1/46 and wherever a periodic seed holds (Corollary B2), and is expected false on the trajectory (GUIDE: confinement). Theorem E: the Fourier-dual class (10*) (small centre couplings; the closed surfaces are the electric sheets of the strong-coupling expansion) has the same end theorem by the same proof, with all twisted masses equal and the periodic and neutral two-period bounds together. ARGUED: for a confining theory the neutral target opens no landing class that the periodic one lacks; the object that must be rare on the coarse lattice is the electric sheet, and its weight is a Fourier coefficient of the positive signed-packet masses. Also: Lemma SST0 and SST1 (PROVED) and their reading (ARGUED) answer the open item of row 1342: the soft stratified model is reflection positive with a strictly positive kernel, orders by disorder at order eps^36, behaves like ST_q below a side of order eps^(-12) and loses the uniform gap above it, so it is not a strictly positive counterexample. First failing step, three ways (6.2): one block step at a coupling above the hand range into a class of the kind (10*). OPEN: that step, its form uniform in the cutoff, the exclusion of alternative II for Wilson by proof, (N-phys), the mass gap. Output library/gap-mini-nphys-fable.md.
