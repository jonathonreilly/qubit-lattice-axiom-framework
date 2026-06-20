# Exercise One — Assumption Ledger From A_min Up To The Three ABJ Identification Walls

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` (Exercise One)
**Slug:** abj-walls-break • **Date:** 2026-06-20 • **Slice:** EXERCISE ONE
**Posture:** framework premises are challengeable; hunt hidden / overbroad /
mis-scoped uses. Per B-AXIS lessons: load ALL FOUR approved primitives before
declaring a wall; test "is X a function of generator G" as membership in the
functional-calculus commutant `{G}'' = {f(G)}`, NOT linear `span{I,G}`; a
realized-state-DEPENDENT result is registered data, NOT a derivation.

**This is an attack map, not a closure claim.** No wall is asserted solved.
No audit verdict, no new axiom/primitive, no proposal. `docs/audit/data/`
parsed READ-ONLY.

## Framework Refresher Read (surfaces actually read for this slice)

- `docs/MINIMAL_AXIOMS_2026-06-05.md` — Lattice (`Z^3`, nearest-neighbor cubic
  adjacency; supplies NO dynamics/gauge group/particle content/species),
  Quantum (one qubit `A_x ≅ M_2(C) ≅ Cl(3,0)`; supplies NO gauge group,
  particle content, species), Record (durable K/CPT-orbit registration in a
  SUPPLIED readout context; supplies NO sector-generation rule, occupancy,
  within-sector data).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` + the four primitive
  source notes: `minimal_axioms`, `scale_reference_primitive`,
  `kinetic_isotropy_primitive` (`c_t=c_s`, the time-edge analogue of cubic
  adjacency — gives the `Z^3 x Z_tau` hypercubic regulator FORM, no dynamics),
  `realized_state_primitive` (pointwise evaluation at the law-admissible
  realized state; counterfactual clause: a value that would differ under
  another admissible state is registered data).
- `docs/audit/data/axiom_premise_nodes.json` + `tier_a_admissions.json`
  (READ-ONLY) — exactly four approved premise nodes; Tier-A genuine admissions
  are only `AC_phi_lambda` and `theta`; `Y0` (alpha=1/3) and `g0` are vacuous
  conventions, NOT derivation targets.
- `docs/ai_methodology/skills/review-loop/SKILL.md` — axiom/primitive/Tier-A
  distinction; primitives chain-satisfy WITHOUT bounding downstream rows.
- `docs/repo/CONTROLLED_VOCABULARY.md` — claim_type/effective_status enums;
  load-bearing step classes (A)-(G).
- Load-bearing wall authorities: `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02`,
  `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`,
  `CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`,
  `CL3_SM_EMBEDDING_THEOREM`, `CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05`,
  `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30`,
  `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28`,
  `KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08`,
  `STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-17`.
- In-flight de-dup map: `anomaly-baxis-wall/GROUNDING_MAP.json`, block01
  per-edge sections, and the block01 stretch note (already-pruned routes
  excluded from the "NEW attack vector" column below).

---

## The three walls (target objects, restated neutral)

- **P-REC selector** (B4; highest value, soft): on the blocked free staggered
  `2^4` carrier the spin/taste Clifford core is exact and R4 reconstruction
  `W: α_μ → γ_μ ⊗ 1_taste` exists (block01). The remaining object is the
  **single-taste selector**: the free `D_red(m,p)` has a full `M_4(C)` taste
  commutant of EXACT symmetries, so two orthogonal rank-4 single-taste
  projectors are equally invariant ⇒ picking one is registered data unless
  derived. Root: `NO_PER_SITE_CHIRALITY` (one-site `M_2(C)`).
- **P-COMP existence** (B3): the opposite-chirality SU(2)-singlet RH template
  `{u_R,d_R,e_R,n_R}` incl. neutral n=0 has no framework-native matter
  supplier; arithmetic banks but existence/minimality is walled and circular
  on its own parent. Root: `CHIRALITY_RECORD_TYPING_INTERFACE` (Record is a
  consumer of chirality, not a source).
- **P-ABJ internal** (B2): external Adler–Bell–Jackiw anomaly-to-inconsistency
  premise; internal route walled by `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO`
  (staggered ε-index = 0 on equal-sublattice even tori). Re-targeted to a
  `χ≠0 / Q≠0` internal background by `ABJ_RESIDUAL_GW_NOT_NECESSARY`.

All three funnel to the `MINIMAL_AXIOMS` gauge-group / particle-content /
species / single-taste withholding gate (P-ABJ additionally external).

---

## LEDGER A — P-REC single-taste selector (B4)

| ID | Layer | Assumption | Exp/Imp | Source / evidence | Why needed | What if wrong? | Failure mode opened | NEW attack vector (genuinely new vs block01/GROUNDING_MAP) | Test / artifact | Confidence wall holds |
|---|---|---|---|---|---|---|---|---|---|---|
| REC-1 | axiom | Per-site carrier is `M_2(C) ≅ Cl(3,0)` (odd #generators, 3) | Exp | Quantum axiom; `NO_PER_SITE_CHIRALITY` N1 (`ω=σ₁σ₂σ₃=iI`, central) | Fixes the algebra inside which a per-site γ_5 is sought | Per-site γ_5 no longer excluded; B4 might not need reconstruction | The whole "must reconstruct off-site" framing collapses | Carrier is fixed by axiom — treat as given. (No new vector; this is the root, correctly scoped.) | n/a | n/a |
| REC-2 | algebra | The OBSTRUCTION is "odd #generators ⇒ ω central" — same wall as `CLIFFORD_VOLUME_CHIRALITY` (`d_s+d_t` must be EVEN) | Exp | `CLIFFORD_VOLUME_CHIRALITY` (V): `ωγ_μ=(-1)^{n-1}γ_μω` | Pins WHY no per-site chirality: n=3 is odd | If even-`n` carrier is natively available, γ_5 is automatic | A native even-`n` carrier would supply chirality with no selector | **NEW V-REC-A: the qubit's OWN even carrier.** `CL3_SM_EMBEDDING` builds Cl(3) on the 8-dim taste space `Λ(C³)=(C²)^⊗3` where the volume element `ω=Γ₁Γ₂Γ₃` has `ω²=−I₈` and the Hamming grading `1,3,3,1` SPLITS `8=4₊⊕4₋` — i.e. an even-graded chirality already lives on ONE qubit's geometric algebra, distinct from the per-site `M_2(C)` where `ω=iI`. Block01 reconstructed chirality on the BLOCKED `2^4` carrier (4 sites); it never tested whether the SINGLE-site `Λ(C³)` chiral split is the physical chirality, sidestepping the multi-site taste-selector entirely. | Build `γ_μ=e_μ∧−ι_{e_μ}` on `Λ(C³)`; check `ω²=−I₈`, `4₊/4₋` split; test whether `{ω, D_KD}=0` for the Kähler-Dirac `D=d−δ`; check if the chiral grading is selector-FREE (single carrier, no taste-copy to pick among) | medium-high (the split exists but identifying it with SPACETIME chirality is the open step) |
| REC-3 | reconstruction | Free taste-reconstruction `W: α_μ→γ_μ⊗1_taste` exists; chirality is `Γ₅^spin` | Exp | block01 R4 (residual 1.9e-15); `LORENTZ_BOOST` `D_red(p)` | Closes the free kinematic content of B4 | (already true) | — | (Banked; not re-attacked) | runner re-verify | n/a |
| REC-4 | selector | A SINGLE taste must be selected to get an irreducible Dirac factor | Exp | block01 R4 PART 3.5: `M_4(C)` taste commutant, 2 invariant rank-4 projectors | Without it, chirality is `γ_5⊗1_taste` (4 copies) not one Dirac γ_5 | If selection is unnecessary, the wall dissolves | The consumer (keystone B4) might only need taste-singlet γ_5, not single-taste | **NEW V-REC-B: does the keystone actually CONSUME single-taste, or only the taste-SINGLET `Γ₅^spin`?** Block01 proved `Γ₅^spin` is already a taste-SINGLET (commutes with the full taste commutant). The anomaly/chirality the keystone needs (B4→B5 even-dimension) may be satisfied by the taste-singlet operator alone — re-read B4's exact consumption point. If B4 needs only `{Γ₅^spin, D}=0` (which block01 PROVED), the selector is not load-bearing for the keystone and the wall is a REFRAME, not a derivation gap. | Extract verbatim what `anomaly_forces_time_abj...bridge` step B4 consumes; check whether "single-taste" appears in the load-bearing sentence or is an over-statement of the actually-needed "taste-singlet γ_5 exists" | medium (reframe candidate — partial unlock of 1105 if B4 only needs taste-singlet) |
| REC-5 | selector | The selector requires interacting/gauged dynamics + taste restoration + OS/continuum reconstruction | Exp | block01 named wall | States the missing object | If a STATIC framework structure breaks taste degeneracy, no dynamics needed | A non-dynamical taste-symmetry-breaking lives in Record/realized-state | **NEW V-REC-C: realized-state as taste-symmetry-breaker, tested by the counterfactual clause.** block01 used the realized-state clause only NEGATIVELY (to label single-taste as registered data). It did NOT test the converse: is there a realized-state functional already-defined elsewhere whose pointwise value PICKS a taste sector invariantly? The `realized_state_primitive` grants pointwise evaluation; if the physical history's Record (K/CPT orbit of the realized central sector) lands the matter in ONE central sector, that sector selection may be a record-DEFINED (not law-defined) single-taste choice — which is exactly "registered data," but registered data the keystone is ALLOWED to consume as a supplied input (primitives chain-satisfy). The wall may then be "P-REC is conditional on supplied realized-state data," NOT "P-REC is underivable." | Check whether Record's central-sector decomposition on the taste carrier is non-trivial; if the K/CPT orbit is a single rank-4 projector, test invariance over the law-admissible family; classify as supplied-input (conditional) vs derivation | medium |
| REC-6 | signature | The Lorentzian sign ε=−1 (Cl(3,1) over Cl(4,0)) is admitted/delegated | Exp | `CL3_TO_CL31` (S4): (3,1) is the UNIQUE single-`M_k(R)` extension of Cl(3,0); (4,0)≅M_2(H) is the Euclidean branch | Needed for the spacetime (3,1) γ_5 to be Lorentzian | If ε=−1 is forced internally, one admitted input drops | The Euclidean Cl(4,0) branch is excluded by something native | **NEW V-REC-D: the kinetic-isotropy primitive may already SELECT ε via reflection positivity on the `Z^3 x Z_tau` block.** `CL3_TO_CL31` delegates ε to `ANOMALY_FORCES_TIME_THEOREM` / reflection-positivity. But `kinetic_isotropy_primitive` was approved (2026-06-09) AFTER that delegation and supplies the hypercubic `Z^3 x Z_tau` OS0 form. The Euclidean Cl(4,0) (ε=+1, compact Spin(4)) is the EUCLIDEAN regulator; the Wick-rotation to the physical (3,1) is exactly the OS reconstruction the isotropy primitive's `c_t=c_s` block sets up. Test whether OS reflection positivity on the isotropic block forces the real-matrix (M_4(R)) reconstruction (Lorentzian) over M_2(H). This is an approved-primitive route not available when CL3_TO_CL31 was written. | Construct the OS transfer matrix on the `c_t=c_s` block; check whether positivity + the single-`M_k(R)` criterion (S4) jointly force ε=−1 without an extra admission | low-medium |
| REC-7 | even-dim | Chirality⇒`d=d_s+d_t` even ⇒ with `d_s=3`, `d_t` odd | Exp | `CLIFFORD_VOLUME_CHIRALITY` (★) | The keystone's B5→B6 step | (sound) | — | (Banked) | runner | n/a |
| REC-8 | implicit | "Irreducible Dirac factor" is the right target object (vs Kähler-Dirac multiplet) | **Imp** | block01 framing; B4 wording | Assumes physical fermion = single Dirac irrep, requiring de-tasting | If the physical object is the Kähler-Dirac multiplet, no de-tasting needed | The whole single-taste problem is an artifact of demanding a Dirac irrep | **NEW V-REC-E: drop the "single Dirac irrep" requirement.** `STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE` shows the staggered carrier IS naturally the Kähler-Dirac form complex `Λ*(C^d)` (graded bijection Hamming↔form-degree). If the consumer can accept a Kähler-Dirac (taste-full) chirality — which has an exact `γ_5` with no selector — then P-REC's load-bearing claim "ε→spacetime γ_5 on the irreducible Dirac factor" is over-specified; the honest target is "ε vs the taste-singlet KD chirality," and the latter EXISTS. Reframe boundary: object (Dirac irrep) vs readout (KD chirality grading). | Check whether the keystone's downstream consumers (the d_t-odd conclusion) actually need a single Dirac irrep or only an even-graded chirality operator; KD `Γ₅` already satisfies even-dim | medium |

**P-REC cluster of "what if wrong?" → routes:**
- **Route R-α (single-carrier chirality):** V-REC-A + V-REC-E + REC-2. Challenge
  REC-8's "Dirac irrep" target. The qubit's own `Λ(C³)` / Kähler-Dirac complex
  already carries an even-graded `γ_5` with `ω²=−I₈`; no multi-site taste
  selector. Expected artifact: a runner showing `{ω_{Λ(C³)}, D_{KD}}=0` and the
  `4₊/4₋` split, plus a re-read of B4's exact consumption. Risk: identifying the
  internal chiral split with SPACETIME chirality is itself a bridge (could just
  relocate the wall). First test: does B4 need a Dirac irrep or a γ_5 operator?
- **Route R-β (consumer reframe):** V-REC-B. Prove the keystone only needs the
  taste-SINGLET `Γ₅^spin` (block01-proven to exist), not single-taste. If so,
  P-REC is reframed away for the consumer — a partial unlock of the 1105 cone.
  Expected artifact: verbatim B4 consumption extract + a note demoting the
  single-taste claim to non-load-bearing. Risk: B4 may genuinely need it.
- **Route R-γ (supplied realized-state selector):** V-REC-C. The selector may be
  legitimately supplied as realized-state data (primitives chain-satisfy), making
  P-REC conditional-not-underivable. Risk: stays registered data (a conditional,
  not a derivation) — but that is still a status improvement over "walled."
- **Route R-δ (OS signature):** V-REC-D + REC-6. Use the post-2026-06-09
  kinetic-isotropy primitive to force ε=−1 via reflection positivity. Risk:
  positivity may be compatible with both signs.

---

## LEDGER B — P-COMP opposite-chirality RH completion existence (B3)

| ID | Layer | Assumption | Exp/Imp | Source / evidence | Why needed | What if wrong? | Failure mode opened | NEW attack vector | Test / artifact | Confidence wall holds |
|---|---|---|---|---|---|---|---|---|---|---|
| COMP-1 | axiom | Record is a CONSUMER of chirality, not a source | Exp | `CHIRALITY_RECORD_TYPING_INTERFACE` result table | Root reason no native RH supplier | If Record can TYPE a second chirality via its readout, a supplier exists | Native RH completion becomes constructible | **NEW V-COMP-A: the second chirality as the Cl(3,0) complexification's OTHER summand.** `CL3_COMPLEXIFICATION_SPLIT` (cited but not exploited here) gives `Cl(3,0)⊗_R C ≅ M_2(C) ⊕ M_2(C)` — a chirality PAIR. The LH 6+2 surface lives in one summand (`CL3_SM_EMBEDDING` builds it). The OTHER `M_2(C)` summand is the native opposite-chirality carrier that `CHIRALITY_RECORD_TYPING` says Record cannot produce — but the complexification split PRODUCES it algebraically, independent of Record. Test whether the RH template `{u_R,d_R,e_R,n_R}` populates the second summand with the forced `{4a,−2a,−6a,0}` hypercharges. Block01 said "no native opposite-chirality slot"; the split says there ARE two summands. | Decompose `(C²)^⊗3` under the complexification split; check whether the second `M_2(C)` summand carries an SU(2)-singlet, color-(3̄+3̄+1+1) content matching the template; if yes, EXISTENCE is native (Record only reads it) | medium |
| COMP-2 | carrier | Taste carrier `V=(C²)^⊗3` (dim 8) splits into ONLY the LH 6+2 surface | Exp | block01 Route 1 (`CL3_SM_EMBEDDING` recompute) | Asserts single chirality, no RH slot native | If the dim-8 carrier also holds the RH content (in the even/odd grading), no adjoining needed | RH completion is already inside the qubit triple | **NEW V-COMP-B: the Hamming-odd sector of `Λ(C³)`.** `CL3_SM_EMBEDDING` uses the EVEN-parity L-sector `{|000⟩,|011⟩,|101⟩,|110⟩}` (Hamming 0,2) for the LH content + Kramers `det(H_L)≥0`. The ODD-parity sector (Hamming 1,3: `{|001⟩,|010⟩,|100⟩,|111⟩}`) is the COMPLEMENTARY chirality block under the `1,3,3,1` split — exactly the opposite-chirality 4-dim space. Block01 looked at the dim-8 carrier as "LH 6+2 only" but the volume-element chirality `8=4₊⊕4₋` says the odd sector is the RH partner. Test whether the odd sector carries the SU(2)-singlet RH quantum numbers. | Compute Y, SU(2), SU(3) action on the Hamming-odd 4-dim sector; compare to `{u_R,d_R,e_R,n_R}`; check if it is SU(2)-singlet (the defining template property) | medium-high |
| COMP-3 | arithmetic | Cancellation forces `{x,y,z,n}={4a,−2a,−6a,0}` up to swap | Exp | block01 core (PASS=49); GROUNDING_MAP P-COMP branch | The bankable arithmetic | (sound, banks) | — | (Banked) | runner | n/a |
| COMP-4 | neutral | n=0 (neutral singlet n_R) is load-bearing | Exp | block01 counterexample `(0,2a,−2a,−4a)` | Without n=0, SM uniqueness fails | If n=0 is forced by a native structure, the admission drops | n_R neutrality is derived, not a branch convention | **NEW V-COMP-C: n_R = the K/CPT-self-conjugate (Majorana) central sector of Record.** Record registers the K/CPT ORBIT of the realized central sector. A neutral singlet (Y=0, all charges 0) is the UNIQUE matter content that is its own K/CPT conjugate (self-conjugate orbit = singleton orbit). The other states pair under K/CPT into charge-conjugate orbits. So n=0 may be FORCED as "the central sector whose K/CPT orbit is a fixed point" — a Record-structural statement, not a branch convention. P2_KCPT no-go ruled out K/CPT supplying the TEMPORAL factor of 2; it did NOT address K/CPT fixed-point ⇒ neutral content. Distinct target. | Build the K/CPT action on the candidate matter sectors; identify fixed points (self-conjugate orbits); test whether the neutral singlet is the unique Y=0 fixed point and whether that forces n=0 invariantly (counterfactual clause) | medium |
| COMP-5 | uniqueness | Vectorlike/mirror completions are excluded (matter is chiral) | Exp | block01 Route 2 leg (a): vectorlike is anomaly-free with NO chiral template | Needed for the SM template to be THE completion | If chirality is not native, vectorlike cannot be excluded | The completion is non-unique; selection premise required | **NEW V-COMP-D: chirality of the completion is forced by the SAME odd/even split, not a separate premise.** If V-COMP-B succeeds (RH = Hamming-odd sector), the completion is automatically OPPOSITE-chirality (odd grading) — a vectorlike (same-chirality) partner would have to live in the SAME even sector as the LH content, which is already fully occupied by the 6+2 surface (dim 4 even sector is exhausted). So the even-sector exhaustion EXCLUDES a vectorlike partner: there is no room. This converts block01's "separate selection premise" into a dimension-counting consequence. | Count even-sector dimension (4) vs LH content (needs the 6+2 = but on the 4-dim even L-sector with weak-doublet fiber); verify the even sector is saturated so a same-chirality mirror cannot be added without enlarging the carrier | medium |
| COMP-6 | circularity | P-COMP is "circular on its own parent" | Exp | block01 §2.2; GROUNDING_MAP | The structural blocker for banking existence | If existence is sourced from carrier structure (V-COMP-A/B/D), the circularity breaks | Existence banks deps-all-retained | This is the PAYOFF condition: V-COMP-A/B/D all route existence through `CL3_SM_EMBEDDING` + `CL3_COMPLEXIFICATION_SPLIT` (carrier algebra), NOT through the keystone parent — breaking the circularity. | If the odd-sector RH content checks out, the existence claim depends only on the carrier-algebra notes, not the keystone | medium |
| COMP-7 | implicit | "Template existence" means a SEPARATE adjoined sector | **Imp** | block01 "the RH completion must be adjoined" | Frames RH as external to the qubit triple | If RH is internal (V-COMP-B), nothing is adjoined | The "no native supplier" wall is an artifact of looking only at the even sector | (Subsumed by V-COMP-B — the implicit "adjoin" assumption is the hidden over-restriction) | n/a | n/a |

**P-COMP cluster of "what if wrong?" → routes:**
- **Route C-α (internal RH sector):** V-COMP-B + V-COMP-D + COMP-2. The biggest
  lever. The Hamming-ODD sector of `Λ(C³)` (the `4₋` chirality block) is the
  native opposite-chirality SU(2)-singlet carrier block01 said does not exist —
  block01 only inspected the even L-sector. Expected artifact: a runner computing
  Y/SU(2)/SU(3) on the odd sector and matching `{u_R,d_R,e_R,n_R}`. If it
  matches, existence + opposite-chirality + vectorlike-exclusion all follow from
  carrier structure, breaking the circularity (COMP-6) → existence becomes
  deps-all-retained bankable. Risk: the odd-sector quantum numbers may not match
  the RH template (e.g., color 3̄ vs 3); decisive either way.
- **Route C-β (complexification summand):** V-COMP-A + COMP-1. The second
  `M_2(C)` of `Cl(3,0)⊗C` is the native RH carrier; `CHIRALITY_RECORD_TYPING`'s
  "Record is not a source" is true but irrelevant because the SPLIT (not Record)
  supplies it. Risk: the split may be the SAME object as the odd/even grading
  (Route C-α) viewed differently — converge.
- **Route C-γ (K/CPT neutral fixed point):** V-COMP-C + COMP-4. Derive n=0 as the
  unique K/CPT self-conjugate Y=0 sector. Risk: stays a convention if the
  fixed-point structure is not unique.

---

## LEDGER C — P-ABJ internal anomaly-to-inconsistency (B2)

| ID | Layer | Assumption | Exp/Imp | Source / evidence | Why needed | What if wrong? | Failure mode opened | NEW attack vector | Test / artifact | Confidence wall holds |
|---|---|---|---|---|---|---|---|---|---|---|
| ABJ-1 | external | ABJ anomaly-to-inconsistency is irreducibly external (standard physics) | Exp | `ANOMALY_FORCES_TIME_THEOREM` L88; Adler/Bell-Jackiw | The premise the keystone admits | If an internal `χ≠0`/`Q≠0` background exists, the internal route reopens | Internal index witnesses the anomaly | (See ABJ-3..6 for the live internal rays) | — | high (external) but the INTERNAL route has live rays |
| ABJ-2 | substrate | The A_min substrate is the closed hypercubic `Z^4` (`Z^3` + `c_t=c_s` time edge) | Exp | `kinetic_isotropy_primitive`; block01 R-A | Fixes the complex on which the index is computed | If A_min admits a non-hypercubic / curved complex, `χ≠0` is reachable | The square-block no-go (which needs equal sublattices) is escaped | **NEW V-ABJ-A: A_min Lattice supplies the `Z^3` SITE SET but NOT the cell complex / cochain dimension.** The square-block no-go and the `χ=0` facts assume the GRAPH (1-skeleton, nearest-neighbor edges). But the anomaly is a COCHAIN/cohomology object. `MINIMAL_AXIOMS` Lattice gives "site set `Z^3` + nearest-neighbor cubic adjacency" — it does NOT specify the higher cells (plaquettes, cubes). The Euler characteristic and the ε-imbalance are properties of the FULL cell complex, not the graph. Block01 enumerated hypercubic TORI (varying edge LENGTHS) but kept the cubic cell structure. A_min does not forbid the natural cubical complex `□^3` with all faces — whose `χ` and cohomology differ from the graph. Test whether the FULL cubical cochain complex on `Z^3` (with `c_t=c_s` time) admits a non-zero Kähler-Dirac / 't Hooft anomaly coefficient. | Build the full cubical de Rham/cochain complex on a finite `Z^3×Z_tau` block; compute `χ` of the COMPLEX (not the graph) and the Catterall KD anomaly coefficient; the all-odd-torus result was for the GRAPH ε-grading | medium |
| ABJ-3 | grading | The chirality grading is the site-parity `ε(x)=(-1)^{Σx}`; `{ε,D}=0` GAPS the substrate | Exp | `ABJ_EPSILON_INDEX_SQUARE_BLOCK`; `ABJ_RESIDUAL_GW` (G1): `H(m)²=K²+m²I` ⇒ flow=0 | The exact obstruction (ε is BOTH the chirality and the gapper) | If the physical chirality is NOT ε but the Kähler-Dirac `γ_5`, the index need not vanish | A different (taste-singlet) grading evades the square-block | **NEW V-ABJ-B: use the Kähler-Dirac chirality `ω_{Λ(C³)}` (the SAME object as V-REC-A), whose Euler characteristic on the qubit is computed and EQUALS 0 — but on a non-trivial REALIZED matter state need not.** Decisive cross-link: `KOIDE_KAHLER_DIRAC...` runner A computes the de Rham/KD Euler char on `Λ(C³)` as `1−3+3−1 = 0` on the VACUUM/static complex. But the ABJ anomaly is sourced by a non-trivial gauge/matter BACKGROUND, and `ABJ_RESIDUAL_GW` says the open residual is exactly `χ≠0`/`Q≠0`. The realized-state primitive supplies a law-admissible matter state; `INDUCED_HOLONOMY_MATTER_STATE` (realized-state register entry 2) shows the derived curvature is "exactly flat on the sea and state-dependently NON-FLAT off it." So a realized matter state OFF the sea may carry the `χ≠0`/holonomy the flat vacuum lacks — exactly the missing P-ABJ background, supplied as realized-state data (chain-satisfies). Block01 R-A/R-B/R-C tested only FLAT/vacuum and injected-external backgrounds; it never tested a realized OFF-SEA matter state. | Take the `INDUCED_HOLONOMY_MATTER_STATE` off-sea state; compute the staggered/KD index `A[1,U]` on it; test whether the state-dependent non-flat holonomy gives `Q≠0` invariantly under the law-admissible family (counterfactual: if it's flow-0 for all admissible states, registered data cannot help) | medium |
| ABJ-4 | balance | Equal `ε`-sublattices ⇒ `B` square ⇒ `BB†`,`B†B` isospectral ⇒ `A_t=0` | Exp | `ABJ_EPSILON_INDEX_SQUARE_BLOCK` theorem | The exact mechanism of the no-go | Imbalance (`χ≠0`) breaks it but block01 showed all-odd-torus also destroys chirality | The χ≠0 ⇔ chirality-destroyed exclusivity (block01 sharper fact) | block01 already proved: χ≠0 (imbalance) ⇔ all-odd ⇔ chirality destroyed in EVERY direction. This is a real wall on the HYPERCUBIC GRAPH. (No new vector at the graph level — V-ABJ-A/B move OFF the graph/onto the complex/realized state.) | — | high (on the hypercubic graph) |
| ABJ-5 | index | The right index is the heat-kernel `Tr[ε e^{-tD†D}]` (K0) or overlap (K1) | Exp | `ABJ_RESIDUAL_GW` (G1,G2); block01 R-B | Both vanish by ε-gap on flat | If a NON-abelian-cohomology / 't Hooft anomaly (not an index) is the object | The anomaly is a partition-function phase, not a mode-count | **NEW V-ABJ-C: the 't Hooft anomaly as a `U(1)→Z_4` phase (Catterall), not a heat-kernel index.** `ABJ_RESIDUAL_GW` CITES Catterall's exact `U(1)→Z_4` 't Hooft anomaly at finite spacing for Kähler-Dirac fermions, "exposed only in curved space, χ≠0." Block01 attacked the heat-kernel/overlap INDEX (a number) and the gauge topological charge `Q`. It did NOT attempt the 't Hooft anomaly as a discrete `Z_4` PHASE under the framework's native `C_3`/cyclic structure. The framework has native `Z_3`/`C_3` symmetry (the generation cycle, `cl3_color_automorphism`); a discrete 't Hooft anomaly of a native discrete symmetry is a partition-function phase that does NOT require `χ≠0` of the spacetime complex — it requires the discrete symmetry to act anomalously. This is a categorically different object (anomaly inflow of a finite group), untouched by the square-block (which is about a continuous index). | Set up the framework's native discrete symmetry (`C_3` or the `Z_4` axial of the Kähler-Dirac complex); compute its 't Hooft anomaly via the finite-group SPT/inflow class (Catterall route translated to repo objects); check non-triviality WITHOUT needing `χ≠0` | low-medium (the most speculative; needs the discrete symmetry to act anomalously) |
| ABJ-6 | implicit | The internal route must REPRODUCE the continuum ABJ to discharge P-ABJ | **Imp** | keystone B2 framing | Sets a high bar (full anomaly-to-inconsistency) | If the keystone only needs `Tr[Y³]≠0` (already banked) PLUS a generic unitarity obstruction, the internal index is not needed | P-ABJ reframes to a unitarity/Ward-identity statement | **NEW V-ABJ-D: reframe P-ABJ from "exhibit an internal index" to "the banked `Tr[Y³]=−16/9 ≠ 0` PLUS a framework-internal unitarity obstruction."** The arithmetic core (`Tr[Y³]≠0`, banked) is the anomaly COEFFICIENT. The external admission is "nonzero coefficient ⇒ non-unitary." But the framework HAS a unitarity/positivity structure: Record's K/CPT + reflection positivity (the OS axioms the kinetic-isotropy primitive invokes). A non-zero anomaly coefficient breaks the Ward identity ⇒ breaks reflection positivity / current conservation on the lattice — which IS a framework-internal inconsistency (the OS-positive transfer matrix fails). This routes the "inconsistency" half through the framework's own positivity rather than importing the continuum ABJ implication. Block01 treated P-ABJ as monolithically external; it never split the COEFFICIENT (internal, banked) from the IMPLICATION (currently external) and tried to source the implication from OS positivity. | Check whether a non-conserved (anomalous) U(1)_Y current on the `c_t=c_s` OS block breaks reflection positivity of the transfer matrix; if non-conservation ⇒ non-positive transfer ⇒ the framework's own consistency fails, the implication is internalized | low-medium |

**P-ABJ cluster of "what if wrong?" → routes:**
- **Route A-α (full cell complex, not graph):** V-ABJ-A + V-ABJ-B. A_min fixes the
  `Z^3` SITE SET + adjacency but not the higher cochain complex; the anomaly is a
  cochain object. Compute `χ` and the KD 't Hooft coefficient on the FULL cubical
  complex (and on a realized off-sea matter state with state-dependent non-flat
  holonomy). Expected artifact: a runner computing the KD index on the full
  complex / off-sea state vs the graph-only result. Risk: the cubical complex on a
  torus may still have `χ=0`; the off-sea state may be flow-0 for all admissible
  states.
- **Route A-β (discrete 't Hooft anomaly):** V-ABJ-C. Attack the anomaly as a
  finite-group (`C_3`/`Z_4`) SPT phase, not a continuous index — categorically
  outside the square-block no-go. Risk: most speculative; needs the discrete
  symmetry to be anomalous.
- **Route A-γ (split coefficient from implication):** V-ABJ-D + ABJ-6. Bank the
  anomaly COEFFICIENT (done) and source the "⇒ inconsistency" IMPLICATION from
  the framework's OWN reflection positivity / K/CPT, internalizing the half that
  is currently imported. Risk: lattice current non-conservation may not directly
  break OS positivity.

---

## Cross-wall structural observations (the load-bearing meta-findings)

1. **One algebraic object spans all three walls: the qubit's `Λ(C³)` /
   Kähler-Dirac complex with chirality `ω`, `ω²=−I₈`, grading `1,3,3,1`,
   `χ=1−3+3−1=0`.** It is the even carrier P-REC needs (V-REC-A/E), the home
   of the opposite-chirality RH sector P-COMP needs (V-COMP-B, the Hamming-odd
   `4₋` block), and the object whose `χ=0` is the P-ABJ obstruction on the
   vacuum (V-ABJ-B). Block01 attacked each wall on a DIFFERENT carrier (P-REC on
   the blocked `2^4`, P-COMP on the `(C²)^⊗3` even sector, P-ABJ on the
   hypercubic torus graph) and never unified them on `Λ(C³)`. **This is the
   single highest-value new lens.**

2. **The per-site `ω=iI` (NO_PER_SITE_CHIRALITY) and the taste-space `ω²=−I₈`
   (CL3_SM_EMBEDDING) are DIFFERENT objects.** The no-go is about `M_2(C)`
   (n=3 odd). The embedding is about `(C²)^⊗3` / `Λ(C³)` (an even-graded
   8-dim chirality). The walls cite the no-go as if it forecloses ALL internal
   chirality, but it only forecloses the ONE-site `M_2(C)` route. The
   `Λ(C³)` chirality is OUTSIDE the no-go's scope (its own N7 steelman /
   corollary C2 explicitly says a larger Clifford algebra can supply chirality).
   This is exactly the B-AXIS failure mode: a wall scoped to a bare object,
   re-cited as if it covers an approved/larger structure.

3. **The realized-state primitive (approved 2026-06-11) is under-used.** Block01
   used its counterfactual clause only to LABEL things as registered data
   (negative use). Its POSITIVE grant — pointwise evaluation at a supplied
   law-admissible state, chain-satisfying without bounding — was never used to
   SUPPLY a selector (P-REC, V-REC-C) or a non-flat background (P-ABJ, V-ABJ-B)
   as a legitimate conditional input. A result conditional on supplied
   realized-state data is a status improvement over "walled."

4. **The kinetic-isotropy primitive (approved 2026-06-09) post-dates the
   CL3_TO_CL31 signature delegation and the square-block no-go framing.** Its
   `c_t=c_s` OS0 block is a NEW approved structure available for the ε-signature
   (V-REC-D) and the OS-positivity internalization of P-ABJ's implication
   (V-ABJ-D). Routes written before it under-scoped to bare three axioms.

5. **All three walls share the consumer-reframe opportunity.** P-REC may need
   only the taste-singlet `Γ₅^spin` not single-taste (V-REC-B); P-ABJ may need
   only the banked coefficient + internal positivity not a full index (V-ABJ-D).
   The B-AXIS lesson "a wall scoped to bare-A_min may be OPEN under a primitive
   / a narrower consumer need" applies to all three.

---

## Honest status (no closure asserted)

No wall is solved. Every NEW vector above is a first-artifact-level attack map
entry, not a derivation. The highest-confidence cross-wall lever is the
unified `Λ(C³)` / Kähler-Dirac lens (observation 1): it is genuinely new (each
block01 edge used a different carrier), it is built from retained-grade carrier
algebra (`CL3_SM_EMBEDDING`, `CL3_COMPLEXIFICATION_SPLIT`,
`STAGGERED_DIRAC_SUBSTEP2_KAHLER_DIRAC_EQUIVALENCE`), and it bears on all three
walls at once. The decisive first test is small and finite: compute the
quantum numbers and chirality grading of the Hamming-odd sector of `Λ(C³)`
(P-COMP V-COMP-B) and the KD chirality `{ω,D_KD}=0` (P-REC V-REC-A) on one
qubit's geometric algebra. Per the exercise skill, the normal output is a
better attack map, which this is.
