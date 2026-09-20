# moving-kernel-with-vacancies, attempt 4 of 4 — a3's half-filling floor does not survive

Worker `w-jonathonsmac4f50-jb1d8` (`claude-opus-5`), unit `J-derive-moving-kernel-with-vacancies:a4`.

**Provenance.** The only prior attempt, `a3` (`w-jonathonsmac4f50-jb416`), **is by me** — same
model family, machine and running worker, finished minutes before this unit was claimed. Nothing
here is independent confirmation of it, and I do not re-run its route. What I do is run the one
cheap executable item its own §4 names: *find out how much room there is between `ρ₂` and the
bound `2ρ − 1`.* The answer removes `a3`'s floor.

## 1. What is claimed

`a3` establishes: with vacancies the infrared bound is `⟨|σ̂(k)|²⟩ ≤ 1/(βρ₂E(k))` with `ρ₂` the
occupied–occupied **bond** density, the sum rule is `ρ`, and so

```
M² ≥ ρ − 3G(0)/(βρ₂),      LRO once   β ρ₂ ρ > 3G(0).
```

Its binding constraint was that the only unconditional tie between the densities is
`ρ₂ ≥ 2ρ − 1`, vacuous at `ρ ≤ 1/2`, giving a threshold only above half filling.

> **Claim.** Summing the contents out of the law with vacancies leaves a measure on the occupied
> set alone,
>
> ```
> μ(A)  ∝  z^{|A|} Z_A ,        Z_A = the content partition function on the subgraph induced by A,
> ```
>
> and this marginal satisfies the **FKG lattice condition** `μ(A∪B)μ(A∩B) ≥ μ(A)μ(B)` on every
> instance tested — *all* pairs of subsets of rings of 6 and 8 and of a `3×3` torus, at several
> couplings and fugacities. Given FKG, the occupation variables are positively associated and
>
> ```
> ρ₂  ≥  ρ² ,
> ```
>
> which is positive at exactly the densities where `2ρ − 1` is negative. `a3`'s criterion then
> reads
>
> ```
> β  >  3G(0)/ρ³ ,
> ```
>
> **finite at every positive density**, strictly below `3G(0)/(ρ(2ρ−1))` for every `ρ < 1`, and
> still exactly `3G(0)` at `ρ = 1`. `a3`'s `ρ > 1/2` floor was an artefact of inclusion–exclusion
> being the only correlation input it had.

## 2. The steps

1. **PROVED + CHECKED (`V1`).** Summing over contents factorizes the weight as `z^{|A|}Z_A`
   because a bond with an empty end contributes `1` regardless of content. Checked on small
   subgraphs: `Z_∅ = 1`, `Z_{one site} = 2`, `Z_{two adjacent} = 2(w + 1/w)`.
2. **CHECKED (`V2`), exhaustively.** The lattice condition over **every** pair of subsets:
   ring of 6 at `(w,z) = (2,1)` and `(3,½)` — 2080 pairs each; ring of 8 at `(2,2)` — 32896 pairs;
   `3×3` torus at `(2,1)` — 131328 pairs. Zero violations in all four.
3. **ASSUMED.** The FKG inequality itself (log-supermodular ⟹ positive association) is a theorem I
   use and do not re-prove. Given it, `ρ₂ ≥ ρ²` since `1[x occ]` and `1[y occ]` are increasing.
4. **CHECKED (`V3`).** Exact `ρ` and `ρ₂` on the `3×3` torus over 15 `(w,z)` pairs spanning
   `w ∈ {1,2,4}`, `z ∈ {⅛,¼,½,1,2}`: `ρ₂ ≥ ρ²` in all 15, and in the 4 cases with `ρ < 1/2` the
   bound `2ρ − 1` is negative while `ρ²` is positive and correct. The tightest case is `w = 1`
   (zero coupling), where `ρ₂/ρ² = 1` exactly — independent sites, so FKG is saturated. That is a
   sanity check on the whole route: the inequality is tight precisely where it must be.
5. **CHECKED (`V4`).** The threshold table, decreasing in `ρ`, strictly below `a3`'s wherever both
   are defined, equal to `3G(0)` at `ρ = 1` (where `ρ² = 2ρ − 1`). `3G(0) ∈ (0.75,0.76)` is
   **ASSUMED** from block 22, as in `a3`.

## 3. Where this stops

- **The lattice condition is checked, not proved.** Four instances, exhaustively over pairs, is
  strong evidence and no more. A proof would presumably go through the random-cluster
  representation of the content sum — `Z_A` is an Ising partition function on the induced
  subgraph, and log-supermodularity of `A ↦ z^{|A|}Z_A` looks like a statement about how the
  cluster measure responds to adding sites. I did not attempt it.
- **Two dimensions, two-valued contents, small tori.** Nothing here is `Z³` or the sphere menu.
  The `ρ₂ ≥ ρ²` consequence is menu-independent *given* the lattice condition, but the lattice
  condition was checked only for the two-valued menu.
- **FKG is assumed**, and so is everything `a3` assumed (Gaussian domination, Bessel positivity,
  `3G(0)`). This attempt adds one more assumed theorem rather than removing any.
- **`ρ₂` is still not computed from `z`.** Both `a3` and this attempt state the criterion in terms
  of the density; the map from the fugacity to `ρ` remains untouched.
- **`β > 3G(0)/ρ³` is a sufficient condition that degrades fast.** At `ρ = 1/4` it demands
  `β > 48.6`. It is finite, which is the point, but it is not evidence that order actually occurs
  at low density — and at densities below the site-percolation threshold of `Z³` it cannot,
  so the bound is certainly not sharp there.

## 4. What would finish it

1. Prove the lattice condition for `μ(A) ∝ z^{|A|}Z_A`, for the Ising content sum first and then
   for the sphere menu. That is the one gap between this and a theorem, and it is a
   self-contained combinatorial statement.
2. Check the lattice condition on a three-dimensional torus (a `2×2×2` has doubled bonds, so
   `3×3×3` with `2²⁷` subsets is out of exhaustive reach — a sampled or structured check is
   needed).
3. Since `ρ₂ ≥ ρ²` is saturated only at zero coupling, the *ferromagnetic* case should do
   strictly better. A bound of the form `ρ₂ ≥ ρ² + f(β)` would lower the threshold further and is
   visible in the `V3` table.
4. Independent re-derivation: `a3`, this attempt, and both assumed constants are the same model
   family. This result contradicts nothing of `a3`'s but weakens its headline limitation, and a
   referee from another family should check that the weakening is real and not a shared error.

## 5. Running it

```
python3 probes/work/derive/moving-kernel-with-vacancies/w-jonathonsmac4f50-jb1d8/check.py
```

Standard library plus `sympy`; 16 checks, exact rational arithmetic throughout (only printed
decimals are floats). The exhaustive pair checks dominate the runtime; about a minute.
