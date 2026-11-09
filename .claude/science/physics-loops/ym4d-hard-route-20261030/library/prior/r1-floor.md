# R1 floor reading

Reading by Codex (GPT-6), 2026-11-09, from checkout `be2f77f424e25d189cee1fe10390af6fd4af94dc`; reading and mapping only, not a proof or audit. Source: Ethan Sussman and Levent Alpoge, `YM4_1400.tex`, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`; its text credits Claude and Codex as authors. I credit Sussman and Alpoge, with Claude and Codex, for the source wording used here. `Y n` is line n of that file.

## Repo search

The lead's `library/prior/repo-search-2026-11-08.md` records a search of `origin/main` and open YM4D PRs #10114, #10133, #10134 and #10141 (the later FINISH rule also lists #10144). The digest has no entry for the R1 floor or a close parameter-floor result. Its `rim-scale` and `h-geo` mentions concern other work. I checked the current checkout's `library/open-registry.md`: `R1-FLOOR` is its own open row 999; `rim-scale` (rows 609 and 613) and `h-geo` (row 614) are dependencies/context, not coverage of this reading. I read the named nearby `rim-scale.md` statements and the relevant `rim-scale-check.md` section: they identify the needed `R_1 >= 42 L` change at the chart admission, and do not answer the all-Y parameter scan. The lead's remote-branch scan is recorded, but no additional PR path was named in the task or digest for me to open. Thus none of the found work supplies this line-by-line answer.

Source files fetched once as instructed: `/tmp/ym4_1400.tex` (136,637 lines), `/tmp/sa_ym4.tex` (32,992 lines), and `/tmp/sa_ca_I.tex` (166,711 lines). I used the SA outline index README, relevant neighboring entries in chunks 09–11, the obligations index, and the CA-I 4.12–4.19 index. The outline index is for the different `YM4_sketch_500.tex` version. Its nearby entries describe the analogous R1/M1 definitions and parameter order (SA 9599, 9658, 9916), but do not settle the Y-version question below. The CA-I index search did not supply a closer statement for this parameter floor. No proof step or computer-assisted evidence is used.

## 1. Every matching Y line

Search: `R_1`, `M_1`, `M_1'`, `M_1^\prime`. Each line below is a separate source line. “Use” entries say how increasing the geometric parameter acts where that meaning is established. Reused symbols from other chapters are identified as such rather than silently identified with the floor parameters.

| Y line | Short quotation | Class; effect of increasing the parameter |
|---:|---|---|
| 638 | “Fix powers … `frakM,M_1',M`” | definition; these are chosen auxiliary powers |
| 639 | “`rho=R_1 frakM`” | definition; larger geometric `R_1` widens the gap |
| 651 | “`R_1 >= L`, `M_1' >= R_1 frakM`” | lower bound; increasing `R_1` raises the required `M_1'` floor |
| 652 | “`M >= L^4 M_1'`” | lower bound; raising `M_1'` raises the required `M` floor |
| 660 | “distance … `> R_1 frakM L^q`” | use in tower rule; larger gap erodes more, so the retained region is smaller |
| 662 | “cube of side `M_1' L^{q+1}`” | use in tower rule; larger `M_1'` makes the admitted cubes larger |
| 664 | “distance … `>= M_1' L^{q+1}`” | use in tower rule; larger `M_1'` raises the inclusion clearance |
| 3662 | “union of `M_1`-cubes … `C M_1 L^j eta_k`” | use in geometry; larger cube/gap scale changes both cell size and spacing requirement |
| 3970 | “`M_1`, `M alpha_0` … satisfy hypotheses” | other (hypotheses delegated to cited lemma); larger sizes can make the smallness premise harder |
| 4391 | “`M_1` be large … `M alpha_0` … below a number” | use in estimate; increasing `M_1` may worsen the smallness condition, while `M` must be chosen to keep `M alpha_0` small |
| 4400 | “`c_1,B_1` may depend on `L,frakM,R_1`” | use in estimate; larger `R_1` may enlarge constants / tighten `alpha_0+alpha_1 <= c_1` |
| 8594 | “gauges on `O(M_1 xi)` cubes” | use in domain size; larger `M_1` enlarges the required gauge region |
| 13449 | “localization … `M_1 L^i`-cubes” | use in geometry; larger `M_1` enlarges localization units |
| 13450 | “intersect the sequence with the `M_1`-tower” | use in geometry; larger `M_1` coarsens tower cubes |
| 14938 | “fix powers `frakM,R_1,rho`” | definition |
| 14941 | “`R_1 >= L`, `R_1 frakM >= L^2 rho`” | lower bounds; increasing `R_1` helps the second inequality when `rho` is held fixed |
| 14946 | “gap … `R_1 frakM xi_j`” | use in geometry; larger `R_1` increases separation |
| 16102 | “cube size … `M_1`, gap number `R_1` … `R_1 >= L`” | definition plus lower bound |
| 16105 | “distance … `> R_1 M_1 xi_j`” | use in geometry; larger `R_1` increases separation |
| 16126 | “cube of side `O(M_1 xi_j)` … real gauge” | use in estimate; larger `M_1` enlarges the cube on which the gauge bound is required |
| 16173 | “`R_1 >= L`” | lower bound |
| 16174 | “`R_1 frakM` at least the floor” | lower bound; larger `R_1` helps |
| 16244 | “cells of side `O(M_1 xi_j)`” | use in geometry; larger `M_1` enlarges walk cells |
| 16250 | “`R_1` denotes a number … not a region `R_t`” | definition / disambiguation |
| 16278 | “torus … multiple of `R_1 M_1`” | lower bound on torus size; increasing either requires a larger torus |
| 16341 | “ceiling … fixed before `M_1` and independent of `M_1`” | other (independence condition); no estimate loss from increasing `M_1` under this clause |
| 16349 | “`M_1` is larger and ceiling … smaller” | other (comparison of two settings); the larger cube setting is paired with a smaller radius ceiling |
| 16355 | “`(C M_1^{-1/2})^{|omega|} M_1^{-|omega|/2}`” | use in estimate; larger `M_1` improves the displayed decay |
| 16371 | “translation in `M_1 xi_k Z^4`” | use in definition of shift; larger `M_1` coarsens allowed shifts |
| 16399 | “preserve the `M_1`-cubes” | use in symmetry condition; larger cubes strengthen the preservation condition |
| 16432 | “gap … exceeds `R_1 M_1`” | use in estimate; larger gap improves the distance lower bound |
| 16439 | “`e^{-c tau R_1 M_1}` … outweighs … `L^4`” | use in estimate; larger `R_1 M_1` improves exponential decay |
| 16463 | “each commutator costs `M_1^{-1}`” | use in estimate; larger `M_1` improves this factor |
| 16970 | “Let … be an `M_1`-cube” | definition/use; larger `M_1` enlarges the local cube |
| 16974 | “`O(M_1^{-1} e^{-c delta M_1/L})`” | use in estimate; larger `M_1` improves both decay factors |
| 16979 | “`O(gamma_0 M_1^{-1} e^{-cM_1/L})`” | use in estimate; larger `M_1` improves the bound |
| 16981 | “`|1-z| <= C M_1^{-1}`” | use in estimate; larger `M_1` improves the bound |
| 16989 | “factor `M_1^{-|omega|/2}` in reserve” | use in estimate; larger `M_1` improves the reserve |
| 17238 | “`rho=R_1 frakM`” | definition/use; larger `R_1` enlarges separation in the subsequent ratio |
| 17399 | “thresholds … on `M_1` and on `R_1 M_1`” | lower-bound choices; increasing either meets or strengthens the flat floors |
| 17434 | “Put `frakM=M_1`” | fixed value (identification in this subsection) |
| 23075 | “`M_1` is” | other (continuation of a separate chapter's definition; see table note below) |
| 23486 | “`M_1 xi_j`” | use in geometry; size scales with `M_1` |
| 23571 | “or `M_1`” | other (symbol in local notation) |
| 26726 | “`R_1-R_2`” | other; operator difference, not geometric gap constant |
| 26764 | “`mathcal M_1-mathcal M_2`” | other; calligraphic operators, not `M_1` cube size |
| 26785 | “compressions of `mathcal M_1^{-1}`” | other; calligraphic operator |
| 28191 | “`R_1-R_2`” | other; operator difference, not geometric gap constant |
| 35698 | “`R_1 frakM eta > L^2 eta`” | lower-bound consequence; larger geometric `R_1` helps fit the stencil |
| 35843 | “Write `M_1=M_1'` in this subsection” | fixed value (identification for this subsection) |
| 35850 | “`R_1 >= L`, `M_1 >= R_1 frakM`” | lower bounds; raising `R_1` requires raising `M_1` |
| 35851 | “`M >= L^4 M_1`” | lower bound; raising `M_1` requires raising `M` |
| 35876 | “`R_1 frakM L^q + frakM L^{q+1}`” | use in tower rule; larger `R_1` increases the first-rule erosion |
| 35877 | “`2 M_1 L^{q+1}`” | use in tower rule; larger `M_1` increases the second-rule clearance |
| 35892 | “than `R_1 frakM L^{q-1}`” | lower-bound comparison; larger `R_1` improves the gap |
| 35893 | “torus side … `M/L >= L^3 R_1 frakM`” | lower bound; raising `R_1` requires a larger torus, supplied by the raised `M` floor |
| 35912 | “`R_1 frakM L^{q-1-n}`” | use in distance estimate; larger `R_1` improves separation |
| 36714 | “`rho=R_1 frakM`” | definition/use; larger `R_1` enlarges separation |
| 36755 | “`rho=R_1 frakM`” | definition/use; larger `R_1` enlarges separation |
| 37082 | “`M_1 >= rho` and `M >= L^3 M_1`” | lower bounds; increasing `R_1` raises `rho`, and the `M_1` floor tracks it; `M` must track `M_1` |
| 37106 | “`2 M_1 sum xi_r < 3 M_1 xi_p`” | use in estimate; both sides scale with `M_1`, so the comparison is unchanged |
| 37112 | “`(2M/L-2)xi_p > 3M_1 xi_p`” | use in estimate; increasing `M_1` worsens RHS, while raising `M` improves LHS |
| 37464 | “at most `C_L M_1 xi_q`” | use in estimate; larger `M_1` worsens the halo size |
| 37466 | “within `C_L M_1 xi_p`” | use in estimate; larger `M_1` worsens the distance allowance |
| 37470 | “increasing … halo from `3M_1`” | use in estimate; larger `M_1` enlarges the halo |
| 37471 | “`C_cut M_1`” | use in estimate; larger `M_1` enlarges the carrier bound |
| 37473 | “`D+C_cut M_1`” | use in estimate; larger `M_1` worsens the bound unless `D` or the later constant changes |
| 37487 | “increase `K_cl`” | use in estimate; larger `M_1` raises the absorbed cut-halo loss |
| 37489 | “`(C_cut-3)_+ M_1 <= D/2`” | upper relation on the halo to `D`; raising `M_1` requires raising `D` |
| 49958 | “`R_1>=L`, `M_1>=R_1 frakM`” | lower bounds; larger `R_1` raises `M_1` |
| 49959 | “`M>=L^4M_1`” | lower bound; larger `M_1` raises `M` |
| 49962 | “`rho=L^-2 R_1 frakM >= r^s`” | lower bound; larger `R_1` helps |
| 49965 | “`R_1 frakM >= max(...)`” | lower bound; larger `R_1` helps |
| 49968 | “`delta_0,red R_1 frakM >= ...`” | lower bound; larger `R_1` improves the product |
| 49969 | “`delta_0,b R_1 frakM >= ...`” | lower bound; larger `R_1` improves the product |
| 49970 | “`delta_* R_1 frakM >= ...`” | lower bound; larger `R_1` improves the product |
| 50211 | “`(R_2-R_1)K_1`” | other; `R_1,R_2` are operator/path parameters, not this gap constant |
| 62437 | “`M_1`-cubes … ambient layers” | use in geometry; larger `M_1` coarsens layers and may affect fit |
| 63174 | “four `M_1`-layers” | use in geometry; layer count fixed, physical thickness grows with `M_1` |
| 63184 | “collar width `M_1`” | use in geometry; larger `M_1` widens collar |
| 63199 | “exceeds `3 M_1 L^t`” | use in estimate; larger `M_1` raises the required clearance |
| 63509 | “`M_1` in their local units” | use in geometry; scale grows with `M_1` |
| 63873 | “`e^{-c(M/M_1)(j-i)}`” | use in estimate; larger `M/M_1` improves decay; scaling both together leaves ratio unchanged |
| 63876 | “For `M` large, the decay … dominates” | lower-bound choice on `M/M_1`; a raised `M_1` needs a correspondingly raised `M` |
| 64111 | “grid of `M_1`-cubes” | use in geometry; larger `M_1` coarsens grid |
| 64243 | “`e^{-c(M/M_1)(j-i)}`” | use in estimate; larger ratio improves decay |
| 64248 | “Choose `M/M_1` so their product is …” | lower-bound choice on ratio; it must absorb the stated shell-growth factors |
| 64454 | “`e^{-c(M/M_1)(j-s-1)}`” | use in estimate; larger ratio improves decay |
| 67830 | “`R_1(hat s)=(I-S)R_0`” | other; indexed matrix function, not geometric gap |
| 67835 | “`Gamma_W=B_W R_1`” | other; matrix factor, not geometric gap |
| 67838 | “`R_1 R_1^T=(D')^-1`” | other; matrix identity |
| 67879 | “`B_W R_1` uses independent noise slots” | other; matrix factor |
| 67908 | “`F=B_W R_1`” | other; matrix factor |
| 67914 | “identity for `R_1`” | other; matrix factor |
| 68513 | “`M >= L^3 M_1`” | lower bound; larger `M_1` requires larger `M` |
| 68516 | “`M_1` is the cube size” | definition |
| 68670 | “`D+3M_1`” | use in geometry; larger `M_1` raises clearance |
| 68675 | “within `C_cut M_1`” | use in estimate; larger `M_1` enlarges read allowance |
| 68681 | “`(C_cut-3)_+M_1 <= D/2`” | upper relation; increasing `M_1` requires increasing `D` |
| 71847 | “Use the separated `M_1`-tower” | use in geometry; larger `M_1` coarsens tower |
| 71858 | “`2M_1 L^t`” | use in estimate; larger `M_1` worsens the distance allowance |
| 71861 | “`2M_1 L^t+L^{t-1}<w`” | upper fit condition; increasing `M_1` requires more room `w` |
| 72930 | “`(M_1,R_1) ... M_1' ... M`” | definition/order of choices; see sections 2–3 |
| 72938 | “rates … before cube sizes … floors … `M`” | lower-bound/order condition; later `M` can take the size loss |
| 72939 | “`M_1` depends on `L` alone; `R_1` depends on `L,M_1`” | definition/order; these symbols are chosen in that order |
| 73300 | “`C(L,varrho_0)M_1 eps_w <= a_D/4`” | use in smallness estimate; larger `M_1` tightens the required `eps_w` |
| 75725 | “`M_2=L^2 M_1`” | fixed value; increasing `M_1` raises `M_2` |
| 77756 | “`e^{-c(M/M_1)(j-l)}`” | use in estimate; larger ratio improves decay |
| 84033 | “`<= R_1 g_j^kappa0`” | use in estimate; this `R_1` is a bound constant in a different chapter |
| 84042 | “not the geometrical gap parameter” | other (explicit disambiguation) |
| 84258 | “walk cell … `O(M_1 xi_n)`” | use in geometry; larger `M_1` enlarges walk cell |
| 84259 | “enlargement by `5M_1 xi_n`” | use in geometry; larger `M_1` enlarges read halo |
| 84261 | “`C M_1 xi_n* < w`” | upper fit condition; increasing `M_1` requires a larger assigned cell side `w` |
| 84277 | “`(C M_1^-1/2)^|omega|`” | use in estimate; larger `M_1` improves the entropy margin |
| 97350 | “`f_j=ceil(M_1(...)/(M checkR_j))`” | use in estimate; increasing `M_1` raises collar count, increasing `M` lowers it |
| 97362 | “`C M_1 sum ...`” | use in estimate; larger `M_1` worsens width bound unless `M` or other terms absorb it |
| 97431 | “remove their … `4M_1`-neighbourhoods” | use in geometry; larger `M_1` enlarges removed neighborhoods |
| 97432 | “union of `M_1`-cubes” | definition/use; larger `M_1` coarsens region |
| 97433 | “`4M_1` inner rim” | use in geometry; larger `M_1` widens rim |
| 97436 | “`10M_1 < M checkR_j`” | upper fit condition; increasing `M_1` requires increasing `M checkR_j` |
| 97440 | “`f_j M checkR_j - 5M_1 >= ...`” | use in estimate; larger `M_1` worsens the subtractive margin |
| 107517 | “`eta_12 M_1 M_2`” | use in estimate; larger cube sizes increase this term |
| 109666 | “`M` link logarithms … `|a|<=R_1`” | use in estimate; this `R_1` is a local coordinate radius, not the geometric gap |
| 109667 | “`gR_1<=1/4` … `C M g^2 R_1^2`” | upper bound / use in estimate; increasing this local radius worsens the bound and must respect `gR_1<=1/4` |
| 109697 | “uniform third-derivative bound” | use in estimate; local coordinate range controls derivative bound |
| 109698 | “`K_S(y)<=C M R_1^3`” | use in estimate; larger local radius worsens the bound cubically |
| 109789 | “`alpha<=C M g R_1^3 + C M g^2 R_1^2`” | use in estimate; larger local radius worsens the error budget |
| 109804 | “`R_1<=C(log x)^B`” | upper bound; applies to the distinct local-coordinate radius in this later argument, not the geometric gap parameter |
| 128495 | “`w=M/M_1`” | definition; a larger ratio improves the separate localization parameter `w` |
| 128790 | “halo … `3L M_1`” | use in geometry; larger `M_1` enlarges halo |
| 128796 | “`3s_n<=3L M_1`” | use in estimate; larger `M_1` worsens the upper scale allowance |
| 131755 | “`M_1-M_0=...`” | other; indexed matrix sequence, not cube size |
| 131926 | “`L M_1 xi_n` in `Y`” | use in geometry; larger `M_1` enlarges region |
| 132201 | “`M_1`-cubes” | use in geometry; larger `M_1` coarsens tower |
| 132204 | “clearance `>R_1 s/L`” | use in estimate; larger geometric `R_1` increases clearance |
| 132205 | “`1+floor((R_1+k)/L)`” | use in estimate; larger `R_1` increases the number of erosion steps |
| 132222 | “In the `M_1` tower take `n>=3`” | use in geometry; threshold count is fixed, physical tower size grows with `M_1` |
| 132258 | “`M>=L^4M_1`, `M_1>=R_1 frakM`” | lower bounds; larger `R_1` propagates to `M_1` then `M` |
| 132408 | “`r_t + L M_1 + r_in`” | use in estimate; larger `M_1` increases the required width |

The search also matched `R_1` in operator/matrix names at Y 26726, 28191, 50211, 67830–67914, and 131755's `M_1-M_0`; these are not the geometric constants. Y 84042 explicitly says its `R_1` is not the geometric gap. Y 109804's upper bound belongs to that later local-coordinate radius family. Neither supplies an upper bound on the geometric gap chosen at Y 638/651. No exact value is imposed on the geometric `R_1`, `M_1'` or `M` in the floor passages; Y does impose the local identity `M_1=M_1'` at 35843 and `frakM=M_1` at 17434 for their named subsections.

## 2. Where a larger geometric `R_1` costs something

The geometric gap enters the estimates in two ways. The separation and exponential estimates improve with `R_1`; the costs are the dependency of `c_1,B_1` in Y 4400 and the larger `M_1'`/`M` floors in Y 651–652 and 35850–35851.

**Potential loss in Y 4400.** Y states: “fix the block and gap numbers `frakM,R_1`. The constants `c_1,B_1>0` may depend on `L,frakM,R_1`, but are independent of depth and compatible volume.” It then assumes “`alpha_0+alpha_1 <= c_1`.” Thus a larger `R_1` may worsen the smallness threshold through `c_1(L,frakM,R_1)` (or the size of `B_1`). In this proposition the constants are allowed to be set after the gap is fixed. **My reading:** this is a potential loss, not a stated monotonicity claim about `c_1` or `B_1`.

Y also has an order statement at 17399: “First comes `L` … [including] the … ceiling on `alpha_0,alpha_1,gamma_0`. Next come `M_1` and `R_1 M_1`; the ceiling does not depend on them, and they do not depend on the ceiling.” It later says the ordinary constants, rates and ceilings are independent of `M_1,R_1` once large enough. **NOT DECIDED:** whether the `c_1` in Y 4400 is the same ceiling as the one fixed independently of `R_1` at Y 17399. If they are the same, the two clauses need reconciliation; I do not identify them without a source statement. This leaves the response of the Y 4400 smallness condition to `R_1=L^3` undecided.

**Loss passed to larger sizes.** Y 638–652 says: “Fix powers … `frakM,M_1',M`, a gap `rho=R_1 frakM` … They are part of the auxiliary data, selected before domains or norms are formed”; then “`R_1>=L`, `M_1'>=R_1 frakM` and `M>=L^4 M_1'`.” Y 35843–35855 says: “Write `M_1=M_1'` in this subsection”; after listing the same floors it states: “The background floors are imposed before these inequalities. The localization size `M` is then increased, if necessary; no constant chosen below depends on the cutoff, the tower depth or a coupling.” Thus a larger gap has an explicit later size outlet: raise `M_1'` and then `M`; the specified order chooses these sizes after the background floors. It does not itself say a fixed `M` remains adequate.

At Y 14938–14946, the separate geometry paragraph says “fix powers `frakM,R_1,rho` … with `R_1>=L`, `R_1 frakM>=L^2 rho`”; it also calls `frakM,rho` fixed floors depending on `L`. This is not an upper bound on `R_1`. Increasing `R_1` helps the displayed comparison if `rho` is held fixed. Y 16095–16110 says the geometric `M_1,R_1` are powers of `L`, `R_1>=L`, with separation `>R_1 M_1 xi_j`; no upper floor appears there.

The order statements requested, with the closely related later order included:

- **Y 620–660:** “Fix powers … `frakM,M_1',M`, a gap `rho=R_1 frakM` … selected before domains or norms are formed.” “Take `L>=13` odd, `R_1>=L`, `M_1'>=R_1 frakM` and `M>=L^4M_1'`.” This fixes the auxiliary data before domains; it does not state that `R_1` is fixed to a particular value.
- **Y 14920–14950:** “fix powers `frakM,R_1,rho` of `L` with … `R_1>=L`, `R_1 frakM>=L^2 rho` … The fixed floors … depend on `L`.” This gives simultaneous conditions, not a strict order among those three values.
- **Y 16095–16110:** “The integer `L` is odd and large. The cube size … `M_1`, and the gap number, `R_1`, are both powers of `L`, with `R_1>=L`.” “A sequence … is called separated when … distance … `>R_1M_1 xi_j`.” No upper bound or selection order is stated in this passage.
- **Y 35840–35855:** “Write `M_1=M_1'` in this subsection.” “The constants satisfy `L>=13`, `R_1>=L`, `M_1>=R_1 frakM`, `M>=L^4M_1`.” “The background floors are imposed before these inequalities. The localization size `M` is then increased, if necessary.” Thus `M` is expressly available after `R_1` and `M_1`.
- **Y 17399:** “First comes `L` … the lower thresholds that the flat case imposes on `M_1` and on `R_1M_1` … and the ceiling on `alpha_0,alpha_1,gamma_0`. Next come `M_1` and `R_1M_1`; the ceiling does not depend on them … The final choices are `M` and the field strengths …” This order is why the possible `c_1` conflict above remains open.
- **Y 72930–72939:** the displayed order is `(… ) prec L prec (M_1,R_1) prec kappa prec (bar-kappa,kappa_1) prec M_1' prec M_2 prec (…) prec M`. It says “rates are chosen before the cube sizes `M_1',M_2,M`” and “`M_1` depends on `L` alone, and `R_1` depends on `L` and `M_1`.” In this later construction, `M_1` and `R_1` are selected before `M_1'` and `M`; `M` is last. It supplies no upper bound on the geometric gap. Whether every symbol in this later list is the same size choice as in Y 638 is **NOT DECIDED** by the lines quoted.

Other geometric `R_1` uses do not create an adverse estimate: Y 35698 uses `R_1 frakM eta > L^2 eta` to fit a stencil; Y 16432–16439 uses the gap to get distance `>= R_1M_1(|j-j'|-1)_+` and decay `e^{-c tau R_1M_1}`; Y 49962–49970 uses positive lower products of `R_1 frakM`. Increasing the gap strengthens these stated bounds. No small-coupling condition depending adversely on the geometric `R_1` was found in the matched parameter lines.

## 3. Upper bounds, fixed values, and independence clauses

For the geometric floor family introduced at Y 638, the explicit relations are lower bounds: `R_1>=L`, `M_1'>=R_1 frakM`, `M>=L^4M_1'` (Y 651–652). In the aliasing subsection, Y 35850–35851 repeats them with `M_1=M_1'`. Y 49958–49970 and 132258 repeat related lower bounds. I found no upper bound on this geometric `R_1`, on `M_1'`, or on the localization cube `M`, and no fixed numerical value for any of those three in that hierarchy.

Two nearby size-fit conditions must be kept distinct from a global ceiling: Y 71861 requires a read distance `2M_1L^t+L^{t-1}<w`; Y 84261 requires `C M_1 xi_{n*}<w_{l(Omega_0)}`; Y 97436 requires `10M_1<M checkR_j`. These bound the cube scale relative to the locally assigned room, and can be met only if that room/`M` is large enough. Y 54165–54167 also defines a separate `M=M(m)` as the smallest power of `L` with `16R_c<=M<16LR_c`; this is a local scale choice, not stated to be the localization cube `M` of Y 638. Y 109804 bounds the separate finite-window count `M` as part of `N+M+m+|W|<=C(log x)^A`. They are genuine bounds on their local `M` symbols, not an upper bound on the floor-family localization cube. They do not place an absolute upper bound on that global floor parameter by themselves. In Y 35843, the local `M_1` is expressly identified with `M_1'`; whether each later `M_1` in the other chapters is that same choice is **NOT DECIDED** solely by these lines.

Independence/dependence quotations:

- **Y 4400:** `c_1,B_1` “may depend on `L,frakM,R_1`, but are independent of depth and compatible volume.” These are not independent of `R_1` by stipulation.
- **Y 16341:** “The ceiling on the radii `alpha_0,alpha_1,gamma_0` is fixed before `M_1` and is independent of `M_1`.” This is explicit independence from the cube size in that statement.
- **Y 17399:** “`bar-kappa` … does not depend on `M_1,R_1`, and they do not depend on it”; and, except for two specified bounds, “every constant, rate and ceiling … is independent of … `M_1,R_1` once these are large enough.” This is the only broad explicit independence clause found for the geometric pair. Its stated exceptions are (i) one statement-7 bound used for convergence and (ii) the entrywise bound in mechanism (i), neither appearing in localized bounds, rates, weights or sums of weights.
- **Y 35854–35855:** “no constant chosen below depends on the cutoff, the tower depth or a coupling.” This does not say constants below are independent of `R_1` or `M_1'`.
- **Y 84042:** the constant called `R_1` in the displayed large-field estimate is “not the geometrical gap parameter”; the following text allows construction-parameter dependence. It is a distinct symbol use.
- **Y 109804:** a later scale criterion requires `R_1<=C(log x)^B`, as well as an upper bound on `N+M+m+|W|`. Here `R_1` is the local coordinate radius from Y 109666–109698, where `|a|<=R_1` and `gR_1<=1/4`; it is not the geometric gap parameter. The same line's `M` counts retained coordinates/terms, not the localization cube `M` of Y 638. This is a genuine upper bound in that separate argument, not an upper bound on the floor parameter.
- **Y 2372:** “Take `M=L^{m_0}`”; this is a fixed value of `M` in that separate graded-source setup. I found no cross-reference equating it with the localization cube of Y 638. Other `M` occurrences define matrices, norms or indices and are not the localization size.

## 4. Candidate `R_1=L^3`, with `M_1'` and `M` raised by Y's rules

“Affected, loss taken by a later constant” means the line explicitly permits a later size or constant to absorb the increased floor. “NOT DECIDED” means Y does not give enough order or identify reused symbols to settle the effect. Each verdict is marked **quoted** when the line says the relation directly, or **my reading** when the disposition follows from comparing lines. This table covers each matching line that the candidate floor or its stated aliases can change. Pure operator/matrix matches and the unrelated local-coordinate `R_1` are not changed by the geometric candidate.

| Y line | Verdict | Basis |
|---:|---|---|
| 638 | affected, loss taken by a later constant (**quoted**) | auxiliary powers are fixed before domains/norms |
| 639 | affected, loss taken by a later constant (**quoted**) | separation `rho` is defined from `R_1` |
| 651 | affected, loss taken by a later constant (**quoted**) | raising `R_1` raises the `M_1'` floor |
| 652 | affected, loss taken by a later constant (**quoted**) | raising `M_1'` raises the `M` floor |
| 660 | affected, loss taken by a later constant (**my reading**) | first tower is more eroded as the gap grows; its definition still applies |
| 662 | affected, loss taken by a later constant (**quoted**) | second tower cube side uses `M_1'` |
| 664 | affected, loss taken by a later constant (**quoted**) | second tower clearance uses `M_1'` |
| 3662 | NOT DECIDED (**my reading**) | regular-configuration cubes use `M_1`; no link to the floor's `M_1'` is stated here |
| 3970 | NOT DECIDED (**quoted**) | `M_1` enters a cited lemma's hypotheses; the choice relation to `M_1'` is not stated here |
| 4391 | NOT DECIDED (**quoted**) | `M_1` and `M alpha_0` have smallness conditions; this paragraph gives no order for them |
| 4400 | NOT DECIDED (**quoted**) | `c_1,B_1` may depend on `R_1`; their identity with the R1-independent ceiling of 17399 is not given |
| 8594 | NOT DECIDED (**my reading**) | gauge cubes use `M_1`; relation to the candidate size is not specified in this line |
| 13449 | NOT DECIDED (**my reading**) | localization cube size uses `M_1`; relation to `M_1'` is not specified here |
| 13450 | NOT DECIDED (**my reading**) | `M_1`-tower relation to the raised size is not identified here |
| 14938 | affected, loss taken by a later constant (**quoted**) | fixes the powers `frakM,R_1,rho` before geometry |
| 14941 | affected, loss taken by a later constant (**quoted**) | larger `R_1` improves `R_1 frakM>=L^2rho` if `rho` stays fixed |
| 14946 | affected, loss taken by a later constant (**quoted**) | the gap is `R_1 frakM xi_j` |
| 16102 | affected, loss taken by a later constant (**quoted**) | lower gap floor and separated-region definition |
| 16105 | affected, loss taken by a later constant (**quoted**) | separated-region distance uses `R_1M_1` |
| 16173 | affected, loss taken by a later constant (**quoted**) | lower bound `R_1>=L` |
| 16174 | affected, loss taken by a later constant (**quoted**) | lower bound on `R_1frakM` |
| 16126 | NOT DECIDED (**my reading**) | larger gauge cubes are stated, but this passage gives no order for the room needed by their gauge bounds |
| 16244, 16278 | affected, loss taken by a later constant (**my reading**) | walk cells and torus lower floor scale with `M_1,R_1`; no fixed torus ceiling is stated |
| 16341 | not affected (**quoted**) | radius ceiling explicitly independent of `M_1` |
| 16349 | affected, loss taken by a later constant (**quoted**) | the longer-sequence case explicitly uses larger `M_1` and smaller radius ceiling |
| 16355, 16463, 16974, 16979, 16981, 16989 | affected, loss taken by a later constant (**my reading**) | the displayed inverse powers/exponentials improve with larger `M_1` |
| 16432, 16439 | affected, loss taken by a later constant (**quoted**) | larger `R_1M_1` improves distance and decay |
| 17238 | affected, loss taken by a later constant (**my reading**) | `rho` is defined using the larger gap; no adverse term is stated in this line |
| 17399 | NOT DECIDED (**quoted**) | choice order allows final `M`, but also says the radii ceiling is independent of `R_1`; relation to Y 4400's `c_1` is unresolved |
| 17434 | NOT DECIDED (**quoted**) | sets `frakM=M_1` in its subsection, with no link to the candidate `M_1'` there |
| 23075 | NOT DECIDED (**my reading**) | separate local `M_1` notation; no identified link to `M_1'` |
| 23486 | NOT DECIDED (**my reading**) | local scale `M_1xi_j`; identity with candidate parameter not specified |
| 23571 | NOT DECIDED (**my reading**) | local `M_1` symbol; identity not specified |
| 35698 | affected, loss taken by a later constant (**quoted**) | larger gap helps the stencil fit |
| 35843 | affected, loss taken by a later constant (**quoted**) | identifies the second-rule `M_1` with `M_1'` |
| 35850 | affected, loss taken by a later constant (**quoted**) | `R_1` and `M_1` floors |
| 35851 | affected, loss taken by a later constant (**quoted**) | `M>=L^4M_1`; localization size is enlarged afterward |
| 35876 | affected, loss taken by a later constant (**my reading**) | first-rule erosion uses the raised gap |
| 35877 | affected, loss taken by a later constant (**my reading**) | second-rule clearance uses the raised `M_1` |
| 35892 | affected, loss taken by a later constant (**quoted**) | separation threshold grows with `R_1` |
| 35893 | affected, loss taken by a later constant (**quoted**) | torus floor; `M/L>=L^3R_1frakM` follows from the displayed size floors |
| 35912 | affected, loss taken by a later constant (**my reading**) | distance allowance grows with the gap |
| 36714, 36755 | affected, loss taken by a later constant (**quoted**) | separation variable is `rho=R_1frakM` |
| 37082 | affected, loss taken by a later constant (**quoted**) | the assumptions are lower floors; `M_1>=rho`, `M>=L^3M_1` |
| 37106 | not affected (**my reading**) | both sides scale by the same `M_1` |
| 37112 | affected, loss taken by a later constant (**my reading**) | RHS grows with `M_1`, but `M` is raised after it; the stronger `M>=L^4M_1` is stated nearby |
| 37464 | NOT DECIDED (**my reading**) | deleted-set distance bound grows with `M_1` |
| 37466 | NOT DECIDED (**my reading**) | changed-row distance allowance grows with `M_1` |
| 37470 | NOT DECIDED (**quoted**) | text increases the fixed cut halo |
| 37471 | NOT DECIDED (**quoted**) | carrier enlargement is `C_cut M_1` |
| 37473 | NOT DECIDED (**my reading**) | bound grows with `M_1`; no order for `D` is quoted here |
| 37487 | NOT DECIDED (**quoted**) | text says to increase `K_cl` |
| 37489 | NOT DECIDED (**quoted**) | explicit fit `(C_cut-3)_+M_1<=D/2`; no choice of `D` after the floor is stated here |
| 49958 | affected, loss taken by a later constant (**quoted**) | lower bounds `R_1>=L`, `M_1>=R_1frakM` |
| 49959 | affected, loss taken by a later constant (**quoted**) | lower bound `M>=L^4M_1` |
| 49962 | affected, loss taken by a later constant (**quoted**) | larger gap improves lower bound on `rho` |
| 49965 | affected, loss taken by a later constant (**quoted**) | lower bound on `R_1frakM` |
| 49968 | affected, loss taken by a later constant (**quoted**) | positive product lower bound |
| 49969 | affected, loss taken by a later constant (**quoted**) | positive product lower bound |
| 49970 | affected, loss taken by a later constant (**quoted**) | positive product lower bound |
| 62437 | NOT DECIDED (**my reading**) | layer cube size grows with `M_1`; fit not settled here |
| 63174 | NOT DECIDED (**my reading**) | four-layer physical width grows with `M_1` |
| 63184 | NOT DECIDED (**my reading**) | collar width grows with `M_1` |
| 63199 | NOT DECIDED (**my reading**) | required clearance grows with `M_1` |
| 63509 | NOT DECIDED (**my reading**) | enlarged local cubes use `M_1` |
| 63873 | affected, loss taken by a later constant (**quoted**) | estimate uses `M/M_1`; increasing the ratio improves decay |
| 63876 | affected, loss taken by a later constant (**quoted**) | text explicitly says to choose `M/M_1` large enough |
| 64111 | affected, loss taken by a later constant (**my reading**) | the grid uses the raised cube size |
| 64243 | affected, loss taken by a later constant (**quoted**) | estimate uses `M/M_1`; larger ratio improves decay |
| 64248 | affected, loss taken by a later constant (**quoted**) | text explicitly chooses `M/M_1` to absorb growth |
| 64454 | affected, loss taken by a later constant (**my reading**) | estimate has exponential decay in `M/M_1` |
| 68513 | affected, loss taken by a later constant (**quoted**) | lower bound `M>=L^3M_1` |
| 68516 | NOT DECIDED (**my reading**) | defines local cube size; no fit statement on this line |
| 68670 | NOT DECIDED (**my reading**) | clearance grows with `M_1` |
| 68675 | NOT DECIDED (**my reading**) | read allowance grows with `M_1` |
| 68681 | NOT DECIDED (**quoted**) | fit condition requires `D` large relative to `M_1` |
| 71847 | NOT DECIDED (**my reading**) | tower uses larger cube size |
| 71858 | NOT DECIDED (**my reading**) | distance allowance grows with `M_1` |
| 71861 | NOT DECIDED (**quoted**) | explicit upper fit `2M_1L^t+L^{t-1}<w` needs room after increasing the cube size |
| 72930 | affected, loss taken by a later constant (**quoted**) | displayed choice order places `M` after `M_1'` |
| 72938 | affected, loss taken by a later constant (**quoted**) | rates precede size choices and `M` is chosen after `L,kappa` |
| 72939 | NOT DECIDED (**quoted**) | says `M_1` is L-only and `R_1` depends on `L,M_1`; link to the Y 638 choice is not explicit |
| 73300 | not affected (**my reading**) | this clause uses `M_1` fixed from `L` alone in its local choice order, not the `M_1'` raised from the Y 638 floor |
| 75725 | affected, loss taken by a later constant (**my reading**) | `M_2=L^2M_1` tracks the cube size |
| 77756 | affected, loss taken by a later constant (**my reading**) | decay depends on `M/M_1`; ratio must be chosen to dominate |
| 84258 | NOT DECIDED (**my reading**) | walk-cell scale grows with `M_1` |
| 84259 | NOT DECIDED (**my reading**) | halo grows with `M_1` |
| 84277 | affected, loss taken by a later constant (**my reading**) | displayed entropy margin improves with larger `M_1` |
| 84261 | NOT DECIDED (**quoted**) | explicit fit condition `C M_1 xi_{n*}<w_{l(Omega_0)}`; no later choice of that room is quoted here |
| 97350 | NOT DECIDED (**my reading**) | collar count grows with `M_1` and falls with `M` |
| 97362 | NOT DECIDED (**my reading**) | total width bound grows with `M_1` |
| 97431 | NOT DECIDED (**my reading**) | removed neighborhood grows with `M_1` |
| 97432 | NOT DECIDED (**my reading**) | region grid uses the raised cube size |
| 97433 | NOT DECIDED (**my reading**) | inner rim grows with `M_1` |
| 97436 | NOT DECIDED (**quoted**) | explicit condition `10M_1<M checkR_j`; floor `M>=L^4M_1` alone does not establish it without a lower bound on `checkR_j` |
| 107517 | NOT DECIDED (**my reading**) | the product `M_1M_2` grows; no compensating choice is stated in this line |
| 109666 | not affected (**quoted**) | `R_1` is a local coordinate radius, not the geometric gap |
| 109667 | not affected (**quoted**) | the local radius has its own smallness bound |
| 109697 | not affected (**my reading**) | local-coordinate derivative hypothesis |
| 109698 | not affected (**quoted**) | local-coordinate radius appears in a cubic bound |
| 109789 | not affected (**my reading**) | local-coordinate error budget |
| 109804 | not affected (**quoted**) | local radius upper bound is explicitly separate from geometric `R_1` |
| 128495 | NOT DECIDED (**my reading**) | this separate local ratio `M/M_1` has no stated identity with the candidate's `M_1'` |
| 128790 | NOT DECIDED (**my reading**) | halo width grows with its local `M_1` |
| 128796 | NOT DECIDED (**my reading**) | local upper scale allowance uses `M_1` |
| 131926 | NOT DECIDED (**my reading**) | local region size grows with `M_1` |
| 132201 | affected, loss taken by a later constant (**my reading**) | tower cubes use `M_1` |
| 132204 | affected, loss taken by a later constant (**quoted**) | clearance grows with geometric `R_1` |
| 132205 | affected, loss taken by a later constant (**quoted**) | the erosion count depends on `R_1` |
| 132222 | affected, loss taken by a later constant (**my reading**) | fixed tower depth count, larger cube scale |
| 132258 | affected, loss taken by a later constant (**quoted**) | repeats the `M_1>=R_1frakM`, `M>=L^4M_1` floors |
| 132408 | affected, loss taken by a later constant (**my reading**) | required width grows with `M_1` |

**Reading outcome:** the geometric `R_1=L^3` floor is not shown to break the tower floor rules. Several Y estimates improve with the increased gap, and Y explicitly raises `M_1'` and then `M`. The all-file check is not a proof that every separate chapter has compatible room: the upper fit conditions at Y 71861, 84261 and 97436, the read/halo costs at Y 37464–37489, and the possible `c_1`/ceiling mismatch at Y 4400 versus 17399 remain **NOT DECIDED** from the quoted order clauses. In addition, later repeated `M_1` and `R_1` uses are not all explicitly identified with the Y 638 geometry. This is a reading result, not a status grant.

