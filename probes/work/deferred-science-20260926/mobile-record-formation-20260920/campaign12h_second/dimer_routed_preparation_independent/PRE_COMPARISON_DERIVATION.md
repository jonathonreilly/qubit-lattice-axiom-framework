# Independent preparation-bound reconstruction

The complete supplied note has SHA-256
`67f5423e29f93cdeaf2b16829354abd080a5205cd6531148cb2d16c187382e03`.
This reconstruction precedes access to any new author checker or its outputs.
The corrected routed note and earlier independent proof assessment are reused
at the identities in `PRE_COMPARISON_SOURCES.json`; no dynamic aggregate was
opened and no literature mixing theorem is imported.

## 1. Complete-transposition constants

Use the uniform probability measure on the K! arrangements of distinct labels.
For a real f, D_all=(1/2)sum_{i<j} E[(f after ij-f)^2], so the continuous-time
unit-rate complete-transposition generator has Dirichlet form D_all. This
one-half convention is essential.

Fix i. Conditional on sigma(i)=a, the other K-1 labels are uniform. For a,b,
swap i with the unique position carrying b. This is a bijection from the
a-conditioned space to the b-conditioned space. Jensen bounds the square
of the conditional-mean difference by the conditional expectation of the
squared swap increment. Summing all a,b gives

    Var(E[f|sigma(i)])
      <= (1/(2K)) E sum_{j!=i}(Delta_ij f)^2
       = D_cross,i/K.

The coefficient 1/K is exact for every f depending only on sigma(i). In
particular, for f=1_{sigma(i)=a}, Var=(K-1)/K^2 and D_cross=(K-1)/K. Thus
the numerator/denominator in this step cannot be changed without checking
the chosen form convention.

The K=2 bound Var<=D_all is valid (the sharp factor is 1/2). Assuming
Var<=2 D_all/(K-1) on K-1 positions and averaging the conditional-variance
decomposition over i gives

    Var(f) <= [2(K-2)/(K(K-1))+2/K^2]D_all
            = [2/K-2/(K^2(K-1))]D_all
            <= (2/K)D_all.

Internal swaps are counted K-2 times and crossing swaps twice. This proves
the displayed sufficient inequality without needing the sharp interchange
gap. Lifting a color configuration to distinct labels preserves both variance
and every transposition energy because each color arrangement has the same
fiber size product_a n_a!. Trivial one-configuration sectors have zero
variance and require no positive-dimensional spectral assertion. Complex
functions follow by applying the real inequality to real and imaginary parts
and using squared moduli in the form.

## 2. Path comparison and the torus bound

For a simple path x_0,...,x_l, the word of edges in forward order followed by
all but the last edge in reverse order swaps just the endpoint labels. Its
length is 2l-1; each physical edge occurs at most twice. Telescoping the f
increments, applying Cauchy--Schwarz and changing variables by each preceding
permutation preserves the uniform count-sector expectation. Hence

    E(Delta_xy f)^2 <= (2D-1) sum_{word steps} E(Delta_e f)^2.

There are K(K-1)/2 endpoint pairs, so even if every selected path uses an
edge twice, its total occurrence count is at most K(K-1). Multiplying the
sum by the Dirichlet factor 1/2 gives

    D_all <= (2D-1)K(K-1) D_H,
    Var <= 2(2D-1)(K-1) D_H.

No favorable congestion estimate or hidden normalization is used. A
symmetric rate r on every edge gives gap at least
r/[2(2D-1)(K-1)]. Restoring intermediate labels is important here: the
comparison is of endpoint transpositions, not a cyclic transport word.

For any perfect matching of the even cubic torus, contracting its pairs
maps a physical nearest-neighbor path to a walk on the connected simple
contracted graph. Removing matching edges and then loops cannot increase
length. The physical torus diameter is 3N/2, so D<=3N/2 for every matching.
Each contracted simple edge has at least one actual routing channel;
channel multiplicities can only increase the symmetric form.

The previously checked pointwise balance makes the sector measure uniform.
Reversing a nontrivial color swap negates its context drive, so each channel
has symmetric rate k0/2. Same-color swaps have zero color increment and
cause no exception to the form identity. Thus the actual symmetric form
dominates (k0/2)D_H and

    g_N = k0/[4(3N-1)(K-1)]

is a valid common lower bound. The floor (k0-|gamma|)/2 is not substituted
for this exact symmetric rate. The strict rate hypothesis in the note
ensures k0>0 and supplies an irreducible conservative color process.

## 3. Nonreversible density contraction and TV

Write the generator on observables as L, with adjoint L* in uniform-sector
L2. If h_t is a density, its evolution is L* h_t. The stationary mean is
one, and for r_t=h_t-1,

    d||r_t||_2^2/dt = 2<r_t,L*r_t>
                    = 2<r_t,(L+L*)r_t/2>
                    <= -2g_N ||r_t||_2^2.

The antisymmetric part drops out of this real quadratic identity. No
normality, reversible dynamics, diagonalization of L or sector condition
is required. For a point mass in a sector of m states, ||h_0-1||_2^2=m-1.
Consequently TV<=sqrt(m-1) exp(-g_N t)/2; arbitrary entrance laws obey the
same estimate by convexity. The crude count m<=14^K gives the specified
preparation time. Its time unit is the microscopic full-state exchange
clock, while the later fixed macroscopic wave observations are separated
by microscopic times Nt.

Direct substitution of (3) makes the logarithm of the loose TV upper bound
exactly log(epsilon). At fixed parameters its leading large-N term is
(3 log(14)/(2k0))N^7. The extra log(1/epsilon_N) term for epsilon_N=N^-4
is O(N^4 log N/k0), so the chosen schedule remains O(N^7/k0). No claim of
a sharp exponent or a lower bound is justified by this comparison.

## 4. Random completion and the exact probability-law target

Condition on the full history up to the almost-sure finite stopping time
tau_fill. This fixes the matching M, counts c and current color arrangement.
The strong Markov property and autonomy of the full-state color projection
apply the same uniform TV bound from that arrangement after the COMMON
deterministic elapsed time t_prep. Averaging gives distance at most epsilon
from the law obtained by keeping the actual (M,c) distribution and replacing
the color arrangement by the uniform c-sector.

The formation premise is stronger than merely having the right marginal
count distribution: the counts must be multinomial(K,p) independently of M.
It holds in the reused supplied construction and is expressly assumed here.
For every color array eta with counts c,

    MultinomialProb(c) / [K! / product_a c_a!]
       = product_a p_a^{c_a}.

Thus the comparison target is exactly Law(M at tau_fill) times pi_p. No
independence of arrangements at completion, geometric mixing, fine-key
mixing, conditioning on a fixed completion time, or estimate of tau_fill
is inserted. The elapsed preparation time is not a future state-dependent
stopping rule.

Useful excluded-premise controls are explicit. Disconnected position graphs
can trap componentwise color counts and fail to approach the full count
sector. Wrong birth-count weights do not become multinomial by conservative
mixing. Even correct multinomial count marginals are insufficient if those
counts are correlated with the geometry: a two-color, K=2 construction has
the correct unconditioned product color law but joint distance 1/2 from
independent geometry times product colors. These do not contradict the
note, which includes the needed hypotheses.

## 5. Path-law and mean-square transfer

On each N, evolve the close joint initial laws by the same M-dependent
Markov path kernel. Total variation cannot increase, even when the fixed
macroscopic observation horizon becomes Nt microscopically. The stationary
reference uses the same (possibly irregular, N-dependent) distribution of M
and independent pair colors pi_p, precisely the setting covered by the
previous matching-uniform theorem.

For a fourteen-indicator Fourier field,
||K^{-1/2}sum phi(u)(xi_u-p)|| <= sqrt(2K), since each ||xi_u-p||<=sqrt(2).
For any fixed list of modes/times, fixed p,gamma,k0 and the corresponding
finite matrices U, the nonnegative squared propagation residual is bounded
by C K with C independent of N and M. The expectation change under TV
distance epsilon_N is therefore at most C K epsilon_N (a factor two is
also a harmless conventionally loose bound). With K=N^3/2 and
epsilon_N=N^-4, this is C/(2N), which vanishes.

The stationary mean-square residual thus transfers; bounded distributional
tests and the stationary Gaussian initial-field limit transfer as well.
The proof does not rely on treating an unbounded Gaussian-limit test as
uniformly bounded at finite N. Merely epsilon_N->0 would not suffice for
this argument: a [0,K]-valued test can change expectation by K epsilon_N.
The stated choice supplies exactly the missing integrability control.

The result concerns fixed finite lists of modes/times and fixed full-support
p and rates. It does not supply a pathwise supremum theorem, variable-mode
or vanishing-density limit, sharp mixing, a polynomial empty-start filling
time, uniform geometric selection at a fixed birth rate, or microscopic
quantum realization. At gamma=0 the imported propagation limit is the
identity, as already qualified in the corrected routed note.

## Provisional conclusion

All displayed constants and law-transfer steps reconstruct under the exact
stated hypotheses. No mathematical correction is provisionally required.
Finite control output and source identities will be sealed with this
derivation before comparison to any forthcoming author checker. Those
finite controls test normalization and hypotheses; the arguments above,
not a list of successful small matrices, establish the all-volume bound.
