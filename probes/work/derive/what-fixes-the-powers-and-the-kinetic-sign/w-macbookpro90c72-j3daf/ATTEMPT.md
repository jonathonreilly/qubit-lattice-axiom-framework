# Does anything in the framework fix p = 1, s = 3 and a negative kinetic term for the lengths?

Attempt 1 of 2. Worker `w-macbookpro90c72-j3daf`, model `claude-opus-5-5`. Script: `check.py` in this directory. It prints 5 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.** No earlier attempt exists, and the plan is my own. My units `many-bodies-of-both-signs-at-rest:a1` (#8814) and `rays-in-a-frame:a2` (#8815) used block 60's field equations but not its powers.

**Sources:**
- block 60 (PR #8590): the member `G = Kℓ^p(aΔλ + bq)`; T3, `β = 1/p` for bilinear members, and the continuum identity; T5, the kinetic term `Σ c_k ℓ^s λ̇²/w` and the closed lattice;
- block 62 (PR #8592): T4, the disturbances, with `X = Kw̄²P²/(4α)`;
- block 59 (PR #8581): the content, the hop and rest energies, and the length as a pure number.

## 1. Statement attempted

**What each principle fixes:**

| principle | what it fixes |
|---|---|
| **Weight one under a change of the time label** (all rates `× L`, `d/dt × L`) | Nothing. `F` and the kinetic term have weight one for every `p` and `s`, as `⟨H⟩` does. |
| **Covariance under the lattice's rotations** | Nothing about `p`, `s` or the sign. A direction-free disturbance speed needs block 62's rotation-invariant kinetic family, which is a further choice. |
| **A uniform rescaling of all lengths with the hop rates held** | It forces `w → Cw`, since `ℓ_b = √(w_xw_y)/c_b`. Then `⟨H⟩_hop × 1`, `⟨H⟩_rest × C`, `F × C^{1+p}`, kinetic term `× C^{s−1}`. |
| — consequence | No weight is common to the whole ledger: massless content alone would need `p = −1`, i.e. `β < 0`. The rescaling is a change of the unit of length, absorbed by `K → C^{−(1+p)}K`: `K` has dimension `length^{−(1+p)}`, which is `length^{−2}` at `p = 1`. |
| **Speeds free of the unit of length** | The field disturbances' `ω² × C^{2+p−s}`, while the walker's frequency (hop rates held) is unchanged. The ratio of speeds is unit-free iff **`s = p + 2`**. With `p = 1` this gives the declared `s = 3`. |
| **The ledger's sum rule on a closed lattice** (block 60 T5) | A uniform solution with content at rest needs `m w² + c_k ℓ^s λ̇² = 0`, so **`c_k < 0`** whenever `m > 0`. Then `ℓ = (1 + t/t₀)^{2/s}`, which at `s = 3` is the comparator's `t^{2/3}`. |
| **Agreement of the disturbances' speed with the walker's top speed** | `α = K/4`. |
| **The curvature reading** (block 60 T3(d)): `F` is the volume integral of the curvature of the stretched lattice | `√g R = −ℓ(4∇²λ + 2|∇λ|²)` for `g = ℓ²δ` in three dimensions: volume `ℓ³` times a curvature of weight `ℓ^{−2}`. So **`p = d − 2 = 1`**, and then `s = p + 2 = d = 3`: the volume power of the kinetic term. |

**(b) The rescaling.** A uniform rescaling `ℓ → Cℓ` with the hop rates held is a change of how many site ticks a crossing takes. For a walker with no rest energy it changes nothing, since that walker never meets a site rate (block 59 T1). The field's ledger scales as `C^{1+p}` and `C^{s−1}`, so it is a change of the unit of length, which `K` absorbs. Demanding one definite weight for everything fixes neither `p` nor `s`. Demanding it for the field's two parts fixes `s − p = 2`.

**(c) What remains declared:**
- `p` itself, equivalently `β = 1/p` (the bending), by choosing the curvature member;
- the value of `K`, which sets the unit of length;
- `α/K`, by choosing speed agreement;
- the rotation-invariant kinetic family.

Not declared once `p` is:
- `s`, forced by unit-free speeds;
- the sign of `c_k`, forced by the closed-lattice sum rule with positive content.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — PROVED and CHECKED [W1]. The time label.**
- `F = Σ w_x Kℓ^p(…)` is linear in the rates, and the lengths have weight zero.
- The kinetic term `c_k ℓ^s λ̇²/w` gets `L²/L = L`.
- Checked symbolically on a ring of 4 sites with generic `λ` and `u`.

**S2 — PROVED and CHECKED [W2]. The length rescaling.**
- *Why `w → Cw`.* With `ℓ → Cℓ` (`λ → λ + log C`) and the bond rates `√(w_xw_y)/(χ_xχ_y)` held, `w → Cw` follows.
- *`F`.* `Δλ` and `q` are unchanged, `ℓ^p → C^pℓ^p` and `w → Cw`, so `F → C^{1+p}F`.
- *Kinetic term.* `ℓ^s/w → C^{s−1}ℓ^s/w`.
- *Content.* `⟨H⟩ = Σ c_b⟨h_b⟩ + Σ w_x⟨m_x⟩` becomes `⟨H⟩_hop + C⟨H⟩_rest`.
- *Check.* Exact on the ring, with sympy's power simplification.

**S3 — PROVED and CHECKED [W3]. Unit-free speeds.** At second order about the uniform state, the mode equation is `(αℓ̄^s/w̄)ω² = Kw̄ℓ̄^p P²`: block 62's form, with the background powers kept. So `ω² ∝ w̄²ℓ̄^{p−s}`, and under the rescaling it gains `C^{2+p−s}`. The walker's frequencies are set by the hop rates, which are held. So the ratio of the two speeds is independent of `C` iff `s = p + 2`.

**S4 — PROVED and CHECKED [W4]. The sign.**
- Block 60 T5(b): stationarity in `w` of `c_kℓ^sλ̇²/w − mw` gives `c_k = −mw²/(ℓ^sλ̇²) < 0`.
- `ℓ = (1 + t/t₀)^{2/s}` solves `2λ̈ + sλ̇² = 0`.

**S5 — PROVED and CHECKED [W5]. The geometric count.**
- `√g R`, computed from the Christoffel symbols for `g = e^{2λ}δ` in `d = 3`, equals `−e^{λ}(4∇²λ + 2|∇λ|²)`: block 60 T3(d).
- *General `d`* (standard formula, not checked here): `√g R = e^{(d−2)λ} × (two derivatives of λ)`, so `p = d − 2`.
- *Speed agreement.* `X = Kw̄²P²/(4α)` equals the walker's `w̄²P²` at long wavelength iff `α = K/4`.

**S6 — PROVED. No definite weight for the whole ledger.** The content has two weights: 0 for hop energy, 1 for rest energy. A common weight with the field would need `1 + p = s − 1 = 0`, so `p = −1` (`β = −1`, rays bent the wrong way), or `1 + p = s − 1 = 1`, so `p = 0` (`β = 1/p` undefined). Neither is block 60's member. The rescaling is therefore not a symmetry of the physics: it changes the dimensionful `K`.

## 3. Where the route stops

- `p` is fixed only by the curvature reading (`p = d − 2`). No principle in the vocabulary forces the field's energy to be the volume integral of the curvature: the choice of member is still the declaration. Equivalently, `β = 1` is a choice.
- `α/K` needs the speed-agreement principle, which is not in the axioms.
- The rotation-invariant kinetic family (a direction-free speed) is a choice among the cube-covariant ones.

## 4. What would finish it

1. A reason inside the framework why the field energy per tick is a curvature: for instance, a requirement that the field's ledger be unchanged under the relabellings that move sites (block 62 T3(b)). Among two-derivative members of the right weight, that singles out the curvature combination. Checking that uniqueness would fix `p = 1`.
2. A statement that disturbances and walkers share one cone, fixing `α/K`.
