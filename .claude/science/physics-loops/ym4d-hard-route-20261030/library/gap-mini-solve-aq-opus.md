lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T02:59Z

# gap-mini-solve-aq-opus: four-dimensional SU(2) Yang-Mills mass gap (row 1284)

Started 2026-11-20T14:59Z (date -u) on the Mac mini, worktree pinned at commit 5b1df13cc
(branch claude/ym4d-hard-route). Labels: PROVED, ARGUED, GUIDE, OPEN, per the row brief.

## 0. Status log (updated in place)

- 14:59Z: file created; reading GOAL.md, FINISH.md rules, `parts/gap.md`, the RESULT lines of the
  earlier mini-solve rows, and `library/prior/gap-onebound-read-sol.md` (row 1218).

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T15:55Z by date -u)

Read: `GOAL.md` in full; `FINISH.md` L1-84 and L299-349; this item's row (L1365, row 1284); the RESULT lines of
rows 1189-1291 (the mini-solve series, the owner's tiling rows 1285-1287, rows 1281, 1283); `parts/gap.md` L1-104
and the route registry L223-267; `library/prior/gap-onebound-read-sol.md` (row 1218) in full;
`library/gap-crux-restate.md` L1-60; `library/gap-crux-exercise3-max.md` L100-160 (row 998's precise form of the
wall); Steps 0-3 of `library/gap-mini-solve-ap-opus.md` (row 1280) and Steps 1-2 of
`library/gap-mini-solve-ao-opus.md` (row 1278); CA-III L16540-16700 (`9.1:prop-blind-site-expansions`, fetched by
URL at Sussman-Alpoge commit 31a47c543775 into a scratch folder outside the repository).

What the record fixes (each item cites where it is proved or checked; none is re-derived here):

1. Modulo the ultraviolet carry, the gap clause reads one lattice input, (N-phys) of row 1161 (Theorem BP, row 1179,
   check 1183; rows 1225, 1233): at one physical side, uniformly in the cutoff, the periodic centre-neutral excited
   trace of the spatial cube at a time u <= n/K is at most 1/2. With K = 512 (row 1161) this needs a box of at
   least 512 log 2 times the inverse gap (check 1287). Equivalent forms: (W), (PHYS-SEED), (SEED) at one coupling
   with a carry, (SL) at one weak coupling (rows 998, 1258, 1277), and a lower bound of asymptotic-scaling type on
   the deconfinement coupling (rows 1180, 1184, check 1187).
2. In thermodynamic words (my paraphrase of item 1, GUIDE): log(1 + s) is the excess free energy of the thermal
   torus over the vacuum, so (N-phys) says the pressure at temperature 1/(u a) on a cube of side K u a is below
   log(3/2) / K^3 in units of T^4. That is a statement deep in the confined phase (at about a quarter of the
   deconfinement temperature, by Monte Carlo lore), not near any small parameter.
3. Every engine on file is blind, its seed sits in the band, and the one selective proved fact (asymptotic freedom at
   small coupling) has no carrier through the band (row 998 6b; `parts/gap.md` "Hardest open obligation").
   The all-coupling template (the posted 2D O(N) proofs) needs closure of a class uniform over pins and strengths;
   in 4D that class contains ordered members (Proposition CA-FAIL, rows 1072-1074: two pinned slices make a 3D O(4)
   magnet above beta about 1.01) and critical members (Lemma SHEET, row 996: K7 is an annealed Wilson model).
4. Row 1218's sources: A's ascent is conditional on its own seed (stronger than (N-phys)); B's Corollary 166 is
   non-selective (B's own Remark 155; row 1219); Zeng's routes are conditional.
5. Rows 1255-1280 worked the inputs of the one-cutoff carry. What remains there (row 1280 RESULT): (U-dom) or
   (P1)-(P4); (E0)-(E6), (E+) against Balaban's CMP 116 (not on this machine); `9.1:prop-blind-site-expansions`
   ("Proof outstanding" in the account, CA-III L16558-16560; its route repeats CMP 116 Section 2 with island-blind
   lengths, CA-III L16663-16700); (DET)'s inputs (rows 987-994); the account's premises.
