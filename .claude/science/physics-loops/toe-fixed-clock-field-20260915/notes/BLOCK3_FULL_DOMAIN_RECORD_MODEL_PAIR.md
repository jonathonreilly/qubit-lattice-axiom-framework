# Full-algebra record laws with different finished-record correlations

Personal proof candidate, 2026-09-15. This is a declared model pair,
not an axiom-update verdict. The compatibility check with the approved
kinetic-isotropy primitive remains open and must not be replaced by attaching
an unrelated quadratic form. No full-foundation witness is claimed yet.

## Exact target and declared interpretation

Here K is the content law conditional on formation and the already readable
neighbour records. A static Gibbs conditional given a completed neighbourhood
is a different object. The current axiom reading notes discuss the former,
but identify themselves as non-governing. This note states the interpretation
it uses and does not adopt it on behalf of the owner. The same condition
applies to interpreting algebra elements as the full possibility domain.


Use Z^3 and the full M2(C) algebra as the local possibility domain, with its
ordinary Borel structure. A record contains one element of that algebra;
blank sites have no readable content. The law below is defined on EVERY
partial nearest-neighbour record configuration with arbitrary M2(C) entries.
Its probability measure happens to be supported on the two intrinsically
defined algebra elements 0 and I. The domain is not replaced by a prepared
Bloch menu, and no star, norm, axis, basis or inter-site algebra identification
is required. Whether this literal full-domain/support distinction exhausts
the intended Qubit reading is an explicit semantic check, not an adopted
interpretation change.

For 0<p<1, define b(A)=1[A=I]. With m recorded nearest neighbours,

    K_p(I | eta) = (1-p)/2 + (p/m) sum_(y recorded) b(A_y), m>0,
    K_p(0 | eta) = 1-K_p(I | eta).

For m=0 give 0 and I probability 1/2 each. All other possibilities receive
zero probability. These are Borel probability kernels on the full algebra.
Both support points always have probability at least (1-p)/2>0. The rule
varies with neighbour content: changing one sole record from 0 to I changes
the I-probability by p. It is invariant under all slot permutations and
under arbitrary real algebra automorphisms independently in every site
fiber, since every such automorphism fixes 0 and I. Thus no spatial/internal
soldering or selected algebraic basis is used.

This is a supplied pair of mathematical laws, p=1/4 and p=3/4, whose possible
consistency with the claimed premises is to be proved. Neither p is selected
as the physical law. The construction is not claimed to recover known matter,
Born measurements, Maxwell fields, gravity, or any empirical observation.

## Global formation with exact local odds

Supply independent Exp(1) activation times T_x, uniform parent-selection marks,
Bernoulli(p) copy marks C_x, and fair independent bits Z_x at all lattice
sites. These are model ingredients, not deductions from the axioms or the
realized-state primitive. The rate and mark construction are identical in
both models apart from p. The law can be conditioned on any compatible
pre-existing 0/I record configuration; use the SAME empty initial condition
for the correlation comparison. That condition is supplied data, not a
preferred state selected by the foundation.

At its activation, a blank site looks only at already recorded neighbours.
If none exist, set its bit Y_x=Z_x. Otherwise choose one of those neighbours
uniformly, call it a(x), and set Y_x=Y_(a(x)) when C_x=1 and Y_x=Z_x
when C_x=0. Lock A_x=Y_x I permanently. The resulting conditional law at
formation is exactly K_p. Both output values stay in support after every
later append, so this construction satisfies formation-time and ongoing
support simultaneously. It never reads an unrecorded possibility.

Every decreasing activation-time path of length n is self-avoiding. From
a fixed site there are at most 6*5^(n-1) candidates, each decreasing with
probability 1/(n+1)!. Hence its ancestor graph has finite depth almost surely;
local finiteness then makes it finite. Countability gives this at every site.
Evaluation on those finite ancestor graphs defines a consistent unique global
process for the supplied marks, with shared ancestors using shared marks.
Every site forms at a finite time and remains immutable thereafter. No first
global event or increasing enumeration of Z^3 is required. A cylinder
function has the local pure-birth generator

    L_p f = sum_(x blank) sum_(s=0,I) K_p(s|eta_x)
                                [f(rho with x=s)-f(rho)].

This is the existing decreasing-priority construction applied to a different,
full-algebra-defined kernel. The probabilistic method is prior art; the
full-domain kernel and a finished-record statistical discriminator are the
new targets here.

## Exact infinite-lattice discriminator in the declared process

Fix the activation times and all parent-selection marks, disregarding copy
and innovation bits. Each site has a finite decreasing parent chain ending
at a local minimum. For distinct x,y, their chains either never meet or have
a first common vertex. In the latter case let L be the sum of the two chain
lengths to that first meeting; L>=1. Those paths are disjoint before meeting.
The actual noise-stopped ancestry coalesces exactly when every one of these
L pre-meeting vertices copies. Its conditional probability is p^L. Therefore

    E Y_x=1/2,
    Cov(Y_x,Y_y)=(1/4) E_parent[1[chains meet] p^L].

A covariance between independent fair innovation bits is zero; coalescence
uses one common bit and gives variance 1/4. This proves the formula rather
than inferring it from a finite correlation simulation.

For nearest neighbours, L=1 exactly when one chooses the other as parent.
At a degree-six site, the probability of having any earlier neighbour is
6/7 by iid rank symmetry on the seven-site star. Uniform earlier-neighbour
selection and symmetry among the six neighbours give probability 1/7 for
each particular parent. The two opposite directed-parent events cannot both
occur. Thus P(L=1)=2/7 exactly.

All powers p^L increase with p. Between p=1/4 and p=3/4 this gives

    Cov_(3/4)(Y_x,Y_y)-Cov_(1/4)(Y_x,Y_y) >= 1/28,
    P_(3/4)(Y_x=Y_y)-P_(1/4)(Y_x=Y_y) >= 1/14.

The comparison uses only the final contents of two neighbouring records,
not a readable clock, order, unrecorded state, or auxiliary mark. Both models
have the same one-site fair marginal. These are law-level conditional
statistics at a shared supplied initial condition; a realized bit or measured
frequency is still state data.

## Discharged checks and remaining foundation obligations

* Full Qubit domain versus constant proper support: the current axiom does
  not say full-support or noncentral records, but the intended algebraic
  presentation and 'no possibility privileged' language must be matched.
* Global formation and Markov odds: discharged for the declared process.
  Before its activation a site's copy/innovation/parent marks have not been
  used anywhere. Conditioning on its not having activated constrains only
  its clock. Exponential memorylessness gives the displayed unit-rate
  generator, while its unused marks give exactly the displayed kernel.
* Support and Record: discharged for the declared process by the positive
  two-point support at every profile, the finite-ancestor construction, and
  the one-time append rule. The final discriminator reads only content.
* Covariance: discharged for the declared actions. The iid marks and uniform
  earlier-neighbour rule are covariant under the entire lattice symmetry
  group. Every algebra automorphism fixes 0,I and preserves the equality
  test b, independently in each fiber. These are general proofs; the finite
  matrix probes are controls only.
* Primitive compatibility: scale conversion and pointwise realized-history
  reference can be shared. The matter kinetic-form equality c_t=c_s is
  approved content, not a missing framework premise. This candidate has not
  yet supplied a matching matter/evolution interpretation that verifies it.
  Setting two unrelated formal coefficients equal would not complete that
  obligation. Do not claim all approved primitives from their failure to
  mention p.
* A mathematical model pair cannot select a preferred physical completion,
  prove no completion exists, or force a unique new axiom clause. Any negative
  consequence requires the committed N1-N8 packet and exact premise scope.


## Reachable support and finite checks

For any finite set F and prescribed 0/I pattern, the event that each site
in F has C_x=0 and the prescribed innovation bit forces that final pattern,
independently of its ancestors. Its probability is [(1-p)/2]^|F|>0. Thus
both terminal laws have the SAME full topological support {0,I}^Z3. The
correlation difference is a difference of probability laws on that support,
not merely a difference between their allowed finite record patterns.
The law is defined for arbitrary compatible initial records and treats
them without redrawing; the empty initial condition used in the comparison
is supplied equally to both models.

The exact runner checks 56 neighbour-count probabilities, 40 algebra
automorphism probes, and finite edge/path/square joint laws by direct
order products against a separate parent-chain expansion. The general
automorphism statement is the algebraic proof that every automorphism
fixes 0 and I; the finite matrices only challenge the implementation. A
basis-coordinate substitute fails under exact conjugation.

On the finite square, the adjacent first-meeting coefficients are a_1=2/3
and a_3=1/6; on the path3, the endpoint coefficient is a_2=2/3. These are
finite blank-exterior examples, not infinite-lattice marginals. The seven
site star calculation gives the exact infinite-lattice directed-parent
probability 1/7 because this choice depends only on those seven iid clocks.
The infinite existence and coalescence arguments are analytic. No simulation
or assertion count replaces them, and there is no independent review.

## No-Go Discipline Gate

See the committed companion BLOCK3_NO_GO_DISCIPLINE_CHECKLIST.md. The
intended all-foundation nonselection claim is not complete: primitive
compatibility and interpretation scope remain explicit. The positive
mathematical construction and its exact discriminator are preserved within
the declared process class. No new axiom, no selected clause, and no
framework-wide impossibility claim is shipped.
