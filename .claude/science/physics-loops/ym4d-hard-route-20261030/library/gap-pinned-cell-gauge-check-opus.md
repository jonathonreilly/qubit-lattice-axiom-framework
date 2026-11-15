lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-16T06:54Z

# Row 1014, gap-pinned-cell-gauge-check-opus: check of row 1011 (work item W1)

Started 2026-11-15T18:54Z on Mac mini worker 3, Claude Opus 5.5 max, at branch
`claude/ym4d-hard-route`, commit f4dd47b82. Checked object:
`library/gap-pinned-cell-gauge-max.md` (row 1011, written by Claude Fable 5.2 max;
same provider as this check, so this is not an independent check in the sense of
the working rules: a second model of the same vendor, but a separate derivation
where the text below says so). Task: work item W1 of that file, section 9.7, exactly
as written there. No new attack.

## 0. Plan (save protocol; at most eight steps, one step per response, result appended before the next)

Fixed after step 1 to the exact W1 list of row 1011, 9.7 (L582-594):

1. Read W1 and the whole of row 1011's file; copy the W1 list; fix this plan. (done)
2. Tests first: (a) is the strength field of 4.2 (b on boundary plaquettes, 0 inside) in the class the row
   means; (b) does the base corner of 4.4 vanish identically; (c) the sign in 7.3 "Use".
3. (i) Proposition A (i), second-order expansion with the quaternion rules of 3.1; (ii) Proposition W, the mixed
   coefficient and its same-link part.
4. (iii) Propositions B and B' (covariance with the tail convention, H_c(1; B) for the boundary strength field,
   the two lower bounds); (iv) Proposition SEAG (four corner cases, gauge averaging, the count 6 + 18).
5. (v) Lemma CEN (and Corollary CEN2, which 4.7 and the RESULT use); (vi) Lemma EMB against p. 13 of OpenAI's
   O(4) paper (fetched into a new empty /tmp folder).
6. (vii) Lemma FR.
7. The two corrections of row 1009 (Section 5 end of row 1011), judged against row 1009 L387-390 and L406.
8. Verdict table (ADVANCE / CORRECT-NO-ADVANCE / WRONG with the failing line), stop rule, RESULT line.

Stop rule (W1): stop at the first WRONG that breaks 4.7 and report it.

## Status log

- 2026-11-15T18:54Z: file created, plan written. Next: step 1.
- 2026-11-15T18:56Z: step 1 done (Section 1). Next: step 2, tests (a)-(c).
- 2026-11-15T18:58Z: step 2 done (Section 2): tests (a), (b), (c) PASS; scope remark on (a). Next: step 3, (i) Proposition A (i), (ii) Proposition W.
- 2026-11-15T19:00Z: step 3 done (Section 3): Proposition A (i) and Proposition W re-derived, both CORRECT-NO-ADVANCE, no defect. Next: step 4, (iii) B and B', (iv) SEAG.
- 2026-11-15T19:03Z: step 4 done (Section 4): B CORRECT-NO-ADVANCE; B' PROVED part ADVANCE; SEAG identity CORRECT-NO-ADVANCE with defect 1 (averaging site at the far corner, repaired) and a scope remark. Next: step 5, (v) CEN and CEN2, (vi) EMB against OpenAI p. 13.
- 2026-11-15T19:05Z: step 5 part 1 written (5 (v)): CEN, CEN2 CORRECT-NO-ADVANCE. Next: fetch OpenAI O(4) paper, check EMB.
- 2026-11-15T19:06Z: step 5 done: EMB checked against OpenAI p. 13, CORRECT-NO-ADVANCE. Next: step 6, (vii) Lemma FR.
- 2026-11-15T19:07Z: step 6 done: Lemma FR CORRECT-NO-ADVANCE, defect 2 (wording of the NA = 0 gloss). Next: step 7, the two corrections of row 1009.
- 2026-11-15T19:09Z: step 7 done: both corrections of row 1009 UPHELD, each narrowed (Section 7). Next: step 8, verdict table and RESULT.

## 1. Step 1: the brief, copied, and what this check reads

Provenance: Anthropic, Claude Opus 5.5, max effort, one session, no subagents, at commit f4dd47b82. Not an audit.
Row 1011 was written by Anthropic's Claude Fable 5.2: same provider, different model. So this is a second reading
by another model of the same vendor; where a step below is re-derived by a different route (a different
parametrisation, a different order of expansion), that is said, and only that part is an independent derivation.

W1 as written (row 1011, 9.7, L582-594), copied without change of content:

- Read Sections 3, 4 and 7.3 of `library/gap-pinned-cell-gauge-max.md` at the commit that holds it (here
  f4dd47b82; the file was read in full, 622 lines).
- Redo by hand, in this order: (i) Proposition A (i): the expansion of t_p(e^(eps B) U) to second order, with the
  quaternion rules of 3.1; (ii) Proposition W: the mixed coefficient and its same-link part; (iii) Proposition B
  and B': the covariance rule with the tail convention, the value H_c(1; B) for the boundary strength field, the
  two lower bounds; (iv) Proposition SEAG: the four corner cases, the gauge-averaging step, the count 6 + 18;
  (v) Lemma CEN; (vi) Lemma EMB against p. 13 of OpenAI's O(4) paper (github.com/openai/math commit
  4eaee87548250b2682affda7d05d947c05554bae, `preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf`);
  (vii) Lemma FR.
- Test first: (a) in 4.2, is the strength field (b on boundary plaquettes, 0 inside) inside the class the row
  means; (b) in 4.4, does the base corner vanish identically; (c) the sign in 7.3 "Use".
- Verdict per statement: ADVANCE, CORRECT-NO-ADVANCE or WRONG with the failing line. Also judge the two
  corrections of row 1009 in Section 5. Stop rule: stop at the first WRONG that breaks 4.7 and report it. No new
  attack.

Reading of the verdict words used here (FINISH, Rules, "Check reports"): ADVANCE = the statement is correct as
written and is new progress for the lane (a new proved fact the lane did not have); CORRECT-NO-ADVANCE = correct
as written (or correct after a repair that does not change what 4.7 uses) but adds nothing the lane did not have,
or is an identity with no consumer; WRONG = a line fails, with the failing line named. A slip that does not change
the statement's use is reported as a defect under a CORRECT verdict, with its line.

What 4.7 of row 1011 rests on (so what the stop rule protects): Propositions B, B', Lemma CEN, Proposition SEAG
for the FAIL verdict on (M2)-(M3); Propositions A, W and 3.4 for "the identities exist". Lemma EMB, Lemma FR and
Corollary CEN2 feed 4.7 (i), 7.3-7.4 and the RESULT, not the FAIL verdict itself.

Credit: the mathematics checked here is row 1011's (Claude Fable 5.2); the 2D mechanism it transfers is OpenAI's
(posted, unrefereed preprints, github.com/openai/math at commit 4eaee8754); readings of it are rows 1009, 1010.


## 2. Step 2: tests (a)-(c), done first

Conventions used in all checks below are row 1011's (3.1, 3.2): U_l -> g_tail U_l g_head^(-1); U_p = U_1 U_2 U_3^(-1) U_4^(-1)
based at x; (e^B U)_l = e^(B_l) U_l; Ad(g) X = g X g^(-1); for imaginary quaternions u v = - u.v + u x v, so
[u, v] = 2 u x v; Ad(cos phi + s^ sin phi) is the rotation by 2 phi about s^ (right-hand sense). The coboundary
convention the row uses (read off 4.2 L248-249 and 4.4 L297) is (d lambda)_l = lambda_head - lambda_tail.

### (a) Is the strength field of 4.2 (b on boundary plaquettes, 0 inside) in the class the row means? YES.

- Row 1011's class (3.1, L142-146) is all (c, omega, beta) with every strength field |beta_p| <= b or beta_p in
  [0, b]; the queue row of 1011 (FINISH L1092) states the 2D hypothesis as "a supremum over every cell, every
  boundary pin and every strength field in [0, b]" and seed 3 as "uniform over all Dirichlet boundary link data and
  all plaquette strengths in [0, b]". The field beta_p = b on boundary plaquettes, 0 on all others, is pointwise in
  [0, b]. It is a member. Boundary plaquettes are in the cell action with weight w_p (3.1, L140-144), as tangent
  boundary bonds are in OpenAI's 2D action with half weight (row 1011 4.5, L327-332, to be checked in step 5).
- The same profile in 2D (b on boundary-boundary bonds, 0 elsewhere) gives H = b sum w_e t_e (f_y - f_x)^2 <=
  b x classical, so the profile itself is harmless in 2D; the 4D failure is not an artefact of the profile.
- Scope remark (no defect; it bounds what 4.7 may claim). The PROVED part of B' uses a member with zero interior
  coupling: the response comes from the pin's own boundary plaquettes. So "no pin-uniform curl bound on C_b" is
  PROVED for the class with all strength profiles, which is the class the row and its source mean. For a smaller
  class with homogeneous strength b' w_p (b' in [0, b]), which is also closed under conditioning on rings, the PROVED
  part of B' does not apply; there the failure rests on the ARGUED remark L259-261 only. Row 1011 labels this
  honestly (L259-261: "ARGUED only"). A route to extend it (unproved, not attempted here, no new attack): if
  omega = 1 minimises F_int(omega) = - log int exp(sum over non-boundary plaquettes of b w_p t_p) dU_int, then
  H_c(1; theta n) >= b sum over boundary plaquettes w_p |d(theta n)_p|^2 at homogeneous strength, and the proved
  bound of B' carries over. That minimisation (a Ginibre-type statement for SU(2)) is not known to this check.

### (b) In 4.4, does the base corner vanish identically? YES.

At a plaquette based at z (x = z) the field B = a d lambda has B_1 = B_4 = -a (tails at z) and B_2 = B_3 = 0. By the
move-left rule of Proposition A, U_p(e^(eps B) U) = e^(-eps a) U_1 U_2 U_3^(-1) U_4^(-1) e^(eps a) = e^(-eps a) U_p e^(eps a), so
t_p(eps) = Re(e^(-eps a) U_p e^(eps a)) = t_p for every eps (Re is conjugation invariant). Both links of p at z have
tail z, and on tail-z links B acts as the gauge transformation g_z = e^(-eps a); so on this plaquette the deformation
is exactly that gauge transformation. The row's direct check (L307-308) is also right: with (a_1, ..., a_4) =
(-a, 0, 0, Ad(U_p) a), |delta_p|^2 = |a - R_(2 phi) a|^2 = 4 sin^2 phi |a_perp|^2, so t |delta|^2 = 4 sin^2 phi cos phi |a_perp|^2;
kappa_p = [-a, Ad(U_p) a] = - 2 a x R a, and (a x R a) . s^ = |a_perp|^2 sin 2 phi, so kappa . s = - 2 |a_perp|^2 sin 2 phi sin phi
= - 4 sin^2 phi cos phi |a_perp|^2. The first-order term - delta . s_p = - (R a - a) . s^ sin phi = 0 as well.

Caution for step 4 (not a defect of the base corner): on links with HEAD z the field B = + a acts as left
multiplication e^(eps a) U_l, while the gauge transformation acts as U_l e^(eps a) on the right. So B is a gauge
direction only on the tail-z links; this is why the other three corners do not vanish.

### (c) The sign in 7.3 "Use". RIGHT, with the head-minus-tail convention.

The infinitesimal gauge transformation g = e^(eps X) gives U_l -> e^(eps X_tail) U_l e^(-eps X_head) =
e^(eps X_tail) e^(-eps Ad(U_l) X_head) U_l, so its left link field is G(X)_l = X_tail - Ad(omega_l) X_head; with X = mu n this is
mu_tail n_tail - mu_head Ad(omega_l) n_head, as the row writes (L477). With D_l n = n_tail - Ad(omega_l) n_head:

  G(- lambda n)_l + lambda_head D_l n = - lambda_tail n_tail + lambda_head Ad(omega_l) n_head + lambda_head n_tail - lambda_head Ad(omega_l) n_head
                                     = (lambda_head - lambda_tail) n_tail = (d lambda)_l n_tail.

So the identity of L476 holds with (d lambda)_l = lambda_head - lambda_tail, the convention of 4.2 and 4.4. (Under the
opposite convention both the sign of the gauge generator and of the defect term flip; the row is self-consistent.)

Remark on the sentence after it (L478, a reading, not under test): "the Ward identity of the U(1) about n fails
exactly by the frame defect D n". Along the exponential curve e^(eps G(X)) omega the Hessian of a gauge-invariant F is
not zero at a pin that is not critical: by Baker-Campbell-Hausdorff, omega^(e^(eps X)) = e^(eps G(X) + eps^2 R + O(eps^3)) omega with
R_l = - (1/2) [X_tail, Ad(omega_l) X_head], so H_c(omega; G(X)) = - 2 DF_c(omega)[R]. For X = lambda n, Ad(omega_l) n_head =
n_tail - D_l n, so R_l = (1/2) lambda_tail lambda_head [n_tail, D_l n]: this correction is also proportional to D n. So the
sentence stands as written (every deviation from the abelian Ward identity is proportional to D n); a reader should not
take "gauge directions are null directions of H_c" as exact at a general pin.

Tests: (a) PASS (with the scope remark), (b) PASS, (c) PASS. No WRONG so far; continue.

## 3. Step 3: (i) Proposition A (i) and (ii) Proposition W, redone by hand

### (i) Proposition A (i) (row 1011 L163-178). CORRECT-NO-ADVANCE.

Holonomy. (e^(eps B_1) U_1)(e^(eps B_2) U_2)(e^(eps B_3) U_3)^(-1)(e^(eps B_4) U_4)^(-1), with (e^(eps B_3) U_3)^(-1) = U_3^(-1) e^(-eps B_3). Each
exponential is moved to the far left past the unperturbed product standing left of it, using g e^X g^(-1) = e^(Ad(g) X)
(exact): e^(eps B_1) U_1 e^(eps B_2) = e^(eps B_1) e^(eps Ad(U_1) B_2) U_1; then U_1 U_2 U_3^(-1) e^(-eps B_3) = e^(-eps Ad(U_1 U_2 U_3^(-1)) B_3) U_1 U_2 U_3^(-1);
then U_p e^(-eps B_4) = e^(-eps Ad(U_p) B_4) U_p. So U_p(eps) = E(eps) U_p with E as stated, a = (c_1, c_2, -c_3, -c_4), and
the c_i use the unperturbed links. Exact for all eps, as the row says.

Second order, by a route other than the row's (direct differentiation instead of the product expansion):
E'(0) = sum a_i = delta_p and E''(0) = sum_i a_i^2 + 2 sum_(i<j) a_i a_j. With a_i a_j = - a_i . a_j + a_i x a_j:
E''(0) = - |sum a_i|^2 + 2 sum_(i<j) a_i x a_j = - |delta_p|^2 + kappa_p, since [a_i, a_j] = 2 a_i x a_j. Then
t_p(eps) = Re(E(eps) U_p) with U_p = t_p + s_p and Re(u (t + s)) = - u . s for imaginary u gives
t_p - eps delta_p . s_p - (eps^2/2)(|delta_p|^2 t_p + kappa_p . s_p) + O(eps^3). Agrees with L164 term by term.

Also checked (used by B' and SEAG, not listed in W1): A (ii) and A (iii). (ii): on interior links e^(eps B_l) is a
fixed left translation, so by left invariance of Haar measure Z(eps) = int exp(A_c(e^(eps B_bd) omega, U_int)) dU_int at
EVERY eps, for every extension; hence F'' = - E[A''] - Var(A') with A'(0) = X_c(B), A''(0) = - sum beta w (t |delta|^2 + kappa . s).
The formula of L168 follows, and independence of the extension holds at every eps, not only at second order.
(iii): delta_p . s_p = sum_i (+-) B_(l_i) . Ad(T_i^(-1)) s_p (Ad orthogonal), regrouped by link; N_l is the derivative of A_c
in the boundary link l. Correct. The U(1) remark (L180-182): all fields and links in one torus, so Ad acts trivially
on a, delta_p = a (d theta)_p, kappa_p = 0, and beta_p t_p <= |beta_p| <= b gives H_c <= b sum w_p (d theta~)_p^2 for every pin
and every extension, so for the infimum over extensions. Correct.

Why no advance: an exact second-order expansion, used inside the row as the tool for B' and SEAG; no open statement
of the lane consumes it.

### (ii) Proposition W (row 1011 L186-200). CORRECT-NO-ADVANCE.

The order of the eight factors. On link 3, (e^(d B_3) e^(e B'_3) U_3)^(-1) = U_3^(-1) e^(-e B'_3) e^(-d B_3), so after moving left the
B'-factor precedes the B-factor; the same on link 4; on links 1, 2 the B-factor comes first. This is exactly the
row's order [c_1][c'_1][c_2][c'_2][-c'_3][-c_3][-c'_4][-c_4] (L187), with c'_i formed with the same transports as c_i.

Vanishing derivative. Since B = 0 on boundary links, on every link e^(d B_l) e^(e B'_l) is either the fixed left
translation of an interior link or e^(e B'_l) on a boundary link, so N(d, e) does not depend on d for any e. Hence
0 = d_d d_e N(0, 0) = Z (E[d_d d_e A] + E[X_c(B) X_c(B')]), with d_d A(0, 0) = X_c(B), d_e A(0, 0) = X_c(B') by A (i).

Mixed coefficient. In a product of eight exponentials each carrying d or e, the d e coefficient is the sum over
mixed pairs k < m of f_k f_m. Each unordered pair {a_i, a'_j} occurs exactly once, so the symmetric part sums to
- sum_(i,j) a_i . a'_j = - delta_p(B) . delta_p(B'); the antisymmetric part is (1/2) sum over mixed pairs of [earlier, later]
= (1/2) kappa_p(B, B'). Taking Re against U_p: d_d d_e t_p = - t_p delta_p(B) . delta_p(B') - (1/2) kappa_p(B, B') . s_p.
Inserting into the vanishing derivative gives the displayed identity of L190 exactly (signs and the factor 1/2).

Same-link part. Pairs on one link: link 1, [c_1, c'_1] = [B_1, B'_1]; link 2, [c_2, c'_2] = Ad(U_1)[B_2, B'_2] (Ad is a Lie
algebra automorphism); link 3, [-c'_3, -c_3] = - Ad(U_1 U_2 U_3^(-1))[B_3, B'_3]; link 4, [-c'_4, -c_4] = - Ad(U_p)[B_4, B'_4]. The sum is
delta_p([B, B']) with the signs of delta_p, so the same-link part of the bracket term is
(1/2) sum beta w delta_p([B, B']) . s_p = - (1/2) X_c([B, B']), as L193 states. [B, B'] vanishes on boundary links, so
E[X_c([B, B'])] = 0 by the first-order identity; the term is a covariance, not a mean. For U(1) all brackets vanish.

Consistency used later by SEAG: with B' = B, for links i < j both mixed pairs (B-slot of i, B'-slot of j) and
(B'-slot of i, B-slot of j) have i first, so they give 2 [a_i, a_j]; same-link pairs give [a_i, a_i] = 0. Hence
kappa_p(B, B) = 2 kappa_p(B) (L304), and Proposition W gives E[X_c(B)^2] = E[direct term of B], which with
H_c(omega; B) = 0 for B vanishing on the boundary (Z does not change) is the same statement read from A (ii).

Why no advance: the second-order Schwinger-Dyson identity, a direct corollary of left invariance of Haar measure;
the lane had the first-order form (row 754). Correct, with no consumer outside the row.

Defects found in (i)-(ii): none.

## 4. Step 4: (iii) Propositions B, B' and (iv) Proposition SEAG, redone by hand

### (iii-1) Proposition B (row 1011 L221-232). CORRECT-NO-ADVANCE.

Covariance with the tail convention: (e^(eps B) omega)^g_l = g_tail e^(eps B_l) omega_l g_head^(-1) = e^(eps Ad(g_tail) B_l) g_tail omega_l g_head^(-1)
= (e^(eps Ad_g B) omega^g)_l, exactly, for every eps. F_c is gauge invariant (extend g arbitrarily to interior sites;
interior links change by U -> U^g, Haar measure and every t_p are invariant). So F_c(e^(eps B) omega) =
F_c(e^(eps Ad_g B) omega^g) for all eps, and the second derivatives agree: H_c(omega; B) = H_c(omega^g; Ad_g B). omega -> omega^g is
a bijection of pins, so the suprema agree. Orbit: (Ad_g (a theta))_l = theta_l Ad(g_tail(l)) a, and Ad: SU(2) -> SO(3) is onto,
so n_x = Ad(g_x) a is an arbitrary unit vector at each site, independently (|a| = 1). Correct as written. No advance:
a one-line consequence of gauge invariance; its content is used through B'.

### (iii-2) Proposition B' (row 1011 L234-261). PROVED part: ADVANCE. ARGUED part: labelled honestly.

The value H_c(1; B) for the boundary strength field. With beta_p = b on boundary plaquettes and 0 elsewhere, every
plaquette with an interior link has strength 0, so int exp(A_c) dU_int = exp(b sum_bdry w_p t_p(omega)) (Haar measure
normalised) and F_c(omega) = - b sum over boundary plaquettes of w_p t_p(omega), a deterministic function of the pin.
By A (i) at U = 1 (t_p = 1, s_p = 0, all transports trivial, so c_i = B_i): H_c(1; B) = b sum_bdry w_p |B_1 + B_2 - B_3 - B_4|^2
for every su(2)-valued boundary field B. Correct (L245-247).

Reduction to the trivial pin. Given n, choose g_x with Ad(g_x) n_x = a. Then Ad_g(theta n) = a theta and, by B,
H_c(1; theta n) = H_c(1^g; a theta) <= sup over pins of H_c(omega; a theta). Correct (L247-248).

First lower bound (closed theta). theta = d lambda, lambda the indicator of a boundary site z, with the head-minus-tail
convention. Take any boundary plaquette p and call its vertex x + mu = z (all four vertices of a boundary plaquette
are boundary sites). Then theta_1 = + 1 (head of l_1 is z), theta_2 = - 1 (tail of l_2 is z), theta_3 = theta_4 = 0 (z is not an
endpoint of l_3 = (x + nu -> x + mu + nu) or l_4 = (x -> x + nu)), so d(theta n)_p = n_x - n_z (L249). Every other boundary plaquette
contributes a term >= 0. Choosing n_x != n_z gives sup over pins of H_c(omega; a theta) >= b w_p |n_x - n_z|^2 > 0, while
the extension d lambda~ (lambda~ = lambda extended by 0) has curl zero on every plaquette, so the infimum of the classical
action is 0. Hence no K exists. The statement "there is NO constant K ... for all pins, all strength fields in [0, b]
and all real boundary fields theta" is PROVED, for the class with all strength profiles (Section 2 (a)).

Second lower bound (random signs). The tails of l_1, ..., l_4 are x, x + mu, x + nu, x (L250), so with n_y = eps_y a,
d(theta n)_p = a [eps_x (theta_1 - theta_4) + eps_(x+mu) theta_2 - eps_(x+nu) theta_3]. x, x + mu, x + nu are distinct, the signs are
independent with mean 0, so the mean square is theta_2^2 + theta_3^2 + (theta_1 - theta_4)^2 (|a| = 1), and the supremum over n is at
least the mean. Summing over boundary plaquettes with w_p gives the second bound of L242-243. Correct.

The ARGUED reading (L253-261). Cauchy-Schwarz on a square of side r with flux f r^2: (f r^2)^2 <= 4 r sum theta^2, so
sum theta^2 >= f^2 r^3/4, for every gauge of the potential (the flux is gauge invariant). Concentric squares with
disjoint perimeters (sides S, S - 2, ...) in each of the order S slices of a boundary 3-face give order f^2 S^5; each
boundary link away from edges is l_2 or l_3 of some boundary plaquette with w_p >= 1/4, so the second bound gives a pin
supremum of order b f^2 S^5 against the classical b f^2 S^4. So the best uniform h is at least of order b S. The
orders check; the constants are not computed, and the row marks them ARGUED. The homogeneous-strength case is marked
ARGUED only (L259-261); see Section 2 (a) for its scope.

Why ADVANCE: the PROVED part turns the reading-level remark of rows 1007 B(5) and 1009 Step 7 (no continuous gauge
twist) into a proof that the transcribed induction hypothesis, a classical-action bound uniform over C_b, is false at
every scale and for every constant. It is the statement that carries the FAIL verdict of 4.7 for (M2)-(M3).

### (iv) Proposition SEAG (row 1011 L294-318). Identity: CORRECT; one imprecise sentence in the proof (not breaking).

Setting: z interior with all neighbours interior; B_l = + a on links with head z, - a on links with tail z (|a| = 1),
B = 0 elsewhere, so B = 0 on boundary links. Every plaquette containing z is not in a boundary 3-face, so w_p = 1.

First equality. Proposition W with B' = B and kappa_p(B, B) = 2 kappa_p(B) (Section 3 (ii)): E[X_c(B)^2] = E[direct term];
and E[X_c(B)] = 0, so E[X^2] = Var. Correct.

The four corner cases, recomputed. For each of the 6 planes (mu, nu), z is one corner of 4 plaquettes:
- Base x = z: B_1 = B_4 = - a, B_2 = B_3 = 0. Vanishes identically (Section 2 (b)).
- z = x + mu: B_1 = + a (head z), B_2 = - a (tail z), B_3 = B_4 = 0. a_1 = a, a_2 = - Ad(U_1) a. Gauge transformation h at z:
  U_1 -> U_1 h^(-1), U_2 -> h U_2, U_p invariant (z is not the base), a_1 invariant, a_2 -> - Ad(U_1) Ad(h^(-1)) a.
- z = x + nu: B_4 = + a (head z), B_3 = - a (tail z), B_1 = B_2 = 0. a_3 = Ad(T_3) a with T_3 = U_1 U_2 U_3^(-1), a_4 = - Ad(U_p) a.
  Gauge h at z: U_3 -> h U_3, U_4 -> U_4 h^(-1), so T_3 -> T_3 h^(-1), U_p invariant; a_3 -> Ad(T_3) Ad(h^(-1)) a, a_4 invariant.
- z = x + mu + nu: B_2 = B_3 = + a (both heads z), B_1 = B_4 = 0. a_2 = Ad(U_1) a, a_3 = - Ad(T_3) a. Gauge h at z: U_2 -> U_2 h^(-1),
  U_3 -> U_3 h^(-1), so T_3 is INVARIANT and a_2, a_3 are both invariant: the gauge transformation at z does nothing
  here. The one that works is at x + mu (a neighbour of z, so interior): U_1 -> U_1 h^(-1), U_2 -> h U_2, T_3 and U_p
  invariant, a_2 -> Ad(U_1) Ad(h^(-1)) a, a_3 invariant. (At x + nu also works.)

Gauge-averaging step. In each non-base corner exactly two a_i are non-zero, |a_i| = |a_j| = 1, so the direct term is
t_p (2 + 2 a_i . a_j) + (+-)[a_i, a_j] . s_p. For a gauge transformation at an interior site s other than the base, the law,
t_p and s_p are invariant, a_j is invariant and a_i = M Ad(h^(-1)) a with M fixed; int over SO(3) of Ad(h^(-1)) a dh = 0, and both
the cross term and the bracket are linear in a_i. So each non-base corner gives 2 beta_p E[t_p], for every (c, omega, beta).

Count. 6 planes x 4 corners = 24 plaquettes at z; 6 are based at z and give 0; 18 give 2 beta_p w_p E[t_p]. In a
homogeneous interior (beta_p = b, w_p = 1, E[t_p] the same at the 18) the value is 2 x 18 x b E[t_p] = 36 b E[t_p]. Correct
(L300-302). Arithmetic against the GUIDE table of 4.8: 36 x 1.0 x 0.2436 = 8.77, 36 x 2.3 x 0.6088 = 50.41,
36 x 2.6 x 0.6706 = 62.77, as tabulated (consistency of the table only; it decides nothing).

Defect 1 (proof text, L308-310; does not break 4.7). "the two links at z have transported colours that differ by
Ad of a link variable ending at an interior site; averaging over the gauge transformation at that site": at the
corner z = x + mu + nu the colours differ by Ad(U_2 U_3^(-1)), a two-link transport through z, and the gauge
transformation at z leaves both colours invariant. The averaging site must be x + mu (or x + nu), the head of U_1
(or of U_4). Repair (checked above): use the site x + mu, which is interior because it is a neighbour of z. The value
and the count are unchanged.

Scope of the "Meaning" paragraph (L312-318; reading, not under W1). SEAG proves the identity for the interior field
a d lambda, whose boundary data are 0 and whose H_c is 0. It does not by itself prove that "drop the covariance" fails
for every extension of a non-zero boundary field: by A (ii) the direct term depends on the extension, and the zero
extension of the zero field has direct term 0. So "the start bound is not 'drop the covariance' even at the trivial
pin" (L312, 9.2 item 2, RESULT) is proved for fixed-colour extensions of the form a d lambda, and is a reading for an
optimal extension. 4.7's FAIL of (M3) on C_b does not need it: B' already proves that no classical start bound holds
uniformly on C_b, by any method. Verdict: CORRECT-NO-ADVANCE (the identity is right and new to the lane, but the
verdict of 4.7 rests on B'; SEAG's own consequence beyond B' is the reading above).

No WRONG in (iii)-(iv). Continue.

## 5. Step 5: (v) Lemma CEN, Corollary CEN2; (vi) Lemma EMB against OpenAI's p. 13

### (v-1) Lemma CEN (row 1011 L263-276). CORRECT-NO-ADVANCE.

Re(X U) = Re(X' U) for all unit U forces X = X': Re(x y) is the R^4 inner product of x with conj(y), and the conjugates of
unit quaternions span H. By cyclicity of Re, t_p(hU) = Re(U_1 X) with X = h_2 U_2 U_3^(-1) h_3^(-1) U_4^(-1) h_4^(-1) h_1, and
t_p(U) = Re(U_1 X') with X' = U_2 U_3^(-1) U_4^(-1). So X = X' for all U_2, U_3, U_4 (L269). U_2 = U_3 = U_4 = 1 gives
h_2 h_3^(-1) h_4^(-1) h_1 = 1; with U_3 = U_4 = 1 this turns X = X' into h_2 U_2 h_2^(-1) = U_2 for all U_2, so h_2 = +-1.
"The other links are the same": done here for h_3 by isolating U_3^(-1) instead of U_1: Re(U_3^(-1) h_3^(-1) U_4^(-1) h_4^(-1) h_1 U_1 h_2 U_2)
= Re(U_3^(-1) U_4^(-1) U_1 U_2) for all U; U_1 = U_2 = U_4 = 1 gives h_4^(-1) h_1 h_2 = h_3, and then h_3^(-1) U_4^(-1) h_3 = U_4^(-1)
for all U_4, so h_3 = +-1; h_1 and h_4 likewise by isolating U_2 and U_4^(-1). With all h_l = +-1 the relation becomes
h_1 h_2 h_3 h_4 = 1. Correct as written; the phrase "the other links are the same" needs the cyclic rotation shown
here, which is routine.

The remarks after it (L272-276). A central link field h with values +-1 gives t_p(hU) = (h_1 h_2 h_3 h_4) t_p(U), so a
non-closed h flips the signs of the strengths by the exact two-cochain dh: these are the signed strengths of the
class. On a box, H^2(B^4, S^3; Z_2) = H_2(B^4; Z_2) = 0 (Lefschetz duality), so every closed Z_2 two-cochain relative to
the boundary is exact, and its h is absorbed by a change of variables inside and a change of pin on the boundary.
Correct. Why no advance: the lane had the content as a remark (row 712, `gap-crux-fp.md` L88); this is its
elementary proof.

### (v-2) Corollary CEN2 (row 1011 L278-288). CORRECT-NO-ADVANCE.

With M = h_2 U_2 U_3^(-1) h_3^(-1) U_4^(-1) and M' = U_2 U_3^(-1) U_4^(-1), cyclicity of the trace gives
Re tr(rho(U_1) Y) = 0 for all U_1 in G, Y = rho(M h_4^(-1) h_1) - rho(M'). rho unitary gives Y* = rho((M h_4^(-1) h_1)^(-1)) - rho(M'^(-1)), so
tr(Y* Y) = tr(rho(A) Y) - tr(rho(B) Y) is real, and its real part is 0 - 0 = 0. So Y = 0, and faithfulness gives
M h_4^(-1) h_1 = M'. The rest is Lemma CEN with "commutes with every U_2" giving h_2 in Z(G), and the other links by the
same cyclic rotation. The closed relation h_1 h_2 h_3^(-1) h_4^(-1) = 1 holds in the abelian group Z(G). No use of
connectedness: it holds for finite G too, as the Q_8 / 2T test of row 1011 Section 6 uses. Correct.

Scope of the reading "no Wilson lattice gauge theory has a link twist that is an exact symmetry on every
configuration and also has a bracket term" (L281-283): the lemma is about configuration-independent LEFT multipliers,
the form in which a boundary field acts (e^(eps B) U). Two-sided multipliers h_l U_l k_l were checked here too (same
argument at each corner, with the corner products k_1 h_2, k_2 k_3^(-1), h_3^(-1) k_4^(-1), h_4^(-1) h_1 in place of the h's): each corner
product must be central, so a two-sided symmetric multiplier is a gauge transformation times a central field, and
gauge transformations do not change F_c at any order. So the reading holds in that wider form as well. It is a
necessary condition on THIS engine (a symmetric twist on every configuration), as row 1011 9.6 says, not a statement
about the wall (W).

### (vi) Lemma EMB against p. 13 of OpenAI's O(4) paper (row 1011 L320-342). CORRECT-NO-ADVANCE.

Source read: OpenAI, "Sharp mass bounds for the two-dimensional O(4) model" (posted, unrefereed), github.com/openai/math
at commit 4eaee87548250b2682affda7d05d947c05554bae, `preprints/Sharp-mass-bounds-for-the-two-dimensional-O4-model-September-23-2026/paper.pdf`,
fetched 2026-11-15 into a new empty folder `/tmp/row1014-src.UwovzH/` (102 pages; text of p. 13 extracted with
PyMuPDF by a script kept in a separate folder). What p. 13 says, in short: Section 3.1 "Local class and Ward
identities"; Q(S) = {0, ..., S}^2 with all boundary spins fixed; for each positively oriented edge e = x -> y,
t_e + s_e = q_y U_e q_x^(-1) with U_e any fixed unit quaternion; signed coefficients |b_e| <= b <= B with w_e = b_e except
w_e = b_e/2 on edges tangent to the boundary; density Z^(-1) exp(sum_e w_e t_e); (3.4) X_Q, H_Q; (3.5) H_Q <= b I "valid
with signed coefficients and twists"; (3.6) under q_x -> e^(a f_x) q_x, D_f^2 A = sum_e w_e t_e (f_y - f_x)^2; (3.7) the bracket
D_eta s_e = t_e (eta_y - eta_x) + (eta_y + eta_x) x s_e.

Interior links. In c = {0,1,2} x {0,1} x {0..S}^2 the boundary 3-faces are x_0 in {0, 2}, x_1 in {0, 1}, y_j in {0, S}.
Links in directions 0, 2, 3 keep x_1 in {0, 1} fixed, so lie in a face. A direction-1 link (x_0, 0, y) -> (x_0, 1, y) lies
in a face iff x_0 in {0, 2} or y is on the boundary of the square. So the interior links are exactly q_y = U_1(1, 0, y),
y in the open square, and the q_y with y on the boundary of the square are pinned (L322-324). Correct.

Plaquettes that see the q_y. A direction-1 link at x_0 = 1 lies in plaquettes of the planes (0,1), (1,2), (1,3) only.
The (0,1) ones get strength 0. For k = 2, 3 the plaquette based at (1, 0, y) has l_1 = q_y, l_2 = u_k(1,1,y), l_3 = q_(y+k),
l_4 = u_k(1,0,y), so U_p = q_y u_k(1,1,y) q_(y+k)^(-1) u_k(1,0,y)^(-1); with the trivial pin on x_1 = 0, t_p = Re(q_y u_k(1,1,y) q_(y+k)^(-1))
= Re(q_(y+k) u_k(1,1,y)^(-1) q_y^(-1)) (Re z = Re z^(-1) for unit z). This is OpenAI's t_e for the edge y -> y + k with
U_e = u_k(1,1,y)^(-1), a pinned link of the face x_1 = 1 (L330-332). Correct. (U_p is the inverse of OpenAI's bond
quaternion, so s_p = - s_e; only t enters the density, so the law is the same.)

Weights. Such a plaquette (x_0 = 1, x_1 varying, y_k varying) lies in a boundary 3-face iff y_j in {0, S} for the other
direction j, that is iff the edge is tangent to the boundary of the square; then it lies in exactly one face, shared
with one neighbouring cell of the tiling by translates of c, so w_p = 1/2; otherwise w_p = 1. This is OpenAI's half
allocation. Correct.

Every member arises. Given OpenAI's data (S, boundary spins, U_e, b_e): pin q_y (y on the boundary of the square) to the
boundary spins, u_k(1,1,y) = U_e^(-1), u_k(1,0,y) = 1, other pinned links arbitrary; beta_p = b_e on the (1,k) plaquettes at
x_0 = 1 and 0 elsewhere. Signed strengths are needed for signed b_e (the row says "signed if allowed"). Correct.

The twist. B = a f(y) on the direction-1 links acts by q_y -> e^(eps a f(y)) q_y, which is OpenAI's rotation q_x -> e^(a f_x) q_x
on p. 13, including the fixed boundary spins (consequence (a), L334-336). Correct. Consequence (b): with a pure-gauge
pin u_k(1,0,y) = h_y h_(y+k)^(-1), Re(q_y u q_(y+k)^(-1) h_(y+k) h_y^(-1)) = Re((h_y^(-1) q_y) u (h_(y+k)^(-1) q_(y+k))^(-1)), so q -> h^(-1) q
works; with a general pin the bond is two-sided. Correct. (c), (d) are readings; not checked beyond this.

Side check of row 1011's (M2)-(M3) against the same page: (3.6) gives the classical direct cost and (3.5) the free
start bound H_Q <= b I, valid with signed couplings and twists, as row 1011 Section 2 states.

Why no advance: the layer idea is on file (Durhuus and Frohlich through rows 712, 825, 977); this is its exact match
with OpenAI's class, with no consumer on the path of (W) (the row says so, L342, 9.5).

## 6. Step 6: (vii) Lemma FR (row 1011 L460-484). CORRECT-NO-ADVANCE.

Covariance of D. Under omega_l -> g_tail omega_l g_head^(-1), n_x -> Ad(g_x) n_x: D_l n -> Ad(g_tail) n_tail - Ad(g_tail omega_l g_head^(-1)) Ad(g_head) n_head
= Ad(g_tail) D_l n. Gauge covariant in the tail frame, as stated.

Telescoping, written out (the row gives one line). With omega_p = omega_1 omega_2 omega_3^(-1) omega_4^(-1):

  n_x - Ad(omega_p) n_x = D_(l_1) n + Ad(omega_1) D_(l_2) n - Ad(omega_1 omega_2 omega_3^(-1)) D_(l_3) n - Ad(omega_p) D_(l_4) n,

term by term: [n_x - Ad(omega_1) n_(x+mu)] = D_(l_1) n; Ad(omega_1)[n_(x+mu) - Ad(omega_2) n_(x+mu+nu)] = Ad(omega_1) D_(l_2) n;
Ad(omega_1 omega_2)[n_(x+mu+nu) - Ad(omega_3^(-1)) n_(x+nu)] = - Ad(omega_1 omega_2 omega_3^(-1)) D_(l_3) n; Ad(omega_1 omega_2 omega_3^(-1))[n_(x+nu) - Ad(omega_4^(-1)) n_x]
= - Ad(omega_p) D_(l_4) n. The four brackets telescope to n_x - Ad(omega_p) n_x (the intermediate terms cancel in pairs), and
each term is a rotation of one D_l n, so |(1 - Ad(omega_p)) n_x| <= sum_i |D_(l_i) n| by the triangle inequality.

Rotation identity. omega_p = cos phi + s^ sin phi, s_p = s^ sin phi; Ad(omega_p) is the rotation by 2 phi about s^, so
|(1 - Ad(omega_p)) n| = |n_perp| |1 - e^(2 i phi)| = 2 |sin phi| |n_perp| = 2 |s_p x n|. Correct (L465, L471).

Squaring and summing. (sum of four)^2 <= 4 sum of squares gives |s_p x n_x|^2 <= sum over the four links of p of |D_l n|^2.
Each plaquette has one base, so summing over x and the plaquettes based at x is summing over all plaquettes; a link
in direction mu lies in 2 plaquettes of each plane (mu, nu), nu != mu, so in at most 6 in d = 4. Hence
sum_x sum_(p based at x) |s_p x n_x|^2 <= 6 sum_l |D_l n|^2, and the left side is at least sum_x lambda_x(omega) = NA(omega).
So sum_l |D_l n|^2 >= NA(omega)/6 for every unit frame n. Correct.

Defect 2 (wording, L479; does not break anything). "NA(omega) is zero only when all plaquette axes at each site are
parallel (an abelian pin)": the "only when" is right, but NA = 0 is the site-local condition that the axes of the
plaquettes BASED at each x are parallel to one n_x, which may change from site to site. An abelian pin (all links in
one maximal torus) has NA = 0; the converse fails. Repair: read "(for instance an abelian pin)". The "Use" and
"ARGUED size" lines that follow are labelled reading/ARGUED and are not part of W1 (the sign in "Use" is test (c),
PASS). The order count in "ARGUED size" (mass-like part of order theta^2 per site after b x (1/b); against b f^2 S^4 it
wins once S^2 > b) is consistent arithmetic of an ARGUED estimate, not a proof.

Why no advance: an elementary inequality, new to the lane, with no consumer (the row's (N1)-(N3) are not attacked).

## 7. Step 7: the two corrections of row 1009 (row 1011 Section 5, L413-418)

Anchors checked: row 1009 = `library/prior/gap-o4-pinned-cell-read-opus.md` at f4dd47b82; L387-390 is Step 6 note (i),
L406 is Step 7 table row 3. Both citations of row 1011 point at the right lines.

### Correction 1 (row 1009 L406, row 3, analogue column). UPHELD, with a narrower reach than its wording.

Row 1009 wrote: an SF form "1/g-bar^2 <= the bare value times the classical action" "would follow the same way by
dropping a variance". Row 1011: "It does not: by Proposition SEAG the direct term is not classical, at any pin."

Judgement. "The same way" in 2D is: H <= E[direct term], and the direct term is bounded configuration by
configuration by b times the classical cost ((3.5), (3.6) on p. 13: |t_e| <= 1 and the cost is (f_y - f_x)^2). In the gauge
cell, dropping the variance is still valid for every configuration-independent extension B~ of the boundary field
(A (ii)): H_c <= E[direct(B~)]. What fails is the second half: the direct term t_p |delta_p|^2 + kappa_p . s_p is built from
adjoint transports by fluctuating links, and SEAG proves, at every pin and every strength field, that a fixed-colour
curl-free field has E[direct] = 2 sum over 18 plaquettes of beta_p w_p E[t_p] > 0 while its classical action is 0. So the
one-line route of row 1009 does not exist, and the correction stands as a correction of that route.

Its reach (narrowing, not a defect of the verdict): SEAG proves this for the interior field a d lambda, whose boundary
data are 0. That dropping the variance fails for EVERY extension of a non-zero boundary field (including an optimal
one) is not proved in row 1011; it is a reading (row 1011 4.4 "Meaning"). The SF bound itself, at the trivial pin and
homogeneous strength, is neither proved nor refuted: row 1011 keeps it OPEN (L316-318, 9.7), which is the right label.
Suggested wording: "It does not follow by that route: by Proposition SEAG the direct term of a fixed-colour field is
not classical, at any pin; whether the SF bound holds is OPEN."

### Correction 2 (row 1009 L387-390, Step 6 note (i)). UPHELD, with the same precision.

Row 1009 wrote that the pinned-cell supremum "is an UPPER bound on a response, which is the direction a supremum over
pins can keep", and left open whether Theorem D2 binds a gauge form. Row 1011: for SU(2) the supremum over pins of the
response to a fixed-colour field is not bounded by the classical action (Proposition B'); the binding fact is gauge
covariance, not Theorem D2.

Judgement. Read literally, an upper bound is always keepable on a finite cell (for fixed c and b, H_c(omega; B) is
bounded over the compact set of pins), so row 1009's sentence is not false as a statement about finiteness. What the
iteration needs is the scale-free form "sup over pins of H_c <= h x classical action", and that is what B' refutes: PROVED
for the class with all strength profiles (no constant at all, by the closed theta of Section 4 (iii-2)), with the growth
of the best constant like b S ARGUED. The mechanism is Proposition B (the pin supremum is blind to site-wise colour
rotations), so "the binding fact is gauge covariance" is right. On D2: this check did not re-read Theorem D2; it agrees
that B' binds the cube class without D2, and accepts row 1011's reading that D2's sheets need interior pins or thin
boxes (Lemma EMB (d)) as a reading, not checked here.

Both corrections were marked "ARGUED until checked" by row 1011. After this check: correction 1 holds as a correction
of the method (its consequence for an optimal extension stays a reading); correction 2 holds for the classical
normalisation, PROVED through B'.
