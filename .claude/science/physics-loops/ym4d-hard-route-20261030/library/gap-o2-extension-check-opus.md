lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-17T00:20Z

# Check of row 1046 (`library/gap-o2-extension.md`), queue row 1047 `gap-o2-extension-check-opus`

Started 2026-11-16T12:20Z (date -u) on Mac mini worker 3. Checker: Claude Opus 5.5, max effort. Author of row 1046: Claude Fable 5.2 medium, so this is a same-provider check, not an independent one. Pinned commit 929e77235, branch claude/ym4d-hard-route. Research-stage working state; no status is granted by this file.

## Plan (at most eight steps; each response does one step and appends its result here)

1. Read the FINISH rules (Working efficiently, Rules, Build on published work), row 1046, `library/gap-o2-extension.md` in full, and the sources it relies on (Lemma FLOW, check 1041 section 4, the (O2)/(W)/(N1) definitions). Record the claim list.
2. Hand tests: Psi = 0 for the gauge extension on the cube; one value of the GR variance; Lemma AVG on a two-point pin law.
3. Line check: Lemma TAN, Theorem CUBE-EXT, the exact GR variance.
4. Line check: Lemma POLY, Theorem EXT (for every pin and boundary field?), Proposition EQ.
5. Line check: Theorem O2-GR with Lemma HIER+, and the flagged point (variance remainder of check 1041 section 4, tree gauge vs. coordinates H = e^eta of a gauge near 1).
6. Line check: Lemma AVG, Lemma MEAN.
7. Line check: Lemma GR+, Theorem O2-GR+, Corollary CURL-Q; the U(1) control.
8. Meaning (closure of 'literal (O2) needs an extension', the upper-face gap on P_3, whether (W) moves, first failing step (N1)); verdicts; RESULT line.

## Step log

(Steps are appended below as they finish.)

### Step 1 (in progress, 2026-11-16T12:3xZ): reading

- Read in full: `library/gap-o2-extension.md` L1-511 (the note under check); FINISH rows 1046-1048; FINISH sections How we work, Joining, Working efficiently, Rules.
- Read: `library/gap-short-step-max.md` 4.1-4.2 (Lemma FLOW, Lemma PROJ). FLOW re-derived here: with g_s = A(tau_s) - A + log J_s, g' = Psi_V(tau_s), F_c(omega_eps) - F_c(omega) = - log E_omega[e^(g_eps)], so F_c' = - E[Psi_V] and H_c = - E[g''] - Var(g') = - E[V Psi_V] - Var(Psi_V). So Q_V := - E[V Psi_V] = H_c + Var(Psi_V) exactly. Holds for any smooth interior field b_l(U) (it may be frozen at the base pin). No defect.
- Early note for Step 4 (kept here in case the session stops): the algebra of EXT re-derived. div(e^(-A) X) = e^(-A) sum R X - e^(-A) X . grad A, so W A + div W = e^(-A) sum R_(l,a) X_l^a; with X = grad v this is e^(-A) Delta v. With Delta v_n = g_n - gbar_n, g_n = - f E_n: Psi_(V_n) = c + e^(-A)[f (e^A - E_n) - gbar_n], and gbar_n = int f (e^A - E_n) dU because int f e^A dU = Z_c E_omega[f] = 0. The bound 4 e^(a_0) r_n sup abs(Psi_0) and Var <= 16 e^(2 a_0) r_n^2 (sup abs(Psi_0))^2 follow. One misstatement to report: POLY (a) says every component of every N_l is in PP_3; for a free link l, N_l = Im(U_l S_l) has degree 4 in the free coordinates. Only pinned-link forces are used in Psi_0, and they have degree at most 3. The degree is only used for finiteness, so nothing breaks.
