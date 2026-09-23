# Parity-odd couplings under the 24 proper rotations only — attempt 1

Worker `w-jonathonsmac4f50-jb5a4`, model `claude-opus-5-5`. The notes used were written by the campaign supervisor, who is from the same model family (Claude). A referee from another family should read every step.

No prior attempts were printed at claim time. Own prior art checked:
- block 54 T1 (#8570). It gives the three-parameter family, and its part (c) is the content-reversing inversion.
- block 65 T4 (#8596). The twist hop's scalar is `−(1/8) ε·T`.
- block 70 T3 (#8602). It defines the two classes and states that `Θ` and `Π` act on all five kinds of field.
- block 77 (#8612) and the fork probe §4.2 (#8572). The scalar hop `a` splits the species 1:3:3:1 by sense.
- my own probe `filling-between-the-a-terms-levels-chiral-content`. The Berry charges on the Fermi sheets total zero. That is a statement about net chirality, not about inversion, so it does not conflict with anything here.

## 1. Statement attempted

The Lattice axiom names only the 24 proper rotations. The content is soldered: the qubit turns with the lattice as a direction.

**(a) Generator.** Classify the terms by their behaviour under every inversion.
- The terms are the translation-invariant, hermitian, nearest-neighbour generators covariant under the 24.
- The inversions allowed are `x → −x` composed with any site-local unitary or antiunitary map of the coin, site by site.

**(a) Field energy.** Classify the parity-odd densities with at most two derivatives. Two field contents are covered:
- block 64 T2's frame class, with the frame index contracted by tensors invariant under the 24 instead of SO(3);
- a rate field `u = log w` together with a rotation field `ϑ`, where `ϑ` is block 65's twist taken as a separate field.

**(b)** For each odd term, decide whether it is odd under `ΘΠ`, the map that exchanges block 70's two classes.

**(c)** For each odd term, decide whether it survives per-tick counting and blindness.

**(d)** Name an observable handedness, and say whether the supplied clauses contain one.

**Result.**

*Field energy.*
- The parity-odd sector is exactly `c₅ det e (ε·T)`. With `ϑ` separate it is instead `div ϑ` (with rate weights), `∇u·ϑ` and `ϑ·curl ϑ`.
- Blindness removes all of these. Point by point, as per-tick counting requires, it forces `c₅ = 0` already at zero strain.

*Generator.*
- The two inversions that keep the walk both reverse the scalar hop `a`. They are `ΘΠ` (block 54 T1(c), block 70) and `εΠ`, where `ε = (−1)^{x₁+x₂+x₃}`.
- `a` survives per-tick timing, and it survives blindness via the completion `−a Σ_j S_j[(∂_jϑ)·σ]`.
- For `aβ ≠ 0`, no inversion composed with any site-local unitary or antiunitary is a symmetry.
- Obstruction: an exact chiral 8-step loop with `τ(γ*) − τ(−γ*) = −a³β⁵`.
- Observable: a chiral rate field and its mirror image have different spectral moments, first at the 8th.

*Supplied clauses.* They contain no handedness. The walk has `a = 0`, and the supplied field energies are even.

## 2. Steps

Conventions:
- `(Tⱼψ)(x) = ψ(x+eⱼ)`
- `Sⱼ = (Tⱼ − Tⱼ†)/(2i)` and `Cⱼ = (Tⱼ + Tⱼ†)/2`, as in block 65
- the family is `H = a₀ + 2a Σ Cⱼ + β Σ σⱼSⱼ`, with symbol `a₀ + 2aΣcos k + βΣσⱼ sin kⱼ`, as in block 54
- `Π ψ(x) = ψ(−x)`
- `Θ = σ₂ × (complex conjugation)`, as in block 70
- `ε = U₍₁₁₁₎`

A linear `P` is a symmetry of the evolution iff `PHP⁻¹ = H`. An antilinear `P` is one iff `PHP⁻¹ = −H`; this is block 54 T1(c)'s criterion. Both hold up to a constant, which is a global phase.

**Step 1 (CHECKED A1).** The translation-invariant, hermitian, nearest-neighbour generators covariant under the 24 form a real space of dimension three: `a₀, a, β`.
- The exact nullspace is taken over all 24 adjoint actions `Ad_R(x₀ + x·σ) = x₀ + (Rx)·σ` together with hermiticity.
- There are 56 real unknowns.
- This re-derives block 54 T1(a) with separate machinery.

It follows that there are no further nearest-neighbour terms, odd or even.

**Step 2 (PROVED, CHECKED A2): the inversions that commute with the rotations, and the parity table.**

*Coin maps.*
- A linear coin map `V` must commute with the lifts `(1 − iσ_c)/√2`, so it commutes with every `σ_c` and is a scalar.
- An antilinear map `VK` must satisfy `V σ̄_c = −σ_c V`, so `V ∝ σ₂`.
- A site-sign pattern `(−1)^{n·x}` is kept by the 24 only for `n = 000` and `111`.
- Translations commute with `H`, so moving the centre of inversion changes nothing.

*The four maps.* Up to phase they are `Π`, `εΠ`, `ΘΠ` and `ΘεΠ`. Their effect on the symbol, checked exactly:

| map | a₀ | a | β |
|---|---|---|---|
| Π (linear) | keeps | keeps | breaks |
| εΠ (linear) | keeps | **breaks** | keeps |
| ΘΠ (antilinear) | breaks | **breaks** | keeps |
| ΘεΠ (antilinear) | breaks | keeps | breaks |

The two maps that keep the walk are `ΘΠ` and `εΠ`. Both reverse `a`.

`a₀` is a global phase `e^{−ia₀t}` and changes no observable, so it is set aside.

*The task's premise, "block 54's family is parity-even".* This holds only for the classical parity of the symbol, where σ is treated as a polar vector.
- No linear map reverses all three `σⱼ` (block 54 T1(b)).
- The antilinear implementation reverses the sign of the evolution.
- So the classically even terms `a₀` and `a` are exactly the ones that break it. Block 54 T1(c) says the same: "content reversed ⇒ a₀ = a = 0".

**Step 3 (PROVED from Step 1; CHECKED A3): no site-local inversion of any kind when `aβ ≠ 0`.**

*Setup.*
- Let `g` be any improper lattice isometry.
- Let `W = ⊕ₓ Wₓ`, where each `Wₓ` is an invertible 2×2 matrix that may be different at every site.
- Consider `P = W∘g` (linear) or `P = W∘K∘g` (antilinear).
- For a closed walk `γ = (x₀, …, x_L = x₀)`, define `τ(γ) = tr Πᵢ H_{xᵢ,xᵢ₊₁}`.

*The constraint.*
- Linear case: `PHP⁻¹ = H` reads `H_{x,y} = Wₓ H_{g⁻¹x, g⁻¹y} W_y⁻¹`. The factors of `W` cancel around a closed walk, so `τ(γ) = τ(g⁻¹γ)`.
- Antilinear case: `PHP⁻¹ = −H` gives `τ(γ) = (−1)^L conj τ(g⁻¹γ)`.

*Reducing to `−γ`.*
- The family commutes with `Θ` (A6), so `τ` is real.
- Lattice walks are closed only for even `L`.
- So both cases require `τ(γ) = τ(g⁻¹γ)`.
- By covariance (Step 1), `τ(Rγ) = τ(γ)` for every proper `R`, so `τ(g⁻¹γ) = τ(−γ)` for every improper `g`.

*The chiral loop.* Take `γ* = (e₁, e₁, e₂, −e₁, −e₂, e₃, −e₁, −e₃)`. Exactly:
- `τ(γ*) − τ(−γ*) = −a³β⁵`.
- A3 also checks `τ(Rγ*) = τ(γ*)` for all 24 rotations.
- No closed 6-step walk has a mirror-odd trace. There are 1860 of them. The odd part is `β(c₁a⁵ + c₃a³β² + c₅aβ⁴)`, and it vanishes at `β/a = 1, 2, 3`, hence identically.
- 2688 of the 44730 closed 8-step walks are chiral.

*Conclusion.* Such a `P` exists iff `aβ = 0`:
- if `a = 0`, `ΘΠ` and `εΠ` work;
- if `β = 0`, `Π` works;
- otherwise nothing does.

**Step 4 (CHECKED A4): an observable.**

*Setup.*
- On the 4³ torus take an integer rate field `w`, generic and therefore chiral.
- Compare it with its mirror image `w(−x)` and with a quarter-turned copy.
- `wH` is similar to the clocked `φHφ` (block 54 T2), so the moments `tr((wH)^L)` are spectral data of the clocked walk.

*Results with (a, β) = (1, 2), using Gaussian-integer arithmetic with a proven int64 bound:*
- the moments of `w` and of its mirror image agree for `L ≤ 7`;
- at `L = 8` they differ: `tr((2wH)⁸) = 4083834945536` against `4082722668544`;
- for `a = 0` and for `β = 0` all eight moments agree;
- the rotated field gives equal moments in all three cases.

*Conclusion.* A chiral pattern of clocks and its mirror image give the clocked walk different frequencies exactly when `aβ ≠ 0`.

**Step 5 (PROVED, CHECKED A5): blindness does not select generator terms, and the completion of `a`.**

*Definition.* For any nearest-neighbour hermitian `X`, set `X[ϑ] := X − (i/2)[ϑ·σ, X]`. It is nearest-neighbour, because `ϑ·σ` is site-diagonal, and it is hermitian.

*Blindness to first order.* Take `U = e^{−iθ·σ/2}`. Then `U X[ϑ] U† = X[ϑ+θ] + O(θϑ, θ²)`. This is block 65 T2's sense of blindness.

*Response identity.* `∂X[ϑ]/∂ϑ_c(x) = −(i/2)[σ_c(x), X]`. Hence `d⟨X[ϑ]⟩/dϑ_c(x) = ½ d⟨σ_c(x)⟩/dt` under the evolution generated by `X`. It vanishes on stationary states. This is block 65 T3 for any `X`, so a field energy independent of `ϑ` stays consistent for the whole family.

*Explicit completion of the scalar hop* (exact on a 3³ torus with a rational `ϑ`):
- `−(i/2)[ϑ·σ, Σⱼ(Tⱼ+Tⱼ†)] = −Σⱼ Sⱼ[(∂ⱼϑ)·σ]`
- Here `Sⱼ[v]ψ(x) = (1/2i)(v(x)ψ(x+eⱼ) − v(x−eⱼ)ψ(x−eⱼ))` and `∂ⱼϑ = ϑ(x+eⱼ) − ϑ(x)`.
- This is a coin-vector hop in all three coin components, unlike the walk's scalar twist hop.
- The same code reproduces block 65 T1 in these conventions.

*Parity is preserved by completion.* `(X[ϑ])^{ΘΠ} = (X^{ΘΠ})[ϑ']` with `ϑ'(x) = ϑ(−x)`. The reasons: `ΘΠ(ϑ·σ)(ΘΠ)⁻¹ = −ϑ'·σ`, and antilinearity reverses `i`.
- The completed scalar hop maps to `+`(itself in `ϑ'`).
- The completed walk maps to `−`(itself in `ϑ'`).
- So `a` stays odd relative to the walk once completed.

**Step 6 (PROVED, CHECKED A5): per-tick timing.**
- The clause `i dψₓ/dτₓ = (Hψ)ₓ` times every generator term (block 54 T2), so `a` included.
- Under `ΘΠ`, `φCφ → +φ'Cφ'`, where `φ'` is the mirrored clock field, while `φWφ → −φ'Wφ'`.

**Step 7 (PROVED, CHECKED B1): the field energy's odd sector under the 24.**

*The class.* Block 64 T2's class: diffeomorphism-scalar densities built from the frame `e`, with at most two derivatives. Every spatial index is turned into a frame index by `e`. The frame indices are contracted by tensors invariant under the 24.

*The monomials.* Up to two derivatives they are `det e × {1, T, T², ∇T}`.

*The parity rule.*
- `x → −x` acts on a rank-r true tensor as `(−1)^r`: `T` has `r = 3` and `∇T` has `r = 4`.
- So on each monomial type it acts as one sign, and every invariant of that type has that parity.
- The characters over O (24 elements) and O_h (48) give the counts below.

| monomial | invariants under O | invariants under O_h | odd |
|---|---|---|---|
| T (linear) | 1 | 0 | 1 |
| T² | 4 | 4 | 0 |
| ∇T (linear) | 1 | 1 | 0 |

For T² there are 4 invariants under O and 3 under SO(3); the cubic group splits spin 2 into E ⊕ T₂.

*The odd invariant.* It is `ε_{jab} T^j_{ab}`. It is kept by the 24 and reversed by all 24 improper elements (B1).

*With `ϑ` as a separate axial field and `u` scalar,* the odd monomials are:
- `div ϑ` (with rate weight: `u div ϑ`, and `∇u·ϑ`);
- `ϑ·curl ϑ`.

There are none at two derivatives. `(∇u)·curl ϑ` is even. This is where the gravitation lens's "w × twist" term sits.

**Step 8 (PROVED, CHECKED B2): blindness removes the whole odd sector.**

*Frame class.* Take a coin rotation at zero strain, `B_b^j = −ε_{bjm}ϑ_m(x)`. It changes:

| term | change |
|---|---|
| `ε·T` | `−4 div ϑ` (block 65 T4) |
| the `c₄` density `∂_bV_b` | `0` |
| `det e` | `tr B = 0` |
| every `T²` invariant (including the extra cubic one) | `0`, since `T = 0` at zero strain |

Per-tick counting demands invariance point by point (block 64: every rate weights its own site's density). So `−4c₅ div ϑ(x) = 0` for all `ϑ` and `x`, and therefore `c₅ = 0`.
- Blindness also contains every global continuous rotation, so the extra cubic `T²` invariant goes too.
- The blind class is block 64's SO(3) family.
- Per-tick weights do not rescue `c₅`: `Σ wₓ c₅ ε·T` is still `c₅ × (−4 div ϑ)` point by point.

*Separate `ϑ`.* Blindness is `ϑ → ϑ + θ` for arbitrary `θ(x)` (block 65 T2/T3), which forces `F` to be independent of `ϑ`. Every odd term in Step 7 contains `ϑ`.

**Step 9 ((b), from Steps 2–8): which odd terms tell the classes apart.**
- `c₅ ε·T` and the `ϑ`-terms are `ΘΠ`-odd, so they would tell the classes apart. Blindness removes them.
- The scalar hop is `ΘΠ`-odd relative to the walk. By Step 3, no other site-local map restores the exchange, so it tells the classes apart. It survives (Steps 5 and 6).
- The walk with rates, frames and twists is `ΘΠ`-covariant (A6; block 70 T3 has all five kinds).
- The twist hop's inversion-odd scalar `div ϑ` (block 65 T4) multiplies a scalar hop of the opposite parity. The product therefore has the walk's parity and carries no handedness.

**Step 10 ((d); CHECKED A4, C): observable handedness.**

*Observables inside the framework:*
- the clocked walk's spectrum in a chiral clock pattern differs from its mirror image's (Step 4);
- in zero field, exactly one species sits on the top level `a₀ + 6|a|`, and its sense `sign det(βD_n)` equals `sign(aβ)`. The mirror image (`β → −β`) reverses it.

*Supplied clauses:*
- The walk has `a = 0`, fixed by block 54's added inversion, and is `ΘΠ`-covariant in every supplied field.
- The supplied field energies are even: block 56's `Σ(φₓ − φ_y)²`, block 60's and 64's members with `c₅ = 0`.
- So the supplied clauses contain no handedness.
- The axioms allow exactly one at nearest-neighbour reach: `aβ ≠ 0`, the family of block 77. Neither of block 64's demands removes it.

## 3. First failing step

None fails. The result is partial. It gives an exact classification together with an exact obstruction.

**How to read the HIT.**
- The surviving odd term is in the generator, not the field energy.
- For generator terms, survival under blindness is automatic (Step 5): blindness selects only field-energy terms, and there it removes the unique odd term.
- A referee may judge that the task's HIT condition was meant for field-energy terms only. On that reading the field-energy answer is "none survives", which would be no HIT.
- I report the generator result because task item (b) defines odd as odd under `ΘΠ`, and `a` meets that definition.

## 4. What would finish it

1. **The reach-two and reach-three strain couplings with `a ≠ 0`** (blocks 63, 69, 73). Carry the relabelling through the scalar hop, and test whether block 66's ledger requirement (stress gradient = weight) still holds.
2. **Exact blindness beyond first order.** Pure-gauge SU(2) links do it for any `X`, but links are not a supplied clause.
3. **A record-level handedness.** For example, the sign of block 54's sideways drift for packets on the top level. It is executed there, not claimed.
4. **Field-energy terms beyond two derivatives.** A blind density depends on `e` only through `g = eᵀe`. The lowest parity-odd scalar density of a 3-metric appears to have five derivatives (Cotton·Ricci). The Chern–Simons form is blind only up to a total derivative, which per-tick counting does not forgive. Both points are ASSUMED here, from standard geometry, as comparators. They are not re-proved.

ASSUMED: nothing is used as a premise beyond the named notes' definitions. The standard character formula for counting invariants is re-derived by the explicit averaging in `check.py`.
