# Scale Axis — Per-Sector Overall Mass Scales Scoping Note

**Date:** 2026-06-05
**Claim type:** meta (scoping; no new theorem, no audit status). Records
which per-sector absolute mass SCALES are RG/structure-derived vs free
Yukawa inputs, complementary to the already-mapped SHAPE (ratio) axis.
**Status authority:** independent audit lane only. This note does not set
or predict an audit outcome; it is a scoping/orientation note that
consolidates and cross-checks existing results on the framework surface
(retained and unaudited, with statuses called out individually below).
**Source-note proposal disclaimer:** scoping/meta note; no status promotion.
**Primary runner:**
[`scripts/scale_axis_per_sector_scales_2026_06_05.py`](../scripts/scale_axis_per_sector_scales_2026_06_05.py)
**Cache:**
[`logs/runner-cache/scale_axis_per_sector_scales_2026_06_05.txt`](../logs/runner-cache/scale_axis_per_sector_scales_2026_06_05.txt)

## 0. Scope and frame

Each fermion mass factors as **mass = (sector scale) × (within-sector
shape)**. The within-sector shape (Koide ratios `r = |b|²/a²`, phase
`θ = arg b` of the circulant `H = a I + b C + b̄ C²`) is the **SHAPE axis**,
mapped elsewhere (charged leptons pinned `r = 1/2, θ = 2/9`; quarks
contingent). This note addresses the orthogonal **SCALE axis**: the
absolute per-sector magnitude — the `I`-component `a`, i.e. the absolute
Yukawa magnitude of each sector (up-type/`m_t`, down-type/`m_b`,
charged-lepton/`m_τ`, neutrino/`m_ν`). The SCALE axis is dynamics-active:
it runs under the RG. **This note does not re-attack the ratios.**

The question: after RG running and the framework's gauge structure, which
sector scales are **derived** (top IR quasi-fixed-point; b–τ Yukawa
unification) and which remain **free** Yukawa inputs (honest count)?

All SM Yukawa/coupling values at low scale enter only as comparators or
running boundary conditions, never as derivation inputs to a framework
claim. The framework coupling packet (`α_LM`, `α_s(v)`, `v_EW`, `M_Pl`) is
imported from the canonical plaquette surface, identical to the existing
top-QFP no-go runner.

## 1. Q1 — Top scale: quasi-fixed-point + derived Ward boundary

**The top quasi-FP focusing is REAL.** Integrating the 1-loop SM
top-Yukawa RGE from `M_Pl` down to `v` for UV seeds
`y_t(M_Pl) ∈ {1, 2, 5, 10, 50}` (UV span 50×) collapses to an IR band of
fractional width ~7% — a **compression of ~47×**. This is the
Pendleton–Ross / Hill quasi-fixed-point: the QCD–Yukawa balance in
`β_{y_t} ∝ y_t(9/2·y_t² − 8 g_3² − …)` drives `y_t` toward an IR attractor
`y_t* ≈ 1.25` largely independent of its UV value. So **the top scale is
forced to be O(1)·v by UV-insensitivity** — a genuine structural feature,
not a free input in the usual sense.

**But the pure attractor lands ~27% HIGH.** On the framework coupling
packet, the focused band gives `y_t(v) ≈ 1.18…1.26`, hence
`m_t ≈ 205…219 GeV` — above the observed 172.7 GeV. The precise top mass
is therefore **not** delivered by the generic attractor alone; it needs a
specific UV boundary at the low end of the basin. (This reproduces the
existing — `unaudited` on the ledger —
[`QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10`](QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md).)

**The framework supplies the needed UV boundary — the lattice Ward
identity.** The chain
([`YT_ZERO_IMPORT_CHAIN_NOTE`](YT_ZERO_IMPORT_CHAIN_NOTE.md), now a
`decoration` under the `retained_bounded` declared-anchor subchain
[`YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN_NARROW_THEOREM_NOTE_2026-05-26`](YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN_NARROW_THEOREM_NOTE_2026-05-26.md))
fixes `y_t(M_Pl) = g_lattice/√6 = √(4π α_LM)/√6 ≈ 0.436` (NB: `g_lattice`
is the **lattice-bare** coupling at the cutoff, ≈ 1.067, **not** the
perturbatively-run SM `g_3(M_Pl) ≈ 0.49`). Running this down gives
`y_t(v) ≈ 0.950`, **m_t ≈ 165 GeV (1-loop, −4.2%)**; the full 2-loop +
color-projection chain refines this to **m_t ≈ 169.5 GeV (−1.84%)**.

**Honest Q1 verdict.** The top scale is the one sector scale that is
**derived-modulo-anchor**: the quasi-FP makes it O(1)·v insensitively, and
the *precise* value is set by the framework-derived Ward UV boundary
`y_t(M_Pl) = g_lattice/√6`. The auditable carrier of that chain is
`retained_bounded` (`YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN`), with the older
full numerical chain a `decoration` over declared anchors; two named
upstream-import gaps remain (the bounded plaquette insertion `⟨P⟩(β=6)` and
the `κ_EW = 0` matching rule). It is **not** a generic quasi-FP prediction;
it is "quasi-FP O(1) magnitude × derived UV anchor → target." This is the
strongest derived-scale result among the four sectors.

## 2. Q2 — Inter-sector hierarchy: b–τ unification vs absolute scale

The inter-sector magnitudes are `m_t/m_b ≈ 40`, `m_b/m_τ ≈ 2.4`,
`m_t/m_e ≈ 3×10⁵`. Two distinct questions: are these from gauge structure,
or independent free scales?

**(a) b–τ RATIO is a genuine structural relation.** `β_{y_b}` carries
`−8 g_3²` (color) while `β_{y_τ}` does not. Running the observed
`y_b/y_τ` UP from `v` to a GUT scale, the ratio moves
**1.56 (at v) → 0.64 (at 2×10¹⁶ GeV)** — i.e. it approaches unity at high
scale. Equivalently, running DOWN from a unified `y_b(M_GUT) = y_τ(M_GUT)`,
QCD enhances `y_b` relative to `y_τ`, generating the observed IR
`m_b/m_τ` from a structural ratio-1 boundary. This is the classic b–τ
Yukawa unification: the down/charged-lepton 3rd-generation **ratio** is a
real gauge-structural relation, reducing the independent-scale count by
one. (Exact unity is scheme- and scale-dependent and is sharper at 1-loop
SUSY scales; the 1-loop SM ratio reaches ~0.64 at 2×10¹⁶ GeV, clearly
converging toward 1 from the IR value 1.56 — the convergence is the
content, not a fitted unification scale.)

**(b) Absolute b SCALE is NOT fixed by unification — it's free.** Imposing
the species-uniform Ward boundary `y(M_Pl) = g_lattice/√6 ≈ 0.436` on ALL
species (the "everything unified at the cutoff" reading) and running down
gives **m_b ≈ 144 GeV — a 35× overshoot** of the observed 4.18 GeV, while
simultaneously dragging the top down to **m_t ≈ 149 GeV**. Both fail
together because the coupled (y_t, y_b) quasi-fixed-point pulls them to a
common ≈ 0.55 at `v`. This independently reproduces the existing
(`unaudited` on the ledger)
[`YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18`](YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md)
(m_b ≈ 145 GeV, 35×). The lesson: **unification constrains the b/τ ratio,
not the absolute b scale.** The absolute down-type scale is a free Yukawa
input (the framework treats `y_b` as empirical infrastructure in its top
chain).

**(c) QCD enhancement of quark vs lepton scales.** The color `−8 g_3²` in
the quark beta functions, with `α_s(v) ≈ 0.103` derived on the framework
plaquette surface, is exactly the mechanism that enhances quark Yukawas
relative to leptons in the IR (and underlies the bounded down-type
`m_s/m_b = [α_s(v)/√6]^{6/5}` ratio lane). This is a structural
**ratio/enhancement** statement — it shapes inter-sector ratios; it does
**not** by itself fix any sector's absolute scale.

## 3. Q3 — Honest residual free-scale count

| Sector | absolute-scale mechanism on the framework surface | scale status |
|---|---|---|
| up-type (`m_t`) | quasi-FP O(1)·v × **derived Ward UV boundary** `g_lat/√6` | **derived-modulo-anchor** |
| down-type (`m_b`) | b–τ ratio ties to lepton 3rd-gen; abs. scale NOT FP-set | free (absolute) |
| charged-lepton (`m_τ`) | b–τ ratio relates to `m_b` at GUT | free (absolute) |
| neutrino (`m_ν`) | no quasi-FP, no unification handle here | free |

**Count.** Start with 4 sector absolute scales (up, down, charged-lepton,
neutrino). The top scale is fixed by the quasi-FP + derived Ward anchor:
**−1 → 3**. The b–τ unification is one RATIO relation tying the
(down, charged-lepton) 3rd-generation magnitudes at the GUT scale, so it
removes one of that pair as independent: **−1 → 2**. The neutrino absolute
scale has no quasi-FP or unification handle on the current surface and
stays free.

**Honest residual: 2 independent free absolute scales** — one of
`{m_b, m_τ}` (the other set by it via b–τ), plus `m_ν`.

## 4. Verdict — derived vs free (honest)

- **DERIVED (genuine):** the **top** absolute scale, via the quasi-FP
  (O(1)·v UV-insensitivity, ~47× compression) combined with the
  framework-derived Ward UV boundary `y_t(M_Pl) = g_lattice/√6`
  → m_t ≈ 169.5 GeV (−1.84%). This is the single quasi-FP/anchor-predicted
  sector scale. Caveat: the auditable carrier is `retained_bounded`
  (declared-anchor subchain) with two named upstream-import gaps, so
  "derived" here means derived-modulo-those-anchors, not unconditional.

- **STRUCTURAL RELATION (genuine, reduces count):** **b–τ unification** —
  the down/charged-lepton 3rd-generation **ratio** is a real gauge-driven
  (`−8 g_3²`) relation, `y_b/y_τ` converging toward 1 at the GUT scale.
  It removes one independent magnitude from the (m_b, m_τ) pair.

- **FREE Yukawa inputs (honest):** the **absolute** down-type/charged-lepton
  scale (one of the pair after b–τ) and the **neutrino** absolute scale.
  Naive species-uniform unification at the cutoff is falsified by 35× on
  `m_b` (existing bottom-retention result), confirming these are not
  FP-fixed.

- **Honest residual count: 2** independent free absolute scales.

This is the SCALE-axis complement to the SHAPE axis: of the four sector
scales, **one is quasi-FP/anchor-derived (top)**, **one ratio relation is
structural (b–τ)**, and **two absolute scales remain free**.

## 5. Cross-references (existing surface, unmodified; ledger status noted)

- [`QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md`](QUARK_TOP_QFP_ATTRACTOR_ROUTE_NO_GO_NOTE_2026-05-10.md)
  (`unaudited`) — generic QFP attractor lands m_t ≈ 205–219 GeV; needs a
  derived UV boundary (reproduced in Q1).
- [`YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN_NARROW_THEOREM_NOTE_2026-05-26.md`](YT_DECLARED_ANCHOR_BOUNDED_SUBCHAIN_NARROW_THEOREM_NOTE_2026-05-26.md)
  (`retained_bounded`) — the auditable carrier of the derived Ward top
  chain; and its `decoration`
  [`YT_ZERO_IMPORT_CHAIN_NOTE.md`](YT_ZERO_IMPORT_CHAIN_NOTE.md) — Ward UV
  boundary `y_t(M_Pl) = g_lattice/√6` → m_t ≈ 169.5 GeV (two named import
  gaps).
- [`YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md`](YT_BOTTOM_YUKAWA_RETENTION_ANALYSIS_NOTE_2026-04-18.md)
  (`unaudited`) — species-uniform unification → m_b ≈ 145 GeV, 35×
  overshoot (reproduced in Q2c).
- [`CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md`](CHARGED_LEPTON_MASS_HIERARCHY_REVIEW_NOTE_2026-04-17.md)
  — each sector requires its own absolute pin when carried as a bounded
  package (consistent with the free-scale residual here).
- `cl3_koide_a1_probe_rg_fixed_point_2026_05_08_probe5.py` — establishes
  that the within-sector RATIO `|b|²/a²` has no matter-sector RG content
  (SHAPE axis), while affirming the three framework RG flows used here:
  Wilsonian gauge running, the EW-VEV staircase, and the top
  Pendleton–Ross focusing.

This note modifies no authority on the surface; PDG masses appear only as
comparators / running boundary conditions.
