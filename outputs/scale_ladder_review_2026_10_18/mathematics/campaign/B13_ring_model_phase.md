> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B13 findings: the ring model is the cubic spin-½ U(1) quantum link model; sign-free QMC stiffness up to 8³



## 1. Model identity

- **Mapping.** H = V·N_f − J·Σ flips, with an exact Gauss law and no charges, equals the spin-½ U(1) quantum link model −J Σ(U+U†) + λ Σ(U+U†)², with λ = V.
- **Configurations.** "Cubic ice": 3 in / 3 out at every vertex.
- **Neighbouring models.** The cubic quantum dimer model is a different background-charge sector. Pyrochlore quantum ice applies only by analogy.

## 2. Literature

- **Direct.**
  - Banerjee, Huffman and Rammelmüller, PRR 4, 033174 (2022), arXiv:2201.07171: ED on (3+1)D tubes plus finite-size scaling, proposing a Coulomb phase.
  - Chandrasekharan, hep-lat/9809084: a Coulomb phase at large finite spin j.
- **By analogy.** Hermele–Fisher–Balents 2004 (pyrochlore); Shannon et al. arXiv:1105.4196 (pyrochlore QMC; window not confirmed); Sikora et al. (diamond dimers); the cubic dimer model's Coulomb phase next to the RK point.
- **Gap.** No QMC phase diagram against V was found for cubic ice.

## 3. Sign problem

- The model is stoquastic. The sign of J is a gauge choice on even tori, via link signs whose product is −1 per plaquette.
- An imaginary source stays sign-free; a real source brings signs back.

## 4. QMC

- **Local world-line updates freeze the winding.** Negative control: 0.02 against the exact 0.285 on 2³.
- **Diffusion MC** with a uniform (RK) guide and forward walking. The estimator ⟨M_c(τ)²⟩ = A + χτ uses E₀(iη) = E₀ − χη²/2.
- **2³ validation, 32/32:**
  - curvature 0.2833(21) against 0.28505 (V=1);
  - staggered 0.1056(9) against 0.10512;
  - winding energies −7.3956(17) against −7.399111, and −5.6574(14) against −4√2.
- **Harmonic curvature χ_h:**

  | V | L=2 (exact) | L=4 | L=6 | L=8 |
  |---|---|---|---|---|
  | 1 | 0.285 | 0.2347(6) | 0.2301(6) | 0.2293(6) |
  | 0.75 | 0.290 | 0.2445(17) | 0.247(4) | – |
  | 0.5 | 0.288 | 0.242(4) | 0.234(9) | 0.228(26) |
  | 0 | 0.267 | 0.115(12) | 0.220(23) | 0.226(33) |
  | −0.5 | 0.219 | 0.025(8) | 0.211(31) | 0.268(41) |

- **Small-q check.** The curvature at q = 2π/L is close to χ_h at L = 6 and 8.
- **Energy check.** The 4³ energy at V=0 is −0.29288 per plaquette, against the repo projector's −0.2926.

## Caveats

- Population bias is uncontrolled: 7e−4 per plaquette between walker counts at 6³, V=0.
- Errors are 10–15% for V ≤ 0.5 at L ≥ 6.
- The L=4 dip at V ≤ 0 is unexplained.
- A finite curvature at V=1 is expected: at RK the electric coupling vanishes, not the magnetic stiffness.

## What the lane can claim

- **Can:** the model identity; that it is sign-free; and that on 4³–8³ the magnetic-source curvature stays near 0.23–0.25 for V = 0.5–1, with no resolved size dependence among those finite samples; this is not uniform size independence or an infinite-volume limit. The V = 0.5 values were confirmed bias-controlled by the check, using a second (twisted-energy) estimator.
- **Withdrawn after the check (`../B13_check/REPORT.md`):** "no decay at V ≤ 0 for L = 6–8". Population bias is uncontrolled there, and the two estimators disagree at L=6, V=−0.5. The L=4 suppression at V ≤ 0 is real and deepens with N, so it may be confinement-like.
- **Cannot:** an infinite-volume Coulomb phase, its window in V, or confinement.
