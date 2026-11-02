lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-03T02:06Z

# lit-balaban: legal full texts of Balaban's series, and where they prove (1b) Theorem 2, (U), the nonlinear response and R

Pinned at 4129bb8ab. Status: in progress.

Builds on `library/lit-large-field.md` (which could not reach any Balaban text:
bot check at Project Euclid, paywall at Springer) and `library/a3-response.md`
Section 8. The outline quoted is Sussman and Alpoge (with Claude and Codex as
authors of the text), `YM4_sketch_500.tex` at `31a47c543775`, read from a scratch
copy outside the repository. Everything here is a search record; nothing is
re-derived, and every Balaban statement below is `unchecked`.

## 0. What the next lane needs from Balaban (targets, from the outline)

- **(U) = outline Theorem 1** (l. 9660): for real eps_1-regular data V the
  regular critical configurations of C(B, V) form exactly one orbit, the
  background U_k(V), with |dU - 1| < C eps_1 eta^2 L(p)^-2. Its induction is
  closed (l. 9795, chain of (1b)) by "the global halving
  eps_0 -> max{C eps_1, eps_0/2}, following Proposition 8 [cited from
  Balaban; Package E] of CMP 102 (1985) 277-309". The outline's index
  (l. 32901-32904) separates "Balaban's Theorem 8, which he states without
  proof and which we must prove" from "Proposition 8 of CMP 102 (1985)
  277-309, which is cited".
- **(1b) Theorem 2 (local regularity)** (l. 9678): a critical regular U has
  eta^-2 L^2 |dU - 1|, L^3 |J(U)| <= C max_tau e^(-delta d_B(x,tau)) |dV(tau) - 1|,
  and (second half) any U regular on an enlarged cube has a local gauge
  e^(i eta A) with xi|A|, xi^2|nabla A|, ... <= C m eps. The outline (l. 9801)
  calls the second half "the counterpart for sequences" of **Proposition 6 of
  CMP 99 (1985) 75-102**, using its (1.135)-(1.136) and conditions (1.7)-(1.9).
- **Background propagators** (group (d) of (1c), l. 9797): Theorems 3.1 and
  3.3 of **CMP 99 (1985) 389-434**, p. 394 (auxiliary first member).
- **Linear minimiser decay**: CMP 95 (1984) 17-40, (1.103), Prop. 1.2, (1.110)
  (outline l. 26141); CMP 96 Lemma 2.1 (raw I l. 19391-19449).
- **R operation**: CMP 122 (1989) 175-202, (0.3)-(0.4) p. 176, pp. 177,
  181-183, Proposition 1 (minimiser in a box, outline Prop 2.4, l. 17656);
  CMP 122 (1989) 355-392, (1.73), (1.79), (1.102), pp. 384-387, Theorem 1;
  CMP 119 (1988) 243-285, Sect. 3, Theorem 1, Corollary 3, (3.40), (3.65),
  pp. 246, 278-279, 281 (outline l. 17290-17316, 17516, 17566, 22594, 22854).
