# The exact residual module after all protected mixed rows

This is a separate analytical consequence of MIXED_TRANSPORT_FOREST.md, for L divisible by four and L>=12. It identifies every remaining condition; it does not prove that its residual observation matrix has full rank. The original actual H2, physical Gauss phases, full matter configuration space, G and mark conventions are unchanged.

## 1. Isometric elimination of all mixed rows

Work in one finite physical Gauss phase fiber, at fixed W=1 and odd B count k. Let P be the protected-union matter projector and let X select all actual output rows that receive both polarities from P. The complete row classification puts these rows outside P. The forest theorem explicitly solves

    X H P psi=0.

For each tree C of size m_C choose its unit Laurent transport z_x from that theorem. Define one column

    R_C = m_C^(-1/2) sum_(x in C) z_x |x>                 (1)

in the FULL W=1 fiber. Isolated vertices give their own columns. The trees partition P, so R*R=I and RR*<=P at every physical phase. The columns are Laurent-polynomial vectors with constant normalization factors. Moreover

    Ran R = {psi in Ran P: X H psi=0}.                   (2)

No physical output has been discarded in (2): X consists of all cross-sign rows, and the tree elimination uses their complete two-term coefficients. Each column has at most (L/4)^3 matter configurations. Its fields are the exact transported words, not independently rephased configuration edges.

## 2. The remaining spectral equations

Let d be the number of trees and put

    A(theta)=R* H R,
    B(theta)=(I-RR*) H R.                                (3)

Both are finite Laurent matrices (the adjoint on the physical torus is the Laurent involution). A is Hermitian on the physical phase torus. Its entries use the actual full source H; B includes all remaining one-polarity outgoing rows AND the component orthogonal to R within P. Already-solved mixed rows obey X B=0 exactly.

An actual H eigenvector psi wholly in P is equivalent to a nonzero z such that

    psi=R z,       A z=lambda z,       B z=0.              (4)

Necessity uses (2); sufficiency follows by splitting H R into R A+B. In particular, merely solving the remaining exterior rows is not enough: B also imposes that the protected-row image has the SAME transported amplitude ratios along each tree.

Define the complete reduced observation matrix

    O_red(theta) = [ B; B A; ...; B A^(d-1) ].            (5)

At a fixed physical phase, no protected-union eigenvector exists if and only if (5) has full column rank. Indeed an eigenvector from (4) lies in its kernel. Conversely, the kernel of (5) is A-invariant by Cayley-Hamilton; since A is finite dimensional and Hermitian there, a nonzero kernel contains an eigenvector satisfying (4). This is a strictly explicit reduced criterion, not a claim that it is satisfied. If P is empty the exclusion is vacuous and no nonempty matrix is needed.

Every entry of (5) is an actual Laurent polynomial. Thus either a maximal minor is a nonzero Laurent polynomial, yielding exclusion at almost every physical phase, or all such minors vanish identically and the protected-union obstruction survives generically. Producing the nonzero minor or the surviving invariant submodule remains the unproved step. A sample rank is not a proof of either alternative unless its exact entries and arithmetic establish a genuine nonzero minor.

## 3. Additional exact structure of the reduced kinetic matrix

On a protected input the complete canceled H column has diagonal 6 and all nontrivial hole outputs at distance two. A protected output from such an input has the SAME polarity: one shared B retains the input sign, so it cannot have a uniform opposite star. At fixed sign the completed A background and literal B pattern are preserved, exactly as in PROTECTED_POLARITY_PROOF.md. Consequently P H P consists of the already derived principal geometric blocks of K_(sigma theta)* K_(sigma theta).

Distinct vertices of the SAME mixed tree have holes in the same coordinate class modulo four; their distance on the original torus is at least four. They therefore have no off-diagonal P H P matrix element. The forest theorem also prevents two vertices of that tree at the same hole. It follows that

    A_CC = 6                                             (6)

for EVERY tree, including an isolated vertex, at all physical phases. In fact different trees with the same hole-coordinate class have no off-diagonal coupling either. Nontrivial A_CC' couples different coordinate classes and is the normalized finite sum of the genuine same-polarity two-hop coefficients weighted by z_x* z_y.

Equation (6) does not mean A=6I. Different coordinate classes are coupled by the original distance-two motion. Nor does it remove the B condition in (4). The FULL geometric matrices at opposite signs are conjugate and have equal spectra; their different protected principal compressions need not have equal spectra. Full geometric spectral simplicity alone cannot split an actual mixed vector.

## 4. Failed shortcuts and exact remaining strength

The first proposed mechanism was phase inconsistency around a mixed relation cycle. The complete forest theorem shows why it cannot work on this torus class: all cycles are exact reversals and their transport is one. This is a failure of that mechanism, not a dark eigenvector construction.

A leaf of a mixed tree need not have an H output with a single predecessor. Rows outside X can receive several same-polarity protected columns from different trees. Those rows also couple different coordinate classes. Deleting one leaf amplitude without solving those rows is unjustified. The quotient (3) keeps them all.

The formerly checked one-polarity theorem supplies no missing step here. R columns can mix signs and completed A backgrounds, so (4) does not separate into the single-background full T eigen-equations used there. The same physical phase variables occur in R, A and B; treating their monomials as independently adjustable edge parameters would change the law.

The remaining precise smaller problem is therefore the actual maximal-minor/invariant-submodule alternative for (5). This is target-equivalent to protected-union eigenvector exclusion at the stated finite volume, with every cross-sign row already eliminated analytically and with d variables in place of dim P. It is not equivalent to full dark-module exclusion: unprotected columns are still absent from this target. No actual source-history image density, positive-Haar source overlap, phase-uniform rate, finite-spin transfer or continuously forced residence estimate follows.
