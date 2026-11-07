lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-07T16:00Z

# PRINT-INVERSE: bounds and walk expansion of q_0 = (Q G_0 Q^*)^{-1}

Queue row 424. Commit 03ffc2764. Proved by Claude, not yet checked by the other model.
Work in progress; sections are written as they close.

Credit. The construction is Tadeusz Balaban's (CMP 96 Proposition 2.7 and §2; CMP 99b
§3, Theorems 3.2, 3.9, 3.10). The target statement, its consumers and the class S1-S2
are from the complete account of Ethan Sussman and Levent Alpoge (Claude and Codex as
authors of their text), commit 31a47c543775, CA-I 13144-13178. The prior-work digest is
`library/prior/print-inverse.md` (Codex). Duplicate check (FINISH rule 0a): `library/open-core.md`
and `library/l17c.md` have no match for PRINT-INVERSE, BP07, (3.132) or the remark label;
`library/open-registry.md:428` assigns PRINT-INVERSE to this row only.

## 1. The three damaged displays, read from the page images

Read from `~/ym4d-papers/balaban_cmp99_389.pdf`, rendered with PyMuPDF (journal page =
388 + PDF page). Quoted in the repository's notation; d is the dimension.

**(3.99)**, journal p. 413 (PDF page 25), Theorem 3.9, hypothesis (3.35), M large:
(Q'G'^2Q'^*)^{-1} = sum_omega R'_0(X_0) R'_{a_1}(X_1) ... R'_{a_n}(X_n)  (3.98), walks with
X_{i-1} ∩ X_i ≠ ∅; a term depends on U restricted to X~_0^5 ∪ ... ∪ X~_n^5, and

  |(R'_0(X_0) R'_{a_1}(X_1) ... R'_{a_n}(X_n))(y,y')|
     <= O(1) (L^j eta)^{-4} (L^{j'} eta)^{-d} O(M^{-1/2})^{|omega|} M^{-|omega|/2} e^{-(1/2) delta_0 d(omega,y,y')},
  y ∈ Λ_j, y' ∈ Λ_{j'}.

"The distance d(omega,y,y') is defined by (3.93), but the infimum is taken over y_i ∈ X_i ∩ B."

**(3.108)**, journal p. 416 (PDF page 28), Theorem 3.10 (hypothesis printed "(3.95)", read as (3.35)):
G = sum_omega R_0(X_0) R_{a_1}(X_1) ... R_{a_n}(X_n)  (3.107); a term depends on U restricted to
X~_0^5 ∪ ... ∪ X~_n^5 and

  |(R_0(X_0) ... R_{a_n}(X_n) J)(x)| <= O(1) (L^j eta)^2 O(M^{-1/2})^{|omega|} M^{-|omega|/2}
                                          e^{-(1/2) delta_0 d(omega,y,y')} |J|,
  x ∈ Δ(y), y ∈ Λ_j, supp J ⊂ Δ(y'),

"and the corresponding inequalities for norms on the left-hand sides of (3.42)-(3.47). The
constant O(1) depends on d and L only."

**(3.132)**, journal p. 422 (PDF page 34), after "let us write only bounds. We have":

  |(QGQ^*)^{-1}(y,y')| <= O(1) (L^j eta)^{-2} (L^{j'} eta)^{-d} e^{-delta_1 d(y,y')},  y ∈ Λ_j, y' ∈ Λ_{j'},

"and the same for the operator with G_1 instead of G." This agrees with the visual reading
in `library/b99.md:123-129` (there with d = 4). The model it is "analyzed in the same way
as" is Theorem 3.2, (3.48), journal p. 398:
|(Q'G'^2Q'^*)^{-1}(y,y')| <= B_0 (L^j eta)^{-4} (L^{j'} eta)^{-d} e^{-delta_0 d(y,y')}.

So the target bounds are (3.132) and the walk bound (3.99) with the scale factor
(L^j eta)^{-4} replaced by (L^j eta)^{-2}; that replacement is Balaban's own instruction
for the field Gram in CMP 96 (OCR 1198-1203: "we replace +4 and -4 in (2.83) by +2 and -2").
