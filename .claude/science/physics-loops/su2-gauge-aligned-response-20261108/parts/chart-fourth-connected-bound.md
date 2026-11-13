# Four-insertion connected bound on the fixed quotient cube

Author proof, 2026-11-09; independent mathematical check pending. This is a
restricted-chart result, not a result for compact rough fields. Source snapshot:
base `55fd670ff8995427b24617b2273bd3f78b7559d9`; mathematical inputs are
`nonlinear-chart-response.md` (C5–C8), `flat-two-step-bound.md` (§3), and the
main two-region note (§§1–3). Current workflow and workhorse instructions were
read. Preflight passed; no target model floor was checked, memory cap was
unavailable, and no numerical job ran. No Git/network mutation was requested.

Literature reconciliation: the 2026-11-09 connected-response inventory locates
Georg Menz's covariance estimate (with Otto credited for its theorem method),
Helffer–Sjöstrand's convex covariance machinery, and the higher-cumulant
expansions of Abdesselam–Procacci–Scoppola and Lohmann. None is imported as an
unchecked fourth-cumulant theorem. Here the already supplied cube covariance
proof plus elementary four-variable cancellation suffices at fixed order four.
This avoids an all-orders forest expansion, whose hypotheses would require
additional work. The inventory's statement that covariance alone is not a
fourth-cumulant theorem remains correct: the moment scales, product-gradient
bounds, cancellations and geometry below are essential extra steps.

## 1. Statement and exact scope

Use exactly the fixed Cartesian terminal-root quotient cube and actual joint
two-hidden-layer law of `nonlinear-chart-response.md`, with terminal V=I,
β=u, both kernel strengths λ=κu, fixed odd L≥3, κ>0, m≥3, u≥u_*.
All normalizers and exponential-coordinate Haar densities remain in the law.
Write μ for this normalized restricted law. Use its constants g_*, α>0,
Hess S≥ug_*/2 and

    |Cov(f,g)| ≤ C0 u^(-1) exp[-α d(supp f,supp g)]
                         ||∇f||_2 ||∇g||_2.                 (1)

Supports are actual sets of terminal blocks containing coordinate readers.
Let F,G be fixed real C² functions on the closed cube, obtained by restriction
of original sources, invariant under simultaneous SU(2) conjugation. Their
actual coordinate support sizes, block diameters and C² norms are bounded
independently of volume and u. Norm bounds refer to quotient-coordinate
restrictions, including all original-source readers introduced by the forest.
For identifying these restrictions with original observables after orbit
integration, gauge invariance under the root-fixed shared gauge group is
required; global conjugation invariance alone does not remove orbit terms.
The theorem itself applies to the specified quotient functions.

For distinct terminal links c,d and fixed unit tangent color vectors n_c,n_d,
set A_c=κu <i n_c·σ,M_(1,c)> and likewise A_d. Their reader sets S_c,S_d
have bounded size and diameter and lie within a fixed radius R(L) of their
terminal starting blocks x_c,x_d. Put S_1=S_F,S_2=S_G,S_3=S_c,S_4=S_d.
Choose D bounding all four diameters. Define τ(S_1,S_2,S_3,S_4) as the minimum
number of nearest-neighbor terminal-block edges in a connected subgraph
meeting every S_i; a minimizer can be a tree. This definition uses actual
supports, allows overlaps and Steiner vertices, and uses periodic distances.
Empty-support insertions are constants and their cumulant is zero; exclude
those trivial cases from τ's definition.

There are C<∞ and μ0=α/3>0 independent of m,u,c,d such that

    |κ4,μ(F,G,A_c,A_d)| ≤ C u^(-1) exp[-μ0 τ].             (2)

Moreover, for every 0≤ν<μ0 there are Cν<∞ and bν>0 such that

    Σ_(c,d:c≠d) exp[ν τ] |κ4,μ(F,G,A_c,A_d)|
        ≤ Cν u^(-1) exp[-bν d(S_F,S_G)].                  (3)

Constants depend on L,κ, the fixed cube, support bounds and source C² norms.
These are existence constants. This is neither a physical mass-gap bound nor
an arbitrary bounded/nonsmooth-source estimate.

## 2. Local moments and the invariant-source improvement

The cube is not invariant under all color rotations. It is invariant under
simultaneous color π rotations around each coordinate axis. These rotations
conjugate every retained link, leave all tree links and terminal I fixed,
preserve both kernel factors, every normalizer and Haar density, and send
any chosen color component to its negative for a suitable axis. Hence Eμ a_i=0
for every scalar coordinate i. No continuous rotation symmetry of the cube
has been assumed.

For a real coordinate vector h, let ψ(t)=log Eμ exp(t h·a).
The tilted density has negative logarithm S−t h·a and the same convex cube
and Hessian lower bound m0=ug_*/2. The scalar Neumann spectral-gap proof
preceding (C8) therefore applies at every real t, giving

    ψ''(t)=Var_t(h·a) ≤ |h|²/m0.

Since ψ(0)=ψ'(0)=0, integration gives ψ(t)≤t²|h|²/(2m0).
Chernoff's inequality with t=m0 r/|h|², and its negative counterpart,
give P(|h·a|≥r)≤2 exp[−m0 r²/(2|h|²)]. Tail integration proves
||a_i||_p≤C_p u^(-1/2) for each fixed finite p. For any coordinate set J
of bounded cardinality, Minkowski's inequality gives

    || |a_J| ||_p ≤ C_(p,|J|) u^(-1/2).                  (4)

This argument invokes only the already derived cube spectral gap, including
its face boundary conditions; no whole-space concentration theorem is
silently applied to a hard cutoff.

Simultaneous conjugation invariance of F implies ∇F(0)=0: the derivative
in each retained link's three color components is a vector fixed by every
SO(3) rotation, and is therefore zero. This assertion concerns the source
function at the origin, not invariance of the cube under arbitrary rotations.
If K_F bounds its local-coordinate Hessian, Taylor's theorem along the segment
from 0 to a_(J_F), contained in the cube, gives

    |F(a)−F(0)|≤K_F |a_(J_F)|²/2,
    |∇F(a)|≤K_F |a_(J_F)|.

The same holds for G. Centering changes no gradient and costs at most two
in Lp, so (4) gives

    ||F−EF||_p + ||G−EG||_p ≤ C_p/u,
    ||∇F||_p + ||∇G||_p ≤ C_p/sqrt(u).                   (5)

The score divided by u, B_c=κ<n_c,M_(1,c),vector>, vanishes at a=0.
The finite contour words give a uniform local C¹ bound on B_c, so
|B_c(a)|≤C|a_(J_c)| and |∇B_c(a)|≤C. Its vector mean is zero by the
same three π rotations; alternatively centering only changes the moment
constant. Consequently

    ||A_c−EA_c||_p≤C_p sqrt(u),  ||∇A_c||_p≤C_p u.        (6)

The constants are uniform in c and the chosen unit color tangent. All
moments used below have fixed finite order (at most order twelve for the
underlying coordinates), independent of volume.

## 3. Cumulant cancellation across every nonempty cut

Put X_1=F−EF, X_2=G−EG, X_3=A_c−EA_c, X_4=A_d−EA_d,
and weights w_1=w_2=u^(-1), w_3=w_4=u^(1/2). Equations (5),(6) say

    ||X_i||_p≤C_p w_i,   ||∇X_i||_p≤C_p sqrt(u) w_i.

For any nonempty subset I of {1,2,3,4} of size at most three, product rule
and Hölder with exponent 2|I| on each factor show

    ||∇(Π_(i∈I) X_i)||_2 ≤ C sqrt(u) Π_(i∈I) w_i.        (7)

There is no dependence on the diameter of the union support in this norm.
Apply (1) to products on two sides I,J of any nonempty cut. Equation (7)
gives

    |Cov(Π_I X_i,Π_J X_j)|
       ≤ C (Π_(i=1)^4 w_i) exp[−α d(S_I,S_J)],           (8)

where S_I=union_(i∈I) S_i. Products are C¹ and have precisely these support
upper bounds; centering adds constants, not coordinate readers.

For a 1|3 cut, label the isolated index i and the other indices j,k,l.
Since EX_i=0, the exact centered fourth-cumulant formula is

    κ4 = Cov(X_i,X_j X_k X_l)
       −Cov(X_i,X_j)Cov(X_k,X_l)
       −Cov(X_i,X_k)Cov(X_j,X_l)
       −Cov(X_i,X_l)Cov(X_j,X_k).                        (9)

Every covariance-pair term contains a factor crossing this cut. Apply (1)
and the gradient bounds to that crossing factor, and Hölder to the other:
|Cov(X_k,X_l)|≤||X_k||_2||X_l||_2. Each whole term is bounded by
C Π_i w_i exp[−α d(S_I,S_J)].

For a 2|2 cut {i,j}|{k,l}, the exact formula instead is

    κ4 = Cov(X_i X_j,X_k X_l)
       −Cov(X_i,X_k)Cov(X_j,X_l)
       −Cov(X_i,X_l)Cov(X_j,X_k).                        (10)

The within-side pairing is already subtracted by the first covariance.
Both remaining pairings cross the cut, so the same bound applies. Equations
(9),(10) exhaust every nonempty split. Since Π_i w_i=u^(-1),

    |κ4|≤ C/u exp[−α d(S_I,S_J)]                         (11)

for every such split. This is the needed disconnected-subtraction check.
Using singleton-isolation cuts alone would miss the separation of two nearby
pairs; (10) is essential. No fourth derivatives of F or G are required.

## 4. Connecting tree geometry with actual supports

Choose arbitrary representatives x_i∈S_i. On the four labeled representatives,
form a minimum spanning tree with edge weights d(x_i,x_j), allowing zero
weights when representatives coincide. Write T for its total weight and e
for a largest edge, so e≥T/3. Removing that edge partitions the four labels
into nonempty sets I,J. The minimum-spanning property implies

    d(x_i,x_j)≥e for every i∈I,j∈J:

otherwise replacing the deleted edge by that crossing edge decreases the
tree weight. For s∈S_i,t∈S_j, the triangle inequality gives

    d(s,t)≥d(x_i,x_j)−2D≥T/3−2D.                        (12)

Realize the three tree edges as shortest terminal-block paths. Their union
is connected and meets every S_i, so τ≤T. Consequently the cut in (12)
has d(S_I,S_J)≥τ/3−2D. Substituting into (11) proves (2), with the
factor exp(2αD) absorbed into C. This proof remains valid when the
right side of (12) is negative, when sets overlap, and on small periodic
tori. It never treats set distance as a metric without diameter correction.

## 5. Weighted sum over the two terminal links

Fix representatives x_F∈S_F and x_G∈S_G. A minimizing connected tree
for τ meets each S_i at a vertex y_i. Each pair of its vertices is at
ambient distance at most τ, and d(x_i,y_i)≤D. Therefore

    d(x_F,x_G)≤τ+2D,
    d(x_F,x_c)≤τ+D+R,   d(x_F,x_d)≤τ+D+R,              (13)

where x_c,x_d now denote terminal-link starting blocks and the fixed R
bounds distances from these anchors to their respective score readers.
Adding (13) yields

    τ ≥ [d(x_F,x_G)+d(x_F,x_c)+d(x_F,x_d)]/3
           −(4D+2R)/3.                                (14)

Let η=μ0−ν>0. Multiply (2) by exp(ντ), then use (14). With fixed four
positive edge directions per terminal vertex, summing over all c,d,
including the diagonal for an upper bound, gives

    Σ_(c≠d) exp(ντ)|κ4|
      ≤ C/u exp[−η d(x_F,x_G)/3]
          [4 Σ_x exp(−η d(x_F,x)/3)]².                 (15)

The periodic four-dimensional graph has at most (2r+1)^4 vertices within
distance r, uniformly in torus size. Thus the bracket is bounded by
4 Σ_(r≥0)(2r+1)^4 exp(−η r/3)<∞. Since d(x_F,x_G)≥d(S_F,S_G),
(15) proves (3) with bν=η/3. Fixed source and score support radii are
essential to this summability statement.

## 6. Exact response and remaining domain boundary

With the fixed cube held fixed as V,s,t vary, compact differentiation of
Z_delta(V;s,t) is legitimate. For distinct links c,d, D_d A_c=0 because
the score depends on V_c and its own hidden readers, not V_d. The exact
identity is therefore

    D_c D_d ∂s ∂t log Z_delta(V;s,t)|_(V=I,s=t=0)
       = κ4,μ(F,G,A_c,A_d).                             (16)

Both hidden-layer normalizers are still inside μ; their output-independence
only explains the score formula. A repeated-link derivative has an additional
derivative-of-score term and is outside (16). For a normalized coarse
conditional log p=log W−log Q one must subtract the complete corresponding
D_c D_d ∂s ∂t log Q coefficient. Bound (2) concerns the specified fixed-terminal
restricted posterior; it does not by itself supply a uniform bound for the
Q law integrating terminal variables or for arbitrary terminal backgrounds.

Author checkpoint: (2),(3) follow from the explicit cube convexity/covariance
inputs by the proofs above. Open outside this result: compact rough-field
reconstruction with normalized connected insertions, orbit contributions for
non-gauge-invariant original sources, nonidentity terminal backgrounds, and
further blocking. Independent checking of this new argument remains pending;
no retained status or full compact/physical-gap claim is made.

Input identities (SHA-256; provenance only, not proof validation):

- `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/nonlinear-chart-response.md`: `5edacc8ee78d54b7fb853fb34da3d8cceffd8eb0e476f8510d15048f8f10f2d1`
- `.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/flat-two-step-bound.md`: `0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a`
- `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`: `94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c`
