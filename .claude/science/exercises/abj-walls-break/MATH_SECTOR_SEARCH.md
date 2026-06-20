# Exercise Four — Mathematics Sector Search (ABJ identification walls)

**Skill:** `docs/ai_methodology/skills/exercise/SKILL.md` (Exercise Four)
**Slug:** abj-walls-break • **Date:** 2026-06-20
**Slice author posture:** max-reasoning physics reviewer; BREAK the walls, find
NEW formal lenses. Treat framework premises as challengeable. No new
axioms/primitives, no audit verdicts, READ-ONLY on `docs/audit/data/`.

## Framework Refresher Read (surfaces actually read this slice)

- `docs/MINIMAL_AXIOMS_2026-06-05.md` (Lattice = `Z^3` cubic adjacency;
  Quantum = one qubit `M_2(C) ≅ Cl(3,0)`; Record = durable K/CPT-orbit readout,
  finite additive — supplies **K/CPT conjugation** but no gauge group / species /
  occupancy / single-taste selector).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` + the four approved
  primitive source-note summaries via `docs/audit/data/axiom_premise_nodes.json`
  (`minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`,
  `realized_state_primitive`) and `docs/audit/data/tier_a_admissions.json`
  (only two Tier-A targets: AC_phi_lambda, theta — neither is an ABJ edge).
- `docs/ai_methodology/skills/review-loop/SKILL.md` (axiom/primitive/Tier-A
  distinction; no-go discipline gate; realized-state counterfactual clause).
- `docs/repo/CONTROLLED_VOCABULARY.md` (claim-strength + audit enums; load-bearing
  step classes (A)-(G)).
- Wall + history surfaces: `.../abj-walls-break/EXERCISE.md`;
  `docs/ANOMALY_FORCES_TIME_ABJ_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`;
  `.claude/science/physics-loops/anomaly-baxis-wall/GROUNDING_MAP.json` (full:
  branchMaps, noteMaps, blueprint incl. `routes_already_tested`,
  `routes_still_to_attempt`, `duplication_warnings`).
- Bounding theorems read in full or load-bearing part:
  `NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02`,
  `CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`,
  `ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30`,
  `ABJ_RESIDUAL_GW_NOT_NECESSARY_NARROW_THEOREM_NOTE_2026-05-28`,
  `INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08`,
  `Z_N_SPECTRAL_ASYMMETRY_PHYSICAL_IDENTIFICATION_NOTE_2026-05-31`,
  `HODGE_STAR_MIDDLE_FORM_DECOMPOSITION_FORCES_D_FOUR_NARROW_THEOREM_NOTE_2026-05-26`,
  `KOIDE_Y_BAE_TOPOLOGICAL_INDEX_KTHEORY_NOTE_2026-05-10`,
  `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`,
  `LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29`.

## What I am NOT allowed to re-propose (already pruned/absorbed — verified)

These are in `routes_already_tested` / `routes_still_to_attempt` /
`duplication_warnings`, or are the *demolition-only* citations of the GW note.
I treat them as **walls to route around**, not vectors:

- **Naive integer K^0 index / staggered ε-index** on the closed even/equal-
  sublattice hypercubic `Z^4` torus → identically 0 (square-block no-go, PASS=45).
- **η-invariant / K^1 spectral flow** of the massive staggered operator on the
  **flat/free** substrate → 0 by the ε-gap `H(m)^2 = K^2 + m^2 I` (GW-not-necessary
  G1). The Fukaya K-theoretic-APS and "no GW needed" papers are *cited, not
  imported*, and already pruned on the flat substrate.
- **Kähler-Dirac anomaly = Euler characteristic χ** is already NAMED (Catterall,
  cited demolition-only): the open ray is "exhibit χ≠0 / Q≠0", and block01 R-A
  already enumerated hypercubic **tori** ({2,3,4,5}^4) showing ε-imbalance ⇔
  all-odd ⇔ chirality destroyed.
- **Finite-group equivariant point K-theory** `K_{C3}(pt)=R(C3)` → only rank/
  character data (KOIDE_Y_BAE topological probe).
- **ε ↔ Γ_5^spin shortcut** and **factored Γ_χ = ε⊗B ⇒ B=0** (gamma5-boundary
  NG-1/NG-2, PASS=52); ε is taste-dressed (spintaste-core, residual 4.0).
- **Cl(3)→Cl(3,1) extension alone** (insufficient: supplies γ_5 only after a
  supplied 4th generator, no reconstruction map).
- **Connes-Lott γ_CL ≡ C3 character grading** hybrid (KOIDE Z3-equivariant no-go).
- **γ_μ ↔ lattice-edge index pairing & first-order kinetic order** are NOT forced
  (INDEX_PAIRING_NOT_FORCED) — I must not silently assume them.

The genuinely-new entries below each name **the object that changes**, **the
invariant/theorem-type that bites**, and **the first concrete artifact** — and
each is differentiated in writing from the pruned item it is nearest to.

---

## Sector table (the new lenses)

### S1 — Real/quaternionic Clifford-module theory (Cartan–Bott KO-degree) → P-REC

| Field | Entry |
|---|---|
| **Sector** | Clifford algebras & spin representation theory; KO-theory / division-algebra (Frobenius) classification of irreducible Clifford modules. |
| **Reframe** | The single-taste selector is **not** a choice inside the complex `M_4(C)` taste commutant (where block01 correctly found two equally-invariant rank-4 projectors). It is the choice of a **real structure** — a Cl(3,1)-real-module (Majorana) reduction. The physical Dirac factor of the framework is `Cl(3,1) ≅ M_4(R)` (CL3_TO_CL31 (S3)), whose *irreducible REAL module* is `R^4`, dim 4, **with real commutant `R` (a division ring), not `M_4(C)`**. The taste `M_4(C)` ambiguity is an artifact of complexifying before reducing to the real form. |
| **Candidate theorem/tool** | Cartan–Bott: `Cl(3,1)≅M_4(R)` is of **real type** (Schur commutant `R`), whereas the free complex staggered carrier on the even `2^4` block has commutant `M_4(C)`. Wedderburn/Schur: an irreducible *real* module of a real central-simple algebra has commutant a division algebra (`R`,`C`, or `H`); for `M_4(R)` it is `R`. So *if* the reconstruction lands in the real (Majorana) form delegated by Record's K/CPT conjugation, the taste commutant collapses `M_4(C) → R` and the single-taste selector becomes **rigid** (Schur's lemma), not free. |
| **Minimal toy** | `Cl(3,1)=M_4(R)` acting on `R^4`; compute the *real* commutant (centralizer in `M_4(R)` of the algebra) = `R·I` (1-dim). Contrast with the complexified `M_4(C)` on `C^4` (taste) whose centralizer of a single γ-factor is `M_4(C)` (16-dim) — the source of the block01 freedom. Then impose the Record K/CPT real structure `J` (an antilinear involution with `J^2=±1`) and check that the surviving J-real invariant projectors number exactly one rank-4 family. |
| **Attacks which wall** | **P-REC** (the highest-value soft wall). Converts "single-taste selection is registered data (M_4(C) is too big)" into "single-taste is forced once the *real* form is taken — and the real form is exactly what Record's K/CPT conjugation supplies." This is an A_min-internal supplier candidate (Record axiom literally carries `K`/CPT), not a new axiom. |
| **Falsifier** | If the real commutant of the *Majorana-reduced* reconstructed Dirac factor is still > `R` (i.e. the K/CPT J does not cut `M_4(C)` down to a 1-dim real centralizer), or if more than one J-real rank-4 projector survives, the reframe fails and P-REC's wall stands. Also fails if the staggered reconstruction is shown to be intrinsically *complex* type (no compatible J exists on the `2^4` carrier). |
| **First artifact** | numpy/sympy runner: build `Cl(3,1)` as `M_4(R)`; build the even-`2^4` staggered α_μ (reuse the LORENTZ_BOOST SO(4) surface convention) and its `M_4(C)` taste commutant; construct the antilinear `J` from the framework `K`/CPT (real anti-Hermitian `D`, CPT_EXACT `εDε=−D`); compute `dim_R Comm_J(α_μ)` and **count J-real rank-4 invariant projectors**. Decisive output = "1 J-real single-taste projector (forced)" vs ">1 (registered data, wall stands)". |

### S2 — Skolem–Noether / Brauer group (uniqueness up to inner automorphism) → P-REC reframe

| Field | Entry |
|---|---|
| **Sector** | Central simple algebras; Skolem–Noether theorem; Brauer-group triviality of `M_n(K)`. |
| **Reframe** | Move the boundary "selector vs admissible dial." Even if a *single* taste cannot be canonically named, the **reconstruction map `W: α_μ → γ_μ ⊗ 1`** between two presentations of the same central simple algebra is unique **up to an inner automorphism** (Skolem–Noether). If every physical observable the keystone consumes (the chirality `Γ_5^spin`, the anomaly trace) is **inner-automorphism-invariant**, then taste-relabelling is a *gauge redundancy*, not registered data — exactly the move that retired α=1/3 for P-HY (homogeneity lemma: provably pure convention). |
| **Candidate theorem/tool** | Skolem–Noether: any two `R`-algebra homomorphisms of a central simple algebra into `M_n` differ by conjugation; `Br(R-matrix-algebra)` trivial ⇒ all faithful irreps are conjugate. Corollary to test: `Γ_5^spin`, `Tr[ε exp(−tD†D)]`, and the chiral projectors are **class functions** (conjugation-invariant), so they do not depend on *which* taste is selected. |
| **Minimal toy** | Two distinct rank-4 single-taste projectors `P_a`, `P_b` (block01's two equally-invariant ones). Find the inner automorphism `U` with `U P_a U^† = P_b` inside the taste commutant; check `U Γ_5^spin U^† = Γ_5^spin` and `Tr` invariance. If all consumed quantities are fixed, the selector is gauge. |
| **Attacks which wall** | **P-REC** as a **reframe** (the EXERCISE's second win-shape: "a reframe that makes the identification unnecessary for the consumer"). Does not derive a selector; proves the consumer never needed one. |
| **Falsifier** | If any keystone-consumed quantity (most importantly the *sign/orientation* of `Γ_5^spin`, since chirality is the load-bearing object) is **not** invariant under the taste-inner-automorphism connecting the two projectors — i.e. taste-relabelling flips a physical chirality — then the selector is genuine registered data and the reframe fails. (This is the real risk: ABJ chirality is exactly an orientation, and orientation can be the one thing inner automorphisms move via det=−1 elements.) |
| **First artifact** | runner extending the spintaste-core: enumerate the taste commutant's unitary group action on the two single-taste projectors; verify (or refute) conjugation-invariance of `Γ_5^spin` and the anomaly trace; **explicitly test the det=−1 / orientation-flip subcase** (the falsifier). Output: "consumer-invariant ⇒ selector is gauge" or "orientation moves ⇒ wall stands." |

### S3 — Kähler–Dirac on a non-product CW/flag complex; combinatorial Euler characteristic → P-ABJ

| Field | Entry |
|---|---|
| **Sector** | Algebraic topology / combinatorial Hodge theory; Dirac–Kähler operator on simplicial/cubical complexes; Euler characteristic as the Kähler-Dirac anomaly coefficient. |
| **Reframe** | The open P-ABJ ray is "exhibit χ≠0 on a framework-internal background." Block01 R-A only enumerated **hypercubic product tori** (`L_1×…×L_4`), where χ=0 always (and ε-imbalance ⇔ all-odd ⇔ chirality destroyed). But A_min's Lattice axiom supplies a **graph** (`Z^3` with cubic adjacency), and a graph canonically generates **non-product** complexes whose χ is a genuine combinatorial invariant: the **flag/clique complex** of the adjacency graph, or a finite simplicial *triangulation* of a window. χ of a non-product complex is **not** forced to 0. The lens: Catterall's anomaly = χ, evaluated on the *intrinsic complex of the cubic graph*, not on a product torus. |
| **Candidate theorem/tool** | Kähler-Dirac / Dirac on a CW complex: index = χ (Euler characteristic), and the 't Hooft `U(1)→Z_4` anomaly coefficient = χ (Catterall, cited demolition-only in the GW note — used here only as the *target identity to test*, recomputed in-tree on a framework complex). Combinatorial χ = Σ (−1)^k (#k-cells). |
| **Minimal toy** | A finite window of the cubic `Z^3` adjacency graph; build (a) the cubical complex (χ=0 as expected, the product case), then (b) the **flag complex** of the graph (cells = cliques) and (c) a standard simplicial triangulation of the same point set. Compute χ for each. The cubic graph has triangle-free adjacency (no 2-cliques beyond edges along a cube face only if diagonals added) — so the flag complex of the *pure nearest-neighbor* graph is just the 1-skeleton: χ = V − E, generically ≠ 0 for an open window. |
| **Attacks which wall** | **P-ABJ internal route** (the one explicitly left open by BOTH no-gos: "imbalanced or curved cell complex with χ≠0"). Distinct from block01's torus enumeration: this changes the *complex*, not the *torus dimensions*. The decisive question: does A_min's adjacency graph, taken as a 1-complex / flag complex *without injecting a boundary twist*, carry χ≠0 intrinsically? |
| **Falsifier** | If every A_min-canonical complex of a **closed** (periodic, boundaryless) cubic graph has χ=0 — which is true for any closed odd/even product torus and likely for any vertex-transitive closed complex — then χ≠0 requires either a boundary (which A_min does not supply, per block01 control) or an externally-chosen non-canonical triangulation (an injected datum). That would *sharpen* the wall (χ≠0 ⇔ boundary/external), mirroring block01's all-odd result, rather than break it. |
| **First artifact** | runner: for closed periodic cubic tori AND for the flag complex / barycentric triangulation of a finite cubic graph, compute χ combinatorially and the Kähler-Dirac index; report whether any **closed, A_min-canonical** complex achieves χ≠0 **without** an injected boundary/transition function. Honest expected outcome: sharpen (closed ⇒ χ=0); a surprise χ≠0 closed case would be a genuine crack. |

### S4 — Representation-theoretic CPT closure (branching + complex-conjugate module) → P-COMP

| Field | Entry |
|---|---|
| **Sector** | Representation theory & branching rules; reality/complex-conjugate (CPT-mirror) of a representation; the K/CPT conjugation that lives **inside the Record axiom**. |
| **Reframe** | The existence-side branches all concluded "Record is a *consumer* of chirality, not a source," so the opposite-chirality RH template must be adjoined (registered data). But the Record axiom's realized outcome is the **K/CPT orbit** of the realized central sector. K/CPT is **antilinear conjugation** = exactly the operation that sends a representation ρ to its **complex conjugate ρ̄** = the opposite-chirality (RH) Weyl content. Reframe: the RH SU(2)-singlet completion is **not new matter to adjoin** — it is the **K/CPT-mirror of the LH surface that Record already orbits over**. P-COMP "existence" becomes "the Record K/CPT orbit of the LH 6+2 surface", an A_min-internal object. |
| **Candidate theorem/tool** | For a complex rep `V` of the gauge algebra, `V̄` is the CPT-conjugate; a Dirac (anomaly-free, vectorlike) completion is `V ⊕ V̄`. Branching: the LH carrier `(C^2)^{⊗3}` (Cl(3) taste) splits into the 6+2 LH surface; its conjugate gives the RH slots. The K/CPT conjugation J of Record acts on the realized central sector; its orbit is `{sector, J·sector}` = `{LH, RH-mirror}`. Test whether `J·(6+2 LH surface)` reproduces exactly `{u_R,d_R,e_R,n_R}` including the **neutral singlet n=0** (the load-bearing piece, since counterexample (0,2a,−2a,−4a) shows n=0 cannot be dropped). |
| **Minimal toy** | Take the retained Cl(3) complexification split `Cl(3,0)⊗C ≅ M_2(C)⊕M_2(C)` (the chirality pair). Apply the antilinear K/CPT J (complex conjugation composed with the Cl(3) charge-conjugation matrix) to the LH 6+2 eigenvalue surface. Check the resulting hypercharges land on `{4a,−2a,−6a,0}` and the **neutral singlet appears as the J-fixed (real) ray** (CPT-self-conjugate ⇒ Majorana-neutral ⇒ Y=0). |
| **Attacks which wall** | **P-COMP** (existence/minimality, the wall flagged "circular-on-parent" and "no native supplier"). If the RH template = Record-K/CPT-orbit of the LH surface, the *existence* is supplied by the Record axiom (no new matter sector), and **n=0** is forced as the CPT-self-conjugate (real/Majorana) fixed point rather than admitted. This is the single most direct "use the four primitives" attack: Record's K/CPT is one of the explicitly approved structures. |
| **Falsifier** | If the K/CPT conjugate of the LH 6+2 surface does **not** reproduce the SU(2)-singlet RH slots (e.g. it returns an SU(2)-doublet, i.e. a *mirror* not a *chiral* completion — exactly the vectorlike B2 counterexample), then CPT closure gives the wrong (vectorlike) completion and P-COMP's chiral template stays unsupplied. Also fails if the J-fixed ray does not coincide with the neutral n=0 slot (then n=0 stays admitted). The vectorlike-vs-chiral distinction is the live danger — CPT conjugation naively gives `V⊕V̄` (vectorlike), and the SM is chiral, so the reframe must show the *gauge* structure (SU(2) acting only on LH) breaks the J-pairing into the chiral pattern. |
| **First artifact** | runner: implement the Record K/CPT J on the retained Cl(3) chirality-pair split; act on the LH abelian surface; check (i) SU(2)-singlet vs doublet character of the image (chiral vs vectorlike falsifier), (ii) whether `{4a,−2a,−6a,0}` is reproduced, (iii) whether the J-fixed subspace is exactly the n=0 neutral singlet. Output decides: "P-COMP existence + n=0 supplied by Record K/CPT" or "K/CPT gives vectorlike/wrong-n ⇒ wall stands." |

### S5 — Cohomology of the gauge group (non-abelian anomaly as a 5-cocycle / descent) → P-ABJ

| Field | Entry |
|---|---|
| **Sector** | Cohomology of the gauge group / Lie-algebra cohomology; the non-abelian anomaly as the degree-(2n+1) primitive (`Tr F^{n+1}` descent), distinct from the perturbative trace. |
| **Reframe** | P-ABJ's external admission is "nonzero anomaly traces ⇒ no unitary QFT." The repo treats this as irreducibly external (Adler/Bell-Jackiw). But the **obstruction-theoretic content** of "anomaly ⇒ inconsistency" is a **group-cohomology statement**: a nonzero `H^{2n+1}(G)` primitive ⇒ the fermion measure is a section of a nontrivial line bundle over gauge-orbit space ⇒ no gauge-invariant partition function. Reframe the *implication* (B2) as: the framework's own gauge configuration space (cubic-graph link variables) carries this cohomology class or it does not. The arithmetic (`Tr[Y^3]`, `Tr[SU(3)^3]`) the framework already computes IS the evaluation of the degree-(2n+1) primitive on the framework reps. |
| **Candidate theorem/tool** | Lie-algebra cohomology: the non-abelian gauge anomaly = the unique (up to normalization) primitive element of `H^*(g)` in degree `2n+1` for `su(n)`, n≥3 (the `d^{abc}` symbol = the degree-5 cocycle for `su(3)`). Caveat already in tier_a context: `su3_dabc_symmetric` is **audited_failed** — so the `d^{abc}` supplier is NOT retained, which is itself a sharpening, not a blocker, since the *cohomology class* can be recomputed in-tree. |
| **Minimal toy** | Compute the `su(3)` cubic Casimir / `d^{abc}` symmetric invariant on the framework LH 6+2 surface (already known nonzero, `Tr[SU(3)^3]=2`), and exhibit it as the degree-5 Lie-algebra cocycle representative (Chevalley-Eilenberg). Then check whether the *cubic-graph link configuration space* admits this as a nontrivial class (winding of the transition functions) — connecting to the block01 R-C result that `Q=0` on closed single-valued links. |
| **Attacks which wall** | **P-ABJ internal route** — specifically the implication B2 ("anomaly ⇒ inconsistency"), the part the repo declares external. If B2 = a cohomology obstruction and the framework's link config space is shown to carry (or provably not carry) the class, then either (a) the implication becomes framework-internal (crack), or (b) it is provably trivial on A_min's closed single-valued links (sharper no-go than "external by policy"). |
| **Falsifier** | block01 R-C already found `Q=0` (winding) on closed single-valued links (max|Q|<1.4e-15); nonzero only under an injected boundary twist. So the cohomology class is very likely **trivial** on A_min's closed config space ⇒ the non-abelian-anomaly-as-obstruction is internally invisible without an external transition function. That would CONFIRM P-ABJ's externality with a cohomological reason (a sharper citable no-go), and *falsify* the crack hope. The reframe fails-as-crack but may succeed-as-sharper-no-go. |
| **First artifact** | runner: Chevalley-Eilenberg representative of the `su(3)` degree-5 cocycle recomputed in-tree (do NOT cite audited_failed `su3_dabc_symmetric`); evaluate on framework reps; then test triviality of the corresponding class on the cubic-graph link configuration space (reuse block01 R-C winding machinery). Output: "class nontrivial internally (crack)" vs "class trivial on closed A_min links (sharper externality no-go)." |

### S6 — Noncommutative geometry / spectral triple with REAL structure J (KO-dimension) → P-REC + P-COMP bridge

| Field | Entry |
|---|---|
| **Sector** | Noncommutative geometry; real spectral triples `(A,H,D,J,γ)`; the KO-dimension table (mod 8) and the first-order / `J`-commutation axioms. |
| **Reframe** | Instead of the *finite* Connes-Lott internal-space triple (which the repo has explored for Koide and which the KOIDE Z3-equivariant no-go bounds), use the **real-structure axiom** of an NCG spectral triple as the formal home for BOTH the chirality grading γ and the CPT conjugation J **simultaneously**. A_min supplies `A = M_2(C)` per site (Quantum), a candidate `D` (staggered, with `εDε=−D`), `γ = Γ_5^spin`, and `J = K`/CPT (Record). The NCG axioms (`J^2=±1`, `JD=±DJ`, `Jγ=±γJ` with signs fixed by KO-dimension mod 8) are **algebraic compatibility constraints** that may *uniquely fix* the chirality/taste data the bare algebra leaves free. |
| **Candidate theorem/tool** | Connes' reconstruction: a real spectral triple's KO-dimension (mod 8) is determined by the three signs `(ε,ε',ε'')` in `J^2=ε`, `JD=ε'DJ`, `Jγ=ε''γJ`. For a 4d Lorentzian/Euclidean Dirac, KO-dim is fixed (e.g. 4 for Euclidean SO(4)); the signs then **constrain γ uniquely** relative to J. The first-order condition `[[D,a],JbJ^{-1}]=0` is a *selector* on which D (hence which taste-restricted chirality) is admissible. |
| **Minimal toy** | On the even-`2^4` carrier: `A=M_2(C)` (site), `H=C^{16}`, `D=D_red(p)`, `γ=Γ_5^spin`, `J=K`/CPT. Compute the three KO-signs; check the first-order condition `[[D,a],JbJ^{-1}]=0`; enumerate which single-taste projectors are compatible with ALL real-triple axioms at the SO(4) KO-dimension. |
| **Attacks which wall** | **P-REC** (selector) AND provides the formal frame for **S1/S4** (J = the same K/CPT that supplies the real-form reduction and the CPT mirror). If the real-triple axioms + KO-dimension single out one taste-chirality datum, the selector is forced by *consistency of the spectral-triple structure A_min already instantiates*, not by a new axiom. |
| **Falsifier** | If the first-order condition + KO-signs are satisfied by **more than one** inequivalent single-taste chirality (i.e. the real-triple axioms are too weak on the finite carrier), the selector remains free and the wall stands. Also fails if A_min's `D` does **not** satisfy the first-order condition for `A=M_2(C)` acting site-locally (then there is no genuine spectral triple to constrain — a different, possibly informative, negative result about whether A_min even forms a real triple). |
| **First artifact** | runner: assemble `(A=M_2(C), H=C^16, D_red, γ=Γ_5^spin, J=K/CPT)`; compute KO-signs `(ε,ε',ε'')`; test the first-order condition and `J`-commutations; **count admissible single-taste chiralities** under the full axiom set. Output: "unique ⇒ selector forced by real-triple consistency" or "≥2 ⇒ wall stands"; secondary output: "A_min is/ is not a genuine real spectral triple on the finite carrier." |

### S7 — Bott periodicity / KR-theory mod-2 invariant (the index that survives when K^0 dies) → P-ABJ / P-REC

| Field | Entry |
|---|---|
| **Sector** | KR-theory / KO-theory; mod-2 (Z_2) topological invariants; the `Pin`/`Spin` cobordism Z_2 anomaly that survives when the integer index vanishes. |
| **Reframe** | The square-block no-go kills the **integer** index `A_t = N_+ − N_-` (it forces `N_+ = N_-`). But integer-trivial Dirac operators can still carry a **mod-2** invariant (the `Z_2` index of a real/quaternionic-type operator, `dim_{Z_2} ker D mod 2`, Atiyah's `KO^{-1},KO^{-2}` mod-2 indices). The reframe: even though `N_+ = N_-` on the closed even torus (integer index 0), the **mod-2 index of the real (Majorana) form** may be nonzero — a different invariant that the square-block argument (which is about *signed heat trace* = integer K^0) does not constrain. |
| **Candidate theorem/tool** | Atiyah's mod-2 index theorem: for a real-skew (KO-degree 1 or 2) elliptic operator, `ind_2 = dim ker mod 2 ∈ Z_2` is a homotopy invariant **even when the integer index is 0**. The framework's `D` is real anti-Hermitian (CPT_EXACT) ⇒ exactly the real/quaternionic class where mod-2 indices live. |
| **Minimal toy** | On the closed even `2^4` torus where `A_t = 0` (integer index 0, square-block), compute `dim_R ker D mod 2` for the **real** form of `D` (use the Majorana/real structure from S1). The square-block argument shows `B B^†` and `B^† B` share spectrum *including zero multiplicity* — so `dim ker = 2·dim ker B`, which is **even** ⇒ mod-2 index 0 on the *square* block. The escape: a **non-square** real block (odd zero-mode count) gives mod-2 = 1; the question is whether the Majorana reduction makes `B` effectively non-square (real vs complex zero modes). |
| **Attacks which wall** | **P-ABJ internal route**, by attacking a *different invariant* than the one the square-block no-go pruned. Explicitly NOT the K^0 / ε-index (pruned) and NOT the K^1 spectral flow (pruned by ε-gap) — it is the `KO^{-2}` mod-2 index, untested. Secondary: ties to **P-REC** since the real form is the same Majorana structure. |
| **Falsifier** | The square-block proof shows the staggered zero-mode multiplicity is **even** on the equal-sublattice closed torus (`dim ker = 2 dim ker B`). If the Majorana reduction preserves this evenness (real zero modes still come in the same paired count), the mod-2 index is **forced to 0** and this lens is pruned too — confirming the square-block wall is robust to mod-2 invariants. The reframe lives or dies on whether the *real* kernel dimension can be odd while the complex one is even. |
| **First artifact** | runner: on the closed even `2^4` torus, build the real form of the staggered `D` (S1 machinery), compute `dim_R ker D mod 2` and `dim_R ker B mod 2`; verify the square-block prediction `dim ker D = 2 dim ker B` (even) and check whether the Majorana reduction breaks the pairing. Output: "mod-2 index can be 1 (NEW escape ray)" or "mod-2 forced 0 (square-block robust to KO^{-2})." |

---

## Cross-sector synthesis (which lens hits which wall, ranked)

| Rank | Lens | Wall | Win-shape if it succeeds | Why ranked here |
|---|---|---|---|---|
| 1 | **S1** real/quaternionic Clifford module (KO-degree) | **P-REC** | derivation of a forced selector from Record's K/CPT real structure | P-REC is the highest-value soft wall; S1 uses an *approved* structure (Record K/CPT) as the supplier, exactly the EXERCISE's preferred win; cheap finite runner; clean falsifier. |
| 2 | **S4** representation-theoretic CPT closure | **P-COMP** | existence + n=0 supplied by Record K/CPT orbit (no new matter) | directly dissolves the "Record is only a consumer" premise that walls P-COMP existence; the K/CPT orbit IS the Record axiom; falsifier (vectorlike vs chiral) is sharp and decisive. |
| 3 | **S2** Skolem–Noether reframe | **P-REC** | reframe: consumer never needed a selector (gauge redundancy) | the second EXERCISE win-shape ("make the identification unnecessary"); parallels the retired α=1/3 convention; but real risk that chirality orientation is moved by inner automorphisms (so ranked below S1). |
| 4 | **S6** real spectral triple (KO-dimension) | **P-REC** (+frame for S1/S4) | selector forced by real-triple consistency of A_min's own data | unifies S1+S4 under one formal frame; but heavier and the first-order condition may simply fail on the finite carrier. |
| 5 | **S3** Kähler-Dirac on non-product complex (χ) | **P-ABJ** | χ≠0 on an A_min-canonical closed complex (integer-index crack) | most likely *sharpens* (closed ⇒ χ=0) rather than cracks, per block01 all-odd result; still the cleanest untested χ route since it changes the *complex* not the *torus*. |
| 6 | **S7** KO^{-2} mod-2 index | **P-ABJ** (+P-REC tie) | a nonzero invariant where the integer index is forced 0 | genuinely attacks a *different invariant* than both pruned index routes; but the square-block evenness (`dim ker = 2 dim ker B`) is a strong headwind. |
| 7 | **S5** gauge-group cohomology (5-cocycle) | **P-ABJ** | crack: B2 implication becomes internal; OR sharper externality no-go | block01 R-C `Q=0` makes the class almost certainly trivial on closed links ⇒ most likely a sharper no-go, not a crack; still worth recomputing the cocycle in-tree since `su3_dabc_symmetric` is audited_failed. |

### Most promising single artifact

**S1 (real Clifford-module / KO-degree selector for P-REC).** It is the only
lens that proposes an A_min-internal **supplier** (Record's K/CPT real structure)
for the one selector that, if forced, would partially unlock the 1105 cone — and
it is a cheap, decisive finite computation (`count J-real single-taste
projectors`). The honest expectation is uncertain: the block01 freedom was a
*complex* `M_4(C)` commutant, and whether the K/CPT real structure cuts it to a
1-dim centralizer (forcing one taste) is exactly the open question — which is why
it is a real attempt, not a foregone conclusion.

### Per-wall reading (math-sector lens)

- **P-REC (soft wall):** most attackable. Three independent new angles (S1 real
  form, S2 Skolem-Noether gauge reframe, S6 real spectral triple) all route
  through Record's K/CPT — a structure the framework already has. **Reframable→
  possibly closable** if K/CPT cuts the taste commutant; not yet walled by any
  read theorem (the M_4(C) freedom is a *complex*-carrier artifact none of the
  bounding notes proves persists under the real reduction).
- **P-COMP:** one strong new angle (S4 CPT closure) that challenges the load-
  bearing "Record is a consumer not a source" premise by pointing at Record's own
  K/CPT orbit. **Reframable**; the decisive risk is vectorlike-vs-chiral, testable
  immediately. Circular-on-parent is untouched by math-sector work (it is a
  dependency-graph problem).
- **P-ABJ:** genuinely walled internally on the integer index (square-block) and
  the spectral flow (ε-gap). The three new math angles (S3 χ on non-product
  complex, S7 KO^{-2} mod-2, S5 gauge cohomology) most likely **sharpen the wall**
  (closed/single-valued A_min ⇒ χ=0, even kernel, trivial class) rather than break
  it — but each tests an invariant the existing no-gos do **not** cover, so each
  yields either a crack or a strictly sharper citable no-go. External B2 admission
  itself is irreducible under no-new-axioms (Decision I).

### What NOT to do next (math-sector specific)

- Do **not** recompute the integer ε-index, the K^1 spectral flow, or
  `K_{C3}(pt)` — all pruned. Do **not** import Fukaya/Catterall/Adams results as
  authority (cited demolition-only); any external skeleton must be rebuilt in-tree
  and re-audited.
- Do **not** assume the `γ_μ ↔ lattice-edge` index pairing or first-order kinetic
  order in any S1/S6 construction — `INDEX_PAIRING_NOT_FORCED` shows both are
  unsupplied; carry them as named conditions, or the runner self-confirms.
- Do **not** re-run the Connes-Lott `γ_CL ≡ C3-character` hybrid (KOIDE Z3
  no-go); S6 uses J=K/CPT as the real structure, a *different* object.
- Do **not** ship any S5/S3 outcome as a P-ABJ closure; the external B2 admission
  stays. The honest deliverable for the P-ABJ lenses is "crack or sharper no-go,"
  not "wall solved."
- Do **not** treat S1/S2/S4 as solved without the runner: each has a named
  falsifier (real commutant > R; orientation moved by inner automorphism; K/CPT
  conjugate is vectorlike / wrong-n). A realized-state-dependent outcome is
  registered data, not a derivation (realized_state_primitive counterfactual
  clause) — the runners must show the result is invariant over the law-admissible
  family, not just true at one state.
