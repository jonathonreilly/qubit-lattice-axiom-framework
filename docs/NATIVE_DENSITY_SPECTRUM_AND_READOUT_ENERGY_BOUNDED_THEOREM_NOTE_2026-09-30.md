---
claim_id: native_density_spectrum_and_readout_energy_bounded_theorem_note_2026-09-30
claim_type: bounded_theorem
claim_scope: "For a supplied full-site qubit pair Hamiltonian: density spectral-moment estimates and exact occupation-readout/monitoring energy comparisons, with all observable, instrument and state hypotheses explicit."
upstream_dependencies:
  - minimal_axioms
  - native_qubit_pair_density_onset_bounded_theorem_note_2026-09-30
runner: scripts/native_density_spectrum_and_readout_energy_2026_09_30.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Connect the supplied density observable and energy-accounted readout to an actual physical collective mode and record process."
conditional_surface_status: "Theorems for the explicitly supplied finite-volume Hamiltonian and specified probes."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Algebraic and spectral bounds under explicit model, observable and instrument hypotheses."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Density spectrum and occupation-readout energy of a local qubit pair model

**Type:** bounded_theorem
**Status:** conditional-support (supplied model; unaudited)

**Target.** Prove quantitative density spectral weight and sharp full/local occupation-readout energy bounds for the same unchanged full-site qubit Hamiltonian, retaining its full hard-core carrier and the stated state/probe domains.

The supplied model is the one in the [density-onset theorem](NATIVE_QUBIT_PAIR_DENSITY_ONSET_BOUNDED_THEOREM_NOTE_2026-09-30.md). Its local algebra and positivity identity are restated below. That linked source supplies the exact normalized trial and finite-volume onset estimates used in the readout examples. Every new load-bearing argument is proved in this note. The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the premise boundary, not a choice of Hamiltonian, density probe or readout instrument. The registered scale, kinetic-form and realized-state primitives retain their stated grants.

The model, tensor-product quantum states, expectation rule, basis, positive parameters and monitoring clock are supplied mathematical conditions. Spectral weight is not identified here with gravity, a sound mode, a selected phase or a permanent framework record. The source makes no use of an open equation of state or four-particle threshold theorem.

For every L>=5, define the positive sharp readout constant

    c_read=min(mu,mu/3+2tau),    Delta(H0)>=c_read N.          (1)

The on-site spectral theorem below applies to ground states of H0-nu N at 0<nu<mu/3, with beta=2mu/3-2nu>0. The long-wave theorem applies for L>=25 and the explicit small positive nu and nonzero reciprocal q bounds given below. Its certified frequency cutoff tends to zero only in a joint nu,q->0 limit. The readout and monitoring comparisons apply to every state, with no ground-state condition.

## 1. Actual carrier, Hamiltonian and instrument

Let Lambda=(Z/LZ)^3, L>=5, V=L^3. Each site has its actual tensor factor C^2, with b_x=|0><1|, n_x=b_x^dagger b_x, N=sum_x n_x and empty vector Omega. Operators on different sites commute. No pair-boson substitution is made. The parameters mu,tau are arbitrary supplied positive numbers.

For axes e_i define

    d_i(x)=b_(x+e_i)b_(x-e_i),
    v_ij^(s,t)(x)=st b_(x+s e_i)b_(x+t e_j), i<j,
    Q_E1=(d_1-d_2)/sqrt2,
    Q_E2=(d_1+d_2-2d_3)/sqrt6,
    Q_Tij=(1/2)sum_(s,t=+/-1) v_ij^(s,t).

Let P_E=sum_(A=E1,E2) Q_A^dagger Q_A and P_T=sum_(i<j)Q_Tij^dagger Q_Tij. Write D for the eighteen displacements +/-2e_i and +/-e_i+/-e_j and m_x=sum_(d in D)n_(x+d). The actual Hamiltonian is

    H0=mu N-2mu sum_x P_E(x)-mu sum_x P_T(x)+V3+W,
    V3=mu sum_x n_x binom(m_x,2),
    W=tau sum_(x,k,A) |Q_A(x+e_k)-Q_A(x)|^2.                 (2)

Here |R|^2=R^dagger R. Its full-carrier positive decomposition, restated to fix every local term, is

    H0=S+mu Ddiag+W,
    S=(2mu/3)sum_x |d_1(x)+d_2(x)+d_3(x)|^2
      +(mu/4)sum_(x,i<j)sum_(r<s)|v_ij^r(x)-v_ij^s(x)|^2,
    Ddiag=sum_x n_x f(m_x),    f(m)=(m-1)(m-2)/2.           (3)

The identities sum_E Q_A^dagger Q_A=sum_i d_i^dagger d_i-|sum_i d_i|^2/3 and sum_(r<s)|v_r-v_s|^2=4sum_r|v_r|^2-|sum_r v_r|^2 give (3), because an axial pair occurs once and a plane pair twice. Indeed 2sum|d|^2+sum|v|^2=sum_x n_xm_x, and 1-m+binom(m,2)=f(m). Each summand in (3) is positive: f(m)>=0 for every integer m=0,...,18. The identity and positivity hold on the entire tensor product, not just on occupation vectors.

For every occupation configuration eta, let P_eta=|eta><eta|. Supply the joint occupation Lüders instrument I_eta(rho)=P_eta rho P_eta. Its outcome-averaged channel is

    Delta(rho)=sum_eta P_eta rho P_eta.                       (4)

The same expression acts on observables and is self-adjoint for the trace pairing. In particular Delta(N)=N, and all instantaneous occupation statistics are unchanged. Throughout, rho is an arbitrary density matrix; no sharp N, translation invariance or stationarity is assumed unless explicitly stated.

Equation (4) is also forced by any CP instrument with effects exactly P_eta and outputs supported in the same rank-one P_eta. If K_(eta,a) are its Kraus operators, the locked output implies K_(eta,a)=|eta><v_(eta,a)|. Its effect sum_a |v_(eta,a)><v_(eta,a)|=P_eta then gives I_eta(rho)=Tr(P_eta rho)P_eta=P_eta rho P_eta. This familiar rank-one normal form does not cover destructive measurement followed by a different re-preparation, unsharp effects or incomplete readout. For a proper subset of sites we use the Lüders instrument specifically; its output sectors are not rank one on the full carrier, so the same uniqueness assertion is unavailable.

## 2. On-site inelastic density weight

### 2.1. Positive-frequency measure and literal row bound

Let b_x=|0><1|, n_x=b_x* b_x on actual M2 site factors. The pair graph has the
18 displacements +/-2e_i and +/-e_i+/-e_j. Let E be its UNIQUE undirected
physical edges, B_e=b_x b_y, P=sum_e B_e* B_e, and m_x its occupied degree.
The complete actual law is H0=S+mu Ddiag+W, with

 Ddiag=(1/2)sum_x n_x(m_x-1)(m_x-2),
 V3=mu sum_x n_x binom(m_x,2),
 S=(2mu/3)sum_x |d1+d2+d3|²
   +(mu/4)sum_(x,i<j,r<s)|v_r-v_s|²,
 W=tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|².

The signed v and five Q are the literal words in section 1. In particular S is retained. Expansion of only S+W defines
Hpair=sum_ef K_ef B_e*B_f, a real symmetric positive kernel on the physical
edge Hilbert space. This is an exact full-carrier identity, not a boson
replacement. Its absolute row sum is <=b=3mu+24tau: axial S rows cost2mu;
plane S rows at both centers cost3mu; axial W rows cost20tau,20tau,16tau;
plane W rows cost24tau. These follow by coefficient absolute sums of each
square before cancellation. Also P<=9N and

                     Ddiag=N-2P+V3/mu.                    (O1)

For Hnu=H0-nu N, let E0 be its lowest eigenvalue, P0 its FULL ground
projection, Q=1-P0, and Gamma any ground density matrix. Put

 sigma(domega)=V^-1 sum_x Tr Gamma n_x Q dP_(Hnu-E0)(omega) Q n_x,
 M_j=integral_(0,infinity) omega^j sigma(domega),
 rho=Tr Gamma N/V, e=Tr Gamma H0/V.

There is no ground-space simplicity assumption. M0 removes all elastic
ground-to-ground density transitions, even across a degeneracy. Because
n_x²=n_x, M0<=rho. Since the vacuum is a variational state, E0<=0 and
e<=nu rho. Translation averaging Gamma is allowed; for a translation-
invariant Gamma, sigma is precisely the one-site measure at any chosen site.
'Homogeneous' concerns the state, not the momentum of the probe. The q=0
observable N has identically zero inelastic response.

### 2.2. Pinned physical-edge gap and first moment

Let p_x be the diagonal projection on edges incident at physical site x.
The literal S compression satisfies

                       p_x S p_x >=(2mu/3)p_x.          (O2)

Here S denotes its pair matrix. The eighteen pinned edges divide into six
axial edges and three groups of four plane edges. Every axial diagonal is
2mu/3 and all its pinned off-diagonals vanish. In a plane the four neighbor
directions (+,+),(+,-),(-,+),(-,-) form a square: each diagonal is3mu/2,
each square-neighbor off-diagonal is+mu/4, and opposite entries vanish.
Each physical plane edge occurs at both centers. The signs follow from
v^(s,t)=st B: the shared-center signed coefficients have opposite signs,
while the difference-square off-diagonal is negative. The plane minimum
is mu (the adjacency eigenvalues are2,0,0,-2). Different planes/axial
families have no S cross entries. W>=0 keeps (O2) valid for K.

For any state the exact site algebra gives

 (1/2)sum_x <[n_x,[H0,n_x]]>
  =sum_x <B* p_x K p_x B>-2<Hpair>.                     (O3)

Indeed sum_x(1_(x in e)-1_(x in f))²=4-2|e intersect f|.
Every edge is incident at TWO endpoints, so sum_x p_x=2I. This factor is
essential. Ground-state spectral resolution and (O2) therefore yield

 VM1 >=(4mu/3)<P>-2<Hpair>
      =(2mu/3)<N>-2<H0>+(4mu/3)<Ddiag>+(2/3)<V3>
      >=(2mu/3)<N>-2<H0>.                              (O4)

Thus beta=2mu/3-2nu gives M1>=beta rho. In particular beta>=mu/3 when
0<nu<=mu/6.

### 2.3. Full hard-core second moment

Write delta_x(e,f)=1_(x in e)-1_(x in f). The actual current is
[Hnu,n_x]=-sum_ef K_ef delta_x(e,f) B_e*B_f. For a unit vector psi,
weighted vector Cauchy-Schwarz, ||B_e*||<=1, and the row bound give

 A_x:=sum_ef |K_ef delta_x(e,f)| <=36b,
 ||[Hnu,n_x]psi||²
   <=36b sum_ef |K_ef delta_x(e,f)| <B_f*B_f>.

The factor36 is two ordered row/column incidences times18 edges. Summing x
uses sum_x |delta_x(e,f)|<=4, hence

 sum_x ||[Hnu,n_x]psi||² <=144b²<P><=1296b²<N>.           (O5)

The same follows for mixed states by linearity. In a ground state this
left side is VM2. Put C2=1296b². No uncorrelated-pair assumption or distant
current factorization is involved.

### 2.4. Actual positive-frequency weight and inverse moment

For beta>0, the exact spectral moment inequalities imply

       M0 >= M1²/M2 >=(beta²/C2)rho,
       M_-1 >= M1³/M2² >=(beta³/C2²)rho.                 (O6)

The second inequality is Holder applied to omega=(omega^-1)^(1/3)
(omega²)^(2/3). It remains valid if the inverse moment is infinite; each
finite volume has a finite positive-spectrum inverse. This is an inelastic
reduced inverse-energy functional. Calling2M_-1 the derivative of a chosen
ground branch would need a separate nondegeneracy/branch prescription.

The stronger frequency-window statement is useful for scope. Define

       delta=beta/4, Omega=2C2/beta.

The energy-weighted mass below delta is at most delta M0<=beta rho/4;
that above Omega is at most M2/Omega<=beta rho/2. Consequently

 integral_[delta,Omega] omega sigma(domega)>=beta rho/4,
 sigma([delta,Omega]) >= beta² rho/(8C2).                (O7)

The interval is volume independent and bounded AWAY from zero. Thus this
result certifies local density excitation weight even in a homogeneous,
degenerate ground state. It can be entirely optical/high-momentum weight.
It is not sound, a zero-momentum response, ODLRO, or the full quantum
collective-phase identification. The separate long-wave analysis must not
be inferred from (O6)-(O7).

## 3. Homogeneous joint dilute and long-wave density weight

Throughout, B_R(x) denotes the l1 nearest-neighbor graph ball; v_R=(2R+1)^3 is only a safe enclosing-cube cardinality bound.

### 3.1. Spectral statement and constants

Take L>=25, V=L³, Hnu=H0-nu N, and any ground density matrix Gamma. Set
rho=<N>/V, e=<H0>/V<=nu rho. For a nonzero reciprocal vector q=2pi m/L chosen in
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
The constants are not empirical calibrations. The certified mass lower bound
tau rho|q|²/(8Omega) vanishes in the joint limit; the normalized energy-weighted
lower bound is the assertion. No upper bound on total spectral mass is claimed.

### 3.2. Actual physical-edge matrix in a pair-center frame

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

### 3.3. A lower first moment at the actual homogeneous point

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
occupation identity Ddiag=N-2P+V3/mu implies P>=(N-Ddiag)/2. Hence

 m1(q)>=|q|²[tau rho/2-C_1 e],

which proves the first claim in (L1) at the stated nu. No derivative of an
energy envelope or assumption on pair coherence was used.

The bare-gradient form used here is

    Egrad=sum_(x,j,t) ||[B_t(x+e_j)-B_t(x)]psi||²,

where t runs over the three d_i and twelve signed v_ij^(s,t) words, including both centered occurrences of a plane edge. To justify H0>=mu Ddiag+a Egrad on the full carrier, orthogonally decompose the three d amplitudes into the E doublet and their singlet, and each four-entry plane amplitude into Q_T and its three perpendicular components. S assigns coefficient2mu to the singlet and mu to those plane complements. The Hilbert-space-valued torus estimate sum_(x,j)||f(x+e_j)-f(x)||²<=12sum_x||f(x)||² then gives Egrad<=6<S_E>/mu+12<S_T>/mu+<W>/tau. Since a=min(tau,mu/12), the claimed comparison follows by retaining the SAME positive Ddiag term. This is the actual fifteen-word form, with its physical multiplicities, not an independent pair-field energy.

### 3.4. A local three-particle cost from the actual hard-core pin

For any fixed integer R and any ball B_R(x), take v_R=(2R+1)^3 as a safe
cardinality bound. On occupation configurations,

 1_(N_B>=3)
 <=sum_(y in B) n_y 1_(m_y=0)
   +sum_(y in B,d in D,z in B minus{y,y+d}) n_y n_(y+d)n_z. (L11)

If there is an occupied y in B with no actual graph neighbor, the first
term covers the configuration. Otherwise take an occupied y, one of its
occupied neighbors (possibly outside B), and a third occupied site z in B.
The first sum is bounded by sum_(y in B)n_y f(m_y), with the ACTUAL outside degree.
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
triples. The full-carrier bare-gradient comparison defined and justified above, H0>=mu Ddiag+a Egrad, proves

 sum_x <1_(N_B_R(x)>=3)>
 <=v_R<Ddiag>+72R²v_R² Egrad
 <=[v_R/mu+72R²v_R²/a]<H0>.                            (L13)

This finite-range high-occupancy estimate is valid for arbitrary coherent
states. It controls local spectators in the nested-current remainder;
it is not a dilute-product-state approximation or an all-distance cluster
tail. L>=25 makes B10's local embedding unambiguous in the use below;
all pins are actual torus paths and remain within the source gradient sum.

### 3.5. Exact full-carrier third moment and its local remainder

Write D_x=n_x f(m_x), so Ddiag=sum_x D_x. Use a positive local grouping h_x=mu D_x+S_x+W_x, with support inside B2(x),
at most25 sites. D_x has norm<=136; S_x has norm<=24mu by its literal
squares; W_x has norm<=240tau. Thus ||h_x||<=h is safe and sum h_x=H0.
This grouping need not coincide term by term with the original attractive
form's grouping. Both are exact sums of the same H0.

Let J_x(q)=[h_x,A_q], J(q)=sum_x J_x(q). Each h_x conserves local number.
Subtract exp(iq.x)N_B2 from A_q inside its commutator. The phase difference
sum is<=50|q|, yielding ||J_x(q)||<=100h|q|. Every J_x kills local sectors
N<=1, because diagonal Ddiag commutes with density and the other terms are
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
N<=1. Their N2 matrices have rows/columns only on the actual pair-graph edges:
pair terms preserve those edges, and every D_x kills an actual two-site
pair-graph edge (its occupied endpoints have degree1). Nonedges are killed by J.

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

### 3.6. Soft-frequency consequence and exact remaining limit

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

## 4. Exact diagonal and sharp constant

Let E_a=sum_(unordered axial edges xy)n_xn_y and E_p=sum_(unordered plane edges xy)n_xn_y. Every occupied pair contributes one to the relevant count, independent of its other neighbors. Then

    Delta(H0)=mu Ddiag+w_a E_a+w_p E_p,
    w_a=2mu/3+4tau,    w_p=3mu/2+3tau.                       (5)

Here is the full diagonal calculation. For a pair annihilator B_e=b_xb_y, x!=y, an occupation vector eta is mapped to its configuration with e removed, or zero. Distinct unordered pairs produce orthogonal output vectors. Hence

    Delta(|sum_e a_e B_e|^2)=sum_e |a_e|^2 n_xn_y.           (6)

For the first part of S, each axial word has coefficient 2mu/3 and unique center. In a plane, each signed word occurs in three pair differences, giving 3mu/4 at each of its two centers, hence 3mu/2 per plane edge.

The sum of squared E-component coefficients of each d_i is 2/3; each plane word has squared coefficient 1/4 in its T component. On summing the three positive-direction gradients over all centers, each same-center Q_A^dagger Q_A occurs six times. Thus W supplies axial weight 6*(2/3)tau=4tau, and plane weight 6*2*(1/4)tau=3tau. No gradient cross term has a diagonal: axial pairs have one center; the two centers of a plane pair differ by a diagonal displacement +/-e_i+/-e_j, never a nearest-neighbor displacement. Thus an identical pair cannot occur at both adjacent centers in the same Q component. These elementary center facts hold modulo L for every L>=5, including odd L. There is no global bipartite-parity assumption.

One can also compute directly in (2): Delta(P_E)=(2/3)E_a and Delta(P_T)=(1/2)E_p. This gives the equivalent identity

    Delta(H0)=mu N+V3+(4tau-4mu/3)E_a+(3tau-mu/2)E_p.       (7)

The coefficients in (7) can be negative; replacing them independently by positive terms would be incorrect. Equation (5) retains the full positive diagonal combination.

To prove (1), allocate half of each edge weight to each endpoint. For an occupied site with m=m_a+m_p neighbors, its allocated diagonal energy is

    mu f(m)+(w_a m_a+w_p m_p)/2.                            (8)

At m=0 it is mu. At m>=1 it is at least min(w_a,w_p)/2, since f(m)>=0. Thus the best candidate among these alternatives is min(mu,w_a/2,w_p/2). This equals c_read in (1). If tau<=mu/3, then w_p/2-w_a/2=5mu/12-tau/2>=mu/4, while c_read=w_a/2. If tau>=mu/3, both w_a/2 and w_p/2 are at least mu. Summing (8) proves the diagonal operator inequality, and hence every-state expectation version.

The constant is sharp, at every stated torus size: a single occupied site has Delta(H0)=mu and N=1; an isolated axial pair has Ddiag=0, E_a=1, E_p=0 and N=2, giving ratio w_a/2. No larger uniform constant can satisfy (1). Plane dimers do not improve it.

For a concrete coherent example, the normalized uniform E1 pair vector

    psi_E=V^(-1/2)sum_x Q_E1(x)^dagger Omega

has N=2 and H0 energy zero by (3). Every occupation configuration in its support is an axial edge, so its fully dephased energy is exactly w_a>0. The state and its dephased twin have the same full occupation distribution. This is both an energy discriminator and a warning: that distribution alone does not recover the initial coherent energy. Occupation pinching and its loss of offdiagonal energy are standard finite-dimensional facts; the model-specific content here is the sharp floor and local coefficient accounting.

## 5. System energy injected by full readout

Define the expected injection, with H0 and its reference unchanged, by

    J_full(rho)=Tr[H0(Delta(rho)-rho)].

Writing E=Tr(H0rho), nbar=Tr(Nrho), (1) yields

    J_full(rho)>=c_read nbar-E.                             (9)

The same injection is obtained for H0-nu N, because the channel preserves N. Equation (9) is an energy difference, not an entropy bound. For an arbitrary input it need not be positive. A diagonal input is unchanged and has J_full=0. For any family with E/nbar tending to zero and nbar>0, it implies

    liminf J_full/nbar >=c_read.                            (10)

Neither existence of that family nor its physical preparation follows from (10). If the readout is followed by the supplied closed Hamiltonian evolution exp(-itH0), both H0 and N expectations remain constant because [H0,N]=0. For nbar>0 its dephased output therefore retains energy per particle at least c_read at every such later time. Closed evolution alone cannot restore a smaller energy-per-particle expectation; this is an energy statement, not permanence of the occupation record. The linked density-onset theorem gives actual controlled low-energy inputs without importing the open EOS, as follows.

Set A=10199347200(182mu+240tau), B0=3870720. The exact normalized full-carrier trial psi(u)=exp(-iuG_pulse)Omega, G_pulse=sum_x i(Q_E1(x)^dagger-Q_E1(x)), has at every finite L

    0<=E_u/V<=A u^4,
    |nbar_u/V-2u^2|<=B0 u^4.

Consequently

    J_full(psi(u))/V >=2c_read u^2-(A+c_read B0)u^4.         (11)

It is positive for 0<u^2<2c_read/(A+c_read B0), uniformly in volume. The particle density is then positive: this range lies within u^2<2/B0. In the limit u->0, E_u/nbar_u->0 uniformly in L. There is no requirement V u^2<<1 and no number-sector projection or bosonic trial.

For a ground-state density matrix of Hnu=H0-nu N, let E_g be its ground energy. The density-onset theorem gives

    nbar/V>=nu/(A+nu B0),    E_g/V<=-nu^2/(A+nu B0).

Since E=E_g+nu nbar, (9) gives

    J_full >=(c_read-nu)nbar-E_g.

For every 0<nu<=c_read, both landed inequalities can be inserted with their correct signs, yielding the positive extensive bound

    J_full/V >=c_read nu/(A+nu B0).                        (12)

This holds for every finite-volume ground-state density matrix, including degenerate mixtures. No differentiable equation of state, thermodynamic uniqueness or state polarization is assumed. For arbitrary nu>c_read this substitution is not valid because the coefficient of nbar changes sign; no extension of (12) is claimed.

The price in (9)-(12) is per particle or expected occupied outcome, not a positive constant per measured site. A complete readout reports V bits, most of which can be zero at low density. Neither n_x=1 nor a bit result is identified with occurrence of a framework Record.

## 6. Spatial readout with the actual boundary terms

Let B be any subset of the finite torus, and Delta_B the Lüders dephasing of all n_x with x in B, leaving the exterior factors otherwise untouched. Use nearest-neighbor torus graph distance and define

    B^-3={x: every site at distance<=3 from x belongs to B},
    B^+2={x: distance(x,B)<=2}.

An empty interior makes the bounds below weak but valid. No large-box hypothesis or infinite-volume limit is needed.

Index the individual positive summands in (3) by alpha: each singlet square, each of the six differences for each plane, each Q-gradient square, and each mu n_x f(m_x). Write them h_alpha>=0. Assign their center to x exactly as in (3), and let

    h_x^+=sum_(alpha based at x) h_alpha,    H0=sum_x h_x^+.

Every h_x^+ has support within the graph-distance ball of radius2 about x. In particular the diagonal term uses the actual eighteen neighbors; none is removed or reset. Define H_touch(B) as the sum of the individual h_alpha whose support meets B. Positivity gives

    0<=H_touch(B)<=sum_(x in B^+2) h_x^+.                  (13)

Let H_in(B) be the sum of the individual h_alpha wholly supported in B. Untouched terms cancel from Delta_B(H0)-H0. The images under Delta_B of all positive touched terms remain positive. Therefore

    Delta_B(H0)-H0 >=Delta_B(H_in(B))-H_touch(B).           (14)

The decisive exact boundary statement is

    Delta_B(H_in(B))>=c_read N_(B^-3).                    (15)

To prove it, first retain the actual diagonal summands mu n_x f(m_x) at every x in B^-3: their radius is2, so they are wholly inside. For any graph edge e={x,y} incident to such x, every S or W row contributing to its full diagonal coefficient in (5) is also inside B. An S row has a center at distance1 from x and endpoints at most2 from x. For a W row, one of its two adjacent centers is at distance1 from x; all endpoints of both stars are at most3 from x. The statement covers both centers of each plane pair, all relevant components, all gradient directions and both gradient appearances of that center. It uses individual complete rows, not the stronger demand that an entire centered family h_z^+ be contained in B.

All these rows dephase completely because their supports lie in B. Equation (6) makes their images nonnegative diagonal edge sums; they therefore supply the entire w_e for every edge incident to B^-3, as well as possibly other positive edge weights. Allocate half w_e to each endpoint in B^-3. An edge with one endpoint there is underused by a factor two; with two endpoints it is used exactly once. Combining this allocation with its actual Ddiag_x is exactly (8) at each interior site. This proves (15), without replacing any physical m_x, assuming monotonicity under edge deletion or introducing an independently minimized cell model.

Combining (13)-(15) gives the local operator inequality and its energy version

    Delta_B(H0)-H0 >=c_read N_(B^-3)-sum_(x in B^+2)h_x^+,
    J_B(rho)>=c_read <N_(B^-3)>_rho
                   -<sum_(x in B^+2)h_x^+>_rho.           (16)

The upper local energy debit is the energy actually present in the original state near B. It is not a putative modified-boundary Hamiltonian. If rho is translation invariant, with r=nbar/V and e=E/V, then

    J_B(rho)>=c_read r |B^-3|-e |B^+2|.                   (17)

For a cube of side ell with no wrap or overlap of its radius2 enlargement, |B^-3|=(ell-6)^3 for ell>=6 and |B^+2|<=(ell+4)^3. Thus, for ell>=7,

    J_B >=c_read r(ell-6)^3-e(ell+4)^3.                  (18)

The exact graph-distance enlargement is generally smaller than this enclosing cube. In particular (18) is a safe inequality, not an asserted volume identity. For any fixed such ell, (18) is positive for a sufficiently small energy-per-particle ratio e/r. The exact unitary trial above is translation invariant, so (11)'s inputs directly supply

    J_B(psi(u))>=2c_read |B^-3|u^2
                -[c_read B0 |B^-3|+A |B^+2|]u^4.        (19)

This can be a genuinely local readout in a much larger torus. Its positive leading cost is the occupied weight in the interior, not an assumption of uniform energy allocation for an inhomogeneous state. For such an inhomogeneous state, use the full expression (16).

Three steps are sufficient for this allocation proof. Two steps are insufficient to retain all the actual gradient coefficients: a gradient containing the pair {-2e_1,0} can also contain the pair {-3e_1,-e_1}. The primary includes a literal row with that support. This does not prove that every possible two-step bound fails; it identifies the exact support requirement of this proof.

For B=Lambda, (16) reduces to (9). For B empty it reads zero>=zero. Partial readout followed by arbitrary exterior feedback is a different channel and is not covered by (16).


## 7. Occupation-monitoring energy identity

Keep full tensor-product M2 site factors on the cubic torus L>=5, mu,tau>0, and the actual H0=S+mu Ddiag+W. The graph edges have offsets +/-2e_i or +/-e_i+/-e_j. Let B_e=b_i b_j for each unordered graph edge e={i,j}, and let K be the positive scalar edge matrix for S+W=B^dagger K B. Each e has two distinct sites. For the convention

    D[n]^*(O)=n O n-(nO+On)/2=-[n,[n,O]]/2,

write P_x for the numerical projection onto edges incident to x. Since [n_x,B]=-P_xB, the dissipator product rule yields

    sum_x D[n_x]^*(B^dagger K B)
       =sum_x B^dagger P_x K P_x B-2B^dagger K B.           (M1)

The two loss terms each give minus B^dagger K B because sum_x P_x=2I. This identity does not assume that distinct B_e are independent physical annihilators. It is an exact algebraic identity on the original hard-core carrier. The positive diagonal Ddiag commutes with every n_x and has zero dissipative derivative. Define

    J=sum_x B^dagger P_x K P_x B,
    Q_read=sum_x D[n_x]^*(H0)=J-2(S+W).

Hence Q_read+2H0=J+2mu Ddiag. Retaining this diagonal term is essential to the all-state N bound.

A useful normalization check is an individual B_e^dagger B_f. Its coefficient under the summed dissipator is |e intersect f|-2. It is0 for e=f, -1 for one shared endpoint and -2 for disjoint pairs. Treating every offdiagonal entry as decaying at rate2 would be wrong. These factors follow directly from the literal input/output occupation values in nOn-{n,O}/2; the primary checks their four-qubit action.

## 8. The complete incident-pair matrix

Fix x=0. The incident vector has eighteen components b_0 b_y: six axial neighbors and four sign choices in each of three coordinate planes. The actual compression P_0 K P_0, on these eighteen coordinates, is

    (2mu/3+4tau)I_6
    direct-sum three copies of
    (3mu/2+3tau)I_4+(mu/4-3tau/2)A_C4.                   (M2)

Here the cycle joins plane sign patterns (s,t) differing in one sign. There is no axial/plane or distinct-plane mixing.

For S, a fixed incident axial word is alone in its centered singlet restriction, giving2mu/3. Each plane word occurs in three differences at each of its two centers, giving diagonal3mu/2. At either center the two incident signed plane words have opposite signs. Their difference Gram therefore gives positive offdiagonal mu/4; these pairs are exactly the cycle edges.

For W, every center containing a pair incident to0 is one of the six nearest neighbors of0. No two distinct such centers are nearest neighbors to one another at L>=5. Thus a gradient between adjacent centers cannot have incident terms on both sides. The cross-center pin block vanishes, although the unpinned Hamiltonian cross terms certainly do not. Each center occurs six times in the three-direction gradient sum. The E Gram gives axial4tau. The T Gram at a fixed center has opposite coefficients1/2 and-1/2 for its two incident words, giving negative offdiagonal-3tau/2. Including both centers supplies diagonal3tau. This accounts for the entire W contribution in (M2). It uses the actual six-center geometry and does not assume global bipartiteness on odd tori.

The plane characters1,s,t,st give eigenvalues

    2mu,    3mu/2+3tau,    3mu/2+3tau,    mu+6tau.

Together with six axial eigenvalues2mu/3+4tau, their minimum is

    lambda_pin=min(2mu/3+4tau,2mu)=2c_read,
    c_read=min(mu/3+2tau,mu)>0.                            (M3)

In particular dropping W is a valid weaker estimate but loses this actual parameter-dependent pin. Its offdiagonal sign cannot be replaced by a diagonal row count.

The numerical18x18 matrix has no nullspace. On the full carrier, the positive operator J does have a kernel: it consists exactly of states annihilated by every graph-edge B_e. Since ||B_e psi||^2=<n_i n_j>, this is the span of occupation configurations that are independent sets in the eighteen-neighbor graph. This numerical matrix acts on edge labels; it does not replace or compress the many-body carrier. Adding2mu Ddiag removes every nonvacuum vector in that kernel; the eventual comparison controls particle number.

## 9. The all-state monitoring comparison

For every vector psi, apply (M3) to the Hilbert-space-valued incident components B_e psi and sum over x. Each unordered edge is counted at its two endpoints. Therefore

    J>=2c_read sum_x n_x m_x=4c_read E_pair,
    E_pair=sum_(unordered graph edges ij)n_i n_j.          (M4)

No independence, factorization, condensate, fixed-N restriction or real-amplitude assumption is used. Arbitrary complex coherent and mixed states are included by the operator inequality.

The actual diagonal count identity is

    Ddiag=N-2E_pair+V3/mu,
    V3=mu sum_x n_x binom(m_x,2).

Consequently the positive remainder estimate is

    Q_read >=2c_read N-2H0
             +2(mu-c_read)Ddiag+(2c_read/mu)V3
           >=2c_read N-2H0.                              (M5)

Both remainders are positive on the full carrier because m_x has integer spectrum, f(m)=(m-1)(m-2)/2>=0 there, V3>=0 and c_read<=mu. The last inequality does not require a low-energy input.

As an additional coefficient discriminator,2c_read is sharp if the coefficient of H0 is held at-2. A monomer has <Q_read>=0 and H0 expectationmu, realizing ratio2mu in Q_read+2H0 per particle. An axial dimer has <Q_read>=0 and H0 expectation2mu/3+4tau, realizing ratio2mu/3+4tau per particle. These occupation configurations are legitimate at every stated L. This is sharpness of the comparison constant, not equality in the integrated bound for an arbitrary evolving state.

The adjective heating requires a state qualification: Q_read is not claimed positive as an operator. The adjoint of this unital finite-dimensional dissipator has zero trace on every input, so a nonzero Q_read cannot be positive everywhere. Equation(M5) instead supplies a useful lower derivative while E<c_read nbar and a general comparison at all energies.

## 10. Integrated monitoring strength

Supply the stated master equation, with real fixed nu,

    rho_dot=-i[H0-nuN,rho]+gamma(t)sum_x D[n_x](rho),

where gamma>=0 is bounded and integrable on the time interval being considered. The finite-dimensional linear equation has a unique absolutely continuous density-matrix solution. Equivalently, piecewise constant positive-rate propagators are completely positive and trace preserving, and their norm limits give the solution. There is no thermodynamic-limit dynamics assertion here. Bounded local integrability suffices for every finite time interval.

Both [H0,N]=0 and [n_x,N]=0 hold literally. Thus nbar=Tr(Nrho(t)) is constant, and all Hamiltonian contribution to E'(t), E=Tr(H0rho), vanishes, including the supplied chemical-potential term. Equation(M5) gives almost everywhere

    E'(t)>=2gamma(t)(c_read nbar-E(t)).

Multiplying by exp(2Gamma(t)), Gamma(t)=integral_0^t gamma, and integrating proves

    E(t)>=c_read nbar+[E(0)-c_read nbar]exp(-2Gamma(t)).    (M6)

Nonconstant rates and intervals with gamma=0 are handled by the same absolutely continuous integrating-factor calculation. There is no division by gamma. If nbar=0, positivity of N forces the vacuum state and both sides vanish. If E(0)>=c_read nbar, (M6) remains valid but does not assert monotonic heating. If E(0)<c_read nbar, its lower bound rises toward the floor with integrated monitoring strength.

For an input with E0<c_read nbar, an endpoint condition E(t)<=Emax<c_read nbar requires

    Gamma(t)<=0.5 log[(c_read nbar-E0)/(c_read nbar-Emax)]. (M7)

Both denominators are positive in the stated domain. If Emax<E0, its negative right side simply shows that the condition cannot hold; if one says maintaining the tolerance over an interval, Emax>=E0 is necessary already at time0. A necessary condition is not a sufficient control or attainability theorem.

For fixed mu,tau and nbar>0, put e0=E0/nbar, emax=Emax/nbar. If e0 and emax are O(r) as r->0, with e0<=emax<c_read, then the right side of (M7) is O(r). The energy scale c_read must remain fixed in this statement; no joint limit mu,tau->0 is implied. In the concrete density notation r=nbar/V, a target E(t)/V<=C r^2 with C r<c_read implies, using E0>=0 alone,

    Gamma(t)<=-0.5 log(1-C r/c_read)=O(r).

This is only the supplied tolerance implication. The landed normalized unitary trial supplies actual small energy-per-particle initial states, but it does not select a phase, a tolerated energy, a measurement strength or a physical clock. No open EOS is necessary for this conclusion.


## 11. Energy accounting and physical boundary

The readout and monitoring formulas concern the change of the system expectation of the same H0 with the same energy reference. To call that change supplied work, include the apparatus, controller, memory and battery in H_A, and keep interaction energy H_int. With external work W_ext the first law is

    W_ext=Delta E_system+Delta E_A+Delta E_int.

For zero expected interaction change at the endpoints, W_ext-Delta E_A equals the system injection. An autonomous conserving implementation then loses that energy from its apparatus; if H_A is nonnegative, its initial expected energy is at least a positive system injection. Without that endpoint condition, the interaction change remains in the ledger. This is a conditional necessary accounting identity, not a constructed finite apparatus or an entropy/erasure theorem.

The complete sharp instrument, its partial Lüders version, and the continuous on-site dissipative law are specified probes. They are distinct protocols. The master equation determines unconditional evolution and does not choose an unraveling, realized outcome, record process or clock. The expected occupied-outcome count N is not the count of all records written. Alternative probes, state preparation, physical mode identification and a permanent readable process are separate scientific targets.

## 12. Scope and evidence

The algebraic chain is: actual full-carrier positive decomposition; diagonal edge geometry; sharp degree allocation; individual positive-row boundary allocation; exact incident-pair compression; full-carrier count inequality; finite-dimensional evolution and integrating factor. These are proved above. The exact trial and onset inequalities used for example inputs are supplied by the linked current-main density-onset theorem. The density response is proved by the literal edge pin and current norm, the nine-edge symbol and exact density form factor, the local two-particle lift with its spectator-controlled many-body remainder, and positive-measure moment inequalities.

The primary and its analytic control derivation test the finite identities identified in this proof; the exact executed evidence and mutations are recorded in the source/input-bound accompanying pack. Finite controls will support the explicit formulas and normalizations; the all-volume quantifiers come from the proofs. The earlier focused checks do not confer a formal review of this new unit. Independent whole-unit review and combined integration validation remain separate requirements.
