# VERDICT: CONFIRMED WITH CORRECTIONS

## 1. Lemma C, parse lemma, and Gauss law

Confirmed. Write \(G_x^a=P_xQ_x^aP_x\). For incompatible markers, the exact parser finds \(P_xP_y=0\), so both \(G_x^aG_y^b\) and its reverse vanish. For compatible markers, the projectors are invariant under the other generator’s colour moves and the quantum registers are disjoint; therefore the generators commute. The exhaustive Z¹ and Z³ checks cover every displacement whose supports overlap ([Z¹ parser](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_tokens_z1_links_lowmem.py:60), [Z³ parser](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_z3_lowmem.py:63)).

Likewise, because \(P_x\) commutes with every component of \(Q_x\),

\[
[P_xQ_x^aP_x,P_xQ_x^bP_x]
=P_x[Q_x^a,Q_x^b]P_x
=if^{abc}G_x^c
\]

on the full Hilbert space—not only the parsed sector.

The worker’s parse test covered colour moves, but pair creation also changes occupancy. I added an independent exact predicate-pullback check; it found no projector toggles for any Z¹ colour pair or any compatible Z³ displacement ([checker](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/referee_checks.py:100), [results](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/referee_checks.out:3)). Combined with the explicitly singlet \(qA\) and \(Bp\) pair-creation operator, this closes full-space gauge invariance of the local Hamiltonian.

Thus the kernels of the commuting generators define a valid Gauss-law space under the preregistered definition ([PREREG.md:15](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/PREREG.md:15)). It is, however, a highly reducible, state-controlled gauge representation: SU(3)\(_x\) acts trivially outside valid marker sectors. “Lemma C” should have been written explicitly rather than merely invoked at [REPORT.md:81](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:81).

## 2. Z¹ matter-only reproduction

Reproduced for \(L=14,16,18\), one process, peak RSS 223,805,440 bytes:

- SU(3) error: \(1.1\times10^{-16}\)
- Casimir error: \(2.2\times10^{-16}\)
- all cross-commutators: exactly zero
- translation-covariance error: exactly zero
- maximum active cells: 2
- floating, nonuniform gaps appear at \(L=16,18\)

These match [col1_tokens_z1_full.out:1](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_tokens_z1_full.out:1)–[9](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_tokens_z1_full.out:9).

Evidence correction: the low-memory linked script defaults to offset 0 and sets both covariance fields to `nan` ([lines 87–89](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_tokens_z1_links_lowmem.py:87), [189–202](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_tokens_z1_links_lowmem.py:189)), despite its hard-coded “all 19 offsets” header. Therefore [REPORT.md:146](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:146) overstates what the low-memory rerun reproduced. Covariance nevertheless follows exactly from translating the definitions.

## 3. Class Q, OWN, and CAP

Class Q is confirmed within its stated domain: finite-range, elementary quadratic number-conserving or BdG charges, with a nontrivial gauge point in every translation orbit. A representation of \(\mathfrak{su}(3)^{|I|}\) on the one-particle space needs \(N\ge3|I|\); on a sufficiently large torus finite support makes translation orbits free, so \(|I|=kN\), producing \(N\ge3kN\), impossible. Twisting does not change that count ([REPORT.md:30–39](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:30), [quadratic checker](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/scripts/col1_quadratic.py:58)).

OWN needs a substantive correction. The commuting-algebra decomposition in [REPORT.md:48](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:48) is correct, but it yields private algebraic tensor factors, not necessarily private physical qubits. An entangling basis change can encode two commuting SU(3) factors across the same multi-qubit overlap. The explicit four-qubit counterexample has zero cross-commutator while both algebras act quantumly on both shared qubits ([referee_checks.py:237](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/referee_checks.py:237), [output](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/referee_checks.out:1)). Therefore the claimed universal requirement of “private physical qubits” is not proved.

CAP remains correct when “simultaneously carry” means one joint sector is nontrivial under all \(k\) gauge factors: that sector has dimension at least \(3^k\), hence \(3^k\le2^n\). It does not bound gauge factors that occur only in mutually exclusive direct-sum sectors.

## 4. Fixed COLOUR-SPREAD-OK reading

Met as fixed in [TESTS.md:78–94](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/TESTS.md:78): exact commuting local SU(3), a nontrivial Gauss-law physical sector, one-step translation covariance of the law, and finite range all hold.

The scope is narrower than a cubic QCD lattice theory:

- The fixed-offset linked marker sector is crystalline, but a translation-breaking thermodynamic ground state was not proved; the report itself lists a translation-invariant ground state as untested ([REPORT.md:106](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:106), [127](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:127)).
- The Z³ rods privilege the \(x\)-axis and fail cubic rotations ([REPORT.md:91–97](/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/chirality_ex/ref_COL1/REPORT.md:91)).
- Continuum Yang–Mills/QCD dynamics, confinement, fermionic statistics, and QCD universality remain open.
- The disentangler literature is contextual rather than coverage: Seifnashri–Shirley proves a finite-symmetry 1+1D result, while Thorngren–Preskill–Fidkowski constructs U(1) rotor examples, not this finite-qubit SU(3) construction ([Seifnashri–Shirley](https://arxiv.org/abs/2503.09717), [Thorngren–Preskill–Fidkowski](https://arxiv.org/abs/2601.04304)).

**Strongest correct statement.** A single two-dimensional on-site Hilbert space cannot carry nontrivial SU(3), and a one-mode-per-site theory with elementary finite-range quadratic colour charges cannot distribute an independent exact SU(3) Gauss generator at every translation-related point; nevertheless, one-qubit sites can collectively carry exact finite-range, one-step-translation-covariant SU(3) through gated many-body representations, with a well-defined commuting Gauss law and gauge-invariant local dynamics. The demonstrated construction is kinematic, state-controlled, anisotropic in Z³, and sector-crystalline; it neither forces private physical qubits nor establishes cubic symmetry, a translation-breaking ground state, or QCD universality.