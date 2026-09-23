# General bounded compensation target: post-PRE comparison

2026-09-23. This comparison concerns only the general bounded perturbation
lemma. The specific local compensation construction remains unread.

**Mathematical disposition:** the canonical coefficients, leading formation
operators, and fixed-graph compact-time O(epsilon) density estimate agree
with the independent reconstruction. One narrow prose correction, F1 below,
is needed. It changes no equation or theorem hypothesis.

## 1. Authorized sources and preserved independence

The exact authorized author seal is

```
local_compensation_author/GENERAL_TARGET_AUTHOR_SEAL.json
630f063e8fd546c844dba720943198070c49573d9de1c3870531ec40791e373f
```

Its sole new bound scientific note is

```
BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET.md
9bc691a07fd70c1a813852aa0cac55832065b3c95cf3d50e5528845f6613e0b0
```

The one other bound source is the already checked parent target note,
SHA `002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e`.
Both author bindings and the author seal authenticate by complete byte count
and SHA-256. I read the entire new note. Its seal truthfully describes an
analytic argument and does not claim numerical author controls; none were
searched for or opened.

The independent PRE remains
`0504a3fc90cca1b0f9b7bab3a1aa346b11e0889bc25abf55bd65966965375a46`.
Its one source and eighteen artifact rows reauthenticate unchanged. The
initial report and independently written finite-block/density controls
remain the evidence preceding author-source access. They were not rewritten
to agree with the author.

No other `local_compensation_author` file, local counterterm proposal,
cube-unprepared packet, other new source, plan, checkpoint, registry, Git,
publication or audit surface was accessed. The comparison does not confer
formal audit or retained status.

## 2. Required narrow correction F1

At line 97 of the frozen note, the sentence

> All displayed operators are self-adjoint.

is overbroad. The immediately preceding graph-coordinate coefficient is

```
G4 = M^2 - M C0 + A† C1 A - Z†Z/2.
```

It is generally not self-adjoint when C0 and M do not commute. The leading
formation operators B_j in Equation (2) are also generally not self-adjoint.
The intended and correct statement is:

> Both Hamiltonian coefficients H2^C and H4^C are self-adjoint.

The exact frozen independent control supplies a concrete counterexample to
the original blanket wording: the squared Frobenius norm of `G4-G4†` is 202.
For its two nonzero formation channels, the squared norms of `B_j-B_j†` are
46 and 29/2. The canonical Hamiltonian coefficients themselves are exactly
self-adjoint. The new `comparison_check.py` verifies these rational identities
and the equality of both author Hamiltonian coefficients to the PRE values.

This is a sentence-scope repair, not a failure of the graph-coordinate
method. The author's derivation already identifies the graph matrix as
nonorthonormal and correctly supplies the similarity transformation that
produces the Hermitian canonical coefficient. No equation needs alteration.
F1 remains open against the frozen source identity until a separately bound
correction is provided.

## 3. Complete coefficient comparison

The hypotheses match: finitely many nonnegative integer W grades at fixed
graph; bounded self-adjoint T with only adjacent-grade blocks; bounded
self-adjoint C commuting with W, uniformly in S; and the parent's bounded
formation channels obeying `jP=0` and `[W,j]=-j`. Number and physical-sector
preservation are stated for the record interpretation. No extra assumption
that C0 commutes with M, or that C commutes with the jumps, has been inserted.

The author's full-cluster Riesz/polar construction is the same positive-
overlap convention fixed in the PRE derivation. It rotates all W clusters,
not just P versus its complement. Xi parity survives because C preserves
W. Consequently the full rotated Hamiltonian differs from
`delta epsilon^-4 W` by O(epsilon^-2), and its canonical P-block truncation
through fourth order has scaled remainder O(epsilon^2). The distinction
between this global bound and merely block-diagonalizing P is correctly
retained.

The graph invariance equation and its epsilon-cubed equation have the
correct signs and multiplication order. Specifically the raw fourth
coefficient is

```
M^2 - M C0 + A† C1 A - Z†Z/2.
```

The canonical normalization adds `[M,C0]/2`, yielding

```
H2^C = C0-M,
H4^C = M^2 -(M C0+C0 M)/2 +A† C1 A -Z†Z/2.
```

This agrees exactly with the independently derived formula, including the
noncommuting C0 case and the nonzero excited C1 contribution. Higher-grade
C blocks do not enter at this order. The first rotation derivative remains
`U'(0)P=-A`, so the supplied instrument's leading jump is still
`B_j=-PjPi1TP`. The formation statement does not equate distinct supplied
instruments or claim an unchanged later waiting law.

The comparison evaluates the author's literal Equation (2) on the frozen
independent nine-state model, using only the independent builder. Every
Hamiltonian and jump matrix equals its stored exact PRE matrix. This check
supplements the proof comparison; it is not an author-run reproduction or
a replacement for the operator derivation.

## 4. Density estimate and uniformity

The large off-block loss source is correctly retained. The author gives

```
Off R_epsilon = O(epsilon^-1),
Diag R_epsilon = O(epsilon).
```

The independent PRE proves the stronger diagonal estimate O(epsilon^2)
using jump parity. The author's weaker bound is sufficient and is not a
mathematical discrepancy.

The inverse of `A0=-i delta[W,.]` is bounded on P-Q off-block matrices because
nonzero W grades are at least one away from zero. Therefore the correction
`-epsilon^4 A0^-1 Off R_epsilon` has norm O(epsilon^3). The exact residual
identity in the author note agrees with the PRE identity. Both remaining
generator norms are O(epsilon^-2), including the entire transformed
dissipator, so the corrected residual is O(epsilon) in induced trace norm.

The Duhamel step is valid on Hermitian trace-class inputs. The correction
need not be positive: the physical full and target CPTP semigroups supply
the necessary contractivity. The input/output unitary changes are O(epsilon)
uniformly over all P-supported densities, including permitted coherences
between number sectors. There is no discarded no-event loss, excited-block
population inverse, or assumed rapid mixing of the fast target.

The constants depend on the finite grade range, fixed graph and uniform
T,C,j bounds, delta, kappa and the compact time interval. Hence they can be
independent of S under the stated hypotheses. The bounded-rotor version is
also justified on trace class; an unbounded electric-square C would require
a different argument. The author explicitly does not infer a resource-
independent target limit, correctly avoiding amplification of coefficient
errors by the fast `epsilon^-2 H2^C` term.

The finite event/count-register extension reuses the parent's finite,
no-overflow observation setup, with C trivial on the register and number
conserving as stated. It does not establish arbitrary continuously
conditioned quantum-history equivalence. No further conclusion about a
specific local compensation or microscopic selection is checked here.

Apart from F1's sentence scope, no missing hypothesis or equation correction
was found in this general bounded theorem.

## 5. New evidence and verification limits

The new exact comparison and authentication run is preserved as

```
comparison_check.py
COMPARISON_RESULTS.json
COMPARISON.stdout
COMPARISON.stderr
COMPARISON_RECEIPT.json
```

Result/stdout SHA:
`6ecdb37da2949d8e4b08b596c6c60d490fab69eeec2eb2dcd36981252f479275`.
The run exited zero with empty stderr. Its command, times, exit code and
source/builder/stream hashes are recorded in the actual receipt. It reuses
only the frozen independent builder, reconstructs the coefficient identities
and F1 countercontrol exactly, and authenticates the PRE and authorized
source seal. There was no new failed execution.

The unchanged PRE full-density propagation was not rerun merely to increase
control counts. Its exact coefficient controls and floating density/residual
checks retain their stated limitations. No author numerical evidence is
claimed for this narrowly authorized analytic packet.

`FINAL_SEAL.json` binds the author note at the original reviewed hash, the
original PRE, all original evidence and the new comparison. A later F1
correction should be acknowledged separately without rewriting these files.
