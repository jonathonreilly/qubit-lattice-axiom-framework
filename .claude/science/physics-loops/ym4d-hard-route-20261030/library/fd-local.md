# Several-jump F-D by localization to one-wall patches
Provenance: OpenAI/Codex (GPT-6 family; exact serving model and runtime effort setting are not exposed), commit `15c601852769bba50f1198cd5f7b01717b45066b`; mapped-side research text, not an audit; no scientific status is granted.

## 1. Contract and premises

**Discharged (scope and source identity).** This note tests localization of the several-jump saddle problem, not (WP). The prescribed sections of `GOAL.md` and `FINISH.md` were read first. Only this file is written. Computer use consists of source inspection and text editing; no run discharges a mathematical claim. The workflow is absent from the sparse working tree but available in the pinned commit. The user's single-file task takes precedence over campaign, delegation and delivery operations.

**Unchecked (inputs).** The one-jump Theorem F-D, the brick extension theorem, covariant block estimates and the consumer inductions are research premises. Their source labels do not independently verify them here. In particular the assertion in the proof of (NC) that clearance supplies one-wall patches is a target of this note, not a premise. No recalled theorem will be used without either a written proof or an explicit memory/gap label.

**Unchecked (memory attribution).** The Lipschitz size-function, greedy-cover, IMS and Schur-parametrix patterns are familiar methods recalled from memory. Their quantitative uses here are written out; no external covering, elliptic regularity or gauge-fixing theorem is imported. The local bump formulas are taken from the cited mapped-side note and expanded below.

**Discharged (notation).** Write `s_l=L^(l-n)`, with top scale `s_n=1`. A retained site block is a leaf of the refined partition. Independent bond rows have at least one leaf endpoint; recovered parent rows are not extra multipliers. `C_N` denotes these bond rows, `r_N` the leaf site averages, and `P_N` the orthogonal projection onto `ker r_N`. The row norm is `||Y||_Lam^2=sum_l s_l^-2 ||Y_l||_(N_l)^2`. Source `s^#` is the enlarged local scale near a wall; its asserted comparison `s <= s^# <= Ls` itself presumes adjacent-scale jumps.

## 2. Clearance geometry

**Discharged (what the printed clearance says).** `quiet-boundary-rarity.md:43–49` measures `t_0` in level-`l` cells. Its conditions are `N(shadow E_(l+1)) subset E_l`, where `N` adds `3t_0` such cells, and `E_l subset neighbourhood_((2/3)t_0 L)(shadow E_(l+1))`, with brick rounding. Its lower layer lies inside the next layer. The two sides have different margins: the margin against `E_(l+1)` is `3t_0 s_l`; the other is at least `(t_0/3-2t_0/L)s_(l+1)`. These are not both `t_0 s_(l+1)`, still less `t_0 s_(l+2)`. Allowing boundary cells and the factor of at most four between the usual lattice distance and maximum distance in dimension four, `t_0 s_l/4` is a safe common maximum-distance margin for `L>=32`. The sentence preceding (NC), `fibre-propagator.md:142`, is stronger-sounding than this actual supplier. The interface at `parts/upper-chain.md:1264` separately asks distance `r_S s_(l+1)` from both boundaries; that requirement must also be met.

**Discharged (a hand-checkable near-two-wall geometric test).** Use the last coordinate of the four-dimensional brick tiling, whose slab faces have spacing `t_0 s_l`. On a large periodic box take two widely separated fronts; near one of them write `E_l={x_4<a_l}` and

```
a_(l+1)=0,       a_l=8t_0 s_l,
Sigma_(l+1)=[0,w_(l+1)],
Sigma_l=[8t_0 s_l,8t_0 s_l+w_l],
t_0 s_i <= w_i <= 2t_0 s_i.                         (G1)
```

Use half-open blocks; `w_i` is the width selected by the source's neighbourhood convention (including a brick at the threshold can add one row). Shifting a closed face by one fine cell does not affect the following strict inequalities. These slabs are unions of the bricks and of whole parent blocks when `t_0` is a multiple of `8L`. A brick within `3t_0` cells of the upper front extends at most one additional brick beyond that neighbourhood, hence lies inside `E_l`. Every brick of `E_l` outside the shadow lies within `8t_0` cells of it. Thus (N),(B) hold for `L>=32`. The second front can be closed in the opposite direction, with separation greater than four times the sum of the displayed widths and displacements; it creates no interaction with this calculation. At `U=1` take all data equal to the identity, so compatibility and quietness impose no further field restriction. Extra levels can use displacement `8t_0 s_i` in exactly the same way.

The first wall changes the leaf scale from `s_(l+2)` to `s_(l+1)` and the second from `s_(l+1)` to `s_l`. Their distance in units of `S=s_(l+2)` is `8t_0/L^2`. A ball centred at the first wall with radius `R S` therefore sees both when `8t_0<R L^2`. This is a counterexample to deducing the centred one-wall-patch assertion from (N),(B) with merely `t_0` large compared with `L`. To meet the separate two-sided interface margin one also needs `8t_0/L>=r_S` and the corresponding outer margin; these are explicit restrictions on this example. **It is not a counterexample under every possible later choice of `t_0` or `a_*`.** In particular the other lower bounds on `t_0` in mapped line 24 might already force a larger value. No such value is inferred from unspecified constants.

**Discharged (moving patch centres does not remove a too-small collar for free).** Write `g=8t_0 s_l`. Suppose a proposed partition has total multiplicity at most `N_*`, and every cutoff active at a coarse-side point `x_4=-epsilon` has Lipschitz constant at most `K_chi/(RS)`; this is the quantitative own-scale cutoff requirement, with comparability constants included in `K_chi`. Each one-wall cutoff must vanish either at `x_4=0` or at `x_4=g`: if it is nonzero at both, its support meets both jumps. Consequently `|chi_i(-epsilon)|<=K_chi(g+epsilon)/(RS)`. A squared partition of unity would give

```
1 <= N_* K_chi^2 (g+epsilon)^2/(R^2 S^2).
```

Letting `epsilon` decrease to zero rules this partition out when `8t_0/L^2<R/(K_chi sqrt(N_*))`. On a lattice take the first coarse-side fine site and then arbitrarily refine the underlying fine spacing, leaving these three block scales fixed. Thus an off-centre cover must pay in cutoff derivatives or overlap when this ratio is small; a large geometric diameter alone is insufficient. This rejects that uniformly normalized localization for those parameter values, not the repair (G2), and not F-D.

**Implication (repair of the geometry, permitted by the order of constants).** Fix a patch parameter `R>=10` before `L`, and choose

```
t_0 >= 10^4 R L^2                                    (G2)
```

as an additional lower bound when the geometry is fixed. Mapped line 24 places `t_0` after `L,a_*` and imposes no competing upper bound; `36t_0<=Lt_0` only asks `L>=36`. Thus (G2) is an available fixed-geometry choice, independent of depth and volume. It is not an existing proved consequence of the smaller printed lower bounds.

Here is a precise domain on which the repair works. Let `F_l` be the union of the level-`l` layers of any number of **complete** families, all on the prescribed level-`l` brick tiling, with `F_n` the whole top domain. Require the supplied collars, including each family's top collar. Then

```
F_l + [-t_0 s_l/4,t_0 s_l/4]^4 subset F_(l+1).        (G3)
```

For a union this follows pointwise: a point belongs to some family's lower layer, and its entire displayed neighbourhood belongs to that family's upper layer. Adding other families cannot destroy the inclusion. This is a useful distinction from pairwise separation of different families, which is not required. Joins at the same scale remain one refinement boundary. If a recursively introduced family is truncated at its top, its top collar must be supplied by the already frozen region; (G3) does not follow merely from its lower collars. The junction discussion at `quiet-boundary-rarity.md:35–39` does not by itself verify every such top collar. **Gap:** this last identification for every data set quantified by `(I_j^D)` is not completed here.

**Discharged (skipped-scale test on (G3)).** Put `sigma(x)=s_l` on `F_l\F_(l-1)`. Because each inclusion has a positive collar, near `boundary F_l` the two actual scales are exactly `s_l,s_(l+1)`. Neither `F_(l-1)` nor the complement of `F_(l+1)` can touch that boundary. Thus a direct jump `s_l -> s_(l+q)`, `q>=2`, is excluded on this domain, including unions of complete families. Dropping intermediate frozen regions would remove this proof; retaining their dependent averages as algebraic rows would not restore the missing geometric collars. Moreover, for `j<k`, the separation of `boundary F_j` from `boundary F_k` is at least `t_0 s_(k-1)/4=(t_0/(4L^2))s_(k+1)`: use `F_j subset F_(k-1)` and (G3) at `k-1`. This tests separated levels, not just consecutive walls. Under (G2), a lower wall cannot approach a higher wall within a fixed patch radius in the higher wall's own scale.

## 3. A cover with overlap bounded across all depths

**Discharged (geometric lemma, conditional only on (G3),(G2)).** The following construction is in the maximum norm on the periodic covering space; periodic cubes use their periodic images. Set `b=1000R` and define the scalar function

```
h(x)=sup_y {sigma(y)-dist(x,y)/b},       r(x)=R h(x).
```

The supremum includes `y=x`, so `h>=sigma>0`. The triangle inequality proves `|h(x)-h(z)|<=dist(x,z)/b`, hence `Lip(r)<=1/1000`. If `x` has scale `s_k` and `y` has scale `s_m>=s_(k+2)`, then `x in F_(m-2)` and `y outside F_(m-1)`. By (G3), their distance is at least `t_0 s_(m-2)/4>=2b s_m`. Such a `y` contributes a negative number to the supremum. All remaining `y` have scale at most `Ls_k`. Therefore

```
sigma(x) <= h(x) <= L sigma(x).
```

Continuity now gives `h=s_(l+1)` on `boundary F_l`: approach from the finer side for the upper bound and from the coarser side for the lower bound. Choose disjoint cubes `Q_i` of radius `r_i=r(x_i)` by processing candidate centres in decreasing radius. On a finite fine lattice this is a finite greedy construction. Every rejected centre is in `2Q_i` of an intersecting chosen cube. Interpolate on fine cells and enlarge by one fine cell where needed; `R>=10` leaves room in `3Q_i`. At any `x in 10Q_i`, `|r(x)-r_i|<=r_i/100`. Thus all these radii lie between `r(x)/1.01` and `r(x)/.99`. The disjoint `Q_i` lie inside a cube of radius `12r(x)`, each with radius at least `r(x)/1.01`. Comparing their volumes bounds their number by

```
N=16^4.                                               (G4)
```

This is a total multiplicity bound, with no count of levels. On a periodic box a cube larger than a period is interpreted as the full circle in that coordinate; the same comparison uses capped lengths, whose enlargement ratio only decreases. Greedy choices and volumes are made on the torus, not counted repeatedly over images.

On `10Q_i`, `h` varies by at most `r_i/(100R)=h(x_i)/100`. Two distinct level boundaries there would have `h` values with ratio at least `L`, contradicting this variation for `L>=2`. Thus each enlarged patch has at most one scale jump. It can contain several facets of that one boundary, handled by the source's brick extension premise, rather than by a new assertion that every patch is a planar half-space.

Choose piecewise linear scalar cutoffs `theta_i=1` on `2.5Q_i`, zero off `3Q_i`, with Lipschitz constant `2/r_i`, and set `chi_i=theta_i/(sum theta_j^2)^(1/2)`. The extra half-radius covers the fine-cell interpolation; the denominator is at least one. Differentiating this finite expression gives `sum chi_i^2=1` and `|D chi_i|<=C_N/r_i`, for instance `C_N=10N`; the same bound for lattice differences follows by integrating along the edge. All enlargements for row supports and bumps below stay in `10Q_i` after increasing the absolute lower choice of `R`.

**Implication (relation to the source weight).** This proves an explicit cover after the strengthened geometry choice, not the original assertion with unexplained patches. The weight `h` is a smooth majorant of `sigma`, within a factor `L`. It is bounded above by the source's step weight `s^#` if the wall collar in that definition is enlarged to `b` coarse cells: any contribution from a larger scale to `h` must come from within that distance. Consequently a bound on `||H/h||` implies the corresponding (NC) bound with that enlarged collar. The parameter of the cover and the collar differ by a fixed factor, which must be retained when choosing `t_0`; they are not silently set equal.

**Unchecked (scope).** This cover does not certify a nest with a missing top collar, a skipped jump admitted without its intermediate regions, or an arbitrary independently shifted brick tiling. These are domain questions for the consumer, not repaired by bounded overlap at each scale. No such enlarged domain is declared refuted.

## 4. The flat cutoff calculation, including constraint restoration

**Discharged (normalizations and the uncorrected error).** Work at `U=1`. Put `S=h(x_i)` on a patch, `R_i=RS`, and `Lip(chi)<=c_chi/(RS)`. A retained row `c` of side `sigma_c` has nonnegative box/triangle kernel `rho_c`, integral one, support in its two endpoint blocks. Write `q_c=C_c(chi H)-chi(z_c)C_c H`. For `C_NH=0`, this is the entire constraint error. Since the support has diameter at most `8 sigma_c`,

```
|q_c| <= 8 c_chi sigma_c/(RS) integral rho_c |H|,
sigma_c^-2 |q_c|^2 <= 64 c_chi^2/(RS)^2 integral rho_c |H|^2.    (C1)
```

The factor `sigma_c^-2` in `Lam` cancels exactly the squared oscillation of the cutoff. At a given scale the density-weighted row kernels have overlap at most `8` in dimension four. On a patch there are at most two relevant scales. Hence

```
||q||_Lam^2 <= 1024 c_chi^2/(RS)^2 ||H||_(P+)^2.        (C2)
```

Rows cannot be arbitrarily coarser than this patch: if a retained row of side `sigma` touches `3Q_i`, its leaf endpoint is within `8 sigma` of a point there; the definition of `h` gives `h>=sigma(1-8/b)` at that point. Thus `sigma<=2S` after the small variation of `h` on the patch is included. The row support and an assigned leaf bump fit inside `10Q_i` for the large fixed `R` chosen below. This checks support enlargement, rather than counting just row base points.

**Discharged (local two-scale right inverse).** Here are the finite ingredients behind the bumps used in `fd-jumps.md:139–205`. In unit block coordinates put `b(t)=max(0,1-4|t-1/2|)`, `p=b/avg(b)`, `a=avg(tp)`, `v=avg((t-a)^2p)`, and

```
psi_- = p[1-a(t-a)/v],
psi_+ = p[1+(1-a)(t-a)/v].
```

The average is the actual lattice average. Expansion gives respectively the moments `(1,0)` and `(0,1)` against `(1-t,t)`. With at least 32 sites, `avg(b)>=1/16`; the two intervals `[5/16,3/8]`, `[5/8,11/16]` each have `p`-mass at least `1/128`. In the identity `v=(1/2)avg_(t,u)p(t)p(u)(t-u)^2`, these two intervals give `v>=2^-18`. Thus the functions and their first derivatives have fixed bounds, for example `2^22,2^25`. Tensor with `p` in the three other directions and put the result in the row's bond component. Its support is inside its assigned leaf, and it separates the two incident same-scale rows. A finest identity row uses its bond indicator. There is no intermediate small block size: when `L>=32`, a nontrivial scale above the fine spacing has at least 32 sites.

Assign each retained row to a leaf endpoint, at most eight rows per leaf. Distinct leaf interiors are disjoint; first differences of the supported bumps have at most eight neighbouring supports. Since `|p|<=16`, `|p'|<=64`, each tensor bump has size at most `2^34` and each coordinate derivative at most `2^37` in unit coordinates. Cauchy–Schwarz over the four derivative directions, eight assigned rows, and eight neighbouring supports is bounded by an additional factor `2^10` in norm. Thus the deliberately loose common constant `K=2^120` suffices for the mass and gradient bounds of each single-scale lifting `R_sigma`:

```
||R_sigma y|| <= K ||y||_N,
||grad R_sigma y|| <= K sigma^-1 ||y||_N.
```

Let the two scales be `h_0=S_0/L,S_0`, with `S_0<=2S` and comparable to `S` when a wall is met. First set `B_f=R_(h_0)q_f`, then

```
B_c=R_(S_0)(q_c-C_c B_f),       B=B_f+B_c.              (C3)
```

Coarse leaf bumps meet no retained finer row, and (C3) corrects every coarse row touched by the fine bumps, including rows initially having zero error. Hence `C_NB=q` exactly. This is a two-step triangular operation, not an iteration over depth. Jensen and the two-fold longitudinal overlap give `||C_c B_f||_N<=sqrt(2)||B_f||`; in the weighted row norm the off-diagonal operator has norm at most `sqrt(2)K/L`. For `L>=4K`, increasing the constant to `K_*=16K^2` bounds the lift by

```
S^-2||B||^2+||grad B||^2 <= K_*^2 ||q||_Lam^2.         (C4)
```

Only a bounded number of leaf neighbours is added to the support. On a patch with no wall the same formula has just one term. Equations (C2),(C4) prove an error `<=1024 K_*^2 c_chi^2 R^-2 ||H/S||_(P+)^2`. They prove neither that `chi H` satisfies the rows nor that an arbitrary solution of the local saddle problem has compact support. The corrected field is `H_chi=chi H-B`.

**Discharged (the gauge projection, flat case).** Write `phi=D*H`, `c_B=avg_B phi` on a leaf of side `sigma`. Choose a tensor tent `g_B` supported in `B`, of mean `sigma^2 c_B`. Its normalization above gives, with the same enlarged `K`,

```
||g_B|| <= K sigma^2 |B|^(1/2)|c_B|,
||Dg_B|| <= K sigma |B|^(1/2)|c_B|.
```

At the finest leaf the site indicator gives these estimates including its adjacent bonds. Since `r_Ng_B` has only its one nonzero leaf mean, exact summation by parts yields

```
sigma^2 |B| |c_B|^2
 = <g_B,phi>-<P_N g_B,P_N phi>
 = <Dg_B,H>-<P_N g_B,P_N phi>.
```

Dividing proves `sigma |B|^(1/2)|c_B|<=K(||H||_(B+)+sigma||P_N phi||_B)`. If `phi=c_B+phi_0` on `B`, direct expansion of `[P_N,chi]phi` gives a constant-mean term `(chi-avg_B chi)c_B` and the constant function `-avg_B((chi-avg_B chi)phi_0)`. Therefore

```
||[P_N,chi]phi||_B
 <= 2 osc_B(chi)(|B|^(1/2)|c_B|+||P_N phi||_B)
 <= C K c_chi/(RS) (||H||_(B+)+sigma||P_N phi||_B).     (C5)
```

Summing over disjoint leaves, with at most eight neighbours for their fine differences and `sigma<=2S`, bounds its square by `C K^2 c_chi^2 R^-2 (||H/S||_(P+)^2+||P_Nphi||_(P+)^2)`. This is the term lost by replacing the gauge projection by an ordinary divergence. It is not an extra bound for each level.

**Discharged (Eps and ordinary differential commutators).** The scaled norm needed for the bump is `||B||_(Eps,S)^2=S^-2||B||^2+||grad B||^2`, not a uniform bound for `||grad H||` by the global graph norm across a wall. The product rule gives `||d(chi H)-chi dH||<=C c_chi(RS)^-1||H||` and the corresponding divergence estimate. Moreover `||dB||<=sqrt(6)||grad B||`, `||P_ND*B||<=2||grad B||` in dimension four, by Cauchy–Schwarz over their component sums. Thus (C4),(C5) control every flat derivative error. The replacement of `P_ND*` by `D*` would change both the estimate and the class problem.

**Implication (flat IMS closure, given the one-jump coercivity premise).** Set `E(H)=||dH||^2+||P_ND*H||^2`, `W(H)=||H/h||^2`. Let `C_0>=1` be the one-jump constant, enlarged by four for the possible change from its coarser scale to `S_i`. A safe explicit error constant is `A=2^30 K_*^2 C_N^2`. For example the bound in (C5) follows with `16K c_chi/(RS)` in front of its parenthesis; squaring and summing its at most eight neighbours costs less than `2^16 K^2 c_chi^2 R^-2(W+E)`. The correction costs `2^10 K_*^2 c_chi^2 R^-2 W`, and the finitely many curl/divergence product terms and squared triangle inequalities fit below the displayed `A`, with `c_chi=C_N`. These constants are absolute once `L>=4K`. Put `e=AN/R^2`. Total overlap gives

```
W <= 4 sum_i S_i^-2 ||H_i||^2 + e W,
sum_i (||dH_i||^2+||P_ND*H_i||^2)
 <= 2 E + e(W+E).
```

The first follows from `chi_i H=H_i+B_i`, the squared triangle inequality and `h/S_i` between `.99` and `1.01`; the second follows by the same inequality and `sum chi_i^2=1`. The localized projection equals the global projection on every leaf touched by these fields. Apply one-jump coercivity to each `H_i`; a wall-free patch uses the uniform-scale special case. Choose `R^2>=100(1+C_0)AN` before choosing `L,t_0`. Then the coefficient of `W` to absorb is `(4C_0+1)e<1/20`, and the coefficient of `E` is `8C_0+4C_0 e`. Dividing gives `W<=16 C_0 E`. This is a **conditional flat coercivity result on (G3)**. It does not assert the full curved saddle theorem or identify every consumer's data with this domain.

**Discharged (why no strengthened Cauchy–Schwarz is needed here).** At a fine bond, at most `N` enlarged patches contribute; hence `|sum_i B_i|^2<=N sum_i |B_i|^2`, and the same count applies to their fine differences after the already reserved support enlargement. There is no factor for the number of scales. If the compact support in (C3) is replaced by global one-jump inverses, this argument disappears. `ue-multilevel.md:238–284` proves a scale gain only for pieces with both `||v_s||<=2s||Dv_s||` and `||D*Dv_S||<=J/S||Dv_S||`; integration by parts gives `2J(s/S)`. Arbitrary saddle outputs or cutoff corrections have not been shown to satisfy that inverse estimate. In particular putting the same nonzero fine oscillation in two levels makes their normalized correlation one. Using that section's conclusion without its hypotheses would not repair overlap at depth.

## 5. Gauge, curvature, and the specific unresolved inequality

**Discharged (what survives at a background without an estimate).** A real scalar cutoff commutes with every adjoint transport. On an oriented edge, expanding `D_U(chi v)` gives `chi D_Uv` plus the scalar difference of `chi` times one transported endpoint value. The same expansion on the finitely many legs of a plaquette proves the covariant curl product rule, with the same Lipschitz cost as at `U=1`. The site projector `P_U=1-r_U^*(r_Ur_U^*)^-1r_U` remains diagonal over leaf blocks whenever the indicated block Gram operators are invertible. Scalar multiplication does not commute with that projector or with `C_U`. If `U_xy=g_x g_y^-1`, conjugating every site and bond by `Ad(g)` carries all the flat calculations to this background isometrically. Pure gauge backgrounds are therefore covered exactly.

**Gap (one local inequality, not (UE), (WP), or F-D).** Here is the first analytic estimate this route still needs at nonzero curvature. It is stated on **one** two-scale brick wall, so it can be tested without constructing a several-jump extension or assuming the full consumer geometry.

Take a patch `P` of radius `RS`, with `P+` its maximum-distance `32S` neighbourhood and `P++` its `64S` neighbourhood; both enlargements must stay in the same one-wall model. The two leaf scales are `S/L,S`; if no wall is met, allow one uniform scale `sigma` with `S/L<=sigma<=S`. At a wall the cover's `h(x_i)` and the actual coarser scale differ by at most a fixed factor, which is absorbed in the cutoff constant. Use the actual pruned bond rows `C_U`, covariant site averages `r_U`, and `P_U` of that model. Let `chi` be supported in `P`, `0<=chi<=1`, `Lip(chi)<=c_chi/(RS)`, and `C_UH=0` on every row whose support meets `P++`. The background is an actual compatible stationary class-fill background, with the (NC) local curvature hypothesis: in coordinates rescaled by `S`, curvature has the stated small `L^4` norm on unit boxes. In physical coordinates the dimensionless quantity is `S||F_U||_(L^4(B_S))`; this is bounded by `C a_*`, with the source's local-scale interpretation. No pointwise curvature bound is substituted.

For all such inputs, the required inequality is

```
inf_B { S^-2||B||^2 + ||grad_U B||^2
                    + ||[P_U,chi]D_U*H||^2 }
 <= A_loc/R^2 { S^-2||H||_(P++)^2
                         + ||P_U D_U*H||_(P++)^2 },    (LC_U)

supp B subset P+,
C_U B = C_U(chi H) on every model row,
A_loc absolute for L>=L_0,
a_* <= a_loc(L,R), with R chosen before L.
```

The projection term is independent of the infimum; it is included to prevent a purported correction estimate from dropping the gauge error. All norms on the left include their full support. The support constraint is part of the assertion. A global right inverse with a bounded norm does not prove it. `(LC_U)` is **discharged at `U=1`** by (C2)–(C5), for example with `A_loc=2^30 K_*^2 c_chi^2`, and at pure gauges by conjugation. At genuinely curved backgrounds it is a gap here.

**Discharged (why the flat proof is not already a curved proof).** In (C5) the identity testing the leaf mean uses a site bump with exactly that covariant mean and with controlled covariant derivative. Replacing the flat bump by contour transport differentiates those transports. Around a fine plaquette the two transports differ by its holonomy; this term vanishes for a pure gauge and contains curvature otherwise. Small curvature in `L^4` is not the assertion that its value on every path is uniformly small. The source supplies a proposed repair through (R3): `fibre-propagator.md:192`, point (6'), explicitly says the pointwise curvature bound fails and invokes the summable estimate `theta_j<=s_j ||F||_(L^4)` in local units. What has not been written here is the resulting **support-preserving** bound for the two-scale bump matrix and the covariant mean test in `(LC_U)`, in its density and `Lam` normalizations. Treating a fixed perturbation as small at every level would allow its sum to grow with depth; the needed summation has to be inside this local estimate.

**Unchecked (expectation, with reason).** I expect `(LC_U)` to be true for the source's actual class-fill/R3 backgrounds after reducing `a_loc(L,R)`. The flat moment matrix has an explicit right inverse above, there are only two active scales, the protected leaf supports give finite support rather than inverse tails, and the source's proposed contour estimate has a geometric sum of scale lengths. This is a reason for a perturbation argument, not that argument. I do not expect arbitrary fields in an Eps ball to suffice: point (6') expressly distinguishes them from R3 backgrounds. Whether small curvature alone, without those class-fill premises, implies the required contour estimates is not claimed.

**Implication (what this inequality would buy).** Given the local one-jump coercivity and local background form estimates asserted by the source, `(LC_U)` replaces (C4),(C5) in the flat IMS calculation. The ordinary covariant product rules were proved above. The curvature error in comparing the actual stationary constrained Hessian with its positive part must still have the source's form `C(L)a_*` times the localized graph energy; choose `a_*` after `L,R` to make it at most, say, `1/(100C_0)`. This use is conditional on that form estimate, including the multiplier term. One must not replace the Hessian by curl squared: `d_U D_U omega` contains `[F_U,omega]`. The exact Ward identity and stationarity are the source's Lemma Inv, not a property of a scalar cutoff.

After these hypotheses, the same `A_loc N/R^2` absorption gives the coercivity portion of several-jump F-D on the covered domain. Inf-sup and weighted conjugation still require their own row and background estimates. At flat background their depth-free mechanisms are the leaf assignment and triangular geometric series in `fd-jumps.md:139–205`, and the row/mean commutators at `206–273`. Those statements are not reclassified as independently checked curved results by this note.

**Discharged (the exact gauge test, conditional on an inverse and Ward identity).** Suppose the saddle has been inverted, the stationary constrained Hessian obeys `bH[H,D_U omega]=0` for `omega in ker r_N`, and the source `J` annihilates these directions. Testing its equation by `D_U omega` gives `<P_ND_U*H,P_ND_U*D_U omega>=0`. The operator `P_ND_U*D_UP_N` has quadratic form `||D_U omega||^2` on `ker r_N`. If it has trivial kernel there, choose its inverse applied to `P_ND_U*H`, obtaining `P_ND_U*H=0`. On a finite lattice trivial kernel follows because `D_U omega=0` means parallel transport of one vector throughout each connected component, and its covariant block mean is that vector in the block root frame; zero means force it to vanish. This identifies the class solution once invertibility is supplied. It does not prove coercivity, a uniform inverse bound, or `(LC_U)`.

**Gap (Schur gluing has not removed the same local issue).** For a candidate parametrix made from local saddle inverses, the row of `S_N(chi_i H_i,chi_i lambda_i)` contains `C_N(chi_i H_i)-chi_(i,c) C_NH_i`. This is exactly the moment error (C1), now with a curved kernel. Its gauge block also contains `[P_N,chi_i]D_U*H_i`. An operator Schur test would have to bound these errors and the tails of their correcting responses in the correct weighted norms. The one-jump inverse has exponential tails, not the compact support used in (G4). No such weighted Schur estimate is proved here. This is not a proof that Schur gluing fails; it explains why merely naming that test does not yet bypass `(LC_U)` in the attempted construction.

**Discharged (strictly smaller target).** `(LC_U)` asks for bounded local lifting of a very special right-hand side, the commutator of a scalar cutoff with the constraint rows, plus a local gauge commutator bound. It has one wall, two scales, and no quantification over an increasing number of walls, no extension of prescribed values throughout the nest, no inversion of the Hessian, and no exponential-decay conclusion. Its flat case is explicit. Thus settling it is a genuine smaller next calculation for this localization route, even though the consumer-domain and inherited-background qualifications recorded above would still have to be checked. This stop does not rename F-D, (UE), or a planar-frequency extension problem.

## 6. Fixed L: exactly which constants the consumers allow

**Discharged (source comparison; answer).** A depth-uniform `C(L)` is allowed for amplitudes and for perturbative costs paid by a later small threshold. A bound on the saddle inverse that gives **only** a rate `delta(L)>0` is not sufficient for the consumers as currently printed. They explicitly keep an absolute fast rate before choosing `L`. An absolute bound for the raw input coefficient norm is not itself a consumer requirement. These are three different assertions.

| Consumer | Decisive source line at this commit | Consequence |
|---|---|---|
| Theorem F-D | `fibre-propagator.md:162`: inverse “with an absolute bound”; `:5` and `:90–106` state the rate free of `L`, permitting `C(L)` in the chart kernel | A `C(L)` prefactor at an independently absolute rate is usable. A bare `C(L)` inverse estimate is weaker than the printed supplier. |
| `(MD*_1)` | `quiet-boundary-rarity.md:267` explicitly has `C(L)` times `x` and shell volume; `:271` sets `c_t=rho/3`. The interface, `parts/upper-chain.md:184`, says **“c_t>0 is absolute”**, while `c_s` may depend on the fixed parameters | The amplitude may depend on `L`; the unsuppressed first exponential may not be replaced by an arbitrarily slow one. |
| `(I_2^D)` | `quiet-boundary-rarity.md:277`: (H1) has `gamma(L)`, but (H2) reads F-D with layers **“with absolute rate”**; `:153` allows derivative constants `C_n(L)` | Fixed-`L` coercivity/amplitude constants alone do not supply its locality clause. |
| `(SCR_1)` | `parts/upper-chain.md:185`: `C(Theta)` prefactor, **“a_f>0 absolute”**, with `a_s` depending on `Theta` | The fast/rare-slow distinction survives screening. |
| K-transport | `library/history-budget-sum.md:287–295`: `2B_j Phi_j(k_m)+3 sqrt(tau_j(m))`; `parts/upper-chain.md:1444–1448` says kappa must not come down to the tail rate and defines the two-tier profile | Square roots halve the screening exponent. A slow unsuppressed term cannot be assigned the small rare-tier amplitude. |
| Order of constants | `parts/hard-core--mapped.md:24` puts `delta_#,rho_1,rho_f,...` **before `L>=L_0`**, then `a_*`, geometry, and `x_*`; `quiet-boundary-rarity.md:288` fixes these once, independent of depth | Later choices can pay finite amplitudes and small perturbations; they do not authorize resetting these already absolute rates to arbitrary functions of `L`. |

**Discharged (the operator distinction).** If `||S_N^-1||<=M(L)` and the conjugation error is at most `C_com delta`, the geometric-series argument only ensures invertibility when `M(L) C_com delta<=1/2`. It therefore supplies `delta<=1/(2M(L)C_com)`, not an absolute decay rate. This is a sufficient perturbation estimate, not a lower bound on the actual decay. A separate weighted inverse argument might still prove an absolute exponent with prefactor `C(L)`; the consumers would accept that exponent and prefactor. Increasing `x_*` cannot turn a term `C(L)exp(-delta(L)m)` into `C'(L)exp(-kappa m)` for unbounded allowed distances when `delta(L)<kappa`: division leaves `exp((kappa-delta(L))m)`. Volume and depth are not fixed after choosing `x_*`. The same observation applies with the halved exponent in K-transport.

**Discharged (what the raw-input example does and does not decide).** `ue-multilevel.md:91–101,153–193` gives a compatible family with raw weighted input cost at least `c L^2` times a bounded energy. It also tests the actual constrained field and obtains a flat Rayleigh quotient at least `8/9` on that family. Thus the example obstructs an absolute estimate for those raw coefficients; it does not obstruct an absolute saddle rate. The localization calculation above does not use those coefficients: its input is `C_U(chi H)`, whose extra factor `sigma/(RS)` cancels the `Lam` weight. In a proof that did use the raw coefficients, `C_in(L)` could harmlessly enter a **prefactor**, or multiply a later small `a_*`; it could not simply be allowed to degrade the only proof of the fast rate and then be declared sufficient by “L is fixed.” This is the answer for the current order of constants, without silently changing it.

## 7. Scope check on the negative conclusion

**Discharged (no-go discipline, narrowed to this file-only research task).** The pinned repository skill `docs/ai_methodology/skills/no-go-discipline/SKILL.md` was inspected. Its audit-packet, runner, ledger, commit and landing operations are outside the user's express scope; no packet status is claimed. The scientific checks relevant to the conclusion are:

1. **Alternative routes.** Attempted: the centred-patch clearance test, the graded cover with compact flat corrections, and the algebra of Schur gluing. The global extension and (WP) were deliberately not continued. These are not five certified distinct closed route families, and no five-route or exhaustiveness claim is made.
2. **Dependence of gaps.** The missing-top-collar question and `(LC_U)` are not asserted independent. One is a domain identification, the other a local estimate; neither has been proved to imply or exclude the other. The inherited one-jump/background premises remain explicitly conditional, not a count of new independent walls.
3. **Hidden premises.** Complete families, common brick tilings, (G2), the actual R3 background, pruned rows, and the local one-jump premise have all been stated. The interface's thicker `6t_0` layers (`parts/upper-chain.md:178`) are not automatically the `t_0`-thick layers of the mapped construction: their collars must be checked in (G3) too. The geometry repair is a proposed choice, not an edit to another source.
4. **Residual matching.** (G1) attacks an insufficient geometric inference; the raw `L^2` example attacks a coefficient norm; neither attacks the saddle inverse. The present unresolved estimate is `(LC_U)` on a single curved wall.
5. **Resolution of the claims.** Flat row identities and leaf-mean identities are per block; the overlap lemma is global over all depths on its stated domain; curved `(LC_U)` is unchecked. No kernel vector or diverging inverse family has been produced.
6. **Partial closure.** Enlarging `t_0` and pruning dependent rows are mathematical/domain choices, not new physical axioms. The former repairs the small-clearance example; the latter avoids the artificial multiplier kernel already identified in `fd-jumps.md:135`.
7. **Steelman.** A successful proof could transport the explicit flat leaf bumps, bound their two-scale covariant moment matrix and the mean-test derivative using the R3 contour estimates, and preserve their supports. That would establish `(LC_U)` and let the displayed IMS estimates proceed once the consumer's top collars are verified. This mechanism remains open, so a claim that localization cannot work would be premature.
8. **Earlier failures.** The sequential extension's per-depth factor in `fd-jumps.md:59–89` does not occur in (C3), which has just two active scales per patch. Section 6 of `ue-multilevel.md` warns correctly that zero means alone do not produce scale orthogonality. Both comparisons support the narrower stop; neither is evidence for impossibility.

## 8. Recovery record and decision

**Discharged (saved results).** The precise clearance units, the near-two-wall family (G1), the repair (G2), the total-overlap cover on (G3), the flat constraint correction, the flat gauge commutator, and the conditional flat IMS estimate are written above. The consumer question is settled at the level of their printed quantifiers: fixed-`L` amplitudes are permitted, while their fast rate remains absolute. The next analytic target is `(LC_U)`, expected true under the actual R3 premises. The next domain check is the top collar of recursively truncated families, including the interface's layer thickness. Neither should be replaced by reopening (WP).

**Unchecked (verification limits).** This is an author calculation using the configured Codex runtime, with exact model identifier and effort unavailable; the target's model-floor setting therefore cannot be independently certified here. The one-jump theorem and the covariant/background suppliers have not received an independent proof check in this session. No computer-assisted mathematical step, numerical search, audit, subagent, commit, push, PR or external post was used. Tool calls only inspected sources, edited this file, or checked file scope and formatting. Some initial search outputs were truncated; they supply no completed verification. The load-bearing passages used here were subsequently read in bounded ranges.

**Discharged (source record).** Pinned source: `15c601852769bba50f1198cd5f7b01717b45066b`. Read `GOAL.md:1–83`, the required `FINISH.md:110–139`, and the pinned workflow blob. Mathematical reads: `fibre-propagator.md:1–106,108–174,186–196`; `fd-jumps.md:1–100,120–273,301–314,340–390`; `ue-multilevel.md:1–194,238–331`; `joint-induction-two-step.md:23–61,127–161`; `quiet-boundary-rarity.md:13–51,149–154,259–294`; `block-poincare-energy-package.md:47–59`; mapped `:22–25,937–951`, plus targeted search lines; upper-chain consumer/interface `:178–186,1232–1307,1444–1473`, plus targeted search lines; `history-budget-sum.md:266–324`; `generated-observable-history.md:425–469`; `far-difference-two-rate.md:156–169`. Other allowed library searches returned only targeted lines in `induction-with-boundary-data.md`, `current-locality-reduced-law.md`, and `one-step-closure.md`. The upper-chain 20.1 range included its comparison of earlier independent-map arguments; none of that comparison is used as a proof input. No forbidden file or gate was opened. The Sussman–Alpoge repository was not read. The installed physics-loop entry point was inspected for applicability; its campaign was not invoked. The pinned no-go skill and freshness instructions were inspected as recorded above. Final source checks found the same HEAD and no tracked source changes; the only new file is this note. Its complete text was reread, and the whitespace check reported no errors. These are editing checks, not mathematical certificates.

**Gap (decision).** No proof of several-jump F-D in the full curved consumer domain has been obtained. No admissible saddle kernel or diverging inverse has been constructed, and the repairable geometric example does not refute localization. The route-specific stopping inequality is `(LC_U)`, with its flat case established, its precise curved domain stated, and its smaller scope and positive expectation explained in section 5.

STOPPED
