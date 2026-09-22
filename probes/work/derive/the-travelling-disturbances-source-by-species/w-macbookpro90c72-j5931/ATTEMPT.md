# J:derive:the-travelling-disturbances-source-by-species:a1 — w-macbookpro90c72-j5931

Attempt 1 of 2, by claude-opus-5-5 (all of `check.py` and this file). `python3 check.py` prints 4 `ok` lines, exits 0
with `FAIL` empty, and runs in under a second.

Exactness:
- States have Gaussian-integer entries and every operator entry is a dyadic rational, so the float64 values are exact.
  This is asserted.
- sympy is used for all symbolic statements.

Nothing is adopted and no gravitational claim is made.

**Sources** (PR branches, read for this attempt):
- block 62 (#8592): the frame; `Θ_a^j = Re ψ†σ_a(S_jψ) = ∂⟨H⟩/∂E_a^j`; `h = −(ε + εᵀ)`; the member `F₂ = −K w̄(uR₁ + R₂)`;
  the kinetic term `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]`; exactly two transverse-traceless (TT) disturbances at
  `ω² = K w̄² p²/(4α)`;
- block 63 (#8593): `π_j = Re ψ†S_jψ` and the bond current `J`;
- block 69 (#8601): `P_j = S_jC_j` and the bond current `K`;
- block 70 (#8602): `V_n = R_nU_n`, `V_nHV_n† = s_nH`;
- block 74 (#8607): T1 (the exact map laws) and T2 (at leading order, `Θ = D_aD_jK` and `J = D_jK` for species `n`).

## 1. Statement attempted

**(a) The TT source, species by species.** Take a disturbance travelling along `e_c`. Let `{a, b}` be the transverse
axes. The polarisations are `+ ∝ (aa − bb)` and `× ∝ (ab)`. Each species' source is compared with its own stress `K`,
the stress that balances its weight (block 74 T3).

| coupling | `+` source | `×` source |
|---|---|---|
| frame (`Θ`) | `+1` for all eight species | `D_aD_b = (−1)^{n_a+n_b}` |
| reach two (`J`), `n_a = n_b` | `D_a` | `D_a` |
| reach two (`J`), `n_a ≠ n_b` | not a multiple of `K`'s `+`: the transverse trace `D_a(K_aa + K_bb)/2` | `0` |
| reach three (`K`) | `+1` | `+1` |

Along `e₃`, for example:
- under the frame, species `000, 001, 110, 111` source `×` with the first species' sign, and `100, 010, 101, 011` with
  the opposite sign;
- under reach two, only `n₁ = n₂ = 0` species source like the first. Those with `n₁ = n₂ = 1` source both
  polarisations with the opposite sign. The four with `n₁ ≠ n₂` source no `×`, and a `+` that is their transverse
  trace.

The source depends only on the two transverse reflections, never on `n_c`.

**(b) The energy of emission.**
- On TT disturbances block 62's member gives `R₁ = 0` and `F₂ = (K w̄/4) p² h_ij h_ij ≥ 0`. So the TT field's energy is
  `(α/w̄)ḣ² + (K w̄/4)p²h²`, positive iff `α > 0` (with `K > 0`, as the real speed then requires).
- The radiated field is linear in the source, and its energy is quadratic in it. The sign a species carries therefore
  cancels.
- **For `α > 0` every species loses energy by radiating under every coupling, reflected or not.** The task's HIT
  condition — a reflected species gaining energy by emitting under the frame — is **not met**.
- The wrong sign shows only in interference: a coherent superposition of species with opposite signs radiates less
  than the sum of its parts.

**(c) Reach three.**
- Everything is species-blind. `K → s_nK` and `e → s_n e` exactly (checked), so the source per unit of the species'
  own energy is the same for all eight.
- For a plane wave, exactly: `Θ_a^j = sin k_a sin k_j/E` and `K_a^j = sin k_a cos k_a sin k_j cos k_j/E = Θ_a^j cos k_a cos k_j`.
- At `k = πn + q` this gives `K_a^j = sin 2q_a sin 2q_j/(4E)`, identical for every species. That is
  `(q_aq_j/E)[1 − (2/3)(q_a² + q_j²) + …]`, and the bracket's second term is the first lattice correction.
- The frame's plane-wave stress keeps the sign `D_aD_j` exactly.

**(d) The two books.** These are exact on the `4³` torus, for every state:
- block 63's one-step momentum transforms as `π_j → D_jπ_j`;
- block 69's two-step momentum transforms as `P_j → P_j`.

So a disturbance travelling along `e_c` that passes between two species is recorded with the same sign by both in
`P`'s books. In `π`'s books it is recorded with opposite signs when their `n_c` differ.
- None of the three couplings' TT sources involves `D_c`, so no coupling compensates this in `π`'s books.
- Whether the coupled dynamics conserves `π + (field)` or `P + (field)` for each coupling is not settled here (§3).

## 2. Steps

**S1 — map laws. CHECKED** on the `4³` torus, for all eight `V_n` and a Gaussian-integer state, at every site and in all
nine components:
- `V_nHV_n† = s_nH`;
- `Θ → s_nD_aD_jΘ`, `J → s_nD_jJ`, `K → s_nK` and `e → s_n e` — block 74 T1, re-checked;
- `π_j → D_jπ_j` and `P_j → P_j` — the momenta, new here.

The coin's half turn `R_n` is `iσ_a` about the unique axis with `ρ_a = +1` (`ρ = s_nD`), or `1`. It is checked to
satisfy `R σ_a R† = ρ_a σ_a`.

**S2 — the tables. PROVED from block 74 T2; CHECKED** by symbolic enumeration over the 8 species and 3 directions.
- Put `Θ = DKD` and `J = KD` with `K` symmetric. Symmetrise `J`, then read off `(M_aa − M_bb)/2` and `M_ab`.
- A ratio to `K`'s component is recorded only if it is free of symbols. Otherwise the entry is marked "trace".
- The reach-two `n_a ≠ n_b` row: `(D_aK_aa − D_bK_bb)/2 = D_a(K_aa + K_bb)/2` when `D_b = −D_a`, and
  `J_(ab) = (D_a + D_b)K_ab/2 = 0`.

**S3 — plane waves. PROVED; CHECKED** (sympy).
- `H(k)² = E²`, and `tr[(1 + H/E)σ_a]/2 = sin k_a/E` (Hellmann–Feynman on the positive branch).
- For a plane wave `(S_jψ) = sin k_j ψ` and `(P_jψ) = sin k_j cos k_j ψ`, and the bond current carries `Re e^{−ik_a} = cos k_a`.
- These give the two formulas in §1(c). The species forms and the series are CHECKED.

**S4 — TT energy. PROVED; CHECKED.**
- Along `e₃` a TT `h` has `h₁₁ = −h₂₂`, `h₁₂` free, and every component involving `3` zero.
- The member's `R₁` vanishes and `F₂ = (K w̄/4)p₃²·(2h₊² + 2h₁₂²)`.
- The mode's energy is the sum of this and the kinetic term. A source `S` enters linearly (`⟨H⟩ = Σ E·Θ`, block 62 T2),
  so the radiated amplitude is `∝ S` and the radiated energy `∝ S²·(sign of α)`.

**ASSUMED.**
- Block 74 T2's leading-order relations. They are the source of the tables; this attempt re-checks T1 but not T2.
- `K > 0`, as in blocks 60–62.

## 3. Where the route stops
- (a)–(c) are complete at the order block 62 works. The task's HIT condition is not met: emission costs energy for every
  species when `α > 0`, and the species' sign cancels in the energy.
- **(d) stops at the dynamics.** The transformation laws say which book records a transfer with which sign. But whether
  the content–field system conserves `π + (field)` under the frame or reach-two coupling needs the coupled equations of
  motion. That is the evolution under `H[E(t)]` together with the member's field equations, which neither block 62 nor
  this attempt writes down. So "do the books balance" is answered for `P`, under reach three, by species-blindness. For
  `π` under the other two couplings it is only reduced to the sign table above.

## 4. What would finish it
- The coupled equations of motion for content and TT field under each coupling, and their exact conserved momentum. A
  run with one wave packet of each of two species exchanging a disturbance would show which book balances.
- Oblique directions. The TT projection of `DKD` mixes components, e.g. for `k̂ ∝ (1,1,0)`. The same enumeration gives
  those tables exactly.
- The interference statement quantified: the radiated power of a superposition of species `n` and `n + (111)` (the
  massive pairing of block 77) under each coupling.
