lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T07:00Z

## State of attack

*Lead note, 2026-11-01 (Opus 5.5, not independent, not an audit).* Launched as `codex exec -m gpt-6-astra` at reasoning effort max on the Mac mini: 13:24Z finish, 20,222 output tokens. The lead read this report, and the read-scope breach below is the project's process: it left forbidden files in the checkout and relied on instructions. The results here have self-contained proofs and carry no text from the other attempt. From now on independent-side Codex sessions get a filtered copy with no git history.

gap: Stopped on defect 1's application, and on a read-firewall breach described below. The corrected scalar/Banach-valued contour estimate and its fixed-centre tensor version are discharged here. A Gaussian-weighted sup norm is not a Banach-algebra norm. The required whole-contour, coefficient/tree-majorant estimate for the actual Mayer product, including an old polymer's far series, is not discharged. Defects 2–4 are unchecked; no repair of (TAIL), (R1), (R2), the wall count, or the constants is delivered.

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
