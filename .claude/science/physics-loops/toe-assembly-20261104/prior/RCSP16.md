**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” and says each consolidation PR has a “*CONSOLIDATED* note” (`ref/README.md:2–3`).
- Initial terms: `RCSP16`, `RCS-P`, `straight.string`, `quasi.equivalence`, `deconfined spinon`, `Gauss dressing`, `charge motion`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-up terms: `Fredenhagen`, `spinor.class`, `spinon`, `charged.representation`, `boundary label`, `static charge`, `spectral weight`, `toric.code`, `fluctuating.loop`, `RC-W`, `plaquette`. Read relevant consolidation entries, ledger rows, TOE parts, drafts, referee reports, prior digests, `LIT_QLM.md` and `LIT_SMG.md`.
- Found the brief at `briefs/RCSP16.txt:1`: “Target: decide RCS-P for spinor-class sectors.” It permits either a construction or a negative result “for a named class of states or updates.”
- Citation prefixes: `T/` means `repo/.claude/science/physics-loops/toe-assembly-20261104/`; `M/` means `ref/main/docs/`; `G` means `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`.

**Already in the repo.**

- **The charged-sector reading is provisional.** The assembly selects straight-string limits with relative parity over parity-sharp backgrounds as “a named working candidate for lanes. It is not adopted” (`T/TOE_ASSEMBLY.md:225`). The brief asks for a node with “a nonzero leading generator”; it separately asks whether that node is a Clifford cone (`briefs/RCSP16.txt:1`).

- **The finite-site composite obstruction has an explicit boundary.** Consolidated #10027 covers fixed finite sets of five-mode sites with site-bilinear Spin(10). Odd excitations are “vector class, never the 16”; “infinite-volume superselection sectors are outside it” (`G:23,979`). Consolidation status is author-side: “These are author statements for review” (`G:11`).

- **Two older escapes have bounded results.** Logged #10038 gives site-count spinor defects, including “interstitial = 16 and vacancy = 16bar,” but their cones remain “vector-like” (`G:1202`). Logged #10045 supplies spinon fusion kinematics but says: “Not shown: any deconfined phase, spinon dynamics, statistics or spatial spin-1/2” (`G:1204`).

- **Local-GNS odd bands are already obstructed.** LZ1 decomposes D1 representations into conserved finite centre patterns. Its Theorem 2.2 makes every band in the nontrivial-pattern subspace “identically `1` on any connected `C¹` neighbourhood of a node” (`T/LZ1.md:50,62`). Its charged-sector boundary is explicit: “This does not exclude a charged representation” (`T/LZ1.md:66`). Status: “FROZEN” (`T/LZ1.md:5`).

- **Relative parity and localization are already formalized.** RCS1 defines `χ_tot` by a strong limit over all finite site sets. It is preserved by quasi-equivalence and direct sums and agrees with the vacuum-GNS grading (`T/RCS1.md:161,163,167`: “`χ_tot=−1` … on … `H_odd`”). For translation-compatible factor sectors over a cell-periodic background, the configuration difference is “empty or infinite”; finite localization forces `χ=+1` (`T/RCS1.md:185`). Status: “FROZEN” (`T/RCS1.md:5`).

- **The general ray obstruction is conditional.** If transversely displaced ray sectors are disjoint and each sector is quasi-equivalent to its tick transform, every band is “flat in both transverse directions at each node” (`T/RCS1.md:125`). RCS-P therefore requires failure of at least one hypothesis: “two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform” (`T/RCS1.md:219`).

- **The U(16)-rishon witness already supplies admissible laws and charged limits.** CG16B’s witness has separately gauge-invariant cube gates and a cell-covariant base tick (`T/CG16B.md:57`: “its base tick is cell covariant”). Lemma NN-W supplies exact finite nearest-neighbour compilation: “both witnesses meet NN-a read with their own registers” (`T/CG16B.md:74`). Example S supplies positive-norm string limits at `m=16`, “at any angles” (`T/CG16B.md:148`; `T/CG16B_REFEREE.md:170`: “`16^{2r+1}>0`”). CG16B is now “FROZEN”; its imported referee closures “are not themselves refereed” (`T/CG16B.md:5,15`).

- **Those rishon limits carry spinor class at the boundary.** Under (F), link-purity and the stated sharpness assumptions, Proposition L preserves every background centre value while giving “`χ_tot(π_∞:ω)=-1`” and a boundary label tending strongly to `χ_tot=-1` (`T/CG16B.md:137–140`). The repaired reading “does not establish an irreducible 16 or a band” (`T/CG16B.md:182`). Whether these sectors propagate remains RCS-P (`T/CG16B.md:11`).

- **The bilinear link-pure flux obstruction is stronger than sector nonexistence alone.** CG16D proves scalar flux on `L5-O[S_+]`: “every `Φ_Λ=1`,” so every representation has `χ_sp=+1` (`T/CG16D.md:45`). On other link-pure registers, its support theorem identifies `χ_sp=-1` with finite odd centre defects (`T/CG16D.md:55`). The referee’s Lemma N strengthens the band conclusion to “flat on a neighbourhood of each node” (`T/CG16D_REFEREE.md:122`). The report emphasizes: “The named step is propagation, not confinement” (`T/CG16D_REFEREE.md:219`).

- **D-reg escapes the scalar internal-link step.** Its transfer flips endpoint signs while preserving local gauge centres; its flux “is not central in `𝔄^G`” (`T/CG16D.md:95`). Theorem 9 supplies a columnar D1 state and a string-limit defect with “`χ_sp=−1`” (`T/CG16D.md:103`). The referee supplies NN-a compilation for the transfer layer, with a cell-covariant composite at `τ_E=0`; the base matter-gate compilation remains open (`T/CG16D_REFEREE.md:251`). The note header still says “Pass 2; not refereed or frozen”; the report recommends freezing after edits (`T/CG16D.md:5`; `T/CG16D_REFEREE.md:260`).

- **RC-W constrains a specified free reading.** It proves `W₃=0` for a translation-covariant finite product of bounded-block unitaries; “No `L_k` need commute with translations” (`T/CG16S_REFEREE.md:99`). Under setting F and condition E, a finite Weyl node set has zero net chirality. The scope expressly leaves open “defects over a filled or entangled background”; “Setting F has no links” (`T/CG16S_REFEREE.md:143`). This is a referee closure awaiting the stated freeze checks, not an audited universal charged-sector theorem (`T/CG16S_REFEREE.md:195`: “No independent second review was run”).

- **Loop layers and exact propagating comparison bands already exist.** Under NN-a, GA1-P-5 members have finite nearest-neighbour implementations (`T/GA1_5.md:7`: “every member … implementable”). Cube-supported layers give only flat physical bands in empty-matter D1 states (`T/GA1_5.md:160`: “every physical band … is `V=1`”). Swap layers evade that support hypothesis. GA15PHI, including its amendment, supplies the proposed R-Φ band for every `1≤m≤9`, but it remains “a conjugated neutral mode” (`T/GA15PHI.md:7`). It has “neither a Clifford cone nor a pair of photon polarizations” (`T/GA15PHI.md:125`). Status: frozen, with imported compilation closures (`T/GA15PHI.md:5,9`).

- **Exact Clifford-band engineering is also on file.** Frozen LZ1I constructs two neutral propagating bands with different Clifford speeds in a stationary, gauge-invariant, cell-invariant, half-filled state (`T/LZ1I.md:5`: “two neutral propagating bands of different Clifford speeds”). It expressly leaves the charged prescription open: “the present bands are neutral” (`T/LZ1I.md:216`).

- **Static charged spaces and path comparisons are available, with different targets.** The selected Wilson-source construction supplies a nonzero reducing charged subspace with two external probes (`M/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md:35`: “It is nonzero”). The finite-clock Villain construction supplies an “insertion-path-independent spectral bottom,” explicitly “not moving matter” (`M/FINITE_CLOCK_STATIC_CHARGE_TRANSFER_HAMILTONIAN_AND_PATH_COMPARISON_BOUNDED_THEOREM_NOTE_2026-09-15.md:4`). Both ledger rows remain `"effective_status": "unaudited"` (`M/audit/data/ledger/ga/gauge_wilson_selected_infinite_static_source_sector_bounded_theorem_note_2026-09-07.json:29`; `M/audit/data/ledger/fi/finite_clock_static_charge_transfer_hamiltonian_and_path_comparison_bounded_theorem_note_2026-09-15.json:29`).

- **An explicit Gauss dressing exists on a different carrier.** The integer-rotor/CAR note constructs an isometry for the entire neutral matter space on free cubic boxes (`M/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md:32`: “an explicitly constructed isometry”). It gives variational compression, not dynamical elimination: “The full Hamiltonian can leave its range” (`same file:237`). Ledger status is `"unaudited"` (`M/audit/data/ledger/ro/rotor_global_gauss_dressing_coulomb_variational_compression_bounded_theorem_note_2026-09-16.json:27`).

- **Charge motion and spectral weight have prior intermediate theorems.** The native-motion note gives low-energy spectral weight but “does not identify a single eigenvalue, a sharp particle pole, or a nonzero curvature of the lowest band” (`M/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:269–271`). The polarized-word construction has actual charge motion and a momentum-independent threshold that “is not an eigenvalue in a momentum fiber” (`M/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md:49–53`). Both ledger rows are `"unaudited"` (`M/audit/data/ledger/na/native_charge_motion_and_spectral_weight_bounds_bounded_theorem_note_2026-09-15.json:32`; `M/audit/data/ledger/po/polarized_word_carrier_and_essential_threshold_bounded_theorem_note_2026-09-15.json:31`).

- **Solvable loop comparators do not already supply RCSP16.** The three-axis Pauli construction has mobile toric-code vertex charges, but “The charges are bosons” (`M/THREE_AXIS_QUBIT_SITE_STABILIZER_RULES_UNSOLDERED_TORIC_CODES_MOVE_SOLDERED_MAXIMAL_RULES_DO_NOT_BOUNDED_THEOREM_NOTE_2026-10-17.md:46,48`). Cubic ice supplies equal-amplitude RK states and a finite fixed-charge orbit, but its ring moves “cannot move or create the fixed charges” (`M/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md:68,269`). Their ledger statuses are `"unaudited"` (`M/audit/data/ledger/th/three_axis_qubit_site_stabilizer_rules_unsoldered_toric_codes_move_soldered_maximal_rules_do_not_bounded_theorem_note_2026-10-17.json:31`; `M/audit/data/ledger/sp/spin_half_cubic_ice_exact_rk_coulomb_correlations_and_finite_qubit_photon_phase_bridge_bounded_theorem_note_2026-09-03.json:32`).

**Failed attempts on file.**

- **RCS1 A1: frozen backgrounds.** Locked states have zero string denominators. The alternating U-law example has transversely flat bands. The extended argument still requires empty matter and sharp end numbers; “this U-law argument does not transfer” to O (`T/RCS1.md:221`).

- **RCS1 A2: free links and Dirac clouds.** One-link coherence bounds block the proposed c-number-unitary approximation. The cloud argument fails because it has “no specified weights or sector decomposition” (`T/RCS1.md:223`). These bounds “do not exclude collective deconfinement” (`same line`).

- **RCS1 A3: loop condensation.** The missing step is a state: “No appropriate fluctuating-loop D1 state is constructed in the draft” (`T/RCS1.md:225`). Missing a specified plaquette layer does not establish absence of loop condensation (`same line`: “does not prove absence”).

- **RCS1 K: universal ray-label conservation.** Its proof uses distant hops annihilating the empty-matter state. In filled states, “hops can act on ray links”; “No general conservation theorem is supplied” (`T/RCS1.md:227`).

- **Literal centre gauging.** Logged #10045 finds the odd centre charge to be “a static c-number background”; “a 16 is never a mobile gauge charge” in that supplied construction (`G:1204`). This is distinct from its unresolved fractionalized-spinon route (`same line`: “Not shown: any deconfined phase”).

- **Reading the limiting charge at a finite endpoint.** CG16B’s original reading fails because relative class is “undefined for these non-finitely localized limits,” or is `+1` through the centre configuration (`T/CG16B.md:178`). The repaired reading uses boundary flux (`T/CG16B.md:179`: “Spinor class means the limit is `-1`”).

- **D-reg transfer plus the existing matching state.** The transfer “breaks matchings.” No update is supplied that both preserves the D1 state and moves the defect with nonzero `N_j`; an energy bound and base-tick NN-a compilation also remain open (`T/CG16D_REFEREE.md:251`).

- **Motion or static thresholds as substitutes for a band.** The Wilson-source theorem does not prove “existence of a charged bottom eigenvector” (`M/GAUGE_WILSON_SELECTED_INFINITE_STATIC_SOURCE_SECTOR_BOUNDED_THEOREM_NOTE_2026-09-07.md:90`). The polarized-word example has “no isolated lowest massive pair band at that threshold” (`M/POLARIZED_WORD_CARRIER_AND_ESSENTIAL_THRESHOLD_BOUNDED_THEOREM_NOTE_2026-09-15.md:266–267`).

**Overlap with this lane's results.**

not run

**Missed inputs.**

- **Start from Proposition L and Example S.** They already supply the U(16) witness’s odd boundary-flux sectors. The next obligation is their dynamics, rather than another existence construction: “Whether these sectors carry a band is RCS-P” (`T/CG16B.md:11`).

- **Keep the two flux identities separate.** CG16B’s (F)-identity contains `P_Λ F_{\partial Λ}` (`T/CG16B.md:122`). CG16D’s bilinear identity instead has a scalar matter contribution, “`=−1`” (`T/CG16D.md:39`), making link-pure flux central (`T/CG16D.md:37`: “central in `𝔄^G`”). These are different premises for transferring a static-label obstruction to the rishon witness.

- **Bridge D-reg’s label to the brief’s requested odd label.** Theorem 9 supplies `χ_sp=−1` (`T/CG16D.md:103`). The brief requests “boundary-flux label, chi_tot = -1” (`briefs/RCSP16.txt:1`). RCS1’s `χ_tot` construction assumes a “parity-sharp” background (`T/RCS1.md:161`). Using these inputs would make the required parity and label agreement an explicit obligation.

- **Use the existing NN-a and loop constructions for A3.** The owner requires gauge invariance and cell covariance “of the complete update only” (`T/TOE_ASSEMBLY.md:235`). GA1’s compilation and GA15PHI’s conjugation construction provide concrete loop-layer methods (`T/GA1_5.md:7`: “finite nearest-neighbour layers”; `T/GA15PHI.md:113`: “band conjugation”). LZ1I provides an exact Clifford-band construction, while retaining the limitation “the present bands are neutral” (`T/LZ1I.md:216`).

- **Use RC-W with its actual hypotheses.** It removes the periodic-layer gap, but its charged-sector application needs a bridge. The report explicitly leaves filled or entangled backgrounds open and says “Setting F has no links” (`T/CG16S_REFEREE.md:143`). This changes a blanket mirror claim into a conditional check on the constructed band.

- **Use dressing, mixed kernels and spectral weight as intermediate targets.** RCS1 already names these prior inputs (`T/RCS1.md:9`: “controlled charge motion and spectral weight”). They would replace an unspecified cloud with defined maps and correlators. Their limits remain essential: the rotor construction cannot “infer the true ground-state phase” (`M/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md:237`).

- **Fix the charged-sector tick implementation and phase convention.** ZM1-OBS records that equality of restricted invariant dynamics “does not establish a unique physical phase convention” (`T/ZM1_OBS.md:80`). Its twist theorem preserves slopes while shifting charged eigenphases (`T/ZM1_OBS.md:76`: “the same slopes after its eigenphase is shifted”). This matters when the target requires a node at eigenvalue one.

**Consumers.**

- **RCS-P and the owner’s R-CS decision.** A scoped existence or obstruction theorem is useful immediately. Adoption still waits for RCS-P and MT1-S in the VC1 vacuum: “adoption waits until those settle” (`T/TOE_ASSEMBLY.md:225`).

- **MT1-S and LZ1’s fermion clause.** They need more than a nonzero directional generator. MT1-S asks for the light odd excitations “in the VC1 vacuum” with “ER’s Clifford one-cone condition” (`T/MT1.md:154`). A band on a supplied witness is an intermediate result unless that common-vacuum identification is added.

- **CG1 and CH1.** CG1 needs the actual family representation and charges, not centre class alone (`T/TOE_ASSEMBLY.md:440`: “The light chiral content of one family”). CG16B warns that its reading “does not establish an irreducible 16 or a band” (`T/CG16B.md:182`). CH1’s weakest immediate input is a specified charged correlator construction: “a gauge-covariant dressing or a charge-sector prescription” (`T/CH1.md:43`).

- **CG16D-NLP.** On D-reg, it needs a stationary update carrying the defect with nonzero `N_j`, plus the separate deconfinement and energy statement. The report lists both “any energy bound” and motion preserving the D1 state as open (`T/CG16D_REFEREE.md:251`).

- **ZM1-OBS class (d).** It needs positive denominators and specified limiting translation-covariant amplitudes. The existing gap is that a common stationary kernel and its Fourier budget “have not been constructed” (`T/ZM1_OBS.md:233`). The finite-string data have “no transverse displacement data” (`T/ZM1_OBS.md:161`).

- **YM branch.** Direct RCSP16 consumer: none found. The named assembly extension is Y4: “T0 is pure gauge”; chiral matter lies “outside T0’s statement,” with CH1-ii as the entry point (`T/TOE_ASSEMBLY.md:584`). The weakest relevant RCSP16 contribution is a precise matter-sector construction compatible with that separate extension.