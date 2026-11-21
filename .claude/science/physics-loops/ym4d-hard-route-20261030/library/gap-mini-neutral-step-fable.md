lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-21T17:12Z

# gap-mini-neutral-step-fable (queue row 1353)

Worker file for queue row 1353 of `FINISH.md`, branch `claude/ym4d-hard-route`, pinned at commit `33f734aed`.
Started 2026-11-21T05:12Z (from `date -u`). Written section by section; each section says what is PROVED, ARGUED, GUIDE or OPEN.

## 0. Status log

- 2026-11-21T05:12Z: file created; reading the row, `GOAL.md`, the rule sections of `FINISH.md`, `parts/gap.md`, rows 1342, 1349, 1351, 1352.
- 05:13Z: read the row (L1434 of `FINISH.md`), `GOAL.md`, the rule sections of `FINISH.md` (L52-73, L320-350), and the RESULT lines of rows 1332, 1335, 1340, 1342, 1349, 1351. Next: `library/gap-blockstep4-astra62.md` in full, then Proposition CH.
- 05:13Z: read `library/gap-blockstep4-astra62.md` (row 1351) in full, L1-355. Its own last section states the open step: carry the short factors (the remaining Wilson plaquettes and the window quotients g_(i,H)) into the end class (23)-(24); its (16) and (25) are lower bounds on interactions that a scalar approximation loses. Next: Proposition CH (row 1332, check 1335), the statement (N-phys) (row 1161), Lemma TP (row 1342), the cores of row 1348.
- 05:35Z: registry grep run (Section 1); Sections 1 and 2 written.

## 1. Repo search and inputs

Searched before deriving (rule 0a and "Repo first"): `library/open-core.md`, every `library/gap-*.md`,
`library/prior/gap-*.md`, `parts/gap.md` and the `FINISH.md` rows, with `grep -c -i -F`, for the terms of each
candidate statement of this file. `library/open-core.md` has no line on (N-phys), on an end class or on a neutral
block step (0 hits for "N-phys", "end class", "chi-square", "gauged"; its 17 hits for "admission" are about the
hard-core part, not about this lane). Cross-branch search (main, PR 10114, 10133, 10134, 10141): not repeated here;
row 1351 ran it for the same statement on the same day (`gap-blockstep4-astra62.md` L3) and found no proof of the
block induction. I rely on that record and did not fetch the other branches.

Matches for the statements I considered, so that none of them is called new below:

| Candidate (my words) | On file | Verdict |
|---|---|---|
| The bond test of a product-reference class at a time cut is the seed itself (Hilbert-Schmidt distance to rank one = thermal sum) | Identity I1, `gap-compress-opus.md` L36-46 ("the thermal sum is a chi-square mutual information"); its 2.4 ("the partition tensor of one box is close to rank one"); Lemma MC, `gap-glue-max.md` (maximal correlation of slices) | on file; cited in Section 3, not re-proved |
| The centre sums may be taken at one fixed block side on the whole cutoff tail | row 1345, `gap-blockstep2-astra62.md` L61 and L103 ("One may even fix B = L^j once and for all") | on file |
| The neutral mass is a positive angular integral with the cube constraints opened | row 1351 (18)-(20), `gap-blockstep4-astra62.md` L232-265; row 1345 (9) | on file |
| The ordinary box blocking fails the bond test at every block side | row 1351 (16), L175-194 | on file |
| A finite-size mixing condition gives a cluster expansion at that scale (Olivieri, Olivieri and Picco) | 35 lane files name Olivieri; the uniform-in-boundary form fails above about 1.01 (Proposition CA-FAIL, row 1072) | on file |

Inputs read for this row. In full: `library/gap-blockstep4-astra62.md` (row 1351, author gpt-6.2-astra; its check,
row 1352, was running when this row started, so every statement of row 1351 used below is "unchecked at this pin").
In part: `library/gap-shrink-box-fable.md` 5.3 and Section 6 (Proposition CH, row 1332; check row 1335);
`library/gap-seed-audit-fable.md` L77-207 (statements (N-phys), (G_ev-phys), Lemma TP, Theorem O; row 1342, check
row 1349); `parts/gap.md` L8-104; the RESULT lines of rows 1332, 1335, 1340-1351.

Credits. Tadeusz Balaban (the block renormalization method). Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text (the account, the trajectory, first-passage data). G. Mack and V. Petkova (the centre
split). G. 't Hooft (twists and flux sectors). K. Osterwalder and E. Seiler, M. Luscher (transfer operator,
reflection positivity). E. Olivieri and P. Picco (cluster expansion from a finite-size mixing condition). In this
lane: gpt-6.2-astra (rows 1341, 1345, 1348, 1351: the centre-sign block map, the cores, the strip elimination, the
neutral end class and bound (24)); Claude Fable 5.2 (rows 1332, 1340, 1342: Proposition CH, Theorem TL, the neutral
target); Claude Opus 5.5 (checks 1344, 1347, 1350; Identity I1 of `gap-compress-opus.md`).

## 2. The target, and how best to attack it

### 2.1 The statement (from row 1342, L93-94, and row 1351, L11-20)

(N-phys): there is an admissible physical side L such that for all late j: 4 divides n_j, n_j >= 2^70, and there is
an integer u_j with 3 <= u_j <= n_j/512 and s_j(u_j; n_j^3) <= 1/2. Here s(u) = sum over a >= 1 of x_a^u is the
excited trace of the neutral sector (electric flux zero, magnetic twist zero) of the Wilson transfer operator on the
box n^3, in units of its vacuum eigenvalue. With Z_+(T) the mean of the partition function over the eight temporal
twists, 1 + s(u) <= Z_+(u)^2/Z_+(2u) (Lemma TP). So (N-phys) follows from D_+(u) := 2 log Z_+(u) - log Z_+(2u)
< log(3/2) at one such u, for all late j.

The row asks for a chain as in Proposition CH: sets C_0, ..., C_N of models that carry the two numbers Z_+(u),
Z_+(2u); maps that keep both numbers; (BASE): every late Wilson datum has a representative in C_0; (END): every
model of C_N has D_+ < log(3/2) with a margin. Row 1351 supplies one (END): a class of models with independent
link variables, small plaquette marks and coherent centre weights, with D_+ <= 8 v e^(-theta j_0), its (23)-(24).

### 2.2 What the chain formalism contains and what it does not (PROVED, by inspection of Proposition CH)

A map that keeps the two masses is not restricted in any other way by Proposition CH. So, for one datum d:

    there is a model in the end class of row 1351 with the two masses of d
    if and only if D_+(d) lies in the set of values of D_+ on that class.

The class contains the pure coherent centre models with weight ratio e^(-2J), J >= 3, and a free scalar per
plaquette. So a representative with the right two masses exists as soon as D_+(d) is a value that those models
take; the chain is then the one map "d goes to that model". Hence the formalism alone is never the proof: all
content is in maps that are LOCAL and EXPLICIT, so that membership of the image can be verified from bounds on the
input. This is known to rows 1332 ("the proof is one line") and 1351; I state it because it fixes what a block step
has to be: a local construction R together with a proof that R(C_k) lies in C_(k+1), where both classes are given
by bounds.

### 2.3 The three legs, with their state on file

- (E) END. On file: row 1345 (11)-(12), row 1351 (10)-(11), (15), (23)-(24). All of them are classes with a
  PRODUCT reference measure (independent variables on links, or on boxes and bonds) and small marks.
- (M) The middle leg. From first-passage data (effective inverse coupling above 5 by check 1331, with no upper
  value) through the band to couplings of order one, and from there into (E). On file: exact maps at every coupling
  (the 2^4 cube map of row 1341, the centre-sign map of row 1345, the strip elimination of row 1351), and
  obstructions to the simplest landings (rows 1345 (14), 1351 (13), (16), (25)). No class is carried by any of
  these maps. This is the open step.
- (U) Entry. The account's last-scale densities on the two neutral tori. Row 1345 avoids it for the centre part by
  working at the bare scale with a large block side. The angular part is not avoided by any row.

### 2.4 Choice of attack

The lane's lesson from rows 1188-1259 is that blind candidate lists return items already on file. So I start
from the open step that row 1351 names (L338, L351): carry the short factors into an end class with a product
reference. I ask first what any landing in such a class needs (Section 3), then try the two landings that the
exact maps on file suggest: more colours of the strip elimination (Section 4) and the opened angular integral
(20) (Section 5). Each section ends with its first failing step.
