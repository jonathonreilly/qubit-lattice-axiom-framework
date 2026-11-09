# Local algebra to record probability: exact types and conditional bridge

2026-11-09. Frozen author proof before the new checker sees this text.
Research parent: 37976c19e673305b1efafc0578327481d9f04c24.
Governing source: origin/main bf92a1d763030836ed55631d5d7a7ef3b288f284,
docs/MINIMAL_AXIOMS_2026-06-29.md, SHA256
301bb33c1a743104208067c14684b34ba71d86674509111638ea898bc6e6c0dc.
Claim type: bounded_theorem. Status: conditional-support; author proposal.
No governing source, approved primitive or audit status is changed.

## 1. What follows before a measurement interpretation

Write R for a configuration of permanent records, eta_x(R) for the supplied
neighborhood condition of site x, and F(eta_x) for its conditional content law
if a record forms there. The axioms supply one such law, its dependence on
the neighborhood, spatial covariance, admissible contents and permanent,
content-determined readout. They do not supply the function F's values.
An unchanged neighborhood gives the same conditional content distribution.
This is not an assertion of independent events or a formation rate.

Using the ordinary meaning of probability distribution, disjoint sets of
possible record contents have additive probabilities. For a supplied joint
history law, conditioning on an event of positive probability uses the usual
ratio. Neither observation constructs that joint history law. Rereading a
fixed content with the same fixed decoder returns the same readout. It does
not follow that a fresh detector measurement has the same value.

Three objects have different types:

* A content law mu is a probability measure on the possibilities M2(C).
* A matrix functional ell maps matrices to scalars, and may or may not be
  linear, positive or normalized under a chosen order structure.
* A physical event/effect correspondence would associate an experimentally
  realizable record event with a specified algebraic object.

The first object is named by Admissibility. The other two cannot be identified
with it by reusing the word state. The governing state is R, not automatically
a positive linear functional or a density matrix.

## 2. An algebraic result requiring no Born rule or adjoint

For A in the complex algebra M2(C), let L_A(B)=AB, a linear map on the
four-dimensional complex algebra. Define

    tau(A) = Tr_complex(L_A)/4 = tr(A)/2.

Left multiplication acts by A on each of two columns, so Tr(L_A)=2 tr(A).
The definition is invariant under algebra isomorphisms: for an isomorphism
T, L_(T A)=T L_A T^(-1). No adjoint or positivity cone is used here.

Moreover tau is the unique complex-linear functional ell with ell(I)=1
and ell(AB)=ell(BA). For matrix units, ell(E12)=ell(E11 E12)
=ell(E12 E11)=0, likewise ell(E21)=0, and
ell(E11)=ell(E12 E21)=ell(E21 E12)=ell(E22). Normalization sets each
diagonal value to 1/2. This proves uniqueness, rather than assuming it.

This result does not say every matrix has a probability tau(A):
tau(2I)=2 and tau(iI)=i. Nor does it give probabilities to record-content
singletons. In particular tau(I/2)=1/2 is a functional value; it does not
assert mu({I/2})=1/2 for a content law mu. The literal contents I and I/2
are different possible recorded matrices, not automatically the certain
event and a fair coin event.

## 3. What symmetry actually constrains

For any supplied equivariant kernel F and relabeling g,
F(g eta)=g_* F(eta). If g fixes eta and exchanges two measurable outcome
sets B and C, their probabilities must agree. This follows by applying
equivariance to B. It gives equality within a symmetry orbit, not weights
between structurally distinct orbits. Algebra automorphisms fix 0 and I
separately. No algebra symmetry exchanges them or forces their odds to 1/2.
Spatial covariance is explicit in the axioms. Extending covariance to a
particular internal algebra-automorphism group must be stated; the following
stronger mathematical test is conditional on that interpretation.

**Conditional finite-measure theorem.** A Borel probability mu on M2(C)
invariant under every similarity A -> S A S^(-1), S in GL2(C), is supported
on the scalar matrices. Conversely every probability supported there is
similarity invariant. This is a theorem about content measures, not about
positive linear functionals on a C*-algebra.

Proof: write the random matrix as [[a,b],[c,d]]. Similarity by diag(2,1)
scales b by 2 and c by 1/2. A finite random variable Z whose law is invariant
under multiplication by 2 is zero almost surely: the annuli
2^j <= |Z| < 2^(j+1), j in Z, have equal probability, so finite total mass
forces every annulus to have mass zero. Apply this also to c (invariance
under 1/2 implies invariance under 2). Thus b=c=0 almost surely. Conjugating
diag(a,d) by [[1,1],[0,1]] produces upper entry d-a. Invariance and the
already proved zero off-diagonals imply a=d almost surely. Conversely
each scalar matrix is fixed pointwise. No moment bounds are required.

Thus even this strong covariance does not choose a measure: every mixture
q delta_I+(1-q) delta_0 is invariant. At an empty, symmetry-invariant
neighborhood it cannot produce a full-support measure on all of M2(C).
This last implication requires both the strong internal covariance and
empty-condition invariance. Neither full support nor that full internal
group is asserted as an additional governing axiom here. With a supplied
adjoint and only unitary conjugations, noncentral invariant measures exist,
for example the uniform orbit measure on rank-one orthogonal projectors.
That different symmetry convention does not force Born weights either.

## 4. The lattice and permanent records do not remove the exhibited freedom

Reuse the previously checked autonomous_runtime/RESULT.md section 6, with
its interpretation and domain explicit. On the literal infinite Z3 lattice,
let the legal record states be {absent,0,I}^Z3 and the full local possibility
domain remain M2(C). The axioms do not require every possible matrix to be
in the support of each law. For six immediate neighbors let k count present
records and l count I records. For any a in (0,1), choose

    p_a(eta)=(a+l)/(1+k),
    F_a(eta)=p_a(eta) delta_I + (1-p_a(eta)) delta_0.

Both weights are strictly positive for every 0<=l<=k<=6, so every old 0/I
record remains admissible after any later neighborhood changes. The law is
nonconstant, is spatially covariant, and uses only algebraically defined
contents; it is invariant even under independent local algebra relabelings.
One obtains an explicit total kernel on neighborhoods with arbitrary matrix
contents by counting all present records in k and just exact I contents in l.
The legal record domain of this witness stays {absent,0,I}^Z3. It is not a
claim that arbitrary noncentral initial records satisfy its support rule.

Supply independent rate-one first-birth clocks and uniform marks, once per
initially absent site; this is an example of a formation law, not its
derivation. At an event only earlier neighboring records matter. For a
root event at time <=t, a dependency path of m earlier random sites has
probability at most t^m/m! for any specified self-avoiding path. There are
at most 6^m paths. Hence the probability of an ancestor path of length m
is at most (6t)^m/m!, tending to zero. Finite branching then gives finite
ancestry almost surely. This argument constructs all countably many events
consistently, without a first event for the entire infinite lattice.
Initially recorded sites are fixed terminal boundary inputs. Memorylessness
and fresh marks give a record-only time-homogeneous process. Readout may
be the indicator that content equals I; it is content-determined.

For the same empty-neighbor record condition, the models a=1/4 and a=3/4
give I probabilities 1/4 and 3/4. These are two explicit lawful choices on
the stated domain, not a fit to experiments or a quantum-device calibration.
They establish probability-law nonuniqueness under this reading. They do
not show that no quantum sector, further bridge or empirical discriminator
can exist. The proof uses no Born or tensor-product assumption.

## 5. Granting familiar one-qubit geometry still leaves a decisive test

This section deliberately grants EXTRA measurement typing: a fixed adjoint,
rank-one orthogonal preparation projector P, and effects 0<=E<=I.
It is not a construction of those devices from the lattice axioms.
Let t=tr(P E) and define

    h(t)=t^2/[t^2+(1-t)^2],   f_P(E)=h(tr(P E)).

On [0,1], h is smooth, increasing, nonnegative, with h(0)=0, h(1)=1
and h(1-t)=1-h(t). It defines normalized probabilities for every binary
menu {E,I-E}; it respects simultaneous unitary covariance and perfect
repeatability at the level of probabilities for {P,I-P}. For rank-one
P,Q it also respects preparation/outcome reciprocity since tr(PQ)=tr(QP).
It disagrees with Born at t=1/4, where h(t)=1/10. This is a rival binary
probability assignment under these extra structures, not a full process
or a noncontextual all-POVM model.

The missing constraint is visible exactly, without numerics. The three-effect
menu {I/4,I/4,I/2} sums to I, but the same assignment gives total
1/10+1/10+1/2=7/10. Equivalently, f_P(I/4)+f_P(I/4) != f_P(I/2).
Each repeated I/4 is a distinct outcome event with the same effect label;
ordinary set union of contents cannot represent that menu by itself.
Binary normalization, smoothness, symmetry and repeatability do not enforce
this refinement consistency. The assignment is rejected once the latter
is supplied. This example strengthens the type distinction of section 1.

## 6. The exact conditional bridge that WOULD determine the form

Suppose separately that the physical devices and record coarse grainings
supply all of the following on one M2(C) with a fixed adjoint:

E1. Every effect 0<=E<=I is realizable as a record event.
E2. For fixed preparation record data r, its probability f_r(E) depends only on
    the effect, not on which device context/refinement realizes that effect.
E3. Exclusive realizable events with effects E,F and E+F<=I can be grouped
    as an event with effect E+F, in a context where both are represented;
    the certain event has effect I.

E1-E3 are proof obligations, not amended axioms. They identify physical
events and operator sums. Admissibility's ordinary event-set additivity
then gives f_r(E+F)=f_r(E)+f_r(F), f_r(I)=1, f_r(E)>=0.
Here r denotes preparation data. Different apparatus contexts may have
different complete record configurations R; E2 is precisely the additional
claim that those implementations have the same probability for an effect.

Here is the finite argument, also proved for the supplied composite setting
in joint_record_law/RESULT.md. Additivity gives f(0)=0 and rational
homogeneity on effects; positivity gives monotonicity because F-E>=0
implies f(F)-f(E)=f(F-E)>=0. Rational lower and upper bounds for a real
t in [0,1] squeeze f(tE)=t f(E). For positive A define
g(A)=c f(A/c) for c>0 with c>=||A||. Comparing any two such c by the
effect homogeneity proves independence of c. A common sufficiently large
c proves g(A+B)=g(A)+g(B), and rescaling proves positive real homogeneity.
For Hermitian H=A-B define g(H)=g(A)-g(B): if A-B=C-D then A+D=C+B,
so this is well-defined and real-linear. Finite-dimensional trace duality
gives a unique Hermitian rho with g(H)=tr(rho H). Nonnegativity on
rank-one positive matrices makes rho>=0; g(I)=1 makes tr(rho)=1.
Consequently

    f_r(E)=tr(rho_r E).

This derives the Born FORM and a density-matrix representation under E1-E3.
It does not choose rho_r, a source preparation, dynamics, tensor composition,
an outcome instrument or joint spatial statistics. rho_r can be a derived
summary of records if a law producing f_r has been constructed; this theorem
does not require asserting an additional independent ontic state. This is a
finite-dimensional Busch-type theorem, not a new theorem of quantum theory.
Reference: Paul Busch, https://arxiv.org/abs/quant-ph/9909073.

## 7. Result and next concrete obligation

The current axioms give neighborhood-conditioned content probabilities and
permanent readouts. Their local algebra also has an intrinsic normalized
trace. The displayed lawful record processes leave physical probability
values free, including under the strong symmetry test. The trace functional
cannot silently replace a record-content measure. Even granting usual
binary quantum measurement geometry does not fill that gap.

The precise constructive target is to build actual neighborhood record
operations and an effect map, then prove E1-E3 (or a genuinely smaller
sufficient domain theorem) from their physical operation. In particular,
derive why regrouping physically exclusive record branches corresponds to
operator addition and why different realizations of the same effect give
the same odds. Mere classical grouping is already additive but supplies
neither the effect map nor its context independence. Selecting a particular
update law to do this must remain labeled a model choice until justified.

This packet does not show that every possible economical foundation is
blocked, claim a smallest new axiom, or change the current axioms. The
remaining operational bridge is an open proof obligation. No Yang-Mills
mass gap, vacuum selection or quantum-limit theorem follows here.
