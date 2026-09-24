# Independent PRE: microscopic cube energy at positive physical times

Sealed independent reconstruction, 2026-09-24. This is a bounded consequential
check in the supplied mathematical model, not a formal audit, a premise
adoption, or a statement about an energy reservoir. The new fifth-campaign
author argument, author files and checkpoint have not been read. The inherited
model and reasoning effort were retained; no subagent was used.

## Result reconstructed before author release

Let the original compensated, lambda=0 cube model and actual first-mark
preparation be as defined below. Along integer-spin sequences

    S -> infinity, epsilon^2 S(S+1) = delta/K,
    delta > 0, K > 0, kappa > 0 fixed,

the following result is supported by the argument in this PRE. For each
resolved plus, resolved minus or coherent first mark on edge (0,1), and every
fixed 0 < t0 <= T < infinity,

    sup_{t0 <= t <= T} |epsilon^2 Tr(H rho_i(t))/delta| -> 0,           (P1)
    sup_{t0 <= t <= T} epsilon^6 Tr(H^2 rho_i(t))/delta^2 -> 0,         (P2)
    sup_{t0 <= t <= T} epsilon^6 Var_{rho_i(t)}(H)/delta^2 -> 0.        (P3)

These are the scales of the positive first-birth coefficients, not assertions
that the unscaled mean energy or variance tends to zero or remains bounded.
No quantitative decay rate or next nonzero asymptotic coefficient follows.
The proof does not insert t/epsilon^2 into a compact-fast-time error estimate.

Two useful scope refinements follow from the same estimates. In (P2)-(P3)
the supremum may extend over every t >= t0. For all three statements a lower
endpoint a_epsilon may replace t0 when 0 <= a_epsilon <= T and
a_epsilon/epsilon^2 -> infinity; this is a consequence of a fixed waiting-time
comparison, not a growing-fast-time approximation. The mean statement here
still has a finite upper physical-time endpoint T.

## Exact model and observable definitions

The cube has A=(0,3,5,6), B=(1,2,4,7), with A-to-B links between vertices
that differ in one bit. Site charges are q=0,+1,-1, with hard-core occupancy.
The finite-spin electric fields are integers in [-S,S] on each link, obeying

    div E = q - 1_A.

An outward charge-s hop takes q_a=s,q_b=0 to q_a=0,q_b=s and changes the
A-to-B field E_ab by -s, with the normalized spin-shift coefficient. Let F_a
be the sum of outward hops from a, F=sum_a F_a, T=-(F+F*), and
W=sum_{a in A}(1-n_a). Use exactly the gated compensation C_S from the
specified local-compensation source, without an additional electric completion:

    H = delta epsilon^(-4) h,
    h = W + epsilon T + epsilon^2 C_S,
    L_j = sqrt(kappa) epsilon^(-1) j.

A resolved birth of sign s on an empty edge creates (q_a,q_b)=(s,-s), with
the original spin-shift coefficient and field change +s; a coherent edge mark
is the stipulated sum of its two resolved signs. The two signs have orthogonal
charge outputs, so j_+*j_-=0. Hence the total loss Gamma=sum_j j*j is the same
for the resolved and coherent instruments. Their recycling outputs are not
being identified.

Omega is the zero-field N=4 state with every A site positive and every B
site empty. Prepare the canonical low-band state U_epsilon Omega for this
Hamiltonian, apply the actual specified mark j_i, and normalize:

    phi_i = j_i U_epsilon Omega / ||j_i U_epsilon Omega||.

This definition supplies the time-zero postbirth state; it does not supply a
distribution of earlier waiting times. rho_i(t) is its complete GKLS ensemble,
including all allowed later births. Define

    e_epsilon(t) = epsilon^2 Tr(H rho_i(t))/delta,
    m_epsilon(t) = epsilon^6 Tr(H^2 rho_i(t))/delta^2,
    v_epsilon(t) = epsilon^6 Var_{rho_i(t)}(H)/delta^2.

On the N=6 sector W=0,1,2. P=Pi_0 denotes W=0. Set

    B_i=j_i F Omega, beta_i=B_i/sqrt(b_i), b_i=||B_i||^2,
    R_i=-F_0 B_i, r_i=R_i/sqrt(b_i), ell_i=||r_i||^2.

The notation r_i here is a vector; the prior source also uses r_i for an
unnormalized squared norm. The exact triples (b_i,||R_i||^2,ell_i) are
(2,4,2), (2,2,1), (4,6,3/2). In particular, the actual mark denominators are
nonzero for sufficiently small epsilon. All these leading vectors have fixed
finite physical-field support and are independent of S>=1.

On N=6, C_S has only its P block, with

    P C_S P = M_S+Q_S, M_S=P F*F P, Q_S=D/C, C=S(S+1),
    D(q,E)=sum_{a in A,b~a,q_b=0} E_ab(E_ab-q_a) on P.

The integer summands in D are nonnegative. On the N=6 spin box, at most six
active links occur and each summand is at most C, so ||Q_S||<=6. Extend Q_S
by zero outside the spin box in the common physical rotor P space. Then
Q_S -> 0 strongly, with this common norm bound. In fact D beta_i=0, though
the fixed-time mean proof below needs only a fixed normalizable beta_i and
the established actual-output expansion.

## 1. Exact reduction of both ensemble moments

After the first birth there can be at most one further birth on eight sites.
Its N=8 output has every site occupied, and W=F=C_S=j=0. Its Hamiltonian is
exactly zero for lambda=0, even when the field is nonzero. Therefore, with

    h_eff = h - i kappa epsilon^2 Gamma/(2 delta),
    chi(t)=exp[-i delta epsilon^(-4) t h_eff] phi_i,

the exact unnormalized no-event vector gives both full ensemble moments:

    Tr(H rho_i(t))   = <chi(t),H chi(t)>,
    Tr(H^2 rho_i(t)) = ||H chi(t)||^2.                              (1)

The full no-event propagator is contractive for all t>=0 because its
Hermitian loss is kappa Gamma/(2 epsilon^2)>=0. Formula (1) does not divide
by the no-event survival probability and does not postselect an energy band.

## 2. Uniform exact block separation and all-time control

All T,C_S,Gamma norms are uniformly bounded at this fixed graph. The integer
W gaps permit uniform contour expansions, for h and h_eff, around the three
grades. Write their projectors P_k^H and P_k^eff. They agree through order
epsilon^2. The first possible difference at order epsilon^2 is a contour
integral of (z-W)^(-1) Gamma (z-W)^(-1); since [Gamma,W]=0, it contains
only double poles and integrates to zero. Thus

    J_epsilon=sum_k P_k^eff P_k^H = I+O(epsilon^3).                  (2)

For small epsilon this is invertible, and it maps each Hermitian cluster
onto the corresponding exact no-event cluster. Let V_epsilon be the canonical
unitary that maps the W grades to the Hermitian clusters; its low column is
the same canonical U_epsilon used in the preparation. Set X=J_epsilon V.
Then X^(-1) h_eff X is exactly W-block diagonal. If E_k(t) denotes the
propagator of its k-th physical-time block, contractivity gives the bound

    ||E_k(t)|| <= c_epsilon := ||X^(-1)|| ||X|| = 1+O(epsilon^3)
                   for every t>=0 and k=0,1,2.                    (3)

This is a bound on all elapsed times, not exp[O(epsilon^2)t/epsilon^2]. It is
obtained from the exact similarity and the original contraction semigroup.

In coordinates x(t)=X^(-1)chi(t), the actual initial output has

    x_0(0)=beta_i+O(epsilon^2),
    x_1(0)=epsilon r_i+O(epsilon^3),
    x_2(0)=O(epsilon^2).                                           (4)

The uniform remainders follow from the canonical jump expansion and W
parity. One may obtain the high coefficient directly from
j F^2 Omega/2-F jF Omega=-F_0 B_i; other centers cancel. Changing from the
Hermitian to the no-event coordinates changes (4) only by O(epsilon^3).
In particular, x_2(t)=O(epsilon^2) for all t>=0.

## 3. The energetic tail is small at every later positive time

The grade-one no-event block is

    I+epsilon^2[G_{1,S}-i kappa Gamma_{1,S}/(2 delta)]+O(epsilon^4),
    G_{1,S}=Pi_1(FF*-F*F)Pi_1,
    Gamma_{1,S}=Pi_1 Gamma Pi_1.

For a fixed finite tau, bounded Duhamel estimates and (4) therefore imply

    ||x_1(epsilon^2 tau)||/epsilon
       -> ||exp[tau A_1] r_i||,
    A_1=-i delta G_1-kappa Gamma_1/2.                              (5)

The rapidly rotating scalar phase has modulus one. Equation (5) uses only
the finite-tau expansion and strong spin-to-rotor convergence on a fixed
vector. It is not asserted uniformly for tau growing with epsilon.

For every t>=epsilon^2 tau, the semigroup property and (3) instead give

    ||x_1(t)||/epsilon
       <= c_epsilon ||x_1(epsilon^2 tau)||/epsilon.                 (6)

For the rotor semigroup, ||exp[tau A_1]r_i|| -> 0 as tau->infinity. A
reconstruction of the load-bearing input is recorded below. Combining
(5)-(6), for any fixed t0>0,

    limsup_joint sup_{t>=t0} ||x_1(t)||/epsilon
       <= ||exp[tau A_1]r_i||   for every fixed tau,

and then taking tau->infinity yields

    sup_{t>=t0} ||x_1(t)|| = o(epsilon).                            (7)

For a moving lower endpoint a_epsilon with a_epsilon/epsilon^2->infinity,
the same comparison holds eventually for each fixed tau. This explains the
scope refinement without using a growing-tau approximation.

In Hermitian coordinates y=V*chi we have
y=x+O(epsilon^3)||x||. Contractivity and (3) bound ||x|| uniformly, so

    sup_{t>=t0} ||y_1(t)||=o(epsilon),
    sup_{t>=0} ||y_2(t)||=O(epsilon^2).                             (8)

## 4. The low block: strong convergence, not an energy inference from density

The low no-event block through fourth order is

    h_eff,0 = epsilon^2 Q_S
        +epsilon^4[H4_S-i kappa Gamma_{B,S}/(2 delta)]
        +O(epsilon^6),
    Gamma_{B,S}=P F* Gamma F P=sum_j B_{j,S}*B_{j,S}.               (9)

This coefficient can be checked without assuming a fixed-time limit. In
Hermitian coordinates the loss term has P compression
-i kappa epsilon^4 Gamma_{B,S}/(2 delta)+O(epsilon^6), because jP=0
and V P=P+epsilon F P+O(epsilon^2). Its off-diagonal entries are
O(epsilon^3). In these coordinates the diagonal blocks of J-I are
O(epsilon^6): for two nearby idempotents the diagonal part of their
difference is quadratic in the difference. Thus the block-removing
similarity changes a diagonal entry first at order epsilon^6. Parity removes
odd diagonal powers. The
Hermitian coefficient is

    H4_S=M_S^2-{M_S,M_S+Q_S}/2-Z_S*Z_S/2
        =-{M_S,Q_S}/2-Z_S*Z_S/2,
    Z_S=Pi_2 T Pi_1 T P.                                         (10)

Every term has a uniform norm bound. Normalized spin shifts and their
adjoints converge strongly to rotor shifts on the common physical word
space, and Q_S->0 strongly. Consequently

    H4_S -> H4_infinity=-Z_infinity*Z_infinity/2,
    Gamma_{B,S} -> Gamma_{B,infinity}                              (11)

strongly, with common bounds.

Under the joint scaling the exact physical-time low generator is therefore

    L_{0,S,epsilon}=-i K D + V_S+O(epsilon^2),
    V_S=-i delta H4_S-kappa Gamma_{B,S}/2.                         (12)

For clarity, D is the common nonnegative diagonal multiplication operator
on the full physical rotor P space. Extend the bounded V_S and the bounded
remainder by zero outside the spin box and use -i K D on that whole common
space. The box reduces this extension and its restriction is precisely the
finite-spin low block. D is self-adjoint on its multiplication domain, and
finite-support vectors form a core. No high-field moment estimate has been
inserted into the argument.

In the interaction picture of exp(-i KDt), the bounded perturbations in
(12) converge strongly with a common norm bound. The Dyson series on each
compact physical-time interval is dominated by its exponential norm series.
Convergence of each term on fixed vectors and compact-orbit approximation
give strong propagator convergence uniformly on [0,T]. With (4), this yields

    sup_{0<=t<=T} ||y_0(t)-psi_i(t)|| ->0,
    psi_i(t)=exp[t(-i(KD+delta H4_infinity)
                         -kappa Gamma_{B,infinity}/2)] beta_i.     (13)

The orbit {psi_i(t):0<=t<=T} is norm compact. Because Q_S->0 strongly and
||Q_S||<=6, a finite-net argument now gives

    sup_{0<=t<=T} ||Q_S y_0(t)|| ->0.                              (14)

This is the particular low-block control needed for the scaled mean. A
trace-norm density limit by itself would not control the diverging high
energy observable.

## 5. Moment estimates and the variance

In Hermitian coordinates h is exactly block diagonal, with uniform expansions

    h_0=epsilon^2 Q_S+epsilon^4 H4_S+O(epsilon^6),
    h_1=I+O(epsilon^2), h_2=2I+O(epsilon^2).                       (15)

Use (1), (8), and (14). The low contribution to e_epsilon is
<y_0,Q_S y_0>+O(epsilon^2), which tends uniformly to zero on [0,T]. The
high contributions are bounded by

    O(epsilon^(-2)) (||y_1||^2+||y_2||^2)=o(1)

uniformly after t0. This proves (P1) without assuming H>=0.

For the second moment,

    m_epsilon = epsilon^(-2) sum_k ||h_k y_k||^2.

The k=0 term is O(epsilon^2) using only the uniform bound on Q_S and
||chi(t)||<=1; its strong convergence is not needed. The k=1 term is
o(1) by (8), and k=2 contributes O(epsilon^2). The bounds hold for all
t>=t0 and prove (P2), including its stated all-future extension.

Finally, exactly

    v_epsilon(t)=m_epsilon(t)-epsilon^2 e_epsilon(t)^2.              (16)

The initial high amplitudes (4), the all-time bound (3), (15), and ||Q_S||<=6
give a time-uniform bound on |e_epsilon(t)| for all t>=0. Hence the subtracted
term in (16) is uniformly O(epsilon^2), proving (P3) with the same future-time
extension. No estimate of the sign of the microscopic mean was used.

## 6. Independently reconstructed rotor stability input

The new control `independent_primitives.py` was written without importing a
repo builder or runner. It enumerates charge words and derives two-hop
Laurent polynomials directly from the outward charge moves. The source facts
and expected inherited coefficients were known during this check; it is an
independent implementation/reconstruction, not a blinded discovery of them.

In N=6 there are 36,96,36 charge words at W=0,1,2. In W=1 the loss is twice
the projector onto the 72 charge words with adjacent vacancies; the other
24 are dark. The reduced incidence matrix of the seven stated tree links
has exact determinant +1. Thus every physical field for a given charge word
has a unique integer five-cycle coordinate, with the chord fields as its
coordinates. Fourier transform gives L2(T^5;C^96), not a single fiber.

At an outward charge-s hop a chord contributes its Laurent phase z_e^(-s).
The control constructs

    G(z)=F_10(z)F_10(z)*-F_21(z)*F_21(z)

by pairing paths through W=0 and W=2, keeping their opposite signs. It
verifies that the entire dark-dark Laurent block vanishes. At z_01=-1 and
all other chord phases +1, Q=P_bright G P_dark has

    det(Q^T Q)=4688333314034185078308864>0.

Therefore some 24 by 24 minor is a nonzero Laurent polynomial. Its zero
set has Haar measure zero, by the elementary one-variable root fact and
induction/Fubini in the five variables. Q(z) is injective almost everywhere.

For an imaginary-axis eigenvector of -i delta G(z)-kappa Gamma/2, its
dissipative quadratic form forces Gamma v=0. The bright part of its equation
then forces Q(z)v=0. With positive delta and kappa, this is impossible for
almost every z. Each such finite matrix has all eigenvalues in the open left
half-plane, so its exponential tends to zero. Fiber contractions and Parseval
then prove strong decay on every fixed normalizable physical input by
dominated convergence. This directly supplies the input used in (7).

The same independently constructed matrices have rank(Q)=23 at the flat
phase and annihilate the constant vector on the 24 dark words. This preserves
the distinction between strong decay and operator-norm decay: the latter is
not available and was not needed in (6)-(7). The flat fiber is not itself a
normalizable physical state.

The physical charge/field dictionary also independently checks Gauss for
every B_i and R_i word, D B_i=0, the first-mark coefficients, and

    ||G_1 R_i||^2 = 48,24,72,
    <G_1 R_i,Gamma_1 G_1 R_i> = 96,48,144.

A deliberate replacement of the relative minus sign in G by a plus sign
produces dark diagonal entries 6 instead of 0. Thus the exact cancellation
check detects a consequential sign defect; it is not an inverse-times-matrix
identity or a constant comparison alone.

Execution: `PYTHONDONTWRITEBYTECODE=1 python3 independent_primitives.py >
independent_primitives.log 2>&1`, exit 0. The complete log was inspected.
`PRIMITIVE_RESULTS.json` contains every reported finite result. These finite
checks support the stated analytic argument; no infinite-time numerical
simulation or finite-spin joint-limit numerical certification was performed.

## Edge cases, exclusions and unresolved quantities

- At t=0, e_epsilon, m_epsilon, v_epsilon tend to ell_i=2,1,3/2. Uniform
  convergence to zero on an interval containing the birth is therefore false.
  At finite fast time their leading high contribution is generally nonzero.
- delta,kappa,K remain fixed and positive. In particular kappa=0 preserves
  the high-block norm under unitary evolution and does not support this decay
  argument. No conclusion is claimed for rates moving with epsilon.
- Moving high-flux inputs, epsilon-dependent concentrations near exceptional
  Fourier phases, and leading blocked marks are not covered. The fixed
  zero-field actual first-output vectors are essential to the precise result.
- The exact ensemble reduction uses the cube's one-remaining-birth capacity
  and the zero terminal Hamiltonian at lambda=0. It must be reconsidered for
  another graph, another compensation, lambda>0, another preparation or
  another instrument.
- These statements do not supply bounded unscaled E(t), bounded unscaled
  Var(H), a decay power or exponential rate, a finite-spin infinite-time
  theorem, heat/work accounting, or a physical bath. A vanishing coefficient
  after rescaling does not establish any of those conclusions.
- The conditional prior source hypotheses are explicitly reused. Their
  unaudited status is unchanged. The PRE checks the needed perturbative
  mechanism and rotor algebra; it does not re-audit all transitive framework
  premises or reproduce the previous complete spin-one spectral runner.

## Provenance, exact sources and exposure boundary

Science checkout:
`/Users/jonreilly/Documents/Codex/physics-sync-2026-09-24-fifth/campaign-working`.
HEAD and observed origin/main both were
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`. The four assigned source hashes
were checked before reading and refreshed before preparation of this PRE.
The planning instructions were read by `git show` at refreshed
origin/ai/execution `eb1f1ca8338848cf2046582e13aef372d8540937`; no planning
files were checked out. No science, prompt, audit state, branch or published
surface was edited. All created evidence is in the assigned independent
output directory. The installed reviewer skill was byte-identical to the
source revision used here.

Full mathematical sources read and reused:

| Repository-relative source | SHA-256 | Use |
|---|---|---|
| docs/ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md | af0b8e6494ea54cdb450e430a45e9d89d9e1e931e21b9a74ab2b4ea260a3a718 | Actual output, exact terminal sector, contour expansions and compact-time starting point |
| docs/ROTOR_CUBE_FAST_ENERGY_STRONG_DECAY_WITHOUT_UNIFORM_DECAY_BOUNDED_THEOREM_NOTE_2026-09-24.md | 072d6024923f05c00f5fd1e80e1dc3952a77c773b48886bd59b7be97adc28133 | Strong-decay proof reconstructed with a new exact charge-hop implementation |
| docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md | c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b | Exact compensation, diagonal D, common physical-space representation |
| docs/BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md | f6cbeb6e0ddaa7d5a7ede3d3f3c2b7f5b22d58adeba8ef84f8aabc10599fb0f9 | Canonical fourth-order Hermitian coefficient and uniform analytic expansion |
| docs/GENERAL_MICROSCOPIC_BIRTH_ENERGY_AND_CUBE_POWER_BOUNDED_THEOREM_NOTE_2026-09-24.md | 9e13c659e9a418e9e77e619a3cbd82d371f8219003a92e49fb2cc9ac5f87d6c7 | Actual jump expansion, moment normalization and local R identity |

Additional read-only provenance sources, not imported computational machinery:

    AGENTS.md
      9bea097b409610ed70f55f53349ce206b6df7e62c63205d7775bac9b3d10dde6
    docs/ai_methodology/SCIENCE_WORKFLOW.md
      d74718214335d4feae4b40d75720482ca93bd1560a3c35174e7bf875b5b59cc4
    docs/ai_methodology/skills/SKILL_FRESHNESS_CHECK.md
      b2593401141d5f88f65feb428b8a4b2072455e038ace1cf313ecbb5a667e64b0
    docs/ai_methodology/skills/physics-claim-reviewer/SKILL.md
      9d841edd05b9dc4c5145abcfd5352cd45460a1cc57c23c1eabd131590dbb1455
    docs/ai_methodology/skills/physics-loop/references/proof-search-governance.md
      be4f955d9ff8a6f18c8f0f5fd6e872cac0ca95fcb752d86ec773961a4bb15258
    docs/ai_methodology/skills/review-loop/SKILL.md (relevant first 150 lines)
      7e977ba99c98a6cf6b7168852ce3e2055db8655f49f6f839a164d39524eea0f0
    scripts/rotor_cube_fast_energy_strong_decay_without_uniform_decay_2026_09_24.py
      0416adf91e69abb63ed5b2cd779e689b3900401513954d2b226b00b9bfe66e77
    scripts/actual_cube_birth_energy_on_the_fast_time_scale_2026_09_24.py
      e72bad34f051c6089f8480b2a5b956c9fd89db76cef77e9dd15d82e074611e9a

The two old runner wrappers were inspected for their evidence boundary, not
executed or imported. No underlying author directory, new fifth checkpoint or
fixed_time_energy_author file was read. This PRE is the independent result to
be compared only after its SHA-256 has been sealed in PRE_SEAL.json.
