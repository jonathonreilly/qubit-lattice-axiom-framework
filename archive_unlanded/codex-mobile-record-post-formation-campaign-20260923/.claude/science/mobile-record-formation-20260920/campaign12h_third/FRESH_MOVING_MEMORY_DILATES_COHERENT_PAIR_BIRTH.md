# Fresh departing memory gives an explicit coherent pair-birth dilation

Date: 2026-09-22. Status: author exact finite construction, awaiting independent
check. The fresh probe, its preparation, coupling and motion are supplied
resources, not derived native lattice structure.

## 1. From a specified instrument to a specified unitary interaction

The preceding note showed that the single coherent birth operator
V=V_++V_- preserves a joint gauge-loop phase, whereas separately recorded
orientation channels can lose it. Its algebra is

    V^dagger V=P,  VV^dagger=R,  PR=0,  V^2=0,
    [N_record,V]=2V,  [G_x,V]=0.

P projects on the two vacant matter endpoints with either field value.
R is the resulting two-dimensional charged-pair/field image. The eighteen-
dimensional local system contains other occupied states as spectators.

Add a neutral two-state probe with states |fuel>,|spent>. For each collision,
its incoming state is the pure |fuel>, uncorrelated with the system and all
other unused probes. Define

    A=V tensor |spent><fuel|,  C=A+A^dagger,
    C^2=P tensor |fuel><fuel|+R tensor |spent><spent|,
    C^3=C.

The exact unitary collision is

    U(theta)=I+(cos(theta)-1)C^2-i sin(theta)C.

Every local Gauss operator commutes with C and U. A fresh-probe input produces
the two reduced Kraus operators

    M_0=I-P+cos(theta)P,  M_1=-i sin(theta)V.

For any occupied endpoint, both V and P vanish: M_0 is identity and M_1 is
zero. Thus the fresh-probe collision cannot remove or overwrite an existing
record. A successful birth creates one plus and one minus record, and the
single spent-probe flag does not reveal their spatial orientation. For an
arbitrary coherent vector psi in the vacant/field subspace,

    U(psi tensor |fuel>)
      =cos(theta) psi tensor |fuel>
       -i sin(theta) V psi tensor |spent>.

Conditioning on the event flag therefore preserves the joint input coherence
through the isometry V. No field-orientation measurement is hidden in this
dilation.

Repeated interactions with separately prepared probes are an established
open-system construction. For context, the abstract, introduction and
repeated-interaction setup through section II.1 of
[Attal and Pautrat, arXiv:math-ph/0311002v2](https://arxiv.org/abs/math-ph/0311002v2)
were read. No general stochastic-limit theorem from that paper is imported;
the finite identities and the single-channel law here are derived directly.

## 2. Exact single-channel clock and its parameter cost

Write c=cos(theta), restricted here to 0<c<1, and

    Phi_c(rho)=M_0(c)rho M_0(c)^dagger+(1-c^2)Vrho V^dagger.

The identities

    M_0(c)M_0(d)=M_0(cd),  M_0(c)V=V,  VM_0(d)=dV,  V^2=0

give Phi_c composed with Phi_d=Phi_(cd). Choose a step Delta_t>0 and

    cos(theta)=exp(-beta Delta_t/2).

After n fresh collisions, the reduced state is exactly the value at
t=n Delta_t of the single-channel semigroup with generator beta D[V].
This holds for every local density, including vacancy/occupation coherences,
not just for a classical empty initial state.

This equality concerns collision boundaries. The microscopic unitary can
exchange amplitudes in both directions during a collision. Reading the pair
mid-collision and then letting that same interaction continue is another
experiment, with no permanence theorem supplied here. Treating a completed
outgoing event flag as the registration point is part of this discrete model,
not a derivation of the native continuous formation rule.

It does not derive beta or a clock. The angle and step are chosen to realize
that beta. If U arises from an interaction Hamiltonian lambda C for duration
Delta_t, then lambda=theta/Delta_t. Keeping nonzero beta fixed while
Delta_t tends to zero requires

    lambda ~ sqrt(beta/Delta_t).

A bounded fixed lambda instead has an effective birth rate tending to zero
in that limit. The exact discrete construction needs no such limit; it has
its explicitly supplied finite step. Different noncommuting edge interactions,
hopping and monitoring do not automatically compose into the exponential
of their summed continuous generator at a finite step. That further limiting
or discretization analysis has not been supplied here.

## 3. Energy and memory are accounted for separately

The operator N_record+2|fuel><fuel| commutes with C. If a record has a supplied
positive energy m, choose the probe's fuel level above its spent level by2m:

    H_free=m N_record+2m |fuel><fuel|.

Then [H_free,C]=0 exactly. A pair birth consumes one fuel excitation and
raises the matter energy by2m. The collision formulas above may be read in
the interaction picture of H_free. Thus this particular rest-energy account
does not require energy creation from a vacuum.

This is an energy statement for the stated mass Hamiltonian. Adding kinetic
or magnetic energy generally makes V cease to be a single energy-raising
operator, and the same two-level probe need not conserve that enlarged
Hamiltonian. A full interacting energy-conserving reservoir is a further
problem. The value m and the supply of excited fuel probes are not predicted.

The outgoing probe stores whether formation occurred. It need not be erased:
it can depart and remain part of the joint unitary state. Reading those flags
gives the usual event histories under an ordinary measurement interpretation.
Neither the Born rule nor an ontologically selected history is derived by
writing this unitary dilation.

## 4. Why movement of used memory matters

Freshness is a real hypothesis. The same unitary has a reverse transition
from R tensor |spent> to P tensor |fuel>. At theta=pi/2, apply the same probe
twice to a vacant input:

    first collision: vacant+fuel -> born pair+spent,
    second collision: born pair+spent -> vacant+fuel,

up to phases. The checker verifies record counts2 and0 after these two
collisions. Reusing a spent probe therefore does not implement a permanent
birth instrument. A fresh fuel probe presented to an already occupied pair,
by contrast, leaves it unchanged.

An exact repeated-interaction dilation can use a stream of distinct probes,
each interacting once and then never returning. For finitely many steps,
retain every departed probe in the joint Hilbert space; the product of the
collision unitaries is unitary and no information has been discarded globally.
Tracing past probes gives the stated reduced semigroup at the observation
steps. For arbitrarily many steps this prescription supplies an unbounded
fresh stream. A finite periodically reused stream needs a new analysis.

A directed shift on an infinite probe chain is one abstract unitary way to
move used probes away while bringing fresh probes to the interaction point.
Its step, direction, preparation and physical carrier are additional data.
No autonomous translation- and cubic-covariant M2-per-site compiler for this
stream has been derived. The construction connects memory motion to reliable
local renewal, while exposing the resource and arrow-of-time assumption.

## 5. Minimal pure probe size for the coarse channel

For the real-chi coarse birth-map family of the preceding note, retain the same
no-event M_0 and multiply the formation coefficient matrix by p=1-c^2.
In the eighteen-dimensional local system, the no-event Choi vector is
orthogonal to the two formation-transition Choi vectors. Their squared norms
are respectively 16+2c^2,1,1. The Choi eigenvalues outside the zero subspace
are therefore

    16+2c^2,  (1-c^2)(1+chi),  (1-c^2)(1-chi).

For 0<c<1 and |chi|=1 its rank is2. For |chi|<1 its rank is3. A unitary
dilation with a pure incoming environment of dimension d gives at most d
Kraus operators, hence Choi rank at most d. Conversely a rank-r Kraus
representation gives an isometry into an r-dimensional environment, extendible
to a finite unitary. Thus the minimal pure environment dimensions are2 and3,
respectively. The displayed qubit collision attains the coherent case.

This minimum concerns the summed channel and its coarse event/no-event
instrument. Preserving a specified finer mu-outcome record is an additional
requirement, not classified by chi or by this channel's Choi rank alone.

This result counts a pure fresh environment and all purification resources.
It is not a bound on a mixed probe whose omitted purification carries
additional information. It also does not establish a physical principle
that nature minimizes probe dimension. It makes the resource difference
between a single event flag and an orientation-resolving event record explicit.

## 6. Exact controls and status

gauge_birth_fresh_memory_dilation_check.py checks all36-dimensional unitary,
Gauss, record/resource and Kraus identities, the semigroup composition,
the Choi-vector Gram matrix, coherence transport for arbitrary input
amplitudes, and the explicit reused-probe reversal. The finite calculation
uses exact symbolic arithmetic.

Its first run stopped on structural symbolic equality of two factorizations
of the same Choi-block determinant. The expanded difference is exactly zero;
the original source, complete failure and diagnosis are preserved under
fresh_memory_dilation_exploration/structural_determinant_equality. Replacing
that comparison by an exact expanded-difference test gave a complete run.
No conservation or dynamical equation was changed.

This is a conditional construction using known dilation machinery. It
clarifies which quantum information can survive record formation and how
departing memory can make local irreversibility compatible with joint unitary
dynamics on the specified forward histories. It is not a derivation of the
fresh stream, native record carrier, physical time or a theory of everything.
The scoped reversal boundary remains private pending the negative-claim
publication gate.
