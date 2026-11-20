lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:57Z

# gap-mini-solve-h-fable (queue row 1198): the mass gap of four-dimensional SU(2) Yang-Mills, eighth plain-brief row

Worker: Claude Fable 5.2 (max) on the Mac mini, single session, no subagents. Pinned at commit f763c22f1 of
`claude/ym4d-hard-route`. Started 2026-11-20T02:57Z (date -u). Research-stage working state; nothing here is a public claim.
Labels used below: PROVED (a written argument, complete in this file or cited to a checked row), ARGUED (an argument
with a named gap), GUIDE (numeric or heuristic, never a proof step), OPEN.

## 0. Status log (one line per step, times from `date -u`)

- 2026-11-20T02:57Z: file created; reading the row, GOAL.md, the rule sections of FINISH.md.
- 2026-11-20T03:32Z: record read; blind pass done (Section 1). Every candidate named blind was grepped at once; all with a mechanism are on file.

## 1. Repo search and where the record stands (GUIDE: statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L299-362, row 1198 and the RESULT lines of rows
1186-1215; `parts/gap.md` L8-104; `library/gap-council-synthesis.md` L19-131; `library/gap-solve9-astra62.md`
L60-150 (row 1161, gpt-6.2-astra, checked by row 1162); the head of `library/gap-solve21-astra62.md` (row 1204);
`library/gap-phys-seed.md` L343-375 (row 720); the section lists of the sibling files g, i, k, l. Cross-branch
search: not repeated; rows 1188-1201 ran it and row 1204 cites the lead search of 8 November.

### 1.1 The open statements (cited, not re-proved)

1. **(N-phys)**, `gap-solve9-astra62.md` L148: on one periodic cube n^3 of one admissible physical side, uniformly in
   the cutoff, the centre-neutral excited trace s(u) at u = floor(n/K) is at most 1/2. Row 1179 (Theorem BP) says the
   Jaffe-Witten gap clause needs (N-phys) and the continuum datum of the T0 chain. Both are OPEN. The periodic wall
   (W) needs the branch selection (BS) in addition.
2. **The wall in one sentence** (`parts/gap.md`, State of attack): every engine found is blind to the group. The one
   selective fact that is provable today is asymptotic freedom at weak coupling. No step is known that carries it
   through the band of order-one coupling.
3. **Lead rules that bind a new row** (`parts/gap.md` L76, L97): no further fresh-framing list; a (K-one) input is a
   one-scale property and is tested against Proposition V and the K7 endpoint; a (K-flow) input reads the first-passage
   data of Wilson SU(2) and must fail for a product with a massless factor. "No mechanism for the selective step is
   on record."
4. **Siblings.** Rows 1188-1201 (a to k) each found the lane's map again and then worked one small item. Row 1202 (l)
   is running and says it repeats no screening.

### 1.2 Blind pass of this row (GUIDE; each line was derived from the target before reading, then grepped)

Counts are files among `library/gap-*.md`, `library/prior/gap-*.md`, `parts/gap.md` (one `grep -l -i -F` loop).

| Candidate derived blind | Selective? | Where it sits on the record | Status |
|---|---|---|---|
| Thermal form: (N-phys) is p(T)/T^4 at most log(3/2)/K^3 = 3.0e-9 at T = K/L; flow form "interaction measure Theta = eps - 3p at least gamma p" (then p/T^4 falls like T^gamma) | yes: Theta = 0 for a free photon, Theta has the sign of the beta function at weak coupling | route RB (row 934); (MONO-Delta), Proposition MB, Proposition NM `gap-phys-seed.md` L351, L353, L375; (NOCRIT) `gap-mid-max.md` L207; (CAS) row 708 | on file; "restates the seed in steps" |
| Spectral form of the same: every neutral level of the box, in units of 1/L, grows with L; lattice form: at fixed n the neutral gaps of the transfer operator fall when beta rises | same | same family; (U1), (U2) `gap-hcphys-max.md` L135 | on file; needs a Griffiths-type inequality that SU(2) does not have |
| Concavity of log(p/T^4) in log T as the carrier of the first-passage slope | yes | not found by name | FAILS as a belief: at a continuous deconfinement point with a positive specific-heat exponent the second derivative is plus infinity; for p/T^4 itself the inflection sits where p/T^4 is of order 0.01 to 0.1, not 3e-9 |
| Integrate all links through positive auxiliary fields (Budczies-Zirnbauer weight; for the Wilson weight the two-stage quaternion Gaussian); the dual model couples site-local quaternion Gram entries by O(4) inner products | no (the U(1) form is an XY ferromagnet of relative phases, the SU(2) form has the Hopf signs again) | idea 28 `gap-brainstorm2-max.md` L178, L233; C4 `gap-invent-selective-max.md` L113, L194; Identity HS1 `gap-global-reform-max.md` L382; row 1157; row 1199 table | on file |
| Hopf split with Ginibre and FKG (the neutral step of the posted 2D O(4) proof); SU(2) matrix entries carry the sign of U_21 = - conj(w), K_4 is not bipartite | - | row 1084, Lemma HF (row 1188), row 1190 | on file. Remark, not on file by name: the sign is exactly compactness (for SU(1,1) all eight monomials have coefficient plus one); no consumer |
| Durhuus-Frohlich with the posted 2D O(4) theorems (3D area law at every coupling) | flux half, 3D | method 36 `parts/gap.md` L70 (row 1139, check 1140): no background-uniform rate at large b; rows 825-834; row 1199 | on file, dead in uniform form |
| Reduction on a 1 x 1 or 2 x 2 twisted two-torus (a 2D model that is semiclassical at weak coupling) | no engine from a small box: a seed needs n m at least K log 2 (row 1184, Lemma N2) | Route T, (AC'), row 842, `gap-ac-lat.md` | on file |
| Spacetime symmetries as the rigid non-abelian group (shifted and rotated periods, stress-tensor response) | no: the free photon passes | row 1201 (`gap-mini-solve-k-fable.md` L84), rows 960-965 | on file |
| Projective (Birkhoff) contraction: cross-ratios of the one-step kernel do not see the spatial weight | no | statement (A), row 1132; 22 files name Birkhoff | on file; the diameter is extensive |
| Born-Oppenheimer lower bound over a block map; Kirsch-Simon comparison | no | not by name; in substance rows 957, 968 (two-level Poincare; Holley-Stroock loss is extensive) | on file in substance |
| Rokhsar-Kivelson form: the Kogut-Susskind operator is the Langevin operator of the 3D Wilson measure minus a positive potential | no | 2 files; ground-state forms rows 863, 957 | on file; eigenvalue differences are not monotone under it |
| a-theorem and thermal counting of massless modes | excludes three free photons only | `prior/gap-kflow-read-opus.md` L99; `gap-direction3-max.md` L474 | on file |
| Fixed-lattice weak-coupling value D(n; beta) = (3/2) log beta + O(log log beta) (twelve quartic constant modes, marginal divergence of the SU(2) matrix integral in four dimensions) | base only | `gap-phys-seed.md` L451 (Item 6) | on file (my first count, 9/4, was wrong: the three global gauge directions are angular directions of the twelve constant modes) |
| Gap from confinement ("all states are flux"); neutral trace bounded by the untwisted periodic excess | needs a Lebowitz-type inequality | row 1190 list; rows 1161 (9), 1179 | on file |
| Other regularizations with a positivity structure (deformed theory on a small circle, finite subgroups, quantum links) | - | row 1190 ("on file in part"); 4 files name deformed Yang-Mills | none reaches R^4 without the same band |

Result of the pass: an eighth screening finds the map again. No candidate with a mechanism is new. Two remarks have
no file hit by name (the failure of log-concavity of p/T^4 at the deconfinement point; the SU(1,1) remark), and
neither has a consumer.
