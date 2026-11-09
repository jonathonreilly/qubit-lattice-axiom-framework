# Check of the fixed-reference density forest and scalar-leg count

The corrected abstract density-forest lemma and its supporting scalar-leg
count are mathematically consistent under their explicit hypotheses. The
final consumer supplies an exact activation identity, uniform normalized
density jets, the required scalar-root summability, an exact full-reader
regrouping, and a convergent common-branch logarithmic ratio. No material
finding remains on the frozen versions below. This checks a conditional
finite-volume lemma; it does not verify its realization by the actual
two-step model or establish a physical gap.

Four issues were raised during this check and corrected by the coordinator:
two activation/orientation gaps, an overbroad constant-source sentence, and
an explicit nonempty-base condition. The initial defects and their
discriminating examples are retained below. I made no source edits.

## Frozen sources and read coverage

The source files are in the coordinator's worktree:

`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics/.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/`.

| Source | Coverage | Final SHA256 |
|---|---|---|
| `zero-shift-marked-density-forest.md` | Complete original and first corrected arguments; final nonempty-base change and source hash rechecked; 403 final lines | `d44adc900daf7ac665e502ac950230a8739b120d1a2be4940fd292ea9a09087f` |
| `scalar-leg-forest-count.md` | All 272 lines, including labeled coefficient derivations | `6df5e3c0f1185e5f56bae18e8dc81053eb33b005244009a70ccc3ed542377f6f` |

The initial consumer hash was
`5ac17f2d6a9c1a3ac85e58899f40468e5f34063fb89d8ff4f5a47cf270cc6791`.
The first corrected version, read in full, was
`cdfc4ee9fe90594ab68943ccf7750995bc722b16ae64eaaaa50f3f06e0f8ae4a`.
The final change explicitly requires nonempty bases and controls external
empty-support factors. These content hashes, rather than an uncommitted
branch description, identify the reviewed mathematics.

The historical source check is recorded separately in
[density-forest-source-check.md](density-forest-source-check.md), SHA256
`fdc8beca9170eaf8e30f15ecbf369d6c817746caaac6ca55370fb7c6ef1fe18f`.
That report contains the applicable instruction/procedure snapshot and
primary forest-formula comparison; they were reused without rerunning a
literature search. The historical review's verdict was not proof of these
new arguments. The direct spectral-jet contract was derived during this
source check and shared with the coordinator before the new consumer was
received; this contribution is disclosed rather than presenting the
consumer check as blind to that estimate.

## Resolved findings

1. **Partial-cell activation could change the integral.** Initially J_v
   was an arbitrary scalar-coordinate set, while F9 prohibited bad-cell
   expansion on every cell meeting J_v. The unspecified remaining bodies
   in such a cell could then disappear when inactive coordinates were
   marginalized. Take one cell with two independent standard Gaussian
   coordinates, no compact label, and
   `W=w 1_(|x1|<=p)`. If `q=Pr(|X|<=p)` with 0<q<1, the selected-W term
   of the original chart integral is `w q^2`, while activating only x1
   gives `w q`. This is an exact counterexample to that implementation
   of the original activation text. The final source makes both J_v and
   H_g unions of full owner cells, retains all their bodies, activates
   all coordinates there, and charges `K_g^(k|cells|)` in F5. These
   changes repair the identity and its Gaussian normalization bound.

2. **Asymmetric reverse paths were not compatible with the row-only
   rooted bound.** Initially F2 allowed Gamma_ij and Gamma_ji to differ.
   Re-rooting a fixed unoriented tree reverses some edge directions; its
   old path cost then need not be bounded by the new directed e_ij.
   A row bound on a nonsymmetric weighted envelope is not the same
   estimate for its transpose. Counting both orientations of the final
   distinguished edge alone does not repair the internal rooted trees.
   The final source chooses one path cell set for each unordered scalar
   pair. Thus e_ij=e_ji, every re-rooting preserves the assigned reader,
   and the auxiliary proof's reversal hypothesis is met.

3. **A field-independent nonlinear source normalization can have mixed
   derivatives.** `V_vac(zeta)=zeta_1 zeta_2` has a nonzero mixed second
   derivative despite its field independence. The final source limits
   the zero higher-cumulant statement to linear coupling to constant
   observables and retains derivatives of other V_vac in each individual
   physical logarithm. A common nonzero exp(V_vac) still cancels exactly
   in the ratio, including when it is nonlinear.

4. **The anchored norm must exclude unpriced empty bases.** If an
   empty-base factor W=-1 were permitted, it would contribute nothing
   to the rooted primitive norm while making Z_a zero. The final
   source explicitly requires every retained primitive base to be
   nonempty, including field-free vertices. An external empty-support
   factor must be the declared nonzero common exponential, or receive
   a priced nonempty syntactic reader. This also matches the explicit
   nonempty-support hypothesis in the scalar-leg note.

## Independent checks of the corrected density argument

**Activation and Gaussian marginal.** After the full-cell correction,
selected vertex and compact reader cells retain their actual bodies/caps.
All other cell bodies are expanded as one minus the true exterior.
Consequently F9 records an exact presence/absence constraint. Any two
primitives coupled by a shared coordinate, native compact incompatibility,
or that constraint have overlapping bases. The unique base-overlap
partition therefore localizes every admissibility condition. All inactive
coordinates marginalize to normalized C[I], not to an inverse principal
precision. A field-free compact primitive retains its nonempty support,
while the completely empty primitive family integrates to one.

**Accretivity and all-order density jets.** For the independent complex
pair variables, the absolute E row and column bounds are at most 2e.
Thus `Re C_I(s)>=p0-2e>=p0/2=c` and
`||C_I(s)||<=U+2e<=U+p0=G`. Its inverse has real part at least c/G^2.
This verifies the analytic domain needed for the finite forest identity
and domination over unbounded bad-cell domains, not just positivity on
the eventual real forest masks.

For a real mask, the inverse J has `a I<=J<=b I`. Expansion of the
complex-shifted quadratic form gives

```
|g_C(x+z)| <= (2pi c)^(-n/2)
             exp[-a|x|^2/4+(b^2/a+b/2)|z|^2].
```

With D0=b^2/a+b/2 and radii `sqrt(nu_i/(2D0))`, scalar Cauchy gives

```
nu_i! (2 exp(1)D0/nu_i)^(nu_i/2)
 <= (2 exp(1)D0)^(nu_i/2) sqrt(nu_i!).
```

This confirms F11–F12 at every order, with the determinant included and
with one factorial for each scalar rather than each component. Splitting
the remaining damping `exp(-a|x|^2/4)` into two equal factors is also
correct: on each distinct bad cell one factor supplies
`exp(-a p^2/8)`, and integration of the other factor costs
`sqrt(4/(a c))` per active coordinate. This is the K_g in F4–F5.
The final full-cell prices dominate all active coordinates, including
ones on which the original function happened to be constant. No tail
is charged to a compact field a second time. The argument takes no
derivative of a bounded measurable insertion or of a chart boundary.

**Normalized heat identity and exact raw gas.** The normalized-density
identity is `dot g=(1/2) sum dot C_ij partial_i partial_j g`.
The symmetric two-entry derivative for an unordered component pair
gives exactly F14, with no extra factor two. Repetition in independent
pair variables keeps Phi fixed. The clock argument proves the forest
identity first for each pair monomial; zero-power edges and the constant
monomial are covered by the empty-forest convention. Its extension to
the present integral is justified by the radius-two analytic domain.

At disconnected masks, cross entries of both P and masked E vanish,
so determinants and normalized densities factor, as do the fixed
functions and their internal admissibility. Grouping forest components
therefore gives the exact raw gas with base compatibility. No unmentioned
conditional Gaussian measure or normalization quotient is substituted.
The complete geometric support is the union of the bases and explicit
forest paths. The covariance is independent of every varied label, so
fixed internal density coefficients need no additional varied-label
reader. This reduction would not prove locality in a varying covariance
or varying coarse background.

## Scalar-leg coefficients and pinned remainder counting

I checked the auxiliary note's exact labeled coefficients, not only its
supersolution inequalities. Marking one vertex converts the unrooted
coefficient 1/n! into 1/(n-1)!. Splitting a rooted tree into r unordered
children of sizes n_1,...,n_r gives

```
(1/r!) product_l 1/(n_l-1)!.
```

The factors come respectively from removing child order, partitioning
the nonroot labels and choosing each child root. Allocating these children
to scalar coordinates contributes `r!/product_i r_i!`. Thus the exact
local occupancy series are H0 and H1 in T9–T10, with only one incoming
leg at each nonroot vertex. Its joining covariance edge pays its L^2
once; the dangling-leg factor itself carries no extra L.

Both proofs of H0<=exp(2y) and H1<=exp(4y), 0<=y<=1/2, are valid.
The main note's geometric comparison uses
`sqrt((j+1)!)/j!<=j+1`, which is true. The auxiliary note's independent
differential inequalities are also correct. With input norm at beta-delta,
the common rooted supersolution is `w_B exp((beta-delta)|S_B|)` at
output rate beta-2delta. For every scalar, its incoming-root sum is at
most h; hence each attachment argument is at most L^2 e h. The explicit
conditions `L^2 e h<=1/2` and `4k L^2 e h<=delta` pay all local
factorials and the linear |S_B| size cost. Neither condition is inferred
from the other without the appropriate rate restriction.

Cutting a distinguished unoriented edge gives two incoming-scalar rooted
trees. The exact coefficient is

```
(L^2/2) sum_(i,j) p_ij(x) A_i A_j,
```

because the ordered pair of rooted halves counts the two edge
orientations. For halves of sizes p and q the labeled coefficient is
`1/[2(p-1)!(q-1)!]`, confirming T16–T17. The final symmetric path
contract makes the two orientation weights equal. Bounding each A_i by
h and summing the ordered pinned path envelope gives at most
`(L^2/2) B h^2`, so the main note's larger `L^2 B h^2` is safe.
There is no missing number-of-edges factor: distinguishing the edge
already counts all such choices. Adding the base pin gives F19.

Repeated formal primitive types only enlarge this positive tree count;
they are never used to assert a repeated physical moment. Empty active
sets are singleton roots without incident Gaussian edges. Arbitrarily
large supports are allowed: all coordinate-count dependence is paid by
the explicit rate loss and |I_B|<=k|S_B|.

## Regrouping, charge and source coefficient

Each base-compatible raw family has a unique partition by overlap of
its full Y readers. Keeping its internal base compatibility gives an
exact gas with disjoint full readers. The third delta pays its rooted
overlap-tree sum. For the hard-core logarithm, a fixed Kruskal rule
partitions connected incompatibility graphs into spanning-tree intervals;
the alternating extra-edge sum has modulus at most one. Rooting at a
polymer through the marked cell and spending the fourth delta bounds
the absolute logarithm by r(h). Since delta=min(beta/8,1/8),
beta-4delta>=beta/2.

The uniform positive bounds apply when the primitive activities are
multiplied by a complex scalar of modulus at most one. The finite gas
and exponential of the convergent logarithm agree near zero, hence
through this disc and at its endpoint by uniform convergence. This
proves nonvanishing, rather than presupposing a branch of log Z.

At zero compact primitives, activation, masks, paths and every subsequent
list are exactly the chart list. Therefore all no-compact logarithmic
terms cancel coefficient by coefficient. Scaling only positive compact
primitive amplitudes by T=H/(2h_comp) leaves the counting budget at most
H, and every remaining positive majorant has at least one such factor.
Undoing it gives `2r(H)h_comp/H` as in F20. It is legitimate to carry
this charge through the entire construction in one rescaling. No
physical function, cutoff, covariance, normalizer or actual source is
changed by that counting argument.

Finally, F21 follows from uniform source holomorphy and the rooted norm:
fix a cell of one nonempty differentiated support; every contributing
Y contains all those supports and satisfies tau<=|Y|-1. Cauchy at a
radius strictly inside the source polydisc supplies r^(-q) for q distinct
labels. Repeated derivatives would require their ordinary multiindex
factorials. This conclusion does not use field analyticity of compact
functions. Common vacuum factors cancel in this ratio; separate physical
logarithms still retain their stated normalization derivatives.

The zero E, zero compact budget, field-free primitive, repeated formal
label, overlapping-reader, small-volume and arbitrary component-size cases
all follow from the same arguments. No division by e, B or h_comp is used
at a zero endpoint. The existence of H follows by taking H positive and
small in F16; its inequalities include r(H)<=delta/4 and provide strict
room for the two final tree sums.

## Scope and operations

This was one initial check followed by the affected-fix confirmation in
the same reviewer context. Four findings were resolved; none was skipped
or left pending on the final source hashes. The supporting scalar-leg
source needed no change. The actual-model composition, its orbit
covariance, source realization and separate chart cumulant argument are
outside this assigned gate and were not read here. The conditional lemma
does not grant them a result by citation.

No numerical job, source edit, prompt edit, lock, worktree operation, Git
mutation, PR action, public post or audit operation was performed. The
coordinator made all consumer fixes. Only this report and the separately
assigned historical-source report were written by this reviewer.
