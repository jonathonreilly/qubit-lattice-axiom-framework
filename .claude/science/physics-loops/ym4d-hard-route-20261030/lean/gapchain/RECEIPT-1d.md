## Repo search

The lead's November 8 inventory covers main and PRs 10114, 10133, 10134 and 10141. Its closest outside-lane hit, MASS_GAP_LOCAL_BLOCK_ASTRA.md 106–149, gives a one-step plaquette correlation. I checked those lines on PR 10114. The search record lists the same text on PR 10133. Across those five local refs, I checked all 12 distinct out-of-lane Lean blobs for PositiveSlot, Hilbert–Schmidt terms, rotated kernels and cyclic spectral terminology. None matched. There is no row-specific prior digest at the pin. I found no competing assignment for the analytic trace identity in the open registry. Row 1509 owns the separate equality with the four-dimensional Wilson integral. [Lead’s repository search](../../library/prior/repo-search-2026-11-08.md)

Claude Opus 5.5 gave the hand transfer construction and Hilbert–Schmidt identities in row 667, Lemma A0 and §2, and the rectangular extension in row 698, Lemma 1.1. Claude Fable 5.2 supplied the spectral design in row 697. The committed Wilson and Transfer modules already construct the positive operator, its finite-family bound and its positive spectral slots. Their remaining interface is equality with the Haar cycle. This row formalizes that interface. [Stage 1c receipt](RECEIPT-1c.md)

Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the cubic transfer design. Outline index chunk 02 points to lines 2315–2335 at 31a47c543775. There GL8 identifies the cubic partition function with the trace using gauge averaging and trace cyclicity. CA-I 447–465 gives the normalized product Haar and plaquette conventions. I use the lane's rectangular kernel and the cubic construction as credited precedents. [Outline, GL8](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L2315-L2335) · [Complete Account I](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L447-L465)

## Plan

1. Check the assigned row, the prior-work records, the Sussman–Alpoge indices and the committed kernel and spectral interfaces.
2. In an isolated Lake project, prove the Hilbert–Schmidt pairing and composition identities needed for the cyclic integral, then specialize to Wilson.
3. Build with the pinned toolchain, record resources and the kernel's axiom reports, and state precisely which equalities were checked.

This receipt is a research checkpoint for row 1508 at `2ff9eeb6b`.

## BUILT

`GapChain.Kernel.cyclic_eq_tsum` identifies the cyclic integral of any complex square-integrable kernel inducing a positive operator on a probability space. At every integer length $a\ge 2$ the integral equals the sum of the real $a$-th powers of the positive eigenvalues, counted with multiplicity and embedded in $\mathbb C$. The theorem returns the equality and summability together. The theorem `GapChain.Kernel.integrable_cyclic` proves product integrability even without positivity. Compactness follows from the prior `GapChain.Kernel.operator_compact`.

`GapChain.Wilson.Trace.cyclic` uses the exact product Haar definition assigned to both rows. `cyclic_hasSum` identifies the positive-slot series with that real integral for every box, $\beta\ge0$ and $a\ge2$. `cyclic_eq_tsum` exposes the requested interface for $\beta>0$, valid $R$ and $a\ge3$. `summable_pow` gives its summability directly. This is a formal result for the finite-volume transfer integral. It supplies row 1509's trace hypothesis. This research receipt grants no scientific or audit status.

## Proof

For basis vectors $e_i,e_j$, the Fourier coefficient of a kernel against $e_j(x)\overline{e_i(y)}$ is $\langle e_j,T_ke_i\rangle$. Testing a zero operator against two indicators gives zero integral on every measurable rectangle. Uniqueness of vector measures then proves product-space completeness of those basis functions.

For every Hilbert basis, `hasSum_hs_pairing` gives $\sum_i \langle T_k e_i,T_l e_i\rangle = \langle k,l\rangle_{L^2(\mu\times\mu)}$. The product-basis construction uses no separability assumption. In `operator_compose`, the kernel $c(x,z)=\int k(x,y)l(y,z)\,d\mu(y)$ represents $T_k T_l$.

A loop with $n+2$ vertices has $n+1$ forward edges with kernel $k$ and one closing edge with kernel $l$. Its operator product is $T_lT_k^{n+1}$. Integrating vertex zero changes the closing edge to $l\circ k$. The norm of the shorter loop with the two incident norm kernels supplies the Fubini bound. When $n=0$, the two distinct directed edges contribute $k(x,y)l(y,x)$.

For the positive specialization, take any added basis vector $v$ orthogonal to the positive slots. For a $z$-eigenvector $y$, symmetry gives $\langle Tv,y\rangle=z\langle v,y\rangle$. This vanishes for $z=0$. Positivity makes each nonzero eigenvalue positive. Its slots index a basis of its full eigenspace, giving the eigenvalue its multiplicity. The compact spectral theorem gives $Tv=0$, so restricting the sum to slots preserves every nonzero term.

## Build and checks

The Mac mini launcher selected `gpt-6.2-astra` at max reasoning effort, at checkout commit `2ff9eeb6b15eda8f8e65d55b49e4535f9bb0a133`. Lean was `leanprover/lean4:v4.33.1` at `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`. Mathlib was `0df444a360eaa60ab8c11dca51a86af692955474`. The isolated Lake project compiled all five committed project modules from byte-identical sources and used the supplied precompiled Mathlib packages. Its package directory links to the supplied fixture, which the macOS sandbox protected from writes. The scratch library listed `GapChain.Trace` as a root. The checkout lakefile and toolchain matched the pinned blobs. Each build was admitted by `memory_pressure -Q` at 50% free or more. The compiler children ran serially with `LEAN_NUM_THREADS=2` and `/usr/bin/nice -n 10`.

The initial plan was saved at 02:34 UTC. The first full build found representative, Fubini and basis conversions. The second checked the arbitrary-basis formula and zero complement. It exposed two remaining elaboration errors in the specialization and an unsupported pretty-printer setting. The final source uses pointwise congruence on the slot injection and rewrites the Wilson operator to its kernel before taking real parts. The pretty-printer setting was removed.

The final Trace compilation is recorded in `check-03.log`. The complete `lake --no-cache build GapChain Validation` run passed in `check-04.log`. The first scratch consumer tried to synthesize a decidability instance for `Box.Valid`. Unfolding it to three natural inequalities fixed that example. The delivered Trace source was identical in both runs. The consumer checked the exact product body by `rfl`, both directed factors at $a=2$ for a general positive kernel, the Wilson equality at $β=2$, $R=(3,4,5)$, $a=3$, and summability at $β=0$, $a=2$. The separately compiled checkpoint contains the operator calculus, the cyclic recursion, and the slot basis. It reuses these proofs.

At 2026-11-25 06:26 UTC, the source SHA-256 was `dc9cc02c3cf3f0ea15004901a014430bdafa6b6fc8344c4650f4cbf245aea8a1`. Byte comparison, the 32-theorem / 32-axiom-report inventory and a scan for disallowed proof constructs passed. The proof uses the Lean kernel, the stated Lean and Mathlib dependencies, and the three axioms printed below. No numerical estimate enters the proof. The full logs and timing files are in `/private/tmp/sa-lean-gap-chain-stage1d-astra62.W7tIiu/logs`. Its parent contains `sa_ym4.tex`, `sa_ca_I.tex` and the Lake project in `project/`.

### Wall time and peak memory

Darwin `/usr/bin/time -l` reports maximum resident set size and peak footprint in bytes. A build's free-memory reading is its admission reading. A child's reading records conditions after admission. The two earlier queue requests launched no Lean process.

| Version query | Selected Lean | Wall (s) | Maximum RSS (bytes) | Peak footprint (bytes) |
| --- | --- | ---: | ---: | ---: |
| First query at checkout root | 4.36.0 | 1.02 | 51,363,840 | 10,863,312 |
| Query before correcting the scratch root | 4.36.0 | 0.94 | 51,298,304 | 10,781,368 |
| Query at the corrected scratch root | 4.33.1 | 0.13 | 50,266,112 | 10,535,632 |

| Invocation | UTC start | Free | Exit | Wall (s) | Maximum RSS (bytes) | Peak footprint (bytes) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| check-01 | 03:32:58 | 51% | 1 | 262.94 | 2,378,481,664 | 250,552,280 |
| check-01-TheoremS-61466 | 03:33:06 | 41% | 0 | 24.14 | 2,283,028,480 | 873,421,720 |
| check-01-LemmaM1-61470 | 03:33:30 | 39% | 0 | 39.82 | 2,040,233,984 | 517,966,144 |
| check-01-Wilson-61725 | 03:34:10 | 38% | 0 | 43.90 | 2,378,481,664 | 593,133,328 |
| check-01-Transfer-62147 | 03:34:54 | 37% | 0 | 62.60 | 2,162,769,920 | 640,237,544 |
| check-01-Trace-62454 | 03:35:57 | 37% | 1 | 83.41 | 2,171,912,192 | 585,351,216 |
| check-02 | 05:13:38 | 51% | 1 | 168.71 | 2,048,131,072 | 221,913,144 |
| check-02-SequenceLemma-1848 | 05:13:46 | 41% | 0 | 36.86 | 2,048,131,072 | 485,644,776 |
| check-02-Trace-1854 | 05:14:23 | 35% | 1 | 69.59 | 1,558,872,064 | 598,343,680 |
| check-02-Checkpoint-1998 | 05:15:32 | 37% | 1 | 54.81 | 1,978,138,624 | 558,137,440 |
| check-03 | 05:24:13 | 51% | 1 | 167.46 | 2,535,014,400 | 222,273,592 |
| check-03-Checkpoint-5899 | 05:24:19 | 40% | 0 | 34.25 | 2,535,014,400 | 593,772,544 |
| check-03-Trace-5900 | 05:24:54 | 37% | 0 | 79.34 | 1,921,253,376 | 608,256,024 |
| check-03-Consumer-7292 | 05:26:13 | 43% | 1 | 47.08 | 2,241,921,024 | 503,054,144 |
| check-04 | 06:25:42 | 52% | 0 | 46.96 | 2,341,306,368 | 205,348,800 |
| check-04-Consumer-29090 | 06:25:50 | 40% | 0 | 38.85 | 2,341,306,368 | 510,721,784 |

## Verbatim axiom reports

~~~text
'GapChain.Kernel.ae_eq_of_operator_eq' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.rankKernel_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.inner_rankKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.inner_rankKernel_rankKernel' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.exists_kernel_basis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.hasSum_hs_pairing' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_apply_ae' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.compose_measurable_ae' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.compose_eq_inner' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.compose_memLp' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.row_compose' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.operator_compose' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.evalPair_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.loopProduct_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.loopProduct_cons' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.loopProduct_rotate' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.loopProduct_aestronglyMeasurable' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integral_vertex' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.loopProduct_abs' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.prepend_apply' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.prepend_preserving' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integrable_loopProduct' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integrable_cyclic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.integral_loopProduct_succ' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.hasSum_loopProduct' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.exists_positive_slot_basis' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.pow_apply_eigenvector' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.hasSum_cyclic' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Kernel.cyclic_eq_tsum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Trace.cyclic_hasSum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Trace.cyclic_eq_tsum' depends on axioms: [propext, Classical.choice, Quot.sound]
'GapChain.Wilson.Trace.summable_pow' depends on axioms: [propext, Classical.choice, Quot.sound]
~~~

## Next two proposed rows and their decisive outcomes

1. Join the periodic factorization in row 1509 to this trace theorem. Check the cyclic definitions agree by `rfl`, prove $Z(\beta,a,R)=\sum_i\lambda_i^a$ at positive coupling for every valid box and $a\ge3$, and instantiate `torusData_of_trace` without a trace hypothesis. The decisive outcome is an unconditional Lean Wilson `TorusData` and its partition-function weight identity.
2. Prove a quantitative seed for that Wilson instance at a stated coupling and scale $N\ge3$. The decisive outcome is a kernel-checked proof of `T.seed N < 1 / 5041` for those parameters, or a counterexample or precise obstruction to that inequality. The present identity alone supplies no seed estimate.
