lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T05:31Z

# Check of `library/loc-4.md` Sections 3-7 (queue row 235)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; checkout `1ad946eb7`; Sussman-Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder ("SA L" numbers refer to it). One reading by one other model, not an audit; it grants no status. Every step below was redone by hand. No computation enters any verdict.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for (R9)-(R12) and the bracket method (SA L5762-5855, L17904-17918). Codex wrote `loc-4.md`. Balaban for the background-localisation method.

Status: in progress. Sections are written as the check proceeds.

## Verdicts

| Statement | Verdict |
|---|---|
| §3 Proposition O, geometry only | ADVANCE |
| §4 (1), inner curves of Theorem A in the Hölder core | ADVANCE (implication) |
| §4 (2), single-layer outer shifts with room | ADVANCE (implication) |
| §4 Hölder conversion and "(2) gives (R11)" | ADVANCE (conditional, as stated) |

## §3. Proposition O — ADVANCE

Checked line by line by Claude, first failing step none. The note keeps only the geometric part of `loc-3.md` Proposition O, which `gates/loc-3-check.md` §3 already passed.

- **First index.** `int W_n` increases with n. Lemma S makes each `W_n` contain S in its interior or miss it there. S lies in `int Omega_0 = int W_N` by separation. So the first n with `S ⊂ int W_n` exists and is unique, and it is at least 1, since S misses `int W_0`.
- **(a).** Enlargements compose: `(A^{+a})^{+b} ⊂ A^{+(a+b)}`. So `S ⊂ W_{n_S+1} ⊂ W_0^{+(n_S+1)mu_W}`, which is the first inequality.
- **(b).** `S ∩ int W_{n_S}` is empty, so S lies in the complement of the interior, which is the closure of `W_{n_S}^c`. Distances to a set and to its closure agree, which gives the second inequality.
- The closing disclaimers are correct. The geometry gives no lower bound on the response, does not refute (N2'), and builds no joint history.

## §4 (1). Inner curves — ADVANCE as an implication

Checked line by line by Claude, first failing step none, given Theorem A (`wf-c.md`; checked by Codex in `b4-step.md` §0), Theorem I with the repairs of `gates/o1-decoupled-gate.md` §4.5, and Lemma 5 with (A2-H) (`gates/bx-fix-check.md`, ADVANCE).

- Theorem A (A1) puts every input clause of the curve at most 5/8 of its radius.
- In (A2), Lemma E gives at most (1+beta) a tau^2 with a <= (5/8) alpha_{0,l}. The gauge ceiling gives e^{C_g sup|B|} <= 1+beta, with beta = 1/8. The product is (9/8)^2 (5/8) = 405/512.
- **Age zero.** 405/512 < 4/5, since (4/5)·512 = 409.6.
- **Positive age m.** The repaired floor gives alpha_{0,l}/alpha_{0,j} <= (1+m)^{1/2}. With L >= 3, (1+m)^{1/2} L^{-2m} <= 2^{1/2}/9. The coefficient is then at most (405/512)(2^{1/2}/9) < 1/8. Theorem A's unrepaired factor 2(1+m)^{1/2} still gives about 0.249. Both are below 1/2.
- Theorem I transfers the bound to every Z ⊂ X, p <= j, n <= p and both rules, with real factor 1.
- **Hölder clause.** For U = 1, g = 1 and A_r = 0 witness (H), and A'' = H(B). Lemma 5 gives [grad H(B)]_alpha <= C_HH sup|B|. With C_H raised to max(C_H, C_HH) in the potential ceiling, this is below alpha_{1,j}/2.
- Theorem A covers every |s_Delta| < e^kappa-bar, so all Boolean corners are included. The margin is 1/5.

Scope note, not a defect: in Theorem A the complex parameter multiplies the window cutoff zeta. This curve family is not the (R10) interpolation, and the note does not claim it is.

## §4 (2). Single-layer outer shifts — ADVANCE as an implication

Checked line by line by Claude, first failing step none, given Lemma T of `a3-close.md`. Lemma T is not yet checked by the other model; `gates/a3-close-meet-gate.md` excludes `a3-close.md` §2, as §2 of the note says.

- **Simple clauses.** P ∔ nu(H,j) = (U, A' ⊞ nu H, J + nu j) (SA L5751-5759). So U, the real gauges and the real towers do not change. `wf-room.md` (3.3)-(3.5) bound the field changes by C|nu| b. On |nu| < R = d a_0/b the fields meet radii (2a_0, 2a_1), since a_0 <= a_1.
- **Towers.** Lemma T at radii (2a_0, 2a_1) needs 2a_0 + 2a_1 <= c_T/2, which is a small-radius choice. It gives K#(2a_0 + 4a_1^2) <= K#(2+4C_0) a_0 = A a_0. The unit change to level p multiplies the bound by L^{-2(j-p)} and the clause radius by L^{-(j-p)}, so the normalised bound only improves. Holomorphy in nu holds because nu -> A' ⊞ nu H_s is holomorphic and stays in Lemma T (a)'s ball.
- **Schwarz step.** Apply it to l(f(nu) - f(0)) for norm-one functionals l. This gives ||f(nu) - f(0)|| <= (A+1/2) a_0 |nu|/R. Choosing c < d/[4(A+1/2)] gives |nu|/R < 1/[4(A+1/2)] on |nu| < c a_0/b. So each tower quantity is below a_0/2 + a_0/4. Every clause is fixed separately with the same constants, so nothing is summed over towers.
- **Current.** |J + nu j_s| < a_0/2 + c a_0 < 3a_0/4 once c < 1/4.
- **Hölder clause.** In the witnessing gauge g of P, A''_new = A'' ⊞ Ad(g^{-1}) h, because conjugation commutes with the bondwise BCH map. The product rule ∇(fg) = (∇f)(τg) + f∇g holds on cubes of fixed side C_box LM. With [g]_alpha <= 2 diam^{1-alpha} ||∇g||_∞, it makes C^{1,alpha_H} a Banach algebra with a mesh-free constant. The BCH remainder G_eta(p,v) vanishes at p = 0, so ||A'' ⊞ h'' - A''||_{1,alpha} <= C||h''||_{1,alpha}. The C^{1,alpha} size of A'' is small: |A''| = |A'|, and |∇A''| <= |∇_U A'| + C|A_r||A'|. Then [∇A''_new]_alpha < a_1/2 + C c a_0 < 3a_1/4.
- **Conversion.** ∇^U h = ∇h + K h(·+eta e_mu), with K = (Ad(U_mu) - I)/eta. This holds for complex bold U as well; K = i ad(w) + O(eta|w|^2) is bounded in C^alpha uniformly in eta. Straight transports over length s <= xi_y differ from 1 by at most C s sup|w|. With Lemma 0 and Proposition PH (ADVANCE in `gates/bx-fix-check.md`), this gives the ordinary bound epsilon <= C|nu| B ||B'||.
- **(R11).** If b <= C e^{C kappa-bar} L^{-(k-j)} delta(theta_k), then rho = c a_0/b >= (c/C) L^{k-j} a_{0,j} delta^{-1} e^{-C kappa-bar}. This is (R11) with c_F = c/C and C_F = C. It is conditional, as the note says.
