lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-20T23:47Z

# gap-mini-solve-ak-opus: the SU(2) mass gap, attack plan and steps

Queue row 1267 of `FINISH.md`. Started 2026-11-20T11:47Z (date -u), at commit a05f4c020 on branch claude/ym4d-hard-route.
Research-stage working state; grants no status. Labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Orientation and plan (written 2026-11-20T11:51Z by date -u)

**0.1 Read for this row.** `GOAL.md`; `FINISH.md` sections Where it stands, How we work, Joining, Working efficiently,
Rules, and the recorded RESULT lines of rows 1150-1265; `parts/gap.md` State of attack; `library/prior/gap-onebound-read-sol.md`
(row 1218) in full; row 1260 (`gap-mini-solve-ai-opus.md`) in full. Summaries are pointers, not evidence; each statement
used below is re-read at its source.

**0.2 Where the problem stands (pointers).**
- The Jaffe-Witten gap on the account's tr F^2 sector reads, beside the account's premises, one infrared input: (N-phys)
  (rows 1161, 1179), or on the one-cutoff carry of row 1233 a seed at one base datum; row 1258 (check 1265: HOLDS) gives a
  sufficient one-coupling form, (SL) or (RR) at one cutoff's couplings.
- Every route family to the infrared seed found by about ninety plain-brief rows is on file with a first failing step
  (`parts/gap.md` methods 19-36 and route registry; screening tables of rows 1189, 1194, 1199, 1237). The published
  sources of row 1218 do not supply it: A (Bhattacharjee et al.) gives a stronger one-scale thermal criterion with a
  conditional ascent; B's Corollary 166 is a weak-coupling bound for straight-path block variables of length b = 2^k at
  beta_W <= k + 2. GUIDE (my reading, not a proof): at that coupling the straight-path variables are close to Haar by
  ultraviolet noise (variance of order g^2 b along a straight path), so the bound holds for the same reason it would hold
  for compact U(1); it is blind in the sense of `parts/gap.md` (row 998 6b) and cannot carry the band.
- The one-cutoff carry on the pin route (rows 1233, 1255, 1256, 1260) has one named open input that no row has attacked:
  **(FC)**, row 1260 (G3): at one step and at the same weights, forming the unmarked coefficient on the frozen frame
  theta_r = X + c_0 r or on the run's own frame changes it by eta_k, with sum_k eta_k bounded uniformly in the cutoff.
  Row 1260 5.2 splits it (GUIDE) into a cut-comparison estimate for YM4_EM's all-small-field kernel and a partition
  matching.

**0.3 Plan (judgement).** The infrared seed is the open core. No session-sized route to it is on record, and row 998 9.5
asks for no further fresh-framing exercise, so I do not re-screen it. I take (FC).
Moves: (FC), the open input of the gap chain's ultraviolet carry (row 1260 4.3). Success: (FC) proved from statements
of Sussman and Alpoge's YM4_EM (their premises named), so the pin-route carry reads no (FI). Failure: the first EM
statement (FC) needs and EM does not state, or a counterexample (a frame-dependent discrete choice that moves the
coefficient by a non-summable amount).
Steps: 1 read EM's formation of the coefficient (actual step, kernel, cut, gauge weight, envelope theorem, slopes) and
pin down exactly what depends on the frame; 2 state (FC) precisely in EM's notation; 3 prove the cut comparison, or name
its first failing step; 4 the discrete choices; 5 status table and RESULT.

