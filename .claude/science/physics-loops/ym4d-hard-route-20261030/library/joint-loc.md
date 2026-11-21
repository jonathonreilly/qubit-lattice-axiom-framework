# Joint localization of the old projection and the step response (row 148)
Provenance: OpenAI Codex, GPT-6 family (exact deployment identifier and runtime effort not exposed; requested effort: max); checkout `def5abd9bee7f4b71abe2f49df52afa8614c08d6`; Sussman–Alpoge source commit `31a47c543775`. Research text, not an audit; no status is granted.

## 1. Contract and source conventions

The target is rank 4's WF7, SA 15850–15866, with the exact hereditary restriction used by WF13 and OA7. Credit **Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text**, for the outline's windows, local pair domains, brackets, background constructions and consumer estimates. SA means `YM4_sketch_500.tex` at the pinned commit, fetched once to `/tmp/sa_ym4.tex`. Credit Tadeusz Balaban for the background-composition and propagator-localization mechanisms examined below. Credit Codex for `wf7-extension.md`, `old-depth.md`, `removed-fix.md`, and `pw-bridge.md`, and Claude for `wf-room-2.md` and `old-depth-gate.md`; their named premises and the corrections in their gates remain attached to every use.

The requested queue rows are 116, 126, 131, 135, 137, 139, 141, 145, 147 and 148. Row 147 is pending at this revision. Reading a proposed proof or its gate does not grant that proof additional status. This note distinguishes a finite algebraic localization, an analytic estimate uniform in volume, and identification with the actual layered box problem. None implies the other merely by terminology.

Only this file is changed. Text retrieval, bounded excerpts and file operations are bookkeeping; no run discharges a mathematical step. Repository methodology is read from this checkout's Git objects where absent from the sparse working tree. The pinned-source, one-file, no-agent and no-publication instructions govern this work.

Notation: `B` is the fixed current-cube base containing the inner box and all its read collars; `Q` is the remaining finite set of current cubes. The old scale in current units is `sigma = L^(j-k)`. The projected window includes the actual nonlinear average, its old critical background, its actual current, the assigned node representatives, and the step response. Anchoring means subtracting the value at `nu = 0`; the consumer uses its derivative there and its integral over `0 <= t <= 1`.

## 2. Counterexample first: what a single boundary comparison cannot prove

The previous counterexamples do **not** disprove joint localization. In `old-depth.md`, the first assigned current coefficient is `z^2 f`, while the old actual current coefficient is `z f`. Projecting first removes that mismatch by changing the extension. In `wf7-extension.md` (5.2)–(5.12), the remaining failure is that the old projection still reads deleted cubes. Putting a support tag on every old propagator as well as every step propagator can remove that failure. It must tag the dependence of the **baseline old background**, not just its fluctuation derivative.

There is, however, a precise obstruction to obtaining the required estimate from the single-collar bound alone. The following is a counterexample to that inference, **not** a Yang–Mills configuration or a no-go theorem for the requested localization.

**Lemma 2.1 (boundary decay does not bound rooted differences).** There are finite local, component-consistent families of entire anchored functions with uniformly bounded values and uniformly exponential dependence on distant domain changes, whose rooted differences are unbounded as the volume grows.

*Proof.* Work on the nearest-neighbour graph of current cubes, identified with `Z^4`; use a torus large enough that the following finite gadget does not wrap. Fix the root `o = (0,0,0,0)` and `B = {o}`. For an integer `r >= 2`, let

\[
 D_r=\{1,\ldots,r\}\times\{1,\ldots,2r\}^3,
 \qquad
 E_r=\{(x_1,x_2,x_3,x_4)\in D_r:
                         x_2,x_3,x_4\text{ all even}\}.
\]

Thus `|E_r| = r^4`. Let `S_r` be `D_r \ E_r` together with the four-edge path which successively changes coordinates 1, 2, 3 and 4 from zero to one, excluding `o` itself. The set `B union S_r` is connected: from any point of `D_r \ E_r`, keep one odd coordinate among the last three fixed, move the other coordinates to 1, then move the retained coordinate to 1. Every point of `E_r` is adjacent to `S_r` by reducing its second coordinate by one. Every gadget vertex is within graph distance `7r` of `o`.

For any active set `A` containing `B`, define

\[
 f_A(\nu,a)=\nu a\,e^{-7\mu r}
      \mathbf1_{\{S_r\subset A\}}
                 (-1)^{|A\cap E_r|},\qquad \mu>0.       \tag{2.1}
\]

Here `a` is one scalar coordinate at the root, with `|a| <= 1`; take `|nu| <= 1`. If `S_r` is present, all relevant vertices are in the root component; otherwise the function is zero. Consequently disconnected extra components are ignored, and the family reads only `A`. It is entire in its continuous variables and vanishes at `nu = 0` and `a = 0`. Its value is at most `exp(-7 mu r)`.

If two active sets agree on the graph ball of radius `d` about `o`, their difference is zero for `d >= 7r`. For `d < 7r`, it is at most `2 |nu a| exp(-7 mu r) <= 2 |nu a| exp(-mu d)`. The same estimate holds after the anchored derivative. All continuous derivatives away from the root are zero. Thus uniform holomorphy, component locality and a single boundary-distance estimate are present.

The Boolean interpolation of `wf7-extension.md` (6.1), with these domain values, is exactly

\[
 {\cal F}(\theta;\nu,a)=\nu a e^{-7\mu r}
       \prod_{x\in S_r}\theta_x
       \prod_{x\in E_r}(1-2\theta_x).                  \tag{2.2}
\]

Indeed summing a spine flag gives `theta_x`, and summing a parity flag gives `(1-theta_x)-theta_x`. Other flags give one. Differentiating once in every gadget flag, then integrating each derivative from zero to one, gives the root bracket

\[
 {\cal F}[S_r\cup E_r\mid B]
             =\nu a e^{-7\mu r}(-2)^{r^4}.             \tag{2.3}
\]

At `nu = a = 1` its magnitude diverges: `r^4 log 2 - 7 mu r` tends to infinity. On the complex polydisc `|theta| <= R`, `R > 1`, evaluation at `theta_x = -R` has magnitude
`exp(-7 mu r) R^{|S_r|}(1+2R)^{r^4}`. This also diverges. These are exact finite products, with no machine enumeration. The graph degree is eight and the base has one cube throughout. The same example can be multiplied by any fixed nonzero proposed removed amplitude; the volume loss remains. This proves the lemma. \(\square\)

The lemma rules out promoting `wf7-extension.md` (4.8) to a bound for (6.1) merely by saying that the functions are local, holomorphic and exponentially insensitive to the boundary. It does not satisfy the old constrained saddle equations, and therefore is not evidence that those equations lack a stronger expansion. In particular the fixed-second-order Cauchy argument in `wf-room-2.md`, Lemma Q, must not be iterated without new estimates: at order `n`, choosing the largest of `n` distances only gives a decay rate divided by `n`, not a uniform connecting-tree estimate.

## 3. The exact finite reduction

Suppose, for this section only, that every required cut-down old problem exists on its specified local pair domain, with compatible assigned representatives, and that its composed step response has the same component restriction. Denote its anchored window by `f_A(P;s)`. These are the **finite-map hypotheses FM**, not a conclusion about arbitrary cut-downs of the actual problem.

Define the domain differences

\[
 c_C(P;s)=\sum_{D\subset C}(-1)^{|C\setminus D|}
                                  f_{B\cup D}(P;s).
                                                               \tag{3.1}
\]

Then the extra interpolation is exactly

\[
 {\cal F}(\theta,s;P)=\sum_{C\subset Q}\theta_C c_C(P;s),
 \qquad \theta_C=\prod_{x\in C}\theta_x.               \tag{3.2}
\]

To verify it, expand each factor `1-theta_x` in (6.1). The coefficient of `theta_C` is precisely (3.1). Conversely, summing `c_C` over `C subset E` gives `f_(B union E)`: the coefficient of `f_(B union D)` in that sum is `(1-1)^{|E\D|}`, zero unless `D = E`. This proves completeness without an estimate. Setting flags outside `Y` to zero leaves only functions of `P|Y`; summing choices in a disconnected component shows independence of its flags. These conclusions remain true after setting `theta = s`, provided the step response also has the stipulated restriction. Anchoring, a `nu` derivative and the finite `t` integral commute with these finite identities.

The missing quantitative input is visible in the exact formula. A sufficient estimate is

\[
 \sum_{C\subset Q} R^{|C|}
       \sup_{P\in{\cal D}_{B\cup C},\ |s|<R}|c_C(P;s)|
       \le H_{j,z},                                  \tag{3.3}
\]

uniformly in the finite volume, with compatible local charts for the restrictions. It bounds the diagonal interpolation on its whole polydisc. For a removed origin one needs `H_(j,z)` with the old-depth exponential and the member Cauchy factor retained. Estimate (3.3) is **not asserted here** for the actual old maps. Lemma 2.1 disproves its deduction from a uniform bound on each `f_A` and a single boundary comparison.

## 4. What is used from Balaban, with the mechanism rebuilt

The bounded readings are CMP **109**, pp. 257–258, 261–263, 270–280, especially (3.3)–(3.4), (3.18)–(3.28), (3.38) and (3.48)–(3.52); CMP **99**, 389–434, Section C, pp. 408–410, and pp. 426–427, Theorem 3.14 and the following discussion of branching expansions; CMP **119**, pp. 256–257, 275–276 and 279–280. The supplied folder contains CMP 109, 119 and 99b, but no CMP 116. Its localization theorem has not been read or imported. The OCR formulas are not used as unquestioned identities: the precise algebra used here is written below. These sources distinguish three operations.

**Critical composition.** Write `M_S` for the actual determining average and `Phi_S` for the admitted critical branch. Let `S'` be memberwise contained in `S`, with aligned blocks and fixed level-zero boundary rows. A variation preserving the `S'` averages extends by zero to a variation preserving the `S` averages: induct through the averages; each exterior row is fixed or has its whole double-block carrier outside the smaller member. Every crossing plaquette contains only fixed collar variations. Thus stationarity of `W = Phi_S(v)` implies stationarity of its restriction at `M_(S') W`. The named **BG** input (regular-orbit uniqueness and its holomorphic continuation) identifies the two backgrounds modulo the specified residual gauge. The explicit axial recursion **AX** fixes that gauge. Equality on a real open datum ball implies equality of complex Taylor coefficients, and hence equality on overlapping balls of the common connected chart. This continues in the critical datum, not in additional independent variables held fixed on the real locus.

Consequently, for an admitted path `V(t)` with critical physical endpoints, gauge invariance and the fundamental theorem of calculus give

\[
 G(P_1)-G(P_0)=\int_0^1\partial_t
       G\bigl(\Phi_{S^{\le j}}(M_{S^{\le j}}V(t)),
                  J(\Phi_{S^{\le j}}(M_{S^{\le j}}V(t)))\bigr)\,dt.
                                                               \tag{4.1}
\]

The derivative is linear in the inserted direction, so a partition of unity gives the windows. This rebuilds the composition mechanism in CMP 109 (3.3)–(3.4). It makes no claim of local dependence before the final localization; Balaban explicitly postpones that operation on p. 276.

**Propagator localization.** Suppose a finite-range operator `K` has admitted local inverses `S_c`, cutoffs `chi_c, psi_c`, and a parametrix `P = sum_c chi_c S_c psi_c` satisfying

\[
 KP=I-E,\qquad \|E\|<1.
\]

Then `P sum_(n>=0) E^n` is a right inverse: multiplication by `K` telescopes to `I-E^(N+1)` for the partial sum, and its remainder tends to zero. If `K` is invertible it is `K^(-1)`. Expanding each product in its local indices gives a walk. Each term reads the union of the **complete** local coefficient and cutoff read sets. A nonlocal coefficient, including a background hidden in `K`, must itself be expanded before this is a local formula in the input field.

Here is the quantitative part needed below. Suppose, in normalized native local norms, a walk with `n` transitions is bounded by

\[
 A q^n\exp\{-\tau\textstyle\sum_{i=0}^{n}d(x_i,x_{i+1})\},
 \qquad \sup_x\sum_y e^{-\tau d(x,y)/2}=K_\tau<\infty.
                                                               \tag{4.2}
\]

Let `t` be the infimum of the sum of leg lengths over the permitted intermediate cells. Reserve half of the exponent for `t`. Sum the remaining factors backwards, one intermediate cell at a time, using the displayed row sum and dropping an unused final factor bounded by one. This gives `A (q K_tau)^n exp(-tau t/2)`. If there are at most `N_0 N_1^n` walk choices per root and `N_1 q K_tau < 1`, summing the geometric series is uniform in volume. These are explicit hypotheses on terms, not a bound inferred from the norm of their sum.

For two determining problems, match only the walks whose **full** read sets and coefficients agree. In their difference those terms cancel. A remaining walk reaches the disagreement set. If its output and input are at distances `D_x,D_y` from that set, its visiting length is at least `D_x+D_y-c_*`, where `c_*` pays the fixed read-set enlargement. Reserving an additional fraction of (4.2)'s exponent gives the boundary factor. Exterior intermediate cells are summed with their own problem's metric and row sum. This is the algebra of CMP 99b Theorem 3.14, with the symmetric-read-set and native-tail correction of `removed-fix.md` Sections 3–5 made explicit. It does not compare the old box to the current-depth system.

**Joint tags, not separate small errors.** A connected carrier with length `t` and read radius `r_*` intersects at most

\[
 b_0+b_1t/\ell_{\mathsf P}                              \tag{4.3}
\]

current parameter cubes, when `ell_P > 8 r_*` and the stipulated cube-count condition holds. To see this, traverse a tree covering the carrier twice, divide the traversal into arcs of length at most `ell_P/4`, and enlarge by `r_*`. Each piece has diameter less than `ell_P/2` and meets at most sixteen cubes under that condition. There are at most `1+8t/ell_P` pieces, so one may take `b_0=16, b_1=128`. This is also the count rebuilt in `pw-bridge.md` (6.4). Tag the union of read sets, including the old background, node factors and step branches. On `|s_Delta| < R`, its monomial costs at most `R^b_0 exp(b_1 log(R)t/ell_P)`. Choose the parameter size so that this consumes at most one reserved fraction of the decay rate. Products and branches join carriers; they are not estimated as unrelated global suprema. The next section makes this elementary mechanism precise.

CMP 119 (2.14)–(2.15) retains old determining rows in the interior and introduces new rows in the collar. Its p. 276 also changes the window scale to the local layer's scale. Both facts matter here. In particular a change of units does not change `exp(-c M)` into `exp(-c M/sigma)`.

## 5. A constructive bound for joint supported expansions

This section proves a sufficient theorem from local coefficient data. It does **not** assume that the nonlinear old projection already has the desired bound. It specifies what must be verified about its defining equations; that verification is left visible in Section 8.

A supported coefficient is a holomorphic function of the pair on a finite carrier, including its complete datum and geometric read sets. On overlapping local domains use the same function, pulled back by restriction. Associate to each term a finite connected collection of paths, its total nonnegative length `ell`, and a finite nonnegative integer multi-index `m` on current cubes outside the fixed base. Every cube intersecting the declared carrier outside the base must have positive multiplicity, including connecting paths even where their coefficients are constant. A primitive walk may give multiplicity one to every cube of its complete carrier. Multiplication joins carriers that meet, adds lengths and **adds multiplicities**. Matrix products keep their order.

Use ordinary convolution on these multi-indices: the coefficient at `m` in `F star G` is the sum of `F_(m1) G_(m2)` over `m1+m2=m`. The tag is `s^m=product_Delta s_Delta^(m_Delta)`. Evaluation at complex flags is now multiplicative, so ordered products, exponentials and convergent inverse series retain their matrix identities there. Replacing multiplicity by set union would be a different algebra: it is multiplicative only at flags zero or one and cannot establish the assigned node identities on the full complex discs. The stronger multiplicity norm below is therefore intentional. Decoupled primitive propagators still need not be inverses of their unmodified operators at complex flags.

On terms rooted at a fixed output, use the absolute norm

\[
 \|F\|_{R,\mu}=\sum_\omega
          R^{|m_\omega|}e^{\mu\ell_\omega}
          \sup_{{\cal D}_{\operatorname{supp}m_\omega\cup B}}
                         |F_\omega|.                 \tag{5.1}
\]

Here `|m|=sum_Delta m_Delta`. For operator terms include the sum over input cells and use normalized input/output norms; take the supremum over output cells. The local pair domains must restrict to the domains of all coefficients being multiplied. Since
`R^{|m1+m2|}=R^{|m1|}R^{|m2|}`, and lengths add, absolute convergence proves
`||F star G||_(R,mu) <= ||F||_(R,mu)||G||_(R,mu)`.
The proof is simply the sum of the product of the two absolute majorants; for operators, sum the intermediate cell first. This is valid also for ordered, noncommuting matrix coefficients.

**Theorem 5.1 (local-coefficient implication).** Assume the following data on one common family of local pair domains. The radius R, length rate mu > 0, normalized bounds and contraction constants are uniform in volume. For the WF application require them uniformly also in j,k, with only the displayed radii and scale factors varying. Finiteness separately on each finite lattice would not meet this hypothesis.

1. **CP-linear:** the primitive old and step inverses, all their needed output blocks, and local source maps have expansions with complete read sets and finite norms (5.1). Their all-one sums are the specified physical operators. They are constructed on separated cut-downs with the actual row, action and node conventions. Interior terms of two problems agree whenever their complete read sets agree.
2. **CP-nonlinear:** after the chosen linear reductions, the unknowns obey a system `x = e + sum_(m>=1) T_m[x,...,x]`. Each local multilinear coefficient, including its linear propagators, has a supported expansion as above. In the multiplicity norm (5.1), its operator norm is at most `a_m`, the forcing norm is at most `epsilon`, and

   \[
   \sum_{m\ge1}m a_m(2\epsilon)^{m-1}\le\tfrac12.
                                                               \tag{5.2}
   \]

   Coefficients may be jointly holomorphic in the independent current and the fluctuation coordinates. They are actual coefficients of the specified equations, not just coefficients of a pointwise majorizing function.
3. **CP-identification:** at all flags one, the small solution is the actual old projected background and specified step response, with the stated physical endpoints. On the fixed inner box its analogous small solution is WF4 in its admitted Landau chart for the full allowed parameter arguments, not merely at all flags one. All output pairs, datum paths, and the separate inner and removed multiplier discs have the margins needed for the member evaluations. The assigned node recursion is applied to its prescribed arguments; equality with an arbitrary different gauge is not allowed.

Then the support-labelled Picard construction converges, is jointly holomorphic on the stated local domains, and defines an exactly hereditary interpolation. It has a volume-uniform complex sup bound. If the matched old/full and old/box equations differ only at their collar, a difference at an output at old distance `D` from that collar has the additional factor `exp(-mu D)`, up to a fixed read-set correction. The anchored first response retains that factor.

*Proof.* Expand products in the reduced equations by ordinary multi-index convolution, retaining every coefficient's read set and tag multiplicity. Start at zero. If `||x|| <= 2 epsilon`, then (5.2) gives

\[
 \Big\|\sum_{m\ge1}T_m[x^m]\Big\|
 \le\sum_{m\ge1}a_m(2\epsilon)^m\le\epsilon.
\]

For `||x||,||y|| <= 2 epsilon`, telescope the `m` ordered slots. There are exactly `m` terms, each bounded by `a_m(2 epsilon)^{m-1}||x-y||`. Hence the nonlinear map has Lipschitz constant at most one half. Consecutive Picard iterates differ by a geometric sequence in the complete absolute coefficient norm; their sum converges. The same calculation proves uniqueness in the ball. On every compact subdomain the holomorphic coefficients converge absolutely and uniformly. Passing their Cauchy integrals to the limit proves joint holomorphy.

Every term is a connected expression from its output to its inputs, by induction through the local vertices and linear carriers. If flags vanish outside `Y`, any term reading a cube outside `Y` has a zero tag. Surviving terms read only the pair and the geometry on `Y`. A wall component missing the root contributes no term. At all flags one the primitive operators and coefficients are the original ones; uniqueness and CP-identification give physical completeness. On the complex polydisc the sum is bounded by (5.1), since each monomial is at most `R^{|m|}`. There the products remain ordinary products of the tagged primitive maps, but it is not asserted that the unmodified saddle equations hold.

For the boundary comparison, pair identical expression trees in the two Picard expansions. Any unpaired tree contains a coefficient or source whose read set reaches the disagreement collar. Its connected path from the tested output has length at least `D-c_*`. Its unweighted norm is consequently at most `exp[-mu(D-c_*)]` times its contribution to (5.1). Sum the two absolute majorants. This argument needs a common expansion of the **equations and sources**, not merely two existing functions with bounded values; Lemma 2.1 explains the distinction.

For a response parameter `nu`, subtract its value at zero, or differentiate the coefficient equation. The derivative solves a linear equation with operator norm at most one half; its inverse is bounded by `sum_(n>=0) 2^(-n) = 2`. A marked differentiated tree retains the same collar-reaching path. Require the differentiated right-hand side, with the unknown derivative removed, to have norm at most `C delta_k sigma_j` in the supported norm (5.1), using old normalized input/output units, uniformly along the `nu` segment. This is stronger than a bound on its all-one sum. Its difference then has bound

\[
 C|\nu|\delta_k\sigma_j e^{-\mu(D-c_*)}.             \tag{5.3}
\]

The complete-data Cauchy neighbourhood is required for this differentiation. First derivatives of local coefficients also enter if the parameter changes those coefficients; include them in the stated forcing derivative after differentiating, rather than holding them fixed. The inverse bound still applies. This proves the theorem. \(\square\)

**Assigned nodes.** The theorem includes matrices, so it also includes the actual axial recursion provided its factors satisfy CP-linear/CP-nonlinear. More explicitly, at an admitted chart with fixed reference contour factors, write each relative factor as `I + v_q`, with coefficient-norm bound `||v_q|| <= c r xi_q/xi_n` down a pillar of top scale `xi_n`. Its ordered product has norm at most

\[
 \prod_q(1+\|v_q\|)\le
             \exp\{c r\textstyle\sum_q\xi_q/\xi_n\}
       \le \exp\{c r/(1-L^{-1})\}.                  \tag{5.4}
\]

The inverse factors have the convergent series `sum_(-v_q)^(star m)` when their norms are less than one. Differentiating the ordered product inserts a single differentiated factor in every possible position; (5.4) bounds the other factors, and the same geometric sum bounds the derivative. A collar mark on that factor is retained. For a current, direct differentiation of `g J g^(-1)` adds `[dot g g^(-1),g J g^(-1)]`. Thus one must retain the pre-existing current norm in the node term; bounded condition numbers of two independently chosen gauges do not compare their difference. With `U^g(b)=g_- U_b g_+^(-1)`, the lower-tower transport remains `g_Z u^(-1) vtilde^(-1)` in that order. This is the AX mechanism and the repair in `wf-room-2-gate.md`, not a choice of polar decomposition at complex input.

**Rooted brackets.** For the interpolated anchored member `Psi`, the theorem gives a sup bound `H` on `|s_Delta| < R`, uniform in volume. Cauchy on separate circles around each real integration coordinate, of radii tending to `R-1`, gives

\[
 |\Psi[K\mid B]|\le H(R-1)^{-|K|}.                 \tag{5.5}
\]

No factorial occurs because each coordinate is differentiated once. The `nu` derivative can be taken on its separate circle, and the `t` interval has length one. The carrier rooting makes a bracket zero when an active component carrying a differenced cube misses `B`. These are the identities used by the finite FTC of WF13. Its spatial-rate allocation additionally requires the stated radius `R=exp(kappa-bar)` with its rate reserve; a bound at an arbitrary radius just above one would not suffice.

For clarity, the passage from pair differences to member differences also needs the undifferentiated comparison. Write the two output pairs in their common member chart as `p,q`. Require the coefficient construction to give `|p-q| <= C alpha_j exp(-mu D)`, `|dot p|+|dot q| <= C delta_k sigma_j`, and `|dot p-dot q| <= C delta_k sigma_j exp(-mu D)`, throughout the parameter domain and with the segment joining the pairs admitted. The first is the undifferentiated tree estimate when its forcing radius in these output units is at most `C alpha_j`; the other two are the differentiated estimates above. For a member bounded by `g_j`, its common margin gives `|DG| <= C g_j/alpha_j` and `|D^2G| <= C g_j/alpha_j^2` by one- and two-variable Cauchy. In
`d(G(p)-G(q))/dnu = DG(q)(dot p-dot q) + (DG(p)-DG(q))dot p`,
integrate the second derivative along that segment. Both terms are at most `C(g_j/alpha_j)delta_k sigma_j exp(-mu D)`. Integrating in `nu` yields the removed member amplitude `C(g_j/alpha_j)|nu| delta_k sigma_j exp(-cM/sigma_j)`. This uses ordinary evaluation of the member on the admitted interpolated pair; it does not require that complex flag values solve the old saddle equations. A finite sum of old members is taken before the inner bracket, as WF13a requires.

The theorem offers a concrete construction from primitive coefficient data. It does not identify CP-linear for a global old background merely by identifying the step propagator: the old background can already occur in the coefficients of that propagator. It also does not derive CP-nonlinear from a summed first-response estimate. These are the two shortcuts that would conceal the unresolved part of this task.

## 6. Flat response tests: the Cartan tail and the vacuum coefficient

Here is a nontrivial positive test of the construction. Its scope is the translation-invariant Cartan slice of wf7-extension Section 5.1, and its linear old response. It is not the full nonlinear WF4 map on arbitrary four-dimensional local pairs.

In the notation of that section, set
\[
 A={L^2-1\over6L},\quad B=L-2A={2L^2+1\over3L},
 \quad T=B I+A(S+S^{-1}),\quad
 q={2A\over B}={L^2-1\over2L^2+1}<\tfrac12,             \tag{6.1}
\]
where \(S\) shifts the old-block index on a finite periodic chain. The scalar saddle equations in that note can be checked directly: inside a block,
\(a_{mL+r}=y_m+(r+1)s_m-\lambda_m r(r+1)/2\); averaging and matching the next block gives
\(u_{m+1}-u_m=A s_m+B s_{m+1}+A s_{m+2}\).
Summing slopes fixes the periodic potential, and a common additive constant fixes the mean. Hence the actual old current multiplier is
\[
 \lambda={1\over L}(2I-S-S^{-1})T^{-1}u.              \tag{6.2}
\]
The remaining four-dimensional saddle equations vanish on this slice: the sole direction-2 component is independent of coordinate 2, its row multiplier annihilates the site-gradient part of the average, and other colour components vanish to first order. The named flat uniqueness input therefore identifies (6.2) with the derivative of the actual old background. This is exactly the scalar mechanism producing the nonzero remote derivative in (5.6) of the previous note.

Expand
\[
 T^{-1}={1\over B}\sum_{n\ge0}
                  [-A(S+S^{-1})/B]^n.                \tag{6.3}
\]
Its \(n\)th term is a sum of \(2^n\) nearest-neighbour walks, each of absolute weight \(B^{-1}(A/B)^n\). The geometric bound \(q<1/2\) proves absolute convergence by hand and verifies the inverse by multiplication and telescoping. This does not rely on a numerical Green kernel.

Divide the old blocks into slabs of \(h\) consecutive blocks, with the periodic length divisible by \(h\). Assign parameter flags to these slabs, and put a flag on every slab visited by a walk, including its source and output. Root-base flags are fixed to one. A walk of \(n\) steps visits at most \(2+n/h\) distinct slabs. The bounded extra row/current stencil in (6.2) changes 2 to a fixed \(b_0\), and nothing depends on the chain length. Repetitions of a visited slab do not introduce another flag. Choose
\[
 h\ge\max\{1,4\log R/\log2\},\qquad
                      \mu={\log2\over4}.
\]
Then \(qR^{1/h}e^\mu<2^{-1/2}<1\). Therefore the tagged inverse has the absolute length-moment bound
\[
 \sup_m\sum_{v,\omega:m\to v}
 R^{|C_\omega|}e^{\mu n(\omega)}
                B^{-1}(A/B)^{n(\omega)}
 \le {R^{b_0}\over B(1-2^{-1/2})}.                   \tag{6.4}
\]
The current map costs in addition at most \(4/L\), by the three coefficients in (6.2). Bounds hold on every complex flag polydisc, uniformly in the number of blocks. If a source is at old-block distance \(d\) from the root, the walks reading it have \(n\ge d-O(1)\). The same estimate gives \(C_R e^{-\mu d}\). If a flag is zero, all walks reading that slab disappear exactly. On a surviving component, the remaining formula depends only on its local data. At all flags one, it is (6.2). For the inverse before its finite current stencils, surviving walks equal the Neumann expansion of the compressed tridiagonal matrix with diagonal \(B\); no global completion of the local datum is needed.

This last local continuation is a definition. At a new boundary it need not be the old first-rule nonlinear box problem, whose lower collar rows are different. It supplies a positive analytic localization of the global flat derivative, not that missing box identification. Slab flags test the scalar sector; they are not the full four-dimensional independent cube flags of WF7.

For the current-square member (5.10), restrict two data directions \(u,v\) to this Cartan sector and write \(J=\epsilon\lambda[u]+a\nu\lambda[v]\) to the relevant order. Its mixed coefficient is the finite sum of \(2\operatorname{tr}(\lambda[u]\lambda[v])/2\), with that member's stated normalization. Define its extension by multiplying the two tagged responses: their walks join at their common output, and repeated flags keep their multiplicities. Formula (6.4), twice, bounds the sum of absolute coefficients; (5.1)'s product inequality proves the complex bound. If \(u\) is supported in a deleted slab, every term in this mixed coefficient contains that slab's flag, so the coefficient is **zero**, rather than a small nonzero tail. It agrees with the physical coefficient at all flags one. The coefficient is unaffected by the \(\nu=0\) subtraction or by the unit-length \(t\) integral, since at this Taylor order it is independent of \(t\). At the flat zero-current base, differentiating a node conjugation contributes a commutator with zero current; the first current jets, and hence their current-square coefficient, are unchanged.

Thus the nonzero-tail calculation does not extend to a no-go theorem once the old response is tagged. This explicit calculation tests the current-square mechanism in its scalar sector.

### 6.1 The actual four-dimensional test coefficient, conditional on flat local inverses

One can also treat the precise first nonzero coefficient of (5.10), rather than substitute an arbitrary scalar fluctuation for its R9 direction. This uses an additional named input and has weaker uniformity than WF7.

Call **FW** the flat instances of [Energy] and [Walk geometry] in pw-bridge Section 6: separated local inverses have exponential local energy bounds, the two-difference cutoff commutators cost \(C/M_1\), their overlap and walk counts are bounded, and their full fixed-region field carriers have radius \(C_LM_1\). Use the graph-norm repair of h-walk-gate Section 5 and only its fixed-region field-locality conclusion in Sections 6–8. No comparison of two different region sequences is made in this subsection. Claude's h-walk Sections 5–7 and Codex's gate are the sources of this input; it retains their conjugation/invertibility dependencies. The following implication does not re-establish those dependencies.

Fix finite depths \(j,k\), fixed geometric parameters and the flat, constant-top periodic sequences used by wf7-extension Section 5. The period may grow. Let \(K_j\) be the derivative of the actual old average, \(H_j\) its flat constrained lift, and \(\mathscr L_j\) the flat Wilson Hessian, with the prescribed unit conversions. Flat lift and gauge invariance give
\[
 A_j:=D(J\circ\Pi_j)(1)=\mathscr L_j H_jK_j.           \tag{6.5}
\]
Indeed the differentiated constrained field is \(H_jK_ju\) up to the derivative of its assigned gauge. That extra field is a gradient at the flat connection, and the Hessian annihilates gradients: its quadratic form is the square of the discrete curl, whose value on a gradient is zero. Here \(H_j\) is understood as the lift for the raw datum. When using the straightened lift in FW, the raw-to-straightened node change adds a coarse gradient. Its critical lift has zero current, since the corresponding pure-gauge configuration is critical and BG identifies its orbit. Thus it makes no change to (6.5). \(K_j\) and \(\mathscr L_j\) have finite read sets at these fixed depths.

Here is the required absolute expansion, derived from FW. Form the parametrix and its commutator remainder as in Section 4. Decompose each source and intermediate output into native cells. The local inverse and commutator bounds give (4.2); the native shell count on these constant-top four-dimensional lattices bounds \(K_\tau\) by a constant times \(\sum_{r\ge0}(r+1)^4e^{-\tau r/2}\), which converges by its successive-ratio limit. Choose \(M_1\) so the walk count times the commutator factor times \(K_\tau\) is below one half. The telescoping identity and the summed geometric series then prove the inverse expansion. Include every local-model box and both endpoint stencils in each carrier.

At a fixed mesh, energy controls point evaluation: a field mass term \(\eta^4m^{-2}|a_b|^2\) in the local squared norm implies \(|a_b|\le m\eta^{-2}\|a\|_E\). Each native cell contains only finitely many fine bonds, bounded in terms of \(j,k,L,M_1\), independently of the period. The absolute row sums of the finite matrices \(K_j\) and \(\mathscr L_j\) have the same independence. Thus the energy walk estimate gives an absolute pointwise row estimate for \(A_j\), with a finite constant allowed to depend on the fixed meshes. This step deliberately makes no mesh-uniform PW claim for the current.

Put independent flags on the full four-dimensional current parameter cubes. For an old carrier of length \(t\) in old units, its length in current units is \(\sigma_jt\le t\); its fixed read radius changes by the same factor. The count (4.3), with the old and step read radii both included, therefore bounds its tag just as for a step walk. First fix \(R\), then enlarge the parameter cube size to pay for the tags with one reserved part of the decay rate. Summing the remaining endpoint exponential and walk factor gives
\[
 \sup_x\sum_{y,\omega}R^{|m_\omega|}
                 |(A_j)_\omega(x,y)|\le C_{j,k,R},
 \qquad
 \sup_x\sum_{c,\beta}R^{|m_\beta|}
                 |(H_{1,k})_\beta(x,c)|\le C_{j,k,R}. \tag{6.6}
\]
The constants are independent of the period. At the flat zero-current pair, every inserted branch coefficient \(H_\beta^{\mathsf T}\mathbf J\) is zero. Hence the second expansion is precisely the zero-branch tangent of the specified R9 system, whose remaining nonlinear terms have zero derivative at zero. It is not an assumed equality between two unrelated decoupled lifts.

Write \(\widehat A_j(s)\) and \(\widehat H_{1,k}(s)\) for these tagged sums. They agree with the physical derivatives at all flags one. Let \(u=\partial_\epsilon\mathbf U_\epsilon|_0\) be the bare direction supported in the deleted slab of wf7-extension Section 5.2, and \(b=\partial_aB'(a)|_0\) its actual fluctuation direction from Section 5.3. Define the extension of that test coefficient by
\[
 \widehat C(s)=
 {2\mathfrak d_j e^{-\kappa d_j(X)}\over C_J\alpha_j^2}
 \sum_{e\in\mathcal S_z}\frac12\operatorname{tr}
 \left((\widehat A_j(s)u)_e\,
       [\widehat A_j(s)\zeta\widehat H_{1,k}(s)b]_e\right).
                                                               \tag{6.7}
\]
Ordinary multiplication retains repeated flags. The two old walks and the step walk have connected union after joining them at their displayed outputs and source insertions. The cutoff has its prescribed fixed support and norm. Multiplying the three absolute row bounds (6.6) therefore bounds (6.7) on the entire complex flag polydisc, uniformly in the period, by a constant times
\(\mathfrak d_j e^{-\kappa d_j(X)}\alpha_j^{-2}
C_{j,k,R}^{\,3}\|u\|_\infty\|b\|_\infty\).
The finite trace sum changes only its constant.

Every term in the first factor which reads \(u\) has a tag in the deleted slab. With those flags zero, \(\widehat C(s)=0\) exactly. At all flags one, (6.7) is the coefficient (5.12). At zero base current, every second derivative of the projected current multiplies that zero current and drops out; differentiating the assigned node conjugation adds a commutator with zero. The same product rule shows that this coefficient is independent of \(t\), and the \(\nu=0\) subtraction does not change it. Thus the exact coefficient which killed the old undecoupled extension has a jointly localized replacement for its actual four-dimensional R9 direction, from FW and Flat lift.

This is only a Taylor-coefficient implication. Its constants may depend on \(j,k\); it supplies neither the old-age factor of WF7 nor a common nonlinear complex core. In particular it does not prove the full member (5.10) at arbitrary inputs. No higher-order coefficient bound follows from (6.7).

## 7. Layered identification: the exact criterion and a seam test

Let \(S^{\le j}\) be the old truncated sequence with members \(\Omega_q\), and let \(T_q(R)\) be the prescribed first-rule tower of the full enlarged box, cut at \(j\). The old localized problem in the comparison is
\[
                         S_R(q)=\Omega_q\cap T_q(R).    \tag{7.1}
\]
There is an elementary sufficient criterion for its exact identification with WF4:
\[
 R\subset\Omega_p\quad\hbox{for some }p\ge j
 \quad\Longrightarrow\quad S_R(q)=T_q(R)\quad(0\le q\le j).
                                                               \tag{7.2}
\]
Indeed \(T_q(R)\subset R\subset\Omega_p\subset\Omega_q\). The determining bonds, omitted inward rows, level-zero boundary rows, contour carriers and nodes then coincide. Using the same nonlinear datum, the same inner-plaquette action and the same assigned axial/Landau convention gives the same map by BG uniqueness and continuation. This is an equality of problems, not just a comparison of metrics. If only the interior tower members lie in \(\Omega_q\), that proves only interior agreement and a collar comparison, not (7.2).

The repaired layered quantifier **LQ** in wf-room-2 Section 3 imposes \(Z\subset X\cap\Omega_p\), with tower depth at most \(p\), separately for every preceding structure. Consequently (7.2) applies whenever the **entire box being used**, including the fixed read collars, is such a \(Z\) for all the relevant structures. It is not enough that the pointed member \(X\) or its centre is in \(\Omega_j\). SA 16137–16176 names an enlarged \(R_z\); it does not itself prove this containment for every layered filing. For a boundary-layer window of physical scale \(\xi_p\), the geometric old distance is \(M\xi_p/\xi_j\), as in CMP 119 p. 276. It equals \(M/\sigma_j\) with the WF convention only when \(p=k\). A separate decay from the integrated field may also be present, but the two factors must be retained separately.

Here is an infinitesimal configuration showing why a lower-layer seam cannot be ignored. It tests an enlarged box allowed to cross below level \(j\); it is excluded if (7.2) is imposed.

Take \(j=1\), odd \(L\) sufficiently large, a large torus, \(\Omega_0\) the torus, and \(\Omega_1\) a large aligned slab. Choose a box \(R\) crossing its boundary, and an entire old block \(Q\) in \(R\setminus\Omega_1\), far from both the seam and \(R\)'s outer collar. Its first-rule tower has \(Q\subset T_1(R)\). In the meet problem every bare bond near \(Q\) is a level-zero determining row. The meet background therefore equals its input on that neighbourhood in constraint coordinates.

Put a \(3^4\)-site bare patch strictly inside \(Q\), including a free bare collar around it. There are \(4\cdot2\cdot3^3=216\) positively oriented patch edges and \(3^4=81\) vertices. The scalar divergence-free edge space has dimension \(216-81+1=136\): the incidence matrix of a connected graph has rank \(V-1\), since its transpose kills exactly the constant vertex functions. A perturbation supported in this patch can affect at most the eight unoriented old determining bonds incident on the node of \(Q\), because the actual average reads only the double block at its endpoints. Reverse orientations add no independent tangent equations. Hence the derivative of the pure tower's raw averages has at most eight scalar rows on this space. There exists a nonzero real divergence-free vector \(a\) supported in the patch with \(K_Ta=0\). This is an existence construction by finite-dimensional linear algebra; it does not select or enumerate vectors by machine.

Take the colour \(T=\operatorname{diag}(1,-1)\) and the small real field \(V_\epsilon(b)=\exp(i\epsilon a_bT)\), with the fixed potential-to-link factor absorbed in \(\epsilon\). The derivative at zero of the pure-tower background in a fixed constraint representative is zero, since its determining datum derivative is zero and BG is differentiable. Any additional assigned gauge contributes a gradient, so its actual current derivative is still zero. In constraint coordinates the derivative of the meet background is \(a\) on the patch and its adjacent stencil, since these bare bonds are fixed rows. Its actual current derivative is therefore the Wilson Hessian applied to \(a\), independently of the assigned gauge, and is nonzero somewhere in that neighbourhood. To verify the last assertion, if \(d^*da=0\), the energy identity gives \(da=0\); also \(d^*a=0\). Expanding the commuting forward/backward differences gives the flat lattice identity \(d^*d+dd^*=\) componentwise scalar Laplacian. Its quadratic form is a sum of squares of differences. Thus every component of \(a\) is constant on the torus, and its compact support forces zero, a contradiction.

At each finite lattice choose a nonzero \(\epsilon\) sufficiently small. Every relevant simple inequality and admitted hereditary chart is strict at the flat field; finite-dimensional continuity supplies room. Unequal first derivatives therefore give unequal actual maps for small inputs. At zero current a differentiated gauge transformation cannot remove this difference. All geometry can be placed above the fixed size and gap floors. No lower bound uniform in the mesh is needed to disprove an exact identification.

The seam example disproves **automatic** meet/pure-tower identification on unrestricted boxes. It does not disprove joint localization on LQ-admissible boxes, nor show that the actual class formation necessarily produces such a forbidden \(R_z\). Establishing which alternative holds for every prescribed \(R_z\) remains necessary. Replacing the pure box by the meet is a possible revised filing, but its pointed cancellation and WF13a domain would then have to be checked for that map; they are not inherited by renaming it.

## 8. The smaller statement and every named consumer

There is a useful finite statement stronger than (6.2) of the previous note. Under **FM**, put \(K=Y\setminus B\) and use the diagonal interpolation (3.2). Repeatedly applying the one-variable fundamental theorem gives exactly
\[
 {\cal F}(\,\cdot\,,\,\cdot\,;P)[K\mid B]
   =\sum_{D\subset K}(-1)^{|K\setminus D|}
             f_{B\cup D}(P;1_{B\cup D}).              \tag{8.1}
\]
At each corner the Boolean weights select that one domain problem, including its step parameters. This proof does not differentiate domain indicators, and does not forget the step dependence when setting \(\theta=s\). If the anchored functions after the \(\nu\) derivative and \(t\) integral have magnitude at most \(H_{j,z}\), (8.1) gives
\[
       |V_{j,z}(Y)|\le 2^{|Y\setminus B|}H_{j,z}.       \tag{8.2}
\]
The bracket still vanishes for an active component missing the base, and its finite sum over \(Y\) equals the complete-domain value. This is a finite, exactly local statement, conditional on the actual finite maps and charts. It is not a spatial formation bound: \(2^{|Y\setminus B|}\) has the wrong sign in its exponent. Lemma 2.1 shows that this is a substantive limitation of the hypotheses.

For a successful old-to-old collar comparison on the *undecoupled* admitted datum domains, the named inputs **T4, AX, AV, MS, PW**, the common old-map identification and the neighbourhood condition of wf7-extension Section 4 give
\[
 H_{j,z}^{\rm rem}\le
 C(g_j/\alpha_j)\delta_k\sigma_j e^{-cM/\sigma_j};
                                                               \tag{8.3}
\]
use \(d_j\) instead of \(g_j\) for vacuum-only origins. This is conditional on the comparison applying to each finite problem in (8.1), with the same constants. Formula (8.2) does not eliminate its growing factor. If Theorem 5.1's coefficient hypotheses are established for these problems, (5.5) instead supplies
\[
 |V_{j,z}^{\rm rem}(Y)|\le
 C(g_j/\alpha_j)\delta_k\sigma_j e^{-cM/\sigma_j}
                         (R-1)^{-|Y\setminus B|}.     \tag{8.4}
\]
These two conclusions must not be conflated.

The source search was made for WF7, WF11–WF15, OA7, “removed field” and the removed exponential, followed by reading the actual passages. There are two explicit references to WF7 after its definition, SA 16102 and 16270; the other consumers below also read its assertions through the window hypotheses.

| Consumer | What the smaller proved statement supplies | What remains necessary for its printed conclusion |
|---|---|---|
| SA 15947–15959, the two removed substitutions | Critical composition (4.1) distinguishes the projected old pair from Current-I. The inner box continues to carry its actual current. | Identify and bound the actual two removed extensions on their separate discs, with their actual node transport. Current-I versus actual-current equality is not restored. |
| **WF11**, SA 16100–16114 | Given (8.3), the member Cauchy estimate and the \(C_M\sigma_j^{-4}\) old-site count give \(Cs_kg_j\rho_j\sigma_j^{-3}e^{-cM/\sigma_j}\) before fine-bracket losses. For (8.2), multiply this by \(2^{|Y\setminus B|}\). | A volume-uniform fine-parameter amplitude or a direct summable rooted-coefficient estimate, such as (8.4). An undecoupled estimate alone is insufficient. |
| **WF12**, SA 16115–16132 | It absorbs every fixed old-scale power against \(e^{-cM/\sigma_j}\). For \(p>0\), choose an integer \(n>p\) and use \(e^x\ge x^n/n!\) at \(x=cM/\sigma_j\); boundedness on the remaining compact interval is immediate. | It cannot absorb \(2^{|Y\setminus B|}\) uniformly in \(Y\) at fixed \(j,k\). The variable counting extra current cubes is independent of the old age. |
| **WF13a–WF13d**, SA 16137–16297 | Under FM, (3.2) and (8.1) supply exact restriction, component rooting and finite completeness. Under (7.2), the one inner box is the prescribed old problem. | The inner window must stay grouped before applying its single bracket. Theorem 5.1 would give the mixed Cauchy factor and the existing rate allocation. Equation (8.2) gives neither its decay nor its entropy reserve. |
| **WF14**, SA 16299–16313 | The regular inner age function remains summable under the named inner window/cancellation hypotheses. The estimate \(a^rL^{-\alpha_Ha}\) is summable by its successive-ratio limit \(L^{-\alpha_H}<1\). | Summation over ages does not repair an unbounded rooted localization at one fixed age. No interchange of an infinite age sum with the new localization is justified by finite completeness. |
| **WF15**, SA 16315–16343, including source derivatives | A finite old-action identity follows under FM and physical endpoint identification. The norm inequality below keeps an explicit localization remainder. | The printed norm bound requires control of that remainder; linearity in source origins does not provide it. The first-source derivative needs the same coefficient/domain estimates on its source disc. |
| **OA7–OA8**, SA 16826–16866 | Existing first-response/tower room applies to the admitted old and step maps separately. The finite interpolation has exact active-component restriction under FM. | Uniform normalized displacements for the new complex interpolation, compatible boundary comparison of the actual boxes, and summable rooted coefficients are still required. A linear combination of admissible pair values is not automatically an admissible nonlinear pair or a chart in the core. |

Here is the precise reduced norm statement if the unestimated localization terms are retained. Denote them by \(R_{j,z}(Y)\), after the \(\nu\) derivative and \(t\) integral, and define
\[
 {\mathfrak D}_j
   =\sup_Y e^{\lambda d_k(Y)}
           \sum_{z:\,B_{j,z}\subset Y}|R_{j,z}(Y)|.     \tag{8.5}
\]
This uses the same output-domain norm and pointed-origin counting as WF15. Let \(V^{\rm known}\) be those inner/far/removed origins for which the stated uniform hypotheses have actually been supplied. Exact linear filing and the triangle inequality give
\[
 \|V^{\rm old}\|_\lambda
           \le\|V^{\rm known}\|_\lambda+\sum_{j\le k}{\mathfrak D}_j.
                                                               \tag{8.6}
\]
When all other WF hypotheses hold, insert their corresponding terms from the right-hand side of WF15 into \(\|V^{\rm known}\|_\lambda\). There is no assertion here that \({\mathfrak D}_j\) is small, age summable, or uniform in volume. Thus (8.6) is a usable finite identity/conditional estimate for keeping track of a genuine remainder; it is **not** a replacement proof of the ordinary induction or UV stability.

The earlier bulk defect is different. If one reverts to the original assigned pair, it must also retain
\(\Delta_\nu(q-\Pi_jV)\), as in old-depth (7.11). Even an assumed per-base bound \(C\delta_k\sigma_j^3\), after the site count and one member Cauchy factor, leaves \(Cs_kg_j\rho_j\sigma_j^{-1}\). For \(a=k-j\), the quotient by the regular WF12 weight is at least
\[
 {L^{(1+\alpha_H)a}\over C_0^2(1+a)},
\]
and that by the vacuum-only weight is at least
\(L^a/(C_0\sqrt{1+a})\), using \(1\le\rho_j\le C_0\sqrt{1+a}\).
Both diverge by the exponential series. This is a failed majorant comparison, not a proved lower bound on a summed gauge-invariant activity. It remains a separate unresolved route.

## 9. Dependency check and recovery point

The new positive implications use these exact inputs:

- **FM:** all required finite local old problems, component consistency, local charts and their specified step evaluations. The finite algebra proves no common volume-uniform radius for them.
- **BG/AX/AV:** regular critical uniqueness and continuation, the actual axial recursion, and nonlinear averaging/local carriers. These prove (4.1) and, with the explicit geometric containment, (7.2).
- **T4/MS/PW and common-chart room:** the old response and native counting, plus the specified step first response. They support the previously proved collar estimate with its weighted datum sums. PW here means pw-bridge Sections 5–6 together with the specified R9 nonlinear construction and its premises; a label “PW” alone supplies no nonlinear old-projection expansion.
- **CP-linear/CP-nonlinear/CP-identification:** the local coefficient conditions of Theorem 5.1. They have **not** been verified for the full nonlinear old projection on the declared complex pair domains. They are sufficient primitive conditions for a construction, not a renamed proved theorem.
- **Flat lift:** identifies the old derivatives in Sections 6 and 6.1. The scalar inverse, its flags and its convergence are computed by hand from (6.1); the four-dimensional coefficient uses FW as well.
- **FW:** used additionally in Section 6.1 for the actual four-dimensional vacuum test coefficient. These are the flat local inverse, commutator and fixed-region carrier hypotheses specified there, with their source gate corrections. The parametrix, tags and three-factor coefficient estimate are re-derived from them. The resulting constant is volume-uniform at fixed mesh; its mesh and age dependence is not bounded here.

The hardest unresolved verification is concrete. Construct the old projection using coefficients local in the **input pair**, with a uniform absolute norm before inserting the shared flags. The existing T4 theorem is centred at a generated real critical reference; that reference itself depends nonlocally on its datum. A walk kernel whose coefficients read this reference has not localized its dependence on the original pair. A global change to a Landau chart likewise needs its node dependence expanded. Merely invoking the current-step R9 estimates, or the first derivative of the old map, does not fill either gap.

One tempting alternative is to use the force-only system of a3-clauses Section 4 at the unprojected input. That theorem assumes a small independent force in its normalized force norm. The actual \(J(\mathbf U)\) of a general admitted input can be as large as \(C\alpha_0\eta^{-1}\xi^{-2}\); its force norm need not be small. Replacing it by the independent current changes the critical projection. A proof that retains its plaquette-divergence structure, supplies the needed pointwise bounds and cancels the dangerous terms could overcome this problem. Such a proof is not supplied by Theorem Sigma as stated. This identifies a live construction problem, not an impossibility claim.

The repository's no-go-discipline questions were applied as scope checks, with the user's no-commit/no-audit rules taking precedence over packet procedures:

- **N1:** the actual alternatives examined are carrying the known bulk defect, finite Boolean interpolation, and a joint supported-coefficient expansion. The last remains live; no five-family exhaustion or packet PASS is claimed.
- **N2:** coefficient localization and layered problem identification are distinct checks. No independence theorem is claimed; neither direction of implication has been proved in general. In the special containment case (7.2), identification is settled.
- **N3:** finite-map existence, common charts, full read sets, native row sums, physical identification and coefficient smallness are explicit above. A finite-volume continuity radius is never called uniform.
- **N4:** old-depth refutes the assigned-pair bridge; wf7-extension refutes leaving the old projection undecoupled; Lemma 2.1 refutes a single-boundary-estimate inference; Section 7 refutes an unrestricted meet/tower identification. None is used as a counterexample to the full requested construction.
- **N5:** the explicit scalar inverse and, under FW, the actual four-dimensional first nonzero current-square coefficient are bounded. No full nonlinear assertion or uniform old-age estimate is inferred from them.
- **N6:** exact finite restriction, the coefficient-algebra implication, the scalar bound and the containment criterion are proved partial statements. They need no new physical axiom.
- **N7:** the strongest counterargument to a negative conclusion is Balaban's own final-localization step: expand the background dependence together with its propagators, compose supported coefficients before tagging, and keep the old collar mark. Theorem 5.1 gives a concrete sufficient implementation; its actual primitive estimates remain to be established.
- **N8:** pw-bridge succeeds by retaining cancellations before estimating sources; removed-fix succeeds by matching complete interior read sets and keeping exterior sums native. Both mechanisms are retained in Theorem 5.1 rather than bypassed by an estimate of the already summed maps.

Recovery: checkout def5abd9bee7f4b71abe2f49df52afa8614c08d6, SA 31a47c543775. The requested earlier files have not been edited. The next decisive task is to verify CP for the actual old projection (including the common complex core and node conventions), or construct a counterexample satisfying those actual equations and domains. For layered uses, first decide whether every prescribed full \(R_z\) satisfies (7.2); otherwise the meet map and its layer scale must be carried explicitly. Repeating only a one-collar estimate or the undecoupled counterexample does not resolve this task.

## Result

**WF7 and rank 4 are not closed. No counterexample to all possible joint localizations has been established.** In particular, this note does not fulfil the full requested nonlinear localization theorem.

What is proved, with its implications separated:

1. From exact finite algebra and **FM**, the joint interpolation has exact restriction, component rooting and physical completeness; its bracket is (8.1) and has the finite bound (8.2). Lemma 2.1 proves that uniform holomorphy and a single exponential boundary comparison do not imply a uniform rooted bound.
2. From **BG, AX, AV**, the aligned containment and admitted charts, the critical endpoint composition (4.1) holds with the actual current and ordered transports. From (7.2), the old meet is exactly the prescribed box problem. The explicit small Cartan seam construction shows that this identification fails for unrestricted boxes crossing into a lower layer.
3. From **CP-linear, CP-nonlinear and CP-identification**, Theorem 5.1 constructs a joint supported expansion with a volume-uniform complex rooted bracket bound, preserves the old collar factor and includes the actual node recursion. These coefficient hypotheses remain unverified for the full actual old projection; the theorem is a sufficient construction criterion.
4. From the explicit flat saddle equations and **Flat lift**, (6.3)–(6.4) give a uniform tagged old response in the scalar Cartan sector. From **FW and Flat lift**, (6.5)–(6.7) additionally localize the precise four-dimensional coefficient (5.12) with its actual R9 direction, uniformly in volume at fixed mesh. Both remove the remote coefficient exactly when its slab is deleted. They do not prove the full vacuum-only member (5.10) at arbitrary inputs or its required age dependence.
5. The consumer check gives (8.6) with the localization remainder retained. WF11–WF15 and OA7 require a summable bound for it; finite exact locality alone does not provide their printed formation estimate.

**Where rank 4 stops:** a supported expansion of the *nonlinear old projection itself*, local in the original pair on the declared complex domains, with the common-chart/node estimates and the old collar mark retained. Layered applications additionally require the full prescribed-box containment/identification or a proved revised meet filing at its actual local scale. The first-system results remain named conditional inputs. No independent verification, audit status, retained status or Yang–Mills existence conclusion is asserted.
