## **Searches run.**

- Read `ref/README.md` first. It identifies `ref/pr10126/` as the gauge–matter consolidation and `ref/ym/` as the YM branch corpus.
- Initial terms: `CG16D`, `spinor`, `spinon`, `deconfined`, `centre class`, `center class`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-up terms: `composite sixteen`, `fractionalisation`, `moving spinor`, `spinor-class charge`, `R-CG1`, `10027`, `10038`, `10045`, `Spin(10)`, and `chiral matter`.
- Read relevant consolidation sections, TOE status blocks and theorem statements, drafts, referee reports, `LIT_SMG.md`, and `LIT_QLM.md`. Used only the permitted file commands.

Paths below use:

- **T/** = `repo/.claude/science/physics-loops/toe-assembly-20261104/`
- **G** = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`
- **C** = `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`

## **Already in the repo.**

- **The five-mode selector selects Fock content conditionally.** #10014 assumes the full Bogoliubov group and reads a parity half as Weyl species. Its minimum is five modes. It does not construct propagating spinor matter. **G:582**: “one fermion-parity half read as Weyl species”; **G:1132**: “Read #10014’s ‘protected content’ as a property of the Fock content only.” The consolidation is `bounded_theorem`, with author-review status. **G:3,11**: “claim_type: bounded_theorem”; “These are author statements for review.”

- **Free five-mode bands and fixed-site composites already have representation obstructions.** #10023’s invariant free bands carry vector content. #10027 extends the obstruction to arbitrary invariant interactions on fixed finite sets of five-mode sites with site-bilinear Spin(10). Infinite-volume superselection sectors lie outside its scope. **G:827**: “The 16 is the site’s Fock space, not a propagating multiplet”; **G:979**: “infinite-volume superselection sectors are outside it”; **G:987**: “every fermion-parity-odd excitation is in the vector class”.

- **Literal Z4 centre gauging was tested.** Logged #10045 supplies Z4 links and exact Gauss operators. The odd centre charge remains static. Link-created charge-one defects are Spin(10) singlets, with bosonic exchange sign. It also records the fusion data relevant to unpaired-site spinons. **G:1204**: “a 16 is never a mobile gauge charge”; “16 x 16 has no singlet”; “16^4 has two”. Its limit is explicit: “Not shown: any deconfined phase, spinon dynamics, statistics or spatial spin-1/2.”

- **Deconfined gauge structure alone has not selected a 16.** #10021 gives a supplied rung-two Z2 stabilizer model with deconfined bosonic point charges. Its tested fermionic twist costs range and rotation symmetry. **G:789**: “the Z2 gauge theory is deconfined”; “the charge is a boson”; **G:790**: “keeps only 6 of the 24 rotations”. Its boundary excludes multiplet selection. **G:802**: “any selection of SU(3)xSU(2)xU(1), Spin(10), the 16 or three families.”

- **A moving spinor exists in a different, supplied site-count model.** Logged #10038 transfers whole five-mode sites. With its odd-site rule, vacancies and interstitials have spinor content and fermionic transfer. This changes the fixed-site premise. Its toy cones remain vector-like. **G:1202**: “sites may be absent from a lattice point”; “interstitial = 16 and vacancy = 16bar”; “the cones are vector-like”.

- **LW1-5 already treats mixed registers and static spinor class.** F/K give the matter-only tensor obstruction. A wider end-mixed register supplies a one-ended spinor-class operator, but not motion. Theorem SC fixes the centre-difference pattern under every tick. **T/LW1_5.md:171**: “Odd matter operators carry the odd exterior powers”; **:185**: “this construction alone gives no moving excitation”; **:196**: “A spinor-class charge does not move.” Status: **:5**: “FINISH: FROZEN”; **:16**: “its closures are themselves unrefereed.”

- **A non-bilinear Spin(10) action is already constructed.** S′ embeds Spin(10) through different actions on the two parity blocks. Odd off-diagonal operators contain spinor copies. The faithful one-mode hop excludes this embedding; alternative A retains the larger frame group. **T/LW1_5.md:149**: “16 copies of the half-spin representation”; “The faithful one-mode hop excludes this embedding”; **:165**: “an alternative, not an adopted law”.

- **SM subgroup content is weaker than a whole Spin(10) 16.** Frozen CH1 supplies odd one-site operators for all family members on both laws. On O these belong to tensor parents. Its O-M obstruction concerns whole exact-group multiplets, not every infrared realization. **T/CH1.md:142**: “All are odd”; “tensor representations `10,120,252`”; **:146**: “dimension at least 40”; **:150**: “not a proof that every possible infrared one-family spectrum must break the microscopic local gauge symmetry.”

- **Free field counts do not close the family problem.** MT1 counts twenty Weyl fields per five-mode free node, but their representations contain neither required family representation. **T/MT1.md:144**: “These contain neither the SU(5) `10` nor a Spin(10) `16`.” Its physical family claim remains open. **:29**: “MT1-ii as a physical family claim”.

- **Charged-sector work constrains any proposed spinon interpretation.** LZ1 excludes propagating odd node bands in the vacuum’s own GNS reading. RCS1 proves the observable algebra is even and restricts finitely localized odd factor sectors. These do not classify all nonlocal charged sectors. **T/LZ1.md:62**: “every odd light species … is flat”; **:66**: “does not exclude a charged representation”; **T/RCS1.md:64**: “Every `A∈𝔄^G` is matter-even”; **:16**: “assumes finite localization”.

- **Main has conditional charged-motion and dressing precursors.** The native-motion note supplies short-time motion and spectral trial weight, not a particle pole. The rotor note supplies an exact neutral-sector Gauss isometry, not a phase theorem. Both ledger rows are `bounded_theorem`, `unaudited`. **ref/main/docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:313–315**: “unavoidable short-time charge motion”; “whether this weight concentrates near a dispersing particle pole”; **ref/main/docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md:32**: “isometry V_g … into the exact Gauss space”. Ledger evidence: **ref/main/docs/audit/data/ledger/na/native_charge_motion_and_spectral_weight_bounds_bounded_theorem_note_2026-09-15.json:6,17** and **ref/main/docs/audit/data/ledger/ro/rotor_global_gauss_dressing_coulomb_variational_compression_bounded_theorem_note_2026-09-16.json:6,17**: `"unaudited"`; `"bounded_theorem"`.

## **Failed attempts on file.**

- **Mott composite sixteen.** The proposed odd site level is not an excitation above a Spin(10)-singlet site vacuum. The fixed-site centre theorem then blocks spinor quasiparticles. **G:1021–1022**: “a level above a degenerate 16 ‘moment’, not an … excitation above a singlet”; **G:987**: “never a spinor 16”.

- **Obtaining mobile spinor matter by gauging the centre.** The matter algebra has no charge-one operators; soft charge-one defects come from singlet link shifts. **G:1204**: “every matter operator has Z4 charge 0 or 2”; “Spin(10) singlets with Levin-Wen sign +1”.

- **Inferring propagation from an end-mixed spinor operator.** The construction changes a conserved centre sector. Its existence does not supply a moving excitation. **T/LW1_5.md:185**: “The operator changes a local centre sector”; **:202**: “changes a joint centre sector that the tick conserves.”

- **Extending the vector-class parity claim to reducible registers.** The recorded counterexample uses `S_+⊕S_-`. End-purity does not supply the scalar-lift hypothesis used by the proof. **T/LW1_5_REFEREE.md:217**: “The hypothesis does not give irreducibility”; **T/LW1_5.md:206**: “Lemma Z(ii) fails”.

- **Straight strings in frozen backgrounds.** Locked U-law states give no strings; the alternating witness gives transverse flatness. Extending the ray-label argument to all matter-filled states fails because distant hops can act on ray links. **T/RCS1.md:221**: “Locked states give no strings”; **:227**: “No general conservation theorem is supplied.”

- **Excluding collective deconfinement from link coherence or missing plaquettes.** Those attempted exclusions remain unsupported. **T/RCS1.md:223**: “do not exclude collective deconfinement”; **:225**: “Absence of a specified plaquette layer does not prove absence of loop condensation.”

- **Closing the mirror gap with the sixteen-Weyl toy.** This supplied SU(4) model does not construct CG16D’s carrier, and its gap result remains inconclusive. **C:723**: “an SU(4) model”; **C:802**: “no L-independent gap is shown.”

## **Overlap with this lane’s results.**

not run

## **Missed inputs.**

- **Start from #10027’s precise boundary and #10045’s negative result.** This separates fractionalized sectors from literal centre gauging. It avoids repeating a tested static-charge construction. **G:979**: “infinite-volume superselection sectors are outside it”; **G:1204**: “static c-number background”.

- **Use Theorem SC with its stated definition of spinor charge.** Any proposed escape must identify the changed premise or representation reading. The CG1 identification remains open. **T/LW1_5.md:52**: “A spinor-class operator anticommutes with the local centre implementer”; **:352**: “Open only as the owner reading R-CG1”.

- **Use RCS-P as the charged-sector intermediate target.** Mere string-limit existence does not supply propagation. The file specifies necessary ways around its transverse-flatness obstruction. **T/RCS1.md:219**: “two non-disjoint sectors at distinct transverse positions, or a sector that is not quasi-equivalent to its tick transform.”

- **Keep the nonlinear-action and subgroup routes distinct.** S′ changes the internal action. CH1’s carriers instead realize SM components inside tensor parents. Neither establishes a light spectrum. **T/LW1_5.md:149**: “Non-Bogoliubov embedding”; **T/CH1.md:150**: “operator-space result under R-M”.

- **Use motion and dressing bounds before claiming a particle band.** The main notes provide intermediate constructions and explicit limits. **ref/main/docs/NATIVE_CHARGE_MOTION_AND_SPECTRAL_WEIGHT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-15.md:315**: “whether this weight concentrates near a dispersing particle pole”; **ref/main/docs/ROTOR_GLOBAL_GAUSS_DRESSING_COULOMB_VARIATIONAL_COMPRESSION_BOUNDED_THEOREM_NOTE_2026-09-16.md:237**: “cannot … infer the true ground-state phase”.

## **Consumers.**

- **CG1:** needs one light chiral SM family with the stated hypercharges and completion. A whole unbroken Spin(10) multiplet is stronger than the stated SM alternative. **T/TOE_ASSEMBLY.md:440**: “Standard Model one-generation multiplet”; “physical identification P-HY”; “P-COMP”.

- **MT1 and LZ1:** need actual vacuum excitations with fermionic exchange, spatial spin one-half, and propagating charged-sector structure. Representation content alone is insufficient. **T/TOE_ASSEMBLY.md:380**: “on the vacuum of VC1”; “exchange sign `-1`”; **T/MT1.md:29**: “Neither is supplied by free-node counting.”

- **CH1:** needs the carrier in a local gauged light spectrum, with unwanted partners removed. The weakest useful CG16D input is a specified carrier and its exact symmetry, parity, and charged-sector interpretation. **T/TOE_ASSEMBLY.md:425**: “one Weyl 16, or the Standard Model multiplet”; “every doubler and every mirror gapped”.

- **VC1:** needs the carrier as an excitation of the same vacuum and law. A supplied cluster background does not meet that interface. **T/TOE_ASSEMBLY.md:502**: “the matter of MT1 is its particle-hole excitations”.

- **GA2/Y4:** needs the resulting chiral matter content and a local gauged measure for matter-inclusive RG. No direct CG16D consumer was found in the pure-gauge YM target. **T/TOE_ASSEMBLY.md:584**: “T0 is pure gauge”; “CH1-ii … is the entry point.”

- **FL1, EW1, CS1, and ST1 route A:** consume the completed CG1 interface. They need identified family charges; ST1 additionally names P-HY and P-COMP. **T/TOE_ASSEMBLY.md:602**: “CG1 -> FL1, EW1, CS1, ST1 (route A, P-HY, P-COMP)”.