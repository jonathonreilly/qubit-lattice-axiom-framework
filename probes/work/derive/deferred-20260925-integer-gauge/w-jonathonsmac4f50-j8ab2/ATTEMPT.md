# Box-free minimum moves of the landed tensor vector stencil

Task `J:derive:deferred-20260925-integer-gauge:a1` · worker `w-jonathonsmac4f50-j8ab2` · model `claude-opus-5-5`
· origin/main `78db61c32a39234bab16034c57361bf0c418c0b1` · checker `check.py` (exact; about three minutes).

**Provenance.** The source PRs (9066, 9069, 9072, 9077, 9081, 9095, 9145) were written on `claude/dynamics-clause-*`
branches, so they come from the same model family as this attempt. They are not this machine's induced-law blocks, and
no independence is claimed. Normal cross-model confirmation applies.

## The obligation chosen

Both landed notes leave the same gap open:

- **PR 9077 note (main).** A radius-two, coefficient-bound-four, anchor-one MILP reports support 10.
  "No box-free minimum theorem" (claim scope). "Box-free minimum support … remain[s] open" (N6).
- **PR 9095 note (main).** The order-12 coefficient is proved only for the named displacement,
  "not that it is the globally first off-diagonal move". "Global minimal order, a complete effective Hamiltonian … remain
  deferred" (N6).

The original PR heads (`bf3663ce79`, `d3ac4167f9`) claimed an "independent complete search, with no box". That search
was never supplied. This attempt supplies the box-free statement: an algebraic proof, plus an independent exhaustive
search that is also box-free.

## Setting (supplied, not adopted)

The stencil is the landed tensor parent's, restated on main:

    (Gp)_j(x) = p_jj(x+e_j) - p_jj(x) + Σ_{i≠j} [p_ij(x) - p_ij(x-e_i)],   x ∈ Z³,  p_ij = p_ji.

A **move** is a nonzero vector v with finite support on the infinite lattice Z³ and Gv = 0. Charges are static.

- Support |v| counts nonzero slots.
- L1 = Σ|v_s| counts unit steps.
- Over Z_N the step count is the cyclic count Σ min(v_s mod N, −v_s mod N).

The domain has no spatial box, no coefficient bound and no anchor normalization: every nonzero move is covered.
Winding shifts on a torus are not finite-support moves on Z³, so they stay outside the statement.

## Theorem 1 (integer, rational or real slots)

Every move has support ≥ 10 and, for integer slots, L1 ≥ 12. Equality holds exactly for the planar moves:

- support 10 ⇔ v = c·δ_{ab,c} with c ≠ 0;
- L1 12 ⇔ v = ±δ_{ab,c}.

Here δ_{ab,c} is the landed named displacement: −2 on p_aa(c) and p_bb(c); +1 on p_aa(c±e_b) and p_bb(c±e_a);
−1, +1, +1, −1 on the ab faces at c, c−e_a, c−e_b, c−e_a−e_b. Every component of every move has coefficient sum zero,
so L1 is always even.

### Proof

**Step 1 (PROVED, CHECKED B1).** Use generating functions P_s(t) = Σ_x p_s(x) tˣ in R = Q[t₁^±, t₂^±, t₃^±]. Put
u_i = 1 − t_i, Q_jj = t_j⁻¹ P_jj and Q_ij = P_ij. Then

    Row_j = Σ_i u_i Q_ij.

The move condition becomes div Q = 0 for a symmetric 3×3 matrix over R. The rescaling t_j⁻¹ is a translation of one
component, so it changes neither support nor L1. `check.py` B1 compares this identity with the lattice formula on
40 random integer vectors.

**Step 2 (PROVED, term-count lemma).** For nonzero f ∈ R and i ≠ j ≠ k:

| If f is divisible by | then f has at least | and, for integer f, L1 at least |
|---|---|---|
| u_i | 2 terms | 2 |
| u_i² | 3 terms | 4 |
| u_i u_j | 4 terms | 4 |
| u_i u_j u_k | 8 terms | 8 |

- **u_i.** f(t_i = 1) = 0, so f is not a monomial.
- **u_i².** Slice f by the exponents of the other two variables. Each slice is divisible by (1 − t_i)². A two-term
  a tᵐ + b tⁿ with a double root at 1 needs a + b = 0 and am + bn = 0, which forces m = n in characteristic 0
  (`check.py` D5). Integer case: three nonzero integers with zero sum have L1 ≥ 4 (D6).
- **u_i u_j.** Slice by the t_j exponent. Each nonzero slice is divisible by u_i, so it has ≥ 2 terms. u_j | f means
  the slices sum to zero, so there are ≥ 2 slices.
- **u_i u_j u_k.** The same argument once more gives ≥ 2 · 4 = 8.

**Step 3 (PROVED, planar lemma).** Take a ≠ b. If u_a A + u_b B = 0 and u_a B + u_b C = 0 in R, or in the
two-variable ring, then

    A = u_b² φ,   B = −u_a u_b φ,   C = u_a² φ.

Proof: R is a UFD and u_a, u_b are non-associate primes. u_b | A gives A = u_b α and B = −u_a α. Then u_b | u_a² α,
so α = u_b φ. `check.py` D1 checks the converse identity.

**Step 4 (PROVED, Case I: some projection is nonzero).** Let π_k set t_k = 1, and let {a, b} be the other two indices.
Rows a and b project to the planar system for (π_k Q_aa, π_k Q_ab, π_k Q_bb), so this triple is (u_b²φ, −u_a u_b φ, u_a²φ).

- If φ ≠ 0, Step 2 gives 3 + 4 + 3 = 10 terms and L1 ≥ 4 + 4 + 4 = 12.
- Projection sums coefficients along lines, so it never raises support or L1. Hence |Q| ≥ 10 and L1(Q) ≥ 12.
- **Equality.** Q_kk = Q_ak = Q_bk = 0, so Step 3 applies in R itself: Q = Airy(Φ).
  - |u_b²Φ| = 3 forces Φ to have a single slice in (t_a, t_k).
  - |u_a²Φ| = 3 forces a single slice in (t_b, t_k).
  - So Φ = c·monomial, which is the planar move (C1).
  - In the L1 case the same slicing gives L1(ψ) = 1. The coefficient 1 of (1 − t_a)² makes ψ integral, so ψ = ±monomial.

**Step 5 (PROVED, Case II: every projection is zero).** Then u_k divides Q_aa, Q_bb and Q_ab for each k. So
u₂u₃ | Q₁₁, u₁u₃ | Q₂₂, u₁u₂ | Q₃₃, u₃ | Q₁₂, u₂ | Q₁₃ and u₁ | Q₂₃. The cases below use S₃ symmetry of the rows.

- **No nonzero diagonal.** Row 1 gives Q₁₂ = u₃a and Q₁₃ = −u₂a. Row 2 gives Q₂₃ = −u₁a. Row 3 becomes −2u₁u₂a = 0,
  so a = 0 and Q = 0 (D2). This is where characteristic ≠ 2 enters: mod 2 the face-only moves exist.
- **One nonzero diagonal (Q₁₁).** Rows 2 and 3 give Q₁₂ = u₃b, Q₁₃ = u₂b and Q₂₃ = −u₁b. Row 1 is
  u₁Q₁₁ + 2u₂u₃b = 0 (D4). So b = u₁β and Q = β(−2u₂u₃, u₁u₃, u₁u₂, −u₁²) (D3). Then |Q| ≥ 15 and L1 ≥ 16.
- **At least two nonzero diagonals (Q₁₁, Q₂₂).** These give ≥ 8 terms and L1 ≥ 8.
  - If Q₃₃ ≠ 0: add 4, plus one off-diagonal forced by row 1, for ≥ 14.
  - If Q₃₃ = 0 and Q₁₃ ≠ 0: row 3 forces Q₂₃ ≠ 0 with Q₁₃ = u₂γ and Q₂₃ = −u₁γ.
    - If Q₁₂ = 0, row 1 forces u₁ | γ, so |Q₁₃| ≥ 4 and the total is ≥ 14.
    - Otherwise three off-diagonals give ≥ 14.
  - If Q₃₃ = Q₁₃ = 0: then Q₂₃ = 0 and Q₁₂ ≠ 0. Step 3 gives Q₁₂ = −u₁u₂Φ with u₃ | Φ, so |Q₁₂| ≥ 8 and the
    total is ≥ 16.

Case II therefore always gives support ≥ 14 and L1 ≥ 14. ∎

**Step 6 (PROVED, zero sums).** For any move, each component evaluated at t = (1,1,1) equals a projected Airy entry
at 1. That value is 0. So every component's coefficients sum to zero, and L1 is even.

**Step 7 (CHECKED, independent box-free exhaustive search, `check.py` E).** This step is independent of Steps 1–6.
Work in doubled coordinates. A minimal-support move has connected support, where two slots are adjacent when they share
a row; otherwise each component is a move by itself. Translate so that the lex-minimal support slot sits at one of six
canonical anchors.

The search keeps sets S ⊆ T of slots known to be in the support and slots known to be out. It picks a row that touches
S and still has undetermined slots, preferring rows that see S exactly once. It then branches over every subset of the
undetermined slots, rejecting any choice that leaves the row with exactly one support slot. Along the branch consistent
with a true support T:

- the branch never dies;
- the search stops only when S = T, by connectivity;
- the leaf rank test then detects the kernel.

With the budget |S| ≤ 12, all six anchors give 1,954,858 nodes and 103 closed leaves.

- **E1.** Exactly three leaves are rationally rank-deficient, all of size 10.
- **E2.** Each has a one-dimensional kernel spanned by a planar move, one per plane.

So every move with support ≤ 12 is a multiple of a planar move. That gives Theorem 1's support and L1 statements and
both equality cases by computation alone, with no box, coefficient bound or anchor value.

## Corollary 2 (rotor slots, formal degenerate perturbation theory; PROVED given Theorem 1)

Supplied model: H0 = U Σ_rows (Gv)² and V = −h Σ_s (X_s + X_s†), with unbounded integer slots. h is the one-step
matrix element; a spin field h_spin σₓ/2 gives h = h_spin/2, which preserves the landed correction.

1. An order-n matrix element of any standard effective Hamiltonian between zero-charge states x and x + δ needs an
   n-step walk, so n ≥ L1(δ) and n ≡ L1(δ) mod 2.
2. By Theorem 1 no off-diagonal term exists below order 12, and none at odd orders (Step 6).
3. At order 12 the walks are monotone. No proper partial state is a move, since that would be a move with
   0 < L1 < 12. So there is no degenerate-sector insertion, and all standard schemes agree.
4. The order-12 off-diagonal part is therefore exactly
   −A (h¹²/U¹¹) Σ_{planes, c, ±} T_{±δ_{ab,c}},
   with A = 111150053/31850496. `check.py` H3 re-derives A by exact recursion over the 2304 partial states.
5. It is state-independent, because translation by a move commutes with H0 and V.
6. Together with the landed statement that the diagonal part is formally a constant, this is the complete leading
   effective Hamiltonian in the zero-charge sector, up to O(h¹⁴/U¹³) off-diagonal corrections.

This is a statement about formal perturbation theory only. Convergence and a uniform limit are not addressed.

## Corollary 3 (unit-entry moves)

A move with entries in {−1, 0, 1} is not a planar multiple, since those contain ±2c. So its support is ≥ 13, and by
Step 6 ≥ 14. The landed radius-two unit-entry search reports 20. The box-free gap 14…20 is open. This bound ignores the
two-level slots' direction constraint, so it is a lower bound for them too.

## Theorem 4 (Z_N clock slots; CHECKED, `check.py` G, box-free)

The same 103 leaves decide Z_N. A minimal Z_N move is connected and passes the same row test, because a row that sees
one slot has value ±v_s ≢ 0. Nonzero Z_N kernels come from Smith invariants.

| N | minimum support | minimum cyclic steps | minimizers at the minimum step count |
|---|---:|---:|---|
| 2 | 6 | 6 | six-face cube only |
| 3 | 10 | 10 | planar moves (−2 ≡ +1) |
| 4 | 6 | 12 | planar moves and the half-period cube |
| 6, 8, 10, 12 | 6 (cube at N/2) | 12 | planar only |
| 5, 7, 9, 11, 13 | 10 | 12 | planar only |

- **Every N (G6).** Only the prime 2 divides a Smith invariant of a leaf of size ≤ 9. So Z_N has a move of support
  ≤ 9 iff N is even, which gives the landed half-period cube. For odd N every move has support ≥ 10 on the whole
  lattice. This extends the landed single-neighbourhood odd-N obstruction to a global one. Up to leaf size 12, too, only the prime 2 appears, so for odd N every Z_N move with support ≤ 12 is a multiple of a planar move.
- **N ≥ 12 (PROVED, lifting lemma).** Lift a Z_N move with fewer than 12 cyclic steps to representatives in
  (−N/2, N/2]. Every row value then has |·| ≤ 11 < N and is ≡ 0, so it is 0: the lift is an integer move with
  L1 < 12, which cannot exist. For N ≥ 13 the equality case lifts to ±planar in the same way.

So for every N ≥ 5 the minimum is 12 steps, attained only by the planar moves. The even-N cube distinction is preserved:

- N = 2 is lower, at 6 steps;
- N = 4 ties at 12 with a non-planar move;
- for even N ≥ 6 the cube still has minimum support 6 but costs 3N ≥ 18 steps.

## First unresolved step and remaining obligations (ranked)

1. **Unit-entry (two-level) minimum.** Box-free lower bound 14 against the radius-two report of 20. Next: raise the
   search budget to 20 with unit-entry leaf tests, or extend the Case I/II algebra with entry bounds.
2. **Second-smallest integer moves.** Do moves with L1 = 14 exist? The original head claimed "next at 16". That fixes
   the order-14 off-diagonal content.
3. **Finite tori.** Every move on Z³ with support ≤ 12 is planar, but torus winding classes (support L) and small-L
   aliases are not covered.
4. **Qubit-background fourth-order formula (201/960)ΔN_A.** Only sampled, as landed. Not addressed.
5. **Other obligations in the bundle.** Phases (9066/9069/9072/9081) and compact oscillators (9145) remain open.
   They were not inspected beyond their snapshot hashes in this pass.
6. **Convergence** of the formal expansion and a controlled phase: open.

## Status of steps

| Step | Status |
|---|---|
| 1–6, Corollaries 2 and 3, lifting lemma | PROVED here (algebraic; outside results used: Laurent polynomial rings are UFDs, factor theorem) |
| B1, C1, D1–D6, E1–E2, G1–G6, H1–H3 | CHECKED exactly by `check.py` |
| Stencil, soft energy, slot fields, conventions | ASSUMED as supplied by the landed notes; not framework premises |
