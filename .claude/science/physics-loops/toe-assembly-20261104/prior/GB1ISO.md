## **Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and the YM corpus as “claude/ym4d-hard-route .md files” (`ref/README.md:2,5`).
- Initial terms: `anisotrop`, `isotrop`, `hypercubic`, `T0-start`, `action class`, `GB1ISO`. Directories: `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder. Follow-up terms included `H-class`, `reflection interface`, `R-ISO`, `Theorem`, `status`, and `effective_status`. Relevant TOE searches included drafts, referee reports, prior digests, and `LIT_QLM.md`.
- Path prefixes below:
  - `T/` = `repo/.claude/science/physics-loops/toe-assembly-20261104/`
  - `D/` = `ref/main/docs/`
  - `A/` = `ref/main/docs/audit/data/ledger/`
  - `Y/` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/`
  - `P25/` = `ref/pr10125/docs/`
  - `P30/` = `ref/pr10130/docs/`
- The working target is the isotropy probe under both live Euclidean readings: “The open probes are the isotropy step (H-class, Y3) under R-SUM and R-IA” (`T/TOE_ASSEMBLY.md:269`).

## **Already in the repo.**

- **Finite-torus SU(2) lifts.** GB1E constructs the local heat-kernel lift and the exact R-SUM semigroup lift. They have gauge invariance, Haar densities, and coordinate link-reflection positivity. Scope: “All constructions below are on finite periodic boxes,” for a proposed test family (`T/GB1E.md:7,9`). Status: “FROZEN 2026-11-07 after pass 3” (`T/GB1E.md:5`). These are not an infinite-lattice or completed T0 hand-off.

- **Finite-lattice anisotropy is already established.** On the cubic four-torus, the local lift is “never invariant under exchanging time with a spatial axis.” For fixed positive electric coefficient and Euclidean step, possible exchange invariance of the exact lift is confined to “a discrete subset” of nonzero magnetic angles (`T/GB1E.md:154`). The exceptional set is symmetric: “Δ(−θ)=−Δ(θ)” (`T/GB1E.md:164`). This leaves continuum restoration open.

- **Heat-kernel and Wilson weights are distinct.** Theorem 7.1 excludes equality even near the identity: “No … satisfy \(k_t(g)=e^{a+b\operatorname{Tr}g}\) on a neighborhood of the identity” (`T/GB1E.md:150`). The exact lift also “need not have a finite plaquette-product action” (`T/GB1E.md:180`).

- **A classical anisotropy dictionary exists.** Theorem 7.3 gives the smooth-field stiffness matching and a unique tree-level isotropic step: “\(c_{\lambda\tau_E}=\lambda|\theta|\)” (`T/GB1E.md:176`). Its stated scope is “not a quantum anisotropy or universality theorem” (`T/GB1E.md:180`).

- **Reflection interfaces have different requirements.** GB1E proves coordinate link RP. It excludes spatial site-reflection invariance for the local lift at nonzero spatial coefficient; the exact transfer likewise fails to commute with that reflection at nonzero magnetic angle (`T/GB1E.md:131`, “does not commute”). Thus “(H-class) fails first” requires the torus formulation, P8.1 reflections, and an exchange-invariant action class (`T/GB1E_REFEREE.md:145`, “under three stated conditions”).

- **The regulator comparison is finite-time and state-bounded.** Frozen GB1QL gives rates \(O((\log s)^4/s^2)\) and \(O(s^{-2/3})\), “uniformly in the volume and in \(n\le T\)” for empty-matter states (`T/GB1QL.md:303`). It supplies no vacuum or continuum choice: “does not choose angles, a vacuum or a continuum limit” (`T/GB1QL.md:259`). GB1E’s Euclidean trace-norm convergence instead has a “fixed-box” order of limits (`T/GB1E.md:206`). GB1QL’s status is frozen (`T/GB1QL.md:5`, “FROZEN”).

- **Spatial cubic symmetry leaves a marginal anisotropy.** The prior quadratic-form result allows independent temporal and spatial coefficients: “Spatial cubic symmetry allows `c_t != c_s`” (`D/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md:47`). Current ledger status is `"effective_status": "unaudited"` (`A/sp/spatial_cubic_time_anisotropy_gate_no_go_2026-06-06.json:29`).

- **B4 protection is conditional on the kinetic-form surface.** The prior B4 theorem gives one diagonal quadratic coefficient and equality of temporal/spatial one-loop self-energies for a B4-invariant measure (`D/EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_BOUNDED_THEOREM_NOTE_2026-06-08.md:62,63`, “one-dimensional”; “B4-invariant measure”). The primitive “supplies only kinetic-form isotropy” (`same file:76`). Current ledger status is `"unaudited"` (`A/em/emergent_lorentz_radiative_stability_discrete_tick_b4_bounded_theorem_note_2026-06-08.json:34`).

- **An anisotropic Wilson-to-Hamiltonian limit already exists on a finite SU(3) cube.** It gives strong convergence and the energy-cutoff estimate \(Ct^2(1+E^2)/n\) (`D/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md:114`, “right-input-cutoff estimate”). It does not select time or take infinite volume (`same file:122`, “does not select a physical clock”). Ledger status: `"unaudited"` (`A/ga/gauge_wilson_full_cube_compact_interacting_hamiltonian_limit_bounded_theorem_note_2026-09-07.json:29`).

- **YM has a stronger Wilson mirror theorem.** LG1 Theorem 13 gives periodic Wilson DLR states invariance and RP at “all coordinate site, coordinate bond and diagonal lattice mirrors” (`Y/library/lg1.md:431`). It is fixed-spacing Wilson SU(2), with no RG premise (`same file:425,462`, “no RG”). Status: “frozen” (`same file:485`). P8’s finite-torus interface is narrower: coordinate reflections through planes containing no sites (`Y/library/port/p8-positivity.md:29,35`, “Neither plane contains a site”).

- **YM already has conditional O(4) restoration.** RO1 Theorem 9 covers a volume-first hierarchy on separated tests, using rooted D1, the mirror/Hilbert interfaces, and state-uniform TU10 (`Y/library/ro1.md:630`, “precisely H-U, H-L, H-C and H-T”). “Neither D1 nor TU10 nor existence of the realizations is discharged here” (`same file:679`). Status: “frozen, as a conditional implication” (`same file:702`).

- **A weaker two-point O(4) route is also frozen.** O4-2 removes H-U for connected action-density two-point functions of volume-first torus-limit Wilson states (`Y/library/o4-two-point.md:188`, “H-U is removed”). It retains CA clauses (iii-b), (iv), LG1, and restricted CL1 inputs, with their outstanding dependencies (`same file:69–72`, “proved as an implication”). Its final status is “frozen,” checked by author and referee (`same file:203`). It is restricted to “Two points only” (`same file:176`).

- **The differentiated anisotropy route remains an open input.** The YM ledger records decay exponent \(c_1>1/2\), with claimed \(c_1=1\), as “Outlined” and “unchecked” (`Y/library/sa-ledger.md:456`). The outline index calls the one-loop law “sketched” (`Y/library/sa-index/chunk-06.md:125`).

- **D4 is a scoped alternative.** Its consolidation reports dimension-eight leading free-field Lorentz violation under the Euclidean W(F4) weight (`P30/D4_ROUTE_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:18`, “Euclidean W(F4)-symmetric weight”). Its positivity evidence is “a Hankel test on the scalar kernel,” while gauge-sector protection remains open (`same file:42,28`). Status: “author statements for review” (`same file:11`).

- **Tick symmetry does not supply the missing exchange symmetry.** The Lorentz consolidation’s supplied tick has 96 step-set symmetries: “All fix the time axis” (`P25/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:101`). Its supplied link law produces unequal dressed cones at one loop (`same file:104`, “kappa negative”). Status: “author statements for review” (`same file:11`).

## **Failed attempts on file.**

- **More character observables did not eliminate GB1E’s exceptional angles.** The failed step is excluding simultaneous zeros: “no argument here shows that their common zero set misses” nonzero real angles (`T/GB1E_REFEREE.md:208`).

- **Convexity did not separate cube-face and omitted-face expectations.** Strict convexity controls the cube-face mean, but “does not separate the `CF` mean from the non-`CF` mean” (`T/GB1E_REFEREE.md:208`).

- **The spatial Markov-property attack did not close.** The missing step is proving that the exact transfer kernel violates the required spatial Markov property: “No argument here shows that the kernel … breaks it” (`T/GB1E_REFEREE.md:208`).

- **Tree-level calibration did not restore finite-measure symmetry.** R-ISO “does not make the measure hypercubic invariant” (`T/GB1E.md:99`). The owner check records failing target/premise tests: “Calibrates to the isotropy target” and “Imposes tree-level isotropy” (`T/GB1_GEN_OWNER_CHECK.md:80`).

- **Strict principal generators did not yield another Euclidean route.** At irrational electric angles, the infinite-register gate has −1 in its spectrum, so the strict generator does not exist (`T/GB1E.md:11`, “does not exist”). Wherever strict R-GEN exists, its bounded sum has the partition obstruction; R3 also has that obstruction (`T/GB1E.md:121,125`, “excludes its lift”; “excludes a lift”).

- **Axis RP did not imply O(4).** The YM comparison records anisotropic free countermodels with axis RP, hypercubic symmetry, and a mass gap. Their missing condition is explicit: “fails reflection positivity at the twelve diagonal mirrors” (`Y/library/ro1-vs-ca.md:96`).

- **The old Clifford and staggered-sign routes did not derive a coupling split.** The pseudoscalar fails to supply the fourth generator; the eta signature has vanishing anisotropic projection (`D/GAUGE_WILSON_ISOTROPY_BOUNDARY_NOTE_2026-05-04.md:236,238`, “supplies no coefficient update”; “anisotropic projection vanishes”). This is “not a derivation of isotropy from the minimal axioms” (`same file:244`). Current ledger status: `"unaudited"` (`A/ga/gauge_wilson_isotropy_boundary_note_2026-05-04.json:30`).

- **Historical SU(3) C-iso closure is not a verified matching theorem.** Its analytic derivation and Hamilton-limit error bound “remain unverified”; the two cited derivation artifacts are absent (`D/C_ISO_SU3_NLO_CLOSURE_BOUNDED_NOTE_2026-05-08_su3nlo.md:5,9`). The finite fit does not supply controlled remainders or transfer a one-plaquette discrepancy to a multiplaquette observable (`same file:38–42`, “obligations here”; “does not transfer”).

- **Compressed-source powers do not establish full slab composition.** The simultaneous anisotropic semigroup note retains an “ADDITIONAL composition contract”: generally \((I^*TI)^n\ne I^*T^nI\) (`D/GAUGE_WILSON_CUBE_SLAB_SIMULTANEOUS_ANISOTROPIC_SOURCE_SEMIGROUP_BOUNDED_THEOREM_NOTE_2026-09-07.md:33`).

## **Overlap with this lane's results.**

not run

## **Missed inputs.**

- **Use the current two-branch target.** No generator reading was adopted. The owner requested probing each, while only R-SUM and R-IA retain open Euclidean isotropy probes (`T/TOE_ASSEMBLY.md:269`, “no reading is adopted”). This keeps the exact-semigroup and fixed-step local starts distinct.

- **Pin the action class before testing membership.** GA2_Y2 says “the class and topology must be pinned before the claims are testable” (`T/GA2_Y2.md:178`). GB1E names its own heat-kernel and exact-lift classes but says neither is identified with T0’s class (`T/GB1E.md:38`, “Neither class is identified”). This changes H-class from an informal resemblance test to a specified membership or extension statement.

- **Use the frozen mirror and growth interfaces together.** LG1 supplies the Wilson all-mirror result; RO1 still requires state-uniform TU10 and rooted D1 (`Y/library/lg1.md:431`, “All mirrors”; `Y/library/ro1.md:679`, “Neither D1 nor TU10”). This identifies what an anisotropic extension must establish beyond coordinate RP.

- **Use O4-2 for a bounded first milestone.** It removes H-U only for the connected two-point function (`Y/library/o4-two-point.md:188`, “H-U is removed”). Higher points still need operator plates (`same file:176`, “hence H-U”). This separates a two-point milestone from the full Y3 target.

- **Retain state, register, and limit obligations.** GB1QL compares matched states at finite time; GB1E’s Euclidean convergence is per box (`T/GB1QL.md:259`, “fix `X`, `n`, `M`”; `T/GB1E.md:206`, “fixed-box”). The existing literature digest also warns that matched moments do not establish “membership in the hard core’s action class” (`T/LIT_QLM.md:3`). These inputs prevent substituting regulator convergence for RG admission or VC1 identification.

## **Consumers.**

- **GB1-H / H-class.** The weakest useful hand-off is a specified admissible small-coupling start, possibly after a proved block transformation, or a proved extension of the hard-core bounds. Y2 expressly allows either domain membership or that its “bounds extend to `S_fw`” (`T/TOE_ASSEMBLY.md:618`). Exact finite-lattice equality with isotropic Wilson is therefore not the only stated route.

- **GA2 / T0-start and T0-rate.** The request needs CT1–CT4 from each admitted start, with constants “independent … of `μ` within the class” (`T/GA2_Y2_DRAFT.md:211`). Its quantitative consumer additionally needs \(O((a_{k_0}/r)^p)+O(g(r)^4)\), \(p>0\) (`same file:213`, “T0-rate”). These remain “requests, not established branch results” (`T/GA2_Y2.md:178`).

- **Y3 / LZ1.** The required symmetry statement is O(4) restoration for the relevant continuum gauge correlations. The assembly asks to “prove O(4) restoration from `O_h x Z_2(time)`” (`T/TOE_ASSEMBLY.md:619`). LZ1 then consumes “O(4) restoration plus OS reconstruction” (`same file:603`).

- **YM RO1, if reused for these starts.** It needs the mirror, continuum Hilbert/cube-cone, and growth interfaces on the same realization (`Y/library/ro1.md:52,64–68`, “same realization”; “diagonal mirrors”; “state-uniform TU10”). For the narrower O4-2 route, connected separated two-point data suffice, with its retained inputs (`Y/library/o4-two-point.md:188`, “connected plaquette-action-density two-point function”).

- **Y1 and the physical-law assembly.** A finite-torus isotropy result alone leaves the infinite-lattice representation and selected-state relation open. Y1 asks for a “local, gauge-invariant action `S_fw`, reflection positive in time” on `Z³ × Z` (`T/TOE_ASSEMBLY.md:617`). GB1E explicitly retains “Y1 on `Z³ × Z`,” E-2, and VC1 as open inputs (`T/GB1E.md:15`).