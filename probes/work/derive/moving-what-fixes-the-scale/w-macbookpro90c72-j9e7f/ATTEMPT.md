# J:derive:moving-what-fixes-the-scale:a4 — w-macbookpro90c72-j9e7f

Attempt 4 of 5, by claude-opus-5-5 (all of `check.py` and this file). `python3 check.py` prints 5 `ok` lines, exits 0
with `FAIL` empty, and runs in about 1 s. All arithmetic is exact:
- sympy for identities in the symbols `p, q, r, c, z, x`;
- `Fraction` and integers for window enumerations.

**Setting.** Block 39 (PR #8530, branch `…block39-records-that-move…`), with its note's `claim_scope` read in full:
- a site is empty or carries one record, whose content is one of six axes;
- a record weighs `z`;
- two neighbouring records weigh `c·ω`, where `ω = p, q, r` for equal, opposite and orthogonal contents;
- a bond with an empty end weighs `1`.

Notation: `A₁ = p+q+4r` and `c₀ = 6/A₁`.

**Prior attempts.** a1 (`w-jonathonsmac4f50-j882f`), a2 (`…-jc19a`) and a5 (`…-jc532`) are all claude-opus-5, and all
are unrefereed. Their results:
- a1: (a) only a relation; (b)'s second half impossible; (c) only on average.
- a5: (b)'s spectral half, `det T = c⁵(p−q)³(p+q−2r)²(c·A₁ − 6)`; and (d), consistent for no scale.
- a2: "no state is privileged" is a one-bond statement.

Their open items were:
- candidate **(e)** (untouched by all three);
- a2 §4.1: are the two `p+q = 2r` conditions one structure?
- a5 §3: the strict-contraction phrasing of (b).

a5 §4.2 (the `(5,2,4)` reflection-positivity question) is already settled by block 39's current T5. That text states
RP "exactly when `p ≥ q`, `p + q ≥ 2r` and `c ≥ c₀`", so it is not re-done here.

My own plan, formed before reading them, was to ask what `c` does to the law of **which sites are occupied**. That
turns out to be the missing piece. It answers the three open items and gives (e) an exact form.

## 1. Statement attempted

1. **(S1) One spectrum behind every scale statement.**
   - `ω = A₁·P_u + λ₂·P₂ + λ₃·P₃`, where `λ₂ = p+q−2r` and `λ₃ = p−q`.
   - `P_u`, `P₂` and `P₃` are orthogonal projectors of ranks 1, 2 and 3. Their entries by pair class (equal / opposite /
     orthogonal) are: `P_u` 1/6; `P₂` 1/3, 1/3, −1/6; `P₃` 1/2, −1/2, 0.
   - Every statement that fixes a scale is a statement about `A₁` (through `c·A₁ = 6`).
   - Every scale-free obstruction is a statement about `λ₂` and `λ₃`. In particular, a2's orthogonal degree-2 branch
     (`λ₂ = 0`) and block 39's RP side condition (`λ₂ ≥ 0`) are conditions on one eigenvalue.
2. **(S2) The occupancy law.** On every window, the marginal law of the occupied set `n` is
   `μ_occ(n) ∝ (6z)^|n| · (c/c₀)^{b(n)} · ∏_C L_C`, where:
   - `b(n)` is the number of occupied bonds;
   - `C` runs over the clusters (connected components of `n`);
   - `L_C = Z_C(ω)·6^{b_C−k_C}/A₁^{b_C}` depends on neither `c` nor `z`;
   - `L_C = 1` for every tree cluster;
   - for an `ℓ`-cycle, `L = 1 + (2λ₂^ℓ + 3λ₃^ℓ)/A₁^ℓ`. At `(3,1,2)` the plaquette gives `433/432` and the full `2×3`
     cluster `15625/15552`.
3. **(S3) What this fixes.**
   - `c/c₀` is exactly the **bare per-bond binding** of the occupancy pattern. `c₀` is the unique scale with no bare
     record–record binding.
   - At `c₀` the occupancy on any cycle-free window is i.i.d. Bernoulli with parameter `6z/(6z+1)`.
   - On a window of `Zᵈ` with a cycle, no scale makes the occupancy independent unless `p = q = r`.
4. **(S4, candidate (e)) A change of the length unit.** On the chain, exact decimation maps
   `x = c·A₁ ↦ 6 + z(x−6)²/(zx+1)²` and `z ↦ z((zx+1)/(6z+1))²`, and the decimated chain stays in the `(p,q,r)` family.
   - So `c₀` is the only binding scale, and the only point with an invariant fugacity, that a change of unit leaves
     fixed. Every other scale flows.
   - In `d ≥ 2` the property behind this — independent occupancy — fails at every scale on windows with a plaquette.
5. **(S4, (b)'s remaining half).** The chain's transfer matrix is a strict contraction off its top state for every
   `c > 0`. `c₀` is where one of its eigenvalues reaches 0, i.e. the RP threshold, not a contraction threshold.

## 2. Steps

**S1 — spectral table. PROVED; CHECKED.**
- `ω` commutes with the six-value symmetries, so it lies in the span of `1`, the antipode `J` and the all-ones `𝟙𝟙ᵀ`.
- `P_u = 𝟙𝟙ᵀ/6`.
- `P₂` is the axis-even traceless part: `½·[same axis] − 1/6`.
- `P₃` is the antipode-odd part: `½(1 − J)`.

CHECKED as symbolic identities:
- `ω = A₁P_u + λ₂P₂ + λ₃P₃`;
- `P_k² = P_k`, `P_aP_b = 0` and `ΣP_k = 1`, with traces 1, 2, 3.

Consequence (PROVED, CHECKED). At `c₀`, a2's averaged-record weight between contents `a` and `b` is
`c₀²(ω²)_{ab}/6 = 1 + 6(λ₂²P₂ + λ₃²P₃)_{ab}/A₁²`. By class this is:
- equal: `1 + (2λ₂² + 3λ₃²)/A₁²`;
- opposite: `1 + (2λ₂² − 3λ₃²)/A₁²`;
- orthogonal: `1 − λ₂²/A₁²`.

An orthogonal pair sees only the `λ₂`-mode, because `P₃` vanishes between different axes. So a2's `12r(p+q+r) −
A₁² = −λ₂²` is exactly this entry. Block 39 T5's `T ⪰ 0` needs `λ₂ ≥ 0` for the same eigenvalue (a5's factor
`(p+q−2r)²`). This answers a2 §4.1: one mode, seen once as an equality and once as an inequality.

**S2 — the occupancy law. PROVED; CHECKED.**
1. Sum the law over contents with the occupied set `n` fixed. The weight is `z^|n| c^{b(n)} Z_n(ω)`, and `Z_n`
   factorises over clusters, since no bond joins two clusters.
2. Writing `Z_C = 6^{k_C}(A₁/6)^{b_C}·L_C` defines `L_C` and gives `(6z)^|n| (c/c₀)^{b} ∏L_C`, using `c·A₁/6 = c/c₀`.
3. `L_C` contains only `ω`, not `c` or `z`.
4. Trees: `Σ_s ω(s,t) = A₁` for every `t`. So summing a leaf's content multiplies by `A₁` and removes one site and one
   bond. Peeling the tree down to one site gives `Z_C = 6A₁^{k−1}`, so `L_C = 1`.
5. An `ℓ`-cycle: `Z_C = tr ω^ℓ = A₁^ℓ + 2λ₂^ℓ + 3λ₃^ℓ` by S1, so `L_C = 1 + (2λ₂^ℓ + 3λ₃^ℓ)/A₁^ℓ`.

CHECKED by brute force over all occupied sets and all contents:
- windows path4, star4, comb6, `2×2` and `2×3`;
- triples `(3,1,2)`, `(5,2,4)` and `(7,3,5)`;
- `(c, z) = (c₀, 1/3)`, `(2c₀, 2/5)` and `(c₀/3, 7/2)`.

The whole factorisation holds exactly. `L_C = 1` on every tree cluster that occurs, and the 4-cycle formula holds at
all three triples: `433/432` at `(3,1,2)`, where `433/432 = 20784/20736 = tr ω⁴/A₁⁴`.

**S3 — consequences. PROVED; CHECKED.**
1. Independence needs `c = c₀` (PROVED). Occupancy is i.i.d. iff the weight is `ρ^|n|`. Compare two adjacent occupied
   sites with two non-adjacent ones: the pair weights are `(6z)²(c/c₀)` and `(6z)²`, which agree iff `c = c₀`.
2. At `c₀` on a cycle-free window every `L_C = 1`, so `μ_occ(n) ∝ (6z)^|n|`: i.i.d. Bernoulli(`6z/(6z+1)`).
   CHECKED on path4, star4 and comb6 at `(3,1,2)`, `z = 1/3`.
3. With a cycle, independence also needs `L = 1`. On `Zᵈ` every cycle is even, so `2λ₂^ℓ + 3λ₃^ℓ = 0` forces
   `λ₂ = λ₃ = 0`, i.e. `p = q = r`, the constant rule. CHECKED at `c₀` on the plaquette:
   `P(all occupied) = 433/2188 > (2/3)⁴`.

**What this says about the scale.**
- The rule `K`, normalised over contents, is blind to `c` (block 39 T2).
- S2 shows exactly what `c` adds on top of `K`: a content-independent attraction `log(c/c₀)` per occupied bond.
- So "records interact only through the rule" — no bare record–record binding beyond `ω` — is a principle that fixes
  `c = c₀`. It is not circular: it is stated for the occupancy law, not for an average.
- It is the principle behind a1's (c) (the averaged formation rate) and a5's determinant. But it is a statement about
  the **law**, and it is exact on forests.
- On cycles the rule itself binds records, through `L_C > 1`, at every scale.

**S4 — the length unit (candidate (e)). PROVED; CHECKED.**

Setup:
- The chain's weight is `∏ D(η_i) ∏ K(η_i, η_{i+1})`, with `D = diag(z·1₆, 1)`.
- Summing every other site gives `K D K`.
- Re-gauging the empty state by `g` (`K ↦ GKG`, `D_∅ ↦ D_∅/g²`, then moving `g²` into `z`) and normalising restores
  "empty-end bond = 1".
- The record–record block `zc²ω² + 𝟙𝟙ᵀ` has class-constant entries, so the decimated chain is again a `(p', q', r')`
  law. CHECKED at `(3,1,2)` and `(5,2,4)`.

On `span{u, e_∅}` (`u` the uniform record) the kernel is `B = [[x, √6], [√6, 1]]` with `x = c·A₁`. The algebra
(symbolic, CHECKED) gives:
- `x' = (zx²+6)(6z+1)/(zx+1)²`, so `x' − 6 = z(x−6)²/(zx+1)²`;
- `z' = z((zx+1)/(6z+1))²`.

Hence:
- `x = 6`, i.e. `c = c₀`, is the unique fixed point, and the unique point with `z' = z`.
- At `c₀`, `B = wwᵀ` with `w = (√6, 1)` has rank one, so `B(DB)^{m} = (6z+1)^m B` for every block size.
- CHECKED on the full 7-state kernels at `(3,1,2)` and `(5,2,4)`, for `z = 1/3, 5/2` and blocks of 2 and 3:
  - at `c₀`, `x' = 6` and `z' = z`;
  - at `2c₀`, both move, with `x' > 6`.

For `x ≠ 6` the flow is `x' ≥ 6` after one step, then `0 < x' − 6 ≤ (x−6)/4` (since `zx/(zx+1)² ≤ 1/4`). So every
scale flows to the neutral one.

The natural-unit gate of the memo ("the scale-reference primitive and … that the framework's natural unit equals the
Planck length") concerns the conversion of lattice units. `c` is dimensionless, so a unit choice cannot fix it
directly (PROVED: no lattice probability depends on the unit). The only tie S4 finds is **unit covariance**: the
requirement that the law written at a coarser unit has the same binding scale. On the chain that tie selects `c₀`
exactly.

In `d ≥ 2`, exact decimation leaves the nearest-neighbour family. Moreover S3 shows that at every scale the occupancy
on a window with a plaquette is not independent. So the property that makes `c₀` unit-invariant on the chain is
absent there, and (e) gives no exact selection in `d ≥ 2`.

**S4 — (b)'s strict-contraction half. PROVED; CHECKED.**
- The chain's transfer matrix `D^{1/2}KD^{1/2}` has positive entries. By Perron–Frobenius (the elementary finite
  form) its top eigenvalue is simple and strictly exceeds every other in modulus, for every `c > 0`. That is a strict
  contraction off the top state at every scale.
- CHECKED at `(3,1,2)`, `z = 1/3`, `c = 1/4, 1/2, 1`. At `c₀ = 1/2` the spectrum is:
  - `3` (top);
  - `1/3` (×3, the `λ₃`-mode);
  - `0` (×3: the `λ₂`-mode, which is 0 at `(3,1,2)`, and the empty–record direction).
- So `c₀` is where an eigenvalue of the `B` block reaches 0. That is block 39's reflection-positivity threshold, not a
  contraction threshold.

**ASSUMED.**
1. The uniform counting measure on the six contents. It is the one the law with vacancies uses, and "no possibility is
   privileged" supports it. As a1 notes, another prior would move `c₀`.
2. The Perron–Frobenius theorem for matrices with positive entries: the top eigenvalue is simple and strictly largest
   in modulus. It is used only for the "every `c > 0`" clause of S4(b). At the three scales checked, the spectra are
   exact.

## 3. Where the route stops
- **The exact selection of `c₀` holds on forests and on the chain only.** On `Zᵈ` with cycles:
  - (e)'s unit covariance has no exact form, because decimation leaves the family;
  - "no bare binding" still fixes `c₀` as the per-bond factor.

  But the rule's own loop factors make the occupancy correlated at every scale. So `c₀` is canonical as "no binding
  beyond the rule", but it is not "no binding".
- **The principle is a choice.** "Records interact only through the rule" fixes `c₀`. The rival reading — records have
  a bare attraction, which is what makes block 39's executed clumping onset depend on `c` — is equally consistent
  with the axioms. S2 makes the choice sharp: it is the per-bond factor `c/c₀`. It does not make the choice for the
  owner.

## 4. What would finish it
- **In three dimensions, a coarse-graining that keeps the loop factors.** For example, blocks of `2×2×2` with the
  cube's loop factor, to test whether `c₀` is at least an approximate fixed point of an honest RG map, and at which
  order the loop factors shift it.
- **The executed clumping onset (block 39) read against S2.** At fixed density the onset's dependence on `c` should
  enter only through `c/c₀`, the bare coupling, plus scale-free loop factors. A run of `moving_gas.py` along lines of
  constant `c/c₀` for two different `(p,q,r)` with equal `λ₂, λ₃` would test that.
- **An independent referee from another model family** for S2–S4. All four attempts on this problem are Claude models.
