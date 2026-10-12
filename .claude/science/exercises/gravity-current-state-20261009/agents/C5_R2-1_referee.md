# VERDICT: CONFIRMED WITH CORRECTIONS

The central finite-fibre obstruction is sound after making one missing global-analyticity premise explicit (or, equivalently in the scalar $W(B_4)$-covariant case, using reflection parity to remove the energy term).  The worker's free perfect-action and Whitney calculations reproduce.  The corrections are material to scope: H4 assumes rather than derives the asymptotic additive charge; written H5 does not contain the analytic one-particle Hamiltonian used in Step 5; the determinant proof excludes finite fibre but does not by itself classify every infinite-fibre escape as the displayed complete ladder; and the Gaussian time-blocked proxy fails OS reflection positivity, so its poles are not established physical one-particle states.  The fixed reading is therefore supportable only as a bounded one-particle statement, not as an unconditional class-wide or microscopic theorem.

## 1. Theorem T

### Constant-ξ reduction

Confirmed at classical/tree order with the report's ordinary κ power counting and a flat background whose tadpole is removed.  At $h=0$, the leading graviton variation is $D\xi$, so it vanishes for constant ξ; terms containing an explicit $h$ vanish; a seagull starts at $h^2$; and an $O(\kappa)$ matter-dependent correction to δh multiplies the $O(\kappa)$ matter source in δS/δh and is therefore $O(\kappa^2)$.  Thus the $O(\kappa\lambda)$ on-shell Ward identity is the matter translation identity stated at `R2-1_report.md:91-97`.  This agrees with the independently refereed constant-ξ reduction in `RFW_F2_referee.md:3`.  The report should say explicitly that a quantum Jacobian is loop order and cannot cancel this tree identity under a regular ℏ expansion; otherwise the phrase "full interacting matter action ... to all orders" at `R2-1_report.md:95` is stronger than what is needed.

### OS reconstruction and collision invariants

Conditional, not independently derived from reflection positivity.  H4 itself assumes that the charge acts additively on asymptotic states (`R2-1_report.md:43`); OS reconstruction alone does not guarantee an unbroken, well-defined quasi-local charge, LSZ scattering, or cluster additivity.  Given those assumptions, conservation and a nonzero elastic amplitude in the same simple one-particle channel do imply

\[
\tau(k_1)+\tau(k_2)=\tau(k_3)+\tau(k_4),
\]

and analyticity/continuity extends the equality through isolated zeros of the amplitude on a connected regular shell, as asserted at `R2-1_report.md:99-101`.  For the advertised matrix/auxiliary-field generality, H2 should also say that the nonzero near-threshold amplitude connects the charge eigenbranch carrying the H3 slope; "not identically zero" somewhere in matter space is not enough.

### Local lemma

Essentially correct, with a compressed step.  At every nearby centre $c'$, fixed total momentum $2c'$ makes $g=\tau(k)+\tau(2c'-k)$ constant on regular level sets of $h=\omega(k)+\omega(2c'-k)$.  Expanding about $c'$ gives $H_\tau(c')=a(c')H_\omega(c')$.  Differentiating this relation and using symmetric third derivatives gives

\[
(\partial_l a)H_{\omega,ij}=(\partial_i a)H_{\omega,lj};
\]

if $\nabla a\ne0$, every column of $H_\omega$ is parallel to $\nabla a$, contradicting nondegeneracy in $d\ge2$.  Hence $a$ is constant and integration gives $\tau=a\omega+b\cdot k+e$.  The report's `R2-1_report.md:103-108` should state that the construction is repeated as the centre varies and should restrict to a simple analytic branch (or a taste block on which the charge slope and scattering are universal).  This is consistent with the qualifications on the related collision lemma at `RC_C1_referee.md:7-9`.

### Determinant and analyticity

The mathematical argument is correct once its matrix premises hold.  Put $A(k)=P_j(k)-aH_1(k)-eI$ and $F(k,z)=\det(A(k)-zI)$.  It is $F$, not $\chi(k)=F(k,b\cdot k)$, that is periodic in $k$.  Since χ is real analytic and vanishes on an open set, χ vanishes on all of connected $\mathbb R^3$.  Therefore, for fixed $k$ and every $n\in\mathbb Z^3$,

\[
0=\chi(k+2\pi n)=F(k,b\cdot(k+2\pi n)).
\]

Choosing an integer direction with $b\cdot n\ne0$ gives infinitely many distinct roots of the degree-$N$ characteristic polynomial $F(k,\cdot)$, an impossibility.  Thus the nonperiodicity highlighted in the prompt is the engine of the proof, not a defect.

There is nevertheless a hypothesis defect in the written theorem.  H5 states analyticity and periodicity only for $P_j(k)$ (`R2-1_report.md:45-46`), while Step 5 says without basis that a globally periodic analytic $H_1(k)$ is "assumed analytic in H5" (`R2-1_report.md:113-116`).  Repair this by adding a global finite-dimensional real-analytic periodic one-particle Hamiltonian matrix, with the local physical state a common energy/charge eigenvector.  In the nondegenerate scalar $W(B_4)$ case one may instead use reflection parity to set $a=e=0$ for a spatial-vector charge and apply the determinant directly to $P_j-b_jk_jI$.  Without one of these repairs, Theorem T is not literally proved under the printed H1-H6.

Finally, the determinant establishes "finite $N$ is impossible."  It does not, without additional global spectral-continuation/Fredholm assumptions, prove that every possible infinite-dimensional escape contains exactly the displayed pure-point ladder.  The complete ladder is explicitly realized by the free blocked example, but `R2-1_report.md:117-122` overstates what follows for an arbitrary infinite fibre.

## 2. Perfect/Ginsparg-Wilson proxy and collision numerics

The worker scripts reran.  The free remnant is odd and imaginary and the quadratic-form residual is $2.63\times10^{-17}$ (`scripts/r21_perfect_remnant.out:1-4`).  An independent implementation at $L=64,128$ gives stable axis fits $1.351716$ for $G^{-1}$ and $1.304143$ for $T_1$ (`R2-1_referee_checks.out:1-3`; implementation at `R2-1_referee_checks.py:19-55`).  This confirms the reported free two-dimensional axis decay, but a finite fit is not itself a uniform strip-width proof; the interacting remnant remains expressly open at `R2-1_report.md:156-169`.

At a generic fixed $k_1$, the term with spatial alias $n$ has $k_0=iE_n$, $E_n^2=m^2+(k_1+2\pi n)^2$, and

\[
\operatorname{Res}G=\frac{e^{\sigma m^2}}{2iE_n},\qquad
\frac{\operatorname{Res}N_1}{\operatorname{Res}G}=i(k_1+2\pi n),\qquad
\frac{\operatorname{Res}N_0}{\operatorname{Res}G}=-E_n.
\]

The independent values agree digit for digit for $n=0,1,-1,2$ (`R2-1_referee_checks.out:4-8`; formula at `R2-1_referee_checks.py:64-79`) and reproduce `scripts/r21_perfect_remnant.out:18-29`.  "Undiminished" should mean "no extra Gaussian alias suppression": the ordinary $1/E_n$ residue still decreases with energy.  At the special momenta $k_1=0,\pi$, opposite aliases can be energy-degenerate, so the scalar residue ratio is their weighted combination rather than a separately resolved ± momentum; the stated pole-by-pole action is clean at generic $k_1$, including the tested $0.7$.

A further physical qualification is required.  The same Gaussian time blocking violates necessary OS reflection-positivity conditions.  With the exact unfolded temporal covariance (including the required $1/E_n$ factor, derived at `R2-1_referee_checks.py:82-100`), both link- and site-reflection $2\times2$ Hankel determinants are negative: $-2.2484\times10^{-3}$ and $-1.8292\times10^{-4}$, respectively (`R2-1_referee_checks.out:9-13`).  Hence these are verified Euclidean poles and remnant eigenvalues, but not an OS-reconstructed physical tower satisfying H4.  This sharpens the report's own warning at `R2-1_report.md:179`.

The collision outputs also reproduce.  In particular, the $d=2$ soft-ball-constrained residual decreases from $1.0198$ to $0.1650$ (`scripts/r21_collision_d2.out:1-9`), so the safe conclusion is exactly the report's: the calculations illustrate improving approximate charges and do not supply a numerical lower bound; only the analytic exact obstruction is at issue (`R2-1_report.md:133-137`).  Minor reproducibility issue: `scripts/r21_collision_d2.py:6` assumes the current directory is `scripts/`.

## 3. Whitney blocking

Confirmed as an exact kinematic orbit-intertwining identity.  For $m\ne n$, integrating $\partial_m\xi_n$ over the plaquette and using the fundamental theorem of calculus gives $D_m\Xi_n$, and the other term gives $D_n\Xi_m$.  On the diagonal, the factor $1/2$ cancels the $2\partial_n\xi_n$, and the two-link tent integral gives $D_n\Xi_n$.  This proves the relation for arbitrary sufficiently regular ξ, stronger than the displayed symbolic test; the implementation and its four zero residuals are at `scripts/r21_whitney_blocking.py:19-41` and `scripts/r21_whitney_blocking.out:1-6`.

What is proved there is the blocking-map identity at $\kappa^0$.  Exact invariance of a fully defined blocked Fierz-Pauli functional additionally requires the quotient/gauge-fixing and measure construction that the report itself calls formal at `R2-1_report.md:145-149`.  Nothing in this check establishes the interacting nonlinear closure requested at $O(\kappa^2)$.

## 4. Counting and fixed reading

Within K1's quadratic operator space, an exact linear identity removes the three mass forms and restricts the nine two-derivative forms to their unique gauge-invariant combination, so the codimension $3+8=11$ is correct (`C4_K1_referee.md:3,15`; `R2-1_report.md:185-189`).  The absence of an exact matter identity removes symmetry protection; it does not prove that every one of the eleven coefficients is radiatively generated in every law.  K1 found one representative non-Einstein loop vector, not eight independent generated directions (`C4_K1_referee.md:9`).  Accordingly `R2-1_report.md:193` should read "all eleven require tuning in the generic quadratic theory," not "all eleven stay unprotected" as if nonzero generation were universal.

Under the fixed definitions at `TESTS.md:2485-2489`, PASS is not met because no interacting quasi-local construction through $O(\kappa^2)$ is supplied.  Literal FAIL is not met because the proof is restricted by H1-H6 (and needs the analytic-matrix repair above), while finite fields per site do not imply finite one-particle fibre.  COLLAPSES-TO-A is the best reading only in the registered bounded sense: in the repaired regular OS/asymptotic finite-fibre class, an exact identity is already impossible at $O(\kappa\lambda)$, so any realization must leave that class through an infinite one-particle fibre, nonanalytic/nonlocal structure, loss of OS/asymptotic assumptions, degeneracy, or another listed exclusion.  The result is one-particle/spectral, not a theorem that the microscopic site ontology is continuum; that distinction agrees with `C4_I1_referee.md:15,21` and is acknowledged at `R2-1_report.md:232-235`.

## Strongest correct statement

For a quasi-local $\mathbb Z^4$ law with a flat-background exact identity, an unbroken additive asymptotic charge on the same interacting simple scalar band, nondegenerate analytic near-threshold dispersion in $d\ge2$, and globally periodic real-analytic finite-dimensional one-particle charge and Hamiltonian matrices (or scalar $W(B_4)$ parity eliminating the energy admixture), constant ξ reduces the $O(\kappa\lambda)$ Ward identity to an additive collision invariant, local collisions force $\tau=a\omega+b\cdot k+e$ with $b\ne0$, and analytic continuation makes a fixed finite matrix have infinitely many distinct characteristic roots, which is impossible; thus an exact identity in this regular class requires leaving finite fibre, and the appropriate fixed reading is **COLLAPSES-TO-A (bounded, at the one-particle/spectral level)**.  The Gaussian $d=2$ blocked proxy independently confirms an exact free remnant, exponential axis decay, generic alias poles, continuum residues, and alias-momentum action, but it fails OS reflection positivity and has no established quasi-local interacting remnant; the Whitney calculation independently confirms only the exact local $\kappa^0$ graviton blocking identity.
