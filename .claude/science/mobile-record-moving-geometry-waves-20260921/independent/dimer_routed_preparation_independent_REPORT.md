# Independent color-preparation proof check

No mathematical correction is required at the reviewed source identities.
The displayed Poincaré, path-comparison, nonreversible contraction and
random-completion mixture arguments reconstruct. The prescribed
epsilon_N=N^-4 also transfers the stationary mean-square theorem, not only
bounded distributional tests. This is a bounded scientific check, not an
audit or retained-status decision.

The complete supplied note was read before any new author checker/results.
The independent derivation, runnable control and full logs were sealed at
`PRE_COMPARISON_SEAL.json`, SHA-256
`c83e2eaa9cd1e5cf8deafc3659377bc3918867cfb3a5f6eaefdbb443018f7dfe`.
The author checker, complete combined results, all group outputs and logs
were inspected afterward. No dynamic aggregate or moving-geometry extension
was read.

## Reconstructed load-bearing steps

1. With D_all=(1/2)sum E(Delta_ij f)^2, the conditional-label bijection gives
   Var(E[f|sigma(i)])<=D_cross,i/K. The factor 1/K is exact for indicator
   functions of the label at i. Averaging the induction gives coefficient
   2/K-2/[K^2(K-1)]<=2/K. Equal-size permutation fibers extend the result
   to every color-count sector; singleton sectors have zero variance.

2. A path of length l realizes an endpoint transposition in 2l-1 swaps and
   restores every intermediate immutable label. Each edge occurs at most
   twice per reference pair, hence at most K(K-1) times in the full comparison.
   This yields Var<=2(2D-1)(K-1)D_H with the note's continuous-time convention.
   Contracting a perfect matching preserves connectivity and cannot increase
   the physical torus diameter 3N/2. Every simple contracted edge has an actual
   channel; multiplicities add rather than reduce energy.

3. The actual stationary color generator has symmetric rate k0/2 per channel.
   Consequently g_N=k0/[4(3N-1)(K-1)] is a valid uniform lower bound.
   Density evolution uses the adjoint generator, whose symmetric part is the
   same S; differentiation gives d||h-1||_2^2/dt<=-2g_N||h-1||_2^2 even
   though the dynamics is nonreversible. Point-mass centered norm squared is
   |Omega_counts|-1, and TV<=||h-1||_2/2. The displayed preparation time
   follows by the deliberately loose |Omega_counts|<=14^K bound.

4. At the random first-completion time, condition on its entire past and apply
   the uniform sector mixing estimate for a common deterministic elapsed
   time. The strong Markov property justifies that restart. The formation
   premise supplies multinomial counts independently of the completed
   matching. Mixing uniform sectors with those weights gives exactly iid
   colors p, independently of that matching, within the stated TV error.
   Neither arrangement independence at completion nor continuous-key mixing
   is presumed.

5. A common M-dependent Markov path kernel contracts TV, including observation
   intervals of microscopic length Nt. A fourteen-indicator Fourier field
   has norm at most sqrt(2K), so its squared propagation residual is bounded
   by C K for fixed modes, times and parameters. Its expectation changes by
   at most C K epsilon_N. Here K epsilon_N=1/(2N), which vanishes. This is
   the necessary additional control for mean-square transfer; epsilon_N->0
   alone would not suffice for this argument.

The complete reconstruction, including the explicit complex-function
extension and the probability-kernel comparison, is in
`PRE_COMPARISON_DERIVATION.md`. The proof gives an O(N^7/k0) sufficient
microscopic waiting time after completion; for epsilon_N=N^-4 the extra
logarithmic term is O(N^4 log N/k0). It does not estimate tau_fill or a
sharp mixing exponent. At gamma=0 the imported propagation matrix is the
identity, consistently with the corrected routed note.

## Independent finite evidence

`independent_check.py` completed on its first execution. Its exact arithmetic
checks and explicitly numerical checks are distinguished in the saved output:

- Conditional-mean controls on all positions for K=2,...,5 distinct-label
  permutations, including exact equality of the indicator ratio 1/K.
  Exact rational LDL certificates establish the sufficient complete-swap
  bound on the full mean-zero spaces for K=2,3,4.
- All endpoint-transposition words on all distinct-label arrangements for
  five independently chosen graphs: path, star, diamond, a triangle with
  a bridged tail, and a five-cycle. There are 2,832 such word checks.
  Exact rational LDL certificates verify the claimed graph gap lower bounds
  on color sectors of sizes 24,12,6,20,20. These include irregular and
  nonbipartite graphs; no numerical eigenvalue tolerance certifies these
  particular lower bounds.
- Independently contracted N=8 winding, columnar and irregular matchings
  have exact graph diameters 8,10,6, respectively, all below 12. These are
  finite controls of the geometric comparison, not its all-volume proof.
- A separately assembled 24-state four-position context chain with
  k0=5/4 and gamma=3/4 is nonreversible. Exact matrices verify uniform
  stationarity, S=(k0/2) times the graph-swap generator, the density-energy
  identity, and the comparison gap 5/144. Five matrix-exponential evaluations
  check the associated L2/TV estimates numerically.
- All 2,744 color arrays in the full fourteen-label K=3 space, partitioned
  into 560 sectors, satisfy the multinomial-to-product identity exactly for
  a nonuniform full-support p. Symbolic logarithmic arithmetic checks the
  preparation schedule and K epsilon_N=1/(2N) for N=8 through 128.

The preserved excluded-hypothesis controls explain the scope. A disconnected
four-position graph can trap a configuration at TV distance 5/6 from its
full count sector forever. Incorrect conserved counts cannot be repaired by
mixing. Correct multinomial count marginals correlated with a two-valued
geometry can leave joint distance 1/2 from independent geometry and product
colors. None violates the reviewed hypotheses. These are countercontrols,
not findings against the supplied theorem.

## Author-source comparison and verification limits

The complete author code uses the same form and clock conventions. It keeps
the conditional coupling and count-mixture computations exact, while its
graph eigenvalues, five-state density example and schedule evaluations are
floating-point controls. The note expressly treats numerical spectral checks
as finite evidence, not a proof of uniformity. No prose/code discrepancy was
found.

`compare_author.py` authenticates the three source bindings, verifies that
every group file equals its combined result, and independently recounts the
771 connected labeled graphs and 7,521 endpoint reference words. It does
not rerun all author eigenvalue computations. Separate character inversion
of the biased five-cycle reproduces the four author density-control rows;
80-digit arithmetic reproduces all six reported preparation times. The
author's randomly selected conditional-test values were read and bound but
not independently rerun; the independent exact tests above use different
functions and include a sharp conditional-coefficient witness.

All independent executions had empty stderr and no failed attempts. The
author log and empty stderr are retained at their authenticated identities;
authentication is not counted as independent proof. Earlier review/seal
artifacts and all primary files remain unchanged.

| Source | SHA-256 |
| --- | --- |
| Preparation note | `67f5423e29f93cdeaf2b16829354abd080a5205cd6531148cb2d16c187382e03` |
| Corrected routed dependency | `dc7bac51a1ffb273e11e9356713778aeb645acbfb280973f927c1f1de007d873` |
| Author preparation checker | `ceb61f213da0e675d27fafd094704590916d77f200f5682187d3c42b3b38c82b` |
| Combined author results | `4006d8eb9072391b9733885c5ac9d9595092f0a82c182dccb39b8f335eadcb2a` |

`FINAL_SOURCE_IDENTITIES.json` and `FINAL_SEAL.json` bind complete paths,
byte counts, all evidence and unchanged dependencies. The scripts can be
run in a fresh sibling evidence directory after copying their required input
manifests; do not overwrite this sealed packet. Actual commands and full
stdout/stderr are in the execution receipts and logs.

The conclusion retains fixed rates, fixed full-support p, fixed finite mode
and time lists, arbitrary frozen perfect-matching geometry, and the stated
formation count law. It establishes neither moving-geometry propagation,
a polynomial empty-start completion time, uniform geometric selection at
fixed birth rate, fine-key equilibration, a physical wave identification,
nor an operational quantum preparation.
