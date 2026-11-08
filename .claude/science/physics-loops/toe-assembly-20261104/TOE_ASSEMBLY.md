# TOE assembly overview: the skeleton of the whole argument

Written 2026-11-04 by a Claude Opus 5.5 subagent of the lead, at the owner's direction of the same day: build our own skeleton of the whole argument, as Sussman and Alpoge did for Yang-Mills, then prove it part by part. The method is the one in the process review (`origin/claude/ym4d-hard-route:.claude/science/physics-loops/ym4d-hard-route-20261030/library/process-review-2026-11-04.md`, section 4, item 8) and in open PR #10138 (draft, distil, review for every part).

**What this file is.** An author-side planning skeleton. It grants no status, adopts no law and changes no axiom. Every "status" line below reports what the sources and the ledger say; none is a verdict. Proposed specifications in section 3 are proposals for the owner, who alone decides axiom and law changes.

**Source revision.** `origin/main` at `f5af11cd01` (fetched 2026-11-04). Axioms doc last changed at `dd16171663` (2026-10-16). Theme PRs #10124-#10131 read at their heads on 2026-11-04. All repo text was read through `git show origin/...` and `gh pr view/diff`, not from a working tree.

**Owner guidance applied (2026-11-04, via the lead).** "Just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed." So the four axioms are read plainly, as the current best statement. Where a part needs something the axioms do not give, this file does not record a wall. It writes a proposed specification (section 3) with exact text, the reason, and what it would let us derive.

---

## 1. Ground truth checked for this skeleton

### 1.1 The axioms (quoted from `origin/main:docs/MINIMAL_AXIOMS_2026-06-29.md`)

- **Lattice.** "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site."
- **Qubit.** "Each site has a domain of local possibilities." "The full one-site possibility domain has algebraic presentation `M_2(C)`."
- **Admissibility.** "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions."
- **Record.** "Records form." "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." "Only records are readable. A readout value is determined by record content alone. A site with no record cannot be read."
- **Qualification.** "A state is a configuration of records." "A law privileges no states. Its domain is a supplied condition, and at every state where the condition holds it gives exactly one answer."
- The doc also says: "Admissibility is not a dynamics axiom." It "does not choose a Hamiltonian or transfer operator, supply transition-probability or weight values, ... define a time metric, or provide a record-production process".

### 1.2 The approved primitives (`origin/main:docs/audit/data/axiom_premise_nodes.json`)

`canonical_ids`: `minimal_axioms`, `scale_reference_primitive` (the single scale `a^{-1}`, "Units conversion only"), `kinetic_isotropy_primitive` (`c_t=c_s`, "the emergent tick is grained on the same footing as the spatial edge"; it "does not re-axiomatize emergent time"), `realized_state_primitive` (one law-admissible realized state, evaluated "POINTWISE only"; "'typical'/'generic' banned as specialization predicates"; the counterfactual test: "a quoted number must be invariant over the law-admissible family, else it is registered data"; "The past hypothesis is explicitly NOT housed here").

### 1.3 The ledger (`origin/main:docs/audit/data/ledger/`, all 5,950 shards read by script)

- `effective_status`: 5,573 `unaudited`, 377 `meta`. **Zero rows are `retained`, `retained_bounded` or `retained_no_go`.** So no part below has a retained ledger row, and the (d) lines say so once per part.
- `claim_type`: 4,254 `bounded_theorem`, 643 `positive_theorem`, 335 `no_go`, 334 `open_gate`, 7 `decoration`, 377 `meta`.
- `claim_scope` is null in every one of the 5,950 rows. Where this file quotes a claim scope, it quotes the note's own frontmatter or "Claim scope" line, and says so.
- `ledger_meta.json`: `row_count` 5950, `last_invalidations` empty.
- Several rows carry older audits in `previous_audits` (for example `native_gauge_closure_note` was `audited_clean` on 2026-05-22 and 2026-05-23). Those grades predate the 2026-08-07 premise-epoch reset and are not current status.

### 1.4 The candidate-law register (`origin/main:docs/CANDIDATE_LAWS.md`, last changed `cab55ff82f`, 2026-10-18)

Three historical clauses with "zero premise weight": the lossless-influence clause (historical alias CL-1), "Influence passes from site to site without loss."; the record-removal clause (alias CL-2), "When a record forms, its qubit leaves the flow: the network is permanently short that site's share."; and a pending conservation proposal (alias CL-3). The register says their approval provenance is "unverified here".

The theme PRs use the same labels for a different three-law set: "CL-1 is the update law (cube tick, edge registers, split), CL-2 the actuality law (Born-preserving transport and records), CL-3 the response law (hinge sum, momentum constraint, shift)" (naming note in the #10128 map note, line 38). Every map note flags this collision. This file calls the theme set "the supplied three-law register" and never uses CL numbers for it.

---

## 2. The target

### 2.1 The repo's own goal statements

- `SCIENCE_WORKFLOW.md`, opening paragraph: "The goal is to build and test a theory of everything; whether any candidate succeeds is an open question." §5: "A candidate TOE is a connected proposed derivation with named gaps. Calling it established requires complete dependency and empirical validation."
- `README.md` (main): the four axioms plus three primitives are "the supplied foundation". Downstream, to be derived: "Born weights, measurement and readout contexts, record-formation rules (which admissible possibility a new record locks, at which site, with what weight, at what rate), dynamics and the time metric, kinetic-branch selection, source and action structure, and physical-observable identification". It also names "Three open derivation obligations": the AC occupancy statistical grain, the R-eta h-class/h-unit readout, and theta's quark-determinant cross-sector readout (`docs/audit/data/derivation_obligations.json`).
- `MINIMAL_AXIOMS_2026-06-29.md`, "Open Gates Outside The Axioms": the staggered-Dirac realization and `AC_phi_lambda`; the strong-CP theta obligations; P2/modulus and log-det readout; "context selection, measurement basis selection, Born weight values, probability rules beyond the distribution clause, update laws, decoherence mechanisms, and the remaining formation rules"; "arrow, record-production dynamics, physical persistence dynamics, time metric, and local observability of records"; "source/action and physical-observable identification"; `g_bare = 1`; "the scale-reference primitive and the separate gravity self-consistency question that the framework's natural unit equals the Planck length."
- The framework-refresher skill: "Standard-Model structure (flavor, masses, mixing, gauge) is to be derived from — or shown to be registered by — four axioms, not imported."
- The 2026-09-22 planning graph (`docs/CANDIDATE_ASSEMBLY_SOURCE_LINKED_GRAPH_ELEVEN_TARGETS_MINIMAL_DECISION_SETS_BOUNDED_THEOREM_NOTE_2026-09-22.md`, runner `TARGET_BRIEF`): "formation law", "possibility domain and menus", "handedness", "Born weights", "readability", "clock/rate", "formation unit", "record dynamics", "matter/composition", "support/gauge structure", "downstream gravity". Its scope: "No edge is certified as a physical necessity or sufficient theory completion."
- The planning scorecard (`origin/ai/execution:TOE_SCORECARD.md`, last changed 2026-09-11) is a status map, not a target statement; it is stale (it counts 4,700 ledger rows).

### 2.2 The target stated precisely

Let **A** be the four axioms, **P** the three approved primitives and **S** the set of owner-approved specifications from section 3 (empty today). The TOE target is a law **L** (section 3, PS-1 to PS-4) and proofs of T1-T9 below from **A + P + S**. Established physics names the targets; it never justifies a step. Each number in T6 is either law-level (it passes the realized-state counterfactual test: invariant over the law-admissible family) and is computed, or it is registered data of the realized state and the target is to show what registers it (guardrail G3).

- **T1, time and arrow.** Histories carry one total order (the tick or history index) along which the record set never shrinks. The arrow is the direction of record accumulation, given a stated initial condition. The time metric (tick length) relates to the spatial step by `c_t=c_s`.
- **T2, 3+1 spacetime.** At scales large against `a`, the effective description lives on three space and one time dimension, with Lorentzian signature (3,1).
- **T3, Lorentz symmetry at long distance.** All light species share one limiting speed `c`. Lorentz-violating terms are suppressed by powers of `a/r`, their leading coefficients computed, and compatible with observation.
- **T4, gauge group and continuum gauge theory.** The gauge group is `SU(3) x SU(2) x U(1)` (target named by the Standard Model; a quotient by `Z_6` is part of the target), with Gauss laws, and its long-distance dynamics is a continuum Yang-Mills theory with matter, with running couplings.
- **T5, matter.** Spin-1/2 fermions with Fermi statistics; chiral light content with doublers and mirrors removed; three generations; each generation in the Standard Model representation with its hypercharges; gauge anomalies cancel.
- **T6, masses and mixings.** Electroweak breaking; fermion masses, CKM and PMNS mixing, the CP phase, `theta_bar` below its bound, neutrino masses; each either computed (law-level) or shown registered.
- **T7, gravity.** Newtonian limit (Poisson equation sourced by energy, universal free fall, `G` in lattice units) and the GR limit (Einstein's equations at long distance, two tensor polarisations at speed `c`, PPN `gamma = beta = 1`, horizons in collapse).
- **T8, quantum readout.** Record frequencies follow Born weights of the state the law carries; readers agree; no signalling of marginals; interference and Bell correlations as in quantum theory.
- **T9, vacuum and cosmology.** A vacuum state of the law, stable, with the matter of T5 as its excitations; the cosmological constant; an FRW history with a perturbation spectrum; a dark-matter candidate or its absence; the baryon asymmetry.

---

## 3. Proposed axiom update (working set)

The owner approved this on 2026-11-04: "im good with the skelleton proposal but for 'adopt' we put them in the proposed axiom update section until we have the full theory figured, then we move them into the real axioms as simply as possible".

**Status.** These are working premises. The parts are drafted under them. They are not axioms, and `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. Every part that uses one names it, for example "under PS-1". When the full theory is in place, we move the set that is actually used into the real axioms, in the simplest wording that still does the work, and only with the owner's approval of that wording. A specification that no part ends up needing is dropped. Two that can be merged are merged.

| Entry | Treatment | Short form |
|---|---|---|
| PS-1 | In the working set | One fixed local covariant unitary update; the update count orders a history. The law choice, cube tick or D4 events, is settled in LW1. |
| PS-2 | In the working set | Menu independence: a possibility's probability does not depend on what else is offered. It gives the Born form by the binary-ternary theorem. |
| PS-3 | In the working set | One actual configuration, moved by minimal-change, maximum-entropy transport. Records never condition the odds. A record forms when a value has been copied to at least two neighbours. |
| PS-4 | In the working set | The first tick has no records. |
| PS-5 | In the working set as its fallback text (owner 2026-11-05, D1) | Each site has five fermion modes, algebra `Cl(10)`. The cell route failed at a named step on `L_cube` (B5b, B5b-T). Section 3.4. |
| PS-6 | In the working set | Frames are local: link registers transport frames, and the update is gauge-invariant. |
| PS-7 | In the working set | The vacuum is the half-filled sea. The record-freezing tension is resolved in VC1/TM1. |
| PS-8 | Law to test | The mirror-gapping interaction, inside CH1. Not a premise. |
| PS-9 | Law to test | The gravity response law, inside GR1/GR2. Not a premise. |
| PS-10 | Not adopted | `G a^{-2}` stays a target of GR1. |
| PS-11 | In the working set | A statement of law-probability one holds in the realized history. |
| PS-1c, PS-3h, PS-3c, PS-6r, PS-7r, PS-11c | In the working set (owner 2026-11-04) | Refinements from LW1, each checked for smuggled physics. Section 3.2. |
| PS-Ar | In the working set (owner 2026-11-04) | Admissibility's "nearest-neighbor conditions" are the state of the one-tick neighbourhood of influence. Section 3.3. |

The full text of each entry, with its reasons, follows.

### 3.1 The proposals in full

Each entry gives the exact proposed text, why a part needs it, and what it would let us derive. They fall into three kinds: an added axiom sentence (owner decision under `AXIOM_MINIMALITY_POLICY.md` §6), a choice of the one Admissibility law (also owner-level, since it fixes the law), and a reading rule. The current evidence uses many different supplied rules; the deepest assembly obligation (AS0, section 9) is that every part runs on one law, so these proposals come first.

**PS-1, the update (added axiom, "Update").**
> "There is one fixed update. It acts on the joint possibilities of all sites as a unitary map built from finitely many layers of nearest-neighbour gates, covariant under lattice translations and proper cubic rotations. A history is a sequence of updates; the update count orders it."

- *Why.* The axioms doc says "Admissibility is not a dynamics axiom" and lists "update laws" outside the axioms. Every theme PR supplies a tick (the Margolus-type cube tick, #9872, #10016; D4 events, #10094). Without an update there is no T1 time metric, no dispersion (T3), no propagation (T4, T7).
- *What it lets us derive.* TM1's order and metric (with `kinetic_isotropy_primitive`); ST1's `d_t = 1` by construction (one update axis); LZ1 and MT1 dispersion; GA1 transport; GR2 propagation. It also makes the lossless-influence clause (CANDIDATE_LAWS alias CL-1) a property of unitarity.
- *Law choice under PS-1 (proposal PS-1L).* Two candidates are on file. (i) The cube tick: a Margolus-type walk on the two `2^3` tilings, one fermion mode per site, face phase `-1` (the cell of #10016; #9872 states a 24-rotation-covariant tick with isotropic cone speed `1/sqrt3`). (ii) The D4 event ordering: events on the D4 lattice, time along a root, one factor per nearest pair "the same for all 24 root directions" (#10094). Candidate (ii) has `Aut(D4) = W(F4)` and pushes the first Lorentz-violating term to dimension eight for spin at most 1 (#10094), but its runners use "four supplied spinor components per event" (#10130 synthesis), which bears on PS-5. The skeleton does not choose; LW1 compares them.

**PS-2, menu independence of the odds (added sentence to Admissibility).**
> "The probability of a possibility does not depend on which other possibilities are offered with it."

- *Why.* BR1 needs Born weights. `BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09` (scope quoted from its frontmatter): "A menu-independent grading on the scaled rank-one and scalar-identity effects in M_2(C), normalized on every binary and ternary nonzero resolution of the identity, has a unique density-matrix trace form on that scaled domain." Menu independence is the input it names.
- *What it lets us derive.* The trace form `p(P) = tr(rho P)` for the one-site distribution, so Born weights become derived rather than postulated, with `rho` the state PS-1 carries to the site.
- *Alternative.* A stronger, simpler text, if the owner prefers to state Born directly: "The distribution at a site is the Born weight of its possibilities in the state the update carries to that site." This one postulates what PS-2 would derive.

**PS-3, actuality and formation (law choice, with one optional axiom sentence).**
> "One actual configuration exists at every tick. It moves by the support-respecting transport that changes the fewest modes, and among those has maximal entropy. Records never condition the odds. A record forms at a site when the site's actual value has been copied into at least two neighbouring sites."

- *Why.* Record says "Records form." but, per the axioms doc, not "at which site, with what weight, at what rate". The records-born theme (#10124) found that the first three sentences keep Born statistics in every supplied model (#9893, #9930) and left open "Which sites are recorded" (#9995) and set selection (#10054: works "for a three-site redundant record", fails "for a bare two-site copy"). The last sentence is the redundancy rule that #10054's working case suggests.
- *What it lets us derive.* BR1 (agreeing readers, no-signalling marginals, CHSH `2 sqrt 2`, as the supplied models show); TM1's arrow (records accumulate where copies form); the readout context of each record.

**PS-4, the initial condition (added axiom sentence, or a stated scope condition).**
> "A history has a first tick, at which no site carries a record."

- *Why.* `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05` shows the microdynamics is time-symmetric ("The arrow is **not** in the map") and that the arrow comes from a low-record boundary condition; its own boundary: "honest pinning, **not** a from-nothing derivation of the arrow." The README treats the past-hypothesis magnitude as "a scope condition, not a premise". The realized-state primitive excludes it explicitly.
- *What it lets us derive.* TM1(ii): record count increases away from the first tick, so the arrow is the direction of record growth in every history.

**PS-5, site content (no axiom change first; a fallback text if needed).**
- *First attempt, no change.* Build each family's content on cells of qubits. A `2^3` cube carries 8 qubits; owner memory 2026-09-02 says superlattice cells are "never a cost". This stays inside Qubit.
- *Fallback proposed text, only if the cell route fails at a named step:*
> "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`."
- *Why.* #10014 (gauge theme): five modes per site is "the smallest anomaly-free, mass-protected full Spin(2N) Fock content under three stated conditions", and the map note says this "bends the Qubit axiom". The D4 runners also depart from one qubit per site. #10027: on fixed five-mode sites with site-bilinear Spin(10), "every parity-odd excitation is vector class, never the 16" — so even the fallback does not by itself give the 16.
- *What it lets us derive.* CG1's one-family 16 (if a spinor arises; see CG1 (e)); the gauge group via PS-6.

**PS-6, the gauge principle (added axiom, "Frames are local").**
> "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."

- *Why.* #9882: "Block covariance and register size select no gauge group". Logged #10024 (cited in the #10126 synthesis): "the free tick has no local constants of motion away from a decoupled point", so Gauss laws are not obtained from the tick. #9926 obtains exact U(1) and SU(3) Gauss laws only "on a supplied role assignment".
- *What it lets us derive.* Exact Gauss laws commuting with the update (GA1); the gauge group as the frame group of the site content. With one qubit per site the frame group of `M_2(C)` is `U(2)` (inner automorphisms `SO(3)`, lifted to `SU(2)`), consistent with #9882's "abelian or copy U(2)" commutant, which is the gauge group of T0 (section 6). With five modes it is `Spin(10)`, which contains the Standard Model group; breaking to it then belongs to EW1/VC1.
- *Correction, 2026-11-05 (from `LW1.md` B3 and `B5B_DRAFT.md`, pass 1).* On `L_cube` a site is one fermion mode, not a spin. A local frame must keep fermion parity (B5B Lemma G1). The one-site CAR automorphisms are `U(1) x| Z_2` (LW1 B3). The law then allows only the phases: Corollary B5b.1 at one site, and Theorems B5b and B5b-T on an even cell (mode image `U(1)^8`, so `U(1)` per site). So the `U(2)` sentence above does not hold on `L_cube`, and the SU(2) gauge group of T0 does not come from site or cell frames of `L_cube`. It needs more modes per site (PS-5's fallback), a law whose update treats a cell as one site, or structure that emerges at long distance.

**PS-7, the vacuum (law choice; the owner named this decision on 2026-09-03).**
> "The vacuum is the half-filled state of the update's fermion modes."

- *Why.* The 2026-09-03 matter campaign named "which state is the vacuum (empty vs half-filled sea)" as an owner decision (memory scorecard only; the landed note below names "the vacuum question" in its title, and its scope keeps "physical readout" and "field zero-mode projection" distinct, so it does not decide it). On main: `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02` and `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03`. A panel ruling for the half-filled sea exists only in memory ("PANEL ONLY, not on main").
- *What it lets us derive.* VC1's state; the staggered sector (MT1); matter as particle-hole excitations; GR1's energy source.
- *Tension to resolve in VC1/TM1.* Vacuum theme: "Records on change are frozen in the tested half-filled seas (#9876, #10018)". So under PS-7 records do not form in the bare vacuum under that reading, and the arrow (TM1) must come from excitations or from PS-3's copy rule.

**PS-8, mirror gapping term (law choice).**
> "The update includes, on each matter block, the unique singlet interaction of the block's mirror modes, at a coupling large against the hop."

- *Why.* CH1 needs mirrors gapped without breaking the gauge symmetry. #9992 (chirality theme): the block-local quartic gaps the Dirac mirror symmetrically ("symmetric and gapped for g/t >= 8" in finite CT-INT diagnostics) but "releases the light partners". #10022 makes symmetric mirror gapping the condition for its family count.
- *What it lets us derive.* A candidate chiral light sector (CH1) and the family count condition of FL1. Open as stated: the version that does not release the light partners.

**PS-9, the gravitational response law (law choice).**
> "Each site carries six edge registers. Their lengths answer the hinge sum of the actual energy, under the momentum constraint and minimal strain."

- *Why.* The gravity theme (#10128) works with a supplied response law. "Six edges per site give two tensor polarisations on the edge cone" (#9932, #10053); the momentum constraint with minimal strain gives "no extra scalar, vector or ghost at linear order" (#9940); "shift-law adoption" is listed open.
- *What it lets us derive.* GR2's linear limit as in #9940 and GR1's static limit (#10040: "gamma = 1 for a count geometry answering the hinge sum").

**PS-10, the scale (optional; not needed by the skeleton).**
> "The lattice spacing is the Planck length."

- *Why listed.* `G` is "one free scale" (#10055, logged in #10128), and the axioms doc lists "the separate gravity self-consistency question that the framework's natural unit equals the Planck length". Adopting this would fix a dimensionless ratio by fiat, which the scale primitive refuses ("does not assert a/l_P=1"). Recommended reading: keep `G a^{-2}` as a target of GR1, not a specification.

**PS-11, reading odds as frequencies (reading rule).**
> "A statement that the law gives probability one holds in the realized history."

- *Why.* BR1 and every frequency claim (T6, T8) speak of long-run frequencies in one history. The realized-state primitive allows pointwise evaluation only and bans "typical" as a specialization predicate. Without a stated bridge, a law-of-large-numbers statement about the law does not reach the one realized history.
- *What it lets us derive.* Frequencies equal Born weights in the realized history, for every statement proved with law-probability one.

### 3.2 Refinements from part LW1 (owner 2026-11-04)

The pass-1 draft of part LW1 (`LW1_DRAFT.md` on `claude/toe-assembly`, section 6) proposed six refinements of the entries above. On 2026-11-04 the owner ticked all six for this section. The owner then added: "to be clear, we should make sure these dont just smuggle physics". So each refinement was tested before it was recorded. A refinement smuggles physics if it does one of these:

1. It states or fixes something that a part lists as its target.
2. It is open-ended, so a part can add to it to get a result.
3. It settles a downstream physics question by premise.
4. It adds a structure or a constant that its own reasons do not need.

Three passed as written. Three failed one test and were rewritten; the owner chose the rewritten text for each. Each refinement fixes the reading of the entry it names. The entry's text above is kept for provenance.

- **PS-1c, cell covariance (refines PS-1).** "In PS-1 and in Admissibility, covariance under lattice translations and proper cubic rotations is read on cells: the update is covariant under the translations of the lattice of `2 x 2 x 2` cells and under the proper cubic rotations about each cell centre, and its symmetry group acts transitively on sites." Check: passed. It is weaker than PS-1: every update that meets PS-1 meets PS-1c. It fixes no constant. It moves one item onto part LZ1: covariance under unit translations must now be recovered at long distance.
- **PS-3h, half-tick transport (refines PS-3).** "The actual configuration is a configuration of site occupations. It exists at every half-tick and moves once per half-tick, using only the nonzero matrix elements of that half-tick between occupation configurations." Check: passed. It says when the transport acts on a two-layer tick. It adds no constant and no target.
- **PS-3c, copy rule (refines PS-3).** "The actual value of a site has been copied into a neighbouring site at a tick when the law gives probability one that their actual values agree at that tick. A record forms at the end of a tick at each site that carries no record and whose actual value has then been copied into at least two of its neighbours; it locks the site's actual value." Check: passed. It defines "copied", which PS-3 used without a definition. The threshold of two neighbours is PS-3's own. It is not tuned to a result: under it, no record forms in the free vacuum (LW1 Theorem B8), and that is a tension for parts TM1 and VC1.
- **PS-6r, finite quantum links (refines PS-6).** "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs. Link registers carry odds but no actual configuration and no records." Check: LW1's text failed tests 3 and 4. It said "Besides the dressed matter gates, the update may contain one layer of on-link electric gates". That closed list banned plaquette gates by premise, which settles in advance part GA1's question of whether the link sector gives the Yang-Mills energy. It also added an electric layer that its own reasons do not need. The text above keeps only the register algebra. Which gauge-invariant gates the update contains is part of the law choice in LW1, and each gate class carries its own named free constant.
- **PS-7r, which sea (refines PS-7).** "In PS-7, the half-filled sea of a tick is the quasi-free state that fills every one-body mode with quasi-energy in `(-pi, 0)`, quasi-energy read in `(-pi, pi]`. It is defined when `pi` lies in a gap. For the gauged law, the vacuum is the state VC1 builds from this sea; PS-7 does not name it by itself." Check: LW1's text failed test 1. It named "the free one-body tick", but the law is gauged, so that state is not stationary under the law, and the text handed part VC1's target (a stationary vacuum) to the free case. LW1 has also not shown that this filling is the only symmetric, stationary, half-filled choice. So the text above is a choice, stated as one. It is the usual meaning of "sea": a tick with a small step angle `eps` acts as `exp(-i eps H)`, and the filled modes are those of negative `H`.
- **PS-11c, a fixed countable list (refines PS-11).** "A statement that the law gives probability one holds in the realized history, for each statement in this fixed list: (1) every event that names finitely many sites and ticks; (2) for every such event `E` and every pair of rationals `a < b`, the statement that the frequency of the translates of `E`, under the law's translations and ticks, over the windows `[-n, n]^3 x [0, n]` converges as `n -> infinity` to a limit in `[a, b]`." Check: LW1's text failed test 2. Its list ended "every limiting-frequency statement about such events that a part uses", so a part could add the statement it needed. The list above is fixed in advance and is countable. A countable intersection of events of probability one has probability one, so the list is consistent. PS-11 read over all statements is not consistent for any law with no atoms (LW1 Theorem B11).

The same text is in PR #10140, `docs/CANDIDATE_LAWS.md`, subsection "Refinements from part LW1". Parts cite these as "under PS-1c" and so on. Results in `LW1_DRAFT.md` that used the old wording of PS-6r (no plaquette layer, one electric layer) or PS-7r (the free-tick sea as the vacuum) are restated in the distilled LW1.


### 3.3 Owner decisions on LW1, round 2 (2026-11-04)

The same text is in PR #10140. The pass-3 referee of LW1 left four readings for the owner. On the first, the owner wrote: "that was never intended to be only nearest neighbors as in direct connections, but "neighborhood" meaning local influence". The owner then chose the text below.

- **PS-Ar, reading of Admissibility.** "In Admissibility, the nearest-neighbor conditions of a site are the state of its neighbourhood of influence: the sites and links from which the update can reach it within one tick. This region contains the site and its six neighbours." Check: passed. It is the owner's intended meaning. It fixes no target, its extent is definite (one tick of the update), and it adds no structure. Its effect is that Admissibility's content rests on the locality of the update (PS-1). It replaces the shell-only reading, which LW1's distillation showed false for the cube law: two states with the same six-neighbour shell lock the centre with different laws.

The other three are not working-set entries. They are recorded here because they bear on the entries above.
- **Non-factor states: held.** PS-3 selects one transport at factor states only; LW1 claims no more. A rule for non-factor states (PS-3m, transport by central decomposition) is not adopted; its smuggle-check caveat is that it would make "macroscopic labels persist" a premise.
- **"Records form.": left to part TM1.** Under PS-3c no record forms in the free vacuum or in the tracial state. Where and why records form is TM1's open input TM1-i. No reading of the Record axiom is adopted.
- **LW1's target item 3 is restated** in `TOE_ASSEMBLY.md` as existence on `Z^3 x N`, with finite-box laws as restrictions of one history. The closed-box reading is false for any dynamics with boundaries.

### 3.4 Owner decision D1 (2026-11-05)

The same text is in PR #10140. The question put to the owner: on `L_cube`, frames on cells of one-mode sites are only site phases (`U(1)` per site), so the cube law gives no exact `SU(2)` or `SU(3)`; what should PS-5 do? The owner chose: put the fallback text in the proposed axiom update section.

- **PS-5, site content (fallback text, now in the working set).** "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`."
- **The named step.** `B5B_DRAFT.md` (pass 1; the lead checked both proofs line by line): Theorem B5b (each gate unchanged after register changes split at the cell) and Theorem B5b-T (only the whole tick unchanged). Under either, every local frame on an even cell of `L_cube` acts on its modes by site phases. The mode image is `U(1)^8`. Many-body frames are included. Entangled register changes give only operator-valued phases that mix no modes (Theorem 7.3; the case with the even gate is open as B5b-E').
- **Check.** Test 1: passes. The text names no group and no target, and #10014's selector uses "Numbers chosen: none. Observed structure by name: none". Test 2: passes; the text is closed. Test 3: passes. It does not put in the 16; #10027 shows site-bilinear `Spin(10)` on five-mode sites gives "vector class, never the 16". Test 4: passes conditionally. The constant 5 comes from #10014 under its conditions (a)-(c). Condition (b), the Weyl-species reading, is called "an inserted identification, borderline" in that note.
- **What it changes.** This text bends the Qubit axiom. It does so only inside the working set; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. LW1's law `L_cube` has one mode per site, so its site content is superseded for the parts that need the gauge group (MT1, GA1, CG1, CH1). The law on five-mode sites is a new open item, **LW1-5**. It needs a covariant local update, with link registers on which the site frame group acts, that keeps that group exact. #10014 records that "no nearest-neighbour inter-cluster coupling keeps Spin(2N>2) exact" for clusters of one-mode sites. Whether a number-conserving hop on five-mode sites keeps more than `U(5)` is LW1-5's first question. LW1's results that do not use one mode per site (geometry, transport, records, infinite volume) are expected to carry over and are to be checked there.
---


### 3.5 Owner decision on the five-mode law, LW1-5-RQ (2026-11-05)

The question put to the owner: which law should five-mode sites use, `L5-O` (Majorana hop, `so(20)` quantum links, `Spin(10)` exact) or `L5-U` (number-conserving hop, rishon links, `U(5)` exact)? The evidence is in `LW1_5_DRAFT.md`, `LW1_5O_DRAFT.md` and `LW1_5U_DRAFT.md` (pass 1 each; the lead checked the central proofs line by line). The owner chose: **keep both live.** MT1, GA1 and CG1 are developed on both laws until one fails at a named step. No law is fixed in the working set.

Facts on file for the choice:
- `L5-O`. It keeps #10014's condition (a), so D1's reason for 5 holds. Every matter operator is tensor class under any registers, so the 16 is site content and never a matter field (`LW1_5O_DRAFT.md` Theorem K). Pure Gauss singlets need opposite centre classes on the two tilings (Theorem S3), which fails test 4 today. The Standard Model `SU(2)` is an exact gauge subgroup (Proposition T).
- `L5-U`. Pure gauge-invariant states exist for every register sector (`LW1_5U_DRAFT.md` Proposition Σ-U). Local operators carry the `SU(5)` types `5bar`, `10` and `1`. `SU(2)` is exact. At one mode the law is `L_cube` with `S = 1/2`. Under `U(5)` or `SU(5)`, #10014's criteria do not pick `N = 5` (Proposition D), so under `L5-U` the number 5 is an underived datum of PS-5.
- Both laws, and `L_cube`: on a periodic box, no pure, locally gauge-invariant, site-transitive state is half filled (`LW1_5U_DRAFT.md` Theorem F-U and Remark F.1). PS-7r already leaves the gauged vacuum to VC1, so this is VC1's question.

### 3.6 Owner decisions on charged sectors and the zoom's observables (2026-11-06)

Three questions were put to the owner on 2026-11-06, from frozen parts `RCS1.md`, `ZM1.md` and `LZ1.md`.

**R-CS, the charged-sector prescription.** The facts on file: on both five-mode laws fermion parity is a product of local centre elements, so every odd band of a stationary, cell-invariant, gauge-invariant state is flat (`LZ1.md` Theorems 2.1-2.2), and no gauge-invariant odd composite exists (`RCS1.md` Theorem 4). `RCS1.md` states eight candidate prescriptions with four-test verdicts; the cleanest is the Fredenhagen–Marcu straight-string limit R-CS^str (tests P, C, C, C), with the referee's relative parity `χ_tot` as the odd label over parity-sharp backgrounds. The owner chose: **R-CS^str, with `χ_tot` over parity-sharp backgrounds, is a named working candidate for lanes. It is not adopted.** Lanes push RCS-P and MT1-S[R-CS^str] in the VC1 vacuum next; adoption waits until those settle. Nothing enters the working set.

**The zoom's observable class (ZM1-I1).** The question: which observables must a block map reproduce? In locally gauge-invariant vacua, charged two-point functions between distinct coarse sites vanish (`ZM1.md`, referee R-GI). The owner chose: **a lane first builds and four-tests several observable classes;** the owner chooses after that. ZM1-I1 is not worked until then.

**Light species, LZ1-SC.** The owner asked that every owner question be checked by Codex `gpt-6-astra` at max effort before it is put to them. Astra (max) confirmed that RC1's failure comes from the static Gauss background and proposed a separate static class. The owner chose it, into the proposed-axiom-update section (PR #10140, "Owner decision LZ1-SC"): **"LZ1's census of bands with a node is unchanged. Its dispersion clause applies only to bands whose image lies in the orthogonal complement of the tick-fixed vectors, `ker(Ũ−1)^⊥`. Tick-fixed weight is recorded as a separate static class, which LZ1 does not constrain."** LZ1-i is unchanged; R-SC stays a separate open reading.

### 3.7 Owner decision on nearest-neighbour gates, GA1-P-NN (2026-11-06)

The question, checked by Codex `gpt-6-astra` at max effort before it was asked: for laws with link registers, must each nearest-neighbour gate of PS-1 be gauge invariant (NN-b), or only the whole update (NN-a)? A third option, gauge-invariant gates of a law-fixed range `r`, was offered. The owner chose **NN-a**, into the proposed-axiom-update section (PR #10140, "Owner decision GA1-P-NN").

- **GA1-P-NN = NN-a, nearest-neighbour gates (owner 2026-11-06).** "For the named five-mode laws, let `F_x=ΛC⁵` and let `H_ℓ` be the chosen link register. A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. It acts identically outside those factors. Evenness means `[g,P_xP_y]=0`, with `P_x=(-1)^{N_x}`. A nearest-neighbour layer is a locally finite product on pairwise disjoint edge triples. The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`. The factors certify a decomposition of the update. Gauge invariance and cell covariance are required of the complete update only."
- **Check.** Codex `gpt-6-astra` at max effort checked the question before it was asked and wrote this text from the law definitions. Its four tests: test 1 P (it names no species, vacuum, dispersion or coupling); test 2 P (support, parity and finite depth are fixed); test 3 C (it settles GA1-P implementability through the referee's compilation, Proposition C of `GA1_5_REFEREE.md`; it passes as a compilation convention in its own right, not as a way to admit a desired class); test 4 P (it uses the existing matter and link factors). The alternative NN-b (each factor gauge invariant) failed test 4 on PS-6's present reasons. Infinite products have the local-automorphism meaning of `LW1.md` E1.
- **What it changes.** GA1-5's swap layers are admissible: on `L5-U[m]`, every `1≤m≤9`, an exact neutral band moves in the physical sector of a gauge-invariant stationary state (`GA1_5.md` Theorem 6.3 and Proposition S-odd). The band carries no flux and has no Clifford cone; it is not a photon. The flux-carrying band GA1-5-Φ and `L5-O` propagation GA1-5-O stay open. Gauge-variant intermediate factors are allowed as compilation steps, not as separate physical operations.

### 3.8 Owner decision on the zoom's comparison class, ZM1-I1[a] (2026-11-06)

The question, checked by Codex `gpt-6-astra` at max effort before it was asked: which of `ZM1_OBS.md`'s five observable classes must a block map reproduce in ZM1-I1, and with what rate exponent `p`? The owner chose **class (a) with p = 2**, into the proposed-axiom-update section (PR #10140, "Owner decision ZM1-I1[a]"). This replaces the section-3.6 line "ZM1-I1 is not worked until then."

- **ZM1-I1[a], the zoom's comparison class (owner 2026-11-06).** "The following specifies the comparison required in the open statement ZM1-I1[O]. It asserts no existence result. Retain the specified VC1 fine vacuum and the admissible fine updates of ZM1-I1. Retain \(L\ge2\), the Definition-Z map \(\Phi:\mathfrak A_1\to\mathfrak A\), (Z-a), (Z-b), (G1), (G2), and singleton embedding sets. Retain a coarse law \(\alpha_1\) of the stated form and an \(\alpha_1\)-invariant state \(\omega_1\). One coarse tick is \(L\) fine ticks. Constants are independent of the variable data, except for the stated support-radius dependence. For every support radius \(R_0\), take all norm-at-most-one \(A,B\in\mathfrak A_1^G\) supported in that ball. Include their cell-group images. Compare their truncated two-point values at every nonnegative coarse tick and every cell separation \(r=|\beta|_\infty\ge1\). For each fixed \(A,B\), set \(M(r,t)=\sup_{|\beta'|_\infty\ge r}\max_i|F_i^T(A^*,\tau_{\beta'}B;t)|\). Require \(|F_0^T-F_1^T|\le C_{R_0}(r^{-p}+tr^{-p-1})M(r,t)\), with \(p=2\). A zero envelope gives zero values on both sides. No separate one-point matching is imposed."
- **Check.** Codex `gpt-6-astra` at max effort checked the question and wrote this text from `ZM1_OBS.md` (frozen) lines 40-48 and 165-176 and `ZM1.md` lines 361-374. Its four tests: test 1 P (it specifies data, not success); test 2 P (radii and data are quantified); test 3 P (no dispersion or continuum conclusion is assumed; it settles neither LZ1-i, nor T0-start, nor the YM consumers); test 4 C (the relative tail envelope is stronger than the printed absolute-error target of ZM1(a)1, a cost the owner accepts). The exponent: "there exists p>=1" is equivalent to p=1; p=2 is the weakest threshold that meets ZM1(a)1's printed p>=2. It is a success criterion, not a claim that the rate is achieved.
- **What it changes.** ZM1-I1 is now a definite open statement, ZM1-I1[a] with p=2, and lanes may work it. It forces the coarse law to match the correlation length and amplitude of every nonzero invariant tail (`ZM1_OBS.md` Lemma ER). It is not shown impossible or trivial. Classes (b)-(e) stay recorded in `ZM1_OBS.md` and are not adopted.
- *Amendment, 2026-11-07 (frozen item `ZM1I1A.md`; `ZM1.md` Amendment 3).* Under R-form, the frozen trace obstruction proves that the map conditions retained above have no `L≥2` instance. This supersedes the sentence "It is not shown impossible or trivial." Class (a) and p=2 did not cause the obstruction. No replacement definition is adopted here; the owner question on the replacement was checked by Codex `gpt-6-astra` at max effort (`ZM1I1A_OWNER_CHECK.md`).

### 3.9 Owner decision on the zoom's block map, ZM1-INV (2026-11-07)

The question put to the owner, after Codex `gpt-6-astra` at max effort checked it: the frozen item `ZM1I1A.md` proves that the Definition-Z map retained in ZM1-I1[a] has no L≥2 instance on either five-mode law (a unital map with (G1) and (Z-a) forces L=1). Which block-map definition replaces it; is class (a) with p = 2 kept; and do coarse sites carry the same law (R-form)? The owner chose the invariant-algebra map, kept class (a) with p = 2, and confirmed R-form. Recorded in PR #10140, "Owner decision ZM1-INV".

- **ZM1-INV, the zoom's block map (owner 2026-11-07).** "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form). Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants. Use this \(\Phi\) in class (a). Impose no map on charged fields or Gauss generators. Retain class (a) and \(p=2\) as the comparison required of any replacement whose observable and state interfaces make that comparison well-defined. Whether the bound is achieved remains unproved."
- **Scope (lead).** In ZM1-I1[a] this replaces the Definition-Z map \(\Phi:\mathfrak A_1\to\mathfrak A\) and its map conditions (Z-a), (Z-b), (G1), (G2) and singleton embedding sets. The other retained data stand: the VC1 fine vacuum, the admissible fine updates, \(L\ge2\), the coarse law \(\alpha_1\) and the \(\alpha_1\)-invariant state \(\omega_1\), one coarse tick as \(L\) fine ticks, and the relative tail-envelope bound with \(p=2\). The open statement is now ZM1-I1[INV].
- **Check.** Codex `gpt-6-astra` at max effort checked the question and wrote the map text and the class-(a) text (`ZM1I1A_OWNER_CHECK.md`, options 8 and Q2). Its four tests: the invariant-algebra map P P C P (test 3 C: charged-sector consumers need another bridge); retaining class (a) with \(p=2\) P P P C (test 4 C: the envelope forces matching of tail amplitudes and decay parameters, a cost the owner accepted on 2026-11-06). Neither full-algebra obstruction of `ZM1I1A.md` applies directly. Existence is not shown. Astra also gave a new, unrefereed argument that the alternative R-G1EQ still forces L=1 on both laws; it was not chosen.
- **What it changes.** ZM1-I1 is a definite open statement again, ZM1-I1[INV]. The 2026-11-06 decision ZM1-I1[a] stands for its comparison class and \(p\); its retained map conditions are replaced. Charged sectors (R-CS, MT1-S, CG1's 16) get no zoom from this map; they need a separate bridge.

### 3.10 Owner decisions on the chirality wall, SMG1 (2026-11-07)

The questions put to the owner, after Codex `gpt-6-astra` at max effort checked them (`SMG1_OWNER_CHECK.md`): wall W2 (chirality by symmetric mass generation, frozen `SMG1.md`) needs a meaning of "gap", since Lemma F (checked once) shows that under infinite translation covariance, stationarity and clustering no NN-a tick has a spectrum-free neighbourhood of 1 on the vacuum complement; whether W2 keeps the bilinear-protection clause W2.1; and what replaces the refuted light-sector condition W2.4. The owner chose bounded R-GEN, kept W2.1, and kept W2-LIGHT open. Recorded in PR #10140.

- **SMG1-GAP = R-GEN, bounded (owner 2026-11-07).** "For SMG1, fix the certified gate decomposition as part of the supplied data. Write \(g=e^{-iX_g}\), with \(X_g=X_g^*\) and \(\|X_g\|<\pi\). Set \(H_U=\sum_gX_g\), with derivation \(i\sum_g[X_g,A]\). A ground state satisfies \(\omega(A^*[H_U,A])\ge0\) for every local \(A\). A unique gapped ground state has GNS generator with kernel \(\mathbb C\Omega\) and spectrum contained in \(\{0\}\cup[\Delta,\infty)\), where \(\Delta>0\). Tick stationarity remains a separate requirement." Scope: SMG1's rungs only, not every TOE gap. Tests C P C C. It excludes gates with eigenvalue −1; the decomposition must be fixed before the gap is evaluated.
- **SMG1-W2.1 kept (owner 2026-11-07).** "Retain \(G_{\rm SM}\hookrightarrow G\), the 16-component \(D\), and W2.1: \(\operatorname{Sym}^2(D)^G=0\). Retain W2.2–W2.3 and the separately selected replacement for W2.4. W2.1 excludes invariant bilinear masses. The existence of the light 16 remains to be proved." Tests C P C P. It forces \(G\supsetneq G_{\rm SM}\), not \(G=\operatorname{Spin}(10)\).
- **SMG1-W2-LIGHT kept open (owner 2026-11-07).** "Do not adopt W2.4 or W2.4′. Keep W2-LIGHT open. Retain the selected W2.1 and W2.2–W2.3. Require a fully stated replacement before claiming exclusion of every additional light sector." Tests P P P P.
- **Check.** Codex `gpt-6-astra` at max effort wrote these texts and their tests (`SMG1_OWNER_CHECK.md`). It narrowed Lemma F's scope (it excludes no isolated fixed eigenvalue, no gap after removing the whole fixed space, and says nothing on finite rings), and the CH1 amendment was corrected to match.
- **What it changes.** SMG1's rungs read "gap" through the bounded R-GEN, with tick stationarity (FLQ) still to prove. W2 keeps the full 16 with bilinear protection. "Nothing else is light" stays an open criterion. No law or axiom changes.

### 3.11 Owner direction on GB1's generator reading (2026-11-07)

The lead asked which generator reading GB1 should use (R-SUM, R-IA, strict R-GEN widened to GB1, non-strict R3), after a Codex `gpt-6-astra` max check (`GB1_GEN_OWNER_CHECK.md`). The owner answered: "cant we probe each of these? why do we need to pick?" So no reading is adopted, and all four stay live as parallel branches. A choice is needed only when the assembly theorem must name one Hamiltonian per law. On file: strict R-GEN and R3 give bounded generators and no lift (`GB1E.md`, closures R2-R3), so they are closed for the Euclidean transfer route; R-SUM gives the reflection-positive lift on even tori; R-IA gives a positive transfer by construction with one free step. The open probes are the isotropy step (H-class, Y3) under R-SUM and R-IA. Astra's record texts for each reading are kept in `GB1_GEN_OWNER_CHECK.md` for when a choice is needed.

## 4. Plan of the derivation

The argument has four layers. First the **law**: one update, one odds rule, one actuality and formation rule and one initial condition (LW1). The axioms fix the frame (sites, one-site algebra, NN-determined odds, permanent records); the law fixes everything the axioms leave open. Today the law is underdetermined: `ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13` exhibits two covariant NN laws that satisfy the Admissibility contract. So LW1 is a choice among candidates plus a consistency proof, and it is where the owner's specifications enter.

Second, the **long-distance limit**. A block map (ZM1, "the zoom") takes the lattice law to effective laws at coarser scales. Under it the update gives one time axis and Lorentzian signature (TM1, ST1), a common light cone for all species (LZ1), Born frequencies for records (BR1), and a vacuum state (VC1). The YM construction on `claude/ym4d-hard-route` is the template for the hard part of the zoom: it controls a non-abelian block RG at every scale, which is what GA2 needs.

Third, the **content**: fermions with spin and statistics on the qubits (MT1); link registers with Gauss laws for a gauge group fixed by the site content (GA1); the continuum gauge theory at long distance (GA2); a chiral light sector with doublers and mirrors gapped (CH1); the one-family charges (CG1); three families (FL1); electroweak breaking (EW1); and masses and mixings, split into law-level numbers and registered data (FL2).

Fourth, **gravity and cosmology**: the response of the edge registers to energy above the vacuum gives the Newtonian limit (GR1) and, at nonlinear order, Einstein's equations (GR2); with the vacuum energy and the history of record formation they give an FRW history, the cosmological constant and the perturbation spectrum (CS1).

The assembly theorem (section 9) chains these. Its one non-local obligation is coherence (AS0): every part must hold for the same law and the same vacuum. Today almost every result is proved on its own supplied model; the vacuum theme says plainly that none of its results "is a result about the register in `docs/CANDIDATE_LAWS.md`".

---

## 5. The parts

Format per part: (a) main statement; (b) premises and imports; (c) sources, with what each one states, read from the primary text or the map note's verbatim scope; (d) status; (e) open inputs, named where they sit in the statement. "Theme note" means a note carried on a theme PR branch, not on main; such notes have no ledger row.

### LW1. The law and its consistency

(a) **Statement.** There is a law `L = (U, rho_0, Act)` — an update `U` as in PS-1, an initial state `rho_0` with no records (PS-4), and an actuality and formation rule `Act` (PS-3) — such that, for every finite box `Lambda` in `Z^3` and every tick `n`:
1. (*Admissibility*) for every site `x`, the conditional law of the possibility a record forming at `x` locks depends only on the conditions on the six neighbours of `x` [**open input LW1-i**: the plain reading that "conditions" include the joint state of the neighbourhood after the last gate layer], and the map from conditions to law is covariant under translations and proper cubic rotations;
2. (*Record*) each site carries at most one record, and records are permanent;
3. (*Consistency*, restated by the owner 2026-11-04, section 3.3) the law exists on `Z^3 x N`: the update is an automorphism of the quasi-local algebra, the formation rule is a function of the state, and an actual history exists whose one-time laws are the Born laws and whose steps respect the half-tick supports; finite-box laws are the restrictions of that history. [The earlier wording, "the finite-box laws are consistent under inclusion", is false for closed boxes under any dynamics with boundaries (`LW1_REFEREE.md` section 3.G).];
4. (*Uniqueness up to choice*) the specifications S fix `L` up to the named free constants, listed with the parts that read them.

(b) **Premises.** All four axioms; `realized_state_primitive`; `kinetic_isotropy_primitive` (tick graining); PS-1 to PS-4 (proposals). Imports: none.

(c) **Sources.**
- `ADMISSIBILITY_COVARIANT_Q8_CONDITIONAL_LAW_PAIR_BOUNDED_THEOREM_NOTE_2026-08-13` (main). Frontmatter scope: "Two separately declared nearest-neighbor conditional probability laws on the one-site M_2(C) possibility domain satisfy the current Admissibility contract." It ends: "These are exact finite-support law models, not a selection of the physical law". It shows the law is not fixed by the axioms.
- `docs/CANDIDATE_LAWS.md` (main), the three historical clauses, "zero premise weight".
- The supplied three-law register used in theme PRs #10124-#10131 (update, actuality, response law), described in the map-note naming notes.
- #9873 and #9893 (records-born theme notes): the actuality law as supplied; #9893's scope (verbatim in the #10124 map note): a support-respecting fewest-change maximal-entropy transport "keeps Born statistics exactly, gives agreeing readers and CHSH 2 sqrt 2, and is unique, label-equivariant and separable" on supplied Margolus-tick models.
- `CANDIDATE_ASSEMBLY_SOURCE_LINKED_GRAPH_ELEVEN_TARGETS_MINIMAL_DECISION_SETS_BOUNDED_THEOREM_NOTE_2026-09-22` (main): within its declared planning graph, "Formation law has {rule, order law}; clock/rate has {order law}." Planning combinatorics only.

(d) **Status.** No retained row. `docs/audit/data/ledger/ad/admissibility_covariant_q8_conditional_law_pair_bounded_theorem_note_2026-08-13.json`: `bounded_theorem`, `unaudited`. Theme-note evidence on open PR #10124. The statement as a whole: open.

(e) **Open inputs.** LW1-i (reading of "conditions"); LW1-ii (infinite volume); the choice between PS-1L candidates (i) cube tick and (ii) D4 events; whether PS-3's transport stays well defined at infinite volume; the owner's decisions on PS-1 to PS-4.

### LW2. Law revision: the law features behind the frozen negatives (owner 2026-11-08: "Yes, start it")

The lead asked: "Start the law-revision part (growing registers, cube-coupling magnetic layer)?" The owner answered "Yes, start it". The reason: most frozen negatives trace to three features of the live laws `L5-U[m]` and `L5-O[S_+]`. These are fixed finite link registers, invariant algebras with a character (locked or oriented states), and a magnetic layer on one cube tiling. This part finds what a law must change to escape them, and what each change costs. It proposes law texts. It adopts nothing. `docs/MINIMAL_AXIOMS_2026-06-29.md` and the working set are unchanged.

(a) **Statement.** Three open targets.
1. **LW2-MAP, the feature map.** For each frozen negative, the exact law features its proof uses. The negatives are: the trace obstruction (`ZM1I1A.md`), the character obstruction (`GB1Z2L5.md` Theorem 2, `ZM1INV.md` Theorem 2.1), K-INV for odd coarse registers (`KINV.md` Theorem 2), the cube-face factorization (`GB1ISO.md`), the need for an infinite register (`GB1E.md`, `GB1QL.md`), no Clifford node (`RCSPC.md`, `RCSPO.md`), flat odd bands (`LZ1.md` Theorems 2.1-2.2), and no moving chiral 16 (`CG16B/D/S/K.md`, `RCSP16.md`). For each feature, give a variant law without it. Then either name the step where the proof fails, or prove the negative again by another argument.
2. **LW2-G, growing registers.** A family `L[s]` of laws, each one fixed and finite and meeting PS-1, PS-5, PS-6 and NN-a. Decide which frozen positives hold uniformly in `s`: GB1QL's Kogut–Susskind rate, GB1E's lift, GA1-5's neutral band, and SGAP0's gap. Decide which negatives of item 1 fail at large `s`. Also probe a fixed finite register with internal structure (quantum-link or D-theory type) as a separate branch.
3. **LW2-M, a magnetic layer that couples cubes.** The four-tiling layer FP of `GB1ISO.md` §6, or another cube-coupling layer. Give the NN-a check. Prove or refute GB1-CF at finite register. Work ISO-FP.

(b) **Premises.** The working set (section 3), with PS-5, PS-6 and NN-a (section 3.7). ZM1-INV (section 3.9). All four GB1 generator readings stay live (section 3.11).

(c) **Sources.** The frozen parts named in (a), with their amendments; `LW1_5.md`; `GA1_5.md`.

(d) **Status.** Open. Pass-1 lanes: LW2 (items 1 and 2) and LW2M (item 3), each after its prior-work digest.

(e) **Rules.** Each candidate law text is four-tested and goes to the owner. The lanes probe every branch and choose none (section 3.11).

### ZM1. The zoom: block maps and the long-distance limit

(a) **Statement.** For the law `L` of LW1, there are block maps `B_k` (cubes of side `2^k a` in space, `2^k` ticks in time, graining by `c_t=c_s`) and effective laws `L_k` such that:
1. correlations of block observables at separations `r >> 2^k a` computed in `L` equal those of `L_k` up to errors `O((2^k a / r)^p)` for an explicit `p >= 2`;
2. the sequence `L_k` approaches a fixed point or a controlled trajectory whose long-distance content is free massless fields plus the interacting gauge sector of GA2, with every irrelevant term's dimension and coefficient bounded [**open input ZM1-i**: the interacting zoom with gauge fields and matter];
3. the fixed point fits the site content of PS-5 [**open input ZM1-ii**: the image tower].

(b) **Premises.** LW1; `kinetic_isotropy_primitive`; `scale_reference_primitive`. Imports: the block-RG method of the YM route (Balaban's structure as rebuilt on `claude/ym4d-hard-route`), credited.

(c) **Sources.**
- #10092 (Lorentz theme note, `ZOOM_FIXED_POINT_TICK_IS_EXACTLY_PERFECT_ONLY_AT_HISTORY_LEVEL_FINITE_BAND_TICKS_KEEP_LIV_BOUNDED_THEOREM_NOTE_2026-10-26.md`): per the #10125 synthesis, "no such update has an exactly relativistic lowest band on an open momentum set"; a history-level weight "needs an infinite image tower of poles, whether that fits one qubit per site being an owner decision."
- #10098, #10111 (D4 theme notes): the zoom fixed-point fermion "has only real positive poles, but site positivity needs a one-slice buffer"; "The matter dimension-eight coefficient is set by the kernel on the events and falls as 16^-n with rung count n" (#10130 synthesis). Conflict #10111 vs #10112 on finite-rung working rules, recorded in that map note.
- #9926 (gauge theme note): link registers "sit covariantly from zoom three" (title).
- `claude/ym4d-hard-route` (draft PR #10132): the non-abelian block RG; see section 6.

(d) **Status.** No retained row. Open-PR evidence only (#10125, #10130, #10126). Open.

(e) **Open inputs.** ZM1-i; ZM1-ii (image tower versus one qubit per site, an owner question per #10092); the rule that fixes the rung `n` or selects the exact fixed point (D4 synthesis "Open").

### TM1. Emergent time and its arrow

(a) **Statement.** For every history of `L`:
1. the tick index is a total order on events, and the record set `R_n` satisfies `R_n ⊆ R_{n+1}`;
2. under PS-4 (`R_0` empty) and the formation rule of PS-3, on every finite box the law-expected record count is strictly increasing in `n` until saturation [**open input TM1-i**: formation in the vacuum, see (e)], so the arrow is the direction of record growth;
3. the tick length equals the spatial step in the units of `c_t=c_s`;
4. outside named degeneracy classes, no spatial direction is record-monotone in the same sense.

(b) **Premises.** Record (permanence), PS-1, PS-3, PS-4, `kinetic_isotropy_primitive`. Imports: LW1, VC1 (for (2) in the vacuum).

(c) **Sources.**
- `TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03` (main). Its firewall: "The index direction nests for **every** realized history (universal, T2(i)); spatial nesting **fails for some** event-bearing history along **each** spatial axis (existential, T2(ii)); per-history uniqueness of the index as the record-monotone direction holds **only outside** two named degeneracy classes (T2(iii))." It also says the spatial-comparability criterion "is a named CONVENTION". This is items (1) and (4) on a finite exact model.
- `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05` (main). On "1 system qubit + nfrag environment-fragment" with redundant pointer broadcast: "(M) The microdynamics is time-symmetric"; record monotonicity is "a candidate arrow" from a low-record start. Boundary: "**not** a from-nothing derivation of the arrow."
- `kinetic_isotropy_primitive` note: "does not re-axiomatize emergent time".
- Vacuum theme (#10127 synthesis): "Records on change are frozen in the tested half-filled seas (#9876, #10018)".

(d) **Status.** No retained row. `docs/audit/data/ledger/ti/time_axis_is_the_history_index_record_monotone_direction_bounded_note_2026-07-03.json` and `docs/audit/data/ledger/ar/arrow_from_record_formation_past_hypothesis_residual_note_2026-06-05.json`: `bounded_theorem`, `unaudited`. Landed evidence, unaudited, for (1), (4) and a toy form of (2).

(e) **Open inputs.** TM1-i: whether records form in the PS-7 vacuum at all (#9876, #10018 say records on change are frozen there); the formation rate; PS-4.

### ST1. Three space dimensions, one time dimension, Lorentzian signature

(a) **Statement.** At scales `r >> a` the effective theory of `L` has three space dimensions, one time dimension and, for every light field, a quadratic form of signature (3,1): time evolution is generated by a self-adjoint generator with spectrum bounded below on the vacuum sector, and the Euclidean continuation of the tick transfer is reflection positive.

Two routes:
- *Route A (on main).* The anomaly route: `d_t = 1` and signature (3,1) follow from gauge content plus anomaly consistency, under named premises.
- *Route B (under PS-1).* `d_t = 1` holds by construction (one update axis). Signature (3,1) follows from unitarity of the update plus reflection positivity of its Euclidean form [**open input ST1-i**: reflection positivity for the chosen update with interactions], which is the OS step that GA2 and T0 already need.

(b) **Premises.** Lattice (three space dimensions), PS-1. Imports: TM1, LZ1, ZM1; for route A also GA1 and CG1.

(c) **Sources.**
- `ANOMALY_FORCES_TIME_THEOREM.md` (main). Its "Claim scope": "conditional 3+1 derivation. Given (a) the retained nonabelian gauge content on the cubic taste space, (b) the bounded abelian eigenvalue surface with the hypercharge identification declared as premise P-HY, (c) the declared external ABJ anomaly-to-inconsistency premise P-ABJ, (d) the declared opposite-chirality SU(2)-singlet completion premise P-COMP, (e) the staggered chirality grading with the taste-reconstruction premise P-REC, and (f) the declared B-AXIS premise ..., the temporal dimension count is exactly d_t = 1 and the spacetime signature is (3,1)." It adds: "the upper bound (d_t <= 1) is local to the declared B-AXIS boundary." Under PS-1, B-AXIS becomes a property of the update; the other premises remain.
- `BINOM_D_2_EQUALS_TWICE_DMINUS1_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26` and `KLEIN_FOUR_PRODUCT_BZ_CORNERS_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26` (main): each is, by its own claim scope, "the standalone integer-arithmetic identity" or "the standalone finite-group / integer-arithmetic identity". They carry no physical identification.
- #10094 (D4 theme note): "Site-reflection positivity holds for time along an axis and along a root" (verbatim scope, free models).

(d) **Status.** No retained row. `docs/audit/data/ledger/an/anomaly_forces_time_theorem.json`: `bounded_theorem`, `unaudited` (older audits `audited_clean` 2026-05-02, `audited_conditional` 2026-05-05, both pre-reset). Route A: landed evidence, unaudited, conditional on five named premises. Route B: open.

(e) **Open inputs.** ST1-i; for route A, P-HY, P-ABJ, P-COMP, P-REC (see CG1, CH1).

### LZ1. Lorentz symmetry at long distance

(a) **Statement.** For the law `L` and its zoom, there are `c > 0` and `p >= 2` such that, for every light species (fermions, gauge bosons, graviton), the low-momentum dispersion is `E = c|k|(1 + O((a|k|)^p))` with the same `c`; the leading Lorentz-violating operator of each sector has mass dimension at least `4 + p`, with its coefficient computed at one loop or better [**open input LZ1-i**: a mechanism that fixes one common `c` across species]; and the computed coefficients satisfy the time-of-flight, birefringence and threshold bounds.

(b) **Premises.** PS-1 (and PS-1L's choice). Imports: ZM1, MT1, GA1, GA2 (gauge sector O(4) restoration), GR2 (graviton).

(c) **Sources.**
- `EMERGENT_LORENTZ_INVARIANCE_NOTE.md` (main): "bounded structural-dispersion theorem on the cubic Z³ lattice"; "The **load-bearing content is the structural-dispersion core only**"; the Planck-suppressed physical estimate is "non-load-bearing".
- `EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03` (main), frontmatter scope: "Conditional unit-hop KS model on the coarse cubic lattice", with "exact cell-phase dispersion and Taylor coefficients -1/12, +1/360, isotropic leading phase velocity in supplied units"; "no band taste splitting or physical clock."
- Lorentz theme (#10125 synthesis): #9872 a supplied 24-rotation-covariant tick "with an isotropic cone of speed 1/sqrt3 (isotropy numerical)"; #9913 "no symmetry fixes the ratio of two species' dressed speeds; for its supplied link law the electron cone lies below the photon cone by kappa alpha, kappa -0.17 to -1.01"; #10092 as in ZM1; tests #10090 ("time-of-flight margins of at least 6.8 orders"), #10091, #10093 (a pure flowed-proton beam "2.2 combined sigma from raw Xmax moments" in a toy shower model; the map note records that #10093's own scope says 1.6 sigma while its results show pulls up to 2.4).
- D4 theme (#10130 synthesis): #10094 "the first Lorentz-violating term of free spin 0, 1/2 and 1 fields is at dimension eight"; for the graviton the W(F4) count is "3 at p^4 against O(4)'s 2; the extra one is birefringent on shell" (verbatim scope); #10096 "A unitary walk on the same events keeps only the 48-element stabiliser and has a dimension-six term (table only)."

(d) **Status.** No retained row. `docs/audit/data/ledger/em/emergent_lorentz_invariance_note.json` and `.../em/emergent_lorentz_invariance_at_the_dirac_point_and_the_taste_census_bounded_theorem_note_2026-09-03.json`: `bounded_theorem`, `unaudited`. Landed evidence (free dispersion) and open-PR evidence (#10125, #10130). Open as stated.

(e) **Open inputs.** LZ1-i (#9913 shows symmetry alone does not fix it; a dynamical attractor is needed — main has `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`, not read for this skeleton); the gap between the Euclidean D4 weight (dimension eight) and a unitary walk (dimension six, #10096); the graviton's extra birefringent `p^4` kernel on D4; the one-loop dimension-six coefficient on the cube tick (#10125 "Open").

### BR1. Quantum readout: Born weights from records

(a) **Statement.** Under `L` with PS-2, PS-3 and PS-11: for every record-forming context realized in a history, with central decomposition `{P_k}` supplied by the record's copy structure,
1. the one-site odds have the trace form `p(P) = tr(rho P)`, with `rho` the state the update carries to the site [from PS-2 via the binary-ternary theorem];
2. the long-run frequency of record value `k` in the realized history equals `tr(rho P_k)` [**open input BR1-i**: PS-11 or a derivation of it];
3. joint records follow the Born law of the joint pointer; two readers of one record agree; single-time marginals do not signal;
4. bare records without a pointer copy are not readable as path knowledge (interference survives), consistent with the canonical record principle (inter-sector coherence is never registered).

(b) **Premises.** Qubit, Admissibility, Record, `realized_state_primitive`; PS-2, PS-3, PS-11. Imports: LW1, TM1.

(c) **Sources.**
- `BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09` (main), scope quoted in PS-2. It ends: "The grading, eligible-menu family, physical registration, and selected density matrix remain explicit inputs or outputs of a supplied law".
- Records-born theme (#10124 synthesis): "One actual configuration moved by a transport that uses only nonzero elements of each half-tick, changes the fewest modes and, among those, has maximal entropy, with records that never condition the odds, keeps the Born law at every half-tick in the supplied models. It gives no Zeno effect, full fringes, agreeing readers, no signalling of single-time marginals and CHSH 2 sqrt 2 (#9893, #9930 ...)". "Bare two-time records depend on the distant setting (total variation 0.2183 in the supplied model ...); after a pointer copy the two-time law equals the Born law of (pointer, outcome)." Failed: "Proportional shortfall switching does not keep Born on one Margolus block (#9893)". "History actuality has no decoherence functional for the chiral weighting, which has no known tick form (#10054)."

(d) **Status.** No retained row. `docs/audit/data/ledger/bo/born_form_from_binary_ternary_scaled_projector_frame_lift_bounded_theorem_note_2026-08-09.json`: `bounded_theorem`, `unaudited`. Theme notes on open PR #10124. Items (1) and (3)-(4): landed and open-PR evidence on supplied finite models. Item (2): open.

(e) **Open inputs.** PS-2 (menu independence) or its derivation from Admissibility; BR1-i; which sites record (#9995: "untested by any readable distribution"); set selection (#10054); a tick form for the chiral weighting (#10054); the three registered obligations' readout parts (FL2).

### MT1. Matter carrier: fermions, statistics and spin

(a) **Statement.** Under `L`, on the vacuum of VC1, there are local excitations that (1) have exchange sign `-1` (Fermi statistics), built from the site qubits by a local encoding, with no added site content [**open input MT1-i**: PS-5's first attempt]; (2) transform as spin 1/2 under the rotation group that emerges at long distance; (3) per cell, carry enough modes for one family's chiral content (a 16 of `Spin(10)`, or the Standard Model multiplet) [**open input MT1-ii**].

(b) **Premises.** Lattice, Qubit, PS-1, PS-5, PS-7. Imports: LW1, ZM1, VC1.

(c) **Sources.**
- `FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-02` (main), frontmatter scope: "exact Pauli calculations verify Bravyi-Kitaev superfast-encoding relations, stabilizer ranks, bounded string-operator syndromes, and fermionic-sign diagnostics on the named open cubic blocks and tori ... These results do not construct one framework Admissibility law, couple the marker sectors to the fixed BKSF embedding, supply state preparation or dynamics, or establish an infinite-volume particle or phase."
- `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-02` (main), scope: "Conditional finite signed-hopping comparisons: exact uniform cube ladders, exact half-filled cube uniqueness and 4-cubed global Cauchy-Schwarz certificate; ... no physical sector selection is derived."
- #10016 (families theme note), verbatim scope: on the cube-tick cell "the cell rep is spinorial, spin (from the velocity matrices) times taste"; "the four tastes are E + E of O (one E per chirality), never 1 + 3".
- #10104 (D4 theme note): "With one mode per event, nearest-neighbour root hops and the stated cells, no spin-1/2 arises" (#10130 synthesis).
- #10014, #10023, #10027 (gauge theme notes), as quoted in PS-5.

(d) **Status.** No retained row. `docs/audit/data/ledger/fi/finite_bksf_sign_and_superlattice_marker_census_bounded_theorem_note_2026-09-02.json` and `.../ha/half_filling_kinetic_energy_selects_the_staggered_flux_sector_bounded_theorem_note_2026-09-02.json`: `bounded_theorem`, `unaudited`. (1)-(2): landed and open-PR evidence on supplied finite models. (3): open.

(e) **Open inputs.** MT1-i (one law that produces the superlattice role pattern and the BKSF embedding together; the 2026-09-03 sweep reported the law "DESIGNED" there); MT1-ii (the 16 per cell; #10027 shows site-bilinear `Spin(10)` on five-mode sites gives the vector, not the 16).

### GA1. Lattice gauge structure

(a) **Statement.** Under `L` with PS-6: (1) every link carries a register on which a compact group `G` acts, with an exact Gauss law at every site commuting with the update; (2) `G` is the frame group of the site content of PS-5 [**open input GA1-i**: the group that the chosen content gives, and its relation to `SU(3) x SU(2) x U(1)/Z_6`]; (3) face (plaquette) loops are gauge invariant and complete; (4) the classical energy of the link sector tends to the Yang-Mills energy at small fields.

(b) **Premises.** Lattice, Qubit, PS-1, PS-5, PS-6. Imports: LW1, MT1.

(c) **Sources.**
- `NATIVE_GAUGE_CLOSURE_NOTE.md` (main), Claim scope: "the nonabelian part of the native cubic gauge-structure surface only: exact `Cl(3)` on the cubic taste space, exact `su(2)` from the Clifford bivectors, exact cubic parity/chiral anticommutation for the nearest-neighbor hopping surface, and the already audit-ratified graph-first selected-axis structural `su(3)` theorem. This note excludes the abelian eigenvalue surface, anomaly-complete `U(1)_Y`, electroweak matching, matter-completion labels, Wilson dynamics, and downstream phenomenology."
- `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`, `GRAPH_FIRST_SELECTOR_DERIVATION_NOTE.md` (main): an `su(3) + u(1)` commutant on the taste cube once a graph axis is selected. Algebra on the taste space; not a gauge field.
- Gauge theme (#10126 synthesis): #9924 "Definite stationary links give classical Coulomb colour, a flat vacuum and one-body matter; estimates against measurement then exclude them, so links must carry odds"; #9926 exact U(1) and, "with three colour rishons per end, an exact SU(3) Gauss law, on a supplied role assignment, with supplied label-blind hops and rishon sites carrying no records"; #9968 "a supplied plaquette law has complete gauge-invariant loops; its classical energy tends to Maxwell and Yang-Mills at O(B_f^2) ... but in a single-loop diagnostic the bare coefficients miss the light cone at small registers"; #9882 "Block covariance and register size select no gauge group"; #10010 "the two-layer cube tick, on two modes per site, has exact internal algebra so(4), with no corner su(4)".
- `COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-14` (main): finite codes; its scope ends "no all-axiom model, universal box no-go, partial-hole law or physical gauge-theory identification."

(d) **Status.** No retained row. `docs/audit/data/ledger/na/native_gauge_closure_note.json` and `.../gr/graph_first_su3_integration_note.json`: `positive_theorem`, `unaudited` (both were `audited_clean` in May 2026, before the reset; the note header's "already audit-ratified" is not current status). Landed algebraic evidence; open-PR model evidence (#10126). Open as stated.

(e) **Open inputs.** GA1-i; Gauss laws from the update itself (logged #10024: none for the free tick), which PS-6 would supply; how colour registers, given that #9926's rishon sites "carry no records".

### GA2. Continuum gauge theory at long distance (the Yang-Mills plug-in)

(a) **Statement.** Let `G = prod_i G_i` be the gauge group of GA1. For each simple factor `G_i` with negative one-loop beta coefficient, the framework's gauge sector at scales `a << r << Lambda_i^{-1}` agrees with continuum `G_i` Yang-Mills with the matter of CG1, at the running coupling `g_i(r)`, up to errors `O((a/r)^p) + O(g_i(r)^4)` [**open input GA2-i**: a convergence-rate form of T0]. For the abelian factor, the corresponding statement holds as an effective lattice theory at scales above `a`, with no `a -> 0` limit required, because the lattice spacing is physical (`scale_reference_primitive`). The continuum objects exist as OS-reconstructed Wightman theories (imported from T0 and its extension).

(b) **Premises.** PS-1, PS-6. Imports: GA1, ZM1, LZ1, CH1 (for chiral matter), and T0 (section 6).

(c) **Sources.** `claude/ym4d-hard-route` (draft PR #10132): GOAL.md states T0 and the interface UV-CT; FINISH.md (2026-11-03 evening): "every clause of T0 is now written as an implication"; "Existence is not proved." PR #10132's body: "Most of what the attempts label derived has not been read from outside." The second route, `claude/ym4d-proof-draft` (draft PR #10114), runs the soft-kernel route. Gauge theme #9968 (classical YM limit of a supplied plaquette law).

(d) **Status.** No retained row (no ledger rows for branch notes). Open; research-stage draft-PR evidence.

(e) **Open inputs.** GA2-i; bridges Y1-Y5 of section 6; matter in the RG (T0 is pure gauge).

### GB1. The lattice gauge bridge (owner 2026-11-07: "Both, layer first")

(a) **Statement (skeleton, to be proved rung by rung).** Fix a gauge group `G` and a framework law `L` with an exact local `G` frame group (PS-6, PS-6r; GA1). There are a zoom rung `n` and a readout `Φ` of the owner's ZM1-INV form (a unital injective cell-covariant exponentially local *-homomorphism on gauge-invariant observables) such that the framework's link sector, restricted to the gauge-invariant algebra, equals a named lattice gauge theory `LGT_G` on `Z^3` with its time step: link Hilbert space, Gauss law, electric and magnetic operators, and update or transfer stated exactly. The target form is chosen by the lane and justified: either Hamiltonian (Kogut–Susskind type on `Z^3`, with the framework tick as a Trotter product `e^{-iτ_B H_B}e^{-iτ_E H_E}`) or Euclidean (Wilson type on `Z^3 × Z`, via a positive transfer matrix). Then the known construction results for `LGT_G` apply to the framework through `Φ`. The ladder is `G = Z_2`, then `U(1)`, then `SU(2)`. For each rung the part records either the theorem or the first failing step, exactly.

(b) **Premises.** PS-1, PS-6, PS-6r; the owner decisions NN-a (3.7) and ZM1-INV (3.9). Imports: GA1 (`GA1_5.md`, `GA15PHI.md`), GA2_Y2 (`GA2_Y2.md` Theorem N: no finite register carries an invertible link exactly covariant under a group with infinite image), ZM1 and `ZM1I1A.md` (the trace obstruction), LW1_5 Proposition T (exact SU(2) subgroups with Gauss laws on both five-mode laws). Literature imports are allowed when re-proved on the framework (owner 2026-10-26, 2026-10-29).

(c) **Sources.** Section 6 (bridges Y1-Y5); GA2_Y2 (T0-start[G], T0-rate, Y2-W); the YM4D contract `GOAL.md` on `claude/ym4d-hard-route` (T0, T1, NT1, NT2) and the Sussman–Alpoge complete account CA-I `3.1:thm-main` at commit `31a47c543775` (indexed in `library/sa-index/ca-full/` on that branch). Literature to digest: Kogut–Susskind Hamiltonian lattice gauge theory; Creutz's transfer matrix for the Wilson action; Z_2 lattice gauge theory and the toric code (Kitaev; Wegner; Fradkin–Shenker); quantum link models and D-theory (Horn; Orland–Rohrlich; Chandrasekharan–Wiese; Brower–Chandrasekharan–Wiese); Balaban; Sussman–Alpoge.

(d) **Status.** New 2026-11-07. Skeleton only. Prior-work digest `prior/GB1.md` first, then a Mini pass-1 lane.

(e) **Open inputs.** GB1-Z2, GB1-U1, GB1-SU2 (the three rungs); GB1-FORM (Hamiltonian or Euclidean target, with reasons); GB1-H (the hand-off: which hypotheses of CA-I `3.1:thm-main`, Wilson SU(2) on 4D Euclidean `Z^4`, the bridge delivers and which it cannot, for example the 4D Euclidean form if time is emergent, hypercubic symmetry (Y3), and the exact Wilson action (Theorem N)).

### CH1. Chirality: a gauged chiral light sector

(a) **Statement.** Within `L` there is a local lattice theory, invariant under `G`, whose light spectrum at scales `>> a` is exactly the chiral content of CG1 (one Weyl 16, or the Standard Model multiplet, per family), with every doubler and every mirror gapped at scale `~ 1/a` [**open input CH1-i**: symmetric mass generation for the mirrors without releasing light partners], no extra light charged state, gauge anomalies cancelling, the gauge field kept massless [**open input CH1-ii**: a local gauged measure], and the measure reflection positive.

(b) **Premises.** PS-1, PS-5, PS-6, PS-8. Imports: MT1, GA1, ZM1; it feeds GA2 (the gauged measure) and FL1.

(c) **Sources.**
- `CL3_FRAME_FREE_AMBIENT_CHIRAL_GRADING_NO_GO_NOTE_2026-06-02` (main), `no_go`. Exact Claim scope: "on the grade-1 vector subspace of the one-site `Cl(3,0)` / `M_2(C)` carrier, no frame-free Spin(3)/Pin(3)-equivariant ambient Clifford operation induces a grade-1 endomorphism that anticommutes with `Gamma_chi = (2/3)J - I`; the anticommuting L4 family exists, but it requires a chosen singlet axis and a free doublet vector, while frame-broken Lattice, momentum, dynamical, and sector-factorization routes remain open." It bars one ambient one-site construction only; it names the other routes open.
- Chirality theme (#10131 synthesis): "**Answer: not obtained.** No kept result constructs a consistently gauged chiral light sector in 3+1D with its mirror and doublers removed." Failures: #9863 ("net cone chirality at 0 and at pi equals minus W3, and products of coins and shifts have W3 = 0"), #9895, #9896, #9908 ("needs unbounded range"), #9971, #9985 ("smoothed far layers induce a cutoff-scale photon mass in 4D slab models at constant layer fields"), #10056, #10060, #9911 and #9992 (mirror gapping "releases vector-like doublers"), #10030, #10042, #10064, #10073, #10072. Survives: #10049 "The overlap of the cube walk's Euclidean kernel has exact Ginsparg-Wilson chirality without doublers; its chiral content is abelian, Euclidean and not a walk sector"; #10052 "3^4 Standard Model anomaly tests are diagnostics"; #10004 "The 16-Weyl toy has Z16 index 0 under the unitary Z4s searched and an inconclusive mirror gap"; 1+1D rotor results #9927, #9939 (logged). Open: #10085 "the U(1) four-field coefficient does not vanish like p^2 at L <= 24".
- D4 theme: #10099 "the slab is vector-like"; #10112 Ginsparg-Wilson "and the zero mode only in the limit".

(d) **Status.** No retained row. `docs/audit/data/ledger/cl/cl3_frame_free_ambient_chiral_grading_no_go_note_2026-06-02.json`: `no_go`, `unaudited` (scope as quoted). Open-PR evidence (#10131, #10130). Open.

(e) **Open inputs.** CH1-i (PS-8 plus a mechanism keeping the light partners chiral; candidates on file: far-wall gapping of mirror plus pi pair, #10073; persistence of the mirror gap, #10004); CH1-ii (#10085); non-abelian existence and reflection positivity of the overlap construction (#10049 "Open"); whether partners surviving as propagator zeros are acceptable (#10030).

### CG1. Charges of one family

(a) **Statement.** The light chiral content of one family is the Standard Model one-generation multiplet — `(3,2)_{1/6}`, `(3bar,1)_{-2/3}`, `(3bar,1)_{1/3}`, `(1,2)_{-1/2}`, `(1,1)_{1}`, and optionally `(1,1)_0` — equivalently the 16 of `Spin(10)` branched under `SU(3) x SU(2) x U(1)`; with the hypercharge normalisation fixed by the structure (the `1:(-3)` ratio) and by anomaly cancellation [**open input CG1-i**: the physical identification P-HY], and the right-handed completion fixed by the law [**open input CG1-ii**: P-COMP].

(b) **Premises.** PS-5, PS-6. Imports: MT1, GA1, CH1.

(c) **Sources.**
- `HYPERCHARGE_IDENTIFICATION_NOTE.md` (main): "bounded/conditional name-free algebra. The source-side claim is only the structural (2,3)+(2,1) decomposition, the unique traceless block-scalar ratio +1:(-3), and the normalized (+1/3,-1) two-block pattern after a supplied scale choice. No physical naming or charge-readout table is theorem content."
- `LEFT_HANDED_CHARGE_MATCHING_NOTE.md` (main), Claim scope (narrowed): "the structural eigenvalue ratio `α : β = 1 : (-3)` ... forced by tracelessness on the `(6+2)` state count"; "SM hypercharge identification via `Q = T_3 + Y/2` is **explicitly out of scope**".
- `CL3_SM_EMBEDDING_THEOREM.md` (main): a supplied Clifford construction on `(C^2)^⊗3`.
- Gauge theme: #9894 "A rung-1 cell with a supplied internal action and supplied masses shows the 1:1:3:3 multiplicity pattern of one generation, without chirality"; #10014, #10023, #10027 as in PS-5.
- `ANOMALY_FORCES_TIME_THEOREM.md`: consumes P-HY and P-COMP as declared premises.

(d) **Status.** No retained row. `docs/audit/data/ledger/hy/hypercharge_identification_note.json`, `.../le/left_handed_charge_matching_note.json`, `.../cl/cl3_sm_embedding_theorem.json`: `bounded_theorem`, `unaudited`. Landed structural evidence; open-PR model evidence. Open.

(e) **Open inputs.** CG1-i; CG1-ii; the spinor 16 rather than the vector 10 (#10027; the #10126 synthesis lists three escapes: "a site-count change, deconfined spinons outside the finite-site theorem, or a Spin(10) not generated by site bilinears").

### FL1. Three generations

(a) **Statement.** Under `L`, the number of light chiral families is `N_f = 3`, as a law-level output (invariant over the law-admissible family) [**open input FL1-i**: the carrier structure that fixes the count; **FL1-ii**: symmetric mirror gapping, shared with CH1-i].

(b) **Premises.** PS-1, PS-5, PS-8. Imports: MT1, CH1, CG1.

(c) **Sources.**
- `CL3_TASTE_GENERATION_THEOREM.md` (main), "Theorem (representation-theory, scope-narrowed)": on the abstract `C^8 = (C^2)^⊗3` with the tensor-position `S_3` action, "The Hamming-weight-1 sector (hw=1) ... transforms as the 3-dimensional permutation representation `A₁ + E` of S₃." The 2026-06-12 narrowing made it "purely abstract".
- #10016 (families theme note): on the cube-tick cell "the four tastes are E + E of O (one E per chirality), never 1 + 3"; "no symmetry protects a family triplet" (title).
- #10022 (families theme note), verbatim scope: "Conditional. Take 5 modes per site with Spin(10) on one 16 per family ..., CL-1's cell and cube tick with the copy mass, and N families repeated by one uniform rule. ... If the mirror 16bars are gapped keeping Spin(10) and at least one turn, the light vertex phase w^(4Nq) must be 1, so N = 0 mod 3, and the smallest N is 3. ... N = 3 is necessary, not shown sufficient: symmetric mirror gapping (SMG) is cited, not established."
- #10059: "the cell slab wall holds at most two opposite-handed copies"; #10071 "Family-blind rules keep U(3), so a unique term gives no family label" (#10129 synthesis).
- The #10129 synthesis: "Three families are not derived."
- `N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24` (main) consumes the count.

(d) **Status.** No retained row. `docs/audit/data/ledger/cl/cl3_taste_generation_theorem.json`: `bounded_theorem`, `unaudited` (pre-reset `audited_clean`, then `audited_decoration`). Landed abstract representation theory; open-PR evidence of a necessary condition (#10022). Open.

(e) **Open inputs.** FL1-i (which carrier: the staggered taste cube with its hw=1 triplet, or the cube-tick cell with E + E; the two sources use different carriers, see section 8); FL1-ii; reconciling #10022 with the later slab notes #10063, #10065 (not carried; the #10129 synthesis says "the sources do not reconcile this with #10022").

### EW1. Electroweak breaking and the Higgs sector

(a) **Statement.** Under `L` on the vacuum of VC1, the gauge group `G` breaks at long distance to `SU(3) x U(1)_em` (from `Spin(10)` or from the GA1 group through the Standard Model group), with three massive weak bosons and a massless photon, a scalar excitation with the Higgs quantum numbers or a composite equivalent, and the weak scale `v` either law-level (in units of `a^{-1}`) or registered data [**open input EW1-i**: the breaking mechanism].

(b) **Premises.** PS-5, PS-6, PS-7. Imports: GA1, GA2, CG1, VC1.

(c) **Sources.** #10129 synthesis: "Logged Higgs, neutrino and weak-scale routes need supplied content, or fail against measured mixing or couplings (#10062, #10082)." No kept result addresses EW1 directly.

(d) **Status.** No retained row. Open.

(e) **Open inputs.** EW1-i; the hierarchy `v a` (a pure number of order `1e-17` if `a` is near the Planck length).

### FL2. Masses and mixings

(a) **Statement.** For each Standard Model mass ratio and mixing parameter `X` (charged-fermion mass ratios, CKM's four parameters, PMNS, neutrino mass splittings, `theta_bar`, and the Koide `Q` of charged leptons): either `X` is law-level, invariant over the law-admissible family, and the law computes it with an error bound; or `X` is registered data of the realized state, and the part shows which record registers it (guardrail G3) [**open input FL2-i**: a family label; **FL2-ii**: a hierarchy mechanism; **FL2-iii**: a CP source without order-one `theta_bar`]. In particular `|theta_bar| < 1e-10` is law-level.

(b) **Premises.** `realized_state_primitive` (counterfactual test); PS-2, PS-3. Imports: FL1, EW1, VC1, BR1 (registration), CH1.

(c) **Sources.**
- `docs/audit/data/derivation_obligations.json` (main), three `open_gate` targets: "Derive from the retained framework chain whether the physical charged-lepton matter action counts the K/CPT orbit or holomorphic pair once rather than counting each sector or channel."; "Derive ... that the physical charged-lepton readout is the fixed-locus density class, identity-read in h-units as the eta angle, with no extra normalization or transport factor."; "Derive whether the charged-lepton K/CPT occupancy carrier is the same physical channel that controls the quark determinant readout and whether that identification forces arg det(M_q)=0."
- Families theme (#10129 synthesis): #9922 "Translation-invariant terms give family-diagonal mixing"; #9958 "at most two spurion distances"; #9960 "The family copy form fits charged-lepton Koide Q but gives the same Q in every sector and one hierarchy step; quarks exclude it"; #10075 "no vacuum tested gives three hierarchical families with a T-odd phase"; #10068 "A kept family-fixing time-reversing antiunitary forces J = 0"; #10047 "A turn-charged order parameter gives J and theta_bar together unless a Nelson-Barr block is supplied"; #9948 zoom-3 characters "keep theta_bar real at renormalisable order with J nonzero; dimension five leaks"; #10086 "a charge on the orders needs Peccei-Quinn: Nelson-Barr's quality problem, not a solution".
- Measure/dial discipline (framework-refresher): `r = 1/2` is a distinguished setting, "not a banned topic"; quark and neutrino `Q` values are evidence against a universal `r = 1/2`.

(d) **Status.** No retained row. Three registered `open_gate` obligations. Open-PR evidence of failures and conditional CP results. Open.

(e) **Open inputs.** FL2-i, FL2-ii, FL2-iii; the three registered obligations; which parameters pass the counterfactual test at all.

### VC1. The vacuum

(a) **Statement.** Under `L` and PS-7, there is a translation- and rotation-invariant stationary state `omega_0` of the update (the vacuum) such that (1) it is stable: gapped against mirrors and doublers (CH1), massless gauge and graviton modes; (2) the matter of MT1 is its particle-hole excitations; (3) its energy density relative to the law's zero is computed and enters GR1 and CS1 [**open input VC1-i**: the zero of energy]; (4) the record behaviour in `omega_0` is fixed (whether records form there; TM1-i).

(b) **Premises.** PS-1, PS-7. Imports: LW1, MT1, BR1.

(c) **Sources.**
- `MATTER_ABOVE_THE_HALF_FILLED_SEA_ODD_AND_EVEN_DENSITIES_AND_THE_VACUUM_QUESTION_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03` and `RECORD_CONSERVING_INTERACTION_KEEPS_THE_STAGGERED_SECTOR_AT_HALF_FILLING_BOUNDED_THEOREM_NOTE_2026-09-03` (main), with `HALF_FILLING_KINETIC_ENERGY_SELECTS_THE_STAGGERED_FLUX_SECTOR...` (scope quoted in MT1).
- Vacuum theme (#10127 synthesis): "The supplied half-filled sea sources zero, a Planck-scale value, or a mass-dominated value, never the measured density (#9880)"; "A fixed 4-volume per record cancels every vacuum term proportional to 4-volume on the supplied frustum carrier but leaves Lambda to initial data, lost matter energy and split kicks (#9900)"; "Records on change are frozen in the tested half-filled seas (#9876, #10018)".

(d) **Status.** No retained row. `docs/audit/data/ledger/ma/matter_above_the_half_filled_sea_odd_and_even_densities_and_the_vacuum_question_conditional_bounded_theorem_note_2026-09-03.json` and `.../re/record_conserving_interaction_keeps_the_staggered_sector_at_half_filling_bounded_theorem_note_2026-09-03.json`: `bounded_theorem`, `unaudited`. Landed and open-PR evidence on supplied models. Open.

(e) **Open inputs.** PS-7 (owner); VC1-i; TM1-i.

### GR1. Newtonian gravity

(a) **Statement.** For static, slowly moving excitations of `omega_0`, at scales `>> a`, the response of the geometry registers defines a potential `phi` with `nabla^2 phi = 4 pi G rho_E`, where `rho_E` is the energy density above the vacuum [**open input GR1-i**: the source is energy, not record count or particle number]; test bodies accelerate as `-nabla phi` independent of composition [**GR1-ii**]; and `G a^{-2}` is computed or shown registered [**GR1-iii**].

(b) **Premises.** PS-1, PS-7, PS-9. Imports: VC1, MT1, ZM1, LZ1.

(c) **Sources.**
- `NEWTON_DERIVATION_NOTE.md` (main), status line: "open_gate. ... the residual gate is the *external-field* generator-invariant inertial-mass step on a persistent compact-object family." Its claim: "on the retained ordered-lattice family, Newtonian mass scaling is selected when" four principles hold; "This is a family-level statement only."
- `G_NEWTON_WEAK_FIELD_RESPONSE_BOUNDED_CLOSURE_NOTE_2026-05-10_gnewtonG3` (main): the weak-field response form follows "once the canonical coupling `V_grav = m*phi` is granted. The canonical coupling remains an admitted input".
- `ENERGY_PRODUCT_AND_TEST_BODY_LAW_ABOVE_THE_HALF_FILLED_SEA_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03` (main), scope: "Conditional real Slater preparations and finite FFT response arithmetic. ... No physical test-body law is derived."
- Gravity theme (#10128 synthesis): "gamma = 1 for a count geometry answering the hinge sum (#10040)"; "Sourcing edges from the actual configuration radiates on every hop (#9929)"; "G (one free scale, #10055, logged)".
- `CANDIDATE_LAWS.md`: under a lossy averaging operator the continuum approximation "has a screening length proportional to epsilon^(-1/2)", so GR1's `1/r` needs lossless influence (automatic under PS-1's unitarity).

(d) **Status.** No retained row. `docs/audit/data/ledger/ne/newton_derivation_note.json`: `open_gate`, `unaudited`; `.../en/energy_product_and_test_body_law_above_the_half_filled_sea_conditional_bounded_theorem_note_2026-09-03.json` and `.../g_/g_newton_weak_field_response_bounded_closure_note_2026-05-10_gnewtonG3.json`: `bounded_theorem`, `unaudited`. Landed and open-PR evidence on supplied models. Open.

(e) **Open inputs.** GR1-i, GR1-ii, GR1-iii; PS-9.

### GR2. General relativity at long distance

(a) **Statement.** At scales `L >> a`, the response of the edge registers to the energy-momentum of excitations obeys Einstein's equations `G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu}` up to corrections suppressed by `(a/L)^2`; at linear order there are exactly two tensor polarisations at speed `c` and no extra scalar, vector or ghost; PPN `gamma = beta = 1`; gravitational collapse forms horizons with a regular exterior slicing [**open input GR2-i**: the nonlinear limit; **GR2-ii**: refinement together with collapse; **GR2-iii**: the shift law].

(b) **Premises.** PS-1, PS-9. Imports: GR1, LZ1, TM1, ZM1, VC1.

(c) **Sources.**
- Gravity theme (#10128 synthesis). Supported: "cube edges alone give no hinge sum; six edges per site give two tensor polarisations on the edge cone in a finite linearised census (#9932; #10053)"; "With a matter momentum constraint and minimal strain there is no extra scalar, vector or ghost at linear order but with an instantaneous shift (#9940). A wave shift is causal at linear order (#9952)"; refinement "a glued split is unitary and local in a 1D toy" (#9935), "In 3D it needs a one-sided collar and 2:1 balance (#9941)"; collapse "on the isotropic frustum carrier a stationary point exists at every tick and zero size is never reached" (#9921), "A revised shift law gives an attracting exterior in spherical vacuum runs (#9976)". Failed: #9929, "Sea entanglement counts bonds, not area (#10020)", #9964. Its answer: "Partly: in linearised continuum models, static or spherical toys and 1D register toys. Refinement and collapse together are not shown on the lattice."
- `LATTICE_GRAVITON_KERNELS_ONE_TT_CONE_DEWITT_CLOSURE_AND_INDUCED_BUBBLE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-10-18` (main), scope: "Universal determinant polynomial and finite curvature controls; conditional supplied-model mathematics and explicitly finite controls."
- `LORENTZIAN_REGGE_CONTINUATION_AND_THE_ATTRACTIVE_GEOMETRY_PHASE_SIGN_BOUNDED_THEOREM_NOTE_2026-10-21` (main), scope: "Finite square-root branch tracking, endpoint derivative and quadratic-kernel diagnostics on supplied Kuhn and coned D4 carriers; source/action sign comparisons are conditional, and full nonlinear action reality, continuum EH matching and the null limit remain open."
- D4 theme: #10100 "Hinge-sum gravity carries over at linear order with an extra frame doublet and graviton birefringence"; #10102 "Under a Lorentzian reading one doublet component is a ghost; a metric-only edge reading removes the pair".

(d) **Status.** No retained row. `docs/audit/data/ledger/la/lattice_graviton_kernels_one_tt_cone_dewitt_closure_and_induced_bubble_seagull_bounded_theorem_note_2026-10-18.json`: `bounded_theorem`, `unaudited`; `.../lo/lorentzian_regge_continuation_and_the_attractive_geometry_phase_sign_bounded_theorem_note_2026-10-21.json`: `open_gate`, `unaudited`. Linear order: open-PR evidence. Nonlinear: open.

(e) **Open inputs.** GR2-i, GR2-ii, GR2-iii; "the dark constant made in collapse" (#10128 "Open"); the D4 frame doublet's graviton coupling.

### CS1. Cosmology

(a) **Statement.** Under `L` from the initial condition PS-4: (1) the large-scale geometry is FRW; (2) the cosmological constant `Lambda` is computed in units of `a^{-2}` or shown registered [**open input CS1-i**]; (3) a mechanism (inflation or another) gives a nearly scale-invariant adiabatic spectrum with tilt `n_s` within current bounds [**CS1-ii**]; (4) a dark-matter species with its abundance, or the absence of one, follows from the law [**CS1-iii**]; (5) the baryon asymmetry follows from the law's CP and baryon-number violation [**CS1-iv**]; (6) `N_eff` follows from FL1.

(b) **Premises.** PS-4, PS-7. Imports: GR2, VC1, TM1, MT1, CG1, FL1, FL2.

(c) **Sources.**
- `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md` (main): "Separates the exact identity `Lambda = lambda_1(S^3_R)` from the still-bounded numerical value of `R` / `Lambda`." (Its header also says "current ledger `effective_status: audited_conditional`"; the ledger now says `unaudited`. See section 8.)
- Vacuum theme (#10127 synthesis): the `Lambda` results quoted in VC1; "a first-slab rule gives a closed-top minimum 1e117 to 1e119 above the measured value"; "supplied curvature-squared inflation with the rules' reheating gives 0.9617, an estimated 4.1 sigma below ACT (#9918)"; "Born split times are white inherited offsets and supply no seed (#10007)"; "none of the four places searched in the update's existing structure protects a dark species (#10005 ...)". "No abundance is set by the rules."
- `N_EFF_FROM_THREE_GENERATIONS_THEOREM_NOTE_2026-04-24` (main).

(d) **Status.** No retained row. `docs/audit/data/ledger/co/cosmological_constant_spectral_gap_identity_theorem_note.json`: `positive_theorem`, `unaudited`; `.../n_/n_eff_from_three_generations_theorem_note_2026-04-24.json`: `positive_theorem`, `unaudited`. Open-PR evidence of failures in supplied models. Open.

(e) **Open inputs.** CS1-i to CS1-iv; "a rule that supplies dephasing or a horizon-correlated seed; a conserved number for a dark species; the size of Lambda" (#10127 "Open").

---

## 6. Where the Yang-Mills construction plugs in

**What T0 is.** From `GOAL.md` on `claude/ym4d-hard-route` (draft PR #10132): T0 is "the existence clause of the Clay problem without the mass gap, for SU(2) first: a non-trivial quantum Yang-Mills theory on R^4 whose Euclidean correlations satisfy the Osterwalder-Schrader axioms strongly enough to reconstruct a Wightman theory", with "full O(4) Euclidean invariance, reflection positivity, symmetry and reality, and clustering", for "the tr(F^2) sector of Wilson SU(2)". The Wightman reconstruction is in scope. Non-triviality is NT1 (dynamics) and NT2 (leading-order perturbative agreement and one-loop running across scales). The milestone T1 is a limit "along a coupling trajectory the proof chooses". FINISH.md, 2026-11-03: "Existence is not proved."

**Which TOE part needs it.** GA2. Through GA2 it also feeds LZ1 (Lorentz symmetry of the gauge sector comes from O(4) restoration plus OS reconstruction), ST1 route B (reflection positivity of the Euclidean tick transfer), EW1 and FL2 (running couplings), and CS1.

**What GA2 imports from T0.**
1. Existence of the continuum SU(2) theory as an OS/Wightman theory (T0 proper); then SU(N), through the planned extension along the Sussman-Alpoge work.
2. O(4) restoration (T0's clause O7) and clustering (O8, O9): the gauge-sector half of LZ1.
3. NT2's running clause: the one-loop running of `g_r`, which is GA2's running-coupling clause.
4. The scale-by-scale bounds of the hard core (the UV-CT interface, CT1-CT4: bounds "independent of a and L"). GA2 consumes these more than the `a -> 0` limit itself, because the framework's lattice spacing is physical (section 5, GA2 (a)).

**The lowest rung fits T0's gauge group.** With one qubit per site and PS-6, the frame group of `M_2(C)` is `U(2)`, with non-abelian part `SU(2)` (consistent with #9882's "abelian or copy U(2)" commutant). So the framework's simplest gauge sector is a pure SU(2) lattice gauge theory on `Z^3` with the update as time evolution. That is T0's theory up to bridges Y1-Y3 below, and it is the natural first rung of the ladder (the process review's "easier analogue" rule).

*Correction, 2026-11-05.* The first sentence does not hold on `L_cube`. There a site is one fermion mode, and its exact frames are `U(1)` (`B5B_DRAFT.md`; section 3.1's PS-6 correction). On five-mode sites (section 3.4) `SU(2)` is an exact gauge subgroup of both live laws, with its own Gauss law: `LW1_5U_DRAFT.md` Proposition T for `U(5)`, and `LW1_5O_DRAFT.md` Proposition T for `Spin(10)`. Their link registers are finite quantum links (PS-6r), not group-valued Wilson links. `GA2_Y2_DRAFT.md` (pass 1) proves that no finite register carries an invertible link that is exactly covariant under a group with infinite image (Theorem N). This holds at every scale of the law (Corollary N5). So the clause "That is T0's theory up to bridges Y1-Y3" is false for every PS-6r law, and Y2 can hold only as universality of gauge-invariant correlators. The statement the TOE needs from the YM programme is **T0-start[G]** with **T0-rate**, given in that file's FINISH block: T0's bounds and conclusions from any start in the hard core's own inductive class at small coupling, with constants independent of the start. `G` is `SU(5)` for `L5-U` and `SO(10)` for `L5-O`. The first open item is Y2-W: whether `L5-U`'s fixed register reaches small coupling at any scale.

**Bridges from the framework to T0's hypotheses (open inputs of GA2).**
- **Y1, Euclidean form.** The framework's SU(2) link sector, with the update as transfer, has a Euclidean representation on `Z^3 x Z` (or on D4 events) with a local, gauge-invariant action `S_fw`, reflection positive in time.
- **Y2, the RG domain.** `S_fw` lies in the domain of the hard-core block RG (Balaban's class as rebuilt on the branch), or the hard core's bounds extend to `S_fw`. T0 is stated for the Wilson action.
- **Y3, lattice symmetry.** T0's O(4) argument starts from hypercubic invariance of `Z^4`. The framework has cubic symmetry in space, a time axis, and `c_t=c_s` graining, but no lattice symmetry exchanging time and space. Two options: prove O(4) restoration from `O_h x Z_2(time)`, or use the D4 event set, whose automorphism group `W(F4)` contains the hypercubic group and which holds site-reflection positivity "for time along an axis and along a root" (#10094).
- **Y4, matter.** T0 is pure gauge. The TOE needs the RG with the chiral fermions of CH1, which is outside T0's statement. CH1-ii (a local gauged measure) is the entry point.
- **Y5, convergence rate (GA2-i).** The TOE needs "framework correlators at scale `r` equal continuum correlators up to `O((a/r)^p)`". T0 as stated gives existence of a limit, not a rate. The hard core's uniform bounds are the natural source of a rate; the statement "T0-rate" should be added to the interface.

---

## 7. Dependency graph, roots and order of attack

### 7.1 Edges (`X -> Y` means Y imports X)

- LW1 -> ZM1, TM1, ST1, BR1, MT1, GA1, VC1
- ZM1 -> LZ1, MT1, GA2, GR1, GR2, ST1
- TM1 -> ST1, BR1, GR2, CS1
- VC1 -> TM1 (formation in the vacuum), MT1, EW1, FL2, GR1, GR2, CS1
- MT1 -> GA1, CH1, CG1, VC1, LZ1, GR1, CS1
- GA1 -> GA2, CH1, CG1, LZ1, EW1, ST1 (route A)
- GA2 -> LZ1 (gauge sector), ST1 (route B, reflection positivity), EW1, FL2, CS1
- T0 (external, `claude/ym4d-hard-route`) -> GA2
- CH1 -> GA2 (Y4), CG1, FL1, FL2, ST1 (route A, P-REC)
- CG1 -> FL1, EW1, CS1, ST1 (route A, P-HY, P-COMP)
- FL1 -> FL2, CS1
- EW1 -> FL2
- BR1 -> VC1, FL2
- LZ1 -> ST1, GR1, GR2
- GR1 -> GR2
- GR2 -> CS1
- FL2 -> CS1 (baryon asymmetry)

The edges MT1 <-> VC1 and TM1 <-> VC1 form two-way couplings: the vacuum is a state of the matter modes, and the arrow needs formation in that vacuum. They are resolved by proving VC1 and MT1 together as one part pair, and TM1 after VC1(4).

### 7.2 Roots

- **LW1** is the root of everything. It holds the owner's specification choices (PS-1 to PS-4, and PS-1L).
- **ZM1** is the technical root of every long-distance statement.
- **T0** is the external root of GA2.
- **PS-5 to PS-9** are root decisions for MT1, GA1, VC1, CH1 and GR2.

### 7.3 Order of attack

Following `SCIENCE_WORKFLOW.md` §7 ("attack the step it is most likely to die on first") and the process review (easier analogue first, draft-distil-review per part):

1. **LW1 with the owner.** Put PS-1 to PS-9 to the owner. Without one law, every later part is proved on a different supplied model and AS0 cannot hold. Then prove LW1's consistency for the chosen law.
2. **CH1 (hardest; most likely place for the law to die).** Ladder: 1+1D rotors (#9927, #9939) -> 2+1D -> the 3+1D wall with PS-8. Kill first: test whether PS-8's mirror term releases light partners on the chosen carrier (it does in #9911, #9992).
3. **GA2 in parallel**, through T0 on its own branch. The TOE side adds Y1-Y5; the lowest rung is the framework's own SU(2) link theory.
4. **FL1**, which is coupled to CH1 through #10022's symmetric-mirror-gapping condition.
5. **ZM1 and LZ1**: the interacting zoom, and the common-cone mechanism (LZ1-i).
6. **GR2 then GR1**: nonlinear response with refinement and collapse (GR2-i, GR2-ii); the energy source (GR1-i).
7. **MT1, GA1, CG1, VC1**: these have the most landed structure and lowest risk once PS-5 to PS-7 are fixed.
8. **BR1 and TM1**: well developed on finite supplied models; open inputs are PS-2, PS-3, PS-11 and TM1-i.
9. **EW1, then FL2, then CS1**: they read everything above.

### 7.4 The hardest open parts

1. **CH1, chirality.** A gauged chiral light sector in 3+1D with mirrors and doublers removed. The #10131 synthesis: "**Answer: not obtained.**" It feeds GA2, CG1, FL1 and FL2.
2. **GA2, continuum gauge theory.** Rests on T0, itself not proved ("Existence is not proved"), plus bridges Y1-Y5, of which Y4 (chiral matter in the RG) meets CH1.
3. **FL1 with FL2, three families and their masses and mixings.** The #10129 synthesis: "Three families are not derived"; no family label, no hierarchy mechanism, no CP source free of order-one `theta_bar`.

Close behind: **GR2** (nonlinear GR; "Refinement and collapse together are not shown on the lattice") and **LW1/AS0** (one law for all parts).

---

## 8. Contradictions and tensions found in the sources

Each item quotes both sides. None is resolved here.

1. **Note headers versus the ledger.** `NATIVE_GAUGE_CLOSURE_NOTE.md` cites "the already audit-ratified graph-first selected-axis structural `su(3)` theorem"; `docs/audit/data/ledger/gr/graph_first_su3_integration_note.json` has `effective_status: unaudited` (its `audited_clean` of 2026-05-22 predates the reset). `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md` says "current ledger `effective_status: audited_conditional`"; its row says `unaudited`. The ledger has zero retained rows of any kind.
2. **Three generations: memory scorecard versus theme PR versus carrier.** The memory scorecard (2026-09-03 delta) says "three generations DERIVED from BZ corners on P-KIN/P-SD". The #10129 synthesis says "Three families are not derived." `CL3_TASTE_GENERATION_THEOREM.md` was narrowed in 2026-06 to abstract representation theory (the hw=1 triplet `A1 + E` on an abstract `C^8`). #10016 says that on the cube-tick cell "the four tastes are E + E of O ..., never 1 + 3". The older lane and the newer one use different carriers (staggered taste cube versus Margolus cube-tick cell), so they are not a direct logical contradiction; but the scorecard's "DERIVED" does not match either primary text.
3. **Family count within the families theme.** #10022 gives `N = 0 mod 3` under symmetric mirror gapping; the #10129 synthesis says later slab notes #10063 and #10065 "report no count when the mirror carries the light copy's charge, as on static slabs", and "the sources do not reconcile this with #10022."
4. **D4 finite-rung rules.** The #10130 map note records that #10111 and #10112 "report different finite-rung working rules" (its corrections entry 1).
5. **#10093's sigma.** The #10125 PR body: "#10093's own scope says 1.6 sigma but its results show pulls up to 2.4."
6. **CL label collision.** Theme notes call their update, actuality and response laws "CL-1, CL-2, CL-3"; `docs/CANDIDATE_LAWS.md` uses the same aliases for the lossless-influence, record-removal and conservation clauses. Every map note says so. The memory index also points to "candidate laws CL-1..CL-7 in #9829"; #9829 is closed and main's register has three entries.
7. **Bound-site records.** The #10124 corrections section, entry 2: "Exclusion of bound sites from records: justification contradicted (#9970, by #9995)".
8. **Arrow "derived" versus "pinned".** The memory scorecard (2026-09-03 evening): "time/cosmology PARTIAL (axis+arrow derived ...)". The arrow note's own boundary: "**not** a from-nothing derivation of the arrow"; it is a pinning modulo the past hypothesis.
9. **Arrow versus vacuum.** TM1 needs records to accumulate; the vacuum theme reports "Records on change are frozen in the tested half-filled seas (#9876, #10018)", and the half-filled sea is the leading vacuum candidate (PS-7).
10. **Colour registration.** The memory scorecard reports a probe in which a non-abelian Gauss law has no record-pattern solutions ("colour cannot be registered"). This was not found on main for this skeleton. #9926 obtains an exact SU(3) Gauss law on rishon sites "carrying no records". The two are about different objects (record patterns versus link operators), but GA1 has to say how colour registers.
11. **One qubit per site.** The Qubit axiom gives `M_2(C)` per site. #10014 (five modes, "bends the Qubit axiom"), the D4 runners ("four supplied spinor components per event ... departs from one qubit per site") and #10092 (the image tower, "an owner decision") each step outside it. PS-5 collects this.
12. **Skill versus note.** The framework-refresher skill names `CL3_CHIRAL_CUBE_WILSON_HOP_DOUBLING_FORECLOSED` as the "Canonical exemplar" of a no-go. Its claim scope is "the standalone lattice-perturbation-theory fact that on a single SU(3) Wilson link ... returns a single fundamental Casimir factor `C_F` ... NOT `2 C_F`"; it is not about chirality or doublers. (Tooling mismatch, not a science conflict.)
13. **Planning scorecard staleness.** `origin/ai/execution:TOE_SCORECARD.md` (2026-09-11) counts 4,700 ledger rows; the ledger now has 5,950. The memory scorecard was last verified at `b8c9d9d819` (2026-09-13). Neither is current.

---

## 9. The assembly theorem

**Coherence obligation AS0.** All parts are proved for one law `L` (LW1), one zoom (ZM1) and one vacuum `omega_0` (VC1). A part proved on a different supplied model counts as evidence for its statement, not as a proof of it for `L`.

**Theorem (assembly; conditional).** Let **S** be the owner-approved subset of PS-1 to PS-11. Assume LW1, ZM1, TM1, ST1, LZ1, BR1, MT1, GA1, GA2, CH1, CG1, FL1, EW1, FL2, VC1, GR1, GR2 and CS1 hold as stated in section 5, for one law `L` (AS0), from **A + P + S** and T0 (with Y1-Y5). Then T1-T9 of section 2.2 hold:

- **T1** from TM1 (1)-(3), with VC1 (4) for formation in the vacuum.
- **T2** from ST1: three space dimensions from Lattice; `d_t = 1` from PS-1 (route B) or from route A's premises; signature (3,1) from LZ1 and the reflection positivity supplied by GA2 and ST1-i.
- **T3** from LZ1: matter and photon sectors from ZM1 and MT1, the non-abelian gauge sector from GA2's O(4) restoration, the graviton from GR2.
- **T4** from GA1 (group, Gauss law, loops) and GA2 (continuum theory with running couplings).
- **T5** from MT1 (statistics and spin), CH1 (chirality, doublers and mirrors gapped, anomaly cancellation), CG1 (charges) and FL1 (three families).
- **T6** from EW1 (breaking) and FL2 (each parameter law-level and computed, or registered and its record named).
- **T7** from GR1 (Newtonian limit) and GR2 (Einstein's equations, two polarisations, PPN, horizons).
- **T8** from BR1.
- **T9** from VC1 (vacuum) and CS1 (FRW, `Lambda`, spectrum, dark matter, baryon asymmetry, `N_eff`).

*Proof.* Each target item is the conjunction of the named parts' conclusions, evaluated on the one law `L`. The imports in section 7.1 form a directed graph whose only cycles are MT1-VC1 and TM1-VC1; these are proved as joint parts (MT1 with VC1, then TM1 after VC1 (4)). Taking the parts in the order of section 7.3, each part's premises are axioms, primitives, members of **S**, T0, or conclusions of parts earlier in the order. AS0 makes the conclusions refer to the same `L` and `omega_0`, so their conjunction is a statement about one theory. Each target item in T1-T9 is then read off as listed. ∎

The theorem is only as strong as its weakest part. Today every part is open or holds only on supplied models; the ledger has no retained row; **S** is empty; T0 is not proved. The theorem says what proving the parts would give, not that any part is proved.

---

## 10. How each part is worked (from PR #10138 and the process review)

For each codenamed part: one long session writes the full argument with no brevity limit; a second session, on the other provider, distils it to a minimal proof and lists every definition it had to infer; a fresh session of the first provider reads the whole distilled part line by line, once. Status (proved or outstanding) lives in the part's text. A part freezes when it passes its review, and reopens only on a `wrong` signal or when an input it reads changes. Published work enters as a credited input, labelled `unchecked` until rebuilt here. No computer-assisted step counts as a proof step; a runner can refute or guide. Before each part, record the literature search once in this folder (`SCIENCE_WORKFLOW.md` §2 rule 9) and find the easier analogue (for GA2, the framework's own SU(2) link theory; for CH1, 1+1D).

## 11. The walls in the Sussman–Alpoge form (2026-11-07)

The owner asked how the TOE would attack its big walls if it followed the principles of the Sussman–Alpoge Yang–Mills work. Those principles, as the YM4D lead session summarised them from their README and repository (2026-11-07): one well-posed theorem per target, stated in standard mathematics; extend an existing research programme instead of starting from scratch; climb a ladder of models and prove the hard trick on the simplest rung first; Claude drafts at volume, Codex distils, one referee, freeze once, batched dated fixes; contracts first (an outline of theorem statements and proof assignments, with every imported hypothesis explicit); a domain expert steers. This file already follows the drafting and freezing rules. What it lacked per wall was the first three. This section supplies them. Each wall gets its own assembly outline `<CODE>_OUTLINE.md` (statements and proof assignments), written by the first lane before any rung lane, and a prior-work digest per rung. The literature named below is to be fetched and checked by each lane; none of it is load-bearing until re-proved on the framework.

**W1. The gauge bridge, GB1** (feeds GA2). Target theorem: the framework's gauge-invariant link sector equals a named lattice gauge theory, so Balaban's and Sussman–Alpoge's results apply (part GB1). Programme: Kogut–Susskind and Wilson lattice gauge theory, quantum links and D-theory, Balaban, Sussman–Alpoge. Ladder: Z₂, U(1), SU(2). Status: pass-1 lane running.

**W2. Chirality and the 16, SMG1** (feeds CH1, CG1, MT1-ii, FL1). Target theorem: a local finite-register law on `Z^3`, NN-a, with exact on-site symmetry `G ⊇` the Standard Model group, whose light sector is one Weyl 16 of Spin(10) with every mirror and doubler gapped, by symmetric mass generation (SMG) rather than symmetry breaking. Programme: interacting classification and SMG (Fidkowski–Kitaev's Z₈ for Majorana chains; Wang–Wen's 1+1D chiral constructions; the 3+1D Spin(10) proposals and the anomaly conditions that permit SMG of the 16). The four frozen routes (LW1_5 Amendment 3) and RCS-P16 show that the live laws give no moving chiral 16 directly; SMG is the route the literature uses. Ladder: rung 1, SMG of 8 Majorana chains in 1+1D on a framework tick (Fidkowski–Kitaev re-proved natively, with a gap and a symmetric unique ground state); rung 2, a 1+1D chiral theory with mirrors gapped; rung 3, 2+1D; rung 4, the 3+1D 16. First rung to work: rung 1.

**W3. A common light cone, CN1** (feeds LZ1, ST1, GR). Target theorem: under the owner's zoom (ZM1-INV), species that interact through a common gauge field have speed differences that flow to zero. Programme: Chadha–Nielsen's "Lorentz invariance as a low-energy phenomenon" and its successors. The frozen counterexample LZ1-i (two free neutral species keep different Clifford speeds) is the free rung's answer; interactions are the escape. Ladder: rung 1, two species coupled to one U(1) field in a solvable or perturbative-with-bounds model; rung 2, the framework's own gauge layer; rung 3, every species. First rung to work: rung 1.

**W4. Breaking to the Standard Model, BK1** (feeds EW1, VC1, CG1). Target theorem: a VC1 vacuum of a live law in which the exact U(5) or Spin(10) is realised, in gauge-invariant (FMS) terms, as SU(3)×SU(2)×U(1) with the 5 split as 3+2. Programme: lattice Higgs complementarity (Fradkin–Shenker, Osterwalder–Seiler), Elitzur's theorem, FMS. Ladder: an abelian Higgs rung, then SU(2) Higgs, then the 3+2 split. Waits for W1's first rungs.

**W5. Three families, FAM1** (feeds FL1, FL2). No established programme derives the number of families. The frozen FL1 shows none of the 2³ cell, taste structure or #10022's turn argument fixes `N_f`. Kept as an open research wall; no lane until W2's rung 2, because #10022 ties family number to mirror gapping.

Order of attack: W1 (running), then W2 and W3 in parallel (each from rung 1), then W4, then W5. GR is worked by the scale-ladder gravity session and is not listed here.

**Law revision, LW2 (2026-11-08).** Positive results came where an established programme was ported. Most negatives trace to three features of the live laws: fixed finite registers, invariant algebras with a character, and a magnetic layer on one cube tiling. Part LW2 (section 5) finds what a law must change to escape them. It serves W1 (the register limit and isotropy) and W3's zoom (K-INV).
