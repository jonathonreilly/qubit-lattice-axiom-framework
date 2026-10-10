# Spatial D3Q27 prior-art and premise inspection

2026-10-09. Read-only source comparison; this is not a review or derivation of the future spatial theorem.

**Finding:** no inspected source establishes the requested local spatial particle generator together with quantitative particle-number and spatial-mesh convergence to a nonlinear finite-velocity kinetic PDE. Existing results provide complementary pieces: homogeneous D3Q27 occupation dynamics, local quantum realization followed by global mixing, supplied continuum **linear** kinetic-to-fluid estimates, and older exclusion-gas streaming identities. The missing spatial limit is therefore a genuine gap within the inspected coverage. This is not a global novelty claim.

## Source identity and coverage

- Main authority: `d9b869b97944676aaa759915462c529dc276a04c`.
- Read checkout: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree`, frozen at `b178e3a5d4c1d1301255596d10ac4e1bc2aeb192` before and after inspection; clean at the final identity check.
- All **40 unique source files in the 69 supplied search hits** were byte-compared with pinned main and matched. All full-read sources below matched the frozen checkout commit. Its scientific additions relative to pinned main are the hydrodynamic and local-quantum notes and their runners; differences in generated audit data are not scientific authority for this report.
- Minimal axioms and premise registry were independently byte-compared across `17a95e60d85afc246fc7c163adef8869ab3f4194`, pinned main and this checkout: unchanged.
- Both search logs were read completely: `spatial_kinetic_search.txt` (48 lines; SHA256 `d31d8f3d1e5b742e9350c272640c91d35d0d57993915792a23732c40e1a0097a`) and `objects_search.txt` (21 lines; SHA256 `cfe92a9dfef0d43dd8d03c52ade3c609d5c4aa92169534dc1e6779c4818832aa`). Below, S/O identify those exact log line numbers, whose entries give complete source paths and source line numbers.

| Supplied hits | Classification from actual source content |
|---|---|
| S1–2 | Relevant partial precedent: 26-neighbor streaming moments and finite-torus stationarity; no particle/mesh limit. |
| S6–9 | Relevant partial precedent: inertial-record exclusion/exchange gas, event conservation and product-state currents; no hydrodynamic theorem. |
| S17–19 | Relevant streaming context: second-order expansion under dilute first-harmonic closure and a separately supplied creeping PDE. |
| S43; O15–21 | Closest matching collision contract: homogeneous D3Q27 finite-population LLN, with no spatial coordinate. |
| S48 | Historical Gaussian correlation estimate, not dynamic propagation of chaos. Original read, not accepted from its title or triage verdict. |
| S3–5, S10, S12–16 | Context only: capture/shadow formulas, independent-walk diffusion, finite-generator flux identities, or separately supplied potential/continuum closures. Their current claim scopes do not contain the target limit. |
| S11, S20 | Context only: curvature-constraint algebra and detailed-balance/persistent-walk spectral algebra. |
| S21–36, S38–42, S45 | Keyword overlap: quadratic kinetic forms, field dispersion, Wilson energies/gaps/loops, spatial/tick graining, or RG normalization. These are not particle collision kinetics. |
| S37, S44, S46–47 | Premise context: dynamics remain supplied; common-order kernels/record laws and axiom-reset distinctions do not select this collision process. |
| O1 | Context only: supplied ray and lattice-symbol comparison. |
| O2–14 | Context only: Lieb–Robinson propagation bounds, not a finite-velocity species collision equation or its particle limit. |

For context-only hits I read the logged passages plus current claim scopes or surrounding source text; I did not review their unrelated proofs. Complete notes and their mathematical arguments were read for these 13 sources, all identified by the frozen checkout commit above:

| ID | Exact source | Lines |
|---|---|---:|
| C | [Supplied finite-velocity collisions](../../../../docs/SUPPLIED_FINITE_VELOCITY_COLLISIONS_AND_GIBBS_EQUILIBRATION_BOUNDED_THEOREM_NOTE_2026-10-08.md) | 462 |
| Q | [Local quantum collisions and rapid mixing](../../../../docs/LOCAL_QUANTUM_COLLISIONS_AND_RAPID_MIXING_BOUNDED_THEOREM_NOTE_2026-10-09.md) | 380 |
| H | [D3Q27 hydrodynamic approximation](../../../../docs/D3Q27_DISSIPATIVE_HYDRODYNAMIC_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-10-09.md) | 816 |
| F | [Forward streaming on 26 neighbors](../../../../docs/ADMISSIBILITY_RULE_FORWARD_STREAMING_ON_THE_26_NEIGHBOURS_ISOTROPY_OF_THE_SECOND_ORDER_TERM_IS_ONE_NUMBER_AND_CONSTANT_RATE_RULES_CAPTURE_ISOTROPICALLY_BOUNDED_THEOREM_NOTE_2026-09-24.md) | 310 |
| I | [Inertial-record gas](../../../../docs/ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md) | 187 |
| B | [Biased symmetric streaming](../../../../docs/ADMISSIBILITY_RULE_A_STREAMING_CLAUSE_WITH_AN_ISOTROPIC_SECOND_ORDER_TERM_CONTENT_AS_A_BIAS_ON_A_SYMMETRIC_WALK_UNBIASED_CAPTURE_AND_ITS_PRICE_BOUNDED_THEOREM_NOTE_2026-09-21.md) | 171 |
| W | [Cubic streaming viscosity](../../../../docs/ADMISSIBILITY_RULE_THE_WIND_OF_A_CAPTURING_BODY_IS_NOT_ISOTROPIC_LATTICE_STREAMING_GIVES_A_VISCOUS_TERM_OF_CUBIC_SYMMETRY_DIRECTION_DEPENDENCE_DOES_NOT_DECAY_BOUNDED_THEOREM_NOTE_2026-09-21.md) | 191 |
| A | [Minimal axioms](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) | 233 |
| R | [Approved premise registry](../../../../docs/audit/data/axiom_premise_nodes.json) | 52 |
| SI | [Historic Stosszahlansatz intake](../../../../docs/historic_intake/HISTORIC_DM_STOSSZAHLANSATZ_THEOREM_NOTE_INTAKE_NOTE_2026-08-05.md) | 60 |
| SO | [Pinned Stosszahlansatz original](../../../../archive_unlanded/historic_intake_originals/branch02/405_DM_STOSSZAHLANSATZ_THEOREM_NOTE.md) | 165 |
| BI | [Historic Boltzmann intake](../../../../docs/historic_intake/HISTORIC_DM_BOLTZMANN_THEOREM_INTAKE_NOTE_2026-08-05.md) | 60 |
| BO | [Pinned Boltzmann original](../../../../archive_unlanded/historic_intake_originals/branch01/338_DM_BOLTZMANN_THEOREM.md) | 275 |

## What the closest results actually supply

**C, Sections 1 and 4–5:** `V={-1,0,1}^3`, energy `|v|^2`, all 288 reversible pair exchanges, and positive equal forward/reverse rates. The finite chain has **27 global occupation counts**, total count N, and rates `kappa_r n_i n_j/N`. Its finite-horizon mean-square LLN is uniform in N for this fixed 27-dimensional unit-mass simplex. It supplies no position cells, local spatial density normalization, transport generator, spatial refinement or estimate uniform in a growing number of cells. Its exact conditional drift does not assert factorization of expectations. The persistence import is used for long-time homogeneous equilibration, not for this LLN.

**Q, Sections 1–4:** the local graph construction really does realize C after rapid interchange, but vertices are **mixing/register slots**, each carrying a supplied 27-level velocity register. Labels do not determine spatial displacements. Fiber averaging mixes labels globally conditional on their counts; the note explicitly warns that this can remove spatial variation. Its bound is for a fixed graph/count; `B=||integral(e^{tS}-P)dt||` is not bounded uniformly in growing graphs, and the displayed loose bound depends strongly on N. This is useful microscopic collision support, not already a spatial kinetic construction. Reinterpreting its graph as physical position would require a new bridge.

**H, Sections 2, 5–7:** continuum streaming `v·grad_x` on a supplied torus is an input. The theorem starts with the linearized distribution `h`, not a nonnegative nonlinear particle density. Its diffusive theorem requires `theta=1/3`, the specified positive rate `alpha_*`, H4 slow initial data with `E=0` and `div j=0`, and bounded diffusive time. Its acoustic theorem permits all fixed positive rates and `theta in (0,1)`, but uses H5 data and the stated first-order preparation; the order-two estimate is for projected fields or the corrected distribution. A spatial nonlinear kinetic theorem would still need a controlled small-amplitude passage and compatible scaling/preparation before either result could be composed. Section 7's exact quadratic flux identities are explicitly not a nonlinear fluid theorem.

**F/I/B/W:** these are conditional record-gas models, not the same D3Q27 collision process. F's 26 spatial offsets coincide geometrically with the nonzero D3Q27 vectors, while content is a unit vector on a sphere (or a separate finite uniform menu for stationarity). Its content-dependent hop rates, exclusion/exchange rule and sphere-averaged fourth-rank tensor differ from C's 27 species and collisions. I has six unit directions or a sphere menu; energy is not an independent fifth invariant there because all contents have unit norm. Its mass current `(1-rho)g` reflects exclusion and cannot simply be substituted for the D3Q27 kinetic flux. F's isotropy reduction is for a truncated, averaged operator; the exact sign enclosure needed for its proposed isotropic mixture remains open. B and W likewise establish streaming expansions and conditional closures, not an N/mesh limit. None of their scoped anisotropy obstructions prohibits a separately supplied D3Q27 construction.

**Historical near-match found by supplemental source search:** BI/BO was absent from the two supplied logs. BO claims a homogeneous relic Boltzmann equation from taste occupations in `L->infinity` at **fixed spacing**; this is neither a local spatial D3Q27 generator nor a particle-number/spatial-mesh estimate. Its Step 1 asserts a closed nonlinear occupation equation from a Hamiltonian without supplying a quantitative Markov/closure derivation. Step 2 imports SO's static free-Gaussian spatial correlation estimate as molecular chaos for the colliding process. SO specifies a Gaussian covariance `(-Delta+m^2)^-1`, uses Wick's identity and supplied freeze-out density, and itself leaves interactions open. That estimate does not provide time-dependent factorization for the proposed interacting particle generator. These are substantive premise/target mismatches, not merely different titles. Both intake wrappers have no attached evidence and explicitly confer no authority. BO's current source must not be used to mark the spatial gap closed.

The historic original identities were checked against their wrappers: SO SHA256 `d2ff19121ed25442119c2b54118225067aa2d581aaf2a11250d58f10e3290c36`, original commit `56d8565f1199dd1eb91f4329941e416a8662d7d0`; BO SHA256 `70330dbc1b9ba39db6af5f359c4dd4c601c4107dc5bab4bfaa83ed5bc33846cd`, original commit `8e20182cc534935063b9a384e11da7b0f6772d37`.

## Premise boundaries and required root reading

A and R supply nearest-neighbor cubic structure, the one-site `M_2(C)` possibility presentation, a local admissibility distribution and permanent locked records with at most one record per site. They do **not** supply the velocity menu, classical occupation carrier, collision rates, energy dictionary, Markov clock, spatial scaling or independent-particle preparation. The three approved primitives add no such dynamics. The kinetic-isotropy primitive concerns structural graining and does not select an isotropic collision rate or viscosity.

Consequently a many-particle cell is not automatically a physical lattice site with one permanent record. Collisions that change species cannot automatically be identified with rewriting immutable Record contents. Diagonal jumps are additional update data, not a consequence of nearest-neighbor adjacency. These are unresolved physical identifications; they do not invalidate an explicitly supplied mathematical model. The older I note already flags its re-drawing/locking incompatibility instead of resolving it.

Before using the proposed construction downstream, root should directly retain/read **C Sections 4–5, Q Sections 1 and 3–4, H Sections 2 and 5–7, and A's Record/dynamics clauses**. They fix the count normalization, distinguish mixing space from streaming space, and limit the linear-fluid composition. For any renewed assertion that earlier repository work already proves molecular chaos/Boltzmann reduction, read **BO Steps 1–3 together with SO Assumptions and Steps 2–4**; the intake summaries omit the decisive mismatch.

Verification limits: this inspection read proofs for scope and premise comparison; it did not rerun the old runners, independently certify their full mathematics, inspect the future theorem, or apply an audit status. No external literature/network search, remote PR refresh or exhaustive archive/history search was performed. The supplemental search was over available `docs`; the referenced `lanes/open_science` directory is absent from this checkout. PR #9475 was excluded as directed. No editable prompt file, repository science file or platform instruction was changed; this report is the only write.


<!-- Packaging: relative repository links rebased; historical draft links rendered as provenance text. Mathematical/review assertions unchanged. Original raw report SHA-256: 16689053bb9ade9ab78dbab43ea3bc0c9a78fbc2817ec6f6d6834b09010b874a. -->
