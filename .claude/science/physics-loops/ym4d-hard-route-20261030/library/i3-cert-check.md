lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T16:13Z

# i3-cert-check (FINISH row 630): line check of `library/i3-cert.md`

Status: DONE 2026-11-10 (one session; not an audit; no numerics).

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, one session, 2026-11-10, at commit
52da449e5. This is a one-model line check, not an audit. `library/i3-cert.md` was written by
Claude Fable 5.2 (row 624); I did not write it. Source: Sussman and Alpoge, `YM4_1400.tex` at commit
2bc0658f91d2 of ethanwsussman/Yang--Mills-LLM-experiment (my own copy, fetched by URL, byte-identical to
`/tmp/ym4_1400.tex`, 136,637 lines). `Y n` is line n of that file. No numeric job was run; every check
below is by hand. `library/cov-x.md` (row 628) was read in sections 0, 3 and 8 only, as the row says;
it is not checked here (row 633 owns that).

Credit. Everything checked here is Sussman and Alpoge's argument (their text names Claude and Codex as
authors), paragraph `hi:prepared-real-endpoint` (Y 65406-65591) and the lines it cites; the nest and the
stage test are Bałaban's (CMP 122 (1989) 175, (1.24)), as ported by Y.

Repo search. `library/open-core.md` has no entry for `i3-cert-check`; `library/open-registry.md` row
RIM-I3 names this row as the check. FINISH rows 622, 624, 628, 633, 634 are neighbours; the row says
this is not a duplicate. I did not attack (COV) (row 628/632 own it).

Verdict scale: HOLDS, HOLDS-WITH-REPAIR (a short repair given, the statement survives), FAILS (first line
that fails).

## 0. Verdict

**Theorem 9.1 of `library/i3-cert.md` HOLDS given (COV)**, with the short repairs below, none of which
changes its statement or `C_3`. With the four edits of `library/cov-x.md` it also holds, with
`C_2' = max(C_2, 6 . 4^r)` in Lemma 2b, in (H5) and in `C_3`; no step uses the spare factor `1/R_l` of
`psi_l <= C R_l` (item 12). One input i3-cert left unchecked is closed here: the conversion from Y's
`R_mat` to `r_U` is Y 35290 (item 6). Another is closed by a short proof: the local form of the
averaging estimate, Lemma 4.1 (item 4).

| Item | Verdict |
|---|---|
| 1. Definitions 4.1-4.3 | 4.1, 4.2 HOLD; 4.3 HOLDS-WITH-REPAIR: move list incomplete (Y 76686-76688), "admitted" must read fail factors |
| 2. Lemma 1, (H4) | HOLDS-WITH-REPAIR: measure form Lemma 1'; (H4) per summand, with indicator removal as an identity |
| 3. F1-F4, (6.2), Lemma 2a | HOLD (one wrong line cite in F2) |
| 4. (AV1), (AV2) local; Lemmas 2, 2b | HOLD given Lemma 4.1, proved here (Y's stencil has an extra layer) |
| 5. Table of 5.2 | (K-ord), (K-shell), (K-core) HOLD; (K-ext) HOLDS for `l = j`; (K-x) not carried at the entrance; (K-col): `c_f` undefined in Y, short repair |
| 6. Lemma 3, (BG), (WM) | HOLD; add `L >= 13` and the floors of Y 35270 to (G1) |
| 7. Lemma 4, `C_3`, "no profile needed" | HOLD |
| 8. Lemma 6, Remark 7.4 | Lemma 6 HOLDS-WITH-REPAIR (the set must include level `l + 1`); Remark 7.4 HOLDS |
| 9. No product over levels or entrances | HOLDS |
| 10. (H5), order of constants | HOLDS-WITH-REPAIR: `C_2 ebar <= 1` explicit, `L_flat` and `c_f` placed, `c_0` renamed |
| 11. T6 not at the entrance; inset-chart Lemma 5.1 | HOLDS; Lemma 5.1 unchanged, Theorem 5.6 is an identity almost everywhere |
| 12. The four cov-x edits | HOLD; `C_2'` also in (H5) |

Defects, ranked by what they break (all repaired or outside the chain to Theorem 9.1):

1. *Local averaging estimate* (item 4). Y's one-step proof reads curvature on `D_C`, a box with an extra
   layer, not on `F(p)`. i3-cert's reason ("`M^l U` reads `U` only in `F(p)`") covers the values, not the
   estimate. Without a repair, Lemma 2 and case A of Lemma 4 lose their hypothesis. Repaired by Lemma 4.1
   (proved): `F(C)` serves as `D_C`.
2. *Lemma 6* (item 8). The set "not a tower holonomy" ignores level `l + 1`, which decides rows and tested
   plaquettes. Repair: add `t = l + 1`, or use Y's interior case `R(p) subset W^{(-2)}`.
3. *(K-col)* (item 5). `c_f` is used once in Y (76670) and never defined. Repair (unproved, short):
   `c_f := 3 sqrt 2 c_0 L^2`. Outside `X` only.
4. *Moves* (item 1). Deletion of a determining plaquette (Y 76686-76688) is missing from (m1)-(m5).
   Affects (c2) of (COV) outside `X`, not Lemma 1.
5. *Lemma 1 form* (item 2). Repaired by Lemma 1'; (H4) needs finite sums and indicator removal
   (Y 77757-77758).
6. *(K-x)* (item 5). Y's `kappa_x` is a clause of the final inset test in the prospective background,
   not carried at the entrance; consistent with cov-x finding 1.
7. *(BG) hypotheses* (item 6): `L >= 13` and the raised floors (Y 35270-35275). Lemma 3 only.
8. *(H5)* (item 10): defect `<= 1` for the conversion; `C_2'` with the cov-x edits; notation `c_0`.
9. *(K-ext) for `l < j`* (item 5): `psi` gets a factor `(1 + Bbar)^{1/2}`; no step uses that case.
10. *Cite* (item 3): the compression identity is Y 63749, 63774-63776, not Y 63798-63801.

## Item 1. Definitions 4.1-4.3

**Definition 4.1: HOLDS.** Y 65417-65422: "The input at a point of a history includes the fields of the
operations still carried by it. A datum plaquette uses the actual determining links and, for a completed
bond, the average of the lower field on its full double block. These values agree with the fields in the
tests by the retained averaging constraints." i3-cert reads "the lower field" as `V_{l-1}`; by the last
sentence the two readings give the same value on the support of the retained deltas, which is the only
place the definition is used. The prospective datum is Y 65486-65487 ("constraints with coarse target
`V_q`") and Y 72259-72265 (other prospective rows keep their old values). Fair.

**Definition 4.2: HOLDS.** The moment "just before the prospective guard is applied" is the moment of
Y 65486-65490: the entering point is fixed on the retained tests and the coarse-target constraints, and
"to remove the preceding guard ... use the separate comparison", so the preceding guard T9 is still
carried (E2). Y 77744-77757 gives the order inside a stage: first the new test `chi_i^{(n+1)}`, the collar
gauge and the approximate test `chi'_j` at `2 delta'_j`, then the removal of the old guard. So T6
(`chi'_j`) is imposed after the entrance and is correctly not in (E). Y 65466-65468 ("After removal and
before integration the collar assignment uses the new positive stage test and the approximate collar
test") is about a later moment, not the entrance. Fair.

**Definition 4.3: HOLDS-WITH-REPAIR (two repairs).** The moves (m1)-(m5) are a fair reading of
Y 65469-65474 and Y 76674-76686. Two things are missing.

1. *The list is not complete.* Y 76686-76688: "If a determining plaquette is deleted, the newly made
   layer uses its own regularity guard." This is a move that changes the region sequence and removes a
   tested plaquette; it is none of (m1)-(m5). Repair: add (m6) "a deletion of a determining plaquette;
   the loops of the newly made layer are supplied by that layer's regularity guard". Lemma 1 does not use
   the list (its proof reads only the iterated-integral form), so Lemma 1 is unaffected. (COV) (c2) is
   affected: a loop crossed by an (m6) move is not "touched only by (m1), (m4)", and its supplier is a
   guard not in the table of 5.2. For rows 628/632/634, not for this check.
2. *"Every test carried equals one" is wrong for a drop-out summand.* Y's term is a finite sum of
   summands from decompositions of unity: the frame sum `1 = |W_4|^{-1} sum_r 1` and the pass/fail split
   `a_r + b_r = m` (Y 63836), drop-outs at a failed test (Y 63856, "it remains live"), and the failed sharp
   indicator "carried as a separate factor" (Y 65449-65450). In a fail summand the factor carried is
   `1 - chi`, so the test `chi` equals zero on its support. Repair: admitted means "every indicator
   factor carried by the summand (pass factors `chi` and fail factors `1 - chi`) equals one, and every
   carried delta constraint holds", with trajectories taken summand by summand. The proofs of
   Corollary 5.2 and Lemma 4 only read the pass factors listed in (E), and (E1)-(E4) are pass factors
   at the entrance of a stage that is being entered (a failed component does not enter the stage), so
   nothing downstream changes. (E5) for other structures is (COV)'s business.

Also not a move but worth one sentence in Definition 4.3: coordinate changes that keep the datum (the
fluctuation coordinates `V'' = e^{i g_k B} V_0`, Y 63858; the framed substitution `V'' = V' V_0`,
Y 78327-78330, "This substitution recovers the same datum"). Points must be read in the original
variables.

## Item 2. Lemma 1 and the hypothesis (H4)

**The induction: HOLDS-WITH-REPAIR (statement form).** As written, "if the incoming term is not zero at
`x_N`" holds when the term is read as the function given at every point by its iterated-integral
formula (then the proof is right as it stands). For a density defined almost everywhere times delta
measures it is not a pointwise statement, and the clause "`x_N` in the support" gives only the closure
of `Ent_N` (a support is closed; `Ent_N` is cut out by strict inequalities). The repair is the form Y
itself uses (Y 78333-78335: "The pushforward
therefore assigns full mass to the set where this indicator is one"):

> **Lemma 1'.** Let `mu_nu` be the (complex) measure of the incoming term at moment `nu`. For every Borel
> set `B` with `B cap Ent_N` empty, `|mu_N|(B) = 0`.

Proof (the same induction). `mu_N(B) = int (1_B chi_N)(f(x, y)) K(x, dy) mu_{N-1}(dx)`, `f` the move,
`K` the kernel, `chi_N` the product of the indicator factors imposed at `N` (the factors carried at
`N - 1` are already in `mu_{N-1}`). If `x` is the end of an admitted trajectory, then either
`chi_N(f(x, y)) = 0` or `f(x, y)` is the end of an admitted trajectory; in both cases
`(1_B chi_N)(f(x, y)) = 0`. By induction `|mu_{N-1}|` is carried by `Ent_{N-1}` (every Borel set disjoint from it
is null), so the integrand vanishes `|mu_{N-1}|`-almost everywhere, and the same bound holds for
`|mu_N| <= |chi_N| f_*(|K| |mu_{N-1}|)`. Base: `mu_0` carries its own indicators. `square`
Measurability of `Ent_N` is never needed, because only Borel sets disjoint from it are measured; the
set `{I != 1}` is Borel (finitely many continuous functions of finitely many links) and, by Theorem 9.1,
disjoint from `Ent_N`. This is what the consumer needs.

**(H4) against Y's operation: HOLDS-WITH-REPAIR.** I read Y 63836-63876 (the operation (0)-(4)) and
Y 77741-77763 (a stop between removal and collar integration). Every step there is one of: insertion of
a finite decomposition of unity (frame sum, pass/fail split), multiplication by an indicator or a delta
(stage tests, `chi_{k,Lambda}`, last-shell test, averaging deltas, collar gauge), integration of
variables against a kernel (stage collar integrations, `V_k` over `Lambda^pr`, gauge averaging by
`prop:averaging-1a-3-3`), replacement of the `V_k`-dependence on the box by mass times the reference law
`frak s_X` (that is (m5)), and **removal of an indicator**: "Remove an old indicator only when it equals
one on the complete chart used for its removal" (Y 77757-77758). Two additions make (H4) cover this:
(a) the term is a finite sum of iterated integrals, Lemma 1' applied per summand (supports of a finite
sum lie in the union); (b) an indicator removal is an identity of measures (Y's rule makes it one), so
it is a step with kernel the identity and the removed indicator still counted at the earlier moment.
Not checked by me: the exponentiation after the main step (Y 63856, "counted separately"; Y 96532). It
is consistent with (H4) as long as it rewrites the density on the support with the indicators kept as
factors; Y does not say otherwise, and i3-cert (Remark 1) already labels the form as read, not rebuilt.

## Item 3. Frame lemmas F1-F4 (Y 1102-1120)

Definitions against Y 1102-1120: the frame inequality (FR), `Ř_j = R(min_{i<=j} theta_i)` with `R(y)` the
smallest power of `L` not below `(log y)^r`, `eps_j = gbar_j p_0(gbar_j) = A_0 theta_j^{-1/2} (log theta_j)^{p_0}`,
`delta_j = (A_1/A_0) eps_j`: all as in i3-cert 2.1. `eta_j = L^{-j}` (Y 593, 8529), so Y's
`eps_i eta_i^2` is i3-cert's `eps_i L^{-2i}`. `delta'_j = g_j A_1 p_1(g_j)` (Y 63858) and the ratio
`delta'_j/eps_j = (A_1/A_0)(log x_j)^{-(p_0 - p_1)}` (Y 63862) are written with the running `x_j`; i3-cert
writes `theta_j`; the same in the run with its own choices (`theta_k = x_k`, Y 63866). `delta'` enters
only (K-col) and Lemma 5b.

**F1: HOLDS.** Checked every inequality. Two facts the proof uses silently, both true: `theta_s <= mu_s + c_5`
(apply (FR) to the index `i* <= s` where the minimum is attained, using `lambda >= 0`), and
`(log mu_l)^r >= 1` so that `R_l < L (log mu_l)^r` (from (T1), `T >= 4`). Both cases and both subcases
give the stated `C_F(n)`; the case `l < s` gives `eps_l/eps_s <= sqrt 2`, used again in Lemma 2a.
The "contains `eps_j/eps_i <= C(1 + (j-i)^{1/2})`" (Y 63876) is right for `j > i` (case `l >= s`).

**F2: HOLDS.** The compression identity is at Y 63776 ("`k_0+1` the last index with `a_{k_0+1} = u_k`")
with `a_i = M Ř_i L^i` (Y 63749) and `u_i = M L^i` (Y 63774); so `Ř_{k_0+1} = L^{k-k_0-1}`. i3-cert cites
Y 63798-63801 for it; the right lines are Y 63749, 63774-63776 (also Y 63876, "`M Ř_{k_♯+1} L^{k_♯+1-k} = M`").
Cite repair only. The bound `n <= 1 + r log_L log t`, the step `mu_l >= t - Bbar n >= t/2` by (T3), and
`log t <= 2 log mu_l` all check.

**F3: HOLDS.** `L_flat^{2(e-1)} <= L_flat^{2 log_L R} = R^{2 log_L L_flat}`; under (LF) the exponent is
below 1, else below 2; then F2. For `e = 0` the claim is trivial. Note that `L_flat < L/2` (Y 63876)
already gives `L_flat^2 < L^2/4`, so the version without (LF) holds with room.

**F4: HOLDS.** `e_l < L^2 (log mu_l)^{2r} eps_l <= L^2 A_0 theta_l^{-1/2} (log theta_l)^{p_0+2r}`, and the
supremum over `t >= gamma^{-2}` tends to 0.

**(6.2) (bound on `K_F`): HOLDS.** Both entries of `C_F(n)` are below `sqrt 2 L^2 (1 + c_5 + Bbar n)^{k_r}`;
`(n+1)^k <= k! binom(n+k, k)` since `k! binom(n+k, k) = (n+1)...(n+k)`. Checked.

**Lemma 2a: HOLDS** (by F1, `eps_{l-1}/eps_l <= sqrt 2`). The conversion `c_0 = pi/2`: for SU(2),
`norm(e^{iF} - 1) = 2 abs(sin(phi/2)) >= (2/pi) abs(phi)` for `abs(phi) <= pi`, and `<= abs(phi)`; HOLDS.

## Item 4. Lemma 2, 2a, 2b and the averaging estimate in local form (i3-cert 2.3, Y 4690-4960)

**(AV1) in local form: HOLDS-WITH-REPAIR.** Y's proof of `prop:nonlinear-average-energy` reads the
curvature on a box `D_C` that is *not* the union of the four corner blocks: "choose a rectangular fine
box `D_C` containing all paths in its four contour averages, with a fixed additional layer ... Enlarge
`D_C` by another fixed layer if needed" (Y 4800-4803, 4815-4816). The estimates
`ne:local-comb-estimate` and `ne:actual-nonlinear-flux` (Y 4808-4813, 4866-4871) are in terms of the
plaquettes of `D_C`. So i3-cert's sentence "the local forms hold because `M^l U` on the four edges of `p`
reads `U` only in `F(p)`" is true of the values and is not, by itself, the local form of the
*estimate*, which reads curvature on `D_C`. Short repair (proved here):

> **Lemma 4.1 (the one-step chart fits in the footprint).** For a coarse plaquette `C`, the box `F(C)`
> (union of the four corner blocks, a lattice box) can serve as `D_C` in Y 4800-4880.
>
> *Proof.* Each contour path of an edge `c = (y, y + L e_mu)` of `C` is a shortest path from `y` to
> `x in B(y)`, the straight segment from `x` to `x + L e_mu in B(y + L e_mu)`, and a shortest path back to
> `y + L e_mu`; a shortest lattice path lies in the coordinate box of its ends, so every path lies in
> `F(C)`. Root the coordinate comb at the initial vertex of `C`; each comb path is coordinatewise
> monotone, so it lies in `F(C)`. In the loop "comb path, edge `b`, comb path back", each interchange of
> two consecutive unit steps replaces one vertex by the fourth corner of a unit square whose other three
> corners are on the path; that corner has each coordinate equal to a coordinate of those three, so it
> stays in the box, and so does the inserted plaquette. Hence the integers `n_{b,p}` of Y 4830-4834 are
> supported on plaquettes of `F(C)`, and every quantity in Y 4806-4871 is read in `F(C)`. `square`

With Lemma 4.1, (AV1) of i3-cert 2.3 holds with `D(p) = F(p)` read on the level-(l-1) lattice and with
Y's constants `eps_L, C_L` (the row sum `L^2`, Y 4756-4758, gives the leading term). Without it, every
footprint in i3-cert and cov-x must be enlarged by a fixed number of sites at each level, at most
`c L^l/(L - 1)` bare units in total; the shell widths (`7 a_i`, `u_{i+1} = M L^{i+1}`) absorb that, but
the containment `F(P) subset Lay_j` of (G2) would then need `dist > 2 L^q + c L^q/(L-1)`.

**(AV2) in local form: HOLDS** (given Lemma 4.1). Y's proof (Y 4927-4948) is the recurrence
`eps_{j+1} <= L^2 eps_j (1 + C_L eps_j / L^2)` with `sum_{j<k} eps_j <= 2 alpha/(L^2 - 1)` and
`alpha_L` chosen with `exp[2 C_L alpha_L/(L^2(L^2-1))] < 2` and `2 alpha_L < eps_L`. In local form put
`eps_j(p) := max |F_q(M^j U)|` over level-j plaquettes `q` all of whose corners lie in `F(p)`. The blocks
are aligned and nested (Y 62001, "all partitions are nested"), so for such `q` at level `j+1`, `F(q)`
consists of order-(j+1) blocks inside `F(p)`, its level-j plaquettes are again of this kind, and
Lemma 4.1 gives the local one-step bound. The recurrence and the induction "first possible failure is
impossible" go through word for word. Constant: `abs(F_p(M^l U)) <= 2 alpha`, the one i3-cert uses.

**Lemma 2: HOLDS** (given (AV2) local and (s1); see cov-x finding 4 on (s1) at a mixed loop, not
checked here). `M^l = M o M^{l-1}` on every edge, so `V(dp) = (M^l U)(dp)`; `norm(e^{iF} - 1) <= abs(F)`.

**Lemma 2a: HOLDS** (item 3).

**Lemma 2b: HOLDS for the table as written, under (5.1).** If `l <= k_0`, `e = 0`; else F3. The reading
`2 psi_l eps_l <= C_2 e_l` uses `e <= (l - k_0)_+` from (5.1); whether (5.1) holds for every kind is
item 5 below, and the (K-wall) kind of cov-x is item 10 (12 in the row's numbering of the added item).

## Item 5. The table of 5.2 against the lines it names

| Kind | Y lines | Verdict |
|---|---|---|
| (K-ord) | Y 134113-134117 | **HOLDS.** "The full bare averaging blocks of a level-k plaquette with a corner in such a density cube lie in its one-layer enlargement. The positive density test gives bare curvature less than `eps_k eta_k^2` there", `eta_k = L^{-k}`. `psi = c_0` (Y itself writes `2 eps_k` at Y 134118-134119, i.e. without the conversion; `c_0` is the safe reading). The (c3) question at a mixed loop is cov-x finding 4, not checked here. |
| (K-shell) | Y 63876 | **HOLDS.** "`(1 - beta_s(1 - 2^{-(j-i+1)})) eps_i eta_i^2` on that shell ... On the shell `i` the factor is `L_flat^{2(i-k_♯-1)_+}`", Y's `k_♯` = i3-cert's `k_0` ("where the level is denoted `k_0`", same line). Bare plaquettes wholly in the shell: Y 78316-78318. |
| (K-ext) | Y 63876 | **HOLDS for a plaquette of level `l = j` (and `l = j + 1` through Lemma 2a); the `psi` column is wrong for `l < j`, unused.** Y: `(1 - beta_s/2) c_l L_flat^{2e} eps_j eta_j^2`, `c_l = 3` adjacent to `Omega_k` at the last stage, else 1; `e = 0` for `j <= k_♯`, `e = (j-l-1)_+` on `Omega_l minus Omega_{l+1}`, `e = j - k_♯ - 1` between the shells and `Omega_{k_♯+1}`. So `e <= (j - k_0 - 1)_+` is right. The bound is in the scale `j`; for a tested plaquette of level `l < j` it gives `psi_l = 3 c_0 L_flat^{2e} (eps_j/eps_l) L^{-2(j-l)} <= 6 c_0 (1 + Bbar)^{1/2}/L_flat^2` (F1 and `L_flat < L/2`), bounded but with a factor `(1 + Bbar)^{1/2}` that `A_L` does not have. No step of i3-cert 5.4 or of cov-x's list uses (K-ext) for `l < j`; if one does, put `(1 + Bbar)^{1/2}` into `A_L`. |
| (K-x) | Y 64308-64313 | **The threshold HOLDS; the description does not.** Y: `F_j = L_flat^{2(j-k_0-1)}`, `kappa_x` at `(1 - 3 beta_s/4) F_j eps_j L^{-2j}`. But Y's `kappa_x` tests "the deep exterior plaquettes straddling `dZ''_m`" in an *inset split*, "in the prospective background". It is a clause of the final inset test, imposed after the entrance, like T6. It is not "a crossing clause at the prepared face of the stage of level `j`" carried by T9. So (K-x) is not available at the entrance unless the operation carries crossing tests (T3). This agrees with cov-x finding 1 (not checked here). |
| (K-col) | Y 65436-65455, 76669-76670 | **Gap (short).** The factor `c_f L_flat^{2(q-k_0)_+}` is asserted at Y 76669-76670; `c_f` occurs nowhere else in Y (grep: one hit) and is never defined or derived. So `A_L` contains an undefined constant. Repair (unproved here, short): the retained stage test `chi_i^{(n+1)}` gives the (K-shell)/(K-ext) bound on the reconstructed field, at most `3 sqrt 2 c_0 L^2 L_flat^{2(l-k_0-1)_+} eps_l L^{-2l}` with Lemma 2a; the four collar links within `2 delta'_{j'}` change the loop by at most `8 delta'_{j'}`; so `c_f := 3 sqrt 2 c_0 L^2` works with the exponent `(l - k_0 - 1)_+`, and Y's `(l - k_0)_+` is a safe overestimate. It is used only for departures of other structures ((E5), row 632), not at the entrance of `X`. |
| (K-core) | Y 65434-65435, 76680-76685, 63876 item (4) | **HOLDS.** The cut-off `chi(Lambda^pr) = 1{abs(log V') < M_0 eps_k}` (Y 63870) and Y 76682-76685 ("comparing the four links with the reference and using the retained cutoff gives the bound `C(M) eps_i`"). `C(M)` is not computed in Y; i3-cert's `C(M, M_0)/2` is a name, not a number. Fine as a fixed constant chosen before `gamma`. |

**(5.1): HOLDS for the kinds as used** (all kinds with `l = j`, and `l = j + 1` via Lemma 2a), with `c_f`
defined as above. The exponent `e <= (l - k_0)_+` and F3 need `l <= k` for the operation that made the
shell; true, since a stage test of an operation of level `k` reads levels `<= k` only.

**Norm convention (minor).** Y's Lie-algebra norm is `<X, Y> = (1/2) Tr(XY)` (Y 4699-4701), so
`abs(F) = abs(phi)`; the test norm `abs(dU - 1)` is read as the operator norm. If Y's test norm were
Hilbert-Schmidt, `c_0` would change by `sqrt 2`. It changes constants only.

## Item 6. Lemma 3 and section 6.1: the hypotheses of (BG) and (WM)

**(BG), `bgc:proper-background` (Y 35634-35646): quotation HOLDS; two hypotheses to add.** The quotation
is exact. Hypotheses i3-cert checks: real datum, ordinary and mixed test holonomies (Definition T, no
pinch tests since no inward row is kept; Y 12456-12458: "On a determining set in force all inward rows
have been removed, so only tested plaquettes remain"), size `eps = B ebar(gamma) <= a_1`. Correct. Missing
from 6.1: the section of (BG) works with `L >= 13` (Y 35270, "Use `L >= 13`, and the aligned separated
geometry of `mb:datum-descent-critical-ascent`; increase its floors below when choosing a fixed local
regularity patch"). So (G1) must include the floors of that geometry as raised at Y 35270-35275, not
only those of `hi:real-datum-profile`, and `L >= 13`. Both are fixed before `gamma`; neither changes a
constant of i3-cert.

**The conversion `R_mat` to `r_U` (i3-cert: "I did not check"): HOLDS, closed here.** Y 35277-35291:
`R(U) = max{ sup_p eta^{-2} L(p)^2 abs(dU(p) - 1), sup_b L(b)^3 abs(J(U)(b)) }`, which is `sup_x r_U(x)` of
`hi:real-datum-profile` (Y 15325-15330, same two readouts), and `R(U) <= R_mat(U)` (`bgc:matrix-current`,
Y 35290). So `U(V)` is regular at radius `a_c` as soon as `C_B B ebar(gamma) <= a_c`, the condition
Lemma 3 states. No extra factor.

**(WM) (Y 12471-12503, 15317-15338, 35615-35627): HOLDS as quoted.** `P` is Y's
`tilde v_delta` (`mb:datum-profile`), the distance to a tested plaquette is the minimum over its corners
(Y 12454-12455), `r_U <= 5 K P` with `e^{delta R} = sqrt 2` (Y 35617-35626), the fixed displacement
factor is Y's (Y 35625-35626), and "No maximum has to be attained" is Y 12492-12494. The pillar scale
`xi = L^t` in `Lay_t` is a reading of Y 12394-12401 ("at a seam the adjacent scales differ by `L`");
Y does not write `L^t` at those lines. Acceptable.

**Lemma D: HOLDS.** Checked both directions and the count of crossed layers (`l' - 1 - s >= l - s - 2`,
`s - 1 - l' >= s - l - 1`). `kappa = delta c_B rho` is positive and fixed: `delta = (log 2)/(2R)`,
`R = 20 L sigma`, `rho >= L^2 sigma`, so `kappa >= c_B L log 2/40`.

**Lemma 3: HOLDS** (given (BG), (WM) and the two added hypotheses). One application of (WM) to one
datum; `P(x) <= B e_s K_F` by Lemma D and F1.

## Item 7. Lemma 4, the exact averaging step, and `C_3`

**Lemma 4: HOLDS** (given Corollary 5.2, (G2), (AV1) local with Lemma 4.1 of item 4). I checked each level.
`l < j`, `l = j`, `l = q + 1`, `l > q + 1`: the tested sets, the row sets and the double blocks read are
unchanged (`Gamma_l` depends on `Omega_l, Omega_{l+1}` only, so only `Gamma_j` and `Gamma_q` move). `l = q`,
case A: every edge of `P` either touches `K` and has no end in the old `Omega_q`, hence is a new row with
`V_q(c) = M(V_j)(c)` by (E1), or is a prospective completed edge whose blocks lie in `Lay'_j` (both
`Omega_q` and `K` are unions of order-q blocks), so its value is `M(V_j)(c)` with old values. Then (AV1)
with `eps(W; D(P)) <= c_0 C_2 e_j <= min(eps_L, L^2/C_L)` (H5) gives `abs(F_P) <= 2 L^2 c_0 C_2 e_j`, and
F1 with `n = 1` gives `e_j <= C_F(1) e_q`. Case B: the old loop is the new loop, edge by edge. So
`C_3 = 2 c_0 L^2 C_F(1) C_2` is right, and `C_3 >= C_2`.

Two remarks. (a) Case A needs that every level-j plaquette of the stencil `D(P)` is an old tested
plaquette (corners in `Lay_j`). This is true for `D(P) = F(P)`; with Y's enlarged `D_C` (an extra layer)
it would need (G2) with a larger margin. Lemma 4.1 of item 4 removes the issue. (b) Y 64093-64101 is
the same argument: "the averaging blocks of a newly tested plaquette are in the preceding member of
level `j` ... the exact one-step average gives the coarse bound"; for level-m plaquettes with a corner
in the old `Omega_m` Y uses the carried density cube instead (Y 64093-64097), and i3-cert uses the old
loop with Corollary 5.2. Both work.

**The finding "(i) and (ii) do not need the layer profile": HOLDS.** The proof of Lemma 4 cites
Corollary 5.2, (G2), (G3), (AV1), (E1) and Definition T, and no line of section 6. Lemma 6 adds only
the trichotomy. Y's own route (Y 65536-65556, through `U_in` and the profile) is longer and gives a
larger constant, as Remark 7.2 says.

## Item 8. Lemma 6 and Remark 7.4

**Lemma 6: HOLDS-WITH-REPAIR (the set that defines "not a tower holonomy").** i3-cert defines it as
"footprint and double blocks of its edges lie where `T_l = T_{l-1} =` everything". Which edges of a
level-l plaquette are rows also depends on level `l + 1` (rows have no endpoint in `J_{l+1}`), and which
plaquettes are tested depends on `J_{l+1}` too. If a corner of `p` lies in `Omega'_{l+1}` but not in
`T_{l+1}`, `p` is tested in the joined sequence and not in the global one, and the proof's sentence
"Definition T gives the same edges with the same values" fails. Repair: require `J_t = Omega'_t` on
`F(p)` for `t = l - 1, l, l + 1`; or use Y's own interior case `R(p) subset W^{(-2)}` (Y 13095-13100,
13114-13116, "In the interior case all determining rows used by the test are ambient rows"), with Y's
dichotomy (Y 13099-13112) proving that every other joined test is a collar test (trivial or a lifted
level-`j_a` holonomy, Y 13117-13126). With either, the proof is the two lines of i3-cert. cov-x
section 7 says it gives a set definition from Y 13095-13130; I did not check it (row 633).

**Remark 7.4: HOLDS.** The reason that matters is the first one: Lemma 4 is a statement about the
global datum `D'(x)`, whose rows are rows of the global sequences, so the lifted rows of the localized
tower are not edges of any plaquette it bounds. The geometric sentence (stencils of case A within `3L^q/2`
of `K`, `K` two level-m cells inside `X`, tower within `3 M_1 L^q` of `X^c`) is consistent with
`O_m = H_m^{[8 a_m]}`, `X = H_m^{[10 a_m]}` and `a_m = M Ř_m L^m >> 3 M_1 L^m`; it is not needed for Lemma 4.

## Item 9. Section 9.2: no constant is a product over levels or over entrances

**HOLDS, of the written proofs.** I went through every estimate in sections 3 to 9.
- Lemma 1 (and Lemma 1' of item 2) is an induction on sets and null sets; no constant.
- Corollary 5.2 takes its bound at each plaquette from one test at one moment, with a threshold written
  in the operation; the loop's *value* is carried to `x_N` by (c2) (or (c2')). No bound obtained at an
  earlier entrance is fed into an estimate. The background a test reads at an earlier moment exists
  under a ceiling on `gamma` that is uniform (`C_3 ebar(gamma) <= a_1`), not under an earlier
  certificate's constant.
- Lemma 4 is one averaging step; Lemma 3 is one application of (WM), with level sums bounded by the
  convergent series `K_F` (and `K_G` in Lemma 5).
- The one literal product over levels is the relaxation `L_flat^{2e}`, one factor `L_flat^2` per
  overlapping compressed level. It is bounded by F3 (`e - 1 <= log_L R_{k_0+1}`), and absorbed into
  `e_l = R_l^2 eps_l` with the fixed constant `2^r L L_flat^2`. So it is not a constant that grows with the
  number of levels. Likewise (AV2)'s constant 2 is uniform in the depth (Y 4927-4948).
The chain `C_2 -> C_3 -> K_w K_F C_3 -> C_5, C_6` has fixed length, restarted at `C_2` at each entrance.
This matches Y 65586-65591.

## Item 10. (H5) and the order of constants (Y 72931)

**HOLDS-WITH-REPAIR (three additions).** Y's order (Y 72931-72932):
`(r, p_0, p_1, q, kappa_0, beta_s, theta_s, theta_c) < L < (M_1, R_1) < ... < M < sigma_* < a_Lambda <
(A_1, A_0, C_0, C_1, alpha_1, alpha_0, E_0, M_0, alpha', B) < (lambda, c_5, Bbar) < gamma`.
`C_2, C_3` depend on `(L, L_flat, r, M, M_0, c_f)` and `(Bbar, c_5)`; `ebar(gamma)` on `(L, A_0, p_0, r)`;
`alpha_L, eps_L, C_L` on `L` (Y 4704). The floors (T1)-(T3) on `T = gamma^{-2}` depend on
`(c_5, Bbar, r, p_0, L)`. All precede `gamma`, so both conditions of (H5) and the floors are ceilings on
`gamma`, satisfiable because `ebar(gamma) -> 0`. Additions:
1. `L_flat` and `c_f` are not in Y's display. `L_flat` is "chosen together with `L`" (Y 63876), so it
   sits with `L`. `c_f` is undefined in Y (item 5); with the repair there it is a function of `L`.
2. The conversion `abs(F) <= c_0 . defect` needs defect `<= 1`, i.e. `C_2 ebar(gamma) <= 1`. It follows
   from the second condition of (H5) only if `eps_L <= c_0`; state it as a third condition, or note that
   Y's `eps_L` may be taken `<= 1`. With the cov-x edit, every `C_2` in (H5) becomes `C_2'`.
3. Notation clash: i3-cert's `c_0 := pi/2` is not Y's `c_0` (`= 11 N^2 log L/(12 pi^2)`, Y 1681), which
   fixes `lambda = c_0/4` (Y 72935). Rename i3-cert's (e.g. `c_pi`). Not a mathematical error.
Lemma 3 adds the ceilings `B ebar <= a_1`, `C_B B ebar <= a_c` with `B = C_2, C_3`; again ceilings on
`gamma`, not needed for Theorem 9.1.

## Item 11. T6 at the entrance, and Lemma 5.1 of `library/inset-chart.md`

**The finding HOLDS.** T6 (`chi'_j` at `2 delta'_j`, centre `S_X = M^j U^+`) is imposed by stage `n + 1`
after the new localized test (Y 77744-77746: "Stage `n+1` first imposes the localized regularity test
`chi_i^{(n+1)}`, the collar gauge and the approximate closeness test `chi'_j` at `2 delta'_j`"), and its
centre needs `U^+`, which needs the certificate. No step of i3-cert reads T6, T8, T11, T12 or T13; the
level-j collar rows are supplied by T9's exterior clauses (5.4 item 4; cov-x P5a).

**Lemma 5.1 of inset-chart needs no change as a lemma** (it is pure logic, checked). Its use in
Theorem 5.6 (`P = T9 T10 T11 T12 T13`, `A = T1 ... T5`, `Q` the kept factors, which include T6, T7, T8)
needs (F1): `P Q != 0` implies `I = 1`. Every factor of `P` and `Q` is a factor of the term or an extra
indicator, so `{P Q != 0}` lies in the support of the incoming term, which lies in `Ent_N` by Lemma 1;
and `I = 1` on `Ent_N` uses none of T6, T8, T11-T13. So (F1-Y) holds and is not circular. One wording
repair in inset-chart: with Lemma 1' (item 2), (F1) holds `|mu|`-almost everywhere rather than at every
point, so the identity `P Q = I Q` of Theorem 5.6 is an identity of measures (equality almost
everywhere for the incoming measure). That is all an integral uses; say so in 5.1 or 5.6. If the term is
read as the function given at every point by its iterated-integral formula, the pointwise form holds too.

## Item 12 (the item added 2026-11-10). Theorem 9.1 with the four edits of cov-x

I take the four edits as stated in cov-x sections 0 and 8 and do not check cov-x's proofs (row 633).

1. **(c2') for (c2): HOLDS.** The proof of Corollary 5.2 uses (c2) only to say that the loop at `x_N` is
   the loop the supplier bounds; (c2') says exactly that (cov-x Lemma 3.2). No other step of i3-cert uses
   "`p` is a tested plaquette of `D(x_nu')` for every `nu'`". Section 9.2's "the value is carried by (c2)"
   reads the same with (c2').
2. **One supplier for items 3 and 5 (the guard before the promotion): HOLDS for i3-cert.** i3-cert's
   proofs use 5.4 items 3 and 5 only through (COV). Replacing the supplier changes `psi` to
   `2 sqrt 2 c_0 L^2 L_flat^{2(l-k_0-2)_+}` (cov-x table, P4), which is within (5.1) with `e <= (l - k_0)_+`.
   This agrees with item 5 above: the (K-x) clause is not carried at the entrance.
3. **The seventh kind (K-wall), `psi_j` of order `R_j^2`: HOLDS for Theorem 9.1.** (5.1) fails for this
   kind, as cov-x says. It is a coarse supplier (bounds on level-l' plaquettes, then depth `j - l'`
   averages), so Lemma 2 is replaced by cov-x Lemma 3.2 for it; (AV2) on the level-l' lattice is the
   same corollary (Y 4905-4960 holds for "every lattice admitting `k` block averages"), and in local form
   it needs Lemma 4.1 of item 4 again.
4. **`C_2' = max(C_2, 6 . 4^r)`: HOLDS,** provided it is used in (H5) as well (both conditions), so that
   the allowance of (K-wall), `3 . 4^r e_j <= alpha_L`, is admitted.

**Does any step of i3-cert use `psi_l <= C R_l` in a way `C_2' e_l` does not replace? No.** The spare
factor `1/R_l` of Lemma 2b is used nowhere: Corollary 5.2, Lemma 4 (with `eps(W; D(P)) <= c_0 C_2' e_j`,
including the P5b plaquettes of the stencil), (H5), Lemma 3 (`B = C_2'`, `C_3`) and Lemma 5 all read the
bound `C e_l` only. The claim `psi_l <= C (log theta_l)^r` of Y 65479-65480 is not consumed in i3-cert.
So Theorem 9.1 holds with the four edits and `C_3 = 2 c_0 L^2 C_F(1) C_2'`, given (COV) in the cov-x form.

## What stays open

- (COV) itself (rows 628, 632, 633; not attacked here).
- The (K-col) constant `c_f` (repair proposed, unproved; outside `X` only).
- Read and not rebuilt, as in i3-cert: (G1)-(G3), the thresholds of the tests, the trichotomy (R1), the
  exponentiation step of Y's operation (item 2).

For row 634 (`i3-repairs`): the repairs to carry into `library/i3-cert.md` are Lemma 4.1 (item 4),
Lemma 1' (item 2), (m6) and the fail-factor reading (item 1), the level-`l + 1` condition in Lemma 6
(item 8), `L >= 13` and the floors of Y 35270 in (G1) (item 6), the (K-x) and (K-col) rows of the table
(item 5), the additions to (H5) (item 10), `C_2'` (item 12), and the cite of F2 (item 3).

RESULT: Theorem 9.1 of i3-cert HOLDS given (COV), also with the four cov-x edits (C_2' = max(C_2, 6.4^r) in Lemma 2b, (H5) and C_3; no step uses the spare 1/R_l); repairs, none changing the statement: local averaging needs Lemma 4.1 (proved here: Y's stencil has an extra layer, F(C) suffices), Lemma 1 in measure form, move (m6) missing from Definition 4.3, Lemma 6's set must include level l+1, (K-x) not carried at the entrance, c_f undefined in Y (short repair, outside X), L >= 13 for (BG); open: (COV) and c_f.
