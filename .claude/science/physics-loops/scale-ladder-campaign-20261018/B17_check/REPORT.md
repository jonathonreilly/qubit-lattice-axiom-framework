# B17 check: anisotropic cone closure

Provenance: a fresh-context checker of the same model family; not independent in model lineage. It wrote its own code, by different routes. Saved by the supervisor from the hand-back.

| Runner | Result |
|---|---|
| `chk1_bracket.py` | PASS=12 |
| `chk2_step_cones.py` | PASS=10 FAIL=1; the FAIL is the claimed 0.5838 |
| `chk3_spectral_sym.py` | informational |
| B17 runner, re-run | PASS=4 |

First-run errors were the checker's own: the W/√2 normalisation, the fit normalisation and the node-search penalty.

## Verdicts

1. **Bracket: confirmed, and stronger.**
   - With a general constant triad E: [h_N, h_M] = −(ξ·∇ + ½ div ξ + spin), with ξ = gw and g = EᵀE.
   - The derivative part is −g^{kj}w_j∂_k. Closure for arbitrary lapses needs g = κI.
   - The spin part independently forces v_a = v_t.
   - **Loopholes, none of which rescue closure:**
     - density improvements, which leave the spin trace unchanged;
     - anisotropic relabelling, since one total constraint has one ξ;
     - a non-diagonal metric;
     - sector lapse rescaling, which gives only a scalar factor and is unavailable for a fixed step;
     - coordinate change or background strain, since the four metric classes are pairwise non-proportional;
     - another O-symmetric single-metric gravity sector, since g ∝ δ;
     - restricting to the ±k* valleys, since closure is an operator identity and the doublers share the quasi-energy.
2. **Step numerics: confirmed, using exact degenerate perturbation theory.**
   - All eight cube points carry an exactly 2-fold level at E = π/2, with no tilt.
   - The ±k* metric is (2/9)I to 1e−9.
   - The doublers are uniaxial: 0.2467203 axial and **0.5837466** transverse, with ratio 1 − 1/√3 to 2e−11.
   - Chiralities net zero.
   - No other crossing of E was found (20³ grid, 25 refinements).
   - **Addition:** a second eight-node set at −π/2 with identical cones. It is forced by spec W(k) = spec(−W(k)) and by conjugation closure.
3. **The Hamiltonian-coupling conditional: fair, with premises spelled out.**
   - **Premises:**
     - (a) local-lapse generators exist, whose leading form is a scalar-weighted energy density;
     - (b) lapses are smooth;
     - (c) there is one shared gravity sector;
     - (d) coupling is universal, doublers included.
   - The band-projected Floquet theory near E realises (a).
   - More generally, path-independent local-time evolution requires each species' cone metric to be the structure function (Teitelboim/Kuchař).
   - **The assumption-free core** is matter-sector Lorentz violation: the species' cones differ.
   - **Caveat:** the step is gapless away from ±π/2 (empty bins shrink toward ±π/2 by 32³). Do not assert a local Floquet Hamiltonian.
   - Timing schemes that are not path-independent make the test moot rather than passed.
   - **Codimension heuristic:** add the symmetry-enforced alternative (taste). The step has no such symmetry, because k → k + π(1,1,1) maps orbits of the same type.
4. **Walk passes, step fails: fair, with qualifications.**
   - The walk's equality comes from the invariance of Σ sin² k_j under k_j → k_j + π.
   - "Passes" means the leading cone test only. Six walk species need momentum-dependent spin structure (as in B15 O5b), and exact closure fails at O(a²).
   - The walk is outside the corner symmetry class.
   - The step's spin part was not tested.

## Corrections applied

- 0.5837, in the B17 findings and note item 6.
- The second node set.
- The runner-support pointers.
- The symmetry alternative.
- No Floquet Hamiltonian claim.
- The runner's `Ws` normalisation, now unitary (cosmetic; the runner still gives PASS=20).
