# Preflight Witnesses

These exact exploratory values were disclosed before preregistration and must
be rederived independently by the target runners.

On the literal D1 L24 fixture at crossings `{0,2,4}`, let `C=A^{-1}` and
`H=C+C*`.  The raw positive-kernel composition residual is

`[H_42 H_20-H_40]_(0,0)
=1860588125181794168951/3216875861507134647600 != 0`.

Inserting the intermediate normalization does not repair it:

`[H_42 H_22^(-1) H_20-H_40]_(0,0)
=-2234183456333136028/714473894240060471595 != 0`,

and the full residual reportedly has rank `32`.  The corresponding predictor
residual witness is

`-67663841820374976848/41707488576114153187201 != 0`.

Thus entrywise-nonnegative cyclic `H` words are a control, not a Markov or
causal insertion.  The primary and independent implementations must reproduce
or falsify these values before using this candidate.

A second candidate under hostile design is the following exact mathematical
control.  It is **not** an action-selected physical insertion at registration.
Write

`V_9=span{I,L_0,...,L_7}`,  `L_alpha(X)=F_alpha X F_alpha`,

so that

`L_alpha o L_beta=delta_(alpha,beta)L_alpha`,
`Delta=sum_alpha L_alpha`, and `(I-Delta)o L_alpha=0`.

On `Fock=Lambda(C^32)`, define the vacuum-reduced exterior lift

`Gamma_+(K)=Gamma(K)-P_vac=direct_sum_(n=1)^32 wedge^n K`

and on the doubled space

`P_hat_alpha=conjugate(Gamma_+(F_alpha)) tensor Gamma_+(F_alpha)`.

The preregistered linear candidate is

`iota(a I + sum_alpha b_alpha L_alpha)
 = a 1 + sum_alpha b_alpha P_hat_alpha`.

The tensor order is load-bearing: it follows the frozen column-vectorization
law `vec(K X K*)=(conjugate(K) tensor K)vec(X)`.  Reversing the two doubled
legs is a swap-conjugate representation with unchanged ranks, but is not
literally the frozen Liouville convention.

It must independently establish `iota(I)=1`, pairwise orthogonal idempotence
of the eight `P_hat_alpha`, and `iota(Delta)!=1`.  On bidegree `(1,1)` it
must reduce exactly to `conjugate(F_alpha) tensor F_alpha`, with branch rank
`16`, dephasing rank `128`, and identity rank `1024`.  On the full doubled
exterior space each selective branch has rank `(2^4-1)^2=225`.

Vacuum subtraction is load-bearing: the naive `Gamma(F_alpha)` candidates
share `P_vac` and therefore have nonzero products for distinct labels.  The
subtraction is uniquely forced only *conditional on* exterior naturality,
exact composition, vacuum-annihilating selective branches, and simultaneous
eight-label symmetry.  None of those bridge requirements is currently a
derived action law.  The claimed normal symbol is

`r_F(bar_eta,eta)=exp(bar_eta(F-I)eta)-exp(-bar_eta eta)`,

with doubled branch symbol, in the same frozen leg order,

`r_(conjugate(F_alpha))(bar_eta-,eta-)
 r_(F_alpha)(bar_eta+,eta+)`.

This is an `O_9` operation candidate, not a unital `E_8` effect insertion:
`sum_alpha P_hat_alpha` omits the vacuum and mixed-label exterior sectors.
Promoting it to the primary effect cylinder, or assigning those omitted
sectors to labels, is a registered failure unless the assignment is derived
from the action without a filling, state, boundary, or label choice.

For any conditional evaluation after a primary T2--T4 pass, use the literal
three-boundary Schur kernels `Q_024 in M_96` and `Q_02 in M_64`, constructed
both directly and as inverse covariance principal blocks.  The pilots report
full ranks `96`, `64`, and `32` for the crossing-4 pivot, the nested Schur
identity, and non-Hermitian-defect ranks `48` and `32`.  These facts are
disclosed only and must be independently recomputed.

The normalized doubled cyclic functional is frozen as

`Omega_B=omega_(Q_B) tensor conjugate(omega_(Q_B))`,

with no depth-dependent renormalization.  Its determinant expansion for a
selective word is preregistered as

`a_B(alpha_1,...,alpha_n)=det(Q_B)^(-1)
 sum_(epsilon in {0,1}^n) (-1)^(n-|epsilon|)
 det[Q_B + direct_sum_j(I-epsilon_j F_(alpha_j))]`,

and `w_B=a_B conjugate(a_B)>=0`.  This formula is a candidate calculation,
not evidence of event normalization, causal gluing, or physical selection.
If reached, it must pass in order: identity gluing from `024` to `02`; the
one-shot `1/8` law; an explicit identity/dephasing distinction; all 512 exact
weights without post-normalization; every latest-outcome prefix equality;
the exact triple-port selector; and the declared commutant/intertwiner gauge
test.  Failure of any earlier gate stops every later physical claim.
