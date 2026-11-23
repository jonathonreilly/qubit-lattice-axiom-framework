# Repo search

Row 1438 at `14c7f73bf003`. The proposed SU(2) factor exists. Extracting it preserves the full neutral transfer spectrum and produces a positive residual that violates reflection positivity through a kept slice.

I searched `origin/main` (`8b11ae2bb`), `pr/10114` (`f76f6c649`), `pr/10133` (`89faef229`), `pr/10134` (`1e70c7211`) and `pr/10141` (`c73ad7b17`). `(M-neutral)`, `(N-phys)` and neutral transfer kernel/thermal seed returned no target. The broader rank-one search hit only the fixed-plane weight on a $4\times2$ moving-record torus (`docs/ADMISSIBILITY_RULE_MOVING_RECORDS_AT_THE_NEUTRAL_SCALE_HAVE_NO_LONG_RANGE_ORDER_AT_LOW_DENSITY_AND_LONG_RANGE_ORDER_AT_LARGE_BETA_AND_HIGH_DENSITY_BOUNDED_THEOREM_NOTE_2026-09-26.md:69`). Method terms included `Haar commutator`, `commutator noise`, `invertible observation/emission kernel`, `star convolution`, site reflection with deconvolution, a contact atom at zero transfer eigenvalue, and an inverse transfer moment of a Wilson plaquette. No matching Wilson residual theorem appeared. The task-specific prior file is absent. The registry has no corresponding owner under the target or method terms. [November 8 search, §11](prior/repo-search-2026-11-08.md)

- On PRs 10114 and 10133, `ym4d-existence/EXISTENCE.md:2472–2476` and its session snapshots interpret a fit as fresh BCH noise of variance $O(\sigma^4)$ in a noisy contour average. This is the prior physical idea. On main, `research/mass-gap/library/gap-os-equiv.md:257` uses the two reflected moment matrices on $c_n(t)=r^{|t|}(1-|t|/n)_+$, with negative site and link minors $-r^2/n^2$ and $-r^4/n^2$. We use its moment test on an actual Wilson observation and retain the common-time variance. [Earlier moment test](gap-os-equiv.md)
- On main, `research/mass-gap/library/gap-phys-seed.md`, Theorem ZD-c, identifies the periodic seed, given its inputs, with bounded doubling defect and unbounded scaled periodic gap on the admissible dyadic grid. On PRs 10114 and 10133, `ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md` (11) bounds one centered plaquette matrix element below by $v_N^2e^{-68\beta}/(1+v_N/r_f(\beta)^4)$. Grok's `MASS_GAP_CROSSOVER_REDUCTION.md` on PR 10133 still needs (CW), (MG2) and (H6). PR 10134's `library/mass-gap-interface.md:27` requires a common hierarchy and common or dense observables. The present target is an upper bound on the entire neutral trace.

## Plan and checkpoint

1. Check the task-specific prior, lane rules, index, repository refs and registry for the exact target and earlier proofs.
2. Write a candidate mechanism and its first lemma from the target and published inputs before opening FINISH rows after 1378.
3. Compare that candidate with all specified mechanism and exact-block passes, their checks, and the five direction filters. Discard equivalent claims.
4. Prove the surviving first lemma or a quantified exclusion, identify the implications for the mass-gap chain, and give two decisive follow-up rows.

## Phase 1. Candidate fixed before the later directions

**OPEN target.** Fix one admissible physical side $L$ on the specified four-dimensional Wilson SU(2) trajectory. At late cutoffs $n_j=L/a_j$ is divisible by four, $n_j\ge 2^{70}$, and $\beta_0\le\beta_j\le B_0\log n_j$. In zero spatial twist let $P_0$ project to the trivial character of the eight electric centre translations. With multiplicity, $s(t)=\sum_{i>0}(\lambda_i/\lambda_0)^t$ in that sector. The desired inequality is $s(2w_j)\le 4/21$ at $w_j=\lfloor n_j/1024\rfloor$ for every late cutoff. The underlying Jaffe–Witten conclusion excludes a fixed positive energy interval above the vacuum in the matched continuum theory. Row 1161's $c n^3$ count rules out a test at one common time on arbitrarily many volumes at fixed cutoff. [Row 1367](gap-seed-astra62.md)

**Published inputs.** Sussman and Alpoge with Claude and Codex, outline at `31a47c543775`, lines 588–599 and 31871–31882, give the counterexample with spectral density $E e^{-E}$. Lines 3712–3720 explain the loss at zero energy. GL3, lines 2195–2232, diagonalizes one-bond central convolution by spin. B3, lines 3986–4004, asks for the actual lattice trace and its nonlinear error in the running coupling. CA-I 2699–2713 states $H\ge0$ in the curvature sector and leaves the gap open. CA-II 60089–60102, 60120–60128 passes lattice positivity to limits at disjoint supports. CA-III 108223–108251 uses a mass gap as one possible input to a reflected-decay estimate. Bałaban's CMP 122b Theorem 1 concerns UV stability with the running couplings in its weak window, as quoted in the lane (unchecked against the paper). Osterwalder–Seiler and Lüscher supply the transfer method rebuilt in row 667. The outline states “Its support reaches zero” for its polynomially decaying example at lines 31871–31882. [Index](sa-index/README.md) · [Outstanding statements](sa-index/obligations.md) · [Bałaban source record, §3](lit-balaban.md) · [Wilson transfer, §§3–8](gap-transfer.md)

**GUIDE.** A small noncommuting rotation shared by several coarse links can act on the colour carried jointly by those links. Two colour angles of order $\beta^{-1/2}$ give a group commutator of order $\beta^{-1}$ and a quadratic response of order $\beta^{-2}$. This is the scale at which a bounded increment could appear in an inverse-width coupling of order $\beta$. The earlier soft-route BCH observation motivates testing the *joint* colour rotation. The test must say what the rotation does to a physical transfer eigenvalue.

**First lemma proposed.** Keep even time slices, and at every even spatial vertex rotate all three outgoing spatial links by the *same* left multiplier. Use the first fine bond for the aligned length-two coarse links. Fix the multiplier law before computing a Wilson expectation. Each kick is $[A,B]$, with independent uniform axes and a fixed common angle $r$ satisfying $\sin^2 r=1/[72(1+\beta)]$. Take a geometric number of independent kicks with probabilities $(1-p)p^k$, $p=1/4$, independently on distinct stars. The proposed factorization represents the true Wilson law on kept slices as this observation of a positive joint residual, with fundamental coefficient $1/(1+4\sin^4r/9)$. The same group word in compact U(1) is identically the identity. If this lemma survives the prior comparison, test whether successive independent time-slice observations give a strict spectral gain after the residual is retained. A candidate failure would be an isometry of the two reflection-positive Hilbert spaces commuting with time translation, in which case the entire neutral heat trace would agree.

The phase-one checkpoint recorded this proposal before FINISH rows after 1378 or their research notes were opened. The first lemma and spectral test were both open at that checkpoint.

## Phase 2. Prior mechanisms and the decision

FINISH 1438 gives the comparison rows explicitly. Its text has no further “Repo prior work” entry. The closest additional precedent is row 1132, highlighted by row 1386. **Frobenius's Haar commutator and a Wilson extraction have already been used here.** In row 1132 (A), a fixed positive branch of the *transition* at physical time ends in independent Haar commutators on all links in Moser coordinates, with a Haar-stationary entrance. Its conclusion is an operator-norm contraction. Row 1135 §3 gets a positive deconvolution of the original output conditional for every box at $\beta\le10^{-6}$, with the entrance marginal specified there. We use a joint observation of the entire history, independent between observation times, with one common rotation on three links. A hidden history and its observation need not have the same one-step transition. The distinction is tested below on the Wilson law itself. [Row 1132](gap-council-op-astra.md) · [Row 1135](gap-slab-a-astra.md) · [Row 1386, §2.3](gap-mech-direction2-fable.md)

| Pass and check | Existing calculation and its bearing here |
|---|---|
| 1380/1381, 1386/1387 | The two lab-frame corner costs close C1. The Haar-commutator multiplier in 1386 is already credited above. Check 1387 corrects the band inventory at line 86. Row 1141 (2) bounds the adjoint Laplacian on growing boxes, and row 1283 (7) carries its roughness estimate into the neutral trace at the test time. A bounded local kick is compatible with these facts. [1381](gap-mech-direction-check-astra62.md) · [1387](gap-mech-direction2-check-astra62.md) |
| 1390/1393, 1396/1401 | Convolution after bond moving and geometric Wilson refinement have different endpoints. The anisotropic neutral comparison needs spatial transport, entry and a coupling increment. Taking every second full Wilson slice is exact. It allows a test of what the proposed noise contributes at *the same* physical time. [1393](gap-dim-carry-check-astra62.md) · [1401](gap-time-coarsen-check-astra62.md) |
| 1402/1407, 1409/1411 | The two-cover ratio can rewrite the trace test. The grid-class and C7 conclusions needed correction. For the two-link submersion and the stated metrics the conditional score varies along a regular fibre, also after quotient, which excludes exact Lott transport. The stochastic rotations here have an algebraic inverse on tests and use neither replica covers nor horizontal transport. [1407](gap-band-fresh-check-astra62.md) · [1411](gap-c7-submersion-check-opus.md) |
| 1418/1420, 1421/1423, 1424/1426 | The raw tensor rank and scalar-radius obstructions leave signed contractions. Reflection-invariant one-link reductions commute on the specified sectors, as do the interior channels with at most one cycle per component. In the two-square test the single-fundamental connected routing cancels by an axis swap. None takes the inverse of an observation on the Wilson time history. [1420](gap-rg-step-sizing-check-opus.md) · [1423](gap-rg-signed-inclusion-check-opus.md) · [1426](gap-rg-two-cycle-check-opus.md) |
| 1425/1429, 1430/1431, 1432/1433, 1435/1437 | The two-strand ring has the wrong sign for its proposed decrement. The crossed reading evaluates the same traceless moment, and another reference reverses its decrement. The Lean work verifies finite interval, census, recoupling and sphere identities under its stated analytic identifications. Equations (2) and (4) instead test the complete joint probability law for a kernel fixed before evaluation. [1429](gap-rg-ring-sign-check-opus.md) · [1431](gap-rg-response-search-check-opus.md) · [1433](gap-rg-ring-lean-replay-check-opus.md) · [1437](gap-rg-haar-finite-lean-check-opus.md) |
| 1434/1436 | The straight-product square has a factorial spin lower tail, excluding an independent heat factor of positive time. Extracting a positive character term also leaves both signs arbitrarily high in the residual character series. Our star law has an atom at identity and ties adjacent edge multipliers together. Its inverse is a difference of two probability operators. Neither prior obstruction settles its positivity or the effect on the neutral spectrum. [1434](gap-mech-candidate-astra62.md) · [1436](gap-mech-candidate-check-opus.md) |

**Decision.** Retain the proposed first lemma for proof. The broader idea of using a commutator as a colour mixer belongs to the prior work. The specific test left open by that comparison is whether an exact, nontrivial slice factor with a positive residual can carry a *change of transfer spectrum*. Reflection through a kept time slice gives an independent test. In the full reversible Markov chain, subtracting the one-step conditional prediction from the future observable gives a null vector in the reflected form. A noisy observation at the shared slice changes the diagonal term. The time-polynomial test below also works after spatial projection. The outline proves positivity on a Wilson site cut by conditioning on its bonds, lines 2811–2818. [Index, chunk 03](sa-index/chunk-03.md)

## Phase 3. An exact positive star factor

**PROVED by hand, author only.** Work on the periodic four-dimensional Wilson lattice with spatial cube $n^3$, $4\mid n$, $n\ge4$, even time period at least four, and $\beta>0$. Zero spatial twist suffices. Count each geometric plaquette once, with either orientation. Its weight is proportional to $\exp(\beta q(U_p))$, with $q(g)=\operatorname{Re}g=\tfrac12\operatorname{tr}g$ in unit quaternion coordinates. At even times take the stars rooted at vertices with three even spatial coordinates. Each star consists of its three positively oriented outgoing spatial bonds. Keep either the full even-time spatial slice or the straight spatial length-two products rooted at even vertices on that slice. All randomness below is independent of the residual field. The choices of bonds, kernel, $p$ and $r$ are fixed by this prescription.

Write $a=\sin^2r=1/[72(1+\beta)]$, with $0<r<\pi/2$, and $p=1/4$. Draw $A=\cos r+u\sin r$ and $B=\cos r+v\sin r$ for independent uniform $u,v\in S^2$ of imaginary quaternions. Put $H=ABA^{-1}B^{-1}$. Conjugation by $A$ rotates $v$ about $u$ through $2r$. Quaternion multiplication then gives

$$
 q(H)=\cos^2 r+\sin^2r\,(\operatorname{Ad}_A v)\cdot v
     =1-2a^2(1-z^2),\qquad z=u\cdot v.                                      \tag{1}
$$

Here $z$ is uniform on $[-1,1]$, by the area element of $S^2$ about $u$. The law of $H$ is invariant under conjugation, and interchanging $A,B$ gives its inverse law. In particular $|H-1|\le2a$ in Euclidean quaternion norm. Let $Q$ act on a star by simultaneous left multiplication by $H$, averaged over its law. Use the same letter for its action on densities and tests, since Haar invariance and inverse symmetry make it self-adjoint for product Haar. Define

$$
 K=(1-p)\sum_{k=0}^\infty p^k Q^k, \qquad D=K^{-1}=\frac{I-pQ}{1-p}.          \tag{2}
$$

The series converges in operator norm on bounded functions and in $L^1$ on densities since $Q$ is a contraction there. Multiplication of the geometric series gives both inverse identities. $K$ is a probability kernel. Its fundamental multiplier on **one** affected bond is

$$
 \kappa=\frac{1-p}{1-p\,\mathbb E q(H)}=\frac{1}{1+4a^2/9},                    \tag{3}
$$

since the expected imaginary part vanishes by symmetry and $\mathbb E z^2=1/3$. A pair of outgoing links receives the *same* multiplier, so its relative product $U_1^{-1}U_2$ is fixed exactly. Thus the joint channel differs even locally from an independent multiplier on each link. The atom of mass at least $1-p$ also distinguishes it from positive-time heat smoothing.

**Positivity with all plaquettes retained.** Fix every fine link outside the chosen stars, before integrating any link. An elementary spatial plaquette has at most one all-even vertex. A temporal plaquette touches a chosen spatial bond on at most one of its two time slices. Thus no plaquette reads two distinct chosen stars. Given the exterior, the unnormalized positive weight is an exterior factor times $\prod_x f_x$, where $f_x$ contains each incident plaquette once, including those using two bonds in the same star. Multiplying the three bonds by $H$ changes each normalized plaquette trace by at most $|H-1|$ per occurrence, by telescoping the ordered product and using invariance of quaternion norm under unit factors and inversion. There are at most $3\cdot 6=18$ occurrences. Consequently

$$
 Q f_x\le e^{36\beta a} f_x\le e^{1/2}f_x,
 \qquad D f_x\ge \frac{1-p e^{1/2}}{1-p} f_x>0 .                              \tag{4}
$$

The elementary bound $e^{1/2}<2$ follows by comparison of its power series with the geometric series. Apply $D$ at every chosen star to the full Wilson density. At fixed exterior the result is the same exterior factor times $\prod_x D f_x$. Equation (4) proves pointwise positivity of the complete residual density, including interactions between bonds of the same star. Individual coefficients in its character expansion or log density can have either sign as far as this argument goes. The integral is unchanged because $D1=1$ and $D$ preserves Haar mass. Applying the product of the probability kernels $K$ recovers the complete original density. This is stronger than positivity of each separate one-star marginal.

Projecting to even-time full spatial slices gives the announced factorization. For the coarse path projection a length-two spatial product is $V_i(x)=U_i(x)U_i(x+e_i)$. Its first factor rotates and the second stays fixed, so at each coarse vertex the three $V_i(x)$ are rotated together. The array of observation kernels commutes with the vertex gauge action by conjugation invariance and with electric centre translations by centrality of the signs. It is translation-invariant in retained time. The residual at fixed volume has a stationary infinite-time limit on the retained fields. Indeed for any continuous cylinder test its residual expectation equals the periodic Wilson expectation of the product of $D$ on that test. Only its finitely many slices and stars enter, and the resulting function is another bounded continuous cylinder test. The finite-box Wilson cylinder limit exists by the positive simple vacuum and trace convergence of row 667. Limits of the positive residual probabilities on the compact spatial state space are consistent, hence give the claimed process. The same construction works with full retained slices before projecting. [Wilson vacuum and cylinder law, §§4, 6, 8](gap-transfer.md)

**What (3) measures.** For a spatial coarse square the star at the starting corner conjugates the entire trace and drops out. The other two stars with outgoing bonds on the square act once each. Their independent averages multiply the residual mean by $\kappa^2$. The opposite corner contributes no kick. The result is exact for each coarse plaquette and each residual field before averaging. The choice in phase 1 fixes this single-slice attenuation. At the very same Wilson coupling, (4) also allows every $0<p<e^{-36\beta a}$ in (2), with a different factor $(1-p)/(1-p+4pa^2/3)$ and a different positive residual. A plaquette attenuation by itself therefore does not select a shift in the Wilson coupling.

## The residual violates reflection positivity through a kept slice

**PROVED by hand.** The exclusion covers spatial projections and observation noise whose conditional covariances vanish beyond a finite time separation. Take a finite Wilson spatial torus, $\beta>0$, and keep spatial observations at any integer time stride $b\ge1$ in its stationary, infinite-time cylinder law. Write $X_t=\pi(U_{bt})$ for any fixed measurable observation $\pi$ of that spatial slice. Let $h(X_t)$ be a bounded real gauge-invariant, electric-centre-neutral observable. The class to be tested consists of stationary residual slice fields $Y_t$ and an observation rule with these properties, all at the same finite cutoff.

1. Given the entire residual history, the mean of $h(X_t)$ is $k(Y_t)$, with the same real function $k$ at every time. Spatial slice fields are fixed under time reflection on its plane.
2. For some finite integer $R\ge0$, the conditional covariance of $h(X_s),h(X_t)$ is zero whenever $|s-t|>R$. Independent emissions on distinct times give $R=0$. The integer $R$ may depend on the box and coupling.
3. The observation adds a genuine variance $v=\mathbb E[\operatorname{Var}(h(X_0)\mid Y)]>0$ on this neutral observable.

**Conclusion.** No such residual has site reflection positivity for the closed half $t\ge0$. If the observation is centre-equivariant and $k$ is neutral, a neutral test witnesses the failure. In particular the residual cannot itself be a Wilson law at any positive coarse coupling, or the slice law of any reversible stationary Markov dynamics for which the reflection fixes its time-zero state. For the latter assertion conditioning on that state makes the two half-paths independent mirror copies, giving a squared conditional mean. Projecting a site-reflection-positive law to spatial slice observables preserves its positivity.

With product Haar on one fine slice let $T$ be the physical Wilson transfer, $\Omega>0$ its normalized vacuum, and $S=T/\lambda_0$. On the gauge-invariant space $T=M C_E M$, where $M$ is the strictly positive spatial half-weight and $C_E$ is the product of the one-bond electric convolutions. Gauge averaging commutes with both and is the identity on this space. GL3 gives a strictly positive coefficient at every spin for $\beta>0$. The finite product $C_E$ and then $T$ have trivial kernel on this space, including its neutral sector. $S$ is a positive self-adjoint contraction. Its eigenvalues can approach zero. Its spectral projection **at** zero is zero. The vacuum eigenvalue of $S$ is one. [GL3 in chunk 02](sa-index/chunk-02.md) · [Transfer construction](gap-transfer.md)

Put $d=R+1$ and let $u=(h\circ\pi)\Omega$ on a single fine slice. The Wilson two-point function is $\langle u,S^{b|t-s|}u\rangle$. For integer $m\ge1$ set $c_i=(-1)^i\binom mi$ and form the residual half-space test $G_m=\sum_{i=0}^m c_i k(Y_{di})$. In the reflected product, every pair of times $-di,dj$ has separation greater than $R$ except $i=j=0$. For all those distinct-time pairs the observation rule gives the Wilson two-point function exactly. At the common time zero it gives $\mathbb E k^2=\mathbb E h^2-v$. Therefore, writing $(\theta Y)_t=Y_{-t}$,

$$
 \mathbb E_Y[(\theta G_m)G_m]
   =\sum_{i,j=0}^m c_i c_j\langle u,S^{bd(i+j)}u\rangle-v
   =\|(I-S^{bd})^m u\|^2-v.                                                    \tag{5}
$$

For each transfer eigenvalue $0<x\le1$, $(1-x^{bd})^{2m}$ tends to zero and lies in $[0,1]$. Bounded convergence against the spectral measure of $u$ gives limit $-v$. Some finite $m$ already makes (5) less than $-v/2$. This proof uses just the two-point moments. It applies even if the kept spatial variables do not determine a fine slice, and it imposes no Markov assumption on the residual. In spectral terms a fresh equal-time variance would require an atom of at least $v$ at transfer eigenvalue zero if the residual obeyed site positivity. Innovations with conditional covariances at arbitrarily large lags can also contribute to the off-diagonal terms in (5).

**A Wilson square witnesses a strictly positive loss.** Take for $h$ the normalized trace of an elementary *coarse* spatial plaquette on the length-two grid. Its four coarse edges are distinct for $n\ge4$. At one of its two mixed corners exactly one of its two incident bonds starts there. Condition on the whole residual and the other multipliers. By cyclicity and inversion symmetry the remaining random trace has the form $q(HD')$ on the branch of exactly one kick, for a fixed unit quaternion $D'$. That branch has probability $(1-p)p=3/16$. For a single kick, conjugation invariance gives zero vector mean, zero covariance of scalar and vector parts and isotropic vector second moment. If $c=q(D')$, its conditional variance is

$$
 c^2\operatorname{Var}(q(H))+(1-c^2)\,\mathbb E|\operatorname{Im}H|^2/3.
$$

From (1) and $\mathbb E z^4=1/5$, these two coefficients are $16a^4/45$ and $8a^2/9-32a^4/45$. The latter is at least the former since $a^2\le5/6$. The law of total variance first over the branch and then over the other multipliers gives

$$
                 v\ \ge\ (3/16)(16a^4/45)=a^4/15.                             \tag{6}
$$

The centre flips fix this contractible trace. Its conditional mean at a retained slice is $k=\kappa^2 h$ on the coarse square of the residual. Thus the positive residual from (4) has a neutral test with **closed-site** reflected form below $-a^4/30$. For each fixed spatial box and coupling, the same finite test is negative on all sufficiently long periodic time cylinders, by cylinder convergence. This statement holds both if all fine spatial links are kept and if only the length-two coarse links are kept. All other links and stars are integrated in their joint law. The size of the test function $G_m$ can grow with $m$.

### A finite test uniform on a coupling interval

**PROVED by hand.** For the straight coarse square, the witness length in (5) for independent times can be chosen uniformly in the spatial volume and in any fixed $J=[\beta_-,\beta_+]\subset(0,\infty)$, in particular the block-line interval $[2,513/256]$. This also gives an error floor for a site-positive approximate representation. We give the constants because trivial kernel at each cutoff alone has no uniform consequence.

Use the unshifted electric weight $e^{\beta q(g)}$ throughout this estimate. Sussman and Alpoge’s GL4–GL7 (outline 2233–2312) give the neighbouring-spin ratios and the finite-block smooth conjugation $C_A^{-1}M_h C_A$. We use their finite-band argument to obtain an explicit column bound and a volume-independent inverse moment against the Wilson vacuum. Its convolution eigenvalue $c_n$ in the representation of dimension $n+1$ is $2I_{n+1}(\beta)/\beta$ by GL3. The factorial series gives

$$
 l_n=\frac{(\beta_-/2)^n}{(n+1)!}\ \le c_n\le\ u_n=e^{\beta_+^2/4}\frac{(\beta_+/2)^n}{(n+1)!} .
$$

Let $A$ consist of the $\ell=8$ distinct fine edges of the coarse square. Define

$$
 B_J=\sum_{n\ge0}(n+1)u_n\sum_{k\in\{n-1,n+1\},\ k\ge0} l_k^{-1/2},
 \qquad C_J=e^{\ell\beta_+} B_J^{2\ell}.                                      \tag{7}
$$

The ratio of successive terms of each of the two series tends to zero, by the factorial formulas. We claim $\langle h\Omega,S^{-1}h\Omega\rangle\le C_J$ as an inverse quadratic form. Here and below $h$ is pulled back to its eight fine edges. To see the locality of this bound, let $c_A(\cdot,y)$ be the product convolution kernel on those edges. Its projection on degrees $(n_e)_{e\in A}$ has $L^2$ norm $\prod_e (n_e+1)c_{n_e}$, since the Haar character on each factor has norm one. Multiplication by $h$ has norm at most one. On each edge it moves $n_e$ only to $n_e\pm1$, by tensoring with the fundamental or its equivalent dual. Project on every possible output degree and apply the triangle inequality. The definition of $B_J$ now gives, uniformly in $y$,

$$
 \|C_A^{-1/2}(h\,c_A(\cdot,y))\|_2\le B_J^\ell .                               \tag{8}
$$

Indeed each output projection costs at most the norm of its input times $\prod_e c_{k_e}^{-1/2}$. Summing first over those neighbours and then the input degrees gives (7). Absolute convergence justifies applying the closed inverse on these columns. The squared operator $(C_A^{-1/2}h C_A)^*(C_A^{-1/2}h C_A)$, with $h$ denoting multiplication, has kernel equal to the inner products of the columns in (8). Its absolute value is bounded by $B_J^{2\ell}\le C_J c_A(y,z)$ since $c_A(y,z)\ge e^{-\ell\beta_+}$.

For the full box write $\Phi=M\Omega>0$ and $\lambda=\lambda_0$, in this unshifted normalization. Then $M^{-1}\Omega=C_E\Phi/\lambda$. The inverse quadratic form of $T=M C_E M$ at $f$ is $\|C_E^{-1/2}M^{-1}f\|^2$. To see this, set $z=Mv$ in the variational supremum of $2\operatorname{Re}\langle f,v\rangle-\langle v,Tv\rangle$. At fixed box $M$ and $M^{-1}$ are bounded. On invariant functions this calculation also holds on the full space, since the operators commute with gauge averaging. Hence

$$
 \langle h\Omega,S^{-1}h\Omega\rangle
 =\lambda^{-1}\|C_E^{-1/2} h C_E\Phi\|^2
 \le \lambda^{-1} C_J\langle\Phi,C_E\Phi\rangle=C_J .                         \tag{9}
$$

For the inequality, tensor the column inner-product kernel above with the positive kernel $C_{E\setminus A}$ on the untouched edges. This is the squared operator on the right of the equality, by the tensor product of the electric convolutions. Its integral against the positive pair $\Phi(y)\Phi(z)$ is bounded by the integral with kernel $C_J C_E(y,z)$. Thus the denominator $\lambda$ cancels exactly even in large volume.

For $b=2$, $R=0$, $\max_{[0,1]} x(1-x^2)^{2m}\le(4m+1)^{-1/2}$ by differentiation. Equation (9) bounds the squared Wilson norm in (5) by $C_J/\sqrt{4m+1}$. Take

$$
 v_J=\frac{1}{15[72(1+\beta_+)]^4},\qquad m_J=1+\left\lceil(C_J/v_J)^2\right\rceil .
$$

The Wilson norm squared in (5) is then less than $v_J/2$. For any proposed stationary site-reflection-positive residual with the specified star emissions, let $\varepsilon$ bound the absolute errors of its observed, uncentred coarse-square two-point moments relative to Wilson at lags $0,1,\ldots,2m_J$ in retained units. Equation (6) works under *every* residual law. The sum of the absolute coefficients $|c_i c_j|$ in (5) is $4^{m_J}$. Its nonnegative residual form therefore forces

$$
                        \varepsilon\ \ge\ \frac{v_J}{2\,4^{m_J}} .               \tag{10}
$$

This is a volume-independent positive exclusion radius for this finite list of moments. The constants come from absolute character bounds and give no practical band precision or estimate for a coupling that grows beyond $J$.

## What the factor carries in the neutral transfer

**PROVED by hand.** Reflection *between* retained times 0 and 1 has disjoint halves. For bounded continuous cylinder tests $F,G$ on times $t\ge1$, write $\mathcal K$ for conditional averaging of all their star multipliers. It acts jointly on all occurrences in one slice and independently on distinct slices. With $\mu$ the observed Wilson law, $\nu$ its residual from (4), and $(\vartheta Y)_t=Y_{1-t}$, independence gives

$$
 \mathbb E_\mu[(\vartheta\overline F)G]
    =\mathbb E_\nu[(\vartheta\overline{\mathcal K F})(\mathcal K G)].           \tag{11}
$$

The product of the signed inverses (2) is an inverse on each finite cylinder, preserves its time support and commutes with time shifts. Thus every residual cylinder has a preimage. Wilson link positivity passes to the residual by (11), and $F\mapsto\mathcal K F$ induces a unitary between the two link-reflection Hilbert spaces after quotient and completion. It preserves the vacuum and the electric-centre action and intertwines translation by one retained step. This proof works for any time-homogeneous, slice-by-slice probability channel with an inverse on these cylinder tests and the stated symmetries. It works for a finite composition of such channels whenever the composition has these properties. No uniform bound on the inverse norm as the volume increases is needed for this finite-box identity.

On **full retained slices** this unitary identifies the whole nonzero neutral transfer spectrum, with multiplicities. Indeed the stationary ground-state chain between two retained slices has transition $f\mapsto \Omega^{-1}S^2(\Omega f)$. Condition a future cylinder $F$ on its first retained slice to get $f_F$. On gauge-invariant cylinders the two halves in the Wilson link form have inner product $\langle\Omega f_F,S^2\Omega f_G\rangle$ by the stationary reversible Markov property. Hence $F\mapsto S(\Omega f_F)$ realizes that form in the physical Hilbert space and sends one retained time shift to $S^2$. Single-slice functions times $\Omega$ are dense there, also after electric-centre averaging, and $S$ has dense range by injectivity. Thus if $S_\nu$ is the normalized residual transfer for the link reflection, for every positive integer $w$,

$$
             \operatorname{Tr}_{+,\nu} S_\nu^w-1
                  =\operatorname{Tr}_+ S^{2w}-1=s(2w).                       \tag{12}
$$

On the spatial path projection (11) gives isospectrality on the Hilbert space generated by those observations. Identifying that space with the entire fine neutral sector would require a totality argument. Equation (5), including its strict negative sign on the projected square, required no such identification. The link form in (11) has no shared time-zero sample. Its equality is consistent with the negative diagonal contribution on the closed site cut in (5).

**Equivalent is not progress.** The local factorization (1)–(4) has a direct Wilson proof for every positive coupling. To separate its content from the seed and (W), tensor the Wilson family with the previously constructed independent line-spin family of row 1135 §6 (the four directional species in its comparison, with physical parameter $m_0>0$). Let the electric centre act trivially on those spins and leave their observations exact. The star factor and its square coefficient survive verbatim. The prior transfer count supplies at least $4n^3$ neutral excitations with ratio $e^{-m_0 a_j}$ from single lines. Their contribution at $2w_j$ diverges for every fixed $L$ as $j\to\infty$. The prior symmetric-torus excess is at least $4n^3\log(1+4e^{-m_0 L})$. Excesses add under products, and the Wilson excess is nonnegative by $F((2n)^4)\le16F(n^4)$ and the pressure limit. Thus the bounded-excess clause of (W) also fails. The additional line spins make this a comparison outside pure Wilson theory. Conversely, at any fixed positive bare $\beta<2/9$ with assigned spacings tending to zero, DOB gives the seed for all sufficiently late cubes while (5) still excludes a site-positive star residual. The assigned trajectory serves only for separation. Asking instead for the residual side of (12) to be small is **exactly (M-neutral)**. [Line-spin model and pressure](gap-slab-a-astra.md) · [Quadrupling defect](gap-phys-seed.md) · [DOB separation, check 1436 item 7](gap-mech-candidate-check-opus.md)

### The five tests and the mass-gap chain

| Test from 1386 §4.5 | Outcome for the proposed carry |
|---|---|
| (t1) Compact U(1) | In (1) the group word itself becomes the identity for every pair and every character. No traceless subtraction is involved. SU(2) has a genuine positive conditional variance (6), but the factor supplies zero spectral improvement by (12). The group distinction at one star does not yield a dynamical four-dimensional gain. |
| (t2) Five-dimensional SU(2) | With four outgoing spatial links and eight incident plaquettes per link, (4) costs at most $64\beta a<1$. The same $p=1/4$ works since $p e<1$. The same mixed corner has (6). Both (5) and (11) apply in five dimensions as well. |
| (t3) SU(3) | Use independent Haar conjugates of $\mathrm{diag}(e^{ir},e^{-ir},1)$. The commuting pair and a noncommuting pair in its upper SU(2) block give different real normalized traces of the commutator, and neighborhoods of these pairs have positive probability. For $A,B$ in this conjugacy class, $\lVert[A,B]-I\rVert_{\rm op}\le 2\lVert A-I\rVert_{\rm op}\lVert B-I\rVert_{\rm op}=8\sin^2(r/2)\le4a$. Thus the four-dimensional star bound costs at most $72\beta a<1$. Its residual one-slice marginal gives positive measure to every nonempty open set. On a single slice the pointwise lower bound in (4) with $e$ in place of $e^{1/2}$ gives a fixed positive multiple of the Wilson marginal at each fixed box, before and after the cylinder limit. The square has positive conditional variance on a neighborhood of the identity residual, taking the other stars' zero-kick branches. For injectivity of the SU(3) electric convolution, expand $e^{\beta\operatorname{Re}\operatorname{tr}(g)/3}$ in defining and dual characters, with positive coefficients. Every irrep occurs in a tensor word since polynomials in matrix entries and conjugates are dense by Stone–Weierstrass and inequivalent matrix coefficients are orthogonal. Thus (5) excludes the same type of site-positive residual. |
| (t4) Fixed lattice, $\beta\to\infty$ | The factorization persists at every finite $\beta$. Formula (3) has $1-\kappa=O(\beta^{-2})$ and (6) gives a floor of order $(1+\beta)^{-4}$. Equation (12) gives exactly zero transfer change already at finite $\beta$. This is compatible with collapse of fixed-index neutral energy levels in the prior fixed-cube test. [Row 1215, (5)](gap-solve23-astra62.md) |
| (t5) Equivalence | The product example separates the local, positive factor from all three target formulations. The full-slice residual trace is the original target by (12). A fresh proof about interactions in an effective law would be an additional input. |

**RESULT — row 1438.** An exact, positive, spatially correlated SU(2) commutator factor exists in the Wilson block law. Any same-slice observation of the specified class with positive neutral conditional variance and finite temporal covariance range rules out a residual with reflection positivity through that slice. For the proposed invertible channel the neutral link-transfer improvement at matched time is exactly zero. The finite-window obstruction (10) also applies to approximate histories on a fixed compact coupling interval. This closes the stated class of carries. A separate estimate on the effective interactions could still bound the residual. Transitions in which a fluctuation changes later states, and observations whose conditional mean reads across the reflection plane, also remain open. The one-cube Wilson seed remains open. In the checked chain the squared relative rank-one distance is $s(2w)/(1+s(2w))$. Tolerance $2/5$ gives $s(2w)\le4/21$ and the neutral seed at $u=\max(3,2w)\le n/512$ on late cubes. Conversely the neutral seed $s(u)\le1/2$ gives $s(3u)\le1/8$, with the reverse time cap handled as in rows 1355 and 1359. Either flux branch then gives the physical neutral-gap and thermal control. The continuum gap conclusion requires the matched data (P1)–(P4), (H2) and totality (TOT). No step of that chain is refuted. All new proofs here are written hand arguments by Codex, without an independent check, Lean computation or generated code. This research note grants no status. [Rows 1356/1359](gap-mini-mneutral-check-astra.md) · [Rows 1342/1349](gap-seed-audit-check-astra.md)

## Next two rows and their decisive outcomes

1. **Check the exclusion on the projected Wilson square.** Independently reconstruct its diagonal and distinct-time moments, the signed joint inverse in (4), and the volume cancellation in (9). A failure of (9) withdraws the uniform finite witness and approximate radius (10). A failure of the single common-time subtraction in (5) withdraws the site-positivity exclusion. Confirmation retires the stated class even with spatial projection and finite-range temporal noise, while (12) decides the full-slice link-transfer claim separately.
2. **Test one temporal Wilson plaquette across a time cut.** Fix the real normalized trace $q_p$ of one temporal plaquette, sampled in slabs $[2t,2t+1]$. Set $A=T[q_p]/\lambda_0$ and $B=T[q_p^2]/\lambda_0$, using the actual one-step marked Wilson kernels. Time reversal fixes the real trace, so $A$ is self-adjoint. The equal-time moment is $\langle\Omega,B\Omega\rangle$. At lag $k\ge1$ it is $\langle A\Omega,S^{2k-1}A\Omega\rangle$ by insertion in the transfer product. Determine, over $4\mid n$, $n\ge4$, $\beta\in J=[2,513/256]$, whether the following uniform inequality holds, with one admissible counterexample sufficient to refute it.

   $$
   \langle\Omega,B\Omega\rangle-\|S^{-1/2}A\Omega\|^2\ \ge\ v_J .
   $$

   A site-positive residual with independent emissions of variance at least $v_J$ requires this inequality. The observed form for the alternating test in (5) decreases to the left side. Relative to the equal-time term its integral is $-\int_{(0,1]}[1-(1-x^2)^{2m}]\,x^{-1}\,d\mu_{A\Omega}(x)$. An infinite inverse moment counts as failure. A value below $v_J$ excludes that floor for a site-positive residual on this straddling observable. A uniform lower bound would clear one necessary test for a reader that spans the cut. It would still need an exact block map with a signed coupling increment, the compact-U(1) and five-dimensional controls, and a rate. The test reads the actual vacuum with the same two fixed insertions throughout and can be posed before choosing an exterior label or evaluating a spin sum.
