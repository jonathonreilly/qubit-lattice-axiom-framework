# Repo search

Row 1430, lane `5e0307e183eb`. The Markdown and TeX searches covered `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`), `pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and `pr/10141` (`c73ad7b177d9`). The statement query for two-strand/traceless ring, relative-orientation moment, crossed adjoint bridges/matchings, double trace near two-square/decrement, `Y_alt` and the row name returned no hits. Method queries included Oeckl/Pfeiffer, spin foam, one-loop convolution, traceless Pauli, quadrupole with plaquette/holonomy and outward adjoint faces/bridges. The capped broad Pauli and Fierz/double-trace searches also returned unrelated controller and electroweak notes, including `SINGLE_PORT_PROGRAM_AND_AUTONOMOUS_CONTROLLER_BOUNDED_THEOREM_NOTE_2026-10-15.md` and `archive/publication/ci3_z3/DERIVATION_ATLAS.md`.

| Source | Exact statement and scope |
|---|---|
| Main, `research/mass-gap/library/prior/gap-math-lit.md` 96 and `gap-seed-lit.md` 51, 92, 112, located also through `research/mass-gap/ROWS.md` 29, 42 | Pfeiffer and Oeckl give a character expansion on plaquettes with Haar intertwiners on links. The contracted weights can have either sign. This supplies the representation. |
| PRs 10114 and 10133, `MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149 | The convolution on the edges of one simple loop has eigenvalue $\rho=(I_2/I_1)^{\lvert C\rvert}$ on its fundamental trace. For its centered trace $F$ the operator dominates $(1+1/(4\rho))^{-1}\lvert F\rangle\langle F\rvert$ in SU(2). This is a lower form bound for a single loop. [November 8 digest, §11](prior/repo-search-2026-11-08.md) |
| Lane, rows 1418 and 1421 | Each face of label $n=2j$ carries $b_n^{1/4}$ per corner. For fixed exterior labels the all-direction block coefficient divided by its vacuum is its exterior weight times the joint internal Wilson expectation. Row 1421 fixes each exposed triangle at its bare weight. Its internal channel operators share spectral blocks on graphs with at most one cycle per component. [1418](gap-rg-step-sizing-astra62.md) · [1421](gap-rg-signed-inclusion-astra62.md) |
| Lane, rows 1424 and 1425 | Row 1424 (4), (6) cancels a single closing fundamental by inversion, and (7) isolates the two-square quadrupole. It also points out that squaring the single-exchange integrand needs extra strands. Row 1425 encloses the quadrupole, its vacuum and a five-dimensional conditional ratio, and reports an **increase** in its alternating single-trace ring magnitude. Its finite sums are the numerical inputs for the present search. [1424](gap-rg-two-cycle-astra62.md) · [1425](gap-rg-ring-sign-astra62.md) |

The target-specific prior is absent. FINISH 1430 names the three earlier tests and has no additional “Repo prior work” entry. The pinned checkout search found the ring and squared-integrand suggestion in those rows. Searches of the open registry, open-core list, L17c, outline chunks, obligations and CA index located no assignment of the adjoint matchings. Row 1429 owns the check of **row 1425**. The exterior adjoint matchings were unresolved at this pin.

In `YM4_sketch_500.tex` (SA) and `theorem_0_complete_account_raw_I.tex` (CA-I), supplied at `31a47c543775`, Sussman and Alpoge, writing with Claude and Codex, define the Wilson law (SA 238–278), prove GL3–GL4 for the positive Bessel coefficients (2195–2243), give the quaternion half-trace (2773–2781) and prove the classical four-dimensional curvature count (8519–8549). C4 asks for “one nonempty class” of complete presentations preserved at every step (4075–4084). CA-I 4209–4239, `4.3:thm-uv-stability`, cites Bałaban's theorem assuming all effective couplings stay below its small ceiling. This row concerns bare finite-block coefficients on an intermediate band. [Index, chunks 01–04 and 08](sa-index/README.md) · [C4 obligations](sa-index/obligations.md) · [Bałaban quotation record](lit-balaban.md)

## Result

Two crossed matchings of spin-one outward faces give one symmetry-related response. Each magnitude is smaller than its fixed reference by **134.848622 to 151.009135 parts per billion** throughout the four-dimensional band. At fixed U(1) charges both vanish pointwise. In five dimensions the classical factor times the magnitude ratio is at least **1.82783288**. Four of the other seven coefficients vanish by inversion and three equal their references. These are bare block coefficients. The numerical inequalities await Lean-kernel replay.

## Plan saved at creation

1. Read the prior search, goal, operating rules, requested FINISH rows, registry and outline index. Search the five named repository refs for both the statement and the method. Record the exact scope of each relevant hit.
2. Select a finite class outside previously resolved cases. Before evaluation, record every routing, the reference, phase, band, fixed-charge condition and five-dimensional acceptance test.
3. Apply exact symmetries, then compute the necessary Taylor coefficients with rational arithmetic. A coefficient at the origin alone does not settle the sign on the requested band.
4. Enclose surviving signs throughout the closed band with explicit tails and check the five-dimensional comparison. Record every member's disposition, trusted base, replay obligations and the next two rows with their decisive outcomes.

This is a research note. No scientific or audit status is conferred.

## Frozen class and acceptance rule

The following choices were saved before evaluating these matchings. Row 1425's sign for its own ring was already known.

Use the two positive plaquette circuits $P=(0,e_1,e_1+e_2,e_2,0)$ and $Q=(0,e_3,e_3+e_4,e_4,0)$ in the open block $B_d=\{0,1\}^d$, with distinct exterior bonds and $\beta\in I=[2,513/256]$. Keep the four mixed fundamental strips of row 1424. Label their root ports $1,2,3,4$. Ports 1 and 2 follow $P$ at respective outward displacements $-e_3,-e_4$. Ports 3 and 4 follow $Q$ at displacements $-e_1,-e_2$. A strip occupies the mixed face between each original edge and its displaced copy. All three nonroot outward bonds per strip use the oriented bivalent invariant $I/\sqrt2$.

Take **all nonempty matchings** of the four root ports. A matched pair $ij$ occupies the unique outward/outward square between those two bonds with physical spin **one** ($n=2$). Join its spin-one index to the traceless part of the oriented fundamental endomorphism at each endpoint. At an unmatched port close the strip with $I/\sqrt2$. Every other exterior slot is vacuum. There are exactly two fundamental strands on each mixed edge of each square. These are six one-edge matchings $12,13,14,23,24,34$ and three perfect matchings $12\mid34,13\mid24,14\mid23$. In five dimensions embed both marked squares in the four-dimensional face at $x_5=0$ and the full five-dimensional internal weight.

Fix $q(G)=\operatorname{tr}(G)/2$ and $G=q(G)I+i\sum_a h_a(G)\sigma_a$ with the Hermitian Pauli matrices in order $x,y,z$. At a matched port use the unit covector with components $G\mapsto\operatorname{tr}(\sigma_aG)/(i\sqrt6)$, and join its vector indices by $\delta_{ab}$ in the real adjoint basis. At an unmatched port the covector is $G\mapsto\operatorname{tr}(G)/\sqrt2$. These formulas fix all phases and orientations. Write $X_{m,d}$ for the resulting coefficient of the vacuum-normalized block.

Let $R_{m,d}$ evaluate exactly that coefficient after independent Haar conjugations of the two rooted holonomies, **one conjugation per square, shared by its two copies**. Keep their joint angle law, every exterior weight and the same internal vacuum. Put $g_{m,d}=|X_{m,d}|/|R_{m,d}|$ when the reference is nonzero. For every member require a nonzero reference throughout the band, a uniform $g_{m,4}\le1-\epsilon_4$ with $\epsilon_4>0$, exact zero of the traceless coefficient on each fixed U(1) charge assignment and a uniform $2g_{m,5}\ge1+\epsilon_5$ with $\epsilon_5>0$. A zero reference cannot pass the strict magnitude test. The factor two compares with the classical $2^{d-4}$ for a length doubling. For the Taylor screen, remove the common exterior factor before expanding the signed difference. Expand the ratio as well when the reduced reference has a nonzero limit. Only a band enclosure can decide the band sign.

## Symmetry reduction

Write $H,K$ for the rooted transports, $u=q(H)$, $v=q(K)$, and $h,k$ for their three real vector components. With product probability Haar on the internal links put

$$
 A(\beta)=\int e^{\beta q(g)}dg,\qquad
 w_d=\prod_{p\subset B_d}\frac{e^{\beta q(U_p)}}{A(\beta)},\qquad
 z_d=\int w_d\,dU,\qquad E_d F=z_d^{-1}\int Fw_d\,dU.
$$

The weights on all 24 or 80 internal faces are present, including both marked faces. Positivity and full support give $z_d>0$. Write $b_n=(n+1)I_{n+1}(\beta)/I_1(\beta)$ and $s=|m|$. The exterior factor for the fixed label is

$$
 a_s=2^{-6} b_1^8 b_2^{s/4}(2/3)^s(\sqrt2)^{4-2s}>0
 \quad (\beta\in I).
$$

Indeed the sixteen mixed faces each contribute $b_1^{1/2}$ and the twelve nonroot bivalent tensors give $2^{-6}$. At a root port the Pauli matrices transform under conjugation by a real orthogonal adjoint matrix. Their total squared Hilbert–Schmidt norm is six. Thus the prescribed three-slot tensor is a unit invariant. It sends a strip to $\sqrt{2/3}\,h_a$ or $\sqrt{2/3}\,k_a$. An unmatched closure yields $\sqrt2\,u$ or $\sqrt2\,v$. Each adjoint corner supplies $b_2^{1/4}$ and one ordinary index identification. This derives one boundary coefficient with all spins in the interior summed. A direct identity for checking the wiring at two ports is

$$
 \sum_a\frac{\operatorname{tr}(\sigma_aG)\operatorname{tr}(\sigma_aJ)}{(i\sqrt6)^2}
 =\frac{\operatorname{tr}G\operatorname{tr}J-2\operatorname{tr}(GJ)}6 .
$$

It follows by contracting the Pauli completeness identity $\sum_a(\sigma_a)_{ij}(\sigma_a)_{kl}=2\delta_{il}\delta_{jk}-\delta_{ij}\delta_{kl}$.

Let $W=|h|^2|k|^2$ and $T=(h\cdot k)^2-W/3$. The following table is exhaustive because each of the four ports has degree at most one. Both integrand columns have the prefactor $a_s$ and use the same joint Wilson expectation. The two paired contractions in a perfect matching see the same $H,K$ before integration.

| Matching | Actual integrand | After the reference rotation | Symmetry decision |
|---|---|---|---|
| $12$ | $\lVert h\rVert^2 v^2$ | same | Magnitude equals reference |
| $34$ | $u^2\lVert k\rVert^2$ | same | Magnitude equals reference |
| $13,14,23,24$ | $uv(h\cdot k)$ | $0$ | Each coefficient vanishes |
| $12\mid34$ | $W$ | $W$ | Magnitude equals reference |
| $13\mid24,\ 14\mid23$ | $(h\cdot k)^2$ | $W/3$ | Two distinct exterior labels with the same remaining test |

In the four one-edge mixed matchings the swap of axes 1 and 2 reverses $H$ and fixes $K$. It preserves the internal Wilson law, $u,v$ and $z_d$, and negates $h$. The swap of axes 3 and 4 gives a second inversion. This is row 1424's symmetry applied after the strip contraction. Within-square dot products and angles are invariant even before integration. For a perfect mixed matching, Haar conjugation of $K$ at fixed $k$ averages $kk^{t}$ to $|k|^2 I_3/3$. This gives the reference as the actual grouped coefficient $X_{12\mid34,d}/3$. The integrands for each nonzero reference and for each crossed coefficient are nonnegative and strictly positive on a nonempty open set of link fields. Full support gives positive integrals. In either dimension its ratio is therefore exactly

$$
 g_d=\frac{3E_d(h\cdot k)^2}{E_dW}=1+\frac{3E_dT}{E_dW},\qquad
 X_{m,d}-R_{m,d}=a_2 E_dT,\qquad a_2=\frac{b_1^8\sqrt{b_2}}{144}.       \tag{1}
$$

Both matchings are single coefficients on **two spin-one outward faces**. The alternating ring of row 1425 used **four fundamental outward faces** and had a negative reference. Equation (1) reuses its dynamical moment with a positive reference determined by these new boundary labels. Swapping axes 1 and 2 exchanges the two $Q$ strips and reverses the two $P$ transports. Their two vector signs cancel. The boundary labels therefore supply one scalar test. For the phase of row 1425 on this band, its alternating magnitude ratio and (1) obey $g_{\rm alt}+2g_d=3$.

At fixed compact U(1) charges the bivalent closures around the three nonroot vertices force the same oriented charge around each strip. At its root the conjugation representation is $\mathrm{End}(V_n)$ with $\dim V_n=1$. The projection $L\mapsto L-\operatorname{tr}(L)I/\dim V_n$ is identically zero, also for $n=0$ or negative $n$. Each nonempty matching couples through that subspace, so actual and reference coefficients vanish pointwise for every compatible assignment. An incompatible charge gives the zero coefficient by Haar projection. No abelian ratio is taken.

## Leading Taylor screen in four dimensions

The seven rejected matchings have zero actual-minus-reference expectation at every order. For the two remaining labels the reduced difference is $E_4T$. Row 1425's eleven leading supports give its first coefficient at degree 16. Their four contributions with multiplicities are

$$
 c=4\frac{-5}{195689447424}+4\frac5{1320903770112}
       +2\frac5{86973087744}+\frac5{77309411328}
   =\frac{15655}{169075682574336}.
$$

Every lower coefficient vanishes in that enumeration. The vacuum has constant term one. At zero coupling the two square transports use disjoint links and are independent Haar. Each has mean squared vector length $3/4$, so $E_4W=9/16$ there. The center transformation that negates every face makes both observables even in $\beta$. Consequently

$$
 g_4-1=\frac{16c}{3}\,\beta^{16}+O(\beta^{18})
      =\frac{15655}{31701690482688}\,\beta^{16}+O(\beta^{18}).
$$

This leading rational coefficient predicts an increase near zero. Its sign leaves the band at $\beta\ge2$ undecided. Both labels go to the full enclosure. The coefficient and support enumeration have the computational standing of row 1425.

For the band calculation write $N=z_4E_4T$ and $D=z_4E_4W$. Row 1425 computed $N$ and a lower bound on $E_4W$. Two scalar insertions in the same torus contraction enclose the previously untabulated $D$ and determine the reference in (1).

## Computing the reference with the same internal vacuum

Set $d_n=n+1$, $\lambda_n=I_{n+1}(\beta)/I_1(\beta)$, and $F_z(g)=\sum_{n\ge0}d_n\lambda_n z^n\chi_n(g)$, where $\chi_n$ has spin $n/2$. In this section $z$ marks the **original Wilson spins**. Define $D(z)$ by inserting $W$ in the product of the 24 functions $F_z$ and integrating all internal links. Then $D(1)=D$. Both scalar marks use the exact identity $1-q(G)^2=(3-\chi_2(G))/4$.

Use row 1425's $C_4\times C_4$ torus with its sixteen mixed faces and eight circuit weights. At each of the two marked circuits a final spin label $n$ in the ordinary signed contraction now has eigenvalue

$$
 \frac1{4d_n}\left(3d_n\lambda_n z^n-
          \sum_{\ell=|n-2|,\ |n-2|+2,\ldots,n+2}
                            d_\ell\lambda_\ell z^\ell\right).            \tag{2}
$$

Character multiplication by $\chi_2$ gives each summand once. The other 22 faces keep their original labels. To collect powers through $z^{28}$ one need only enumerate ordinary geometries through total label 32, since each of the two final labels differs from its Wilson label by at most two. For each geometry expand the two instances of (2) and keep precisely the original-label terms of degree at most 28. Leave the resulting signed rational sums grouped by original-spin histogram. The circle symmetries that fix the root and interchange both marks preserve these even scalar insertions and their product. This uses the ordinary vertex overlap of row 1425 throughout, with no tensor insertion at a vertex.

The vacuum circle bound times $3/2$ controls every omitted spin. On $|z|=t$ write $M=\sup_\ell \lambda_\ell t^\ell$. Since $\sum_{\ell\in n\otimes 2}d_\ell=3d_n$, (2) has modulus at most $3M/2$. In the fourth-direction gauge slice one of the two marked faces is a crossing convolution and the other is in the lower three-cube. The crossing convolution therefore has norm at most $3M/2$, with each of the eleven ordinary crossing convolutions bounded by $M$. Multiplication of the lower-slice wavefunction by $1-q(H)^2\in[0,1]$ can only lower its $L^2$ norm. Thus the same slice-norm and sphere-gluing bounds that give $M^{12}P E_5$ for the ordinary vacuum give $3M^{12}P E_5/2$ for $D(z)$. Here $P$ is the squared one-face norm majorant and $E_5$ the fivefold face-convolution majorant in row 1425, “Bounding every omitted spin”. The factorial character majorant gives analyticity on every finite circle. Multiplying links in direction $i$ at $x$ by $(-1)^{\sum_{j<i}x_j}$ negates all face holonomies and leaves $W$ invariant. Hence the odd powers vanish. Applying Cauchy's inequality and summing the even powers gives, with row 1425's uniform vacuum circle bound,

$$
 |D(1)-D_{\le28}(1)|\le
 \frac{3}{2}\,15466258\,
     \frac{(4/9)^{30}}{1-(4/9)^2}.
                                                                    \tag{3}
$$

This bounds the infinite remainder in the newly computed reference as well as its mixed-face and circuit-spin tails.

## Band enclosure and disposition

The following outward enclosures include both endpoints of $I$. Each computed band inequality is a **gap (computation specified, not yet formally checked)**.

For the signed moment use row 1425's two-quadrupole histogram through original Wilson degree 46 and its circle bound $216821257148$ at $t=11/4$. The tail starts at degree 48. For the vacuum use its ordinary histogram through degree 28 and its circle bound $15466258$ at $t=9/4$. For $D$ use (2) and (3). The tails of $N,D,z_4$, in that order, have absolute upper bounds $(204047,786271671008,524181114006)/10^{15}$. The first and third use the same even Cauchy remainder as (3) with their own circle constants and first omitted degrees.

On each of 512 equal closed cells of $I$, the evaluator bounds $\lambda_n=L_n/L_0$ using the positive Bessel series $L_n=\sum_{j\ge0}(\beta/2)^{n+2j}/(j!(n+j+1)!)$. It keeps terms through $j=32$ and bounds the tail by twice the first omitted term, checking the ratio bound $1/2$. It multiplies each signed rational histogram coefficient by its interval monomial, sums the signed terms and applies $16/\beta^4$ to the quadrupole polynomial. It adds each infinite tail **before** dividing. The remaining operations use outward integer endpoints at scale $2^{112}$. The square root in $a_2$ is bounded by integer square roots rounded down and up. Hulls below are taken only after the three quantities and each displayed ratio or difference are evaluated on common cells.

| Four-dimensional quantity for either crossed matching | Lower numerator | Upper numerator | Common denominator |
|---|---:|---:|---:|
| $N_{\le46}$ | $-25569294$ | $-23271660$ | $10^{15}$ |
| $D_{\le28}$ | $512391305272895$ | $512820046932150$ | $10^{15}$ |
| $N=z_4E_4T$ | $-25773340$ | $-23067614$ | $10^{15}$ |
| $D=z_4E_4W$ | $511605033601887$ | $513606318603158$ | $10^{15}$ |
| $z_4$ | $1256288427845381$ | $1259982656688565$ | $10^{15}$ |
| $E_4W$ | $406372366155038$ | $408496245477337$ | $10^{15}$ |
| $X_{m,4}$ | $189167473600$ | $192220542589$ | $10^{15}$ |
| $R_{m,4}$ | $189167500186$ | $192220570503$ | $10^{15}$ |
| $X_{m,4}-R_{m,4}=a_2N/z_4$ | $-28938$ | $-25587$ | $10^{15}$ |
| $1-g_4=-3N/D$ | $134848622$ | $151009135$ | $10^{15}$ |

The separate value ranges of $X$ and $R$ overlap. The direct difference on a common cell proves the direction, conditional on replay of the finite arithmetic. There is also a shorter way to decide the sign if the new radial table is unavailable. From row 1425, $-E_4T\in[1829,2054]/10^{11}$ and $(5047/10000)^2\le E_4W\le1$. Applied directly to (1) these give $54/10^9\le1-g_4\le242/10^9$. This uses the same dynamical moment. The new scalar sum measures its denominator more precisely.

**Five dimensions.** Row 1425 integrates two free links on each marked square conditional on the other links. Given those links the pairs are independent. With $w_H=E(|h|^2\mid\mathrm{rest})$, the conditional trace-free tensor has the form $a_H(nn^t-I/3)$ with $0\le a_H\le\eta w_H$. The same bound holds for $K$. Row 1425 gives $\eta=2934/10000$ in $d=5$. Thus $-\eta^2/3\le E_5T/E_5W\le 2\eta^2/3$. This keeps the joint outer Wilson weight on all 80 plaquettes. The conditional bound retains spins $n\le20$, uses $R=3(513/256)$ for the staple radii and bounds each discarded normalized kernel integral times $\beta^2$ by $4(513/256)^2(R/2)^{42}/(21!)^2$. The $2048\times4$ closed boxes and the minimum principle in the two staple vectors extend the bounds to the whole parameter set. In particular,

$$
 \boxed{\frac{182783288}{10^8}=2-2\eta^2\ \le\ 2g_5\ \le\ 2+4\eta^2=\frac{234433424}{10^8}.}
$$

The classical inverse-coupling factor is $2^{d-4}$ because one block contains $2^d$ cells while squaring the coarse constant flux contributes $2^4$. For the crossed coefficients the corrected five-dimensional factor stays above one. The enclosure leaves the sign of $g_5-1$ open. For the three rotation-invariant labels $g_4=g_5=1$ and the classical factors are 1 and 2. For each of the four odd labels both reference and coefficient vanish in both dimensions.

## Witnesses and checks

The scratch directory is `/tmp/ym4d-row1430.mIMDw1ZR/`. The signed and vacuum histograms came from row 1425's `/tmp/ym4d-row1425.a4IgI8Ax/`. Its source and inputs were copied before reuse. Row 1429's cross-provider check was still pending at the requested pin. This row did not regenerate the two old histograms. The table evaluation, scalar histogram and exterior wiring checks are new.

| Scratch file and invocation | Witness or control |
|---|---|
| `radial.py 28`, `radial28.txt`, `radial28.log` | Equation (2) through degree 28. The geometry cap 32 admitted 118,792 labelled assignments with orbit multiplicity. Of these, 57,293 had nonzero geometry and could contribute within the cutoff. Their signed sum has 384 nonzero histograms. |
| `matching_bounds.py 512`, `matching512.log` | Recomputed the degree-16 coefficient from `groups42.txt`, both needed circle constants and the joint cell bounds from those 384 histograms, 1,884 nonzero signed histograms and 96 nonzero vacuum histograms. This is 1,210,368 signed histogram contributions over the 512 cells. |
| `matching_geometry.py`, `geometry.log` | Constructs the mixed and outward squares from their vertices in both dimensions. For all nine labels it checks the Pauli contraction against the fundamental trace identity, the parity of each matching under inversion of $H$, and the reference on rational unit quaternions by the 24 proper signed permutations. For the crossed labels, parallel and perpendicular unit imaginary holonomies give reduced coefficients 1 and 0 with the same reference $1/3$. |
| `controls.py`, `controls.log` | A direct cube calculation gives $[\lambda_1^6]D=15$, as does the scalar histogram. Re-evaluating the five-dimensional conditional boxes gives the upper bound $2934/10000$ used above. |
| `recouple.py`, `conditional_ring.py`, `circle_tail.py`, `groups42.txt`, `vacuum28.txt` | Copied row-1425 contraction, Bessel and tail inputs. `SHA256SUMS` records the input, output and producer digests. |

For the cube control, a central sign on one link forces the six fundamental plaquettes to have even incidence at every edge. Direct enumeration of the six-face subsets of the four-cube gives eight closed sets, its elementary cube boundaries. Four contain neither marked face and four contain one. The unmarked cube weight is $b_1^6/16=4\lambda_1^6$. A mark off the cube has a free link and gives its Haar mean $3/4$ independently. On a marked cube face the other five faces glue to its fundamental character, so the face is weighted by $\chi_1^2$, of Haar mass one. Its radial factor is $4(E_{\rm Haar}q^2-E_{\rm Haar}q^4)=4(1/4-1/8)=1/2$. Thus the coefficient is $4[4(3/4)^2+4(3/4)(1/2)]=15$. This check uses face incidence and Haar moments independently of the Racah contraction. The 24 rotations in the fixed-field check integrate the first two angular moments exactly by signed-permutation invariance and trace.

In that scratch directory, the invocation for each new script is `python3 -I -B run_local.py SCRIPT [ARG]`. The single numeric job held the lab lease with a 1,500 MiB RSS guard. The largest recorded peak among the new producers was 50,839,552 bytes for the scalar histogram. The runner kept its assigned priority when the requested nice adjustment was unavailable. All signs and interval endpoints claimed here use exact arithmetic. This is author-only work. No Lean replay or independent check of the complete four-dimensional enclosure was performed here.

## Exact Lean replay obligation

For $d\in\{4,5\}$ use product probability Haar on the positive links of $B_d$, inverse matrices on reverse links and the full Wilson density $w_d/z_d$ above. Form $X_{m,d},R_{m,d}$ using the nine fixed exterior labels and independent conjugations specified above, with the same conjugation for both copies of each square. For **every real** $2\le\beta\le513/256$ and **each** $m\in\{13\mid24,14\mid23\}$, the required conclusion, in a form that avoids division, is

$$
\begin{aligned}
 &z_4,z_5,R_{m,4},R_{m,5}>0,\qquad 0<X_{m,4}<R_{m,4},\\
 &134848622\,R_{m,4}\ \le\ 10^{15}(R_{m,4}-X_{m,4})
                      \ \le\ 151009135\,R_{m,4},\\
 &182783288\,R_{m,5}\ \le\ 2\cdot10^8 X_{m,5}
                      \ \le\ 234433424\,R_{m,5}.
\end{aligned}                                                        \tag{4}
$$

Check the raw four-dimensional intervals in the table, the exact identities for all other matchings in both dimensions, the leading rational coefficient, and $X_{m,d}=R_{m,d}=0$ for every nonempty matching on every fixed U(1) charge assignment. For the crossed labels (4) gives admissible uniform margins $\epsilon_4=134848622/10^{15}$ and $\epsilon_5=82783288/10^8$.

Replay must connect the integers to the integrals. It must verify the strip contractions, conjugation average, root symmetries, character and Haar normalizations, and row 1425's signed spin enumeration, recoupling phases and marked operator. For the scalar insertions it must prove (2) and (3), verify the orbit multiplicities and show that the degree-32 enumeration covers every term of original degree at most 28. Check the Fourier slice and sphere identities and the Cauchy, Bessel and five-dimensional conditional bounds with their infinite remainders. Finally check coverage of the closed cells, outward arithmetic, vacuum positivity and all multiplications or divisions leading to (4). The degree-six cube value and perpendicular-unit fixture distinguish a missing scalar mark and an erroneous pairing. Reversing the quadrupole sign should fail the strict four-dimensional inequality.

The intended trusted base is the Lean kernel checking proof terms, with the foundational axioms actually used for real analysis, compact-group Haar measure and representation theory listed by `#print axioms`. The Python scripts and their tables supply witnesses. The checker must verify their integer relations and coverage without trusting the scripts, a compiled evaluator, `native_decide` or an assumed numerical bound. A kernel receipt for the two-dimensional fixture exists on the Mac mini. The finite-block computation specified here is open pending its own receipt. [Row 1427 receipt](../lean/glue/RECEIPT.md)

## Next two rows

1. **Replay the crossed matching in Lean on the Mac mini.** Reuse the signed-moment work of rows 1425/1429. First recover the sign with the coarser bound from (1), then check the scalar reference and both margins in (4), with the Haar semantics, tails, independent fixtures and axiom list. A kernel-checked strict inequality throughout $I$ accepts this one response. A failed sign, normalization or tail bound reopens it. A corrected wider interval still passes the qualitative test if it separates the required thresholds.
2. **Test one four-direction inclusion using this coefficient.** Freeze a contraction-preserving change across the cut, an input chart, an output chart and their centres. In the actual sector containing this label, show exactly how its $a_2E_4T$ term enters a residual with the frozen sign. Carry the grouped reference, rotations of the crossed labels, the exposed triangles and high spins through the full block. Accept one local inclusion only with every bare input on $I$ covered, a positive vacuum lower bound and a rational $v>0$ for which the outward majorant satisfies $M_I(0)\le v/16$ and $M_I(v)-M_I(0)\le15v/16$ componentwise. A certified excess rejects those charts. An unresolved inequality leaves the inclusion open. The decrease here supplies one signed bare boundary coefficient for that test. Control of the full effective action, physical stiffness and the seed requires further estimates.
