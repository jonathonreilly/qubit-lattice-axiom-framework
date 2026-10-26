# J:derive:the-hard-core-sea-in-two-and-three-dimensions:a1 — the hard-core sea beyond the ring

**Worker:** Claude Sonnet 5.5, one session, attempt 1 of 2. Same family as the sources; unrefereed.
**Verdict:** PARTIAL. The route stops at step 14 (a certified exact value of the 4×4 half-filled ground energy and the infinite-volume sign of the stiffness).

## 0. Plain language

On a ring, the hard-core records are one band of particles that cannot pass each other, so the exchange sign does not matter and the energy is exactly half the free sea's (block 130). In two and three dimensions I found the following.

1. **An exact simplification that works in every dimension.** After a site-by-site rotation of the coin, the 2D and 3D walk with one record per site is an ordinary hopping problem with no coin dependence at all: real hops of size 1/2 with a half-flux (π) through every square, and the coin acts as a conserved spin. So the sea's lowest energy can be read in the sector of smallest total spin projection. Every lower or upper bound below uses this.
2. **Exact bounds on the volume term per site.** In 2D the volume term lies between −1/√2 = −0.7071 (exact) and −0.4790 for fermion-like records, or between −0.7071 and −0.3536 for boson-like records. The free sea (double occupancy allowed) has −0.9581. The ring's value is exactly half the free sea's; in 2D the bracket for fermion-like records is [−0.569 (float), −0.479], so the upper end is exactly "half the free sea". In 3D: lower −1.0607 (exact), fermion upper −0.5969.
3. **The exchange sign matters beyond the ring.** On a 2×3 cluster with 3 records, exact ground energies are −1/2−√3 = −2.2321 for fermion-like and −2.1126 (a root of a degree-9 integer polynomial) for boson-like. On the 4×4 torus at half filling (floating point) they differ by 1.7 percent: −7.45819 and −7.58611.
4. **The 4×4 torus (floating point, not exact).** Half filling is the minimum over record number (checked N=1 to 15 in a development run, N=7 and 8 in `check.py`). Energy per site −0.466137 (fermion-like, total spin 2) and −0.474132 (boson-like, spin 0). The rate-mode coefficient at the smallest wave vector is −0.094313 and −0.093072, which sits above c0/4 (−0.116534 and −0.118533) by 0.0222 and 0.0255: the same sign as the ring, a bit smaller than the ring's value at the same wave vector. This is evidence, not a certificate.
5. **What is not done.** I did not get an exact (certified) 4×4 ground energy; I did not use momentum sectors; and I have no sign certificate for the stiffness in infinite volume.

## 1. Sources read, and the premises

**Read in full, on main (detached checkout at `a77a3449c91a753b06ce2a63876cd460b62cb4cf`, committer date 2026-10-25), not from PR branches:**

- `docs/MINIMAL_AXIOMS_2026-06-29.md` (233 lines). Used: Lattice (:35-41), Qubit (:43-53), Admissibility (:55-73), Record (:75-83), "Admissibility is not a dynamics axiom" (:114-123). The axioms supply a site domain, a distribution rule and one record per site; they do not supply a Hamiltonian, a composition rule, a record number or a rate field.
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` (130 lines). Approved primitives: `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` (:31-129). **None is used here.**
- Block 130, as landed: `docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md`. It is already on main, so I did not need PR #9187's branch. Used: T1 packing (:68-82), T2 band (:84-99), T3 one twist set (:101-107), T4 `c0 = −1/π`, `κ = 1/(6π)` (:109-139), "Open: two and three dimensions" (:187), N1 route 1 (:196), `next_trace_action` (:152) naming the 4×4 torus in momentum sectors.
- Block 76, as landed: `docs/ADMISSIBILITY_RULE_THE_FILLED_SEAS_ENERGY_AS_THE_LEDGERS_FIELD_TERM_A_CHESSBOARD_OF_CLOCKS_IS_INVISIBLE_THE_SEA_INDUCES_A_CLOCK_STIFFNESS_NOT_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-22.md`. Used: reciprocal chessboard invariance (:29-33); the comparator is "not the exact sea Hessian" (:4, :55).
- Block 78, as landed: `docs/ADMISSIBILITY_RULE_ONE_RECORD_PER_SITE_IS_AN_INTERACTION_NOT_A_FREE_SEA_TWO_RECORDS_UNDER_EXCLUSION_AGAINST_FREE_ANTISYMMETRIC_AND_SYMMETRIC_PAIRS_BOUNDED_THEOREM_NOTE_2026-09-22.md`. Used: the compression of the free generator to different-site configurations, either exchange sign supplied (:25-27).
- Block 54, as landed: `docs/ADMISSIBILITY_RULE_A_PHASE_TIMED_BY_THE_LOCAL_CLOCK_EVERY_PACKET_FALLS_TOWARDS_SLOW_CLOCKS_FORCE_IS_ENERGY_TIMES_GRADIENT_WEIGHT_AND_INERTIA_TIED_BY_THE_WALK_BOUNDED_THEOREM_NOTE_2026-09-21.md`. Used: `D_j = (i/2)(T_j − T_j†)`, `H = Σ_j σ_j D_j` (:26, :40) and `H_w = φHφ` (:44).

I did not read the open PR branches for blocks 126-129. The only open-PR search I ran (`gh pr list --search "hard-core sea"`) returned nothing, which is not an exhaustive search. A scan of the file names under `docs/` on main found no note on a 2D or 3D hard-core sea.

**Supplied by the lane, not by the axioms** (assumptions, as in the sources): the walk `H = Σ_j σ_j D_j` with `⟨x|H|x+e_j⟩ = −(i/2)σ_j`; the clock `φ = e^{u/2}` acting as `H_w = φHφ`, so a hop across bond `xy` carries `φ_xφ_y`; `n` sites, `N` records, one coin per record; the generator is the free many-record generator compressed to configurations with at most one record per site; fermionic (order sign over modes `2x+coin`) or bosonic (no sign) composition; "the sea" = lowest state over all `N` and all coin sectors; rate mode `u = ε cos(q·x)` with `E₀(ε) − E₀(0) = Π(q) ε² n + O(ε³)`, `c₀ = E₀/n`, `Π(q) = c₀/4 + (κ/4)|q|²_lat + …`. Tori have every side divisible by 4 (needed for the real-hop form in step 1; divisibility by 2 suffices for a complex scalar hop).

**Method note.** I formed my plan before reading the prior attempts: reduce the coin structure by a gauge, use total-spin conservation, bound by tiles, and treat the 4×4 torus with sparse Lanczos in the `S_z` sector. The earlier attempt `the-hard-core-seas-energy` a1 (Opus, unrefereed) did the 3×3 torus in floating point and listed the 4×4 torus as open; I did not use its numbers.

## 2. The exact statement attempted

For the 2D walk `σ₁D_x + σ₂D_y` (and the 3D walk `σ₁D_x + σ₂D_y + σ₃D_z`) with one record per site, both exchange signs:
- (a) on the 4×4 torus at half filling `N = 8`, the exact ground energy per site and the second-order coefficient `Π(q_min)` of `u = ε cos(q·x)`, `q_min = (π/2, 0)`;
- (b) rigorous two-sided bounds on `c₀` per site in 2D and 3D;
- (c) the sign of the induced stiffness, with a certificate if possible.

## 3. Steps

**Step 1. PROVED, CHECKED exactly (`check.py` S1).** *Gauge to a scalar π-flux hop.* Put `g(x) = σ₁^{x₁}σ₂^{x₂}σ₃^{x₃}` and `V = ⊕_x g(x) i^{x₁+x₂+x₃}`. Then `V† h V = t ⊗ 1₂` with `t` real: `t(x,x+e₁) = 1/2`, `t(x,x+e₂) = (−1)^{x₁}/2`, `t(x,x+e₃) = (−1)^{x₁+x₂}/2`.
*Proof.* A hop along `e_j` has block `−(i/2)σ_j`. With `g(x)† = σ₃^{−x₃}σ₂^{−x₂}σ₁^{−x₁}`, the product `g(x)†σ_j g(x+e_j)` has `σ_j` twice in the `σ_j`-power slot, giving `σ_j² = 1`, and one has to commute the extra `σ_j` past the Pauli factors of lower index: `σ₁^{−x₁}σ₂σ₁^{x₁} = (−1)^{x₁}σ₂`, and `σ₂^{−x₂}σ₁^{−x₁}σ₃σ₁^{x₁}σ₂^{x₂} = (−1)^{x₁+x₂}σ₃`. So the block is scalar: `−i/2` times `1`, `(−1)^{x₁}`, `(−1)^{x₁+x₂}` for `j = 1, 2, 3`. The phase factor `i^{x₁+x₂+x₃}` on the two ends contributes `conj(i^{|x|}) i^{|x|+1} = i`, which turns `−i/2` into `1/2`. For a torus, `g` and `i^{x}` are periodic exactly when each side is divisible by 4. Every plaquette has hop product `−(1/2)⁴` (π flux). `check.py` verifies `V†hV` equals the real matrix entry by entry (zero difference) for 4×4, 4×4×4 and 8×8, and the plaquette sign on the 4×4 and 4×4×4 tori. ∎

**Step 2. PROVED (argument), CHECKED (`check.py` S2).** *The hard-core generator is gauge covariant.* The constraint `n_x ≤ 1` (`n_{x↑}n_{x↓} = 0` for fermions, `n_x(n_x−1) = 0` for bosons) depends on the two coin modes of a site only through `n_x = Σ_a c†_{xa}c_{xa}`, which is invariant under a unitary on those two modes. The many-body map `Γ(V)` therefore carries `P dΓ(h) P` to `P dΓ(V†hV) P`, for both exchange signs, and the rate weights `φ_xφ_y` are scalars on each bond, so they commute with `V`. `check.py` compares the first four to six traces of powers of the original coin-basis generator (N=2, 3 on the 4×4 torus, both signs) with the sum over `S_z` sectors of the gauged generator: zero difference. For the 3D walk the many-body check is on the open 2×2×2 cube (N=3, 4: full spectra of the original coin-basis generator against the union of gauged sectors); the 3D torus is covered by the one-body identity and the argument. It also reproduces the ring value `−csc(π/8)` for `L = 8`, `N = 4` in the original model for both signs (block 130 T4a). ∎

**Step 3. PROVED, CHECKED (S3).** *Spin conservation.* The gauged generator is `Σ_b t_b B_b`, where `B_b` hops a record along bond `b` onto an empty site keeping its coin. It commutes with `S = Σ_x d†_x(σ/2)d_x` (the hop is coin independent; `P` depends on `n_x` only). Hence every eigenvalue of the full space occurs in the sector `S_z = 0` (`N` even) or `S_z = 1/2` (`N` odd). The minimum over all spins is the minimum in that sector. `check.py` verifies `S⁻H = HS⁻` entrywise for the integer matrix `2H` on the 4×4 torus (N=3, 4, 5; both signs).

**Step 4. PROVED. *Tile lower bound.*** Let `H = Σ_b B_b` over the bonds of a torus (side ≥ k+1), each hop with its gauged amplitude. A `k^d` window `W` of sites contains `m = (k−1)k^{d−1}` copies of any given bond direction among its translates. So `H = Σ_{translates W} (1/m) Σ_{b∈W} B_b`. The operator `H_W = Σ_{b∈W} B_b` is an even operator supported on the sites of `W`; with the modes of `W` ordered first, it acts as `H_W^{isolated} ⊗ 1`, and the hard-core projector factorizes. So its lowest eigenvalue on the whole space equals the lowest eigenvalue of the isolated window over all record numbers and spins, `λ_W`. Therefore `E₀ ≥ n λ_W / m`, i.e. `c₀ ≥ λ_W / m` for every torus whose side is at least `k+1` and divisible by 4, in either composition (using the composition's own `λ_W`).
- `d = 2`, `k = 2`: `λ_W = −√2` for both signs, `m = 2`, so `c₀ ≥ −1/√2` (CHECKED exactly: sympy characteristic polynomials of every sector, 60-digit root).
- `d = 2`, `k = 3` (float, `check.py` S5): `λ_W = −3.4142136` (F), `−3.2269617` (B); `m = 6`: `c₀ ≥ −0.56904` (F), `−0.53783` (B).
- `d = 3`, `k = 2` (float): `λ_W = −2√3 = −3.4641016` (F), `−3.0208819` (B); `m = 4`: `c₀ ≥ −0.86603` (F), `−0.75522` (B).
- `d = 3` from plaquette tiles (exact): each bond lies in 4 plaquettes and there are 3n plaquettes, so `c₀ ≥ (3/4)(−√2) = −1.0607`.
The cube minima do not depend on the base position of the window (S4, all four positions; the gauge differs by site signs).

**Step 5. PROVED. *Product-state upper bound, both signs.*** Partition the lattice into disjoint clusters. A product of cluster eigenstates with definite record number has zero expectation for every hop between clusters (it changes the cluster numbers) and is exactly additive for the intra-cluster terms (for fermions the intra-cluster bilinears are even and commute with the other clusters' creation polynomials). So `c₀ ≤ λ_C / |C|`. With the 2×2 plaquette: `c₀ ≤ −√2/4 = −0.35355` in 2D and 3D (exact). Larger clusters (float): 3×3: −0.37936 (F), −0.35855 (B); cube: −0.43301 (F), −0.37761 (B).

**Step 6. PROVED. *Fermion bracket from the free sea.*** (i) Lower: the fermionic hard-core generator is a compression of the free N-fermion generator on a subspace, so its lowest eigenvalue is at least the free N-particle lowest eigenvalue; minimum over N gives `c₀ ≥ c₀^{free}` (the sum of all negative one-body levels per site; −0.95809 in 2D, −1.19380 in 3D; weaker than the tiles). (ii) Upper: fill only the coin that is rotated to "up" at every site in the gauged frame. No site can then hold two fermions, so the state is in the hard-core space, and the hop acts as the spinless π-flux hop `t`. Its sea has exactly half the free sea's energy, because the one-body spectrum of `t ⊗ 1₂` is the free spectrum and `t` carries each level once. So `c₀ ≤ c₀^{free}/2`: −0.479046 in 2D, −0.5969 in 3D (numerical quadrature: the 2D value is an elliptic-integral quadrature in mpmath at 25 digits; the 3D value is a midpoint grid, 96 and 192 points agreeing to 6 digits). On the 4×4 torus the exact numbers are free `−(8+4√2)/16 = −0.85355` and polarized `−0.42678`. For bosons the spin-polarized state is not a boson state of this kind, so this step gives nothing for bosons.
Consequence (PROVED): `c₀ < 0` strictly in 2D and 3D for both signs, since the product-state bound is negative.

**Step 7. PROVED. *Second order splits into a held term and a relaxation term.*** For `w_b = exp(ε α_b)`, `α_b = (cos q·x_a + cos q·x_b)/2`, write `H_w = H + εH₁ + ε²H₂ + …`, `H₁ = Σα_bB_b`, `H₂ = ½Σα_b²B_b`. If the ground level is nondegenerate (or the first-order matrix on it vanishes), `Π(q) n = ⟨H₂⟩ − ⟨H₁ R H₁⟩`, with `R = Q(H−E₀)^{-1}Q ≥ 0`. So the relaxation term is ≤ 0 and `Π(q) ≤ ⟨H₂⟩/n = (1/2n) Σ_b α_b² ⟨B_b⟩`. At `q = (π,…,π)` each bond joins sites of opposite parity, `α_b = 0`, `H_w = H`, `Π = 0` exactly (block 76's chessboard). If the ground state is translation invariant, `⟨B_b⟩ = e_j/n` for a bond in direction `j` (`e_j` = total energy of direction-`j` bonds), and for `2q ≢ 0` the held term reduces to `(1/4) Σ_j (e_j/n) cos²(q_j/2)`, block 130's `(c₀/4)cos²(q/2)` in 1D; for `q = (π, 0)` the bond products `α_b²` average to 1 on the y-bonds, not 1/2. CHECKED (S7): the held term equals `½ Σ_b α_b² ⟨B_b⟩` with `⟨B_b⟩ = e_j/16` to 10⁻⁷ at `q = (π/2, 0)` and `(π, 0)`.

**Step 8. CHECKED exactly (S4). *The exchange sign matters in 2D.*** On the open 2×3 cluster (6 sites, gauged flux π on both squares), `N = 3` records, the sector `S_z = −1/2` contains every spin. Exact characteristic polynomials: fermion ground energy `−1/2 − √3 = −2.232051` (root of `x²+2x−11` after dividing by 2); boson ground energy −2.112633 (least real root of the degree-9 integer polynomial `x⁹+x⁸−20x⁷−6x⁶+99x⁵+9x⁴−156x³−9x²+54x+9` after halving). They differ by 0.1194. The spectrum of the original coin-basis generator on this cluster equals the union of the gauged sectors for both signs (S4). This is a counterexample to extending block 130's T3 (same ground energy for both signs) from the ring to the 2D walk. It is a statement about a 6-site cluster, not about the torus.
*Reading (not proved):* on a ring records cannot pass, so their cyclic order and coin sequence are conserved and the sign only changes the twist set, which is the same. In 2D they pass, and the spatial parts of the many-record problem lie in different representations of the permutation group for the two signs (at most two rows for bosons, at most two columns for fermions, by Schur-Weyl duality with the spin-1/2 coin). I did not check this decomposition.

**Step 9. CHECKED, floating point (S7). *The 4×4 torus at half filling.*** Sector `N = 8`, `S_z = 0`, dimension 900 900; sparse Lanczos from two different start vectors:

| | fermion-like | boson-like |
|---|---|---|
| `E₀` | −7.458194293716 | −7.586109962153 |
| `c₀ = E₀/16` | −0.466137143 | −0.474131873 |
| residual `‖Hψ − E₀ψ‖` | 4×10⁻¹⁴ | 3×10⁻¹⁴ |
| gap to next level in the sector | 0.02656 | 0.26444 |
| `⟨S²⟩` of the ground state | 6 (S = 2) | 7×10⁻²⁸ (S = 0) |
| bond energy per direction `e_x = e_y` | −3.729097147 | −3.793054981 |

The ground state is nondegenerate in the `S_z = 0` sector for both signs. For the fermion-like sign the full ground level is a spin-2 multiplet (five degenerate states across `S_z`); the rate perturbation is spin-scalar, so the multiplet does not split.
*Minimum over N (development run of the same code, N = 1 to 15, `S_z ≈ 0`, sparse Lanczos; `check.py` re-runs N = 7 and 8 only):*

| N | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F | −1.4142 | −2.8284 | −3.9991 | −5.1759 | −5.8574 | −6.8284 | −7.1399 | **−7.4582** | −7.2875 | −7.0585 | −6.3864 | −5.5731 | −4.4189 | −3.2366 | −1.7915 |
| B | −1.4142 | −2.8284 | −3.9991 | −5.1759 | −5.9722 | −6.7378 | −7.1585 | **−7.5861** | −7.4281 | −7.1132 | −6.5032 | −5.7283 | −4.6280 | −3.3586 | −1.7915 |

So the minimum over record number is at half filling `N = n/2` for both signs, as on the ring. The sign changes the energy from `N = 5` on; the two signs cross over (B lower at N=5, F lower at N=6).
*What is exact:* an exact rational Rayleigh quotient of a 2²⁸-rounded eigenvector (integer arithmetic, 900 900 components) gives an upper bound `E₀ ≤ −7.458194293709` (F) and `≤ −7.586109962145` (B), and an exact residual shows an eigenvalue within about 8×10⁻⁶ of those. **There is no certified lower bound.** The tile bound gives only `E₀ ≥ −9.10` (F) and `−8.61` (B).

**Step 10. CHECKED, floating point (S7). *Rate-mode coefficient on the 4×4 torus.*** Per site, `Π(q) = (held + relax)/16` by conjugate gradients in the full sector (first-order terms vanish to 10⁻¹⁵; a finite-difference with `ε = 0.02` agrees to 3×10⁻⁶). Units of `q`: `(m₁, m₂)` means `q = (m₁, m₂)π/2`.

| q | F held | F relax | **F Π** | B held | B relax | **B Π** | free Π |
|---|---|---|---|---|---|---|---|
| (1,0) | −0.087401 | −0.006913 | **−0.094313** | −0.088900 | −0.004172 | **−0.093072** | −0.191942 |
| (1,1) | −0.058267 | −0.009384 | −0.067651 | −0.059266 | −0.005886 | −0.065153 | −0.150888 |
| (2,1) | −0.029134 | −0.008708 | −0.037842 | −0.029633 | −0.008956 | −0.038589 | −0.088388 |
| (2,0) | −0.116534 | −0.009421 | −0.125956 | −0.118533 | −0.015724 | −0.134257 | −0.213389 |
| (2,2) | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

`Π(π,π) = 0` as required by step 7. The held term equals `½ Σ_b α_b² ⟨B_b⟩` with translation-invariant bond energy to 10⁻⁷, and the relaxation is ≤ 0 everywhere, as step 7 says.
*Comparison with `c₀/4`* (F: −0.116534, B: −0.118533, free: −0.213388): `Π − c₀/4` = F 0.02222, 0.04888, 0.07869, −0.00942, 0.11653 at the five `q`; B 0.02546, 0.05338, 0.07994, −0.01572, 0.11853. At `q = (π/2, 0)` the effective stiffness `κ_eff = 4(Π − c₀/4)/|q|²_lat` with `|q|²_lat = 2(1−cos q) = 2` is 0.0444 (F), 0.0509 (B), 0.0429 (free); the ring at the same `q` gives 0.0600 (closed form of block 130) and tends to `1/(6π) = 0.0531` as `q → 0`. So at the smallest torus wave vector the stiffness indicator is positive for both signs, with the same sign as the ring and the free sea. At `q = (π, 0)` the difference is negative (−0.0094, −0.0157) while the free sea's is zero to 10⁻⁶: a stripe of clocks along one axis lowers the hard-core sea's energy slightly below the uniform value. That is a finite-size feature at a large wave vector; I did not explain it.

**Step 11. PROVED given an assumption, answers (c) partly.** Assume `Π(q) → c₀/4` as `q → 0` (the convention of block 76 and 130 for the infinite sea; not proved in 2D or 3D). Then `Π(π,…,π) − Π(0⁺) = −c₀/4 > 0` by step 6. So the secant slope of `Π` from the uniform mode to the chessboard has the ring's sign in 2D and 3D, for both exchange signs. This does not give the sign of `κ` at `q → 0`.

**Step 12. ASSUMED.** Thermodynamic limits exist and the tile/cluster brackets pass to them (they hold on every finite torus of side ≥ k+1 divisible by 4).

**Step 13. READING.** The fermion-like sea is bracketed by [−0.569, −0.479] in 2D, a window of 0.09 per site; the ring is exactly at the top ("half the free sea"). The 4×4 value −0.4661 lies inside it. For bosons the bracket [−0.538, −0.359] is wide and the 4×4 value −0.4741 lies inside it. Nothing here says whether the infinite 2D value is the top of the bracket.

**Step 14. THE FIRST STEP THAT FAILS: a certified exact value for the 4×4 half-filled ground energy.**
- The sector has 900 900 states (180 180 with total spin 0 and 56 000-ish per translation sector). Even after translations (16, magnetic), the coin-sublattice parity and the point group, the remaining blocks are about 10³-10⁴ states. I did not do that reduction. Without `flint`, a sparse exact factorization, or a certified eigenvalue solver in the available tools, I could produce only an exact upper bound (rational Rayleigh quotient) and a floating-point eigenvalue, not a lower bound.
- The tile bound is too loose by 1.0 to 1.6 in energy (−9.10 against −7.46 for F, −8.61 against −7.59 for B).
- The infinite-volume sign of `κ` needs the thermodynamic ground state in 2D, where there is no spin-charge separation. I have only the 4×4 evidence and the secant statement of step 11.

## 4. What is new relative to the sources

- **New and exact (within the lane's supplied model):** step 1 (gauge to an SU(2)-symmetric π-flux hop in 2D and 3D, with the explicit sign pattern), step 3 (spin conservation, so the sea is read in the `S_z ≤ 1/2` sector), steps 4, 5, 6 (exact and float-checked two-sided brackets, both signs), step 7 (held/relaxation split with a sign), step 8 (exact 2×3 counterexample to carrying T3 beyond the ring).
- **New but floating point only:** steps 9 and 10 (4×4 torus). The earlier unit `the-hard-core-seas-energy` a1 did the 3×3 torus in floating point and listed the 4×4 torus as not done. Its 3×3 setting is odd, so the gauge of step 1 does not apply to it; I did not compare.
- **Not new:** retrieval of blocks 54, 76, 78, 130; the ring result; the facts that the chessboard is invisible and that the volume term is negative on a connected hopping graph.
- Overlap with open PRs: none found (see section 1).

## 5. Falsifiers

- A site-rotation `V` of step 1 for which `V†hV` is not `t ⊗ 1₂`, or a plaquette of the gauged lattice whose hop product is not −(1/2)⁴.
- An N=2 or N=3 coin-basis trace of the original generator that differs from the gauged one.
- A different exact ground energy for the 2×3 cluster, N=3 (either sign) from the two integer polynomials above.
- A 4×4 half-filled eigenvalue below −7.4582 (F) or −7.5861 (B) by more than 10⁻⁹, or a different `Π(π/2, 0)`.

## 6. What would finish it

1. Sector the 4×4 problem by magnetic translations (16), the coin-sublattice parity, the point group, and total spin, then certify a lower bound on the lowest eigenvalue per sector by an exact factorization or a certified (interval) eigensolver; or find a Lehmann/Temple bound with a certified gap.
2. For the stiffness: the 8×4 or 4×4×2 torus in the same sector method (with larger `q` resolution), or tensor-network methods for the infinite 2D problem; and an analytic account of the `q = (π, 0)` dip.
3. For the exchange sign: classify the spatial representations that lie below for each sign (Schur-Weyl) and see which one holds the half-filled sea.
4. Whether the spin-2 multiplet of the fermion-like 4×4 sea is generic (Nagaoka-type) or finite-size.

## 7. Running it

```
python3 check.py
```
Final run: `TOTAL: PASS=63 FAIL=0`, 169 s wall, one process, peak resident memory 1.28 GB (an earlier run of the same code measured 1.08 GB; the 4×4 half-filling matrices dominate). No RECOVERY_STATUS.json: the task names no source branch. The `dev/` folder holds the exploratory scripts and logs that produced the N=1 to 15 table and the open 4×4 patch values (not used in any claim): `dev/t3.log`, `dev/open4.log`.
