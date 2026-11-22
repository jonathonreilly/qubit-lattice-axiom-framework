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

