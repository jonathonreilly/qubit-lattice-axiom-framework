lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T14:01Z

# gap-mini-solve-g-fable (FINISH row 1197): the mass gap of 4D SU(2) Yang-Mills, plain brief

Research-stage working state. Nothing here is a public claim. Every statement carries one of the labels
PROVED (a written argument in this file or a cited checked row), ARGUED (an argument with a named gap),
GUIDE (numeric or heuristic evidence, never a proof step), OPEN.

## 0. Status log

- 2026-11-20T02:01Z start. Pinned commit 35f40c473. Read GOAL.md, FINISH.md L1-84 and row 1197 (L1278). File created.
- 2026-11-20T02:28Z Section 1 written (record and first screening). Attack not yet chosen; Section 2 will state it.

## 1. Repo search and where the record stands (GUIDE: statements about the record, not evidence)

Read in this session: `GOAL.md` in full; `FINISH.md` L1-84, L320-350, row 1197 and the RESULT lines of rows
1185-1210; `parts/gap.md` L1-104 and L223-322 (state of attack, route registry, test table, price);
`gap-crux-restate.md` L20-125 (definitions, Theorem D, candidates C1-C5); `gap-solve9-astra62.md` L1-160
(row 1161: the Pfaffian seed (7), the one-cube theorem (8)-(10), the finite-aspect statement and its
consumer); `prior/gap-2don-proofs-read-opus.md` L30-125 (digest of Ding, Huang and Yang and of OpenAI);
the head of `gap-solve21-astra62.md` (row 1204, the relativistic test (1)-(2)); the plans of the sibling
files i and k (both in progress, no attack named yet).

1. **The open lattice statement.** (N-phys) of row 1161 (gpt-6.2-astra; checked by row 1162): on one periodic
   cube n^3 of fixed physical side, uniformly in the cutoff, the centre-neutral excited trace s(u) at a time
   u at most n/K is at most 1/2. Row 1179 (Theorem BP) says the Jaffe-Witten gap clause needs this and the
   continuum datum of the T0 chain, and not the branch selection (BS). Row 1184: (N-phys) is the crux lemma
   (GLUE-FP) of rows 895 and 920 with other constants. All OPEN.
2. **The wall in one sentence** (`parts/gap.md` L321-322): one selective inequality at every scale between
   first passage and the seed size is missing; selective means false for a massless factor.
3. **What a tool must fail on** (test table, `parts/gap.md` L268-309): compact U(1) at weak coupling, the free
   photon, a product with a massless factor, Theorem D2 (supremum over tilts), Lemma SHEET (uniform over
   coupling fields), Proposition V (peaked weights at a first-order point), and non-local weights from
   integrated matter (so a tool must use the Markov property of the Wilson weight or first-passage data).
4. **The two posted 2D O(N) proofs** are the only all-coupling proofs of a gap in an asymptotically free
   model. The lane ported OpenAI's bracket step (rows 1009-1016, 1076-1086, 1188, 1193, 1195: fails in the
   class of all pins, the conditional abelian model is frustrated, no global non-abelian symmetry on the
   integration variables). For Ding, Huang and Yang the digest marks every key input "NONE" in 4D
   (`prior/gap-2don-proofs-read-opus.md` L96-110).

**Registry grep before choosing** (count of files among `library/gap-*.md`, `library/prior/gap-*.md`,
`parts/gap.md` that contain the term; done with one `grep -l -i` loop). Zero hits: "mass inequalit",
"colour-flavour", "induced QCD", "Savvidy", "shifted bound", "Parisi-Wu", "reflection coupling", "Eberle",
"Fredenhagen-Marcu", "holonomy flow", "Hardy", "Born-Oppenheimer", "Dirichlet-Neumann". Present (so not new by
name): Vafa 2, Zirnbauer 2, paramagnet 10, Nielsen 11, Singer 21, O'Neill 12, orbit space 24, Karabali 3,
Feynman 39, trace anomaly 17, Cheeger 6, Ollivier 5, Wasserstein 17, path coupling 2, Lieb-Robinson 3,
instanton 30, abelian projection 10, Witten Laplacian 13, Brascamp 31, van Baal 37, Zwanziger 15, Gribov 24,
Simon-Lieb 12, hypercontract 37, Knabe 23, martingale 47, Luscher 48, step scaling 19, tunnel 43,
adiabatic 13, semiclassical 18, min-max 34, variational 86.

**First screening (GUIDE; each line is a route I derived blind in this session and then found on the map).**

| Route derived blind | Where it already sits |
|---|---|
| Fixed-coupling form: a seed at one coupling of the window plus a carrier to finer cutoffs | `parts/gap.md` L26-28; set-aside method 23 (row 978) |
| Gronwall in beta: d log m / d beta bounded below; equivalent to "no zero of the lattice beta function"; action sum rule | (NOCRIT), (VIR-log) `gap-mid-max.md` L172, L207; row 859 G8 |
| Thermal form: (N-phys) is "pressure over T^4 below 3e-9 at one temperature"; coupling integration | route RB; row 934; Theorem D (f) |
| Uniform Poincare inequality of the 4D Gibbs measure gives the gap | route RF; rows 957, 968, 982 |
| One-sided renormalization inequality on tori (contraction of D under doubling) | (CAS), route RA |
| Stiffness under a twist needs a global symmetry; SU(2) has only the centre | rows 1011, 1013, 1016 (Lemma CEN+) |
| Time-independent gauge rotations in temporal gauge as the global group | rows 944-952; row 1190's list |
| The layer of time-like links as an O(4) model in an SO(4) background; Durhuus-Frohlich | rows 712, 825-834, 1139 |
| Wilson weight as a Gaussian in two-link transporters; quaternion auxiliary field | `gap-brainstorm-max.md` L329; row 996 Identity MIX; row 1194 D1 |
| Signs of real coordinates as coupled Ising gauge fields; SO(3) matrix-entry expansion | method 35 (rows 1127-1133); row 1190 |
| SO(3) x Z_2 split, Z_2 monopoles as the frustration of the conditional Ising gauge theory | rows 1155-1175 (adjoint-only forms); Mack and Petkova in row 1025 |
| Tomboulis decimation needs a sign for bond moving on the ratio | rows 1025, 1029; row 876 item 16 |
| Thin twisted torus, fractional instanton gas, adiabatic continuity | Route T, (AC'), row 842; C5 of row 697 |
| Rotation-twisted tori (non-abelian point group characters) | rows 960-965 (vargeom, rotgeom) |
| Massless photon is not protected by a symmetry in SU(2), but an adjoint-Higgs Coulomb phase shows that "only a Z_2 one-form symmetry" does not give a gap | test table last row (non-local weights); row 1017 |

So a seventh screening finds the map again. The next section picks one mechanism and works on it.
