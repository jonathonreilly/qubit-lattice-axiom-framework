# FS Stress-Test: the Fermion Sign is "Forced-Modulo Emergent-Lorentz + R", Not a Free Admission Needing a New Principle

**Date:** 2026-06-06
**Claim type:** bounded_theorem (exercise stress-test; reclassifies a prior verdict)
**Status:** review-loop source proposal. Adds **no axiom**, no fitted input, no audit
verdict. Reclassifies (does not overturn the static reading of) the same-day
`SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06`.
**Primary runner:**
[`scripts/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.py`](../scripts/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.txt`](../logs/runner-cache/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.txt)
**Exercise packet:** `.claude/science/exercises/fs-admission-stress-test/`

---

## Role

The repo's `/exercise` skill (5-subagent fan-out + literature) run as a
**stress-test** of the prior conclusion "FS (the cross-site fermion exchange sign)
is an irreducible admission," under the owner constraint: **introduce no new
import/principle/axiom beyond the approved Planck scale-reference primitive** unless
genuinely forced (and then name the single cheapest one).

## Refined verdict (runner SCORECARD 15/15 PASS)

**FS does not require a new principle beyond Planck.** It reclassifies from
"irreducible admission" to **"forced-modulo emergent-Lorentz + R"** — conditional on
a framework **target** (emergent Lorentz) plus a buildable reconstruction `R`, not on
a new axiom. The static "admission" reading is correct for `{Lattice, Quantum,
Record}` *alone*, but it abstracts away the spin-1/2-ness of the qubit and the
emergent-Lorentz continuum.

### The forcing chain

| Link | Content | Repo status |
|---|---|---|
| **A** | the qubit carries spin-1/2 | **retained** (`per_site_su2_spin_half`); the rotation su(2) `S_i=σ_i/2` *are* the Clifford Spin(3) bivectors (`internal_external_su2_merger`, retained_bounded) |
| **B** | algebra-3 = spatial-3 | **retained at the discrete level** (`O_h` acts on Cl(3) by the vector rep; qubit = 2D spinor, `2π=−1`; `cl3_oh_cubic_lift`). Continuum upgrade = Link C — **not the residual** |
| **C** | emergent Lorentz | framework **target** / bounded-conditional (`emergent_lorentz_invariance` retained_bounded) — **not a new axiom** |
| **D** | spin-statistics theorem (engine) | **rigorous comparator**: a spin-1/2 field quantized bosonically is inconsistent (energy unbounded below / trivial field; Pauli 1940, Streater–Wightman). So spin-1/2 + Lorentz + positivity ⟹ **fermionic forced**; the hard-core **spin-0** boson is excluded |

Verified in the runner: the spin-1/2 CCR attempt has a `−E` mode (unbounded below),
while the spin-1/2 CAR spectrum is `≥ 0` — the engine's content.

**The single residual** is the continuum upgrade of Link B (= Link C) plus the
OS→Wightman reconstruction **`R`** (`free_field_os_wightman_reconstruction`,
unaudited), which must deliver the boost-spinor and the antiparticle sign **without
presupposing the fermionic branch** (currently circular — see
`flavor_spin_statistics_forces_modulo_reconstruction`, audited_conditional). Both are
**buildable science, not axioms**.

## The last static opening is refuted

The one un-refuted static opening — the multi-loop graph-braid cocycle (intersecting
Jordan-Wigner-string framings on a Z³ patch) — is **statistics-blind**: a subagent
built it (theta-graph, `β₁ = 3`, no torsion), and both boson (+1) and fermion (−1)
satisfy the multi-loop cocycle `s(L2∘L1) = s(L1)·s(L2)` (the double swap is the
identity permutation = `+1` in both frames). The hard-core boson is **not** frustrated
out. So no static graph-braid route forces the sign.

## The cheapest principle, if ever forced (weaker than an axiom)

If neither the continuum/`R` route nor any static route closes it, the cheapest
closer is **graded locality / fermion-parity superselection** — a *sign-selection
between the two Record-given `Z₂` parity sectors* (the grading is retained;
`fermion_parity_z2_grading_theorem`). It is **weaker than a fresh axiom** (no new
structure — just the sign between two existing sectors, half-implied by Record) and is
**not currently forced** (the continuum/`R` route remains open), so it should not be
invoked prematurely.

## Owner bottom line

- **No new principle beyond Planck is needed.** FS rides on **emergent Lorentz** (a
  framework target) + the reconstruction **`R`** (buildable), fed through the standard
  spin-statistics engine.
- **Reclassify FS:** *forced-modulo emergent-Lorentz + `R`* — conditional on a target,
  not a free-standing admission.
- The genuine next artifact is **`R`**: prove the relativistic spin-1/2 reconstruction
  (and the reflection-positivity that excludes the bosonic branch) without
  presupposing the sign — the live blocker (cf. the audited_failed
  `..._reflection_positivity_wilson_temporal_gauge_bridge`).

## Honest scope

Reclassification + refutation of the multi-loop opening + the cheapest-principle
classification — **not** a closure of FS (the reconstruction `R` and emergent Lorentz
remain to be built/audited). No new axiom; literature (Pauli, Streater–Wightman,
emergent-Lorentz fixed points, Levin–Wen) is comparator only.

## Reprove-and-cite ledger

- **Reproven here** (runner): the spin-1/2 CCR-unbounded-below vs CAR-bounded-below
  engine content; the multi-loop cocycle statistics-blindness (both frames survive);
  the link/route classifications.
- **Cited**: `per_site_su2_spin_half`, `internal_external_su2_merger`,
  `cl3_oh_cubic_lift`, `emergent_lorentz_invariance`,
  `fermion_parity_z2_grading_theorem`, `flavor_spin_statistics_forces_modulo_reconstruction`,
  the four FS no-gos; literature (Pauli 1940; Streater–Wightman; emergent-Lorentz
  fixed points arXiv:1305.0011/1506.07570; Levin–Wen cond-mat/0302460) as comparators.

## Audit dependency repair links

- [SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md](SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06.md)
- [AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md)
- [FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- [SCALE_REFERENCE_PRIMITIVE_NOTE.md](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
