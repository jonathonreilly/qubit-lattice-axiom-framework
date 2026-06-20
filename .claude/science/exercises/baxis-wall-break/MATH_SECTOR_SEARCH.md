# Exercise Four — Mathematics Sector Search (B-AXIS wall)

**Slice:** EXERCISE FOUR (math-sector search) of the `baxis-wall-break` exercise.
**Date:** 2026-06-20  •  Posture: BREAK the wall / find genuinely NEW formal lenses,
not defend the current no-go. Treat every framework premise as a challengeable
assumption for this exercise.

**Framework Refresher surfaces read (stated per skill requirement):**
`docs/MINIMAL_AXIOMS_2026-06-05.md`; `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`;
`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`; `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`;
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`; `docs/audit/data/axiom_premise_nodes.json`
and `docs/audit/data/tier_a_admissions.json` (READ-ONLY);
`docs/ai_methodology/skills/review-loop/SKILL.md`; `docs/repo/CONTROLLED_VOCABULARY.md`.

**Wall surfaces read:** the exercise `EXERCISE.md`; the consolidated
`docs/SINGLE_CLOCK_BAXIS_OBSTRUCTION_UNIFIED_NO_GO_NOTE_2026-06-20.md`; the route
ledger `NO_GO_LEDGER.md`; the keystone
`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`; the
governing fence `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`; the
`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md`; the prior
operator-algebra attempts on the *different* P1-additivity target
(`OBSERVABLE_PRINCIPLE_P1_BRIDGE_TOMITA_GIBBS_MODULAR_NARROW_NOTE_2026-05-21.md`,
`..._JONES_INDEX_SUBFACTOR_...`, `..._CONNES_NC_SPECTRAL_...`); the
`A3_ROUTE2_SINGLE_CLOCK_C3_OBSTRUCTION_NOTE_2026-05-08_r2.md` (modular-conjugation-J
attempt, for the Koide C_3 target).

---

## 0. What the campaign has ALREADY closed in math-sector terms (do not re-propose)

To keep every entry below genuinely new, here is the math content the campaign has
already burned, stated in sector vocabulary:

- **Finite group / rep theory (B_4 / S_4).** The bare-surface automorphism group is
  the signed hyperoctahedral `B_4`, `|G_bare| = 384`, with axis-permutation image the
  **transitive `S_4`** (block01 `single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`).
  Every A_min *kinetic-surface enrichment* E1–E8 has joint stabilizer either full
  `S_4` (isotropic) or trivial (axis-symmetric W-break). The only sub-`S_4`
  (one-axis-selecting, `S_3`) enrichment is a per-axis `Z_2` BC datum, itself
  `S_4`-transportable and (the campaign says) outside A_min. **→ A finer kinematic
  invariant on the bare surface is closed. New rep-theory vectors must change the
  acted-on object (state, not surface) — see §1.**
- **Operator algebras — commutant / center.** N5 is closed-as-FALSE for the
  commutant/center route because the supplied `T̂² = ⊗_p diag(1, e^{−2E(p)})` is
  *maximally factorized*; the factor-generator span is `{n_p}`, dimension `L_s`, and is
  **abelian**. No commutant argument forces a single orbit.
- **Operator algebras — Tomita-Takesaki, Jones index, Connes NC-spectral.** All three
  were tried, but ONLY against the **P1 scalar-additivity** target (`OBSERVABLE_PRINCIPLE`
  family), where each reduces to the Cauchy `log(xy)=log x+log y` "Pattern-L"
  circularity. **Crucially, modular theory was applied there on the TRACIAL pre-record
  state (modular flow trivial) or as the Gibbs state of the framework's own `D`
  (circular). The modular FLOW σ_t as an intrinsic clock for N2b/N5/orientation on a
  non-tracial, Record-conditioned A_min state was never run.** (The A3_ROUTE2 note used
  modular *conjugation J* — antilinear, Bisognano-Wichmann — to distinguish C_3 corners
  for Koide; it is a different operator and a different target.)
- **KMS / APBC.** Closed as an axis supplier (N4): KMS is formulated *after* a trace
  circle is named, and W maps APBC-τ → APBC-x₁ exactly.
- **Index / spectral-flow / anomaly (count-not-label).** The `ε(x)=(−1)^{Σx}` chirality
  grading is W-invariant and `{D_hop, ε}=0` is W-preserved: a count rule constrains the
  *number* of temporal directions, not a *label*.
- **Native-on-Z³ reframe.** Dissolves N4 as a question but RELOCATES (does not derive)
  N2b/N5/orientation to the emergent-dynamics open gate.

Everything below targets a hole NOT in that list.

---

## 1. Sector entries (Sector | Reframe | Theorem/tool | Toy | Attack | Falsifier | First artifact)

### S-1 — Operator algebras / Tomita-Takesaki: modular flow of the **Record-conditioned** (non-tracial) state as the intrinsic clock [N2b + N5 + orientation]

- **Object that changes.** Not the surface, not the tracial state, not the Gibbs state
  of `Ĥ`: the **GNS state ω of the full non-abelian A_min algebra `⊗_x M_2(C)`
  conditioned on a realized record** (supplied by the `realized_state_primitive`,
  which is an *approved premise node*, not a BC datum). A faithful normal state ω on a
  von Neumann algebra `M` canonically determines the modular automorphism group
  `σ_t^ω = Ad(Δ_ω^{it})` (Tomita-Takesaki) — a **distinguished one-parameter group with
  no external time input**.
- **Reframe.** N2b says "no A_min observable carries `1/time` units, so `a_τ` is gauge."
  But Tomita-Takesaki produces a *canonical, dimensionless* one-parameter flow `σ_t^ω`
  intrinsic to (M, ω) — Connes' "le temps = la dynamique modulaire". The clock unit is
  not imported; it is fixed by the state. N5 says "the factor clocks `{n_p}` are a
  commuting `L_s`-parameter family with no canonical single orbit." But `σ_t^ω` is a
  *single* canonical orbit selected by ω, and on a non-abelian M it is generically NOT
  inner / NOT a factor clock.
- **Theorem/tool.** Tomita-Takesaki modular theory; **Connes cocycle Radon-Nikodym
  `(Dω : Dφ)_t`** and the **Connes spectral invariant `S(M)` / `T(M)` (type
  classification)**; KMS uniqueness (the modular flow is the *unique* flow for which ω
  is KMS at β=1).
- **Minimal toy (RUN — see §2 Probe A).** On `(C^2)^{⊗2}` with a generic full-rank
  non-tracial ρ, `K = −log ρ` satisfies `‖K − (a·H_factorclock + b·I)‖ = 3.46 > 0` and
  `‖[K, n_0]‖ = 2.11 > 0`. So the modular generator is provably NOT a factor clock and
  does NOT commute with them: it is a genuinely distinct one-parameter group, exactly
  the object N5 says is "missing." This is the toy that shows the lens has teeth.
- **How it attacks N2b/N5.** If A_min + Record canonically fixes a faithful state ω
  (the record-conditioned state via the realized-state primitive), then σ_t^ω is a
  derived, unit-free, single-orbit clock — candidate closure of BOTH N5 (single
  canonical orbit) and N2b (intrinsic dimensionless rate). Orientation bonus: the
  modular flow has a built-in direction (the KMS `+iβ` strip), a potential arrow
  source that is *not* the past-hypothesis.
- **What would falsify it (the trap to check FIRST).** Two ways it dies, both decisive:
  (i) **Circularity** — if the only A_min-canonical faithful state is the Gibbs state of
  the supplied `Ĥ` (or the tracial state), then `σ_t^ω = Ad(e^{itβĤ})` is just the
  transfer dynamics back again (this is exactly why the P1 Tomita-Gibbs route failed),
  or trivial. (ii) **State non-canonicity** — the realized-state primitive supplies the
  state *pointwise* but explicitly disclaims a state-selection rule; if the modular flow
  depends on *which* realized state (counterfactual-test failure), it is registered data,
  not a derived clock. **The make-or-break question: is there a state on A_min that is
  (a) canonical from Lattice+Quantum+Record alone, (b) non-tracial, and (c) NOT the
  Gibbs state of `Ĥ`?** If yes → real crack. If the answer is forced to (a)+Gibbs-of-Ĥ,
  the route sharpens the no-go to "the modular clock = the transfer clock, so N2b/N5 are
  the SAME residual as the keystone's own `T̂²`" — a citable strengthening.
- **First artifact.** A finite runner on `⊗_{x∈small Z^3} M_2(C)` that (1) builds the
  record-conditioned state ω from the realized-state primitive (a localized durable
  record + the dephasing readout context), (2) computes Δ_ω and σ_t^ω, (3) tests
  whether σ_t^ω equals `Ad(e^{itβĤ})` for the transfer Ĥ (circularity check) and
  whether it depends on the realized record choice (counterfactual check). Decision tree:
  distinct-and-canonical → closure lane; equals-transfer or state-dependent → sharpened
  no-go that *unifies* N2b and N5.

### S-2 — Probability / realized-state measure theory: the realized-state primitive breaks `S_4` *intrinsically* (a record locus is not `S_4`-fixed) [N4]

- **Object that changes.** Not the kinetic surface (which is `S_4`-isotropic), and not a
  translation-invariant BC datum (which is the only thing N4's enrichment search E1–E8
  tested): the **realized state's record support** — the set of sites carrying durable
  records, supplied by the `realized_state_primitive` (approved premise) together with
  the Record axiom.
- **Reframe.** The entire N4 no-go is "every A_min *kinetic-surface* anchor is
  W/S_4-transported (resid 0); the only one-axis-selecting datum is a translation-
  invariant per-axis `Z_2` BC, which is `S_4`-transportable and outside A_min." This
  silently restricts "A_min content" to *translation-invariant* structures. But A_min
  now includes the realized-state primitive, and a **generic realized state is not
  translation-invariant** — its record locus is a specific finite set of sites. The
  stabilizer of a generic finite point-set under `B_4`/`S_4` is a *proper* subgroup.
- **Theorem/tool.** Orbit-stabilizer over the signed hyperoctahedral `B_4`; the fact
  that `S_4` acts transitively on axes but the stabilizer of a generic configuration
  (non-`S_4`-symmetric record locus) is trivial or `< S_4`. This is finite group theory,
  but applied to the *state*, not the Hamiltonian — the move the campaign never made.
- **Minimal toy (RUN — see §2 Probe B).** On the even block `L=(4,4,4,4)` the signed
  `W` keeps the hop exactly (`‖W M Wᵀ − M‖ = 0`). A realized ground state with a durable
  record at the W-fixed diagonal site `(0,0,0,0)` has *identical* τ- and x₁-marginals
  (axis-symmetric — the honest control). But a record at the asymmetric site
  `(1,0,0,0)` gives `‖τ-profile − x₁-profile‖ = 0.0015 ≠ 0`: **the realized state
  breaks the τ↔x₁ exchange.** The kinetic surface is exchange-symmetric; the realized
  *state* on it need not be.
- **How it attacks N4.** The S_4-transitivity argument compares *bare surfaces*: "any
  axis-anchor about τ conjugates by W to the identical anchor about x₁." That is true of
  the surface but FALSE once a specific realized state is fixed: `W` maps state ω to a
  *different* state `WωW†` with a relabeled record locus. The axis is then selected
  *relative to the realized record content*, which is exactly the kind of
  "history-supplied, not law-supplied" selection the realized-state primitive is licensed
  to provide. N4 may not need a new BC datum at all — it may need the realized state it
  was already allowed to evaluate at.
- **What would falsify it.** (i) **Transportability survives** — if for *every*
  realized state ω there is a `B_4` element g with `gωg† = ω` AND g non-trivial on axes,
  the selection is still transportable (check: generic record loci have trivial
  stabilizer, so this should fail for the adversary — i.e. the route survives). (ii)
  **Counterfactual/registered-data objection** — the realized-state primitive forbids
  quoting a value that changes under another law-admissible state; "which axis is time"
  must be invariant over the law-admissible family or it is registered data, not a
  derivation. **This is the crux: is the time-axis label a state-INVARIANT, or merely
  state-data?** If the *same* axis is selected for the whole law-admissible class (e.g.
  because every physical record-forming history shares the arrow/low-record past
  hypothesis), it is a derivation; if different realized states pick different axes, N4
  collapses into the realized-state register (still progress: it MOVES N4 out of "needs
  a new BC axiom" into "is realized-state data," a strictly weaker residual).
- **First artifact.** A runner that (1) enumerates the `B_4` stabilizer of a generic
  finite record locus and confirms it is `< S_4` (so a record breaks transport), then (2)
  tests INVARIANCE: across a sampled family of law-admissible realized states sharing a
  past-hypothesis-style low-record initial condition, is the W-broken axis the *same*?
  Invariant → N4 derivation candidate; varies → N4 demoted to realized-state register.

### S-3 — Category theory / universal property: time as the **terminal object of the record-poset (causal-set colimit)**, bypassing the 4th-coordinate embedding [N4 dissolution + orientation]

- **Object that changes.** Replace "which of 4 Euclidean lattice axes is time" with the
  **partial order generated by the durability relation on records** (record r₁ ≤ r₂ iff
  r₁ is fixed-once-registered before r₂ can change — the Record axiom's *durable*
  clause). Time becomes a derived structure on a poset/category, not a coordinate.
- **Reframe.** The keystone reads dynamics off the transfer `T̂` on the 4-torus, which
  is *why* W/S_4 act (time is a coordinate there). The native-on-Z³ reframe removes the
  coordinate but leaves the generator unsourced. Category theory offers a THIRD frame:
  the one-parameter evolution is the **universal (terminal/initial) cofiltration of the
  record poset** — a colimit over the durability order. Universal properties are
  unique-up-to-unique-iso, which is exactly the "exactly one clock" content N5 wants,
  derived rather than premised.
- **Theorem/tool.** Causal-set / poset-of-events reconstruction (Sorkin; Malament's
  theorem that the causal order fixes the conformal structure); colimit uniqueness;
  the **Hasse-diagram height function** as a canonical (up to additive/scale) "time"
  on a graded poset. Grading of a poset → a `Z`-valued time with a *direction* built in.
- **Minimal toy.** Take 3–4 qubits, a sequence of durable records (CPT-orbit
  registrations from the Record axiom) forming a small poset; compute its height
  function and check (a) it is unique up to the poset automorphisms, (b) it is NOT
  invariant under the spatial `S_4` (records are events, not lattice axes), (c) the
  number of independent maximal chains = the number of independent "clocks."
- **How it attacks N5/N4.** If the record poset is **graded with a unique height
  function up to scale**, that is a single canonical time order (N5: one orbit) with a
  direction (orientation), and it lives on *events* so the spatial-axis `S_4` is simply
  not the relevant symmetry group (N4 dissolves *with* an answer, unlike the native-Z³
  reframe which dissolves without one). N5's "L_s independent factor clocks" become
  "L_s independent maximal antichains," and the question sharpens to: does the Record
  axiom's durability force a *total* order on the central-sector registrations (one
  clock) or only a *partial* one (many)?
- **What would falsify it.** (i) The durability relation may be too weak to grade the
  poset (Record supplies "fixed once registered" but "no time metric, no
  sector-generation rule" — so the poset may be an antichain with no order). (ii)
  Malament-style reconstruction needs the order to be *locally finite + past-finite*;
  the Record axiom may not supply past-finiteness without the past hypothesis (so
  orientation leaks back to the past-hypothesis, matching the campaign's firewall).
- **First artifact.** A symbolic check: from the Record axiom's "durable = fixed once
  registered" + finite additivity, derive the strongest order relation provable on
  central-sector registrations, then test whether it is total (→ one clock) or admits
  incomparable pairs (→ N5 stays open, but now *as a poset-width statement*, a sharper
  and more citable no-go than "L_s commuting factor clocks").

### S-4 — Ergodic theory / Galois-type rigidity: is `a_τ` pinned by an **arithmetic/return-time** invariant of the transfer spectrum? [N2b]

- **Object that changes.** N2b's `a_τ → c·a_τ` gauge rescales all of `spec(Ĥ) = {E(p)}`
  by `1/c`. The campaign's claim "no A_min observable carries 1/time units" is about
  *expectation values*. But the **set of spectral ratios + their arithmetic type** is
  rescaling-invariant and could carry a *canonical* unit via a return-time / rotation-
  number normalization.
- **Reframe.** A one-parameter unitary group `U(t) = e^{−itĤ}` on a finite block is
  *almost periodic*; its **recurrence/return-time spectrum** (the group generated by
  `{E(p) − E(q)}` over `Z`) is a finite-rank subgroup of `R`. Rescaling moves the
  subgroup but not its *rank* or its *commensurability pattern*. If A_min forces a
  specific commensurability (e.g. a rational relation among the `E(p)` from the staggered
  dispersion `E(p) = arcsinh√(m²+sin²p)` at special m), there is a canonical generator
  of the return-time group = a canonical tick.
- **Theorem/tool.** Almost-periodic / Bohr spectrum; the **rotation number** as a
  conjugacy invariant (Poincaré); three-distance / continued-fraction structure of
  `{n·E(p) mod 1}`; Masser-type results on when `arcsinh√(m²+sin²p)` values are
  `Q`-linearly (in)dependent.
- **Minimal toy.** For `L_s = 3, m = 0.5`, compute `{E(p)}`, the rank of the `Z`-module
  they generate, and whether any nontrivial integer relation `Σ n_p E(p) = 0` holds. A
  relation would mean a *finite* return time → a canonical period → a canonical `a_τ`
  (up to the integer). No relation (rank = `L_s`) → genuinely no arithmetic tick (N2b
  confirmed, but now via an arithmetic-independence statement, much sharper than "gauge").
- **How it attacks N2b.** A canonical return period `T*` (smallest `t>0` with
  `U(T*) = I` up to phase) would be a dimensionless number that, paired with the
  scale-reference primitive `a^{−1} = M_Pl`, fixes `a_τ` — turning N2b's gauge into a
  *derived* value. The lever is that return time is a `1/energy` = time-dimensioned
  object that is NOT a mere expectation value, so it dodges the "no observable carries
  1/time" wall.
- **What would falsify it.** Generic `m` gives `Q`-linearly independent `E(p)` (rank
  `L_s`, no finite return) → no canonical period; AND the return time still rescales
  under `a_τ → c·a_τ`, so unless A_min *also* forces a specific `m` (it does not — `m` is
  realized-state/admission data), the unit stays free. Most likely outcome: a **sharper
  N2b no-go** ("the transfer spectrum is generically arithmetically independent, so not
  even a return-time normalization pins `a_τ`"), which is still a real deliverable.
- **First artifact.** A number-theory runner: tabulate the `Z`-module rank and any
  integer relations among `{E(p)}` over the staggered dispersion for several `(L_s, m)`;
  report whether a canonical period exists. This is cheap and decisively settles whether
  N2b can ever be closed by an arithmetic invariant.

### S-5 — Convexity / SDP: the transfer-clock orbit as the **unique extreme ray** of the cone of A_min-admissible positive evolutions [N5]

- **Object that changes.** N5's missing supplier is "a chosen positive clock-ray in
  `span_{≥0}{n_p}` carrying `(L_s−1)` free parameters." Reframe the *set* of admissible
  clock generators as a convex cone and ask for a **variational / extremality**
  principle that picks one ray canonically.
- **Reframe.** The factor clocks span a simplex of commuting positive generators
  `K = Σ_p λ_p n_p, λ_p ≥ 0`. The transfer's own generator `Ĥ = Σ_p E(p) n_p` is ONE
  interior ray. A canonical selection needs a strictly convex functional on the cone
  whose unique minimizer is a single ray. Candidate: **maximum-entropy / minimum
  Fisher-information** clock, or the ray minimizing the Lieb-Robinson velocity (fastest
  vs slowest clock), or the **Connes-Stormer entropy** of the flow.
- **Theorem/tool.** Strict convexity → unique minimizer (KKT); the **maximum-entropy
  principle** (Jaynes) selects the least-committed generator; SDP duality to certify the
  minimizer is unique and to read its `(L_s−1)` free parameters as the *active
  constraints* — i.e. exactly what A_min would have to supply.
- **Minimal toy.** On the 2-qubit `[C-2CLK]` countermodel (`T_A⊗I`, `I⊗T_B`), set up the
  cone of `λ_A n_A + λ_B n_B`, and test three candidate selection functionals
  (entropy-rate, LR-velocity, Fisher info) for whether each has a *unique* extreme ray
  and whether that ray equals the transfer ray `E_A n_A + E_B n_B`.
- **How it attacks N5.** If a *physically motivated, A_min-expressible* functional has a
  unique minimizing ray = the transfer ray, N5 closes by a variational principle (no new
  axiom — the functional is built from Record additivity + the supplied transfer). If
  the minimizer is unique but ≠ transfer ray, that is a *second* canonical clock → N5
  WORSENS (a real result: "A_min's natural extremal clock disagrees with the transfer
  clock"). If no functional gives uniqueness, N5 confirmed as a genuine `(L_s−1)`-cone.
- **What would falsify it.** Every natural functional (entropy, LR-velocity) is itself
  `S_{L_s}`-symmetric under permuting modes, so its minimizer is the *symmetric* ray
  `Σ_p n_p` (= total number), NOT the dispersion-weighted transfer ray `Σ_p E(p) n_p`
  unless the dispersion weights enter the functional — and the dispersion is supplied by
  the staggered surface (a Tier-A `AC_phi_lambda` admission), so the selection may
  inherit the admission rather than A_min. Check this dependency first.
- **First artifact.** An SDP/convex runner over the factor-clock cone evaluating
  uniqueness of the extreme ray for entropy-rate, LR-velocity, and Fisher-information
  functionals; report whether any picks the transfer ray *without* consuming the
  staggered dispersion as input.

### S-6 — Spectral graph theory: drop the kinetic-isotropy primitive and ask whether the **graph Laplacian alone** ever distinguishes a time axis [N4 — challenge the c_t=c_s premise]

- **Object that changes.** The approved `kinetic_isotropy_primitive` grants `c_t = c_s`
  (hypercubic `Z^3 × Z_τ`). This is *precisely the premise that makes W/S_4 exact*
  (the keystone says so: "kinetic isotropy makes the surface MORE exchange-symmetric").
  Reframe: treat `c_t/c_s` as a free dial (the primitive admits this is the genuinely
  free kinetic-form ratio) and ask whether *spectral-graph* asymmetry between the time
  cycle and space cycles is a derived A_min fact or a primitive-supplied one.
- **Reframe.** The N4 no-go is conditional on a primitive that *imposes* the very
  symmetry it then fails to break. This is a hidden load-bearing premise: N4's
  "S_4-isotropic" is downstream of kinetic isotropy. If `c_t = c_s` is itself the
  emergent-Lorentz *output* (the primitive note admits "treating it as derived would be
  circular"), then the no-go is "given the symmetric surface, the surface is symmetric"
  — true but possibly vacuous about the *physical* (pre-isotropy) lattice.
- **Theorem/tool.** Spectral graph theory of product graphs `C_{L_τ} □ C_{L_s}^3`; the
  Laplacian spectrum factorizes as a Minkowski-sum of cycle spectra; **Cheeger /
  algebraic-connectivity** differences between a distinguished cycle and the rest;
  isospectrality vs the signed-exchange `W`. The diagnostic is whether *any*
  graph-spectral invariant (not just the adjacency Laplacian E2, already tested) is
  W-asymmetric when `c_t ≠ c_s`.
- **Minimal toy.** Build the weighted hop with a tunable temporal weight `w_τ ≠ 1`;
  recompute `‖W M Wᵀ − M‖` as a function of `w_τ`. At `w_τ = 1` it is 0 (confirmed,
  §2 Probe B); for `w_τ ≠ 1` it is nonzero — so the time axis IS spectrally
  distinguished the moment kinetic isotropy is relaxed.
- **How it attacks N4.** It reframes N4's residual: the axis is selected by `c_t ≠ c_s`,
  and `c_t = c_s` is an *approved primitive*, not A_min. So the honest statement is "N4
  is open ONLY because the kinetic-isotropy primitive symmetrizes the surface; the
  physical lattice generically distinguishes the axis." This does not add an axiom — it
  reads an *existing approved primitive* as the (anti-)selector and asks whether the
  emergent-Lorentz program (which OUTPUTS `c_t = c_s`) makes the selection circular.
- **What would falsify it.** The primitive is explicitly dimensionless-structural and
  the campaign would say "relaxing it is adding anisotropy = a selector = outside A_min,
  same as the BC datum." The counter is that the BC datum is *not* an approved premise
  whereas the kinetic-form ratio *is* registered — so the asymmetry direction is already
  in the premise set, just set to the symmetric value. Decisive check: does the
  emergent-Lorentz derivation of `c_t = c_s` *consume* a chosen time axis? If yes, the
  whole loop is circular and N4 is not independent of the emergent-Lorentz program.
- **First artifact.** (a) the weighted-`w_τ` W-residual curve (cheap); (b) a citation
  audit of `EMERGENT_LORENTZ_INVARIANCE_NOTE.md` and the kinetic-isotropy primitive to
  determine whether the `c_t = c_s` output is derived *before or after* an axis is fixed
  — i.e. whether N4 and the isotropy primitive are circularly entangled.

### S-7 — Algebraic topology / index theory: temporal axis as the **odd K-theory / spectral-flow generator** of the staggered Dirac family [N4 — count-to-label upgrade]

- **Object that changes.** The campaign closed "anomaly = count not label" (`ε`
  W-invariant). Reframe from the *parity grading* to the **spectral flow of the Dirac
  operator under the one-parameter family generated by translation along each axis** —
  a `Z`-valued index that is orientation-sensitive.
- **Reframe.** `{D_hop, ε} = 0` only gives a `Z_2` count. But spectral flow `SF(D_θ)`
  along a loop in parameter space is a *signed* integer (odd K-theory `K^1`), and the
  time direction is the one along which the *Hamiltonian* (not the Euclidean Dirac)
  generates spectral flow = particle creation. The asymmetry between "axis that carries
  spectral flow of `Ĥ`" and "axes that don't" could be a labeled, not merely counted,
  invariant.
- **Theorem/tool.** Atiyah-Patodi-Singer spectral flow; the **suspension isomorphism**
  `K^0 → K^1` that turns the `Z_2` chirality count into a `Z` flow; the fact that
  spectral flow requires a *distinguished* parameter (the would-be time) and is
  orientation-reversing-odd.
- **Minimal toy.** On the small staggered block, compute spectral flow of the one-
  particle Dirac operator as each axis's gauge holonomy / twist is cranked `0 → 2π`;
  check whether `W` maps the τ-flow to the x₁-flow (transport, route dies) or whether the
  flow is tied to `Ĥ ≥ 0` (the spectrum condition) in a W-breaking way.
- **How it attacks N4.** If spectral flow is nonzero only for the axis along which the
  spectrum condition `Ĥ ≥ 0` is imposed, and `Ĥ ≥ 0` is the (orientation-carrying) past-
  hypothesis correlate, then the time *label* (not just count) is the spectral-flow-
  carrying axis. This tries to upgrade the firewall's "count-not-label" by making `Ĥ ≥ 0`
  the labeler.
- **What would falsify it.** `W` commutes with `ε` and transports the Euclidean Dirac;
  spectral flow of the *Euclidean* operator will transport too. The route lives or dies
  on whether the *Lorentzian/Hamiltonian* `Ĥ` flow is W-covariant — and since `Ĥ` is
  reconstructed from `T̂²` which is W-symmetric, it most likely transports (route dies,
  but cleanly, as a spectral-flow-transport no-go that is new and citable). The honest
  prior is this strengthens the no-go rather than cracks it.
- **First artifact.** A spectral-flow runner over axis twists; primary output is the
  W-covariance of `SF`; secondary is whether `Ĥ ≥ 0` breaks that covariance.

### S-8 — Logic / model theory: is N2b/N5 **formally independent** of A_min (a definability / O-minimality statement)? [meta — turn the no-go into a theorem]

- **Object that changes.** Instead of attacking the wall, *prove the wall* at the right
  strength: show `a_τ` (N2b) and the clock-ray (N5) are **not definable** from the A_min
  signature, by exhibiting an automorphism of the A_min structure that moves them.
- **Reframe.** The `[τ-RESCALE]` gauge and the `[C-2CLK]` countermodel are exactly
  *automorphisms of the A_min-definable structure* that move `a_τ` and the clock-ray.
  Model theory packages "no observable carries 1/time units" as "the rescaling is an
  automorphism of the full A_min structure, hence anything it moves is undefinable."
  This converts the no-go from "we tried N routes" into "definability theorem."
- **Theorem/tool.** Beth definability / Svenonius theorem (a relation is definable iff
  it is fixed by all automorphisms); O-minimality of the real-closed structure carrying
  the transfer spectrum (so the only definable scalars are the `Q`-algebraic combinations
  of the `E(p)`, none of which is `1/time`).
- **Minimal toy.** Formalize the A_min observable algebra + Record readout as a structure
  `𝔄`; exhibit the rescaling and the factor-swap as automorphisms; conclude by
  Svenonius that `a_τ` and the preferred clock-ray are undefinable.
- **How it attacks N2b/N5.** It does not crack them — it makes them **theorems of
  independence** rather than route-exhaustion no-gos, which is a strictly stronger and
  more citable deliverable (the EXERCISE explicitly counts "a sharper, citable no-go" as
  progress). It also tells you the EXACT extra symbol any supplier must break.
- **What would falsify it.** If the automorphism group is *smaller* than assumed (e.g.
  the Record readout context secretly fixes a scale), then `a_τ` could be definable after
  all — which would itself be a crack. So running this is a no-lose: either a clean
  independence theorem or a discovery that something fixes the scale.
- **First artifact.** Write the A_min structure's automorphism group explicitly
  (rescaling `R_{>0}` × factor-permutations `S_{L_s}` × ...) and check, symbol by symbol,
  what it fixes; any non-fixed quantity is provably undefinable (no-go sharpened), any
  surprisingly-fixed quantity is a closure lead.

---

## 2. Grounding probes actually run (so the entries are not hand-waving)

Two finite numerical probes were run at `/tmp/baxis_probe.py` (read-only, no repo
state touched) to confirm the two strongest new vectors have teeth:

**Probe A (S-1, modular clock).** Generic full-rank non-tracial ρ on `(C^2)^{⊗2}`:
- `K = −log ρ`, fit against the factor-clock generator `H_fc = n_0 + n_1`:
  `‖K − (a·H_fc + b·I)‖ = 3.46` (NOT a factor clock).
- `‖[K, n_0]‖ = 2.11` (modular flow does NOT commute with the factor clocks).
→ The Tomita-Takesaki modular flow of a non-tracial A_min state is a genuinely distinct
one-parameter group from the `{n_p}` factor clocks — exactly the object N5 calls
"missing." (Open question that decides the route: is such a state *canonical* from
A_min+Record, or is it the Gibbs-of-`Ĥ` / state-dependent, which would make it circular.)

**Probe B (S-2 / S-6, realized-state and isotropy).** Staggered Kawamoto-Smit hop on
`L = (4,4,4,4)`, time-first KS phases:
- `‖W M Wᵀ − M‖ = 0.000` (confirms the even-block W-symmetry the campaign relies on).
- Realized ground state with a durable record at the W-fixed diagonal site `(0,0,0,0)`:
  τ-profile = x₁-profile exactly (the honest axis-symmetric control).
- Realized ground state with a record at the asymmetric site `(1,0,0,0)`:
  `‖τ-profile − x₁-profile‖ = 0.0015 ≠ 0` → **the realized state breaks the τ↔x₁
  exchange the kinetic surface preserves.**
→ N4's `S_4`-isotropy is a property of the *surface*, not of *A_min + a realized state*.
The campaign's enrichment search (E1–E8) and BC-datum analysis never tested a generic
(non-translation-invariant) realized state, which the `realized_state_primitive` (an
approved premise) explicitly licenses pointwise.

---

## 3. Ranking of the new vectors (for the synthesis hand-back)

| rank | vector | clause | why it is the highest-value NEW lens | first decisive test |
|---|---|---|---|---|
| **1** | **S-2 realized-state breaks S_4** | N4 | Uses an APPROVED primitive the N4 no-go never tested; turns "needs a BC axiom" into "is realized-state data" at worst, "axis is a state-invariant" at best. Probe B shows it breaks W. | `B_4`-stabilizer of a generic record locus + invariance of the broken axis over the law-admissible family |
| **2** | **S-1 modular clock on Record-conditioned state** | N5 + N2b | Tomita-Takesaki gives a canonical, unit-free, single one-parameter flow; Probe A shows it is distinct from the factor clocks. Directly targets the two clauses the native-Z³ reframe only relocates. | does σ_t^ω = Ad(e^{itβĤ}) (circular) or depend on the realized state (data)? if neither → crack |
| **3** | **S-8 definability/independence theorem** | N2b + N5 | No-lose: converts the route-exhaustion no-go into a citable Svenonius/Beth independence theorem, or finds a surprise fixed scalar (a crack). The EXERCISE counts this as progress. | write the A_min automorphism group; check what it fixes |
| 4 | S-3 record-poset universal time | N4 + N5 | Gives N4 an ANSWER (not just dissolution) and reframes N5 as poset-width; orientation built in. | is the durability order total (one clock) or partial? |
| 5 | S-4 arithmetic return-time | N2b | A `1/time` object (return time) that dodges "no observable carries 1/time"; likely a sharper no-go via arithmetic independence. | `Z`-module rank / integer relations among {E(p)} |
| 6 | S-6 kinetic-isotropy circularity | N4 | Names the hidden load-bearing premise (c_t=c_s) that symmetrizes the surface; checks N4-vs-emergent-Lorentz circularity. | does the c_t=c_s derivation consume a chosen axis? |
| 7 | S-5 extremal clock ray (SDP) | N5 | Variational single-orbit selection; honest risk it inherits the staggered dispersion admission. | does any natural functional pick the transfer ray w/o consuming dispersion? |
| 8 | S-7 spectral-flow label | N4 | Upgrade count→label via odd K-theory; honest prior is it strengthens the no-go. | W-covariance of spectral flow of Ĥ |

---

## 4. What NOT to do (so the next agent does not burn cycles)

- Do NOT re-run modular theory / Jones index / Connes NC-spectral against the **P1
  scalar-additivity** target — that is closed (Pattern-L Cauchy circularity), and it is
  a DIFFERENT target than N2b/N4/N5. The new content (S-1) is modular *flow* as a *clock*
  on a *Record-conditioned non-tracial* state, not modular structure for additivity.
- Do NOT propose KMS/APBC as an axis supplier (N4) — pruned (W maps APBC-τ→APBC-x₁).
- Do NOT propose the parity/chirality grading or a richer *kinetic-surface* enrichment
  as an N4 selector — E1–E8 are exhausted; the new move is the *state* (S-2), not the
  surface.
- Do NOT claim the native-on-Z³ reframe derives anything — it relocates.
- Do NOT treat any of S-1…S-8 as solved: each is a *first artifact* to build, and the
  honest prior for several (S-4, S-5, S-7) is "sharper no-go," not "crack." Only S-1 and
  S-2 have a plausible closure branch, and both have an explicit circularity/counterfactual
  trap that must be checked FIRST.
