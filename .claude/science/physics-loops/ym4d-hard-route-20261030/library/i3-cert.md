lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T10:40Z

# i3-cert: the certificate `I(omega) = 1` on the entering support (registry row RIM-I3)

Status: IN PROGRESS (started 2026-11-09T22:40Z; sections are appended as they are written).

Queue row: FINISH 624. Pinned at commit da6cf71d8. Source: Sussman and Alpoge,
`YM4_1400.tex` at commit 2bc0658f91d2 of the Yang--Mills-LLM-experiment repository;
`Y n` is line n of that file.

Credit. The argument is Sussman and Alpoge's (with Claude and Codex as authors of their text), paragraph
`hi:prepared-real-endpoint`, Y 65406-65591, with Y 64088-64102, 72248-72281, 76628-76689, 78299-78339,
134198-134216. The geometry of the regions is Bałaban's (CMP 122 (1989) 175) as ported by Y. This note
writes Y's prose as lemmas and proves the steps that are elementary; it adds no new route.
The labels are: **proved** (a written argument from the stated hypotheses), **cited** (one of the four
inputs the row allows, with its hypotheses checked), **gap** (not proved here).

## 0. Result

(Filled in at the end of the session; see section 10 for the state if this line is still here.)

## 1. Repo search

- `library/open-core.md`: no entry for RIM-I3, `i3-cert`, "entering support" or `hi:prepared-real-endpoint`
  (grep, 2026-11-09). FINISH rows 609 (RIM-SCALE), 617 (INSET-CHART), 620 (`i3-read`) are the neighbours;
  the row says they are not duplicates. Row 620 is a reading and proves nothing. No other row covers the
  statement.
- In this lane the passage Y 65406-65591 is mentioned in FINISH row 624, `library/open-registry.md` (RIM-I3),
  `library/inset-chart.md` 5.2 (input (F1-Y), "I did not rebuild it") and `library/prior/i3-read.md` only.
- This checkout has only the branch `claude/ym4d-hard-route`; `origin/main` and the other PR branches are
  not fetched here, so I did not search them. I rely on the search recorded in `library/prior/i3-read.md`
  (its "Repo search" section: no interior-holonomy supplier on `origin/main`, #10114, #10133, #10134, #10141).
- Used from the lane: `library/inset-chart.md` sections 2, 3, 5.1, 5.2 (setting, tests T1 to T13, the
  certificate), `library/rim-scale.md` (R1), (I4), `library/h-geo.md` (members and nest gaps inside `X`).

## 2. Setting

### 2.1 Frame, thresholds, scales (Y 1102-1120, 62001)

A frame is a real sequence `theta_0, ..., theta_k >= T := gamma^{-2}`, `gamma < e^{-1/2}`, with

`lambda (j - i) - c_5 <= theta_i - theta_j <= Bbar (j - i)` for `i <= j`.   (FR)

`mu_l := min_{i <= l} theta_i`. `R_l` (Y's `\check R_l`) is the smallest power of `L` not below
`(log mu_l)^r`, `r >= 2`. `eps_l := A_0 theta_l^{-1/2} (log theta_l)^{p_0}` (this is `gbar_l p_0(gbar_l)`),
`delta_l = (A_1/A_0) eps_l`, `delta'_l = (A_1/A_0)(log theta_l)^{-(p_0 - p_1)} eps_l <= eps_l`, and

`e_l := R_l^2 eps_l`   (Y 65409).

`L_flat` is an integer with `2 <= L_flat < L/2` (Y 63876). The paragraph ported here uses in addition

`L_flat^2 < L`   (LF)   (Y 65481).

(LF) does not follow from `L_flat < L/2` (take `L = 9`, `L_flat = 4`); it is a condition on the choice of
`L_flat`, satisfiable for every `L >= 5` by `L_flat = 2`. Section 5.3 says where it is used and what
survives without it.

### 2.2 Determining sets, tested plaquettes, footprints (Y 10505-10611, 72270-72276, 78299-78303)

A region sequence is `Omega_0 supset ... supset Omega_k`, unions of aligned cubes, with
`dist_infty(Omega_l^c, Omega_{l+1}) > rho L^l` in bare units (Y `mb:separation`; `rho >= C_geom L`).
Layer `l` is `Lay_l := Omega_l minus Omega_{l+1}` (Y's `\mathcal L_l`). The no-inward determining set is
`Gamma_l = { level-l bonds in Omega_0 that touch Omega_l and have no endpoint in Omega_{l+1} }`
(Y `mb:determining-rows`). A datum is a family `V = (V_l on Gamma_l)_l`.

**Definition T (tested plaquette; my reading of Y 10604-10611, 65511-65513, 72270-72276).** A tested
plaquette of level `l >= 1` is a level-l plaquette `p` with at least one corner in `Omega_l` and no corner
in `Omega_{l+1}`. By the separation its corners are in `Lay_{l-1} cup Lay_l`. An edge of `p` that touches
`Omega_l` is in `Gamma_l` (a *row edge*). An edge with both ends in `Lay_{l-1}` is a *completed edge*; its
two order-l blocks lie in `Lay_{l-1}`, all level-(l-1) bonds of these blocks are in `Gamma_{l-1}`, and its
value is the one-step average `M(V_{l-1})` on that double block (Y 72270-72276: "A bond that is not a
determining row has both ends in the layer just below `q`. Its two blocks lie in that layer, where the
determining rows supply the complete one-step average"). At level 0 the tested plaquettes are the bare
plaquettes of `Lay_0`. The *datum loop* `V(dp)` is the product of the four edge values; its *defect* is
`norm(V(dp) - 1)`. A real gauge conjugates it.

If Y's convention is instead "place in `Lay_l`" for a fixed corner, the sets differ only by level-l
plaquettes with the place in `Lay_{l-1}` and another corner in `Omega_l`. Remark 7.3 says what changes.

The *footprint* `F(p)` of a level-l plaquette is the union of the order-l blocks (of bare sites) of its
four corners. It is a box of sides `2L^l, 2L^l, L^l, L^l` and reaches at most `3L^l/2` from a corner
(Y 78302-78303). The *one-step stencil* `D(p)` is the same union read on the level-(l-1) lattice.

### 2.3 The averaging estimate (Y 4690-4960)

For a real `SU(2)` configuration `W` put `F_p = -i log dW(p)` (small branch) and `eps(W; S) = max |F_p|`
over the plaquettes in a set `S`.

- (AV1) one step, `prop:nonlinear-average-energy` (Y 4706-4720) in the local form its proof gives
  (`ne:actual-nonlinear-flux`, Y 4866-4871, with the row sum `L^2`, Y 4878-4886): there are `eps_L, C_L`
  with: if `eps(W; D(p)) <= eps_L` then the means defining `M(W)` on the four edges of `p` are on their
  regular branch and `abs(F_p(M W)) <= L^2 eps(W; D(p)) + C_L eps(W; D(p))^2`.
- (AV2) all depths, `cor:iterated-average-energy` (Y 4905-4960), local form: there is `alpha_L` with: if
  `0 < alpha <= alpha_L` and `eps(U; F(p)) <= alpha L^{-2l}` for a level-l plaquette `p`, then
  `abs(F_p(M^l U)) <= 2 alpha`.

Status: Y states both for a whole lattice with the global maximum. The local forms hold because `M^l U` on
the four edges of `p` reads `U` only in `F(p)`, and the proof of the corollary (Y 4927-4948) is a
recurrence on the maxima over the nested stencils of `p`. I read the proofs; I did not rebuild them. They
are not among the four inputs the row allows, so they are **cited, unchecked** beyond that reading.
`library/rim-scale.md` (I4) uses the same corollary in the same local form.
`norm(e^{iF} - 1) <= abs(F)`, so a bound on `abs(F_p)` is a bound on the defect; and defect `<= d <= 1`
gives `abs(F_p) <= (pi/2) d`. I write `c_0 := pi/2` for this conversion.

### 2.4 The stage (from `library/inset-chart.md` section 2)

Depth `m`, class component `X`, stages `n = 0, ..., N_m - 1`; the stage of level `j` promotes level-j rows
to level `q = j + 1`. For the final stage `j = m - 1`, `q = m`. *Old* means before the collar integration
of the stage, *prospective* after it. The old sequence is `Omega_.`, the prospective one `Omega'_.`:
`Omega'_l = Omega_l` for `l != q` and `Omega'_q = Omega_q cup K`, `K subset Lay_j` the collar released by
the stage (for the final stage `K = (Omega_m^c minus Y_m) cap X`). So `Gamma'_l = Gamma_l` for
`l notin {j, q}`, `Gamma'_j subset Gamma_j`, and `Gamma'_q supset` the rows of `Gamma_q`
(Y 65522-65535, 64088-64092).

Geometric facts used, with their source. I did not re-derive them; inside `X` they are in `library/h-geo.md`
(Lemma 2 and the Theorem, "holds, given CORE").

- (G1) Both sequences, and the global ones, satisfy the separation with the floors of
  `hi:real-datum-profile` (Y 15317-15322): `sigma >= L^2 rho_c`, `frakM >= frakM_c`, `rho >= L^2 sigma`,
  at least `6 rho` sites in each direction at the top level.
- (G2) `dist_infty(K, Omega_j^c) > 2 L^q` and `dist_infty(K, Omega'_{q+1}) > 2L^q`: the footprint of a
  level-q plaquette with a corner in `K` and no corner in `Omega_q` lies in `Lay_j` ("the order-`q`
  carrier stays inside the unchanged level-`j` member by the separation of the prospective sequence",
  Y 65550-65552; Y 72255-72258; Y 64097-64100).
- (G3) A level-(q+1) completed edge of the old sequence has its double block in `Omega_q`, at distance
  more than `2L^{q+1}` from `Omega_q^c` (Y 65529-65533). Empty for the final stage (`q = m` is the top).

## 3. Frame lemmas (proved)

`f(t) := t^{-1/2} (log t)^{p_0}` is decreasing for `t >= e^{2 p_0}`, and `eps_l = A_0 f(theta_l)`.
Floors on `T` used below: (T1) `T >= max(e^{2p_0}, 2 c_5, e)`; (T2) `(1 + c_5/(T log T))^{p_0} <= 2`;
(T3) `c_5 + 2 Bbar (1 + r log_L log t) <= t` for all `t >= T`. Each holds for `T` large, and each depends
only on `(c_5, Bbar, r, p_0, L)`.

**Lemma F1 (growth of the allowance).** Assume (FR), (T1), (T2). For all levels `l, s` with `n = abs(l - s)`:

`e_l / e_s <= C_F(n) := max( 2 (1 + Bbar n)^{1/2}, sqrt(2) L^2 (1 + log(1 + c_5 + Bbar n))^{2r} )`.

*Proof.* By (FR), `mu_l >= theta_l - c_5` and `mu_l <= theta_l`.

Case `l >= s`. `R` is non-increasing in the level, since `mu` is; so `R_l <= R_s`. By (FR),
`theta_l - c_5 <= theta_s <= theta_l + Bbar n`. `eps_l/eps_s = (theta_s/theta_l)^{1/2} (log theta_l / log theta_s)^{p_0}`.
If `theta_l <= theta_s`, the second factor is at most 1 and the first is at most `(1 + Bbar n/T)^{1/2}`.
If `theta_s < theta_l <= theta_s + c_5`, the first factor is at most 1 and the second is at most
`(1 + log(1 + c_5/theta_s)/log theta_s)^{p_0} <= (1 + c_5/(T log T))^{p_0} <= 2`. So
`e_l/e_s <= 2 (1 + Bbar n)^{1/2}`.

Case `l < s`. `theta_s - c_5 <= theta_l <= theta_s + Bbar n`. If `theta_l >= theta_s` then `eps_l <= eps_s`
(`f` decreasing). Otherwise `eps_l/eps_s <= (theta_s/theta_l)^{1/2} <= (1 - c_5/T)^{-1/2} <= sqrt(2)`.
For the radii, `mu_l <= theta_l <= theta_s + Bbar n <= mu_s + c_5 + Bbar n`, so
`log mu_l <= log mu_s + log(1 + (c_5 + Bbar n)/mu_s) <= (log mu_s)(1 + log(1 + c_5 + Bbar n))`, because
`mu_s >= e`. With `R_l < L (log mu_l)^r` and `R_s >= (log mu_s)^r` this gives
`R_l/R_s <= L (1 + log(1 + c_5 + Bbar n))^r`. `square`

So `e_l/e_s` grows at most like `n^{1/2}` upward and like a power of `log n` downward. This is the
statement "The frame bounds make `e_l/e_s` grow at most polynomially in `abs(l - s)`" (Y 65515-65517),
and it contains `eps_j/eps_i <= C(1 + (j - i)^{1/2})` (Y 63876).

**Lemma F2 (the compressed interval).** Assume (FR), (T1), (T3). Let `k_0 < k` with
`L^{k - k_0 - 1} = R_{k_0+1}` (the compression identity, Y 63798-63801: `a_{k_0+1} = u_k`). Then for
`k_0 < l <= k`: `R_{k_0+1} <= 2^r L R_l`.

*Proof.* Put `t = mu_{k_0+1}` and `n = k - k_0 - 1 = log_L R_{k_0+1} <= 1 + r log_L log t`. For
`k_0 + 1 <= i <= l`, (FR) gives `theta_i >= theta_{k_0+1} - Bbar n >= t - Bbar n`, so `mu_l >= t - Bbar n`,
and `t - Bbar n >= t/2` by (T3). Then `log t <= log mu_l + log 2 <= 2 log mu_l`, and
`R_{k_0+1} < L (log t)^r <= 2^r L (log mu_l)^r <= 2^r L R_l`. `square`

**Lemma F3 (the relaxed thresholds).** Assume the hypotheses of F2. For `k_0 < l <= k` and `0 <= e <= l - k_0`:

`L_flat^{2e} <= L_flat^2 R_{k_0+1}^{2 log_L L_flat}`.

Under (LF) this is at most `2^r L L_flat^2 R_l`, so `L_flat^{2e} eps_l <= 2^r L L_flat^2 e_l / R_l`.
Without (LF), from `L_flat < L` alone, it is at most `4^r L^2 L_flat^2 R_l^2`, so
`L_flat^{2e} eps_l <= 4^r L^2 L_flat^2 e_l`.

*Proof.* `e - 1 <= k - k_0 - 1 = log_L R_{k_0+1}`, so `L_flat^{2(e-1)} <= R_{k_0+1}^{2 log_L L_flat}`. Under
(LF) the exponent is below 1; in general it is below 2. Then F2. `square`

**Lemma F4 (weak coupling).** `max_l e_l <= ebar(gamma) := sup_{t >= gamma^{-2} - c_5} L^2 A_0 t^{-1/2} (log t)^{p_0 + 2r} sqrt(2)`,
and `ebar(gamma) -> 0` as `gamma -> 0`. The bound does not depend on the number of levels, the volume or
the history.

*Proof.* `R_l < L (log mu_l)^r <= L (log theta_l)^r`, so `e_l <= L^2 A_0 theta_l^{-1/2} (log theta_l)^{p_0 + 2r}`,
and `theta_l >= T`. `square`

## 4. Lemma 1: the entering support (definition)

Y has no formal definition of "admitted incoming fibre" (`library/prior/i3-read.md` section 1(b)). The
definition below is built from Y 65417-65424 (what the input holds), Y 65459-65474 (which tests are in
force at which moment), Y 65486-65487 ("Fix an entering point on these retained tests and on the
constraints with coarse target `V_q`"), and Y 78331-78337 (the certificate is one "before the old
averaging deltas are integrated, on the admitted entering fibre").

**Definition 4.1 (point, datum at a moment).** A *moment* is an entrance of a stage of an operation carried
by the history: the place in the formula just before the prospective guard of that stage is applied. A
*point* at a moment is an assignment of real values to all variables the term carries at that moment:
"The input at a point of a history includes the fields of the operations still carried by it"
(Y 65417-65418). The *old datum* `D(x)` of the point is the family `(V_l on Gamma_l)_l` for the global
region sequence in force at that moment, where the value on a row is the carried determining link
(Y 65419-65420). The *prospective datum* `D'(x)` is the family on the prospective sequence: old values on
old rows that remain rows, and on each new row `c` of level `q` the value `V_q(c)` that the point carries.

**Definition 4.2 (the tests in force at the entrance of a stage of `X`).** In the numbering of
`library/inset-chart.md` section 3, at the entrance of the final stage:

- (E1) the averaging constraints: for each new row `c`, `V_q(c) = M(V_j)(c)` on its double block (the
  retained delta, Y 72259-72260, 65486-65487), and the constraints of the rows carried from earlier steps;
- (E2) the preceding guard T9 `= chi_m^{(N_m - 1)}`, with convention D (an undefined background is a
  failure): the shell clauses, the exterior clauses, the deep exterior (crossing) clause at the last
  prepared face, and carried crossings if the operation has them (T3);
- (E3) the carried density tests of all levels: T4 (top) and T10 (lower), and the density tests on the
  unchanged places of the lower layers;
- (E4) the core selectors T5 (the tests and deltas under the core operation);
- (E5) for every other structure of the history outside `X`: the tests it carries at this moment, by its
  own rules (Y 65425-65474). I do not list them; see (COV) in section 5.4.

Not in force at the entrance, and not used below: the prospective guard T1, T2, T3 of this stage (it is
applied after the admission), the approximate collar test T6 against `S_X` and the sharp ball T7 (their
centre `S_X = M^j U^+` exists only after the admission; using T6 here would be circular), the strip
indicators T8, the belt groups T12, the contour indicators T11 and the mean conventions T13 (in force, but
no step below reads them).

**Definition 4.3 (admitted trajectory, entering support).** A *trajectory* to a moment `N` is a sequence of
points `x_0, ..., x_N` at consecutive moments `0, ..., N` of the history, where `x_0` is at the first
moment at which a test of the list (E) is carried, and `x_{nu+1}` arises from `x_nu` by the moves between
the two moments, each of one of these kinds (Y 65469-65474, 76674-76689):

- (m1) a gauge draw, frame change or tree gauge: every datum loop is conjugated;
- (m2) a promotion: new rows get the values fixed by (E1);
- (m3) an integration: the variables integrated at the stage are dropped from the point;
- (m4) a late Haar refresh with the inner datum retained: the old determining datum stays in its slot;
- (m5) a reference-law draw (restoration): the datum on the restored box is replaced.

The trajectory is *admitted* if at every moment `nu <= N` every test carried by the term at that moment
equals one at `x_nu` and every carried constraint holds. The *entering support* `Ent_N` is the set of end
points `x_N` of admitted trajectories.

**Lemma 1 (the support of the incoming term lies in the entering support).** Suppose the incoming term of
the stage at moment `N` is an iterated integral: at each earlier moment `nu` it is the integral, over the
variables dropped by (m3) and drawn by (m1), (m4), (m5), of a kernel times the term at `nu` times the
indicators and deltas carried at `nu`. If the incoming term is not zero at `x_N` (or `x_N` is in the
support of the delta measures it carries), then `x_N in Ent_N`.

*Proof.* Induction on `N`. If every `x_{N-1}` that the moves send to `x_N` had a carried indicator equal
to zero, or violated a carried delta, or had the term at `N - 1` equal to zero, the integrand would vanish
on the whole fibre over `x_N`, and so would the integral. So some `x_{N-1}` has all indicators one, the
constraints true, and the term at `N - 1` not zero; apply the induction hypothesis to it. At `N = 0`
there is nothing before. `square`

Remarks. (1) The hypothesis "iterated integral" is the form of Y's operation (Y 63836-63876, 77741-77763);
I take it as the definition of the term and did not rebuild the formula. (2) The lemma is the only place
where the *history* of the point enters. It is what lets a supplier be a test "carried at the relevant
moment" (Y 65459) and not only a test carried now. (3) `Ent_N` is larger than the set `{P Q != 0}` of
`library/inset-chart.md` Lemma 5.1, because the tests T6, T8, T11, T12, T13 are not imposed. So
`I = 1` on `Ent_N` gives (F1-Y) there.

## 5. Lemma 2: from a retained test to the datum defect

### 5.1 The supplier lemma (proved, given (AV2))

**Definition 5.1 (supplier).** Let `p` be a tested plaquette of level `l >= 1` of a datum `V`. A *supplier*
of `p` with allowance `alpha` is a real configuration `U` on the bare bonds of the complete footprint `F(p)` with

- (s1) `(M^l U)(c) = V_l(c)` on every row edge `c` of `p`, and `M^{l-1} U = V_{l-1}` on every level-(l-1)
  bond of the double block of every completed edge of `p`;
- (s2) `eps(U; F(p)) <= alpha L^{-2l}` and `alpha <= alpha_L`.

**Lemma 2.** If `p` has a supplier with allowance `alpha`, its defect is at most `2 alpha`.

*Proof.* `M^l = M o M^{l-1}`, so by (s1) the value of every edge of `p`, row or completed, is `(M^l U)(c)`.
Hence `V(dp) = (M^l U)(dp)`, and (AV2) with (s2) gives `abs(F_p) <= 2 alpha`. `square`

**Lemma 2a (two layers).** Let `F(p) subset Lay_{l-1} cup Lay_l` and let the bare plaquettes of `F(p)`
satisfy `abs(F) <= tau eps_l L^{-2l}` if all corners are in `Lay_l` and `abs(F) <= tau' eps_{l-1} L^{-2(l-1)}`
otherwise. Then (s2) holds with `alpha = max(tau, sqrt(2) L^2 tau') eps_l`, provided this is at most `alpha_L`.

*Proof.* `eps_{l-1} L^{-2(l-1)} = L^2 (eps_{l-1}/eps_l) eps_l L^{-2l}` and `eps_{l-1}/eps_l <= sqrt(2)` by the
proof of Lemma F1 (case `l < s`, `n = 1`). `square`

This is Y 65476-65477: "The witnesses on the complete footprints give `2 psi_l eps_l` for the datum
defect", with `psi_l := alpha / eps_l`. The symbol `psi_l` occurs in Y only at Y 65477-65478; Y does not
define it. The definition `psi_l = alpha/eps_l` is my reading; it agrees with Y 76666-76672 ("The ordinary
defect bound is of order `eps_q`. For a remade shell it has the factor `C_L L_flat^{2(q-k_0-1)_+}`, and a
collar departure has the factor `c_f L_flat^{2(q-k_0)_+}`").

### 5.2 The kinds of supplier, with their allowances

Each line gives the test, the bound it puts on bare plaquettes, and the resulting `psi_l`. `c_0 = pi/2`
converts a norm bound into a bound on `abs(F)`. The thresholds are quoted from Y; I did not rebuild the
definition of the tests.

| Kind | Test (positive on the trajectory) | Bare bound it gives | `psi_l` |
|---|---|---|---|
| (K-ord) | ordinary density test `chi_l(square)`; background: the local orbit of the cube, with the prescribed `V_l` | `norm(dU - 1) < eps_l L^{-2l}` on the one-layer enlargement of the cube (Y 134113-134117) | `c_0` |
| (K-shell) | shell clause of a stage test, shell `i` | `< (1 - beta_s(1 - 2^{-(j-i+1)})) L_flat^{2(i-k_0-1)_+} eps_i L^{-2i}` on bare plaquettes wholly in the shell (Y 63876) | `c_0 L_flat^{2(i-k_0-1)_+}` |
| (K-ext) | exterior clause of the stage test of level `j` | `< (1 - beta_s/2) c_l L_flat^{2e} eps_j L^{-2j}`, `c_l <= 3`, `e <= (j-k_0-1)_+` (Y 63876) | `3 c_0 L_flat^{2(j-k_0-1)_+}` |
| (K-x) | crossing clause `kappa_x` at the prepared face of the stage of level `j` | `< (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j-k_0-1)_+}` (Y 64308-64313) | `c_0 F_j` |
| (K-col) | collar departure: the stage test `chi_i^{(n+1)}` and the approximate collar bound at `2 delta'_{j'}`, `j' = i_flat + n` (Y 65436-65455) | stage-test bound on the reconstructed field; four collar links each within `2 delta'_{j'}` of it | `c_f L_flat^{2(l-k_0)_+}` (Y 76669-76670), plus `8 delta'_{j'}/eps_l` |
| (K-core) | restored core: the retained reference cutoff `abs(log V') < M_0 eps_i` and the surrounding ordinary tests (Y 65434-65435, 76680-76685, 63876 item (4)) | defect `<= C(M) eps_i` on the datum directly | `C(M, M_0)/2` |

A footprint that meets two layers, or a shell and the exterior, takes the larger bound after the
conversion of Lemma 2a, which costs the factor `sqrt(2) L^2`. So in every kind

`psi_l <= A_L L_flat^{2e}`, `e <= (l - k_0)_+`, with `A_L := max(3 sqrt(2) c_0 L^2, c_f, C(M, M_0)/2) + 8`,   (5.1)

where `k_0` is the cutoff of the operation that made the shell (for a stopped component, its own `k_0(i)`).

### 5.3 The bound `C_2 e_l`, and where `L_flat^2 < L` is used

**Lemma 2b.** Assume (FR), (T1), (T3), (LF), and (5.1). Then `2 psi_l eps_l <= C_2 e_l / R_l <= C_2 e_l` with

`C_2 := 2^{r+1} L L_flat^2 A_L`.

So "each test gives a bound `C e_l` directly" (Y 65484-65485). `C_2` depends on
`(L, L_flat, r, M, M_0, c_f)` only.

*Proof.* If `l <= k_0` then `e = 0` and `psi_l <= A_L`. If `k_0 < l <= k`, Lemma F3 gives
`L_flat^{2e} eps_l <= 2^r L L_flat^2 e_l / R_l`. `square`

(LF) enters only here, through Lemma F3: it makes the exponent `2 log_L L_flat` at most 1, so that
`psi_l <= C R_l <= C' (log theta_l)^r`, which is Y's claim (Y 65479-65484, 76671-76672). The "compressed
interval of length at most `log_L R_{k_0+1}`" is the identity `k - k_0 - 1 = log_L R_{k_0+1}`, and "the
frame comparison of the running scales" is Lemma F2. Without (LF), Lemma F3 still gives
`2 psi_l eps_l <= 2 . 4^r L^2 L_flat^2 A_L e_l`: the conclusion `C e_l` of this note survives with a
larger constant, because `e_l` carries `R_l^2` and the relaxation is below `R^2` whenever `L_flat < L`.
What is lost without (LF) is the spare factor `1/R_l`. The lead should record which of the two the
consumers of `psi_l <= C (log theta_l)^r` need; I found no consumer in this paragraph that needs more than
`C e_l`.

For (s2) one needs `alpha = psi_l eps_l <= C_2 ebar(gamma) <= alpha_L`: a ceiling on `gamma`.

### 5.4 The assignment (COV): the one step not proved here

**Statement (COV).** Let `x_N in Ent_N` with admitted trajectory `x_0, ..., x_N`, `N` the entrance of the
final stage of `X` at depth `m`. For every tested plaquette `p` (level `l >= 1`) of the old global datum
`D(x_N)` there are a moment `nu <= N`, a test `T` of one of the kinds of 5.2 carried at `nu` (so
`T(x_nu) = 1`), and a real configuration `U` such that

- (c1) `F(p)` lies in the set where `T` gives its bare bound, so (s2) holds with `alpha = psi_l eps_l`,
  `psi_l` as in (5.1);
- (c2) `p` is a tested plaquette of `D(x_nu')` for every `nu <= nu' <= N`, and its datum loop at `x_nu'`
  is a conjugate of its datum loop at `x_nu` (only moves (m1), (m4) touch its edges, or none);
- (c3) `U` is the background that `T` reads at `x_nu` (or, for (K-col), the reconstructed field), and it
  satisfies (s1) for the datum `D(x_nu)`.

For `l = 0` the bare datum test gives the defect directly (Y 65519-65520). For (K-core) the bound is on
the datum loop itself and (c3) is void.

**Corollary 5.2 (base bound; proved from Lemma 2, 2b, given (COV)).** At every `x_N in Ent_N`, every
tested plaquette of level `l` of the old global datum `D(x_N)` has defect at most `C_2 e_l`.

*Proof.* Lemma 2 at the moment `nu` with the supplier of (c1), (c3) gives defect `<= 2 psi_l eps_l` at
`x_nu`. By (c2) the defect at `x_N` is the same number. Lemma 2b. `square`

The constant in Corollary 5.2 is `C_2` at every entrance. The proof passes a *value* from the moment `nu` to
`N` by (c2); it never applies an estimate to a bound obtained at an earlier entrance. This is the first
half of the crux (section 9.2).

**What Y gives for (COV), and what is missing.** Y gives the assignment in prose (Y 65425-65474, repeated
at Y 76654-76689):

- untouched component, footprint missing the inset of its stage test region, untouched higher levels,
  unchanged action top: (K-ord) (Y 65427-65431);
- inner footprint in a tested shell: "the last positive stage test at that departure" (Y 65432-65433):
  (K-shell), (K-ext), (K-x);
- departure at the sharp collar split after `n` integrations: (K-col), with the ordinary test for a
  footprint outside the inset and the original strip tests for the old-wall reads (Y 65436-65457);
- restored core: (K-core) (Y 65434-65435);
- by moment (Y 65459-65474): before the first stage the untouched datum; while a positive stage test is
  carried, that test; after removal and before integration, the new positive stage test and the
  approximate collar test on the old collar variables; a standing departure below the waiting window
  keeps its earlier reads; gauge moves conjugate; a refresh keeps the inner slot; a restoration brings the
  tests of the restored datum.

Missing, so that (COV) is a **gap** and not a port: (a) Y has no definitions of "departure", "stopped
component", "inset of the stage test region" from which (c1) can be checked for a structure outside `X`;
(b) Y gives no argument for (c3) at a mixed loop (which background carries both the level-l rows and the
level-(l-1) rows of the completed edges); (c) for footprints that meet a face of an earlier shell Y says
itself that the literal clauses do not cover them: "A lower footprint can still meet a seam of an earlier
shell. The literal shell bound is on bare plaquettes wholly contained in that shell. The comparison test
at the last prepared seam supplies a different set of plaquettes" (Y 78316-78319), and then refers back to
this paragraph (Y 78320-78322).

**Inside `X` at the final entrance: the assignment I checked against Y's geometry (argued, not proved).**
This is the part of (COV) that statement (i) needs. Regions as in `library/inset-chart.md` section 2 and
`library/h-geo.md` section 2; `j = m - 1`.

1. Levels below `h` (the core `G_h`): (K-ord) from the density tests of T5 and the deltas under the core
   operation, or (K-core) (Y 63876: "the tests and delta functions that stand under the core operation
   ... make the data stored in the core regular").
2. Level `i`, `h <= i < j`, footprint wholly in the shell of level `i`: the shell clause of T9, at `nu = N`.
3. A seam loop at the last prepared face `dZ''_j`: footprint in the last shell, astride the face, and in
   the exterior; the shell clause, the crossing clause and the exterior clause of T9, at `nu = N`, with
   Lemma 2a. (c3): `U^-` has the old datum.
4. Level `j`, footprint in the exterior `(Omega_m^c minus Z''_j) cap X`: the exterior clauses of T9, at
   `nu = N`. This covers the collar `K`. No use of T6.
5. A seam loop at an earlier face `dZ''_{i+1}`, `i + 1 < j`. If the operation carries the crossings (T3),
   T9 contains the clause, at `nu = N`. In the default operation T9 has no clause on the bare plaquettes
   astride that face; this is case (c) above. The supplier is then the stage test of the stage of level
   `i`, at the moment `nu` just after that stage: its shell clause (inside), its crossing clause (astride),
   its exterior clause (outside), with Lemma 2a, and `U^{(.)}` of that stage has the datum of that moment.
   (c2): the rows of the loop lie within `L^{i+1}` of the face, inside the shells of levels `i` and `i+1`,
   whose widths are at least `u_{i+1} = M L^{i+1}` (Y 63846-63851); later stages change rows of level
   above `i + 1` only, and "all holonomies below level `j` are unchanged" (Y 65522-65523).
   Lemma 1 is what makes that earlier test available at `x_N`.
6. Level `m`, and the mixed loops at the old seam of `Omega_m`: T4 with (I4) of `library/rim-scale.md`,
   defect `<= 2.1 eps_m` ("The density cubes on `Omega_m^{~4}` cover the plaquettes near the old seam",
   Y 64096-64097). Statement (i) excludes these plaquettes anyway.

Items 2 to 5 use that the shells are wider than a footprint (`7 a_i` or `u_{i+1}` against `3 L^{i+1}/2`).
I did not write the containments as proofs; each is a comparison of box coordinates from Y 63786-63851.
