# Referee: library/layer-thm-part.md (LAYER-THM conditional part)

File: `library/layer-thm-part.md`, 1608 lines (Codex distil of layer-pkg,
walks-gw, layer-r3, adm-pl). Date: 2026-11-07. FINISH row 452.
Account: Sussman–Alpöge at 31a47c543775; SHA-256 of part I checked
(`4cb5cb5e0af8…`, matches the part's table).

One referee pass. Imports PI, GW (repaired walks-gw.md), B98-P5 port and
the b98p5-r3 gate are used as given.

(Sections below are saved one at a time.)

## (M3) verdict

**Verdict: HOLDS, as stated in the part (a test of two proposed switched
extensions, not a refutation of the layer theorem). It is a gap in the
account's assumed layer package (an undefined object), plus one
over-wide sentence; it is not a false proved step of the account.**

Source facts (read in the account).

1. I 14404–14409 defines the chart current by formula:
   Λ^J(B) = P_0^T Ξ + Q^*(q_0 − a)B̃ − Q^* k X_G − Λ^T j_J(H^J X_G),
   𝔍 = Λ^J − Δ'𝓗^J + F. Expanding 𝓗^J = A_G − H^J X_G gives exactly the
   part's (M2) with m_c of (M1). I checked this term by term.
2. I 14439–14493 proves the representation identity
   Δ_a A_G = P_0^T Ξ + Q^* q_0 B̃ and the reduced form
   𝔍 = (Δ_a − Q^*aQ − Δ')A_G − 𝒦_1 X_G + F. The proof uses the P_0G_0
   fixed-point form, Δ_a P_0 G_0 = P_0^T, Δ_a H_0 = Q^* q_0 and
   QA_G = B̃ (from QP_0 = 0, QH_0 = ℓ^{-1}). All are inverse identities.
   𝒦_1 = m_c exactly. With Δ_a = 𝒟(W) + D_0 R D_0^T + Q^T a Q and
   P = I − R (I 25322), Δ_a − Q^*aQ − Δ' = D_1^TD_1 + D_0RD_0^T
   = Δ_W + K_W − P_1 with P_1 = D_U P D_U^* (I 14727). So (18) at σ = 1
   is the account's reduced form. (M1) is correct.
3. I 15266–15339 (K10): G_0, q_0, q_J, G̃^J and the others are primitive
   and walk-tagged; composites (H_0, P_0^T, H^J, Λ, D^J, V', 𝒜, 𝓗, Λ^J, 𝔍)
   are formed "by the formulas" from the primitives at s. Q, a and the
   identity are not primitives, so they carry no tag. The fixed point at s is
   taken in the G̃^J form (I 15317), not in the P_0G_0 form.
4. I 15338–15339 and 15448–15451: the explicit formulas enter only
   chart-structure-a, response-chart-a and diagonal-exactness-a, "This is
   why the first and the last of these are asserted at s≡1 only". The
   representation identity (the middle one) is not restricted there. It is
   stated "At every (U,J)∈𝔖" (I 14439).
5. I 72720–72728 and 72831–72851: the link current is
   𝔰^♯_s, "a local function of (A',X,𝒴), up to the action of the decoupled
   operators P_1(s) and m_H(s)", whose kernels "vanish unless both arguments
   lie in one component of Y(σ)". I 111394–111399 writes the rider in the
   reduced form (18) with P_1(σ), m_H(σ). The account never defines
   P_1(σ), m_H(σ) at σ ≠ 1; the layer package is assumed (I 72392–72399).

My own argument for the zero-switch test. Take site (T), so 𝖪 = ∅ and
σ_0 = π (I 72705). Put s ≡ 0. Every walk term of every primitive meets a
cube, so every primitive is zero: G_0 = q_0 = q_J = G_π^J = G̃^J = 0.
Then H_0 = H^J = B_0 = Γ = 0, and the composites P_0 = I and
k = (q_J − a)ℓ^{-1} = −aℓ^{-1}, because I and a are untagged (fact 3).
At j = 0, (S5) gives A' = 0, X = C(0) = 0, h = 0, and Ξ = 0 since V'(0) = 0.
So the rider (18) is F(W,0) = 0. The definitional current (M2), which is
the account's own 𝔍(s) of fact 3, is −Q^T a ℓ^{-1} b. Choose b on one block
bond; Q^T b is the transpose of one nonzero averaging row times b, so it is
nonzero. Also QA_G = 0 ≠ B̃, so the reduced form of fact 2 fails at s ≡ 0.
And m_c(0) = −Q^T a ℓ^{-1} ≠ 0, while Y(0) = ∅, so the locality clause of
fact 5 requires a zero kernel. The flat torus and J = 0 are not needed for
the vanishing of the primitives; they only keep the point in the admitted
class. The argument holds.

Where the identity is used. Inside the account's proved text, the
representation identity is not load-bearing at s ≠ 1:
- K3 at s (via K10 "verbatim", I 15429–15438) only reads the term list of
  I 14759–14765, which is the definitional list. The bound on 𝔍(s) is
  therefore valid without the identity.
- K6 (I 15676–15860) uses it only at s ≡ 1.
So the identity is not used beyond its hypotheses in a proved step.
The sentence at I 15450–15451 is over-wide: it leaves the identity
unrestricted although its proof is valid only at s ≡ 1.

Account or route? The account consumes the rider at arbitrary s in the
reduced form (fact 5) with P_1(s), m_H(s) that it never defines. The only
switched current the account does construct (K10's 𝔍(s), = (M2)) is not
of that form and violates the locality clause at s ≡ 0. Thus:
- It is a defect of the account's assumed package (missing definition and
  proof of P_1(s), m_H(s)), not only of the (S5) route.
- It is not a contradiction in the account: a rider defined directly by
  (18) with every local diagonal term tagged (reduce before switching) may
  satisfy everything that is consumed (holomorphy, (7), locality, value at
  s = 1 by K6). That assignment and its checks are absent. This is exactly
  premise M.

Repair to the part (REVISE, wording only). In the Outstanding M paragraph,
after "all primitive sums vanish;" insert: "here 𝖪 = ∅ (site (T), I 72705),
and, as in I 15266–15339, Q, a and the identities in P_0 = I − G_0Q^Tq_0Q
and k = (q_J − a)ℓ^{-1} are untagged composite factors;". After "…requires
a zero kernel for the empty retained region." insert: "The account's own
switched current at I 15317–15322 is (M2). Its proved bounds at s read only
the definitional term list (I 14759–14765), so no proved account step uses
the representation identity at s ≠ 1; I 15450–15451 leaves that identity
unrestricted, which is too wide. The defect is the absence of a definition
of P_1(σ), m_H(σ) at σ ≠ 1 in the assumed package." In (M3) state the
assumption m_H = m_c used in the subtraction.
