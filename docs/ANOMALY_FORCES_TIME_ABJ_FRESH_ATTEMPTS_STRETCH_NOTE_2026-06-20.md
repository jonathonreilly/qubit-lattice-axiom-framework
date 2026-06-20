# ANOMALY_FORCES_TIME ABJ — Fresh Per-Edge Attempts + Bounded-Core Banking (Block 01)

**Type:** stretch_attempt + bounded-core-banking
**Date:** 2026-06-20
**Branch:** physics-loop/anomaly-abj-bridge-block01-20260620
**Keystone under audit:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (ledger=unaudited; fanout 1105)
**Parent:** `anomaly_forces_time_theorem` (ledger=unaudited)

```yaml
Type: stretch_attempt + bounded-core-banking
Status: arithmetic cores BANKABLE (3 deps-all-retained bounded theorems); four physical identifications WALLED (honest, non-bare); no crack
proposal_allowed: false
bare_retained_allowed: false
audit_required_before_effective_retained: true
```

## 0. Scope and ground rules (what this note is and is not)

This is the Block-01 synthesis of FIVE genuine fresh attacks on the four premise
edges of the ABJ accepted-premise bridge, run from **A_min** (Lattice + Quantum +
Record) plus the **four approved primitives** in `docs/audit/data/axiom_premise_nodes.json`
(`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
`realized_state_primitive`). Approved primitives are LEGITIMATE premises that
chain-satisfy WITHOUT bounding downstream rows; they are NOT new axioms.

Source discipline: every load-bearing fact below was recomputed in-tree by a
numpy/sympy runner with explicit residuals and a `TOTAL: PASS=.. FAIL=..` line.
NO load-bearing fact is cited from the unaudited keystone or unaudited parent
blind. Each runner caught at least one real error where stated.

Banking-overreach guard: the physical IDENTIFICATIONS are kept as **named,
stated, admitted premises** — never silently re-imported as load-bearing inside
a banked core. The bankable artifacts are the **scale-free / label-free
ARITHMETIC cores** only, mirroring the `SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED`
precedent (ledger=retained_pending_chain, PASS=11): the audit lane retains the
arithmetic decoupled from the keystone, while the identification stays a named
premise P (not derived).

Exercise-lessons applied from the just-completed B-AXIS reassessment:
(1) primitives loaded before declaring any edge walled (no under-scope to bare
3-axioms); (2) "is X a function of generator G" tested as membership in the
functional-calculus commutant `{G}'' = {f(G)}`, NOT linear `span{I,G}`
(P-REC R3a: `epsilon` fails this test, residual 4.0); (3) realized-state-DEPENDENT
results are flagged registered data via the counterfactual clause, NOT
derivations (P-HY B1 gaugedness, P-COMP n=0, P-REC single-taste selector);
(4) genuinely new hard walls are flagged for an exercise-skill run rather than
shipped as a bare no_go.

## 1. The four premise edges (keystone consumption points)

| Edge | Keystone step | Claim consumed | Block-01 verdict |
|---|---|---|---|
| **P-HY** | B1/B3 | the bounded LH abelian eigenvalue surface {+1/3 ×6, −1 ×2} IS the physical anomaly-relevant U(1)_Y | arithmetic core BANKABLE; identification wall SHRINKS to the single "is-gauged" predicate |
| **P-COMP** | B3 | existence/minimality of the opposite-chirality SU(2)-singlet RH completion {u_R,d_R,e_R,n_R} incl. neutral n_R | arithmetic core BANKABLE (conditional on template); existence WALLED (new hard wall, circular-on-parent) |
| **P-REC** | B4 | staggered ε → spacetime Clifford γ_5 on the irreducible Dirac factor | arithmetic core BANKABLE + stronger (explicit reconstruction); single-taste SELECTOR WALLED (new hard wall) |
| **P-ABJ** | B2 | external Adler–Bell–Jackiw anomaly-to-inconsistency implication; internal route walled | external admission (by policy); internal route SHARPER-walled |

## 2. Per-edge fresh attempts

### 2.1 P-HY — hypercharge identification (outcome: shrinks_wall, cracked=no)

**Attempted from A_min + primitives.** Three routes plus an arithmetic-core
recomputation:

- **Route B1 (gauged-direction selection from Record):** tested whether
  A_min Record + approved primitives supply the narrowed claim "this canonical
  traceless u(1) direction IS the gauged U(1) entering the anomaly test."
  Recomputed in-tree from `MINIMAL_AXIOMS_2026-06-05` (Quantum/Record withhold
  gauge group, species, sector-generation rule) plus a realized-state
  counterfactual test. **Result: WALLED but SHARPENED** — the DIRECTION is
  canonical (retained graph_first); only the dynamical "is-gauged" predicate is
  withheld. Not rescuable as realized-state data (gaugedness is law-level, not
  registered).
- **Route B2 (α=1/3 as pure convention):** proved every ABJ anomaly polynomial
  is homogeneous in Y (deg-1 scales by λ, deg-3 by λ³), so {anomalies = 0} is
  invariant under Y → λY; verified λ ∈ {2, −5, 1/7}. **PARTIAL WIN** — α is
  provably pure convention FOR the anomaly test (the admission is REMOVABLE /
  harmless for the keystone B1/B3 arithmetic); it remains load-bearing only for
  the GMN physical electric-charge value match, which is the retained
  α-bridge's named P1–P4 SM conventions.
- **Route B3 (Sym²/Anti² → 3/1 from Cl(3) rep theory, label-free — the
  2026-05-02 repair target):** τ = SWAP eigendecomposition (Sym²=3, Anti²=1
  dims, no labels) + su(3) action ([λ₁,λ₂]=2iλ₃ closes, nontrivial on 3-dim ⇒
  fundamental; trivial on 1-dim ⇒ singlet). **HALF MET** — rep-content map
  derived label-free; only the species NAMING (color-charged ≡ quark) remains an
  admitted SM convention, and that name is NOT load-bearing in the anomaly
  polynomial.
- **Part A arithmetic core:** recomputed the keystone B1 trace tuple in-tree
  scale-free, `Y_a = a(P_sym − 3P_anti)`:
  `{Tr[Y]=0, Tr[Y³]=−16/9, Tr[SU(3)²Y]=1/3, Tr[SU(3)³]=2, Tr[SU(2)²Y]=0}` at a=1/3.
  Deps-all-retained on `graph_first_su3_integration_note` (retained,
  chain_closes=True). **The runner caught and I fixed a real SU(3)²-Y
  colour-counting arithmetic bug mid-cycle (3a → a) before PASS=41.**

**Absorbed, not rebuilt** (per GROUNDING_MAP duplication_warnings):
`abj-scale-free-anomaly-core` PASS=54, `abj-hypercharge-completion-boundary`
PASS=47 (B1/B2/B3 negative lemmas), `abj-phy-supplier-wiring` PASS=26,
`anomaly-hy-parent-edge` PASS=90 (cited as hygiene/precedent).

**Runner:** `scripts/frontier_abj_phy_identification_routes_2026_06_20.py` —
**TOTAL: PASS=41 FAIL=0** (cache
`logs/runner-cache/frontier_abj_phy_identification_routes_2026_06_20.txt`).

**Named wall:** the single load-bearing wall is the **"is-gauged" predicate** on
the already-canonical traceless u(1) direction: `MINIMAL_AXIOMS_2026-06-05`
withholds the gauge group / which-symmetry-is-gauged. This is strictly NARROWER
than the prior "physical U(1)_Y identification" wall — α=1/3 (B2 homogeneity
lemma) and species-naming (B3 label-free rep content) are both proven NOT
load-bearing for the anomaly test. Funnels to the same MINIMAL_AXIOMS
gauge-group/content-withholding gate as P-COMP and the P-REC/P-ABJ walls.

**Retained authority:** `graph_first_su3_integration_note` (retained,
positive_theorem, chain_closes=True — supplies gl(3)+gl(1) split + the
hypercharge-like u(1) spectrum {+1/3 ×6, −1 ×2});
`hypercharge_identification_note` (retained_bounded, chain_closes=True);
`hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25`
(retained_bounded, chain_closes=True — **in-tree ledger correction: NOT "still
conditional," contra the stale GROUNDING_MAP framing**);
`lhcm_matter_assignment_from_su3` + `lh_doublet_traceless_ratio` (both
decoration_under_graph_first_su3_integration_note, retained);
`SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED` (retained_pending_chain) as the
banking precedent. `MINIMAL_AXIOMS_2026-06-05` + `realized_state_primitive` used
to establish the wall. Exercise-skill: **no** (the wall shrank; it does not need
a fresh exercise run beyond the existing N1≥5 + N7 readiness).

### 2.2 P-COMP — opposite-chirality RH completion (outcome: confirms_wall_sharper, cracked=no)

**Attempted from A_min + primitives.** Three fresh routes plus arithmetic-core
re-derivation:

- **Route 1 (template existence from Record/Cl(3) native matter):** recomputed
  `CL3_SM_EMBEDDING_THEOREM` in-tree (numpy) — the Cl(3) taste carrier
  V = (C²)^⊗3 (dim 8) splits into ONLY the LH 6+2 surface {+1/3 ×6, −1 ×2};
  single chirality, no opposite-chirality SU(2)-singlet slot is native.
  **WALLED:** `CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05` establishes Record
  is a CONSUMER of chirality, not a source (cannot produce the carrier grading);
  the RH completion must be adjoined. Residual relocates to MINIMAL_AXIOMS
  withholding of the second-chirality matter sector.
- **Route 2 (minimal-axioms NO-GO, steelman-then-attack):** the steelman
  "consistency forces the template" is DEFEATED on three legs in sympy —
  (a) a vectorlike/mirror completion is anomaly-free with NO chiral template;
  (b) a non-neutral chiral model (0, 2a, −2a, −4a) cancels all the same
  anomalies; (c) the 2-RH-triplet slot count is a template INPUT (the carrier
  supplies 0; one triplet leaves an SU(3)³ residual of 1). **Result: a
  conditional no-go (steelman-defeat), NOT a hard impossibility proof** — there
  is no positive supplier and no closed impossibility theorem.
- **Route 3 (derive n=0 from neutrality / Record-trace):** total-hypercharge
  neutrality = the grav anomaly already imposed → reduces to the B1 family, n
  free (does NOT pin n). RH-singlet-block neutrality DOES force n=0 algebraically
  BUT fails the `realized_state_primitive` counterfactual test on the
  anomaly-equivalent model (0, 2a, −2a, −4a) (block sum −4a ≠ 0) ⇒ it is
  registered selection data, not a derivation. **WALLED:** n=0 stays an admitted
  branch convention (matches retained `ONE_GENERATION_ANOMALY_SINGLET` neutral
  branch).
- **Arithmetic core (independent re-derivation):** anomaly cancellation forces
  {x,y,z,n} = {4a, −2a, −6a, 0} up to x↔y swap; verified at a ∈ {1/3, 2/5, 7/4,
  −1/2}; a=1/3 reproduces keystone B3 (4/3, −2/3, −2, 0). The (0,2a,−2a,−4a)
  counterexample re-derived ⇒ n=0 is load-bearing; matter content not
  anomaly-unique; absolute scale is convention.

**Runner:** `scripts/frontier_abj_pcomp_block01_template_existence_2026_06_20.py`
— **TOTAL: PASS=49 FAIL=0** (cache
`logs/runner-cache/frontier_abj_pcomp_block01_template_existence_2026_06_20.txt`).

**Named wall:** the physical EXISTENCE/MINIMALITY of the opposite-chirality
SU(2)-singlet template {u_R,d_R,e_R,n_R} + the neutral singlet (n=0) from
framework-native structure. The same wall hits all three fresh routes: A_min
(Lattice + Quantum + Record) withholds the second-chirality matter sector /
particle content / species. Root supplier fact: Record is a consumer of
chirality, not a source (`CHIRALITY_RECORD_TYPING_INTERFACE`). Plus n=0 is
load-bearing (counterexample (0,2a,−2a,−4a)) and stays an admitted convention;
plus **P-COMP is circular-on-parent**.

**Retained authority (arithmetic core, deps-all-retained):**
`one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10`
(retained_bounded — ALREADY banks the RH-Y closed form (4/3,−2/3,−2,0) as a
conditional bounded_theorem); `lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10`
(retained_bounded); `cl3_color_automorphism_theorem` (retained_bounded);
`cl3_complexification_split_narrow_theorem_note_2026-05-10` (retained). Wall
corroboration: `CHIRALITY_RECORD_TYPING_INTERFACE_2026-06-05` (meta),
`RH_COMPLETION_COLOR_ANTI_FUNDAMENTAL` (unaudited). **CAVEAT: only the
ARITHMETIC banks.** The existence-side suppliers
(`one_generation_matter_closure`, `rh_completion_color_anti`,
`su3_anomaly_forced_3bar`) are ALL unaudited and `su3_dabc_symmetric` is
audited_failed — the template/existence wall CANNOT be banked and P-COMP stays
circular-on-parent. **Exercise-skill: YES** (genuinely new hard existence wall:
no positive supplier, no closed impossibility theorem).

### 2.3 P-REC — staggered ε → spacetime γ_5 (outcome: confirms_wall_sharper, cracked=no)

**Attempted from A_min + primitives.** Three fresh routes:

- **R4 (attack R4 directly — free taste reconstruction):** built the blocked
  free staggered carrier α_μ (Cl₄) + the free staggered Dirac op
  D_red(m,p) = m·I₁₆ + i Σ α_μ sin(p_μ a)/a per the retained LORENTZ_BOOST SO(4)
  note; tested chirality and built explicit taste reconstruction.
  **SUCCEEDED as a free-theory theorem:** {Γ₅^spin, D_red(m=0,p)} = 0 exactly
  (residual 0.0); explicit unitary W: α_μ → γ_μ ⊗ 1_taste (residual 1.9e-15);
  W Γ₅^spin W† = γ_5^Dirac ⊗ 1_taste (residual 2.4e-15). This CLOSES the free
  kinematic content. BUT the reconstruction yields a full M₄(C) taste commutant
  of EXACT symmetries of D_red(m,p) for all p (residual 1.6e-15), so single-taste
  selection is NOT forced; two distinct orthogonal rank-4 single-taste projectors
  are both invariant ⇒ single-taste chirality is selector-dependent = registered
  data. R4 does NOT close the physical identification.
- **R2 (Cl(3)→Cl(3,1) 4th generator + single-taste selector):** the per-site
  Cl(3) constraint is full rank ⇒ only M=0 anticommutes with all 3 Paulis (root
  NO_PER_SITE_CHIRALITY reconfirmed, residual 0.0); adjoining e₄ (ε=−1) gives a
  Cl(3,1) volume element anticommuting with the 3 spatial generators (residual
  0.0) ⇒ a finite γ_5 exists ALGEBRAICALLY. **WALLED:** the ε=+1 branch
  (Cl(4,0) ≅ M₂(H)) is a distinct extension, so the Lorentzian sign-ε is
  admitted/delegated not derived; identification still needs the same unforced
  single-taste selector. R2 reduces to the R4 wall.
- **R3a (Adams taste-singlet staggered index):** functional-calculus-correct
  membership test confirms Γ₅^spin ∈ {α}'' (residual 0.0) but ε ∉ {α}''
  (residual 4.0) ⇒ ε cannot be the index grading; naive Tr[Γ₅^spin]=0 on the
  even 2⁴ carrier (residual 0.0, square-block no-go content); a nonzero
  taste-singlet index requires an imposed χ≠0 / Q≠0 background (index 2 given
  imbalanced modes) which the free framework on the even torus does not supply.
  **RE-TARGETS** to the χ≠0 background open ray — the SAME ray as P-ABJ.

**Runner:** `scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py` —
**TOTAL: PASS=43 FAIL=0** (cache
`logs/runner-cache/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.txt`).

**Named wall:** ONE sharpened object — the **gauged/interacting single-taste
SELECTOR**. The free taste reconstruction has a full M₄(C) taste commutant of
EXACT symmetries of D_red(m,p) for all p, so NO single taste is preferred — two
distinct orthogonal rank-4 single-taste projectors are equally invariant.
Selecting one is a SELECTION, which under the `realized_state_primitive`
counterfactual clause is registered data, not a derivation. The selector
(requiring interacting/gauged dynamics + taste restoration + OS/continuum
reconstruction) is not supplied by A_min nor by any of the four approved
primitives. Secondary: the Lorentzian sign-ε (ε=−1, Cl(3,1)) is admitted via
CL3_TO_CL31's own scope; the χ≠0/Q≠0 background is not produced by the free
framework on the even torus.

**Retained authority:** `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02`
(retained_no_go; root M₂(C) wall, recomputed in-tree);
`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29`
(bounded_theorem PASS=54; supplies α_μ + D_red(p));
`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27` (positive_theorem;
4th-generator sign-ε branch); `CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10`
(EVEN/B5); `STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07` (CHI
carrier — **audited_conditional, kept CONTEXT-ONLY; α_μ recomputed in-tree**);
`ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30` (cited for R3a).
**Exercise-skill: YES** (new hard wall at the interacting-selection step).

### 2.4 P-ABJ — external Adler–Bell–Jackiw premise (outcome: confirms_wall_sharper, cracked=no)

**Attacked the internal-route wall's open escape rays on the A_min-internal substrate.**

- **R-A (χ≠0 / Q≠0 background on the A_min closed hypercubic Z⁴):** enumerated
  all {2,3,4,5}⁴ tori. **NEW sharper fact:** a hypercubic torus ε-imbalances IFF
  total site count is odd IFF EVERY edge length is odd (16 imbalanced cases, all
  all-odd). When all edges are odd, every direction has an odd cycle ⇒ {ε,D}=0
  broken in every direction (verified (3,3,3,3): N₊=41, N₋=40 imbalanced but
  max|εDε + D| = 1.000). The only imbalanced closed hypercubic complex A_min
  supplies DESTROYS the chirality grading. **FAILED to escape (wall sharpened).**
- **R-B (taste-singlet / Adams / overlap-GW index):** built the overlap index
  (1/2)Tr[ε·sign(K)] with K=εD Hermitian on (4,2,2,2) and (4,4,4,4); index=0 on
  flat AND under nonzero-flux U(1); verified the ε-gap H(m)²=K²+m²I exactly
  (m ∈ {0.37, 1.0}) pinning spectral flow to 0. Overlap/GW does NOT escape — the
  obstruction is the ε-gap, not the absence of GW. **FAILED to escape.**
- **R-C (non-abelian cohomology / topological charge Q):** the closed A_min torus
  with single-valued links has total winding Q=0 (max|Q_plane| < 1.4e-15);
  nonzero Q (Q_tx = −16) appears ONLY when a boundary twist/transition function
  is injected = external topological datum. **DECISIVE:** even with injected
  Q≠0, A_t=0 on the balanced substrate (max|A_t| < 1.2e-14) — the square-block
  wall survives nonzero gauge topological charge. **FAILED to escape.**
- **Control (OFF A_min substrate):** an open 3×3 complex IS imbalanced (N₊=5,
  N₋=4), KEEPS {ε,D}=0 (rectangular B), and yields NONZERO index
  A_∞ = N₊−N₋ = 1 — confirms the escape mechanism is real but requires a
  boundary A_min does not supply. **SUCCEEDED as control.**
- **Part 0 source-discipline:** recomputed the retained square-block no-go in-tree
  on all four governed backgrounds (Z4×Z2³ and Z4⁴, random + flux U(1)):
  balanced, εDε=−D, max|A_t| < 1.2e-14 (reproduced retained no-go without citing
  keystone blind).

**Runner:** `scripts/frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.py`
— **TOTAL: PASS=34 FAIL=0** (cache
`logs/runner-cache/frontier_abj_internal_chi_nonzero_index_escape_2026_06_20.txt`
+ `.json`).

**Named wall:** the chirality grading {ε,D}=0 GAPS the A_min substrate. Sharper:
on A_min's closed hypercubic Z⁴ (Lattice cubic adjacency + `kinetic_isotropy_primitive`
time edge), ε-sublattice imbalance (χ≠0, the only thing that defeats the
square-block A_t=0) occurs IFF every edge length is odd, which is exactly when
the ε grading is non-bipartite/destroyed in every direction. Hence χ≠0 and
intact chirality are MUTUALLY EXCLUSIVE on A_min. Every nonzero-index closure
condition (imbalanced + intact grading; open boundary/non-cubic cell; injected
gauge topological charge on an imbalanced complex) requires structure A_min does
not supply. The external ABJ implication (B2) is a separate, irreducibly-external
admission.

**Retained authority:** `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30`
(retained_no_go, PASS=45 reproduced); `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28`
(retained_bounded, PASS=36); `ABJ_ANOMALY_FRAMEWORK_INTERNAL_U1_JACOBIAN_NARROW_NOTE_2026-05-27`
(PASS=19). Primitives loaded: `kinetic_isotropy_primitive` (time edge →
hypercubic Z⁴), `scale_reference_primitive`, `realized_state_primitive`,
`minimal_axioms`. Adler 1969 / Bell–Jackiw 1969 = external authority for the
premise STAYING external. **Exercise-skill: YES** (the N7 steelman "a
curved/non-hypercubic framework complex witnesses a nonzero index" needs an
exercise run before the P-ABJ-internal wall is fenced; the P2 control is the
honest off-substrate non-vacuity witness).

## 3. Bankable arithmetic cores — the non-no-go win

The highest-value Block-01 outcome (outranking any no_go) is that **three ABJ
arithmetic cores are deps-all-retained, keystone-decoupled, conditional bounded
theorems the audit lane can retain NOW**, mirroring
`SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED` (retained_pending_chain). All
three recomputed exact in-tree by the bankability runner
(`scripts/frontier_abj_arithmetic_cores_bankability_2026_06_20.py`,
**TOTAL: PASS=55 FAIL=0**, cache
`logs/runner-cache/frontier_abj_arithmetic_cores_bankability_2026_06_20.txt`),
and each per-edge runner above independently re-derives its own core. The
keystone and parent were both confirmed `unaudited` by read-only ledger parse,
so NO core routes through them.

### 3.1 P-HY core — scale-free LH anomaly tuple

**Statement (conditional bounded theorem):** on the scale-free LH abelian
surface Y_a = a(P_sym − 3P_anti), the anomaly traces are
`Tr[Y]=0, Tr[Y³]=−48a³, Tr[SU(3)²Y]=a, Tr[SU(2)²Y]=0, Tr[SU(3)³]_LH=2`,
specializing at a=1/3 to `{0, −16/9, 1/3, 0, 2}`; nonzero forced by the ratio
1:(−3) alone, convention-independent in a.

**Dep set (all retained-grade):** `graph_first_su3_integration_note` (retained);
`native_gauge_closure_note` (retained);
`native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23`
(decoration_under_graph_first); `lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02`
(decoration_under_graph_first).

**Banking guard:** use the ratio note + graph_first parent ONLY. Keep
`hypercharge_identification_note` / α=1/3 OUT of the load-bearing set — the
B2 homogeneity lemma proves α is pure convention for the anomaly test, so the
admission stays NAMED, not load-bearing.

### 3.2 P-COMP core — scale-free completion classification

**Statement (conditional bounded theorem, premises {template existence, P-HY,
n=0 branch} kept explicit):** GIVEN the opposite-chirality SU(2)-singlet template
+ the LH surface, anomaly cancellation FORCES {x,y,z,n} = {4a, −2a, −6a, 0}
unique up to triplet swap; a=1/3 ⇒ (4/3, −2/3, −2, 0). Non-vacuity lemmas:
B1 the (0,2a,−2a,−4a) counterexample proves n=0 load-bearing; B2 vectorlike
(t,−t) pairs preserve every anomaly zero (content not anomaly-unique); B3 global
rescaling preserves every anomaly zero (absolute scale is convention).

**Dep set (all retained-grade):**
`one_generation_anomaly_singlet_completion_narrow_theorem_note_2026-05-10`
(retained_bounded — already banks the RH-Y closed form);
`lh_traceless_eigenvalue_ratio_narrow_theorem_note_2026-05-10` (retained_bounded);
`cl3_color_automorphism_theorem` (retained_bounded);
`cl3_complexification_split_narrow_theorem_note_2026-05-10` (retained).

**Banking guard:** ONLY the arithmetic banks. The existence side (template) is
NOT bankable (suppliers unaudited; `su3_dabc_symmetric` audited_failed). Carry
the circular-on-parent flag verbatim.

### 3.3 P-REC core — spin/taste Clifford reconstruction (carrier-conditional)

**Statement (conditional bounded theorem, conditional on the even 2⁴ carrier):**
on the blocked free staggered 2⁴ carrier — (a) the α_μ form Cl₄ (residual 0.0),
spin algebra dim 16, taste commutant dim 16; (b) Γ₅^spin = α₀α₁α₂α₃ is a
taste-singlet spacetime γ_5 (commutes with the full taste commutant, 1.2e-15);
(c) the explicit unitary reconstruction W: α_μ → γ_μ ⊗ 1_taste exists (residual
1.9e-15) with Γ₅^spin → γ_5^Dirac ⊗ 1_taste (residual 2.4e-15); (d)
{Γ₅^spin, D_red(m=0,p)} = 0 exactly ⇒ Γ₅^spin is the chirality of the free
massless staggered Dirac op. This is STRONGER than the prior partial closure
(adds the explicit W + free-massless chirality, not merely existence of Γ₅^spin).

**Dep set (all retained-grade):** `no_per_site_chirality_theorem_note_2026-05-02`
(retained_no_go); `clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10`
(retained); `lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29`
(retained_bounded).

**Banking WRINKLE (load-bearing for packaging):** the staggered Kawamoto–Smit
carrier (`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`) is
**audited_conditional / chain_closes=False — NOT retained-grade**. If the P-REC
bank cites it as load-bearing it FAILS deps-all-retained. It must stay
CONTEXT-ONLY with α_μ recomputed in-tree (mirroring the SM_ANOMALY_CLOSURE
reprove-and-cite pattern). Keep the carrier-conditional (even 2⁴, odd-L caveat)
and do NOT import the single-taste identification.

### 3.4 P-ABJ — NOT bankable as an edge bounded theorem

P-ABJ's load-bearing content is the EXTERNAL anomaly-to-inconsistency implication
(B2), which has no in-tree deps-all-retained arithmetic core — the implication is
itself the external admission. The only bankable arithmetic for P-ABJ is the
trace INPUTS it consumes (Tr[Y³]=−16/9 etc.), already covered by the P-HY core.
The bankable artifact specific to P-ABJ is the internal-route **no-go** (sharpens
the retained `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO` without routing through the
keystone) — see NO_GO_LEDGER.

## 4. Honest status summary

| Edge | Crack? | Core bankable? | Wall | Exercise-skill run? |
|---|---|---|---|---|
| P-HY | no | YES (deps-all-retained) | "is-gauged" predicate only (narrower) | no |
| P-COMP | no | YES (arithmetic only; existence not bankable) | opposite-chirality template existence/minimality; circular-on-parent | **yes** |
| P-REC | no | YES (carrier-conditional; KS carrier context-only) | gauged/interacting single-taste selector | **yes** |
| P-ABJ | no | N/A (external admission; only consumed traces bank) | χ≠0 ⇔ all-odd ⇔ chirality destroyed exclusivity + external implication | **yes** |

**No crack on any edge.** Three edges (P-COMP, P-REC, P-ABJ) hit genuinely new
hard walls warranting an exercise-skill run (per the user standing directive: do
not ship a bare no_go). P-HY's wall SHRANK and does not need a fresh exercise run.

**N1/N7 readiness (for the later consolidated note):** P-HY has 5 attacked routes
+ an attacked N7 steelman; P-COMP adds 3 fresh genuine routes + the N7 steelman;
P-REC has 4 prior + 3 fresh routes; P-ABJ adds 3 fresh escape rays (R-A/R-B/R-C)
to the prior deeply-pruned route, with the N7 steelman still needing an exercise
run.

## 5. Stale-map / in-tree ledger corrections recorded

- **α-bridge status:** `hypercharge_alpha_third_normalization_bridge_bounded_note_2026-05-25`
  and `hypercharge_identification_note` are BOTH retained_bounded /
  chain_closes=True on this branch base — the GROUNDING_MAP "α still conditional /
  chain_closes=FALSE" framing is **stale**. The bridge's own caveat is carried
  verbatim: it "does not eliminate the admission, [it] formally exposes P1–P4."
- **P-REC KS-carrier wrinkle:** `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`
  is audited_conditional (not retained) — load-bearing for how block02 must
  package the P-REC bank (context-only).
- **Dangling cross-ref:** `ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17`
  is absent from this branch / main (flag for the consolidation note).

## 6. Firewall / forbidden-surface attestation

This note + the five runners + their caches + the branch-local block01 sections,
certificate, and NO_GO_LEDGER are the ONLY new artifacts. **No file under
`docs/audit/`, `docs/publication/`, AUDIT_LEDGER/QUEUE, MISSING_DERIVATION_PROMPTS
was edited.** `docs/audit/data/` was parsed READ-ONLY (python) for
effective_status/chain_closes. No row/effective status set; no audit verdict
asserted. Independent audit required before any effective-retained movement.

---
*Block 01 of the anomaly_forces_time ABJ bridge attack. Block 02 plan: bank the
three cores as standalone deps-all-retained bounded theorems + write the unified
hybrid obstruction note. See CLAIM_STATUS_CERTIFICATE_block01.md and
NO_GO_LEDGER.md (anomaly pack).*
