# ST1: Intrinsic stage domains and stage admission

Provenance: Codex (serving variant and effort not exposed), 2026-11-04; Pass 2 of Claude Opus 5.5's `st1-draft.md`, read in full at repository commit `49b01bbdf3b61615c6a7993da238cea62e43f010`. Research text, not an audit; grants no status. Not yet refereed.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, for the graded domains, ambient towers, response substitution and re-expansion used below. Their sources are [SA](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex), [CA-I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex), and [YM3](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM3/YM3_I.tex), all at `31a47c543775`. Credit Tadeusz Balaban for the background and preparatory-stage method. This distillation uses hand arguments only. Text retrieval and citation checks supply no mathematical proof.

## 1. Main statement

**Theorem 1 (ST1*, conditional admission and re-expansion).** Fix a finite four-dimensional periodic lattice, a finite history, its formation records, and constants chosen in Section 4. Assume the imports in Section 3, with all their stated domains. Assume also the following **application hypotheses**, for every transition and every inherited read, uniformly in the cutoff, volume, history length, earlier parameters, stored tiers and switches.

1. The real background has the real admission bounds of Proposition 5. Every real and complex tower datum, before and after substitution, satisfies the averaging hypotheses and the half-tube bound of Lemma 4.
2. Each transition has the compatible read data and positive gaps specified in Definition 4. In particular, target tower maps, lifts, gauge cubes and core addresses are compared as functions, not just as addresses.
3. Every input belongs to the pair, source-cube and pivot domains of DR and AV; every pinned input also belongs to LEV's triple domain, including its turning-cell gauge requirements. Each tower read has the ambient Lipschitz estimate (T) below. The pointwise and core constants $K_{\rm pt},K_{\rm tw},K_{\rm core}$ of Proposition 6 are uniform.
4. The regional shift and, when used, its pinned version satisfy (S) and the endpoint-pillar bounds in Definition 5. The resulting number $a_X$ satisfies $a_X<1/2$. These estimates hold on the entire complex parameter domain, not only at real background points.
5. On the physical locus, the old determining map $M_-$ determines the new map locally: $M_+=F\circ M_-$. The source changes $M_-(U_+)$ into the actual old datum, with the pivot and return factors included. The constraints and regularity satisfy CRIT. Pinned levelling identifies the stored transports as specified in LEV.
6. NL1 and LF1 supply their activities on these domains, with the boundedness, tie, covariance, locality and stored-coordinate properties in Definition 3. Restriction preserves these supplied properties and domains.

For overlapping collars, Lemma OS is the named open input needed to verify these hypotheses there. It is not used to excuse a failure of hypotheses 1–6 at other stages.

Then every carried composition is defined and holomorphic on each fixed-real-factor fibre for
\[
 s\in\mathbb D(Y),\qquad |\lambda|<\varrho_X=(2a_X)^{-1}>1.
 \tag{1}
\]
If $a_X=0$, set $\varrho_X=\infty$. Every scalar read retains at least half its target coefficient gap. Core reads belong to the corresponding midpoint-radius cores. Real gauge witnesses remain valid, stored coordinates remain in their formation tiers, and every tower datum has distance at least $\delta_B/8$ from the complement of its intrinsic tube. The actual real background belongs to the half-radius domain.

For an activity $f$, with formation bound $b_f$, its localized excess satisfies
\[
 |V_f(Y)|\le {2b_f\over\varrho_X}
       (e^{\bar\kappa}-1)^{-|Y\setminus X^\uparrow|}
 \le {2b_f\over\varrho_X}
       e^{-(\bar\kappa-1)|Y\setminus X^\uparrow|},
 \tag{2}
\]
and its finite sum equals the full substituted value minus the unshifted value. On the physical locus the substituted value equals the old read. Finite composition of these transitions therefore gives (D4): all nested evaluations stay in their formation domains on their specified interpolation discs.

*Proof.* Proposition 5 gives real admission. Lemma 4 gives tube room. Proposition 6 gives inclusion with half the gap left. Definition 5 and (1) place both the unpinned and pinned shifts inside that proposition's bounds; the pillar bound ensures local holomorphy of pinning. Proposition 7 identifies the real evaluations. Lemma 8 proves (2) and resummation. Apply these statements successively to the finite ordered transitions, retaining each formation record and its parameter domain. At each step the inclusion holds for **every** value of the earlier parameters, so it also holds inside the next composition. The complex variables are not replaced by physical currents. The unchanged unshifted summand keeps its old coefficient; no assertion about a total mass norm follows from this identity. ∎

**Outstanding — application of ST1*.** The draft does not establish hypotheses 1–6 for all actual stages, even before overlapping collars occur. The failures are identified in Sections 3 and 6. The theorem above is an implication from explicit estimates, not a proof of the draft's claim that only OS remains after its original imports.

## 2. Definitions supplied in distillation

These definitions make explicit the objects or conventions that the draft leaves implicit or uses inconsistently. Actual erosion sets, row carriers, tests and record lists are formation data; an inequality about them does not specify them.

**Definition 1 (fields, units and geometry).** Work on a finite periodic lattice in four dimensions. A real configuration assigns a matrix in $SU(2)$ to each positive bond; a complex configuration uses $SL(2,\mathbb C)$. Set $U(\bar b)=U(b)^{-1}$. Use operator norm on $2\times2$ matrices and the maximum norm on finite arrays. The real Lie algebra consists of traceless Hermitian matrices; its complexification consists of traceless complex matrices. Products are in path order. Write $U_p=\partial U(p)$ for the oriented plaquette holonomy and $I$ for the identity matrix. A complete bond star has **six** plaquettes. A regional action sums only plaquettes whose full boundary belongs to the region.

The current is defined, including its normalization, by
\[
 {d\over dz}\bigg|_{z=0}\sum_p\left(1-\tfrac12\operatorname{tr}
              (e^{i\eta zB}U)_p\right)
 =\eta^4\sum_{b>0}\tfrac12\operatorname{tr}(J_\eta(U)(b)B(b)).
 \tag{3}
\]
Use the regional action to define $J^\circ$. A *plain triple* uses $J_\eta$ on complete stars and zero on incomplete stars. Its independent current coordinate need not equal $J^\circ$ at the boundary.

At numerical bare mesh $\eta$, set $\xi_l=L^l\eta$. In level-$j$ units the same bare mesh is $\eta_j=L^{-j}$; these are different coordinate systems, not different physical lattices. For a decreasing sequence $\Omega_0\supset\cdots\supset\Omega_t$, put $m(x)=\max\{l:x\in\Omega_l\}$ on $\Omega_0$ and $l(x)=\xi_{m(x)}$. It is $\rho$-separated if
\[
 \operatorname{dist}_\infty(\Omega_{l+1},\Omega_l^c)\ge\rho\xi_l.
\]
The weighted distance is the infimum of path lengths with density $l(x)^{-1}$, with the lower limiting density on shared faces. A sequence is subordinate if it is contained member by member. Its meet with another sequence is their memberwise intersection. All distances are periodic distances when the domain wraps.

For definiteness, $\operatorname{Bd}(X)$ consists of bonds incident to the site set $X$, and $\operatorname{Bd}^\circ(X)$ consists of bonds with both endpoints in $X$. Conditions on a stencil require all its bonds in the named bond set. Empty maxima are zero. A localization partition is a specified partition into half-open cubes; $X^\uparrow$ is its hull. $Z^{\wr p}$ removes two layers of the specified level-$(p-1)$ localization cubes. Both erosion assignments supply their actual nested cubical sets $\Omega_l^{\mathfrak r}(Z)$, not merely a gap size.

A determining row of level $l$ is a bond of the level-$l$ lattice with an endpoint in $\Omega_l$, no endpoint in $\Omega_{l+1}$, and both endpoints in $\Omega_0$; put $\Omega_{t+1}=\varnothing$. Denote this set by $\Gamma_l$ and its union by $\mathbf B$. The determining map is $M_{\mathbf B}(U)=(\mathcal M^lU|_{\Gamma_l})_l$, where the nonlinear averaging maps, their carriers and branches are supplied by AV. A field is critical over its datum if the first variation of its regional action vanishes on the kernel of $DM_{\mathbf B}$; the gauge slice and regularity class are supplied by BG. The row endpoints are nodes. A residual gauge equals one at the nodes. A pillar is the block of bare sites assigned to a node by this construction. A gauge acts by $U^v(b)=v(b_-)U(b)v(b_+)^{-1}$, and on a current by $\operatorname{Ad}v(b_-)$. The highest layer of a plaquette or bond is the largest layer containing one of its corners or endpoints.

The covariant difference includes the mesh denominator:
\[
 (\nabla^U_\mu A)_\nu(x)=\eta^{-1}
 [\operatorname{Ad}U_\mu(x)A_\nu(x+\eta e_\mu)-A_\nu(x)].
 \tag{4}
\]
This corrects the unnormalized definition in draft Lemma 5.2. The same convention defines $\nabla^{\mathbf U}$. A change from level $u$ units to level $v\le u$ units is
\[
 \rho_X^{u\to v}(U,A',\mathbf J)
 =(U,L^{-(u-v)}A',L^{-3(u-v)}\mathbf J)|_X.
 \tag{5}
\]
Thus $\eta A'$, $\eta^2\nabla A'$, and $\eta^3\mathbf J$ are invariant.

**Definition 2 (structures, radii and domains).** Here a history is a finite ordered list of transitions and formation records supplied by GEO. Each label $\mathcal S$ specifies the determining regions $\Omega_i$, the core regions $\Lambda_i\subset\Omega_i$, its marked sets and the actual cubical stage sets $Z_i,Z''_i$. These sets, their incidences and all inherited read lists are input data. Its structures are $\sigma=(\mathcal S,\boldsymbol\nu;t,\phi)$, including retained earlier records. At operation level $t$, $N_t\ge1$, $t-N_t\ge0$, and stage $n+1$ has level $j=t-N_t+n$. Its collar is $R_n=Z_{j+1}\setminus Z''_{j+1}$. The determining sequence uses completed counts $\boldsymbol\nu$; the action sequence uses zero counts. They are not interchangeable.

Put $\varpi_{\rm in}=1$, $\varpi_n=1-n/(2N_t)$, and $\varpi_{\rm out}=0$. Precedence counts no more completed stages and has lower level, or the same level and larger phase weight. Write
\[
\begin{split}
 c_\sigma(x|m)&=1-\beta_s+\beta_s2^{-(t-m)}+\varpi_\phi g_t(m)
                   -\beta_R\sum_{l\in\mathrm{Re}_\sigma(x)}2^{-|m-l|},\\
 g_t(m)&=\theta_s\beta_s2^{-(t-m)}\quad(m<t),\qquad g_t(t)=\beta_s.
\end{split}\tag{6}
\]
Here $\mathrm{Re}_\sigma(x)$ is a **set** of completed marked levels. Standing waiting windows are disjoint at a point, as a GEO hypothesis. Set $e_\sigma(x)=m_\sigma(x)-m^{\rm original}_\sigma(x)\ge0$ from the two recorded layer assignments and $\lambda_\sigma(x)=L_\flat^{2e_\sigma(x)}$. It is not a generic tower-scale difference.

The formation table supplies $r_0(\sigma;m),r_1(\sigma;m)>0$. The simplified running choice is $r_\iota(m)=\alpha_\iota\varepsilon_m$, $\alpha_0\le\alpha_1$. If that choice replaces SA's unfinished-top and level-zero conventions (SA 6144–6148), it is a new design that NL1/LF1 must use. Specify the level-zero table separately. At a common top use $r_\iota(\sigma''|\sigma;m)=r_\iota(\sigma;t)$ when $m=\operatorname{level}(\sigma'')=t$, and $r_\iota(\sigma'';m)$ otherwise. Define
\[
 R^{p,\iota}_\sigma(x)=c_\sigma(x|m)\lambda_\sigma(x)
                         r_\iota(\sigma;m)L^{-pm},\qquad m=m_\sigma(x).
\]
A triple $P=(U,A',\mathbf J)$ has $U$ real and pair $\mathbf p(P)=(\mathbf U,\mathbf J)$, $\mathbf U=e^{i\eta A'}U$. One splitting serves every record. Its fixed-real-factor fibre varies only $A',\mathbf J$.

The domain $\widetilde U_{\sigma'|\sigma}(Y)$ is the following finite intersection, with strict inequalities.

- **L1.** On $\operatorname{Bd}_{\mathcal S}(Y)=\operatorname{Bd}(Y)\cap\operatorname{Bd}^\circ(\Omega_0^\sigma)$, require $|\partial U-I|,|\partial\mathbf U-I|<R^{2,0}_\sigma$, $\eta^3|\mathbf J|<R^{3,0}_\sigma$, $\eta|A'|<R^{1,1}_\sigma$, and $\eta^2|\nabla^U A'|<R^{2,1}_\sigma$.
- **L2.** Each recorded cube $Q\subset Y\cap\Omega_l$, of side at most $oLM$ in level-$l$ units, has a real gauge $U^v=e^{i\eta_lA}$ with $|A|,|\nabla A|<oLMB^{cg}\lambda r_0$. The cube's radius index and lift are recorded separately. Also require the omitted YM3 containing-cube clause: each recorded natural cube of side at most $12\mathfrak M$ has a containing cube within the domain with a real gauge bounded by $a_\flat$ in its own units. Include the four CA-I gauge families below whenever their operators are read.
- **L3.** A tower address records $\sigma''\preccurlyeq\sigma'$, $1\le i\le\operatorname{level}(\sigma'')$, $Z\subset Y$ at level $i-1$, an erosion rule, and $1\le q\le p\le i$. The tower is the intrinsic background of the actual averages on $(\Omega_l^\sigma\cap\Omega_l^{\mathfrak r}(Z))_{l\le q}$. At a settled element, with $\ell=\min\{m_{\sigma''}(x),i\}$, require
  \[
  |\partial T_q-I|<L^{i-p}c_\sigma(x|\ell)\lambda r_0(\sigma''|\sigma;\ell)L^{-2\ell},\quad
  \eta_q^3|J_q(T_q)|<L^{i-p}c_\sigma(x|\ell)\lambda r_0(\sigma''|\sigma;\ell)L^{-2\ell-\min(q,\ell)}.
  \tag{7}
  \]
  Read on $Z^{\wr p}$, with complete stencils, and repeat for $U$. Settled means the tower layer equals $\min\{\hbox{ambient layer},q\}$. The draft restricts (7) to settled elements; matching every consumer stencil to such an element remains a geometry requirement. YM3 L3 tests all stated interior stencils and proves settlement there.
- **L4.** At each core address $(\sigma'',i,X')$, $X'\subset Y\cap\Lambda_i$, require $\rho_{X'}P\in\mathcal U_i^\circ(X';b_0,b_1)$, with $b_\iota=c_\sigma(x|i)\lambda r_\iota(\sigma''|\sigma;i)$. A core radius must be constant on its address; otherwise split the address or use the infimum over its read set. The core means SA (R4)–(R6): $|\partial U-I|,|\partial\mathbf U-I|<b_0\eta_i^2$, $|A'|,|\nabla^UA'|<b_1$, and $|\mathbf J|<b_0$; on every contained cube of side at most $C_{\rm box}LM$ there is a real gauge with $|A|,|\nabla A|<C_{\rm pot}Mb_0$. For every allowed subdomain, both erosion rules and $1\le q\le p\le i$, its subtower has curvature $<b_0L^{-(i-p)}\eta_p^2$ and current $<b_0L^{-(i-p)}L^{2(q-p)}$ in level-$q$ units, also for $U$. All required towers exist on their specified open branches; every stencil is interior to its eroded read region.

At an address all lifts and units must be fixed before evaluating an inequality. The half-radius domain halves the table and $a_\flat$. The real factor of a general domain point is **not** assumed critical.

For the CA-I gauge families, let $p$ be the exit-stage level, $m$ the cube index, and $k_0$ the old interface. Cubes have side $M\xi_m$; their gauge is on $Q\cap Y$. Their lift exponents are $(m-k_0)_+$ for $m<p$; $(p-k_0)_+$ for $m=p$, $Q\not\subset\Omega_{k_0+1}$; $p-\bar m$ for $m=p$, $Q\subset\Omega_{k_0+1}$, $\bar m=\max\{i\le p:Q\subset\Omega_i\}$; and zero for $m>p$. Use radius index $m$ in each case. These are CA-I 48527–48565. The fact that a cube belongs to a family does not supply its gauge witness.

**Definition 3 (substitution, activities and physical locus).** For a shift $h=(H,K)$, define on the active bonds
\[
 P\dotplus h=(U,A'',\mathbf J+K),\qquad
 A''=(i\eta)^{-1}\log(e^{i\eta H}e^{i\eta A'}).
 \tag{8}
\]
Use the convergent series logarithm. Outside the active bonds leave the coordinates unchanged; do not apply $\log(e^{i\eta A'})$ to unrestricted outer coordinates. Restriction uses (5).

A carried activity is a scalar function on its **fixed formation domain**, together with its fixed stored variables. It is bounded by $b_f$, holomorphic on fixed-$U$ fibres, Borel in $U$ and near stored variables, analytic in far stored variables and switches, and invariant under simultaneous real gauge transformations of pair and stored variables. A real tie means equal values on real splittings of one pair; a pair function has this property for complex splittings too. These are different hypotheses.

Each stored slot records its bond, initial site, formation level, real range and near/far classification. A near slot ranges over its prescribed real Hermitian ball; a far slot over the complex ball of radius $\lambda_l^{st}$ times its real range. Switches have $|\mu_b|<\lambda_l^{st}$. The value is independent of the slot when its switch is zero, and independent of the switch when the slot is zero. The tie holds at every switch value. All these slots stay fixed in the composition.

The physical locus has real fields, $s=\mathbf1$, $\lambda=1$, and the prescribed physical current, with the plain-current boundary convention. Off this locus the composition is a definition. Equality on this locus identifies integrands, but does not identify arbitrary holomorphic extensions or prove their bounds.

**Definition 4 (compatible read data and room).** For one transition write $+$ for its input and $-$ for the earlier domain to be read. A read record contains its function $F_a(P)$, stencil, units, base radius $R_a>0$, and coefficients $c_a^+<c_a^-$. Thus its bounds are $|F_a|<c_a^\pm R_a$. For example, the normalized simple reads are
\[
 L^{2m}(\partial U-I),\ L^{2m}(\partial\mathbf U-I),\
 L^{3m}\eta^3\mathbf J,\ L^m\eta A',\ L^{2m}\eta^2\nabla^UA',
\]
with base radii $\lambda r_0,\lambda r_0,\lambda r_0,\lambda r_1,\lambda r_1$. Normalize tower reads in (7) by $L^{2\ell+p-i}$ and $L^{2\ell+\min(q,\ell)+p-i}\eta_q^3$, respectively. Put
\[
 \Delta_a=(c_a^--c_a^+)R_a,
 \qquad b_a^{\rm mid}=(c_a^-+c_a^+)R_a/2.
 \tag{9}
\]
Compatibility means: each target read is the **same function** as a read controlled at the input with bound $c_a^+R_a$; each target real gauge requirement is already imposed with no smaller witness bound; and each target core is imposed initially at $(1-\tau_a)b_\iota^{\rm mid}$, with $\tau_a=1-c_a^+/[(c_a^-+c_a^+)/2]$. Restriction must preserve these statements. A change of tower or lift requires its own comparison; equality of the names $(\sigma'',i,Z)$ is insufficient. This definition states the exact common-domain hypothesis used below.

Choose a positive profile $w(b)$ and set
\[
 \|h\|_w=\max_b{\max\{l(b)|H(b)|,\ l(b)^2|\nabla^UH|(b),\ l(b)^3|K(b)|\}\over w(b)}.
 \tag{10}
\]
All neighboring values required in a stencil enter this maximum. In the fixed-layer, fixed-lift case the draft's choice is
\[
 w(m)=\tfrac12d_*2^{-(t-m)}\alpha_0\varepsilon_m,
 \quad d_*=(1-\theta_s)\beta_s\text{ for a main step},\quad
 d_*={\theta_s\beta_s\over2N_t}\text{ for a preparatory stage}.
 \tag{11}
\]
For the half-gap conclusion require that the pointwise increment, tower increment and restricted core-shift bounds used in Proposition 6 are valid with this profile. In particular, compare the full radii in (9), including changed layer powers and lifts. The coefficient difference alone is not that comparison.

**Definition 5 (regional response and interpolation radius).** The source $\mathcal S_v$ of a transition is its actual set of changed rows, with their averaging carriers. Pivot completion is a specified analytic map $\mathcal A\mapsto B'_Y$ on these rows, extended by zero on the other rows. The regional shift is DR evaluated at the restricted input pair and $B'_Y$, in one common system of units. Assume, for all $s\in\mathbb D(Y)=\{|s_c|<e^{\bar\kappa}\}$,
\[
 \mathfrak n(h_Y)(b)\le C_{\rm src}C_{\mathcal A}\delta_{\rm src}
                          e^{-\mu d(b,\mathcal S_v)}.
 \tag{S}
\]
Here $\mathfrak n$ is the numerator of (10), $C_{\mathcal A}\delta_{\rm src}$ bounds the complex fluctuation contour, and $\mu>0$. Conversion from DR's $\mathbf U$-transport to $U$-transport is included in $C_{\rm src}$; it is not an equality of derivatives.

For a pinned read assume LEV gives $\| (\lambda h_Y)^\delta\|_w\le C_{\rm lev}|\lambda|C_{\rm src}C_{\mathcal A}\delta_{\rm src}Q_X$ whenever its endpoint pillars are levelled. Include the full profile loss $C_m e^{C_m\delta_{\rm prof}}$ in $C_{\rm lev}$. Let
\[
 Q_X=\max_{b\text{ read by }X}{e^{-\mu d(b,\mathcal S_v)/2}\over w(b)},\qquad
 E_X=\max_{y\text{ endpoint pillar of }X}e^{-\mu d(y,\mathcal S_v)/2}.
\]
The read set includes all tower, core and pinning neighborhoods used by the estimate. Empty maxima are zero. Require the pillar-size functional of the unpinned shift, which triggers levelling, to be at most
$K_{\rm pin}|\lambda|C_{\rm src}C_{\mathcal A}\delta_{\rm src}E_X$.
For plain reads set $C_{\rm lev}=1$ and omit the pillar term. Define
\[
 a_X=C_{\rm src}C_{\mathcal A}\delta_{\rm src}
       \max\left\{{C_{\rm lev}Q_X\over r_*},
                         {K_{\rm pin}E_X\over\epsilon_{\rm lev}}\right\}.
 \tag{12}
\]
Then $|\lambda|<(2a_X)^{-1}$ gives shift norm $<r_*/2$ and pin size $<\epsilon_{\rm lev}/2$. The amplitude multiplies the shift before pinning; pinning is not linear in $\lambda$.

A localized composition is
\[
 \Phi_Y[f](s,\lambda)=f(\rho_XP\dotplus_{\mathcal S}\rho_X(\lambda h_Y);\mathfrak q_X),
 \tag{13}
\]
or uses $\rho_X(\lambda h_Y)^\delta[P]$. For disjoint cube sets $K,N$, define
\[
 [K|N]F=\sum_{A\subseteq K}(-1)^{|K|-|A|}F(\mathbf1_{N\cup A}),
 \qquad [K|N]^*F=[K|N](F-F(0)).
 \tag{14}
\]
Take $K=Y\setminus X^\uparrow$, $N=X^\uparrow$, and define $V_f(Y)=[K|N]^*\Phi_Y[f](\cdot,1)$. Regional consistency means these evaluations equal restrictions of one torus function at the same parameter corners. Component locality means a component of varied cubes disconnected from the base contributes zero. These are response properties, not consequences of Cauchy's inequality.

**Definition 6 (thresholds and auxiliary constants).** The frame is a supplied positive sequence $\theta_l$, with $g_l=\theta_l^{-1/2}\le\gamma$; density weights $x_l$ are separate variables. RUN supplies $\varepsilon_l=g_lp_0(g_l)$, where $p_0$ is the specified logarithmic threshold function. Main fluctuations use $\delta_l=(A_1/A_0)\varepsilon_l$, and preparatory fluctuations use $\delta'_l=(A_1/A_0)(\log\theta_l)^{-(\mathfrak p_0-\mathfrak p_1)}\varepsilon_l$, with fixed $\mathfrak p_0>\mathfrak p_1$. Thus $\delta_{\rm src}$ means the appropriate threshold at the actual source level. The constant $C_{\rm run}\ge1$ controls the ratios stated below.

The geometric data include the background cube size $\mathfrak M$, localization size $M$, gauge-cube factor $o$, and minimum size $M'_1$. The constants $B^{cg},C_{\rm box},C_{\rm pot},K_{cg}$ are the supplied cube-gauge size and comparison constants. The positive ceilings $a_m,a_{\mathfrak h},\epsilon_{\mathfrak h},c_{rt},a_\flat,a^\sharp$ respectively name averaging/source-cube admission, DR pair admission, DR source admission, LEV triple admission, the natural-cube gauge bound, and CORE admission. The constants $C_{\rm os},K^\sharp,c_\natural$ have exactly the roles in (16). The constants $\delta_T,\delta_{\rm prof},\mu$ are decay rates for towers, profiles and response; $\epsilon_{\rm lev}$ is the pillar threshold forcing levelling. Their values and domain hypotheses come from the named imports, not from the three-dimensional labels. Finally, $\mathfrak q_X$ is the restriction of the fixed stored-coordinate list to the bonds and levels of the formation record.

For pinning, a level-$q$ pillar is the recorded block $B^q(y)$ with top $y$ and side scale $\xi_q$. A top in $Y$ has $B^q(y)\subset Y$. It is *pinnable* when $q\ge2$, or when $q=1$ and every bare site within $2\eta$ of its pillar belongs to a level-zero or level-one pillar. Its read set $\operatorname{Rd}_Y(y)$ contains all bonds used by its block recursion; for a pinnable level-one top it is enlarged to all active bonds with endpoints within $2\eta$ of its pillar. Define $\widehat\varepsilon_y(H)=\xi_q\sup_{\operatorname{Rd}_Y(y)}|H|$. A top is *levelled* when this is below $\epsilon_{\rm lev}$; this is the functional bounded in Definition 5. The exact block carriers and stored axial paths are part of GEO/LEV. Preservation of a stored transport means equality of its ordered path product before and after the pinned response. This is the YM3 54647–54710 convention; its four-dimensional estimates are still LEV's obligation.

## 3. Imports and the quantitative hypotheses they must supply

All imports below are hypotheses. A source label or a three-dimensional proof supplies no four-dimensional verification.

- **GEO (LF1):** the actual nested regions, separated sequences where required, two erosion assignments, torus floors, row/carrier geometry, persistence of formation records, and disjoint standing waiting windows. It must prove settlement at every required interior tower stencil and the geometry of each source. SA 9776 and 17398–17401 assert separation for stage sequences. Overlap of collars at different stages does not negate that assertion.
- **BG (BG1):** on each admitted determining system $e$, real data have one regular critical orbit and one canonical axial representative. Its continuation $\Phi_V(B)$ is holomorphic for $\|B\|<r_B$, real at real $B$, agrees on the specified overlaps, and obeys the restriction identity. To specify the datum class, supply the finite set of test loops $\mathscr T_e$, their ordered row products $V_\tau$, and their thresholds $\epsilon_{e,\tau}$. Set $\mathcal R_e=\{V\in SU(2)^e:|V_\tau-I|<\epsilon_{e,\tau}\ \forall\tau\}$, with thresholds chosen inside BG's regularity class and with its real perturbation margin. The intrinsic tube is
  \[
  \mathcal T_e=\bigcup_{V\in\mathcal R_e}\{e^{iB}V:\|B\|<\delta_B\},\qquad
  T_e(D)=\Phi_V(i^{-1}\log(DV^{-1})).
  \tag{15}
  \]
  The common-branch hypothesis is the one in `intrinsic-dom.md`, equations (5)–(6), not uniqueness of an ungauged field.
- **AV:** the actual nonlinear averages and pivot completions, their branches, locality and covariance. On the fields used below, $M_e(U)\in\mathcal R_e$ with its real margin and $M_e(e^{i\eta A'}U)=e^{i\beta}M_e(U)$, $\|\beta\|\le C_{\rm av}\max_b l(b)|A'(b)|$. The constants may depend on $L$. SA 9667 has a seam constant $CL^2$; it does **not** supply the exact four-dimensional value $2L^2$ imported from YM3 by the draft.
- **PROF (PR1):** real critical backgrounds have the local curvature and current profile bounds, and the cube-gauge theorem with its smallness and enlargement hypotheses. The real-admission estimates in Proposition 5 must hold on all required gauges and core addresses, including the containing-cube clause.
- **DR (PR1/NL1):** the actual fixed-system decoupled response, including its independent multiplier-current increment, on a supplied open pair domain $D_{\rm DR}$. It is zero off the active bonds and has weighted first-order bounds, holomorphy, Borel dependence, covariance, restriction, component splitting and vanishing at zero source/parameters. Pivot sources belong to its supplied source ball. `dec-field.md` Proposition 5.1 proves a conditional **field** response under [PW], [NL]; it does not by itself supply all these current, gauge and stage-domain assertions.
- **CRIT:** at $s=1$ over a real regular critical pair, the response solves the actual shifted constraint, yields the shifted current, and is regular enough for BG uniqueness. It also supplies the invariance under the plain-current boundary correction when used. The correction is supported on bare determining rows, not on all bonds outside the stage collar. SA 5800–5803 and 10446–10464 sketch this identification. Its required four-dimensional form remains an open import.
- **CORE (NL1):** the stated cores, their gauge clauses, and outer substitution. Precisely, for $0<\tau<1$, $0<b_0\le b_1$, $b_1^2\le c_\natural b_0$, $2(b_0+b_1)\le a^\sharp$, a shift satisfying
  \[
  |H|,|\nabla^{\mathbf U}H|<{\tau b_0\over C_{\rm os}K^\sharp(1+c_\natural)},
                  \qquad |\mathbf J+K|<b_0
  \tag{16}
  \]
  sends the core at $((1-\tau)b_0,(1-\tau)b_1)$ into the core at $(b_0,b_1)$. The derivative convention and separate current condition matter. YM3 42287–42325 gives $C_{\rm os}=18$ there. The four-dimensional outer-core substitution remains an open import.
- **LEV:** pinned levelling on a supplied regular triple domain $D_{\rm LEV}$, with its local gauge requirements on turning cells. It gives the gauge $u$, the transformed pair, and the bounds in Definition 5. With the current already in the shift's units,
  \[
  e^{i\eta H^\delta}\mathbf U=(e^{i\eta H}\mathbf U)^u,
  \qquad K^\delta=\operatorname{Ad}u(\mathbf J+K)-\mathbf J.
  \tag{17}
  \]
  It is holomorphic only where every endpoint pillar used by the read remains levelled. It must preserve the actual stored transports at their pinnable sites and give the common-center continuation used for complex ties. Pointwise bounds on $u,u^{-1}$ alone do not suffice. The four-dimensional construction remains an open import; YM3 54627–55124 is its model, not its proof in four dimensions.
- **FL:** the actual real fluctuation tests and the full complex contour bound $|\mathcal A|<C_{\mathcal A}\delta_{\rm src}$. Passed real tests alone do not prove the complex bound or its half-radius version.
- **RUN:** the supplied positive threshold/table sequences and all comparisons actually used. For the elementary estimates below assume $\varepsilon_{n+\nu}/\varepsilon_n\le C_{\rm run}(1+\sqrt\nu)$ and $\varepsilon_n/\varepsilon_{n+\nu}\le C_{\rm run}$. If only the symmetric polynomial bound is available, retain the extra polynomial in the constants and decay estimates. For off-diagonal histories the tests use the frame $\theta$, not the density weights $x$. Put $\underline\theta_t=\min_{i\le t}\theta_i$ for waiting-depth estimates (SA 19410).

One further quantitative hypothesis is used for towers. On $\mathcal Q^T(a_T)=\{(U,A'):L^{2m}|\partial U-I|<a_T,\ l|A'|,l^2|\nabla^UA'|<a_T\}$, each fixed subordinate tower exists, and its settled, ambient-normalized curvature/current $G_e$ satisfies
\[
 |G_e(U,A'_1)-G_e(U,A'_0)|
 \le K_T\max_b e^{-\delta_Td(x_e,x_b)}
       \max\{l(b)|A'_1-A'_0|,l(b)^2|\nabla^U(A'_1-A'_0)|\}.
 \tag{T}
\]
Here $G_e=L^{2m}(\partial T-I)$ or $L^{2m+\min(m,q)}\eta_q^3J_q(T)$. Use the record's truncated ambient scale when it is shallower. This is the content needed from the draft's Theorem B and Corollary B′.

**Outstanding — derivation of (T).** YM3 55448–55930 proves its three-dimensional form. SA 9755 states its four-dimensional analogue as part of Theorem 5(b). The draft's proof invokes the Landau-difference norm including second-order field control, the pillar gauge derivative, and a weighted row sum without supplying their four-dimensional statements. A bound on $H,\nabla H,K$ from DR is not the bound on $D^{\mathsf T}DH$ used at YM3 55700–55760. Merely changing a dimensional counting constant does not complete this step. Lemma 4 below proves tube room under AV/BG; it does not prove (T).

## 4. Constants in order of choice

The theorem is uniform only when this order can be fulfilled uniformly.

1. Fix $0<\beta_s\le1/4$, $0<\theta_s<1$, $0<c_R\le(1-\theta_s)/16$, and $\beta_R=c_R\beta_s$. Fix the logarithmic exponents. Choose odd $L\ge13$ and integer $2\le L_\flat<L/2$.
2. Obtain the primitive averaging, background and response constants and rates from their imports, in their declared order. Choose the geometric lengths after the rates they must dominate: $\rho\ge4$, $\rho\min(\delta_T,\mu/2)\ge\log4$, $\rho\delta_{\rm prof}\ge64\log L$, and $M\ge L^4M_1'$, together with every imported torus/cube floor. Radii may be decreased afterwards. This requires that those imports allow such enlargement; it is not a proof of that compatibility.
3. Fix $0<\delta_B\le\min(1/40,r_B/40)$, $a_T,a^\sharp,a_m,a_{\mathfrak h},a_\flat,c_{rt},\epsilon_{\rm lev}$, and $\bar\kappa\ge1$. Fix the source, pivot, pinning, tower and gauge constants. Choose $\alpha_0\le\alpha_1$ large enough for the real-admission floor $C_{\rm mb}C\le(1-\beta_s-3\beta_R)\alpha_0/2$. No coupling has yet been chosen.
4. Choose an absolute radius ceiling $\widehat a\le\min\{a_T/4,2^{-12}L^{-2},a_m,c_{rt},a_{\mathfrak h}/\max(K_{cg},L^3),a^\sharp/16,\delta_B/(4C_{\rm av})\}$. On every formation read require $c_\sigma\lambda_\sigma r_\iota\le\widehat a$, $b_1^2\le c_\natural b_0$, and $2(b_0+b_1)\le a^\sharp$, also for the midpoint cores. Supply the natural/source-cube and turning-cell witnesses and their own imported ceilings. These are the radius comparisons omitted from draft Theorems E–F.
5. Determine uniform constants $K_{\rm pt},K_{\rm tw},K_{\rm core}\ge1$ for Proposition 6 from these fixed data and profile comparisons. Put
   \[
   r_*={1\over8\max\{1,K_{\rm pt},K_{\rm tw},K_{\rm core}\}}.
   \tag{18}
   \]
   The factor $C_{\rm lev}$ is charged separately in (12).
6. Choose $A_1/A_0$, the waiting-depth rule and then the coupling ceiling $\gamma$ so that all absolute-radius ceilings, $C_{\mathcal A}\delta_{\rm src}<\epsilon_{\mathfrak h}$, and $a_X<1/2$ hold. At a main step this includes $\delta_{t-1}/\varepsilon_t$, with its RUN factor. At a preparatory stage it is the **actual** $Q_X$ of (12), not the estimate with the wrong source level in the draft. Section 6 explains why the draft's (N-growth) does not verify this choice.

A polynomial lift bound $\lambda\le C(1+\log\underline\theta)^s$, if supplied by GEO, is absorbed by the final absolute-radius ceiling because $\theta^{-1/2}(\log\theta)^q\to0$ for every fixed $q$. To see this by hand, write $y=\log\theta$, choose an integer $m>q$, and use $e^{y/4}\ge(y/4)^m/m!$. Then $y^qe^{-y/2}\le4^mm!y^{q-m}e^{-y/4}\to0$. This absolute-radius argument does not verify the response-to-gap bound: there the coupling factor cancels and only a logarithmic saving remains, as (34) shows.

## 5. Lemmas and proofs

**Lemma 2 (coefficient, geometric and profile arithmetic).** Under the standing-mark convention,
\[
 1-\beta_s-3\beta_R\le c_\sigma\le1+\beta_s,
 \qquad c_\sigma\ge1-2\beta_s\ge\tfrac12.
 \tag{19}
\]
For fixed marks and $m\le t-1$, the main-step gap is
\[
 c_{(t-1,\mathrm{out})}(m)-c_{(t,\mathrm{in})}(m)
                =(1-\theta_s)\beta_s2^{-(t-m)}.
 \tag{20}
\]
For a preparatory stage with new, distinct marked levels $E_n$,
\[
 c_n(m)-c_{n+1}(m)={g_t(m)\over2N_t}
                 +\beta_R\sum_{l\in E_n}2^{-|m-l|}.
 \tag{21}
\]
Their sum over one operation is at most $g_t(m)/2+3\beta_R$. Passing from phase $N_t$ to output, with no further marks, spends the remaining $g_t(m)/2$.

Meets of separated sequences are separated with the smaller gap. For a separated sequence,
\[
 |m(x)-m(z)|\le1+d(x,z)/\rho.
 \tag{22}
\]
For an ambient sequence and a subordinate tower of depth $p$, let $\xi'$ and $d'$ be the tower scale and distance, and $d^\flat$ the distance of the ambient sequence truncated at $p$. Then $d'\ge d^\flat$, $d'(x,z)\ge\xi_p^{-1}|x-z|_\infty$, and, writing $s(x)=l(x)/\xi'(x)$,
\[
 {s(x)\over s(z)}\le L^{2+2d'(x,z)/\rho}.
 \tag{23}
\]
At a settled element with $s(x)>1$, the tower has ended at $p$; outside the Euclidean $l(x)$-neighborhood, $d'(x,z)>s(x)$.

For the profile (11), RUN and $L\ge4$ give
\[
\begin{split}
 w(n-\nu)&\le C_{\rm run}2^{-\nu}w(n),\\
 w(n+\nu)L^{-p\nu}&\le C_{\rm run}w(n)\quad(p\ge1),\\
 e^{-\omega(\nu-1)}w(n+\nu)&\le4C_{\rm run}w(n)
                         \quad(\nu\ge1,\ \omega\ge\log4).
\end{split}\tag{24}
\]
For identical read functions, radii and witness requirements, increasing every coefficient gives domain inclusion.

*Proof.* The sum over any subset of integer levels is at most $1+2\sum_{r\ge1}2^{-r}=3$. At $m<t$ the first three terms of (6) are at most $1-\beta_s+(1+\theta_s)\beta_s/2\le1$; at $m=t$ they are at most $1+\beta_s$. This proves (19). Subtraction proves (20) and (21). Distinctness of marks gives the stated sum; $\varpi_{N_t}=1/2$ gives the final gap.

The complement of a meet is the union of complements. Each point in its next member is therefore at least the smaller gap from that complement. A path changing layer by $\nu$ crosses $\nu-1$ disjoint intermediate strips, each contributing at least $\rho$ to its weighted length. This proves (22). Tower density is at least ambient density and everywhere at least $\xi_p^{-1}$. Apply (22) to both layer functions to obtain (23). At a settled point with unequal scales, $\xi'(x)=\xi_p$; the global density bound, not merely a bound near $x$, gives the last assertion.

For $\nu\ge1$, $1+\sqrt\nu\le2^\nu$: it holds at one, and $1+\sqrt{\nu+1}\le2(1+\sqrt\nu)$ gives induction. Hence $w(n+\nu)/w(n)\le C_{\rm run}4^\nu$. The other RUN inequality and geometric factors give (24). Finally, each fixed scalar inequality and each monotone core inequality persists when its radius increases; unchanged real witnesses still apply. This last assertion requires equality of the functions being bounded. ∎

**Lemma 3 (local substitution estimates).** Put $\ell(X,Z)=\log(e^Xe^Z)-X-Z$. For $|X|+|Z|\le1/2$, the series logarithm exists and $|\ell|\le3$. For $|X|+|Z|\le1/4$,
\[
 |\ell(X,Z)|\le12(|X|+|Z|)^2.
 \tag{25}
\]
For $|X|\le1/8, |Z|\le1/16$, $|\ell|\le4|X|$. For all arguments of norm at most $1/16$,
\[
 |\ell(X,Z)-\ell(X,Z')|\le96|X||Z-Z'|,\qquad
 |\ell(X,Z)-\ell(X',Z)|\le12|X-X'|.
 \tag{26}
\]
Thus, with $D=A''-A'$ and $\eta|H|,\eta|A'|\le1/16$,
\[
 \eta|D|\le5\eta|H|,\qquad
 \eta^2|\nabla^UD|\le13\eta^2|\nabla^UH|
                 +96\eta|H|\eta^2|\nabla^UA'|.
 \tag{27}
\]
For the plaquette estimate impose the smaller bound $\eta|H|,\eta|A'|\le1/64$ on its bonds. With $h=\max_p|H|$, $a=\max_p|A'|$, $g=\max_p|\nabla^UH|$,
\[
 |\partial(e^{i\eta H}\mathbf U)-\partial\mathbf U|
 \le2^{12}\{\eta^2g+\eta h(\eta h+\eta a+|\partial\mathbf U-I|)\}.
 \tag{28}
\]

*Proof.* The exponential series gives $|e^Xe^Z-I|\le e^{|X|+|Z|}-1$. For $n\ge2$, $n!\ge2\,3^{n-2}$, so $e^{1/2}\le1+1/2+$1/8$/(1-1/6)=33/20<5/3$. The logarithm series therefore has norm less than $2$; adding $|X|+|Z|$ gives the bound $3$. The function has no constant or linear term. On the complex line $(zX/(2u),zZ/(2u))$, $u=|X|+|Z|$, twice applying Schwarz gives $3(2u)^2$, proving (25). Schwarz follows by applying the maximum principle to $F(z)/z$ and letting the circle approach the domain radius; the same argument applies to matrix-valued functions by scalar linear functionals.

On $|z|\le1/8$, $\ell(z\widehat X,Z)$ has norm at most $12(3/16)^2<1/2$ and vanishes at zero. This gives $4|X|$. A Cauchy circle of radius $1/16$ in the second variable, with first variable of norm at most $1/8$, bounds its derivative by $12$. Apply Schwarz in the first variable to the difference at $Z,Z'$ to get the first inequality of (26). A Cauchy circle in the first variable gives the second. Integrate derivatives along the segments between the arguments.

Conjugation commutes with the exponential and logarithm series wherever both branches exist; only unitary conjugation preserves the norm balls. Transport neighboring $H,A'$ by $U(e)$, apply (26) first to $H$, then to $A'$, and divide by the mesh denominator in (4). This gives (27).

For completeness, move the four inserted exponentials past the old path factors in one plaquette. Each conjugating path has at most four bonds, hence condition number at most $e^{8/64}<2$. The four exponent norms are at most $2\eta h$. Their product minus its constant and linear terms has norm at most
$(8\eta h)^2$, since $8\eta h\le1/8$ and $e^u-1-u\le u^2$ for $0\le u\le1/2$, by the same factorial bound.

Write $P=\partial\mathbf U(p)$. In the first variation, after transport to the base point, the linear sum divided by $i\eta$ is
\[
 \eta(\nabla^{\mathbf U}_\mu H_\nu-\nabla^{\mathbf U}_\nu H_\mu)
 +(1-\operatorname{Ad}P)
        (\operatorname{Ad}\mathbf U_\nu H_\mu(x+\eta e_\nu)+H_\nu(x)).
\]
For a matrix $V$ with $V,V^{-1}$ bounded, use
$VXV^{-1}-X=(V-I)XV^{-1}+X(V^{-1}-I)$.
Here all partial path factors and their inverses have norm at most $2$. Also
\[
 |\nabla^{\mathbf U}H-\nabla^UH|
 \le\eta^{-1}(e^{2\eta a}-1)h\le4ah.
\]
These identities bound the linear sum by
$2\eta^2g+8\eta^2ah+32\eta h|P-I|$. Multiplying the remainder and linear sum by the remaining old plaquette factor costs at most $2$. Each coefficient is less than $2^{12}$, proving (28). ∎

The constants are deliberately weaker than YM3. Its 56066–56095 gives quadratic coefficient $2$ and mixed coefficient $16$, versus $12,96$ here and in the draft. YM3 56103–56125 gives normalized current, potential, gradient and curvature increments $1,3/2,3/2,2.03$. The draft gives $1,5,13$ plus its $96$-term, and an unspecified curvature constant. Equations (27)–(28) provide a valid explicit replacement. These fixed losses shrink $r_*$ and the fluctuation ceiling. They do not affect the conditional theorem's form, and cannot repair the stage-level or changing-tower problems below.

**Lemma 4 (intrinsic tube room).** Assume BG and AV. Let $V=M_e(U)\in\mathcal R_e$ and $D=M_e(\mathbf U)=e^{i\beta}V$, with $\|\beta\|<\delta_B/2$. Then $T_e(D)$ exists, is holomorphic in the fixed-$U$ fibre, and
\[
 \operatorname{dist}(D,\mathcal T_e^c)\ge\delta_B/8.
 \tag{29}
\]
The distance is in the finite product $SL(2,\mathbb C)^e$, with maximum matrix norm, not in all unconstrained matrix arrays.

*Proof.* If $D'$ is in this product and $\|D'-D\|<\delta_B/8$, unitarity of $V$ gives
\[
 \|D'V^{-1}-I\|<\delta_B/8+{\delta_B\over2-\delta_B}<3\delta_B/4.
\]
The logarithm series has norm at most $(3\delta_B/4)/(1-3\delta_B/4)<\delta_B$. Its trace is zero: exponentiating its trace gives determinant one, and its small norm selects the zero trace branch. Thus $D'$ belongs to the patch about $V$ in (15), proving (29). Holomorphy is composition of AV with BG's common intrinsic branch. ∎

**Proposition 5 (real admission from the real background estimates).** Suppose BG restriction and AV apply at every recorded subordinate tower. Suppose the real critical field has, at each complete regularity element of highest layer $q$, curvature and current bounds
\[
 |\partial U-I|<C\varepsilon_qL^{-2q},\qquad
 \eta^3|J_\eta(U)|<C\varepsilon_qL^{-3q}.
 \tag{30}
\]
Suppose the imported cube-gauge estimates give normalized gauge size $<C_{\rm mb}C\varepsilon_l$ at every required address: divide by its fixed gauge factor, namely $oLMB^{cg}$ for large cubes, $C_{\rm pot}M$ for core cubes, and one for natural cubes. Assume $C_{\rm mb}\ge C_{\rm run}$, every restricted datum has the required real margin, and
\[
 C_{\rm mb}C\varepsilon_l\le\tfrac12c_{\min}\lambda r_0(\tau;l),\qquad
 C_{\rm mb}C\varepsilon_l\le a_\flat/2,
 \quad c_{\min}=1-\beta_s-3\beta_R,
 \tag{31}
\]
at every address. Then the plain triple belongs to every specified half-radius domain.

*Proof.* If the base layer is $l\le q$, RUN gives
$L^{-2(q-l)}\varepsilon_q\le C_{\rm run}\varepsilon_l$, since $L\ge4$ and $1+\sqrt\nu\le2^\nu$. The current has still stronger decay. Equations (30)–(31) prove L1; the potential is zero and the incomplete-star current is zero. The assumed cube-gauge estimates and (31) give both parts of L2.

BG restriction identifies each real tower with a real gauge transform of the restricted field, once AV has admitted its datum. Curvature and current norms are unchanged. Their bounds imply (7) because $L^{i-p}\ge1$ and $L^{-3\ell}\le L^{-2\ell-\min(q,\ell)}$. This proves L3, including existence at zero logarithmic perturbation.

For a core address $X'\subset\Lambda_i\subset\Omega_i$, separation supplies complete stars. The same restrictions and gauges give its simple conditions. A subtower of depth $q\le p\le i$ has curvature $<C_{\rm run}C\varepsilon_iL^{-2i}$ and level-$q$ current $<C_{\rm run}C\varepsilon_iL^{-3(i-q)}$. Compare with the core bounds using $2i\ge i+p$ and $3(i-q)\ge i+p-2q$. This gives L4. The same real factor serves all addresses. ∎

**Outstanding — supplying (30)–(31).** The draft's Theorem A refers to a recomputed four-dimensional $C_{\rm mb}$, but does not give the required gauge theorem and all its ceilings on the remade cube families. It also omits YM3's containing-cube clause, used to admit DR and LEV. Proposition 5 states the exact conditional implication; passed real tests, a tower address, or the label “critical” alone do not verify its hypotheses. The actual plain triple is critical; arbitrary real factors in the complex domain are not.

**Proposition 6 (half-gap substitution).** Use compatible read data. Let $r=\|h\|_w\le r_*$. Require that the local logarithms and both tower arguments lie in the radius ceilings of Section 4, and that the normalized pointwise estimates from Lemma 3 and the tower estimate (T) give respectively
\[
 |F_a(P\dotplus h)-F_a(P)|\le K_{\rm pt}r\Delta_a/2
 \quad\hbox{or}\quad K_{\rm tw}r\Delta_a/2.
 \tag{32}
\]
For each midpoint core require the restricted potential, derivative and current bounds to be at most $K_{\rm core}r$ times their allowable increments in (16), with current increment allowance $\tau_ab_0^{\rm mid}$. Then all target scalar reads are $<b_a^{\rm mid}$ and all target core reads belong to the midpoint cores. The same holds for a pinned shift satisfying these bounds.

*Proof.* The input read is $<c_a^+R_a$. Equations (18) and (32) add at most $\Delta_a/16<\Delta_a/2$. This proves the claimed scalar inequalities. L2 is unchanged because the real factor is unchanged and compatibility includes every target gauge cube. For each core, $K_{\rm core}r\le1/8$; hence (16) holds strictly at the midpoint target radii. Its current remains below $b_0^{\rm mid}$, since the input current is below $(1-\tau_a)b_0^{\rm mid}$. Apply CORE. Equations (4)–(5) show that restriction commutes with (8). The small logarithm is defined only on the active bonds; outside them the unchanged-coordinate definition applies. ∎

Here is what is required to obtain uniform constants in (32). On fixed layer data, a finite adjacent-stencil comparison $C_{\rm adj}$ bounds the neighboring scaled shift by $C_{\rm adj}rw(m)$. Lemma 3 then gives a pointwise constant depending only on $C_{\rm adj},L,\widehat a$. For instance its curvature bound, after multiplication by $L^{2m}$, is at most
\[
 2^{12}rw(m)\{C_{\rm adj}+C_{\rm adj}^2\widehat a
                                  +C_{\rm adj}(L+1)\widehat a\}.
\]
Potential and derivative constants follow from (27). For towers, (T) and (27) reduce the bound to the profile convolution
$\sup_b e^{-\delta_Td(x,b)}w(m_b)$.
Equations (22)–(24) bound this by $4C_{\rm run}w(m_x)$, up to the fixed site-to-top and restriction factors. Restricted core shifts have the factors $L,L^2,L^3$ of (5), with the incident-layer comparison in (24); charge these to $K_{\rm core}$. Each argument concerns the **same tower map on both sides**. These estimates do not bound the change caused by replacing that map with a different determining system.

**Proposition 7 (physical identification).** Assume hypothesis 5 of Theorem 1. Then the carried composition at $s=\mathbf1,\lambda=1$ equals the actual old read, with stored variables fixed in its recorded coordinates.

*Proof.* The relation $M_+=F\circ M_-$ gives $\ker DM_-\subseteq\ker DM_+$. The new critical background is therefore critical for $M_-$ over its own datum $M_-(U_+)$. CRIT, including its plain-current boundary correction, makes the shifted field critical for the reconstructed old datum and identifies its current in the units (5). Regularity and BG uniqueness identify its real orbit with the old background's orbit. LEV and the stored-coordinate reconstruction give a real gauge $v$ relating the **joint** pair and stored coordinates to the old joint data. Gauge invariance and the real tie of $f$ then give equality of values. Since this equality holds on the real integration domain, the represented integrand is unchanged. No uniqueness theorem for extensions off that locus is used. ∎

**Outstanding — the preparatory reconstruction.** The one-step pivot chart SA 8289–8296 supplies a chart for a single homogeneous fibre. CA-I 54287 requires the actual collar variables $(A_j,B_j)$. The draft does not identify their joint map to the old determining rows, including any changed outward rows and return factors. Nor does it prove that every stored site is pinnable for this stage. CRIT applies only after this datum and domain matching. The stronger claim in draft Lemma D.1, allowing current changes on any bonds not touching the stage region, is unsupported: YM3 54449–54527 uses bare rows outside $\Omega_1$. In four dimensions an incomplete star can retain five plaquettes, not three; a safe local current factor is six, with imported regularity ceilings reduced accordingly.

**Lemma 8 (localized excess and exact finite resummation).** Suppose the compositions (13) are admitted and bounded by $b_f$ on $\mathbb D(Y)\times\{|\lambda|<\varrho_X\}$, with $\varrho_X>1$. Suppose the zero shift, regional consistency and component locality of Definition 5 hold. Then (2) holds and
\[
 \sum_{Y\supseteq X^\uparrow}V_f(Y)
 =\Phi_T[f](\mathbf1,1)-f(\rho_XP;\mathfrak q_X).
 \tag{33}
\]
The sum is over the finite cube subsets; terms excluded by the stated component locality vanish.

*Proof.* $G(s,\lambda)=\Phi(s,\lambda)-\Phi(s,0)$ vanishes at $\lambda=0$ and is bounded by $2b_f$. Schwarz gives $|G(s,1)|\le2b_f/\varrho_X$. Its value at zero cube parameters is zero. Iterating the fundamental theorem of calculus expresses $[K|N]G$ as the integral of its mixed derivative over the unit cube. At every integration point each Cauchy circle can have radius arbitrarily close to $e^{\bar\kappa}-1$. Cauchy's formula gives (2); $e^{\bar\kappa}-1\ge e^{\bar\kappa-1}$ for $\bar\kappa\ge1$.

For resummation expand (14). The coefficient of a corner indexed by $N\cup A$ is
$\sum_{K:A\subseteq K\subseteq T\setminus N}(-1)^{|K|-|A|}$, which is zero unless $A=T\setminus N$, when it is one: pair subsets differing in any remaining cube. The subtracted zero value occurs only for $K=\varnothing$. This proves (33). Component locality permits removal of zero terms. Holomorphy, Borel dependence and covariance pass through finite sums. ∎

The unshifted summand in (33) retains its bound $b_f$. The total new bound is at most $b_f+\sum_Y|V_f(Y)|$. A bound on that sum, its summability over stages, or the stored-field exponential mass in SA 18108–18128 is an NL1/LF1 input. Exact resummation alone proves none of them.

## 6. Application to the actual stages

**Outstanding — the source level and the no-new-mark margin.** A stage of the operation at level $t$ has source level $j=t-N_t+n$, not necessarily $t-1$. Its source collar is $R_n=Z_{j+1}\setminus Z''_{j+1}$ (SA 17612–17624; CA-I 53806–53814). No stated geometric fact puts all its changed-row carriers in ambient layers at least $t-1$. Thus the distance estimate in draft Corollary E′ does not follow.

For example, at a source carrier in layer $m=j<t$, the profile (11) is
\[
 w(j)={\theta_s\beta_s\alpha_0\varepsilon_j\over4N_t}
                         2^{-(t-j)}.
\]
The bound (S), at distance zero, therefore gives only
\[
 {C_{\rm src}C_{\mathcal A}\delta'_j\over w(j)}
 ={4C_{\rm src}C_{\mathcal A}\over\theta_s\beta_s\alpha_0}
       N_t2^{t-j}{\delta'_j\over\varepsilon_j}.
 \tag{34}
\]
This is a bound supplied by that argument, not a lower bound on the actual response. It diagnoses a missing estimate, not a counterexample. In the first stage, $t-j=N_t$. The proposed condition $N_t^{3/2}(\log\theta_t)^{-(\mathfrak p_0-\mathfrak p_1)}\ll1$ does not control (34). In particular, a waiting depth growing as a positive power of $\log\theta$ permits $2^{N_t}$ to dominate every fixed logarithmic saving. A possible additional $N_t^{1/2}$ RUN loss does not help. Nor may one use $x_j\ge x_t$ for an arbitrary frame history: SA 19410 uses the running minimum of the frame. To close this step one needs the actual carrier geometry and a stronger response-to-gap estimate, or a different coefficient table with all consumer comparisons proved. Simply relabelling $t$ as $j$ changes the design. This failure can already occur in the argument for disjoint collars.

**Outstanding — changing reads and full-radius gaps.** The tower in L3 uses the current determining sequence intersected with its erosion sequence. Enlarging a determining member changes that function. Estimate (T) compares two inputs to one function; it does not compare two different determining systems. The draft's nesting lemma and Theorem E omit this distinction. The same issue applies to remade levels, lifts, eroded read sets and gauge-cube families. Proposition 5 supplies witnesses at a real background only; it does not supply a newly required witness at every complex-domain point's real factor.

There is also an arithmetic gap in the truncated-layer argument. The draft bounds a smaller radius by
\[
 {5\over4}C_{\rm run}(1+\sqrt\nu)2^{-\nu}
                  L^{-(p-1)\nu}
\]
 times the comparison radius. At $p=\nu=1$ this factor is $5C_{\rm run}/4\ge5/4$, independently of $L$. It cannot imply the claimed $3/8$ positive gap. YM3 55989–56000 uses a different bound without this added RUN factor. Definition 4 requires the actual full-radius comparison, including every truncation and lift; it is not replaced by the scalar identity (20) or (21). The phase-$N_t$ to output transition also needs this comparison, since its phase weight is still $1/2$.

**Lemma 9 (OS: overlapping-collar input).** For the actual stages with overlapping collars, BG, PROF, AV and DR hold on their admitted determining systems with constants uniform in the number of overlaps, cutoff and volume. The ambient estimate (T) and the pinning/domain estimates used in Theorem 1 hold on the recorded meet towers and read neighborhoods, with their stated lifts and unit conversions. Together with verified compatible-read comparisons and the **actual** source budget (12), these estimates imply the conclusions of Theorem 1 at those stages.

*Proof.* **Outstanding.** No proof of the uniform analytic estimates on this specific geometry is supplied here. Conditional on them and the explicitly separate comparisons and budget, apply Propositions 5–7 and Lemma 8. OS does not assert, or repair, those separate comparisons or budget.

The draft's proposed reasons for failure of OS need correction. SA 9776 and 17398–17401 expressly give separation of stage sequences; SA 17624 describes overlap of collars belonging to different stages. These are different assertions. Overlap alone neither defeats the strip argument of Lemma 2 nor proves that many constraint-row levels meet at one site. Likewise, SA 9987–9997 counts the actual reduced-datum interactions: one finer block contributes $O(L^4)$ rows and is incident to at most eight coarse rows. SA 9998–10001 explicitly distinguishes that calculation from a right inverse of all field constraints. It cannot support the draft's alleged right-inverse obstruction. The defining equation for $k_\sharp$ in SA 17624 involves the running depth at $k_\sharp+1$; the exact equality “number of overlaps $=\log_L N_t$” needs an additional comparison. Finally, the lift trade $L_\flat^2/L^2<1/4$ is a real-test comparison; by itself it proves no complex response or tower-map comparison. These observations leave OS open without endorsing the draft's three failed-attack diagnoses.

For (LOC), the inner and removed cores in SA 5813–5826 are two separate substitution problems. Their interpolation radii must each satisfy (12); they are not the curvature and potential radii $r_0,r_1$. Pair covariance follows only for activities supplied as pair functions, or with the needed tie continuation supplied by LEV. The real tie alone does not establish that continuation. B4 and the stored-field mass bound also need the activity construction and summability stated after Lemma 8. Thus no complete B4 or LF-mass conclusion is asserted here.

### Source concordance

All line numbers below refer to the three files at the credited commit, fetched once. These entries record the draft's mislocated quotations and the substantive source checks; they introduce no extra imports.

| Draft citation or assertion | Correct location and reading |
|---|---|
| SA 6150–6153 for the warning that inclusions are analytic hypotheses | SA **6155–6158**. The definition starts at 6150. |
| SA 6116–6118 for the after-$n$ phase weight | SA **6117–6121**. The coefficient formula is 6124–6135; lifts and the separate initial/unfinished tables are 6137–6148. |
| SA 6158 for the stored gauge law; 6155–6173 for stored variables | The gauge law is **6160–6162**; stored ranges, near/far dependence, switches and tie are **6160–6173**. |
| YM3 56330–56340 for the substituted composition | Composition **56309–56318**; restricted substitution **56319–56323**. Lines 56330–56334 define the localized excess; 56336–56338 specify the starred subtraction. |
| YM3 56461–56463 for the tie | The real tie hypothesis is **56442–56444**; its preservation is asserted at **56454–56457**. Proposition II-104-17 is **56432–56470**; its proof is **56472–56757** and uses forced levelling and a common-center argument. |
| YM3 real admission, ambient towers, shift and identification | Proposition II-90-39 at 53024, II-90-62 at 53427, I-95-61 at 55600, I-95-81 at 55869, II-93-26 at 53737, and II-93-38 at 54530 have the stated subjects. Their checked ranges are 52979–53920, 54441–54626 and 55448–55930. Their hypotheses must travel with the labels. |
| YM3 local substitution and pinned levelling | II-88-43 at 56023 and II-88-50 at 56230 are correctly identified. Read 55931–56283 with the outer-core hypotheses at 42287–42325. II-85-34 at **54729–54787** makes holomorphy conditional on levelled endpoints; its proof is 54788–55124. The source-cube preparation at **53922–54090** is also needed. |
| SA background, response and consumers | 9913 does require a boundary within one layer, in the mechanism at 9907–9916. The four-dimensional ambient statement is 9755, within 9746–9791. Critical response is 5800–5803 and 10446–10464. B4 is 4006–4012; the core/interpolation/bracket definitions are 5663–5861. The majorant at 18108–18128 places the domain suprema inside the stored-field integral. None supplies the missing stage comparisons. |
| CA-I collar reconstruction and scope | **54287** does require the actual $(A_j,B_j)$ reconstruction. **49495–49546** places the background supply outside the implication; **54986–54994** assumes the stage theorem. These are assumptions or instructions, not supplied proofs. The four gauge families are 48527–48565. Retained lower rows involve $\mathcal B_p\cup\Gamma_i$ at 9840–9848 and 9953–9965, so an abstract layer label alone does not identify the physical changed rows. |
| SA stages, thresholds and constant order | 17255–17259 gives the main thresholds. 17415–17440 distinguishes retained stages and marks; at most one drop-out at a point and level does not bound the total number of drop-outs. 17550–17564 writes retained terms in the new variables. 17612–17630 gives actual stage levels and overlap/lift tests. 19408–19410 uses the frame and its running minimum; 19463–19473 orders constants with the coupling ceiling last. |

## Result

The distilled ST1 proves the elementary coefficient, geometric, logarithmic and tube estimates, and the precise conditional implication ST1*: verified compatible domains and response-to-gap bounds imply half-gap admission, physical identification, localized re-expansion and finite nested (D4). It does **not** establish those application hypotheses for every actual stage. In particular, the source-level error, changing-tower comparison and truncated-radius gap remain **Outstanding** even without overlapping collars.

The one named open lemma is **OS**. The open four-dimensional imports **CRIT**, **pinned levelling (LEV)** and **outer-core substitution (CORE)** remain explicit. BG, AV, PROF, DR, GEO, FL, RUN and the NL1/LF1 activity package are hypotheses with the domains stated in Section 3; (T), real gauge admission, actual reconstruction and the budgets still require the verifications identified in place. None is promoted to a theorem by a citation to YM3.

Corrections to the draft, grouped by the statement affected:

1. **Definitions and real admission:** supplied units, normalized differences, current/boundary convention, metrics, row/pillar/erosion data, fixed formation records, full core clauses, the missing containing-cube gauges, four CA-I gauge families, stored-coordinate/tie conventions and intrinsic tube topology. Removed the claim that every real factor is critical. Separated the initial and unfinished radius tables from the simplified design.
2. **Nesting and towers:** limited coefficient nesting to identical read functions and witnesses; exposed changed determining maps, lifts and gauge rosters. Made the missing four-dimensional second-order/gauge estimates behind (T) explicit. Ambient meets avoid the particular reversed-scale estimate; they do not make every counterexample datum or consumer read automatically admissible.
3. **Coefficient and profile arithmetic:** used the mark set and disjoint waiting windows, with total mark weight at most three; retained RUN constants; included the last half-phase-to-output gap; rejected the draft's truncated-radius estimate.
4. **Elementary substitutions:** inserted the mesh denominator in $\nabla$, restricted conjugation claims to common logarithm branches, repaired the inconsistent plaquette smallness premise, and gave a hand proof with an explicit curvature constant. Recorded the weaker constants relative to YM3 and their fixed smallness cost.
5. **Actual shifts and constants:** restored the preparatory source level, its missing $2^{t-j}$ budget, amplitude dependence and full complex-contour requirement. Replaced the unsupported (N-growth) conclusion by (12), distinguished frame from density weights, required an actual polynomial lift bound, and restored all core, source and gauge ceilings. The order of choice no longer chooses $L$ against an unspecified possibly $L$-dependent $C_{\rm run}$.
6. **Physical identification and returns:** restricted the boundary-current correction to its supported rows, corrected the four-dimensional star count, and exposed the actual collar reconstruction. Restored endpoint levelling, the profile loss in pinning, the current term $\operatorname{Ad}u\,\mathbf J-\mathbf J$, stored pinnability and complex-tie continuation. No pointwise gauge bound is substituted for a derivative estimate.
7. **Consumers and composition:** separated inner/removed interpolation radii from $r_0,r_1$; used nested substitutions rather than adding noncommutative shifts; retained the unshifted summand without claiming an unchanged total mass. B4, polymer summability and LF-mass require their additional inputs.
8. **OS and sources:** corrected overlap versus sequence separation, the reduced-datum row-count interpretation and the unsupported exact overlap count; kept OS open. Corrected the mislocated source lines listed above and read the previously second-hand CA-I and SA passages and the needed YM3 proofs.

This is research text, grants no status, and is **not yet refereed**.
