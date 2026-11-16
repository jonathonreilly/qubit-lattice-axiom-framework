lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T02:37Z

# Check of row 1052's Lemma FLUX-W and target T_JW-lat (row 1054)

Written by Claude Opus 5.5 (max), Mac mini worker 3, started 2026-11-16 14:37Z (date -u),
from commit b04caeebc on branch claude/ym4d-hard-route. Same provider as the author of
row 1052 (Claude Opus 5.5 high), so this is not an independent check in the sense of the
working rules; row 1055 (gpt-6-astra) is the cross-provider check. A research check, not an
audit; no mass gap is claimed anywhere in this file.

Object checked: `library/gap-wall-assumptions-opus.md` (row 1052) at b04caeebc: Lemma
FLUX-W (a)-(d), the definition of T_JW-lat (6b), sections 6c and 6d, and the Reading
"(W) = Jaffe-Witten gap + unbroken centre on tori".

## Plan (at most eight steps, one per response)

1. Read the sources: FINISH rules (build on published work, efficiency, rules), row 1052's
   FLUX-W, 6b-6d and Reading, and the on-file statements it uses: (W), (TM-c), (G1) of
   row 720, (PHYS-SEED), M_*.
2. Hand test of (a): one plaquette in an (i,k)-plane at the crossing plane; plaquette count;
   Haar invariance; commutation of C_i with T on gauge-invariant functions (TM-c).
3. Hand test of (b), (c): a two-state toy transfer operator; psi_0 invariance; E_e >= m.
4. Check (d): (G1) of row 720, (PHYS-SEED), M_*; does (W) force every flux energy above M_*.
5. Check T_JW-lat (6b): definition, and whether it implies the Jaffe-Witten gap for the
   lattice route.
6. Check 6c (frozen Z_2, Q_8, 2T do not bind T_JW-lat; flat field on a simply connected
   region is pure gauge) and 6d (no set-aside verdict changes).
7. Check the Reading ((W) = JW gap + unbroken centre on tori; argued one way, reading for
   strictness).
8. Meaning: does replacing (W) by T_JW-lat lose or gain anything; is it easier for SU(2).
   Verdicts, RESULT line.

## Status

Steps 1-7 done (written below). Next: step 8, meaning, verdict table, RESULT.

## Step 1. Sources read (all at b04caeebc)

Rule 0a: this row is a check, not an attack on an open lemma, so no open-core search was needed to start.
Repo search for prior work on the same objects: `grep` over `library/` for "(TM-c)" (20 files), "(G1)",
"limit state", "DLR". Read, with lines:

- Object: `library/gap-wall-assumptions-opus.md` L73-105 (target T, A0, A1), L188-199 (A2), L399-575
  (steps 5-7: 5.0-5.5, T_JW and T_JW-lat at L484-485, 6c table L491-510, 6d L512-528, 7.1, FLUX-W L554-561,
  Reading L563, "What this changes" L565), and the report lines L586-630 that restate them.
- (TM), (TM-c): `library/gap-crux-restate.md` L33, L35 (statements), L217 (Corollary S3'), L328 (who checked);
  `library/gap-seed-check.md` L18-40 (Lemma 1.1 (i)-(v), the checked form of (TM), (TM-c) on every box with
  sides >= 3; Claude row 698; gpt-6-astra row 699 has the same point).
- (W), (PHYS-SEED), Theorem ZD-c, (G1)-(G3): `library/gap-dichotomy.md` L73-212 and L284-292 (3.8, sources of
  (G1), (G2)); `library/gap-phys-seed.md` L320 (proof of ZD-c, where (G1) comes from), L328 (the flux reading
  of (Z-UNB) already on file); `library/gap-zd-astra.md` L205-216, L478-516 (row 730, cross-provider check of
  row 720: "(I) iff (W)" HOLDS AFTER CORRECTION of the domain of (W); "G1's lattice inequality ... follows
  directly from S3' and Z3 with N_j = l/(2 a_j) and one q' < 1").
- Limit states: `library/gap-seed-limit.md` L120 (definition), L142, L166-172, L200-204 (Proposition P' and
  its inputs), L288 (what it does not show).

Two facts from these reads that the check uses below.

1. (TM-c) on file is stated and checked on the full space H = L^2(SU(2)^E), with T_P = 0 on the
   non-invariant part (`gap-seed-check.md` L36-40, Lemma 1.1 (iv), remark (b) of L40). FLUX-W works on the
   gauge-invariant subspace. The two agree: H = H_inv (+) H_inv-perp, T_P and every C_k leave both parts
   invariant, and T_P is 0 on the second.
2. `gap-seed-limit.md` proves clustering only for limit states of admissible sequences of periodic tori. It
   says at L172 (3): "Whether a limit state satisfies the Dobrushin-Lanford-Ruelle equations is not needed
   here and not proved here", and at L288: "It does not show that the limit state is unique, that it is a
   Gibbs state". Step 5 below uses this.

## Step 2. Part (a), tested by hand

Statement checked (L556, L560): C_i (multiply by -1 every link of direction i that crosses the plane
x_i = c) preserves Haar measure and every plaquette trace, and commutes with T.

**Hand test on one plaquette at the crossing.** Take i = 1, k = 2, c = 0, base point x with x_1 = 0. The
plaquette is U_p = U_(x,1) U_(x+e1,2) U_(x+e2,1)^(-1) U_(x,2)^(-1). The link (x,1) runs from x_1 = 0 to 1:
flipped. The link (x+e2,1) also has first coordinate 0: flipped. The links (x+e1,2) and (x,2) have direction 2:
not flipped. So C_1 U_p = (-U_(x,1)) U_(x+e1,2) (-U_(x+e2,1))^(-1) U_(x,2)^(-1) = (-1)(-1) U_p = U_p, because
-1 is central and (-V)^(-1) = -V^(-1). Numbers: U_(x,1) = diag(e^(i theta), e^(-i theta)), the other three links
1. Then tr U_p = 2 cos theta before and after the flip. Two controls: (i) the same plaquette with base x_1 = -1
(mod n_1) contains no flipped link (its 1-links start at x_1 = -1; its 2-link at x + e1 lies in the plane but
does not cross it); (ii) left multiplication of the two 1-links by a non-central g turns U_p into
g U_(x,1) U_(x+e1,2) U_(x+e2,1)^(-1) g^(-1) U_(x,2)^(-1). With g = i sigma_1, U_(x,1) = D_theta :=
diag(e^(i theta), e^(-i theta)), U_(x,2) = D_phi and the other two links 1: before, tr U_p = 2 cos(theta - phi);
after, g D_theta g^(-1) = D_(-theta), so tr = 2 cos(theta + phi). These differ when sin theta sin phi != 0.
So centrality is used, and it is enough.

**The full count.** Every plaquette of the 4-torus lies in one plane (mu, nu). Planes without the direction i
contain no link of direction i: no flip. A plaquette in a plane (i, nu), nu != i (nu spatial or time), based at
x, has exactly two links of direction i, (x, i) and (x + e_nu, i), and both have i-coordinate x_i (nu != i).
So both cross the plane x_i = c, or neither does. The count "0 or 2" holds for spatial and time-like
plaquettes alike; for a time-like plaquette in the plane (0, i) the two flipped links are U(t)_(x,i) and
U(t+1)_(x,i), one in each slice. This is why C_i must act on both arguments of the kernel, which is what
"commutes with T" means: T(Z_i u, Z_i v) = T(u, v) gives T C_i = C_i T by the substitution v -> Z_i v
(Z_i preserves product Haar measure and Z_i^2 = 1). The time-like links are never flipped. Note: the flip must
be of links that cross the plane. Flipping the links that lie in the plane would flip one link of each
(i, nu)-plaquette at x_i = c and change the sign of its trace.

**Haar measure.** Left multiplication by -1 preserves Haar measure on SU(2), so Z_i preserves the product
measure. **Gauge.** (h.u)_(x,k) = h_x u_(x,k) h_(x+e_k)^(-1), and h_x (-u) h^(-1) = -(h_x u h^(-1)), so
Z_i commutes with every gauge transformation and C_i maps gauge-invariant functions to gauge-invariant
functions. **Independence of c (not used by the lemma; makes H_e canonical).** Z_i at c composed with Z_i at
c' > c is the gauge transformation h_x = -1 for c < x_i <= c', h_x = 1 otherwise (direct check on each link).
So on gauge-invariant functions C_i does not depend on c.

**Agreement with (TM-c) on file.** Lemma 1.1 (iv) of `gap-seed-check.md` (checked; inputs `gap-transfer.md`
9.3: V o Z_k = V, K_0(Z_k u, Z_k v) = K_0(u, v), Z_k(h.u) = h.(Z_k u), Z_k preserves du) states exactly this
for the plane x_k = 0, on the full L^2, with C_k a unitary involution that maps a.e.-positive functions to
a.e.-positive functions. FLUX-W's own proof of (a) and the file's statement agree; the file's form also covers
the plaquette count through 9.3.

**Verdict (a): HOLDS.** One remark, no defect: the setting line L555 lists "positivity improving" inside (TM);
the file's (TM) (`gap-crux-restate.md` L33) says only "positive trace-class, simple top eigenvalue, strictly
positive eigenfunction". The extra word is true (the kernel of T_P is continuous and strictly positive,
Lemma 1.1 (iii) gives psi_0 >= e^(-12 beta |Lambda|)) and FLUX-W does not use it.

## Step 3. Parts (b) and (c), tested on toy transfer operators

**Two-state toy.** Space {u, v}, uniform measure, T = [[a, b], [b, a]] with a > b > 0 (all kernel entries
positive; eigenvalues a + b > a - b > 0, so T is positive). C = composition with the swap u <-> v: a
measure-preserving involution. TC = [[b, a], [a, b]] = CT. Top eigenvector psi_0 = (1, 1)/sqrt 2: strictly
positive, simple, and C psi_0 = psi_0, as (b) says. The odd sector H_1 = span (1, -1) has the eigenvalue a - b, so
E_1 = log((a + b)/(a - b)) = m: (c) holds with equality. Limits: b -> 0 gives E_1 -> 0 (two degenerate
"flux" states: the frozen-Z_2 picture); b -> a gives E_1 -> infinity.

**Four-state toy (strict inequality).** T = T_f (x) T_g with T_f = [[a, b], [b, a]], T_g = [[a', b'], [b', a']],
C = swap (x) 1. Eigenvalues (a +- b)(a' +- b'). Even sector: (a + b)(a' +- b'); odd sector: (a - b)(a' +- b').
So E_odd = log((a + b)/(a - b)), m = min(E_odd, log((a' + b')/(a' - b'))), and E_odd > m when the even
excitation is lower. So (c) is an inequality, not an identity.

**(b) in general.** C_i commutes with T, so T(C_i psi_0) = lambda_0 C_i psi_0. Simplicity gives
C_i psi_0 = c psi_0; C_i^2 = 1 gives c = +-1; C_i psi_0 = psi_0 o Z_i is a.e. positive, so c = 1. HOLDS
(the file's proof says "same norm" and "by simplicity it equals psi_0"; the sign step is the positivity, which
the file's sentence "strictly positive eigenfunction" carries).

**(c) in general.** C_1, C_2, C_3 flip disjoint sets of links, so they commute; each is a self-adjoint unitary
involution. The joint eigenspaces H_e, e in Z_2^3, are orthogonal and span the space, and T leaves each
invariant. psi_0 is in H_0 by (b). For e != 0, H_e lies in psi_0-perp, and the norm of the positive compact
operator T on psi_0-perp is lambda_1 (min-max). So lambda_0^(e) <= lambda_1 and E_e >= m, with E_e = +infinity
if T = 0 on H_e. HOLDS.

**Verdicts (b), (c): HOLD.** What (c) says: the lowest level of each flux sector is one of the levels of the
full periodic transfer operator, and m(B) of `gap-dichotomy.md` L82 is the gap of the full operator, all
sectors included (Z(k, B) = Tr T_B^k is the periodic partition function). So (c) is elementary; the content
of FLUX-W is that (W) bounds the full gap on all large cubes, which is (d). The file says this itself at L554
("found again in substance") and `gap-phys-seed.md` L328 already reads (Z-UNB) as a flux statement.

## Step 4. Part (d) and what (G1) says

Statement checked (L559, L560 (d)): (W) implies, through (PHYS-SEED) and (G1), that for all large j and every
periodic cube of side L >= l, every electric flux energy satisfies E_e >= M_* = 2 log(1/q')/l in physical units.

**The chain on file, link by link.**

1. (W) gives (PHYS-SEED). `gap-dichotomy.md` L158 ("(I) holds if and only if (W) holds") and Theorem CR
   L179-182 ("The equivalence of (1) and (2) does not need (BDD-Delta)"). (W) here is the repaired wall of
   L119 (D_0 bounds D^+ on the sizes of P from L/4 on), which is the form row 1052 quotes at L405. Check:
   row 730, `gap-zd-astra.md` L499: "(I) iff (W); CR's W clause: HOLDS AFTER CORRECTION of W's domain, as in
   item 18" (the correction is that repaired domain). Standing hypothesis: (S0), `gap-dichotomy.md` L95 and
   L140 ("Everything in Section 2 is for a family with units under (S0)").
2. (PHYS-SEED) at l gives (G1). Source: proof of Theorem ZD-c, `gap-phys-seed.md` L320 ("fix q' < 1 with
   5041 S_j <= q' for all large j ... Corollary S3' gives (L/a_j) m_j >= 2 (L/l) log(1/q')"), restated at
   `gap-dichotomy.md` L198-200 and L288. Corollary S3' (`gap-crux-restate.md` L217; checked rows 698, 699):
   "Let N >= 3 and s = S(N; (2N)^3) < 1/5041, q = 5041 s. Then for every integer L >= 2N:
   m(L^3) >= log(1/q)/N." I redid the substitution: N = N_j = l/(2 a_j), an integer >= 6 by (S0) since
   l = 2^i l_1 and l_1/(4 a_j) is an integer >= 3; (PHYS-SEED) says limsup_j S_j(N_j; (2N_j)^3) < 1/5041, so
   there are s_* < 1/5041 and j_0 with S_j <= s_* for j >= j_0; put q' = 5041 s_* < 1. For j >= j_0 and every
   integer L >= 2N_j = l/a_j, m_j(L^3) >= log(1/(5041 S_j))/N_j >= log(1/q')/N_j = (2 a_j/l) log(1/q'). That is
   (G1) in the form FLUX-W uses: (l/(2 a_j)) m_j(L^3) >= log(1/q'). Cross-provider: `gap-zd-astra.md` L484-485
   ("G1's lattice inequality at Q198-200 follows directly from S3' and Z3 with N_j = l/(2a_j) and one q' < 1").
3. m_j(L^3) is the gap of the full periodic transfer operator: `gap-dichotomy.md` L81-82 defines it through
   Z(k, B) = Tr T_B^k, the periodic partition function, so all flux sectors are included. Then (c) of step 3
   gives E_e^(j)(L) >= m_j(L^3) >= (2 a_j/l) log(1/q') for every e != 0, i.e. E_e^(j)(L)/a_j >= M_*.
4. M_* agrees with the rate of (G2) (`gap-dichotomy.md` L202: M_* = 2 log(1/q')/l).

**Verdict (d): HOLDS AFTER CORRECTION (wording; no step fails).** The mathematics is right and (G1) says what
is used, for every integer side, with j_0 uniform in L. Three things are missing from the statement:

- the setting: a family with units under (S0), as in `gap-dichotomy.md` Section 2; (W) and its equivalence
  with (PHYS-SEED) are only defined and proved there;
- which (W): the repaired (W) of `gap-dichotomy.md` L119 (row 730, item 18);
- where l and q' come from: l in P is the size of (PHYS-SEED) produced by (W), not the size L of (W), and q' is
  as in step 2 above.

Corrected text of (d): "(d) Let the family Z_j satisfy (S0), and let (W) (`gap-dichotomy.md` L119) hold. Then
there are l in P, q' < 1 and j_0 such that for every j >= j_0 and every periodic cube of integer side
L >= l/a_j, every e != 0 has E_e^(j)(L) >= (2 a_j/l) log(1/q'); in physical units E_e^(j)(L)/a_j >= M_* =
2 log(1/q')/l. Inputs: Theorem ZD-c with CR ((W) gives (PHYS-SEED); row 720, check row 730 after the domain
repair of (W)), Corollary S3' (rows 697-699), and (a)-(c)."

**Lemma FLUX-W as a whole: HOLDS AFTER CORRECTION of (d)'s wording.** (a), (b), (c) hold as written. Its marks
in row 1052 ("PROVED by hand here, unchecked; found again in substance") are right: (c) is elementary, and the
link (W) -> flux bound was already on file in substance (`gap-phys-seed.md` L328: "By (TM-c) the space of the
cube splits into the eight flux sectors, so (Z-UNB) says two things ... L E_e(L) is unbounded for every flux
e"). What FLUX-W adds is the uniform form E_e >= M_* for every large cube and every large j.

## Step 5. T_JW-lat (row 1052 L485; the brief calls it 6b)

Text checked: "T_JW-lat: there are c > 0 and a physical length l such that for all large j, every
infinite-volume limit state of the cutoff-j theory (torus limits or DLR states) clusters in the sense of A2 at
rate c/l in physical units, for a total set of local observables, constants depending on the observable only.
(T_JW-lat with T0's (H2), (TOT) gives T_JW by A2 (iii); this is the lane's (G2)-(G3) with (G2) taken as the
hypothesis instead of (W).)" Row 1052 then uses two relations: (R1) "(W) implies T_JW-lat" (L611: "T_JW-lat,
which the lane's (W) implies"; L565: "weaker than (W) ... by exactly the flux clause"); (R2) T_JW-lat with T0's
data gives T_JW.

**A2 itself (L194-198): HOLDS.** I redid the proof. psi_F = [F] - <F> Omega lies in Omega-perp, the left side
is the integral of e^(-t lambda) against the spectral measure mu_F of psi_F, so mu_F([0, Delta - eps]) <=
C_F e^(-eps t) -> 0, hence E([0, Delta)) psi_F = 0; E([0, Delta)) [F] = <F> Omega; totality gives
E([0, Delta)) = projection on C Omega. (The file's sentence "E([0, Delta)) Omega... is Omega itself" is
elliptic but right.) At one fixed cutoff A2 needs no uniformity of C_F at all.

**(R1) fails as written. First failing line: L485, the state class "(torus limits or DLR states)", read with
L611 "which the lane's (W) implies".** What (W) gives on file is (G2) = Proposition P (`gap-seed-limit.md`
L188-196): clustering, and the bound ||T_nu^t psi|| <= e^(-M_* t a_j) ||psi|| on the complement of the vacuum,
for every limit state of an **admissible sequence** of periodic tori (L120, L118: spatial cubes (L_k)^3, time
extents T_i with T_i - n_(k_i) -> infinity; every integer side by row 703). Two kinds of state in T_JW-lat are
outside that class:

1. DLR states. `gap-seed-limit.md` L172 (3): "Whether a limit state satisfies the Dobrushin-Lanford-Ruelle
   equations is not needed here and not proved here"; L288: "It does not show that the limit state is unique,
   that it is a Gibbs state". Nothing on file gives clustering of a DLR state that is not such a limit state.
2. Torus limits that are not admissible, e.g. L^3 x T with T -> infinity but T - L/2 -> -infinity, or tori
   with non-cubic spatial sections. (G1) bounds the thermal sum only from half the side on (`gap-seed-limit.md`
   L92: "It gives nothing for a < n_k (below half the side)"), and S3' is for cubes only.

So with the state class as written, (W) is not known to imply T_JW-lat. Both statements are then not ordered by
anything on file: T_JW-lat asks for states (W) does not reach, and (W) asks for the flux bound that T_JW-lat does
not contain. No counterexample to "(W) implies T_JW-lat" is claimed; the implication is unproved.

**Repair (proved here from the file; same provider, not cross-checked).** Fix the state class to the one (G2)
covers:

> **T_JW-lat (corrected).** There are c > 0 and l in P such that for all large j, every limit state nu of an
> admissible sequence of periodic tori at the cutoff j (`gap-seed-limit.md` 4.1; spatial cubes of integer side)
> has ||T_nu^t psi|| <= e^(-(c/l) t a_j) ||psi|| for all psi orthogonal to its vacuum and all integers t >= 0.
> (By A2 at the fixed cutoff, this is the same as clustering at rate c/l in physical units for some total set of
> local positive-time functions, with any constants.)

Then (R1) holds: (W) gives (PHYS-SEED) and (G1) (step 4), and Proposition P (c) with n_j = l/(2 a_j),
ell_* = l/2, s_* = q'/5041 (`gap-dichotomy.md` L289-290) gives the corrected T_JW-lat with c = 2 log(1/q').
A variant T_JW-lat+ that keeps the DLR states is a stronger statement, and (W) is not known to imply it.

**(R2) HOLDS AFTER CORRECTION of the mechanism.** "By A2 (iii)" needs constants C_F uniform in the cutoff for
the lattice versions of each continuum observable. The file says this fails for the natural constants:
`gap-seed-limit.md` L198, "The sup norms in (b) are useless for renormalized observables". The working route is
the one on file: the operator bound at each cutoff (which A2 gives at fixed j, with no uniformity in C_F), then
Proposition P' (`gap-seed-limit.md` L200) with M_* replaced by c/l. P' uses only the operator bound, through the
positive-time functions of (H2) (for t >= t_0 > 0: <psi, T^t psi> <= e^(-(c/l)(t - t_0) a_j) <psi, T^(t_0) psi>,
whose right side converges under (H2)). Conclusion: given T0's continuum datum with (P1)-(P4), (H2) for the
limit states that T_JW-lat covers, and (TOT), the datum has a unique vacuum and spec(H) in {0} union
[c/l, infinity). Corrected text of the parenthesis: "(T_JW-lat with T0's datum, (H2) and (TOT) gives T_JW by
A2 at each cutoff and Proposition P' with M_* replaced by c/l.)"

**Does T_JW-lat give the Jaffe-Witten gap for the lattice route?** As an implication, yes, in the same sense as
(W) does and no more: (i) only given T0's datum, (H2) and (TOT), which nobody supplies (`gap-dichotomy.md`
L210-211; check 723: "P' additionally needs the continuum datum, positive-time convergence and totality");
(ii) the gap is on the Hilbert space of that datum. JW's clause is on all of Omega-perp of the theory with all
local gauge-invariant fields. T0's observable class is the tr(F^2) sector (`gap-seed-limit.md` L204 (4)), so
(TOT) for a class that generates every local gauge-invariant field is a further input (row 1052 marks this as
its assumption a3, L284). (iii) (H2) must hold for the states T_JW-lat covers, so T0's lattice states must be
limit states of admissible cubic tori; for the account's tori of side 2 L^m this is open
(`gap-seed-limit.md` L204 (5); `gap-dichotomy.md` L107-109). None of (i)-(iii) distinguishes T_JW-lat from (W).

**"This is the lane's (G2)-(G3) with (G2) taken as the hypothesis": HOLDS for the corrected class.** The
corrected T_JW-lat is Proposition P (c) with M_* replaced by c/l, i.e. (G2) as a hypothesis. So the gap leg
(G2) -> (G3) consumes exactly T_JW-lat; (W) enters the gap leg only through it.

**Verdict on T_JW-lat (6b): HOLDS AFTER CORRECTION.** Fix the state class as above (else (R1) is unproved), and
cite P', not A2 (iii) with cutoff-uniform constants, for (R2).

## Step 6. Sections 6c and 6d

Read for this step: row 1052 L491-528; `parts/gap.md` L28-31, L44-50, L66-70, L199-221 (test table and
definitions T_fix, T_W, T_per, T_ev at L211-212); `library/gap-crux-exercise2-max.md` L428, L436, L552 (Z_2
above 2.191); `library/gap-crux-exercise2-check-astra.md` L227-259 (check 884: the Q_8, 2T witness).

### 6c

**The elementary fact (L508): "a flat lattice gauge field on a simply connected lattice region is a pure
gauge". The statement HOLDS; the proof FAILS as written for non-abelian groups and HOLDS AFTER CORRECTION.**
First failing line: L508, "because each non-tree link closes a cycle that is a product of plaquette boundaries
on Z^4 (H_1 of the 2-skeleton of Z^4 vanishes)". H_1 = 0 says that each cycle is a sum of plaquette boundaries
in the abelian group of 1-chains. For a non-abelian group (Q_8, 2T, SU(2)) that is not enough: holonomy is a
homomorphism from the fundamental group of the 2-complex, so one needs each fundamental cycle to be a product of
conjugates of plaquette loops, i.e. pi_1 of the 2-skeleton = 1 (true: it equals pi_1(R^4) by cellular
approximation, but that is a citation, not a hand step). Q_8 and 2T are exactly the cases 6c applies the fact to.
Corrected proof, by hand, any group G, written so that it can be formalized:

> **Lemma FLAT.** Let Lambda be Z^4 or a box [0, n_1] x ... x [0, n_4] of Z^4 with its links and plaquettes, and
> let U give each link (x, mu) an element U_(x,mu) of a group G, with every plaquette holonomy
> U_(x,mu) U_(x+e_mu,nu) U_(x+e_nu,mu)^(-1) U_(x,nu)^(-1) = 1. Then there is g: Lambda -> G with
> U_(x,mu) = g_x g_(x+e_mu)^(-1) for every link.
>
> Proof (complete axial gauge). For x in Lambda let P_x be the lattice path from 0 to x that moves first along
> direction 1, then 2, then 3, then 4, and h_x the ordered product of U along P_x (an inverse for each step
> against a link's orientation). Claim: h_x U_(x,mu) = h_(x+e_mu) for every link (x, mu) of Lambda. Prove it for
> mu = 4, 3, 2, 1 in this order. If (x, mu) lies on the path P_(x+e_mu) (for mu = 4 always; for mu < 4 when
> x_nu = 0 for all nu > mu), the claim is the definition of h. Otherwise let nu > mu be the largest direction with
> x_nu != 0, say x_nu > 0 (x_nu < 0 is the same with the plaquette at x), and y = x - e_nu. Flatness of the
> (mu, nu)-plaquette at y gives U_(x,mu) = U_(y,nu)^(-1) U_(y,mu) U_(y+e_mu,nu). The claim for the nu-links
> (y, nu) and (y + e_mu, nu) is known (nu > mu was done first), and the claim for (y, mu) holds by induction on
> |x_nu|. So h_x U_(x,mu) = h_x U_(y,nu)^(-1) U_(y,mu) U_(y+e_mu,nu) = h_y U_(y,mu) U_(y+e_mu,nu)
> = h_(y+e_mu) U_(y+e_mu,nu) = h_(x+e_mu). Put g_x := h_x^(-1). QED. No step commutes two elements of G.

For a finite box only plaquettes inside the box are used (y_nu = x_nu - 1 >= 0), so free boundary is allowed,
as L508 says. Consequence used by 6c, checked: in a frozen model (all plaquettes 1) every gauge-invariant
function of the links of a box takes its value at the trivial field. On a torus whose side exceeds the width
of the support, the support lies in such a box, so every local gauge-invariant function is a.s. constant in every
torus state, every limit state is the point mass at the trivial field on local functions, and both the original
and the corrected T_JW-lat (step 5) hold trivially (the OS space is C Omega). So the frozen models are positive
controls of T_JW-lat, as 6c says.

**The table's T_JW-lat column: HOLDS, with three wording corrections.**

1. "bind exactly the statements made on periodic tori with all (or all centre-even) sectors" (L508): "exactly"
   should be "only". The binding comes from flat classes around non-contractible cycles. It reaches every
   statement made on a region with such cycles and with those sectors kept (periodic tori, and the spatially
   periodic cylinders L^3 x Z that `gap-seed-limit.md` L118 also uses), and no statement about local functions
   in limit states or on simply connected boxes.
2. Frozen Q_8, 2T row (L500): the extra centre-even flat states come from commuting holonomy **triples** with a
   non-central entry, e.g. (i, 1, 1) against (1, 1, 1) (check 884, L235), not "pairs".
3. Frozen Z_2 row (L499): the lane's theorem-grade Z_2 test is at beta above 2.191, not at beta = infinity
   (`parts/gap.md` L220; `gap-crux-exercise2-max.md` L428). At finite beta the flat-field lemma does not apply.
   There "T_JW-lat true" rests on the recalled weak-coupling decay theorem for finite groups (I16: Adhikari and
   Cao; the Chatterjee 2020 paper named in the row is about Wilson loops). The verdict "does not bind" stands,
   with that input marked recalled.

The other rows of the T_JW-lat column check out against the definitions: compact U(1), the free photon and the
products with a massless factor have power-law or massless decay in every limit state, so T_JW-lat fails there
and they bind; for Proposition NP, the ordered Ising factor makes the torus limit state the symmetric mixture of
the two phases, which does not cluster, so NP binds T_JW-lat too (the row says "yes for T_JW"; the same holds for
T_JW-lat); D2, SUB, SHEET are false hypothesis forms and bind whatever the target.

**Credit, found again.** The scoping itself was on file before row 1052: check 884 (gpt-6-astra,
`gap-crux-exercise2-check-astra.md` L231): "A local mass gap does not imply every finite-volume seed, especially
a trace seed counting all topological states. Thus the test for a confinement conclusion is not automatically a
test for a local mass gap. This part of the narrowing HOLDS." Row 1052 credits row 838 item 94 and the test table.
What it adds is the topological reason, now with the corrected proof.

**Verdict 6c: HOLDS AFTER CORRECTION** (proof of the flat lemma; three wording repairs). No binding claim changes.

### 6d

Checked: whether any verdict on the lane's lists rests **only** on a frozen-group test. Bounded search:
`grep` of `parts/gap.md` (258 lines) for "frozen", "Q_8", "2T", "FG". Hits: L30, L49, L70, L151, L201, L207,
L220-221. None of them is the sole kill of a method. L70 and L201 are the re-judged filter "Q_8, 2T bind T_per
only", which check 884 struck as a blanket exemption for ES (an even-sector torus statement); that strike stands
for torus statements, and 6c does not touch it. Exercise 4 input 2 (Fact T) is killed by FG at the flux half,
which T_JW-lat does not need: moot, as row 1052 says. Rows 1004-1050 were not opened by row 1052 or by me; on
`parts/gap.md` L136-150 none of their kills is a frozen-group test.

**Verdict 6d: HOLDS (as a statement about verdicts on the methods as they were stated).** A method killed at a
torus statement stays killed there; whether it can be re-aimed at a simply connected or infinite-volume statement
is a new route, not a re-judged verdict, and this check makes no attack.

**One consequence row 1052 does not list (for its work item W2).** Two lane filters name the frozen groups as
models a selective step must fail in: `parts/gap.md` L30 (comparison cases "frozen Q_8 and 2T") and L48-49
((K-flow): "a step that fails for U(1), for frozen groups and for products with a massless factor"). For a
T_JW-lat target the frozen groups drop out of both lists (they become positive controls). W2 names only the
test-table row; if the lead adopts it, L30 and L49 need the same note.

## Step 7. The Reading (row 1052 L563, repeated at L588, L611, L621 and in the RESULT line)

Read for this step: row 1052 L563-565; `parts/gap.md` L17-24 (the lane's target is the wall (W)) and L169
(registry column "Strength against the target"); `gap-phys-seed.md` L328; `gap-crux-exercise2-max.md` L428;
FINISH L947 (only the clause on the Peierls test).

The Reading has five parts. Verdict for each.

**R1. "(W) implies the flux bound" (marked argued).** This is FLUX-W (d). HOLDS (step 4, with the wording
correction). The mark can read: proved by hand from Theorem ZD-c with CR (row 720, check row 730), Corollary
S3' (rows 697-699) and (S0); checked line by line by Claude Opus 5.5 (this row, same provider); cross-provider
check pending (row 1055).

**R2. "(d) is a statement that the centre one-form symmetry stays unbroken on large spatial tori".**
HOLDS AFTER CORRECTION (wording). (d) is a uniform positive lower bound on the flux-sector levels. The usual
meaning of an unbroken centre symmetry is the area law, which makes E_e(L) grow like sigma L. (d) asks much less;
the file says so for (Z-UNB) (`gap-phys-seed.md` L328: "The flux part is far weaker than an area law: it asks
that the flux energy is not of the order of 1/L"). (d) excludes flux sectors that become degenerate with the
vacuum (E_e -> 0). It is "unbroken centre" only under the physics reading that a gapped phase either confines or
has degenerate flux sectors. Suggested words: "(d) says the electric flux sectors of large periodic cubes stay a
fixed physical gap above the vacuum: a non-degeneracy of the flux sectors, implied by the area law and much
weaker than it."

**R3. The separating example: "a Z_2 topologically ordered phase ... would satisfy T_JW and violate (d), hence
(W)", marked "recalled, not built".** HOLDS AFTER CORRECTION.
(i) It is an example in another model (Z_2 at fixed large beta). That model has no continuum limit, so it
can only satisfy the lattice form: T_JW-lat at one fixed coupling (the constant sequence), not T_JW. It
separates the logical forms of the two statements on the class of reflection-positive lattice gauge models with
(TM). It says nothing about Wilson SU(2) on the account's trajectory.
(ii) The torus half is on file, not only believed. The lane records "the periodic seed" as failing for Z_2
above beta = 2.191 as THM (Peierls; `gap-crux-exercise2-max.md` L428, which cites FINISH L947; `parts/gap.md`
L220, "T_per only"). I did not re-derive that Peierls proof; FINISH L947 describes it as refuting "an
environment-uniform conditional bound (proof valid for beta above 2.191)". So the mark should read: torus half
lane THM as recorded (not re-derived here); infinite-volume half recalled THM (I16, Adhikari and Cao).
(iii) A completely hand-checked separation of the forms exists only at the frozen end (beta = infinity). The
eight flat Z_2 sectors of the periodic cube are exactly degenerate there, so every periodic seed fails, and
Lemma FLAT (step 6) makes every limit state trivial on local functions, so T_JW-lat holds. That model is trivial
and has no simple top eigenvalue, so it separates only the forms, and only at the boundary of the class.

**R4. "So, relative to what is proved, (W) is the JW gap plus an unbroken-centre (confinement-type) statement
on tori"; RESULT line: "(W) = the Clay gap plus an unbroken-centre statement on tori".** FAILS as an identity.
HOLDS AFTER CORRECTION as a one-way statement. First failing line: L563, the bold sentence. What is proved is one
direction: (W) implies the corrected T_JW-lat (step 5, through (G2)) and the flux bound (d) (step 4). The
converse, T_JW-lat (or T_JW) together with (d) implies (W), is not proved. It needs at least:
(a) a finite-size step, from a clustering rate of infinite-volume limit states and a flux bound to a uniform gap
of every large periodic cube in the even sector. On file this is the open direction: row 838 item 52 ("a gap
alone is not shown to give one [a seed]") and check 884 L231 ("A local mass gap does not imply every
finite-volume seed").
(b) (BDD-Delta), a bounded Casimir free energy on physical sizes, which (W) contains (Theorem ZD-c) and neither
T_JW-lat nor (d) mentions (row 1052's own S5, L464).
(c) For T_JW in place of T_JW-lat: uniformity on every lattice of the sequence (S2, L461), also open.
So the flux clause is one identified part of the excess of (W) over T_JW-lat, not shown to be the whole excess.
L565 "weaker than (W) ... by exactly the flux clause" has the same defect: "exactly" must go. Corrected text for
L563: "So (W) implies T_JW-lat (for limit states of periodic cubes, through (G2)) and the flux bound (d); the
converse is open (finite-size step, (BDD-Delta)). The flux bound is one identified part of what (W) asks beyond
the JW gap; on the class of lattice gauge models it is a real part, by Z_2 above 2.191; for SU(2) no separation
is known or believed (B4)."

**R5. "The lane's registry 'strength against the target' column measures against (W), not against T_JW".**
HOLDS. `parts/gap.md` L17-24 states the lane's target as (W) itself, and the registry column (L169) is read
against that target.

**Verdict on the Reading: HOLDS AFTER CORRECTION.** One direction is proved, as the author marks it. The bold
identity and "exactly" overstate it. The separating example is better supported than the file says (the torus
half is lane THM), but it lives on the class of models, not on SU(2).
