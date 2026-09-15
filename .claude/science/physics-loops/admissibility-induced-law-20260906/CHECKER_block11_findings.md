# Refuting pass — block 11 (supervisor-run, disjoint machinery; 2026-09-15)

Routes compared (controls in `specs/supervisor_control_block11_locus_*.py`, outputs in `.out.txt`):

| item | runner's route | refuting route | result |
|---|---|---|---|
| candidate points off the lines | lex elimination basis of `(E_1, G)`; `p = ψ(q)` modulo the sextic | the resultant `Res_q(E_1, E_2)` factored, each positive root refined to width `10^{-12}`, every ordered candidate pair tested by an exact rational enclosure of `E_1` and `G` over the box (control C): 20 of 25 pairs excluded; the 5 undecided are exactly the six points' pairs (the constant rule, `(1, ρ)`, `(ρ, 1)`, `(σ_1, σ_2)`, `(σ_2, σ_1)`) | consistent |
| the line `p = r` | divisibility of the 16 numerators by `(q−1)³(q³−3q²−15q−19)` | direct enumeration of `Z_3` on the line (three values) and factorization of the four distinct nonzero numerators there (control D) | equal factors |
| the sextic pair | `s(ψ) ≡ E_1(ψ, q) ≡ G(ψ, q) ≡ 0 (mod s)` | `gcd(E_1(1, q), G(1, q))` over `Q` for the `p = 1` family and the explicit inversion `A^{-1} mod s` (control E) | equal |
| sufficiency at the six points | reductions modulo the minimal polynomials | the same reductions computed independently in control F before the runner was written | 0 of 16 numerators nonzero at each |

Attempts to refute (nothing refuted): the necessity direction (pair-additive ⇒ `E_1 = E_2 = 0`) is by definition (two of the cross-ratio identities); the sufficiency direction is executed on all 16 numerators; the exchange `ψ(σ_1) = σ_2` is exact (an enclosure inside the other root's coarse isolating interval, and `ψ` permutes the roots of `s`). Findings: F1 (fixed) the runner's first pairing check demanded containment in a refined interval narrower than any enclosure — corrected to the coarse interval; F2 (fixed) method names (elimination bases, sign-change sequences) appeared in eleven places outside Prior art / Imports; F3 (retired) the algebraic-field gcd route was too slow and was replaced. Verdict of this pass: PASS-NO-BLOCKER at the supervisor's own standard, pending the owner's independent review.
