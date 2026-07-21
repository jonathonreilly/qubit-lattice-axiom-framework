# KCPT Dirac-radius grading of End_H(C^64): P = D2·J_full is the negative Dirac-radius operator −|D2|, block-scalar with eigenvalue −2√m on each of the six CP-completed constituents, and it does NOT separate 12⁺ from 12⁻ (both radius-degenerate at m = 1)

**Type:** bounded_theorem
**Date:** 2026-07-20
**Lane:** KCPT (L = 4, N = 64 staggered qubit lattice over the 4³ cube)

## Claim boundary

Define the operator `P := D2·J_full` on `C^64`, from the antisymmetric integer staggered adjacency `D2` and the ambient-invariant total complex structure `J_full` (the kernel + bulk assembly `J_ker + Σ_{m∈{1,2,3}} D2·P_m/(2√m)`). Everything below is exact finite-dimensional linear algebra over `C^64`; the runner rebuilds every object from the bare site construction with no import of another runner. All group labels are **geometric labels for lattice operators only**. "CP" throughout is the label for the geometric lattice parity involution `S_eps = diag((−1)^{x₁+x₂+x₃})` and its index-2 extension `H = ⟨G_amb, S_eps⟩`; **nothing here is a statement about Standard-Model CP.** The theorem fixes no free parameter, selects no bulk sign-family member, and is r-neutral and orientation-neutral.

## T1 — P = D2·J_full is real-symmetric and H-invariant, an element of the c_H = 6 commutant

`P` is real-symmetric because `D2` and `J_full` **commute**: `Pᵀ = (D2·J_full)ᵀ = J_fullᵀ·D2ᵀ = (−J_full)(−D2) = J_full·D2 = D2·J_full = P` (both factors are real and antisymmetric; `D2` commutes with each shell idempotent `P_m` because `P_m` is a polynomial in `M = D2²`, and `D2·J_ker = J_ker·D2 = 0` because the range of `J_ker` is `ker D2`).

`P` is **H-invariant**: `[P, h] = 0` for all 1536 elements `h ∈ H`. Neither factor is invariant on its own — both `D2` and `J_full` are `S_eps`-odd (`S_eps·D2·S_eps = −D2` exactly, and `S_eps·J_full·S_eps = −J_full`). Their product is therefore `S_eps`-**even**:

`S_eps·P·S_eps = (S_eps·D2·S_eps)(S_eps·J_full·S_eps) = (−D2)(−J_full) = D2·J_full = P.`

`G_amb`-invariance holds because `D2` and `J_full` are each `G_amb`-invariant, so `P` commutes with the whole coset as well as with `G_amb`: `P ∈ End_H(C^64)`, the six-dimensional commutant (`c_H = 6`). This is a genuine odd×odd = even effect, not inherited from either factor (T4).

## T2 — Closed form P = −|D2| = −√(−M), block-scalar with eigenvalue λ_i = −2√(m_i)

The closed form follows term by term:

`P = D2·J_ker + Σ_{m∈{1,2,3}} D2²·P_m/(2√m) = 0 + Σ_m (−4m)·P_m/(2√m) = −Σ_m 2√m·P_m = −√(−M) = −|D2|,`

using `D2²·P_m = M·P_m = −4m·P_m` on the shell `P_m`, and `−M = Σ_m 4m·P_m ⪰ 0` so `√(−M) = Σ_m 2√m·P_m` (the kernel term `m = 0` contributes `−2√0 = 0`). `P` is thus the **negative Dirac-radius operator** on the staggered lattice.

Because `P = −√(−M)` is a function of `M`, it is block-scalar on the six CP-completed constituents of `C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻`, with

`λ_i = −2√(m_i),`  `m_i` = the `D2²`-shell radius of that constituent,

and the full `P`-spectrum is `{0 (×8), −2 (×24), −2√2 (×24), −2√3 (×8)}`, tiling exactly the `[8, 24, 24, 8]` shell dimensions of an **independent** `eigh(M)`. The runner reproduces `−|D2|` from a separate diagonalization of the integer `M` (closed-form residual `2e-15`) and confirms every `λ_i` against `m_i` recomputed independently from `Z_iᴴ M Z_i`.

## T3 — the computed shell assignment: Dirac radius does NOT separate 12⁺ from 12⁻

Grouping the constituents by their holomorphic `W`-source rank (a basis-independent, seed-robust multiset), the computed shell membership is:

- the **CP-split pair `{12⁺, 12⁻}`** — the unique rank-12 `W`-source, the one constituent that splits under the extended group — sits **entirely at m = 1** (`λ = −2`): **radius-degenerate**;
- the two **induced 12's** (rank-6 `W`-source) sit at `m = 2` (`λ = −2√2`);
- the two **induced 8's** (rank-4 `W`-source) occupy the two **extreme shells** `m ∈ {0 (kernel), 3 (top)}`.

So the `m = 1` shell (dim 24) is exactly `12⁺ ⊕ 12⁻`, and the `m = 2` shell (dim 24) is the two induced 12's. **The Dirac-radius grading is strictly coarser than the constituent grading, and on the rank-12 CP-doublet it is constant.** The CP-parity that split the real 12 (the `S_eps` eigenvalue) and the Dirac radius (the `M`-shell) are therefore **independent quantum numbers**: the most natural H-invariant built from both structures — the product `D2·J_full` — is radius-blind to CP. This is a clean **negative** answer to the forward question left by the CP-completion note: no geometric datum carried by `P` distinguishes `12⁺` from `12⁻`.

## T4 — anti-fabrication contrast (why block-scalarity is non-vacuous)

The block-scalar structure is genuinely bought by the even product, not inherited:

- `D2` **alone** is not H-invariant (`max_h ||[D2, h]|| ≥ 1`) and not block-scalar; it carries a **nonzero** `S_eps`-odd off-block `|Z_{12⁺}ᴴ D2 Z_{12⁻}| ≈ 1.24 ≠ 0`, i.e. `D2` maps `12⁺ ↔ 12⁻`, whereas `P`'s off-blocks vanish (`< 1e-9`). `J_full` alone is likewise not H-invariant (`max_h ||[J_full, h]|| ≥ 0.5`).
- The rational `√m → 1` proxy for `J_full` fails `J² = −I` and yields the **wrong integer spectrum** `−2m ∈ {0, −2, −4, −6}`, distinct from `P`'s irrational `−2√m`. No parity/sign/integer stand-in reproduces the `±2√2, ±2√3` shell radii; the shell `√m` normalizers are load-bearing.

## Honest boundary

Geometric-label only, and a **negative** structural result. `P` fixes no free parameter, selects no member of the bulk sign family, and is r-neutral and orientation-neutral. The independence of CP-parity and Dirac radius is a statement purely about the two lattice operators `S_eps` and `M = D2²`; "CP" is the label for the parity involution `S_eps`, not Standard-Model CP. This note registers what the extended-group structure does and does not grade — it does not derive any physical mass, angle, or sign.

## The next path this opens

Since the Dirac radius is constant across the CP-split, the datum that separates `12⁺` from `12⁻` must live in a **different** H-invariant. The next path this opens is to ask which invariant of the Kähler triple does resolve the pair — the symplectic leg `ω`, or a higher `M`-Casimir — i.e. to hunt for the H-invariant operator whose block-scalar values differ across `12⁺` and `12⁻`, complementary to the radius-blind `P` established here.

## Runner evidence

`scripts/kcpt_dirac_radius_grading_of_end_h_2026_07_20.py` (paired), cached at `logs/runner-cache/kcpt_dirac_radius_grading_of_end_h_2026_07_20.txt`. Class-A finite-dimensional check, `TOTAL: PASS=15 FAIL=0`.

| Gate | what it certifies | count |
|------|-------------------|-------|
| G1 | \|G_amb\| = 768; \|H\| = 1536 = 2·768; G_amb ⊆ H, coset S_eps·G_amb ⊆ H and disjoint (index 2) | 1 |
| G2 | J_full² = −I, antisymmetric; ANTI-PROXY: √m→1 proxy fails J² = −I and differs from J_full (shell √m normalizers load-bearing) | 1 |
| G3 | P := D2·J_full real-symmetric (‖P−Pᵀ‖ < 1e-9) because D2, J_full COMMUTE (‖P−J_full·D2‖ < 1e-9); P ≠ D2, P ≠ J_full | 1 |
| G4 | THE THEOREM: max_{h∈H} ‖[P,h]‖ < 1e-9 over all 1536 elements — P ∈ End_H(C^64), the c_H = 6 commutant | 1 |
| G5 | ANTI-FAB CONTRAST: neither factor H-invariant (‖[D2,h]‖ > 1, ‖[J_full,h]‖ > 0.5); both S_eps-odd, product S_eps-even; S_eps preserves the D2²-shells | 1 |
| G6 | exact-integer commutant pins: c_G = 12, c_H = 6 (Σtr²/\|G\|); coset traceless (Σtr² = 0, max\|tr\| = 0) | 1 |
| G7 | the six Unit-14 constituents rebuilt object-identically: dims (sorted) [8,8,12,12,12,12] = 6 = c_H; exactly 2 CP-split (both rank-12 W-source), 4 induced | 1 |
| G8 | CLOSED FORM P == −\|D2\| == −√(−D2²): ‖P − (−√(−M))‖ < 1e-9 (\|D2\| from an INDEPENDENT eigh(M)); M-shell dims [8,24,24,8]; P's own spectrum tiles the same | 1 |
| G9 | BLOCK-SCALAR CENSUS: on every constituent Z_iᴴ P Z_i = λ_i I (max ‖blk − λI‖ < 1e-9), λ_i == −2√(m_i) with m_i from an INDEPENDENT Z_iᴴ M Z_i; P block-diagonal | 1 |
| G10 | THE COMPUTED ASSIGNMENT: CP-split {12⁺,12⁻} both at m = 1 (RADIUS-DEGENERATE, λ = −2); induced 12's at m = 2 (λ = −2√2); induced 8's at the extreme shells {0,3} | 1 |
| G11 | ANTI-FAB: D2 alone has a nonzero S_eps-odd off-block \|Z_{12⁺}ᴴ D2 Z_{12⁻}\| > 1 and is not block-scalar; √m→1 proxy gives INTEGER −2m ∈ {0,−2,−4,−6}, not −2√m | 1 |
| G-PIN-U14 | Unit-14 note contains `9216 / 1536 = 6` (c_H = 6, the six constituents P is block-scalar on) | 1 |
| G-PIN-U9 | Unit-9 note contains `S_eps J_full S_eps = -J_full` (with S_eps D2 S_eps = −D2, the two sign reversals that make P S_eps-even → H-invariant) | 1 |
| G-PIN-SELF | this note carries exactly two KCPT dependency links (Units 14, 9); Units 8/10/11/12/13 backticked only | 1 |
| G-MEM | greedy generating sets close to exactly 768 / 1536 with loose length bounds; commutant kron stacks use generators only (OOM-avoiding) | 1 |

## Dependencies

- [Unit 14 CP-completion under the extended group](KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the six CP-completed H-constituents `C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻` and the `9216 / 1536 = 6` commutant count, the constituents that `P` is tested against, and the `12⁺/12⁻` split whose radius-degeneracy is the payload here.
- [Unit 9 chiral-parity common-sign-orbit](KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md) — the two exact sign reversals `S_eps·D2·S_eps = −D2` and `S_eps J_full S_eps = -J_full` whose product makes `P` `S_eps`-even, hence H-invariant; and `S_eps·M·S_eps = M`, so `S_eps` preserves the Dirac-radius shells.

Units 8, 10, 11, 12, 13 enter only transitively through Units 14 and 9 and are referenced by name only, never as dependency links: the total complex structure `J_full` assembled in `KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md`, the Kähler triple of `KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md` (whose symplectic leg the next path invokes), the real-Lagrangian polarization of `KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md`, the five holomorphic G_amb-idempotents `{4,4,6,6,12}` of `KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md`, and the rank-12 self-conjugacy of `KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md`.
