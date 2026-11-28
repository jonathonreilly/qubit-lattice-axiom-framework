# Repo search

FINISH row 1432, Mac mini slot `repo2`, pinned at `1a479e108f7cffaf60466fc589bc281d7103a30c`. The lead’s search and row 1425’s follow-up on main and PRs 10114, 10133, 10134 and 10141 found general character duality and finite-cutoff loop bootstrap on main (`gap-crux-lit-nonab.md` §T6 and `gap-crux-lit-2.md` 237), a single-loop bound in PR 10114 (`MASS_GAP_LOCAL_BLOCK_ASTRA.md` 106–149), finite-configuration ribbon tests (`EXISTENCE.md` 3758–3761) and a planar Gram form (`ro1.md` (6.2)). I checked those passages. Each concerns a different observable or a general representation. Searches of Lean files for the exact numbers and row name on those refs and PR 10144 found no ring replay. The row-specific prior file is absent and the registry has no matching owner. [Lead’s search](prior/repo-search-2026-11-08.md)

Row 1418’s Lean fixture covers a two-dimensional square. Row 1421 supplies the one-plaquette coefficient bounds. The direct sources for this replay are row 1425’s signed histograms and rounding contract, and row 1429’s checks. [Row 1425](gap-rg-ring-sign-astra62.md) · [Row 1429](gap-rg-ring-sign-check-opus.md)

## Stage 1 result

Lean 4.36.0 checked all finite arithmetic required for the final row-1425 table. The 4D numerator is negative after its tail is included, the common vacuum is positive, and their quotient together with the bounds on $\mathbb E_4W$ gives $g_4-1\ge109/10^9$. On the row-1425 interpretation this rules out a decrement for the frozen alternating ring. Identifying the arithmetic with the Haar integrals is the open Stage 2 task below.

Here $h,k$ are the imaginary quaternion parts of the two rooted plaquette holonomies in the $(1,2)$ and $(3,4)$ planes. Row 1425 uses $W=|h|^2|k|^2$, $T=(h\cdot k)^2-W/3$, and the magnitude ratio to the same-angle independent-conjugation reference, $g_d=|1-6\mathbb E_dT/\mathbb E_dW|$. The common vacuum $Z$ uses $e^{\beta q(g)}/A(\beta)$ on every internal face, with $A(\beta)=\int e^{\beta q(g)}dg$ for probability Haar. The table uses these labels for the corresponding arithmetic expressions. [Frozen routings in row 1424, equation (7)](gap-rg-two-cycle-astra62.md)

| Quantity in row 1425 | Kernel-checked value or enclosure |
|---|---|
| Marked core through $z^{46}$, in units of $10^{-15}$ | $[-25591398,-23250036]$ |
| Ordinary core through $z^{28}$, in units of $10^{-15}$ | $[1256795084726467,1259476223854567]$ |
| Marked circle at $11/4$, first omitted even power 48 | $216821257148$, remainder at most $204047/10^{15}$ |
| Vacuum circle at $9/4$, first omitted even power 30 | $15466258$, remainder at most $524181115/10^{12}$ |
| $N=z_{B_4}\mathbb E_4T$ | $[-25795445,-23045989]/10^{15}$ |
| $Z=z_{B_4}$ | $[1256270903611467,1260000404969567]/10^{15}$ |
| $N/Z$, labelled $\mathbb E_4T$ | $[-2054,-1829]/10^{11}$ |
| $\Delta_4=Y_{\rm alt}+Y_{\rm grp}/3$ | $[-4072,-3488]/10^{14}$ |
| $g_4-1$ | $[109,484]/10^9$ |
| $\mathbb E_5T$ | $[-5148361,10296722]/300000000$ |
| $\Delta_5$ | $(87/100)^9[-5148361,10296722]/(144\cdot300000000)$ |
| $2g_5$ | $[131133152,234433424]/10^8$ |
| Fixed-charge scalar trace-removal multiplier | $[0,0]$ from $1-1$. The group-theoretic identification is open. |

The leading coefficient is $15655/169075682574336$ by both rational sums. The division uses the unrounded quotient endpoints in the subsequent computations of $\Delta_4$ and $g_4-1$. For the conditional estimates, the kernel checks $Z,W_1>0$ in their scaled boundary-box forms. In dimensions 4 and 5 it verifies, respectively, $(\eta,\xi,w)=(1450,1037,5047)/10000$ and $(2934,2269,4354)/10000$, where $D\le\eta W_1$, $D\le\xi Z$ and $W_1\ge wZ$ on those boxes.

The complete file checked in 1285.84 seconds with 1,444,233,216 bytes peak RSS. All 584 named theorems reported no axioms. [Lean source](../lean/ring/Ring.lean) · [Receipt, run measurements and verbatim axiom output](../lean/ring/RECEIPT.md)

The source uses only `import Init`. The integer checks use kernel reduction through `decide` and `rfl`. The trusted computing base is the stated Lean kernel and its bundled core arithmetic. External scripts supplied literal data. The file checks the Taylor and interval endpoints, the rational sums and the integer square-root witness. Earlier order-34 and order-40 diagnostic core logs, auxiliary absolute-value shell totals and the 1,689 individual magnetic comparisons were outside this final-table replay. No audit or scientific status changes follow from the row.

## Source conventions

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, supply the probability Haar and Wilson conventions (outline 238–278), the Bessel character series and bounds GL3–GL4 (2195–2243), and the quaternion formula (2773–2781). The index and neighbouring entries in chunks 01–03 locate these passages. CA-I 43099–43109 defines a constrained Wilson action in a different calculation. The index’s Haar and common-integral obligations concern other constructions. Both external sources are pinned at `31a47c543775`. [Outline index](sa-index/README.md) · [Index of obligations](sa-index/obligations.md) · [Pinned outline](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2195-L2243) · [Pinned complete account](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L43103-L43107)

## Plan saved at creation

1. Confirm the pinned source, ownership and scope. Locate row 1425, its check, the index entries and certificate data.
2. Start with the quotient and degree-16 coefficient. Encode the signed histogram and outward interval arithmetic in one core Lean file, with rejected sign and vacuum fixtures.
3. Check the numerator, vacuum, both circle enclosures, even Cauchy tails and final table. Record each proof run and every axiom report.
4. Write the remaining Haar identifications as named obligations and give the decisive outcomes of the next two rows. This research grants no status.

## Replay record

The installed executable reports Lean 4.36.0, release commit `611c117bfaf7b7ae1cfcf246ce6fba31e8f509e9`. The external witness directory contains all five requested producer scripts. I read them as data. The marked order-42 file has 1,897 histogram rows (13 signed zeros), and the ordinary order-28 file has 96. The two retained bounds use extrema of the **whole sum within each coupling cell**. Adding independently rounded shell extrema would lose the cancellation needed for the marked sign.

### First kernel checks

The four-dimensional division and the five-dimensional endpoints replay from the logged integer inputs. Changing the sign of one marked insertion gives `[1829,2054]/10^11`. Using a unit vacuum gives `[-2580,-2304]/10^11`. Both are disjoint from the claimed moment. The degree-16 coefficient agrees by two exact sums, one from the signed histogram and one from the four multiplicities of the sphere fixture. The core, circle and conditional input bounds were still open at this checkpoint.

### Histogram and tail construction

For a histogram of arity $a$ (the number of its nonzero spins) the evaluator multiplies its monomial by $2^{112(24-a)}$. All terms then have denominator $D(2^{112})^{24}$, with $D=6298560000$ for the marks and $D=9$ for the vacuum. One further factor of $2^{112}$ accounts for the prefactor, $16/\beta^4$ for the marks and one for the vacuum. The kernel verifies divisibility of every rational coefficient denominator and the arity bound. Positive coefficients use the lower monomial endpoint for the lower sum. Negative coefficients use the upper endpoint. The evaluator sums on each closed cell before rounding to units of $10^{-15}$.

The eight scalar and prefactor intervals in each marked cell are literal integers. Each is checked against its own rational endpoints. In the positive Bessel series the numerator uses the sum through $k=32$, a common denominator $(2q)^{n+66}33!(n+34)!$ for $\beta=p/q$, and twice the first omitted term on the upper side. On a cell $[a,b]$, positivity pairs $L_n^-(a)$ with $L_0^+(b)$ for the lower ratio, and $L_n^+(b)$ with $L_0^-(a)$ for the upper ratio. This is a finite polynomial-and-majorant calculation. Identifying it with the Haar character is a later obligation. The first four full marked cells passed together. The next run covered the full 512-cell and 128-cell meshes.

Two circle witnesses use a separate $2^{80}$ grid. They include all 25 low-spin weights, the 49 tensor-product sums, the high-spin correction, the two maxima and the squared norms. The marked square-root numerator is $7172047727325330188$ on the $2^{56}$ grid. Verifying the two neighbouring integer squares suffices for its outward rounding.

### Conditional-grid construction and provenance

The two-dimensional conditional grid has four closed coupling cells crossed with 2,048 closed angle cells in each of $d=4,5$. For each coupling cell the checker forms the 21 scalar and derivative coefficients. It splits $6k+n(1-n)$ into its positive and negative parts before enclosing the derivative. On each certifying angular interval it checks the Chebyshev recurrence through its second derivative, both denominator signs, and three inequalities by integer cross multiplication. For example, the upper test on $D/W_1$ reads $10000D_{\rm hi}\le\eta_{\rm int}(W_1)_{\rm lo}$ in the shared scaled units. Every product takes its minimum and maximum over the four endpoint products before outward rounding. At this checkpoint the full conditional-grid run was still pending.

All scratch inputs and timed proof logs for this run live in `/tmp/sa-gap-rg-ring-lean-replay-astra62.2nayX0`. A reverse decoder reconstructed every original spin key, signed numerator and denominator from the delivered Lean literals, in file order. The marked and vacuum source files have SHA-256 `a74838223d2f9e5fec4fdb648cbd7b0cdfb4d2619bfaf26497d719b4a8939acb` and `ae66db958f3c42062d7707e2bb90d07634d0829a7e1dcceb6503ab1634e9fdae`. The full core and circle run was `corecircle`. The conditional-grid trial and the two deliberately false acceptance claims followed it.

### Complete core and circle pass

Lean exited 0 on all 512 marked coupling cells, all 128 vacuum cells, both circle calculations and both Cauchy remainders. The 290 declarations in that run each reported no axioms. The run took 1,153.14 seconds and peaked at 1,434,796,032 bytes. From these checks the vacuum interval is strictly positive and the normalized four-dimensional moment interval is strictly negative. A separate kernel run accepted the conditional input tables and the first eight angular cells in both dimensions. Each deliberately false quotient claim failed specifically because `decide` proved its proposition false.

The kernel also located the rounded extrema. For the numerator, cell 0 supplies the upper endpoint and cell 511 the lower. For the vacuum, cells 0 and 127 supply the lower and upper endpoints, respectively. The bounds on $b=2\lambda_1$ hold on each of the 512 marked cells. Flipping the one degree-16 grouped coefficient $-160/3$ to $+160/3$ changes the leading fraction to $50215/169075682574336$ and fails the sphere-fixture comparison.

The eight-angle direct conditional trial took 34.09 seconds. To check the full grid economically, the final certificate groups adjacent original angle cells when every dimension and coupling passes the same interval tests on their union. The 271 closed intervals have widths $1,2,4,8,16,32,64,128$ in fine-cell units, occurring $160,48,18,13,9,8,11,4$ times. The kernel checks the endpoints of every constituent fine cell against its parent, both denominator signs and all three tests on every parent, and that the contiguous cover ends at 2,048.

Eight representative covering intervals passed in a preliminary kernel run. The first integrated run hit its 1,400 MB Lean memory limit while checking both 49-entry convolution lists in one declaration. I stopped it after the diagnostic. The revised source checks seven consecutive seven-entry groups per circle and verifies that they cover all 49 tensor-product indices. This calculation passed in 7.13 seconds at 551,862,272 bytes peak RSS. The accepted full run used sequential elaboration, a 1,600 MB internal limit and a separate 2 GiB RSS guard. Its complete output is `verified.out`.

## Stage 2 obligations

These are proposed Lean theorem names and statements. They are open. Their inputs use probability Haar on the positive bonds of $B_d=\{0,1\}^d$, inverse transport on reversed bonds, $q=\operatorname{tr}/2$, and the row-1425 rooted $(1,2)$ and $(3,4)$ circuits through the origin. The band is the closed interval $[2,513/256]$.

| Proposed theorem | Statement needed to attach the finite certificate to the integral |
|---|---|
| `wilson_bessel_coefficients` | The normalized plaquette weight has character coefficient $b_n=(n+1)L_n/L_0$, with $L_n(x)=\sum_{k\ge0}(x/2)^{n+2k}/[k!(n+k+1)!]$. Prove positivity, the GL4 factorial majorant, $L_n/L_0\le1$, the derivative weights $6k+n(1-n)$ and the infinite-series remainder bounds used in the finite tables. |
| `marked_recoupling_trace` | On the $C_4\times C_4$ presentation of the 24 faces, ordinary link integrations give the two stated Clebsch–Gordan paths and their phased $6j$ overlap. At the common root the two trace-free insertions give $16K/\beta^4$ with $K=X(X+1/2)-C_aC_b/3$ and $X=J_a\cdot J_b$. Prove the triangle-root cancellations and recover each signed rational weight with the stated orientations. |
| `spin_histogram_complete` | For sums of twice-spin labels at most 46 for the marks (spin order 42) and at most 28 for the vacuum, the triangle and parity intersections, pruning and root-preserving orbit multiplicities cover every labelled assignment exactly once with its weight. Grouping equal multiplicities gives precisely the two literal lists, including their zero entries. |
| `haar_sphere_moment_fixture` | Identify quaternion probability Haar with uniform measure on $S^3$ and prove the trace-pairing moment identity. It must give the eleven degree-16 supports and their four signed values with multiplicities $4,4,2,1$. Only the rational addition is checked here. |
| `temporal_circle_and_even_remainder` | The temporal-gauge integral has the two slice norms and cube-sphere convolution used in row 1425. Derive $M^{11}M_Q\sqrt{P P_Q}E_5$ and $M^{12}P E_5$, including the high-index correction in $E_5$. Prove entireness, central-sign evenness and the Cauchy estimate beginning at powers 48 and 30. The finite ceilings and geometric factors are available in this replay. |
| `conditional_quadrupole_bounds` | Derive the $Z,W_1,D$ polynomial integrands from the four-link conditional law, including their derivative and spin tails. Prove nonnegative quadrupole amplitude, the two successive minimum-principle extensions to the staple balls, and independence of the two pairs conditional on the exterior links. Integrate the bounds against their common positive exterior law. Deduce $\mathbb E_4 W\ge(5047/10000)^2$ and the five-dimensional inequalities from the checked boundary boxes. |
| `ring_routings_common_vacuum` | For every real coupling in the band, identify $N(1)=z_{B_4}\mathbb E_4T$, the ordinary $Z(1)=z_{B_4}$ and both normalized routings with row 1424 (7). Include positivity of the four- and five-dimensional Wilson vacua, $\Delta_d=b^9\mathbb E_dT/144$, $g_d=\lvert1-6\mathbb E_dT/\mathbb E_dW\rvert$ and the one-dimensional fixed-charge routing identity, including inadmissible assignments. Compose the preceding obligations with the arithmetic. |

## Next two rows

1. **Identify the signed finite expansion.** Prove `wilson_bessel_coefficients`, `marked_recoupling_trace`, `spin_histogram_complete` and the sphere-moment fixture in the stated conventions. Acceptance requires termwise agreement with both literal histograms, including orbit multiplicities and empty vacuum. A differing sign, multiplicity or supported term supplies a specific counterexample and reopens the affected core.
2. **Attach the tails and normalize the physical response.** Prove `temporal_circle_and_even_remainder`, `conditional_quadrupole_bounds` and `ring_routings_common_vacuum` on the full band. Success gives a kernel proof that the frozen alternating ring increases in magnitude in four dimensions. An unproved analytic bound leaves that integral-level verdict open. Row 1431 already identifies the crossed matching as another reading of the same moment. A four-direction carry would require its own signed contribution to an independently specified block map. [Row 1431](gap-rg-response-search-check-opus.md)
