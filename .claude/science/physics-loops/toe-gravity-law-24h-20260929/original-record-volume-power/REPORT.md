# Full original-process power on a volume-independent early-time interval

Author proof candidate, September30. Not independently checked or formally
reviewed. Contract and exact current source identities are adjacent. This uses
the original supplied rotor model, both separately defined instrument choices,
and Omega from that contract. The complete GKSL ensemble is kept throughout.
K,delta,kappa>0 and evenL>=24. N=L^3/2. All constants below are deliberately
loose; no optimal time, physical calibration or thermodynamic semigroup is claimed.

## 1. Local algebra and a weighted-band lemma

On the all-A-occupied carrier each effective B_a,b,sigma and A_ac=-2delta*S_ac* S_ac
is a local tensor operator. The global P symbols in their definitions can be
replaced by projectors on the A sites touched by the word: all other A factors
are identities on this carrier. These local extensions commute at disjoint
supports; restricting their gauge-invariant words to the physical Gauss space
preserves that equality. No tensor factorization of the Gauss space is assumed.

An elementary outward hop changes one integer field by1. Therefore B has total
rotor displacement at most2, A_ac at most4, and B*B at most4, including all
charge/occupancy gates and coherent sums. The source bound ||F_a||<=6 gives
||A_ac||<=2592delta. This bound is intentionally weaker than possible improved
star bounds. There are18 distance-two A partners. Each resolved B has norm<=5;
there are12 per center. Each coherent B has norm<=10 and there are6. In both
cases the safe center bound is

    g0 = 600kappa >= sum_(marks at a) ||sqrt(kappa) B_m||^2.

For any finite link set S set Q=1+sum_(e in S)|E_e|. It counts masked as well as
unmasked links. It is a positive integer diagonal operator and commutes with
ALL electric terms D_e, even after births. If O changes Q by at most s then

    ||Q^u O Q^-u|| <= b_u(s)||O||,
    b_u(s)=(2s+1)(1+s)^u,  u>=0.                         (1)

For rigor take Fourier components O_d=(2pi)^-1 integral exp(-idt)
exp(itQ) O exp(-itQ) dt, |d|<=s, each norm<=||O||. On its input spectral
subspace, Q^u O_d Q^-u multiplies the output by ((q+d)/q)^u<= (1+s)^u.
The sum proves(1). Negative conjugation has the same bound by adjoint.
The proof holds with charge degeneracies and with product-box compressions.
It also applies to O Q^-v when this operator is bounded with the same bands.
No electric coercivity after formation is being assumed.

## 2. Uniform local moments for the actual generator

Temporarily compress every rotor link to |E_e|<=R in a PRODUCT box; use the
actual compressed jumps L_m,R and their loss L_m,R* L_m,R. The compressed
Hamiltonian is K D_R+sum A_ac,R. These are finite matrices on the finite
physical charge/field space; Omega is in every box. Locality survives this
product cutoff. Compressing a radial global ball would not give that fact.

For any fixed S and p>=0, conjugate the adjoint generator applied to Q^p by
Q^-p/2. The Hamiltonian contribution of a local bounded A has norm at most
2 b_(p/2)(4)||A||. The contribution of a jump has upper bound
[b_(p/2)(2)^2+b_(p/2)(4)]||L||^2. The gain is positive; the two loss products
are bounded separately. Terms whose field support misses S cancel exactly,
and K D commutes with Q^p. Thus as quadratic forms,

    L_R* Q^p <= C_p(S) Q^p,
    C_p(S)=2b_(p/2)(4) v_S
             +[b_(p/2)(2)^2+b_(p/2)(4)] g_S,             (2)
    Tr(Q^p rho_R(t)) <= exp(C_p(S)t).                    (3)

Here v_S bounds the sum of norms of magnetic pairs whose field support meets S,
and g_S bounds the sum of squared jump norms with such support. All compressed
norms and bands obey the same bounds, uniformlyR. Initial Q=1 exactly.

For the estimate below choose S_a to be all oriented edges whose B endpoint
has a representative in the cube a+[-9,9]^3. On a torus interpret the cube as
its image; any identifications only reduce the following overcounts. A star
using a link in S_a has center in a+[-10,10]^3. Therefore it is enough to use

    v_S=18*21^3*2592delta,
    g_S=21^3*600kappa,
    C8=11250 v_S+169650 g_S.                             (4)

The second number follows b_4(2)=405, b_4(4)=5625. Counting all sites in a
coordinate cube overcounts A sites and is harmless. S_a can be a large finite
local set; its size never scales withL. No large-torus first-event limit enters.

## 3. A local current and its continuity

Let L_m=sqrt(kappa)B_m. Define the original center current on a common weighted
core, and similarly in every box,

    P_a=sum_(m at a) [L_m* h L_m - {L_m*L_m,h}/2].        (5)

Only h terms meeting the root star survive (5). Electric terms are the36 edges
ending at its six B neighbors. For a magnetic term, one A center is the root
or one of its18 distance-two neighbors. At most19*18=342 unordered pairs
are therefore enough (overcounting pairs is intended). The remaining center
is at distance at most4, so the union of its stars is within the coordinate
cube of radius5. Set

    v0=342*2592delta,
    P0=g0*(316K+2v0).                                   (6)

All electric terms in that local sum have distinct links and satisfy
||D_U psi||<=2||Q^2 psi|| for Q=Q_(S_a). This follows from
sum(E_e^2+|E_e|)<=2(1+sum|E_e|)^2, retaining all occupancy masks.
The gain L* D_U L costs2K b_2(2)||L||^2=90K||L||^2.
The two losses cost K[1+b_2(4)]||L||^2=226K||L||^2.
The bounded magnetic gain and loss together cost2v0||L||^2. Consequently

    ||P_a psi|| <= P0 ||Q^2 psi||.                      (7)

P_a has Q bandwidth at most8 and vertex support within radius5, even though
it is unbounded in electric fields. All quantities also obey (7) in the
product boxes with the same constants.

Now apply the FULL adjoint generator to P_a, including later births. The
magnetic terms that can fail to commute with its support have a center in
cube radius6, the other within radius8, and stars within radius9. The jumps
have a center within radius6. All electric terms that can fail to commute
have B endpoint within radius6. Thus they all have their links in S_a, and
safe bounds are

    v1=18*13^3*2592delta,
    g1=13^3*600kappa.

For the electric commutator, ||D_near psi||<=2||Q^2 psi|| and(1),(7) give
||[K D_near,P_a]psi||<=2K[1+b_2(8)]P0||Q^4 psi||.
Here b_2(8)=1377. For the magnetic commutator the coefficient is
[1+b_2(4)]v1 P0=226v1 P0. For the dissipator it is
[b_2(2)+(1+b_2(4))/2]g1 P0=158g1 P0. Hence

    ||(L_R* P_a,R)psi|| <= Ccur ||Q^4 psi||,
    Ccur=P0*(2756K+226v1+158g1).                        (8)

For example the left electric product is bounded by applying(1) to the
bounded banded operator P_a Q^-2, not by pretending P_a is bounded. Remote
terms cancel before this estimate. The Hamiltonian diagonal used here is
the true occupied-B-masked D, never the prebirth sum E^2.

Cauchy and(3) withp8 imply

    |Tr(P_a,R rho_R(t))-Tr(P_a,R rho_R(0))|
       <= Ccur integral_0^t exp(C8 s/2) ds
       <= Ccur t exp(C8 t/2).                          (9)

These are finite-matrix identities followed by bounds uniform inR,L. The
large constants are explicit upper bounds, not fitted finite-volume values.

## 4. Removing the rotor cutoff at each volume

At each fixed finiteL use Q_all=1+sum_alllinks|E|. It commutes with K D,
including every charge/occupancy gate. Every bounded shift polynomial in
A or L or L*L is bounded in each Q_all graph norm by(1), with a finite
constant possibly depending onL. Product projections commute with Q_all;
the compressed polynomials and their adjoints converge strongly in every
weighted space on finite words, then on that space by the common bound.

For a direct process argument, unravel the finite marked GKSL generator.
Each jump increases the number of occupied B sites by2; at mostN/2 jumps
are possible. Expand each no-jump propagator in the interaction picture of
K D, with bounded perturbation A-i Gamma/2. Its weighted Dyson series is
dominated by the exponential of the finite weighted bound. This domination
also holds for the compressed actual Gamma_R=sum L_R*L_R. Termwise weighted
strong convergence and finite ordered jump integrals prove convergence of
all polynomial-field moments and the corresponding current expectations,
uniformly on each finite time interval at this fixedL. No uniform-inL cutoff
rate is asserted or needed. The Ω input has all moments. The argument also
proves their differentiability/integrated generator identities.

Thus(3),(7)–(9) pass to the full physical rotor ensemble. To pass the total
energy use |D|<=2Q_all^2 and boundedA, with a higher weighted moment in the
same argument. Alternatively first integrate its exact boxed generator
identity, then pass both endpoints and the integrable current terms. Trace
norm convergence alone would not justify this step. The order is: prove the
local estimates uniformlyL,R, removeR for eachL, and retain constants that
were independentL from the start. An infinite-volume dynamics construction
is unnecessary for the stated family of finite-volume inequalities.

## 5. Positive full-ensemble drift and supplier consequence

The landed first-wait source gives the exact INITIAL current

    <Omega,P_a Omega>=p0=123744 kappa delta.             (10)

This is its existing855-coefficient result, not new science claimed here.
Translation invariance makes all centers equal. For R>=8 every word needed
for(10) starting from E=0 lies within the box; the same equality holds there.
The independent first-birth reconstruction is recorded in the parent campaign.
The new ingredient is(9) for the full later-birth ensemble with constants
independent of volume.

Define the explicit positive time

    t0=min(1/C8, p0/(4 Ccur)).                          (11)

For0<=t<=t0, exp(C8t/2)<=exp(1/2)<2, so(9) gives
Tr(P_a rho_L(t))>=p0/2. The Hamiltonian contributes zero to the derivative
of its own mean. Summing the actual dissipator currents and integrating gives

    d/dt Tr(h rho_L(t)) >= 61872 kappa delta N,
    Tr(h rho_L(t))-<Omega,h Omega>
                         >=61872 kappa delta N t.       (12)

This includes arbitrary allowed later births, not just a surviving no-birth
sector. It is a small-time theorem for each evenL>=24 with one time valid
for allL. The bound is intentionally too conservative to identify a physical
laboratory time. The initial energy is negative and extensive; its increase
is not a contradiction with closed-system energy conservation.

For a SEPARATELY supplied autonomous completion Htot=h_sys+Hsup+V with
Hsup>=0 and conserved total mean, suppose the actual system energy gain
approximates the target gain with absolute error<=epsilon_E, and suppose
|Delta<V>|<=zeta on[0,t]. Then the exact ledger implies

    <Hsup>_initial >=61872 kappa delta N t-epsilon_E-zeta.

The supplier may be coherent or correlated with the system; this elementary
consequence needs only the stated conservation, lower bound and error ledger.
It is vacuous if endpoint interaction energy is allowed to cancel the gain
without control. It proves no work/heat identification, no universal physical
reservoir prohibition and no demand for an axiom update. The finite autonomous
supplier campaign construction is a surviving supplied-model escape, with
explicit large resources and endpoint interaction errors.

## 6. Check and scope state

No new numerical control or independent proof comparison has yet completed.
Planned exact controls: geometry overcounts and support containment; band
coefficients and current/moment constants; a finite noncommuting charge/rotor
fixture with actual gain AND loss, checking weighted form bounds and detecting
wrong compression of the loss. The algebraic proof, not finite samples, carries
all-volume quantifiers. The current physical-law/source/clock selection remains
open. This result would strengthen energy demand within an optional supplied
model, not establish current axiom inconsistency.
