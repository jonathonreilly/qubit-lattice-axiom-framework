# Lane RI, probe I2 (truncation): report

**Provenance.** Worker: Claude Opus 5.5 (same model family as the supervisor). Ran 16:22Z to about 16:55Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/I2/`

| Script | Output | What it does |
|---|---|---|
| `i2_fold.py` | `i2_fold.out` | (a) N-site cell = folded fine chain; band-resolved C1 residual and C3 anomaly against N; loop-weighted anomaly in d = 1 and d = 3 |
| `i2_poincare_exact.py` | `i2_poincare_exact.out` | (a) Coarse-cell Poincaré generators against fine ones, in exact dyadic arithmetic; the cell-local improvement |
| `i2_sumrule.py` | `i2_sumrule.out` | (b) Sum rules on random N-band networks; C1's two-band network shown to be a folded fine chain; optimized N-band towers |
| `i2_umklapp.py` | `i2_umklapp.out` | (iii) Tower umklapp: on-shell, thermal and vacuum-loop fractions; networks without the Z_N label |
| `i2_nstar.py` | `i2_nstar.out` | Readout Q-RI |

Units: coarse cell a = 1, c = 1 in the IR, target β = c² = 1. The tower is E_n(k) = √(m² + K²), with lifted (tower) momentum K = k + 2πn.

## Bottom line

**Yes: N-band truncation is a finer lattice with spacing a/N.** It is not merely like one.
- **(a)** The N-site cell is exactly the fine lattice, folded. That holds for the spectrum and, after a cell-local improvement of the energy density, for the global Poincaré generators.
- **(b)** C1's face-touching two-band network is a folded fine chain with spacing a/2. Its face touching is just the folding. Generalized to N bands, the construction is a fine chain with spacing a/N and long-range fine hopping.
- **Every finite-N network** obeys two exact sum rules that stop the C1 and C3 obstructions from being removed. They can only be moved: to the fine zone face, i.e. the truncation edge.
  - C3: the zone-averaged boost anomaly is exactly −β per mode.
  - C1: the face residual summed over bands is at least πβN.
- **Tower-normal contact interactions** among the low bands need an internal Z_N (fine-translation) label. With that label the network *is* a fine lattice.

**So the "infinite-band network" is the continuum limit.** The exact tower needs N → ∞: infinitely many modes per cell and a continuous translation generator. That is the Lattice/Qubit price I1 names. At every finite N it is an ordinary lattice of spacing a/N:
- low-energy defects fall as (Ka/N)^{2r} (r = fine stencil range);
- in loops, the anomaly relative to the cutoff-scale natural size is independent of N (d = 3: −1.09 for the zero-point weight, −0.87 for the tadpole weight);
- the absolute vacuum anomaly per coarse cell grows like N⁴.

**Q-RI:**
- For the loop-level P0 bound there is **no finite N\***.
- For window-confined content only, N\* ≈ 2.6e24·(Ka) (quadratic response) or 9.4e48·(Ka) (linear response), with nearest-neighbour fine stencils (reading).

## Reading against the FIXED lines (lane RI; I2 is one probe)

- **PASS is not supported.** No finite-N network closes C1 + C3 (sum rules below). The only exact object is N = ∞.
- **I2 supplies the FAIL clause's "every finite-N truncation inexact" part.** Bounded to:
  - finite-component quadratic networks whose dynamical matrix W(k) (or h(k)) is periodic and C²;
  - the band-diagonal (conserved-momentum) sector of the C3 bracket and the C1 face residual.
- **I2 also gives evidence for I3's half of the FAIL clause.** The equivalence makes a coarse cell of N sites the same object as the folded tower. The loop-weighted relative anomaly is independent of N. Whether this fixes the induced TT response is I3's computation, not done here.
- **Lane verdict:** not mine to set. It needs I1 (exact closure ⇔ infinite DOF per cell) and I3 refereed.

## (a) N-site cells: literally a finer lattice

**Proposition E (PROVED; CHECKED).** An N-site cell with nearest-neighbour hopping, including the bond to the next cell, is the fine chain of spacing a/N, block-Bloch transformed.
- Its N×N dynamical matrix W(k) has eigenvalues ω²_fine(k + 2πn), n = 0…N−1.
- Check: max deviation / bandwidth ≤ 7.8e-16 for N = 2–32 (`i2_fold.out` (1)).
- Adjacent bands touch exactly at the coarse face and centre. The folding *is* a set of face touchings.

**Generators (PROVED; CHECKED exactly, `i2_poincare_exact.out`).**
- **Unimproved choice.** Take T(X) = Σ_{x∈X} t(x), K_c = Σ X·T(X), P_c = −{K_c, H}. Then P_c is not even conserved: max|{P_c,H}| = 47–100, against |P_f/N| = 10–28.
  - P_c − P_f/N is the time derivative of a bounded coarse-periodic total, so it is purely interband.
  - Its time average is ≤ 1e-3 of its rms (decreasing with averaging time).
- **Improved choice.** The cell-local improvement T′(X) = T(X) − [B(X) − B(X−1)], with B(X) = Σ_{x∈X}(δ(x)/N)t(x) and δ(x) the position of x inside its cell, gives exactly:
  - K′_c = K_f/N and P′_c = P_f/N;
  - residual 0.0 for N = 2, 4, 8 (dyadic, exact) and 1.2e-12 for N = 3 (1/3 is not dyadic).
- **Invariance (PROVED).** For a conserved, band-diagonal P, the band-diagonal symbol of {K,P} cannot be changed by any coarse-periodic improvement. The commutator [q(k), f(k)] of a k-local q with a band-diagonal f has zero diagonal.
- **Conclusion.** C3's refereed boost and rotation theorems apply verbatim to the network with a → a/N.

**Band-resolved scalings (CHECKED, `i2_fold.out` (2), (3)).** Nearest-neighbour fine stencil: f(K) = E∇E = N sin(K/N) and A(K) = Hess u − 1 = cos(K/N) − 1.

| Quantity | Lowest band n = 0 (\|K\| ≤ π) | Band n (n ≪ N) | Truncation edge \|K\| = πN | Zone average, all bands |
|---|---|---|---|---|
| C1 residual sup\|f − K\| | π − N sin(π/N) → π³/(6N²) = 5.17/N². N = 64: 1.26e-3; N = 1024: 4.93e-6 | ≈ ((2n+1)π)³/(6N²). N = 64: 3.40e-2 (n = 1), 0.157 (n = 2) | **= πN exactly** (relative 1.0000 for every N) | — |
| C3 boost anomaly \|A\| | ≤ (π/N)²/2. N = 64: 1.20e-3 | ≈ ((2n+1)π/N)²/2 | **−2 for every N** | **−1.000000 for every N** |
| Window \|K\| ≤ π/4, C1 residual | 7.9e-5 (N = 32), 7.7e-8 (N = 1024) | — | — | — |

Improved fine stencils of range r:
- the band-0 anomaly falls like N^{−2r}: at N = 64 it is 1.2e-3, 9.7e-7 and 7.6e-10 for r = 1, 2, 3;
- the edge value grows: −2, −2.6667, −3.2000, −3.6571 (the exact −2, −8/3, −16/5, −128/35);
- the zone average stays −1.0000.

The rotation sector was not computed separately. By Proposition E, C3's rotation theorem applies to the fine lattice as stated.

**Loop-weighted anomaly (CHECKED, `i2_fold.out` (4)).** Define R_s = Σ_modes A_x ω^s / Σ ω^s over the whole fine zone, i.e. all N^d bands. Graded quadrature.

| d = 3, N | 2 | 4 | 8 | 16 | 32 | 64 |
|---|---|---|---|---|---|---|
| R_1 (zero-point weight) | −1.087 | −1.091 | −1.092 | −1.092 | −1.092 | −1.092 |
| R_−1 (tadpole weight) | −0.890 | −0.880 | −0.876 | −0.875 | −0.874 | −0.874 |
| R_−3 (marginal) | −0.569 | −0.465 | −0.388 | −0.330 | −0.287 | −0.253 (~1/ln N) |
| R_−5 (IR-dominated) | −0.218 | −0.082 | −0.027 | −0.008 | −0.002 | −0.0007 (~N^−2) |
| Σ A_x ω/2 per coarse cell, divided by N⁴ | −1.328 | −1.310 | −1.305 | −1.304 | −1.303 | −1.303 |

In d = 1: R_1 → −4/3, and R_−1 falls only logarithmically.

Ultraviolet-weighted loop averages carry an O(1) relative anomaly that does not depend on N. The absolute vacuum anomaly per coarse cell grows like N^{d+1}.

## (b) Optimized N-band networks, and the sum rules that bind every N

**S1, Hessian sum rule (PROVED, short).** Let W(k) be an N×N periodic C² dynamical matrix (for fermions, use h(k)²), and u_n = λ_n/2. Then:
- Σ_n u_n = ½ tr W is periodic and C², so Σ_n ∫_BZ Hess u_n = ∫ Hess(½ tr W) = 0.
- This holds distributionally, crossings included. Kinks of individual sorted bands cancel in the sum.
- Hence, for every finite N, the band-summed, zone-averaged boost anomaly is Σ_n ⟨Hess u_n − β⟩ = −β per mode.
- CHECKED on random range-2 networks, N = 2–16: |⟨Σ_n u_n″⟩| ≤ 8e-13, against max u″ up to 1225 (`i2_sumrule.out` (A)).

**Multiband C3 corollary (PROVED given the band-diagonal reduction; the reduction is ARGUED).**
- The C3 closure requires P_tot to be conserved, so it is band-diagonal on nondegenerate bands.
- The band-diagonal part of {K_b, P_c} is then Hess(u_n)_bc × energy. Off-diagonal Berry-connection terms of K drop out of the diagonal.
- Closure therefore needs Hess u_n = M a.e., with one constant M shared by all bands, since C3's structure-function deformation multiplies the total H.
- S1 then gives N·M = 0, so M = 0: the Carroll contraction only.
- So C3's C-FAIL extends from one band to every finite-N periodic C² quadratic network in the band-diagonal sector. Interband conditions only add constraints.
- The tower escapes only because tr W = Σ_n(m² + K_n²) diverges (N = ∞). SLAC escapes because W is not periodic-C².

**S2, face sum rule (PROVED, short).**
- Σ_n f_n = ½∂_k tr W is continuous and periodic.
- Any N tower members assigned continuously on the open zone have Σ_n K_n = Nk + const, which jumps by 2πN across the face.
- So sup_k |Σ_n (f_n − βK_n)| ≥ πβN: the C1 face floor (πc² for N = 1) summed over bands.

**C1's two-band construction is a fine lattice with spacing a/2 (CHECKED spectrally; the unitary equivalence is ARGUED).**
- Its bands equal {ε(k), ε(k+2π)}, to 1.8e-15, of the single function ε(K) = D0(K) − 2cos(K/2)α(K).
- That function is smooth and 4π-periodic: Fourier coefficients 2.4e-10, 1.4e-13 and 4.5e-18 at orders 200, 400 and 800.
- The Fejér–Riesz phase of a(k) is analytic because α² ≥ 0.908 > 0, so a quasi-local cell unitary maps C1's h(k) onto the folded fine chain.
- **The "partner-band obstruction" C1 left open is the fine lattice's own face floor** (`i2_sumrule.out` (B)):
  - lowest band residual 5e-12;
  - at the fine face K = 2π, |f − K| = 6.2825 = πN with N = 2;
  - partner-band mean anomaly −2.000; total −1.000.

**Optimized N-band towers (CHECKED, `i2_sumrule.out` (C)).**
- **Construction.** A fine dispersion exactly equal to √(m² + K²) for |K| ≤ π(N − 1.8), glued smoothly to a flat even cap at the fine face, then Fourier-truncated to fine range R.
- **Low bands converge super-algebraically in R.** For N = 17 and R = 1088: band-0 energy error 3.4e-11, closure residual 2.2e-9; the band pair below the top 7.3e-8.
- **The top band pair n = ±(N−1)/2 carries the entire anomaly.**
  - Mean A = −N/2 each: −1.50, −2.50, −4.50, −8.50 for N = 3, 5, 9, 17.
  - min A ≈ −(4.3 to 4.7)N.
  - Edge residual = πN.

**The trade-off is fixed by S1 and S2.**
- Spreading the anomaly (nearest-neighbour fold) gives O(1) relative anomaly over the upper bands.
- Concentrating it (optimized) gives O(N) on the top pair.
- Neither reduces the total of −β per mode.

## (iii) Interband scattering at the truncation edge (contact interaction)

**Folded fine lattice, d = 2, fine-site φ⁴** (`i2_umklapp.out` (A)). Tower momentum is conserved mod 2πN. Tower umklapp is exactly fine umklapp.

**On-shell 2→2 umklapp fraction against E_in/E_max** (bins of 0.2; E_max = fine bandwidth ≈ 2√2·N):

| N | 0.4–0.6 | 0.6–0.8 | 0.8–1.0 | 1.0–1.2 | 1.2–1.4 | 1.4–1.6 |
|---|---|---|---|---|---|---|
| 4 | 0.000 | 0.000 | 0.073 | 0.263 | 0.475 | 0.533 |
| 8 | 0.000 | 0.005 | 0.086 | 0.265 | 0.478 | 0.534 |
| 16 | 0.000 | 0.003 | 0.100 | 0.254 | 0.491 | 0.534 |

The curves coincide in E/E_max, so the threshold scales with N.

**Thermal Γ_U/Γ:**
- At T = 2: 0.23 (N = 4), 3.0e-2 (N = 8), 7.7e-6 (N = 16). This is consistent with exp(−E_th/T) and E_th ≈ 2N in coarse units, read from the N = 8 → 16 ratio.
- At T ≳ N it is O(1).

**Vacuum loops (zone-averaged).** The fraction of momentum-conserving contact 4-tuples that are tower umklapp:
- flat measure: 1/3, 5/9, 19/27 in d = 1, 2, 3 (checked 0.334, 0.555, 0.704);
- basketball weight 1/(ω₁ω₂ω₃ω₄): 0.36–0.40 in d = 2 and 0.61–0.62 in d = 3;
- **both independent of N** (N = 4, 16, 64). In d = 1 the weighted fraction falls (IR-dominated).

**Networks without the Z_N label** (`i2_umklapp.out` (C)).
- With the exact fine translation, the low-band tower-umklapp vertex (bands (0,0) → (1,0), with a 2π mismatch at energies ~π/a) is machine zero (≤ 5e-15).
- Breaking the fine translation by random onsite terms of relative size δ switches it on linearly. Ratio to the normal vertex:
  - 8.6e-4, 7.5e-3, 0.107 at δ = 1e-3, 1e-2, 1e-1 (N = 4);
  - 5.2e-3, 6.3e-2, 0.30 at the same δ (N = 16).
- **ARGUED:** an N-band network whose contact interactions are tower-normal among its low bands must carry a conserved Z_N label that acts as a fine translation (T_f^N = T_coarse). Such a network is a lattice of spacing a/N.

## Scalings with N (summary)

| Diagnostic | Low-energy window (fixed Ka) | Whole zone, band-resolved | Truncation edge | Zone or loop average |
|---|---|---|---|---|
| C3 boost anomaly | (Ka/N)²/2; c_r(Ka/N)^{2r} | ((2n+1)π/N)²/2 on band n | −2 (NN), −8/3, …; −N/2 if concentrated | **−β per mode, every N (S1)**. UV loop weights −1.09 / −0.87 (d = 3), N-independent |
| C1 residual | (Ka)³/(6N²) | ((2n+1)π)³/(6N²) | πN (relative 1) | Σ over bands ≥ πβN (S2) |
| Tower umklapp | 0 below E_th ≈ 2N; thermal ~ e^{−E_th/T} | — | O(1) above 0.6–0.8 E_max | 0.62 of the d = 3 basketball phase space, N-independent |

## Readout Q-RI (READING; `i2_nstar.out`)

Assumptions:
- G3 design A: response quadratic in the defect, |A| ≤ √B; linear response |A| ≤ B.
- B = 5.7e-99 (refereed, reduced-Planck cell).
- Anomaly c_r(Ka/N)^{2r}.

| Fine stencil range r | N\*/(Ka), quadratic | N\*/(Ka), linear | N\* at Ka = π, quadratic |
|---|---|---|---|
| 1 (nearest neighbour) | 2.57e24 | 9.37e48 | 8.1e24 |
| 2 | 1.22e12 | 2.33e24 | 3.8e12 |
| 3 | 9.34e7 | 1.44e16 | 2.9e8 |
| 5 | 4.70e4 | 3.84e9 | 1.5e5 |

With B = 9.0e-102 these are about 1.4–5 times larger (quadratic). Larger r moves the defect to the edge (−2 → −128/35 …).

**For loop content** (lattice-scale modes up to the truncation edge, the binding case for P0):
- the mode-averaged anomaly is −β for every N (S1), and the UV-weighted loop averages are N-independent;
- so **N\* = ∞**: no finite N meets the P0-level bound without P0's own tuning;
- in coarse-cell natural units the absolute vacuum anomaly grows like N⁴.

## Against the supervisor expectation

**Expected:** a low-energy defect ∝ (ka/N)^p, staying order one at the truncation edge. **Confirmed, and sharpened:**
- p = 2r for folded fine stencils, and super-algebraic in hopping range for optimized towers.
- At the edge the anomaly is O(1) when spread, and O(N) when concentrated.

**Not foreseen:**
- exact sum rules (S1, S2) pin the total at −β per mode and πβN for every finite N, so the defect can only be moved;
- C1's face-touching two-band network is itself a folded fine lattice with spacing a/2;
- the C3 C-FAIL extends to every finite-N periodic C² network (band-diagonal sector);
- tower-normal interactions force the network to be a fine lattice.

## Labels

**PROVED (short; same family, unrefereed):**
- Proposition E (folding equivalence plus the cell-local improvement);
- invariance of the band-diagonal bracket symbol under coarse improvements;
- S1 and its multiband C3 corollary, given the ARGUED band-diagonal reduction;
- S2.

**CHECKED:**
- folding to 1e-15;
- exact generator identities;
- the scaling tables;
- the loop-weighted ratios;
- the sum rules on random networks;
- C1-two-band = folded chain (spectral, 1.8e-15);
- the optimized-tower tables;
- the umklapp fractions;
- the Z_N-breaking vertex.

**ARGUED:**
- the band-diagonal reduction of {K,P} for multiband networks (Berry terms);
- the quasi-local unitary for C1's two-band network;
- Z_N label ⇔ fine lattice.

**SUGGESTED:**
- that the UV-weighted loop anomaly is what drives the induced TT response (I3's job);
- E_th ≈ 2N (a two-point estimate).

**READING:** the N\* values and the axiom-cost reading.

**COMPARATORS:**
- C1 and C3 (refereed) results;
- the empty-lattice/folding construction (standard);
- the Kato–Sakamoto–So infinite-flavour escape, which this identifies with N → ∞.

## Scope and assumptions

- **What is covered.** Quadratic (free) scalar networks, with periodic C² W(k); the fermion version uses h². Gravity side as in C3 (09-14 stencils; regular structure functions).
- **What is not computed.**
  - Interacting dressing of the sum rules.
  - Gapless-dressed bands (lane RD).
  - Non-periodic or non-local W (SLAC).
  - The full interband part of the bracket for general networks.
  - Any TT-response number.
- **"Exact" is used only for:** algebraic identities, the exact-arithmetic checks, and the sum rules.
- **"No finite N\*"** is bounded to loop content under the stated scaling (relative anomaly → response).
