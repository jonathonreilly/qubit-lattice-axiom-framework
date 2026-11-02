lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T20:25Z

# Gate: `library/rarity-fresh-x.md` (queue item 59, `rarity-x-gate`)

Status: in progress. Sections are written as they finish.

## Provenance

Gate by anthropic/claude-opus-5-5, effort high, on the Mac mini worker, at commit `0e8a5a4e7`. The note under test was written by OpenAI Codex (GPT-6), so this read is cross-provider, but it is one read, not an audit, and it grants no status. Mapped-side firewall of `FINISH.md` obeyed. Sections 1 to 4 of the note (statements and proofs) were read and checked before its Section 5 (its own verdicts).

## Verdicts on `library/rarity-fresh-x.md`, one per step

Each step below was redone by hand from the note's own text and the sources it quotes. No run was used; `checks/gate_rx/` holds a README only.

| Step | Verdict | Note |
|---|---|---|
| Sect. 1, consumer contract (RAR^1, RAR^ch, DM's product form, rate translation) | ADVANCE | Quotes match `parts/upper-chain.md:182–183`. Cell to brick: `upper-chain.md:178` declares a cell non-quiet iff its brick is, and 7w/3 separation gives brick separation > 12 t_0, so the injection holds. Nonregular (flux > T_2 >= 2A_f T >= 2T) lies inside the type-II test. |
| Sect. 2, exact positive partition W_x(D) | ADVANCE | A finite sum of indicators of disjoint events, which is trivially exact. It is conditional on the predicates being measurable and defined, and the note says so (quiet's Lift_B^D existence and selection are inputs per `upper-chain.md:178`). Type-II "labelled or above 2T" is a.s. the same as "labelled", since chi = 1 on [2T, pi] (mapped Text 5.2). |
| Sect. 2, bounded-degree graph D_0(Theta) | unchecked, as labelled | Plausible: D_0 ~ C L^4 with patch ranges fixed. Forced co-activity (type-II at l+1 on B^{++} makes the type-I brick at l non-quiet; a Haar parent forced by labelled children) only links tests with overlapping patches, so it stays inside one component. |
| Sect. 2, (CD) | gap, as labelled; no counterexample | Well-posed. The zero-mass clause is part of it. I looked for a structural refutation (D3) and found none. Strictly stronger than RAR, as the note says. |
| Sect. 3, the base measure nu is x-free, and the history law is proportional to exp(-tA) dnu | ADVANCE | chi, T = a_*/L^2, T_2 and the maps are fixed before x (mapped `:991`). A depends on the finest field only, so Haar parents and labels carry no action. |
| (3.1) zero-temperature limit | ADVANCE | Two-sided bound b_eps e^{-t(m+eps)} <= W_t <= nu(D) e^{-tm}; needs only 0 < nu(D) < infinity and A bounded below, both true. |
| (CD) at all large t forces (SEP) | ADVANCE (implication) | Correct given x_l(t)/t -> 1 at fixed depth, or with liminf otherwise. The all-large-x uniformity is not an extra choice for the DM replacement, since DM is stated for every x >= x_*. Polynomial prefactors drop out. |
| (3.1a), (3.2) | ADVANCE | Algebra checked. |
| "First attempted proof of (SEP)" failing at the class-chart boundary | CORRECT-NO-ADVANCE | The missing inference is real: a Hessian bound near the class branch says nothing about ess inf A on a sector whose near-minimisers lie on another label or Haar branch. But the r_(t,out) wording mixes the finite-t mass with the t -> infinity statement. (SEP) is purely variational; see D1. |
| (3.3) F'' = E[S_vv] - Var(S_v) | ADVANCE | Quotient rule redone: d E[f]/dv = E[f_v] - Cov(f, S_v), then f = S_v. |
| Two-branch calculation | ADVANCE (as a counterexample to the generic inference only) | F_t = t(v^2+a^2)/2 - log(2 cosh(tav)), F_t''(0) = t - t^2 a^2. Wording slip: each branch *action* has second derivative 1; S_t has t. It does not bear on (SEP), since both branches have the same minimum. |
| Sect. 4, counting lemma (4.1) to (4.4) | ADVANCE | Successive deletion, injectivity of D -> D\Gamma, the bound sum_Gamma h >= (1/2) sum_M h + (H/2)|Gamma|, the rooted-forest DFS encoding with d^{2(n_j-1)} strings, and the geometric sum [a/(1-d^2 a)]^{|M|} <= 1 iff e^{-H/2}(1+d^2) <= 1 were all checked. |
| Sect. 4, slopes alpha, l_1 and the choice of X | ADVANCE (implication) | Coefficients of X and of (K-l) checked against 8w_0 lambda_l and 2 lambda_l; x_l >= X/2 for all l gives h >= H. |

**First step that fails: (SEP).** Nothing in Sections 1 to 4 is wrong as written. The route stops where the note says, at (SEP) inside (CD). (SEP) is neither proved nor refuted here, and (D3) records the kill attempts.
