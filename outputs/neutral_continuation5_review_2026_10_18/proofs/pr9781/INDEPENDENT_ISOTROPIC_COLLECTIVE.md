<!-- Original PR9781 source SHA256 508d662ac707d8f7d9a1fa96669ef888d2841125d9da6d5620f8d1a7b28dc0cd. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Isotropic maximal-spin sector: independent algebra check

Disposition: PASS. The result is an exact leakage boundary for the fully permutation-symmetric sector of the stated isotropic native Hamiltonian, including its entangled states. It is not a no-go for general collective features. Read /tmp/neutral_isotropic_collective_root.md; no shared files edited.

For N distinct spins on the periodic cubic lattice, each axis has N undirected bonds. Permutation compression gives

 P sigma_i^alpha sigma_j^alpha P=[4S_alpha^2-N]/[N(N-1)] P, i!=j.

Since S=N/2 and sum S_alpha^2=N(N+2)/4, summing the three axis families yields PHP=-JN P exactly. This is a scalar compression, not invariance of P.

## Coherent-state leakage and operator reconstruction

An independent direct check avoids relying only on covariance bookkeeping. In the product coherent state, each bond has a two-spin-flip amplitude of modulus J(1-n_alpha^2). The one-spin-flip contributions from all six neighbors cancel because the isotropic local mean field is parallel to n. Distinct bonds give distinct two-flip configurations. The zero-flip contribution is exactly -JN. Hence

 ||(H+JN)|n>^N||^2=J^2 N sum_alpha(1-n_alpha^2)^2
 =J^2 N[1+sum_alpha n_alpha^4].

This agrees with the draft's covariance count: same-axis adjacent unordered pairs number N per axis, and cross-axis adjacent unordered pairs number 4N per axis pair. No duplicate bond or wrapped short-cycle correction arises under the stated lengths.

For completeness, the independent fourth-moment expansion for one component is

 16<S_alpha^4>=3N^2-2N
  +[4N(N-1)+6N(N-1)(N-2)]n_alpha^2
  +N(N-1)(N-2)(N-3)n_alpha^4.

Summing over alpha gives precisely A0=(6N^3-5N^2+2N)/16 and D4=N(N-1)(N-2)(N-3)/16. Thus the coherent-state expectation of the proposed quartic operator equals that of L=P H(1-P)H P=P(H+JN)^2P for every n. Spin-S coherent-state projectors span the operator space on the irreducible maximal-spin representation (equivalently, their spherical harmonics detect every tensor rank through 2S). The coherent Q symbol is injective, so this determines the operator, not just its product-state diagonal:

 L=J^2 N[1+(sum_alpha S_alpha^4-A0)/D4]P.

## Lower bound for every symmetric vector

Let C=S(S+1). The operator sum_alpha(S_alpha^2-C/3)^2 is positive and expands to sum_alpha S_alpha^4-C^2/3, with no cross-component commutation assumption required. Substitution and simplification yield exactly

 L >= [4J^2 N(N-1)(N-6)/(3(N-2)(N-3))]P.

For N>6 this is strictly positive. Hence every normalized vector in P, including arbitrary symmetric entangled/cat states, obeys

 ||(1-P)H psi|| >= |J| sqrt[4N(N-1)(N-6)/(3(N-2)(N-3))].

For the stipulated positive J the draft's sign convention is correct. The lower bound is asymptotic to J sqrt(4N/3). It excludes any exact H eigenvector lying wholly in P. It does not alone give a finite-time leakage probability uniformly in N: higher global energy moments can grow with N, so a global survival-time interpretation would require another estimate.

## Local magnetization

The initial product state is an eigenvector of the total n magnetization with value N. The only nontrivial first-order amplitudes are the two-flip bond states above, each lowering that magnetization by four. Thus the normalized magnetization has exactly

 m_n(t)=1-4J^2[1+sum_alpha n_alpha^4]t^2+O(|Jt|^3).

No factor of two or bond-count factor is missing. A rigorous volume-independent remainder follows by applying the third-order Heisenberg Taylor formula to each local n.sigma_i: only connected sequences of three bonds meeting its successively enlarged support contribute, so the third nested-commutator norm is at most C|J|^3 with C depending only on the bounded local degree. Unitary conjugation in the integral remainder preserves this bound. Averaging over i leaves the same constant, independent of N and n. Thus a sufficiently small fixed nonzero time has a nonvanishing magnetization loss uniformly in volume; this is a local short-time statement.

The conclusions use the unchanged isotropic native interaction and a specified maximal-spin sector or coherent initial state. They provide neither a long-time decay law, lifetime, gap, nor exclusion of lower-spin spatially structured or dressed collective states. The flat projected orientation energy must not be used as an invariant effective sector without accounting for the proven leakage.

## Constructive dimer trial and actual-ground weight: confirmed

PASS for the added even-x periodic family and positive J. On a matched x bond, the state cos(theta)|00>+sin(theta)|11> has <XX>=sin(2theta), <Z> on each site =cos(2theta), and <X>=<Y>=0. There are N/2 matched x bonds. Every unmatched x bond and every y bond connects different dimers, so its XX or YY expectation vanishes. Each z bond likewise connects different dimers and has ZZ expectation cos^2(2theta). Therefore

 E_trial/N=-J[cos^2(2theta)+(1/2)sin(2theta)].

Writing s=sin(2theta), the bracket is 1-s^2+s/2=17/16-(s-1/4)^2. Thus s=1/4 gives exactly E_trial=-17JN/16 and Eg<=-17JN/16. This uses the original interaction and is only a variational upper bound, not an identification of a dimerized ground phase.

The component operator inequality S_alpha^4<=S^2 S_alpha^2 follows from the spectrum |S_alpha|<=S. Summing gives sum S_alpha^4<=S^3(S+1). Substitution into the already checked exact leakage operator yields

 L<=M P, M=2J^2 N(N-2)/(N-3).

Since L=(PHQ)(QHP), this is also ||PHQ||^2<=M. For any normalized exact ground vector psi and w=||Ppsi||^2, projecting the eigenvalue equation gives

 (Eg+JN)Ppsi=PHQ Qpsi,
 (Eg+JN)^2 w<=M(1-w).

The variational bound guarantees |Eg+JN|>=JN/16. Consequently

 w<=M/[(JN/16)^2+M]
  =512(N-2)/[N(N-3)+512(N-2)].

All constants and factors are correct. The bound tends to zero as O(1/N) and is uniform over every vector in a possibly degenerate exact ground space; averaging also gives the same bound for any exact-ground density. It does not assume that the variational state is close to the ground state.

The dimer calculation needs even Lx>=4 and transverse periods at least three to avoid bond degeneracies. The earlier stated larger-period family is a safe common domain for both results. The H^2 leakage counting also remains valid for distinct nearest-neighbor bonds on the smaller periods specified here; no triangle term enters that second-moment calculation. One may simply retain the larger common family if avoiding a separate geometry statement.

This strengthens the maximal-spin exclusion to vanishing actual-ground weight in that sector. It does not exclude spatially structured entangled ground states, other low-energy collective modes, or all large features.

## Exact first leakage channel and infrared norm: confirmed

PASS. For a coherent product oriented along n, define a_alpha=<n-|sigma_alpha|n+>. The spinor identities sum n_alpha a_alpha=0 and sum a_alpha^2=0 are exact. The first cancels the one-flip amplitudes; the residual after subtracting -JN is the two-flip vector with bond coefficient -J a_alpha^2. Acting with total S_n^+ gives at each site the sum of its incident bond coefficients, -2J sum a_alpha^2=0. The residual has S_n^z eigenvalue Smax-2. In a decomposition into total-spin irreducibles, a vector at this magnetic quantum number killed by the raising operator can have only total spin Smax-2; components of higher spin have strictly positive raising norm. Thus this is not merely an expectation-value assertion.

Every coherent state in P gives a residual in the same total-spin eigenspace (the quantization axis changes, but total S^2 does not). Coherent vectors span P and PHP=-JN P, so linearity proves

 range[(1-P)HP] subset {S_total=Smax-2}

for all symmetric input vectors, including entangled ones. This identifies the first H-induced leakage channel only; subsequent actions of H need not remain there.

For n=z, a_x=1 and a_y=i in a conventional spinor phase, hence the residual is exactly J sum_r(s_r^-s_(r+ey)^- -s_r^-s_(r+ex)^-)|up>. With b_k^dag=N^-1/2 sum_r exp(ik.r)s_r^-, Fourier inversion gives the stated J sum_k F(k)b_k^dag b_-k^dag|up>, F=cos ky-cos kx. Its leading small-k term is (kx^2-ky^2)/2. No bosonic commutation relation is used.

The exact pair-state Gram matrix is

 <up|b_-k b_k b_k'^dag b_-k'^dag|up>
 =delta_(k,k')+delta_(k,-k')-2/N,

including self-inverse lattice momenta. Thus for an inversion-symmetric cut and real even F,

 ||J sum_cut F(k)b_k^dag b_-k^dag|up>||^2
 =2J^2 sum_cut F(k)^2-(2J^2/N)|sum_cut F(k)|^2.

The final term vanishes if the cut AND momentum mesh are invariant under exchanging x and y. This is automatic for an equal-side cubic torus with a symmetric ball; it is not automatic for an arbitrary rectangular torus with different x/y periods. Retain the exact Gram correction in that case.

For the cubic thermodynamic continuum approximation, the angular mean of (kx^2-ky^2)^2/4 is r^4/15. Therefore

 integral_(|k|<=kappa) (kx^2-ky^2)^2/4 d^3k=4pi kappa^7/105,

 sum_cut F^2 ~ N kappa^7/(210pi^2),
 ||filtered leakage||^2 ~ J^2 N kappa^7/(105pi^2).

The draft's “before factor two” value is correct, and the final coefficient supplied in the task is correct. More precisely the small-k expansion has relative O(kappa^2) corrections, together with the finite-mesh error; the continuum limit requires L kappa tending to infinity (or first taking L to infinity at fixed small kappa). Relative to the exact total z-oriented leakage norm squared 2J^2N, the fraction is kappa^7/(210pi^2) to leading order.

This is a diagnostic momentum-filtered spin-pair vector, not an invariant dynamical subspace or a canonical-boson occupation. It shows strong infrared suppression of this particular first leakage form factor and does not exclude other scalar or dressed collective channels.
