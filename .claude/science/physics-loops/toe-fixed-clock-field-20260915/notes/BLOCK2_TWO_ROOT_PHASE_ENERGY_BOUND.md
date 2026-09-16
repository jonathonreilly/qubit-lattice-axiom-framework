# Two choices of the mixed phase give physical-energy bounds at both roots

Personal derivation, 2026-09-15. Provisional mathematical support for the
fixed-clock coupled-defect campaign. No independent review, all-order gas
theorem, state selection, or physical field limit is asserted.

The mutual phase can be bounded in a way that charges the root's physical
Coulomb energy, instead of the area of its chosen filling. The two species
require different, exactly equivalent representatives of that phase. This
repairs a large-component loss in the even mixed bond. It does not remove
the odd orientation cycles or same-species interactions of the actual law.

## 1. Objects and exact periodicity

Use either a finite free cubical complex with integer H1=H2=0, or finite
integer fillings on Z^4. Let D=d_1, B=d_2, P the orthogonal projection onto
exact two-forms, and Q=I-P the coexact projection. In the infinite setting
these are the bounded Fourier multipliers, with no harmonic l2 sector.

An electric component j has integer filling S with D* S=j and physical
energy E_e(S)=||PS||_2^2. A magnetic component q has integer filling n with
B n=q and energy E_m(n)=||Qn||_2^2. Write

    g=N/sqrt(beta), b=2 pi sqrt(beta), c=g b=2 pi N,
    theta_P(S,n)=c <n,PS>,
    theta_Q(S,n)=-c <Qn,S>.

Here N is an integer. Since P+Q=I and S,n are integer,

    theta_P-theta_Q=c <n,S> is in 2 pi Z.                 (1.1)

Thus exp(i theta_P)=exp(i theta_Q), with identical sine and cosine.
This is exact, including overlapping fills. It does not hold as equality
of the real phase representatives; their difference is a local integer
contact. On a torus an additional harmonic term must be kept; that case
is outside this note.

## 2. Root estimates for an arbitrary positive filling measure

Let nu_e and nu_m be positive marked measures on the integer fillings,
including any desired self-weights and nonnegative mark normalization.
Assume the frame operators

    K_e=integral S tensor S nu_e(dS),
    K_m=integral n tensor n nu_m(dn)

are bounded on the two-form l2 space. Infinite total translation mass is
allowed: the frame integrals are defined by their bounded quadratic forms.
Set f(S,n)=cos(theta_P(S,n))-1. Then

    integral |f(S,n)| nu_m(dn)
      <= (c^2/2) <PS,K_m PS>
      <= (c^2/2) ||K_m|| E_e(S),                        (2.1)

whereas, using the other phase representative,

    integral |f(S,n)| nu_e(dS)
      <= (c^2/2) <Qn,K_e Qn>
      <= (c^2/2) ||K_e|| E_m(n).                        (2.2)

The proof is simply 1-cos(t)<=t^2/2, followed by the frame identity and
its operator bound. Equation (2.2) would be weakened to ||Pn||^2 if the
same real representative theta_P were used at both roots. That quantity
can increase arbitrarily under n->n+Dk while the magnetic charge, energy,
and phase factor stay unchanged. Equations (2.1)-(2.2) avoid that error.
Changing the entire marked filling measure can change its frame norm;
no uniform statement over arbitrarily bad filling rules is intended.

## 3. A quantitative energy reserve for all finite component shapes

For this section use exactly the infinite-lattice component measures and
odd, signed-cubic averaged filling rules in prior campaign
BLOCK27_ALL_COMPONENT_MIXED_COEFFICIENT.md at commit
e3fc0b7707dce894ef98e7981a9feaf6041708f8. They include every translation,
finite connected closed integer component, and normalized filling mark.
The convention counts both signs with weight 1/2, hence counts an even
function of an unoriented component once. The actual orientation factor 2
is accounted for explicitly below.

The self-weights in these measures are

    w_e=exp[-g^2 E_e/2], w_m=exp[-b^2 E_m/2].

Give each root a reserve a_e=g^2 E_e/4 or a_m=b^2 E_m/4.
Weighting nu_e by exp(a_e), or nu_m by exp(a_m), leaves precisely the
half-self-weight measures nu_e^(1/2),nu_m^(1/2). Their frame norms are
bounded by the anchored second moments M_e^(1/2)(2),M_m^(1/2)(2).
Thus, for the actual factor 2 from orientations,

    2 integral |f(S,n)| exp(a_m(n)) nu_m(dn) <= a_e(S)
       if 4 b^2 M_m^(1/2)(2) <= 1,                     (3.1)
    2 integral |f(S,n)| exp(a_e(S)) nu_e(dS) <= a_m(n)
       if 4 g^2 M_e^(1/2)(2) <= 1.                     (3.2)

Both inequalities are uniform in the root's mass and filling area.
They also hold after restricting the measure to any finite subset.
They are weighted reproduction bounds for the even mixed bond. Calling
them a convergence proof for the actual full component gas would be wrong.

For completeness the previous anchored count gives, with C_A=1,562,500,

    M^(1/2)(2) <= (32 C_A/393) sum_(m>=1) m^8 z^m,
    z=393 exp(-t),
    t_e=g^2/64, t_m=b^2/64=pi^2 beta/16.                (3.3)

This uses ||fill||_1<=4m^2, at most 2*393^(m-1) connected signed
component encodings at an anchor, at most C_A m^4 possible anchors near
a fill through a specified plaquette, and E>=m/16. Closure can reduce
the count but is not needed for this upper bound. The finite free-boundary
filling count is different; (3.3) is not silently imported there.

An elementary fully explicit bound follows from m<=2^(m-1):

    sum_(m>=1) m^8 z^m <= z/(1-256 z),  if 256 z<1.

For either x=g^2 or x=b^2 with x>=2048 this implies

    4 x M^(1/2)(2)
       <= 128 C_A x exp(-x/64)/(1-100608 exp(-x/64))
       < 0.006.                                       (3.4)

The right-hand side decreases for x>=2048. For example beta=64,N=512
gives b^2>2048 and g^2=4096. These are fixed finite parameters. No
optimization or assertion about the complete model's phase window follows.

## 4. What the orientation average actually contains

For a finite set of electric and magnetic components, with signs sigma_i,
the mixed-only orientation factor is exactly

    2^(-V) sum_sigma prod_(ij mixed)
           [cos(theta_ij)+i sigma_i sigma_j sin(theta_ij)]
      = sum_(F subset mixed edges: every vertex has even degree)
           i^|F| prod_(ij in F) sin(theta_ij)
                 prod_(ij outside F) cos(theta_ij).    (4.1)

The product of cosines is only the empty F term. A bipartite four-cycle
contributes a product of four sines; it survives the orientation average.
The full clock representation also contains same-species factors
exp(-sigma_i sigma_j J_ij) and same-species support compatibility. Those
are absent from (4.1), whose purpose is to expose a specific missing term.

The linear sine term still carries a signed Hodge kernel. Switching its
representative changes the sine-minus-linear remainder by the contact
c<n,S>; one cannot use (1.1) to switch that remainder without recording
the contact. The two root bounds here control the even bond only.

## 5. Next decisive obligation

Retain the linear signed kernels and derive a summation bound for connected
orientation-even networks with the actual same-species energies and
compatibility. Closed cycles may be handled by operator traces, but general
networks and physical sources require a separate argument. In particular,
an operator inverse for a quadratic model is not the all-order remainder
estimate for this component gas. That remains the open target.

The finite check accompanying this note must use exact cochain projections,
gauge changes of integer fills, both rooted frame inequalities, a genuine
four-cycle orientation average, and the explicit reserve constant. Such a
check challenges algebra and normalization; it is not an infinite-volume
or independently reviewed proof.
