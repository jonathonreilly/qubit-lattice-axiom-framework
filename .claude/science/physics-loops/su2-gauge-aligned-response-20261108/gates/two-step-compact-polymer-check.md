# Independent check of the two-step compact insertion decomposition

2026-11-09. Research signal **advance** on the corrected frozen source.
One shell-width quantifier defect was found and repaired by the author; its
affected-source confirmation is below. No unresolved material mathematical
defect was found in the exact partition, regional bound, simultaneous
resummation or overlap grouping. This is a research gate, not an audit verdict,
retained status, marked-response theorem or connected-log estimate.

## Source identity, correction and scope

The complete initial 357-line draft `parts/two-step-compact-polymer-decomposition.md`
was read in the pack
`.claude/science/physics-loops/su2-gauge-aligned-response-20261108` under
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics`.
Initial SHA-256:
`0bd86de4574e84445605cf78e07e4429567a6a6770924fdfce19cac64bbc15fc`.
Final checked SHA-256:
`1e3772f4781fa082de6d117e8f61adef616deb00fe293bbd01e07f030107d54e`
(359 lines).

The author changed the two K-choice paragraphs at lines 62–77. The corrected
source prescribes the least positive K satisfying (P3), and limits the
any-admissible-K scope to the identities and bounds through (P19). The changed
window was reread. Reversing exactly those two edits reconstructs the original
hash, verifying that no other source byte changed.

| Severity | Finding and disposition |
|---|---|
| Medium, resolved | The original text allowed any deterministic K satisfying (P3), but the (P20) absorption used K=O(log u). An arbitrarily fast-growing admissible K does not satisfy that inference. The least-K prescription and revised scope now discharge the quantifier. |
| Critical / high | None found. In particular, the simultaneous resummation was reconstructed as an actual integral-domain bijection, not accepted from historical labels. |
| Other unresolved material findings | None. All selected dummy regions are excluded from the annular predicate, and the global chart expectation is never factorized. |

| Mathematical input | SHA-256 |
|---|---|
| arbitrary-boundary-interior-moments.md | c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11 |
| compact-energy-coercivity.md | 7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa |
| local-conditional-tail.md | cf47acdfe0deea09fe49f7b08d90d45a3aac0df3251062ba4f67f566e639072d |
| rough-component-bound.md | 1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44 |
| compact-forest-exchange.md | b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2 |

These exact energy, full-factor conditional, reader-radius and forest inputs
were already read and checked in this session; matching coverage is reused.
For architectural provenance, the historical
`.claude/science/toe-ruleset-20261021/agents/ym4d-proof/HOLOMORPHIC_COMPACT_RETURN_ASTRA.md`
was read at commit `89faef229ff6e6bde42baad15ed8270c2f4087d8`, lines 1–397,
including HC10–HC21 and their setup. Its source labels and claims are not
accepted as proof. No historical holomorphic, critical-point, transported-chart
or Gaussian-consumer estimate is imported into this check.

The inherited source base remains `55fd670ff8995427b24617b2273bd3f78b7559d9`.
The coordinator refreshed main from `1e0d3b58dcda7f83152b0bb51729260247454d65`
to `bf92a1d763030836ed55631d5d7a7ef3b288f284`; a read-only path diff showed
no change to the applicable AGENTS/workflow/skills, pack, or main SU(2) source
note. The mathematical hashes above remain unchanged. No audit-status
conclusion is inferred from that refresh.

Applicable instructions and the inherited supervising model/effort are
unchanged. No model substitution, numerical job, source edit, Git/network
mutation, formal verification or status operation was performed by this
reviewer. Only this report was written, and earlier gate reports remain
immutable. No editable prompt changed.

## 1. Parameters and the exact first-shell partition

The good-cell implication has the correct constants. Since
`theta^2 <= (pi^2/2)b_e` and `q=rho^2/(2 pi^2)`, `T_X<q` implies every owned
principal angle is strictly less than rho/2 and hence lies in the Cartesian
chart. The converse is unnecessary and false in general. The cap used in the
denominator also lies inside the chart once `(pi/2)d0<p(u)`, because its
principal angle is at most `(pi/2)d0/sqrt(u)<rho`. This justifies using its
full Haar mass within the actual regional chart integral.

For each actual bad-cell component A in the distance-d_conn graph, all cells
within distance 2K but outside A are good: another bad cell there would be
connected directly to A. If each of the K shell tests failed, positivity of
T and the disjoint inclusion of I_j and S_j in I_(j+1) would give
`T_(I_K)>(1+alpha)^K q|A|`. Compactness instead gives
`T_(I_K)<=2M(4K+1)^4|A|`, contradicting (P3). The intermediate layer
`N_(2j+1)(A)\I_j` is simply an additional nonnegative contribution; its
omission from this lower growth estimate is legitimate.

Thus each component has exactly one first successful j, with equality in a
shell test assigned to success and equality `T_X=q` assigned to bad. Conversely,
a nonzero history selector makes the bad-cell set precisely the union of its
cores. Their separation and connectedness then identify the actual components,
and the failure factors identify the unique first j of each. This proves the
pointwise partition, including the all-good empty history. Empty shells and
neighborhoods saturating a finite torus preserve the argument.

For the repaired K quantifier, put `t=log(1/q)`. A trial
`K_trial=ceil[C_alpha(1+t)]` with `C_alpha log(1+alpha)>2` makes the left side
of (P3) grow exponentially in t and the right side grow only as t^4. It is
therefore admissible for sufficiently small q. The prescribed least K is at
most this trial value, proving the required O(1+log(1/q)) upper bound. Without
that prescription, choices such as K=ceil(exp(u)) satisfy (P3) eventually but
do not justify the claimed logarithmic growth or the volume-cost absorption
for an admissible C>1. The source correction resolves this issue narrowly.

## 2. Regional ratio and one retained energy charge

The selected regional factor contains each entire plaquette or normalized
kernel whose full syntactic retained readers meet J_R. Its exterior readers
are exactly contained in the one-cell collar S. The given global-to-local
energy estimate and radial H comparison consequently apply to the actual
two-layer conditional, including hidden outputs and conditionally constant
normalizers. There is no new intermediate Wilson law.

The chart denominator cap gives its common `H(kappa u)^k` factor, n-coordinate
Haar power `u^(-3n/2)`, and the cost `(K_E+K_r)u T_S` stated in (P9).
The numerator's local lower energy bound contributes another `K_E u T_S`
cost after division. The relevant effective energy is therefore exactly
`c_E T_R-C_shell T_S`, with `C_shell=2K_E+K_r`.

On the same selector, `T_S<=alpha T_I`, `T_I<=T_R`, and `T_I>=q|A|`.
Splitting before substituting the fixed core lower bound gives

```
c_E T_R-C_shell T_S
 >= (c_E/2)T_R+(c_E/2)T_I-C_shell alpha T_I
 >= (c_E/2)T_R+(c_E/4)T_I
 >= (c_E/2)T_R+(c_E/4)q|A|.
```

The second inequality uses the fixed choice of alpha. This preserves half
the T_R damping for the reference Haar integral and charges the core only
once. In particular it does not attempt to pay an arbitrary larger shell
sum from q|A| after discarding T_I.

Integrating the remaining product reference Haar factors cancels exactly
`u^(-3n/2)` as well as `H(kappa u)^k`. The only remaining dimensional cost
is C^|R| with a fixed C independent of K,u and the volume. The numerator
difference is the single compact regional chart-complement integral with
the same selector; it is nonnegative and at most N^c. Hence the same bound
holds for B^a and D without a factor two. On the admitted good-shell exterior,
I_R is a strictly positive integral over an open chart. The zero extension
off that exterior does not alter any identity where the shell predicate
is present.

## 3. Source-free factorization and both history identities

For separated cores, the distance between active regions is at least
`(4K+5)-2(2K-1)=7`. No original factor with owner-reader diameter at most one
can touch two of them. Allocating a touching factor to its unique active
region therefore gives an exact product of the regional factors and one
outside factor. The entire input-dependent kernel normalizer follows its
kernel in this allocation. The outside factor is not discarded from the
global integral.

Every coefficient B or D reads only its exterior shell. These shells are
outside every active region, and the history's O_h-good event makes them
good. Integrating the dummy chart variables in the active regions against
the single global chart density gives precisely the product of I_R factors.
Their cancellation with the coefficient denominators reconstructs the compact
history integrals in the first line of (P13), and the regional chart history
integrals in the second line. No product probability law for the exteriors
or for the global chart measure is introduced.

For the empty history, the remaining predicate is good on the whole torus.
Its chart expectation is Z_good/Z_a, which need not equal one because the
chart contains q-bad cells. This vacuum contribution is correctly retained
until the next resummation.

## 4. Independent integral-bijection proof of (P15)

I checked (P15) by restoring actual selected-region variables, which gives a
different way to expose its domain bookkeeping. Fix a selected family s and
start with its proposed right side
`<1_good(H_s) product_s D>_a`. Every D is independent of the dummy variables
in every selected region, and H_s excludes all of those regions. Integrate
those dummy chart variables first. The factors I_R cancel the denominators
in D. Expand each remaining N^out as its actual integral over
`SU(2)^J_R \ C_R` with its selector. The result is one integral of the full
density w over configurations with:

- each selected region in its compact regional chart complement and carrying
  its actual selector ell_(A,j);
- all coordinates outside the selected regions in the chart;
- good(H_s) imposed outside all selected regions.

The selected cores are actual bad-cell components in every such configuration.
Their selectors make their own cores bad and their surrounding active-region
cells good. H_s makes all remaining cells within distance d_conn of a selected
core good. A different selected region can meet that annulus, but its bad core
cannot, by core separation; its own selector makes the intersecting noncore
cells good. Thus the same conclusion holds there as well.

The unique full first-shell history of this actual configuration consequently
contains the selected pairs, including their selected j values. Every additional
core is at distance greater than d_conn from the selected cores. Its full
N_(2K) first-shell test is outside the selected active regions, and its active
region is in the already-chart exterior. The remaining components therefore
supply precisely the unselected chart-history labels on the left side.

Conversely, restore all regional numerator integrals in any left-side term.
Selected regions are compact chart complements, unselected regions are chart
integrals, and O_h-good implies its exterior is chart. Any point of H_s is
either in O_h and good, or in an unselected active region outside its core
and good by that selector; an unselected bad core in H_s would violate the
core separation. This reconstructs exactly the right-side domain above.
The domains are partitioned once by the unique actual history. This proves
the equality as a finite sum/integral bijection, without assuming independence
under the chart law.

This derivation also tests the critical subtraction of *all* selected R.
If an annular good predicate were left on another selected dummy region,
its chart integral would be capped and would no longer cancel its I_R
denominator. Such a cap is not automatically one: a chart cell can have
T_X>=q on a positive-measure open subset. The current definition removes
that predicate from every selected dummy region. After those variables are
replaced by their actual numerator variables, the necessary noncore goodness
is already supplied by their selectors. Thus neither a missing cap nor an
extra cap remains. For s empty, the same bijection is the second history
identity and yields the resummed value one.

## 5. Complete-reader overlap grouping and the final bound

For every core, R, its shell and all its original factor readers lie in
`Gamma_A=N_(d_conn+2)(A)`; the annular absence predicate lies there too.
The actual exterior arguments of D may be fewer, but the larger labeled
reader is retained consistently. The shell of each selected core belongs
to H_g, since its radius is at most 2K and it cannot meet another selected
active region. Defining Theta to be zero off good(H_g) therefore avoids
evaluating an unadmitted regional ratio.

Every selected family has a unique decomposition into connected components
of the Gamma-overlap graph. Conversely, pairwise Gamma-disjoint polymer
labels reconstruct a separated selected family: any forbidden cross-core
distance or cross-group annular/active intersection would create Gamma
overlap. Across groups no selected region removes part of another group's
annulus, so H_s is exactly the disjoint union of their H_g. Consequently the
products of predicates and D factors match the resummed expression exactly.
Keeping the entire core/index list in each label prevents multiplicity loss
when different lists have the same union support.

This proves (P17). Its empty family is the fully resummed chart contribution,
not the single empty-history term in (P13). A field-independent insertion
still has its nonempty assigned Gamma reader and is not omitted as a vacuum.
The expectation of a product under the coupled chart law is never replaced
by a product of expectations.

The volume bounds follow from radius d_conn=4K+4 and d_conn+2: their ball
counts are respectively `(8K+9)^4` and `(8K+13)^4`, times the disjoint core
count n_g. Multiplying the regional estimates gives (P18). With the corrected
least-K prescription, `V_K=O(log^4 u)` while
`u q=c_q log(2+u)^(2a)`. The chosen a>5/2 therefore makes the latter dominate
the fixed `(log C)V_K` cost and proves (P20) after a volume-independent
increase of u0. No summation over polymer labels or covariance contraction
is performed in this last step.

The supported result is this source-free real compact decomposition into
bounded insertions inside the common actual chart expectation. Marked source
or terminal derivatives, a scalar activity factorization, a Gaussian forest
consumer, a connected logarithm norm, spatial response decay and further
blocking are outside the checked statement. No separate next consumer proof
is confirmed by this report. Reopen the affected check if the frozen source,
K rule, chart, factor allocation, selector domain or complete-reader convention
changes.
