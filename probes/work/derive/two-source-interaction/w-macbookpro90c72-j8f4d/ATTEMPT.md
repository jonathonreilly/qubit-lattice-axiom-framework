# two-source-interaction, attempt 4 (worker w-macbookpro90c72-j8f4d, model grok-4.6)

Plan formed before reading other attempts: treat the *linear* (Gaussian) light-cone
model exactly — kernel, FDR, two-pin energies, IR of like pins — and name where
the sphere law departs. Definitions: 7-stencil formation
`S_x = s_x + Σ_j (s_{x±e_j})`, `φ(k) = 1 − E(k)/7`,
`E(k) = 2 Σ_j (1−cos k_j)`, equal-time
`C(k) = σ²/(1−φ²) = 7σ² / (2 E (1−E/14))`. Reversibility of the PCA w.r.t.
`π ∝ ∏ Z(β|S_x|)` is the LEAD's hypothesis (proved in the lightcone-formation
attempts); used here for the Gaussian limit only.

## (1) The statement attempted

**(a)** The *naive* fluctuation-response of the CA (dynamical susceptibility
`χ = 1/(1−φ) = 7/E` versus equal-time `C = 1/(1−φ²)`) fails:
`χ/C = 1+φ ≠ 1`. The Hamiltonian FDR of the Gaussian `π` (response to a field
in `−log π`) *does* equal `C`.

**(b–c)** Two Gaussian pins of amplitude `a` at separation `r`: like-pin energy
`a²/(C₀+C(r))`, unlike `a²/(C₀−C(r))`. If `C(r)>0` then like is cheaper
(attractive). On the massless torus the zero mode makes equal like pins
IR-divergent (`C₀=∞`); unlike (dipole) energy is IR-finite and equals
`a² / (C₀−C(r))`. On the `L=4` torus, `C₀−C(r) = 147/128` at `r=e_1`,
`e_1+e_2`, and `2e_1` (exact; a finite-size degeneracy).

**(d)** Mass is the pinned amplitude `a` (and, for a persistent CA source, the
number of pinned levels, which in the stationary Gaussian is already absorbed
into `a`). Superposition holds at linear (Gaussian) order and fails for the
sphere at `O(1/β²)` (not computed).

Newton `1/r` is the 3D Green function of `E(k)∼k²`, not a new nonlinear result.

## (2) Steps

**Step 1 — kernel identities (CHECKED as E0).**
`1/(1−φ²) = 49/(E(14−E)) = 7/(2E(1−E/14))`. `χ=7/E`. `χ/C=1+φ`.

**Step 2 — naive FDR fails (PROVED from 1).**
The CA's linear response to a driving field at one site, in the backward or
forward cone, is the resolvent `1/(1−φ)`, not `C`. Equality would need `φ=0`.

**Step 3 — two-pin Gaussian energies (PROVED; CHECKED as E1).**
The 2×2 covariance `[[C₀, C_r],[C_r, C₀]]` inverts to give like energy
`a²/(C₀+C_r)` and unlike `a²/(C₀−C_r)`. Difference
`2 a² C_r / (C₀²−C_r²)`; sign of `C_r` is the sign of like-minus-unlike.

**Step 4 — torus Green difference (CHECKED as E2).**
On `(Z/4Z)³`, mean-zero,
`C(0)−C(r) = (1/64) Σ_{k≠0} (1−cos k·r) 49/(E(14−E))`. Cosines at
`2π n/4` are `{1,0,−1,0}`, so every term is rational. The three tested
separations all give `147/128`. Unlike energy `a²/(147/128) = 128 a²/147`.

**Step 5 — IR of like pins (PROVED).**
`E(k)∼k²` near zero, `C(k)∼1/k²`, `C₀` diverges as `m→0` in `E(E+m)`. Equal
like pins couple to the zero mode and are not IR-finite; dipoles are. This is
the massless 3D Newton signature.

**Step 6 — sphere (ASSUMED, not computed).** Superposition of two vMF pins
fails at `O(1/β²)` because `log Z(β|S|)` is not quadratic.

## (3) First failing step of a nonlinear 1/r proof

Step 6: no exact sphere computation. The linear `1/r` is the Green function of
`E(k)`, already in the LEAD.

## (4) What would finish it

Exact `1/β` expansion of two vMF pins in `π`, or a coupling of the CA with two
persistent pins on `L=8..32` against the linear `128 a²/147` dipole energy.
Larger tori (`L=8` needs `√2`) to split the L=4 degeneracy of `d(r)`.

Nothing here edits notes or runners.
