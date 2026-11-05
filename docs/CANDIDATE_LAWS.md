---
claim_id: candidate_laws
claim_type: meta
claim_scope: "Historical proposal register with reported owner quotations unverified in this review; zero premise weight. Explicit scalar models are conditional choices, not a new foundation admission channel."
---

# Candidate law proposals and provenance

Claim type: meta.

This register preserves two proposed working clauses and the approval quotations reported by the original branch. The underlying conversation record was not independently retrieved in this review. Their approval provenance is therefore **unverified here**; this does not assert that approval did not occur elsewhere. Neither this register nor a quoted approval changes the foundation registry.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md), [policy section 6](audit/AXIOM_MINIMALITY_POLICY.md#6-explicit-owner-approval-for-axioms-and-primitives) and `docs/audit/data/axiom_premise_nodes.json` control premise admission. This register has zero premise weight. Any use of the clauses below must remain an explicit conditional model choice unless supported through those authorities. Admissibility does not specify time evolution, scalar averaging, source weights, a floor algorithm or a conservation functional. Identical one-site algebras do not assign an equal numerical drain to every record.

## Reported lossless-influence clause (historical alias CL-1)

> "Influence passes from site to site without loss."

The original branch reports the owner saying: "If you are confident decision 1 is correct (that there is no loss in influence) then lets go with it and build on it."

The mathematical comparator is a supplied scalar averaging operator. For its particular attenuated resolvent, the resolvent I-(1-epsilon)A has small-momentum denominator epsilon+(1-epsilon)|k|^2/6+O(|k|^4); its continuum approximation has a screening length proportional to epsilon^(-1/2). This is conditional model mathematics, not a theorem that every kind of loss screens or that physical gravity requires this rule. A finite scaling comparison does not classify every coarse-grained dynamics. The clause alone does not determine the update rule or coefficients.

## Reported record-removal clause (historical alias CL-2)

> "When a record forms, its qubit leaves the flow: the network is permanently short that site's share."

The original branch reports "I am good with decision 2" and the explanation "the record removes the qubit which is a drain in a way". These quotations have the same unverified-here provenance boundary.

The [companion finite-model note](CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md) supplies distinct scalar equations and examines their consequences. It does not derive those equations from the clause. Equal drains, prescribed boundaries, scalar wave mass weights, seeds and packet readouts are separate supplied choices. Fixed-source linear responses superpose, but a finite-point proxy per source depends on source position. Uniform-boundary hole and equilibrium-pinning identities have explicit hypotheses. The local floor equation does not justify the old enlarged irreversible clamping region. Undamped torus traces do not establish a lasting stationary field, and finite scalar packet delays do not establish universal free fall.

## Reported pending conservation proposal (historical alias CL-3)

The original pending wording was: "When a record forms, the share its qubit takes out of the flow is held by the record, not destroyed; the total is unchanged."

A chosen conserved source can satisfy a Ward identity in a supplied model. That does not derive record conservation or identify the conserved functional. These remain open conditional choices. This entry does not certify adoption or an additional premise.

Exact original wording and numerical records are preserved in `archive/record_flow_review_2026_10_18/MANIFEST.json`. Broader exclusion, uniqueness and physical-interpretation claims from that history are deferred rather than relabeled as theorems. No audit standing is assigned here.

## Proposed axiom update: TOE working set (2026-11-04)

The owner approved the TOE assembly skeleton (draft PR #10139, `TOE_ASSEMBLY.md` section 3) on 2026-11-04 and gave this direction in the session that wrote it: "im good with the skelleton proposal but for 'adopt' we put them in the proposed axiom update section until we have the full theory figured, then we move them into the real axioms as simply as possible."

These entries are working premises for drafting the TOE parts. Like the rest of this register, they have zero premise weight. They do not change the minimal axioms, policy section 6 or `axiom_premise_nodes.json`. A part that uses an entry names it, for example "under PS-1". When the full theory is in place, the entries that are actually used go to the owner for approval of the exact axiom wording, in the simplest form that still does the work. Entries that no part needs are dropped, and entries that can be merged are merged. The labels PS-n are kept distinct from the historical CL aliases above.

- **PS-1, update.** "There is one fixed update. It acts on the joint possibilities of all sites as a unitary map built from finitely many layers of nearest-neighbour gates, covariant under lattice translations and proper cubic rotations. A history is a sequence of updates; the update count orders it." The choice of law, the cube tick or D4 events, is open and is settled in part LW1.
- **PS-2, menu independence.** "The probability of a possibility does not depend on which other possibilities are offered with it."
- **PS-3, actuality and formation.** "One actual configuration exists at every tick. It moves by the support-respecting transport that changes the fewest modes, and among those has maximal entropy. Records never condition the odds. A record forms at a site when the site's actual value has been copied into at least two neighbouring sites."
- **PS-4, initial condition.** "A history has a first tick, at which no site carries a record."
- **PS-6, local frames.** "The internal frame of each site's possibilities is local. Each nearest-neighbour link carries a register that transports frames between its two sites. The update is unchanged when the frame at one site and the registers on its links are changed together."
- **PS-7, vacuum.** "The vacuum is the half-filled state of the update's fermion modes."
- **PS-11, realized frequencies.** "A statement that the law gives probability one holds in the realized history."

Not in the working set:
- PS-5, the five-mode site content, is a fallback only, used if building on cells of qubits fails at a named step.
- PS-8, mirror gapping, is a law to test inside CH1.
- PS-9, the gravity response law, is a law to test inside GR1/GR2.
- PS-10, lattice spacing equal to the Planck length, is not adopted.

### Refinements from part LW1 (owner 2026-11-04)

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

### Owner decisions on LW1, round 2 (2026-11-04)

The pass-3 referee of LW1 left four readings for the owner. On the first, the owner wrote: "that was never intended to be only nearest neighbors as in direct connections, but "neighborhood" meaning local influence". The owner then chose the text below.

- **PS-Ar, reading of Admissibility.** "In Admissibility, the nearest-neighbor conditions of a site are the state of its neighbourhood of influence: the sites and links from which the update can reach it within one tick. This region contains the site and its six neighbours." Check: passed. It is the owner's intended meaning. It fixes no target, its extent is definite (one tick of the update), and it adds no structure. Its effect is that Admissibility's content rests on the locality of the update (PS-1). It replaces the shell-only reading, which LW1's distillation showed false for the cube law: two states with the same six-neighbour shell lock the centre with different laws.

The other three are not working-set entries. They are recorded here because they bear on the entries above.
- **Non-factor states: held.** PS-3 selects one transport at factor states only; LW1 claims no more. A rule for non-factor states (PS-3m, transport by central decomposition) is not adopted; its smuggle-check caveat is that it would make "macroscopic labels persist" a premise.
- **"Records form.": left to part TM1.** Under PS-3c no record forms in the free vacuum or in the tracial state. Where and why records form is TM1's open input TM1-i. No reading of the Record axiom is adopted.
- **LW1's target item 3 is restated** in `TOE_ASSEMBLY.md` as existence on `Z^3 x N`, with finite-box laws as restrictions of one history. The closed-box reading is false for any dynamics with boundaries.
