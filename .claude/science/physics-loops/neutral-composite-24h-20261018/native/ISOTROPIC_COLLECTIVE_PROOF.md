# Native isotropic collective-spin fluctuation

Status: bounded-support. The supplied Hamiltonian is now evaluated at Jx=Jy=Jz=J>0, without adding a term. The result concerns a specified collective sector, not all possible large spatial features.

Let N be the number of sites on a periodic cubic grid, with each side at least three. There is one undirected bond per positive direction per site; in particular no length-two duplicate bonds or self-loops occur. Write

    H = -J sum_(r,alpha) sigma_r^alpha sigma_(r+e_alpha)^alpha,
    S_alpha = (1/2) sum_r sigma_r^alpha,
    S = N/2,

and let P project onto total spin S, the fully permutation-symmetric sector. Q=1-P. This includes entangled symmetric states, not just uniform product states.

## Flat compression is not protected dynamics

For distinct sites i,j, permutation symmetry gives

    P sigma_i^alpha sigma_j^alpha P
      = [4 S_alpha^2 - N]/[N(N-1)] P.

There are N bonds in each direction. Therefore PHP=-JN P exactly. A model obtained by simply retaining this sector would have a flat orientation energy. It is necessary to compute QHP before treating this as a collective mode.

For a coherent product |n>^N, with unit n, direct bond covariances give

    <(H+JN)^2> = J^2 N [1 + sum_alpha n_alpha^4].

The same-bond contribution per N is sum(1-n_alpha^4). The N unordered adjacent bond pairs in each direction contribute twice sum n_alpha^2(1-n_alpha^2). The 4N unordered shared-site pairs for each distinct direction pair contribute -8 sum_(alpha<beta) n_alpha^2 n_beta^2. Disjoint bonds have zero covariance. These sum to the displayed result. Only symmetrized covariances enter; imaginary Pauli products cancel.

Define L=P H Q H P=P(H+JN)^2P. The coherent-state expectation of an operator uniquely determines it in a fixed irreducible spin representation. The fourth moment identity is

    sum_alpha <S_alpha^4> = A0 + D4 sum_alpha n_alpha^4,
    A0 = (6N^3-5N^2+2N)/16,
    D4 = N(N-1)(N-2)(N-3)/16.

It follows that the exact leakage operator is

    L = J^2 N [1 + (sum_alpha S_alpha^4-A0)/D4] P.

Since sum_alpha (S_alpha^2-S(S+1)/3)^2 is positive,

    sum_alpha S_alpha^4 >= [S(S+1)]^2/3.

Also S_alpha^4<=S^2 S_alpha^2 for each alpha. Thus

    4J^2 N(N-1)(N-6)/[3(N-2)(N-3)] P
      <= L <= 2J^2 N(N-2)/(N-3) P.

For N>6 every normalized vector in P leaks with norm at least asymptotically J sqrt(4N/3). No exact H eigenvector lies wholly in P. This does not exclude a dressed collective structure with substantial support outside P.

## A native entangled trial lowers the energy extensively

Take even Lx>=4 and match disjoint x bonds. On each matched pair use

    cos(theta)|00> + sin(theta)|11>,

and take their tensor product. The exact energy per site is

    E_trial/N = -J[cos^2(2theta)+(1/2)sin(2theta)].

Matched XX bonds supply the second term. Unmatched XX and all YY bonds have zero expectation. Every ZZ bond joins distinct dimers and has expectation cos^2(2theta). Choosing sin(2theta)=1/4 gives E_ground<=-17JN/16. This is a variational bound, not an assertion of a dimer ground phase.

For any actual ground vector psi, the projected eigenvalue equation gives

    (E_ground+JN)P psi = PHQ Q psi.

Use the upper leakage bound M=2J^2 N(N-2)/(N-3) and |E_ground+JN|>=JN/16. Then

    ||P psi||^2 <= M/[(JN/16)^2+M]
      = 512(N-2)/[N(N-3)+512(N-2)] = O(1/N).

Thus every ground vector loses its maximal-spin weight in this growing even-x family. Ground preparation cannot justify the flat maximal-spin compression as the physical scalar sector.

## The first fluctuation channel is derived, not inserted

Let a_alpha=<n-|sigma_alpha|n+>. Pauli identities imply sum n_alpha a_alpha=0 and sum a_alpha^2=0. The one-spin-flip amplitudes in H|n>^N cancel. The remaining pair amplitude on an alpha bond is -J a_alpha^2. Applying total S_n^+ to this residual gives zero: each site's incident pair coefficients sum to -2J sum a_alpha^2=0. Its magnetic quantum number is S-2, so it lies in total spin S-2. Coherent states span P; consequently

    range(QHP) is contained in the total-spin Smax-2 sector.

At n=z the exact first fluctuation is

    QH|up> = J sum_r [s_r^- s_(r+ey)^- - s_r^- s_(r+ex)^-]|up>
            = J sum_k (cos ky-cos kx) b_k^dag b_-k^dag |up>,
    b_k^dag = N^-1/2 sum_r exp(ik.r) s_r^-.

The b operators are spin Fourier operators, not canonical bosons. The form factor vanishes at zero momentum and begins (kx^2-ky^2)/2. It describes a structured pair fluctuation rather than a derived scalar zero mode.

For an inversion- and x/y-symmetric momentum mesh AND cutoff |k|<=kappa (for example, equal-side cubes), sum F(k)=0 with F=cos ky-cos kx. The exact spin-pair Gram matrix is

    <k',-k'|k,-k> = delta_(k,k') + delta_(k,-k') - 2/N.

In general the norm squared is 2J^2 sum_cut |F(k)|^2-(2J^2/N)|sum_cut F(k)|^2. Under the stated mesh/cutoff symmetry the second term vanishes. In the resolved continuum limit, followed by kappa->0,

    norm_squared ~ J^2 N kappa^7/(105 pi^2).

Indeed the angular average of (kx^2-ky^2)^2/4 is r^4/15. This is an initial-state Fourier diagnostic, not an invariant spectral projector or a lifetime.

## Local dynamics also lacks size protection

For the coherent initial state, the magnetization along n has expansion

    m_n(t) = 1 - 4J^2[1+sum n_alpha^4]t^2 + O(J^3 |t|^3).

Each native pair-flip state changes the total magnetization by four; its probability at order t^2 is J^2(1-n_alpha^2)^2t^2. This gives the coefficient. Bounded-degree finite-range nested commutators bound the cubic remainder for each local observable uniformly in N, hence also for their average. At sufficiently small fixed time the loss does not vanish with system size. No long-time decay law follows from this expansion.

## Checks and scope

Exact local controls apply H to low-excitation Dicke vectors on 27 physical sites and verify 25 entries of L against the collective matrix; they do not diagonalize the 2^27 physical Hilbert space. Additional controls check coherent amplitudes, the dimer expectation, the highest-weight cancellation and the Fourier integral. Independent checks cover the analytic identities and scope.

The native H and isotropic parameter choice remain premises. The many-site grid itself has not selected a protected uniform collective spin; instead its first internal coupling and a ground-sector exclusion are derived. Structured lower-spin features, entangled ground phases and their collective spectra remain open. No observation calibration or independent empirical test occurs.
