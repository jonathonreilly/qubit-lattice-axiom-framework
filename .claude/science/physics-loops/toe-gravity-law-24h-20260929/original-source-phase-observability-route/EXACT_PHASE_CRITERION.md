# What an actual finite-torus phase certificate must prove

Author reconstruction for the unchanged original rotor law. This criterion does not assert its full-rank hypothesis. It specifies the real algebraic target, its source-sensitive alternative, and why the cube's small certificate cannot simply be reused.

## 1. Complete physical matrix, including the original loss

Fix even L, n=L³/2, odd k<=n-1, W1 and total charge n. Put M=n-1+k and r=(k-1)/2. A physical matter label consists of the A hole, an occupied-B set of size k, and r minus charges among the M occupied sites. Its full finite fiber dimension is

 d_f=n binomial(n,k) binomial(M,r).                      (P1)

A spanning-tree Gauss representation has d_c=4n+1=2L³+1 integer cycle coordinates. Each actual two-hop term of H=C+[F,F*] is a Laurent monomial of total absolute degree at most2 in z_1,...,z_(d_c), with its original occupation gates, charge permutations and sign. No field cutoff is present. The matrix is Hermitian on the unit torus. G is diagonal, equal to twice the number of empty B neighbors of the hole. Original coherent and resolved marks have the same G but still have their separate j_mu(z) outputs.

Use G rather than a phase-dependent square root to form the Laurent observation matrix

 O(z)=[G; G H(z); ...; G H(z)^(d_f-1)].                  (P2)

Zero rows may be omitted. Let N(theta)=ker O(exp(i theta)). Cayley--Hamilton implies that it is the largest H(theta)-invariant subspace contained in ker G. Because H is Hermitian, N and its orthogonal complement reduce H; G vanishes on N and preserves its complement. Thus for the actual no-original-event semigroup

 S_theta(u)=exp[u(-i delta H(theta)-kappa G/2)],
 lim_(u->infinity)||S_theta(u)v||²=||P_N(theta)v||².      (P3)

On the complement there is no imaginary-axis eigenvalue: its real-part identity would force a vector into ker G and then into N. A finite-dimensional matrix exponential therefore decays there, regardless of nonnormality or Jordan blocks. On N it is unitary. No phase-uniform spectral gap is needed for(P3).

For every physical normalizable rotor vector, direct-integral dominated convergence gives the terminal no-event mass as the norm of its decomposable dark projection. For a positive trace-class input rho, the result is Tr(P_N rho). Equivalently, decompose rho into positive rank-one terms and integrate their fiber norms. This is not a dephasing operation and does not identify a trace-class operator with a diagonal multiplication kernel on a nonatomic angle space. Original first-mark outputs remain sqrt(kappa)j_mu S(u); their total mass is Tr rho-Tr(P_N rho) by the exact loss identity.

## 2. Algebraic dichotomy and finite-field counterexample certificates

The following statements are equivalent for the COMPLETE sector:

(i) N(theta)=0 for almost every physical phase.
(ii) O has full column rank over the fraction field of the Laurent-polynomial ring.
(iii) At least one d_f by d_f minor of O is a nonzero Laurent polynomial.
(iv) There is no nonzero Laurent-polynomial vector v(z) with O(z)v(z)=0.

A nonzero Laurent polynomial has a Haar-null zero set by elementary induction/Fubini in its variables. Thus one exact nonzero minor proves(i); an exact evaluation at any nonzero complex z which certifies a nonzero polynomial is also sufficient, although Hermiticity is used only on the physical unit torus. An approximate sampled rank or an assumed graph-controllability theorem is not such a certificate.

Conversely, if the rank is deficient over the fraction field, rational Gaussian elimination gives a nonzero rational null vector. Multiplying by a common Laurent denominator produces the vector in(iv). Cayley--Hamilton and(P2) imply

 G H(z)^m v(z)=0 for EVERY m>=0.                         (P4)

Its inverse physical Fourier transform is a finite linear combination of actual charge/Gauss field words, hence normalizable with every polynomial field moment finite. Equation(P4) implies that its entire H orbit is dark and its original no-event norm is exactly constant. Thus a positive-measure unobservable branch would not require an exotic nonnormalizable phase preparation: it admits a finite-field algebraic dark vector. No such vector is constructed in this packet.

This is an existence/certificate dichotomy for the actual matrices, not a replacement by a generic connected matrix. The gates, charge transports, all B masks and original G are fixed in(P1)-(P2). Connectivity alone does not decide whether their minors vanish identically. The old global H=FF* factorization is false and cannot be used to count this kernel.

## 3. Actual-source domain and a sufficient negative certificate

For an injection into k, the actual leading positive map is B_mu^+=-F_a j_mu F_a acting on W0 with N_B=k-3. The actual fixed-graph source is

 tau_a(s)=sum_(mu@a) B_mu^+ rho_eff(s)(B_mu^+)*,

where rho_eff is the full original W0 rotor target from bare Omega, including its diagonal electric term, H4, every later ordinary b_mu=j_mu F_a event, and original coherent/resolved mark convention. Its phase distribution is not freely selected. The limiting initial rotated one-hole input has k=1, already in the direct-loss scope; that does not settle the later injected k sectors.

All-source strong absorption follows from(i), but a weaker source theorem would only need Tr(P_N tau_a(s))=0 for every actual s. Rank deficiency alone would not disprove that source-specific statement.

There is a concrete sufficient negative certificate: find a nonzero Laurent null vector v as in(iv), and a LEGAL complete original zero-waiting-time word

 Phi(z)=B_mu^+(z) b_(mu_m)(z)...b_(mu_1)(z) Omega

such that the Laurent scalar v(z)*Phi(z) is not identically zero on the unit torus. No path summand may replace a complete coherent mark. Multiplying v by a suitable scalar Laurent monomial then produces a normalizable finite-field dark test vector with nonzero full-Hilbert overlap with Phi. This follows by taking a nonzero Fourier coefficient of the displayed scalar; scalar multiplication preserves(P4).

The actual effective no-event propagators and original jumps are strongly continuous on the finite-word inputs in this fixed graph. Inserting sufficiently small positive waiting durations into the word therefore preserves a nonzero overlap with that bounded-norm dark test. The positive quantum-jump expansion of rho_eff(s) then gives a strictly positive terminal survival contribution for every sufficiently small s>0, with the genuine original m-mark simplex weight. This would be an ACTUAL sourced positive-measure counterexample, not merely an isolated dark fiber. No such pair(v,Phi) has been found here.

Conversely, checking only zero-waiting-time birth words for orthogonality is NOT enough to prove source stability: the actual interspersed K D+delta H4 no-event motion may rotate their source domain. A positive source theorem must control that full orbit or prove the stronger all-sector statement(i). The previously proved smooth-source polynomial LOWER tail near a flat phase does neither. It excludes exponential uniformity while remaining compatible with(i).

## 4. An exact resource and depth obstruction to copying the cube method

For k>=6 the dark and bright charge dimensions are

 d_dark=n binomial(n-6,k-6) binomial(M,r),
 d_bright=n[binomial(n,k)-binomial(n-6,k-6)]binomial(M,r). (P5)

A hole is dark precisely when its six distinct neighboring B sites are occupied. These counts include all charge labels and do not count a coherent mark as two different losses. With k=n-1,

 d_f=n² binomial(2n-2,(n-2)/2),
 d_bright=6n binomial(2n-2,(n-2)/2).

The stack through power R has rank at most(R+1)d_bright. Full observability in this dense physical sector therefore needs at least

 R>=ceil(n/6)-1.                                        (P6)

The cube's 72-by24 single bright/dark block is not a template with a fixed Krylov depth. Here the dark-dark block is genuinely nonzero; the already checked lambda=2 flat-phase strip is an explicit example. A P_bright H P_dark injectivity argument is dimensionally impossible in dense large sectors.

More sharply, for every R with(R+1)d_bright<d_f, the truncated Laurent stack has a nonzero polynomial null vector by the same fraction-field argument. It supplies some finite-field physical state with G H^j v=0 for j<=R. This is a finite dark PREFIX, not an invariant dark vector or an actual Omega source. It does not determine the rank at the full depth(P2). It explains why a shallow sparse rank sample cannot prove the requested generic-phase theorem.

No enormous matrix was assembled and no rank was numerically sampled. The counts(P1),(P5)-(P6) are analytic resource prices. An exact all-sector proof needs an actual structural elimination or a controlled full Laurent certificate. The partial staircase/slab proof gives such an elimination for one restricted spatial question only; it does not produce the missing full-rank minor.
