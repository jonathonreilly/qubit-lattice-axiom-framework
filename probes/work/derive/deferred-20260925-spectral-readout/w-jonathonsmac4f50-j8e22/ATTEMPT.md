# Readout remainder in a growing time window (postmark electric chain)

Task `J:derive:deferred-20260925-spectral-readout:a1` · worker `w-jonathonsmac4f50-j8e22` · model `claude-opus-5-5`
· origin/main `78db61c32a39234bab16034c57361bf0c418c0b1` · checker `check.py` (exact plus float diagnostics; about 5 s).

**Provenance.** The source PRs 9078 and 9091 are owner-account physics-loop branches, with commit author
`jonathonreilly` and no model trailer. They are not this machine's work, and no independence from other reviewers is
claimed. Cross-model confirmation applies.

## Obligation chosen

The task asks for a selected-time cancellation or readout remainder estimate, with the spin, window and time scaling
and a success witness stated explicitly.

What main already has:

- The landed short-time theorem gives the readout limit only at T = Ct = τ fixed. That is qualitative strong
  convergence with no rate.
- The exact-side note controls the prepared profile e^{−itN²}|0⟩ at fixed t, but leaves the long unitary e^{iCtN}
  (T ~ S²) open.
- The 9078 head's "growing-window" estimate is only a coefficient estimate in an index window |k| = o(√S), stated
  there as "not an operator-norm or propagation estimate".

No propagation estimate for any diverging T exists on main. This attempt proves one, with explicit constants.

## Setting (supplied; conditional exactly as the landed notes are)

- M_S = −H_{2,S} is tridiagonal on I_S = [−5S, 5S−4], with C = S(S+1).
- Diagonal entries: a_n = 2 − (y₁+y₂)/C. Off-diagonal entries: b_n = √((1−x₁/C)(1−x₂/C)). Here x_i, y_i = m(m+a) are the
  landed legal-hop factors, loaded from `scripts/core_derivation.py` at main 78db61c3 with a pinned sha256.
- Generator: G_S = M_S² − CM_S.
- Prepared state |0⟩; readout P_S(t) = ⟨ψ|O|ψ⟩ with ψ = e^{−itG_S}|0⟩ and O = 1[n ≡ 0 mod 3] = (I+V+V*)/3.
- Free comparison: M_∞ = 2 + U + U*. Landed: ⟨e^{iTM_∞}0|O|e^{iTM_∞}0⟩ = 1/3 + (2/3)J₀(2√3 T).

## Theorem

For integer S ≥ 7 and 0 ≤ T ≤ S, with lab time t = T/C,

    |P_S(T/C) − 1/3 − (2/3) J₀(2√3 T)| ≤ 2ε(T,S),
    ε(T,S) = (6/(25C)) (√6 T³/3 + (19/√2) T² + 81 T) + 16 T/C + 6 T √(32/15) (e/4)^{5S−6}.

The leading term is 2ε ≈ 0.392 T³/C.

**Consequences.**

- **Window limit.** For every T_S → ∞ with T_S³/S² → 0, P_S(T_S/C) → 1/3. In lab time this is 1/C ≪ t ≪ S^{−4/3}.
  Success witness: the explicit ε together with |J₀(x)| ≤ √(2/(πx)).
- **Critical window.** Uniformly on T ≤ κS^{2/3}, limsup_S |P_S − 1/3 − (2/3)J₀(2√3T)| ≤ 0.392κ³.
- **Short-time rate.** At fixed τ the theorem gives the landed short-time limit with rate O(S^{−2}).

## Proof

**Step 1 (CHECKED exact, A1–A2; the per-residue form is PROVED in the landed notes).** At fixed residue r, with
n = 15k + r, every edge and return factor is 9k² + βk + γ. check.py fits and verifies this exactly on |n| < 1300.

For every integer n,

    x₁, x₂, y₁, y₂ ≤ (|n|+7)²/25.

Proof: g = (|15k+r|+7)² − 25p(k) is linear in k on each side of 15k + r = 0, because the k² terms cancel. Its slopes
and its values at k = 0 and k = −1 are ≥ 0 for all 15 residues and all four factors (exact). The constant c = 7 is
sharp for the method: c = 6 fails for six polynomials.

**Step 2 (PROVED).** Let W = M_∞ − M, with M the zero extension of M_S.

- Inside I_S: 0 ≤ W_nn = (y₁+y₂)/C and 0 ≤ W_{n,n+1} = 1 − b_n ≤ (x₁+x₂)/C. The second inequality holds because
  √((1−α)(1−β)) ≥ 1 − α − β for α, β ∈ [0,1], using √u ≥ u on [0,1] (A4 checks this).
- Rows with |n| ≤ 5S − 5 lie wholly inside, and every entry is ≤ q(n) := 2(|n|+8)²/(25C).
- Every entry of every row is ≤ 2. Outside I_S, W equals M_∞.

**Step 3 (PROVED, Duhamel).** Write ψ̃_T = e^{iTM}|0⟩ and φ_s = e^{isM_∞}|0⟩, where |φ_s(m)| = |J_m(2s)| (B5).
Duhamel gives

    ‖ψ̃_T − φ_T‖ ≤ ∫₀ᵀ ‖Wφ_s‖ ds.

By Cauchy–Schwarz on each row (bandwidth one),

    ‖Wφ‖² ≤ 3 Σ_m |φ_m|² Σ_{|n−m|≤1} w_n².

Splitting at |m| ≤ 5S − 6 gives

    ‖Wφ_s‖ ≤ (6/(25C)) ‖(|m|+9)²‖_{L²(μ_s)} + 6 (μ_s{|m| ≥ 5S−5})^{1/2},   where μ_s(m) = J_m(2s)².

**Step 4 (PROVED; B1–B3).** From the Neumann generating function Σ_m J_m(z)² e^{imθ} = J₀(2z sin(θ/2)):

    Σ m² J_m(z)² = z²/2,   Σ m⁴ J_m(z)² = z²/2 + 3z⁴/8.

Minkowski's inequality with z = 2s, plus √(a+b) ≤ √a + √b, gives
‖(|m|+9)²‖ ≤ √6 s² + 19√2 s + 81. Integrating gives the first term of ε (C1).

**Step 5 (PROVED; B4).** The Poisson integral gives |J_m(z)| ≤ (z/2)^m/m!. For s ≤ T ≤ S and N = 5S − 5 ≥ 4S, the tail
satisfies μ_s{|m| ≥ N} ≤ (32/15)(e/4)^{2N}. This gives the third term of ε, which is conservative (it uses 5S−6).

**Step 6 (PROVED).** ψ = e^{iTM}e^{−i(T/C)M²}|0⟩, so ‖ψ − ψ̃_T‖ ≤ (T/C)‖M‖² ≤ 16T/C. The bound ‖M‖ ≤ 4 is the landed
row-sum bound. For a projector O and unit vectors, |⟨ψ,Oψ⟩ − ⟨φ,Oφ⟩| ≤ 2‖ψ−φ‖. ∎

## Diagnostics (float, not proof; `check.py` D1)

Exact finite-S evolution uses tridiagonal eigensolves for S = 21…336 and 0 ≤ T ≤ S. The error never exceeds the bound;
the largest error/bound ratio is 0.063 at S = 21 and 0.0055 at S = 336.

Scratch scan outside the theorem:

| Window | |P − P∞| or |P − 1/3| |
|---|---|
| T = S^{2/3} | |P − P∞| ≲ 3×10⁻³ |
| T = S | |P − 1/3| ≈ 0.01–0.03, slowly decreasing with S |
| T = C/4, the fixed lab time 1/4 | |P − 1/3| ≈ 0.007–0.015 for S = 336 and 672, with no visible decay |

This matches the landed "fluctuating near 1/3" record.

## First unresolved step and ranked obligations

1. **S^{2/3} ≲ T ≲ S.** The free comparison fails once the packet sees coefficient changes (T/S)² over time T. The
   next comparator is the adiabatic local symbol 4(1−ρ)cos²(p/2): a WKB or commutator estimate for ⟨V⟩ on a
   slowly varying Jacobi flow, before any boundary reflection.
2. **S ≲ T ≲ S².** Reflections at the finite-spin ends, the two resonant band pairs and the central stationary layer
   (landed notes). Fixed lab time is T = C/4 ~ S²/4. The O(S^{−2}) eigenvalue-error warning applies: it can give O(1)
   phase error at T ~ S².
3. **Fixed-lab-time readout** Re q_S(1/4) → 0, a different limit, or separated subsequences (landed open item). Not
   addressed.
4. **Related task J:derive:deferred-20260925-preparation-optical-readout.** Distinct; not touched.

## Status of steps

| Step | Status |
|---|---|
| 1 (all-n coefficient bound) | PROVED + CHECKED exact |
| 2–6, theorem, corollaries | PROVED here (outside results used: Duhamel formula, Neumann addition theorem, Poisson integral for J_m, N! ≥ (N/e)^N) |
| Model, entry form, O = (I+V+V*)/3, free readout J₀(2√3T), ‖M_S‖ ≤ 4 | ASSUMED as supplied/proved in the landed notes |
| D1 | CHECKED numerically (float diagnostic only) |
