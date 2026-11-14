lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-14T16:07Z

# gap-seam-max (row 929): the U(1) fact test for (SEAM), then the SU(2) attack

Provenance: Claude Fable 5.2, max effort, Mac mini worker, pinned at commit 5be5e895d of
`claude/ym4d-hard-route`. Author lane, not a check. Research-stage working state; nothing here is a
public claim and nothing here grants status. Statements are marked PROVED, CONDITIONAL (on named
inputs), GUIDE (numeric or heuristic, never a proof step) or OPEN.

## 0. Plan (at most eight steps; one step per response, appended before the next)

1. Read row 929's inputs in full: `library/gap-glue2-opus.md` (row 920) and
   `library/gap-glue2-check-astra.md` (row 921). Write the exact statements used here (INS, (SEAM)_a,
   Delta_theta, S_ev, the threshold, C1-C3, (I1)-(I3)) into Section 1.
2. Repo search and duplicate check (rule 0a, Repo first): grep `library/open-core.md` and the FINISH
   rows for (SEAM), (I1)-(I3) and the U(1) endpoint; list what is already covered. Section 2.
3. STEP A, set-up: write the Gaussian U(1) model (Villain or noncompact) on the same box and time
   extent, with the same twist/sector definitions, and derive S_ev and Delta_theta in closed form.
   Section 3.
4. STEP A, values: evaluate the exact S_ev, Delta_theta at theta = 0, 1 and an interior theta, and
   the threshold; settle "a^-4 law against a^-3 threshold" by hand, with a numeric GUIDE only as a
   cross-check. Verdict: does U(1) fail (SEAM), where, by how much. Section 4.
5. If U(1) passes (SEAM) at some size: the corrected crux form that U(1) fails. Section 5.
6. STEP B: attack (SEAM) (or the corrected form) for SU(2) Wilson at beta 2.3-2.6, or the weakest of
   (I1)-(I3) that suffices; the proof must use a property U(1) lacks and show the exact step where
   the photon breaks it. Section 6.
7. Binding checks: frozen Q_8 and 2T (check 896 D6), ceilings 2/3, 0.775, 4G_3 = 1.0109. Section 7.
8. Result table and the RESULT line. Section 8.

Status of the plan: step 1 in progress (file created 2026-11-14T04:07Z).

## 1. Inputs read (step 1; READ = read at the pinned commit, not re-proved here)

Read in full: `library/gap-glue2-opus.md` (row 920, Claude Opus 5.5, 304 lines) and
`library/gap-glue2-check-astra.md` (row 921, Codex gpt-6-astra, 232 lines).

Objects (row 920 Sections 4.1-4.4, check 921 Sections 1-4, all HOLDS there).

- Box: spatial b^3 periodic, time a, b = 24a. T = e^(V/2) K e^(V/2) the Wilson transfer operator,
  lambda_0 its simple top eigenvalue, Omega its vacuum, psi = e^(V/2) Omega. P_0 = average of the 8
  centre flips. Z_0(t) = Tr(T^t P_0) = lambda_0^t (1 + S_ev(t)).
- Seam kernel K_theta: the last slices (U, W) of copies 1, 2 are joined to the first slices (U', W')
  with weight exp(beta sum_l [(1-theta)(x_A1 + x_A2) + theta (x_B1 + x_B2)]); A1 = (U,U'), A2 = (W,W'),
  B1 = (U,W'), B2 = (W,U'). delta_l = x_A1 + x_A2 - x_B1 - x_B2 on one spatial link l.
- Z_theta(a) = Tr(T^(a-1) P_0 Nt_theta), Phi_theta = <psi x psi, K_theta psi x psi>; Z_theta(a) =
  lambda_0^(a-2) Phi_theta E_theta^inf[rho], rho = pbar_(a-1)(U', U).
- (INS): log(1 + S_ev(a; b^3)) = 3 b^3 beta int_0^1 Delta_theta dtheta,
  Delta_theta = E_theta^(a)(delta_l) - E_theta^(inf)(delta_l). The reference part integrates to zero
  (Phi_0 = Phi_1), not pointwise.
- (SEAM)_a: sup_theta |Delta_theta(a; 24a)| <= psi_*(a, beta) := log(1.1)/(3 beta (24a)^3).
  Sufficient for (GLUE-FP)_a: S_ev(a; (24a)^3) <= 1/10. The SIGNED theta-average of Delta at most
  psi_* is necessary and sufficient (check 921 Section 4). No converse to the sup.
- Lemma E: Delta_0 = u^t_(a,ev) - u^t_inf (thermal shift of one time-like plaquette), Delta_1 = 0.
  Proof uses the compact gauge average of the mismatched plaquettes.
- Lemma V: d/dbeta_t log(1 + S_ev) = 3 a b^3 Delta_0 at beta_t = beta_s.
- C1: Delta_theta = Cov_theta^inf(delta_l, rho)/E_theta^inf(rho). C2: |Delta| <= 8 d_TV <= 4 sqrt(chi2)
  of one link's seam variables. C3 with (I1) slab clustering in L^2, (I2) spatial localization in L^1
  under BOTH laws, (I3) local chi-square distance of ring and vacuum SEAM marginals (check 921
  Section 8: the reference of (I3) is the seam law, not nu x nu).
- Check 921 Section 12.1 (the point of row 929): from Lemma E only sup_theta |Delta| >= |Delta_0|;
  with a GUIDE law |Delta_0| = C a^-4 the ratio to psi_* is 3 beta 24^3 C/(L a), L = log 1.1, which
  tends to 0. So the exponent alone shows no U(1) failure. "This does not prove that U(1) satisfies
  GLUE or SEAM: an interior theta value, or the exact thermal trace, could still refute them."
- Check 921 Section 12.2: frozen Q_8, 2T fail (SEAM) at each fixed box for large finite beta
  (S_ev >= 1/2 from check 896 D6 plus the necessary average).

Status of the plan: step 1 done. Step 2 (repo search, duplicates) next.
