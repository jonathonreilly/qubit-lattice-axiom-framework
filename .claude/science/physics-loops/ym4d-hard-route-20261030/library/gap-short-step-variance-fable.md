lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T17:57Z

# The short step as one conditional-variance inequality (row 1383)

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, pinned commit 2df402783. Not checked by another model.
Not an audit. Started 2026-11-22T05:57Z (date -u).

Moves: mechanism M-D of row 1380 (Section 5, row 3), "dressed moves". Item on the path: the mass-gap seed of the gap
lane. If (BUB) is proved in the window, the short step has a sign and the lane gets a first selective inequality. If
it is disproved or shown equivalent to the seed, M-D is closed and the lead does not queue it again.

## 0. Plan and status log

Plan (one step per response, each appended here before the next):

1. Read the row's sources: row 1380 Section 4-5, row 1018 (short step in three forms), row 1244 (Lemma 2.1, split of
   F'', Proposition 2.3), rows 1026 and 1034 ((SYM), Theorem BD), row 1012 (Balaban CMP 109 Ward-Takahashi quote).
   Repo search and registry grep (rule 0a, Repo first).
2. Fix one explicit gauge-covariant block map of ratio 2 and one explicit lift of a block move. Write the exact
   identity: cost of the block move under the blocked law = cost of the lift under the Wilson law minus the mean
   conditional variance of the lift's divergence term.
3. State (BUB). Run the tests: compact U(1), SU(2) in five dimensions, SU(2) with an adjoint Higgs factor,
   weak coupling against Balaban's Ward-Takahashi identification of the marginal term.
4. Equivalence question: is (BUB) equivalent to the seed (rule "Equivalent is not progress")?
5. Prove or disprove (BUB) in the window beta 2.3 to 2.6; if neither, a GUIDE run (criteria written first, numeric
   lock) for the sign, and what a proof would need.

Status log (times by date -u in the same command):

- 2026-11-22T05:57Z file created with the plan. Nothing proved yet.
- 06:09Z Section 1 written: sources, registry grep, design. Identity next.

## 1. Sources read, registry matches, and the design (written 06:09Z by date -u)

Credits. The split "response = direct term minus variance" is Lemma FLOW of row 1018 (Claude Fable 5.2,
`gap-short-step-max.md` L217-231). Its Gaussian form with the best flow is Lemma 2.1 of row 1244 (Claude Opus 5.5,
`gap-mini-solve-aa-opus.md` L115-142), which also says where the one-loop running sits (Proposition 2.3). The
corner formalism and Lemma WN are row 1013's (`gap-invent-selective-max.md` L101-102). (SYM), Proposition LF and
Theorem BD are rows 1026 and 1034. The quotation of Balaban, Commun. Math. Phys. 109 (1987), (0.18)-(0.22) and
p. 258, is row 1012's (`prior/gap-gauge-stiffness-read-opus.md` L109-115). Block maps with staples are Swendsen's;
the averaging block map and the background minimiser are Balaban's. The row itself was proposed by row 1380.

**Read in full:** FINISH.md rule sections (L52-73, L299-351) and row 1383; row 1380 Sections 1-5; row 1018
Sections 2 and 4 (Lemmas FLOW, PROJ, FR+, SPLIT, sizes); row 1244 Steps 1-3; row 1012 Step 5 (B1); row 1243
Step 3 ((S-V)). **Read by RESULT line and headings only:** rows 1026, 1034. **Not read:** Balaban's paper itself
(row 1012's quotation is used); the rest of the lane.

**Registry grep (rule 0a), `/usr/bin/grep -l -i -F` over `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md`; `library/open-core.md` has no hit for "(BUB)" or "conditional variance".**

| Term | Files | What is on file |
|---|---|---|
| "(BUB)", "dressed move", "bubble minus" | 1 (row 1380) | only the proposal of this row |
| "blocked law", "block move" | 4, 2 | rows 1290/1297 ("straight blocked law", another object); no cost identity |
| "one-link Fisher", "Monte Carlo renormalization", "harmonic lift" | 0 | not on file |
| "MCRG", "Swendsen" | 1, 2 | literature notes only |
| "Fisher information" | 19 | (FC), Theorem BR of rows 940/941 (heat-flow contraction of Fisher information; another object); row 1371/1374 (Fisher bound of chord coordinates given all other links) |
| "step scaling" | 22 | killed as a seed supplier in `gap-phys-seed.md` Part 2 (row 720) and `gap-mid-max.md`; a ratio of sizes, not a block law |
| "(S-V)" | 6 | row 1243: an explicit flow whose direct term is below the abelian value; OPEN |
| "straight transport" | 20 | row 1145 (near-Haar straight transports, a sup-norm class), rows 1353-1360 |

So the identity of this row is the blocked form of Lemma FLOW and is not on file. The nearest statements are
Lemma FLOW (pin response, one scale) and row 1244's Gaussian split.

**The design, and what the reading already shows.** Section 2 gives the identity for every block map and every
lift (Proposition LIFT). Three facts about the wording of (BUB) follow from the sources and are proved or tested
below; I state them here so that a reader sees the direction at once.

1. A block move needs a colour direction. For a lab-frame direction the cost under any gauge-invariant law is
   site-local (Lemma WN applied to the blocked law). So "the classical curl form" has a frame-free meaning only
   through one number per law: the one-link Fisher information J (Section 3). For frame moves rows 1026/1034
   bind ((SYM), Theorem BD).
2. The reference matters. With the bare classical form as reference, (BUB) holds for compact U(1) at every
   coupling, by the plaquette tadpole alone (Section 4). So the literal form is not selective.
3. With the previous level as reference (J at level k + 1 against J at level k) the statement is canonical, but
   it is a statement about all levels through the band, and it depends on the block map (Section 4, Lemma THIN:
   for straight-path decimation J tends to 0 in every model).
