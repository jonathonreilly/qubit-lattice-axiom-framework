# Depolarized record pointer: positivity fails already at first order in the noise

Task `J:derive:deferred-20260926-quantum-record-codes-and-pointers:a1` · worker `w-jonathonsmac4f50-j07c6` · model
`claude-opus-5-5` · origin/main `e37967e326` · checker `check.py` (exact; about 4 s).

**Provenance.** The source is Codex (campaign 12h_third). This referee is Claude, a different model family, so this
counts as the cross-model check the packet lacked. Codex's own separate-context checks were within one family.

## Obligation chosen

Of the three offered finite claims, this attempt referees the depolarized commuting pointer's exact negative
off-diagonal generator entry for every 0 < η < 1. It then attacks the registry's open step for that family, an
approximate implementation, by asking at what order in η positivity first fails.

## Setting (supplied by the source notes; not framework premises)

- **Lattice and labels.** The periodic lattice has side N = 12. U is its even sublattice (864 sites). There are 14
  colours: six A labels (e = ±eᵢ, b = 0) and eight B labels (e = 0, b ∈ {±1}³).
- **Routes.** δ ∈ {−e1, ±e2, ±e3} with a = δ − e1. The stencil is (u−a, u, u+a, u+2a) = (l, c, d, r).
- **Dynamics.** Colours c and d swap at rate k0/2 + h/4, with k0 = 11/10 and γ = 1:
  - S_δ(c,d) = ½ δ·(e_c×b_d + e_d×b_c);
  - h = S(l,c) + S(c,r) − S(l,d) − S(d,r).
- **Pointer.** ρ_a = (1−η)|a⟩⟨a| + (η/14)I. The preparation matrix is B = rI + q11ᵀ with r = 1−η and q = η/14. The
  target is the full routed law, reached by intertwining with a positive map.
- **Positivity criterion (PROVED in the source; re-checked here).** B is invertible, so linearity fixes the quantum
  action on the pointer diagonal: G = B^{⊗K} L_class B^{−⊗K}. A positive evolution needs G_{x,y} ≥ 0 for x ≠ y,
  because d/dt⟨x|Λ_t(|y⟩⟨y|)|x⟩ at t = 0 equals G_{x,y}. Complete positivity is not needed.

## Steps

1. **CHECKED R1–R2.**
   - Every S_δ is symmetric, has zero diagonal and zero row sums, and satisfies |S| ≤ ½, so every rate is ≥ 1/20.
   - B⁻¹ = (I − q11ᵀ)/r exactly.
2. **CHECKED R3.** There are 864 × 5 = 4320 routed stencils. Exactly two contain the three consecutive δ = −e1
   positions (0,0,0), (10,0,0), (8,0,0).
3. **PROVED (locality).** B^{⊗K} acts factorwise, so G is a sum of stencil-local terms B^{⊗4}L_e B^{−⊗4}. An entry
   with differences on a set D gets contributions only from stencils containing D. On each stencil:
   - the constant-rate part (k0/2)(P − I) commutes with B^{⊗4}, since P permutes identical factors;
   - the h/4 part is (P − I)Σ±K_pair, with K_S = (B⊗B)diag(S)(B⁻¹⊗B⁻¹) on each pair.
4. **PROVED + CHECKED R4 (the author's entry).**
   - With w^{(i,j)}_s = B_is B⁻¹_sj = (q/r)[δ_sj − rδ_si − q] for i ≠ j, the zero row sums and zero diagonal of S
     give (K_S)_{ij,ji} = q²(1+r²)S_ij/r².
   - Only the terms −S(d,r) of edge (u0,u1) and −S(l,d) of edge (u1,u2) reach the witness, so
     G_{x,y} = −¼[(K_S)_{ab,ba} + (K_S)_{ac,ca}] = −η²[1+(1−η)²]/[784(1−η)²].
   - sympy confirms this for symbolic η.
5. **CHECKED R5–R6.**
   - Torus-level exact values at η = ½, ⅕ and 9/10 agree with the formula.
   - An independent algorithm gives the same stencil contributions, −5/6272 each, at η = ½. It propagates
     (B⁻¹)^{⊗4}e_y through the sparse generator on the full 14⁴ stencil space and then contracts with B^{⊗4}. This is
     neither the author's symbolic pair formula nor their 38416-term sum.

   **The author's claim holds.**
6. **NEW, PROVED + CHECKED N1–N6.** Use the same three positions with
   y = (A(+e2), B(·,·,+1), B(·,·,−1)) and x = (A(−e2), B(·,·,−1), B(·,·,+1)). That is the swap on the second edge plus
   a changed end colour. Exactly:

       G_{x,y} = η(η − 2)(η² − 14η + 14) / [784 (1 − η)²] = −η/28 − η²/56 + O(η³).

   - It is negative for every 0 < η < 1: η > 0, η − 2 < 0, and the roots 7 ± √35 of the quadratic lie above 1.
   - It matches exactly on the full torus at η = ½, ⅕ and 1/100, and by tensor propagation at η = ½.
   - At η = ½ it equals −87/3136, 17.4 times the author's −5/3136.
   - **Mechanism.** At first order, G = L + η[Σ_w A_w, L] with A = J/14 − I. The commutator's entry for "swap (c,d)
     plus change the end colour l" is (1/56)Δh, where Δh = [S(y_l,y_c) − S(y_l,y_d)] − [S(x_l,y_c) − S(x_l,y_d)] can
     reach −2.
7. **Consequence for the open step (PROVED).**
   - Every positive (Markov or Lindblad) generator M on the pointer diagonal has M_{x,y} ≥ 0. So its sup-entry
     distance from the required G is at least η/28 − O(η²).
   - The orthogonal-pointer dynamics L itself is positive and differs from G by O(η), because G − L = η[ΣA, L] + O(η²)
     with stencil-bounded entries.
   - So the best achievable generator error of a positive implementation in this family is of order η, not η².
     Small depolarizing noise cannot be absorbed at second order.
8. **Diagnostic D1 (not a proof).** In random contexts, single-site colour changes also give negative first-order
   entries. The most negative exact value in the sample, at η = 1/1000, is −0.0536η. The global minimum entry is not
   determined.

## First unresolved step and what would finish it

- **Sharp constant.** The minimum of G_{x,y}/η over all entries is unknown: 1/28 is a proved lower bound on the
  approximation error, and the sample reaches 0.0536. Finishing it needs an exhaustive first-order search over the
  29-site neighbourhood. Its structure: G1 = [ΣA, L_h] with L_h = ¼(P − I)Σ±K is local and linear in S.
- **Best approximate positive implementation.** The upper-bound constant is open. Candidates include clipping and
  reweighting G, or modifying the rates at order η.
- **Not addressed.** The six-qubit block pointer's local logical-block Lindblad dynamics and the fixed nonorthogonal
  code (the other two offered claims).

## ASSUMED

- The supplied model: labels, rates, routes, pointer family and product preparation.
- The positivity criterion's premise that the implementation is a positive linear map on the span of the prepared
  states. This is the source's stated target.
