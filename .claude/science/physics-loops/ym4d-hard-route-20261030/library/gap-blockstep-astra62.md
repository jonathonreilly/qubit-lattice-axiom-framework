# Repo search

**GUIDE.** Row 1341 is research text at `32314dd10`. The target-specific prior file is absent. The November 8 digest covers earlier ultraviolet questions and points to a soft-route local-block transfer result. Ethan Sussman and Levent Alpoge, with Claude and Codex, are the authors of the two texts consulted at `31a47c543775`. [Outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex) · [Complete account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex)

**GUIDE.** The November 8 digest, lines 395 and 487, identifies the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. On PR 10114 at `f76f6c649c`, lines 106–149 give a lower quadratic-form bound for a local centered loop. Its exterior convolution remains present. It supplies neither an upper bound on excited states nor a map between effective actions. The rule-9 filename search also covered main at `8b11ae2bb9` and PRs 10133, 10134, 10141 and 10144 at `89faef229f`, `1e70c7211a`, `a2f6a430e2` and `1f20846b80`. Main's `docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md`, lines 10–30, treats SU(3) and leaves the four-dimensional recoupled contraction open. The pinned registry has no match for the task name, SEED-L, UNIV-K, shrink-box, or the mass-preserving chain wording. These are bounded searches.

**GUIDE.** Rows 1326 and 1331 distinguish a finite pair of integrals at one coupling from the first-passage cutoff tail. I use CH from row 1332, §6.1, with row 1335, “Proposition CH”. For fixed admissible physical tori of sides `ell` and `L ell`, CH transports their two positive masses separately. Its end bound is on the defect $L^4\log Z_\ell-\log Z_{L\ell}$, uniformly for every sufficiently late datum, with threshold strictly below $(L/2)\log(13/10)$. CH alone implies no cost estimate. No predecessor comparison is used.

**GUIDE.** In the Sussman–Alpoge outline, lines 394–416 distinguish a mass identity from a specified pushforward. Lines 4075–4084 and 7501–7524 give the invariant-class programme and its small-coupling, history and tube conditions. Lines 17280–17286 give the mass identity within the induction. CA-I 2562–2582 describes localized terms and gives the integrated mass, and 4209–4238 states the small-coupling restriction on the cited Bałaban theorem. These ranges supply no common numerical enclosure at order-one coupling. The scalar-sector scope is explicit at outline lines 31860–31882. I take the two-torus defect itself as the endpoint observable, which lets the proof use the bare transfer matrix.

**GUIDE.** A closer internal hit than the November 8 digest is row 846, `gap-handoff-opus.md`, §§2, 4, 6–7, with the domain and strict-margin repairs in `gap-handoff-check-astra.md`, §§3, 20–22. It already gives an open endpoint for global Gibbs actions with sufficiently small weighted perturbations. EXIT, which would put every required datum there, remains open. I use this as prior work. The proposed calculation below instead tests an exact factor after integrating shared Wilson links. The comparison measure for its local norms is specified product Haar. This is a test of a local interaction at one scale. The additional first-passage requirement reads the whole Wilson flow.

## What row 1341 establishes

**PROVED.** Integrating the eight interior links of a $2\times2\times2\times2$ cube preserves each Wilson partition function. Equations (16)–(18) enclose its interior integral uniformly over the boundary at $0\le\beta\le7/3$ with absolute error below $2^{-24}$ and fewer than $7\cdot10^{14}$ rational arithmetic gates. The exact integral is carried in the mass. Equation (14) exhibits 49 boundary modes across just one face, and (24) and (27) give explicit obstructions to the tested iterations at every even block size.

**OPEN.** Uniform propagation of the actual first-passage densities into a robust end class remains missing. The circuit represents a local function and its error bound. A passing certificate for the Wilson trajectory still requires an estimate on interacting boundaries under gluing. The labels in this file record hand arguments in a research draft and grant no status.

## Exact integration on a plaquette cover

**GUIDE.** Use the period-two set of links $P$ from Lemma LF of `gap-seed23-opus.md`, §5.2, also Lemma P of `gap-mixed-opus.md`, §4, credited to the Opus lane. On an even torus it has one positively oriented link per site and exactly one link per plaquette. I use the cover as proved there. Here the links in $P$ will be integrated with Haar measure, including the links closing its torus cycles. This differs from fixing a forest gauge. Grok's PR 10133, `MASS_GAP_CW_CROSSOVER_ATTACK.md`, §2, already records the six-staple quaternion field.

**PROVED (one mass-preserving step).** Let all periods be even and at least four. Use Haar probability, $q(U)=\tfrac12\operatorname{tr}U$, $A(t)=\int_{S^3}e^{t u_1}\,du$, and $w_\beta(U)=e^{\beta q(U)}/A(\beta)$. For a marked link $s$, orient its six three-link complementary paths to give staples $v_1,\ldots,v_6$ with incident plaquette factors $w_\beta(u v_i^{-1})$. With $SU(2)$ identified with the unit quaternions, $q(u v^{-1})=u\cdot v$. The exact new factor is
$$
 F_\beta(v_1,\ldots,v_6)
   = \int_{S^3}\prod_{i=1}^6 w_\beta(u v_i^{-1})\,du
   = \frac{A(\beta|v_1+\cdots+v_6|)}{A(\beta)^6}.
$$
Each original plaquette is used once. Given the unmarked links the marked links integrate independently. Fubini therefore gives the partition function of the normalized weights exactly as $\mathbb E_{\rm Haar}\prod_{s\in P}F_\beta(v(s))$. For the convention $e^{\beta(q-1)}$ restore $[e^{-\beta}A(\beta)]^{6|P|}$ on each torus. This preserves each CH mass, including its normalization. The same argument works with translated copies of a general positive six-plaquette factor depending on its single marked link and the unmarked links of its star. Within one star the six staples use disjoint triples of unmarked links. They are independent Haar under the reference measure, even though factors at different stars share links.

**OPEN (iteration).** This operation eliminates one quarter of the links. Its output is a product of six-staple interactions on the remaining links, with their actual shared incidences. Replacing it by a new plaquette Wilson density at an adjusted coupling needs an identity or a bounded residual in a class closed under the next step. The equality just proved supplies neither. I test a specific residual norm next.

## A one-block end test with a volume-independent norm

**PROVED (small residual implies CH's END).** Use the preceding period-two incidence pattern. At each marked link $s$ put a positive factor $G_s=c_s(1+h_s)$ on its 18 unmarked links. Assume $c_s>0$ and that $c_s,h_s$ repeat with period two, with the same local functions on a torus $T_n$ and its $L^4$-sheeted periodic cover $T_{Ln}$. Here $n$ is even, $n\ge 8$, and $L$ is an integer. The functions may differ between different cutoff data. Each $h_s$ belongs to $L^6$ for product Haar on its 18 links. Put $D=90$, $d=D+1$. If
$$
     \max_s\|h_s\|_6 < \frac{1}{64d},                                      \tag{1}
$$
then, with $Z$ the integral of the product of the $G_s$,
$$
 \left|L^4\log Z(T_n)-\log Z(T_{Ln})\right|
 \le \frac{4(Ln)^4}{d}\,2^{-\lceil n/8\rceil}.                              \tag{2}
$$
This is an open end class in the relative $L^6$ topology of the positive factors for a fixed period. For fixed $L$ the right side tends to zero. Thus, if all the first-passage presentations landed in this class at a common physical mesh, one could choose an admissible side in that mesh large enough for the strict FL margin. Equation (2) makes no use of positivity of an effective transfer operator.

**PROVED (uniform nonvanishing).** In the graph of marked links, join two stars sharing an unmarked link. Every unmarked link belongs to at most six stars and a star uses 18 such links, so its degree is at most $D=18(6-1)$. Write $b=1/(64d)$. For any set $C$ of distinct stars, successive Hölder integration on each shared link gives
$$
 |\mathbb E\prod_{s\in C}h_s|\le\prod_{s\in C}\|h_s\|_6\le b^{|C|}.
$$
At a link use exponent six on each factor and supply the remaining reciprocal exponent by the constant 1. The resulting nested sixth moments integrate to the full sixth moment of each factor. This is Finner's product-space bound, also used in `gap-flat-check-opus.md`, §3. Disconnected components have disjoint sets of links, so expectations factor across them.

For any subset $A$ of stars let $Q_A(z)=\mathbb E\prod_{s\in A}(1+z h_s)$. For $v\in A$ separate the terms in its expansion that use $v$ by their occupied connected component $C$ at $v$. With $N[C]$ its closed graph neighbourhood, this gives the polynomial identity
$$
 Q_A=Q_{A\setminus\{v\}}+
 \sum_{v\in C\subset A,\ C\ {\rm connected}}
 z^{|C|}\mathbb E\prod_{s\in C} h_s\; Q_{A\setminus N[C]} .
$$
Induct on $|A|$, starting with $Q_\varnothing=1$. Suppose all smaller deletion ratios $Q_B/Q_{B\setminus\{u\}}$ have modulus at least $e^{-1/d}$ for $|z|\le2$. Then the quotient of the last polynomial factor by $Q_{A\setminus\{v\}}$ has modulus at most $e^{|C|}$ by deleting at most $d|C|$ vertices. There are at most $(4D)^{k-1}$ connected sets of size $k$ containing $v$. Fix an order of neighbours, select a deterministic rooted spanning tree, and encode its plane tree shape and the neighbour choice at each descent. The depth-first traversal shape has at most $4^{k-1}$ possibilities and the encoding determines the set. The deletion ratio for $A$ consequently differs from 1 by at most
$$
 \frac{2eb}{1-8eDb} < \frac1{2d}.
$$
Here $e<3$. Also $e^{-x}\le1/(1+x)\le1-x/2$ for $0\le x\le1$. This closes the induction, including nonvanishing. The power-series logarithm of each ratio about 1 has modulus at most $-\log(1-1/(2d))\le1/d$. Telescoping the deletion ratios gives an analytic logarithm, zero at $z=0$, of modulus at most $|A|/d$ on $|z|\le2$.

**PROVED (cancellation of the short coefficients).** Introduce one formal variable per star in $Q$. The coefficient of a monomial in $\log Q$ vanishes if its support is disconnected. Setting all variables off that support to zero factors the remaining polynomial across the disconnected parts, so its logarithm adds. A degree-$k$ coefficient has at most $k$ distinct stars. Give it a root at each occurrence, with weight $1/k$. Star paths have coordinate displacement at most two per graph edge, and their individual link endpoints lie within sup distance one of the star's base vertex. For $k<n/8$, the whole rooted pattern can be lifted from its root in a box of radius $2(k-1)+1$, with no new vertex, link or adjacency identification on reduction modulo $n$. Every cycle lifts consistently because an extra graph edge can close a path of at most $k$ jumps of size at most two, hence cannot wind around side $n$. Rooted patterns on $T_n$ therefore have exactly $L^4$ translates lifting their root on $T_{Ln}$ and the same rooted coefficients. Conversely every such pattern on $T_{Ln}$ reduces injectively on its support. Independence of the Haar links gives identical expectations. This is the short-cluster cancellation used in `gap-seed-sc.md`, §2.3, applied here to star factors and the four-side cover.

Thus $L^4\log Q_{T_n}-\log Q_{T_{Ln}}$ vanishes through degrees $k<\lceil n/8\rceil$. Its modulus on $|z|=2$ is at most $2(Ln)^4/d$, since there is one marked link per site. The Cauchy coefficient bound and the geometric tail at $z=1$ prove (2). At real $z\in[0,1]$ the logarithm is the ordinary real logarithm by positivity. The $\sum_s\log c_s$ terms cancel exactly under the cover. The argument measures a whole-star norm under Haar and uses the incidence at every shared link. The Hölder step uses independence of the underlying Haar variables.

## The exact six-staple test

**PROVED (a finite arithmetic reduction).** Write $M_j=\mathbb E F_\beta^j$ for the product-Haar expectation on the six staples, including $M_0=1$. In particular $M_1=1$. Let $u_1,\ldots,u_j$ be independent Haar unit quaternions and $S_j=\sum_{a=1}^j u_a$. Integrate the six independent staples first in $j$ copies of the central-link integral. This gives
$$
 M_j=A(\beta)^{-6j}\,\mathbb E\,A(\beta |S_j|)^6,\qquad
 \|F_\beta-1\|_6^6=\sum_{j=0}^6(-1)^{6-j}{6\choose j}M_j.                \tag{3}
$$
The sixth power is even. A coordinate of the uniform point on $S^3$ has density $(2/\pi)\sqrt{1-x^2}$ on $[-1,1]$ by slicing the sphere. Its odd moments vanish and its $2k$th moment is $(2k)!/[4^k k!(k+1)!]$ by integration by parts (the ratio of successive even moments is $(2k-1)/(2k+2)$). Therefore $A(t)=\sum_{k\ge0}a_k t^{2k}$ with $a_k=1/[4^k k!(k+1)!]$. Set $B(X)=\sum a_k X^k$. Rotation invariance, or averaging over an independent uniform direction including when $S_j=0$, gives $\mathbb E A(t|S_j|)=A(t)^j$. In particular
$$
 \mathbb E|S_j|^{2k}=[X^k]B(X)^j/a_k.                                      \tag{4}
$$
A single bounded list of rational polynomial products evaluates (3) to a certified absolute precision using radial moments. Equations (3)–(4) describe integration of a local factor. They contain all the link-sharing used in (2) only through the separate gluing proof above.

**PROVED (error and operation bound for this proposed test).** For rational $0\le\beta\le3$, let $P(X)=\sum_{k=0}^{128}a_kX^k$. Replace each $A(t)$ in (3) by $P(t^2)$, evaluating the numerator polynomial by (4) exactly up to $k=768$. For $0\le t\le18$ the first omitted term is at most $(27/129)^{258}<2^{-516}$, using $k!\ge(k/e)^k$ (integrate $\log x$ up to $k$) and $e<3$. The ratio of successive terms from there is at most $81/(130\cdot131)<1/2$. The uniform error is less than $2^{-515}$. Both the exact radial factor and the polynomial are bounded by $e^{18}<2^{36}$ and both denominators have base at least 1. The numerator sixth-power error is at most $6\cdot2^{180}2^{-515}$. On $x\ge1$ the derivative of $x^{-6j}$ has absolute value at most 36. The error contributed by the reciprocal is at most $36\cdot2^{216}2^{-515}$. Summing with the binomial coefficients in (3) gives an absolute error less than $2^{-280}$.

For example the attempted local predicate at $\beta=23/10$ is the rational upper endpoint from (3), enlarged by $2^{-280}$, strictly below $(64\cdot91)^{-6}$. Build $a_0,\ldots,a_{768}$ by the ratio $a_{k+1}/a_k=1/[4(k+1)(k+2)]$. Build the six truncated powers of $B$ through degree 768 by ordinary convolution, and $P^6$ through degree 768 by the same procedure. Contract coefficients with (4) and the powers of $\beta^2$, then compare integers after clearing positive denominators. The count is below $10^8$ rational additions, multiplications and divisions. Twelve convolutions cost less than $24(769)^2$ multiply/add operations, and the scalar arrays and dot products take fewer than $10^5$ further operations. The count is in arithmetic operations. In particular, $4^{768}768!769!$ is a common denominator of the $a_k$, so powers through six use at most its sixth power, and $1/a_k$ is an integer. The fixed rational $23/10$ adds powers of ten and one common positive denominator for $P(\beta^2)^{-6j}$, $j\le6$. A Lean checker could replay the recurrences and compare the integers by kernel reduction, with proofs of (3), (4) and the tail. There is no Lean check in this work. The following hand test settles the sign relevant to (1) without running this calculation.

**PROVED (the natural test fails at order one).** Put $r=A'(\beta)/A(\beta)$. Under the law with density $F_\beta$ the six unit vectors are conditionally independent given a uniform central unit vector $u$, and each has conditional mean $ru$. Under reference product Haar the functions $2v_i\cdot v_j$, one for each $i<j$, are orthonormal because each is centered in both arguments and $\mathbb E(v_i\cdot v_j)^2=1/4$. Their inner products with $F_\beta$ are $2r^2$. Projection gives
$$
   \|F_\beta-1\|_6\ \ge\ \|F_\beta-1\|_2\ \ge\ 2\sqrt{15}\,r^2.       \tag{5}
$$
$r$ increases with $\beta$ by the strictly positive variance formula for $(\log A)''$. From $(k+1)!\ge2^k$ one has $A(t)\le e^{t^2/8}$. At $\beta=1$, $A'(1)\ge1/4$ and $e^{1/8}<8/7$, so $r(1)>1/5$. At $\beta=2$, the first two nonconstant Taylor terms give $A'(2)\ge1/2+1/6$ and $e^{1/2}<5/3$ (for instance $e\le5/2+(1/6)/(1-1/4)<25/9$). Thus $r(2)>2/5$ and (5) exceeds one throughout $\beta\ge2$. For any $c>0$, (1) for $F_\beta/c-1$ would give $1/c>1-b$ by its mean, where $b=1/(64d)$. Its two-argument projection already has norm at least $(1-b)2\sqrt{15}/25>b$ for every $\beta\ge1$. No bulk normalization repairs this particular test. This is a hand refutation of the proposed local predicate. It says nothing about the value of the Wilson two-torus defect at $\beta=23/10$.

**PROVED (a six-argument residual survives every additive proper-subset truncation).** On each copy of $S^3$ take the four orthonormal functions $2v_a$, $1\le a\le4$. On a fixed subset of $k$ arguments use products of these functions and the constant on the other arguments. The squared norm of the projection of $F_\beta$ onto this space is
$$
 (2r)^{2k}\sum_{a_1,\ldots,a_k}(\mathbb E_u u_{a_1}\cdots u_{a_k})^2
   =(2r)^{2k}\mathbb E_{u,u'}(u\cdot u')^k ,
$$
by conditional independence in the preceding paragraph and independent Haar $u,u'$. For $k=6$ the last moment is $5/64$. Any sum $H$ of square-integrable functions each omitting at least one staple is orthogonal to this product space, including an arbitrary constant term. It follows that
$$
    \|F_\beta-H\|_6\ge\|F_\beta-H\|_2\ge8\sqrt{5}\,r^6
       >16/15625 > 1/(64\cdot91)\qquad (\beta\ge1).                         \tag{6}
$$
An infinite $L^2$ limit of such sums obeys the same lower bound. This rules out meeting the absolute residual tolerance (1) by keeping every pair through every five-staple **additive** term at this normalization. Products of lower-argument functions, an approximation to $\log F_\beta$, or a change of reference measure can carry this degree-six component. They require their own gluing argument.

## Keeping a finite interaction through the next step

**GUIDE.** Equations (5)–(6) motivate keeping a nonconstant core at each step. The following bisection gives a precise local test for an entire class, including its discarded boundary information. The two-site block is used in successive coordinate directions. I specify its entry condition since the preceding six-staple factor has a different incidence graph.

**PROVED (finite table test for one exact bisection).** On a rectangular periodic four-dimensional grid give each unoriented bond in direction $\mu$ an independent state with probability law $m_\mu$ on a measurable space $\Omega_\mu$. One nonnegative cell factor $K$ is a function of its eight signed incident bond states. Its two neighbouring cells see the same state on their common bond. Use one local rule on both tori. Finite types can be included by retaining the types and all their incidences. Here take the translation-invariant case and sides at least four before and after bisection. For each direction let $\pi_\mu:\Omega_\mu\to I_\mu$ be a measurable map onto a finite alphabet up to null sets, with law $p_\mu$. Suppose a nonnegative table $A$ in the eight face labels represents the cell with distortion $E\ge1$ as follows.
$$
       E^{-1} A(\pi\boldsymbol\omega)\le K(\boldsymbol\omega)
            \le E A(\pi\boldsymbol\omega)\quad\text{a.e.}                       \tag{7}
$$
Carry also a positive scalar per cell in both masses. Equation (7) permits zeros of $A$. The endpoint used below is strictly positive.

Pair cells in direction $i$ on an even side. A pair has 14 external old bonds. On each new $i$-face the old tuple has length one, and on each transverse face it is an **ordered pair** of old states, ordered along $i$ at both ends of every transverse bond. On the two new $i$-faces use the appropriate outer old state. Integrate the one internal bond of the two exact factors with $m_i$. Its finite comparison is
$$
 B(\mathbf a)=\sum_{s\in I_i}p_i(s)\,
       A(\mathbf a_{\rm left},s) A(s,\mathbf a_{\rm right}),                 \tag{8}
$$
in the corresponding signed slots. New alphabets are supplied by maps $t_\mu$ on each tuple of old labels. Supply two positive finite functions $u_\mu^+,u_\mu^-$ on those tuples, a scalar $c>0$, a table $A'$ on eight new labels, and $D_0\ge1$. The **one-block finite inequality** is the pair of comparisons for all 14 external labels
$$
 D_0^{-1} H(\mathbf a) \le B(\mathbf a)\le D_0 H(\mathbf a),\qquad
 H=c\, A'(t\mathbf a)\prod_{\mu,\pm} u_\mu^\pm(\mathbf a_\mu^\pm).       \tag{9}
$$
All quantities in this test, including the $p_i$, can be rational. The functions $u^+,u^-$ may absorb arbitrarily large positive one-face factors. Formula (9) has no quantifier over a surrounding lattice.

**PROVED (propagation and individual masses).** Let $J$ be the product of the two exact factors integrated on their shared bond. Positivity and (7) put $J$ between $E^{-2}B$ and $E^2B$ almost everywhere in the external states. Null sets cause no exception in the torus integral by Fubini. Divide $J$ by $c\prod u_\mu^\pm$ to form $K'$. Tilt the product law of the tuple on each new bond by $u_\mu^+u_\mu^-/b_\mu$, where
$$
 b_\mu=\sum_{\mathbf a}p_\mu^{\otimes m}(\mathbf a)
                 u_\mu^+(\mathbf a)u_\mu^-(\mathbf a),\qquad
 m=1\ (\mu=i),\quad m=2\ (\mu\ne i).
$$
The new label law $p'_\mu$ is the pushforward under $t_\mu$ of these normalized finite weights. The new label of an exact tuple is $t_\mu$ applied to its old labels. The bound (7) holds on the new grid for $(K',A')$ with $E'=E^2D_0$. If the old scalar per cell was $s_0$, the new scalar is $s_0^2 c\prod_\mu b_\mu$. To see the equality of masses, multiply the divisions across the new cells. Every new bond supplies exactly the product that was used to tilt its law, and there is one unoriented bond in each direction per new cell. All remaining integrations are the original ones, regrouped by Fubini. This proves exact preservation for each torus separately. No sign or volume-dependent choice is needed. The exact tuple spaces may grow indefinitely. Only their finite label laws enter (8)–(9).

**PROVED (iteration after a verified entry).** After $N$ pair steps along a prescribed list of axes on admissible grids, the distortion is at most
$$
        E_N=E_0^{2^N}\prod_{j=0}^{N-1}D_j^{\,2^{N-1-j}},                    \tag{10}
$$
where $D_j$ is the comparison factor in (9) at step $j$. Suppose a full number of sweeps ends with cubic grids of sides $n,Ln$, and the last table has positive minimum $a_-$ and maximum $a_+$. Absorb $a_-$ into the bulk scalar and put $\eta=E_N a_+/a_--1$. The exact residual about 1 then has supremum norm at most $\eta$, since its lower bound is $1/E_N$. For these degree-eight cell factors the deletion and lifting proof of (2) applies with graph degree 8 and $d=9$, since two cells share a state only at a common bond and their centers are neighbours. The same conservative short-coefficient cutoff $k<n/8$ works. Hence $\eta<1/(64\cdot9)$ suffices for (2) with $d=9$. The bulk scalar, including all tilts, is the same per corresponding cell at a given cutoff and drops out of the defect. This is a genuinely iterable statement for the class (7). To apply it to CH one needs this entry and the finite tables uniformly on the actual cutoff tail, and a choice of grids compatible with the fixed physical tori. Bisections require an even side. An admissible side $2L^m$ with $L$ odd has just one factor of two. Further dyadic sweeps would require another tiling or a change of admissible presentation with a proof of both mass identities.

**PROVED (size of the table comparison).** At common alphabet size at most $q\le6$, (9) has at most $q^{14}$ external configurations. For each, (8) takes at most $3q$ rational multiply/add operations. Forming the positive product and the two comparisons, including the bounds, takes fewer than 20 further arithmetic operations. Computing the new laws uses at most four lists of $q^2$ terms. Thus a conservative bound is $80\cdot6^{14}$ arithmetic operations per table pair, and fewer than $10^{15}$ for 100 prescribed pairs including the law updates and endpoint scans. This is an operation count for tables already supplied with exact rational probabilities and entries. Operand bit sizes, the construction of a witness and the verification of (7) for a given continuous input are additional matters. There are no numerical Wilson tables satisfying (7)–(10) in this work.

**PROVED (implementing the odd blocking factor).** The tiling issue in (10) can be removed within the table theorem. In a sweep in direction $i$, partition every $i$-line into aligned intervals of length $L$, using the same cuts on every line. Build each interval by the same binary tree with $L$ leaves. At a merge of lengths $h,k$ use $A_h$ on the left and $A_k$ on the right in (8). Throughout this sweep leave the two outer $i$ labels, the axial bond law and the two axial face factors unchanged (identity label map and face factors 1). The internal axial bond therefore always has the input law $p_i$. Each new transverse face uses an ordered pair, with law before tilting $p_{\mu,h}\otimes p_{\mu,k}$, as both transverse neighbours have the identical interval partition. The proof for (9) gives $E_{h+k}\le E_h E_k D_{h,k}$. Its bulk scalar is $s_hs_k c_{h,k}\prod_{\mu\ne i}b_{\mu,h,k}$. In particular, interfaces between unequal lengths along $i$ require no new identification. These observations prove the assertion inductively for every node of the tree, even when the period is not divisible by an intermediate length. At the root all cells have length $L$. Repeat in the other axes. An admissible side $2L^m$ now supports $m$ complete four-axis factor-$L$ steps.

Only one finite test is needed for each distinct pair of child types in the chosen tree. A binary addition chain for the integer $L$ uses at most $\lfloor\log_2L\rfloor+\operatorname{popcount}(L)-1$ types of merge per axis (successive doublings and additions of 1). For example, for $L=25$ the lengths $1,2,4,8,16,24,25$ suffice. Four isotropic factor-25 steps would require at most 96 table pairs if each scale and axis uses its own tables. This illustrates the count, without selecting the UV ceiling or the physical matching data. For a final cell built from $M$ input cells with every comparison factor at most $D_*$, the binary-tree bound is $E_{\rm in}^M D_*^{M-1}$ because the tree has $M$ leaves and $M-1$ internal nodes. The explicit accuracy price is an upper bound for this proof. Actual errors can cancel.

## Testing entry into the finite-table iteration

**PROVED (rank required at one resolved staple).** Take $\beta\ge1$ and the unit-mean Wilson star $F_\beta$. If an approximation $H$ has separation rank at most 13 between $v_1$ and the other five staples in product-Haar $L^2$, then
$$
               \|F_\beta-H\|_2>1/900.
                                                                            \tag{11}
$$
For $\beta\ge2$ the lower bound improves to $1/100$. This applies to signed as well as nonnegative cores. Multiplication by functions on the two sides separately preserves finite separation rank whenever the resulting factors are in $L^2$.

Indeed, put $(Tf)(v)=\int e^{\beta u\cdot v}f(u)\,du/A(\beta)$. Averaging $F_\beta$ in staples 3 to 6 gives the integral kernel of $T^2$ in the first two staples. The corresponding marginal of $H$ still has rank at most 13. The orthogonal subspaces of constants, linears $a\cdot v$, and trace-free quadratics $v^t Bv$ for real symmetric traceless $4\times4$ matrices have dimensions $1,4,9$. The dimensions follow by scaling a homogeneous polynomial off the sphere. The orthogonality follows from parity and $\mathbb E v_av_b=\delta_{ab}/4$. $T$ has eigenvalues $1,r,\tau$ on these spaces. For the last, the conditional second moment at direction $v$ has eigenvalue $a=A''/A$ along $v$, and $(1-a)/3$ on its perpendicular space, by rotation invariance. Thus $\tau=(4a-1)/3$.

The function $a$ increases on $\beta\ge0$. Under the original distribution of $t=|u_1|$ its formula is an expectation of $t^2$ reweighted by $\cosh(\beta t)$. Its derivative is the covariance of $t^2$ and $t\tanh(\beta t)$ in the tilted probability. Both are increasing, so the independent-copy covariance identity gives a nonnegative derivative. Also
$$
 \tau(\beta)=\frac{1}{A(\beta)}
       \sum_{k\ge1}a_k\beta^{2k}\frac{k}{k+2}.
$$
This follows directly from the even-moment ratio above, by expanding $4A''-A$. The first summand gives $\tau(1)\ge1/[24A(1)]>1/30$ and $\tau(2)\ge1/[6A(2)]>1/10$. The corresponding linear eigenvalues exceed $1/5$ and $2/5$. On the 14-dimensional sum, the norm of $T^2f$ for a unit vector exceeds the smaller stated **squared** eigenvalue bound. The rank-13 marginal operator kills a unit vector in that sum. Its difference from $T^2$ thus has operator norm exceeding the bound, its kernel has at least that $L^2$ norm by Cauchy–Schwarz, and averaging the four omitted arguments cannot increase $L^2$. This proves (11).

**PROVED (comparison with a multiplicative enclosure).** If $H$ has the rank just specified and $H/E\le F_\beta\le EH$ pointwise, then $|H-F_\beta|\le(E-1)F_\beta$. A sharper comparison on the two-staple marginal works without the size of $\|F_\beta\|_2$. After averaging, the difference kernel is bounded pointwise in absolute value by $(E-1)$ times the kernel of $T^2$. The latter is symmetric, nonnegative and has every row and column integral one. Jensen followed by integration gives $\|T^2|f|\|_2\le\|f\|_2$. Hence the difference operator has norm at most $E-1$. The null-vector argument forces $E-1>1/900$ at $\beta\ge1$ and $E-1>1/100$ at $\beta\ge2$. These bounds already exceed the endpoint allowance $1/(64\cdot9)$ at $\beta\ge2$, before any squared distortions. In particular a direct division into at most six classes of a single resolved staple cannot initialize this iteration at the Wilson window with its required tolerance. One-face positive factors on that staple can be included in $H$. A different presentation entangling the staples across the cut, a more accurate higher-rank core, or a stronger propagation estimate falls outside (11).

**PROVED (a positive finite core that keeps all six staples).** There is an alternative to assigning a small alphabet to each staple. For rational $0\le\beta\le3$, use $P_{64}(X)=\sum_{k=0}^{64}a_kX^k$ and define
$$
 \widehat F(v)=\frac{P_{64}(\beta^2|\sum_i v_i|^2)}
                         {P_{64}(\beta^2)^6}.
$$
For $0\le t\le18$ the first omitted term in $A(t)$ is at most $(27/65)^{130}<2^{-130}$ and successive ratios are below $1/2$. Since $P_{64}(t^2)\ge1$, one has $1\le A(t)/P_{64}(t^2)\le1+2^{-129}$. Hence, uniformly on the **whole** block boundary,
$$
       E^{-1}\widehat F\le F_\beta\le E\widehat F,\qquad
       E=(1+2^{-129})^6.                                                     \tag{12}
$$
This is a written error bound. Keep $F_\beta$ as the exact local factor in the measure and $\widehat F$ as its comparison. The comparison is a strictly positive polynomial of a single scalar invariant, despite the lower bounds on separable approximations.

**PROVED (one further exact local elimination).** An unmarked link $x$ occurs in six plaquettes and in six distinct marked stars because a particular star uses each external link at most once. In its $j$th incident star only one staple moves when $x$ varies. With the other links fixed that staple is $O_jx$, where $O_j$ is an orthogonal linear map of quaternion coordinates (left and right unit multiplication and possibly inversion). Write $B_j$ for the sum of the other five staples. Then the argument of $P_{64}$ there is $\beta^2(a_j+b_j\cdot x)$, with $a_j=1+|B_j|^2$ and $b_j=2O_j^t B_j$. The exact new factor is $J=\int\prod_{j=1}^6 F_j\,dx$. Its comparison $\widehat J=\int\prod_{j=1}^6\widehat F_j\,dx$ is positive and $E^{-6}\widehat J\le J\le E^6\widehat J$. Integrate any collection of unmarked links no two of which occur in one star, keeping $J$ in the actual mass. Their contractions commute by Fubini. For example, repeat one unmarked link based at the origin by translations in $(2L)\mathbb Z^4$ on tori of periods divisible by $2L$, $L\ge3$. The star support radius one makes the stated independence immediate. This gives two consecutive local eliminations on the pure Wilson input across the window. It leaves shared links and a new interaction type.

**PROVED (arithmetic for the second local map).** At fixed exterior quaternions expand each $P_{64}(\beta^2(a_j+y))$ in powers $y^{k_j}$. To integrate the product it suffices to compute $M_{\mathbf k}=\mathbb E_{S^3}\prod_j(b_j\cdot x)^{k_j}$, $0\le k_j\le64$. Set $M_{\mathbf0}=1$, use zero for odd total $h$, and for positive even $h$ choose any $i$ with $k_i>0$. Then
$$
 (h+2)M_{\mathbf k}
 =\sum_{j:\, k_j-\boldsymbol1_{j=i}>0}
   (k_j-\boldsymbol1_{j=i})(b_i\cdot b_j)
           M_{\mathbf k-e_i-e_j}.
$$
For a standard four-dimensional Gaussian $Y$, integration by parts in direction $b_i$ gives the sum on the right for Gaussian moments. Writing $Y=Rx$ in polar coordinates separates the independent radial moment. Integration by parts in $\int_0^\infty r^{h+3}e^{-r^2/2}dr$ gives $\mathbb E R^h=(h+2)\mathbb E R^{h-2}$. This proves the recurrence. There are $65^6$ entries, with at most six terms and fewer than 60 rational arithmetic gates per entry, including multiplication by the six univariate coefficients and accumulation of the integral. The binomial expansions and 21 Gram entries are smaller than $10^6$ extra gates. For rational $\beta$ this is a straight-line polynomial circuit with rational constants in the external quaternion coordinates for $\widehat J$, of size below $10^{13}$. No sampling over external fields enters (12). This operation bound for the local function neither bounds all subsequent contractions nor checks a global inequality involving that circuit. No circuit or proof certificate of that size was run or materialized.

## A cubical Wilson step and the boundary information it transmits

**PROVED (exact boundary law for the $2^4$ block).** Work on $[-1,1]^4$ with unit fine links. On each unit four-cell assign one quarter of the exponent of each of its 24 plaquettes. Each torus plaquette belongs to four unit cells, so these positive cell factors reproduce each torus mass. Merge 16 cells and integrate all links not contained in the boundary of the resulting cube. The interiors of disjoint such blocks use disjoint link sets. Exact gluing on an even torus follows by Fubini, retaining **all** shared boundary links. A boundary plaquette factor belongs to a closed three-face (split or assign terms on their intersections consistently). Remove these explicit factors from the block amplitude for the following analysis.

The eight interior links are the spokes from the origin to $a\in\{\pm e_1,\ldots,\pm e_4\}$. The remaining plaquettes in this integral are precisely those through the origin. For a plaquette outside the boundary its two fixed transverse coordinates must be zero, and its two unit intervals both meet zero. Its coefficient is the full Wilson coefficient. The central-star geometry, including the distinctness of the 48 far links, is Lemma STAR in `gap-blockcrit-opus.md`, §4 (see the statement starting at line 172). Label the far link from $a$ to $a+b$ by $V_{ab}$ whenever $a\perp b$. It lies in the relative interior of the three-face normal to $a$ in the sense of its midpoint. Put $H_{ab}=V_{ab}V_{ba}^{-1}$, $H_{ba}=H_{ab}^{-1}$. With the spokes oriented out of the origin, the remaining factor, up to its known bulk scalar, is
$$
 I(V)=\int\prod_{\{a,b\}:\,a\perp b} w_\beta(U_a H_{ab} U_b^{-1})
                 \prod_a dU_a.                                              \tag{13}
$$
There are 24 factors on the graph $K_{2,2,2,2}$. With all far links independent Haar, $I$ has mean one because integrating either half of each $H_{ab}$ integrates that normalized $w_\beta$ to one.

**PROVED (what two and three faces see).** For a subset $S$ of the eight faces integrate all its complementary face variables with product Haar. Each edge with an endpoint outside $S$ loses its normalized factor by integration of its private far link. What remains is (13) on the induced graph. If this graph is a forest, integrate the leaf spokes one at a time to obtain 1, including for every one- and two-face marginal. For three pairwise perpendicular signed directions $a,b,c$, the induced graph is a triangle. On the remaining boundary its density is $w_\beta^{*3}(H_{ab}H_{bc}H_{ca})$, by the two Haar substitutions at successive vertices and centrality/inversion symmetry of $w_\beta$. Equivalently, under this density, the three edge noises $U_aH_{ab}U_b^{-1}$, $U_bH_{bc}U_c^{-1}$, $U_cH_{ca}U_a^{-1}$ are independent with density $w_\beta$, conditional on the spokes. The mean fundamental character of the triangle is $2r^3$, because each noise quaternion has scalar mean $r$ and mean vector zero. Under reference Haar this character has mean zero and $L^2$ norm one.

**PROVED (separate face factors cannot approximate the cube accurately).** Even allow an arbitrary positive function of the whole coarse two-skeleton, multiplied by an arbitrary positive function on each closed three-face, including its interior links. Fixing the two-skeleton makes this a product over the independent face interiors. The explicit removed boundary terms are themselves of that product form after the fixing, so division removes them exactly. Suppose such a product $H$ obeys $H/E\le I\le EH$ in the remaining variables. All relations can be read almost everywhere, by disintegration under Haar. Write $z=\int H$ and write its normalized one-face densities as $f_a$. The unit mean and the unit two-face marginals of $I$ imply $E^{-1}\le z\le E$ and $E^{-1}\le z f_if_j\le E$. Thus $E^{-2}\le z f_af_bf_c\le E^2$ by squaring and multiplying the three pair bounds and dividing by $z$. The exact three-face density lies in $[E^{-3},E^3]$. Test it minus 1 against the triangle character. Cauchy–Schwarz gives reference $L^1$ norm at most one for this character, so $2r^3\le E^3-1$. The distortion is bounded away from 1 at every fixed $\beta>0$. The stronger rank estimate below tests joint finite labels that can retain actual three-face correlations.

**PROVED (49 modes across one cubical face).** Fix a face $a$. In the exact normalized factor (13), let $H$ be any square-integrable comparison of separation rank at most 48 across the variables of face $a$ versus the other seven faces, after fixing the two-skeleton. If $H/E\le I\le EH$, then
$$
                       E-1\ \ge\ r(\beta)^3.                                \tag{14}
$$
The same statement applies to the full block amplitude after dividing its known boundary factors, since at fixed two-skeleton each such factor is a product across the cut. It suffices that the divided comparison have the stated rank. All eight cuts are equivalent. In particular, at $\beta=23/10$ the lower bound exceeds $8/125$.

To prove (14), there are six neighbours of $a$. Of the 15 unordered pairs $\{b,c\}$ of neighbours, 12 are perpendicular. Order each of these 12 pairs once. Define quaternions on opposite sides of the cut by
$$
 P_{bc}=V_{ac}^{-1}V_{ab},\qquad
 Q_{bc}=(V_{ba}^{-1}V_{bc}V_{cb}^{-1}V_{ca})^{-1}.
$$
Cyclic conjugation sends the triangle word to $P_{bc}Q_{bc}^{-1}$. Use the test functions $2(P_{bc})_j$ on side $a$ and $2(Q_{bc})_j$ on the other side, $1\le j\le4$. Include the constant 1 on each side. Each family is orthonormal under reference Haar. Every quaternion indicated is Haar and distinct pairs have an unpaired, separately centered link.

The matrix of pairings of the two test families with weight $I$ is
$$
                  \operatorname{diag}(1,r^3\mathbf 1_{48}),                   \tag{15}
$$
where the last block is $r^3$ times the identity matrix. For a matching pair the triangle marginal applies. The variables $P,Q$ are independent Haar under the reference and the pairing kernel is $w_\beta^{*3}(P Q^{-1})$. Convolution by $w_\beta$ has eigenvalue $r$ on each coordinate, so the four pairings are $r^3\delta_{ij}$. For different pairs choose $d$ in the left pair absent from the right pair. The right test then uses no $V_{da}$. Integrating it removes the unique factor involving $V_{ad}$, and integrating $V_{ad}$ centers the left test. Tests paired with the constant vanish by the one-face marginal or the next paragraph.

The norms of **both** test spans also equal their Euclidean coefficient norms in the probability with density $I$. For the left this is the unit one-face marginal. On the right, first integrate the entire face $a$. Each $V_{da}$, $d\perp a$, is now Haar, independent of all others and of the variables on edges of the induced graph on the other seven faces. Conditional on everything except these six private variables, each $Q_{bc}$ is Haar and two different pairs have a variable appearing in only one test. The conditional orthogonality, including the constant, follows. Weighted Cauchy–Schwarz and $|I-H|\le(E-1)I$ show that the matrix of test pairings of $I-H$ has operator norm at most $E-1$. The matrix of $H$ has rank at most 48. Some unit vector of the 49-dimensional test space is killed by it, while (15) has least singular value $r^3$. This proves (14).

**PROVED (consequence for the table architecture).** For a single face label with $q$ values and arbitrary joint table in all eight face labels, the rank across that face is at most $q$, even with separate positive face multipliers. The label functions and the table may depend on the fixed two-skeleton. Thus this concrete factor-two Wilson step at $\beta\ge1$ cannot produce such a description with $q\le48$ and $E-1<1/125$. At the window this excludes the small distortion and $q\le6$ budget of the preceding generic iteration by a strict margin, even if the whole two-skeleton is retained. Dense enumeration of fourteen external labels of size at least 49 would itself have more than $10^{21}$ entries, since $49^2>10^3$. This count pertains to that explicit enumeration. The 65-term radial polynomial in (12), sparse invariant tensors, or exact identities among whole configurations do not have its representation or its cost.

## A bounded arithmetic formula for the whole cubical integral

**PROVED (radial coefficient identity).** The SU(2) structure permits a less costly representation of the scalar block function. Write $Z_\square(H)=A(\beta)^{24}I(V)$, the unnormalized eight-spoke integral in (13) at the given boundary. View a quaternion as two complex coordinates, with complex scalars acting on the left. Right multiplication by a unit quaternion $h$ is a matrix $R_h\in SU(2)$ whose columns for $h=h_1+h_2j$ are $(h_1,h_2)^t$ and $(-\bar h_2,\bar h_1)^t$. Form the $16\times16$ Hermitian matrix $M$ in two-by-two blocks, one block index per spoke, with $M_{ba}=(\beta/2)R_{H_{ab}}$, $M_{ab}=M_{ba}^*$ on an oriented edge, and zeros elsewhere. Then $z^*Mz$ on unit spinors is exactly the exponent of $Z_\square$. There is no factor of two left in the exponent.

Let $J$ be block diagonal with blocks $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, and let $T=\operatorname{diag}(t_a\mathbf1_2)$. Because $R^tJ_2R=J_2$ and $R^{-1}=R^*$, we have $M^tJ=JM$. Define the real multiaffine polynomial
$$
  P(t)=\Bigl(\prod_a t_a\Bigr)\operatorname{Pf}\!\big(J(T^{-1}-M)\big),
  \qquad \det(1-TM)=P(t)^2,\qquad P(0)=1.                                  \tag{16}
$$
The matrix in the Pfaffian is skew. A factor $1/t_a$ uses the two indices of its site as a pair in a matching and can occur only once. This proves polynomiality and the degree claim. The Pfaffian identity follows by taking the top exterior power of the skew form, since congruence by $S$ multiplies its Pfaffian by $\det S$. Reducing a nondegenerate alternating form to blocks $J_2$ by elimination therefore gives $\operatorname{Pf}(B)^2=\det B$, and polynomial continuation covers singular forms. Since $1-TM$ is similar to a Hermitian matrix for positive $t$ and its determinant is positive near zero, the square root with value 1 is real there, so the coefficients of $P$ are real. A circuit using subtraction and multiplication forms all coefficients by taking, for each subset of sites, the Pfaffian of the corresponding principal submatrix of $-JM$. The complementary diagonal pairs have even index shifts and introduce no sign. The usual expansion by the partner of the first index computes all even principal Pfaffians with at most $16\cdot2^{16}$ matching terms.

For independent standard complex Gaussian two-vectors $z_a$, the expectation of $\exp(z^*T^{1/2}MT^{1/2}z)$ is $1/\det(1-TM)$ for small positive $t$, by unitary diagonalization and the one-complex-coordinate Gaussian integral. The direction of each $z_a$ is independent uniform on $S^3$ and $\mathbb E|z_a|^{2k}=(k+1)!$ by elementary radial integration. Expand by the 24 edge exponentials. Each site of odd total degree integrates to zero by sign symmetry. A site of degree $2k_a$ supplies $t_a^{k_a}(k_a+1)!$ times its spherical integral. It follows that
$$
    Z_\square(H)=\sum_{\mathbf k\ge0}
          \frac{[t^{\mathbf k}]P(t)^{-2}}{\prod_a(k_a+1)!}.                 \tag{17}
$$
The sphere-side sum is absolutely convergent by $e^{24\beta}$ for real $\beta\ge0$. Equality of coefficients only needs the Gaussian calculation near the origin. No Gaussian integral at $t=1$ is asserted.

**PROVED (seven indices and an explicit uniform remainder).** Choose one spoke as 0 and write $P=P_0-t_0P_1$, where $P_0(0)=1$, $P_1(0)=0$ because $M_{00}=0$. Eliminate $k_0$ from (17) before doing arithmetic. Its coefficient at fixed $k_0$ is $(k_0+1)P_1^{k_0}/P_0^{k_0+2}$. Dividing by $(k_0+1)!$ and summing produces the power series
$$
                  G=P_0^{-2}\exp(P_1/P_0)
$$
in the other seven variables. The coefficients exist formally since $P_1$ has zero constant. Let $C(H)$ be the sum of $[t^{\mathbf k}]G/\prod_{i=1}^7(k_i+1)!$ over $0\le k_i\le45$. For $0\le\beta\le7/3$,
$$
                 |C(H)-Z_\square(H)|<2^{-24}
                   \quad\text{for every boundary } H.                       \tag{18}
$$
In fact, if the cut misses a term, at one of seven vertices the total power of incident edges exceeds 90. Bounding each fine plaquette trace $q$ in absolute value by one, the sum of absolute Taylor monomials for that event is at most $e^{18\beta}\sum_{h\ge91}(6\beta)^h/h!$ by counting the six incident edges and the eighteen other edges. The first omitted term is bounded by $(14e/91)^{91}<2^{-91}$ and successive ratios are below $1/2$. Use $e^{42}<2^{63}$ and sum over seven vertices. This gives (18) even after the regrouping in (17). Jensen under the eight independent spokes gives $Z_\square\ge1$ because every unweighted edge has zero mean and the exponential is convex. Thus $C>0$ and (18) gives a uniform multiplicative enclosure with factor $(1-2^{-24})^{-1}$. The exactly known boundary plaquette factors may instead be kept unchanged throughout. The construction covers $\beta=23/10$.

**PROVED (cost of representing or evaluating this map).** Let $D=\sum_{i=1}^7t_i\partial_{t_i}$ and $Y=P_1G/P_0$. Use the identities
$$
      P_0 DG=D(P_1-2P_0)G-(DP_0)Y,\qquad P_0Y=P_1G.
$$
The first identity is logarithmic differentiation of $G$. At nonzero $\mathbf k$ the coefficient of $DG$ is $|\mathbf k|G_{\mathbf k}$. Moving the nonconstant part of $P_0DG$ to the right uses only lower indices. After computing $G_{\mathbf k}$, the second recurrence gives $Y_{\mathbf k}$ in the same fashion. Start with $G_0=1$, $Y_0=0$. Componentwise truncation to $0\le k_i\le45$ retains every needed predecessor. Each of $P_0,P_1$ has at most $2^7$ coefficients. The five products with already known coefficients require at most $5\cdot128$ multiply/add pairs per index. Allowing divisions, the Euler factors and the factorial-weighted final sum, fewer than 1,500 real arithmetic gates per index suffice if $|\mathbf k|G_{\mathbf k}$ is stored. Including the small Pfaffian stage, the total is below $7\cdot10^{14}$, since $46^7<4.5\cdot10^{11}$. With rational $\beta$ this is a rational straight-line circuit in the real boundary quaternion coordinates, with divisions only by nonzero integer constants in the coefficient recurrence. The imaginary parts of the Pfaffian coefficients vanish by (16). One can use pairs of real coordinates for that small stage.

The cost unit is a scalar arithmetic gate of the local polynomial. Peak memory, bit operations and Lean replay time remain unmeasured. The uniform remainder (18) holds by the Taylor tail for the entire boundary domain. The multiaffine coefficient method avoids enumerating the dense table excluded by (14). It supplies the output function of **one actual isotropic block**, including the modes that made the small table fail.

**PROVED (where the quadratic-spin formula stops under direct gluing).** In $[0,b]^4$ there are $4b(b-1)^3$ links not contained in the boundary. A tree gauge fixing the boundary vertices can set at most $(b-1)^4$ such links to 1 because a forest component can have at most one boundary root, and each fixed edge requires a different interior vertex. Each remaining interior link lies in six nonboundary plaquettes. There are $6b^2(b-1)^2$ nonboundary plaquettes. If every one had at most two remaining interior links, incidence counting would give
$$
  6\big(4b(b-1)^3-(b-1)^4\big)\le12b^2(b-1)^2 .
$$
This would require $b^2-2b-1\le0$, false at every integer $b\ge3$. A plaquette with three such links supplies a genuine higher-order term. Give the boundary and the other links identity values and vary the three links over independent central signs. The alternating three-variable sum of the Wilson exponent on these eight configurations is nonzero, since no other plaquette contains these three links. A quadratic function of the remaining link quaternions has zero such sum. Thus (16) cannot simply be reused with a larger matrix of the same bilinear exponent in the tree-gauged Wilson links. This count permits auxiliary variables and other nonlinear presentations.

## Putting the auxiliary bonds on the whole lattice

**PROVED (a positive independent-bond presentation at every bare coupling).** Use the first Hubbard–Stratonovich identity HS1 of row 1016, `gap-global-reform-max.md`, §3.3, with the check in `gap-global-reform-check-astra.md`, line 206. On an even torus join the two *even* corners of every plaquette by its auxiliary diagonal. Orient original links from even to odd and regard each two-link path between the diagonal's endpoints through an odd corner as a quaternion $v=u_a u_b^{-1}$. If the paths through the two odd corners are $v,v'$, the plaquette trace is $v\cdot v'$. For $\beta>0$ put $d\gamma_\beta$ equal to the centered Gaussian law of covariance $\beta\mathbf1_4$ and define
$$
 d\lambda_\beta(y)=\frac{A(|y|)^2}{e^\beta A(\beta)}\,d\gamma_\beta(y),
 \qquad k_y(v)=e^{y\cdot v}/A(|y|).
$$
To check normalization, write $A(|y|)^2$ as the expectation of $e^{y\cdot(v+v')}$ under two independent Haar quaternions, integrate $y$, and use $|v+v'|^2=2+2v\cdot v'$. More particularly,
$$
         \int k_y(v)k_y(v')\,d\lambda_\beta(y)
                          =e^{\beta v\cdot v'}/A(\beta).                     \tag{19}
$$
The angular part of $\lambda_\beta$ is uniform on $S^3$ independent of the radius. For each odd site $o$ integrate its eight incident original links to obtain the positive local function
$$
          J_o(y)=\int\prod_{p\ni o}k_{y_p}(v_{o,p})\prod_{a=1}^8du_a .
$$
Orient each $v_{o,p}$ according to the chosen orientation of the even diagonal. Every original link belongs to exactly one odd site. Each $y_p$ is now an independent bond variable shared by exactly two cells, the two *odd* corners of $p$. Their displacement has two entries $\pm1$ and the other two zero. The cell graph has degree 24 on periods at least six. By (19) the partition function of the normalized Wilson plaquettes is exactly $\mathbb E_{\lambda_\beta}\prod_o J_o$. Restore the same original scalar per plaquette as above. Conditional on the radii, each $J_o$ takes the eight-spoke form (13) with independent angular boundary matrices, up to edge inversions and a quaternion convention exchanging left and right. HS1 supplies the Gaussian split. The parity choice, bond normalization and local norm calculation below are the uses here.

**PROVED (one finite cubical quantity controls this particular end test).** $\mathbb E J_o=1$ because for independent angular directions each $k_y(v)$ has angular mean one at fixed radius. In two replicas integrate every $y_p$ with (19). If $u'_a=u_a g_a$, then $v_{ab}(u)\cdot v_{ab}(u')=q(g_b g_a^{-1})$ on their common corner, with the same value when both paths are inverted. The $g_a$ are independent Haar. Consequently
$$
       \|J_o-1\|_2^2
             = \frac{Z_\square(\mathbf1;\beta)}{A(\beta)^{24}}-1.            \tag{20}
$$
Finiteness also follows from the compact integral on the right. The deletion proof of (2) applies with $D=24,d=25$ and exponent two, since just two cell factors share each independent auxiliary bond. Graph edges have sup displacement one, short patterns lift at the same conservative $k<n/8$, and there are $n^4/2$ odd sites. Thus (20) less than $(64\cdot25)^{-2}$ implies (2) with $d=25$ at that coupling, and the comparison is stable for positive period-two factors satisfying the strict norm bound. The flat-boundary case of (17)–(18) gives a finite arithmetic approach to this scalar, within its stated precision. No supremum over unknown boundary data appears in (20).

**PROVED (the flat-cube test is false in the window).** At fixed radii $t_e$ in one cell, the triangle characters of the angular edge matrices are orthonormal under independent angular Haar. Different triangles have a private edge. The inner product of $J_o-1$ with the character of a triangle is $2\prod_{e\in\triangle}r(t_e)$ by the three-path calculation, where the kernel at each edge has its own parameter $t_e$. There are $\binom{4}{3}2^3=32$ triangles. To see that $\mathbb E_{\lambda_\beta} r(|y|)^2=r(\beta)$, give two quaternions conditionally independent densities $k_y$ and take the mean of their dot product. Their conditional means are $r(|y|)y/|y|$, whereas (19) gives the unconditional mean $r(\beta)$. Projection at fixed radii followed by independent radial integration proves
$$
           \|J_o-1\|_2^2\ge128\,r(\beta)^3>128/125>1
                                      \qquad(\beta\ge1).                     \tag{21}
$$
This hand bound settles the predicate for the microscopic Wilson weight. This refutes the proposed small-residual criterion about independent auxiliary bonds. The 32 contributions are local.

**PROVED (smaller exact calculation for the flat cube).** In (20) all boundary holonomies are identity. Let $s_i=u_{+i}+u_{-i}$ for the four independent antipodal pairs of spins. Then the unnormalized exponent is $\beta\sum_{i<j}s_i\cdot s_j$. For a standard real four-Gaussian $Y$, completing one square gives
$$
 Z_\square(\mathbf1;\beta)=\mathbb E_Y\!\left[
       \left(\mathbb E_s e^{-\beta|s|^2/2}A(\sqrt\beta\,|Y|\,|s|)\right)^4\right],
 \qquad s=u+v .
$$
Here the fourth power is inside the Gaussian expectation. Write the inner series as $H(\beta,x)$, $x=|Y|^2$. Its coefficient of $\beta^n x^k$ for $0\le k\le n$ is
$$
      \mathbb E|s|^{2n}\, a_k\frac{(-1/2)^{n-k}}{(n-k)!}.
$$
Equation (4) with $j=2$ supplies the moments. Square the bivariate coefficient array twice, truncating the total degree in $\beta$ at $M=512$, then replace $x^k$ by $2^k(k+1)!$ from the real Gaussian radial integral. All coefficients are rational. Equality of the Taylor coefficients follows by differentiation near zero (the bounded spins give Gaussian domination by a constant times $e^{c|Y|}$ on a small parameter disc), or by matching the finite Gaussian moments degree by degree. The original spin exponent gives the error bound through $|\sum s_i\cdot s_j|\le24$. At $0\le\beta\le7/3$ the Taylor tail is bounded by $\sum_{h>512}56^h/h!<2^{-512}$, using $56e/513<1/2$ and the subsequent ratios. There are at most $513\cdot514/2$ array entries, so the two ordinary polynomial squares, including multiply/add pairs, need fewer than $10^{11}$ rational operations in total. This is the flat integral only. It can also price comparisons with a more structured reference than 1.

## A finite gluing test that accepts correlated local functions

**PROVED (Hilbert-space gluing).** In the independent-bond presentation group cells into disjoint regions. For each region retain every external bond state and integrate the internal states exactly. If two regions merge, their kernels $K_1,K_2$ share precisely the independent bonds across the interface, including interfaces with several bonds. For square-integrable real kernels write $K_1\star K_2$ for contraction over the shared variables. Cauchy–Schwarz in those variables followed by the product integrals in the disjoint remaining variables gives $\|P\star Q\|_2\le\|P\|_2\|Q\|_2$. The true integral is preserved separately on each torus, including on a partially merged tiling. Suppose $\|K_i-A_i\|_2\le\epsilon_i$, $\|A_i\|_2\le a_i$, and a *local* comparison gives $\|A_1\star A_2-c A'\|_2\le\delta$, $c>0$. Keep $(K_1\star K_2)/c$ as the new exact kernel and carry $c$ into the scalar normalization. Its error relative to $A'$ is at most
$$
       (\epsilon_1a_2+a_1\epsilon_2+\epsilon_1\epsilon_2+\delta)/c.           \tag{22}
$$
This follows by expanding the two errors on the interface. Scalar factors are multiplied per copy of the given region type on each torus. No positivity of the *comparisons* is needed.

**PROVED (a concrete finite dictionary at order-one Wilson coupling).** On an external auxiliary bond use the functions $1$ and $y\mapsto k_y(v)$ for rational unit quaternions $v$. Their Gram entries are $1$ if one input is 1, and $w_\beta(vv'^{-1})$ otherwise, by (19) and angular averaging. Use a finite signed sum of products of these functions as a comparison tensor. At a single odd site take atoms $\Phi_U=\prod_{p\ni o}k_{y_p}(v_{o,p}(U))$ made from eight rational unit spokes. Set $A_0=\sum_i b_i\Phi_{U_i}$ with $\sum_i b_i=1$. Haar invariance in the other copy of the spokes gives $\langle J_o,\Phi_{U_i}\rangle=Z_\square(\mathbf1;\beta)/A(\beta)^{24}$ for *every* $i$, by the same change of variables as in (20). This yields the following finite local comparison for the input error.
$$
  \|J_o-A_0\|_2^2=\sum_{i,j}b_i b_j
       \prod_{p\ni o} w_\beta(v_{o,p}(U_i)v_{o,p}(U_j)^{-1})
                  - Z_\square(\mathbf1;\beta)/A(\beta)^{24}.                 \tag{23}
$$
At fixed finite $\beta$ the map from the eight spokes to $\Phi_U$ is norm continuous by its explicit Gram kernel. Compactness gives finite approximations to its Haar average by partitioning the spoke space into sets of small norm diameter. Rational quaternions are dense by stereographic parametrization, and the probability weights can be approximated by rational weights summing to one. This proves existence for one prescribed positive tolerance, with no bound on the necessary list length.

**PROVED (checking a merge without enumerating boundary configurations).** Write each comparison as a list of at most $R$ product atoms with weights. In contracting two such lists, the new weight $d_{ij}$ is the product of their weights times the single-bond Gram entries on the shared bonds. On the exterior the two atom parts $l_i,r_j$ use disjoint old bonds. Set $L_{ii'}=\langle l_i,l_{i'}\rangle$ and $B_{jj'}=\langle r_j,r_{j'}\rangle$. Then
$$
  \|A_1\star A_2\|_2^2=\operatorname{tr}(d^t LdB).
$$
For an output atom $h_k$ on the same exterior, split its product between the two regions. Its pairing with the contracted core is $\sum_{ij}d_{ij}\langle l_i,h_{k,l}\rangle\langle r_j,h_{k,r}\rangle$. Together with the output Gram matrix this gives $\|A_1\star A_2-c A'\|_2^2$ by subtracting twice the cross term. All Gram entries are products of (19), with the constant also allowed. With at most $b$ fine bonds in the participating boundary and interface lists, the number of scalar operations per merge, given the one-bond entries, is $O(bR^2+R^3)$ by ordinary matrix multiplication. The bound (23) can use the flat-cube polynomial above. Strict inequalities between the resulting expressions at a specified rational coupling can be tested with rational Taylor bounds, including reciprocal and cancellation errors, carrying the actual operand sizes and slack into any claimed certificate. None of these list lengths, precisions or total costs has been verified for a successful Wilson chain.

**PROVED (fixed-coupling consumer).** Tile the odd sites periodically by the odd sites in aligned cubes of one even side $B$. A fixed binary tree inside such a cube implements (22), starting with (23) and using the actual auxiliary bonds. After grouping by neighbouring boxes, each external state is still shared by exactly two boxes, and the block graph has degree at most $3^4-1=80$, with sup displacement at most one. On a torus of $n^4$ such boxes, $n\ge8$, short rooted patterns lift as in (2). If the local tests produce $A_{\rm end}=1$ with $\epsilon_{\rm end}<1/(64\cdot81)$, (2) holds with $d=81$ for the two bare Wilson masses at this **fixed** coupling. Repeating a whole tiling on the larger torus repeats its scalars $L^4$ times. The only unknown data for this fixed-coupling implication can thus be finite atom lists and rigorous arithmetic inequalities on one representative block. The next calculation tests whether lists can meet this particular endpoint.

**PROVED (an exposed triangle obstructs the constant endpoint at every block size).** For the aligned tiling in the last paragraph take any even $B\ge2$ and an odd corner $o$ of a block $C$ of fine sites. Pick three distinct directions from $o$ pointing out through three of its faces. A plaquette at $o$ using any one of these outward spokes has its other odd corner outside $C$ because a step in a perpendicular direction preserves the outward displacement. The three plaquettes between the three chosen spokes therefore supply three external auxiliary bonds.

Write $K_C$ for the exact contracted tensor before normalization and $m_C=\mathbb E K_C>0$. Integrating all its external auxiliary bonds other than these three sets every other exposed half-factor to 1. Equation (19) has already integrated the internal bonds. No internal plaquette reads the three outward spokes. Their three Haar variables thus separate completely from the internal mass $m_C$. The marginal of $K_C/m_C$ on these bonds is precisely the normalized triangle factor from the proof of (21), for every $B$. Its $L^2$ distance from 1 is at least $2r(\beta)^{3/2}$ by the conditional angular projection onto just that one character. Orthogonal projection by conditional expectation can only reduce the norm. Consequently, for *every* scalar $c>0$, putting $t=m_C/c$ gives
$$
 \|K_C/c-1\|_2^2\ge(t-1)^2+4t^2r(\beta)^3
          \ge \frac{4r(\beta)^3}{1+4r(\beta)^3}.
                                                                            \tag{24}
$$
For $\beta\ge1$ the norm exceeds $2/\sqrt{129}$. Thus no list, even of unlimited length, can satisfy the constant endpoint of (22) for this tiling at the window using only scalar normalizations. This is a property of the boundary left by the contractions. Equation (25) removes these local correlations before applying another end test.

**PROVED (exact removal of the exposed corner correlations).** Classify auxiliary bonds between blocks according as the displacement to the other odd corner crosses one or two block-coordinate cuts. It cannot cross more than two. At a boundary odd site $o\in C$, let $D(o)$ be its outward coordinate directions. The bonds at $o$ crossing two cuts are in bijection with the unordered pairs in $D(o)$. Define $P_o$ to be the integral over $|D(o)|$ independent Haar spokes of the product of the $k_y$ factors for those pairs, with $P_o=1$ when there is no pair. These functions are strictly positive. As in (24), every plaquette using an outward spoke is external. Integration of all single-crossing auxiliaries incident to $C$ therefore gives the exact functional identity
$$
     \int K_C(y_{\rm single},y_{\rm double})\,d\lambda_{\rm single}
                    =m_C\prod_{o\in C} P_o(y_{\rm double}).                 \tag{25}
$$
Indeed the remaining internal plaquettes read only nonoutward spokes. No outward spoke belongs to a second odd site. Each remaining boundary half-factor uses two outward spokes at the same site. The integrations split just as displayed.

On the full periodic grid, the product of the $P_o$ over cells can be included in a new **local probability law**. A coordinate near an aligned cut has two possible values $jB-1,jB$. A double-crossing bond flips two such coordinates and fixes the others. Hence its connected component is contained in a single product of these two-point sets with all other coordinates fixed. More explicitly the set of near-cut coordinates is unchanged by a flip, and the component consists of the parity-allowed vertices of a k-dimensional binary cube for some $2\le k\le4$. Its at most eight odd sites lie in distinct coarse cells. This also holds on the periodic seam, for coarse sides at least four. For $B=2$, use the unique cut pair containing a given site coordinate, which exists because the pairs are disjoint. Components have disjoint auxiliary variables. Normalize the product of their $P_o$ against their original bond laws component by component. Applying (19) within a component shows that its normalizing constant is the normalized Wilson partition function on the free unit $k$-cube, since every cube edge supplies one outward spoke, and every square face supplies its one Wilson weight after the two opposite odd corners are glued. This finite positive constant depends only on the component type and $\beta$.

Give $C$ the exact tensor $R_C=K_C/(m_C\prod_{o\in C}P_o)$ and retain all the $m_C$ and component normalizers in the mass. Multiplying the identities recovers the exact original integral. The densities of the components are now joint laws on at most eight odd sites, independent from component to component and of the single-crossing bond variables. Equation (25) gives $\mathbb E_{\rm single}R_C=1$ for every fixed set of double-crossing values. All the modes proving (24) were removed. The torus counts of these scalar factors repeat under the $L$-fold cover, so their logarithms cancel in the defect.

**PROVED (a repaired finite criterion, at one specified coupling).** The coarse $R_C$ share each independent reference variable with at most eight cells. Single-crossing bonds meet two. Distinct participating cells are within sup distance one on the coarse grid. Hölder with exponent eight and the deletion proof of (2) therefore give the strict end test
$$
       \mathbb E |R_C-1|^8 < (64\cdot81)^{-8} .                              \tag{26}
$$
The expectation is under the component laws just defined and the single-crossing bond laws. The factors repeat on corresponding cells of the two tori. Thus (26) implies (2) with $d=81$ at any compatible coarse side. It is a finite-region integral for a specified $B,\beta$, including the finitely many incident components. Its value for the pure Wilson weight is determined below.

**PROVED (a mixed correlation also refutes the repaired test).** Choose an odd corner of any even block $B\ge2$. Take two outward directions 1, 2 and an inward direction $l$ on a third coordinate axis. The auxiliary $y_{12}$ belongs to the finite double-crossing component. The two plaquettes $(1,l)$ and $(l,2)$ each cross just one cut. Reverse an auxiliary quaternion by conjugation if necessary to read the paths consistently. Under the new reference the two single-crossing auxiliaries are independent with law $\lambda_\beta$ and are independent of the component. Write $t_1,t_2$ for their radii and $Q$ for the ordered product of their two angular quaternions in the path order $1,l,2$.

Conditional on all the double-crossing variables $Y$, put on the outward spokes at the chosen odd site the probability with density $\prod_{i<j}k_{y_{ij}}(u_i u_j^{-1})/P_o$ in the oriented conventions above. Let $m(Y)$ be the conditional mean of $u_1u_2^{-1}$. By (25) the double variables have exactly their new reference distribution under the one-cell law $R_C\,d\mathrm{ref}$. After integrating the other single variables, the conditional outward-spoke law is the one just displayed when the two test auxiliaries are generated from those spokes. The internal spins have their internal Gibbs weight. The two test kernels then generate angles independently, conditional on the spins and the radii, with means $r(t_1)u_1u_l^{-1}$ and $r(t_2)u_lu_2^{-1}$. The unknown inward spoke cancels *before* any estimate. The radii still have the reference radial law, since each angular conditional integrates to one.

Use the centered test $f=r(t_1)r(t_2)Q\cdot m(Y)$. Its reference squared norm is $r(\beta)^2\mathbb E|m|^2/4$, because $Q$ is Haar there. Its mean in the one-cell law is $r(\beta)^2\mathbb E|m|^2$ by the preceding conditional calculation and (19). It remains to check that $m$ is large under the actual component reference. Generate that reference by putting back all the spokes of its free unit $k$-cube. Given its auxiliaries, the spoke integrals at different odd sites separate, so the local conditional mean really is $m(Y)$. Given the cube spokes, $y_{12}$ is Gaussian with mean $\beta(v+v')$ and covariance $\beta\mathbf1_4$, where $v=u_1u_2^{-1}$ and $v'$ is the other path of this plaquette (use the same orientation). Hence
$$
 \mathbb E\, m\cdot y_{12}=\beta(1+p),\qquad
 \mathbb E|y_{12}|^2=4\beta+2\beta^2(1+p).
$$
Here $p$ is the plaquette mean of the free unit $k$-cube. All its plaquettes are symmetry-equivalent. For the unnormalized Wilson convention their common mean is the logarithmic derivative of its partition function divided by the number of plaquettes. It is zero at $\beta=0$ and nondecreasing because the second derivative of the log partition function is a variance. Thus $0\le p\le1$. Cauchy–Schwarz yields $\mathbb E|m|^2\ge\beta/[4(1+\beta)]$.

Testing $R_C-1$ against $f$ now gives
$$
  \|R_C-1\|_8\ge\|R_C-1\|_2
       \ge2r(\beta)\sqrt{\mathbb E|m|^2}
       \ge r(\beta)\sqrt{\beta/(1+\beta)}
       >1/(5\sqrt2)\qquad(\beta\ge1).                                      \tag{27}
$$
If the eighth moment is infinite the first inequality still excludes (26). This is an obstruction on **every** even block size to this particular repair. It involves both single-crossing and double-crossing variables. Integrating out the single crossings erases it. A reference or blocking map retaining their joint correlation is a different problem.

**PROVED (fixed-rank error at weak bare coupling).** In the auxiliary presentation, at a single odd site fix one bond of one triangle and separate it from the other 23 bonds. For any fixed rank $q$, the best absolute product-reference $L^2$ error of a rank-$q$ approximation to $J_o$ across this cut tends to infinity as $\beta\to\infty$.

Here is a proof using only the three-bond marginal. Choose any $m>q$ real, continuous orthonormal functions $f_1,\ldots,f_m$ on Haar $S^3$, for example by orthogonalizing powers of the first coordinate. On one side use them on the first angular quaternion $x$. On the other use them on $z$, the inverse product of the other two angles in cyclic order. Under product reference both families are orthonormal. In the triangle marginal the three radii have independent radial law from $\lambda_\beta$. Given three independent Haar spokes and those radii, the angles are independent with densities $e^{t\omega\cdot v}/A(t)$ about the three spoke products, which multiply to 1. The radii tend to infinity in probability because the increasing radial tilt $A(t)^2$ of the Gaussian decreases the probability of $t\le M$ for each $M$, by the independent-copy covariance inequality, and the Gaussian has scale $\sqrt\beta$. The angular law concentrates uniformly about $v$ as $t\to\infty$. Outside any cap $\omega\cdot v>1-\eta$ its probability is at most $e^{-t\eta/2}$ divided by the positive Haar measure of the cap $\omega\cdot v>1-\eta/2$. In the limit $x=z$ is the Haar product of two independent spokes. Boundedness and uniform continuity therefore give $\mathbb E_{\rm ref}[J_o f_i(x)f_j(z)]\to\delta_{ij}$.

Every rank-$q$ approximation gives a matrix of rank at most $q$ in these tests. On its null space, of dimension at least $m-q$, the difference matrix has norm at least $1-o(1)$ on every unit vector. Its squared Frobenius norm is therefore at least $(m-q)(1-o(1))^2$. Bessel's inequality for the orthonormal products $f_i(x)f_j(z)$ bounds this by the squared $L^2$ error of the full tensor. Now let $m$ be arbitrarily large. The statement allows signed, coupling-dependent approximants with arbitrary one-bond basis functions. The obstruction concerns this one-bond cut and fixed-rank absolute error. The Sussman–Alpoge weak-coupling construction keeps continuous weak-field information.

## Including the plaquettes that cross one cut

**PROVED (conditional integration on the cut).** A different reference keeps *all* fine plaquettes crossing block cuts at their full coupling. Describe it in the original link variables. The graph of links crossing cuts is a product of the coordinate cut pairs and isolated coordinates, so all its components are unit k-cubes, $0\le k\le4$. This product observation also appears for three spatial directions in `gap-solve4-check-opus.md`, the check of (9). Given all the crossing links, group each noncrossing link by its ordered pair of endpoint components and its positive direction $j$. Distinct groups contain disjoint variables. Any plaquette crossing just one cut has its two noncrossing links in the same group. If the endpoint components have $k$ common near-cut coordinates transverse to $j$, the group's links are indexed by $\{0,1\}^k$ and the single-crossing plaquettes in the group are precisely its adjacent pairs. To verify the indexing, fix the two $j$ coordinates of the endpoints. In each of the other directions there is either one fixed coordinate or a choice of its two cut values. Changing one choice moves to the other noncrossing link of exactly one single-crossing plaquette. Thus integration of the noncrossing links in the crossing-only reference factors conditionally over these groups. The double-crossing plaquette action stays inside each component. The groups with $k=0,1$ have conditional mass 1 for normalized Wilson weights by Haar integration. Larger groups can have nonconstant mass.

**PROVED (an order-one estimate for a codimension-two sheet).** For $k=2$ denote the two parallel square holonomies in the endpoint components by $h,h'$. The conditional integral of the four noncrossing links is
$$
 V_\beta(h,h')=\int w_\beta^{*4}(h u h'^{-1}u^{-1})\,du
              =1+\sum_{j\ge1}r_j(\beta)^4\chi_j(h)\chi_j(h'),              \tag{28}
$$
where $j$ is twice the spin, $\chi_j$ has dimension $j+1$, and $r_j=I_{j+1}(\beta)/I_1(\beta)$. For the first equality change the frame successively at the four vertices of each square to set three edge transports on each side to 1. This changes the four integrated links by left and right Haar translations. Integrate three of the resulting four kernels by convolution and integrate the last link by Haar. For the second equality use the normalized one-link coefficients of Sussman and Alpoge with Claude and Codex, outline GL3–GL4, lines 2197–2239, also noted in `gap-transfer.md`, Remark 2.6. Haar conjugation of the irreducible matrix of $h'^{-1}$ gives its trace divided by $j+1$ times the identity. The factorial series in GL3 gives absolute convergence.

Here are rational bounds uniform for $0\le\beta\le7/3$, using the continuous value at zero. $r_1=r$ and $r_2=\tau$ of (11) since $\chi_2=4q^2-1$. Both increase, so bound them at $\beta=7/3$. Set $x=7/6$, $Y=49/36$ and $z=11/8>Y$. We have $A(7/3)\ge1+Y/2+Y^2/12+Y^3/144>37/20$. The GL3 series bounds both numerators.
$$
 \frac{I_2(7/3)}{x}
 \le x\left(\frac12+\frac z6+\frac{z^2}{48}
                +\frac{16z^3}{15\cdot720}\right)<\frac{181}{200},
 \qquad
 \frac{I_3(7/3)}{x}
 \le z\left(\frac16+\frac z{24}+\frac{z^2}{240}
                +\frac{16z^3}{15\cdot4320}\right)<\frac{33}{100}.
$$
After the displayed first tail term each successive ratio is at most $z/(4\cdot6)<1/16$. Since $I_1(7/3)/x=A(7/3)$ this yields $r_1<49/100$, $r_2<9/50$. For $j\ge2$, GL4 gives $r_{j+1}/r_j\le (7/6)/(j+2)$. Successive terms $(j+1)^2r_j^4$ then have ratio at most $(4/3)^2(7/24)^4<1/64$. It follows from $|\chi_j|\le j+1$ that
$$
 |V_\beta(h,h')-1|\le d_*=
 4(49/100)^4+(64/63)9(9/50)^4<1/4.                                          \tag{29}
$$

At a crossing-link component with exactly two near-cut coordinates the only nonconstant groups incident to it point along its two other coordinate axes. There are at most four such groups. On the interior of that sheet the square holonomy has a one-site law times the four factors (28), conditional on its neighbours. This follows by fixing a tree of the square, leaving its single Haar holonomy. Arbitrary positive one-site weights are allowed. Changing one neighbour changes the conditional law in total variation by at most $d_*$. In detail, for two unnormalized weights their ratio lies in $[a,b]=[(1-d_*)/(1+d_*),(1+d_*)/(1-d_*)]$. If the ratio has mean $s$ in the first probability, the chord bound for the convex function $|t-s|$ bounds total variation by $(b-s)(s-a)/(s(b-a))$. Its maximum is $(\sqrt b-\sqrt a)/(\sqrt b+\sqrt a)=d_*$. The one-site Dobrushin row sum is thus strictly less than one at the Wilson window on this part of the reference. The reference includes the mixed plaquettes of (27). Estimate (29) covers the groups with two common transverse cut coordinates.

**OPEN (full action).** The same grouping has $k=3$ groups with eight transported spins between endpoint components. Their normalizers couple higher-codimension holonomies. More importantly, reintroducing the plaquettes wholly inside the original boxes couples different groups of noncrossing links. Their product no longer factors in the conditional integral used for (28). Controlling those couplings in a class preserved by merging is necessary for this reference to give a block step for the full Wilson action. Inequality (29) bounds one part of that calculation.

## Checks and the first-passage obligation

**PROVED (two normalization checks by hand).** Keep just one edge of strength $s$ in (16). Its two active sites give $P=1-(s^2/4)t_1t_2$. The coefficient in (17) divided by its two radial factorials is $(s^2/4)^k/[k!(k+1)!]$, reproducing the single-edge Haar integral $A(s)$. In the flat eight-spoke calculation, after the 24 one-edge factors have been normalized, the leading nonconstant term comes from the 32 triangles. A monomial on distinct edges with a degree-one vertex averages to zero. At order three the only surviving connected supports are triangles. A thrice-used edge has zero third moment and a double edge with a separate single edge also integrates to zero. For one triangle the moment is $1/16$ by two successive uses of $\mathbb E uu^t=\mathbf1_4/4$. Thus (20) starts with $2\beta^3$. The lower bound (21) has the same leading coefficient since $r(\beta)=\beta/4+O(\beta^3)$.

**OPEN (the missing Wilson step in CH).** Equations (13) and (16)–(18) give the exact mass-preserving cubical map on a pure Wilson weight and a uniformly accurate finite polynomial for its interior integral at order-one coupling. Equations (22)–(23) say exactly how to certify gluing errors for correlated boundary functions at a fixed coupling. The candidate constant endpoint and the candidate corrected by integrating double crossings fail by (24) and (27). The full crossing reference gives (29) on a sheet but has an uncontrolled response when the interior plaquettes are restored. I have no estimate putting the full next-scale Wilson presentation into a class with a certified continuation through the band.

There is also a precise entry issue. In the Sussman–Alpoge first-passage definition, outline 6854–6861, $x_0$ is the bare inverse coupling. Under the account's stated hypotheses, CA-I 56439–56458 and 56530–56547 give $x_0-x_K\ge\lambda_\sharp K-c_5$ and $x_K>g^{-2}$, so the bare inverses grow on the cutoff tail. A uniform bounded-rank initialization at that bare scale in the auxiliary $L^2$ scheme is excluded above. At the last admitted scale, CA-I 2562–2582 gives a sum over histories with a background action and localized terms. It preserves the original mass. No estimate here gives that family a common local input of the kind needed by (9) or (22), with constants uniform for all late cutoffs on both tori. A finite calculation at the pure Wilson coefficient $23/10$ cannot supply that missing identification. The exact maps use no (UNIV-K). Row 1335 would apply the transfer estimate to the bare masses after the uniform bound, with the subsequent continuum and observable-sector premises still required. No Lean kernel check or large computation was run. The cost bounds above count arithmetic operations in the specified representations.

RESULT: OPEN. A $2\times2\times2\times2$ Wilson block has an exact mass-preserving map and a uniform order-one polynomial enclosure below $7\cdot10^{14}$ rational arithmetic gates. The tested finite closures fail by explicit boundary correlations, including after the corner correction. Uniform entry and propagation from the first-passage Wilson densities into a robust end class remain open. This row establishes neither (SEED-L) nor the Jaffe–Witten mass gap and grants no status.
