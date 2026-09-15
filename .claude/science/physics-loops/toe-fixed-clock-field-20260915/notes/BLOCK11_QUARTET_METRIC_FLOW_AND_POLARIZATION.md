# Metric contrasts and photon polarization in the supplied Weyl quartet

Personal derivation, 2026-09-15. PROVISIONAL; personal analytic review and bounded checks completed.
No independent scientific audit or retained-status decision.
This is a formal one-loop calculation, not a nonperturbative phase theorem.
It combines the actual Hall-free mixed quartet and the explicit loop
coefficients newly present on main083a58b4e7faca5839a7b31fab553f6fa1f2c254.
It does not assume that equality of bare metrics is protected by T and Mz.

## 1. Exact inputs and the question being answered

The supplied free carrier is
 docs/LOCAL_HALL_FREE_MIXED_WEYL_QUARTET_AND_COMMON_METRIC_BOUNDED_THEOREM_NOTE_2026-09-13.md.
It has four distinct twofold Weyl nodes, unit charge, unbroken ordinary
T=tau_x K and reflection Mz. Its full occupied-band Hall coefficient is
zero. The equal-metric mixing direction is theta=b; a small angle deviation
splits reflected xz metric entries while keeping four simple nodes.
The Hamiltonian, filling, CAR representation and symmetries are inputs.

Use a supplied massless noncompact dynamical photon and a gauge-preserving
weak-coupling prescription. Work in the untilted spatial-coframe sector near
one positive common metric, with no time-space coframe mixing. Finite matching,
possible other marginal operators, stability against ordered/massive phases,
and a fixed finite-qubit gauge realization are not solved. T must remain
unbroken to forbid the Hall term; a free-band symmetry is not proof of that
interacting-state hypothesis.

The loop source is
 docs/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md,
sections on coframe self-energy, photon coefficient, and native matching.
Its explicit one-Dirac calculation gives, with kappa=1/(6pi^2),

    dot C_f=-2 kappa e^2(C_f-C_g),
    dot C_g= kappa e^2(C_f-C_g),
    dot e^2=-kappa e^4.                            (1)

Dot means L=log(mu0/mu). C denotes the symmetric spatial coframe perturbation
after the stated time normalization. These are coefficients of the truncated
one-loop expansion, not all-orders beta functions.

The underlying fermion parameter integral can be checked without an external
sign convention. In the following integral E and C are FOUR-dimensional,
E=I4+C with C=diag(0,C_spatial), and tf uses the four-dimensional trace.
Put A(x)=xI4+(1-x)E^2:

 M(E)=-int_0^1 dx x det(A)^(-1/2)
                 [2E^2-tr(E^2)I] E A^(-1)
     =E-(8/3)C_tf+O(C^2).                         (2)

The common logarithmic radial factor is L/(8pi^2). Removing the wavefunction
factor and setting the temporal coframe to one gives the first coefficient
in(1). The four-component bubble has coefficient e^2 L/(6pi^2), and its
coframe tensor is det(E)^(-1)(E^T E) wedge(E^T E). Those two ingredients
fix the remaining coefficients, including normalization.

## 2. Count the actual Weyl nodes instead of doubling every self-energy

Let i label two-component cones, and let n_i=1/2 for each such cone.
For an optional general Dirac block n_i=1. Its charge is e q_i. The
parity-even closed Weyl trace is half the Dirac trace, since insertion of
(1+chi gamma5)/2 halves its even part. A self-energy on an external chiral
line has no closed trace and has the same relative coframe coefficient as
a Dirac line. Chirality changes no parity-even coefficient. The full lattice
Hall cancellation remains a separate condition, already supplied for the
actual quartet.

Consequently the node-resolved equations are

    dot C_i=-2 kappa e^2 q_i^2(C_i-C_g),
    dot C_g= kappa e^2 sum_i n_i q_i^2(C_i-C_g),
    dot e^2=-kappa N_q e^4,
    N_q=sum_i n_i q_i^2.                           (3)

There is no extra factor of the total node count in an individual fermion
self-energy. For the actual quartet n_i=1/2, q_i=1, i=1,...,4, so N_q=2.

The logarithmic coefficient matches the mixed native jets for the same
reason as in the source note, which can be checked directly here. At each
separated node choose its smooth rank-two spectral subspace; the other bands
are uniformly separated. The projected symbol is its linear Weyl coframe
plus O(a|p|^2), and Peierls vertices have O(a|p|) corrections. Extra spectator
propagators remove the logarithmic singularity. Transfer to another separated
cone samples a photon momentum bounded away from zero and gives no additional
infrared logarithm. Gauge contacts are retained for the Ward cancellation.
Thus summing the four small-momentum annuli gives(3); hard finite terms are
not set to zero by this argument. The domain stays away from a node merger.

## 3. Exact consensus statement for these linear equations

Let N=sum_i n_i, e0^2>0, and take every q_i nonzero. Define

    C_*=[sum_i n_i C_i(0)+2C_g(0)]/(N+2),
    tau=kappa int_0^L e^2(l)dl=log z/N_q,
    z=1+kappa N_q e0^2 L.                         (4)

The weighted common coframe is conserved, even with different charges.
For each matrix component the generator is a star graph: the center is the
photon, an outer node has weight n_i, and the center has weight2. Its two
directed coefficients satisfy detailed balance
 n_i(2q_i^2)=2(n_i q_i^2).
Therefore the generator is similar to a real symmetric negative Laplacian.
Its kernel is exactly the common-coframe line. For the Frobenius energy

    E=sum_i n_i||C_i-C_*||^2+2||C_g-C_*||^2,

one obtains directly

    dE/dtau=-4 sum_i n_i q_i^2||C_i-C_g||^2
             <=-4 min_i(q_i^2) E.                (5)

To see the last step, weighted mean zero gives
 sum_i n_i||C_i-C_g||^2=E+(N+2)||C_g-C_*||^2>=E.
Thus all six spatial coframe components converge in the truncated system.
A zero-charge cone is a disconnected component and is an explicit exception.
At e0=0 there is no flow. The optional general charged collection in(3)
also presumes a gauge-consistent effective action; it is not an arbitrary
uncanceled chiral gauge theory.
The limiting common value C_* is fixed by input data, not selected by the
framework. No physical speed calibration is determined.

For unit charges, let Cbar=N^(-1)sum n_i C_i,
R=Cbar-C_g and Delta_i=C_i-Cbar. The equations diagonalize exactly:

    R=R0 z^(-(1+2/N)),
    Delta_i=Delta_i0 z^(-2/N),
    e^2=e0^2/z.                                  (6)

For the actual quartet these powers are2 and1 respectively. Inter-node
contrasts decay more slowly than the mean matter/photon mismatch.
A single-metric initial simplification would erase precisely these slow modes.
The source's one-Dirac result is recovered at N=1 with no contrasts.

## 4. Photon polarization records the variance of matter metrics

Now restrict the initial relative coframes to small real trace-free shears,
with common initial photon metric set to zero by one coordinate choice.
Take C_i(0)=S0+Delta_i0, weighted mean Delta=0, and no initial birefringence.
The precise nonmetric diagnostic is the traceless part of the constitutive
product epsilon b. At second order write

    W=(epsilon b)_tf/2 + O(C^3),                  (7)

after removing its scalar normalization. This avoids confusing the quadratic
terms of a single exact metric with physical birefringence.
For a matter coframe I+C its exact positive Maxwell tensor has
 epsilon_C=(I+C)^2/det(I+C), b_C=epsilon_C^(-1).
A normalized sum of such tensors has, to quadratic order in trace-free C,

    W=2[<C^2>-<C>^2]_tf.                         (8)

The brackets include the initial photon tensor and the accumulated positive
fermion-loop weights. Unknown second-order changes of the individual metrics
cancel from this product, because each single tensor satisfies epsilon_C b_C=I.
No commutation of different C_i is required at this order.

In fixed coordinates the linear matter mean from(6) is

    Cbar(z)=f_N(z) S0,
    f_N(z)=[N+2 z^(-(1+2/N))]/(N+2),
    Delta_i(z)=Delta_i0 z^(-2/N).

The normalized photon averages are
 <C>=z^(-1)int_1^z Cbar(t)dt and
 <C^2>=z^(-1)int_1^z [Cbar(t)^2+V_Delta t^(-4/N)]dt,
where V_Delta=N^(-1)sum n_i Delta_i0^2. The initial photon has weight1
and C=0. Substitution into(8) gives

 W = [2N/(N+4)](S0^2)_tf [z^-1-z^(-(2+4/N))]
       +2(V_Delta)_tf z^-1 int_1^z t^(-4/N)dt
       +O(C^3).                                   (9)

For the actual quartet N=2,

 W=(2/3)(S0^2)_tf(z^-1-z^-4)
        +2(V_Delta)_tf(z^-1-z^-2)+O(C^3).          (10)

An initial independent W0 of second order in the small anisotropy adds W0/z at this order. For general N=4 the
contrast source gives2(V_Delta)_tf log(z)/z; for N>4 it decays as z^(-4/N),
slower than the homogeneous z^-1 mode. These are exact functions of the
truncated equations; uniform control of omitted orders at infinite L is
not asserted. A contrast multiplet with isotropic V_Delta has no traceless
quadratic source; unequal metrics alone do not guarantee birefringence.
The actual reflected quartet in section5 has nonisotropic variance.
Higher loop order and higher anisotropy order are separate
expansions and neither is silently summed here.

Equation(9) also follows by differentiating the constitutive increment:
 dW/dz=-W/z+2[R^2+N^(-1)sum n_i Delta_i^2]_tf/z.
This is a second derivation of the variance result, not independent science.

## 5. Match the specific allowed mixing-angle perturbation

Use the quartet parent's parameters0<b<pi/2,1/2<zeta<1,
0<mu^2<1-zeta^2. Set R_b=sqrt(1-mu^2),
x*=acos(R_b cos b), z*=acos(1+zeta-R_b).
At aligned angle theta=b its common squared spatial metric is

 G0=diag(R_b^2,1,R_b^2 sin^2 b sin^2 z*/sin^2 x*).

Perturb the mixing angle by eta, keeping the other parameters fixed.
The exact root and determinant formulas in the parent give

    dG_xz/deta|0=-s_x s_z mu^2 sin z*/(sin b sin x*),        (11)

where s_x,s_z name the signs of the node coordinates. All diagonal first
variations are common to the four nodes. Normalize once by D0=sqrt(G0),
and choose the initial photon metric to match that common first variation.
Since a coframe perturbation is half the squared-metric perturbation,

    Delta_(s_x,s_z)=s_x s_z d (E_xz+E_zx)+O(eta^2),
    d=-mu^2 eta/[2(1-mu^2)sin^2 b].                       (12)

This coefficient is measured from the full mixed four-band symbol, not an
assumed species coupling. Opposite reflected cones have opposite shear,
so their linear photon increments cancel. Their squares add:

    V_Delta=d^2 diag(1,0,1).

For S0=0, W0=0, the generated photon diagnostic is therefore

    W=2d^2(z^-1-z^-2) diag(1/3,-2/3,1/3)+O(eta^3).       (13)

It is nonzero for eta!=0 and any finite z>1 at this order, despite exact
Hall cancellation. Along x (or z), the two squared polarization speeds
differ by magnitude4d^2(z^-1-z^-2)+O(eta^3) in the instantaneous common
metric coordinates. Along y this leading split vanishes by the residual
uniaxial symmetry. A coordinate change cannot remove a polarization split.
The same formal flow tends toward a common metric as z grows, but the
birefringent transient decays only as1/z and cannot simply be omitted.

## 6. What this does and does not accomplish

The actual quartet's bare metric mismatch is not, by itself, an axiom wall:
its stated parity-even one-loop equations have attractive inter-node modes.
They also generate an allowed photon response missed by a single-metric
truncation. A supplied Hall-free action and correct node count are essential.

This is not a demonstration of a finite-qubit charged Coulomb phase, an
all-order infrared limit, radiative stability of every allowed microscopic
operator, a physical hierarchy large enough for the slow running, or a
selected speed/charge/vacuum. No numerical physical parameter is fitted.
The [2011 limiting-speed work](https://arxiv.org/pdf/1102.0789) already treats interaction-driven equalization
and its slow logarithmic character; the generic mechanism is not new.
The new bounded calculation matches the actual mixed quartet's tensor
contrast and its second-order photon variance to the supplied loop action.


## 7. Verification and scope review

The paired checker recomputes the parameter coefficients, the Weyl/Dirac
trace count, a24-cell angular control of the vanishing linear W insertion,
and the exact weighted quartet generator. Its eigenvalues are0,2,2,2,4
in tau units. Symbolic integration recovers the constitutive variance at
N1,N2,N4,N6, including the logarithmic resonance.

It independently projects the full four-band velocity matrices at all four
nodes to challenge(12), and compares full positive constitutive tensors
with the quadratic response and its polarization roots. The largest
native derivative error is below2.2e-8 at step1e-3 and decreases quadratically.
A neutral cone and an isotropic contrast-variance multiplet are explicit
exceptions. These are finite checks of a formal derivation, not simulations
of a quantum gauge ground state or independent scientific review.
See [the N1-N8 scope review](BLOCK11_ROUTE_AND_NO_GO_REVIEW.md).
