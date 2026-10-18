# B20 findings: no step reaches its node quasi-energy only at isotropic one-speed cones

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. It agrees with the B18 check's corrections, but that is same-family agreement.

| Runner | Result |
|---|---|
| `x_point_taste.py` | PASS=12 |
| `kstar_velocity_lemma.py` | PASS=7 |
| `winding_chirality.py` | PASS=6 |
| `fixed_points.py` | PASS=6 |
| `screen_words.py` | 6 runs × PASS=3 |
| `continuous_taste_opt.py` | PASS=2 (control) |

## 1. X-point isotropy (exact)

- S² = diag(e^{2ik·f_c}), and S²(k + (π/2)e_i) = S²(k)·Z_i, with Z_i the corner-plane signs.
- For W = S²·A·S²·B: Z_i W(k) Z_i = W(k + (π/2)e_i) iff [B, Z_i] = 0.
- With Y = diag((−1)^{f_c·(1,1,1)/2}): Y W Y = −W(k + (π/4)(1,1,1)) iff {B, Y} = 0.
- L202 = 1 − 2P_pl is plane-block-diagonal, so it qualifies for both.
- So the X nodes are exact taste copies of the k = 0 node. The (π/4)(1,1,1) nodes are copies of the E + π doublet, with opposite chirality.
- **Census of S2.H20.S2.L202 at E = −π, per (π/2)-cube:**
  - 2 isotropic nodes (1.885618) of opposite chirality;
  - 3 uniaxial nodes (2.49426, 1.581297, 1.581297) at (π/4)e_i, chirality +1;
  - 3 uniaxial nodes at (π/4)(1,1,0), chirality −1.

  Net chirality is 0. A Lipschitz certificate excludes other crossings outside 0.03-balls.

## 2. Lemmas

- **L1 (exact).** For any word in S^{±1}, S^{±2}, R_L and symmetric on-site unitaries, every 2-fold level at ±k* has speed |n_S|·√2/3 and chirality sign(n_S)·ε_D. Here n_S is the total power of S, and ε is ±1 for E1/2 and E5/2. This explains "√2/3 per S" (1,200 random checks, error 7e−13).
- **L2 (exact).** D₊ = {H_on = 2, Λ = −2√2} has ε = +1, and D₋ has ε = −1. R_L acts as (∓1, ±1) at ±k*. The net chirality from ±k* at E vanishes iff n_R is odd and the on-site scalar products on D₊ and D₋ are equal (400 random checks). The eight-node step satisfies this.
- **L3.** The 3D winding W₃ is additive and vanishes for every letter (diagonal phases, constants, reflections), so W₃ = 0 for every word. By the Floquet Nielsen–Ninomiya theorem (Bessho–Sato 2021; proof sketch only), the net chirality at any point-node quasi-energy is 0. A control with W₃ = −1 discriminates. So "anomalous" steps do not occur in this class.
- **L4 (exhaustive on (π/8)Z³).** A linear cone is forced isotropic only if its little group's rotation parts contain T.

  | Translation group | T-fixed points |
  |---|---|
  | 2πZ³ | ±k* |
  | + π(1,1,1) | k* only |
  | (π/2)Z³ (S² Z-tastes) | {0, (π/4)(1,1,1)} |
  | πZ³ (S·A·S·L202) | {0, (π/2)(1,1,1)} |

  The cube doublers, X_r and M_r all have D4 little groups.
- **Conditional obstruction (via L3).** If the T-fixed nodes at E have nonzero net chirality, E must also be reached at a point where isotropy is not forced.
  - Basic-translation words are excluded unless n_R is odd and λ₊ = λ₋.
  - Words without R_L are always excluded, unless a Y-type taste supplies the opposite chirality.

## 3. Search

- **Scope.** 92,512 parameter-free words up to 6 letters, giving 69,894 (word, E) pairs with a linear k* Weyl doublet. Clifford one- and two-slot skeletons, π/6 phases, and a taste family.
- **Fermi-surface test.** r(k) = det(W − e^{iE})/(e^{6iE}√det W) is real. A sign change on a 16³ grid proves E is reached on a surface.
- **Result.** 99.1% of pairs have a band crossing E. The other 648 each have an anisotropic node, or an isotropic node at another speed, exactly at E. **Passing candidates: 0.**
- **Obstruction pattern.**
  - R_L words: uniaxial cube doublers.
  - Taste words: all T-fixed nodes are isotropic at v* and their chiralities cancel. The only remaining obstruction is the D4 points X_r and M_r, with doublets pinned at E and uniaxial (ratios such as (0.839, 1.323)).
- **Continuous-phase control (not parameter-free).** Generic phases move the D4 doublets off E but create Fermi pockets. The best minimum grid distance was 0.061, with no point certified clean. So the observed rule is "pinned uniaxial node or pocket"; there is no counting proof.

## Status

- **Exact:** the X/Y tastes, L1, L2, W₃ = 0, and the T-fixed sets.
- **Conditional:** net chirality = W₃ (Bessho–Sato).
- **Numerical:** speeds and certificates.
- **Negative search, not a no-go.** Open:
  - whether E must be reached near X_r/M_r in the taste family;
  - steps whose taste group makes X_r or M_r T-fixed (the most promising route).

## Prior art

- Bessho–Sato, PRL 127, 196404 (2021), checked at abstract level.
- Unverified: Higashikawa–Nakagawa–Ueda 2019; Rudner–Lindner–Berg–Levin 2013; Kitagawa et al. 2010; Nielsen–Ninomiya 1981; Kogut–Susskind; Golterman–Smit; Wen 2002; Kluberg-Stern et al. 1983; van den Doel–Smit 1983; Bedaque et al. 2008.
