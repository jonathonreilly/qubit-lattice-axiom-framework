## **Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and the YM corpus as “claude/ym4d-hard-route .md files” (`ref/README.md:2,5`).
- Initial terms: `ISO-FP`, `GB1-CF`, `four-tiling`, `cube-coupling`, `LW2M`, `plaquette`, `magnetic layer`, `cube.face`, `Kogut.Susskind`, `Wilson action`, `reflection positivity`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder.
- Follow-ups: `NN-a`, `compilation`, `noncommut`, `plaquette ordering`, `colored Floquet`, `anisotropy decay`, `IR-fl`, and current ledger status. Read relevant notes, consolidations, drafts, referee reports, prior digests, and `LIT_QLM.md` by line.
- Path abbreviations below: `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`; `D/` = `ref/main/docs/`; `A/` = `ref/main/docs/audit/data/ledger/`; `P26/` = `ref/pr10126/docs/`; `P35/` = `ref/pr10135/docs/`; `Y/` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/`.

## **Already in the repo.**

- **The cube obstruction is established on the existing test family.** Empty-matter ticks preserve each cube’s link factors, including at finite register. Cube-disjoint observables have “zero connected correlation at every time separation” (`T/GB1ISO.md:72,93`). The continuum statement covers volume-first states and observables with shrinking physical support. Under its hypotheses, an invariant separated two-point limit “vanishes on all separated tests” (`T/GB1ISO.md:128`). Under additional P1–P2 and OS-limit hypotheses, reconstruction gives only `CΩ` (`T/GB1ISO.md:148`, “Then the reconstructed Hilbert space is”). Status: “FROZEN 2026-11-08 after pass 3” (`T/GB1ISO.md:5`).

- **FP already has an infinite-register counting theorem.** Each plaquette occurs twice. Commuting multiplication operators give the full magnetic exponential. The same theorem excludes exact time–space exchange symmetry of the local R-IA lift on even cubic four-tori: “for any … \(t>0\)” (`T/GB1ISO.md:161`). This is part of the frozen note, not an adopted law (`T/GB1ISO.md:156`, “proposed, not adopted”).

- **Finite-register FP remains distinct.** Shared-link operators “need not commute”; therefore “the ordered product’s covariance and exact full-sum form do not follow” (`T/GB1ISO.md:165`). GB1-CF remains open. The source also records: “Neither pass made an NN-a check of FP” (`T/GB1ISO.md:165`).

- **NN-a compilation machinery already exists.** Proposition C(ii) states that every member of GA1-P-5, “on either law,” has finite nearest-neighbour depth, with periodic layers (`T/GA1_5_REFEREE.md:184`). This requires membership in that class. The class itself remains proposed. The owner’s NN-a amendment closes its compilation gap (`T/GA1_5.md:7`, “makes every member … implementable”). Proposition C is explicitly among “Referee closures, unrefereed” (`T/GA1_5.md:11`).

- **GA1-5 supplies scoped support obstructions.** Disjoint covariant finite supports preserve parity-split charges (`T/GA1_5.md:80`, “commutes with each parity-split charge”). Cube-supported magnetic gates give flat physical bands near nodes: “It does not propagate there” (`T/GA1_5.md:160`). These statements concern the named support classes and empty-matter D1 states, not every cube-coupling layer.

- **The growing SU(2) register comparison is available, but uses cube faces.** GB1QL reports empty-matter correlator errors \(O((\log s)^4/s^2)\), or \(O(s^{-2/3})\) under bounded local electric energy, “uniformly in the volume and in \(n≤T\)” (`T/GB1QL.md:303`). Its scope explicitly fixes “the Trotterized model with the cube-face layer” and chooses no vacuum or continuum limit (`T/GB1QL.md:259`). Status: frozen, as recorded in `T/GB1.md:9`, “frozen item `GB1QL.md`”.

- **Finite-box Euclidean lifts already exist.** GB1E records gauge-invariant Haar-density lifts and coordinate link-reflection positivity for both readings. Scope: “All constructions below are on finite periodic boxes” (`T/GB1E.md:7,9`). Status: “FROZEN 2026-11-07” (`T/GB1E.md:5`). The weight mismatch is explicit: no heat kernel equals a Wilson weight “on a neighborhood of the identity” (`T/GB1E.md:150`).

- **Earlier face-register work couples blocks classically.** The consolidation carries exact loop gauge-invariance and completeness, classical Yang–Mills energy convergence, and harmonic dispersion. Its completeness statement is “dim ker(curl) = (blocks - 1) + 3”; its harmonic statement gives speed one with supplied coefficients (`P26/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:379,392–394`). Scope: proposed face-register law, classical results and finite diagnostics, with register-cutoff identification supplied (`same file:340,350`). Status: “author statements for review” (`same file:11`). This is a different layout from FP.

- **Finite-depth ordering already has a bounded warning example.** In the two-bond U(1) model, the Lie product has “`O(h^2)` one-tick summed-energy drift”; the palindrome suppresses it to `O(h^3)` and conserves a different Floquet generator (`D/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md:100–105`). Scope: “a bounded two-bond statement” (`same file:386`). Current ledger: `"effective_status": "unaudited"` (`A/u1/u1_quantum_link_exact_local_backreaction_and_colored_floquet_energy_fork_bounded_theorem_note_2026-09-03.json:33`).

- **A finite SU(3) Wilson-to-Hamiltonian bridge exists.** It retains nonlinear plaquette holonomies and gives the right-input-cutoff bound \(Ct^2(1+E^2)/n\) (`D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md:114`, “precise right-input-cutoff estimate”). It does not take infinite volume or select physical time (`same file:122`, “does not select a physical clock”). Ledger status: `"unaudited"` (`A/ga/gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07.json:29`).

- **Spatial cubic symmetry alone leaves anisotropy.** “Spatial cubic symmetry allows `c_t != c_s`” (`D/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md:47`). Scope: quadratic kinetic forms under spatial symmetry and time parity. Ledger status: `"unaudited"` (`A/sp/spatial_cubic_time_anisotropy_gate_no_go_2026-06-06.json:29`).

- **A full-plaquette finite-truncation gap result is conditional support.** The MDTN note treats SU(2)/SU(3) strong-coupling Hamiltonians with local gauge-invariant plaquette perturbations and volume-independent constants (`P35/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:143–150`, “not on L”). Its BHM rebuild remains an “open obligation”; the citation label means “not ‘repo-established’” (`same file:31–33`). Status: “proposed; unaudited” (`same file:20`).

- **YM has conditional restoration tools.** LG1 supplies Wilson periodic states with RP at “all coordinate site, coordinate bond and diagonal lattice mirrors” (`Y/library/lg1.md:431`). RO1 requires H-U, H-L, H-C and H-T on the stated realization (`Y/library/ro1.md:630`). It leaves D1, TU10 and realization existence undischarged (`same file:679`, “Neither D1 nor TU10”). Status: “frozen … as a conditional implication” (`same file:702`). O4-2 removes H-U for connected separated action-density two-point functions, retaining its other inputs (`Y/library/o4-two-point.md:188`, “H-U is removed”). Its status is “frozen” (`same file:203`).

## **Failed attempts on file.**

- **Finite-register extrapolation from FP’s target identity.** Different tilings share links. Noncommutation prevents inferring either the full-sum exponential or covariance of the ordered product (`T/GB1ISO_REFEREE.md:120`, “neither … follows”).

- **RO1 port for ISO-FP.** It fails at H-L. The local FP lift lacks the required exchange symmetry, and rescaled diagonal reflections need not be lattice maps (`T/GB1ISO_REFEREE.md:132`, “Fails at H-L”).

- **Tree-level matching plus perturbative finite renormalization.** It fails at nonperturbative control: “no bound on long-distance correlations” (`T/GB1ISO_REFEREE.md:133`). The assertion that every FP start has order-one anisotropy was also rejected as “not established” (`same file:134`).

- **Sussman–Alpoge Ward route.** The missing steps are the anisotropy decay exponent and applicability to heat-kernel starts (`T/GB1ISO_REFEREE.md:134`, “unproved use for heat-kernel-in-time starts”). The YM ledger labels the required typed calculation and transport “Outlined” and “unchecked” (`Y/library/sa-ledger.md:456`).

- **Unconditional exclusion of every T0 class.** The draft applied volume-first results to an unpinned torus trajectory. The referee records: “Without (P1), the claim is not established” (`T/GB1ISO_REFEREE.md:182`). The frozen replacement is conditional on P1–P2.

- **Bare small-register coefficients reproducing the classical light cone.** The earlier single-loop diagnostics found: “at small S the bare Hodge coefficients do not give the light cone” (`P26/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:405`). These are finite supplied-model diagnostics, not an impossibility result for tuned layers.

## **Overlap with this lane’s results.**

not run

The assembly calls LW2M a pass-1 lane “after its prior-work digest” and lists its status as “Open” (`T/TOE_ASSEMBLY.md:323`). GB1ISO’s results above are prior inputs.

## **Missed inputs.**

- **Use Proposition C for compilation.** It can supply NN-a implementation once a candidate’s class membership, gauge invariance and covariance are established. It does not remove those obligations (`T/GA1_5_REFEREE.md:194`, “gauge invariance and covariance of the full layer”).

- **Specify the magnetic target precisely.** GB1-CF asks for “the full plaquette sum,” while FP currently supplies its exponential only on the commuting target (`T/GB1.md:111`; `T/GB1ISO.md:161`). The earlier two-bond example distinguishes a summed Hamiltonian from its finite-step Floquet generator (`D/U1_QUANTUM_LINK_EXACT_LOCAL_BACKREACTION_AND_COLORED_FLOQUET_ENERGY_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md:105`, “cross-bond matrix entries”).

- **Rework the register comparison for changed layers.** GB1QL’s existing estimates explicitly concern “the cube-face layer” (`T/GB1QL.md:259`). A cube-coupling candidate needs its own comparison before inheriting those rates.

- **Use O4-2 as a narrower isotropy milestone.** Its connected two-point route removes H-U. Higher points still need operator plates and H-U (`Y/library/o4-two-point.md:176,188`, “Two points only”; “H-U is removed”). FP admission to its remaining hypotheses stays open.

- **Keep classical symbols separate from vacuum control.** The repository literature digest warns that large-register classicality at selected states does not establish comparison “in the vacuum,” or action-class membership (`T/LIT_QLM.md:3`). This leaves state identification and RG admission explicit.

## **Consumers.**

- **GB1-CF / W1.** The immediate consumer needs an admissible finite-register update supplying the full plaquette magnetic term. Exact finite-register isotropy is not part of GB1-CF’s stated requirement (`T/GB1ISO_REFEREE.md:235`, “An admissible finite-register update whose magnetic term is the full plaquette sum”).

- **ISO-FP / Y3 / LZ1.** The target needs a nontrivial volume-first action-density limit, invariant after one finite positive time rescaling, with rate \(O((a/r)^p)\), \(p>0\) (`T/GB1ISO.md:167`, “non-trivial limit”). LZ1 consumes “O(4) restoration plus OS reconstruction” through GA2 (`T/TOE_ASSEMBLY.md:621`).

- **Y1 / Y2 / T0-start.** Y1 needs a local gauge-invariant Euclidean action with time RP. Y2 needs RG-domain membership or a proved extension of the hard-core bounds (`T/TOE_ASSEMBLY.md:634–635`, “bounds extend to `S_fw`”). Exact equality with isotropic Wilson weights is therefore stronger than this interface requires.

- **Anisotropic T0-start / T0-rate.** The proposed extension needs uniform CT1–CT4, rescaled convergence and rates over a pinned compact anisotropy range (`T/GB1ISO.md:171`, “uniformly in lattice spacing, volume, start and …”). Fixed-box time-blocked convergence alone is insufficient (`same file:178`, “not uniform RG admission or interchange of limits”).

- **W3’s framework rung.** It needs a specified framework gauge layer for the interacting common-cone analysis. The assembly names “rung 2, the framework’s own gauge layer”; LW2 serves W3 alongside W1 (`T/TOE_ASSEMBLY.md:751,759`).