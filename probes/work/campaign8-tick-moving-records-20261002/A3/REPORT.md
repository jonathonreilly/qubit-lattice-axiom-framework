I'm done with the derivation and checks. The report follows.

# Lane M report: can moving records stay consistent with the possibilities' odds?

## 1. Question

Suppose I2 and I3 hold:
- records move at most one site per tick, with odds set by the neighbourhood;
- collisions are settled by relative probability;
- the shared possibilities change reversibly between ticks.

Is there a move rule T_t(x→y) under which, at every tick, the probability of each record configuration equals what the possibilities' odds assign? That is, P_{t+1}(y) = Σ_x T_t(x→y) P_t(x). And is that rule fixed by locality plus consistency?

## 2. Answer

**Conditional yes.** It depends on how a move is read.

**(a) A move is a fresh formation at the arrival site.** Here the shared possibilities are cut every tick so that they agree with the record. The rule is then unique, and consistency comes for free: the move odds are the formation odds of the possibilities after the change (EXACT). The cost is that the possibilities never interfere from one tick to the next, so a record diffuses: variance grows like t (CHECKED).

**(b) The record is guided.** The possibilities keep changing reversibly underneath it and are not cut by moves.
- A consistent one-site rule exists for every state if and only if each tick is strictly local, meaning no possibility reaches past the nearest neighbours in one tick (EXACT).
- Continuous change run for a whole tick does not qualify. At τ=1, 28.5% of the odds of a just-formed record land two or more sites away (CHECKED).
- The consistent rule is "follow the net flow": T(x→y) = max(0, J(x→y))/P_t(x), where J is a time-symmetric flow of the tick (the Margenau–Hill form, defined in Step 5) (EXACT).
- **One record on a line:** this rule is always valid. It is the unique rule that both uses a local formula and never sends odds both ways across a bond ("flow, not swap"). So locality + consistency + flow-not-swap fix it (EXACT). Without flow-not-swap it is not fixed (EXACT).
- **Loops (plaquettes of Z²/Z³) and several records:** the rule is not fixed. The time-symmetric choice sometimes asks a site to give away more odds than it holds: 68 of 570 random plaquette ticks, and most two-record ticks. Valid rules always exist (CHECKED).
- **Several linked records** need a joint rule. Independent per-record odds with relative-odds collisions miss the possibilities' odds by up to 0.50 in total variation (CHECKED).
- **Signalling:** single-tick record odds never carry a distant choice (EXACT). But the natural guided rules make a record's two-tick history depend on a distant choice, by up to 0.32 (CHECKED). Under (b), a moving record's past positions must therefore not be readable unless a new formation registers them.

## 3. Derivation

### Setup (supplied toy, not framework content)

- **Sites:** Z, a ring Z_N, or Z³.
- **Possibilities:** the one-excitation sector, ψ_t ∈ ℓ²(sites) ⊗ C^d.
  - d=1 is the case of one qubit per site, with the record being a locked |1⟩ in a sea of |0⟩.
  - d≥2 appears only in supplied cell models.
- **Odds:** P_t(x) = ‖Π_x ψ_t‖².
- **Tick:** ψ_{t+1} = U_t ψ_t. The tick is strictly range-1 when Π_y U Π_x = 0 unless y ∈ N̄(x), where N̄(x) is x plus its neighbours.
- **Record:** a definite site X_t, moved by a kernel T_t ≥ 0 with rows summing to 1 and support on N̄(x).
- **Consistency:** Prob(X_t = x) = P_t(x) for all t.
- **n records:** X_t is an n-subset of sites, and the possibilities live in the n-excitation sector of the qubit lattice. That sector holds at most one excitation per site.

### Step 1 (Task 1): what "moving the lock" can mean

The three readings are definitions (ARGUED); their consequences are EXACT.

- **R1, re-formation.** The lock is released at x, the possibilities change, and a record forms in N̄(x). Under Q1 the possibilities are cut to agree with it.
  - Departure: x is released, and the cut makes it agree with "no record here".
  - Arrival: the site is cut to agree with the record.
  - The rule is T(x→y) = ‖Π_y U ψ_x‖², where ψ_x is the agreeing state. It is unique and consistency is automatic. For d=1 it reduces to |U(y,x)|², a classical random walk.
- **R2, transported lock.** The change itself carries locked possibilities. This needs U to map a locked site to a single site, so the motion is deterministic.
- **R3, guided record.** The possibilities evolve by U regardless of the record. Q1's agreement holds only at formation.
  - Departure: the site is unrecorded but its possibilities are untouched, so it may still carry odds.
  - Arrival: the site is recorded but not cut.

**Flow versus swap at the possibility level (Lemma L1, EXACT).** Take one possibility per site, on a ring with N≥5 or on Z. Every strictly range-1 tick is one of two kinds:
- (i) mixing inside disjoint adjacent pairs, plus phases. This is swap-like: zero net transport of possibility content across every cut (index 0).
- (ii) a phase-weighted uniform shift. This is the I4 conveyor (index ±1).

Proof:
- Columns two sites apart share one row only, so each site receives off-diagonal amplitude from at most one neighbour. By the same argument on rows, it sends to at most one.
- If x sends right and x+1 sends left, the pair is a closed 2×2 block.
- If x sends right and x+1 does not send left, orthogonality forces U(x+1,x+1)=0 and |U(x+1,x)|=1. Then x+1 must send right with modulus one, and this propagates around the ring as a shift.

Consequences of L1:
- Literal I4 flow at the possibility level is the conveyor. The departure site is refilled from behind and the arrival site's old content moves on, everywhere at once. A record carried this way moves deterministically.
- Genuine odds (I3) require pair mixing.
- At the record level, "flow, not swap" is the no-counterflow condition of Step 4.

**Minimal consistent object.** Candidate (a), "the excitation is the record", keeps the possibilities agreeing with the record at all times, so it reduces to R1 or R2. The smallest object where consistency is a real constraint and interference survives is candidate (b): the pair (X_t, ψ_t) in the one-excitation sector, which is R3. Steps 2–12 treat R3; R1 is recalled where it matters.

### Step 2: consistency is a transport problem (EXACT)

Set π_t(x,y) = P_t(x) T_t(x→y). This is a coupling with marginals P_t and P_{t+1}, supported on one-step pairs. Conversely, any such coupling gives a rule T = π/P_t. So a consistent rule exists at tick t exactly when a one-step coupling P_t → P_{t+1} exists.

### Step 3: existence holds exactly for strictly local ticks (EXACT)

**If the tick is range-1.** For any set Y, Π_Y U = Π_Y U Π_{N̄(Y)}. Hence
P_{t+1}(Y) = ‖Π_Y U Π_{N̄(Y)} ψ‖² ≤ ‖Π_{N̄(Y)} ψ‖² = P_t(N̄(Y)).
This is the Hall–Gale supply–demand condition, so a coupling exists. This holds for any d and any graph.

**If the tick reaches two sites.** Suppose Π_y U Π_x ≠ 0 with y ∉ N̄(x). The state right after a record forms at x (under Q1) has P_t = δ_x but P_{t+1}(y) > 0, so no one-step rule exists.

**Consequence.** U = exp(−iHτ) with nearest-neighbour H fails for all but isolated τ.

### Step 4: flow, continuity, and the minimal rule (EXACT)

- Every coupling has a net flow J = π − πᵀ obeying continuity: P_{t+1}(y) − P_t(y) = Σ_x J(x→y).
- Conversely, take any antisymmetric bond flow J obeying continuity and the outflow bound Σ_{y≠x} J⁺(x→y) ≤ P_t(x). Then T(x→y) = J⁺(x→y)/P_t(x), with T(x→x) set to the remainder, is consistent. Check: Σ_x P_t(x)T(x→y) = P_t(y) + Σ_x J(x→y) = P_{t+1}(y).
- Any coupling with net flow J has the form π = J⁺ + m, where m is a symmetric counterflow ≥ 0. The probability of moving, Σ|J| + 2Σm, is smallest exactly when m = 0. So J⁺/P is the unique minimal rule for a given J.
- The outflow bound is the new discrete-time ingredient. In continuous time it holds automatically for small steps.

### Step 5: the flow of one discrete tick (EXACT)

Define K(x,y) = ⟨ψ_{t+1}|Π_y U Π_x|ψ_t⟩, π_MH = Re K, and J_MH = π_MH − π_MHᵀ. Its properties:

1. Σ_y K = P_t(x) and Σ_x K = P_{t+1}(y), exactly.
2. π_MH = ⟨ψ|½{Π_x, U†Π_y U}|ψ⟩. It is supported on supp U and is local: the bond flow depends on ψ on {x−1, …, x+2}.
3. Any real quasi-joint αΠ_xU†Π_yU + βU†Π_yUΠ_x with the correct marginals for all ψ equals Re K + λ Im K.
4. The reversed tick has K^rev(y,x) = conj K(x,y). Requiring the film run backwards to retrace the same moves gives λ = 0.
5. For U = 1 − iτH + O(τ²), J_MH(x→y) = 2τ Im[ψ(y)* H_yx ψ(x)] + O(τ²). This is the continuous-time probability current (comparator).
6. Summed over a basis of states, J_MH across bond (x,x+1) equals ‖Π_{x+1}UΠ_x‖² − ‖Π_xUΠ_{x+1}‖² (Hilbert–Schmidt norms). This is the same at every cut, because the traced continuity equation is divergence-free. It is the tick's index: the I4 "standing conveyor" is exactly this traced flow.

### Step 6: all solutions (EXACT)

- The consistent rules at one tick form a polytope. Each point is a net flow (J₀ plus any divergence-free circulation) together with a counterflow per bond.
- Generic dimension = (number of independent loops) + (number of bonds). That is N+1 on a ring, N−1 on an open chain, and B−V+1+B in general.
- On a tree, the net flow is forced.
- Minimal rule: m = 0, with the flow chosen by the step's own flow or by L1-minimality.
  - On a ring, the L1-minimal circulation is c* ∈ −median{J₀}.
  - That choice is global, not local, and it cannot see a conveyor: for uniform odds it says "stay" (CHECKED).

### Step 7: one record on a line, the rule is always valid (EXACT)

Take a ring with N≥5 or Z, any d, and any strictly range-1 tick.

- Let a = Π_xψ and b = Π_{x+1}ψ. Write Ua = a₋+a₀+a₊ and Ub = b₀+b₊+b₊₊ (parts at successive sites).
- Cross terms from sites x−1 and x+2 vanish, because columns two apart overlap in one row and U is unitary. Using ⟨a₀,b₀⟩ + ⟨a₊,b₊⟩ = 0:
  J_MH(x→x+1) = ‖a₊‖² − ‖b₀‖² + 2Re⟨a₊,b₊⟩ = ⟨ψ|A_x|ψ⟩,
  where A_x = Π_x − Q U†Π_{x−1,x} U Q and Q = Π_x + Π_{x+1}.
- Therefore J_MH(x→x+1) ≤ P_t(x) and −J_MH(x→x+1) ≤ P_t(x+1).
- If both bonds carry odds away from x, the outflow is P_t(x) − P_{t+1}(x) ≤ P_t(x).

So T = J_MH⁺/P is valid for every state and every tick. CHECKED: the identity holds to 1.8e-15, and there were 0 violations in 2400 random ticks.

### Step 8: one record on a line, the rule is fixed by locality (EXACT)

- Suppose two local flow laws both satisfy continuity for all states. Their difference is divergence-free, so on a line it is one number c(ψ) on every bond.
- Locality forces c to be independent of the state (use three disjoint windows; with quadratic laws two suffice, so N≥8).
- A window with zero odds forces c = 0.
- So the net flow is J_MH, and flow-not-swap then fixes T = J_MH⁺/P.
- Without flow-not-swap, counterflow (swap) additions remain.
- Records guided this way ride a conveyor: +1 site per tick (CHECKED).

### Step 9: loops (plaquettes, Z², Z³)

- Lemma L1 and Step 7 fail on a 4-cycle, where two sites have two common neighbours. On random range-1 plaquette ticks:
  - the λ-flow is non-zero, up to 0.22 (CHECKED);
  - the minimal rule from Step 7 breaks the outflow bound in 68 of 570 ticks with d=1, excess up to 0.076 (CHECKED);
  - a valid coupling always exists (Step 3; LP 0 failures);
  - clipping the loop circulation into its feasible interval repairs every case (CHECKED).
- So locality + consistency + no counterflow do not fix the rule on loops. Time symmetry selects λ = 0 within the bilinear family (EXACT), but that choice can be invalid.
- Exception: coin–hop–coin walks, where each bond carries its own channel. There the λ-flow vanishes and no violations appeared in 600 ticks on a 2D torus (CHECKED; a proof is open).

### Step 10: covariance blocks motion with one possibility per site (EXACT)

- Suppose a tick on Z³ is homogeneous, number-conserving and strictly range-1. On one excitation it is U = Σ_v a_v S_v, and unitarity says Σ_v a_v z^v is a Laurent unit, so it is a single monomial.
- Proper cubic rotations make the six neighbour coefficients equal, which forces them to zero. So U = e^{iθ}·1: a single record never moves.
- Motion under I2 therefore needs one of: per-tick symmetry breaking (for example a cycling partition of pairs), multi-site cells, or non-conserving ticks. Each is a named conditional.

### Step 11 (Task 3): several records

- **Existence (EXACT).** Suppose a number-conserving tick reaches only nearest neighbours. Then U†N_R U lives on N̄(R), commutes with N_{N̄(R)}, and is ≤ m on the m-excitation sector of N̄(R). So ⟨C′|U|C⟩ ≠ 0 implies |C′∩R| ≤ |C∩N̄(R)|. By Hall's theorem, old records can be matched to new ones with each moving at most one site. Step 3 on configuration space then gives existence. Exclusion is built in.
- **A joint rule is needed (EXACT).** Take two bonds with one record each, Ψ = (|LL⟩ + e^{iφ}|RR⟩)/√2, and a Hadamard on each bond.
  - φ=0 and φ=π/2 give the same P_t and the same bond odds before and after.
  - But P_{t+1} = (½,0,0,½) for φ=0 and (¼,¼,¼,¼) for φ=π/2.
  - So no rule built from neighbourhood odds alone works.
- **The time-symmetric rule fails on configurations.** Applied jointly to the configuration, the minimal rule breaks the outflow bound on most ticks, because configuration space has loops (CHECKED).
- **A valid alternative (EXACT).** Settle the bonds one at a time; their gates commute. Each sub-step is a matching, so its rule is forced and valid. The result depends on the order (couplings differ by up to 0.07); averaging over orders is valid (CHECKED).
- **Collisions.** The configuration-level rule settles competing records by the relative configuration weights π(C,C′), so I3 holds in that sense (EXACT by construction). Under R1, joint formation odds settle collisions (EXACT).
- **I3 read literally fails.** Independent proposals with relative-odds collisions miss: joint TV up to 0.50, and per-record odds off by up to 0.12 after a single tick (CHECKED).

### Step 12 (Task 4): no-signalling

- Under R3, moves never act on the possibilities (EXACT).
- For every consistent rule, B's single-tick odds are independent of a distant setting at A (EXACT; CHECKED to 1.7e-15).
- B's individual move odds depend on A's setting, by up to 0.48 (CHECKED).
- B's two-tick history (b at t, b′ at t+1) depends on A's setting:

| Rule | Max change with A's setting |
|---|---|
| Minimal rule (where valid) | 0.23 |
| L1-minimal | 0.24 |
| Settle A's bond first | 0.32 |
| Settle B's bond first | 2e-16 |
| Average over orders | 0.16 |

- Two-tick no-signalling in both directions is achievable: an LP finds such a rule in 200/200 instances with the one-site limit binding. The rules that achieve it are "forgetful": a record is re-placed within its bond, ignoring where in the bond it was.
- Requiring each record's history to follow its own neighbourhood's minimal rule is impossible for linked possibilities (0/200), but works for unlinked ones (50/50) (CHECKED).
- Under R1, no-signalling is standard (EXACT).

### Step 13 (Task 5): fit with the Record axiom (ARGUED)

| Axiom text | Fit under moving records | What would need re-reading or rewording |
|---|---|---|
| "Records form." | Under R1, arrival is formation. Under R2/R3, arrival is a new way to come to a site. | R2/R3 need a sentence such as "a record may move to a neighbouring site" (candidate, not adopted). |
| "When present, a record locks exactly one admissible local possibility." | R1: holds every tick. R2: holds if carried into the arrival site's menu. R3: holds only at formation. | Under R3, "locks" becomes "names an admissible possibility of its current site". Arrival is automatically into the menu: T(x→y) > 0 implies P_{t+1}(y) > 0 (EXACT). |
| "A site never carries more than one record" | Compatible. One qubit per site gives doubles zero odds (EXACT). | None. |
| "records are permanent" | Fails if read as "a site keeps its record"; I2's site reuse contradicts that. | Read as "a record is never destroyed and may relocate". Candidate: "once formed, a record is never destroyed; it may move to a neighbouring site." |
| "Only records are readable … A site with no record cannot be read." | Fine if position is not content. | Under R3 the trail must not be readable (Step 12). |
| Admissibility reading note 2 | The move rule supplies site odds. | This is new law content; it must be named. |
| Campaign 7 sentence 2, "keeps locked possibilities" | Conflicts with R3 and R1. | Fits R2 only if "keeps" is read as "carries". |
| Q1 "change at once to agree" | Applies every step under R1, only at formation under R3. | Depends on the reading chosen. |
| Time as accumulation of records | Ticks with moves but no formation add no records. | Ticks need their own standing (I1). |

### Comparators (not adopted; cited from memory, not re-verified)

- **Bell 1984**, "Beables for QFT": continuous-time jumps at rate J⁺/P. Matches Step 5's continuum limit; one jump at a time, so no collisions or outflow issue.
- **Vink 1993**, Phys. Rev. A 48, 1808: Bell-type dynamics for general discrete beables and its continuum limit. The discrete-tick outflow issue and the 1D theorem above were derived independently.
- **Aaronson 2005**, Phys. Rev. A 71, 032325: discrete-time "flow theory", with existence via max-flow; this is the closest match to Step 3. His matrix-scaling rule is valid but not local.
- **Dürr–Goldstein–Tumulka–Zanghì**: "minimal" jump rates; matches Step 4.
- **Deotto–Ghirardi 1998; Bacciagaluppi–Dickson 1999**: guidance is non-unique (divergence-free additions); matches Steps 6 and 9.
- **Kirkwood/Dirac/Margenau–Hill**: the source of the Re K quasi-joint.
- **Meyer 1996**: scalar 1D homogeneous quantum cellular automata are trivial; compare L1 and Step 10.
- **Gross–Nesme–Vogts–Werner 2012**: the index as a flow across a cut, unchanged by continuous deformation; compare Step 5(6) and I4.
- **Mathematics:** Hall/Gale supply–demand theorem (max-flow/min-cut).

## 4. Checks

All scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A3/`, with all outputs in `outputs.txt`.

Run conditions: every run took ≤ 3 s and ≤ 185 MB peak, with `nice -n 10` and all four thread caps set to 1. Exact propagation was compared at tolerance 1e-12. An outflow violation was counted when the excess exceeded 1e-12. LPs used scipy HiGHS.

1. **`t1_brickwork_one_record.py`** — one qubit per site, ring N=8, Dirac-type brickwork ticks (one layer per tick), 40 ticks, three starting states.
   - J_MH equals the forced flow to ≤ 4.4e-16; exact propagation error ≤ 1.4e-15.
   - Monte Carlo with M = 2e5 trajectories: max TV ≤ 0.0036; worst per-tick χ² p ≥ 0.016 over 41 ticks.
   - Counterexamples (max TV against the odds): symmetric random moves 0.87; re-formation odds |U|² without the cut 0.87; "go where the next odds are high" 0.25.
2. **`t2_coinshift_nonuniqueness.py`** — Hadamard coin-shift, d=2, ring N=8.
   - The MH split itself, the minimal rule, and the L1 rule are all exact (≤ 3.9e-15).
   - Their two-tick statistics differ. Probability of moving per tick: 1.00 / 0.60 / 0.47. Mean signed displacement per tick: +0.435 / +0.435 / −0.054.
   - On a conveyor with uniform odds, MH rides at +1/tick while L1 never moves.
   - The traced flow equals the index (0, 1, 2) at every cut.
3. **`t3*`** — feasibility tests.
   - 2400 random range-1 d=2 ticks on a line: π_MH < 0 in 2092, but 0 outflow violations; a coupling existed in every case.
   - Bond identity (t3b): 1.8e-15.
   - 2D coin–hop–coin (t3b): 0/600 violations.
   - Plaquettes (t3c): 68/570 (d=1) and 20/570 (d=2) violations; λ-flow up to 0.22; every case repaired, exact to 1.2e-15.
4. **`t4_hamiltonian_tick.py`** — U = exp(−iHτ).
   - Least probability that must jump two or more sites from a just-formed record: 0.285, 0.027, 1.9e-3, 5.0e-5 and 3.1e-6 for τ = 1, 0.5, 0.25, 0.1 and 0.05, i.e. ≈ τ⁴/2.
   - Random states with no one-step coupling: 217/300 at τ=1; 8/300 at τ=0.25.
   - Spreading on a 201-site chain at ticks 10/20/40/80: guided (R3) variance 29.5 / 117 / 469 / 1875 (≈ 0.293 t²) versus re-formed (R1) 9.5 / 19.5 / 39.5 / 79.5 (≈ t).
5. **`t5*`** — two records, brickwork, 28 configurations.
   - Joint minimal rule invalid in 27/30 and 30/30 ticks (excess up to 0.042).
   - L1, sequential settling, and the order average all exact (≤ 6e-16); order dependence up to 0.071.
   - Monte Carlo of the order-averaged rule: TV ≤ 0.006. A χ² p of 1e-4 appeared once; it did not recur with three fresh seeds (min p = 0.044, 0.033, 0.0038).
   - Bond-local independent rule: TV 0.37 and 0.43.
   - Configuration-level λ-flow: 0.064.
6. **`t6_collisions.py`** — 3-site blocks, 2–3 records competing for sites.
   - Configuration-level L1 rule exact.
   - Joint minimal rule invalid on 11 to 24 of 24 ticks.
   - I3 read literally: accumulated TV 0.36–0.48; single-tick joint TV ≤ 0.50; single-tick per-record error ≤ 0.12.
7. **`t7*`** — no-signalling; numbers as in Step 12. The product-state sanity check (LOC feasible 50/50) passed.
8. **`t8`** — sampling of strictly range-1 scalar ticks for Lemma L1: every converged sample was a pair-mixing (148) or a shift (6).
9. **`t9`** — continuum limit: J_MH/τ approaches the current with error 1.45e-1, 1.46e-2, 1.46e-3 (O(τ)); the non-neighbour part of J_MH scales as O(τ³).

## 5. Real-physics match

1. **Single-time position statistics** are reproduced by construction. In the fine-tick limit the discrete flow becomes the standard probability current (EXACT within the toy).
2. **Light cone.** I2 plus consistency demands strictly local ticks, i.e. a hard maximal speed of one site per tick. Continuous local change leaks odds beyond it (≈ τ⁴/2 per tick from a just-formed record). If ticks are at lattice scale, the change must be cellular-automaton-like (ARGUED).
3. **Components.** A covariant tick with one possibility per site cannot move a record (EXACT). This is an analog of the known lattice need for spinor-like components (Meyer). The one-qubit staggered (brickwork) tick does give ballistic, Dirac-like spreading (CHECKED).
4. **Interference.** R3 keeps interference in the single-time odds; R1 loses it, and records diffuse.
   - In known physics, a particle whose position is recorded every step diffuses (R1-like), and which-path records destroy interference.
   - So R3 fits only if a moving record's trail is not itself a readable which-path record.
   - Falsifier: a readable trail combined with interference.
5. **Signalling.** Known physics forbids signalling.
   - Natural guided rules make two-tick histories depend on distant choices. This would be falsified if such histories were readable.
   - Rules that are safe for histories exist, but they are forgetful and not neighbourhood-local when possibilities are linked (CHECKED).
6. **I4 conveyor** (analog only). Equivariance cannot see a conveyor; only the step's own flow can. Guided records ride it at maximal speed. No such universal drift is seen for massive matter, so any conveyor would have to be confined to special sectors (ARGUED).

## 6. Open edges and next steps

1. **Loops in Z³.** Find a canonical, always-valid local rule on loops. Candidates:
   - per-plaquette circulation clipping (valid for disjoint loops, CHECKED);
   - covariant random-order settling;
   - sub-tick integration of continuous-time rates (needs a generator).

   Next toy: a 2×2×2 cell with cycling plaquette layers.
2. **Coin–hop–coin walks.** Prove a Z³ version of Step 7 for single-channel hops (conjecture, supported by 0/600 violations in 2D).
3. **Owner decisions:**
   - R1, R2 or R3;
   - whether a moving record's trail is readable;
   - the Record rewording candidates in Step 13.
4. **Multi-tick no-signalling.** Run an LP over ≥ 3 ticks. Conjecture: it is incompatible with neighbourhood-local odds when possibilities are linked.
5. **Formation and moves in the same tick (I1/I2).** A new formation's cut changes the possibilities that guide other records. Check consistency, including reuse of sites vacated in the same tick.
6. **Jammed regions (I5).** With exclusion a jammed region has no moves, so consistency needs its odds frozen. Test the Hall condition with exclusion at a jam boundary.
7. **Covariance and soldering.** Is a partition schedule cycling through axes and parities over 6 ticks acceptable under Admissibility's covariance and Q3's soldering?

## 7. Plain-language summary

If records may step to a neighbouring site each tick, the steps can be chosen so that, at every tick, where the records sit matches the odds the shared possibilities give. This works only if the possibilities themselves never spread more than one site per tick. The rule is simple: a record follows the net push of odds across each link, never against it. Along a single line this rule is the unique one built from nearby conditions that never sends odds both ways across a link, so it is pinned down. On the full grid, and when several records are linked, extra choices remain, and the simplest version sometimes asks a site to give away more than it holds. Linked records cannot each step by their own neighbourhood's odds: their steps must be chosen together, a step can depend on a choice made far away, and so a moving record's trail must not itself be readable. The other option is to treat every step as a fresh formation: that is always consistent and fully fixed, but then the possibilities stop reinforcing and cancelling from tick to tick, and records just wander.