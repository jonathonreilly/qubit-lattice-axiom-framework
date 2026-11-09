lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T10:49Z

# h-geo-check: line-by-line check of `library/h-geo.md` (FINISH row 615)

Provenance: Claude Opus 5.5, effort high, Mac mini worker 2, branch `claude/ym4d-hard-route` at 5d7b71fab. Not an audit. Checker did not write `library/h-geo.md` (Claude Fable 5.2 did). Source: Sussman-Alpoge YM4_1400.tex at commit 2bc0658f91d2 (Y below), read by line number; Sussman and Alpoge, with Claude and Codex as authors of their text, are credited for every cited line.

Status: in progress (written section by section). No numeric job was run (memory 62 percent free at start; none needed). Everything below is by reading Y and by hand.

## Repo search

`grep -n` over this lane folder for `h-geo`, `H-GEO`, `M_1'`, `minimal recursive tower`, `R_1 M_1`: the only prior items are `library/h-geo.md` (row 614, the object of this check), `library/rim-scale.md` (the consumer), `library/geo-5.md` (outline geometry, cited by h-geo for CORE) and the registry row `library/open-registry.md` line 1002. `library/open-core.md` has no row for H-GEO or for the convention question of item (5); FINISH row 616 owns CORE, which this check does not rebuild. No other row covers the five checks below.

## (1) Constants: HOLDS AFTER A STATED REPAIR (notation only)

Read: Y 637-676, 14925-14952, 35258-35278, 35836-35890, 72920-72940, 132254-132260, 49955-49972, 55275, 61995-62004.

- The order holds as written in Y: `L >= 13` odd, `R_1 >= L`, `M_1' >= R_1 frakM`, `M >= L^4 M_1'` (Y 650-652), "in addition to the background floors"; Y 35853-35855 adds that the floors come first and `M` is increased after. Y's global order (Y 72930) puts `R_1` before `M_1'` and `M_1'` before `M`, so the floors `M_1' >= R_1 frakM` and `M >= L^4 M_1'` are floors on later constants. Consistent.
- **Fact 1.1 holds**: `u_{q+1} = L M L^q >= L^5 M_1' L^q >= L^5 R_1 frakM L^q`. Two lines of arithmetic; checked.
- **The `M` of the box formula is the localization size `M` of Y 637-645.** Y 63774: `u_i = M L^i` "the side of an `M`-cube"; Y 637-645: "`M` is the localization cube size ... The partition `pi_j` consists of the centered, half-open `M`-cubes"; Y 55275 "localization size `M`, a power of `L`"; Y 72930 has a single `M`, last of the cube sizes; Y 132256-132258 ("the original `pi_k`-cells have side `M/L`. The inequalities `M >= L^4 M_1` and `M_1 >= R_1 frakM`") ties the large-field cells to the same `M`. `a_i = M Rcheck_i L^i` is a union of these `M`-cubes since `Rcheck_i` is a power of `L` (Y 61998-62000).

**Defect 1 (notation; repair stated).** Y uses the letter `M_1` for two different constants. Y 72930 and Y 72939: `L < (M_1, R_1) < ... < M_1' < M_2 < ... < M`, "`M_1` depends on `L` alone, and `R_1` depends on `L` and `M_1`". So the global `M_1` (the walk-cube size of Y 16102, Y 17399) is chosen **before** `R_1` and cannot be assumed `>= R_1 frakM`. The inequality `M_1 >= R_1 frakM` that h-geo uses (its section 1 item 2, Fact 1.1, Lemma 3.1, the order paragraph of section 4) is true only for `M_1'`: Y 35843 "Write `M_1 = M_1'` in this subsection", and Y 49958, Y 132258 are uses of the same renamed constant (they are the tower rules of Y 656-667). Repair: in h-geo read every `M_1` as `M_1'` and cite Y 651-652 and Y 35843 for `M_1' >= R_1 frakM`. With that reading every statement of h-geo section 1 holds. h-geo's section 1 item 2 also lists Y 35848-35853 and Y 49957-49959 as "again" the same inequality; they are, under Y 35843.

A second notational point, already noted by h-geo (section 1 item 3), is correct: Y 638 writes `rho = R_1 frakM`, while Y 14940 and Y 49962 use `rho = L^{-2} R_1 frakM` (the `rho` of `mb:separation`). The floor of `bgc:proper-background` is `R_1 frakM xi_j` in both readings (Y 14942-14943).

## (2) Lemma 2, the nest gaps: HOLDS AS WRITTEN (one citation to add in (d))

Read: Y 63684-63705, 63716-63830, 61980-62004, 72244-72256.

I recomputed every gap by hand from Y's box formula (Y 63783-63811, `eq:elab-history-prepared-boxes`). Notation as in h-geo: `O_i = H_i^{[8 a_i]}`, `G_i = H_i^{[10 a_i]}` for `h < i <= m`, `G_{i-1} subset H_i` (Y 63788), `a_{k_0+1} = u_m`.

- Box formula itself: `Z''_i = O_i^{[-5 a_i]} = H_i^{[3 a_i]}` for `h < i <= k_0`; `Z''_i = O_{k_0+1}^{[-(5 u_m + w_i)]} = H_{k_0+1}^{[3 u_m - w_i]}` for `i > k_0`, valid because `5 u_m + w_i <= 8 u_m` (`w_{k_0+1} = 2 u_m`, and `w_i <= u_m L/(L-1) < 2 u_m` otherwise) and Y's erosion formula (Y 63792-63797) holds for `0 < s <= 8 a_i`. Agrees.
- (a) `Z''_{q+1} = H_{q+1}^{[3a_{q+1}]} supset G_q^{[3 a_{q+1}]} = H_q^{[10 a_q + 3 a_{q+1}]}`, so `g_q >= 7 a_q + 3 a_{q+1}`. Agrees (Y 63820-63822 states `>= 7 a_i`).
- (b) `Z''_{k_0+1} = H_{k_0+1}^{[u_m]} supset H_{k_0}^{[10 a_{k_0} + u_m]}`, gap `>= 7 a_{k_0} + u_m`. Agrees.
- (c) Same centre box, so `g_q = w_q - w_{q+1}`. For `k_0+2 <= q <= m-1`: `= u_{q+1}` exactly. For `q = k_0+1`: if `m = k_0+2`, then `w_{k_0+1} = 2u_m` (the explicit rule takes precedence over the sum, which would give `u_m`) and the gap is `2 u_m`; if `m >= k_0+3`, the gap is `2u_m - sum_{r=k_0+3}^m u_r > u_m (L-2)/(L-1) >= u_m/L >= u_{k_0+2}`, using `L^2 - 3L + 1 >= 0`. Agrees.
- (d) `g_h >= 3 a_{h+1}`: needs `Omega_h^c cap X subset G_h`. Y's formula `O_i = H_i^{[8a_i]}` is stated only for `i > h` (the step at `h` may create; Y 63759-63761), so h-geo's "`D_h = O_h`" must read `O_h := Omega_h^c cap X`. The inclusion into `G_h = Z_h cap X` holds because each step has `Z^{[0]} = bx((Omega_t^c)^{~2} cup ...) supset Omega_t^c` (Y 61983-61986) and the three fates enlarge `Omega` and `Lambda = Z^c` together (Y 62103-62125), and Y 63818-63819 states the conclusion. **Repair (citation only):** add these two citations to (d). Then `D_h subset G_h subset H_{h+1}` and `g_h >= 3 a_{h+1}`.
- (e) `Z''_{j+1} subset O_{j+1}` (for `j+1 > k_0` via `H_{k_0+1}^{[3u_m]} subset O_{k_0+1} subset O_{j+1}`), and `O_{i+1} supset H_i^{[10a_i + 8 a_{i+1}]} = O_i^{[2a_i + 8a_{i+1}]}`, so the splice gap is `>= 2a_{j+1} + 8 a_{j+2} >= 8 a_{j+2}`. Agrees. The stage members are as h-geo says: Y 72244-72250 ("The only member of the sequence that changes is the one of index `j+1`").
- (f) `dist(H_{k_0+1}^{[3u_m]}, X^c) >= 5u_m + 2a_m`, from `O_{k_0+1} = H_{k_0+1}^{[8u_m]} subset O_m` and `X = G_m = O_m^{[2a_m]}`. Agrees.
- Last sentence: `a_i >= u_i` since `Rcheck_i >= 1`; each case is `>= u_{q+1} = L M L^q >= L^5 R_1 frakM L^q` by Fact 1.1 (with `M_1'`, Defect 1). Agrees.

Remarks (i)-(iii) of h-geo section 2 hold; (i) is Y 62088-62091 verbatim in content.

## (3) Lemmas 3.1 and 3.2, towers and meet: HOLDS AFTER A STATED REPAIR

Read: Y 656-676, 12928-13030, 35857-35890, 37069-37115, 62430-62440, 63170-63200, 132180-132215, 135190-135215.

- **First rule** (Y 657-660): every kept cube has `dist(C, T_q^c) > R_1 frakM L^q`, a finite union, so the gap is `> R_1 frakM L^q`. Holds as written.
- **Second rule** (Y 661-665, with `M_1'`): gap `>= M_1' L^{q+1} = L M_1' L^q >= L R_1 frakM L^q > R_1 frakM L^q`. Holds, with Defect 1's reading.
- **`mu`-tower** (Y 12983-12996): gap `>= mu xi_{q+1}`. For powers of `L`, `L mu > R_1 frakM` iff `mu >= R_1 frakM`, so h-geo's condition `mu >= R_1 frakM` is exactly the right one. h-geo's note that Y's own bound `mu xi_{q+1} > rho xi_q` (with `mu >= max{rho, frakM, L^2}`, Y 12961) is weaker than the floor by a factor up to `L` (when `rho = L^{-2} R_1 frakM`) is correct. h-geo's claim "true for `mu = M_1`" needs Defect 1's repair: it is true for `mu = M_1'`, and **not implied** for the global walk-cube `M_1` of Y 72939. I could not settle from Y 62436-62437 and Y 63183-63184 which of the two the large-field collars use (Y 68516: "`M_1` is the cube size used in the localization"; Y 63873 has decay `e^{-c(M/M_1)}`). **This does not reach the consumer**: the tower at `dX` in `rim-scale.md` (G3) is "the minimal recursive tower of the component" (Y 135196-135197), and Y 132180-132210 identifies the minimal recursive tower as either "the minimal determining tower with `M_1`-cubes" (clearance `>= s`, the second rule) or "the rule with `frakM`-cubes and strict clearance `> R_1 s / L`" (the first rule), in a passage that fixes `M >= L^4 M_1`, `M_1 >= R_1 frakM` (Y 132257-132258). Both are covered. Repair: in Lemma 3.1 replace "`mu = M_1`" by "`mu = M_1'`" and add that the consumer's tower is a first- or second-rule tower (Y 132180-132210).
- **Erosion bound**: increments `<= 2 M_1' L^{q+1}` (second rule) or `<= R_1 frakM L^q + frakM L^{q+1} <= 2 M_1' L^q` (first rule, using `M_1' >= R_1 frakM >= L frakM`); summing, `w_q <= 2 M_1' L^q L/(L-1) < 3 M_1' L^q <= 3 L^{-4} M L^q < M L^{q-3}`. Holds; agrees with Y's `htc:geometry` (Y 35868-35881), which states `w_q <= M L^{p-3}`.
- **Alignment**: `T_q` is a union of cubes of side `frakM L^q` or `M_1' L^q`, aligned and nested since `L` is odd (Fact 1.2). Holds.
- **Lemma 3.2 (meet)**: `J_q^c = A_q^c cup T_q^c`, `J_{q+1} subset A_{q+1} cap T_{q+1}`, so the gap is at least the minimum of the two gaps. For the relative version, `A_q^c cap T_0^c subset T_q^c` (towers decrease), so that part is handled by the tower gap. `J` decreases. The cube-wise meet equals the intersection because both factors are unions of aligned `frakM xi_q`-cubes. Holds as written; it is Y's own argument (Y 37102-37103, Y 13024-13030).
