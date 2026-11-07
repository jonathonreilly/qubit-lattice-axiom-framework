# The local Wilson passage for the two-step sparse crossing
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; queue row 65 requests max); commit `c0a0dc4b0fe933f0f0378fdfd870ad07058aa299`; research text, not an audit, grants no status.

## 1. Contract and source discipline

**Discharged — scope.** This is queue row 65, on the mapped side. The object is the two-step history measure and supported singleton event of `rarity-repair.md`, Section 7. The complete `qr-decide.md` and `sp-decide.md` were read before this argument. The quadratic reserve is retained as supplied; it is not replaced by a smaller quadratic problem. Here a routing prescription is a proposed choice of kernel, a local window is a changed conditioning event, and neither change is silently identified with an existing construction.

**Discharged — method and revision.** The checkout is pinned at the commit above. `GOAL.md` and the three requested instruction sections of `FINISH.md` were read first. The sparse working tree omits `docs/ai_methodology/SCIENCE_WORKFLOW.md`; its pinned Git blob was read without checking it out. Only this note is written, section by section. Source inspection and revision bookkeeping supply no mathematical evidence. There is no computational proof, numerical experiment, audit, commit, push, PR, post or subagent. No theorem from memory is used as a premise: any unproved recollection will be marked **gap — memory**.

**Gap — endpoint to decide.** The requested Wilson comparison must cover every low-action numerator history, including torus holonomies and fields outside a chosen identity chart. Its total dimensionless energy error is at most `1/64`, its marked-plaquette error at most `1/16`, and its all-lines reference must have positive support in the same window. A stationary solution inside a supplied class chart does not establish this coverage. Failure of one chart does not by itself refute the essential action gap or repaired S1–S4.

**Unchecked — first falsifier to test.** A flat torus connection can have nontrivial gauge-invariant periods at zero Wilson action. I will test whether such a period can be attached away from the marked hole while preserving the local window and the actual numerator event. A counterexample must distinguish a global identity chart, a chart on the local read patch, and a chart relative to a variable flat background.

## 2. Routing: an explicit choice, and its admission boundary

**Implication — construction on the singleton cubical collar.** The routing choice below does not authorize replacing the literal hull by a convenient larger cube. Here is its proved geometric domain: the singleton cell has its minimal internal filling and its prescribed collar is in the maximum metric, of integer width `d=ceil(d_1)`. Its cellular two-cycles can be filled inside the cell, and there is no complementary pocket to add: push a cycle one coordinate at a time to a face, subtracting the boundaries of the corresponding prisms; after all four pushes a positive-dimensional cycle is zero. On this domain the hull is the cell enlarged by `d` in all four directions, of side `s=2d+1`, and its block intersections are rectangles. Whether the literal collar convention has this form is an admission condition, not a consequence of that cycle argument. Keep the original test for excluded straight lines: a line is excluded exactly when it meets the literal hull. Do not exclude extra straight lines because an old contour meets it.

**Discharged — an elementary rectangle detour.** Let `B` be a block with centre `y`, and `D=B intersect hull`. Assume `y` is outside `D`, every coordinate interval of `D` has length at most `s`, and `L>=4(s+2)`. For an endpoint `x` outside `D`, pick a coordinate `i` in which `y` is outside the corresponding interval, and a coordinate `j` in which `x` is outside. If `i!=j`, first set coordinate `j` to `x_j`, keeping `i` safe; then set the remaining coordinates to those of `x`, keeping `j` safe. This path has length `|x-y|_1`. If `i=j` and the two values lie on the same side, the same monotone construction works. If they lie on opposite sides, choose `k!=i`, move coordinate `k` to a nearest value outside the forbidden interval, move coordinate `i` across to `x_i`, and finish the other coordinates while keeping `i` safe. The parking move has distance at most `s+1` when needed. The path length is at most

    |x-y|_1 + 2(s+1) <= 2(L-1)+2(s+1).                    (2.1)

All vertices stay in `B`; in the three stages there is always a coordinate outside `D`. When `D` is empty use the original prescribed class contour. Use the same chosen contour to `x` for every direction reading `x`. Unused endpoints inside the hull get an axis path solely for the algebraic extension in `qr-decide`, never for a retained kernel row. A finite average of these choices has the same length bound. To retain the original contour family's spatial symmetries at the level of path averages, transport this prescription through its signed coordinate orders with their original weights. The estimates below hold for each member, hence for that average. They do not require a preferred coordinate order.

**Discharged — privacy and the explicit current constant.** An internal contour uses no bond crossing a block face. A surviving straight line therefore still has a private crossing-face bond, with positive coefficient in its parent's derivative and zero coefficient in every other parent's row. The two endpoint terms use the same endpoint contour in all directions. On all lines they still telescope to the coarse gradient of Text 3.1; after exclusions their non-gradient part is exactly the current in `qr-decide` (2.1), not zero. A full retained path has length at most `5L+4(s+1)<=6L`; unused extensions obey the same bound. A singleton cube meets at most `2L(s+2)^3` of the `L^4` starts. With

    a=2(s+2)^3,   q<=a/L^3,

the elementary triangle inequality for the difference of normalized means gives

    ||q[avg_R J-avg_D J]||_1 <= 2q(6L) <= 12a/L^2.        (2.2)

Consequently the exact (RC) constant is met if

    L>=2^20 M sqrt(a),                                    (2.3)

since `12*45*2^29 <=2^40`. This also implies `L>=2^18 M`. This is a written count, not an enumeration. The exclusion normalization, the retained/deleted endpoint contours and the private bonds are all included.

**Implication — what survives unchanged.** On a block with no hull the prescription is exactly the original contour family, so every class-contour estimate in `c0-loc` and `lc-u` has exactly its original domain and constants there. Their hypotheses on whole class read patches still have to hold. Neither note claims those estimates on rough rerouted patches (`c0-loc`, Section 11); I make no such extension. The block support, hull exclusions and Haar rule are unchanged for the specified singleton hull. In the formula domain the existing relative-log construction can use the routed family. A globally defined, symmetry-preserving continuation of that nonlinear averaging convention outside its logarithm domain is not proved by a bound on path lengths.

**Gap — geometry and scale qualification.** This supplies a concrete routing, not an unconditional theorem about all sparse cores. A noncubical multi-core hull needs its own rectangle cover and connected exterior argument. Even for the singleton, the centre must remain outside its collar and (2.3) must hold for the actual `d_1`. Text 5.3 allows `d_1` to depend on `L` and the smallness thresholds; its paragraph at line 726 gives a lower bound involving `mu` and `tau`. I have not proved compatibility of that dependence with (2.3), and do not freeze an `L`-dependent collar before choosing `L`. If the admitted singleton has this cubical geometry and these displayed sizes, (RC) is discharged. If not, this construction has not silently changed its hull or made an empty event energetic. This issue is not used to avoid the nonlinear question below.

## 3. Local windows: remove the volume factor by freeing the exterior

**Discharged — definition of the changed event.** Let `P` be the complete top cell complex in a fixed cubical neighbourhood of the hole's two ancestors and of the support of the centre field. Include a second fixed cube around `b_*` if it is remote; retain both components, and merge them into a bounded cube if their full fine read enlargements touch. Each component is contractible, and separated components have disjoint read enlargements. Include every bond on its cells, and write `n=|P_1|`. The radius includes all prescribed parent read widths. For volumes in which these patches embed without wrapping, `n` is independent of `Q`. Define

    B^loc_w={dist(V_2(b),W(w)(b))<T/100, b in P_1}.         (3.1)

The exterior top field is integrated against the original history measure. No exterior top is assigned Haar measure, fixed to the centre, or required to be regular. These are new windows. A gap for (3.1) alone does not imply a gap conditional on every exterior top field, or the original globally constrained (SP).

**Discharged — the finite data bound in the tangent problem.** Apply once the fixed commuting top gauge that removes the contour gradient of `W_*`. In this gauge the centre cochain is `Q_path^(1)((v/T)e_f)+(w/T)e_*`. A linear window field `z` on `P_1` has zero extension `z^ext` with

    ||d z^ext|| <=5||z^ext||
       <=45/(8L)+5rho/4+sqrt(n)/20 <=m,
    m:=2rho+1+sqrt(n)/20,                 L>=9.             (3.2)

Here `||Q_path^(1)||<=1/L`, `v/T<9/8`, and each window perturbation has Euclidean colour norm at most `1/100`. This is a tangent-coordinate statement; a group-distance window still needs the comparison in Section 5. The replacement for `Q^2` is `sqrt(n)`, independent of the ambient volume.

**Discharged — why an arbitrary exterior cannot simply be zeroed.** Use `X,C_h,C_0,G_h,G_0,H_h,H_0` of `qr-decide`, with the three colours if required. Let `C_{h,P}` be restriction of the top curl to plaquettes of `P`, and minimize `||x||_X^2/2` subject to

    C_{h,P}x=d_P z.                                       (3.3)

Equality of curls on each contractible component says that the difference of the two bond fields is a gradient: integrate it along paths, fill path differences by coordinate plaquettes, and telescope. A fine gradient extending the values of the resulting top potential matches the bonds at zero curl energy. Thus (3.3) is the correct local constraint modulo gauge, with all exterior top data free.

**Implication — localization of the supplied quadratic reserve, with explicit constants.** Assume the actual routed rows obey (RC) at budget `M=172m`, and use the scales of `qr-decide`. Its right inverse and Gram comparison give a competitor for (3.3), namely `H_h d z^ext`, with norm at most `64m/(1-e)<=86m`, since `e<=1/4`. The minimum `x_P` exists: in finite dimensions restrict to the orthogonal complement of the constraint kernel and solve its positive definite Gram system. Hence `||x_P||_X<=86m`. Put

    y=C_h x_P,                  ||y||<=172m=M.              (3.4)

Indeed `||C_0||<=1`, `||C_h-C_0||=delta=e/64<1`, so `||C_h||<=2`. The local minimum is also the full minimum at its own full data: a smaller competitor with `C_h x=y` would satisfy (3.3). Therefore `x_P=H_h y`. This is the crucial choice of completion; it is not the zero extension of the actual exterior field.

For any `x` satisfying (3.3), `x-x_P` is orthogonal to `x_P`. The norm of the plaquette functional is at most one on this larger kernel too. The same one-mark subtraction consequently gives

    E(x)-E(H_0y)
       >= [(t-|ell_p H_hy|)_+^2
                -max(0,<y,(G_0^-1-G_h^-1)y>)]/2.          (3.5)

The all-lines field `H_0y` has the same local top curl, and a gradient matches its local bond data. Apply the already supplied (QR) to (3.4). For `t=1` this is at least `1/8`; for `t=15/16` it is at least `49/512`, exactly the reserve used in `qr-decide` (6.4). No exterior data norm appears. The numerator may have any exterior tangent field, not just a field of bounded support. This is a localization of the existing quadratic result, not a new smaller quadratic target.

**Gap — remaining uniformity.** The constants above are uniform in `Q` for embedded windows of fixed geometry, at depth two, and under the stated routed-current and scale bounds. They are not uniform in growing read radius, arbitrary numbers of holes, or depth. Group logarithms, positive label support and the total Wilson error are not consequences of (3.5). Replacing global windows also changes the question: a full-law repair with arbitrary fixed exterior data would need a separate argument.

## 4. First nonlinear attack: a distant twist

**Discharged — a zero-cost twist, written on links.** On a periodic fine lattice of side `N=QL^2`, choose a coordinate cut `x_1=t` disjoint from the fixed read patch. Let `z(b)=-I` on positive 1-bonds crossing that cut and `z(b)=I` elsewhere, with inverse values on reversed bonds. Every plaquette contains zero or two cut bonds, so its central product is `I`. Consequently

    U^z_b=z(b)U_b,
    hol_p(U^z)=hol_p(U),                A(U^z)=A(U).         (4.1)

This holds for noncommuting `U` as well: `-I` is central. In particular `z` itself is flat but its 1-period is `-I`, whereas the identity's period is `I`. A periodic gauge conjugates a closed holonomy and cannot change either central value. Thus these flat fields are gauge inequivalent.

**Discharged — effect on the two blocking steps.** On every nonwrapping read patch the cocycle `z` is a vertex coboundary. To see this, integrate its signs from one vertex; two paths differ by plaquette boundaries, all of whose signs are one. Gauge covariance then gives the same induced central cocycle on parent links. Relative path products have no extra sign, so their small relative logarithms remain on the same branch. This applies at both steps and to either fixed hull pattern. All fine and intermediate plaquette fluxes and all label weights are unchanged. On the specified local read patch the link histories themselves are unchanged. It preserves the local window and the crossing inequality. It also preserves any non-quiet predicate that reads only those unchanged variables.

**Gap — full numerator admission is not inferred.** If the actual non-quiet predicate invokes a globally selected lift, its invariance under this twist additionally requires equivariance of that selector. This has not been checked. The explicit supported face crossing in `rarity-repair` can be twisted with exactly the same action and local label weights, but its non-quiet admission was already conditional there. Moreover its prescribed face action is of order `L^2T^2`; it has not been shown to lie below the low-action cutoff used below. Thus (4.1) is not being passed off as a low-action supported counterexample to (SP).

**Discharged — exactly what the twist defeats.** In a maximal-tree gauge a remaining period variable may equal `-I` at zero action. Hence no positive absolute-action penalty follows merely from that variable leaving a small chart about `I`. On a period of length `N`, the inequality `dist(I,product U_b)<=sum_b dist(I,U_b)` also rules out a representative with every link angle less than `pi/N` for period `-I`. It does **not** rule out a larger bondwise chart: the commuting representative `U_1=exp(pi tau/N)`, `U_j=I` for `j!=1`, is flat and its links are small for large `N`. Allowing flat periods as separate variables, or taking a chart only on the local read patch, escapes the obstruction. No claim about the nonexistence of all common charts follows from this example.

## 5. What small absolute action does prove locally

**Discharged — a fixed local gauge prescription for every low-action field.** Fix a nonwrapping rectangular fine patch `D` containing the two-step reads of one component of `P`, and let each side have at most `d` bonds. For `0<=theta<=pi`, concavity of sine gives `1-cos theta=2 sin^2(theta/2)>=theta^2/8`. Thus `A(U)<=K T^2` implies

    sum_p theta_p^2 <=8K T^2,             theta_p<=3sqrt(K)T.

From the lower corner take the same axis-ordered path to every vertex. Gauging its parallel transport to identity leaves on a bond the loop between two such paths. Moving the final unit step past the later coordinate runs fills that loop with at most `4d` plaquettes. Remove those plaquettes in order; each contributes a conjugate of its holonomy. The bi-invariant triangle inequality gives

    dist(I,U^g_b)<=12d sqrt(K)T,                   b in D. (5.1)

This proves existence by an explicit gauge, including the rough plaquette at the hole. It uses no stationarity, no class lift and no exterior gauge fixing. A distant flat twist disappears on this patch.

**Discharged — preserve the observed top vertices.** First use the fixed top gauge of Section 3 on the entire problem. The original observed top links then have angles bounded by `C_W T`, with `C_W` depending only on the fixed window geometry and `rho`. The top image of the gauge in (5.1) has angles bounded by `C_D sqrt(K)T`: it consists of finitely many paths and relative logarithms on the small branch. Gauge covariance therefore bounds the distance between this gauge's values at adjacent observed top vertices by `C_D(sqrt(K)+C_W)T`. Connect the vertices inside each component of `P`, normalize the gauge to identity at one vertex, and telescope along a path of at most `|P_0|` edges. All its other observed vertex values are within `|P_0|C_D(sqrt(K)+C_W)T` of identity. Multiply by their inverses at those vertices and by identity at the other fine vertices. This gives a gauge equal to identity at every observed top vertex, with

    max_(b in D)|log U^g_b| <= B_D(sqrt(K)+rho+1)T.         (5.2)

Here `B_D` is the displayed finite path/vertex bound enlarged to include the two endpoint changes on a link. Distinct separated components are treated in disjoint patches. The fine gauge extends to all remaining vertices arbitrarily. This does not alter the action or the actual top window. Discontinuity of this gauge as a lattice function is harmless for this finite-link statement; no derivative bound for the gauge is asserted.

**Discharged — total local Taylor error, not an error per uncounted plaquette.** Let `a_b=log U^g_b`, and `xi=a/T`. Choose a positive radius `r_D` so that every path product and both relative-log maps read in `D` stay at matrix distance below `1/4` from identity whenever `max|a_b|<=r_D`. For instance one may take the reciprocal of 64 times the total number of link occurrences in these finitely many words, enlarged to one. The logarithm series and its first three differentiated series converge uniformly on matrix distance at most `1/3`. Their finite sums/products have finite derivative bounds. Define `C_D` to be the maximum of those bounds, multiplied by the numbers of bonds, plaquettes and read words. Taylor's integral remainder then gives, with every local plaquette counted,

    ||log hol(U^g)/T-d xi||_2 <= C_D T ||xi||_2^2,
    |A^D(U)/T^2-||d xi||_(2,D)^2/2|
          <= C_D[T||xi||_2^3+T^2||xi||_2^4],
    ||log M_0^(1)M_h(U^g)/T-Q_0^(1)Q_h xi||_(2,P_1)
          <= C_D T||xi||_2^2.                             (5.3)

The scalar action remainder follows also directly from `0<=t^2/2-(1-cos t)<=t^4/24`. In the first line one subtracts the first derivative of the plaquette word, which is its signed four-link sum. In the last line one differentiates the actual fixed-pattern maps, retaining the endpoint terms and exclusion normalization. These explain each linear term; there is no assertion that nonabelian curvature equals an ordinary curl exactly.

**Discharged — an explicit order of smallness at fixed geometry.** Put `B=B_D(sqrt(K)+rho+1)` and `N_D=|D_1|`. Then `||xi||_2<=sqrt(N_D)B`. Require

    BT<=r_D,
    C_D T N_D B^2<=1/64,
    C_D[T N_D^(3/2)B^3+T^2 N_D^2 B^4]<=1/256.             (5.4)

These are positive thresholds on `T` after `D,K,rho` are fixed. They prove a hole-to-curl error at most `1/64`, and a **total local** energy error at most `1/256`. On the observed top links, the derivative bound for the logarithm on this ball is at most two, by its power series; hence the group window gives a tangent perturbation at most `1/50`. In Section 3 use `m=2rho+1+sqrt(n)/10`, and `M=172m`, for these actual windows.

**Gap — the precise failure of the immediate promotion to (6.2).** The cochain in (5.3) is defined on `D`. Extending it by zero generally creates curl on the boundary of `D`; no term in `A^D(U)` pays that curl. Keeping the original field outside `D` does not give a global real cochain in this gauge. Thus the bound in (5.4) is not the claimed global error `1/64` in `qr-decide` (6.2). A private-bond correction can repair the last line of (5.3) locally, at finite cost, but cannot repair this missing exterior energy comparison. Multiplying a local error bound by the volume would reintroduce precisely the problem being removed.

**Implication — local constraint correction once an energy-controlled extension exists.** The derivative to observed top bonds has a finite supported right inverse. At the second step assign one private level-1 crossing bond per observed row; at the first step realize those level-1 variations with its private fine bonds. Each coefficient is the number of retained starts reading that private bond divided by at most `L^4` starts, so it is at least `L^-4`. Distinct rows have distinct private variables and no off-diagonal coefficient on them. Dividing twice therefore gives a right inverse of Euclidean norm at most `L^8`. Apply it to the last residual in (5.3). Its dimensionless correction is at most `L^8 C_D T||xi||_2^2`; its curl norm is at most five times that. The energy change is at most `||x||_X||d correction||_2+||d correction||_2^2/2`. With a bounded-energy extension, explicit further positive thresholds on `T` make these changes at most `1/64` in one fine curl and `1/256` in energy. This supplies exact linear local constraints and keeps the total marked-plaquette loss below `1/16`, **provided** the initial cochain has an energy-controlled global extension. No inverse or remainder constant depends on `Q` at this fixed geometry.

## 6. A supported reference and an absolute bound outside the local chart

**Discharged — a deliberately crude smooth reference.** This construction supplies a cutoff for high actions; it does not assert (6.3). For any actual top in the local window let `z=log V_2/T` on `P_1` after the fixed top gauge, and extend `z` by zero. Choose the fixed bound

    Z=max(1,sqrt(n)[9/(8L)+rho/4+sqrt(n)/50]),
    ||z||_2<=Z,                         ||z||_1<=Z.         (6.1)

For `n>=1` this follows from the centre's path-norm bound and the logarithm's factor-two window bound. Put `R=L^2`. Use the explicit all-lines path right inverse: at each top Fourier frequency `p`, lift to fine frequency `p/R` and divide component `mu` by the full complex multiplier in `qr-decide` (3.3). Its magnitude is at least `R/32`. The zero frequency has multiplier `R`. Take the real part for real data. Finite-character orthogonality and the triangle inequality give the following written bounds for the resulting real fine cochain `a`:

    Q_path^(2)a=z,
    ||a||_infinity<=32Z/R,       ||a||_2<=32R Z,
    ||a||_4^4<=2^20 Z^4,        ||d a||_2<=256Z,
    E(a)<=2^15 Z^2.                                     (6.2)

For the supremum, normalized top coefficients satisfy `|hat z(p)|<=Q^-4||z||_1`, and there are `Q^4` frequencies. Parseval supplies the second bound with fine/top normalization ratio `R^4`. Their product supplies the fourth power bound. Each fine frequency has difference vector length at most `2pi/R<8/R`, supplying the curl bound. No Green-function estimate or numerical Fourier check is used.

**Discharged — fine and intermediate class margins.** A single fine difference is bounded by `(pi/R)(32Z/R)`, so a fine plaquette curl is at most `256Z/R^2`. Its first all-lines image is at most `256Z/L^2`, since the plaquette weights are positive with row sum `L^2`. Require `L^2>=2^12 Z`. Both are at most `1/16`. For `U_b=exp(Ta_b)`, the local plaquette and block-map series then give actual fine and intermediate flux at most `T/8` when `T` is small after `L,Z`. The per-patch Taylor constants are uniform in `Q`, since the same finite words occur in each translated patch and `||a||_infinity` is uniformly bounded.

**Discharged — aggregate action control for this reference.** On the fixed small four-link ball, Taylor's formula gives the plaquette error bound

    |log hol_p(exp(Ta))-T(da)_p|
                      <=c T^2 sum_(b in boundary p)|a_b|^2.

The second derivative of the four-link word on that closed ball defines the finite absolute `c`. Each link meets six plaquettes; squaring and summing bounds the error norm by another absolute constant times `T^2||a||_4^2`. Since `1-cos t<=t^2/2`,

    A(exp(Ta))/T^2
       <= E(a)+c' T||da||_2||a||_4^2+c' T^2||a||_4^4.    (6.3)

Equations (6.2) make this error at most `1/8` by a positive threshold on `T` depending only on `Z`. This is a total action estimate on the entire torus, including the tails of `a`.

**Discharged — exact local top data and positive support.** The full linearized all-lines map differs from its path map by a top gradient (Text 3.1). A fine vertex gauge, prescribed at observed top vertices, removes that gradient to first order. Its required vertex angles are `O_{L,P}(TZ)`: the contour integrals contain finitely many fine links, bounded by (6.2). Gauge transformation changes neither fine nor intermediate flux or action. The residual observed top error is now `O_{L,P,Z}(T^2)`.

Use the supported private-bond right inverse from Section 5, now for the all-lines pattern. To spell out the nonlinear correction, write the local top log map in these correction coordinates as `F(t)`. Its derivative at the flat field has right inverse `J`. On the small ball the derivative difference from that flat derivative is bounded by a finite constant times `T+|t|`. Starting at `t=0`, repeatedly add `J(target-F(t))`. The error after an addition is bounded by `||J|| sup||DF-DF(0_flat)||` times the old error, by integrating the derivative along the segment. Choose `T` so this factor is at most `1/2` on the ball of radius `2||J||` times the initial residual. The iterates remain in that ball and their increments have a summable geometric bound. Their limit solves every observed top bond exactly and changes only finitely many fine bonds by `O(T^2)`. The total action change divided by `T^2` is at most `1/8` after another finite smallness choice: its first variation is bounded by the global `O(T)` curvature norm times an `O(T^2)` supported change, and its second variation by a constant times `T^4`.

The reference `U_ref` therefore has the original actual top on `P_1`, fine and intermediate flux strictly below `T`, and

    A(U_ref)/T^2 <=2^15 Z^2+1/4=:B_ref.                   (6.4)

It lies strictly in the same open local window. By continuity a fine-link open neighbourhood stays there and has all labels zero with probability one. Every such neighbourhood has positive product Haar measure: finitely many translates cover the compact group, so invariance and unit total mass preclude zero measure for a nonempty open set. Thus this is genuine denominator support. Its neighbourhood mass need not be bounded below uniformly in volume; only its action bound is uniform here.

**Discharged — histories outside the local chart have an absolute bound.** Choose

    K=2^15 Z^2+1.                                         (6.5)

Use the local chart domain and thresholds of Section 5 with this `K`. Every history with `A(U)<=K T^2` lies in that domain. The contrapositive, together with (6.4), gives for every history outside it

    A(U)>K T^2 >= A(U_ref)+(3/4)T^2.                      (6.6)

The same strict cutoff also handles high-action histories that happen to lie inside it. None is discarded. This concerns the local chart, not a global chart that excludes flat periods. It holds at fixed admitted geometry with all the displayed scale and smallness conditions; if collar widths change with `T`, their compatibility must be proved before calling the choices uniform.

**Gap — why the sharp reference remains unpaid.** The smooth right inverse in (6.2) need not be the minimum `H_0y`. Its upper bound `2^15 Z^2` cannot replace `E(H_0y)+1/64` in the signed subtraction. For the sharp reference one must control a near-minimal all-lines cochain, its nonlinear action, both class margins, and exact local top restoration together. In particular (6.4) cannot be subtracted from a numerator lower bound of only order `T^2/2`. The construction settles positive support and a uniform absolute cutoff, not the sharp (6.3) of `qr-decide`.

## 7. Decision: one strictly smaller nonlinear inequality

**Gap — the selected next inequality is an absolute annular reset (AR).** Work on the unit fine lattice in four dimensions, with no block map. Let `B_s` be the full cubical complex with vertices in `[-s,s]^4`. For integer `r>=8`, define `S_r` to be the plaquettes contained in `B_(4r+2)` but not contained in `B_(r-2)`. This fixes the boundary buffers exactly. Sum the Wilson action over `S_r`, counting each unoriented plaquette once. The target is: there is a finite constant `C_AR`, independent of `r`, and for every `r` a number `epsilon_r>0`, such that every connection `U` on `B_(4r+2)` with `A^{S_r}(U)<=epsilon_r` admits a connection `V` on the same complex satisfying

    V=U on every bond contained in B_(2r),
    V=I on every bond not contained in B_(3r),
    A^{S_r}(V) <= C_AR A^{S_r}(U).                         (AR)

The action sum includes every plaquette crossing either transition. Extend `V` by identity outside the given cube. Gauge transformations in constructing `V` are allowed; the displayed endpoint equalities concern the final links. No link outside the given cube is read. The threshold may depend on `r`; the coefficient may not. This quantifier order is sufficient for a two-step finite-patch argument and does not assert a continuum small-energy gauge theorem.

**Discharged — why (AR) is strictly smaller, and why a radius-dependent constant is insufficient.** (AR) contains one connection, one annulus and one absolute nonnegative action. It has no numerator event, labels, hull, parent map, local top data, signed minimum, marked plaquette, inverse Gram matrix, fluctuation integral or all-lines reference. It asks for a cutoff cost, not an action gain. Its constant is not required to be small. Thus it isolates the nonlinear exterior operation missing after the already proved local chart; it is not (6.2) with different notation and is not another quadratic reserve.

To check the reduction quantitatively, take `J` disjoint annuli of radii `r_j=8^j r_0` around the fixed read patch. Their total action is at most `A(U)`, so one has action at most `K T^2/J`. If (AR) holds, resetting at that annulus leaves the inner field unchanged and yields a compactly supported field with

    A(V) <= A(U)+C_AR K T^2/J.                            (7.1)

Choose `J>=512 C_AR K`, then choose `T` so `K T^2<=min_(j<J) epsilon_(r_j)`. A finite-box logarithm comparison can then spend another `T^2/512`, giving an energy-controlled extension with added action at most `T^2/256`. This is the budget that Section 5 lacked. The patch size is fixed before this smallness choice, so its Taylor constants are finite and independent of the larger ambient volume. One must require the largest patch not to wrap; the resulting volume lower bound is stronger than the initial `100`-read-width convention. Conversely constants `C(r_j)` with no common bound do not permit this choice of `J`: enlarging `J` enlarges the radii and may increase the loss faster than the pigeonhole gain. I have not replaced that problem by an unspecified large constant.

**Implication — separated window components.** The preceding reduction concerns one connected read patch. For two components take `J>=1024 C_AR K` and perform the two resets if their outer cubes are disjoint. If those cubes meet, enclose their union in one cube before choosing the new annuli. Its side is bounded by four times the previous outer side; there are then no other components to meet. The resulting finite radius and nonwrapping volume requirement depend on the fixed geometry and `J`, not on the ambient volume or the separation of genuinely remote components. This accounts for the extra `b_*` window without silently growing `n` with `Q`.

**Implication — the logarithm step after a reset has only finite geometry.** A reset field is identity in a thick outer collar. Choose a gauge tree rooted in that connected collar, using its identity bonds first, and keep its boundary gauge equal to identity. If the cube side is `d` and it has `N_v` vertices, a tree-bond loop has length at most `2N_v+1`. Insert corner-rooted axis paths between its successive edges; the inserted paths cancel. Each resulting edge loop is reduced by at most `4d` plaquette swaps as in (5.1). Thus the full loop is a product of at most `4d(2N_v+1)` conjugated plaquettes. This is a finite bound depending on this radius, not an unproved filling theorem. The gauge's links are uniformly small when the total action is sufficiently small. Its logarithms vanish in the outer collar and extend by zero without boundary curl. The finite Taylor argument of (5.3) now applies to the complete support. Preserving the observed top gauges uses the finite vertex adjustment in Section 5. Thus (AR), with these finite smallness conditions, would repair the missing numerator extension in this two-step setting. This is an implication, not a proof of (AR), nor by itself a proof of the sharp reference.

**Discharged — one obstruction test that (AR) passes.** If the input on the annulus is explicitly a pure gauge `U_xy=q_x^-1 q_y`, choose vertex values equal to `q` through radius `2r` and equal to identity beyond radius `3r`, with arbitrary values in between. Put their pure-gauge links in the transition and keep the original field inside. All transition plaquettes are identity and the boundary links agree. Hence the reset cost is zero. Large relative vertex values and the distant central-twist test do not refute (AR). This statement is proved for the displayed pure-gauge representation; it does not import a general gauge-existence theorem on annuli.

**Unchecked — expectation and reason.** I expect (AR) to be true. The shell has comparable thickness and radius; an absolute-energy gauge on that shell should have potential squared norm bounded by a constant times `r^2` times its curvature energy. A cutoff with derivative of size `1/r` would then have exactly the scale in (AR). At fixed `r`, higher product errors can be made small by `epsilon_r`; the difficulty is obtaining one radius-independent coefficient while matching both boundary gauges. The pure-gauge test above removes one apparent obstruction but is not a proof for nonzero curvature. The finite-box estimates in Section 5 do not supply this uniform coefficient. The annular patching discussion in `curl-poincare-exterior.md`, Lemma 2, explicitly leaves a homological step without a general proof, and its nonabelian passage is a sketch; it is not used as a discharged supplier here.

**Gap — disposition of the original item.** The local quadratic window reduction is complete under its stated routed-current premise. The routing is explicit for the admitted singleton cubical collar, with its scale compatibility still exposed. Every low-action history has the local chart in Section 5, and Section 6 gives supported references and an absolute high-action separation. I have not proved the energy-controlled global numerator extension or the sharp reference inequality of `qr-decide` (6.3), and have not verified the collar's order of choices. The twist refutes only charging an identity-period-chart exit by positive action; it does not kill repaired S1–S4, (SP), or Yang–Mills existence. The selected next inequality is (AR), with its strict reduction and reason for expected truth above. The terminal decision is therefore a research stop, not a no-go theorem.

## 8. No-Go Discipline Gate

**Discharged — N1, actual routes and scope.** Five mechanisms were examined: the global identity-period chart (explicit zero-action counterexample); local axial gauges (proved on a fixed patch, insufficient for global energy); minimizing over the free exterior top (the quadratic localization in Section 3); an explicit smooth all-lines right inverse (supported reference and cutoff, insufficient for the sharp comparison); and an annular reset (the open (AR)). These are attempted mechanisms, not five ruled-out routes. There is no retained-authority claim and no packet PASS; the prescribed five-closed-family submission criterion is not met. The user forbids commits, audit packets, runners and extra files, so this scope check stays in this research note.

**Discharged — N2, dependencies without an invented wall count.** The local gauge plus an energy-controlled extension implies the numerator correction, as Section 5 proves. The supplied quadratic reserve plus that numerator comparison plus the sharp reference implies the action gap, as `qr-decide` (6.4)–(6.5) prove. For the remaining pairs (routing/extension), (routing/sharp reference), and (extension/sharp reference), neither implication nor independence is asserted; their relation is unresolved. They are not counted as independent obstructions.

**Discharged — N3 and N4, hidden conditions and matching.** The explicit conditions are singleton cubical collar admission, centre clearance, actual scale inequalities, nonwrapping local patches, smallness after fixed geometry, and the stated fixed-pattern logarithm convention. The class results cited from `c0-loc`, `lc-u` and `seam-nonlinear-c` concern admitted class backgrounds or stationary lifts. They do not match arbitrary numerator histories and are not cited as proving their chart coverage. Source labels and source numerical runs supply no additional premise.

**Discharged — N5 and N6, resolution and alternatives.** The negative example is a lattice-wide period statement; it is false as an obstruction on a contractible block, and no per-plaquette, per-mode or all-chart impossibility is asserted. Local charts, an atlas over flat periods, and an absolute annular reset remain legitimate mathematical alternatives. None requires a new physical axiom. No primitive-registry or audit-status claim is made.

**Unchecked — N7, strongest opposing argument.** A sufficiently low total Wilson action, unlike merely small individual plaquette flux, may allow a good shell gauge and a reset with bounded absolute cost. Once the patch is finite, its nonlinear remainders are ordinary Taylor estimates and private-bond corrections. Therefore the failure of a global identity-period chart gives almost no evidence against the desired local action gap. The concrete terminal obligation in this counterargument is (AR), followed by the sharp all-lines comparison; the existing class-lift arguments do not themselves deliver either for all numerator histories.

**Discharged — N8, prior warning checked within the read boundary.** Mapped Text 5.2 already distinguishes flat exterior holonomy from small amplitude and switches off an unjustified amplitude test near the core. `seam-nonlinear-c`, Section 4, similarly keeps its global relative-gauge input (REL) explicit, for a much more restricted stationary pair. Those warnings support keeping gauge coverage separate from curvature estimates. Neither is a proof that the present local route fails. No cross-attempt search or forbidden source was used.

## 9. Source boundary and current checkpoint

**Discharged — source record.** Repository content is at `c0a0dc4b0fe933f0f0378fdfd870ad07058aa299`. Required reads were `GOAL.md`; `FINISH.md`'s three named sections and row 65; `qr-decide.md` and `sp-decide.md` in full; `rarity-repair.md`, Section 7; mapped Text 3.1 and Text 5.2–5.3. Supporting bounded reads were `rarity-repair.md:26–83`; `relative-density-bound.md:145–170,325–371`; `c0-loc.md:1–105,181–235,361–435,521–610,1214–1286`; `lc-u.md:1–59,263–325,439–500,1102–1151`; `seam-nonlinear-c.md:1–104,446–540`; `curl-poincare-exterior.md:9–35,51–65`; and `one-window.md:41–103` for the failure of a one-link gain. Location searches in these allowed sources were retrieval aids, not additional proof coverage. Truncated required arguments were retrieved in bounded pieces before use. No forbidden independent-side text, gate, external proof account or literature was opened.

**Discharged — workflow and verification limit.** The pinned workflow was read by `git show`. The installed physics-loop entry was inspected for applicability; its campaign/delivery process was not invoked. The no-go-discipline entry was used for the scope check in Section 8; its bytes match the pinned repository version, and the user's one-file/no-audit/no-commit instructions govern delivery. Source inspection, editing and final scope checks are bookkeeping only. The evidence is the displayed hand arguments; there is no formalization, independent reviewer or computational certificate. No result recalled from memory is used without its proof; the shell-gauge expectation in Section 7 is explicitly unchecked.

**Gap — current recovery point.** Preserve Sections 3, 5 and 6: they respectively remove the global window norm, establish local coverage, and pay for high absolute actions without discarding them. Do not substitute the crude reference for the sharp one. The next target is precisely (AR), whose coefficient must be independent of radius although its threshold need not be. Geometry compatibility in Section 2 and the sharp all-lines action comparison remain exposed. Only `library/sp-nonlinear.md` was written; no editable prompt file, source file elsewhere, platform instruction or scientific status was changed.

STOPPED
