# The actual gauge-matter transfer and its fixed-volume state join

Author theorem proposal, 2026-09-16; `conditional-support`. This joins the exact open-boundary Wilson determinant of current Block03 to a positive compact gauge transfer. It explicitly depends on the provisional calibration and state-limit proofs in PR8162 at frozen commit0f02dc5127416f347e231bbd8aa7c2a8b58a02fa. No independent audit or phase theorem is asserted.

## 1. Supplied model and exact finite transfer

Fix a finite free spatial cube, its oriented links and plaquettes, and supplied parameters g,kappa,m>0. Put mu=m+3kappa and r=2|Lambda_s|. The heavy-mass curl bound of Block02 additionally requires m>3kappa; the algebraic transfer construction in this note only requires m>0. The spatial lattice spacing is1. Time spacing delta and the clock order N>=3 are external regulators.

Let F_pair,delta(theta) and Omega_pair be exactly the positive paired Fock multiplier and its neutral filled state from Block03, with all scalar determinants retained. The finite clock Hilbert space has normalized counting measure on (Z/NZ)^E and the full finite paired Fock space. Define the temporal gauge kernel by the normalized integer jumps

    Q_delta,N=product_links sum_(k in Z) p_c(k) X_l^k,
    p_c(k)=exp(-c k²)/sum_j exp(-c j²),
    E_c k²=delta g²N²/(4pi²).                       (1)

There is a unique c>0. As proved in the cited prior pack, Q is positive, self-adjoint and contractive. Its angle-space matrix is also a Markov kernel with positive entries. These are two different positivity properties; both hold here by the integer-jump and Poisson formulas.

For y=delta/(2g²)<1/8 use the actual spatial Villain factor

    B_delta(theta)=product_p b_y((Ctheta)_p),
    b_y(phi)=sum_k y^(k²) exp(i k phi)/sum_k y^(k²).

This is a positive scalar bounded by1. Set

    M_delta(theta)=B_delta(theta)^(1/2) F_pair,delta(theta)^(1/2),
    T_delta,N=M_delta,N Q_delta,N M_delta,N.          (2)

Square roots are the unique positive matrix square roots. Scalar B commutes with F_pair. Thus M and T are strictly positive Hermitian. Each factor transforms covariantly under spatial gauge transformations, so T preserves the finite-clock physical Gauss space. The local paired charge is the first Fock number minus the conjugate Fock number. Neither that representation nor its Hamiltonian is inferred from the framework axioms.

The sign convention can be fixed explicitly. Let D be tail-minus-head incidence and S_chi the one-particle diagonal matrix exp(i chi_x). Then a link angle changes by theta->theta-D*chi, the Dirac matrix changes by S_chi* D_full S_chi, and the Fock multiplier by U_chi* F_pair U_chi, where U_chi=Gamma(S_chi) tensor conjugate(Gamma(S_chi)). Physical wavefunctions obey psi(theta-D*chi)=U_chi*psi(theta). On Fourier/charge basis vectors this is Dn=Q, or its congruence modulo N. Thus the incidence and matter-charge signs used below agree.

## 2. Exact open determinant, including endpoint factors

For M_t>=1 time slices, let

    v_delta(theta)=M_delta(theta) Omega_pair,
    Z_delta,N=<v_delta,T_delta,N^(M_t-1) v_delta>.   (3)

Inner products use normalized counting measure. Write q(a,b) for the matrix entries of Q in the angle basis, with sum_b q(a,b)=1. Expanding(3) gives precisely

    Z_delta,N=N^(-E) sum_(theta_0,...,theta_(M_t-1))
       [product_(t=0)^(M_t-2) q(theta_(t+1),theta_t)]
       [product_t B_delta(theta_t)]
       |det(D_full(theta) D_0^-1)|².                (4)

To see every factor, the bra v contributes a leftmost M, followed by the first M of T; at the other end the same happens to the ket. At each interior slice the adjacent T factors likewise produce M²=B F_pair. The matrix matter product therefore has the chronological order F_pair(theta_last)...F_pair(theta_first). Block03 identifies its Omega_pair matrix element exactly with the paired determinant in(4). The single factor N^(-E) is the outer Hilbert inner-product normalization; q already contains its discrete transition probabilities and is not divided by N^E again. For M_t=1, (3) is <v,v> and the same formula applies with no q factors.

Using Omega_pair itself as both endpoint vectors in(3) would leave half of the endpoint multipliers and would not give(4). No endpoint normalization is dropped. The scalar determinant normalization inside F_pair is also the one in Block03.

Omega_pair has zero charge at each site and is constant in theta. It is a physical vector. Gauge covariance of M makes v_delta physical as well; the Gauss projector can consequently be inserted in(3) without changing it. Formula(4) is the temporal-gauge open-slab model. Restoring temporal link variables by normalized gauge averaging gives the same physical amplitude: on an open interval each temporal link is removed recursively by a vertex gauge transformation, with invariant counting measure and neutral endpoints. There is no temporal winding variable to retain. This statement is not applicable to a periodic-time determinant without modification.

## 3. A contractive shift for the exact multiplier

It is not generally true that the normalized Fock multiplier is a contraction. A uniform finite-graph scalar shift supplies the hypothesis used by the prior convergence proof.

Let C=mu+3kappa. The spatial blocks in Block03 obey ||a||,||b||,||d||<=C, with a,d>=mI. Inverting its positive block factorization yields

    ||X_delta^-1||
      <=(1+delta ||b||)² max(||A^-1||,||D||)
      <=exp(3C delta).

On a one-particle space of dimension2r, the full exterior algebra obeys ||Gamma(S)||<=max(1,||S||)^(2r). The exact scalar in F_delta satisfies

    c_delta=det A/(1+mu delta)^(2r)<=exp(r C delta).

Hence ||F_delta||<=exp(7r C delta), ||F_pair,delta||<=exp(14r C delta), and ||M_delta||<=exp(7r C delta). These bounds hold for every spatial gauge field and do not depend on N. Put s=14r C and define

    Mhat_delta=exp(-s delta/2)M_delta,
    That_delta,N=exp(-s delta)T_delta,N,
    vhat_delta=exp(-s delta/2)v_delta.               (5)

Then 0<Mhat<=I and 0<That<=I. This deliberately loose shift depends on the fixed graph. It is remembered throughout: the shifted open amplitude is exp(-s delta M_t) Z_delta,N, and normalized Gibbs states and spectral projections are unaffected by restoring the scalar energy.

## 4. First derivative and the common Fourier core

Block03 proves, uniformly in theta on the fixed graph,

    F_pair,delta=I-delta H_pair(theta)+O_graph(delta²),
    H_pair=H_F tensor I+I tensor conjugate(H_F),
    H_F=dGamma(gamma_0(mu-K_s(theta)))+mu r I.

For all sufficiently small delta the spectrum lies uniformly near1, so the convergent power series of sqrt(1+x) gives its matrix square-root expansion. The spatial factor has B_delta=1-delta V+O_graph,g(delta²), where V=g^-2 sum_p(1-cos(Ctheta)_p). Consequently

    Mhat_delta=I-delta W(theta)/2+O_graph,g(delta²),
    W=V+H_pair+sI.                                  (6)

W is a fixed Hermitian gauge-compatible finite Laurent polynomial. The exact Mhat need not have finite Fourier support. Only the first derivative W must have that support: the uniform remainder in(6) remains O(delta²) in the sampled multiplier norm for every N. This avoids the false inference that an exponential or a square root of a finite Laurent polynomial has finite Fourier support.

Embed centered clock Fourier labels into the integer Fourier basis by J_N as in the prior pack. For a fixed finite Fourier polynomial f, its product with W has fixed finite support, and sampling that product eventually has no wrapping. Thus

    J_N Mhat_delta,N J_N* f=f-delta Wf/2+O_f(delta²).

The calibrated kinetic estimate from prior Block02 gives

    J_N Q_delta,N J_N* f=f-delta Kf
                            +O_f(delta²+delta/N²),
    K=(g²/2)sum_l E_l².

Applying the same estimates also to Wf and Kf, which remain finite Fourier polynomials, and using contraction of the exact factors proves

    ||J_N That_delta,N J_N* f-f+delta Hhat f||
       <=C_f(delta²+delta/N²),
    Hhat=K+V+H_pair+sI.                              (7)

Hhat is the bounded Hermitian perturbation of K on its domain, with this Fourier core. It is nonnegative: either take the form limit of the positive operators (I-That)/delta on the core, or use (6) and Mhat<=I to obtain W>=0 before adding K. This is the hypothesis needed for the contractive resolvent argument.

## 5. Joint regulator and physical state limits

All hypotheses actually used in prior PR8162 Block02 sections6-8 and Block03 are now checked for Mhat: positivity and contraction; uniform ||I-Mhat||<=C delta; a finite-Laurent first derivative with O(delta²) multiplier remainder; gauge covariance; and finite-dimensional matter. Its exact formula need not be exp(-delta h/2)B^(1/2). The previous proofs use precisely these properties, so they apply with W in(6).

For clarity, the remaining load-bearing estimates are

    Q_delta,N<=exp[-delta(2g²/pi²)|n|²],
    I-That=(I-Mhat²)+Mhat(I-Q)Mhat.                 (8)

The first is the calibrated all-mode Jacobi-product bound, and the second is an exact identity with positive terms. A unit vector of bounded (I-That)/delta energy therefore has Fourier tail at radius L bounded by

    sqrt(R delta/[1-exp(-delta(2g²/pi²)L²)])+C delta.

For every sequence delta_j->0,N_j->infinity, first j->infinity and then L->infinity gives precompactness. Combining this with the core consistency(7) yields norm convergence of embedded shifted resolvents. The exact logarithmic generator Ghat_j=-delta_j^-1 log That_j has the same limit: its resolvent differs by at most2delta_j from the (I-That)/delta resolvent. Isolated spectral clusters, with their full multiplicities, converge in projection norm.

The finite-clock Gauss projector selects Dn=Q modulo N, while the rotor projector selects exact equality. On each fixed Fourier label and fixed matter charge the two eventually coincide. This gives strong projector convergence, which becomes norm convergence after multiplication by the compact limiting resolvent. Thus the preceding conclusions also hold in every nonempty physical sector. Extra modular Gauss states do not remain at bounded energy.

Finally the contraction in(8) and min-max give a heat-trace majorant

    Tr exp(-t Ghat_j)<=d_m [sum_(n in Z)exp(-t(2g²/pi²)n²)]^E.

The same majorant controls spectral tails. With norm-resolvent convergence, it yields trace-norm convergence of positive-time heat operators and of normalized physical Gibbs states, exactly as in prior Block03. The actual integer transfer powers have the same limit after accounting for their time rounding. Ground spaces converge as isolated spectral clusters; uniqueness of a ground vector is not assumed. These are all fixed-graph statements. Their constants and the displayed heat-trace majorant do not remain bounded as the spatial graph grows.

Undoing the shift identifies the supplied Hamiltonian

    H=(g²/2)sum_l E_l²+g^-2 sum_p(1-cos(Ctheta)_p)+H_pair(theta).
                                                               (9)

For delta_j M_t,j->T>0, the exact boundary vectors obey J_N vhat_delta->Omega_pair. The product limit, with M_t,j-1 time transitions, and the explicit scalar in(5) give

    Z_delta_j,N_j -> <Omega_pair,exp(-T H)Omega_pair>.           (10)

The factor exp(-s delta_j M_t,j) tends to exp(-sT), so the shift is restored without an endpoint ambiguity. Operator convergence proves(10) without assuming that typical gauge paths have a classically differentiable continuum history.

## 6. Connection to the curl estimate and its limits

For m>3kappa, Block02's local extension and physical-metric Hessian/third-variation bounds apply pointwise to exactly the determinant in(4), before any gauge sum. Thus the heavy-fermion bound, the supplied boundary determinant and the physical Hamiltonian now refer to one explicitly identified construction. This statement does not transfer a Gaussian phase theorem from an isotropic gauge model to the anisotropic clock kernel, or control the spatial-volume limit of the state in(10).

The original determinant represents the particular open boundary amplitude(4). Thermal and ground-state conclusions above concern the constructed positive transfer. They do not assert that the open determinant is itself a thermal trace, nor that arbitrary fermionic insertions have been matched. Omega_pair lies in a specified conserved particle-number sector. Taking a long-time boundary amplitude does not identify a global ground state without also proving the necessary sector and overlap statements; no such inference is made here. Gapless matter, a fixed finite-payload photon phase, native action/time selection and an axiom-forcing contradiction remain unproved.

The finite check sums27 actual three-slice clock histories using the original four-component Dirac matrix, and compares the result with a separately assembled1296-dimensional physical Fock transfer. Its one-edge graph tests Gauss reduction and charged hopping but has no magnetic plaquette or propagating photon. Separate joint refinements compare with a sparse CAR Hamiltonian and its exact integer electric energy. They are finite floating diagnostics of this derivation, not general proofs.
