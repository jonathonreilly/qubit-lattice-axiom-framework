lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T08:00Z

## State of attack

gap: Current continuation completed on the user-supplied filtered copy of `3100fdc3b`, 2026-11-01. The first stop is (C-JET) / (C-JET-field), with series-centre uniformity, in Section 5; item 2 also needs (CM-rows) on the walls. Section 7 proves the scalar summation repair and the Gaussian-budget implication, but the actual all-orders centre majorant (R-MAJ) remains open. Section 8 proves a length covering inequality, verifies `C_0=160` and the `L^4` positional/shape sum for one connected carried support, and gives the extra payment for multiple old components. Section 9 separates the constants and gives a noncircular conditional choice, including `C_2` and the needed row norms. Full (TAIL), (CM), and the mixed-family recursion remain open; the final ledger is Section 10. Only this file was edited. No external source, numerical job, or subagent was used. The predecessor's results and provenance below are retained as a historical checkpoint.

*Lead note, 2026-11-01 (Opus 5.5, not independent, not an audit).* Launched as `codex exec -m gpt-6-astra` at reasoning effort max on the Mac mini: 13:24Z finish, 20,222 output tokens. The lead read this report, and the read-scope breach below is the project's process: it left forbidden files in the checkout and relied on instructions. The results here have self-contained proofs and carry no text from the other attempt. From now on independent-side Codex sessions get a filtered copy with no git history.

gap: Predecessor's stopping state: stopped on defect 1's application, and on a read-firewall breach described below. The corrected scalar/Banach-valued contour estimate and its fixed-centre tensor version are discharged here. A Gaussian-weighted sup norm is not a Banach-algebra norm. The required whole-contour, coefficient/tree-majorant estimate for the actual Mayer product, including an old polymer's far series, was not discharged. Defects 2–4 were unchecked; no repair of (TAIL), (R1), (R2), the wall count, or the constants was delivered at that checkpoint.

unchecked: Provenance: requested lead label above; pinned checkout `519bdd7fceb10c95b42c99b5a40b7f1038b22c01`. This is a research note, not an audit. No numerical calculation, audit, commit, push, or subagent was run. The author's part was not edited.

gap: Read-scope exception, which prevents certifying this as a firewall-clean report. The initial locator command printed FINISH headings and its independent-side status row outside the three permitted sections. Later bounded reads of `upper-chain.md:315–361` included proof prose beyond the permitted clause statements, and `:984–1026` extended into the explicitly excluded audit table. I stopped the application investigation when that happened. No other attempt's proof file or forbidden library file was opened, but the excluded cross-attempt summary was exposed. Its content is not repeated or used below. The elementary results below have self-contained proofs; this does not erase the provenance failure.

## 1. Corrected (GOOD)

discharged: The gate's counterexample can be derived without quadrature. Write `rho(t) = exp(-t^2/2)/sqrt(2 pi)`, `s = i y`, and `Phi_a(z) = exp(i a z)`. Then

    mu_s(Phi_a) = exp(y^2/2)/sqrt(2 pi)
                  * integral_{-P}^{P} exp(-x^2/2) exp(i(a+y)x) dx,
    |mu_s^A(Phi_a)| <= exp(-a y).

For `A_n = (pi/2 + 2 pi n)/P`, put `a_n = A_n-y > 0`. Integration by parts once gives the boundary term `2 exp(-P^2/2) sin(A_n P)/A_n`. Integrating its remainder once more bounds it by

    A_n^(-2) ( |f'(P)| + |f'(-P)| + integral_{-P}^{P} |f''(x)| dx ),
    f(x) = exp(-x^2/2).

Consequently `mu_s(Phi_{a_n}) = c(P,y)/A_n + O_P,y(A_n^-2)`, with `c(P,y)>0`, while the proposed shifted-line norm equals `exp(-a_n y)`. Subtracting `mu_s^A` leaves a ratio to that norm growing without bound. This refutes the displayed functional inequality, not a Yang–Mills configuration.

discharged: **Whole-rectangle replacement.** Let `1 <= p <= P/2`, `s = u+i v`, `|u| <= P/4`, `|v| <= P/8`. Let `B` be a Banach space and `Phi` be `B`-valued holomorphic on a neighbourhood of

    D_s = { x+i t : -P <= x <= P, min(0,v) <= t <= max(0,v) }.

Define

    M_s(Phi) = sup_{z in D_s} exp(-|z-s|^2/8) ||Phi(z)||_B,
    mu_s(Phi) = integral_{-P}^{P} rho(x-s) Phi(x) dx,
    A_s(Phi) = integral_{-p}^{p} rho(t) Phi(s+t) dt,
    G_s = mu_s - A_s.

There is an absolute constant `C` (for example `C=10`) such that

    ||G_s(Phi)||_B <= C exp(-p^2/3) M_s(Phi).                 (GOOD-rectangle)

A norm on the two vertical walls and the shifted horizontal segment suffices; the rectangle norm is a convenient stronger version. No values outside `|Re z| <= P` are needed.

discharged: **Proof, including the walls.** Put `h(z)=rho(z-s)Phi(z)`. For `H(t)=integral_{-P}^{P} h(x+i t) dx`, holomorphy and differentiation under this finite integral give

    H'(t) = i integral_{-P}^{P} h'(x+i t) dx
          = i(h(P+i t)-h(-P+i t)).

Integrate from `0` to `v`. This proves the contour identity directly, also when `v<0`. The segment `s+[-p,p]` lies inside the shifted horizontal segment. Thus `G_s` is the sum of its two horizontal tails and the signed wall integrals. On the horizontal tails, `z=s+t` and

    ||rho(t)Phi(s+t)||_B <= M_s(Phi)/sqrt(2 pi) * exp(-3t^2/8).

Since `t/p >= 1` for `t>=p`, direct integration gives

    integral_p^infinity exp(-3t^2/8) dt
       <= (4/(3p)) exp(-3p^2/8).

The two tails therefore cost at most `8/(3p sqrt(2 pi)) exp(-3p^2/8) M_s`, which is at most an absolute constant times `exp(-p^2/3) M_s`.

On a wall put `a=+P-u` or `a=-P-u`, and `b=t-v`. Then `|a|>=3P/4`, `|b|<=P/8`, and

    ||rho(a+i b)Phi(+-P+i t)||_B
       <= M_s/sqrt(2 pi) * exp(-3a^2/8 + 5b^2/8)
       <= M_s/sqrt(2 pi) * exp(-103P^2/512).

The total wall length is `2|v|<=P/4`. Its contribution is at most

    P/(4 sqrt(2 pi)) exp(-103P^2/512) M_s.

To compare with the stated bound, use `p^2/3<=P^2/12` and `103/512-1/12=181/1536>0`. The function `P exp(-(181/1536)P^2)` has a finite absolute maximum, found by differentiating. These estimates give `C=10` with room. They use only norm inequalities and finite integrals, so they also prove the Banach-valued statement. In the oscillatory test above the new norm is at least `exp(-y^2/8)`, by evaluating at `z=0`; it does not incorrectly suppress the walls by `exp(-a y)`.

## 2. Tensor estimate and the algebra test

discharged: **Fixed-centre tensor version.** Let `I` be finite, with fixed scalar centres `s_i` satisfying the preceding hypotheses. For `T subset I`, take `z_i in D_{s_i}` when `i in T`, and `z_i=s_i+t_i`, `|t_i|<=p`, otherwise. Define

    M_T(Phi) = sup exp(-sum_{i in T}|z_i-s_i|^2/8) ||Phi(z)||_B.

For jointly holomorphic `Phi` on the product rectangles,

    || (product_{i in T} G_{s_i})(product_{i not in T} A_{s_i}) Phi ||_B
       <= (C exp(-p^2/3))^|T| M_T(Phi).                     (GOOD-product)

Proof: the wall/tail representation above is a finite signed contour measure in each variable. The weighted total variation in a `G` variable is at most `C exp(-p^2/3)`. In an `A` variable the mass is `integral_{-p}^{p}rho<=1`. Multiplying those bounds and applying the triangle inequality proves the display; finite product integration also proves commutation. Expanding `product_i(mu_i)=product_i(A_i+G_i)` is consequently exact. There is no factor per `A` variable. Centres that themselves are series in far fields require an additional composition estimate; this lemma does not supply it.

discharged: **The weighted norm is not an algebra norm.** Even for `s=0`, `v=0`, and scalar functions, let

    ||f||_q = sup_{-P<=x<=P} exp(-q x^2)|f(x)|,
    f(z)=exp(q z^2), q>0.

Then `||f||_q=1`, whereas `||f^2||_q=exp(q P^2)>1`. Thus replacing the shifted-line norm by a Gaussian-weighted rectangle norm does not establish the submultiplicative hypothesis of `ultralocal_cluster_expansion.md:74–78`.

discharged: The valid multiplication rule is graded:

    ||f h||_{q+r} <= ||f||_q ||h||_r.

Indeed the weight on the left is the product of the two weights on the right, pointwise. The same proof works for Banach-algebra-valued functions and separate weights per variable. Consequently, if factors `F_a` satisfy

    ||F_a(z)||_A <= b_a exp(sum_{i in T} q_{a i}|z_i-s_i|^2),
    q_{a i} >= 0,     sum_a q_{a i} <= 1/8 for every i in T,

then `M_T(product_a F_a) <= product_a b_a`, and (GOOD-product) applies. This is an implication with an explicit hypothesis on the *whole product*. It is not a verification of that hypothesis for the Mayer factors.

implication: There are two legitimate routes to the cluster library: an unweighted, submultiplicative contour algebra with adequately small activities, or integrated activities in the existing far-variable Banach algebra with a proved whole-product Gaussian budget. The library's integrated-activity variant (`:70–78`) allows the latter. It does not follow from a separate weighted bound on each factor. In particular, replacing a weighted bound by an unweighted one at cost `exp(theta P^2)` is not harmless: here `P=p_2` is proportional to `g^-1`, while `p` is a power of `log(1/g)`. For fixed positive `theta`, `theta P^2-p^2/3` tends to positive infinity. To verify that last comparison, set `t=log(1/g)`; an exponential `exp(2t)` dominates every fixed power of `t`, as follows from its positive Taylor series by retaining a term of sufficiently high degree.

## 3. Application checkpoint: the first unresolved estimate

unchecked: Location map, to distinguish the gate's version from this checkout. At `b4de676b7`, (GOOD) is line 742, its uses are lines 788, 790, 812. At pinned HEAD these are respectively lines 707, 767, 769, 791; Lemma 4.7e at lines 712–716 adds a product argument using the same invalid shifted-line norm. That argument is replaced only conditionally by (GOOD-product): its right-hand side must be the whole-rectangle norm. The following checks describe what that replacement demands, not a completed repair of the actual integrand.

| Factor in the Mayer integral | Status on the corrected contour and the needed weight |
|---|---|
| `rho(x_i-s_i)`, the cut `S_i`, and state `A_i` | discharged for fixed centres: they are exactly the functionals of Sections 1–2. The walls retain their endpoint contributions. The mass of `A_i` is at most one. |
| Other sharp local indicators | implication: if the stipulated separation from Bad plus collar and from every `NV(Z)` makes them independent of the shifted variables, they stay constant, with sup norm at most one and weight zero. An indicator that still reads a shifted variable cannot be treated by this lemma. The geometric separation is an input here. |
| Unexpanded `exp(f_C)` on a component of the rough core, and an old polymer's near data | implication: keep their variables real in `x` and integrate with the existing rough-core bound. They are not holomorphic factors to which (GOOD-rectangle) applies. Their complex-centre density cost still needs defect 2; it is unchecked here. |
| Crossing `exp(HH(X))-1`: action remainder, analytic old density, `log JJ`, `log FP`, and Schur/determinant contributions | gap: their joint, whole-contour bound in the far-variable coefficient/tree norm has not been established here. The needed Gaussian budget is a sum over *all* factors reading a variable. The real-variable quadratic budget in stage (i), item 3(b), is not by itself a proof on the vertical walls. For any verified Banach norm bound `h_X` one has `||exp(HH(X))-1|| <= h_X exp(h_X)` by its power series, but one must still prove and sum the `h_X` on this contour. |
| Chosen `z_k`, and chosen `exp(B_k+C_k)-1`, when they read `x_i` through far variables | gap: input (TAIL) controls a series on its field-radius polydisc. A whole-contour substitution into that series, uniformly in real bases and in the coarse coefficient/tree norm, is additionally needed. If such a substitution is a contraction, the old factor can use weight zero; otherwise its Gaussian weight must share the `1/8` budget above. The displayed comparison of an imaginary mean with a radius is not the full substitution estimate. |
| Products and the sum over connected families | gap: multiplication must occur in the far-variable Banach algebra, with the Gaussian budget allocated before integration. A product of individually bounded Gaussian-weighted factors is insufficient. The library's integrated variant remains available once these activity bounds are proved. |

discharged: **A test that kills a tempting far-series shortcut.** Consider just one analytic far-field coordinate `v`, with series norm

    ||F||_r = sum_{n>=0} |F_n| r^n,     F(v)=sum_n F_n v^n.

Suppose a contour variable enters a linear coordinate as `v=h x`. If `|h|P>r`, the map from this series algebra to the Gaussian-weighted real-segment norm is unbounded. Indeed take `F_N(v)=(v/r)^N`. Its input norm is one, but its output norm is at least

    exp(-P^2/8) (|h|P/r)^N,

by evaluation at `x=P`; this tends to infinity as `N` increases. A tree factor depending on the support of this single coordinate, rather than its degree, is a fixed multiplier and cannot fix this example. It already fails at `y=0`, so analyticity through a small imaginary height is not sufficient to justify substitution of the *fixed-base series* on the whole horizontal range.

implication: In the draft's scaling a nonzero local linear noise response has `h` of order `g`, whereas an uncapped old radius at a fixed far distance `d` is `r=c' g exp(c_1 d)`. Since `P=p_2` is of order `g^-1`, `|h|P/r` can be arbitrarily large. Thus the shortcut “the imaginary width is inside the radius, so the same fixed-base far series is bounded on the whole strip” fails as a norm argument. A fixed positive Gaussian weight does not repair that unbounded substitution operator.

unchecked: This is **not** a counterexample to an actual old Yang–Mills polymer, nor to the stronger hypothesis that an entire family of local expansions is uniformly bounded about every admissible real base. The polynomials in the preceding test need not satisfy that stronger uniform hypothesis. Re-expanding about the real field at each horizontal contour point could avoid the test. It requires proving regularity of every such base, keeping the near data fixed, and preserving the coefficient/tree norm under the simultaneous complex perturbations. Pointwise re-expansion alone does not prove that last assertion, and a small imaginary displacement in each coordinate separately does not bound their sum.

gap: **Named missing estimate: contour–TAIL composition (CTAIL).** Let `A_Z` be the input anchored series algebra at old rough set `Z`, with radii

    rho_Z(l)=min(rho_e, c' g exp(c_1 d(l,Z))),

and let `A_{Y'}` be the output anchored algebra of coarse far variables, with its radius function and tree weight as in (TAIL). Near data remain real. For a whole-contour choice `z`, let `C_z` denote substitution of the local chart into an old polymer, using an admissible real reference field for its expansion. What is needed for an old factor with weight zero is a bound of the following precise form:

    sup_{z in the full product of contour rectangles}
        || C_z F ||_{A_{Y'}}
       <= C_*^|Z| sup_{admissible real reference fields} ||F||_{A_Z},     (CTAIL)

with `C_*` independent of `g`, the volume, the contour choices, and the polymer's far-series degrees. If weight zero is unavailable, replace the left side by the corresponding weighted supremum and include its weights in the total per-variable budget `sum_a q_{ai}<=1/8`. The right side includes the declared `t` floor for a carried `C_k` factor. One must retain the actual input activity budget; an additional `exp(c/g^2)` per analytic tail variable is not allowed.

implication: For a fixed reference and a single radius algebra, the elementary sufficient condition for coefficientwise substitution is `||a_l||<=rho_Z(l)` for every substituted displacement: expand `F`, apply submultiplicativity to each monomial, and sum its absolute majorant. In the anchored setting, one must also bound the new tree weight by the old tree weight and the weights of the substitution coefficients. Thus (CTAIL) asks for a simultaneous, summed/tree-norm bound for the chart on the whole contour, including moving centres and endpoints. Neither (GOOD-rectangle) nor the preceding one-coordinate test supplies it.

gap: **The whole Mayer product has a second explicit requirement.** At fixed scalar centres and fixed real rough-core data, write `Phi_F` for the analytic part of an admissible connected family `F`, with its old far-series factors included. A sufficient estimate is

    sum_{F with output Y} M_T(Phi_F; A_{Y'})
        <= B_Y exp(-lambda |Y outside Y_0|),                              (CM)

where `M_T` is precisely the norm in Section 2, `B_Y` is the product of the input old-polymer bounds and rough-core costs (including any allowed factor per rough-core cube), and `lambda` leaves the decay required by the cluster library after its stated losses. The constants must be uniform in volume and `g`. Composing with series-valued centres `s_i(w)` must preserve this bound in `A_{Y'}`. This is a coefficient/tree-norm assertion; a scalar supremum over `w` does not prove it. Under (CM) that fixed-centre term has the extra factor `(C exp(-p^2/3))^|T|` by (GOOD-product). No proof of (CTAIL), (CM), or the series-valued-centre composition is delivered in this note.

## 4. Delivery and remaining work

discharged: The wrong shifted-line comparison has a correct replacement with the same `exp(-p^2/3)` small factor, but with a norm on the entire contour. The proof includes the walls and is valid in any Banach space. Its tensor extension has no loss on state-A variables. The weighted-norm algebra counterexample and the fixed-base far-series substitution test are also proved here.

implication: The corrected functional estimate would contribute to a repaired (TAIL) only given (CTAIL), the whole-product budget (CM), the composition estimate for far-field-dependent centres, and the remaining density/geometry/constant estimates. These are additional conditions, not silently supplied hypotheses. They could be proved internally without changing the wording of (TAIL), but until then its delivery by (GOOD), (R1), (R2), and Lemma 4.7e is unestablished by this repair.

unchecked: Defect 2 (the summed response and “at most e per cube”), defect 3 (the covering inequality, `C_0=160`, and the `L^4` positional sum), and defect 4 (constant names and order) were not repaired or certified. The current source contains changes since the gate; their presence is not a verification. I did not proceed into those dependent items after the first application gap and the firewall stop.

gap: No change to an upper-chain clause is proposed, and no clause is discharged. In particular this note supplies neither a full (TAIL) induction nor a source-dependent RG estimate from which UV-CT could be claimed. The earlier analytical-sector statements are not refuted here; the contested step is the passage to the true integrand and its R sector.

unchecked: Reads and execution record. Mathematical source inspection used bounded ranges of the independent part at HEAD and at `b4de676b7`, defect statements in the permitted second gate, and the setting and two variants of the permitted cluster library. `GOAL.md` and the permitted FINISH sections were read. The three other permitted libraries and the earlier gate were not opened. The upper-chain and FINISH read exceptions are recorded at the top. No source cited inside those files was followed. Only text search, text extraction, Git object reads, and report-file editing ran; no numerical evidence is asserted and no numeric lock was needed. No file in `checks/independent-good/` is necessary for these hand proofs.

## 5. Item 1: local bases, (CTAIL), and centres

unchecked: All source line references in this continuation refer to the supplied `3100fdc3b` copy of `parts/hard-core--independent.md`, not the gate's version. Its lines 733–739 already specify an arbitrary admissible real far base, with uniform anchored coefficient bounds and the floor for `C_k`; line 705 explicitly appeals to a series about any real field. Thus a fixed-base series is not the intended input. Sections 1–4 above remain the predecessor's record, not a claim to have checked the subsequently changed source.

discharged: **Adversarial tests of the four options.** The monomials in Section 3 kill fixed-base substitution on the full horizontal interval. Shrinking a variable's interval to `|h x| <= r` avoids that test, but the complementary integral is still present in `mu`; discarding it is not an identity. Keeping that entire variable real in state `mu` avoids the holomorphic substitution, but expanding its density at a far tail can cost `exp(c/g^2)` (the mean there may move by order `1/g`). This is not paid by a fixed exponential per cube. Re-expansion is the viable *conditional* option: choose the real chart field at each real contour parameter as base, and expand only its complex/formal displacement. Choosing the base separately as a function of `Re w` is not a holomorphic operation and does not estimate the Taylor coefficients in `w`.

implication: **Precise uniform-local input (UL-TAIL).** For fixed real near data, every admissible real far field `V_0` has a germ `F^{V_0}(v,s)` representing the same old function, with the stated radius `rho_Z(l)` and anchored norm at most its old activity budget `B_Z(V_0)`. The germs agree on overlaps. The supremum is over the same admissible base class at every contour parameter. For a carried factor `B_Z(V_0)` includes `max(t_Z(V_0),t_fl)^2 + max(t_Z(V_0),t_fl)^3`; replacing this by the value at a different base is an additional estimate. This explicit interpretation is sufficient as an *input*, subject to (C-JET) below. It makes the intended quantifier in (TAIL) precise, rather than establishing the induction which delivers it.

discharged: **Anchored substitution lemma.** Write an old germ as `sum F_{alpha,Xi} v^alpha s_Xi`. Let `a_l` be the substituted displacement series in the new variables, rooted at the image `l*`, with rooted coefficient norm `||a_l||_{l*}`. Suppose for every grafted monomial the target tree length obeys

    tau_new(Y'; target support)
       <= A_Z + B tau_old(Z; supp alpha, Xi)
          + sum over occurrences of l in alpha of tau_new(l*; graft support),
    c_new B <= c_old,              ||a_l||_{l*} <= rho_Z(l).       (C-JET)

Old site variables must likewise be carried by grafts satisfying this inequality, with norm at most their input weight. Then

    ||F^{V_0}(a,s_new)||_{Y'} <= exp(c_new A_Z) ||F^{V_0}||_Z.

Proof: expand each occurrence of `a_l` separately. The tree inequality bounds the weight of its resulting monomial by `exp(c_new A_Z)` times the old tree weight times all graft weights. Triangle inequality, summation over the graft coefficients, and `||a_l|| <= rho_Z(l)` bound the term by `exp(c_new A_Z)|F_{alpha,Xi}| prod_l rho_Z(l)^alpha_l` times its old tree weight. Summing proves the result by absolute convergence. This also proves it for infinite series by taking increasing finite absolute majorants. There is no constant raised to the degree. If `A_Z <= a |Z|`, the prefactor is `C_*^|Z|`, as requested in (CTAIL). All quantities here are norms of coefficients, not pointwise suprema over the far polydisc.

gap: **The exact application obligation.** For every simultaneous contour choice, with near variables kept real, one needs a representation in fixed real block frames

    V_l(w,z) = exp(i a_l^{t}(w,z)) V_l^{t},
    V^{t} admissible real, independent of w,
    a_l^{t}=0 on N_1(Z),
    sup_t ||a_l^{t}(w,z)||_{l*} <= rho_Z(l),                 (C-JET-field)

and the graft inequality (C-JET), including site grafts, uniformly over the required walls and their neighbourhoods. The norm includes the displacement from the real base caused by the imaginary contour height as well as the displacement caused by *all* coarse variables and centres. The real fields `V^{t}` must stay in the `epsilon_2` class off their holes for all horizontal choices up to `P`, and their activity budgets must satisfy `sup_t B_Z(V^{t}) <=` the budget actually allocated to this old factor (or a separately charged Gaussian/polynomial bound). Source lines 769–773 give a lift estimate at fixed real noise; they do not give this assertion for the simultaneous contour chart. In particular `g P` is a fixed multiple of `eps_0`, not a power of `g`; coefficients of `P(W) x` on the walls must be estimated with that size. A comparison of one imaginary mean with one radius proves neither the sum nor its graft weights. I have not derived (C-JET-field) from the cited saddle/chart construction. This is the first stop for the actual old polymers, not a counterexample to them.

discharged: **What a series-valued-centre composition actually requires.** Let `A` be a unital commutative Banach algebra with submultiplicative norm and `||1||=1`, `sigma_i in A`, `a_i=||sigma_i||`, and let `H(u)` be `A`-valued holomorphic and bounded by `M` on a polydisc `|u_i-s_i^0|<=R_i`. For radii `r_i<R_i`, integrate its Taylor expansion on `u_i=s_i^0+r_i exp(i theta_i)` against `exp(-i sum n_i theta_i)`. Termwise integration on compact subdiscs kills every other monomial and gives its coefficient as `prod_i r_i^(-n_i)` times that normalized integral. Taking norms and then `r_i` up to `R_i` bounds the coefficient by `M prod_i R_i^(-n_i)`. Hence, if `a_i<R_i`,

    ||H(s^0+sigma)||_A <= M prod_i (1-a_i/R_i)^(-1).          (CENTRE)

The same calculation works for a coefficientwise majorant carrying compatible graft weights. For this bound to cost at most `exp(b)`, require `sum_i -log(1-a_i/R_i) <= b`, for example `a_i/R_i<=1/2` and `2 sum_i a_i/R_i<=b`. Submultiplicativity follows term by term; convergence of the displayed geometric series justifies substitution.

discharged: **Test of a dimension-independent factor 2.** Set `f(z)=(3/4-z)/(1-3z/4)`. For `|z|<=1`, `|1-3z/4|^2-|3/4-z|^2=(7/16)(1-|z|^2)>=0`, so `|f|<=1`. Its series is `3/4-(7/16) sum_{n>=1}(3/4)^(n-1)z^n`, whose absolute coefficient norm at radius `1/2` is `3/4+7/20=11/10`. Thus `H(u)=prod_{i=1}^N f(u_i)` has scalar supremum at most 1 on the unit polydisc, but substituting independent formal coordinates of norm `1/2` gives norm `(11/10)^N`, unbounded with `N`. A coordinatewise half-radius condition therefore cannot imply a single factor 2. A suitably controlled joint norm or the summable ratios in (CENTRE) could; it must be specified and proved.

gap: For `H=(prod G_i)(prod A_i) Phi`, (CENTRE) also needs a bound `M` on the enlarged centre polydisc in the **output coefficient/tree algebra**, with a common holomorphic chart and the whole-contour norm of Sections 1–2. The proof cannot take the scalar supremum over `w` first and then declare it a coefficient norm. Nor can it use centre-dependent `Re w` as a Taylor base. The source's one-sentence factor-2 argument at line 709 supplies none of those hypotheses. A factor 2 for every scalar noise coordinate would be `2^n_v` per cube, not a harmless factor 2; it has no automatic payment from `kappa>=log L`. (C-JET-field) with an adequate centre buffer and summable centre ratios would supply the needed composition control; alternatively a direct coefficient majorant for the moving contour operators would do. Neither is established here.

implication: **Delivery decision.** Adopt uniform compatible local expansions about every admissible real base, and re-expand at real contour parameters independent of formal `w`. Conditional on (C-JET), (C-JET-field), the actual budget comparison for `C_k`, and the centre estimate just specified, the substitution lemma proves (CTAIL) with weight zero. No conclusion about the actual old polymers is unconditional. The final intended wording of (TAIL) need not change beyond making its uniform quantifier and compatibility explicit; its claimed delivery must add these estimates. The real-state and smaller-horizontal-range alternatives require a different decomposition and density budget, so they are not completed repairs of the current delivery.

## 6. Item 2: the whole-product budget

discharged: **Kill the real-to-wall shortcut first.** Fix `0<v<P/8`, `0<theta<1/8`, `N P=2 pi n`, and set `H_N(z)=(theta/P) z^3 cos(Nz)`. It is entire, vanishes to third order, and `|H_N(x)|<=theta x^2` for `|x|<=P`. But

    Re H_N(P+i v) = theta (P^2-3v^2) cosh(Nv) -> infinity.

Thus a real quadratic remainder bound, even with third-order vanishing, does not bound `exp(H)` on a vertical wall. This is a counterexample to that inference, not an example of an actual action/Jacobian. The actual analytic coefficient estimates could rule it out, but must be supplied on the required domain.

implication: **One explicit allocation of `1/8`.** For each shifted variable `i` use eight accounts of `1/64` each. These are *totals over an entire admissible connected family*, not allowances for each factor:

| Account | Required bound on the whole contour, in the far coefficient/tree norm |
|---|---|
| Action remainder | The sum of its contributions to the exponent's quadratic row at `i` is at most `1/64`. |
| Analytic old density `EE^an` | Same, at most `1/64`. |
| `log JJ(b)-log JJ(b*)` | Same, at most `1/64`; its constant at the saddle is already extracted. |
| `log FP(b)-log FP(b*)` | Same, at most `1/64`, on a single holomorphic determinant branch. |
| Schur quadratic contributions | At most `1/64` on shifted variables; cross terms with real rough variables must also be charged to their separate rough Gaussian margin. |
| Remaining determinant contributions | At most `1/64`; a field-independent piece may use zero. Hole-set decay alone does not verify this row. |
| Prefactors in every `exp(HH(X))-1` and any polynomial old-factor growth | At most `1/64`, retaining a summable small activity coefficient for each attachment. |
| Series-centre composition | At most `1/64` if it consumes a Gaussian weight; at fixed centres this account is unused. Its nonquadratic coefficient loss must also be paid. |

An old far factor can use weight zero only under Section 5's (CTAIL), with its actual activity budget. Indicators independent of shifted variables use zero. Real near data and the unexpanded rough-core exponentials remain outside this allocation. The crossing `exp(HH)-1` is not a ninth contribution: the six exponent accounts and its prefactor account bound that very factor. Other allocations are possible; this one fixes exactly what must be checked.

discharged: **A usable sufficient inequality for crossing factors.** Put `u_i=|z_i-s_i|^2`. For each crossing set `X` suppose, simultaneously on the product contour,

    ||HH(X)|| <= h_X^0 + sum_i q_Xi u_i,
    ||HH(X)|| <= b_X exp(sum_i r_Xi u_i).

The first row is split into the first six accounts above. The second retains its activity `b_X` and uses the prefactor account. The exponential series gives

    ||exp(HH(X))-1|| <= b_X exp(h_X^0)
                              exp(sum_i (q_Xi+r_Xi)u_i).

If centre losses and other factors have analogous rows, and for every family `F`

    sum_{X in F}(q_Xi+r_Xi) + q_other,i <= 1/8    for every i,  (CM-rows)

then the graded multiplication proof in Section 2 bounds its whole-product norm by the product of its activity coefficients and `exp(sum_X h_X^0)`. This proves the budget implication on the **walls as well as horizontal segments** if its hypotheses hold there. Summing these coefficients over connected families with the required tree/exclusion margin is still part of (CM).

gap: A bound on `sum_X ||HH(X)||` alone does not preserve the small attachment factors in `prod_X ||HH(X)|| exp(||HH(X)||)`. For example, replacing `b_X(1+u)` by `b_X exp(u)` loses the small `b_X` in the coefficient of `u`; summing that loss over arbitrarily many attachments is unjustified. The prefactor row or an integrated moment/tree estimate is genuinely needed. Source lines 815–833 assert real-noise quadratic rows and scalar summations; they do not supply (CM-rows) in the coefficient/tree algebra on the walls, nor the prefactor rows. The holomorphic log branches and Schur coercivity under these simultaneous complex substitutions also need bounds; real positivity is not such a bound. Since (C-JET) already stops item 1, I do not claim to reconstruct the dependent Mayer estimate. The requested actual `1/8` budget is **open**, and so is its vertical-wall validity. The table is an exact sufficient allocation, not a certification that any of its six actual exponent rows has been proved here.

## 7. Item 3 / gate defect 2: sum the response

discharged: **The equal-rate test.** On `Z^4`, take `K(0,c)=delta exp(-a |c|_1)` and `rho(c)=min(rho_e,c'g exp(a |c|_1))`. Up to `D=floor(a^{-1} log(rho_e/(c'g)))`, every summand of `K rho/g` equals `delta c'`. The box `0<=c_j<=floor(D/4)` has at least `(floor(D/4)+1)^4` such sites. Thus the row grows at least as a constant times `delta c' D^4`. This proves the gate's objection without computing a saddle. A fixed positive rate difference is indispensable for this argument.

discharged: **Weighted row lemma.** Use coarse lattice distance and finitely many link components per cell. Shells have at most `A(n+1)^3` sites: choose four nonnegative coordinate distances with prescribed sum and at most `2^4` signs, absorbing orientations and a fixed endpoint offset into `A`. Define

    Q_4(b)=1+6/(1-exp(-b))^4,       b>0.

Indeed `(n+1)^3<=6 binom(n+3,3)` and multiplying four geometric series gives `sum binom(n+3,3)t^n=(1-t)^(-4)`. If

    |K(l,c)| <= B delta_1 exp(-lambda (d(l,c)-R)_+),
    rho(c) <= c'g exp(c_1 d(l,c)),         lambda>c_1,

then, with harmless enlargement for integer endpoints,

    sum_c |K(l,c)| rho(c)/g
       <= A B delta_1 c' exp(c_1 R) (R+1)^4 Q_4(lambda-c_1).   (ROW)

For `n<=R`, bound the exponential by `exp(c_1 R)` and sum the shell counts. For `n=ceil(R)+m>R`, use `(R+m+2)^3 <= C(R+1)^3(m+1)^3` and the geometric identity above. This proves (ROW), uniformly in volume; on a periodic lattice choose one shortest displacement per site. Also, for **any** `a<lambda`,

    sum_c |K(l,c)| exp(a(d(l,c)-R)_+)
       <= C A B delta_1 (R+1)^4 Q_4(lambda-a).                (WROW)

In particular the source's `lambda=2 c_tau`, `c_1=c_tau` permits `a=3 c_tau/2>c_1`. This is a weighted row-sum estimate at a strictly larger rate, derived from the stronger pointwise kernel, not from an equal-rate supremum.

implication: **Application with all linear factors exposed.** The supplied source already uses `lambda=2 c_tau` in lines 746–753 and the sum in line 767. Take those pointwise response bounds, uniformly on the relevant complex domain, as input. Let `R_0=sup_i sum_l |R_il|`, let `C_2,resp` include the weighted row norm of the gauge correction taking `V^*-V^#` to `b*`, and write `delta_1=D(L) exp(-2 c_tau R_loc)`. Then the near mean obeys

    a_J := sup_i |delta s_J,i|
      <= sqrt(2) R_0 C_2,resp D(L) C A Q_4(c_tau)
                  (R_loc+1)^4 exp(-c_tau R_loc) c'.          (J-ROW)

There is no missing `C_2` here. For this use of an **unweighted** row norm of `R`, every link `l` in its row at a near noise variable must have its coarse image in `Y'`. Then `d(c,Y')<=d(c,l*)`, so apply (ROW) at `l*` before summing `|R_il|`. The two ranges of `P,R`, followed by `R_loc`, fit in the specified `R_P=R_loc+2 rho_P/L`; the far variables do not change `R` on these rows. If that containment is not available for a different variable, the correct replacement is a weighted row norm of `R`, or a larger plateau radius, not the same `R_0`. Finite range alone can cost `exp(a rho_P/L)`, which need not be polynomial in `L`.

implication: A gauge-map convolution with kernel `Q(l,m)` preserves the response rate `lambda` with multiplier `sup_l sum_m |Q(l,m)| exp(lambda d(l,m))`: use `(d(m,c)-R)_+ >= (d(l,c)-R)_+-d(l,m)` in its absolute convolution. This defines the required `C_2,resp`. A kernel with rate greater than `lambda` has a finite such row by the shell calculation. The source's first-order inverse kernels are asserted to have that room; their nonlinear coefficient norm is not proved by this calculation. Neither upstream existence nor Lemma 4.7d's differentiated nonlinear estimate is independently discharged here.

discharged: **Slow spectator kernels at the cap.** Let `nu=s_P L>0`, `a=c'g`, `D=c_1^{-1} log(rho_e/a)`, and first suppose `0<nu<c_1`. Splitting shells at `D`, and summing a growing geometric series below it and a decaying one above it, gives

    sum_c exp(-nu d(i,c)) min(rho_e,a exp(c_1 d(i,c)))
      <= C(nu,c_1) (1+D)^3 rho_e (a/rho_e)^(nu/c_1).        (CAP)

For example below `D`, factor out `a exp((c_1-nu)D)` and sum the remaining backward geometric series; above it use `(D+m+1)^3 <= (D+1)^3(m+1)^3`. At `nu=c_1` the inside sum is instead bounded by `C a(1+D)^4`; at `nu>c_1` it is `C a`, with a smaller cap tail. Thus all cases tend to zero after multiplication by any fixed power of `log(1/g)`. The correct bound is a sum, and the power and shell polynomial must be retained before taking `g` small.

implication: **Radius, eta, and smoothing after this repair.** Keeping the source's `c_1=c_tau` is now allowed by (WROW); no equality of the *response* and radius rates is used. Keep `eta=c_3/(8c_1)`. Require `nu>2 eta c_1=c_3/4`, which is compatible with `nu=kappa_G/M` and `c_3=kappa_G/(C M^4)`. Then (CAP), multiplied by `p_4` and all fixed row norms, is `O(g^(2 eta))` after decreasing `gamma`. For `r'=c_1^{-1} log(rho_e/(C(L)g))`, the far-state factor `exp(-c_3 r'/2)` is a fixed constant times `g^(4 eta)`; its logarithmic losses are below `g^eta`. The torus-capped branch instead retains `exp(-c_3 T_{k+1}/8)` as in the source; it must not be replaced by a power of `g`.

implication: The smoothing perturbation grows as `g (D'+d) exp(c_1 d/2)`, so a lift kernel at rate `delta>=4 c_tau` is summable against it with a finite moment row at `delta-c_1/2>0`. The triangle inequality gives explicitly a bound of the form

    C(L) g (D'+d(l,Y')+1) exp(c_1 d(l,Y')/2),

with the shell moment included in `C(L)`. Off the zone `r_e=(2/c_1) log(C_7/c')`, the uncapped old radius is `c'g exp(c_1 d_k(l,Y))`; `d(l,Y')` grows no faster than `d_k(l,Y)/L` up to fixed offsets. The exponential in that old radius absorbs the displayed polynomial and half-rate growth. At `d_k=r_e`, `c' exp(c_1 r_e)=C_7^2/c'`, so choosing `C_7` after these row constants gives the desired small ratio. At the cap the perturbation is at most `C(L)(1+r') sqrt(rho_e g)`, below `rho_e` for small `gamma`. Thus the rate arithmetic and fixed-size zone survive the summed repair. This is conditional on the lift/chart estimates and the admissible-base construction; it is not a new proof of Gaussian smoothing or of (C-JET).

discharged: **The exact `e`-per-cube test for a density.** In a commutative coefficient algebra with submultiplicative norm and `||1||=1`, let `s=s_0+sigma`, with `s_0` real, constant coefficient of `sigma` zero, and `a=||sigma||`. At real `x`, putting `t=x-s_0`,

    rho(t-sigma)=rho(t) exp(t sigma-sigma^2/2),
    integral_{-P}^P ||rho(x-s)|| dx
       <= exp(a^2/2) E exp(a |N(0,1)|)
       = 2 exp(a^2) Phi(a)
       <= exp(sqrt(2/pi) a+a^2).                           (DENS-MAJ)

The equality follows by completing the square separately on each half-line. Finally `2 Phi(a)=1+2 integral_0^a rho(t)dt <=1+sqrt(2/pi)a <=exp(sqrt(2/pi)a)`. For a cube with `n_v` scalar noise coordinates, the tensor density norm is therefore at most `e` if

    sum_{i in cube}(sqrt(2/pi) a_i+a_i^2) <= 1.             (E-CUBE)

For instance `a_i<=1/(4 n_v)` suffices. This proves a coefficient-majorant statement, stronger than the scalar modulus cost `exp(sum |Im s_i|^2/2)`. It also bounds integration against a uniformly bounded algebra-valued old factor by its supremum times `e`.

gap: **What is still missing for the actual assertion.** (J-ROW) and (CAP) bound scalar simultaneous variations, conditional on the stated kernels. To use (DENS-MAJ) in (TAIL) one needs

    ||s_tot,i(w)-s_tot,i(0)||_{A_{Y'}}
       <= A_J(L,R_loc)c' + A_s(L,M) p_4 (1+D)^3
                         rho_e (c'g/rho_e)^(nu/c_1),        (R-MAJ)

with the analogous faster-rate bounds if `nu>=c_1`, and the same bound after adding site variables. Here `A_J` is the full prefactor in (J-ROW), and all constants are uniform in volume and degree. This all-orders anchored norm is not a consequence of a first-derivative pointwise kernel or of a scalar supremum. No such inference is made here. If (R-MAJ) holds, choose `c'` and then `gamma` so that its right side is at most `1/(4 n_v)`; (E-CUBE) proves the claimed cost. If integration also includes an unbounded rough-core factor, its tilted Gaussian moment/remaining margin must be bounded as well; the normalized density estimate alone is not a relative bound on that integral. Therefore the gate's missing *scalar sum* is repaired, but its “at most e per cube” conclusion in the actual coefficient/tree expansion remains conditional on (R-MAJ) and the applicable rough-core moment bound.

## 8. Item 4 / gate defect 3: walls, length, and positions

discharged: **Tests.** The gate's star within one brick can reach eight face neighbours, so neither `5 N` nor “four extra cubes per component” is valid. Another necessary test is many distant small rough components: no fixed additive short-set constant can cover all of them without charging their connecting length or counting components. The following proof handles faces, corners, and arbitrary branching without assuming that the set stays near one vertex.

discharged: **Packing lemma (short-set constant 16).** Let axis-parallel bricks of side `M` have disjoint interiors in four dimensions. A box with every side strictly below `M` meets at most `2^4=16` bricks. Indeed each meeting brick's centre lies in the box enlarged by `M/2` in every direction, of side strictly below `2M`. Divide each enlarged coordinate interval into two intervals of length strictly below `M`. Two centres in the same one of the resulting 16 boxes would differ by less than `M` in every coordinate, so their brick interiors would overlap. This is impossible. Closures and brick-wall offsets cause no exception. On a torus apply it to a local lift; repeated images only decrease the number of distinct bricks. A torus too small for that local lift has at most the corresponding total number of bricks and is bounded separately by the same count.

discharged: **Length covering lemma.** If a connected rectifiable path `Gamma` has length `ell` measured with the `l-infinity` norm, and `r<M/4`, the bricks meeting its `r`-neighbourhood number at most

    16 max(1,ceil(2 ell/M)) <= 16 + 32 ell/M.               (COVER)

Partition its parameter interval into at most `max(1,ceil(2 ell/M))` pieces of length at most `M/2`. Every piece has coordinate diameter at most `M/2`; adding its `r`-neighbourhood gives a box of side at most `M/2+2r<M`. Apply the packing lemma and sum. The first 16 bricks are free; each additional batch is charged to length travelled along the set between successive boxes, including travel between different faces or vertices. A tree is covered by its depth-first traversal, which traverses each edge twice. No lower bound on the separation of neighbouring brick-wall vertices is needed.

discharged: **Application to an old connected support.** Let `n` be the number of old full bricks in a connected polymer support, allowing closure adjacency. In coarse units their side is `M/L`. Join centres along a spanning tree of the old adjacency graph. Each edge has `l-infinity` length at most `M/L`; its straight segment stays in the two meeting bricks. A depth-first path has length at most `2(n-1)M/L`. The old bricks, and one layer of old neighbours, lie within `3M/L` of that path. Consequently, with

    r := R_P + 3M/L < M/4,
    Y' := all coarse bricks meeting (image(N_1(Y)) + B_{R_P}),
    m := |Y'|,

one has

    m <= 16 + 64(n-1)/L.                                  (WALL)

Here `image` is geometric rescaling, `B_{R_P}` is an `l-infinity` ball, and the coarse brick cover is taken **after** the thickening, as in the radius rule `rho/L+R_P`. Rounding to full coarse bricks before thickening is a different rule and is not covered by (WALL). If only `Rg(Y) subset Y` is thickened, the same bound holds, even when `Rg(Y)` is disconnected: the connecting support `Y` supplies the path. This uses the source's full-side-`M` brick specification at line 272, not the variable-size region tiles. Any extra analytic attachment must be counted separately, as below. If `N_1` is the smaller one-link neighbourhood rather than one brick layer, the same conservative bound still applies.

discharged: **Check `C_0=160`, including the threshold.** Put `w(n)=exp(-kappa(n-160)_+)`. If `L>=128` and `n<=169`, (WALL) gives `m<=100`, hence no output weight is requested. For `n>=170`,

    (n-160)_+ - (m-160)_+ >= 10 + (n-170)/2.               (MARGIN)

If `m<=160`, the left side is `n-160`. Otherwise it is `n-m >= n-16-64(n-1)/L >= n/2-16`, which is more than the displayed right side. Thus

    w(n) <= w(m) exp(-10 kappa) exp(-kappa(n-170)/2).

This repairs the claimed payment with a different covering argument; it does not use `5N`. For short old supports the smoothing hypothesis still separately needs `169 M+2r_e << L` in level-k units. These are compatible scale conditions, not numerical estimates in this copy.

discharged: **`L^4` positions and all connected shapes.** For a fixed coarse brick `c*` met by `Y'`, some old centre is within `r` (or the harmless extra `M/L`) of `c*`. Old centres have pairwise `l-infinity` separation at least `M/L`. Partition the enclosing box into intervals shorter than `M/L`; at most `(3L)^4` cells are required when `r<M/4` and `L>=128`. Thus there are at most `81 L^4` possible root old bricks. This argument does not require nested old and new tilings.

At most `D=80` other full bricks touch a given brick: their centres are in a box of side `2M`, partitionable into `3^4=81` boxes of side below `M`, including the original centre. A rooted connected set of size `n` can be encoded by the length-`2(n-1)` depth-first walk of a deterministically chosen spanning tree. The visited set recovers the set, so there are at most `D^{2(n-1)}` possibilities. Summing (MARGIN), including **all** shapes and positions, gives

    sum_{connected Y, n>=170, c* in Y'} w(n)/w(|Y'|)
      <= 81 L^4 D^338 exp(-10 kappa)
                    / (1-D^2 exp(-kappa/2)).               (POS-WALL)

For `D^2 exp(-kappa/2)<=1/2` and `kappa>=log L`, this is at most `162 D^338 L^-6`. A fixed geometric constant cannot be silently called 1; taking `L` large makes this a contraction. A fixed polynomial in `n`, such as the volume factors of a carried `C_k`, can also be included: its remaining sum is bounded by a constant times `sum_j (j+1)^q t^j`, finite for `t<1` since `(j+1)^q<=q! binom(j+q,q)` and the product of `q+1` geometric series sums the latter. The finite short-shape sum still has the `L^4` positional factor, to be cancelled by the stated smoothing/extraction estimates, not by this geometry.

discharged: A proved density loss of at most `e` per **old** cube is compatible with this payment: insert `e^n=e^170 e^(n-170)` in (POS-WALL), replacing the numerator by `e^170` times itself and the geometric ratio by `D^2 exp(1-kappa/2)`. Take that ratio at most `1/2`. For the short supports it costs at most the absolute factor `e^169`. A loss per output cube is bounded by `exp(16+64(n-1)/L)` and is no worse after adjusting an absolute factor. This verifies the geometry's compatibility with (E-CUBE) if that density hypothesis is established; it does not replace (R-MAJ).

discharged: **Multiple old supports require an extra payment.** Suppose a connected output family has old connected supports `Y_1,...,Y_h` with output covers of sizes `m_j`, and additional attachment supports whose union outside those covers has at most `a` cubes. Then, entirely independently of shape or overlaps,

    (|Y'|-160)_+ <= sum_j (m_j-160)_+ +160(h-1)+a,    h>=1. (FAMILY-WALL)

Indeed `|Y'|<=sum_j m_j+a` and `m_j<=(m_j-160)_++160`. Therefore converting the product of old weights and an attachment weight `exp(-lambda a)` to the single output weight costs at most

    exp(160 kappa(h-1))
       * prod_j exp(-kappa[(|Y_j|-160)_+-(m_j-160)_+])
       * exp(-(lambda-kappa)a).                            (FAMILY-COST)

All bracketed differences are nonnegative by (WALL) under the preceding scale choices, with the stronger (MARGIN) for large supports. The component counterexample shows why the factor involving `h` cannot simply be omitted. Equivalently, without paying it one must carry the forest weight `exp(-kappa(|Y'|-160h)_+)`, with a free constant for *each* old component, rather than the claimed single-component weight.

implication: For terms with at least two old factors, (FAMILY-COST) is compatible with a nonlinear activity budget if the rescaled activity `exp(160 kappa)(bb_k+cc_k)` and the corresponding rooted sums are sufficiently small; choose this smallness after `L,M,kappa` are fixed. Extra analytic cubes must retain rate `lambda>kappa` with enough surplus for their shape sum. The source's hull-supported attachments at lines 773–785 are the objects to charge, not just their possibly sparse marked endpoints. A born rough component or a mandatory `z_k` has its own rough/large-field cost and collar; it is not an old `B_k,C_k` with weight `w(n)`. Its cover must be paid by that separate budget or included as an explicitly counted component in (FAMILY-WALL).

gap: Thus `C_0=160` survives the geometry and positional summation for every connected carried support, including disconnected rough subsets and arbitrary thin or branched shapes. A universal `5N` assertion is replaced by (WALL), and multiple components by (FAMILY-WALL). To certify **every term of the full expansion** with the original single-output weight still requires the attachment/rough budgets and their summed activity smallness just specified. They are part of the open (CM), not a consequence of a covering lemma. Until those payments are proved, the honestly available mixed-family weight is the component-counted forest weight above. No full polymer recursion is discharged here.

## 9. Item 5 / gate defect 4: constants and their order

discharged: **Kill the missing-factor inference.** From `|b*|<=C_2 delta_1 eps_0` and `s_J=sqrt(2) R b*/g` one obtains only

    |s_J|_infinity <= sqrt(2) R_0 C_2 delta_1 eps_0/g.

Even the scalar example `R=1`, `b*=C_2 delta_1 eps_0` shows that dropping `C_2` is invalid. Comparing this with `p_2/16=c_p eps_0/(16g)` cancels `eps_0/g` exactly: taking `eps_0` or `g` smaller cannot repair a failed coefficient comparison. Likewise making `c_p` smaller *after* choosing `R_loc` can invalidate it. This is a parameter-order defect, not a proof that no fixed radius works.

implication: **Names and factors to use instead of the two `C_R(L)`s.** These are definitions of the constants required by the revised proof, not estimates of them:

| Name | Meaning and use |
|---|---|
| `C_REL(L)` | The constant `C(L^2+C_dich^2)` in the regular-fibre representation (REL); `rho_g=C_REL eps_0`. It is not a noise row norm. |
| `C_2,size(L)` | Sup-norm factor for the gauge-coordinate map, including the stated complex-domain allowance; `|b*|<=C_2,size delta_1 eps_0`. Also used with `C_REL` in `r_*`. |
| `C_2,resp(L;lambda)` | The weighted row factor for its **response**, as defined by convolution in Section 7. An unweighted bound for `C_2,size` does not automatically give this bound. |
| `R_0(L)` | `sup_{W,i} sum_l |R_il(W)|` for the local right inverse in (LOC-INV). If its coefficients are being expanded, the analogous coefficient norm is required. |
| `R_a(L)` | `sup_{W,i} sum_l |R_il(W)| exp(a d(i,l))`, when a weighted row is actually needed; use the near-set containment in Section 7 to avoid inserting this in (J-ROW). |
| `P_0,row(L)`, `K_chart(L)` | Absolute row bound of `P`, and the local field/curvature chart bound multiplying `g P x`. Their product, with `1/sqrt(2)`, enters the definition of `c_p`. |
| `D(L)` | The prefactor in `delta_1=D(L) exp(-2 c_tau R_loc)`, including the saddle inverse row `C_S` and comparison-source factors. |
| `A_s(L,M)`, `n_v(L,M)` | Full response/moment row constants of `sqrt(2) R(G_1 xi_1+G_2 xi_2)` and the number of scalar noise coordinates in a cube. The first includes both terms in `D(RG)=(DR)G+R(DG)`, when they are present. |

The `R` temporarily used for `C_1^{-1/2}P` in the source's conjugation argument is yet another operator; none of its row bounds is substituted for the (LOC-INV) right inverse without a proof. Colour components, both noise sectors, root offsets, and shell constants belong in the named row constants, not in an omitted factor.

implication: **A noncircular selection recipe.** Its hypotheses are finite uniform bounds for the named operators and chart on a prescribed regular class, and fixed polynomial upper bounds in `L,M` for the constants that determine `c_p`, `c'`, and `R_loc`. These are the intended upstream inputs. Work with those functions of the candidate scale `L` before fixing its numerical value.

1. Fix the absolute linear rates and their strict margins, the absolute overlap and energy constants (including `C_OS,c_F`), and the region/brick design. Choose `c_tau` below the available linear rates by a fixed factor, `c_1=c_tau`, and use response rate `2 c_tau` and test row rate `3 c_tau/2`. Fix the powers/constants defining `t,t',M_1,rho_P` and `M(L)`; define `nu,kappa_G,kappa,c_3,eta` from them. These choices do not use `eps_0` or `g`.
2. Obtain upper bounds for `C_REL,C_2,size,C_2,resp,R_0,P_0,row,K_chart,D,A_s,n_v` on that regular class, independent of `eps_0,g`, and uniformly in the eventual local-box radius. Fix the positive chart margins `c_ind,c_rho` and the constant `C_complex` in the complex-field restriction. Also fix `epsilon_1,rho_T,epsilon_2` from the already specified functional/saddle bounds. If a bound depends on the box radius, a uniform envelope or its explicit growth bound is needed before the next step; naming it `C(L)` does not provide one.
3. Choose `c_2>0` first, with the required complex-field restriction, for example `c_2^2<=c_F/(64 C_complex M^3)` and `c_2<=1`. Here `C_complex` is the already bounded constant in that restriction. Choose the cut coefficient `c_p>0` next. With `B_chart=K_chart P_0,row/sqrt(2)`, require, in addition to the source's indicator restriction,

       B_chart c_p <= c_ind/64,
       B_chart c_p <= c_rho c_2/64,       rho_e=c_rho c_2 eps_0.

   These are the missing comparison with `c_2` and all local row factors. Conditions involving `rho_T` can be met later by decreasing `eps_0`. Choose `c'` against the declared density/floor row constants, and `C_7` against the smoothing moment rows, then set `r_e=(2/c_1)log(C_7/c')`. Under the polynomial envelopes these choices can have `log(1/c')+log C_7=O(log L)`.
4. Only now choose `R_loc` so that both

       sqrt(2) R_0 C_2,size D exp(-2 c_tau R_loc) <= c_p/32,
       A_J(L,R_loc) <= min{1/(8 n_v c'), 1/(8 K_chart)},      (R-CHOICE)

   where `A_J` is the complete coefficient of `c'` in (J-ROW). The second condition both leaves half the density budget for the spectator and reserves the stated imaginary-field margin. It is a conditional scalar/majorant choice, not a proof of (R-MAJ). Set `R_P=R_loc+2rho_P/L` afterward. Exponentials beat `(R_loc+1)^4`, so a finite `R_loc` exists at each fixed `L` under these envelopes. With polynomial prefactors and a polynomial lower bound on `c_p`, an absolute sufficiently large `A_R` gives `R_loc=A_R log L` for all sufficiently large `L`.
5. Select and freeze `L` large enough for all the preceding explicitly defined functions to satisfy the geometry and linear contraction conditions: in particular `R_P+3M/L<M/4`, `169M+2r_e<<L`, `D_brick^2 exp(1-kappa/2)<=1/2`, and the desired small bound in (POS-WALL), including its `e^170` allowance when using (E-CUBE), with `D_brick=80`. This is possible under the stated envelopes because `rho_P/L=O((log L)^3)`, `R_loc,r_e=O(log L)`, `M=O((log L)^5)`, and `M/L` tends to zero. This use of functions of `L` avoids choosing `L`, later increasing `R_loc` without limit, and assuming that `R_P<<M` survived.
6. Choose `eps_0` after these constants and radii. Require, for example, `2 C_2,size C_REL eps_0` below the chart and tree radii, real contour bases below `epsilon_2` with their chart factor, and every stated nonlinear absorption product `C_non(L,R_t,R_loc) eps_0` below its assigned margin. Then define `alpha=c_2 eps_0`, `rho_e=c_rho alpha`, `r_*=2 C_2,size C_REL eps_0`, `rho_g=C_REL eps_0`, and `p_2(g)=c_p eps_0/g`. Decreasing `eps_0` can satisfy these upper bounds; it does not substitute for (R-CHOICE) or for a missing complex coefficient estimate.
7. Fix `p_0>2` and choose `gamma` last. For all `g<=gamma` require `1<=p(g)<=p_2(g)/8`, the spectator part of (R-MAJ) at most `1/(8 n_v)`, the scalar centre height restrictions, the cap/smoothing remainders, and the birth/activity smallness needed in (FAMILY-COST). Every finite requirement of the form `C g^b (log(1/g))^q <= epsilon` with `b>0` can be met: put `t=log(1/g)` and bound a sufficiently high term in the positive exponential series below `exp(bt)`. Smallness of the actual activities is still conditional on their birth estimates. Source-dependent constants, if used, would also have to precede `gamma`; none is analysed here.

discharged: Given the bounds assumed in that recipe, (R-CHOICE) gives `|s_J|<=p_2/32`, hence the requested `p_2/16` with room, with no radius depending on `g`. If (R-MAJ) is also available, steps 4 and 7 give `a_i<=1/(4 n_v)` and hence (E-CUBE). The conditional parameter selection does not use `c_2`, `c_p`, `C_2`, or a row factor before it is fixed. Existence with logarithmic `R_loc` follows from the polynomial-envelope hypothesis by taking `A_R` larger than their total exponents divided by `c_tau`, and then taking `L` large; the factor `(log L)^4` is absorbed by any extra fixed power of `L` by the same exponential-series argument.

gap: The recipe does **not** certify the missing uniform coefficient bounds, the nonlinear saddle comparison, or their claimed polynomial envelopes. If an actually required weighted row is bounded only by `R_0 exp(a rho_P/L)`, it can force `R_loc` of order `(log L)^3`, rather than the source's `A_R log L`; that still fits `M=O((log L)^5)` but changes the stated choice and must be recorded. If an unknown constant grows as fast as `exp(2 c_tau R_loc)` or depends circularly on the very margin it must establish, even that repair is unavailable. Thus the two `C_R`s, the omitted `C_2`, and the formal order are repaired conditionally; a closed parameter choice for the actual induction remains contingent on the explicitly named estimates.

## 10. Final ledger and stopping point

discharged: **Proved here, in addition to the predecessor's preserved proofs:** the anchored substitution implication (C-JET); the multivariate centre majorant (CENTRE) and the counterexample to a dimension-independent factor 2 from coordinatewise half-radii; the real-quadratic/wall counterexample; the sufficient whole-product allocation (CM-rows); the equal-rate divergence test and the fixed-slack row sums (ROW), (WROW), (CAP); the density majorant (DENS-MAJ) and its exact per-cube criterion; the covering lemmas (COVER), (WALL), the `C_0=160` margin, the full connected-shape/positional bound (POS-WALL), and the multiple-component correction (FAMILY-COST). The constant comparison with `sqrt(2) R_0 C_2` and the noncircular **conditional** selection have explicit derivations. No new actual Yang–Mills counterexample is claimed.

| Item | Final status and exact condition |
|---|---|
| 1. Actual (CTAIL), including centres | **gap.** Need (C-JET-field), the graft/tree inequality, admissible compatible real bases with the actual `C_k` budget, and a uniform centre polydisc/majorant with summable losses. Uniform local (TAIL) is the intended input; its delivery is still open. |
| 2. Actual whole-product (CM) | **gap.** Need the six exponent rows and the prefactor/centre rows in the output algebra on the entire contour, plus the connected-family activity sum and rough-core margins. No vertical-wall certification is made for the actual factors. |
| 3. Response and `e` per cube | **implication.** The scalar missing-sum defect is removed by the supplied stronger pointwise kernel and the explicit row lemmas. The actual coefficient conclusion additionally requires (R-MAJ), its gauge/site bounds, and any rough-core tilted moment estimate. Radius, `eta`, and smoothing scale arithmetic remain valid with those conditions. |
| 4. Walls and positions | **discharged** for the geometric/connected-carried-support statements under the explicit full-brick and scale hypotheses. **implication** for mixed families: pay (FAMILY-COST) with activities and attachment decay, or retain the component-counted forest weight. Actual activity closure is still (CM). |
| 5. Constant order | **implication.** Names, factors, and the order are fixed; existence of the stated logarithmic-radius choice requires the declared uniform polynomial envelopes. Missing analytic estimates are not consequences of choosing small constants. |

gap: The first honest stop for the actual old-polymer application is Section 5's simultaneous coefficient/tree chart estimate. Items 3–5 were pursued because they do not depend on its proof. This note delivers neither a (TAIL) induction nor a UV statement. The exact inequalities above, not a claim that a small constant exists somewhere, are the handoff.

unchecked: **Possible diagnostic, not run.** On a specified finite lattice and admissible real chart, a coefficient calculation could falsify (C-JET-field) or (R-MAJ): FAIL if a rigorously enclosed finite partial absolute coefficient sum already exceeds its stated radius or per-cube budget, or if an allowed horizontal base leaves the declared regular class. PASS for that finite instance would require certified upper bounds on the remaining coefficients and on the whole contour, including walls, below the thresholds. A sampled scalar supremum, a finite Taylor truncation without a tail bound, or success at finitely many volumes cannot prove the uniform assertion. No numerical job is available in this copy, and none ran.

unchecked: **Continuation's read/execution record.** Read `GOAL.md`, `FINISH-rules.md`, the entire predecessor note, and the specified gate; used text searches in the permitted independent part and bounded reads of its constant order, brick definition, (TAIL), lift/tree statements, chart/right inverse, (GOOD), two-centre response, crossing/stage-(i) estimates, smoothing and wall recursion. Some broad locator results were truncated; no claim relies on their completeness. No library body, upper-chain file, other gate, git history, machine path outside this directory, or web source was opened in this continuation. Only text inspection and edits to this file were performed; source-reported numerical results were not rerun or adopted as evidence. No other file was edited; no subagent, audit, commit, push, or post was made.
