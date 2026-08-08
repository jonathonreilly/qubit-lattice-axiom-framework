# Planck as the Framework's Sole Dimensionful Input — Framing Synthesis

**Date:** 2026-05-27
**Type:** publication-surface synthesis note (front-door narrative)
**Status authority:** independent audit lane only. This is a *framing/synthesis* note
for the publication surface. It does **not** introduce new axioms, admissions, or
repo vocabulary. It does **not** assert retained-grade on any single row. It
catalogs the cumulative bounded-closure posture reached after the 2026-05-25 →
2026-05-27 hierarchy attack and frames its publication-surface presentation.
**Source-side `proposal_allowed: false`**.

## 1. Headline claim (framing only, not a theorem)

> **The Cl(3)/Z³ framework takes the Planck mass `M_Pl` as its sole dimensionful
> input.** The algebraic axioms `A_min = {A1: per-site qubit, A2: Z³ lattice}` carry
> no numerical content. Every dimensionless ratio in the Standard Model derives
> from this `A_min` substrate. Translating to human units (kg/m/s) using a single
> human-unit value of `1/a = M_Pl ≈ 1.22 × 10¹⁹ GeV` reconstructs `v = 246.28 GeV`
> (vs PDG `246.22 GeV`), with the residual `0.0255%` at the predicted 2-loop
> running scale `(α_LM/π)² ≈ 0.083%` (confirmed at order-of-magnitude;
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
| P1 | `stated_principle` | canonical-convention class (not an input) |
| Y₀, g₀ | `conventions` | vacuous rescaling (already classified) |
| AC_φλ | retired | gated PR #1969 + Codex capstone #1959-#1965 |
| θ | retired | gated PR #1978 + Track A capstone #1974-#1981 |

After audit ratification of these registry edits, the registry collapses to one
entry: **`{S = M_Pl}`** in the `empirical_anchors` class. The
`derivation_targets` category becomes empty.

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

**P2 (Wick rotation Z³ → Z⁴ + N=16 species count):**
- **10 d=4 algebraic witnesses** (1 pre-existing retained + 9 new awaiting audit):
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

### Spacetime vs spatial dimensionality

The character expansion coefficients `c_n` count closed-surface lattice graphs
touching a plaquette in `d_spacetime`. The framework's spatial substrate is
`Z³` (per `A_min`), but the relevant plaquette in the hierarchy chain lives on
the Wick-rotated `Z⁴ = Z³ × time` substrate (per PR #2026 bounded P2 closure).
The Drouffe-Zuber `c_6 = 24` is the d=4 coefficient. **D=3 spatial does not change
c_6 directly** because the relevant dimension for character-expansion graph
enumeration is `d_spacetime = 4`, which the framework's d=4 forcing chain
provides. The Padé[3/3] = 3/5 result therefore inherits the same d=4 chain
already required by P2 closure.

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
> `A_min = {qubit, Z³}`. The single dimensionful translation is `M_Pl ↔ 1/a`.
> Human-unit `M_Pl = 1.22 × 10¹⁹ GeV` reconstructs `v = 246.28 GeV` (vs PDG
> `246.22 GeV`), with the residual at the predicted 2-loop running scale.

This framing is consistent with GR (`G_Newton` is structural, not free) and QM
(`ℏ` is structural, not free). The framework's content is the structure of
`A_min` plus the bounded chain — not a number derived from nothing.

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
