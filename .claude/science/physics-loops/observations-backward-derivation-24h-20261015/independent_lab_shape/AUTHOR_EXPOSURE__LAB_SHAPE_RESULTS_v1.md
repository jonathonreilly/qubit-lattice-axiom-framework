# Shape diagnostics: output and exact pair obstruction

The frozen root computation completed with 158 mathematical and solver checks
passing. These checks include the primal and dual residuals of nine linear
programs; their count is not an evidence count for gravity. The complete output
is `LAB_SHAPE_CONTROLS_v1.json`, with every one of the 95 printed runs retained
in each channel. The data were already exposed and processed. The independent
focused check is pending at this writing.

| Channel | Central monotone | Central decreasing convex | Interval-order relaxation |
| --- | ---: | ---: | ---: |
| 120-fold | 1.935401975 | 1.982247502 | 1.878539071 |
| 18-fold | 2.258426966 | 2.635614874 | 2.258426966 |
| 54-fold | 2.237623762 | 2.280778856 | 2.237623762 |

Each entry is the smallest multiplier on printed marginal **torque** errors
that admits a nonnegative curve in the indicated relaxation. The interval
calculation holds the printed separation intervals at one quoted marginal
error. These are hypothetical boxes, with no assigned joint coverage.
Neither a number near two nor a number above two is a statistical significance.
Run correlations, phase estimation and model-dependent corrections remain
unresolved. In particular, this is not a scalar-theory exclusion.

## Exact certificate for the monotone subproblem

For a finite transitive preorder `i <=_P j` meaning that i must precede j in
separation, require `t_i >= t_j`. Include reflexive pairs. At a fixed k define
`L_i=max(0,y_i-k sigma_i)` and `U_i=y_i+k sigma_i`.

A feasible nonnegative ordered assignment exists exactly when `U_i>=0` and
`L_j<=U_i` for every ordered pair. Necessity follows from
`L_j<=t_j<=t_i<=U_i`. For sufficiency choose

`t_i=max_{j: i<=_P j} L_j`.

Transitivity makes these assignments ordered. The pair conditions place them
below U_i, and reflexivity places them above L_i. Equal-separation equivalence
classes consequently get equal values.

Therefore, for positive sigma, the optimal multiplier is exactly

`max(0, max_i[-y_i/sigma_i], max_{i<=_P j}[(y_j-y_i)/(sigma_i+sigma_j)])`.

The frozen runner's pair-obstruction calculation agrees with its independent
linear-program formulation for all six monotone cases. Disjoint ordered
separation intervals define a transitive relation, so the same proof applies
to that relaxation. The existence of an ordered latent vector does not prove
there is a compatible placement of all uncertain separations on a continuous
physical curve.

The convex program has the additional correctly oriented inequality

`-dr*t_i + (dl+dr)*t_(i+1) - dl*t_(i+2) <= 0`

for consecutive positive gaps dl and dr. Dividing by dl+dr preserves its sign.
The stored dual vectors, slacks, reduced costs and objective gaps provide
floating checks of optimality, not certified interval arithmetic.

## What this removes, and what survives

A common positive multiplicative gain and a common separation zero are absent
from these necessary shape inequalities. This retires their numerical values
only for this particular conditional diagnostic. It does not determine G,
scalar normalization, mass, the field potential or a physical environment.

The positive-Laplace representation requires a suitable matched pattern and
fixed linear static response. The measured foil metrology is unequal and
includes differing pattern centers, so exact matching has not been established.
The source also reports epoxy, finite-thickness and transfer corrections.
The successful cone calculation cannot be promoted to a fully applicable
apparatus prediction without those inputs and their error propagation.

A positive mixture containing a Newtonian contribution also has support down
to q=0. Its overall decay slope does not provide a lower support bound for a
separate Yukawa mass. Attributing the whole curve's slope to a massive scalar
would supply an unproved component separation. No such inference is made here.

