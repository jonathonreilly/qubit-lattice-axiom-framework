# Finite Point-Like Massless Zero Set (B-Z2) — Downstream Load-Bearing Scouting Report

**Type:** PROPOSAL (scouting / reconnaissance)
**Status:** hypothetical_axiom_status (`proposal_allowed = false`)
**Status authority:** the independent audit lane + owner ONLY. **This note sets
NO audit status** — it neither asserts, predicts, promotes, nor demotes any
audit outcome or effective status.
**Date:** 2026-06-24

> **This note touches NO canonical, audit, or publication file.** It does not
> edit any `MINIMAL_AXIOMS_*`, `AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`,
> `MISSING_DERIVATION_PROMPTS.md`, any `*_EFFECTIVE_STATUS.md`, or any
> `docs/audit/data/**` file. It registers **no primitive** and changes no axiom
> memo. It runs no script that rewrites tracked `outputs/`. It is a source-side
> reconnaissance note only; the independent audit lane is the sole status
> authority.

---

## PURPOSE

Scout whether the candidate primitive **B-Z2** is already implicitly load-bearing
across the repo's downstream retained/landed results, and — the actual prize —
whether any downstream consumer needs it for a reason **logically prior to /
independent of** the kinetic-order choice (`φ = ±1`).

**B-Z2 (the scouted primitive).** "The realized matter kinetic kernel has a
FINITE, point-like massless zero set — finitely many propagating zero modes per
Brillouin zone; equivalently `ker = carrier`, no extra massless sectors beyond
the embedded carrier (no extensive flat zero band)."

**Why it matters.** The `d ≤ 3` upper leg of the dimension derivation is
conditional on the single bit `φ = −1` (first-order Dirac kinetic order `K1` vs
second-order scalar `K0`). The 2026-06-23 adversarial attack
([`PHI_MINUS_ONE_SELECTOR_ATTACK_PROPOSAL_2026-06-23.md`](PHI_MINUS_ONE_SELECTOR_ATTACK_PROPOSAL_2026-06-23.md))
proved `φ = −1` is IRREDUCIBLE on the current primitive set
`{Lattice, Quantum, Record, P2 kinetic-isotropy, P3 realized-state}`. Its Route 2
(VERDICT table, Attack §VERDICT) is the **only** route that excludes the `K0`
countermodel by a non-circular, geometry-blind principle — and that principle is
exactly B-Z2. The attack found B-Z2 fails on AUTHORITY (no accepted primitive
supplies it), not on circularity. If B-Z2 were already pervasively and
**independently** load-bearing downstream, admitting it explicitly would be nearly
free — it would formalize an existing assumption AND discharge `φ = −1` AND let A1
weaken from the `Z³` lattice primitive to a derived `Zᵈ` cap (the upper leg of
[`D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md`](D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md),
Clause A).

**The circularity bar (applied ruthlessly).** A downstream reliance on B-Z2 counts
as INDEPENDENT justification ONLY if its need for a finite/point-like massless set
does NOT already presuppose `K1` / `φ = −1` / first-order Dirac / the linear cone
`|E| = |p|`. A result that first ASSUMES the staggered-Dirac (`K1`) realization and
THEN counts its 8 zeros is CIRCULAR (it assumed `φ = −1` already) — it is a
cost-benefit datum (shows B-Z2 is pervasively assumed) but NOT independent
justification.

**The respected negative (already proven, not re-tread).** DENSITY-based arguments
do NOT forbid `K0`. Per-volume entropy density `N₀·ln2/V → 0` and per-volume IR
log-det coefficient `2N₀/V → 0` on BOTH branches; the extensive `K0` zero surface
has measure-zero density in the continuum (verified
[`P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md)
§F-2, L186-197). A valid independent consumer must need POINT-LIKENESS
(integer/isolated), not merely finite density.

**The two rays (settled).** `K0` `φ=+1` scalar `H=(Σ cos p)I₂`, qubit spectates
`[H,σ]=0`, EXTENSIVE zero surface `{Σ cos p=0}` (20/68/140 modes at L=4/8/12);
`K1` `φ=−1` Dirac `H=Σ σ sin p`, qubit active, 8 isolated zeros at `p_μ ∈ {0,π}`
(Attack THE TWO RAYS, L56-67).

---

## PER-SECTOR FINDINGS

Six sectors were scouted and independently re-adjudicated against the source notes.
The taxonomy used below has three load-bearing classes, because the data forced a
distinction the binary circular/independent split obscures:

- **CIRCULAR** — assumes `K1`/staggered-Dirac first, then counts its zeros. Pervasive
  assumption of B-Z2, but no independent justification (the bar's circular case).
- **CARRIER-FINITE / SUPPLIED-FINITE** — needs a finite INTEGER count, but gets it
  from somewhere OTHER than a kinetic-kernel zero set (the algebraic carrier
  `C^8 = (C²)^{⊗3}`; or an externally-supplied Record decomposition). Non-circular
  w.r.t. `K1`, but **a non-consumer of B-Z2**: it never reads a propagator zero
  locus, so admitting B-Z2 discharges nothing it needs.
- **AMBIGUOUS** — touches a cone-free point-like clause but carries zero load (a
  named-open residual nothing consumes), OR separates branches only via a forbidden
  density currency.

### Sector A — Species / Particle Content

Verified the root supplier and the four best "independent"-looking rows in full.

- **CIRCULAR (assume `K1`, then count):**
  `NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md:19-35`
  — finiteness is literally read off the first-order Dirac symbol:
  `D_naive(k) = (i/a)Σ γ_μ sin(k_μ a)` (L19), `(-i a D)² = (Σ sin² k_μ)I` so
  `D=0 iff sin(k_μ a)=0`, cardinality `2^d` (L27-32); own Boundary (L43) disclaims
  "regulator-independence of the `2^d` count." This IS the `K1` ray. Also
  `STAGGERED_DIRAC_SUBSTEP3_SPECIES_REDUCTION_BRIDGE...2026-05-16.md` (16=4×4 corner
  count), `CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER_DECOUPLING...2026-06-08.md`
  (8 doubler corners), `STAGGERED_CHIRAL_SYMMETRY_SPECTRUM...2026-05-02.md` (8 zero
  modes of the staggered kernel).
- **CARRIER-FINITE (non-circular, but NOT a B-Z2 consumer):**
  `CL3_TASTE_GENERATION_THEOREM.md:53-83` — a pure S3/Z3 representation theorem on
  the "admitted abstract `C^8 = (C²)^{⊗3}` carrier" (L53-56); Non-Claim Boundary
  (L78-83) explicitly disavows carrier realization, action, kinetic kernel,
  chirality. Finiteness is representation-space dim 8, NOT a propagator zero set.
  Likewise `NATIVE_GAUGE_CLOSURE_NOTE.md` (finite matrix algebra on `C^8`),
  `LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md` (exact Fraction trace
  arithmetic on retained multiplicities 6+2 Weyl),
  `CLIFFORD_CHIRALITY_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md:200-207` (its
  forbidden-imports list literally states "No staggered-Dirac realization … not a
  fermion field, action, or Grassmann CAR boundary").
  - SHARPENING on `ANOMALY_FORCES_TIME_THEOREM.md:107-116` — its lower bound imports
    premise CHI (the staggered Dirac `{ε, D_staggered}=0`) and P-REC, so it DOES
    touch the `K1` realization — but only as a chirality GRADING (anticommutation
    algebra), never as a kinetic-zero count; its integer count (8 Weyl) is
    carrier/HY-surface algebraic. Still a non-consumer of B-Z2.
- **AMBIGUOUS:** `AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN...2026-05-26.md` — its
  hypothesis (Z) bundles point-likeness WITH a linear cone; density currency;
  it is the proposed SUPPLIER of B-Z2, not a consumer (see Sector B).

**Verdict A.** No independent consumer. Decisive structural finding: the retained
species/generation/anomaly/chirality RESULTS get their finite integer count from
the algebraic taste-cube carrier `C^8 = (C²)^{⊗3}` (= the 8 sublattice corners of
bipartite `Z³` + finite Cl(3), i.e. A1+A2), NOT from any kinetic-kernel massless
zero set. `CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER_DECOUPLING` proves these are
different objects (a γ-matrix is not a momentum-space corner; spinor dim 4 ≠ species
count 16). So admitting B-Z2 formalizes NO pervasive existing assumption in Sector A
— the species sector stands on carrier finiteness, a separate already-supplied
primitive (`Z³`-bipartiteness hands them an integer count for free).

### Sector B — Finite Species Density / Matsubara / Determinant (where B-Z2 was first named)

- **The cone-free clause exists but carries zero load.**
  `P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md` states
  B-Z2 cone-free (L33-34 "a point-like zero set; `ker = carrier`, equivalently no
  extra massless sectors"; N2 L167-168) and proves point-likeness is SEPARABLE from
  kinetic order via the on-site `−6` scalar comparator with point-zeros `1,1,1`
  (L96-98). That separability is real. BUT the file is a NO-GO and the clause is a
  NAMED-OPEN RESIDUAL no result consumes: L59-60 "the linked candidate rows do not
  require that property"; L80 "This note supplies none of those principles"; L127
  "Adding it would select `K1`; this note does not add it"; N7 L183-187. A residual
  nothing depends on is **not an independent consumer** — there is no consumer.
  Correct label: **AMBIGUOUS** (right cone-free shape, zero load).
- **Every load-bearing separator routes through the linear cone (CIRCULAR).**
  `P_FLUX_FINITE_SPECIES_DENSITY...2026-06-10.md` confirms the only separator with
  retained-grade currency, `g_eff`, is cone-bundled: B-F2 (L266) "strictly stronger
  than the bare point-like-zero-set clause (it adds conical dispersion)"; F-3
  (L436-438). The cone-free F-1 order-of-vanishing currency (L429 `ord_m det(D_E+mI)
  = N₀(L)`, bounded `(8,8,8)` vs extensive `(20,56,68)`) is consumed by no retained
  row (B-F1, L265 "real but consumed by no retained row; stating a retained
  requirement on any of them IS B-Z2, still open and not granted").
- **The supplier smoking gun.**
  `AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN...2026-05-26.md` (FSB-K) is the unique
  retained-currency would-be supplier of B-Z2, and it mathematically REQUIRES the
  linear cone: hypothesis (Z) bundles finite zero set with "invertible real `3×3`
  matrices `V_jb`" (L9-13); `g_eff = Σ|det V_jb|⁻¹` (L16); it proves bare
  point-likeness is insufficient (a quadratic point-zero gives `g_eff ∝ T^{−3/2}`,
  L24-25); it is "neither assumes nor derives `phi = -1`" (L30-32) and is the named
  SUPPLIER ("If retained, this row supplies, conditionally on (Z), the clause 'the
  massless species density is finite'", L42-44). It is positioned as the supplier of
  B-Z2, not a downstream consumer of it. `STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE
  _CERTIFICATE...2026-06-11.md` and `P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE
  ...2026-06-11.md` certify (Z) on the already-`K1` Kawamoto-Smit kernel and select
  `φ=−1` by counting its 8 cones — textbook circular.

**Verdict B.** No independent consumer. The FINITENESS half of B-Z2 is pervasively
COMPUTED throughout the family (cost-benefit datum), but every actual selector with
currency smuggles the Dirac cone. Density route killed on both branches (respected
negative confirmed live).

### Sector C — Continuum limit / Emergent Lorentz / Poincaré

- **CIRCULAR matter-side rows (≥5):** the free staggered-Dirac SO(4) 2-point
  (`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4...2026-05-29.md:38-56`, starts
  from `D̃(p)=m+iΣγ_μ sin p_μ`), `EMERGENT_LORENTZ_INVARIANCE_NOTE.md:88-98` (expands
  the staggered `sin²` dispersion), the velocity-RG attractor
  (`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR...2026-06-06.md` — a "velocity"
  presupposes a linear cone), `EMERGENT_POINCARE_FREE_SECTOR...2026-06-09.md` (free
  Euclidean Dirac kernel), `FREE_FIELD_OS_WIGHTMAN_RECONSTRUCTION...2026-05-30.md`
  (Dirac-form-fixed `S(p)=(m-iγ·p)/(p²+m²)`).
- **Non-circular but NON-supporting:** `LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM
  _NOTE.md:66-104` uses the SECOND-ORDER bosonic Laplacian dispersion and still gets
  exact continuum SO(3,1) — but expands around a MASSIVE mass shell (`m>0`), never a
  massless set. `OSTERWALDER_SCHRADER_FROM_FRAMEWORK...2026-05-27.md` needs finite-
  DIMENSIONALITY of the reconstructed Hilbert space and even excludes the zero
  spectrum (a Record/finite-block fact, not point-likeness).
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION...2026-04-29.md` needs a mass GAP (opposite
  regime) and disclaims continuum Lorentz (L426-427).

**Verdict C.** No independent consumer. The two real K1-independent inputs the
sector uses are (a) a single IR band-minimum/mass-shell expansion point — satisfied
by ANY band including `K0`'s at `p=0`, so NOT a point-likeness need — and (b) a mass
gap (gap-based). Counter-evidence noted: the free-SCALAR SO(3,1) family shows
continuum Lorentz survives on the `K0` second-order branch WITHOUT a point-like cone.

### Sector D — Cluster decomposition / mass gap / reflection positivity / transfer matrix / Lieb-Robinson

- **The strongest non-circular candidate is a clean NEGATIVE.**
  `CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md:147-205` and
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION...2026-04-29.md`: the load-bearing object is the
  transfer-matrix gap `Δ_T := -log(λ_1/M_T) > 0`, which is "non-degeneracy of the
  top eigenvalue (Perron–Frobenius regime, isolated top eigenvalue)" (B.5, L154-158)
  — i.e. **vacuum / ground-state uniqueness**. This is genuinely non-circular w.r.t.
  `φ` (no Dirac cone, no staggered frame), but it is logically ORTHOGONAL to B-Z2:
  the object it needs is a unique vacuum, NOT finiteness of the propagating massless
  set. The bridge is even only TEMPORAL ("does not prove spatial cluster
  decomposition", L201-205) and conditional on an underived `Δ_T>0`.
- **DEGENERACY-TYPE MISMATCH (decisive).** `K0`'s extensive zero set is a codim-1
  SURFACE in the single-particle MATTER dispersion (a band-center / Fermi surface),
  a different object from many-body VACUUM degeneracy. The framework's own no-gap
  counterexample (cluster note, `H=0`) is a vacuum degeneracy. So the a-priori
  intuition "flat band → infinite ground-state degeneracy → breaks cluster
  decomposition" is NOT instantiated.
- **RUNNER-CERTIFIED BRANCH-NEUTRALITY.** `P_FLUX_POINT_ZERO_SET...2026-06-10.md`
  (L64-67, L102-104): at `m=0` BOTH branches gapless; under the shared anticommuting
  mass probe `mε` BOTH gap to exactly `m`, with identical range/hopping-norm data;
  runner `PASS=22 FAIL=0`. Cluster decomposition literally cannot distinguish an
  8-point zero set from a 140-mode zero surface.
- **CIRCULAR (staggered-grounded):** `AXIOM_FIRST_SPECTRUM_CONDITION` (SC3),
  `TRANSFER_MATRIX_LOG_QUASILOCALITY...2026-06-10.md` (rate `arcsinh(m)`), microcausality
  M2b — all ground on the Kogut-Susskind (=`K1`) surface per the
  `GATE_RP_REGROUND_STAGGERED_ONLY` pin. The LR core (L1/L3/L4) is the sole genuinely
  non-circular leg and is provably INERT on B-Z2 (finite-range + Hermiticity + finite
  Cl(3) norm, shared identically by both branches).

**Verdict D.** No independent consumer. The sector bottlenecks on a transfer-matrix
GAP (vacuum uniqueness) or a staggered mass `m>0` — both logically prior to AND
distinct from B-Z2, and both branch-neutral. The sector is silent on point-likeness;
admitting B-Z2 buys essentially nothing here.

### Sector E — Mass spectrum / Hierarchy / Koide

- **PERVASIVE and uniformly CIRCULAR.** The finite, isolated, enumerated species set
  is the structural backbone of essentially the entire tower, and all of it traces
  to ONE supplier: the `2^d` / `1+3+3+1` BZ-corner zero set of the first-order naive/
  staggered Dirac operator (`NAIVE_LATTICE_FERMION_TWO_POWER_D...2026-05-10.md`,
  verified to read finiteness off `D_naive=0 iff sin(k_μ a)=0`, L30). Downstream:
  3-generation count (`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md:97-102`), Koide
  value chain (`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`),
  hierarchy exponent 16 (`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE...2026-05-10.md`),
  DELTA0 taste staircase n∈{1..16} (`HIERARCHY_DELTA0_S3_FIXED_GAP_SPECTRUM...2026-06-18.md`),
  cosmology k_B=8 (`COSMOLOGY_FROM_MASS_SPECTRUM_NOTE.md`).
- **Cleanest internal admission:** `HIERARCHY_ALPHA_LM...2026-05-10.md:71-72` —
  "the exponent 16 is substrate-imposed unless a named regulator/substrate target is
  supplied", and its B1 table shows the count is regulator-dependent (Wilson 1,
  staggered 4, overlap 1). The repo ITSELF proves the 16 is NOT a kinetic-order-
  independent invariant — it inherits finiteness FROM the naive Dirac form.
- **Record/readout route probed and found circular:** `ACPHILAMBDA_SPECIES_BRIDGE
  _REALIZED_STATE_DECOMPOSITION...2026-06-11.md:46-60,225-244` — the
  realized_state_primitive/G1 machinery only does pointwise sector-to-mass
  REGISTRATION on an already-supplied finite hw=1 triplet; the triplet's finiteness
  comes (dep table L242-244) from the staggered-Dirac corner Hamming orbit; the
  residual is named "forcing the first-order chiral operator class" = `φ=−1`.

**Verdict E.** No independent consumer. B-Z2 is silently assumed nearly everywhere
(maximally favorable cost-benefit datum) but supplies ZERO non-circular justification:
every integer (3, 16, 4) is a Dirac corner cardinality.

### Sector F — Non-kinetic-order supplier hunt (the prize)

The dedicated hunt for a consumer needing B-Z2 for a reason logically prior to the
kinetic order, across the bar's named candidate routes.

- **Record/readout finiteness — non-circular but INERT on B-Z2.**
  `RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md:17-46`: finiteness is a
  SUPPLIED INPUT ("Given a supplied finite record-sector decomposition", L18-20); the
  object is a sector readout VECTOR bounding registered OUTCOMES, not a kinetic
  kernel's spectral support; it does not turn readout into "dynamics, source/action,
  occupancy, or a value selector" (L22-26). Same for
  `RECORD_FINITE_ALPHABET_POST_RECORD_DYNAMICS_2026-06-05.md`. This matches the
  Attack's own Route-2 tier-(ii): A3 finiteness is "distinguishable registered
  OUTCOMES, not the spectral support of a propagator" (Attack L203-209).
- **Integer-species well-definedness — CIRCULAR (carrier-conditional).**
  `P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md:8-9,61,78`
  computes the embedded hw=1 Klein-cube carrier (full Klein cube, count 3) inside
  BOTH `K0` and `K1`: K0's zero-mode sector "contains a unique embedded pi-cube
  carrier satisfying the same battery" (L61). So the integer-3 count is
  carrier-conditional, true on both branches, and does NOT require `ker=carrier`. The
  closest "integer particle number" candidate,
  `STAGGERED_DIRAC_PHYSICAL_SPECIES_DIRECT_THEOREM_NOTE_2026-05-07.md`, builds count=3
  on this embedded carrier on the staggered surface and self-disclaims closing the
  physical-species bridge. A version excluding `K0` must assert
  carrier=realized-matter-sector=`ker=carrier`=B-Z2 itself (self-supply).
- **Cluster decomposition / mass gap — non-circular but does NOT supply B-Z2.** As in
  Sector D: forbids extensive VACUUM degeneracy; the `K0` object is an extensive
  single-particle massless zero SURFACE of measure zero with a UNIQUE vacuum — these
  principles have no grip on it; and cluster is gap-conditional + branch-neutral.
- **Reeh-Schlieder vacuum-separation — CIRCULAR.**
  `AXIOM_FIRST_REEH_SCHLIEDER_THEOREM_NOTE_2026-05-01.md` is scoped to the staggered-
  only surface; bounds local-algebra annihilators, never a kinetic kernel's zero-set
  cardinality.
- **Continuum-limit existence — non-circular but INERT.** `CONTINUUM_LIMIT_NOTE.md`
  is a gravitational-deflection trend table whose `h→0` claim is diagnostic-only and
  concerns a gravity propagator centroid, not the matter kinetic kernel.

**Verdict F.** No independent supplier/consumer found. The wave-3 supplier sweep
(`P_FLUX_FINITE_SPECIES_DENSITY...`) ran exactly the families where a non-circular
prize could live — determinant/Matsubara (consume the FULL spectral density, not a
carrier slice), thermal/g*/entropy, isotropy/Lorentz — and certified all
supplier-less; the density negative is confirmed live.

---

## THE KEY QUESTION ANSWERED

### (1) Is B-Z2 already pervasively assumed downstream?

**YES — pervasively, but almost entirely as a CIRCULAR / carrier-derived assumption,
never as an independent need.** Two distinct facts must be kept apart:

- **The FINITENESS half is pervasively COMPUTED.** The integer zero-mode count
  `(8,8,8)` for `K1` vs extensive `(20,68,140)` for `K0`, the `2^d` corner
  cardinality, the order-of-vanishing `N₀(L)`, the carrier count 3 — these recur
  across Sectors A, B, E, F. The repo computes B-Z2's predicate constantly, so the
  finiteness clause would formalize cleanly (favorable cost-benefit).
- **But the load-bearing RESULTS do not stand on B-Z2 as a propagator-zero-set
  fact.** Where a kinetic-kernel zero set is actually counted, the count is read off
  an already-fixed naive/staggered Dirac symbol (Sectors A, E — CIRCULAR). Where a
  finite INTEGER count is genuinely needed prior to the kinetic order (generations,
  Koide, anomaly, hierarchy), it comes from the algebraic carrier
  `C^8 = (C²)^{⊗3}` = the 8 sublattice corners of bipartite `Z³` + finite Cl(3)
  (A1+A2) — a DIFFERENT, already-discharged primitive, NOT the matter kinetic
  kernel's massless zero set (Sectors A, E, F — CARRIER-FINITE non-consumers).

Pervasiveness tally across the adjudicated consumers: roughly **15 CIRCULAR rows**
(assume `K1`/staggered, then count zeros — the entire Sector E backbone plus the
Sector A/B/C/D staggered-grounded rows), **~7 CARRIER-FINITE / SUPPLIED-FINITE
non-consumer rows** (carrier `C^8` or supplied Record decomposition), and **~6
AMBIGUOUS/inert rows** (cone-free residual carrying zero load, or density currency,
or gap/vacuum-uniqueness objects orthogonal to B-Z2). The split is overwhelmingly
**circular-or-orthogonal**.

### (2) Does any NON-circular consumer/supplier exist (the prize)?

**NO.** Across all six sectors, not one consumer needs point-likeness
(integer/isolated, as opposed to finite density) for a reason that is BOTH
non-circular AND actually bites `K0`. The three best non-circular candidates each
fail to be a B-Z2 consumer:

- **Cluster decomposition / mass gap** (the strongest non-`K1` principle) needs
  VACUUM uniqueness (`Δ_T > 0`), an object logically prior to but ORTHOGONAL to
  B-Z2, and is branch-neutral besides.
- **Record/readout finiteness** supplies finiteness of registered OUTCOMES as an
  external input, never a bound on a kinetic kernel's zero-set cardinality.
- **The carrier integer count (3, 8)** is carrier-conditional — true on BOTH
  branches — so it does not entail `ker = carrier`; the only version that excludes
  `K0` IS B-Z2 (self-supply).

The single quantifier that actually binds the realized kernel's massless set is FSB-K
hypothesis (Z), which is (a) density currency (`g_eff`, the respected negative),
(b) cone-bundled (strictly stronger than point-likeness; the linear cone is the
circular Dirac assumption), and (c) the proposed SUPPLIER of B-Z2, not a consumer.
This UPHOLDS the Attack's Route-2 verdict exactly: B-Z2 fails on AUTHORITY, and there
is no downstream result whose authority could be borrowed.

---

## NET MINIMALITY

The cost-benefit question: admitting B-Z2 costs **+1 primitive**. What does it buy?

**The cost is a genuine new primitive (not a free formalization).** The decisive
structural finding is that the downstream tower does NOT free-ride on B-Z2 as a
matter-kinetic-kernel zero-set fact. The species/generation/anomaly/hierarchy results
that look like they need "a finite integer particle count" get that count from the
algebraic carrier `C^8 = (C²)^{⊗3}` (A1+A2), a SEPARATE primitive already discharged.
`CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER_DECOUPLING` proves a γ-matrix is not a
momentum-space corner — carrier finiteness and zero-set finiteness are different
objects. So the headline "B-Z2 is nearly free because it formalizes a pervasive
existing assumption" is **NOT supported** at the level of independent justification:
the rows that compute B-Z2's predicate either assumed `K1` first (circular — they
cannot ground it) or get their finiteness elsewhere (carrier — they do not consume
it). There is no row whose retained status would transfer to B-Z2.

**The benefit is real but singular and conditional.** Admitting B-Z2 (pure
finite-zero-set clause) would, per the Attack and the d3 proposal:
- discharge `φ = −1` from the primitive set (Route 2 is the only non-circular
  exclusion of `K0`; B-Z2 is exactly its missing premise — Attack VERDICT, L404-408);
- make the `d ≤ 3` upper leg unconditional (currently graded entirely by the
  UNAUDITED `φ=−1` bit — d3 proposal UPPER LEG, L354-359);
- license weakening A1 from the `Z³` lattice primitive to a derived `Zᵈ` cap
  (Attack IMPACT, L494-498).

**Quantitative net assessment.** The benefit is **+0 new rows grounded** (no row
free-rides on B-Z2 as a zero-set fact) and **exactly 1 bit discharged** (`φ=−1`,
which then unblocks the upper leg and the A1→Zᵈ weakening). The cost is **+1
primitive**. So the trade is NOT "remove N free-riders for the price of 1" — it is
"pay 1 primitive to convert the UNAUDITED `φ=−1` posit into an admitted one of equal
logical weight, and thereby buy the upper-leg/A1 consequences." That is a **lateral
move in primitive count** (B-Z2 replaces the `φ=−1` posit one-for-one; the d3
proposal already counts `φ=−1` / Clause A as a named posit), NOT a net simplification
of the kind "admit one, retire many." It is justified ONLY if the owner values the
`d≤3`-unconditional / A1→Zᵈ consequences enough to pay one explicit primitive for
them. There is no minimality discount from pervasive free-riding, because the
pervasive computation of B-Z2's predicate is either circular (cannot pay) or
carrier-sourced (does not need to be paid).

**Caveat on the weaker-vs-stronger form (load-bearing for minimality).** The minimal
admissible form is the **pure finite-zero-set clause** (cone-free). It is genuinely
non-circular (the `−6` scalar comparator with point-zeros `1,1,1` passes it —
`P_FLUX_POINT_ZERO_SET...` L96-98), and it is strictly WEAKER and more defensible
than the FSB-K cone-strengthened form. But note: bare B-Z2 does NOT by itself entail
linear dispersion. On the two-ray equivariance-forced surface
`M_μ = a·I + i·b·σ_μ`, the pure clause is logically identical to `φ=−1` (it forces
`b≠0`, the qubit-active branch — Attack Minimal posit, L417-426), so for the
selector question it suffices. It is when one additionally wants the linear cone
(emergent Lorentz) that the stronger cone form is needed — and that strengthening is
circular for the `φ` question and should NOT be bundled into the admission.

---

## RECOMMENDATION

**`do_not_admit`** as a free/cheap formalization of an existing pervasive assumption.
The premise of "nearly free because already load-bearing" is **not met**: no
independent (non-circular, point-likeness-needing) consumer exists, and the pervasive
computation of B-Z2's predicate is circular-or-carrier-sourced, so it transfers no
grounding. Reconnaissance verdict: **the prize is not in this repo as of 2026-06-24.**

This does NOT say B-Z2 should never be admitted. It says the **justification must be
the direct dynamics value** (`φ=−1` discharge → `d≤3` unconditional → A1→Zᵈ), priced
honestly as **+1 primitive replacing the `φ=−1` posit one-for-one**, NOT a minimality
windfall from downstream free-riders. If the owner+audit decide that direct value is
worth one explicit primitive, the recommendation is **`admit_conditional`** on the
audit checks below, with this exact minimal wording:

> **[B-Z2]** "The realized matter kinetic kernel has a FINITE, point-like massless
> zero set — finitely many propagating zero modes per Brillouin zone; equivalently
> `ker = carrier`, with no extra massless sectors beyond the embedded carrier (no
> extensive flat zero band). This clause does NOT by itself entail linear
> dispersion; it is strictly weaker than, and must not be conflated with, the
> conical/linear-cone (FSB-K) strengthening."

(Equivalent action-level form on the two-ray surface `M_μ = a·I + i·b·σ_μ`: "the
realized NN charge-conserving kinetic bilinear lies in the flux(−1) class, i.e.
`b ≠ 0`" — logically identical to `φ=−1`.)

### What the owner + audit must verify

1. **No-supplier finding still holds.** Confirm B-Z2 is genuinely NOT entailed by
   Lattice / Quantum / Record / P2 / P3 / A3 (verify against the actual primitive
   texts; confirm the wave-2/wave-3 P-FLUX "no retained supplier" finding survives).
2. **No independent free-rider was missed.** Re-confirm that every retained row
   computing a finite count either (a) reads it off an assumed naive/staggered Dirac
   symbol (circular), or (b) gets it from the algebraic carrier `C^8 = (C²)^{⊗3}`
   (carrier-finite non-consumer), or (c) supplies it as an external Record
   decomposition (inert). In particular re-audit `CL3_TASTE_GENERATION`,
   `NATIVE_GAUGE_CLOSURE`, `ANOMALY_FORCES_TIME`, `LH_ANOMALY_TRACE_CATALOG` confirm
   they never read a propagator zero locus.
3. **Carrier ≠ kernel.** Confirm `CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER
   _DECOUPLING` (γ-matrix is not a momentum-space corner; spinor dim 4 ≠ species
   count 16) — the carrier-finiteness primitive is a different object from B-Z2.
4. **The pure clause is the admitted one, not the cone.** Confirm FSB-K's binding
   clause (Z) bundles the circular isotropic linear cone and must NOT be the admitted
   form; B-Z2 must be admitted cone-free.
5. **Density does not sneak back.** Confirm the per-volume objects are finite on both
   branches (`2N₀/V → 0`, `N₀ ln2/V → 0`) so the admission is NOT justified by any
   density argument (respected negative).
6. **Net count is honest.** Confirm the admission is graded as +1 primitive replacing
   the `φ=−1` posit, NOT as retiring N free-riders; the d3 proposal's Clause-A count
   must be reconciled so `φ=−1` and B-Z2 are not double-counted.

---

## HONEST RESIDUALS / WHAT THIS DOES NOT CLAIM

- **Does not claim B-Z2 is false, unphysical, or unnatural.** It is the physically
  expected Dirac ray; the claim is only that it is not independently load-bearing
  downstream and is not freely formalizable.
- **Does not claim `K0` is the physical kinetic term.** `K0` is the
  runner-certified COUNTERMODEL that keeps the supplier question open; it is the
  witness, not a proposal for nature.
- **Does not claim exhaustiveness over every retained row.** Six sectors and their
  highest-risk consumers were read; a row outside the enumerated families could in
  principle harbor an independent need, though the dedicated wave-3 determinant/
  Matsubara/thermal/isotropy sweep (the families most likely to host one) found none.
- **Does not re-tread the settled `φ`-attack.** `φ=−1` irreducibility on the current
  primitives is taken as proven; this note only scouts the downstream load-bearing
  question the attack flagged for a future ledger decision.
- **Does not set, predict, or propose any audit status, retire any axiom, register
  any primitive, or perform any closure.** Source-side reconnaissance only.
- **The honest negative is itself the valuable outcome.** It tells the owner that
  B-Z2 cannot be sold as "already pervasively assumed by the downstream tower" — the
  tower's finiteness lives on the separate, already-discharged carrier primitive
  (`C^8` / `Z³`-bipartiteness), and where the kinetic kernel's zeros are counted it
  is downstream of an assumed Dirac form. The admission, if made, must rest on its
  direct dynamics value, priced as a genuine new primitive.

---

## CROSS-REFERENCES (by filename)

- [`PHI_MINUS_ONE_SELECTOR_ATTACK_PROPOSAL_2026-06-23.md`](PHI_MINUS_ONE_SELECTOR_ATTACK_PROPOSAL_2026-06-23.md)
  — the five-route `φ=−1` irreducibility attack; Route 2 names B-Z2 as the minimal
  posit; its VERDICT and Minimal-posit sections are this report's anchor.
- [`D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md`](D3_NATIVE_UNBLOCK_PROPOSAL_2026-06-23.md)
  — the dimension-compression companion; Clause A is the `φ=−1` bit B-Z2 would
  discharge; the upper-leg conditionality and A1→Zᵈ consequence.
- [`P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_POINT_ZERO_SET_FROM_RETAINED_ROWS_NARROW_NO_GO_NOTE_2026-06-10.md)
  — where B-Z2 is first named/collapsed-to; the cone-free clause as a named-open
  residual (AMBIGUOUS); the `−6` scalar comparator separability; branch-neutral
  clustering.
- [`P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_FINITE_SPECIES_DENSITY_FROM_DETERMINANT_MATSUBARA_SURFACE_NARROW_NO_GO_NOTE_2026-06-10.md)
  — wave-3 supplier sweep; F-1/F-2 (order-of-vanishing vs density), B-F2 (g_eff
  strictly stronger than point-likeness), respected-negative density confirmation.
- [`AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_FERMIONIC_STEFAN_BOLTZMANN_NARROW_THEOREM_NOTE_2026-05-26.md)
  — the named SUPPLIER of B-Z2 (hypothesis (Z)); proves point-likeness alone
  insufficient; bundles the circular linear cone.
- [`P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md`](P_FLUX_SELECTION_VIA_FSB_K_AND_Z_CERTIFICATE_CONDITIONAL_THEOREM_NOTE_2026-06-11.md)
  and [`STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md`](STAGGERED_KERNEL_SATISFIES_Z_POINT_CONE_CERTIFICATE_NARROW_THEOREM_NOTE_2026-06-11.md)
  — the within-surface FSB-K selection on the already-`K1` kernel (circular).
- [`P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md`](P_FLUX_SELECTION_FROM_MATTER_CONTENT_NARROW_NO_GO_NOTE_2026-06-10.md)
  — the carrier-conditional finding: the embedded Klein-cube carrier (count 3) lives
  inside BOTH branches, so the integer count does not entail `ker=carrier`.
- [`NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md`](NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the root CIRCULAR supplier of Sector E; finiteness read off the first-order Dirac
  symbol; own Boundary disclaims regulator-independence.
- [`CL3_TASTE_GENERATION_THEOREM.md`](CL3_TASTE_GENERATION_THEOREM.md)
  — the strongest CARRIER-FINITE non-consumer; pure S3/Z3 representation theorem on
  abstract `C^8`; Non-Claim Boundary disavows kinetic kernel.
- [`CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER_DECOUPLING_BOUNDED_NOTE_2026-06-08.md`](CLIFFORD_GAMMA_NOT_LATTICE_SPECIES_CORNER_DECOUPLING_BOUNDED_NOTE_2026-06-08.md)
  — proves carrier finiteness (spinor dim 4 / Clifford) and zero-set count 16 are
  different objects.
- [`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  and [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
  — the strongest non-circular candidate, a NEGATIVE: load-bearing object is vacuum
  uniqueness (`Δ_T>0`), orthogonal to B-Z2.
- [`RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md`](RECORD_FUNCTION_FINITE_SECTOR_ALGEBRA_2026-06-05.md)
  — the Record/readout-finiteness candidate; finiteness is a supplied input on
  registered outcomes, inert on the kinetic kernel.
- [`LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md`](LORENTZ_BOOST_COVARIANCE_3PLUS1D_THEOREM_NOTE.md)
  — counter-evidence: continuum SO(3,1) on the second-order (`K0`-class) bosonic
  Laplacian, no point-like massless set needed.
- [`HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`](HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md)
  — the repo's own admission that the integer 16 is substrate-imposed /
  regulator-dependent (Sector E circularity).

**Independent audit required.** This note asserts no effective-status change and
registers no primitive.
