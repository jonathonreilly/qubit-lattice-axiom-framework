lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T03:02Z

# gap-mini-solve-as-opus: the four-dimensional SU(2) mass gap (FINISH row 1293)

Started 2026-11-20T15:02Z (date -u) on the Mac mini Claude worker 2, branch claude/ym4d-hard-route pinned at 05378c8d5.
Research-stage working state. Labels: PROVED, ARGUED, GUIDE, OPEN, as the row asks.

## Status

Step 0 (reading) and Step 1 (choice of attack) done, written 2026-11-20T15:10Z (date -u). Next: Step 2, reading the account's
one-step kernel and coefficient theorem (YM4_EM) for the statement of the item.

## Repo search (rule "Repo first")

This checkout has no `origin/main` ref and holds `docs/` only in the index, so main and the open PR branches
(#10114, #10133, #10134, #10141, #10144) were not searched from here; only this folder was. Rule 0a grep of
`FINISH.md`, `library/open-core.md`, `library/l17c.md` for "parity envelope", "(PE)", "half-loop": the only match is
row 1280 (`library/gap-mini-solve-ap-opus.md`, this worker's thread, Proposition PE ARGUED). No queued row owns it.

## Step 0. Record read (statements about the record, not evidence)

Read at the pin: `GOAL.md` in full; `FINISH.md` L1-85 and L299-356, row 1293; the RESULT segments of rows 1240-1296;
`parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` in full (row 1218); row 1280
(`library/gap-mini-solve-ap-opus.md`) L42-469; row 1291's file (its Step 1 digest only, no choice yet). Summary:

1. The infrared seed ((N-phys) of row 1161, equivalently (SL)/(RR) of row 1258 at one weak coupling, or the stronger
   full-thermal window (A-B*) of Bhattacharjee et al.) is OPEN. About sixty idea families are screened on file (rows
   1189, 1194, 1199 tables; rows 1228-1287). Row 1218's reading: none of the three published sources supplies it.
2. The one-cutoff carry on the pin route (rows 1233, 1255, 1256, 1260, 1264, 1267, 1268, 1275, 1278, 1280) is a
   chain of implications. Its open inputs after row 1280 and checks 1263, 1266, 1276, 1288: the supplier readings
   (E0)-(E6), (E+), (TH) against Balaban's CMP 116 (not on this machine); either (U-dom) or the inputs (P1)-(P4) of
   row 1280's parity envelope (PE); row 1267's (H2)-(H3) (row 1278: H3' given readings, H2' ARGUED); the account's
   outstanding `9.1:prop-blind-site-expansions`; (V9) (check 1288: row 1275's reading N2 FAILS); (DET)'s inputs.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T15:10Z by date -u)

**The seed.** I do not attack it. Every route I can name (vortex free energies, Migdal-Kadanoff bounds, abelian
projection, Gribov region, Bakry-Emery, chessboard and infrared bounds, Lee-Yang in beta, twisted boxes, layer
reductions, large N) has a match in the tables cited in Step 0, item 1, and `parts/gap.md` (row 998 9.5) names a
further blind screen as waste. The seed is a statement at order-one coupling with a number in it, and no hand method on
file or in the literature read here reaches it.

**The item: the parity envelope (PE) of row 1280, from ARGUED to PROVED given precisely stated inputs.** Claim of
(PE): the unmarked coefficient of one Balaban step obeys |f_(k+1)| <= C theta_k^(-1) (log theta_k)^q + tails, not only
EM's C theta_k^(-1/2) (log theta_k)^(p_0): one step has no half-loop term. Row 1280 4.5 shows what it buys: the drift
of the account's runs from the scaffold becomes polylog, (U) closes without (U-dom), and Route Z's flow law (B3+) of
row 680 gets its mechanism.

Moves: the one-cutoff carry on the pin route (row 1280 5.2: (U) needs (U-dom) and (E+), or (PE)); Route Z's (B3+)
(row 680 Section 5). Success: (PE) becomes PROVED GIVEN inputs that are read in the account's text, so (U) leaves the
carry without (U-dom). Failure: an odd-in-g term in the step that survives the parity, which would be a named obstruction
for (PE), (B3+) and Route Z.

**New idea for the proof (to be written in Step 3).** Row 1280 used a parity rule degree by degree ((P2)), which needs
Taylor remainders. A cleaner device: every factor of the step that is a function of the configuration depends on the
coupling g and the normalized fluctuation b only through exp(i g b) (and on g^2 through the action's prefactor), so it
is invariant under the joint flip (g, b) -> (-g, -b). Replace g by a complex parameter h in the fluctuation, keep the
cut frozen at the actual g, and use the symmetry of the Gaussian reference: the localized coefficient is then an
analytic function of h that is even up to the cut's asymmetry, and a Cauchy estimate for even functions gives
f(g) - f(0) = O((g/r)^2) on a disc of radius r of order 1/(log theta)^(p_0). The cut's asymmetry is a thin shell at the
threshold (path products and their inverses differ only at third order), so it costs tails by row 1280's Lemma SW.

**Plan.** Step 2: read YM4_EM's one-step kernel and coefficient theorem (definitions of f, of the unmarked output, of
the cut, and what EM assumes of the localization and of complex data). Step 3: state and prove Theorem PE in the form
those definitions allow (Lemmas: flip invariance, even Cauchy estimate, near-evenness from Lemma SW, assembly). Step 4:
check the flip invariance against each factor of the step (action, Haar and chart densities, soft axial weight, cut,
inherited list) in Balaban's CMP 119 as read in rows 1268 and 1280. Step 5: consequences, labels, RESULT.

