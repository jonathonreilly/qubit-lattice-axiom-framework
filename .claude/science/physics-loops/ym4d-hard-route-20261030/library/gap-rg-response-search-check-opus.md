# Check of row 1430 (gap-rg-response-search-astra62.md), FINISH row 1431

lead: anthropic/claude-opus-5-5/high laptop-subagent (row 1431)
Start: 2026-11-23T01:58:26Z (date -u)
File checked: library/gap-rg-response-search-astra62.md (author gpt-6.2-astra).
Research text only. No status is granted.

## Plan

1. Read row 1430 in full, then the parts of rows 1418, 1421, 1424, 1425 it uses, and row 1386 section 4.5.
2. Decide the lead's flag first: (a) new coefficient or relabelled E_4 T; (b) is the reference natural; (c) does it count under "Equivalent is not progress" and the 4.5 filter.
3. Check: frozen class and acceptance rule; symmetry reduction; Taylor screen; same-vacuum reference; band table (recompute from logs, rerun what fits); 5D bound 2 g_5 >= 1.8278.
4. Read scratch code before running; copy to a fresh folder; run with python3 -I only.
5. Ranked defects, outcome paragraph, RESULT line.

## Steps

### Step 1. Sources read

Read in full: row 1430 (204 lines). Read the parts used: row 1425 (frozen response, conditional bound, torus contraction, circle bound, final table); row 1424 (7) and the product subtraction (5); row 1386 sections 4.1 to 4.5; the lane rule "Equivalent is not progress" (FINISH.md line 350). Check 1429 of row 1425 exists and reports HOLDS for E_4 T in [-2054,-1829]/1e11. I rely on that check for the sign of E_4 T and do not redo it.
Digests in row 1430's SHA256SUMS all match the files in its scratch folder (shasum -c, 15 of 15 OK).

### Step 2. The lead's flag, decided first

Exact checks for this step are in my scratch script `alg.py` (exact rationals). Re-derived by hand: the strip contractions, the reference average, and the identities below.

**(a) Is the crossed response a different coefficient? No. It is the same scalar E_4 T with a positive prefactor.**
Every label in row 1430's class, and both ring labels of row 1424 (7), is a linear form c1 E(h.k)^2 + c2 E W on the same two-dimensional space of joint moments. The per-square reference replaces (h.k)^2 by W/3. So for every such label
  Y - R = c1 E T,  R = (c1/3 + c2) E W.
The label sets only the sign of c1 (c1 + 3 c2). A magnitude decrease holds exactly when c1 (c1 + 3 c2) E T < 0.
- Crossed matching: c1 = 1, c2 = 0, product +1. With E T < 0 it reads as a decrease.
- Alternating ring of row 1425: c1 = 2, c2 = -1, product -2. The same E T < 0 reads as an increase.
- Grouped labels: c1 = 0. No change.
The row itself states g_alt + 2 g_d = 3 (line 84). I checked it exactly. This identity says the two verdicts are one fact: E(h.k)^2 < E W / 3. The only quantity new to row 1430 is D = z_4 E_4 W, a sharper denominator. It moves the size of 1 - g_4, not its sign. Row 1430's own coarse route (line 155) gets the sign from row 1425's numbers alone.
Since E_4 T < 0 was known when the class was frozen (line 31), and the class contains a label with c1 (c1 + 3 c2) > 0, the pass was fixed by the label choice before any new evaluation. Verdict: **relabelled moment, not a new signal.**

**(b) Is the reference natural and convention-independent? No. Two other natural references change the verdict.**
- R0, independent conjugation of each copy (each strip) instead of each square. Then the crossed reference is E[(O1 h . k)(O2 h . k)] = 0. A zero reference fails the strict test by row 1430's own rule (line 39). Verdict flips to FAIL.
- R2, the disconnected product: the two squares sampled from their own marginal laws. This is the "product-of-marginals subtraction" of row 1424 (5), the lane's earlier reading of "disconnected". By gauge invariance at the root, E[h h^t] = E|h|^2 I/3, so R2 = a_2 (E|h|^2)^2 / 3 and
  X - R2 = a_2 [E T + Cov(|h|^2, |k|^2)/3].
  The covariance of the two radial parts is a different moment. Row 1430 does not compute it. Its leading strong-coupling term is positive and far larger than |E T| (Step 5 below). Under R2 the crossed coefficient is an **increase**.
- R1, row 1430's choice (one conjugation per square, shared by its copies), keeps the joint radial law and removes only the relative orientation. It is a legitimate isolation of the orientation moment. But it is the reference that makes the coefficient equal to E T by construction. It is not a convention-free baseline for a "decrease".

**(c) Does it count as evidence of a four-dimensional carry? No.**
- Rule "Equivalent is not progress": the row's pass is equivalent to the already known statement E_4 T < 0 (row 1425, check 1429). It adds no new inequality. Under the rule it is no progress as a signal.
- Filter (t1), U(1) zero: the zero is kinematic. A traceless projection on a one-dimensional charge line is zero for every traceless label, whatever the dynamics. It does not separate a gain from a non-gain. Row 1425's ring has the same zero and was rejected.
- Filter (t2), five dimensions: the test 2 g_5 >= 1 + eps passes for any label with |g_5 - 1| < 1/2. Row 1425's ring passed it too (2 g_5 >= 1.311). The factor 2 is put in by hand. It is not the output of a block step. So the test does not discriminate here.
- Remark PAIR (row 1386 4.2): the missing object is a carry, an inequality that moves a gain through an exact block step. A single bare coefficient of one 2^4 block at fixed beta is neither a gain per scale nor a carry. Its relative size, about 1.4e-7, is also far below the rate (h) of 0.173 in beta per doubling.
- Filters (t3) SU(3) and (t4) beta growing at a fixed lattice: not addressed by the row.
**What it would have to do inside a four-direction inclusion to count:** (i) enter an exact block map (input chart to output chart) through a combination fixed by the map, not chosen after the sign of E T is known; (ii) keep a definite sign in that map's residual after the grouped reference, the rotated crossed labels, the exposed triangles and all high spins are added; (iii) give a margin that the map transports to the coarse coupling at a rate comparable to (h); (iv) make the 5D comparison on the step, not on the coefficient; (v) not be equivalent to "E_4 T < 0" under a different label. Row 1430's next row 2 states part of (ii). None of (i) to (v) is shown.

### Step 3. Replays of row 1430's producers

Copied (digests identical to the source folder) into my own scratch folder and run with `python3 -I -B run_local.py ...`. All under 70 MB RSS and under one minute each.
- `matching_bounds.py 512`: output identical line for line to `matching512.log` (13 s).
- `radial.py 28`: `radial28.txt` regenerated, sha256 identical (a6140f71...).
- `matching_geometry.py`, `controls.py`: output identical to `geometry.log`, `controls.log`.
- My variant `radial_var.py` (same geometry kernel `recouple.geom`, my own loop): with the orbit folding switched off, the two-mark table equals `radial28.txt`; the unmarked table equals row 1425's `vacuum28.txt` through degree 28; marking only the P circuit equals marking only the Q circuit. This checks the orbit folding and the P/Q symmetry. It is not independent of the geometry kernel.
These are replays. A rerun of the same code is not an independent check.

### Step 4. Item verdicts

**Item 1. Frozen class and acceptance rule: HOLDS AFTER CORRECTION (read, re-derived).**
The class (nine nonempty matchings of the four root ports) and the rule (reference, phase, band, U(1) zero, 2 g_5 >= 1 + eps) are well defined and were stated before evaluation. First failing line: plan line 23, "Select a finite class outside previously resolved cases". Line 31 records that row 1425's sign was known, and line 84 shows the only live member reuses that moment. Correction: the class is not outside resolved cases; its live member is equivalent to row 1425's E_4 T < 0 (Step 2 (a)).

**Item 2. Symmetry reduction: HOLDS (re-derived; geometry replay identical).**
I re-derived the strip contraction (sqrt(2/3) h_a per matched port, sqrt 2 u per closed port), the exterior factor a_2 = b_1^8 sqrt(b_2)/144 (prefactor 2^-6 (2/3)^2 = 1/144, exact), the Pauli identity (exact check on Gaussian integers), and the table rows. The four one-edge mixed labels vanish: swapping axes 1 and 2 preserves the internal Wilson law, sends H to H^-1 and fixes K, so E[u v (h.k)] = -E[u v (h.k)]. The three labels 12, 34, 12|34 are invariant under the per-square rotation. The two crossed labels have the same integrand (h.k)^2, so they are one number, as the row says. The corner-weight convention for a_s (b_n^{1/4} per corner at a block vertex) I only read; it is a positive factor and does not affect any sign.

**Item 3. Taylor screen: HOLDS (recomputed exactly).**
c = 15655/169075682574336 from the four listed contributions, and 16c/3 = 15655/31701690482688. E_4 W = 9/16 at beta = 0 (Haar E q^2 = 1/4). Evenness by the centre flip holds. The screen predicts an increase near zero and so decides nothing on the band; the row says so. The support enumeration is row 1425's (check 1429 reproduced the coefficient by its own network).

**Item 4. Reference with the same internal vacuum: HOLDS (re-derived; producer replayed).**
(2): with 1 - q^2 = (3 - chi_2)/4, the coefficient of chi_n after the mark is [3 d_n lam_n z^n - sum_{l in n x 2} d_l lam_l z^l]/4; dividing by the circuit factor d_n kept in the geometry gives (2). The code `radial_channels` implements exactly this. (3): sum_{l in n x 2} d_l = 3 d_n holds for n = 0, 1 and n >= 2, so |(2)| <= 3M/2. In the axis-4 slice, P lies in the lower cube (multiplier in [0,1]) and Q is a crossing face (norm 3M/2). So the circle bound is 3/2 times the vacuum bound. The tail 786271671008/1e15 follows. Cube control: I re-derived [lam_1^6] D = 15 by hand (8 cube boundaries; 4 with no mark, 4 with one; factors 3/4 and 1/2).
Independent check at a higher degree: I counted the 10-face closed fundamental surfaces by hand (24 two-cube unions; 4 contain both P and Q, 6 only P, 6 only Q, 8 neither). This gives [lam_1^10] of Z, D, D1 as 96, 40, 62, so [lam_1^10](Z D - D1^2) = 40 + 96(9/16) - 2(3/4)(62) = 1. My exact tables give the same value 1. This uses face incidence and Haar moments, not the Racah contraction.

**Item 5. Band enclosure table: HOLDS (rerun identical; key differences recomputed from the logs).**
From the log endpoints: N_core + tail: -25569294 - 204047 = -25773341 <= -25773340 (table; floor of a sum is at least the sum of floors, so this is consistent). D: 512391305272895 - 786271671008 = 511605033601887, exact match. Z: 1256812608959386 - 524181114006 = 1256288427845380 <= ...381. From the hulls alone, a_2 N / z lies in [-2.8998e-11, -2.5535e-11] and -3N/D in [1.3474e-7, 1.5113e-7]. The row's per-cell values sit inside these, as they must. The direct difference on common cells is the right way to beat the X/R overlap. Row 1425's N and Z intervals contain row 1430's, so the two runs are nested. The coarse route (line 155) gives [5.49e-8, 2.42e-7], exact.

**Item 6. Five-dimensional bound 2 g_5 >= 1.8278: HOLDS (re-derived; controls replay identical).**
Given the rest, the two pairs are independent, so E[(h.k)^2 | rest] = tr(M_H M_K) with M_H = w_H I/3 + a_H (n n^t - I/3). Hence E[T | rest] = a_H a_K [(n_H.n_K)^2 - 1/3], which lies in [-a_H a_K/3, 2 a_H a_K/3]. With 0 <= a <= eta w and E[W | rest] = w_H w_K, E_5 T / E_5 W lies in [-eta^2/3, 2 eta^2/3]. So 2 g_5 lies in [2 - 2 eta^2, 2 + 4 eta^2] = [182783288, 234433424]/1e8, exact for eta = 2934/10000. The value of eta is row 1425's (check 1429 HOLDS). As Step 2 (c) says, the test does not discriminate.

**Item 7. Fixed U(1) charges: HOLDS (read, re-derived).** The traceless part of a 1x1 endomorphism is zero. This is a kinematic zero for every label in the class.

### Step 5. A second natural reference reverses the verdict (new computation by this check)

Reference R2 is the disconnected product: each square from its own marginal law, which is row 1424's product subtraction (5). Root gauge invariance gives E[h h^t] = E|h|^2 I/3, so R2 = a_2 (E|h|^2)^2/3 and
  3 z^2 (E T + Cov/3) = 3 z N + (z D - D1^2),  with D1 = z E|h|^2 and Cov = Cov(|h|^2, |k|^2).
X > R2 (an increase) exactly when this is positive.
Method: my variant `radial_var.py` gives exact rational tables for Z (no mark), D (two marks) and D1 (one mark, folded symmetrically; equal to the unfolded P-only table at degree 28) through original degree 34. Tails from degree 36 by the even Cauchy rule of (3): circle bound 15466258 at t = 9/4, times 3/2 for D and D1 (one or two marks; the bound for one mark is re-derived from (3)). N is row 1430's (groups42, tail 204047e-15). Evaluation on 512 closed cells with row 1430's outward integer Ball arithmetic (`cov_bounds.py`, 16 s). Through degree 28 my tables equal the cutoff-28 tables.
Results, hulls over the band:
- tails x 1e15: Z 4040045543, D and D1 6060068314 each.
- E_4 W in [0.40715963, 0.40770636], inside the row's [0.40637237, 0.40849625].
- E_4 |h|^2 in [0.63798745, 0.63842908].
- z^2 Cov in [1.514064e-4, 2.387568e-4].
- 3 z N in [-9.738e-8, -8.697e-8].
- **3 z^2 (E T + Cov/3) in [1.513161e-4, 2.386628e-4], strictly positive on every cell.**
So, against the disconnected-product reference, the crossed coefficient is larger than its reference by a relative amount of at least 2.3e-4 throughout the band. This is about 1500 times the size of the row's decrement, and it has the opposite sign. The leading strong-coupling term is +lam_1^10 (exact, hand count in Item 4). Standing: exact tables and outward integer arithmetic; the geometry kernel and the enumeration completeness are row 1425's (check 1429); the tail rule is the row's (3) with one mark; not Lean-replayed. Reference R0 (one conjugation per strip) gives zero for every crossed or grouped label, so it is degenerate and fails the strict test.
Conclusion for (b): the "decrease" belongs to the choice R1. R1 is the reference that removes only the relative orientation, which makes X - R equal to a_2 E T by construction.

## What I re-derived, recomputed, or only read

- Re-derived: strip contractions and a_2; the symmetry table; the per-square reference average; (1) and g_alt + 2 g_d = 3; (2) and (3); the cube control 15; the 5D conditional algebra; the U(1) zero; the label-sign rule c1 (c1 + 3 c2) E T < 0.
- Recomputed with exact rationals: c and 16c/3; the coarse bound; 2 - 2 eta^2 and 2 + 4 eta^2; log sums for N, D, Z; the lam_1^10 covariance coefficient (hand count and table agree on 1).
- Rerun (replay, same code): matching_bounds 512, radial 28, matching_geometry, controls. All identical.
- New computation (my variant code, same geometry kernel): unfolded tables, degree-34 Z, D, D1 and the R2 test.
- Only read: the corner-weight convention for a_s; row 1425's enumeration, recoupling phases, circle constants and eta (relied on check 1429).
Scratch folder of this check: /private/tmp/claude-501/chk1431/ (`alg/alg.py`; `run/replay/`; `run/radial/radial_var.py`, `cov.py`, `cov_bounds.py`).

## Ranked defects

1. **Relabelled moment, not a new signal.** The decrement is a_2 E_4 T with the same E_4 T < 0 as row 1425. For any label c1 E(h.k)^2 + c2 E W, the per-square test reads a decrease exactly when c1 (c1 + 3 c2) E T < 0. The crossed label has product +1; the ring had -2. Line 84's identity g_alt + 2 g_d = 3 makes the two verdicts one fact. The Result (line 18) and next row 2 (line 204) present it as a new signed coefficient.
2. **The verdict depends on the reference.** With the disconnected-product reference of row 1424 (5), 3 z^2 (E T + Cov/3) lies in [1.513e-4, 2.387e-4] > 0 on all 512 cells: an increase of at least 2.3e-4 relative. The per-strip reference gives zero. Only R1 gives a decrease, and R1 makes X - R equal to a_2 E T by construction.
3. **The pre-registration has no force.** The class was frozen after the sign of E_4 T was known (line 31) and contains a label with the right sign product. Plan line 23 ("outside previously resolved cases") fails.
4. **The filter tests do not discriminate.** The U(1) zero is kinematic for every traceless label. The 5D test passes whenever |g_5 - 1| < 1/2; row 1425's rejected ring passed it too. The factor 2 is inserted, not produced by a block step.
5. **No carry and no rate.** A bare coefficient of one block at fixed beta, with relative size 1.35e-7 to 1.51e-7, is not an inequality through a block step (Remark PAIR). It is far from rate (h). Filters (t3) and (t4) are not addressed.
6. **Next row 1 duplicates work.** A Lean replay of this response re-certifies E_4 T < 0, which the replay of row 1425 already covers. The only new item is the scalar D, which affects the size and not the sign.
7. **Next row 2 lacks an anti-selection clause.** It must require that the block map fixes the combination (c1, c2) and its sign before evaluation. Otherwise any sign of E T can be read as a gain by choosing the label.

No arithmetic, enclosure or symmetry line of row 1430 fails. The defects concern what the numbers mean.

## Decisive outcome

The crossed-matching "decrement" is the row-1425 moment E_4 T < 0 read through a label whose reference has the opposite sign. It is a relabelled moment, not a new signal. Under the lane rule "Equivalent is not progress" it counts as no progress. Its sign is also not robust to the choice of reference. Against the lane's own earlier disconnected-product reference, the same coefficient is an increase, about 1500 times larger than the claimed decrease. The gate is passed only in the form the label and reference R1 guarantee. The U(1) and 5D parts of the gate are non-selective here. So the pass does not matter for a four-dimensional carry. The finite arithmetic of the row holds as written: all replays match, and the key sums and the 5D bound are re-derived. To count, the response would have to enter an exact block map that fixes its combination in advance, keep a definite sign in that map's residual with every other term included, and be transported to the coarse coupling at a useful rate. None of this is shown.

End: 2026-11-23T02:14:55Z (date -u). Steps were appended in order between the start time and this time.
RESULT: HOLDS AFTER CORRECTION as arithmetic (replays identical; 1 - g_4 in [134.85, 151.01] ppb and 2 g_5 >= 1.8278 confirmed), but the decrement is row 1425's E_4 T < 0 relabelled (g_alt + 2 g_d = 3), and against the disconnected-product reference it reverses to an increase (3 z^2 (E T + Cov/3) in [1.513e-4, 2.387e-4] > 0), so it is no new signal and no evidence of a 4D carry.
