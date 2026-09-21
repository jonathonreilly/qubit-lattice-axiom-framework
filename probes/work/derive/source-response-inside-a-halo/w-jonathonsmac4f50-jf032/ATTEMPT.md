# source-response-inside-a-halo, attempt 3 of 5 — the drift does not vanish at the neutral scale

Worker `w-jonathonsmac4f50-jf032` (`claude-opus-5`), unit `J-derive-source-response-inside-a-halo:a3`.

**Provenance.** No prior attempt existed at claim time. Blocks 39/40/41 are taken as the unit
states them and are same-family campaign work; I re-derive none of them.

## 1. What is claimed

Gas assumption, stated plainly: **independent sites**, occupancy probability `ρ(x) = ρ + g·x`,
contents **uniform on the six axes and independent of occupancy**. Everything below is first order
in `ρ` and in `g`.

> **(a) The exact first-order drift coefficient** of a free test record is
>
> ```
> v/g = ( 18c³pqr − 10c²pq + 11c²pr + 11c²qr − 17cp − 17cq + 4cr − 24 )
>       / ( 3 (cp+1)(cq+1)(cr+1) )
> ```
>
> Of this, the **blocking of occupied targets contributes exactly `−1`**, independently of `c, p,
> q, r`. (By hand: a gas record on a target removes that hop, so `D_x(s) = −s_x/2` for a
> neighbour, and `−½ Σ_{s∈AX} s_x² = −1`.)
>
> **(b) The drift at the neutral scale is NOT zero.** It is negative — the record drifts *away*
> from density — on every triple tested:
>
> | `(p,q,r)` | `c₀` | drift coefficient | of which weights-only |
> |---|---|---|---|
> | (3,1,2) | 1/2 | **−52/45** = −1.15556 | −2/15 = −0.13333 |
> | (12,1,2) | 2/7 | **−21002/9207** = −2.28109 | −3370/3069 = −1.09808 |
> | (5,2,4) | 6/23 | **−13866/12455** = −1.11329 | −8466/87185 = −0.09710 |
> | (7,3,5) | 1/5 | **−79/72** = −1.09722 | −1/12 = −0.08333 |
>
> **Why the expectation fails.** `⟨c₀ω⟩ = 1` is what makes a random-content neighbour weigh what a
> void weighs. But the hop uses `φ/(1+φ)` with `φ = c₀ω`, and that function is **concave**, so
> `⟨φ/(1+φ)⟩ < ½`, the value at the mean. A neighbouring record lowers the chance of hopping
> *towards* it even while weighing one on average. *"No binding without a cycle" is a statement
> about the static measure; the drift in a gradient is a kinetic asymmetry out of equilibrium, and
> it survives the absence of binding.*
>
> **(a) again, the sign.** The drift reverses to up-gradient only above a scale `c*`:
>
> | `(p,q,r)` | `c₀` | `c*` | `c*/c₀` |
> |---|---|---|---|
> | (3,1,2) | 0.5000 | 0.702965 | 1.4059 |
> | (12,1,2) | 0.2857 | 0.597174 | 2.0901 |
> | (5,2,4) | 0.2609 | 0.361617 | 1.3862 |
> | (7,3,5) | 0.2000 | 0.275496 | 1.3775 |
>
> So at and just above the neutral scale the gas is **dispersive, not accretive**.
>
> **(c) Accretion.** A held cube of side `m` capturing at rate `κ` per face-site sees `ρ ± gm/2` on
> its two `x`-faces, so `d(MX)/dt = κ g m⁴/2` and, with `M = m³`,
>
> ```
> v_cm = κ g m / 2          — linear in the side, i.e. ∝ (record count)^{1/3}.
> ```
>
> A lump therefore drifts **up** the gradient where a single record drifts **down**: accretion and
> hop-asymmetry are different mechanisms, with different signs and different sizes.
>
> **(d) B inside A's halo.** With `u = Q G/κ` and `G ≈ 1/(4πR)`, the gradient at `B` is
> `|g| = Q/(4πκR²)`, so a cube of side `m` has
>
> ```
> v_B = κ g m / 2 = Q_A m_B / (8 π R²).
> ```
>
> One over `R²`, linear in `A`'s production and linear in `B`'s linear size. **Not symmetric under
> exchanging A and B**: `v_B` depends on `(Q_A, m_B)` and `v_A` on `(Q_B, m_A)`, which agree only
> if production is proportional to size for both. There is no single "mass" playing both roles.
>
> **And it is not a force law.** `v ∝ g` is overdamped — velocity set by the local gradient, no
> memory. Inertia needs a conserved momentum to accelerate, and block 41's result (1) is that the
> **only** local additive invariant density is the occupancy. Getting one means adding a conserved
> vector density: new axiom content, not a consequence of the present clauses.

## 2. The steps

1. **PROVED + CHECKED (`H1`).** The exclusion coefficient `−1`, both by enumeration and by hand.
2. **CHECKED (`H2`).** The full coefficient, by exact enumeration over the 24 gas sites that can
   affect a hop, both contents averaged, matched against the closed form.
3. **CHECKED (`H3`).** The four neutral-scale values and their weights-only parts.
4. **CHECKED (`H4`).** The reversal scales as exact real roots of the numerator.
5. **PROVED + CHECKED (`H5`), (`H6`).** The cube algebra and the halo gradient, symbolically.

## 3. Where this stops

- **First order in `ρ` only.** One gas record at a time. At the densities where clumping matters
  (block 39 put the onset near `ρ ≈ 0.3`) the pair term is not small, and its sign is not
  determined here.
- **The gas is assumed independent with uniform contents.** That is stated as an assumption, not
  derived, and it is exactly what a halo around a producer will *not* be — block 41's own result
  (3) says the field of a held record through a medium is the pair correlation. So the drift
  coefficient computed here is the response to an *imposed* independent-site gradient, which is a
  different object from the response to a real halo.
- **(c) assumes a capture rate proportional to local density with a single constant `κ`,** uniform
  over faces. I did not derive `κ` from the hop rule, and I did not check that a captured record
  stays captured.
- **(c) and (d) are scaling arguments, not enumerations.** Unlike (a) and (b) they are not checked
  against an exact computation on a window.
- **The reversal scale `c*` is computed for a single free record.** Whether a bound cluster
  reverses at the same scale is not addressed, and (a) explicitly asks about "a small bound cluster
  whose binding comes from loops at `c₀`" — which I did **not** do.

## 4. What would finish it

1. The bound-cluster case, which is the half of (a) I skipped: a two- or three-record cluster held
   together by the loop factor `1 + 3l₁ⁿ + 2l₂ⁿ`, drifting in the same gradient.
2. Second order in `ρ`, enough to tell whether the dispersive sign at `c₀` survives to the
   densities where clumping happens.
3. Replace the imposed independent gradient with block 41's actual halo `G*(j−⟨j⟩)/κ`, including
   the pair correlation, and recompute (a). That is the honest version of (d).
4. Another model family: blocks 39/40/41 and this attempt are the same family, and the result
   contradicts an expectation stated in the unit, which is exactly when an outside check is worth
   most.

## 5. Running it

```
python3 probes/work/derive/source-response-inside-a-halo/w-jonathonsmac4f50-jf032/check.py
```

`sympy` only; 14 checks, exact rational and symbolic arithmetic throughout. Runs in about a minute.
