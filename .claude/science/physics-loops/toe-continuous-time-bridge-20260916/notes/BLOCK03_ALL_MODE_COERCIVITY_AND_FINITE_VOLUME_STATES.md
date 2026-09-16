# All-mode coercivity and convergence of finite-volume physical states

Author theorem proposal, 2026-09-16. This extends the calibration construction in BLOCK02_CALIBRATED_CLOCK_ROTOR_TRANSFER_THEOREM.md, whose assumptions and core-consistency proof are provisional dependencies. It is a fixed finite spatial-complex result, with supplied g>0 and bounded gauge-compatible matter. No independent audit or infinite-volume phase is claimed.

## 1. The high-mode question

Strong convergence on a fixed test state does not exclude low-energy states escaping to increasingly high clock frequencies. Such escape would invalidate an inference about ground states from the transfer-product result alone. Here an exact theta product supplies the missing coercivity. It upgrades that result to norm convergence of embedded resolvents, convergence of isolated spectral projections, and trace-norm convergence of positive-temperature states along every joint delta->0, N->infinity path.

The finite graph, its number of links, matter dimension, and positive coupling are fixed throughout. Constants depending on these data are not thermodynamic estimates.

## 2. An all-mode kinetic floor

Let q=exp(-c) in(0,1), v(c)=E_c k^2, and

    a_m=4 q^(2m-1)/(1+q^(2m-1))^2, m>=1.

Jacobi's product, divided by its value at zero, gives

    lambda_c(h)=E_c exp(i h k)
      = product_(m>=1) [1-a_m sin^2(h/2)].             (1)

The primary formula used here is NIST DLMF 20.5.3 (equivalently 20.5.9), https://dlmf.nist.gov/20.5.E3 . Its hypotheses hold because c>0 and the nome q lies strictly inside the unit disk. Every factor in(1) is strictly positive for real h; a_m<1 and sum a_m<infinity. Uniform convergence and twice differentiating at zero give

    v(c)=(1/2) sum_m a_m.                             (2)

Using -log(1-x)>=x and sin(|h|/2)>=|h|/pi for |h|<=pi yields

    -log lambda_c(h)>=2 v(c) sin^2(h/2)
                          >=2 v(c) h^2/pi^2.         (3)

For the exact variance calibration v(c)=delta g^2 N^2/(4pi^2), centered integer clock label r, and h=2pi r/N, this becomes

    -delta^-1 log lambda_r
      >= g^2 N^2 sin^2(pi r/N)/(2pi^2)
      >= (2g^2/pi^2) r^2.                            (4)

These are bounds, not matching equalities. The target low-mode coefficient remains g^2/2. Both odd and even N are covered, including |r|=N/2 for even N.

For E links and finite matter dimension d_m, let |n|^2=sum_l n_l^2. Set a=2g^2/pi^2. The exact tensor-product temporal transfer obeys the diagonal operator inequality

    0<Q_delta,N<=exp[-delta a |n|^2].                (5)

This controls every centered clock Fourier mode. It is compatible with the low-mode consistency estimate, but does not assert uniform approximation of all their energies.

## 3. Compactness of low-energy vectors of the actual product

Use M and T=M Q M from Block02, with the scalar shift making the matter multiplier nonnegative. Thus 0<M<=I and ||I-M||<=C delta, uniformly in N on this fixed graph. In the finite clock space,

    I-T=(I-M^2)+M(I-Q)M.                             (6)

Both terms on the right are positive. If ||f||<=1 and
<f,(I-T)f>/delta<=R, then

    <Mf,(I-Q)Mf>/delta<=R.

Let F_L be the common-Hilbert-space Fourier projection onto |n|<L (including all matter states). Equation(5) gives

    ||(I-F_L)J_N Mf||^2
      <= R delta/[1-exp(-delta a L^2)].              (7)

Together with ||(I-M)f||<=C delta, this implies

    limsup_j ||(I-F_L)J_(N_j) f_j||
      <= sqrt(R/(a L^2))                            (8)

for any joint delta_j->0,N_j->infinity sequence with the stated uniform energy and norm bounds. Taking L->infinity proves precompactness of such embedded sequences. The finite-rank projection F_L is fixed before j->infinity; no illicit uniform Taylor expansion over all frequencies occurs.

## 4. Norm convergence of the embedded resolvents

As in Block02 put Ttilde_j=J_j T_j J_j*, A_j=(I-Ttilde_j)/delta_j, and R_j=(1+A_j)^-1 on the full rotor Hilbert space. Block02 proves R_j->R=(1+H)^-1 strongly. Here H=K+V+h has compact resolvent: K is diagonal with finite multiplicities and eigenvalues growing to infinity on a finite-dimensional torus, and V+h is bounded.

For ||u_j||<=1, f_j=R_j u_j has ||f_j||<=1 and <f_j,A_j f_j><=1. The component outside the clock image has norm at most delta_j/(1+delta_j). Applying(8) inside the clock image makes {R_j u_j} precompact along j->infinity.

To prove norm convergence, suppose a subsequence violated it and choose unit u_j witnessing the violation. Pass to a weakly convergent subsequence u_j->u, and a norm-convergent subsequence R_j u_j->f. Self-adjointness and strong convergence imply, for every fixed v,

    <v,f>=lim <R_j v,u_j>=<R v,u>=<v,Ru>.

Thus f=Ru. Compactness of R also gives Ru_j->Ru in norm, contradicting the violation. Therefore

    ||(1+A_j)^-1-(1+H)^-1||->0.                     (9)

On the clock image define the exact logarithmic transfer generator G_j=-delta_j^-1 log T_j. It is finite and positive because T_j is strictly positive. Its embedded resolvent is understood to be zero on the complement, rather than defining an infinite-valued operator there.

For 0<lambda<=1, x=(1-lambda)/delta and z=-log(lambda)/delta satisfy z>=x. If lambda>=1/2, z-x<=delta x^2 and hence

    0<=(1+x)^-1-(1+z)^-1<=delta.

If lambda<1/2, the difference is at most(1+x)^-1<=2delta. The clock-complement resolvent of A is at most delta. Functional calculus and(9) consequently prove

    ||J_j(1+G_j)^-1 J_j*-(1+H)^-1||->0.             (10)

This is norm convergence of compact positive operators and does not claim an operator-norm bound on G_j-H.

## 5. Spectral multiplicities and physical Gauss sectors

For a compact positive operator, any nonzero isolated spectral cluster is separated from the remainder by a contour in its resolvent set. The resolvent identity and a Neumann series give uniform contour-resolvent convergence from(10). Integrating around the contour gives norm convergence of the corresponding projections. Once their norm difference is less than1, the finite ranks agree: each projection is injective on the range of the other. Applying the continuous eigenvalue transformation E=1/r-1 shows convergence of every fixed eigenvalue cluster of G_j to that of H, with multiplicity, and no additional bounded-energy eigenstates escaping to infinity.

In particular the ground-state cluster converges, including a possibly degenerate ground space. This does not select a unique vector within a degenerate ground space or impose a ground-state uniqueness hypothesis on matter.

Let Ptilde_j=J_j P_N J_j* and P be the finite-clock and integer-Gauss projectors. Block02 proves Ptilde_j->P strongly. Since the limiting resolvent is compact,

    ||Ptilde_j R-RP||->0.

Here P commutes with R, and strong convergence times a compact operator is norm convergence by finite-rank approximation. Combining this with(10) gives norm convergence of the restricted embedded resolvents to R P. The same spectral conclusions hold on every fixed nonempty physical charge sector. Extra modular Gauss states cannot remain at bounded energy in the joint limit. The zero-sector case must simply be excluded when normalizing a state.

## 6. Thermal trace control

Let rho_k be the nondecreasing list, with multiplicity d_m, of |n|^2 for n in Z^E. There are finitely many values below any fixed number. The nonzero spectra of M Q M and Q^(1/2) M^2 Q^(1/2) agree, and the latter operator is at most Q. The finite-dimensional min-max principle and(5) give, for the ordered eigenvalues E_(j,k) of G_j,

    E_(j,k)>=a rho_k.                               (11)

The finite centered box contains a subset of the full integer lattice, so its kth kinetic value is at least rho_k. Restricting to any physical sector only increases the kth eigenvalue by min-max. Thus, for every fixed t>0,

    Tr exp(-tG_j)<=d_m [sum_(n in Z)exp(-t a n^2)]^E,
    sum_(k>K)exp(-t E_(j,k))<=sum_(k>K)exp(-t a rho_k).
                                                               (12)

The second tail tends to zero uniformly in j as K->infinity. Equation(10) and continuous functional calculus imply norm convergence of the embedded exp(-tG_j) to exp(-tH); the function of the resolvent eigenvalue r is exp[-t(1/r-1)], extended by zero at r=0. Spectral convergence plus(12) proves convergence of their traces.

For completeness, positivity upgrades these facts to trace-norm convergence. Choose a finite-rank projection F for which Tr((I-F)exp(-tH)) is small. Norm convergence controls the F block; trace convergence then makes the complementary traces small for the approximants too. For any positive trace-class B, the off-diagonal block obeys

    ||F B(I-F)||_1
       <=sqrt[Tr(F B) Tr((I-F)B)],

by factoring through B^(1/2) and the Hilbert-Schmidt Cauchy-Schwarz inequality. Decomposing into four blocks proves

    ||J_j exp(-tG_j) J_j*-exp(-tH)||_1->0.            (13)

The argument applies to the physical restrictions using the restricted resolvent convergence and the same majorant. Dividing by the positive limiting partition function gives trace-norm convergence of the normalized Gibbs density operators on every nonempty fixed physical sector. Hence expectations of all uniformly bounded operators converge under the same embedding.

The actual discrete transfer power has time t_j=delta_j floor(t/delta_j)->t. Replacing exp(-tG_j) by exp(-t_j G_j) changes its trace norm by at most

    |t-t_j| Tr[G_j exp(-min(t,t_j)G_j)].

For sufficiently large j, min(t,t_j)>=t/2; x exp(-t x/2)<=C_t exp(-t x/4), and(12) bounds the remaining trace uniformly. Thus(13) also holds for the actual integer power T_j^floor(t/delta_j).

## 7. Limits of this advance

The matching now reaches the actual finite-volume ground-space and Gibbs operators, not only smooth initial states. It still does not exchange the spatial thermodynamic limit with N->infinity or delta->0. The heat-trace majorant grows with the number of links, and the multiplier constant in(7) depends on the graph and coupling. A fixed-N, fixed-coupling phase or a volume-uniform anisotropic defect theorem remains open here. No native coupling, Hamiltonian, time parameter, matter representation or axiom update is derived.

This note imports only the cited classical theta identity and the explicitly stated Block02 construction. Its spectral and compactness arguments are supplied above. Floating finite examples test constants, multiplicities, Gauss reduction and noncommuting factors; they are not a substitute for the uniform estimates.
