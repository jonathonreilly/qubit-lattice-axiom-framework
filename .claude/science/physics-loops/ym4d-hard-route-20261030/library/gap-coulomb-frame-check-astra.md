# Repo search

Writer: GPT-6-astra, xhigh, at checkout `bf8a0f879840edf20567aee65b494abd9a9e10ea`.
Research check of row 1042, not an audit; no status or mass gap claimed.
Does not cover row 1044 (not read), a new attack, or computer-assisted proof.
The ARGUED positive-COUL and smooth-field claims, GUIDE logs and original
literature citations are not verified or promoted here.

The target-specific prior digest does not exist at this checkout. The supplied
2026-11-08 repo digest concerns earlier analytic and RG targets; the relevant
near matches are checked below. The lead reports a
search of main and PRs 10114, 10133, 10134, 10141. This report does not treat
that report as a proof or a fresh exhaustive search. The exact-target search
of `open-registry.md` found no other owner or completed check.

The near hits actually checked are PR 10141 at
`a2f6a430e251aa47bc3eb4f67a1dca2a88530116`'s
`research/ym4d/library/out-pi.md:352–381` (fetched PR head), about boundary
admission for a compressed classical Hessian, and main at
`8b11ae2bb95e641494fe75ed83d108ee712fa3a9`'s
`docs/MASSIVE_WILSON_LOOP_CURVATURE_NONCOMPACT_COVARIANCE_AND_COMPACT_DEFECT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-14.md:120–145`,
about a specified noncompact Maxwell measure and its score identity.
Neither supplies the compact pinned-cell frame response. Closest are the
existing same-lane GR and CUBE-Z of `gap-boundary-q.md`, and CG's tree
precursor, CUBE-H, LEAD, and LIP-TREE in `gap-collapse-frame.md`, with
the precise remainders and scope corrections in check 1041. Those inputs
are reused, not claimed as new findings here.

The index was consulted before the external source: `sa-index/chunk-07.md`
and neighbours at outline 7178–7202 describe axial and constrained Landau
gauges; these are different from absolute maximal trace. The corresponding
Landau obligations remain named in `obligations.md`. The CA-4.12–4.19
index, chunk 01, points to CA-I 43690–43865: the account proves the
plaquette-swap product estimate and axial box gauge used by LIP-TREE.
Those source lines were read. LIP-C reuses this established argument;
it is not a new curvature-to-potential method. Credit Sussman and Alpoge,
with Claude and Codex as authors of their text, and Balaban for that method.
Chunk 02 and outline 2197–2243 also supply the positive, factorially
decaying Wilson character coefficients used by CUBE-Z; its normalization
is `u_d=exp(beta)c_l`, `d=2l+1`. This is an existing cited input.
This was a targeted source check, not a claim of absence throughout CA-I.

## Checkpoint

Sources: pinned checkout above; Sussman–Alpoge outline and CA-I at
`31a47c543775`, downloaded once into
`/tmp/sa-gap-coulomb-frame-check-astra.6fHPVS/`. Credit Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text, for any use.
The reviewed source's SHA-256 is
`f1f70553fb71bd61cacb365ee91ad97e9e2a7e7d5bd4e63db9f926488d3ff400`.

Plan: (1) read rules, ownership and indexed sources; (2) do the three required
hand tests; (3) check CG, UNIQ, LIP-C; (4) check cube and LEAD-C;
(5) check HIER, EXIST and selection; (6) check LOOP, SQ, CURL-P and U(1);
(7) state verdicts and implications. These steps are complete.

Completed: all requested hand tests and theorem checks. Corrections are
written below; the source file is unchanged. No numerical run was used.
The source's positive COUL witness and smooth-field heuristic remain
ARGUED; no typical-pin, full (O2), or wall estimate was supplied.
Next decision belongs to the lead: apply these precise corrections to
row 1042 before using its conclusions. No further attack is launched.

## First hand tests

Line numbers below refer to `gap-coulomb-frame.md` at the pinned commit.

1. **Even split.** Write `h=exp(phi u)`, `0<phi<pi`, and
   `q=exp(phi u/4)`. The rooted gauges in L133 give
   `H_a=H_1=q`, `H_b=q^{-1}` and
   `H_2=q h^{-1}q^2=q^{-1}`. Their ordered product is `q^4=h`.
   To verify maximality without assuming feasibility of changing one factor,
   let `alpha_i` be the four class angles. The triangle inequality gives
   `sum alpha_i>=phi`. Choose `0<=a_i<=alpha_i` with `sum a_i=phi`.
   Then `sum cos alpha_i<=sum cos a_i<=4 cos(phi/4)` by the two pair
   averaging inequalities in L138–139. The displayed gauge attains the bound.
   Equality forces all four angles to equal `phi/4`; equality in the sphere
   triangle inequality forces the common shortest geodesic when `phi<pi`.
   Thus the split and rooted uniqueness hold. At `phi=pi` the geodesic axis
   is free; at `phi=0` all four links equal one. L137's instruction to
   “lower one angle” needs this upper-bound argument, not a feasible gauge move.

2. **One exact CUBE-COUL value.** Take `phi=2pi/3`, `u=i`, `a=j`,
   `lambda_100=1`, and the other three lambda values zero. In Coulomb gauge
   only `H_a` moves under the GR curve. Direct multiplication gives
   `t(h(e))=Re(exp(-e j) q exp(e j) q^3)=-cos(2e)/2`.
   Hence `t'(0)=0`, `t''(0)=2`, and
   `H_c=-2[b_0+kappa(-1/2)]`. L156 gives the same value since
   `c=1/2`, `sin^2 gamma=1`, `theta_1=1`, `theta_2=0`.
   This checks the sign and normalization without a finite difference.

3. **SQ versus `2xy`.** For `q(x,y)=2xy`, the y-axis has zero quadratic
   form, so no `m>0` is available. Setting `x=1` and increasing `y`
   refutes every upper bound `C x^2`. With the stated strict hypothesis,
   `q_m(x,y)=2xy-m y^2=x^2/m-m(y-x/m)^2`, so the bound `x^2/m`
   is exact. SQ does not silently apply the strict lemma to the zero case.

## Frame and cube verdicts

**CG, L63–85: HOLDS AFTER CORRECTION of the covariance wording.**
The quaternion identity, returned curve, torus action and Hessian identity
in (a)–(c) hold. For (d), fix a reference colour `a` once. Choose at each
site a rotation carrying `n_x` to `a`; its ambiguity is a *left* rotation
fixing `a`. This proves every frame has the stated form. Covariance gives
`g(omega^k)=r g(omega) k^{-1}`, with each `r_x` fixing `a`, and the converse.
If the reference colour itself varies with the pin, the same equation must
instead say `Ad(r_x)a(omega)=a(omega^k)`.

The first false proof assertion is L83: `g_x k_x g_x^{-1}` need not be
constant in x. Correct text: “A stabilizer of H is a site family `c_x`
satisfying `c_x H_l=H_l c_y`; covariance requires `Ad(c_x)a=a`
at every site. In a tree gauge it is constant.” Constant centralizers
are only a subgroup in a general gauge. The site-sign freedom at reducible
pins was already identified in check 1041; reducibility alone does not
force every covariant frame to have `Dn=0`. For COUL in the unique small
neighbourhood, or on the noncentral cube, its common-colour construction
does have `Dn=0` at reducible pins: put the pin in a common-axis gauge,
use uniqueness to make the rooted maximizer commute with that axis,
then transform back. Restrict L99–100's claim to these proved cases.

**UNIQ, L104–115: HOLDS AFTER CORRECTION, with the same threshold.**
Compactness supplies an absolute maximizer. The energy comparison and
path estimate in L107–109 hold for every maximizer. The second derivative
bound in L111 is correct. L114 is the first invalid inference: its displayed
coefficient is exactly zero at `eps=eps_G`, so that bound alone is not
strictly negative. Retain the unused margin. For `N>=1`, `V>=2`,

`delta<=2 V sqrt(N) eps`,
`|K_l(t)-1| <= sqrt(N)eps+2pi delta <14 V sqrt(N)eps`

(using `pi<13/4`). Thus L113 gives
`phi'' <= -(1-28 d V^3 sqrt(N)eps) sum_l |v_x-v_y|^2`
and at the stated threshold this is at most `-sum_l |v_x-v_y|^2/8`.
Rooted connectedness makes it strict for a distinct maximizer. Compactness
and uniqueness give continuity: every convergent subsequence of maximizing
gauges has the unique maximizer of the limiting pin as its limit.
The displacement bound is in the chosen small representative, not an
arbitrary original gauge. The singleton graph (`N=0`) is trivial and
must be separated from the formula. “No copies” here means unique
absolute maximizer; arbitrary stationary points were not excluded.

**LIP-C, L236–265: HOLDS AFTER CORRECTION of its title.**
It minimizes `sum |H_l-1|^2`, not the colour-dependent defect itself.
At the hand-test cube pin, with a perpendicular colour, COUL's squared
defect sum is 4, whereas TREE's is `4 sin^2(2pi/3)=3`. Duplicating
this square in a third direction with identity joining links gives the
same counterexample on a 3D face box: each square reaches its trace
maximum and each joining link reaches trace one.
For the reversed-coordinate comb, direction 1 links are tree links;
direction 2 needs at most S1 swaps of type (1,2); direction 3 needs
at most S1 swaps of type (1,3) and S2 of type (2,3) at x1=0.
A fixed (1,2) or (1,3) plaquette occurs in at most S1 ladders.
A fixed (2,3) plaquette at x1=0 occurs for at most
`(S1+1) S2` direction-3 links. For positive side lengths these bounds
give exactly `C_F=(S1+S2)(S1+1)S2` after Cauchy–Schwarz and summation.
CG supplies the factor 4. Also `|U-1|^2=2(1-t)<=2(1-t^2)` for `t>=0`.
The stencil is the whole face and the stated constant grows with it.
NOLIP's separated fixed-radius local read hypothesis fails: a global
maximizer is used. No claim about the impossibility of a better constant
follows. Replace the title by “maximal trace gives a mean-square defect
bound.” No numerical or size-uniform result is being inferred.

**CUBE-C, L130–144: HOLDS AFTER CORRECTION of L137's proof sentence**
as in the first hand test. The bound, equality cases and rooted gauges
are unchanged. **Cube defect, L146–151: HOLDS.** Adjoint rotation is
through phi/2; hence each defect has size `2 sin(phi/4) sin(gamma)`.
The sine comparison holds precisely on the stated interval; the group
distance comparison holds on all `0<=phi<=pi`.

**CUBE-COUL, L153–177: HOLDS.** Direct expansion of the moved holonomy
in CUBE-H gives `t'=0`. Factor out `sin^2(gamma)` and put
`s=sin(phi/2)`, `c=cos(phi/2)`.
The two squared-norm coefficients are `2(1-c)`, and their cross
coefficient is `4c(1-c)`. Including the ordered quaternion cross products
reduces the diagonal coefficient to `-2(1-c)(1+2c)` and the off-diagonal
polynomial coefficient to `4c(1-c)`, as L170–173 state.
The eigenvalues of the bracket matrix are `1+c` and `1+3c`.
Strict negativity concerns the two theta differences; there remain the
two stated null lambda directions. For a covariant COUL colour on the
noncentral cube, gamma is zero or pi, so the whole form vanishes.
The off-axis negative form is not a covariant cube-frame construction.

**Cube Q, L179–201: HOLDS to the stated order and for the stated GR
extension.** At the trivial pin the scalar covariance matrix is
`C_0=beta xbar I-kappa ss^T`, where `s_l=[p_0:l]`.
Writing `lambda_l=lbar+(lambda_l-lbar)` gives L183's variance and
`Vv=(3theta_1^2+3theta_2^2-2theta_1theta_2)/4`.
Its constant mode gives `beta xbar-4kappa>=0`; shifting lambda by
`-lbar` minimizes the leading variance. The resulting coefficient is
exactly L187. For `b_0=beta/2`, `xbar<=1`, `kappa(1)>0` make it
strictly negative off the null modes. For `b_0=0`, only the leading
nonnegative coefficient is asserted; no sign of a vanishing leading
term is inferred from the remainder. The fixed-cell Taylor bound from
check 1041 applies. The source's GUIDE numbers supply no premise here.

## The existential statement

**LEAD-C, L277–291: HOLDS**, with all unrestricted pair sums interpreted
as ordered sums. For each unordered link pair the quadratic energy has
the term `Hh_0(l,l') Re(conj(z_l) z_l' exp(i(v_l'-v_l)))`.
Two derivatives along lambda multiply it by `-(lambda_l'-lambda_l)^2`.
The change `v=-2theta` supplies the factor 4. Summing unordered pairs,
or half the ordered pairs, gives exactly L283. Diagonal and equal-head
terms contribute zero. The ground is the sum of all fixed-head blocks.
The exact returned logarithm rotates, so its first and second derivatives
have norms at most `2||lambda|| r` and `4||lambda||^2 r`.
The Hessian Taylor remainder contributes `4M_3||lambda||^2 r^3`,
and the gradient remainder contributes `2M_3||lambda||^2 r^3`.
This proves the stated uniform-in-theta error for the fixed cell.

**HIER, L297–311: HOLDS AFTER CORRECTION of an empty minimum.**
If all `c_ij=0`, set `c_min=c_max=1`; then the hypothesis makes every
`b_j` nonzero and the sum of independent cosines proves the result
directly. Otherwise use the stated least nonzero modulus. `b_min`
exists because `b_1!=0`. The geometric tail estimates in L303–305
give a nonzero `g_j` at every angle. At an inductively chosen maximum,
adjoin the equation `Im(exp(-i v_j)g_j)=0`. At `r_j=0` its derivative
in `v_j` is `-|g_j|`, while the old gradient block is invertible.
The implicit function theorem therefore gives the stated branch.
For its Hessian the old block remains negative definite. Its Schur
complement is `-r_j|g_j|+O(r_j^2)`, which is strictly negative for
small positive `r_j`. Choose each new size below both this threshold
and `q r_(j-1)`. There are finitely many choices, in this order.
This is an existence proof, not an optimization run or a claim that
every connected XY model with fixed sizes has such a maximum.

**EXIST, L313–370: HOLDS AFTER CORRECTION of step (4) and completion
of step (5).** The exact uniform negative-response statement survives.
The selector as printed covers only a full-measure subset, not all
irreducible pins as L317 says. Here are explicit corrected arguments.

### Construction and connectivity

For (1), each required nonzero block gives a nonzero real polynomial
condition in the real and imaginary parts of `z_G,zeta_1,...,zeta_k`.
For a complex pairing use its squared modulus. Their finite product
is a nonzero polynomial, since the real polynomial ring is an integral
domain. A nonzero polynomial cannot vanish everywhere on real Euclidean
space (induct on its number of variables). Thus the simultaneous choice
exists. The breadth-first order from ground gives precisely HIER's
hypothesis. No machine enumeration is involved.

For (2), choose the HIER sizes first, then its `mu>0`, then rho small
enough for L331 and for the prescribed neighbourhood of the pure-gauge
orbit. In the invariant product metric on links, that orbit is compact.
A sufficiently small invariant tubular neighbourhood therefore lies
inside the prescribed open neighbourhood. Choose rho and B inside
this tube; gauge saturation stays inside it.
The factor 4 and remainder 6 are correct. A closed ball of
positive radius around H* fits inside both the neighbourhood and the
strict Hessian inequality, by continuity of a finite matrix. Shrink it
so the inequality has the stated margin `m_0=mu rho^2`. Saturating its
interior under the gauge group proves (3). This creates points with
negative definite response. It does **not** by itself make H* an exact
critical point of the full torus function: HIER maximizes its quadratic
model, and the full gradient can be of order rho cubed. L363's phrase
“to second order” is appropriate; the unqualified summary at L542 is
stronger than the proof. Replace claims
that the selected frames “sit at non-degenerate maxima of F_c” by
“come from non-degenerate maxima of the quadratic torus energy, and
have strictly negative full torus Hessian.” No stationarity is needed.

For (5), the following supplies the missing graph proof. All coordinates
are integral and `0<=y_mu<=S_mu`, with `S_mu>=2`. Consider a positive
boundary edge `(y,y+e_nu)` not lying on an axis through 0. Some transverse
coordinate `kappa!=nu` is at a boundary value.

* If a coordinate `mu` outside `{nu,kappa}` has `y_mu>=1`, then
  `(y-e_mu;mu,nu)` is a plaquette in face kappa.
* Otherwise all coordinates outside `{nu,kappa}` are zero. If
  `y_kappa=0`, this edge is an excluded axis edge. If
  `y_kappa=S_kappa`, choose `mu=kappa`; one of the other zero
  coordinates supplies a boundary face containing that plaquette.

In either allowed case its two successive links have heads `y` and
`y+e_nu`. Its Hessian block is nonzero for `0<beta<3/2`.
Indeed, on a 2-face, all plaquettes at its links are pinned, so their
force at the trivial pin is deterministic and zero; the unique common
plaquette gives `Hh_0(l,l')=+/- beta/4`. On a single 3-face, each link
has at most one plaquette containing free links, with weight one.
At the trivial pin `|N_l|<=beta`, its mean is zero by global colour
symmetry, and each component variance is at most `beta^2/3`.
Cauchy–Schwarz gives `|C_0(l,l')|<=beta^2/3`. The pinned common
plaquette gives `|K_0(l,l')|=beta/2`, hence the asserted lower bound.
If one of the links belongs to a 2-face its covariance is zero instead;
the same bound still applies. Distinct links have at most one common
plaquette in this box.

It remains to prove these boundary edges connect every relevant site.
Inside a lower 3-face, the vertices with at least two positive free
coordinates connect to its `(1,1,1)` vertex: first raise any zero free
coordinate to 1, then lower the other coordinates to 1. Each edge has
another positive coordinate and is not an axis edge. A nonzero axis
vertex attaches to this set by raising a second free coordinate to 1.
Lower faces intersect in nonempty 2-faces away from 0, so their unions
minus 0 are connected. A boundary vertex on no lower face has all
coordinates positive and lies on an upper face. Keep that face coordinate
fixed and lower a different coordinate to zero. This path remains on
the boundary and uses no axis edge; it reaches the connected lower-face
union. Thus the whole boundary minus 0 connects through the stated
edges. U is nonempty, for example `(S1,1,1,1)` belongs to it. Collapsing
U to ground preserves connectedness and gives exactly (CONN).

For (6), finite compact integration proves that Z and its pin derivatives
are entire in beta: the exponential series and each differentiated
series converge uniformly on every bounded complex beta disc. On the
real line `Z>0`, so the logarithmic Hessian entries are real analytic.
Fix the finite set of link pairs used by the preceding graph, independent
of beta. None of their scalar entries is identically zero, by the
strict lower bound on `(0,3/2)`. For a nonzero analytic function, at each
zero its first nonzero Taylor coefficient isolates that zero; an
accumulation of zeros in the domain would force the function identically
zero. A finite union of these zero sets is locally finite in `(0,infinity)`.
Consequently D is indeed discrete there and finite on `[2.3,2.6]`.
It is a sufficient exceptional set, not necessarily the actual failure
set for (CONN). The proof does not assert (CONN) at every beta>=3/2.

### A Borel covariant selector on every irreducible pin

The first scope failure in step (4) is L336: two *fixed* non-tree links
can have parallel axes at an irreducible pin. Other holonomies can make
that pin irreducible. The lexicographic selection claim in L340 is also
left without the needed measurable-selection proof. Neither requires
a new scientific assumption. Replace step (4) by the following text.

Fix the tree, enumerate all pairs of non-tree links, and take the first
pair whose imaginary holonomy vectors are nonparallel. Such a pair
exists at every irreducible pin: in SU(2), commuting holonomies lie in
one maximal torus, and their common stabilizer otherwise is the centre.
The pair choice is Borel and gauge invariant. In tree gauge, normalize
the first vector to e1, normalize the component of the second perpendicular
to e1 to e2, and set e3=e1 cross e2. The rotation carrying this oriented
basis to `(i,j,k)` is unique and continuous on each pair chart.
Conjugating the holonomies by this rotation gives the canonical pin
`omega_hat`, equal for all members of a gauge orbit. Tree transport and
this rotation give a gauge `s` with `omega^s=omega_hat`, unique up to
one global central sign. A Borel SU(2) lift exists explicitly: use the
first largest squared quaternion coordinate in the rotation-matrix
formulas, take its positive square root, and solve for the other three
coordinates. The chosen squared coordinate is at least 1/4, so every
division is defined; each branch is Borel. Only Ad(s) is used in n.

Let `(a_j)` be a fixed countable dense subset of the finite product
SU(2) of site gauges. For `omega in P` choose the least j for which
`omega_hat^(a_j)` belongs to the **interior** of B. The set of such
gauges is nonempty and open: P is precisely the saturation of that
interior. Density gives an index. Each test is open in the canonical
pin, so choosing the least index is Borel. Put `g=a_j s` and
`n_x=Ad(g_x^{-1})i`. Then `omega^g` lies in B and L334 gives the
same uniform m0. Under `omega -> omega^h`, the canonical pin and j do
not change, and `s(omega^h)=s(omega)h^{-1}` up to the global centre.
Hence `n(omega^h)=Ad(h)n(omega)` exactly. This proves both Borel
measurability and covariance without a lexicographic compact-fibre theorem.

The irreducible domain is open. Its complement has Haar measure zero:
tree gauge preserves product Haar measure on the independent non-tree
holonomies; a fixed pair is nonparallel almost surely. Conditional on
the first noncentral holonomy, the second belongs to its one-dimensional
centralizer with probability zero in the three-dimensional group SU(2).
This follows directly from smooth Haar charts, or polar coordinates on
the unit three-sphere. The boundary graph has at least two non-tree links.
Finite Wilson conditional densities are strictly positive, so the open
set P retains positive probability in the surrounding Gibbs law.

This completes the corrected existential statement on `P minus reducibles`,
with all lambda on L and a uniform m0. It proves no typical-pin bound,
no lower bound on the measure of P, and no full (O2) extension estimate.

**Global COUL selection, L117–120: HOLDS AFTER CORRECTION of the
unproved selection shortcut.** The open-ball selector above is enough
for EXIST, but does not select an exact trace maximizer. For that use
the following compact construction. Let K be the compact product of
rooted site gauges. For every fixed nonempty compact `C subset K`,
`m_C(omega)=max_(g in C) M_omega(g)` is continuous, since M is jointly
continuous on compact sets. Thus the test `m_C=m_K` is closed.
For each integer n choose a finite cover of K by closed balls of radius
`2^(-n)`. Start with C0=K. At stage n take the first ball whose
intersection Cn with C(n-1) has `m_Cn=m_K`. At least one exists because
the preceding compact set contains a maximizer. Every finite history
is Borel by these closed tests. The Cn are nested compact sets, have
diameters tending to zero, and each intersects the compact maximizer
set. Their unique common point is an exact maximizer. It is a Borel
function: the chosen ball centres are Borel and converge to that point.
Apply this construction to the canonical irreducible representative
above, then undo its canonical gauge. Carry its colour by the same
rule. The resulting frame is Borel and covariant. The central sign
acts trivially. This replaces, rather than silently invokes, the
source's lexicographic-selection assertion. It does not give global
continuity or remove Gribov multiplicity outside UNIQ's domain.

## Remaining checks

**LOOP, L381–387: HOLDS**, for a face large enough to contain the two
specified disjoint deep plaquettes. Each oriented loop has two opposite
signed imaginary link values at each vertex, so its divergence vanishes
*exactly*, not just to first order. The two loops preserve this property.
For small rho, compare the critical gauge g=1 with the absolute
maximizer using the strict second-derivative bound in corrected UNIQ;
both lie in its comparison ball, so they coincide. The reference
holonomy is `exp(4rho a_0)`, whose axis is a_0 for sufficiently small
positive rho. Its transverse part is zero. At the tested site's two
incoming loop links, the other two loop links provide four cross pairs.
Their signed K entries are beta/2 and each covariance component has
modulus at most beta squared/3. LEAD-C therefore gives exactly
`H_c <= -16rho^2(beta/2-beta^2/3)+O(rho^3)`.
For fixed `0<beta<3/2`, choose rho small, then use continuity of the
axis and the response to obtain an open pin set. No all-lambda result
for COUL follows. The positive witness of L388–394 remains ARGUED;
the exactly transverse correction it omits is not discharged here.
The smooth-field discussion L395–402 remains a model heuristic.

**SQ, L432–437: HOLDS.** Completing the square as in the initial test
proves the exact constant `A+B^2/m`. Orthogonality of X and Y is not
needed. A merely semidefinite gradient restriction does not suffice.

**CURL-P, L439–451: HOLDS given corrected EXIST.** Here are the
constant and domain checks. At most six plaquettes of the 4D box meet
one link. Cauchy–Schwarz on each four-link plaquette gives
`|A''|<=24beta ||theta||_2^2`. Also
`|A'|<=6beta sum_l |theta_l|<=6beta sqrt(N)||theta||_2`, so
`Var(A')<=36beta^2 N||theta||_2^2`. Thus the stated A0 bounds
the absolute quadratic form. By the spectral theorem for its real
symmetric matrix, it bounds the associated mixed form by
`A0 ||x||||y||` as well.

First set lambda_0=0. Each pinned site has degree at most eight, hence
`||d lambda||_2^2<=16||lambda||_2^2`. EXIST gives the strict bound
with `m=m0/16` on this gradient subspace. For arbitrary lambda_0,
`d(lambda_0 1_{0})` is a null direction with zero mixed form: every
link at 0 has tail 0, all its rotations use n0, and adding this
direction multiplies those link curves by one common site gauge.
Those rotations commute with the other rotations at tail 0, so F
is exactly unchanged even with an arbitrary theta already present.
Remove that component before applying SQ. This proves (c) with B=A0.
On `(ker d)^perp`, the spectral definition of mu1 gives
`||theta_c||^2<=||d theta_c||^2/mu1`, and `d(d lambda)=0`.
Consequently

`C=(A0+16A0^2/m0)/mu1`,  `A0=24beta+36beta^2 N`,

is valid exactly on the stated space
`(ker d)^perp + d{lambda: supp(lambda) subset L}`.
This does not prove the same estimate for every boundary field.

One correction to the explanation at L454–455: a lambda merely
*nonzero* on U need not give a missing direction. If it is constant
on U, subtract that constant everywhere; its gradient then has a
representative supported on L. Because the boundary graph is connected,
a gradient has such a representative exactly when lambda is constant
on U. Thus the missing gradients are those with nonconstant restriction
to U. Such gradients exist. The bound supplies neither the classical
constant nor size uniformity.

**U(1), L415–428: HOLDS for the common-axis frame.** Its adjoint action
is trivial; the returned pin curve is constant for every allowed
gradient. Therefore `Dn=Psi=H_c=Q=0` on those gradients. There is no
transverse z, so HIER's required nonzero couplings cannot be realized
and EXIST's strict conclusion has no U(1) analogue. For any real extension
of theta to the cell, each plaquette phase changes by `s(d theta)_p`;
the negative of its second action
derivative is bounded by `beta w_p(d theta)_p^2`. Subtracting the
nonnegative score variance gives the classical bound
`H_c<=beta sum_(p in cell) w_p(d theta)_p^2`. Boundary gradients
are exact U(1) gauge moves after extending their site function to the
cell, so they have zero mixed terms as well. No improved constant or
boundary-only extension estimate is inferred from this argument. The zero
claim is about gradient gain, not the response to arbitrary fields.
Site-sign frames are outside this common-axis control.

## Meaning and final disposition

The existential finite-cell (O2-min) statement survives for every
`0<beta<3/2` and every positive beta outside the discrete sufficient
exceptional set D. Its Borel covariant frame and uniform strict bound
on one open pin set are supplied by the corrected proof above. It
does not identify that frame with COUL. It does not select a named
beta in `[2.3,2.6]`, although all but finitely many values there work.

This is negative curvature of F_c along special, nonlinear pin paths.
The cube test explicitly obtains it by acceleration tangent to a level
set at first order. EXIST obtains it by arranging maxima of the
quadratic torus energy; no positive stiffness bound is inferred.
The representation of every frame as a constant colour is an algebraic
fact, not a small-potential estimate for every frame. The defect and
probability requirements still have to be proved for the chosen rule.

The wall (W), as stated in `parts/gap.md:18–23`, does not move. Literal
(O2) still needs an admissible extension, since the GR score variance
can cancel the negative response at the same order. N1 at the pins
carrying the measure, N2 there, N3's gain, O1, the classical constant,
the missing upper-face gradients and compatibility between cells all
remain outside this result. No universal failure of other frames follows.

The material corrections, ranked by their downstream effect, are:

| Statement | Verdict | First failing or incomplete source line; correction |
|---|---|---|
| EXIST selection on every irreducible pin | HOLDS AFTER CORRECTION | L336, fixed pair does not cover that domain; use the finite pair charts and explicit Borel selector above. |
| Exact full-energy maximum interpretation | FAILS as an inference | L542's unqualified summary; L363 already says “to second order.” The proof gives the negative Hessian, not exact stationarity. |
| UNIQ at the printed threshold | HOLDS AFTER CORRECTION | L114, zero margin is called negative; retain the sharper constant 28 instead of 32 in the proof. |
| CG stabilizer/covariance wording | HOLDS AFTER CORRECTION | L83, transformed stabilizers are not generally constant; use site stabilizers and a fixed reference colour. |
| COUL minimizes the colour defect | FAILS | L236 title; squared defect is 4 versus TREE's 3 in the hand example. The actual LIP-C inequality HOLDS. |
| CUBE-C proof | HOLDS AFTER CORRECTION | L137, lowering one class angle need not preserve the product; use the scalar upper-bound argument. |
| HIER edge-free case | HOLDS AFTER CORRECTION | L302, empty c_min; separate the independent-cosine case. |
| Missing-gradient description | HOLDS AFTER CORRECTION | L454; nonconstant restriction to U is the obstruction, not merely a nonzero restriction. |

LEAD-C, the CUBE-COUL formula, LOOP on its stated geometric domain,
SQ and common-axis U(1) control HOLD. CURL-P HOLDS given corrected
EXIST, with its printed constant and restricted field class. The graph
and discrete-beta arguments hold with the explicit details recorded here.

Verification was by the displayed hand arguments, including the three
required initial tests. No numerical, interval, enumeration or Lean run
was used as proof. No audit, ledger, registry, source note or FINISH row
was edited. Row 1044 was not read. The source's GUIDE logs and the
original Zwanziger, van Baal, Singer and Balaban papers were not checked;
no result here relies on those unverified reading claims. The indexed
SA passages and named repository inputs above are the literature used.

RESULT: HOLDS AFTER CORRECTION: generic-beta existential (O2-min), the cube formula and restricted CURL-P survive the hand check; explicit selector, endpoint-margin and scope corrections are required, exact full-energy stationarity is not proved, and (W), full (O2) and the mass-gap problem remain untouched. Research check only; no status granted.
