# From physical periodic cells to the full threshold form

This is owned supporting proof for the canonical four-particle threshold
note, with exactly its law, conventions and claim scope. Together with the
periodic-band proof it establishes that note's equation(2). Fix mu,tau>0
and R>=14 throughout; constants below can depend on these fixed parameters.
Only sufficiently large ODD L are considered. All profiles are physical
four-site occupation coefficients, never independent collision-core dimers.

## Raw amplitudes, the polar condition and the 81 fields

Let chi_L[A] be the actual occupation profile obtained by keeping Phi_A
only when its two graph edges are mutually R-isolated. There is then a
unique matching. On such an occupation its coefficient is
sqrt2(UAU^T)_(d,e). In this proof chi_L and every adjoint on profiles use the orbit Hilbert
inner product, one coefficient per translation orbit. Write G_L for the
15 by 15 Gram form chi_L^*chi_L/V;
it is the same G_L as in the band proof. For large L the omitted relative
anchors form a fixed finite set for each d,e, so exactly

                         G_L=I-K_R/V,                    (1)

where K_R is a fixed positive matrix. In particular G_L^(+/-1/2)=I+O(V^-1).
The normalized frame in the orbit basis is V_L=chi_L G_L^-1/2/sqrt V.
Its literal physical occupation coefficient is chi_L G_L^-1/2/V.

The normalized orbit basis vector is V^-1/2 times the sum of the physical
occupations in that orbit. Multiply the ORBIT BASIS coefficients of the
normalized constrained Schur minimizer by sqrt V and denote this raw
profile by psi_L[A]. Equivalently its literal physical coefficients were
multiplied by V. There is no orbit stabilizer for odd L: its
order would divide both4 and L^3. Therefore the constrained minimum reads

    E_L(psi_L[A])=V<A,S_L A>,
    chi_L^*psi_L/V=G_L^1/2 A.                            (2)

Here E_L is the physical torus energy DIVIDED BY V, and the adjoint in(2)
is an orbit sum. Assigning the same raw coefficient to every physical
translate gives a full physical sum V times larger. The band proof gives E_L(psi_L)<=C||A||^2. The
complement inverse and the translation invariance of the constraint give
a unique K=0 minimizer; no momentum sector is thrown out by hypothesis.

Define the scaled removal fields

 F_(d,e)(r)=psi_L({0,e,r,r+d})/sqrt2 for four distinct sites, zero otherwise.

All81 fields vanish at r=0, and F_(d,e)(r)=F_(e,d)(-r). Each exact ordered
removal is retained. Resolving the output rows in the joint positive bound
of the owner note gives, with means M=V^-1 sum_r F(r),

 E_L>=2a sum_(d,e)||gradient F_(d,e)||_2^2+mu||Q_nm psi_L||_orbit^2,
 E_L>=2sum_e S_one-pair(F_(.,e))>=4mu V||P_high M||_HS^2. (3)

The two inequalities on separate lines are used separately; their right
sides are not added. The second follows by mean orthogonality of the
translation invariant S form. In the first, a matching orbit with m
matchings has2m ordered representations, including multiple matching
orbits. The nonmatching norm is an orbit sum. These exact factors also
follow by expanding the positive torus rows before dividing by V.

## Uniform discrete Sobolev bounds

For any mean-zero scalar f on a cubic torus,

    ||f||_6 <= C||gradient f||_2,                         (4)

with C independent of L; the norms use unnormalized sums. One elementary
proof uses piecewise affine interpolation on a fixed tetrahedral division
of each cube. Its Lp norms are uniformly equivalent to the vertex norms
by finite-dimensional norm equivalence on a tetrahedron; its integral is
a constant multiple of the vertex sum by translation symmetry, hence zero.
Its gradient norm is bounded by neighboring lattice differences. Extend
periodically to three copies in each direction and multiply by a cutoff
of scale L. The Euclidean Sobolev inequality gives
||f||_6<=C(||gradient f||_2+L^-1||f||_2), and the mean-zero torus Poincare
bound absorbs the second term. Euclidean Sobolev itself follows from the
coordinate-line fundamental theorem of calculus (the W^(1,1) inequality)
applied to |v|^4 and Holder. The same proof on finitely supported lattice
fields gives the infinite-lattice inequality. Thus no lower spectral bound
for a continuum approximation is being assumed here.

Apply(4) to each F-M. The hard-core pin F(0)=0 gives
|M|<=||F-M||_6<=C sqrt(E_L), componentwise, and therefore also a uniform
supremum bound for F. Let q_R(d,e,r) be the actual isolated-edge guard.
It differs from1 at only finitely many anchors independent of L. A direct
ordered-pair contraction with chi_L gives the exact full-channel identity

    chi_L^*psi_L/V=U^T[ V^-1 sum_r q_R F(r)]U.             (5)

For instance a uniquely matching physical orbit contributes twice to the
ordered fields, cancelling the two sqrt2 normalizations; dividing the full
physical sum by V is exactly the orbit inner product. Thus(5) holds also for arbitrary complex A and
its off-diagonal basis vectors, without an extra factor two.
The finite omitted set and uniform supremum bound imply
U^T M U=A+O(V^-1)||A||. The second inequality in(3), and the exchange
symmetry of M, bound its other rows AND columns by C V^-1/2||A||. Hence

    ||M-UAU^T||<=C V^-1/2||A||,
    ||F-UAU^T||_6+||Q_nm psi_L||_2<=C||A||.               (6)

In the first term of the second line, the constant mean error has l6 norm
V^1/6 O(V^-1/2), and so is harmless. The incoming Phi_A differs from the
constant ordered fields only in a fixed collision region.

For the infinite-volume minimizing profile psi_infty[A]=Phi_A+chi_infty,
existence in the faithful energy completion was proved in the owner note.
Affine orthogonal projection gives E(chi_infty)<=E(Phi_A)<=C||A||^2.
Applying the infinite version of(4) to its compact approximants, and(9) of
the owner note, proves

    ||F_infty-UAU^T||_6+||Q_nm psi_infty||_2<=C||A||.      (7)

These are statements about physical coefficients in the energy completion;
no l2 norm of the full response is required.

## A physical logarithmic cutoff and its cost

Use the physical diameter s of a four-site orbit. A finite local pair row
changes s by a bounded amount. If s<L/3, a periodic orbit has a unique
infinite-lattice lift modulo translation when its support lies in such a
small cluster; the cluster is determined by its mutually short differences.
The cutoff below is used only at s<=sqrt L, where this lift is unambiguous.
Put r_-=L^1/4, r_+=L^1/2, J=log(r_+/r_-), and

    eta(s)=1 for s<=r_-,
           log(r_+/s)/J for r_-<s<r_+,
           0 for s>=r_+.

Rounding to integer shells or shifting shell endpoints by a fixed stencil
width changes only uniform constants. For large L all collision rows lie
where eta=1. Consider the actual physical profile

                      Y=Phi_A+eta(psi-Phi_A).            (8)

There are no artificial independent output amplitudes in this definition.
Outside a fixed core, every nonzero S or W row is either entirely in the
separated-two-graph-edge exterior or entirely in Q_nm. To see this, fix its
residual two sites: if they are a graph edge and the removed edge is far,
there is one matching and no cross graph edges. If they are not a graph
edge and remain far from the local removed edge, no matching is possible.
Any crossing between these cases forces all four sites into a fixed core.
The positive diagonal Ddiag has no cutoff commutator.

On the matching exterior each ordered pair of edge types has three relative
coordinates, and the shell count is O(s^2). A local row's cutoff difference
is at most C/[J(1+s)]. Consequently

    sum_exterior |delta eta|^3<=C J^-2.

Holder, with the uniform l6 bound on the exterior deviation u from(6) or(7),
bounds the SUM OF SQUARED commutator rows by

 C||u||_6^2 (sum|delta eta|^3)^(2/3)<=C||A||^2 J^-4/3.    (9)

The actual row width and incidence are bounded independently of the orbit;
this follows directly from(4)-(5). On Q_nm, the corresponding squared cost
is at most C||Q_nm psi||_2^2/(J^2 r_-^2). All rows of Phi_A vanish off the
core. On the core eta=1. Applying Minkowski to the direct sum of actual
positive rows therefore proves

       E(Y)<=E(psi)+C||A||^2 J^-2/3.                     (10)

Indeed the main row norm is at most sqrt(E(psi)), and the commutator norm
is O(J^-2/3); its cross term gives the stated rate. This estimate is valid
in both directions of embedding, with the same finite-core law. A sharp
cutoff with an unpriced surface norm would not give(10).

## Both variational inequalities and the polar correction

First take psi=psi_L and lift the compact correction in(8) to Z^3. It is an
admissible actual compact response to Phi_A. Equations(2),(10) give

                    T0[A]<=V<A,S_L A>+C||A||^2 J^-2/3.   (11)

Conversely take psi=psi_infty and periodize the compact correction in(8).
Its energy is at most T0[A]+C||A||^2 J^-2/3. It does not yet have exactly
the polar constraint(2). Define the defect in normalized incoming units by

             beta=G_L^-1/2 chi_L^*Y/V-A.

The finite-core contribution is O(V^-1)||A||. The separated exterior has
O(r_+^3) relative sites and l6 norm O(||A||); Holder bounds its l1 norm by
C r_+^(5/2)||A||. Nonmatching coefficients have zero overlap with chi_L.
Together with(1) this gives

        ||beta||<=C||A||(V^-1+r_+^(5/2)/V)=O(L^-7/4)||A||. (12)

Subtract the physical profile chi_L G_L^-1/2 beta from Y. Its polar
coordinate is exactly beta, so the result satisfies(2). Its energy is at
most V theta_L||beta||^2=O(||beta||^2), and its cross term with Y is
O(||A||||beta||), by positive-form Cauchy. This is smaller than the error
in(10). The constrained Schur variational principle now gives

                    V<A,S_L A><=T0[A]+C||A||^2 J^-2/3.   (13)

These are uniform quadratic-form bounds on ALL fifteen complex channels;
polarization, or the Hermitian norm characterization, yields the operator
norm convergence in the owner note. Since J=(log L)/4, its rate is precisely
the stated O((log L)^(-2/3)).

The band proof bounds the rescaled difference between each low eigenvalue
and the corresponding Schur eigenvalue by O(L^-1). Weyl's finite-dimensional
inequality and(11)-(13) then prove the low-spectrum convergence, and its
physical complement gap proves the claim for lambda_16. Every estimate
keeps R fixed before L tends to infinity.

One can also read a local response consequence without an l2 assertion.
The lifted Y_L of(11) has excess threshold energy O(J^-2/3)||A||^2. Compact
stationarity and density of compact corrections imply
E(Y_L-psi_infty)=E(Y_L)-T0[A]. Infinite Sobolev on the matching coordinates
and the Q_nm norm in the joint bound control each physical coefficient by
the square root of this excess (ordered-removal multiplicities are bounded
by six). Thus on all orbits of diameter<=L^1/4,

    |psi_L[A](S)-psi_infty[A](S)|<=C||A|| (log L)^(-1/3).

This is local coefficient convergence of raw constrained responses, not
convergence of their full l2 norms. No uniform-in-pair-number estimate,
thermodynamic equation of state, physical cell-boundary comparison or
selection among coherent/fragmented channels follows from the argument.
