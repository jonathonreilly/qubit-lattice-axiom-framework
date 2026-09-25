# A continuing loss contribution to time-integrated microscopic variance

Personal root derivation, 2026-09-24, fifth campaign. Conditional candidate,
not independently checked or published at creation. The independent PRE is
being reconstructed without access to this file. No premise is adopted.

## 1. Target and parents

Retain the supplied compensated lambda=0 cube, integer spin S, C=S(S+1),
epsilon^2 C=delta/K and fixed delta,K,kappa>0. The actual canonical first
birth on edge 01 has one of the original normalized outputs phi_i. The
subsequent full original ensemble rho_i(t) includes a possible second birth.
The six-site example is not used: it cannot form that second pair.

On N=6 let

    H = delta epsilon^-4 h,
    h = W + epsilon T + epsilon^2 C_S,
    H_eff = H - i kappa Gamma_S/(2 epsilon^2),
    v(t) = exp(-it H_eff) phi_i.

Gamma_S is the original sum of marked j* j, not a replacement energy filter.
It is supported in grade W=1. The terminal N=8 Hamiltonian is exactly zero.
Consequently the full, unconditioned ensemble moments are

    m(t)=Tr(H rho_i(t))=<v(t),H v(t)>,
    M2(t)=Tr(H^2 rho_i(t))=||H v(t)||^2,
    Var_H rho_i(t)=M2(t)-m(t)^2.                           (1)

No division by no-event survival probability occurs.

Use the exact no-event low coordinate and weighted bounds from the ordinary
energy theorem in open PR #9057, at c234d47c9d99b7fd5590957ec08d9083877d25e6.
That is a provisional mathematical dependency, not retained audit authority.
Its parents provide the exact uniformly bounded Riesz intertwiners, actual
birth expansion, full original generator and common matter/field limit.

Write the limiting no-event low ket as

    u_i(t)=exp[t(-i H_rot-kappa Lambda/2)] beta_i,
    Lambda=sum_j B_j* B_j,
    B_j=j_j F_infinity P,
    H_rot=K D-delta Z_infinity* Z_infinity/2,
    beta_i=B_i/sqrt(b_i),     b_i=2,2,4.

Its survival probability S_i(t)=||u_i(t)||^2 is the no-second-birth
probability of the common effective ensemble. A first birth is already the
specified normalized initial condition. Define

    P_i(a,b)=S_i(a)-S_i(b).

This is the probability of a second birth during [a,b] in that effective
model. It is not a newly selected physical rate or apparatus.

The proposed conclusion, for every fixed 0<a<b<infinity, is

    liminf_(epsilon->0) epsilon^2
        integral_a^b Var_H rho_i(t) dt
        >= (kappa/2) P_i(a,b).                            (2)

Thus whenever the effective second-birth probability on the interval is
positive, the integrated ordinary variance is at least of order epsilon^-2.
No matching upper bound, pointwise asymptotic or finite-spin spectral gap is
asserted. Divergence of these integrals alone does not rule out pointwise
convergence along every possible sequence; concentration in time must not be
silently excluded. The conclusion is about this stated time-integrated metric.

## 2. The exact low component carries microscopic energy variance

Let E_j be the exact Riesz projections of h_eff=epsilon^4 H_eff/delta near
j=0,1,2. Choose the parent's uniformly bounded invertible intertwiner J
from the bare grade spaces Pi_j to E_j, and write

    v(t)=sum_(j=0)^2 J_j a_j(t),
    J_j=J Pi_j,   dot a_j=K_j a_j.

All norms of J,J^-1 are uniformly bounded for small epsilon. In particular
J_0=P+epsilon F_S P+O(epsilon^2), and the grade-one parity refinement gives

    Gamma_S J_0 = epsilon Gamma_S F_S P+O(epsilon^3).       (3)

The constants are uniform in S. For the main limit, O(epsilon^2) in (3)
would already suffice: after multiplication by epsilon^-1 it is o(1).
Gamma_S P=0, and the derivative of the low spectral isometry is +F_S P
because T=-(F_S+F_S*) and the low/first-high gap is one. The additional
Hermitian-to-no-event intertwiner differs from identity by O(epsilon^3),
so it does not change that leading coefficient.

The weighted low theorem gives, on every fixed [0,T],

    sup_t ||w a_0(t)|| <= C_T,
    sup_t ||a_0(t)-u_i(t)|| ->0,
    K_0=-i K D + B_epsilon,
    sup_epsilon ||B_epsilon|| < infinity,                 (4)

where w=1+sum E_e^2 and |D|<=Cw. Thus sup_t ||K_0 a_0(t)|| is uniformly
bounded. This is a vector bound on the actual low trajectory, not the false
claim that the norm of the entire low Hamiltonian is uniformly bounded.

The exact intertwining identity H_eff J_0=i J_0 K_0 gives

    H J_0 a_0 = i J_0 K_0 a_0
                 + i kappa Gamma_S J_0 a_0/(2 epsilon^2).

Multiplying by epsilon and using (3),(4), bounded strong convergence of the
normalized spin shifts and compactness of the limiting trajectory yields

    epsilon H J_0 a_0(t)
        -> i(kappa/2) Gamma_infinity F_infinity u_i(t)     (5)

uniformly on [0,T] in the common physical word Hilbert space. The first
term is O(epsilon) in norm. The second term has the displayed limit because
Gamma_S F_S is uniformly bounded and converges strongly, and the input
trajectory converges uniformly. It follows that

    epsilon^2 ||H J_0 a_0(t)||^2
        -> (kappa^2/4)||Gamma_infinity F_infinity u_i(t)||^2 (6)

uniformly. This energy contribution comes from the difference between the
physical Hermitian Hamiltonian and the no-event generator. Removing the
initial fast Riesz component does not remove it.

## 3. Rapid relative phases control integrated cross terms

It remains essential to show that the other two Riesz components cannot
cancel (6) throughout the fixed interval. They are not mutually orthogonal
in the physical energy norm. Dropping their cross terms pointwise would be
invalid. The following exact Sylvester estimate controls their integrals.

Uniform cluster expansions and grading give

    K_j=-i delta epsilon^-4 j I+R_j,
    ||R_j||<=C epsilon^-2,                  j=0,1,2.       (7)

The exact dissipative full evolution is a contraction. Since E_j commutes
with it, the actual birth estimates and bounded intertwiner imply, for all
t>=0,

    ||a_0(t)||<=C,  ||a_1(t)||<=C epsilon,
    ||a_2(t)||<=C epsilon^2.                               (8)

The stronger O(epsilon^4) second-high estimate is unnecessary here.
From H_eff J_j=i J_j K_j and (3),

    ||H J_0||<=C epsilon^-2,
    ||H J_1||+||H J_2||<=C epsilon^-4.                    (9)

The first is an operator norm on the full low space: ||K_0||=O(epsilon^-2)
on the finite spin box, while the additional loss term has norm O(epsilon^-1).
The two high estimates also follow directly from ||H||=O(epsilon^-4).

For j<k put C_jk=(H J_j)* H J_k and solve

    K_j* Y_jk+Y_jk K_k=C_jk.                              (10)

On the rectangular operator space the left map is the scalar
i delta (j-k)epsilon^-4 times identity plus an operator of norm at most
C epsilon^-2. Its inverse exists by the norm-convergent Neumann series for
small epsilon, with norm at most C epsilon^4. This works uniformly in the
growing finite dimensions and requires no diagonalizability or dissipative
gap inside a cluster. Therefore

    ||Y_01||+||Y_02||<=C epsilon^-2,
    ||Y_12||<=C epsilon^-4.                              (11)

Differentiate <a_j(t),Y_jk a_k(t)> and use (10). Exactly,

    integral_a^b <H J_j a_j(t),H J_k a_k(t)> dt
       = [<a_j(t),Y_jk a_k(t)>]_a^b.                     (12)

Combining (8),(11), these three integrals are respectively
O(epsilon^-1), O(1), O(epsilon^-1). All vanish after multiplication by
epsilon^2. There is no replacement of the actual fast propagator by its
rotor limit at a growing time.

The diagonal high-component squared norms are nonnegative. Expanding (1),
integrating and applying (6),(12) thus gives

    liminf epsilon^2 integral_a^b M2(t) dt
      >= (kappa^2/4) integral_a^b
                     ||Gamma_infinity F_infinity u_i(t)||^2 dt. (13)

This is a lower bound; the high diagonal terms need not have a limit and
are not discarded from an equality.

## 4. Relation to the second birth and to variance

On the rotor N=6 cube, Gamma_infinity=2 P_bright: an active state has exactly
one vacant A and one vacant B joined by an edge, with two original resolved
orientations of unit shift norm. The original coherent/resolved descriptions
have the same complete loss. Other grades and opposite vacancies have zero
loss. In particular

    Gamma_infinity^2=2 Gamma_infinity,
    Lambda=P F_infinity* Gamma_infinity F_infinity P,
    ||Gamma_infinity F_infinity u||^2=2<u,Lambda u>.       (14)

The effective no-event norm satisfies

    dS_i/dt=-kappa <u_i,Lambda u_i>.

Inserting (14) into (13) gives the right-hand side of (2). The ordinary
mean-energy theorem proves m(t) converges uniformly to the bounded common
matter/field energy on every fixed [a,b] with a>0. Hence

    epsilon^2 integral_a^b m(t)^2 dt ->0,

and (2) follows for the full ensemble variance. This last subtraction is
why the theorem is stated away from the initial t=0 birth layer.

The exact integer root word calculation gives, for each of plus, minus and
coherent beta_i,

    <beta_i,Lambda beta_i>=8,
    ||Gamma_infinity F_infinity beta_i||^2=16.             (15)

It constructs j_i F Omega, then every original j_j F beta_i, and verifies
the equality with the complete Gamma loss. Thus S_i'(0)=-8 kappa, and the
low-component coefficient (6) at t=0 is 4 kappa^2. These are author results
pending independent reconstruction. Continuity guarantees positive P_i(a,b)
for sufficiently early fixed 0<a<b. No unproved claim that this probability
is positive on every possible interval is needed for (2).

## 5. Limitations and review obligations

The microscopic energy is H of the supplied compensation model. This does
not identify a conserved total energy with a physical apparatus, account
for an omitted interaction, select the compensation, select Markovian time
or determine an empirical theory. Changing the instrument or postbirth
Hamiltonian changes the question. No field-only restriction is imposed.

The candidate does not solve pointwise ordinary variance, obtain its sharp
time-average asymptotic, or prove a uniform finite-spin high-block decay
rate. It does identify a possible load-bearing contribution missed by
examining only the initially populated energetic transient. The positive
lower bound is conditional and is not a universal reservoir impossibility.

Before publication: independently reconstruct (3)-(14), check the exact
original loss convention and actual input rate, exercise the nonorthogonal
cross-term calculation in separately built controls, preserve source pins,
and compare the complete final publication to its sealed evidence. A
finite example alone cannot supply the joint-limit or weighted-domain proof.
