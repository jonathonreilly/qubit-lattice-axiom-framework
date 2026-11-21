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
4. (PROVED, elementary.) A class in which a confining theory can land must have all eight class masses
   M_{c(h)} within a factor close to one of each other. Then Z_+ and Z^0 agree up to that factor at both
   periods, and the neutral two-period bound and the periodic one are the same statement up to that factor.
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

**4.2 Corollary B2 (a rigorous instance; PROVED GIVEN Proposition B and Theorem E).** Let beta <= 1/46. On a
torus where tau is small enough that e^tau (e^tau - 1) < e^(-2 tau), the Wilson model has no twist-wise exact
representation in the class (10). Reason: by 3.2 item 2 and Theorem E (a) its twisted masses agree within
e^(2 tau); by Proposition B a representation in (10) would make them differ by the factor delta. The same
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
bound for every member. The two classes on file with such a proof, (10) and (10*), each fix the alternative:
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

## Step 5. (in progress)
