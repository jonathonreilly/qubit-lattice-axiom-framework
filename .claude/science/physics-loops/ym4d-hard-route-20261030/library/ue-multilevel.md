# Simultaneous extension: testing the multilevel input
Provenance: OpenAI/Codex (GPT-6 family; exact runtime model identifier and effort setting are not exposed to this session), commit `4ccc0b688a47f462c0ce2ce902b1f7ddb93ea227`; mapped-side research text, not an audit; no status is granted.

## 1. Contract, sources and conventions

**Discharged (scope).** This item concerns (UE) in `fd-jumps.md`, Section 6, and the proposed simultaneous multilevel construction. The required parts of `GOAL.md` and `FINISH.md` were read first. No file on the independent side, forbidden library file or gate was opened. Only this note is written. Source inspection and file writing are the only uses of the computer; no mathematical assertion is discharged by a run.

**Unchecked (inherited premises).** The one-jump extension, torus decomposition, brick geometry and background estimates of `fibre-propagator.md` are research premises. Their labels in that source are not independent verification here. The workflow file is absent from the sparse working tree but present in the pinned commit; its blob was inspected. The installed physics-loop instructions were inspected for applicability; the user's single-file, no-audit, no-delegation contract overrides their campaign and delivery operations.

**Discharged (notation).** Work first at `U=1`, in potential normalization on a periodic fine lattice of spacing `eta`, in dimension four. `D` denotes the gradient divided by `eta`; all fine inner products have weight `eta^4`. Set `s_n=1` and `s_l=L^(l-n)`. A site block average `r_l` has density weight `s_l^4`. At the flat background,

```
Q_l D = D_l r_l,
r_(l+1) = A_l r_l,
```

where `A_l` averages the `L^4` children. These identities follow by telescoping the path sums in mapped Text 3.1. The bond average has a triangular weight in its bond direction and box weights in the other directions. Distinguish this bond average from the site average throughout.

**Discharged (precise domain).** The retained tree in `fd-jumps.md`, Section 4, replaces a refined block by all its children. Its leaves partition the fine sites. A retained bond row connects two present blocks of the same size with at least one leaf endpoint. Parent bond rows with two refined endpoints are recovered by composition, not retained as independent multipliers. `r_N` reads leaf site averages. Thus a full-grid sum over every scale is a different quantity from a sum over retained data near the layers.

**Gap (target under test).** For the actual compatible pairs,

```
Q_n H_s=0,       P_n D*H_s=0,
r_n omega=0,    C_N(H_s+D omega)=0,
```

the proposal needs control of the weighted differences of prescribed site averages before any strengthened Cauchy--Schwarz estimate can help. Whenever a parent value is compared with a child value, its pullback is the constant parent value on that child; averaging in the opposite direction is `A_l`. No value on an unprescribed child may silently be counted as prescribed data.

**Unchecked (memory attribution).** The BPX/Oswald/Dahmen--Kunoth comparison and strengthened Cauchy--Schwarz strategy are the user's explicitly memory-sourced suggestion. No theorem under those names is used as a premise. The calculations below must distinguish raw box-average differences from residuals after a smooth coarse reconstruction.

## 2. First kill attempts: what can actually be counted

**Discharged (a tempting but inapplicable divergent sum).** Let a one-dimensional parent have side `Ls`, its child centres be `x_j=x_P+s(j-(L-1)/2)`, and let the sampled site function be `u(x)=a x+b`. Its child mean minus its parent mean is `a s(j-(L-1)/2)`. Consequently

```
(1/L) sum_(j=0)^(L-1) s^-2 |d_j-d_P|^2
    = |a|^2 (L^2-1)/12.
```

The identity follows from the sums of the first `L-1` integers and their squares. Counting *all* child blocks at each of `m` refinement levels on a region of fixed volume therefore gives `m` times this number per unit volume. This rejects a raw full-tree Haar bound on general `H^1` functions. It is not a counterexample to the proposed retained input estimate: the coarse internal rows in such a fully refined region are redundant and have been pruned. The affine function also does not, by itself, supply a periodic compatible pair. Neither defect can be waived.

**Discharged (zero-source attempt is impossible).** Suppose `H_s=0` and all four constraints in Section 1 hold. Every present bond row has zero gradient of the corresponding site data: a row with a leaf endpoint is retained, and a row with two refined endpoints is recovered from its children. In a refined parent the children form a connected Cartesian grid, so their means are equal. Starting with zero top means and descending the tree gives zero means on every leaf. Thus arbitrary choices of constants on nested frozen pieces do not give a counterexample; the parent constraints eliminate them. This says nothing about nonzero `H_s` until it is estimated.

**Unchecked (nonzero-frequency attack, before the estimate).** A harmonic normal profile times a tangential oscillation is the next possible threat: it can be cancelled by a divergence-free `H_s` on the frozen region, unlike an arbitrary scalar profile. Such a profile is developed explicitly in Section 4. For fixed tangential frequency its retained layers occupy different physical volumes; the full-tree calculation above cannot be reused by counting their common interior repeatedly. The estimate in Section 3 rules out a divergent *retained* raw-input sum for every such compatible family, including frequencies and wall spacings depending on depth.

## 3. The raw retained input is bounded at fixed L

**Discharged (definition of the sum).** A present block `B` of side `s` has datum `d_B=avg_B omega`. If it is not a top block, let `P(B)` be its immediate tree parent, of side `Ls`, and set `e_B=d_B-d_(P(B))`. For a retained bond row `c=(B,B')` at scale `s_c`, put

```
I_raw = sum_c s_c^(4-2) (|e_B|^2+|e_B'|^2),
```

omitting top endpoints, whose data are zero. Endpoint occurrences may be repeated in this definition. It dominates the corresponding site sum with each retained endpoint counted once, and in particular the leaf-site version of the input asked for. The norm is a density norm, not counting measure. This is the literal difference of given child and parent means; it is not a residual against an interpolated parent function.

**Discharged (all internal child edges are available).** In any refined parent `P`, all its `L^4` children are present. For an edge between two children, either it is retained, or both children are refined. In the latter case the composition formula for `Q` expresses that row as a weighted sum of rows between their descendants, with support contained in the two endpoint blocks. Repeating reaches retained rows after finitely many steps. No estimate is made in this recursion: it is an identity. Therefore the actual constraint gives, on every internal child edge,

```
(d_(B+se_mu)-d_B)/s = -(Q_s H_s)(B,mu).             (3.1)
```

This also proves the claim about recovered edges used in Section 2. Only `C_N(H_s+D omega)=0` is needed here; imposing the other three hypotheses narrows the domain further.

**Discharged (pointwise parent comparison).** The following deliberately loose estimate avoids all scale summations. In dimension `d`, choose for each child `K` of `P` a coordinate path from `B` to `K` inside the child grid. Average the telescoping identity over `K`, take absolute values, and bound the multiplicity of each edge by the total number `L^d` of paths. This gives

```
|e_B| <= s sum_(c internal to P) |Q_s H_s(c)|
       <= 2d s^(1-d) integral_P |H_s|.              (3.2)
```

Here a fine bond component is represented on its starting fine cell. Each flat row weight is nonnegative, at most `s^-d`, and supported in the union of its two endpoint blocks. At a fine cell at most two such rows per direction contribute. This proves the second inequality, including rows recovered rather than retained. The finest identity rows obey the same bound. Boundary placement changes no constant if half-open fine cells and oriented bonds are used consistently.

Assign each retained row `c` to one of its leaf endpoints `F_c`. Distinct leaf blocks are disjoint and a leaf is assigned at most `2d` rows. For either endpoint `B` of `c` and any `x` in `F_c`, a cube centred at `x` of side `4Ls_c` contains `P(B)`. If `M` denotes the centred cube maximal average of `|H_s|`, (3.2) yields

```
|e_B|/s_c <= A_d L^d M|H_s|(x),
A_d = 2d 4^d.                                      (3.3)
```

The endpoint need not itself be a leaf. This is why this estimate also covers the refined endpoint of a wall row.

**Discharged (the needed maximal estimate, rebuilt).** For completeness, `||Mf||_2^2 <= 8*5^d ||f||_2^2` is sufficient. For a finite collection of cubes with averages exceeding `t`, choose largest disjoint cubes successively. Every rejected cube is contained in the triple of a chosen cube. Enlarging to factor five accounts for fine-cell boundaries, so the union has measure at most `5^d ||f||_1/t`. On a torus use the periodic distance and cap cubes at the torus size; the same enlargement-volume bound holds. The estimate for any finite subcollection passes to the supremum. The part `|f|<=t/2` has maximal average at most `t/2`, hence

```
|{Mf>t}| <= (2*5^d/t) integral_(|f|>t/2) |f|.
```

Integrating `2t` times this bound over `t>0` and interchanging nonnegative integrals gives the stated `L^2` bound. This is the covering argument recalled from memory in `fd-jumps.md`, Section 5, rebuilt here; it is not a citation to a multilevel norm theorem.

**Discharged (input conclusion, with constants).** Square (3.3), integrate over the assigned leaf of volume `s_c^d`, sum the two endpoints and then the rows. The overlap is only that of assigned leaves, at most `2d`. Therefore

```
I_raw <= 32d 5^d A_d^2 L^(2d) ||H_s||_2^2
      <= C_in(L) ||H_s||_Eps^2,
C_in(L) = 32*4*5^4*(8*4^4)^2 L^8.                 (RI)
```

This constant is independent of fine spacing, volume, number of jumps, and tangential frequency. No assumption that a wall has zero tangential frequency entered (3.1)--(3.3). In particular a nonzero-frequency family with jump ratios equal to `L` cannot make this retained sum diverge with depth while its `H_s` energy stays bounded. If a row skips `q` unrepresented levels and is compared directly with an ancestor `L^q` times larger, the displayed proof uses `L^q` in place of `L`; the immediate-parent formulation in the question does not skip those intermediate site averages. This distinction matters if jumps are allowed to skip levels.

**Discharged (scope of the constant).** (RI) is uniform in depth at fixed `L`. The compatible example below shows that an absolute constant for this raw input norm would be false as `L` increases: its necessary growth is at least `L^2`. A negative power of `L` in off-diagonal pairings does not remove that diagonal cost. This concerns this coefficient norm, not the infimum in (UE).

## 4. A compatible nonzero tangential mode, and the saddle test

**Discharged (exact lattice family).** This construction tests the four constraints simultaneously. Take a rectangular torus with integer side lengths in top units, a normal coordinate `x`, and tangential coordinate `y`. Let `eta^-1` be an integer at least 32, `z=exp(2 pi i eta)`, and

```
k_eta^2 = (2-z-z^-1)/eta^2,
zeta+zeta^-1-2 = eta^2 k_eta^2,       zeta>1.
```

The positive root exists explicitly from the quadratic equation; no numerical value is used. Choose a fixed slab `Omega`, made of whole top blocks, containing all the finer row supports of a permitted planar nest. On a slightly larger slab put `a_j=zeta^(j-j_*)`, with `j_*` at its right edge. Choose a fixed twice continuously differentiable cutoff `chi(x)`, equal to one on that larger slab and zero away from a still larger slab before the torus seam. Let `a` and

```
psi_j = -(a_(j+1)-a_j)/(1-z^-1)
```

be multiplied by such cutoffs outside the larger slab; inside it keep these displayed exact values. The cutoffs can be polynomials on fixed-width transition intervals, with value and first two derivatives matched to zero at their exterior ends. Define globally

```
omega(j,k) = a_j z^k,
H_s,x(j,k) = (1-z^-1) psi_j z^k / eta,
H_s,y(j,k) = -(psi_j-psi_(j-1)) z^k / eta,
H_s,3 = H_s,4 = 0.
```

The real or imaginary part gives real data in any fixed Lie-algebra direction. Backward differences commute, hence `D*H_s=0` exactly, including the cutoff region. In `Omega`, the recurrence for `a` gives

```
H_s,x = -D_x omega,
H_s,y = [(2-z-z^-1)/(1-z^-1)] a_j z^k / eta
      = -D_y omega.
```

Every top site average vanishes because `sum_(k=0)^(eta^-1-1) z^k=0`. Every component of `Q_n H_s` also vanishes: the `y` weight is a box factor for the `x` component and contains a box factor for the `y` component. All finer retained rows are supported where `H_s+D omega=0`; exterior top rows vanish by the same tangential averaging. Thus all four hypotheses of (UE) hold, for any permitted refinement tree confined to this slab. In particular lower walls can have any permitted separations and any number of jumps. The geometry is not being inferred from a spectrum: select an admissible planar nest first and put its finite collection of row supports inside `Omega`.

For an explicit fixed-width nested-wall layout, take even `L>=32`, `h_j=L^-j`, and a planar coarse front at `x=a_0`. Put `a_j-a_(j-1)=(t_0/2)h_(j-1)` and let its level-`j` layer have thickness `t_0 h_j`. All front positions lie within `t_0/[2(1-L^-1)]` of `a_0`. The lower layer lies inside its predecessor; its inward clearance is `(t_0/2)h_(j-1)`, exceeding `(t_0/3-2t_0/L)h_(j-1)`. Its displacement is at least `3t_0 h_j` and at most `(2/3)t_0 h_(j-1)`, the flat versions of (N) and (B). With `t_0` a multiple of `8L`, every face is on the required parent grid and brick grid. Use a second widely separated front to close the construction periodically. Refinement on these whole-parent slabs produces the pruned tree. A fixed slab covering the two fronts and their layers works for every depth.

**Discharged (uniform energies in a fixed slab).** Write `zeta=exp(kappa_eta eta)`. The defining identity is `sinh(kappa_eta eta/2)=sin(pi eta)`. Since `sinh t>=t` and `sin t<=t` for nonnegative `t`, `kappa_eta<=2 pi`. The latter inequalities follow by integrating `cosh t>=1` and `cos t<=1`. Also `|1-z^-1|/eta` lies between 4 and `2 pi` for `eta<=1/2`, by the chord lower bound for sine on `[0,pi/2]`. Difference quotients of the exponential profile through order three are bounded by constants depending only on the fixed slab width; integral representations of differences give the same bounds for the cutoff profile. These observations bound `||omega||_H1` and `||H_s||_Eps` by a constant independent of depth and `eta`. They do not depend on a continuum limiting calculation.

**Discharged (a nonzero top-grid tangential frequency is also possible).** For later use take two tangential frequencies `(p,2 pi)`, where the torus period allows `p=pi/2` or `p=pi`. Write `c_t=(exp(i q_t eta)-1)/eta`, `k_eta^2=sum_t |c_t|^2`, and choose the normal recurrence with this `k_eta`. Use two antisymmetric potentials

```
Psi_t = (c_t/k_eta^2) D_x a,
H_s,x = sum_t D_t^- Psi_t,
H_s,t = -D_x^- Psi_t,
```

all with their common tangential Fourier factor, and cut off the potentials outside the slab. Here `D^-` is the backward difference, so its symbol times `c_t` is `-|c_t|^2`. These formulas give `D*H_s=0` globally, and `H_s=-D omega` in the slab because `D_x^-D_x a=k_eta^2 a`. The `2 pi` tangential factor kills every top mean and every top bond average as before. All constants in the energy bound depend only on the fixed frequencies and slab. This provides actual compatible data in distinct eigenspaces of translation by one top unit in the `p` direction, without requiring the top mean of a lone `p` wave to vanish.

**Discharged (the absolute-L raw-input estimate fails on compatible data).** Use one refinement from parent scale one to `h=1/L`. Set `W=t_0/L`, an integer at least eight, and freeze the slab `-W<=x<0`. It is a union of whole parent blocks and a single row of fine-level bricks of physical side `W`; take all torus periods to be multiples of `W`, with normal period `4W`. Thus arbitrarily large prescribed brick sizes cause no problem. In the first, `2 pi`-frequency family put `a_j=exp(kappa_eta x_j)` on `[-W-1,1]`, and cut off both `a` and its displayed stream potential in the free intervals `[-W-2,-W-1]` and `[1,2]`. One explicit cutoff profile is `theta(t)=1-10t^3+15t^4-6t^5` on `[0,1]`, continued by one and zero; `|theta'|<=30`, `|theta''|<=360`. It is twice continuously differentiable at the joins. The profile is harmonic on the whole frozen slab. On the interior strip `-2<=x<-1`, its normal block average is at least `exp(-4 pi)`. The tangential fine-block factor has modulus

```
sin(pi h) / [M sin(pi eta)] >= 2/pi,
M=h/eta>=32,
```

using `sin(pi h)>=2h` and `M sin(pi eta)<=pi h`. Every parent mean is zero. Averaging the square of the real part over complete tangential periods contributes exactly `1/2`, since the geometric sum of the doubled frequency is zero for `L>=32`. Hence, on a strip of fixed positive physical volume per unit tangential area,

```
I_raw >= [2 exp(-8 pi)/pi^2] L^2 V_tan,
||H_s||_Eps^2 + ||omega||_H1^2 <= C V_tan,
C = 2^24 (1+2 pi)^10 exp(12 pi).
```

These constants are independent of `L` and `W`. For the upper bound, `kappa_eta>=2`: use `sin(pi eta)>=2 eta` and `asinh(t)>=t/sqrt(2)` for `0<=t<=1`, the latter obtained by integrating its derivative. Also `|(zeta-1)/(1-z^-1)|<=(pi/2) exp(pi)`. For derivative orders zero through two, the cutoff stream potential is consequently bounded pointwise by
`400(1+2 pi)^2 (pi/2) exp(pi) exp(kappa_eta x)` on its support. Its squared normal integral is at most the squared prefactor times `exp(8 pi)/4`; the sampled sum is bounded by the same quantity with factor two in place of `1/4`, by comparison with the decreasing exponential integral. Integral representations of the first and second finite differences give the same loose bound for their squared norms. The tangential differences multiply by a number of modulus at most `2 pi`. Adding the mass, normal-gradient and tangential-gradient terms gives the displayed safe `C`, including the smaller scalar `omega` terms. This proves the uniform upper bound without a limiting argument. All four constraints were checked above. Thus the raw coefficient bound cannot have a constant independent of `L`, even with nonzero tangential frequency and only one jump. It does not contradict the fixed-`L` depth bound (RI). The simultaneous competitor `w=omega` stays bounded per unit tangential area, so this example rejects an absolute bound for the raw coefficient route, not F-D.

**Discharged (the same family does not destroy saddle coercivity).** Test the actual field `H=H_s+D omega` of the `2 pi` family. Write `X=D*D` and `k_eta=|z-1|/eta>=4`. On every refined leaf in the frozen slab, `X omega=0`. Outside it the leaves are top blocks and the `y` average of `X omega` vanishes. Consequently

```
P_N D*H = P_N X omega = X omega.                         (4.1)
```

Since `||D_y omega||=k_eta||omega||`, periodic summation by parts gives

```
k_eta^2 ||omega||^2 <= ||D omega||^2 = <omega,X omega>,
||D omega|| <= k_eta^-1 ||X omega||.                     (4.2)
```

For the divergence-free `H_s`, `||grad H_s||^2=||dH_s||^2`. This identity, recalled from memory, follows here by expanding the curl and divergence squares: their off-diagonal terms cancel because
`<D_mu H_nu,D_nu H_mu>=<H_nu,D_mu* D_nu H_mu>` and the coordinate differences and adjoints commute; their diagonal terms leave exactly the full gradient square. Each component still has the same `y` frequency, so
`k_eta||H_s||<=||grad H_s||=||dH_s||`. Also `dH=dH_s`. Combining with (4.1)--(4.2),

```
||H||^2 <= (2/k_eta^2)(||dH||^2+||P_N D*H||^2)
        <= (1/8)(||dH||^2+||P_N D*H||^2).
```

Thus the constrained Rayleigh quotient of the flat saddle form's field block, measured in `G`, is at least `8/9` on this family, despite its divergent raw coefficient cost as `L` grows. The extension competitor `w=omega` has the bounded energy already displayed. This is a direct test of the proposed counterexample, not an upper bound for the full saddle inverse, whose norm is a supremum over all inputs. It supplies no counterexample to F-D and does not certify its inf-sup or other field directions.

**Unchecked (unbounded skipped ratios).** If a direct comparison omits every intermediate mean between scales `s` and `S`, the same family illustrates the danger: on a fixed part of `Omega`, with `S=1`, the coarse mean is zero but the fine mean approaches a nonzero oscillation. Its raw weighted cost is of order `s^-2`. A hand lower bound follows by choosing a fixed subinterval of `y` where the real part is at least `1/2` and using `|exp(it)-1|<=|t|` for the fine box average. Thus a constant independent of arbitrarily large *skipped* ratios is unavailable for this raw norm. This is a different formulation from (RI), which retains the immediate level means even if they are not independent rows. It does not refute (UE), since `w=omega` remains a bounded competitor.

## 5. A summable affine residual, and why it is not yet a lift

**Discharged (an improvement using the actual Eps input).** Let `P` be any refined parent of side `S=Ls`, let `x_B` be the centre of its child `B`, and put `a_P=avg_P H_s`, component by component. Define the affine prediction and its residual by

```
p_P(B) = d_P - a_P . (x_B-x_P),
xi_B = d_B-p_P(B).
```

The residual has zero average over the children. By (3.1), its child-grid gradient is `-Q_s(H_s-a_P)`. The following elementary block Poincare estimate suffices:

```
||f-avg f||_B^2 <= (d/2) side(B)^2 ||Df||_(internal edges)^2.   (5.1)
```

Indeed the variance equals the average of squared pair differences divided by two. Join each ordered pair by a coordinate path of at most `dm` edges on an `m^d` grid. A fixed edge lies on at most `m^(d+1)` such paths. Cauchy--Schwarz gives (5.1) after inserting the density and spacing factors. Jensen for the triangular rows and their overlap, at most two per component, gives

```
sum_(B child of P) s^d |xi_B|^2
 <= d S^2 ||H_s-a_P||_P^2
 <= (d^2/2) S^4 ||grad H_s||_P^2.
```

Allowing the looser constant `4d^2` covers the same boundary-cell conventions as Section 3. At a fixed level the parents are disjoint. Summing *even over every refined parent in the tree*, rather than just retained endpoints, therefore gives

```
sum_(P refined) sum_(B child of P) s_B^(d-2) |xi_B|^2
 <= [4d^2 L^2/(1-L^-2)] ||grad H_s||_2^2.           (AI)
```

Here `sum S^2<=1/(1-L^-2)` over parent scales at most one; all overlap across levels was paid with this geometric series. This estimate annihilates the affine example of Section 2 exactly. It is valid with arbitrary tangential dependence and uses a derivative of the given `H_s`, never a derivative of a previously constructed extension.

**Discharged (the distinction from a smooth coarse residual).** Suppose a coarse piece on `P` is `d_P Phi_P`, with `avg_P Phi_P=1`. Write `alpha_B=avg_B Phi_P`. A fine piece with child mean `d_B-d_P` gives total child mean

```
d_P alpha_B + (d_B-d_P) = d_B+d_P(alpha_B-1).
```

The correct residual is `d_B-d_P alpha_B`, not `d_B-d_P`. Its parent mean is zero because the average of `alpha_B` is one. Nevertheless its norm contains the oscillation of the coarse reconstruction. Replacing the constant by the affine prediction in (AI) removes the leading local affine error but does not prove that a globally smooth coarse lift has these predicted averages on the next frozen layer. That is a compatibility problem, not an output cross-term estimate.

**Gap (precise remaining distinction).** (RI) and (AI) bound explicit functions of the given data and `H_s`. They do not bound
`r_l omega-r_l v_(l+1)` for an energy-minimizing or otherwise smooth coarse extension `v_(l+1)`. Setting those expressions equal would silently reintroduce the unresolved step in `fd-jumps.md`, Section 2.2. The stopping inequality below isolates a strictly smaller part of this comparison.

## 6. The strengthened cross-term estimate can be elementary

**Discharged (a specific family of pieces).** This subsection concerns blocks with at least 32 fine sites per direction. It does not claim to handle the final single-site blocks of a general nest. On `[0,1]` put

```
b(t) = [(t-1/4)(3/4-t)]^3   for 1/4<=t<=3/4,
       0                   otherwise,
p_m(t) = b(t)/mu_m,
mu_m = (1/m) sum_(i=0)^(m-1) b((i+1/2)/m).
```

The extension of `b` by zero is twice continuously differentiable. At least an eighth of the sample points lie in `[3/8,5/8]`, where each factor in the product is at least `1/8`. Thus `mu_m>=2^-21`; use the weaker bound `2^-24`. Differentiating the displayed polynomial gives the safe bounds `|p_m|<=2^24`, `|p_m'|<=2^27`, `|p_m''|<=2^30`. These are elementary upper bounds, not optimized constants. On a block `B` of side `s`, let `Phi_B` be the tensor product of these sampled functions. Its block mean is exactly one and its support is in the central half of `B`.

For an arbitrary subset of scale-`s` blocks and coefficients `a_B`, set `v_s=sum_B a_B Phi_B`. The supports, their first-difference supports and their second-difference supports are disjoint between blocks at this scale, since `s/eta>=32`. Along a coordinate line telescope from the zero exterior to obtain the Dirichlet bound `||v_s||<=2s||Dv_s||`. The finite second difference is the average of the continuous second derivative over two unit intervals after scaling. The displayed polynomial bounds, and a support enlargement of at most `2 eta`, therefore give

```
||v_s|| <= 2s ||Dv_s||,
||D*D v_s|| <= (J_d/s) ||Dv_s||,
J_d = d 2^(25d+8).                                    (6.1)
```

For the second bound, first bound `||D*D Phi_B||` by
`d 2^(24d+6+d/2) |B|^(1/2)/s^2`. Jensen gives `||Phi_B||>=|B|^(1/2)`, and the preceding Dirichlet bound gives `||D Phi_B||>=|B|^(1/2)/(2s)`. Division proves (6.1), with room in `J_d`; disjointness then sums the squared bounds for arbitrary coefficients.

**Discharged (cross-scale gain).** For `s<S`, exact lattice summation by parts, followed by (6.1), gives

```
|<Dv_s,Dv_S>| = |<v_s,D*D v_S>|
 <= 2 J_d (s/S) ||Dv_s|| ||Dv_S||.                    (6.2)
```

Thus for scale ratios at least `L` the gain is `L^-|i-j|`, with an absolute prefactor. If `g_j=||Dv_(s_j)||`, then

```
||D sum_j v_(s_j)||^2
 <= [1+4J_d/(L-1)] sum_j g_j^2,
||sum_j v_(s_j)||^2
 <= [4/(1-L^-2)] sum_j g_j^2.                         (6.3)
```

For the first estimate, sum (6.2) by scale separation and use
`sum_j g_j g_(j+r)<=sum_j g_j^2`. For the second, use `s_j<=L^-j`, the first bound in (6.1), and Cauchy--Schwarz. Taking `L>=1+4J_d` makes the sum of the two constants at most eight. No theorem about multilevel bases is imported.

**Discharged (support and moments).** If coefficients on all children of a parent satisfy `sum a_B=0`, their bump sum has zero parent mean exactly. It consequently has zero mean on every ancestor. Its support stays inside that parent, so it also leaves the means of disjoint previously retained leaves untouched. In particular, an actual residual whose parent mean is zero can be lifted this way with cost at most a fixed constant times `sum_B s^(d-2)|a_B|^2`; the derivative bound on `Phi_B` proves this directly. There is no support-versus-zero-mean obstruction for these complete child families.

**Gap (what (6.3) does not say).** The coefficients still have to be the residuals of the *sum of the preceding smooth pieces*. The algebra in Section 5 shows why (RI) does not bound them. Nor does (AI) identify them with the affine residuals. Applying (6.3) to the wrong coefficients would give a stable sum that fails the prescribed averages. Zero coarse means alone also imply no strengthened inequality for arbitrary pieces: one nonzero fine oscillation supported in the overlap of two putative neighbourhoods can be used as both pieces, with all the required coarse means zero, and their gradient correlation is one. The inverse estimate in (6.1), not the names of the levels, supplied the gain.

## 7. Backgrounds: what survives and what has not been proved

**Discharged (pure gauge backgrounds).** If `U_xy=g_x g_y^-1`, transport the site functions and bond fields by `Ad(g)`. This is an isometry, conjugates `D` to `D_U`, and conjugates the flat block averages to the corresponding transported averages. Each displayed flat estimate is then unchanged. This includes nonconstant gauge choices; it is not an argument for nonzero curvature.

**Implication (the cross-term gain, under explicit stronger local bounds).** Suppose the chosen bump pieces, in compatible local frames, satisfy

```
||v_s|| <= c_0 s ||D_U v_s||,
||D_U*D_U v_S|| <= c_1 S^-1 ||D_U v_S||             (BI)
```

with constants independent of scale and depth. Covariant summation by parts gives the exact same argument as (6.2), with `c_0 c_1 s/S`. In particular there is no necessary additive error per level in this cross term: the negative power of `L` survives under (BI).

One sufficient, stronger coefficient assumption can be stated without hiding a regularity estimate. Write `D_U=D+A` in a frame on each support of side `S`, assume `||Av||<=a S^-1||v||`, and assume the discrete product estimate

```
||D*(Av)|| <= a S^-1||Dv|| + b S^-2||v||.
```

For `a<1/4`, (6.1) implies

```
c_0 = 2/(1-2a),
c_1 = [J_d+2a+2b+2a^2]/(1-2a).
```

Indeed `||D_Uv||>=(1-2a)||Dv||`; expanding
`D_U*D_U=D*D+D*A+A*D+A*A` proves the other bound term by term. These assumptions control variation of the coefficients, not just their size.

**Gap (actual background input).** The source permits local small-curvature hypotheses, including `L^4` curvature control at a class fill. A fine-scale bound for the product term just displayed, for these particular bump frames throughout an admissible nest, has not been rebuilt here. It cannot be replaced by the assertion that link matrices are close to the identity: their differences also enter `D*(Av)`. Consequently (BI), and hence an absolute cross-term gain for the actual background construction, remains conditional.

**Discharged (why the flat input proof does not transfer by notation).** Put the child data into the parent-root frame, `u_B=T_(P<-B)d_B`, so `d_P` is their average. On a child edge the covariant gradient equation takes the form

```
R_e u_B' - u_B = -s h_e,
u_B'-u_B = -s R_e^-1 h_e + (R_e^-1-I)u_B,
```

where `R_e` is the holonomy around the root paths and that edge, and `|h_e|=|Q_U H_s(e)|`. The second term is absent at `U=1`. For example, if one supplies `||R_e-I||<=b s/S` and the transported row bounds, block Poincare gives an inequality of the form

```
||u-d_P||_P <= C S ||Q_U H_s||_P
              + C b ||u-d_P||_P + C b |P|^(1/2)|d_P|.
```

Small `b` absorbs the middle term but not the last one. A uniform sum must control these transported parent data or gain a summable scale factor from the curvature assumption. Treating `b` as the same small number at every level and iterating is precisely a possible depth loss. No estimate for this term on the actual class-fill backgrounds is discharged here. The pure-gauge case has `R_e=I` and is covered exactly. The nonzero-curvature version of (RI) and (AI) is not established by the flat result.

## 8. A strictly smaller stopping inequality

**Discharged (definition, with no unknown choice of extension).** Restrict now to `U=1`, one family of nested planar walls normal to `x`, and one fixed tangential frequency
`q0=(pi/2,2 pi,0)` on a torus with appropriate integer periods. Fix `L>=32` and the prescribed brick clearance `t_0`. Set `h_j=L^-j`, using an extra fine subdivision so the smallest retained blocks have at least 32 fine sites per side. Let `T_j` be the final leaf tree stopped after `j` refinements. Define the unique, fully specified minimizers

```
v_j = argmin { ||v||^2+||Dv||^2 : r_(T_j) v=r_(T_j) omega },
v_0=0,             u_j=v_j-v_(j-1).
```

All top means are zero. The constraint sets are nested. First variation shows that `v_(j-1)` is energy-orthogonal to `u_j`, and that `u_i` is energy-orthogonal to `u_j` for `i<j`. Indeed `u_j` has zero means on `T_(j-1)`, which refines `T_i`; both `v_i` and `v_(i-1)` are orthogonal to that subspace. Therefore

```
sum_j (||u_j||^2+||Du_j||^2) = ||v_m||^2+||Dv_m||^2.       (8.1)
```

For each parent newly refined at step `j`, and each of its children `B`, define the actual residual

```
rho_j(B)=d_B-avg_B v_(j-1)=avg_B u_j.
```

Choose one of the newly exposed planar wall faces at this step. Let `F_j` consist of the first `h_j`-thick sheet of its child blocks on the chosen side, within the newly refined parents, across a fixed tangential period of volume `V_tan`. If a step has no such face it contributes zero. Denote child centres tangentially by `y_B`, and set

```
b_j = (h_j^3/V_tan) sum_(B in F_j) exp(-i q0.y_B) rho_j(B).
W_q0 = V_tan sum_j h_j^-1 |b_j|^2.
```

Thus `b_j` is one normalized Fourier coefficient on one normal sheet, not the norm of all the new prescribed averages. One may first project the input to the `p=pi/2` eigenspace of translation by a top unit in the first tangential direction; every operator defining `v_j` commutes with that translation for these planar masks. Restricting to that eigenspace makes the stopping problem smaller still.

**Gap (the single terminal inequality).** Prove, for these planar compatible pairs in that eigenspace,

```
W_q0 <= C_W(L,t_0) ||H_s||_Eps^2,                         (WP)
```

with `C_W(L,t_0)` independent of depth, fine spacing and normal or tangential volume. This is a wall-predictor square estimate for a single fixed nonzero tangential frequency. It does not request an extension or an estimate of its full energy.

**Discharged (why this is smaller than (UE)).** On each newly refined parent `P`, `avg_P u_j=0`. Jensen and (5.1) give

```
sum_(B child of P) h_j^(d-2) |rho_j(B)|^2
 <= (d/2) L^2 ||Du_j||_P^2.
```

Taking one sheet and its normalized Fourier projection only decreases this weighted sum. Summing and applying (8.1) yields the unconditional comparison

```
W_q0 <= (d/2) L^2 (||v_m||^2+||Dv_m||^2).                 (8.2)
```

Consequently (UE) would imply (WP), with `C_W=(d/2)L^2 C_E`. The converse information is absent: (WP) discards all but one Fourier coefficient on one sheet per level, and it treats only flat planar masks. This is a real loss on compatible data. The `p=pi` family at the end of Section 4 has nonzero leaf data but zero selected `p=pi/2` coefficients at every step, since translation by a top unit has different eigenvalues and commutes with the strictly convex minimization. The extension energy is positive whenever a leaf mean is nonzero, by Jensen. Even within the selected eigenspace, the other normal sheets and the other tangential aliases are not measured. Thus (WP) is not a variational restatement of (UE), nor the full residual square estimate, which would essentially recreate the original extension problem.

**Gap (attempt on (WP), and expectation).** On a newly refined parent the exact decomposition is

```
rho_j(B) = xi_B + p_P(B)-avg_B v_(j-1).                   (8.3)
```

The contribution of `xi_B` to `W_q0` is bounded by (AI), with its displayed constant, because sheet restriction and Fourier projection are contractions. What remains is the single selected coefficient of the old predictor's defect against the affine data. The normal harmonic family in Section 4 does not produce growth in the total extension energy, hence cannot make (WP) fail by (8.2). The affine term removes the repeated smooth-gradient contribution responsible for the full-tree divergence in Section 2. These are reasons to expect (WP) to be true at fixed `L,t_0`.

It has not been proved here. In particular the minimizer has a blockwise constant multiplier in `A0 v`, whose tangential Fourier expansion contains aliases separated by the current reciprocal block scale. A single tangential Fourier coefficient of the forcing does not give a closed scalar normal recurrence for the next minimizer. Discarding those aliases would change (WP). A bound on their contribution at the selected wall, uniform over the nested block constraints, is the next concrete decision. No numerical Fourier reduction or literature theorem is used to replace it.

## 9. Consequences and recovery record

**Discharged (decisions made).** In the flat pruned system, the literal retained immediate-parent input sum is bounded at fixed `L`, by (RI), including all nonzero tangential frequencies. No depth-divergent family for that sum exists with bounded `H_s` energy. Its bound cannot be uniform in `L`: Section 4 gives compatible data with ratio at least a fixed constant times `L^2`. The stronger affine remainder (AI) is also square-summable at fixed `L`. Smooth compact pieces admit the strengthened estimate (6.2), with a negative power of `L`; zero parent means and support are compatible for complete child families. None of these statements identifies the coefficients needed by an actual simultaneous smooth lift. No admissible counterexample to F-D has been constructed. The nonzero-curvature claims are conditional as specified in Section 7.

**Implication (downstream scope).** Several-jump Theorem F-D receives no completed new supplier: its coercivity step still cannot consume this note as a proof of (UE). Its one-jump theorem is neither reviewed nor refuted here. The use of several-jump F-D in the layer version of `(I_2^D)` therefore remains conditional; so do the corresponding `(SCR_1)` and K-transport steps from the second scale onward. These are dependency statements from `joint-induction-two-step.md:34--53,131--137` and `quiet-boundary-rarity.md:259--292`, not new checks of those consumers. Even a future proof of (WP) alone would not close them: the rest of the residuals, an exact simultaneous lift and the actual background estimates would still have to be established.

**Discharged (scope of the negative conclusion).** The conclusion is a failure to finish this item, not a no-go theorem. The live choices remain a smooth multilevel predictor, a direct simultaneous geometric extension, the constrained variational operator, or a justified localization to one-wall patches. Their equivalence or impossibility is not asserted. The rejected full-grid counting argument and the skipped-ratio caution do not refute the pruned F-D statement. No claim of independent review, retained status or exhaustive route elimination is made.

**Discharged (source and recovery record).** Mathematical sources read in bounded ranges at the pinned commit: `fd-jumps.md`, Sections 2--7 and its scope record; `fibre-propagator.md:1--201`; mapped Text 3.1 and targeted search hits concerning F-D and its consumers; `quiet-boundary-rarity.md:9--58,240--292`; and the dependency rows and defect D1 of `joint-induction-two-step.md`. Broader search/combined-read output that was truncated supplied no complete-verification claim; the statements used above were reread in bounded ranges. `GOAL.md` and the three required `FINISH.md` sections were read before the mathematics. The workflow blob and installed skill instructions supplied process context only. No independent-side file, forbidden gate or forbidden library file was opened. No external account, proof program, numerical calculation, audit, subagent, commit, push or PR was used. Only this output file was edited.

**Gap (current checkpoint).** Resume with (WP), the explicitly defined single-frequency wall residual inequality in Section 8. The flat raw input, affine-input and bump cross-term calculations above can be reused at this source revision; they cannot be substituted for (WP). The expected answer to (WP) is positive for the stated reason, but no uniform constant has been obtained. The model's exact runtime identifier and effort remain unavailable, as recorded in the provenance; no model change was made.

STOPPED
