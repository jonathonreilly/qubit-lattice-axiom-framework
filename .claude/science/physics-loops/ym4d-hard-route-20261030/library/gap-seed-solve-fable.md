lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T15:36Z

# gap-seed-solve-fable (queue row 1510): crux attack on the physical seed (PUR-io)

Started 2026-11-25T03:36Z (date -u) at commit 43b92735c on branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim. Unchecked when written.

## 0. Status log

- 03:36Z started; reading the row, the rules and the inputs.
- 03:40Z read: FINISH rules, row 1510, RESULT lines 1496-1502 and 1461/1462/1465, gap-k2-tool-design-fable 2-3.3, gap-k2-direction-checkpoint-fable in full.
- 03:51Z read: gap-r8-loop-consumer-fable 1.3-2.2 ((W), Lemma GF), gap-k2-direction-checkpoint-check-astra62 in full. Thinking recorded in Section 1 next.
- 03:56Z read: row 1474 3.5 (open bridge step), Theorem W statement (gap-ds-gauge 3.1). Long thinking pass done; writing Section 1.
- 04:02Z Sections 1-2 written; cross-branch search started in the background.
- 04:05Z cross-branch search done: main (83 mass-gap .md files) and PR 10114 (12 MASS_GAP files), pattern 'weighted Poincar|Poincare ... (probability kernel|block kernel|image measure)|PUR-io': no hit. Read Lemma LD-1 and Corollary LD-2 (gap-crux-direction-fable.md L255-281): LD-2 caps the stiffness from above and gives no lower bound, so it does not give the floor of Corollary NF below.

Labels used below: **proved** (a written proof is in this file), **read** (I read the statement in a row or
source and did not re-derive it), **sketched** (argument outlined, steps missing), **guessed** (my judgment),
**guide** (heuristic number, never a proof step). Nothing here is checked by another model.

## 1. The target and the frame (read; nothing new in this section)

- Target (row 1468, 3.1, Fact PUR; checks 1462, 1465). T is the Wilson transfer operator at beta_K on the
  spatial torus of side n = l b^K, u = n/512, Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2. (PUR-io): P_K is
  at least 457/625 at infinitely many K, for one l and one g_0. It gives s_K(u) <= 4/21 and a gapped
  calibrated limit.
- Readings on file, which I use and do not count: 1 + s = Z_+(u)/lambda_0^u is the neutral thermal sum
  (rows 1367, 1386, 1496 2.1); the rank-one (Hilbert-Schmidt) test of rows 1373, 1461; the replica swap
  (rows 1131, 1201, 1337). In one line: with r_i the neutral eigenvalue ratios, s(u) = sum of r_i^u is the
  sum of the squared canonical correlations of two time slices at lag u/2, and log(1 + s) is 512^3 times
  the pressure over T^4 at temperature T = 512/l. So the seed says: the pressure of the theory at T = 512/l
  is below 1.3e-9 T^4 (guide arithmetic: log(25/21)/512^3). With a mass m this needs m l of order 1e4.
- Closed lines that I do not restate as progress: Theorem K2 and 2.4 of row 1496 (every class of a chain
  already has the purity); check 1484; the end class at beta <= 0.00872 (rows 1471, 1473); the release floor
  (rows 1464, 1470); the weak-side tests (rows 1472-1495); (W) and Lemma GF (rows 691, 1498, 1501); the
  registry of triggers (R1)-(R9).
- The two statements left open by the checks: check 1497 (i) (can a class restriction concentrate the
  selective estimate in an entry bound, one transition or the terminal bound, and does that help?) and
  check 1501 (the truth of (W) at side 4 and beta = 23/10). Section 3 answers the first for three explicit
  families of classes. I did not decide the second (Section 4.4).

## 2. Repo search

- Local: `grep -l -i -E "weighted Poincar"` on `library/gap-*.md` and `library/prior/*.md`: no hit.
  `library/open-core.md`: no entry for PUR, purity, the seed or a Poincare carry (grep, 2 unrelated hits).
  `library/open-registry.md`: no hit for PUR-io. Relatives that are on file and that I cite where used:
  Lemma LD-1, LD-2 and Theorem LOSS (row 1460), Lemma NG (row 1474 2.3), Proposition G1 (row 1128),
  Lemma MARG / Proposition SIGMA and Theorem TS-J (row 957), Proposition AVG (row 968 5.4), the two-block
  product defect (row 1474 2.5), Theorem W (row 691), the open bridge step (row 1474 3.5), Lemma BT (row 1353).
- Cross-branch (main and PR 10114, mass-gap files only, bare blob-less fetch in a /tmp scratch folder): see
  the status log for the result.
