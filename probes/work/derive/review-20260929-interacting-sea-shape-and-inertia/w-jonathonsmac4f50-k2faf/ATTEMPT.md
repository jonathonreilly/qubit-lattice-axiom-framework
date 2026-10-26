# J:derive:review-20260929-interacting-sea-shape-and-inertia:a1

Worker: Claude Sonnet 5.5, same family as the sources, unrefereed. Nothing here is audited or accepted.

## Plain-language summary

The source note says that on a lattice the vacuum energy changes when the metric is sheared at fixed volume. It says that for interacting matter no construction is known that removes the change, so a tuning would be needed.

I tested one candidate exit that is neither tuning nor a volume-preserving relabelling. The candidate is a supersymmetric ("Q-exact") completion: a boson and a fermion per site, with the interaction included, where the Hamiltonian is `{Q, Q^dag}` and the metric enters only through the prepotential `W`.

For that supplied model, the ground energy is exactly zero for every shear, constant or position dependent. This holds with a quartic interaction and is not a perturbative statement.

Each half alone does carry a shear coefficient, `+2` for the boson half and `-2` for the fermion half per site, and the excitation levels do move with the shear. So the matter sees the shear while the vacuum energy does not.

This is a continuous-site comparator. It is not the walker's Dirac sea, it has no light cone, it is not on qubit sites, and soft breaking of the supersymmetry brings a first-order leak back. So it shows that tuning and volume-preserving flow are not the only logical exits. It does not show that the walker's sea has one.

## What I read

- I read `docs/MINIMAL_AXIOMS_2026-06-29.md` in full on current main (a77a3449c9, plus a fetch of origin/main). Cited: Lattice lines 35-41, Qubit lines 43-53 (the one-site domain is `M_2(C)`, line 47), Record lines 75-80, Qualification lines 85-90 (further structure needs a retained derivation or an approved primitive).
- I read `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full. The approved primitives are `scale_reference_primitive` (line 31), `kinetic_isotropy_primitive` (line 58) and `realized_state_primitive` (line 98). None supplies shape-blindness, supersymmetry or a bosonic site.
- I read the full source note
  `docs/THE_WALKERS_SEA_FEELS_THE_SHAPE_OF_A_CONSTANT_METRIC_UNDER_THE_NATURAL_COUPLING_A_DESIGNED_COUPLING_REMOVES_IT_FOR_FREE_MATTER_INTERACTIONS_BRING_IT_BACK_BOUNDED_THEOREM_NOTE_2026-09-27.md`
  (sha256 verified). It is **not on current main**, only on the author branch at frozen commit `fd51a1f4c7f3`. I also read `SOURCE_MAP.json` and its "WALKER_SEA" correction list. The other 25 source objects were hash-verified; I searched them (not read in full) for the exits, tuning, boson and Ward-identity passages in ROUTES, WALL and SUMMARY.
- Prior-art search:
  - `git grep` on origin/main finds no note on a Q-exact or supersymmetric lattice vacuum energy under shear (supersymmetry appears only in unrelated YT/Koide notes).
  - The probes view `work/` tree has no attempt on it. The nearest are `compute/the-interacting-seas-polarisability-2d` (a clock modulation, hard-core crowd) and `derive/the-seas-long-wavelength-shear-response-exactly`, which are the free-sea or clock cases.
  - No other `review-20260929-*` attempt appears in the probes view `work/derive` listing, so none overlaps.

## Setting and premises (every one assumed)

- A1 (ASSUMED, supplied comparator): sites carry a real unbounded variable `phi_x` and one fermion mode `psi_x`. **This is outside the Qubit axiom's domain `M_2(C)`.** Main's own no-go says exact bosonic CCR is impossible in one-qubit algebras (`docs/NO_PER_SITE_BOSONIC_CCR_THEOREM_NOTE_2026-05-02.md:5-9`). The model is therefore the source's "option A" (continuous sites), not a consequence of the axioms.
- A2 (ASSUMED): the supplied prepotential
  `W(phi; g) = 1/2 sum_x g^{ij}(D_i phi)_x (D_j phi)_x + 1/2 m^2 sum phi^2 + (lam/4) sum phi^4`.
  `D_i` is the forward difference, `g = g^{ij}` the inverse metric, `det g = 1` for a shear, and `g = expm(t eps)` with `eps` symmetric traceless and `tr eps^2 = 1`.
  Source action: **the metric enters only through `W`**.
- A3 (ASSUMED): `A_x = d_x + W_x`, `Q = sum_x psi_x^dag A_x`, `H = {Q, Q^dag}`. The state is the ground state of `H`.
- A4 (ASSUMED, the real premise): the supersymmetric structure is exact. It is not an axiom, and no approved primitive supplies it.

## Steps

1. **PROVED.** `Q^2 = 0` for any `W`. Proof: `Q^2 = sum_{xy} psi_x^dag psi_y^dag A_x A_y`. The `psi^dag` anticommute, and `[A_x, A_y] = d_x W_y - d_y W_x = 0` because `W_x` is a gradient. **CHECKED** symbolically (S1): 3 sites with symbolic entries of a general symmetric quadratic part, quartic and cubic terms on polynomial test vectors; 2 sites on completely generic component functions.

2. **PROVED.** `H = {Q, Q^dag} = sum_x (-d_x^2 + W_x^2 - W_xx) + 2 sum_{xy} W_xy psi_x^dag psi_y`. Proof: use `[A_x, A_y^dag] = 2 W_xy` and `A_x^dag A_x = -d_x^2 + W_x^2 - W_xx`. **CHECKED** (S2, same cases).

3. **PROVED.** If `exp(-2W)` is integrable, then `Psi_0 = exp(-W)|vac>` satisfies `Q Psi_0 = 0` and `Q^dag Psi_0 = 0`, so `H Psi_0 = 0`. Also `H = Q^dag Q + Q Q^dag >= 0` in the form sense. So the **ground energy is exactly 0**.
   - **CHECKED** symbolically (S3): `H exp(-W)|vac> = 0` with free symbolic `a_ij`, `lam`, `mu`.
   - A technical premise: `H` is taken as the Friedrichs extension. Its zero-fermion part is a Schrödinger operator with polynomial potential bounded below.

4. **PROVED.** For `A(g) = m^2 + g^{ij} D_i^T D_j` we have `v^dag g v >= 0` for every `v`, since `g` is positive definite and the form is a sum of squares. So `W` is coercive and `exp(-2W)` is integrable for every shear `g > 0`, constant or position dependent. **CHECKED** with exact rational pivots (S5): `A` on the `3^3` torus for `g = [[2,1,0],[1,1,0],[0,0,1]]`, `det = 1`.

5. **PROVED, conditional on A1-A4.** The static ground-energy functional of the metric is identically zero: `E_0[g(x)] = 0` for every positive `g(x)` with arbitrary position dependence. This follows from steps 1-4 with an arbitrary symmetric `A_xy` (S1-S3 already carry free `a_ij`).
   - So the static kernel has no mass term `c_0`, no gradient term `kappa`, and no cubic `E`/`T` anisotropy, at any order in `lam` and with the interaction included.
   - The source's T3 birefringence has no analogue in this model. That does not remove it for the walker.

6. **CHECKED, exact (S4, S6).** Static cubic shear coefficients of the two unprotected halves.
   - The boson half is `E_b = sum a_k = tr A` (oscillator algebra, S4b), with `A_xx = m^2 + sum(g) + tr(g)` (S4a).
   - The fermion half, in the zero-fermion sector, is `-sum W_xx = -tr A` in the quadratic case.
   - For `E = E_0 + c t^2/2`: `c = +2` (boson) and `-2` (fermion) per site, for both axis and face shears. They are equal, `c_E = c_T`, because `Cbar = I + 11^T` makes the response bilinear in `g`.
   - With the central-difference coupling `sin k_i sin k_j` they are `+1/2` and `-1/2`. So the coefficient is coupling dependent; the cancellation is not.
   - This separates static cubic coefficients from anything dynamical. The source's `c_E != c_T` is a Dirac-sea property; it does not appear in this model.

7. **CHECKED (N1, N2, N4), numeric, exact diagonalisation.** Periodic 2x2 cluster, harmonic-oscillator truncation `d = 13` per site, `s = 6`, quartic coupling `lam = 0` and `3`, axis and face shears at `t = 0, +/-0.3`.
   - The truncated SUSY ground energies are `<= 2e-4`, positive (a variational upper bound), and `d = 9, 11, 13` give `2.8e-3, 6.8e-4, 1.1e-4`, converging to the exact 0.
   - At `lam = 3` the boson-only energy at `t = 0` is `23.65` against `20` free, so the interaction is not a small effect.
   - The boson-only curvature is `7.96` (axis) and `7.72` (face) against `8.03` free. The supersymmetric total curvature is `<= 2e-4`.

8. **CHECKED (N3).** The matter sees the shear while the vacuum does not. The 12 lowest levels differ between `t = 0` and `t = 0.3` (face) by up to `0.18` (`lam = 0`) and `2.2` (`lam = 3`), while `E_0` stays at its `1e-4` truncation floor.
   - **PROVED** at `lam = 0` (oscillator algebra): the one-boson level at lattice momentum `k` is `2 a_k(g)`, with `a_k = m^2 + conj(v_i) g^{ij} v_j` and `v_i = e^{i k_i} - 1`. It depends on `g` for `k != 0`.
   - The model has `omega ~ k^2` at small `k`. It has no cone, so it has no wave speed. This step makes **no** statement about the speed of any transverse-traceless wave.

9. **CHECKED (B1).** Soft breaking leaks at first order. Shift the boson `phi^2` coefficient by `delta` only, with the Gaussian sector exact. Then `E = sum (sqrt(a^2 + delta) - a)` and the curvature per site is `-0.0125 delta`, with the same slope at `delta = 0.02` and `0.1`. A finite-difference cross-check agrees to `1e-6`. The supersymmetry would have to be exact, not approximately tuned. The leak is small only because `a >= m^2 = 1` here.

10. **CHECKED (B2, B3), inertia, two different objects.**
    - For one oscillator `H = p^2 + a^2 phi^2` with parameter `a(eps)`, the adiabatic mass `M = 2 sum |<n|H'|0>|^2/E_n^3` equals `a'^2/(16 a^3)` and the Berry metric equals `a'^2/(8 a^2)`. Both are verified by sum over states.
    - On the 3D free lattice (`m^2 = 1`), per site: `M = 0.00060` (axis) and `0.00059` (face); Berry metric `0.0064` and `0.0086`.
    - On the 2x2 cluster at face shear `t = 0`, from exact diagonalisation with MINRES resolvents: `M = 0.00274` at `lam = 0` (matches the mode formula) and `0.00202` at `lam = 3`; Berry metric `0.0494` and `0.0401`.
    - So the sea contributes **inertia but no potential**. These are adiabatic and geometric quantities of a constant `eps(t)`. They are not the member's `alpha`, which is supplied. `Q` depends on `t`, so the zero energy is the instantaneous one; I make no claim about full time dependence.

11. **READING.** "Strict curvature requires the field to see the shear." In this model, `eps` enters only through `W`, so the matter-induced potential for `eps` is identically zero, and the induced action is a pure kinetic term (step 10). Separating the two: the static coefficients vanish identically, and the dynamical response does not. The wave speed of any member induced from this sea is then not fixed by the static kernel. It would need gradient and kinetic terms that this model does not provide.

12. **NOT DONE (first unresolved step): a Q-exact interacting completion for the walker's Dirac sea on qubit sites.** This needs three things at once:
    - a nilpotent `Q` on `M_2(C)` sites (no bosons per site),
    - a fermion sector with the walker's symbol and a cone (so wave speeds exist),
    - the metric entering through `Q` alone.

    Nothing here shows it exists or is excluded. The source's T5 matched boson (exact for free matter) and this model are the two data points; neither is the walker.

## What is new relative to the sources

- **New (CHECKED/PROVED, scoped):**
  - An explicit interacting family (quartic, nonperturbative) whose ground energy is exactly shape-independent. The shear-dependence of the unprotected halves and of the excitations is shown beside it.
  - The source's exits list (N1) has routes "matching" (free only), "Ward identity" (momentum only) and "relabelling". It does not list an exact Q-exact interacting completion, so route 3 as written is incomplete.
  - The static / dynamic separation of step 11, and a soft-breaking leak estimate.
- **Not new:** a supersymmetric vacuum has zero energy (Witten 1981, reference only). Source retrieval, and the source's own T5 free matching, are not new. The source's N2 already remarks that a supersymmetric spectrum would cancel the effect, but gives no interacting construction.
- **Source scope corrections respected:** I did not rely on the source's `c_E`, `c_T`, `kappa` or `Gamma a` values, only on its definitions.

## Limits

- This is a **comparator with continuous sites**. By the source's price lemma, continuous sites are one of the known exits (option A). The new content is that the shape term can be removed there *with interactions and without tuning*, by an exact symmetry.
- **A4 is a new structural premise.** It is not an approved primitive. It would have to be approved or derived. It also sets the vacuum energy to zero, which is a much stronger claim than shape-blindness.
- The ED is a 2x2 periodic cluster. The algebra (steps 1-5) is exact in all sizes; the numbers are not infinite-volume.
- Not computed: trace and shift sectors; finite-`q` dynamics; any pole, whether numerical roots of a response kernel or exact full-theory poles; Lorentzian time; the walker; three-dimensional ED; a 3D cluster with a true shear in all three directions (the 3D rows are Gaussian sums).
- Failed search is not a no-go. Nothing here supports a negative claim, so the N1-N8 gate does not apply to this result.

## Files

- `check.py`: 34 checks, about 45 s, one process.
- `RECOVERY_STATUS.json`: source hashes and the first unresolved step.
- `run.log`: output of the last run.
