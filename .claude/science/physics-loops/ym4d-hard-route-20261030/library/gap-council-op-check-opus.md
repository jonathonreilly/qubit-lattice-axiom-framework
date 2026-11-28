# Check of gap-council-op-astra.md (FINISH row 1136)

Status: done, 2026-11-18 03:01Z (date -u). All six steps written; RESULT line at the end.
Scope: Sections 2 and 3 of the file under check (L23-90). Sections 1, 4 and 5 were read
for context and are not checked here, except the definition at L21 that L37 uses.

Checker role: line-by-line check of `library/gap-council-op-astra.md`.
Setting: `library/gap-council-brief.md`.

Checker: Claude Opus 5.5 (max effort), laptop subagent. The file under check is by
gpt-6.2-astra (row 1132), so this is a cross-provider check. All line numbers below refer
to `library/gap-council-op-astra.md` as read on 2026-11-17 (106 lines, 24506 bytes).

Note on the save protocol: the first tool call created this file with a header only. The
plan below was added by the second write. No check result was written before the plan.

## Plan (six steps)

1. Consumer of (A), L37: Jensen on the residual, the multiplier (2j+1)^(-2), the norm 1/4,
   the bound 1 - 3p/4, the passage to (Z-UNB) and the one-size form. Check against row 720.
2. Comparison lines: U(1) and product (L39); frozen Q_8 and 2T (L41).
3. Moser construction and equivariance (L27); the multiplier identity W = (1 - Delta)^(-1)
   (L49); the equivalence of (A) with the sign test on g (L51).
4. One-step obstruction above beta = 1/3 (L53-59); disjoint-plaquette Chebyshev bound
   (L61-63).
5. Twelve-step pass with a_d at most (13/20)^(d-1) (L65-72); fixed-box bound with A_1, B_1
   (L74-80); the (1 - 6 beta) example (L82-88).
6. The other lines of Sections 2-3 (L25, L29-35, L43, L45, L90); numeric guide; verdict
   table; RESULT line.


## Step 1. The consumer of (A), L37 (with the set-up of L19 and L29)

Sources read for this step: `library/gap-phys-seed.md` L276-281 and L311-336 (row 720,
Theorem ZD-c); the account's outline (`YM4_sketch_500.tex`) lines 2195-2247, (GL3)-(GL4);
`library/gap-vortex-astra.md` (6) (row 778).

Set-up used (L19, L29), checked first. $T=MC_EPM$ has a real symmetric, smooth, strictly
positive kernel; $C_E$ and $M$ commute with gauge maps and centre flips, so $P$ commutes
with $C_E$ and $T$ is a positive operator. With $S_\#H=\pi=\psi^2\,dU$, the joint law of
two stationary slices in the coordinates $S^{-1}$ has density
$j_k(x,y)=T^k(Sx,Sy)/[\lambda_0^k\psi(Sx)\psi(Sy)]$ with respect to $H\otimes H$: the joint
density with respect to $\pi\otimes\pi$ is $T^k(U,V)/[\lambda_0^k\psi(U)\psi(V)]$, and
pulling back by $S\times S$ keeps it. Both marginals are one by $T\psi=\lambda_0\psi$.
$V_Sf=f\circ S$ is unitary from $L^2(\pi)$ to $L^2(H)$ and $J_kV_S=V_SP_0^k$, so
$\|J_k\|_{L^2_0(H)}=\|P_0^k\|_{L^2_0(\pi)}$. Also $J_k=J_1^k$ (compose the kernels and use
$S_\#H=\pi$). The non-invariant part of $L^2$ is killed by $T$, so the mean-zero norm
equals the norm on the gauge-invariant mean-zero space with all eight flux sectors.
Verdict on this set-up: HOLDS.

1a. "The residual divided by $1-p$ is a Haar-stationary Markov kernel when $p<1$." Put
$R(x,dy)=j_k(x,y)H(dy)-p(rW_E)(x,dy)$. By (A) it is a positive measure for $H$-a.e. $x$.
Its mass is $1-p$. $HR=H-pHrW_E=H-pH=(1-p)H$, using the $y$-marginal one, $Hr=H$ and
$HW_E=H$. HOLDS.

1b. "Such kernels preserve means and contract $L^2$ by Jensen." For a Markov kernel $Q$
with $HQ=H$: $\int Qf\,dH=\int f\,dH$ and
$\|Qf\|_2^2\le\iint Q(x,dy)f(y)^2H(dx)=\|f\|_2^2$. HOLDS.

1c. "The commutator multiplier on spin $j$ is $(2j+1)^{-2}$." Row 778 (6):
$\mathbb E\,D([a,b])=I/d^2$ (Schur twice; re-derived here by hand). For a matrix
coefficient $f(z)=D(z)_{mn}$, $(W f)(z)=\mathbb E f(zc)=\sum_l D(z)_{ml}\,\mathbb E D(c)_{ln}
=d^{-2}f(z)$. The commutator law is central, so left and right convolution agree. HOLDS.

1d. "$\|W_E\|_{L^2_0(H)}=1/4$ for any nonempty finite $E$." On the Peter-Weyl block with
spins $(j_e)$ the multiplier is $\prod_e(2j_e+1)^{-2}$. Mean zero means some $j_e>0$. The
supremum $1/4$ is attained with one $j_e=1/2$ and all others $0$. HOLDS. (On the
gauge-invariant subspace the norm is smaller; the bound $1/4$ is all that is used.)

1e. "$\|P_0^k\|_0\le1-3p/4$ also on the physical subspace." $J_k=p\,rW_E+(1-p)Q$ with
$Q=R/(1-p)$. For $f\perp1$: $\|rW_Ef\|\le\|W_Ef\|\le\|f\|/4$ ($r$ is an $L^2$ contraction
by 1b, since $Hr=H$) and $\|Qf\|\le\|f\|$. So $\|J_kf\|\le(p/4+1-p)\|f\|$. Transport by
$V_S$. HOLDS. In general form the bound is $1-p(1-q_G)\le1-\delta$.

1f. "At fixed $L$, the lower cutoff limit of $na\,m_{\rm phys}$ is at least
$(L/t)[-\log(1-3p/4)]$." From $e^{-ka\,m}\le1-3p/4$ and $ka\le t$ ($k=\lfloor t/a\rfloor$):
$m\ge c/t$ with $c=-\log(1-3p/4)\ge3p/4>0$ (since $-\log(1-u)\ge u$). Then $Lm\ge Lc/t$ for every $j\ge j_0(L)$, so the lower limit over $j$ is at least $Lc/t$.
HOLDS. Units agree with row 720: $na\,m_{\rm phys}=n\,m_{\rm lattice}$, and row 720
defines $z^-(L)$ as the lower limit over $j$ of $(L/a_j)m_j((L/a_j)^3)$, with $m_j$ the
lowest gap of the whole space of the cube, flux sectors included (L311, L328).

1g. "This grows along dyadic $L$ and supplies Z-UNB." Row 720 takes
$\mathcal P=\{2^il_1\}$ with $l_1/(4a_j)$ an integer at least 3; it is closed under
doubling, so $2^hL_0\in\mathcal P$, and "unbounded" means: for every $C$ and $L'$ some
$L\ge L'$ in $\mathcal P$ has $z^-(L)>C$. With $z^-(2^hL_0)\ge2^hL_0c/t$ this holds.
The uniformity of $t,p$ over all $L$ and $j$ is what (A) asks (L29, L35). HOLDS.

1h. One-size version: "$(L/t)[-\log(1-3p/4)]>2\limsup_j\Phi_{4,j}(n/4)+30$". Row 720's
(Z-SEED) is $z^-(L)>2\psi^+(L)+30$ with $\psi^+(L)=\limsup_j\Phi_4(L/(4a_j);\beta_j)$ and
$\Phi_4(m)=256F(m^4)-F((4m)^4)$, $F=\log Z$ (`gap-phys-seed.md` L276, L315). The note's
only definition of the symbol is L21: "$\Phi_4(m)=16\log Z(m^4)-\log Z((2m)^4)$". That is
the one-doubling defect $\Phi_2$, the error of the first version of the brief, which the
lead corrected on 2026-11-18. With row 720's $\Phi_4$ the clause gives (Z-SEED) at that
$L$ directly. With the L21 definition it does not. By hand,
$\Phi_4(m)=16\Phi_2(m)+\Phi_2(2m)$, and $\Phi_2\ge0$ (halve each of the four sides with
$\mathrm{Tr}\,T^{2b}\le(\mathrm{Tr}\,T^b)^2$ and the symmetry of $Z$, as in Lemma A of
`gap-crux-restate.md`). So the L21 quantity is the smaller right side, and the clause with
it is weaker than (Z-SEED). HOLDS AFTER CORRECTION: read
$\Phi_{4,j}(m)=256F_j(m^4)-F_j((4m)^4)$ in L37 and in L21.

1i. "Both formulations leave the free-energy input visible. The all-size argument needs
BDD-Delta for the brief's wall." Theorem ZD-c: (PHYS-SEED) is equivalent to (BDD-Delta)
and (Z-UNB) together, so (Z-UNB) alone is not the wall. HOLDS.

Step 1 verdict: the consumer HOLDS (1a-1g, 1i); the one-size clause 1h HOLDS AFTER
CORRECTION of the definition of $\Phi_4$.

## Step 2. The comparison lines, L39 and L41

2a. U(1), L39: "In compact U(1) the commutator is the identity almost surely, so $q_G=1$
even on a nonconstant gauge-invariant loop. The positive margin in (A) fails." For an
abelian group $[a,b]=1$, so $W_E=I$ and $q_G=1$ on every mean-zero vector, gauge-invariant
loops such as $\cos(\arg U_{\rm loop})$ included. Then $p(1-q_G)=0<\delta$. HOLDS. (The
failure is at the margin clause of (A), for every slab and every coupling.)

2b. Product, L39. Model: state space $X\times Y$, stationary law $\pi\otimes\pi'$, transfer
$T\otimes T'$, so the physical transition is $P_0\otimes P_0'$. An SU(2)-only kick is
$W_E\otimes I$ and fixes $1\otimes f$ for every $f\in L^2_0$ of the spectator, so its
mean-zero norm is $1$ and the margin fails. HOLDS. Redesigned versions: any consumer that
gives $\|(P_0\otimes P_0')^k\|_0\le1-\delta$ gives, on the vectors $1\otimes f$ (which are
mean-zero), $\|P_0'^k\|_{L^2_0(\pi')}\le1-\delta$, because
$(P_0\otimes P_0')^k(1\otimes f)=1\otimes P_0'^kf$. This restriction needs no coordinates
and no group structure on $Y$. If the spectator's lowest physical energy $m'(L)$ tends to
zero along the boxes, then $\|P_0'^k\|_0=e^{-ka\,m'}\ge e^{-t\,m'}\to1$ (since $ka\le t$),
which violates $1-\delta$ for large $L$; (A) demands the same $t,\delta$ at all $L$. HOLDS.

2c. Frozen, L41, the quotient characters.
- "On a finite group every one-dimensional character equals one on every commutator":
  $\chi(aba^{-1}b^{-1})=\chi(a)\chi(b)\chi(a)^{-1}\chi(b)^{-1}=1$. HOLDS.
- $Q_8/\{\pm1\}\simeq C_2^2$: $\{\pm1\}$ is the centre and the commutator subgroup, and the
  quotient of order 4 has all elements of order at most 2. HOLDS.
- $2T/Q_8\simeq C_3$: $Q_8$ is normal of index 3 in the group of order 24. The image of
  $2T$ in SO(3) is the rotation group of the tetrahedron, the image of $Q_8$ is the group
  of diagonal half-turns, and the lifts of the rotations by $2\pi/3$ about $(1,1,1)$, which
  permute the coordinate axes cyclically (for example $(1+i+j+k)/2$), give the two
  nontrivial cosets. HOLDS.
- "a nontrivial quotient character around a closed loop is gauge invariant, Haar-centred
  and fixed by every kick": a gauge map conjugates the holonomy and $\chi$ is a class
  function; for a simple loop of distinct links the holonomy is Haar-distributed on the
  finite group, so $\mathbb E\chi=0$; a kick $U_e\mapsto U_ec_e$ multiplies $\chi$ by
  $\chi(c_e)^{\pm1}=1$, since $\chi$ is a homomorphism (the order of factors does not
  matter for $\chi$). So the finite-group margin is $1-q_G=0$. HOLDS.

2d. Frozen, L41, the spin-two lines. Spin two is the space of harmonic quadratics on
$\mathbb R^3$ (dimension 5), acted on through SU(2) to SO(3).
- $Q_8$: $i,j,k$ act as the half-turns $\mathrm{diag}(1,-1,-1)$, $\mathrm{diag}(-1,1,-1)$,
  $\mathrm{diag}(-1,-1,1)$. Then $xy\mapsto-xy,\,-xy,\,+xy$: a nontrivial character of
  $C_2^2$. HOLDS.
- $2T$: $f=x^2+\omega y^2+\omega^2z^2$ has $\Delta f=2(1+\omega+\omega^2)=0$, so it is
  harmonic. Squares are fixed by the half-turns. Under the cyclic substitution
  $f(y,z,x)=\omega^2x^2+y^2+\omega z^2=\omega^2f(x,y,z)$: a nontrivial cube root. HOLDS.
- "Both lines are commutator-fixed after restriction": on each line the restricted
  representation is a one-dimensional character, so the matrix coefficient
  $g\mapsto\langle f,D_2(g)f\rangle/\|f\|^2$ restricted to the finite group is that
  character, fixed by the finite-group kicks. HOLDS.
- "On the full SU(2) spin-two space the multiplier is $1/25$": $(2\cdot2+1)^{-2}$. HOLDS.
- Remark (no verdict change): for $Q_8$ the same already happens in spin one ($x,y,z$
  carry the three nontrivial characters of $C_2^2$); for $2T$ spin two is the lowest spin
  with a one-dimensional constituent, since spin one restricts to the irreducible
  three-dimensional representation of the tetrahedral group. The note does not claim
  minimality, so nothing needs correcting.

Step 2 verdict: all lines of L39 and L41 HOLD.

## Step 3. Moser map (L27), the inverse $W=(1-\Delta)^{-1}$ (L49), the sign test (L51)

3a. Moser construction, L27.
- Metric and measure: the round metric of the unit $S^3=\mathrm{SU}(2)$ is bi-invariant,
  so the normalized Riemannian volume of the product is $H$. Divergence and Laplacian are
  taken for this volume.
- Poisson step: $\int(1-\rho)\,dH=1-\int\psi^2\,dU=0$. On the Peter-Weyl block with spins
  $(j_e)$ the Laplacian is $-\sum_e4j_e(j_e+1)$, which is at most $-3$ off the constants.
  Dividing rapidly decaying coefficients by it keeps rapid decay, so $u$ is smooth and is
  the unique zero-mean solution. HOLDS.
- Continuity equation: with $\rho_s=1-s+s\rho>0$ and $v_s=\nabla u/\rho_s$,
  $\partial_s\rho_s+\mathrm{div}(\rho_sv_s)=(\rho-1)+\Delta u=0$, and $\rho_0=1$. The field
  is smooth on $[0,1]\times X$ with $X$ compact, so the flow $\Phi_s$ exists, consists of
  diffeomorphisms, and $(\Phi_s)_\#H=\rho_sH$ (uniqueness for the continuity equation with
  a smooth field). So $S=\Phi_1$ has $S_\#H=\rho H=\pi$. HOLDS.
- Positivity and smoothness of $\psi$: $T$ has a smooth kernel that is strictly positive
  (the factors $e^{\beta\,\mathrm{tr}(\cdot)/2}$ are positive; gauge averaging keeps
  this), so $\psi=\lambda_0^{-1}T\psi$ is smooth and, being nonnegative and nonzero,
  strictly positive. HOLDS.
- Equivariance: vertex gauge maps are left and right translations on links, and centre
  flips multiply some links by $-1$; both are isometries of the bi-invariant product
  metric, hence preserve $H$. $T$ commutes with them (the class-function kernels and the
  Wilson weight are invariant; a flip changes the sign of two links in each plaquette that
  it meets), so the simple Perron vector $\psi$ and $\rho$ are invariant. For such an
  isometry $\gamma$, $u\circ\gamma$ solves the same zero-mean problem, so $u\circ\gamma=u$;
  then $d\gamma(\nabla u)=\nabla u\circ\gamma$, $v_s$ is $\gamma$-invariant, and by ODE
  uniqueness $\Phi_s\gamma=\gamma\Phi_s$. HOLDS.
- The caveat (no locality, no cutoff-uniform derivative bounds) is accurate.
Verdict L27: HOLDS.

3b. The inverse, L49.
- Row 778 (6), $\mathbb E\,D([a,b])=I/d^2$: average over $a$ of $D(a)XD(a)^{-1}$ is
  $(\mathrm{tr}X/d)I$; then $\mathbb E_b\,\chi(b)D(b^{-1})_{mn}=\sum_l\mathbb E\,D(b)_{ll}
  \overline{D(b)_{nm}}=\delta_{mn}/d$ by orthogonality. HOLDS.
- Laplace eigenvalue: the spin-$j$ entries are restrictions of harmonic polynomials of
  degree $2j$ on $\mathbb R^4$, so the eigenvalue on the unit $S^3$ is
  $-2j(2j+2)=-4j(j+1)=1-d^2$. The Casimir route agrees: the unit quaternion generators act
  as $2iJ_a$ in spin $j$, and $\sum_a(2iJ_a)^2=-4j(j+1)$. HOLDS.
- So $1-\Delta$ multiplies spin $j$ by $d^2$ and $W$ by $d^{-2}$: $W=(1-\Delta)^{-1}$ on
  $L^2$. With $D_E=\prod_e(1-\Delta_e)$, $D_EW_E=W_ED_E=I$ blockwise, on test functions,
  and on distributions by transposition (both are symmetric multipliers that keep
  polynomial growth of coefficients). HOLDS.
Verdict L49: HOLDS.

3c. The sign test, L51.
- (A) gives $g$: $(rW_E)(x,dy)$ has a density in $y$, since the commutator law has the
  Haar density $(\pi-\theta)/(2\sin\theta)$ (row 778 (7); its character series is
  $\sum_jd^{-1}\chi_j$). Put $g=p\,(rW_E)(x,y)$. Then $0\le g\le j_k$ a.e. by (A). The
  $x$-marginal is $p\,(rW_E1)=p$, the $y$-marginal is $p\,(HrW_E)=p$. For a test function
  $\phi$, $\langle(1\otimes D_E)g,\phi\rangle=\langle pH\otimes r,(1\otimes W_ED_E)\phi\rangle
  =\langle pH\otimes r,\phi\rangle$, so $D_{E,y}g=pH(dx)r(x,dy)\ge0$. HOLDS.
- Converse: let $\mu=(1\otimes D_E)g\ge0$. Pairing with $\phi\otimes1$ uses $D_E1=1$ and
  gives the $x$-marginal $pH$. Pairing with $1\otimes\phi$ gives $p\int D_E\phi\,dH
  =p\int\phi\,dH$, since every term of $D_E\phi-\phi$ contains a Laplacian and integrates
  to zero. A positive distribution is a positive measure; disintegrate
  $\mu=pH(dx)r(x,dy)$ with $r$ a probability kernel; the $y$-marginal gives $Hr=H$. Then
  $(1\otimes W_E)\mu=g\,H\otimes H\le j_k\,H\otimes H$, which is (A) for $H$-a.e. $x$.
  HOLDS.
- The two closing sentences of L51 are remarks. "A one-link marginal need not pass it" is
  supported by the disjoint-plaquette argument of L61-63 (Step 4). No verdict needed.
Verdict L51: HOLDS. The margin clause $p(1-q_G)\ge\delta$ is separate and is not part of
the equivalence; the text does not claim otherwise.

## Step 4. One-step obstruction (L53-59) and the disjoint-plaquette bound (L61-63)

4a. Radial Laplacian, L53. For a function of the angle $\theta$ to the identity on the
unit $S^3$, $\Delta f=\sin^{-2}\theta\,\partial_\theta(\sin^2\theta\,\partial_\theta f)=f''+2\cot\theta\,f'$.
With $x=\cos\theta$: $\partial_\theta=-\sin\theta\,\partial_x$,
$\partial_\theta^2=\sin^2\theta\,\partial_x^2-\cos\theta\,\partial_x$, so
$\Delta=(1-x^2)\partial_x^2-3x\partial_x$. HOLDS.

4b. The identity $(1-\Delta)h_\beta=h_\beta[1+3\beta x-\beta^2(1-x^2)]$: with $h=Ce^{\beta x}$,
$\Delta h=h[\beta^2(1-x^2)-3\beta x]$. HOLDS. The bracket at $x=-1$ is $1-3\beta$; its
derivative $3\beta+2\beta^2x\ge\beta(3-2\beta)>0$ on $[-1,1]$ for $0<\beta<3/2$, so for
$0<\beta\le1/3$ the minimum is $1-3\beta\ge0$. $\int(1-\Delta)h_\beta\,dg=1$. HOLDS.

4c. "the electric-link law is a convolution of a probability measure with the Haar
commutator law exactly when $0\le\beta\le1/3$". If $\beta\le1/3$, $\mu=(1-\Delta)h_\beta$
is a probability density and $h_\beta=W\mu$ by L49. If $h_\beta\,dg=\nu*\mu'$ for some
probability $\mu'$, then $\mu'=(1-\Delta)h_\beta$ as distributions (L49), so the
deconvolution is unique; for $\beta>1/3$ it is negative near $x=-1$, an open set around
$-I$. ($\beta=0$: $h_0=1$.) HOLDS. The scope sentence ("this particular factorization",
one link, no gauge projection) is accurate.

4d. L61, the set-up. Spatial weights off: $T=C_EP$, $T1=\lambda_01$, so $\psi=1$, $\rho=1$,
$u=0$ and $S$ is the identity. HOLDS. The multiplier: the account's (GL3) gives
$c_l=(2e^{-\beta}/\beta)I_{2l+1}(\beta)$ (outline line 2212), so the normalized multiplier
of dimension $d=2l+1$ is $a_d=I_d/I_1$. Equivalently $\int h_\beta D_{1/2}\,dg=a_2I$, from
$\int e^{\beta x}\chi_j\,dg=(2d/\beta)I_d(\beta)$ and $\int e^{\beta x}dg=(2/\beta)I_1(\beta)$.
HOLDS.

4e. $a_2=1/(4/\beta+I_3/I_2)>2/5$. The recurrence $I_1-I_3=(4/\beta)I_2$ gives the
formula. (GL4) (outline line 2238) gives $I_3/I_2\le\beta/6$; the series proves it term
by term. On $[23/10,13/5]$: $4/\beta\le40/23<2$ and $\beta/6\le13/30<1/2$, so
$a_2>1/(5/2)=2/5$. HOLDS. (GUIDE: $a_2=0.4793,\,0.5004,\,0.5203$ at
$\beta=2.3,\,2.45,\,2.6$.)

4f. Means and independence. Before the projection the output is $y_e=x_eg_e$ with $g_e$
i.i.d. of law $h_\beta$, which is central and inversion-symmetric, so
$\mathbb E\,D_{1/2}(g_e^{\pm1})=a_2I$. A plaquette holonomy is a product of four factors
$x_eg_e$ or their inverses, so its mean matrix is $a_2^4x_p$ and the mean trace is
$a_2^4w(x_p)$. Edge-disjoint plaquettes use disjoint sets of $g_e$, so their traces are
independent. Plaquette traces are gauge invariant, so the projection $P$ does not change
their joint law. The set $\{w(x_{p_i})>\eta,\ i\le N\}$ is open and contains the identity
configuration, so it has positive Haar measure. Edge-disjoint families of size $N$ exist
in large tori (for instance the $(1,2)$-plaquettes based at points with both first
coordinates even). HOLDS.

4g. The Chebyshev bound, L63. $a_2^4>(2/5)^4=0.0256>4^{-4}$, so $\eta<1$ with
$b=\eta a_2^4-4^{-4}>0$ exists. On the commutator branch the output is $y=zc$ with $c$
independent of $z$ and $\mathbb E\,D_{1/2}(c)=I/4$; given $z$ the $N$ traces are
independent, in $[-1,1]$, with means $4^{-4}w(z_i)\le4^{-4}$. Each variance is at most 1,
so the empirical mean has variance at most $1/N$.
- Wilson step, on the input set: the mean of the empirical mean exceeds $4^{-4}+b$, so
  $A$ needs a downward deviation larger than $b/2$; Chebyshev gives
  $\Pr(A)\le(1/N)/(b/2)^2=4/(Nb^2)=e_N$. HOLDS.
- Commutator branch: $A^c$ needs an upward deviation larger than $b/2$ given $z$, so
  $\Pr(A^c\mid z)\le e_N$ for every $z$, and averaging over any law of $z$ keeps it. HOLDS.
- Domination: (A) at one input $x$ of the positive-measure set (it holds for $H$-a.e. $x$)
  gives $e_N\ge\Pr_{\rm Wilson}(A)\ge p\Pr_{\rm branch}(A)\ge p(1-e_N)$, so
  $p\le e_N/(1-e_N)$. No property of $r$ is used. HOLDS.
- Growing tori allow $N\to\infty$, so $e_N\to0$ and no box-independent $p>0$ exists for
  $k=1$ in this model on the window. HOLDS. (GUIDE at $\beta=2.3$, $\eta=0.99$:
  $b=0.0483$, $N=10^6$ gives $p\le1.7\times10^{-3}$.)

Step 4 verdict: L53-59 HOLDS; L61-63 HOLDS.

## Step 5. Twelve steps (L65-72), the fixed-box bound (L74-80), the $(1-6\beta)$ example (L82-88)

5a. "$a_d\le(13/20)^{d-1}$ for $d\ge2$, $0\le\beta\le13/5$." $a_d=\prod_{n=1}^{d-1}I_{n+1}/I_n$
and (GL4) gives $I_{n+1}/I_n\le\beta/(2n+2)\le\beta/4\le13/20$. At $\beta=0$, $a_d=0$ for
$d\ge2$ (Haar). HOLDS. (GUIDE: on a grid of $\beta\in(0,2.6]$, $d\le40$, the largest
value of $a_d/(13/20)^{d-1}$ is $0.80$.)

5b. The expansion. The multiplier of $h_\beta^{*12}$ on spin $j$ is $a_d^{12}$, so its
density is $\sum_jd\,a_d^{12}\chi_j$ and $(1-\Delta)h_\beta^{*12}=\sum_jd^3a_d^{12}\chi_j$,
constant term $1$. The nonconstant part is at most $\sum_{d\ge2}d^4a_d^{12}$ by
$|\chi_j|\le d$. HOLDS.

5c. The sum. $d\le2^{d-1}$ gives $d^4\le16^{d-1}$. $(13/20)^{12}<(2/3)^{12}=((2/3)^3)^4<(1/3)^4
=1/81$. So $d^4a_d^{12}<(16/81)^{d-1}$ and $\sum_{d\ge2}(16/81)^{d-1}=(16/81)/(65/81)=16/65$.
HOLDS. So $(1-\Delta)h_\beta^{*12}\ge49/65>0$ and it integrates to one. HOLDS. (GUIDE: the
actual sum is $2.4\times10^{-3}$ at $\beta=2.3$ and $6.3\times10^{-3}$ at $\beta=2.6$.)

5d. Assembly. With spatial weights off, $J_1=C_EP$ (normalized), $P$ commutes with the
central link convolutions and $P^2=P$, so $J_{12}=C_E^{12}P$. Each link factor is
$h_\beta^{*12}=\nu*\mu$ with $\mu=(1-\Delta)h_\beta^{*12}\ge0$, so
$C_E^{12}=R_\mu W_E$ (all central link convolutions commute). Hence
$J_{12}=(PR_\mu)W_E$ with $r=PR_\mu$ a probability kernel and $Hr=H$: (A) holds with
equality and $p=1$, margin $3/4$, on every finite torus. HOLDS. The scope sentences (bare
temporal weight; the stopped effective action needs its own estimate) are accurate.
(GUIDE, not claimed in the note: the single-link deconvolution of $h_\beta^{*k}$ is
already positive from $k=4$ at $\beta=2.3$ and from $k=5$ at $\beta=2.6$, so "twelve is
a sufficient hand bound" is consistent.)

5e. The fixed-box bound, L74-80.
- $j_1$ is smooth, symmetric and strictly positive: $S$ is a diffeomorphism, $T$ has a
  smooth, symmetric, strictly positive kernel, $\psi$ is smooth and positive. On the
  compact product $h=\min j_1>0$, and $h\le1$ because $\int j_1(x,y)\,dy=1$. HOLDS.
- $j_1=h+(1-h)q$ with $q\ge0$ bistochastic; for $f\perp1$, $J_1f=(1-h)Qf$, so
  $\|J_1\|_0\le1-h$. HOLDS.
- $A_1,B_1<\infty$ by smoothness on the compact product ($D_E$ is a differential operator
  of finite order). HOLDS.
- The identity: with $\Pi$ the constant projection, $J_1\Pi=\Pi J_1=\Pi$ (both marginals
  one), so $(J_1-\Pi)^k=J_k-\Pi$ and $j_k(x,y)-1=\langle j_1(x,\cdot)-1,\,
  (J_1-\Pi)^{k-2}(j_1(\cdot,y)-1)\rangle$ (for $k=2$ the middle factor is $I$). Applying
  $D_{E,y}$ under the integral acts on the last factor only, and $D_E1=1$ gives
  $D_{E,y}j_k-1$ on the left. $\|(J_1-\Pi)^{k-2}\|\le(1-h)^{k-2}$ on all of $L^2$ (zero on
  constants, $J_1$ on $L^2_0$). Cauchy-Schwarz gives
  $|D_{E,y}j_k(x,y)-1|\le A_1B_1(1-h)^{k-2}$. HOLDS.
- For $h<1$ and $k$ with $A_1B_1(1-h)^{k-2}<1$, $D_{E,y}j_k>0$, so $g=j_k$ passes the
  sign test with $p=1$; $h=1$ is $j_1\equiv1$. HOLDS. The closing scope sentences (no
  spectral input; dependence on box and cutoff) are accurate.
Verdict L74-80: HOLDS.

5f. The $(1-6\beta)$ example, L82-88. In a three-dimensional periodic cube each link lies
in $2(3-1)=4$ spatial plaquettes. With all links $I$ except $U_e=-I$, each incident
plaquette has holonomy $-I$ (either orientation), so $w=-1$. As a function of $U_e$ alone,
$w_p=\tfrac12\mathrm{tr}(U_eX_p)$ with $X_p=I$; it is a spin-$\tfrac12$ function, so
$\Delta_ew_p=-3w_p$, and its gradient vanishes at $U_eX_p=-I$, the minimum of $x$. With
$M\propto e^F$, $F=(\beta/2)\sum_pw_p$:
$\Delta_eM=M(\Delta_eF+|\nabla_eF|^2)=M\cdot(\beta/2)\cdot4\cdot3=6\beta M$. So
$(1-\Delta_e)M=(1-6\beta)M$ there, negative for $\beta>1/6$ and, by continuity, on a
neighbourhood. HOLDS. Cross-check: here $M\propto e^{2\beta x}$ in $x=\tfrac12\mathrm{tr}U_e$,
and 4b with $\beta\to2\beta$ gives $1-3(2\beta)$ at $x=-1$. (GUIDE: a finite-difference
radial Laplacian matches the formula to $10^{-6}$.)
- The product rule term $-2\nabla_eM\cdot\nabla_ef$ is correct:
  $(1-\Delta)(Mf)=f(1-\Delta)M-M\Delta f-2\nabla M\cdot\nabla f$. HOLDS.
- What the example refutes: with $f=1=W1$, the product $M\cdot(W\text{ of a positive
  measure})$ need not be $W$ of a positive measure. That is the stated claim ("passing the
  sign through one multiplier"), in the physical coordinates where the electric step is a
  convolution. HOLDS. "Neither positivity of the transfer nor its Haar commutator
  multipliers bounds that signed term" is a remark, not a proved statement; it is not used.

Step 5 verdict: L65-72 HOLDS; L74-80 HOLDS; L82-88 HOLDS.

## Step 6. The other lines of Sections 2-3, guide runs, verdicts

6a. L25 (GUIDE, rank 1). The description matches (A) and the consumer: on the branch the
kicks multiply every nontrivial representation by at most $1/4$. The label "K-one" is a
classification, not a claim to check. Note that (A) asks for one physical thickness $t$ but
for every size $2^hL_0$ and every cutoff, so it is a uniform statement, not a number at a
single box. No verdict needed.

6b. L29-35 (OPEN, the statement (A)). The definitions are consistent: $j_k$ is the joint
density of the stationary pair in the coordinates $S^{-1}$ (Step 1), both marginals are
one, $q_G$ is the mean-zero norm of $W_E$ on the full product. "Multiplying separate
linkwise acceptance probabilities does not furnish the joint weight" is borne out by Step
4g. No verdict needed (OPEN).

6c. L43 (ARGUED). The identity: for $f=1_B-\pi(B)$ and a stationary pair $(X,Y)$,
$\mathbb E(f(X)-f(Y))^2=2\mathrm{Var}f-2\mathbb E f(X)f(Y)$ and $(f(X)-f(Y))^2
=1[1_B(X)\ne1_B(Y)]$, so the loss of the normalized autocorrelation is
$\Pr[1_B(X)\ne1_B(Y)]/[2\pi(B)(1-\pi(B))]$. HOLDS. The consequence (weights bounded away
from 0 and 1 and vanishing crossing probability force the norm to 1, against $1-3p/4$)
HOLDS. Locator slip: the pinned-cell step (L3) is in Section 6 of the brief, not Section
5 (checked in both versions of the brief); RC is in Section 5. No mathematical effect.

6d. L45 (GUIDE, the cheapest test). For a simple loop of $b$ distinct links,
$\mathbb E\chi_j(\prod_i U_ic_i^{\pm1})=\mathrm{tr}\prod_i(D(U_i)\,d^{-2})=d^{-2b}\chi_j$;
kicks off the loop do not enter. $1\pm\chi_j/d\ge0$. Integrating (A) against them gives
$1\pm m(x)\ge p(1\pm d^{-2b}(r\chi_j/d)(x))\ge p(1-d^{-2b})$, so
$|m(x)|\le1-p[1-(2j+1)^{-2b}]$ for a.e. $x$. HOLDS. The refutation logic (positive
measure of violations at one box; a cofinal sequence along the cutoff) HOLDS.

6e. L90 (OPEN, where the attempt stops). An accurate statement of what Steps 4-5 leave
open: no control of $h,A_1,B_1$ along the trajectory, the wrong one-step sign in the
window, no magnetic plaquettes in the twelve-step pass, and the free-energy side. No
verdict needed.

6f. Scope remark on L41 (no verdict change). The margin argument works for Q_8 and 2T
because they have nontrivial one-dimensional characters. It gives nothing for a perfect
finite subgroup: for the binary icosahedral group every nontrivial irreducible
representation has dimension at least 2, so $q_G=1/4$ exactly as for SU(2), and any
separation would have to come from the domination inequality itself. Row 838 records
(GUIDE) that this group freezes near $\beta\approx5.7$ and does not bind at order one, and
the brief's list is Z_2, Q_8, 2T; so nothing in Sections 2-3 needs correcting. The point
matters only if the comparison list is widened.

6g. Guide runs (stdlib Python, run with `-I`; scratch only, not in the repo; a guide, not
a proof). Every hand bound above was consistent with the runs: $a_2\in[0.479,0.521]$ on
the window; $I_3/I_2\le\beta/6$; $\max a_d/(13/20)^{d-1}=0.80$ on a grid; the twelve-step
sum $\le6.3\times10^{-3}<16/65$; the one-step bracket minimum is $1-3\beta$ for
$\beta\le1/3$ and negative at $\beta=0.34$; quadrature of the commutator density
$(\pi-\theta)/(2\sin\theta)$ gives total mass $1$ and $\mathbb E\chi_d=1/d$ for $d=2..6$
to six digits (a Monte Carlo run with $2\times10^5$ samples agreed within its noise,
about 1-2 standard errors low); the $(1-6\beta)$ value and the radial Laplacian formula
matched a finite difference to $10^{-6}$. Peak memory was far below 2 GB.

## Verdict table

| # | Statement (file under check) | Line | Verdict |
|---|---|---|---|
| 1 | Set-up: $j_k$ formula, marginals one, $\|J_k\|_0=\|P_0^k\|_0$ | L19, L29 | HOLDS |
| 2 | Residual$/(1-p)$ is a Haar-stationary Markov kernel; Jensen | L37 | HOLDS |
| 3 | Multiplier $(2j+1)^{-2}$; $\|W_E\|_{L^2_0(H)}=1/4$ | L37 | HOLDS |
| 4 | $\|P_0^k\|_0\le1-3p/4$ on the physical subspace | L37 | HOLDS |
| 5 | Lower cutoff limit $\ge(L/t)[-\log(1-3p/4)]$; passage to (Z-UNB) | L37 | HOLDS |
| 6 | One-size clause against $2\limsup\Phi_{4,j}(n/4)+30$ | L37 (with L21) | HOLDS AFTER CORRECTION: $\Phi_4(m)=256F(m^4)-F((4m)^4)$ (row 720), not L21's one-doubling defect |
| 7 | BDD-Delta still needed for the wall | L37 | HOLDS |
| 8 | U(1): $q_G=1$, margin fails | L39 | HOLDS |
| 9 | Product: SU(2)-only kick fixes $1\otimes f$; redesigned consumers fail on a massless spectator | L39 | HOLDS |
| 10 | Frozen: commutators kill 1-d characters; $Q_8/\{\pm1\}\simeq C_2^2$, $2T/Q_8\simeq C_3$; loop characters invariant, centred, kick-fixed | L41 | HOLDS |
| 11 | Spin-two lines $xy$ ($Q_8$), $x^2+\omega y^2+\omega^2z^2$ ($2T$); SU(2) multiplier $1/25$ | L41 | HOLDS |
| 12 | Moser map $S$ with $S_\#H=\pi$ | L27 | HOLDS |
| 13 | Equivariance of $S$ under vertex gauges and centre flips | L27 | HOLDS |
| 14 | $W=(1-\Delta)^{-1}$; $D_EW_E=I$ on distributions | L49 | HOLDS |
| 15 | (A) is equivalent to the sign test on $g$ | L51 | HOLDS |
| 16 | One-step obstruction: positive deconvolution exactly for $\beta\le1/3$ | L53-59 | HOLDS |
| 17 | $a_2>2/5$ on $[23/10,13/5]$; means $a_2^4w$; conditional independence | L61 | HOLDS |
| 18 | Chebyshev: $p\le e_N/(1-e_N)$, $e_N=4/(Nb^2)$ | L63 | HOLDS |
| 19 | $a_d\le(13/20)^{d-1}$; nonconstant part $<16/65$; (A) with $p=1$ at twelve electric steps | L65-72 | HOLDS |
| 20 | Fixed box: $\|J_1\|_0\le1-h$; $\lvert D_{E,y}j_k-1\rvert\le A_1B_1(1-h)^{k-2}$; $p=1$ at large $k$ | L74-80 | HOLDS |
| 21 | $(1-\Delta_e)M=(1-6\beta)M$ at the one-flipped-link configuration | L82-88 | HOLDS |
| 22 | Phase-event autocorrelation identity (ARGUED) | L43 | HOLDS (locator slip: (L3) is in brief Section 6) |
| 23 | Cheapest test: $\lvert m\rvert\le1-p[1-(2j+1)^{-2b}]$ (GUIDE) | L45 | HOLDS |

No statement FAILS. Statement (A) itself stays OPEN, as the note says (L29, L90).

RESULT: row 1132 (`library/gap-council-op-astra.md`, gpt-6.2-astra) Sections 2-3 checked line by line by hand by Claude Opus 5.5 at max effort (cross-provider): 22 of 23 checked statements HOLD and none FAILS, namely the consumer of (A) (Jensen on the residual, multiplier $(2j+1)^{-2}$, norm $1/4$, bound $1-3p/4$, passage to (Z-UNB)), the U(1), product and frozen $Q_8$/$2T$ lines, the Moser map and its equivariance, the equivalence of (A) with the sign test on $g$, the one-step obstruction above $\beta=1/3$ and the disjoint-plaquette Chebyshev bound, the twelve-step pass with $a_d\le(13/20)^{d-1}$, the fixed-box bound with $A_1,B_1$, and the $(1-6\beta)$ example; one HOLDS AFTER CORRECTION: the one-size clause of L37 must use row 720's quadrupling defect $\Phi_4(m)=256F(m^4)-F((4m)^4)$, not the one-doubling defect written in L21 (inherited from the first brief); scope remark: the frozen margin argument does not reach perfect finite subgroups (binary icosahedral, $q_G=1/4$), which row 838 records as non-binding at order one; (A) and the free-energy side stay OPEN; no mass gap is claimed.
