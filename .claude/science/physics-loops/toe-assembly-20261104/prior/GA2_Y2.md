## **Searches run.**

Paths below are relative to `~/toe-worker`. Abbreviations:

- `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`
- `D` = `ref/main/docs`
- `P` = `ref/pr10126/docs`
- `M` = `ref/pr10135/docs`
- `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030`

Read `ref/README.md` first. It identifies the consolidation notes and the ledger location: “Each has a *CONSOLIDATED* note” and “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2–3`).

Used `grep -rl -i` with these term groups over `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `T`, including drafts, referees, other parts, and literature notes:

- `rishon`, `quantum.link`, `invertible.*link`, `finite.register`.
- `small.coupling`, `strong.coupling`, `CT1`, `T0-start`.
- `finite.*truncat`, `weak.coupling`.
- `453600`, `cube.*antisymmetr`, `bounded.*flux.*floor`, `invertible.*covarian`.

Followed relevant hits with single-file `grep -n -i`, `sed -n`, and `head`. Read `briefs/ga2ref.txt`; it describes the three drafts as the lane’s pass-1 sources: “Claude drafted it” (`briefs/ga2ref.txt:1`).

## **Already in the repo.**

- **Target and present status.** GA2 asks for continuum correlator agreement with errors `O((a/r)^p) + O(g_i(r)^4)` (`T/TOE_ASSEMBLY.md:405`, “agrees with continuum”). Y2 asks for RG-domain membership or extended bounds (`T/TOE_ASSEMBLY.md:574`, “T0 is stated for the Wilson action”). The lane is “FROZEN 2026-11-05” (`T/GA2_Y2.md:5`). Its results remain conditional model statements: “They do not establish a continuum theory” (`T/GA2_Y2.md:7`). Y2 and Y2-W remain open (`T/GA2_Y2.md:11`, “No law is excluded”).

- **Exact finite-register Gauss laws precede this lane.** Consolidated #9926 supplies finite U(1) links, rishon-dressed hops, plaquettes, and SU(3) endpoint actions. Its scope includes an “exact continuous U(1) gauge group although E has finitely many levels” (`P/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:252`). It derives neither the supplied register choices nor a continuum limit: “No role assignment, spin S, coupling or continuum limit is derived” (same line). Consolidation status is explicitly “author statements for review” (same file:11).

- **Gauge-invariant loop constructions and classical limits also precede it.** Consolidated #9968 records covariant SU(2)/SU(3) rishon links, gauge-invariant many-body loops, loop completeness, a classical Yang–Mills energy expansion, and harmonic speed one. These concern a supplied nested-face model and supplied cutoff identification (`P/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:349`, “Finite diagnostics of supplied models”). The interacting register’s “Confinement, running and the continuum limit … are not computed” (same file:27).

- **A close prior transporter obstruction and a positive approximation route exist.** The Peter–Weyl compression note records an exact SU(3) cutoff defect: “D_R has eigenvalue1 and ||D_R||=1” (`D/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:64`). It also gives energy-controlled approximation despite that defect: “the bound tends to zero for uniformly bounded electric energy” (same file:77). Its older general negative argument has “formal negative certification … deferred” (same file:40). Current ledger status is `"audit_status": "unaudited"` (`D/audit/data/ledger/ga/gauge_wilson_pw_compression_shell_and_energy_path_bounds_bounded_theorem_note_2026-09-07.json:6`).

- **Finite-region observable approximation is already available for a supplied Wilson Hamiltonian.** The local Peter–Weyl theorem combines finite-neighborhood dynamics and energy-priced finite-carrier errors, uniformly in ambient volume. It explicitly excludes “a uniform all-energy fixed-R approximation” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). It takes no spatial continuum limit (same file:87, “does not … take a spatial continuum limit”). Its ledger is unaudited (`D/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:6`).

- **Finite-image and positivity examples exist, with different laws.** The clock carrier has a “controlled small-field tangent” equal to three-dimensional Maxwell theory (`D/U1_FINITE_CLOCK_GAUGE_MATTER_AND_CONTROLLED_TAME_MAXWELL_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:38`). Its additive-flux comparison uses a “controlled no-wrap sector” (same file:70). Separately, Gaussian smoothing supplies a positive electric extension under a stated smallness condition (`D/FINITE_CLOCK_GAUSSIAN_SMOOTHING_POSITIVE_LOCAL_ELECTRIC_EXTENSION_AND_FLUX_SCALING_EQUIVALENCE_BOUNDED_THEOREM_NOTE_2026-09-15.md:15`, “positive electric extension”). Both ledger rows are unaudited (`D/audit/data/ledger/u1/u1_finite_clock_gauge_matter_and_controlled_tame_maxwell_bridge_bounded_theorem_note_2026-09-03.json:6`; `D/audit/data/ledger/fi/finite_clock_gaussian_smoothing_positive_local_electric_extension_and_flux_scaling_equivalence_bounded_theorem_note_2026-09-15.json:6`).

- **Strong-coupling gap work does not supply Y2’s weak window.** The MDTN note states a volume-uniform physical gap for fixed truncated SU(2)/SU(3) Hamiltonians (`M/MDTN_TRUNCATED_GAUGE_STRONG_COUPLING_PHYSICAL_GAP_BOUNDED_THEOREM_NOTE_2026-10-31.md:148`, “gap_phys(L) ≥ 4(1 − c₁|δ|) − 2ε_L”). Status is “proposed (unaudited)” (same file:14), and the BHM-dependent step remains an “open obligation” under repository policy (same file:31). Its replacement supporting note supplies finite Gauss-projector lemmas and cycle support, also “proposed (unaudited)” (`M/MDTN_TRUNCATED_GAUGE_SUPPORTING_LEMMAS_LEAN_READY_NOTE_2026-11-01.md:13`, and :101, “Z_p 1-cycles”).

- **An all-coupling cube gap is a different result from a cube-product defect floor.** The compact SU(3) cube note gives a positive gap on twelve full Wilson links (`D/GAUGE_WILSON_COMPACT_CUBE_ALL_COUPLING_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:32`, “gap(H on Hphys) >= … > 0”). It says “not a volume-uniform, continuum or QCD/Yang-Mills mass-gap statement” (same file:34). Its ledger is unaudited (`D/audit/data/ledger/ga/gauge_wilson_compact_cube_all_coupling_gap_bounded_theorem_note_2026-09-07.json:6`).

- **The YM branch has the bare Wilson small-field input, not the requested general-start theorem.** Upper-chain Theorem 2 gives “<s_p> <= C_5/beta” (`Y/parts/upper-chain.md:282`), explicitly “at the bare scale only” (same file:286). CT1–CT4 demand source, locality, and pressure bounds with constants “independent of a and L” (same file:405–410). Overall branch status remains “Existence is not proved” (`Y/FINISH.md:11`).

## **Failed attempts on file.**

- **Finite-list SC ⇒ GA2.** The failing step is extrapolating one-scale, finite-support moments to the whole window. The referee constructs completions preserving SC while producing defects elsewhere: “every state satisfying SC has a completion outside those links that still satisfies SC” (`T/GA2_Y2_REFEREE.md:128`).

- **Unqualified exclusion of every Wilson identification.** Pass 1 assumed that an identification carries the Wilson link to the specified covariant operator. The referee identifies the missing hypothesis: “Its proof assumes one” (`T/GA2_Y2_REFEREE.md:130`).

- **Extending the obstruction to unbounded coarse generators.** The referee gives an unbounded summed-flux generator with a unitary raising operator: “Y is unitary” (`T/GA2_Y2_REFEREE.md:182`). The finite-block result survives; the infinite-generator extrapolation does not (`T/GA2_Y2.md:48`, “It fails for an unbounded summed-flux generator”).

- **Y2-W Attack 1: flux floor excludes SU(5).** Failing step: “every loop that sees `SU(5)` raises a bounded grading.” The cube product instead commutes with every endpoint number (`T/Y2W_DRAFT.md:141`, “[N^x_ℓ, Θ_c] = 0”).

- **Y2-W Attack 2: the bare electric corner is classical.** Failing step: “the corner is classical.” The recorded floors are kinematic and independent of the constants (`T/Y2W_DRAFT.md:147`, “Theorems W1 and W2 are kinematic”).

- **Y2-W Attack 3: blocking supplies a large-register vacuum.** Failing step: “the block state is close to a product of aligned coherent states.” The D-theory variant also fails the dimension count (`T/Y2W_DRAFT.md:153`, “leaves three Euclidean directions, not T0’s four”).

- **Y2-W-LB, m=3,…,7: three unsuccessful extensions.** The stopped steps are extending antisymmetric active states to all octants, assuming some end is always empty/full, and treating multi-rishon corners as permutations of three single-rishon colours (`T/Y2WL_DRAFT.md:287–289`, “It excludes the family, not every state”; “in every sector some end is empty or full”; “the corner operators are polynomials”).

- **High coherence ⇒ small loop defect.** The referee exhibits coherence tending to one while a plaquette has zero expectation and defect at least two (`T/GA2_Y2_REFEREE.md:204`, “A coherence bound is not a small-coupling statement”).

- **Band limitation decides kernel positivity.** The referee contrasts positive Fejér and sign-changing Dirichlet kernels with the same band (`T/GA2_Y2_REFEREE.md:208`, “band-limitation decides neither positivity nor its failure”).

- **Earlier small-register light-cone matching.** In the nested-face diagnostic, “the bare Hodge coefficients do not give the light cone” (`P/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md:405`). The missing repair is “The small-S dressed coefficients, which need a many-loop calculation” (same file:445).

## **Overlap with this lane’s results.**

“DUPLICATES” below distinguishes same-lane draft ancestry from independent prior work.

- **Theorems 2.1–2.2: EXTENDS the earlier finite-unitary transporter obstruction.** The prior note describes simultaneous “finite dimension, exact fundamental endpoint covariance and exact matrix unitarity” (`D/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:106`). The lane instead assumes an “invertible” link and a bounded generator (`T/GA2_Y2.md:30`). Its SU(3) cutoff norm-defect specialization was already on file (prior note:64, “||D_R||=1”). The spectral theorem itself **DUPLICATES** same-lane pass-1 Theorem N (`T/GA2_Y2_DRAFT.md:61`, “spectral obstruction”).

- **Theorem 2.3: DUPLICATES same-lane Proposition N4.** Both give finite-image links on `L²(K)` (`T/GA2_Y2_DRAFT.md:83`, “entrywise-commuting unitary link”; `T/GA2_Y2.md:40`, “If K=ρ(G) is finite”). The clock example is a special finite-image predecessor, not the general converse.

- **Corollary 2.4 and Y2-0: scoped continuation, with a CONTRADICTED unqualified draft claim.** Pass 1 says “For no PS-6r law … is the gauge sector Wilson’s lattice gauge theory” (`T/GA2_Y2_DRAFT.md:130`). The frozen scope says it “does not exclude an identification of gauge-invariant correlators” (`T/GA2_Y2.md:60`). The bounded-generator statement itself repeats N5 (draft:95).

- **Theorem 2.5: DUPLICATES same-lane Proposition R.** Both use factorization through another register sector to obtain the ranks (`T/GA2_Y2_DRAFT.md:118`, “rishon links factor through one register”; `T/GA2_Y2.md:62`, “rishon identities and ranks”). Earlier exact Gauss algebras are related inputs, not duplicate rank theorems.

- **Theorem 3.1: DUPLICATES Lemmas 0 and 0′.** They already transfer SC plus the listed image’s small-field bound to a defect bound (`T/Y2W_DRAFT.md:64`, “SC gives SC-loop”; `T/Y2WL_DRAFT.md:299`, “Lemma 0 for a cube product”). The referee **EXTENDS** this with `εΘ≤36εµ` (`T/GA2_Y2_REFEREE.md:156`, “36ε_µ”).

- **Theorems 3.2–3.3: DUPLICATES Lemma F, W1 and W1′.** These already give the bounded-flux floor and the normalized U(5) plaquette constraint (`T/Y2W_DRAFT.md:84`, “bounded flux floor”; :94, “flux floor”; :102, “2/K_m^2 ≤ 8ε_μ + 6δ”).

- **Theorems 3.4–3.5: DUPLICATES W2 and W4.** The coherence bounds, reference states, and independent-copy averaging formula are already stated there (`T/Y2W_DRAFT.md:112`, “coherence gap”; :127, “Lemma W4”; :131, “k/(k + 5)” and “k/(k + 9)”). They do not duplicate the consolidation’s classical energy expansion.

- **Theorems 4.1–4.2: DUPLICATES same-lane cube lemmas.** Neutrality, CAR pairing, point factorization, corner types, spectators, particle–hole symmetry, and permutation formulas appear as B0/C/K/T/S/P/R (`T/Y2WL_DRAFT.md:65`, “commutes with every”; :122, “corner factorisation”; :169, “cyclic permutation”).

- **Theorems 4.3–4.4: DUPLICATES L0, L0-r and S∞.** The one-cube states and all-cube symmetrized state are already recorded (`T/Y2WL_DRAFT.md:187`, “Theorem L0”; :218, “every scale”; :245, “all block cubes; every scale; every m”).

- **Theorems 4.5–4.6: DUPLICATES B1/B2 and Remark F.** The draft already has the `1/453600` threshold and translated-order obstruction (`T/Y2WL_DRAFT.md:265`, “η < 1/453600”; :281, “two of these cubes have orthogonal supports”). No independent earlier match was found in the stated searches. The compact-cube spectral gap above concerns a different operator and quantity.

## **Missed inputs.**

- **Use the Peter–Weyl shell and energy bounds as an explicit comparison template.** They separate norm-one cutoff defects from controlled low-energy approximation (`D/GAUGE_WILSON_PW_COMPRESSION_SHELL_AND_ENERGY_PATH_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md:77`, “despite the exact norm-one defect”). This would make the required state and energy restrictions explicit; it would still require matching those registers to L5-U or L5-O.

- **Use the finite-region observable theorem to price locality, energy, time, and normalization.** It prescribes “First choose r … then choose R” (`D/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:75`). It could supply one component of a regulator comparison, within its supplied Hamiltonian.

- **Use the later GA1 magnetic-symbol construction.** Theorem 5.1 extends the m=5 reference symbol to all occupancies; Theorem 5.2 identifies the O-link symbol’s determinant-minus-one coset (`T/GA1_5.md:123`, “reference state”; :140, “det D=−1”). This provides a concrete observable dictionary. Its limit remains “a magnetic quadratic form, not the full electric-plus-magnetic energy” (same file:138).

- **Use the later observable-interface work.** Complete invariant two-point data determine the physical cyclic representation (`T/ZM1_OBS.md:45`, “determine the cyclic representation”). Its proposed GA2 interface still requires “a common dictionary and propagated errors” (same file:124). This sharpens what must replace finite-list SC.

- **Keep the actual vacuum obligation visible.** VC1’s symmetry and extremality conditions “do not select a unique state”; plaquette-dependent existence questions remain open (`T/VC1_5.md:234`). Explicit cube witnesses therefore cannot substitute for VC1.

- **Reduce the requested small-field input to the plaquette bound.** The referee already gives `εΘ≤36εµ` (`T/GA2_Y2_REFEREE.md:156`). The existing Wilson bound is only “at the bare scale” (`Y/parts/upper-chain.md:286`). What remains is its appropriate counterpart for the actual comparison start.

## **Consumers.**

- **GA2 / Y2 / GA2-i.** The weakest useful output is a quantified gauge-invariant correlator comparison across the required window, plus propagated errors. Exact Wilson-link identification is unnecessary. The target is correlator agreement (`T/TOE_ASSEMBLY.md:405`, “up to errors”), and Y5 explicitly asks for a rate (same file:577, “T0 as stated gives existence of a limit, not a rate”).

- **ZM1’s interacting-map work.** Its recorded c-number-reduction attack uses only the state-independent coherence bounds. It stops at “the link operators act as c-numbers” (`T/ZM1.md:382`). Its linear-field obstruction also uses the bounded-charge obstruction, then strengthens it to nilpotence (`T/ZM1.md:335`, “here it is nilpotent”).

- **GA1’s reference-symbol work.** It needs the particular Slater and diagonal-involution reference states, not a continuum theorem (`T/GA1_5.md:27–28`, “DUPLICATES the m=5 Slater reference symbol”; “EXTENDS the L5-O reference state”).

- **EW1’s transport bounds.** It consumes the specific rishon product identity, square-zero expectation bound, and bounded-flux floor (`T/EW1.md:245`, “Frozen GA2_Y2.md Theorem 2.5”; :278, “For square-zero X”; :305, “Apply it … and sum”). It needs these scoped inequalities, not exclusion of either law.

- **Requested YM extensions.** T0-start[G] needs controlled starts and uniform RG bounds; T0-rate needs quantitative continuum and running-coupling errors. These remain requests: “Neither is proved” for the alternative QLR/D routes, and the general-start requests are “not established branch results” (`T/GA2_Y2.md:169`). For the immediate SC diagnostic, the weakest added estimate is the selected start’s plaquette small-field bound; the cube bound follows from R1 (`T/GA2_Y2_REFEREE.md:313`, “needs only the plaquette bound”).