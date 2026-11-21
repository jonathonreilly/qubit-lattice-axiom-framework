lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-10T09:56Z

# INSET-CHART: the retained tests of the inset final stage, each on its actual chart

Row 617 of `FINISH.md`. Root R1 (TRIAL) of `library/t0-approach.md`, registry row INSET-CHART. Pinned at commit 228251b79.

Status: finished 2026-11-09 (one session, started 21:56Z). Not checked by another model.

## 0. Result

**Stop condition (i): every retained test has a way. The proof is an implication from named arguments of Y, which I read and did not rebuild.** No test is left without a way. No statement outside Y and our library is needed.

| Step of the row | Verdict |
|---|---|
| (1) List of retained tests | 13 tests, T1 to T13 (section 3), taken from Y's definition of the stage. `rim-scale.md` has no such list; seven of the 13 do not occur there. |
| (2) Way (A) | T1 to T5: the inset guard `chi_in`, the crossing tests, the final top density, the core selectors. Each is a function of the fixed datum `omega` (Proposition 4.1, proved here). |
| (2) Way (B) | T6 to T8: the approximate collar test, the sharp ball, the strip indicators. In the stage coordinates they are one-bond balls, so the overlap estimate holds with multiplicity 1 once the three ordinary indicators at a strip slot are one selector and T6 is dropped on the passing sharp branch (R3-a of `inset-chart-check.md`) (Lemma 4.2 and Proposition 4.3, proved here; the Gaussian tail itself is Y's). |
| (3) Way (C) | T9 to T13: the preceding guard, the lower density tests, the contour indicators, the two belt groups, the domain convention of the means. Each equals one on the complete chart (Theorem 5.6). For the preceding guard the ladder is proved here with explicit constants (Theorem 5.4), given Y's response bounds. For T10 to T13 it is Y's argument, with its hypotheses supplied here. |
| (3) RIM-REG | It is a statement on the complete chart, not only on the support of the literal guard (section 6). Its hypotheses are functions of the fixed datum and do not contain the rim clauses. At a collar stage the rim clause itself is of kind (A), not of kind (C). No fixed-domain form is needed. |
| (4) Moving domains | None remains for the direct graded rule with the global sharp ball (section 7). The incident-bond convention would leave one: the sharp read on the inherited crossings; its tail estimate is open in Y and is not needed here. |

In one sentence: under the inset rule the removal of the old tests needs from the rim only that the localized background exists and is regular there, and that follows from the top density test and the datum certificate at the fixed datum, so it holds on the whole chart.

The two new steps of this note are Lemma 5.1 (an active guard that is implied on the complete chart of each certified datum can be replaced by the certificate, a factor of kind (A)) and Lemma 5.2 with Proposition 5.3 (the admission at the rim is all that the removal arguments read there).

Inputs that stay open (section 9): the certificate on the entering support, which is (I3) plus its global form; H-GEO, which rests on CORE; and six arguments of Y that are read here and not rebuilt, of which the collar path with its response bounds carries the most weight.

Provenance. One session of Claude Fable 5.2 (high), worker on the Mac mini. No other model checked this file. No numeric job was run. All steps are by reading and by hand. This is research-stage working state. It grants no status.

Credit. The operation, its stages, the inset guard `G = chi_in kappa_x`, the three ways (A), (B), (C) and every estimate cited as "Y n" are from `YM4_1400.tex` by Ethan Sussman and Levent Alpoge (their text names Claude and Codex as authors), commit 2bc0658f91d2. "Y n" is line n of that file. The method (stage tests on localized backgrounds, removal of the old tests on the new support) is Tadeusz Bałaban's, CMP 119 (1988) 243 and CMP 122 (1989) 175. RIM-REG is `library/rim-scale.md` Theorem 6.2 (Claude Fable 5.2; checked by Claude Opus 5.5 in `library/rim-scale-check.md`). H-GEO is `library/h-geo.md` (Claude Fable 5.2; not yet checked).

## 1. Repo search and scope

- `grep -n -i "inset" library/open-core.md library/l17c.md`: no hit. In `FINISH.md` and `QUEUE_DONE.md` the word occurs in rows 523, 609, 614 and 617 only. Row 617 is the only row on INSET-CHART. No other row covers it.
- `grep -l "kappa_x\|chi_in\|inset guard\|inset rule\|inset split" library/*.md library/prior/*.md`: `rim-scale.md`, `rim-scale-check.md`, `open-registry.md`, and two files that match the pattern with other objects (`chi_int` in `a2-layers.md`, a weight `kappa_x` in `composite-adjoint.md`). So our library has no earlier work on this statement.
- This checkout has the ref `origin/claude/ym4d-hard-route` only. `origin/main` and the other PR branches are not present here, so I did not search them.
- Read in Y, with their paragraphs: Y 61970-62078, 62255-62324, 63694-64594 (all), 64598-65404 (all), 65406-65700, 65860-65900, 67320-67345, 69500-69605, 71336-71405, 72243-72326, 76653-76697, 76878-76896, 77706-77790, 78286-78340, 13283-13411, 13800-13816, 35634-35672, 134197-134222.
- NOT READ: Y 62326-63693 (the ordinary strip: Jacobian, local strip background, axial frames, retained strip). Y 65700-65860 and 65900-67320 (the complex substitutions and the expansion). Y's proofs of the response and propagator bounds that section 5 cites.
- Not in scope, as the row orders: CORE, (I3), the checks of rows 613 and 615.

## 2. Setting and notation

Level `m`, class component `X`, final stage of the operation of level `m`: `n + 1 = N_m`, `j = m - 1`, `q = m`. Lengths are in bare units. `a_m = M R_m L^m` is the side of a level-m cell (`R_m` is Y's `\check R_m`), `u_m = M L^m`.

**Regions (Y 63760-63765, 63798-63803, 64028-64031, 69576-69579).** `O_m = Omega_m^c cap X` is `X` with two cell layers removed. `Y_m := Z''_m(X)` is the last prepared box, and `Z''_j` the one before. `K := (Omega_m^c minus Y_m) cap X` is the exterior collar. `X_in` is `X` with one full level-m cell layer removed. `E` is the set of bare plaquettes of `X` with a corner outside `X_in`.

**The rule.** I use the direct graded rule (Y 64035-64036, 65155-65159, 65879-65882, 69580-69582). The stage releases the level-j bonds with an endpoint in `K` and neither endpoint in `Omega_m`. Section 7 says what changes under the other rule of Y.

**The variables at the collar integration.** I split a point `x` of the real pre-collar fibre space into two parts.

- `omega`, the fixed part. It holds the prospective datum: the top field `V_m` (on `X cap Omega_m` and outside `X`), the new level-m rows of `K` with their values `V_m(c)`, the held rows of the prepared nest in `Y_m`, and the frozen core. It also holds every other stored variable that the stage does not integrate. The new rows are targets of the averaging deltas, which are still present when the stage is tested (Y 72259-72268).
- `z = (a, B)`, the active part (Y 69527-69534). `B` is the family of the free collar nonpivots. `a` is the family of the strip coordinates `A'_j(b)` on the active slots of the old strip: the level-j stored fluctuation on `X cap Omega_m`, on slots that meet `Omega_m`, have no endpoint in `Lambda_m`, and are not original pivots. The pivots are solved from the deltas at the fixed targets (Y 64910-64958).

`pi(x) = omega` is the projection. The set of `z` over one `omega` is the collar fibre.

**Backgrounds.** `U^+(omega) = U^{(N_m)}_{m,X}` is the prospective background localized in `X`. It depends on `omega` only. `U^-(omega, B) = U^{(N_m - 1)}_{m,X}` is the preceding one; its datum has the level-j rows of `K`. `S_X(omega) = M^j U^+` and `S_g(omega) = M^j U_g^+`, with `U_g^+` the global prospective background (Y 65023-65027). The two collar charts are `V_j = e^{i g_j B_g} S_g = e^{i g_j B_X} S_X` on the free nonpivots (Y 65085-65090).

**Convention D ("defined").** Y counts an undefined tested background as a failure (Y 64484-64486, 62013). Y defines the background as the unique attained minimum on "the prescribed constrained regular set" (Y 13800-13816). I use this form: `U^+(omega)` is defined when a constrained-critical configuration with the prescribed averages and radius `R <= a_0` exists. It is then one orbit, by `bgc:proper-background` (Y 35634-35646). I did not check that the two forms agree outside the supports where that proposition applies. Nothing below uses the convention outside those supports.

**The inset guard (Y 64306-64315, 64482-64486).** `chi_in(omega)`: `U^+` is defined, and the literal final clauses hold on the bare plaquettes with all corners in `X_in`. `kappa_x(omega)`: each deep exterior plaquette astride `dY_m` has `norm(dU^+(p) - 1) < (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j - k_0 - 1)}`. `G = chi_in kappa_x`. `r(omega)` is the product of the literal final clauses that `chi_in` omits (Y 64465-64468); it contains the rim clauses on `E`.

**The complete chart.** For a fixed `omega` put

`Ch(omega) := { (a, B) : norm(V_j(b) S_X(b)^{-1} - 1) < 2 delta'_j on every free nonpivot b; abs(g_j a_b) < rho_b on every active strip slot b }`,

with `rho_b` the least ordinary threshold at `b` (Y 69538-69540). `Ch_s(omega)` is the subset with `max_b abs(g_j B_g(b)) < delta'_j` (the global sharp ball, Y 65104-65106). Y removes the old indicators on the approximate ball, before the sharp split (Y 77759-77761: "Remove an old indicator only when it equals one on the complete chart used for its removal"; Y 64970-64972: "the full real product ball on which the released nonpivots satisfy the approximate collar bound"). So `Ch(omega)` is the complete chart of the row. (`K` alone always means the exterior collar.)

## 3. The retained tests (step 1 of the row)

I took the list from Y's definition of the stage (Y 63836 item (1), 63864-63876, 77741-77763), from the tests of the stored step that the stage integrates (Y 61973, 62029-62039, 62050, 62078), and from the two lists of Y for the collar integrand (Y 64646-64665, 69527-69549). "Active" means that the test depends on `z`.

| # | Test | Reads (variables) | Lines | Active? |
|---|---|---|---|---|
| T1 | Prospective regularity guard, inset form `chi_in` | `omega`, through `U^+` on `X_in` | Y 64306-64308, 63876, 69544-69546 | no |
| T2 | Prospective crossing test `kappa_x` at `dY_m` | `omega`, through `U^+` on plaquettes astride `dY_m` | Y 64308-64315 | no |
| T3 | Crossing tests of the earlier faces `dZ''_{s+1}`, `s < j`, carried with the coefficient of shell `s` (only in "an operation using these additional tests through the whole window") | `omega`, through `U^+` in `Y_m` | Y 64437-64463 | no |
| T4 | Final top density `chi_m(square)`, bases in `Omega_m^{~4}`; it covers `X cap Omega_m` and reads outside `X` | `omega` (`V_m` only) | Y 62050 (c), 64096-64097, 64657-64658, 64826-64827, 78312-78314 | no |
| T5 | Bottom-core and frozen-core selectors: the level-h density tests, the failed factors and the deltas under the core operation | `omega` (core spectators) | Y 64022-64025, 64643-64644, 64836-64837 | no |
| T6 | Approximate collar test `chi'_j` at `2 delta'_j` against `S_X` | `B`; centre from `omega` | Y 64032-64036, 77744-77746 | yes |
| T7 | Sharp collar ball at `delta'_j` (after the removal) | `B_g` | Y 65104-65106, 65868-65870, 77762-77763 | yes |
| T8 | Ordinary strip indicators on their original masks: fluctuation test (`delta_j`), which the stage completes on the strip, collar test (`delta_j / (4 Theta_1)`), rim test (`theta_c delta_j`), with the signs of the queried outcomes; only passing factors occur on an eligible component | `a` | Y 62035-62039, 64619-64644, 69536-69540, 77746-77747 | yes |
| T9 | Preceding regularity guard `P = chi_m^{(N_m - 1)}`: shell clauses, exterior clauses, deep exterior clause, carried crossings | `B` and `omega`, through `U^-` on `X cap Omega_m^c` | Y 63876, 64221-64232 | yes |
| T10 | Lower density tests `chi_j(square)`, bases in `(Omega_j^{~4} minus Omega_m^~) cap X` | `B` and `omega`, through the test-cube background | Y 64699-64716 | yes |
| T11 | Contour indicators of the old exterior belt (the indicators of the gauge factor of step `m`), on the order-m blocks between the first and third layers outside `Omega_m` | `B` | Y 64791-64801, 62050 (a) | yes |
| T12 | The two approximate belt groups ("fifth and sixth"): `chi'_j(square)` at `2 delta_j`, bases in `(Omega_m^{~2} minus Omega_m) cap X` and in `(Omega_m minus Lambda_m^~) cap X` | `B`, `a`; centre from `V_m` | Y 64046-64052, 61973 | yes |
| T13 | Domain convention of the block means: in the soft gauge factor (a factor is 1 where a mean is undefined) and in the regular branch of the averaging rows | `B` | Y 62013, 62015-62027, 64910-64927 | yes |

Not tests, listed so that nothing is left out: the soft gauge density of the collar gauge (a weight; Y 64809-64810, 77767-77780), the Haar and pivot densities (Y 65091-65102), the Gaussian and chart factors, and the averaging deltas (they define the fibre).

Outside the chart of this stage: the old approximate tests that meet the small-field region `Lambda_m`. Y assigns them to the integral of the ordinary step `m` ("The later stage has no independent copy of those variables", Y 64849-64858). They read neither `U^+` nor `G`, so the inset rule does not change them. I do not treat them.

**Comparison with `rim-scale.md`.** That file has no list of tests. Its section 4 lists 13 consumers of the final guard, and its 7.1 states the nesting claim for the earlier guards. The match is: consumers 1 and 2 are the removal of T9 with T2; consumers 3 and 4 are the removal of T12; consumer 5 is T8; consumer 12 is the admission step (5.2 below). Not in `rim-scale.md`: T3, T5, T6, T7, T10, T11, T13. One difference of substance: `rim-scale.md` 4, finding 1, says that nine consumers "use no bound in the outer cell layer". For T12 this needs a qualifier. The sixth group has bases in the second cell layer and its reads can enter the outer cell layer by up to `4 M_2 R_m + 1` level-m units; they stay at distance at least `c M R_m` from `dX` (Y 64053-64059). Its removal reads `S = M^j U^+` there (Y 64068-64081). It uses the existence and the regularity radius of `U^+` and the values `V_m` of its top rows, and no threshold of the guard. Section 5.2 supplies exactly that.

## 4. Ways (A) and (B) (step 2 of the row)

### 4.1 Way (A): T1 to T5

**Proposition 4.1.** T1, T2, T3, T4 and T5 are functions of `omega`. So they are constant on each collar fibre.

*Proof.* T1 to T3 read plaquette norms of `U^+`. A residual gauge conjugates a plaquette, so these norms are functions of the orbit, and the orbit is a function of the prospective datum. I list the rows of the prospective no-inward determining set of `X` (members as in `h-geo.md` section 2 with `j + 1 = m`: the level-m member is `X minus Y_m`, the level-j layer is the shell `Y_m minus Z''_j`).

1. Rows of level below `j`, and level-j rows with both ends in `Y_m`. They are held: "the internal fine links on the prepared side are held" (Y 69603-69606). They are in `omega`.
2. Level-j bonds that cross `dY_m`. They have an end in the level-m member, so they are inward rows and are absent from the set (Y 64874-64876).
3. Level-m rows with both blocks in `K`, and outward level-m rows from `K` into the shell. Their values are the targets `V_m(c)` of the averaging deltas. The deltas are present when the stage is tested (Y 72259-72260), and the pivots are solved "keeping `W` fixed" (Y 64960-64961). They are in `omega`.
4. Level-m rows in `X cap Omega_m`, and the tower rows at `dX`, which are the face lift of `V_m` (Y 135200-135209). They are in `omega`.

The collar gauge is pinned at the level-m sites, "so the coarse row remains fixed", and the guard is covariant under it (Y 77767-77774). So the value of T1 to T3 is the same before and after the gauge draw. T4 reads `V_m` on the halo of its cube. T5 reads the frozen core: the halos reach less than `a_{h+1}` and the gap to the first prepared face is at least `3 a_{h+1}` (Y 64022-64025), so no read of T5 meets `K`. `square`

This agrees with Y 69544-69546: "The prospective regularity guard depends on the fixed datum and remains outside the collar logarithm. This includes the prospective crossing tests wherever they are used." It also covers the rim clauses `r`: they read `U^+` and are functions of `omega`. Section 6 uses this.

### 4.2 Way (B): T6, T7, T8

**Lemma 4.2 (selectors; Y 64520-64548, with the proof written out).** Let `z = (z_b)` be real coordinate blocks. Let `I_alpha`, `alpha in A`, be indicators, and `S_alpha` finite sets of blocks, such that `I_alpha(z) = 1` whenever `abs(z_b) < h` for every `b in S_alpha`. Suppose each block lies in at most `nu` of the sets `S_alpha`. Then

`prod_{alpha in A} (1 - I_alpha) <= sum_{(b_alpha)} prod_{b in {b_alpha : alpha in A}} 1{abs(z_b) >= h}`,

the sum over all choices `b_alpha in S_alpha`. It has `prod_alpha abs(S_alpha)` terms, and in each term the set `{b_alpha}` has at least `abs(A)/nu` elements.

*Proof.* If `I_alpha(z) = 0`, some `b in S_alpha` has `abs(z_b) >= h`. So `1 - I_alpha <= sum_{b in S_alpha} 1{abs(z_b) >= h}`. Multiply over `alpha` and expand the product of sums. In one term the indicator of a block that is chosen several times occurs several times; an indicator is idempotent, so the term is the product over the distinct blocks. The map `alpha -> b_alpha` takes each value at most `nu` times, because a block lies in at most `nu` sets. So it has at least `abs(A)/nu` values. `square`

Y then applies "the stage Gaussian tilt once per distinct bond" and gets the tail `(prod abs(S_alpha)) e^{-c h^2 abs(A)/nu}` (Y 64542-64548). That tail is Y's estimate, on "a stage chart with the real-contour Gaussian bound". I cite it and did not rebuild it.

**Proposition 4.3.** In the coordinates `(a, B_g)` the tests T7 and T8 are products of one-bond balls. T6 is a product of one-bond factors with centres fixed on the fibre. In detail:

1. T7 is `prod_b 1{abs(g_j B_g(b)) < delta'_j}` over the free nonpivots.
2. T8 is `prod_b 1{abs(g_j a_b) < rho_b}` over the active strip slots, with `a_b` in field units and `g_j a_b` Y's angular coordinate `a'` (Y 72106), with `rho_b >= min(theta_c, 1/(4 Theta_1)) delta_j`.
3. T6 is `prod_b 1{norm(e^{i g_j B_g(b)} C_b(omega) - 1) < 2 delta'_j}` with `C_b = S_g(b) S_X(b)^{-1}`. If `norm(C_b - 1) <= delta'_j / 8`, the factor at `b` is 1 on `abs(g_j B_g(b)) < delta'_j`.

So Lemma 4.2 holds for them with `S_alpha = {b}` and with every `h` such that `g_j h <= delta'_j` on a free nonpivot and `g_j h <= rho_b` on a strip slot. The multiplicity is `nu = 1` after two merges (R3-a of `inset-chart-check.md`). (i) The three ordinary indicators at one strip slot are one selector, their conjunction (Y 69538-69540). (ii) T6 and T7 read the same bond `b`; if both are kept as failure selectors (before the sharp split), then `nu = 2` and the tail has `c h^2 abs(A)/2` in place of `c h^2 abs(A)`. On the passing sharp branch T6 is identically one (Y 65869-65870), and then `nu = 1`. No domain depends on `omega`, on a source or on a complex parameter.

*Proof.* (1) is the definition (Y 65104-65106). (2): the stored strip variable is the coordinate `A'` after the ordinary substitution, and under the strip bound `abs(H_b) <= delta_j/8` (Y 62301-62302, 64681-64682) a hard test with threshold at most `29 delta_j / 24` is the same function of the new variable as of the old one (Y 62298-62315, 64681-64685). The strip bound holds at weak coupling: the centre shift is at most `C_L eps_j e^{-c R_q}` (Y 63937-63939), and `delta_j/eps_j = A_1/A_0` is fixed (Y 62068). The three thresholds are `delta_j`, `delta_j/(4 Theta_1)` and `theta_c delta_j` (Y 62035-62039), all at most `delta_j`. The conjunction at one slot is the ball with the least threshold (Y 69538-69540). "The inherited Schur complement and the retained rim and collar indicators are evaluated in the original variables of the strip" (Y 65402-65404). (3): `V_j S_X^{-1} = e^{i g_j B_g} S_g S_X^{-1}` (Y 65069-65073), and `C_b` depends on `omega` only. For a Hermitian traceless 2 by 2 matrix `theta` with Y's norm (Y 4700-4705), `norm(e^{i theta} - 1) = 2 sin(abs(theta)/2) <= abs(theta)`. Also `e^{i theta} C - 1 = (e^{i theta} - 1) C + (C - 1)` with `C` unitary. So on the ball `norm(e^{i g_j B_g} C_b - 1) <= delta'_j + delta'_j/8 < 2 delta'_j`. `square`

Y states (3) as its example of way (B) (Y 64513-64519) and the bound `abs(H) <= delta'_j / 8` at Y 65139-65141. The centre bound is the joined comparison; section 5.3 gives its hypotheses.

For the direct graded rule, on the passing sharp branch and with the merges (i), (ii) above, the overlap estimate of the row is therefore the case `nu = 1` of Lemma 4.2. The count of Y 64557-64569 (a bond lies in a bounded number of enlarged test cubes) is needed only when a cube test is kept as one selector with many slots. No test of that kind remains after section 5.

## 5. Way (C): the active guards T9 to T13 (step 3 of the row)

### 5.1 The fibre lemma

**Lemma 5.1.** Let `pi : X_0 -> Omega_0` be a map of sets and `K_0` a subset of `X_0`. Let `P : X_0 -> {0,1}`, `I, A : Omega_0 -> {0,1}`, and let `Q` be a complex function on `X_0`. Assume

- (F1) `P(x) Q(x) != 0` implies `I(pi(x)) = 1`;
- (F2) `A(pi(x)) I(pi(x)) = 1` and `x in K_0` imply `P(x) = 1`.

Then `P(x) Q(x) = I(pi(x)) Q(x)` for every `x in K_0` with `A(pi(x)) = 1`.

*Proof.* If `I(pi(x)) = 1`, then `P(x) = 1` by (F2), and both sides are `Q(x)`. If `I(pi(x)) = 0`, then `P(x) Q(x) = 0` by (F1), and both sides are 0. `square`

Use. `P` is the product of the active guards. `Q` is the product of the kept factors, tests and weights. `A` is the product of the kept fixed-datum tests. `I` is a certificate: a fixed-datum indicator that holds on the entering support. (F2) is "the guard equals one on the complete chart". The lemma then replaces the active guard by a factor of kind (A). It needs (F2) only at the `omega` that carry the certificate. Y uses the same device at the main step: "Carry these bounds as a support condition on the prepared datum ... The pushforward therefore assigns full mass to the set where this indicator is one. Insert the indicator in the retained kernel" (Y 78331-78339).

### 5.2 Admission on the kept support

**The certificate `I(omega)`.** Fix a constant `C_3`. `I(omega) = 1` when both hold:

- (i) each tested holonomy of the prospective joined datum of `X` that is not a tower holonomy and has no corner in a carried top density cube is within `C_3 max_q e_q` of one, `e_q = R_q^2 eps_q` (Y 65408-65410);
- (ii) each tested holonomy of the global prospective datum is within `C_3 max_q e_q` of one.

`I` is a function of `omega`, given by finitely many inequalities on holonomies.

**Input (F1-Y).** `I(pi(x)) = 1` at every point `x` of the entering support, that is, where the incoming term is not zero: the preceding guard and the other tests of the term are 1 there. This is Y's: "use the promoted datum bounds on the entering support. These bounds, `C e_q` in each layer `q`, use the actual promoted averages before their delta functions are integrated" (Y 134201-134205); the derivation is Y 64088-64102 for `X` and Y 65417-65563 for the global datum. For `X` it is (I3) of `rim-scale.md`. It is not in the scope of this row. I did not rebuild it.

**Lemma 5.2 (admission; this is the place of RIM-REG).** Assume H-GEO for the prospective joined set. Put `eps_bar := max(2.1 eps_m, C_3 max_q e_q)` and assume `eps_bar <= a_1`. Let `omega` have `T4(omega) = 1` and `I(omega) = 1`. Then `U^+(omega)` is defined. It satisfies `R(U^+) <= C_B eps_bar` on the whole joined set of `X`, in layer units, tower and `E` included. It is the only critical orbit with `R <= a_0`. The hypotheses contain neither `r`, nor `G`, nor `z`.

*Proof.* A tested holonomy of the joined datum is of one of three kinds (Y 134207-134210, 72270-72281). A tower holonomy is one or a top plaquette of `V_m` (fact (R1) of `rim-scale.md`). A top plaquette with a corner in a carried density cube has defect at most `2.1 eps_m`, by T4 and (I4) of `rim-scale.md` with the constant of its check (Y 134113-134120). The top plaquettes of `X cap Omega_m` are of this kind, because the cubes with bases in `Omega_m^{~4}` cover the outer six cells of `X` (Y 76692-76697). The other holonomies are bounded by (i). So the datum is `eps_bar`-regular, and `bgc:proper-background` (Y 35634-35646) gives the three claims. `square`

This is the first half of `rim-scale.md` Theorem 6.2, stated for every `omega` of the kept support. Y asserts the same: "The regular orbit for the localized set in force therefore exists before the prospective guard is applied" (Y 134215-134216).

### 5.3 The inputs from Y, with their hypotheses on `omega`

I read each of these arguments in Y. I did not rebuild them. For each I checked which facts about `omega` it uses.

**(Y-PATH)** `hi:real-finer-collar-path`, Y 64860-65017. Hypotheses: the preceding and the prospective joined sets have the geometry of the background theorem (H-GEO at stages `N_m - 1` and `N_m`; the theorem of `h-geo.md` is stated for every stage, given CORE); `U^+(omega)` exists and its radius is below "the fixed small regularity ceiling of the background theorem, with room for constants depending on `L`" (Y 64868-64869); weak coupling. Conclusion, for every `B` with `norm(V_j S_X^{-1} - 1) < 2 delta'_j` on the free nonpivots: each pivot has one value in the regular chart; the old datum lies in the real continuation polydisc about the datum induced by `U^+`; the regular old orbit `U^-(omega, B)` exists; and for a bare plaquette `p` read by the preceding guard,

- (E1) `abs( norm(dU^-(p) - 1) - norm(dU^+(p) - 1) ) <= C_L delta'_j L^{-2j}` on the level-j carriers of `X cap Omega_m^c` outside the old shells (Y 65010-65014);
- (E2) the same difference is at most `C_L (delta'_j / eps_j)(1 + sqrt(j - i)) e^{-kappa (j - i)} eps_i L^{-2i}` on the shell `i < j`, with `kappa = c M/M_1` (Y 64239-64245);
- (E3) it is at most `C_L delta'_j L^{-2s} e^{-kappa (j - s - 1)}` at a carried crossing of `dZ''_{s+1}`, `s < j` (Y 64451-64455).

Y states: "This constructs the old datum without using the preceding guard on that ball" (Y 64976-64977). The argument uses the bound on the radius of `U^+` and no clause of the guard.

**(Y-JOIN)** The comparison with the real joined background, Y 13283-13396 (`mb:real-collar-datum`, `mb:real-collar-norm`), used at Y 65019-65067. Hypotheses: the global prospective datum has all test holonomies within `eps_1 <= a_1` of one (part (ii) of `I`), and the geometry floors. Conclusion: the localized orbit is the regular orbit of the joined datum, and the difference of the two backgrounds at `x` is at most `C_mu eps_1 e^{-delta_0 d(x, W^c)/2}` in the normalized norm. On the collar read set the weighted distance to the joining collar is at least `c M R_m`, so `sup_b norm(S_g S_X^{-1} - 1) <= C eps_* e^{-c M R_m} = o(delta'_j)` (Y 65054-65067).

**(Y-DENS)** Y 64699-64789, the lower density tests at `q > k_0 + 1`. It uses: the exterior clauses of `chi_in` on plaquettes in the halo, which "lies in the top inset of `X`" (Y 64707-64708); a translation with the Hölder bound of the local regularity of `U^+`; (E1); the joined comparison on the density box.

**(Y-CONT)** Y 64791-64810, the contour indicators. It uses the approximate collar ball and the regular branch of the mean contours. The blocks "lie entirely in the collar".

**(Y-BELT)** Y 64027-64211, the two belt groups. It uses: T4 for the datum of the test cube; `norm(S (V^{bg}_{j,square'})^{-1} - 1) <= C eps_* e^{-c M_2 R_m}` from the joined comparison on the test-cube box; the annulus comparison of the ordinary centre with `S^-`; `norm(S^- S^{-1} - 1) <= C(L) delta'_j` from the path; T6 on the collar bonds; T8 on the strip slots. Y says of the first comparison: "It does not require the discarded sharp bound at the artificial bare rim of `X`" (Y 64085-64086).

**(Y-MEAN)** Y 64929-64953 and 64802-64807: on the approximate ball every block mean and every double-block average of the collar is on its regular branch.

**Proposition 5.3 (what the inputs read on `E`).** In the arguments (Y-PATH), (Y-JOIN), (Y-DENS), (Y-CONT), (Y-BELT), (Y-MEAN), as written at the lines cited, the localized backgrounds `U^+` and `U^-` enter on the outer cell layer of `X` in two ways only: (1) through their existence as regular critical orbits with radius below a fixed ceiling; (2) through the values of their top rows, which are `V_m`. No threshold of the literal final guard on a plaquette of `E` is used. Every clause of the prospective guard that is used reads a plaquette with all corners in `X cap Omega_m^c`, or astride `dY_m`, and so is a clause of `chi_in`, `kappa_x` or T3.

*Evidence.* This is a statement about the text of Y, so its proof is a reading. (Y-PATH): hypotheses at Y 64863-64869; reads at Y 64894-64908 and 64991-64996, all in `K` and at the prepared face. (Y-JOIN): hypotheses at Y 13284-13293. (Y-DENS): Y 64707-64708. (Y-CONT): Y 64794. (Y-BELT): the reads stay at distance at least `c M R_m` from `dX` (Y 64057-64059); they can enter the outer cell layer, and there the argument uses (1) and (2) (Y 64068-64086). The guards: "every earlier guard reads only `X cap Omega_m^c`" (Y 64229-64231). I read Y 63884-65404 in full for this. It is one reading, by the model that wrote this note.

### 5.4 The preceding guard T9

Thresholds (Y 63876, 64234-64261, 64306-64313, 64437-64446). Put `c(i, J) := 1 - beta_s (1 - 2^{-(J - i + 1)})` and `F_i := L_flat^{2 (i - k_0 - 1)_+}`. The final stage is compressed: `k_0 <= m - 2`, so `j >= k_0 + 1`.

| Case | Plaquette `p` read by the preceding guard | Preceding threshold `T^-(p)` | Clause of the inset guard, threshold `T^+(p)` |
|---|---|---|---|
| (a) | wholly in a shell `i < j` | `c(i, j) F_i eps_i L^{-2i}` | shell clause of `chi_in`: `c(i, m) F_i eps_i L^{-2i}` |
| (b) | wholly in the new shell `Y_m minus Z''_j` | deep exterior: `(1 - beta_s/2) F_j eps_j L^{-2j}` | shell clause of `chi_in`: `(1 - 3 beta_s/4) F_j eps_j L^{-2j}` |
| (c) | wholly outside `Y_m`: in the deep exterior, or in `Omega_l minus Omega_{l+1}`, `k_0 < l <= j` | `(1 - beta_s/2) c_l L_flat^{2e} eps_j L^{-2j}` | exterior clause of `chi_in`, with `T^+ <= (eps_m/eps_j) max{L_flat^2, 3} L^{-2} T^-` |
| (d) | astride `dY_m` (then wholly in `Omega_{k_0+1}^c minus Z''_j`) | deep exterior: `(1 - beta_s/2) F_j eps_j L^{-2j}` | `kappa_x`: `(1 - 3 beta_s/4) F_j eps_j L^{-2j}` |
| (e) | a carried crossing of `dZ''_{s+1}`, `s < j` | `c(s, j) F_s eps_s L^{-2s}` | T3: `c(s, m) F_s eps_s L^{-2s}` |

The cases are all the reads. A clause of the preceding guard requires containment in a shell, in the deep exterior or in one original layer (Y 64277-64279), or it is a carried crossing. A plaquette of the deep exterior of stage `j` is inside `Y_m`, outside `Y_m` or astride `dY_m`; `Y_m` lies in `Omega_{k_0+1}^c cap X` (Y 63816-63817). In case (c) the exponent `e` rises by one from stage `j` to stage `m`, except at `l = j`, where `e = 0` at both stages and `c_l` rises from 1 to 3. This gives the ratio of Y 64255-64261. Each `p` lies in `X cap Omega_m^c`, two cells inside `X` (Y 64229-64231), so each clause in the last column reads a plaquette with all corners in `X_in`: it is a clause of `G` (with T3).

**Theorem 5.4 (T9 equals one on the complete chart).** Assume (Y-PATH) and

- (L1) `kappa >= ln 2 + 1/2`;
- (L2) `20 C_L max(1, C_f) delta'_j <= beta_s eps_j`, where `eps_j / eps_s <= C_f (1 + sqrt(j - s))` for `s <= j` (Y 63876, 64456-64458);
- (L3) `eps_m <= (3/2) eps_j`, `L >= 4`, `L_flat < L/2`, `0 < beta_s < 1/4`.

Let `omega` have `G(omega) = 1`, T3 equal to 1 if it is used, and `U^+(omega)` regular as (Y-PATH) requires. Then `P(omega, B) = 1` for every `B` in the approximate ball.

*Proof.* By (Y-PATH) the tested orbit `U^-(omega, B)` is defined. Fix a read `p`. `G(omega) = 1` gives `norm(dU^+(p) - 1) < T^+(p)`. Let `E(p)` be the bound of (E1) to (E3). It is enough to show `E(p) <= T^-(p) - T^+(p)`; then `norm(dU^-(p) - 1) <= norm(dU^+(p) - 1) + E(p) < T^-(p)`.

Two elementary facts. For real `n >= 0`: `e^{n/2} >= 1 + n/2` and `sqrt(n) <= (1 + n)/2`, so `(1 + sqrt(n)) e^{-n/2} <= (3 + n)/(2 + n) <= 3/2`. By (L1), `2 e^{-kappa} <= e^{-1/2}`.

(a) `n := j - i >= 1`. `T^- - T^+ = beta_s (2^{-(n+1)} - 2^{-(n+2)}) F_i eps_i L^{-2i} = beta_s 2^{-(n+2)} F_i eps_i L^{-2i}`, and `F_i >= 1`. By (E2), `E(p) 2^{n+2} / (eps_i L^{-2i}) <= 4 C_L (delta'_j/eps_j)(1 + sqrt(n)) (2 e^{-kappa})^n <= 6 C_L delta'_j/eps_j <= beta_s`.

(e) `n := j - s >= 1`. The reserve is `beta_s 2^{-(n+2)} F_s eps_s L^{-2s}`, and `eps_s >= eps_j / (C_f (1 + sqrt(n)))`. By (E3), `E(p) 2^{n+2} / (eps_s L^{-2s}) <= 8 C_L C_f (delta'_j/eps_j)(1 + sqrt(n)) (2 e^{-kappa})^{n-1} <= 8 e^{1/2} (3/2) C_L C_f delta'_j/eps_j < 20 C_L C_f delta'_j/eps_j <= beta_s`, since `e^{1/2} < 1.65`.

(b), (d) The reserve is `(beta_s/4) F_j eps_j L^{-2j}`. By (E1), `E(p) <= C_L delta'_j L^{-2j} <= (beta_s/20) eps_j L^{-2j}`.

(c) By (L3), `T^+ <= theta T^-` with `theta = (3/2) max{L_flat^2, 3}/L^2 <= 3/8`. `T^- >= (1 - beta_s/2) eps_j L^{-2j} >= (7/8) eps_j L^{-2j}`. So `T^- - T^+ >= (35/64) eps_j L^{-2j}`, and `E(p) <= (beta_s/20) eps_j L^{-2j} < (1/80) eps_j L^{-2j}`. `square`

The proof uses `G` and no clause of `r`. Y states the result in pieces: "On the passing branch the fixed-target response estimate below fits that reserve throughout the admitted real collar box, so the preceding seam test is one there" (Y 64326-64329); "All these reads remain in the inset" (Y 64268).

### 5.5 The other active guards

**Proposition 5.5.** Let `omega` have `G = 1`, `T4 = 1`, `I = 1`, and let `z in Ch(omega)`. Under the hypotheses of the inputs: T10 is 1 by (Y-DENS); T11 is 1 by (Y-CONT); T12 is 1 by (Y-BELT); T13 is 1 by (Y-MEAN). If `z in Ch_s(omega)`, T6 is 1 by (Y-JOIN) and Proposition 4.3 (3).

This is an implication from the five inputs. The step added here is Lemma 5.2 with Proposition 5.3: at each such `omega` the inputs have their hypotheses, whether or not `r(omega) = 1`.

### 5.6 The statement INSET-CHART

**Theorem 5.6.** Assume H-GEO, the inputs (F1-Y), (Y-PATH), (Y-JOIN), (Y-DENS), (Y-CONT), (Y-BELT), (Y-MEAN), the conditions (L1) to (L3), and weak coupling as in section 8. Let `x = (omega, z)` be a point of the real pre-collar fibre space with `T1 T2 T3 T4 T5 (omega) = 1` and `z in Ch(omega)`. Let `Q` be the product of the kept factors of the term at `x`. Then

`[T9 T10 T11 T12 T13](x) Q(x) = I(omega) Q(x)`.

So on the branch `G = 1` each retained test has a way:

- T1 to T5, and the certificate `I`: way (A). They stand outside the collar logarithm.
- T6, T7, T8: way (B). They are fixed one-bond balls (T6: one-bond factors that accept the sharp ball). After the sharp split the passing branch has T7 and T8 only.
- T9 to T13: way (C), first property. Each equals one on the complete chart `Ch(omega)` over every `omega` with `G T4 I = 1`.

*Proof.* Lemma 5.1 with `P = T9 T10 T11 T12 T13`, `A = T1 T2 T3 T4 T5`, `K_0 = {(omega, z) : z in Ch(omega)}`. (F1) is (F1-Y). For (F2): let `A(omega) I(omega) = 1`. Lemma 5.2 gives the admission of `U^+(omega)` with radius `C_B eps_bar`, below the ceilings by section 8. Part (ii) of `I` gives the hypothesis of (Y-JOIN). Then Theorem 5.4 gives T9, and Proposition 5.5 gives T10 to T13. `square`

The identity is between functions on the fibre space. It holds for every incoming measure, positive or complex, and for a sourced bare measure, because the tests are those of the unsourced run (Y 64491-64495). The factor `I(omega)` is kept: it is a factor of kind (A), outside the collar logarithm, and it replaces `P` (R4 of `inset-chart-check.md`). It may not be dropped after the integration: the integrated kernel at `omega` is `I(omega) int Q dz`, and at an `omega` with `I(omega) = 0` the integral `int Q dz` need not vanish. `I` may be dropped only on a set where the outgoing `omega`-measure is already known to vanish when `I = 0`; that is the content of (F1), and it is applied before the integration.

## 6. The rim clause and RIM-REG (the decision asked in step 3 of the row)

**Decision.** RIM-REG is a statement on the complete chart. It is not "a bound only on the support of the literal prospective guard". The fixed-domain form is not needed.

Reasons, in order.

1. *The rim clause is not a test of kind (C).* Y's sentence (Y 64580-64585) is about "a preceding curvature guard on the active collar": a test whose argument moves with `z`. The rim clauses read `U^+`, and `U^+` depends on `omega` only (Proposition 4.1). The final stage is the last collar stage, so the final guard is never the preceding guard of a later collar integration of this operation. The earlier guards have no rim clause: "The artificial bare rim occurs only in the final guard" (Y 64229-64232). So no rim clause is ever an active guard of a collar integration. The literal product `r(omega)` and the layer-unit clause `chi_E(omega)` of `rim-scale.md` 6.1 are both of kind (A).
2. *What the inset rule needs at the rim is admission, not a threshold.* By Proposition 5.3 the removal arguments use, on the outer cell layer, the existence of `U^+` as a regular orbit and the values of its top rows. Under the literal rule the factor `r` could supply the regularity there. Under the inset rule `r` is absent, and this is the gap that Y 64583-64585 names: an estimate proved on `{chi_in r = 1}` says nothing on the sector `{chi_in kappa_x (1 - r) = 1}`.
3. *RIM-REG supplies the admission on the whole kept support.* The hypotheses of `rim-scale.md` Theorem 6.2 at an evaluation `(omega, z)` are (a) the carried top density tests, which are T4, and (b) the interior bound, which is part (i) of the certificate `I`. Both are functions of `omega`. Neither contains `r`. So the conclusion holds at every point of `Ch(omega)`, for every `omega` with `T4 I = 1`, also when `r(omega) = 0`. That is Lemma 5.2. The stronger half of RIM-REG (curvature at most `2 K_w eps_m L^{-2 lambda(p)}` on `E`, so `chi_E = 1`) holds on the same set under the further hypotheses of the second half of `rim-scale.md` Theorem 6.2, which Lemma 5.2 does not contain (R5 of `inset-chart-check.md`): `C_B eps_bar <= a_c` (the profile, (I2)), `eps_bar e^{-delta d} <= eps_m/2` with `d` the weighted distance from `E` to `X cap Omega_m^c`, and repairs R-a, R-b of `rim-scale-check.md`. The two coupling conditions are in section 8 item 5; they hold at weak coupling, since `d >= c M R_m` (Y 77947-77949) and `eps_* e^{-c delta_c M R_m} = o(eps_m)` (Y 71386-71391).
4. *The sector where the two rules differ is not empty.* Y's own example (Y 72340-72428) is a field with `r = 0`. Y says of it that the earlier stage tests pass and that "The inset estimate applies on the inset" (Y 72415-72418, 72428). `rim-scale.md` 5.2 gives a second such field. So a proof on the literal support alone would leave a real sector open, and item 3 is needed.
5. *Fixed-domain form.* If a consumer wants a rim test as an explicit factor, `chi_E(omega)` is one. It does not depend on `z`, so it is trivially in fixed-domain form and accepts every ball. It equals one where `G T4 I = 1`, so it can be inserted or left out. The literal `r(omega)` is also of kind (A), but it is not one on that set (item 4), so it cannot be inserted without changing the rule.

6. *The main step.* After the last stage the final guard is the preceding guard of the central integration. Its background then depends on the box variables. Under the literal rule the rim clauses would be active guards there, and item 4 shows that the other tests do not imply them. Under the inset rule no rim clause enters the main step. The admission at the rim is again a statement about the datum: the tower datum is still the lift of `V_m`, and Y bounds the prepared datum on the main-step ball (Y 71349-71381). I did not write that step (section 9, item 8).

Consequence for the tested background. On the support of the incoming term, `T4 = 1` and `I = 1`. So `U^+` is defined there, and the convention "an undefined tested background is a failure" (Y 64484-64486) is never used on that support. The failure branch `G = 0` on the support consists of threshold failures of `chi_in`, `kappa_x` (and T3) only.

## 7. Moving domains (step 4 of the row)

**Result.** With the direct graded rule, the global sharp ball and the inset guard, no moving domain remains.

After Theorem 5.6 the integrand of the passing branch has the form of Y 69553-69564, `int 1_E(a, B) F(P, y; a, B) d mu(a, B)`, with `1_E = T7 T8`. By Proposition 4.3 the set `E` is a product of fixed balls in `(a, B_g)`. It depends neither on `omega`, nor on the source, nor on the shift `y`, nor on the complex potential and current coordinates. The factors of kind (A) are real functions of `omega`. The tests use the frozen frame and the unsourced run (Y 64491-64495, 69547-69549). The chart `Ch(omega)` of the removal is centred at `S_X(omega)`; it moves with the real datum, which is not an analytic parameter.

Y has two variants that do create a transported domain. Neither is needed for Theorem 5.6.

1. *The local sharp guard written in the global chart.* The ball `abs(g_j B_X) < delta'_j` is the set `abs(log(e^{i g_j B_g} e^{iH})) < delta'_j` in the chart `B_g`. If the shift `H` is then replaced by the free source `y`, the domain moves with `y`. Y's rule avoids this: use `B_X` as the variable of the fixed ball and the actual shift in the analytic factors (Y 65875-65877), or use the global sharp ball with source zero (Y 65868-65874). To compare the two rules one must treat the two disagreement sectors (Y 65119-65127). An operation that uses one rule from its first formation has no such comparison.
2. *The incident-bond convention.* The sharp mask then also reads the inherited bonds that cross the old `Omega_m` wall. The test is `abs(log((V_j S_o^{-1})(S_o S_g^{-1}))) < delta'_j`, with `V_j` read in the inherited chart. "There is no new integration coordinate for that bond" (Y 65167-65168). Y's way to keep this read (Y 65193-65218) is to re-centre the inherited coordinate at `S_g` by a right translation. The read is then a fixed ball, and the conditional density changes. This needs three things. (i) The centre bound `abs(log(S_g S_o^{-1})) + delta'_j < rho_b` on the complete crossing stencils; then the ordinary factors at `b` are one on the ball. (ii) The ordinary centre is fixed on the joint fibre. (iii) Analytic bounds of the new density on the strip discs. Y derives (i) at order `O_L(delta'_j)`, which fits because `rho_b` is a fixed fraction of `delta_j` (Y 65220-65224 inside `Omega_m`; Y 65231-65341 at the old-wall crossings). Y leaves (ii) and (iii) as checks (Y 65212-65216, 65342-65345). So for this convention the transported integral and its bound are open. I did not attempt them. The direct graded rule does not have this read: "The inherited crossing coordinates remain in the ordinary strip integral with their completed tests" (Y 65879-65882).

Not checked: whether a later estimate of Y needs the sharp bound `delta'_j` on the old-wall crossings, which only the incident-bond convention gives. The belt comparison does not need it (Y 64184-64198).

## 8. Order of constants

1. The geometry: `L` (odd, at least 13), `L_flat` with `2 <= L_flat` and `L_flat^2 < L` (R10-a of `inset-chart-check.md`; Y uses `L_flat^2 < L` at Y 65481 and states only `2 <= L_flat < L/2` at Y 63876; for `L >= 4` it implies `L_flat < L/2`, so (L3) holds; example `L = 13`, `L_flat in {2, 3}`), `delta_0` (fixed together with `L`, Y 62001), `frakM`, `R_1`, `rho`, `M_1`, `M_2` (after `delta_0`, R10-b: Y requires `c delta_0 M_2 >= 1`, Y 62001). Then `beta_s` in `(0, 1/4)`.
2. From the geometry: `a_0`, `a_1`, `C_B` of `bgc:proper-background`; the regularity ceiling `e_0` of (Y-PATH); `C_mu` of (Y-JOIN) (its `delta_0` is fixed in step 1, R10-b); the rate constant `c` and `C_L` of (E1) to (E3); `C_f`.
3. `M`, with `M >= L^4 M_1` (H-GEO), `M >= L^2 M_2` (Y 62001, R10-b) and `c M / M_1 >= ln 2 + 1/2` (L1). Y chooses `M/M_1` at this place (Y 64248-64249).
4. `C_3`, the constant of the certificate, from (F1-Y).
5. The coupling ceiling. For couplings below it: `eps_bar <= a_1`; `C_B eps_bar <= min(a_0, e_0)`; (L2); `eps_m <= (3/2) eps_j`; `C eps_* e^{-c M R_m} <= delta'_j / 8`; for the stronger half of RIM-REG (section 6 item 3, R5): `C_B eps_bar <= a_c` and `eps_bar e^{-delta d} <= eps_m/2`.

None of these depends on `m`, on the number of steps or on the torus, if the inputs are uniform as Y states.

## 9. What stays open, and the next step

Open or unchecked, in the order of what each could break.

1. **The six inputs of section 5.3** are Y's arguments. I read them and did not rebuild them. (Y-PATH) carries the most weight: Theorem 5.4 rests on (E1) to (E3). It cites the real Landau response with decay in the metric of the preceding joined sequence.
2. **(F1-Y)**: the certificate holds on the entering support. Part (i) is (I3) of `rim-scale.md`, registry row RIM-SCALE. Part (ii) is Y 65417-65563. Not in scope here.
3. **H-GEO** rests on CORE (rows 615, 616).
4. **Convention D.** I did not compare the definition of "defined" at Y 13800-13816 with the form used here, outside the supports.
5. **T3.** Y's formula `G = chi_in kappa_x` names the new crossing only. If the operation carries the earlier crossings through the window (Y 64437-64463), the guard of Theorem 5.6 is `chi_in kappa_x` times T3. This is Y's own convention, not a new guard.
6. **Proposition 5.3** is a reading of Y 63884-65404. A second reader should repeat it.
7. **Earlier stages.** The same proof applies to a transition `j -> j + 1` with `j + 1 < m`: there is no rim, and the level-`(j+1)` density test is the fixed-datum factor (Y 64812-64821). The first face and the uncompressed stages have their own arguments in Y (Y 64367-64463, 64718-64737). I did not write these cases.
8. **The main step.** After the last stage, `G` is a preceding guard for the central integration, whose variables are the prepared field `V''` in the box. Y treats this at Y 63876 ("the final regularity threshold follows on its inset") and Y 71336-71405 (the crossing factor). Under the inset rule no rim clause enters that step. Not proved here.
9. **The old approximate tests that meet `Lambda_m`** (Y 64849-64858): Y leaves their bookkeeping to the ordinary step. The inset rule does not change them.
10. **The incident-bond convention** (section 7, item 2).

Not addressed, by scope: the payment of the branch `G = 0` (root R5), and ownership over ages.

Next steps, for the lead to decide.

- One line-by-line check of this note by Opus 5.5, with a second reading of Y 63884-65404 for Proposition 5.3 and the table of 5.4.
- A proof item for (F1-Y) part (i), which is (I3). It is now the shared input of RIM-REG and of INSET-CHART.
- A check or rebuild of (Y-PATH). I found no note of our library on `hi:real-finer-collar-path`.
- Form to adopt: the operation with `G` from its first formation, the direct graded rule, the global sharp ball. Then the final stage has the same structure as each earlier stage: the guard reads the inset only, and the regularity at `dX` comes from the datum (Lemma 5.2).
