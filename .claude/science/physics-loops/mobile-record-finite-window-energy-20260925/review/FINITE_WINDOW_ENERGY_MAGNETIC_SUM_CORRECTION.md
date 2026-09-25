# General-graph magnetic summation correction

The released independent comparison identified a missing restriction in Section 1
of the sealed root note FINITE_WINDOW_MICROSCOPIC_ENERGY_MEASURES_ROOT.md,
SHA256 a72af425e970c080502a394902adf86437d767e90921b30f6e6c889c99ccb902.
The printed expression for H4 sums over a<c without restricting the stars.
For the supplied general graph the correct parent expression is

    H4 = -2 sum_(a<c, distance(a,c)=2) (F_c F_a P)*(F_c F_a P).

Only distinct A stars sharing a B neighbour are included. Contributions from
distant stars cancel in the parent's canonical fourth-order expression.
The public synthesis must include this restriction. This corrects the displayed
identification of the target Hamiltonian; it does not change the subsequent
spectral and conditional-state arguments, which use the correct parent H4,
its uniform boundedness and strong convergence. The generic four-state
bounded-compensation example is unaffected and remains labelled as such.

The original author note, programs, results and seal remain unchanged. This
correction was made after author disclosure and is not part of the blind PRE.
The stopped-instrument proof and disconnected physical twelve-dimensional
counterexample in the independent PRE retain their separate provenance.
