# FS: Building R (Reflection-Positivity Selects Fermionic) + a Tightness Review of Every Chain Link

**Date:** 2026-06-06
**Claim type:** bounded_theorem (builds the RP-selection step R; audits each link of the FS chain)
**Status:** review-loop source proposal. Adds **no axiom**, no fitted input, no audit
verdict.
**Primary runner:**
[`scripts/frontier_fs_reconstruction_R_and_link_review_2026_06_06.py`](../scripts/frontier_fs_reconstruction_R_and_link_review_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_fs_reconstruction_R_and_link_review_2026_06_06.txt`](../logs/runner-cache/frontier_fs_reconstruction_R_and_link_review_2026_06_06.txt)

---

## Role

Two jobs, per the owner request "build it [R], but review every link to make sure
it's absolutely tight":

1. **Build R** — the reflection-positivity / OS-positivity **selection step**.
2. **Review every link** A, B, C, D, R of the chain
   "FS = forced-modulo realization gate + emergent-Lorentz + R" for tightness, with explicit
   verification and an honest status.

## (R) The reflection-positivity selection — built (runner BUILD R)

**Given** the relativistic spin-1/2 (Dirac) structure, positivity selects fermionic:

- **Fermionic** (anticommutators): the negative-energy Dirac solutions are Pauli-
  reinterpreted as antiparticles, `H = E(a†a + b†b) ≥ 0`, all states positive-norm —
  **reflection-positive** (via OS reconstruction). Verified.
- **Bosonic** (commutators): no Pauli reinterpretation; the negative-energy branch
  persists, `H = E(a†a − b†b)` is **unbounded below** — RP/positivity **fails**.
  Verified.
- Microcausality (Pauli, comparator): for spin-1/2 the **anticommutator** is the
  causal one (vanishes at spacelike); the commutator is acausal — the other half of
  the spin-statistics connection.

**R is non-circular.** It *derives* the exchange sign from positivity + the Dirac
spin-structure; it does **not** presuppose the sign. `S(p) = (−iγ·p + m)/(p²+m²)`
supplies the **spin** (the `γ·p` kinematics), and RP supplies the **statistics** (the
relative particle/antiparticle sign). The only thing presupposed is the **continuum
Dirac structure** — which is upstream (Link C + the boost-spinor), not R itself.

## (Review) Tightness of every link

| Link | Content | Verification (runner) | Status |
|---|---|---|---|
| **A** | qubit spin-1/2 (rotation) | Casimir `Σ(σ_i/2)² = ¾ I`; `S₃ = −(i/2)σ₁σ₂` = the Cl(3) bivector | **TIGHT** (rotation spin-1/2; the *boost* is not from A → C) |
| **B** | algebra-3 = spatial-3 | 90°-z rotation conj: `Uσ_xU† = σ_y`, `Uσ_yU† = −σ_x` (O_h vector rep on the Pauli vectors — the *abstract* Clifford triple) | **abstract O_h vector rep: TIGHT**; the *algebra-3 = spatial-3 identification* remains **conditional on the staggered/Kähler-Dirac realization gate**, see the 2026-06-08 correction below |
| **C** | emergent Lorentz | (target; `emergent_lorentz_invariance` retained_bounded; full Lorentz conditional, leading LV dim-6) | **NOT TIGHT** — the single open link; the **boost-spinor** lives here |
| **D** | spin-statistics engine | = BUILD R (a spin-1/2 bosonic field is positivity-inconsistent) | **TIGHT** (rigorous; Pauli/Streater–Wightman/OS) |
| **R** | RP-selection given C | the BUILD R computation above | **TIGHT given C**; non-circular |

**3 of the 5 links are tight (A, D, R).** Beyond the abstract O_h vector rep, the **algebra-3 = spatial-3 *identification* (Link B) remains a realization-gate residual** (see the 2026-06-08 correction below), alongside **C (emergent Lorentz)
+ the boost-spinor** (the relativistic upgrade of the *retained discrete* spin-1/2
rotation structure of A/B).

## Verdict

- The chain is **tight except Link B (the algebra-3 = spatial-3 realization-gate identification) and
  Link C**. R (built) closes the **sign** given C, so
  **FS = forced-modulo {identification B (the staggered/Kähler-Dirac realization gate) + emergent
  Lorentz + boost-spinor}** — C and the boost-spinor are framework **targets**; **no new axiom or
  primitive** is added.
- **Refinement of the earlier "R is circular":** R's RP-selection is **non-circular**.
  The circularity flagged previously was misattributed to R; it actually lives
  **upstream in C** (delivering the continuum Dirac structure / boost-spinor from the
  lattice). So R is not the bottleneck — **emergent Lorentz is.**
- **No new gap** was found by the review beyond the already-named C + boost-spinor and the
  Link-B identification re-tagged in the 2026-06-08 correction below.

## 2026-06-08 Correction — Link B "TIGHT (discrete)" was an over-read

The original Link-B status ("TIGHT (discrete)") conflated two distinct claims. The runner
verification (and the cited authorities `cl3_oh_cubic_lift`,
`internal_external_su2_merger`) establish only the **abstract** fact: the cubic point group
`O_h` lifts to act on the **abstract `Cl(3)`/Pauli generator triple** as the vector rep (inner
automorphisms of `M₂(ℂ)`). They do **not** establish the **external identification** that the
abstract Clifford-3 *is* the spatial `Z³` lattice-3:

- the merger note's **Reading Rule** forbids citing it "to obtain lattice discreteness,
  translation primitives, cubic Bravais structure," and its *What This Does Not Claim* states
  it "does not identify cubic lattice primitive translation axes";
- the d=3 panel closure (#2559) ruled `M₂(ℂ)=Cl(3,0)=GA(3)` a **matched-pair consistency, not a
  derivation** (`d=3` is a `Z³` primitive);
- this note supplies no separate theorem that the Clifford/derivative index of the
  Kähler-/staggered-Dirac operator is the spatial lattice edge direction. That identification is
  the realization gate left open here, not a consequence of the three baseline axioms by itself.

**Corrected reading:** the *abstract* O_h vector rep on the Clifford triple is **tight**
(= the "forced-given-B" content); the *identification* algebra-3 = spatial-3 is **conditional
on the staggered/Kähler-Dirac realization gate**, NOT tight. Downstream notes
must cite Link B only for the abstract O_h vector rep, **not** as supplying the
external-spacetime identification. This does not overturn the chain's core (FS is not a
free-standing new-axiom admission); it re-tags one over-read and adds B to the residual.

## Honest scope

- "Build R" here = the **RP-selection step** (tight, non-circular). It is **not** a
  full lattice→continuum reconstruction; delivering the continuum Dirac structure
  (the boost-spinor + emergent Lorentz) is Link C, the genuine open target. R is built
  to the extent it is buildable without C.
- The energy-positivity computation is the OS-equivalent of reflection positivity
  (positive metric + bounded-below energy); the explicit Euclidean OS Gram and the
  Pauli–Jordan microcausality are cited as the rigorous comparators, with the energy
  form computed here.
- No new axiom. Emergent Lorentz remains a target (bounded-conditional); the live
  blocker for it is the `audited_failed` reflection-positivity Wilson-temporal-gauge
  bridge.

## Reprove-and-cite ledger

- **Reproven here** (runner): the Dirac fermionic-vs-bosonic energy positivity (RP via
  OS); LINK A Casimir ¾ and `S₃ = −(i/2)σ₁σ₂`; LINK B O_h vector rep on the Pauli
  vectors; the link tightness map.
- **Cited**: `per_site_su2_spin_half`, `internal_external_su2_merger`,
  `cl3_oh_cubic_lift`, `emergent_lorentz_invariance`,
  `fs_forced_modulo_emergent_lorentz_stress_test`; literature Pauli 1940,
  Osterwalder–Schrader 1973 (fermions), Streater–Wightman (comparators).

## Audit dependency repair links

- [FS_FORCED_MODULO_EMERGENT_LORENTZ_STRESS_TEST_NOTE_2026-06-06.md](FS_FORCED_MODULO_EMERGENT_LORENTZ_STRESS_TEST_NOTE_2026-06-06.md)
- [AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
