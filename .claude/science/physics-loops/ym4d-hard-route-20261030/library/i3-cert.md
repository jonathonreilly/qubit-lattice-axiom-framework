lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-10T10:40Z

Repairs applied 2026-11-10 (FINISH row 643, log `library/i3-apply.md`; old and new sentences in `library/i3-repairs.md`, row 634): A1 (c2'), (c3') and
the edge form of (s1); A2 one supplier for 5.4 items 3 and 5, the guard before the promotion; A3 the
seventh kind (K-wall) and `C_2'' = max(C_2, 6 . 4^r L^2)` (the constant that `library/cov-xstar-check.md`, row 639, accepts) in Lemma 2b, Corollary 5.2, (H5) and `C_3`; A4 Lemma 4
case A with `C_2''`; B1 Lemma 2.3a (local averaging); B2 Lemma 1' and (H4); B3 (m6) and fail factors; B4
the interior set of Lemma 6 (levels `l - 1, l, l + 1`), which is also (d1) of `library/cov-x-check.md` in its first form; B5 `L >= 13` in (G1); B6 (K-x), (K-col); B7 (H5) and
the order of constants, with (d2) of `library/cov-x-check.md`; B9 cite in F2; (COV) restated with (c2') up to conjugation and the wider set of moments (defect (6) of `library/cov-global-check.md`, row 636). Not applied: the rename
of `c_0`. The uses of the restated (COV) wait for one check by another model.

# i3-cert: the certificate `I(omega) = 1` on the entering support (registry row RIM-I3)

Status: DONE 2026-11-09 (one session, Claude Fable 5.2, medium; not checked by another model; no numerics run).

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

**Verdict: stop condition (iii).** `I(omega) = 1` on the entering support is proved from the retained
tests, with one named step not proved: the assignment lemma (COV) of section 5.4. No counterexample.
Not checked by a second model.

| Lemma of the row | Statement here | Status |
|---|---|---|
| 1 (definition) | Definitions 4.1-4.3: points, tests in force (E1)-(E5), admitted trajectories, `Ent_N`. Lemma 1: where the incoming term is not zero, the point is in `Ent_N` | definition; Lemma 1 **proved**, given that the term is an iterated integral |
| 2 (test to defect) | Lemma 2: a supplier on the complete footprint gives defect `<= 2 alpha`. Lemma 2b: `2 psi_l eps_l <= C_2'' e_l`, `C_2'' = max(C_2, 6 . 4^r L^2)`. `L_flat^2 < L` enters only in Lemma F3; without it `C e_l` still holds from `L_flat < L` | **proved**, given the averaging corollary of Y in local form (read, not rebuilt). *Which* test supplies *which* plaquette is (COV): **gap** |
| 3 (layer profile) | Lemma 3: defect `<= B e_l` at all levels gives `r_U <= K_w K_F B e_s` in layer `s`; `K_F` is bounded by an explicit convergent series (6.2), independent of the number of levels. Lemma D (layer distance) and Lemma F1 (growth of `e_l/e_s`) | **proved**, with `bgc:proper-background` and the weighted maximum **cited**, hypotheses checked in 6.1 |
| 4 (prospective datum) | Lemma 4: every tested plaquette of the prospective global datum has defect `<= C_3 e_l`, `C_3 = 2 c_0 L^2 C_F(1) C_2''`. Proof by one exact averaging step from the old level-j datum (Y 64097-64101). Remark 7.4: why the face lift does not enter | **proved**, given the base bound (Corollary 5.2) and the facts (G2), (G3) |
| 5 (varied old datum) | Lemma 5a, 5b: the old datum over the chart has defect `<= C_6 e_l`; only levels `j`, `q` move | **proved** given (V), (Lip) (gaps; not needed for `I = 1`) |
| crux | 9.2: a fixed chain of four constants at one entrance, restarted at `C_2''` at every entrance; no product over levels or entrances | **proved** as a statement about this note's proof |

Three findings the lead should know:

1. **Statements (i) and (ii) do not need the profile.** Lemma 4 gets the new level-q holonomies from the
   old level-j datum by one exact averaging step, as Y does at Y 64097-64101. Y's second form (Y 65536-65560,
   through `U_in` and the level-j profile) proves the same with a larger constant (Remark 7.2). So
   `I(omega) = 1` rests on (COV), the averaging estimate and the geometry, and on none of the four cited
   inputs. The profile is needed for the layerwise curvature bounds and for Lemma 5.
2. **The open step is the assignment, not an estimate.** (COV): every tested plaquette of the old global
   datum has a retained test with complete footprint. Y gives it in prose. Inside `X` I checked it against
   Y's boxes and found one uncovered case, which Y names itself (Y 78316-78319): loops at an *earlier*
   prepared face when the operation does not carry the old crossings. The repair is the exterior clause of the preceding guard at the entrance of the stage of level `i`,
   before the promotion, used at its own moment, with (c2') (5.4, items 3 and 5; `library/cov-x.md`
   Lemma 6.3, checked in `library/cov-x-check.md`). The stage test after the stage has no crossing clause in
   the default operation.
   Outside `X` nothing is checked.
3. **T6 must not be used at the entrance.** The approximate collar test reads `S_X = M^j U^+`, which
   exists only after the admission. The level-j collar rows are supplied by the exterior clauses of the
   preceding guard T9 (5.4, item 4). `Ent_N` is defined without T6, T8, T11, T12, T13.

`C_3` is uniform in `m`, the volume and the history. It depends on `(L, L_flat, r, c_5, Bbar, M, M_0, c_f)`;
the row's list omits the frame constants and `M_0, c_f` (9.2).

## 1. Repo search

- `library/open-core.md`: no entry for RIM-I3, `i3-cert`, "entering support" or `hi:prepared-real-endpoint`
  (grep, 2026-11-09). FINISH rows 609 (RIM-SCALE), 617 (INSET-CHART), 620 (`i3-read`) are the neighbours;
  the row says they are not duplicates. Row 620 is a reading and proves nothing. No other row covers the
  statement.
- In this lane the passage Y 65406-65591 is mentioned in FINISH row 624, `library/open-registry.md` (RIM-I3),
  `library/inset-chart.md` 5.2 (input (F1-Y), "I did not rebuild it") and `library/prior/i3-read.md` only.
- This checkout has only the branch `claude/ym4d-hard-route`; `origin/main` and the other PR branches are
  not fetched here, so I did not search them. A `git grep` of `HEAD` for the two labels outside the lane
  folder was stopped at its time limit without output; the checkout has no `research/ym4d` folder. I rely on the search recorded in `library/prior/i3-read.md`
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

Status: Y states both for a whole lattice with the global maximum. Y's proof of the one-step bound reads
curvature on a box `D_C` with an extra layer (Y 4800-4803, 4815-4816), so the fact that `M^l U` on the four
edges of `p` reads `U` only in `F(p)` gives the values, not the estimate. The local form of the estimate
is Lemma 2.3a.

**Lemma 2.3a (the one-step chart fits in the footprint; `library/i3-cert-check.md` Lemma 4.1).** For a
coarse plaquette `C`, the box `F(C)` (the union of the four corner blocks, a lattice box) can serve as
`D_C` in Y 4800-4880.

*Proof.* Each contour path of an edge `c = (y, y + L e_mu)` of `C` is a shortest path from `y` to
`x in B(y)`, the straight segment from `x` to `x + L e_mu in B(y + L e_mu)`, and a shortest path back to
`y + L e_mu`; a shortest lattice path lies in the coordinate box of its ends, so every path lies in
`F(C)`. Root the coordinate comb at the initial vertex of `C`; each comb path is coordinatewise
monotone, so it lies in `F(C)`. In the loop "comb path, edge `b`, comb path back", each interchange of
two consecutive unit steps replaces one vertex by the fourth corner of a unit square whose other three
corners are on the path; that corner has each coordinate equal to a coordinate of those three, so it
stays in the box, and so does the inserted plaquette. Hence the integers `n_{b,p}` of Y 4830-4834 are
supported on plaquettes of `F(C)`, and every quantity in Y 4806-4871 is read in `F(C)`. `square`

So (AV1) holds with `D(p) = F(p)` read on the level-(l-1) lattice. For (AV2), put
`eps_t(p) := max abs(F_q(M^t U))` over the level-t plaquettes `q` with all corners in `F(p)`; the blocks
are aligned and nested (Y 62001), so for such `q` at level `t + 1` the box `F(q)` is a union of order-(t+1)
blocks inside `F(p)`, and Lemma 2.3a gives the one-step bound for it. Y's recurrence
`eps_{t+1} <= L^2 eps_t (1 + C_L eps_t / L^2)` and its induction (Y 4927-4948) then run word for word, with
the constant 2. I read Y's proofs of (AV1), (AV2); apart from the localisation, I did not rebuild them. They
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
  at least `6 rho` sites in each direction at the top level; and, for (BG), `L >= 13` with the floors of
  the aligned separated geometry of `mb:datum-descent-critical-ascent` as raised at Y 35270-35275. All are
  fixed before `gamma`; none changes a constant of this note.
- (G2) `dist_infty(K, Omega_j^c) > 2 L^q`. Consequence: the footprint of a level-q plaquette `P` with a
  corner in `K` and no corner in `Omega_q` lies in `Lay_j`. (Each point of `F(P)` is within `3L^q/2` of the
  corner in `K`, so `F(P) subset Omega_j`; `Omega_q` is a union of order-q blocks, so the block of a corner
  outside `Omega_q` misses `Omega_q`.) Y: ("the order-`q`
  carrier stays inside the unchanged level-`j` member by the separation of the prospective sequence",
  Y 65550-65552; Y 72255-72258; Y 64097-64100).
- (G3) A level-(q+1) completed edge of the old sequence has its double block in `Omega_q`, at distance
  more than `2L^{q+1}` from `Omega_q^c` (Y 65529-65533). Empty for the final stage (`q = m` is the top).

## 3. Frame lemmas (proved)

`f(t) := t^{-1/2} (log t)^{p_0}` is decreasing for `t >= e^{2 p_0}`, and `eps_l = A_0 f(theta_l)`.
Floors on `T` used below: (T1) `T >= max(e^{2p_0}, 2 c_5, 4)`; (T2) `(1 + c_5/(T log T))^{p_0} <= 2`;
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
`L^{k - k_0 - 1} = R_{k_0+1}` (the compression identity, Y 63749, 63774-63776: `a_i = M R_i L^i`, `u_i = M L^i`, `a_{k_0+1} = u_k`). Then for
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

**Lemma F4 (weak coupling).** `max_l e_l <= ebar(gamma) := sup_{t >= gamma^{-2}} L^2 A_0 t^{-1/2} (log t)^{p_0 + 2r}`,
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
by the history: the place in the formula just before the prospective guard of that stage is applied; or
one of the other places at which `library/cov-global.md` takes a supplier: the output of a step, the exit
of a stage, and the place just after a stop or a main step (`library/cov-global-check.md` item (10)).
Definition 4.3 and Lemma 1 are read with this set of moments; the proof of Lemma 1 does not change. A
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
- (m5) a reference-law draw (restoration): the datum on the restored box is replaced;
- (m6) a deletion of a determining plaquette: the newly made layer uses its own regularity guard
  (Y 76686-76688), which supplies its loops. A loop crossed by an (m6) move has that guard as supplier,
  which is not in the table of 5.2; this concerns structures outside `X` (rows 628, 632). Lemma 1 does
  not use the list of moves.

The term is a finite sum of summands from decompositions of unity: the frame sum, the pass/fail split
`a_r + b_r = m` (Y 63836), drop-outs at a failed test (Y 63856), and failed sharp indicators carried as
separate factors (Y 65449-65450). Trajectories are taken summand by summand. The trajectory is *admitted*
if at every moment `nu <= N` every indicator factor carried by its summand at that moment (pass factors
`chi` and fail factors `1 - chi`) equals one at `x_nu`, and every carried delta constraint holds. (E1)-(E4)
are pass factors at the entrance of a stage that is entered. Points are read in the original
variables: coordinate changes that keep the datum (`V'' = e^{i g_k B} V_0`, Y 63858; `V'' = V' V_0`,
Y 78327-78330) are not moves. The *entering support* `Ent_N` is the set of end
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

**Lemma 1' (measure form; `library/i3-cert-check.md` item 2).** Let `mu_nu` be the (complex) measure of
the incoming term at moment `nu`. For every Borel set `B` with `B cap Ent_N` empty, `|mu_N|(B) = 0`.

*Proof.* `mu_N(B) = int (1_B chi_N)(f(x, y)) K(x, dy) mu_{N-1}(dx)`, `f` the move, `K` the kernel, `chi_N` the
product of the indicator factors imposed at `N` (the factors carried at `N - 1` are already in `mu_{N-1}`).
If `x` is the end of an admitted trajectory, then either `chi_N(f(x, y)) = 0` or `f(x, y)` is the end of an
admitted trajectory; in both cases `(1_B chi_N)(f(x, y)) = 0`. By induction `|mu_{N-1}|` is carried by
`Ent_{N-1}`, so the integrand vanishes `|mu_{N-1}|`-almost everywhere, and the same holds for
`|mu_N| <= |chi_N| f_*(|K| |mu_{N-1}|)`. Base: `mu_0` carries its own indicators. `square`

Measurability of `Ent_N` is not needed: only Borel sets disjoint from it are measured. The set
`{I != 1}` is Borel (finitely many continuous functions of finitely many links) and, by Theorem 9.1,
disjoint from `Ent_N`; so `I = 1` holds `|mu_N|`-almost everywhere. Lemma 1 is the pointwise form, valid
when the term is read as the function given at every point by its iterated-integral formula.

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

- (s1) `(M^l U)(c) = V(c)` for each of the four edges `c` of `p`, where `V(c) := V_l(c)` on a row edge
  and `V(c) := M(V_{l-1})(c)` on a completed edge (edge form, `library/cov-x.md` section 3). The bondwise
  form `M^{l-1} U = V_{l-1}` on the double blocks implies it and is not required; it can fail for (K-ord)
  at a mixed loop (`library/cov-x.md` finding 4);
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
| (K-x) | crossing clause `kappa_x` astride `dZ''_m` of the final inset test, in the prospective background (Y 64308-64313). It is imposed after the entrance, like T6, and is **not carried at the entrance**; a crossing clause is carried only if the operation has the added crossing tests (T3; Y 64384-64386). No step of 5.4 uses it (A2) | `< (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j-k_0-1)_+}` | `c_0 F_j` |
| (K-col) | collar departure: the stage test `chi_i^{(n+1)}` and the approximate collar bound at `2 delta'_{j'}`, `j' = i_flat + n` (Y 65436-65455) | stage-test bound on the reconstructed field; four collar links each within `2 delta'_{j'}` of it | `c_f L_flat^{2(l-k_0)_+}` (Y 76669-76670), plus `8 delta'_{j'}/eps_l`. `c_f` occurs in Y only at Y 76670 and is not defined there; put `c_f := 3 sqrt(2) c_0 L^2` (from the (K-shell)/(K-ext) bound with Lemma 2a; **unproved**, `library/i3-cert-check.md` item 5). Used only for departures outside `X` |
| (K-core) | restored core: the retained reference cutoff `abs(log V') < M_0 eps_i` and the surrounding ordinary tests (Y 65434-65435, 76680-76685, 63876 item (4)) | defect `<= C(M) eps_i` on the datum directly | `C(M, M_0)/2` |
| (K-wall) | original density tests of level `l'` at the wall `dO_{l'}`, `k_0 < l' <= j`, carried at the entrance `nu_{l'}` of the stage of level `l'` (Y 64697-64716, 77673-77686); coarse supplier of depth `d = j - l'` (`library/cov-x.md` Definition 3.1, Lemma 6.4; Y 77647-77704) | `abs(F_q) <= 2.1 eps_{l'}` on the level-l' plaquettes of `F(p)`, i.e. allowance `alpha = 3 . 4^r e_j` at depth `d >= 1` | `<= 3 . 4^r L^2 R_l^2` at level `l`: `3 . 4^r R_j^2` at the walls inside `X` at the final entrance (`library/cov-x.md` Lemma 6.4); the factor `L^2` is needed for a plaquette made at the last stage of an operation (`library/cov-xstar.md` (Q3), `library/cov-xstar-check.md` item (6)); not within (5.1) |

A footprint that meets two layers, or a shell and the exterior, takes the larger bound after the
conversion of Lemma 2a, which costs the factor `sqrt(2) L^2`. So in every kind except (K-wall)

`psi_l <= A_L L_flat^{2e}`, `e <= (l - k_0)_+`, with `A_L := max(3 sqrt(2) c_0 L^2, c_f, C(M, M_0)/2) + 8`,   (5.1)

where `k_0` is the cutoff of the operation that made the shell (for a stopped component, its own `k_0(i)`).
For (K-wall), `psi_l <= 3 . 4^r L^2 R_l^2` is of order `(log theta_l)^{2r}`, not `<= C R_l`; (5.1) fails there.
It enters only through Lemma 2b below, as `2 psi_l eps_l <= 6 . 4^r L^2 e_l` (`library/cov-x.md` finding 3;
`library/cov-xstar-check.md` item (6)).

### 5.3 The bound `C_2'' e_l`, and where `L_flat^2 < L` is used

**Lemma 2b.** Assume (FR), (T1), (T3), (LF), and (5.1) for the kinds other than (K-wall). Then for those
kinds `2 psi_l eps_l <= C_2 e_l / R_l <= C_2 e_l`, and for every kind, (K-wall) included,
`2 psi_l eps_l <= C_2'' e_l`, with

`C_2 := 2^{r+1} L L_flat^2 A_L`,  `C_2'' := max(C_2, 6 . 4^r L^2)`.

So "each test gives a bound `C e_l` directly" (Y 65484-65485). `C_2` depends on
`(L, L_flat, r, M, M_0, c_f)` only.

*Proof.* If `l <= k_0` then `e = 0` and `psi_l <= A_L`. If `k_0 < l <= k`, Lemma F3 gives
`L_flat^{2e} eps_l <= 2^r L L_flat^2 e_l / R_l`. For (K-wall), `2 psi_l eps_l <= 6 . 4^r L^2 R_l^2 eps_l = 6 . 4^r L^2 e_l`;
for `d = 0` its defect is `2.1 eps_l <= 2 c_0 eps_l <= C_2 e_l`. Both bounds are at most `C_2'' e_l`. `square`

(LF) enters only here, through Lemma F3: it makes the exponent `2 log_L L_flat` at most 1, so that
`psi_l <= C R_l <= C' (log theta_l)^r`, which is Y's claim (Y 65479-65484, 76671-76672). The "compressed
interval of length at most `log_L R_{k_0+1}`" is the identity `k - k_0 - 1 = log_L R_{k_0+1}`, and "the
frame comparison of the running scales" is Lemma F2. Without (LF), Lemma F3 still gives
`2 psi_l eps_l <= 2 . 4^r L^2 L_flat^2 A_L e_l`: the conclusion `C e_l` of this note survives with a
larger constant, because `e_l` carries `R_l^2` and the relaxation is below `R^2` whenever `L_flat < L`.
What is lost without (LF) is the spare factor `1/R_l`. The lead should record which of the two the
consumers of `psi_l <= C (log theta_l)^r` need; I found no consumer in this paragraph that needs more than
`C e_l`.

For (s2) one needs `alpha = psi_l eps_l <= C_2'' ebar(gamma) <= alpha_L`: a ceiling on `gamma`. For
(K-wall) the allowance is `<= 3 . 4^r L^2 e_l <= C_2'' ebar(gamma)`.

### 5.4 The assignment (COV): the one step not proved here

**Statement (COV).** Let `x_N in Ent_N` with admitted trajectory `x_0, ..., x_N`, `N` the entrance of the
final stage of `X` at depth `m`. For every tested plaquette `p` (level `l >= 1`) of the old global datum
`D(x_N)` there are a moment `nu <= N` of Definition 4.1 (it may come before the first moment at which `p` is a
tested plaquette, as for a stage supplier), a test `T` of one of the kinds of 5.2 carried at `nu` (so
`T(x_nu) = 1`), and a real configuration `U` on the bare bonds of `F(p)` (a *bare supplier*) or, for a
*coarse supplier* of depth `d = l - l'`, a configuration `W` on the level-l' bonds of `F(p)`, such that

- (c1) `F(p)` lies in the set where `T` gives its bare bound, so (s2) holds with `alpha = psi_l eps_l`,
  `psi_l` as in (5.1); for (K-wall), in the coarse form `abs(F_q(W)) <= alpha L^{-2d}` for every level-l'
  plaquette `q` with corners in `F(p)`, `alpha = psi_l eps_l` with `psi_l` of the (K-wall) row
  (`alpha = 3 . 4^r e_j` at the walls inside `X` at the final entrance; `library/cov-x.md` Definition 3.1);
- (c2') the datum loop of `p` at `x_N` is a conjugate of `(M^l U)(dp)`, respectively of `(M^d W)(dp)`. This
  holds in particular if `(M^l U)(c) = V(c)` at `x_N` for each of the four edges `c` of `p` (`V(c)` as in
  (s1)), respectively `(M^d W)(c) = V(c)` (`library/cov-x.md` Definition 3.1). The plaquette need not be a
  tested plaquette of `D(x_nu)`;
- (c3') `U` is the restriction to `F(p)` of the configuration that `T` reads at `x_nu` (or, for (K-col),
  the reconstructed field); for a coarse supplier, `W` is the level-l' datum at `x_nu`.

For `l = 0` the bare datum test gives the defect directly (Y 65519-65520). For (K-core) the bound is on
the datum loop itself: (c2') reads that the datum loop of `p` at `x_N` is a conjugate of its datum loop at
`x_nu`, and (c3') is void.

**Corollary 5.2 (base bound; proved from (AV2) and Lemma 2b, given (COV)).** At every `x_N in Ent_N`, every
tested plaquette of level `l` of the old global datum `D(x_N)` has defect at most `C_2'' e_l`.

*Proof.* By (c2') the datum loop of `p` at `x_N` is a conjugate of `(M^l U)(dp)`, or of `(M^d W)(dp)` for a
coarse supplier, and the defect is invariant under conjugation. (AV2) with (c1) gives defect
`<= 2 psi_l eps_l` at `x_N`; for a coarse supplier, (AV2) on the level-l' lattice at depth `d`
(`library/cov-x.md` Lemma 3.2). For (K-core) the bound on the datum loop at `x_nu` is carried to `x_N` by
(c2'). Lemma 2b. `square`

The constant in Corollary 5.2 is `C_2''` at every entrance. The proof passes a *value* from the moment `nu` to
`N` by (c2'); it never applies an estimate to a bound obtained at an earlier entrance. This is the first
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
3. A loop at the last prepared face `dZ''_j`. Footprint wholly in the last shell: the shell clause of
   T9 at `nu = N`. Wholly in the exterior: item 4 (or item 7 at an original wall). With a corner in `Z''_j` and the footprint astride the face (case P4 of
   `library/cov-x.md`, `l = j`): the exterior clause of the preceding guard `chi_m^{(j-1-h)}` at the
   entrance `nu_{j-1}` of the stage of level `j - 1`, before the promotion (`library/cov-x.md` Lemma 6.3;
   Y 77621-77645), with (c2'), (c3') and `psi_j = sqrt(2) c_0 L^2 L_flat^{2(j-k_0-2)_+}`. No crossing
   clause is used: in the default operation T9 has none (Y 64278, 64371-64373).
4. Level `j`, footprint in one exterior region of T9 inside `(Omega_m^c minus Z''_j) cap X` (case P5a of
   `library/cov-x.md`): the exterior clauses of T9, at `nu = N`. A footprint in `K` astride an original
   wall is item 7. No use of T6.
5. A seam loop at an earlier face `dZ''_{i+1}`, `h <= i`, `i + 1 < j`, with a corner in `Z''_{i+1}`
   (case P4 of `library/cov-x.md`, `l = i + 1`). In the default operation T9 has no clause on the bare
   plaquettes astride that face; this is case (c) above. The supplier is the same as in item 3: the
   exterior clause of the preceding guard `chi_m^{(i-h)}` at the entrance `nu_i` of the stage of level
   `i`, before the promotion. The whole footprint lies in one exterior region of that guard, inside the
   layer of index `i`, and the loop at `x_N` is the level-(i+1) plaquette of the averages of that guard's
   background ((c2'), (c3'); `library/cov-x.md` Lemma 6.3; Y 77557-77589, 77609-77645), with
   `psi_{i+1} = sqrt(2) c_0 L^2 L_flat^{2(i-k_0-1)_+}`. The stage test just after the stage is not used:
   its clause `kappa_x` astride the face exists only in the split with added crossing tests
   (Y 64384-64386). Lemma 1 is what makes the earlier guard available at `x_N`.
6. Level `m`, and the mixed loops at the old seam of `Omega_m`: T4 with (I4) of `library/rim-scale.md`,
   defect `<= 2.1 eps_m` ("The density cubes on `Omega_m^{~4}` cover the plaquettes near the old seam",
   Y 64096-64097). Theorem 9.1 (i) does not exclude them; they are covered here.
7. Level `j`, footprint astride an original wall `dO_{l'}`, `k_0 < l' <= j`, inside the exterior (case P5b
   of `library/cov-x.md`; these walls lie in `K` and no clause of T9 reads them, Y 77647-77704): (K-wall),
   the level-l' density tests at `nu_{l'}` and the exact averages of depth `j - l'`
   (`library/cov-x.md` Lemma 6.4). Defect `<= 6 . 4^r e_j`, or `<= 2.1 eps_j` if `l' = j`.

Items 2 to 5 use that the shells are wider than a footprint (`7 a_i` or `u_{i+1}` against `3 L^{i+1}/2`).
I did not write the containments as proofs; each is a comparison of box coordinates from Y 63786-63851.

## 6. Lemma 3: the layer profile

### 6.1 The two cited inputs, with their hypotheses

**(BG) `bgc:proper-background` (Y 35634-35646).** "For the geometry fixed above there are `a_0, a_1, C_B > 0`,
independent of depth and volume, with `C_B a_1 < a_0`, such that every real mixed datum whose ordinary and
mixed test holonomies are within `eps <= a_1` of one has a constrained-critical configuration `U(V)` with
`M_B U(V) = V`, `R_mat(U(V)) <= C_B eps`. Any two critical configurations for the same datum with
`R <= a_0` lie in the same residual gauge orbit."
Hypotheses here: the geometry is (G1); the datum is real; the test holonomies are the tested plaquettes of
Definition T ("ordinary" = all edges rows, "mixed" = some edge completed, Y 10604-10611), with no pinch
tests because no inward row is kept. The size hypothesis is supplied by Corollary 5.2 or Lemma 4 with
`eps = C ebar(gamma)`.

**(WM) `hi:real-datum-profile` with `mb:datum-profile`, `mb:weighted-maximum` (Y 15317-15338, 12471-12503,
35618-35627).** In the geometry (G1), let `U` be critical and regular at the radius `a_c`. Let
`r_U(x)` be the maximum of `L^{2 lambda(p)} norm(dU(p) - 1)` and `L^{3 lambda(b)} abs(J(U)(b))` (bare units)
over the plaquettes and full bonds based at `x`, `lambda` the largest corner layer (Y 65501-65504,
15327-15330). Let `v(tau)` be the defect of the datum test `tau`, and
`P(x) := sup_tau e^{-delta d_B(x, tau)} v(tau)`, the distance to a tested plaquette being the minimum over
its corners (Y 12451-12452). Then

`r_U(x) <= K_w P(x)`,   (6.1)

with `K_w` and `delta > 0` depending only on the constants of the local estimate (`K_loc`, `R = 20 L sigma`,
`e^{delta R} = sqrt(2)`, `K_w = 5 K_loc` times the fixed factor for the displacement of a readout,
Y 35620-35625). "No maximum has to be attained, so the proof works on infinite volume as well when the
input radius is bounded" (Y 12492-12495).
Hypotheses here: (G1); `U` is the orbit given by (BG), and its radius `C_B C ebar(gamma)` is at most `a_c`
for `gamma` small. As in `library/rim-scale.md` Theorem 6.2, I use that the radius `R_mat` of (BG) bounds
the radius `r_U` of (WM) up to a fixed factor; Y uses them so (Y 65495-65498) and I did not check the
conversion.

### 6.2 The layer distance (proved)

`d_B` is the infimum over paths of `int ds / xi(s)`, `xi` the local pillar scale (Y 12395-12402); in `Lay_t`
the pillar scale is `L^t` (bare units). A lattice version differs by a fixed factor; let `c_B in (0, 1]`
be that factor.

**Lemma D.** Let `x in Lay_s` and let `p` be a tested plaquette of level `l`. Then
`d_B(x, p) >= c_B rho (abs(l - s) - 2)_+`.

*Proof.* Let `y` be a corner of `p`; `y in Lay_{l'}` with `l' in {l - 1, l}`. Let `l' > s`. For each `t`
with `s + 1 <= t <= l' - 1`: `x notin Omega_{s+1} supset Omega_t`, and `y in Omega_{l'} subset Omega_{t+1}`.
A path from `x` to `y` has a first time in `Omega_{t+1}`, and before it a last time in `Omega_t^c`; between
the two it runs in `Lay_t`, and its Euclidean length there is at least
`dist_infty(Omega_t^c, Omega_{t+1}) > rho L^t`. Its weighted length there is at least `rho`. The pieces for
different `t` lie in disjoint layers. There are `l' - 1 - s >= l - s - 2` values of `t`. For `l' < s`
exchange the roles: for `l' + 1 <= t <= s - 1`, `y notin Omega_t` and `x in Omega_{t+1}`; there are
`s - 1 - l' >= s - l - 1` values. `square`

This is Y 65511-65515: "The place of a tested level-`l` plaquette is in `L_l`, and its corners lie in
layers `l - 1, l`. From layer `s` the path to this read crosses the intervening layers, giving distance at
least `c (abs(l - s) - 2)_+`", with `c = c_B rho`.

### 6.3 The lemma

Put `kappa := delta c_B rho`, `k_r := ceil(2r)`, and

`K_F := sup_{n >= 0} C_F(n) e^{-kappa (n - 2)_+}`,
`K_F <= S_F := sum_{n >= 0} C_F(n) e^{-kappa (n-2)_+} <= sqrt(2) L^2 e^{2 kappa} (1 + c_5 + Bbar)^{k_r} k_r! (1 - e^{-kappa})^{-(k_r + 1)}`.   (6.2)

*Proof of (6.2).* `C_F(n) <= sqrt(2) L^2 (1 + c_5 + Bbar n)^{k_r} <= sqrt(2) L^2 (1 + c_5 + Bbar)^{k_r} (1 + n)^{k_r}`
(both entries of the maximum in Lemma F1 are below this, since `L >= 3` and `1 + log(1 + u) <= 1 + u`).
`(e^{-kappa(n-2)_+} <= e^{2 kappa} e^{-kappa n})`. And `sum_{n >= 0} (n + 1)^k x^n <= k! (1 - x)^{-(k+1)}` for
`0 <= x < 1`, because `(n+1)^k <= k! binom(n + k, k)` and `sum_n binom(n + k, k) x^n = (1 - x)^{-(k+1)}`. `square`

The series converges, and its bound contains `kappa, c_5, Bbar, r, L` only. The number of levels does
not occur: the sum is over all `n >= 0`.

**Lemma 3 (layer profile).** Assume (G1), (FR), (T1), (T2). Let `V` be a real datum on a region sequence,
with every tested plaquette of level `l` of defect at most `B e_l`, for all `l`. Let `B ebar(gamma) <= a_1`
and `C_B B ebar(gamma) <= a_c`. Then the orbit `U(V)` of (BG) satisfies, at every bare site `x in Lay_s`,

`r_U(x) <= K_w K_F B e_s`.

*Proof.* (BG) applies with `eps = B max_l e_l <= B ebar(gamma)` (Lemma F4). (WM) applies. By Lemma D and
Lemma F1, `P(x) <= sup_l B e_l e^{-kappa (abs(l-s) - 2)_+} <= B e_s sup_l C_F(abs(l - s)) e^{-kappa (abs(l-s)-2)_+} <= B K_F e_s`.
Then (6.1). `square`

So `C' = K_w K_F B`: one application of (WM) to one datum. The constant is the product of three numbers
fixed before `gamma`, and none of them is a power of a per-level factor. Y applies "the same profile on
both stage sequences" (Y 65520-65521): Lemma 3 is used once for the old sequence (`B = C_2''`) and once for
the prospective one (`B = C_3`), each time from the datum bound of that sequence.

## 7. Lemma 4: the prospective datum

**Lemma 4.** Assume (G2), (G3), (AV1), Definition T, (E1), and the base bound of Corollary 5.2 at
`x in Ent_N`. Let `gamma` be so small that `c_0 C_2'' ebar(gamma) <= min(eps_L, L^2/C_L)` and `C_2'' ebar(gamma) <= 1`. Then every tested
plaquette of level `l` of the prospective global datum `D'(x)` has defect at most `C_3 e_l`,

`C_3 := 2 c_0 L^2 C_F(1) C_2''`,  `C_F(1) = max(2 (1 + Bbar)^{1/2}, sqrt(2) L^2 (1 + log(1 + c_5 + Bbar))^{2r})`.

*Proof.* `C_3 >= C_2''`. I go through the levels (Y 65522-65535).

`l < j`. `Omega_l, Omega_{l+1}` and `Omega_{l-1}` are unchanged, so the tested plaquettes, their row
edges, their completed edges and all values are the old ones. Corollary 5.2.

`l = j`. A prospective tested plaquette has a corner in `Omega_j` and none in `Omega'_q supset Omega_q`, so
it is an old tested plaquette. Its row edges are old rows with the old values (`Gamma'_j subset Gamma_j`);
its completed edges read `Lay_{j-1}`, unchanged. Corollary 5.2.

`l = q`. Let `P` be a prospective tested plaquette of level `q`: a corner in `Omega'_q = Omega_q cup K`,
none in `Omega_{q+1}`.

Case A: no corner of `P` in the old `Omega_q`. Then `P` has a corner in `K`, and by (G2) `D(P)` lies in the
old `Lay_j`. Every level-j bond of `D(P)` touches `Omega_j` and has no endpoint in `Omega_q`, so it is an
old row; put `W := V_j` on `D(P)`. Every level-j plaquette of `D(P)` has its corners in `Lay_j`, so it is
an old tested plaquette, with all four edges rows; by Corollary 5.2 and 2.3, `eps(W; D(P)) <= c_0 C_2'' e_j` (this includes the plaquettes of `D(P)` astride
an original wall, item 7 of 5.4).
Every edge `c` of `P` has the prospective value `M(W)(c)`: if `c` touches `K` it is a new row and (E1)
gives `V_q(c) = M(V_j)(c)`; otherwise both ends are in `Lay'_j` and it is a completed edge of the
prospective sequence, with value `M(V_j)(c)` on its double block, whose bonds are in `Gamma'_j subset Gamma_j`
with the old values. So `D'(dP) = (M W)(dP)`, and (AV1) gives
`abs(F_P) <= L^2 c_0 C_2'' e_j + C_L (c_0 C_2'' e_j)^2 <= 2 L^2 c_0 C_2'' e_j <= 2 L^2 c_0 C_2'' C_F(1) e_q`.

Case B: `P` has a corner in the old `Omega_q`. Then `P` is an old tested plaquette of level `q`. An edge
that touches the old `Omega_q` is an old row with its old value. An edge `c` that does not has both ends
in the old `Lay_j`; in the old datum it is a completed edge with value `M(V_j)(c)`. In the prospective
datum it is a new row (if it touches `K`), with value `M(V_j)(c)` by (E1), or a completed edge, with the
same value as in case A. So the datum loop is the old one. Corollary 5.2.

`l = q + 1`. The tested plaquettes are the old ones (`Omega_{q+1}, Omega_{q+2}` unchanged). Row edges keep
their values. A completed edge has both ends in the old `Omega_q` (old separation) and, by (G3), its
double block is in the old `Omega_q`, where `Gamma'_q` has the old rows with the old values. Corollary 5.2.

`l > q + 1`. Nothing changes. `square`

**Remark 7.1 (this is Y's argument).** Case A is Y 64097-64101 ("the averaging blocks of a newly tested
plaquette are in the preceding member of level `j` ... Here the fine plaquettes are formed from the old
determining rows, and the exact one-step average gives the coarse bound") and Y 65540-65549. Case B is
Y 65538-65539 ("A determining row that met the old `Omega_q` keeps its value") with Y 72270-72276.

**Remark 7.2 (Y's second form, through `U_in`).** Y 65536-65560 writes the same bound through the old
orbit: with `U_in = U(D(x))` from (BG), `(M^j U_in) = V_j` on `D(P)`, so `D'(dP) = (M^q U_in)(dP)`; the old
level-j profile (Lemma 3 with `B = C_2''`) and the conversion of 2.3 give bare curvature at most
`c_0 K_w K_F C_2'' e_j L^{-2j}` on `F(P) subset Lay_j`; (AV2) gives `abs(F_P) <= 2 L^2 c_0 K_w K_F C_2'' e_j`.
This is "`C(L) e_j <= C'(L) e_q`" (Y 65556). It proves the same statement with the larger constant
`2 c_0 L^2 K_w K_F C_F(1) C_2''`. Lemma 4 as proved above does not use Lemma 3 at all; so statements (i)
and (ii) do not depend on (WM), and of the four cited inputs they use none. Lemma 3 is needed for the
curvature and current bounds "with `C e_s` in layer `s`" (Y 65561-65563) and for Lemma 5.

**Remark 7.3 (the other convention for tested plaquettes).** If a level-q plaquette counts as tested by
its place, there can be prospective tested plaquettes with the place in `K` that are not old tested
plaquettes although a corner is in the old `Omega_q`. The loop is the same level-q loop as in case B, and
in case B's convention it is covered. In the place convention its bound must come from a test: at the
final stage it has a corner in a carried top density cube (Y 64093-64097), which gives `2.1 eps_m <= C_2 e_m` by (I4)
of `library/rim-scale.md`; Theorem 9.1 (i) does not exclude it. At an earlier stage use Remark 7.2 with the old
profile on `Lay_j cup Lay_q`.

**Remark 7.4 (why the face lift does not enter).** Y 65557-65558: "The artificial face lift of the
localized problem does not enter this global calculation." Reason: Lemma 4 is about the global datum
`D'(x)`. Its rows are rows of the global sequences. The lifted rows of the tower at `dX` are rows of the
problem localized in `X` only; no edge of a tested plaquette of `D'(x)` is one of them. Every stencil
`D(P)` of case A lies in the old `Lay_j` near `K`, and `K subset Omega_m^c cap X` is two level-m cells
inside `X` (Y `eq:elab-history-quiet-boxes`: `O_m = H_m^{[8 a_m]}`, `X = H_m^{[10 a_m]}`), while the tower
is within `3 M_1 L^q` of `X^c` (`library/h-geo.md` Lemma 3.1). The lift enters only in Lemma 6.

**Lemma 6 (statement (i) from statement (ii)).** Let `p` be a tested plaquette of the prospective joined
datum of `X` that is not a tower holonomy. Then `p` is a tested plaquette of the prospective global datum
with the same datum loop. Hence its defect is at most `C_3 e_l`.

*Proof.* The joined sequence is `J_l = Omega'_l cap T_l` with `T_.` the tower of `X` (`library/h-geo.md`
Theorem). "Upon joining to the tower of the component, an interior holonomy is unchanged. A holonomy on
the joining collar is trivial or equals a top plaquette holonomy of the original datum" (Y 72277-72280;
Y 134207-134210; (R1) of `library/rim-scale.md`). A tested plaquette of level `l` is *interior* when its
footprint and the double blocks of its edges lie
where `T_t =` everything for `t = l - 1, l, l + 1` (`t <= m`), that is, where `J_t = Omega'_t` for these `t`.
Level `l + 1` is needed because it decides which edges of `p` are rows and whether `p` is tested
(Definition T). A *tower holonomy* is a tested plaquette of the joined datum that is not interior, at
every level, the top level included (Y 13100-13102: either `R(p) subset W^{(-2)}`, or `R(p) subset Q_a`
for a part with `q <= j_a`); Y bounds those through (R1) (Y 13117-13126). For an interior plaquette
Definition T gives the same tested status, the same edges and the same values for the two sequences.
(This is the first form of (d1) in `library/cov-x-check.md`. A plaquette with `F(p) subset Int` of
`library/cov-x.md` Definition 7.1 is interior here, since every point of `Int` lies in every `T_q`
(`library/h-geo.md` Lemma 3.1); for it the conclusion is `library/cov-x.md` Lemma 7.2 (a).) Lemma 4. `square`

Lemma 6 takes the trichotomy as the definition of "tower holonomy"; the trichotomy itself is (R1) of
`library/rim-scale.md`, which I did not re-prove.

## 8. Lemma 5: the varied old datum

Lemma 5 is not needed for `I(omega) = 1`. It is the last part of Y's paragraph (Y 65565-65585) and feeds
(Y-PATH) of `library/inset-chart.md` 5.3: the old datum over the whole collar chart is regular.

Setting. Let `x in Ent_N`, so by Lemma 4 the prospective global datum `D'` has the bounds `C_3 e_l`. Let
`C_3 ebar(gamma) <= a_1` and `C_B C_3 ebar(gamma) <= a_c`, and let `U^+_g := U(D')` be the global prospective
orbit of (BG). Put `D^0 := (M^l U^+_g on Gamma_l)_l`, the averages of this configuration on the *old*
determining set (Y 65565-65567). Put

`K_G := sup_{n >= 0} C_F(n) L^{-2n}` (finite by (6.2) with `e^{-kappa}` replaced by `L^{-2}`),
`C_5 := 2 c_0 L^2 K_w K_F K_G C_F(1) C_3`.

**Lemma 5a (the centre).** Assume in addition `rho >= 2L`, (AV2), and `L^2 c_0 K_w K_F K_G C_3 ebar(gamma) <= alpha_L`.
Every tested plaquette `p` of level `l` of the old sequence has defect at most `C_5 e_l` in `D^0`.

*Proof.* `l >= 1`. `p` has a corner `y_0` in `Omega_l`. Every corner of `p` is within `L^l` of `y_0` in the
sup norm, and every point of `F(p)` is within `L^l/2` of a corner. So `F(p)` is within `3L^l/2` of
`Omega_l`. Since `dist_infty(Omega_{l-1}^c, Omega_l) > rho L^{l-1} >= 2L^l`, `F(p) subset Omega_{l-1}`
(Y 65568-65569: "its order-`l` carrier is inside the old member of level `l - 1`"). Since `Omega'_t supset Omega_t` for every `t`, each point of
`F(p)` is in `Omega'_{l-1}`: its prospective layer is `lambda >= l - 1` (Y 65569-65570). By Lemma 3 for the
prospective sequence (`B = C_3`) and 2.3, a bare plaquette `b` of `F(p)` with largest prospective corner
layer `lambda` has

`abs(F_b) <= c_0 K_w K_F C_3 e_lambda L^{-2 lambda} = c_0 K_w K_F C_3 [e_lambda L^{-2(lambda - l + 1)}] L^{-2(l-1)} <= c_0 K_w K_F K_G C_3 e_{l-1} L^{-2(l-1)}`,

by Lemma F1 ("the powers `L^{-2(s-l+1)}` absorb the frame variation in `e_s/e_{l-1}`", Y 65571-65572). So
`U^+_g` is a supplier of `p` for the datum `D^0` ((s1) holds by the definition of `D^0`) with
`alpha = L^2 c_0 K_w K_F K_G C_3 e_{l-1}`. Lemma 2 gives defect `<= 2 alpha <= C_5 e_l`.
`l = 0`: the bare plaquette has prospective layer `lambda >= 0`, and the same display gives
`c_0 K_w K_F K_G C_3 e_0`. `square`

**Lemma 5b (the fibre).** Let `V^B` be an old datum that equals `D^0` except on level-j rows, where
`norm(V^B_j(b) D^0_j(b)^{-1} - 1) <= C_V delta'_j` (hypothesis (V)). Assume the one-step average is
Lipschitz on its regular branch: `norm(M(W)(c) - M(W')(c)) <= C_M max_b norm(W(b) - W'(b))` over the double
block of `c` (hypothesis (Lip), `C_M = C_M(L)`). Then every tested plaquette of level `l` of `V^B` has
defect at most `C_6 e_l`, `C_6 := C_5 + 4 max(1, C_M) C_V C_F(1)`, and the defect differs from that in
`D^0` only for `l in {j, q}`.

*Proof.* By Definition T a level-j row is read by a tested plaquette of level `l` either as a row edge,
and then `l = j`, or inside the double block of a completed edge, and then `l - 1 = j`. For `l = j` the
four edge values move by at most `C_V delta'_j` each (the completed edges read level `j - 1` and do not
move). For `l = q` the row edges do not move and each completed edge moves by at most `C_M C_V delta'_j`.
For unitary factors `norm(abcd - a'b'c'd') <= norm(a - a') + norm(b - b') + norm(c - c') + norm(d - d')`. So
the loop moves by at most `4 max(1, C_M) C_V delta'_j`, and
`delta'_j <= eps_j <= e_j <= C_F(1) e_q`. `square`

Then (BG) and Lemma 3 apply to `V^B` with `B = C_6`, for `gamma` small: "The old orbit on the varied fibre
has the same layerwise bound from the weighted maximum" (Y 65581-65582).

Status of (V) and (Lip): Y 65573-65579 ("Only level-`j` rows move, by `O_L(delta'_j)` including the
reconstructed pivots ... On their full double blocks the regular average and the product of the four
group factors change by `O_L(delta'_j)`"). On the free nonpivots (V) is the definition of the chart
`Ch(omega)` with `C_V = 2` plus the comparison of the centres `S_g, S_X` ((Y-JOIN) of
`library/inset-chart.md`); on the pivots it is (Y-PATH), (Y-MEAN) there. Both are **gaps** here. They do
not touch `I(omega) = 1`.

## 9. The statement, the constants, and the crux

### 9.1 Theorem

**Theorem 9.1 (I3-cert, given (COV)).** Assume:

- (H1) the frame (FR) with the floors (T1), (T2), (T3), and (LF) (or `L_flat < L` with the larger constant
  of 5.3);
- (H2) the geometry (G2), (G3), Definition T, and the tests with the thresholds of the table in 5.2;
- (H3) (AV1), (AV2) in the local form of 2.3;
- (H4) the incoming term is a finite sum of iterated integrals in the sense of Lemma 1, each step being
  the insertion of a finite decomposition of unity, a multiplication by an indicator or a delta, an
  integration against a kernel, a reference-law replacement (m5), or the removal of an indicator that
  equals one on the chart of its removal, which is an identity of measures (Y 77757-77758); Lemma 1' is
  applied summand by summand;
- (H5) `gamma` so small that `C_2'' ebar(gamma) <= alpha_L`, `c_0 C_2'' ebar(gamma) <= min(eps_L, L^2/C_L)`
  and `C_2'' ebar(gamma) <= 1` (the last for the conversion `abs(F) <= c_0 . defect` of 2.3);
- (COV) of 5.4.

Then at every point `x` of the entering support of the final stage at depth `m` (so, by Lemma 1', `|mu_N|`-almost everywhere for the incoming measure, and, in the pointwise reading
of Lemma 1, wherever the incoming term is not zero), with `omega = pi(x)`:

- (ii) every tested holonomy of level `l` of the global prospective datum is within `C_3 e_l` of one;
- (i) every tested holonomy of level `l` of the prospective joined datum of `X` that is not a tower
  holonomy is within `C_3 e_l` of one.

In particular `I(omega) = 1` with this `C_3`, since `e_l <= max_q e_q`.

*Proof.* Lemma 1 puts `x` in `Ent_N`. Corollary 5.2 gives the base bound `C_2'' e_l` for the old datum.
Lemma 4 gives (ii). Lemma 6 gives (i). `square`

### 9.2 Where each constant comes from

| Constant | Definition | Depends on | Source |
|---|---|---|---|
| `C_F(n)` | Lemma F1 | `Bbar, c_5, r, L` | frame |
| `A_L` | (5.1) | `L, c_f, M, M_0` | thresholds of the tests |
| `C_2` | `2^{r+1} L L_flat^2 A_L` | `L, L_flat, r, c_f, M, M_0` | Lemma 2b; one test, one footprint |
| `C_2''` | `max(C_2, 6 . 4^r L^2)` | `C_2, r, L` | Lemma 2b; (K-wall) |
| `C_3` | `2 c_0 L^2 C_F(1) C_2''` | the above and `Bbar, c_5` | Lemma 4; one averaging step from level `j` to `q` |
| `K_w, delta` | (WM) | `K_loc, L, sigma` | cited |
| `K_F` | (6.2) | `delta c_B rho, Bbar, c_5, r, L` | Lemma 3; a convergent series in the level distance |
| `K_G` | section 8 | `Bbar, c_5, r, L` | Lemma 5a |
| `C_5, C_6` | section 8 | the above, `C_M, C_V` | Lemma 5 |

`C_3` does not depend on `m`, on the volume, or on the history: the level enters only through `e_l`, and
`ebar(gamma)` is a supremum over the coupling (Lemma F4). It does depend on the frame constants
`(r, c_5, Bbar)` and, through (K-core) and (K-col), on `M_0` and `c_f`. The row lists
`(L, L_flat, frakM, R_1, M_1, M)`; the frame constants and `M_0, c_f` are to be added. All are fixed
before `gamma` in Y's order (Y 72931). `L_flat` is not in Y's display; it is chosen together with `L`
(Y 63876). `c_f` is not defined in Y; with B6 it is a function of `L`. So the three conditions of (H5) and
the floors (T1)-(T3) are ceilings on `gamma`, satisfiable since `ebar(gamma) -> 0`. `frakM, R_1, M_1` enter only through the geometric facts (G1)-(G3).

**No constant is a product over levels or over entrances.** The chain at one entrance is

`tests --(Lemma 2, 2b)--> C_2'' --(Lemma 4)--> C_3 --(Lemma 3)--> K_w K_F C_3 --(Lemma 5)--> C_5, C_6`,

of fixed length four. At the next entrance the chain starts again at `C_2''`, because Corollary 5.2 takes
its bound from (COV): each tested plaquette is supplied by a test with a threshold written in the
definition of the operation, at the moment that test is carried, and the *value* of the loop is carried
to the present by (c2'). The number `C_3` obtained for a new level-q plaquette at one entrance is not the
input of the next: at the next entrance that plaquette is an old one, and (COV) must supply it from the
retained test of the kind that supplies it (items 3, 4, 5 and 7 of the list in 5.4), which gives `C_2''` again.
This is Y 65586-65591: "take the profile from the actual retained tests at each entrance, as in the
levelwise datum bound. Repeatedly multiplying the adjacent comparison constant would not give a uniform
profile." An induction that used `C_3` of entrance `N` as the base bound of entrance `N + 1` would give
`(2 c_0 L^2 C_F(1))^N C_2''`; no step above does that. The only induction in this note is Lemma 1, on sets,
with no constant.

Within one entrance, the level sums are suprema bounded by convergent series: `K_F` (weights
`e^{-kappa n}` against `C_F(n)`) and `K_G` (weights `L^{-2n}` against `C_F(n)`).

## 10. What stays open

1. **(COV), section 5.4.** The one step of the chain to `I(omega) = 1` that is not proved here. It is the
   lemma that is needed: *at an admitted point, every tested plaquette of the old global datum has a
   supplier of one of the seven kinds (with (K-wall)), with complete footprint (c1), the loop at `x_N`
   equal, up to conjugation, to the loop the supplier bounds (c2'), and the right averages (c3').* Y's lines: 65425-65474, 76654-76689, 78299-78323. Inside `X` at the
   final entrance I checked the assignment against Y's box geometry (list in 5.4) and found one case where
   Y's literal clauses do not cover the footprint (item 5, earlier faces in the default operation; Y
   78316-78319 says so); the repair is the preceding guard at the entrance of the earlier stage, with (c2') (`library/cov-x.md`
   Lemma 6.3; HOLDS in `library/cov-x-check.md`). Outside `X`
   (statement (ii) for the rest of the history) I did not check anything: it needs the definitions of the
   stopped components, islands, drop-outs and restored cores.
2. **No counterexample.** I looked for a point of the entering support with a tested holonomy of the class
   in (i) far from one. The candidates were: a loop at an earlier prepared face (item 5 of 5.4), a
   level-m loop next to the old seam (covered by T4), a core loop (covered by T5). None gives one; for the
   first, the preceding guard at the entrance of the stage of level `i` bounds the same loop
   (`library/cov-x.md` Lemma 6.3).
3. **Inputs read and not rebuilt:** (AV1), (AV2) in local form (2.3); the thresholds of the stage tests
   (5.2); (G1)-(G3) (inside `X`: `library/h-geo.md`, given CORE); the form of the term (Lemma 1, remark 1);
   the trichotomy of the joined datum (Lemma 6); for Lemma 5 only: (V), (Lip), and the conversion between
   `R_mat` and `r_U`.
4. **Definition T** is my reading. Remark 7.3 covers the other reading.

For the owners of other files (I did not edit them):

- `library/inset-chart.md` 5.2: (F1-Y) holds on the larger set `Ent_N` of Definition 4.3, which does not
  impose T6, T8, T11, T12, T13. The certificate can be stated levelwise (`C_3 e_l` at level `l`), which is
  stronger than `C_3 max_q e_q`.
- `library/open-registry.md`, RIM-I3: `C` is `C_3` of 9.2, uniform in `m`, volume and history, with the
  dependence listed there; the status becomes "proved given (COV)"; (COV) is the new open row.
- The row's list of constants for `C_3` omits `(r, c_5, Bbar, M_0, c_f)`.
- Y: `psi_l` is used at Y 65477-65478 and defined nowhere; (LF) `L_flat^2 < L` is used at Y 65481 and is
  not among the conditions on `L_flat` at Y 63876.
