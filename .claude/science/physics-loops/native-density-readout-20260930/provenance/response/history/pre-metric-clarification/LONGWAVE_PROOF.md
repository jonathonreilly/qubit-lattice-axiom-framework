# A homogeneous long-wave density sum-rule theorem

Author discovery candidate, to receive a separate focused check. This is a
new extension of CONTRACT.md's secondary target, not an implication of the
on-site result. The actual H0=S+mu D+W, actual M2 factors, and supplied
mu,tau>0 remain unchanged. No EOS or ODLRO enters the proof.

## L1. Spectral statement and constants

Take L>=25, V=L³, Hnu=H0-nu N, and any ground density matrix Gamma. Set
rho=<N>/V, e=<H0>/V<=nu rho. For a nonzero reciprocal vector q chosen in
[-pi,pi]^3 let A_q=sum_x exp(iq.x)n_x. Use the FULL ground projection P0,
Q=1-P0, and the positive measure

 sigma_q(domega)=(1/2V) Tr Gamma[
 A_-q Q dP_(Hnu-E0)(omega) Q A_q
 +A_q Q dP_(Hnu-E0)(omega) Q A_-q], omega>0.

Write m_j(q)=integral omega^j sigma_q. Translation averaging Gamma gives a
homogeneous state and does not change the bounds. The probe is the Fourier
transform of the actual local n_x, not total N or a pair-density proxy.
At q=0 the measure is identically zero.

Here are deliberately large, explicit constants, independent of L,nu,q:

 a=min(tau,mu/12), a2=min(tau,mu/6), b=3mu+24tau,
 h=182mu+240tau, c_h=pi²/(4a2),
 C_Q=2tau+mu²/(6tau),
 C_H=(C_Q/(2mu))*(1+(9b/2)*c_h)+162b*c_h,
 C_1=tau/(2mu)+C_H,
 q_*²=tau/(182b), nu_*=tau/(4C_1),
 v10=21³=9261,
 C_10=v10/mu+7200*v10²/a,
 C_rem=20000*33282*(1+9*v10)*h³*C_10,
 C_E=4000*b³*c_h+C_rem, C_N=36000*b³.

For 0<nu<=nu_* and 0<|q|²<=q_*², the claims are

 m1(q)>=(tau/4)rho |q|²,
 m3(q)<=|q|²(C_E e+C_N |q|²rho)
       <=rho |q|²(C_E nu+C_N |q|²).                    (L1)

Consequently, with

 Omega(nu,q)=sqrt[(8/tau)(C_E nu+C_N |q|²)],

 integral_(0,Omega] omega sigma_q(domega)>=(tau/8)rho|q|²,
 sigma_q((0,Omega]) >=tau rho|q|²/(8Omega),
 integral_(0,Omega] omega^-1 sigma_q(domega)
                         >=tau rho|q|²/(8Omega²).       (L2)

Only the first and third moments carry the proof. Zero-energy ground mixing
is never counted. For ANY sequences of admissible volumes, nu->0 and
nonzero q->0, Omega->0 and the energy-weighted response divided by rho|q|²
has the stated positive lower bound. At fixed positive nu this does NOT give
a gapless limit as q->0, nor sound, dispersion, a pole, condensate, or ODLRO.
The constants are not empirical calibrations. Absolute weight vanishes in
a dilute sequence; the normalization and lower bound are part of the claim.

## L2. Actual physical-edge matrix in a pair-center frame

For each unique physical edge B_e=b_x b_y, use three axial types with
endpoints c+/-e_i and six diagonal types d=e_i+eta e_j with midpoint c.
Fourier phases are exp(ik.c). Half-integral diagonal midpoints are a unitary
change of phase from integer anchors, not a new lattice site or carrier.
The actual N2 graph-edge matrix h2(k), here abbreviated h(k), is block
real and even in k. Its axial block is

 h_E(k)=2mu Q_E+tau ell(k)P_E,
 P_E=I-11*/3, Q_E=11*/3, ell=2sum_i(1-cos k_i).

For plane ij its two-entry vector and block are

 v(k)=(-cos((k_i-k_j)/2), +cos((k_i+k_j)/2)),
 h_ij(k)=2mu I+[tau ell(k)-mu]v(k)v(k)*.                 (L3)

This follows by expanding the same S/W rows. Each plane edge has two
centers; no Gram division is performed. Its low eigenvalue is
mu(2-s)+tau ell s, s=1+cos k_i cos k_j in[0,2]; its other eigenvalue is2mu.
The two axial low eigenvalues are tau ell and the axial high one is2mu.
Thus h(0)=2mu Q0 for a rank-four projection, P0pair=I-Q0 has rank five, and

 h(k)>=a2 ell(k)I,  |k|²I<=c_h h(k) for k in[-pi,pi]^3. (L4)

The symbol P0pair must not be confused with the full many-body ground
projection P0 used in the spectral measure.

All real-space K coefficients have pair-center displacement with l1 norm
at most3: within one star the two midpoints differ by at most2, and a W
row adds one center step. The absolute row sum bound b therefore gives

 ||h(k)||<=b, ||D²h(k)[u,v]||<=9b|u||v|,
 ||D^4h(k)[u,v,w,z]||<=81b|u||v||w||z|.                (L5)

One applies Schur's bound after multiplying each literal hopping coefficient
by its displacement factors. Global inversion makes D h(0)=D³h(0)=0.
These estimates are valid for all real k, including k+q outside the chosen
Brillouin representatives. This avoids any smooth eigenvector gauge.

For a general physical state define the positive pair density matrix by
G_ef=<B_f*B_e>. Then <sum M_ef B_e*B_f>=Tr(MG), Tr G=<P>, and
Tr(hG)=<Hpair>. For translation-invariant M only the diagonal momentum
blocks of G enter, even if the physical state was not translation invariant.
This is a positive reduced correlation matrix, not a free-particle
identification of the many-body state.

## L3. A lower first moment at the actual homogeneous point

On edge type d, A_q maps momentum k to k+q with
F_q(d)=2cos(q.d/2), a real diagonal matrix. Let F=F_q. Its norm is<=2 and
||F-2I||<=|q|² since every edge has Euclidean length<=2. The exact density
commutator, before any Fourier transform, is

 (1/2)[A_-q,[H0,A_q]]
   =-(1/2)sum_ef K_ef |w_e(q)-w_f(q)|² B_e*B_f,
 w_e(q)=exp(iq.x)+exp(iq.y).                             (L6)

Equivalently its pair symbol is

 M_q(k)=(1/2)F[h(k+q)+h(k-q)]F-(1/2){h(k),F²}
       =F Delta_q h(k) F-(1/2)[F,[F,h(k)]],
 Delta_q h(k)=(h(k+q)+h(k-q))/2-h(k).                   (L7)

The moment m1 equals Tr(M_q G)/V in a ground state. This formula includes
the endpoint form factors, the symmetrization and all elastic subtractions.

Put h^(2)(q)=(1/2)D²h(0)[q,q], A(q)=4h^(2)(q). The fourth derivative bound,
D³h(0)=0, and the symmetric integral for Delta imply

 ||M_q(k)-A(q)||
   <=162b |q|²|k|²+182b |q|^4.                         (L8)

For detail, ||Delta_q h(k)-h^(2)(q)||<= (81b/2)|q|²(|k|²+|q|²);
multiplication by F costs at most4. Replacing F Delta F by4Delta costs
<=18b|q|^4, and the double commutator with F-2I costs<=2b|q|^4.

The axial block of A(q) is4tau|q|² P_E. In a plane use low unit vector
u=(-1,1)/sqrt2 and high vector w=(1,1)/sqrt2. Its matrix is

 [ 8tau|q|²+2mu(q_i²+q_j²),  2mu q_i q_j ;
                    2mu q_i q_j,          0 ].

Its off-diagonal absolute value is<=mu|q|². Completing the square with the
remaining6tau|q|² of the low diagonal proves

 A(q)>=2tau|q|² I-C_Q |q|² Q0.                          (L9)

Also h(0)=2mu Q0 and ||h(k)-h(0)||<=(9b/2)|k|², so (L4) gives
Q0<=[1+(9b/2)c_h]h(k)/(2mu). Combining (L8)-(L9),

 M_q(k)>=|q|²[(2tau-182b|q|²)I-C_H h(k)].               (L10)

For the stated q range this is >=|q|²[tau I-C_H h(k)]. The actual
occupation identity D=N-2P+V3/mu implies P>=(N-D)/2. Hence

 m1(q)>=|q|²[tau rho/2-C_1 e],

which proves the first claim in (L1) at the stated nu. No derivative of an
energy envelope or assumption on pair coherence was used.

## L4. A local three-particle cost from the actual hard-core pin

For any fixed integer R and any ball B_R(x), take v_R=(2R+1)^3 as a safe
cardinality bound. On occupation configurations,

 1_(N_B>=3)
 <=sum_(y in B) n_y 1_(m_y=0)
   +sum_(y in B,d in G,z in B minus{y,y+d}) n_y n_(y+d)n_z. (L11)

If there is an occupied y in B with no actual graph neighbor, the first
term covers the configuration. Otherwise take an occupied y, one of its
occupied neighbors (possibly outside B), and a third occupied site z in B.
The first sum is bounded by sum_(y in B)D_y, with the ACTUAL outside degree.
No boundary degree is silently changed.

For each triple let e={y,y+d}. Translate the same raw pair word by r=z-y,
using a coordinate path of length m<=2R. Then n_z B_(e+r)=0 exactly,
because n_z b_z=0. Keep n_z on the LEFT throughout the telescope:

 ||n_z B_e psi||²
 <=m sum_(path steps) ||[B_(e+t+e_j)-B_(e+t)]psi||².      (L12)

There is no commutation of a projector past a translated annihilator.
At the starting edge z is distinct from both endpoints, so the left side
is precisely <n_y n_(y+d)n_z>. Summing over the center x for a fixed
relative triple gives at most m² Egrad. There are at most18 v_R² relative
triples. The source's full-carrier bound H0>=mu D+a Egrad proves

 sum_x <1_(N_B_R(x)>=3)>
 <=v_R<D>+72R²v_R² Egrad
 <=[v_R/mu+72R²v_R²/a]<H0>.                            (L13)

This finite-range high-occupancy estimate is valid for arbitrary coherent
states. It controls local spectators in the nested-current remainder;
it is not a dilute-product-state approximation or an all-distance cluster
tail. L>=25 makes B10's local embedding unambiguous in the use below;
all pins are actual torus paths and remain within the source gradient sum.

## L5. Exact full-carrier third moment and its local remainder

Use a positive local grouping h_x=mu D_x+S_x+W_x, with support inside B2(x),
at most25 sites. D_x has norm<=136; S_x has norm<=24mu by its literal
squares; W_x has norm<=240tau. Thus ||h_x||<=h is safe and sum h_x=H0.
This grouping need not coincide term by term with the original attractive
form's grouping. Both are exact sums of the same H0.

Let J_x(q)=[h_x,A_q], J(q)=sum_x J_x(q). Each h_x conserves local number.
Subtract exp(iq.x)N_B2 from A_q inside its commutator. The phase difference
sum is<=50|q|, yielding ||J_x(q)||<=100h|q|. Every J_x kills local sectors
N<=1, because diagonal D commutes with density and the other terms are
literal pair transfers.

Ground spectral resolution, including BOTH q and -q, gives

 m3(q)=(1/2V)<[J(q)*,[H0,J(q)]]>.                       (L14)

The chemical term drops out since [N,J]=0. The expectation is real and
positive even though individual local nested terms need not be Hermitian.
Expanding (L14), a nonzero inner pair has r within B4(t), at most129 choices.
The outer s lies within B4(t) or B4(r), at most258 choices. There are at most
33282 terms anchored at t; their support is contained in B10(t), and each

 O_srt=(1/2)[J_s(q)*,[h_r,J_t(q)]]

has norm<=20000h³|q|². All such operators preserve local N and kill local
N<=1. Their N2 matrices have rows/columns only on the actual G edges:
pair terms preserve those edges, and every D_x kills an actual two-site
G edge (its occupied endpoints have degree1). Nonedges are killed by J.

For each O take its EXACT local N2 matrix O^(2) and lift it as
Q(O^(2))=sum_(e,f inside support) O^(2)_ef B_e*B_f.
Then R=O-Q(O^(2)) has zero blocks on local N<=2. Because both terms preserve
local number, R=P_(Nlocal>=3) R P_(Nlocal>=3), on the full local tensor
product, including entangled outside states. The vector map psi->(B_e psi)
has squared norm at most the number of edges, <=9v10. Thus

 ||R||<=(1+9v10)||O||,
 |<sum R>|/V <= C_rem |q|² e,                           (L15)

by (L13). This is where actual hard-core higher-particle corrections are
paid. Dropping them or using canonical pair commutators would be invalid.

Linearity of exact N2 restriction shows that the sum of the lifted terms
is precisely the pair lift of the global N2 double-current matrix. On that
sector J(q) maps k to k+q with

 C_q(k)=h(k+q)F-Fh(k).

Using (L5), D h(0)=0 and ||F-2I||<=|q|² gives

 ||C_q(k)||<=20b |q|(|k|+|q|),
 ||C_q(k-q)||<=20b |q|(|k|+2|q|).                       (L16)

The N2 symbol T_q(k) of one half of the double current has four products:

 2T_q(k)= C_q(k)* h(k+q) C_q(k)-C_q(k)*C_q(k)h(k)
          -h(k) C_q(k-q)C_q(k-q)*
          +C_q(k-q)h(k-q)C_q(k-q)*.

Therefore

 ||T_q(k)||<=b[||C_q(k)||²+||C_q(k-q)||²]
            <=4000b³ |q|²(|k|²+|q|²).                  (L17)

This is a matrix norm bound, so it also bounds the real trace against the
positive G(k). Equation (L4), Hpair<=H0 and P<=9N give

 |<sum Q(O^(2))>|/V
 <=4000b³ |q|²[c_h e+9|q|²rho].                         (L18)

Adding the actual remainder (L15) proves the second claim of (L1).
No many-body current clustering, global pair Fock embedding, finite-size
spectral gap, or excitation ansatz has entered.

## L6. Soft-frequency consequence and exact remaining limit

For a positive measure, integral_(Omega,infinity) omega sigma_q<=m3/Omega².
The chosen Omega makes that upper bound <=tau rho|q|²/8, half the lower
first moment. This proves all three inequalities (L2), the latter two by
omega<=Omega and omega^-1>=omega/Omega² on the retained interval.

For fixed nu, the certified cutoff retains a term proportional to sqrt(nu).
To prove fixed-density sound or a frequency bound proportional to |q|
sqrt(rho), one would need a further source-specific cancellation of the
q²e term in (L1), or another actual long-wave theorem. The local N>=3
remainder estimate does not supply that cancellation. Thus the joint
small-nu/long-wave result is a genuine homogeneous density-response
statement but leaves the fixed-positive-density phase and spectrum open.
