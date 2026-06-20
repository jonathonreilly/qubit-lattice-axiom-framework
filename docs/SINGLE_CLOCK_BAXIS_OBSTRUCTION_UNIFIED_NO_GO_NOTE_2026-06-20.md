# Single-Clock B-AXIS Obstruction — Unified No-Go Note (Block 02)

**Date:** 2026-06-20
**Branch:** `physics-loop/single-clock-baxis-wall-block02-20260620` (stacked on block01)
**Type:** no_go (negative_route_pruning) + exact-support pin (N2a)
**Claim type:** no_go
**Status:** consolidated no-go / exact negative boundary on the retained
even-extent staggered-Dirac surface; B-AXIS (N2b/N4/N5) not derivable from A_min;
all residuals relocate to the emergent-dynamics open gate; not a new axiom;
proposal_allowed=false; bare_retained_allowed=false;
audit_required_before_effective_retained=true; independent audit lane is sole
status authority.
**No new axiom / no new primitive.** A_min = Lattice + Quantum + Record only.

**Boundary flags:** B_AXIS_DERIVED = FALSE; B_AXIS_CONSUMED_AS_PREMISE = TRUE;
SECOND_PHYSICAL_CLOCK_EXCLUDED = FALSE; AUDIT_LEDGER_WRITTEN = FALSE;
AUDIT_VERDICT_APPLIED = FALSE; NEW_AXIOM_ADDED = FALSE.

**Consolidated verification runner:**
`scripts/single_clock_baxis_obstruction_unified_2026_06_20.py`
(TOTAL **PASS=32 FAIL=0**; cache
`logs/runner-cache/single_clock_baxis_obstruction_unified_2026_06_20.txt`),
which recomputes the headline N4 / N5 / N2b / N2a facts in-tree plus the
source-discipline `[SRC]` and even-extent `[SCOPE]` guards. The four absorbed
block01 clause runners (aggregate PASS=91 FAIL=0) are indexed in Section 12.

---

## 1. Purpose, target, and status

This note consolidates the Block 02 B-AXIS obstruction into one coherent
`no_go`. The **target keystone** is
`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
(audited_conditional, bounded_theorem, downstream fanout 959 / Class A). Its only
undischarged edge is the **B-AXIS** missing-bridge premise. This note shows that
B-AXIS — decomposed into the three clauses N2 / N4 / N5 — is **not derivable from
A_min** on the retained surface, names the minimal supplier shape for each clause,
and relocates all three residuals to a single emergent-dynamics open gate.

This is a **no-go about the retained surface**, NOT a framework-wide impossibility
proof, and NOT a closure of B-AXIS. The note authors no audit grade, sets no
publication status, and edits no audit-lane file. The independent audit lane is the
sole status authority. `proposal_allowed=false`; `bare_retained_allowed=false`;
`audit_required_before_effective_retained=true`.

---

## 2. B-AXIS three-clause decomposition (N2 / N4 / N5) and per-clause retirement path

The B-AXIS premise of the single-clock keystone is not one opaque assumption. It
decomposes into exactly three premise clauses, each owning a distinct missing-bridge
question. The clause labels N2/N4/N5 are inherited verbatim from the governing fence
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go): that note's
N2/N4/N5 checklist clauses *became* B-AXIS.1/.2/.3, and it is cited here as the
governing boundary whose scope each clause inherits — Stone uniqueness held there only
**transfer-relative and τ-relative**, which is precisely why none of the three clauses
is auto-discharged by the spectral core.

| clause | B-AXIS slot | question | current honest status | retirement path (named supplier shape, NOT a closure) |
|---|---|---|---|---|
| **N2** | B-AXIS.1 | one supplied blocked time-step `2a_τ` | **split**: N2a exact-support-FORCED; N2b open | N2a needs nothing further (forced by the supplied `T̂²`). N2b retires only by a supplied **clock/rate bridge** carrying units of `1/time`. |
| **N4** | B-AXIS.2 | one declared evolution axis / RP-transfer construction (which of 4 Euclidean directions is time) | **open** (declared premise) | retires by a **non-transportable registration-direction bridge** OR a declared **per-axis Z₂ BC-asymmetry datum**, derived from A_min — neither exists. |
| **N5** | B-AXIS.3 | no independent commuting transfer factor admitted as a second clock | **open** (declared premise) | retires by a **`T̂²` irreducibility/nonfactorization theorem**, OR a **physical-clock-admission ray** `(L_s−1)`-param, OR a **gauge/redundancy theorem** — none supplied by A_min. |

**N2 sub-split (governing detail).** N2 must never again be relisted as a single import:
- **N2a (exact-support, FORCED — NOT a wall):** for the supplied two-step staggered
  transfer `T̂² = exp(−2 a_τ H)`, the aligned reconstruction
  `H_block = −(1/(2a_τ)) log(T̂²/M_T)` is forced internally by the retained two-step
  blocked-time normalization bridge. The one-step denominator `1/a_τ` is a
  falsifier that doubles every non-vacuum energy (`H_wrong = 2·H_block`). This is a
  source-side consequence of the already-retained `T̂²`, not a new import.
- **N2b (open / no-go):** the *absolute* physical clock unit `a_τ` (a number carrying
  units of time) is NOT derived. This is the only walling half of N2.

Each clause's retirement path names a **supplier shape**, never a new axiom. Per the
no-new-axiom hard rule, a clause that could only close by adding a primitive is
`infeasible`; every path above is an A_min-internal supplier that is simply *absent*
on the retained surface, which is exactly the no-go content.

---

## 3. Non-vacuity witnesses — the premises exclude realizable things (load-bearing, not cosmetic)

A premise is cosmetic if dropping it changes nothing realizable. We exhibit explicit,
machine-verified realizable objects that the B-AXIS premises *exclude*. All are
recomputed in-tree (Section 12); none is cited blind.

### Witness W-1 — [C-2CLK]: a genuine two-commuting-tensor-factor transfer with multi-dimensional generator span (kills "N5 is vacuous")

If N5 (no independent commuting transfer factor) were vacuous, A_min + equal-time
tensor locality would already force a single one-parameter clock orbit. It does not.
The supplied two-step transfer is itself **maximally factorized**:

`T̂² = ⊗_p diag(1, e^{−2E(p)})`,  `E(p) = arcsinh(√(m²+sin²p))`,

a tensor product of `L_s` commuting positive per-mode factor clocks. The
recomputation (consolidated runner `[N5]` block, and block01
`single_clock_n5_irreducibility_factor_clock_2026_06_20.py`, PASS=36/0) shows:
- the per-mode factors are positive-definite and **commute pairwise** (max comm
  resid = 0.00e+00);
- the **factor-generator tangent span has dimension `L_s`** (rank = 3 at `L_s = 3`) —
  a genuinely **multi-parameter abelian generator span**, not a reparametrized single
  orbit;
- the relative factor flow is **not gauge** (a single-mode generator `n_0` escapes
  `span{I,Ĥ}`, best-fit residual ≈ 1.3 on the runner surface; on the block01 surface
  ≈ 0.65), and the factor clocks produce **distinct durable occupation records** that
  no swept single-clock time reproduces (min-dist ≈ 0.40), so the second clock is
  **Record-visible**, hence realizable, hence genuinely excluded by the N5 premise.

The companion 2-qubit form (T_A⊗I, I⊗T_B commute resid 0, rank-2 span, U_A(1)⊗I off
the diagonal one-clock orbit min_gap 0.292) is the canonical [C-2CLK] countermodel of
the n5-factor-boundary branch; we cite it and do **not** rebuild it. Either form proves
the same thing: **a second commuting clock is realizable on the A_min surface, so N5 is
load-bearing.**

### Witness W-2 — [τ-RESCALE]: `2a_τ → 2c·a_τ` gives identical dimensionless transfer data (kills "N2b is vacuous")

If N2b (absolute clock unit) were vacuous, the surface would already pin `a_τ`. It does
not. The joint rescaling `a_τ → c·a_τ`, `H → H/c`, `Q → Q/c` is an **exact
one-parameter gauge** of every A_min observable (consolidated runner `[N2]` block, and
block01 `single_clock_n2b_joint_clock_unit_check_2026_06_20.py`, PASS=18/0):
- `T̂²` invariant, record-block kernel `K = exp(2a_τ Q)` invariant, full per-block
  evolution `T̂² ⊗ K` invariant (max Δ over `c ∈ {0.5,1.3,2,5}` < 4e-16);
- the dimensionless datum (`gap · a_τ`, equivalently `m_gap · relaxation-time`) is
  `c`-invariant, while every dimensionful number rescales;
- a **malformed** rescaling (`a_τ` scaled, `Q` not) MOVES a record-count datum
  (move ≈ 1.57 / 0.50), proving the gauge zeros are real computed facts, not vacuous
  identities.

So a whole one-parameter family of distinct absolute clock units yields *identical*
dimensionless transfer data: the absolute unit is realizable-but-unfixed, which is
exactly what the N2b premise must supply. **N2b is load-bearing.**

### Why N4 is non-vacuous

N4 is load-bearing by the dual fact: the signed exchange unitary
`W = P_{τ↔1}·diag((−1)^{x_τ x_1})`, upgraded to **S₄-transitivity** over all four
Euclidean axes, maps every candidate temporal axis onto a spatial axis with residual 0
(consolidated runner `[N4]` block: hop resid 0, adjacent exchanges (0,1),(1,2),(2,3)
preserve the hop ⇒ transitive S₄; absorbed from the S4-transportable branch and
recomputed in block01's `single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`,
`|G_bare| = 384`, axis image = transitive S₄, PASS=17/0). A whole orbit of four axis
labels gives identical surface data; the axis label is realizable-but-unfixed.
**N4 is load-bearing.**

**Conclusion of Section 3.** N2/N4/N5 each exclude an explicitly realizable object
(a commuting second clock; a rescaled clock unit; an exchange-equivalent axis label).
None is cosmetic. The B-AXIS premise carries genuine content.

---

## 4. N2 treatment — N2a exact-support FORCED + N2b NO-GO

**B-AXIS clause:** B-AXIS.1 = N2 — "one supplied blocked time step `2 a_τ`."

### N2a — exact-support FORCED (the `1/(2 a_τ)` denominator is supplied)

For the supplied two-step staggered transfer `T̂² = exp(−2 a_τ H)` (`H ≥ 0`,
vacuum-normalized), the aligned spectral reconstruction
`H_block = −(1/(2 a_τ)) · log(T̂²/M_T) = Ĥ − E₀` is FORCED internally by the retained
two-step blocked-time normalization bridge. The `1/(2 a_τ)` denominator is a
source-side consequence of the already-retained `T̂²` — **not a new import, axiom, or
primitive**.

**The factor-two falsifier (discriminating certificate).** The wrong one-step
denominator `1/a_τ` applied to the SAME `T̂²` doubles every non-vacuum energy:
`H_wrong = −(1/a_τ) log(T̂²/M_T) = 2·H_block`. Only `1/(2 a_τ)` recovers the correct
generator; `1/a_τ` is exactly excluded. Recomputed in-tree: consolidated runner
`[N2]` block (reconstruction resid 0; falsifier `H_wrong = 2H` resid 0) and block01
`single_clock_n2b_joint_clock_unit_check_2026_06_20.py` block [A] (resid 0).

**Absorbed (cited, not rebuilt):** the full N2a exact-support result is owned by the
blocked-time-unit-split branch
`origin/physics-loop/single-clock-blocked-time-unit-split-20260617`
(`scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py`, PASS=35),
citing the two-step normalization bridge
`AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05`.

**Bottom line for N2a:** SUPPLIED, not a wall. N2 must never again be relisted as a
single opaque import — the internal denominator is forced exact-support; only the
absolute unit walls.

### N2b — NO-GO (the absolute clock unit `a_τ` is underivable)

The absolute physical clock unit / time metric carried by `a_τ` is NOT derivable from
A_min (Lattice + Quantum + Record), nor from post-record count histories, nor from the
transfer spectrum, nor from the two retained rate gates jointly. The simultaneous
rescaling `a_τ → c·a_τ, H → H/c, Q → Q/c (c > 0)` is an **EXACT 1-parameter gauge** of
the joint construction: `T̂²`, the record kernel `K`, and the full joint per-block
evolution `T̂² ⊗ K` are all invariant. The two retained rate gates fix only
DIMENSIONLESS ratios; **no A_min observable carries `1/time` units**, so no datum can
fix `c`.

**Absorbed runner — R-N2b-JOINT (in-tree).** Block01
`single_clock_n2b_joint_clock_unit_check_2026_06_20.py` (PASS=18) recomputes:

| block | check | residual |
|---|---|---|
| [A] | `1/(2 a_τ)` reconstruction recovers `H` (N2a forced) | `0.0e+00` |
| [B] | `T̂²` invariant under joint rescaling | max Δ `5.6e-17` |
| [B] | record-block kernel `K = exp(2 a_τ Q)` invariant | max Δ `3.3e-16` |
| [B] | FULL joint `T̂² ⊗ K` invariant → `a_τ` is gauge | max Δ `3.3e-16` |
| [C] | dimensionless ratio `m_gap / relax` invariant (the fixed datum) | `0.400000` |
| [D] | record COUNT-per-block datum clock-free under CORRECT joint rescaling | max dev `2.2e-16` |
| [D] | MALFORMED rescaling (`a_τ` scaled, `Q` NOT) MOVES the count datum | `0.50` |

R-N2b-JOINT was a GENUINE fresh derivation attempt: it built BOTH retained rate
gates (GATE-S spectrum-condition normalization; GATE-R record clock/rate gate) under
the strongest possible single-clock coupling — ONE clock driving both the transfer
step and the record stream (`K = exp((2 a_τ) Q)`) — precisely the case most likely to
over-determine `a_τ`. **Outcome: WALLED (ratio-only).** Sharpened structural reason
(stronger than the single-gate argument): **no A_min observable returns a unit-bearing
`1/time` number**, so no gate of this type can EVER pin the unit. The malformed-
rescaling discriminator (count datum moves by `0.50`) proves the invariance is a real
computed gauge, not a vacuous identity.

**Where the residual relocates.** N2b relocates to the **emergent-dynamics /
clock-rate OPEN GATE** of `MINIMAL_AXIOMS_2026-06-05`: any downstream physical-rate or
unitful (mass-in-seconds) claim must identify a SEPARATE supplied clock/rate bridge
carrying an actual `1/time` unit. No retained framework row supplies one. B-AXIS.1
stays LIVE on its N2b half.

**Authorities (cited; load-bearing facts recomputed):**
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go) — Stone is
transfer-/τ-relative; `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06` — finite record
histories fix order+counts, not seconds; `MINIMAL_AXIOMS_2026-06-05` — Lattice supplies
no metric scale, Record supplies no time metric.

---

## 5. N4 axis-label core obstruction (W upgraded to S₄-transitivity)

**B-AXIS clause:** B-AXIS.2 = N4 (axis-label / evolution-axis selection): which of the
four Euclidean directions carries the RP/transfer construction — derived or declared?

### 5.1 The signed exchange unitary W, upgraded to S₄-transitivity

The staggered-Dirac surface carries the signed time↔space exchange unitary
`W = W_{τ,1} = P_{τ↔1} · diag((−1)^{x_τ x_1})`. The plain unsigned swap is **not** a
symmetry (residual > 1); only the *signed* W conjugates the staggered hop `M_KS` to
itself, `W M_KS Wᵀ = M_KS` (residual 0, even block; consolidated runner `[N4]`).

**Upgrade to the full group (recomputed in-tree).** W is one element of the entire
bare-surface automorphism group. The block01 runner
`single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` enumerates the signed
hyperoctahedral group B₄ (24 axis-permutations × 16 per-axis reflections = 384) and
admits `g` iff `‖U_g M U_gᵀ − M‖ < 1e-9`. Result: **`|G_bare| = 384`**; axis-
permutation image = **all of S₄, acting transitively** (orbit of axis 0 is
`{0,1,2,3}`). The consolidated runner independently confirms transitivity via the
adjacent exchanges `(0,1),(1,2),(2,3)` each preserving the hop (resid 0). Transitive ⇒
any axis-selector built from W-invariant structure is transportable onto any other axis
⇒ the time axis cannot be derived from the surface, only declared. Authority for the S₄
upgrade: `SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17`
(retained_no_go); the S₄ fact is recomputed in-tree, not taken as a citation edge.

### 5.2 The corrected R-N4-AUT enrichment-stabilizer result (steelman falsified)

The block01 steelman R-N4-AUT searched for **any** A_min-available surface enrichment
whose automorphism stabilizer drops below S₄ and **fixes exactly one axis** (a
non-transportable axis-selector), without presupposing the Hamiltonian. Eight
enrichments E1–E8 enumerated; selector criterion = stabilizer fixes exactly one axis
AND acts transitively on the other three (S₃-fixing-one).

| id | enrichment | A_min source | joint-stab class | selects axis? | A_min? |
|----|-----------|--------------|------------------|---------------|--------|
| E1 | reality/CPT parity grading ε=(−1)^{Σx} | Quantum | S₄-isotropic | None | yes |
| E2 | cubic adjacency Laplacian | Lattice | **trivial-joint (symmetric W-break)** | None | yes |
| E3 | staggered η hop-sector family | staggered structure | S₄-isotropic | None | yes |
| E4 | STW crossing-link RP invariant P_a | crossing-link surface | S₄-isotropic | None | yes |
| E5 | η-curvature 2-cocycle | staggered phase curvature | S₄-isotropic | None | yes |
| E6 | Record additive scalar readout | Record | S₄-isotropic | None | yes |
| **E7** | **per-axis Z₂ BC datum (A,P,P,P)** | **boundary datum (NOT A_min)** | **one-axis-selecting S₃** | **axis 0** | **NO** |
| E8 | face-diagonal-enriched cubic graph | richer Lattice graph | **trivial-joint (symmetric W-break)** | None | yes |

**Corrected headline:** *every A_min enrichment's joint stabilizer with the staggered
hop is either all of S₄ (isotropic) or trivial (a symmetric, non-axis-selecting break
of W); NO A_min enrichment has a one-axis-selecting (S₃) stabilizer.* The only
one-axis-selecting enrichment is the per-axis Z₂ BC datum (E7), which is
S₄-transportable and outside A_min. This is stronger than "every A_min enrichment is
S₄-isotropic": E2 (cubic Laplacian) and E8 (face-diagonal graph) **do break W** — but
axis-SYMMETRICALLY (trivial joint stabilizer fixes all four axes), so they single out
no axis. The consolidated runner `[N4]` independently confirms: the signed W keeps the
hop but breaks the Laplacian (resid ≈ 22.6), while the plain swap keeps the Laplacian
but breaks the hop (resid ≈ 11.3) — no element keeps both, the W-break is genuine and
axis-symmetric. Recomputed in-tree: R-N4-AUT TOTAL PASS=17 FAIL=0.

### 5.3 The four transport witnesses (no W-invariant anchor selects the axis)

Every previously proposed axis-anchor is exactly transported across W-equivalent axes
(or is circular). These are CITED from the retained no-go
`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11`
(retained_no_go) and the in-flight branch runners — **not rebuilt here**:

1. **OS/GNS reconstruction.** W transports the OS reflection, covariance, one-particle
   kernel (`W M⁻¹ Wᵀ = M⁻¹`, resid ~2.7e-15), half-space kernels, spectra, positivity
   to `x_1`. The OS construction is built *after* the axis is chosen. *Cited:* branch
   `single-clock-axis-nogo-self-contained-20260617`
   `scripts/single_clock_axis_selection_check_2026_06_11.py` block [RT-RP].
2. **Record durability.** Durability = operator-order monotonicity, unitary-transport
   invariant (Δ 8.9e-16); Record supplies no time metric. *Cited:* same runner block
   [RT-REC]; `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`.
3. **Finite-speed registration cone (circularity).** Any cone whose evolution
   generator and clock window are already supplied is downstream of B-AXIS, so citing
   it consumes B-AXIS to derive B-AXIS. Slice transports `W_sl D^(1) W_slᵀ = D^(τ)`
   (resid 0). *Cited:* same runner block [RT-REC] **and recomputed** by block01
   R-N4-REGDIR (`single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`,
   PASS=20): the A_min record-accumulation monotone is a W-invariant reflection-
   symmetric **ball, not a cone**; a real LR cone needs a supplied generator whose
   W-conjugate yields an identical cone (Δ 7e-16, circular).
4. **Anomaly / chirality (count-not-label firewall).** `ε(x) = (−1)^{Σx_μ}` is
   W-invariant (resid 0) and `{D_hop, ε} = 0` is W-preserved (resid 0); a count-only
   rule constrains the *number* of temporal directions but not a *label*. *Cited:*
   2026-06-11 retained_no_go route B; branch block [RT-ANOM]. (NOT cited from the
   downstream ANOMALY_FORCES_TIME consumer — the count-not-label fact is recomputed.)

### 5.4 Pruned-supplier enumeration

| candidate axis-supplier | outcome | mechanism | authority |
|---|---|---|---|
| OS/GNS reconstruction privileges τ | PRUNED | W transports reflection/kernel/spectra to x₁ (resid 0) | 2026-06-11 retained_no_go + branch [RT-RP] |
| Record durability as physical axis | PRUNED | unitary-invariant operator-order monotonicity | 2026-06-11 retained_no_go + branch [RT-REC] |
| Finite-speed registration cone / CAP-K | PRUNED (circular) | cone consuming a supplied generator is downstream of B-AXIS; A_min monotone is a ball | 2026-06-11 retained_no_go + R-N4-REGDIR |
| Anomaly/chirality identifies the axis | PRUNED | ε W-invariant, count-not-label firewall | 2026-06-11 retained_no_go (route B) |
| KMS/APBC thermal antiperiodicity | PRUNED | exchange-covariant: W maps APBC-τ → APBC-x₁ exactly | **retained_no_go** `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16` |
| Wilson temporal-gauge / plaquette | PRUNED (labeled choice) | singles an axis only via labeled choice U₀=1 (transportable) | s4-transportable retained_no_go |
| Quantum tensor factor as a time slot | PRUNED (reduces to OS) | equal-time tensor factor carries no axis; reduces to OS package | 2026-06-11 retained_no_go + Lieb-Robinson equal-time tensor locality note |
| reality/CPT grading ε as selector | PRUNED (W-inert) | W ε Wᵀ = ε (resid 0); stabilizer image = full S₄ | N4-AUT E1 (in-tree) |
| crossing-link RP invariant + η-curvature cocycle | PRUNED (isotropic) | P_a=+1 all axes; cocycle=−1 all planes | N4-AUT E4/E5 (in-tree) |
| cubic Laplacian / face-diagonal graph | PRUNED (symmetric W-break) | trivial joint stabilizer: W broken but axis-symmetrically | N4-AUT E2/E8 (in-tree) |
| record-production direction (LR cone) | PRUNED (relocated) | production CPTP + POVM W-covariant; breaks W only with a supplied asymmetric pointer datum | R-N4-REGDIR (in-tree) |
| **per-axis Z₂ BC-asymmetry datum** | **the sole selector** | breaks W exactly; S₃ stabilizer — **but S₄-transportable + outside A_min** | 2026-06-11 sharpened pin + s4 retained_no_go + N4-AUT E7 |

### 5.5 The N4 sharpened pin (positive boundary) and its undischarged datum

The exact negative boundary of N4: the **minimal** axis-selecting input is **precisely
one per-axis Z₂ boundary-condition asymmetry datum** (e.g. `bc=(A,P,P,P)`). Four legs
pin it (from the 2026-06-11 retained_no_go sharpened pin + the apbc-axis-bridge
companion, `frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py` PASS=21):
- **(A)** all-PBC surface is W-invariant (resid <1e-13); the two hop sectors have equal
  kernel dim (32 = 32). The kinetic/RP surface cannot select the axis.
- **(B)** with `bc=(A,P,P,P)`, W is broken exactly (resid 2.828) and the temporal APBC
  hop sector has trivial kernel **0** vs the spatial PBC kernel **32** — a basis-free,
  **relabeling-invariant kernel-dimension discriminator** proving no signed exchange
  map can identify the two sectors once the asymmetric datum is present.
- **(C)** APBC on **both** τ and x₁ RESTORES W exactly (resid 0) and re-matches kernel
  dims (0 = 0) — the selector is **BC-ASYMMETRY, not APBC alone**.
- **(D)** the boundary vector `(A,P,P,P)` has automorphism group exactly **S₃**, fixing
  the APBC axis and permuting the three spatial axes — selects one axis *label* but no
  spatial orientation.

**The datum is NOT derived.** (1) *S₄-transportability:* a `G_bare` element maps
`(A,P,P,P)` onto `(P,A,P,P)` exactly (recomputed in-tree, N4-AUT E7 and the
consolidated runner `[N4]` block: `W` maps the APBC-τ hop onto the APBC-x₁ hop, resid
0); (2) *A_min withholds it:* the Lattice axiom supplies no boundary condition; it is
an EXPLICIT OPEN GATE in `MINIMAL_AXIOMS_2026-06-05`. The residual is relocated, not
dissolved: B-AXIS.2 stays a declared premise; the sole conditional contract is *if* a
per-axis Z₂ BC-asymmetry datum is supplied, *then* the axis label is fixed.

---

## 6. N5 treatment — no independent commuting transfer factor / no second clock

**B-AXIS clause:** B-AXIS.3 = N5 — "no independent commuting transfer factor is
admitted as a second physical clock."

### 6.1 Headline result (source-surface, not proxy)

N5 cannot be derived from A_min plus the supplied two-step transfer. The decisive
correction over all prior N5 work is that the obstruction is anchored on the
framework's **own** supplied object:

> The supplied two-step transfer is **maximally factorized**:
> `T̂² = ⊗_p diag(1, e^{−2E(p)}) = exp(−2 a_τ Ĥ)`, with `Ĥ = Σ_p E(p) n_p`,
> `E(p) = arcsinh(√(m² + sin²p))`, `n_p = a_p† a_p`. It is a tensor product of `L_s`
> independent commuting positive per-mode factor clocks (generator tangent span `{n_p}`
> has dimension `L_s`, not 1).

Two consequences, each a closed route rather than an open hope:
1. **The naive irreducibility / commutant-center route is CLOSED-as-FALSE.** No
   commutant or center argument can force a single one-parameter clock orbit, because
   the supplied transfer is maximally *reducible* — it already exhibits the `L_s`-factor
   split a second-clock comparator would need.
2. **The gauge-redundancy route is FALSIFIED.** The factor flows are not gauge: their
   generators escape `span{I, Ĥ}` (best-fit residual of `n_0` against `c·Ĥ + b·I`
   ≈ 0.65 on the block01 surface; ≈ 1.3 on the consolidated-runner surface; both > 0),
   and they produce **distinct durable occupation records** that no single `Ĥ`-orbit
   reproduces — a swept single-clock time `t` never matches the alternate factor
   clock's durable record pair `(⟨n_0⟩, ⟨n_1⟩)` (min-distance ≈ 0.40; normalized record
   profiles differ by L1 ≈ 2.0). A relabeling-invariant, Record-visible discriminator.

Therefore the missing supplier is a **physical-clock-admission datum**: a chosen
positive clock-ray in `span_{≥0}{n_p}`, equivalently a record-order bridge tying durable
outcomes to one supplied clock. That choice carries `(L_s − 1)` undetermined parameters
and is NOT supplied by Lattice, Quantum, or Record. N5 relocates to the
**record-production / emergent-dynamics OPEN GATE** of `MINIMAL_AXIOMS_2026-06-05`.

### 6.2 Absorbed runner (in-tree, recomputed, NOT rebuilt)

This section ABSORBS the block01 fresh-attempt runner R-N5-IRR
(`scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py`, TOTAL PASS=36
FAIL=0; B_AXIS_DERIVED=FALSE, SECOND_PHYSICAL_CLOCK_EXCLUDED=FALSE), which builds the
actual supplied `T̂²` from action-derived data on surfaces `L_s=3/m=0.5` and
`L_s=4/m=0.3`:
- **[SURF]** `T̂² = exp(−2 a_τ Ĥ)` (resid ≤ 5.6e-17); `T̂² = ∏_p` lifted per-mode
  factor (resid 0); factors positive-definite, commute pairwise (resid 0); generator
  span dim = `L_s`. Maximal reducibility established.
- **[GAUGE]** all `L_s` mode generators lie OUTSIDE `span{I, Ĥ}`; `n_0 ≠ c·Ĥ + b·I`
  (resid ≈ 0.65). Gauge-collapse closure FALSIFIED.
- **[CONTENT]** factor clock freezes durable `⟨n_1⟩` while `Ĥ` moves it; no swept `t`
  reproduces the alt clock's `(⟨n_0⟩, ⟨n_1⟩)` (min-dist ≈ 0.40); profiles differ
  (L1 ≈ 2.0); alt-clock projectors commute / additive (Record-legitimate flow).
- **[BRIDGE]** physical-clock admission is a free ray choice in `span_{≥0}{n_p}`
  carrying `(L_s − 1)` free parameters.

The consolidated runner `[N5]` block independently reconfirms the Stone identity (resid
3.1e-17), pairwise commutation (resid 0), the dimension-`L_s` span (rank 3), and the
non-gauge escape (resid ≈ 1.3 > 0).

### 6.3 Supersession of precursor N5 branches + physical-clock-admission definition

Two prior in-flight branches owned N5 and left an **unexplained** boundary flag because
they built only a *foreign* arbitrary two-qubit tensor product:

| precursor branch | runner | PASS | left-open flag |
|---|---|---|---|
| `origin/physics-loop/single-clock-n5-factor-boundary-20260617` | `single_clock_independent_commuting_transfer_factor_n5_no_go_2026_06_17.py` | 34 | `SECOND_PHYSICAL_CLOCK_PROVED=FALSE` |
| `origin/physics-loop/single-clock-physical-clock-inventory-20260617` | `single_clock_physical_clock_admission_inventory_n5_support_2026_06_17.py` | 35 | `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE` |

R-N5-IRR **supersedes** both with a **source-surface reason**: the factor split is the
real object's own maximal `⊗_p` structure, so the irreducibility route is closed-as-
false and the gauge route is falsified by Record-visible content. The precursors are
CITED by path+PASS, NOT rebuilt.

The **4-part physical-clock-admission definition** (carried forward verbatim from the
physical-clock-inventory precursor) — a transfer is an admitted physical-clock transfer
only if ALL four hold: (1) a named source authority supplies it as a physical
evolution/clock object; (2) the authority supplies positivity/trivial-kernel data for
the finite Stone/log construction; (3) the authority supplies the clock denominator /
block spacing; (4) the source packet consumes it as the framework evolution clock, or
explicitly admits it as a second physical-clock transfer. The **only** currently
admitted physical-clock transfer is `{ (T̂², 2 a_τ) }`; the per-mode factors satisfy
(1)–(3) on the surface but FAIL check (4). This is not a new axiom or primitive; it is a
source-scope firewall.

**Authorities (cited):** `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`
(retained_no_go, N5 checklist — finite-Stone uniqueness is transfer- and τ-relative);
`MINIMAL_AXIOMS_2026-06-05` (Record supplies no occupancy rule / time metric /
dynamics; record-production dynamics is an EXPLICIT OPEN GATE).

---

## 7. Unified residual relocation — N2b + N4 + N5 funnel to one emergent-dynamics OPEN GATE

The three open residuals are not three independent missing lemmas. They are one and the
same residual, made visible by the **native-on-Z³ framing**.

Treat time NOT as a 4th lattice coordinate (the Euclidean 4-torus reconstruction that
carries W / S₄), but as the **parameter of a one-parameter group/semigroup** `U(t)`
acting on a *fixed* spatial Hilbert space `⊗_{x∈Z³} C²`. In this framing there is no
"4th axis" object at all: time is `t ∈ R`, not `x_4 ∈ Z`. The **which-of-4-axes
question DISSOLVES** — there is nothing to permute, so W / S₄ have no axis to act on,
and N4's axis-label problem evaporates as a *question*.

But dissolving the question is not deriving the answer. The framing **RELOCATES, does
not derive**:
- the generator of `U(t)` is **not axiom-supplied** (the only retained lattice generator
  is the RP/transfer reconstruction — the 4-torus route that carries W / S₄; a generator
  sourced from a record-production layer lands in the emergent-dynamics OPEN GATE);
- the **rate / metric** still needs a supplied `τ` (this is N2b — the [τ-RESCALE] gauge
  is exactly the statement that `U(t)` has no native unit);
- **no-second-commuting-clock** is still unproven (this is N5 — the [C-2CLK]
  multi-dimensional span is exactly the statement that `⊗_{x∈Z³} C²` admits commuting
  factor flows on the fixed spatial space);
- **orientation** (past → future) is NOT sourced by the framing: it is carried by the
  **past-hypothesis** (low-record initial condition `↔` spectrum-condition `H ≥ 0`).

```
                          native-on-Z³ framing
   N4 (which axis?)  ──────────────────────────────►  DISSOLVED as a question
                                                       (no 4th coordinate to permute)
                                  │
   N2b (absolute unit a_τ) ───────┤
                                  ├──► ONE emergent-dynamics OPEN GATE:
   N5 (second commuting clock) ───┤    derive U(t) over ⊗_{x∈Z³} C² from a
                                  │    record-production dynamics layer
   orientation (t → −t) ──────────┴──► carried by PAST-HYPOTHESIS, not records
                                       (ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_
                                        RESIDUAL_2026-06-05)
```

**Orientation firewall (cite, do not re-derive).** The arrow is *not* records-sourced.
It is fixed only by `H ≥ 0` ⟺ low-record past hypothesis, per
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_2026-06-05`. Block01 R-N4-REGDIR
confirmed in-tree that the A_min record-accumulation monotone is a W-invariant
reflection-symmetric **ball, not a cone**.

**What relocation does NOT buy.** The native framing is an honester premise shape, NOT
fewer admissions: it renames where the admission lives. The residual is genuinely open;
B-AXIS stays **live**. This is a no-go about the **retained surface**, not an
impossibility proof. (Off-surface, dimension-selection — why `Z³` and one time —
remains axiomatic; the exact-zero W / S₄ facts are bounded to **even cubic-symmetric**
blocks, odd-`L` falsifier resid 6.000.)

---

## 8. No-Go Discipline Gate — N1 through N8 (per-clause, three columns N2b / N4 / N5)

The negative claim ("none of N2b / N4 / N5 is derivable from A_min plus the retained
Euclidean reconstruction surface") is shippable as a `no_go` only if it clears N1–N8
*per clause*. All load-bearing facts are recomputed in the absorbed runners cited by
branch+path+PASS; nothing is cited blind from the conditional parent keystone, the
unaudited finite-speed cone note, or the downstream ANOMALY_FORCES_TIME consumer.

### N1 — ≥5 distinct attacked routes per clause ([ATT] attempted / [ROP] ruled-out-by-prior)

**N2b column (5 routes):** (1) [ROP] absolute unit from transfer spectrum / Stone —
transfer-/τ-relative; (2) [ROP] unit from minimal Lattice/Quantum — no metric scale;
(3) [ROP] time metric from Record alone — no time metric; (4) [ROP] clock/rate from
post-record counts — many inequivalent clock maps; (5) **[ATT] joint two-rate-gate
construction (R-N2b-JOINT)** — built GATE-S ⊗ GATE-R under the strongest single-clock
coupling, WALLED ratio-only (`T̂², K, T̂²⊗K` invariant max Δ < 4e-16). N2a stays FORCED,
kept separate.

**N4 column (12 routes):** (1)–(4) [ROP] OS/GNS, durability, registration cone
(circular), anomaly/chirality — all W-transported resid 0; (5) [ROP] KMS/APBC —
exchange-covariant; (6) [ROP] APBC-alone — falsified by symmetric-APBC restoration;
(7) [ROP] per-axis Z₂ BC datum as *non-transportable* selector — S₄ acts transitively,
datum is transportable; (8) [ROP] reality/CPT grading — W-inert; (9) [ROP] Wilson
temporal-gauge — labeled choice; (10) [ROP] crossing-link P_a + η-curvature cocycle —
S_d-isotropic; (11) **[ATT] full bare-surface automorphism + enrichment search
(R-N4-AUT)** — `|G_bare|=384` transitive S₄, every A_min enrichment stabilizer full-S₄
or trivial; (12) **[ATT] derived registration-direction bridge (R-N4-REGDIR)** —
RELOCATED: A_min monotone is a direction-free ball, real LR cone is circular.

**N5 column (6 routes):** (1) [ROP] algebraic exclusion of commuting positive factors —
countermodel commutes resid 0; (2) [ROP] product-transfer Stone uniqueness erases
factor flows — `U_A(1)⊗I` off the diagonal orbit min_gap 0.292; (3) [ROP] Record
additivity collapses disjoint counters — disjoint projectors commute/additive; (4)
[ROP] physical-clock-admission firewall — inventory yields one admitted transfer; (5)
[ROP] KMS/APBC thermal circle as second clock — only decorates a supplied circle; (6)
**[ATT] irreducibility/nonfactorization of the supplied `T̂²` (R-N5-IRR)** — `T̂²`
maximally factorized (irreducibility FALSE), gauge FALSIFIED.

**N1 verdict:** PASS all three columns (N4 = 12 ≥ 10, N5 = 6 ≥ 5, N2b = 5 ≥ 4). The two
historically deferred load-bearing positive routes (`T̂²` irreducibility, derived
registration-direction bridge) are now [ATT], so the "premature no-go" objection is
closed.

### N2 — Wall-independence (one load-bearing wall per column)

| column | the ONE load-bearing wall | walls collapsed INTO it |
|---|---|---|
| **N2b** | the **clock-unit wall** — no A_min observable carries a `1/time` unit; `a_τ→c·a_τ` is an exact `ℝ_{>0}` gauge | Stone/spectrum, Lattice-no-scale, Record-no-metric, post-record-counts, joint two-gate — all the same `c`-rescaling viewed through a different gate |
| **N4** | the **single axis-label wall** — automorphism image is transitive S₄, every A_min anchor is W/S₄-transported (resid 0) | OS/GNS, durability, cone, anomaly, reality/CPT, KMS/APBC, Wilson, crossing-link/cocycle are presentations of the one transitive-orbit fact; E7 is the single sub-S₄ enrichment and is itself transportable |
| **N5** | the **factor-exclusion wall** — supplied `T̂²` is maximally factorized into `L_s` commuting per-mode clocks; no commutant/center forces one orbit | tensor-locality countermodel, product-Stone non-uniqueness, Record-additivity, admission-firewall inventory all collapse to "the source object itself already exhibits independent factor flows" |

Cross-column independence: N2b (a *unit*), N4 (a *label*), N5 (a *factor count*) are
genuinely distinct missing data; no column's wall is a corollary of another's.
**N2 verdict:** PASS.

### N3 — Hidden-wall scan (explicitly constructed countermodels, not imported physics)

Every load-bearing surface is an explicitly constructed finite countermodel verified by
exact arithmetic: the N2b GATE-S⊗GATE-R joint carrier (exact arithmetic, max Δ < 4e-16,
no continuum/thermodynamic import); the N4 `G_bare` computed by BFS-solving the Z₂ sign
field per relabeling (no OS theorem, no Lorentz/boost content, boost-faith guardrail
respected); the N5 countermodel is the framework's OWN supplied `T̂²` recomputed from
the free staggered dispersion (no Lieb-Robinson lightcone M2 imported — only equal-time
tensor locality M1, generator-free). The one place physics could be smuggled is the
staggered-Dirac *surface itself*; but it is the retained (R-RP2)/(R-SC2)/(R-CL3) object
and the no-go's claim is explicitly ABOUT that retained surface. **N3 verdict:** PASS.

### N4-check — residual matching for every cited witness no-go

Every cited witness's open residual is the same open gate as this note's residual; no
cited authority secretly discharges a clause this note leaves open. The N4-only witness
(2026-06-11) and KMS-only witness (2026-06-16) are NOT borrowed into N2b/N5 (they own
neither). The four block01 [ATT] runners each terminate on a wall whose residual is one
of: N2b → clock/rate gate; N4 → boundary-condition / record-production-dynamics gate;
N5 → physical-clock-admission ray — all sub-cases of the single
`MINIMAL_AXIOMS_2026-06-05` emergent-dynamics open gate. **N4-check verdict:** PASS.

### N5-check — rhetoric audit: even cubic-symmetric staggered blocks only (odd-L falsifier)

Every "residual 0 / exactly invariant / exact" W/S₄ claim is bounded to **EVEN
cubic-symmetric staggered-Dirac blocks**. The odd-L falsifier is carried verbatim: at
`L=(3,3,3,3)` the signed exchange does NOT preserve the hop, `‖W M Wᵀ − M‖ = 6.000`
(consolidated runner `[SCOPE]` and R-N4-AUT [SCOPE]); at even `L=(4,4,4,4)` the residual
is 0. The N5 `T̂²=⊗_p diag(1,e^{−2E(p)})` exact-zeros are surface-specific (free-sector
staggered transfer); the escapes-`span{I,Ĥ}` / distinct-record claims are inequalities
(≈ 0.65, ≈ 0.40), not exact zeros. No exact-zero is stated as framework-wide.
**N5-check verdict:** PASS (binding requirement on the prose, satisfied here).

### N6 — Partial-closure path scan (named suppliers as open targets, never new axioms)

| column | named supplier (partial-closure path) | new-axiom requirement? |
|---|---|---|
| **N2b** | a separate supplied **clock/rate bridge** carrying a `1/time` unit | NO — an open downstream bridge any unitful claim must identify |
| **N4** | one per-axis Z₂ **BC-asymmetry datum** OR a derived **registration-direction bridge** | NO — open derivation targets; A_min withholds the boundary datum as an EXPLICIT OPEN GATE |
| **N5** | an **irreducibility** theorem (closed-as-FALSE), a **physical-clock-admission** ray, or a **gauge/redundancy** theorem (FALSIFIED) | NO — the surviving supplier (admission ray) is an open source decision / derivation target |

All three reduce to data the **emergent-dynamics OPEN GATE** of
`MINIMAL_AXIOMS_2026-06-05` would supply if a record-production dynamics layer were
derived. None is phrased as "add an axiom." **N6 verdict:** PASS (critical under the
no-new-axiom hard rule).

### N7 — Steelman per clause (strongest hostile counter, then the fresh attempt that falsified it)

- **N2b steelman:** "Two gates pinned to the SAME physical clock jointly over-determine
  `a_τ`." **Falsified by R-N2b-JOINT:** built under exactly that coupling
  (`K=exp((2a_τ)Q)`); the rescaling is an EXACT `ℝ_{>0}` gauge (max Δ < 4e-16); no A_min
  observable returns a `1/time` number.
- **N4 steelman:** (a) "a richer A_min enrichment will fix one axis"; (b) "record-
  PRODUCTION singles out the evolution direction intrinsically." **Falsified by R-N4-AUT
  and R-N4-REGDIR:** (a) the entire 384-element `G_bare` computed, every A_min
  enrichment full-S₄ or trivial; only E7 (a supplied BC datum outside A_min, itself
  S₄-transportable) selects; (b) the A_min monotone is a direction-free ball, the LR
  cone is circular (Δ 7e-16).
- **N5 steelman:** "the supplied `T̂²` is irreducible, or any factor split is gauge."
  **Falsified by R-N5-IRR:** `T̂²` is *maximally* factorized into `L_s` commuting per-mode
  clocks (irreducibility FALSE); each mode generator escapes `span{I,Ĥ}` (resid ≈ 0.65)
  and produces a distinct durable record (min-dist ≈ 0.40, Record-visible) — gauge
  FALSIFIED.

**N7 verdict:** PASS. Each column's strongest hostile counter was built in block01 and
falsified by computation.

### N8 — Cross-cycle echo (all clauses funnel to the same emergent-dynamics open gate)

N2b → absolute clock unit needs a clock/rate bridge; N4 → axis label needs a
BC-asymmetry / registration-direction datum from a record-production dynamics layer;
N5 → a physical-clock-admission ray. All three are the *same* missing thing viewed from
three sides: **the emergent-dynamics OPEN GATE of `MINIMAL_AXIOMS_2026-06-05`**
(Lattice/Quantum/Record supply no dynamics, no time metric, no record-production
dynamics, no arrow, no boundary datum, no occupancy rule). The native-on-Z³ framing
(Section 7) is the single dissolving framing that makes which-of-4-axes disappear but
RELOCATES rather than derives; orientation is separately carried by the past hypothesis.
**N8 verdict:** PASS.

### N1–N8 gate disposition

PASS per clause for all three columns, with the even-extent qualifier on every
exact-zero, the named-supplier-as-open-target framing on every escape, and the
off-surface dimension-selection carve-out. The negative claim is shippable as a `no_go`
on the retained even-extent staggered-Dirac surface (intended classification;
independent audit lane is sole status authority).

---

## 9. Consumer firewall summary + boundary flags

This note derives nothing of B-AXIS; the consumer-firewall branch
`origin/physics-loop/single-clock-baxis-consumer-firewall-20260617` already demoted 9
scoped downstream consumers of the keystone to consume N2/N4/N5 explicitly as
PREMISES (runner `scripts/single_clock_baxis_consumer_firewall_check_2026_06_17.py`,
PASS=46), including the withdrawal of the G_NEWTON S3 "unique RP-admissible reflection
axis / no second clock" claim. Boundary flags for this note: **B_AXIS_DERIVED = FALSE;
B_AXIS_CONSUMED_AS_PREMISE = TRUE; AUDIT_LEDGER_WRITTEN = FALSE; AUDIT_VERDICT_APPLIED =
FALSE.** Independent audit lane is the sole status authority.

---

## 10. Honest scope statement (binding on the shipped no_go)

1. **Surface-specific.** The exact-zero W/S₄ transport facts and the maximal `T̂²`
   factorization hold on the **even cubic-symmetric staggered-Dirac reconstruction
   surface** ((R-RP2)/(R-SC2)/(R-CL3) object). On **odd** extents the signed exchange is
   not even a symmetry (`resid 6.000`); the claims are scoped to even cubic-symmetric
   blocks and the odd-L falsifier is exhibited.
2. **Not an impossibility proof.** The note proves that **A_min + this retained surface**
   does not *derive* N2b, N4, or N5; it does NOT prove no extension could ever supply
   them. Each named supplier is an open derivation/admission target, not a refuted
   object.
3. **Dimension-selection off-surface remains axiomatic.** Selecting the spacetime
   dimension off this surface is not addressed and remains an axiomatic input.
4. **Conditional-parent caveat.** The keystone parent
   (`axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`,
   audited_conditional, downstream fanout 959) is itself conditional; this note
   recomputes every load-bearing fact in-runner rather than citing it (or the unaudited
   finite-speed cone note or the downstream ANOMALY_FORCES_TIME consumer) blind. Any
   wall ultimately resting on the parent is conditional until the audit lane adjudicates
   the parent.

---

## 11. Source-discipline statement (load-bearing)

This note takes **NO load-bearing citation edge** to:
- the **conditional parent keystone**
  `axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03`
  (audited_conditional — citing it blind would make the wall conditional on an
  unaudited parent);
- the **unaudited finite-speed registration cone note** (the R-N4-REGDIR cone fact is
  recomputed in-runner instead);
- the **downstream ANOMALY_FORCES_TIME consumer** (the count-not-label fact is
  recomputed, not inherited from the consumer; ANOMALY_FORCES_TIME is referenced here
  ONLY inside this disclaimer, never as a derivation authority).

Every load-bearing fact is reproduced by an in-tree runner listed in Section 12 (the
source-discipline lesson established by the axis-nogo-self-contained branch: recompute,
do not cite blind).

---

## 12. Machine certificate index (absorbed / consolidated runners)

Every load-bearing fact above is **recomputed in-tree**, not cited blind.

**Consolidated runner (this note):**

| runner | clauses / facts | PASS/FAIL |
|---|---|---|
| `scripts/single_clock_baxis_obstruction_unified_2026_06_20.py` | N4 S₄-transitivity + symmetric W-break + BC transportability; N5 maximal factorization + non-gauge; N2b joint-rescale gauge + malformed discriminator; N2a forced denominator + factor-two falsifier; `[SRC]` source-discipline; `[SCOPE]` even-extent / odd-L falsifier | **PASS=32 FAIL=0** |

**Absorbed block01 clause runners (in-tree, recomputed this cycle):**

| runner (absolute path) | clause / fact | PASS/FAIL |
|---|---|---|
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` | N4: `|G_bare|=384`, axis image transitive S₄; every A_min enrichment joint stabilizer full-S₄ or trivial; even-extent scope | **PASS=17 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py` | N5: supplied `T̂²` maximally factorized, `L_s` commuting per-mode clocks, rank-`L_s` generator span, factors not gauge | **PASS=36 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` | N2b: joint `a_τ→c·a_τ, H→H/c, Q→Q/c` exact 1-param gauge; gates fix only dimensionless ratio; N2a forced | **PASS=18 FAIL=0** |
| `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` | N4: record-accumulation monotone is W-invariant ball not cone; LR cone transports with H (circular); arrow = past-hypothesis | **PASS=20 FAIL=0** |

**Aggregate of the four absorbed block01 runners: PASS=91 FAIL=0, cracks=0**
(matches `SINGLE_CLOCK_BAXIS_FRESH_ATTEMPTS_STRETCH_NOTE_2026-06-20.md`).

**Cited (not rebuilt) — in-flight branch runners (by branch+path+PASS):**
- `origin/physics-loop/single-clock-axis-nogo-self-contained-20260617`:
  `scripts/single_clock_axis_selection_check_2026_06_11.py` blocks
  [RT-RP]/[RT-REC]/[RT-ANOM]/[PIN] (PASS) — OS/GNS, durability, cone, anomaly
  transport + kernel-dim discriminator.
- `origin/physics-loop/single-clock-apbc-axis-bridge-20260616`:
  `scripts/frontier_single_clock_apbc_axis_label_bridge_2026_06_16.py` (PASS=21) —
  conditional axis-label bridge (W-break, kernel discriminator, symmetric-BC falsifier,
  S₃ automorphism).
- `origin/science/single-clock-axis-datum-s4-transportable-2026-06-17`:
  `scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py` (PASS=22) —
  S₄ transitivity + BC datum transportability.
- `origin/physics-loop/single-clock-blocked-time-unit-split-20260617`:
  `scripts/single_clock_blocked_time_unit_split_n2_support_2026_06_17.py` (PASS=35) —
  N2a exact-support + N2b no-go split.
- `origin/physics-loop/single-clock-n5-factor-boundary-20260617` (PASS=34) and
  `origin/physics-loop/single-clock-physical-clock-inventory-20260617` (PASS=35) —
  N5 precursors, superseded with a source-surface reason.
- `origin/physics-loop/single-clock-baxis-consumer-firewall-20260617`:
  `scripts/single_clock_baxis_consumer_firewall_check_2026_06_17.py` (PASS=46) —
  consumer firewall.

**Authorities CITED as authorities (not recomputed — RETAINED no-gos + minimal axioms):**
- `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06` (retained_no_go) — governing
  fence; N2/N4/N5 clause labels; Stone transfer-/τ-relative.
- `SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_2026-06-11`
  (retained_no_go) — OS/GNS, durability, cone-circularity, anomaly count-not-label
  W-transport witnesses; sharpened pin.
- `SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_2026-06-16` (retained_no_go) — KMS/APBC
  exchange-covariant; cited as pruned route, not re-tested.
- `MINIMAL_AXIOMS_2026-06-05` — A_min content + the EXPLICIT OPEN GATES (arrow,
  measurement, decoherence, record-production dynamics) that Section 7 relocates onto.
- `ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_2026-06-05` — orientation
  carried by past-hypothesis (Section 7 orientation firewall).

---

## 13. Status discipline

Branch-local source artifact for `physics-loop/single-clock-baxis-wall-block02-20260620`.
Adds NO framework axiom, introduces NO primitive, sets / updates NO audit status, edits
NO audit / publication / effective-status surface. Branch-local status vocabulary only;
no bare "retained"/"promoted" in any status line. Cited upstream statuses
(`retained_no_go`, `exact-support`) are quoted from their source notes, not reasserted
here. `proposal_allowed=false`; `bare_retained_allowed=false`;
`audit_required_before_effective_retained=true`. The independent audit lane is the sole
status authority.

---

## CORRECTION (2026-06-20, block05 exercise reassessment)

**This is an ADDITIVE correction, appended — not a silent rewrite.** The original
sections 1–13 above are left verbatim so the audit trail is honest. The
`baxis-wall-break` exercise (packet
`.claude/science/exercises/baxis-wall-break/`) surfaced five attack routes; each
was verified by an independent max-rigor route author with its own runner. The
block05 synthesis is
`docs/SINGLE_CLOCK_BAXIS_WALL_REASSESSMENT_NOTE_2026-06-20.md`
(consolidated runner `scripts/single_clock_baxis_reassessment_2026_06_20.py`,
PASS=34 FAIL=0; five per-route runners aggregate PASS=143 FAIL=0). It found the
no_go's **verdict correct (B-AXIS not derivable; no clause closes; no crack)**
but **three overclaims in the supporting reasoning/scope** that this section
amends. NO clause status changes; NO new axiom or primitive; A_min remains
Lattice + Quantum + Record + the four approved primitives.

### C-1. N5 algebra — §6.1, §6.2 `[GAUGE]`, Witness W-1: linear-span is the wrong test

**Original claim (amended, not deleted).** §6.1(2), §6.2 `[GAUGE]`, and Witness
W-1 argue the per-mode factor flows are "not gauge ⇒ independent second clocks"
because their generators **escape `span{I,Ĥ}`** (resid ≈0.65), concluding a
**`(L_s−1)`-parameter physical-clock-admission ray**.

**Correction (R-FC-N5, runner `single_clock_n5_functional_calculus_one_clock_2026_06_20.py`
PASS=50/0).** "Function of the single generator `Ĥ`" is NOT "in the 2-d linear
span `{I,Ĥ}`"; the correct algebra is `{Ĥ}'' = {f(Ĥ)}` (spectral functions),
of dimension = **#distinct eigenvalues of `Ĥ`** (recomputed: `2^{L_s}`=16/64/256
collapse to 9/15/45 distinct eigs at `L_s`=4/6/8), generally ≫ 2. Escaping
`span{I,Ĥ}` is **necessary but far from sufficient** (`Ĥ²`, `√Ĥ`, every spectral
projector escape it yet are single-clock); the correct discriminator is
`n_p ∉ {f(Ĥ)}`. The genuine second-clock room is the **`Ĥ`-degeneracy room**
`2^{L_s} − #distinct` = **7/49/211**, NOT `(L_s−1)`=3/5/7. The wall STANDS only
because the supplied many-body `Ĥ` IS degenerate (reflection `E(p)=E(L_s−p)`
plus energy-sum collisions; every `n_p` has fc-resid >0, 0 of `L_s` reachable);
on a non-degenerate spectrum the room is 0 and N5 holds with a single clock
outright (falsifier leg, max resid 0). **So §6 got the right answer (live wall)
for the wrong reason (linear span).** Replace the "escapes `span{I,Ĥ}` ⇒
independent clock, `(L_s−1)`-param ray" wording with: *single clock iff `Ĥ`
non-degenerate; genuine room = `Ĥ`-degeneracy room (`2^{L_s}−#distinct`)*.

### C-2. N5 cause — §6.1: the `L_s`-fold tower is the integrable signature, not generic

**Original claim (amended).** §6.1 anchors the N5 wall on the maximal `⊗_p`
factorization (span dim `L_s`) as the obstruction, with the `(L_s−1)`-param ray
as the missing supplier.

**Correction (R-DICHOTOMY-N5, runner
`single_clock_n5_integrability_dichotomy_2026_06_20.py` PASS=37/0).**
`Ĥ = Σ_p E(p) n_p` is a **free-fermion `H`** and `{n_p}` is its **free
conserved-charge tower** — the integrable signature, NOT a generic A_min
obstruction. A minimal A_min-admissible local interaction `V = g Σ_x n_x n_{x+1}`
(Hermitian, on-site `M_2(ℂ)`, number-preserving, dimensionless `g`) **destroys
the tower** (every mode charge decommutes; bilinear conserved-charge span
collapses 9→1 toward `{I,N,Ĥ}` on a clean NN chain, generically in `g`).
**Corrected missing supplier:** N5 holds **conditional on non-integrability** of
the emergent dynamics — a **one-bit generic-position premise, not an
`(L_s−1)`-parameter admission ray** (that count is just the dimension of the FREE
tower). The relocation-to-open-gate conclusion is unchanged; N5 stays LIVE
(dynamics unsupplied). `L_s=3` is excluded (the ring is `K₃`, `V` is number-only).

### C-3. N4 consumer-relevance — §2 table, §9 firewall: label is over-specified for the sole consumer

**Original claim (amended).** §2's table lists N4 (axis LABEL) as a load-bearing
"open (declared premise)" wall for the 959 cone, and §9's consumer firewall
demotes every consumer to consume B-AXIS as one opaque premise (the coverage
runner checks only a single B-AXIS marker per consumer; it does not split count
from label).

**Correction (R-COUNT-N4, runner `single_clock_count_label_free_n4_2026_06_20.py`
PASS=16/0).** The keystone's **only** consumer
(`docs/ANOMALY_FORCES_TIME_THEOREM.md`) reads from B-AXIS exactly the codim-1
**COUNT** cap `d_t ≤ 1` ("one admitted clock factor"), never the axis LABEL (its
conclusion is the pure signature `(3,1)`). The count is **S₄-invariant /
label-free**: the four per-axis codim-1 constructions form ONE inequivalence
class modulo S₄ (every `g ∈ G_bare` maps `D_a → ±D_{π(a)}` resid 0; single orbit
`{0,1,2,3}`). The LABEL is genuine non-derivable data (`‖D_0−D_1‖=16` per the
route's surface) but **over-specified for this consumer**. So **N4-as-a-LABEL
wall shrinks for the 959 cone**; N4-LABEL-derivation stays walled (S₄-transitive,
recomputed), N2b and N5 untouched. This sharpens — does not contradict — §5.3's
"count-not-label firewall" (which only said the anomaly cannot *supply* the
label; the dual is that the consumer does not *need* it).

### C-4. Scope — A_min now = Lattice + Quantum + Record + the FOUR approved primitives

**Original framing (amended).** Sections 1–13 phrase the obstruction as "not
derivable from A_min = Lattice + Quantum + Record." The reassessment hardens this
to the **four approved primitives** (`scale_reference`, `kinetic_isotropy`,
`realized_state`) as legitimate premises.

**Correction (R-DEFINABILITY PASS=24/0; R-KINFORM-N2b PASS=16/0).** A Beth/
Svenonius independence theorem shows `a_τ` (N2b), the axis label (N4), and the
clock-ray (N5) are each undefinable from **A_min + all three approved primitives**
— **NO CRACK** on any primitive: `scale_reference` is spatial-units-only (the
spacing ratio `a_τ/a` is disclaimed); `kinetic_isotropy` grants the **isotropic**
`c_t=c_s` form whose axis image is transitive S₄ (the axis-selector `c_t≠c_s` is
exactly what it does NOT grant — closing the REFRAMING A1 lead); `realized_state`
gives only pointwise evaluation (the realized axis is registered data by the
counterfactual clause). Additionally R-KINFORM-N2b adds a **6th N2b column**: the
form↔spacing identity `c_t/c_s == a_τ/a_s` is FALSE (it is `(a_s/a_τ)²` at best,
convention-dependent), so the primitives do not pin the absolute clock unit.
**Sharpening of §5.2:** a one-axis-selecting (S₃) enrichment DOES exist
(anisotropic `c_t≠c_s`); it is excluded because the approved primitive sets the
form to the symmetric `S₄` value — strictly stronger than "no S₃ enrichment
found."

### C-5. Net disposition of this correction

The no_go's **verdict and direction stand** (B-AXIS not derivable; all residuals
on the emergent-dynamics open gate; no closure; no new axiom). What is amended is
the **shape, size, and consumer-relevance** of three walls: N5's reasoning
(span→`{f(Ĥ)}`) and ray size (`(L_s−1)`→degeneracy room / one non-integrability
bit), and N4's label (over-specified for the sole consumer). No boundary flag
flips. Full reassessment, scope, and runner index:
`docs/SINGLE_CLOCK_BAXIS_WALL_REASSESSMENT_NOTE_2026-06-20.md`.
`proposal_allowed=false`; `audit_required_before_effective_retained=true`; the
independent audit lane is the sole status authority.
