# a-filled-level-of-one-sense-under-exclusion, attempt 1 of 2

**The free content is a partition with zero net flux; the lens's filling does not exist under exclusion; the reachable mirror loses its species content.**

Worker `w-jonathonsmac4f50-j3b8b` (`claude-opus-5-5`), unit `J:derive:a-filled-level-of-one-sense-under-exclusion:a1`.

**Provenance.**
- There were no prior attempts.
- Definitions come from:
  - block 77 (PR #8612): the family `a₀ + 2aΣ_j C_j + Σ_j σ_j S_j`, its levels and senses;
  - block 78 (PR #8613): the exclusion. Records carry a coin, and no two sit on one site whatever their coins, with either exchange sign. The compressed generator `PHP` is block 78's and block 80's.
- I formed my plan first: the capacity bound, the jam, the free content, and ground states on the `4×4` slice. Only then did I read the later blocks of the same campaign, which are by the same model family as me and unrefereed:
  - Block 80 (PR #8615) found, executed only and at `a = 0`, that under exclusion the free sea's filling is a jammed lattice.
  - Block 85 (PR #8657) T2(b) proves that with a record on every site the compressed generator is zero ("the jam is blind"). My step 7 restates this with `a₀` and adds `n(k) = 1`.
- The sibling derivation `filling-between-the-a-terms-levels-chiral-content` asks the free part in more detail. It has no delivered attempts.
- Nothing is adopted. The parked decisions are not touched. The exchange sign is not supplied, so both signs are run.

## 1. What is claimed

> **(a) The free comparator.** Take `H(k) = a₀ + 2aΣcos k_j + σ·s(k)`, `s = (sin k_j)`, on `Z³` (and on the 2D slice, and on every even torus), with `a ≠ 0`, and a Fermi level `μ` not at a level.
>
> 1. *(exact count; two standard theorems ASSUMED)* Both bands' Fermi seas contain exactly the zeros below `μ`. So:
>    - The degree of `s/|s|` on either band's Fermi surface (oriented outward from the sea) is the sum of the senses below `μ`: `−1, +2, −1` in the three gaps, top to bottom (`a > 0`).
>    - The two bands' Berry fluxes are opposite.
>    - Hence **the net right-minus-left of the whole gapless content, counted by Berry flux, is 0 in every gap and for every `a`.**
> 2. *(exact count)* The content is a partition of the species by level. The zeros above `μ` versus below `μ` are:
>
>    | Gap | Above `μ` | Below `μ` |
>    |---|---|---|
>    | 3D top | 1 species, sense `+1` | 7 species, net `−1` |
>    | 3D middle | 4, net `−2` | 4, net `+2` |
>    | 3D bottom | 7, net `+1` | 1, net `−1` |
>    | 2D top | net `+1` | net `−1` |
>    | 2D bottom | net `−1` | net `+1` |
>
>    The lens's "single right-handed species" is the side above `μ` of the top gap.
> 3. *(numeric)* Which species are gapless:
>    - At `a = 1/10` every gap has eight pockets, one per species, each of degree equal to its sense. So all eight species are gapless, four of each sense.
>    - At `a = 1` in the top gap, the only species enclosed is the top one. It is enclosed by two sheets, one per band, with opposite Berry flux. This holds across the top gap for `a ≥ 0.3`.
> 4. *(exact identity; Weyl-cone comparator)* The chiral density is `Σ_i χ_i(μ − E_i)³/(6π²) = −64a³/π²` at every `μ`. The `a`-term sets it, not the filling.
>
> **(b) Under the Record axiom's exclusion** (owner's reading: one record per site at a time, whatever the coins).
> 1. *(exact)* The spectrum is symmetric about `a₀`.
> 2. *(proved; exact counts)* A Fermi level in the top gap needs more records than sites: at least `N_s + 6` in 3D and `N_s + 2` in 2D, on every even torus. **The lens's filling does not exist for the axioms' records, for either exchange sign or none.**
>    - On the `4³` torus (`a = 1/12`) the three gaps need 70, 64 and 58 records on 64 sites.
>    - So the 3D middle gap is exactly one record per site, and only the bottom gap is reachable.
>    - On the `4×4` slice (`a = 1/8`) the two gaps need 18 and 14 records on 16 sites.
> 3. *(proved; checked)* At one record per site every move is blocked. The generator is `a₀N` times the identity and `n(k) = 1` at every `k`, so no species is singled out.
> 4. *(executed, not claimed)* The reachable mirror is 14 records on the `4×4` slice, the free sea's bottom gap. The free sea there has the `(π,π)` species (sense `+`) full and the other three empty. Under exclusion, for both exchange signs and for `a = 1/8` and `1/16`:
>    - the ground state has crystal momentum `(π,π)`;
>    - its per-state occupations at the four zeros differ by less than 0.08 (free: by 1);
>    - they are ordered by level energy across both senses, and the differences shrink with `a`.
>
>    **The free content is not of one sense and does not survive.** The task's HIT condition, a one-sense interacting content, is not met.
> 5. *(executed, not claimed)* Now read the lens's filling as a chemical potential in the free top gap, `(0, 4a)`. On the `4×4` slice at `a = 1/8` the hard-core ground state then holds at most 14 records, for either sign. A 15th record, or filling to the jam, costs more than `4a` by a margin above 0.5. So the same chemical potential also lands at or below the bottom gap's filling.
>
> **(c)** What "chiral content" can mean for an interacting many-record state, and what a theorem would need: section 4.

## 2. The steps

1. **CHECKED (A1).** At `k = πn`, `Σcos = d − 2|n|` and `s = 0`. The index `sign det Ds(πn) = Πcos(πn_j) = (−1)^{|n|}` is block 77's sense. Multiplicities are 1:3:3:1 (3D) and 1:2:1 (2D).

2. **PROVED, from two ASSUMED standard theorems; CHECKED count (A2).**
   - *Setup.* Let `O_b = {k : E_b(k) < μ}` for `b = ±`. At a zero both bands equal `E_i`, so `k_i ∈ O_b` iff `E_i < μ`, for both `b`. Away from the zeros `s ≠ 0`, so the bands never touch there. For `μ` a regular value, `∂O_b` is a smooth closed surface avoiding the zeros; otherwise move `μ` slightly within the gap.
   - *ASSUMED (index theorem).* For a compact region of the torus with smooth boundary avoiding the zeros of `s`, the degree of `s/|s|` on the boundary equals the sum of the indices of the zeros inside. Hence `deg(ŝ|∂O_±) = Σ_{E_i<μ} χ_i`.
   - *ASSUMED (two-band flux relation).* For `d₀ + d·σ`, the Berry curvature of band `±` is `∓½` the pull-back under `d̂` of the sphere's area form. So band `±`'s flux through `∂O_±` is `∓2π·deg`.
   - *Conclusion.* The two bands' fluxes cancel for every `μ` in every gap and every `a`. The partition table is an exact count.

3. **NUMERIC (A3).** The pockets are found on a `64³` grid:
   - components of `{E₋ > μ}` (holes) and `{E₊ < μ}` (electrons), with periodic labelling;
   - the degree of `ŝ` on each component's voxel boundary, by summing signed solid angles.
   - At `a = 1/10`, mid-gap, the pocket radii are at least 0.2 against a grid step of 0.098.
   - A scan over `a = 0.2 … 1` shows the merging. Near the gap edges at `a = 0.2`, pockets smaller than the grid step are missed; the claim is made only where the radii are resolved.

4. **CHECKED (A4).** `Σ_m (−1)^m C(3,m)(μ − a₀ − 2a(3 − 2m))³ = −384a³`, because the moments `Σ_m(−1)^mC(3,m)(3 − 2m)^p` are `0, 0, 0, 48` for `p = 0…3`.
   - This is the comparator only: unit isotropic cones, pocket counts `(μ − E_i)³/(6π²)`, and the `a`-term's curvature near each zero neglected.

5. **CHECKED (B1).** `k → k + π(1,…,1)` flips `Σcos` and `s`, so `E₊(k + π) − a₀ = −(E₋(k) − a₀)`. On an even torus this is a bijection of the momenta.

6. **PROVED + CHECKED (B2).**
   - By B1, on any even torus `#(E < a₀) = #(E > a₀) = N_s − z/2`, with `z = #(E = a₀)`.
   - *3D, top gap.* The six states of the second level `a₀ + 2|a|` lie between `a₀` and `μ`, so `N_free(μ) ≥ N_s − z/2 + z + 6 ≥ N_s + 6`.
   - *2D, top gap.* The middle level lies at `a₀` with four states, so `z ≥ 4` and `N_free ≥ N_s + 2`.
   - *The cap.* Exclusion allows `N ≤ N_s`.
   - *Infinite volume.* The same holds as a density: the filling fraction exceeds one half, which is more than one record per site.
   - *Exact counts.* Sympy with exact square roots: no state lies strictly inside any gap on the `4³` torus at `a = 1/12` or on `4×4` at `a = 1/8`, so each gap has one filling. The fillings are 70/64/58 and 18/14.
   - This is conditional on the owner's reading of the Record axiom. If opposite coins could share a site, the free antisymmetric sea would be allowed and the filling would exist (block 78 N1, route 1).

7. **PROVED + CHECKED (B3).** With every site occupied, every term of the generator moves a record onto an occupied site, so `PHP = a₀N·1`. For the same reason `⟨c†_x c_y⟩ = 0` for `x ≠ y`, and `n(k) = N_s^{-1} Σ_x ⟨n_x⟩ = 1`. Checked on the `4×3` torus: 4096 states, no moves, the off-site elements exactly zero, `n(k) = 1` at all 12 `k`. The `4×4` torus with 16 records has no moves.

8. **CHECKED (B4).** The many-record generator in `manyrec.py` equals, entry by entry, an independent construction (mode tuples, Jordan–Wigner signs) on the `3×3` torus, for 1–3 records and both signs. It also reproduces block 78's `4×4` two-record traces: `28/15` for either sign; `119/15` and `39/5` at fourth order.
   - In scratch, not in `check.py`: the same equality held for 4 records on `3×3` and for 11 and 12 records on `4×3`, including the one-body density matrices of random states.

9. **NUMERIC (B5).** 14 records on the `4×4` slice, `a₀ = 0`. The generator is compressed to the hard-core space (`C(16,14)·2^14 = 1 966 080` states); ARPACK finds the lowest four states; the one-body density matrix is averaged over the ground manifold. The run's numbers are in section 3.

10. **NUMERIC (B6).** One hole (15 records, 524 288 states), `a = 1/8`, both signs. The costs of the 15th record, `E₀(15) − E₀(14)`, and of the last two, `(E₀(16) − E₀(14))/2` (with `E₀(16) = a₀N = 0`), are both compared with `4a`.
    - The run gives `E₀(15) = −1.824052` for either sign, and costs of `1.490` and `1.657` (antisymmetric) and `1.596` and `1.710` (symmetric), against `4a = 0.5`.
    - This bounds the grand-canonical record number from above by 14 for every chemical potential in the free top gap.
    - `N*` itself would need `E₀(N)` for `N ≤ 13`.

## 3. Where this stops

- **The lens's route fails at step 6.** A Fermi level between the top two levels needs more records than sites. Under the Record axiom's exclusion no many-record state has that filling. This is exact and holds for either exchange sign.
- **The middle 3D gap** is the jam on the `4³` torus (step 7): no content at all.
- **The mirror route fails at step 9, executed only.** In the bottom gap, the free sea's one filled species (`(π,π)`) and three empty ones become, under exclusion, nearly equal occupations. They are ordered by level energy across both senses: no step marks a Fermi level between species.
  - Per-state occupations at the zeros `(π,π)/(π,0)/(0,0)`, against the free `1/0/0`:

    | Sign | `a = 1/8` | `a = 1/16` |
    |---|---|---|
    | antisymmetric (ground manifold two-fold) | `0.521/0.493/0.446` | `0.506/0.493/0.475` |
    | symmetric (ground state single) | `0.411/0.381/0.361` | `0.392/0.380/0.371` |

  - Every ground state is at crystal momentum `(π,π)`. The steps shrink by factors 2.0–2.6 when `a` halves.
  - The ground state lies in a dense low-lying spectrum: the next state is 0.009–0.023 above. This is expected for 14 nearly immobile coins with two holes. ARPACK's lowest vectors are closed under the slice's rotation and reflection, so the average covers the whole ground manifold. A first run without this closure caught only one of the antisymmetric pair, and the check failed on the rotation symmetry of `n(k)`.
- **Even the free comparator's content is never a net sense** (step 2). It is a partition of the species by level. "Chiral content at the Fermi level" in the lens's sense is the side above `μ` of that partition, and it exists only in the top gap and its mirror.

## 4. (c) What chiral content means for an interacting many-record state, and what would make it a theorem

**Free records.** Three readings exist, and they differ:
- **The Berry flux of the Fermi surfaces:** zero in total, always (step 2).
- **The partition by level:** `+1|−1`, `−2|+2`, `+1|−1`.
- **The cone chiral density:** filling-independent (step 4).

**Interacting records.**
- The momentum distribution is a density, not a sense. It shows a partition only if it has steps at the zeros, and on the `4×4` slice it has none of size.
- The usual interacting definition is the winding of the one-record Green function `G(ω, k)` of the many-record state on a surface around each zero. In 3D this is the `N₃` invariant, `(1/24π²)∮ tr(G dG⁻¹)³` (comparator: Volovik). It is quantised while `G` is nonsingular on the surface. Poles and zeros of `G` both carry it, and on the lattice its total vanishes (comparator: the Nielsen–Ninomiya argument extended to `G`; ASSUMED if used).
- By the same logic as step 2, the total is zero for interacting records too. At most a partition can be of one sense.

**What a theorem would need:**
1. **A composition rule:** the exchange sign, which the axioms do not supply (block 78), or a sign-free formulation of `G`.
2. **The thermodynamic limit of the hard-core problem** at a filling below one per site, with `G` nonsingular on the chosen surfaces. For hard-core records close to the jam, zeros of `G` are expected (the infinite-repulsion comparator), so the content can move from poles to zeros.
3. **A statement about the partition** (which zeros' windings sit at `ω = 0` on which side), since the total is zero.

**Also open:**
- *The grand-canonical reading, beyond the bound.* Step 10 gives `N* ≤ 14` at a chemical potential in the top gap. The value of `N*` and its content need the ground energies for `N ≤ 13`, with sectors up to 8.9 million states. Not done.
- *Tori beyond `4×4` and any 3D filling.* These are out of reach for exact diagonalisation.

## 5. Running it

```
python3 probes/work/derive/a-filled-level-of-one-sense-under-exclusion/w-jonathonsmac4f50-j3b8b/check.py
```

- It has 10 lines:
  - A1, A2, A4, B1, B2 are exact (sympy and integers);
  - B3 and B4 compare floating arrays for exact equality, built by two independent routes from the same entries; block 78's traces are at `a = 0`, where every entry is `±½` or `±i/2`;
  - A3, B5 and B6 are labelled NUMERIC.
- `manyrec.py` holds the many-record code.
- It runs in about 8.5 minutes, dominated by four ARPACK runs of 2 million states.
