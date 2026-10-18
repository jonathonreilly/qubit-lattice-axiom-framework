# Step 0 prior-art map, cluster A: record-side and admissibility-side chirality

Reader: read-only prior-art pass, 2026-10-14, 12:59–13:30Z. All paths are on `origin/main` unless a branch is named. Line numbers come from `git show origin/main:<path> | cat -n`.

**Framework refresher.** I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (233 lines). It has four axioms. Lattice: `Z^3` with nearest-neighbour adjacency, translations, and **proper** cubic rotations only. Qubit: `M_2(C)`, with a `Cl(3,0)` presentation that "adds no further primitive structure". Admissibility: one fixed nearest-neighbour rule, covariant under translations and proper rotations, that determines a per-site probability distribution. Record: records form, each locks one possibility, they are permanent, and only records are readable. Two passages bear directly on this wall:
- The open-gate list puts "the staggered-Dirac/finite-Grassmann realization" outside the axioms (MINIMAL_AXIOMS:178).
- The Qualification says "A choice not fixed by the supplied structure remains a named conditional or open dependency" (MINIMAL_AXIOMS:89-90), and that "No admission class exists" (:111).

**Scope warning for the whole slice.** Almost everything here concerns **handedness of the admissibility rule, the record alphabet, or record statistics**, meaning mirror-pair structure under the cubic group O_h. None of it constructs a chiral *fermion spectrum*, attacks doubling or Nielsen–Ninomiya, or assigns SM chiral gauge content. Several notes say this outright ("No fermion-sector claim"). "Chiral pair" in the 2026-10-10 programme means a pair of record-alphabet orbits, not Weyl fermions.

## Short keys used below
- MIRROR = `docs/A_MIRROR_ASYMMETRIC_ADMISSIBILITY_RULE_..._BOUNDED_NOTE_2026-09-05.md` (corrected 2026-09-09)
- SWEEP = `docs/A_TIME_DIRECTED_FORMATION_SWEEP_REGISTERS_..._BOUNDED_NOTE_2026-09-05.md` (corrected 2026-09-09)
- WIND = `docs/THE_CONTINUUM_RECORD_ALPHABET_KEEPS_THE_WINDING_PHASE_..._BOUNDED_THEOREM_NOTE_2026-09-04.md` (corrected 2026-09-09)
- CORR = `.claude/science/physics-loops/chirality-correction-20260909/CORRECTION_HISTORY.md`
- OB0922 = `docs/ORDER_BLIND_NEAREST_NEIGHBOUR_FORMATION_INDEPENDENCE_BEYOND_NEIGHBOURS_UNSOLDERED_CONSTANCY_AND_SOLDERED_ESCAPE_BOUNDED_THEOREM_NOTE_2026-09-22.md`
- ACH012 = `docs/ACHIRAL_ZERO_ONE_TWO_ORBIT_ORDER_BLIND_FACTOR_BOUNDED_THEOREM_NOTE_2026-10-09.md`
- CP-* = `docs/CHIRAL_PAIR_*_BOUNDED_THEOREM_NOTE_2026-10-10.md`, and UNEQ = `docs/UNEQUAL_HEIGHT_SIGNATURE_WITH_ONE_PARTNER_BOUNDED_THEOREM_NOTE_2026-10-10.md`
- PSEUDO = `docs/ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md`
- COV0703 = `archive/notes/docs/ADMISSIBILITY_RULE_COVARIANCE_EXTENSION_CLASSIFICATION_..._MINIMAL_CHIRAL_CHANNEL_BOUNDED_THEOREM_NOTE_2026-07-03.md`
- BOOT0704 = `archive/notes/docs/EMPTY_STATE_BOOTSTRAP_..._DEGREE_NINE_CHIRALITY_WALL_BOUNDED_THEOREM_NOTE_2026-07-04.md`
- ACHMIN0704 = `archive/notes/docs/RULE_ACHIRALITY_FROM_MINIMALITY_QUALIFICATION_LICENSING_LAW_ACHIRAL_STATE_FREE_BOUNDED_THEOREM_NOTE_2026-07-04.md`
- MATTER0714 = `archive/notes/docs/work_history/repo/review_feedback/MATTER_COUNTING_CHIRALITY_EXACT_LAW_PLACEMENT_NOTE_2026-07-14.md`
- TRIAD0714 = `archive/notes/docs/work_history/repo/review_feedback/CHIRAL_TRIAD_TRANSVERSE_CONTEXT_CYCLE17_NOTE_2026-07-14.md`
- ARC = `archive/families/toe-lphys-chirality-lightcone-arc.md`
- DEFER = `docs/repo/DEFERRED_DECISIONS.md`

## Table

| Object | path:line | Status (as stated) | What it shows | What it does NOT show |
|---|---|---|---|---|
| One-site γ5 | `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`:55-65, 140-143 | no_go (single-site); "independent audit required" | In `M_2(C)`, ω=σ1σ2σ3=iI, and only 0 anticommutes with all σ_i. No one-site γ5 and no (1±γ5)/2 projector | Says nothing about multi-site, temporal or larger-Clifford chirality. C2 names those as the remaining routes |
| Record typing vs chirality | `docs/CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05.md`:56, 60-68, 70-78 | meta support map; route-pruning PASS for scope only | "record dynamics is a consumer, not a chirality source". Five routes pruned: signed spectra, Hermitian sqrt, counts, ungraded tensor→CAR, transport | Does not say chirality is impossible (:68). Leaves the carrier/dynamics theorem open |
| Registration and the Koide Z3 grading | `docs/REGISTRATION_REINSTATES_CHIRALITY_NO_GO_NOTE_2026-06-07.md`:25-36, 116-122 | no_go | The C3-character registration map D annihilates every Γ_χ-anticommuting operator, so Record registration cannot source the Q=2/3 chiral carrier | This is *generation-space* chirality (Γ_χ=(2/3)J−I), not spacetime/Weyl chirality. N1.6 leaves a T-odd emergent route open |
| Three distinct "orientation" objects | `docs/CHIRAL_CONTENT_IS_THE_EPSILON_D_..._NARROW_THEOREM_NOTE_2026-06-08.md`:18-26, 39-41 | bounded_theorem | The staggered ε(x), the qubit ω (K-odd) and the generation sign(Vandermonde) are distinct data. The grading check cannot tell chiral from vector coupling | Derives none of them and no chiral gauging |
| Rule covariance extension, minimal chiral channel | COV0703:60-67, 69-82, 84-94, 96-117, 225-228 | bounded_theorem (archived) | Openness-only (k=2) rules are automatically achiral. k=3 has exactly one chiral pair (57 vs 56 orbits). The canonical k=4 carrier is the oriented frame, with frame sign as the P-odd invariant. Under the antilinear twist, i·frame_sign is achiral with Re=0. A chiral rule costs **one orientation bit**, shared with the theta seed | "Does not determine the framework's physical rule". "No fermion-sector claim" (:225-228) |
| First availability set A0, Ψ9 wall | BOOT0704:64-79, 81-99, 101-122, 218-234 | bounded_theorem (archived; set-level after the 08-05 repair, :24-35) | A0 must be proper-cubic-invariant. Generic 24-orbits are chiral twins; mirror-locus orbits are achiral. No det-character cubic harmonic exists below l=9, and the unique one is Ψ9=xyz(x²−y²)(y²−z²)(z²−x²). A chiral A0 spends the one bit | Does not determine A0. Spontaneous (history) orientation is **not excluded** (:231-233). No fermion claims |
| Rule achirality vs state chirality | ACHMIN0704:29-31, 100-117, 297-308, 321-325 | bounded_theorem (archived); conditional licensing | Within the finite witness: the law is achiral, yet a reachable *state* can carry the reflection-odd J2. A mirror axiom is "over-strong — it would forbid the observed weak-sector chirality too" | "does not resolve chiral-fermion emergence". Its licensing quotes the 07-04 Qualification wording ("unless that choice is admitted"). The current memo (:89-90, :111) has no admission class, so the licensing step needs re-reading against the current text |
| Law sign vs realized domain | MATTER0714:90-111, 248-266 | review feedback, "Authority: none" | Proper covariance does not choose a hand (det V vs det PV). Naive sin(k) Weyl has 8 corners, 4 per chirality. The domain wall gives a chiral mode only after an imposed mass profile, and a periodic system carries an anti-wall. Three-way split: law chirality / state chirality / effective chiral mode | Not a theorem. "does not by itself establish a globally undoubled chiral theory" (:258-259) |
| Chiral triad vs X/Y apparatus | TRIAD0714:452-459 | review feedback, no authority | Proper chirality does not select the X vs Y pointer leg. It explicitly separates that from the "Weyl/matter chirality lane" | Not about fermion chirality |
| Chiral labelling on grown fronts | ARC:27-36 | archive roll-up; "promotion candidates" | The July-3 chiral pair needs 4 occupied neighbours. **No NN-determined G+-equivariant chiral labelling exists on any 4-occupied star** (#6668). Lock-ticks do not repair this. The escape needs one age bit, which is not recoverable from occupancy (#6682) | Roll-up only. Defects listed at :43-52 |
| Mirror-asymmetric rule (corrected) | MIRROR:22-39, 41-56, 58-75, 77-107, 109-120, 145 | bounded_theorem; `conditional-support` | T1: 729 ternary profiles give 57 proper / 56 full orbits and **one chiral pair**. A table constant on proper orbits can break mirrors only there, and label-equivariant tables (3^24) are all mirror-symmetric. T3: conjugate kernels give identical fixed-basis occupation laws. T4: on a 12×12×24 KS string, 16 in-gap states, 8 carrying Jz (−4 core/+4 ring) | T5:115 says this is "**not** absence of all handed interface modes". There is no physical T identification and no weak coupling (:127-131) |
| Directed sweep (corrected) | SWEEP:48-63, 65-80, 82-95, 132-159, 184 | bounded_theorem; `conditional-support` | The sweep registers direction of motion (Δ_core −.468 at τ=.5). Screw responses cancel only under a C2(x)-**invariant weighted** measure; set closure is not enough. T5 counterexample: a covariant nonempty 57-menu table gives 1272 vs 1320 completions, mean Ξ=+.0068 | Not a probability law generated by the conditional rule (:156-159). No physical chiral formation mechanism |
| Winding phase / vortex (corrected) | WIND:22-39, 41-61, 86-109, 111-134, 159 | bounded_theorem; `conditional-support` | Supplied staggered and D4 vortex operators give returned near-zero pairs. A shared fair coin preserves winding where independent resampling destroys it | "zero returned core pairs is not a theorem of absence". No index theorem |
| Correction packet | CORR:3-7 | history | Ten findings F1-F10 corrected across #7973/#7989/#7991. F6: "replaces the false universal order exclusion with the full nonempty 57 orbit table" | No grade; formal audit deferred "until a solid TOE" |
| Handed rule census | PSEUDO:32-52, 54-59, 61-70, 72-84, 518-532 | bounded_theorem; proposed_retained | On the six-axis Bloch alphabet, handed covariant rule terms exist in all three readings: dims 90 (unsoldered SO3), 43 (O3), 4540 (soldered). In the soldered reading the lowest is the DM curl v·A_DM. Exact parity-odd record correlators are negated by the mirror rule and killed if any arm is unrecorded when the centre forms | Does not say which reading is realized, or that any fermion-parity result is affected (:531-532). The 3×3×3 window was not run |
| Moriya handedness in dynamics | `docs/DYNAMICS_CLAUSE_MORIYA_HANDEDNESS_..._2026-09-24.md`:24-44 | bounded_theorem | The DM bond is an XXZ bond twisted by φ. The twist is a gauge on a line and not on bent graphs or the cube. Records see −2 sinφ (a×b)·e | Uses a supplied, non-adopted clause; makes no fermion claim |
| T-odd star terms | `docs/DYNAMICS_CLAUSE_TIME_REVERSAL_ODD_STAR_TERMS_..._MAJORANAS_FREE_..._2026-09-24.md`:24-41 | bounded_theorem; unaudited | Covariant T-odd star terms exist. None keeps the cube carving's Majoranas free: Kitaev's term is never covariant, and the tripod is quartic | Does not exclude record-content fields, terms reaching recorded sites, or other carvings (:38-41) |
| Order-blind soldered escape (chiral pair defined) | OB0922:48-59, 212-256, 325-335 | bounded_theorem; bounded-support | Unsoldered order-blind positive rules are constant. Soldered: on the 48-point **chiral pair** (both proper orbits of (1,2,3)), chirality ±1 on the a·d=3 caps gives a varying order-blind rule (:243-249) | "generic orbits beyond the exhibited rules, higher-rank bond spaces, and mixed alphabets are not classified" (:329-331) |
| Achiral (0,1,2) orbit | ACH012:77-100, 102-153, 155-201, 203-216 | bounded_theorem; proposed_retained; bounded-support | The 24-point orbit is achiral: proper orbit = full orbit, so it does not split into a chiral pair. The transverse-sign factor vanishes on it. The axis-role ε factor is varying, order-blind and mirror-fixed | (1,1,2), (1,2,2), mixed alphabets and rank>1 bond spaces stay unclassified. κ is not selected |
| Chiral-pair bond space | CP-BOND_FACTOR_DIMENSION:71-105 | bounded_theorem; proposed_retained | On the 48 signed permutations of (1,2,3), the soldered bond-symmetric factors span 312 dims, and the normalised ones form a 300-dim affine space | "strongest missing lemma is whether order-blindness cuts this affine space" (:104-105) |
| One-orbit bond space | `docs/ONE_ORBIT_BOND_FACTOR_DIMENSION_..._2026-10-10.md`:59, 85 | proposed_retained | 84 dims, 78 normalised, on one 24-point orbit | Does not settle whether order-blindness cuts it to one line |
| Height-line cut | CP-HEIGHT_LINE_ORDER_BLIND_CUT:96-102, 132 | open_gate | A height-linear line in the 300-dim space is not order-blind (mean 71/50≠1), so order-blindness does cut the space | No order-blind factor is exhibited off the chiral-cap line |
| Partner-kernel programme (~65 CP notes) | e.g. CP-EVEN_SPAN_PARTNER_KERNEL:95-98, 150-151, 184-185; CP-CROSS_HEIGHT_PARITY_SPAN_CROSS_MOMENTS:86-121; CP-TWO_PARITY_EXCLUDED_PARTNER_KERNEL:112, 192; CP-CAP_SUM_CHIRALITY_SCALE:89 | all open_gate, "partial narrowing with an incomplete formal no-go packet" | Bond factors are built from ten named kernels: chirality cap, transverse-sign cap, sign product, swapped/matched/orthogonal crosses, parallel/oblique dots, and others, at "heights" a·d∈{1,2,3}. The **partner kernel** of a source-height vector is the space of partner-height vectors with every kernel cross sum zero, a necessary condition for normalised neighbour products and hence for order-blindness via OB0922 Th2. Results are exact ranks: odd pairs only with even and vice versa; a mixed vector pairs only with 0; many combinations "keep partner rank 10" | Each is a restricted ansatz. "Do not claim the ten-kernel coefficient span is settled". The full soldered bond space is not classified |
| 168/72 split | UNEQ:4, 89-101, 103-110, 112-116 | open_gate | On the **one proper 24-orbit** (not the 48-point pair), a corrected linear monomial test eliminates the unequal block in 168 of 240 ordered unequal-plus-partner cases. The prior all-240 claim is withdrawn after a symmetric cross-term assembler bug | The 72 cases are unresolved, which is "not evidence that a nonzero solution exists" |

## (a) What was tried and failed, with reasons
1. **A one-site γ5 in `M_2(C)`** fails: ω is central (NO_PER_SITE:55-65).
2. **Post-record readout as the chirality source** is pruned. Signed spectra commute with gradings, and counts update only after a readout is chosen (RECORD_TYPING:58-68).
3. **Registration sourcing the Koide chiral carrier** fails because D commutes with Γ_χ (REGISTRATION:25-36).
4. **Openness-level chiral rules** are impossible (COV0703:60-67).
5. **Label-equivariant ternary tables** are all mirror-symmetric (MIRROR:33-35).
6. **NN-determined G+-equivariant chiral labelling on 4-occupied stars** fails: N_stab_ok=0 over all 15 masks, and lock-ticks give no repair (ARC:31-36).
7. **The universal "no covariant rule registers handedness" claim** (original #7991) was **false**. It is withdrawn and replaced by the 57-menu counterexample (SWEEP:146-152; CORR F6).
8. **Original broad titles** ("movers are T-images with identical record laws", "screw sense registers nothing", "fair coin destroys winding") were narrowed. Identical laws hold only for fixed-basis conjugation (MIRROR:58-66). Cancellation needs a symmetric *weighted* measure (SWEEP:82-89). The independent-resampling destruction is an auxiliary protocol; a shared coin preserves winding (WIND:121-126).
9. **The all-240 elimination** was withdrawn because of an assembler bug (UNEQ:103-110).
10. **The height-linear chiral-pair line** is not order-blind (CP-HEIGHT_LINE:96-102).
11. **The T-odd star term keeping Majoranas free on the cube** fails within its class (DYNAMICS_CLAUSE T-odd:29-36).
12. **A mirror axiom** was considered and rejected as over-strong because it would forbid weak chirality (ACHMIN0704:29-31). Hard-coding one hand was also rejected (MATTER0714:261-266).

## (b) Tests pre-registered or named but not run
- PSEUDO next_trace (:97): take the degree census to the 3×3×3 window (6^27 configurations, not run, :521-522) and to the continuum Bloch alphabet. Test whether the emergent-fermion parity notes of 09-03 and 09-05 are consistent with a soldered handed rule. **Not run, and this is the most direct record-side→fermion test named anywhere in the slice.**
- BOOT0704:345-349: second-step propagation of achirality from an achiral A0. Not run.
- COV0703:235-242: identify the physical alphabet, and run the achirality derivation route (openness-graded dependence would upgrade proper covariance to full covariance).
- ACHMIN0704:321-325: law-achiral/state-chiral weak sector made concrete against maximal parity violation. The note names this the "Nielsen-Ninomiya / domain-wall chiral-from-achiral program". Not run.
- UNEQ:112-116: rational/real zero sets of the 72 DIRECT_TEST_UNRESOLVED pairs.
- CP-BOND_FACTOR_DIMENSION:104-105 and CP-HEIGHT_LINE:132: is there a strictly positive order-blind factor on the 48-point pair off the chiral-cap line?
- CP-EVEN_SPAN:150-151: does the swapped cross have a ten-kernel partner outside the even space? CP-TWO_PARITY_EXCLUDED:192: does chirality cap + transverse-sign cap + matched cross pair with a nonzero vector?
- MIRROR:150 and SWEEP:189: "Resolve the named supplied-model interface".
- DYNAMICS_CLAUSE T-odd:38-41: T-odd content from record contents, terms reaching recorded sites, or other carvings.

## (c) Statements of the "current wall"
- COV0703:115-116: "One bit is in question anywhere in this sector, and this note locates where it can live."
- BOOT0704:120-122: chiral A0 means "the rule has spent exactly the one orientation bit at the very first step. There is no third possibility, and no cheaper carrier."
- MATTER0714:109-111: "a chiral exact law may own its mirror-odd sign, or an achiral law may have a chiral realized domain owned by boundary/state data. Proper rotations alone force neither."
- MATTER0714:258-259: the effective chiral mode "does not by itself establish a globally undoubled chiral theory."
- RECORD_TYPING:43-44: "The last arrow is exact record information dynamics. The first arrow remains the chirality gate."
- DEFER:52-58: whether the Qubit sentence forces flip-invariance (chirality non-definable) or sign(Ψ9) is one honest Z2 bit. "Standing default: not adopted, either way."

## (d) Open gates named
1. **Structuralist reading (Ψ9 flip-invariance)**, PARKED (DEFER:50-79). Wake condition 1 is the chirality/A0 programme resuming, and condition 2 is "A weak-sector or handedness result needs the bit's status". **This exercise would trigger both.**
2. **M_4(C) Qubit-domain enlargement**, PARKED (DEFER:121-145). Its rationale reads "chirality exists only for even Clifford dimension". It gates entries 1 and 2.
3. **A0 unpaired-orbit residual.** No live lane works it as of 2026-09-05 (`archive/chains/july-qca-cubic-era.md`:137-151). The "August alphabet-exclusion / orientation bit" work is a name collision.
4. **Carrier/dynamics chirality theorem** and the CAR/Jordan–Wigner bridge (RECORD_TYPING:70-78). The staggered-Dirac realization is an axiom-memo open gate (MINIMAL_AXIOMS:178).
5. **Soldered vs unsoldered reading, and SO(3) vs O(3) internal group**, recorded as decision points and not adopted (PSEUDO:78-84).
6. **Classification of the 48-point chiral-pair bond space.** All ~65 CP notes and the 168/72 note are open_gate with incomplete N1 packets. None claims retained grade.
7. **Supplied-model interface** for MIRROR/SWEEP/WIND: physical formation process, weak coupling, and physical T (MIRROR:127-131).
8. **T-odd emergent route to K-reality** in the Koide lane (REGISTRATION:116-122).

## Notes for the exercise author
- The record-side literature consistently places chirality at **one Z2 orientation bit** (rule-level, A0-level, or presentation gauge, all identified as the same bit in the archived notes). The live alternative it keeps open is **law-achiral, state-chiral**.
- Nothing in this slice touches doublers. The only doubling statements are MATTER0714:100-107 (naive sin k has 4+4 corners, and the domain wall has an anti-wall partner) and the MIRROR T4/T5 finite string and wall counts, which are explicitly not exclusion theorems.
- Before citing ACHMIN0704's licensing step, check it against the current Qualification text, because the admission clause it quotes was later removed.
- Fermion-side items found by the synonym grep belong to other clusters and were only noted here: record-time domain walls 09-03 and 09-04 (supplied Wilson-Dirac), `STAGGERED_DIRAC_*`, `NATIVE_WEYL_*`, `THREE_GENERATION_CHIRALITY_BOUNDARY_NOTE.md`, and `historic_intake/HISTORIC_HIERARCHY_EXPONENT16_CHIRALITY_FORCED_DOUBLER_NEGATIVE_*`.

## Not reached / limits
- I read about 8 of the 82 notes from commit 516cb69d84 in full or in their Theorem sections: BOND_FACTOR_DIMENSION, EVEN_SPAN, CROSS_HEIGHT_PARITY_SPAN (theorem section), UNEQ, HEIGHT_LINE (conclusion), CAP_SPAN (conclusion), TWO_PARITY_EXCLUDED (conclusion), and SIGN_PRODUCT_OUTSIDE_BOTH_CAPS (conclusion). The rest are characterized from their H1 titles and status lines: all are open_gate except two proposed_retained dimension counts.
- I did not read every section of TRIAD0714 (814 lines), MATTER0714 beyond :1-112 and :248-266, PSEUDO Theorems 1-5 bodies, or BOOT0704 N1-N8.
- I did not open the original pre-correction notes in `originals/` beyond the correction summary.
- I did not inspect `physics-loop/mirror-asymmetric-rule-...` on origin. It appears to be the original #7989 branch, whose corrected form is on main.
