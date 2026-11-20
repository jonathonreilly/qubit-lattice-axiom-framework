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

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T16:10Z by date -u)

**The seed.** Modulo the carry, the problem is a lattice gap of Wilson SU(2) at one coupling, with a box of several
hundred correlation lengths (Step 0, items 1-2). I re-derived these routes before reading the tables, then grepped
each (rule 0a); every one has a match on file with its first failing step:
- continuity in beta from the strong-coupling seed, closed by a bound on how fast a level can fall: rows 708, 978,
  1281 ((LEV) is false as an operator inequality; it needs a "bounded excess" of the first level, which is the crux).
  My variant: the volume-robust thermal form d/dbeta log(1 + s) = (thermal action deficit) with a Gronwall bound
  "deficit <= K log(1 + s)" is equivalent to (LEV) with K proportional to u, so it adds nothing (checked by the
  one-level example: deficit / log(1 + s) = u |dm/dbeta|).
- a bootstrap through local excitations (Lieb-Robinson bounds for the Kogut-Susskind Hamiltonian, isolated
  one-particle band): rows 1113, 1213 and `library/gap-outside-box-max.md`; my estimate of what it gives is an excess
  bound of order m^(-4) in lattice units, so the gap would close at finite beta in the bootstrap; FAILS quantitatively.
- vortex and electric-flux free energies, twist eaters (Fact T): `library/gap-crux-restate.md` (TUBE'),
  `library/gap-cr-tomboulis-max.md` and its check (Tomboulis 2007 and the Ito-Seiler critique).
- Migdal-Kadanoff and hierarchical bounds: route RG, retired (row 998 7.4: "the departing step is the crux").
- B's ascent (H2)/(S) with C_B = 1 + O(g_k^2): the product over scales grows like a power of log(1/a) unless the
  O(g^2) term has a selective sign; this is a (K-flow) statement with no supplier (row 998 6b).
- Bakry-Emery for the Doob-transformed ground-state diffusion: needs the ground state; a coupling-uniform curvature
  would make the limit trivial (row 1237 Proposition UNI).
- gapless comparison models with asymptotic freedom (Georgi-Glashow, adjoint matter, products with a photon): on
  file (rows 1285, `library/gap-afield-b-max.md`, `library/gap-global-reform-max.md`).
- dimensional reduction to the posted 2D O(4) theorem, abelian projection, Gribov-Zwanziger, anomaly matching
  (theta = pi), Weinberg-Witten: on file or give no lower bound on the spectrum (anomalies and Weinberg-Witten allow a
  free Maxwell infrared and a trivially gapped one alike).
Verdict (ARGUED): I have no route to the seed that is off the record, and the record (row 998 9.5) says a further
screen is waste. I do not attack the seed in this row.

**What I do instead (the rule "only closures count").** The record leaves two kinds of items: the seed (no engine),
and inputs of the one-cutoff carry, most of which read Balaban's CMP 116 (not on this machine). Two carry inputs are
unowned at this pin and can be worked with sources on hand (rule 0a: grep of FINISH.md and `library/open-core.md` for
"(U-dom)", "H2'", "absolute core", "cross-admission": hits only in rows 1267, 1268, 1278, 1280, as OPEN or ARGUED):
- **Item A: (U-dom) of row 1280 (3.3),** ARGUED there; the input of Theorem U (row 1280 3.6) at the window levels.
  Sources: Balaban CMP 102 (Theorem 1 and (190)) and CMP 119 ((1.2), (3.2)-(3.13)), both in the owner's papers folder.
- **Item B: the connectedness clause of Lemma H2' (row 1278 2.3),** "connectedness and isometry-invariance of the
  absolute core (not found stated)". Source: YM4_EM at c7fef8b21b58 (fetched by URL to a scratch folder).

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1267, 1268, 1278, 1280). Success on A:
(U) leaves the carry's list with only (E+) and the supplier readings left at the window levels. Success on B: Lemma
H2' becomes PROVED GIVEN readings with no geometric gap. Failure: the first step that does not close, named.
Neither item changes the seed; this is said plainly so that nobody counts it as progress on the crux.

**Plan.** Step 2: item B (short). Step 3: item A, reading CMP 102 Theorem 1, (190) and CMP 119 (3.6)-(3.9).
Step 4: labels, state, RESULT.
