# J:derive:a-clause-that-fixes-gamma:a1 -- what could fix gamma?

Worker: Claude Sonnet 5.5, one session. Same-family, unrefereed. Nothing here is adopted and no status word applies.

**Read first, as the rules require.** I read in full `docs/MINIMAL_AXIOMS_2026-06-29.md` (on main `a77a3449c91a753b06ce2a63876cd460b62cb4cf`) and `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`. Short form of what they allow: the four axioms (Lattice `Z^3`, Qubit, Admissibility, Record; `MINIMAL_AXIOMS_2026-06-29.md:35-83`) supply no energy functional, no ledger, no clock field and no filled sea; "Axioms and approved primitives are the complete supplied foundation" and every other dependency "must be retained-derived or remain conditional/open" (`:108-112`). The approved primitives are `scale_reference_primitive` (a units conversion with "zero dimensionless content", `PRIMITIVE_REGISTRY_CHECK.md:31-56`; it does not assert `a/l_P = 1`, `:50-52`), `kinetic_isotropy_primitive` (`c_t = c_s`, `:58-96`) and `realized_state_primitive` (`:98-129`). None of them supplies a number such as gamma. So every object below is a **lane-supplied model**, not an axiom consequence.

## 0. Plain-language summary

Gamma is the exchange rate between the energy of the amplitudes and the stiffness of the clock field. Scale covariance cannot fix it, because the field energy can always be multiplied by a constant (landed in block 104 and block 55). I looked for a clause that ties the field's stiffness to the amplitudes' own energy, and I tested the filled sea of the clocked walk as that clause.

1. The raw sea, used as the field energy, pushes every Fourier mode of the clock the wrong way. The reason is a one-line scale-covariance sum rule: the uniform part of the Hessian is forced to equal the sea's (negative) energy per site.
2. Remove the sea's uniform energy with a pure volume term (a cosmological-constant-type term, a potential in the site rate with no neighbour dependence). The Hessian becomes a positive closed form, `<(r r' - d.d')/(r + r')>`, and gamma is `12/<r>`, where `<r>` is the Brillouin-zone mean of the walk's single-particle energy. I certify `gamma` by interval arithmetic: `gamma = 12/<r>` lies in `[10.0519196, 10.0519378]` (step S7).
3. This is **not** new in its main value: `kappa = <r>/12` and `gamma = 12/<r>` are in earlier unrefereed or grok-confirmed attempts (listed below). What is new here is the exact positive closed form, the sum-rule class statement, the stability threshold of the localisation family, the unique-ultralocal characterisation of the clause, and a rigorous (interval) bracket instead of floating quadrature.
4. The clause is still **supplied**: whether the subtraction is a volume term (gamma about 10.05) or a term counted bond by bond (no `1/R` tail at all) is not decided by the axioms, the primitives or blocks 53-56.

## 1. Landed-version controls (what I did not build on)

The brief's SETTING paraphrases some claims that the landed notes narrow. I used the landed versions:

* Block 104 T3 (`docs/ADMISSIBILITY_RULE_THE_RULES_OWN_CLOCK_HAS_NO_FAR_FIELD_THE_PULL_NEEDS_A_RATE_LAW_WITH_A_MONOPOLE_A_REST_ENERGY_AND_A_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-23.md:38-41`; call it [B104]) says the `S/E = -gamma/6` identification "is not supplied by the ledger alone" and that homogeneity "leaves gamma undetermined by that test". It does not say "every gamma > 0 satisfies the clauses of blocks 53-56" for the weak-field pull; that is a reading of the brief.
* Block 55's point-force coupling `g` is not gamma ([B55] `docs/ADMISSIBILITY_RULE_ACTION_AND_REACTION_THE_RATE_FIELDS_SOURCE_IS_THE_AMPLITUDES_ENERGY_DENSITY_MATCHED_PULLS_AND_A_KEPT_LEDGER_FIX_THE_CLOCK_LAWS_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-21.md:48`). The linearised law with `F = (2/gamma) sum_bonds (phi_x - phi_y)^2` is at `[B55]:60`: `L_avg(du) = -(gamma/(6 wbar))(e - mu)`; I recomputed its Hessian symbol `L(q)/gamma` (check A4).
* Block 76 as landed ([B76] `docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md`) contains **no** value `gamma_ind = 10.5` and no induced-stiffness theorem. Its `c = -1193/1000`, `kappa = 95/1000` are "declared rational inputs ... not derived sea coefficients" (`[B76]:53`), and "The comparator cannot equal the exact sea Hessian at all momenta" (`[B76]:55`). The figure 10.5 is `1/0.095`, a comparator input. I do not build on it.
* Walk and clocked walk are [B54] `docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md`: symbol `sum_j sigma_j sin k_j` (`:40`), `H_w = W^{1/2} H W^{1/2} = phi H phi` (`:44`).

## 2. Prior art in the repository (searched before claiming anything is new)

Found in the read-only `ai/probes` view `/Users/jonBridger/.probe-clones/probes-view/probes/work/derive/`:

* `normal-ordering-as-a-rule/w-macbookpro90c72-j8445/ATTEMPT.md:15-44` (attempt a2, PR #8761, referee `.../referee_w-macbookpro90c72-j4629/REPORT.md` "confirmed", grok): `kappa = |c0|/12` exactly for the per-site subtraction, `gamma = 12/|c0| = 10.0519`, the interband bubble `B(q) <= 0`, `B = O(q^4 log(1/q))`, the per-bond subtraction with zero `q^2` stiffness, and the family `theta T_site + (1-theta) T_bond` with stiffness `theta |c0|/12`; verdict "the counter-term is supplied" (`:46`, `:98`).
* `the-seas-polarisability-as-a-lattice-sum/w-macbookpro90c72-jabe7/ATTEMPT.md:25-36`: `kappa = I/12`, `I` as a Bessel integral to 20 digits (`1.19380112142979520212`), interband kernel `Delta Pi`.
* `the-held-sea-against-the-free-sea/` (PR #8716), referee "HIT: confirmed": the interband deficit is a negative zone integral of order `q^4 log(1/q)`.
* `what-fixes-gamma-if-not-the-sea/w-macbookpro90c72-j952b/ATTEMPT.md:25,34,53`: collects `gamma = 12/|c0|` and the comparator `a/l_P = sqrt(4 pi/gamma) = 1.118`; `gamma-the-one-number/w-macbookpro90c72-j0f83/ATTEMPT.md:32,49`: nothing in blocks 53-55 fixes gamma, and reading it off the scale reference is circular.

I formed my own plan before opening these files (a scale-covariance sum rule for a class, then the exact sea Hessian and the normal-ordered clause). Everything I derived that matches the list above is therefore an **independent re-derivation, not new**.

## 3. The exact statement attempted

Supplied model (all of it, nothing adopted): the walk `H = sum_j sigma_j D_j` of [B54], symbol `d(k).sigma`, `d = (sin k_1, sin k_2, sin k_3)`, `r(k) = |d(k)|`; clocks `w = e^u`, `phi = e^{u/2}`, `H_w = phi H phi`; the half-filled sea `E_sea[u] = sum of the negative eigenvalues of H_w` (a mathematical filling choice, [B76]:27); weight one: `E_sea[u + c] = e^c E_sea[u]`. Write `c0 = E_sea[0]/V = -<r>`, `<.>` the Brillouin-zone mean, `L(q) = sum_j 2(1 - cos q_j)`, `h(q)` the Hessian symbol per site, normalised by `E^(2)/V = (1/2) sum_q h(q)|u_q|^2`.

**Attempted.** (a) A clause for the field energy `F`, tying its stiffness to the amplitudes' own energy, whose Hessian has no wrong-sign volume term, or an exact no-go in a stated class; (b) its value of gamma, defined (as in [B55]:60) by `h_F(q) = wbar L(q)/gamma + o(q^2)`.

## 4. Steps

Labels: **PROVED** (full argument here), **CHECKED** (executed by `check.py`; "float" if not exact arithmetic), **ASSUMED**, **READING**.

**S1. PROVED (sum rule for the weight-one class).** Let `F` be a twice-differentiable, translation-invariant, finite-range functional of `u` on a periodic lattice with `F[u + c] = e^c F[u]`. At uniform `u` its Hessian symbol satisfies `h(0) = F[0]/V =: e0`.
*Proof.* Differentiate `F[u + c 1] = e^c F[u]` twice in `c` at `c = 0`: `sum_{x,y} d^2F/du_x du_y = F[u]`. Translation invariance at uniform `u` makes every row sum equal, so each equals `F[0]/V`, and the row sum is `h(0)`. For a finite-range `F` the symbol `h(q)` is a trigonometric polynomial, hence `h(q) = e0 + kappa L(q) + O(q^4)` with cubic symmetry. (The sea itself is not finite range, its symbol has a `q^4 log q` term (S4); for it only `h(0) = e0` is used, which needs just the row-sum identity, and is checked in C1.) This is the second derivative of the identity `sum_x dL/du_x = L` of [B55]:56. QED.
*Consequences.* A pure Laplacian response (`1/R` tail with coefficient `1/kappa`) needs `e0 = 0`. With `e0 > 0` the response is screened (mass squared `e0/kappa`); with `e0 < 0` the denominators `e0 + kappa L(q)` are negative for `L < |e0|/kappa` and the long-range response has the opposite sign. So the "volume term" `c` that [B76]:51-53 declares is **forced** to equal `e0` for any weight-one `F`; it is not a free input. [Not in [B76]; the sum rule itself is elementary.]

**S2. PROVED + CHECKED (exact second variation of the sea).** By second-order perturbation theory of `sum_{lambda<0} lambda` with `H_w = H + (1/2){U,H} + (1/8){U^2,H} + (1/4) U H U + O(U^3)` (CHECKED A1, entrywise), the two-band filled sea gives, with `d1 = d(k)`, `d2 = d(k+q)`, `r1,r2` their norms, `c = d1.d2/(r1 r2)`,

`h(q) = < -(1/2)(r1 + d1.d2/r1) - (r1 - r2)^2 (1 - c)/(4(r1 + r2)) >_k`.

The first term is the expectation of the second-order operator; the second is the interband term, whose squared matrix element `|<+(k+q)| (H(k)+H(k+q))/2 |-(k)>|^2 = (r1 - r2)^2 (1 - c)/8` is checked as an identity (CHECKED A2, sympy). Occupied-occupied terms cancel in pairs. CHECKED B3 (float): dense diagonalisation of `E_sea[a cos(q.x)]` on an antiperiodic `6^3` torus equals this expression for 7 modes (relative deviation 3.6e-6, the finite-difference error).
*Derivation (standard Rayleigh-Schroedinger for a filled band; written out so the formula is not taken on trust).* For the filled lower band `Phi_0`, `E^(2) = <Phi_0|H2|Phi_0> - sum_{i occupied, j empty} |<j|H1|i>|^2/(eps_j - eps_i)`, with `H1 = (1/2){U,H}` and `H2 = (1/8){U^2,H} + (1/4) U H U`. The pair sum over two occupied states cancels by antisymmetry. `Phi_0` is translation invariant, so only the momentum-diagonal part of `H2` survives: for `u = sum_q u_q e^{iq.x}` `(1/4) U H U` contributes `(1/4) sum_q |u_q|^2 H(k+q)` and `(1/8){U^2,H}` contributes `(1/4) H(k) sum_q |u_q|^2`; in the state `|-,k>`, `<H(k')> = -n1.d(k')` and `<H(k)> = -r1`, which gives the first term. `H1` takes `|-,k>` to `|+,k+q>` with amplitude `u_q <+,k+q| (H(k)+H(k+q))/2 |-,k>` and energy denominator `r1 + r2`, which gives the second term with the squared element of A2. Zero modes (`r = 0`) form a null set of `k`; the integrand is bounded, so the infinite-volume symbol is the zone integral (ASSUMED as the definition of the infinite-volume Hessian: the limit of the torus values).
The first term is simplified exactly: `<d1.d2/r1> = (<r>/3) sum_j cos q_j`, because `d1.d2/r1 = sum_j (s_j^2/r1) cos q_j + sum_j (s_j c_j/r1) sin q_j` (here `s_j = sin k_j`, `c_j = cos k_j`), the second sum averages to zero under `k_j -> -k_j`, and `<s_j^2/r> = <r>/3` by permutation symmetry. With `sum_j cos q_j = 3 - L/2`:

**`h(q) = c0 + kappa L(q) - R(q)`, `kappa = <r>/12`, `R(q) = <(r1 - r2)^2 (1 - c)/(4(r1 + r2))> >= 0`.** (CHECKED C1, C2 to 3e-16.)

[Equivalent to the bubble form in the earlier attempts; the packaging with the sum rule S1 and the sign of every term is mine.]

**S3. PROVED (the raw sea is repulsive in every mode; exact version of [B76]'s sign statement).** `h(q) = -<r>(1 - L(q)/12) - R(q) <= 0`, and `< 0` unless `L(q) = 12`, i.e. unless `q` is the chessboard momentum `Q = (pi,pi,pi)` where `h(Q) = 0` (this is the chessboard invariance of [B76] T1; CHECKED D3). So with `F = E_sea` alone the field equation `h du = -(e - mu)` has the wrong sign at every mode except `Q`, for the exact two-band sea, not only for the comparator inputs of [B76] T4 (which [B76]:55 says are not the sea Hessian). [READING: wrong sign means clocks speed up near a positive-energy source.]

**S4. PROVED (the volume-subtracted sea: positive closed form).** Let `F_site = E_sea - c0 sum_x w_x` (a potential term in the site rate). Then `F_site` has weight one, vanishes on uniform clocks and has zero first variation there, and

**`h_site(q) = h(q) - c0 = < (r1 r2 - d1.d2)/(r1 + r2) >_k = kappa L(q) - R(q)`.**

*Proof of the first equality.* `h - c0 = <(1/2)(r1 - d1.d2/r1)> - R`. The map `k -> -k - q` preserves the measure and sends `(d1, d2) -> (-d2, -d1)`, so `(r1, r2, c) -> (r2, r1, c)`. Averaging the first term with its image gives `<(1/4)(r1 + r2)(1 - c)>`. Hence `h - c0 = <(1-c)[X/4 - Y^2/(4X)]>` with `X = r1 + r2`, `Y = r2 - r1`, and `X/4 - Y^2/(4X) = r1 r2/X` (CHECKED A3, sympy). Finally `(1 - c) r1 r2 = r1 r2 - d1.d2`. QED. (CHECKED D1 to 4e-16.)
*Positivity.* `r1 r2 - d1.d2 >= 0` by Cauchy-Schwarz, with equality iff `d1`, `d2` are positively parallel. For `q` not in `2 pi Z^3` this fails on an open set of `k`: if `d(k+q) = lambda(k) d(k)` held on an open set with `lambda > 0`, comparing components, `sin(k_j + q_j)/sin k_j = cos q_j + sin q_j cot k_j` is independent of `k_j` only if `sin q_j = 0`, and positivity then forces `cos q_j = 1`. So `h_site(q) > 0` for `q != 0`.
*Sandwich.* `0 < h_site(q) <= kappa L(q)` since `R >= 0` (CHECKED D2).
*Small `q`.* `0 <= R(q) <= |q|^2 <(1 - c)/(4(r1+r2))>`, because `|r1 - r2| <= |d1 - d2| <= |q|`. As `q -> 0`, `1 - c -> 0` almost everywhere and `(1 - c)/(r1 + r2) <= 2/r1`, with `<1/r>` finite (eight conical zeros, `int d^3p/|p| < inf`). Dominated convergence gives `R = o(|q|^2)`. Hence `h_site(q)/L(q) -> kappa = <r>/12` (CHECKED D4 shows `R/L` of order 1e-4 and falling like `q^2 log`).
*Result.* `F_site` has a pure Laplacian response with stiffness `kappa wbar` (weight one) and a determined chessboard mode (`h_site(Q) = <r> > 0`, where the raw sea leaves the mode undetermined). Matching to [B55]:60, `wbar L/gamma`, gives

**`gamma_site = wbar/kappa_phys = 12/<r>`** in units where the walk's coefficient `beta` (B54:40) is 1; for general `beta` and `wbar`, `gamma = 12/(beta <r>)` (weight one in `w`, degree one in `beta`).
[The `1/R` far field of the weak-field pull with coefficient `gamma/(4 pi)` then uses the standard lattice-Laplacian Green function asymptotics `G(R) -> 1/(4 pi R)`: ASSUMED, a standard import; block 55 uses the same.]

**S5. PROVED (bare plus induced).** If `F = (2/gamma_b) sum_bonds (phi_x - phi_y)^2 + F_site`, the Hessians add and `1/gamma = 1/gamma_b + 1/gamma_site`; so `gamma <= gamma_site` for every `gamma_b > 0` (CHECKED E5, sympy). This is the induced-gravity form: the sea contributes a stiffness `<r>/12` that a bare term can only increase.

**S6. PROVED (the clause is unique among ultralocal volume terms).** Clause **U**: `F = E_sea + T`, where `T` is translation-invariant, of weight one, and **ultralocal** (a function of the single-site rate, no neighbour dependence), with `F[uniform] = 0`. Then `T = c sum_x w_x` (a function `f` of one variable with `f(t w) = t f(w)` is `f(1) w`), and `F[uniform] = 0` fixes `c = -c0`. So U selects `F_site` uniquely and gives `gamma = 12/<r>`; it has no free parameter. (Also: zero first variation at uniform clocks holds automatically, `dE_sea/du_x = c0` by S1 and translation invariance.)

**S7. CHECKED (interval arithmetic, rigorous up to the stated enclosures) -- the value.** `<r> = (1/(2 sqrt(pi))) int_0^inf psi(t) t^{-1/2} dt`, `psi(t) = (1 - G(t))/t`, `G(t) = <exp(-t sum sin^2 k)> = (e^{-t/2} I_0(t/2))^3`. Proof of the representation: `sqrt(A) = (2 sqrt(pi))^{-1} int_0^inf (1 - e^{-tA}) t^{-3/2} dt` for `A >= 0` (integrate by parts; `int_0^inf (1 - e^{-s}) s^{-3/2} ds = 2 sqrt(pi)`), then Tonelli. `psi(t) = int_0^inf e^{-ts} P(A > s) ds` is a Laplace transform of a nonnegative function, so it is positive, decreasing and convex. On each cell in `tau = sqrt t` of width `1/400`, the chord bounds `psi` from above and the tangent at the left end from below (convexity); both are integrated exactly against `t^{-1/2}`; the tail `t > 900` is bounded by `[2(1 - G(900))/30, 2/30]`; `psi(0) = <A> = 3/2` and `psi'(0) = -<A^2>/2 = -21/16` are exact rational moments (CHECKED A5); `I_0, I_1` are evaluated by positive series with a geometric tail bound in `mpmath.iv`. The result, `check.py` F1/F2:

* `<r> in [1.19379966849, 1.19380183175]` (width 2.2e-6)
* `gamma_site = 12/<r> in [10.0519196, 10.0519378]`

The exact rational Holder bracket `[1.1339, 1.2247]` (CHECKED A6) is the coarse baseline. The earlier quadrature value `1.19380112142979520212` lies inside the bracket (F3), and an independent `96^3` midpoint sum agrees (F4, float). The earlier attempts used floating-point quadrature only; the interval enclosure is the new part of (b).

**S8. PROVED + CHECKED (the localisation family; no-go for a bond-counted subtraction; stability threshold).** Let `T_bond = (c0/3) sum_bonds sqrt(w_x w_y)` (linear in the walk's own bond rates, the operator normal ordering of `H_w`, which contains bond terms only) and `F_theta = E_sea - theta T_site - (1 - theta) T_bond`. By S2 and the exact Hessian of `T_bond` (`(c0/12) sum_j (2 + 2 cos q_j)`, the non-bubble part of `h`), `h_theta(q) = theta kappa L(q) - R(q)`.

* `theta = 0` (operator normal ordering): `h_0 = -R <= 0`, no `q^2` term: **no `1/R` tail and a negative semidefinite Hessian** (PROVED from S2/S4; this agrees with the earlier attempt's "no long-wavelength stiffness").
* Chessboard: `E_sea` is blind to `u = a eps` (CHECKED E1, dense); `F_theta[a eps]` costs `theta V |c0| (cosh a - 1)` (CHECKED E2, E3). So **chessboard invariance of the field energy holds iff `theta = 0`, which is also the case with no Newtonian stiffness**: in this family a walk-blind relabelling of the clocks and a Newtonian pull cannot both hold (E4).
* The uniform clock is a strict minimum of `F_theta` against all nonuniform modes iff `theta kappa L(q) > R(q)` for all `q != 0`, i.e. `theta > theta_* = sup_q R/(kappa L)`. CHECKED D5 (float): `theta_* ~ 0.055`, at `q ~ (1.4, 1.4, 1.4)` (coarse global scan on a `32^3` grid plus a diagonal refinement on `64^3`). Hence stable members have `gamma_theta = 12/(theta <r>) < ~183`; `theta = 1` gives `10.05`. The family therefore leaves `gamma in (0, ~183)` after stability. [Only `theta_*` is float; it is a scan, not a proof of the global maximum.]

**S9. READING (not claimed).** If the sea clause U is read with `hbar = c = a = 1` (the low-`k` speed is `beta wbar`, so `c_t = c_s` of `kinetic_isotropy_primitive` reads `beta wbar = 1`) and the weak-field pull `-(gamma/(4 pi)) E_A E_B/R` is compared with Newton, then `G = gamma/(4 pi)` and `a/l_P = sqrt(4 pi/gamma) = sqrt(pi <r>/3) = 1.118`. The registry says `a/l_P = 1` is an open derivation (`PRIMITIVE_REGISTRY_CHECK.md:50-52`); this comparator is the earlier attempt's, not a result.

## 5. First failing step, and what is new

**First unresolved step: selecting the subtraction.** Clause U gives a unique, parameter-free `gamma = 12/<r>`, but U itself ("the vacuum subtraction is a volume term, not a gradient term") is a supplied choice. The axioms, the three approved primitives and blocks 53-56 do not select it: the bond-counted member of the same family (which looks equally natural, as the operator normal ordering of a bond-only generator) gives no pull, and a bare gradient term adds a free `gamma_b` (S5). Also the filling of the sea, its exclusion rule and the identification of `e_x` as the source of the clock field are supplied (cf. [B76] premises, [B55] T1).

**Verdict for (a)/(b).**
* Class no-go (PROVED): in the weight-one local class `W`, scale covariance forces `h(0) = F/V` (S1) and cannot fix gamma (also [B104]:41, not new); the raw sea alone is repulsive in every mode (S3); the operator-normal-ordered sea has no Newtonian tail (S8).
* A clause with its gamma (supplied, not forced): U, `gamma = 12/<r>`, certified bracket in S7.

**New relative to the sources** (retrieval, old numbers and scope cleanup excluded):
1. S1 as a statement about the whole weight-one local class (the "volume term" is forced to equal `e0`).
2. The exact sign structure `h = c0 + kappa L - R` with `R >= 0`, hence S3 (raw sea strictly repulsive for all `q != Q`) and S4's compact **positive** closed form with the sandwich `0 < h_site <= kappa L`.
3. S5 (bare plus induced gives `gamma <= gamma_site`).
4. S6 (U selects `F_site` uniquely) and S8's chessboard dichotomy as a statement, and the stability threshold `theta_* ~ 0.055` (float).
5. S7: an interval-certified enclosure of `<r>` and of gamma.

**Not new:** `kappa = <r>/12`, `gamma = 12/<r> = 10.0519`, the interband kernel and its `q^4 log q` order, the per-site/per-bond ambiguity and the verdict "supplied" (all in the attempts of section 2).

## 6. What would finish it

* A principle that forces the subtraction to be ultralocal (U) rather than bond-counted; for instance a requirement that all vacuum-energy bookkeeping be per site rate, as the clock field lives on sites, plus an independent reason the bare gradient term vanishes. Nothing in the repository supplies one.
* A proof (not a scan) of `theta_* = sup R/(kappa L)` and its value; a derivation of the sea's filling from Record/Admissibility.
* If instead gamma is to be treated as the lane's free number, S1-S5 give the bounds that remain.

## 7. Running it

`python3 check.py` (exact sympy/rational for A, interval arithmetic for F, float labelled elsewhere). The last run took 264 s (the sympy identity A2 dominates); `TOTAL: PASS=27 FAIL=0`; the stdout of that run is `check_run_output.txt`, well under 1.5 GB.
