# C5 R19-13 report: can a site be born already entangled? Insertion cost against isometry radius

- **Worker:** Claude Opus 5.5 (Claude Code agent). Started 05:10Z, report about 05:50Z, 2026-10-13. Same family as the supervisor. Unrefereed.
- **Item:** `TESTS:7717-7743`. Its readings are FIXED there.
- **Scratch folder:** `.../scratchpad/C5/R19-13/` (`r1913_*.py`, `r1913_*.out`; archived-runner recheck in `recheck/`).
- **Abbreviations:**
  - `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
  - `TESTS` = `.claude/science/exercises/gravity-current-state-20261009/TESTS.md`.
  - `rR19-10` = `agents/C5_R19-10_report.md` in that exercise folder.
  - `vR19-10` = `scratchpad/C5/ref_R19-10/REFEREE_VERDICT.md`. It appeared during this run and says NOT CONFIRMED, reading OPEN (`vR19-10:1-3`).
- **Units:** a = c = ħ = 1. Cosmology at a = ℓ_P, H₀ = 1.1775e-61, ρ_Λ = 1.134e-123. These are RECALLED inputs, the same as R19-10 (`r1913_numbers.out:1`).

---

## 0. Reading against the FIXED readings

**Worker reading: NO-LOCAL-ESCAPE for every field computed. A referee is required.** Scope: free quadratic laws, plane insertion, net excitation above the completed law's ground state, and any operation confined to the radius-R slab.

- **ENTANGLED-ESCAPE: not met. It is excluded for every field computed** [inequality proved; evaluation checked].
  - With R ≤ 10a, no operation on the slab gets below either threshold. This holds for every operation: any isometry, any circuit, any channel with ancillas, Gaussian or not.
  - The best possible leftover per inserted site is at least:
    - massless scalar: 5.3e-11 (`r1913_lb_m1.out:8`);
    - scalar with m = 1/a: 2.8e-24 (`r1913_lb_m1.out:3`);
    - Wilson-Dirac, m = 0: ≥ 1.7e-12 (`r1913_dirac_lb_m0.out`, R = 16, by monotonicity);
    - Wilson-Dirac, m = 1: ≥ 1.5e-26 (`r1913_dirac_lb_m1.out`, R = 16).
  - The thresholds are 3.8e-124 (persistent excitation) and 3.2e-63/τ_ins (registered formula).
- **NO-LOCAL-ESCAPE: met as a worker reading, with these stated bounds on the required isometry radius.**

| Field | Proved inequality, evaluated on the lattice | Same inequality, continuum-asymptotic evaluation (checked to 0.3%) | Central value from the explicit optimum [suggested] |
|---|---|---|---|
| Scalar, m = 0 | R > 256 a (both criteria) | R > **1.7e23 a** (persistent); > 7.9e13 a (registered, τ_ins = R); > 1.4e11 a (registered, τ_ins = 1 t_P) | R ~ 2e24–5e24 a (persistent); ~2e15 a (registered, τ_ins = R) |
| Photon (2 transverse massless scalars) [suggested identification] | R > 256 a | R > 1.9e23 a | ~5e24 a |
| Scalar, m·a = 1e-17 (SM-like) | — | R > 1.7e18 a (persistent) | — |
| Scalar, m = 1/a | R > 12 a | — | R ≈ 65–75 a (persistent); ≈ 35 a (registered) |
| Wilson-Dirac, m = 0 | R > 512 a | R > 1.5e17 a [suggested R⁻⁷ extrapolation of the bound] | R ~ 1.4e24 a (persistent); ~9e9 a (registered, τ_ins = R) |
| Wilson-Dirac, m = 1 | R > 16 a | — | R ≈ 84 a (persistent); ≈ 42 a (registered) |

Sources: `r1913_analysis.out:16,32-44,46-47`; `r1913_lb_m1.out:1-5`; `r1913_dirac_lb_big_m0.out:2-10`; `r1913_dirac_summary.out`.

- **What the referee must rule:**
  - whether the stated bound is the fully numerical one (R > 256a / 512a) or the asymptotic one (R > 1.7e23 a);
  - whether the scope below is the right class.
- **Expectation check** (`TESTS:7743`):
  - The direction is confirmed: there is no local escape for gapless fields.
  - The numbers differ:
    - The best cost falls as **R⁻⁵** (3D plane insertion), not R⁻⁴. So the required R is about 1e23–1e25 a, not 1e30 a.
    - For gapped fields the decay rate is 4κ(m) per unit R, with κ = arccosh(1 + m²/2), not m. So m ~ 1/a needs R ≈ 70a, which is not local at the R ≤ 10a standard.

---

## 1. Plain words

- **The setup.** A new plane of sites appears. Before it appears, the lattice is in its old lowest state. We may do anything we like to the new plane and to the old planes within distance R of it, but nothing further out.
- **What cannot be fixed.** In the old lattice, the two regions beyond the slab are a distance 2R+1 apart. In the new lattice they should be 2R+2 apart. Their mutual correlations are set by that distance, and nothing done inside the slab can change them. That leftover mismatch must cost energy.
- **How big it is.**
  - It falls like 1/R⁵ for massless fields.
  - It falls exponentially for massive ones, but only on the scale of the field's own correlation length.
  - For the photon, getting below the observed dark-energy density needs R of at least about 1e23 lattice spacings. That is about 3 picometres if a = ℓ_P.
- **What that radius means.**
  - It is not acausal: a light signal crosses it in about 1e-20 s.
  - But it is nowhere near "a few lattice spacings".
  - If sites were inserted one at a time as balls of that radius, each site would sit inside about 1e33 insertions running at once. Insertion would then be a collective process, not a set of local events.

---

## 2. Method

**Geometry** (as in R19-10, plane insertion, `rR19-10:84-85`).
- A new x-plane is inserted.
- Transverse momentum q is conserved, so the problem splits into 1D chains along x:
  - scalar: mass M_q² = m² + 4sin²(q_y/2) + 4sin²(q_z/2);
  - Wilson-Dirac: a 4-component chain, the same conventions as `r1910_insert_product.py`.

**Window reduction (exact, infinite chain)** [proved, elementary; `r1913_lib.py` docstring].
- Every quantity depends only on the old ground-state correlators on 2R+2 consecutive sites:
  ΔE = E_mid,new(ψ) − E_mid,old(GS) − e₀(M).
- Check: R = 0 reproduces R19-10's product numbers exactly:
  - 1D: 0.271319, 0.089796, 0.559603 (`r1913_test1.out:1-3` against `recheck/r1910_insert_product.out:4,7,10`);
  - 3D Wilson-Dirac P-loc: 0.975567 and 0.677308 (`r1913_dirac_test.out:1-2` against `:20,22`).
- The per-q optimum at R = 0 equals R19-10's P-plane: 0.041031 (infinite transverse size) against 0.040813 (L_p = 16), and 0.026126 against 0.026126 (`r1913_numbers.out:4-5`).
- The correlators agree with a 2²⁰-site ring to 2e-15 (`r1913_corrcheck.out`).

**(U) Upper bound: explicit Gaussian isometry** [checked].
- Append the new site in its local ground state.
- Apply a symplectic S (scalar) or a one-particle unitary U (Dirac) on the 2R+1 slab sites.
- Minimise the exact quadratic energy by L-BFGS on the Lie algebra (`symp_opt`, `r1913_dirac.opt`).
- The fermion gradient was checked by finite difference to 1e-9 relative (`r1913_dirac_test.out:3`).
- Random restarts converge to the same value or slightly higher, by ≤ 1%. The identity start is lowest in every case, so the values are upper bounds converged to about 1% (`r1913_restarts.out:1-3`; `r1913_dirac_test.out:4-6`).

**(L) Relaxation over all operations on the slab** [proved, elementary].
- The cross-covariance with the untouched far region must lie in the span of the old one. The Schur complement of the old pure state then gives a window SDP whose constraint matrix is
  [[Γ_SS + iJ/2, T·L], [L†·Tᵀ, 1]] ⪰ 0, with Q₀ = Γ₀,S_old + iJ/2 = L L†.
- This SDP is a valid relaxation over every state whose far-region marginal is the old one: any channel, with ancillas, Gaussian or not. It is attained by the ground state of h_new minus a quadratic term on the far region (dual argument; reading-level for attainment).
- Clarabel reaches only "optimal_inaccurate" (about 1e-7 to 1e-6 absolute). Within that accuracy it matches the explicit isometry (`r1913_sdpcheck.out:2-16`). So the SDP is used as a consistency check, not as a certificate.

**(B) Rigorous lower bound, used for every "proved" bound above** [proved].
- **The chain.** For each transverse chain with gap M_q, any feasible state ρ obeys
  ΔE_q ≥ M_q(1 − ⟨g|ρ|g⟩) ≥ M_q·D(ρ_T, σ_T)² ≥ M_q·(Δ⟨O⟩)²/4.
  - T = the two boundary planes next to the slab. Their state is the old marginal, while the new ground state σ has them one site further apart.
  - O = cos(λ(φ_bL − φ_bR)) with ‖O‖ = 1 and λ optimised.
  - The per-q reduction is valid because the energy depends only on the per-chain covariance. The Gaussian state with that covariance has the same T-marginal as the old one.
- **Fermions.** O = c†_bL X c_bR + h.c., with ‖O‖ = ‖X‖₁. This gives ΔE_q ≥ gap_q·‖G_old(d) − G_new(d+1)‖²_op (`r1913_dirac_lb.py` docstring).
- **Monotonicity [proved].** ΔE_min(R) is non-increasing in R, because a larger slab contains every smaller-slab operation. So LB(R*) > threshold excludes every R ≤ R*.
- **Evaluation.**
  - Lattice correlators (quad, 1e-13), for R ≤ 256 (scalar) and R ≤ 512 (Dirac).
  - Unresolved terms are dropped, so the bound stays a bound.
  - The scalar's continuum asymptotic (K₀/K₁ form) matches the lattice evaluation to 0.3% at R = 32–256 (`r1913_analysis.out:32-38`). It is used to solve for the thresholds.
- **Tightness.** The bound sits 100–170× below the optimum (scalar m = 0, `r1913_analysis.out:18-23`) and has an extra 1/ln²R. It is conservative.

**Thresholds** (`r1913_numbers.out:2-3`).
- **Persistent:** the net excitation left after insertion, 3ΔE/a³ per Hubble time < ρ_Λ, i.e. ΔE < 3.78e-124.
  - This is R19-10's per-Hubble-time measure (`rR19-10:97-103`).
  - It is the "net excitation deposited after insertion" observable that `vR19-10:32` separates from storage.
  - If the leftover is radiation, its steady-state density is 3ΔE/(4a³). That changes the threshold by 4×, and R by 4^(1/5) ≈ 1.3.
- **Registered:** 3H·ΔE·τ_ins/a³ < ρ_Λ, i.e. ΔE·τ_ins < 3.21e-63.
  - At every intermediate time of a slab-confined protocol, the state is again a slab operation on the old ground state. So its excess over the completed law is ≥ ΔE_min(R) throughout [proved], and the registered product is a lower bound on the storage A_fix.
  - That is completed-law accounting. `vR19-10:32` rules that it differs from instantaneous-law excitation; it is reported here only because the registered formula asks for it.

---

## 3. Results by probe

### (a) ΔE(R) for each field, with fits

**Scalar, 3D plane insertion, per inserted site** (`r1913_analysis.out:5-13`) [checked; upper bound attained to about 1%].

| R | m = 0 | m = 0.1 | m = 0.3 | m = 1 |
|---|---|---|---|---|
| 1 | 3.06e-4 | 3.01e-4 | 2.71e-4 | 1.17e-4 |
| 2 | 1.25e-5 | 1.18e-5 | 8.05e-6 | 5.03e-7 |
| 4 | 5.00e-7 | 4.07e-7 | 1.16e-7 | 7.04e-11 |
| 8 | 1.82e-8 | 9.03e-9 | 2.38e-10 | (floor) |
| 16 | 6.25e-10 | 6.65e-11 | 1.30e-13 | — |
| 32 | 2.16e-11 | 1.13e-13 | — | — |

For comparison, R = 0 (the new plane in its own 2D ground state) costs 0.041 (m = 0) and 0.026 (m = 1).

- **m = 0.**
  - Local exponents rise from 4.6 to 4.89 (`:9`).
  - ΔE·R⁵ grows slowly: 6.2e-4 at R = 10, 7.2e-4 at R = 32 (`:11`).
  - So the decay is R⁻⁵ times a slowly growing factor (reading: the 1D zero-mode logarithm). The fit is 4.56e-4·R^(−4.87) (`:10`).
  - The R⁻⁵ is the IR count [suggested]: per transverse chain the cost is about R⁻³·g(M_q R), and the 2D transverse integral gives R⁻².
  - 1D massless check: c ≈ 0.011/R³ (`r1913_timing.out`).
- **m > 0.**
  - The ratio ΔE(R)/ΔE(R+1) tends to e^{4κ(m)} = 47 for m = 1 (`:12-13`).
  - The m = 1 values reach the double-precision floor (about 1e-14) at R ≥ 5.

**Wilson-Dirac** (`r1913_dirac_summary.out`) [checked; 8×8 graded Gauss-Legendre transverse grid, 1.7% quadrature error at R = 4].

| R | m = 0 | m = 1 |
|---|---|---|
| 0 | 0.6245 | 0.4201 |
| 1 | 2.7e-3 | 2.0e-3 |
| 2 | 5.7e-5 | 1.5e-5 |
| 4 | 1.7e-6 | 1.2e-8 |
| 6 | 2.5e-7 | — |
| 8 | 6.0e-8 | — |

- The m = 0 local exponent reaches 4.99 at R = 6–8, so the decay is again R⁻⁵.
- The fermion lower bound decays as R⁻⁷ (local exponent 6.89 → 7.07 over R = 32–512; `r1913_dirac_lb_big_m0.out:7-10`). It is looser than the optimum's R⁻⁵.

**Photon** [suggested]: the transverse content as 2 massless scalars, R19-10's identification. The Gauss-law bookkeeping for the new links is not built.

### (b) The R needed at a = ℓ_P

See the table in §0.
- **Plane insertion (dilute):** every gapless field needs R ≳ 1e23 a for the persistent criterion. That is a proved inequality with asymptotic evaluation; the central value is about 1e24 a.
- **SM masses:** m·a ~ 1e-17 cuts this to R ≳ 1.7e18 a.
- **m ~ 1/a:** R ≈ 70a.
- **Heavier fields [suggested, crude, prefactor ~1].** For R ≤ 10a to suffice, fields need m·a ≳ 35 (persistent) or ≳ 6 (registered) (`r1913_analysis.out:49-50`). For m·a ≥ 2 the computed bound hits the floor at R ≈ 6–8 (`r1913_lb_m1.out:11-18`), so this is undecided. Gapless fields exist (the photon), so this does not open an escape.

### (c) Circuit realisability (Lieb–Robinson)

- **A depth-D nearest-neighbour circuit** started at the insertion acts within radius D, so ΔE ≥ ΔE_min(D) [proved, strict light cone].
  - So the depth needed is at least the required R: ≳ 1e23 layers for the photon, persistent.
  - Hamiltonian protocols with Lieb–Robinson velocity v obey the same bound with R = vτ plus exponential tails [suggested].
- **The optimal slab isometry** is a per-q Gaussian unitary. Along x it needs depth O(R) (Bloch–Messiah plus a nearest-neighbour decomposition; RECALLED).
  - Its transverse locality is not established: S(q) is optimised per q and may be non-analytic at q → 0.
  - This matters only for an escape, which is excluded anyway.
- **Dilution check** (`r1913_numbers.out:11-15`) [checked arithmetic; reading].
  - Plane events stay dilute at these R: 2HR² ≈ 6e-15 at R = 1.7e23.
  - Ball-shaped (point) insertions with τ ≈ R overlap 4πHR⁴ times. That is 1 at R = 9e14 a and about 1e33 at R = 1.7e23 a.
  - So at the required radius, local point insertion is not a set of independent events. The dilute-event bookkeeping (`rR19-10:143`; `vR19-10:26`) fails there.
- **Local or acausal?** Not acausal if executed over τ ≥ R/c ≈ 1e-20 s. Not local at the lattice scale, by about 22 orders of magnitude beyond the R ≤ 10a bar.

### (d) Prices (named; none adopted)

- **P-r1913a (entangled-birth radius).** Removing R19-10's product-birth excitation by entangling the new site at birth needs a coherent creation operation over R ≳ 1.7e23 a for each gapless free field. The fully numerical floor is R > 256a.
  - That is not a nearest-neighbour rule.
  - Axiom text touched: `AX:37-41` (locality), `AX:57-58` (one fixed nearest-neighbour rule); creation itself is P52.
  - For point insertion it also makes creation collective (overlap about 1e33).
- **The remaining routes (count once with R19-10, `rR19-10:197-203`):**
  - no site creation (E6: V1 or set A);
  - a principle that makes the insertion excitation weightless (E4; this conflicts with N_red);
  - continuous deformation instead of events (E2′ reading);
  - interacting laws, untested.
- **No tuning can evade this inside the class.** The lower bound holds for every slab operation, so tuning the isometry or the birth state cannot beat it [proved within scope].

---

## 4. Scope, and what is not shown

- **Covered:**
  - free quadratic laws: the NN scalar for m ≥ 0 and r = 1 Wilson-Dirac; the photon only via the 2-scalar identification;
  - plane insertion with dilute, additive events;
  - before insertion, the lattice is in the old ground state (as R19-10 assumes; under the `vR19-10:36` caveat);
  - the operation acts only on the radius-R slab: any CPTP map, ancillas allowed;
  - energy is measured against the completed new law's ground state.
- **Not covered:**
  - interacting laws;
  - laws with a product ground state, or commuting-projector laws (zero cost, but no gapless fields);
  - "anticipatory" states, where correlations outside the slab are prepared before insertion (this is R19-10's ramp / law-change family, counted once);
  - continuous deformation;
  - Gauss-law bookkeeping for the photon;
  - the graviton (R⁻⁵ suggested for any free gapless field);
  - point insertion in 3D (the defect geometry);
  - instantaneous-law energy accounting (`vR19-10:32`).
- **The qubit caveat.** The free bosonic oscillator is not an M₂(C) site (`AX:47`). As in R19-10 these are the registered stand-in fields.
- **Labels.**
  - "Proved" means the inequality chain and monotonicity.
  - Values at R ≤ 256 (scalar) or ≤ 512 (Dirac) are numerical evaluations of that inequality, checked.
  - Values at R ~ 1e11–1e23 use the continuum asymptotic. It is checked at R = 32–256 (0.3%) and extrapolated beyond, so those numbers are checked asymptotics, not proved.
  - Dirac thresholds beyond R = 512 and all central values are suggested.
- **Strong words checked.**
  - "any operation": scoped to the slab, the class above and free laws.
  - "exact": used only for the window reduction, the per-q decomposition, and the R = 0 matches.
  - "excluded": only for ENTANGLED-ESCAPE in the computed fields.

## 5. Rechecks and files

- **Archived runner.** `scripts/C5/R19-10/r1910_insert_product.py` was rerun: byte-identical outside the timing line (`recheck/`).
  - My independent window code reproduces its 1D and Dirac numbers (§2).
  - The other R19-10 runners were not used.
- **Scripts:**
  - `r1913_lib.py` (window, optimiser, SDP);
  - `r1913_scan.py` (c(M,R));
  - `r1913_analysis.py` (3D integrals, scalar lower bound, thresholds);
  - `r1913_dirac.py`, `r1913_dirac_lb.py`, `r1913_dirac_lb_big.py`, `r1913_dirac_summary.py`;
  - `r1913_lb_m1.py`;
  - `r1913_numbers.py`;
  - checks: `r1913_test1.py`, `r1913_sdpcheck.py`, `r1913_corrcheck.py`, `r1913_restarts.py`, `r1913_dirac_test.py`, `r1913_timing.py`.
- **Outputs:** the matching `.out` files, `r1913_scan_R*.out`, `r1913_scan_gap_R*.out` and `r1913_dirac_m*_R*.out`.
