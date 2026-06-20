# Single-Clock B-AXIS — Fresh-Attempt Stretch Note (Block 01)

**Date:** 2026-06-20
**Type:** stretch_attempt (no_go-supporting)
**Status:** stretch-attempt with honest residual; all four routes either wall on a
named A_min boundary or relocate to the emergent-dynamics / record-production
open gate of `MINIMAL_AXIOMS_2026-06-05.md`. Not a closure, not a derivation of
B-AXIS, not a new axiom, not a status edit. Independent audit lane is the sole
status authority.
**proposal_allowed:** false
**bare_retained_allowed:** false
**audit_required_before_effective_retained:** true
**Scope:** branch-local source artifact for branch
`physics-loop/single-clock-baxis-wall-block01-20260620`. Sets no audit or
publication status.

---

## Purpose

Four B-AXIS clauses were flagged "live-positive but never genuinely built" in
`ROUTE_PORTFOLIO.md` / `NO_GO_LEDGER.md`. A consolidated B-AXIS no-go is
PREMATURE while those routes are merely cited rather than worked. This note
records that each of the strongest never-attempted POSITIVE routes was tried as
a real derivation attempt from A_min (Lattice + Quantum + Record only), with a
self-contained runner that builds the actual operators/surfaces and checks the
attempt with explicit residuals. The note (a) closes the N1 ≥5-route
enumeration and the N7 steelman weak points by converting four "never built"
flags into honestly-run outcomes, and (b) flags any crack.

**Crack flag: NONE.** No route derived B-AXIS, a second physical clock, an
absolute clock unit, or a non-transportable axis-selector from A_min. Each
attempt terminates on a named load-bearing wall with retained authority, or
relocates to an explicit open gate. B-AXIS stays live.

---

## A_min reminder (what each axiom withholds — `MINIMAL_AXIOMS_2026-06-05.md`)

- **Lattice** supplies `Z^3` + cubic adjacency. Withholds: dynamics, boundary
  condition, metric scale, lattice spacing, causal cone, probabilistic
  independence, physical unit conversion.
- **Quantum** supplies the one-qubit / `Cl(3,0)` site algebra. Withholds:
  dynamics, composition beyond lattice placement, measurement instrument, Born
  rule, gauge group, observable bridge.
- **Record** supplies durable additive registration of the realized outcome.
  Withholds: readout context, decomposition, `K`/CPT structure, weighting,
  probability, measurement/decoherence dynamics, time metric, occupancy rule.
- **EXPLICIT OPEN GATES (outside axiom content):** arrow, measurement,
  decoherence, **record-production dynamics**, physical persistence dynamics,
  source/action, observable identification.

---

## Route R-N5-IRR — irreducibility / nonfactorization of the supplied transfer

**Clause:** N5 / B-AXIS.3 — no independent commuting transfer factor admitted as
a second physical clock.

**What was attempted (from A_min):** A genuine irreducibility / nonfactorization
theorem for the framework's OWN supplied two-step transfer `T̂²` (not an
arbitrary 2-qubit proxy): prove its commutant/center structure FORCES a single
one-parameter clock orbit, OR prove the candidate commuting factor clocks are
gauge/redundant with no independent Record-visible order parameter — either would
CLOSE N5. This pushes past the two prior N5 branches that used a foreign tensor
product and left `MATHEMATICAL_FACTOR_TRANSFERS_EXCLUDED=FALSE` /
`SECOND_PHYSICAL_CLOCK_PROVED=FALSE` unexplained.

**Method (A_min-only):** Recomputed the actual supplied object from
action-derived data: `T̂² = Γ(t₁^(2)) = ⊗_p diag(1, e^{-2E(p)}) = exp(-2 a_τ Ĥ)`,
`Ĥ = Σ_p E(p) n_p`, `E(p) = arcsinh(√(m²+sin²p))`. Four legs, explicit numpy
residuals:
- **[SURF]** `T̂²` is MAXIMALLY factorized into `L_s` commuting positive per-mode
  factor clocks (generator span dim = `L_s`, not 1) — naive irreducibility is
  FALSE on the source surface.
- **[GAUGE]** gauge-collapse closure (every factor generator in span{I,Ĥ}):
  FALSIFIED — all `L_s` mode generators escape span{I,Ĥ}; `n_0 ≠ c·Ĥ + b·I`
  (resid ≈ 0.65).
- **[CONTENT]** factor flows carry independent Record-visible content: a
  single-mode clock freezes durable record ⟨n_1⟩ while Ĥ moves it; NO swept
  single-clock time `t` reproduces the alt clock's durable occupation pair
  (min dist ≈ 0.40–0.44); record profiles differ by L1 ≈ 2.0; alt-clock
  projectors commute/additive (Record-legitimate).
- **[BRIDGE]** missing supplier = an `(L_s−1)`-parameter physical-clock-admission
  ray, not supplied by A_min.

**Runner:** `scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py`
— **TOTAL: PASS=36 FAIL=0**.

**Outcome:** walled_named. NO crack. Negative boundary / no-go for N5, now
anchored on the actual source surface rather than a proxy.

**Load-bearing wall:** N5 closure requires a physical-clock-admission datum — a
chosen positive clock-ray in `span_{≥0}{n_p}` (equivalently a record-order bridge
tying durable outcomes to one supplied clock), carrying `(L_s−1)` undetermined
parameters. The supplied `T̂²` is maximally factorized (⊗_p per-mode clocks), so
no commutant/center argument forces a single orbit, and the factors are not gauge
(they escape span{I,Ĥ} and produce distinct durable occupation records Ĥ cannot
reproduce). A_min + the (R-RP2)/(R-SC2) surface does NOT supply this admission
ray.

**Authority:** `MINIMAL_AXIOMS_2026-06-05.md` (Record supplies no occupancy
rule / no time metric / no dynamics; record-production dynamics is an EXPLICIT
OPEN GATE); `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
(retained_no_go, N5 checklist; finite-Stone uniqueness is transfer- and
τ-relative); `AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`
(B-AXIS.3 / N5 target wording; block [C-2CLK]).

---

## Route R-N4-REGDIR — derived non-transportable registration-direction bridge

**Clause:** N4 (axis-label / time-axis selection).

**What was attempted (from A_min):** DERIVE a non-transportable
registration-direction bridge — does record-accumulation, modeled as a
Lieb-Robinson / causal-cone monotone over `Z^3`, single out a UNIQUE
evolution-generating direction WITHOUT presupposing a generator, thereby breaking
the signed exchange unitary `W = P_{τ↔1}·diag((-1)^{x_τ x_1})`?

**Method (A_min-only):** Lattice graph distance + Quantum one-qubit
algebra/equal-time tensor locality (M1) + Record durable additive registration.
Four genuinely-built legs, each checked with explicit residuals against
W-conjugation and axis-swap covariance:
- **[BALL]** the A_min record-accumulation monotone is reflection-symmetric in
  every axis and W-invariant (resid 0) → a ball, not a cone.
- **[DYN]** a genuine LR cone is a single point at `t=0` (M1) and spreads only
  with a supplied generator; the W-conjugate generator `H' = P_π H P_π^T` gives
  an IDENTICAL cone (max diff 7e-16) → the cone transports with H (circular).
- **[ARROW]** the same time-symmetric map gives up/down record profiles from
  low/high-record boundaries → arrow is the supplied past-hypothesis boundary.
- **[PROD]** an axis-agnostic site-diagonal record-PRODUCTION CPTP map + uniform
  broadcast POVM are exactly W-/swap-covariant (resid 0); only an asymmetric
  pointer-axis datum breaks covariance (break = 3.44).

**Runner:**
`scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py`
— **TOTAL: PASS=20 FAIL=0**.

**Outcome:** relocated_to_open_gate. NO crack. N4 axis-label relocates to the
record-production-dynamics / arrow OPEN GATE.

**Load-bearing wall:** Record-production dynamics, the arrow / initial-condition
(past hypothesis), and the readout-context / pointer-basis are EXPLICIT OPEN
GATES outside axiom content. A_min supplies no dynamics, no causal cone, no time
metric, no readout context, no arrow; so no A_min-only monotone is
non-transportable across W-equivalent axes. Record-production breaks W only when
handed an asymmetric pointer / readout-axis datum, which IS the
registration-direction bridge — undischarged.

**Authority:** `MINIMAL_AXIOMS_2026-06-05.md` (Lattice no causal cone; Record no
readout context / time metric; open-gate list: arrow, measurement, decoherence,
record-production dynamics);
`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md` (arrow
in initial condition = past hypothesis);
`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` (retained_no_go);
`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md` (retained_no_go, N4 +
Stone τ-relativity);
`LIEB_ROBINSON_EQUAL_TIME_TENSOR_LOCALITY_NARROW_THEOREM_NOTE_2026-05-10.md` (M1
generator-free; M2 requires a Hamiltonian, out of scope).

---

## Route R-N2b-JOINT — absolute clock unit from two retained rate gates, jointly

**Clause:** N2b (B-AXIS.1b) — absolute physical clock unit `a_τ`, distinct from
the `1/(2 a_τ)` internal denominator that N2a already forces.

**What was attempted (from A_min):** Derive an ABSOLUTE clock unit `a_τ` (a number
carrying units of time) from the two retained rate gates JOINTLY — GATE-S
(spectrum-condition blocked-time bridge supplying dimensionless
`T̂² = exp(-2 a_τ H)` and the `1/(2 a_τ)` reconstruction) and GATE-R
(record clock/rate normalization gate supplying a reversible production generator
`Q` with `Q π = 0`, kernel fixing only the dimensionless product `t·Q`).
Hypothesis: demanding ONE clock drive BOTH the transfer block and the record-rate
stream might over-determine and pin `a_τ` absolutely.

**Method (A_min-only):** On a finite carrier, built both gate objects from the
A_min surface (`H ≥ 0`, `T2 = exp(-2 a_τ H)` positive Hermitian, reversible `Q`
with `Q π = 0`), tied them with the strongest single-clock coupling
(record-block kernel `K = exp(2 a_τ Q)`, one record block per transfer step),
then applied the candidate second-clock rescaling `a_τ → c a_τ`, `H → H/c`,
`Q → Q/c`. CRACK criterion: any A_min+GATE-S+GATE-R observable changes ⇒ `c`
forced to 1 ⇒ `a_τ` absolute. WALL criterion: every observable invariant ⇒
ratio-only gauge. Swept `c ∈ {0.5, 1.3, 2.0, 5.0}`; steelman with explicit
record-count-per-block datum + group-structure check of the rescaling.

**Runner:** `scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py`
— **TOTAL: PASS=18 FAIL=0**.

**Outcome:** walled_named. NO crack. Ratio-only no-go on N2b, confirmed by a
worked joint two-gate construction (not merely cited). N2a remains
exact-support / forced (resid 0); never relist N2 as a single opaque import.

**Load-bearing wall:** No A_min observable returns a unit-bearing `1/time`
number: `T̂²`, the record-block kernel `K`, and `T2(x)K` are ALL exactly
invariant under the joint 1-parameter rescaling `a_τ → c a_τ` (`H → H/c`,
`Q → Q/c`), residuals < 4e-16. The two gates jointly fix only dimensionless
ratios (`m_gap · relaxation-time`, counts-per-block). The absolute unit requires
a metric scale that Lattice withholds and a time metric that Record withholds.
The rescaling extends verbatim from GATE-S to the GATE-R generator, so the joint
system inherits the single-gate gauge rather than escaping it. Sharpened
statement: no A_min observable carries units of `1/time` — every observable is a
dimensionless ratio or a pure count — so no additional gate of this type can ever
pin the unit.

**Authority:** `SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`
(retained_no_go: Stone is transfer- and τ-relative; `2 a_τ → 2c a_τ` rescales H
by `1/c`, `T̂²` unchanged); `MINIMAL_AXIOMS_2026-06-05.md` (Lattice
no-metric-scale, Record no-time-metric);
`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md` (counts fix order + number, not
seconds).

---

## Route R-N4-AUT — automorphism-stabilizer steelman ("richer surface breaks W")

**Clause:** N4 (axis-selection / axis-label of B-AXIS.2).

**What was attempted (from A_min):** Steelman — search for ANY A_min-available
surface enrichment on the even cubic-symmetric staggered-Dirac block whose
automorphism stabilizer is strictly smaller than `S4` and fixes exactly one axis
(a non-transportable axis-selector), WITHOUT presupposing the Hamiltonian / H.
Enumerated 8 enrichment candidates (E1–E8): reality / CPT parity grading, cubic
adjacency Laplacian, staggered `η` hop-sector family, STW crossing-link RP
invariant, `η`-curvature 2-cocycle, Record additive scalar readout, per-axis
`Z2` BC datum, face-diagonal-enriched cubic graph.

**Method (A_min-only):** Computed the FULL automorphism group of the bare surface
(not just the single W): enumerated the signed hyperoctahedral group `B4` (384
candidate site relabelings = 24 axis-perms × 16 reflections), solved per-element
for the diagonal `Z2` sign field via BFS over the hop graph, admitted `g` iff
`‖U_g M U_g^T − M‖ < 1e-9`. Result `|G_bare| = 384`, axis image = full transitive
`S4`. Then computed each enrichment's stabilizer inside `G_bare`, reporting the
axis-permutation image. **Corrected crack criterion:** an enrichment SELECTS an
axis iff its stabilizer fixes exactly one axis as a common fixed point AND acts
transitively on the other three (the S3-fixing-one signature); a trivial
identity-only stabilizer fixes all four and selects none. Exact finite-dim linear
algebra, deterministic, no RNG.

**Precise structural result (corrected):** every A_min enrichment's JOINT
stabilizer with the staggered hop is **either all of `S4` (isotropic) or trivial
(a symmetric, non-axis-selecting break of W)**; **NO A_min enrichment has a
one-axis-selecting (`S3`) stabilizer**. The only one-axis-selecting enrichment is
the per-axis `Z2` BC datum (E7), which is `S4`-transportable and outside A_min.
Specifically **E2 (cubic Laplacian) and E8 (diagonal graph) actually BREAK W** —
their joint stabilizer with the staggered hop is **trivial (identity-only), NOT
`S4`-isotropic**: the plain swap keeps the Laplacian/diagonal graph but breaks the
staggered hop (resid ≈ 22.63), the dressed W keeps the hop but breaks the graph
(resid ≈ 45.25), and no non-identity `B4` element keeps both. But the break is
axis-SYMMETRIC (a trivial joint stabilizer fixes all four axes / acts freely),
singling out no axis. This is **stronger** than "every A_min enrichment is
`S4`-isotropic": some A_min enrichments DO break W; they just break it
symmetrically.

**Runner:** `scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py`
— **TOTAL: PASS=17 FAIL=0**.

**Outcome:** walled_named. NO crack. The steelman was genuinely built and
falsified: no A_min enrichment is one-axis-selecting, so the `S4` automorphism
orbit is exhaustive over A_min-available surface enrichments
(negative_route_pruning).

**Load-bearing wall:** the Lattice axiom's explicit withholding of any boundary
condition (and of dynamics / orientation), an EXPLICIT OPEN GATE. The only
enrichment with a genuine sub-`S4` axis-selecting stabilizer (E7: per-axis `Z2`
BC datum `(A,P,P,P)`, stabilizer = `S3` fixing axis 0) is precisely a
boundary-condition datum A_min refuses to supply, and it is itself
`S4`-transportable (a `G_bare` element maps `(A,P,P,P)` onto `(P,A,P,P)`,
transport resid 0). Every enrichment A_min DOES supply has a joint stabilizer
that is **either full `S4` (isotropic) or trivial (a symmetric, non-axis-selecting
break of W)** and selects no axis: the qubit reality grading, staggered `η`
sectors and their curvature 2-cocycle, and additive scalar record readout are
`S4`-isotropic, while the cubic graph (E2) and face-diagonal graph (E8) actually
BREAK W (trivial joint stabilizer) but axis-symmetrically. NONE is
one-axis-selecting.

**Authority:**
`SINGLE_CLOCK_AXIS_DATUM_S4_TRANSPORTABLE_NATIVE_REDUCTION_NARROW_NO_GO_NOTE_2026-06-17.md`
(retained_no_go, S4 transitive + BC datum transportable);
`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`
(retained_no_go, sharpened pin = per-axis `Z2` BC-asymmetry datum);
`docs/MINIMAL_AXIOMS_2026-06-05.md` (Lattice supplies no boundary condition /
dynamics / metric; boundary condition and dynamics are EXPLICIT OPEN GATES).

### Even-extent scope boundary (recorded from R-N4-AUT)

The 384-element `|G_bare|` certificate and the full enrichment table are computed
on the **EVEN-extent** cubic staggered block. The odd-`L` falsifier returns
resid 6.000 (matches the s4-branch). The exhaustive-`S4`-orbit conclusion and the
enrichment table are therefore scoped to even extent; odd extent is a separate
surface not covered by this certificate.

---

## Machine-certificate index (runners by path + PASS/FAIL)

| route | clause | runner (absolute path) | cached log | PASS/FAIL | outcome |
|---|---|---|---|---|---|
| R-N5-IRR | N5 / B-AXIS.3 | `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n5_irreducibility_factor_clock_2026_06_20.py` | `logs/runner-cache/single_clock_n5_irreducibility_factor_clock_2026_06_20.txt` | PASS=36 FAIL=0 | walled_named |
| R-N4-REGDIR | N4 | `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.py` | `logs/runner-cache/single_clock_registration_direction_bridge_n4_regdir_2026_06_20.txt` | PASS=20 FAIL=0 | relocated_to_open_gate |
| R-N2b-JOINT | N2b / B-AXIS.1b | `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n2b_joint_clock_unit_check_2026_06_20.py` | `logs/runner-cache/single_clock_n2b_joint_clock_unit_check_2026_06_20.txt` | PASS=18 FAIL=0 | walled_named |
| R-N4-AUT | N4 / B-AXIS.2 | `/Users/jonBridger/tp-audit-bridge-20260620/scripts/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.py` | `logs/runner-cache/single_clock_n4_aut_enrichment_stabilizer_2026_06_20.txt` | PASS=17 FAIL=0 | walled_named |

**Aggregate: 4 routes, 91 checks, PASS=91 FAIL=0, cracks=0.**

---

## N1 / N7 honesty impact

- **N1 (≥5-route enumeration):** the four "live-positive but never built" flags in
  `ROUTE_PORTFOLIO.md` / `NO_GO_LEDGER.md` are now honestly-run outcomes backed by
  runners. New distinct route mechanisms added to the enumeration:
  (i) source-surface transfer irreducibility (R-N5-IRR — transfer is maximally
  reducible, factors are not gauge); (ii) record-accumulation / Lieb-Robinson
  causal-cone monotone (R-N4-REGDIR — ball not cone; cone transports with H);
  (iii) joint two-rate-gate unit-pinning (R-N2b-JOINT — exact 1-parameter gauge);
  (iv) full-automorphism-group enrichment search distinct from all transport-only
  routes (R-N4-AUT — `|G_bare|=384`, S4-transitive, every A_min enrichment's joint
  stabilizer is full-S4 or trivial, NONE one-axis-selecting). A consolidated
  B-AXIS no-go is therefore NOT premature on the
  enumeration count.
- **N7 (steelman weak points):** the strongest pro-derivation moves were built and
  falsified, not deferred. "record-production singles out the evolution
  direction" → answered: production per se is exchange-symmetric, its directional
  content is a supplied arrow / pointer OPEN-GATE datum. "a richer surface breaks
  W" → answered by computing the actual 384-element automorphism group; every
  A_min enrichment's joint stabilizer is full-S4 or trivial (E2/E8 do break W, but
  axis-symmetrically), and the only one-axis-selecting enrichment is a supplied BC
  datum that is itself transportable. "the supplied transfer is
  irreducible" → answered: it is maximally factorized; exclusion needs an
  unsupplied physical-clock-admission ray. "two rate gates jointly pin the unit" →
  answered: exact ratio-only gauge.

**No crack on any route. B-AXIS remains a live wall.** All four residuals
relocate to the record-production-dynamics / emergent-dynamics / boundary-
condition OPEN GATES of `MINIMAL_AXIOMS_2026-06-05.md`, or wall on
Lattice no-metric-scale / Record no-time-metric. This note supports — but does
not itself constitute — a later consolidated no-go. Independent audit lane is the
sole status authority.
