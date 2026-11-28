## Repo search

**GUIDE.** FINISH row 1204, research text at `129499820`. The 8 November lead search covered main and PRs 10114, 10133, 10134 and 10141. Its §11 points to the one-step plaquette witness. I checked PR 10114, `MASS_GAP_LOCAL_BLOCK_ASTRA.md`, lines 4–14 and 106–149. The witness gives a lower bound on a one-step correlation. The contraction there assumes bare coupling at most $1/32$ at fixed lattice spacing. Grok’s PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md`, lines 1–8 and 77–86, still requires crossover clustering and source transport. PR 10134, `mass-gap-interface.md`, I1–I5, separates a nonempty excited sector from a positive lower spectral edge. PR 10141, `research/ym4d/library/fp1.md`, lines 299–314, controls a constrained ultraviolet fluctuation. Main’s `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c, gives a conditional finite-size criterion. These are different estimates. [Lead search](prior/repo-search-2026-11-08.md)

**GUIDE.** No task-specific prior file is present. In the pinned branch, row 1161 proposes a sufficient neutral-sector trace bound on one periodic spatial cube at a fixed physical side. Row 1192 ends with a probability ratio for two time periods and leaves that bound open. The brief records row 1192 as unchecked. The registry lists no entry under “mass gap”, “neutral trace”, or “N-phys”. [Cube criterion](gap-solve9-astra62.md) · [Row 1192](gap-solve20-astra62.md) · [Ownership registry](open-registry.md)

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, distinguish decay of a scalar correlation from exclusion of an energy interval in their outline, lines 581–599. Their complete account I, lines 2704–2712 and 3213–3222, explicitly leaves a mass gap outside the assertion. Both sources here are at `31a47c543775`. [Outline index](sa-index/README.md) · [Indexed obligations](sa-index/obligations.md)

**OPEN.** Construct a nontrivial four-dimensional continuum $SU(2)$ Yang–Mills theory on the intended local observable algebra, and prove that its Hamiltonian has no spectrum in some interval $(0,m)$, with $m>0$. The question below is whether a local Wilson correlation can isolate all possible positive energies arbitrarily close to the vacuum while discarding irrelevant finite-volume states.

## A local spatial difference at one physical separation

**GUIDE.** There is a way to avoid counting every state of the spatial cube. Use the difference of a local source and its spatial translate as the insertion. The earlier sheared-torus identities in row 962, §7.4, take a trace with a translation. Row 963, §3, explains the loss in projecting that trace onto zero momentum. Here the quantities are vacuum matrix elements, and the Lorentz action on the *continuum* energy-momentum spectrum is essential. The relation between a rest-energy gap and a gap in invariant mass is already in A0 of the lane. [Sheared tori](gap-constraints-max.md) · [Spatial sectors](gap-rotgeom-opus.md) · [A0](gap-wall-assumptions-opus.md)

**PROVED (an exact norm, given a relativistic vacuum representation).** Let the strongly continuous translations have joint generators $(H,\mathbf P)$ and spectrum in the closed forward cone. Assume unitary covariance under the proper orthochronous Lorentz group. Write $\Sigma$ for the closed support of the joint spectral measure. Suppose $\Sigma\setminus\{0\}$ is nonempty, and put
\[
 M=\inf_{(E,\mathbf p)\in\Sigma\setminus\{0\}}\sqrt{E^2-|\mathbf p|^2}.
\]
For $h>0$ define the bounded positive operator
\[
 B_h=\tfrac14(1-e^{ihP_1})^* e^{-hH}(1-e^{ihP_1}).
\]
Then
\[
 \boxed{\ \|B_h\|=Q(hM),\qquad
 Q(y)=\max_{0\le x\le\pi}e^{-\sqrt{x^2+y^2}}\sin^2(x/2).\ }       \tag{1}
\]
No discrete mass shell, isolated eigenvalue or particle state is assumed.

**PROVED.** The multiplier of $B_h$ is $b(E,\mathbf p)=e^{-hE}\sin^2(hp_1/2)$. Its norm is the supremum of this continuous nonnegative function on $\Sigma$. Indeed every open neighborhood of a support point has nonzero spectral projection, and the spectral integral gives the converse inequality. Unitary covariance sends each such projection to that of the transformed neighborhood, so $\Sigma$ contains the entire Lorentz orbit of each of its points. On an orbit of mass $\mu>0$, for each $x\ge0$ the momentum $(x/h,0,0)$ occurs with energy $\sqrt{\mu^2+(x/h)^2}$. This follows by boosting the rest vector along axis 1. On the nonzero null orbit the same holds for $x>0$, by rotation and a boost rescaling a null vector. At fixed $|hp_1|$, transverse momentum can only decrease $b$. Folding $|hp_1|$ to the element of $[0,\pi]$ with the same cosine preserves the sine squared and can only lower the energy in this maximization. Thus the supremum along an orbit is $Q(h\mu)$. The origin contributes zero. Uniform continuity on compact $x,y$ rectangles makes $Q$ continuous. It is decreasing, so a sequence of orbits with masses tending to $M$ gives (1).

**PROVED (sharp threshold).** At zero mass, differentiating $\log(e^{-x}\sin^2(x/2))$ on $(0,\pi)$ gives $\cot(x/2)-1$. The unique maximum is at $x=\pi/2$, hence
\[
 q_0=Q(0)=\tfrac12 e^{-\pi/2}.
\]
For $y>0$ every positive value of the multiplier is strictly smaller than its value at $y=0$ at the same $x$. The maximum is attained and is positive, so $Q(y)<q_0$. Consequently $\|B_h\|<q_0$ for even one $h>0$ is equivalent to $M>0$. More quantitatively, $\|B_h\|\le q_0e^{-\delta}$ with $\delta>0$ implies
\[
                  M\ \ge\ h^{-1}\sqrt{\pi\delta+\delta^2}.             \tag{2}
\]
Evaluate (1) at $x=\pi/2$ and take logarithms. A positive $M$ bounds every nonzero energy below by $M$, and boosts of the timelike spectral points to rest give the converse edge. The zero four-momentum space is annihilated by $B_h$ irrespective of its multiplicity. The uniqueness of the vacuum and nontriviality are separate premises for the Jaffe–Witten conclusion.

**OPEN.** For the Wilson fields the new target is a strict deficit below $q_0$ in (1), on the collection of **matched local** states. Bounding the transfer on each finite spatial torus separately need not bound this quantity by a common strict constant. The following steps address what a Wilson estimate of the required kind would actually measure.

## What diagonal reflection positivity already gives in Wilson theory

**GUIDE.** Use an infinite-lattice, translation-invariant Wilson state obtained from periodic cubes at fixed bare parameters, with coordinate and diagonal reflection positivity. Use the link reversal and closed-half conventions of the outline. Sussman and Alpoge's PL4–PL7, lines 3260–3427, give the following joint spectral bound. PH1 already ports its polynomial-measure proof. Finite tori periodically repeated as configurations are outside the stated domain of that argument (outline 3195–3215). [PH1, Lemma 2](ph1.md) · [Indexed source passages](sa-index/chunk-03.md)

**PROVED (from PL5).** Let $T$ be forward translation by one time step on the reflection Hilbert space and $U$ translation by one spatial step along axis 1. Write $T=e^{-E}$, allowing $E=\infty$, and $U=e^{i\eta}$ with $-\pi<\eta\le\pi$. PL5 gives
\[
 E\ge g(|\eta|),\qquad g(t)=2\operatorname{arsinh}(\sin(t/2)),\quad 0\le t\le\pi .
\]
For the lattice version $B^{(k)}=(1-U^k)^*T^k(1-U^k)/4$, $k\ge1$, it follows that
\[
 0\le B^{(k)}\le b_k I,\qquad
 b_k=\max_{0\le x\le\pi}\sin^2(x/2)\exp[-k g(x/k)].                 \tag{3}
\]
Indeed, fold $k|\eta|$ to $x=\arccos(\cos(k\eta))$. Then $x\le k|\eta|$, $g$ is increasing, and $\sin^2(k\eta/2)=\sin^2(x/2)$. The kernel of $T$ contributes zero. Analytic expansion at zero gives $g(t)=t-t^3/12+O(t^5)$, with a uniform remainder for $t\in[0,\pi/k]$ as $k\to\infty$. The maximizers converge to $x_0=\pi/2$ by uniform convergence and its strict isolated maximum. There the logarithmic derivative is $\cot(x/2)-g'(x/k)$, and the derivative of $\cot(x/2)$ at $x_0$ is $-1$. The critical point equation therefore gives $x=x_0+O(k^{-2})$ for any maximizer. Taylor expansion of the logarithm at $x_0$ yields
\[
                    b_k=q_0\exp\{\pi^3/(96k^2)+O(k^{-4})\}.           \tag{4}
\]
In particular the non-strict continuum threshold is already a cutoff-uniform limiting upper bound for these Wilson matrix elements, before constructing relativistic limit fields.

**PROVED (location of a possible failure of strictness).** For a unit reflection vector $v$, let $\mu_v$ be its joint spectral probability and $x=k|\eta|$ *without* folding. There are numerical constants $C,K$ such that for $k\ge K$, $\langle v,B^{(k)}v\rangle\ge q_0(1-d)$, $d\ge0$, implies
\[
\begin{split}
 &\mu_v\{x>\pi\}
 +\int_{x\le\pi}\min\!\left(1,(x-x_0)^2+k[E-g(|\eta|)]\right)\,d\mu_v\\
 &\hspace{46mm}\le C(d+k^{-2}).                                      \tag{5}
\end{split}
\]
To prove it, the log of $e^{-x}\sin^2(x/2)$ has second derivative $-\tfrac12\csc^2(x/2)\le-1/2$. Its maximum and zero first derivative at $x_0$ give an upper bound $\log q_0-(x-x_0)^2/4$. Use the expansion of $g$ on $x\le\pi$ and subtract $k(E-g)$ in the exponent. On $x>\pi$ use $kE\ge k g(\pi/k)\to\pi$ and $e^{-\pi}<q_0$. These two bounds give (5) upon integration, since $1-e^{-z}\ge (1-e^{-1})\min(1,z)$ for $z\ge0$. The same bound holds at $E=\infty$ by continuity of the multiplier. Thus improving (3) at physical scale $h=\lim ka$ requires an estimate near $|p_1|=\pi/(2h)$ and the bottom of the dispersion allowed by the diagonal mirrors. Large energy, low spatial frequency and the other periods of the sine each already lose a fixed fraction outside any fixed neighborhood of that maximum.

## A strict Wilson bound for sources with controlled transverse reflection norm

**PROVED (two perpendicular reflections).** Work in the preceding Wilson state. Write $\theta_0$ for time reflection, $\theta_1$ for reflection at $x_1=0$, and $\tau_w$ for spatial translation by $w$ lattice steps along axis 1. Translate a bounded positive-time source $F$ so that its support has $0\le x_1\le D$. Set $\Phi=[F]_0$, assume $\|\Phi\|>0$, and define
\[
 L_F=\theta_1\tau_{-D}\theta_0F,\qquad
 R(F)=\frac{\|[L_F]_1\|\,\|[F]_1\|}{\|\Phi\|^2}.
\]
Both functions in the numerator belong to the positive half-space for $\theta_1$. If $S$ is one normal step in that reflection space, $S$ is a positive contraction. PL4 in the two directions gives, for $w\ge D$,
\[
 \langle\Phi,U^w\Phi\rangle_0
  =\nu(\overline{\theta_0F}\,\tau_wF)
  =\langle[L_F]_1,S^{w-D}[F]_1\rangle_1 .
\]
The second equality translates both insertions by $-D$ before reflecting. In particular for integers $w_0\ge D$, $m\ge0$ and $k\ge1$,
\[
 \left|\left\langle\Phi,U^{w_0}
        \left(\frac{1-U^{2k}}2\right)^m\Phi\right\rangle_0\right|
 \le 2^{-m} R(F)\,\|\Phi\|^2.                                        \tag{6}
\]
Expand the polynomial. In the transverse picture it becomes $S^{w_0-D}(1-S^{2k})^m/2^m$, whose norm is at most $2^{-m}$. This uses neither parity of $F$ nor a product measure on the slice.

**PROVED (a quantitative deficit).** There are numerical $c>0$ and $K$ such that for $k\ge K$,
\[
 1-\frac{\langle\Phi,B^{(k)}\Phi\rangle}{b_k\|\Phi\|^2}+k^{-2}
 \ \ge\ \frac{c}{[1+D/k+\log(2+R(F))]^2}.                           \tag{7}
\]
Normalize $\Phi$ and denote the left side by $\gamma$. One has $b_k\ge q_0$ because $g(t)\le t$. Thus (5) applies with $d\le\gamma$ by taking $d=(1-\langle B^{(k)}\rangle/q_0)_+$. On $x\le\pi$, $|x-x_0|\le\pi/2$, so (5) gives $\int_{x\le\pi}|x-x_0|^2\,d\mu\le C\gamma$ and $\mu(x>\pi)\le C\gamma$. Take $w_0=4k\lceil D/(4k)\rceil$. At $k\eta=\pm x_0$, both $e^{iw_0\eta}$ and $(1-e^{2ik\eta})/2$ are one. On $x\le\pi$ their respective distances from one are at most $(w_0/k)|x-x_0|$ and $|x-x_0|$. For $|z|\le1$, $|z^m-1|\le m|z-1|$. Cauchy–Schwarz and the bound two on the other part of the spectrum show that the normalized left matrix element in (6), before taking its absolute value, is within $C(1+w_0/k+m)\sqrt\gamma$ of one. Here one may assume $\gamma\le1$, the other case being immediate. Take $m=\lceil\log_2(2+2R(F))\rceil$. The upper bound in (6) is at most $1/2$, so $C(1+w_0/k+m)\sqrt\gamma\ge1/2$. This proves (7).

**PROVED (all same-time Wilson sources in a spatial strip).** If $F$ reads only spatial bonds in the time-zero slice, then $\|\Phi\|^2=\nu(|F|^2)$. Each transverse reflection norm is at most the $L^2(\nu)$ norm by Cauchy–Schwarz and reflection invariance. Hence $R(F)\le1$. For every fixed finite $A$, all such sources with $D\le Ak$, including arbitrary gauge-invariant functions with arbitrarily many transverse bonds, obey
\[
 \limsup_{k\to\infty}\ \sup_{F,\nu}
 \frac{\langle[F]_0,B^{(k)}[F]_0\rangle}{\|[F]_0\|^2}
 \le q_0\bigl(1-c'/(1+A)^2\bigr),                                    \tag{8}
\]
with a numerical $c'>0$. The supremum here ranges over the stated class and the infinite-lattice states with the mirror properties. It includes varying bare couplings. The same argument applies to sources in positive-time boxes with uniformly bounded $D/k$ and $R(F)$. For fixed $D/k$, any source approaching $q_0$ with $\gamma\downarrow0$ must pay $R(F)\ge\exp(c''/\sqrt\gamma)$ eventually, with a decrease of $c''$ if needed.

**GUIDE.** The ratio in (8) uses three one-sample reflected expectations and a supremum over sources. It grants a uniform deficit on an infinite-dimensional source class. Passing to a full continuum Hilbert space needs control of the normalized states that this class can approximate. Rows 845/852, 895/896 and 1118–1122 distinguish such suprema from averages and from couplings of two replicas. Here (6) uses a single Wilson state throughout. [Lane source and quantifier rules](../parts/gap.md)

## Testing the extension with the original Wilson action

**PROVED (loss of states in a time slice).** At any fixed spacing and finite $\beta$, functions of the spatial links in a fixed finite-width strip form a proper subspace of the full time-zero $L^2$ space, also after restricting to gauge invariants. Choose a spatial plaquette outside the strip, pick one edge $e$, and set $W_p=\tfrac12\operatorname{Tr}(U_p)$. Conditional on every other link, $W_p$ is a unit linear functional on the unit quaternion $U_e$ and its law has the six-staple Haar tilt $e^{H\cdot U_e}$, $|H|\le6\beta$. The one-link variance bound (8) of row 1173 gives $\operatorname{Var}(W_p\mid\hbox{other links})\ge c(1+\beta)^{-2}$. The all-but-one-link information contains the strip, so conditional variance in the strip leaves at least this mean-square error. The residual after subtracting the strip conditional mean is orthogonal to all its functions and has this positive squared norm. Gauge averaging gives an invariant version of the conditional mean, since the sigma field of strip links is preserved. This fixed-cutoff witness makes no claim about the physical energy of the residual. [Wilson one-link bound](gap-solve15-astra62.md)

**PROVED (unbounded reflection-norm ratio already for linear plaquette sources).** The following obstruction uses only fundamental spatial plaquette traces, all on the transverse mirror $x_1=0$. In lattice units take a $23$-plaquette $p$ in the time-zero slice, and $p_\ell=p+3\ell e_2$ for $0\le\ell\le m$. Write $U_2$ for one tangential translation on the time reflection space, and set
\[
 G_m=2^{-m}\sum_{\ell=0}^m(-1)^\ell {m\choose\ell} W_{p_\ell},
 \qquad F_{b,m}=\tau_{b e_0}G_m,\qquad b,m\ge1 .
\]
The joint conditional distribution of one selected edge per plaquette, given the remaining spacetime links, is a product of the six-staple laws because no action face contains two selected edges. Applying the cited variance bound and using $\sum_\ell 2^{-m}{m\choose\ell}=1$ gives
\[
 \nu(|F_{b,m}|^2)\ge
  c(1+\beta)^{-2}\sum_\ell 4^{-m}{m\choose\ell}^2
  \ge \frac{c}{(1+\beta)^2(m+1)} .                                    \tag{9}
\]
All spatial bonds read by $F_{b,m}$ or $\theta_0F_{b,m}$ lie in the spatial mirror. Thus at $D=0$ the numerator defining $R(F_{b,m})$ is precisely the left side of (9).

**PROVED.** The time norm is bounded in the other direction. The time-zero vector of $W_p$ has norm at most one. Its multiplier for $F_{b,m}$ has modulus $e^{-bE}|\sin(3\eta_2/2)|^m$. PL5 in direction 2 gives $E\ge\kappa|\eta_2|$ with $\kappa=2\operatorname{arsinh}(1)/\pi>0$. Maximizing $e^{-bE}E^m$ for $E\ge0$ yields
\[
 \|[F_{b,m}]_0\|^2
 \le \left(\frac{3m}{2e\kappa b}\right)^{2m}.                         \tag{10}
\]
Take $m=\lfloor \kappa b/6\rfloor$ for large $b$ and set $\epsilon_b=(4e)^{-m}$. Translation invariance makes $\nu(F_{b,m})=0$. Replacing $F_{b,m}$ by $F_{b,m}+\epsilon_b$ gives a time norm squared between $\epsilon_b^2$ and $2\epsilon_b^2$ while preserving the lower bound (9). Thus for these nonnull vectors
\[
 R(F_{b,m}+\epsilon_b)\ \ge\
       \frac{c(4e)^{2m}}{2(1+\beta)^2(m+1)}.                          \tag{11}
\]
The sources fit in a fixed physical box with $ba$ fixed and positive. Their spatial width in direction 1 is zero. For example, if $\log(1+\beta)=o(b)$ this grows exponentially in $b$. For the mirror through the source, this rules out a uniform comparison of the two reflection norms in the isotropic Wilson measure. The effect of moving that mirror is determined in (25) and the paragraph preceding it. The undivided time norms in (10) tend to zero. The construction neither exhibits low physical masses nor rules out choosing better representatives for specific nonzero continuum states.

**OPEN.** A Wilson-specific argument must control the states near the spectrum in (5) after normalization. The width in (8) and even the representation of each plaquette in a source do not by themselves control the change of reflection norm. Replacing the cube trace by local states has removed a state-counting requirement and introduced a question about which energy-momentum states the local sources can carry.

## Which local tests would suffice

**PROVED (three reflected correlations).** Fix $h>0$ and any nonempty open Euclidean box $\mathcal O$ of bounded closure strictly inside positive time. Suppose a full Wightman vacuum theory with the forward spectrum condition and Lorentz covariance has been constructed and its ordered Euclidean field products are matched on the same Wilson states. For each finite linear combination $A$ of strictly time-ordered smeared products in $\mathcal O$, including the constant, use the matched lattice representatives $F_j$. At fixed spacing take the specified infinite-volume periodic limit $\nu_j$ first. Let $a_j\downarrow0$ and $a_jk_j\to h$ with positive integer $k_j$. Assume matching for the three displayed reflected products, with the action of the indicated translations in the same vacuum representation. Write
\[
 C_j(s,w)=\nu_j\bigl(\overline{\theta_0F_j}\,\tau_{s e_0+w e_1}F_j\bigr).
\]
For every $A$ of nonzero limiting reflection norm,
\[
 \frac{\langle v_A,B_hv_A\rangle}{\|v_A\|^2}
   =\lim_j\frac{C_j(k_j,0)-\operatorname{Re}C_j(k_j,k_j)}
                      {2C_j(0,0)} .                                   \tag{12}
\]
Expand the difference squared in $B^{(k_j)}$ and use the commutation and unitarity of the spatial shift. PL4 identifies the lattice matrix elements. The same computation in the matched continuum datum proves (12). In particular an upper bound $q<q_0$ on the **supremum over $A$ of these limits** gives (2), with $\delta=\log(q_0/q)$. Taking a supremum over arbitrary cutoff-dependent sources before the limit would be stronger. A zero-norm limit supplies no normalized test. If only the scalar Schwinger functions are matched, this argument applies only in their cyclic sector. [Matching on the target Hilbert space](gap-neutral-chain-check-astra.md)

**PROVED (totality in the box, under the Wightman hypotheses).** Here is why the source restriction to $\mathcal O$ in (12) suffices. Let $\psi$ annihilate the Euclidean product vectors in this box and the vacuum. For each ordered list of $r$ generating fields, pair $\psi$ with the corresponding real-time vacuum vector distribution, using successive coordinate increments $y_1=x_1$, $y_i=x_i-x_{i-1}$. This is tempered. The norm squared of a smeared vector is its $2r$-field Wightman distribution applied to the reflected adjoint test tensor its test, and is bounded by a continuous Schwartz seminorm squared. With $U(x)=\exp(iP\cdot x)$, the Fourier momenta dual to the increments are each in the forward cone (plane waves $e^{ip\cdot y}$). For polynomial bra vectors this is the Wightman spectral support at the corresponding cuts between consecutive fields, including the cut between the bra and the first ket field. Smearing the bra preserves the support. Approximation of $\psi$ in Hilbert norm and the seminorm bound give the same support for general $\psi$.

**PROVED.** At $y_i+i\eta_i$ with every $\eta_i$ in the open forward cone, multiply the Fourier kernel by $\exp(-\sum_i p_i\cdot\eta_i)$. On the support this damps exponentially in every $|p_i|$. Locally in the $\eta_i$, a smooth cutoff equal to one near the support may extend the kernel as a Schwartz function by restricting large momenta to slightly larger cones with the same damping. Differentiation gives a holomorphic function in the connected product tube. Its boundary value is the original tempered distribution. After smearing in the real variables the multipliers tend to one on the Fourier support in every required Schwartz seminorm of the test, using its rapid decrease. Its values at purely imaginary time increments of positive length and real spatial increments are the ordered Euclidean vector pairings. Choose the $r$ absolute times in disjoint ordered subintervals of $\mathcal O$ and the spatial positions in its spatial interior. The pairings vanish on this open Euclidean set, by the assumed orthogonality and arbitrary smooth smearing. The power series of a holomorphic function vanishing on this open totally real set has every coefficient zero, after the invertible change to increment coordinates and multiplication of the time coordinates by $i$. Analytic continuation and the boundary-value identity give zero on all real tests. Wightman cyclicity for the full generating family gives $\psi=0$. This proves the totality used in (12) without a time-zero cyclicity assumption.

**PROVED (a limitation intrinsic to time-zero configuration algebras).** Suppose more specifically there is a vacuum net of bounded local observables, cyclic globally, with positive energy and nonzero Hamiltonian. An abelian von Neumann algebra of configurations localized at time zero in a fixed-width spatial strip cannot be cyclic on this Hilbert space if it commutes with observables spacelike to the strip. Indeed some two bounded local operators do not commute. Otherwise the globally generated von Neumann algebra would be abelian and cyclic. Complex conjugation $J$ on its cyclic representation, defined by $J A\Omega=A^*\Omega$, is an antiunitary isometry because the algebra is abelian. It commutes with the vacuum-preserving time translations, whence $JHJ=-H$, contradicting positive, nonzero energy. Translate a noncommuting local pair far enough in direction 1 that both supports are spacelike to the time-zero strip. Both now belong to the strip algebra's commutant. An abelian algebra with a cyclic vector has abelian commutant. In its cyclic spectral representation it acts by all bounded multipliers on a scalar $L^2$ space. An operator commuting with indicators there agrees on simple functions with multiplication by its value on the constant one, and boundedness makes that value essentially bounded. The translated pair contradicts this property. This distinguishes the full box of ordered field products in (12) from the class covered in (8).

**PROVED (a shell representation in the Wilson model).** For a lattice box $D$ compactly inside $\mathcal O$, take a set $I$ of interior bonds and take as boundary bonds all exterior bonds in any plaquette meeting $I$. Enlarge this one-layer boundary to include other bonds read by the source if needed. For a source supported on $I$ and the boundary, let $f$ be its conditional integral over $I$ with that boundary fixed. It is the finite Haar integral with the Wilson factors on the plaquettes meeting $I$, divided by the same integral with insertion one. The denominator is strictly positive. The DLR formula gives the same $f$ conditional on the whole exterior. For any bounded negative-time test $G$, both $G$ and the boundary are exterior for fine enough spacing. Hence $\nu_j(\overline G F_j)=\nu_j(\overline G f_j)$. Reflection and translation covariance give the same identity for the other reflected and displaced copies in (12). Equivalently their disjoint interiors integrate independently conditional on the common exterior. Thus replacing each source by its shell function gives exactly the same three numbers at each cutoff. This observation supplies actual Wilson boundary integrals for (12). It supplies no estimate on their normalized difference.

## Sharpness tests with free gauge curvature

**PROVED (why the strip width enters quadratically).** In the free four-dimensional theory of three independent Maxwell colours, a colour-singlet pair of time-zero magnetic fields approaches $q_0$ with deficit $O(A^{-2})$ using a strip of width $Ah$. To see this, use units $h=1$ and put $\mathbf p_c=(\pi/4,0,0)$. Smear each $F_{12}^a$ with $f_A(\mathbf x)=A^{-3/2}\phi(\mathbf x/A)e^{i\mathbf p_c\cdot\mathbf x}$, where $\phi$ is smooth, supported in a ball of diameter one, and has nonzero integral. Use a spatial translate if needed to place the strip. Take the vacuum-subtracted sum of squares of these smeared fields over the three colours. This is invariant under the common adjoint colour rotation and the linear abelian gauge shifts of the free potentials.

**PROVED.** The positive-time two-point measure for a time-zero $F_{12}$ has spatial density proportional to $(p_1^2+p_2^2)/(2|\mathbf p|)$ and energy $|\mathbf p|$. Fourier differentiation of the transverse free potential uses the vector $(-p_2,p_1,0)$ orthogonal to $\mathbf p$. Equivalently take the two spatial curls of the scalar covariance with time transform $e^{-t|\mathbf p|}/(2|\mathbf p|)$. In the Wick square its two momenta have, after normalization, the product of the corresponding one-field probability laws weighted by $|\widehat f_A|^2$. This follows by the two cross pairings. Subtracting the vacuum removes the internal pairing and summing colours supplies a common positive constant. The mean squared distance of either momentum from $\mathbf p_c$ is $O(A^{-2})$. Indeed change variables to $A(\mathbf p-\mathbf p_c)$, use rapid decay of $\widehat\phi$ and the linear growth of the density. The normalizing integral tends to a strictly positive limit. The multiplier now is
\[
 e^{-|\mathbf p|-|\mathbf p'|}\sin^2((p_1+p'_1)/2).
\]
At $(\mathbf p_c,\mathbf p_c)$ it equals $q_0$ and all six first derivatives vanish. Taylor's theorem on a fixed small neighborhood and the bound on the two second moments outside give a normalized expectation at least $q_0-C/A^2$. Smearing makes these Gaussian variables square integrable with all polynomial moments. Truncations of the quadratic reading give bounded same-time functions with convergent Hilbert norms and matrix elements. The construction uses free fields throughout. It shows why allowing the strip width to tend to infinity in (8) loses its uniform deficit even in a singlet curvature sector.

**PROVED (a compact scalar source can see the threshold without a massless pole).** Use the free action-density field in the normalization of Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Their outline lines 1601–1624 give the separated connected covariance $A_0|x|^{-8}$, $A_0=3d_Gg^4/\pi^4$, $d_G=3$ here. Its positive spectral representation on separated reflected tests is
\[
 \frac{A_0}{|x|^8}=\frac{A_0\pi^2}{192}\int_0^\infty s^2G_s(x)\,ds,\qquad
 G_s(x)=\int_0^\infty (4\pi u)^{-2}e^{-su-|x|^2/(4u)}\,du .          \tag{13}
\]
In fact the $s$ integral at fixed $u$ is $2/u^3$ and substitution $z=|x|^2/(4u)$ leaves $\int_0^\infty z^3 e^{-z}dz=6$. The spatial transform of $G_s$ at positive time $t$ is $e^{-tE}/(2E)$, $E=\sqrt{|\mathbf p|^2+s}$. The full Fourier transform is $(p_0^2+|\mathbf p|^2+s)^{-1}$ by the Gaussian integral, and its inverse in time is the decaying Green function with derivative jump $-1$. All reflected insertions used here are separated in time. Contact terms play no role. [Free curvature entry](sa-index/chunk-02.md)

**PROVED.** Fix $h>0$ and choose a smooth positive-time test $f$ in the box with Fourier–Laplace transform $f_L(E,\mathbf p)=\int f(t,\mathbf x)e^{-tE+i\mathbf p\cdot\mathbf x}\,dt\,d\mathbf x$ nonzero at $(p_*,\pm p_*e_1)$, $p_*=\pi/(2h)$. A nonnegative bump narrow in $x_1$ has this property, since its spatial phases lie in an open semicircle at those momenta. For the resulting centered vector $v_f$ there are $0<c_f\le C_f<\infty$ such that for all sufficiently large integers $l$,
\[
 c_f q_0^l l^{-9/2} \le
       \langle v_f,B_h^l v_f\rangle\ \le\ C_f q_0^l l^{-9/2}.         \tag{14}
\]
Indeed (13) gives the measure proportional to $s^2|f_L(E,\mathbf p)|^2 ds\,d^3\mathbf p/(2E)$. The multiplier $b=e^{-hE}\sin^2(hp_1/2)$ has just the two maxima at $s=0$, $\mathbf p=\pm p_*e_1$. Near either, $\log(q_0/b)$ is between positive constant multiples of $s+|\mathbf p\mp p_*e_1|^2$. The longitudinal term has a nondegenerate quadratic maximum, and $E-|p_1|=(s+|\mathbf p_\perp|^2)/(E+|p_1|)$ there. The remaining density factor $|f_L|^2/(2E)$ is bounded above and below there. Integrating $s^2e^{-cl s}$ costs $l^{-3}$, and the three momentum integrations cost $l^{-3/2}$. For the lower bound integrate $s<1/l$, $|\mathbf p\mp p_*e_1|<1/\sqrt l$. Off fixed neighborhoods the multiplier is bounded strictly below $q_0$ by compactness at bounded $E$ and exponential damping at large $E$. The source has finite spectral measure. This proves (14). Vanishing threshold density through order $s^2$, gauge invariance of the local free scalar, and the explicit power gain in (14) all coexist with spectral support down to zero. A strict improvement of the exponential base for the interacting Wilson theory requires an additional estimate.

## How much of a near-threshold vector a whole strip can measure

**PROVED (a spatial momentum estimate in the Wilson Hilbert space).** Let $\mathcal S_D$ be the closed span of the time-zero functions in a *specified* strip of width $D$ along axis 1. One may take gauge-invariant functions throughout. For $0<\varepsilon<1/4$ let $\Pi_{\varepsilon,k}$ project on the two momentum intervals $\bigl|k|\eta|-\pi/2\bigr|\le\varepsilon$, with principal lattice angle $\eta$. Uniformly over translations of the strip and over the Wilson states above,
\[
         \|\Pi_{\varepsilon,k}P_{\mathcal S_D}\|^2
                     \le C(1+D/k)\varepsilon .                         \tag{15}
\]
This estimates the projection itself, so it also controls the best mean-square approximation of a momentum packet by all functions of the strip.

**PROVED.** Normalize one time-zero vector $\Phi$ in the strip. Its spatial spectral measure has Fourier coefficients $C(w)=\langle\Phi,U^w\Phi\rangle$. By the identity preceding (6), for $w\ge D$ these are $\int_0^1 s^{w-D}\,d\sigma(s)$ with $\|\sigma\|_{\rm TV}\le1$. Indeed the spectral projections of $S$ paired between the two transverse vectors have total variation at most the product of their norms, by Cauchy–Schwarz on any partition, and $R(F)\le1$. Also $C(-w)=\overline{C(w)}$. For $0<z<1$ form the Poisson smoothing of the spectral probability, with density $(2\pi)^{-1}\sum_w z^{|w|}C(w)e^{-iw\eta}$. Put $D'=\max(1,D)$. The terms $|w|<D'$ have total modulus at most $2D'$. For $w\ge D'$ the geometric sum under the measure is bounded in absolute value by $\sup_{0\le s\le1}|1-zs e^{-i\eta}|^{-1}$. To bound this by $2/|1-e^{-i\eta}|$, use $1-zs\le|1-zs e^{-i\eta}|$ and the triangle inequality. The conjugate tail has the same bound. On either interval in (15) the resulting density is at most $C(D'+k)$. The bound holds on slightly larger intervals as well. Passing $z\uparrow1$ against nonnegative continuous test functions there yields the same density domination for the unsmoothed measure, including interval endpoints. Integrate over the total length $4\varepsilon/k$ and complete the time-zero subspace. Spatial translations commute with the momentum projection and carry the strip subspace onto the translated strip subspace. This proves (15).

**PROVED (delocalization of a possible obstruction).** For any unit vector $v$ set $\gamma=1-\langle v,B^{(k)}v\rangle/b_k+k^{-2}$. When $k\ge K$, (5) gives $\|(1-\Pi_{\varepsilon,k})v\|\le C\sqrt{\gamma}/\varepsilon$. Taking adjoints in (15) gives
\[
 \|P_{\mathcal S_D}v\|
    \le C\bigl(\sqrt{(1+D/k)\varepsilon}+\sqrt{\gamma}/\varepsilon\bigr)
    \le C'(1+D/k)^{1/3}\gamma^{1/6},                                  \tag{16}
\]
whenever $(\gamma/(1+D/k))^{1/3}<1/4$, by taking that value for $\varepsilon$. Thus a sequence approaching the sharp threshold becomes orthogonal, in projection norm, to every time-zero strip of bounded physical width at fixed $h$. This holds uniformly even if the strip position is chosen after the state. For a bounded positive-time source $F$, the projection $P_{\mathcal S_D}[F]_0$ is represented by the conditional expectation of $F$ given the spatial links in the strip. Pair both with an arbitrary strip function in the time-reflection inner product, using that time reflection fixes that function. For invariant $F$, conditional expectation has an invariant version by gauge averaging. Thus even the best such strip representative retains a vanishing fraction of a normalized near-threshold state's norm as $\gamma$ tends to zero.

## A test with fixed sources and increasing separation

**PROVED (the gain from the known Wilson estimates).** For a bounded strip-supported positive-time $F$ with nonzero time norm, $k\ge K$, and $l\ge1$,
\[
 \frac{\langle\Phi,(B^{(k)})^l\Phi\rangle}{b_k^l\|\Phi\|^2}
       \le \frac{C[1+D/k+R(F)]}{\sqrt l}.                            \tag{17}
\]
In the Abel-sum argument of (15), the two tails for a normalized general source acquire the factor $R(F)$. In a fixed small neighborhood of $x= k|\eta|=\pi/2$, the spatial measure in the variable $x$ is consequently bounded by $C(D/k+1+R(F))\,dx$. For $0<x<\pi$ the log of the upper multiplier in (3) has second derivative $-\tfrac12\csc^2(x/2)-g''(x/k)/k\le-1/4$ for all sufficiently large $k$, since $g''$ is bounded near zero. Its maximum at $x_k=\pi/2+O(k^{-2})$ therefore gives a relative upper bound $\exp[-(x-x_k)^2/8]$. Outside the neighborhood there is a uniform strict loss, including all $x>\pi$ by the estimate in (5). Integrating this Gaussian to power $l$ and bounding the rest by the total spectral mass proves (17). This gives a power improvement over the unrestricted spectral envelope using only actual reflected Wilson norms. Equation (14) explains why an inverse power, even with a larger exponent, cannot give the desired spectral conclusion.

**PROVED (a full-space test without interchanging cutoff and source suprema).** Under the matching and totality hypotheses of (12), now with matching of all fixed translated pairs, take a countable total family $v_i$ from the box in the separable Hilbert space and $w_i=2^{-i}/(1+\|v_i\|^2)$, $i\ge1$. For any integer $J(l)\to\infty$,
\[
 s_l=\sum_{i=1}^{J(l)} w_i\langle v_i,B_h^l v_i\rangle,\qquad
                     \lim_{l\to\infty}s_l^{1/l}=\|B_h\|.             \tag{18}
\]
The upper bound uses positivity and $\sum_i w_i\|v_i\|^2\le1$. For any $0<r<\|B_h\|$ the spectral projection of $B_h$ on $(r,\|B_h\|]$ is nonzero and some fixed $v_i$ has nonzero projection there by totality. Its contribution for every sufficiently large $l$ bounds $s_l$ below by a fixed positive multiple of $r^l$. At zero norm the identity is immediate.

**PROVED.** In (18) each term of fixed order $l$ is a limit of a *finite* linear combination of ordinary Wilson observables. In the notation of (12) the coefficients of $C_j(lk_j,dk_j)$, $-l\le d\le l$, are $(-1)^d4^{-l}{2l\choose l+d}$. This is the expansion of $4^{-l}(2-U^{k_j}-U^{-k_j})^l$ and their absolute values sum to one. With $k_j$ even, the whole combination is also the squared reflection norm of the positive-time source $2^{-l}\tau_{lk_j e_0/2}(1-\tau_{k_je_1})^lF_{i,j}$. For each $l$ the cutoff limit is taken on this finite list *before* increasing $l$. Small denominator directions of an unrelated cutoff ensemble do not enter (18). A growth bound $s_l\le C(q_0 e^{-\delta})^l$ for all large $l$ at one physical $h$, with $\delta>0$, would suffice.

**PROVED (precision at short physical distances).** For $y\downarrow0$, the maximizers in (1) are $x_0+O(y^2)$. Uniform convergence places them near $x_0$, and the critical equation there is $\cot(x/2)=x/\sqrt{x^2+y^2}$. Using this estimate of $x$ and the vanishing first derivative of the zero-mass log multiplier gives
\[
            \log[Q(hM)/q_0]=-\frac{(hM)^2}{\pi}+O((hM)^4).            \tag{19}
\]
Thus the distinction between a fixed positive mass and zero mass in this norm is quadratic in the observation length as $h\downarrow0$. If $g(h)^{-2}/\log(\ell/h)\to c_*>0$ at a fixed reference length $\ell$, that distinction is smaller than every fixed power of $g(h)$. The running law is an explicit hypothesis here. The outline's F3 requires this logarithmic law, and its F2 bounds a relative error on prescribed test shapes. The precision on (18) remains open. [Outline lines 4289–4314 and 4360–4374, indexed here](sa-index/chunk-04.md)

**PROVED.** More precisely, take a nonzero fixed $M$ and states whose normalized expectations at small $h$ come within $O((hM)^2)$ of $q_0$. If the lattice error $k^{-2}=o((hM)^2)$ and the same approximation holds for their Wilson representatives, (7) forces
\[
        1+D/k+\log(2+R(F))\ \ge\ c/(hM),                              \tag{20}
\]
where $c$ depends on the constant in the approximation. At bounded $D/k$ this demands exponential growth of the ratio of the two reflection norms in $1/(hM)$. At bounded $R(F)$ it demands a spatial strip of physical width of order at least $1/M$ when $ka=h$. Boosting to weak coupling changes momentum and energy together and leaves the mass scale in the small difference (19).

## A contact sum rule for the actual Wilson transfer matrix

**PROVED.** Work first on a finite periodic spatial cube of side $n\in4\mathbb N$ with the time direction in its vacuum limit. Use the normalized time transfer $\mathcal T=D C D/\lambda$, with real positive normalized vacuum $\psi$, as in row 1161. Here $D$ is the bounded, strictly positive magnetic half-weight, $C=\bigotimes_e C_e$ is the normalized electric convolution before restriction to gauge invariants, and $\lambda$ is the largest eigenvalue of $D C D$. For real gauge-invariant polynomial multipliers $f,g$ on disjoint sets of spatial links (subtracting a real constant is allowed),
\[
 \langle\mathcal T^{-1/2}f\psi,\mathcal T^{-1/2}g\psi\rangle
                          =\langle f\psi,\mathcal T g\psi\rangle .       \tag{21}
\]
Time energies and momenta in this section are in lattice units. Row 1161 proves a diagonal inverse-moment estimate. Equation (21) determines the off-diagonal matrix elements of its difference from the forward transfer. The convolution multipliers, their factorial decay and localized polynomial conjugation also appear in the outline by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. [Row 1161, (18)–(20)](gap-solve9-astra62.md) · [Outline GL3–GL7, lines 2224–2243 and 2293–2311](sa-index/chunk-02.md)

**PROVED.** Write $v=D\psi$, so $D^{-1}\psi=Cv/\lambda$. Polarization of the inverse-form variational formula for $DCD$ gives the left side of (21) as $\lambda^{-1}\langle C^{-1/2} f C v,C^{-1/2}g C v\rangle$. On finite Peter–Weyl sums the tensor-factor identity $C f C^{-1}g C=g C f$ holds. On the support of $f$ it reads $C_A f C_A^{-1}C_A=C_A f$, on that of $g$ it reads $C_B C_B^{-1}g C_B=g C_B$, and the exterior factor is just $C_{\rm ext}$. For the passage to $v$, truncate all link degrees at $N$. At fixed $\beta,n$ the degree shift of $f$ is bounded. On each affected link the ratio of convolution eigenvalues at two allowed degrees is bounded by a fixed polynomial in the input degree by GL4. The remaining factor from $C^{-1/2} f C$ decays factorially, since its block weight is $r_{\rm in}^{1/2}(r_{\rm in}/r_{\rm out})^{1/2}$. Each block meets boundedly many output blocks and the exterior factor $C_{\rm ext}^{1/2}$ is bounded. Thus $C^{-1/2}fC$ and its counterpart for $g$ extend boundedly on this fixed cube. Taking $N\to\infty$ gives the mixed form as $\lambda^{-1}\langle v,g C f v\rangle$. Reality and symmetry give $\lambda^{-1}\langle f v,C g v\rangle$, proving (21). No bounded inverse of the transfer is required.

**PROVED.** Choose a spatial $23$-plaquette $p$ and let $f_x$ be translates of the same centered real plaquette polynomial on $p+x e_1$, $x\in\mathbb Z/n$. These plaquettes have disjoint links for every pair of distinct $x$. Write $u_x=f_x\psi$, $V u_x=u_{x+1}$, and let $\mu$ be the joint spectral measure of $u_0$ for $\mathcal T=e^{-E}$ and $V=e^{i\eta}$. Injectivity removes any atom at transfer eigenvalue zero. With $\mu_\eta$ the measure over one axial momentum and $d_{\beta,n}=\langle u_0,(\mathcal T^{-1}-\mathcal T)u_0\rangle_{\rm form}$, cyclic Fourier inversion of (21) gives
\[
 \int 2\sinh E\,d\mu_\eta(E)=\frac{d_{\beta,n}}{n}
             \qquad\left(\eta=\frac{2\pi j}{n},\ 0\le j<n\right).       \tag{22}
\]
Indeed every nonconstant Fourier coefficient of the measure on the left vanishes. This is exact on the finite spatial cube and uses neither a continuum identification nor an estimate of a running coupling.

**PROVED.** Fix the absolute $A$ in row 1161 and use $f_x=\cos(d\arccos W_{p+x e_1})-\langle\cos(d\arccos W_p)\rangle$ with $d=\lceil A\sqrt\beta\rceil$, $\beta\ge1$. The inverse estimate there gives $d_{\beta,n}\le C_A^4$. For any complex coefficients $z_x$, choose even or odd $x$ carrying at least half of $\sum |z_x|^2$. On a finite periodic spacetime cylinder condition on all links except one fixed-orientation edge on each of these chosen plaquettes. No action plaquette contains two of the selected links. Each remaining plaquette reading in the family is fixed, and the selected readings are conditionally independent with conditional variance at least $c_0$ by the one-link estimate of row 1161. The law of total variance gives $\|\sum z_x u_x\|^2\ge(c_0/2)\sum |z_x|^2$ after the cylinder time length tends to infinity. The limit uses the simple top eigenvalue of the positive transfer kernel. Applying the inequality to $z_x=e^{-ix\eta}/n$ and using (22) yields
\[
 \mu_\eta([0,E_*])\ge\frac{c_0}{4n},\qquad
              E_*=\operatorname{arsinh}(2C_A^4/c_0).                  \tag{23}
\]
The spectral mass above $E_*$ is at most $d_{\beta,n}/(2n\sinh E_*)$. Every axial momentum on every such cube thus occurs among center-neutral excited states of the Wilson theory with energy at most $E_*$ in lattice units. Centering removes the vacuum also for $\eta=0$. This resolves the earlier count by one exact momentum component. It supplies an upper bound on accessible excitation energies, whereas the physical lower edge requires information at lattice energies of order the lattice spacing. [Row 1161, conditional variance and inverse estimate](gap-solve9-astra62.md) · [Check of row 1161, S21–S24](gap-solve9-check-opus.md)

## Testing the sum rule at a two-particle threshold

**PROVED (a massless singlet comparison with the same axial contact).** Use three independent copies of a free lattice magnetic $23$-curvature and their centered colour sum of squares. The free covariance needed for this calculation can be defined directly. For dimensionless spatial momentum $p$ in the three-torus set $\widehat p_i^2=4\sin^2(p_i/2)$, $b(p)=\widehat p_2^2+\widehat p_3^2$ and
\[
 \cosh\omega(p)=1+\tfrac12\bigl(m^2+\textstyle\sum_i\widehat p_i^2\bigr).
\]
The time-$t$ covariance for one copy at fixed $p$ is $b(p)e^{-|t|\omega(p)}/(2\sinh\omega(p))$. Indeed the temporal Fourier inverse of $(2\cosh\omega-2\cos p_0)^{-1}$ solves the decaying second-order difference equation with unit source at $t=0$, giving the stated denominator. Taking the spatial curl of two independent free components in directions 2 and 3 gives the numerator. At $m=0$ this is the Maxwell field-strength two-point function in these indices. The resulting covariance is finite locally in three spatial dimensions and time-reflection positive by its displayed spectral form. The nonzero-$m$ formula is also a Gaussian comparison.

**PROVED.** Wick's rule gives the singlet square a two-particle measure, up to a positive constant,
\[
 \frac{b(p)b(q)\,dp\,dq}{4\sinh\omega(p)\sinh\omega(q)},\qquad
       E=\omega(p)+\omega(q),\qquad\eta=p_1+q_1\pmod{2\pi}.           \tag{24}
\]
The Haar momenta may be normalized to mass one. Multiplication by $2\sinh E$ replaces the factor after $b(p)b(q)$ by $\tfrac12(\coth\omega(p)+\coth\omega(q))$. At fixed $\eta$ integrate with $q_1=\eta-p_1$. In the first term $b(q)$ is independent of $q_1$ and no other factor depends on $q_1$. In the second term interchange the integration variables. The resulting density in $\eta$ is exactly constant, positive and bounded for $0\le m\le1$. The unweighted axial density also has an absolute positive lower bound in that range. Restrict both transverse momenta to fixed positive-measure sets on which $b$ is bounded below, and use the common upper bound on $\omega$. All integrals at $m=0$ converge since $b(p)=O(|p|^2)$ at zero. Thus the analogues of both (22) and (23) hold in this singlet sector.

**PROVED.** For $m=0$ the lower edge at fixed axial angle is exactly $g(|\eta|)$ despite the absence of a one-particle component. Each $\omega(p)\ge g(|p_1|)$. The increasing concave function $g$ vanishes at zero, so $g(u)+g(v)\ge g(u+v)$ for $u+v\le\pi$. For $u+v\ge\pi$, concavity gives $g(u)+g(v)\ge (u+v)g(\pi)/\pi\ge g(\pi)$. The triangle inequality for principal angles now gives the lower edge bound. Conversely take $q$ close to zero and $p$ close to $(\eta,0,0)$ with the prescribed axial sum, keeping both transverse curls nonzero. Every neighborhood above that edge has positive measure by (24), including when $\eta=0$. The sharp multiplier in (3) therefore lies in the support for every $k$ in this comparison. For $m>0$ all energies in (24) are at least $2\operatorname{arcosh}(1+m^2/2)$. The Wilson contact identity fixes a moment of positive energies. Its form and a coupling-uniform lower bound on the accessible spectral weight by themselves allow both lower edges.

## Padding and the cost of preparing a fixed momentum

**PROVED.** The lower bound (11) concerns the mirror through the source. In the axis-symmetric periodic limit, enclose the very same source in the interval between transverse mirrors at distances $b$ on both sides. Translate it to $x_1=b$ and use $D=2b$ in (6). The functions $G_m$ and the constant are invariant under interchanging the 0 and 1 coordinates. The squared right transverse norm now pairs two copies with separation $2b$ in direction 1 at the same time. The squared left transverse norm does the same after a time reflection. By translation and the axis interchange, each equals the original time norm squared, which pairs the two copies at time separation $2b$. Hence this choice has $R=1$ for every $b,m$, including the added constant. In particular it would be incorrect to use the exponentially large value in (11) as a lower bound over all enclosing strips.

**PROVED (every bounded-width representation of certain matched packets has large cost).** Suppose the nontrivial relativistic theory and totality of the box in (12) hold, with matching at every fixed spatial translate used below. Fix $A<\infty$ bounding $D_j/k_j$ and an integer $m\ge1$. Take an integer $L$ with $4L>A$. Every nonzero spectral orbit contains a point with $hp_1=\pi/2$. In every sufficiently small joint spectral neighborhood of that point there are unit vectors for which the real part of the expectation of
\[
                   e^{4iLhP_1}\left((1-e^{2ihP_1})/2\right)^m          \tag{25}
\]
exceeds $3/4$. This follows from continuity of the multiplier and its value one at that point. The spectral neighborhood can be bounded in energy. By the box totality, approximate one such vector in norm by a normalized finite linear combination of fixed box sources until its expectation has real part greater than $1/2$. The error in expectation is at most twice the distance, since (25) is a contraction. For *any* sequence of Wilson representatives of this fixed combination matching its norm and its finitely many spatially translated pairs, (6) at $w_0=4Lk_j$ yields $\liminf_j R(F_j)\ge 2^{m-1}$ for every choice of enclosing strips of the indicated widths. Nonvanishing continuum norm is built into this construction.

**PROVED.** As $m$ is arbitrary, no common reflection-norm bound over fixed-box preparations with bounded physical padding is compatible with a full nontrivial relativistic limit, even one with positive mass. Equation (25) depends only on momentum. The contribution of energy in (5) is indispensable to any argument using (7) to separate the massive and massless cases.

## A second Wilson moment and its range in space

**PROVED.** On the same vacuum cube, for polynomials in disjoint bond sets $S_f,S_g$ such that no spatial action plaquette meets both sets, one has
\[
 \langle\mathcal T^{-1}f\psi,\mathcal T^{-1}g\psi\rangle
                       =\langle\mathcal T f\psi,\mathcal T g\psi\rangle . \tag{26}
\]
Here the individual inverse vectors exist. Write $\widehat f=C^{-1}fC$ as the finite-band series GL5 on smooth functions and use its formal adjoint on the same domain, as justified in the outline by Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Put $A_f=D^{-1}\widehat f D$ and $A_f^\dagger=D\widehat f^\dagger D^{-1}$. Both maps preserve smooth functions. The vacuum is smooth by $\lambda\psi=D C D\psi$ and the smooth kernel of $C$. The identity $\mathcal T A_f=f\mathcal T$ on smooth functions follows from GL6, and its formal adjoint is $A_f^\dagger\mathcal T=\mathcal T f$. Thus $\mathcal T^{-1}f\psi=A_f\psi$ by injectivity, and $\mathcal T f\psi=A_f^\dagger\psi$. [Outline GL5–GL7, lines 2245–2311](sa-index/chunk-02.md)

**PROVED.** In $A_f$ or $A_f^\dagger$ all factors of $D$ from plaquettes missing $S_f$ cancel, since they are multiplications in spectator variables. The remaining operator acts on $S_f$, with the other variables of plaquettes meeting $S_f$ entering as smooth parameters. When no spatial plaquette meets both supports, $A_f^\dagger$ and $A_g$ commute. To verify this even for shared spectator variables, fix those variables and use the tensor product of the two independent sets of active variables. Their smooth expansions in their separate active variables commute by GL5 and its adjoint. Consequently the left side of (26) is $\langle\psi,A_f^\dagger A_g\psi\rangle=\langle\psi,A_g A_f^\dagger\psi\rangle=\langle\mathcal T g\psi,\mathcal T f\psi\rangle$. Reality gives (26).

**PROVED.** For the single $23$-plaquette family in (22), the weighted measure $\int 2\sinh(2E)\,d\mu_\eta$ has discrete Fourier coefficients zero except at $0,\pm1$. Indeed a spatial plaquette cannot meet links in two parallel $23$ planes at axial distance greater than one. The remaining coefficients are real and even by reality, self-adjointness and translation invariance. Thus for real constants $a,b$ depending on the cube, coupling and insertion,
\[
 n\int 2\sinh(2E)\,d\mu_\eta=a+2b\cos\eta .                           \tag{27}
\]
For a nonconstant centered reading, $d_{\beta,n}>0$ by simplicity of the vacuum. Under the probability measure $n(2\sinh E)\,d\mu_\eta/d_{\beta,n}$, the mean of $\cosh E$ is exactly $(a+2b\cos\eta)/(2d_{\beta,n})$. This is a second constraint on the distribution, with no estimate here on the lower end of its support.

**PROVED.** Even the range statement (27) is compatible with the massless comparison (24). Expanding $\sinh(2(\omega_p+\omega_q))$ by addition and dividing by $2\sinh\omega_p\sinh\omega_q$ gives a sum of a constant times $\cosh\omega_p(2\cosh^2\omega_q-1)/\sinh\omega_q$ and its interchange. In the first term the only dependence on $p_1$ outside the constraint is through $\cosh\omega_p=c(p_\perp)-\cos p_1$. Integrating at $p_1=\eta-q_1$ removes the sine part by symmetry in $q_1$, leaving only the constant and the first cosine. The other term has the same property. Thus a nearest-neighbor second moment of this type cannot by itself remove the continuum reaching the massless edge in (24).

## Resolving neutral Wilson excitations at every spatial momentum

**PROVED.** There is a bounded neutral Wilson source on eight links and absolute constants $c_*,E_*>0$ such that for every $\beta\ge1$, every periodic spatial cube $n\in4\mathbb N$, $n\ge16$, and every full lattice momentum $P\in(2\pi/n)(\mathbb Z/n)^3$, its centered vacuum spectral measure satisfies
\[
                     \mu_P((0,E_*])\ \ge\ c_*/n^3 .                  \tag{28}
\]
The source depends on $\beta$ as in (23). The estimate includes $P=0$ and all fine-grid momenta without folding to a sublattice. The energy bound is in lattice units.

**PROVED.** Index the $23$-plaquettes by their lower vertex $x$ and write $g_x=\cos(d\arccos W_{p+x})$ with $d$ as in (23). Put $s=3e_1$, $h_x=g_xg_{x+s}$, and $u_x=(h_x-\langle h_x\rangle)\psi$. Select the edge $(x,2)$ in the first plaquette and $(x+s,3)$ in the second. Of all the translates $h_y$, exactly $h_x$ can read both selected edges. To see this, the first edge requires $y\in\{x,x-e_3,x-s,x-e_3-s\}$, and the second requires $y\in\{x+s,x+s-e_2,x,x-e_2\}$. The intersection is $\{x\}$ on the stipulated torus.

**PROVED.** Colour the periodic sites with at most $K=17^3$ colours so sites in a common class have cyclic sup distance greater than eight. The conflict graph has degree at most $17^3-1$ and greedy colouring gives this bound. For coefficients $z_y$ choose a class $I$ carrying at least $K^{-1}\sum_y |z_y|^2$. Fix all spacetime links except the two selected edges at each $x\in I$. They occur in no common action face, even the two edges in one selected pair, so their conditional laws are independent. For each $x\in I$, project a function under this product law onto the subspace of centered functions in *both* selected variables of $x$, constant in all the other selected variables. This is conditional integration over the other variables followed by the two commuting operators subtracting the respective one-variable means. The subspaces for different pairs are orthogonal. Every $h_y$ with $y\ne x$ misses at least one variable of the pair and has zero projection there. The projection of $h_x$ is the product of its two centered one-plaquette readings, as the separated class ensures that $h_x$ reads no other selected variable. Its squared norm is at least $c_0^2$ by the conditional variance in row 1161. Integrate over the fixed links and take the long-time vacuum limit as in (23). Constants vanish under the pair projections, yielding
\[
                 \Big\|\sum_x z_xu_x\Big\|^2
                            \ge (c_0^2/K)\sum_x|z_x|^2.                \tag{29}
\]

**PROVED.** Put $c_G=c_0^2/K$. The full Fourier character, normalized by $n^{-3}$, gives $\mu_P([0,\infty))\ge c_G/n^3$ by (29). The spatial Fourier coefficients of $\int 2\sinh E\,d\mu_P$ vanish by (21) except when the supports of $h_0$ and $h_x$ share a link. At most $8^2$ translation vectors can do so, since a pair of equally oriented links determines the translation. Each coefficient is at most $C_A^8$ in absolute value by Cauchy–Schwarz for the positive form $\mathcal T^{-1}-\mathcal T$, translation invariance and the local inverse bound of row 1161 for a bounded polynomial on eight links. Fourier inversion gives $\int 2\sinh E\,d\mu_P\le64C_A^8/n^3$. Take $E_*=\operatorname{arsinh}(64C_A^8/c_G)$ and $c_*=c_G/2$. At most half the stated lower bound on total weight lies above $E_*$. Centering excludes the unique vacuum and gives (28). Restriction to a positive compact energy interval is legitimate on each cube since the transfer is compact and its top simple. This rules out missing momentum sectors as an explanation for a low count of neutral states at the cutoff. It gives no uniform bound on their spectral edge at fixed physical separation.

## Taking the contact estimate through periodic four-cubes

**PROVED (a thermal estimate uniform in both periods).** Let $F=DCD$ be the unnormalized spatial Wilson transfer, restricted for the trace to the gauge-invariant space. Take spatial period $n$ and temporal period $L\ge2$. For a real gauge-invariant polynomial $f$ on $b$ spatial links with $|f|\le2$ and degree at most $\lceil A\sqrt\beta\rceil$ per link, $\beta\ge1$, there is a constant $K_A$ independent of $n,L,\beta$ with the following property. In a joint eigenbasis of $F$ and the spatial translations write $\lambda_a>0$, $P_a$ for their eigenvalues and momenta and $Z=\sum_a\lambda_a^L$. Set
\[
 d\rho=\frac1Z\sum_{a,c}\lambda_a^L |f_{ca}|^2\,
    \delta_{(\log(\lambda_a/\lambda_c),\,P_c-P_a)}(dE,dP).
\]
Its mass is at most four. Cyclic Wilson correlations at integer separations $0\le t<L$ are its moments $e^{-tE+iP\cdot x}$, by expansion of the transfer trace. We have
\[
                \int e^E\,d\rho\le K_A^b,\qquad
 d\rho(-E,-P)=e^{-LE}\,d\rho(E,P).                                   \tag{30}
\]
The second expression denotes the corresponding reflected measure identity, obtained by interchanging $a,c$. Complex conjugation on configurations commutes with real multiplication by $f$, with $F$ and with spatial translations. It sends momentum $P_a$ to $-P_a$ and leaves $\lambda_a$ fixed, so $\rho(dE,-dP)=\rho(dE,dP)$ as measures.

**PROVED.** For the first bound in (30) one must account for the signs of excited eigenfunctions. Use a real eigenbasis of $F$ for this momentum-integrated calculation and put $v_a=D\psi_a$. With $B_f=C^{-1/2}fC$, the inverse form as in (21) gives
\[
 \int e^E\,d\rho=Z^{-1}\sum_a\lambda_a^{L-1}\|B_f v_a\|^2 .
\]
The band proof of (20) in row 1161 gives a positive convolution operator $K$ with $B_f^*B_f\le K$ in quadratic forms and $|K(u,v)|\le K_A^b C(u,v)$ in the Haar kernel. Specifically its degree weights are constants times those of $C$ multiplied by $\prod_{e\in\operatorname{supp} f}m_{\ell_e}(y)$, with $y=c_A/\sqrt\beta$ and $m_\ell(y)=(\ell+1)^{-1}\sum_{j=0}^{\ell}e^{(\ell-2j)y}$. The band estimate holds for every smooth input before testing on a vacuum. The conjugacy average of the complex-shifted Wilson kernel gives the displayed absolute kernel comparison, using $\sup_{\beta\ge1}\beta(\cosh(c_A/\sqrt\beta)-1)<\infty$. These are precisely the two estimates needed here from that proof. [Row 1161, proof of (20)](gap-solve9-astra62.md)

**PROVED.** On the full Haar space let $\mathsf P$ be gauge averaging. The positive operator $\sum_a\lambda_a^{L-1}|v_a\rangle\langle v_a|=D F^{L-1}\mathsf P D$ also has a nonnegative integral kernel. This follows by composing the positive Wilson kernels and the Haar average, with $L-1\ge1$. Consequently integration of its kernel against $|K(u,v)|$ bounds the last sum by $K_A^b\operatorname{Tr}(D F^{L-1}\mathsf P D C)=K_A^b Z$. This proves (30) without any positivity assumption on an excited eigenfunction.

**PROVED.** Define the positive momentum measure
\[
 W_{L,n}(dP)=\int_{E>0}2\sinh E\,(1-e^{-LE})\,d\rho(E,dP).
\]
By (30) it equals the integral over signed energies of $2\sinh E\,d\rho$ at the same momentum, and its total mass is at most $K_A^b$. Its spatial Fourier coefficient at displacement $x$ vanishes if $f$ and its translate have disjoint links. Indeed apply the tensor identity in (21) to each real eigenvector $\psi_a$, with $F/\lambda_a$ in place of $\mathcal T$. The proof of equality there uses reality and the eigenvector equation, which persist for every $a$. The inverse forms are finite at fixed volume and their weighted absolute mixed sum converges by (30) and Cauchy–Schwarz. The forward sum converges as well since $\lambda_a^{L-1}\lambda_c\le(1-1/L)\lambda_a^L+\lambda_c^L/L$. Summing gives the stated vanishing. There are at most $b^2$ displacements where two supports share a link. Each Fourier coefficient of $W_{L,n}$ is bounded by its total mass. Therefore discrete Fourier inversion gives the pointwise bound
\[
                   W_{L,n}(\{P\})\le b^2 K_A^b/n^3.                  \tag{31}
\]
This argument works in particular for equal time and space periods. It avoids identifying a limit of spatial-cube vacua with a limit of periodic four-cubes.

## An infrared bound for actual Wilson spectral weight

**PROVED.** Take any periodic four-cube limit at fixed $\beta\ge1$ as in (3), and let $\mu_f$ be the time-reflection spectral measure of the time-zero polynomial in (30). If $dP$ denotes Haar probability on the three-dimensional momentum torus, then, as measures in $P$,
\[
        \int_{E>0}2\sinh E\,d\mu_f(E,dP)\ \le\ b^2 K_A^b\,dP.          \tag{32}
\]
To pass from (31), the finite-cube transition measures $\rho$ have tight positive energy tails by (30). Their negative tail below $-\epsilon$ has mass at most $4e^{-L\epsilon}$ by detailed balance. On every fixed time translate $t\ge0$ the corresponding tail after insertion of $e^{-tE}$ is at most $4e^{-(L-t)\epsilon}$. Along a converging sequence of four-cubes, any joint weak limit is therefore supported on $E\ge0$, and its moments $e^{-tE+iP\cdot x}$ are the limiting Wilson correlations. These identify the time-reflection measure uniquely by density of polynomials in $e^{-E}$ times spatial characters on $[0,1]\times\mathbb T^3$. For a nonnegative continuous spatial test, first include a continuous energy cutoff with compact support in $E>0$ and values in $[0,1]$. The factor $1-e^{-LE}$ then tends uniformly to one on that support. Apply (31), take Riemann sums in $P$, and exhaust $E>0$ by such cutoffs. This proves the domination (32). No convergence of the unbounded signed thermal moment is assumed.

**PROVED (low positive energy weight and temporal decay).** For $0<\epsilon\le1$, integer $t\ge0$ and any spatial translate $x$,
\[
 \begin{split}
      \mu_f\{0<E\le\epsilon\}&\le C b^2K_A^b\epsilon^2,\\
 \big|\nu(f\,\tau_{t e_0+x}f)-\mu_f\{E=0\}\big|
                      &\le C b^2K_A^b(1+t)^{-2}.                    \tag{33}
 \end{split}
\]
Indeed PL5 in each of the three directions gives $E\ge\kappa\max_i|P_i|$. On $s<E\le2s$, $0<s\le1$, the momentum lies in a cube of Haar volume at most $Cs^3$ and $2\sinh E\ge2s$. Equation (32) bounds the mass there by $C b^2K_A^b s^2$. Sum over the dyadic subintervals of $(0,\epsilon]$. The zero-energy measure is at $P=0$ by PL5. For the rest, integrate $e^{-tE}$ against the positive measure, using $t\int_0^\infty e^{-ts}\mu_f((0,s])\,ds$, the first bound at $s\le1$ and total mass at most four beyond it. The spatial phase has modulus one. At $t=0$ the total mass bound suffices. These are original Wilson correlations on the periodic limit for every stated coupling. The constant term in (33) includes the entire invariant projection if the state has several components.

**PROVED.** One also gets a Fourier-space bound. Subtract the invariant part and sum the autocorrelations over integer times with factor $e^{itp_0}$, leaving the spatial Fourier transform as a measure $G(p_0,dP)$. Its time series converges in the norm of spatial measures by (33)'s positive mass estimate at $x=0$. Summing the two-sided geometric series at $E>0$ yields the kernel $\sinh E/(\cosh E-\cos p_0)$. The interchange is justified by summability of the time integrals at $x=0$. By PL5, $\cosh E-1\ge\max_i(1-\cos P_i)$. Hence, away from vanishing denominator,
\[
         0\le G(p_0,dP)\le
       \frac{3 b^2 K_A^b\,dP}{2\big[(1-\cos p_0)+
                                      \sum_{i=1}^3(1-\cos P_i)\big]} . \tag{34}
\]
At $p_0=0$ the spatial singularity on the right is locally integrable. There is no atom of the positive-energy part at $P=0$ by (32). Thus the bound holds as a measure on the whole torus. This derivation of inverse-square infrared control for gauge-invariant Wilson readings uses no assumption of angular order in a pinned sheet. The earlier $O(4)$ sheet estimate applies to a different measure. [Row 977, §5.3](gap-tiltproof-max.md)

**OPEN.** The power in (33) permits positive spectral measure in every interval $(0,\epsilon)$ and is in lattice units. The continuum conclusion needs zero measure on an entire fixed *physical* interval for a total family of matched states. The singlet examples (13) and (24) have still stronger suppression at threshold and retain arbitrarily small positive masses. The Fourier estimate (34) also permits the massless Green singularity.

## Exact contact in the same infinite-volume state

**PROVED.** At each fixed $\beta$ and fixed polynomial $f$, the first-moment contact itself survives the periodic four-cube limit. A second exponential moment controls the possible loss at the ultraviolet end of the integral. On the Haar space $A_fF$ has a real smooth kernel satisfying
\[
             |(A_fF)(u,v)|\le C(\beta,f)F(u,v),\qquad
                     \int e^{2E}\,d\rho\le C(\beta,f)^2 .             \tag{35}
\]
The constant here can depend on $\beta$, the polynomial and its support, but is uniform in the periods for cubes containing that support without wrap. For the first assertion write $A_fF=D^{-1}\widehat f D^2 C D$. In the ratio of its kernel to that of $F$, only factors in $D^2(u)$ from spatial plaquettes meeting the support $S$ of $f$, and the electric kernels for links in $S$, remain inside the action of $\widehat f$. Explicitly the ratio is $(\widehat f\,r)(u_S)/r(u_S)$ where $r$ is the product of these local factors, with the adjacent spatial links and $v_S$ as parameters. This is a compact family of smooth strictly positive functions on a fixed finite product, with all derivatives uniformly bounded and its infimum positive at fixed $\beta$. Continuity of GL5 on smooth functions bounds the numerator uniformly. This proves the pointwise comparison independent of the volume.

**PROVED.** For each eigenvector, $A_f\psi_a=\lambda_a F^{-1} f\psi_a$ as in (26). Thus the second moment in (35) equals $Z^{-1}\sum_a\lambda_a^L\|A_f\psi_a\|^2$. It is the trace divided by $Z$ of $(A_f F) F^{L-2}\mathsf P (A_f F)^*$ on the full Haar space. Gauge averaging and $F^{L-2}$ preserve positivity of kernels, allowing a positive measure kernel also when $L=2$. Replacing both exterior kernels in absolute value by $C(\beta,f) F$ bounds this trace by $C(\beta,f)^2 Z$. This proves (35) without a volume-uniform bound on eigenfunction derivatives.

**PROVED.** In the limiting argument for (32), the part of $\int e^E\,d\rho$ on $E>R$ is now at most $C(\beta,f)^2e^{-R}$. Detailed balance bounds the $e^{-E}$ tail on $E<-R$ by $4e^{-(L-1)R}$, with the other two tails also negligible. Hence the Fourier coefficients of $\int 2\sinh E\,d\mu_f$ are the limits of those of the signed thermal moment, for every fixed displacement. They vanish when supports are disjoint. Its full spatial density at that fixed cutoff is exactly a nonnegative trigonometric polynomial supported in the finite set of overlapping displacements in Fourier space. In particular for a single $23$-plaquette reading it has the form $a_0+2a_2\cos P_2+2a_3\cos P_3$, independent of $P_1$. Indeed the only translates sharing a link are those at $0,\pm e_2,\pm e_3$, and reality gives equal coefficients on opposite translates. This conclusion and the infrared estimate (33) concern the very same infinite-volume state for which the diagonal reflection dispersion bound holds.

## Applying infrared control to the mass detector

**PROVED (arbitrarily broad axial plaquette packets).** In the same periodic infinite-volume states, let $f$ be a centered fundamental $23$-plaquette, or the centered oscillatory plaquette of (23). Write $\Phi_z=\sum_{x\in\mathbb Z} z_x[\tau_{x e_1}f]_0$ for arbitrary finitely supported coefficients. There is an absolute $C$ for the fixed $A$ of (23) such that for $k\ge1$,
\[
 \sup_{\Phi_z\ne0}
 \frac{\langle\Phi_z,B^{(k)}\Phi_z\rangle}{\|\Phi_z\|^2}
 \ \le\
 \begin{cases}
 C(1+\beta)^2/k+e^{-k} &\text{for the fundamental reading},\\
 C/k+e^{-k}             &\text{for the oscillatory reading}.
 \end{cases}                                                           \tag{36}
\]
Here there is no bound on the axial width or on the number of translates in the wave packet. The high-degree source has uniformly positive time-zero fluctuations at all $\beta\ge1$.

**PROVED.** Set $\eta=P_1$. For any nonnegative test $\varphi(\eta)$, (32) and $E\ge\kappa\max_i|P_i|$ imply
\[
 \int_{u<E\le2u}\varphi(\eta)\,d\mu_f
    \le C b^2K_A^b\,u\int\varphi(\eta)\,d\eta,\qquad 0<u\le1,
\]
using normalized Haar measure also on the circle. Indeed the allowed area in $(P_2,P_3)$ is at most $Cu^2$, and $2\sinh E\ge2u$. Dyadic summation gives the same upper bound with $u$ replaced by $\epsilon$ on $0<E\le\epsilon\le1$. Insert $\varphi=|\sum_xz_x e^{ix\eta}|^2$, whose Haar integral is $\sum_x|z_x|^2$. Since $B^{(k)}$ kills the invariant projection, layer-cake integration as in (33) bounds its numerator by $Ck^{-1}\sum_x |z_x|^2+e^{-k}\|\Phi_z\|^2$. The equal-time Gram lower bound from the conditional even-or-odd edge argument of (23) passes directly through the four-cubes for any fixed finite list of coefficients. It bounds the denominator below by $c\sum_x|z_x|^2$ in the oscillatory case and by $c(1+\beta)^{-2}\sum_x|z_x|^2$ in the fundamental case. This proves (36), including the supremum after the infinite-volume limit.

**PROVED.** At physical separation $a_j k_j\to h>0$, $k_j\to\infty$, (36) tends to zero for the oscillatory fields at all $\beta_j\ge1$, and for the fundamental fields if $(1+\beta_j)^2=o(k_j)$. It therefore excludes these entire translation spans, even with cutoff-dependent coefficients and arbitrarily precise axial momentum selection, as possible sequences attaining $q_0$. They have a fixed transverse plaquette and a single time. The massless free example uses transverse smearing or positive time to select its low-energy sector. A proof for the interacting full algebra has to reach normalized vectors prepared with those operations as well.

## Testing an infrared bootstrap on the full Wilson propagator

**PROVED (a lower bound at all Euclidean frequencies).** For the eight-link reading $h_x$ of (28), the proof of (29) applies to finite linear combinations of its translates in all *four* Euclidean directions. Colour the centers in the periodic spacetime lattice at cyclic sup distance greater than eight with at most $17^4$ colours. Select the same two spatial edges at each chosen spacetime center. Distinct times can read the same selected edge only if the times coincide, and no action plaquette contains two of the selected links. The conditional pair projection for $x$ again kills every other translate. Thus their Euclidean Gram form is bounded below by $c_0^2 17^{-4}$ times the squared coefficient norm. Passing to the periodic limit gives a lower bound by this constant times four-dimensional Haar measure for the full Euclidean Fourier measure. Indeed its integral against the squared modulus of any trigonometric polynomial has that lower bound, and square roots of nonnegative continuous tests can be uniformly approximated by trigonometric polynomials. Subtracting the invariant atom at four-momentum zero preserves the same domination, since Haar measure has no atom there. Together with (34), the positive-energy Fourier density of this actual neutral Wilson reading is bounded below by a positive constant and above by a constant times the massless lattice Green symbol, for Haar-almost every four-momentum.

**PROVED (even a bounded real-frequency upper bound is insufficient).** In the massless singlet comparison (24), impose the *full* spatial sum $q=P-p$ on the momentum torus. The time-summed density at $p_0=0$ is proportional to
\[
 \int \frac{b(p)b(P-p)}{\sinh\omega(p)\sinh\omega(P-p)}
                  \coth\!\left(\frac{\omega(p)+\omega(P-p)}2\right)dp .
\]
On the compact dispersion range $b(p)/\sinh\omega(p)\le C\omega(p)$, since $b(p)\le2(\cosh\omega(p)-1)$. With $u=\omega(p),v=\omega(P-p)$ the integrand is bounded by $Cuv[1+(u+v)^{-1}]$, uniformly even as $u+v\downarrow0$. This bounds the spatial density uniformly in $P$ at $p_0=0$ and hence at every $p_0$ by the positive temporal kernel. For a lower bound, restrict the transverse $p$ so that both $b(p)$ and $b(P-p)$ exceed a small fixed constant. Each individual good set occupies more than three quarters of the transverse torus for a sufficiently small choice of constant. Their intersection has measure at least one half for every $P$. On that set the energies lie in a compact subset of $(0,\infty)$, so the Fourier kernel $\sinh(u+v)/(\cosh(u+v)-\cos p_0)$ and the remaining factors in (24) have positive uniform lower bounds. The real-frequency density is bounded above and below, although the positive-energy support reaches zero. In particular a bound by $C/(m_{\rm test}^2+\sum_{i=0}^3 4\sin^2(P_i/2))$ on the real torus with a fixed $m_{\rm test}>0$ could hold for this gapless local scalar. Inserting a positive constant into the real upper envelope of (34) would still leave the spectral question open.

**OPEN.** At one fixed physical separation $h$, the unresolved estimate is a common $q<e^{-\pi/2}/2$ for the ratios (12) on the full matched local algebra, equivalently a strictly smaller exponential base in (18). The estimates above establish a quantitative deficit for concrete classes of Wilson states and control positive spectral weight down to arbitrarily small lattice energies. No step excludes that weight on a fixed positive physical interval for a total set of continuum states. The construction and full observable matching of the nontrivial Jaffe–Witten theory also remain open here.

RESULT — Row 1204. PROVED by hand in this note are the sharp relativistic mass test (1), the strict strip bound (8), the Wilson contact and infrared estimates (21), (26), (32)–(35), and the exclusion of axial plaquette packets in (36). OPEN are the strict estimate on the full matched continuum Hilbert space and the four-dimensional $SU(2)$ Yang–Mills construction with a Jaffe–Witten mass gap. This is author research with no independent check or status grant.
