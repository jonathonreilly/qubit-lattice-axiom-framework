# Exact spectrum of a supplied eight-Majorana quartic

Claim type: bounded_theorem

Primary runner: [eight_majorana_quartic_finite.py](../scripts/eight_majorana_quartic_finite.py).

## Supplied finite model

Work on four qubits, with standard Pauli matrices and
\(\gamma_{2j}=Z^{\otimes j}\otimes X\otimes I^{\otimes(3-j)}\),
\(\gamma_{2j+1}=Z^{\otimes j}\otimes Y\otimes I^{\otimes(3-j)}\), for j=0,1,2,3.
These satisfy \(\{\gamma_a,\gamma_b\}=2\delta_{ab}I\).
For an increasing word abcd write \(\gamma_{abcd}=\gamma_a\gamma_b\gamma_c\gamma_d\).
Supply the Hermitian operator

\[
\Omega=\gamma_{0123}+\gamma_{0145}+\gamma_{0167}+\gamma_{0246}
-\gamma_{0257}-\gamma_{0347}-\gamma_{0356}
+\gamma_{4567}+\gamma_{2367}+\gamma_{2345}+\gamma_{1357}
-\gamma_{1346}-\gamma_{1256}-\gamma_{1247}.
\]

The theorem concerns H=W Omega for real W>0. The coefficient signs, four-qubit
carrier and Hamiltonian are supplied mathematical data, not derived physical
laws or newly approved framework primitives.

## Spectrum and proof

In the computational basis, Omega vanishes on the eight odd-weight strings.
It equals 2 on each of the six weight-two strings. On the ordered pair
(|0000>,|1111>) it is the matrix [[-6,8],[8,-6]]. All other entries vanish.
This follows directly by applying each displayed Pauli word: the six words
0123,0145,0167,4567,2367,2345 are diagonal; the other eight flip all four bits.
Their phase sum is 8 on weights zero and four and zero on weights one, two
and three. The six diagonal terms sum to -6,0,2,0,-6 at weights 0,1,2,3,4.
Thus Omega has eigenvalues -14 (once), 0 (eight times), 2 (seven times).
Its normalized ground state is (|0000>-|1111>)/sqrt(2), even under Z tensor Z
tensor Z tensor Z. H has unique ground energy -14W and excitation gap 14W.
The sign condition is essential: at W=0 every state is a ground state, and
at W<0 the ground multiplicity is seven.

## Antiunitary symmetry

Let K be computational-basis complex conjugation and
U=gamma_1 gamma_3 gamma_5 gamma_7. U is real, Hermitian and U squared is I:
four imaginary factors give a real product, and reversing four mutually
anticommuting factors gives sign (-1)^6=1. Conjugation by U changes the sign
of each odd-index gamma and leaves each even-index gamma fixed. K changes
exactly the odd-index signs, so T=UK fixes every gamma and T squared is I.
It follows termwise that T H T inverse=H, whereas every Hermitian bilinear
i gamma_a gamma_b (a<b) is T-odd. The unique ground ray is T-invariant.
Its expectation of each such bilinear is therefore zero: antiunitary
conjugation complex-conjugates the expectation, which is real for a
Hermitian observable, and the odd transformation negates it.

## Scope and provenance

The exact runner checks the complete 16-by-16 block formula, Clifford relations,
antiunitary action and all 28 bilinear expectations using integer complex
arithmetic. A coefficient-sign mutation is a failing control for the block
formula. These are finite algebra checks, not empirical measurements.

This extracts the finite calculation from PR #9571, commit
`6afb06951a13ca861b50f47a8faf5d5c06594109`, historical files
`.claude/science/exercises/strain-hot-matter-and-twins-20261013/agents/C5_TW3_report.md`
and `scripts/TW3/tw3_fk.py`, `scripts/TW3/tw3_lib.py` within that exercise.
The source branch remains a recovery handle for the larger unlanded work.
The argument above is self-contained; historical reports supply no proof authority.
The existing Spin10 symmetric atomic-gap construction is context with a
different carrier and Hamiltonian. No novelty or priority claim is made here.

This result supplies neither an interacting chiral lattice limit nor a mirror
sector realization, strain law, taste selection, gauge embedding, universal
Z8 classification or Spin(7) identification. Those questions remain separate
research obligations. No audit grade is asserted.

## No-Go Discipline Gate — packet HOLD

N1 — Alternative routes: ATTEMPTED exact complete matrix reduction and antiunitary transformation; independent Kronecker reconstruction provides a control, not five distinct attack families.
Fewer than five distinct routes have been established. Current no-go-discipline
schema therefore withholds packet PASS. This is a procedural limitation,
not evidence against the displayed finite theorem. This candidate has not landed.

N2 — Wall independence: no list of independent physical walls is asserted.
The supplied mathematical hypotheses define the theorem's domain; no wall
count or pairwise non-implication claim is made.

N3 — Hidden conditions: the complete proof was reread. The four-qubit carrier, Pauli convention, all coefficient signs, positive W and the explicit antiunitary are supplied. No framework distribution or dynamics is imported.
Historical provenance and comparisons are non-load-bearing context.

N4 — Residual matching: no prior no-go or campaign is cited as proof authority.
Historical paths identify origin only; the current argument is self-contained.
The contextual Spin10 atom is a different Hamiltonian and supplies no premise for this spectrum.

N5 — Rhetoric: the runner checks exact matrix entries and the finite module
or cluster stated above. Its five resolution lines state executed scope and
nonexecution explicitly. No site-independent or lattice-wide physical
exclusion is asserted.

N6 — Partial closure: Changing the Hamiltonian, the symmetry, or W can change the conclusion; W=0 and W<0 are addressed explicitly.
No approved primitive is called a missing premise, and no new axiom is required
for these finite mathematical statements.

N7 — Steelman: An opponent can change a quartic sign or choose a symmetry-breaking Hamiltonian and invalidate the block formula. The runner detects the sign mutation. To refute the stated theorem, the opponent must find a wrong entry or bilinear transformation in the exact supplied matrix, not a different model.
The direct proof, rather than failure to imagine another route, supports the
mathematics. This does not waive the N1 packet shortfall.

N8 — Cross-cycle echo: the independent check compared the existing Spin10 symmetric atomic-gap note and historical TW3 cluster proposal; symmetric finite gaps are allowed and no global physical obstruction is inferred.
This focused comparison is not an exhaustive campaign-ledger search. Packet
coverage remains incomplete; no overall review-loop PASS is claimed.
