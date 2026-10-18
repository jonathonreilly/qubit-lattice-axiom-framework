# B18 findings: taste symmetry and isotropic doublers

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. The runners exec the scratchpad `qca/walklib.py` (and `c20/diraclib.py`) read-only through `b18lib.py`.

| Runner | Part | Result |
|---|---|---|
| `taste_obstruction.py` | 1 | PASS=10 (759 s) |
| `taste_symmetric_steps.py` | 2 | PASS=4 (608 s) |
| `partner_nodes.py` | 2 | PASS=3 |
| `doubler_iso_scan.py` | 3 | PASS=4 |

**Bottom line.**
- No taste relates k* to its doublers in the eight-node step.
- No tested step has every species isotropic at one speed.
- Taste-symmetric steps with isotropic spin-½ Weyl nodes exist (words in S²), but they carry other, anisotropic nodes at the same quasi-energy.

## 1. Taste unitaries T = (−1)^{e·x} V(k)

Here a taste is an invertible V with V X(k) = ω X(k+πe) V.

- **S has no taste except e = (1,1,1), which maps k* → −k* (exact).**
  - S(k) = diag(σ_c e^{ik·f_c}) over 12 distinct face diagonals, so V is diagonal and ω = (−1)^{e·f_c} for every c.
  - This covers continuous V(k) and antiunitaries.
- **H_link has tastes for every e, with ω = ±1.** The tastes form a 3-dimensional diagonal family of corner-plane signs, and they commute (Z2³, not Clifford). The reason is that H_link keeps each corner in its plane.
- **H_on, Λ and their projectors have only the trivial taste.** S² has both kinds.
- **No joint taste.** No on-site V intertwines H_link and also commutes with H_on, or commutes or anticommutes with Λ. Range-1 V(k) is also excluded for e_x with ω = +1.
- **Normaliser obstruction (exact).** |Stab(k*)| = 24 but |Stab(k*+πe_x)| = 8, so no operator normalising PSG + translations maps k* to k*+πe_x. A taste must enlarge the group. In the enlarged group, isotropy at the doubler would be forced.
- **Step-level obstruction (c3; computed for 14 α choices, not proved for all).**
  - An operator commuting with the PSG rotations and with one H_link-type T_x acquires extra on-site symmetries at k*. These cut the commutant to two 6-fold blocks.
  - So such an operator has no spin-½ doublet at k*.
- **The trivial taste (−1)^{x_i}** forces W(k+πe) = W(k), so the sublattices decouple.
- **The eight-node step has no taste of any form.**
  - The spectra under k → ±k+πe_x differ by up to 0.70 rad.
  - The velocity determinants differ: v*³ = 0.104757 at ±k*, against v_ax v_tr² = 0.084072 at the doublers. This excludes every translation-covariant unitary or antiunitary with momentum map k → Mk+πe, M ∈ GL(3,Z).
- **Whole B1 family.** Of 6,384 Clifford-phase steps, 29 have a genuine on-site taste. None of those 29 has a Weyl doublet at k*. This used a necessary spectral screen.
- **Chirality lemma (standard).** A unitary taste with linear part L preserves chirality iff det L > 0. So (−1)^x-type tastes give same-chirality copies.

## 2. Taste-symmetric steps

- **Words in S^{±2} and R_L** split into the three corner-plane sectors. They have no point nodes, and their multiplicities at k* are multiples of 6.
- **17,056 words in S^{±2} with on-site factors.** These are exactly invariant under T_i = (−1)^{x_i} and under k → k+(π/2)(1,1,1); they amount to 16 decoupled sublattices.
  - 10,620 (word, level) pairs have spin-½ Weyl at k*. All are isotropic at √2/3 per application of S, identically at 16 points.
  - **None is clean.** Exact crossings (7.7e−13) occur at X-type points.
- **Census of S2.H20.S2.L202 at E = −π.**
  - X points: isotropic at the same speed. This is unexplained.
  - 24 points of type (π/4)(1,1,0): anisotropic, speeds 1.58–2.47.
  - Every sampled node class has Berry flux +1. That is consistent with an anomalous gapless Floquet step; a gap was not checked.
- So the taste makes its copies isotropic, but other species remain anisotropic, and B17's condition fails.

## 3. Doublers in the B1 families (refined)

- **Scope.** 6,384 steps with 7,266 k* Weyl nodes, all isotropic at √2/3.
  - 1,872 have uniaxial doublers at ±k*+πe_x.
  - 252 have doublets that are not linear cones.
- **Eleven distinct (v_ax, v_tr) pairs,** for example (√2/8, 3√2/16), (0.2467, 0.5837) and (sin15°, cos15°/2).
- **Closest to the k* speed:** (2√2/5, 3√2/10), with score 0.1414.
- **Accidental isotropy.** 384 S·U records (no R_L) have isotropic doublers, but at the wrong speed, √2/5 = (3/5)v*. These steps are also unclean.

## Status

- **Exact:** the S theorem, the H_link plane structure, the normaliser obstruction, the chirality lemma, and the family symmetries.
- **Finite exact linear algebra:** the intertwiners and c3.
- **Refined numerics:** speeds, determinants, fluxes and cleanliness.
- **Open:** non-diagonal or longer-range V, and new non-symmetric layers. The search results are negative findings, not no-gos.

## Prior art

- Karsten–Smit 1981 (the naive doubling symmetry relates opposite chiralities in 4-component Dirac).
- Kogut–Susskind 1975; Golterman–Smit 1984 (Clifford taste group).
- Minimally doubled fermions: Karsten 1981, Wilczek 1987, Creutz, Boriçi 2008, with anisotropy counterterms (Capitani et al. 2010). This parallels the D4 doublers here.
- Nielsen–Ninomiya 1981. Floquet net chirality: Higashikawa–Nakagawa–Ueda 2019, unverified.
