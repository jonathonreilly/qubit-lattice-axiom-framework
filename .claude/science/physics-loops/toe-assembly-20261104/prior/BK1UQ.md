**Searches run.**

- Read `ref/README.md` first. It identifies the ledger location and the PR consolidation notes: “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).
- Initial terms: `central charge`, `charge capacity`, `charge-capacity`, `strict transporter`, `rishon`, `determinant character`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and `repo/.claude/science/physics-loops/toe-assembly-20261104/`.
- Follow-ups: `BK1UQ`, `BK1`, `bounded grading`, `finite.*register`, `Higgs`, `S(U(3)`, `determinant.square`, `finite.*charge.*spectrum`. Read relevant definitions, theorem statements, status blocks, referee corrections, consolidation passages, and ledger rows with `grep -n -i`, `sed -n`, and `head`.
- Path abbreviations below: `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`; `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`; `M` = `ref/main/docs/RECORDS_REGISTER_COLOUR_ONLY_THROUGH_TRIALITY_AND_SINGLETS_THE_SU3_CASE_BOUNDED_THEOREM_NOTE_2026-09-04.md`; `L` = `ref/main/docs/audit/data/ledger`.

**Already in the repo.**

- **The precise UQ target is already sketched, but remains open.** It fixes EW1’s transporter definition and asks for charge quantization, vanishing single-link matrices, and both defect floors: “Prove that every nonzero bosonic \(H\)-fixed charged component has charge in \(10\mathbb Z\)” (`T/BK1_TREE.md:683`). Its status is explicit: “a new candidate lemma. It is not a frozen negative” (`T/BK1_TREE.md:248`).

- **The smallest nilpotent-link rung predates this lane.** The gauge consolidation gives the one-rishon spin-half identity: “U is nilpotent (U^2 = 0), not unitary” (`G:263`). Its inputs are supplied: “the role assignment of fine sites” and “the spin S” (`G:273`). Status is author-side: “These are author statements for review” (`G:11`). This proves the elementary rung, not the U(5) charge-ten theorem.

- **Main contains an analogous one-rishon colour identity.** The supplied SU(3) model states “products U U = 0 on the one-rishon factor” (`M:53`). Its scope is “conditional supplied-model mathematics” (`M:14`). Ledger status is `"effective_status": "unaudited"` (`L/re/records_register_colour_only_through_triality_and_singlets_the_su3_case_bounded_theorem_note_2026-09-04.json:30`).

- **Charge and parity accounting are frozen inputs.** LW1-5 Z-U states that total local Gauss charge equals matter-number change and that “its matter parity is \((-1)^{\sum q_x}\)” (`T/LW1_5.md:242`). EW1 applies this to bosonic composites: “only even `q` occur” (`T/EW1.md:125`). LW1-5 reports “FROZEN 2026-11-05” (`T/LW1_5.md:5`); EW1 reports “FROZEN 2026-11-06” (`T/EW1.md:5`).

- **EW1 supplies the exact representation convention UQ needs.** Projected link products use a fixed irreducible decomposition and central charge “`q_r = p′ − p`” (`T/EW1.md:44`). Reverse traversal uses “its matrix adjoint, with the operator products reversed” (`T/EW1.md:50`). For the standard \(H=S(U(3)\times U(2))\), the fifth-root central element “lies in `H`” (`T/EW1.md:338`). These are separate ingredients of the proposed charge-ten argument.

- **GA2 already proves finite-spectrum obstructions, with weaker conclusions than UQ.** Corollary 2.2 says a finite register with nontrivial infinitesimal covariance has “no invertible covariant link” (`T/GA2_Y2.md:43`). Theorem 3.2 assumes “spectrum in K consecutive integers” and `[E,Y]=Y`, then gives a two-sided defect floor (`T/GA2_Y2.md:85`). Status: “FROZEN 2026-11-05” (`T/GA2_Y2.md:5`). Noninvertibility and a defect floor do not themselves assert that the whole charged matrix vanishes.

- **EW1 extends the grading floor to arbitrary charge and FMS alignment.** Lemma 6.3a assumes `[E,Y]=qY` (`T/EW1.md:295`). Theorem 6.3′ requires a cut crossed “exactly once” with fixed orientations, plus “(O), (C) and (A)” (`T/EW1.md:307`). Its scope remains bounded-cut transport: “The floor weakens as the cut grows” (`T/EW1.md:321`).

- **Sharp matter already obstructs persistent charged orbit components.** EW1 Lemma 6.4(3) concludes that, for a fixed triple realized at every tolerance in sharp-block-number states, “the central `U(1)` of `U(5)` fixes `v`” (`T/EW1.md:326`). This is state-dependent. It is not UQ’s proposed operator identity.

- **The same endpoint-capacity method already appears in a smaller charge sector.** CH1-5U-q Theorem 5.1 proves a triple hop “is nonzero exactly when `3≤m≤7`” (`T/CH1_5UQ.md:120`). Its proof uses the endpoint-number interval and states that the operator otherwise “vanishes” (`T/CH1_5UQ.md:122`). Status: “FROZEN 2026-11-06” (`T/CH1_5UQ.md:5`). This supplies a direct capacity-method predecessor, not the projected charge-ten result.

**Failed attempts on file.**

- **Same-order reverse evaluation failed.** EW1 records forward and reverse scalar factors that differ in the \(m=1\) sector: “these are `1` and `0`” (`T/EW1.md:392`). Definition 2.3 repairs reversal using adjoints (`T/EW1.md:50`: “do not replace it by a fresh same-order evaluation”).

- **The original alignment floors omitted classicality.** The referee’s empty-matter example satisfies orbit and alignment at every tolerance but “fails (C)” (`T/EW1_REFEREE.md:253`). The failing step identifies the symmetrized norm polynomial with the unsymmetrized operator norm; the referee says they differ by a commutator term “which (C) controls” (`T/EW1_REFEREE.md:130`).

- **Copying the orthogonal coherent-link construction to U(5) stopped at one-link quality.** EW1 names the failing step: “one L5-U link can be prepared with transport near a group element” (`T/EW1.md:357`). The recorded bounds are fundamental norm \(1/2\) and adjoint fidelity \(3/10\), in that same passage.

- **Using existing floors to exclude every U-law FMS construction failed.** The rejected step is “every R-FMS alignment operator raises a bounded grading through a bounded cut” (`T/EW1.md:359`). Neutral data are grading-blind; charged cut floors decrease with cut size (`T/EW1.md:359`: “decays like `n^{−2}`”).

- **Collective correlated transport has no exhibited state there.** EW1 names the stopping point: “such a state of L5-U is exhibited” (`T/EW1.md:361`). It immediately records: “No state is exhibited here.”

- **A blanket triple-transport exclusion failed.** CH1-5U-q explicitly refutes “the proposed step that one link cannot carry a triple” for \(3\le m\le7\) (`T/CH1_5UQ.md:124`). The failing step ignores the available endpoint-number width.

**Overlap with this lane’s results.**

not run.

The tree labels UQ “OPEN” (`T/BK1_TREE.md:232`) and says “no node below is proved by this file” (`T/BK1_TREE.md:1`). There are no lane results to classify.

**Missed inputs.**

- **Use the frozen projected-product conventions before normal ordering.** They already pin the charge sign, decomposition, ordering, and adjoint reversal (`T/EW1.md:44`: “a fixed decomposition into irreducibles”; `T/EW1.md:50`: “operator products reversed”). This makes the lane’s unresolved step precise: “including multiplicities and ordering” (`T/BK1_TREE.md:288`).

- **Use CH1-5U-q’s capacity proof as the immediate finite-register precedent.** Its number interval is exactly “`max(0,m-5),…,min(5,m)`” (`T/CH1_5UQ.md:122`). It would supply the existing spectral-capacity argument to adapt, while leaving the new charge-ten and representation-projection steps explicit.

- **Keep neutral electroweak data outside the obstruction’s scope.** EW1 provides a neutral vector with “central charge 0” (`T/EW1.md:336`). It warns that the bounds do not establish charged data are necessary “for EW” at the Lie-algebra level (`T/EW1.md:342`). This limits downstream conclusions to the stated \(H\)-fixed, centre-breaking BK1 target.

- **A determinant interaction changes the law’s symmetry.** The local literature digest says a nonzero single-flavour determinant occurs at \(m=N\), but “It changes the gauge symmetry” (`T/LIT_QLM.md:23`). It cannot silently serve as spontaneous breaking of the unchanged U(5) law.

**Consumers.**

- **BK1’s strict U-law branch needs only the two transport-defect floors.** The tree says UQ “Decides whether the entire strict U-law BK1 branch is viable” (`T/BK1_TREE.md:668`). A floor of one in either required transport inequality already blocks arbitrarily small tolerance; the target explicitly requests both floors (`T/BK1_TREE.md:240–246`: “every strict transporter has a vanishing charged summand”).

- **BK1-T1 needs the exact boundary between strict paths and networks.** Its dependency list includes “UQ, R6, R8” (`T/BK1_TREE.md:312`). The weakest useful output identifies which strict-path hypothesis a network must remove. The lane brief requires precisely that and adds: “Do not claim that extension satisfies FMS” (`T/BK1_TREE.md:689`).

- **EW1, VC1, and CG1 consume the eventual BK1 phase statement.** The assembly names BK1 as “feeds EW1, VC1, CG1” (`T/TOE_ASSEMBLY.md:753`). UQ alone supplies a restriction on the strict U-law construction route; the larger target still requires “a VC1 vacuum of a live law” with “the 5 split as 3+2” in that same line.

- **Direct YM-branch consumers:** none found.