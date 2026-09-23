# J:derive:the-two-record-pull-under-exclusion:a1: on a chain two records under exclusion are two free spinless fermions of the charge band, so exclusion adds no failure of action = reaction; far apart the source is additive up to the near-coincidence probability

**Provenance.**
- Worker `w-macbookpro90c72-j3e98`, model `claude-opus-5-5`, one session. Attempt 1 of 2; the claim printed no prior attempts.
- **Overlap to declare.** Earlier in this session I did two related units:
  - the sibling `J:derive:the-two-record-ledger-under-exclusion:a2` (issue #8736): the pair as one body, active mass = passive mass;
  - `J:derive:the-hard-core-seas-energy:a1` (issue #8730): on a ring, records under exclusion are one spinless band with a coin-sequence twist.

  Part (a) here re-derives the ledger identity independently. Part (b) uses the chain version of the #8730 reduction, **re-checked here with rates**. Neither issue is used as authority (both are unrefereed).
- **The task's own framing.** Block 55 T3's matched pulls hold for the pull model whenever each part sources what it couples to. The exact lattice momentum law already differs from that model for a single free record: the lattice force carries `cos k` factors (block 66). So the question is whether **exclusion** adds a failure, and part (b) answers it.
- Definitions come from blocks 54, 55 (T1, T3), 76 (T3), 78 (its ring of 6) and 80 (T1 to T3), on their PR branches. Nothing is adopted and no gravitational claim is made.

## 1. The statement attempted

**Setting.**
- The clocked reduced walk: `H_w = φσ₃Dφ`, `(Dψ)(x) = (ψ(x+1) − ψ(x−1))/(2i)`, `w = φ²`.
- Two records under exclusion: `PH₂P`, with `P` removing coincidences. Either exchange sign.
- The one-record density is `e_x = Re χ_x†(H_wχ)_x`.

**(a) (PROVED; CHECKED P.a, exact.)**
- `∂⟨PH₂P⟩/∂u_x = e^{(2)}_x = Σ_slots Re⟨PΨ|P_x^{[s]}H_w^{[s]}|PΨ⟩/⟨PΨ|PΨ⟩` at every site.
- `Σ_x e^{(2)}_x = ⟨PH₂P⟩`, weight one.
- Checked on block 78's ring of 6 (its rates and states; the energy is block 78's `12349656/122046701`) and on a ring of 8, both signs.

**(b) (PROVED; CHECKED P.map, P.src, exact.)**
- **The reduction.** On a chain, with any rate field and either exchange sign, write configurations in the ordered basis (`x_L < x_R`, coins in order) and apply the gauge `(−1)^x` on down coins. Then:

  `PH₂_wP = h₂ ⊗ 1_coin sequence`,

  where `h₂` is the generator of **two free spinless fermions** with the up coin's hop and the same bond weights `φ_xφ_y`.
- **What that means.**
  - The records never pass, and they keep their coins.
  - The exclusion is exactly the charge band's Pauli principle.
- **Consequences:**
  - **The source is additive over the charge orbitals:** `e^{(2)}_x = Re Σ_y ⟨x|h|y⟩ρ(y, x)`, with `ρ` the charge one-particle density matrix. So block 76 T3 holds in the charge picture.
  - **Block 78's non-additivity** is with respect to the original coin-carrying one-record states, which are not the charge orbitals.
  - **The momentum law** of the compressed generator is that of two free charge fermions. Each orbital's one-body law applies, and crystal momentum is conserved at uniform rates (block 80 T2).
  - **Block 80 T3's non-conservation** of the one-step momentum is a statement about the original variables, not a dynamical interaction.
  - So every pull law that holds for free records holds unchanged for records under exclusion. In block 55 T3's model the pulls between parts that source what they couple to are matched (for example, the two occupied charge orbitals). Where the exact lattice law departs from that model, it does so for free records too.
- **Exclusion adds no failure of action = reaction. The task's HIT condition is not met.**

**(c) (PROVED; executed.)** For orthonormal `ψ₁, ψ₂` and `Ψ = (ψ₁⊗ψ₂ ∓ ψ₂⊗ψ₁)/√2`:

  `|e^{(2)}_x − e₁_x − e₂_x| ≤ 4‖D_x‖ ν/(1 − q)`,

  where `ν` is the probability that the records are within one site and `q` that they coincide.
- For records localised with decay length `ξ` and separation `d`, `ν` falls like `e^{−2d/ξ}`.
- Executed on a ring of 24 with `ξ = 1.2`:

  | `d` | max deviation | `ν` |
  |---|---|---|
  | 4 | `1.6·10⁻³` | `1.6·10⁻²` |
  | 12 | `2.7·10⁻⁹` | `1.5·10⁻⁷` |

  The ratio stays at or below 0.1.

## 2. Steps

**S1 (definitions).**
- Configurations of two records are pairs of modes `(2x + c, 2y + c′)`.
- `P` keeps `x ≠ y`. On a chain the ordered basis is `(x_L < x_R, s_L, s_R)`.

**S2 (PROVED; CHECKED P.a). The ledger.**
- `P` is diagonal and does not depend on the rates, and `∂H_w/∂u_x = ½{P_x, H_w}`. So the derivative at fixed state is the local density.
- At fixed state, `E` is linear in each bond factor, and `φ_x` enters each bond once. So the central difference in `φ_x → φ_x(1 ± t)` is exact.
- **CHECKED** at every site on the rings of 6 and 8, both signs, in exact rationals.

**S3 (PROVED; CHECKED P.map, 480 matrix elements). The chain reduction.**
- **Order and coins.** `σ₃` is diagonal, so coins are conserved. Nearest-neighbour hops cannot carry a record onto or past the other's site under `P`, so the order is kept.
- **The gauge.** For a down record, the gauge factor `(−1)^{x}(−1)^{x±1} = −1` turns its hop amplitude into the up coin's.
- **No sign from exchange.** No hop passes the other record, so no exchange sign arises on a chain. The fermionic and bosonic matrix elements coincide in the ordered basis.
- **The result.** The compressed generator acts on the ordered positions as the hard-core hop of spinless particles, which on a chain is the free two-fermion generator (Jordan–Wigner with no boundary term). It acts trivially on the coin sequence.
- **CHECKED:** on a chain of 7 with generic rational `φ`, every nonzero matrix element for both signs:
  - keeps the coin sequence;
  - moves exactly one record by one site;
  - equals the gauged up-coin hop times `φ_xφ_y`.

**S4 (PROVED; CHECKED P.src). The source over charge orbitals.**
- For a free two-fermion state with antisymmetric amplitude `c`, the one-body density is `e_x = 2 Re Σ_z Σ_b c(x,z)*⟨x|h|b⟩c(b,z)/‖c‖²`, the trace against the one-particle density matrix.
- **CHECKED:** for a generic rational charge amplitude in the coin sector (up, down), the compressed density of the corresponding record pair equals it at every site, exactly.

**S5 (PROVED). Pulls and the momentum law.**
- By S3 the pair's dynamics, observables and source are those of two free charge fermions.
- **Block 55 T3's identity** `Σ c∇G₀s = −Σ s∇G₀c` (circulant `∇` and `G₀` on a ring) makes the pulls between parts that source what they couple to cancel pairwise.
- **Momentum.** The charge orbitals are such parts, and their momenta obey one-body laws. At uniform rates crystal momentum is conserved (block 80 T2); in the charge picture each orbital's is.
- **The comparison.** Any departure of the exact lattice force from `−e∇u` (block 66) is the same for free records as for records under exclusion. So exclusion adds no failure.
- **The limit.** This is exact on a chain. On a ring the reduction carries the coin-sequence twist (#8730, re-checkable the same way). That changes boundary conditions, not the local momentum law.

**S6 (PROVED; executed). Far apart.**
- Normalise `Ψ`. Then `e^{(2)} − e₁ − e₂ = [q⟨Ψ|D|Ψ⟩ − 2Re⟨QΨ|D|Ψ⟩ + ⟨QΨ|D|QΨ⟩]/(1 − q)`.
- `D_x` moves one record by one site, so `⟨QΨ|D|Ψ⟩` involves only configurations at distance ≤ 1. Its size is at most `‖D‖·√q·√ν ≤ ‖D‖ν`.
- Hence the bound `4‖D_x‖ν/(1 − q)`.
- For free antisymmetric `ψ₁, ψ₂`, `e_free = e₁ + e₂` (block 76 T3). Executed as in §1(c).

## 3. The first failing step

None for the claims made. The limits:
1. **The reduction is one-dimensional.** It uses the coin-diagonal reduced walk. In 2D or 3D, records pass each other and hops flip coins, so no such reduction exists (block 78's `4×4` spectra).
2. **Whether the exact lattice pull law is matched** is a single-record question (block 66), not an exclusion question. It is not settled here.

## 4. What would finish it

1. **2D and 3D:** whether the exclusion adds momentum exchange beyond free composition.
2. **The exact lattice momentum law** for one record in a non-uniform self-field, as block 66's weight identity at higher order.

## 5. Running it

```
python3 probes/work/derive/the-two-record-pull-under-exclusion/w-macbookpro90c72-j3e98/check.py
```

The run takes about 1 s. It prints three exact checks and one floating-point note, then the SUMMARY and HIT lines.
