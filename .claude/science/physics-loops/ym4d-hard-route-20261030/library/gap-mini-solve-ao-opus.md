lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T01:45Z

# gap-mini-solve-ao-opus: the SU(2) mass gap in four dimensions

Queue row 1278 of `FINISH.md`. Started 2026-11-20T13:45Z on the Mac mini, Claude worker 3, pinned at commit 45997b1e3.
The problem as briefed: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels: PROVED (a complete written argument here or in a cited, checked source), ARGUED (an argument with a named gap), GUIDE (heuristic or numeric orientation only), OPEN.

## File status

Written section by section. Sections below are appended as each step finishes.

## Step 0. Reading record (13:45Z-14:00Z by date -u)

Read: `GOAL.md`; `FINISH.md` opening sections, rules, efficiency section and queue rows 1143-1286 (titles); `parts/gap.md`
State of attack (lines 1-104); `library/prior/gap-onebound-read-sol.md` (row 1218) in full; the RESULT lines of every
`library/gap-mini-solve-*`, `gap-owner-*` and `gap-laptop-solve*` file at this commit.

What the record says, in short (each item is a citation, not evidence of its own):
- The only open lattice input of the gap clause is the infrared seed (N-phys) (row 1179 Theorem BP with check 1183;
  the continuum datum is proved given the account's premises, rows 916-917; row 1219's RESULT line).
- About forty plain-brief rows (1188-1275) screened route families against (N-phys); each ends "NOT proved, nothing
  disproved". The literature names I tested by grep (Tomboulis, Migdal-Kadanoff, Ito-Seiler, Chatterjee, Adhikari-Cao,
  Shen-Zhu-Zhu, instantons, Gopfert-Mack, Brydges, Federbush, Magnen-Rivasseau, Durhuus, Osterwalder-Seiler,
  Mack-Petkova, Yaffe, Borgs, Kovacs) each have 20 to 180 hits in `library/`, `parts/` and `FINISH.md`.
- The later Opus rows (1255-1275) worked the one-cutoff carry: (EDGE), (FI), (FC), (FC-T)/(FC-1), (V9). Open there per
  rows 1268 and 1275: (U) at the jumps of R_k; the readings (E0)-(E6) against Balaban CMP 116; row 1267's (H2)-(H3);
  Theorem 9.1's hypothesis (e) `9.1:prop-blind-site-expansions` (outstanding in the account; row 1264 was blocked by a
  bot check on CMP 116); (DET)'s inputs.
- Siblings in flight at this commit: row 1277 (an) reads the question left UNDECIDED by check 1239 (does the slab
  hypothesis (M) of Bhattacharjee et al. fail along the 4D Wilson tuning?); row 1280 (ap) was at its Step 0.

Decision rule for Step 1: no forty-first screen of route families (lead's "what not to do next", row 998 9.5, and
the forty RESULT lines above). Choose one precise statement on the gap chain that no row owns, and take it to a proof,
a counterexample, or one precise failing step.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T14:02Z by date -u)

**The crux, as I read the record and as I re-derive it.** Modulo the ultraviolet carry, the gap clause reads one
lattice input: a seed of Wilson SU(2) at one coupling of the account's window (rows 1179, 1225, 1233, 1234; check 1183).
At beta between 2.3 and 2.6 (standard normalisation) the glueball correlation length is of order one to four lattice
spacings (GUIDE, recalled Monte Carlo lore, not used as a step). So the seed is a statement about a lattice of a few
tens of spacings per side at a coupling where:
- every published rigorous method stops far below: cluster and character expansions, Dobrushin and Bakry-Emery bounds
  reach beta of order 0.1 to 0.2 in this normalisation (row 1218: A's single-link and star ranges, B's Corollary 74,
  the curvature range of A and B Theorem 5);
- the uniform-boundary finite-size criteria are false (Proposition CA-FAIL, row 1072/1073, holds after correction in
  check 1074: two pinned adjacent slices make the temporal links a 3D O(4) magnet that orders above about beta 1.01);
- a finite computation would be a computer-assisted step, which GOAL.md forbids.
So the seed is the lattice mass gap at one intermediate coupling. I know of no rigorous result of that kind for any
four-dimensional lattice gauge theory with a continuous non-abelian group, and the forty plain-brief rows found none
on file. My own re-derivations (center-vortex and electric-flux free energies, Singer's positive curvature of the orbit
space with the Faddeev-Popov density, the Kogut-Susskind electric gap, finite-subgroup approximants, Migdal-Kadanoff
flows, a change of bare action) each meet a recorded first failing step: the curvature gain is O(1) against a Hessian
of order beta; finite subgroups and Migdal-Kadanoff are group-blind or meet the same band; a change of bare action
changes only irrelevant terms, and the effective theory at the physical scale is the same strongly coupled one.
Verdict (ARGUED): no attack on the seed fits one session; a further screen is waste.

**What I do instead.** One open input of the chain that no row owns and that can be closed with sources on hand.
Owned at this commit or at the branch tip (read by `git fetch` at about 14:00Z): (U) by row 1280; the slab hypothesis (M) by
row 1277; the CMP 116 readings (E0)-(E6) and `9.1:prop-blind-site-expansions` are blocked (CMP 116 is not in the
papers folder; row 1264 met a Project Euclid bot check). Unowned: (H2) cross-admission and (H3) the total-form list
comparison of row 1267's Proposition FC-chain. Row 1267 labels (H3) ARGUED from EM input (4) with an open condition
("This needs f'' to be admitted") and (H2) assumed.

Moves: the one-cutoff carry on the pin route (row 1233 Proposition 3.7; rows 1260, 1267, 1268). Success: (H2) and (H3)
leave the input list of Theorem FCT' (row 1268). Failure: an admission condition of EM that the shifted list f'' or the
other frame's list violates; then the frame comparison needs a different splitting.

Rule 0a: grep of FINISH.md and `library/open-core.md` for "(H2)", "(H3)", "cross-admission": hits only in rows 1267,
1268, 1275 (as OPEN inputs); no queued row names them.
