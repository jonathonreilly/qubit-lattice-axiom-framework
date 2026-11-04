# LW1, pass 1 (long draft): the law and its consistency

Written 2026-11-04 by a Claude Opus 5.5 subagent, as pass 1 of part LW1 of the TOE assembly (method of open PR #10138: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "Proposed specification" means: exact text for the owner to decide. Nothing here is a verdict.

**Source revisions read** (all through `git show`, `git grep` and `gh pr view/diff`, never a working tree; `git fetch -q origin` run first on 2026-11-04):

| Ref | Commit |
|---|---|
| `origin/main` | `f5af11cd01` |
| `origin/claude/toe-assembly` (skeleton) | `7d26e9bb89` |
| `origin/docs/candidate-laws-working-set` (PR #10140) | `44556f8556` |
| `origin/docs/consolidate-gauge-matter-registers` (#10126) | `7086189d10` |
| `origin/docs/consolidate-chirality-doublers` (#10131) | `a1bced899b` |
| `origin/docs/consolidate-d4-route` (#10130) | `899b749fed` |
| `origin/docs/consolidate-records-born` (#10124) | `d501c51fd4` |
| historical register with the full CL-1 text, `origin/claude/candidate-law-cl3-read-once-20261019` | `4603a51acd` |

Closed source PRs read through `gh pr diff`: #9872, #10016, #10091, #10093, #10094, #10096.

**Owner guidance applied (2026-11-04).** "our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". So the axioms are read plainly. Where LW1 needs more than they say, this draft writes a proposed specification with its exact text and reasons.

**Working set used.** PS-1, PS-2, PS-3, PS-4, PS-6, PS-7, PS-11, as they will land in `docs/CANDIDATE_LAWS.md` (PR #10140). PS-5 is "no change": build on cells of qubits.

**One tiny exact check.** One scratch script (216 x 216 matrices, under 100 MB, under 5 s) checked the band formula, the covariance group and a dispersion coefficient of the cube tick. It guides only. Every statement below that it touches has its own written proof. Its numbers are quoted where used, labelled "[check]".

---

## 0. The target, quoted

From the skeleton (`TOE_ASSEMBLY.md`, LW1 (a)):

> "There is a law `L = (U, rho_0, Act)` — an update `U` as in PS-1, an initial state `rho_0` with no records (PS-4), and an actuality and formation rule `Act` (PS-3) — such that, for every finite box `Lambda` in `Z^3` and every tick `n`:
> 1. (*Admissibility*) for every site `x`, the conditional law of the possibility a record forming at `x` locks depends only on the conditions on the six neighbours of `x` [**open input LW1-i**: the plain reading that "conditions" include the joint state of the neighbourhood after the last gate layer], and the map from conditions to law is covariant under translations and proper cubic rotations;
> 2. (*Record*) each site carries at most one record, and records are permanent;
> 3. (*Consistency*) the finite-box laws are consistent under inclusion and have a limit on `Z^3 x N` [**open input LW1-ii**: infinite-volume existence for the chosen `Act`];
> 4. (*Uniqueness up to choice*) the specifications S fix `L` up to the named free constants, listed with the parts that read them."

The task brief adds five concrete items (a)-(e). This draft follows them in order.

## 0.1 Summary of the outcome

- **Chosen law: the cube tick**, in its minimal form (one fermion mode per site, flux `pi` on every unit face, two Margolus tilings, step angle `eps`, mass angle `mu`), gauged by `U(1)` link registers under PS-6, with the PS-7 sea as vacuum, and the PS-3 transport with a law-level copy rule for formation. Section 4 states it in full.
- **The D4 event law is not a second law.** Proved here: the cube tick's own event set is a D4 lattice with time along a root (Theorem A3). The D4 law as written is a Euclidean weight; it is not a PS-1 update (Theorem B12, with #10096 for fermions). Its `W(F4)` protection becomes a target for the zoom (LZ1), and its Euclidean weight is the natural comparison object for the T0 bridges Y1 and Y3. No combined law clause is needed.
- **Proved here:** the exact covariance group of the cube tick (Theorem A2); that no one-mode, number-conserving, quasi-free update is covariant under all of `Z^3` and the site rotations unless it is trivial (Theorem B2); exact `U(1)` Gauss laws for the gauged tick (Theorem B4); that one mode per site gives no non-abelian frame group for the tick (Theorem B5); existence and finite-box uniqueness of the PS-3 transport (Lemma B6, Theorem B7); the Admissibility and Record checks under the copy rule (Theorem B9); the PS-7 sea, exactly half filled and stationary (Theorem B10); the D4 event geometry (Theorem A3); the tree-level dimension-six term of the tick (Theorem C1); infinite-volume existence of the whole law (Theorems E1-E6).
- **Found here (counterexamples or conflicts with the working-set text as worded):**
  1. PS-11 read over all statements is inconsistent for every atomless history law, and the PS-7 vacuum gives one (Theorem B11). A countable reading repairs it (PS-11c).
  2. The cube tick is not covariant under unit translations or under rotations about a site (Theorem A2). PS-1 and Admissibility, read plainly, need a cell reading (PS-1c).
  3. With one fermion mode per site the PS-6 frame group of the tick is `U(1)`, not `U(2)` (Lemma B3, Theorem B5). The skeleton's section 6 line "With one qubit per site and PS-6, the frame group of `M_2(C)` is `U(2)`" holds in the qubit reading, not in the fermion reading the cube tick uses.
  4. In the free tick, under the copy rule, no record ever forms in the PS-7 vacuum (Theorem B8). This is the TM1-i tension in exact form.
- **First outstanding statement: Lemma LW1-U** (Section 5.6). At infinite volume, the PS-3 transport set (fewest changes per site, then greatest entropy per site) has exactly one element. Three attacks are written out with the exact reason each fails.
- **Proposed specifications:** PS-1c (cell reading of covariance), PS-3h (transport per half-tick), PS-3c (law-level copy), PS-6r (register algebra and gauge layers), PS-7r (which sea), PS-11c (countable statements). Section 6 collects their text.

---

## 1. Sources and what each one states

Each line quotes the text before saying what it shows.

### 1.1 Axioms (`origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md`)

- Lattice: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." And: "No site is privileged. Sites are distinguished by the supplied lattice structure alone."
- Qubit: "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`."
- Admissibility: "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions." Reading note (2), marked "interpretive, non-governing": "Read with Record, the distribution concerns which possibility a forming record locks, conditional on formation at that site; it does not supply the formation site, probability, or rate." Reading note (1): "deterministic substrates as boundary realizations -- the law supplies the odds; the realized state supplies the pick."
- Record: "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."
- Qualification: "A state is a configuration of records." "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
- "Admissibility is not a dynamics axiom. ... It does not choose a Hamiltonian or transfer operator, ... define a time metric, or provide a record-production process".

### 1.2 Working set (PR #10140 diff, `docs/CANDIDATE_LAWS.md`)

- PS-1: "There is one fixed update. It acts on the joint possibilities of all sites as a unitary map built from finitely many layers of nearest-neighbour gates, covariant under lattice translations and proper cubic rotations. A history is a sequence of updates; the update count orders it." "The choice of law, the cube tick or D4 events, is open and is settled in part LW1."
- PS-2: "The probability of a possibility does not depend on which other possibilities are offered with it."
- PS-3: "One actual configuration exists at every tick. It moves by the support-respecting transport that changes the fewest modes, and among those has maximal entropy. Records never condition the odds. A record forms at a site when the site's actual value has been copied into at least two neighbouring sites."
- PS-4: "A history has a first tick, at which no site carries a record."
- PS-6: "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."
- PS-7: "The vacuum is the half-filled state of the update's fermion modes."
- PS-11: "A statement that the law gives probability one holds in the realized history."
- PS-5 (not in the set): "the five-mode site content, is a fallback only, used if building on cells of qubits fails at a named step."

### 1.3 Primitives (quoted in the skeleton section 1.2 from `axiom_premise_nodes.json`)

- `kinetic_isotropy_primitive`: `c_t=c_s`, "the emergent tick is grained on the same footing as the spatial edge"; it "does not re-axiomatize emergent time".
- `realized_state_primitive`: one law-admissible realized state, evaluated "POINTWISE only"; "a quoted number must be invariant over the law-admissible family, else it is registered data".

### 1.4 The cube tick

- #9872 (closed; `gh pr diff 9872`), claim scope: "In a supplied Margolus tick with one fermion mode per site and rotations acting on site modes as spin-3/2 coherent states along the body diagonals, the edge hop with overlap phases is unitary, exactly covariant under the 24 proper cubic rotations about every block centre, and has bands cos w = cos^2(mu/2)(cos Kx + cos Ky + cos Kz)/3 - sin^2(mu/2); no classification of all ticks, derivation from the axioms or physical identification is established." Its text: "The massless node has zero net Berry flux (-6.7e-16), so it is not net-chiral."
- #10016 (closed), claim scope: "For CL-1's cell (one fermion mode per site, face phase -1, the Margolus cube tick on both tilings, Bloch over 2Z^3) with the 24 cube-centred rotations realised up to a +-1 site gauge: the cell rep is spinorial, spin (from the velocity matrices) times taste ...; the four tastes are E + E of O (one E per chirality), never 1 + 3; every rotation-invariant mass gaps all four alike; ... the copy mass leaves one light Dirac family. ... Three families are not derived."
- The full CL-1 text, from the historical register at `4603a51acd` (not main; main's register now has three historical clauses only). Its first sentences: "Sites are the points of Z^3, tiled in two ways by 2x2x2 cubes offset by (1,1,1); each site's qubit is one fermion mode, and modes at different sites anticommute. The odds, one amplitude per joint occupation of the modes, change only by half-ticks that alternate between the tilings." And: "Let W_i pass each site's odds to its edge neighbour along axis i with a phase, the phases multiplying to -1 around every unit face." And: "A species of mass m applies exp(-i(eps - mu/2)R) on every even cube and exp(+i(eps + mu/2)R) on every odd cube". The register's own claim scope lists its departures: "CL-1's split (Lattice ...); CL-1's copy mass (Admissibility's rotation clause); CL-1's role layout of coarser-block sites as matter, rishon and edge-register sites ... (Lattice: "no site is privileged" ...)". Its band line: "Flat-edge bands: cos w = A S - (cos 2b - cos mu)/2, b = pi/2 - eps, A = (cos 2b + cos mu)/2, S the cubic structure factor". Its copy-mass line: "with it exactly one light copy, untuned, keeping the 12 tetrahedral rotations ... This narrows Admissibility's rotation clause." Its spin line: "With one mode per site, a hopping block unitary covariant under the 24 rotations exists exactly when the site's rotation character is of spin-3/2 type".
- Gauge theme (#10126 synthesis at `7086189d10`): "Block covariance and register size select no gauge group (#9882)". "Gauss laws are not derived from the tick (logged #10024: the free tick has no local constants of motion away from a decoupled point)." #9882's scope: "the spin-3/2 twist of the coin leaves M_2(C) (a copy U(2)) which the coin breaks to U(1) x U(1)". #9926 (in the synthesis): exact U(1) and "with three colour rishons per end, an exact SU(3) Gauss law, on a supplied role assignment".
- Chirality theme (#10131 synthesis at `a1bced899b`): "net cone chirality at 0 and at pi equals minus W3, and products of coins and shifts have W3 = 0 (#9863)". "**Answer: not obtained.**"
- Records theme (#10124 synthesis at `d501c51fd4`): "One actual configuration moved by a transport that uses only nonzero elements of each half-tick, changes the fewest modes and, among those, has maximal entropy, with records that never condition the odds, keeps the Born law at every half-tick in the supplied models." Its dependencies line: "An independent rederivation is in #9902, section 4 (gravity theme): the supply-demand bound for any unitary in any basis (20,000 sets, max excess 2e-15) ... uniqueness of the greatest-entropy plan by strict concavity". And: "#9902 qualifies the label statement: "'Label-free' means equivariant under relabelling configurations; the plan still depends on the mode basis, the half-tick and the global configuration."" On selection: "the selector works for a three-site redundant record ... and fails for a bare two-site copy (#10054)". On failure: "Proportional shortfall switching does not keep Born on one Margolus block (#9893)".
- #10091 (closed), claim scope opening: "With the rule-fixed dimension-six dispersion (c_q = -S/6 + 1/24, E* = 1.217e18 GeV) and nucleons taken UNIVERSAL ...". Its verdict: "EXCLUDED unless the rules also alter air-shower development (uncomputed)."
- #10093 (closed), verdict: "TENSION, not EXCLUDED; the decisive unknown is the air cross section of the flowed hadron, which the rules have not yet computed".

### 1.5 The D4 event law

- #10094 (closed; also carried on #10130), claim scope opening: "Supplied free models on the D4 event lattice with one factor per nearest pair, the same for all 24 root directions. (T) Aut(D4) = W(F4) (1152 built by closure)." And: "Site-reflection positivity holds for time along an axis and along a root". And: "Root slicing (events = the centre sites of the active cubes, c x half-tick = a): ... v - 1 = (-1.67e-2, -1.98e-2)(ka)^4, subluminal." Its proposed text: "Events are the centre sites of the active tiling's cubes, one half-tick apart with c x half-tick = a; they form the D4 lattice. A history's odds are a product of one local factor per pair of nearest events, the same for all 24 nearest directions; matter is weighted by the overlap of the 24-direction Wilson kernel and links by their triangle loops. Records grow along a root of D4 (the direction in which a site's cube recurs), and the real-time step is the Osterwalder-Schrader transfer over two half-ticks." Its list "What must be rebuilt", item 1: "CL-1's cube tick becomes a D4 history weight, with real time from the OS transfer over two half-ticks." Item 5: "Records. The arrow breaks W(F4) in the STATE."
- #10096 (closed), setup: "Each slice is a cubic lattice of spacing sqrt2. Alternate slices are body-centre shifted, so they are CL-1's two tilings." Route C: "In real time, the only symmetry that survives is the stabiliser of r_t in W(F4): 48 elements, the slice's cube group." Verdict: "So the D4 law does NOT survive for fermions as written. Its dim-6 protection is a theorem for the Euclidean weight, and that weight's fermion sector has no positive slice Hilbert space".
- D4 theme (#10130 synthesis at `899b749fed`): "A unitary walk on the same events keeps only the 48-element stabiliser and has a dimension-six term (#10096, table only)." "With one mode per event, nearest-neighbour root hops and the stated cells, no spin-1/2 arises (#10104). The zoom runners use four supplied spinor components per event, a supply that departs from one qubit per site."

### 1.6 The covariant law pair on main

`ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13`, claim scope: "Two separately declared nearest-neighbor conditional probability laws on the one-site M_2(C) possibility domain satisfy the current Admissibility contract. Both use the parity of the number of +I values in the six-site neighbor shell ... and are covariant under translations and proper cubic rotations." It ends: "These are exact finite-support law models, not a selection of the physical law". So the four axioms alone do not fix the law. LW1 needs the working set and a choice.

### 1.7 The skeleton line this draft corrects

Skeleton section 6: "With one qubit per site and PS-6, the frame group of `M_2(C)` is `U(2)`, with non-abelian part `SU(2)` (consistent with #9882's "abelian or copy U(2)" commutant). So the framework's simplest gauge sector is a pure SU(2) lattice gauge theory on `Z^3` with the update as time evolution." Theorems B3 and B5 below show that this holds only in the qubit reading of the site, not in the fermion reading the cube tick uses.

---

## 2. Conventions

**C1. Sites, modes, algebra (fermion reading).** Each site `x` in `Z^3` carries one fermion mode `c_x`. Modes at different sites anticommute. The one-site algebra generated by `c_x` is `M_2(C)` (basis `1, c_x, c_x^dag, n_x`). This is the Qubit axiom's one-site presentation. The global algebra is the CAR algebra `A(Z^3)`, the graded tensor product of the site algebras. The Qubit axiom says nothing about how site algebras combine, so the graded product is a reading, not an addition. The bosonized alternative (site qubits that commute, fermions as string ends) is on file (register "bosonized-sites", `4603a51acd`) and needs link qubits and "a vertex ordering with no rotation-invariant choice"; this draft does not use it.

**C2. Parity superselection.** Physical local operators and local unitaries are even. The even part of one site's `M_2(C)` is `span{1, n_x}`. So the only commuting local basis that respects parity is the occupation basis. This fixes PS-3's "configuration": a configuration is an occupation pattern `c : Lambda -> {0,1}`. PS-3 needs a basis (#9902: "the plan still depends on the mode basis"). The fermion reading supplies it without a choice.

**C3. Born measure.** Under PS-2 the one-site odds have the trace form (skeleton PS-2: "The trace form `p(P) = tr(rho P)`"). For a state `omega` of `A(Z^3)` the Born measure on configurations is `mu_omega(c_F = s) = omega( prod_{x in F} n_x^{s_x} (1-n_x)^{1-s_x} )` for finite `F`. The `n_x` commute, so these numbers are a consistent family. By Kolmogorov extension they define one probability measure on `{0,1}^{Z^3}`.

**C4. Ticks.** A tick is one application of the update `U`. A half-tick is one of its two layers of cube gates (Section 3.1). Ticks are indexed `n = 0, 1, 2, ...`; half-ticks `h = 0, 1, 2, ...` with `h = 2n` at tick `n`.

**C5. Words.** "Exact" means proved in full in this draft. "[check]" means the scratch computation, which guides only.

---

## 3. Part (a): the two candidates stated precisely

### 3.1 Candidate A: the cube tick

**Definition A1 (the cube tick, minimal form).**

1. *Tilings.* The even tiling is the set of cubes `C_e(b) = b + {0,1}^3`, `b in 2Z^3`. The odd tiling is `C_o(b) = b + (1,1,1) + {0,1}^3`, `b in 2Z^3`. Each tiling partitions `Z^3`.
2. *Edge ownership.* The edge from `x` to `x + e_i` lies in exactly one cube of exactly one tiling: in the even tiling if `x_i` is even, in the odd tiling if `x_i` is odd. Proof: an edge along `i` lies in a cube with offset `o` iff `x_i = o_i mod 2` (both ends then lie in the cube's `i`-range) and `x_j` lies in `{o_j, o_j + 1} mod 2` for `j != i`, which always holds. Exactly one of `o = (0,0,0)`, `o = (1,1,1)` matches `x_i mod 2`. Within that tiling the cube is fixed by `b_j = x_j - ((x_j - o_j) mod 2)`. ∎
3. *Hop phases.* On the edge `x -> x + e_i` put the Kawamoto-Smit sign `eta_i(x) = (-1)^{x_1 + ... + x_{i-1}}`. Around every unit plaquette of `Z^3` the product of the four signs is `-1` (flux `pi`). Proof for the plane `(1,2)` at base `x`: `eta_1(x) eta_2(x+e_1) eta_1(x+e_2) eta_2(x) = 1 . (-1)^{x_1+1} . 1 . (-1)^{x_1} = -1`; the planes `(1,3)` and `(2,3)` are the same computation. ∎ This is CL-1's "the phases multiplying to -1 around every unit face", read on every unit face of `Z^3`. (Half of the plaquettes of `Z^3` lie in no single cube, because their two edge directions have opposite parity. Their flux is still physical data of the tick, since a particle can circle them by alternating half-ticks. Reading "every unit face" as every face of `Z^3` fixes it.)
4. *One-body hop.* For a tiling `T`, `R_T = (1/sqrt3) sum_{edges in T} eta_i(x) (|x+e_i><x| + |x><x+e_i|)` on `l^2(Z^3)`. Restricted to one cube, the three axis parts `R_i` satisfy `R_i^2 = 1/3` (each corner has exactly one partner along `i` in the cube) and `R_i R_j + R_j R_i = 0` for `i != j` (flux `pi` on each face). Hence `R_T^2 = 1`. [check: `|R^2 - 1| = 2.2e-16` on the 6^3 torus for both tilings.]
5. *Gates and layers.* With step angle `eps` and mass angle `mu`, the even half-tick is the one-body unitary `V_e = exp(-i(eps - mu/2) R_e) = cos(eps - mu/2) - i sin(eps - mu/2) R_e`, and the odd half-tick is `V_o = exp(+i(eps + mu/2) R_o)`. The one-body tick is `V = V_o V_e`. The many-body update is the Fock lift `U = Gamma(V) = Gamma(V_o) Gamma(V_e)`, where `Gamma(W)` is the unique number-conserving even unitary with `Gamma(W) c^dag(f) Gamma(W)^* = c^dag(W f)`. Each `Gamma(V_e)` is a product of commuting cube gates `G_C = Gamma(exp(-i(eps - mu/2) R_C))`, one per even cube.
6. *Constants.* `0 <= mu < 2 eps < pi` (Theorem B10 shows why this window makes the vacuum canonical).

What is set aside from CL-1, and why:
- The copy mass `exp(i (M N/4)(1 - s) R)`: CL-1 itself says it "narrows Admissibility's rotation clause" (12 of 24 rotations). PS-1 asks for covariance under the proper cubic rotations. So it is not in the PS-1 law. Its job (one light copy) moves to MT1/FL1.
- The split, the edge registers and the lapse: CL-1's scope says the split departs from Lattice. They belong to PS-9 (gravity response), which is not in the working set.
- The role layout (rishon and edge-register sites): CL-1's scope says it departs from "no site is privileged". PS-6 puts registers on links instead (Section 5.3).
- The species-dependent dressed cone: one species here.

What remains is the tick of #9872 up to a site gauge (the register's face-clause note: "the former spin-3/2 overlap field is this field up to a site gauge"), with CL-1's step and mass angles.

**Lemma A1a (layers of nearest-neighbour gates).** `U` is a finite product of layers of two-site nearest-neighbour gates, each layer covariant under `2Z^3`.

*Proof.* Fix one cube and its one-body gate `u = exp(-i theta R_C)` in `U(8)`. The cube's corners admit a Hamiltonian path along cube edges (a Gray code: 000, 001, 011, 010, 110, 111, 101, 100; consecutive words differ in one bit). Any `u` in `U(8)` is a product of a diagonal unitary and Givens rotations acting on consecutive indices of any fixed ordering (QR factorisation by Givens rotations; credited: Reck et al. 1994, Clements et al. 2016; standard linear algebra). With the Gray-code ordering each Givens rotation acts on two corners joined by a cube edge, so on two nearest neighbours. The Fock lift is a group homomorphism, `Gamma(u_1 u_2) = Gamma(u_1) Gamma(u_2)` exactly, and the lift of a Givens rotation on modes `x, y` is `exp(theta (e^{i phi} c_x^dag c_y - h.c.))`, an even two-site gate. The lift of the diagonal part is a product of one-site phases. Apply the same decomposition, with the same relative edges, in every cube of the tiling at once. Gates in different cubes act on disjoint sites and are even, so they commute, and each layer is invariant under `2Z^3`. The two half-ticks give a finite number of layers in all. ∎

**Theorem A2 (exact covariance group of the cube tick).** Let `c_0 = (1/2,1/2,1/2)`. Let `O` be the 24 proper rotations of the cube.

(i) For every `t` in `2Z^3`, translation by `t` commutes with `V` exactly.
(ii) For every `R` in `O`, the rotation `x -> R(x - c_0) + c_0` maps `Z^3` to itself, maps each tiling to itself, and there is a sign function `d_R : Z^3 -> {+1,-1}` such that the one-body unitary `Omega_R = D_R P_R` (permutation `P_R`, diagonal signs `D_R`) commutes with `V_e`, `V_o` and `V`. The same holds about every odd-cube centre.
(iii) Assume `sin(eps - mu/2) sin(eps + mu/2) != 0` (otherwise a half-tick is trivial). A translation by `t` with some odd coordinate does not commute with `V`, even up to any diagonal unitary gauge. A rotation about a site is a symmetry (up to gauge) iff it fixes that site's even-cube centre, i.e. iff it is one of the three rotations about the body diagonal through the site and that centre.
(iv) Translation by `(1,1,1)` maps the even tiling to the odd one. It is a symmetry of `V` only when composed with a half-tick shift, and then only at `mu = 0` (composed also with the sublattice sign).

*Proof.* (i) A translation by `t` in `2Z^3` maps each tiling to itself. It preserves the signs: `eta_i(x + t) = eta_i(x) (-1)^{t_1 + ... + t_{i-1}} = eta_i(x)` since each `t_j` is even. So it commutes with `R_e`, `R_o` and hence with `V`.

(ii) `R(x - c_0) + c_0 = R x + (c_0 - R c_0)`. `R` permutes coordinates with signs, so `c_0 - R c_0` has entries in `{0, +1, -1}`; the map sends `Z^3` to `Z^3`. A cube `b + {0,1}^3` of the even tiling has centre `b + c_0`; its image has centre `R b + c_0`, and `R b` is in `2Z^3`. So the even tiling maps to itself. An odd centre `c_0 + (1,1,1) + b` maps to `c_0 + R(1,1,1) + R b`, and `R(1,1,1) - (1,1,1)` has entries in `{0, -2}`, so the image is an odd centre. All hop weights are `1/sqrt3`, so `P_R R_T P_R^{-1}` is a hop on the same edges with signs `eta'` = the pulled-back signs. The flux of `eta'` through any plaquette equals the flux of `eta` through the preimage plaquette, which is `pi`. Two `Z_2`-valued edge functions on `Z^3` with the same flux through every plaquette differ by a coboundary, because every closed edge loop in `Z^3` bounds a sum of plaquettes (the first cohomology of the cubical complex of `Z^3` with `Z_2` coefficients is zero, since `Z^3` is contractible). So `eta' = eta . (d_R(x) d_R(y))` for some `d_R`. Then `D_R P_R` maps `R_T` to `R_T` for both tilings, and `cos, sin` of the same angles give `V_e`, `V_o`, `V`. The odd centres: rotation about an odd centre equals rotation about `c_0` composed with a translation in `2Z^3`, by the computation above.

(iii) A diagonal unitary changes only the phases of matrix entries, so it suffices to find `x, y` with `|<y + t|V|x + t>| != |<y|V|x>|`. Write `alpha = eps - mu/2`, `beta = eps + mu/2`. Let `t_i` be odd and compare the entries for the step `+2e_i`. From the site `0`: `V = V_o V_e` applies `V_e` first. The only two-hop path from `0` to `2e_i` is straight along `i`. Its first edge `0 -> e_i` is even (its `i`-coordinate is even) and its second edge `e_i -> 2e_i` is odd, so `<2e_i|V|0> = <2e_i|V_o|e_i><e_i|V_e|0>`, of modulus `|sin alpha sin beta|/3 != 0`. From the site `t`: the first edge `t -> t + e_i` has odd `i`-coordinate, so it is an odd edge and `V_e` cannot use it; hence `<t + 2e_i|V|t> = 0`. So translation by `t` is not a symmetry. For a rotation `R` about the site `0`: `R x = R(x - c_0) + c_0 + t_R` with `t_R = R c_0 - c_0`, whose entries are in `{0, +1, -1}`. The first part is a symmetry by (ii). So `R` is a symmetry iff translation by `t_R` is, iff `t_R` has no odd entry, iff `t_R = 0`, iff `R c_0 = c_0`. The proper rotations fixing `c_0` (and `0`) are those about the body diagonal through `0` and `c_0`: the identity and two turns. [check: on the 6^3 torus at `(eps, mu) = (0.3, 0.1)`, `max | |V| - |T V T^-1| | = 0.058` for `t = e_1` and for `t = (1,1,1)`, and `0` for `t = 2e_1`; 3 of 24 site rotations and 24 of 24 cube-centre rotations are symmetries up to a sign gauge.]

(iv) Translation by `(1,1,1)` swaps the tilings and so maps `V_e = exp(-i(eps - mu/2) R_e)` to `exp(-i(eps - mu/2) R_o)` up to gauge. `V_o` is `exp(+i(eps + mu/2) R_o)`. The sublattice sign `D_s = (-1)^{x_1 + x_2 + x_3}` anticommutes with every nearest-neighbour hop, so `D_s R D_s = -R`. Composed with `D_s`, the image is `exp(+i(eps - mu/2) R_o)`. This equals `V_o` iff `mu = 0`. ∎

So the exact covariance group of the cube tick is `G_U = 2Z^3 ⋊ O_{c_0}` (translations of the cell lattice, rotations about cell centres), with the glide of (iv) added at `mu = 0`.

**Corollary A2a (no site is privileged).** `G_U` acts transitively on `Z^3`. Proof: the 24 rotations about `c_0` move the corner `0` to all eight corners of `{0,1}^3` (the cube's rotation group is transitive on its vertices), and `2Z^3` moves those eight to all of `Z^3`. ∎ The stabiliser of a site in `G_U` is `C_3`, not `O`.

**Theorem A3 (the cube tick's events form a D4 lattice, time along a root).** An *event* is a pair (active cube, half-tick). Write it as `(X, h)` with `X = (cube centre) - c_0`. Take the half-tick `Delta` with `c Delta = a` (the reading of `kinetic_isotropy_primitive` used here: the tick is grained on the same footing as the edge). Then the event set is `E = {(X, h) in Z^4 : X_1 = X_2 = X_3 = h mod 2} = 2 D4*`, where `D4* = Z^4 ∪ (Z^4 + (1/2)(1,1,1,1))`. Its 24 shortest vectors are `(+-1, +-1, +-1, +-1)` and `+-2 e_mu`, so it is a scaled copy of the root lattice D4, and the time direction `e_4` is a shortest vector (a root).

*Proof.* Even cubes are active at even `h` with centres `c_0 + 2Z^3`; odd cubes at odd `h` with centres `c_0 + (1,1,1) + 2Z^3`. So `X` is in `2Z^3` for even `h` and in `(1,1,1) + 2Z^3` for odd `h`: all four coordinates have one parity. The set of integer 4-vectors with all coordinates of one parity is `2Z^4 ∪ (2Z^4 + (1,1,1,1)) = 2 D4*`. Its nonzero vectors of least squared length are `(+-1)^4` (length^2 4, sixteen of them) and `+-2 e_mu` (length^2 4, eight). Every other nonzero vector has length^2 at least 8. A lattice in 4 dimensions with 24 shortest vectors forming the 24-cell vertex set is similar to D4 (the vertex set of the 24-cell is the D4 root system up to rotation and scale: `D4*` is `D4` rotated and scaled by `1/sqrt2`, a standard fact; #10094 also states "D4* is D4 rotated" and that the landed carrier `Z^4 u (Z^4 + u/2)` "is D4*, which is similar to our D4"). `e_4` is proportional to the shortest vector `2 e_4`. ∎

Remarks. The 16 vectors `(+-1)^4` join an even cube to the 8 odd cubes that share one of its corners: these are the gate links of the tick. The 6 vectors `+-2 e_i` join cubes of one tiling sharing a face. The 2 vectors `+-2 e_4` join a cube to itself two half-ticks later. This matches #10096's "Each slice is a cubic lattice of spacing sqrt2. Alternate slices are body-centre shifted, so they are CL-1's two tilings."

### 3.2 Candidate B: the D4 event law

**Definition B1 (the D4 event law, as written in #10094).** Events: the set `E` of Theorem A3 (#10094: "Events are the centre sites of the active tiling's cubes, one half-tick apart with c x half-tick = a"). Weight: "A history's odds are a product of one local factor per pair of nearest events, the same for all 24 nearest directions". Matter: "weighted by the overlap of the 24-direction Wilson kernel". Links: "by their triangle loops". Time: "Records grow along a root of D4". Real time: "the real-time step is the Osterwalder-Schrader transfer over two half-ticks".

- *Gates and layers.* None. The law is a Euclidean weight on histories. Real time is derived from it by OS reconstruction.
- *Site content.* Per #10130: "The zoom runners use four supplied spinor components per event". With one mode per event (#10104): "no spin-1/2 arises".
- *Covariance.* The weight is invariant under `Aut(D4) = W(F4)`, order 1152 (#10094 "(T)"). Any real-time step along a root keeps only the root stabiliser, 48 elements (#10096 route C).

---

## 4. The chosen law, stated (result of parts (b)-(d))

For reference before the proofs. Section 5 proves each clause consistent; Section 7 gives the reasons for the choice.

**Law `L_cube`.**

1. *Sites and modes.* One fermion mode per site of `Z^3` (C1).
2. *Links.* Under PS-6 and PS-6r: each nearest-neighbour edge `l` of `Z^3` carries a register: a spin-`S` quantum link (`E_l = S^z_l`, `U_l = S^+_l`, `S` a supplied constant, `S >= 1/2`). Link registers carry odds but no actual configuration and no records. (A `U(1)` rotor is the alternative; Section 5.3 says what each choice costs.)
3. *Update.* One tick is `U = E . G_o . G_e`, where `G_e` (`G_o`) is the product over even (odd) cubes of the dressed cube gates `exp(-i theta_T R_C^U)`, with `R_C^U = (1/sqrt3) sum_{edges of C} eta_i(x) (c_{x+e_i}^dag U_l c_x + h.c.)`, `theta_e = eps - mu/2`, `theta_o = -(eps + mu/2)`; `E = prod_l exp(-i tau_E E_l^2)`. There is no separate plaquette layer: with quantum links the plaquette terms on neighbouring plaquettes do not commute, and no ordering of them is rotation covariant (Section 5.3). Plaquette dynamics then arises from the matter hops (each hop moves `E_l`), which is GA1's to compute.
4. *Vacuum (PS-7, PS-7r).* The quasi-free state `omega_P` filling the negative quasi-energy modes of the one-body tick `V` of Definition A1 (Theorem B10). For the gauged law, PS-7 names the zero-coupling sea; the interacting vacuum is VC1's (Theorem E2b gives existence of stationary, gauge-invariant, half-filled states).
5. *Actuality (PS-3, PS-3h).* One actual configuration of site occupations at every half-tick, moved at each half-tick by the support-respecting, fewest-change, greatest-entropy transport (Theorem B7).
6. *Formation (PS-3c).* At the end of each tick `n >= 1`, a record forms at every unrecorded site `x` for which there are two distinct neighbours `y, z` of `x` with `omega_n( (n_x - n_y)^2 + (n_x - n_z)^2 ) = 0`. The record locks the actual occupation of `x` at tick `n`.
7. *Initial condition (PS-4).* The domain of the law is a supplied initial state `omega_0`; no site carries a record at tick 0.
8. *Reading (PS-11c).* Statements of law-probability one hold in the realized history, for a fixed countable list of statements.

Free constants: `eps`, `mu` (window `0 <= mu < 2 eps < pi`), `S`, `tau_E`; and the supplied `omega_0`.

---

## 5. Part (b): which candidates satisfy the axioms and the working set

### 5.1 Lattice, PS-1 and the cell reading

**Theorem B1 (the cube tick against Lattice, Admissibility covariance and PS-1).**
(i) Nearest-neighbour: yes. The generators are sums of nearest-neighbour bilinears, and Lemma A1a writes the free `U` as finitely many layers of two-site nearest-neighbour gates (for the gauged tick, see Section 5.3, which uses one credited step).
(ii) Unitary: yes. Each gate is the exponential of a Hermitian even operator.
(iii) "No site is privileged": yes (Corollary A2a).
(iv) Covariance under "lattice translations and proper cubic rotations", read as all of `Z^3` and the 24 rotations about each site: no (Theorem A2 (iii)).
(v) Covariance under translations of the cell lattice `2Z^3` and the 24 rotations about each cell centre: yes (Theorem A2 (i)-(ii)).

*Proof.* Items (i)-(v) are restatements of Lemma A1a, Definition A1 (5), Corollary A2a and Theorem A2. ∎

Is the failure in (iv) special to the Margolus layout? The next theorem says that for a free one-mode tick it is forced.

**Theorem B2 (no free one-mode tick is covariant under all of `Z^3` and the site rotations).** Let `W` be a unitary on `l^2(Z^d)` of finite range (there is `r` with `<y|W|x> = 0` when `|x - y| > r`). Suppose `W` commutes with every translation of `Z^d`. Then `W = e^{i phi} T_a` for some phase and some `a` in `Z^d` (a pure shift). If in addition `W` commutes, up to a diagonal unitary, with a group of rotations about a site whose only fixed vector is `0`, then `W = e^{i phi}`.

*Proof.* Translation covariance gives `<y|W|x> = w_{y-x}` with finitely many nonzero `w_a`. In Fourier variables `W` is multiplication by `w(z) = sum_a w_a z^a`, a Laurent polynomial in `z = (z_1, ..., z_d)` with `z_j = e^{i k_j}`. Unitarity gives `|w(z)| = 1` on the torus `|z_j| = 1`. Let `w^*(z) = sum_a conj(w_a) z^{-a}`. On the torus `w^*(z) = conj(w(z))`, so `w(z) w^*(z) = 1` on the torus. Both sides are Laurent polynomials; two Laurent polynomials equal on the torus have the same Fourier coefficients, so `w w^* = 1` in the ring `C[z^{+-1}]`. In this ring the units are exactly the monomials `c z^a`, `c != 0`. Proof: order the exponents lexicographically (a total order compatible with addition). For nonzero `f, g`, the leading (largest) exponent of `f g` is `lead(f) + lead(g)` and the trailing (smallest) exponent is `trail(f) + trail(g)`, because the extreme products cannot cancel. The exponents of `w^*` are the negatives of those of `w`, so `lead(w^*) = -trail(w)`. From `w w^* = 1`: `0 = lead(w w^*) = lead(w) - trail(w)`. So `lead(w) = trail(w)`, and `w` has one term. So `w = c z^a`, `|c| = 1`: `W = c T_a`. A rotation `R` about the site `0` acts by `(P_R psi)(x) = psi(R^{-1} x)`, and `P_R T_a P_R^{-1} = T_{R a}`. A diagonal unitary `D` gives `D T_{Ra} D^{-1} = (diagonal) T_{Ra}`. Equality with `c T_a` needs `R a = a` for every `R` in the group, so `a = 0`. ∎

For the cube tick the one-body tick `V` is number-conserving and of finite range on one mode per site, so Theorem B2 applies to it. It also applies to any number-conserving quasi-free update with one mode per site. Hence: **under the plain all-translations reading, PS-1 with one fermion mode per site admits no free hopping update.** Fully covariant updates do exist under the plain reading, for example interacting ones built from layers of commuting covariant gates (a layer of on-site even gates and a layer of `exp(i g n_x n_y)` on all edges). Such layers move no particle. This draft does not claim that every fully covariant fermionic update is static; that question is not needed for the choice.

Theorem B2 is a classical result for scalar quantum walks (Meyer 1996, quant-ph/9604003, cited on main in `TWELVE_HOUR_TOE_FRAMEWORK_CAMPAIGN_DIAGNOSIS_2026-07-16.md`). It is rebuilt above in full.

**Proposed specification PS-1c (cell reading of covariance).**
> "In PS-1 and in Admissibility, covariance under lattice translations and proper cubic rotations is read on cells: the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites."

*Reasons.* (1) Theorem B2: with one mode per site, a free hopping update covariant in the plain sense is a global phase. (2) Theorem A2: the cube tick meets the cell reading exactly. (3) PS-5 already says "build site content on cells of qubits". (4) The transitivity clause keeps "No site is privileged" in force (Corollary A2a). (5) The Admissibility rule itself (Theorem B9) stays covariant under the full site group; only the update needs the cell reading.

*What it costs.* The stabiliser of a site drops from `O` to `C_3`. The emergent theory must restore full rotation symmetry at long distance; #9872 reports the tick's light band isotropic at the cone (speed `1/sqrt3` block per tick), and Theorem C1 gives the first anisotropic term.

*Alternative for the owner.* Keep the plain reading. Then the cube tick is excluded, the D4 law is excluded as well (Theorem B12), and LW1 needs a fully covariant interacting update, which has no candidate on file.

### 5.2 Qubit

**Theorem B1q.** The cube tick uses one fermion mode per site. The one-site algebra is `M_2(C)` (C1). No cell is needed for the site content; cells are needed for covariance only (PS-1c). ∎ (Restatement.)

The D4 law needs four spinor components per event (#10130 quote in 1.5). Read on cells, an event is an active cube whose eight corner modes could host them; no source builds that map, and the W(F4) results were computed with supplied components. So the D4 law, as run, departs from one qubit per site.

### 5.3 PS-6: local frames and link registers

**Lemma B3 (the frame group of one fermion-mode site).** Let `beta` be an automorphism of the CAR algebra that fixes `c_y` for every `y != x` and maps the one-site algebra `A_x` onto itself. Then `beta(c_x) = u c_x` or `beta(c_x) = v c_x^dag` with `|u| = |v| = 1`. These form the group `U(1) ⋊ Z_2 = O(2)`. The subgroup that commutes with the number operator `sum n` is `U(1)`.

*Proof.* `d = beta(c_x)` lies in `A_x = span{1, c_x, c_x^dag, n_x}`. For `y != x`, `c_x` anticommutes with `c_y` and `c_y^dag`, and `beta` preserves this, so `d` anticommutes with them. The even elements `1, n_x` commute with `c_y`; so `d` is in the odd part, `d = u c_x + v c_x^dag`. The CAR give `d^2 = 0` and `d d^dag + d^dag d = 1`. `d^2 = u v (c_x c_x^dag + c_x^dag c_x) = u v`, so `u v = 0`. `d d^dag + d^dag d = |u|^2 + |v|^2 = 1`. So one of `u, v` is zero and the other has modulus 1. ∎

So, in the fermion reading, "the internal frame of each site's possibilities" is `O(2)`, and its number-conserving part is `U(1)`. The `U(2)` of the skeleton's section 6 is the frame group of `M_2(C)` acting on a site qubit whose algebra commutes with its neighbours' (the qubit reading). In that reading every site carries a fundamental `SU(2)` charge at all times (the site space `C^2` is the fundamental), and the hop of a fermion is not defined.

**Theorem B4 (exact `U(1)` Gauss laws for the gauged cube tick).** Orient each edge `l = (x -> x + e_i)`. Let `G_x = n_x + sum_{l out of x} E_l - sum_{l into x} E_l`, with `[E_l, U_l] = U_l` (quantum link or rotor). Then every factor of `U = E . G_o . G_e` (and of a rotor plaquette layer, if one is used) commutes with `exp(i theta G_x)` for every `x` and `theta`. So `U` commutes with all local gauge transformations, and each `G_x` is conserved.

*Proof.* Take a hop term `c_y^dag U_l c_x` with `l = (x -> y)`. Conjugation by `exp(i theta n_x)` sends `c_x` to `e^{-i theta} c_x`. Conjugation by `exp(i theta E_l)` sends `U_l` to `e^{i theta} U_l` (from `[E_l, U_l] = U_l`). `l` is out of `x`, so `exp(i theta G_x)` contains `exp(+i theta E_l)`, and the term is invariant. At `y`: `c_y^dag` gains `e^{+i theta}`; `l` is into `y`, so `exp(i theta G_y)` contains `exp(-i theta E_l)`, which sends `U_l` to `e^{-i theta} U_l`; invariant. The hermitian conjugate is the same computation. Terms that do not touch `x` or its links commute with `G_x`. So each `R_C^U` commutes with each `G_x`, and so does its exponential. `E_l^2` commutes with `E_l` and with matter at `x`. For a rotor plaquette layer: `U_p` around a plaquette contains, at each corner, one link out and one link in (orientation along the loop), or two links of opposite orientation relative to the corner, so `exp(i theta G_x)` multiplies it by `e^{i theta} e^{-i theta} = 1`. ∎

Each edge lies in exactly one cube (Definition A1 (2)), so the dressed gates of one half-tick act on disjoint sets of sites and links, and they commute. The `E` layer consists of commuting one-link gates and is covariant under the full lattice group.

*Nearest-neighbour form of the dressed gates.* Lemma A1a used the Givens decomposition, which needs a one-body (Gaussian) gate. A dressed gate is not Gaussian, because its hops carry link operators. For quantum links the cube system (8 modes, 12 links of dimension `2S+1`) is finite-dimensional. The even operators supported on one edge triple (two neighbouring modes and the link between them), over the 12 edges of the cube, generate as a Lie algebra all even operators of the cube system. For qubits this is the standard universality of two-local gates on a connected graph, and for fermion modes it is the universality of even two-mode gates (Bravyi and Kitaev 2002); both are credited. Its extension to edge triples that include a link register is not written out here and is a step for the distiller. Given it, every element of the connected compact group of even unitaries is a finite product of edge-triple gates, so each dressed cube gate is a finite product of nearest-neighbour gates; repeating the same factorisation in every cube gives layers covariant under `2Z^3`, whose product is the half-tick exactly.

*Rotor versus quantum link.* With rotors the `U_l` commute, so a plaquette layer `prod_p exp(-i tau_B (U_p + U_p^dag))` is a product of commuting gates and is exactly covariant; but then the link space is infinite-dimensional, and the finite factorisation above is not available. With quantum links the factorisation is available, but `U_p` on two plaquettes that share a link contain `S^+_l` and `S^-_l` and do not commute, so a plaquette layer needs an ordering of plaquette classes, and no ordering is invariant under the rotations. This draft takes quantum links and no plaquette layer. Either choice keeps Theorem B4.

**Theorem B5 (one mode per site gives no non-abelian frame group for the tick).** Suppose a compact group `G` acts on modes by one-body unitaries, either (a) site by site, or (b) on the eight corner modes of each even cell, and the dressed half-tick gates are invariant under local `G` transformations combined with transformations of link registers attached to the gate's own cube. Then the image of `G` in the transformations of the modes is abelian: in case (a) a subgroup of `U(1)` per site, in case (b) the scalars `U(1)` per cell.

*Proof.* (a) A one-body unitary on one mode is a phase (Lemma B3 for the number-conserving part). (b) Let `g` act on the eight corner modes of the even cell `A`. Each odd cube `C` contains exactly one corner `x` of `A` (an odd cube `b + (1,1,1) + {0,1}^3` meets the even cube `b' + {0,1}^3` in exactly one site when they meet, since their coordinate ranges `{b_j + 1, b_j + 2}` and `{b'_j, b'_j + 1}` overlap in one value per axis). The dressed gate of `C` is `Gamma(u_C)` times link factors, with `u_C` a one-body unitary that acts nontrivially on `c_x` (its generator hops `x` to its three neighbours in `C`). Invariance requires `Theta_g(Gamma(u_C) . links) = Gamma(u_C) . links'` with `links'` supported on the links of `C`. On modes, `Theta_g Gamma(u_C) Theta_g^{-1} = Gamma(g u_C g^{-1})` (lift homomorphism). Its support is `g(span of modes of C)`. For it to stay inside the modes of `C`, `g` must map `c_x` into `span(modes of C) ∩ span(modes of A) = span(c_x)`. This holds for every corner `x` of `A` (each corner lies in one odd cube), so `g` is diagonal in the corner basis. The even gate of `A` is internal to `A` and, with frames per cell, has no link registers inside `A`; invariance needs `g` to commute with `u_A = exp(-i theta R_A)`. A diagonal `g` commutes with `R_A` iff `g_x = g_y` whenever `<y|R_A|x> != 0`. The cube graph is connected, so `g` is a scalar. ∎

*Scope of Theorem B5.* It covers one-body (mode-linear) frame actions. Many-body unitaries on a cell's Fock space can have non-abelian commutants (#9882: "U(m) commutants with m >= 3 occur. They act on n-particle states, not as one-body transformations of the modes, so they are not minimal-coupling gauge groups"). It also does not cover several modes per site or per corner, which is PS-5's fallback.

**Consequence for GA1/GA2 and the skeleton.** Under the chosen law with one mode per site, PS-6 gives a `U(1)` lattice gauge theory (compact QED with Kawamoto-Smit-type fermions on a Margolus tick). The skeleton's "simplest gauge sector is a pure SU(2) lattice gauge theory" does not follow. A non-abelian gauge group needs site content beyond one mode per site, or a non-abelian field that emerges at a coarser rung. This is GA1-i's problem; LW1 records it.

**Proposed specification PS-6r (register algebra and gauge layers).**
> "Each link register is a spin-`S` quantum link carrying the frame group of the site content. Link registers carry odds but no actual configuration and no records. Besides the dressed matter gates, the update may contain one layer of on-link electric gates."

*Reasons.* PS-6 names a register but not its algebra. Theorem B4 needs `[E, U] = U`. A quantum link keeps every register finite, like a site, and allows the nearest-neighbour factorisation above. With quantum links the matter hops move the link values (`U_l = S^+_l` changes `E_l`), so the gauge field has dynamics without a plaquette layer. A plaquette layer is left out because no rotation-covariant finite-depth form of it was found for quantum links. "No records on links" keeps the Record axiom's objects as sites, as the Lattice and Record axioms speak of sites. (#10124 corrections, entry 4, records that different notes used different link record rules; this choice follows #9887's.)

### 5.4 PS-3: actuality, transport and formation

**Definitions.** Fix a finite set `Lambda` that is a union of whole cubes of the active tiling. Let `rho` be the reduced state on the modes of `Lambda` and on the links inside it. Let `U_Lambda` be the product of the dressed gates of the active cubes in `Lambda`. Configurations: `Omega_Lambda = {0,1}^Lambda`, projectors `P_c` (tensored with the identity on links). Born weights: `p(c) = tr(P_c rho)`, `p'(c') = tr(P_{c'} U_Lambda rho U_Lambda^*)`. Support: `S = {(c, c') : P_{c'} U_Lambda P_c != 0}`. Couplings: `Pi(p, p'; S)` = probability measures `pi` on `Omega x Omega` with marginals `p`, `p'` and `pi(S^c) = 0`. Cost: `d(pi) = sum pi(c, c') |c Δ c'|` (number of modes that change). Entropy: `H(pi) = - sum pi log pi`.

Because the gates are even and act on disjoint cubes, `P_{c'} U_Lambda P_c` is (up to a sign from mode ordering) the tensor product of the cube factors `P_{c'_C} G_C P_{c_C}`. So `S = prod_C S_C` is a product of per-cube supports.

Also, the reduced state on `Lambda` after the half-tick is exactly `U_Lambda rho U_Lambda^*`: gates outside `Lambda` are even and act on disjoint modes and links, so they drop out of every expectation of an operator in `Lambda`.

**Lemma B6 (support-respecting couplings exist; supply-demand bound).** For every unitary `U` on a finite-dimensional space with orthogonal projectors `{P_c}` summing to the identity, and every density matrix `rho`, `Pi(p, p'; S) != ∅`.

*Proof.* Step 1 (the bound). For a set `A` of outputs let `N^T(A) = {c : P_{c'} U P_c != 0 for some c' in A}`. With `P_A = sum_{c' in A} P_{c'}` and `P_N = sum_{c in N^T(A)} P_c`, we have `P_A U P_c = 0` for `c` outside `N^T(A)`, so `P_A U = P_A U P_N`. Then `p'(A) = tr(P_A U rho U^* P_A) = tr( (P_A U)(P_N rho P_N)(P_A U)^* ) <= ||P_A U||^2 tr(P_N rho P_N) <= p(N^T(A))`, using `tr(B X B^*) <= ||B||^2 tr X` for `X >= 0`.
Step 2 (the forward bound). For a set `X` of inputs let `N(X) = {c' : P_{c'} U P_c != 0 for some c in X}`. Put `A = Omega ∖ N(X)`. If `c` were in `N^T(A) ∩ X`, some `c'` in `A` would satisfy `P_{c'} U P_c != 0`, so `c'` would be in `N(X)`, a contradiction. So `N^T(A)` lies in `Omega ∖ X`, and Step 1 gives `1 - p'(N(X)) = p'(A) <= p(Omega ∖ X) = 1 - p(X)`. Hence `p(X) <= p'(N(X))`.
Step 3 (max flow). Build the network: source to each input `c` with capacity `p(c)`; input `c` to output `c'` with infinite capacity if `(c, c')` is in `S`; output `c'` to sink with capacity `p'(c')`. A cut of finite capacity is given by inputs `X` and outputs `Y` on the source side with `N(X)` inside `Y`; its capacity is `p(Omega ∖ X) + p'(Y) >= p(Omega ∖ X) + p'(N(X)) >= p(Omega ∖ X) + p(X) = 1`. The cut that separates the source alone has capacity 1. By max-flow min-cut (Ford and Fulkerson 1956; credited, standard), the maximum flow is 1. A flow of value 1 saturates every source edge and every sink edge, so `pi(c, c') =` flow on `c -> c'` is a coupling of `p` and `p'` supported on `S`. ∎

This is the supply-demand form of Gale's theorem (1957). #9902 reports the same bound numerically ("the supply-demand bound for any unitary in any basis (20,000 sets, max excess 2e-15)", as quoted in #10124). Aaronson's flow theory (2005) uses the same structure.

**Theorem B7 (the PS-3 transport exists and is unique on every finite box).** For every finite union of active cubes `Lambda` and every state, the set of fewest-change couplings `F = argmin_{Pi(p,p';S)} d` is a nonempty compact convex face of `Pi(p,p';S)`, and `H` has exactly one maximiser `pi*` on `F`. The transport kernel `K(c'|c) = pi*(c, c')/p(c)` is defined for every `c` with `p(c) > 0`.

*Proof.* `Pi(p,p';S)` is nonempty (Lemma B6), and it is a polytope (finitely many linear equalities and nonnegativity constraints in finitely many variables), so compact and convex. `d` is linear, so its minimum is attained and the set of minimisers is a face, nonempty, compact and convex. `H` is continuous and strictly concave on probability vectors (the function `-t log t` is strictly concave on `[0,1]`), so it has exactly one maximiser on a nonempty compact convex set: if `pi_1 != pi_2` were both maximisers, `H((pi_1 + pi_2)/2) > (H(pi_1) + H(pi_2))/2 = max`, a contradiction. ∎

On a torus the same proof applies with `Lambda` the whole torus.

**Proposed specification PS-3h (the transport acts per half-tick).**
> "The actual configuration is a configuration of site occupations. It exists at every half-tick and moves once per half-tick, using only the nonzero matrix elements of that half-tick between occupation configurations."

*Reasons.* PS-3 says "at every tick" and "support-respecting" without naming the support. The supplied models that keep Born use half-ticks (#10124: "a transport that uses only nonzero elements of each half-tick"). The half-tick is the canonical layer: Lemma A1a's two-site decomposition is not unique, while the half-tick (the product of commuting cube gates) is. The support of the full tick `G_o G_e` can be smaller than the composition of the half-tick supports, because of cancellations, so "per tick" and "per half-tick" are different laws. This specification picks the one the evidence uses.

**The word "copied".** PS-3 says "A record forms at a site when the site's actual value has been copied into at least two neighbouring sites." The text does not define "copied". Three readings:

- (R1) *Configuration agreement.* At tick `n`, the actual values of `x` and of at least two neighbours agree. In the half-filled sea this holds at a positive fraction of sites at every tick (the probability that three given sites agree is positive in any state whose Born measure gives all eight patterns positive weight). So under (R1) records form at a positive density in the vacuum at the first tick and saturate quickly. They copy nothing: agreement by chance is not a copy.
- (R2) *Dynamical copy.* A neighbour's actual value changed at tick `n` to equal `x`'s. Also chance-prone, and it depends on the transport, which Lemma LW1-U leaves open at infinite volume.
- (R3) *Law-level copy.* The law gives probability one that the actual values agree: `omega_n((n_x - n_y)^2) = 0`. Then the neighbour's value is a copy in the state, and by PS-11 it agrees in the realized history.

**Proposed specification PS-3c.**
> "The actual value of a site has been copied into a neighbouring site at a tick when the law gives probability one that their actual values agree at that tick. A record forms at the end of a tick at each site that carries no record and whose actual value has then been copied into at least two of its neighbours; it locks the site's actual value."

*Reasons.* (1) It makes the formation site and time law-level (functions of `omega_n`), so they pass the realized-state counterfactual test. (2) It gives the Admissibility check exactly (Theorem B9). (3) It matches #10054's working case ("a three-site redundant record (GHZ) fixes the Z basis") and its failure case ("a two-site record (Bell) leaves a continuous U x U* family"): two copies plus the site make three. (4) It is covariant under the full site group (the rule reads only the six-neighbour shell). (5) It never conflicts with "records never condition the odds" (it reads the odds; it does not change them).

**Theorem B8 (in a quasi-free state, a perfect copy only joins deterministic sites).** Let `omega` be a gauge-invariant quasi-free state with one-body density `G_{xy} = omega(c_y^dag c_x)`. Then `omega((n_x - n_y)^2) = 0` iff `G_{xy} = 0` and `(G_xx, G_yy)` is `(0,0)` or `(1,1)`.

*Proof.* `(n_x - n_y)^2 = n_x + n_y - 2 n_x n_y`. Wick's theorem for gauge-invariant quasi-free states gives `omega(n_x n_y) = G_xx G_yy - |G_xy|^2` for `x != y`. So `omega((n_x - n_y)^2) = G_xx(1 - G_yy) + G_yy(1 - G_xx) + 2|G_xy|^2`. Each of the three terms is nonnegative (`0 <= G_xx <= 1`). The sum is zero iff `G_xy = 0` and `G_xx(1-G_yy) = G_yy(1-G_xx) = 0`, i.e. `G_xx = G_yy` in `{0, 1}`. ∎

**Corollary B8a (no record in the free vacuum).** Under PS-3c and the free tick, starting from the PS-7 sea, no record ever forms. Proof: the sea is quasi-free and stationary with `G_xx = 1/2` at every site (Theorem B10), so no perfect copy exists at any tick. ∎ This is the exact form of the vacuum theme's "Records on change are frozen in the tested half-filled seas (#9876, #10018)" (quoted in the skeleton). The arrow (TM1) must come from the initial state or from interactions. Under reading (R1) the vacuum would instead record everywhere at once. Neither reading gives a slow vacuum record rate; the owner's choice of reading decides which tension TM1 inherits.

**Theorem B8b (records do form; witnesses).** (i) If `omega_0` is an even product state in which the cube of side 7 centred at `x` is empty, then at tick 1 the sites near `x` are still deterministically empty, and records lock "empty" there. (ii) Let `psi` be the even state `(|111>_{xyz}|000>_{abc} + |000>_{xyz}|111>_{abc})/sqrt2` on six sites, with `y, z` neighbours of `x` and `a, b, c` other sites, times any even state elsewhere, and let `omega_0 = omega_psi o alpha^{-1}` (the state whose image after one tick is `omega_psi`). Then at tick 1 `x` has perfect copies in `y` and `z`, `omega_1(n_x) = 1/2`, and a record forms at `x` locking 0 or 1, each with law-probability 1/2.

*Proof.* (i) Gates are number-conserving and act within cubes. In one tick a mode moves within one even cube and then within one odd cube, so each coordinate changes by at most 2. A site's occupation at tick 1, and the occupations of its neighbours, depend only on the initial state within sup-distance 3. The gates acting there conserve the number of fermions in that region, which is zero. So `omega_1(n_y) = 0` for `y = x` and for its neighbours, and `omega_1((n_x - n_y)^2) = 0`. (ii) Both branches have three fermions, so `psi` is even (parity superselection is respected). In `psi`, `n_x = n_y = n_z` on each branch, so the copy condition holds and `omega_1(n_x) = 1/2`. `omega_0` is a state because `alpha` is an automorphism. PS-4 holds because formation is evaluated at ticks `n >= 1` only. ∎

So the axiom "Records form." is consistent with `L_cube` on a nonempty domain of initial states, including states with genuinely random records.

**Theorem B9 (the Admissibility and Record checks under PS-3c).** Read "the nearest-neighbor conditions" of `x` at tick `n` as the reduced state of the six-neighbour shell of `x` at tick `n` (this settles LW1-i). Then:
(i) *Determined by.* Conditional on formation at `x` at tick `n`, the locked value has the law `P(v) = omega_n(n_y^v (1 - n_y)^{1-v})` for any copy neighbour `y`; this is a function of the shell's reduced state alone.
(ii) *Varies with.* There are two shell states giving different laws (shell states in which `y, z` are both empty, or both occupied, with the copy present).
(iii) *One fixed rule, covariant.* The map from shell state to law is the same at every site and is invariant under every translation and every rotation about the site that maps the shell to itself.
(iv) *Record.* Each site carries at most one record (formation only at unrecorded sites); records are permanent (nothing removes them); a record locks one admissible possibility (the actual value has positive Born weight with law-probability one, since the actual configuration is distributed as the Born law and the transport stays in the support); readout uses record content only (nothing in the law reads anything else).

*Proof.* (i) Formation at `x` means two neighbours `y, z` with `omega_n((n_x - n_y)^2) = 0`. Then `n_x = n_y` with law-probability one, so the law of the actual value of `x` equals the Born law of `n_y`, which depends only on `omega_n` restricted to `y`. Different copy neighbours give the same law, because each agrees with `x` with probability one. The formation event itself is a function of `omega_n`, not of the actual configuration, so conditioning on it does not change the Born law of the actual configuration. (ii) Immediate. (iii) The rule names no direction and no position. (iv) As stated; admissibility: the transport kernel moves only to configurations of positive Born weight (it is a coupling with second marginal `p'`), and `n_x`'s value in the actual configuration then has positive weight. ∎

Reading note (2) of the axiom says the distribution "does not supply the formation site, probability, or rate". PS-3c supplies them; this is consistent with the note, which leaves them to "downstream supplier content".

### 5.5 PS-7: the vacuum

**Theorem B10 (the PS-7 sea).** Let `V` be the one-body tick of Definition A1 with `0 <= mu < 2 eps < pi`. Then:
(i) The quasi-energies `w` (eigenvalues `e^{-iw}` of the Bloch matrix over the cell lattice) satisfy `cos w = A S(K) - B`, with `S(K) = (cos K_1 + cos K_2 + cos K_3)/3`, `A = (cos 2b + cos mu)/2`, `B = (cos 2b - cos mu)/2`, `b = pi/2 - eps`, each value with multiplicity 4 for each sign of `w`. [check: max deviation `1.9e-15` over four `(eps, mu)` pairs on the 6^3 torus.]
(ii) `|w|` lies in `[mu, 2 eps]`. So for `mu > 0` the spectrum has gaps at `w = 0` and `w = pi`, and the projection `P = 1_{w < 0}(V)` is canonical. For `mu = 0` the band touches `w = 0` only at `K = 0`, a null set.
(iii) The antiunitary `Theta = D_s K_c` (sublattice sign times complex conjugation in the site basis) commutes with `V`. Hence `Theta P Theta^{-1} = 1 - P` (up to the null set at `w = 0` when `mu = 0`), and `P_xx = 1/2` for every site `x`.
(iv) The quasi-free state `omega_P` (`omega_P(c^dag(f) c(g)) = <g, P f>`) is a pure state of `A(Z^3)`, stationary under `alpha_V` (the Bogoliubov automorphism of `V`), invariant under `G_U`, and half filled: `omega_P(n_x) = 1/2` at every site.
(v) For `mu > 0`, `P_{xy}` decays exponentially in `|x - y|`.

*Proof.* (i) Step 1, the anticommutator. `R_e R_o + R_o R_e = (1/3) sum_i (T_{2e_i} + T_{-2e_i})`, with `T_t` the shift by `t`. Each term of the product is a two-step path `x -> y -> z` using one odd edge and one even edge (in either order). There is no backtracking: a path `x -> y -> x` uses one edge twice, and an edge belongs to one tiling only (Definition A1 (2)). *Turning paths cancel:* the paths `x -> x + e_i -> x + e_i + e_j` (in `R_e R_o`, which applies `R_o` first) and `x -> x + e_j -> x + e_j + e_i` (in `R_o R_e`) exist under the same condition (`x_i` odd and `x_j` even, or the reverse parities for the reverse order), and their amplitudes are `(1/3) eta_i(x) eta_j(x + e_i)` and `(1/3) eta_j(x) eta_i(x + e_j)`. Their ratio is the product of the four signs around the plaquette, which is `-1` (Definition A1 (3); this plaquette has edge directions of opposite parity, so it lies in no single cube, and it is here that the flux on every face of `Z^3` is used). So they cancel; the same holds for negative directions. *Straight paths remain:* along axis `i`, consecutive edges alternate between the tilings, so exactly one of the two products contains `x -> x + e_i -> x + 2e_i`, with amplitude `(1/3) eta_i(x) eta_i(x + e_i) = 1/3` (`eta_i` does not depend on `x_i`). [check: identity holds to `1.1e-16` on the 6^3 torus.] On the Bloch fibre of cell momentum `K`, `T_{2e_i}` acts as `e^{iK_i}`, so the anticommutator is the scalar `2 S(K)`.
Step 2, the tick. With `alpha = eps - mu/2`, `beta = eps + mu/2`: `V = (cos beta + i sin beta R_o)(cos alpha - i sin alpha R_e)`. Expanding `V` and `V^* = (cos alpha + i sin alpha R_e)(cos beta - i sin beta R_o)`, the terms linear in `R_e` or `R_o` cancel in the sum, and `V + V^* = 2 cos alpha cos beta + sin alpha sin beta (R_e R_o + R_o R_e)`. On the fibre this is `2 (cos alpha cos beta + sin alpha sin beta S(K))` times the identity. Every eigenvalue `e^{-iw}` of the unitary `V(K)` therefore has `cos w = cos alpha cos beta + sin alpha sin beta S(K)`. Now `cos alpha cos beta = (cos mu + cos 2eps)/2` and `sin alpha sin beta = (cos mu - cos 2eps)/2`; with `cos 2b = cos(pi - 2eps) = -cos 2eps` these are `-B` and `A`. So `cos w = A S(K) - B`.
Step 3, multiplicities. `tr R_e(K) = tr R_o(K) = 0` (hops are off-diagonal), so `det V(K) = exp(-i alpha tr R_e) exp(i beta tr R_o) = 1`. All eight eigenvalues are `e^{-iw}` or `e^{+iw}` for one `w(K)`; with `n_+` and `n_-` of each, `det V(K) = e^{-i(n_+ - n_-) w} = 1`. For `K` with `w(K)/pi` irrational this forces `n_+ = n_- = 4`. Under the window of (ii) the eigenvalues never reach `0` or `pi` for `mu > 0`, so `n_+` is constant in `K` (eigenvalues move continuously and cannot cross the gaps), hence `4` everywhere. For `mu = 0` the same argument runs on the connected set `K != 0`.
(ii) `A >= 0` iff `cos mu >= cos 2 eps` iff `mu <= 2 eps`. With `S` in `[-1, 1]`, `cos w` ranges over `[-A - B, A - B] = [cos 2 eps, cos mu]` (since `-A - B = -cos 2b = cos 2 eps` and `A - B = cos mu`). So `|w|` is in `[mu, 2 eps]`, inside `(0, pi)` when `0 < mu` and `2 eps < pi`.
(iii) `D_s R D_s = -R` (every hop joins opposite sublattices), and `R` is real. So `D_s V_e D_s = exp(+i alpha R_e) = conj(V_e)` and `D_s V_o D_s = exp(-i beta R_o) = conj(V_o)`; hence `D_s V D_s = conj(V)`, i.e. `Theta V Theta^{-1} = V`. If `V psi = e^{-iw} psi` then `V Theta psi = Theta V psi = e^{+iw} Theta psi`. So `Theta` maps the spectral subspace of `w < 0` onto that of `w > 0`: `Theta P Theta^{-1} = 1 - P - Q_0`, with `Q_0` the projection on `w in {0, pi}`, which is zero by (ii) (or a null set when `mu = 0`: the spectral measure of `{0}` is the Lebesgue measure of `{K : w(K) = 0}`, which is zero). `(Theta P Theta^{-1})_{xx} = conj(P_xx) = P_xx` (diagonal entries of a Hermitian operator are real; `D_s` contributes `(+-1)^2`). So `P_xx = 1 - P_xx`.
(iv) For any projection `P` on `l^2(Z^3)`, the gauge-invariant quasi-free state with two-point function `P` is a pure state of the CAR algebra (Powers-Størmer; credited, standard). `V P V^* = P` because `P` is a spectral projection of `V`, so `omega_P o alpha_V = omega_P`. Each element of `G_U` is implemented by a one-body unitary commuting with `V` (Theorem A2), hence with `P`, so `omega_P` is invariant. Half filling is (iii).
(v) `V` has finite range; for `mu > 0` the contour around the negative arc of quasi-energies lies in the resolvent set at distance at least `min(mu, pi - 2eps)` from the spectrum; the Combes-Thomas estimate (credited, standard) gives exponential decay of `(z - V)^{-1}_{xy}` on the contour, hence of `P_{xy}`. ∎

**Proposed specification PS-7r (which sea).**
> "The vacuum is the quasi-free state that fills every mode of negative quasi-energy of the free one-body tick, the cut being placed at quasi-energy pi, which lies in a gap when 2 eps < pi."

*Reasons.* "Negative quasi-energy" is not canonical for a Floquet unitary (quasi-energy is an angle). Theorem B10 (ii) shows that for `0 < mu < 2 eps < pi` both cuts lie in gaps, so the choice is forced once the cut is placed in the gap at `pi`. For `eps = pi/2` (#9872's tick) the gap at `pi` closes ("The only other node is w = pi at K = pi(1,1,1), which mu does not gap", #9872), and the sea is not canonical. The window `2 eps < pi` is CL-1's "the partner at K = pi(1,1,1) is gapped while MN < 2 eps" in the flat case.

### 5.6 PS-4 and PS-2

- PS-4: the law's domain is a supplied `omega_0`; formation is evaluated at ticks `n >= 1`; so `R_0 = ∅`. ✓
- PS-2: used only for C3 (Born weights on configurations) and in Theorem B9.

### 5.7 PS-11: consistency

**Theorem B11 (PS-11 read over all statements is inconsistent for atomless history laws; the vacuum gives one).** (i) Let `Q` be the law of the actual history. If `Q({h}) = 0` for every history `h`, then PS-11 applied to every statement contradicts PS-3's "One actual configuration exists at every tick". (ii) The Born measure of the PS-7 sea on `{0,1}^{Z^3}` has no atoms. So does the Born measure of the tracial state (each site `1/2`, independent), which is a law-admissible initial state and stationary under any update.

*Proof.* (i) For each history `h`, the statement "the realized history is not `h`" has law-probability one. PS-11 then makes each such statement true, so the realized history differs from every history; no realized history exists. (ii) Every configuration `c` has infinitely many occupied sites or infinitely many empty sites. For a gauge-invariant quasi-free state with two-point function `P`, `omega(prod_{x in F} n_x) = det(P_F)` and `omega(prod_{x in F}(1 - n_x)) = det((1 - P)_F)` (Wick; standard). `P_F` and `(1 - P)_F` are positive semidefinite with diagonal entries `1/2`, so by Hadamard's inequality each determinant is at most `2^{-|F|}`. Taking `F` inside the occupied (or the empty) sites of `c`, `mu({c}) <= 2^{-|F|}` for arbitrarily large `F`, so `mu({c}) = 0`. The tracial case is the product measure. The one-time marginal of `Q` is this measure, so `Q` has no atoms. ∎

**Proposed specification PS-11c.**
> "A statement that the law gives probability one holds in the realized history, for each statement in a fixed countable list. The list contains every event that names finitely many sites and ticks, and every limiting-frequency statement about such events that a part uses."

*Reason it is consistent.* A countable intersection of events of probability one has probability one, so it is not empty, and the realized history can lie in it. BR1's frequency claims are countably many (one per local pattern and rational tolerance), so the list covers them. The analogous classical device is Martin-Löf randomness (credited); PS-11c does not need its computability clause.

### 5.8 The D4 law against PS-1

**Theorem B12 (the D4 event law is not a PS-1 update).** (i) A PS-1 law is one fixed update applied tick after tick, so every symmetry of its defining data maps ticks to ticks. No element of `W(F4)` that moves the time root `r_t` off `+-r_t` does, so `W(F4)` is not a symmetry of any PS-1 law on the events of Theorem A3; at most the root stabiliser is (#10096: "48 elements, the slice's cube group"). (ii) The D4 law's real time is "the Osterwalder-Schrader transfer over two half-ticks"; for its scalar sector #10094 shows the root-sliced step is "exponentially local", which is not "finitely many layers of nearest-neighbour gates". (iii) For its fermion sector, #10096: "the D4 law does NOT survive for fermions as written ... that weight's fermion sector has no positive slice Hilbert space"; #10097 (in #10130): "The nearest-neighbour fermion family has no fully positive transfer". So no unitary real-time fermion update is defined by the D4 weight.

*Proof.* (i) If `g` in `W(F4)` maps `r_t` to a vector not proportional to `r_t`, it maps the slice `h = 0` (a hyperplane orthogonal to `r_t`) to a hyperplane not orthogonal to `r_t`, which contains events of many different ticks. A symmetry of a PS-1 law must map the state space at a tick to a state space at a tick (the update count orders the history), so `g` is not one. The stabiliser of `+-r_t` maps slices to slices. (ii)-(iii) quoted. ∎

Consequences. Without a PS-1 update, PS-3's transport has no half-tick to respect, and PS-7's "the update's fermion modes" has no referent. #10054 (in #10124) states the same gap from the history side: "History actuality has no decoherence functional for the chiral weighting, which has no known tick form". And a unitary walk on the same events (#10096 route C) is "a unitary, strictly local fermion, but with dim-6 nonzero" with "the same O_h shape as CL-1's" — it belongs to the cube-tick class, not to the `W(F4)`-protected one.

### 5.9 Table of checks

| Requirement | Cube tick `L_cube` | D4 event law |
|---|---|---|
| Lattice: NN adjacency | yes (Lemma A1a) | no on `Z^3` sites (hops of length `sqrt3` and `2`); yes read on cells |
| Lattice: no privileged site | yes (Cor. A2a) | events are cells, not sites |
| Translations, site rotations (plain) | no (Thm A2 (iii)); forced for free one-mode ticks (Thm B2) | no |
| Cell reading PS-1c | yes (Thm A2) | weight: `W(F4)`; real time: root stabiliser |
| Qubit: one mode per site | yes | no as run (four supplied components per event) |
| PS-1 unitary, finite depth | yes | no (Thm B12) |
| PS-3 transport (finite box) | exists, unique (Thm B7) | undefined (no tick) |
| PS-3 formation, Admissibility | yes under PS-3c (Thm B9) | undefined |
| PS-6 exact gauge invariance | yes, `U(1)` (Thm B4); non-abelian no with one mode (Thm B5) | Euclidean triangle loops; no real-time form |
| PS-7 vacuum | canonical sea for `0 < mu < 2eps < pi` (Thm B10) | no referent |
| PS-4 | yes | yes (trivially) |
| PS-11 | needs PS-11c (Thm B11), as for any atomless law | same |

---

## 6. Proposed specifications, collected

Each is for the owner to decide. None is used as if adopted; every result that needs one says so.

1. **PS-1c.** "In PS-1 and in Admissibility, covariance under lattice translations and proper cubic rotations is read on cells: the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites." Reasons: Section 5.1.
2. **PS-3h.** "The actual configuration is a configuration of site occupations. It exists at every half-tick and moves once per half-tick, using only the nonzero matrix elements of that half-tick between occupation configurations." Reasons: Section 5.4.
3. **PS-3c.** "The actual value of a site has been copied into a neighbouring site at a tick when the law gives probability one that their actual values agree at that tick. A record forms at the end of a tick at each site that carries no record and whose actual value has then been copied into at least two of its neighbours; it locks the site's actual value." Reasons: Section 5.4.
4. **PS-6r.** "Each link register is a spin-`S` quantum link carrying the frame group of the site content. Link registers carry odds but no actual configuration and no records. Besides the dressed matter gates, the update may contain one layer of on-link electric gates." Reasons: Section 5.3.
5. **PS-7r.** "The vacuum is the quasi-free state that fills every mode of negative quasi-energy of the free one-body tick, the cut being placed at quasi-energy pi, which lies in a gap when 2 eps < pi." Reasons: Section 5.5.
6. **PS-11c.** "A statement that the law gives probability one holds in the realized history, for each statement in a fixed countable list. The list contains every event that names finitely many sites and ticks, and every limiting-frequency statement about such events that a part uses." Reasons: Section 5.7.

PS-1c and PS-3c carry the most weight. Without PS-1c no candidate on file passes PS-1. Without PS-3c (or another precise reading) "copied" has no meaning, and the Admissibility check cannot be written.

---

## 7. Part (c): comparison on what the downstream parts need

### 7.1 LZ1 (the first Lorentz-violating dimension)

**Theorem C1 (the cube tick's tree-level dimension-six term).** For the massless free tick (`mu = 0`), with `s = sin eps` and cell momentum `K = k n` (`|n| = 1`), the light band obeys
`w(K) = (s k / sqrt3) [1 + k^2 (s^2/72 - (n_1^4 + n_2^4 + n_3^4)/24) + O(k^4)]`.
So the phase velocity has a `k^2` correction whose anisotropic part is `-(sum n_i^4) k^2/24`. It is nonzero for every `eps`. In site momentum `q = K/2` the anisotropic part is `-(sum n_i^4) q^2/6`.

*Proof.* At `mu = 0`, `A = sin^2 eps = s^2` and `-B = cos^2 eps`, so `cos w = s^2 S + 1 - s^2`, i.e. `1 - cos w = s^2 (1 - S)`. Expand: `1 - S = k^2/6 - k^4 (sum n_i^4)/72 + O(k^6)`; `1 - cos w = w^2/2 - w^4/24 + O(w^6)`. Put `w^2 = s^2 k^2/3 + X` with `X = O(k^4)`: then `s^2 k^2/6 + X/2 - s^4 k^4/216 = s^2 k^2/6 - s^2 k^4 (sum n^4)/72 + O(k^6)`, so `X = s^4 k^4/108 - s^2 k^4 (sum n^4)/36`. Hence `w^2 = (s^2 k^2/3)[1 + k^2 (s^2/36 - (sum n^4)/12)]`, and taking the square root gives the stated form. [check: residual divided by `k^4` stays below `4e-4` along the axis, face and body directions at `k = 0.02, 0.04`.] ∎

The anisotropic part `-S/6` in site units (with `S = sum n_i^4`) is the anisotropic part of #10091's "c_q = -S/6 + 1/24"; the isotropic part depends on `eps` (`s^2/18` here; `1/24` corresponds to `s^2 = 3/4`).

Comparison. The cube tick has a fixed dimension-six term (LZ1's `p = 2`). #10091 finds that this term breaks nuclei above "<= 46 EeV" and gives the verdict "EXCLUDED unless the rules also alter air-shower development (uncomputed)"; #10093 finds "TENSION, not EXCLUDED". The D4 Euclidean weight removes dimension six for spin up to 1 by `W(F4)` (#10094), but only in the Euclidean weight; its unitary walk "loses the dimension-six protection" (#10096). Under PS-1 both candidates therefore carry a dimension-six term in real time. The D4 result becomes a target: if the zoom of the cube tick flows to a `W(F4)`-symmetric Euclidean fixed point, the dimension-six term of the long-distance theory is set by the approach to that fixed point. That is a ZM1/LZ1 statement, open. **LZ1 favours D4 as a target, and gives no PS-1 law that realises it.**

### 7.2 CH1 (chirality and doublers) and MT1 (spin)

- Cube tick: the cell is spinorial with one mode per site (#10016: "the cell rep is spinorial"). The massless node "is not net-chiral" (#9872). Products of coins and shifts have `W3 = 0` (#9863). The partner at `K = pi(1,1,1)` is gapped for `2 eps < pi` (Theorem B10 (ii)). Without the copy mass the light content at `K = 0` is two degenerate Dirac copies (#10016: "the four tastes are E + E"). Chirality: "not obtained" (#10131).
- D4: one mode per event gives no spin 1/2 (#10104). The overlap on the D4 kernel gives Ginsparg-Wilson chirality in the Euclidean weight; "the slab is vector-like" (#10099, in #10130). No tick form.
- **CH1 and MT1 favour the cube tick**: spin 1/2 with one mode per site, and a tick on which PS-3 can run. Neither candidate has chirality.

### 7.3 GA1, GA2 and the T0 import

- Cube tick: exact `U(1)` Gauss laws with link registers (Theorem B4). No non-abelian frame group with one mode per site (Theorem B5). Real-time update; no Euclidean action.
- D4: Euclidean triangle-loop weight with `W(F4)`, which contains the hypercubic symmetry that T0's O(4) argument starts from (skeleton bridge Y3). Site reflection positivity "holds" for the free scalar (#10094). No real-time update.
- T0 is Euclidean (pure SU(2) Wilson on `Z^4`). Bridge Y1 asks for a reflection-positive Euclidean form of the framework's gauge sector. A unitary tick is not a positive transfer matrix (a unitary `T >= 0` is the identity), so for the cube tick Y1 is a long-distance statement (ZM1), not a lattice identity.
- **GA2 favours D4 as the Euclidean comparison object** for Y1 and Y3. **GA1 favours the cube tick** (exact real-time Gauss laws). Under either, the gauge group at one mode per site is abelian (Theorem B5 for the tick; the D4 theme lists as open "dynamical links, gauge loops and non-abelian fields", #10130 synthesis). The SU(2) rung of the skeleton's section 6 needs content beyond one mode per site.

### 7.4 TM1 and BR1 (records and the arrow)

- Cube tick: PS-3's transport is defined and unique on finite boxes (Theorem B7), with supplied-model evidence for Born, no signalling and CHSH `2 sqrt2` on the Margolus tick (#9893, #9930). Formation under PS-3c is law-level (Theorem B9). In the free vacuum no record forms (Corollary B8a).
- D4: no tick, so no transport; the arrow "breaks W(F4) in the STATE" (#10094).
- **TM1 and BR1 favour the cube tick decisively**: they need a tick.

### 7.5 Summary of the comparison

| Part | Needs | Cube tick | D4 law |
|---|---|---|---|
| LZ1 | high first LIV dimension | 6 (Thm C1) | 8 in the Euclidean weight; 6 for its unitary walk |
| MT1 | spin 1/2, one mode per site | yes | no (four supplied components) |
| CH1 | chiral light sector | not obtained | not obtained (Euclidean GW only) |
| GA1 | exact Gauss law in real time | yes, `U(1)` | no real time |
| GA2 / T0 | Euclidean RP, hypercubic symmetry | Y1, Y3 open | closer (W(F4) contains hypercubic) |
| TM1, BR1 | a tick for actuality | yes | no |

---

## 8. Part (d): the choice

**Choice: `L_cube` (Section 4).**

*Reason.* PS-1 asks for "a unitary map built from finitely many layers of nearest-neighbour gates". The cube tick is one (Lemma A1a). The D4 law is not (Theorem B12), and its fermion sector has no positive transfer (#10096, #10097). Every downstream part that needs a tick (PS-3, PS-7, TM1, BR1, MT1's carrier, GA1's real-time Gauss law) has one only under the cube tick. The D4 law's distinct advantage, the `W(F4)` protection of dimension six, holds only for a Euclidean weight, and the unitary walk on the same events loses it.

*How D4 enters.* Not as a law clause. (1) As a theorem about the cube tick: its events form a D4 lattice with time along a root (Theorem A3). (2) As a target for ZM1/LZ1: does the zoom of `L_cube` reach a `W(F4)`-symmetric Euclidean fixed point, and how fast? (3) As the Euclidean comparison object for GA2's bridges Y1 and Y3. So no combined law is needed; the combination is "cube tick as the law, D4 as its spacetime and as a long-distance target".

*What would reverse the choice.* Any one of these:
- (R1) A PS-1 update with a `W(F4)`-protected fermion: a unitary, finite-depth step on these events whose fermion sector keeps dimension six zero. Theorem B12 (i) shows it cannot have `W(F4)` as a symmetry of its defining data, so this would have to be an emergent protection; #10096 found none in the nearest-neighbour family. Or the owner relaxes PS-1 to exponentially local unitaries and a positive `W(F4)` fermion transfer is found (#10098: the zoom fixed point has "only real positive poles, but site positivity needs a one-slice buffer").
- (R2) Measurement excludes the cube tick's dimension-six term after the zoom and loops are included (#10091's verdict made firm with the air cross-section computed; #10093 says that cross-section is "the decisive unknown"), while a D4-type law passes.
- (R3) The owner rejects PS-1c. Then the cube tick fails PS-1, and so does D4; LW1 then needs a fully covariant interacting update, which no source supplies.
- (R4) CH1 or GA2 is shown to need a lattice-level `W(F4)` or hypercubic symmetry that no PS-1 update can have.
- (R5) A non-abelian gauge group is required at the lattice level with one mode per site (Theorem B5 says the cube tick cannot give one); if the D4 route can, that favours it. No source shows that it can.

---

## 9. Part (e): infinite-volume consistency of the chosen law

This part proves that `L_cube` is a well-defined law on `Z^3`: the update, the vacuum and the formation rule exist together at infinite volume, with every clause of the axioms and of the working set (under PS-1c, PS-3h, PS-3c, PS-6r, PS-7r, PS-11c) holding. One statement is outstanding: uniqueness of the transport at infinite volume (Lemma LW1-U).

The skeleton's item 3 asks for "finite-box laws ... consistent under inclusion". For a dynamics with boundaries this cannot hold as worded: a box's restriction of a larger box's history is not a closed system (influence enters from outside within the light cone). This draft proves the intended content instead: existence on `Z^3` with local agreement with finite-volume objects where that holds. The amended item 3 is stated in Section 10.

### 9.1 The update

**Theorem E1 (the update is an automorphism of the quasi-local algebra; Gauss laws are conserved).** Let `A` be the quasi-local C*-algebra of `Z^3` (the CAR algebra of the site modes, graded-tensored with the algebras of the link registers; for quantum links each link algebra is `M_{2S+1}(C)`; for rotors use the C*-algebra generated by the functions of `U_l` and the unitaries `exp(i t E_l)`). Then each half-tick and the `E` layer define automorphisms of `A`, and so does `U` (and so would a rotor plaquette layer). Each `exp(i theta G_x)` is fixed by them.

*Proof.* Take a layer that is a product of gates `g_j`, each even, each supported in a finite set `X_j`, with the `X_j` such that any finite set meets finitely many of them and gates in one layer commute (for the half-ticks the `X_j` are disjoint: cubes with their twelve links, disjoint by Definition A1 (2); for `E` each gate is on one link; for a rotor plaquette layer the gates are functions of commuting link operators). For a local `a` supported in a finite `F`, define `beta(a) = (prod_{j : X_j ∩ F != ∅} g_j) a (prod ...)^*`. Adding any further gate `g_k` with `X_k ∩ F = ∅` does not change this, because `g_k` is even and commutes with `a` (even operators commute with every operator of disjoint support in a graded tensor product) and with the other gates. So `beta` is well defined on the local algebra, is a *-homomorphism, is isometric (it is implemented by a unitary on each finite piece), and has inverse given by the same formula with `g_j^*`. It extends by continuity to an automorphism of `A`. The composition of the layers is an automorphism. By Theorem B4 each gate commutes with `exp(i theta G_x)`, so each layer fixes it. ∎

### 9.2 The vacuum

**Theorem E2a (the PS-7r vacuum of the free tick).** For `0 < mu < 2 eps < pi`, `omega_P` of Theorem B10 is a pure, stationary, `G_U`-invariant, exactly half-filled state of the CAR algebra on `Z^3`, with exponentially decaying two-point function. For `mu = 0` the same holds, except that the two-point function decays as a power (the Dirac point at `K = 0`). ∎ (Theorem B10.)

**Theorem E2b (stationary gauge-invariant half-filled states of the gauged law exist).** Let `omega` be any state of `A` that is invariant under `2Z^3`, under the gauge transformations, and half filled (`omega(n_x) = 1/2` averaged over a cell). Let `omega_N = (1/N) sum_{n<N} omega o alpha^n`. Every weak-* limit point of `omega_N` is a state that is stationary, invariant under `2Z^3` and under gauge transformations, and half filled. If `omega` is also invariant under `O_{c_0}`, so is the limit.

*Proof.* The state space is weak-* compact, so limit points exist. `omega_N o alpha - omega_N = (omega o alpha^N - omega)/N`, which tends to zero on each element, so limits are stationary. Translations in `2Z^3`, rotations in `O_{c_0}` and gauge transformations commute with `alpha` (Theorems A2, B4, E1), so invariance passes to each `omega o alpha^n` and to limits. Half filling: let `N_Lambda` be the number operator of a box `Lambda` that is a union of cells. `alpha(N_Lambda) - N_Lambda` is supported within distance 3 of the boundary of `Lambda` (gates conserve number and act within cubes), so `|omega(alpha(N_Lambda)) - omega(N_Lambda)| <= c |boundary of Lambda|`. For a translation-invariant state, dividing by `|Lambda|` and letting `Lambda` grow shows the density is preserved by `alpha`, and hence by Cesàro means and limits. ∎

For the rotor alternative with no electric or plaquette layer there is an exact product stationary state: `omega_P` on matter times the state with `U_l = 1` on every link (the dressed gates then act on matter as the free gates and leave the link state fixed, since they are functions of `U_l` and the link state is a joint eigenstate of all `U_l`). It is not gauge-invariant; its gauge average (Haar measure on the local gauge group, which is well defined on local elements) is stationary and gauge-invariant, by the argument above. Which stationary state PS-7 names when the gauge layers are on is VC1's question.

### 9.3 The formation rule

**Theorem E3 (formation is well defined at infinite volume).** For every state `omega_0` and every tick `n >= 1`, the set `F_n` of sites with two perfect copies (PS-3c) is a function of the three-site marginals of `omega_n = omega_0 o alpha^n`. The record set `R_n = R_{n-1} ∪ F_n` (formation only at unrecorded sites, so each site's record is the first one) is increasing in `n`, `R_0 = ∅`, and it is a deterministic function of `omega_0`. If `omega_0` is invariant under a subgroup of `G_U`, so is each `R_n`. ∎ (Immediate from the definitions.)

So the formation sites and times pass the realized-state counterfactual test (they are invariant over realized histories for given `omega_0`). The record values are realized data.

### 9.4 The actual configuration at infinite volume

**Theorem E4 (support-respecting couplings exist at infinite volume).** Let `omega` be any state of `A` and `mu, mu'` the Born measures (on site occupations) of `omega` and of `omega o beta`, with `beta` an active half-tick. Then there is a probability measure `pi` on `{0,1}^{Z^3} x {0,1}^{Z^3}` with marginals `mu, mu'` such that, for every active cube `C`, `pi`-almost surely `(c_C, c'_C)` lies in the cube support `S_C`. If `omega` is invariant under `2Z^3`, `pi` can be chosen invariant.

*Proof.* Let `Lambda_m` be an increasing sequence of finite unions of active cubes exhausting `Z^3`. By the remark after the definitions in Section 5.4, the Born law of `omega o beta` on `Lambda_m` is the Born law of `U_{Lambda_m} rho_{Lambda_m} U_{Lambda_m}^*`. Lemma B6 (with links traced out: its proof holds verbatim with `P_c` tensored with the identity on links) gives a coupling `pi_m` on `Lambda_m` supported on `prod_{C in Lambda_m} S_C`. Extend `pi_m` to all of `Z^3` by a product with any coupling of the outside (for instance the independent one). The space `({0,1} x {0,1})^{Z^3}` is compact; by the Riesz and Prokhorov theorems the sequence has a weak limit point `pi`. For a cylinder event inside `Lambda_{m_0}`, `pi_m` gives it its exact `mu` (or `mu'`) probability for all `m >= m_0`; cylinder events are clopen, so the limit keeps these probabilities. The same holds for the clopen event `{(c_C, c'_C) not in S_C}`, which has `pi_m`-probability zero once `C` is inside `Lambda_m`. For invariance, average `pi` over the translations of `2Z^3` in growing boxes (Følner averaging); marginals and the support event are invariant, so they are kept, and limit points are invariant. ∎

**Theorem E5 (the actual history exists at infinite volume).** For every state `omega_0` there is a probability measure `Q` on actual histories `(c_h)_{h >= 0}` in `({0,1}^{Z^3})^N` such that: (i) each `c_h` has law `mu_h`, the Born measure of `omega_h`; (ii) the history is a Markov chain; (iii) each step respects the cube supports of its half-tick; (iv) the odds `omega_h` never depend on records; (v) with records `R_n` of Theorem E3 and values `c_{2n}(x)` for `x` in `F_n` (half-tick `2n` is tick `n`), the Record axiom's clauses hold; (vi) PS-4 holds.

*Proof.* For each `h` choose a coupling `pi_h` of `mu_h, mu_{h+1}` by Theorem E4. The configuration space is a compact metric space, so `pi_h` disintegrates over its first marginal: `pi_h(dc, dc') = mu_h(dc) K_h(c, dc')` with a measurable kernel `K_h`. By the Ionescu-Tulcea theorem the kernels `K_h` and the initial law `mu_0` define a unique Markov measure `Q`. By induction its one-time marginals are `mu_h`: if `c_h ~ mu_h` then `c_{h+1} ~ mu_h K_h = mu_{h+1}`. (iii) holds because `pi_h` gives the support event probability one. (iv): `omega_h`, the image of `omega_0` under `h` half-tick automorphisms, is defined without records. (v): Theorem B9 (iv) at infinite volume; the locked value lies in the support of the Born law with `Q`-probability one. (vi): Theorem E3. If each `omega_h` is invariant under `2Z^3`, each `pi_h` may be taken in the set `O_h` of Theorem E6, and then every step is a PS-3 transport in the per-site sense. ∎

**Theorem E6 (the PS-3 selection is nonempty at infinite volume).** Let `omega_h` be invariant under `2Z^3`. Let `C_h` be the set of `2Z^3`-invariant couplings of `mu_h, mu_{h+1}` that respect the cube supports. Let `dbar(pi) = (1/8) E_pi sum_{x in cell} 1[c_x != c'_x]` (changes per site) and `s(pi)` the specific entropy of `pi` (per cell, on the pair alphabet). Then `O_h = argmax_s argmin_dbar C_h` is a nonempty compact convex set.

*Proof.* `C_h` is nonempty (Theorem E4) and weak-* closed (the marginal constraints and the support events are closed conditions, invariance is closed), inside a compact space, so compact; it is convex. `dbar` is the expectation of a cylinder function, hence continuous and affine, so its minimum on `C_h` is attained and the set of minimisers `M_h` is a nonempty compact convex face. `s` is affine and upper semicontinuous on invariant measures (affinity is proved in Section 9.5, Attack 1; upper semicontinuity: `s = inf_m H_{Lambda_m}/|Lambda_m|` over cubes `Lambda_m` of side `2^m` cells, by subadditivity, and an infimum of continuous functions is upper semicontinuous). An upper semicontinuous function on a nonempty compact set attains its maximum, and the set of maximisers of an affine function on a convex set is convex and, by upper semicontinuity, closed. ∎

So the infinite-volume law exists, with every element of `O_h` a valid PS-3 transport per half-tick. What is not proved is that `O_h` has one element. The Qualification ("at every state where the condition holds it gives exactly one answer") needs it, because multi-time record statistics can depend on the transport (#10124: "Bare two-time records depend on the distant setting ... after a pointer copy the two-time law equals the Born law of (pointer, outcome)").

### 9.5 The outstanding statement

**Lemma LW1-U (outstanding).** *For the cube tick, PS-3h and a `2Z^3`-invariant state `omega_h` (in particular the PS-7r vacuum and its half-tick images), the set `O_h` of Theorem E6 has exactly one element, and it is the local limit of the unique torus transports of Theorem B7 on tori of side `L -> infinity` with states converging locally to `omega_h`.*

Three distinct attacks, and the exact reason each fails.

**Attack 1: strict concavity, as on finite boxes.** On a finite box, uniqueness came from strict concavity of `H` (Theorem B7). At infinite volume the selecting functional is the specific entropy `s`, and `s` is affine on invariant measures. Proof of affinity: for invariant `pi_1, pi_2` and `t` in `(0,1)`, on each box `Lambda`, concavity of `H` gives `H_Lambda(t pi_1 + (1-t) pi_2) >= t H_Lambda(pi_1) + (1-t) H_Lambda(pi_2)`, and the mixture bound (from `H(X) <= H(X, T) = H(T) + H(X|T)` with `T` the mixing label) gives `H_Lambda(t pi_1 + (1-t) pi_2) <= t H_Lambda(pi_1) + (1-t) H_Lambda(pi_2) + log 2`. Divide by `|Lambda|` and let it grow: `s(t pi_1 + (1-t) pi_2) = t s(pi_1) + (1-t) s(pi_2)`. *Why the attack fails:* the strictly concave part of `H` is at most `log 2` per box, so it vanishes per site. If two optimisers exist, every mixture of them is also optimal, and nothing in `dbar` or `s` excludes that.

**Attack 2: torus limits.** The torus transports `pi_L` are unique (Theorem B7). Their local limit points lie in `C_h` (support and marginal conditions pass to limits, as in Theorem E4, provided the torus states converge locally to `omega_h`, which holds for the sea by Riemann-sum convergence of the torus projections at `mu > 0`). Two things are needed: (a) the limit is optimal, i.e. `lim dbar(pi_L) = min_{C_h} dbar`, and the analogous statement for `s`; (b) all limit points agree. The lower half of (a) is automatic (continuity of `dbar`). The upper half needs a recovery sequence: from an optimal `pi` in `C_h`, build torus couplings `pi'_L` of the torus Born laws, respecting the torus supports, with `dbar(pi'_L) -> dbar(pi)`. *Why the attack fails:* the torus Born laws are not restrictions of `mu_h`; turning `pi` into a coupling of the torus laws means moving probability between configurations, and the moves must use only nonzero matrix elements of the half-tick. Gluing `pi` to near-identity couplings between the torus laws and `mu_h` (the standard d-bar gluing) produces moves that are not in the support. No estimate of a "support-respecting distance" between the torus laws and `mu_h` is available. Without it, (a) is not shown, and (b) is not even approached.

**Attack 3: a dual (Gibbs) form.** On a finite box, the greatest-entropy coupling at a fixed cost has, by convex duality (entropic optimal transport, the Schrödinger-bridge form), the shape `pi(c, c') = exp(phi(c) + psi(c') - lambda d(c, c')) 1_S(c, c')`, and the fewest-change selection is the limit `lambda -> infinity`. If `phi` and `psi` were sums of local terms with summable interactions, the infinite-volume problem would be a zero-temperature limit of Gibbs measures with a local specification, and uniqueness could be attacked by Dobrushin's criterion at finite `lambda` plus a selection argument as `lambda -> infinity`. *Why the attack fails:* (i) `phi` and `psi` are fixed by the marginal constraints, which are the Born laws of the sea, a determinantal (fermionic) measure; no summable-potential (Gibbsian) form of these marginals is known, so `phi`, `psi` need not be local. (ii) Even with local potentials, the fewest-change selection is the `lambda -> infinity` limit, where Dobrushin's condition (a high-temperature condition) fails, and zero-temperature limits of Gibbs measures are known to be non-unique in general.

**What LW1-U decides.** If true, `L_cube` gives one answer at every state at infinite volume, as the Qualification asks. If false, the owner must choose among: a further tie-break rule (a proposed specification, for example "the transport is the local limit of the torus transports along a fixed sequence", which still needs Attack 2's limit to exist); restricting the readable record statistics to those that do not depend on the transport (single-time Born statistics and pointer-copied multi-time statistics, which #9930 and #10054 show transport-independent in supplied models); or a different actuality law.

**The easier analogue to try next.** The one-dimensional analogue: a Margolus walk on `Z` with one mode per site (two-site cells, flux plays no role), the half-filled sea, and the same PS-3 selection. There the per-site optimisation is over couplings of two determinantal measures on `{0,1}^Z` with a product support of two-site blocks. If LW1-U fails there (two invariant optimisers), it fails as stated; if it holds, its proof is the template.

---

## 10. Status of the LW1 statement (author-side)

Re-reading the skeleton's LW1 (a) items with what this draft proves:

1. *Admissibility.* Proved for `L_cube` under PS-3c (Theorem B9), with "conditions" read as the reduced state of the six-neighbour shell (this settles LW1-i). The rule is covariant under the full site group; the update is covariant under the cell group (needs PS-1c).
2. *Record.* Proved (Theorems B9 (iv), E3, E5 (v)).
3. *Consistency.* Proposed amended wording: "the law exists on `Z^3 x N`: the update is an automorphism of the quasi-local algebra, the vacuum is a stationary state of it, the formation rule is a function of the state, and an actual history exists whose one-time laws are the Born laws and whose steps respect the half-tick supports." Proved (Theorems E1-E6). Uniqueness of the transport at infinite volume: outstanding (Lemma LW1-U). Finite boxes: unique (Theorem B7).
4. *Uniqueness up to choice.* Free constants of `L_cube`: `eps`, `mu` (window `0 < mu < 2 eps < pi` for a canonical vacuum), `S`, `tau_E`; and the supplied `omega_0`. Readers: LZ1 (`eps`, Theorem C1), MT1/VC1 (`mu`, the gap), GA1/GA2 (`S`, `tau_E`), TM1 (`omega_0`).

Open inputs carried forward, named where they sit:
- Owner decisions: PS-1c, PS-3h, PS-3c, PS-6r, PS-7r, PS-11c.
- Lemma LW1-U (Section 9.5).
- One step of Section 5.3 is credited, not written out: Lie-algebra universality of edge-triple gates that include a quantum-link register (used for the nearest-neighbour form of the dressed gates).
- For downstream parts: no record in the free vacuum (Corollary B8a; TM1-i); `U(1)` only at one mode per site (Theorem B5; GA1-i and the skeleton's section 6); two light Dirac copies without the copy mass (MT1/FL1); a fixed tree-level dimension-six term (Theorem C1; LZ1, with #10091/#10093).

Nothing in this draft uses established physics to justify a step. Every literature result used is named and credited: max-flow min-cut (Ford-Fulkerson), Gale's supply-demand theorem, Givens/QR decomposition (Reck et al., Clements et al.), Powers-Størmer purity of quasi-free states, the Combes-Thomas estimate, Wick's theorem and Hadamard's inequality, the Ionescu-Tulcea and Prokhorov theorems, Meyer's scalar-walk result (rebuilt in full as Theorem B2), and, for orientation only, Aaronson's flow theory and Martin-Löf randomness. The scratch check refuted nothing and guided three numbers; it proves nothing.
