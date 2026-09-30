# Inelastic on-site density response in homogeneous ground states

Author discovery theorem for the supplied H0, not a physical-law selection.
The contract is CONTRACT.md. All statements below are finite-volume, exact,
and uniform over cubic tori L>=5. No numerical input is used.

## O1. The actual operator and the spectral measure

Let b_x=|0><1|, n_x=b_x* b_x on actual M2 site factors. The pair graph has the
18 displacements +/-2e_i and +/-e_i+/-e_j. Let E be its UNIQUE undirected
physical edges, B_e=b_x b_y, P=sum_e B_e* B_e, and m_x its occupied degree.
The complete actual law is H0=S+mu D+W, with

 D=(1/2)sum_x n_x(m_x-1)(m_x-2),
 V3=mu sum_x n_x binom(m_x,2),
 S=(2mu/3)sum_x |d1+d2+d3|²
   +(mu/4)sum_(x,i<j,r<s)|v_r-v_s|²,
 W=tau sum_(x,j,A)|Q_A(x+e_j)-Q_A(x)|².

Definitions of the signed v and five Q are those in the contract's actual
main source. In particular S is retained. Expansion of only S+W defines
Hpair=sum_ef K_ef B_e*B_f, a real symmetric positive kernel on the physical
edge Hilbert space. This is an exact full-carrier identity, not a boson
replacement. Its absolute row sum is <=b=3mu+24tau: axial S rows cost2mu;
plane S rows at both centers cost3mu; axial W rows cost20tau,20tau,16tau;
plane W rows cost24tau. These follow by coefficient absolute sums of each
square before cancellation. Also P<=9N and

                     D=N-2P+V3/mu.                    (O1)

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

## O2. Pinned physical-edge gap and first moment

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
      =(2mu/3)<N>-2<H0>+(4mu/3)<D>+(2/3)<V3>
      >=(2mu/3)<N>-2<H0>.                              (O4)

Thus beta=2mu/3-2nu gives M1>=beta rho. In particular beta>=mu/3 when
0<nu<=mu/6. An early mechanism message used a weaker bound after discarding
one endpoint multiplicity; root's precomparison independently restored it.
No frozen proof or executed control was changed by that preliminary algebra.

## O3. Full hard-core second moment

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

## O4. Actual positive-frequency weight and inverse moment

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
