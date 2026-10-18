# Step 0 prior-art map, cluster C: anomaly cancellation, generations, hypercharge/SM content

Reader: read-only, origin/main plus the named unlanded branches. Written 2026-10-14, about 13:10Z.

**Framework refresher.** I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines). Four axioms: Lattice (Z^3), Qubit (M_2(C) ~ Cl(3,0)), Admissibility (a nearest-neighbour distribution) and Record. Its "Open Gates Outside The Axioms" list includes "the staggered-Dirac/finite-Grassmann realization and `AC_phi_lambda`". No kinetic branch, time metric or chirality is axiom content.

**Ledger convention.** Every row checked below currently reads `audit_status: unaudited`, because formal audit is deferred under the owner directive (see e.g. `THE_GENERATION_COUNT_...:15`). Where one exists, the last prior verdict is given in brackets, written as [prev: ...].

## Table

| Object | path:line | Status (as stated) | What it shows | What it does NOT show |
|---|---|---|---|---|
| Three-gen / chirality boundary (front door) | docs/THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:3-5,21-30,58-62,83-84 | bounded_theorem; "proposed_retained support"; species reading narrowed to an **open bridge** on 2026-10-02 | Exact 8 = 1+1+3+3 corner orbits. Says rooting is undefined in Hamiltonian Cl(3). The hw=1 label algebra has no proper quotient. Doublers are **kept, not discarded** ("takes the lattice as physical", :73) | Explicitly does NOT claim chirality on the spatial surface (:28-30). Does NOT claim a Nielsen–Ninomiya (NN) evasion (:60-62). Chirality is outsourced to anomaly-forces-time plus one-generation closure (:51-53) |
| Anomaly forces time (3+1) | docs/ANOMALY_FORCES_TIME_THEOREM.md:13-26,105-116,125-137,413-433 | bounded_theorem, conditional [prev: audited_conditional 2026-05-05] | Takes the LH packet (2,3)_{+1/3}+(2,1)_{-1} as anomalous. Under P-ABJ and P-COMP, a chirality grading is needed, and EVEN then gives d_t odd. B-AXIS caps d_t at 1 | **Assumes** the chiral spectrum through declared premises: P-HY (Y_like is the gauged U(1)_Y), P-COMP (the completion is opposite-chirality SU(2) singlets), P-REC (ε realised as Clifford γ5 on the irreducible Dirac factor), P-ABJ (external), B-AXIS. Does not address gauging a chiral subset on the lattice. Counterfactual: vector-like content makes the chain inert (:366-370) |
| One-generation matter closure | docs/ONE_GENERATION_MATTER_CLOSURE_NOTE.md:12,44-74,109-111,116-124 | bounded_theorem [prev: audited_conditional] | Conditional SM right-handed (RH) completion (u_R 4/3, d_R −2/3, e_R −2, ν_R 0). Records "no weak singlets on the purely spatial C^8 surface, proper chirality only on the 4D C^16 surface" | Not a derivation of the RH sector from the graph. ν_R=0 is a branch **convention** (:76-100). Imports chirality from anomaly-forces-time |
| RH-sector runner (where chirality enters) | scripts/frontier_right_handed_sector.py:44-55,515,744 | runner (PASS=61) | C^16 = C^8_L ⊕ C^8_R under 4D γ5. The taste algebra **commutes with γ5, so the same taste quantum numbers appear in both chirality sectors** (:47-48) | SU(2) singlet-ness of C^8_R is put in by hand: "SU(2)_weak SINGLETS by the chirality of weak interactions" (:515). The native structure is therefore vector-like and the chiral gauging is assumed |
| Historic chiral completion | docs/historic_intake/HISTORIC_CHIRAL_COMPLETION_NOTE_INTAKE_NOTE_2026-08-05.md:17-25,45; original archive_unlanded/.../152_CHIRAL_COMPLETION_NOTE.md:17-19 | historic intake, unaudited, branch-only | Same 16 = 8_L + 8_R construction, with RH hypercharges from anomalies | "RH are SU(2) singlets because SU(2) is a chiral gauge symmetry coupling only to left-handed fermions." This is an assumption |
| SM anomaly synthesis | docs/AXIOM_FIRST_SM_ANOMALY_CANCELLATION_COMPLETE_THEOREM_NOTE_2026-05-03.md:15-37,46-58,230-250 | positive_theorem (synthesis aggregator), awaiting audit | (A0)–(A5) vanish exactly on the given LH+RH × 3 content | Does not derive the LH content, N_c, n_gen, ABJ or Witten, and gives no completion uniqueness: "vectorlike or B-L-extended matter content can also pass" (:248-250). Pure arithmetic on an assumed chiral spectrum |
| SM anomaly closure, decoupled | docs/SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08.md:35-54,82-96,103-108 | bounded_theorem [prev: audited_clean 2026-07-10] | RH Y values are forced *given* a minimal singlet completion. Six anomalies cancel. Decoupled from anomaly-forces-time | C1: the content is not anomaly-unique (vectorlike pairs pass). Mirror exclusion "is the separate chirality question … not closed here" (:84-86). C3: ν_R gives a one-parameter family |
| LH trace catalog / SU(3)^3 / Witten / B−L / 3̄ completion / singlet completion / RH identities | docs/LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md:4-7,153; SU3_CUBIC_...:4-16; SU2_WITTEN_Z2_...:4-7,120; BMINUSL_..._2026-04-24.md:4-16,214; SU3_ANOMALY_FORCED_3BAR_...:5-15,42; ONE_GENERATION_ANOMALY_SINGLET_COMPLETION_...:4-18,235; RH_SECTOR_...:4 | positive/bounded; prevs: catalog cond., Witten cond., singlet completion clean (2026-07-12), B−L never audited | Exact traces. N_D = 12 (even). The B−L traces vanish. 3̄ follows under a **minimal-field-count principle**. Shift completion (a+1, a−1, b−1, b+1) | Each consumes the chiral content as input. "Chirality assignment is a hypothesis" (singlet completion :235). Witten assumes three generations (:6). None touches lattice gauging |
| ABJ scale-free core | docs/ABJ_SCALE_FREE_NATIVE_ABELIAN_ANOMALY_CORE_BOUNDARY_NOTE_2026-06-18.md:12-36,58-66 | bounded_theorem [prev: audited_decoration] | The anomaly is nonzero for any Y_a = a P_6 − 3a P_2, so normalisation is not load-bearing | Open: "the physical gauging / anomaly-relevant U(1) role of `Y_a`" (:62), plus P-COMP, P-ABJ, P-REC and B-AXIS |
| ABJ ε-index square-block | docs/ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md:33-61,131-144,190-206 | no_go (route-pruning) | Tr(ε e^{−tD†D}) = 0 on every equal-sublattice even Z^4 torus with any U(1) links (square bipartite block). This is the staggered form of the doubler cancellation | Does NOT prune a taste-singlet/Adams index, an overlap/Ginsparg–Wilson (GW) index, an imbalanced or curved complex with χ≠0, continuum ABJ, or ABJ taken as a premise |
| ABJ P-REC spin/taste core | docs/ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md:17-26,55-81,85-93,101-110 | bounded_theorem [prev: audited_conditional 2026-08-03] | The blocked 2^4 hypercube has a genuine taste-singlet Γ5^spin = α0α1α2α3. ε is taste-dressed and not ±Γ5^spin | Open: a bridge saying the anomaly-carrying chirality and **chiral gauge representation** use Γ5^spin "in the relevant interacting single-taste/continuum readout context" (:90-93). No single-taste selector (:107) |
| ε is not spacetime γ5 (historic) | docs/historic_intake/HISTORIC_ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026_06_17_INTAKE_NOTE_2026-08-05.md:21,47-49 | historic no-go, unaudited | The ε shortcut is dead | Leaves open a taste-reconstruction or Cl(3,1) route |
| P-COMP classification | docs/ABJ_P_COMP_SCALE_FREE_SINGLET_COMPLETION_CLASSIFICATION_NOTE_2026-06-18.md:17-47,95-100 | positive_theorem (abstract algebra) [prev: clean] | The supplied polynomial system with n=0 gives {x,y}={4a,−2a}, z=−6a | "no physical realization … chirality-selection law, or completion-minimality theorem" (:95-97) |
| P-HY formal packet | docs/ABJ_P_HY_RETAINED_BOUNDED_SUPPLIER_WIRING_NOTE_2026-06-18.md:20-32,64-75 | bounded_theorem | Trace arithmetic on a supplied formal 6+2 packet | Labels Q_L, L_L and U(1)_Y are "not conclusions". It does not derive the 6+2 packet or P-HY |
| ABJ U(1) Jacobian / accepted-premise bridge | docs/ABJ_ANOMALY_FRAMEWORK_INTERNAL_U1_JACOBIAN_NARROW_NOTE_2026-05-27.md:13-31; docs/ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md:13-71 | bounded [bridge prev: audited_conditional 2026-06-18] | Narrows (P1) to (P1′) and registers P-ABJ as a named premise (B1–B6) | Does not derive (P1′) or (P1), nor P-HY, P-COMP or P-REC |
| Historic "ABJ from framework action" | docs/historic_intake/HISTORIC_ABJ_FROM_FRAMEWORK_ACTION_U1_CUBIC_..._INTAKE_NOTE_2026-08-05.md:19,46 | historic positive, branch-only, unaudited | Claims the Jacobian gives −16/9 and that no local counterterm cancels it, so "ABJ import retired" | Never mainlined. Main still lists P-ABJ as "irreducibly external" (ANOMALY_FORCES_TIME:110,307-317). Conflict unresolved |
| No per-site γ5 | docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md:4-12,24-27 | no_go [prev: audited_clean 2026-07-07] | No element of M_2(C) anticommutes with all of σ_i | No spacetime Clifford algebra and no SM L/R |
| Native gauge closure / LH abelian surface | docs/NATIVE_GAUGE_CLOSURE_NOTE.md:149-154; docs/NATIVE_GAUGE_LEFT_HANDED_ABELIAN_SURFACE_BOUNDED_NOTE_2026-05-23.md:5-13,21-24 | positive [clean] / bounded [decoration] | su(2)+su(3) structure on the taste C^8. Traceless {+1/3×6, −1×2} | Excludes "chirality completion" (:154). "`left-handed` names the inherited weak-fiber surface label only" (:21-22) |
| LH charge matching / Y identification | docs/LEFT_HANDED_CHARGE_MATCHING_NOTE.md:27-35; docs/HYPERCHARGE_IDENTIFICATION_NOTE.md:5-9,130-139 | bounded [decoration / cond.] | Ratio 1:(−3) from 6α+2β=0 | No species, readout or anomaly closure. The scale is a convention |
| Cl3 Y spectrum on "chiral cube" | docs/CL3_HYPERCHARGE_EIGENVALUE_SPECTRUM_ON_CHIRAL_CUBE_NARROW_THEOREM_NOTE_2026-05-27.md:8-11,63-93,147-176 | bounded [prev: clean 2026-07-02] | Y = (1/3)P_sym − P_anti on (C^2)^⊗3 has spectrum {+1/3×6, −1×2}. The hw=3 singlet carries +1/3 | The cube↔SM carrier and algebraic-Y↔physical-Y bridges are **deferred**. "Chiral cube" is a name, not Weyl chirality |
| Cl3 chiral body-diagonal | docs/CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md:4-21,81-163 | no_go [prev: cond.] | Koide Γ_χ: the axis (1,1,1) is native but the doublet h is an unsourced C3 break | Concerns **generation/Koide chirality**, not Weyl/gauge chirality |
| Two independent chirality gates | docs/CHIRALITY_GATE_IS_TWO_INDEPENDENT_GATES_DIRAC_VS_GENERATION_SCOPING_NOTE_2026-06-08.md:12-19,49-69,91-101 | bounded/conditional (not in ledger) | γ5 = I_3⊗σ_3 is generation-blind, so the Dirac and Koide chiralities are independent | Does not derive γ5 from Cl(3,1), nor its spin-statistics |
| Diagonal gate (corrected) | docs/DIAGONAL_GATE_CHIRALITY_HW1_ORBIT_TEST_NOTE_2026-06-04.md:10-13,42-69; correction .claude/science/physics-loops/diagonal-adjacency-7870-correction-20260909/CORRECTION_HISTORY.md (D2) | bounded (finite math) | C3-equivariant and anticommuting gives H = 0. A complex Hermitian zero-diagonal counterexample exists | "No global chirality no-go … BZ-corner mixing have not been identified with these matrix entries" (:66-69) |
| Three-gen structure | docs/THREE_GENERATION_STRUCTURE_NOTE.md:4-13,104-115 | bounded [prev: clean 2026-05-29] | Wilson m(p) = 2hw(p). hw=1 is the lightest nonzero triplet on the admitted surface | Does NOT claim the triplet is physical SM generations, nor chirality or no-rooting (:111-115) |
| Three-gen observable theorem | docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md:3,23-33,44-60,329-336 | bounded [prev: clean] | M_3(C) on the hw=1 labels; no proper quotient | The labels are **not** observable sectors of the KS operator near its zero modes. The corner translations are not joint symmetries, and the kinetic term's X_1 factor changes Hamming weight (:50-59). The 12-dim cell carrier has a multiplicity commutant (:3) |
| Generation axiom boundary | docs/GENERATION_AXIOM_BOUNDARY_NOTE.md:5-14,40-55 | bounded [prev: clean] | Local M_3(C) on H_hw=1 | The physical-species bridge and substrate fundamentality are out of scope |
| Taste-cube S3/Z3 | docs/CL3_TASTE_GENERATION_THEOREM.md:7-10,53-83 | bounded [prev: decoration] | C^8 = 4A1+2E. hw=1 = A1+E. Restricted Y {+1/3,+1/3,−1} | "not a framework carrier theorem and not a physical-family theorem" |
| Rooting undefined | docs/THREE_GENERATION_ROOTING_UNDEFINED_NARROW_THEOREM_NOTE_2026-05-27.md:3-9,40-56 | no_go [prev: clean] | Every proper coordinate projection of the corners breaks the Cl(3) anticommutators | Only diagonal coordinate projections are covered; "not a physical species-semantics claim" |
| Generation count = d (corrected) | docs/THE_GENERATION_COUNT_IS_..._2026-09-03.md:25-31,80-86,131-137,174-182; correction .claude/science/physics-loops/generation-correction-20260909/CORRECTION_HISTORY.md (G1–G3) | bounded; audit deferred | The K1 corner count is C(d,1). A central K0 corner projector exists | Isolation window and "undefined on K0" were **withdrawn**. "no physical generation/species identification" (:176-182) |
| Parity violation does not reach the triplet | docs/PARITY_VIOLATION_DOES_NOT_REACH_GENERATION_TRIPLET_NARROW_THEOREM_NOTE_2026-05-23.md:20-55 | bounded [prev: clean] | ε maps hw=1 → hw=2 ("generations ↔ anti-generations"). Inversion is trivial. S3 is separate | Reads hw=1 as "the three generations" and hw=2 as the 3̄. The reading is not derived there |
| Common hw=1 carrier ID | docs/STAGGERED_DIRAC_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_BRIDGE_NARROW_THEOREM_NOTE_2026-07-05.md:14-56 | bounded | The concrete 2×2×2 carrier realises the abstract hw=1 orbit | "derives no labeling, no mass value" |
| Color vs generation Z3 | docs/COLOR_GENERATION_INDEPENDENT_Z3_STRUCTURES_2026-06-05.md:6-10,17-37; docs/Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10.md:26-34 | bounded / open_gate | Characters (3,3ω,3ω²) vs (3,0,0) are inequivalent | No physical color or generation carrier |
| HF96 Connes candidate | docs/CLOSURE_T1_HF_96_CONNES_CONSTRUCTION_NOTE_2026-05-10_t1hf96.md:6-43,197 | bounded candidate | H_F = C^8 ⊗ C^3 ⊗ C^4. The hw=1 orbit is lifted to a **separate** C^3 factor | Order-one D_F is open. "does not close left-handed content" |
| Gauging selection | docs/GAUGE_ALGEBRA_SUPPLIED_CARRIER_GAUGING_SELECTION_OPEN_GATE_NOTE_2026-06-08.md:18-30,47-67,104; docs/GAUGE_GAUGING_SELECTION_CONJUGATION_INDEPENDENCE_NO_GO_NOTE_2026-06-16.md:43-49,59-76 | open_gate [prev: cond.] / no_go [prev: clean] | On a supplied C^3⊗C^2, su(3)⊕su(2)⊕u(1) is the factor-preserving cut of u(6). Conjugation-invariant data cannot select it | "does **not** derive chiral `su(2)_L`" (:50,104) |
| Anomaly inflow (A3 route 3) | docs/A3_ROUTE3_ANOMALY_INFLOW_BOUNDED_OBSTRUCTION_NOTE_2026-05-08_r3.md:8-15,512-575 | bounded; the 2026-10-04 gate narrows it to an operator identity | C-commuting H has equal corner diagonals | Broader exhaustion was **withdrawn**. Not about chirality or gauging |
| Domain-wall chiral edge + inflow (archived) | archive/notes/docs/DOMAIN_WALL_CHIRAL_EDGE_FROM_ACHIRAL_CL3_BULK_..._2026-07-04.md:5-13; archive/notes/docs/DOMAIN_WALL_EDGE_ANOMALY_INFLOW_SPECTRAL_FLOW_..._2026-07-05.md:5-12,189-208 | bounded, archived (densify freeze) | Native Cl(3,0) operator is NN-doubled. A record-time domain wall localises one Weyl species on the wall and the opposite on the anti-wall. Callan–Harvey (CH) flow is seen in a background field | Free field only, gauge non-dynamical, net chirality zero on the torus. The higher-dimensional regulator is not derived. "full electroweak chiral structure is not derived" |
| Physical-lattice necessity | docs/PHYSICAL_LATTICE_NECESSITY_NOTE.md:11-49,161-176 | narrowed no-go (β, u_0 rigidity) | Two-invariant rigidity only | Triplet species semantics and substrate necessity are open, delegated to the single-axiom notes |
| Historic: anomaly forces three generations | docs/historic_intake/HISTORIC_GENERATION_ANOMALY_FORCES_THREE_NOTE_INTAKE_NOTE_2026-08-05.md:19,45; original archive_unlanded/historic_intake_originals/branch02/609_...:26-62,114-126 | historic bounded, pre-reset | Continuous anomalies are blind to 1×24 vs 3×8. The Z3 Dai–Freed leg (ν=2 per orbit) obstructs identification. Each 8-state LH sector needs its own RH completion | Conditional on "taste-physicality" (A1) and on interacting 't Hooft matching. Uses "24 LH taste states (3 copies of 8)" |
| Historic: generation physicality obstructed / K-theory / Fermi point | docs/historic_intake/HISTORIC_GENERATION_PHYSICALITY_OBSTRUCTED_ROUTE_..._2026-08-05.md:21,56-59; ..._KTHEORY_...:21,49; ..._FERMI_POINT_...:19,49 | historic, unaudited | 11 closure routes fail, and a physical-substrate axiom is needed. K-theory is blocked by a non-equivariant P. C(d,1) = 3 | Red flag: an exhaustiveness claim. A dressed U P U⁻¹ was never tried. The 1+3+3+1 vs 1+1+3+3 mapping is left open |
| Branch: 3plus1 / P-ABJ firewall / ABJ-Y completion boundary | origin/physics-loop/3plus1-spacetime-anomaly-forces-time-20260530 (.../NO_GO_LEDGER.md); origin/physics-loop/anomaly-pabj-local-premise-firewall-20260617 (HANDOFF, NO_GO_LEDGER); origin/physics-loop/abj-hypercharge-completion-boundary-20260617 (HANDOFF, NO_GO_LEDGER) | unlanded loop packets | ε-index no-go. P-ABJ stays external. The Y completion is forced given P-HY and the minimal singlet completion | HANDOFF: "P-COMP-min and vectorlike/mirror exclusion are still premises". NO_GO_LEDGER: "vectorlike pairs preserve anomaly zeros" |
| Branch: Berry/holonomy, rooted spin-generation | origin/physics-loop/generation-berry-holonomy-selector-20260607, rooted-spin-generation-entanglement-20260607 (HANDOFF, NO_GO_LEDGER) | unlanded, route-pruned | A native C3 Berry connection is flat. Equivariant rooted entanglement induces only central operators | Not a general rooting no-go |
| Branch: one chirality ε for SU(2)_L and the flavor phase | origin/science/one-chirality-weak-and-flavor-phase-20260604: docs/ONE_CHIRALITY_GRADING_..._2026-06-04.md:5-18,57-60,71 | branch-only structural map | Claims a single ε underlies both the chiral SU(2)_L coupling and the η/δ mechanism | "the ORIGIN of SU(2)'s chiral coupling … not derived" (:58-59). It uses ε, which main's P-REC note shows is taste-dressed and not γ5 |

## Key structural readings (labelled: my reading of the notes, not repo claims)

1. **The doublers are reinterpreted, not removed. There are two readings of the same 8 corners, and I found no note reconciling them.**
   - (R1) Tensor/taste basis: C^8 = (2,3)+(2,1) = Q_L+L_L of **one** generation (`frontier_right_handed_sector.py:8-12`; NATIVE_GAUGE_LEFT_HANDED surface). In 4D, C^16 = 8_L + 8_R.
   - (R2) Momentum/Hamming basis: 8 = 1+3+3+1, with hw=1 read as the **three generations** and hw=2 as the anti-generations (PARITY_VIOLATION:29-37).
   - HF96 tensors a separate C^3 generation factor onto C^8 (CLOSURE_T1_HF_96:27). The historic 609 note counts "3 copies of 8". On main, the R2 species reading is an open bridge.
2. **The native 4D taste structure is vector-like. Chirality of the gauge coupling is put in by hand.** The runner states that the taste algebra commutes with γ5, so the "same taste quantum numbers appear in both chirality sectors" (:47-48). It then declares C^8_R to be SU(2) singlets "by the chirality of weak interactions" (:515). This is the NN wall in framework form. It sits inside P-COMP / P-HY, and the mirror-exclusion premise.
3. Every anomaly-cancellation note **assumes** the chiral LH packet and the singlet RH completion, and does exact trace arithmetic on them. None constructs or gauges a chiral subset on the lattice. All of them concede that the completion is not unique: vectorlike pairs pass, and ν_R gives a one-parameter family.
4. "Chiral cube", "chiral body-diagonal" and Γ_χ mean **Koide/generation chirality**, not Weyl chirality. CHIRALITY_GATE_IS_TWO proves the two are independent. They should not be counted as attacks on this wall.

## (a) Tried and failed (with reasons)

- **Staggered ε-index as the lattice ABJ witness.** Identically zero by the square bipartite block (ABJ_EPSILON:33-61).
- **ε = spacetime γ5 shortcut.** ε is taste-dressed and not in the spin Clifford algebra (ABJ_P_REC:72-81; historic ε-not-γ5 intake).
- **Per-site γ5.** The volume element is central in M_2(C) (NO_PER_SITE:5-12).
- **Rooting by coordinate projection of corners.** It breaks the Cl(3) anticommutators (ROOTING_UNDEFINED:5-9). Only coordinate projections are covered.
- **"Anomaly forces 3 generations".** Continuous anomalies are blind to the generation split. The Dai–Freed leg is conditional on taste-physicality and the interacting theory (609:33-37,114-126).
- **Generation physicality.** 11 routes failed (historic intake :21). K-theory was blocked by non-equivariance (KTHEORY :21).
- **Generation count from Wilson isolation, and "undefined on K0".** Withdrawn on 2026-09-09 after collisions at λ = 2/5 and 2/3, and because a central corner projector exists (GENERATION_COUNT:80-86,131-137).
- **Diagonal-hop pure anticommuting route.** The general exclusion was withdrawn after a complex counterexample (DIAGONAL_GATE:42-58).
- **Parity violation (ε) as the generation splitter.** It maps hw=1 → hw=2.
- **Anomaly inflow as a BZ-corner distinguisher.** Reduced to an equal-diagonal identity; the broader claims were withdrawn (A3 r3:512-523).
- **Native C3 Berry/holonomy and equivariant rooted spin-generation entanglement.** Both pruned (branches).
- **Gauging selection from conjugation-invariant or irreducibility data.** No-go (GAUGE_GAUGING_SELECTION:59-76).
- **Color = generation Z3.** The characters are inequivalent.
- **Anomaly uniqueness of the SM completion.** Fails because of vectorlike pairs and the ν_R family (SM_ANOMALY_CLOSURE:82-96).

## (b) Pre-registered or named, but not run (in this slice)

- **ABJ_EPSILON:195-202.** Positive routes are named but not executed here:
  - a native taste-singlet/Adams index or overlap/GW index proven to be "an allowed physical chiral measure";
  - an imbalanced or curved complex with χ≠0;
  - a direct native ABJ derivation.
- **ABJ_P_REC:90-93,105-107.** A single-taste selector and an interacting/gauged chirality bridge to Γ5^spin. Neither is constructed.
- **One-chirality branch next action (:71).** "derive the chiral (P_L) coupling of su(2) from the staggered eps". Unrun, and already undercut by P-REC.
- **Historic K-theory (:49).** A dressed Z3 action U P U⁻¹ commuting with H(k) was "not attempted".
- **Historic 609 (:119-122).** Interacting Z3 anomaly matching remains open.
- **A3 r3 N7 (:564-569).** Three escapes "remain open physical work":
  - a Fourier-character readout;
  - a source that splits the characters;
  - an APBC carrier mixing nearest-corner labels.
- **Generation branches' "Next Work".** Mass/Yukawa fluctuation-determinant holomorphy; T-odd K-reality origin. Status not checked beyond the handoffs.
- **Pointer only, not read (outside this slice).** The current branch's commits "C5 TW-1/2/3 pre-registered (twin halving, generations, symmetric gapping)" and "C5 referees NF-1 OPEN (symmetry confirmed; literal U(1)_eps)" bear directly on this wall.

## (c) Current-wall statements (quoted)

- THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md:83-84: "So the current package is not claiming a loophole in the usual no-go theorem. It is claiming a different theory surface."
- SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_...:84-86: "Excluding vectorlike/mirror content is the separate chirality question, … not closed here."
- ABJ_P_REC_SPINTASTE_...:21-24: the residual is "the physical bridge identifying the anomaly-carrying physical chirality and chiral gauge representation with that spin `gamma_5`".
- GAUGE_ALGEBRA_SUPPLIED_CARRIER_...:50: "does **not** derive chiral `su(2)_L`".

## (d) Open gates named

- **ANOMALY_FORCES_TIME premises.** P-ABJ, P-HY, P-COMP (including P-COMP-min and vectorlike/mirror exclusion), P-REC (the single-taste spin-γ5 bridge) and B-AXIS (:105-116,413-433).
- **Axiom-memo gate.** Staggered-Dirac/finite-Grassmann realization, `AC_phi_lambda` (MINIMAL_AXIOMS "Open Gates").
- **hw=1 species/generation reading.** THREE_GENERATION_CHIRALITY_BOUNDARY:22-24,44-46; PHYSICAL_LATTICE_NECESSITY:169-172.
- **Physical-Y carrier and operator bridges.** CL3_HYPERCHARGE §3.
- **Gauging selection.** MR_color/factor-locality and chiral su(2)_L (GAUGE_ALGEBRA open gate).
- **Z3 color/generation.** Z3_CHARACTER_ISOMORPHISM open gate.
- **Koide/generation chirality.** The C3-breaking M_gen (CHIRALITY_GATE_IS_TWO:96-99).
- **ν_R branch selection.** ONE_GENERATION_MATTER_CLOSURE:76-100.
- **Further gates.** The P-ABJ derivation; the historic Jacobian "retired" claim conflicts with main and is unresolved.

**Not reached.** Full section-by-section reads of:
- SU2_WITTEN, BMINUSL, SU3_CUBIC, SU3_3BAR, LH_TRACE_CATALOG and RH_SECTOR (heads and non-claim lines only);
- ANOMALY_FORCES_TIME_ABJ bridge §141-397;
- KCPT_CORNER_CARRIER_..._HW1_DOUBLET (07-17);
- GENERATION_TRIPLET_DIMENSION_PARITY no-go;
- AXIOM_FIRST_LATTICE_WZ_FUJIKAWA;
- STAGGERED_DIRAC_REALIZATION_GATE;
- the codex/chirality-* branches (out of slice);
- the audit-repair three-generation branch (it adds no docs).
