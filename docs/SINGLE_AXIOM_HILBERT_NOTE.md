# Finite Tensor Factorization: Exact Factor Locality and Conditional Operational Consequences

**Date:** 2026-04-12 (original operational experiment); 2026-07-12
(exact theorem replacement).
**Type:** bounded_theorem
**Status:** exact support/boundary theorem. A supplied finite tensor
factorization determines its factor operator algebras and their
disjoint-factor commutativity. A supplied support Hamiltonian, Hermiticity,
and Born readout have the exact conditional consequences proved below. None
of those three physical selectors is relabeled as a Hilbert-space consequence.
**Audit-status authority:** independent audit lane only.
**Runner:** [`scripts/frontier_single_axiom_hilbert.py`](../scripts/frontier_single_axiom_hilbert.py)
**Selector boundary (context, not a positive dependency):**
`docs/FINITE_FACTORIZED_HILBERT_PHYSICAL_SELECTOR_NONUNIQUENESS_NO_GO_NOTE_2026-07-12.md`
**Framework comparison:**
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)

## Question

What follows exactly from a finite tensor factorization, and what follows only
after graph, dynamics, and readout data are supplied?

Let

\[
 B=\left(I,\{\mathcal H_i\}_{i\in I},
 J:\bigotimes_{i\in I}\mathcal H_i
 \overset{\mathrm{unitary}}{\longrightarrow}\mathcal H\right),
 \qquad 2\le |I|<\infty,\quad
 2\le\dim_{\mathbb C}\mathcal H_i<\infty .
\]

The answer has a clean boundary. Factor-algebra locality is intrinsic to `B`.
Graph adjacency, a physical time evolution, and probability readout require
additional objects. Once those objects are explicit, several useful
consequences are exact rather than numerical demonstrations.

## Theorem 1: exact factor-algebra locality

For every factor define its embedded full operator algebra

\[
 \mathcal A_i=
 J\left(\mathcal B(\mathcal H_i)\otimes
 1_{I\setminus\{i\}}\right)J^{-1}.
\]

If `i != j`, then

\[
 [\mathcal A_i,\mathcal A_j]=0.
\]

Indeed, for `A in A_i` and `C in A_j`,

\[
 (A_i\otimes 1)(1\otimes C_j)=A_i\otimes C_j
 =(1\otimes C_j)(A_i\otimes 1).
\]

This is exact algebraic factor locality. It does not define which factor pairs
are adjacent, select an interaction, or imply a finite propagation speed.

## Theorem 2: exact support recovery in a supplied two-factor class

Now supply a simple graph `G=(I,E)`. For each factor choose a nonzero traceless
Hermitian operator `X_i`, normalized by
`Tr(X_i^2)=dim(H_i)`, and supply nonzero real edge coefficients `c_ij`. Define

\[
 H_G=\sum_{\{i,j\}\in E}c_{ij}X_iX_j .
\]

Hilbert--Schmidt orthogonality gives

\[
 \frac{\operatorname{Tr}(X_iX_jH_G)}{\dim\mathcal H}=c_{ij}
 \quad\text{for }\{i,j\}\in E,
\]

and zero for nonedges. Thus `E` is recovered exactly from `H_G` inside this
supplied operator class.

The direction of implication matters:

\[
 (G,\{X_i\},\{c_{ij}\})\longrightarrow H_G
 \longrightarrow \operatorname{support}(H_G)=E.
\]

This is not a derivation of `G` or `H_G` from `B`. It is an exact recovery
theorem after the support data are supplied.

## Theorem 3: Hermiticity conditionally gives unitary evolution

For any supplied Hermitian operator `H=H^dagger` and any real `t`,

\[
 U_t=e^{-itH}
 \quad\Longrightarrow\quad
 U_t^\dagger U_t=e^{itH}e^{-itH}=1.
\]

Thus Hermiticity is sufficient for a unitary one-parameter group. This theorem
does not select `H`, identify the parameter with physical time, or derive the
premise that closed-system evolution is the group `U_t`.

## Theorem 4: Born readout conditionally gives zero third-order interference

Supply the Born readout. For three exclusive path amplitudes `a`, `b`, and
`c`, write

\[
 P(S)=\left|\sum_{k\in S}a_k\right|^2.
\]

Then the third-order inclusion--exclusion combination is

\[
\begin{aligned}
 I_3={}&|a+b+c|^2-|a+b|^2-|a+c|^2-|b+c|^2\\
      &+|a|^2+|b|^2+|c|^2=0.
\end{aligned}
\]

Every diagonal term appears with coefficient `1-2+1=0`, and every pairwise
cross term appears with coefficient `1-1=0`. The cancellation is exact for
arbitrary complex amplitudes. It is conditional on the supplied quadratic
readout; it does not derive physical probabilities from the inner product.

## Exact selector boundary

The separate leaf source
`docs/FINITE_FACTORIZED_HILBERT_PHYSICAL_SELECTOR_NONUNIQUENESS_NO_GO_NOTE_2026-07-12.md`
uses a fixed expansion signature and explicit same-base countermodels. It
shows that the bare factorized object plus type conditions do not uniquely
distinguish one physical graph, one CPTP dynamical semigroup, or one contextual
probability rule. The statement is deliberately narrower than “no formula can
be written from Hilbert data”: empty/complete graph rules, identity dynamics,
and the quadratic amplitude formula are all writable. What is absent is a
premise that identifies one such mathematical construction as the physical
one and excludes the alternatives.

Consequently this note makes two different kinds of statement:

- Theorems 1--4 are exact positive implications on their stated surfaces.
- Selector uniqueness is not claimed here; the separate no-go note carries
  that negative theorem and its N1-N8 discipline record.

## Relation to the current framework

The Lattice axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies
`Z^3` nearest-neighbor adjacency directly. The framework graph is therefore
Lattice premise content, not a consequence of factorization. Qubit supplies
the one-site algebraic presentation. Admissibility supplies a covariant
nearest-neighbor availability rule. Record supplies permanent records and
finite scalar additivity.

The same framework note explicitly leaves Hamiltonians, transition weights,
Born probabilities, measurement contexts, and physical persistence dynamics
outside the four axioms. This note does not enlarge or reduce that framework
surface.

## Replacement of the earlier numerical packet

The historical runner performed small fixed-seed experiments after choosing a
local Hamiltonian, Born readout, and support-to-edge convention. Those
experiments are replaced by the exact algebra above.

In particular, the former Test 4 compared a participation ratio made from six
overlapping, unnormalized qubit-occupation marginals with one made from a
normalized 64-outcome distribution. Because the sample spaces and
normalizations differ, that ratio is not a valid localization comparison. It
has been deleted. This note makes no numerical localization claim.

## Assumptions and imports

- Theorem 1 uses only the supplied finite tensor factorization.
- Theorem 2 explicitly supplies `G`, the operator family, and edge
  coefficients.
- Theorem 3 explicitly supplies a Hermitian `H` and the exponential evolution
  form.
- Theorem 4 explicitly supplies the Born quadratic readout.
- No observed value, fitted selector, literature value, unit convention, or
  empirical comparator enters any proof.
- Independent audit remains required before the audit pipeline assigns an
  effective status.

## Falsifiers

- Theorem 1 fails if two embedded disjoint-factor operators have a nonzero
  commutator.
- Theorem 2 fails if a normalized Pauli-word coefficient disagrees with the
  supplied edge coefficient in the displayed class.
- Theorem 3 fails if a Hermitian `H` yields `U_t^dagger U_t != 1`.
- Theorem 4 fails if direct expansion leaves a nonzero diagonal or pairwise
  coefficient in `I_3`.

The paired runner checks all four statements, the source boundary, and the
removal of the invalid localization comparison.

## Conclusion

Finite tensor factorization yields an exact and useful locality theorem:
operators on disjoint factors commute. Supplied graph support, Hermiticity,
and Born readout then give exact graph-recovery, unitarity, and `I_3=0`
consequences. Keeping the arrows in that order removes the earlier class-E
compression. The physical selectors are either separate framework premises
or separate derivation obligations; they are not hidden inside the word
“Hilbert.”
