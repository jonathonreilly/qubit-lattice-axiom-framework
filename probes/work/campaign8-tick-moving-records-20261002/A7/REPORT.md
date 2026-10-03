The report follows.

# Lane A7 report: can moving records with readable positions be consistent, local and non-signalling?

## 1. Question

Assume I2 and I3. Every record's position is readable at every tick, so a record's positions over several ticks have a joint law (the history). Can one moving-record rule satisfy all four of these at once?
- **(C)** At every tick, the odds of each record configuration equal the possibilities' odds.
- **(L)** Each record's move odds depend only on a bounded neighbourhood.
- **(NS)** The joint law of a region's record positions over several ticks does not depend on a distant choice of tick operator.
- **(I)** Moves do not cut the possibilities (reading R3, not R1).

Sub-questions:
- Does C + NS hold without L?
- Do C + L + NS force R1, or some intermediate?
- What must the owner decide?

## 2. Answer

**No, not in general. EXACT, in a supplied two-record toy.**
- If L means "each record's own move odds use only local data", L already implies NS for every multi-tick history (EXACT). So the obstruction is not about locality.
- **Main result.** The obstruction appears as soon as one linked record's earlier position is *registered* at a later tick. The one-site limit does this by itself when a tick carries that record's two branches more than one site apart.
- From then on, readable positions plus uncut linked possibilities force signalling under every rule, local or not, Markov or not.
- **Minimal case.** A linked pair on two bonds, one binary choice of tick operator at A, two ticks. Every rule with the right odds makes B's own two-tick record history depend on A's choice by total variation at least √2 − 1 ≈ 0.414 (EXACT, a triangle inequality). The LP attains this bound.
- So C + NS without L fails, and C + L + NS + I fails with it.

Two narrower regimes behave differently:
- **No position ever registered** (each record confined to one bond): a correlated "forgetful" re-draw satisfies all four (EXACT). Here L means local move odds only. Rules whose moves are independent given the full past fail C by CHSH = 2√2 (EXACT).
- **A partner's motion carries memory but no distant choice exists:** C + NS can hold while C + L fails (EXACT).

Keeping C + NS with readable positions works when every step re-forms the record with the cut (R1, EXACT). It fails for the uncut reading and for every uniform partial cut tested (CHECKED). So in this toy, readable "records move" amounts to "records re-form at a neighbouring site each tick".

## 3. Derivation

### Setup (supplied toy, not framework content)

- **Possibilities:** one qubit per site, in the sector with one excitation per region. The regions A and B are far apart, with one record in each. "Linked" means not a product.
- **Ticks:** ψ_{k+1} = (U_A ⊗ U_B) ψ_k, with strictly range-1, excitation-conserving gates. Each side may choose its gate (a "setting").
- **Odds:** P_k(a,b) = |ψ_k(a,b)|².
- **Rule:** for each setting sequence σ, a law Q_σ on histories X_0, …, X_K, with X_k = (a_k, b_k).
- **(H) Readable histories:** positions at different ticks share one probability space. This is the coordinator's reading of "a state is a configuration of records".
- **I2 has two variants:**
  - lattice moves: to any neighbour;
  - flow moves: only along links the tick uses.

  All the main results hold for both.
- **Gate notation:** R(θ) = [[cos θ, −sin θ], [sin θ, cos θ]] acting on a pair of sites.

### Step 1 (Task 1): multi-tick no-signalling, formalised

**NS_K.** For setting sequences that differ only in A's settings, the laws of (b_0, …, b_K) coincide; likewise with A and B swapped. K stays inside the light cone (one site per tick, plus the rule's radius).
- Single-tick NS follows from C automatically (lane M). NS_K for K ≥ 1 is new content.
- CAUS means no retro-causation. None of the no-go results below need it.

**Two strengths of L:**
- **L_ind (Bell's local causality).** Given the full past, the two moves are independent, and each move uses only its own neighbourhood and its own settings.
- **L_odds.** Given the full past, each record's marginal move odds depend only on:
  - its own position, and optionally its own past positions;
  - its own settings;
  - its neighbourhood's local part of the possibilities.

  Under L_odds, the two moves may be jointly correlated.

**Lemma 1 (EXACT).** L_odds ⇒ NS_K.
- Sum out a_K, then a_{K−1}, and so on. This gives Q(b_0..b_K) = P_0^B(b_0) Π_k T_B(b_{k+1} | b_{≤k}; B-local data).
- U_A ⊗ U_B never changes B's local part of the possibilities, so the right-hand side ignores A's settings.
- So with L read as L_odds, NS adds nothing, and the question becomes C + L + I. Lane M's two-tick signalling (up to 0.32) therefore always came from move odds that depended on distant positions.

### Step 2: moves that are independent given the past fail C (EXACT)

- Take a Bell pair on two bonds. A rotates by α ∈ {0, π/4}; B rotates by β ∈ {±π/8}.
- The CHSH value of the record positions after one tick is 2√2 (checked: 2.828427124746).
- Under L_ind, the joint move factorises given any past λ, so CHSH ≤ 2. This holds even when λ includes both records' full histories.
- So C + L_ind is impossible for linked possibilities, with or without memory. From here on, L means L_odds.

### Step 3 (Task 3, positive case): a rule that satisfies all four when no position is ever registered (EXACT)

**Condition.** For every record, each site of its next-tick support lies within one step of each site of its current support. A record confined to a bond is the example.

**The correlated forgetful re-draw.** Draw the whole next configuration from P_{t+1}, independent of the current configuration.
- **C:** holds by construction.
- **L_odds:** each record's move odds are its own next-tick odds, computed from its local part of the possibilities and its own tick.
- **NS:** by Lemma 1.
- **I:** nothing is cut.

Checks:
- Deviation 3.3e-16 over 3 ticks × 4 setting pairs.
- LPs feasible for 1, 2 and 3 ticks.
- Some memory is allowed: max P(B stays) = 3/2 − 1/√2 ≈ 0.793 under C + L_odds at the CHSH settings (CHECKED).

**Structure.** This is "re-formation without the cut". Each tick the record is re-placed by its formation odds, but the possibilities are not cut. The link between the two re-draws is the same kind of outcome link that Q1 gives linked formations; independent local moves cannot produce it (Step 2).

### Step 4: local move odds fail once a partner's motion carries memory

**Lemma 4 (EXACT).** Suppose a label c of B's position is conserved by every C-consistent one-site rule during tick k, so that c(b_{k+1}) = g(c(b_k)). Examples:
- B's pair, under flow moves with a pair-mixing tick;
- B's whole position, when B's transport is forced.

Then every Markov rule whose A-move odds ignore B's position satisfies Σ_a P_k(a, c=γ) T_A(a→a') = P_{k+1}(a', c=g(γ)) for every γ with P_k(c=γ) > 0. One kernel T_A must therefore transport A's odds conditioned on each γ separately. This is overdetermined whenever those conditioned possibilities differ in phase.

**Example (EXACT, no choices needed).**
- A is a bond. B is a ring Z_5 with the conveyor (shift) tick.
- ψ_0 = (|+⟩|0⟩ + |−⟩|1⟩)/√2, and A applies H.
- B's transport is forced (b' = b+1), even with lattice moves.
- A must go to L when b = 0 and to R when b = 1, yet its odds are (½, ½) in both cases. So A's move odds must use B's position.
- LP: C + NS feasible; C + Markov-L infeasible (1 and 2 ticks).

**Plaquette pairs** (4-cycles with alternating pairings, random linked states; CHECKED):
- Markov-L infeasible in 5/5 instances (flow moves) and 12/12 (lattice moves, 2 ticks).
- C + NS feasible in all 17.

**Lane M's 4-site, two-bond geometry** (CHECKED). A general local rule (any local odds, not just lane M's minimal rule) is infeasible for 0/50 linked instances and feasible for 50/50 unlinked ones; C + NS is feasible for 50/50. This strengthens lane M's 0/200.

**With own-past memory** the first tick after linking is identical (EXACT). Later ticks can be rescued only if the record's own past already carries the partner's label (ARGUED).

### Step 5: the one-site limit registers positions (EXACT)

Suppose record X's odds sit on {p, q}, and a tick maps them by a permutation to {p', q'} with dist(p', q) ≥ 2. Then every C-consistent one-site rule has x_{t+1} = p′ if and only if x_t = p:
- mass at p' can only come from p;
- P_{t+1}(p') = P_t(p).

No new record is needed. A travelling record's later position remembers its earlier one.

### Step 6: main result — readable histories plus uncut linked possibilities force signalling (EXACT)

**Instance.** A has sites −1, 0, 1; B has sites 0, 1; the two regions are far apart (embeddable in Z³).
- Possibilities: ψ_0 = (|0⟩_A|0⟩_B + |1⟩_A|1⟩_B)/√2.
- **Tick 0:** A applies R(θ) to its bond; θ ∈ {θ_0, θ_1} is A's choice. B is idle.
- **Tick 1:** A applies R(π/2) to its pair (−1, 0), which moves its site-0 possibility to −1; site 1 is idle. B applies R(φ) to its bond.

All ticks are strictly range-1, and nothing crosses between the regions.

**Argument:**
1. **Odds.** ψ_1(a,b) = R(θ)_{ab}/√2, so P(b_1 ≠ a_1) = sin²θ. Write α for A's branch at tick 2 (0 if a_2 = −1, 1 if a_2 = 1). Then P(b_2 ≠ α) = sin²(θ − φ).
2. **Registration.** By Step 5, α = a_1 for every rule.
3. **Triangle inequality** on the single probability space of the history (H): |P(b_1≠a_1) − P(b_2≠a_1)| ≤ P(b_1≠b_2) ≤ P(b_1≠a_1) + P(b_2≠a_1).
4. **Choices.** Take 0 < φ < π/2, θ_0 = φ/2 and θ_1 = φ/2 + π/4.
   - For θ_0: P(b_1≠b_2) ≤ 1 − cos φ.
   - For θ_1: P(b_1≠b_2) ≥ sin φ.
   - So B's own two-tick record law moves with A's choice by total variation ≥ sin φ + cos φ − 1 > 0.
   - At φ = π/4, with θ ∈ {π/8, 3π/8}, the bound is √2 − 1 ≈ 0.414. The interval for P(b_1≠b_2) is [0, 0.293] for θ_0 and [0.707, 1] for θ_1.

**What the proof uses.** Only H, C at ticks 1 and 2 with the uncut odds, and A's one-site limit. It does not use L, Markov, CAUS, or which move set is chosen.

**Checks.**
- The LP minimum over all rules equals sin φ + cos φ − 1 at φ = π/12, π/6, π/4, π/3 and 5π/12.
- At φ = π/4 the summed difference is 2(√2 − 1) = 0.828427, with a verified dual certificate (Aᵀy ≤ 1.8e-15).
- A three-tick variant gives the same value.
- **Control:** without A's split, the minimum is 0 and the forgetful re-draw works. Registration is the trigger.

**Narrow claim (EXACT).** The scope is:
- one excitation per region and one possibility per site;
- products of range-1 gates;
- supplied, non-covariant tick schedules (lane M's Step 10: covariant ticks cannot move a single record at all);
- this instance and its angle variants.

It does not say every linked state or tick sequence forces signalling (Step 7).

### Step 7: how often signalling is forced in random instances (CHECKED)

Three ticks, A's ticks fixed, B choosing at two ticks. "Forced" means minimal summed difference > 1e-4 (dual simplex).

| Ensemble | Moves | Forced | Max summed difference |
|---|---|---|---|
| Plaquettes, complex gates | flow | 8/400 | 0.156 |
| Plaquettes, real gates | flow | 106/400 | 0.544 |
| Same 20 real plaquette instances | lattice | 0/20 | — (9/20 with flow moves) |
| Rings Z_6, start on a bond | lattice | 5/60 | 0.391 |
| Rings Z_6, start on a bond | flow | 6/60 | 0.467 |

- On a 4-cycle, a record reaches 3 of the 4 sites in one step, so forgetting is nearly free under lattice moves.
- Best ring instance, certified: ≥ 0.389. With a single choice by B, still ≥ 0.280 (total variation 0.140), certificate verified.
- All 17 two-tick random plaquette instances were NS-feasible: the 4-cycle registers positions only weakly.

### Step 8 (Task 4): what restores no-signalling

**(a) Cut the reading record (EXACT).** Cut B to agree with b_1 (R1 for B). Then:
- P(b_2 ≠ b_1) = sin²φ for both choices, so B's history law ignores θ;
- C (with the cut odds), L and NS all hold;
- if every record is cut each tick, the possibilities stay unlinked, and each record follows a local chain with kernel |U(y,x)|².

**(b) Cut the partner instead (EXACT): no help.** A's cut commutes with A's split and with B's tick, so the joint odds of (α, b_2) do not change.

**(c) Partial cuts (CHECKED).** Replace B's possibilities by (1−λ)ρ + λ Σ_b Π_b ρ Π_b. In the triangle family, some choices still force a gap for every λ < 1:

| λ | Forced gap |
|---|---|
| 0.5 | 0.118 |
| 0.9 | 5.0e-3 |
| 0.99 | 5.0e-5 |
| 0.999 | 5.0e-7 |

Near λ = 1 the gap is about (1 − λ)²/2.

**(d) The forgetful rule of Step 3 is not R1, but it breaks** once a linked partner's position is registered (Step 6 control).

**Conclusion.** "Cutting at every move without changing odds" is exactly the Lüders cut: it never changes the current odds, only later ones. That is R1. In this toy, keeping C + NS with readable positions requires the reading record to be fully cut at each readable tick: uncut fails (EXACT) and uniform partial cuts fail (CHECKED). Extending this to all records is ARGUED.

A cut that removes only the links while keeping local odds would also restore NS. But it agrees with no record and is nonlinear, so it is not a cut of Q1's kind (ARGUED).

### Step 9: interference and the conveyor under R1

- **Interference (EXACT).** A record's position becomes the classical chain with kernel |U(y,x)|², so interference between its branches across ticks is gone. On a brickwork tick it diffuses (lane M, CHECKED: variance 79.5 vs 1875 at tick 80).
- **Conveyor (EXACT).** Under R1, a record's net flow across a cut, averaged over a uniform record distribution, equals the tick's index (it is the same sum Σ|U(y,x)|² over crossing pairs). By lane M's Lemma L1, with one possibility per site this is 0 (symmetric pair hopping) or ±1 (shift). On the conveyor a record moves exactly one site per tick.
- **What survives (ARGUED).** The index-carrying step is a property of the tick, so it survives as record drift. What is lost for readable moving records is the interference-built part of the chirality line. Unrecorded possibilities are not cut by moves, so their interference and flow remain.

### Step 10 (Task 5): fit with the axioms (ARGUED)

There are two consistent options and one inconsistent middle:
- **(A) Readable every tick.** Each step is a formation with the Q1 cut (R1). "Records are permanent" then has to mean "never destroyed; may re-form at a neighbour" (as lane M noted). I3 holds literally, because move odds are formation odds.
- **(B) Readable only when a new formation registers the position.** That formation cuts. Between registrations the possibilities do the moving (R3) and interference survives. "A state is a configuration of records" must then not make interim positions readable.
- **Middle (readable every tick, uncut).** Inconsistent with NS once anything registers a linked partner's position (Step 6). Operationally: any register of B's earlier position that is itself a new formation cuts B under Q1, and that disarms the signal (Step 8a). So the middle signals only if record positions are readable without any cut.

### Comparators (not adopted; cited from memory, not re-verified)

- Wigner 1970, the triangle form of Bell's inequality (the form used in Step 6).
- Bell 1964 and CHSH 1969 (Step 2); the √2 − 1 optimum matches the Tsirelson-type bound.
- Leggett–Garg 1985 and Fritz 2010 (temporal CHSH): Step 6 is a hybrid of a two-time and a two-party scenario.
- Bell 1984 (beables) and Valentini 2002 (signal-locality): trajectories with quantum odds at each time allow signalling if they are accessible.
- Jarrett 1984: L_odds corresponds to parameter independence.
- Lüders 1951 (the cut); Misra–Sudarshan 1977 (Zeno); Gross–Nesme–Vogts–Werner 2012 (index).

## 4. Checks

All scripts are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A7/`. Outputs are in `outputs.txt`, and `run_quick.sh` reruns the cheap set.

| Script | What it tests | Result |
|---|---|---|
| `mtlp.py` | Shared LP builders: history LP (C, CAUS, NS) and per-tick Markov-L LP; dual certificates | — |
| `e1_conveyor_bond.py` | Step 4 example | C+NS feasible; Markov-L infeasible (1 and 2 ticks) |
| `e2_bond_bond.py` | Step 2 and Step 3 | CHSH 2.828427; Markov-L and NS feasible for 1–3 ticks; forgetful rule exact to 3.3e-16; max stay 0.792893 |
| `e3_plaquettes.py` | Random plaquettes, Markov-L vs NS | Numbers as in Step 4 |
| `e4`–`e8` | First forced instance (min 4.7e-3) and its dissection | Needs B to choose at two ticks; CAUS not needed |
| `e9`, `e10` | Random scans | Numbers as in Step 7 |
| `e11`, `e12` | Best ring instance | Certified bounds ≥ 0.389 and ≥ 0.280 |
| `e13`, `e14` | Search over angles that are multiples of π/8, then greedy simplification | Led to the Step 6 instance (Bell-pair starts forced in 288/2500) |
| `e15`, `e17`, `e18`, `e20` | Triangle instance: analytic odds, LP, certificates, general φ | Matches sin φ + cos φ − 1 |
| `e16` | Partial-cut scan | Step 8c |
| `e19` | Lane M's geometry | Step 4 numbers |

Solver notes:
- HiGHS default tolerances are 1e-7.
- Born constraints are soft with weight 1e4, to absorb 1e-16 rounding; the measured Born slack is ≤ 2e-15, with one run at −9.8e-8.
- Interior-point objectives can be off by about 2e-3 because of that weight. Certified values come from dual-simplex duals checked with numpy (Aᵀy ≤ 1.8e-15, |y| ≤ w).

Run conditions:
- Every run used `nice -n 10` with all four thread caps set to 1, and finished in under 60 s (max 53 s).
- Peak memory was under 300 MB for every run except one exploratory run: `e3`, 3 ticks with 64 setting sequences, peaked at **461 MB**, which broke the cap. It was not repeated; smaller runs replaced it.

## 5. Real-physics match

1. **No-signalling.** Known physics forbids signalling. Step 6 says readable trajectories with uncut odds would signal. So a real-physics match needs (A) or (B); (A) reproduces the standard statistics for repeated position readouts (comparator).
2. **Interference.** Under (A), readable moving records cannot interfere across ticks. Electrons, neutrons and large molecules do interfere, so such excitations cannot be readable moving records each tick. Option (B) fits them. Macroscopic readable tracks behave like (A) (ARGUED).
3. **Conveyor drift.** Under R1, an index-carrying conveyor gives records a steady drift. No universal drift of massive matter is seen, so any conveyor must be confined to special sectors (ARGUED, as in lane M).
4. **Fine ticks.** If ticks were fine compared with continuous change, R1 would freeze records (Zeno, comparator). Lane M already requires cellular-automaton-like ticks (ARGUED).
5. **Falsifiers:**
   - any local record history that depends on a distant choice;
   - interference of an object whose path is readable at every step.

## 6. Open edges and next steps

1. **Scope.** Extend to n records, internal components, loops in Z³, and covariant cycling schedules.
2. **Memory without choices.** Can a record's own past positions rescue L when no distant choices exist?
3. **Partial cuts.** Test partial cuts outside the triangle family, and a formal statement about link-only cuts.
4. **Option (B) as a model.** Build it formally: records re-form only at registrations. Check C, L and NS together with I1 ticks and I3 collisions.
5. **Owner decision.** Readable every tick (then each step re-forms with the cut) or readable only at registrations? A candidate wording, not adopted: "A record's position is readable at a tick only when a formation fixes it there; then the shared possibilities change at once to agree with it." This also needs the Record ("permanent") and Qualification readings settled.
6. **Longer rings, 4+ ticks.** Measure how the forced fraction grows with spreading. The scripts are ready; these runs may need more than 300 MB, so they were not run.

## 7. Plain-language summary

Suppose a moving record's place could be read at every tick while the shared possibilities underneath carried on unchanged. Then a choice made far away would show up in the pattern of another record's places over two ticks: a signal faster than one site per tick. A tiny exact example shows this with two linked pairs of sites, one far-away choice and two ticks. That choice changes how often the pattern turns up by at least 41 times in 100, and in that example no move rule avoids it.

Things work when every step is treated as a fresh formation, so that the shared possibilities change at once to agree with the record each tick. The odds stay right, the steps stay local, and nothing far away can be learned from a record's path. The cost is that a moving record no longer gets its possibilities reinforcing and cancelling between ticks, so it wanders instead of spreading cleanly, although a built-in push along a line still carries it one site per tick.

The owner therefore needs to decide whether a moving record's place is readable at every tick (then each step is a re-formation), or only when something new forms to register it (then, between registrations, it is the possibilities that move, not a readable record).