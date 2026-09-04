# KCPT Dirac-radius grading of End_H(C^64): P = D2·J_full is the negative Dirac-radius operator −|D2|, block-scalar with eigenvalue −2√m on each of the six CP-completed constituents, and it does NOT separate 12⁺ from 12⁻ (both radius-degenerate at m = 1)

**Type:** bounded_theorem
**Date:** 2026-07-20
**Lane:** KCPT (L = 4, N = 64 staggered qubit lattice over the 4³ cube)

## Claim boundary

Define the operator `P := D2·J_full` on `C^64`, from the antisymmetric integer staggered adjacency `D2` and the named all-plus total complex-structure representative `J_full` (the kernel + bulk assembly `J_ker + Σ_{m∈{1,2,3}} D2·P_m/(2√m)`). Everything below is exact finite-dimensional linear algebra over `C^64`; the runner rebuilds every object from the bare site construction with no import of another runner. All group labels are **geometric labels for lattice operators only**. "CP" throughout is the label for the geometric lattice parity involution `S_eps = diag((−1)^{x₁+x₂+x₃})` and its index-2 extension `H = ⟨G_amb, S_eps⟩`; **nothing here is a statement about Standard-Model CP.** The theorem fixes no free parameter and supplies no selector for the bulk sign family: it evaluates the already named representative `J_full`. It is r-neutral and orientation-neutral.

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

So the `m = 1` shell (dim 24) is exactly `12⁺ ⊕ 12⁻`, and the `m = 2` shell (dim 24) is the two induced 12's. **The Dirac-radius grading is strictly coarser than the constituent grading, and on the rank-12 CP-doublet it is constant.** The two halves are inequivalent `H`-constituents related by the quotient sign character, `12⁻ ≅ 12⁺ ⊗ χ_sgn`; the superscripts do **not** mean that `S_eps` acts pointwise as `+I` or `−I` on either half. The fixed operator `P = D2·J_full` assigns the same scalar `−2` to both quotient-sign-related constituents. This is the exact **negative** answer to the forward question left by the CP-completion note: the Dirac radius, and this operator `P`, do not distinguish `12⁺` from `12⁻`. No broader claim about all `H`-invariant data follows.

## T4 — anti-fabrication contrast (why block-scalarity is non-vacuous)

The block-scalar structure is genuinely bought by the even product, not inherited:

- `D2` **alone** is not H-invariant (`max_h ||[D2, h]|| ≥ 1`) and not block-scalar; it carries a **nonzero** `S_eps`-odd off-block `|Z_{12⁺}ᴴ D2 Z_{12⁻}| ≈ 1.24 ≠ 0`, i.e. `D2` maps `12⁺ ↔ 12⁻`, whereas `P`'s off-blocks vanish (`< 1e-9`). `J_full` alone is likewise not H-invariant (`max_h ||[J_full, h]|| ≥ 0.5`).
- The rational `√m → 1` proxy for `J_full` fails `J² = −I` and yields the **wrong integer spectrum** `−2m ∈ {0, −2, −4, −6}`, distinct from `P`'s irrational `−2√m`. No parity/sign/integer stand-in reproduces the `±2√2, ±2√3` shell radii; the shell `√m` normalizers are load-bearing.

## Honest boundary

Geometric-label only, and a **negative** structural result about one fixed operator. `P` fixes no free parameter and supplies no sign-family selector; it is evaluated for the named representative `J_full`, and is r-neutral and orientation-neutral. For a different bulk-shell sign tuple, the corresponding product has the same shell radii but may reverse individual shell signs, so the all-negative closed form is specific to `J_full`; the `m=1` degeneracy of its two quotient-sign-related halves is the result used here. "CP" is the geometric label inherited from the `S_eps` extension, not Standard-Model CP, and the `12⁺/12⁻` superscripts are quotient-character labels rather than pointwise `S_eps` eigenvalues. This note registers what `P` does and does not grade — it does not derive any physical mass, angle, or sign.

## The next path this opens

Since `M = −4I` on all of `12⁺ ⊕ 12⁻`, no polynomial, spectral function, or higher Casimir built only from `M` can separate the pair. The symplectic leg `ω = −J_full` is likewise not an `H`-invariant scalar separator: it is `χ_sgn`-covariant under `S_eps` and can pair the quotient-sign partners rather than assign them distinct invariant scalars. The multiplicity-free `H`-commutant already contains the two central constituent projectors; the open constructive question is instead to find a geometrically natural closed form, outside the functional calculus of `M`, for an `H`-invariant such as their projector difference that has distinct scalar values on `12⁺` and `12⁻`.

## No-Go Discipline gate for the narrow fixed-operator corollary

**Exact negative claim tested:** on this fixed `L=4` carrier and the Unit-14 decomposition, `P = D2·J_full = −√(−M)` restricts to `−2I` on each of the quotient-sign-related constituents `12⁺` and `12⁻`; therefore `P` and the Dirac-radius grading alone do not distinguish them. This is not a claim that `S_eps` acts pointwise as `±I`, that no other `H`-representation datum separates the constituents, or that the conclusion extends to other lattice sizes or physical CP.

### N1 — five distinct attacks

1. **ATTEMPTED — direct constituent restrictions.** Compress `P` to the two `12`-dimensional subspaces and look for unequal block scalars. Both restrictions equal `−2I` within the stated residual.
2. **ATTEMPTED — common spectral-shell support.** Test whether either half leaves the other's `M`-shell. Both halves lie wholly in the `24`-dimensional `m=1` shell.
3. **ATTEMPTED — closed functional calculus.** Use `P=−√(−M)` to look for distinct radius values despite the common `M` eigenvalue. Functional calculus sends `M=−4I` to the single value `−2I` on the whole shell.
4. **ATTEMPTED — off-diagonal mixing.** Test `Z_+^† P Z_-` as a possible distinguishing channel. It vanishes within tolerance, while `D2` supplies a nonzero contrast.
5. **ATTEMPTED — commutant coordinates.** Read the two scalar coordinates of this particular `P` in the multiplicity-free algebra `End_H(C^64)`. They are equal. Other commutant idempotents can distinguish the constituents; this route closes only the claim about `P`.

These routes use different primary objects and terminal obligations: compressed blocks, shell support, spectral functional calculus, cross-block mixing, and commutant coordinates.

### N2 — wall independence

No multiple no-go walls are asserted. The fixed carrier, the Unit-14 decomposition, and the specified operator `P` are domain hypotheses of the finite theorem, not independent missing premises.

### N3 — hidden-wall scan

The fixed surface, named `J_full` representative, geometric meaning of the `12⁺/12⁻` labels, and absence of dynamics or physical identification are explicit. No appeal to standard QFT, a hidden selector, a fitted value, or an unstated framework primitive is load-bearing.

### N4 — residual matching

The Unit-14 forward question asks what geometric data distinguish its two quotient-sign-related constituents. The residual closed here is narrower and exact: whether `P`, equivalently the `M`-radius on this fixed representative, distinguishes that same pair. Unit 9 supplies sign-reversal premises and is not used as a prior no-go witness.

### N5 — rhetoric and resolution

The equality is checked on every vector of the two blocks through `P|_{12⁺⊕12⁻}=−2I`, on each constituent block, on the full `m=1` shell, and in the full finite-lattice spectrum. Other lattice sizes, a continuum limit, pointwise `S_eps` eigenvalues, Standard-Model CP, and other `H`-invariants are untested and unclaimed.

### N6 — partial-closure paths

No new axiom or primitive is required. Functions of `M` are excluded as separators by the common shell. The `χ_sgn`-covariant form `ω` can pair the halves but is not an invariant scalar separator. The already existing central `H`-idempotents distinguish the inequivalent constituents algebraically; the open path is a natural closed form for such a separator outside `C[M]`.

### N7 — steelman

The strongest objection is that the pair is already distinguished by inequivalent `H`-representation types and by their distinct central idempotents, so a claim that no `H`-invariant datum separates them would be false. That objection fixes the scope but does not defeat the stated corollary: this particular `P` has equal central coordinates `−2,−2`, zero cross-block, and cannot refine the shared `M` eigenspace.

### N8 — cross-cycle echo

Repository precedents warn against promoting failure of one operator into a universal no-go. The present result follows that lesson by restricting the conclusion to `P` and the functional calculus of `M`; it does not treat an untested route, a convention, or an approved primitive as foreclosed.

**No-Go Discipline disposition:** `PASS` for the narrow fixed-operator corollary above; no broader no-go ships.

## Runner evidence

`scripts/kcpt_dirac_radius_grading_of_end_h_2026_07_20.py` (paired), cached at `logs/runner-cache/kcpt_dirac_radius_grading_of_end_h_2026_07_20.txt`. Class-A finite-dimensional check, `TOTAL: PASS=15 FAIL=0`.

| Gate | what it certifies | count |
|------|-------------------|-------|
| G1 | \|G_amb\| = 768; \|H\| = 1536 = 2·768; G_amb ⊆ H, coset S_eps·G_amb ⊆ H and disjoint (index 2) | 1 |
| G2 | J_full² = −I, antisymmetric; ANTI-PROXY: √m→1 proxy fails J² = −I and differs from J_full (shell √m normalizers load-bearing) | 1 |
| G3 | P := D2·J_full real-symmetric (‖P−Pᵀ‖ < 1e-9) because D2, J_full COMMUTE (‖P−J_full·D2‖ < 1e-9); P ≠ D2, P ≠ J_full | 1 |
| G4 | THE THEOREM: max_{h∈H} ‖[P,h]‖ < 1e-9 over all 1536 elements — P ∈ End_H(C^64), the c_H = 6 commutant | 1 |
| G5 | ANTI-FAB CONTRAST: neither factor H-invariant (‖[D2,h]‖ > 1, ‖[J_full,h]‖ > 0.5); direct residuals verify both factors S_eps-odd and the product S_eps-even; S_eps preserves the D2²-shells | 1 |
| G6 | exact-integer commutant pins: c_G = 12, c_H = 6 (Σtr²/\|G\|); coset traceless (Σtr² = 0, max\|tr\| = 0) | 1 |
| G7 | the six Unit-14 constituents rebuilt object-identically: dims (sorted) [8,8,12,12,12,12] = 6 = c_H; exactly 2 CP-split (both rank-12 W-source), 4 induced | 1 |
| G8 | CLOSED FORM P == −\|D2\| == −√(−D2²): ‖P − (−√(−M))‖ < 1e-9 (\|D2\| from an INDEPENDENT eigh(M)); M-shell dims [8,24,24,8]; P's own spectrum tiles the same | 1 |
| G9 | BLOCK-SCALAR CENSUS: on every constituent Z_iᴴ P Z_i = λ_i I (max ‖blk − λI‖ < 1e-9), λ_i == −2√(m_i) with m_i from an INDEPENDENT Z_iᴴ M Z_i; P block-diagonal | 1 |
| G10 | THE COMPUTED ASSIGNMENT: the quotient-sign-related pair {12⁺,12⁻} is at m = 1 (RADIUS-DEGENERATE, λ = −2); induced 12's at m = 2 (λ = −2√2); induced 8's at the extreme shells {0,3} | 1 |
| G11 | ANTI-FAB: D2 alone has a nonzero S_eps-odd off-block \|Z_{12⁺}ᴴ D2 Z_{12⁻}\| > 1 and is not block-scalar; √m→1 proxy has exactly the integer block-value set {−6,−4,−2,0}, not −2√m | 1 |
| G-PIN-U14 | Unit-14 note contains `9216 / 1536 = 6` (c_H = 6, the six constituents P is block-scalar on) | 1 |
| G-PIN-U9 | Unit-9 note contains `S_eps J_full S_eps = -J_full` (with S_eps D2 S_eps = −D2, the two sign reversals that make P S_eps-even → H-invariant) | 1 |
| G-PIN-SELF | this note carries exactly two KCPT dependency links (Units 14, 9); Units 8/10/11/12/13 backticked only | 1 |
| G-MEM | greedy generating sets close to exactly 768 / 1536 with loose length bounds; commutant kron stacks use generators only (OOM-avoiding) | 1 |

## Dependencies

- [Unit 14 CP-completion under the extended group](KCPT_CP_COMPLETION_UNDER_EXTENDED_GROUP_BOUNDED_THEOREM_NOTE_2026-07-20.md) — the six CP-completed H-constituents `C^64 = 8 + 8 + 12 + 12 + 12⁺ + 12⁻` and the `9216 / 1536 = 6` commutant count, the constituents that `P` is tested against, and the `12⁺/12⁻` split whose radius-degeneracy is the payload here.
- [Unit 9 chiral-parity common-sign-orbit](KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md) — the two exact sign reversals `S_eps·D2·S_eps = −D2` and `S_eps J_full S_eps = -J_full` whose product makes `P` `S_eps`-even, hence H-invariant; and `S_eps·M·S_eps = M`, so `S_eps` preserves the Dirac-radius shells.

Units 8, 10, 11, 12, 13 enter only transitively through Units 14 and 9 and are referenced by name only, never as dependency links: the total complex structure `J_full` assembled in `KCPT_TOTAL_COMPLEX_STRUCTURE_AMBIENT_INVARIANT_KERNEL_BULK_ASSEMBLY_BOUNDED_THEOREM_NOTE_2026-07-19.md`, the Kähler triple of `KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md` (whose symplectic leg the next path invokes), the real-Lagrangian polarization of `KCPT_CHIRAL_PARITY_LAGRANGIAN_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-19.md`, the five holomorphic G_amb-idempotents `{4,4,6,6,12}` of `KCPT_HOLOMORPHIC_GAMB_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-20.md`, and the rank-12 self-conjugacy of `KCPT_HOLOMORPHIC_REALITY_CP_CENSUS_FROBENIUS_SCHUR_BOUNDED_THEOREM_NOTE_2026-07-20.md`.
