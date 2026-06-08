# Lattice-Quantum-Record Framework

This repository is the current public working package for the
**Lattice-Quantum-Record Framework**: a discrete-physics program whose named
minimal premises are **Lattice**, **Quantum**, and **Record**. The front door is
deliberately status-first. It separates what the repo currently names as its
axioms, what the audit lane has ratified, what the publication package proposes,
what numbers are usable only with qualifiers, and which science lanes remain
open.

The canonical axiom memo is
[`docs/MINIMAL_AXIOMS_2026-06-05.md`](docs/MINIMAL_AXIOMS_2026-06-05.md).
Old `A1` / `A2` / `A3` labels are historical. New public wording should use
the repo name and axiom names above unless it is quoting older notes.

## Current Bottom Line

Status below reflects the generated audit refresh on **2026-06-08** after this
branch was rebased onto latest `origin/main`.

| Surface | Current state |
|---|---|
| Framework name | **Lattice-Quantum-Record Framework** |
| Minimal axioms | **Lattice**: `Z^3` nearest-neighbor cubic adjacency. **Quantum**: one qubit per site, equivalently one-site `M_2(C)` / real `Cl(3,0)`. **Record**: durable realized-outcome registration with finite scalar additivity in a fixed readout context. |
| Audit authority | The audit-derived `effective_status` in [`docs/audit/AUDIT_LEDGER.md`](docs/audit/AUDIT_LEDGER.md), not legacy author-side `retained` / `promoted` wording. |
| Generated front-door counts | [`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md): 3006 ledger rows; 1219 retained-grade rows including boxed decorations; 36 open gates; 1345 unaudited rows; 16 citation cycles. |
| Audit queue | 1347 pending rows, 24 ready rows, 16 cycle-break targets. |
| Publication gap | 440 distinct publication-table citations are not retained-grade in the audit-derived view. |
| Sharp forecast surface | Three conditional, currently unaudited falsifiable forecasts: PMNS `delta_CP` third-quadrant bracket, PMNS `theta_23` upper-octant prediction, and absolute Higgs-vacuum stability. |
| Open flagship science | Charged-lepton mass retention remains open, including Koide `Q = 2/3`, Brannen `delta = 2/9`, and the absolute charged-lepton scale. |
| Other critical open lanes | Hadron masses, atomic scales, non-top quark masses, neutrino quantitative closure, and `H_0` closure remain active open science lanes. |

The short practical rule is: a result is publication-usable as ratified science
only when its cited authority is retained-grade in the effective-status view.
Otherwise it is proposed, bounded, conditional, support-tier, a no-go, a
renaming/numerical match, or still unaudited.

## The Three Axioms

The Record axiom is now the third named premise, but it is intentionally narrow.
It is not a hidden import of measurement theory, dynamics, probability, or
observable selection.

| Axiom | What it supplies | What it does not supply |
|---|---|---|
| **Lattice** | Site set `Z^3`, standard translation action, nearest-neighbor cubic adjacency, and finite-range locality by support or graph distance. | Dynamics, boundary condition, metric scale, lattice spacing, continuum/IR limit, causal cone, probabilistic independence, or physical unit conversion. |
| **Quantum** | One qubit at every site; one-site operator algebra `M_2(C)`, equivalently real `Cl(3,0)`. | Dynamics, composition beyond lattice placement, measurement instrument, Born rule, species, gauge group, particle content, or physical observable bridge. |
| **Record** | Durable registration of the realized outcome. Given a readout context with finite central sectors and fixed `K`/CPT conjugation, the realized outcome is the `K`/CPT orbit of the realized central sector. Finite disjoint records have finitely additive scalar readout `I`, with `I(empty)=0`. | The readout context itself, central decomposition, `K`/CPT structure, sector-generation rule, weighting, normalization, probability, measurement/decoherence dynamics, time metric, within-sector data, occupancy rule, or downstream selectors. |

The machine-readable axiom authority is the stable `minimal_axioms` premise node
in [`docs/audit/data/axiom_premise_nodes.json`](docs/audit/data/axiom_premise_nodes.json).
Depending on the axioms chain-satisfies audit dependencies without turning
downstream claims into bounded retained claims.

## How Status Works

The repo is in an audit-transition state. Many older notes and publication
tables still say `retained`, `derived`, or `promoted` in author-side language.
Those words are not the current authority. The current authority is the
computed `effective_status`.

| Effective status | Reading rule |
|---|---|
| `retained` | Audit-ratified positive theorem. |
| `retained_no_go` | Audit-ratified negative result or obstruction. This is retained science, not a failure to track. |
| `retained_bounded` | Audit-ratified result with an explicit bounded premise/admission/import boundary. |
| `decoration_under_*` | Boxed algebraic or bookkeeping decoration under a retained parent. |
| `retained_pending_chain` | Locally clean, but waiting for upstream retained-grade closure. |
| `open_gate` | Explicit blocker or unclosed bridge. |
| `audited_conditional` | Audited as conditional only; not retained-grade. |
| `audited_renaming` | Audited as a naming/reframing result only; not retained-grade. |
| `audited_numerical_match` | Audited as a numerical match/comparator only; not retained-grade. |
| `unaudited` / `audit_in_progress` | No final audit authority yet. |
| `meta` | Index, map, methodology, or package-management material. |

The generated status surface is
[`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md). It refreshes
automatically when the audit pipeline runs:

```bash
bash docs/audit/scripts/run_pipeline.sh
```

That command regenerates the audit ledger, audit queue, effective-status
publication views, publication/audit divergence report, and front-door status
snapshot.

## Ratified Surface Today

The retained-grade surface is broad but not the same thing as the full
publication package. Current retained-grade totals are:

| Category | Count |
|---|---:|
| Retained positive theorems | 207 |
| Retained no-go rows | 218 |
| Retained bounded rows | 745 |
| Boxed decorations under retained parents | 49 |
| Total retained-grade rows including boxed decorations | 1219 |

Representative high-load retained-grade areas include:

- core structural positives such as
  [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](docs/THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md),
  [`NATIVE_GAUGE_CLOSURE_NOTE.md`](docs/NATIVE_GAUGE_CLOSURE_NOTE.md),
  [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](docs/GRAPH_FIRST_SU3_INTEGRATION_NOTE.md),
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](docs/CL3_COLOR_AUTOMORPHISM_THEOREM.md),
  and [`CPT_EXACT_NOTE.md`](docs/CPT_EXACT_NOTE.md);
- bounded structural scaffolding such as
  [`THREE_GENERATION_STRUCTURE_NOTE.md`](docs/THREE_GENERATION_STRUCTURE_NOTE.md),
  [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](docs/PLAQUETTE_SELF_CONSISTENCY_NOTE.md),
  [`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](docs/EMERGENT_LORENTZ_INVARIANCE_NOTE.md),
  [`STRONG_CP_THETA_ZERO_NOTE.md`](docs/STRONG_CP_THETA_ZERO_NOTE.md), and
  [`GRAVITY_CLEAN_DERIVATION_NOTE.md`](docs/GRAVITY_CLEAN_DERIVATION_NOTE.md);
- retained no-go or obstruction results that keep the package honest, including
  [`YT_EW_COLOR_PROJECTION_THEOREM.md`](docs/YT_EW_COLOR_PROJECTION_THEOREM.md),
  [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](docs/PHYSICAL_LATTICE_NECESSITY_NOTE.md),
  [`S3_MASS_MATRIX_NO_GO_NOTE.md`](docs/S3_MASS_MATRIX_NO_GO_NOTE.md),
  [`EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md`](docs/EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md),
  and multiple Koide, plaquette, Planck, source/action, and gravity gate
  obstructions.

The highest load-bearing nodes in the citation graph are still
`minimal_axioms`, `three_generation_observable_theorem_note`,
`observable_principle_from_axiom_note`, `graph_first_su3_integration_note`, the
historical `minimal_axioms_2026-05-03`, `staggered_dirac_realization_gate`, and
the time/anomaly/terminology cluster. Several of those are not retained-grade;
that is exactly why the audit queue matters.

## Publication Package Versus Audit Surface

The publication package is useful, but it is ahead of the audit lane. Read the
generated effective-status mirrors before quoting any claim:

- [`CLAIMS_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md)
- [`QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md)
- [`USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md)
- [`DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/DERIVATION_VALIDATION_MAP_EFFECTIVE_STATUS.md)
- [`PUBLICATION_AUDIT_DIVERGENCE.md`](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md)

The current divergence report lists **440** non-retained-grade cited rows in
publication tables: 188 critical unaudited, 145 high unaudited, 92 medium
unaudited, plus smaller sets of open-gate, renaming-only, numerical-match, and
conditional rows. Notable critical unaudited publication dependencies include
`alpha_s_derived_note`, `anomaly_forces_time_theorem`,
`ckm_atlas_axiom_closure_note`, `standard_model_hypercharge_uniqueness`,
`bminusl_anomaly_freedom`, `yt_ward_identity_derivation`, many CKM/PMNS/DM
source notes, Higgs/vacuum notes, and several GR/QG closure notes.

This does not make those rows useless. It means they must be described as
proposed, conditional, support-tier, bounded, or unaudited until the audit lane
ratifies them.

## Falsifiable Forecasts

The current sharp forecast catalog is
[`docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md`](docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md).
It is a publication-surface catalog, not an audit verdict.

| Forecast | Current statement | Falsifier | Status discipline |
|---|---|---|---|
| PMNS `delta_CP` | Third quadrant, near maximal: `delta_CP in [251.86 deg, 270.00 deg]`, with `sin(delta_CP) ~= -0.987` and `cos(delta_CP) < 0` at the PDG anchor. | A 5-sigma DUNE/T2HK measurement outside the bracket. | Conditional on named NuFit comparison bands, preimage-localization admission, chamber chart, branch-choice rule, and currently unaudited flavor/PMNS chain. |
| PMNS `theta_23` | Upper octant over the stated rectangle, with certified `s_23^2 > 0.5277`. | A significant lower-octant determination, `s_23^2 < 0.5`. | Same comparison/admission boundary as the PMNS `delta_CP` forecast. |
| Higgs vacuum | Absolute stability, with `lambda(M_Pl)` conditionally zero on the Coleman-Weinberg-boundary surface. | A definitive metastability determination. | Conditional on the framework `y_t` / `m_H` lane; not an unconditional `m_H` closure. |

None of these forecasts imports PDG or NuFit values as derived framework
outputs. The external bands are comparison windows and labels.

## Current Quantitative Surface

Use
[`QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md)
and
[`USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX_EFFECTIVE_STATUS.md)
for the full machine-refreshed status view. The short map is:

| Quantity or lane | Current value or claim | Current qualifier |
|---|---|---|
| `alpha_s(M_Z)` | `0.1181` on the existing conditional chain. | The direct Wilson-loop/static-potential route remains pending; `ALPHA_S_DERIVED_NOTE` is unaudited, while the direct-route theorem is retained-bounded. |
| `alpha_LM` | `alpha_LM^2 = alpha_bare alpha_s(v)`. | Retained bookkeeping identity; not an independent empirical prediction. |
| `sqrt(sigma)` | `465 MeV`. | Bounded companion; confinement is structural, but quantitative hadron masses are still open. |
| Electroweak couplings | `sin^2(theta_W)(M_Z) = 0.2306`, `1/alpha_EM(M_Z) = 127.67`, `g_1(v) = 0.4644`, `g_2(v) = 0.6480`. | Matching-rule conditional; EW color projection and matching-rule open-gate/no-go boundaries remain load-bearing. |
| EW Higgs gauge masses | `M_W^2 = g^2 v^2 / 4`, `M_Z^2 = (g^2 + g_Y^2) v^2 / 4`, `M_A^2 = 0`, `rho_tree = 1`. | Retained structural guardrail; no pole-mass or loop-corrected prediction by itself. |
| `M_W` probe | Tree `79.80 GeV`, RGE `80.5573 GeV`. | Bounded same-surface probe, not a few-MeV SM-indirect prediction. |
| `y_t(v)` and top mass | `y_t(v) = 0.9176`; `m_t(pole)` two-loop `172.57 GeV`, three-loop `173.10 GeV`. | Identification-conditioned through the YT/top transport lane and Ward-identification boundary; authorities are largely unaudited. |
| Higgs mass and vacuum | `m_H` two-loop `119.8 GeV`; framework-side three-loop `125.1 GeV`; vacuum stability favorable. | Identification-conditioned; the forecast is a discrimination surface, not a clean retained `m_H` closure. |
| Taste-scalar pair | `124.91 GeV`. | Bounded companion under retained taste-block/isotropy support. |
| DM/cosmology support | `R_base = 31/9`, matter-radiation equality identity, `N_active = 3` with standard `N_eff = 3.046` readout, gravity/cosmology tower ratios. | Mostly structural or supplied-readout support; not a full native density, Hubble, or particle-ID derivation. |
| Neutrino bounds | `sum m_nu > 50.58 meV`, `m_beta <= 50.58 meV`, `m_betabeta <= 50.58 meV`, normal-ordering inequalities. | Bounded observable inequalities; no point prediction for masses, PMNS angles, Majorana phases, or solar gap. |
| CKM atlas package | Numerically rich atlas package including `lambda^2 = alpha_s(v)/2`, `A^2 = 2/3`, `delta = 65.905 deg`, `J ~= 3.33e-5`, `phi_s ~= -0.03850 rad`, barred-triangle/Napoleon/Weitzenbock/Brocard identities, and related support rows. | Publication-captured quantitative package, but most cited CKM authorities are currently unaudited in the audit-derived view. |
| Charged-lepton Koide | Strong support around `Q = 2/3` and `delta = 2/9`. | Open flagship lane; CKM-side support does not close charged-lepton Koide or the absolute lepton scale. |

Every number above must travel with its qualifier. If the qualifier is too long
for the context, link to the generated effective-status table instead of
dropping it.

## Lane Map

The repo contains historical programs, active working lanes, and publication
surfaces. The current lane map is:

| Lane | Current standing | Best next status source |
|---|---|---|
| Axioms and naming | Lattice, Quantum, and Record are the current named minimal premises; Record is third axiom and deliberately narrow. | [`MINIMAL_AXIOMS_2026-06-05.md`](docs/MINIMAL_AXIOMS_2026-06-05.md) |
| Audit lane | Mechanical authority for retained status. Current backlog: 1347 pending, 24 ready, 16 cycle-break targets. | [`docs/audit/AUDIT_QUEUE.md`](docs/audit/AUDIT_QUEUE.md) |
| Gauge/matter backbone | Native `SU(2)`, graph-first `SU(3)`, confinement structure, three-generation observable, CPT, and several anomaly/gauge/matter claims have retained-grade pieces, but major publication dependencies remain unaudited. | [`SCIENCE_MAP.md`](docs/publication/ci3_z3/SCIENCE_MAP.md), effective-status tables |
| Spacetime/gravity/QG | Retained or bounded pieces cover weak-field, Poisson/Newton/WEP/time-dilation, emergent Lorentz, and parts of the gravity route; several GR/QG publication rows are unaudited or bounded. | [`GRAVITY_PUBLICATION_PACKAGE_SUMMARY_2026-04-15.md`](docs/publication/ci3_z3/GRAVITY_PUBLICATION_PACKAGE_SUMMARY_2026-04-15.md) |
| Staggered/finite-Grassmann realization | Important load-bearing gate. Some narrow steps are retained/bounded; `staggered_dirac_realization_gate_note_2026-05-03` itself is audited as renaming, not retained closure. | [`docs/lanes/staggered/README.md`](docs/lanes/staggered/README.md), audit queue |
| Strong CP/action/time | Strong-CP theta-zero support has retained-bounded material and no-go companions; action/time bridges still include open gates and unaudited critical dependencies. | [`STRONG_CP_THETA_ZERO_NOTE.md`](docs/STRONG_CP_THETA_ZERO_NOTE.md), audit ledger |
| Couplings/EW/QCD | Useful numerical package exists, including `alpha_s`, EW matching, plaquette, and string-tension rows, but key values are conditional, bounded, or unaudited until direct gates close. | [`QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md) |
| YT/top/Higgs | Top/Higgs/vacuum package is one of the most valuable quantitative surfaces, but current status is identification-conditioned and audit-limited. | quantitative effective-status table and Higgs/YT notes |
| CKM/flavor | CKM atlas is numerically rich and publication-captured; most authorities remain unaudited. CKM-side `2/9` support does not close charged-lepton Koide. | [`CKM_ATLAS_AXIOM_CLOSURE_NOTE.md`](docs/CKM_ATLAS_AXIOM_CLOSURE_NOTE.md), divergence report |
| Charged leptons / Koide | Highest-leverage open flagship. `Q = 2/3`, Brannen `delta = 2/9`, source-domain selection, rational-to-radian observable law, and `V_0` absolute scale are not closed. | [`docs/lanes/open_science/06_CHARGED_LEPTON_MASS_RETENTION_OPEN_LANE_2026-04-26.md`](docs/lanes/open_science/06_CHARGED_LEPTON_MASS_RETENTION_OPEN_LANE_2026-04-26.md) |
| Neutrino / PMNS / DM | PMNS forecasts are sharp but conditional and unaudited. Neutrino absolute observable bounds are bounded; quantitative mass closure and Majorana phases remain open. | falsifiable predictions catalog, Lane 4 open-science note |
| Cosmology / `H_0` | Structural identities and reduction rows exist; numerical `H_0` still needs absolute-scale plus cosmic-history/`L` gates. | Lane 5 open-science note |
| Hadron masses | Confinement structure retained, `sqrt(sigma)` bounded; `m_p`, `m_pi`, and spectroscopy are not derived. | Lane 1 open-science note |
| Atomic scales | Scaffold uses textbook inputs; true atomic predictions depend on charged-lepton mass/`m_e`, `alpha(0)`, and nonrelativistic physical-unit closure. | Lane 2 open-science note |
| Non-top quark masses | Bounded support exists; five non-top quark masses are not retained. | Lane 3 open-science note |
| Record/post-record dynamics | Record is now an axiom, but post-record dynamics, objective weighting, source measures, and physical persistence remain separate lanes or conditional notes. | post-record notes and audit ledger |
| Teleportation/chronology/signed gravity | Exploratory or parked frontier lanes. They are not current core physics claims and should not be quoted as matter, mass, object, energy, or FTL transport claims. | `docs/lanes`, effective-status tables |
| Historical/comparison lanes | Mirror, ordered-lattice, generated-geometry, action-law, controls, coin-walks, and moonshot lanes preserve provenance and alternate attempts. | [`docs/lanes/README.md`](docs/lanes/README.md) |

The critical open-science package is
[`docs/lanes/open_science/README.md`](docs/lanes/open_science/README.md). Its
six active lanes are charged-lepton mass retention, atomic scales, `H_0`,
quark masses, hadron masses, and neutrino quantitative closure, with
charged-lepton mass retention currently the highest-leverage dependency because
it unlocks `m_e` for atomic-scale work.

## What Is Still Open

The honest open surface is large:

- The audit backlog is still large: 1347 pending rows and 440 publication-table
  citations outside retained grade.
- Several load-bearing publication parents are unaudited, including the older
  observable-principle parent, anomaly/time rows, `alpha_s` derived chain, CKM
  atlas authorities, YT/Higgs authorities, and many PMNS/DM source rows.
- The Record axiom does not derive Born weights, measurement dynamics, time's
  arrow, source/action identification, physical persistence, selector weights,
  or the physical observable bridge.
- Charged-lepton mass closure is still open: neither Koide `Q = 2/3` nor
  Brannen `delta = 2/9` is a retained physical charged-lepton theorem, and the
  absolute lepton scale remains separate.
- Hadron masses, atomic spectra, non-top quark masses, neutrino quantitative
  closure, and `H_0` are not closed as first-principles retained predictions.
- Many impressive numerical matches are either bounded companions,
  identification-conditioned, audited as numerical matches, or unaudited.

This repository is valuable precisely because these boundaries are tracked in
the same place as the positive claims.

## Read First

Use these entry points in order:

1. [`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md) -
   generated current audit/status snapshot.
2. [`docs/MINIMAL_AXIOMS_2026-06-05.md`](docs/MINIMAL_AXIOMS_2026-06-05.md) -
   current Lattice/Quantum/Record axiom memo.
3. [`docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md`](docs/publication/ci3_z3/FALSIFIABLE_PREDICTIONS_2026-06-08.md) -
   current forecast catalog.
4. [`docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/QUANTITATIVE_SUMMARY_TABLE_EFFECTIVE_STATUS.md) -
   audit-badged quantitative values.
5. [`docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md`](docs/publication/ci3_z3/CLAIMS_TABLE_EFFECTIVE_STATUS.md) -
   audit-badged manuscript claim table.
6. [`docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md`](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md) -
   publication rows still outside retained grade.
7. [`docs/lanes/open_science/README.md`](docs/lanes/open_science/README.md) -
   active critical open-science lanes.
8. [`docs/publication/ci3_z3/REPRODUCE.md`](docs/publication/ci3_z3/REPRODUCE.md) -
   reproduction path.
9. [`docs/audit/AUDIT_LEDGER.md`](docs/audit/AUDIT_LEDGER.md) -
   full generated audit ledger.
10. [`docs/audit/AUDIT_QUEUE.md`](docs/audit/AUDIT_QUEUE.md) -
    current next audit queue.

## Reproduce And Refresh

For the publication package:

```bash
cd docs/publication/ci3_z3
cat REPRODUCE.md
```

For audit status and generated front-door status:

```bash
bash docs/audit/scripts/run_pipeline.sh
```

For status after a local change, read:

- [`docs/repo/FRONT_DOOR_STATUS.md`](docs/repo/FRONT_DOOR_STATUS.md)
- [`docs/audit/AUDIT_LEDGER.md`](docs/audit/AUDIT_LEDGER.md)
- [`docs/audit/AUDIT_QUEUE.md`](docs/audit/AUDIT_QUEUE.md)
- [`docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md`](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md)

## Non-Claims

The front door should prevent over-quotation. In particular, the repo does not
currently claim:

- that every publication-captured result is audit-retained;
- that Record alone derives probability, Born weights, measurement dynamics,
  physical persistence, source/action identification, or selector weights;
- that charged-lepton Koide, the charged-lepton absolute scale, hadron masses,
  atomic spectra, non-top quark masses, neutrino mass closure, or `H_0` are
  already closed retained predictions;
- that CKM, PMNS, Higgs, top, EW, QCD, DM, or cosmology numbers can be quoted
  without their effective-status badges and bridge qualifiers;
- that historical lane language supersedes the current Lattice/Quantum/Record
  axiom memo or the audit-derived effective-status views.

The canonical boundary documents are
[`INPUTS_AND_QUALIFIERS_NOTE.md`](docs/publication/ci3_z3/INPUTS_AND_QUALIFIERS_NOTE.md),
[`WHAT_THIS_PAPER_DOES_NOT_CLAIM.md`](docs/publication/ci3_z3/WHAT_THIS_PAPER_DOES_NOT_CLAIM.md),
and the generated
[`PUBLICATION_AUDIT_DIVERGENCE.md`](docs/publication/ci3_z3/PUBLICATION_AUDIT_DIVERGENCE.md).
