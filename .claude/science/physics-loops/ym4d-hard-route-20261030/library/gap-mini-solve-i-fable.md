lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T13:36Z

# gap-mini-solve-i-fable (FINISH row 1199)

Research-stage working state. It grants no status. Nothing here is a public claim.

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 5e5082e7c.
No subagents. Checked by no one. File created 2026-11-20T01:36Z (`date -u`).

**The problem (row 1199).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the
sense of Jaffe and Witten. Labels used below: PROVED, ARGUED, GUIDE, OPEN.

## Plan (written before any reading of the lane files)

1. Step 0: read the lane's map (`parts/gap.md` method list and route registry, the RESULT lines of the
   mini-solve rows a to h, the two screening tables in `gap-mini-solve-b-fable.md` and
   `gap-mini-solve-e-fable.md` Step 2.1, `library/open-core.md`). Record where the lane stands.
2. Step 1: choose one named, unattempted item and say why it is not a repeat (rule 0a grep).
3. Steps 2+: attack that item, one stage per response, each stage appended here before the next.
4. End: one RESULT line.

## Step 0. Where the lane stands (statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L297-360, the row (L1280) and the RESULT lines of
rows 1179, 1180, 1184, 1187, 1188-1190, 1193-1195; `parts/gap.md` L1-104 and L213-322; the screening tables of
`gap-mini-solve-b-fable.md` (Step 2.1) and `gap-mini-solve-e-fable.md` (Step 2.1, Steps 5-6);
`gap-solve9-astra62.md` L120-175 (the form of (N-phys)).

1. **The target splits in two (Theorem BP, row 1179; check row 1183: main chain HOLDS AFTER CORRECTION).** The
   Jaffe-Witten gap clause follows from the continuum datum of the T0 chain (OPEN) and one lattice estimate,
   (N-phys) of row 1161 (OPEN): at one admissible physical side, uniformly in the cutoff, the periodic
   centre-neutral excited trace of the cube n^3 at a time u at most n/K is at most 1/2.
2. **(N-phys) in other words (rows 1180, 1184; check row 1187: main statements HOLD).** It is a neutral lattice
   gap at arbitrarily weak coupling with a bound of asymptotic-scaling type on the seed size. In thermal form:
   the cube at aspect K is on the confined side, with a dilute gas of neutral excitations.
3. **The wall (`parts/gap.md` L321-322).** One selective inequality at every scale between first passage and the
   seed size. Selective means false for a massless factor. Tests a tool must fail on: compact U(1) at weak
   coupling, the free photon, a product with a massless factor, Theorem D2, Lemma SHEET, Proposition V (the K7
   line in theorem form).
4. **Siblings.** Rows 1188-1190 and 1193-1195 (mini-solve a to f) each screened routes from first principles
   and found every one on the lane's map (about 65 route families in all, tables in rows 1189, 1190, 1194).
   Each then worked one item to a first failing step. Rows 1197, 1198, 1200-1202 (g, h, j, k, l) have no
   result at this pin.
5. **Consequence for this row.** I do not screen route families again. Step 1 below records only the candidates
   that are not in those three tables, each with its grep. Then one item is attacked.

## Step 1. Literature probe, and what this session derived again (GUIDE; no statement here is a proof step)

### 1.1 Literature probe (arXiv API, two queries, sorted by date)

Queries: lattice gauge AND (mass gap OR confinement OR exponential decay) in math.PR and math-ph; and
(Yang-Mills OR gauge theory OR sigma model OR O(N)) AND (mass gap OR exponential decay OR confinement) in
math.PR, math-ph, hep-lat, hep-th. Newest entry seen: 2026-11-15. Result: no posted proof of a gap or of
confinement for a non-abelian lattice gauge theory beyond strong coupling. The entries that bear on the lane
are all on file already (file counts by `grep -l` over `library/gap-*.md`, `library/prior/*.md`, `FINISH.md`):
A. Mihajlovic, arXiv:2611.11534 (7 files); Yan Ru Pei, arXiv:2611.01532 (14); V. P. Nair, arXiv:2608.10133 (6);
S. Chatterjee, arXiv:2602.00436, confinement in three dimensions with a central U(1) (8). One sentence of Pei's
abstract states the lane's (SING) in two dimensions: "only odd observables transfer".

### 1.2 Candidates derived from the target in this session, each grepped before any work

Only candidates that are not in the tables of rows 1189, 1190 and 1194 are listed. Every one has a match.

| Candidate | Where it ends | Match on file |
|---|---|---|
| Fundamental Higgs with custodial SU(2), then hopping to zero (Fradkin and Shenker; Osterwalder and Seiler) | the rigid group acts trivially at zero hopping | Fradkin 18 files; row 1016 family 1 |
| Sharpness-type differential inequalities (Aizenman and Barsky; Duminil-Copin and Tassion) | need a monotone structure; none for SU(2) | sharpness 48 files, Aizenman 23 |
| Corner Hubbard-Stratonovich form: the links as an O(4) model in an annealed quaternion plaquette field, then loop soups | signs of the holonomy weights | Identity HS1, row 1016 3.3; `gap-mini-free-fable.md` 5.1 |
| Random surfaces from the multilinear action | crosscap signs (Frobenius-Schur indicator -1) | method 35; rows 737, 744, 878, 1127 |
| One-link noise acting on products of Wilson loops as a positive cone | the same sign: a reconnection inside one loop has coefficient -(1 - a_1)/2 | method 35 in other words; Mandelstam 3 files |
| Centre twist as a commutator of two removable colour twists; twist eaters | zero classical cost, so the twist cost is a logarithm of the coupling, not a stiffness | Fact T, `gap-crux-restate.md` Section 2; rows 731, 1181 |
| Spread vortex with a field-built colour axis | pays beta a^2 abs(D n)^2 with abs(D n)^2 at least c/beta on typical fields | row 1141 (2); row 1177 (14), (26), (33)-(35) |
| Thermal form: a lower bound of asymptotic-scaling type on the deconfinement coupling at temporal extent n/K | it is (N-phys) | rows 1180, 1184; "THERMAL", row 934 |
| Replica swap as a continuous family of field-dependent diagonal rotations (two replicas, sum and difference variables) | the collar cost is of mass form, proportional to sin^2 of the angle, so the sharp junction is optimal | Proposition J, checks 1121, 1123 (independent swaps); lead rule CL leaves coupled interpolations unbound |
| Durhuus-Frohlich layers with the posted two-dimensional O(4) theorem, for three dimensions first | two-sided backgrounds; worst case orders the layer | method 36, rows 1139, 1140 |
| Charged decay with a transitive rigid group gives neutral decay (a soft conversion) | false: van Enter and Shlosman weights; product examples | Proposition V; Example PROD; row 1115 2.3 |
| Stability of mixing of all observables under small perturbations (Dobrushin and Shlosman block criterion) | needs the unperturbed neutral mixing | `gap-face-stability.md` (FST-BD) |
| Mass inequalities from positivity of the measure (Weingarten; Vafa and Witten; West) | they bound the lightest mass from above only | Vafa 2 files; no consumer |

Three structural constraints that I derived again are on file: a proof at one coupling in the band reads a
number (K7, Proposition V); the gap is a property of the unique continuum object, so no model can refute a
(K-flow) tool (`parts/gap.md` test table, point 5); the neutral half is not implied by the charged half.

Verdict (GUIDE): a seventh plain-brief screening, about thirteen more candidates, no route off the lane's map.

## Step 2. Choice of attack

### 2.1 What is left to attack (ARGUED; the lane's reading, confirmed)

1. The only statement with a consumer on the path is (N-phys). Its engine (Theorem S, rows 697-699) carries a
   small neutral trace from one size to larger sizes. No engine creates the small trace: in a small box the
   neutral trace is large (a hot gluon gas), and it has to become small at about K correlation lengths.
2. The posted two-dimensional proofs create it in two halves. The charged half is the bracket gain. The neutral
   half is association of the untwisted linear-weight ferromagnet. The gauge theory has neither a rigid frame
   nor association. Rows 1011-1018, 1115-1123, 1188-1195 hold this with proofs of each obstruction.
3. So a row can do three things: a new mechanism for one half (none found here, Step 1.2), a bound with no
   association for a neutral response in a member of (SING) (the reopen condition of BR-2), or a decision on a
   side statement that an earlier row left open.

### 2.2 The item

I found no new mechanism. By rule 0a I do not attack the items of Step 1.2 again. I take the third kind, and
only one bounded item: the diamagnetic comparison for S^3 sheets with one-sided twists. Row 1194 5.1 records it
as "neither proved nor on file"; method 36 (rows 1139, 1140) settles the two-sided form by a counterexample.
What it can give: the answer to that recorded question, in three parts (unnormalized; normalized for charged
two-point functions; neutral covariances). What it cannot give: any step toward (N-phys). It is off the path,
and I say so before starting.

Pass and fail criteria of the guide run, written before the run: on four small graphs (triangle, square with
a diagonal, K_4, a five-site bridge graph), at four couplings, compare abs(E_g[n_x conj(n_y)]) under one-sided
twists g (a centre twist, two anticommuting twists, two Haar-random fields) with the untwisted E_1[<n_x, n_y>].
A violation is a difference above 6 standard errors and above 0.004. A run without a violation is no proof.
