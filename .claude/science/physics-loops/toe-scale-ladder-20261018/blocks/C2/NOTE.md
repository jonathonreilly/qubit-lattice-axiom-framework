# C2: under the matter-only reading of kinetic isotropy, the photon and fermion light cones are not tied, and the one-loop flow toward a common cone is too slow to help

**Block:** C2 of `toe-scale-ladder-20261018` (R3→R4, OBL-R3.1). **Base:** main @ 584755767.
**Status:** worker output. Unreviewed and unaudited. No audit status is claimed.
**Runners:** `scripts/run_all.py` runs all four runners. The output is in `logs/run_all.log`: `TOTAL: PASS=49 FAIL=0`.
**Review:** `REVIEW.md` (independent reviewer). Every finding is applied; see §9.

## 0. Result up front

1. **(Proved conditional, exact) T_tie: a premise that would tie the two cones.** Suppose the *whole* quadratic Euclidean action is invariant under the hypercubic group B4 of `Z^3 x Z_tau` with `a_tau = a`. "Whole" means the gauge kinetic form, the matter kinetic form and the interaction. Then the dimension-4 IR quadratic forms of the photon and the fermion are each proportional to `delta_{mu nu}`, so `c_gamma = c_psi = a/a_tau`. Group theory gives the counts. B4 has exactly one invariant rank-2 tensor and exactly one invariant quadratic form on `F_{mu nu}`.
   - Under spatial cubic symmetry times time reflection there are two of each: `(c_t, c_s)` and `(E^2, B^2)`. Time reflection or inversion is an extra assumption beyond the Lattice axiom.
   - Under the proper rotations alone, which is all the Lattice axiom gives, there are 2 rank-2 invariants and 3 gauge forms: `E^2`, `B^2` and `E.B`. `E.B` is the theta term and carries no velocity, so no conclusion changes.
   - The exact hypotheses are listed in §2.
2. **(Witness under matching premises) The registered primitive does not tie them.** The registered `kinetic_isotropy_primitive` says that *the matter kinetic normalization* has `c_t = c_s`. Its own support notes scope it to matter. `KINETIC_ISOTROPY_FROM_STRICT_LICENSE_...` says: "Matter sector only ... the gauge-sector plaquette-coefficient anisotropy ... separate rows". Witness pair W2: B4-isotropic matter (`zeta_0 = 1`) with Gaussian U(1) plaquette weights `beta_s/beta_t = xi^2`. It gives exactly `c_psi = 1` and `c_gamma = xi`. Model A (`xi = 1`) has ratio 1. Model B (`xi = 6/5`) has ratio 6/5. Both meet Lattice, cubic covariance, one tick with `a_tau = a`, the matter-only kinetic isotropy (for the bare matter action) and the scale reference. The scale reference carries no dimensionless content, so it cannot separate the two models.
3. **(Witness with the supplied ingredients on main) W1.** The photon is the supplied Gaussian lattice-Maxwell comparator. It has `omega = sqrt(UK)|s(k)|` exactly, so `c_gamma = sqrt(UK)` per unit Hamiltonian time; the landed reading gives 1.025. The fermion is the supplied two-qubit O-covariant Dirac walk with cone speed `s(b) = b0 + 2b1 + b2` per tick. Comparing them needs a declared clock conversion `rho` (Hamiltonian time per tick). Then `c_gamma/c_psi = sqrt(UK) rho / s(b)`.
   - With `rho = 1` fixed, admissible walks give 1.025/0.9144 = 1.1209 (b*) and 1.025/1 = 1.025 (`b_gold`).
   - Along a sampled admissible curve (`b2 = 3/20`, `b0` in [0.33, 0.40]), `s` runs monotonically over [0.8642, 0.9667] (numerical).
   - Neither carrier is an OS0 Euclidean object, so the kinetic-isotropy primitive **cannot be evaluated** on them as worded.
4. **(One-loop derivation plus an independent numerical check) The flow.** The matter content is a toy: U(1) plus one unit-charge Dirac fermion (N_f = 1), with independent speeds, no mass thresholds, and `alpha(m_e) = 1/137.036` imposed at the IR end. Write `eta = c_gamma/c_psi`, `delta = ln eta`, `l = ln(Lambda/mu)` (increasing toward the IR) and `alpha = e^2/4pi`:

       d ln c_psi  /dl = (e^2/6pi^2) [eta - 4/(1+eta)^2]
       d ln c_gamma/dl = (e^2/12pi^2) (1/eta - eta)
       d (1/e^2)   /dl = (eta + 1/eta)/(12 pi^2)
       d ln eta    /dl = (e^2/12pi^2) [1/eta - 3 eta + 8/(1+eta)^2]
       linearised:  d delta/dl = -(2 alpha/pi) delta      (N_f = 1)
                    d delta/dl = -(2 alpha/3pi)(N_f + 2) delta   (N_f unit-charge species, common speed)

   - The flow is attractive for all `eta > 0` (checked on (0.05, 20)). Because `alpha` itself runs to zero logarithmically, `delta(l)/delta(0) = (alpha(l)/alpha(0))^((N_f+2)/N_f)`. This is an inverse power of a logarithm.
   - Over `l = 51` with `alpha(m_e) = 1/137.036` and `N_f = 1`, the IR mismatch is **0.781** of the UV mismatch.
   - For the illustrative `N_f = 3` and `N_f = 8`, the factors are 0.637 and 0.287.
   - These numbers belong to the toy content. The real charged spectrum, with thresholds and the hypercharge embedding, would give a different O(1) number.
5. **(Conclusion: obligation for R3.)** For the declared running, the IR flow removes an O(1) factor. One loop has to stay valid up to the cutoff for this to hold. Even at the edge of perturbativity (`alpha_UV ~ 1`), the suppression is no more than about `alpha_IR^((N_f+2)/N_f)`. For `N_f = 1` that is about 4e-7, still about 8 orders short of 1e-15 (reviewer's estimate; not run in my scripts). An IR bound on `|c_gamma - c_e|/c` of order 1e-15 to 1e-20 therefore needs `|delta|` at the cutoff of the same order (1.28e-15 or 1.28e-20 for `N_f = 1`). R3 must supply that cutoff-scale equality itself. It can come from a T_tie-type symmetry that acts jointly on the gauge and matter kinetic forms, or from a derivation, which would amount to a fine-tuning statement. The natural mismatches in W1 and W2 (0.03 to 0.2) are excluded by about 13 to 19 orders of magnitude.

So the target "kinetic isotropy ⇒ common light cone" is **retired under reading K_m**. K_m is the matter-only reading, which is the scope the primitive's support notes give it. **Under reading K_full it holds, via T_tie.** The primitive's word "equivalently" means its author read "matter isotropy" and "regulator block hypercubic-symmetric" as the same statement. The phrase "the regulator block on which loops are computed" can fairly be read as covering the gauge propagator too. Deciding which reading the primitive carries is an owner or audit question; this block does not settle it.

## 1. Premises as stated on main

- **Lattice, Qubit, Admissibility, Record** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Admissibility "is not a dynamics axiom ... does not ... define a time metric". All dynamics are supplied.
- **`scale_reference_primitive`** (`a^{-1} = M_Pl`). It is "a units conversion ... zero dimensionless content". It therefore cannot fix the dimensionless `rho`, `b` or `xi`.
- **`kinetic_isotropy_primitive`** (`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`, registry node). It reads: "the matter kinetic normalization is space-time isotropic, `c_t = c_s`, equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are computed is hypercubic-symmetric". It "supplies only the kinetic form ratio".
  - **Reading K_m** (the registered text, and the scope of its support notes): matter's kinetic form is B4-symmetric.
  - **Reading K_full**: every kinetic form, including the gauge field's, and the interaction are B4-symmetric.
  - The phrase "regulator block ... hypercubic-symmetric" is ambiguous between the geometry of the block (`a_tau = a`) and the symmetry of the action on it. I record that ambiguity rather than resolve it.
  - The B4 note (`EMERGENT_LORENTZ_RADIATIVE_STABILITY_DISCRETE_TICK_B4_...`) says "species differences also vanish". That concerns the fermion self-energy for any gauge representation. It does not concern the gauge field's own kinetic form.
- **A common tick or single clock** fixes that one time parameter exists. It does not fix the ratio between sector couplings and that tick (`rho`, `xi`). This is consistent with the existing support note's finding that "the single-clock product `a_tau * H`" leaves `c_t/c_s` free.

## 2. T_tie (proved conditional; exact group theory)

**Statement.** Let the Euclidean lattice be `Z^4` with `a_tau = a`. The hypotheses are:
- (H0) the quadratic action of the gauge field and of the fermion, and their coupling, are B4-invariant;
- (H1) B4 acts on the fermion through a Pin/spinor lift under which `gamma_mu` transforms as a vector;
- (H2) no internal (taste or flavour) index transforms nontrivially under B4. Otherwise B4-invariant bilinears such as `sum_mu (gamma_mu ⊗ xi_mu) d_mu` exist, and their IR content needs a separate argument. This matters for staggered carriers;
- (H3) a local Euclidean action exists on `Z^4`. Neither the Hamiltonian comparator nor the QCA walk provides one;
- (H4) no spontaneous breaking of B4, and an analytic small-momentum expansion of the IR quadratic forms.

`c = a/a_tau` is only the conversion of the lattice-unit value 1 into physical units.

Then the dimension-4 bilinears are `Z_psi psibar gamma_mu d_mu psi` and `(1/4e^2) F_{mu nu}F_{mu nu}` (plus the topological `F Ftilde` if only proper B4 is imposed; it carries no velocity). Hence `c_psi = c_gamma = 1` in lattice units.

**Proof.** The invariant rank-2 tensors under B4 are one-dimensional, from the character average `(1/384) sum tr(g)^2 = 1`. The invariant symmetric forms on `Lambda^2 R^4` are also one-dimensional, from the `Sym^2(Lambda^2)` character average, which is 1 for B4 and 2 for the proper subgroup. A B4-invariant regulator keeps radiative corrections B4-invariant, so the equality persists order by order. Lorentz violation then starts at dimension 6, at `O(a^2 p^2)`. Runner: `witness_os0_surface.py`.

**Scope.** Exact for the group-theory counts. The all-orders persistence is the standard symmetry argument and is not re-proved here. Without the gauge-sector B4 (reading K_m), the gauge count is 2 under `O_h x Z2(t)`, and W2 realises the second invariant. Under proper `O` alone (the Lattice axiom, with no time reflection) the count is 3: `E^2`, `B^2` and `E.B`. The extra invariant `E.B` carries no velocity, so the conclusion is unaffected. This is checked in `witness_os0_surface.py`.

## 3. Witness W2 (OS0 surface; claim type: underdetermination witness under matching premises)

The exact Euclidean poles, continued `k0 -> iE`, are:
- naive or staggered fermion `sum zeta_mu gamma_mu sin k_mu`: `zeta0^2 sinh^2 E = sum sin^2 k_j`, so `c_psi = 1/zeta0`;
- noncompact Gaussian U(1) with weight `beta_t` on (0j) plaquettes and `beta_s` on (jk) plaquettes: transverse kernel `beta_t shat0^2 + beta_s |shat|^2`, so `4 beta_t sinh^2(E/2) = beta_s |s(k)|^2` and `c_gamma = sqrt(beta_s/beta_t)`. The pure-gauge zero mode was checked.

| | A | B |
|---|---|---|
| matter `zeta0` | 1 (B4) | 1 (B4) |
| gauge `beta_s/beta_t` | 1 (B4) | 36/25 (O_h × Z2(t) only) |
| tree-level `c_gamma/c_psi` | 1 | 6/5 |

Both models share every listed premise, under reading K_m, with K_m applied to the *bare* matter action. They differ only in a gauge coupling ratio that no premise constrains. The carriers (Grassmann fermion, noncompact link field) are supplied, as all fermion and photon carriers on main are. **Not claimed:** that either model satisfies Qubit as a qubit-per-site realisation. Once the interaction is on, model B also generates matter anisotropy at `O(alpha)` at the cutoff. This is the Collins mechanism. The coefficient is not computed here.

## 4. Witness W1 (supplied ingredients; claim type: exact dispersion plus numerical sample)

- **Photon.** The rebuilt lattice curl on 4³ has `ker C^T C = N + 2` and nonzero spectrum `{|s(k)|^2, twice per k != 0}` to 2e-14. So `c_gamma = sqrt(UK)`, isotropic at O(k²). The value 1.025 is the landed reading and is **cited, not recomputed** here.
- **Walk.** The Gram identity `phi^T G phi + |g|^2 = 1` holds exactly (sympy). `b_gold` has `s = 1` exactly.
  - Nine members on the curve `b2 = 3/20`, `b0` in [0.33, 0.40] are PSD of rank 3.
  - The factorised `U(k)` is unitary to 2e-15.
  - The eigenphase cone speed equals `s(b)` along an axis and along a body diagonal, to 1e-5.
  - `s` rises monotonically from 0.8642 to 0.9667. b* gives `s = 0.914422`, matching the landed value.
- **Ratio.** `c_gamma/c_psi = sqrt(UK) rho / s(b)`. At `rho = 1` the samples run from 1.025 (`b_gold`) to 1.186.
- **Premise match.** The two-qubit site is outside the Qubit axiom, as the source note says. The Gaussian comparator is not a qubit model. Kinetic isotropy is not evaluable on a Hamiltonian-time comparator or a QCA tick without a further identification. W1 therefore shows that **Lattice + cubic covariance + common tick + scale reference + the supplied carriers** do not fix the ratio. It is not a witness at the full framework premise set; W2 covers the kinetic-isotropy level.
- **Unchecked.** Continuity between the sampled points is numerical (sampled, monotone). Not proved: that it follows from a simple root of det G (implicit function theorem).

## 5. One-loop flow (derivation, then independent check)

**Setup.** Euclidean, `hbar = 1`.
- Fermion: `S = psibar[gamma0(d0 + iA0) + c gamma_j(d_j + iA_j)]psi`.
- Photon: `S_A = (1/2)[eps E^2 + B^2/mu]` with `eps = 1/(e^2 v)` and `1/mu = v/e^2`, so `v = c_gamma`.
- Photon propagator in Feynman gauge of the v-rescaled frame: `D_00 = e^2 v^3/(k0^2+v^2k^2)` and `D_jl = e^2 v delta_jl/(k0^2+v^2k^2)`. Its static limit is `e^2 v/(4 pi r)`.
- Fermion speed: `Sigma_lin = i(delta_0 gamma0 p0 + delta_s c gamma.p)` and `d ln c_psi = delta_0 - delta_s`.
  - The angular reduction is done by hand. The 4D shell integral is done exactly with sympy.
  - The pure-gauge part of any gauge choice gives a term proportional to `K(p)`, by the Ward identity, so the velocity flow is gauge-independent at one loop.
- Photon: in the frame `x' = x/c` the fermion loop is the standard QED loop. Mapping back gives `d eps/dl = 1/(6 pi^2 c)` and `d(1/mu)/dl = c/(6 pi^2)`.

**Internal consistency checks.**
- `eta = 1` is a fixed point.
- At `eta = 1`, `d(1/alpha)/dl = 2/(3pi)`, the standard QED running.
- In the `eta -> infinity` (instantaneous Coulomb) limit, `d ln c_psi/dl -> 2 alpha_C/(3pi)` with `alpha_C = e^2 c_gamma/(4 pi c_psi)`. This agrees with the one-loop Coulomb velocity enhancement for 3D Dirac fermions as I recall it from the Weyl-semimetal literature (e.g. Goswami–Chakravarty 2011). That citation is recalled, not re-checked here.
- `c_gamma^2 c_psi` is invariant to first order in `eta - 1`: `d ln(c_gamma^2 c_psi)/dl = e^2 delta^2/(24 pi^2) + O(delta^3)`. This matches the structure that a web-search abstract summary reports for Isobe–Nagaosa, PRB 86, 165127 (2012): "c and v approach the common value with c²v almost unrenormalized". Their explicit coefficients could not be fetched (network blocked), so the coefficients themselves are **not cross-checked against the literature**.

**Independent check (`rg_independent_numeric.py`).** This is a different implementation:
- explicit 4×4 gamma matrices and a numerical inverse;
- full 4D hyperspherical quadrature with no hand angular averaging;
- a non-spherical smooth regulator `exp(-(k0^2 + 2k^2))` (Frullani difference);
- an explicit fermion-loop `Pi_{00}` and `Pi_{xx}` second derivative for the photon, instead of the frame-rescaling argument;
- a gauge-parameter term to test gauge independence.

Results:
- Five `(c_psi, c_gamma)` pairs agree with the closed form to about 1e-6 relative.
- Changing the gauge parameter changes the flow by less than 1e-7.
- `d eps/dl` and `d(1/mu)/dl` agree to about 2e-6.

The first run used a truncated radial range. It failed four checks at about 2e-4, which was the quadrature truncation error. That log is kept as `logs/rg_independent_numeric_run1_truncated_radial_range.log`. The range was extended and the tolerance was left unchanged.

**What is not independent.** The sign convention `K_eff = K - Sigma~` and the definition of `Sigma~` are shared by both scripts. The sign is anchored separately by the Coulomb-limit enhancement, by the screening sign of the vacuum polarisation, and by the qualitative attraction of Chadha–Nielsen (NPB 217 (1983) 125).

**Residuals (declared inputs).**
- `alpha(m_e) = 1/137.036`. `alpha_UV` is fixed by Lorentz-limit one-loop running over `l`.
- The full nonlinear system was integrated with `solve_ivp`.

| l | eta_UV | eta_IR | ln eta_IR / ln eta_UV |
|---|---|---|---|
| 51 | 1.001 | 1.000781 | 0.7813 |
| 51 | 1.025/0.9144 (W1, b*) | 1.093089 | 0.7795 |
| 51 | 1.2 (W2, B) | 1.152478 | 0.7784 |
| 51 | 2 | 1.700558 | 0.7660 |
| 51.53 (`M_Pl` = 1.22e19 GeV) | 1.001 | 1.000779 | 0.7792 |
| 49.92 (reduced `M_Pl`) | 1.001 | 1.000785 | 0.7856 |

The small-mismatch ratio matches `(alpha_IR/alpha_UV)^3 = 0.78129` to 1e-4.

**Experimental comparison (order of magnitude only; values not verified in this block).** Bounds on a photon–electron maximal-speed difference from vacuum Cherenkov, photon decay, synchrotron and inverse-Compton arguments, and from Hughes–Drever-type tests, are of order 1e-15 or tighter. Sources: Coleman–Glashow, PRD 59, 116008 (1999); Stecker–Glashow, Astropart. Phys. (2001); Altschul's synchrotron and Cherenkov analyses; the Kostelecký–Russell *Data Tables for Lorentz and CPT Violation*. The required cutoff tuning in §0.5 uses 1e-15 and 1e-20 only as declared illustrative thresholds.

## 6. What R3 must still derive (open obligation)

- **OBL-R3.1a (symmetry route).** Show that the emergent photon and the emergent fermion come from a single structure whose gauge-sector *and* matter-sector kinetic forms are B4-related on a common tick. That is the T_tie premise. With it, dimension-4 LV vanishes and residuals are dimension 6, `~ (E/M_Pl)^2`. The ring-model photon (continuous Hamiltonian time) and the QCA walk do not currently share any such structure. Promoting reading K_full to a primitive would be new primitive content and needs owner approval (workflow rule 3).
- **OBL-R3.1b (fine-tuning route).** Without such a symmetry, derive that the cutoff-scale mismatch is below about 1e-15 to 1e-20, including the regulator-induced `O(alpha)` threshold term. This is the lattice-induced dimension-4 LV of Collins–Perez–Sudarsky–Urrutia–Vucetich, PRL 93, 191301 (2004). It is not suppressed by the cutoff, and the logarithmic IR flow of §5 cannot remove it.
- **Not addressed.** The size of that threshold coefficient for W1 or W2; two-loop and non-perturbative effects; strong coupling at an emergent-photon cutoff, where one loop is not valid; a photon built from bilinears of the same fermion (the "hidden constraint" failure mode, which the supplied ingredients do not realise).

## 7. Novelty and relation to repo work

- The two-velocity QED flow is standard physics. The literature I could name: Chadha–Nielsen 1983; Anber–Donoghue, PRD 83 (2011), as recalled; Iengo–Russo–Serone, JHEP (2009), as recalled; Isobe–Nagaosa 2012.
- In the repo:
  - `EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_...` proves the attraction for *any* positive drag coefficients.
  - `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_...` uses a *supplied* one-loop packet.
  - This block supplies explicit U(1)+Dirac coefficients: fermion drag `a = e^2/(3pi^2)` and photon drag `b = N_f e^2/(6pi^2)` on `delta`. They are positive, so they instantiate that exchange-matrix theorem. The block also supplies the `alpha^((N_f+2)/N_f)` closed form.
- The witness pairs and the precise K_m versus K_full split are new bookkeeping.

## 8. Reproduction

```
python3 scripts/run_all.py          # ~1 min; TOTAL: PASS=49 FAIL=0
```
Per-runner logs: `logs/witness_supplied_ingredients.log` (10/0), `logs/witness_os0_surface.log` (14/0), `logs/rg_one_loop_analytic.log` (14/0), `logs/rg_independent_numeric.log` (11/0).

## 9. Review dispositions (`REVIEW.md`)

| Finding | Disposition |
|---|---|
| 1a–1c: flows, linearisation, closed form correct (re-derived in Coulomb gauge, fermion frame) | No change needed. The reviewer's Coulomb-gauge result, with its `Z_2` sign anchor, is an independent check of the convention I had flagged as load-bearing. |
| 1d: name the toy matter content in §0.4 | §0.4 now states U(1) plus one unit-charge Dirac fermion, no thresholds, `alpha(m_e)` imposed at the IR end, and that the real spectrum gives a different O(1) number. |
| 1e: "at most O(1)" holds only in the perturbative window | §0.5 now reads "O(1) for the declared running". It adds the `alpha_UV ~ 1` bound, about `alpha_IR^((N_f+2)/N_f)` ≈ 4e-7 for `N_f = 1`, which is still about 8 orders short. That number is the reviewer's estimate and was not run in my scripts. |
| 1f: literature coefficients unverified | No change. The note already says they were not cross-checked. |
| 1g: "stationary to second order" is ambiguous | Changed to "invariant to first order in `eta - 1`", with the O(δ²) drift stated explicitly. |
| 2a: the Lattice axiom gives proper rotations only, so the gauge count is 3 (incl. `E.B`) | Stated in §0.1 and §2. Time reflection is marked as an extra assumption, and the conclusion is unaffected. A new runner check confirms the O-only counts (2, 3). |
| 2b: list the T_tie hypotheses | §2 now lists H0–H4: spinor lift, no B4-charged taste index, Euclidean local action, no symmetry breaking or analyticity. It also notes that `c = a/a_tau` is a units conversion. |
| 3a/3b: W2 and W1 correct as scoped | §3 now says K_m applies to the *bare* matter action. |
| 3c: headline conditional on K_m | The title and the §0 closing line now say the result is retired under K_m and holds under K_full via T_tie. The "equivalently" ambiguity is spelled out, and the choice of reading is left to owner or audit. |
| Typo in §0.2 | Rewritten: "the scale reference carries no dimensionless content". |
