# the-two-record-ledger-under-exclusion, attempt 1 of 2: the ledger survives with the projected density; matched pulls hold for every split that sources what it couples to; the exclusion changes the source only through the state

Worker `w-jonathonsmac4f50-j99c8` (`claude-opus-5-5`), unit `J:derive:the-two-record-ledger-under-exclusion:a1`.

**Provenance.**
- There were no prior attempts.
- My plan, formed first:
  - (a) differentiate at fixed state, using that the exclusion's projector does not depend on the rates;
  - (b) extend block 55 T3 to densities through the antisymmetry of the weak field's gradient kernel;
  - (c) compute exact densities on block 78's ring of 6.
- Block 80 (PR #8615) is a later block of the same campaign, by the same model family as me, and unrefereed. Its T1 already states (a) and checks it exactly on a ring of 6; it leaves matched pulls open. My A1 re-derives (a) independently.
- New here:
  - A2: the ledger along any motion;
  - B1: the pulls;
  - C1: the per-site densities;
  - C2: exactly what the exclusion changes in the source;
  - D1: the weak-field limit of the question itself.
- The sibling derivation `the-two-record-pull-under-exclusion` asks for the pulls through the actual momentum law of the compressed generator, including the contact. I do not attempt that here.
- Definitions follow blocks 53–55 (PRs #8568, #8570, #8571), 76 (#8611), 78 (#8613) and 80 (#8615):
  - the reduced walk `H_w = φσ₃Dφ` with `(Dψ)(x) = (ψ(x+1) − ψ(x−1))/(2i)` and `w = φ² = e^u`;
  - the one-record density `e_x = Re χ_x†(H_wχ)_x`;
  - two records under exclusion: the projector `P` onto different-site configurations, and `PH₂P` with `H₂ = H_w ⊗ 1 + 1 ⊗ H_w`.
- Nothing is adopted. No gravitational claim is made.

## 1. What is claimed

> **(a) The ledger.** Take the exclusion with either exchange sign, and any two-record state `Ψ_P` in the range of `P`. Define
>
> `e^(2)_x := Σ_slots Re⟨Ψ_P|P_x^{[s]} H_w^{[s]}|Ψ_P⟩`.
>
> Then:
> - `∂⟨Ψ_P|PH₂P|Ψ_P⟩/∂u_x = e^(2)_x` (block 80 T1);
> - `Σ_x e^(2)_x = ⟨PH₂P⟩`, so the density has weight one;
> - along any motion under `PH₂P(u(t))`, `d⟨PH₂P⟩/dt = Σ_x e^(2)_x du_x/dt`;
> - hence the ledger `⟨PH₂P⟩ + F` is kept iff `dF/du_x = −(e^(2)_x − μ)`: the source is the projected state's energy density.
>
> **The identity does not fail.**
>
> **(b) The pulls, in block 55 T3's model.** In that model a body's pull is `−Σ_x c_x (∇u)_x` for coupling density `c`, and the weak field is `u = −κG₀(s − mean)` for source `s`, where `G₀` is the zero-mean inverse of `1 −` (neighbour average) and `∇` is the centred difference. Then `Σ c ∇G₀ s = −Σ s ∇G₀ c` for every `c, s`. Hence:
> 1. The pair's self-pull vanishes when the source is `e^(2)`, which (a) makes both what the pair couples by and what it sources.
> 2. Split the pair into parts, each of which sources what it couples to. The parts' mutual pulls are then equal and opposite. For example, splitting by position on the ring gives `∓30733341219015/2127913889283343 κ`.
> 3. The exchange-symmetric split gives each record exactly `e^(2)/2`, and the two records' mutual pull is zero.
> 4. Block 76's additive source `e₁ + e₂`, the one-record densities of the states the pair was built from, is different. Against the coupling `e^(2)` it leaves the pair a self-pull of `−23366363968074/2352181536986099 κ` on block 78's ring of 6.
>
> **Matched pulls survive the exclusion with the source from (a).** No HIT under the task's criterion.
>
> **(c) The densities on block 78's ring of 6** (its rates and its two orthogonal complex states).
> - The one-record densities sum to block 78's free value `16169964/134909593`, and the free antisymmetric pair's density equals `e₁ + e₂` site by site.
> - The projected pair's density differs site by site; it sums to block 78's hard-core value `12349656/122046701`. The symmetric pair's density is also given.
> - **The exclusion changes the source only through the state:**
>   - For any state on different sites, the compressed density is the free formula applied to that state.
>   - Product states whose supports share no site are unchanged by `P`, and their density is exactly `e₁ + e₂`, whether or not the supports are adjacent.
>   - Blocked hops change the dynamics, not the instantaneous source.
>
> **(d) A limit of the question, numeric.** Take block 55's full field energy `F = (2/γ)Σ_bonds(φ_x − φ_y)²` at strong field. The centred-gradient self-pull `Σ_x (dF/du_x)(∇u)_x` is not zero, for one free record as much as for a pair. So matched pulls with this pull law are a weak-field statement, independent of the exclusion.

## 2. The steps

1. **PROVED + CHECKED (A1): the derivative.**
   - `P` is diagonal in the site basis and does not depend on the rates. So it commutes with every `P_x^{[s]}` and every site field.
   - With `φ = e^{u/2}`, `∂H_w/∂u_x = ½{P_x, H_w}`.
   - For `Ψ_P = PΨ_P`: `∂_x⟨Ψ_P|PH₂P|Ψ_P⟩ = Σ_s ½⟨Ψ_P|P{P_x^{[s]}, H_w^{[s]}}P|Ψ_P⟩ = Σ_s Re⟨Ψ_P|P_x^{[s]}H_w^{[s]}|Ψ_P⟩`.
   - Weight one follows from `Σ_x P_x = 1`.
   - Checked exactly: the pair's compressed energy is computed symbolically in the six `φ`'s and differentiated as `(φ_x/2)∂/∂φ_x` at block 78's rates. It equals `e^(2)_x` at all six sites and sums to the energy. The unprojected pair's derivative equals its own density, which differs.

2. **PROVED + CHECKED (A2): the ledger along any motion.**
   - Let the state evolve under `PH₂P(u(t))`; it stays in the range of `P`.
   - `d⟨PH₂P⟩/dt = ⟨∂_t(PH₂P)⟩`, because the commutator term `⟨[PH₂P, PH₂P]⟩` is zero. This equals `Σ_x e^(2)_x u̇_x`.
   - With `Σu` fixed, keeping `⟨PH₂P⟩ + F` for every motion of the field is equivalent to `dF/du_x = −(e^(2)_x − μ)`. This is block 55 T2(a) with the compressed generator.
   - Checked exactly on a two-parameter path `u(t)` at `t = 0`.

3. **PROVED + CHECKED (B1): the pulls.**
   - *Identity.* `∇ᵀ = −∇` and `G₀ᵀ = G₀`, and both are circulant, so they commute. Hence `cᵀ∇G₀s = (cᵀ∇G₀s)ᵀ = sᵀG₀ᵀ∇ᵀc = −sᵀ∇G₀c`.
   - *Self-pull.* With `s = c` the self-pull equals its own negative, so it is zero.
   - *Parts.* With `s^A = c^A` and `s^B = c^B`: `F_{A←B} + F_{B←A} = κ(c^A∇G₀c^B + c^B∇G₀c^A) = 0`.
   - *Slots.* For `Ψ_P(ij) = ∓Ψ_P(ji)`, relabelling the slots shows the two slot densities coincide. So the exchange-symmetric split gives `e^(2)/2` each, and their mutual pull is `κ/4 · e∇G₀e = 0`.
   - *The additive source.* Its self-pull is nonzero. This is an exact rational, as are `G₀` (the inverse of a rational matrix) and all the densities.
   - **ASSUMED:** the pull law `−Σ c∇u` is block 55 T3's model, block 54's `−E∇u` for point bodies extended linearly. The exact lattice force carries `cos k_j` factors (block 66), and under exclusion there is a contact term (block 80 T3). Both belong to the sibling task.

4. **CHECKED (C1): the densities.** Block 78's `φ_x = 1 + ((3x² + x) mod 5)/7` and its states are reproduced from its runner: `ψ₂` is made orthogonal to `ψ₁` exactly. The free and hard-core energies match block 78's `16169964/134909593` and `12349656/122046701`. The per-site values are printed in the log.

5. **PROVED + CHECKED (C2): what the exclusion changes.**
   - For `Ψ_P` in the range of `P`: `⟨Ψ_P|P_x^{[s]}PH^{[s]}P|Ψ_P⟩ = ⟨Ψ_P|P_x^{[s]}H^{[s]}|Ψ_P⟩`, because `P` commutes with `P_x^{[s]}` and fixes `Ψ_P`.
   - If `ψ₁` and `ψ₂` share no site, then `P` fixes `ψ₁ ⊗ ψ₂ ∓ ψ₂ ⊗ ψ₁`, and the free antisymmetric pair of orthogonal states has density `e₁ + e₂`.
   - Checked on a ring of 8: record A on sites 0–2, record B on 4–6 or on 3–5 (adjacent) gives the additive density exactly; B on 2–4 (sharing site 2) does not.
   - In block 78's T3 the non-additivity comes entirely from the same-site components that `P` removes.

6. **NUMERIC (D1): the weak-field limit.** On a ring of 7 with three rate fields of amplitude 0.8:
   - the full `F` gives `Σ(dF/du)(∇u) = −0.2145, −0.1869, −0.0023`;
   - its quadratic part gives zero to `1e−16`.

## 3. Where this stops

- In block 55 T3's model at weak field, nothing fails:
  - the ledger identity holds, with the projected state's density as the source;
  - the pulls match for every split that sources what it couples to.
- For identical records the pair's density has no canonical split into "each record's" density. The exchange-symmetric split is the canonical one, and it makes the mutual pull zero. So "the two records' pulls on each other" are meaningful only for parts one can tell apart, for example by position.
- The failure of action = reaction requires a source other than the density the dynamics couples to. Block 76's additive source is such a source under exclusion (step 3).
- **Not decided here:**
  - the actual momentum balance of the compressed generator in a rate field. The exclusion's contact exchanges one-step momentum (block 80 T3), and the lattice force is species-dependent (block 66). This is the sibling task.
  - matched pulls at strong field, which fail with the centred-gradient pull law even for one free record (step 6).

## 4. What would finish it

1. **A momentum law for the compressed generator.** Which momentum is conserved at uniform rates under exclusion? Crystal momentum is (block 80 T2), but it is not a linear observable. Then: its change in a self-sourced field, as an exact computation on rings of 6–8.
2. **A strong-field pull law** for which the self-pull of a body in its own field vanishes. The step-6 numbers show that the centred gradient does not provide one.
3. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/the-two-record-ledger-under-exclusion/w-jonathonsmac4f50-j99c8/check.py
```

- It has 6 lines:
  - A1–C2 are exact (sympy rationals, with symbols for the rates where a derivative is taken);
  - D1 is labelled NUMERIC.
- It runs in about 3 seconds.
- It prints no HIT line: under the task's criterion a HIT needs the identity or the matched pulls to fail, and neither fails.
