# Static positive two-body active-energy SWAP with a product reference

New ROOT author derivation, requiring a distinct check. A single static Hamiltonian on freely degenerate Q, active P with literal free term omega nP, and N equal-gap reference qubits approximates the COMPLETE SWAP_QP with all reference outputs retained. This extends the standalone active-P rotation to the full two-data-qubit swap component. It is NOT the complete path/record loader, fixed-range lattice implementation, native preparation, permanent halt or reset. The interaction graph contains a degree-N reference star and the phase-aligned product reference is supplied.

## 1. Full-space Hamiltonian and positive blocks

Take omega>0, lambda>0 and integer N>=1. Set

    a=lambda/sqrt(2), b=sqrt(5)lambda/4, c=3lambda/4,
    g=sqrt(2)lambda=2a,
    HE=omega(nP+sum_j nBj), beta=|+>^tensor N.

Q has no free-energy term; P and each Bj have equal gap omega. Supply the following separately listed interaction blocks:

    a(I+XQ), b(I+ZQ), b(I+ZP), c(I+ZQ ZP),
    h_j=(g/N)(I+sigmaP+ sigmaBj-+sigmaP- sigmaBj+), j=1..N.

Every displayed block is real, positive and at most two-body on its COMPLETE support. The first four have norms2a,2b,2b,2c. Each exchange block has eigenvalues0,g/N,g/N,2g/N and norm2g/N. The free occupations are positive onsite blocks of norm omega. No low-energy-sector positivity or hidden many-body coupling is used.

Write

    HS=a XQ+b(ZQ+ZP)+c ZQ ZP,
    V=(g/N)sum_j(exchange_PBj),
    s=a+2b+c+g=lambda(3/sqrt(2)+sqrt(5)/2+3/4).

The literal installed Hamiltonian is H=HE+sI+HS+V. All interaction blocks commute with HE, including the exchanges because they preserve nP+nBj. Hence

    exp(-itH)=exp(-ist) exp(-itHE) exp[-it(HS+V)].       (1)

The terms inside HS+V need not commute with one another. In particular no sequential gates or switched couplings are invoked. The scalar s is the sum of actual positive identity shifts and is retained exactly once.

## 2. Exact effective two-qubit gate

The analytical comparison replaces V by V0=a XP. Define

    Heff=a(XQ+XP)+b(ZQ+ZP)+c ZQ ZP.                    (2)

This is a comparison operator, not an additional installed energy-nonconserving drive. Let |S>=(|01>-|10>)/sqrt(2). Its eigenvalue under Heff is -c=-3lambda/4. The orthogonal symmetric subspace is ordered |00>,|T>=(|01>+|10>)/sqrt(2),|11>. On this subspace (Heff+cI)/lambda is

    M=[[ (3+sqrt(5))/2, 1, 0 ],
       [ 1,                 0, 1 ],
       [ 0,                 1, (3-sqrt(5))/2 ]].        (3)

Its trace is3; sum of principal2x2 minors is -1 because the product of the two corner diagonal entries is1 and the two unit offdiagonals contribute -2. Its determinant is -3. Thus det(xI-M)=x^3-3x^2-x+3=(x-3)(x-1)(x+1). The exact triplet eigenvalues of Heff are lambda times{-7/4,1/4,9/4}. Along with singlet -3lambda/4 this gives ||Heff||=9lambda/4.

At tau=pi/lambda the triplet evolution has common phase exp(-i pi/4), since its three eigenvalues differ by even multiples of lambda. The singlet phase is exp(+3i pi/4)=-exp(-i pi/4). SWAP has eigenvalue+1 on the triplet and-1 on the singlet. Therefore the exact full-four-dimensional identity is

    exp(-i tau Heff)=exp(-i pi/4) SWAP_QP.             (4)

This checks every coherent input and relative phase, not only two transferred basis vectors. It uses an explicit characteristic polynomial, not a fitted numerical spectrum. No claim of novelty for static spin-gate synthesis is made.

## 3. Full-output product-reference residual

Let E_beta insert beta while retaining arbitrary QP and passive reference input. On beta, sum X_B=N and the vectors Y_Bj beta have zero cross inner products and unit norm. The exchange identity gives

    V=(g/(2N))(XP sum X_B+YP sum Y_B).

Thus

    (V-V0)(psi tensor beta)=(g/(2N)) YP psi tensor sum Y_Bj beta,
    ||(V-V0)(psi tensor beta)||=g/(2sqrt(N)) ||psi||.    (5)

The statement is exact and dimension independent on the entire QP/passive-reference input. The comparison evolution exp(-itHeff) leaves the reference factor beta, even when it entangles Q and P. Equation5 holds on every resulting data vector. Duhamel along this comparison trajectory therefore yields

    ||exp[-it(HS+V)]E_beta-(exp(-itHeff) tensor I)E_beta||
       <=g|t|/(2sqrt(N)).                              (6)

This does not bound V-V0 on the whole Hilbert space, presume the ACTUAL state remains product, discard reference entanglement, or reset the reference along the path. After multiplication by the exact free/scalar factors in1, the complete comparator is

    A_t psi=exp(-ist) [exp(-it omega nP) exp(-itHeff)psi]
                          tensor beta(t),
    beta(t)=(exp(-it omega n)|+>)^tensor N.              (7)

The order of data factors matters. HE does not commute with Heff; only its commutation with the ACTUAL HS+V was used to obtain1.

## 4. Revival, complete SWAP and finite window

Choose integer m>=1 and lambda=omega/(2m). Then tau=pi/lambda=2pi m/omega is an exact full free-energy revival. Equations4,6,7 imply

    ||exp(-i tau H)E_beta
       -exp[-i(s tau+pi/4)](SWAP_QP tensor beta)||
       <=pi/sqrt(2N).                                 (8)

The scalar phase is explicit and independent of input. All N reference outputs and arbitrary passive references are included. Approximation to a returning beta is not exact restoration of its energy moments or authorization of repeated use.

For t=tau+Delta>=0 use the normalized comparator

    B_t psi=exp[-i(st+pi/4)] SWAP_QP psi tensor beta(t).

The factor exp(-it omega nP) differs from identity by at most omega|Delta| because tau is a revival. The effective evolution differs from its tau value by at most ||Heff|| |Delta|=(9lambda/4)|Delta|. Without commuting these two factors, the triangle inequality gives

    ||exp(-itH)E_beta-B_t||
       <=gt/(2sqrt(N))+(omega+9lambda/4)|Delta|.        (9)

For0<epsilon<=1 take

    N>=ceil(512 pi^2/epsilon^2),
    w=epsilon/[32(omega+9lambda/4)], I=[tau-w,tau+w].

Here w<tau, hence all times are positive and t<2tau. The first term in9 is strictly below g tau/sqrt(N)=sqrt(2)pi/sqrt(N)<=epsilon/16; the second is <=epsilon/32. Thus uniformly on the closed window the COMPLETE induced vector error is <3epsilon/32 and unhalved stabilized complete-output channel error is <3epsilon/16. At the center8 gives the sharper ceiling epsilon/32. No postselection or input-dependent success probability is used. The reference is beta(t), not frozen beta throughout this interval. The scalar phase is also retained throughout.

Relative width2w/tau=epsilon lambda/[16pi(omega+9lambda/4)] shrinks linearly with epsilon at fixed m. This is finite-window operation under a supplied static Hamiltonian, not a record/capture/halt mechanism.

## 5. Literal resources and incident cap

There are N+2 physical qubits. The N reference exchanges plus four other interaction blocks and N+1 free occupations give2N+5 separately listed positive blocks. Full-support incident loads are

    load(Q)=2a+2b+2c=lambda[sqrt(2)+(sqrt(5)+3)/2],
    load(P)=omega+2b+2c+2g=omega+lambda C,
    load(Bj)=omega+2g/N,
    C=(sqrt(5)+3)/2+2sqrt(2).

For any Lambda>omega choose

    m>=max{1,ceil[omega C/(2(Lambda-omega))]},
    lambda=omega/(2m).

Then load(P)<=Lambda. Its interaction coefficient exceeds the Q coefficient and the reference coefficient2sqrt(2)/N, so both other loads are also <=Lambda. This counts full identity shifts and active free onsite terms, with no subspace subtraction. The physical time is tau=2pi m/omega; increasing N improves the error at fixed m but increases reference size and degree. Exact exchange coefficientg/N shrinks with N. This is not a permitted error tolerance.

The reference free-energy mean is N omega/2 and maximum N omega, supplied through phase-coherent |+> factors. Data energy exchange is exactly balanced by the actual reference under [H,HE]=0. Complete-state closeness alone does not imply equal reference energy moments in a family with growing energy norm. The always-on reference interactions meet the same P, so its degree grows as N. No fixed-range embedding in fixed dimension, native coefficient/state supply, suppression of stray terms, thermal preparation or reset is derived.

## 6. Scope and evidence

The new result is a standalone full QP SWAP component with an active omega nP, static positive real two-body blocks, and supplied product reference. It removes the requirement that P be freely degenerate for THIS component; Q remains degenerate. The original physical loader also contains path/record operations and head propagation, and these have not been autonomously composed with this Hamiltonian. An arbitrary active H_PE and the historical Record identification are not handled. No exact early-record correctness, prior loader runtime, permanent halt, storage or reuse follows.

Source exposure: the checked standalone rotation product_reference_two_body_rotation/PROPOSAL.md9354342473198de039f429e55077b628db10c687aefc7eddfdd64b896f1f41fb and check0f5a7fc787a1f228316ad98179443fbeb62202fdd37f69f8bbd7493e69028e36 motivated the residual mechanism. ROOT retained full reads; the residual was re-derived here with arbitrary QP rather than P alone. The exact spin-one characteristic-polynomial construction in2-4 and the complete composition/cap/window are new author calculations. A separate agent's preliminary static three-qubit pair-exchange report suggested commensurate spectra as an avenue, but none of its unpublished formulas or proof is a premise of this result. All load-bearing algebra is displayed here.

This source requires distinct independent calculation with exact exposure disclosed, especially triplet/singlet phases, the actual-vs-comparison energy commutation and full-support load. No mathematical solver, numerical simulation, scientific execution or retained audit has been performed for this new note. Only this proposal was written; no editable prompt, axiom, Git, model or existing source changed.
