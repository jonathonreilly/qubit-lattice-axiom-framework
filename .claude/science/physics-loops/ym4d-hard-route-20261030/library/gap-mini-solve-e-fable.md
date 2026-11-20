lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T12:00Z

# gap-mini-solve-e-fable (queue row 1194)

Provenance: Claude Fable 5.2, max effort, Mac mini worker 2, one session, pinned at commit 36be8070a. Not an audit. Not checked by another model. Start 2026-11-20T00:00Z (`date -u`).

Problem of the row: prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

Labels used below: PROVED (every step written here, by hand), ARGUED (argument written, a step is not fully written or rests on a named input), GUIDE (numeric or heuristic, never a proof step), OPEN.

Status of this file: in progress. Sections are appended step by step.

## Step 0. Plan (written before any reading of earlier results)

1. Read the RESULT lines of the sibling rows (gap-mini-solve-a to -d) and of the gap lane, `parts/gap.md` (method list, route registry, test table) and the route screening table in `library/gap-mini-solve-b-fable.md` Step 2.1.
2. Name the exact open statement the lane has reduced the gap to, and the attacks already on file for it.
3. Choose one attack that is not on file, or one named unattempted item, and carry it to a proof, a counterexample, or one precise lemma with the reason each way failed.
4. Rule 0a: before a statement is called new, grep `library/open-core.md` and the FINISH rows for it.

## Step 1. What the record holds (read in this session; statements about the record, not evidence)

Read in full: `GOAL.md`; `FINISH.md` L1-84 and L299-360; the row (L1275); the RESULT lines of rows 1178-1190 and 1193; the three sibling files `gap-mini-solve-a-fable.md`, `-b-`, `-c-` and the start of `-d-`; `parts/gap.md` L1-104 and L213-322; `library/gap-council-synthesis.md`.

1. The lane reduces the Jaffe-Witten gap clause to two open inputs (Theorem BP of row 1179; check row 1183: main chain HOLDS AFTER CORRECTION): the continuum datum of the T0 chain, and one lattice estimate (N-phys) of row 1161. (N-phys) is a neutral gap with a level count on one periodic cube of fixed physical side, uniformly in the cutoff. Rows 1180 and 1184: it is a uniform neutral lattice gap at arbitrarily weak coupling with an asymptotic-scaling bound.
2. The wall in the lane's words (`parts/gap.md` L321-322): one selective inequality at every scale between first passage and the seed size. Selective means false for a massless factor.
3. Siblings of this row. Row 1188 (a): the pinned-slice Ward route, Lemma PC. Row 1189 (b): the doubly flat corner, Theorem A8, stop at (Sigma-unif) and (SING). Row 1190 (c): seventeen candidates on file; cube identity; chi-square form of (N-phys). Row 1193 (d): started, no attack written at this pin. Each sibling found the lane's map again and advised against one more fresh choice of route.
4. Consequence for this row: I do not screen routes again. I choose one mechanism question and work it to a proof or to a first failing step.

## Step 2. Choice of attack (written 2026-11-20T00:51Z, `date -u`)

### 2.1 What was screened in this session (GUIDE; statements about the record)

I derived routes again from the target and grepped each before any work. Each has a match. I list only the ones that are not in the tables of rows 1189 and 1190.

| Route, from first principles | Match on file |
|---|---|
| The Witten Laplacian on exact one-forms: the glue half as the ground energy of one adjoint ("gluelump") particle | `gap-brainstorm-max.md` L299 (idea 20), `gap-next3-max.md` L336 (C6), rows 957, 968. My own count: the Ricci term is cancelled to every order of perturbation theory, because the true gap is of order exp(-c beta). So an averaged-curvature bound of order one cannot hold in the band (ARGUED) |
| The thin twisted torus with a dilute gas of fractional instantons (Tanizaki and Unsal) | Route T, rows 678-684, 842, 856, 862 (Theorem S1, Lemma PE; open above the vortex spacing M_1) |
| Centre twist as a double rigid colour twist with anticommuting transition elements; the zero-action twist eater | rows 731, 1013 (Lemma TWIST, C1, C2), row 1181 (Proposition J) |
| Singlet response to a far bond cut as an average over Haar twists on the cut | reduces to a singlet covariance again; rows 1115-1123 hold the conversion question (CONV), (RESP-TR) |
| Convexity in the coupling: the volume-normalized energy variance is integrable in beta, uniformly in the volume | elementary; no pointwise consequence (a free photon has a finite specific heat and no gap) |
| The SO(3) x Z_2 form (Mack and Petkova; Tomboulis): given the SO(3) field, the centre field is a Z_2 gauge theory | 62 files name Petkova, 88 Tomboulis; flux half only (council 2c) |
| Feynman-Hellmann and a continuity method in beta from strong coupling | (NOCRIT-HF), rows 859, 878: needs a lower bound on the lattice beta function |

So the screening of rows 1189 and 1190 stands. I add no route.

### 2.2 Where every route stops, in one sentence (ARGUED; the lane's reading, row 1115)

The posted two-dimensional proofs reach singlet observables only through association of the untwisted O(4) ferromagnet (OpenAI Section 3.11, as read in row 1009 and `library/prior/gap-o4-pinned-cell-read-opus.md` L128-141). In four dimensions every observable is a singlet, link coordinates are uncorrelated by Elitzur's theorem, and associated uncorrelated variables are independent. So no association of link coordinates exists, and the glue half needs another conversion from charged decay to singlet decay. The lane names this step (SING), with the cleanest open member (K4-N) (`gap-sing-direction-fable.md` L144-150): a neutral bound for the constrained law (K4), "the first neutral bound for interacting non-abelian sheets with no association".

### 2.3 The attack chosen

**Item.** The conversion step in its smallest exact instance: the family K_N of N sheets with product one (N = 4 is the lane's (K4); it is the doubly flat corner of row 1053 with a fibre that is one cycle; rows 1110 and 1189).

**Why.** (a) It is the named first lemma of the neutral half in the lane's own registry (BR-2 reopen condition). (b) It has a rigid group that is transitive on the one-site space, so the charged half is supplied (GIVEN the posted estimate (3.61); row 1110 (O5), row 1115 3.2). (c) I found an exact structure of K_N that is not on file under the words I grepped ("convolution" in the corner and face files, "Plancherel", "charge gas", "Coulomb gas", "random walk on"; `library/open-core.md` has no line on K4, on a corner or on a cycle): K_N is a convolution power on the group of sheets, and it has a positive dual gas of non-abelian charges. Step 3 proves it. Steps 4 and 5 use it on (K4-N).

**What it can give.** Not the Jaffe-Witten gap. By row 1115 2.2 the family (SING) is not on the path from the target; BR-2 fully proved stops at C_beta. A proof of (K_N-N) would be a mechanism for singlet decay with no association. A failure names the first step that a mechanism has to supply.

**Stop rule.** A proof, a counterexample, or one lemma that failed in three written ways.
