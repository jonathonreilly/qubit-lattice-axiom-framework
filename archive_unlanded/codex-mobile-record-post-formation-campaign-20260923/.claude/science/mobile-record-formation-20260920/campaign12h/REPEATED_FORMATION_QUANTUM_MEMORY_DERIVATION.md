# Primary derivation: repeated formation and the quantum memory resource

2026-09-21. Primary work with a completed separate pre-source check. This investigates
an explicitly supplied ordinary-quantum interface. It is not a claim that
the minimal-axiom record must be an unknown physical qubit.

## Two independent formation marks are a stronger requirement than one

Let the physical input be one unknown Pauli-axis pure state rho_a, with no
input-correlated ancillary information. In the exactly realizable one-event
family P(b|a)=(1+j v_a dot v_b)/6, ask for two conditionally independent
classical outputs given the original immutable label a:

```
P(b,c|a)=P(b|a)P(c|a).
```

This is a model of two isolated formation episodes with fresh blanks and no
feedback from the first child to the stipulated parent label. It is a full
history requirement, stronger than matching a one-event marginal. Adaptive
control, arbitrary ancillas independent of a, and discarding the parent at
the end are permitted. Every such two-output experiment is nevertheless a
single POVM on the original qubit.

For the output b=c=+x, the requested probability averaged over input +/-x
is (1+j^2)/36. Averaged over input +/-y it is 1/36. Both input mixtures
are I/2. Thus no quantum experiment on the single initial qubit realizes
this exact two-event history for j!=0, even if parent disturbance is allowed.
The one-event square-root instrument is consistent because its later
statistics depend on the changed parent and previous result. It does not
provide the stipulated iid history of an unchanged hidden preparation label.

If only the two newborn qubits are supplied and the classical marks are
discarded, independent children have target density operator

```
Omega_a=[(I+lambda v_a dot sigma)/2] tensor
        [(I+lambda v_a dot sigma)/2],       lambda=j/3.
```

The antipodal mixtures along x and y now differ by
lambda^2(sigma_x tensor sigma_x-sigma_y tensor sigma_y)/4, which is nonzero
for lambda!=0. Thus that independent-children target also fails affine
consistency. Merely asking for the two individual marginals is weaker;
correlated outputs are not excluded by this product-state witness. An explicit
channel measures the one-event POVM and prepares rho_b tensor rho_b. Both
marginals are correct for every |j|<1, while the siblings are correlated.
The difference of the two incompatible target mixtures has eigenvalues
+/-lambda^2/2 and two zeros, so their trace distance is lambda^2/2. The same
triangle argument gives a worst-input trace-distance error lower bound
lambda^2/4=j^2/36 for the product-child target, without claiming optimality.

## A sharp weak-coupling error for the two classical marks

Let delta be the largest total-variation error over the six input rows,
optimized over arbitrary 36-outcome qubit POVMs. Compare the two target
antipodal-mixture output laws M_x and M_y. They differ only where both
outputs lie on axis x or both on axis y, and

```
TV(M_x,M_y)=j^2/9.
```

Any qubit POVM produces the same distribution on those two preparations.
Convexity and the triangle inequality therefore imply delta>=j^2/18.
For |j|<=1/2 this bound is attained by the explicit effects

```
E_(b,c)=[I+j(v_b+v_c) dot sigma]/36.
```

They are positive because |v_b+v_c|<=2, and they sum to I. The realized
probabilities differ from the iid target only by the removed term
j^2(v_a dot v_b)(v_a dot v_c)/36. For a Pauli-axis input, exactly four
entries have nonzero discrepancy, giving total variation j^2/18. Both
one-event marginals remain exactly the specified six-outcome POVM.

Thus two individually correct formation marginals can coexist through
correlations between the outputs, but exact conditional independence fails.
At j=1/2 the optimal worst-row error to the iid two-mark target is 1/72.
For larger |j| the lower bound remains valid, while these explicit effects
cease to be positive; no sharp formula for that regime is claimed here.

## An explicit resource that permits unlimited repeatable formation

The following construction tests a real alternative rather than declaring
the classical record kernel physically impossible. Supply an orthogonal
three-valued axis register, with state |axis(a)> accompanying the parent.
The six joint input vectors

```
|Psi_a> = |axis(a)> tensor |psi_a>
```

are mutually orthogonal: different axes are separated by the register and
opposite signs on the same axis are already orthogonal qubit states.
For any classical kernel P(b|a), including arbitrary positive p,q,r, define

```
K_b=sum_a sqrt(P(b|a)) |Psi_a><Psi_a|.
```

These Kraus operators form a complete instrument on the six-dimensional
record space. Conditional on every outcome b, the retained encoded record
is exactly Psi_a. Fresh instruments therefore generate arbitrarily many
conditionally iid marks with the prescribed row law, without changing the
encoded parent. Product-weight marked clocks for multiple encoded parents
are implemented by the corresponding positive diagonal rate operators.
This is ordinary copying of orthogonal facts, not cloning of nonorthogonal
unknown qubit states. The axis register is an additional physical resource.

For the nonzero j-family, this extra dimension is also necessary for an
unlimited iid-history interface when the parent reduced state is the pure
rho_a. Every initial joint state must then be a product rho_a tensor tau_a.
Distinct kernel rows become perfectly distinguishable in the limit of many
iid marks, for example by their empirical frequencies. Contractivity of
trace distance under the complete N-output channel implies that the initial
joint states for distinct rows must have orthogonal supports. For the three
inputs +x,+y,+z, the qubit factors have pairwise nonzero overlaps. Their
ancillary states tau_a must therefore have mutually orthogonal supports,
requiring ancillary Hilbert dimension at least three. The axis-register
construction attains this bound. The argument uses no ability to measure
the unknown qubit without disturbance.

A single extra input-correlated qubit, such as another copy of rho_a, can
supply information for one event while preserving the original parent. It
does not evade this unlimited-history lower bound. The bound concerns a
finite initial memory resource and unlimited iid reuse, not a supply of
fresh input-correlated systems at every event. Uniform, input-independent
kernel rows are the trivial exception.

If vacancy is also an orthogonal, locally readable state distinct from the
six encoded contents, that single-cell memory has dimension at least seven.
Three qubits can encode such a cell, using seven of their eight computational
basis states. This is a block construction with an explicit storage cost;
it is not an identification of one fundamental M2 site with seven orthogonal
states. A claim that surrounding history or geometry supplies the axis
register must actually locate and transport that information. It cannot
be treated as free preparation knowledge.

If the entire cell, including vacancy, is required to keep a fixed tensor
factorization C^2 tensor C^d, dimension at least seven instead requires d>=4.
The seven-dimensional direct sum and the fixed qubit-times-ancilla architecture
are separate assumptions; neither is implicit in the bare word vacancy.

## Campaign interpretation and completed checks

The unknown-qubit, classical-label, and encoded-record readings make different
operational demands. A one-event rate construction alone does not settle
the full history. Conversely, an unknown-qubit obstruction does not rule
out the positive encoded-record construction. The remaining framework task
is to specify which operational resources a record and its moving carrier
actually contain, and derive their dynamics and storage from declared premises.

The primary checker verifies exact mixture witnesses, eleven unrestricted
36-effect qubit POVM programs at weak and strong j, and explicit encoded
instruments and two-step joint laws. No sharp larger-j optimum is inferred
from those numerical fits. Results are in `REPEATED_FORMATION_QUANTUM_RESULTS.json`.

The separate pre-source report `independent_repeated_formation/REPORT.md`,
SHA-256 `c4560984c11009def72d5f7726224261d4dac23ec7ed05dcd552c3ddc7e4337e`,
sealed at 02:22:15 UTC, confirms the mathematical claims. Its complete report
and checker were read, and all five sealed artifacts verified. Its controls
include 3,888 encoded three-event histories. The explicit correlated-child
channel, trace-distance lower bound, and distinction between the two vacancy
architectures above are credited to that calculation and reconstructed here.
This is selective mathematical scrutiny, not an independent audit or physical
prediction. A complete formal publication source review remains separate.
