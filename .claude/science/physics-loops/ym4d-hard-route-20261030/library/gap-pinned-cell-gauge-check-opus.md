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
