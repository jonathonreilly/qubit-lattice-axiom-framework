# Repo search

**GUIDE.** At `e063df811` the target-specific prior file is absent. The lead's 8 November search covers main and PRs 10114, 10133, 10134 and 10141. It concerns thirteen UV problems. The closest soft-route hit, PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md` at `f76f6c649c`, lines 73–149 and 315–343, gives a one-step Wilson-loop estimate and a contraction at bare coupling at most 1/32. Neither passage estimates the weak-coupling periodic partition function. The digest identifies PR 10141 as a snapshot. The cited main result on finite-clock Villain covariance (14 September, lines 4 and 79–94) uses a different, abelian measure. My search of the YM paths on these five refs also located the Chatterjee citation in PR 10114's `PANEL_P3.md`, line 64, used in §7.

**GUIDE.** The direct predecessors are row 720, `gap-phys-seed.md`, lines 416 and 451, which asks for the logarithmic asymptotic of the fixed-lattice doubling defect, and row 1028, `gap-uv-rigidity-max.md`, §4.1. Claude Fable's Lemma FV there gives a pressure upper bound, a comb tree gauge and a lower bound for the excess. It predicts a further log-log term and leaves the matching upper bound open. Row 1008, `gap-outside-box-check.md`, lines 419–422, gives a dimension count for the one-plane twist. I use row 1028's tree gauge and interior plaquette shelling. Its pressure upper bound checks the bulk normalization. The proposed coefficients and the attribution in row 1028 to work of Krauth and Staudacher on the quartic integral predate this note. The council brief, synthesis, gap part, FINISH results and open registry give no competing assignment for the missing two-sided estimate.

## Plan and target

**GUIDE.** Row 1143, based on `e063df811`. The plan was to determine the weak-coupling torus excess, compare the finite-cube and bulk plaquette shifts, and test the spectral seed on all electric fluxes. PROVED labels the hand arguments in this research note. Independent mathematical review is pending.

**GUIDE.** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, use Balaban's renormalization group for the ultraviolet construction. At source revision `31a47c543775`, the outline gives the Wilson measure at lines 238–270 and distinguishes the flat constrained estimate from the physical spectrum at 9568–9577. CA-I states the spectral scope at 2700–2712. The estimates below start directly from the Wilson integral. Credit for the small-volume flat-connection analysis also belongs to Lüscher and van Baal, as discussed in the lane’s `prior/gap-small-volume-lit.md`.

**OPEN.** The Jaffe–Witten target here is a nontrivial four-dimensional $SU(2)$ Yang–Mills theory with a positive gap above its vacuum. In row 720 write $F_\beta(n)=\log Z_\beta(n^4)$, $f_\beta$ for the bulk log partition function per site, and $D_\beta(n)=F_\beta(n)-n^4f_\beta$. On the common physical grid $\mathcal P=\{2^i\ell_1:i\ge0\}$, with $\ell_1/(4a_j)$ an integer at least three eventually, put $n_j=L/a_j$, $D^+(L)=\limsup_jD_{\beta_j}(n_j)$ and $z^-(L)=\liminf_j n_j\log(\lambda_0/\lambda_1)$ for the periodic spatial cube. The second eigenvalue is taken over all eight electric-flux sectors. Wall (W) requires one bound $D^+(L)\le D_0$ on the entire tail $L\ge L_0$ and one size $L\ge4L_0$ there with $z^-(L)>256D_0+30$. The fixed-lattice question below concerns the opposite end of the scale range.

**GUIDE — main result.** Equations (13) and (17) give the sign of the excess derivative and the constant remainder in the excess at fixed lattice side. Equation (10) controls the seven charged energies on growing cubes with $n^2=o(\beta)$. Section 8 compares these ranges with the size required in (W).

## 1. Separating the winding holonomies at finite cutoff

**PROVED — a comparison uniform in the shape.** Take a rectangular periodic lattice of sides $n_1,\ldots,n_4\ge3$, volume $V=\prod n_i$, and $M=3V-3$. Put $Q=\max_{i<j}n_i n_j$. For $u\in SU(2)$ write $a(u)=1-\tfrac12\operatorname{tr}u=|u-1|^2/2$, where $|\cdot|$ is quaternion length. For signs $\epsilon_{ij}=\pm1$, insert $\epsilon_{ij}$ on the $ij$ plaquettes at $x_i=n_i-1$, $x_j=n_j-1$, with the other two coordinates arbitrary. Denote the resulting partition function by $Z_\epsilon$. The all-plus choice is the periodic model in (W). With normalized Haar measures define
$$
 I(s)=\int e^{-s a(u)}\,du,\qquad
 J_\epsilon(s)=\int_{SU(2)^4}
       e^{-s\sum_{i<j}a(\epsilon_{ij}[h_i,h_j])}\,dh .
$$
Here $[h,k]=hkh^{-1}k^{-1}$. At every $\beta\ge0$,
$$
 I(30\beta)^M J_\epsilon(5Q\beta)
 \ \le\ Z_\epsilon\ \le I(\beta/2)^M J_\epsilon(\beta/(2Q)).                                      \tag{1}
$$

**PROVED — proof of the lower bound.** Use row 1028's comb tree. It consists of nonwrapping $i$-edges at sites with all coordinates below $i$ zero. Reducing coordinates in increasing order joins every vertex to the root by a unique parent path. Fix these $V-1$ links to one. As in row 1028, conditional on the old tree links, left and right multiplication by the tree transports preserves Haar on every other link. There is no residual gauge-volume factor. Keep $h_i$ on the wrapping $i$-edge with transverse coordinates zero. Define $B_e(h)=1$ on interior edges and $B_e(h)=h_i$ on every wrapping $i$-edge. The other $M=4V-(V-1)-4$ variables are $Y_e=U_eB_e(h)^{-1}$ with product Haar given $h$. Put $Y_e=1$ on the tree and the four kept edges. A plaquette of $B$ has product one unless it wraps in both directions, where it has product $[h_i,h_j]$ in the positive $ij$ orientation. Each pair has at most $Q$ such plaquettes. Telescoping the four unitary factors of a plaquette gives
$$
 |\epsilon_p U_p-1|\le |\epsilon_p B_p-1|+\sum_{e\in\partial p}|Y_e-1|.
$$
Square using Cauchy–Schwarz on the five terms. Each edge occurs in six plaquettes, so the signed action is bounded above by $30\sum_e a(Y_e)+5Q\sum_{i<j}a(\epsilon_{ij}[h_i,h_j])$. Integration gives the left side of (1).

**PROVED — the independent plaquette coordinates for the upper bound.** For each interior nontree edge $e=(x,i)$ take the least $k<i$ with $x_k>0$. Use the $ki$ plaquette based at $x-e_k$. Its two $k$-edges are tree edges, and the other $i$-edge has coordinate sum one lower. This is the interior shelling of row 1028. Next, for each wrapping $i$-edge except the kept $h_i$, take the least $k\ne i$ with $x_k>0$ and the $ki$ plaquette based at $x-e_k$. The two $k$-edges are interior and the preceding wrapping $i$-edge has transverse coordinate sum one lower. Order interior edges first by increasing coordinate sum, then wrapping edges by increasing transverse coordinate sum. Each selected plaquette contains its own pivot once, all its other variables are known when that pivot is reached, and it wraps in at most one direction. Interior faces have their pivot in the larger coordinate direction. A selected wrapping face identifies the wrapping direction and then its unique upper transverse edge. Thus the $M$ faces are distinct and every sign on them is positive. Replacing each pivot by its selected plaquette product is a triangular Haar-preserving bijection conditional on $h$, since each replacement is a left and right translate of the pivot or its inverse. The signed action $A_\epsilon$ is at least the sum of the $M$ selected plaquette actions.

**PROVED — the winding constraint in the opposite inequality.** In the fundamental $ij$ rectangle of side lengths $n_i,n_j$ based at the root, the outer boundary transport is $[h_i,h_j]$ in tree gauge. The other coordinates are zero. Unfold the rectangle in the universal cover. Add plaquettes row by row starting from a corner. At each addition the boundary word changes by a conjugate of the added face word, since the shared boundary arc is replaced by its other three edges, or by the complementary two edges. Equivalently, insert that face word at the shared arc's starting vertex, conjugated by the boundary path to it, and cancel reversed edges. This proves the boundary product formula, including after the links are identified on the torus. The product of the central face signs on this rectangle is $\epsilon_{ij}$. The triangle inequality and then Cauchy–Schwarz give
$$
 a(\epsilon_{ij}[h_i,h_j])
 \le n_i n_j\sum_{p\text{ in the rectangle}} a(\epsilon_p U_p).
$$
Different coordinate pairs use different plaquette orientations and hence disjoint plaquette sets. Thus $A_\epsilon\ge Q^{-1}\sum_{i<j}a(\epsilon_{ij}[h_i,h_j])$. Average this bound with the selected-face bound, then integrate in the independent plaquette coordinates. This gives the right side of (1).

## 2. The four-holonomy integral

**PROVED — periodic signs.** There are absolute positive constants $c,C$ with
$$
 c\,\frac{\log(2+s)}{(1+s)^3}\ \le J_+(s)\le C\,\frac{\log(2+s)}{(1+s)^3}\qquad(s\ge0).                      \tag{2}
$$
Throughout this proof $X\asymp Y$ means bounds by positive absolute multiples in both directions. For a unit quaternion $h=(x,u)$ with vector part $u\in\mathbb R^3$, quaternion multiplication gives $hk-kh=(0,2u\times v)$ for $k=(y,v)$. Hence $a([h,k])=2|u\times v|^2$. The radius $r=|u|$ has Haar density $w(r)=4r^2/(\pi\sqrt{1-r^2})$ on $(0,1)$, with uniform independent direction on $S^2$. This follows by writing $h=(\cos t,\omega\sin t)$ with angle density $2\sin^2t/\pi$ and adding the two preimages of $r$.

**PROVED — comparison near the commuting configurations.** Choose $u_1$ of largest radius $r$, multiplying the integral by four after restricting to that choice. Ties have measure zero. Write $e=u_1/r$ and $u_j=\alpha_j e+v_j$, $v_j\perp e$, for $2\le j\le4$. For the three pairs including $u_1$ the sum of squared cross products is $r^2\sum|v_j|^2$. For the other pairs use $|u_j\times u_k|\le r(|v_j|+|v_k|)$. Thus the full sum is between $r^2\sum|v_j|^2$ and five times that value. At radius $v$ the cosine of the angle to $e$ is uniform on $[-1,1]$. For $b\ge0$,
$$
 \int_0^1 e^{-b(1-y^2)}dy\asymp(1+b)^{-1}.
$$
Indeed $1-y\le1-y^2\le2(1-y)$, and integrating the two exponentials gives the claim, including its value at $b=0$. All three angular integrations now factor between the upper and lower comparisons. It follows that
$$
 J_+(s)\asymp \int_0^1 w(r)
    \left[\int_0^r \frac{w(v)}{1+sr^2v^2}\,dv\right]^3 dr.
$$

**PROVED — the logarithm.** The inner integral is comparable to $r^3/(1+sr^4)$. For the lower bound integrate over $r/2\le v\le r$. For the upper bound, dropping the denominator gives $C r^3$ by $v=rt$ and $(1-r^2t^2)^{-1/2}\le(1-t^2)^{-1/2}$. Using the denominator $sr^2v^2$ instead gives $C/(sr)$ by the same substitution. These bounds give
$$
 J_+(s)\asymp\int_0^1
       \frac{r^{11}\,dr}{\sqrt{1-r^2}(1+sr^4)^3}.
$$
For $s\ge32$, the part $r\le1/2$ is comparable to $s^{-3}\int_0^{s/16} x^2(1+x)^{-3}dx$ by $x=sr^4$. For $x\ge1$ the integrand lies between $1/(8x)$ and $1/x$. This part is comparable to $s^{-3}\log(2+s)$. The part $r\ge1/2$ is at most $C s^{-3}\int_{1/2}^1(1-r^2)^{-1/2}dr$. On $0\le s\le32$ the continuous positive integral and the right side of (2) are bounded above and away from zero. This proves (2), including the borderline logarithm.

**PROVED — a single twisted plane.** For exactly one negative sign, taken in the 12 plane, one has
$$
 J_\epsilon(s)\asymp(1+s)^{-9/2}.                                  \tag{3}
$$
Indeed the 12 action is $2(1-|u_1\times u_2|^2)$. It vanishes precisely when $x_1=x_2=0$ and $u_1\perp u_2$. The 13, 23, 14 and 24 actions then require $u_3=u_4=0$. Take a neighbourhood $|x_1|,|x_2|<1/4$, $|y|<1/2$, $|u_3|,|u_4|<1/4$, where $y$ is the cosine between $u_1,u_2$. Its complement has energy bounded below by a positive constant by compactness, since it contains no zero. The 12 term divided by two is
$$
 x_1^2+x_2^2-x_1^2x_2^2+(1-x_1^2)(1-x_2^2)y^2
 \asymp x_1^2+x_2^2+y^2.
$$
For any $v$, the sum $|u_1\times v|^2+|u_2\times v|^2$ lies between absolute positive multiples of $|v|^2$ on this set. In fact the sum of the projections on the two unit directions has top eigenvalue $1+|y|$, as seen by adding and subtracting the unit vectors. Subtract it from $2I$ and use $|u_i|^2\ge15/16$. The 34 action is bounded above by $2|u_3|^2|u_4|^2$. Thus all the action is comparable to $x_1^2+x_2^2+y^2+|u_3|^2+|u_4|^2$. The marginal densities of the first two scalars are $2\sqrt{1-x_i^2}/\pi$, the third has density $1/2$, and each of $u_3,u_4$ has a density proportional to $(1-|u|^2)^{-1/2}$ on its ball, counting both quaternion scalar signs. They give bounded positive factors. Gaussian integration in these nine coordinates bounds the neighbourhood integral above by $Cs^{-9/2}$ for $s\ge1$, and restriction to a ball of radius $1/(8\sqrt{s})$ bounds it below by $cs^{-9/2}$. The complement is exponentially small. Continuity covers $0\le s\le1$.

## 3. The excess, the doubling defect and the one-plane twist

**PROVED — uniform error estimates.** Write $B(\beta)=\tfrac32\log\beta+\log\log(2+\beta)$. For every rectangle as in §1 and $\beta\ge2$, the following estimates hold with an absolute constant $C$ common to both bounds.
$$
 \begin{aligned}
 \left|\log Z_+ + \tfrac92 V\log\beta-B(\beta)\right| &\le CV,\\
 \left|\log Z_\epsilon + \tfrac92 V\log\beta\right| &\le CV
       &&\text{(one twisted plane).}
 \end{aligned}                                                       \tag{4}
$$
Indeed $I(t)\asymp(1+t)^{-3/2}$. Use the Haar angle density from §2 and $2\theta^2/\pi^2\le1-\cos\theta\le\theta^2/2$ for $0\le\theta\le\pi$. The upper bound follows by integrating $C\theta^2 e^{-2t\theta^2/\pi^2}$, using $I(t)\le1$ near zero. The lower bound follows by restricting to $0\le\theta\le(1+t)^{-1/2}$ and $\sin\theta\ge2\theta/\pi$ there. Thus either link factor in (1) costs $\beta^{-3M/2}$ up to $e^{\pm CM}$. In the periodic case (2) gives an upper bound $C Q^3\beta^{-3}\log(2+\beta)$ at $t=\beta/(2Q)$ and a lower bound $c Q^{-3}\beta^{-3}\log(2+\beta)$ at $t=5Q\beta$. In the twisted case (3) gives the corresponding factors $C Q^{9/2}\beta^{-9/2}$ and $c Q^{-9/2}\beta^{-9/2}$. Since $Q\le V$ and $3M/2=(9V-9)/2$, taking logarithms proves (4).

**PROVED — bulk subtraction.** For the normalization in row 720, $f_\beta=\inf_{\boldsymbol n}V^{-1}\log Z_+(\boldsymbol n)$. The first inequality of (4) bounds every such quotient below by $-\tfrac92\log\beta-C$, because $B(\beta)>0$. Its upper bound on cubes of increasing side gives $f_\beta\le-\tfrac92\log\beta+C$, in agreement with the sharper upper constant in row 1028, §4.1(A4). Hence for every $n\ge3$ and every integer $\rho\ge2$,
$$
 \begin{aligned}
 |D_\beta(n)-B(\beta)| &\le 2C n^4,\\
 |\Phi_\rho(n)-(\rho^4-1)B(\beta)| &\le 2C\rho^4 n^4,\qquad
 \Phi_\rho(n)=\rho^4 F_\beta(n)-F_\beta(\rho n).
 \end{aligned}                                                       \tag{5}
$$
The second inequality uses (4) directly. At fixed $n$, the doubling defect is $\tfrac{45}{2}\log\beta+15\log\log\beta+O_n(1)$. This proves the fixed-lattice statement proposed in row 720, item 6. The one-plane twist costs
$$
 -\log(Z_\epsilon/Z_+)=\tfrac32\log\beta+\log\log\beta+O(V),         \tag{6}
$$
which proves the fixed-shape count in row 1008. The $O(V)$ constants in (4)–(6) are independent of the shape and coupling. In particular $D_\beta(n)/(\log\beta)\to3/2$ when $n^4=o(\log\beta)$, even along growing cubes. Observing the subleading coefficient one by (5) requires $n^4=o(\log\log\beta)$ or a fixed cube.

**OPEN — physical-size estimate.** At $n_j=L/a_j$ with $L>0$ fixed, the error in (5) is extensive in the number of fine sites. It can exceed both displayed logarithms. The shift from a fixed lattice to a fixed physical size in (BDD-Delta) therefore still requires new control of the finite-volume remainder.

## 4. A winding-state upper bound for the full cube gap

**PROVED — spectral conclusion.** There is an absolute $K>0$ such that a periodic spatial cube of any side $n\ge3$ obeys
$$
 m_\beta(n^3)\le m_{i,\beta}(n^3)
 \le -n\log(1-K/\beta)\le 2K n/\beta\qquad(\beta\ge\max(4,2K)).     \tag{7}
$$
Here $m_{i,\beta}$ is the bottom energy above the vacuum in the sector odd under the $i$-th centre flip and even under the other two. The estimate holds for each $i$. The energies in (7) are dimensionless lattice energies.

**GUIDE — provenance.** The transfer construction is due to Osterwalder–Seiler and Lüscher. I use the form in row 667, `gap-transfer.md`, §§1–3, 6, and the rectangular extension in rows 698–699. Sussman–Alpoge give the one-link Fourier coefficients at outline lines 2195–2231 and the gauge projection at 2313–2335. The reflection-positivity arguments for Wilson loops, static potentials and Polyakov lines are associated with Bachas and Borgs–Seiler, as recorded in `gap-brainstorm2-max.md`, line 470, and `gap-measured-vectors-max.md`, line 131. Here the charged trace comparison at a full turn gives a bound in the actual periodic transfer spectrum.

**PROVED — a local input uniform in both periods.** In any rectangular periodic box let $u=\langle\tfrac12\operatorname{tr}U_p\rangle$ for one fixed orientation. Translation invariance and $a\ge0$ give $V(1-u)\le\langle A\rangle_\beta$. Convexity of $F=\log Z_+$, with $F'=-\langle A\rangle_\beta$, gives
$$
 \langle A\rangle_\beta\le\frac{2}{\beta}\big(F(\beta/2)-F(\beta)\big)
 \le \frac{K V}{\beta}\qquad(\beta\ge4).
$$
For the last bound use (4) twice, $B(\beta/2)\le B(\beta)$, and absorb $\tfrac92\log2+2C$ into $K/2$. In particular $u\ge1-K/\beta$.

**PROVED — a rectangle as a positive moment.** Pick any lattice direction as transfer direction, with period $N$. In a transverse slice let $\gamma$ be an oriented path from $x$ to a different vertex $y$. Write $W_\gamma(k)$ for the expected half-trace around the ribbon formed by $\gamma$, its translate by $k$ steps, and the straight connectors. This includes $k=N$, when both copies of $\gamma$ lie on the same slice. On the full scalar slice Hilbert space use the ungauged positive transfer $B_*=e^{-V_s/2} C_{\mathcal E} e^{-V_s/2}$, where $V_s$ is the spatial Wilson action times $\beta$ and $C_{\mathcal E}$ is the product of one-link convolutions. It commutes with vertex gauges. Its restrictions below are positive compact trace-class operators. The one-link eigenvalues are strictly positive at $\beta>0$ by the positive Bessel series in outline (GL3), so these restrictions have no kernel.

**PROVED — the two restrictions.** Let $B_0$ be the transfer on invariant scalar functions and $B_{xy}$ the componentwise transfer on matrix functions satisfying $G(hU)=h_x G(U)h_y^{-1}$ for vertex gauges $h$, with matrix inner product $\tfrac12\operatorname{tr}(G^*H)$. The map $Jf(U)=U(\gamma) f(U)$ is an isometry from the first space into the second. Gauge averaging on the second space uses the color action $\sigma(h)A=h_x A h_y^{-1}$. If $b(U,V)$ is the ungauged kernel, the projected kernel is $\int b(U,hV)\sigma(h)\,dh$, as follows by changing $V$ to $hV$ in the projection integral. Multiplying these kernels along the $k$ steps between $J$ and $J^*$ transports the two color indices along the connectors. The normalized matrix inner product at $J^*$ takes the half-trace around the ribbon. The other steps have scalar gauge averaging. Thus, with $Z=\operatorname{Tr} B_0^N$,
$$
 W_\gamma(k)=Z^{-1}\operatorname{Tr}_0
   (B_0^{N-k}J^* B_{xy}^k J)\qquad(0\le k\le N).                    \tag{8}
$$
At $k=N$ multiplication by $U(\gamma)$ intertwines the scalar and color gauge actions. Consequently $J^*B_{xy}^{N}J$ already has a scalar gauge projection at the seam when written on the full space.

**PROVED — two uses of (8).** Use eigenbases $a,b$ of the two restrictions, with eigenvalues $\lambda_a,\mu_b$. The weights $Z^{-1}\lambda_a^N |\langle b,Ja\rangle|^2$ sum to one. Equation (8) is the $k$-th moment of $\mu_b/\lambda_a$ with these weights. Jensen gives $W_\gamma(k)\ge W_\gamma(1)^k$. At $k=N$ the inequality $JJ^*\le I$ gives $W_\gamma(N)\le Z^{-1}\operatorname{Tr}_{xy} B_{xy}^N$. In the latter trace the color character of the product of the temporal gauges is $\operatorname{tr}H_x\,\overline{\operatorname{tr}H_y}$, where $H_x,H_y$ wind in the chosen transfer direction. This follows directly by taking the ordinary four-dimensional trace of $A\mapsto H_x A H_y^{-1}$ on matrices. Thus the upper bound is $4\langle P_x P_y\rangle$, where $P=\tfrac12\operatorname{tr}H$ is real for $SU(2)$.

**PROVED — passage to the cube spectrum.** Give ordinary time a finite period $T>t$, $T\ge3$. Take $N=n$ in spatial direction $i$ and let $\gamma$ join ordinary times $0,t$ along a straight time line. The preceding paragraph bounds $4\langle P_0P_t\rangle$ below by the $n$-th power of the $1\times t$ rectangle expectation. Read that rectangle with ordinary time as transfer direction and with $\gamma$ now one spatial link. Equation (8) bounds its expectation below by $u^t$. Consequently $4\langle P_0P_t\rangle\ge (1-K/\beta)^{nt}$ for every $T>t$ in the range of (7). At fixed $\beta,n,t$ take $T\to\infty$. By row 667 §6 the limit is $\langle P\Omega,(T_{\rm cube}/\lambda_0)^t P\Omega\rangle$. The unique strictly positive vacuum is invariant under the three commuting centre flips, and $P\Omega$ has the specified single-odd flux. Its norm is at most one. Thus $4e^{-tm_{i,\beta}}\ge(1-K/\beta)^{nt}$. Taking the $t$-th root and letting $t\to\infty$ proves (7), using $-\log(1-x)\le2x$ for $0\le x\le1/2$.

**PROVED — sizes ruled out.** Along any bare sequence $\beta_j\to\infty$, $n_j^2=o(\beta_j)$ forces $n_j m_{\beta_j}(n_j^3)\to0$. The bound applies to the lowest excitation of the full cube because even one such flux sector furnishes a trial sector for it. In particular, obtaining a finite-cutoff dimensionless gap above 30 requires $n^2>15\beta/K$ in (7)'s range.

## 5. Simultaneous control of the seven charged sectors

**PROVED — a joint winding-loop moment.** Take the three straight spatial loops based at the same vertex and put $P_i=\tfrac12\operatorname{tr}H_i$. At any time on any periodic rectangle, for every subset $S\subseteq\{1,2,3\}$,
$$
 \left\langle\prod_{i\in S}P_i^2\right\rangle\ge 4^{-|S|}.             \tag{9}
$$
The bound also holds in the finite spatial cube's vacuum. At $\beta=0$ equality holds because disjoint sets of edges give independent Haar holonomies and each second moment is $1/4$. Row 765's Polyakov trial construction in `gap-fusion-astra.md`, §5.3, uses the same types of observables with a local density comparison. The estimate here is for their squared norm. That row also considers the distinct variance of their square.

**PROVED — conditioning by a positive insertion.** Fix $i\in S$. In transfer direction $i$, $G=\prod_{j\in S\setminus\{i\}}P_j^2$ is a nonnegative gauge-invariant multiplication operator on a single transverse slice because all the other loops lie in $x_i=0$. Take the adjoint color representation at the base vertex. The charged trace argument of §4, now with one adjoint color space, gives
$$
 Z\langle G\,\chi_{\rm adj}(H_i)\rangle
 =\operatorname{Tr}_{\rm adj}(M_G B_{\rm adj}^{n_i})\ge0 .
$$
When the projected kernels are multiplied, the color index at the base vertex gives precisely the character of the winding product in the trace. For the inequality one can sum the nonnegative diagonal entries of $M_G$ in an eigenbasis of $B_{\rm adj}^{n_i}$. For a fundamental $SU(2)$ matrix with eigenvalues $e^{\pm i\theta}$, the adjoint character is $1+2\cos 2\theta$, so $4P_i^2=1+\chi_{\rm adj}(H_i)$. This gives $\langle G P_i^2\rangle\ge\langle G\rangle/4$. Successively remove the elements of $S$ and use the cylinder limit of the bounded slice observable to obtain (9).

**PROVED — excitation in each prescribed sector.** Work in the coupling range of (7). For a nonzero electric character $e$, let $S$ be the set of its nonzero bits, $k=|S|$, and $F_e=\prod_{i\in S}P_i$. It transforms in precisely that sector. At adjacent times, parallel transport the upper loop's base point to the lower one along the time bond. If $H,H'$ are these based holonomies in direction $i$, then
$$
 |P_i(1)-P_i(0)|^2\le |H'-H|^2
 =2\left(1-\tfrac12\operatorname{tr}(H^*H')\right).
$$
The half-trace on the right is the winding $n\times1$ ribbon of §4. Its expectation is at least $(1-K/\beta)^n$ by (8). Since $|P_i|\le1$, telescoping the product, squaring and taking expectations gives
$$
 \langle |F_e(1)-F_e(0)|^2\rangle
 \le 2k^2[1-(1-K/\beta)^n]\le 2k^2 K n/\beta .
$$
Pass to infinite ordinary time at fixed cube. If $r_e$ is the top transfer eigenvalue in sector $e$ divided by the vacuum eigenvalue, then the left side is at least $2(1-r_e)\|F_e\Omega\|^2$. Equation (9) therefore gives
$$
 1-r_e\le 4^k k^2 K n/\beta.                                         \tag{10}
$$
Each of the seven subspaces has a nonzero test vector by (9). In the range $4^k k^2 K n/\beta\le1/2$, its bottom energy $-\log r_e$ is at most $2\cdot4^k k^2 K n/\beta$. Thus if $n^2=o(\beta)$, all seven charged bottom energies in units $1/n$ tend to zero together. This rules out a seed throughout that weak-coupling range even if there is a positive gap inside the neutral sector.

## 6. A positive finite-volume plaquette shift

**PROVED — sharp asymptotic at fixed lattice size.** For each fixed rectangle there are $c_{\boldsymbol n}>0$ and, for a single twisted plane, $d_{\boldsymbol n}>0$, such that
$$
 Z_+(\beta)\sim c_{\boldsymbol n}\,\beta^{-(9V-3)/2}\log\beta,
 \qquad
 Z_\epsilon(\beta)\sim d_{\boldsymbol n}\,\beta^{-9V/2}.              \tag{11}
$$
The limits in (11) give information about coupling derivatives which the bounded log errors in (4) alone cannot give.

**PROVED — rescaling the periodic integral.** Use the upper-bound coordinates in §1, calling the selected face variables $p_e$. Reconstruction is by finite words in $p_e,h_i$ and inverses. At $p_e=1$ it gives exactly $B(h)$, because all its selected plaquettes are one and the word reconstruction is unique. Multiplying any $h_i$ by $-1$ multiplies all wrapping $i$-edges by $-1$ at fixed $p_e$. This preserves every face word. We can consequently restrict the four quaternion scalar parts to their positive hemispheres and sum the identical sign branches.

**PROVED.** Split according to which vector part has largest radius $r$. Present the case of index one, with relabelling for the other choices. The bounds in (1) hold with an indicator in $h$ inserted on both sides, by the same conditional integrations. The contribution from $r\le\beta^{-1/4}$ is $O_{\boldsymbol n}(\beta^{-(9V-3)/2})$ because the four small three-balls have joint measure $O(\beta^{-3})$ and the selected faces give the remaining $O_{\boldsymbol n}(\beta^{-3M/2})$. The contribution from $r\ge1/2$ has the same bound by the outer-integral estimate in §2 with $s=\beta/(2Q)$. These two pieces vanish in the normalization of (11).

**PROVED.** In the remaining region set $r=\beta^{-v}$ and $u_1=r e$ for $e\in S^2$. Set $b_1=1$, $w_1=0$. For $j=2,3,4$ use
$$
 u_j=r b_j e+(\sqrt\beta\,r)^{-1} w_j,\qquad
 w_j\in e^\perp,\qquad b_j^2+|w_j|^2/(\beta r^4)\le1 .
$$
Lebesgue measure on the four vector parts becomes $\beta^{-3}(\log\beta)\,dv\,de\,\prod_{j=2}^4 db_j\,d^2w_j$. Indeed $u_1$ gives $r^2dr\,de$, and each other vector contributes $\beta^{-1}/r$. The four Haar density factors, apart from their fixed normalization, are $(1-|u_j|^2)^{-1/2}$. They stay bounded since $r\le1/2$. Simultaneous conjugation allows $e$ to be fixed in this integral with its sphere-area factor. Put $p_e=\exp(\xi_e/\sqrt\beta)$ for $|\xi_e|<\pi\sqrt\beta$ in the imaginary quaternions. The omitted antipodal points have Haar measure zero. Each Haar measure is a constant times $\beta^{-3/2}[\sin(|\xi_e|/\sqrt\beta)/(|\xi_e|/\sqrt\beta)]^2d^3\xi_e$.

**PROVED.** For $0<v<1/4$, fixed finite $\xi,w$ and $|b_j|<1$, all domains eventually include the point, $r\to0$ and $\sqrt\beta\,r^2\to\infty$. Off this $v$ interval or outside $|b_j|\le1$ the limiting indicator is zero, up to endpoints of measure zero. Each face has a limiting scaled displacement $\sqrt\beta(U_p-1)$. Variation of its word in the selected faces contributes its ordinary first derivative at $p_e=h_i=1$, applied to $(\xi_e)$. This follows by integrating the derivative along $p_e(t)=\exp(t\xi_e/\sqrt\beta)$ and using continuity of the finite word's derivative. At $p_e=1$ its displacement is zero except on double seams. On an $ij$ double seam the identity $[h_i,h_j]-1=(h_i h_j-h_j h_i)h_i^{-1}h_j^{-1}$ gives limit $2e\times(b_i w_j-b_j w_i)$ since $w_i\times w_j/(\sqrt\beta r^2)\to0$. Hence $\beta A$ converges pointwise to half the sum of squared limiting displacements.

**PROVED.** The action bounds preceding (1) furnish an integrable majorant after extracting $\beta^{-3M/2-3}\log\beta$. They give Gaussian decay in all $\xi_e$ since $\beta a(p_e)\ge2|\xi_e|^2/\pi^2$, and in all $w_j$ since $\beta a([h_1,h_j])=2|w_j|^2$. Their half-sum works simultaneously. The remaining domains $0\le v\le1/4$, $|b_j|\le1$ have finite measure. Dominated convergence gives a finite coefficient, strictly positive since the limiting exponential is positive on a set of positive measure. Summing the four maximum-index cases proves the first assertion of (11).

**PROVED — where the logarithm comes from in the Wilson measure.** For the largest vector radius $r$ of the four based holonomies on a fixed rectangle, $-\log r/\log\beta$ converges in law to the uniform distribution on $[0,1/4]$. Indeed, inserting any bounded continuous function of $v$ in the preceding proof leaves the majorant valid. The limiting integrand is independent of $v$ on this interval, and the two omitted radial ranges have vanishing normalized mass. Consequently the distance of the winding tuple from the set of sixteen central tuples tends to zero in probability. For each fixed radius threshold $r_0>0$, first bound $\Pr(r>r_0)$ by $\Pr(v<\delta)$ for large $\beta$, then let $\delta\downarrow0$. The four centre flips give equal probabilities to the sixteen disjoint equal-radius neighbourhoods.

**PROVED — twisted integral.** Outside the neighbourhood from the proof of (3), the holonomy integration in the full integral contributes $O_{\boldsymbol n}(I(\beta/2)^M e^{-c_{\boldsymbol n}\beta})$ by the upper-bound argument of (1). Inside that neighbourhood scale $(x_1,x_2,y,u_3,u_4)$ by $\beta^{-1/2}$, meaning that each original coordinate is its new coordinate divided by $\sqrt\beta$. Keep the direction of $u_1$ and the azimuth of $u_2$ about it. They range over a compact set with the usual sphere and circle measures. At $x_1=x_2=y=u_3=u_4=0$ the two directions are orthogonal, so this parametrization is smooth locally. Sum the two independent choices of scalar sign for $h_3,h_4$. Use the same $p_e=\exp(\xi_e/\sqrt\beta)$ as above. At the origin of these scaled fluctuations all signed plaquettes are one. Differentiability of each reconstructed word gives convergence of each $\sqrt\beta(\epsilon_p U_p-1)$ to its differential in the scaled variables. The half-sum action bounds in §1 and the quadratic comparison in §2 dominate the integrand by a Gaussian in the $3M+9$ fluctuating coordinates, with a constant depending only on the fixed shape. The Haar factors tend to strictly positive densities there. Dominated convergence again gives a strictly positive finite coefficient, proving the second assertion of (11).

**PROVED — sign of the size shift.** For a partition function with $Z(\beta)\sim c\beta^{-p}(\log\beta)^q$, $F=\log Z$ and $F''=\operatorname{Var}_\beta A\ge0$, one has $\beta F'(\beta)\to-p$. For any $b>1$, sandwich the derivative by the secants on $[\beta/b,\beta]$ and $[\beta,b\beta]$. After multiplying by $\beta$, their limits are $-p\log b/(1-1/b)$ and $-p\log b/(b-1)$, respectively. Both tend to $-p$ as $b\downarrow1$. Apply this separately to the two periodic volumes in $\Phi_\rho$ and to the two signs in (6). At fixed $n$ and $\rho$ this gives
$$
 \lim_{\beta\to\infty}\beta\,\partial_\beta\Phi_\rho(n)
       =\tfrac32(\rho^4-1),\qquad
 \lim_{\beta\to\infty}\beta\,\partial_\beta[-\log(Z_\epsilon/Z_+)]=\tfrac32 .
                                                                         \tag{12}
$$
Write $\bar a_n$ for the mean action of one plaquette on the symmetric torus. Then $\partial_\beta\Phi_\rho(n)=6\rho^4 n^4(\bar a_{\rho n}-\bar a_n)$. Equation (12) gives $\bar a_n<\bar a_{\rho n}$ for sufficiently large $\beta$ at each fixed $n,\rho$. The starting coupling for this sign can depend on both boxes.

## 7. The plaquette shift against the infinite lattice

**PROVED — fixed-size part of row 720's monotonicity condition.** For each fixed $n\ge3$, both one-sided derivatives obey
$$
 \lim_{\beta\to\infty}\beta\,\partial_{\beta,\pm}D_\beta(n)=\tfrac32.   \tag{13}
$$
In particular, $D_\beta(n)$ is eventually strictly increasing at each fixed $n$. The weak-coupling threshold in this implication can depend on $n$. The proof below controls a difference of bulk pressures at two couplings with the same Gaussian determinant.

**GUIDE — credit.** Weak-coupling free-energy comparison with Gaussian lattice fields is the subject of Sourav Chatterjee's *The leading term of the Yang–Mills free energy*, cited for $U(N)$ in the soft route's `PANEL_P3.md`, line 64 on PR 10114. We give the $SU(2)$ pressure comparison used here. Equation (13) combines the bulk derivative with the finite periodic calculation (11).

**PROVED — open box.** Let $b=\lceil(\log\beta)^2\rceil$ for sufficiently large $\beta$, and consider the open cube $\{0,\ldots,b-1\}^4$ with its internal links and plaquettes. Fix its comb tree. The number of remaining links is $m_b=4(b-1)b^3-(b^4-1)=3b^4-4b^3+1$. Allow a subset $S$ of these remaining links also to be fixed to one. Write $m=m_b-|S|$. Let $dX$ be the oriented sum of the four Lie algebra edges of a plaquette, with all fixed edge values zero. Write $K_S=d^*d$ on the $m$ free scalar edge coordinates, so the same matrix acts on each of the three color components.

**PROVED.** The interior shelling in §1 bounds, for numerical $c,C>0$,
$$
 c b^{-5}I\le K_S\le24I,\qquad
 \max_{e}|U_e-1|^2\le 8 b A_{\rm box}(U).                            \tag{14}
$$
For an interior nontree edge its selected plaquette has both transverse edges on the tree. Hence its distance from the preceding edge is the plaquette distance from one, and the corresponding linear difference is $\pm(dX)_p$. Follow predecessors until the tree is reached, in at most $4b$ distinct steps because coordinate sum decreases. Apply Cauchy–Schwarz and use that the sum of all squared plaquette distances is $2A_{\rm box}$. In the linear problem sum the resulting bound over at most $m_b\le3b^4$ free edges. The upper operator bound follows by squaring the four-term sum on each plaquette and counting at most six occurrences of each edge. The argument applies with the extra links fixed to one.

**PROVED — uniform Gaussian estimate.** Let $Z^{\rm open}_{b,S}(s)$ integrate the free edge variables after these fixings, and set $h_0=1/(2\pi^2)$, the normalized Haar density at zero in exponential coordinates. Uniformly for $s$ in any fixed interval $[c_1\beta,c_2\beta]$, $0<c_1<c_2$, and for these subsets $S$,
$$
 \log Z^{\rm open}_{b,S}(s)=\log G_{b,S}(s)+o(b^4),\qquad
 G_{b,S}(s)=h_0^m(2\pi/s)^{3m/2}(\det K_S)^{-3/2}.                 \tag{15}
$$
Put $\eta=\beta^{-1/4}$. Outside the set $U_e=\exp X_e$, $\max|X_e|\le\eta$ (using the shortest logarithm), (14) bounds the integral by $e^{-c s\eta^2/b}$ since $|e^X-1|\ge2|X|/\pi$ for $|X|\le\pi$. This is $o(G_{b,S}(s))$ because the upper eigenvalue bound in (14) gives $G_{b,S}(s)\ge(c' s^{-3/2})^m$, and $\beta^{1/2}/b\gg b^4\log\beta$.

**PROVED.** On the stated set, expansion of the four factors gives $U_p-1=(dX)_p+R_p$, with $|R_p|\le C\eta\sum_{e\in p}|X_e|$. Indeed, $|e^{\pm X}-1\mp X|\le e|X|^2$ for $|X|\le1$, and every product of at least two increments costs a further factor at most $C\eta$. Summing the squared remainders and using (14) gives $\|R\|_2\le C\eta b^{5/2}\|dX\|_2$. It follows that $A_{\rm box}$ is between $(1\pm\delta)\|dX\|_2^2/2$, with $\delta=C'\eta b^{5/2}=o(1)$. The product Haar Jacobian divided by $h_0^m$ is between $e^{-Cm\eta^2}$ and one by its sine formula. For either Gaussian of precision $s(1\pm\delta)K_S$, the probability that some $|X_e|>\eta$ is at most $Cmb^5/(s\eta^2)=o(1)$ by (14) and Markov's inequality. The full Gaussian integral changes by a factor $(1\pm\delta)^{-3m/2}$ when its precision is multiplied by $1\pm\delta$. These logarithmic errors are $o(b^4)$ and prove (15).

**PROVED — gluing the open boxes in the pressure.** Tile a periodic four-cube of side $kb$ by the open $b$-boxes with disjoint vertex sets ($k\ge3$). At each fixed $s$ its pressure density tends to $f_s$ as $k\to\infty$ because the transfer trace implies that $F/V$ decreases in each side since $(\operatorname{Tr}T^N)^{1/N}$ decreases in $N$. Thus these cubes approach the infimum over rectangles. Dropping crossing plaquettes bounds $f_s$ above by $b^{-4}\log Z^{\rm open}_{b,\varnothing}(s)$. For the reverse comparison, fix the comb in every box. Conditional on the original trees, this change of gauge preserves independent Haar measure on every remaining link, including links between boxes.

**PROVED.** Restrict each link joining boxes and each remaining link tangent to an outer face of a box to $|U_e-1|\le s^{-1}$. There are at most $C b^3$ such links per box, since each face contains at most $3b^3$ tangential links and there are eight faces, besides at most $4b^3$ outgoing crossing links. Each restriction has Haar measure at least $c s^{-3}$ by the angle density. Call the restricted internal edges $S$. Set all restricted variables to one in a comparison configuration $U^0$. Every crossing plaquette of $U^0$ is then one. A plaquette crossing one boundary has two joining links and two links on boundary faces, while one crossing two boundaries has four joining links. The internal action of $U^0$ factors over boxes. For $\varepsilon=s^{-1/4}$ the triangle inequality and $(v+w)^2\le(1+\varepsilon)v^2+(1+\varepsilon^{-1})w^2$ give
$$
 A(U)\le(1+\varepsilon)\sum_{\rm boxes}A_{\rm box}(U^0)
         + C(1+\varepsilon^{-1}) k^4 b^3 s^{-2}.
$$
Here the squared sum of restricted-edge errors on each face is at most four times the sum of their squares, and each restricted link touches at most six faces. Integrating gives
$$
 f_s\ge b^{-4}\log Z^{\rm open}_{b,S}(s(1+\varepsilon))
       -C(1+\log s)/b .
$$
For the determinant in (15), eliminating the free variables outside $S$ leaves a Schur complement on $S$. Its quadratic form is the minimum of the full form over those other variables at fixed values on $S$, so its eigenvalues are also in $[cb^{-5},24]$ by (14), using zero for the other variables for the upper bound. Block Gaussian elimination gives $|\log\det K_{\varnothing}-\log\det K_S|\le C|S|(1+\log b)$. Removing $|S|$ variables also changes the free normalization in (15) by $O(|S|(1+\log s))$, and changing $s$ to $s(1+\varepsilon)$ costs $O(b^4\varepsilon)$. Since $b\gg\log\beta$ and $|S|=O(b^3)$, the two pressure bounds yield
$$
 f_s=b^{-4}\log G_{b,\varnothing}(s)+o(1)
 \quad(c_1\beta\le s\le c_2\beta).
$$

**PROVED — cancellation and sign.** At $s=\beta$ and $s=t\beta$ for fixed $t>0$, use the very same $b$ just chosen from $\beta$. The determinant and Haar normalization cancel exactly in the difference. Thus
$$
 f_{t\beta}-f_\beta=-\frac{3m_b}{2b^4}\log t+o(1)
       \longrightarrow-\tfrac92\log t .
$$
The bulk pressure is convex as the pointwise limit of convex finite-cube pressures. Sandwich both its one-sided derivatives by the two secants used in §6. It follows that $\beta f'_{\beta,\pm}\to-9/2$. Subtraction from the fixed-cube derivative given by (11) proves (13). The excess is locally absolutely continuous on $(0,\infty)$ as a difference of finite convex functions. Its almost-everywhere derivative is positive beyond the fixed-box threshold in (13), so it is strictly increasing there.

**PROVED — quantitative bulk remainder.** There is a constant $c_\infty$ such that, for each $0<\alpha<1/12$,
$$
 f_\beta=-\tfrac92\log\beta+c_\infty+O_\alpha(\beta^{-\alpha}),
 \qquad
 \beta f'_{\beta,\pm}=-\tfrac92+O_\alpha(\beta^{-\alpha/2}).          \tag{16}
$$
Choose $\alpha<\gamma<1/12$ and repeat the comparison (14)–(15) with $b=\lceil\beta^\gamma\rceil$, $\eta=b^{-7/2}$. Uniformly for $\beta/2\le s\le4\beta$, the exponent controlling the exterior of the integration region is at least $c\beta/b^8$. This dominates $b^4\log\beta$, since $\beta/b^{12}\gg\log\beta$. The Gaussian restriction in (15) now follows from the one-dimensional Gaussian tail bound. Each scalar edge coordinate has variance at most $Cb^5/s$ by (14), also after multiplication of the precision by $1\pm\delta$ with $\delta=C\eta b^{5/2}=C/b$. A union bound on three coordinates per link gives probability at most $C b^4\exp(-c\beta/b^{12})$ that any edge logarithm has norm above $\eta$. This and the exterior error relative to $G$ decay faster than every inverse power of $\beta$. Per site the precision error is $O(1/b)$ and the Haar error is $O(\eta^2)$. The box comparison then gives $|f_s-b^{-4}\log G_{b,\varnothing}(s)|\le C(\log\beta)/b$ for $\beta\le s\le2\beta$, including the boundary and Schur-complement costs above.

**PROVED.** For $g(s)=f_s+\tfrac92\log s$, using the same $b$ for $s=\beta$ and $s=t\beta$ gives $\sup_{1\le t\le2}|g(t\beta)-g(\beta)|=O((\log\beta)/b)=O_\alpha(\beta^{-\alpha})$. Here $3-m_b/b^4=O(1/b)$. For any $s\ge\beta$, first double $\beta$ until $s$ is within a factor two, then use that last interval. The sum of the errors is bounded by $C_\alpha\beta^{-\alpha}\sum_{k\ge0}2^{-k\alpha}$. Thus $g$ has a finite limit $c_\infty$ with the asserted rate. Squeeze both bulk derivatives between secants over $[\beta(1-h),\beta]$ and $[\beta,\beta(1+h)]$. After multiplication by $\beta$, the error relative to $-9/2$ is $O_\alpha(h+\beta^{-\alpha}/h)$. Taking $h=\beta^{-\alpha/2}$ proves (16).

**PROVED — the constant in the excess.** With $c_{(n,n,n,n)}$ the positive coefficient from (11), for each fixed $n\ge3$,
$$
 \lim_{\beta\to\infty}
 \big[D_\beta(n)-\tfrac32\log\beta-\log\log\beta\big]
     =\log c_{(n,n,n,n)}-n^4c_\infty.                               \tag{17}
$$
This follows by subtracting $n^4$ times (16) from the logarithm of (11). Even for growing $n$, the error from the bulk term alone is $O_\alpha(n^4\beta^{-\alpha})$ for the excess and $O_\alpha(n^4\beta^{-\alpha/2})$ for its logarithmic coupling derivative. The error for the finite periodic integral in (11) still depends on $n$.

**OPEN — what remains of monotonicity.** Row 720's (MONO-Delta) requires a single starting coupling that works for every $n$. Equation (13) gives such a starting coupling for every finite list of sizes, by taking their maximum threshold. The growth rate of this list relative to $1/a_j$ is open. Equation (16) bounds the bulk error per site. Preserving the sign in (13) requires an error below its positive margin after subtracting two extensive derivatives in $\beta\,\partial_\beta F$.

## 8. The physical-size limit

**PROVED given the lane's ultraviolet input.** Write $b_{\rm RG}>1$ for the account's blocking factor. Its first-passage definitions at outline lines 6844–6861 give $a_j=b_{\rm RG}^{-K_j}$ and $x_0=\beta_j$. Under the drift and terminal bounds (RF25), lines 20781–20801, one has $\beta_j\le h+B_\sharp+B_\sharp K_j$ at fixed reference $h$. Thus $n_j=L b_{\rm RG}^{K_j}$ at any fixed physical $L>0$ eventually exceeds every fixed power of $\beta_j$. In (1) on such cubes the two arguments of $J$ are $\beta_j/(2n_j^2)\to0$ and $5n_j^2\beta_j\to\infty$. The two sides of the comparison probe different parts of that integral. In (13), taking the large-coupling limit at each fixed side does not supply a sign at these $n_j$. In (7), the upper bound on the dimensionless gap grows like $n_j^2/\beta_j$ and supplies no spectral lower bound.

**PROVED — group dependence of the finite-box result.** For $U(1)$ the untwisted four-commutator factor is identically one. For a finite subgroup it tends by finite summation to the positive fraction of commuting quadruples. Neither calculation has the logarithmic integration of §2. A product measure with a decoupled spectator multiplies partition functions and tensors transfer operators, so a low spectator excitation remains available in the product. These checks delimit the information the weak-coupling coefficients can give about the physical gap.

**OPEN.** The finite-box sign in (13) would have to hold with a common threshold across all box sizes to provide (MONO-Delta). A bound on $D^+(L)$ throughout the physical tail and a lower bound on its companion $z^-(L)$ at one sufficiently large physical size are both outstanding. The downstream implication used here is the lane's Theorem ZD-c, with the strict margin and domain repair recorded in `gap-zd-astra.md`, item 18.

RESULT — PROVED by hand for Wilson SU(2). At each fixed lattice side, $D_\beta(n)-\tfrac32\log\beta-\log\log\beta$ has a finite limit and $\beta\,\partial_{\beta,\pm}D_\beta(n)\to\tfrac32$. All seven charged bottom energies in units $1/n$ tend to zero when $n^2=o(\beta)$. OPEN — Wall (W) at fixed physical size and the Jaffe–Witten mass gap.
