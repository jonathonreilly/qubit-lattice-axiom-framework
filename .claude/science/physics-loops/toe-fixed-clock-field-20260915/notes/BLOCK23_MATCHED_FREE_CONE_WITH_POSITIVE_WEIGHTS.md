# Matching the free photon and Weyl cones with positive direction weights

Provisional personal derivation, 2026-09-16 UTC. This is a construction within
the already supplied weighted rotor family, not a selection theorem or an
interacting Lorentz-symmetry theorem. Blocks20--22 remain premises pending
independent review. The simple constitutive calculation below is self-contained.

## 1. The mismatch and the allowed change

Block22 kept unit electric and magnetic weights. Its photons therefore had
small-momentum metric I while the paired Wilson cones had

    G=diag(1,1,3/4).                                             (1)

The existing exact-Gauss Hamiltonian permits strictly positive electric link
weights and magnetic plaquette weights. Keep them constant by direction. Write

    W_E=diag(e1,e2,e3),    W_B=diag(b1,b2,b3),    ei,bi>0,          (2)

where bi weights the plaquette whose NORMAL direction is i. No electric--magnetic
cross term is introduced. The quadratic physical normal Hamiltonian is

    a H=(1/2)P^T W_E P+(1/2)(curl A)^T W_B(curl A),
    div P=0,               A modulo gradients and harmonics.     (3)

Equation (3) is the g->0 fixed-box normal operator of the full weighted rotor
Hamiltonian. It is not a replacement definition of the microscopic model.
The finite-dimensional charge connection, flat holonomy minimum and matter
Hamiltonian are as in Block21. Changing fixed positive gauge weights leaves
the zero set of the magnetic potential and the flat free matter energy
unchanged. It changes the normal zero-point energy and the slow electric metric.

## 2. An exact lattice criterion for equal photon polarizations

Use link and plaquette CENTERED Fourier phases. Curl is then i[s(k)]_cross,
where

    s_i(k)=2 sin(k_i/2).                                         (4)

The harmless link/plaquette phase transformations commute with the diagonal
direction weights. On the canonical variables A=W_E^(1/2)x,
P=W_E^(-1/2)p, the squared normal-frequency matrix is

    M(k)=W_E^(1/2)[s]_cross^T W_B[s]_cross W_E^(1/2).              (5)

Its kernel is W_E^(-1/2)s and its two positive eigenvalues are the physical
squared frequencies in units a^-2. This keeps the Gauss constraint; simply
restricting W_E to an unweighted two-plane before the canonical change would
give a different answer.

Within (2), the two nonzero frequencies agree for EVERY nonzero momentum iff

    W_E=c W_B,       c>0.                                        (6)

Necessity already follows along the three coordinate axes. For s along z,
the two eigenvalues are s_z^2 e1 b2 and s_z^2 e2 b1. The analogous x,y
equalities force e1/b1=e2/b2=e3/b3. This proves necessity for the continuous
Brillouin zone, or for any periodic cube with a nonzero mode on every axis.

For sufficiency set D=W_B and use the elementary three-dimensional identity

    D^(1/2)[s]_cross D^(1/2)
                   =sqrt(det D)[D^(-1/2)s]_cross.                (7)

It follows either component by component from the Levi-Civita symbol or from
the determinant transformation of a cross product. Then (5) becomes

    M(k)=c det(D) ( |D^(-1/2)s|^2 I
                          -(D^(-1/2)s)(D^(-1/2)s)^T ).          (8)

Both physical modes therefore have the EXACT lattice frequency

    a omega(k)=sqrt(s(k)^T G_ph s(k)),
    G_ph=c det(D) D^(-1).                                       (9)

The zero mode is still omitted from the transverse oscillator. Positivity of
the weights makes every nonzero-momentum frequency positive. Nothing in this
calculation addresses photon poles at nonzero coupling.

## 3. Matching any prescribed positive diagonal Weyl metric

Given a prescribed positive diagonal G and any eta>0, choose

    W_E=eta sqrt(det G) G^(-1),
    W_B=eta^(-1) sqrt(det G) G^(-1).                              (10)

Here c=eta^2. Substitution in (9) gives G_ph=G exactly. Conversely, (6) and
G_ph=G force (10), with the one positive parameter eta. Thus the six positive
diagonal weights obey five independent matching conditions once G is fixed.
The remaining parameter changes the electric/magnetic fluctuation normalization;
in the original rotor Hamiltonian it can also be absorbed by replacing
g with g sqrt(eta). It is not an extra prediction for a gauge coupling.

For (1), eta=1 gives the concrete allowed weights

    W_E=W_B=diag(sqrt(3)/2,sqrt(3)/2,2/sqrt(3)).                  (11)

The two photon polarizations then obey

    (a omega)^2=4 sin^2(kx/2)+4 sin^2(ky/2)+3 sin^2(kz/2).        (12)

All four Weyl cones of the paired Wilson example have the same leading
energy squared px^2+py^2+(3/4)pz^2 about their own nodes. Consequently the
photon and fermion LEADING small-momentum cones agree in the same microscopic
coordinates. Their full lattice dispersions are not equal. This construction
does not change the positions or number of Weyl nodes.

## 4. Compatibility with the observable limit and positive parent

Block21's fixed-box proof uses positive normal Hessians and a finite normal
gap; it does not require equal unit direction weights. The unique flat-matter
minimum and its positive Hessian from Block20 are unaffected by (10). Thus the
same proof applies at each sufficiently large fixed box. Its slow kinetic
metric is now W_E/L, as derived separately in the harmonic-metric review.

For clarity the weighted Gaussian covariances can be written before taking
volume to infinity. On the gauge quotient let

    M=W_E^(1/2) C^* W_B C W_E^(1/2),
    Omega=M^(1/2),    Omega^+=inverse on its positive subspace.   (13)

Here C is the actual link-to-plaquette curl and the link-space W_E has the
declared repeated directional entries. With all inverse square roots positive,

    <P P^T>=(1/2) W_E^(-1/2) Omega W_E^(-1/2),
    <B B^T>=(1/2) C W_E^(1/2) Omega^+ W_E^(1/2) C^*.              (14)

The same bounded electric/magnetic Weyl probes as Block22 have their Gaussian
limit with (14). The symbols are bounded and vanish continuously at k=0:
Omega is O(|s|), while the two curls in the magnetic expression cancel the
single O(|s|^-1) inverse. Fixed-support Riemann sums and fixed-time evolution
therefore converge exactly as in that block. Matter retains the same limiting
neutral Slater correlations. Limits remain g->0 FIRST, then L->infinity,
at fixed a and fixed physical probe times.

Strictly positive direction weights are also compatible with the earlier
positive cyclic-history construction: they multiply the positive single-link
electric rates and the real magnetic energies by positive constants. They do
not alter opposite-charge conjugation of the two fermion determinants. This
compatibility does NOT allow exchanging the fixed-g regulator limit of Block16
with the g->0 limit here, and does not supply a volume-uniform regulator size.

## 5. What the construction does and does not decide

The unit-weight cone mismatch is removable within the supplied Hamiltonian
family. It is not by itself a wall forcing a new framework axiom. Conversely,
positivity, Gauss law and the paired fermion construction allow all the unequal
weights as well. They do not select (10). One may impose it as a model choice,
or seek a dynamical mechanism which drives it; neither is derived here.

For example W_E=diag(1,2,3), W_B=I is fully positive but its z-directed
photon polarizations have squared frequencies k_z^2 and 2 k_z^2 at leading
order. Positivity and exact Gauss law alone do not imply a common optical cone.
This is a counterexample to that specific inference, not a counterexample to
all approved framework primitives or a claim that no selection mechanism exists.

At g>0, lattice corrections can renormalize the electric, magnetic and fermion
coefficients differently. Gauge Ward identities alone do not impose Lorentz
symmetry. A common free cone is therefore an appropriate starting comparator
for the phase problem, not its solution. No gravitational field, universal
matter coupling, axiom selection or empirical parameter value is obtained.

Context only: Favaro and Bergamin, [arXiv:1008.2343v4](https://arxiv.org/abs/1008.2343v4),
study a much broader constitutive classification. Only its abstract was consulted
here to check that this is established optical-metric territory. Their general
classification is not imported as a proof premise; (5)--(10) prove precisely
the restricted positive diagonal claim needed in this model.

The checker compares literal finite real-space weighted curls with (9), checks
the three axis necessity tests, and computes the Wilson metric by a separate
derivative of its Bloch vector. It is a finite algebra discriminator, not a
nonzero-coupling phase calculation.
