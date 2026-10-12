# C5 R14-1 report: do the box-route PASS results survive a subluminal box?

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 20:53Z to about 21:15Z. No repository file was edited. No downloads, no web lookups.

**Scratch.** `S/` = `.../scratchpad/C5/R14-1/`. Scripts and outputs are in `S/scripts/`. Each run took under 3 min at `OMP_NUM_THREADS=2`.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`).
- `TESTS.md`: the C5 method (`:2302-2320`); R7-1 (`:3242-3256`, verdict `:3398-3407`); R8-1/R8-2 (`:3445-3466`, verdicts `:3550-3557`, `:3795-3805`); R8-5 (`:3807-3812`); R9-2 (`:3643-3661`, verdict `:3889-3900`); R9-5 (`:3917-3923`); R9-6 (`:3769-3788`, verdict `:4016-4024`); R9-9's Theorem T (`:3945`); R11-4 (`:4192-4214`, verdict `:4425-4436`); the R13-4 worker entry (`:4767-4776`); R14-1 (`:4777-4800`).
- The `agents/` reports: `C5_R13-4_report.md` §3.3 (`:170-214`) and `C5_R8-2_report.md` §§3.1–3.4 (`:64-148`).
- The R13-4 referee files, which appeared during this run: `scratchpad/C5/ref_R13-4/REFEREE_VERDICT.md:9-21` and `R13-4_referee_verdict.md:146-160,207`. The referee confirms Lemma V.

**Labels.** proved (complete under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Every listed result survives with a subluminal box.** I re-ran each one with R13-4's subluminal box law at b = 1.4: zone-wide group velocity 0.993 in d = 3. That covers:
   - R7-1's free algebra;
   - R8-1's two-body algebra (d = 1 lattice, d = 2 lattice mass) and its leakage;
   - R9-2's fall of bound bodies;
   - R9-6's d = 3 triplet mass flatness;
   - R11-4's pole–dipole moments.

   The reason is simple (proved): every one of these results lives on states whose momenta stay inside the box. Changing the band outside the box changes nothing there. The only real requirement is that the box still contains the interaction's support. In d = 2 and d = 3 that forces one parameter down: the end of the transition shell, Π₂, drops from 1.2 to at most 0.99.
2. **What moves.**
   - Rapidity budgets fall by ln(2/1.4) = 0.357 (proton 45.40 → 45.04).
   - One-body boost leakage at fixed rapidity grows (η = 1: 5.8e-3 → 2.7e-2).
   - Shell sources at |P| = 0.7 grow about 7.5× because the shell is narrower.
   - The hopping kernel decays more slowly: 8.4e-8 vs 1.9e-9 at r = 128.
   - Every plateau number is unchanged.
3. **New problems.**
   - **(a) Exact doublers.** R13-4's subluminal symbol makes the energy repeat exactly under k → k + π on every axis (proved). The free lattice therefore splits into 2^d identical decoupled sublattices: seven exact relativistic copies of every particle in d = 3. In the box laws used so far the corner copies were only approximate.
   - **(b) The doublers are avoidable.** A gapped "even" band (the kind R8-2 already used) is subluminal for every box size b < π (proved) and has no light corners. R8-2's own gapped band at b = 2 is already subluminal (v_max = 0.9966, checked). So Lemma V's b*(m) bound applies only to odd-symbol laws, not to "every one-band box law" as TESTS paraphrases it.
   - **(c) The shear tuning was superluminal.** R9-2's edge tuning that cancelled the free shear sits on a superluminal edge (v_max = 1.59). Every subluminal edge I tried gives a nonzero, positive shear coefficient. This bites only the supplied zero-point completion; the actual empty vacuum still gives zero.
4. **A subluminal Wilson-box Dirac exists** (proved, with an explicit condition r ≤ 1/√d; checked). The price: its doublers are about 20× lighter than R8-5's (m + 0.095n vs m + 2n in lattice units at b = 1.4).

**Against the FIXED readings: PASS (worker reading).** The PASS is on the box domains the original results already claimed. Every changed number is stated below and checked. Nothing here enlarges the original scopes.

---

## 1. The laws used (FIXED: b ≤ 1.4, Gevrey step)

- **S(b), R13-4's odd symbol** (`S/scripts/sublum.py`, class `SymS`). The slope s′ is +1 on [0, b], falls by a Gevrey-2 step to −1 over [b, π−b], and stays −1 on [π−b, π]. Then ε = √(m² + Σ s(k_i)²).
  - It is tabulated by Gauss–Legendre plus cubic spline (error about 1e-15), not by R13-4's 2^16-point linear interpolation.
  - Checks: max|s − k| on the box is 4.4e-16; s(π) = 0.
- **G(b), a gapped even form** (`SymG`), used as a variant. The energy is ε² = m² + Σ h(k_i)², with h′ = 1 − sstep((|k| − b)/(π − b)), so h′ ∈ [0, 1] and h′ is flat zero at π. The momentum symbol is S's s, which matters only on the box.
- **Runner override.** `S/scripts/r81_common.py` is R8-1's module with `BoxLaw` replaced:
  - environment variables `LAWFORM` = S or G, and `LAWB` = 1.4;
  - the callers' B and B2 arguments are ignored;
  - the hard-coded leg masks `< 2.0` in the copied runners become `< LAWB`.

## 2. The restriction lemma (proved; it is why everything carries over)

**Statement.** Each listed result is an identity among H, P, K, J, X_P, D₁ and T^{μν}. The identity is evaluated on states whose one-body legs lie in the open box (or the inscribed ball, for rotations) with W supported there. On such states:
- ε = √(m² + k²) and s = k;
- the operator X = i∂_k preserves compact support.

So the identities involve the band only on the box, and any C^∞ band equal to √(m² + k²) on the box gives the same identities. This is the route the original verdicts used (`TESTS:3399-3400`).

**What has to be re-checked.** Three things:
- that the supports and plateaus fit in the smaller box;
- quasi-locality of the new symbol;
- the numbers that see the edge.

## 3. Results, item by item (all checked; files in `S/scripts/`)

| listed result | original | subluminal S(1.4) (G(1.4) where run) | file |
|---|---|---|---|
| **R7-1 P1**, in-box packet k₀ = (0.4, −0.3): [K,P]−iH, [K,H]−iP, [K_x,K_y]+iJ, [J,K]−iK | 4.8e-14, 4.1e-14, 1.7e-12, 6.1e-12 | 2.9e-14, 2.6e-14, 8.5e-13, 2.8e-12 | `r71_sub_free_b1.4.out` |
| R7-1, fast in-box packet | (1.4, 0.3): 1.6e-13 | (1.0, 0.3): 1.3e-9; set by the Gaussian tail beyond the box (weight 6.0e-7). Compact support gives 0 (§2) | same |
| R7-1 finite-boost leakage ‖U_lat − U_cont‖ (bound 2‖1_Eψ‖) at η = 0.5 / 1 / 1.5 / 2 | 1.3e-5 (1.9e-3) / 5.8e-3 (0.11) / 9.4e-2 (0.55) / 0.35 (1.09) | 8.7e-4 (4.5e-2) / 2.7e-2 (0.38) / 0.15 (0.93) / 0.38 (1.41): the bound holds at every η | same |
| **R8-1 d = 1 ring** (L = 1024), repaired K: [K,P]−iH / [K,H]−iP | 1.4e-7–2.4e-7 / 1.0e-6–1.1e-6 | S: 1.8e-8–1.4e-7 / 6.1e-7–8.4e-7; G: 1.8e-8–1.6e-7 / 6.1e-7–1.1e-6 | `r81_d1_ring_L1024_{S,G}.out` |
| R8-1 d = 1 invariant-mass plateau spread; hermiticity in the shell | 1.44e-13; 1.1e-14 | S: 1.43e-13; 6.2e-15. G: 1.44e-13 | same |
| **R8-1 d = 2** doublet mass plateau spread (L = 128; Π₂ 1.2 → 0.95) | 6.32e-7 | 6.32e-7, identical: plateau points only | `r81_d2_lattice_mass_L128_S.out` |
| R8-1 d = 2 chart algebra | refereed | b-independent (continuum chart, legs on plateau ≤ 1.14 < 1.4), so unchanged by §2. Not rerun | — |
| R8-1 interacting leakage theorem | refereed | chart-level, imports no lattice symbol. BT orbits stay in \|P\| < Π₁ = 0.6, so legs ≤ 0.742 < 1.4 | `r81_leak.out`: rerun output identical to R8-1's (diff empty); η* = 0.3674 |
| **R9-2** bound-body Eötvös η, binding fractions 0.05/0.15/0.30, at rest and moving | ≤ 5.64e-13 | S: ≤ 5.41e-13; G: ≤ 5.73e-13 | `r92_fall_d1_L1024_{S,G}.out` |
| R9-2 "free region" packet | P₀ = 1.6: w − 1 = 1.1e-13 to 2.0e-13 | P₀ = 1.6 now leaves the b = 1.4 box (legs 1.44): w − 1 = −2e-2 (an artefact of the box size). At P₀ = 1.3, σ = 0.03: w − 1 = −1.2e-7 to −3.9e-7 (packet tails in the narrowed window 1.2 < P < 1.55) | `r92_fall_d1_free13_L1024_S_free1.3.out` |
| **R9-6** d = 3 triplet invariant-mass plateau spread (Π₂ 1.2 → 0.95; legs < 1.4) | L = 96: 3.03e-6; L = 128: 2.49e-7 | S: 2.95e-6; 2.26e-7. G (L = 96): 2.95e-6 | `r96_d3_lattice_mass_L{96,128}_{S,G}_*.out` |
| **R11-4** pole–dipole moments, von Laue, Dixon comparison, P = 0 fibre | 0 / ≤ 5.7e-14 | bit-identical rerun: the closed form on the plateau bundle uses no band symbol; plateau legs ≤ 1.14 < 1.4 | `r114_copy/*.out` |
| R11-4 transition shell, ‖[h, J′_∥]b‖/E_b at \|P\| = 0.7 (M_b = 0.95/0.85/0.70) | 0.022/0.030/0.042 (Π₂ = 1.2) | 0.168/0.231/0.316 (Π₂ = 0.95). Binding is lost by \|P\| ≈ 0.8, not 0.9. Plateau rows unchanged (≈ 2e-12) | `r141_shell_Pi2_0.95.out` |

**The mirror-box packet** (R7-1 runner, k₀ = (2.9, 2.9)) shows the doubler's algebra:
- [K_x,P_x] + iH = 2.7e-14 and [K_x,H] + iP_x = 2.4e-14;
- [J,K_x] − iK_y = 2.2e-12.

So the corner copy carries an exact Poincaré algebra with boost −K, the parity image (checked).

## 4. Which numbers move (all checked)

- **Rapidity budgets at rest, a = ℓ_P, asinh(bE_P/m)** (`r141_symbols.out` (D)):

  | particle | b = 2.0 | b = 1.4 |
  |---|---|---|
  | electron | 52.91 | 52.56 |
  | proton | 45.40 | 45.04 |
  | top | 40.18 | 39.83 |

  - Every budget shifts by ln(2/1.4) = 0.357.
  - A 3e20 eV proton keeps 17.9, down from 18.2.
  - Toy one-body budgets (m = 0.5): 2.35 (b = 2.6) → 1.75 (b = 1.4).
- **Interaction plateau sizes** (`r141_domains.out`, `r141_geometry.out`). Worst leg is q ∥ P, m = 0.5.
  - **d = 1** (κ = 0.4, Π 0.6/1.2): max leg on supp W is 1.148 < 1.4. No change needed. The W-free window for legs < b shrinks to |P| < 1.546; it was 3.10 at b = 2.6.
  - **d = 2 and d = 3** (κ = 0.8):
    - Π₂ = 1.2 is not admissible: legs reach 1.548.
    - Legs stay in |k| < 1.4 only for |P| < 0.992, so I used Π₂ = 0.95 (legs ≤ 1.371).
    - At Π₁ = 0.6, κ ≤ 1.066.
    - Keeping Π₂ = 1.2 would need κ ≤ 0.644.
    - The plateau Π₁ = 0.6 and the plateau boost budgets asinh(Π₁/M_b) (0.596/0.658/0.777) are unchanged.
  - **R8-1's d = 2 lattice-native algebra runner** (κ = 1.0, Π 1.0/1.4: plateau legs 1.595) does not fit at b = 1.4. It was "not a precision check" (`TESTS:3800`) and was not rerun.
- **Leakage.** One-body: §3 table. Interacting (R8-1 Theorem L): unchanged, because it is set by Π₁.
- **Quasi-locality** (`r141_symbols.out` (C), d = 1 axis). The narrower S step (width π − 2b = 0.34, against 1.1) slows the kernel's decay:

  | law | r = 128 | r = 256 | r = 512 |
  |---|---|---|---|
  | R7-1 literal | 2.5e-9 | 1.3e-12 | 1.2e-16 |
  | S(1.4) | 9.6e-8 | 4.3e-10 | 6.7e-13 |
  | G(1.4) | 2.9e-14 | 1.7e-17 | — |

  The stretched-exponential fit gives β = 0.44, a = 0.97, against R7-1's β = 0.43, a = 2.68 (`r71_sub_free_b1.4.out` (B)). Still super-polynomial (checked to the 1e-12 level).

## 5. New problems from the subluminal step

**(a) Doublers: worse in S(b), absent in G(b).**
- **S(b) has exact doublers** (proved). σ = s′ is antisymmetric about π/2, so s(π − k) = s(k). With oddness this gives:
  - s(k + π) = −s(k);
  - ε(k + πe_i) = ε(k).
- **Consequences:**
  - ε is π-periodic on every axis. Its kernel vanishes on odd distances (checked: 1e-18), so H splits into 2^d decoupled sublattices.
  - The 2^d − 1 corner valleys are exact copies of the box: ε(πe_x + q) = √(m² + q²) for |q| ≤ b (checked to 1.3e-15).
  - In R7-1's literal band the corners are mass-m valleys with sin-dispersion (`C5_R8-2_report.md:64-70`).
- **Box-supported interactions never reach them**, as before. But any vertex reaching the corners (Peierls; R8-5 Lemma C, `TESTS:3808`) sees seven exact light copies.
- **G(b) has none** (proved, checked):
  - its corners sit at ε = 2.29/3.23/3.94 (b = 1.4, m = 0.3);
  - its edge minimum equals the face value √(m² + b²) = 1.432, which is R8-2's ceiling (`C5_R8-2_report.md:147`).

**(b) Lemma V's scope (proved; checked).** Lemma V's proof needs ε² = m² + Σ s(k_i)² with s odd and C¹. Then s(π) = 0 (`C5_R13-4_report.md:188-189`; referee `R13-4_referee_verdict.md:148`).

For the even form ε² = m² + Σ g(k_i) with g = h², h = k on the box and 0 ≤ h′ ≤ 1:

|∇ε|² = Σ h_i²h′_i²/(m² + Σ h_j²) < 1 for every b < π, every d and every m > 0 (proved).

Checked, for d = 3:

| law | v_max |
|---|---|
| G(1.4), m = 0.3 | 0.9938 |
| G(2.0), m = 0.3 | 0.9966 |
| G(2.6), m = 0.5 | 0.9941 |
| **R8-2's own gapped band** (b = 2, b₂ = 3.1), m = 0.3 | **0.9966**; d = 1: 0.9902 |

So "every one-band box law with b > b*(m) has v_max > 1" (`TESTS:4773,4780`) is broader than the proof. The correct scope is odd-symbol laws, which always carry mass-m corner valleys.

For number-conserving one-band matter (the R7-1/R8-1/R9-x laws), the subluminal step therefore does **not** force b < π/2. With a G(2.6) edge, R8-1, R9-2, R9-6 and R11-4 keep their original parameters, by §2. For Dirac matter, oddness is forced (§6), and the Wilson term pays instead.

**(c) A smaller box for interactions.** This applies only if S(b) with b < b*(m) is kept; see §4. In d = 2 and d = 3, Π₂ ≤ 0.99 at κ = 0.8. The shell sources grow about 7.5×.

**(d) Theorem E's edge share** (`r141_symbols.out` (B); Theorem E at `C5_R8-2_report.md:115-143`).
- **The zone mean of A = Hess(ε²/2) − I is −1 for every law** (checked to 1e-6; forced).
- **S(1.4):**
  - A ≠ 0 only on the transition slabs, 10.2% of each axis (R7-1: 74%);
  - A ∈ [−18.8, 0] (R7-1: [−33.0, +19.8]; the b = 2.6 law: [−370, +180]);
  - d = 3 edge means: −1.10 (plain), −1.41 (energy-weighted), −0.000 (low-T 0.1). The low-T population is the exact doublers, which have A = 0 and so fall universally.
- **G(1.4):** edge means −1.10 / −1.20 / −0.036.
- **Pointwise sign (proved).** A_xx = s′² − 1 + s s″ ≤ 0 for S, and h′² − 1 + h h″ ≤ 0 for G, because |s′|, h′ ≤ 1 and s s″, h h″ ≤ 0. So in these families every edge quantum falls with weight ≤ 1 (the "falling up" values are gone).
- **Consequence for R9-9's Theorem T** (`TESTS:3945`, which needs Ξ ∝ ⟨|V|²A_zz/ε⁵⟩). In the S and G families Ξ < 0 for every nonzero edge vertex. The positive literal-edge value came from a superluminal edge (proved within S/G; not a statement about all subluminal bands — A > 0 is possible for other subluminal profiles near the face; suggested).

**(e) Free shear: the tuning was superluminal (checked; the vacuum is conditional).** I used R9-2's closed form, R8-2's universal box ⊕ edge stress, a supplied zero-point vacuum, d = 3 and m = 1 (`r141_shear.out`, convergence in `r141_shear_extra.out`, N = 160/320/480).

| edge | μ_E |
|---|---|
| S(1.4) | +5.063e-3 |
| G(1.4) | +3.525e-3 |
| R8-2 gapped (subluminal) | +7.976e-3 |
| literal L | −0.2057 |

- The R9-2 root t* = 0.287922 of the family g_t = (1−t)g_L + t g_G has **v_max = 1.595**; at m = 0.3, t* = 0.2977 gives 1.746.
- The family is subluminal only for t ≳ 0.6, where μ_E > 0 (+3.1e-3 to +8.0e-3).
- So in that family the shear-cancelling edge is superluminal, and no tested subluminal edge cancels μ_E. Whether some subluminal edge does: open.
- In R8-2's actual empty vacuum μ_E = 0 for every edge, unchanged (`TESTS:3897`).

## 6. Is a subluminal Wilson-box Dirac possible? Yes (proved; checked)

**Why oddness is forced** (proved, elementary). The π-rotations about the coordinate axes are proper cubic rotations (`AX:37-38`). With spinor covariance they send (k_x, k_y, γ_x, γ_y) → (−k_x, −k_y, −γ_x, −γ_y). So the Dirac symbol s must be odd, hence s(π) = 0, so the corners are massless at W = 0 and a Wilson term W is needed.

**Construction D1(r)** (`r141_wilson.py`):
- s = S(b);
- W′ = r√(1 − s′²) on the slabs, W even and flat elsewhere;
- E² = (m + ΣW)² + Σ s².

**Theorem** (proved, Cauchy–Schwarz per component). (MW′_j + s_j s′_j)² ≤ (M²r² + s_j²)((W′_j/r)² + s′_j²) ≤ M²r² + s_j². Summing over j gives |∇E|² ≤ (d r²M² + Σ s²)/(M² + Σ s²) ≤ 1 whenever r ≤ 1/√d. On the box W = 0 and s = k, so E = √(m² + k²) exactly.

**Checked** (`r141_wilson.out`), b = 1.4, r = 1/√3:
- v_max in d = 3 is 0.9950 (m = 0.3) and ≤ 1.0000 (m = 0.1), on grid and lines;
- r = 1 and r = 0.7 exceed 1 slightly (up to 1.10 at b = 1.0, m = 0.3), as the theorem allows;
- the W kernel decays super-polynomially (2.3e-8 at r = 129; 4.9e-11 at r = 513).

**The cost: light doublers.** Corner masses are m + nW_π, with:

| b (r = 1/√3) | W_π |
|---|---|
| 1.4 | 0.095 |
| 1.2 | 0.207 |
| 1.0 | 0.318 |

R8-5's Wilson box (r = 1) has m + 2n.

- Within the sufficient-condition family, concavity gives W_π ≤ r√((π−b)² − b²) = 0.597 at b = 1.4, approached by a nearly constant s′ (proved for the family).
- Whether a subluminal Wilson box can gap the doublers to O(1)/a: open.
- R8-5's Ward no-go and cone split were not rerun. They are not on the R14-1 list.

## 7. Against the FIXED readings (`TESTS:4797-4800`)

**PASS (worker reading; referee required).** Each listed result holds with the subluminal box S(1.4), with the changed numbers stated (§§3–4) and checked:
- R7-1 P1;
- R8-1 (d = 1 algebra; d = 2 lattice mass; leakage by construction);
- R9-2;
- R9-6;
- R11-4.

The PASS is within the original scopes (PASS WITH SCOPE in each verdict). It adds nothing about N ≥ 3, pair creation, gauge fields, global quasi-local fluxes or self-consistent gravity.

**Answers to the item's questions.**
- **Does each conclusion carry over unchanged?** Yes on the box domain (§2).
- **Which numbers move?** §4.
- **Does the step create new problems?**
  - Exact doublers in S(b), avoidable with G(b).
  - A smaller interaction box, only if S(b) is kept.
  - An edge share concentrated on 10% slabs with A ≤ 0.
  - R9-2's shear tuning needing a superluminal edge (conditional vacuum).
- **Is a subluminal Wilson-box Dirac possible?** Yes, with doublers about 20× lighter.

The R13-4 referee's statement — R7-1, R8-1, R9-2, R9-5, R9-6 and R11-4 survive after replacing the edge and shrinking supports, while edge numbers do not transfer (`ref_R13-4/REFEREE_VERDICT.md:21`) — is consistent with this. R9-5 (qubit encoding) was not rerun and is not on the list. Reading: its Kitaev encoding takes any quasi-local free CAR hopping, so it should carry over (suggested).

## 8. Strong-word check

- **"Exact"** is used for:
  - the box identities (proved by restriction; checked to 1e-14 on in-box packets);
  - the doubler identities ε(k + πe_i) = ε(k), s(k + π) = −s(k) (proved; checked to 1e-15);
  - the mirror algebra with −K (checked to 2.7e-14).
- **"Proved"** is used for:
  - §2;
  - §5(a);
  - §5(b)'s G-form bound;
  - §5(d)'s pointwise sign in S/G;
  - §6's theorem and the oddness argument;
  - the §6 family bound on W_π.
- **"Checked"** is used for all tables. Grids:
  - d = 3 group velocities on a 160³ grid plus axis/diagonal lines;
  - lattice runs at the stated L;
  - μ_E converged at N = 320/480.
- **Not claimed:**
  - "every subluminal box" (FAIL-type class statements);
  - that μ_E ≠ 0 for every subluminal edge;
  - a necessary bound on the Wilson doubler gap;
  - R8-5/R9-5 reruns;
  - certified (interval) bounds.
- **Naming.** "Lemma V" also names R6-3's count-variance lemma (`TESTS:3106`). The box lemma is R13-4 (iii).

## 9. For the referee

1. **§2's restriction lemma.** Is every identity in the five results evaluated only on box-supported states? Watch the R9-2 stress, whose Construction A part is whole-zone but whose box-state matrix elements see only box values.
2. **§5(b).** The G-form velocity bound, and whether TESTS:4773/4780 should be re-scoped to odd-symbol laws.
3. **§5(a).** The π-periodicity of S(b)'s ε, and its consequence (decoupled sublattices).
4. **§6.** The Cauchy–Schwarz step, and the claim that π-rotation covariance forces odd s for the Dirac symbol.
5. **§5(e).** The v_max of g_t at t*.
6. **R8-1 leakage** (`r81_leak.out`). It is chart-level and imports no box symbol. The rerun in `S/scripts/` is byte-identical to R8-1's `r81_leak.out`.

**Files.** All in `S/scripts/`:
- `sublum.py`, `r81_common.py` (override), `r141_symbols.{py,out}`, `r141_wilson.{py,out}`, `r141_domains.{py,out}`, `r141_geometry.{py,out}`, `r141_shell.py` + `r141_shell_Pi2_0.95.out`, `r141_shear.{py,out}`, `r141_shear_extra.{py,out}`;
- `r71_sub_free.py` + `r71_sub_free_b1.4.out`;
- `r81_d1_ring.py` + `_L1024_{S,G}.out`, `r81_d2_lattice_mass.py` + `_L128_S.out`, `r81_leak.py` + `r81_leak.out`;
- `r92_fall_d1.py` + `_L1024_{S,G}.out`, `r92_fall_d1_free13.py` + `.out`;
- `r96_d3_lattice_mass.py` + `_L{96,128}_*.out`;
- `r114_copy/` (the R11-4 closed-form reruns);
- `*.log`.
