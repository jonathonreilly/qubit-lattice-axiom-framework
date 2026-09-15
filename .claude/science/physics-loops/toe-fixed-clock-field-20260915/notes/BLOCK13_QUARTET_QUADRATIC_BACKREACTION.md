# Quadratic coframe drift and a resonance in the supplied quartet flow

Personal derivation, 2026-09-15. PROVISIONAL; personal analytic review and bounded checks completed.
No independent scientific audit or retained-status decision.
This remains a one-loop weak-coupling calculation for the supplied Hall-free
massless phase. It does not prove that phase or control all loop orders.

## 1. Why the linear mean mode needs another look

Block11 derives two different linear powers for the actual four-Weyl-node
quartet. Writing z=1+2 kappa e0^2 L and kappa=1/(6pi^2), inter-node coframe
contrasts decay as z^-1, while the mean matter/photon mismatch decays as
z^-2. The square of a contrast therefore decays at exactly the latter
power. This is a possible resonance; the linear mean law alone cannot
resolve it. The quadratic photon polarization derived there is unaffected
by the mean correction below, because that correction first enters its
variance at higher anisotropy order.

Use initial zero first-order mean mismatch and four trace-free contrasts
Delta_i0 with weighted mean zero. They may have arbitrary symmetric
orientations. Define

 V= N^(-1)sum_i n_i Delta_i0^2,  N=sum_i n_i,

with unit charges and n_i=1/2 for each Weyl node. The actual quartet has
N=2. Keep terms through second order in the initial contrasts. Initial
second-order mean mismatch and common metric are allowed and are displayed
below. An independent birefringent initial tensor is at most second order.

## 2. Derive the quadratic self-energy coefficient from the full integral

The source's four-dimensional coframe integral, with E=I4+C and C00=0, is

 M(E)=-int_0^1 dx x det(A)^(-1/2)
          [2E^2-tr(E^2)I4] E A^(-1),
 A=xI4+(1-x)E^2.                                  (1)

Set T=tr(C), Q=tr(C^2); these equal the spatial traces because C00=0.
For y=1-x,

 A^(-1)=I-2y C+(4y^2-y)C^2+O(C^3),
 det(A)^(-1/2)=1-yT+(y^2-y/2)Q+(y^2/2)T^2+O(C^3).

Multiplication and elementary parameter integration give

 M=I-(5/3)C+(2/3)T I-2C^2+T C+(Q/2-T^2/4)I+O(C^3).
                                                               (2)

The scalar temporal coefficient is
 M00=1+(2/3)T+Q/2-T^2/4.
The coframe velocity renormalization uses M_spatial-M00 E_spatial, not
M_spatial alone. Consequently

 M_spatial-M00 E_spatial
       =-(8/3)C-2C^2+(T/3)C+O(C^3).              (3)

Multiplying by e^2/(8pi^2) gives the self-energy contribution to dC/dL.
For trace-free first-order contrasts the quadratic source is

 dC_i/dL=-2 kappa e^2(C_i-C_g)
           -(3/2)kappa e^2 Delta_i^2+O(e^2 delta^3).        (4)

Here C_g and the matter mean start at second order; delta measures the
initial contrast size. Terms from an initial first-order common metric
are removed by the one common coordinate choice. A photon nonmetric tensor
of second order has no linear contribution to the fermion coframe at one
loop, as checked by the angular/Clifford identity in Block11. Products
of that tensor with a first-order contrast are beyond(4).

An independent scalar check is available. Put C=c I3 in(3); it gives
 -(8/3)c-c^2. This agrees with the expansion about r=1 of the source's
exact scalar coefficient

 dr/dL= -e^2(4r^2+3r+1)(r-1)/[6pi^2(r+1)^2]

when the photon speed is held at one. This checks both temporal subtraction
and the quadratic sign; the coupled photon flow is a different term.

## 3. The photon metric receives its own quadratic source

For a positive symmetric spatial coframe E_i=I+C_i, the metric Maxwell
constitutive tensors are
 epsilon_i=E_i^2/det(E_i),  b_i=epsilon_i^(-1).
To quadratic order,

 epsilon_i=I+2C_i-tr(C_i)I+C_i^2+(tr(C_i^2)/2)I+O(delta^3),
 b_i=I-2C_i+tr(C_i)I+3C_i^2-(tr(C_i^2)/2)I+O(delta^3),
                                                               (5)

where the first-order traces vanish. Terms linear in the second-order
trace are retained; trace-times-first-order terms are third order.
A normalized positive tensor mixture has a common scalar wavefunction
factor, a metric coframe, and a traceless nonmetric part. Since its
first-order mean vanishes, extracting the metric at this order gives

 C_g=(epsilon-b-tr(epsilon-b)I)/4+O(delta^3)
     =<C_i>-(1/2)<Delta_i^2>+O(delta^3).           (6)

The bracket includes the initial photon and the accumulated matter-loop
weights. An overall common rescaling of epsilon and b changes(6) only at
higher order here. For simultaneously diagonal tensors an exact metric
coordinate is c_i=(b_j b_k/(epsilon_j epsilon_k))^(1/4); expanding it
checks(6). No simultaneous diagonalization is used for the quadratic
matrix formula.

The incremental photon equation is thus

 dC_g/dz=[Cbar-C_g-(1/2)V z^(-4/N)]/z+O(delta^3),
 dCbar/dz=-2(Cbar-C_g)/(Nz)-(3/(2N))V z^(-1-4/N)+O(delta^3).
                                                               (7)

The gauge-coupling normalization can receive second-order corrections;
its effect on first-order contrasts starts at third order and its effect
on the displayed quadratic terms at fourth order. Thus the leading
z=1+kappa N e0^2 L suffices at the anisotropy order stated here.
The remainders in(4)-(7) are coefficient-expansion notation. Uniform
control of their integral for arbitrarily large L is not asserted.

## 4. Solve the resonant mean and the common drift

Let R=Cbar-C_g and C_*=(N Cbar+2C_g)/(N+2). At quadratic order,

 dR/dz=-(1+2/N)R/z+[(N-3)/(2N)]V z^(-1-4/N),
 dC_*/dz=-5V z^(-1-4/N)/[2(N+2)].                (8)

For N!=2 the sourced relative solution is

 R(z)=R(1)z^(-(1+2/N))
       +[(N-3)/(2(N-2))]V[z^(-4/N)-z^(-(1+2/N))].        (9)

For the actual N=2 quartet it is instead

 R(z)=R(1)/z^2-(V/4)log(z)/z^2,
 C_*(z)=C_*(1)-(5/16)V(1-z^-2).                  (10)

In general the last coefficient is5N/[8(N+2)] and z^-2 is replaced by
z^(-4/N). Thus the weighted common metric conserved by the linear flow
is not conserved by this quadratic truncation. It shifts by a finite
amount depending on the initial contrasts. This is not a selected physical
speed. The relative mean still decays in the quadratic equations, now
with a logarithmic correction. At N=3 the displayed quadratic relative
source cancels; that cancellation does not remove the common drift.

For zero second-order initial mean data at N=2,

 Cbar(z)=-(5/16)V(1-z^-2)-(V/8)log(z)/z^2,
 C_g(z)=-(5/16)V(1-z^-2)+(V/8)log(z)/z^2.          (11)

Initial R(1) adds +/-R(1)/(2z^2), and initial C_*(1) adds equally to both.
The exact positive-tensor history formula in(6), using this Cbar and
Delta_i(z)=Delta_i0/z, recovers C_g in(11). This supplies a second algebraic
route to the photon backreaction; it is not independent scientific review.

## 5. Apply the actual native quartet contrast

For the small mixing-angle perturbation in Block11,

 Delta_(s_x,s_z),0=s_x s_z d(E_xz+E_zx),
 d=-mu^2 eta/[2(1-mu^2)sin^2 b],
 V=d^2 diag(1,0,1).

Hence the universal quadratic sourced part of the relative mean is

 -(d^2/4)diag(1,0,1) log(z)/z^2.                 (12)

The microscopic angle family may also produce a second-order initial
mean mismatch, which contributes the homogeneous R(1)/z^2 term. It
cannot remove the logarithmic coefficient for every z. A second-order
correction to the signed contrast itself affects its square only at
third order and therefore does not alter(12).

The photon polarization remains, through quadratic order,

 W=2d^2(z^-1-z^-2)diag(1/3,-2/3,1/3),

as in Block11. The common coframe shift affects the definition of the
instantaneous metric coordinates but changes this second-order splitting
only at higher anisotropy order. These results specify additional terms
that an eventual controlled interacting-flow theorem must reproduce.
They are not a nonperturbative attraction proof or a photon-phase theorem.

## 6. Verification and review

The checker derives the full quadratic coefficient twice, first by the
Feynman parameter formula and then by the unshifted angular integral with
exact S3 moments through degree six. Temporal normalization and the exact
scalar-speed comparator agree. Full positive four-dimensional matrices
at shear.04,.02,.01 have central quadratic-source errors
7.545e-4,1.886e-4,4.714e-5; they decrease quadratically with the step.

Symbolic ODE substitution and direct photon-history integration agree at
N=1,2,3,4,6, keeping both the N=2 resonance and N=3 cancellation. Nine
full positive constitutive mixtures challenge the common drift and the
unchanged polarization coefficient; errors decrease at fourth order in
the reflected shear amplitude. No numerical phase or higher-loop theorem
is inferred. See the [personal N1-N8 review](BLOCK13_ROUTE_AND_NO_GO_REVIEW.md).
