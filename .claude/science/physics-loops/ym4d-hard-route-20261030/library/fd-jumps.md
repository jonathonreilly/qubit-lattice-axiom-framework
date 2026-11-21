# Theorem F-D with several jumps
Provenance: OpenAI/Codex (GPT-6 family; exact runtime model identifier and effort setting are not exposed to this session), commit `169e1d5f3d71daa336bfd8e8056516eb08a14a5d`; a different provider from the Anthropic/Claude author of the mapped attempt; research text, not an audit, and no status is granted.

## 1. Source finding and the first obligation

**Discharged (source comparison).** `fibre-propagator.md:118–120` defines the frozen/free partition at just two consecutive levels, `n = k + 1`, and defines `bC`, `r_N`, `G`, and `Lam` for that partition. Its Theorem F-D at lines 162–172 uses this setting. The intervening nest-coercivity paragraph, lines 142–158, states (NC), but does not define or prove the multi-level saddle theorem. `quiet-boundary-rarity.md:275–277` explicitly consumes “Theorem F-D with layers” for (H2). Its MD* recursion at lines 263–269 keeps the level-j data while introducing lower layers. At j = 1 that reads levels 0 and 1 below the level-2 parent. Its induction at lines 281–292 retains these inputs. This confirms the missing supplier identified in `joint-induction-two-step.md:135`; the further SCR/K-transport dependency is recorded at lines 42–53 of that file, not independently proved here.

**Gap (the first obligation, attacked below).** In D-coer, Step (4), replacing a two-level partition by three levels requires one fine site function `w` that simultaneously has all the prescribed surviving block averages. Extending the intermediate averages and subsequently extending the finest averages is not enough: the second correction must have zero intermediate averages wherever those are retained. The required energy constant must be uniform over the depth of this procedure. A factor `C_ext` for each passage would not prove the consumer's claim.

**Unchecked (inherited inputs).** The one-jump theorem, the background estimates, and the quoted chart identifications are research premises rather than independently checked results of this note. Numerical paragraphs in the sources supply no proof here. No mathematical assertion below is justified by a run. No theorem from memory is being used without a displayed argument; any later such use will be marked explicitly.

The worktree omits `docs/ai_methodology/SCIENCE_WORKFLOW.md`; its pinned blob was read with `git show HEAD:...` in two bounded ranges, covering sections 1–10. No execution branch, audit, or campaign is invoked. The owner's specific file-only research instructions govern this item.

## 2. First attack: the extension, with two actual jumps

### 2.1 A simultaneous flat-wall construction

**Discharged (auxiliary scalar lifting, including its lattice version).** Consider a periodic line partitioned into intervals `I_i` of lengths `h_i`, each an integer multiple of the fine spacing `eta`. Prescribe the average `c_i` on each interval. This includes three consecutive regions with sizes `h, Lh, L^2 h`, and arbitrarily many further jumps. At a boundary of two unequal intervals choose the common trace to be the mean on the *smaller* interval; at equal sizes choose the average of the two means. Write the two traces on `I_i` as `a_i,b_i`. In its coordinate `t in [0,1]` set

```
u_i(t) = (1-t)a_i + t b_i
         + 6t(1-t) [c_i - (a_i+b_i)/2].
```

The traces agree, and the integral average is exactly `c_i`. With `A_i=a_i-c_i`, `B_i=b_i-c_i`, direct integration gives

```
integral_(I_i) |u_i'|^2
 = h_i^-1 [(B_i-A_i)^2 + 3(A_i+B_i)^2]
 <= 6 h_i^-1 (A_i^2+B_i^2).
```

At an unequal-size interface only the larger interval pays, and at an equal-size interface the two contributions total at most `3(c_i-c_(i-1))^2/h_i`. Consequently

```
integral |u'|^2
 <= 6 sum_interfaces |c_i-c_(i-1)|^2 / max(h_i,h_(i-1)).        (2.1)
```

There is no factor for the number of intervals or jumps. In particular the two interfaces `h -> Lh -> L^2 h` do not multiply their constants.

For the exact lattice statement put fine sites at the midpoints of their fine cells. If `m=h_i/eta`, replace `6t(1-t)` by `6t(1-t)/mu_m`, where

```
mu_m = (1/m) sum_(j=0)^(m-1) 6[(j+1/2)/m][1-(j+1/2)/m]
     = 1 + 1/(2m^2) >= 1.
```

The identity follows from `sum j=m(m-1)/2` and `sum j^2=m(m-1)(2m-1)/6`; these follow by telescoping consecutive squares and cubes. The sampled mean is now exactly `c_i`. The linear derivative has zero integral pairing with the derivative of the quadratic correction. Thus the displayed energy estimate only improves when the correction is divided by `mu_m`. For each consecutive pair of fine sites,

```
eta |(u(x+eta)-u(x))/eta|^2 <= integral_[x,x+eta] |u'|^2.
```

Sum these disjoint segments to obtain (2.1) for the lattice Dirichlet energy. This proves a simultaneous, mean-preserving lift on the line, not a sequence of extensions. Tensoring with a constant in the three tangential directions gives the same estimate multiplied by the tangential volume. If the prescribed means have zero average in each top interval, the lift does too; the telescoping/Cauchy–Schwarz identity on that interval gives `||u||^2 <= S^2 ||Du||^2`, where `S` is its length.

**Unchecked (scope of this test).** The right side of (2.1) has *mixed-size interface differences*. The actual D-coer hypotheses provide same-level differences of block averages of `omega`, through `Q^{o,(l)} H_s`; they do not directly provide the right side of (2.1). Nor does constant tangential data test the trace problem on a wall. This calculation rules out a compulsory multiplicative loss in the normal scalar lifting construction. It does not establish D-coer, even at `U=1`.

### 2.2 Why two sequential reflections do not finish the argument

**Discharged (compatibility algebra).** Let `r_0,r_1,r_2` denote averaging to the three scales, with `r_1=A_01 r_0`, `r_2=A_12 r_1`. The top decomposition has `r_2 omega=0`. After constructing an intermediate lift `w_1`, the fine residual is

```
d_0 = r_0(omega-w_1),
A_01 d_0 = r_1 omega - r_1 w_1.
```

Where an intermediate mean has already been matched, a fine correction must therefore have that intermediate mean zero. Reflection of the fine trace alone need not have this property. The correction by a bump must be supported in the still-free part of that parent; subtracting its mean on the whole parent changes the prescribed fine data. These are simultaneous constraints, including when both walls are flat.

**Implication (the estimate supplied by this attempted route).** Grant the one-jump extension estimate with constant `A`, and suppose the mean-preserving second correction has been constructed. Its input gradient contains both `Q^{o,(0)}H_s` and `Q^{o,(0)}D w_1`. The direct triangle estimate has the form

```
||D v_2|| <= A (B + ||D w_1||),
||D(w_1+v_2)|| <= A B + (1+A)||D w_1||,
```

where `B` is the controlled local norm of `H_s`. Iteration of this bound produces `(1+A)^m`; that is not a uniform estimate. It is a failure of this proof, not a lower bound and therefore not a counterexample to F-D.

**Discharged (what energy orthogonality repairs, and what it does not).** Choose `w_1` to minimize Dirichlet energy subject to its old means. If `v_2` preserves those means then the first variation gives `<Dw_1,Dv_2>=0`. Nevertheless the preceding estimate yields only

```
||D(w_1+v_2)||^2
 <= (1+2A^2)||Dw_1||^2 + 2A^2 B^2.
```

Thus orthogonality of the *outputs* alone does not give a summable estimate on the residual *inputs*. A bound on their squared energies, or a direct simultaneous lift as in (2.1), is needed. No geometric decay of those residuals has been proved here.

**Gap (tangential route).** Applying the one-dimensional construction separately on normal lines prescribes traces varying tangentially. Its normal derivative is controlled by (2.1); its tangential derivative differentiates the chosen trace and the mean-correction coefficient. Those are precisely the intermediate averages and residual averages above. Controlling their sum by one local `H_s` energy is the missing estimate. Merely calling each interface a flat wall does not supply it.

### 2.3 A nonzero tangential mode: testing and repairing the first ansatz

**Discharged (auxiliary continuum calculation, not a lattice counterexample).** The difficulty can be seen before corners or nonabelian transport enter. On a middle slab of thickness `h`, prescribe boundary traces `1,0` and normal average zero. The polynomial construction of section 2.1 gives

```
p_h(x)=1-4x/h+3(x/h)^2,
integral |p_h'|^2=4/h,       integral |p_h|^2=2h/15.
```

For a tangential Fourier factor `e^(iqy)`, with unit tangential `L^2` norm, its energy is therefore `4/h+(2/15)q^2h`. The two integrals follow by integrating `16-48t+36t^2` and `1-8t+22t^2-24t^3+9t^4` on `[0,1]`.

This high-frequency cost is an artefact of that particular extension. For `qh>=4`, put `eps=1/q`, `b_h(x)=6(x/h)(1-x/h)`, and

```
v_h(x)=max(1-x/eps,0) - [eps/(2h)] b_h(x).
```

It has the same two traces and zero normal average. From `|a+b|^2<=2|a|^2+2|b|^2`, and the directly integrated values `integral |b_h'|^2=12/h`, `integral |b_h|^2=6h/5`,

```
integral |v_h'|^2 <= 2/eps + 6eps^2/h^3,
integral |v_h|^2  <= 2eps/3 + 3eps^2/(5h),
integral (|v_h'|^2+q^2|v_h|^2)
 <= (8/3)q + 3/(5h) + 6/(q^2h^3) <= 3q.
```

The last step uses `qh>=4` and `8/3+3/20+3/32<3`. Hence the polynomial choice can cost at least `(2/45)qh` times the cost of this admissible competitor. This demonstrates a failure of the frequency-independent polynomial *algorithm*, not of the desired extension bound.

**Gap (attempted repair at two walls).** The displayed triangular layer repairs the high-frequency cost without an imported extension theorem. But its subtraction of `b_h` generally changes finer block averages throughout the middle slab. With a second frozen interface there, that subtraction must be replaced by a correction supported on still-free blocks and with zero means on previously matched parents. Thus the explicit frequency repair returns to the simultaneous constraint in section 2.2. I have not bounded that constrained correction uniformly over the tangential frequencies and the nest. No continuum calculation in this subsection is used as a proof step for the lattice theorem.

## 3. The statement that needs to be decided

**Implication (necessary correction of the wording).** Use top-level units, `s_n=1`, `s_l=L^(l-n)`, and potential rather than angle normalization. Let `N_l` be density normalization, so `||Y_l||_(N_l)^2=s_l^d sum |Y_l(c)|^2` on the retained level-l rows. Then the intended operator and norms are

```
C_N H = (Q^{o,(l)}_U H on retained rows)_l,
P_N = orthogonal projection onto ker r_N,
||H||_G^2 = ||H||^2 + ||d_U H||^2 + ||P_N D_U^*H||^2,
||Y||_Lam^2 = sum_l s_l^-2 ||Y_l||_(N_l)^2,
S_N = [[bH + D_U P_N D_U^*, C_N^*], [C_N, 0]]
    : G x Lam^* -> G^* x Lam.
```

The assertion must quantify over the admissible whole-parent brick layers and their clearances, specify the compatible, stationary constrained background and its local small-curvature hypotheses, and require fixed constants independent of the number of layers, depth, and volume. Stability means conjugation by fine-site multiplication `e^f` and by `e^{f(z_c)}` on a constraint row based at `z_c`, with `Lip(f)<=delta` in top units. It is an inverse bound, not just finite-dimensional nonsingularity. The source additionally seeks constants independent of `L` after choosing `L>=L_0` and then the background threshold. Even allowing a fixed `C(L)` would not allow growth with depth.

**Discharged (redundant rows must be removed).** Retaining every parent row as an independent multiplier, even where it is a linear combination of retained finer rows, makes the saddle singular. If `C_parent=A C_fine`, the multiplier `(-A^*lambda,lambda)` is nonzero and is killed by `C_N^*`. Thus “retained rows” must mean the nonredundant rows from the frozen/free construction: a wholly prescribed parent is not an additional multiplier. The site averages must likewise be represented on the disjoint leaf blocks of the refined partition, with parent means recovered by averaging. This is a wording correction, not a refutation of the intended, pruned statement.

**Unchecked (existing scalar versus weighted coercivity).** The unweighted `G` above is the source's graph norm. The nest estimate (NC) uses `s^#` in its lower bound, not the sharper `s`. Replacing `s^#` by `s`, or using a norm with an unrecorded per-level sum, changes the problem. This note makes neither replacement.

## 4. Second attack: inf-sup across three scales

**Discharged (flat, recursively pruned leaf construction).** Here `U=1`; all block averages are the box/triangle averages derived in mapped Text 3.1. The tree realization is precise: a present block either stops as a leaf or is replaced by all its children; a row is retained when both endpoint blocks are present and at least one is a leaf. Rows with two refined endpoints are recovered recursively by composition from finer rows. A retained row at scale `s` therefore has at least one unrefined leaf block of side `s` in its two-block support. Assign it to one such block. Each block receives at most two rows in each direction. A bump inside that block meets no retained finer row. The conclusion below applies to this realization of the multi-level rows, not to an arbitrary independent subset of all rows.

For completeness the local biorthogonal bumps can be constructed without a claim about a finite Gram matrix. On the interior of a block, the two incident one-dimensional triangle weights are `t` and `1-t`. Let

```
b(t) = max(0,1-4|t-1/2|),
p = b / average(b),
a = average(t p),       v = average((t-a)^2 p),
psi_- = p[1-a(t-a)/v],
psi_+ = p[1+(1-a)(t-a)/v].
```

Averages here are the actual fine-site averages in that block. For at least 32 sites per direction, `average(b)>=1/16`. Each of the intervals `[5/16,3/8]` and `[5/8,11/16]` has `p`-mass at least `1/128`: it contains at least a `1/32` fraction of the sites, and `b>=1/4` there. Their separation is at least `1/4`. Using

```
v = (1/2) average_(t,u) [p(t)p(u)(t-u)^2]
```

therefore gives `v>=2^-18`. Direct substitution gives

```
average((1-t)psi_-)=1,    average(t psi_-)=0,
average((1-t)psi_+)=0,    average(t psi_+)=1.
```

The displayed bounds give `|psi_±|<=2^22` and lattice Lipschitz constants at most `2^25` in unit-block coordinates. Multiply by the normalized tents `p` in the transverse directions. The resulting bond field has only its specified component, is supported in the central half of its block, and separates the two incident rows exactly. A finest-level identity row instead uses the corresponding single-bond field. Summing at most two bumps per component per leaf, and counting the at most `2d` neighbouring supports of a lattice difference, gives the following deliberately loose common bound, with `K=2^(20d+40)`:

```
C_l R_l Y_l = Y_l,
||R_l Y_l|| <= K ||Y_l||_(N_l),
||sum_l R_l Y_l||_G <= K ||Y||_Lam.                         (4.1)
```

For the last estimate, `P_N` is a contraction, `||dH||^2<=2(d-1)||grad H||^2`, and `||D^*H||^2<=d||grad H||^2`. Disjoint leaf interiors, with the stated neighbour count for differences, suffice; there is no summation of a global bound once per level.

Fine bumps can change coarser rows. Put `R^0=sum R_l` and `C_N R^0=I+A`. Finer rows kill coarser bumps, so `A_(ji)=0` for `j<=i`. At `U=1`, positivity and overlap at most two of the scale-j triangle weights give `||Q^{o,(j)} H||_(N_j)<=sqrt(2)||H||` by Jensen's inequality. Thus, in the weighted norms,

```
||A_(ji)|| <= B L^-(j-i),       j>i,       B=sqrt(2) K.      (4.2)
```

On three scales the entire matrix and its inverse are

```
T = [ I     0    0 ],          T^-1 = [ I                 0       0 ].
    [ A10   I    0 ]                 [ -A10              I       0 ]
    [ A20   A21  I ]                 [ A21 A10 - A20    -A21     I ]
```

In particular the two-jump product costs `B^2/L^2`, not a new uncontrolled factor. At any depth, the triangle inequality for shifts of an `ell^2` sequence gives

```
||A|| <= sum_(q>=1) B L^-q = B/(L-1).
```

Choose `L>=max(32,1+4B)`. Then the geometric series for `(I+A)^-1` has norm at most `4/3`, and

```
F = R^0 (I+A)^-1,       C_N F=I,       ||F||_(Lam -> G)<=4K/3.
```

Pairing `lambda` with `C_N F Y=Y` proves inf-sup at least `3/(4K)`. All constants here are independent of the number of jumps and the finest spacing. The large lower bound on `L` is an existence choice, not a computed value.

**Implication (background input, not independently discharged).** The analogous conclusion at a background follows if the local perturbation estimate used in the one-jump proof bounds `(C_U-C_0)F` by `1/2` in the mixed `Lam` norm: invert `I+(C_U-C_0)F`. Lemma 4 and hostile point (6') of the source are the proposed suppliers at each patch scale. Their application to the actual nonabelian class fill is an inherited premise, not a result of the flat calculation above.

## 5. Third attack: the constraint commutator

**Discharged (flat active rows, at every depth).** The pointwise assertion “each scale costs `C delta`” would, by itself, give `C sqrt(m) delta` after summation. The row-to-leaf assignment in section 4 supplies the missing packing argument.

Regard a lattice field as constant on its fine cells. Let `M h(x)` be the supremum of averages of `|h|` over cubes centred at `x`. **Memory provenance:** the maximal-cube covering method is recalled from memory; its needed estimate and constants are rebuilt here, rather than assumed:

```
||M h||_2^2 <= 8 * 5^d ||h||_2^2.                          (5.1)
```

To prove it, among finitely many cubes whose averages exceed `t`, choose successively a largest cube disjoint from those already chosen. Every discarded cube lies in a triple of a chosen larger cube. Allowing `5^d` for lattice boundary cells gives measure at most `5^d ||h||_1/t` for their union. Taking increasing finite families proves the weak estimate for the supremum. Since the part of `h` of size at most `t/2` has every average at most `t/2`,

```
|{M h>t}| <= (2*5^d/t) integral_(|h|>t/2) |h|.
```

Integrating `2t` times this inequality over `t>0`, and reversing the nonnegative integrals, proves (5.1). The same selection works on a periodic box, with a wrapping cube represented by its periodic cube and a harmless enlargement already covered by `5^d`.

For row `c` at scale `s_c`, write `q_c(h)=integral rho_c |h|`. Its weight is nonnegative, has integral one, is at most `s_c^-d`, and lies in its two endpoint blocks. For every `x` in the assigned leaf `B_c`, a cube of side at most `8s_c` centred at `x` contains that support. Hence

```
q_c(h) <= 8^d M h(x),
sum_c s_c^d q_c(h)^2
 <= 2d * 8^(2d) ||M h||_2^2
 <= 16d * 320^d ||h||_2^2.                                 (5.2)
```

Here the assigned leaves are disjoint and each is assigned at most `2d` rows. Coarse supports may overlap finer supports: (5.2) does not incorrectly assume they are disjoint.

Let `D=3d`, which bounds the distance from a row base to its support in its own scale. If `Lip(f)<=delta<=1`, then

```
|e^(f(z_c)-f(x))-1| <= D e^D delta s_c.
```

Using (5.2), and exactly the factor `s_c^-2` in `Lam`, yields

```
|| e^f C_N e^-f - C_N ||_(L^2 -> Lam)
 <= 4 sqrt(d) D e^D 320^(d/2) delta.                        (5.3)
```

This is a depth-free estimate for the conjugated commutator, including nested flat walls; it uses neither a spectral experiment nor a per-level global estimate. It also explains why the proposed `Lam` weights are the correct ones for this term.

**Discharged (the flat block-mean summation).** There is no need to pay separately for each level in the projection term either. Put `phi=D^*H` and let `c_B` be its mean on a leaf block `B` of size `s_B<=1`. Set

```
X^2 = sum_B s_B^2 |B| |c_B|^2.
```

Choose a site bump on each block of mean `s_B^2 c_B`, vanishing at its boundary; normalized products of the tents above give a sum `g` with `||Dg||<=K X`, `||g||<=K X`. On a single-site leaf use its site indicator; the neighbour count is again bounded by `2d`. Since the conditional means of `g` are `s_B^2 c_B`,

```
X^2 = <g,phi> - <P_N g,P_N phi>
    = <Dg,H> - <P_N g,P_N phi>
   <= K X (||H||+||P_N phi||).
```

Thus `X<=sqrt(2)K ||H||_G`. On each block the oscillation of `f` is at most `d delta s_B`; subtracting its value at the block centre in the averaging projection bounds its conjugation error on `phi` by

```
2d e^(2d) delta [s_B ||P_N phi||_B + s_B |B|^(1/2)|c_B|].
```

Squaring and summing gives a constant times `delta^2 ||H||_G^2`, independent of depth. This is the weighted version of the block-mean argument in one-jump F-D.

**Unchecked (background scope).** The positive triangle kernels used in (5.2) are exactly the flat kernels. A general small-curvature background uses the source's transported local estimates, not an assertion that its kernels remain positive. Extending those local bounds through the admissible patch cover is part of the inherited one-jump localization package. This section establishes the flat summation mechanism and does not silently certify the nonabelian estimates.

## 6. The single stopping inequality

**Gap: uniform simultaneous block-average extension (UE).** Normalize the top scale of a patch to one. Use the recursively pruned row system and leaf site averages for admissible whole-parent layers, including two jumps. At `U=1`, differences below are divided by their lattice spacing, consistently with potential normalization. Put `P_n` for the projection onto `ker r^{(n)}` and `Eps` for `L^2` plus the full gradient norm. For every pair `(H_s,omega)` satisfying

```
Q^{o,(n)} H_s = 0,       P_n D^* H_s = 0,
r^{(n)} omega = 0,       C_N (H_s + D omega) = 0,
```

the required inequality is

```
inf { ||w||^2 + ||Dw||^2 :
      r_N w = r_N omega,  r^{(n)} w = 0 }
    <= C_E ||H_s||_Eps^2.                                  (UE)
```

The infimum is over fine site functions, not separately chosen functions on the layers. It is nonempty since `omega` is a competitor. The required `C_E` is independent of the number of jumps, the depth, the volume and the fine spacing. For the absolute-rate version it must also be independent of sufficiently large `L`. At a background the same inequality uses `D_U`, the covariant averages and the source's local small-curvature assumptions. **Already the flat case with tangentially varying data is unresolved here.** That is the stopping point, rather than a proposed physical obstruction.

The `Eps` norm on the right is sufficient: the torus decomposition in D-coer bounds that norm of `H_s` by the curvature energy. The source states the stronger `L^2` estimate for its one-jump extension. No stronger estimate is needed to stop the present loss of constants.

### Why this inequality is load-bearing

**Implication, with explicit constants (flat case).** Grant (UE), and grant the torus decomposition used in D-coer, with

```
H=H_s+D omega,
||H_s||_Eps <= T ||dH||,
||omega|| <= C_P ||D omega||.
```

Here `T` is the inherited torus constant. **Memory provenance:** the coordinate-path proof of block Poincare is recalled and rebuilt as follows. On a block with `m^d` sites and zero mean,

```
sum_x |omega(x)|^2 = [1/(2m^d)] sum_(x,y) |omega(x)-omega(y)|^2.
```

Join `x` to `y` by changing coordinates in order. Each path has at most `dm` edges; each fixed unoriented edge lies in at most `m^(d+1)` such ordered-pair paths, since the unused coordinates give `m^(d-1)` choices and the two endpoints in its direction give at most `m^2`. Cauchy–Schwarz and summation therefore give `sum |omega|^2 <= (d/2)m^2 sum_edges |Delta omega|^2`. With physical differences and block side at most one this implies `||omega||<=C_P||D omega||`, for example with `C_P=2d`. All top blocks have zero mean, so their estimates sum without a depth factor.

Set `E=sqrt(C_E)`, `a=||D omega||`, `b=||dH||`, `p=||P_N D^*H||`. Choose a minimizing `w` in (UE), so both its mass and gradient norms are at most `ETb`. The torus orthogonality and equality of the mixed means give, exactly,

```
a^2 = <omega,D^*H>
    = <omega-w,P_N D^*H> + <Dw,H>
   <= (C_P a + ETb)p + ETb(Tb+a).
```

Using `aX<=a^2/2+X^2/2` and `2bp<=b^2+p^2` gives

```
a^2 <= (2C_P^2+ET)p^2
       + (2E^2T^2+ET+2ET^2)b^2.
```

Consequently a valid loose bound is

```
||H||^2 <= C_0(b^2+p^2),
C_0 = 8(1+C_P^2)(1+T^2)(1+E)^2.
```

The flat saddle form is thus coercive on `ker C_N` in `G` with constant `kappa=(1+C_0)^-1`. This calculation identifies exactly where an extension constant growing with depth would enter. Such a *bound* would not establish the claimed uniform result; an actual lower bound forcing that growth would be needed to refute it.

**Discharged (saddle algebra, conditional on its constants; elimination method recalled from memory and rebuilt).** To make the remaining implication precise, suppose the symmetric form `K` is bounded by `M` on `G`, coercive on `ker C_N` with constant `kappa`, and a right inverse `F` has norm `R`. For input `(J,Y)` write `H=FY+h`, `h in ker C_N`. Minimization on that kernel gives

```
||h|| <= kappa^-1 (||J|| + M R ||Y||),
||H|| <= kappa^-1 ||J|| + R(1+M/kappa)||Y||.
```

The functional `J-KH` vanishes on `ker C_N`; define
`lambda(Y')=(J-KH)(F Y')`. This is independent of the choice of lift, gives `C_N^*lambda=J-KH`, and satisfies

```
||lambda|| <= R (||J||+M||H||).
```

For the sum product norms, an inverse bound is therefore

```
M_S = (1+RM)[kappa^-1 + R(1+M/kappa)] + R.
```

If the total conjugation error is at most `C_com delta`, taking `delta<=1/(2 M_S C_com)` gives inverse norm at most `2M_S`, by summing the geometric series for the perturbed operator. Sections 4–5 supply depth-free flat constants for the delicate constraint and projection terms. The local background/Hessian inputs are explicitly inherited and unchecked; this algebra grants them no new status.

## 7. Where the attempted routes meet (UE)

**Discharged (variational reformulation; Schur-complement method recalled from memory and rebuilt).** There is a second, exact way to state the same missing estimate. On `V=ker r^{(n)}` let `A_0` represent `||w||^2+||Dw||^2`, let `B=r_N|_V`, and put

```
Gamma = B A_0^-1 B^*   on range(B),       d_0=r_N omega.
```

`Gamma` is positive definite on `range(B)`: a zero quadratic form implies `B^*d=0`, hence `d` is orthogonal to `range(B)` as well as belonging to it. The minimizer is

```
w_* = A_0^-1 B^* Gamma^-1 d_0,
min (||w||^2+||Dw||^2) = <d_0,Gamma^-1 d_0>.
```

Indeed `Bw_*=d_0`, and its `A_0` pairing with every `v in ker B` is zero. Expanding the square at `w_*+v` proves the minimum formula. Thus (UE) asks for a uniform upper bound on this quadratic form for the compatible data produced by `(H_s,omega)` in section 6. Merely asserting existence of the minimizer says nothing about that bound.

**Gap (why the routes tried do not supply this bound).**

1. **Successive reflection and subtraction of means:** the second extension must preserve the first means. Once this is enforced, the available estimate contains the derivative of the previous extension. Section 2.2 displays the resulting multiplicative recurrence. No lower bound forcing such growth was obtained.
2. **Energy-minimizing corrections:** they remove the cross term between consecutive extensions, but leave `||Dw_1||` in the next residual's bound. The squared recurrence still has a coefficient greater than one. A square-summable bound on the residual inputs would settle this route; output orthogonality is insufficient.
3. **Direct construction on nested flat walls:** (2.1) gives a simultaneous exact lattice lift with constant 6 for normal scalar data. The missing comparison is between its mixed-size interface differences, together with the tangential derivatives of the chosen traces, and the single `H_s` energy. Section 2.3 explicitly tests nonzero tangential frequency, rejects the polynomial extension's excess cost, and repairs that cost by a thin layer; its mean correction still has to preserve the second wall's fine data. These calculations are useful tests, not a counterexample or a proof for the actual four-dimensional data.
4. **Variational/Schur elimination:** the formula above is exact, but eliminating intermediate averages introduces a Schur complement of `Gamma`. Bounds for the separate diagonal blocks do not bound that Schur complement below. For example, the abstract matrix `[[1,rho],[rho,1]]`, with `0<=rho<1`, has eigenvectors `(1,1)` and `(1,-1)`, eigenvalues `1+rho` and `1-rho`, and fixed diagonal entries. This is an algebraic explanation of the missing joint estimate, **not** a claimed realization by admissible lattice walls. A uniform comparison for the actual `Gamma` on the specified compatible data would prove (UE).
5. **Exclude the second wall by localization:** the source's same-family geometric clearance, in physical units, is at least `(t_0/3-2t_0/L)s_(l+1)` between the lower layer and free level-(l+1) bonds. A patch at the next coarser scale has radius `R_0 L s_(l+1)`. For `L>=32`, taking `t_0>=32R_0 L` leaves room to separate the two interfaces of that family, even allowing two lattice cells at the boundary. This does not by itself construct a cover for every admissible union of layer families and for the enlarged supports of its constraint-restoring corrections. The assertion “each patch meets at most one wall” in the source was not verified in that scope here. A written cover with bounded overlap, preserved means and explicit error absorption would reduce (UE) to the one-jump input. I do not replace the requested two-jump extension by that unproved reduction.

**Gap (what would settle this stop).** Produce a simultaneous site-function extension satisfying (UE), with a single constant for all admissible nests, or establish the last route's actual one-jump reduction with those constants. A result for one tangential Fourier mode, a constant depending on the number of layers, or a numerical smallest eigenvalue does not suffice. Conversely, refutation of F-D requires an admissible hand-checkable family whose *saddle inverse* norm diverges (or a nonzero kernel vector). Divergence of the cost of one chosen extension algorithm would only reject that algorithm. No such counterexample has been established here.

## 8. Scope and recovery checkpoint

**Discharged (scope record).** Only this file was written. No numerical or symbolic computation program, proof runner, audit, commit, push, PR, message to another person, or subagent was used. Tool use was restricted to source inspection and writing this note. All mathematical calculations used above are displayed finite identities or written inequalities. Methods recalled from memory are marked in sections 5–7 and rebuilt there; no unproved theorem recalled from memory is used as a premise.

Read at the pinned commit: `GOAL.md`; `FINISH.md:85–151`, including the three required sections; `fibre-propagator.md:1–86,110–174,186–196`; `joint-induction-two-step.md:1–9,23–61,103–118,131–141,156–167`; `quiet-boundary-rarity.md:9–53,259–306`; `block-poincare-energy-package.md:9–31,33–45,51–59`; mapped Text 3.1 and 3.9, plus targeted search lines in that file; targeted search lines only in `induction-with-boundary-data.md`. The first broad search output was truncated, so it was not used to claim complete verification; the load-bearing statements were reread in bounded ranges. The pinned workflow blob was read as recorded in section 1. The installed `physics-loop` entry point was inspected for applicability; its campaign workflow was not invoked.

The independent attempt, gates on it, the forbidden history/compute/strategy gates, `shelling-by-hand`, `adapted-domains`, `tail-two-step*`, `mixed-coefficient*`, and `conditional-normalization` were not opened. No gate file or external account of a Yang–Mills proof was read. The one-jump theorem and its background inputs remain inherited research premises, not an independent verification claim.

**Gap (decision).** D1 is confirmed. The pruned multi-jump statement is not proved or refuted by this note. The single named stopping inequality is (UE), already open here for tangentially varying fields at nested flat walls. The flat inf-sup and commutator results eliminate two proposed sources of automatic depth loss; they do not repair the extension. Resume at (UE), with the five failed/incomplete routes above and the exact source revision recorded here. The downstream use must remain conditional.

STOPPED
