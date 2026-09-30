# Charge-preserving two-cut construction in the actual canonical sector

Conditional supplied-model mathematics. No physical state or Hamiltonian is
selected. This proof concerns the lowest eigenvalue in the FULL exact-N
subspace, not a selected pair channel, parity subspace, or momentum subspace.
It neither bounds a gap above an already degenerate ground space nor supplies
local density spectral weight. All operators below act on the full site tensor
product before any matrix element is restricted to charge N.

## Statement

Fix mu,tau>0 and use the actual H0=S+mu Ddiag+W of the landed density source.
On the cubic periodic lattice with V=L^3, let E_N be the canonical minimum.
For all sufficiently large L with N/L not an integer, either this minimum is
degenerate or its same-N first excitation gap obeys

    Delta_N <= C_h log(L)/L.                              (F1)

Constants depend on the fixed local law, not N or V. Other number sectors may
have lower energies, arbitrary degeneracies and zero gaps. There is no premise
that a chemical potential makes E_N a unique full-space ground. Conversely,
(F1) says nothing when N/L is an integer; a density limit alone does not settle
that finite arithmetic. Taking even L is not needed for this flux theorem.

The detailed U(1) two-cut argument in Hastings, cond-mat/0411094v2, is the
closest primary construction. It uses a restricted local dynamics to factor
a twist and compares a translated cut. We give a Gaussian-filter variant and
explicitly keep only the charge-sector spectral gap where a gap is used.
The survey2111.01854v1 Theorem3, as stated for a unique FULL ground, is not
applied as a black box to a non-tensor-product fixed-number Hilbert space.

## 1. Actual local inputs

Use the original grouping H0=sum_x h_x. Every h_x commutes with total N, has
support in the Manhattan radius-two ball centered at x (at most25 sites), and

    ||h_x|| <= h = 182mu+240tau.

The grouping is the literal onsite/attraction/triple/gradient grouping; it is
not required to be positive. Its terms remain number conserving separately.
Centers of two overlapping radius-two supports differ by distance at most4;
there are at most d=129 such centers. Onsite number has integer spectrum0,1.
H0 and N commute with each unit translation T. Tensor dimensions and all local
norms are bounded independently of volume. These statements are exact for the
full hard-core law, including both centers of every plane pair.

For a unique canonical ground psi, T psi=z psi, |z|=1, and
<psi,n_x psi>=rho=N/V. Set E=E_N and Delta=Delta_N>0.
Every spectral estimate below involves only a vector A psi with [A,N]=0.
Thus (H0-E) restricted to such a vector orthogonal to psi is >=Delta. No
inequality H0-E>=0 on other sectors is used.

## 2. Locality on the full carrier

For this bounded tensor interaction, repeated Duhamel expansion of the
commutator gives the interaction-path bound. A path of m overlapping terms
has norm cost (2h|t|)^m/m!, at most d^m continuations, and cannot join two
centers at distance r in fewer than r/4 steps, up to the initial overlapping
term. Using 1_{m>=ell}<=exp(m-ell) in that series gives, with a harmless
initial factor de,

 ||[alpha_t(A_x),h_y]||
 <=2de ||A_x|| h exp(v|t|-dist(x,y)/4),
 v=2edh.                                                   (F2)

Here A_x is supported inside the radius-two ball of x. One obtains the path
series by differentiating the commutator and removing the unitary evolution
of terms already supported at its first end; only successive overlapping
interaction supports remain. Dropping missing edges proves the same bound
for every restriction of H0 to a subset of its terms. Onsite gauge conjugation
preserves supports and norms, so (F2) also holds for every twisted or restricted
Hamiltonian below. The bound is deliberately loose; at t=0 its right side
also covers overlapping endpoints. Norm convergence is automatic on the finite
carrier. No spectral hypothesis enters this locality estimate.

## 3. Two separated cuts and their Gaussian filter

For L>=128 choose the first coordinate and a half-slab X consisting of
m=floor(L/2) consecutive planes. Let

 G=Q_X-rho|X| I, Q_X=sum_(x in X)n_x, R(theta)=exp(i theta G),
 H(theta)=R(theta)H0R(theta)*.

Only terms meeting either boundary of X change. Write its derivative as
A(theta)=A1(theta)+A2(theta), with the two sums assigned to the two cuts.
A term derivative costs at most50h, and at most five planes of centers meet
each cut. The safe total bound, also allowing a cut shifted by one site, is

    sum_x ||A_x(theta)|| <= A_*=1000h L^2.                 (F3)

All these operators commute with N. The centering gives <G>=0. H(theta) is
unitarily equivalent to H0 on every sector, and R(theta)psi has the same
sector gap Delta. A one-cut Hamiltonian need not remain gapped anywhere.

Choose a>0 and define the real odd integrable filter

 f_a(t)=(1/2)sgn(t) erfc(|t|/(2sqrt(a))),
 K_a(H,A)=integral_R f_a(t) exp(itH) A exp(-itH) dt.

It is Hermitian for Hermitian A, commutes with N when H,A do, and

 integral f_a(t) exp(i omega t)dt=i(1-exp(-a omega^2))/omega,
 ||f_a||_1=2sqrt(a/pi),
 integral_(|t|>t0)|f_a(t)|dt
             <=2sqrt(a/pi) exp(-t0^2/(4a)).                (F4)

The Fourier identity follows by one integration by parts on the sine
integral. The tail follows by integrating erfc, or its defining positive
Gaussian integral. At omega=0 use the continuous value0.

Put K(theta)=K_a(H(theta),A(theta)) and let W'=iK W, W(0)=I.
Since A=i[G,H], its matrix element from the canonical ground to a same-sector
state of energy E+omega is -i omega G_(j0). Hence

    (K(theta)-G) R(theta)psi
        =-exp[-a(H(theta)-E)^2] G R(theta)psi,
    ||(K(theta)-G)R(theta)psi|| <= V exp(-a Delta^2).       (F5)

The displayed equality is on that vector: its ground component vanishes by
<G>=0; all other charge-sector matrix elements vanish identically. Duhamel
comparison of the two unitary ODEs gives

    ||W(phi)psi-R(phi)psi||<=|phi| V exp(-a Delta^2).       (F6)

This is the only spectral-gap use. In particular the negative energies of
other sectors do not enter an imaginary-time integral or an operator norm.

## 4. Exact local twists and a norm factorization error

Around each cut retain Hamiltonian terms with centers within L/4-6 of that
cut, denoting the sums H1(theta),H2(theta). Adjust integer endpoints inward.
Their site supports are separated by a fixed buffer larger than4. Define
Kj(theta)=K_a(Hj(theta),Aj(theta)) and Wj'=iKj Wj, Wj(0)=I.
These are exact local, charge-preserving unitaries on disjoint slabs. Therefore
W1(phi) and W2(chi) commute for every phi,chi. The same is true after translating
the first slab by one site. Each original h_x commutes with at least one of
W1,W2, since its support has diameter at most4 and cannot bridge the buffer.

The first-cut derivative is a distance at least L/8 in center metric from
all terms removed in H1, and similarly for the second cut, for sufficiently
large L (increase the fixed threshold if rounding requires it). Set

 t0=L/[256(1+v)], B_*=2de h V A_*.

Duhamel comparison of real-time full and restricted evolutions, term by term,
uses (F2). For |t|<=t0, summing over removed centers and all local derivative
terms bounds the sum of both evolution differences by

                    B_* |t| exp(-L/64).

Indeed the distance exponent is at most -L/32, while v|t|<=L/256;
-L/64 is a weaker exponent. For longer times the trivial bound is2A_*.
Integrating against f_a and then comparing the unitary theta ODEs yields

 ||W1(phi)W2(phi)-W(phi)|| <= |phi| delta_loc,
 delta_loc=2sqrt(a/pi)[B_* t0 exp(-L/64)
                        +2 A_* exp(-t0^2/(4a))].          (F7)

No gap of H1 or H2 is invoked. Their use buys exact support and exact commuting
local factors; the approximation is priced by (F7), not asserted zero.

Let

 eta=2pi[V exp(-a Delta^2)+delta_loc].                     (F8)

Then at phi=2pi,

 ||W1 W2 psi-r psi||<=eta,
 r=exp(-i2pi rho|X|).                                    (F9)

The scalar r is retained: R(2pi) need not equal I with the centered charge.
Integer site charges imply precisely that it is a scalar.

## 5. Canonical energy and the translated-cut phase

Set psi1=W1(2pi)psi. It is normalized and has exactly N particles. For each
h_x, if it commutes with W1 its expectation is unchanged. Otherwise it commutes
with W2, so (F9) and the unit-vector expectation bound give an error at most
2h eta. Thus

       0<=<psi1,H0 psi1>-E <=2hV eta.                     (F10)

The left inequality uses the canonical variational minimum only.

Translate the first local twist by one plane: W1'=T W1 T*. Use the same second
cut. The gauge slab X' is X with that first plane removed (reversing the
translation orientation conjugates all phases and changes no conclusion).
Center its charge as G'=Q_X'-rho|X'|. Translation invariance of psi gives
<G'>=0. The entire derivation(F3)-(F9) applies to this shifted two-cut problem,
with the same safe constants. By translation covariance of the restricted
local Hamiltonian and filter its first local factor is exactly W1'. Therefore

 ||W1' W2 psi-r'psi||<=eta,
 r'=exp(-i2pi rho(|X|-L^2))=r exp(i2pi N/L).               (F11)

This is where centering and the one-plane charge enter. A mere assumption that
flux insertion preserves momentum would miss this phase.

Using Tpsi=zpsi and exact disjoint-support commutation with W2,

 <psi1,Tpsi1>/z = <psi,W1*W1'psi>
               = <W1W2psi,W1'W2psi>.

Equations(F9),(F11) imply

 |<psi1,Tpsi1>-z exp(i2pi N/L)|<=2eta.                     (F12)

The translation operator is tested on an actual same-N state of the original
homogeneous H0. No final external field remains.

## 6. Quantified contradiction and scope

Take a=t0/(2Delta). Both spectral and Gaussian exponents become

       a Delta^2=t0^2/(4a)=L Delta/[512(1+v)].

If Delta>=C0 logL/L, with C0=16384(1+v), then sqrt(a)<=L for large L and

 eta<=C'_h L^7 [exp(-L/64)+L^(-32)].                      (F13)

The constant C'_h is explicitly obtained from(F3),(F7),(F8); no volume-dependent
constant is suppressed. N/L noninteger implies

 d_N=|exp(i2piN/L)-1|>=2sin(pi/L)>=4/L.

Write p=|<psi,psi1>|^2. Because Tpsi=zpsi and T preserves psi's orthogonal
complement, |<psi1,Tpsi1>-z|<=2(1-p). Together with(F12),

              1-p >=(d_N-2eta)/2 >=1/L                  (F14)

for large L. The sector spectral theorem and(F10) give

             Delta<=2hV eta/(1-p)<=2h L^4 eta.

Equation(F13) contradicts Delta>=C0 logL/L for sufficiently large L. Increasing
the constant to cover the remaining finite sizes proves(F1). All constants
are uniform over the permitted integer N.

This is a canonical-sector adaptation of a known flux method, not a claim of
a new general LSM theorem. Its actual-model value is to remove the otherwise
unjustified unique-FULL-ground premise. It provides degeneracy or a low-lying
same-number eigenvalue on noncommensurate finite sequences. It does not choose
such a sequence from the EOS, remove a degenerate ground projection, prove
ODLRO/topological order, or force a local density operator to couple to the
low-energy eigenvector. That last matrix-element problem remains separate.
