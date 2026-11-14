# TOP-W for the consumer weights: continuation at 8e7fd0a79

Pinned source: `8e7fd0a79b46f32924c1bd85574efa13c34a827b`, 2026-11-01, OpenAI Codex, mapped side. Author investigation, not independent review or audit. No numerical computation. Recovery state: `../parts/hard-core--excess.md`, Summary, Section 6 and Obligations. The earlier arbitrary-weight obstruction and its scope remain in `excess-weighted-fibre-stop.md`. Lemma EX and EX-loc are inputs at their recorded standing; their proofs are not changed.

Conventions: `C(L)` may depend on the fixed odd block side L, dimension four, SU(2), the chosen comb/tensor profiles, a fixed positive weight rate and its margin below the inverse-decay rate. Unless explicitly qualified, a required uniform constant is free of coupling x, depth, volume, location and weight normalization. A finite-lattice local constant below is explicitly *not* such a uniform constant. No absolute TOP coefficient is assumed.

## 1. The weights actually read

**Discharged identification and elementary comparisons.** The relevant source ranges are `sector-values.md`, Sections 3A--3B: (TS), Lemma TOP, FALL, CRUDE and DS; and the part's Section 4.1. The label COMP-ii-g is in the part, not in `sector-values.md` at this pin. The latter parks the old COMP(ii) and consumes FALL/CRUDE/LAN through DS.

| Reader | Weight and convention | What it does not demand |
|---|---|---|
| FALL | One positive scalar top profile w with `abs(log w(x)-log w(y)) <= nu d(x,y)`, nu below the stated fixed ceiling; all depths of the same chain | An arbitrary indicator profile |
| Weighted (TS) | Any fixed family of level weights telescopes algebraically; EX-loc uses the exact family `W_k^q=w`, `W_j^q(z)=sum_y L^4 chi_y^q(z) W_(j+1)^q(y)` | Scalar weights at every lower level, or compatibility for telescoping alone; compatibility is needed for the no-quadrature-error EX-loc identity |
| COMP-ii-g in the part | The preceding compatible family, and the local/max/convolution enlargements in EX-loc and TOP-W | A leading coefficient absolute in L; the displayed theorem already permits C_T(L) |
| DS through CRUDE/SRC/FALL | `w_y(x)=exp(-nu d(x,y))/C_nu`, `C_nu=sum_z exp(-nu d(z,0))`, in top cells; w_y^+, w_y^{++}; intermediate compatible weights or a controlled comparison with the sampled profile | An independent TOP-W estimate for each sharply supported source or for an arbitrary orientation weight |
| Mixed derivatives in DS | `exp(-delta' St(B,bonds))`, and the rate losses in LAN | These are response profiles; they do not turn the energy weight into an indicator |

Here d is the consumer's lattice distance; replacing it by another fixed lattice norm only changes fixed rate factors. On a finite torus use its translation-invariant distance and its own C_nu. The triangle inequality proves the log-Lipschitz property. Summing in y gives `sum_y w_y(x)=1` exactly. For fixed nu>0, C_nu is bounded above by the corresponding infinite-lattice shell sum and below by 1, uniformly in volume. Normalization cancels from all homogeneous weighted inequalities. For a tree profile, moving its root from B to B' changes a minimal connecting tree length by at most d(B,B'), by attaching a path and then reversing the argument; thus it too is log-Lipschitz at its stated rate.

Extend log w from the top sites with the same Lipschitz constant (for example by `inf_y(log w(y)+nu d(x,y))`). Each down-average is a convex combination, since `sum_y L^4 chi_y^q(z)=1`. Its ancestor sites are within a fixed top-cell distance of z: the one-step support radii form a geometric series. Consequently, with `w_j(z)=w(L^(j-k)z)` in common physical coordinates,

    exp(-C nu) w_j(z) <= W_j^q(z) <= exp(C nu) w_j(z).       (W-COMP)

This follows directly from the support and the log-Lipschitz inequality, without iterating a fixed factor. It supplies bounded ratios between orientations and neighboring sites, but **not** a fine-edge rate `nu L^(j-k)` for the compatible weights.

**Discharged diagnostic: a jump does not shrink with depth.** Choose orientation q=(1,2) and w depending only on the transverse coordinate x_3. The chi kernel in x_3 is the box indicator, so its down-adjoint simply assigns w(y_3) to every child in the centered block of y_3. Repetition makes it constant on each centered top block of side L^(k-j). Across two adjacent such blocks whose top values have ratio exp(nu), the adjacent level-j values still have ratio exp(nu), for every k-j. A periodic profile `exp(-nu d(x_3,0))` supplies such adjacent blocks on any sufficiently long ring. Therefore the statement `W_j changes locally by exp(C nu L^(j-k))` is false with fixed C at those faces. Cross-orientation differences can likewise persist there. The sentence in the part's Section 1.7 is not used with that interpretation here; its EX proofs are left untouched as requested. The valid bound is (W-COMP), and EX-loc itself permits the jumps.

For the consumer's *sampled* slow weights w_j, the rate really is `nu_j=nu L^(j-k)`. The energies `E_j(V_j;w_j)` telescope exactly when the same w_j is used in both neighboring differences. They are not the down-compatible energies. To use EX-loc on one step, start its down-weight at w_(j+1); it differs from w_j by a factor exp(O(nu_(j+1))). If b=C nu_(j+1), positivity of fine energy gives `e_sample >= exp(-b)e_compatible-(1-exp(-b))E_(j+1)`. This introduces the energy error FALL already budgets; it cannot simply be deleted. To apply TOP at an intermediate level l, restart compatible weights from the sampled w_l. With b=C nu_l, positivity likewise gives `Y_sample <= exp(b)Y_compatible+(exp(b)-1)E_l`. Thus a compatible TOP upper estimate transfers with an O(nu_l)E_l error and a bounded multiplier. No per-level smoothness assertion about the old W_j is needed.

A local maximum of radius a satisfies `P_a w <= exp(a nu)w`. For a nonnegative probability kernel K, `K*w <= M_nu(K) w`, where `M_nu(K)=sum_z K(z)exp(nu d(z,0))`. This is just `w(x-z)<=exp(nu d(z,0))w(x)` inside the sum. The corrected trial kernels have `M_nu<=exp(C nu)` after the stated small-flux choice. A flux-independent inverse tail can be used if its exponential moment at nu is finite. Fixed compositions retain these bounds. For compatible weights, compare to w_j using (W-COMP) once before and once after a positive estimate. Do not pay that comparison separately at every depth. A depthwise convolution on sampled profiles has total cost `exp(C sum_m nu L^-m)`; transferring this observation to a hierarchical variance still needs its stated transport/variance premises. No nonlinear response estimate is proved by a weight comparison.

**Implication repairing the signed trial bound, without the false shrinking-jump claim.** Assume the existing one-step T2-r/T3-r bounds of `excess-finite-range-repair.md` and its trial/class threshold checks. For a compatible descendant W_j, (W-COMP) and the kernel moment give `W_j^+<=C_w W_j` componentwise, with one fixed C_w independent of depth, volume and L (rates and kernel cutoff fixed). This factor need not approach 1 down the chain. Put `a_m=I^grad(T^m V;W_(n-m))`, `c_m=cub(T^m V;W_(n-m))`. The one-step inequalities give

    a_(m+1) <= C_w C_2 L^-2 a_m + C(L) f_m c_m,
    c_(m+1) <= C_w C_3 L^-2 c_m.

Choose L first with both leading factors <=1/2, in addition to the earlier trial/CLASS requirements. Then `sum_m c_m<=2c_0` and, since f_m<=1, summing the first recurrence gives `sum_m a_m<=2a_0+C(L)c_0`. T2-r and exact compatible telescoping now yield

    E_0(T^n V;W_0)-E_n(V;W_n)
          <= 2 C_1 C_w I^grad(V;W_n)+C(L)cub(V;W_n).          (TR-SLOW)

All constants are free of x,depth,volume and position, conditional on the named one-step estimates; the leading trial constant is absolute after fixing the weight ceiling. This pays the bounded jump factor against L^-2, not against a fictitious shrinking rate. The earlier trial proof's weighted iteration is to be read with this correction and possibly a larger L_0. No numerical L_0 is certified. TR-SLOW is a signed trial excess bound; identifying or bounding the hierarchical Yhat_tr still retains CJ/CR, and nothing here compares the trial with the minimizer.

**Restricted target (gap).** Rename this part's leading upper-bound coefficient `C_TOP(L)`. For the foregoing family only, at every top level n, for the specified class minimizer U of V and compatible W,

    Y_n(W) := E_0(U;W_0)-E_n(V;W_n)
      <= C_TOP(L) I_n^grad(V;W_n^dagger)
           + C_cub(L) sum_(i<=n) L^(-(n-i)/2) cub(V_i;W_i^dagger).   (TOP-slow)

The enlargements must have a bounded ratio to W at the weights/rates read by the consumer. Constants are to be free of n, volume, x and location. Only the upper sign is needed by hole-filling; EX-loc supplies the separate lower control with cubic errors. Together with cubic decay and energy comparability, this target suffices for the scalar FALL/COMP arguments on levels 1 through k. DS additionally needs SRC/CRUDE, domain and tail control, and a strictly positive margin between its response rates and norm rates. The fine endpoint is separate. Thus restriction to this weight family removes an unnecessary false requirement; it does not close TOP-W or DS.

For COMP-ii-g, a partial-chain top weight can itself be a compatible descendant of the original scalar profile. Include these descendants in the restricted family, with the bounded comparison (W-COMP), rather than asserting they are smooth at rate nu_j. Positive weighted norm estimates can be transferred by (W-COMP) once; a signed excess cannot be so compared without an energy error. That distinction is part of the TOP-slow obligation.

**Discharged endpoint identification.** DS sums `Z_(k-m-1) o Lambda_m` only for `0<=m<=k-1`: the source indices are 0 through k-1, and their arguments have levels 1 through k. It therefore needs FALL with `sum_(m<=m'<=k-1) a_m'`. A claim about a_k at bare level 0 is stronger and is not supplied by hole-filling. The original part's level-0 gap remains for the stronger COMP statement, but is not an extra FALL endpoint required by this DS sum.

## 2. Attempts to break the restricted comparison and to bypass it

**Discharged linear diagnostic, no nonlinear conclusion.** The earlier localized falsifier has inverse tail `rho_L^d`, with `rho_L=(a_L-sqrt(a_L^2-4b_L^2))/(2b_L)` and `a_L/b_L>4`. Hence `rho_L<2-sqrt(3)`. Put kappa=-log rho_L>0. For a kernel bounded by `C exp(-kappa d)`, conjugating by sqrt(w) changes its entries by at most `exp(nu d/2)`. The row and column sums are bounded by `C sum_z exp(-(kappa-nu/2)d(z,0))`, so Cauchy--Schwarz with these two sums bounds its l^2(w) operator norm whenever nu<2 kappa. Periodizing first preserves the bound by the cover shell sum. The consumer's small fixed nu satisfies this condition in that slab test. Thus the amplitude mismatch from an indicator weight does not extend to the slow weight in this calculation. This checks that proposed falsifier only; it is not a proof of the nonlinear estimate or of an all-depth inverse.

**Discharged limitation of the proposed EX-loc shortcut.** Suppress the already budgeted cubic errors to see the issue at quadratic order. EX-loc for all W gives a lower local budget. Minimality compares only the unweighted total. For `0<=W<=1`, subtracting the lower bound at `1-W` from the global upper bound leaves the trial's *global* excess. It does not replace it by the trial excess near W. Allowing all nonnegative W in the lower bound does not change that direction of inequality.

Here is an exact test of this inference, including a nonzero lower budget and a weighted trial upper bound. On two sites a distance R apart, keep the parent parameter a fixed and minimize over the affine fibre `u_A-u_B=a`. Define

    e_A=a^2+u_A^2,       e_B=u_B^2,       I(W)=a^2 W(A).

For every fibre point and every W>=0, `e(W)>=I(W)`. The trial `(u_A,u_B)=(a,0)` has `e_tr(W)=2I(W)`. The unique minimizer of the unweighted energy is `(a/2,-a/2)`, so

    e_min(1)=3a^2/2 <= 2a^2=e_tr(1),
    e_min(w)=a^2(5 exp(-nu R)+1)/4,
    e_min(w)/I(w)=(5+exp(nu R))/4,

for the slow profile `w(x)=exp(-nu d(x,B))`. Thus no volume-free weighted upper constant follows from those inequalities and minimality alone, even with zero cubic error. Scaling a to zero respects any small-amplitude restriction. This is a countermodel to the *inference*, not a counterexample to Yang--Mills: its fibre constraint directly couples the distant sites, and does not have the block map's locality. That locality would have to be used through a proved localized competitor or response estimate.

**Gap for a bypass.** EX-loc remains useful, but the requested shortcut is not closed. One sufficient replacement would be an admissible localized comparison giving

    Y_U(W) <= C_loc(L) Yhat_tr(W^dagger)
                  + epsilon Yhat_U(W) + C_err(L) Cub(W),       (LOC-MIN)
    epsilon<1,

with a parent-fixed replacement field or a variational argument deriving this inequality, and the CR cross term bounded separately. Global minimality alone is not (LOC-MIN). No such replacement is constructed here. A localized replacement is still a live alternative to NF-W; the scalar test does not rule it out.

## 3. A genuine local chart, and where uniform endpoint coverage stops

**Discharged finite-lattice local construction.** Fix L, depth n and a finite torus. Restrict the parent V to a sufficiently small link-coordinate neighborhood of 1, which may shrink with n and volume. This is a restriction stronger than small flux. Let T(V) be the specified exact trial from the finite-range repair. It is analytic near 1 and T(1)=1. Write M_n for the *true* composite map, not its contour-free modification.

At the trivial field, Q=D M_n is onto: differentiate the exact right inverse T. The Wilson Hessian is the Maxwell curl form. On ker Q its null vectors are precisely infinitesimal fine gauges whose parameters vanish at the top centers, after subtracting a constant parameter. To check this, integrate a curl-free field around the torus: it is a constant 1-form plus d omega. Coarse periods of Q kill the constant; `Q d omega=d' ev omega=0` makes ev omega constant on the connected parent lattice. Subtract that constant from omega. Fixing the indicated residual gauges therefore makes the constrained Hessian positive definite in finite dimension. The constrained stationarity equations then have an analytic local minimizing branch U(V), U(1)=1, by the finite-dimensional inverse function theorem (or its Newton contraction using this invertible derivative). This constructs only the local branch. Identifying it with the global class infimum, even for this local parent family, remains item (o)'s separate premise.

Here is an explicit fibre chart at any such U=U(V). All derivatives below are in the fine log coordinate `Exp_U Z=exp(eta Z)U`, eta=L^-n. Let G_0 be the fine gauge parameters zero at all top centers, let D_U be the infinitesimal fine gauge action in this coordinate, and let P_0 project site parameters onto G_0. Set

    L_U Z=P_0 D_U^* Z,                 E_U=ker L_U,
    C_U(Z)=log(M_n(Exp_U Z)V^-1),       Q_U=D C_U(0).

The finite Dirichlet gauge matrix `P_0 D_U^* D_U P_0` is positive definite on G_0: its null vector is covariantly constant and zero at an anchor, hence zero on the connected graph. Subtracting a vector D_U omega puts any Z in E_U without changing Q_U Z, because top-fixed gauges preserve M_n. Since Q_U remains onto near 1, its restriction to E_U is onto. Choose a linear right inverse B_U into E_U, put `K_U=E_U cap ker Q_U`, and `P_U=I-B_U Q_U` on E_U. These are finite-dimensional operators; no uniform bounds on them are asserted.

With `R_U=C_U-Q_U`, solve on K_U

    Z(h)=h+B_U z(h),      z(h)=-R_U(h+B_U z(h)).               (TRUE-CH)

Indeed R_U(0)=D R_U(0)=0. On a sufficiently small finite-dimensional ball, the derivative of `b -> -B_U R_U(h+b)` has norm below 1/2 on im B_U and the map preserves the ball (use `||B_U R_U(Z)||<=C||Z||^2`). Iteration gives its unique fixed point. Analyticity follows by differentiating the convergent local iteration, or by the same inverse function theorem. Thus

    Phi_U(h)=Exp_U Z(h),       M_n(Phi_U(h))=V,
    Phi_U(0)=U,              D Z(0)|_(K_U)=I.

This is a true parent-fixed slice chart. It is not the trial's separate parent-correction equation, and it does not identify equality of nonlinear parents with a tangent constraint.

**Discharged endpoint coverage on this finite neighborhood only.** The gauge-slice equation

    L_U [eta^-1 log((g . T(V)) U(V)^-1)]=0,     g|_top centers=1

has a unique small solution g near 1: its derivative in the gauge parameter at V=1 is the invertible Dirichlet gauge matrix just described. Both U(V) and T(V) tend to 1. Hence, by making the parent neighborhood smaller, their aligned relative logarithm Z_tr lies inside the chart ball. It satisfies C_U(Z_tr)=0 exactly; take `h=P_U Z_tr`, `z=Q_U Z_tr`. Uniqueness of TRUE-CH gives `Z_tr=Z(h)`. This proves that a genuine chart covers both endpoints for this restricted finite problem. It proves no uniform neighborhood for the class of the consumer, no charged-sector statement and no depth-free relative-log estimate.

**Discharged derivative and secant identities in that chart.** Write `a_U(Z)=A(Exp_U Z)`, `S=A o Phi_U`, `A_U=D^2 S(0)` and `J_h=D S(h)`. Differentiating the fixed-point equation, with every operator evaluated at Z(h), gives

    D Z(h)v = v-B_U (I+D R_U B_U)^-1 D R_U v,
    J_h(v) = D a_U(Z(h))[D Z(h)v],                           (TRUE-J)
    J_h-A_U h = integral_0^1 [D^2 S(th)-D^2 S(0)]h dt.        (SEC-id)

The inverse in TRUE-J exists in the chart ball by its contraction estimate. Since U is a constrained critical point, D S(0)=0. The fundamental theorem of calculus proves SEC-id; it is not yet the uniform estimate (SEC). At this fixed finite problem let M_3 bound D^3 S on a convex chart ball and let K_A bound A_U^-1 in the chosen finite norm. Then

    ||A_U^-1(J_h-A_U h)|| <= (K_A M_3/2)||h||^2.              (SEC-fin)

Taylor's integral remainder proves this inequality directly. After shrinking the ball it is at most `||h||/2`. A fixed positive weighted norm is equivalent to this norm, so the analogous local statement holds there with finite constants. Their bounds can depend on n, volume, the base field, and the ratio of largest to smallest weight. The local chart also gives `||Z(h)||_W<=C_ch,fin ||h||_W`. None of these finite equivalences supplies the required uniform constants. TRUE-J explicitly retains the derivative of the fibre correction; using D a_U(Z)[v] alone would omit it.

**First honest stop: uniform endpoint coverage (gap).** For the actual small-flux class, all sectors and depths, what is still required is a parent-fixed gauge and chart with a radius r_ch(L)>0 independent of depth and volume, containing the specified trial, with

    Z_tr=eta^-1 log((g . T(V))U(V)^-1),   g|_top centers=1,
    sup_B ||Z_tr||_Eps(B) <= r_ch(L),
    Z_tr=Z(h),    {th:0<=t<=1} inside the chart,
    ||Z(h)||_(Eps,W) <= C_ch(L)||h||_(Eps,W).                 (END)

The chosen radius must also lie inside the domain where the uniform secant contraction below holds. The local proof above only supplies r_ch(L,n,volume,U), and does not bound it below on the requested class. A small flux bound on each field is not a proved small bound on their relative logarithm in a common parent-fixed gauge. Item (o)'s last sentence, which calls such differences “responses”, does not supply this finite-displacement estimate. Prop AN3 varies the parent along the minimizing branch; it does not compare that branch with the specified nonstationary trial at the same parent. Theorem F(iv) is a linear map on tangent classes. Neither is endpoint coverage.

The contour-free chart can avoid some true-map gauge costs, but it still needs a controlled nonlinear conversion to a parent-fixed representative. The fibre note itself warns that the singular composite contour is not uniformly L^2 bounded and that an arbitrary Eps ball does not supply (R3)'s summable contour control. No unconstructed interpolation is assumed to satisfy the hypotheses of F. TRUE-CH is thus a genuine *local* construction, not a claimed uniform solution of this conversion problem.

For clarity, the next two inequalities needed after END are still the original NF-W obligations, now for the consumer family only:

    ||A_U^-1 integral_0^1 [D^2 S(th)-D^2 S(0)]h dt||_(Eps,W)
        <= epsilon ||h||_(Eps,W),       epsilon<=1/2,          (SEC-unif)
    ||A_U^-1 {v -> D a_U(Z(h))[D Z(h)v]}||_(Eps,W)^2
        <= C_J(L) Yhat_tr(W^dagger)
                     + C_4(L) sum_B W^dagger(B) f_B^4.        (TRIAL-J)

Their constants must be free of depth, volume, x and position, uniformly below a threshold chosen after L. The inverse and norm must be transported to the class representatives of Theorem F by a controlled map, not by an unbounded change of gauge. SEC-fin proves neither SEC-unif nor TRIAL-J. The exact sufficient implication remains `H-W <= C_ch(L)^2/(1-epsilon)^2` times the right side of TRIAL-J, by `h=A_U^-1 J_h-A_U^-1(J_h-A_U h)`. It is an implication, not a derivation of the premises.

**Dependent work stopped.** HC-W, the all-depth hierarchical comparison CJ/CR, TOP-W, and the resulting COMP/FALL estimates are not promoted or re-proved here. The constant-order question below is independent of END. This is a named gap in this attempt, not a claim that a uniform chart or TOP-slow is impossible.

## 4. The C_T order: two different constants

**Discharged source identification.** In `one-step-closure.md`, C_T appears only in Section 1's constants list, before L. It is not named as the TOP coefficient there. The source it assembles, `relative-density-bound.md`, Lemma TE, explicitly calls the rough-cell counting constant C_T:

    sum_(j<=k) |R_j cap Z| <= C_T E(Z^+)/T^2.

Its Step 4 prints C_T=32 after the choices of m_* and L; the value is fixed in advance and the thresholds enforce its validity. The mapped part's Obligations also identifies C_T with this count, and its classical descent uses `c_b=1/C_T` in the choice of m_*. This is the pre-L object. That statement is only identified here, not re-proved or audited. The unrelated transverse covariance also called C_T in the mapped part is not an upper-excess coefficient either.

In contrast, `sector-values.md` calls the coefficient in Lemma TOP C(L), and in FALL C_Y; the present part introduced C_T as its own TOP-W notation. **There is no displayed consumer equation identifying these constants.** Distinguish `C_TE` for rough-cell counting from `C_TOP(L)` for TOP-slow and `C_Y(L)` for its FALL conversion. The earlier claim in this part and its two repair notes that the closure list forces an absolute TOP coefficient was an unsupported identification of the same symbol. It is superseded by this read. Keep C_TE before L; a proved C_TOP(L) belongs after L. No change to another file is made.

**Discharged scalar implication, with its hypotheses explicit.** Suppose the still-open upper comparison and its cubic/energy inputs supply, at every l on a fixed chain,

    c_eff T_l <= Y_l + F_l,
    Y_l <= C_Y(L)(T_l-T_(l-1))+G_l,

where `T_l=sum_(1<=j<=l) a_j`, c_eff>0 is uniform, and `(F_l+G_l)/C_Y` has a bound `D(L) sigma^(k-l) B` with sigma<1, uniform in depth. Enlarge C_Y so C_Y>c_eff. Then

    T_(l-1) <= q_h T_l + D(L) sigma^(k-l) B,
    q_h=1-c_eff/C_Y(L),       0<q_h<1.

Iteration gives `T_(k-m)<=q_h^m T_k+D(L)B sum_(r<m) q_h^(m-1-r) sigma^r`. For any `q_bar` strictly between `max(q_h,sigma)` and 1, the sum is at most `C(q_h,sigma,q_bar) q_bar^m`: each summand is at most `r_0^(m-1)` with r_0=max(q_h,sigma), and `sup_m m(r_0/q_bar)^(m-1)` is finite. This also covers equal rates. The initial bound is `T_k<=(Y_k+F_k)/c_eff`, followed by the upper estimate at k and the known a_k. No lower bound for `1-q_h` uniform in L is used. For FALL's stated forcing, sigma can be chosen above max(theta_1,1/L) and the toron-tail rate. COMP-ii-g uses its separate cubic rho in the same convolution. These remain implications of their error bounds, not proofs of those bounds.

**Discharged dependency check for the active closure.** Section 10 replaces the old low-order recursion. Its Step B reads DS only through `C_low(L)`, including `1/(1-q_bar^(1/4))`. Step B' may introduce T_2^-1 and T_2^-2; Step C first makes the genuinely absolute singleton coefficient `C_1^n L^(4-n)(log L)^((n-1)/2)` small for n=5,6. The coefficient here is C_1 from the first derivative of the lift, not C_Y. After L, choose a_* for `C C_5(L)T_2<=1/8`; finally choose x_* to make `C(L,a_*) C_low(L) x_*^-1/2<=1/2`. Thus finite C_Y(L), uniform over allowed small flux and depth, is enough for this constants dependency graph. It need not beat a power of L or stay bounded as L tends to infinity. This does not certify Step C, SRC, CRUDE, rate matching or the rest of closure.

The scalar rate q_bar is a rate *in depth*, distinct from the spatial nu and the exponential response margins. Its value can depend on those fixed rates through C_Y and c_eff; choosing q_bar close to 1 does not itself shrink a spatial rate. A large C_Y(L) may make q_bar very close to 1 and the final constants very large; for fixed L that remains finite. Depth dependence of C_Y would instead invalidate this argument. Shrinking the flux can pay a factor C(L) times flux in a nonlinear error, but cannot turn a bare leading C(L) into an absolute constant. No such conversion is needed for this reader.

| Quantity | Allowed dependencies / uniformity | State here |
|---|---|---|
| C_TE | Fixed absolute count; thresholds chosen afterward; free of x,L,depth,volume | Source identification discharged; its proof not checked |
| Weight comparisons | Fixed dimension, profile rates, enlargement radii and kernel moment margins; free of x,L,depth,volume after the stated kernel cutoff | Discharged elementary comparisons, with jumps retained |
| Finite TRUE-CH and SEC-fin constants | May depend on L,n,volume,U and weight condition number; free of x for the unscaled action | Discharged local branch construction only |
| Required C_ch(L), C_J(L), C_4(L), C_H(L), C_O(L) | May depend on L and fixed rates; must be uniform in x,depth,volume,location and throughout the chosen flux class | Gaps; none supplied by finite-dimensional norm equivalence |
| Required C_TOP(L), C_Y(L) | Same uniformities; fixed after L, uniformly below the flux threshold | Gap as estimates; their permitted order is discharged |
| q_bar(L), C_F(L), DS constants | Depend on the preceding constants and fixed positive rate margins; free of x,depth,volume if their inputs are | Conditional scalar consequences |
| Final B_n and x_* | May depend on L,a_* and fixed rates; B_n free of the running x once x>=x_* | Consumer dependency reading only, no closure certification |

## 5. Result and reopening point

**Discharged:** consumer weight and endpoint scope; the compatible-weight jump diagnostic and safe conversions; failure of the proposed minimality-only inference; a genuine parent-fixed finite-lattice local chart with both specified endpoints on the local branch, its exact trial derivative and finite secant estimate; the distinction C_TE versus C_TOP and the fixed-L scalar constants implication.

**Implication:** TR-SLOW repairs the signed weighted trial iteration from the existing T2-r/T3-r inputs with a possibly larger L_0. NF-W would give H-W with the stated constant; then HC-W, CJ/CR and the trial/cubic hypotheses would give TOP-slow; TOP-slow with the error/decay inputs would give the levels 1..k FALL/COMP bounds. DS still reads its own SRC/CRUDE/domain/tail and spatial-rate hypotheses. None of these premises is promoted here.

**Gap, first stop:** (END) on the whole consumer class with a radius and norm controls free of depth and volume, followed by SEC-unif and TRIAL-J for the actual fibre derivative. Alternatively prove LOC-MIN using an admissible localized replacement. HC-W and the all-depth CJ/CR checks were not continued across this stop. No counterexample to TOP-slow is asserted, and no numerical or independent check was run.
