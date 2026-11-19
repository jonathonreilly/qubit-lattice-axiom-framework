lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:59Z

# gap-mini-solve-b-fable (queue row 1189)

Pinned at commit f7e5907e5 of `claude/ym4d-hard-route`. Research-stage working state. It grants no status. Nothing here is a public claim.

**The problem (row 1189).** Prove that four-dimensional SU(2) Yang-Mills theory has a mass gap, in the sense of Jaffe and Witten.

**Labels.** Each statement below carries one of: PROVED (every step written here or in a cited checked note), ARGUED (an argument with a named unproved step), GUIDE (heuristic or numeric guidance, never a proof step), OPEN.

**Process.** One step per response. Each step is appended here before the next one starts.

## Step 0. Plan (written before reading the earlier work)

1. Read the earlier work on the gap: the FINISH.md RESULT lines for the gap rows, `parts/gap.md`, `library/open-core.md`, and the notes the newest gap rows name. Record what is established and what is open. No duplicate attack (rule 0a).
2. Choose one line of attack on the first open statement the gap needs. Say why it is not a repeat.
3. Carry it through, or name the first step that fails, with the explicit failure.

(Steps follow.)

## Step 1. What the earlier work fixes (read, not re-derived)

Sources read at this pin: `FINISH.md` rows 1007-1018 and 1179-1187 (RESULT lines), `parts/gap.md` L1-104 and the route registry L223-267, `library/gap-council-synthesis.md` in full, `library/gap-mini-branch-fable.md` L300-312. None of these is evidence by itself. Each says where a proof and its check are.

1. **The target splits in two (rows 1179, 1065; check row 1183: main chain HOLDS AFTER CORRECTION).** The Jaffe-Witten gap clause follows from (i) the continuum datum of the T0 chain (existence, with (H2), (TOT)), which is OPEN, and (ii) one lattice estimate, (N-phys), which is OPEN. The Wilson branch selection (BS) enters only the wall (W) as worded (confinement on tori), not the gap clause.
2. **(N-phys) (row 1161, `gap-solve9-astra62.md` L146-148).** At one admissible physical side L, for every cutoff index j >= j_0, with n_j = L/a_j, there is an integer u_j with 3 <= u_j <= n_j/K and s_+(u_j; n_j^3) <= 1/2. Here s_+ is the periodic centre-neutral excited trace of the cube n_j^3 in units of its vacuum. Rows 1180 and 1184 (two independent attacks, unchecked at this pin; check row 1187 running): (N-phys) is a neutral lattice gap at arbitrarily weak coupling together with an upper bound of asymptotic-scaling type on the seed size. Nineteen routes ended at steps already on file.
3. **The map.** Route families RA-RG, LC, BR-2, (T-pin), (DS-W), (A) and methods 1-36 of `parts/gap.md`. The common verdict (row 998 6b): every engine found is blind, and no input excludes the massless branch beyond first passage. Comparison cases that a proof must fail on: compact U(1) at weak coupling, frozen Q_8 and 2T, the K7 endpoint (mixed action), the free photon, a product with a massless factor.
4. **The 2D precedent (rows 1007-1010, reading only).** The posted 2D O(N) proofs cross the band by a stiffness iteration on pinned cells. The gain per scale is a commutator (curvature) term. Rows 1011, 1016, 1018 (Fable 5.2 max, with gpt-6-astra checks): the direct port fails in the class of all pins (Propositions B, B', Theorem BH). SU(2) has the bracket and no symmetric continuous twist. Compact U(1) has the twist and zero gain.

So the open lattice statement is one sentence: **a selective gain at order-one response**. Step 2 chooses the attack.

## Step 2. Choice of attack

### 2.1 Screening (GUIDE; no statement here is a proof step)

Before choosing, I derived candidate routes from the Jaffe-Witten target alone and searched the lane for each (`grep` over `library/gap-*.md` and `parts/gap.md`). Every one has a match. The count is the number of lane files that name the tool.

| Candidate, from first principles | Where it ends | Match on file |
|---|---|---|
| Orbit-space curvature, Bakry-Emery, Helffer-Sjostrand with the O'Neill term | the positive Ricci term is cancelled at order one by the averaged paramagnetic term (lattice Ward identity) | method 31; Helffer 16 files, O'Neill 10, Singer 15 |
| Convex Gribov region, log-concave Faddeev-Popov weight | magnetic energy is not convex | Gribov 15, Zwanziger 10 |
| One-link conditional randomization (Simon and Yaffe) | charged lines only; ultraviolet self-energy | 3 files; route (A), rows 1132-1138 |
| Finite-volume trace anomaly, virial sign | a sign in beta with no number | route RB; rows 710-715 |
| Gradient-flow coupling t^2 E(t) as a twist-free neutral stiffness | Hamilton's monotonicity gives only "the action decreases"; no consumer | `gap-outside-box-max.md` I15 |
| Lee-Yang property of S^3 with beta as the field | true in 2D (zeros of I_1); no zero-free region in 4D | route B9, Lemmas LYP, LYP2; `parts/gap.md` L281 |
| Migdal-Kadanoff recursion (Ito 1985; Mueller and Schiemann 1985) | no comparison with the true lattice; confines 4D U(1) too | route RG; rows 797-801 |
| Durhuus-Frohlich layers; anisotropic 2+2 split; frozen planes | uniform mixing over backgrounds fails; (SING); (MON-L) | method 36; BR-2; rows 1053, 1072-1115 |
| Central twist, vortex containers (Mack and Petkova) | flux half only | council 2c; rows 731, 1018 |
| Pinned-cell stiffness iteration (the 2D engine) | SU(2) has the bracket and no symmetric continuous twist | rows 1011-1018, 1118-1123 |
| Static-potential (force) scheme, concavity (Bachas) | a running-coupling inequality at all scales, as RA | route RA |
| Correlation inequalities for plaquette energies | none known for SU(2); wrong direction for decay | GKS: `parts/gap.md` test table |

Three constraints that I re-derived are on file too. (i) The neutral gap at a fixed coupling in the band reads a number: the mixed action has a critical end-point close to the Wilson axis (K7). (ii) Reflection positivity, gauge invariance and perturbative data do not separate theta = 0 from theta = pi (16 files). (iii) A fixed colour axis has a mass-form twist cost (row 1181 Lemma 5.1a; Lemma FR).

Verdict (GUIDE): this screening found no route off the lane's map. It agrees with rows 1128-1130 and 1179-1184.

### 2.2 The attack chosen

**Item.** Route S2 of row 1103 (`gap-face-exercise-fable.md` L1051-1054, L1318-1327), first stated as a remark in row 1053 6.8 (`gap-wall-vectors-max.md` L296-298): the doubly flat corner, beta_L = beta_T = infinity, mixed coupling beta. Row 1103 records it as "not attempted beyond the kill pass". Row 1053 records it as a corner "at which a theorem looks reachable".

**Why this one.** It is the only place on the map where all three hold at once: (a) the model is four-dimensional and comes from Wilson SU(2) by a limit of plane couplings; (b) it has an exact continuous non-abelian symmetry with a transitive action on boundary data, so the missing object of rows 1011-1018 (a symmetric twist with a bracket) exists exactly; (c) no row has attempted it. Its U(1) version is believed massless (row 1053), so a proof must be selective.

**What it can and cannot give.** It cannot give the Jaffe-Witten gap. Row 1103 marks S2 "wounded twice": the end-point is open, and the two descents to the isotropic point control different rates. So the plan has two parts.
- Part A (Steps 3-4): the end-point. Reduce the gap at the doubly flat corner to one statement about a two-dimensional model, with every identity written. Then attack that statement.
- Part B (Step 5): the descent. Decide by a hand estimate whether the symmetric twist of the corner survives when the in-plane curvature is unfrozen. This is the step that decides whether Part A is on the path of (N-phys).

Stop rule: a proof, a counterexample, or the first failing step with its explicit failure, for each part.
