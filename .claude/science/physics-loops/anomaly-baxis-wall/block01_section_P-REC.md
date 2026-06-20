# Block01 Section — Edge P-REC (chirality / staggered-eps -> spacetime gamma_5)

**Keystone:** `anomaly_forces_time_abj_inconsistency_accepted_premise_bridge_bounded_note_2026-05-26` (fanout 1105), step B4.
**Edge role:** identify the staggered epsilon carrier with a spacetime Clifford gamma_5 on the irreducible Dirac factor. Declared premise; not derived in the bridge.
**Scope:** A_min (Lattice+Quantum+Record) + the four approved primitives in `docs/audit/data/axiom_premise_nodes.json`. No new axiom/primitive introduced.
**Runner:** `scripts/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.py`
**Cache:** `logs/runner-cache/frontier_abj_prec_r4_taste_reconstruction_2026_06_20.txt`
**Runner result:** `TOTAL: PASS=43 FAIL=0` (exit 0).

---

## Headline (read this first)

R4 does **NOT** crack P-REC. **No campaign pivot.** The honest finding is the opposite of a closure and stronger than the prior wall: the positive R4 taste-reconstruction map now **provably exists and is exact** (the blocked free staggered carrier reconstructs to four identical irreducible Dirac factors, and `Gamma_5^spin` maps exactly to the irreducible-factor chirality `gamma_5^Dirac (x) 1_taste`), AND `Gamma_5^spin` is an **exact chirality operator for the free massless staggered Dirac operator** (`{Gamma_5^spin, D_red(m=0,p)} = 0`). So the entire **free algebraic/kinematic** content of P-REC is now closed, in-tree, at machine precision.

The wall is therefore sharpened from "soft wall, live escape R4" to a **single named missing object**: the **gauged/interacting single-taste selector**. The free reconstruction produces a full `M_4(C)` taste commutant of **exact symmetries of `D_red(m,p)` for all p**, so no single taste is preferred; two genuinely distinct rank-4 single-taste projectors are both equally invariant. Picking one is a **selection**, which under the `realized_state_primitive` counterfactual clause is **registered data, not a derivation** — and the selector itself is not supplied by A_min (it requires interacting/gauged dynamics + taste restoration + OS/continuum reconstruction). This is a genuinely **new hard wall** at the interacting single-taste-selection step; the repo **exercise skill should be run on it**.

---

## What was absorbed (cited, not rebuilt)

Both in-flight P-REC branch artifacts live only on their own branches (absent from this branch / main); their facts were **recomputed in-tree** by my runner, not blind-cited:

- **`origin/codex/abj-prec-spintaste-core-20260618`** — `ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md` + runner (reported PASS=12). Positive core: the four 16x16 staggered-phase flip matrices `alpha_mu` form `Cl_4`, generated spin algebra rank 16 with 16-dim taste commutant, `Gamma_5^spin = alpha_0 alpha_1 alpha_2 alpha_3` is a taste-singlet spacetime gamma_5; epsilon is taste-dressed (not +/-G5, residual 4.0 outside `Cl_4`, commutator 0.375 with taste commutant). **Re-verified in-tree (PART 0/1/2):** Cl_4 residual 0.0, spin-dim 16, taste-commutant dim 16, G5 commutes with full taste commutant (1.2e-15), epsilon residual 4.0, epsilon-taste commutator 0.375.
- **`origin/physics-loop/abj-gamma5-boundary-20260617`** — `ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17.md` + runner (reported PASS=52). Negative boundary: NG-1/NG-2 prune the epsilon=gamma5 shortcut; the factored lemma `{B,sigma_j}=2a sigma_j+2b_j I => B=0`. **Re-verified in-tree (PART 4):** per-site Cl(3) constraint matrix is full rank => only `M=0` anticommutes with all three Pauli (root `NO_PER_SITE_CHIRALITY` reconfirmed).
- **DANGLING-REF FLAG (campaign Decision F):** the spintaste-core note cites `ABJ_STAGGERED_EPSILON_NOT_SPACETIME_GAMMA5_BOUNDARY_NOTE_2026-06-17.md`, which exists only on the gamma5-boundary branch and is **absent from origin/main**. Confirmed absent on this branch. Must be landed together or rewired before consolidation.

Retained authorities (present in-tree, used as source surfaces, recomputed where load-bearing):
- `docs/NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md` (retained_no_go) — root M_2(C) wall: omega = sigma_1 sigma_2 sigma_3 = iI, no nonzero element anticommutes with all three Pauli. **Recomputed (PART 4).**
- `docs/LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md` (bounded_theorem, PASS=54) — supplies the exact `alpha_mu` surface and `D_red(p) = m I_16 + i sum_mu alpha_mu sin(p_mu a)/a`, continuum limit `-> m + i gamma.p` SO(4)-covariant. **This is the surface I attacked R4 on.**
- `docs/CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md` (positive_theorem) — 4th generator via the sign-eps branch; eps=-1 -> Cl(3,1) ~ M_4(R), eps=+1 -> Cl(4,0) ~ M_2(H). Explicitly does NOT derive eps=-1 or reconstruct the staggered carrier. **Recomputed (PART 4).**
- `docs/CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md` (B5 input, EVEN), `docs/STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md` (CHI carrier), `docs/ABJ_EPSILON_INDEX_SQUARE_BLOCK_NO_GO_NOTE_2026-05-30.md` (P-ABJ-relevant; index vanishes on equal-sublattice even tori).

---

## Fresh routes attempted (all in-tree, with explicit residuals)

### R4 (route 1) — ATTACK R4 DIRECTLY: taste-reconstruction map to an irreducible Dirac factor

**Method:** On the canonical blocked free staggered 2^4 hypercube I built `alpha_mu` (Hermitian Cl_4 involutions, `(alpha_mu)_{b xor e_mu, b} = (-1)^{sum_{nu<mu} b_nu}`) and the free staggered Dirac operator at momentum p exactly per the retained SO4 note: `D_red(m,p) = m I_16 + i sum_mu alpha_mu sin(p_mu a)/a`. I then:
1. Tested whether `Gamma_5^spin = alpha_0..alpha_3` is a chirality operator for the operator the anomaly test actually uses.
2. Built the **explicit unitary reconstruction** `W` carrying `alpha_mu -> gamma_mu (x) 1_taste` (one irreducible Dirac factor + 4-dim spectator taste), via the intertwiner space of the two multiplicity-4 `Cl_4` reps.

**Result (SUCCEEDED as a positive free-theory theorem):**
- `{Gamma_5^spin, D_red(m=0,p)} = 0` exactly (residual 0.0) — `Gamma_5^spin` **IS** a chirality operator for the free massless staggered Dirac operator. With mass, `{G5, D_red(m,p)} = 2 m G5` exactly (residual 0.0) — only the mass term breaks chirality, the standard situation.
- Intertwiner space of `{alpha_mu}` vs `{gamma_mu (x) 1_taste}` has dimension **16 = M_4(C)** (residual 0.0) => the two reps are unitarily equivalent.
- **Explicit unitary `W`** found: `W alpha_mu W^dag = gamma_mu (x) 1_taste` (residual **1.9e-15**), and under it `W Gamma_5^spin W^dag = gamma_5^Dirac (x) 1_taste` (residual **2.4e-15**). The blocked carrier reconstructs to **four identical irreducible Dirac factors whose chirality is exactly `Gamma_5^spin`.**

This is **more than the spintaste-core branch had**: it not only exhibits the taste-singlet `Gamma_5^spin`, it produces the explicit reconstruction map and verifies `Gamma_5^spin` is the chirality of the free Dirac operator — the full kinematic content of B4 in the free theory.

**Result (the WALL, PART 3.5):** the reconstruction is FREE and gives a full `M_4(C)` taste commutant that are **exact symmetries of `D_red(m,p)` for all p** (residual 1.6e-15). The carrier splits into **4 degenerate taste sectors with no preferred one**; two **distinct, orthogonal rank-4 single-taste projectors** are both invariant under all `alpha_mu` (commutator 1.3e-15, overlap ~0). So a "single-taste gamma_5 sector" is **selector-dependent**. Under `realized_state_primitive`'s counterfactual clause, a quoted single-taste chirality is **registered data, not a derivation**. The free algebra **does not force** the single-taste selection.

### R2 (route 2) — CL3_TO_CL31 4th generator JOINED to a single-taste selector

**Method:** reconfirm the root no-go (per-site Cl(3) has no gamma_5), adjoin the 4th generator via the retained `CL3_TO_CL31` sign-eps branch, test whether the gauged/interacting identification follows.

**Result:** per-site Cl(3) constraint matrix full rank => only `M=0` anticommutes with all three Pauli (residual 0.0, root `NO_PER_SITE_CHIRALITY` reconfirmed). Adjoining `e_4` with eps=-1 gives Cl(3,1) whose volume element anticommutes with the three spatial generators (residual 0.0) — **a finite gamma_5 exists algebraically.** BUT: (a) the eps=+1 branch (Cl(4,0) ~ M_2(H)) is a **distinct** extension, so the Lorentzian sign eps=-1 is an **admitted/delegated** input per the CL3_TO_CL31 note's own scope, not derived here; (b) the identification still requires the **same unforced single-taste selector** as R4. **R2 reduces to the R4 wall.** No closure.

### R3a (route 3) — Adams-style taste-singlet staggered index as chirality witness

**Method (functional-calculus-correct):** the index grading must be a **function of the generators**, i.e. in `{alpha}'' = {f(alpha)}` (spectral/polynomial), NOT span{I,G}. Test membership; compute the naive index; test what a nonzero index requires.

**Result:** `Gamma_5^spin` IS in `{alpha}''` (it is a polynomial product, residual 0.0); epsilon is NOT (residual 4.0) — so epsilon **cannot** be the index grading, confirming the correct algebra. Naive `Tr[Gamma_5^spin] = 0` on the even 2^4 carrier (residual 0.0) — reproducing the square-block no-go content (index vanishes on equal-sublattice even tori). A nonzero taste-singlet index requires an **imposed chi!=0 / Q!=0 background** (demonstrated: imbalanced mode space gives index 2); the **free framework on the even torus supplies none**. R3a **re-targets, does not close** — it leaves a genuine open ray (curved/imbalanced complex), the SAME ray flagged for P-ABJ.

---

## Algebra discipline applied (B-AXIS lessons)

1. **Did not under-scope to bare 3-axioms:** loaded the four approved primitives; the wall is stated against A_min + primitives, and the missing object (interacting single-taste selector) is explicitly outside what `minimal_axioms`, `scale_reference_primitive`, `kinetic_isotropy_primitive`, `realized_state_primitive` supply.
2. **Correct "is X a function of G" algebra:** tested membership in `{alpha}'' = {f(alpha)}` (functional calculus), not linear span — that is exactly what separates `Gamma_5^spin` (in the algebra) from epsilon (taste-dressed, residual 4.0).
3. **Realized-state counterfactual clause:** the single-taste chirality is invariant over NO law-admissible family (two distinct invariant taste projectors), so it is **registered data**, not a derivation — load-bearing for the wall.
4. **New hard wall => exercise-skill flag (not a bare no_go):** the interacting single-taste selector is a genuinely new wall (R4 fully closed the free kinematics, isolating it). **Run the repo exercise skill on the interacting/gauged single-taste-selection step.**

---

## Verdict for P-REC

- **Arithmetic core:** **CLOSABLE bounded theorem (now stronger than the prior partial closure).** Free taste-reconstruction map `W` exists exactly; `Gamma_5^spin` is the chirality of the free massless staggered Dirac operator; it reconstructs to `gamma_5^Dirac (x) 1_taste`. Deps are all retained (the SO4 2-point note + Cl_4 algebra), so per the **SM_ANOMALY_CLOSURE precedent** this core is **bankable WITHOUT routing through the unaudited keystone** — package it deps-all-retained, named-conditional on the carrier choice, for audit-lane retention.
- **Physical identification:** **WALLED**, sharpened to a single named object — the **gauged/interacting single-taste selector** (plus the admitted Lorentzian sign-eps via CL3_TO_CL31, plus the missing chi!=0 background for the index route). Not supplied by A_min. **R4 does not crack P-REC.**
- **Wall texture:** still **softer than P-HY/P-COMP** (the escape is concrete and named), but R4's free half is now exhausted/closed, so the remaining wall is a genuine new hard wall at the interacting-selection step — warrants an **exercise-skill run**, not a bare no_go.
