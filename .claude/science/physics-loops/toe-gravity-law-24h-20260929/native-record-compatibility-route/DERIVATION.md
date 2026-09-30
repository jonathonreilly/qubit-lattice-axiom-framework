# Actual local memory algebra and an irreversible-formation test

Author discovery proof; focused independent checking is required before downstream use. The precise optional memory realizations below are supplied conditions, not definitions forced by the current Record axiom. H0 is exactly equation (3) of the landed native density-onset note. mu,tau>0. The conclusions also hold with an arbitrary onsite chemical potential -nu N where explicitly stated. No phase, physical clock, Born rule, or axiom inconsistency is inferred.

## 1. An exposed four-site transport coefficient

Write b_x=|0><1| and use the original commuting site factors. In the E pair plane the Gram matrix on the three axial words is

    G_E=I_3-(1/3)11^T.

This follows directly from the coefficients (1,-1,0)/sqrt(2) and (1,1,-2)/sqrt(6). In particular the d_1-to-d_1 coefficient in sum_A Q_A(y)^dagger Q_A(x) is 2/3. The T words have endpoints on different axes and cannot equal an opposite axial pair.

Let v be a lattice site and denote v+j e_1 by j for this paragraph. In the full Hamiltonian the complete term on the four distinct collinear sites 0,1,2,3, with a nonidentity raising/lowering operator at each site, is exactly

    -(2 tau/3)(b_1^dagger b_3^dagger b_0 b_2
                      +b_0^dagger b_2^dagger b_1 b_3).       (1)

The pair centers are v+e_1 and v+2e_1. The gradient expansion contributes -tau in each direction once. A pair with endpoints separated by 2e_1 has only its axial midpoint as center, so no other pair gradient has these input/output pairs. A same-center collective square has support inside one unit star and cannot contain all four collinear sites. The onsite term has one-site support, and V3 has three-site support. They cannot alter (1), even after an onsite basis change. No other four-flip word on these same four collinear sites is present.

There is a stronger half-space coefficient statement. Let O have finite support S in {x_1<=v_1}, with v in S. In the tensor expansion of [H0,O], take the coefficient of the outside operator

    b_(v+e1)^dagger b_(v+2e1) b_(v+3e1)^dagger,            (2)

and identity on every other site outside S. This coefficient is

    -(2 tau/3)[b_v,O].                                   (3)

To check uniqueness rather than presume it, an exterior creation pair at v+e1,v+3e1 forces its center to v+2e1 and the E component. Its other center is one nearest-neighbor step away. For its annihilation pair to contain v+2e1 and a point in {x_1<=v_1}, the other center must be v+e1 and the other endpoint must be v. Every other possible center/end point remains strictly outside that half-space. Monomials with all factors outside S commute with O. Overlapping input/output pairs have at most two offdiagonal site factors and cannot match (2). The diagonal V3 cannot match even one such factor. Conjugating (2) gives the corresponding coefficient -(2 tau/3)[b_v^dagger,O].

These coefficient extractions use the linearly independent one-site basis I,n,b,b^dagger on the exterior. They do not replace n by its trace or identify a selected particle sector with the full carrier. For infinite Z3 only finitely many Hamiltonian terms meet S, so the commutator and extraction are finite algebraic expressions. A periodic version is identical whenever the support is contained in a box with four empty collar planes on either side before periodic identification; no optimal minimum torus size is claimed.

## 2. Full strictly local commutant

**Theorem A.** On the full physical tensor carrier, every finite-support operator O with [H0,O]=0 is scalar. Equivalently the intersection of the exact Hamiltonian fixed algebra with the strictly local algebra is C I. The same statement holds for H0-nu N at any real nu. On sufficiently large tori this holds for operators supported in the unaliased local domain just described, not for arbitrary global operators.

Proof. Choose the maximal first-coordinate plane of S. For each v in that plane, (3) and its conjugate show that O commutes with b_v and b_v^dagger. Those two matrices generate M2 at v. Writing O as a 2 by 2 block matrix at v immediately gives O=I_v tensor O_rest. Remove every site of that plane from the support. Repeat on the next maximal plane. Finitely many steps leave a scalar. The chemical-potential term has no three exterior offdiagonal factors and does not change the extraction. QED.

This is stronger than computing [H0,n_v]. It tests all local matrix directions, arbitrary finite blocks and coherences, including operators which change particle number. It does not assume that O commutes separately with each interaction term. Global N, parity and spectral functions are outside the support condition. Operators with genuinely infinite tails and quantities conserved only on a restricted state domain are also outside it.

For a finite torus, a fixed local sharp record projector required to be permanent under the unitary dynamics on its entire range must commute with H0: invariance of that finite-dimensional range under every positive-time unitary makes it reducing. Theorem A therefore excludes a nontrivial such projector in every bounded support block. Likewise an exactly stationary finite-support POVM effect on all states is scalar. This is a conditional sharp/static-readout statement, not a derivation of how the axiom must be represented.

## 3. Why arbitrary Markov loss cannot repair a common site marker

Supply a continuous finite-dimensional quantum Markov semigroup on a finite torus with generator

    L(rho)=-i[H0,rho]+sum_j (L_j rho L_j^dagger
                                  -{L_j^dagger L_j,rho}/2).       (4)

The jumps may be arbitrary bounded operators; they need not be local, number preserving, or weak. There may be any finite number of them. This is a stronger allowed noise family than a finite-range repair. For any fixed basis {|0_r>,|1_r>} common to all sites, put P_x=|1_r><1_r|_x.

The supplied **all-state formed-marker persistence condition** is: for every site x, every positive rho supported in P_x, and every t>=0, exp(tL)rho is still supported in P_x. The complementary blank sector is allowed to gain a marker. Only the one formed content |1_r> is required persistent; two permanent outcomes at each site are not assumed.

For any invariant projector P, define M=sum L_j^dagger L_j and K=-iH0-M/2. Testing the leakage derivative on rho=|psi><psi| with psi in ran P gives

    0=sum_j ||(I-P)L_j psi||^2.

Hence (I-P)L_j P=0 for every jump. The offdiagonal block of L(rho) must also vanish, yielding

    (I-P)K P=0.                                         (5)

This retains the possible cancellation of H0 by the no-event loss. Dropping M from (5) would be invalid in general.

If every P_x is invariant, (5) forces K_mn=0 whenever the product pattern m loses any occupied record of n. For two distinct incomparable patterns m,n, both K_mn and K_nm vanish. Since both H0 and M are Hermitian,

    -i H_mn-M_mn/2=0,   i H_mn-M_mn/2=0,

so H_mn=0. Thus no-event loss cannot cancel a coherent coupling in both directions between incomparable record patterns.

For the actual H0 choose the four sites in (1), and patterns n=1010 and m=0101 in the common r basis, with identical arbitrary product spectators. Every other Hamiltonian term acts on at most three of these four sites, or has different support, so its matrix element between these patterns is zero. Write

    a=<0_r|b|1_r>, d=<1_r|b|0_r>.

Equation (1) gives exactly

    <m|H0|n>=-(2 tau/3)(|a|^4+|d|^4).                    (6)

For any orthonormal qubit basis, |a|=t and |d|=1-t for a t in [0,1]. Thus t^4+(1-t)^4>=1/8, and

    |<m|H0|n>|>=tau/12>0.                               (7)

The phases cancel in the displayed products. mu, V3 and -nu N do not enter this four-flip matrix element. Taking a sufficiently large torus avoids wrapping coincidences. The two patterns are incomparable even though each has only two formed markers.

**Theorem B.** No semigroup (4) can satisfy the all-state formed-marker persistence condition for one common rank-one site basis on the full carrier. This includes irreversible birth noise and nonlocal noise, at any finite strength, and does not require the blank projector to be stationary. It is not merely a unitary commutator test.

The Lindblad representation has a Hamiltonian gauge freedom, so “retaining H0” needs care. Under the putative persistence condition, every jump has zero matrix element between either orientation of the incomparable pair, since it loses an existing marker. Adding a scalar identity to a jump can shift the Hamiltonian only by a linear combination of that jump, its adjoint, and identity. Such a gauge shift has zero matrix element on this pair. Mixing jump labels also does not change this conclusion. The nonzero witness (6) cannot therefore be hidden by a permissible representation change of a semigroup obeying the persistence condition. Adding an actual coherent feedback term that cancels (1) changes the supplied Hamiltonian and lies outside the theorem.

The condition is deliberately strong in its state domain and deliberately weak in its noise class. It says every state having an already formed local marker must preserve it, with arbitrary environment correlations. A process defined only on a smaller admissible state domain need not obey it. A site-dependent basis, a migrating record identity, a multi-site code with a restricted range, time-discrete readout, non-Markov history, and an infinite-rate limiting protocol have not been classified by Theorem B. Theorem A still applies to a genuinely conserved full-carrier finite-support operator regardless of basis.

## 4. A substantial restricted-domain countercontrol

Let G be the actual eighteen-neighbor pair graph. Let C_ind be the span of every physical occupation word whose occupied sites form an independent set of G. This is a subspace of the unchanged full M2 carrier, not an isometry to a pair gas. Every bare pair annihilator, and hence every Q_A(x), kills C_ind. The pair gradient differences also kill it. Every occupied site has m_x=0, so V3 kills it. Therefore

    H0|_(C_ind)=mu N|_(C_ind).                            (8)

The occupation projectors preserve this subspace and commute with its restricted dynamics. They are exact local memories there, including on coherent superpositions and references. On tori divisible by three, arbitrary occupations of the sublattice (3Z)^3 give a 2^(V/27)-dimensional example. The memory is extensive; it is not restricted to the single-particle sector. Every nonvacuum fixed-N vector in this code has energy mu N. This does not represent the low-energy collective pair states or establish the dilute thermodynamic phase as a record medium.

A separately supplied local formation law can even keep the same Hamiltonian while operating on this restricted domain. Define

    J_x=sqrt(gamma) b_x^dagger product_(y:x~_G y)(1-n_y),
    L_ind=-i[H0, .]+sum_x D[J_x], gamma>0.                (9)

On C_ind, each allowed jump adds exactly one previously absent marker with no occupied graph neighbor. Each no-event loss J_x^dagger J_x is diagonal. Consequently C_ind is invariant, old occupied sites remain occupied in every trajectory, and the natural original jump label is just the new site. Starting from Omega gives a monotone random independent-set growth law on the same physical qubits. No extra physical storage factor has been introduced, although the CP/Born law and classical observation of the jumps are supplied mathematical structure. Its rates and selected basis are additional inputs, and its range-two guard is not the axioms' unspecified nearest-neighbor conditional distribution rule.

Equation (9) is only a constructive one-content marker model. It does not provide distinct readable contents or justify treating the blank/no-click branch as a readable value. It does not supply the actual framework Admissibility rule, a physical clock, or a source/readout identification. It illustrates the precise failure of extending Theorem B outside its all-state domain: configurations with conflicting occupied graph neighbors are not preparation states of this restricted memory process. The full-carrier semigroup (9) cannot make the site projectors absorbing on all states, consistently with Theorem B.

## 5. Expected independent finite controls, before execution

The proof is analytic. A small sparse control will independently expand the literal five collective pair templates using rational Gram coefficients, without importing previous builders. Expected facts derived above:

1. The full four-collinear-site, four-flip catalog contains only (1), with coefficient pair (mu coefficient 0, tau coefficient -2/3) in each direction.
2. Exterior string (2) in the x_1>0 half-space has just the remaining operator b_0, with the same coefficient; its conjugate isolates b_0^dagger.
3. Literal four-site matrix elements in the original, real rationally rotated, and balanced bases agree with (6); the balanced basis attains tau/12. Deleting pair mobility removes this witness, so tau>0 is load-bearing for this proof.
4. Literal complete-H0 action on small independent-set occupation configurations equals mu N times that configuration. A graph-edge pair is a control outside this sufficient memory domain and need not obey (8).

Price: <=30 CPU seconds, <=90 wall seconds, <=150 MiB, single thread, deadline/STOP guard. Code and this proof must be hashed before execution; every failure is retained. No finite fixture proves the support-peeling induction or the general GKSL invariant-subspace statement.

The strongest remaining physical obligation is to specify and derive a state domain, instrument and content map that realize actual permanent readable records while retaining the collective low-energy physics. Merely calling the particle density a record, or asking for an unspecified “compatible instrument,” restates that obligation. The theorems here decide two explicit full-carrier implementations and exhibit a real restricted-domain alternative; they do not decide every allowed completion of the framework.
