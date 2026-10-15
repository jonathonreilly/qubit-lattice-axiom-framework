# M17 canonical physical-source and measurement correspondence

Reviewer: `/root/launch_check`. This is a focused source/measurement review and PR-opening recommendation, not a formal audit, numerical reimplementation, empirical validation, or integration/landing gate. Root remains the scientific author.

**Finding:** no unresolved material source or measurement-scope error in the final note identified below. The outward-endpoint repair closes the one relevant operational ambiguity in equation (10). One coherent `bounded_theorem` / `conditional-support` PR is warranted; the separate opening assessment applies the current-main cluster brief.

## Source and exposure boundary

The independent primary-source conclusions and hand derivation were frozen at 2026-10-15 18:21:35 UTC before exposure to the new root argument. They remain unchanged: `REPORT_v1.md`, `DERIVATION_v1.md`, `SOURCE_RECORD_v1.json`, and `SOURCE_FREEZE_v1.json`. All 27 files enumerated by that freeze are rehashed by the accompanying identity checker. No additional paper or data acquisition was performed for this continuation.

After that freeze I read the complete canonical note, complete primary and both named helpers, the complete negative-scope checklist, paired current summary, execution/binding receipts, all serialized check names/outcomes, and the source-relevant result metadata. The six numerical profile arrays were inspected structurally, not independently recomputed. The three inherited action/response/finite-body notes were previously read completely and their current bytes are matched to the frozen copies. I also read the prior mass/curvature-count note completely to distinguish its propagation/count result from this static environmental result. This does not re-review the earlier campaign.

| Current source | SHA-256 |
| --- | --- |
| Canonical note | `7393fe28d957358c22fdc1915eeca7c6564ad3b83f3f1355ea2628722fc94fda` |
| `scalar_physical_curvature_check.py` | `61286432a5d19c861dda47a0dbbdf7258b4d0d77ad0513af5d667fd4edb52792` |
| `scalar_physical_curvature_action.py` | `dc584405e9e77726ab2c40371a646d4b1adcf5bd022b51dd7ac04887b309c15a` |
| `scalar_physical_curvature_geometry.py` | `17df25aa6257363c4511fd9bb9b839765fd77bf4ef37aba9b0bee14462f23768` |
| Current summary | `506a81180828e02b6f312a2ca6b8e0b4dbdc28f4c3fc3717856baf4c47faf21f` |
| Current results | `2b313f597b04cd80e91042d9165dd4e14d1c1dfac218065bb1ad85e687cc4b60` |
| Current primary cache | `7d9b88fed89815408c732a37aa70f4f6045e4fac1920b304e0c90633a130c516` |

The earlier exposed note was `9e8d265f4a5a30135b3bb8aeb3be2939c538c1f185fbc2d8d134b47e4624cca1`. The supplied `RANGE_DOMAIN_REPAIR_v1.json` records the changed endpoint premise. The repaired note `5ab35d877647f97949adf0712ddff833dfa84d286bcec6abddc675bb635eab51` was subsequently read completely. During report preparation root removed one excess terminal newline from that note and the primary, preserving both earlier files and paired output in `formatting_v1`. The final identity check compares those actual bytes, verifies the primary AST is unchanged and compares all nonidentity result/summary fields. Thus the full reading transfers to the final identities above; no changed scientific passage is inferred from a checksum alone. Exact paths, snapshots, policy revisions, file lengths and comparison results are in `M17_CANONICAL_IDENTITY_v1.json`.

## Equation (10): operational derivation and limits

For the declared static spherical physical metric, a photon has conserved Killing energy. Standard clocks stationary at the emitter and receiver therefore measure

```text
frequency_received / frequency_emitted = N(r0)/N(r) = 1/f(r).
```

For a fixed emitter, a stationary outward endpoint `r>r0`, vacuum radial null propagation and instantaneous reflection, the two coordinate legs are identical. Multiplying their sum by the emitter lapse yields

```text
tau(r) = 2 N(r0) integral_[r0,r] ds/[N(s) sqrt(B(s))],
g = tau' = 2/[f sqrt(B)] > 0,
B = 4/(f^2 g^2).
```

Put `A=f'/f` and `G=g'/g`. Then `B'/B=-2(A+G)` and `N''/N=f''/f`. Substitution into the physical Ricci formula gives precisely

```text
R_J = 2B[-f''/f + A^2 + A G + 2G/r] + 2(1-B)/r^2.
```

This independently checks the roundtrip factor, lapse normalization and curvature substitution without calling the author helpers. The original positive integral omitted which side of the emitter was intended; the final outward-domain statement and regular center-emitter limit resolve it. An inward endpoint would need the absolute path integral and a different derivative sign. That extension is not claimed.

These identities require independently calibrated **areal** radius. A radar distance is not automatically that radius; using the same unknown radial metric to define it would not discharge the calibration premise. The clocks/reflector must be stationary in the declared static chart; moving endpoints, finite turnaround delay, nonradial paths, material refractive media and time-dependent geometry need additional terms or a different model. The note explicitly chooses the ideal model and admits no real instrument pipeline.

The constant normalization of the lapse cancels. Absolute physical units still need consistent time/length calibration; the note uses natural units. A finite list of clock and range values does not supply their derivatives, continuous curvature envelopes or the whole-domain Green problem without error and regularity information. The compact-ripple example correctly demonstrates the insufficiency of function-value errors alone. It is neither a full candidate solution nor a universal impossibility theorem.

The theorem requires the metric/curvature and boundary throughout its chosen domain. Exterior clock, lensing or tidal measurements do not automatically determine interior Ricci curvature. An exterior domain can instead retain its actual inner boundary. The note makes both restrictions explicit. No new measurement qualification is needed for its present conditional claim.

## Correspondence with the frozen primary readings

The canonical links match the versioned primary URLs in the blind source record. The following is the exact reused reading scope, not a claim of whole-literature coverage:

| Primary and reading scope | Legitimate comparison and excluded inference |
| --- | --- |
| [Salgado, gr-qc/0509001v2](https://arxiv.org/pdf/gr-qc/0509001v2), PDF pp. 1–4, Section II through Eq. 18; Eqs. 1, 6–17 used | Jordan scalar variation includes a curvature source; the metric trace still contains matter and scalar terms. The canonical note does not infer matter independence from absence of an explicit matter term in the scalar variation. No later well-posedness theorem or measured Newton normalization is imported. |
| [Kaiser, 1003.1159v2](https://arxiv.org/pdf/1003.1159v2), PDF pp. 1–9, Section II and opening III, Eqs. 1–32 used | Conformal curvature and kinetic normalization comparison. No generic field-space flattening conclusion, Higgs model or numerical Planck calibration is admitted. The candidate coefficients are displayed and checked directly. |
| [Khoury and Weltman, astro-ph/0309411v2](https://arxiv.org/pdf/astro-ph/0309411v2), PDF pp. 1–12, Sections I–III, Eqs. 1–31 used | Concrete competing finite-body matching construction with its potential, coupling, source/ambient densities and boundary conditions. Its approximate shell charge and ambient minimum are not transferable to this candidate without those premises. No historical observational acceptance is reused. |
| [Philipp et al., 1702.08412v2](https://arxiv.org/pdf/1702.08412v2), complete PDF pp. 4–6, Section III A–C, Eqs. 13–27 | Stationary clock redshift/lapse comparison. The source does not supply the second spatial metric function or an actual M17 ranging calibration. Partial exposure of introductory pages remains recorded as partial, not a full read. |
| [Faber and Visser, astro-ph/0512213v2](https://arxiv.org/pdf/astro-ph/0512213v2), PDF pp. 1–7, Sections 1–9, equations through 70 | Their static weak-field dynamical/lensing metric comparison is a concrete prior route, while their GR density/pressure interpretation is not a scalar-theory curvature law. The note does not attribute its exact clock/range identity or any current data reconstruction to this paper. |

The original PDF/text hashes, six equation-page image checks, exact access/version records and extraction warnings remain in `SOURCE_RECORD_v1.json`. Those 16 third-party PDF/text/render files stay local; this report does not authorize their publication. The cited comparisons do not establish priority for the new candidate-specific inequality.

## Theorem, implementation inventory and observational status

The canonical statement agrees with the blind assessment: a necessary one-sided static environment bound can follow from the supplied complete action, positive chart, uniformly elliptic physical metric, all-static scalar fields and a bound on every boundary component. The Green ceiling requires `eta<1`; its failure is inconclusive. The complementary maximum bound uses the potential scale `Hv`. Neither produces a full Einstein/matter solution, a preferred state, existence, stability, uniqueness, a gradient/force bound, or a measured Newton constant.

The note keeps the difference between four-dimensional Ricci curvature and spatial/Weyl/tidal curvature, and between a static metric and static scalar fields. The lower-field sign counterexample only defeats an unrestricted extension of this proof. No alternative route is falsely exhausted. The N1–N8 checklist is consistent with those narrow claims.

The primary imports exactly the two named helpers and declares the note, both helper files, three inherited premise notes and checklist. Its file reads bind those identities. The helpers contain symbolic expressions and explicit synthetic profiles; they do not open observational arrays, reviewer results or inherited numerical outputs. The source inventory therefore matches the stated input admission boundary.

The paired current artifact contains **27 action controls plus 55 geometry controls, 82 passed and 0 failed**, with **six synthetic scalar profiles, zero observational datasets and zero empirical tests**. These are author results read from the frozen artifacts; I did not rerun them or claim their count as independent proof. The final v3 execution receipt reports exit 0 and 1.464587926864624 seconds within the primary's 180-second budget. Its values other than source identities match the fully read v2 result. The initial geometry result still contains **48 passed and 1 failed**, namely the logarithm simplification without the static-chart domain. Its exact failed expression is bound in the receipt and is not overwritten by the current result.

The manuscript's free physical suppliers remain substantial: the action and parameters, realized static domain and fields, calibrated metric with derivative errors, all boundary data, matter/metric consistency, and any operational identification of `q` or `Fgrav`. Stating these is compatible with a useful conditional theorem. It does not constitute observational action determination or a TOE claim.

No canonical edits, Git mutations, external messages, new paper/data acquisitions, author-code executions, formal audit, aggregate science rerun, final archive/index validation or current-main integration check occurred in this continuation. Those delivery and landing operations are outside this report.
