# FS Stress-Test: the Fermion Sign is Forced-Modulo Realization Gate + Emergent-Lorentz + R

**Date:** 2026-06-06
**Claim type:** open_gate / conditional-support stress-test
**Status authority:** independent audit lane only. This source note adds **no
axiom**, no fitted input, and no audit verdict. It records a conditional route
map and finite stress-test for the same-day
`SPIN_STATISTICS_FS_ADMISSION_LOCATED_EXERCISE_NOTE_2026-06-06`, not a closed
FS-forcing theorem.
**Primary runner:**
[`scripts/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.py`](../scripts/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.txt`](../logs/runner-cache/frontier_fs_forced_modulo_emergent_lorentz_2026_06_06.txt)

---

## 2026-06-18 Open-Gate Source-Scope Repair

The current audit blocker is the top-level posture, not the finite stress-test
itself. The runner verifies route-map text, a toy spin-1/2 CCR/CAR
energy-sign witness, and multi-loop statistics-blindness witnesses. It does
not derive the realization-gate/external-spacetime identification, emergent
Lorentz/positivity/microcausality, or a non-circular OS-to-Wightman
reconstruction `R`.

This repair therefore makes the auditable source claim an `open_gate`
conditional-support stress-test:

```yaml
actual_current_surface_status: open
conditional_surface_status: conditional-support
target_claim_type: open_gate
proposal_allowed: false
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The surviving statement is exactly:

```text
if Link-B realization-gate/external-spacetime identification,
   emergent Lorentz/positivity/microcausality,
   and non-circular reconstruction R
are supplied, then the comparator spin-statistics engine selects the
fermionic sign; meanwhile the finite graph-braid opening is statistics-blind.
```

No FS closure, new axiom, new primitive, accepted-premise registration, or
effective-status movement is claimed here.

## 2026-06-16 Post-Audit Scope Firewall

Independent audit correctly treated this packet as conditional support rather
than a bounded theorem. The finite runner remains useful as a stress-test: it
checks a toy spin-1/2 CCR/CAR energy-sign witness, verifies that the multi-loop
graph-braid opening is statistics-blind, and records the exact residual route.
It does **not** derive the external Clifford-to-spacetime identification,
emergent Lorentz/positivity/microcausality, or the OS-to-Wightman
reconstruction `R` from the framework baseline.

Accordingly the live source boundary is:

```text
spin-1/2 support + abstract O_h/Cl(3) support
  + supplied realization gate + supplied/emergent Lorentz/positivity
  + supplied reconstruction R
  => fermionic sign forced by the comparator spin-statistics engine.
```

This is a conditional route map and finite stress-test, not closure of FS and
not a new axiom. The static baseline remains open to the hard-core boson until
the realization/Lorentz/`R` chain is derived or otherwise admitted by retained
authority.

## Role

The repo's `/exercise` skill (5-subagent fan-out + literature) run as a
**stress-test** of the prior conclusion "FS (the cross-site fermion exchange sign)
is an irreducible admission," under the owner constraint: **introduce no new
axiom or primitive** unless genuinely forced.

## Refined route map (runner SCORECARD 23/23 PASS)

**The current route adds no new axiom or primitive.** It reclassifies from
"irreducible admission" to **forced-modulo realization gate + emergent-Lorentz + R**:
conditional on the Link-B realization-gate identification, a framework **target**
(emergent Lorentz), and a buildable reconstruction `R`, not on a new axiom. The
static "admission" reading is correct for `{Lattice, Quantum, Record}` *alone*, but
it abstracts away the spin-1/2-ness of the qubit, the realization gate, and the
emergent-Lorentz continuum.

### The forcing chain

| Link | Content | Repo status |
|---|---|---|
| **A** | the qubit carries spin-1/2 | **retained** (`per_site_su2_spin_half`); the rotation su(2) `S_i=σ_i/2` *are* the Clifford Spin(3) bivectors (`internal_external_su2_merger`, retained_bounded) |
| **B** | algebra-3 = spatial-3 | **abstract O_h vector rep: supported** (`O_h` acts on the *abstract* Cl(3) by the vector rep; qubit = 2D spinor, `2π=−1`; `cl3_oh_cubic_lift`). The *algebra-3 = spatial-3 identification* remains **conditional on the staggered/Kähler-Dirac realization gate** (see the 2026-06-08 correction), so the identification is part of the residual with C |
| **C** | emergent Lorentz | framework **target** / bounded-conditional (`emergent_lorentz_invariance` retained_bounded) — **not a new axiom** |
| **D** | spin-statistics theorem (engine) | **rigorous comparator**: a spin-1/2 field quantized bosonically is inconsistent (energy unbounded below / trivial field; Pauli 1940, Streater–Wightman). So spin-1/2 + Lorentz + positivity ⟹ **fermionic forced**; the hard-core **spin-0** boson is excluded |

Verified in the runner: the spin-1/2 CCR attempt has a `−E` mode (unbounded below),
while the spin-1/2 CAR spectrum is `≥ 0` — the engine's content.

**The residual** is the *identification* Link B (the staggered/Kähler-Dirac realization gate;
see the 2026-06-08 correction), its continuum upgrade (= Link C), plus the
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
closer is **graded locality / fermion-parity superselection** — a sign-selection
on the retained `Z₂` fermion-parity grading
(`fermion_parity_z2_grading_theorem`). That would still be an extra theory
principle if invoked; it is **not currently forced** (the continuum/`R` route
remains open), so it should not be invoked prematurely or attributed to Record.

## Owner bottom line

- **No new axiom or primitive is added on the current route.** FS rides on the
  realization-gate residual + **emergent Lorentz** (a framework target) + the
  reconstruction **`R`** (buildable), fed through the standard spin-statistics engine.
- **Reclassify FS:** *forced-modulo realization gate + emergent-Lorentz + `R`* —
  conditional on residual/target surfaces, not a free-standing new axiom.
- The genuine next artifact is **`R`**: prove the relativistic spin-1/2 reconstruction
  (and the reflection-positivity that excludes the bosonic branch) without
  presupposing the sign — the live blocker (cf. the prior failed-attempt
  `..._reflection_positivity_wilson_temporal_gauge_bridge`).

## 2026-06-08 Correction — Link B "retained at the discrete level" was an over-read

The Link-B row originally read "retained at the discrete level" for "algebra-3 = spatial-3".
The cited authority (`cl3_oh_cubic_lift`, with `internal_external_su2_merger`) establishes only
the **abstract** fact — `O_h` lifts to act on the **abstract `Cl(3)`/Pauli generator triple**
as the vector rep (inner automorphisms of `M₂(ℂ)`) — **not** the **external identification**
that the abstract Clifford-3 *is* the spatial `Z³` lattice-3:

- the merger note's **Reading Rule** forbids citing it "to obtain lattice discreteness,
  translation primitives, cubic Bravais structure," and it "does not identify cubic lattice
  primitive translation axes";
- #2559 ruled `M₂(ℂ)=Cl(3,0)=GA(3)` a **matched-pair consistency, not a derivation** (`d=3` is
  a `Z³` primitive);
- this note supplies no separate theorem that the Clifford generator index is the spatial
  lattice-edge index. That identification is exactly the staggered/Kähler-Dirac realization
  gate left open here, not a consequence of the three baseline axioms by itself.

**Corrected reading:** the *abstract* O_h vector rep on the Clifford triple is **supported/tight**;
the *identification* algebra-3 = spatial-3 is **conditional on the realization gate** — so Link B
is **part of the residual** (with C), and the chain reads
**FS = forced-modulo {identification/realization gate + emergent Lorentz (C) + R}**. Downstream notes must
cite Link B only for the abstract O_h vector rep, **not** as supplying the external-spacetime
identification. This re-tags one over-read; it does not overturn the core reclassification (FS
is not a free-standing new-axiom admission).

## Honest scope

Conditional route-map stress-test + refutation of the multi-loop opening +
the cheapest-principle classification — **not** a closure of FS (the
realization-gate/external-spacetime identification, reconstruction `R`, and
emergent Lorentz remain to be built/audited). No new axiom; literature
(Pauli, Streater–Wightman, emergent-Lorentz fixed points, Levin–Wen) is
comparator only.

## Reprove-and-cite ledger

- **Checked here** (runner): a finite toy CCR/CAR energy-sign witness for the
  spin-statistics engine, the multi-loop cocycle statistics-blindness (both
  frames survive), and the link/route classifications. The full spin-statistics
  theorem remains literature comparator context plus repo-local reconstruction work,
  not an imported audit verdict.
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
- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
