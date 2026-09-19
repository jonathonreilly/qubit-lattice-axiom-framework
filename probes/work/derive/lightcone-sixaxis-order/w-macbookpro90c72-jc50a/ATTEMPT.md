# lightcone-sixaxis-order, attempt 3 (worker w-macbookpro90c72-jc50a, model grok-4.6)

No prior attempt printed. Route: reversibility for general six-axis `(p,q,r)` from symmetry of `φ`, not from a spin bilinear; then a cube Peierls ratio at `(3,1,2)`.

## (1) The statement attempted

(a) For any symmetric pair weight `φ(s,s')=φ(s',s)` — in particular six-axis `(p,q,r)` — the synchronous light-cone kernel `P(s→s')=∏_x r(s'_x | {s_y : y∈N(x)})` with `r(s'|N)∝∏_{y∈N} φ(s',s_y)` is reversible with respect to `π(s)∝∏_x Z_x(s)`, `Z_x=∑_{s'}∏_{y∈N(x)} φ(s',s_y)`, on any *undirected* neighbourhood `N`. The site itself may be included (7-stencil) or omitted (6-stencil); both work. (b) `π` is invariant under signed permutations of the axes, so the six constant configurations have equal weight. On the `2×2×2` cube at `(3,1,2)` a one-site antipodal flip and a 4+4 two-axis split are strictly lighter than a constant, so the constants are local maxima of `π` already at the PSD boundary `p=3`. (c) The static law of block 17 is a different interaction (`∏_{\mathrm{bonds}} φ`); its threshold is not `π`'s. (d) For a reversible automaton, “memory of the aligned plane” is convergence to the corresponding stationary phase, not a transient of a Toom eroder (and the symmetric majority is not an eroder, as the task states).

A proved infinite-volume Peierls threshold on `(p,1,2)` is not obtained (`L=2` cube degeneracy; no contour sum).

## (2) Steps

**Step 1 — product identity (PROVED; CHECKED R.1–R.4).** `φ` is symmetric (same / antipodal / orthogonal are symmetric relations). For undirected `N`,

    ∏_x ∏_{y∈N(x)} φ(s'_x, s_y) = ∏_{x,y: y∈N(x)} φ(s'_x, s_y) = ∏_{y,x: x∈N(y)} φ(s_y, s'_x) = ∏_y ∏_{x∈N(y)} φ(s_y, s'_x).

Hence `π(s)P(s→s')` equals `π(s')P(s'→s)`. Checked on `C_4` for both the 3-stencil (site included) and the 2-stencil (site omitted), every 6-valued configuration against four probes. The site itself is optional.

**Step 2 — detailed balance, six-axis (CHECKED R.5–R.6).** On the two-site period-2 torus the 7-stencil double-counts the neighbour. At `(3,1,2)` the `36×36` kernel is stochastic and satisfies detailed balance against `∏_x Z_x` on every pair.

**Step 3 — six constants (PROVED; CHECKED P.3).** Signed permutations of the axes preserve `φ` and the lattice, hence preserve `π`. The six constant configurations have equal weight (checked on the cube).

**Step 4 — local Peierls ratios on the cube (CHECKED P.1, P.4).** At `(3,1,2)`, the unnormalized `π`-weight of a one-site antipodal flip over a constant is `2167007881/207594140625 < 1`; a 4+4 split is also strictly lighter. So an island of a wrong axis already costs at `p=3` on this window. This is not a contour bound on `Z^3`: the `L=2` 7-stencil is degenerate (`±e_j` coincide), and there is no sum over contours.

**Step 5 — memory for a reversible chain (PROVED).** Unique mixing on a finite torus (the kernel is strictly positive) sends every initial plane to `π`, which is a mixture of the six constants if those dominate, or a paramagnet if they do not. “Memory” is then the finite-torus mixing time, or, in infinite volume, which phase is selected by the aligned start. It is not Toom stability of a majority eroder (closed by the task).

## (3) Where the route stops

The first step that fails as an infinite-volume ordered-phase theorem is the contour sum: a single-cube cost at `p=3` does not control the entropy of large contours, and `L=2` is degenerate. Comparison with block 17's constant (under repair) is therefore only qualitative (`π` ≠ static). Executed light-cone six-axis memory is not given a proved `p_*` here.

## (4) What would finish it

A Peierls / chessboard bound for `π=∏_x Z_x` on even tori of side `≥4`, using bond-plane RP of the many-body weight (or a contour energy from `log Z`); a nondegenerate `L=4` one-flip ratio as a function of `p` on `(p,1,2)`.
