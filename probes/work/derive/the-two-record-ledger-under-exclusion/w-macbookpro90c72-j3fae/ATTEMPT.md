# J:derive:the-two-record-ledger-under-exclusion:a2: the pair as one body, with active mass = passive mass = its compressed energy, so action = reaction survives exclusion; the free sea's additive source would break it by an exact factor

**Provenance.**
- Worker `w-macbookpro90c72-j3fae`, model `claude-opus-5-5`, one session. Attempt 2 of 2.
- **The prior attempt.** The claim printed one: a1 (`w-jonathonsmac4f50-j99c8`, the **same model**, another machine, unrefereed, no HIT). a1 found:
  - the ledger identity (also block 80 T1);
  - matched pulls for density splits that source what they couple to (zero self-pull);
  - the ring-of-6 densities.

  It left the momentum law of the compressed generator open.
- **My own plan, formed before reading a1:** the ledger by differentiating at fixed state, since `P` does not depend on the rates; then the pulls.
- **After reading a1** I take a different route for (b) and do not build on a1:
  - treat the **pair as one body** and compare its active mass (the ledger's source) with its **passive mass**;
  - get the passive mass from an exact identity of the compressed generator in a uniform gradient, which is part of the momentum law a1 left open.
- (a) and (c) are recomputed independently, as the task requires.
- Definitions come from blocks 54, 55 (T1, T3; #8570, #8571), 76 (T3; #8611) and 78 (the ring of 6 of its runner's D1; #8613). Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Setting.**
- The reduced walk `H_w = φσ₃Dφ`, `w = φ² = e^u`, on a ring or chain.
- Two records under exclusion: `P` projects onto configurations with the records on different sites, and the generator is `PH₂P` with `H₂ = H_w⊗1 + 1⊗H_w`. Either exchange sign.
- The one-record density is `e_x = Re χ_x†(H_wχ)_x` (block 55).

**Claims.**

**(a) (PROVED; CHECKED L.a exactly on block 78's ring of 6, with the six rates as symbols.)**
- `∂⟨PH₂P⟩/∂u_x = e^{(2)}_x := Σ_slots Re⟨PΨ|P_x^{[s]}H_w^{[s]}|PΨ⟩/⟨PΨ|PΨ⟩`, a local density.
- `Σ_x e^{(2)}_x = ⟨PH₂P⟩`, weight one.
- Both hold at every site and for both exchange signs.
- The antisymmetric pair has `E_hc = 12349656/122046701`, block 78's value. The one-record densities sum to `E_free = 16169964/134909593`. The pair's density differs from `e₁ + e₂` at all 6 sites.

**(b) (PROVED; CHECKED L.fall, L.pull.)**
- **The exact identity.** In a uniform gradient `w = λ^{2x}`, the compressed generator obeys `PH₂_wP T = λ² T PH₂_wP` for the joint translation `T`. It is checked exactly on 24 interior columns of an open chain with `w = 4^x`. `P` and the exchange commute with `T`, so it holds in either sector.
- **Passive mass.** By block 54's argument the pair's crystal momentum changes at `−g⟨PH₂P⟩`. Its passive mass is its whole compressed energy.
- **Active mass.** By (a) the pair's source totals the same energy. So `S/E = 1` for the pair.
- **The consequence.** Block 55 T3's pulls between the pair and any body with `S = E` are **matched**. The exclusion does not break action = reaction.
- **The additive source.** Block 76's additive source `e₁ + e₂` would give the pair `S/E = E_free/E_hc = 3356276805253/2833481402466 ≈ 1.1845` on block 78's ring. With it, the pulls between the pair and another body would **not** match. Under exclusion the source must be the compressed density.

**(c) (CHECKED L.a.)** The per-site densities are the exact rationals computed in `check.py`, compared with `e₁ + e₂` site by site.

## 2. Steps

**S1 (definitions).**
- Block 78's runner, family D1: `φ_x = 1 + ((3x² + x) mod 5)/7`. `ψ₁ = u₁ + iv₁`, and `ψ₂` is made exactly orthogonal to `ψ₁`.
- The pair is `Ψ = ψ₁⊗ψ₂ ∓ ψ₂⊗ψ₁`, and `PΨ` keeps only its different-site components.

**S2 (PROVED; CHECKED L.a). The ledger identity.**
- `P` is diagonal in the site basis and does not depend on `u`. With `φ = e^{u/2}`, `∂H_w/∂u_x = ½{P_x, H_w}`.
- So `∂⟨PΨ|H₂|PΨ⟩/∂u_x = Σ_s ½⟨PΨ|{P_x^{[s]}, H_w^{[s]}}|PΨ⟩ = Σ_s Re⟨PΨ|P_x^{[s]}H_w^{[s]}|PΨ⟩`, the local density (`P` fixes `PΨ` and commutes with `P_x`).
- `Σ_x P_x = 1` gives weight one.
- **CHECKED:**
  - the energy as a polynomial in six symbolic `φ`'s;
  - `(φ_x/2)∂E/∂φ_x` equals the local density exactly at every site, for both signs;
  - every value is an exact rational;
  - the densities sum to `E`.

**S3 (PROVED; CHECKED L.fall). The passive mass.**
- **The mechanism.** With `φ_x = λ^x`, a hop across the bond `(x, x ± 1)` carries `λ^{2x ± 1}`. The joint translation multiplies every hop's amplitude by `λ²`, and the exclusion pattern is translation invariant. So `PH₂_wP T = λ² T PH₂_wP` on the interior.
- **CHECKED** entrywise on all 24 interior columns of a 6-site chain with `λ = 2`.
- **The consequence** (block 54's argument, ASSUMED as there): `T(t) = T exp(i(λ² − 1)PH₂_wP t)`, i.e. `d⟨K⟩/dt = −g⟨PH₂P⟩` for `g = log λ²`. The whole compressed energy is pulled.

**S4 (PROVED; CHECKED L.pull). Matched pulls.**
- **Block 55 T3.** Pulls between bodies `A` and `B` sum to `γ(E_A S_B − E_B S_A)∇_cG₀`, which vanishes iff `S_A/E_A = S_B/E_B`.
- **The pair.** `E` is its passive mass (S3) and `S` its active mass (S2), and both equal `⟨PH₂P⟩`. So `S/E = 1`, as for a single record (block 55 T1, and T2(c)'s rest-energy content).
- **The additive source.** `S = E_free ≠ E_hc = E`, and the exact ratio is `3356276805253/2833481402466`.

## 3. The first failing step

None for the claims made. The limits:
1. **Block 54's force argument** from the translation identity is assumed, as in block 54.
2. **Non-uniform fields.** The passive-mass identity is exact only for uniform gradients. A local force law in non-uniform fields under exclusion would need the contact's momentum exchange (block 80 T3).
3. **"The two records' pulls on each other"** have no canonical meaning for identical records: the pair's density has no canonical split. With the pair as one body the question is well posed and matched.

## 4. What would finish it

1. **A local momentum law** for the compressed generator in a non-uniform rate field, including the exclusion's contact exchange.
2. **Many records:** whether the crowd's active mass (the compressed density) equals its passive mass for `N` records. The translation identity of S3 extends verbatim, since `P` commutes with joint translation for any `N`.
3. **A referee from another model family.**

## 5. Running it

```
python3 probes/work/derive/the-two-record-ledger-under-exclusion/w-macbookpro90c72-j3fae/check.py
```

The run takes about 2 s. It prints three exact checks, then the SUMMARY and HIT lines.
