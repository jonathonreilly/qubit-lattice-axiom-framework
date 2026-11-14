## **Searches run.**

- Terms: `GB1E`, `GB1-E`, `T0-start`, `transfer matrix`, `reflection positivity`, `anisotropic`, `quantum link`, `Kogut`, and `inductive class`.
- Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder, including drafts, referee reports, prior digests, and `LIT_*.md`. Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and the YM corpus as “claude/ym4d-hard-route .md files” (`ref/README.md:2,5`).
- No literal GB1E target or optional `briefs/GB1E.txt` was found. The relevant open target is the Euclidean lift: “E-1, E-2, E-3, E-4 = Y3” (`T/GB1.md:17`, paths abbreviated below).

Path prefixes used throughout:

- `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`
- `D/` = `ref/main/docs/`
- `A/` = `ref/main/docs/audit/data/ledger/`
- `Y/` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/`

## **Already in the repo.**

- **Tick, logarithm, and Trotter identities.** GB1 proves finite-box statements conditional on its specified laws. A positive unitary must be trivial; a Hermitian logarithm requires a choice. Quote: “The tick alone does not select this logarithm or its imaginary-time correlators” (`T/GB1.md:45`). Small-angle scaling gives an “`O(tδ)` finite-box error” (`T/GB1.md:55`). Status: frozen, with referee edits applied; “these are not retained-status audit results” (`T/GB1.md:5,11`).

- **Exact finite-volume Z₂ Wilson transfer.** Theorem F4 gives the gauge-projected partition-function/transfer identity, with a symmetric positive transfer: “`Tr(P_0T^{N_t})`” and “`T ... >0`” (`T/GB1.md:62`). This is an analytic relation between real and imaginary angles. It does not supply law data: “the Wilson transfer is the tick at imaginary angles, which is not law data” (`T/GB1.md:209`). Status: the same frozen conditional GB1 result (`T/GB1.md:11`).

- **Finite-register obstructions have explicit scope.** GA2_Y2 excludes invertible, exactly covariant finite links: “A finite register with a nontrivial infinitesimal link representation has no invertible covariant link” (`T/GA2_Y2.md:43`). GB1 separately excludes uniformly local injective readouts from its specified infinite link algebra: “No injective readout ... has the uniform exponential locality of Definition 1” (`T/GB1.md:95`). Euclidean variables remain available: “Correlator-level and Euclidean-variable routes are not excluded” (`T/GB1.md:208`). GA2_Y2 is frozen after referee edits (`T/GA2_Y2.md:5`).

- **SU(2) quantum-link regulator comparison.** GB1QL proves local, finite-time comparisons for its proposed `so(5)` test-law family. The bounded-flux rate is “`O((log s)⁴/s²)`” (`T/GB1QL.md:245`). Bounded local electric energy gives “`O(s^{−2/3})`” (`T/GB1QL.md:271`). The bounds also cover two-time correlators and natural loops (`T/GB1QL.md:279`, “Corollary 4.10”). Scope: “specified matched states and finite time”; the model is “not either named working-set law” (`T/GB1QL.md:7`). Status: frozen after E1–E10 and referee closures (`T/GB1QL.md:5`).

- **Corrected Euclidean hand-off order.** Lemma H makes the missing object explicit: the gauge invariance, Haar reference, RP, and RG-class clauses are properties of one measure. Quote: “the first input it lacks ... is (H-4D)” (`T/GB1QL.md:328`). The final hand-off says “no probability measure on links of a four-dimensional lattice is constructed” (`T/GB1QL.md:343`). This incorporates the referee repair, rather than the draft’s earlier labels (`T/GB1QL_REFEREE.md:193`, “Replace the hand-off table”).

- **Finite two-slice Wilson reflection positivity.** The repaired SU(N) note proves character-coefficient positivity, positive plane kernels, and the integrated reflected Gram for a finite open temporal slab with supplied Wilson weight. Quotes: “coefficients ... are nonnegative” and “is positive semidefinite” (`D/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md:54,70`). It remains bounded in “extent, volume, and sector” and excludes fermionic generators (`same file:76`). Ledger: `"effective_status": "unaudited"` (`A/ax/axiom_first_reflection_positivity_wilson_temporal_gauge_bridge_narrow_theorem_note_2026-06-05.json:27`). The earlier SU(3) one-link result supplies only the “gauge-kernel positivity half” (`D/WILSON_SU3_GAUGE_TRANSFER_KERNEL_POSITIVITY_BOUNDED_NOTE_2026-05-30.md:11`); its ledger is also `unaudited` (`A/wi/wilson_su3_gauge_transfer_kernel_positivity_bounded_note_2026-05-30.json:30`).

- **Full physical SU(3) cube transfer and genuine gluing.** The physical carrier is “`Hphys = L2(SU3^5, product Haar)^simultaneous Ad`” (`D/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md:39`). Its positive transfer preserves that carrier (`same file:43`, “`T=Msp C Msp preserves Hphys`”). Powers integrate complete intermediate boundaries: “all12 intermediate spatial links at every time” (`same file:49`). This is a supplied finite model. Ledger: `unaudited` (`A/ga/gauge_wilson_full_cube_physical_transfer_geometry_bounded_theorem_note_2026-09-07.json:30`).

- **Compact interacting Wilson-to-Hamiltonian limit.** For the supplied anisotropic finite SU(3) cube, the note constructs `F(h)` and `H=−(3/(2a))Δ+V` (`D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md:35,41`). It gives strong convergence and the energy-cutoff estimate “`C t²(1+E²)/n`” (`same file:114`). The potential remains nonlinear: “complete bounded non-Abelian plaquette potential V” (`same file:120`). Physical time remains unselected: “does not select a physical clock” (`same file:122`). Ledger: `unaudited` (`A/ga/gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07.json:29`).

- **Compressed-source anisotropic semigroup.** A separate supplied construction gives “a simultaneous norm limit `exp(-tN)`” (`D/GAUGE_WILSON_CUBE_SLAB_SIMULTANEOUS_ANISOTROPIC_SOURCE_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-09-07.md:25`). Its composition contract is explicit: “in general `(I* T I)^n` is not `I* T^n I`” (`same file:33`). It therefore supplies no uncompressed multilayer identity. Ledger: `unaudited` (`A/ga/gauge_wilson_cube_slab_simultaneous_anisotropic_source_semigroup_bounded_theorem_note_2026-09-07.json:31`).

- **Local finite-region/Peter–Weyl approximation.** The supplied cubic SU(3) Hamiltonian has local-observable approximation bounds whose constants depend on local data, “not the total ambient volume” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:57`). Its cutoff error is energy-priced: “`2(1+M T)sqrt(E/g_R)+E/g_R`” (`same file:72`). It supplies no physical clock conclusion (`same file:30`). Ledger: `unaudited` (`A/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`).

- **YM finite-lattice positivity and limits.** P8 ports the finite Wilson reflection-positivity lemma and conditional subsequential-limit positivity. Quote: “B5 ... and its reflection-form corollary are proved here” (`Y/library/port/p8-positivity.md:856`). Its limit statements retain the specified geometry and hypotheses (`same file:862`, “H-TORUS-RP is proved ... for the even centred link-reflection geometry”). Status: “not yet checked by another model”; no audit status (`same file:866`).

- **YM all-mirror Wilson result.** LG1 Theorem 13 supplies finite-cutoff Wilson probability measures, DLR limits, chessboards, and RP at coordinate and diagonal mirrors. Quote: “all coordinate site, coordinate bond and diagonal lattice mirrors” (`Y/library/lg1.md:431`). Its group is explicitly `SU(2)` (`same file:425`). Status: “frozen” (`same file:485`); provenance says “Research text, not an audit; grants no status” (`same file:3`).

- **YM O(4) restoration is conditional.** RO1 uses rooted D1, the lattice-mirror interface, continuum Hilbert/cube-cone input, and state-uniform TU10. Quote: “Neither D1 nor TU10 nor existence of the realizations is discharged here” (`Y/library/ro1.md:679`). Status: “frozen, as a conditional implication” (`same file:702`). It is not a theorem for arbitrary anisotropic starts.

- **D4 positivity evidence is narrower than the assembly shorthand.** The consolidation identifies a finite scalar test: “a Hankel test on the scalar kernel”; fermion RP was “UNTESTED” (`ref/pr10130/docs/D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:42`). It classifies the positivity tests as “finite numerical diagnostics,” in “supplied free models” (`same file:49`).

## **Failed attempts on file.**

- **Literal tick-as-positive-transfer.** The failing step is positivity of a nontrivial unitary: “A positive unitary is the identity” (`T/GB1.md:45`). Choosing a logarithm also does not select a local Euclidean measure: “not thereby local transfer matrices of a Euclidean measure” (`T/GB1.md:49`).

- **Slice covariance/Haar space promoted to measure properties.** The referee identified the conflation: the earlier assertion concerns “dynamics on slice Hilbert spaces, not ... a measure `μ`” (`T/GB1QL_REFEREE.md:100`). The repaired conclusion leaves all four measure properties undelivered (`T/GB1QL.md:343`, “are properties of that measure and are not delivered”).

- **Flux-uniform quantum-link comparison.** The referee closure gives a one-tick error “at least `0.9θ²`, for every `s`” (`T/GB1QL.md:183`). The fixed `L5-U` large-register route also stops at U2: its block dimension is “`C(4, m') ≤ 6`” (`T/GB1QL.md:310`).

- **Wrong-sign Wilson positivity.** The historical bridge used a weight with a negative Z₂ coefficient: “`(e^{-beta} - e^{beta})/2 < 0`” (`D/RP_WILSON_TEMPORAL_GAUGE_BRIDGE_SIGN_AND_POSITIVITY_REPAIR_NOTE_2026-06-06.md:30`). Its finite-grid exactness claim also failed: the integrand is “not a bounded-degree trigonometric polynomial” (`same file:36`). The record says “The audit is correct on all three” (`same file:38`). Current repair ledger: `unaudited` (`A/rp/rp_wilson_temporal_gauge_bridge_sign_and_positivity_repair_note_2026-06-06.json:33`).

- **Spatial cubic symmetry promoted to Euclidean isotropy.** The failing inference leaves two quadratic coefficients: “Spatial cubic symmetry allows `c_t != c_s`” (`D/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md:47`). Current ledger: `unaudited` (`A/sp/spatial_cubic_time_anisotropy_gate_no_go_2026-06-06.json:29`).

- **Axis RP promoted to O(4).** The YM comparison records anisotropic free countermodels with axis RP and a mass gap, yet no O(4). Their missing condition is explicit: “fails reflection positivity at the twelve diagonal mirrors” (`Y/library/ro1-vs-ca.md:96`).

## **Overlap with this lane’s results.**

not run

## **Missed inputs.**

- **Start from the corrected hand-off object.** Lemma H would make construction of `μ` the first deliverable, with its properties checked afterward: “the first input it lacks ... is (H-4D)” (`T/GB1QL.md:328`).

- **Use the full-boundary transfer for multilayer composition.** It supplies actual gluing: “exactly the longer slab action in temporal gauge” (`D/GAUGE_WILSON_FULL_CUBE_PHYSICAL_TRANSFER_GEOMETRY_BOUNDED_THEOREM_NOTE_2026-09-07.md:49`). This changes which composition theorem GB1E can import; compressed powers retain an “ADDITIONAL composition contract” (`D/GAUGE_WILSON_CUBE_SLAB_SIMULTANEOUS_ANISOTROPIC_SOURCE_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-09-07.md:33`).

- **Use the existing Hamiltonian-limit and regulator bounds with their domains.** The compact-cube theorem prices the cutoff by “`1+E²`” (`D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md:114`). GB1QL gives “no statement uniform in all ticks” (`T/GB1QL.md:259`). Together they identify the estimates a joint time/register limit must supply.

- **A finite-rank group kernel is a possible representation, not established probability data.** GA2_Y2 already names the missing check: “a band-limited kernel is not automatically a positive probability density” (`T/GA2_Y2.md:176`). This prevents treating equivariant embedding as completion of Y1.

- **Use the existing coherent-state proposal as a proposed route only.** The literature digest asks for an exact representation of the actual update, while retaining “positivity/reflection positivity, small-field control, and the VC1-state comparison” (`T/LIT_QLM.md:163`). Those obligations would remain explicit.

- **Pin the requested RG class before claiming a T0 hand-off.** The frozen interface says “the class and topology must be pinned before the claims are testable” (`T/GA2_Y2.md:178`). It also separates “SU(5), SO(10), matter, anisotropy and matching” as extensions (`same line`).

## **Consumers.**

- **GB1QL / GB1-H.** The weakest next structural input is one four-dimensional link probability measure, followed by its GI, Haar, RP, and class properties. Quote: “(H-4D) first; (H-GI), (H-Haar), (H-RP) and (H-class) as properties of the missing measure” (`T/GB1QL.md:21`).

- **GA2, Y1–Y2.** Y1 needs a “local, gauge-invariant action `S_fw`, reflection positive in time” (`T/TOE_ASSEMBLY.md:613`). Y2 additionally needs membership in the hard-core RG domain or an extension of its bounds (`same file:614`, “bounds extend to `S_fw`”). A finite transfer alone supplies only part of this interface.

- **T0-start / T0-rate.** The requested producer statement begins with a gauge-invariant, RP Haar-reference measure in the inductive class at small coupling (`T/GA2_Y2_DRAFT.md:211`, “density in `𝒜_{k_0}(g)`”). GA2 needs scale-uniform bounds and quantitative errors; these remain “requests, not established branch results” (`T/GA2_Y2.md:178`).

- **YM P8 and RO1.** P8 needs RP on its specified half-algebra and geometry (`Y/library/port/p8-positivity.md:797`, “Retain H-TORUS-RP”). RO1 needs the stronger lattice-mirror interface together with its separate growth and continuum inputs (`Y/library/ro1.md:679`, “state-uniform TU10 give full scalar O(4) covariance”).

- **ST1, LZ1, EW1, FL2, CS1 through GA2.** ST1 route B consumes reflection positivity of the Euclidean transfer. LZ1 consumes O(4) restoration plus OS reconstruction. EW1 and FL2 consume running-coupling information. The assembly names these dependencies explicitly (`T/TOE_ASSEMBLY.md:600`, “LZ1 ... ST1 route B ... EW1 and FL2 ... and CS1”) and distinguishes the scale-by-scale bounds from the limit itself (`same file:606`, “GA2 consumes these more than the `a -> 0` limit itself”).