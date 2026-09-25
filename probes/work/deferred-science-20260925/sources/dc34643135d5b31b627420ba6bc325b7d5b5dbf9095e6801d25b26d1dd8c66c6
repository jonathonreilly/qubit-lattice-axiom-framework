# Actual energy power of one original mark on the charged probe

Personal root derivation, 2026-09-24. Conditional author candidate, not yet
independently reconstructed. The question is whether the original selected
formation mark has an energy response that can be called photon absorption.
We calculate its actual contribution to the full effective energy derivative.
No new detector, reservoir, axiom or empirical identification is supplied.

## 1. Observable and premises

Use the same supplied common matter/field generator and the exact preparation
J_- of PR9143. On an even cubic torus L>=16, all A sites are plus except
d=(1,1,0),h=(2,2,0) minus. Three B plus blockers occupy (0,-1,0),(0,0,1),
(0,0,-1); a fourth is at c=(1,0,0) or e=(0,1,0). The two arms have the
common fixed integer flow V_com and respective U_dc^-1,U_de^-1 factors,
with amplitudes +1/sqrt(2),-1/sqrt(2). Let a=(0,0,0), b=(-1,0,0), and
select either original mark B=B_(a,b,sigma)=P j_(a,b,sigma) F_a P.

The full Hamiltonian in frequency units is

    h_g = K D + delta H4, K=g^2/(2 tau), delta=1/(4 tau g^2),
    D = sum_(x in A,y~x) 1_(q_y=0) E_xy(E_xy-q_x),
    H4 = -2 sum_(x<z, overlapping) S_xz* S_xz,
    S_xz = F_z F_x P.

All matter sectors and the EMPTY-B electric projector are retained. For a
normalized input psi in the domain of D define this single channel's power

    P_j(psi)=kappa [<B psi,h_g B psi>
                             - Re <B psi,B h_g psi>].             (1)

This is the adjoint dissipator expectation, including the anticommutator.
The Hamiltonian part contributes zero to the derivative of its own energy.
Other channels contribute their own terms; (1) is not the total flux. It is
not a conditional output mean minus an unconditional input mean, energy per
record, heat, work, or an implemented microscopic reservoir-energy balance.
Smooth compact packets and finite Wilson shifts preserve the electric
operator domain, so both terms in (1) are defined at every fixed g>0.

Let phi_0,g and phi_1,g be the parent's normalized compact transverse vacuum
and one-excitation packets, with fixed finite graph and normalized coefficients
alpha. Write psi_n,g=J_- phi_n,g. Let x=A_transverse/g, Omega_r=sqrt(lambda_r),
and real orthonormal transverse modes f_r. For any contractible circulation z,

    d_zr=(z.f_r)/sqrt(2 Omega_r), chi_z=sum_r alpha_r d_zr,
    v_p=sum_r d_pr^2 >=1/sqrt(3).

Harmonic angles have their required Haar distribution. They are not set to
zero. Contractible circulation observables ignore them; fixed common flow
shifts contribute only bounded constants to electric derivatives.

## 2. Exact magnetic compression with the anticommutator

Suppress V_com, which commutes with every magnetic angle multiplication.
Use the unnormalized two-arm vector v, with integer Laurent amplitudes +1,-1.
Set M=B*B. The magnetic part of (1), divided by kappa delta, is multiplication
by the exact real Laurent polynomial

    C(A)=sum_(x<z) [-||S_xz B v||^2
                                 + Re <S_xz M v,S_xz v>].         (2)

The preparation's factor1/2 and H4's factor-2 cancel. In the second term use
<B v,B H4 v>=<M v,H4 v> before substituting the pair form. Distinct final
matter configurations are orthogonal; only their equal-output amplitudes
interfere. The finite control implements outward charge-q hops with exponent
-q, original creation with exponent sigma, its actual adjoint with -sigma,
then inward charge-q hops with +q. It includes the full B*B action on v.

If the support of S_xz is disjoint from the star of a, S_xz commutes with B
and B*. Its two contributions cancel exactly. The 264 potentially contributing
pairs have centers with unfolded coordinates in [-4,4]^3 and neighborhoods
in [-5,5]^3. These embed without collisions for every L>=16. Thus the side16
enumeration gives the same local polynomial on all stated tori; it does not
approximate a sum of remote terms. The common preparation's endpoints also
lie in this patch. Its common flow cancels from (2) regardless of its routing.

The two signs give the same polynomial. Its 303 terms have constant 2794,
coefficient sum 0 and absolute coefficient sum 6700. All nonzero words are
divergence-free, conjugate-paired, and have length at most 10 (the retained
certificate actually has maximum 8). Since10<L, none winds around the torus.
Every word is preserved by the harmonic Haar average.

Let c_p be the positively oriented xy plaquette row at the origin. The exact
Hessian H=-sum_z C_z z z^T has 520 nonzero entries and c_p^T H c_p=49600.
It factors over integers as

    H=c_p t^T+t c_p^T,
    C(A)=(c_p.A)(t.A)+O(|A|^4).                              (3)

The 67-edge circulation t is recorded in POWER_SPECTRAL_RESULTS.json. All
entries of the matrix identity are checked with Fraction arithmetic. The
factor is recovered without a numerical fit: H c_p/4 minus
c_p(c_p^T H c_p)/32 equals t since ||c_p||^2=4. Its divergence is exactly zero.
Conjugate pairing removes odd powers. C(0)=0 is also consistent with Bv=0
when the original plaquette phase vanishes; the factorization is verified
directly, not inferred from that consistency observation alone.

## 3. Electric contribution and the power limit

The exact selected output is a fixed charge/flow factor times
(W_p-1) phi_n,g/sqrt(2), up to an irrelevant sign and unitary Wilson factor.
Consequently ||B psi_n,g||=O(g), and every first electric derivative of that
vector is O(1): differentiating W_p-1 costs O(1), while differentiating the
packet costs O(g^-1) multiplied by an O(g) factor. Fixed flow derivatives
are bounded. The actual D is a finite sum of quadratic and linear derivatives
with matter-diagonal bounded coefficients, including its occupancy gates.
Thus

    |<B psi,D B psi>|=O(1), ||D psi||=O(g^-2),
    |<B psi,B D psi>| <= ||B psi|| ||B|| ||D psi||=O(g^-1).

Multiplication by K=g^2/(2 tau) makes their contribution to (1) tend to
zero. This argument needs no false replacement of D by sum E^2 after
formation. It establishes O(g) as a sufficient bound; it does not assert a
sharp correction order. Constants depend on the fixed graph and packet.

The finite Laurent expansion, compact Gaussian moment bounds and exponentially
small cutoff errors now give

    lim_(g->0) P_j(psi_0,g) = kappa/(4 tau) C_pt,
    lim_(g->0) [P_j(psi_1,g)-P_j(psi_0,g)]
                         = kappa/(2 tau) Re(conj(chi_p) chi_t),  (4)
    C_pt=sum_r d_pr d_tr.

Here C_pt is the vacuum covariance of c_p.x and t.x. The one-excitation
covariance increment is 2 Re(conj(chi_p) chi_t). This is an instantaneous
effective-generator limit of the supplied input states. It is not a result
for a finite laboratory interval or a microscopic initial derivative, and
it does not discard the full dynamics between subsequent marks.

## 4. A positive baseline proved without a floating sign

The retained exact plaquette certificate is

    t=1550 c_p + sum_q b_q c_q, sum_q |b_q|=646.             (5)

All 32 nonzero integer coefficients and their elementary plaquettes are
listed in POWER_POSITIVE_CERTIFICATE.json. A numerical linear program found
a candidate filling; rational recomposition verifies every one of 525 link
equalities exactly. No optimizer tolerance or optimality conclusion is used
as a proof premise. Translation and cubic symmetry give ||d_q||=sqrt(v_p)
for every elementary plaquette. Cauchy and the triangle inequality therefore
prove

    904 v_p <= C_pt <=2196 v_p.

In particular the selected channel already has strictly positive limiting
energy power on the REFERENCE vacuum charged preparation:

    lim P_j(psi_0,g) >= (226/sqrt(3)) kappa/tau >0            (6)

for kappa>0. This vacuum is not the full charged ground state. Equation(6)
does not measure creation of energy in an isolated closed system: the given
open generator has no derived energy-conserving reservoir completion here.
It shows why treating every selected original mark as absorption of an
incident positive-energy photon is not established by the count formula.

For the unrestricted bright packet alpha=d_p/sqrt(v_p), the excess in (4)
is twice this vacuum contribution and the full one-excitation power limit
is three times it. This is a property of the supplied state, not a detector
quantum efficiency or photon absorption rate. The distinct earlier root29
candidate concerning INPUT mean-energy increments is not used to prove (4).

## 5. Low-band response and the observational limitation

If alpha is supported in 0<Omega<=epsilon<=2, the local Fourier estimate is
v_p,epsilon<=27 epsilon^4/128. It follows by enclosing the centered integer
momenta in a cube: nonempty band implies L epsilon>=4, at most
27 L^3 epsilon^3/64 momenta contribute, each with plaquette weight at most
epsilon/(2 L^3). The two transverse polarizations are already included.
Every elementary plaquette has the same restricted norm. Equations(4),(5)
then imply

    |lim(P_j(psi_1,g)-P_j(psi_0,g))|
          <= kappa/(4 tau) (2196*27/64) epsilon^4,
    |lim(P_j(psi_1,g)-P_j(psi_0,g))|/lim P_j(psi_0,g)
          <= (2196/904)(27 sqrt(3)/64) epsilon^4.             (7)

These are bounds on the limits at fixed graph. A hard band is a stronger
premise than a mean energy ceiling. Nothing here bounds arbitrary rare
high-energy tails by epsilon^4, makes the band invariant under the full
charged dynamics, or supplies a physical finite-g error at tiny optical
scales. The fractional power response and the count response are different
observables; neither is automatically the measured efficiency of an APD.

## 6. Evidence and surviving scope

The root personally wrote the new B/B* pair-form calculation, reviewed its
complete code, exact normalization, support cancellation and all covariance
arguments. Laurent/preparation geometry is explicitly reused from the prior
author controls, not presented as an independent implementation. The Hessian,
integer filling and all eighteen finite Fourier rows were inspected. The
retained side16/32/64 vacuum covariance values are approximately 1245.3524,
1245.3667,1245.3676; these are floating controls, while (6) supplies the sign.
All three programs completed successfully; their actual logs/receipts remain.
The earlier spectral output says the electric proof was pending at execution;
section3 supplies that argument later without rewriting the old output.

N1: native bound matter, collective energy-selective responses, other inputs
and reservoir completions remain open. N2: this single-channel instantaneous
power, input-energy increments, broad energy spread and short-window counts
are separate results. N3: supplied state/law, fixed graph before g->0, exact
occupancy gates and harmonic Haar fiber are explicit. N4: all terms in the
selected adjoint dissipator are kept; the full all-channel ledger is not
computed. N5: no framework no-go or empirical exclusion follows. N6: (7)
retains a quantitative low-band statement while exposing the positive
baseline. N7: actual photon absorption requires a physical source, matter
identification and calibrated count/energy dynamics. N8: earlier output
mean-minus-input estimates do not substitute for (1). Independent checking
is still required before publication promotion. No audit verdict is applied.
