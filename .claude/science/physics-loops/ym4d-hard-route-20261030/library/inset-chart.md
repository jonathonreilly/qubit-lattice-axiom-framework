lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-10T09:56Z

# INSET-CHART: the retained tests of the inset final stage, each on its actual chart

Row 617 of `FINISH.md`. Root R1 (TRIAL) of `library/t0-approach.md`, registry row INSET-CHART. Pinned at commit 228251b79.

Status: in progress (started 2026-11-09 21:56Z). Sections are written as they are finished. The result table of section 0 is written last.

Provenance. One session of Claude Fable 5.2 (high), worker on the Mac mini. No other model checked this file. No numeric job was run. All steps are by reading and by hand. This is research-stage working state. It grants no status.

Credit. The operation, its stages, the inset guard `G = chi_in kappa_x`, the three ways (A), (B), (C) and every estimate cited as "Y n" are from `YM4_1400.tex` by Ethan Sussman and Levent Alpoge (their text names Claude and Codex as authors), commit 2bc0658f91d2. "Y n" is line n of that file. The method (stage tests on localized backgrounds, removal of the old tests on the new support) is Tadeusz Bałaban's, CMP 119 (1988) 243 and CMP 122 (1989) 175. RIM-REG is `library/rim-scale.md` Theorem 6.2 (Claude Fable 5.2; checked by Claude Opus 5.5 in `library/rim-scale-check.md`). H-GEO is `library/h-geo.md` (Claude Fable 5.2; not yet checked).

## 1. Repo search and scope

- `grep -n -i "inset" library/open-core.md library/l17c.md`: no hit. In `FINISH.md` and `QUEUE_DONE.md` the word occurs in rows 523, 609, 614 and 617 only. Row 617 is the only row on INSET-CHART. No other row covers it.
- `grep -l "kappa_x\|chi_in\|inset guard\|inset rule\|inset split" library/*.md library/prior/*.md`: `rim-scale.md`, `rim-scale-check.md`, `open-registry.md`, and two files (`a2-layers.md`, `composite-adjoint.md`) that use `chi_in` for another object. So our library has no earlier work on this statement.
- This checkout has the ref `origin/claude/ym4d-hard-route` only. `origin/main` and the other PR branches are not present here, so I did not search them.
- Read in Y, with their paragraphs: Y 61970-62078, 62255-62324, 63694-64594 (all), 64598-65404 (all), 65406-65700, 65860-65900, 67320-67345, 69500-69605, 71336-71405, 72243-72326, 76653-76697, 76878-76896, 77706-77790, 78286-78340, 13283-13411, 13800-13816, 35634-35672, 134197-134222.
- NOT READ: Y 62326-63693 (the ordinary strip: Jacobian, local strip background, axial frames, retained strip). Y 65700-65860 and 65900-67320 (the complex substitutions and the expansion). Y's proofs of the response and propagator bounds that section 5 cites.
- Not in scope, as the row orders: CORE, (I3), the checks of rows 613 and 615.

## 2. Setting and notation

Level `m`, class component `X`, final stage of the operation of level `m`: `n + 1 = N_m`, `j = m - 1`, `q = m`. Lengths are in bare units. `a_m = M R_m L^m` is the side of a level-m cell (`R_m` is Y's `\check R_m`), `u_m = M L^m`.

**Regions (Y 63760-63765, 63798-63803, 64028-64031, 69574-69579).** `O_m = Omega_m^c cap X` is `X` with two cell layers removed. `Y_m := Z''_m(X)` is the last prepared box, and `Z''_j` the one before. `K := (Omega_m^c minus Y_m) cap X` is the exterior collar. `X_in` is `X` with one full level-m cell layer removed. `E` is the set of bare plaquettes of `X` with a corner outside `X_in`.

**The rule.** I use the direct graded rule (Y 64035-64036, 65155-65159, 65879-65882, 69577-69579). The stage releases the level-j bonds with an endpoint in `K` and neither endpoint in `Omega_m`. Section 7 says what changes under the other rule of Y.

**The variables at the collar integration.** I split a point `x` of the real pre-collar fibre space into two parts.

- `omega`, the fixed part. It holds the prospective datum: the top field `V_m` (on `X cap Omega_m` and outside `X`), the new level-m rows of `K` with their values `V_m(c)`, the held rows of the prepared nest in `Y_m`, and the frozen core. It also holds every other stored variable that the stage does not integrate. The new rows are targets of the averaging deltas, which are still present when the stage is tested (Y 72257-72268).
- `z = (a, B)`, the active part (Y 69529-69537). `B` is the family of the free collar nonpivots. `a` is the family of the strip coordinates `A'_j(b)` on the active slots of the old strip: the level-j stored fluctuation on `X cap Omega_m`, on slots that meet `Omega_m`, have no endpoint in `Lambda_m`, and are not original pivots. The pivots are solved from the deltas at the fixed targets (Y 64910-64958).

`pi(x) = omega` is the projection. The set of `z` over one `omega` is the collar fibre.

**Backgrounds.** `U^+(omega) = U^{(N_m)}_{m,X}` is the prospective background localized in `X`. It depends on `omega` only. `U^-(omega, B) = U^{(N_m - 1)}_{m,X}` is the preceding one; its datum has the level-j rows of `K`. `S_X(omega) = M^j U^+` and `S_g(omega) = M^j U_g^+`, with `U_g^+` the global prospective background (Y 65023-65027). The two collar charts are `V_j = e^{i g_j B_g} S_g = e^{i g_j B_X} S_X` on the free nonpivots (Y 65085-65090).

**Convention D ("defined").** Y counts an undefined tested background as a failure (Y 64484-64486, 62013). Y defines the background as the unique attained minimum on "the prescribed constrained regular set" (Y 13800-13816). I use this form: `U^+(omega)` is defined when a constrained-critical configuration with the prescribed averages and radius `R <= a_0` exists. It is then one orbit, by `bgc:proper-background` (Y 35634-35646). I did not check that the two forms agree outside the supports where that proposition applies. Nothing below uses the convention outside those supports.

**The inset guard (Y 64306-64315, 64482-64486).** `chi_in(omega)`: `U^+` is defined, and the literal final clauses hold on the bare plaquettes with all corners in `X_in`. `kappa_x(omega)`: each deep exterior plaquette astride `dY_m` has `norm(dU^+(p) - 1) < (1 - 3 beta_s/4) F_j eps_j L^{-2j}`, `F_j = L_flat^{2(j - k_0 - 1)}`. `G = chi_in kappa_x`. `r(omega)` is the product of the literal final clauses that `chi_in` omits (Y 64465-64468); it contains the rim clauses on `E`.

**The complete chart.** For a fixed `omega` put

`K(omega) := { (a, B) : norm(V_j(b) S_X(b)^{-1} - 1) < 2 delta'_j on every free nonpivot b; abs(a_b) < rho_b on every active strip slot b }`,

with `rho_b` the least ordinary threshold at `b` (Y 69539-69543). `K_s(omega)` is the subset with `max_b abs(g_j B_g(b)) < delta'_j` (the global sharp ball, Y 65104-65106). Y removes the old indicators on the approximate ball, before the sharp split (Y 77757-77762: "Remove an old indicator only when it equals one on the complete chart used for its removal"; Y 64970-64972: "the full real product ball on which the released nonpivots satisfy the approximate collar bound"). So `K(omega)` is the complete chart of the row.

## 3. The retained tests (step 1 of the row)

I took the list from Y's definition of the stage (Y 63836 item (1), 63864-63876, 77738-77762), from the tests of the stored step that the stage integrates (Y 61973, 62029-62039, 62050, 62078), and from the two lists of Y for the collar integrand (Y 64646-64665, 69529-69553). "Active" means that the test depends on `z`.

| # | Test | Reads (variables) | Lines | Active? |
|---|---|---|---|---|
| T1 | Prospective regularity guard, inset form `chi_in` | `omega`, through `U^+` on `X_in` | Y 64306-64308, 63876, 69544-69546 | no |
| T2 | Prospective crossing test `kappa_x` at `dY_m` | `omega`, through `U^+` on plaquettes astride `dY_m` | Y 64308-64315 | no |
| T3 | Crossing tests of the earlier faces `dZ''_{s+1}`, `s < j`, carried with the coefficient of shell `s` (only in "an operation using these additional tests through the whole window") | `omega`, through `U^+` in `Y_m` | Y 64437-64463 | no |
| T4 | Final top density `chi_m(square)`, bases in `Omega_m^{~4}`; it covers `X cap Omega_m` and reads outside `X` | `omega` (`V_m` only) | Y 62050 (c), 64096-64097, 64657-64658, 64826-64827, 78312-78314 | no |
| T5 | Bottom-core and frozen-core selectors: the level-h density tests, the failed factors and the deltas under the core operation | `omega` (core spectators) | Y 64022-64025, 64643-64644, 64836-64837 | no |
| T6 | Approximate collar test `chi'_j` at `2 delta'_j` against `S_X` | `B`; centre from `omega` | Y 64032-64036, 77741-77743 | yes |
| T7 | Sharp collar ball at `delta'_j` (after the removal) | `B_g` | Y 65104-65106, 65860-65862, 77761-77762 | yes |
| T8 | Ordinary strip indicators on their original masks: completed fluctuation test (`delta_j`), collar test (`delta_j / (4 Theta_1)`), rim test (`theta_c delta_j`), with the signs of the queried outcomes; only passing factors occur on an eligible component | `a` | Y 62035-62039, 64619-64644, 69539-69543 | yes |
| T9 | Preceding regularity guard `P = chi_m^{(N_m - 1)}`: shell clauses, exterior clauses, deep exterior clause, carried crossings | `B` and `omega`, through `U^-` on `X cap Omega_m^c` | Y 63876, 64221-64232 | yes |
| T10 | Lower density tests `chi_j(square)`, bases in `(Omega_j^{~4} minus Omega_m^~) cap X` | `B` and `omega`, through the test-cube background | Y 64699-64716 | yes |
| T11 | Contour indicators of the old exterior belt (the indicators of the gauge factor of step `m`), on the order-m blocks between the first and third layers outside `Omega_m` | `B` | Y 64791-64801, 62050 (a) | yes |
| T12 | The two approximate belt groups ("fifth and sixth"): `chi'_j(square)` at `2 delta_j`, bases in `(Omega_m^{~2} minus Omega_m) cap X` and in `(Omega_m minus Lambda_m^~) cap X` | `B`, `a`; centre from `V_m` | Y 64046-64052, 61973 | yes |
| T13 | Domain convention of the block means: in the soft gauge factor (a factor is 1 where a mean is undefined) and in the regular branch of the averaging rows | `B` | Y 62013, 62015-62027, 64910-64927 | yes |

Not tests, listed so that nothing is left out: the soft gauge density of the collar gauge (a weight; Y 64809-64810, 77764-77777), the Haar and pivot densities (Y 65091-65102), the Gaussian and chart factors, and the averaging deltas (they define the fibre).

Outside the chart of this stage: the old approximate tests that meet the small-field region `Lambda_m`. Y assigns them to the integral of the ordinary step `m` ("The later stage has no independent copy of those variables", Y 64849-64858). They read neither `U^+` nor `G`, so the inset rule does not change them. I do not treat them.

**Comparison with `rim-scale.md`.** That file has no list of tests. Its section 4 lists 13 consumers of the final guard, and its 7.1 states the nesting claim for the earlier guards. The match is: consumers 1 and 2 are the removal of T9 with T2; consumers 3 and 4 are the removal of T12; consumer 5 is T8; consumer 12 is the admission step (5.2 below). Not in `rim-scale.md`: T3, T5, T6, T7, T10, T11, T13. One difference of substance: `rim-scale.md` 4, finding 1, says that nine consumers "use no bound in the outer cell layer". For T12 this needs a qualifier. The sixth group has bases in the second cell layer and its reads can enter the outer cell layer by up to `4 M_2 R_m + 1` level-m units; they stay at distance at least `c M R_m` from `dX` (Y 64053-64059). Its removal reads `S = M^j U^+` there (Y 64068-64081). It uses the existence and the regularity radius of `U^+` and the values `V_m` of its top rows, and no threshold of the guard. Section 5.2 supplies exactly that.

(Sections 4 to 9 follow.)
