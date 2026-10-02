I've read both lane reports in full, along with the axioms memo and the landed notes they lean on. No code was run and no files were written.

# Unification report: one owner clause for composition, the Born form and dynamics (Lane A × Lane G)

**Labels.** EXACT means a proof written here or in a cited note on origin/main. ARGUED means a reading or reasoning I have not verified.

**Sources read on origin/main:**
- `MINIMAL_AXIOMS_2026-06-29.md`, including the Qualification sentence "A state is a configuration of records."
- Dynamics-clause notes 9083 (recorded randomizer), 9084 (locality of marginals gives complete positivity), 9085 (compression update) and the 9061 synthesis.
- `RECORD_DYNAMICS_FINISHED_RECORD_CORRELATORS_…` (static and formation readings).
- `HOLES_AS_UNRECORDED_SITES_…`, `ORDER_BLIND_…` and 9046 (records-only admissibility).

**Hand re-checks of the lane steps I rely on (EXACT, no error found):**
- Lane A, Step 1: the steering formulas.
- Lane A, Step 3: s₊ = 1/λ and s₋ = 1 at r = c = √ρ, and (A) ⇒ H = tanh(γ artanh rc).
- Lane A, Steps 4–5: the ε-derivative.
- Lane A witness values: 4401/5425 and 7641/15625.
- Lane G: the A4 Lüders step and the B4 clique lemma.

**Readings of "determined by the nearest-neighbour conditions" used below:**
- R_pm: the law reads the neighbourhood's law-level state (Lane G's "possibility-map" reading).
- R_st: static reading. In the finished record law, a site's conditional given all other sites depends on its neighbours alone. This is the landed correlators note's reading.
- R_fo: formation (chain-rule) reading.
- R_ns (new here, not on main): no-signalling reading. A site's record distribution does not depend on formation choices made outside its neighbourhood at that moment (whether a record forms there, when, and on which menu).

---

## 1. Premise ledger, deduplicated

| Premise | Lane A | Lane G | Relation after dedup |
|---|---|---|---|
| Joint operator state on faithful site copies | inside C1 | S1 | S1 is the source |
| Ordinary tensor composite | C1 | output of Result A | delivered at non-adjacent pairs (§1.2) |
| Lock (ρ = PρP, permanent) | implied | L | implied by C2 |
| Normalised compression update | C2 | used inside A4 (Lüders) | shared premise |
| Law reads the site's M₂(C) part | C3 | R_pm (wider) | C3 is R_pm narrowed to one site |
| Pick coherence | C4 | — | R_ns at non-adjacent pairs, or a sentence |
| Unsoldered possibility covariance | Step 0 | B5 | one reading serves both |
| "varies with" read on the odds | removes the coin | B7 (J ≠ 0) | one reading serves both |
| Positive odds where the state allows | — | Reach / weighted branching | needed by Result A |
| Off-axis menus at both sites | inside C4's "every menu" | — | a menu-abundance premise |
| Continuous, homogeneous, reversible change | — | S2–S4 | clause |
| Local differential determination | — | A-diff | clause |
| Born-weighted ensembles | output | input to B1 (landed 9084) | fixes the derivation order |

### 1.1 Is C2 the same as L, or stronger?

- **EXACT: C2 implies L,** since P(PρP)P = PρP.
- **EXACT: L does not imply C2.** Two countermodels satisfy L at every stage and violate C2.
  - The landed replacement rule (9083). On a singlet, C2 gives |m⟩⟨m| ⊗ |−m⟩⟨−m|, while replacement gives |m⟩⟨m| ⊗ 1/2.
  - Noisy locks with Kraus operators |m⟩⟨φ_j| ⊗ 1. These steer the partner by E_m = Σ_j |φ_j⟩⟨φ_j|, which is not P_m.
- **Lane G's Result A does not run on L alone.** Its A4 step uses Lüders formation at x and at y, which is C2's normalised compression. So C2 is a premise both lanes share, and L follows from it.
- **Lemma U1 (EXACT).** Suppose formation branches are compressions (C2) and the non-selective formation map at y is linear (Lane G's "general local instrument" variant). Then the odds are Born.
  - Proof: write Φ(ρ) = Σ_± g_±(ρ) Q_±ρQ_±, with g_± = w_±/Tr(Q_±ρ).
  - Q₊Q₋ = 0, so linearity makes each corner map linear.
  - With at least one other site, Q₊ has rank ≥ 2, so Q₊ρQ₊ ranges over more than one dimension and g₊ is constant. Likewise for g₋.
  - Then w_± = c_± Tr(Q_±ρ), and normalisation forces c_± = 1.
  - On a lone qubit the corners are rank one, so there is no constraint. That is why composites are needed.
- **Consequence for the union:**
  - Lane G's general-instrument variant must be dropped, or Born enters through the word "instrument".
  - Lane G's A4′ and A2(c) use Σ_± P_±QP_±, the Born-weighted non-selective map. They become usable after Born is in hand.

### 1.2 Is C1 delivered by Result A?

- **EXACT at non-adjacent pairs.**
  - A4 (Lüders form) plus A5 (spanning) give [A_x, A_y] = 0 under C2 and positive odds.
  - Commuting unital copies of the central simple algebra M₂(C) generate M₂ ⊗ M₂. No generation premise is needed for a single pair.
  - Both site gradings fail at such a pair.
- **Adjacent pairs.** These need Reach (ARGUED, Lane G A5). There is an EXACT alternative after Born (§1.6, step 3).
- **Lemma U2 (EXACT, by inspection).** Lane A's Theorem 1 never uses adjacency.
  - Steps 0–5 use the two-site reduced pure state, the partner's menu, the probe, covariance, and the same law at both sites.
  - So Theorem 1 runs verbatim at a non-adjacent pair, where Result A supplies C1 exactly.
- **Entangled states.**
  - EXACT: the Schmidt family lies in the state space of M₂ ⊗ M₂.
  - EXACT native realization: σ·σ = 2 SWAP − 1, so e^{−iJτσ·σ}|01⟩ = e^{iJτ}(cos 2Jτ |01⟩ − i sin 2Jτ |10⟩). The reduced Bloch length is |cos 4Jτ|, covering [0, 1].
  - This answers Lane A's open item for an isolated pair. With recorded neighbours, the field components along the excitation axis must be equal on both sites (ARGUED).
  - Non-adjacent example (EXACT, from §3.3): on the 4-ring singlet, recording site 4 as ↓ leaves sites 1–2–3 in a W-type state with down-weights (1/6, 2/3, 1/6). Sites 1 and 3 are non-adjacent and entangled.

### 1.3 Is C3 implied by S1 plus the text?

- **EXACT: S1 supplies the object C3 reads.** Restricting a state on B to A_x gives a state on M₂(C).
- **EXACT: the reading itself is independent of S1 plus the text.**
  - Countermodel: F = ½[1 + (s_x + ε Σ_{y~x} s_y)·p / (1 + 6ε)].
  - It is covariant, normalised, bounded and nearest-neighbour, and it reads the neighbours' parts directly, so it violates C3.
- **ARGUED: inside the clause, C3 is the natural division of labour.** Neighbours act through the change between records and through the menu; the odds read the site's own part. Lane G's B7 vector-sum fingerprint uses C3 implicitly.
- **R_pm is forced on any clause world.** Landed 9046 shows that records-only conditions make forming sites isolated and non-interacting. Lane A's sequential formation at two entangled unrecorded sites lies outside the records-only reading for the same reason.

### 1.4 Is C4 implied by S1 plus the text?

- **EXACT: no, not at an adjacent pair, under any reading.**
  - Setup: the path C–B–A, with ψ_AB a pure Schmidt state, C recorded, and B's menu along C's record axis. Take the cubic law with any mixed extension.
  - C1–C3 hold.
  - Nearest-neighbour determination holds under all three readings:
    - R_pm: A's odds are a function of ρ_A.
    - R_fo: A's chain-rule conditional is F(n_b), a function of B's record.
    - R_st: given B's record b, A's conditional does not depend on C's record c.
  - C4 fails: Lane A's 4401/5425 against 7641/15625.
  - The reason: B's menu reaches A through B's record content, which is itself a nearest-neighbour condition. Lane A's grounding ("B's menu is distance-2 data") does not go through.
- **EXACT given R_ns: yes, at a non-adjacent pair (A, C).**
  - Whether C forms, and on which menu, are formation choices outside A's neighbourhood.
  - R_ns then requires that "C does not form" and "C forms on menu m, averaged over its own odds" give A the same odds, for every m. That is C4 verbatim.
  - With Lemma U2, Theorem 1 needs no pick-coherence sentence beyond R_ns.
- **EXACT: with a linear instrument (Lemma U1 setting), C4 is automatic, but Born is already built in.** So this is not a route.
- **ARGUED: R_ns is a reading of "determined by".** A function of the neighbourhood data does not move when nothing in the neighbourhood moves. It is not recorded on main.

### 1.5 Hidden shared premises

- **"Every menu" is a menu-abundance premise (EXACT).**
  - If B's menus are aligned with its own state axis (c = ±1), the family H(r, t) = g(r)h(t) passes every C4 instance, for any odd h with h(1) = 1 and any g. A's averaged odds equal ½ + g(r)h(p_z)/2, which are A's own odds.
  - So Theorem 1 needs off-axis menus at both sites. That is the same kind of price the landed menu-independence note records.
  - C4's "for every menu" carries this premise. Lane A lists abundance (P3) as not axiom content for its R2 route, but its R1 sentence audit does not list it separately.
- **The coin survives unless "varies with" is read on the odds (EXACT).** The constant coin with a field-aligned menu rule satisfies every premise in the union. Its distribution ½δ_m + ½δ_{−m} still moves with the neighbours through m. Lane G's B7 J ≠ 0 argument rests on the same odds reading.
- **Positive odds where the state allows.** Result A needs this before the law is known. Born and the coin (Theorem 1's two survivors) both satisfy it. Laws with zero odds on allowed possibilities, such as step laws, die in Lane A's Step 5 anyway (ARGUED that this costs nothing).

### 1.6 New result: Theorem 1′ for aligned menus on three sites (EXACT)

**Setting.**
- C1 on three sites, C2, C3, covariance, and C4 for the pair (A, C) with B unrecorded. A and C may be non-adjacent.
- All menus are aligned with the excitation axis.
- States: Ψ = α|100⟩ + β|010⟩ + γ|001⟩, with a = |α|², c = |γ|² and a + c ≤ 1.
- u(p) denotes the odds of outcome "1" at a site whose part has excitation probability p.

**Steps.**
1. Antipodal normalisation plus a π rotation about x give u(1 − p) = 1 − u(p).
2. By C2: C records 1 with odds u(c), leaving A pure 0. C records 0 with odds 1 − u(c), leaving A with excitation probability a/(1 − c).
3. C4 then reads: u(a) = u(c)u(0) + (1 − u(c)) u(a/(1 − c)).
4. Setting a = 1 − c and using step 1 gives u(0)(1 − 2u(c)) = 0. So either u(0) = 0 (repeat certainty) or u ≡ ½ (the coin).
5. With u(0) = 0, put x = a/(1 − c) and y = 1 − c. Then u(xy) = u(x)u(y) on (0, 1].
   - A zero at some x₀ in (0, 1) would spread: u(x₀^{1/n}) = 0 for all n, so u ≡ 0 on (0, 1). That contradicts u(½) = ½.
   - φ(t) = −log u(e^{−t}) is additive and non-negative, hence linear, so u(x) = x^γ.
   - u(½) = ½ gives γ = 1.

**Conclusion.** u(p) = p, that is F(s; ±ŝ) = (1 ± |s|)/2 on pure and mixed states, or the coin. This uses no off-axis menus and no regularity assumption.

**Witness values at a = c = 1/3 (hand arithmetic):**

| Law | Left side u(a) | Right side |
|---|---|---|
| Born | 1/3 | (2/3)(1/2) = 1/3 |
| u = p² | 1/9 | (8/9)(1/4) = 2/9 |
| Cubic (h = t³) | 13/27 | (14/27)(1/2) = 7/27 |

**Use.** In aligned worlds, the law's off-axis values are never evaluated, and Theorem 1′ fixes every value that is. Theorem 1 covers the off-axis values when off-axis menus occur.

**Derivation order (EXACT as a dependency audit):**
1. S1 + C2 + positive odds + spanning → commuting site algebras at non-adjacent pairs, hence C1 there.
2. C1 + C2 + C3 + covariance + R_ns (or sentence 3 below) → Theorem 1 (off-axis menus) and Theorem 1′ (aligned menus) → Born or the coin. Reading "varies with" on the odds leaves Born, with affinity and repeat certainty as outputs.
3. Born + equal-time no-signalling for adjacent pairs (all-pairs form of sentence 3) → via A4′, Σ_± P_±QP_± = Q, so [P, Q] = 0. Adding generation gives B ≅ ⊗M₂ (landed `GENERATED_FINITE_COMPOSITION_MINIMALITY`).
4. Born-weighted steering ensembles + sentence 3 at record-enclosed regions + the complete-positivity extension → linear completely positive evolution (landed 9084). Then S4 → unitary, S2–S3 → e^{−iHτ}, A-diff → nearest-neighbour two-site form, covariance → Heisenberg with no one-site field.
   - Ensemble richness, region autonomy and the complete-positivity extension stay ARGUED.

There is no circularity, provided Result A uses the Lüders form of A4 (Lemma U1).

---

## 2. One clause, and what it leaves supplied

> **Between records, the unrecorded sites hold one joint possibility, built from their site domains alone; it changes continuously, reversibly and the same way at every moment, and the change at each site is set by its nearest neighbours. A forming record takes its odds from its own site's part of that joint possibility, with some odds for every possibility that part does not exclude; when it forms, it cuts the joint possibility down to the part in which its site holds the locked possibility. Taken over its own odds, a forming record changes no other site's odds except through the change between records.**

**Mapping:**

| Clause phrase | Premise supplied |
|---|---|
| "hold one joint possibility, built from their site domains alone" | S1 plus generation |
| "continuously, reversibly … the same way at every moment" | S2, S4, S3 |
| "the change at each site is set by its nearest neighbours" | A-diff |
| "takes its odds from its own site's part" | C3 |
| "some odds for every possibility that part does not exclude" | positive odds |
| "cuts … down to the part …" | C2, hence L; excludes replacement and noisy locks; deliberately not "instrument" (Lemma U1) |
| Sentence 3 | C4 for every pair at equal time; 9084's no-signalling premise at record-enclosed regions (region autonomy ARGUED) |

**Variants:**
- **V1 (narrower).** "…changes the odds of no site outside its neighbourhood except through…". This is R_ns written down. Born still follows by Lemma U2, but adjacent commutation then needs Reach (ARGUED).
- **V0.** Drop sentence 3 and record R_ns as the reading of "determined by". The consequences are those of V1.

**Wording (EXACT, text).** The Qualification says "A state is a configuration of records." Lane G's "joint possibility state" collides with that definition, so the clause uses "joint possibility".

**What remains supplied:**
- **Preparation.** Three EXACT constraints:
  - 1/2^N, combined with record projectors, is invariant under every compressed generator P_R H P_R and under every cut at an unrecorded site, and covariance gives odds F(0; ·) = ½. In that world every record is a fair coin for every H, every schedule and every covariant law. Neither the Born form nor J is visible.
  - A product preparation invariant under global SU(2) is 1/2^N. So a preparation that privileges no possibility, in a world whose odds vary, must be correlated.
  - Lane G's B7 ("J ≠ 0 is forced") holds for product preparations with non-zero Bloch vectors. Under 1/2^N, no value of J makes the odds vary.
- **Formation site, rate and schedule,** including the ratio γ/J.
- **The menu rule (EXACT):**
  - Aligned-only menus exercise u(p) and nothing else.
  - State-aligned menus admit H = g(r)h(t).
  - Off-axis Born needs Lane A's abundance, or the reading that sentence 3 binds the law on its whole domain (ARGUED).
- **Sign of J (EXACT).**
  - Θ^{⊗N} is antiunitary with ΘKΘ⁻¹ = K. It maps the J-history from ρ₀ to the −J-history from Θρ₀Θ⁻¹ with every lock flipped, and Born odds are Θ-covariant.
  - So sign J is a convention exactly when the preparation rule commutes with this transport.
  - It does not for ground-state preparations: Θ preserves eigenspaces of K, and the two finished laws in §3.3 differ.
- **|J|,** which sets the unit.
- **Soldering.** Both lanes use unsoldered covariance. Under full soldering, K/J and D/J stay free (landed 9040), and Theorem 1's soldered form is open.
- **Reach** for adjacent pairs (needed under V1 or V0).
- **9084's remaining premises:** the complete-positivity extension, ensemble richness and region autonomy (ARGUED).
- **The reading of "varies with"** (odds against menu), which decides whether the coin is excluded.

---

## 3. Consistency between the lanes

### 3.1 The union is consistent (EXACT)

- Quantum mechanics with Heisenberg H, Lüders cuts and Born odds satisfies every sentence. The non-selective cut at B leaves ρ_A unchanged, and Born odds are affine.
- The coin also satisfies every sentence.

### 3.2 Lane A's grounding of C4 does not go through (EXACT, §1.4)

The distance-2 argument treats a pick-averaged frequency as if it were a per-condition distribution.

### 3.3 Lane G's §5(b), worked by hand in the equal-time, z-menu limit (EXACT, rational)

**Mechanism (conservation).**
- Global SU(2) makes H conserve S^tot.
- A cut on an n̂-menu commutes with S_n̂^tot.
- With records on ±n̂, the compressed generator is a field along n̂ plus Heisenberg terms.
- So S_n̂^tot is conserved through the whole formation process, and finished records on a definite-S_n̂^tot preparation have a fixed sum.

**Three preparations:**
- **(a) 1/2^N.** Records are independent fair coins, so the cross-ratio test passes (Lane G's outcome A), but the test is vacuous (§2).
- **(b) J > 0, 4-ring ground state.**
  - The bond sum is (S₁ + S₃)·(S₂ + S₄) = ½[S² − S_A² − S_B²]. Its unique minimum is S_A = S_B = 1, S = 0, with state (|1,−1⟩ − |0,0⟩ + |−1,1⟩)/√3.
  - Probabilities: P(↑↓↑↓) = P(↓↑↓↑) = 1/3, and each of the four mixed configurations has 1/12.
  - Given a₂ = ↑ and a₄ = ↓, site 1's odds of ↑ go from 1 to 0 as the non-neighbour site 3 flips. The cross-ratio is 1/144 against 0. The static reading fails.
- **(c) J < 0, symmetric ground multiplet.**
  - The covariant state is Π_sym/(N+1) = ∫dn |n⟩⟨n|^{⊗N} (Schur's lemma).
  - Its z-record law gives P(configuration with k ups) = k!(N−k)!/(N+1)!.
  - So P(a₁ = ↑ | all others) = (j+1)/(N+1), where j counts ups among all other sites (Laplace's rule).
  - On the 4-ring the conditional moves from 2/5 to 3/5 as site 3 flips. This state is separable, so the failure comes from global correlation, not entanglement.

**What this means for §5(b):**
- At finite formation rate with z-menus, the fixed-sum constraint holds at every γ for (b) (EXACT). Positivity of the two slice entries at finite γ is ARGUED generic.
- So Lane G's expected outcome (B) is confirmed in this limit, and the variable that matters is the preparation, not γ.
- With covariant field-aligned menus seeded by a covariant first cut, every later field stays along ±n̂ until some site's field cancels. On such schedules the process is the rotated z-process (EXACT). The zero-field fallback is the open case.

### 3.4 The precise tension

- **Non-adjacent pairs.** Admissibility grounds C4 here (R_ns), and Theorems 1 and 1′ run here. But a correlated non-adjacent pair, once recorded, creates dependence on a non-neighbour, which the static reading forbids.
  - EXACT example: a non-adjacent singlet with non-orthogonal menus gives P(a = +p | c = ±m) = (1 ∓ p·m)/2. Section 3.3 gives two more.
- **Adjacent pairs.** C4 is compatible with the static reading, but no reading of Admissibility supplies it.
- **So both lanes stand or fall on one reading fork:**
  - Under R_st: the clause is excluded for the natural covariant preparations, the 1/2^N world hides everything, and C4 has no ground in the text. Both lanes fail together.
  - Under R_pm with R_ns: everything goes through, and the static failure is an expected property rather than a defect. Retiring R_st does not obviously reopen the landed all-pairs exclusion, because that note also excludes the law under the formation reading (ARGUED).
- **Menu side.**
  - "B's menu is distance-2 data" is true at both pair types. It is harmless at adjacent pairs and is not what grounds C4; what grounds C4 is the partner lying outside A's neighbourhood.
  - Field-aligned menus make the world aligned. Born then rests on Theorem 1′, and off-axis Born is never exercised there.

---

## 4. Decision-point statement (draft for a program note)

**Decision point (owner; not adopted): one composition-and-dynamics clause.** [Clause from §2.]

Adopting it also records the reading of "determined by the nearest-neighbour conditions" as R_pm with R_ns, and retires the static reading of the finished record law in clause worlds.

**Derived under the clause (conditional on the listed premises):**
- **Ordinary tensor composition,** with both site gradings excluded. EXACT at non-adjacent pairs; at adjacent pairs, EXACT via sentence 3 plus Born.
- **The Born form** F(s; p) = (1 + s·p)/2 on pure and mixed states, with affinity and repeat certainty as outputs.
  - EXACT by Theorem 1 (off-axis menus, given Lane A's abundance) and Theorem 1′ (aligned menus).
  - The coin survives unless "varies with" is read on the odds.
- **Dynamics:** e^{−iHτ}, nearest-neighbour two-site form, Heisenberg with no one-site field, and |J| as the unit. EXACT given 9084's premises, which become dischargeable once Born is an output (ARGUED).
- **Exclusions and compatibility:**
  - Replacement and noisy-lock updates are excluded.
  - Equal-time order-blindness becomes compatible with odds that vary, in contrast to the landed records-only constancy.
- **The program's three decision points** (composition law, Born affinity plus repeat certainty, dynamics generator) become this one decision.

**Not derived:**
- the preparation (subject to the EXACT constraints in §2);
- formation site, rate and schedule;
- the menu rule;
- the sign of J;
- soldering;
- the complete-positivity extension and ensemble richness;
- Reach (under V1 or V0);
- any physical identification.

**Cheapest exact checks:**
1. **Exact-rational runner, under 1 s.**
   - Lane A §5 as specified.
   - Theorem 1′ residuals: zero for Born and the coin; non-zero for u = p² (2/9 against 1/9) and the aligned cubic (7/27 against 13/27).
   - The identity u(0)(1 − 2u(c)) = 0.
   - Lemma U1 on 4×4 rational states.
   - The family H = g(r)h(t) passing every C4 instance with c = ±1.
2. **sympy, under 1 min.**
   - Lane G §5(a) as specified.
   - Invariance of 1/2^N (with record projectors) under P_R H P_R and under cuts.
   - The C4 countermodel on the path C–B–A.
   - The Schmidt family r = |cos 4Jτ|.
3. **Exact rational, 16 dimensions.**
   - The equal-time §5(b) values: 1/3 and 1/12 with 1 against 0; Laplace's rule with 2/5 against 3/5; and the vacuous pass under 1/2^N.
   - Optional: Gibbs preparations with rational x = e^{−βJ}.
4. **FLOAT on 4- and 6-site rings (the decisive remaining computation).**
   - Lane G §5(b) at γ ∈ {0.1, 1, 10} with the resolvent average, for preparations (b) and (c).
   - First on z-menus (expect B at every γ; check that both slice entries stay positive).
   - Then on field-aligned menus, with the coherent-state instrument for the first record and as the zero-field fallback.

**What each outcome means:**
- **Checks 1–3 as stated:** record the clause package as an EXACT conditional theorem.
- **Any law that is neither Born nor the coin but has zero residual** in (A), (B) or Theorem 1′: the corresponding step is wrong; stop and redo it.
- **Outcome (B) for both preparations at every γ:** retiring the static reading is a condition of adopting the clause.
- **Outcome (A) for some covariant, non-trivial preparation with covariant menus:** the static reading survives in that corner. C4 at adjacent pairs must then come from the all-pairs sentence 3.

---

## 10-line summary

1. [EXACT] Lane A's C2 is strictly stronger than Lane G's L (the replacement rule and noisy locks satisfy L but not C2). Lane G's A4 already uses Lüders formation, so C2 is shared and L follows from it.
2. [EXACT] Lemma U1: a linear non-selective formation map with compression branches forces Born odds. Lane G's "general instrument" variant would build Born in, so the clause must say "cuts down", not "instrument".
3. [EXACT] Lane A's Theorem 1 never uses adjacency. Run at a non-adjacent pair, it needs C1 where Result A delivers it exactly. The Heisenberg bond gives the Schmidt family r = |cos 4Jτ| from |01⟩.
4. [EXACT] C3's object is supplied by S1, but the reading is independent (covariant countermodel). C4 is implied by no reading of nearest-neighbour determination at an adjacent pair (cubic countermodel), so Lane A's "distance-2 menu" grounding does not go through.
5. [EXACT given R_ns, a reading I introduce; ARGUED] At non-adjacent pairs, the no-signalling reading of "determined by" gives C4 verbatim.
6. [EXACT, new] Theorem 1′: with aligned menus on three-site one-excitation states, C2 + C3 + C4 give u(p) = p or the coin, with no off-axis menus and no regularity. Theorem 1 itself needs off-axis menu abundance: state-aligned menus admit H = g(r)h(t).
7. [EXACT] Lane G's §5(b) as specified is vacuous: under 1/2^N every record is a fair coin for every H and every law. Covariant ground-state preparations fail the static test by conservation: 1 against 0 for J > 0, and Laplace's 2/5 against 3/5 for J < 0.
8. [EXACT/ARGUED] The tension, stated precisely: C4 is grounded where the static reading fails, and is ungrounded where it holds. So both lanes stand together under the possibility-map plus no-signalling readings and fall together under the static reading.
9. [ARGUED] One three-sentence clause supplies everything both derivations need, collapsing composition, Born, and generator into one decision plus a reading fork. Still supplied:
   - the preparation (covariant plus "varies with" forces it to be correlated, EXACT);
   - formation site and rate;
   - the menu rule;
   - the sign of J (a convention exactly when the preparation rule is Θ-transported);
   - soldering;
   - Reach, the complete-positivity extension and ensemble richness;
   - the odds reading of "varies with", which decides the coin.
10. Next checks: an exact-rational runner (Lane A §5 plus Theorem 1′ and Lemma U1); the sympy lemma certificate; the exact 4-ring laws; then the one FLOAT computation, §5(b) at finite γ with ground-state preparations and field-aligned menus.