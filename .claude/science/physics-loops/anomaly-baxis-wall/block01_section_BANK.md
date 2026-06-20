# block01 Section BANK — ABJ arithmetic cores: bankability verification

**Edge:** EDGE-INDEPENDENT — bankability of the three ABJ arithmetic cores
(P-HY anomaly core, P-COMP completion classification, P-REC spin/taste Clifford
core). Seeds block02's lead deliverable (Decision A: bank the cores).

**Branch:** `physics-loop/anomaly-abj-bridge-block01-20260620`
**Runner:** `scripts/frontier_abj_arithmetic_cores_bankability_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_arithmetic_cores_bankability_2026_06_20.txt`
**Result:** `TOTAL: PASS=55 FAIL=0` (exact sympy/Fraction + small-matrix numpy)
**Precedent:** `SM_ANOMALY_CLOSURE_RETAINED_ANCHORS_DECOUPLED_BOUNDED_THEOREM_NOTE_2026-06-08`
(deps-all-retained, audit-ready; ledger `effective_status=retained_pending_chain`,
`chain_closes=True`).

## Thesis (confirmed)

Each of the three arithmetic cores CAN be packaged exactly the way
`SM_ANOMALY_CLOSURE` was: (a) arithmetic recomputed in-tree, exact and
convention-independent; (b) load-bearing dependency set is retained-grade; (c)
does NOT route through the unaudited keystone
`anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26`
or the unaudited parent `anomaly_forces_time_theorem` (both verified `unaudited`
in the ledger). **All three cores are BANKABLE NOW** as conditional bounded
theorems, with the physical identifications left as STATED admitted premises
(not derived) — mirroring `SM_ANOMALY_CLOSURE`'s premise (P).

## Retained-grade vocabulary (from the ledger, read-only)

`effective_status` values that count as deps-all-retained ("ready"):
`retained`, `retained_bounded`, `retained_no_go`, `retained_pending_chain`, and
`decoration_under_<retained-parent>` (decorations roll up under a retained
parent). NOT retained-grade: `audited_conditional`, `unaudited`, `open_gate`,
`meta`. The keystone bridge and `anomaly_forces_time_theorem` are both
`unaudited` (chain_closes=None) — so routing any core through them is forbidden.

## The three cores — recomputed in-tree

### CORE 1 — P-HY scale-free native abelian anomaly core
`Y_a = a·P_6 − 3a·P_2` on the LH abelian surface ({+1/3×6, −1×2} at a=1/3):
- `Tr[Y]=0`, `Tr[Y^3]=−48 a^3` (nonzero ∀ a≠0), `Tr[SU(3)^2 Y]=a` (nonzero),
  `Tr[SU(2)^2 Y]=0`, `Tr[SU(3)^3]_LH=2`. At a=1/3 → (−16/9, 1/3, 2).
- Convention-independent: nonzero anomaly forced by the native ratio 1:−3 alone;
  a=1/3, e-charge sign, SM names NOT load-bearing (verified on a-grid).

### CORE 2 — P-COMP scale-free singlet-completion classification
On Q_L:(2,3)_a, L_L:(2,1)_{−3a}, GIVEN RH template {u_R,d_R,e_R,n_R}:
- anomaly cancellation FORCES {x,y,z,n}={4a,−2a,−6a,0}, unique up to triplet swap
  (solver returns exactly {x,y}={4a,−2a}, z=−6a).
- Non-vacuity lemmas reproduced verbatim: **B1** counterexample (0,2a,−2a,−4a)
  cancels the same anomalies ⇒ n=0 (neutral singlet) is LOAD-BEARING; **B2**
  vectorlike (t,−t) preserves all zeros ⇒ content not anomaly-unique; **B3**
  global Y-rescaling preserves zeros ⇒ absolute scale is convention.

### CORE 3 — P-REC spin/taste Clifford core (blocked 2^4 hypercube)
α_μ (16×16) built directly from staggered phases η_μ(b)=(−1)^{Σ_{ν<μ}b_ν}:
- Hermitian involutions forming Cl_4 ({α_μ,α_ν}=2δ_{μν}I); generated spin algebra
  dim=16; taste commutant dim=16.
- `Γ5spin = α0α1α2α3` Hermitian, ²=I, anticommutes all α_μ, rank-8/8 chirality
  projectors, commutes with taste commutant ⇒ genuine taste-singlet spacetime γ5.
- staggered ε(b)=(−1)^{Σb} anticommutes α_μ BUT is NOT ±Γ5spin (max|ε∓Γ5|=1.0),
  NOT in Cl_4 (lstsq residual=4.0), does NOT commute with taste commutant
  (commutator=0.359) ⇒ ε is taste-dressed. (epsilon≠gamma5 sharpened.)

## Dependency-set retained-grade audit (read-only ledger parse)

| core | load-bearing retained-anchor deps | every dep status | routes keystone? | BANKABLE |
|---|---|---|---|---|
| **P-HY** | graph_first_su3_integration_note (retained); native_gauge_closure_note (retained); native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23 (decoration→graph_first); lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02 (decoration→graph_first) | all retained-grade | NO | **YES** |
| **P-COMP** | graph_first_su3_integration_note (retained); native_gauge_closure_note (retained); native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23 (decoration→graph_first) | all retained-grade | NO | **YES** |
| **P-REC** | no_per_site_chirality_theorem_note_2026-05-02 (retained_no_go); clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10 (retained); lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29 (retained_bounded) | all retained-grade | NO | **YES** |

Axiom baseline `{Lattice,Quantum,Record}` (MINIMAL_AXIOMS, ledger `meta`) enters
as the axiom node (chain-satisfies; listed `(Axiom)` separately, as in
SM_ANOMALY_CLOSURE), NOT as a retained dep.

## Admitted premises (STATED, not ledger deps — mirror SM_ANOMALY_CLOSURE (P))

- **P-HY:** the native nonzero abelian direction IS the gauged anomaly-relevant
  U(1) entering the test (NARROW gauged-direction role, not full SM U(1)_Y). The
  α=1/3 absolute normalization is a convention (B3-style rescaling invariance),
  NOT load-bearing for the nonzero-anomaly core.
- **P-COMP:** existence of the opposite-chirality SU(2)-singlet RH template incl.
  the neutral singlet n_R (n=0). Stated, not imported. Still circular on its own
  parent — banking the core does NOT resolve the circularity (keep as open flag).
- **P-REC:** the interacting/gauged single-taste reconstruction map (R4) from the
  blocked staggered carrier to an irreducible Dirac factor whose chirality is
  Γ5spin. Open (the soft-wall escape).

External comparator facts (named, reproven-in-runner where arithmetical): Adler
1969; Bell-Jackiw 1969; Dynkin T(2)=T(3)=1/2; SU(3) cubic A(3)=+1.

## WRINKLE (independent finding — load-bearing for block02 banking)

The P-REC staggered carrier `staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`
is **`audited_conditional`** (chain_closes=False), i.e. NOT retained-grade. If the
P-REC bank were to cite the staggered carrier as a load-bearing markdown dep, it
would FAIL deps-all-retained. The bankable shape AVOIDS this by recomputing the
α_μ in-tree from the staggered phases (done in CORE 3, all PASS), so the carrier
enters only as a recomputed construction surface — exactly the
`SM_ANOMALY_CLOSURE` "reprove-and-cite" move (reprove the arithmetic, cite prior
packaging as context-only, not as a load-bearing dep). **Block02 must keep the
staggered carrier context-only in the P-REC bank.**

Two further banking-overreach guards carried from the SM_ANOMALY_CLOSURE pattern:
(1) the cores are CONDITIONAL on the named admitted premises — keep them named,
do not silently re-import the physical identifications as load-bearing; (2) the
`hypercharge_identification_note` is `retained_bounded` but `chain_closes=True`
only via the admitted α=1/3 bridge — the P-HY bank should NOT lean on it for the
scale-free core (the core needs only the ratio note + graph-first parent), keeping
the α=1/3 admission out of the load-bearing set.

## Exact dep set for each bank (block02 hand-off)

- **P-HY anomaly core bank:** {graph_first_su3_integration_note,
  native_gauge_closure_note,
  native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23,
  lh_doublet_traceless_abelian_eigenvalue_ratio_narrow_theorem_note_2026-05-02}
  + Axiom(MINIMAL_AXIOMS) + admitted(P-HY gauged-direction) + external(Adler/BJ,
  Dynkin). Decoupled from keystone. **Bankable now.**
- **P-COMP completion bank:** {graph_first_su3_integration_note,
  native_gauge_closure_note,
  native_gauge_left_handed_abelian_surface_bounded_note_2026-05-23}
  + Axiom + admitted(RH SU(2)-singlet template incl n_R) + external. Decoupled.
  **Bankable now** (carry the circular-on-parent flag).
- **P-REC spin/taste core bank:** {no_per_site_chirality_theorem_note_2026-05-02,
  clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10,
  lorentz_boost_free_staggered_fermion_2point_so4_narrow_theorem_note_2026-05-29}
  + Axiom + admitted(R4 reconstruction map) + external; staggered carrier
  CONTEXT-ONLY (audited_conditional, recompute in-tree). Decoupled. **Bankable now.**

## Firewall / source discipline

No edits to docs/audit/data (`git status --porcelain docs/audit/data/` clean),
AUDIT_LEDGER/QUEUE, MISSING_DERIVATION_PROMPTS, or docs/publication. Ledger parsed
read-only. No new axiom/primitive. The arithmetic was recomputed independently of
the in-flight sibling-branch runners (not trusted, re-derived). This section banks
ARITHMETIC only; the four physical identifications stay walled and the no_go on
them is HELD pending N1≥5 + N7 per edge (block01 fresh attempts, separate edges).
