# Blind PRE: recent first births in the full compensated-cube ensemble

This independent reconstruction uses only the four frozen notes listed below.
No current author candidate, checkpoint, new research route, or author builder
was read. The result is conditional mathematics for the supplied model, not
an audit verdict, physical selection claim, or resource theorem.

## Supported conclusion

Let rho_e(t) be the complete original continuous GKLS density from the canonical
Hermitian N=4 zero-field input. Keep t>0 and delta,K,kappa>0 fixed, and take the
joint integer-spin limit

    epsilon^2 S(S+1)=delta/K,  S -> infinity.

Recent first births alone imply strictly positive lower bounds on the scaled
ordinary microscopic second moment and the full mixed-state variance. In the
normalization of the supplied notes, the following conservative bounds follow:

    liminf epsilon^4 Tr[H_e^2 rho_e(t)] >= 36 delta^2 exp(-48 kappa t),
    liminf epsilon^4 Var_(rho_e(t))(H_e) >= 36 delta^2 exp(-48 kappa t).    (P1)

The proof actually gives a sharper family of lower bounds involving the full
fast no-second-birth semigroup and the evolved pre-first-birth input, given in
(P20) below. It does not require a bound on the total mean to obtain the
variance statement. It does not identify the full pointwise asymptotic of the
second moment or variance, prove a matching upper bound, establish an external
resource cost, or lower-bound mixed-state quantum Fisher information.

A shrinking recent-birth slice also has a finite positive limiting contribution
to the ordinary mean, given by (P18). That slice is not the complete mean.
In particular no normalized N=6-start ordinary-energy theorem is being
substituted for this continuously injected N=4-start ensemble.

## Frozen sources and conventions

The first three sources are read at the authorized main
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`, with these exact source hashes:

| Source | SHA256 |
| --- | --- |
| ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md | `af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718` |
| LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md | `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b` |
| BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md | `f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9` |
| ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md, explicitly permitted PR9057 source at `c234d47c9d99b7fd5590957ec08d9083877d25e6` | `4a484ec7403e3f2306454fe01cfb91cdf2a7f601d2e896aaef6307134deec28f` |

All four complete arguments were read. The optional fourth source is reused
for its weighted cluster machinery and for the exact scope of the normalized
N=6-start problem. Its author or checker code was not read or imported. The
present lower bound does not use its sharp large-fast-time tail estimate.
Applicable main AGENTS and SCIENCE_WORKFLOW were reused at reverified unchanged
hashes. The inherited model and effort were retained; no delegation occurred.

The cube has A={0,3,5,6}, B={1,2,4,7}, with edges oriented from A to B. Physical
charge/electric words obey div E=q-1_A. Records have q=0,+1,-1 with hard-core
occupancy. An outward hop F_a moves q_a=+/-1 to an empty adjacent B site and
changes the oriented edge field by -q_a. A resolved formation j_(ab,+/-)
acts only when a,b are empty, creates (+/-1,-/+1), and changes that field by
+/-1. The coherent edge mark is the stipulated sum of its two resolved
operators, without a factor of 1/sqrt(2). Finite-spin amplitudes are the
normalized spin shifts; rotor shifts have unit amplitude.

Write F=sum_a F_a, T=-(F+F*), W=sum_(a in A)(1-n_a), P=1_(W=0), and
C=S(S+1). The specified lambda=0 Hamiltonian and formation operators are

    H_e=delta epsilon^-4 [W+epsilon T_S+epsilon^2 C_S],
    L_i=sqrt(kappa) epsilon^-1 j_(i,S).                         (P2)

The gated local compensation on this cube is C_S=P(M_S+D/C)P, M_S=PF_S*F_SP,
and vanishes on W>=1. D is the nonnegative diagonal polynomial of the sources.
No electric completion outside this block is added. H_e is Hermitian; it is
not assumed nonnegative. All graph and coupling choices remain supplied.

## 1. Exact first-birth decomposition before a limit

Let H_(N,e) and Gamma_(N,S)=sum_i j_i*j_i denote restrictions to N records.
Both H and Gamma preserve N. The no-event propagator is the exact contraction

    V_(N,e)(u)=exp[u(-i H_(N,e)-kappa Gamma_(N,S)/(2epsilon^2))]. (P3)

Let U_(4,e) be the Hermitian canonical low-band column, with the positive-
overlap convention of the sources, and let Omega be the all-A-plus, zero-field
vector. Define

    xi_e(s)=V_(4,e)(s) U_(4,e) Omega,
    v_(i,e)(t,s)=V_(6,e)(t-s) j_(i,S) xi_e(s).                 (P4)

The complete N=4 and N=6 blocks of the actual density are exactly

    rho_(4,e)(t)=|xi_e(t)><xi_e(t)|,
    rho_(6,e)(t)=kappa epsilon^-2
                   sum_i integral_0^t |v_(i,e)(t,s)><v_(i,e)(t,s)| ds. (P5)

The integral has its usual quantum-jump meaning: first birth at s, mark i,
and no second birth before t. Its probability density is
`kappa epsilon^-2 ||v_(i,e)(t,s)||^2`. There is no survival normalization in
(P5). The second-birth N=8 density is another positive term in the total state;
it is obtained by the corresponding ordered two-jump integral. On that sector
every site is occupied and H=Gamma=0 exactly. Thus for p=1,2,

    Tr[H_e^p rho_e(t)]
      =<xi_e(t),H_(4,e)^p xi_e(t)>
        +kappa epsilon^-2 sum_i integral_0^t
             <v_(i,e)(t,s),H_(6,e)^p v_(i,e)(t,s)> ds.          (P6)

This is an exact identity for the full original ensemble, not an effective
replacement instrument. The N=8 contribution to the centered observable
`(H-mu)^2` is generally nonzero; it will only be discarded as a nonnegative
term in the variance lower bound. It is not mistakenly set to zero there.

For a fixed finite Lambda>0, the recent slice has s in
`[t-epsilon^2 Lambda,t]`, which is a positive interval for sufficiently small
epsilon at the fixed t>0. Changing variables to `s=t-epsilon^2 tau` cancels the
factor epsilon^-2 in (P5)-(P6). Recent slices for different Lambda are selected
only as positive terms in this identity; no physical energy measurement,
filter, or change of initial preparation is imposed.

## 2. The evolved pre-first-birth input

Denote the Hermitian cluster unitary in each N sector by V^H_(N,e), its column
on P by U_(N,e), and the no-event Riesz projectors by E_(N,k). The Hermitian
cluster projectors are P^H_(N,k). Since [Gamma,W]=0, the order-epsilon^2
projector difference caused by the imaginary loss is a contour integral of
grade-diagonal double poles and vanishes. Uniform resolvent expansions give

    E_(N,k)-P^H_(N,k)=O(epsilon^3),
    S_(N,e)=sum_k E_(N,k) P^H_(N,k)=I+O(epsilon^3).             (P7)

The exact intertwiner J_(N,e)=S_(N,e)V^H_(N,e) block diagonalizes the no-event
generator. Its condition number is uniformly bounded, and every exact block
semigroup inherits a common all-forward-time bound from the contraction (P3).
This controls nonnormality without a diagonalizability assumption.

The initially Hermitian-low vector U_(4,e)Omega therefore has only
O(epsilon^3) total high no-event coordinates. These stay O(epsilon^3) for every
bounded physical time, indeed for all later times in ordinary norm. If a_e(s)
is its exact low no-event coordinate, then

    xi_e(s)=U_(4,e) a_e(s)+r_e(s),
    sup_(0<=s<=T) ||r_e(s)||=O(epsilon^3).                     (P8)

The low no-event generator in physical time is

    A_(4,e,0)=-i K D_4-i delta H4_(4,S)
               -kappa Gamma_(B,4,S)/2+epsilon^2 R_(4,e),
    H4_(4,S)=-Z_(4,S)*Z_(4,S)/2-{M_(4,S),D_4/C}/2,
    Gamma_(B,4,S)=sum_i B_(i,S)*B_(i,S).                     (P9)

The remainder is uniformly bounded. One can obtain the imaginary coefficient
directly: in Hermitian coordinates the low loss is
`epsilon^2 P F*Gamma F P+O(epsilon^4)`, and the off-diagonal no-event blocks are
O(epsilon^3) in the dimensionless h_eff. Eliminating those blocks first changes
the low dimensionless coefficient at order epsilon^6, so it cannot alter the
displayed fourth-order imaginary term. This is the same coefficient argument
as in the authorized fast-time note, now applied to N=4.

The weighted extension needed here is controlled. Put `w=1+sum_e E_e^2`.
Every finite-hop operator and its adjoint has a uniform w-conjugated norm;
W, its projectors, and D/C commute with w. The resolvent, canonical polar, and
intertwiner series therefore have a common small-epsilon radius in ordinary
and weighted norms. The remainder in (P9) has a common weighted norm as well.
Extending spin operators by zero and using the same diagonal -iKD_4 outside
the spin box puts all low generators in a common interaction picture.
The bounded perturbation series gives

    sup_(0<=s<=T) ||w a_e(s)|| <= C_T,
    sup_(0<=s<=T) ||a_e(s)-psi_4(s)|| ->0.                    (P10)

For the second statement, normalized shifts and all fixed products converge
strongly with common bounds; the bounded interaction-picture Dyson series
converges termwise and has a uniform tail. D/C converges strongly to zero.
The initial low coordinate converges to Omega with a common weighted bound.
These facts establish (P10) without multiplying an O(epsilon) density error
by the diverging norm of H or H^2.

The rotor quantities on this first sector satisfy

    Gamma_(B,4,infinity)=48 I,
    h_4=K sum_e E_e^2-delta Z_(4,infinity)*Z_(4,infinity)/2,
    psi_4(s)=exp(-24 kappa s) exp(-i h_4 s) Omega.             (P11)

The local-compensation note gives the equivalent magnetic expression
`h_4=K sum E^2-2delta sum_faces(W_p+W_p*)-84delta I`.
The scalar affects a phase only. In particular
`||psi_4(s)||^2=exp(-48 kappa s)>0` at every fixed finite s. The surviving field
at time t is generally not Omega. It must be used in the birth source.

## 3. Source coefficients for an arbitrary evolved low field

Let i be a resolved sign or the coherent mark on an edge (a,b). On the all-A-
plus N=4 low sector define bounded finite-spin operators

    B_(i,S)=P_6 j_(i,S) F_S P_4,
    R_(i,S)=Pi_(6,1) [j_(i,S) F_S^2/2-F_S j_(i,S) F_S] P_4.

The canonical initial column and output Hermitian rotation give these
coefficients in `j_i U_(4,e)` and `V^H_(6,e)* j_i U_(4,e)`, respectively.
They are operator coefficients, not calculations restricted to Omega.

Outward F_c commute with j_i for c!=a; overlapping destination cases vanish
in both orders by hard-core occupancy. Outward F_c commute with each other,
and F_a^2=0. Since j_iP_4=0, these identities imply the exact minimal-coefficient
cancellation

    R_(i,S)=-F_(a,S) B_(i,S).                               (P12)

It includes the finite-spin weights: this argument never exchanges opposite
shifts on the same link. Compensation and low-column normalization cannot
change these minimal outward coefficients.

At rotor order the complete operator identities on the initial field Hilbert
space are

| Mark on any one edge | B_i*B_i | R_i*R_i |
| --- | --- | --- |
| resolved plus | 2I | 4I |
| resolved minus | 2I | 2I |
| coherent | 4I | 6I |

To see that these hold on arbitrary fields, there are two choices for the
first outward neighbor other than b. Their B outputs have different charge
labels and are orthogonal; each is a unitary field translation. For the plus
mark, the two remaining outward orders in R give the same charge/translation
word and add to amplitude -2. For the minus mark they have distinct charge
labels and each amplitude -1. Plus and minus outputs are mutually orthogonal
at this initial source calculation. These statements do not depend on the
starting divergence-free field or on its superposition coefficients.

Summing over the complete instruments yields, in either case,

    sum_i B_i*B_i=48 I,       sum_i R_i*R_i=72 I.              (P13)

This is a rotor identity; finite-spin source norms on an evolved field are
not asserted to equal these constants. Uniform bounds and strong convergence
of B_(i,S),R_(i,S), together with (P10), supply their limiting use.

Every R_i output has its A vacancy at a and its B vacancy at the opposite
cube vertex. It is initially dark under every original formation. This does
not permit omission of the loss at subsequent times: the complete fast
Hamiltonian can move the vacancies. Nor does equal loss identify resolved
and coherent source densities. For a coherent mark, R_i=R_++R_- must remain
inside the same propagated vector.

## 4. The exact recent-birth fast layer

On the complete physical N=6, W=1 rotor space put

    G_1=Pi_1(FF*-F*F)Pi_1,
    Gamma_1=Pi_1 sum_i j_i*j_i Pi_1,
    A_1=-i delta G_1-kappa Gamma_1/2.                        (P14)

These are the full operators on physical charge/electric words, not one
Fourier phase or the low-sector Hamiltonian. The relative minus sign between
the two virtual denominators is retained. Resolved and coherent instruments
have the same Gamma because j_+*j_-=0, but their propagated recycling/source
densities need not agree.

For fixed Lambda and t, (P7)-(P12) and the no-event cluster expansion give,
uniformly on 0<=tau<=Lambda, with s=t-epsilon^2 tau,

    first high Hermitian coordinate of v_(i,e)(t,s)
      =epsilon^2 exp(-i delta tau/epsilon^2)
          exp(tau A_(1,S)) R_(i,S) a_e(s)+O(epsilon^3),
    second high coordinate=O(epsilon^3),
    low coordinate=O(epsilon).                              (P15)

The first high generator after removing its scalar phase is
`A_(1,S)+O(epsilon^2)` in fast time, uniformly in S. Duhamel on a fixed tau
interval controls this error; exact no-event contraction and bounded
intertwiners control propagation of the O(epsilon^3) pre-first-birth remainder.
The Hermitian versus no-event coordinate error on a vector of norm O(epsilon)
is only O(epsilon^4), smaller than the displayed conservative remainder.
The second high coordinate estimate already suffices here; the stronger
special N=6-start cancellation from PR9057 is not required.

The low part can be decomposed into a leading vector with weighted norm
O(epsilon), and an ordinary-norm O(epsilon^3) remainder. The exact low
Hamiltonian is KD_6+delta H4_(6,S)+O(epsilon^2), has weighted action bounded
on the leading vector, and ordinary norm O(epsilon^-2). Its contribution to
`<v,Hv>` is therefore O(epsilon^2). Its squared-energy-vector contribution is
also negligible after multiplying by epsilon^4. This avoids requiring a
weighted bound on the whole fast high component.

The high Hermitian energy blocks are
`delta epsilon^-4[kI+O(epsilon^2)]`, k=1,2. Their cross terms vanish exactly
in energy moments, since these are orthogonal Hermitian spectral blocks.
Strong convergence of the bounded fast operators and their exponential
series, (P10), and uniform continuity of psi_4 on its compact time orbit imply

    epsilon^-2 ||v_(i,e)(t,t-epsilon^2 tau)||^2
                         -> b_i exp(-48 kappa t),
    <v_(i,e),H_(6,e) v_(i,e)>
                         -> delta f_(i,t)(tau),
    epsilon^4 ||H_(6,e) v_(i,e)||^2
                         -> delta^2 f_(i,t)(tau),             (P16)

uniformly on each such tau interval, where

    f_(i,t)(tau)=||exp(tau A_1) R_i psi_4(t)||^2,
    F_t(tau)=sum_(i in the original complete instrument) f_(i,t)(tau).

Here b_i=2,2,4 as appropriate. Equation (P16) retains exact microscopic
no-second-birth evolution before taking its fast limit. It neither resets
the evolved pre-first-birth field to zero nor freezes the fast generator.

In particular

    F_t(0)=72 exp(-48 kappa t).                              (P17)

For a coherent instrument, its f contains the coherent sum before propagation;
no equality of F_t between the two instruments at positive tau is assumed.

## 5. Recent-slice moments and the mixed-variance lower bound

Let M_(p,recent,e)(t;Lambda) be the contribution of the recent portion of (P6).
The change of variables following (P6) and uniform convergence in (P16) give

    M_(1,recent,e)(t;Lambda)
                      -> kappa delta integral_0^Lambda F_t(tau) d tau,
    epsilon^4 M_(2,recent,e)(t;Lambda)
                      -> kappa delta^2 integral_0^Lambda F_t(tau) d tau. (P18)

For the second moment, every omitted density contribution is nonnegative
when tested against H^2. The first relation is an additive slice identity
only, since H need not be nonnegative.

For variance, write mu_e=Tr[H_e rho_e(t)], allowing it to depend on epsilon
arbitrarily. Positivity of the ensemble decomposition gives

    Var_(rho_e)(H_e)
       >=kappa epsilon^-2 sum_i integral_recent
             ||(H_(6,e)-mu_e)v_(i,e)(t,s)||^2 ds
       >=kappa epsilon^-2 sum_i integral_recent
          [ ||H_(6,e)v_(i,e)||^2
             - |<v_(i,e),H_(6,e)v_(i,e)>|^2/||v_(i,e)||^2 ] ds. (P19)

The second inequality minimizes each quadratic over an arbitrary real center;
it is the variance concavity identity for an unconditioned mixture, including
a continuous birth-time decomposition. It does not assume those branch vectors
are orthogonal or that the total mean is bounded. For each fixed t,Lambda,
the first line of (P16) bounds the denominator below by a positive constant
times epsilon^2, while the mean numerator is uniformly O(1). Consequently
the subtracted term is O(epsilon^-2), negligible after the epsilon^4 scaling.

Combining (P18)-(P19), for every fixed finite Lambda>0,

    liminf epsilon^4 Tr[H_e^2 rho_e(t)]
       >= kappa delta^2 integral_0^Lambda F_t(tau) d tau,
    liminf epsilon^4 Var_(rho_e(t))(H_e)
       >= kappa delta^2 integral_0^Lambda F_t(tau) d tau.       (P20)

The integrand is positive near zero by (P17) and bounded-operator continuity,
already proving a strict lower bound without a long-time classification.
There is also a simple explicit conservative constant. A W=1,N=6 charge word
has one A vacancy and one B vacancy. If they are adjacent, precisely their
two resolved signs can form; if they are not adjacent, none can. The rotor
loss is therefore `Gamma_1=2 Pi_bright`, for either complete instrument. Thus

    d/dtau ||exp(tau A_1)v||^2
        =-kappa <exp(tau A_1)v,Gamma_1 exp(tau A_1)v>
        >=-2kappa ||exp(tau A_1)v||^2,
    F_t(tau)>=72 exp(-48 kappa t) exp(-2kappa tau).             (P21)

This inequality retains G_1; it uses only its Hermiticity, not an assumption
that it vanishes or commutes with the loss. Equations (P20)-(P21) give

    both liminfs >=36 delta^2 exp(-48 kappa t)
                              [1-exp(-2kappa Lambda)].       (P22)

Taking the supremum over finite Lambda after the epsilon limit proves (P1).
No uniform microscopic approximation on tau up to infinity has been invoked.
The bound is deliberately non-sharp and is not uniform as kappa tends to zero:
kappa>0 is fixed before both limiting operations.

## 6. Distinctions and unresolved questions

1. **N=4 ensemble versus a normalized N=6 start.** The earlier ordinary-energy
   result prepares a specified normalized actual first output at time zero,
   then studies its later evolution. Here first births are continuously
   injected. At a fixed observation time t, the contributing ages in this
   proof are epsilon^2 tau and shrink to zero. A normalized N=6 theorem at
   fixed positive age cannot be substituted into this boundary layer, or
   integrated over birth times without a suitable dominating estimate.

2. **Mixed variance versus Fisher coherence.** (P1) is a lower bound on the
   ordinary variance of the microscopic Hermitian H in a mixed GKLS state.
   Quantum Fisher information for unitary H encoding satisfies F_Q<=4 Var,
   with equality on a pure state; a variance lower bound does not reverse
   this inequality. For example, with H=diag(0,delta epsilon^-4) and
   rho=diag(1-epsilon^4,epsilon^4), the mean is delta and the variance is
   delta^2(epsilon^-4-1), while [rho,H]=0 and F_Q=0 exactly. This example does
   not claim the actual ensemble is diagonal; it rules out that inference
   from its variance alone. No actual Fisher-coherence or apparatus-cost
   conclusion follows from the present argument.

3. **Lower bound versus complete asymptotics.** Older first births and the
   pre-first-birth block were omitted only for positive second-moment or
   centered-square inequalities. They may add a leading or larger contribution.
   A matching upper bound, a full pointwise coefficient, and the behavior of
   the complete mean require estimates over ages up to t/epsilon^2 and suitable
   source-dependent weighted bounds. Neither (P16) nor the normalized-input
   PR9057 theorem supplies that interchange automatically. No claim of
   `Var=Theta(epsilon^-4)` is made here.

4. **Uniformity and order.** The graph, t>0, finite upper physical horizon T,
   delta,K,kappa, and original instrument are fixed. Analytic remainder bounds
   are uniform in S; low input convergence is uniform on [0,T]; recent fast
   estimates are uniform only on fixed [0,Lambda]. First epsilon tends to zero
   along the specified integer-spin sequence. Only then may one take the
   supremum over finite Lambda. No microscopic initial-derivative limit,
   moving high-flux input, joint t->0 or t->infinity uniformity, or growing
   graph statement is used.

5. **Supplied hypotheses.** The canonical Hermitian preparation, local gated
   compensation, spin shifts, original quantum-jump instrument, lambda=0,
   coupling relation and time parameter remain model inputs. The proof uses
   the actual microscopic H and exact waiting dynamics; it supplies no bath,
   battery, external energy balance, native field selection, or resource bound.

No unresolved mathematical step is being hidden behind density convergence:
the necessary source expansion, uniform block comparison, weighted low-input
control, and positive-mixture variance estimate are given above. Their parent
operator definitions and analytic hypotheses remain conditional imports. A
released candidate would still need to be checked against these exact
uniformities and distinctions, particularly if it proposes an upper bound or
a full asymptotic beyond this PRE.

## 7. Limited independent evidence and failure record

`primitive_source_check.py` is an independent standard-library exact-word
program. It starts from charges, A-to-B link shifts, and hard-core actions;
it imports no author builder. It verifies all 36 edge/sign/coherent source
identities, (P12), Gauss preservation, and the Laurent-polynomial identities
B_i*B_i=b_i I and R_i*R_i=r_i I. Testing the complete translation polynomial,
rather than one vector norm alone, establishes the control's arbitrary-field
meaning. It verifies all sources are initially dark, and rejects removal of
the factor 1/2 in their canonical coefficient.

The same small control enumerates the 96 first-high charge labels, yielding
72 bright and 24 dark labels and loss maximum two. This latter enumeration is
a charge-label check of the diagonal rotor loss; its dummy zero field is not
asserted to satisfy Gauss for every charge label. Each such physical charge
label admits a field solution, and the rotor loss depends only on vacancy
adjacency. Source word checks themselves impose Gauss explicitly.

The control also shows that replacing a coherent source by the two resolved
source densities changes the one-edge density: the squared Hilbert-Schmidt
norm of their difference on the zero-field input is exactly 16. Equal total
source norm alone is therefore not a license to change the instrument.

All exact checks completed successfully; stderr is empty. The complete log
and result JSON are retained. No large existing numerical calculation was
repeated. These primitive checks support the local coefficient algebra, not
the analytic uniform-time argument or a numerical test of the full GKLS limit.

The rejected reasoning routes are preserved explicitly: multiplying a trace-
norm approximation by H^2; reusing the zero-field fast curve for the evolved
input without its source operator; freezing the fast Hamiltonian; replacing
a coherent mark by a resolved mixture; extrapolating fixed-Lambda convergence
to all ages; and treating mixed variance as Fisher coherence or an external
resource cost. No computational failure was discarded or overwritten.

This PRE and its complete permitted source/evidence packet are sealed before
any root candidate release. No publication, audit, axiom, branch, or other
checker packet was modified.
