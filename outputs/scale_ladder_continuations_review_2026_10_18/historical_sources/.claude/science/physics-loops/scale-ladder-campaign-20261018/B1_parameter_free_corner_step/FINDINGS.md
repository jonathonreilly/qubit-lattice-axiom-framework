# B1 findings: parameter-free corner step rules (main agent, in progress)

## Exact facts (runner Part 6 and these scripts)

- **Link hopping.** H_link(k)² = 2 at every k in infinite volume, so R_L = H_link/√2 is an exact local reflection. The chiral link orbits Tb1 and Tb2 square to 2 only on the L=4 torus; that is an artefact.
- **Walk R_L(1−2P₂).**
  - The node at k* is 6-fold, G3/2 + E1/2.
  - Four bands leave at ±|q|/√3, each 2-fold; two bands are exactly flat (forced by a dimension count).
  - This is the spin-1 ⊗ spin-½ type.
- **Lemma.** Symmetric factors with a k-independent spectrum give zero velocity to every spin-½ doublet at k*. The large Clifford-phase searches (about 16k + 4k walks) found no Weyl doublet, as the lemma predicts.
- **Diagonal shift S.** The map {d,e}@v → {d,e}@(v+d+e) is a gauge-consistent, symmetric signed permutation (`shift.py`, `S_110_0.npy`). It is exactly unitary, and its spectrum depends on k, so it escapes the lemma.
- **Shift walks.** 3738 walks of the form S·U, S·R_L·U or R_L·S·U (U a Clifford-phase on-site step) have Weyl doublets at k*.
  - The speed is √2/3 (0.4714045), isotropic, with anisotropy ∝ q².
  - Example S·(1−2Q_top): Berry flux +1 at both k* and −k*, but pinned 2-fold lines at quasi-energy π cross the zone.
  - Example S·R_L·(H23·L110): node at −π/2.
    - Weyl doublets at all 8 points (π/2)(±1,±1,±1).
    - At ±k* they are isotropic, speed √2/3, chiralities ±1.
    - At the other 6 they are anisotropic (spread about 0.3), chiralities ±1; the net is 0.
    - Nothing else reaches −π/2 (refined search).
- **Running:** `cube_scan.py`, looking for candidates whose node quasi-energy is reached only at ±k*.

## Final search result (03:45Z)

- `cube_scan.py`: 4,476 node/step combinations have no level at the node quasi-energy at the other cube or high-symmetry points.
- `clean_rank2.py`: all of those have other crossings. The best minimum distance on a 12³ grid away from ±k* is 0.007.
- So in this family a clean node quasi-energy comes only with the six cube-point doublers (example: S·R_L·H23·L110).
- The independent check (B1_check) confirmed (a)–(c) with corrections, which are applied in the note: the lemma needs isolated doublets, the strengthening to a derivation, H_link² = 2 proved, the speed exactly 1/√3 via M³ = (|q|²/3)M, and the minimal Weyl automaton's maximum group speed 1/√2.

## π/6-phase extension (04:40Z)

- **Scope.** `pi6_search.py` uses on-site phases e^{iπn/6} (canonical C3/C6 angles) with S and S·R_L links.
- **Coarse result.** 5,349 Weyl-at-k* steps have no cube-point doublers. The best far-grid distance on an 8³ grid is 0.08, for S·R_L·(P₀ + iP₁ − iP₂).
- **Refined result.** Refined minimization (`refine_H39.py`) finds about 60 crossings at the node quasi-energy, so it is not clean. The coarse-grid rankings are not reliable for cleanliness.
- **Conclusion.** No doubler-free clean Weyl step was found in the searched families. The only clean structure seen is the eight-node one.

## Random word search (05:10Z)

`word_search.py` tried 120,730 random words of length 2–4 in S, S⁻¹, R_L and Clifford-phase on-site factors. There were 158 hits passing the coarse filter: Weyl at k*, no level at the node quasi-energy at the other cube points, and an 8³-grid gap of at least 0.05. All 158 have the same coarse value, 0.0813. They are cyclic or conjugate forms of the S·R_L·(P₀ + iP₁ − iP₂) family, which the refined search (`refine_H39.py`) shows is not clean.

## Non-Clifford canonical on-site steps (05:20Z)

- **Search** (`expH_search.py`). On-site steps exp(±iπH_on/n), exp(±iπΛ/(n√2)) and exp(±iπ(H_on+Λ)/n) for n = 1…8, with S and S·R_L links, give 264 Weyl-at-k* steps.
- **Best candidate.** S·R_L·exp(iπH_on/6), with node at π/3, no level at the other cube points (distance 0.23), and a refined distance of 0.009 after the first pass.
- **Dense check** (`dense_check.py`, 32³ grid plus 80 refinements). It finds exact crossings elsewhere, so this candidate is not clean either.
- **B1 conclusion.** No doubler-free clean parameter-free Weyl step exists in any searched family: Clifford phases, π/6 phases, random words, or exp(iπH/n) coins. The six cube-point doublers are the only clean structure found. Not a no-go.
