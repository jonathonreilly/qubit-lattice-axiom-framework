# Repo search

Pinned lane `27074b3a5`, row 1418. I searched Markdown and TeX on `origin/main` (8b11ae2bb95e), `pr/10114` (f76f6c649cff), `pr/10133` (89faef229ff6), `pr/10134` (1e70c7211a2c) and `pr/10141` (c73ad7b177d9). The target-specific prior inventory is absent. The searches for Ebel/Kennedy, 2506.03247, Koch/Wittwer, Lanford with fixed point or renormalization, computer-assisted block/tensor RG, Yosprakob, armillary sphere and bond Gram matrices returned no matches in their targeted queries. Terms for the statement were order-one block/RG, K-flow, UNIV-K, M-neutral, gauge tensor truncation and “the crux is the middle”. Method terms included Oeckl, Pfeiffer, Haar/intertwiner, spin foam and disentangling.

| Relevant hit | What it supplies and how close it comes |
|---|---|
| Main, `research/mass-gap/library/gap-crux-fp.md:94` | Theorem S improves a seed quadratically once it is in its small basin. The weak endpoint controls a different observable. This is the missing band inequality. |
| Main, `research/mass-gap/library/prior/gap-seed-lit.md:51` and `gap-math-lit.md:96` | Plaquette characters and link intertwiners give an exact signed dual sum. Positive character coefficients do not bound its mass ratio. The lane's `gap-means-astra.md` §3.2 already asks for the connected estimate after gluing. |
| Main and the PR refs, `docs/PLAQUETTE_ENVIRONMENT_QUOTIENT_EQUIVARIANCE_NARROW_THEOREM_NOTE_2026-06-12.md` 99–125, `GAUGE_VACUUM_PLAQUETTE_TENSOR_WORD_MULTIWORD_PERRON_LADDER_BOUNDED_NOTE_2026-06-11.md` 65–79 and `SU3_FUSION_ENGINE_PR1_THEOREM_NOTE_2026-05-03.md` 173–188 | Respectively, complete labelled cells can be quotiented by the marked geometry's stabilizer, two different finite singlet-word contractions have different dimension factors, and the SU(3) fusion API supplies finite multiplicities. None encloses a four-dimensional RG image. Main's `BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md` 13–30 already proposes truncating the recoupled network and gives a 2D SU(3) benchmark. Its 4D contraction remains open. |
| Pinned lane, `gap-blockstep-astra62.md` and `gap-blockstep-check-opus.md`, rows 1341/1344 | The pure Wilson cube interior already has a uniform polynomial enclosure below $6.6\cdot10^{14}$ gates. Their boundary-gluing test is separate. The remaining target here is an **iterable signed boundary calculation** and its error budget. |

The Nov 8 [repository digest](prior/repo-search-2026-11-08.md) also points to the soft-route `MASS_GAP_LOCAL_BLOCK_ASTRA.md` on PR 10114, which gives a positive one-step loop witness. It gives a lower correlation bound. Registry entries B109-last-scale and B122b-last-scale cover the quotations in CA-II 64593–64601. No matching owner or completed sizing of this boundary calculation was found. The FINISH row contains the named comparison rows and no separate “Repo prior work” text.

# Computer-assisted SU(2) block step at intermediate coupling

**Decision. A bare order-one block is finite. The cost and the error estimates rule out two implementations of the carry.** At $\beta=2$, error at most $1/4$ needs bond rank at least 67 in the chosen site tensor. A dense site at that rank stores 406,067,677,556,641 entries, about 13 PB. A factored rank-128 implementation has affordable arithmetic for a trial window, but 166 resolved boundary channels and inequality (2) force its scalar error radius above the endpoint tolerance after eight doublings. A sectorwise, signed verifier is buildable. Whether it encloses the actual first-passage action in the band remains open.

Research sizing, 2026-11-22. New arguments are hand derivations without an independent scientific check. Exact inventories and the runnable fixture below have no Lean-kernel receipt. The plan saved at creation was to identify the precise consumer, read the primary RG constructions, bound the finite part and its tail, then design a checker and its first acceptance test. The account source snapshot is identified in the request as `31a47c543775`.

## What the existing results supply

- Row 1326 and check 1331 sized a direct finite-torus seed. The state count is an explicit-vector cost. A cut-dependent signed correction to the Gaussian comparison remains possible. Here the object to be sized is the open boundary of a *local* block before a global trace. [Seed sizing](gap-verified-compute-sizing-fable.md) · [Its corrections](gap-verified-compute-sizing-check-astra.md)
- Row 1332 and check 1335 give two distinct consumers. Theorem T needs a finite time-doubling KER inequality at its own window pair plus A0–A3. A2 ranges over every bare coupling above the window, with a common margin and an exponential upper bound on size. Proposition CH instead transports both unnormalised masses of every admitted first-passage datum to an end class. A single intermediate tensor enclosure is one inclusion in that chain. [Theorem T and CH](gap-shrink-box-fable.md) · [Check 1335](gap-shrink-box-check-astra.md)
- In the Sussman–Alpoge outline (with Claude and Codex), SA 394–408 states the mass/observable distinction, 4075–4084 states obligation C4, and 7501–7524 gives the proposed activity class subject to coupling and formation assumptions. SA 17282–17285 and CA-I 2574–2582 identify the masses. CA-I 2533–2547 gives the window under the admitted flow. CA-I 4209–4239 quotes Bałaban's UV stability with every effective coupling at most the small ceiling. The account records that the proof invoked for a possible removal of this hypothesis was unpublished. These source ranges came through SA-index chunks 01, 04, 07, 16, the obligations list and the CA index. No one-parameter Wilson form for the terminal density follows. The lane quotation record is secondary. [Outline, invariant class](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L7501-L7524) · [CA-I, UV theorem](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4209-L4239) · [Bałaban quotations](lit-balaban.md)
- Row 1386 §4.4 calls an intermediate-coupling theorem K-II, distinct from a sign theorem (K-I) and a direct verified seed evaluation (K-III). Row 1394 located rigorous model problems. Its original search had no access to these lane and account files. Row 1367 requires a neutral thermal trace on one physical side at all late cutoffs. [Literature row 1394](prior/gap-carry-lit-luna.md)

## The closer block calculation

Row 1341 already constructs a mass-preserving cubical Wilson integral. Check 1344, §§1–3, gives absolute error below $2^{-24}$ on $0\le\beta\le7/3$ in fewer than $6.6\cdot10^{14}$ rational gates for its seven-index circuit. This is an error bound on the function with open boundary arguments. It is no budget for contracting the functions on neighbouring blocks. Row 1341 also exhibits 49 modes in its face test. Checks of rows 1340, 1345, 1348 and 1351 preserve their conditional end tests, signed/centre gluing or finite angular core, and leave entry of the interacting Wilson law open. In particular check 1352 has a neutral end class at coarse side about $2^{36}$. The present calculation sizes a different representation of the *shared* boundary. Computing another isolated Wilson integral would duplicate row 1341. [Row 1341](gap-blockstep-astra62.md) · [Check 1344](gap-blockstep-check-opus.md) · [Finite angular core](gap-blockstep3-check-opus.md) · [Neutral end class](gap-blockstep4-check-opus.md)

## Original methods and the choice of space

Lanford's degree-20 even polynomial and controlled sequence tail give a Newton-like proof for a scalar period-doubling equation. The physical RG map itself need not contract. Koch and Wittwer treat the three-dimensional hierarchical Dyson–Baker scalar model. Their exact hierarchical recursion does not integrate a shared six-plaquette link. Ebel, Kennedy and Rychkov's nonhierarchical square-lattice construction uses gauge changes, disentangling, splitting and a rigorous master map on 63 sector bounds. In Theorem 3.1 the initial componentwise bound is $0.02$. The comparison of iterates **16 and 15** gives the multiplier $0.96$. Each of the 63 entries bounds an infinite-dimensional sector. The authors supply working code for their two-dimensional map. The present tool needs a four-dimensional contraction and a separate error theorem for its compression. These primary texts were read online. [Lanford, pp. 429–431](https://people.math.harvard.edu/~knill/history/lanford/papers/LanfordCollectedWork.pdf) · [Koch and Wittwer](https://web.ma.utexas.edu/users/koch/papers/dyson.pdf) · [Ebel, Kennedy and Rychkov, §§2–3](https://arxiv.org/html/2506.03247v2) · [Authors’ code](https://github.com/ebelnikola/2x1)

Use a site tensor for the **Boltzmann weight**. This avoids taking a logarithm of a possibly signed tensor entry. The tensor is a local presentation of the full partition function. Keeping every intertwiner on a bond allows neighbouring blocks to share its correlations. This is the exact dual construction of Oeckl and Pfeiffer. Local colour contractions can have either sign. The connected-activity endpoint proposed in this lane by `gap-means-astra.md`, §3.1, still applies once the entire coarse integral is controlled. [Dual transformation, §§2–3](https://arxiv.org/html/hep-lat/0110034) · [Prior endpoint](gap-means-astra.md)

## The block, the norm and a finite bare calculation

Write $n=2j$, $d_n=n+1$. Divide each Wilson plaquette weight by its vacuum character coefficient $c_0=2e^{-\beta}I_1(\beta)/\beta$, keeping $c_0^{\#p}$ in the mass. The resulting character coefficients are $b_n=d_n I_{n+1}(\beta)/I_1(\beta)$, $b_0=1$, with the continuous value at zero. This is GL3–GL4 of SA 2195–2243 (index chunk 02), with dimension times convolution eigenvalue. Each link sees six plaquettes. Its bond label is their **ordered** six spins and a basis vector in the invariant subspace of their oriented tensor product. Haar integration gives the orthogonal projector onto that subspace. At each vertex contract the eight incident intertwiners, respecting duals and matching the spins at each of 24 plaquette corners. Attach $b_n^{1/4}$ per corner. The resulting real signed tensor $A$ has $A_{0\ldots0}=1$. Four corners restore the weight exactly. This is the Oeckl–Pfeiffer representation, including its magnetic-index contractions.

Use $\mathcal H=\ell^2(\{\text{bond labels}\})$, and the Hilbert–Schmidt norm on $\mathcal H^{\otimes8}$. A local centre $C$ is a finite real tensor, with an absolute radius $\|A-C\|_2\le\eta$. A single scalar vacuum sector and the $2^8-1=255$ choices of nonvacuum legs can be bounded separately. Each bound covers all multiplicities in its sector. The entries of $C$ are counted separately. An effective Wilson action generally contains multiloop terms. The proposed representation accepts it only with a local tensor presentation, or an exact enlargement of the bond space with the corresponding tail estimate.

A factor-two block collects the 16 sites in $\{0,1\}^4$. Sum every shared bond once (32 internal bonds), leaving 64 external bonds in eight bundles of eight. Pick the same real isometric identification $\mathcal H^{\otimes8}\simeq\mathcal H$ on both ends of each coarse bond, with compatible orientations. It preserves the **untruncated** contraction. Four successive pair fusions, one per axis, implement the same grouping up to relabelling. A complete change of basis on a bond is exact. Projection onto the first $r$ coordinates is an approximation to the tensor in its norm enclosure. Restore every positive normalization in the exact masses. Vacuum factors cancel on a paired cover only if the assignments on the larger torus are the lifts of the smaller ones.

**A tail one can actually bound.** For the bare input at $0\le\beta\le5/2$, GL4 gives $b_n\le(5/4)^n/n!$. Pairing tensors along all shared indices is bounded by the product of their Hilbert–Schmidt norms, by matrix Cauchy–Schwarz. This applies successively to a graph without self-loops by contracting all edges between the two pieces at each merge. In the vertex tensor an entry for fixed corner spins is thus bounded by $\prod b_n^{1/4}$. Each link has at most the product of its six representation dimensions in multiplicities. Each corner occurs on two incident links. Put
\[
 h_n=(n+1)^2\sqrt{(5/4)^n/n!},\quad H=\sum_{n\ge0}h_n,\quad T_N=\sum_{n>N}h_n .
\]
Then $\|A\|_2\le H^{12}$ and $\|A-A_{\le N}\|_2^2\le24T_N H^{23}$ by the union bound over corners. Cauchy–Schwarz and $\sum(n+1)^4/2^n=300$ give $H^2\le300e^{5/2}<128^2$. This also justifies taking the finite-volume character expansion to its limit. The bound concerns the full local tensor, an extra step beyond the one-plaquette tail in check 1331.

For a conservative, fully specified benchmark take $N=2048$. The ratio $h_{n+1}/h_n<1/2$ for $n\ge2049$. The inequalities $2049!>1024^{1025}$, $(5/4)^{2049}<2^{683}$ and $2050^2<2^{24}$ give $T_N<2^{-4758}$. Hence $\|A-A_{\le N}\|_2<2^{-2290}$. Telescoping the 16 multilinear inputs costs at most $16(2^{84})^{15}$, since both input norms are below $2^{84}$. In **unrenormalised block-tensor units after removing the plaquette scalars**, the following finite target has a uniform analytic truncation error:
\[
 \sup_{0\le\beta\le5/2}
 \|\mathcal R(A_\beta)-\mathcal R(A_{\beta,\le2048})\|_2<2^{-1000}.
\]
This gives a concrete one-step statement for **effective actions with a certified remainder**. At each of the 16 sites allow a normalized tensor in $\|A_x-A_\beta\|_2\le2^{-1400}$, including spatially differing perturbations, at common $\beta\in[2,7/3]$. The image lies within $2^{-120}$ of the finite tensor $\mathcal R(A_{\beta,\le2048})$. The extra term is at most $16(2^{84}+1)^{15}2^{-1400}<2^{-121}$ before adding $2^{-1000}$. The radii price one guaranteed inclusion. Entry of the actual first-passage family into this tube and a seed property of its image are both open. The spin series supplies the bare part. For general inputs, (1) below handles the remaining tensor error.

## What must be stored and multiplied

With $0\le n\le N$, let $D_N$ be the number of bond states. It is the singlet multiplicity of $(\bigoplus_{n=0}^N V_{n/2})^{\otimes6}$. In the torus weight variable $z$ the multiplicity is weight zero minus weight two. Multiplying the one-factor character by $z^N$ gives $(1-z^{N+1})(1-z^{N+2})/[(1-z)(1-z^2)]$ by summing the finite geometric series. Symmetry of weights yields the integer inventory formula
\[
 D_N=[z^{6N}]\frac{(1-z^{N+1})^6(1-z^{N+2})^6}{(1-z)^6(1-z^2)^5}.
\]
For $N=1$ the counts by number of occupied plaquettes are $1,15,30,5$ for $0,2,4,6$ fundamentals. This uses the singlet multiplicities $1,1,2,5$ already used in check 1331. It is a six-plaquette **local link** count.

| Spin cutoff $N=2j_{\max}$ | Bond states $D_N$ | Dense site $D_N^8$ | Open block $D_N^{64}$ | Direct summands $D_N^{96}$ |
|---|---:|---:|---:|---:|
| 1 | 51 | 45,767,944,570,401 | $1.93\,10^{109}$ | $8.45\,10^{163}$ |
| 2 | 977 | $8.30\,10^{23}$ | $2.26\,10^{191}$ | $1.07\,10^{287}$ |
| 2048, sufficient for the bare benchmark | 7,467,515,903,828,308,564,331,208,705 | $9.67\,10^{222}$ | $7.64\,10^{1783}$ | $6.68\,10^{2675}$ |

The last column counts boundary assignments times internal assignments in literal enumeration. Each summand has 16 factors and an accumulation. A materialised block uses $32D_N^{64}$ bytes under the optimistic assumption of two 128-bit fixed-point endpoints per real coefficient, common scale and no metadata. Streaming removes that storage requirement from a scalar calculation. All operation counts below are scalar multiply-adds or gates as specified, before big-integer bit cost, certificate serialization and kernel overhead. Even the $N=1$ site takes about 1.46 PB in this dense layout.

**A less wasteful implementation.** At $N=1$ the vertex figure is $K_{2,2,2,2}$, with the eight oriented link ends as nodes and the 24 corners as edges. An occupation pattern is an even subgraph, so only $2^{24-8+1}=131{,}072$ patterns occur. For pattern $F$ the number of structurally admissible entries is $\prod_v {\rm Cat}(\deg_F(v)/2)$. Entries may still vanish after recoupling. Enumerating the non-tree edges of a spanning tree and completing the tree edges by parity gives **12,910,079 slots** (413,122,528 bytes of endpoint payload). The histogram below also specifies how to reproduce the count: fix one of the eight legs, group by its six-bit pattern and by its intertwiner, and tally the choices on the other seven legs. For each even $F$ add $\prod_{v\ne v_0}{\rm Cat}(\deg_F(v)/2)$ to each compatible label on the fixed leg.

| Compatible slots on the other legs | 50,920 | 114,551 | 115,144 | 262,978 | 265,805 | 635,318 |
|---|---:|---:|---:|---:|---:|---:|
| Number of fixed-leg labels | 1 | 3 | 12 | 6 | 24 | 5 |

The first moment gives the site count. The second gives **4,329,800,859,159** matched pairs for the direct sparse join of two sites in the half-spin core, prior to extra zero tests. There is a cheaper calculation for its *unprojected squared norm*. For $Y_{IJ}=\sum_\alpha A_{I\alpha}B_{\alpha J}$ it is the trace of the two bond Gram matrices multiplied together. Different six-spin patterns have disjoint row support. There are only $1+15+15\cdot2^2+5^2=101$ ordered Gram entries. Each site's accumulation costs at most $5\cdot12{,}910{,}079$ real multiply-adds once its recoupled values exist. This saving applies to the norm of a pair. An outgoing projection or the next pair changes the diagram. The histogram and large counts are sizing arithmetic with a reproducible finite sum, without a Lean run.

## A lower bound that survives a change of bond basis

Fix the Wilson site tensor at $\beta=2$, in the vacuum normalization above. Flatten it across one oriented link versus the other seven. The following minor is a test of the accuracy of **any** rank-$r$ approximation across this bond, with arbitrary signed coefficients. It differs from row 1341's resolved-staple and face tests.

Fix the leg $+1$. The six plaquettes at that link correspond to $+2,-2,+3,-3,+4,-4$ at the vertex. Choose two of them and put the same nontrivial spin $n/2$ on both. Their link singlet is unique.

- Twelve choices use two different transverse axes. Occupy the three corners of the triangle on the vertex figure formed by those two legs and $+1$.
- Three choices use the opposite ends of one transverse axis. Occupy the square on $+1,+\mu,-1,-\mu$.
- All other spins in the chosen column are zero. Include also the vacuum row and column. The other seven legs fix the six spins on $+1$, so the selected columns couple to their designated rows only. Distinct choices of spin and pair give distinct orthonormal rows and columns.

For a cycle of length $k$, orient the representation lines consistently and contract the unit two-line singlets. There is one free index, giving magnitude $d_n^{1-k/2} b_n^{k/4}$. Reversing a self-dual basis can change a sign. Thus the triangle entries have magnitude $b_n^{3/4}/\sqrt{d_n}$ and the square entries $b_n/d_n=I_{n+1}/I_1$. The vacuum entry is one. The surface integral in the earlier `gap-kappa-order.md`, §2 and Lemma T, already contains the dimensional factor on unbranched surfaces. The new use is the diagonal minor with distinguishable columns. [Prior surface calculation](gap-kappa-order.md)

At $\beta=2$, GL4 gives $b_n\le1/n!$ and the triangle is at least as large as the square. From the positive series $I_1(2)<2$ and $I_{n+1}(2)>1/(n+1)!$. For $n=1$ all 15 entries exceed $1/4$. For $n=2$, $I_3(2)>5/24$ and $I_1(2)<5/3$ (after $1+1/2$, bound the tail by $(1/12)/(1-1/12)$). All 15 additional entries exceed $1/8$. For $1\le n\le5$ each exceeds $1/1440$. On any $k$ selected rows with diagonal magnitudes $>a$, a rank-$r$ approximation with $r<k$ has squared Hilbert–Schmidt error $>(k-r)a^2$ on that minor. Restrict to the kernel of the approximating minor, or apply the singular-value variational principle. Restriction cannot increase the whole-tensor error.

| Requested absolute local error | Necessary bond rank at $\beta=2$ |
|---|---:|
| $1/4$ | at least 16 |
| $1/8$ | at least 31 |
| $1/2048$ | at least 76 |

In particular, discarding spin one at the half-spin cutoff loses a single triangle of magnitude $>1/8$. An $N=1$ sparse run can validate signs, gluing and inventories, but its tail must be supplied before any inference for the Wilson action. High rank at a local leg does not imply high rank for a scalar mass ratio, for a factored dictionary, or after a transformation acting across that cut.

**Cost of dense compression.** A directional fusion of two sites of bond rank $r$ produces 14 open indices before compressing the six paired transverse legs. A direct dense multiply uses $r^{15}$ multiply-adds and $32r^{14}$ bytes for that intermediate. At $r=3$ this is 14,348,907 multiply-adds and 153 MB, but the raw Wilson tensor fails the local error test. Already at $r=16$ one direction has $2^{60}$ multiply-adds and $2^{61}$ bytes (2 EiB). The retained site alone costs $2^{37}$ bytes (128 GiB). The row-1332 comparison budget is about $10^{15}$ exact operations and this laptop has 8 GB of RAM. This rules out the stated dense implementation with error at most $1/4$ on the raw $\beta=2$ chart. It uses one local block and one local Schmidt cut, independently of the size of a seed torus. Sparsity, changing the cut, summing the two masses together and signed cut-dependent Gaussian references are outside that conclusion.

**Why simple regrouping also misses contraction.** At the product tensor $V=e_0^{\otimes8}$, perturb in the unit triangle component with nonvacuum legs $+1,+2,+3$. In the derivative of the raw $2^4$ block, a single perturbation survives at exactly two vertices: all three positive legs must point outwards and the fourth coordinate is free. Their outgoing labels occupy different microscopic positions and are orthogonal. The vacuum scalar has zero derivative there, so the output derivative has norm $\sqrt2$. The reflected sum over triangle orientations has the same factor at first order, by disjoint supports. An arbitrary identification of each bundled leg by a unitary preserves this norm. Thus a claim of contraction in a fixed raw HS ball about $V$ already fails at its centre. For the single directed perturbation $V+tC$, every closed periodic contraction equals one, since an active outward leg always meets a vacuum-only incoming leg. Tensoring this redundant presentation onto a Wilson network leaves its masses unchanged. A local HS certificate is a genuinely stronger, presentation-dependent condition than a seed. This calculation does not restrict a signed change of presentation across bonds or a chain of inclusions away from $V$.

## A tool to build instead of the dense table

**Certificate for one inclusion.** Give two finite centres $C,D$, radii $\eta,\xi$, an outgoing centre $C'$, radius $\eta'$, oriented face embeddings, and the exact order of the pair fusion. The inputs range over *all* tensors in these balls in the specified gauges. On each paired transverse face supply a real isometry $W_e:\mathbb R^r\to\mathbb R^{r^2}$, the same on its neighbouring block, with a distinguished unit vacuum. Embed the two axial legs identically. Write $W$ for this product inclusion. Its orthogonal complement remains part of the exact coarse Hilbert space. Normalize $C'$ to vacuum entry one. Set $Y_*=\operatorname{pair}(C,D)$ and let $z_*$ be its outgoing vacuum component in the specified basis. The following are directly verifiable strict or weak inequalities, with rational outward endpoints:
\[
 \begin{split}
 e&=\|C\|_2\,\xi+\|D\|_2\,\eta+\eta\xi,\qquad z_*-e>0,\\
 t^2&\ge\|Y_*\|_2^2-2z_*\langle Y_*,WC'\rangle+z_*^2\|C'\|_2^2,\quad t\ge0,\\
 t+(1+\|C'\|_2)e&\le\eta'(z_*-e). \tag{1}
 \end{split}
\]
For the actual pair $Y$, multilinearity gives $\|Y-Y_*\|\le e$, hence $|z-z_*|\le e$. The triangle inequality gives $\|Y/z-WC'\|\le\eta'$. The exact scalar $z$ goes into the partition function. This proves a map on a ball when (1) passes. Importantly, the norm of $Y_*$ includes every outgoing coordinate, including the finite part lost by the isometries. Checking only the projected tensor would give an incorrect certificate. Analytic tails of both arbitrary inputs are charged in $e$; the bare factorial bound is used only where its hypotheses hold.

**Factored signed centres.** Store each centre as a sum of $H$ weighted products of eight real $r$-vectors. This format allows negative interference before taking a norm. The site costs $H(1+8r)$ coordinates, as against $r^8$ dense. Compute a single-leg Gram matrix of each input from products of the seven other leg inner products. The first term in (1) is $\operatorname{tr}(G_C G_D)$ in compatible real bases. For the mixed term, for each output product $l$ and each of six transverse directions form the $r\times r$ matrix obtained by reshaping $W_e u'_{le}$. Premultiply and postmultiply by the two lists of input leg vectors. Their entries are the overlap for every pair of input products $h,k$. Multiply the six numbers, the axial overlaps, shared-bond inner product and weights, then sum over $h,k,l$. The other norms are products of eight leg dot products summed over two indices. This evaluates (1) without forming the output tensor or a $H^4$ sum. Equality of the exact masses is the graphical contraction identity, independent of success in (1).

For a priced trial choose $r=H=128$, absolute HS radii, rational or certified algebraic face maps and dyadic interval endpoints. There are **131,200 centre entries**, plus at most $6r^3=12,582,912$ isometry entries per directional fusion and the radii. The mixed term uses at most $6(Hr^3+H^2r^2+H^3r)$ scalar multiply-adds for the transverse matrix products, plus order $H^3$ products and the smaller Gram and axial computations. Direct checks of six $W_e^tW_e=I$ add at most $6r^4$ multiply-adds. An allowance of $10^{10}$ scalar multiply-add equivalents per ordered pair covers these operations at the stated sizes (count each standalone product or sum as one equivalent). The streaming workspace at 32 bytes per stored scalar is under 0.6 GB for six isometries, three centres and work matrices reused one output product at a time. This excludes big-integer temporary limbs, the Lean runtime and proof objects. Choosing larger mantissas multiplies payload accordingly. Orthogonality is an exact identity in a certified representation, e.g. a rational Householder product. Intervals containing zero in off-diagonal Gram entries alone do not prove orthogonality.

As an engineering scenario, 16 parameter subintervals in $[2,7/3]$, eight isotropic steps and four directions give 512 bulk inclusions, at most $5.12\cdot10^{12}$ scalar operations at that rank. Distinct isometries for every inclusion require about 206 GB of witness payload at 32 bytes per scalar, streamable or shareable. For $M$ required ordered fusions including geometry types the corresponding checker budget is $10^{10}M$, with input generation, admission, bit precision and the analytic proof additional. An interval subdivision encloses a continuum of parameters only with a proved interval extension and coverage at common endpoints. A certificate covering this trial window would cover just that window. The actual number of scales, cells, ranks, precision and the cost of obtaining an initial ball for all the account's histories are unknown. Thus the finite arithmetic design fits the nominal operation budget in this scenario. An end-to-end feasible Yang–Mills certificate has not been exhibited.

On odd side lengths pair sites and use one group of three in that direction. A triple needs two signed pair inclusions, the second with the untouched third input. Store short/long cell and face types, and use one face isometry shared on its two sides. Lift the tiling and face assignments from the small torus to the comparison cover. This gives an exact untruncated layout; it requires additional (1) entries for *every* realized mixed pair and scalar. In particular the account's $2L^m$ with $L$ odd does not license eight successive homogeneous dyadic steps. A missing seam or entry proof is a failing certificate, and the 512 count covers homogeneous bulk only.

**Admission and signed compression are the hard parts.** For a bare Wilson input, an exact fallback for admission into a given centre is its full norm, the centre norm and their mixed overlap, using the truncated spin sum plus the analytic tail. The $N=2048$ row prices a sufficient dense realization before compression. The half-spin sparse block gives a much cheaper way of testing recoupling code. For $\rho_K$ one needs an equality (or a local expansion with bounded remainder) that puts the *entire* effective density, including vacuum factors, histories and interactions between blocks, into the selected local tensors. The existing bare cubical circuit can serve as a local integration primitive or benchmark. Substituting a Wilson action at its recorded effective coupling would discard this admission problem. An exact change of presentation across neighbouring bonds could reduce the ranks or radii; it needs its own cancellation identity and error bounds. The finite test (1) returns either a verifiable inclusion or an unresolved interval. A wide interval does not refute the underlying dynamics.

### The priced rank-128 trial fails its own error test

The failure can be seen before constructing the $5.12\cdot10^{12}$-operation transcript. First enlarge the minor above. Write $u_n=b_n^{3/4}/\sqrt{d_n}$ for a triangle. Allow two triangles that meet only at the distinguished leg. In its invariant space take the tensor product of their two normalized singlets as the selected row vector. The column has a unique two-line singlet on each of its four active legs. Its designated entry has magnitude $u_nu_m$. Columns for different six-spin patterns have orthogonal row support even before choosing a basis within each pattern.

At $\beta=2$, $u_1>2^{-5/4}>2/5$, $u_2>1/8$, and $u_3>(1/12)^{3/4}/2>1/16$. The last bound uses $b_3=4I_4/I_1>1/12$. Select the following orthogonal rows and their columns.

| Rows | Count | Reason |
|---|---:|---|
| Vacuum and all one-cycle pairs with $n=1,2$ | 31 | The preceding minor |
| Two fundamental triangles | 15 | Choose four of six legs. They can always be matched in two pairs on different axes |
| One triangle with $n=1$ and the other with $n=2$ | 60 | 12 choices of the first cross-axis pair, then five cross-axis pairs on the four remaining legs |
| One triangle with $n=1$ and the other with $n=3$ | 60 | Same count, different spin patterns |

All 166 diagonal magnitudes exceed $1/40$. For example the smallest of the displayed product bounds is $(2/5)(1/16)$. A rank-128 centre therefore has **absolute error greater than $\sqrt{38}/40>1/8$**, even after optimizing its single-leg bases. The 166-row test strengthens the one-cycle ranks to at least 67, 142 and 166 at errors $1/4,1/8,1/2048$, respectively. At the strengthened floor $r=67$ the dense engine would perform $67^{15}>2.46\cdot10^{27}$ multiply-adds for one directional fusion. Its open intermediate alone has $67^{14}$ entries and requires more than $1.17\cdot10^{27}$ bytes in the stated layout. Both bounds use selected coefficients and integer counts.

The same witness prices relative errors. In the squared norm of the site tensor, sum the two copies of each link intertwiner over their common label. This reinstates the Haar projector at each of the eight leg ends. Each corner then contributes a trace of a product of two unitary representation matrices (with the appropriate duals), of modulus at most $d_n$, times $\sqrt{b_n}$. Applying the bound first in a finite spin sum and then taking its limit gives
\[
 \|A_2\|_2\le\left(\sum_{n\ge0}(n+1)/\sqrt{n!}\right)^{12}
 \le(\sqrt{12}\,e)^{12}<10^{12}.
\]
Here $\sum(n+1)^2/2^n=12$ and $e^2<8$. For an enclosing rank-128 centre, $\|C\|\le\|A_2\|+\eta$ and $\eta>1/8$ imply $\eta/\|C\|>1/(8\cdot10^{12}+1)>2^{-43}$.

Finally, every use of (1), regardless of the chosen output, has
\[
 \frac{\eta'}{\|C'\|}\ \ge\ \frac{\eta}{\|C\|}+\frac{\xi}{\|D\|}.
 \tag{2}
\]
Indeed $z_*-e\le z_*\le\|C\|\,\|D\|$ and $1+\|C'\|\ge\|C'\|$. After eight complete dyadic blockings a bulk output uses $16^8=2^{32}$ input sites. Equation (2) forces its relative radius above $2^{-11}$. Every normalized output centre has norm at least one. Consequently the scalar-radius test cannot certify $\|C'-V\|+\eta'\le2^{-11}$ for that pilot, which includes $\beta=2$, even with exact arithmetic and perfect centre selection. A shorter chain, signed correlated remainders, a different gauge acting across bonds, an analytically absorbed reference or a different endpoint requires a separate estimate. A one-bond change of orthonormal basis or more working precision cannot remove this obstruction.

## The endpoint, and exactly where it would be used

Take the explicit sufficient end class $\|A_x-V\|_2\le 2^{-11}$ with vacuum scalars saved and with compatible local tensors on a torus and its cover. This is a convenient sufficient tolerance chosen for sizing. Expand in marked sites $A_x-V$. The weight of a connected occupied set $X$ is at most $(2^{-11})^{|X|}$ by contraction. Separated components factor, with polymers incompatible if they touch or are nearest neighbours. A rooted connected $k$-set in degree eight occurs among at most $8^{2(k-1)}$ depth-first walks. Thus the rooted sum with weight $e^{2|X|}$ is at most
\[
 \frac{2^{-11}e^2}{1-64\,2^{-11}e^2}<1/192<1/100.
\]
This supplies the numerical part of the existing (M1a) for the **whole** normalized tensor network. To see the cover compatibility, use the Kotecký–Preiss bound with size penalty $|X|$ and decay weight $|X|$. Incompatible supports meet one of at most $9|X|$ sites. Their weighted sum is below $|X|$. The sum of connected log terms containing a given site, weighted by the exponential of total polymer size, is at most one (test with a singleton polymer). This application includes absolute values after each signed polymer is formed. [Prior M1 and M1a](gap-means-astra.md) · [Kotecký and Preiss, theorem (1)–(4)](https://www.math.ucla.edu/~biskup/290k.1.24w/PDFs/Kotecky-Preiss.pdf)

On a small coarse torus with $V_s$ sites and shortest side $m\ge 3$, all rooted connected terms of total size $<m/2$ lift uniquely from their local neighbourhood. Their multiplicities on a $q$-sheet cover agree after multiplying by $q$ (assign the rooted sum weight $1/|\operatorname{supp}|$ per root). All local vacuum factors lift too. The remaining absolute contributions on both tori give
\[
 |q\log Z_{\rm small}-\log Z_{\rm cover}|\le 2q V_s e^{-m/2}. \tag{3}
\]
The original masses must be positive; for the Wilson consumer they are. One can take the small network with a periodic pattern of tensor types and repeat that exact pattern on the cover. Mere proximity to two unrelated bulk densities will not give (3).

- **Theorem T, rows 1332/1335.** At one bare $\beta_w$, certifying (3) for a matched time-doubling pair with upper bound $\log(1+q_0/5041)$ would supply **KER only**. T then uses A0, both A1 and A2, and the strict rate fit A3. A2 says *every* bare $\beta\ge\beta_w$ admits $3\le N(\beta)\le C_1e^{c(\beta-\beta_w)}$ at the same margin $5041 S(N;(2N)^3;\beta)\le q_0$. To replace A2, an entrance theorem plus repeated band inclusions must cover this whole family with a size bound. For example, one doubling per inverse-coupling increment $\delta$ gives $c=(\log 2)/\delta$ up to the prefactor for rounding. The required inequality is $4c\kappa<4\log L+\log(1/q_{\rm UV})$. Row 1386's $0.173$ is illustrative and depends on the rates. One successful local step or one bounded interval establishes none of these universal rate claims. As a geometry check, (3) at $m=128$ on $128\times256^3$ is below $2^{-31}$ for the double time cover and would fit $q_0=1/2$.
- **Proposition CH, the intended use.** If an exact entry covers *each* admitted first passage at both physical tori, the chain of inclusions ends in the preceding class, and its geometries satisfy $2L^4 V_s e^{-m/2}<p< (L/2)\log(13/10)$ uniformly for one fixed admissible physical side, (3) supplies END for the $L^4$-sheet cover. CH and FL give SEED-L and then SEED-FP. The positive $p$ incorporates check 1335's repair. This route bypasses the comparison to another cutoff in A1 and the all-bare-coupling A2. The computed object would be one of the intermediate inclusions until BASE, the entire path and END have been supplied.
- **(M-neutral), row 1367.** Take one admissible physical side $L_{\rm phys}$, $n_j=L_{\rm phys}/a_j$, $4\mid n_j$, $n_j\ge2^{70}$ and $\beta_0\le\beta_j\le B_0\log n_j$ at every late cutoff of the trajectory. Put $w_j=\lfloor n_j/1024\rfloor$. For the bare positive transfer matrix, $2F(t)-F(2t)\ge\log(1+S_{\rm all}(t))$ at fixed spatial side. This follows by writing $F(t)=t\log\lambda_0+\log(1+S_{\rm all}(t))$ and using monotonicity. The simple positive vacuum is centre neutral since the centre flips commute with transfer and preserve positivity. Thus $s_0(t)\le S_{\rm all}(t)$. At $t=2w_j$ a periodic pair with defect $\le\log(25/21)$ suffices for $s_0(2w_j)\le4/21$. For instance, aligned endpoint dimensions $m=128$, $b=65{,}536$ give $4mb^3e^{-m/2}=2^{57}e^{-64}<1/128<\log(25/21)$. This example prices the required *coarse* geometry. Reaching it with the late Wilson laws is open. Coverage includes rounding, seams and a fixed physical side for all late cutoffs. An alternative using only the neutral trace must transport the eight electric-twist insertions at zero spatial twist and average them at the end. Projecting each little block separately changes the measure. The reconstructed-sector conclusion retains the continuum hypotheses in checks 1349/1359. [Neutral trace and quantifiers](gap-seed-astra62.md) · [Neutral check](gap-mini-mneutral-check-astra.md)

## Does this carry distinguish the theories?

| Row 1386 §4.5 | Result for the proposed calculation |
|---|---|
| t1 · compact U(1) in 4D | Haar gluing, the HS triangle inequality in (1), and the endpoint estimate all apply to U(1). They produce **zero established non-Abelian advantage**. A signed recoupling estimate would have to exhibit the term giving the gain. For instance, at the line taking a commutator of two different channel projectors its value on a fixed Abelian intertwiner space is identically zero. The lane already examined incompatible pair filters. No bound passing that term through the actual block has been obtained. |
| t2 · SU(2) in 5D | The raw single-triangle derivative becomes $\sqrt{2^{d-3}}=2$, compared with $\sqrt2$ in 4D. Both expand. Different incidence counts change the cost, and do not provide a four-dimensional drift. A proposed stiffness decrement must be tested with the classical $2^{d-4}$ factor over the band and the actual signed quantum correction. Neither is computed by the norm bound. |
| t3 · SU(3) | The Haar projector, oriented representation/dual distinction, face contractions and transfer endpoint make sense for SU(3). Its conjugate fundamentals and multiplicities require new tables. The SU(2) numbers and the quaternion acceptance test have only their stated scope. A dynamical estimate depending on three quaternion directions alone fails this group test. |
| t4 · increasing bare $\beta$ on a fixed lattice | The finite window explicitly terminates. More strongly, for fixed $n$, the normalized plaquette measure concentrates at the identity as $\beta$ increases, whence $b_n\to d_n$ by integrating $\chi_{n/2}$. Every square entry in the minor tends to one. For any fixed $r$ choose enough distinct $n$ to make more than $r$ such entries; at sufficiently large $\beta$ a fixed-rank raw local ball of error $<1/2$ fails. Physical blocking and a proved entrance at finite running coupling would be essential. |
| t5 · equivalence | The local norm and mixed-overlap calculation in (1) can fail on presentations with exactly the same partition functions, as the directed triangle example shows. This is a falsifiable microscopic method and the rank-128 trial fails it. Defining its input class by “all laws with a seed” would throw away this distinction. |

The spin-tensor input represents the Haar-integrated Wilson weight. Bounds on a pinned boundary or on an average plaquette alone cannot certify membership for that law. The selective step would have to occur in the **signed, volume-compatible passage between the actual input and output classes**, including the appropriate scaling with dimension. Checking a few additional models numerically, or observing an Abelian seed at high temperature, gives no such implication. [Filter and the three kinds of input](gap-mech-direction2-fable.md) · [Existing noncommuting-channel test](gap-tree-astra.md)

## What to implement and what the checker must accept

1. **Implement the finite arithmetic and Haar conventions first.** Use rational numbers, or dyadic pairs of integers for interval endpoints. A fast producer may use FLINT/Arb balls to find enclosures. The independent verifier takes the dyadics, the contraction graph with orientations, representation labels, invariant-basis Gram matrices, exact isometry data and the proof of each inequality. Elementary interval operations reduce to integer sign and product checks. Root endpoints require sign checks and squared inequalities. Positive Bessel series use a verified next-term ratio and geometric remainder. Carry centre phases at their plaquettes and all local vacuum scalars on the two covers. Use exact normalization or a certified lower denominator in every division. [FLINT real ball arithmetic](https://flintlib.org/doc/arb/index.html)
2. **Generate the recoupled values and bounded-memory contractions.** Keep the sparse vertex incidence and signed magnetic contractions. For the half-spin build, noncrossing singlet pairings give bases of sizes $1,1,2,5$. Their Gram and inverse Gram implement the Haar projector $T(T^*T)^{-1}T^*$ even in a nonorthogonal basis; check nonsingularity, dimensions and the invariant span. Closing paired fundamental lines evaluates a signed product of loop dimensions. Cross-check small cells by an independent Haar integral. For higher spin, use symmetrized fundamental powers or Clebsch–Gordan recursions, checking orientation, multiplicity and normalization. Yosprakob already eliminates magnetic indices around a site in general dimension. Yosprakob and Okunishi use this in 3D with a finite representation list and HOSVD/anisotropic truncation. Their signed tables/ordering are implementation precedents; their numerical truncation error does not provide (1). [Yosprakob, §§3–4](https://arxiv.org/html/2311.02541v2) · [Yosprakob and Okunishi, §§2–3](https://arxiv.org/html/2406.16763v2)
3. **Replace the failed scalar propagation.** One implementable master-map layout has three orthogonal spaces per leg: vacuum, retained nonvacuum and complement. There are $3^8=6{,}561$ error sectors including the vacuum. Separate the centre from these error sectors. During one directional merge only matching sectors on the shared bond contract, leaving $3^{15}=14{,}348{,}907$ compatible sector pairs. A bundled transverse leg with a high input stays high when $W$ is supported on the product of the retained spaces. Two vacuum inputs stay vacuum. The remaining low products split into at most two output sectors on each transverse leg. Each bilinear error sum therefore has at most $2^6 3^{15}=918{,}330{,}048$ scalar routing terms per merge before exploiting symmetry. Stream them into 6,561 accumulators. For a first inexpensive enclosure, bound each projected signed centre residual by the one full residual $t$ from (1); apply separate sector estimates to the two mixed terms and the tail–tail term. Normalization uses the *vacuum sector's* lower bound. This design permits zero when a lone high strand cannot match and reach the output. It does not prove a small enough radius. If sharper signed residuals require projecting individual sectors, price those contractions separately. Even the simple version with three bilinear sums, at most ten elementary arithmetic operations per routed bound and the factored core is about $5\cdot10^{10}$ scalar operations per merge, or about $2.56\cdot10^{13}$ for the 512 bulk checks. This estimate assumes scalar majorants and precomputed sector norms for the centres. Those input norms can be bounded together by projecting each product factor onto the three leg spaces and summing the pairwise Gram products (about $8\cdot 3^8H^2$ scalar multiplications of precomputed overlaps per centre). A signed rearrangement acting across bonds is a separate mathematical construction: it must preserve every required closed contraction and account for the triangle that survives raw regrouping. Ebel's 3D rearrangement theorem treats tensors near the high-temperature point and illustrates this distinction. [Ebel, §§3–4](https://arxiv.org/html/2401.04229v2)
4. **Verify the actual statement by replay.** An inclusion certificate contains the parameter subdivision, exact centres and face embeddings, proof-producing arithmetic DAGs for signed residuals and positive normalizers, analytic tail lemmas with their parameters, a coverage graph with all bulk and seam types, and the paired endpoint inequalities. Stream subproofs and reuse proved DAG nodes. Trust the Lean kernel checking the proof terms and the explicitly listed foundational axioms of the imported analysis (inspect with `#print axioms`). The planned arithmetic check uses kernel reduction or kernel-checked proofs of integer products, with no `native_decide`, compiled evaluator axiom, external interval oracle or assumed computed lemma. A hash identifies a replay input and confers no mathematical validity. The verifier must also prove the Haar, analytic and mass-preservation lemmas connecting its integers to the asserted real quantities. No Lean executable was available on the runner's PATH. No kernel certificate or run of the full 4D tool is claimed in this row.

**First buildable component, known answer.** Glue the four plaquettes of a 2D open square by central SU(2) convolution. Take $f=1+\chi_{1/2}/4+\chi_1/16$, a strictly positive unit-mean weight. Schur orthogonality gives coefficients $1,1/2048,1/1769472$ in $f^{*4}$, with all other characters zero. An independent integration uses a Haar unit quaternion $q$, $x=q_0$, $y=q\cdot v$, $u=v_0$. The second and fourth sphere moments give $\mathbb E(xy)=u/4$, $\mathbb E(x^2)=\mathbb E(y^2)=1/4$ and $\mathbb E(x^2y^2)=(1+2u^2)/24$. These are the rank-two and rank-four cases of the sphere moment identities used in row 1341. With $\chi_{1/2}=2u$ and $\chi_1=4u^2-1$, the two paths must agree as polynomials, including the vacuum. The following reusable reference fixture uses only exact rational arithmetic.

```python
from fractions import Fraction as Q

def haar_glue(left, right):
    a, b, c = left
    d, e, f = right
    return (a*d + (a*f + c*d)/4 + c*f/24, b*e/4, c*f/12)

def to_polynomial(coeffs):
    vacuum, fundamental, adjoint = coeffs
    return (vacuum - adjoint, 2*fundamental, 4*adjoint)

def schur_glue(left, right):
    return tuple(x*y/d for d, (x, y) in enumerate(zip(left, right), 1))

seed = (Q(1), Q(1, 4), Q(1, 16))
two = schur_glue(seed, seed)
four = schur_glue(two, two)
p = to_polynomial(seed)
pair = haar_glue(p, p)
target = (Q(1), Q(1, 2048), Q(1, 1769472))
assert four == target
assert haar_glue(pair, pair) == to_polynomial(target)
assert haar_glue(haar_glue(pair, p), p) == to_polynomial(target)
assert haar_glue(pair, pair) != to_polynomial((Q(1), Q(1, 256), target[2]))
assert haar_glue(pair, pair) != to_polynomial((Q(1), target[1], Q(0)))
```

The Python fixture passed all five assertions, including the two intentionally wrong outputs. It takes fewer than 200 rational arithmetic operations and 1 MB of numeric payload. Replaying these identities in Lean is one small job. The Haar moment and Schur identities are separate proof obligations. Rejecting a certificate with a missing $1/d$, a dropped spin-one channel, or a zero denominator is part of acceptance. For a further independent inventory check on the 4D generator, replace $x^k$ at each vertex of $\prod_{ij\in E(K_{2,2,2,2})}(1+x_i x_j)$ by its SU(2) character moment. Through degree six the signed integer quadrature on $-3,-2,-1,0,1,2,3$ with weights $(-1,36,225,200,225,36,-1)/720$ has moments $1,0,1,0,2,0,5$. Contracting this finite polynomial gave 12,910,079 again. This is a different arithmetic check of the inventory, not of the physics or the Lean implementation.

For the kernel bring-up, the following standalone Lean 4 fixture is specified for the same polynomial path. Its four naturals represent $(a+bx+cx^2)/d$ on this positive-coefficient example. The factor 24 clears all sphere-moment denominators. It can be saved as `GlueFixture.lean` and passed directly to `lean`. It has not been executed here.

```lean
import Init

structure MomentPoly where
  a : Nat
  b : Nat
  c : Nat
  d : Nat

def sew (p q : MomentPoly) : MomentPoly :=
  ⟨24*p.a*q.a + 6*(p.a*q.c + p.c*q.a) + p.c*q.c,
   6*p.b*q.b, 2*p.c*q.c, 24*p.d*q.d⟩

def equivalent (p q : MomentPoly) : Bool :=
  (p.d != 0) && (q.d != 0) && (p.a*q.d == q.a*p.d) &&
  (p.b*q.d == q.b*p.d) && (p.c*q.d == q.c*p.d)

def plaquette : MomentPoly := ⟨15, 8, 4, 16⟩
def pairOfPlaquettes := sew plaquette plaquette
def square := sew pairOfPlaquettes pairOfPlaquettes
def known : MomentPoly := ⟨1769471, 1728, 4, 1769472⟩

example : equivalent square known = true := by decide
example : equivalent (sew (sew pairOfPlaquettes plaquette) plaquette) known = true := by decide
example : equivalent square { known with b := 6912 } = false := by decide
example : equivalent square { known with d := 0 } = false := by decide
```

## Next two rows

1. **Build and kernel-check the Haar gluing component.** Accept when Lean replays both associations of the 2D square with the stated Haar/Schur semantics, rejects the corrupted factor and denominator, and verifies the $N=1$ four-dimensional link inventory and one signed closed fundamental cube. With plaquette coefficient $b$ its contribution must be $b^6/16$ by the existing unbranched surface formula. Use the rational fixture $b=1/16$, for which it is $2^{-28}$. Emit the checker source, certificate, `#print axioms` and peak memory. An incorrect normalization or twist sign must fail a corresponding fixture (a local centre source on one face reverses its sign, a closed twist pairs trivially with a cube boundary, and a wrapping sheet with odd twist pairing reverses sign). This builds a reusable verified component and settles no intermediate-coupling inequality.
2. **Proof-design row for one signed 4D inclusion.** Freeze a basis/rearrangement that acts across the obstructing cut and preserves the exact closed network, and freeze its input/output centres before evaluating the first compact interval $[2,2+1/256]$. Carry the resolved one- and two-triangle sectors, signed overlaps and the remaining high-spin norms through all four pair directions. A concrete acceptance test is to exhibit a positive rational sector vector $v$ on the allowed nonvacuum directions, a positive lower vacuum denominator and an outward majorant $M_I$ with $M_I(0)\le v/16$ and $M_I(v)-M_I(0)\le15v/16$ componentwise. Use separate input/output charts in their stated scaled coordinates. Also demonstrate entry for every bare input in $I$ without discarding its tail. A pass gives **one** local inclusion with measured cost. To count it toward the carry, identify the signed gain that disappears in U(1) and test its scaling in 5D. A certified expanding channel or lower residual exceeding the allowed sector budget rejects that specified design. An interval straddling the threshold leaves it open. Full first-passage entry, the remaining band, cover geometry and the seed continue to require their own proofs.
