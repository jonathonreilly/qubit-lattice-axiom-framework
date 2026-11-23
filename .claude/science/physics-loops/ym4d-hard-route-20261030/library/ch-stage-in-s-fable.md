lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-24T09:44Z

# CH stage spaces inside the chart class S (row 1448, `ch-stage-in-s-fable`)

Provenance: Claude Fable 5.2, medium effort, Mac mini worker, pinned at b47e86bbb. Author only, one reading,
unchecked. Sources credited: T. Balaban (CMP 99b, 109, 116 via quotation, 119, 122a, 122b), the Sussman-Alpoge
complete account (with Claude and Codex), and this lane's rows 1444 (`cm-o3-fable.md`) and `ch-r2.md`.

## 0. Plan and statement (written 2026-11-23T21:44Z, before any reading of the sources)

Statement to decide (row 1448): for every admitted history and every piece of the old-terms step, the stage
spaces U~^c_k(Y_4, a~_0, a~_1) of CMP 122a (1.64)-(1.69), and the reached link backgrounds of the three links of
CMP 122b (1.61)-(1.63), lie in the chart class S of 4.5:thm-chart-existence (CA-I 12945-13017), with radii fixed
before M and the M-reading ceiling falling on alpha_0 only. Either prove it, or exhibit a stage-space clause on
Omega''_{k_0+1} minus Omega_{k_0+1} whose constant exceeds a_0^S for every admitted alpha_0.

Plan, one step per response, each appended here before the next:
1. Read the inputs named by the row (cm-o3-fable, ch-r2 with (P4'), prior/ch, CH rows of open-registry and
   open-core). Record what is already on file.
2. Print the chart class S (CA-I 12945-13017) and its order of choice (a_0^S, alpha_0, M).
3. Print the stage spaces, CMP 122a (1.64)-(1.69), and the account's version; list every clause with its constant.
4. Print the three links, CMP 122b (1.61)-(1.63), and the reached backgrounds.
5. Clause-by-clause comparison: stage clause constant against the class constant, in the account's order of choice.
6. Verdict, labels (proved / sketched / guessed), next two rows.

Status log (times from date -u):
- 2026-11-23T21:44Z file created.

## 1. What is on file (step 1, written 2026-11-23T21:46Z)

Read: FINISH rows 1444, 1447, 1448 and the rule sections; `cm-o3-fable.md` (whole); `ch-r2.md` (whole);
`prior/ch.md` (stage-entry table L68-87 and hits for "stage"); registry rows CH (L17), CH4-AUX (L23);
`open-core.md` L551. Account: CA-I 12936-13085 (class S and its inclusion proof), 49497-49700
(`4.14:rem-supply-scope` with proof). CA-I and CA-II are the copies fetched for row 1444 at the pinned upstream
commit, in my scratch folder /tmp/cm-o3-fable-sa.

1.1 **The class S (CA-I 12936-12971).** Radii a_0, a_1, a_gamma "depending on d and L only". (S1) U = e^{i eta a} U_r,
U_r G-valued, and for every level j and every cube of side 12 M-frak in level-j units a G-valued gauge u with
U_r^u = e^{i eta A}, l_j |A| < a_0, l_j^2 |grad A| < a_0. (S2) N_{U_r}(a) < a_1. (S3) |J|_{(-3)} < a_gamma. No
relation between J and U, no condition (iv), no auxiliary configuration U_{p,X}, J_{p,X}.
So of the seven stage entries (CA-I 49597-49600) the class reads at most: the gauge clause of the real factor
(S1), the twist entries 6-7 (S2), the current entry 3 (S3). Entries 1, 2, 4, 5 are not read by S. This is
`ch-r2.md` Proposition F (L109-122) applied to the class.

1.2 **The account's own inclusion (CA-I 13000-13085) is for CMP 109 (i)-(iii) on X, one scale.** Ceilings
c_12 L M B^109 alpha_0 <= a_0, alpha_1 <= a_1, gamma_0 <= a_gamma; floors 17 M_1 <= L M, 17 M_1 <= c_12 L M,
c_12 L >= 2. Its proof puts every cube of side <= 17 M_1 l_j in one cube of side c_12 L M of CMP 109 (1.12) and uses
l_j <= 1. It does not treat the layered conditions of CMP 119 (2.34)-(2.39) or the stage spaces of CMP 122a.

1.3 **The tool already in the account: the powers of L_0 are paid by R_n (CA-I 49543-49700,
`4.14:rem-supply-scope` (v), written for the operator theorem 4.14, not for S).** The stage bound is
(coefficient <= 1) x L_0^{2e} x (bracket of seven entries with alpha_{0,n} or alpha_{1,n}), with e = max(0, m - k_0),
n = m in (1.64); e = j - m, n = j in (1.66); e = 0 in (1.68). Always 0 <= e <= n - k_0 <= N_0 (4.14:eq-supply-scope-1)
and L_0^{2e} <= c_1 R_n, c_1 = 1 + c(beta_0) L (L+1) (4.14:eq-supply-scope-2, from lem-integer-power-bound /
lem-top-power-bound). The account concludes: the gauge constant supplied on a cube in layer n is at most
c_1 R_n alpha_{0,n}, the radii are read at c_1 R_n alpha_{.,n}, and these are "one-sided conditions ... on each
layer's own coupling", imposed after L and M. So the candidate obstruction of the row (a constant on
Omega''_{k_0+1} minus Omega_{k_0+1} above a_0^S for every admitted alpha_0) has to beat this: the power is at most
polylogarithmic in g_n and alpha_{0,n} is g_n times a polylogarithm, so the product tends to 0 with the coupling.
What rem-supply-scope does NOT do: (a) the class S of 4.5 (it serves 4.14:eq-real-backgrounds); (b) the match of
levels between the stage layers and the tower of the chart at each link (`ch-r2.md` (P4')); (c) the reached
link backgrounds.

1.4 **Rule 0a matches for the row's statement.** `ch-r2.md` (P4), (P4') L148, L188-198 (level match, open);
`cm-o3-fable.md` 2.4 last paragraph and Section 4 item 2 (this row); `prior/ch.md` L79-87 (stage weight on
every entry); CA-I `4.14:rem-supply-scope` (v). No file found proving stage space inside S.
