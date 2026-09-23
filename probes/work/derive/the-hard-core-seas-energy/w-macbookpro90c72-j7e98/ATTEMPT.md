# J:derive:the-hard-core-seas-energy:a1: on a ring the axioms' records are one twisted spinless band; their sea is half filled and carries half the free sea's volume term and clock stiffness; at the free sea's filling exclusion leaves 2^d holes

**Provenance.**
- Worker `w-macbookpro90c72-j7e98`, model `claude-opus-5-5`, one session. Attempt 1 of 2; the claim printed no prior attempts.
- I formed the plan before reading the notes in detail:
  1. An exact one-dimensional reduction. The reduced walk `σ₃S` never changes a record's coin, and exclusion on a ring never lets two records pass. So the records should be one spinless band with a boundary twist.
  2. Exact diagonalisation on the `3×3` torus, with degenerate second-order perturbation theory.
- **Related earlier unit.** The same worker and model, earlier this session, did `J:derive:the-held-sea-against-the-free-sea:a1` (issue #8716, unrefereed). That unit was about the free sea only. Its one-dimensional free closed form is re-derived here (S7 treats the free sea as two bands) and is not used as authority.
- **Sources.** I read on their branches:
  - block 76 (#8611): `φ = e^{u/2}`, `Π(q)`, `c₀`, `κ`, the "gradient part" `(Π(q) − c₀/4)/|q|²_lat`;
  - block 78 (#8613): the reduced walk `H = σ₃S` on a ring, the 2D walk `σ₁S_x + σ₂S_y`, the exclusion sectors, either exchange sign, and its control script's conventions;
  - the fork probe of 2026-09-22 (§3, §4 item 1, §7).

  Block 77's scalar hop and staggered term are not used; the task names the reduced and 2D walks.
- Nothing is adopted and no gravitational claim is made. The statistical postulate and the larger site algebra are not touched.

## 1. The statement attempted

**The model.**
- `n` sites and `N` records, at most one record per site, each record carrying a coin. The generator is `H_hc(u) = P dΓ(φHφ) P`: second quantisation of the clocked one-record walk (fermionic or bosonic), compressed to configurations without a doubly occupied site.
- Each hop across the bond `xy` carries its own bond's factor `φ_xφ_y`. This is not `Γ(φ) dΓ(H) Γ(φ)`, which would rescale the resting records too.
- Rate mode: `u = ε cos(q·x)`. Second-order coefficient: `E₀(ε) − E₀(0) = Π(q) ε² n + O(ε³)`.
- As in block 76: volume term `c₀ = E₀/n`, gradient part `G(q) = (Π(q) − c₀/4)/|q|²_lat`, and `κ = 4G` as `q → 0`.

**Fillings.** Three are reported, because "half filling" is ambiguous:
- half the sites, `N = n/2`;
- the free sea's filling `N_neg` (the number of negative one-body states);
- half the one-body states, `N = n`.

**Claims.**

**(a) and (c): exact statements.**
1. **Packing (S2).**
   - At `N = n` the hard-core generator is identically `0`.
   - For `0 < N < n` it is traceless and nonzero. So the volume term is strictly negative: it never changes sign.
2. **Rings (S4, S5).** For every rate field and either exchange sign, `N` records on a ring with the reduced walk are exactly one spinless band whose wrap bond carries an eigenvalue of a signed rotation `R` of the coin sequence.
   - The twist set is the same for both signs: all `N`-th roots of unity on even rings, all `2N`-th on odd rings. Only multiplicities differ.
   - So fermionic and bosonic records have the same ground energy and the same second variation at every rate field.
3. **The ring's sea (S6, S7).**
   - The lowest state over all record numbers (block 76's sense of a sea) is half filled, with `E = −1/sin(π/L)` when `4 | L`. The free sea has `−2cot(π/L)`.
   - At half filling, `0 ≤ E_free(u)/2 − E_hc(u) ≤ 2 max_b w_b` for every rate field, and `Π_hc(q) → −cos²(q/2) ln(sec(q/2) + tan(q/2))/(4π sin(q/2)) = Π_free(q)/2` at every fixed `q`.
   - Hence `c₀ = −1/π` and `κ = 1/(6π)`: exactly half the free sea's `−2/π` and `1/(3π)`, with the **same sign**.
4. **The free sea's filling (S8).**
   - Exclusion leaves `h = N_sites − N_neg` empty sites: 2 on even rings, 1 on odd rings and on `3×3`, 4 on even 2D tori, 8 on even 3D tori.
   - `|E_hc| ≤ h·d·max w_b`. So the energy is `O(1)`, not `O(n)`, and the volume term vanishes per site.
   - In 1D the per-site second-order coefficient at fixed `q` is `O(1/L)`.
5. **A side identity for the free comparator (S9).** On every even ring the free sea's mode `q = 2π/L` has gradient part exactly `0`: it is carried entirely by the zero modes.

**(a) and (c): executed in floating point, labelled (S10).**
- **Rings of 7 and 8 and the `3×3` torus, full tables in the log.** At the free sea's filling the smallest-mode gradient parts are negative:

  | lattice | hard-core `G` | free `G` |
  |---|---|---|
  | ring 7 | `−0.157` | `+0.021` |
  | ring 8 | `−0.070` | `0` (S9) |
  | `3×3` | `−0.027` | `+0.025` |

  This is the relaxation of a few holes toward fast clocks. In 1D it grows like `−L³` at `q = 2π/L`, with `Π(2π/L) → −L/(8π²)`, and vanishes per site at fixed `q`. It is not a local stiffness.
- **At half filling:** `G` is positive on the rings (`+0.015` to `+0.020`) and on the `3×3` sea (`N = 5`: `+0.009`, `+0.012` fermionic; `+0.0015` bosonic along `(1,0)`).
- **First-order splitting.** Where the ground level is degenerate across momenta differing by `q` (`3×3`, `N = 4` for both signs; `N = 5` bosonic along `(1,1)`), the rate mode splits it at first order, `E₀(ε) = E₀ − μ|ε|`, and no second-order coefficient exists.
- **The exchange sign in 2D.** It changes the half-filled `3×3` energies (fermionic `−4.172`, bosonic `−3.821` at `N = 5`), but not the one-hole sector.
- **The `3×3` sea.** For both signs the lowest energy over `N` is at `N = 5`.

**(b) Exact (S3).** The clocked generator depends on the rates only through the bond products. A chessboard `φ = c^{±1}` has every bond product exactly 1 on even tori, so the hard-core sea, every eigenvalue and every second variation are unchanged at any amplitude, for either sign. Odd tori have no chessboard.

## 2. Steps

**S1 (definitions).**
- Block 78's conventions:
  - ring: `⟨x|H|x+1⟩ = (−i/2)σ₃` (`H = σ₃S`, `S = (T − Tᵀ)/2i`);
  - torus: `⟨x|H|x+e₀⟩ = (−i/2)σ₁`, `⟨x|H|x+e₁⟩ = (−i/2)σ₂`.
- **Fermionic sign.** The modes `2·site + coin` are ordered, and a hop `c†_m c_{m′}` carries `(−1)^{#occupied modes below m′ + #occupied modes below m (after removal)}`. Bosonic records carry no sign.
- `H` has no on-site term, so a hop moves one record to an empty neighbouring site.

**S2 (PROVED; CHECKED X.pack). Packing and the volume term's sign.**
- At `N = n` every hop targets an occupied site, so `H_hc ≡ 0`.
- For `0 < N < n`: the lattice is connected, so some record has an empty neighbour and `H_hc ≠ 0`. There are no diagonal entries, so `tr H_hc = 0`.
- A nonzero traceless Hermitian matrix has a negative eigenvalue, so `E₀ < 0`.
- For uniform rates `u = ε`, `H_hc(ε) = e^{ε}H_hc`, so `E₀(ε) = e^{ε}E₀`.

**S3 (PROVED; CHECKED X.chess). The chessboard.**
- The hop of a record across `xy` has amplitude `φ_xφ_y⟨x|H|y⟩`. The other records do not enter, and the exclusion projector is diagonal in configurations.
- So `H_hc` depends on `u` only through the bond products. A chessboard has all bond products equal to 1 on bipartite lattices, which the check confirms exactly on the ring of 8 and the `4×4` torus.

**S4 (PROVED; CHECKED X.ring, 24768 entries exact). The ring as one spinless band.**
- **The picture.** `σ₃` is diagonal, so every record keeps its coin. On a ring, hops to empty neighbours preserve the cyclic order of the records. Write a configuration as positions `x₁ < … < x_N` plus the coin sequence `(s₁, …, s_N)` in site order.
- **The gauge.** Multiply by `g = Π_{i: s_i = ↓}(−1)^{x_i}`.
  - Every hop not crossing the wrap bond `(L−1, 0)` becomes the up-coin spinless hop, with the sequence unchanged. A down coin's opposite amplitude is cancelled by the gauge's factor `−1` on the bond.
  - A hop across the wrap bond rotates the sequence: the record at `L−1` becomes the first.
- **The wrap sign.** The spinless-fermion wrap sign is `(−1)^{N−1}`. Hard-core fermions carry the same sign. Hard-core bosons carry none, i.e. an extra `(−1)^{N−1}` relative to spinless fermions (Jordan–Wigner). On odd rings the gauge is not single valued: a down coin crossing the wrap keeps a factor `−1`.
- **The result.** `H_hc = h_open ⊗ 1 + h_wrap ⊗ R + h.c.`, where `h` is `N` spinless fermions on the ring and `R` is the signed rotation.
- **The check.** `check.py` verifies every nonzero entry exactly, with generic rational bond weights, for rings `8 (N = 4, 6)` and `7 (N = 3)`, both signs:
  - the gauged value equals the predicted spinless value times the predicted factor;
  - the coin sequence transforms as predicted.
- **The consequence (linear algebra).** Diagonalise the unitary `R`. On its eigenvalue `ρ` the generator is the spinless band with twist `ρ` on the wrap bond. The spectrum is the union over `ρ`, with multiplicity.

**S5 (PROVED; CHECKED X.twists). Both exchange signs have one twist set.**
- `R` permutes coin sequences with signs. An orbit of period `p` whose signs multiply to `σ` carries the `p`-th roots of `σ`, once each.
- **Even rings.** `R^N = 1` (bosons: `((−1)^{N−1})^N = 1`). A sequence of full period `N` exists (↑↓…↓), so every `N`-th root occurs, for both signs.
- **Odd rings.** `R^N = (−1)^{n_↓}`, and both parities of `n_↓` occur with full period, so every `2N`-th root occurs.
- The sets coincide, so for every rate field the ground energy (the minimum over twists of the band's lowest `N` eigenvalues) is the same function for both signs.
- CHECKED exactly (integer orbit counting) on rings `8 (N = 4, 6)` and `7 (N = 3, 6)`. Example: 10 against 14 sequences at the twist `−1` for 6 records on the ring of 8. The executed ground degeneracies `g = 10/14` agree.

**S6 (PROVED; CHECKED X.sea exactly, X.half's floating note). The ring's sea and the half-filling bound.**
- **The ring's sea.** With twist `e^{iθ}` the band has eigenvalues `sin((2πm + θ)/L)`. For fixed `θ`, the minimum over `N` of the lowest-`N` sum is the sum over the window of negative ones.
- **The window lemma.** A window of `M` consecutive grid points sums to `sin(centre)·sin(πM/L)/sin(π/L) ≥ −1/sin(π/L)` (identity CHECKED exactly by minimal polynomials). Equality holds only for `M = L/2` centred at `−π/2`, i.e. `θ = π`, which the twist set contains when `N = L/2` is even. So for `4 | L` the lowest state over all `N` is half filled, with `E = −1/sin(π/L)`.
- **The free sea.** `E_free = 2 Σ_{λ<0} spec(φSφ)`, exactly, for every rate field. The down coin's band is `−φSφ`, and `Σ_{λ<0}(−A) = Σ_{λ<0}(A) − tr A` with `tr φSφ = 0`.
- **Zero modes persist.** `φSφ = −iφAφ` with `A` real antisymmetric, so `ker(φSφ) = φ^{−1} ker S` for every positive `φ`: the zero modes persist exactly.
- **The half-filling bound.** For `N = ⌊L/2⌋` or `⌈L/2⌉`, the untwisted sector (`θ = 0` is always in the twist set) gives exactly `E_free/2`, so `E_hc ≤ E_free/2`. For every rank-`N` projector, `Σ_N(A) ≤ Σ_N(B) + ‖A − B‖₁`. Twisting the wrap bond changes the band by a rank-2 operator of trace norm `w_wrap|e^{iθ} − 1| ≤ 2w_wrap`. Hence `0 ≤ E_free/2 − E_hc ≤ 2 max w` for every rate field.
- Executed on random rate fields on rings 8 to 16: the ratio lies in `[0.023, 0.147]`.

**S7 (PROVED; CHECKED X.half). The half-filled band's polarisability in closed form.**
- **The expansion.** Write `a_b = (u_x + u_{x+1})/2 = cos(q/2) cos(q(x + ½))`. The bond factor is `1 + εa_b + ε²a_b²/2 + …`.
- **The pieces for plane waves.**
  - Diagonal: `⟨k|h₂|k⟩ = sin k cos²(q/2)/4`.
  - Vertex: `⟨k+q|h₁|k⟩ = ½cos(q/2) sin(k + q/2)`.
  - Energy difference: `e_k − e_{k+q} = −2cos(k + q/2) sin(q/2)`.
- **The allowed transitions.** For `0 < q < π` they are two intervals of length `q`: `k ∈ (−q, 0)` by `+q`, and `k ∈ (−π, −π+q)` by `−q`. On both, `|cos(k ± q/2)| ≥ cos(q/2) > 0`, so the integrand is bounded.
- **Twist independence.** The twist shifts the grid by `θ/L` and the interval ends by `O(1/L)`. So the finite sums converge to the same Riemann integrals for every twist.
- **The integrals.**
  - Held: `−cos²(q/2)/(4π)`.
  - Relaxation: `−(cos²(q/2)/(4π sin(q/2)))[ln(sec + tan)(q/2) − sin(q/2)]`, using `∫ sin²t/cos t dt = ln(sec t + tan t) − sin t`.
  - The sum is the closed form of S7's statement.
- **The series** (sympy): `−1/(4π) + q²/(24π) + …`, so `c₀ = −1/π` and `κ = 1/(6π)`.
- **The two limits.** The free sea is two such bands (S6), so `Π_free → 2Π_hc`. The hard-core ground sector's second-order coefficient is its own band's, since the twist label is conserved at every rate field. Hence `Π_hc/Π_free → 1/2` at every fixed `q`.
- Executed at `L = 256`: ratio `0.49996` and `0.49994`; `Π_hc` matches the closed form to `2·10⁻⁶`; the `c₀` ratio is `0.50004`.

**S8 (PROVED; CHECKED X.holes). The free sea's filling under exclusion.**
- **The hole count.** `H(k)² = Σ_a sin²k_a`, so the one-body zeros are `k ∈ Π_a{0, π if L_a even}` times 2 coins, and the spectrum is symmetric. Hence `N_neg = n − h`, with `h = 2^{#even sides}`.
- **The energy bound.** Every entry of `H_hc` has modulus `w_b/2`, since every hop matrix is `σ_a/(2i)` with one target coin. A configuration with `h` holes has at most `2d·h` entries in its row, so Gershgorin gives `|E| ≤ h·d·max w`. CHECKED exactly (moduli and row counts) on rings 7, 8 and `3×3` at `N_neg`.
- **1D at fixed `q`.** The energy is minus the sum of the top `h ≤ 2` eigenvalues of a twisted band. The second-order coefficient of an eigenvalue is at most `‖h₂‖ + ‖h₁‖²/Δ_q`, where `Δ_q = 1 − cos q + O(1/L)` separates the two top levels from the plane waves they couple to (the top pair is closed under the sum). So `Π` per site is `O(1/L)`.
- Executed: `Π(π/2) = −0.0159` (L = 32), `−0.0039` (L = 128); `Π(2π/L)·8π²/L → −1.000`.

**S9 (PROVED; CHECKED X.edge). The free sea's smallest mode on even rings.**
- With `q = 2π/L`, the only relaxation channels of each coin's band are `k = −q → 0` and `k = −π + q → −π`: transitions into the exact zero modes. Each gives `−(1/16) sin q`.
- The held gradient term is `−(E₀/4) sin²(q/2)`, with `E₀ = −2cot(π/L)`.
- The sum `½cos(π/L)sin(π/L) − ½sin(π/L)cos(π/L) = 0` (sympy).
- So on even rings the smallest mode's gradient part measures the zero modes, not the sea. This matches the torus effect found in #8716.

**S10 (EXECUTED, floating point, labelled `note`). Exact diagonalisation.**
- **Method.** Dense diagonalisation, then second-order perturbation theory within the whole degenerate ground level: the first-order matrix `P₀H₁P₀`, then `P₀H₂P₀ + Σ_{n∉0}|·|²/(E₀ − E_n)`. On the ring of 8 with 6 records, direct second differences at `ε = 0.02, 0.04` and the twisted spinless band give the same `Π = −0.09857`.
- **Lesson.** A sparse Lanczos solver drops copies from highly degenerate ground levels (for example `g = 13` found against the true `14`) and then gives a wrong `Π`. All tables here are dense.
- **Ring 7:**
  - free: `c₀ −0.6259`, `G` `+0.0206`, `+0.0290`, `+0.0359`;
  - `N = 3`: `c₀ −0.3201`, `G` `+0.0150` … `+0.0188`;
  - `N = 4`: `c₀ −0.3210`, `G` `+0.0156` … `+0.0189`;
  - `N = 6` (1 hole): `c₀ −0.1429`, `G` `−0.1571`, `+0.0053`, `+0.0089`.
- **Ring 8:**
  - free: `c₀ −0.6036`, `G` `0`, `+0.0221`, `+0.0303`;
  - `N = 4`: `c₀ −0.3266`, `G` `+0.0204`, `+0.0169`, `+0.0184`;
  - `N = 6` (2 holes): `c₀ −0.2310`, `G` `−0.0697`, `−0.0120`, `+0.0134`.
- **`3×3`:**
  - free (`N = 8`): `c₀ −0.9292`, `G` `+0.0249`, `+0.0257`;
  - `N = 4`: splits at first order along `(1,0)`: slope `−0.0050` fermionic, `−0.0195` bosonic;
  - `N = 5` fermionic: `c₀ −0.4635`, `G` `+0.0092`, `+0.0124`;
  - `N = 5` bosonic: `c₀ −0.4246`, `G` `+0.0015`, and a first-order split along `(1,1)`;
  - `N = 8` (1 hole): `c₀ −0.1911`, `G` `−0.0267`, `+0.0046`, for both signs.
- **The `3×3` ground energy over `N`.** Lowest at `N = 5` for both signs (`−4.1715`, `−3.8211`), against `−1.7203` at `N = 8`.

**S11 (answers).**
- **(a)** The tables above.
- **(b)** Yes, exactly (S3).
- **(c) The volume term** never changes sign (S2). On rings the sea's is exactly half the free sea's in the limit. At the free sea's filling it vanishes per site (S8).
- **(c) The clock stiffness.**
  - The axioms' sea (half filled): on rings exactly half the free value and positive (S7); on `3×3` positive and smaller (`N = 5` fermionic: `0.37` and `0.48` of the free sea's along `(1,0)` and `(1,1)`).
  - At the free sea's filling the executed smallest-mode gradient parts are negative. The task's hit condition (opposite sign) is met there **only in that formal sense**: the response is the few holes' relaxation (`−L³` scaling in 1D, zero per site at fixed `q`), not a stiffness.

## 3. The first failing step

None for the claims made. The limits:
1. **2D and 3D.** Beyond the ring, the half-filled problem has no spin-charge separation (in 2D, hops flip coins and records pass each other), so only the `3×3` torus is executed.
2. **Degeneracy on `3×3`.** There the ground levels are degenerate across momenta at `N = 4` (both signs) and at `N = 5` (bosons, along `(1,1)`). The rate mode splits them at first order, so no polarisability exists for those levels on that torus.
3. **The `4×4` torus is not done.** Its half-filled and free-filling spaces have dimensions `3.3·10⁶` and `7.5·10⁶`, and dense or sparse-Lanczos treatment of degenerate levels fails, as S10's lesson shows. It needs momentum sectors.

## 4. What would finish it

1. **The `4×4` torus in momentum sectors.** Translation times the coin-sublattice parity `Q = n_↑ + Σ(x+y) mod 2` gives sectors of about `10⁵`. This would give 2D numbers on a bipartite torus with the chessboard.
2. **The half-filled hard-core sea in 2D and 3D in the thermodynamic limit.** With coin-flipping hops this is a genuinely interacting problem; a sign-free formulation or tensor-network methods would be needed.
3. **The massive and scalar-hop families (block 77).** In 1D the reduction survives any coin-diagonal walk; the staggered term `mε` is on-site and would enter the spinless band as a staggered potential.
4. **Whether the sea's number of records is fixed by anything in the clauses.** Here "the sea" is the minimum over `N`, as for the free sea.

## 5. Running it

```
python3 probes/work/derive/the-hard-core-seas-energy/w-macbookpro90c72-j7e98/check.py
```

The run takes about 130 s (dense diagonalisation up to dimension 4032) and uses about 1 GB. It prints eight exact checks, then the floating-point notes, then the SUMMARY and HIT lines.
