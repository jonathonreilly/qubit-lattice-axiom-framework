lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-10T16:13Z

# i3-cert-check (FINISH row 630): line check of `library/i3-cert.md`

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
`x_N`" is a pointwise statement about an object that is a density defined almost everywhere times delta
measures, and "`x_N` in the support" gives only the closure of `Ent_N` (a support is closed; `Ent_N` is
cut out by strict inequalities). The repair is the form Y itself uses (Y 78333-78335: "The pushforward
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
