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

Steps 1-4 done (written below). Next: step 5, T_JW-lat.

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
