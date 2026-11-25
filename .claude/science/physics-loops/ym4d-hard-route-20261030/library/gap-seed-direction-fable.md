lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T16:32Z

# gap-seed-direction-fable (queue row 1515): direction for the physical seed after rows 1510 and 1511

Status: IN PROGRESS. Research-stage working state; nothing here is a public claim. Unchecked.
Pinned at commit c4db00930 on branch claude/ym4d-hard-route. Started 2026-11-25T04:32Z (date -u).

## 0. Plan (written first, per the save protocol of the row)

Task of the row: from the target (PUR-io) and the results of rows 1510 (`library/gap-seed-solve-fable.md`)
and 1511 (`library/gap-seed-solve-astra62.md`), find the attack that could still succeed, or prove that every
attack of an explicitly stated family fails. Decide what kind of input the calibrated obstruction of row 1511
still allows:

- (a) scaling of the action insertion,
- (b) cancellation between signed seam responses,
- (c) rates integrated over shrinking coupling intervals,
- (d) an in-law carry as in row 1510 (PC, REV),

and whether any of these has a first lemma that is not equivalent to a closed line.

Steps, each appended as its own section when done:

1. Read rows 1510 and 1511 in full; restate (PUR-io), the refutation of (W), criterion (3) and the calibrated
   obstruction in the exact form used below, with line anchors.
2. Formalize the family of attacks the obstruction covers, and state precisely what it leaves outside.
3. Test each of (a)-(d) against the obstruction and against the closed lines (grep `library/open-core.md` and
   the FINISH rows before calling anything new).
4. Decisive outcome: one named attack row with its first lemma, or an obstruction theorem over a stated family,
   or the statement that no such row exists on present knowledge, with triggers.
5. Next two rows with their decisive outcomes.

## Status log

- 2026-11-25T04:32Z file created with plan; no reading done beyond the queue row and GOAL.md.
- 2026-11-25T04:39Z read rows 1510 and 1511 in full, FINISH rules, row 1496 Sections 2-4, row 708 Section 4 (L112-200), row 1461 first lemma and (1)-(2). Section 1 written.
<!-- LOG-MARKER -->

## 1. The target and the two results, in the form used below (read; nothing new here)

Written 2026-11-25T04:39Z (date -u). Labels: **proved** (a written proof is in this file), **read** (read in a row, not
re-derived), **sketched**, **guessed**, **guide** (heuristic size, never a proof step).

### 1.1 Target (read: row 1468 3.1, checks 1462, 1465; row 1511 "Physical target")

n = l b^K, u = n/512, T the Wilson transfer operator on the spatial torus n^3 at the least-root coupling
beta_K(g_0), Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2. **(PUR-io):** P_K >= 457/625 at infinitely many K
for one l and one g_0.

### 1.2 Three exact forms of the same number (read; elementary)

With r_i the neutral eigenvalue ratios and s(v) = sum of r_i^v:

- (E1) -log P_K = 2 log(1 + s(u)) - log(1 + s(2u)).
- (E2) -log P_K = 12 u n^3 * integral over t in [0, beta_K] of (x_u(t) - x_2u(t)) dt, where x_v(t) is the
  mass-weighted mean plaquette of the n^3 x v tori at coupling t (the proof of (4) in row 1511; rows 1461
  and 1465, Step 6; P(0) = 1).
- (E3) the same with the infinite-time torus as reference: d/dt log(1 + s(v)) = 6 v n^3 (x_v - x_inf)
  (row 708, `gap-mid-max.md` Lemma 4.1, L112-116, in that row's sign convention).

### 1.3 Row 1511 (gpt-6.2-astra; unchecked, check 1514 running)

- **(W) refuted.** Bound (1): delta >= 3 [1 - ((R-1)/(R+1))^3] m_beta. At beta = 23/10 and side four it
  forces delta > 392/225. Every cube with R <= 10 fails at every beta >= 23/10.
- **Criterion (3).** With the cost counted modulo vertex gauges on the cube, C_i < N_R + b_i gives decay of
  gauge-invariant correlations with rate lambda and prefactor 2 N_R |Y| |V| e^(lambda (R+2)) / L. At R = 4
  the test is C_i < 1350: the sum of 796 excess costs below 554. Open.
- **Bound (4).** Under a common margin on [0, beta_K]:
  -log P_K <= 768 beta_K u n^3 N_R |V| e^(-lambda D) / L, D = (u/2 - R - 4)_+.
- **Calibrated obstruction.** (i) Rate bound: an actual uniform periodic covariance rate lambda_K at the
  least roots has lambda_K b^K bounded (reflection positivity removes the prefactor; the positive separated
  two-point witness of row 1461 forbids an unbounded physical rate). (ii) Hence the right side of (4), and
  every majorant bounded below by a_K e^(-c lambda_K n) with a_K -> infinity, diverges at the calibrated
  roots. Its last paragraph names three features a physical comparison could use: the scaling of the action
  insertion, cancellation between the signed seam responses, rates integrated separately over shrinking
  coupling intervals.

### 1.4 Row 1510 (mine; unchecked, check 1513 queued)

Proposition PC (a weighted Poincare inequality passes fine to coarse through one Q2 step, in law), Lemma REV
(coarse to fine, given (H1), (H2) for the posterior), Corollary NF and Theorem NB (weak steps give every
family a Poincare constant above 3/2 and keep the sixteen masses), and the unproved (FL). Its own verdict:
PC and REV both transport a gap; neither makes one.

### 1.5 First reading (the dictionary that the rest of this file uses)

(E2) is the transport of the thermal sum along the coupling on a fixed lattice. This is on file: row 708
(`gap-mid-max.md` Section 4: Lemma 4.1, Theorem TR, (VIR_K), Remark LEV, (DEF_K), (VIR-log)), with the
verdicts "three ways failed" (its 4.4) and "the trace anomaly has no lattice form" (its 4.5); the table of
row 1380 (`gap-mech-direction2-fable.md` L258) lists it as blocked-equivalent; row 1496 4.1 lists "integration
along beta at a fixed lattice" as equivalent to a closed line. So row 1511's (4) is one bound for the
integrand of row 708's transport, and the three features named in 1.3 are three ways to bound that
integrand. Sections 2-4 test them one by one against row 708, and Section 5 tests the in-law carry.

<!-- APPEND-MARKER -->
