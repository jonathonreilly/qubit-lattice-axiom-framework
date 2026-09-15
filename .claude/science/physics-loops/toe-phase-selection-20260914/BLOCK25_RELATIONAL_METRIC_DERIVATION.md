# Block25: relational Gaussian kernels and permanent formation laws

Date: 2026-09-15. Status: private derivation proposal, not independently reviewed.
No axiom or primitive update; no physical law selection or TOE closure.
Current-main premise revision: 5deabeb698a27c2c3f68c5df685af2521ef15307.
Prior campaign milestone PR8136 is independent of this block.

## Target and opportunity

The current minimal axioms supply the full local M2(C) possibility domain and
a nearest-neighbor conditional probability law, without selecting its form.
Existing Gaussian compiler notes use a supplied Hermitian structure and prove
simultaneous unitary covariance. The new question is whether the actual
neighbor contents can supply an inner product covariantly under arbitrary
complex algebra automorphisms, rather than importing one fixed inner product.

The precise target is a full-domain, local, translation/permutation-covariant
probability kernel on matrix contents, with full support on the open subset
of irreducible neighbor conditions. The inner product construction must be
unique on that subset for its declared functional. Selection of that
functional, Gaussian profile and variance remains supplied candidate-law data.

No claim is made that the axioms impose internal PGL2 covariance: the explicit
axiom symmetry clause names translations and proper cubic rotations. We test
the stronger algebra-covariant class as a concrete candidate. We also do not
assume a selected star, initial empty state, formation clock, or preparation.
The older May20 hardening and May27 Pauli-generator notes use selected
Hilbert/Clifford presentations; they do not by themselves settle the meaning
of every added structure under the current June29 memo and its later updates.

The general mathematical mechanism is standard Kempf--Ness orbit balancing.
The following two-dimensional proof is direct. Its value, if sound, is the
explicit nearest-neighbor probability construction and exact scope, not a
claim of new invariant theory.

## 1. Matrix tuple and functional

Let eta=(A1,...,Am), 0<=m<=6, be the recorded nearest-neighbor matrices in a
common supplied algebra presentation. Blank neighbors contribute no matrix.
The common presentation identifies the six neighbor algebras with the output
algebra; this is a candidate-law interface and is not a derived connection.
The tuple is irreducible if there is no common complex invariant line in C2.
Equivalently its unital generated complex algebra is M2(C), but this equivalence
is not needed in the existence proof below.

For a positive definite Hermitian matrix H of determinant one, put

    A^{*H}=H^{-1} A^dagger H,
    ||A||_H^2=Tr(A^{*H} A),
    F_eta(H)=sum_i ||Ai||_H^2.

The coordinate dagger here presents the variable Hermitian form. It is not
held fixed as a physical metric: H ranges over every positive Hermitian form
up to scalar. Under a change of basis S the form becomes S^{-dagger} H S^{-1};
the norm and trace are invariant. Determinant one only chooses a representative
of the positive scalar class and has no effect on *H.

## 2. Existence and uniqueness on irreducible tuples

Write H=U diag(exp(t),exp(-t)) U^dagger, t>=0, and Bi=U^dagger Ai U. Then

    F_eta(H)=sum_i (|Bi11|^2+|Bi22|^2
                         +exp(2t)|Bi12|^2+exp(-2t)|Bi21|^2).

For every unitary U, sum_i|Bi12|^2>0: otherwise the second coordinate line is
invariant for all Bi, contradicting irreducibility. This continuous function
on compact U(2) has a strictly positive minimum c_eta. Therefore
F_eta(H)>=c_eta exp(2t), which is coercive on determinant-one positive forms.
Continuity and compact sublevel sets give a minimizer.

To compare two forms, take an invertible g with H0=g^dagger g and a traceless
Hermitian X such that H1=g^dagger exp(2X)g. Along the connecting geodesic
H(s)=g^dagger exp(2sX)g, diagonalize X with real eigenvalues x1,x2. In that
basis let Ci=g Ai g^{-1}, with the diagonalizing unitary included in g. Then

    F_eta(H(s))=sum_i,a,b |Ciab|^2 exp(2s(xa-xb)),
    d2/ds2 F_eta(H(s))=4 sum_i,a,b (xa-xb)^2 |Ciab|^2 exp(2s(xa-xb)).

If X is nonzero, its two eigenvalues differ. Irreducibility ensures a nonzero
off-diagonal coefficient, so this second derivative is strictly positive.
Two distinct minimizers are impossible. Denote the unique form H_eta.
The same expression gives a positive Hessian in each nonzero tangent direction.
Local implicit inversion of the stationarity equation therefore makes H_eta
real analytic on the irreducible open set. Local coercivity also prevents an
unrelated minimizing branch from escaping while eta stays near an irreducible
tuple. This is a local statement, not a uniform bound near reducibility.

The first variation at H=g^dagger g is

    d/ds F_eta(g^dagger exp(2sX)g)|0
      =2 Tr[X sum_i(Ci Ci^dagger-Ci^dagger Ci)].

Thus the balanced tuple satisfies sum_i[Ci,Ci^dagger]=0. In original coordinates,

    sum_i[Ai,Ai^{*H_eta}]=0.

The commutator sum is traceless, so restricting X to traceless matrices loses
no stationarity condition.

## 3. Exact covariance and its limits

For any S in GL2(C), define S eta S^{-1} componentwise. Uniqueness and the
change-of-basis identity give

    H_{S eta S^{-1}}=|det S| S^{-dagger} H_eta S^{-1},
    (S A S^{-1})^{*H_{S eta S^{-1}}}=S A^{*H_eta} S^{-1}.

Permuting the neighbors does not change F or H. Adding arbitrary central
matrices ci I to the tuple changes F by an H-independent constant, hence does
not change H. Multiplying every matrix by the same nonzero complex scalar
also leaves H unchanged. These statements are stronger than proper-cubic
permutation covariance; no internal axis was selected by the construction.

Reducibility matters. A simultaneous diagonal tuple has a whole family of
minimizing diagonal H. A nonzero nilpotent tuple (E12,0,...,0) has infimum zero
but no positive minimizer. It is incorrect to assign an arbitrary minimizer
and call that assignment algebra-covariant. No globally defined positive form
can be selected equivariantly at a tuple of central matrices: its stabilizer
contains diag(r,r^{-1}), which cannot preserve any positive form up to scalar
for all r>0.

## 4. Candidate probability kernel

For all six-neighbor conditions define the algebraic mean

    C_eta=(sum of recorded neighbor matrices)/6.

Division by six is fixed even with blanks; zero contributions here are an
algebraic convention in a conditional law, not a readable blank Record value.
Choose a supplied sigma>0. On an irreducible tuple set

    K_eta(dA)=pi^{-4} sigma^{-8}
               exp(-||A-C_eta||_{H_eta}^2/sigma^2) d^8 A.

The change of variables Z=g(A-C_eta)g^{-1}, g^dagger g=H_eta, has complex
determinant one and hence real Jacobian one: Ad_g on M2 has determinant
(det g)^2(det g^{-1})^2=1. The four complex Gaussian integrals normalize the
law exactly. Its support is all M2(C), and all moments are finite at each
irreducible condition. The coordinate volume is invariant under similarities;
its overall normalization cancels in the probability law.

On a reducible tuple use the explicitly declared fallback

    K_eta=delta_{C_eta}.

Irreducibility is an open Borel condition, the minimizer is continuous on that
set, and the fallback is continuous as a function of eta within its own piece.
This gives one Borel kernel on the entire neighbor domain, including blanks.
It is covariant under simultaneous arbitrary complex similarities and every
neighbor permutation, and therefore under lattice translations and proper
cubic rotations acting by neighbor permutation in the common presentation.

This is a construction of a law, not its selection. At central conditions it
is deterministic and central; at irreducible conditions it has full support.
No claim of global continuity at the reducible boundary is made.

## 5. Preliminary inference boundary

A candidate-law functional can make a local inner product depend on relational
Record content. This is a concrete escape from the claim that every compatible
Gaussian law must supply a fixed external Hilbert metric. It does not derive a
physical star from the axioms alone or identify the Gaussian law as Nature's.
A common comparison of neighboring algebra elements is still a supplied
interface. Initial conditions, formation process, readout identification,
Born selection, matter, gauge phase and gravity remain separate obligations.

The later sections execute the nonunitary covariance, two-matrix solution,
reducible degeneration, regular total kernel and supplied formation-process
checks, with their metric and causal inputs kept explicit.

## 6. Stronger total construction: Gaussian random words

The metric is not needed merely to obtain an algebra-covariant probability
law. A simpler construction also repairs the degeneration of the balanced
Gaussian family. Pad the recorded tuple to the six directed neighbor slots by
setting blank inputs to algebraic zero, retaining that this is a law convention.
For every ordered word w in the six indices of length at most three let
W_w(eta) be its matrix product, including W_empty=I. Fix strictly positive
candidate-law coefficients c0,c1,c2,c3 and independent standard circular complex
Gaussian scalars z_w. There are 1+6+36+216=259 such scalar marks. Define

    Y_eta=C_eta+sum_{|w|<=3} c_|w| z_w W_w(eta).

This finite polynomial random map defines a normalized law at every tuple.
It transforms by simultaneous similarity because every word does. Neighbor
permutations only permute the identically distributed scalar marks within
each length. No matrix norm, chosen fiber star, matrix eigenbasis, menu,
program decoder or metric minimization is used to define this law.

The topological support is exactly C_eta+V3(eta), where Vl is the complex span
of words of length at most l. Every finite-dimensional linear image of a
nondegenerate circular Gaussian has its image subspace as support. C_eta is
itself in V3, so the support is V3.

For a two-dimensional representation, V3 is the whole generated unital
algebra. Indeed V0 has dimension one; if a successive inclusion Vl in Vl+1
is equality, multiplication on the left by any generator preserves Vl, and
all later word spaces are equal. If no equality has occurred by l=2, the
three strict dimension increases give dim V3>=4, which is already M2.

A direct proof that a proper unital subalgebra B of M2 preserves a line is as
follows. If B has a matrix with two distinct eigenvalues, its two spectral
idempotents lie in B. In that basis, irreducibility requires an element with
nonzero 12 entry and an element with nonzero 21 entry. Sandwiching with the
idempotents then produces E12 and E21, hence all of M2. Otherwise every
noncentral element, after subtracting its scalar eigenvalue, is nilpotent.
Choose a nonzero such element and conjugate/scale it to E12. If every element
has 21 entry zero there is a common invariant line. If A21 is nonzero, then
E12 A has eigenvalues A21 and zero, which are distinct; the preceding case
applies. Thus irreducibility is equivalent to V3=M2.

Consequently the random-word kernel has full support on M2 at every
irreducible condition, and its support on a reducible condition is precisely
the proper algebra generated by those neighbors. It varies weakly continuously
on the full domain: couple the same finite scalar marks for a convergent
sequence of tuples, obtain pointwise polynomial convergence, and apply
bounded dominated convergence to each bounded continuous output test.
All moments are finite at each condition and locally bounded on compact sets
of input tuples. This is stronger regularity than the piecewise balancing
kernel, without a fixed external Hilbert metric.

The supplied common-algebra interface, four coefficients, complex Gaussian
profile and mean remain law choices. The construction is not a uniqueness
statement and does not select Born weights or a physical readout.

## 7. Exact degeneration and noncompact symmetry controls

For eta=(a E12,b E21,0,0,0,0), a,b nonzero, the balanced minimizer is

    H=diag(sqrt(|b|/|a|),sqrt(|a|/|b|)).

Its unit-variance Gaussian has entry variance Var(Y12)=|a|/|b|. As b tends
to zero at fixed a, that family is not tight, so its scalar fallback cannot
make it globally continuous. The random-word family instead converges to a
Gaussian supported on span{I,E12}; the same polynomial coupling proves this.
This is a failed regularization mechanism with an explicit surviving route.

For comparison, any Borel probability mu on M2 invariant under conjugation
by all GL2(C) is supported on the center. Conjugation by diag(r,r^{-1}) scales
the 12 and 21 entries by r^2 and r^{-2}. A complex random variable invariant
under multiplication by 2 is zero almost surely: the disjoint annuli
{2^k<=|z|<2^{k+1}} all have equal mass, hence zero, and their union is z!=0.
Thus mu is supported on diagonal matrices. Invariance under one fixed
non-diagonal change of basis, for example [[1,1],[1,-1]], then forces the two
diagonal entries to agree. Conversely every central probability is invariant.
No moments, density or finite-support assumption is needed.

This does not obstruct an equivariant conditional kernel on noncentral
neighbor conditions: the condition transforms along with its law. In the
random-word construction a central condition produces only central content,
while an irreducible condition produces full support. A globally conjugation-
invariant probability on countably many site matrices has central one-site
marginals and therefore almost surely only central contents; conditioning on
specific noncentral Records is a different hypothesis. None of these symmetry
conditions is silently promoted into axiom content.

## 8. Whole-lattice supplied formation process

A normalized local kernel is not yet a formation history. The random-word
kernel admits the following explicit process on the countable lattice, given
an arbitrary fixed initial Record configuration R0 and a supplied rate lambda>0.
Every initially blank site x receives an independent exponential time T_x of
rate lambda and an independent 259-component complex Gaussian mark. At T_x it
writes Y_eta using the neighbors already recorded at that instant. Existing
Records are untouched, and each site writes only once.

This simultaneous countable construction does not require a first event on
the infinite lattice. To determine a site's value before time t, recursively
follow nearest-neighbor ancestors with strictly decreasing formation times.
A length-n self-avoiding dependency path lies in a prescribed time simplex;
its probability is at most (lambda t)^n/n!. There are at most 6^n candidate
paths from a root. Therefore the probability of a depth-n ancestor path is
at most (6 lambda t)^n/n!, tending to zero. The finite-branching ancestor tree
is almost surely finite, by the elementary fact that an infinite finitely
branching tree has an infinite path. Evaluation on this finite directed
acyclic graph defines the mark uniquely. Taking a countable intersection over
sites and integer t defines the full process on one probability-one event.

Finite boxes converge under the same marks, and the probability of a local
boundary discrepancy at distance at least r is bounded by the corresponding
path sum sum_{n>=r}(6 lambda t)^n/n!. The memoryless remaining exponential clocks and unused independent marks
give the Markov property after the finite-ancestor construction. The uniform
bounds and polynomial coupling give continuity of expectations of bounded
continuous local tests. This is a weak Feller statement on the product
state space, not a claim about a C0 semigroup on a locally compact space.
Every initially blank site forms almost surely at finite time; countability
makes this true simultaneously at all sites. Each coordinate is permanent
after its one jump. The law is covariant under translations, proper cubic
rotations and simultaneous algebra similarities when R0 transforms with it.
The rate and initial condition are supplied, not selected by the axioms.

There is a sharp limitation of this particular iid one-shot clock law. If two
initial states differ on a finite set S but have the same occupied-site set,
couple every other mark and time. A difference can reach a site only along
a nearest-neighbor path starting at S whose later n initially blank vertices
have strictly increasing iid continuous times. Each prescribed path has
probability 1/n!, even when the time horizon is infinite. Consequently

    E[number of possibly affected sites] <= |S| sum_{n>=0}6^n/n!
                                        = |S| exp(6).

In particular the influence cluster is almost surely finite. This is an exact
formation-law limitation, not a general bound on all permanent-Record laws.
Making the clock depend on previously formed neighbors changes the hypothesis;
Section10 constructs and bounds an unbounded-growth escape.

## 9. A general commutative-sector statement under the extra covariance

Let K be any normalized conditional kernel equivariant under all simultaneous
GL2(C) similarities, and suppose every neighbor lies in one fixed commutative
unital subalgebra B of M2. If B is noncentral it is span{I,A} for some
noncentral A; there are two cases. In a diagonal presentation the stabilizer
contains all diag(r,r^{-1}), and its invariant probability is diagonal by the
annulus argument above. In a Jordan presentation it contains I+nE12 for every
integer n. If T is conjugation by I+E12, then T^n X is a polynomial in n and
is bounded for infinitely many n only if [E12,X]=0. For each radius R, the
Cesaro mean of 1_{||T^n X||<=R} tends to zero off that fixed subspace. Invariance
and bounded dominated convergence give mu(ball_R)<=mu(fixed). Letting R grow
proves probability one on the commutant span{I,E12}; it does not require
full topological support there. For a central tuple use the
full-similarity invariant-probability result in Section7.

Thus a forming output remains in B almost surely. For any formation history
whose local dependency graph is well founded, induction shows that a common
commutative initial sector remains commutative. The iid clock construction
above satisfies the needed finite-ancestor property. The statement uses the
extra internal covariance and a history hypothesis; the minimal axioms alone
are not claimed to impose either one.

This is not a theorem for every proper generated algebra. A reducible but
noncommuting tuple, for example (diag(1,-1),E12), has only scalar simultaneous
commutant. Its stabilizer gives no analogous probability restriction. The
random-word kernel preserves that tuple's upper-triangular algebra because of
its specific polynomial construction, not because all equivariant kernels
must do so. This counterexample blocks an overbroad bootstrap inference.

## 10. A neighbor-triggered growth escape

The finite-influence result is a property of independent times assigned from
the initial instant. It is not imposed by one-record-per-site permanence.
Here is an explicit alternative supplied formation law using the same local
random-word mark kernel. Start from a nonempty finite initial Record set S.
Every directed lattice edge has an independent exponential transmission delay
of rate lambda/6, started when its source first records. A blank site forms
on the first incoming transmission from a recorded neighbor, then writes
its mark using all neighbors already recorded. Equivalently the instantaneous
blank-site hazard is (lambda/6) times its number of recorded neighbors.

Formation times are directed first-passage times from S with independent
positive edge weights. Along a fixed length-n simple path, its sum is Gamma
with rate lambda/6. Its probability of being at most t is at most
(lambda t/6)^n/n!. The number of candidate paths is at most |S|6^n. Hence

    E[number of sites recorded by time t] <= |S| exp(lambda t),
    Pr(reach graph distance >=r from S by t)
       <= |S| sum_{n>=r}(lambda t)^n/n!.

These bounds prove nonexplosion from a finite seed and a well-defined event
sequence on every finite time interval. Every fixed site has a finite path
from S and a finite sum of edge delays, so every site eventually records
almost surely, simultaneously by countability. The growth is unbounded.
Translations, proper cubic rotations and simultaneous algebra similarities
preserve the law with the seed transformed. Neither lambda nor the seed is
selected by the framework.

For r>=2e lambda t, the outer tail is at most 2|S|2^{-r}, using n!>=(n/e)^n
and the ratio of successive terms. A crude inner bound follows by choosing a
fixed shortest path from one seed to each x. With n=|x-x0|_1,

    Pr(T_x>t)<=2^n exp(-lambda t/12),

by the exponential moment at lambda/12. Therefore a whole l1 ball of radius
r is occupied by t except with probability at most

    (2r+1)^3 2^r exp(-lambda t/12).

For example r=floor(lambda t/48) gives an exponentially small error up to the
explicit polynomial prefactor. These are loose propagation bounds for the
supplied growth law, not emergent relativistic light cones or physical time.

A deterministic mark kernel delta_{C_eta} makes the causal escape especially
transparent. Begin with one seed of content A and all other sites blank.
Every newly formed content is a strictly positive real multiple of A, since
it averages at least one previously formed positive multiple and divides by
six. With seed zero every output is zero; with seed I every output is a
strictly positive scalar multiple of I. Thus one initial distinction reaches
every site eventually under this alternative law, with no Record erasure.
This changes the clock law, not the permanence rule. The Gaussian random-word
kernel can also be used, but this exact deterministic boundary realization
already falsifies a general finite-influence inference.

## 11. Current conclusion and next physical obligation

The most useful result of the block is the total continuous random-word
kernel and the explicit choice between two whole-lattice formation laws.
It removes a fixed matrix metric from this candidate probability construction
and identifies its actual support from the neighbor-generated algebra.
A balancing metric remains available on irreducible conditions when a later
proposal needs a fiber inner product, with a proved degeneration boundary.

The next physical question is whether an algebra-covariant formation law can
support a specified persistent interacting observable sector and select its
weights from an independently justified rule. Neither a normalized kernel,
an unbounded growth process, nor a locally derived inner product answers that
question. The initial commutative-sector result shows where noncommuting
relational data must enter under the extra symmetry. The axioms are not
proved inconsistent and no update is claimed forced.

## 12. Source and implementation boundary after repository comparison

The current `RECORD_NATIVE_MARKED_PURE_BIRTH_RESOURCE_GENERATOR_BOUNDARY`
note dated August14 already constructs general bounded marked pure-birth
processes from finite seeds, with a supplied occupancy pointer and mark law.
Accordingly, whole-lattice Markov existence by itself is prior support, not a
new claim of this block. The new candidate content is the algebra-covariant
full-domain word kernel, its exact generated-algebra support, the relational
metric alternative and degeneration, and the explicit iid-clock versus
neighbor-triggered influence comparison. Richardson/first-passage growth and
Kempf--Ness balancing are standard mathematics, with direct proofs here.

A Record map with M2-valued entries is treated here as a classical space of
locked contents on which the proposed conditional law is evaluated. This does
not construct a physical nondemolition instrument that reads an arbitrary
unknown live qubit, nor does it prove an occupancy pointer or common-fiber
comparison interface. If a downstream proposal interprets these matrices as
unknown live quantum states instead of locked classical contents, its no-copy
and physical instrument obligations remain separate and cannot be discharged
by the present kernel.

A possible fixed content-only Gaussian trace uniformizer was also checked
against current main before development. The August10
`ADMISSIBILITY_GAUSSIAN_CONTENT_ONLY_UNIFORMIZER_WEIERSTRASS_DECODER_BOUNDARY`
note already supplies that mechanism. No new block or claim is made for it.

The positive construction, its restricted inference boundaries, and seven
finite author check families are being preserved privately while a stronger
physical consequence is sought. A public PR is not forced by this checkpoint.


## 13. Author verification and disposition

Seven final finite families check the actual kernel map, independent fixed
Gaussian covariance and factorized quadrature, seven generated-algebra ranks,
nonunitary metric and word covariance, all24 proper-cubic word permutations,
a nilpotent degeneration, all line orders through eight sites, a24-order
cycle control, and two distinct finite first-passage solvers. These are bounded
falsifiers for the analytic arguments, not proofs of infinite-volume physics.
Nine final actual source faults are caught. An earlier fault deleting the
quadratic/cubic terms of the sampled kernel survived because the covariance
check used a separate word list. The corrected check extracts columns from
the actual source map and compares with an independently specified4x4 matrix.
The initial source and failure receipt are preserved. A separate initial
SymPy structural equality failure was corrected by simplifying the exact
zero difference; neither failure is concealed as an original successful run.

The cold source read corrected one probability wording: concentration on the
commutant is not full topological support on that commutant. No mathematical
claim of a noncentral seed, chosen physical metric, quantum instrument,
selected probability profile, selected clock or new axiom is made. This block
stays private for now; its strongest new construction does not yet identify
a persistent interacting physical sector. The campaign continues personally.
