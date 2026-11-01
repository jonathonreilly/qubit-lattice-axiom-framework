lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T11:15Z

# tail-two-step-c: blind two-step kill test of the tail induction, independent side

Pinned at commit c0e57d701 (working tree of branch claude/ym4d-hard-route). In progress; written section by section. Nothing here is a status claim.

Provenance: Anthropic claude-opus-5-5, max effort, Mac mini worker; working tree at `c0e57d701`. Same model as the attempt, so this is not independent in model and it is not an audit. Side: independent, blind to `library/tail-two-step.md`. All references below are to `parts/hard-core--independent.md` unless named.

## 0. What was read

Read: `FINISH.md`, `GOAL.md`, of `parts/hard-core--independent.md` the state of attack, Obligations, Requests, Texts 3.1 to 3.3, 4.5k, the head of 4.6, 4.7, 4.8, 6.0 to 6.4f. Later sections of this file name anything further. Not read: `library/tail-two-step.md`, the mapped file, any gate, any other library file except the four the firewall allows.

## 1. Frozen definitions at `c0e57d701`

| Name | Definition used here | Where |
|---|---|---|
| radius | rho_P(l) = min(rho_e, c' g exp(c_1 d(l, P))), d read off Rg(P) | (TAIL), Text 4.7 |
| norm | ||G||_P = sum_{alpha, Xi} prod_l rho_P(l)^{alpha_l} exp(c_3 tau_k(P; supp alpha, Xi)) |G_{alpha, Xi}| | (TAIL) |
| C growth | |C_k(Y; V)| <= cc_k exp(-kappa (|Y| - C_0)_+) (t_Y^2 + t_Y^3), and in the norm t_Y becomes max(t_Y, t_fl), t_fl = C_s L^{-2} c' Vol(Y)^{1/2} | (TAIL) |
| chart | b = 2^{-1/2} g P x, x = xi + s_tot, s_tot = s(W, xi') + s_J(W); at fixed x, V reads W only within R_P | (2C), (LOCAL) |
| near labels | NV(Z): labels a link of N_1(Z) reads through the chart; unsplit, law mu_i with the cut S_i = 1[|x_i| <= p_2] | (R2), (3S) |
| rough set | Rg gains image(N_1(Z)) + B(R_P^+), R_P^+ = R_P + rho_P / L + 1 | (R2) |
| group | components of: NV meet or N_1(Z) touch; U_q, A_q; tt_k = C(L, M) g_k^{-3} (bb_k + cc_k) | (GROUP) |
| far noise | alpha_q(c) = 32 C_row g / min rho_{U_q}(l); a_q(c) = alpha_q(c) max_i (|xi_i| + 1); Lg_q = { a_q > 1/4 } | Lemma 4.7j |
| linear term | term (2) = (N_good^Z / N_good) E^Z_W[e^{e_k} - 1] | (ONE) |
| contraction | ||Gamma - Gamma_1(0) - beta(e)(F_0^*(w), F_0^*(w))||_{Y'} <= C sup||e|| (t_#^3 + t_#^2 (D_e / L)^a) + ||Rem_B||_{Y'} | (BANACH) |
| recursion | bb_{k+1}, cc_{k+1} as displayed after "The recursion, with the weighted t" | Text 4.7 |
