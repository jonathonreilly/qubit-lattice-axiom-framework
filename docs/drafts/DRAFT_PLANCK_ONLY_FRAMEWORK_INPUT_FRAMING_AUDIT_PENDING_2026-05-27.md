# [DRAFT — PARKED] Planck as Framework's Sole Dimensionful Input — Audit-Pending Synthesis

**Date:** 2026-05-27
**Status:** 🛑 **DRAFT — PARKED. DO NOT TREAT AS PUBLICATION SURFACE.**
**Location:** `docs/drafts/` — explicitly OUTSIDE `docs/publication/`
**Type:** planning document / future-state synthesis
**Status authority:** independent audit lane only. **Every projection in this
note depends on audit ratification of underlying PRs that have not happened yet.**

## ⚠ Why this note is parked as DRAFT (read first)

This note describes a future state of the framework that **does not exist on
live `main` yet**. It synthesizes the cumulative bounded-closure posture of
the 2026-05-25 → 2026-05-27 hierarchy attack, but every claim about
"reduced axiom surface", "Tier-A retirement", or "Planck-only minimum"
depends on PRs that are sitting unratified in the audit pipeline.

### What's actually on live main (as of 2026-05-27)

- `MINIMAL_AXIOMS_2026-05-20.md`: A1 (per-site qubit) + A2 (cubic lattice Z³)
  — **A2 is still a separate axiom**
- `tier_a_admissions.json`: `genuine_admitted_input_count: 4` (P1, AC_φλ, S, θ
  all as derivation_targets / not_a_node) — **registry edits #1983, #1984 not
  merged**
- AC_φλ retirement (#1969) and θ retirement (#1978) **gated on capstones**
- 24+ hierarchy bounded-closure PRs (#1991-#2046) **all unratified**

### What this note projects

- A1 reduces to qubit on 3D Euclidean substrate (via PR #2046 partial A2 collapse + identification clarification commit)
- Tier-A registry collapses to `{S = M_Pl}` (post #1983, #1984, #1969, #1978 ratification)
- Hierarchy primitives P1-P4 in bounded-closure (post the 24+ PR ratifications)
- (4π)^-16 chain in 7-named-premise form
- F2 2-loop residual confirmed at order-of-magnitude

**The projections are honest** — they describe what the publication surface
*will* look like IF the audit pipeline ratifies the queued work cleanly. But
the projections are not the publication surface itself; they are a
forward-looking synthesis kept in `docs/drafts/` until ratification happens.

### When to migrate this back to `docs/publication/`

When all of the following ratify on the live audit ledger:
1. PR #1983 (P1 → stated_principle reclassification)
2. PR #1984 (S → empirical_anchor reclassification)
3. PR #1969 (AC_φλ Tier-A retirement) — gated on Codex capstone #1959-#1965
4. PR #1978 (θ Tier-A retirement) — gated on Track A capstone #1974-#1981
5. The 24+ hierarchy chain PRs (#1991-#2046, including #2026 P2 bounded closure, #2030 F2 confirmation, #2046 A2 partial collapse)

At that point, this note's projections become ACTUAL framework state and the
synthesis can be migrated back to `docs/publication/ci3_z3/` as the
publication-surface mic-drop framing. Until then it stays here as a planning
document.

### What this draft does NOT do

- Does **not** introduce new axioms, admissions, or vocabulary
- Does **not** assert retained-grade on any individual row
- Does **not** modify the live publication surface (`INPUTS_AND_QUALIFIERS_NOTE`,
  `ARXIV_DRAFT`, etc.)
- Does **not** consume PDG values as load-bearing inputs
- **Source-side `proposal_allowed: false`** — this is a draft / planning
  document, not a source-note proposal for audit ratification

---

## Original synthesis content (unchanged below — describes the post-audit projection)

## 0. Axiom surface and dimensionality convention

### 0.1 The honest axiom surface

After the 2026-05-25 → 2026-05-27 hierarchy attack + PR #2046 partial
collapse of A2 + PR #1983 reclassification of P1, the framework's
**honest minimum** is:

| Component | Class | Role |
|---|---|---|
| **A1** | structural | per-site qubit at discrete sites of a 3D Euclidean substrate — packages qubit + spatial-3D identification + discreteness as one substrate axiom |
| **P1** (observable principle) | stated_principle (post PR #1983 audit) | scalar observables are additive over independent subsystems; forces `W = log|det(D+J)|` readout |
| **M_Pl** | empirical anchor | sole dimensionful input — `1/a = M_Pl ≈ 1.22 × 10¹⁹ GeV` (= the Z³ lattice spacing in human units) |

Plus the **retained derivation chain** (no admissions):
- anomaly inflow forces `D_temporal = 1` (PR #2015 + ANOMALY_FORCES_TIME)
- bounded sign-ε closure forces Lorentzian `Cl(3,1)` signature (PR #2026)
- the 10 algebraic d=4 witnesses (PRs #2004-#2013) inherit the same chain

That's it. **One structural substrate axiom + one observable-readout principle
+ one dimensionful translation = whole framework.**

### 0.2 Why "qubit alone forces D=3" is not quite right

A single qubit lives in `C²` with internal symmetry `SU(2)`. Mathematically,
`SU(2) ≅ Spin(3)` is the double cover of `SO(3)` — the rotation group of 3D
space — but **isomorphism is not identification**. A qubit's `SU(2)` could
abstractly be the spin-double-cover of any 3D space, or an internal symmetry
with no spatial meaning.

The bridge from "qubit internal SU(2)" to "qubit's algebra IS the 3D spatial
rotation algebra" is the **internal-external symmetry merger**: the qubit's
local algebra at site `x` IS the algebra of spatial rotations around `x`. This
identification is implicit in the framework's "Cl(3,0) reading" of A1 —
calling the qubit's algebra `Cl(3,0)` already presupposes signature `(3,0)` =
3 positive spatial directions.

Three honest framings of A1:

| Framing | What's in A1 | What's separately needed |
|---|---|---|
| **(a) Spatial-explicit (canonical)** | "qubit at each site of a 3D Euclidean substrate" | discrete translations (small, in P1 below) |
| (b) Algebra-only | "per-site qubit, internal algebra Cl(3,0)" | discrete translations + internal-external identification |
| (c) Merger-explicit | "qubit at each site, qubit algebra = local spatial-rotation algebra" | discrete translations |

**Framing (a) is the canonical reading of `MINIMAL_AXIOMS_2026-05-20`** ("qubit
at every site of `Z^3`"). The `Z^3` clause packages the 3D-spatial structure
into A1 explicitly. The "Cl(3,0) reading" is the equivalent phrasing under
the merger identification.

PR #2046 derived: **GIVEN A1 (under any of (a)/(b)/(c)) + discrete translations,
the lattice is forced to be primitive cubic `Z^3`** (Bravais cell selection
from O_h symmetry + lattice constants). The "cubic" part collapses out of A2;
the "discrete" part remains a small named premise.

### 0.3 Dimensionality convention

The framework's accepted spacetime is `D = 3+1` — three spatial dimensions
(from A1) plus one temporal dimension (emergent via Wick rotation, with
**Lorentzian signature `(3,1)`** forced from primitives by the bounded sign-ε
closure of PR #2026). The relevant Clifford algebra is **`Cl(3,1) ≅ M_4(ℝ)`**
(Cartan-Bott cell at signature `(3,1)`), NOT the Euclidean `Cl(4,0) ≅ M_2(ℍ)`
cell.

When this note (and the cited PRs) refer to "d = 4" or "d_spacetime = 4", the
intended reading is always **D = 3+1 Lorentzian**, post-Wick-rotation to
Euclidean `Z^4` for lattice computation only. The Lorentzian-vs-Euclidean
distinction matters because:

- The 10 algebraic witnesses (PRs #2004-#2013) all hold for D = 3+1 specifically
  via the Cl(3,1) Cartan-Bott cell identification (PR #2007) and the bounded
  sign-ε closure (PR #2026). Cl(4,0) Euclidean is excluded by unitarity vs
  contraction-semigroup (PR #2026 §3-§4).
- The 7/8 fermion/boson Stefan-Boltzmann ratio (PRs #1998, #2000) is the d=4
  Fermi-Dirac vs Bose-Einstein integral ratio — which is computed on
  Wick-rotated Euclidean `Z^4`, but the physical content (APBC fermion vs PBC
  boson Matsubara periodicities) is the D = 3+1 Lorentzian content.
- The Drouffe-Zuber strong-coupling character coefficients (PR #2040, c_6 = 24)
  count closed-surface graphs in d_spacetime = 4. This is the same number for
  D = 3+1 Euclidean lattice computation, since the graph enumeration depends
  only on the *spacetime* dimension count, not on the metric signature. **The
  framework's `Z^3` spatial substrate (D_spatial = 3 alone) does not change
  c_6** because the relevant dimension for character-expansion graph counting
  is `d_spacetime = D = 3+1 = 4`, post-Wick-rotation to Z⁴ for lattice
  computation.

**Throughout the rest of this note and the cited PRs, please read "d=4" as
"D=3+1 Lorentzian, Wick-rotated to Euclidean Z⁴ for lattice computation."**

## 1. Headline claim (framing only, not a theorem)

> **The Cl(3)/Z³ framework takes the Planck mass `M_Pl` as its sole
> dimensionful input.** The structural axioms are:
> 1. **A1**: qubit at each discrete site of a 3D Euclidean substrate (= "Cl(3,0)
>    per-site algebra" under the internal-external merger reading)
> 2. **P1**: scalar observables are additive over independent subsystems
>    (forces the `W = log|det(D+J)|` readout — stated principle post PR #1983)
>
> The temporal direction (D_temporal = 1) is **derived**, not axiomatic:
> anomaly inflow (PR #2015) + bounded sign-ε closure (PR #2026) force `D = 3+1`
> with Lorentzian signature `Cl(3,1)`. The cubic structure of A2 (formerly
> separate axiom) is **derived** from A1 + small (P1) discreteness premise
> (PR #2046). Every dimensionless ratio in the Standard Model derives from
> this substrate + the bounded forcing chain. Translating to human units
> (kg/m/s) using a single human-unit value of `1/a = M_Pl ≈ 1.22 × 10¹⁹ GeV`
> reconstructs `v = 246.28 GeV` (vs PDG `246.22 GeV`), with the residual
> `0.0255%` at the predicted 2-loop running scale `(α_LM/π)² ≈ 0.083%`
> (confirmed at order-of-magnitude;
> `HIERARCHY_TWO_LOOP_RESIDUAL_F2_SCALE_TEST_NARROW_BOUNDED_NOTE_2026-05-27`).

This is **not a derivation of the number `1.22 × 10¹⁹ GeV`** — that would
require a comparator unit and is logically impossible from pure mathematics.
It is the same epistemic posture as:

- General relativity: `G_Newton` is the unique dimensionful coupling; the
  Einstein-Hilbert action's metric structure is fixed; the human-unit value
  `G = 6.67 × 10⁻¹¹ m³/kg/s²` is a translation-table entry.
- Quantum mechanics: `ℏ` is the unique dimensionful action quantum; the
  commutator structure `[x, p] = iℏ` is fixed; the human-unit value
  `ℏ = 1.054 × 10⁻³⁴ J·s` is a translation-table entry.

The framework's content is the **structure** of `A_min`, the **bounded chain**
from `A_min` to every dimensionless ratio, and the **single dimensionful
translation** `M_Pl ↔ 1/a` where `a` is the Z³ lattice spacing.

## 2. Tier-A admissions registry — current state vs post-audit projection

The framework's `docs/audit/data/tier_a_admissions.json` registry tracks the
genuine non-axiom admitted inputs. Two passes were applied during the session
window:

### Pre-session live state (`genuine_admitted_input_count: 4`)

| id | class | what |
|---|---|---|
| P1 | derivation_target | observable principle (scalar additivity) |
| AC_φλ | derivation_target | generation mass pattern + species bridge |
| S | not_a_node (pervasive) | scale-setting empirical anchor |
| θ | derivation_target | QCD vacuum angle = 0 |

### Post-audit projection (after PRs #1969, #1978, #1983, #1984 ratify)

| id | class | what |
|---|---|---|
| **S** | **`empirical_anchor`** = M_Pl | **the sole dimensionful input** |
| P1 | `stated_principle` | observable-readout principle (NOT an input, NOT a derivation target — a structural assumption about how scalar observables compose) |
| Y₀, g₀ | `conventions` | vacuous rescaling (already classified) |
| AC_φλ | retired | gated PR #1969 + Codex capstone #1959-#1965 |
| θ | retired | gated PR #1978 + Track A capstone #1974-#1981 |

After audit ratification of these registry edits, the `derivation_targets`
category becomes empty. The `empirical_anchors` category collapses to one
entry: **`{S = M_Pl}`**. The `stated_principles` category contains P1 — a
structural assumption about observable extraction (scalar additivity), not a
numerical input or derivation target.

**Note that P1 is NOT eliminated** — it remains a stated principle. The
framework is honest that scalar additivity is assumed, not derived. P1 is
not in the same epistemic class as M_Pl (which is a number) nor as A1 (which
is a substrate). It is a third kind of axiom: an observable-extraction rule.
The mic-drop claim "M_Pl is the sole *dimensionful* input" is honest; the
claim "M_Pl is the sole admission" would be overreach because P1 (algebraic
admission) and A1 (structural admission) are also present.

## 3. The hierarchy formula bounded chain (`v = M_Pl × (7/8)^(1/4) × α_LM^16`)

The session shipped a 26-PR bounded-closure chain demonstrating that **every
factor on the RHS derives from `A_min` + Cl(3) structure**, with `M_Pl` as the
sole carry of dimensionful information.

### Primitive-by-primitive status

**P1 (M_Pl import via Wald-Noether):**
- Algebraic skeleton: `BH_QUARTER_WALD_NEWTON_COEFFICIENT_NARROW_THEOREM_NOTE_2026-05-10` (retained)
- Coframe-response premise: PR #1991 (accepted-premise bridge)
- Boundary/action-density premise: PR #1994 (accepted-premise bridge)
- **Status:** bounded closure pending audit ratification of the two named-premise bridges

**P2 (Wick rotation `Z^3` → Lorentzian `D = 3+1` (Cl(3,1)) + N=16 species count):**
- **10 `D = 3+1` (i.e. `d_spacetime = 4` Lorentzian, post-Wick-rotation) algebraic witnesses** (1 pre-existing retained + 9 new awaiting audit):
  W_A so(4)≅su(2)⊕su(2) (#2004); W_B ω∧ω top-form (#2005); W_C binom(d,2)=2(d-1) (#2006);
  W_F Cl(3,1)≅M_4(ℝ) Cartan-Bott (#2007); W_D Chern-character k=2 (#2008);
  W_G Yang-Mills marginality (#2011); W_E Klein-four V_4×V_4 (#2012);
  W_H Hodge *²=±id (#2013); plus pre-existing Clifford-volume chirality-even.
- ANOMALY_FORCES_TIME parent on canonical promotion path: PR #2015 ABJ accepted-premise bridge
- **Bounded sign-ε closure:** PR #2026 — composition `(C-Ext PR #2022) + (C-Sc) + (C-RP) + (C-Aft) + (P-OS)` forces `ε = -1` (Cl(3,1) Lorentzian) by unitarity-vs-contraction-semigroup argument
- (P-OS) Osterwalder-Schrader bridge: PR #2028 derives the finite-dim `T^n ↔ U(t)` correspondence from framework companions; no new admission introduced
- ABJ U(1)_Y branch partial advance: PR #2027 (Fujikawa Jacobian on Z⁴ staggered)
- **Status:** bounded closure on 5 named upstreams, with (P-OS) now framework-derived (#2028) and the remaining (P1') overlap-Dirac residual narrowed by #2027

**P3 (`α_bare = 1/(4π)` origin):**
- Full **7-named-premise audit-readable chain**:
  1. `g_bare = 1` accepted-premise (W2 H_unit residue, PR #2001)
  2. Plancherel substrate-internal `1/(4π)` (PR #2002)
  3. BZ-volume `(2π)³` standalone narrow (PR #2010)
  4. Maradudin asymptotic accepted-premise (PR #2014)
  5. I1 static-source readout accepted-premise (PR #2018)
  6. I2 `α := g²/(4π)` accepted-premise (PR #2023)
  7. I3 `Tr(T_aT_b) = δ_{ab}/2` + Wilson no-rescaling accepted-premise (PR #2020)
- **Status:** bounded closure on 7 named premises, every premise in canonical
  audit-readable form. No continuum-Fourier-measure import remains in the
  load-bearing path. Same posture as the audit-ratified α=1/3 hypercharge
  bridge.

**P4 (EWSB observable identification):**
- PR #1992 (bounded narrow theorem with curve-fit defense in §5.1)
- **Status:** bounded closure on retained EW gauge-mass diagonalization + retained
  dimensional fourth-root compression + retained Riemann-Dirichlet anchor +
  retained `α_LM` geometric-mean identity, under four admitted-context inputs C1-C4

### 0.0255% residual confirmation

PR #2030 verified PR #2000's falsifiable F2 prediction: the 0.0255% residual is at
the 2-loop running scale `(α_LM/π)² = 0.083%`. Ratio `0.31` is within factor 4
(passes the within-decade and within-factor-4 thresholds); neither falsifier
triggered. Independent cross-check vs `YT_QFP_INSENSITIVITY_SUPPORT_NOTE` 1-vs-2-loop
SM RGE shift on y_t(v): the v residual is `~1.06%` of that — consistent with bulk
2-loop running absorbed into tree-level α_LM^16 exponentiation.

This is a **quantitative analytic prediction landing in the right range** — not
a curve-fit defense.

## 4. The lattice plaquette `<P> = 0.5934` — analytic status

The hierarchy formula's `α_LM = α_bare / u_0 = (1/(4π)) / <P>^(1/4)` uses the
Wilson plaquette `<P>` at canonical β=6 (the `g_bare = 1` normalization, which
is itself in accepted-premise form via PR #2001 + retained W1+W2 chain).

### Two complementary analytic attacks were shipped this session

| Route | PR | Result | Gap to MC `0.5934` |
|---|---|---|---|
| Weak-coupling tadpole-improved + Padé (NSPT through n=16) | #2039 | 0.911 | **+53.4%** (gluon-condensate territory) |
| Strong-coupling SU(3) character + Padé[3/3] | #2040 | **`3/5` = 0.6000** | **−1.11%** |

### Result

The strong-coupling Padé[3/3] gives the **exact rational `3/5`** within 1.1% of
the lattice Monte Carlo measurement at canonical β=6. Cross-checked via
conformally-mapped variables at two distinct α values. The weak-coupling route
**honestly bails** at the QCD IR-renormalon onset (`n* ≈ 4.57`) — the 53%
residual is the standard non-perturbative gluon-condensate contribution. This
two-sided bracketing diagnoses the structure of the non-perturbative content.

The 3/5 strong-coupling prediction is conditional on the SU(3) character coefficient
`c₆ = 24` (Drouffe-Zuber 1983 tabulation). A framework-internal derivation of
c₆ = 24 on the framework's retained SU(3) primitives + d=4 forcing chain
(post-Wick-rotation via PR #2026) is in flight and would close this conditional.

### Spacetime vs spatial dimensionality (D = 3+1, not abstract d=4)

The character expansion coefficients `c_n` count closed-surface lattice graphs
touching a plaquette in **`d_spacetime` = 4 = (3 spatial + 1 time)**. The framework's
**spatial** substrate is `Z^3` (per A2 of A_min), and the temporal direction is
emergent via Wick rotation with **Lorentzian signature `(3,1)`** forced from
primitives by PR #2026 (the bounded sign-ε closure rules out Cl(4,0)
Euclidean via unitarity-vs-contraction-semigroup).

The Drouffe-Zuber `c_6 = 24` is the `D = 3+1` coefficient (Lorentzian
spacetime, post-Wick-rotation to `Z^4 = Z^3 × Z` for lattice computation only;
the metric signature does not affect graph-counting in the character
expansion). **D = 3 spatial alone does not change c_6** because the relevant
dimension for the character-expansion graph enumeration is `d_spacetime = 4`,
which the framework's bounded `D = 3+1` forcing chain (PR #2026 + 10
algebraic witnesses #2004-#2013) provides. The Padé[3/3] = 3/5 result
therefore inherits the same `D = 3+1` chain already required by P2 closure.

## 5. What remains genuinely open (research-grade, multi-month)

After this session's bounded-closure landings, the truly research-grade items
that remain open — beyond audit-lane ratification — are:

| Item | Narrowed from | Current status |
|---|---|---|
| (P1') overlap-Dirac on Z⁴ for non-zero U(1)_Y index | original monolithic ABJ admission | narrowed by PR #2027 to Adams 2002 / Lüscher 1998 lattice-overlap-Dirac |
| Non-abelian ABJ branches (SU(2), SU(3) traces) | original monolithic ABJ admission | scoped; PR #2027 closes only U(1)_Y |
| Full infinite-dim Osterwalder-Schrader reconstruction (Wightman fields, cluster decomposition) | (P-OS) admission | PR #2028 closes only the finite-dim `T^n ↔ U(t)` bridge needed by PR #2026 |
| Sub-factor-2 F2 precision | `(α_LM/π)²` order-of-magnitude check | PR #2030 confirms at factor-4; tightening needs full non-perturbative YT_P2 staircase |
| Strong-coupling Padé[3/3] = 3/5 precision (1.1% → tighter) | `<P>` MC value | PR #2040 ships the algebraic 3/5; closing the residual requires higher-order character coefficients |

None of these block the **bounded-closure posture** at the audit-lane level. They
are targets for the next research session.

## 6. Publication-surface framing

The `INPUTS_AND_QUALIFIERS_NOTE` and `PREDICTION_SURFACE_2026-04-15` should
continue to enumerate explicit external inputs (T_CMB, H_0, PDG lepton masses,
etc.) for cosmology-facing rows. **The hierarchy chain shipped this session
does not add new external inputs** — the M_Pl = 1.22 × 10¹⁹ GeV value already
in the publication surface IS the framework's sole dimensionful anchor, now
backed by an end-to-end bounded chain.

The publication front-door framing is therefore the headline claim of §1:

> The framework derives every dimensionless ratio in the Standard Model from
> A1 (per-site qubit at discrete sites of a 3D Euclidean substrate) + P1
> (scalar additivity readout principle). The single dimensionful translation
> is `M_Pl ↔ 1/a`. Human-unit `M_Pl = 1.22 × 10¹⁹ GeV` reconstructs
> `v = 246.28 GeV` (vs PDG `246.22 GeV`), with the residual at the predicted
> 2-loop running scale.

**Comparison to other frameworks' axiom surfaces:**

| Framework | Algebraic/structural admissions | Dimensionful inputs |
|---|---|---|
| **GR** | spacetime topology (4-manifold) + Lorentzian metric existence + diffeomorphism invariance + Einstein equations as field eqs | `G_Newton` |
| **QM** | complex Hilbert space + bounded observables + Born rule + unitary dynamics | `ℏ` |
| **SM** | gauge group `SU(3) × SU(2) × U(1)` + 3 fermion families + Higgs doublet + Yukawa matrices + CKM/PMNS structure | ~19 free parameters |
| **Cl(3)/Z³ framework** | **A1 (qubit-on-3D-substrate) + P1 (scalar additivity) + (P1-discreteness from PR #2046)** | **`M_Pl`** |

The framework's admissions are **strictly comparable in count** to GR or QM
(one substrate + one observable-readout) and **strictly less in count** than
the Standard Model. The dimensionful surface is **strictly one number**,
matching GR (`G`) and QM (`ℏ`) — but with the difference that the framework
*derives* every dimensionless ratio that GR/QM/SM admit as separate inputs.

This framing is consistent with GR (`G_Newton` is structural, not free) and QM
(`ℏ` is structural, not free). The framework's content is the structure of A1
+ P1 plus the bounded chain — not a number derived from nothing.

## 7. What this synthesis note does NOT do

- Does **not** introduce new axioms or admissions
- Does **not** add Tier-A registry entries
- Does **not** promote any individual row's `effective_status`
- Does **not** introduce new repo vocabulary
- Does **not** consume PDG values as load-bearing inputs (cosmology/lepton-mass
  inputs already on the public paper surface remain explicit external inputs;
  this note does not subsume them)
- Does **not** claim the lattice plaquette `<P>(β=6) = 0.5934` is fully
  analytically derived — only that the strong-coupling Padé[3/3] = 3/5 result
  (PR #2040, awaiting framework-internal c_6 derivation) lands within 1.1% on
  the same retained d=4 forcing chain

## 8. Cross-references

- `MINIMAL_AXIOMS_2026-05-20.md` — accepted A_min surface (A1 + A2)
- `INPUTS_AND_QUALIFIERS_NOTE.md` — public input ledger (cosmology, lepton-mass)
- `ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23.md` — registry note explaining
  the pre-session 4-admission state
- `docs/audit/data/tier_a_admissions.json` — machine-readable registry (live state)
- `HIERARCHY_FORMULA_HONEST_STATUS_NOTE_2026-05-10.md` — pre-session honest
  status of the hierarchy formula (canonical 4-primitive enumeration)
- `HIERARCHY_FORMULA_EW_VEV_OBSERVABLE_IDENTIFICATION_BRIDGE_BOUNDED_NOTE_2026-05-26.md` (PR #1992) — P4 bridge
- `HIERARCHY_SEVEN_EIGHTHS_QUARTER_FERMION_BOSON_SCALE_CONVERSION_BRIDGE_BOUNDED_NOTE_2026-05-26.md` (PR #2000) — `(7/8)^(1/4)` structural identification + F2
- `P2_WICK_ROTATION_SIGN_EPSILON_CLOSURE_NARROW_THEOREM_NOTE_2026-05-27.md` (PR #2026) — bounded P2 closure
- `PLAQUETTE_BETA6_STRONG_COUPLING_CHARACTER_NARROW_THEOREM_NOTE_2026-05-27.md` (PR #2040) — strong-coupling 3/5 result
- `PLAQUETTE_BETA6_PERTURBATIVE_DERIVATION_BOUNDED_OBSTRUCTION_NOTE_2026-05-27.md` (PR #2039) — weak-coupling honest no-go
- `HIERARCHY_TWO_LOOP_RESIDUAL_F2_SCALE_TEST_NARROW_BOUNDED_NOTE_2026-05-27.md` (PR #2030) — F2 confirmation

## 9. Path forward

The work to consolidate this framing into publication-grade prose is:

1. **Update `ARXIV_DRAFT.md`** to lead with §1's headline claim explicitly,
   citing the bounded-closure chain.
2. **Refresh `CLAIMS_TABLE.md` / `CLAIMS_TABLE_EFFECTIVE_STATUS.md`** to add
   the four hierarchy-primitive bounded-closure rows + the F2 confirmation row +
   the strong-coupling `<P>` prediction row.
3. **Refresh `DERIVATION_ATLAS.md`** to include the 26-PR bounded chain.
4. **Update `EXTERNAL_REVIEWER_GUIDE.md`** to explicitly flag the GR/QM
   epistemic precedent — preempting the reviewer reflex of "but you still
   have one admission, M_Pl".

These updates depend on the audit lane ratifying the 26+ PRs shipped this
session. Until then, this note carries the synthesis without promoting any
individual row's status.

---

**This is a framing note for the publication surface only.** Audit lane retains
exclusive authority over `effective_status` on every cited row.
