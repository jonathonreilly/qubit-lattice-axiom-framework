## **Searches run.**

- Read `ref/README.md` first. It identifies the ledger location and consolidation sources: line 2, “Ledger rows: main/docs/audit/data/ledger/”; line 3, “Each has a *CONSOLIDATED* note.”
- Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/` for: `CG16S`, `spinor 16`, `tensor class`, `deconfined spinon`, `site bilinear`, `Spin(10)`, `spinon`, `composite sixteen`, and `Fock content`.
- Followed relevant hits into consolidated notes, ledger rows, TOE status blocks, theorem statements, drafts, referee reports, and `LIT_HIGGS.md` and `LIT_SMG.md`. The lookup for `briefs/CG16S.txt` found no file.
- Path abbreviations below:
  - **T** = `repo/.claude/science/physics-loops/toe-assembly-20261104`
  - **G** = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`
  - **C** = `ref/pr10131/docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`

## **Already in the repo.**

- **The target already distinguishes family content from a literal spinor.** CG1 permits the Standard Model multiplet or a branched 16. MT1 requires physical excitations on the VC1 vacuum. PS-5 supplies five modes, without supplying a propagating 16. Sources: `T/TOE_ASSEMBLY.md:440`, “equivalently the 16 of `Spin(10)`”; line 380, “on the vacuum of VC1”; line 129, “even the fallback does not by itself give the 16.”

- **#10014 selects five modes only under its supplied Fock-content reading.** Its minimum is \(N=5\) under the full Bogoliubov group, stated anomaly tests, and mass protection. It does not identify Fock states with propagating species. This is a carried bounded result in an author-side consolidation. Sources: `G:590`, “read as 2^(N-1) Weyl species”; `G:743`, “an inserted identification, borderline”; `G:1132`, “Read #10014's ‘protected content’ as a property of the Fock content only.” Status authority: `G:11`, “These are author statements for review.”

- **#9894, #10023 and #10027 already separate site states from fields.** #9894 supplies a generation-like multiplicity pattern without chirality. #10023 gives vector content for invariant free bands. #10027 extends the obstruction to interacting excitations on any fixed finite set of five-mode sites with summed site-bilinear Spin(10). Infinite-volume superselection sectors are outside that theorem. Sources: `G:23`, “without chirality”; `G:827`, “The 16 is the site's Fock space, not a propagating multiplet”; `G:979`, “infinite-volume superselection sectors are outside it”; `G:987`, “never a spinor 16.” These are carried results under supplied models, subject to `G:11`’s author-review status.

- **#10038 tests changing the site count.** An odd site-count change has spinor class. Fermionic statistics additionally use the supplied odd-site rule. A finite vacancy band moves, but the toy cones remain vector-like. Status: **logged**, supplied model and finite diagnostics. Source: `G:1202`, “a change of site count by dn carries a spinor class iff dn is odd”; “with no further rule, bosonic spinor defects exist”; “the cones are vector-like.”

- **#10045 tests literal centre gauging and records spinon kinematics.** In its supplied Z4-link model, odd spinor charge is a static background. The spinon construction does not establish deconfinement or motion. Status: **logged**. Source: `G:1204`, “a 16 is never a mobile gauge charge”; “Not shown: any deconfined phase, spinon dynamics, statistics or spatial spin-1/2.”

- **Frozen LW1-5 extends the centre analysis to finite registers.** F/K distinguish matter tensors from half-spin site states. End-mixed registers can carry spinor-class operators, including a one-ended construction. Theorem SC says their local centre-class discrepancy stays fixed in place. Sources: `T/LW1_5.md:171`, “tensor rather than spinor class”; line 187, “Theorem SC (static spinor class)”; line 196, “A spinor-class charge does not move”; line 202, “They do not make every fermion-odd operator tensor class when registers are end-mixed.” Status: line 5, “FROZEN”; line 16, “its closures are themselves unrefereed.”

- **A different internal Spin(10) action is already constructed.** S′ acts as a half-spin representation on one parity block and trivially on the other. Its odd operator space contains half-spin copies. The faithful one-mode hop excludes it; a separate full-frame law retains it. This is an alternative, not an adopted law. Sources: `T/LW1_5.md:149`, “16 copies of the half-spin representation”; “The faithful one-mode hop excludes this embedding”; line 167, “This is an alternative, not an adopted law.”

- **Standard Model subgroup carriers already exist without a full Spin(10) spinor field.** Frozen CH1 Theorem F supplies odd one-site operators \(c\), \(ccc\), and \(c^5\) with the family’s subgroup charges. On O they lie in tensor parents. O-M excludes a complete 15/16-dimensional family as one full microscopic Spin(10) operator multiplet; it does not exclude every infrared family reading. Sources: `T/CH1.md:143`, “All are odd”; “tensor representations `10,120,252`”; line 147, “dimension at least 40”; line 151, “not a proof that every possible infrared one-family spectrum must break the microscopic local gauge symmetry.” Status: `T/CH1.md:5`, “FROZEN.”

- **The U law already has an anomaly-free twisted family as operator content.** CH1 U-A gives the anomaly-free line \(u(1,-3,5)\). Corollary U-T″ realizes \(u=-3\) at one site exactly for \(2\le m\le8\). CH1-5U identifies the twisted family as a pulled-back spinor representation. This does not construct light chiral particles. Sources: `T/CH1.md:182`, “They all vanish exactly on … `u(1,-3,5)`”; line 218, “exactly when `2 ≤ m ≤ 8`”; line 222, “operator content only”; line 7, “full global-anomaly conclusion is conditional on cited standard bordism theorems.”

- **MT1 already counts the auxiliary free fields.** Each five-mode law has twenty Weyl fields per cell. Their representations do not contain the desired family. This settles the free-node reading only. Sources: `T/MT1.md:144`, “These contain neither the SU(5) `10` nor a Spin(10) `16`”; line 150, “not as a physical family claim.” Status: line 5, “FROZEN”; “MT1 is open.”

- **Older main-branch charge algebra remains narrower than CG1.** The hypercharge note proves a traceless two-block ratio after a supplied scale choice. The Cl(3) embedding uses supplied commuting actions. Sources: `ref/main/docs/HYPERCHARGE_IDENTIFICATION_NOTE.md:5`, “bounded/conditional name-free algebra”; line 8, “No physical naming or charge-readout table”; `ref/main/docs/CL3_SM_EMBEDDING_THEOREM.md:25`, “matrix constructions, not a derivation of physical color.” Both ledger rows are `bounded_theorem`, `unaudited`: `ref/main/docs/audit/data/ledger/hy/hypercharge_identification_note.json:6,17` and `ref/main/docs/audit/data/ledger/cl/cl3_sm_embedding_theorem.json:6,17`.

- **Supplied spinor-field atomic models already have exact symmetric gaps.** They assume two or four copies of a chiral 16, rather than deriving those fields from five modes. Their boundary calculations retain unwanted modes. Source: `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md:28`, “CAR modes in two or four copies of the chiral 16”; line 15, “restores eight Weyl nodes.” Actual source status: line 7, “conditional-support.” Ledger: `ref/main/docs/audit/data/ledger/sp/spin10_symmetric_atomic_gaps_mirror_boundary_projection_and_current_response_bounded_theorem_note_2026-09-14.json:6`, `"audit_status": "unaudited"`.

## **Failed attempts on file.**

- **Promote the five-mode Fock 16 to a cone multiplet.** The failing step is the representation of creation operators. Source: `G:827`, “its cones carry the real vector 10”; “a 16 per cone … is false for the five-mode reading.”

- **Recover a composite 16 through fixed-site Mott interactions.** The failing step is the centre action on relative excitations. Composite fermions propagate, but remain vector class. Sources: `G:1036`, “extends #10023 A2 … to all many-body excitations”; `G:1079`, “they are vector-class tensors.”

- **Use site-count motion as the full chiral-family solution.** The supplied odd-site rule gives fermionic spinor defects, but the toy band admits an invariant mass. Source: `G:1202`, “An invariant staggered on-point energy gaps them all.” The consolidation also records the premise cost: `G:1139`, “bends the Lattice axiom.”

- **Gauge Z4 to make a mobile spinor.** Literal centre gauging pins the charge; soft charge-one Gauss defects are bosonic Spin(10) singlets. Source: `G:1204`, “static c-number background”; “Spin(10) singlets with Levin-Wen sign +1.”

- **Use mixed registers to infer unrestricted mobile spinors or universal vector class.** Mixed registers permit spinor operators, but SC keeps their centre discrepancy static. Separately, the reducible-register vector-class claim has an explicit counterexample. Sources: `T/LW1_5.md:202`, “changes a joint centre sector that the tick conserves”; line 206, “So Lemma Z(ii) fails.” The corrected statement retains tensor class for that counterexample.

- **Treat subgroup carriers as independent elementary modes or a complete light spectrum.** Ten triple products cannot form ten independent CAR modes on the 32-dimensional matter site. The elementary one-site U-family assignment also fails the anomaly ledger under AM-5. Sources: `T/CH1.md:125`, “cannot be ten independent CAR modes”; line 182, “For the one-site carriers they are `(-40,-400,-5)`”; line 224, “Under AM-5.”

- **Infer mirror gapping from anomaly cancellation or an atomic gap.** The 16-Weyl toy has an unresolved bulk gap, and supplied atomic boundary removal restores partners. Sources: `C:21`, “an inconclusive mirror gap”; `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md:15`, “restores eight Weyl nodes.”

## **Overlap with this lane's results.**

not run

## **Missed inputs.**

- **Use the corrected centre hierarchy before attempting composites.** Separate matter-only tensors, end-mixed register operators, and mobile centre charge. This prevents repeating #10027 or treating an operator’s existence as propagation. Sources: `G:979`, “fixed finite set”; `T/LW1_5.md:202`, “answered no for that notion”; “Whether CG1's ‘16’ needs a different notion … is … R-CG1.”

- **Choose the required family statement explicitly.** CH1’s R-B asks for subgroup components; R-M asks for a complete exact-group multiplet. These lead to different obligations on O. Source: `T/CH1.md:42`, “R-B asks for its individual components under a subgroup”; “R-M asks for a full exact-group multiplet.” The physical infrared identification remains open there.

- **Use the twisted U-family instead of the anomalous elementary assignment.** It changes the remaining task from finding representation content to binding composites, selecting chirality, and gapping mirrors. Source: `T/CH1.md:242`, “No proof binds the required composites into a chiral spectrum or gaps their mirrors.”

- **Use charged-sector results when considering nonlocal escapes.** RCS1 excludes certain finitely localized odd factor sectors from translation covariance, but does not exclude deconfinement generally. It also blocks gauge-invariant odd local composites. Sources: `T/RCS1.md:12`, “has no implemented nonzero cell translation”; line 64, “Every `A∈𝔄^G` is matter-even”; line 16, “Neither a coherence bound nor an absent specified plaquette layer rules out deconfinement.”

- **Use the repository’s literature mappings with their stated limits.** FMS projector constructions cannot manufacture the forbidden local spinor. Spinor interaction pullbacks do not turn composite carriers into independent canonical modes. Sources: `T/LIT_HIGGS.md:71`, “Nor can the construction manufacture a forbidden local `16`”; `T/LIT_SMG.md:86`, “does not turn their composite operators into independent canonical modes.”

## **Consumers.**

- **CG1 and MT1-ii.** They need a physical one-family carrier on the common law and vacuum. The weakest printed target permits the Standard Model multiplet; it does not require a microscopic full-group spinor. Sources: `T/TOE_ASSEMBLY.md:380`, “a 16 of `Spin(10)`, or the Standard Model multiplet”; line 440, “light chiral content.”

- **CH1.** It needs specified family fields and charges, then light chiral dynamics with all unwanted partners removed. Operator occurrence alone is insufficient. Sources: `T/TOE_ASSEMBLY.md:425`, “no extra light charged state”; `T/CH1.md:222`, “light, chiral dynamics and the mirror gap remain open.”

- **FL1.** Its current family-count definition needs a gauge module \(F\) and a realization satisfying CH1. It accepts the twisted U-family or O’s subgroup family. Source: `T/FL1.md:26`, “For U, `F` may be the twisted `R_u`”; “For O use the CH1 family `F_t`”; line 30, “This is an open existence condition.”

- **EW1 and ST1 route A.** EW1 needs the Standard Model subgroup and charge assignment through which the breaking is interpreted. ST1 route A needs the physical hypercharge and completion bridges. Sources: `T/TOE_ASSEMBLY.md:475`, “through the Standard Model group”; line 342, “P-HY, P-ABJ, P-COMP, P-REC.”

- **GA2 and the YM interface.** GA2 needs the realized matter representations for its matter-coupled continuum statement. No direct CG16S consumer was found in the searched YM registry; the assembly explicitly identifies matter as an extension beyond T0. Sources: `T/TOE_ASSEMBLY.md:413`, “with the matter of CG1”; line 421, “matter in the RG (T0 is pure gauge).”

- **CS1.** It needs the physical species and charges for its matter and baryon-asymmetry questions, rather than a particular microscopic spinor construction. Source: `T/TOE_ASSEMBLY.md:549`, “the baryon asymmetry follows from the law's CP and baryon-number violation”; line 551, “Imports: … CG1.”