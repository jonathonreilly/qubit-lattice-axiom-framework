# Specified dynamical gauge field and relative cone flow

Working derivation, not independent review. Expected one-loop comparator
coefficients were visible before this calculation. No physical photon phase
or native gauge law is inferred from continuum perturbation theory.

Use Euclidean action S=int[psibar(gamma0 D0+r gammai Di)psi+F^2/4]
with photon speed set to one at the scale under consideration, charge e,
and D=partial+i e A. Gamma0=gamma0 and Gammai=r gammai are the vertices.
Feynman gauge has photon propagator delta_mu_nu/k^2. The fermion inverse
is i(gamma0 p0+r gammai pi), and its propagator has numerator -i times
that slash over p0^2+r^2 p^2. There is one Dirac field from the two native
opposite Weyl cones. The Lorentz-symmetric comparator is r=1.

Clifford multiplication gives
sum_mu Gamma_mu gamma0 Gamma_mu=(1-3r^2)gamma0,
sum_mu Gamma_mu gammaj Gamma_mu=-(1+r^2)gammaj.
Feynman parameters in k^2[(p0-k0)^2+r^2(p-k)^2] give
A(x)=x+(1-x)r^2. After translation, the fermion numerator has weights
x p0 and x pj/A. The common radial logarithm is 1/(8pi^2) log(Lambda/mu).
Thus the two parameter integrals are
I0=int_0^1 x/A^(3/2)=2/(1+r)^2,
Is=int_0^1 x/A^(5/2)=2(2+r)/(3r(1+r)^2).

The inverse-fermion kinetic increments per logarithmic shell are
z0=-e^2(1-3r^2)I0/(8pi^2),
zs=+e^2(1+r^2)Is/(8pi^2).
Their common value at r=1 is a wave-function change, not a speed change.
Canonical time normalization gives
v_dot=r(zs-z0)
 =e^2/(6pi^2) (1-r)(4r^2+3r+1)/(1+r)^2.
These statements still require a fully checked sign/regularization argument.

A fermion loop is reduced by q_i -> r q_i. Its measure is r^-3 and
external gauge vertices are (1,r). The resulting photon electric and
magnetic quadratic increments should be
zE=e^2/(6pi^2 r), zB=e^2 r/(6pi^2).
Then c_dot=(zB-zE)/2, and the physical ratio obeys
r_dot=v_dot-r c_dot. A direct coefficient derivation and Ward check are
still required; a standard vacuum-polarization constant cannot simply be
copied from the target.

Restoring unit photon speed by tau=c t and A_tau=A0/c gives the common
gauge kinetic normalization sqrt(ZE ZB). Therefore a charge normalized
in this photon coordinate system obeys
(e^2)_dot=-(e^4/(12pi^2))(r+1/r).
This convention must be checked against the literature definitions;
it is not automatically the coupling called alpha there. At equality
it reduces to -e^4/(6pi^2), and the relative velocity eigenvalue is
-e^2/(2pi^2). The resulting near-equality suppression is logarithmic
with exponent three, not a constant-coupling power of momentum.


## General coframe derivative, independently of scalar speed formulas

Let E=I+C be a real symmetric positive Euclidean fermion coframe, photon
metric fixed at I, and Gamma_mu=gamma_a E_a_mu. For symmetric E,
sum_mu Gamma_mu (gamma.x) Gamma_mu
 =gamma.[(2 E^2-tr(E^2)I)x].
Feynman parameterization of k^2 (E(p-k))^2 gives
A(x)=x I+(1-x)E^2 and shifted numerator x E A^-1 p. Hence the coefficient
of i gamma_a p_b in the inverse-fermion correction, divided by e^2/(8pi^2), is

 M(E)=-int_0^1 dx x det(A)^(-1/2)
                   (2E^2-tr(E^2)I) E A^-1.

This exact logarithmic coefficient is valid for any fixed positive E under
the declared Euclidean Gaussian theory; it is not a native phase theorem.
Expanding E=I+C gives

 M(I+C)=I-(5/3)C+(2/3)tr(C)I+O(C^2)
        =E-(8/3) C_tf+O(C^2).

After wavefunction normalization, the traceless fermion coframe therefore
moves at -(e^2/(3pi^2)) C_tf per infrared logarithm. This coefficient has
also been derived by differentiating the propagator before angular averaging:
<n_a n_b>=delta_ab/4 and
<n_a n_b n_c n_d>=(delta_ab delta_cd+delta_ac delta_bd+delta_ad delta_bc)/24.
The two integration paths will be checked separately.

## Photon polarization coefficient from the determinant

The fermion determinant yields a bubble with trace
4[q_mu(q+p)_nu+q_nu(q+p)_mu-delta_mu_nu q.(q+p)].
After the Feynman shift, use dimensional integration by parts to retain its
transverse local coefficient: the l_mu l_nu and l^2 terms contribute an
additional delta_mu_nu x(1-x)p^2, equal to the explicit such term. The
result is 8 int_0^1 dx x(1-x) (p^2 delta_mu_nu-p_mu p_nu) I2.
Since int x(1-x)=1/6 and I2 has logarithm 1/(8pi^2), the coefficient is
e^2/(6pi^2). The four-component trace counts the two Weyl cones once.
A gauge-preserving regulator or the exact native Peierls seagull is needed;
naively retaining the quadratic bubble alone can create a spurious mass.

For E, replace p by E p, vertices by E and the integration measure by detE^-1.
The induced Maxwell density is proportional to
(1/4) detE^-1 (E^T E)_mu_rho (E^T E)_nu_sigma F_mu_nu F_rho_sigma.
At linear order its coframe part is C_tf. Thus a photon metric coframe
C_g receives +(e^2/(6pi^2))(C_f-C_g), after its common normalization.
Combined with the fermion result, relative metric R=C_f-C_g obeys
R_dot=-(e^2/(2pi^2))R. The weighted common coframe C_f+2 C_g is stationary
to this linear order. This is derived for the supplied coupled action,
not postulated as a positive exchange matrix.

## A different photon anisotropy sector

It is useful to restrict to real parity-even spatial media, without time
mixing. Write L_gauge=(1/2) Efield^T epsilon Efield
 +(1/2) Bfield^T b Bfield in Euclidean signature, with epsilon,b symmetric.
Near identity, write epsilon=I+a and b=I+d. A pure metric coframe C_g
has a=2C_g-tr(C_g)I and d=-2C_g+tr(C_g)I, plus a common scalar wavefunction
factor. The remaining five traceless components

 W=((a+d)/2)_tf

are birefringent. For example W=diag(w,-w,0) gives photon squared speeds
(1-w)/(1+w) and (1+w)/(1-w) along the third axis. Positivity holds for
|w|<1, so this is an allowed perturbation of the Gaussian model.

The W contribution to the photon inverse kernel obeys K(n)n=0,
tr K(n)=0 and <K(n)>=0 on the four-sphere of loop directions. In a flat
Feynman gauge its propagator insertion is -K/k^4. Clifford contraction
reduces the linear fermion self-energy contribution to 2<K_jnu> gamma_nu,
which vanishes. Thus W does not feed the fermion metric in the universal
one-loop logarithm at this order. The fermion bubble supplies only the
metric sector at linear order; photon wavefunction normalization gives

 W_dot=-(e^2/(6pi^2)) W.

This slower sector is absent from an assumed scalar two-speed exchange
matrix. It need not be present when exact additional spatial symmetries
forbid it. Its finite matching value in the actual native regulator is
still uncomputed; the native two-node Wilson symbol is not fully cubic.

At equality the same photon normalization yields
(e^2)_dot=-e^4/(6pi^2). Let L=log(mu0/mu). To one-loop and linear in the
anisotropies,

 e^2(L)=e0^2/[1+e0^2 L/(6pi^2)],
 R(L)=R0/[1+e0^2 L/(6pi^2)]^3,
 W(L)=W0/[1+e0^2 L/(6pi^2)].

These are logarithmic suppression laws in a massless perturbative model.
They are not a nonperturbative phase theorem, a bound at physical couplings,
or a claim that all native marginal matching terms were calculated.


## Metric-only photon kinetics are not closed for a finite relative shear

A single Maxwell metric with V=diag(1+s,1-s,1) is nonbirefringent exactly:
epsilon_f=V^2/detV and b_f=detV V^-2. Add its fermion-loop contribution
with small positive weight u to an initially flat photon:
epsilon=I+u epsilon_f, b=I+u b_f. Along the first axis the two squared speeds
are (1+u b_f,zz)/(1+u epsilon_f,yy) and
(1+u b_f,yy)/(1+u epsilon_f,zz). Their difference to first order in u is

 -u s^2(4-s^2)/(1-s^2),

which is nonzero for 0<|s|<1. This is a direct wave-equation discriminator,
not just a parametrization count. Both quadratic forms remain positive.
Thus a sum of the two different metric Maxwell kernels is generally
birefringent, despite gauge invariance. The scalar two-speed family is a
special closed symmetry class; the general relative shear is different.

For a small symmetric spatial relative coframe R, expanding the induced
Maxwell density at fixed flat photon metric gives the traceless tangent
source 2(R^2-tr(R)R)_tf. This is not a definition of exact birefringence
away from the identity: a single finite metric has such second-order terms
in its coordinates too. It is the component of an infinitesimal loop
increment outside the tangent to the photon metric family at the identity.
The direct squared-speed difference above establishes its physical content.

At second order in a trace-free initial shear S0, with initial W0=0,
the one-loop perturbation expansion of the RG equations gives

 R=S0/z^3+O(S0^2), z=1+e0^2 L/(6pi^2),
 W_dot=-e^2 W/(6pi^2)+2e^2 (R^2)_tf/(6pi^2)+O(S0^3),
 W=(2/5)(S0^2)_tf (z^-1-z^-6)+O(S0^3).

The formula follows by differentiating zW and integrating z^-6.
It shows how a shear that is itself attracted toward the photon metric
can generate a slower-decaying birefringent coefficient in this specified
one-loop expansion. It is not an all-orders uniform asymptotic theorem;
finite native matching and higher-loop effects are separate obligations.


## Native Peierls completion and the logarithmic matching argument

The dynamical gauge field in this test is a supplied noncompact Gaussian
link field. It is not yet encoded as an autonomous finite-qubit photon.
No short-range GMP theorem applies to its long-range exchange. Its cell
coordinates are y=D^-1 a n and its positive gauge dispersion is
omega^2+sum_i [2 D_ii sin(k_i/2)/a]^2, with D=diag(1,1,sqrt(1-zeta^2)).
It has only the photon zero at k=0. The matter is r h0/a at two nodes,
with a declared tuning of any allowed node-position counterterm. A positive
massless phase and the validity of perturbative expansion are inputs.

For the basic Wilson symbol, T_i=-sigma3/2-i sigma_i/2 for i=1,2,
T_3=-sigma3/2 and the onsite term is (2+zeta)sigma3. Peierls multiplication
of each oriented hopping by exp(i e a A_i/D_ii) gives the exact centered
one-photon spatial vertex (with e removed)
Gamma_i(k)=r/D_ii partial_i h0(k).
For dimensionless transfer q the finite Ward identity is
sum_i [2 D_ii sin(q_i/2)/a] Gamma_i(k)
 =r[h0(k+q/2)-h0(k-q/2)]/a.
The temporal vertex in the Hamiltonian Euclidean convention is iI.
The required second derivative is r a partial_i^2 h0/D_ii^2. Dropping it
would change the regulated gauge model and can leave a false photon mass
or finite marginal matching term. This contact has no leading infrared
logarithm. Longer fixed paths give the same endpoint gauge identity and
node vertex; their additional field strengths have derivative suppression.

A common small spatial coframe C is available through finite Laurent
matter sources. In units of h0, add sum_aj C_aj D_jj sigma_a V_aj(k), where
V_aj=sin k_j for a<3,j<3;
V_a3=(zeta-cos k3)sin k3/v^2 for a<3;
V_3j=sin k3 sin k_j/v for j<3;
V_33=(zeta-cos k3)/v.
All V vanish at the nodes, and their derivatives give the same coframe in
both opposite chiralities after the relative sigma3 basis change. These
finite sources do not themselves supply a gauge field or a source law.
Small coframes preserve the two nodes in a sufficiently small neighborhood;
no claim is made for arbitrary large deformations.

For a fixed nonmerging node pair, choose a small radius delta around each
fermion node and the photon zero. In canonically normalized y coordinates,
h_lat(q)=r alpha.q+O(a|q|^2), current vertices are their constant cone values
plus O(a|q|), and the photon denominator is q^2+O(a^2|q|^4). On an annulus
mu<|q|<delta/a, uniform positive denominators bound the difference of each
logarithmically divergent differentiated integrand by a power-integrable
O(a|q|) relative error. The remainder of the Brillouin zone has no common
massless denominator and is analytic in sufficiently small external momentum.
Photon transfer near 2kappa can reach the other fermion node, but the photon
there is gapped in this regulator, so it supplies no additional logarithm.
Continuous frequency tails are integrable after the stated derivatives.

Hence the coefficient of the infrared logarithm is the continuum one above.
The hard region and the Peierls tadpoles supply finite local matching terms;
they have not been computed or set to zero. Gauge invariance constrains
those terms but does not force all their metric or birefringent coefficients
to vanish. The native Wilson regulator is not fully cubic after selecting
its two-node axis. A chosen scalar matching class is an extra restriction.

The direct native shell challenge evaluates differentiated matrix products
with actual h0, link vertices and second derivatives, at both nodes. For
the self-energy it includes derivatives of the two vertices. For the photon
bubble it uses the full fermion propagator, with its time and transverse
spatial second derivatives. The continuum limits of the normalized radial
shell coefficients are z0 and zs above, and 4/(3r),4r/3 for the electric and
magnetic coefficients before multiplication by 1/(8pi^2). The two Weyl
nodes are summed once for the photon loop. Finite shell errors should be
O(radius^2): the normalized integrands extend analytically to radius zero,
and the symmetric sphere average removes odd powers. Numerical shell data
challenge that proof but do not replace its uniform remainder hypotheses.


## Exact escape class for the two-metric photon mixture

The birefringence result is generic, not universal. For positive symmetric
V and positive loop weight u, epsilon_f=V^2/detV and b_f=epsilon_f^-1
commute. The full mixture satisfies

epsilon b=(1+u^2)I+u(epsilon_f+epsilon_f^-1).

In their shared eigenbasis, equal polarization speeds on all three axes
require epsilon_i b_i equal for all i; this is also sufficient, since
b=Z^2 epsilon^-1 reconstructs a single positive Maxwell metric. Therefore
the mixture is nonbirefringent exactly when every eigenvalue x_i of
epsilon_f has the same x_i+1/x_i. Each x_i must then be either x or 1/x.
Using x_i=v_i^2/(v1 v2 v3) shows that the allowed positive V are precisely
(i) V=vI, or (ii) V has two eigenvalues one and a single arbitrary positive
eigenvalue. The latter is an arbitrary rotated rank-one coframe change.
Both classes are exact escapes. A general traceless spatial shear has
neither form unless it vanishes, so the concrete trace-free discriminator
stands. This classification must accompany any public negative framing.

At small R, the source 2(R^2-tr(R)R)_tf vanishes for a pure scalar or a
rank-one change. For trace-free real symmetric S in three dimensions,
(S^2)_tf=0 would require all three eigenvalues to have equal magnitudes;
their sum can vanish only if all are zero. Thus every nonzero trace-free
shear has the second-order source, within the stated perturbation expansion.


## Independent accumulated-Maxwell check of the quadratic memory

For trace-free S0, the linear solution in the original fixed coordinates is
Cf=f(z)S0, f(z)=(1+2z^-3)/3, and Cg=(1-z^-3)S0/3. The unnormalized photon
quadratic kernel starts at I and accumulates the matter Maxwell kernel with
weight dz. Dividing by the common coefficient z, define averages
m1=z^-1 int_1^z f(t)dt and m2=z^-1 int_1^z f(t)^2dt.
To second order, epsilon b has traceless part 4(m2-m1^2)(S0^2)_tf.
This removes the second-order curvature of the common metric family.
The actual transverse birefringent coefficient is therefore
2(m2-m1^2)(S0^2)_tf. Direct integration gives
m1=(1-z^-3)/3 and 2(m2-m1^2)=(2/5)(z^-1-z^-6), matching the moving-frame
ODE derivation. Unknown second-order coframe corrections enter with opposite
signs in epsilon and b and cancel from this product at this order.

A separate finite 3^3-cell Peierls calculation builds H(theta), H'(0), H''(0)
from link hoppings, without constructing a target by unitary conjugation.
For three seeded site gauge functions, Tr(P H'') and the occupied/empty-band
bubble are nonzero (roughly 14.7 to 42.3) and cancel within 1.5e-14.
The directly rebuilt gauge-transformed spectra agree within 6.1e-15.
This checks a pure-gauge static curvature and the contact factor. It does
not compute physical transverse finite matching constants.

The native fermion self-energy shell includes its two-photon tadpole as well
as exchange. An earlier exchange-only exploration was successful for the
log limit but incomplete at finite radius; its bytes are preserved separately.
The tadpole changes the finite shell error by O(radius^2) and leaves the
logarithmic coefficient unchanged. This is an author correction, not an
independent review. The extended primary now also checks exact scalar and
rank-one escape polarizations and the nine common native coframe node jets.
