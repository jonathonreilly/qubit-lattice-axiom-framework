lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-15T02:09Z

# Row 963, gap-rotgeom-opus: rotated and diagonal geometry for the seed

Queue row 963 of `FINISH.md` (pinned at commit 3900bfe8b). Owner's question: "could the box
rotate in time as well?" Test item, analysis plus GUIDE. Author: Claude Opus 5.5 max, Mac mini
worker 2. Labels: PROVED (written argument, checkable by hand), CONDITIONAL (proved given a
named hypothesis), GUIDE (a run or heuristic; refutes or guides only), OPEN.

## Plan (at most eight steps; one step per response, each appended here before the next)

1. Sources: FINISH rules; rows 960 (`gap-vargeom-opus.md`), 962 (`gap-constraints-max.md`),
   row 892 section 4.1 (Lemma SPLIT, centre-twist flux sectors); the definition of the seed
   S(a; B); grep `open-core.md` and the FINISH rows for overlap.
2. Item (1): twisted tori. Exact statement of Tr((R T)^a) = Tr(R^a T^a); sector decomposition of
   the seed by characters of the spatial symmetry group; the centre-twist flux sectors as the
   existing analogue.
3. Item (2): sector-wise statements. Which sectors carry the soft modes (free photon, U(1)
   toron, frozen Q_8 / 2T flat vectors); whether momentum or lattice angular momentum gives a
   free-energy margin; whether the trivial sector carries the full order-one difficulty.
4. Item (3a): reflection positivity of the Wilson action across diagonal hyperplanes: literature
   with sources, and a by-hand proof or refutation on the smallest case.
5. Item (3b): what a diagonal transfer operator and its thermal sum give relative to the axis one.
6. Item (4): fact tests (U(1), frozen groups, SMALL-BOX) by hand.
7. GUIDE: sector thermal sums in a solvable model (only if cheap), scripts in `guide/lane963/`.
8. Verdict: does rotated or diagonal geometry buy anything over the static axis tori, and why.
   RESULT line.

## Step log

(Steps are appended below as they finish.)
