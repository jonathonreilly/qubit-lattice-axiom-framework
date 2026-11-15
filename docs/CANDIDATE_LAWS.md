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
- PS-5 entered the working set on 2026-11-05 as its fallback text; see "Owner decision D1" below.
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

### Owner decision D1 (2026-11-05)

The question put to the owner: on the cube law of part LW1, frames on cells of one-mode sites are only site phases (`U(1)` per site), so the cube law gives no exact `SU(2)` or `SU(3)`; what should PS-5 do? The owner chose to put the fallback text in this section.

- **PS-5, site content.** "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`."
- **The named step.** `B5B_DRAFT.md` on branch `claude/toe-assembly` (draft PR #10139; pass 1, the lead checked both proofs line by line): Theorems B5b and B5b-T. A local frame on an even cell of the cube law acts on the cell's modes by site phases. This holds whether each gate or only the whole tick must be unchanged, for register changes split at the cell, and it includes many-body frames.
- **Check.** Tests 1-3 pass: the text names no group or target, it is closed, and it does not put in the 16 (#10027: site-bilinear `Spin(10)` on five-mode sites gives "vector class, never the 16"). Test 4 passes conditionally: the constant 5 comes from #10014 under its conditions (a)-(c), and #10014 itself calls condition (b), the Weyl-species reading, "an inserted identification, borderline".
- **What it changes.** The text bends the Qubit axiom inside this working set only. The minimal axioms are unchanged. The law on five-mode sites is a new open item (LW1-5) of the TOE assembly.

### Owner decision LZ1-SC, light species (2026-11-06)

The question put to the owner: part LZ1 of the TOE assembly (frozen `LZ1.md` on branch `claude/toe-assembly`, draft PR #10139) defines a light species as a band with a node (its D4). That census counts static bands. The LZ1 referee proved that, with it, the common-light-cone statement fails on `L5-O` in every locally gauge-invariant, stationary, cell-invariant state, because a static Gauss-generator band exists (`LZ1_REFEREE.md` RC1). Codex `gpt-6-astra` at max effort checked the question before it was asked. It confirmed that the cause is the static background and proposed the option below. The owner chose it.

- **LZ1-SC, static class apart.** "LZ1's census of bands with a node is unchanged. Its dispersion clause applies only to bands whose image lies in the orthogonal complement of the tick-fixed vectors, `ker(Ũ−1)^⊥`. Tick-fixed weight is recorded as a separate static class, which LZ1 does not constrain."
- **Check.** Astra gave the reasons for this option but no per-test table; the lead (Claude Opus 5.5) ran the four tests from those reasons. Test 1 passes: it fixes no cone and no common speed. Test 2 passes: membership is a closed condition on the band's image. Test 3 passes: it settles neither MT1-S nor any boson's sector by premise, and it keeps moving bands whose slope vanishes at the node. Test 4 passes: it uses only the tick already in the law.
- **What it changes.** The static Gauss bands of RC1 no longer count against LZ1(a). LZ1-i, the common speed of the moving species, is unchanged. Whether static physical weight is excluded is a separate question (the spectral reading R-SC), not settled here.

### Owner decision GA1-P-NN, nearest-neighbour gates (2026-11-06)

The question put to the owner: PS-1 builds the update from nearest-neighbour gates, but for laws with link registers it did not say whether each gate must itself be gauge invariant. Part GA1-5 of the TOE assembly (frozen `GA1_5.md` on branch `claude/toe-assembly`, draft PR #10139) and its referee showed that the answer decides whether its swap layers are admissible. The owner chose NN-a.

- **GA1-P-NN = NN-a, nearest-neighbour gates (owner 2026-11-06).** "For the named five-mode laws, let `F_x=ΛC⁵` and let `H_ℓ` be the chosen link register. A nearest-neighbour gate `g` is a unitary supported within `F_x`, `F_y` and `H_ℓ`, where `ℓ=(x,y)` and `y=x+e_i`. It acts identically outside those factors. Evenness means `[g,P_xP_y]=0`, with `P_x=(-1)^{N_x}`. A nearest-neighbour layer is a locally finite product on pairwise disjoint edge triples. The update has a fixed finite number of such layers, independent of volume. Its automorphism `α` fixes every local gauge generator. It commutes with every cell lift `α_s`, for `s∈𝒢=2Z³⋊O_{c₀}`. The factors certify a decomposition of the update. Gauge invariance and cell covariance are required of the complete update only."
- **Check.** Codex `gpt-6-astra` at max effort checked the question before it was asked and wrote this text from the law definitions. Its four tests: test 1 P (it names no species, vacuum, dispersion or coupling); test 2 P (support, parity and finite depth are fixed); test 3 C (it settles GA1-P implementability through the referee's compilation, Proposition C of `GA1_5_REFEREE.md`; it passes as a compilation convention in its own right, not as a way to admit a desired class); test 4 P (it uses the existing matter and link factors). The alternative NN-b (each factor gauge invariant) failed test 4 on PS-6's present reasons. Infinite products have the local-automorphism meaning of `LW1.md` E1.
- **What it changes.** GA1-5's swap layers are admissible: on `L5-U[m]`, every `1≤m≤9`, an exact neutral band moves in the physical sector of a gauge-invariant stationary state (`GA1_5.md` Theorem 6.3 and Proposition S-odd). The band carries no flux and has no Clifford cone; it is not a photon. The flux-carrying band GA1-5-Φ and `L5-O` propagation GA1-5-O stay open. Gauge-variant intermediate factors are allowed as compilation steps, not as separate physical operations.

### Owner decision ZM1-I1[a], the zoom's comparison class (2026-11-06)

The question put to the owner: part ZM1 of the TOE assembly (frozen `ZM1.md` and `ZM1_OBS.md` on branch `claude/toe-assembly`, draft PR #10139) needs a fixed class of observables that a block map must reproduce before its open statement ZM1-I1 can be worked. `ZM1_OBS.md` states five classes. The owner chose class (a), with rate exponent p = 2.

- **ZM1-I1[a], the zoom's comparison class (owner 2026-11-06).** "The following specifies the comparison required in the open statement ZM1-I1[O]. It asserts no existence result. Retain the specified VC1 fine vacuum and the admissible fine updates of ZM1-I1. Retain \(L\ge2\), the Definition-Z map \(\Phi:\mathfrak A_1\to\mathfrak A\), (Z-a), (Z-b), (G1), (G2), and singleton embedding sets. Retain a coarse law \(\alpha_1\) of the stated form and an \(\alpha_1\)-invariant state \(\omega_1\). One coarse tick is \(L\) fine ticks. Constants are independent of the variable data, except for the stated support-radius dependence. For every support radius \(R_0\), take all norm-at-most-one \(A,B\in\mathfrak A_1^G\) supported in that ball. Include their cell-group images. Compare their truncated two-point values at every nonnegative coarse tick and every cell separation \(r=|\beta|_\infty\ge1\). For each fixed \(A,B\), set \(M(r,t)=\sup_{|\beta'|_\infty\ge r}\max_i|F_i^T(A^*,\tau_{\beta'}B;t)|\). Require \(|F_0^T-F_1^T|\le C_{R_0}(r^{-p}+tr^{-p-1})M(r,t)\), with \(p=2\). A zero envelope gives zero values on both sides. No separate one-point matching is imposed."
- **Check.** Codex `gpt-6-astra` at max effort checked the question and wrote this text from `ZM1_OBS.md` (frozen) lines 40-48 and 165-176 and `ZM1.md` lines 361-374. Its four tests: test 1 P (it specifies data, not success); test 2 P (radii and data are quantified); test 3 P (no dispersion or continuum conclusion is assumed; it settles neither LZ1-i, nor T0-start, nor the YM consumers); test 4 C (the relative tail envelope is stronger than the printed absolute-error target of ZM1(a)1, a cost the owner accepts). The exponent: "there exists p>=1" is equivalent to p=1; p=2 is the weakest threshold that meets ZM1(a)1's printed p>=2. It is a success criterion, not a claim that the rate is achieved.
- **What it changes.** ZM1-I1 is now a definite open statement, ZM1-I1[a] with p=2, and lanes may work it. It forces the coarse law to match the correlation length and amplitude of every nonzero invariant tail (`ZM1_OBS.md` Lemma ER). It is not shown impossible or trivial. Classes (b)-(e) stay recorded in `ZM1_OBS.md` and are not adopted.

### Owner decision ZM1-INV, the zoom's block map (2026-11-07)

The question put to the owner, after Codex `gpt-6-astra` at max effort checked it: the frozen item `ZM1I1A.md` (branch `claude/toe-assembly`, draft PR #10139) proves that the Definition-Z map retained in ZM1-I1[a] has no L≥2 instance on either five-mode law (a unital map with (G1) and (Z-a) forces L=1). Which block-map definition replaces it; is class (a) with p = 2 kept; and do coarse sites carry the same law (R-form)? The owner chose the invariant-algebra map, kept class (a) with p = 2, and confirmed R-form.

- **ZM1-INV, the zoom's block map (owner 2026-11-07).** "Coarse sites carry the same five-mode construction as the fine sites, with any allowed coarse m₁ (R-form). Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). Retain cell covariance. Require exponential locality for every local invariant input, with support-radius-dependent constants. Use this \(\Phi\) in class (a). Impose no map on charged fields or Gauss generators. Retain class (a) and \(p=2\) as the comparison required of any replacement whose observable and state interfaces make that comparison well-defined. Whether the bound is achieved remains unproved."
- **Scope (lead).** In ZM1-I1[a] this replaces the Definition-Z map \(\Phi:\mathfrak A_1\to\mathfrak A\) and its map conditions (Z-a), (Z-b), (G1), (G2) and singleton embedding sets. The other retained data stand: the VC1 fine vacuum, the admissible fine updates, \(L\ge2\), the coarse law \(\alpha_1\) and the \(\alpha_1\)-invariant state \(\omega_1\), one coarse tick as \(L\) fine ticks, and the relative tail-envelope bound with \(p=2\). The open statement is now ZM1-I1[INV].
- **Check.** Codex `gpt-6-astra` at max effort checked the question and wrote the map text and the class-(a) text (`ZM1I1A_OWNER_CHECK.md`, options 8 and Q2). Its four tests: the invariant-algebra map P P C P (test 3 C: charged-sector consumers need another bridge); retaining class (a) with \(p=2\) P P P C (test 4 C: the envelope forces matching of tail amplitudes and decay parameters, a cost the owner accepted on 2026-11-06). Neither full-algebra obstruction of `ZM1I1A.md` applies directly. Existence is not shown. Astra also gave a new, unrefereed argument that the alternative R-G1EQ still forces L=1 on both laws; it was not chosen.
- **What it changes.** ZM1-I1 is a definite open statement again, ZM1-I1[INV]. The 2026-11-06 decision ZM1-I1[a] stands for its comparison class and \(p\); its retained map conditions are replaced. Charged sectors (R-CS, MT1-S, CG1's 16) get no zoom from this map; they need a separate bridge.

### Owner decisions SMG1-GAP, SMG1-W2.1 and SMG1-W2-LIGHT, the chirality wall (2026-11-07)

The questions put to the owner, after Codex `gpt-6-astra` at max effort checked them (`SMG1_OWNER_CHECK.md` on branch `claude/toe-assembly`, draft PR #10139): wall W2 (chirality by symmetric mass generation, frozen `SMG1.md`) needs a meaning of "gap", since Lemma F (checked once) shows that under infinite translation covariance, stationarity and clustering no NN-a tick has a spectrum-free neighbourhood of 1 on the vacuum complement; whether W2 keeps the bilinear-protection clause W2.1; and what replaces the refuted light-sector condition W2.4. The owner chose bounded R-GEN, kept W2.1, and kept W2-LIGHT open.

- **SMG1-GAP = R-GEN, bounded (owner 2026-11-07).** "For SMG1, fix the certified gate decomposition as part of the supplied data. Write \(g=e^{-iX_g}\), with \(X_g=X_g^*\) and \(\|X_g\|<\pi\). Set \(H_U=\sum_gX_g\), with derivation \(i\sum_g[X_g,A]\). A ground state satisfies \(\omega(A^*[H_U,A])\ge0\) for every local \(A\). A unique gapped ground state has GNS generator with kernel \(\mathbb C\Omega\) and spectrum contained in \(\{0\}\cup[\Delta,\infty)\), where \(\Delta>0\). Tick stationarity remains a separate requirement." Scope: SMG1's rungs only, not every TOE gap. Tests C P C C. It excludes gates with eigenvalue −1; the decomposition must be fixed before the gap is evaluated.
- **SMG1-W2.1 kept (owner 2026-11-07).** "Retain \(G_{\rm SM}\hookrightarrow G\), the 16-component \(D\), and W2.1: \(\operatorname{Sym}^2(D)^G=0\). Retain W2.2–W2.3 and the separately selected replacement for W2.4. W2.1 excludes invariant bilinear masses. The existence of the light 16 remains to be proved." Tests C P C P. It forces \(G\supsetneq G_{\rm SM}\), not \(G=\operatorname{Spin}(10)\).
- **SMG1-W2-LIGHT kept open (owner 2026-11-07).** "Do not adopt W2.4 or W2.4′. Keep W2-LIGHT open. Retain the selected W2.1 and W2.2–W2.3. Require a fully stated replacement before claiming exclusion of every additional light sector." Tests P P P P.
- **Check.** Codex `gpt-6-astra` at max effort wrote these texts and their tests (`SMG1_OWNER_CHECK.md`). It narrowed Lemma F's scope (it excludes no isolated fixed eigenvalue, no gap after removing the whole fixed space, and says nothing on finite rings), and the CH1 amendment was corrected to match.
- **What it changes.** SMG1's rungs read "gap" through the bounded R-GEN, with tick stationarity (FLQ) still to prove. W2 keeps the full 16 with bilinear protection. "Nothing else is light" stays an open criterion. No law or axiom changes.

### Owner decisions without a working-set change (2026-11-05 and 2026-11-06)

These decisions direct work on branch `claude/toe-assembly` (draft PR #10139). None adds text to this working set. They are recorded in `TOE_ASSEMBLY.md` sections 3.5 and 3.6.

- **LW1-5-RQ (2026-11-05): keep both five-mode laws live.** `L5-O` (Majorana hop, `so(20)` quantum links, `Spin(10)` exact) and `L5-U` (number-conserving hop, rishon links, `U(5)` exact) are both developed until one fails at a named step.
- **R-CS (2026-11-06): a working candidate, not adopted.** On both laws fermion parity is a product of local centre elements, so fermions are not local gauge-invariant excitations and need a charged-sector prescription. The Fredenhagen–Marcu straight-string limit, with a relative parity as the odd label over parity-sharp backgrounds, is the named working candidate for lanes (frozen part `RCS1.md`). Adoption waits for its open statements.
- **The zoom's observable class (2026-11-06): options first.** A lane builds and checks several observable classes for the block map; the owner chooses after that.
