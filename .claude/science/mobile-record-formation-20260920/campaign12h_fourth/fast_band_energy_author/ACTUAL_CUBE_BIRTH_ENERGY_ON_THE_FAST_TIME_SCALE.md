# Actual cube birth energy on the subsequent fast time scale

Personal root derivation, 2026-09-24. Conditional result in the supplied
compensated model, lambda=0. Original resolved or coherent formation marks are
unchanged. This extends the first-event microscopic moment calculation to a
shrinking physical-time interval after that actual event. Independent source
comparison is pending. No energy filter, field-only state or reservoir is added.

## 1. State, clock and claim

Use the cube A={0,3,5,6}, B={1,2,4,7}, with A-to-B oriented links. Let Omega
have all A charges+1, B vacant and zero electric field, satisfying divE=q-1_A.
At integer spin S>=1 let C=S(S+1), and retain

    H=delta epsilon^-4 h, h=W+epsilon T+epsilon² C_S,
    T=-(F+F*), F=sum_a F_a, L_j=sqrt(kappa)/epsilon j.

C_S is the supplied gated local compensation, without the additional electric
completion term. Prepare the Hamiltonian's canonical low-band state U_epsilon
Omega and apply the actual first mark j_i on edge(0,1). Normalize this actual
output, phi_i=j_i U_epsilon Omega/||j_i U_epsilon Omega||. The three cases below
are resolved plus, resolved minus, or the stipulated coherent edge mark.
Subsequent evolution uses the same original instrument as the first event.

Define B_i=j_i F Omega, R_i=-F_0 B_i, b_i=||B_i||², r_i=||R_i||² and
ell_i=r_i/b_i. The preceding first-event result gives

    (b_i,r_i,ell_i)=(2,4,2), (2,2,1), (4,6,3/2).          (1)

These zero-flux coefficients are exact at every S>=1. The full microscopic
birth has a small energetic part; R_i is its leading rotated coordinate, not
a newly applied operation or a physically postselected energy state.

On the complete physical N=6, W=1 space define

    G_1,S=Pi1(FF* - F*F)Pi1,
    Gamma_1,S=Pi1 sum_j j*j Pi1,
    A_1,S=-i delta G_1,S-kappa Gamma_1,S/2,
    f_i,S(tau)=||exp(tau A_1,S)R_i||²/b_i.                (2)

The original two instruments have the same Gamma: on each edge the plus and
minus birth ranges are orthogonal, so j_+*j_-=0. This does not identify their
recycling channels or all conditional states. G_1,S and Gamma_1,S are bounded
uniformly in S at fixed graph. In the rotor limit, keep physical charge/field
words distinct and denote the corresponding operators and f_i by dropping S.

Let rho_i(t) be the full original GKLS state from phi_i. For every finite
T_0, with epsilon² C=delta/K and fixed positive delta,K,kappa,

    sup_(0<=tau<=T_0) |epsilon² Tr(H rho_i(epsilon²tau))/delta
                                      -f_i(tau)| ->0.    (3)

Thus the first large microscopic energy contribution need not stay stored.
The curve f_i is nonincreasing, and below we prove that it decreases for small
positive tau. Equation(3) is a fast-time statement t=epsilon²tau. It proves
neither a fixed-positive-physical-time energy limit nor complete eventual decay.
The Hamiltonian on this many-center cube is not asserted nonnegative.

There is also an actual second-event probability statement. Let p_2,i(t) be
the probability of another original formation after the specified first event.
Then, uniformly on the same finite tau interval,

    p_2,i(epsilon²tau)/epsilon²
                  ->8 kappa tau+ell_i-f_i(tau).           (4)

Both terms concern the original instrument. The first is the usual slow-sector
contribution; the second is the depletion of the initially rare energetic
component. No detector for energy bands or replacement formation rule is used.

## 2. Why the no-event state gives exact ensemble energy

After the first event N=6 and total charge is4. At most one further birth is
possible on the eight-site cube. Its N=8 output has every site occupied, so
W=F=C_S=0 and every original j vanishes. Its Hamiltonian is exactly zero in
the present lambda=0 model. The postbirth N=6 sector has W=0,1,2.

Let Gamma=sum_j j*j on that sector. With physical time t=epsilon²tau, its
unnormalized no-event state is exactly

    chi_i(tau)=exp[-i delta epsilon^-2 tau h_eff] phi_i,
    h_eff=W+epsilon T+epsilon²(C_S-i kappa Gamma/(2delta)). (5)

Consequently, without any approximation to the second-event ensemble,

    Tr(H rho_i(epsilon²tau))=<chi_i,H chi_i>,
    p_2,i(epsilon²tau)=1-||chi_i||².                      (6)

The coherent instrument can change the terminal density, but that density has
zero energy and no further events. This is why Gamma alone suffices in(5)-(6).
This capacity argument is for the cube. The six-site cycle cannot form twice.

All A centers on the cube have overlapping stars. Its gated compensation
therefore has only its W=0 block in this record sector:

    C_0=M+Q_S, M=P F*F P, Q_S=D/C, C_1=C_2=0.            (7)

The zero-flux B_i vectors have D B_i=0 exactly. This fact is essential to
removing a leading low-band contribution in(3); moving high-flux preparations
are not covered by this statement.

## 3. Reduction from the full microscopic generator

Here are estimates before either limit. They hold uniformly in S at fixed
cube and bounded tau. The local T,C_S,Gamma have uniform norms, and W has
integer gaps. Resolvent contours of radius less than1/2 around each W grade
therefore define analytic separated cluster projectors for small epsilon,
for both the Hermitian h and the non-Hermitian h_eff in(5).

Their projector expansions agree through orderepsilon². Indeed the first
coefficient is set by T. The difference at second order would be the contour
integral of

    (z-W)^(-1) Gamma (z-W)^(-1).

Gamma commutes with W, so this is a sum of grade projectors times double poles;
each closed-contour integral is zero. The first possible projector difference
is therefore O(epsilon³), with a uniform bound from the resolvent expansion.
Let P_k^H and P_k^eff be the two families. The invertible intertwiner

    S_epsilon=sum_k P_k^eff P_k^H=I+O(epsilon³)            (8)

maps each Hermitian cluster to its exact no-event cluster. Use the canonical
unitary V_epsilon from the W grades to the Hermitian clusters; its low-band
column is the specified U_epsilon. Conjugating h_eff by S_epsilon V_epsilon
block diagonalizes it exactly. W parity makes its grade blocks even in
epsilon. The first high block has expansion

    h_eff,1=I+epsilon²[G_1,S-i kappa Gamma_1,S/(2delta)]
                  +O(epsilon^4).                        (9)

The ordinary second-order cluster formula has denominators1-0 and1-2.
Together with C_1=0 it gives precisely FF* - F*F in(2). Replacing it by the
low-band Hamiltonian, or giving both denominators the same sign, is incorrect.

The actual first output, in Hermitian cluster coordinates, has grade-one
amplitude epsilon R_i/sqrt(b_i)+O(epsilon³), grade-two amplitude O(epsilon²),
and grade-zero amplitude beta_i+O(epsilon²), beta_i=B_i/sqrt(b_i). These are
the canonical jump expansion and its parity grades. The near-identity map(8)
changes them only by O(epsilon³). Finite-tau propagation of the blocked
matrices in(9) consequently gives the grade-one term

    epsilon exp(-i delta tau/epsilon²)
                 exp(tau A_1,S)R_i/sqrt(b_i)+O(epsilon³). (10)

All transformed propagators are uniformly bounded on finite tau intervals;
the exact no-event propagator is contractive, and the intertwiners and their
inverses have norms1+O(epsilon³). Ordinary bounded-matrix Duhamel estimates
control the O(epsilon²) correction to the generator in(9). Grade-two norm
remains O(epsilon²).

In the Hermitian coordinates the rescaled energy operator is block diagonal.
Its grade-one block is epsilon^-2 I+O(1); its grade-two block has normO(epsilon^-2).
The low block is Q_S+O(epsilon²). Since Q_S beta_i=0 and the low coordinate
stays beta_i+O(epsilon²) up to its harmless leading Q_S evolution, its rescaled
energy contribution tends to zero. Grade two contributes O(epsilon²). The
O(epsilon³) intertwiner error, even using the global rescaled energy norm
O(epsilon^-2), contributes only O(epsilon). Equations(6) and(10) prove

    epsilon² Tr(H rho_i(epsilon²tau))/delta=f_i,S(tau)+O(epsilon) (11)

uniformly on finite tau intervals and uniformly in S. This argument computes
microscopic energy before limiting it; it is not an inference from density
convergence alone.

For completeness, the norm accounting needed for(4) uses the low no-event
block one order further. Its expansion is

    h_eff,0=epsilon² Q_S
        +epsilon^4[H4_S-i kappa Gamma_B,S/(2delta)]+O(epsilon^6),
    Gamma_B,S=P F* Gamma F P=sum_j B_j*B_j.               (12)

Here H4_S is the already checked Hermitian compensation coefficient. The
additional imaginary term follows directly by expanding the high-block
resolvent in the Schur complement: Gamma has zero P block and the term through
W=1 is -i kappa F*Gamma F/(2delta). Canonical normalization adds no further
imaginary term at this order. The use of a complex coefficient in(12) is not
an assertion that the no-event generator is self-adjoint.

The initial low norm squared is1-epsilon²ell_i+O(epsilon³). Since Q_S beta_i=0,
its subsequent norm squared is

    1-epsilon²ell_i-kappa epsilon² tau
                   <beta_i,Gamma_B,S beta_i>+O(epsilon³).

The Hermitian fourth-order term contributes no first-order norm loss.
Grade one contributes epsilon²f_i,S(tau)+O(epsilon^4), and grade two contributes
O(epsilon^4). The similarity error in(8) is O(epsilon³). Exact physical paths
give <beta_i,Gamma_B,S beta_i>=8 for each of the three first marks and either
original instrument, at every S>=1. This proves the finite-S counterpart of(4)
with an O(epsilon) remainder after dividing by epsilon².

## 4. Taking the rotor limit without replacing a physical state by one fiber

Embed finite-spin physical states into the common charge/integer-field word
space by zero extension outside the spin box. Normalized shifts converge
strongly on each finite-support vector. The finite number of products in
G_1,S and Gamma_1,S therefore converge strongly, with a common operator bound,
to their rotor versions. Their exponential power series converge on fixed
vectors, uniformly for bounded tau: truncate the series uniformly by the
common norm bound, then take the limit in each finite product. The vectors
B_i and R_i have fields of magnitude at most one and do not change with S.
Thus f_i,S converges uniformly to f_i. Combining with(11)-(12) proves(3)-(4)
along the specified joint scaling. No normalizable state is replaced by a
single Fourier fiber, and no growing-graph or infinite-physical-time limit
is involved.

## 5. The energetic component starts dark and becomes accessible

Every R_i word has its A vacancy at0 and its B vacancy at the opposite cube
vertex7. No original birth edge joins them. Hence j R_i=0 for every mark,
including finite-spin weights. It does not follow that the subspace remains
dark under G_1. Two-hop paths move a vacancy into a neighboring configuration.
Exact physical-word summation gives

| first mark | b_i | r_i | sum_j||j G_1 R_i||² | ||G_1 R_i||² |
|---|---:|---:|---:|---:|
| resolved plus |2|4|96|48|
| resolved minus |2|2|48|24|
| coherent |4|6|144|72|

In the rotor each word in G_1 R_i has adjacent vacancies; Gamma_1 acts there
as2. The exact finite-spin version of the fourth column is

    sum_j||j G_1,S R_i||²=(24-12/C) r_i.                 (13)

The symbolic control obtains(13) from the link amplitudes with
C=2/(1-z²),0<=z<1. It is not fitted to a few spin values. It also verifies
the slow rate8 and keeps full charge/field certificates for the rotor paths.

Since f_i'=-kappa||Gamma_1^(1/2)exp(tau A_1)R_i||²/b_i,
Gamma_1 R_i=0, and A_1 R_i=-i delta G_1 R_i, Taylor expansion of bounded
operators gives

    f_i(tau)=ell_i-kappa delta² tau³
                    [sum_j||jG_1 R_i||²]/(3b_i)+O(tau^4)
             =ell_i[1-8kappa delta²tau³]+O(tau^4).       (14)

Thus the respective cubic coefficients are16,8,12 times kappa delta².
The finite-spin coefficient8 is replaced by8-4/C. There is a real loss on
small positive fast time, even though the leading energetic component is
initially dark. Neither obligatory persistence nor an immediate simple
exponential loss describes this onset.

The order of limits is explicit: first the microscopic/joint limit at fixed
bounded tau, then the small-tau expansion of f_i. These results do not assert
convergence of microscopic initial derivatives, or a uniform relative cubic
approximation for arbitrarily shrinking tau(epsilon). They also do not prove
that f_i eventually reaches zero; dark invariant states and longer-time
spectral behavior have not been classified.

## 6. Complete physical controls and limits

The exact path control starts from charge/link actions and preserves distinct
integer-field words. The separate complete spin-one control enumerates all
3^12 link assignments and imposes Gauss, yielding physical dimensions3197
in N=4,5604 in N=6 and672 in N=8. It extracts all69 low eigenvectors in N=4,
uses their positive-overlap Gram inverse square root for the exact canonical
preparation, applies the actual first marks, and propagates the complete N=6
no-event matrix. No Fourier identification or truncated matter sector is used.
The exactly zero terminal energy makes this the full ensemble energy control.

It compares the measured rescaled microscopic energy and actual second-event
probability against(11)-(12), for both resolved signs and the coherent first
mark, at three epsilon values and four fast times. Fixed S=1 refinement tests
the uniform fast-time formulas with its actual G_1,S. It does not by itself
verify the large-S limit; that limit follows from the bounded strong-convergence
argument and exact physical paths. Root controls are consistency evidence;
selective independent reconstruction remains a separate requirement.

The energy decrease is a property of the supplied GKLS generator. No bath is
specified to receive it, so no heat, work or reservoir-transfer identification
is made. This result does not remove the earlier need to account for the
energy supplied at formation. It shows why initial power alone cannot be
integrated as though every rare energetic component were permanently stored.
The compensation, dressed preparation, graph and parameters remain supplied;
physical selection, finite physical-time many-event energy, locality and
experimental identification remain unresolved. No axiom, audit verdict or
TOE-completion claim is made.
