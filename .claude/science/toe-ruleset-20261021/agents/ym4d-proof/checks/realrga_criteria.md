# REALRGA finite diagnostic criteria — registered before implementation

These exact rational checks test normalization and the four-source
interface, not a gauge-model bound or the RG induction. No fitted constants
or floating point tolerances are used. Existing sources have already been
read. The following expectations are derived before writing the checker.

1. For X Bernoulli(p), p=1/3, the first four cumulants are
   p, p(1-p), p(1-p)(1-2p), p(1-p)(1-6p(1-p)). A formal distinct-source
   logarithm through four labels must equal these values at every nonempty
   subset (15 checks). The first real-tilt response is 2/9; treating the
   reference as undifferentiated gives 1/3 and must disagree.
2. Let H be fair and X given H be Bernoulli(1/4) or Bernoulli(3/4).
   The conditional-log/outer-exponential/outer-log construction through
   four distinct sources must equal the direct Bernoulli(1/2) logarithm
   at all 15 nonempty subsets. Omitting the conditional triple jets must
   change the degree-four result. Expected direct fourth cumulant: -1/8.
3. Three hard-core polymers with incompatibility path 1--2--3 and
   activities z*(1/8, -1/9, 1/10) have exact partition function
   1+z*(1/8-1/9+1/10)+z^2/80. Through degree four in z, its formal real
   log coefficients must equal the connected incompatibility-graph sum
   including repeated polymer labels. Omitting repeats must disagree.

Run sequentially, no pools, `nice -n 10`, Python -B and BLAS/OpenMP thread
variables all 1. Before and during checks require RSS <1 GB, 1-minute
load <8, and system free memory >=30%; do not use RLIMIT_AS. Acquire a
lane lock. If nice, memory measurement or a resource gate is blocked,
report NOT RUN rather than bypass it. Save stdout, stderr and result.
An assertion mismatch is FAIL; an execution/resource refusal is NOT RUN.
