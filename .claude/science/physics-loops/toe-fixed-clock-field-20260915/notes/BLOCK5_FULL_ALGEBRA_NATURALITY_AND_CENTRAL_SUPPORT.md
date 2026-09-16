# Full algebraic naturality and the support of a probability law

Personal conditional derivation, 2026-09-15. The chosen naturality group is
an explicit hypothesis, not a new interpretation adopted for the axioms.
These statements concern ordinary Borel probability measures on the algebra
M2(C), not density matrices, quantum instruments, or a selected physical law.

## 1. A finite invariant measure cannot follow an escaping polynomial orbit

Let T be a unipotent linear map on a finite-dimensional real vector space.
For every v outside Fix(T), T^n v is a vector-valued polynomial in n with
a nonzero positive-degree leading coefficient, so ||T^n v|| tends to infinity.
If a probability measure mu is invariant under T, then for every ball B_R,

    mu(B_R)=integral 1[B_R](T^n v) mu(dv).

Dominated convergence gives mu(B_R)=mu(B_R intersect Fix(T)). Increasing
R to infinity proves mu(Fix(T))=1. No moment, density or bounded-support
hypothesis was used. The norm is a temporary proof coordinate, not structure
added to the invariant measure or physical law.

Apply this to conjugation by U=I+E12 on M2(C), viewed as a real vector
space. For B=[[a,b],[c,d]],

    U^n B U^(-n)=[[a+nc, b+n(d-a)-n^2 c], [c,d-nc]].

The fixed subspace is c=0 and d=a. Conjugation by I+E21 similarly fixes
only b=0 and d=a. Therefore any probability measure invariant under both
of these conjugations, and hence any measure invariant under all inner
automorphisms of M2(C), is supported on the center C I. Conversely every
probability on that center is invariant under inner automorphisms.
For invariance under all real algebra automorphisms its scalar law must
also be invariant under complex conjugation.

In particular no such invariant probability has full topological support
on M2(C), or assigns positive probability to noncentral matrices. This
does not say there is no probability law on the full algebraic DOMAIN:
the intrinsic 0/I law and every conjugation-symmetric scalar law are
examples. Domain and support remain different notions.

The unipotent fixed-measure mechanism is established mathematics; the
related primary article *Generic subgroups of Lie groups*, section3, was
located by search. This proof specializes the mechanism directly to two
explicit matrices and imports no general homogeneous-space theorem.

## 2. A one-input equivariant kernel stays in the input-generated algebra

Suppose K(A,dB) obeys simultaneous inner-conjugation covariance. Fix A.
Then K(A,.) is invariant under every invertible matrix commuting with A.

If A has two distinct eigenvalues, use a conjugate coordinate in which it
is diagonal. Its stabilizer contains diag(2,1/2), whose action multiplies
B12 by4 and B21 by1/4. A finite probability invariant under multiplication
by4 on C is concentrated at zero: equal measures of the disjoint annuli
4^k<=|z|<4^(k+1) must all be zero. Applying this also to the inverse
scaling forces both off-diagonal entries to vanish. The remaining matrices
are exactly C[A].

If A is a nontrivial Jordan block, its stabilizer contains I+E12 after
conjugation and rescaling its nilpotent part. The preceding unipotent
argument forces B=[[b0,b1],[0,b0]], again exactly C[A]. If A is scalar,
its stabilizer is the full group, and section1 forces scalar B=C[A].
Thus, in every case,

    K(A, C[A])=1.                                     (1)

This is a support theorem for one input; it is not a classification of
all kernels or a claim about two noncommuting inputs. Similarity/Jordan
coordinates only prove a coordinate-independent conclusion.

## 3. Independent fibers and shared fibers are different hypotheses

If a forming site's algebra can be relabeled independently of ALL its
neighbour algebras, its relabeling fixes the input profile. An equivariant
kernel must then have an invariant output probability at every profile.
Section1 forces central support even when neighbour records are noncentral.
This is the independent-fiber naturality hypothesis.

If all site algebras have instead been identified with one common algebra
and only simultaneous relabeling is required, neighbour contents transform
with the output. Two noncommuting records can supply enough algebraic
structure for a noncentral law. The companion note gives a full-domain
kernel and a reachable example. Products of elements in different abstract
fibers are undefined until such a comparison/identification is supplied.
The existing lattice covariance clause alone does not choose between these
two internal action contracts.

Under the simultaneous action, an all-central input profile is still fixed
by every inner automorphism. Its output law is therefore central. Any
empty-start sequential construction with finite ancestor sets remains
central at every formed site, by induction through each finite ancestor
graph. This conclusion does not assume that every possible initial state
is empty or central; the companion compatible-seed example escapes it.

## 4. Concrete controls on overbroad readings

Replacing all inner automorphisms by unitary conjugations changes the
answer: independent circular complex Gaussian matrix entries define a
full-support probability invariant under unitary conjugation. Its density
uses a supplied Hermitian norm. Conjugating by diag(2,1/2) multiplies
the variance of its12 entry by16, so it fails the full-inner hypothesis.
Compact symmetry does not establish full algebraic naturality.

A law can be covariant while a selected initial state is not invariant.
The realized-state primitive does not supply a probability measure invariant
under every automorphism. It is therefore invalid to infer central physical
records merely from that primitive. Conversely calling a kernel covariant
does not authorize multiplying neighboring algebra elements without a
specified comparison of their fibers.

The approved kinetic-isotropy primitive is unchanged and is not verified
by these support statements. They neither give a complete model of the
foundation nor force an axiom update. See BLOCK5_SCOPE_AND_NO_GO_REVIEW.md
for the attempted routes and surviving constructive escapes.
