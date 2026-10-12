# C5 R2-5: the arrow of time in the state (is set B compatible with Record?)

**Worker.** Claude Opus 5.5 (same family as O1–O5, the supervisor and the other round-2 probes). **Unrefereed.** Run 2026-10-12, 11:53Z to about 12:45Z. No repository file was edited.
**Scratch.** `scratchpad/C5/R2-5/`: nine scripts `r25_*.py`, each with its `.out` (list at the end).
**Read in full.** `docs/MINIMAL_AXIOMS_2026-06-29.md`; `TESTS.md:2302-2643` (C5 method, round-1 results, round-2 pre-registration); `agents/C5_O5_synthesis.md`; `SUMMARY.md` §§15–21; `PRICE_NOTE.md` §5 and the v6 delta; `agents/C5_O1_report.md` §§2–5; `agents/C5_O1_referee.md`; `agents/C5_O4_referee.md`.
**Prior art read (counted once each, §6).** `docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md`; `docs/POST_RECORD_ARROW_ORIENTATION_FIREWALL_2026-06-06.md`; `docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md`; `docs/RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md`; block 93 (`docs/ADMISSIBILITY_RULE_COVARIANCE_FORCES_A_REVERSIBLE_FORMATION_LAW_…_2026-09-23.md`); owner memory notes "formation reading is the axiom" (09-18, a directive on meaning) and "record count rises until frozen" (09-28, an owner's thought, not a rule).

**Labels.** PROVED (a proof is given here); CHECKED (a script reproduces it); SUGGESTED (argued); RECALLED (literature from memory, not fetched); reading (an interpretation). Same-family, unrefereed throughout.

---

## 0. Verdict against the FIXED readings (`TESTS.md:2607-2610`)

**SUGGESTED.** Neither DERIVED nor REFUTED is met.

- **Not DERIVED.** Under reflection positivity (RP, which set B needs for real time: `C5_O5_synthesis.md:356`; `C5_O1_report.md:224`), I found the arrow in the state with (i) and (iii) bounded, but (ii) only as "un-formation probability ≤ δ", not "never". Records that keep forming up to the present need one law number tuned to about 1e-61 or smaller (§3.5). Several general statements rest on checked classes, not proofs.
- **Not REFUTED.** I have no proof that "form" or "permanent" forces a law-level orientation. Two explicit counterexamples to that claim:
  - **P2.** Hard tagged records (§3.4). Strictly permanent and forming, with no law-level arrow, but not reflection positive.
  - **P3.** Soft tagged records (§3.5). Reflection positive, with permanence holding with probability 1 − δ.
- **What is refuted, bounded.** Take the strict reading of (ii): records never un-form, yet they keep forming after the boundary. Under RP and time-reflection covariance, no law does this:
  - PROVED for slices with no time-odd content (Lemma T′);
  - PROVED for strictly persistent time-odd records (Lemma RP-odd);
  - CHECKED exhaustively for every hard single-site law on six alphabets of up to 6 values (§3.3).

  This is a no-go, so it needs the codex referee before it is recorded (`TESTS.md:2451`).
- **Against the expectation** ("SUGGESTED for the block reading, with a real risk of REFUTED", `TESTS.md:2611`): matched, but sharper. Strict permanence fails in every RP class checked. Permanence with probability 1 − δ survives, at the cost of a tuning.

---

## 1. In plain words

- Set B makes time a fourth grid direction, equivalent to the other three. Its rules then cannot say which way time runs (Lemma E). The only place left for the arrow is how the universe starts: few records at one end.
- **First result: permanence cannot be a rule.** If the rule itself forbade a record from vanishing, the backwards-symmetric rule would equally forbid records from appearing. So "permanent" can only be a fact about our particular history, not a law. This is a one-line proof.
- **Second result: a symmetric rule does give an arrow from a low-record start.**
  - Records pile up going away from the start. Put the empty boundary at the other end and the arrow reverses, exactly.
  - In the toy, far from the boundary, formation and un-formation balance (u/f = 1.000). The arrow lasts only a few correlation times.
- **Third result: "never vanishes" plus "still forming" fails under reflection positivity.** Reflection positivity is the property set B needs to recover real time. Every reflection-positive rule I could check fails here.
  - Records that carry their own "this way is forward" tag can do it.
  - But exactly those rules break reflection positivity.
- **Fourth result: "almost never vanishes" plus "still forming today" works only with a tuning.** Here "almost never" means the chance that any record in the observable universe ever vanishes is below δ. It is possible with tagged records and reflection positivity. But one number in the rule, how much a record outweighs a blank per step, must be tuned to the formation rate: at most about 1e-61 to keep records forming for 8e60 Planck times.
  - In a static 4D law, a record's weight accumulates over its whole future. So the time at which a record forms is set by that tiny imbalance.
  - Untagged records with all four directions equivalent cannot do even this in the toy. Whatever makes a record cheap to keep in time also makes it cheap to spread sideways.
- **Lorentz violation from the state is harmless if records are sparse.** At the refereed O4 record budget it is about 1e-67 × coupling, against bounds of 1e-19. It is of natural size if records fill space (a miss of 3e16).
- **What this means for Record.** In set B, "permanent" survives only as "permanent with overwhelming probability, given a low-record start". "Records form", read as still happening today, costs a tuning. Both are prices on the Record text, not free readings.
- **A tension the owner should see.** The owner's 09-18 directive says the formation (process) reading *is* the axiom, and the static joint law is only a comparator. Set B's block reading uses the static Z⁴ joint law as the meaning of Record. That is an owner decision, not something a calculation settles.

---

## 2. Hypotheses (stated before titles) and outside realizations excluded

- **H-B (set B).** Z⁴, whole-law B4⁺ covariance including the record sector (`C5_O5_synthesis.md:355`, price B2), and time reflection θ (pre-registered). PROVED and CHECKED (`r25_b4.out`): B4⁺ already contains 24 proper elements with g e₀ = −e₀, for example diag(−1,−1,1,1) and −1. So for records whose "present/absent" predicate is unchanged by those rotations, B4⁺ alone supplies the time reversal that the lemmas use.
- **H-RE (what a record is: the block reading).** Records are values of the realized Z⁴ configuration: a site, i.e. a Z⁴ event, is blank or carries one locked value. The realized configuration is a sample of a Gibbs state of the law's specification.
  - A **formation event** is (blank at (x,t), record at (x,t+1)) along the axis the state's arrow selects.
  - An **un-formation event** is the reverse.
- **H-T.** The law couples only nearest neighbours in the time direction, i.e. it is a transfer matrix between time slices, and θ acts slice-wise. Used for Lemma T′, Lemma RP-odd and the exhaustive search.
- **H-RP.** Bond reflection positivity across time planes. For classical slice algebras this is: M(a′, b) = T(θa′, b) is positive semidefinite (PSD).
- **H-state.** A low-record boundary at t = 0 and no future boundary (the top is free). For tagged records, add: no records reaching spatial infinity (§3.4).
- **O-rec (observational, added; not in (i)–(iii) as registered).** Records of the Record axiom still form at the present epoch, about N = 8.07e60 Planck times after any low-record boundary (`r25_numbers.out:1`). The record rarity budget is O4's refereed ≤ 5.3e-11 s⁻¹ per nucleon (`TESTS.md:2410`), used here as an illustrative upper rate.
- **(ii) is read two ways.**
  - (ii-s), strict: never.
  - (ii-δ): with probability ≥ 1 − δ over the whole history, like (i).

**Outside realizations that this scope excludes.**
- **(R-Q).** Records as real-time events of the Osterwalder–Schrader (OS) reconstructed quantum theory. This covers emergent decoherence records, real-time flash/collapse laws, and the time-symmetric collapse formulation (Bedingham–Maroney 2017, RECALLED). In this reading the Euclidean configuration is not a history (§5).
- Laws that are not nearest-neighbour in time, for the RP results beyond the exhaustive single-site search.
- Multi-site slices with mixed time-odd companions (only single-site alphabets were exhausted).
- Quantum (non-commuting) slice algebras: the RP arguments use a classical twisted kernel.
- Two-time (initial plus final) boundary conditions.
- Records whose *definition* carries an orientation. That is a law-level arrow, so Lemma E applies.

---

## 3. Results

### 3.1 (a) The time-oriented words of the axioms (`MINIMAL_AXIOMS_2026-06-29.md`)

| Word / clause | Where | Time-symmetric block reading | Status |
|---|---|---|---|
| "Records form." | `:77` | (1) **Existence:** the record set is non-empty. This is time-symmetric and empty of process content. (2) **Located formation:** a record's *tail* is the end opposite its own tag. This is covariant, and the state supplies which end is the past (P2, P3). With orientation-free records, formation and un-formation are θ-images of each other and a symmetric law cannot tell them apart (Lemma T). | Reading. (2) exists **only if records carry time-odd content** |
| "When present, a record locks exactly one admissible local possibility" | `:79` | "Where present": at a record-bearing event, its content is one admissible possibility | Time-symmetric. Reading |
| "locks" | `:79` | "Fixes the content at that event" is time-symmetric. "Prevents later change" is permanence (below) | Reading |
| "A site never carries more than one record" | `:79-80` | Under B1 (sites are Z⁴ events): at most one record per event, which is trivially symmetric. Under a Z³-site reading it would constrain a whole worldline and needs a time axis | Reading |
| "records are permanent" | `:80` | (P-1) Per event, no meta-time: vacuous, symmetric, carries no persistence. (P-2) Persist along +t: a law-level arrow, so Lemma E gives V₁ ≠ 0, class I. (P-3) Persist along the t-axis either way: a law-level axis, S₂ = 2 (count (e) and Lemma A, `C5_O1_report.md:86,96`), so not B4⁺. (P-4) Persist along the record's own tag: covariant and symmetric in law. That is P2 (strict, not RP) or P3 (RP, probability 1 − δ) | (P-1) is empty; (P-2) and (P-3) are excluded in B; (P-4) is the only non-empty one |
| "Only records are readable … determined by record content alone … cannot be read" | `:82-83` | Readout is a function of content. No time word | Time-symmetric |
| "A state is a configuration of records" | `:92` | The state is the 4D record configuration, i.e. the whole history. "The arrow in the state" then means this configuration has a low-record boundary | Reading. It is consistent with "A law privileges no states" (`:94`): the boundary is realized data, not privileged by the law |
| Admissibility: "determined by … the nearest-neighbor conditions" | `:60-61` | On Z⁴ the neighbours include the *future* neighbour x + e₀. Each site's odds then depend on its future (the teleology of §3.5) | Reading. Compare `:67-69`: the distribution is "conditional on formation at that site" |
| Open gates: "arrow, record-production dynamics, physical persistence dynamics, time metric" | `:185` | The axioms deliberately leave the arrow outside. "Permanent" is a constraint, not a persistence dynamics | Text |

**Answer to (a).** Every word has a time-symmetric block reading. But for "form" and "permanent", the only readings with content need records to carry time-odd content: a tag that marks which end is the tail. The orientation-free block readings are vacuous: "form" becomes existence, and "permanent" becomes per-event.

### 3.2 Lemma T: permanence cannot be law-level (PROVED)

**Statement.** Let a specification γ be invariant under a time-reversing symmetry θ, and let the record predicate be θ-even. Suppose γ forbids the un-formation pattern (record at t, blank at t+1 at site x) in every context. Then γ forbids the formation pattern in every context.

**Proof.** θ maps each allowed (or forbidden) local pattern, with its context, to an allowed (or forbidden) one. Reflecting about t + ½ maps formation (0 then 1) at x to un-formation (1 then 0). □

**Soft version (PROVED; CHECKED in `r25_lemmaT.out` (b)).** For a θ-symmetric transfer matrix, the half-line Doob kernel is reversible with respect to π = ψ²: detailed-balance defect ≤ 5.6e-16 over 2000 random laws. So K(1→0) = 0 forces K(0→1) = 0 wherever π > 0.

**Consequence for set B.** Under whole-law B4⁺, Lemma T applies to every orientation-free record (H-B). Permanence must therefore be a property of the realized state. So in this sense "permanent" cannot itself impose a law-level arrow. If it is made law-level, it forbids formation.

### 3.3 Strict permanence with ongoing formation under RP: a bounded no-go (needs the codex referee)

**Lemma T′ (PROVED under H-T, for slices with no time-odd content: θ acts trivially on slices).**
- θ-covariance gives T(a,b) = T(θb,θa) = T(b,a), so T is symmetric.
- Suppose a formation step c → d (c blank at x, d with a record at x) has positive probability in a half-line Gibbs state. Then d is reachable and c can be continued.
- So T(d,c) = T(c,d) > 0. The un-formation step d → c then has positive probability: its Doob kernel is K(d,c) ∝ T(d,c)β(c) > 0.
- Hence strict state-level permanence fails. □

**Exhaustive check of hard column laws (CHECKED, `r25_lemmaT.out`).** I took every θ-symmetric hard column law of window range 3 and 4: 44 and 688 laws with an allowed column. Among the 24 and 352 laws with bulk formation, **0** have zero bulk un-formation.

**Lemma RP-odd (PROVED under H-T and H-RP).**
- Let a slice a carry a time-odd record value r (θr ≠ r) that strictly persists with the *same* value, so T(a, θa) = 0.
- Then M(θa, θa) = T(a, θa) = 0. A PSD matrix with a zero diagonal entry has that whole row zero, so T(a, ·) ≡ 0. Slice a has no successor.
- So strictly persistent time-odd records cannot occur in the bulk of an RP law. □
- **CHECKED instance.** The P2 tag rule's twisted kernel has eigenvalue −0.892 (`r25_rp.out`).

**Exhaustive search (CHECKED, `r25_rp_search2.out`).** I enumerated every θ-covariant, bond-RP, hard single-site law on six alphabets:
- S1 {b, r};
- S2 {b, U, D};
- S3 {b±, r±};
- S4 {b0, b±, r±};
- S5 {b0, r0, U, D};
- S6 {b0, r0, b±, r±}.

These give 5, 15, 52, 203, 52 and 877 RP laws. The count of laws with strict permanence and formation **after t = 0** is **0** in every alphabet.

Strict permanence occurs only with **boundary-only** formation (6, 12 and 88 pairs of law and boundary in S3, S4 and S6). There the blank boundary value has no predecessor and its θ-image has no successor. Everything forms at the first step and then freezes. That is the frozen universe, which O-rec excludes.

**Control without RP.** With θ-covariance only, ongoing formation with strict permanence does occur: 4 cases in S2 and 4224 in S4. The P2-type label rule is one of them. So RP is what removes it.

**Scope.** Proved for two subclasses; exhaustive only for single-site hard alphabets. Multi-site slices with mixed time-odd companions and quantum slices are open. General statement: SUGGESTED.

### 3.4 P2: strict permanence with no law-level arrow, but not RP (CHECKED)

**The rule.**
- Records carry a tag d ∈ {±e_μ}.
- Hard rule: a record tagged d at y requires a record with the same tag at y + d.
- The rule has range 1, is covariant (B4⁺ acts transitively on the 8 tags) and is θ-invariant (θ swaps U and D).
- The state: a blank past, blank spatial infinity and a free future.

**Results (`r25_labels_open.out`).**
- P(no record ever un-forms) = 1.000000000000 exactly.
- Formation times are geometric: median t₅₀ = 15 at w = 1.05, against ln 2 / ln w = 14.2.
- For w < 1, formation is pushed to the free end: density 0.0000 at T/2 and 0.9 at T.
- With a periodic ring (`r25_labels.out`), sideways-tagged records wrap around and un-form in time at 0.006–0.11 per site-step for each sideways tag, and P(no un-formation) falls to 1e-8–0.33. U-tagged records still never un-form. So the state must also exclude records at spatial infinity.

**The cost.** Not RP (§3.3): there is no OS reconstruction of real time, so B3 fails.

### 3.5 P3: tagged, soft, RP; permanence with probability 1 − δ and a tuned balance (CHECKED in 1+1 single column; 3+1 SUGGESTED)

**The time-bond weights** (`r25_soft_labels.py:1-20`).
- B→U = f (a tail) and D→B = f (its θ-image).
- U→B = B→D = e₁ (un-formation).
- U→D = e (two heads meeting).
- D→U = x (two tails meeting).
- U→U = D→D = B→B = 1.

These are θ-covariant. With f = r, e = u/r, e₁ = u and x = (1+η)/e, the twisted kernel has det = η(1 − ru) > 0, so it is PSD. CHECKED eigenvalues: all ≥ 0.

**Covariance in 1+1.**
- Among {B, U, D}, the spatial-bond weights are rotation images of the time weights among {B, L, R}, which are all 1. So the columns decouple.
- Rows B, R and L of the twisted kernel are identical, so PSD reduces to the 3×3 case.
- Sideways segments need two spatial ends, weight r·u per segment.
- Infinite sideways lines are excluded by the state; this exclusion is SUGGESTED stable inside a Hubble-sized region.

**Untuned, the records fill everything at the first step** (`r25_soft_labels.out`: m(1) = 0.51). RP forces x·e ≥ 1, so the record sector grows by λ_UD = 1 + √(xe) ≥ 2 per step.

**With a θ-even on-site record weight w_rec = (1+κ)/λ_UD** (RP-neutral), `r25_soft_labels_tuned.out` gives:
- the formation rate per blank site-step ≈ κ (9.9e-3 at κ = 1e-2; 9.8e-4 at κ = 1e-3);
- un-formation per record-step ≈ u·r/κ (9.8e-11 and 1.0e-9, with u = 1e-9 and r = 1e-3);
- at κ = 0, formation spreads uniformly up to the free end;
- for κ < 0, formation is suppressed and un-formation grows (1.4e-7).

**Teleology (CHECKED in three toys; SUGGESTED in general).**
- In a static Z⁴ law, a permanent record's weight accumulates over its whole future.
- So the formation time is geometric, with rate κ = log of the per-step weight advantage of a record over a blank.
- The toys: h in the column (`r25_tradeoff.out`: ξ = 1/h exactly, K(0→1) ≈ h); ln w in P2; ln(w_rec λ_UD) in P3.

**What O-rec needs.** At least κ ≲ 1/N = 1.2e-61. For uniform formation together with (iii), κ ≲ 3e-78 (§3.7). In P3 this is a cancellation between O(1) numbers (w_rec·λ_UD = 1 + κ), i.e. a tuning. In P2 the balance w = 1 is a normalization choice, but P2 is not RP.

### 3.6 (b) The registered toy: 1+1 Euclidean, time-reflection-symmetric, low-record boundary, no future boundary (CHECKED, `r25_toy_gibbs.out`, `r25_tradeoff.out`)

The model has s ∈ {0,1} with a weight factor ε per disagreeing bond and a field h. In the isotropic case, ε is the same on space and time bonds (the square-group analogue of B4⁺). Rows are exact transfer matrices with L = 1–10, T = 60–400.

- **An arrow from the boundary alone: yes.**
  - Blank bottom: f(0..3) = 0.269, 0.284, 0.197, 0.121 and u(0..3) = 0, 0.008, 0.009, 0.010.
  - Blank top: the exact mirror (residual 6.9e-17).
  - Blank at both ends: f(t) = u(T−1−t) to 2.8e-17, and total net formation 5.6e-17.
  - No oriented coupling exists anywhere in the model.
- **The bulk carries no arrow.** At t = T/2, u/f = 1.000 (to three decimals) in 32 of the 40 isotropic rows. The 8 exceptions (0.71–0.999) are the h = 0.01 rows plus (h, ε) = (0.1, 0.01) at L = 6. In those, the arrow has not finished by T/2.
- **Arrow length.** t₉₀ is 1–6 steps except at the smallest field, h = 0.01, where it reaches 17–29 steps. In those long-arrow rows:
  - for ε ≥ 0.3, permanence fails badly: P(no un-formation in the box) is 7e-3 to 3e-14;
  - for ε = 0.1, almost nothing forms: m(T/2) = 0.003 at L = 6 and 0.0002 at L = 8.
- **The trade-off (isotropic).** The maximum t₉₀ on the 14×14 grid shrinks as the cap on un-formation tightens:

  | Lattice | u_bulk ≤ 1e-2 | ≤ 1e-4 | ≤ 1e-6 | ≤ 1e-8 |
  |---|---|---|---|---|
  | L = 6 | 30 | 18 | 10 | 1 |
  | L = 8 | 25 | 8 | 8 | 1 |

  Over L = 2→10 the arrow *shortens*: t₉₀ falls from 46 to 21 at ε = 0.1, h = 0.01. For L ≥ 4, ξ = 1/(L·h) exactly (25, 16.67, 12.5, 10.0).
- **Anisotropic column** (no spatial coupling, i.e. a law-level preferred axis, S₂ = 2). Arrow length (1/h) and un-formation (ε²/h) are independent: ξ = 1/h exactly; K(1→0) = 9.95e-9 against c²/(b−a) = 1.005e-8.
- **Plain reading.** With orientation-free records and all directions equivalent, whatever keeps a record in time also makes it spread sideways. A sparse, still-forming, almost-permanent record set needs either a preferred axis in the law or tagged records (P3).
- **Scope.** CHECKED for L ≤ 10 in 1+1. The 3+1 statement is SUGGESTED.
- **Supporting argument.** For a scalar pair law, an isolated record worldline has per-step weight g = (φ₁/φ₀)(W₁₀/W₀₀)^{2(d−1)}(W₁₁/W₀₀). Making g ≈ 1 with W₁₀ = ε ≪ 1 needs ln(φ₁/φ₀) ≈ 2(d−1) ln(1/ε). Compact domains then gain about ε^{−2(d−1)V}, so the blank phase is unstable.

### 3.7 (c) Induced Lorentz violation (`r25_numbers.out`; arithmetic CHECKED, formulas RECALLED where marked)

| Source of anisotropy in the state | Size | Against F1 (c_γ − c_e < 2.66e-19) | Against (iii) literal: ρ/M_Pl⁴ |
|---|---|---|---|
| Gravitational strength, cosmological state | ρ_crit/M_Pl⁴ = 1.7e-123 (1.1e-120 reduced); ρ_CMB/M_Pl⁴ = 9.0e-128 | passes | equal by definition |
| Standard-model medium, photon in the CMB (Euler–Heisenberg, δv = −(44/135)α²ρ_γ/m_e⁴; RECALLED formula) | 5.1e-43 | passes | **exceeds** by about 85 decades |
| Electron thermal mass in the CMB, ~αT²/E² (RECALLED order) | 4e-28 (1 GeV) to 2e-40 (1.4 PeV) | passes | exceeds |
| Sparse tagged records (P2/P3), linear response g × (records per site), at the O4 budget | g × 3.2e-67 (Earth matter); g × 2.4e-98 (cosmic mean) | passes by ≥ 48 decades | exceeds in Earth matter (3.2e-69 at g = 1e-2, against a bar of 1.1e-93) |
| Uniform formation at rate κ, density κN | needs κ ≤ F1/(gN) ≈ 3e-78 for g = 1e-2 | conditional | – |
| A gentle arrow's gradient, a∂ln n ~ 1/N | 1.2e-61 (linear); 1.5e-122 (quadratic); b-type ~ M_Pl/N = 1.5e-33 eV | passes | linear exceeds; quadratic is about at the bar (1.7e-123) |
| Records filling space (tag condensate O(1)), coupled at F2's natural size | 8.55e-3 | **misses by 3.2e16** (needs ≤ 3.1e-17) | fails |

**Readings.**
- **(iii) as literally registered is stricter than ordinary physics.** The Standard Model in the CMB already exceeds ρ/M_Pl⁴ by 85 decades. So I report (iii) against F1.
- **The pre-registered side condition holds.** In P2 and P3 the law has only B4⁺-invariant couplings (tag–matter terms such as d^μd^νT_μν), so there is "no natural-size u^μ operator in the law" (`TESTS.md:2599`). The u^μ appears only through the state's tag density.
- That the LV is linear in the density is SUGGESTED (dilute linear response).

### 3.8 Requirements in numbers for permanence with probability 1 − δ (`r25_numbers.out`, last two lines)

- With 1e80 baryons and 2.3e7 records per nucleon at the O4 budget, there are N_rec = 2.3e87 records.
- (ii-δ) then needs un-formation ≤ δ·5.4e-149 per record-step (δ = 1e-2).
- In the column toy, with the arrow lasting the age (h = 1.2e-61), this needs ε ≤ 2.6e-106 (cost −ln ε ≥ 243).
- In P3 it needs u·r ≤ (formation rate) × 5e-151.

These are large but logarithmic costs. The real price is κ (§3.5).

---

## 4. Against (i), (ii), (iii) and O-rec, route by route (set B: RP plus whole-law B4⁺)

| Route | (i) count never falls (1 − δ) | (ii-s) never | (ii-δ) | (iii) vs F1 | O-rec (still forming today) | Status |
|---|---|---|---|---|---|---|
| Law-level permanence | – | – | – | – | no formation at all | **Excluded** (Lemma T, PROVED) |
| P1: scalar records, soft isotropic, "fill then freeze" | yes | no (Lemma T′) | yes with strong couplings | yes: the bulk is B4⁺-symmetric | **no**: formation within ξ ~ 1–5 steps | CHECKED (toy) |
| P1 with a preferred axis (column) | yes | no | yes | conditional | yes with h ~ 1/age | **Not set B**: S₂ = 2 in the law |
| Boundary-only RP laws (S3/S4/S6) | yes | **yes** | yes | SUGGESTED fine | **no**: everything forms at step 1 | CHECKED |
| P2: hard tags | yes | **yes** | yes | yes if sparse | yes with ln w ~ rate | **Not RP**, so B3 fails (PROVED) |
| P3: soft tags, RP | yes | no (Lemma RP-odd) | **yes** | yes if sparse | yes **only with κ tuned** to ≲ 1.2e-61 (≲ 3e-78 for uniform formation) | CHECKED (1+1); SUGGESTED (3+1) |
| Strict permanence plus formation after t = 0 plus RP | – | – | – | – | – | **None in any checked class**; no-go needs the referee |

**Does "permanent", read in a block sense, impose a law-level arrow?** No, it does not *impose* one:
- the per-event reading (P-1) is empty;
- the tagged reading (P-4) is covariant, with the arrow in the state.

But inside set B (RP), strict permanence plus ongoing formation is excluded in every checked class. The surviving versions are:
- (ii-δ) with a tuned κ (P3); or
- strict permanence with no RP (P2); or
- a law-level arrow or axis (class I, via Lemmas E and A).

---

## 5. Excluded reading (R-Q), briefly (SUGGESTED)

If records are real-time events of the OS-reconstructed theory, the Euclidean configuration is not the history. B4⁺ ∋ −1 continues to CPT (Jost; RECALLED), so the reconstructed law is CPT-symmetric and the arrow sits in the initial state, as in standard physics. Record formation then has three options:

- **Emergent decoherence records.** Permanence is probability 1 − δ only: the repository's 06-05 toy shows records *decreasing* from a time-reversed state (`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md:44-59`). This also gives up "a state is a configuration of records" (`:92`), because the state becomes a vector.
- **A real-time flash law.** This is a Lindblad semigroup, which is oriented. Lemmas B and E then apply inside the record sector. The induced LV could be suppressed by record rarity (Γ/E ~ 3e-35 for a 1 GeV nucleon at the O4 rate; SUGGESTED), but whole-law B2 is broken in the record sector.
- **A time-symmetric collapse formulation** (Bedingham–Maroney; RECALLED). It needs boundary-state input again.

None of these was computed here.

---

## 6. (d) Prior art (each counted once)

- **06-05 arrow note.** "The arrow is in the initial condition, not the dynamics". It has a residual: the past hypothesis is a "universal-floor open input" (`:44-69,111-115`). R2-5 agrees and adds that the same symmetric law gives an *equal* un-formation flux far from the boundary (u/f = 1.000), so the arrow is local to the boundary.
- **06-06 firewall.** "Post-record counts do not orient a physical arrow" (`:16,30-44`). This is consistent with Lemma T.
- **06-11 existence reduction.** "Durability is exactly the load-bearing property" (`:49-54`). R2-5 shows that strict durability is exactly what RP plus symmetry cannot supply with ongoing formation.
- **06-23 signature-neutral note.** "The arrow coexists with a Euclidean substrate" (`RECORD_TICK_SIGNATURE_NEUTRAL_2026-06-23.md:50`). It is right about the direction, which comes from the boundary. It is silent on strict permanence under RP, which R2-5 finds fails in every checked class.
- **Block 93.** Covariant symmetric weights give detailed balance, "History is time-reversal invariant under the stationary law" (`…2026-09-23.md:29`). This is the stationary-law version of my reversibility step. It concerns the excluded re-recording comparator.
- **Owner directive, 09-18 (memory).** "'records form' means records form: the formation (causal, level-time) reading IS the axiom; the static/frozen Gibbs law is only the equilibrium comparator". Set B's block reading is in tension with this (§1).
- **Owner thought, 09-28 (memory; a thought being tested, not a premise).** "A sealed box fills until frozen". The P1 and boundary-only RP regimes are exactly "fill then freeze". The owner also says "there is no sealed box", and O-rec excludes that regime as our epoch.
- **Literature (RECALLED, not fetched).**
  - Boltzmann; Albert, *Time and Chance* (2000); Price (1996): the Past Hypothesis.
  - Aharonov–Bergmann–Lebowitz (1964): time-symmetric measurement statistics, with the arrow from pre-selection.
  - Bedingham–Maroney, Found. Phys. 47 (2017): time-symmetric collapse.
  - Osterwalder–Schrader (1973/75) and Osterwalder–Seiler (1978): reflection positivity and the positive self-adjoint transfer matrix.
  - Kolmogorov's reversibility criterion.
  - Collins–Perez–Sudarsky–Urrutia–Vucetich (2004): Planck-scale LV transmitted at natural size.

  As far as I know, the lattice statements here are not in that literature:
  - RP excludes strictly persistent time-odd records;
  - strict permanence under RP needs boundary-only formation;
  - in the static law, formation time is set by the free-energy balance κ.

  This is unverified.

---

## 7. Prices named (none adopted; owner decisions)

- **R2-5-a (Record text, `:80`).** "records are permanent" becomes "in states with a low-record boundary, records are permanent with probability ≥ 1 − δ". The low-record boundary is supplied state data (the past-hypothesis residual already logged in the 06-05 note). This refines O5's B4 (`C5_O5_synthesis.md:357`).
- **R2-5-b (Record content; B2's action on content).** Records carry a time-odd tag (tail and head). Without it there is no non-vacuous block reading of "form" or "permanent" (§3.1). SUGGESTED: the tag can live in M₂(C) ⊃ ℍ ≅ R⁴, with SO(4) acting as q ↦ aqb̄, so the Qubit domain text need not change. But how B4⁺ acts on site content is new B2 content.
- **R2-5-c (a tuning).** The record-versus-blank per-step weight balance κ ≲ 1.2e-61 for O-rec, and ≲ 3e-78 for uniform formation under (iii). Under RP this is a cancellation of O(1) numbers.
- **R2-5-d (the alternatives that keep strict permanence).**
  - Drop RP. Set B then loses the OS route to real time (B3).
  - Or keep a law-level arrow or axis. Lemma E (and Lemma A) then put set B back in class I, i.e. toward set C.
- **Owner reading conflict.** Set B's Record is the static Z⁴ joint law read as the meaning. The 09-18 directive says the formation reading is the axiom.

## 8. Referee requests

For codex sol, before anything here is recorded as a no-go:
- Lemma T′.
- Lemma RP-odd, including the claim that bond-RP is equivalent to the twisted kernel being PSD for these classical transfer laws.
- The scope of the exhaustive search (`r25_rp_search2.py`).
- The P3 construction: its RP, and its 3+1 covariance with sideways tags.

Two further requests:
- Check the teleology claim (formation rate = κ) beyond the three toys.
- Check the RECALLED Euler–Heisenberg thermal coefficient.

## 9. Files (`scratchpad/C5/R2-5/`)

- `r25_b4.py`/`.out`: B4⁺ contains 24 time-reversing proper elements.
- `r25_lemmaT.py`/`.out`: exhaustive hard column laws (r = 3, 4); soft reversibility.
- `r25_toy_gibbs.py`/`.out`: the registered 1+1 toy, isotropic and anisotropic, with controls.
- `r25_tradeoff.py`/`.out`: arrow length against un-formation; column kernel checks.
- `r25_labels.py`/`.out` (periodic) and `r25_labels_open.py`/`.out` (blank walls): P2.
- `r25_rp.py`/`.out`: P2's twisted kernel is not PSD.
- `r25_rp_search.py`/`.out` and `r25_rp_search2.py`/`.out`: the exhaustive RP search, S1–S6, with and without RP.
- `r25_soft_labels.py`/`.out` and `r25_soft_labels_tuned.py`/`.out`: P3.
- `r25_numbers.py`/`.out`: LV and requirement numbers.
