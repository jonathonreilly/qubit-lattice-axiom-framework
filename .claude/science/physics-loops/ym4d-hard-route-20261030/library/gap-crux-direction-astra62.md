# Repo search

Research note for row 1461 at `9ebd1828a`. The five refs were `origin/main@8b11ae2bb`, `pr/10114@f76f6c649`, `pr/10133@89faef229`, `pr/10134@1e70c7211` and `pr/10141@c73ad7b17`. The searches covered neutral transfer, Wilson weak-coupling gap, replica exchange, exterior-square kernels, cofinal seeds, first-passage shifts, bounded-width bare couplings, last crossings, slope bounds at last roots and calibration-weighted purity. The target-specific prior file is absent. The November 8 search covers thirteen UV obligations. The open registry lists no owner for the cutoff selection or the calibration integral. [Prior search](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md)

- On main, `research/mass-gap/library/gap-ac-lat.md` Lemma A gives a translation-invariant RP Wilson state with decay rate $m_0(\beta)$ in two directions **given** a positive infimum of twisted thin-torus masses. The open premise is already a weak-coupling mass estimate. Main's `su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md` §4 and `MANUSCRIPT_RG.md` §4.30 on PRs 10114/10133 instead exchange coordinates of two copies of a fixed posterior. They preserve the normalizers, and show pure-gauge saturation for unsigned exchange in their limiting test. PR 10134's `parts/upper-chain.md` F5/F10 leave a zero-momentum comparison or a block defect. These results concern other estimates. The target grep on PR 10141 returned no closer statement.
- On the five refs the specific compound-kernel, physical seed-size, harmonic-centre/least-root and last-root slope searches returned no matching theorem. The coarea search hit PRs 10114/10133 `SOFTHARD.md` C1 on single-link normalizers. The decisive hits are **in the pinned lane**. Rows 1304/1308 exclude every orientation of mixed neutral transfer minors. Rows 1321/1322 treat signed replica sewing. Row 1450 permits infinitely many seeds *on the sequence already defining a limit*. Row 1453 gives the bounded all-cutoff first-passage lag, equality of the shifted boxes, and the all-late seed criterion. Row 1456 §4.3 discusses the width of one first-passage window, conditional on the run-domain comparison. The precise distinctions enter the proofs below. [Minor obstruction](gap-positivity-astra-check-opus.md) · [Replica sewing](gap-solve38-check-opus.md) · [Existing subsequence result](sa-ym4-lean-faithful-astra62.md) · [First-passage comparison](prior/sa-ym4-lean-flow-vs-ca-opus.md)

**Result.** Any prescribed infinite set of calibrated cutoff depths contains a subsequence realizing the released continuum properties in the original units. A bounded-width interval of bare inverse couplings contains all last roots for a compact interval of reference levels. Together these facts permit a sufficient test for the gap using one Wilson integral, (4) below. **The strict integral bound, the physical seed and the mass gap remain open.** The two lemmas and the conditional implication have hand proofs here and await independent review.

**Plan saved at the start.** Read the published target and priors, fix an attack before the comparison, retire any duplicate, and work the first surviving lemma through its physical consequence. The two proposed follow-up rows are at the end.

## Phase 1, fixed before the later rows

**Proved input from the brief and source reading.** Ethan Sussman and Levent Alpoge, with Claude and Codex, obtain a subsequential Wilson continuum datum with a mixture of clustering OS components. A mass gap requires one positive-energy interval empty of spectrum on the vacuum complement. Any proof must enforce this exclusion in physical units as the cutoff disappears. The proposed slab estimate also has to pay for the multiplicities of all neutral excitations. The outline illustrates the distinction with the spectral density $E e^{-E}\,dE$. Its Laplace transform is $(1+t)^{-2}$ and its support reaches zero. The outline gives the vanishing filter responsible for its plateau bound. The earlier account leaves the mass gap open. [Outline index, chunk 01 at 588–599](sa-index/chunk-01.md) · [Chunk 03 at 3712–3720](sa-index/chunk-03.md) · [Chunk 29 at 31860–31882](sa-index/chunk-29.md)

**Published reach, as quoted here.** Tadeusz Bałaban's CMP 122b ultraviolet stability theorem controls the effective densities throughout a run for which $0<g_j\le\gamma$. Its stated range ends with that small-coupling condition. Magnen–Rivasseau–Sénéor keep an infrared cutoff. The strong-coupling lattice gap estimates apply in a small-bare-inverse-coupling regime. None of the located bounds controls the neutral thermal count on one fixed physical side of the tuned Wilson trajectory. The finite Wilson kernel used for the Phase 1 proposal is the outline's quaternion Gram expansion (AM2) and gauge compression (AM4), lines 2773–2795 and 2834–2854. [Bałaban quotation and source locations, §3](lit-balaban.md) · [CA-I, lines 4209–4240](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4209-L4240) · [Earlier literature reading](prior/gap-lit-recent.md)

**Guessed choice of attack.** Antisymmetrize two copies of the physical neutral transfer. Its exterior square cancels the vacuum-vacuum pair identically and retains the vacuum-excitation pairs. The kernel is the two-by-two determinant of actual blocked Wilson kernels. This puts the vacuum subtraction inside the integral without requiring its wavefunction. My first proposed lemma was that orienting pairs of boundary orbits could make every mixed determinant nonnegative, permitting a positive path estimate. I recorded this choice before reading any post-1142 research row. Its disposition follows.

## Phase 2, comparison and decision

**Proved earlier.** Row 1304 uses an exchange path of distinct boundary orbits to refute exactly the proposed lemma, even almost everywhere, at positive coupling and any finite slab thickness. Check 1308 R4 covers all minor orders at least two and independent choices of orientation on the two ends. Solve 38 retains the signs and still needs a relative weight of sectors after sewing. I stopped the orientation attack at that result. [Row 1304](gap-positivity-astra62.md) · [Check 1308](gap-positivity-astra-check-opus.md) · [Solve 38, check](gap-solve38-check-opus.md)

**Common wall, inferred from the recorded results.** On the physical spatial slice of growing lattice size, one must control all the neutral information that can pass through an interacting Wilson slab. Controlling a fixed list of observables, or obtaining a strict finite-cutoff contraction, leaves open a collective neutral mode or enough thermal multiplicity to spoil the estimate. In an RG proof the same missing input appears as a signed estimate on the full weight that can be continued through the intermediate coupling regime. An exact group-dependent coefficient helps only to the extent that the residual permits this continuation.

| Research rows | What survives the comparison |
|---|---|
| Solves 1–23, rows 1143–1221 | Fixed lattice size, an anisotropic solvable range, controlled parts of a seam, and electric/magnetic flux alternatives give genuine estimates. Fixed-size neutral levels can coalesce. The flux reductions already consume a neutral one-cube input. [Solve 2](gap-solve2-astra62.md) · [Solve 9](gap-solve9-astra62.md) · [Solve 23](gap-solve23-astra62.md) |
| Solves 24–45 and the two fresh attempts | Grid, winding, plaquette, adjoint-colour, update and noisy-face estimates leave a singlet sum or the unsmoothed two-period deficit. In particular an annealed adjoint Green-function bound and a cyclic family of plaquette histories at a fixed cutoff both coexist with the outstanding physical estimate. [Fresh colour attempt](gap-solve-fresh2-astra62.md) · [Solve 28](gap-solve28-astra62.md) · [Solve 45](gap-solve45-astra62.md) |
| Mechanisms 1380–1433 | The checked survey retains the borderline four-winding integral at fixed size and a bridge estimate. Time coarsening, two-cutoff comparison and local signed tensor contractions still require an estimate on the full normalized law. The checked ring arithmetic survives, while changing the disconnected reference changes the proposed sign assessment. [Selective survey check](gap-selective-5d-check-astra62.md) · [Time-coarsening check](gap-time-coarsen-check-astra62.md) · [Signed response check](gap-rg-response-search-check-opus.md) |
| Mechanisms 1434, 1438, 1439 and direction 1442–1447 | A positive straight-link heat factor fails the high-spin test, the matched-time invertible slice channel has zero neutral spectral gain, and thinning an independent commutator leaves the sign of the coarse interaction free. The Villain comparison restricts what a stand-alone factor implies. Fixed-probe overlap in the cell-event test leaves the full collective data open. The CM-O3 row is an upstream UV supplier. [1436](gap-mech-candidate-check-opus.md) · [1440](gap-mech-candidate2-check-opus.md) · [1441](gap-mech-candidate3-check-opus.md) · [1443](gap-mech-direction3-check-astra62.md) · [1445](gap-gc-astra62.md) |

**Decision, guessed direction.** Use the freedom to choose a continuum witness *after* locating favorable calibrated cutoffs. Then test the neutral heat trace integrated over a compact interval of physical reference levels. This changes which cutoffs must pass and gives a finite Wilson integral at untuned couplings. It still faces the physical wall in (4). Its compactness and width lemmas can be decided independently of that inequality.

## Phase 3, calibrated cutoff selection

**First lemma, proved here by hand.** Fix the release witnesses $b,M,\delta$ as in check 1453 and fix $0<g_0<\delta$. Write $\beta_K$ for the inverse square of its least positive bare root. For **every infinite set $E$ of original cutoff depths**, there are strictly increasing $K_j\in E$ giving a volume-first Wilson continuum limit in the original physical units with the same least-root calibration, positive separated two- and connected four-point witnesses, and an OS decomposition with almost-everywhere non-Gaussianity. The limit may depend on $E$.

1. **Proved input from rows 1451/1453, BND-2.** Put $x_i=\mathrm{coupling}(p,\beta_K,i)$, choose $W_*=\max(W',B_s+\gamma^{-2}+1)$ and $g_*=(W_*-B_s)^{-1/2}$. The first $J=J(K)$ with $x_J\le W_*$ gives a first-passage pair $(J,\beta_K)$ at this one $g_*$. Eventually $1\le J\le K$ and $0\le K-J\le D$, since $\lambda(K-J)-c_r\le x_J-x_K\le W_*-H$. The bound $D$ may depend on $g_0$. The least-root assertion holds at $K$ and the first-passage assertion at $J$. The root theorem supplies the full coupling conditions at every $0<g\le\gamma$, including $g_*$. [Root theorem, lines 9–22](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/ReferenceRoots.lean#L9-L22) · [Check 1453, bracket and slope](sa-ym4-lean-trajectory-check-astra62.md)
2. **Proved.** Partition the late elements of $E$ by the finitely many values of $K-J(K)$. On an infinite part the difference is one integer $d$. Enumerate it in increasing order. The corresponding $J=K-d$ are strictly increasing. Apply `su2_continuum_limit_of_frequent_passage` to the prescribed $(J,\beta_K)$. The frequent-passage hypothesis holds at every member. The theorem extracts a subsequence of its argument and applies the volume-first limit clause to those pairs. Its output includes the OS mixture, strictly positive second and fourth cumulant witnesses, and both moment limits at mesh $b^{-J}$. [Quantifiers and conclusions, lines 115–152](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/ContinuumLimit.lean#L115-L152)
3. **Proved.** Set $h=b^d$ and $D_h f(x)=f(x/h)$ on every argument. A torus of exponent $m$ at $K$ has the same number of sites as the torus of exponent $m+d$ at $J$. Barycentres and period vectors at $J$ are $h$ times their positions at $K$. The smear has no spacing prefactor. Evaluating $D_h f$ at $J,m+d$ therefore gives exactly the evaluation of $f$ at $K,m$, including periodization. The Wilson law on the indexed links is identical. Centered moments and cumulants agree. This is Sussman–Alpoge's finite dilation RF53 applied to the release normalization. For the simultaneous-volume tori at $J$, discard the finite prefix needed to subtract $d$ from their exponents and keep them positive. For each fixed $j$, do the same within its volume-first sequence. Relabelling the infinite-volume states equivalently gives both limits in the public statement. The original reference torus, tests and least root at $K$ were fixed at the start. [RF53, lines 22014–22040](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L22014-L22040) · [Release action, smear and calibration](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Challenge.lean#L81-L123)
4. **Proved.** If $S'$ is the limit in $J$ units, set $S(F)=S'(D_h F)$. Dilation commutes with rotations, permutations and time reflection, intertwines translation by $v$ with translation by $hv$, and preserves diagonals, time half-spaces and tensor products. It carries normalization and reflected positivity through the quotient. For the released Schwartz seminorm of order $q$, a derivative costs $h^{-|\alpha|}$ and the weight costs at most $h^q$. Taking $q=kn$ replaces the exponential growth constant $C$ by $Ch^k$. Apply this map to every component with its existing probability law. The barycentre identity and clustering on spatial rays follow. Applying the inverse test dilation to the nontriviality witnesses preserves their values. Finally $J/K\to1$ preserves the asymptotic-freedom coefficient. [OS axioms and growth](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Challenge.lean#L137-L190) · [Construction of the public volume limits](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/WilsonSubsequence.lean#L30-L67)

**Proved conditional consequence.** At a fixed $g_0$, it suffices for an existential calibrated gapped limit to find one $\ell\in4\mathbb N_{>0}$ with a passing neutral slab at infinitely many **original** least roots. Take $E$ to be their depths. For $n=\ell b^K$ and $w=\lfloor n/1024\rfloor$, row 1356 identifies the Hilbert–Schmidt test exactly with $s_K(2w)\le4/21$, where $s_K(t)=\sum_{i>0}(\lambda_i/\lambda_0)^t$ counts neutral eigenvalues with multiplicity. Here $\lambda_0$ is the vacuum eigenvalue. Equivalently the optimum of $\|c^{-1}P_0T^w-|\phi\rangle\langle\phi|\|_{\rm HS}$ is at most $2/5$, attained using the vacuum projector. In passage units the same finite operator has side $h\ell\in4\mathbb N_{>0}$ and the identical $n,w,\beta$. The large-size and logarithmic coupling conditions hold along this sequence. Dilation sends the even time grid $2b^{-K}\mathbb Z$ onto $2b^{-J}\mathbb Z$ and is a bijection of the positive-time test class used for totality. The checked gap implication at that side gives a unique vacuum and gap at least $2\log(2^{18}/5041)/(h\ell)$ in passage units. Original time $t$ corresponds to passage time $ht$. Hence in the original action-density sector the bound is

$$
m_{\rm phys}\ \ge\ \frac{2}{\ell}\log\!\frac{2^{18}}{5041}.
$$

One obtains the same rate by applying the checked implication to the relabelled volume-first data. [Sharp rank-one test](gap-mini-mneutral-fable.md) · [Original physical rate and conditions](sa-ym4-lean-faithful-astra62.md)

**Scope of the quantifiers.** The first lemma holds even if every seed fails. For the conditional gap, row 1450 already allows infinitely many successes inside one sequence defining a given $S$. Here the set of depths can be specified *before* choosing any continuum witness. Even and odd depths illustrate why intersecting two arbitrary infinite sets would fail. This improvement supplies an existential witness. A gap for a preassigned limit on a disjoint sequence, the all-late statement (M-neutral-all), and bounds on the seed's physical side each need further information.

### A bounded interval of bare inverse couplings

**Proved here by hand.** A compact interval of calibration levels can be searched in a bare inverse-coupling interval whose width stays bounded as $K\to\infty$. Its centre involves the release's actual table. Write $s=11\log b/(3\pi^2)>0$, let $a_i$ and $q_i$ be the table's oneLoop and secondStep entries, and set

$$
B_K=\sum_{i=0}^{K-1}a_i+\frac1s\sum_{i=0}^{K-1}\frac{q_i}{K-i}.
\tag{1}
$$

Write $R_K(\beta)$ for the fixed-reference covariance, $r(g_0)=c_{\rm ref}g_0^4$ with $c_{\rm ref}>0$, and $\beta_K(r)$ for the largest inverse-coupling root at response $r$. For each closed interval $I=[r_-,r_+]\subset(0,r(\delta))$ of positive length there are finite $C_I,K_I$ such that

$$
|\beta_K(r)-B_K|\le C_I\qquad(K\ge K_I,\ r\in I).
\tag{2}
$$

The centre satisfies $B_K=sK+O(\log(1+K))$. A universal two-loop coefficient and the physical seed size remain undetermined.

**Proof at the two endpoint levels.** Fix either endpoint. Use its tuned run $x_i=x_i(\beta_K)$ with $x_0=\beta_K$, $H\le x_K\le W'$ and $x_{K-j}\ge H+\lambda j-c_r$. The release table gives, on this above-floor prefix, $|q_i|\le Q$, a constant $A$ and the bounds

$$
\left|\sum_{i=u}^{v-1}a_i-s(v-u)\right|\le 2c,\qquad
x_i-x_{i+1}=a_i+q_i/x_i+e_i,\qquad |e_i|\le A x_i^{-5/4}.
$$

These use a *single* table for all roots. In the source, the refined remainder is written for the expansion flow. On the prefix its entries agree with the total-density flow. The bound $|x_i-x_{i+1}|\le 2T.B$ also holds there. [Refined step and second coefficient, lines 59–85](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/RecordCutoffs.lean#L59-L85) · [Average on every interval, lines 10–16](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/Construction/SummableBoundsOfTheFlow/FlowOfTheNumbers.lean#L10-L16) · [Step bound and agreement, lines 108–153](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/YangMills/ContinuumLimit/RunAboveTheFloor.lean#L108-L153)

Choose a fixed integer $j_0\ge1$ so that $H+\lambda j-c_r\ge\lambda j/2$ for $j\ge j_0$. The last $j_0$ steps give $|x_{K-j_0}|\le \max(|H|,|W'|)+2T.B\,j_0$. Sum the refined increment from $K-j$ up to $K-j_0-1$. The one-loop sum differs from $s(j-j_0)$ by at most $2c$. The other terms cost at most $(2Q/\lambda)\sum_{m=j_0+1}^{j}1/m+A(2/\lambda)^{5/4}\sum_{m>j_0}m^{-5/4}$. Consequently $|x_{K-j}-sj|\le C(1+\log j)$ for $j\ge j_0$. Since $x_{K-j}\ge\lambda j/2$ there,

$$
\left|\,x_{K-j}^{-1}-(s j)^{-1}\right|
\le \frac{2C(1+\log j)}{s\lambda j^2}.
$$

In the sum from $0$ to $K-j_0-1$ replacing every $q_i/x_i$ by $q_i/[s(K-i)]$ therefore has bounded total cost. The remainders have bounded total cost as well. For instance the sums of $(1+\log j)/j^2$ and of $j^{-5/4}$ converge by integral comparison. The omitted $j_0$ terms of (1) cost at most $j_0(s+2c)+(Q/s)\sum_{m=1}^{j_0}1/m$, and the remaining terminal value is bounded as above. This proves (2) for the two endpoints. Only the boundedness of $q_i$ enters.

**Proof between the endpoints.** At each fixed $K$, $R_K$ is continuous and tends to zero as $\beta\to\infty$. Indeed the action $A_{\rm ref}\ge0$ vanishes at the identity field. For any $\eta>0$ the Haar mass $v_\eta$ of $\{A_{\rm ref}<\eta/2\}$ is positive. Wilson probability of $A_{\rm ref}\ge\eta$ is at most $e^{-\beta\eta/2}/v_\eta$. The two smeared energies are bounded by fixed-cutoff constants times $A_{\rm ref}$, so their covariance tends to zero. If $0<r_1<r_2$, the intermediate value theorem gives a crossing of $r_1$ strictly to the right of the last crossing of $r_2$. Existence for all $r\in I$ is simultaneous on the tail by the least-root theorem. Thus $\beta_K(r_+)\le\beta_K(r)\le\beta_K(r_-)$, even if $R_K$ has many turning points. Taking the larger of the two endpoint constants proves (2). The bounded-width statement pertains to the bare couplings of distinct physical calibrations on the same table. Row 1456 §4.3 considers the width of a single *first-passage* window in that coordinate.

**A difference estimate checks the width and the order of choices.** For two endpoint runs let $\Delta_i=x_i-\tilde x_i$. On their common prefix, writing $j=K-i$, the same recurrence gives

$$
\Delta_{i+1}=\left(1+\frac{q_i}{x_i\tilde x_i}\right)\Delta_i+\varepsilon_i,
\qquad |\varepsilon_i|\le 2A\left(\frac{2}{\lambda j}\right)^{5/4}\quad(j>j_0).
$$

Increase $j_0$ so $4Q/(\lambda^2j^2)\le1/2$ there. The product of the inverse step factors on this prefix is bounded in absolute value by $\exp(8Q\lambda^{-2}\sum_{j>j_0}j^{-2})$, since $1/(1-u)\le e^{2u}$ for $0\le u\le1/2$. Iterating backward from the bounded endpoint difference at $K-j_0$ gives a uniform bound on the separation of the two bare roots independently of the centre formula (1). Iterating **forward** compares any intermediate root with one endpoint. Their starting difference is bounded by (2), their positive prefix floors follow just from $x_K,\tilde x_K\ge H$, and the forward product is bounded by $\exp(4Q\lambda^{-2}\sum_{j>j_0}j^{-2})$. The summable errors above and the final $j_0$ increments, each bounded in difference by $4T.B$, give one terminal upper bound for all $r\in I$. Thus a common $W_*$ and lag bound $D$ may even be fixed across that compact interval. This checks the width by a second derivation on the same refined table.

### A Wilson integral that would produce seed-bearing cutoffs

**Proved reduction. Inequality (4) is guessed.** Choose $I$ and a covering $C_I$ from (2), then one side $\ell\in4\mathbb N_{>0}$. Write $n=\ell b^K$, $t=2\lfloor n/1024\rfloor$ and $Z_u^0(\beta)=\operatorname{Tr}(P_0 T_{n,\beta}^{u})$. The superscript denotes the mean over the eight electric-centre translations on the physical gauge-invariant space. Use zero spatial twist. For late $K$, $t\ge2$. Put

$$
P_K(\beta)=\frac{Z_{2t}^0(\beta)}{Z_t^0(\beta)^2},\qquad
\kappa_K(\beta)=\mathbb E_{\beta,\rm ref}
[(X-\mathbb EX)(Y-\mathbb EY)(A_{\rm ref}-\mathbb EA_{\rm ref})].
\tag{3}
$$

Here $X,Y$ are the two fixed Wilson smears on the **reference** torus. The traces are taken on the **seed** spatial torus at that same bare $\beta$. Row 1373 and its finite-copy successors already show $0\le P_K\le1$ and $P_K\ge457/625\Rightarrow s_K(t)\le4/21$. I use that stronger two-period test. Its deficit $1-P_K$ and its exact spatial-face integral already occur in the seed work. [Two-copy bound](gap-seed5-astra62.md) · [Rank-one criterion](gap-mini-mneutral-fable.md)

The proposed Wilson estimate is

$$
\liminf_{K\to\infty}\frac{1}{|I|}
\int_{\substack{|\beta-B_K|\le C_I,\ \beta>0\\r_-<R_K(\beta)<r_+}}
[\kappa_K(\beta)]_+\,\bigl[1-P_K(\beta)\bigr]\,d\beta
< \frac{168}{625}.                                      \tag{4}
$$

It tests a signed three-point action insertion against a neutral partition-function ratio at uncalibrated couplings. It needs no root finder in the integrand. The physical content is whether the neutral thermal deficit is small on enough of the *decreasing* reference crossings. The reference width, origin of $\beta$, two tori and sign of the insertion in (4) are fixed before that question is tested.

**Proof of the implication.** By differentiating the normalized finite Haar integrals in (3), $-R_K'=\kappa_K$. Every integrand before normalization is bounded on compact $\beta$ intervals, and the partition function is positive on the real axis. Thus $R_K$ is real analytic there. It is nonconstant on the late tail since all levels of $I$ are attained and its limit at infinity is zero. Its critical points are isolated on any compact interval. Split the interval in (4) into its intervals of monotonicity and change variables $r=R_K(\beta)$ on each decreasing piece. Endpoints and critical values have zero Lebesgue measure. For every remaining $r\in I$ the last root $\beta_K(r)$ lies in this window, is simple, and has negative derivative because $R_K<r$ to its right by the last-root property and the zero limit. All other decreasing crossings add nonnegative weight. The integral divided by $|I|$ consequently majorizes

$$
\frac{1}{|I|}\int_I [1-P_K(\beta_K(r))]\,dr.
\tag{5}
$$

$P_K$ is continuous at positive coupling by its finite Wilson integrals, and the last root is monotone in $r$, so this average is measurable. If (4) holds, choose $\epsilon>0$ and infinitely many $K$ with (5) at most $d_*-\epsilon$, where $d_*=168/625$. The set $G_K$ of $r$ with $1-P_K(\beta_K(r))\le d_*$ has measure at least $\epsilon|I|/d_*$. Every tail union of these sets has at least that measure. Continuity of finite measure from above gives the same lower bound for their limsup. Choose one $r$ there *once*, then $g_0=(r/c_{\rm ref})^{1/4}$, and apply the first lemma to the infinite set of its good cutoffs. This supplies the original physical gap bound for a jointly chosen calibrated limit. For a prescribed $g_0$, the first lemma applies directly to its good depths. An interval average alone selects a positive-measure set of levels and need not contain that prescribed value.

**Proved lower bound on the magnitude of the descending slope for a set of levels.** The bounded width gives a quantitative Wilson estimate even before imposing (4). For every late $K$,

$$
\int_I \frac{dr}{\kappa_K(\beta_K(r))}\ \le\ 2C_I .
$$

Omit the finitely many critical values in this integral. On each decreasing piece, restrict to the points that are last crossings of their level and substitute $r=R_K(\beta)$. The integral becomes the length of these disjoint subsets of the bare-coupling window. They have total length at most $2C_I$. Hence the levels whose last-root slope magnitude satisfies $\kappa_K(\beta_K(r))\le\eta$ have measure at most $2C_I\eta$. Fatou's lemma gives $\int_I 1/\limsup_K\kappa_K(\beta_K(r))\,dr\le 2C_I$, using the extended nonnegative reciprocal. For almost every fixed level the reference action insertion therefore stays strictly positive on some infinite subsequence, with a lower bound that can depend on the level. If (4) holds, take $2C_I\eta<\epsilon|I|/d_*$ in the selection proof. A positive-measure set of levels then passes the neutral seed **and** has descending slope of magnitude at least $\eta$ at the same infinitely many cutoffs. The remaining estimate concerns the thermal deficit at those crossings.

**Attempt on (4), proved obstruction to dropping its sign selection.** At $\beta=0$ and late $K$ the two small bump supports involve disjoint sets of bonds, also across the periodic boundary of side at least eight. Under product Haar their smeared energies are independent, hence $R_K(0)=0$. We already proved $R_K(+\infty)=0$. Globally the integral of $\mathbf1_I(R_K)(-R_K')$ is exactly zero, by applying the fundamental theorem to the function $u\mapsto\min(\max(u-r_-,0),|I|)$. The downward variation crossing $I$ is at least $|I|$. Thus a signed endpoint cancellation in the reference response would discard the very roots needed for the seed. The variable thermal factor and the positive part in (4) require a genuine joint estimate.

**Independence checks, proved.** A successful seed need not satisfy the integrated purity criterion. For a positive transfer whose normalized thermal probabilities at time $t$ are $(21,2,2)/25$, the seed is exactly at threshold while $P=449/625<457/625$. Keeping these probabilities at every level and taking one decreasing crossing of each level produces an algebraic example that passes the seed and fails (4). As a second check, tensor any Wilson transfer with a centre-neutral independent two-state reversible transition with eigenvalues $1,u_K$, $u_K=e^{-1/n^2}$, diagonal entries $(1+u_K)/2$ and off-diagonal entries $(1-u_K)/2$. The Wilson response and its derivative are unchanged if the reference smears act only in the Wilson factor. But the purity is multiplied by $(1+u_K^{2t})/(1+u_K^t)^2\to1/2$. By (5) the normalized integral then has lower limit at least $1/2$. A proof using only the reference-flow estimates and generic transfer positivity misses which neutral modes the actual SU(2) Wilson action permits. The additional neutral state tests precisely what the reference observable can control.

**An exact way to omit surplus crossings.** Set $B^\pm=B_K\pm C_I$, restricting to late $K$ so $B^->0$. For $u\in[B^-,B^+]$ put

$$
F_K(u)=\min\!\left(|I|,\ \max\!\left(0,\max_{u\le v\le B^+}R_K(v)-r_-\right)\right).
$$

For all $r\in I$ except possibly the single height of this maximum, $\beta_K(r)>u$ precisely when $r$ lies below that maximum. This follows by continuity and passage to the zero limit on the right. After $B^+$ every response is below $r_-$, by (2) and the last crossing of $r_-$. Thus $F_K(u)=|\{r\in I:\beta_K(r)>u\}|$, from $|I|$ at the left endpoint to zero at the right. The finite positive Stieltjes measure $-dF_K$ is exactly the image of $dr$ under the last-root map, as seen by subtracting two such tail lengths. Consequently

$$
L_K=\frac1{|I|}\int_{B^-}^{B^+}(1-P_K)\,(-dF_K)                 \tag{6}
$$

is precisely (5), lies in $[0,1]$ uniformly, and costs no multiplicity for extra downward oscillations. The same selection proof works with $\liminf L_K<168/625$. Identity (6) is bookkeeping. Its quantitative Wilson estimate is open.

**Direct attempt to carry a measured purity across the interval.** The finite-torus neutral trace is the positive mean of eight time-twisted Wilson integrals. If $A_u$ denotes the dimensionless signed-plaquette Wilson action in the corresponding positive mixture (each plaquette term is between zero and two), differentiation gives

$$
(\log P_K)'=2\langle A_t\rangle_{t,0}-\langle A_{2t}\rangle_{2t,0}.
$$

There are $6un^3$ plaquettes on a period-$u$ torus, so the absolute value on the right is at most $24tn^3$. Each nonnegative term in the displayed difference is bounded by that same number. An interval mesh of spacing at most $\eta/(24tn^3)$ therefore transports a proved log-purity value to within $\eta$. Using only the action range to cover (2) takes order $tn^3$ intervals at fixed width and tolerance. Across a fixed positive fraction of that width the resulting error allowance grows like $n^4$. This estimate gives no strict upper bound below the threshold in (6). One would have to bound the **difference** of the two thermal action means or control the weighted purity by another Wilson-specific argument. The two-period energy comparison itself is present in the earlier coupling-interpolation work. [Prior two-period comparison](gap-solve10-astra62.md)

**Verification scope.** The original mathematics above consists of written arguments. I read the pinned public Lean sources through raw file URLs into a fresh scratch directory because the designated local release folder contained TeX and the overview. The implementation is `wilson_subsequence` in `Formulation/WilsonSubsequence.lean`, while `Challenge.lean` also contains the public specification. The release reports Lean 4.33.1 with Mathlib and the axiom dependencies `propext`, `Classical.choice` and `Quot.sound` for its continuum export. This row used no build, evaluator, numerical evidence or newly kernel-checked assertion. The analytic cutoff-selection and width lemmas await an independent check. [Implementation](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/3932084a9b82fc79466b4a2faad9ec032b637445/YM4%20Lean/Formulation/WilsonSubsequence.lean#L69-L71) · [Release verification record](sa-ym4-lean-faithful-astra62.md)

## Next two rows and their decisive outcomes

1. **Check calibrated cutoff selection and the bounded inverse-coupling interval.** On the pinned release verify the two volume indices, test dilation, Hamiltonian time unit, common refined table and summability in (1)–(2). Check the reciprocal-slope bound by the variation of the monotone last-root map. Success establishes an independently checked reduction from seeds on a prescribed infinite set of raw roots to an existential calibrated gapped witness. A failure should identify the first incompatible source hypothesis and which reduction survives.
2. **Estimate neutral purity on decreasing reference levels.** Fix one physical side and a compact interval of positive calibrations. Use the archive's complete-face deficit or the two-period action difference to bound (4) or (6) strictly below $168/625$ along unbounded cutoffs, with one margin. That yields a gapped calibrated action-density limit and the displayed physical rate. A lower bound at or above the threshold on every late cutoff for the proposed side and interval rules out that particular integrated test. A single finite-cutoff value leaves the physical estimate open.
