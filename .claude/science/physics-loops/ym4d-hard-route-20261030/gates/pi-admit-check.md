# Check: library/pi-admit.md (PI-ADMIT, stop (c))

Checked line by line by Claude (Opus 5.5), 2026-11-08. One reading. Not an audit.
Clone `eba68a83d`. Note: `library/pi-admit.md` (561 lines, Codex gpt-6-astra).
Sources read: I (`31a47c543775`) and N (SHA-256 `222ef1bd...f178`, matches the note).
SA (`YM4_sketch_500.tex`) was not opened. SA 17396 and 17440 are not checked.

## Verdict: ADVANCE

The proofs that the note says are proved here are correct.
The stop (c) is honest: no counterexample is claimed, and the refined class is not proved.
I found no statement in I or N that already supplies (5)-(6) at I 131725-131746.
I 137566-137569 says the opposite (finding 15).
Findings 4, 9, 11, 13 and 15 ask for small wording repairs. None changes a result.

## Findings

### Proposition 3.1 (note 79-175)

1. **Box conditions (1).** Note 95-101; I 52670-52705, 45242-45244. CONFIRMED.
   `M_1 | M_1^sharp | M`, (F1) `M >= 13 L^2 M_1^sharp` and (F2) `M_1^sharp >= 3 M_1`
   are I's hypotheses. `r_N + 2 <= 4 M_1^sharp` is the right condition for (3):
   `s_j + r_N l_j + 2 eta <= 5 s_j` follows because `eta <= l_j`.
   With `M_b = M_1` and `M_t | M_b`, it holds anyway, since `7 M_t + 2 <= 7M_1^sharp/3 + 2`.

2. **Choice of the box centre.** Note 123-127; I 52800-52814 (Fact (i)), I 52881-52925 (lemma). CONFIRMED.
   If `lambda(x) = j`, then `x` is in `X_j`. Fact (i) puts `x` in an `s_j`-cube contained in `X_j`.
   A vertex of that cube is a centre `y` with `|x - y|_inf <= s_j`.

3. **Inclusion (3) and data region.** Note 129-138; I 52381-52384 (col), I 52394-52409. CONFIRMED.
   PI's `Omega_0^+` (out-pi 103-106) equals I's `Omega_0^{+2 eta}`. So (col) puts every S1-loc bond
   in `square^4` intersected with the data region. The arbitrary gauge outside the data region is unused.

4. **Two adjacent shells, all levels.** Note 140-146; I 52816-52878, 53220-53245. CONFIRMED, with one gap in the wording.
   The account derives "at most two adjacent shells" from (A1) and (F1).
   (A1) (I 45570-45585) needs `Omega_j` to be unions of level-j **M-cubes**, with gaps `>= M l_j` for `j >= 1`,
   and it needs `Omega_0` to be the Dirichlet hull. PI's (T) asks only for `M_b`-block unions.
   (A1) has **no** gap between `Omega_0^c` and `Omega_1`. The note's "aligned shells" (89) and
   "retain the PI gap" (104) cover this, but only by implication.
   Repair: write the (A1) nest explicitly as a hypothesis, and say that the `j=0` gap of (T) is added.

5. **Scale conversion and (4).** Note 142-154; I 52412-52416, 52640-52646; out-pi 135-141. CONFIRMED.
   Both endpoint levels and the index position lie in the two shells met. So `l_{lambda(z)} <= L l(x_iota)`.
   That gives `l|A| < L a^sharp` and `l^2|grad A| < L^2 a^sharp`.
   With `a_0 = a^sharp <= a_0^*/2`, this is S1-loc (`<= L^2 a_0`). The exterior scale is `eta` in both conventions.
   One small point: the S1-loc difference pairs are read only inside `Omega_0^+`, as S2+ says (out-pi 125).
   Then the claim "no required bound uses the arbitrary gauge" (138) holds.

6. **S2 and S2+.** Note 158-165; I 52620-52647, 52762-52801. CONFIRMED.
   The direct ratio argument (value loss `L`, difference loss `L^2`) gives `N_{U_r}(a) < L^2 r a_1^oplus <= a_1^*/2`.
   This needs no restriction to `j in {0,1}` (I clause (b) is stated only there).
   S2+ holds at weight `eta` without seam loss, **provided** the norm's bond set includes those exterior bonds and pairs.
   I's norm runs over `B-hat` (I 52648-52651), and `B-hat` is not shown to contain them.
   The note states this as an assumption (92-93, 162-163). Correct.

7. **Order of constants.** Note 167-170; I 53164-53218. CONFIRMED.
   `a^sharp <= a_0^*/2` is a one-sided ceiling imposed after `M`. `a_0^*` depends only on `N, L` (out-pi §3.3 item 7).

8. **The conclusion matches out-pi's definitions.** It covers every `x` in `Omega_0`, every bond of `N(x)` in `Omega_0^+`,
   endpoint scales, S2 on field bonds with stencils, and S2+ on `Omega_0^+`.
   The constants are uniform. CONFIRMED.

### (7)-(10), (13), (16)-(18)

9. **(7)-(8).** Note 232-267; N 61992-62009. CONFIRMED.
   N gives `Omega_1^c` containing `H_1 = P_0'^{~5}` and `Omega_0 = Omega_1^~`.
   The cell count is right: a cell meeting `Q_x` is at most 2 from `Omega_1`, and so at least 4 from `A`.
   This uses `q eta < W_1` (sup-distance less than one cell means touching cells).
   A bare cube whose enlargement contains a given plaquette passed its test, which gives (8).
   Scope: this is a certificate for `U_bare`. No PI entry is shown to have `U_bare` as its reference on `Q_x`.
   The note says this (297-299, 553). Repair (wording): line 534 says "the first bare inverse uses I 13142-13173".
   That remark is the general (S1)-(S2) entry. It is not a first-step entry with the bare field.

10. **(9)-(10).** Note 269-295; N 5104-5125. CONFIRMED.
    In 4D, sliding a bond past the later coordinate segments of a `2q` box takes at most `3 * 2q = 6q` plaquettes, and `K = 8q` covers this.
    The bound comes from telescoping unitary conjugates. The principal SU(2) logarithm is traceless.
    `eta|A| <= 2K eps_0` holds when `K eps_0 < 1/4`. For (10), `eta^2|grad A| = eta|A(b') - A(b)| <= 4K eps_0`.
    The twist is zero. Constants are fixed before `eps_0`.

11. **(13), restriction.** Note 359-374. CONFIRMED.
    From `Omega'_j subset Omega_j` we get `lambda' <= lambda`, `N'(x) subset N(x)`, and `Omega'_0^+ subset Omega_0^+`.
    Old field bonds and their stencils include the new ones. Newly exterior bonds keep their old bounds at weight `>= eta`.
    Repair (wording): also require that the smaller tower satisfies (T) and the PI floors.
    N 37360-37386 is the finer-scale restriction of a critical field. "Matches" is fair as an analogy.

12. **(16)-(17).** Note 453-481; out-pi 1195-1197, N 10546-10551, 16129. CONFIRMED.
    Exactly one of the six plaquettes of `b = (0, eta e_2)` has a corner with `x_1 = eta`.
    In PI's normalization a flat plaquette contributes `+eta^{-2}||A||^2`.
    This is the same formula with the sign reversed against out-pi 1197, where holonomy `-I` gives `-eta^{-2}`. So (17) is exact.
    (18) is the standard Schur complement.

13. **(14)-(15), inference test.** Note 393-421. CONFIRMED as stated. Its reach is weaker than it looks.
    `b_2` lies at sup-distance `2 eta` from `X`. No coefficient of `M_5` reads it.
    Plaquettes through field bonds stay within `eta` (every corner is within `eta` of the interior endpoint).
    Level-0 rows are field bonds, and `D_U` reads field bonds. `b_2` enters only the S2+ and S1-loc **hypothesis** domain.
    The example therefore tests a hypothesis index, not an actual read. The note's own filler remark (423-430) applies to `b_2`.
    Repair: say so at 409-421.
    Possible sharpening (UNCLEAR; it needs a check that the local models of out-pi §5.2 read no more):
    C0-SUP (5)-(6) may be needed only on bonds within `eta` of `X`, together with the difference stencils at those bonds.

### C0-SUP and the three routes

14. **Statement and bare scale.** Note 179-217; out-pi 763-798, 1630, §3.3 item 6. CONFIRMED.
    A patch at level `j >= 1` has `dist(x, Omega_0^c) > R M_b eta >= 24 M_b eta > r_N L eta + 2 eta`, so it cannot cross.
    A crossing level-0 patch reaches at most `2 r_N eta`, which is less than the gap.
    So (5) at scale `eta` with `L^2 a_0^*` is exactly S1-loc there. (6) is exactly S2/S2+ there.
    C0-SUP is the boundary part only. Prop 3.1's interior antecedent `(reg)^sharp` at actual entries is also unsupplied
    (I 49495-49523; layer-thm-part R, L0). The table lists it as an input (552, 560).
    "First open input" is therefore right, but it is not the only open input.

15. **Is (5)-(6) already supplied at I 131725-131746?** MISMATCH with any such hope. The note is CONFIRMED.
    Item 10 gives `K_109` membership on `X_a` and lists the strata: cubes, raw index-zero members, and `(3.35)_0` on `Y'`.
    Its tested cubes and Balaban's gauge clauses act only on `Q cap Omega_0` (I 49503-49510; out-pi 1212).
    I 137566-137568 says that `B_Z` "lies outside the geometry in which the spaces of pairs ... are defined".
    I 137568-137569 calls the source of item 10 "the part of [the T-step layer lemma] on the localised layer function (proof incomplete)".
    That lemma is headed "Stated; proof incomplete" (I 131633). The account itself does not supply C0-SUP there.
    Repair: cite I 137566-137569 beside the remark at note 221-222.
    My targeted searches of N (protruding, crossing, exterior plaquette) found no supply.
    Near N 63836 and 72688 there are exterior-plaquette tests, but they belong to the arrest/large-field box.
    They are not the small-field PI entry. This search was not exhaustive.

16. **The routes are distinct, and each fails where the note says.** CONFIRMED.
    Route 1 (bare tests) stops at (11), which is correct: unitary telescoping, real `h`.
    Route 2 (hull gauges, restriction and cutoff) stops at `Y_loc` and the global pair (I 49120-49189, 46800-46829, 119615-119650).
    Each cited range says what the note reports.
    Route 3 (native inner inverse) is blocked by (17)-(18). This route replaces PI instead of proving C0-SUP. As a route to the target it is still distinct.

17. **Scope.** CONFIRMED. No counterexample is claimed (518-522). The construction on the refined class is not claimed (526-531, 560).
    The partition-coverage caveat matches N 62010-62019. No independent check is claimed.

## Not checked

SA 17396 and 17440; N 1990-2078, 16964-16977, 31940-32015, 35634-35907 (only 35276-35287 was read), 40688-40713;
I 45439-45507, 47789-47812, 50149-50319, 53260-53333.
