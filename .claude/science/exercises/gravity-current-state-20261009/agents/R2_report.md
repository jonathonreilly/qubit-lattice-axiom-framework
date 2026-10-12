# Lane R, probe R2: rank-2 symmetric-tensor U(1) gauge theory on Z^3

Worker: Claude Opus 5.5 (same family as the supervisor). Not refereed. Every FAIL below
needs the codex sol referee before it is recorded (lane R rules).

Labels: **proved** = elementary derivation here (unrefereed); **checked** = numerics run here
(scripts and .out files in this folder); **suggested** = argument; **reading** = interpretation;
**comparator** = literature, recalled and not re-read in this run.

## 0. Prior art (read before building)

- **Landed, main:** `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`
  (proposed_retained, conditional-support, unaudited). It covers the vector + scalar-constraint version (my "VS"):
  - strong (compact, regular-character) class gives every frequency O(k^3);
  - the linear H_N comparator (DeWitt kinetic plus h:R) is only weakly gauge-invariant;
  - finite penalties leave an indefinite scalar block with a Jordan chain;
  - its "every local h-character is O(k^2)" cycling argument is the same fact behind my vector-charge row V.
  - V and VS below are re-verifications, not new.
- **Landed, main, 09-24:** the two DYNAMICS_CLAUSE tensor notes (freeze under two-site generators; soft vector constraint generates curvature moves at twelfth order). Both concern the same complex.
- **Landed, main, 09-30:** `FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-30.md`, the mixed lapse/shift obstruction.
- **Viability campaign, PR #9363** (closed unmerged; its core was salvaged in d31bbef9a8):
  - probe 10: sum rule, slow gravitons in the regular class;
  - probe 11: a first-order (linear) spin-2 mode carries helicity-1 partners, gapless unless chi_1 -> 0; Pretko's vector-charge theory is prior art for its T4.
  - My scalar-charge rows S and S-tl reproduce probe 11's partner statement in an explicit model.
- **Gravity exercise packet:**
  - ROUTES.md F6: an emergent rank-2 Gauss law is "blocked-equivalent to K3a's exact interacting stress" (matter's charge must equal its momentum);
  - OUTSIDE_VIEW.md:46,49,68 and B_referee.md:176 (fractons do not all have k^2 or k^3 dispersion).
- **Comparator (literature):**
  - Gu–Wen (gr-qc/0606100, arXiv:0907.1203);
  - Xu (2006, soft-graviton boson liquid);
  - Pretko (PRB 95, 115139 (2017): scalar and vector charge theories; "fracton gauge principle" 2018);
  - Rasmussen–You–Xu (arXiv:1601.08235: stable gapless rank-2 phases in 3D);
  - Hermele–Fisher–Balents (2004: spin-ice photon);
  - Carroll–Field–Jackiw (CS-type instability);
  - Weinberg–Witten (1980).

## 1. Setting (stated as prices; nothing adopted)

A_ij symmetric, with the diagonal on sites and the off-diagonal on plaquette centres. E_ij is its conjugate. With midpoint placement the lattice symbols are the continuum ones with k -> q = 2 sin(k/2), exactly (the landed note's convention).

Versions (each redundancy is a **price**: an exact local gauge redundancy on the record/qubit tensor slots that the axioms do not supply):

| Version | Gauge redundancy on A | Gauss law on E |
|---|---|---|
| S (Pretko scalar charge) | A -> A + ∂∂α | ∂_i∂_j E_ij = 0 |
| S-tl | A -> A + ∂∂α + δ_ij φ | ∂∂E = 0, tr E = 0 |
| V (vector charge) | A -> A + ∂_iλ_j + ∂_jλ_i (linearized spatial diffeo) | ∂_i E_ij = 0 |
| V-tl (Xu-type) | V plus δ_ij φ (linearized Weyl) | ∂_iE_ij = 0, tr E = 0 |
| VS (landed 09-14) | V on A, plus the scalar constraint tr R(h) = 0 generating E -> E + (Δ-Hess)β | — |

Hamiltonian: H = ½ E·K(k)·E + ½ A·Q(k)·A + Re E·X(k)·A.
- Symmetry: only the proper cubic group O, as the Lattice axiom gives. Neither P nor T is supplied.
- Gauge invariance: Q(k)V(k) = 0 and X(k)V(k) = 0 for every k.
- **Strong class:** Q is a Hermitian form in local gauge-invariant linear functionals. This is what a compact lattice model built from local gauge-invariant operators gives.
- **Weak class:** everything with Q(k)V(k) = 0, i.e. invariant only after integration (Chern–Simons-like, h:R-like).

## 2. Complete term list (checked: `r2_terms.py` → `r2_terms.out`)

Columns:
- **I(d):** dimension of the local invariant linear functionals of degree d, with no symmetry imposed.
- **W(n):** all cubic-invariant gauge-invariant A-block symbols of degree n.
- **S(n):** the strong subset.

| Version | I(0..3) | W/S, n=0 | n=1 | n=2 | n=3 | n=4 | n=5 | n=6 |
|---|---|---|---|---|---|---|---|---|
| S | 0, 8, 21, 39 | 0/0 | **1/0** (rank-2 CS, P-odd) | 3/3 | 4/4 | 9/9 | – | – |
| S-tl | 0, 5, 15, 29 | 0/0 | **1/0** | 2/2 | 3/2 | 6/6 | – | – |
| V | 0, 0, 6, 15 | 0/0 | 0/0 | **1/0** (h:R, P-even) | 1/0 | 3/3 | – | – |
| V-tl | 0, 0, 0, 5 | 0/0 | 0/0 | 0/0 | **1/0** (grav. CS, P-odd) | **1/0** (P-even) | 1/0 | 2/2 |

E-block K at order k^0, by irreps of Sym² = A1 + E + T2: 3 coefficients (kA1, kE, kT2); the traceless versions have 2.

Mixed E–A terms, lowest order (S family), by irrep count: E:sym(B) has 2 coefficients (E→E, T2→T2). Both are P-odd and T-odd. One combination, proportional to K, is a canonical transformation, i.e. a shift of E by the CS functional (checked: it gives zero helicity splitting).

## 3. Step 1: spectrum, helicities, dispersion (checked: `r2_spectra.py` → `r2_spectra.out`)

Each row is a generic strong cubic Hamiltonian. ⟨m²⟩ is the continuum helicity² about k̂. Modes are listed along [001], [110], [111] and a random direction.

| Version | Physical modes | Helicities (along [001]) | Dispersion | Notes |
|---|---|---|---|---|
| S | 5 | ±2, ±1, 0 | ω ∝ k, all 5 | Along [001] the two helicity-2 polarisations differ: v² = kE·mT2 vs kT2·mE (cubic birefringence). Along [111], C3 mixes helicity 2 and 1 |
| S-tl | 4 | ±2, ±1 | ω ∝ k, all 4 | Same anisotropy |
| V | 3 | ±2, 0 | **ω ∝ k²** | Strong class; lowest invariant is linearized curvature R (degree 2) |
| V-tl | 2 | ±2 | **ω ∝ k³** | Lowest invariant is the Cotton tensor (degree 3) |
| VS | 2 | ±2 | ω ∝ k³ (strong) | Landed 09-14 note; not recomputed |

**Lattice check (checked).** The S model on Z³ with q = 2 sin(k/2) and a cubic harmonic multiplier was run on a 14³ BZ grid. Away from Γ there are no zero modes (min ω = 0.33) and no instability (max |Im ω| = 6e-15). ω/|k| converges as |k| → 0 (0.603, 0.631, 0.858, 1.066, 1.070), so the five modes are linear.

## 4. Step 2: protection

**(a) No gauge-invariant term gives a mass (proved; checked by W(0) = 0 in every version).**
- Q(k)V(k) = 0 at lowest order gives Q₀·V_lead(k) = 0 for all k.
- For S, V_lead = k⊗k, and these span Sym², so Q₀ = 0.
- For V, the cycling argument (landed note) puts every invariant at O(k²).
- For V-tl, I(d) = 0 for d ≤ 2 (checked), so invariants are O(k³).
- So the A-block vanishes at k = 0 for every term allowed by the redundancy, and no helicity-2 gap can arise. This holds in both the strong and the weak class.

**(b) Weak-only terms do not gap the mode, but they destabilize it (checked).**

| Version + lowest weak term | Result at small k |
|---|---|
| S + rank-2 CS (A:B, degree 1, P-odd), either sign | Helicity ±2 and ±1 unstable (Im ω ≠ 0) for k below θ/g; the Carroll–Field–Jackiw analogue |
| V + g·h:R (degree 2) | g > 0: helicity-2 linear but helicity-0 unstable. g < 0: helicity-2 unstable, helicity-0 linear. Linear helicity-2 with a stable vacuum needs g = 0, which returns ω ∝ k² |
| V-tl + gravitational CS (degree 3, P-odd) | Unstable; the other branch goes as k^1.5 |
| V-tl + the P-even degree-4 weak term | Definite on TT; one sign gives stable ω ∝ k², the other is unstable. Never linear |

The strong class (compact lattice models) excludes all of these. **Suggested:** a CS-type weak term can still be induced by integrating out P-violating matter (as in 2+1D induced CS and the chiral-magnetic instability), and h:R is Sakharov's induced Einstein–Hilbert term. The strong/weak distinction is therefore protected only by P, or by the matter content, not by the redundancy alone.

**(c) Breaking the redundancy with the stiffness wall's label-dependent shear terms (checked).**
- I added μ_E·P_E + μ_T2·P_T2 to the S model, using the full 6×6 phase space with no Gauss law.
- μ_E ≠ 0 gaps the E-type polarisations (ω₀ = 0.089 = √(kE·μE)).
- μ_T2 ≠ 0 gaps the T2-type polarisations, including the helicity-1 modes (ω₀ = 0.107).
- The former gauge direction becomes a physical linear mode (v = 2.91), Stückelberg-like.
- **Gaplessness of helicity 2 needs μ_E = μ_T2 = 0: two tunings, exactly P0's two TT numbers.**

**(d) What perturbation theory says (suggested plus comparator).**
- Suppose matter couples only through the Gauss-law charge, so the redundancy is exact; or suppose it is emergent, with the Gauss law enforced energetically and its violations gapped (the spin-ice mechanism, Hermele–Fisher–Balents).
- Then the vacuum polarization obeys the Ward identity Π(k)V(k) = 0, so by (a) Π(0) = 0 and no shear mass is generated, to all orders.
- Non-perturbative stability of compact rank-2 phases in 3D is claimed by Rasmussen–You–Xu (comparator).
- **But** if matter couples to A through its lattice stress T_ij (needed for (iii)), the coupling is gauge-invariant only when T obeys the Gauss law's conservation law (§6), and lattice matter's stress does not.
- **Check:** a free lattice scalar coupled by hopping modulation (1 + A_ii) gives a nonzero uniform E-channel response, d²E_vac/dε² = −0.0386 at m = 0.5 and −0.0310 at m = 1. This is the paramagnetic piece only; any contact term must be tuned against it.
- That is the stiffness wall again (cf. K3a″, K₀⁴/(120π²) per boson).

## 5. Step 3: speed and isotropy tunings (checked: `r2_tune.py` → `r2_tune.out`)

| Version | Leading-order cubic coefficients | Helicity-2 isotropy conditions (local codim at an isotropic point) | Matter-cone match | Birefringence ±2 without T or P | Total speed tunings |
|---|---|---|---|---|---|
| S | 6 (kA1, kE, kT2; mT1, mE, mT2) | **2** (the isotropic family kE = kT2, mE = mT2 satisfies them; exact locus not mapped) | +1 | +1 (anisotropic E:B part; xE = xT2 gives zero splitting, checked) | **3** with T or P supplied; **4** without |
| S-tl | 4 (kE, kT2; mE, mT2) | **2** | +1 | +1 | 3 / 4 |
| V, V-tl, VS | — | not counted: no stable linear helicity-2 in the strong class | | | |

- A matter cone on the cubic lattice (scalar or staggered at O(k)) is isotropic automatically, since the rank-2 cubic invariant is δ_ij. The graviton's rank-4 structure is not, hence the two isotropy tunings.
- The extra helicity ±1 (and 0) branches have independent speeds. They are not part of criterion (iv), but they are extra gapless modes.
- **Against P0:**
  - P0 is two TT fine tunings at about 1e-99, plus speed tunings the K referee calls "generically expected", which are unproved.
  - R2's S version needs no mass tunings, but 3 speed tunings (4 without T or P) at observational precision (|c_g − c|/c ≲ 1e-15).
  - On established counts alone, 3 > 2. If P0 needs as many speed tunings for a supplied graviton (reading: any helicity-2 field on the cubic grid has the same rank-4 anisotropy), S needs fewer.
  - **(iv): INCONCLUSIVE**, because P0's speed count is not established.

## 6. Step 4: universality and coupling to matter

**Minimal gauge-invariant matter (proved, by the symbol argument).**
- **S:** a single scalar charge hopping x → x+a needs a Wilson factor whose gauge variation is α(x+a) − α(x). That requires c_ij(k)q_iq_j = e^{ik·a} − 1, with a left side of O(k²) and a right side of O(k). This is impossible for finite support. Isolated charges are immobile (fractons); only dipoles hop. The tensor mode couples to fracton charge density and dipole currents.
- **V:** a particle with vector charge n can hop by a only if a ∥ n. The leading-order condition 2m_ij(0) = i n_j a_i, with m symmetric, forces this. Charges move only along their charge vector (Pretko's result, re-derived).

**Coupling to energy and momentum (proved within the linear coupling class A_ij J_ij + (temporal gauge field)·ρ).**
- **S:** gauge invariance requires ∂_tρ + ∂_i∂_jJ_ij = 0, i.e. charge and dipole conservation.
  - Take ρ = T_00. That needs T_0i = ∂_jJ_ij, so total momentum is identically 0 and the energy dipole is frozen. Ordinary moving matter violates this (dD/dt = P).
  - A_ij T_ij alone needs ∂_i∂_jT_ij = 0 identically, so ∂_t²T_00 = 0.
  - **FAIL (iii).**
- **V:** gauge invariance requires ∂_tρ_j + 2∂_iT_ij = 0. With ρ_j = matter momentum density this is momentum conservation, so in the continuum the vector-charge mode can couple to P_j and T_ij.
  - **Universality is then forced (proved, elementary):** the Gauss law ∂_iE_ij = Σ_s κ_s P_s,j is preserved in time only if Σ_s κ_s P_s is conserved. For species that exchange momentum this forces κ_s = κ.
  - But there is no lapse, so there is no coupling to T_00: static matter (P = 0) sources nothing, and there is no Newtonian potential.
  - The dispersion is k² in the strong class (FAIL (i)).
  - **Suggested:** on Z³ there is no exactly conserved local momentum density for interacting matter (discrete translations, Umklapp; the repo's Lemma R and K3a are the in-framework versions). The coupling cannot be exact, so the redundancy is broken and the shear mass of §4(c) returns. This is ROUTES F6's "blocked-equivalent" verdict, now with the mechanism explicit.

**Weinberg–Witten (reading plus comparator).**
- WW's premises (a Lorentz-covariant conserved T_μν and Lorentz-invariant one-particle states) fail at the lattice level, so WW does not constrain the lattice model.
- In the IR, S and S-tl are not Lorentz invariant even after the isotropy tunings: they have gapless ±1 (and 0) partners with independent speeds, and the gauge group is not linearized diffeomorphisms. So WW still does not apply.
- For the same reason, Weinberg's soft-graviton universality theorem (which needs Lorentz invariance) does not force universality either.
- The obstruction actually met is the conservation-law mismatch above, not WW.
- For the ±2-only versions (V-tl, VS), a Lorentz-invariant IR would need linear dispersion. That exists only in the weak H_N comparator, which evades WW the way GR does (a gauge-dependent graviton stress).

## 7. Verdict against the FIXED readings

| Version | (i) gapless ±2, linear | (ii) protected (complete list) | (iii) universal coupling to E and p | (iv) tunings ≤ P0 | Probe reading |
|---|---|---|---|---|---|
| S | **PASS with partners** (checked): linear ±2, plus gapless linear ±1 and 0 | **PASS** for gap (proved, complete to degree 4); stable only in the strong class or with P (weak degree-1 CS destabilizes, checked) | **FAIL** (proved, linear coupling class): charges are dipole-conserving fractons; energy cannot be the charge | INCONCLUSIVE (3, or 4 without T/P, speed tunings vs 2 + unproved) | **FAIL** on (iii) |
| S-tl | PASS with ±1 partners (checked) | PASS (same) | **FAIL** (same) | INCONCLUSIVE (same) | **FAIL** on (iii) |
| V | **FAIL** (checked): ω ∝ k² in the strong class; linear only with weak h:R, which destabilizes helicity 0 or helicity 2 | PASS for gap (proved) | Continuum: momentum and stress only (universality forced); no energy coupling. Lattice: not exact (suggested) | n/a | **FAIL** on (i) (and (iii) for energy) |
| V-tl | **FAIL** (checked): k³ strong; k² with P-even weak term; P-odd weak term unstable | PASS for gap (proved) | as V | n/a | **FAIL** on (i) |
| VS | FAIL in the strong class (landed 09-14 bounded theorem, re-cited, not recomputed); linear only in the weak H_N comparator, which has an indefinite scalar under finite penalties | (landed) | needs lapse coupling to T_00; not done here | n/a | FAIL on (i), strong class (prior art) |

**Probe R2 overall: FAIL**, bounded to linearized rank-2 symmetric-tensor U(1) models on Z³ (scalar charge, vector charge and their traceless variants; quadratic Hamiltonians complete to degree 4, or 6 for V-tl; cubic O symmetry; linear matter-coupling class).
- No version meets (i) and (iii) together. The versions with a linear helicity-2 mode protected by the redundancy couple to fracton (dipole-conserving) charge, not to energy and momentum. The version whose charge can be momentum has ω ∝ k², no energy coupling, and needs an exactly conserved lattice momentum density, which interacting lattice matter lacks.
- Protection itself, (ii), works as in spin ice. But it protects the mode only from terms built from the redundancy's own charge. Coupling the mode to matter's stress breaks the redundancy and returns P0's two shear numbers (§4(c)).
- The FAIL needs the codex sol referee before it is recorded.

**Against the supervisor's registered expectation:**
- (i) passes only for the scalar-charge versions, with extra helicity-±1 (and 0) partners (as probe 11 of PR #9363 predicted). Vector-type versions give k² and k³.
- (ii) passes as expected, with a new caveat: weak CS-type terms are allowed, since the axioms give no P, and they destabilize.
- (iii) fails, as expected.
- (iv) needs at least 1 speed tuning, as expected; the count is 2 isotropy + 1 match (+1 without T/P).
- So the expectation "INCONCLUSIVE leaning FAIL on (iii)" becomes FAIL on (iii) for this class.

**Strong-word check.**
- "Impossible" is used only for the hopping symbol identity and the S charge/energy mismatch, both inside the stated linear coupling class.
- "Complete" means complete to the stated degree, under cubic O, for translation-invariant quadratic symbols.
- The lattice-momentum (Umklapp) statement is labelled suggested.
- Not tested:
  - nonlinear or compact-phase effects (monopoles);
  - non-quadratic matter couplings;
  - event substrates (that is R3);
  - any framework-native origin of the redundancy (that is R1).

## Files
- `r2_common.py`: the machinery.
- `r2_terms.py` / `r2_terms.out`: term counts.
- `r2_spectra.py` / `r2_spectra.out`: spectra, weak terms and mass terms.
- `r2_tune.py` / `r2_tune.out`: tunings, mixed terms, the BZ check and matter polarization.
- `r2_vtl_deg4.py` / `r2_vtl_deg4.out`: the V-tl P-even degree-4 weak term.
