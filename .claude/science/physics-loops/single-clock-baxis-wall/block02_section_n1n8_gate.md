# Block 02 section — N1–N8 NO-GO DISCIPLINE GATE (per-clause, three columns)

**Section role:** the mandatory No-Go Discipline Gate for the unified B-AXIS
obstruction note. The negative claim ("none of N2b / N4 / N5 is derivable from
A_min = Lattice + Quantum + Record plus the retained Euclidean reconstruction
surface") is shippable as a `no_go` only if it clears N1–N8 *per clause*. This
section answers every gate clause IN WRITING for the three columns
**N2b** (absolute clock unit), **N4** (axis-label), **N5** (no-second-clock /
factor-clock exclusion).

**Status discipline (whole section):** branch-local source artifact. No audit /
publication / effective-status surface touched; no bare "retained"/"promoted" in
any status line; Type:/Claim type: used only for *intended* audit classification.
The independent audit lane is the sole status authority. All load-bearing facts
are recomputed in the absorbed in-tree / in-flight runners cited by branch+path+
PASS; nothing is cited blind from the conditional parent keystone, the unaudited
finite-speed cone note, or the downstream ANOMALY_FORCES_TIME consumer.

**Authorities admissible as cited (per source discipline):** the retained no-gos
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go),
`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_2026-06-11`
(retained_no_go), `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16`
(retained_no_go), and `MINIMAL_AXIOMS_2026-06-05`. Witnesses covered by block01
in-tree runners are CITED by path+PASS, not rebuilt; witnesses not covered by
block01 (OS/GNS, record durability, registration cone, anomaly/chirality
transport; APBC sharpened pin) are CITED to the retained no-gos + the in-flight
branch runners by branch+path+PASS.

---

## Gate clause N1 — ≥5 distinct attacked routes per clause (ATTEMPTED vs RULED-OUT-BY-PRIOR, with authority)

The negative claim is admissible only if the route space was genuinely searched.
Each entry is tagged **[ATT]** (genuinely attempted in-cycle, terminating on a
named wall or relocation) or **[ROP]** (ruled out by a prior with authority).
Counts: **N4 ≥ 10** (incl. block01 R-N4-AUT automorphism + R-N4-REGDIR
registration-cone); **N5 ≥ 5** (incl. block01 R-N5-IRR irreducibility);
**N2b ≥ 4** (incl. block01 R-N2b-JOINT joint-gate).

### N2b column (absolute clock unit) — 5 routes

1. **[ROP] Absolute unit from the transfer spectrum / Stone reconstruction.**
   FAILED: finite-dim Stone is transfer- and τ-relative; `2a_τ → 2c·a_τ`
   rescales `H` by `1/c` with `T̂²` unchanged. Authority:
   `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go) +
   finite-Stone uniqueness; restated in
   `origin/physics-loop/single-clock-blocked-time-unit-split-20260617`
   (`scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py`,
   PASS=35 FAIL=0).
2. **[ROP] Unit from minimal Lattice/Quantum.** FAILED: Lattice gives sites +
   adjacency but no metric scale, spacing, or unit conversion. Authority:
   `MINIMAL_AXIOMS_2026-06-05` (Lattice clause).
3. **[ROP] Time metric/rate from Record alone.** FAILED: Record gives durable
   outcomes + finite additivity but no time metric, clock map, or rate.
   Authority: `MINIMAL_AXIOMS_2026-06-05` (Record clause).
4. **[ROP] Physical clock/rate from post-record count histories.** FAILED: a
   fixed finite record word embeds in many inequivalent strictly increasing
   clock maps (same word + counts under uniform/slow/accelerated clocks → distinct
   rates). Authority: `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06` +
   blocked-time-unit-split branch runner block `block_record_clocks`.
5. **[ATT] Joint two-rate-gate construction (block01 R-N2b-JOINT).** Genuinely
   built GATE-S (spectrum-condition normalization, `T̂²=exp(-2a_τH)`) ⊗ GATE-R
   (record clock/rate gate, kernel `K=exp(2a_τQ)`) under the *strongest single-
   clock coupling* (one clock drives both, `K=exp((2a_τ)Q)`), then applied the
   candidate rescaling `a_τ→c·a_τ, H→H/c, Q→Q/c`. WALLED (ratio-only): `T̂²`,
   `K`, `T̂²⊗K` all invariant (max Δ < 4e-16, swept `c∈{0.5,1.3,2.0,5.0}`); the
   gates fix only `m_gap·relaxation-time` (= 0.400000) and counts-per-block, never
   a unit. Sharpened structural reason: **no A_min observable returns a unit-
   bearing `1/time` number**. Runner:
   `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` (in-tree,
   PASS=17 FAIL=0). N2a (the `1/(2a_τ)` internal denominator) stays FORCED
   (resid 0), kept separate.

### N4 column (axis-label) — 11 routes

1. **[ROP] OS/GNS reconstruction privileges τ.** FAILED: W transports reflection,
   covariance, half-space kernel, spectra, positivity to `x₁` (resid 0; min eig
   both −1.648227). Authority: `..._RECORD_DURABILITY_NARROW_NO_GO_2026-06-11`
   (retained_no_go); recomputed in
   `origin/physics-loop/single-clock-axis-nogo-self-contained-20260617`
   (`scripts/single_clock_axis_selection_check_2026_06_11.py`, block [RT-RP]).
2. **[ROP] Record durability as physical axis.** FAILED: durability = operator-
   order monotonicity, unitary-transport-invariant (increment-spec diff 8.9e-16);
   Record supplies no time metric. Authority: same retained no-go + block [RT-REC].
3. **[ROP] Finite-speed registration cone / CAP-K.** FAILED (circular): any cone
   consuming a supplied generator + window is downstream of B-AXIS; slice
   transports `W_sl D^(1) W_sl^T = D^(τ)` (resid 0). Authority: same retained
   no-go + block [RT-REC]; (NOT cited from the unaudited finite-speed cone note —
   recomputed).
4. **[ROP] Anomaly/chirality identifies temporal axis.** FAILED: `ε(x)`
   W-invariant, `{D_hop,ε}=0` preserved; count-not-label firewall (constrains the
   number `d_t`, not the label). Authority: same retained no-go + block [RT-ANOM];
   (NOT cited from the downstream ANOMALY_FORCES_TIME consumer — recomputed).
5. **[ROP] KMS/APBC thermal antiperiodicity.** FAILED: exchange-covariant; W maps
   APBC-τ → APBC-x₁ exactly. Authority:
   `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16` (retained_no_go).
6. **[ROP] APBC-alone as selector.** FALSIFIED: symmetric APBC on *both* axes
   restores W (resid 0); only BC ASYMMETRY selects. Authority: KMS/APBC retained
   no-go + `origin/.../single-clock-apbc-axis-bridge-20260616`
   (`scripts/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py`,
   PASS=21 FAIL=0, falsifier leg (C)).
7. **[ROP] Per-axis Z₂ BC-asymmetry datum as a *non-transportable* selector.**
   FAILED: S₄ acts transitively on all four axes; `W₀₁ M_appp W₀₁^T = M_pappp`
   exactly, so the datum selects only relative to an already-privileged axis (block
   [T] self-resid 16). Authority:
   `SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_..._2026-06-17`
   (`scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py`,
   PASS=22 FAIL=0).
8. **[ROP] Reality/CPT grading `ε=(−1)^{Σx_μ}` as selector.** FAILED:
   `W ε Wᵀ = ε` (resid 0), W-inert. Authority: s4-transportable branch block [R]
   + s3-axis-identity-convention branch.
9. **[ROP] Wilson temporal-gauge / plaquette.** FAILED: singles an axis only via
   labeled choice `U₀=1` (transportable); plaquette/Bessel coeffs axis-blind.
   Authority: s4-transportable branch §4/§6.
10. **[ROP] Crossing-link RP invariant `P_a` + η-curvature 2-cocycle.** FAILED:
    `P_a=+1` on all axes; cocycle `=−1` in all planes incl. temporal;
    S_d-isotropic. Authority:
    `origin/science/single-clock-s3-axis-identity-convention-records-arrow`
    (`scripts/single_clock_axis_identity_convention_records_arrow_runner.py`,
    PASS=5 FAIL=0).
11. **[ATT] Full bare-surface automorphism + A_min-enrichment stabilizer search
    (block01 R-N4-AUT).** Genuinely computed `|G_bare|=384` (hyperoctahedral),
    axis image transitive S₄; swept enrichments E1–E8 for a sub-S₄ one-axis-
    selecting stabilizer. WALLED: every A_min enrichment's joint stabilizer is
    full S₄ (E1,E3–E6) or *trivial* (E2,E8 — W genuinely broken, but axis-
    symmetrically, selecting none); only E7 (per-axis Z₂ BC datum) is sub-S₄ (S₃),
    and it is S₄-transportable + outside A_min. Runner:
    `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` (in-tree,
    PASS=17 FAIL=0).
12. **[ATT] Derived non-transportable registration-direction bridge (block01
    R-N4-REGDIR).** Genuinely built record-accumulation / causal-cone monotones
    from A_min. RELOCATED-TO-OPEN-GATE: the A_min monotone is a direction-free
    *ball* (W-invariant, reflection-symmetric, resid 0); a real LR cone needs a
    supplied generator whose W-conjugate gives an identical cone (Δ 7e-16,
    circular); record-PRODUCTION CPTP+POVM are W-covariant (resid 0), break W only
    with a supplied asymmetric pointer datum (break 3.44). Runner:
    `scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`
    (in-tree, PASS=20 FAIL=0).

### N5 column (no-second-clock / factor exclusion) — 6 routes

1. **[ROP] Algebraic exclusion of commuting positive factor transfers.** FAILED:
   countermodel `T_A⊗I, I⊗T_B` commute (resid 0), rank-2 generator span.
   Authority: `origin/.../single-clock-n5-factor-boundary-20260617`
   (`scripts/single_clock_independent_commuting_transfer_factor_n5_no_go_2026_06_17.py`,
   PASS=34 FAIL=0) + physical-clock-inventory branch.
2. **[ROP] Product-transfer finite-Stone uniqueness erases factor flows.** FAILED:
   Stone returns `H_sum` but `U_A(1)⊗I` is off the diagonal one-clock orbit
   `exp(-irH_sum)` (min_gap 0.292 over `r∈[−8,8]`). Authority: n5-factor-boundary
   branch + `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go).
3. **[ROP] Record additivity collapses disjoint factor counters.** FAILED:
   disjoint projectors commute, operator-monotone (`0≤P_A≤P_A+P_B`), additive
   readout. Authority: n5-factor-boundary branch + `MINIMAL_AXIOMS_2026-06-05`.
4. **[ROP] Physical-clock-admission firewall (admit only the named transfer).**
   Recorded as a SOURCE-SCOPE FIREWALL, not an algebraic exclusion: inventory
   yields exactly one admitted physical-clock transfer `(T̂², 2a_τ)`. Authority:
   `origin/.../single-clock-physical-clock-inventory-20260617`
   (`scripts/single_clock_physical_clock_admission_inventory_n5_support_2026_06_17.py`,
   PASS=35 FAIL=0; emits `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE`).
5. **[ROP] KMS/APBC thermal circle as a second clock source.** FAILED: KMS/APBC
   only decorates an already-supplied time circle, not a pre-existing second clock.
   Authority: `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16`
   (retained_no_go) + physical-clock-inventory branch.
6. **[ATT] Irreducibility / nonfactorization of the supplied `T̂²` (block01
   R-N5-IRR).** Genuinely built the *actual* supplied object
   `T̂² = ⊗_p diag(1,e^{−2E(p)}) = exp(−2a_τ Ĥ)` (resid ≤ 5.6e-17) — not a proxy.
   WALLED on its own source surface: (a) `T̂²` is MAXIMALLY factorized into `L_s`
   commuting per-mode clocks, so the naive irreducibility theorem is FALSE; (b)
   gauge-redundancy closure FALSIFIED — every mode generator escapes
   `span{I,Ĥ}` (best-fit resid ≈ 0.65) and the factor clocks produce distinct
   durable occupation records no single Ĥ-orbit reproduces (min-dist ≈ 0.40 over
   swept t). Missing supplier = an `(L_s−1)`-param physical-clock-admission ray.
   Runner: `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py`
   (in-tree, PASS=36 FAIL=0).

**N1 verdict:** PASS all three columns. N4 = 12 ≥ 10 (two genuinely attempted,
incl. the previously never-built registration-direction route); N5 = 6 ≥ 5 (incl.
the never-built `T̂²` irreducibility route); N2b = 5 ≥ 4 (incl. the never-built
joint two-gate route). The two historically deferred load-bearing positive routes
(`T̂²` irreducibility, derived registration-direction bridge) are now [ATT], so
the "premature no-go" objection is closed.

---

## Gate clause N2 — Wall-independence (collapse any wall that follows from another)

The no-go must rest on **independent** walls, with each column collapsed to ONE
load-bearing wall; redundant walls that follow from another are demoted to
presentations of the same wall.

| column | the ONE load-bearing wall | walls collapsed INTO it (not independent) |
|---|---|---|
| **N2b** | the **clock-unit wall** — no A_min observable carries a `1/time` unit; `a_τ→c·a_τ` is an exact `ℝ_{>0}` gauge | the Stone/transfer-spectrum route, the Lattice-no-scale route, the Record-no-metric route, the post-record-counts route, and the joint two-gate route all collapse to this single rescaling gauge (each is the same `c`-rescaling viewed through a different gate; R-N2b-JOINT proves the joint gate inherits it verbatim) |
| **N4** | the **single axis-label wall** — the staggered surface's automorphism image is transitive S₄, so every A_min anchor is W/S₄-transported (resid 0) | OS/GNS, durability, registration cone, anomaly/chirality, reality/CPT grading, KMS/APBC, Wilson gauge, crossing-link/cocycle are all *presentations of the one transitive-orbit fact*, not independent walls (the 2026-06-11 no-go states explicitly: BC-asymmetry and registration-direction are alternative presentations of the SAME axis-label supply). The per-axis Z₂ BC datum (E7) does not add a wall — it is the single sub-S₄ enrichment and is itself transportable |
| **N5** | the **factor-exclusion wall** — the supplied `T̂²` is maximally factorized into `L_s` commuting per-mode clocks; no commutant/center forces one orbit | the tensor-locality countermodel, the product-Stone non-uniqueness, the Record-additivity route, and the admission-firewall inventory all collapse to "the source object itself already exhibits the independent factor flows"; R-N5-IRR shows the prior arbitrary-2-qubit proxy is a strictly weaker instance of this one wall |

Cross-column independence: N2b (a *unit*), N4 (a *label*), N5 (a *factor count*)
are genuinely distinct missing data — N2a is FORCED while N2b is open
(intra-clause independence), the N4 axis-label is open while the N4 transfer-
construction *choice* is merely declared, and N5 is open independently of both.
No column's wall is a corollary of another's.

**N2 verdict:** PASS. Each column collapses to exactly one wall; the three walls
are mutually independent.

---

## Gate clause N3 — Hidden-wall scan (surfaces are explicitly-constructed countermodels, not imported physics)

Confirm that every load-bearing surface is an **explicitly constructed finite
countermodel / exact linear-algebra certificate**, not a smuggled physics import
that would constitute a hidden axiom.

- **N2b:** the GATE-S ⊗ GATE-R joint construction is a finite vacuum-normalized
  `H = diag(E_i−E_0)` with `T̂²=exp(−2a_τH)` and a complete-graph reversible `Q`
  with `Qπ=0` — both built from A_min surface data in-runner; the rescaling
  invariance is exact arithmetic (max Δ < 4e-16), no continuum or thermodynamic
  import. (R-N2b-JOINT §2.)
- **N4:** `G_bare` (384 elements) is computed by BFS-solving the diagonal Z₂ sign
  field for each hyperoctahedral relabeling and admitting it only if
  `‖U_g M U_g^T − M‖ < 1e-9`; the enrichment stabilizers E1–E8 are computed, not
  asserted. The LR cone in R-N4-REGDIR is an explicit 5-site TFIM Heisenberg cone;
  the record-accumulation monotone is an explicit graph-distance ball operator.
  No OS reconstruction theorem, no Lorentz/boost content (boost-faith guardrail
  respected), no continuum microcausality is consumed. (R-N4-AUT §2; R-N4-REGDIR
  [BALL]/[DYN]/[PROD].)
- **N5:** the countermodel is the framework's OWN supplied `T̂² = ⊗_p
  diag(1,e^{−2E(p)})`, recomputed from the free staggered dispersion
  `E(p)=arcsinh(√(m²+sin²p))` and the second-quantization functor — not a foreign
  tensor product (this is the explicit correction R-N5-IRR makes over the prior
  proxy branches). The `σ_x⊗σ_x` and `n_0` comparators are constructed in-runner.
  No Lieb-Robinson lightcone (M2) is imported — only equal-time tensor locality
  (M1), which is generator-free. (R-N5-IRR [SURF]/[GAUGE]/[CONTENT].)

The one place physics could be smuggled is the staggered-Dirac *surface itself*;
but that surface is the retained (R-RP2)/(R-SC2)/(R-CL3) reconstruction object,
and the no-go's claim is explicitly ABOUT that retained surface (see N5-check and
the scope statement), not an importation of a new axiom.

**N3 verdict:** PASS. Every load-bearing surface is an explicitly constructed
finite countermodel verified by exact arithmetic in an absorbed runner; no hidden
imported-physics wall.

---

## Gate clause N4-check — residual matching for every cited witness no-go

For each cited witness no-go, confirm its open residual MATCHES (is the same open
gate as) this section's residual — i.e. no cited authority secretly discharges a
clause this note leaves open, and no cited authority opens a *different* residual
the note fails to carry.

| cited witness | clause it owns | its open residual | matches this note's residual? |
|---|---|---|---|
| `..._UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go) | N2/N4/N5 checklist supplier | Stone is transfer-/τ-relative; no-second-clock needs a SEPARATE axis/transfer-uniqueness premise; τ is an extra premise | YES — exactly the N2b unit-gauge, N4 axis-label, N5 factor walls below |
| `..._RECORD_DURABILITY_..._2026-06-11` (retained_no_go) | N4 axis-label only | axis label underivable; minimal supplier = one per-axis Z₂ BC-asymmetry datum / registration-direction bridge; **N2 and N5 explicitly OUT OF SCOPE** | YES for N4; the note must NOT borrow it for N2b/N5 (it owns neither) — respected |
| `..._KMS_APBC_AXIS_SUPPLIER_..._2026-06-16` (retained_no_go) | N4 (KMS/APBC route) | APBC is axis-covariant; per-axis BC asymmetry is a separate undischarged bridge; does NOT exclude factor clocks (N5) | YES for N4; note must NOT borrow it for N5 — respected |
| `MINIMAL_AXIOMS_2026-06-05` | A_min content boundary | Lattice/Quantum/Record supply no dynamics, no time metric, no boundary datum, no occupancy rule; dynamics/arrow/record-production are EXPLICIT OPEN GATES | YES — the single emergent-dynamics open gate all three columns funnel to (N8) |
| n5-factor-boundary branch runner (PASS=34) | N5 | factor exclusion fails on tensor surface; escape = irreducibility/admission/gauge theorem | YES — R-N5-IRR closes the irreducibility/gauge sub-routes as FALSE, leaving the admission ray, matching |
| physical-clock-inventory branch runner (PASS=35) | N5 admission half | `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE`; residual = `T̂²` irreducibility | YES — R-N5-IRR resolves that exact relocation on the source object |
| s4-transportable branch runner (PASS=22) | N4 axis-label | S₄-transitive; residual = emergent-dynamics open gate via native-on-Z₃ | YES — identical gate |
| apbc-axis-bridge branch runner (PASS=21) | N4 axis-label (conditional support) | datum NOT derived; B-AXIS stays live; residual on the datum supplier | YES — the supplier is the same boundary-condition open gate |

No cited witness discharges a clause the note leaves open; no witness opens a
residual the note omits. The four block01 [ATT] runners each terminate on a wall
whose residual is one of these same gates (N2b → clock/rate gate; N4 → boundary-
condition / record-production-dynamics gate; N5 → physical-clock-admission ray),
all of which are sub-cases of the single `MINIMAL_AXIOMS_2026-06-05` emergent-
dynamics open gate (see N8).

**N4-check verdict:** PASS. Every cited witness's residual matches; scope
boundaries of the N4-only / KMS-only witnesses are respected (not borrowed into
N2b/N5).

---

## Gate clause N5-check — rhetoric audit: confine exact-zero claims to even cubic-symmetric staggered blocks (the odd-L falsifier)

Audit every "residual 0 / exactly invariant / exact" claim for over-reach beyond
the surface on which it is computed.

- **The exact-zero W/S₄ facts are bounded to EVEN cubic-symmetric staggered-Dirac
  blocks.** The odd-L falsifier is explicit and must be carried verbatim: at
  `L=(3,3,3,3)` the signed exchange does NOT preserve the hop,
  `‖W M Wᵀ − M‖ = 6.000` (R-N4-AUT [SCOPE]; matches the s4-transportable branch
  odd-L resid 6 exactly); at even `L=(4,4,4,4)` the residual is 0. The even-extent
  condition is the standard staggered-fermion requirement (the periodic η-phase
  closes consistently across the wrap iff the extent is even). **Every N4 exact-
  zero (`W M Wᵀ=M`, `W ε Wᵀ=ε`, the 384-element `G_bare`, the E7 transport
  `W₀₁ M_appp W₀₁ᵀ=M_pappp`) is asserted ONLY on even cubic-symmetric blocks.**
- **N5 exact-zeros are surface-specific, not surface-universal.** The
  `T̂²=⊗_p diag(1,e^{−2E(p)})` factorization (resid ≤ 5.6e-17) and the commuting
  per-mode factors (resid 0) are exact properties of the supplied free-sector
  staggered transfer; the "maximally factorized" claim is confined to that
  object. The escapes-`span{I,Ĥ}` and distinct-record claims are inequalities
  (resid ≈ 0.65, min-dist ≈ 0.40), not exact zeros, and need no scope guard.
- **N2b exact-zeros are gauge-invariance residuals, surface-agnostic in form but
  claimed only for the finite construction.** `T̂²`, `K`, `T̂²⊗K` invariant
  (max Δ < 4e-16) is asserted for the built finite carrier under
  `c∈{0.5,1.3,2.0,5.0}`; the *structural* "no `1/time` observable" reason is the
  general statement and is phrased as a property of the A_min observable algebra,
  not an exact-zero.
- **No exact-zero is stated as framework-wide.** The note must say "on the even
  cubic-symmetric staggered-Dirac surface" wherever it states `resid 0`, and must
  NOT phrase any W/S₄ exact-zero as an impossibility on all lattices/dimensions.

**N5-check verdict:** PASS provided the consolidated note carries the even-extent
qualifier on every W/S₄ exact-zero and exhibits the odd-L `resid 6` falsifier.
This is a binding requirement on the prose, recorded here.

---

## Gate clause N6 — Partial-closure path scan (every named supplier listed WITHOUT calling it a new-axiom requirement; the import-retirement path)

Under the hard rule (A_min = Lattice + Quantum + Record; no new axiom/primitive),
a no-go is only honest if its escape suppliers are listed as **open derivation
targets / import-retirement paths**, never as "you must add an axiom." Confirm
each named supplier is a thing that *could* be derived from A_min + retained
surface in principle (or admitted by an explicit source decision), not a demanded
primitive.

| column | named supplier(s) (the partial-closure path) | listed as new-axiom requirement? |
|---|---|---|
| **N2b** | a separate supplied **clock/rate bridge** carrying an actual `1/time` unit (a metric-scale supplier) | NO — listed as an open downstream bridge any unitful claim must *identify*; could be a derived record-rate normalization, not an axiom |
| **N4** | one per-axis Z₂ **BC-asymmetry datum** OR a **declared/derived registration-direction bridge** tying realized record order to one axis (record-production dynamics layer) | NO — both are open derivation targets; A_min withholds the boundary datum as an EXPLICIT OPEN GATE, so deriving it from a record-production layer is import-retirement, not a new axiom. (E7 shows the supplier *shape*; it is not demanded as a primitive) |
| **N5** | exactly one of: an **irreducibility/nonfactorization** theorem (closed-as-FALSE by R-N5-IRR), a **physical-clock-admission** datum (an `(L_s−1)`-param chosen positive ray / record-order rule), or a **gauge/redundancy** theorem (FALSIFIED by R-N5-IRR) | NO — the surviving supplier (admission ray) is an open source decision / derivation target; the note explicitly does NOT demand it as an axiom (the firewall framing narrows the *claim*, it does not add a primitive) |

Common import-retirement path: all three suppliers reduce to data the
**emergent-dynamics OPEN GATE** of `MINIMAL_AXIOMS_2026-06-05` would supply if a
record-production dynamics layer were derived (no dynamics/time metric/boundary
datum currently in A_min). None is phrased as "add an axiom"; each is "derive or
explicitly admit X from the existing surface."

**N6 verdict:** PASS. Every named supplier is an open derivation / admission
target on the import-retirement path; none is a demanded new axiom or primitive
(critical under the no-new-axiom hard rule).

---

## Gate clause N7 — Steelman per clause (strongest hostile counter-argument, then why block01's fresh attempts already falsified it)

For each column, the strongest pro-derivation hostile argument, then the in-cycle
fresh attempt that already falsified it.

- **N2b steelman:** "Each rate gate alone is τ-relative, but two gates pinned to
  the SAME physical clock (one clock driving both the transfer step and the
  record stream) jointly over-determine the system and must fix `a_τ`."
  **Falsified by R-N2b-JOINT:** the joint construction was genuinely built under
  exactly that strongest single-clock coupling (`K=exp((2a_τ)Q)`), and the
  rescaling `a_τ→c·a_τ, H→H/c, Q→Q/c` is an EXACT `ℝ_{>0}` gauge — `T̂²`, `K`,
  `T̂²⊗K` all invariant (max Δ < 4e-16). The gates fix only the dimensionless
  `m_gap·relaxation-time` ratio; **no A_min observable returns a `1/time`
  number**, so no joint coupling of this type can ever pin the unit.
- **N4 steelman (two prongs):** (a) "The W/S₄ obstruction is an artifact of a
  too-poor surface; a *richer* A_min enrichment will have a stabilizer that fixes
  one axis." (b) "Record-PRODUCTION is dynamical, not a static structure — a
  record-accumulation / causal-cone monotone singles out the evolution direction
  intrinsically." **Falsified by R-N4-AUT and R-N4-REGDIR:** (a) the *entire*
  384-element `G_bare` was computed and every A_min enrichment E1–E8 has a joint
  stabilizer that is full S₄ or trivial (a symmetric, non-selecting W-break); the
  only one-axis-selecting enrichment (E7) is a supplied BC datum outside A_min and
  is itself S₄-transportable — the orbit is exhaustive, not an artifact. (b) the
  A_min record monotone is a direction-free *ball* (W-invariant, resid 0); a real
  LR cone needs a supplied generator whose W-conjugate gives an identical cone
  (circular, Δ 7e-16); record-production CPTP/POVM are W-covariant (resid 0) and
  break W only with a supplied asymmetric pointer datum (break 3.44) that Record
  explicitly withholds.
- **N5 steelman:** "The supplied `T̂²` is a *single physical* transfer; either it
  is irreducible (no nontrivial commuting factor split) or any factor split is
  gauge (Record cannot see it), so a second clock is excluded on the source
  surface." **Falsified by R-N5-IRR:** building the actual
  `T̂²=⊗_p diag(1,e^{−2E(p)})` shows it is *maximally* factorized into `L_s`
  commuting per-mode clocks (irreducibility FALSE), and each mode generator
  escapes `span{I,Ĥ}` (resid ≈ 0.65) and produces a distinct durable occupation
  record no single Ĥ-orbit reproduces (min-dist ≈ 0.40, Record-visible) —
  gauge-redundancy FALSIFIED. The exclusion needs a physical-clock-admission ray
  A_min does not supply.

**N7 verdict:** PASS. Each column's strongest hostile counter-argument was
genuinely built in block01 and falsified by computation — not waved off. The two
historically "live-positive but never built" steelman prongs (N5 irreducibility,
N4 registration-direction) are precisely the ones now executed, which is what
upgrades the gate from premature to shippable.

---

## Gate clause N8 — Cross-cycle echo (all clauses funnel to the same emergent-dynamics open gate)

Confirm the three independent walls relocate their residual to ONE shared open
gate, so the no-go is a single coherent obstruction, not three unrelated dead ends.

- **N2b** residual → the absolute clock unit `a_τ` needs a supplied **clock/rate
  bridge** carrying a `1/time` unit. A_min supplies no dynamics and no metric
  scale.
- **N4** residual → the axis label needs a supplied **boundary-condition asymmetry
  / registration-direction** datum from a **record-production dynamics** layer.
  A_min supplies no dynamics, no causal cone, no arrow, no boundary datum.
- **N5** residual → a **physical-clock-admission ray** (a record-order rule
  selecting one factor flow). A_min supplies no occupancy rule and no dynamics.

All three are the *same* missing thing viewed from three sides: **the emergent-
dynamics OPEN GATE of `MINIMAL_AXIOMS_2026-06-05`** — Lattice/Quantum/Record
supply no dynamics, no time metric, no record-production dynamics, no arrow, no
boundary datum, no occupancy rule (the explicit open-gate list). The native-on-Z₃
framing (time = parameter of a one-parameter group/semigroup over the fixed
spatial Hilbert space `⊗_{x∈Z³} C²`, not a 4th lattice coordinate) is the single
dissolving framing that makes the which-of-4-axes question disappear, but it
RELOCATES rather than derives: the generator, its rate/unit, and its uniqueness
all land back in this one gate (orientation is separately carried by the past
hypothesis). Independently, every absorbed in-flight branch — apbc-axis-bridge,
axis-nogo-self-contained, consumer-firewall, blocked-time-unit-split,
n5-factor-boundary, physical-clock-inventory, s4-transportable,
s3-axis-identity-convention — funnels to this same gate. The convergence is the
cross-cycle echo.

**N8 verdict:** PASS. N2b + N4 + N5 funnel to the single emergent-dynamics open
gate of the minimal axioms; the obstruction is one coherent wall with three faces.

---

## Honest scope statement (binding on the shipped no_go)

This is a **no-go about the RETAINED SURFACE**, not a framework-wide impossibility
proof. Precisely:

1. **Surface-specific.** The exact-zero W/S₄ transport facts and the maximal
   `T̂²` factorization hold on the **even cubic-symmetric staggered-Dirac
   reconstruction surface** ((R-RP2)/(R-SC2)/(R-CL3) object). On **odd** extents
   the signed exchange is not even a symmetry (`resid 6`); the claims are scoped
   to even cubic-symmetric blocks and the odd-L falsifier is exhibited.
2. **Not an impossibility proof.** The note proves that **A_min + this retained
   surface** does not *derive* N2b (absolute unit), N4 (axis label), or N5
   (factor-clock exclusion); it does NOT prove no extension of the framework could
   ever supply them. Each named supplier (clock/rate bridge; BC-asymmetry /
   registration-direction bridge; physical-clock-admission ray) is an open
   derivation/admission target, not a refuted object.
3. **Dimension-selection off-surface remains axiomatic.** The theorem lives on the
   `Z³+1` 4-torus; selecting the spacetime dimension off this surface is NOT
   addressed and remains an axiomatic input. The obstruction does not bear on it.
4. **Conditional-parent caveat.** The keystone parent
   (`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`,
   audited_conditional, downstream fanout 959) is itself conditional; this gate
   recomputes every load-bearing fact in-runner rather than citing it (or the
   unaudited finite-speed cone note or the downstream ANOMALY_FORCES_TIME
   consumer) blind. Any wall ultimately resting on the parent is conditional until
   the audit lane adjudicates the parent.

With the even-extent qualifier on every exact-zero, the named-supplier-as-open-
target framing on every escape, and the off-surface dimension-selection carve-out,
the negative claim clears N1–N8 per clause and is shippable as a `no_go` (intended
classification; independent audit lane is sole status authority).
