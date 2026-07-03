# Named Hopping Matter-Unitary Primitivity Requires a Presupposed Background Connection

**Date:** 2026-06-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** the matter-realization input of the block-06 color-einselection
unistochastic-irreducibility criterion — whether the single-emergent-time-step
matter color unitary on the supplied `C³` carrier is primitive — resolved for
the two named source-proposal hopping Hamiltonians, with an exhibited
presupposed-connection circularity.
**Script:** `scripts/frontier_color_einselection_matter_unitary_primitivity_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_color_einselection_matter_unitary_primitivity_2026_06_09.txt`
**Status:** source proposal. All statements are finite-dimensional exact algebra
checked by the runner (`PASS=26 FAIL=0`). Authority role: source proposal; the
audit lane sets status.

## The named input this addresses

Block 06
([`COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09`](COLOR_EINSELECTION_POINTER_FRAME_FORK_IS_A_UNISTOCHASTIC_IRREDUCIBILITY_CRITERION_NARROW_THEOREM_NOTE_2026-06-09.md),
PR #3436, source proposal) reduced single-record-frame color depolarization to a
property of the coherent matter color unitary `U` on the `C³` color carrier. For
the predictability-sieve channel `Φ(ρ) = D_B(U ρ U†)` with one **named** record
frame `B` (a frame-naming instrument admission on the `retained_no_go`
record-formation ground;
[`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)),
the color pointer states are the `B`-diagonal states stationary under the
unistochastic matrix `S_ij = |⟨e_i|U|e_j⟩|²`, and `ρ_color` depolarizes to
`I₃/3` under a single record frame **iff** `S` is **primitive** (sufficient:
`U` has no zero amplitude in `B`). Block 06 relocated the relocated-ADM-2 input
onto: **is that matter color unitary primitive?**

This note answers it on the matter-realization lane, for the two named hopping
Hamiltonians of the block-01 composite-link model
([`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md),
source proposal).

## Setting and conditionality (load-bearing, named)

Every statement is conditional on all of:

1. **The supplied `C³` color carrier** (`MR_color` residual;
   [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)).
   Nothing here derives color from the axioms. Color SU(3) is the irreducible
   3-dimensional carrier `V₃ ≅ C³` extracted from the taste cube — **not**
   identified with taste.
2. **A named record frame `B`** on the color carrier (block-02 frame-naming
   instrument; an admission, not delivered by Record).
3. **The two named matter Hamiltonians** (block-01 model), on a few sites:
   - `H_free = κ A ⊗ I₃` — color-diagonal nearest-neighbour hopping (the named
     free source surface: staggered-Dirac hopping acts on the Grassmann fields
     with spatial Kawamoto–Smit phases only and carries **no** color index;
     [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md));
   - `H_cov = κ(|x⟩⟨y| ⊗ V† + |y⟩⟨x| ⊗ V)` — a **frozen, presupposed** generic
     SU(3) link background `V` on the edge.

   The "connection" reading that would make the covariant hopping forced is
   `matter_gauge_minimal_coupling_fiber_frame_forces_connection_...` (PR #3332),
   **unaudited** on the live ledger as of this writing and **not consumed** here.
   Without consuming that unaudited connection reading, the named free lane is
   the color-diagonal `H_free`.

The matter color unitary `U` the sieve sees is the **color action of one
emergent-time hopping step on the carrier**, derived (not assumed) below.

## Verdict (the matter color unitary is the per-edge link `V`)

### 1. Free hopping is color-inert; the induced transporter is the link `V`

`H_free = κ A ⊗ I₃` factorizes exactly: `e^{-iH_free} = e^{-iκA} ⊗ I₃` (runner
D1), so the color factor of every emergent-time step is `I₃` — free hopping
**never rotates the color frame**. More generally, on a two-site edge with link
block, the off-diagonal hopping block squares to the identity, so
`e^{-iH} = cos κ · I − i sin κ · (block)`, and the color of the amplitude that
hops `x→y` is exactly `V|c⟩` (runner D2, derived for both `V = I₃` and a generic
`V ∈ SU(3)`). Hence the matter color unitary the sieve sees is the per-edge link
**`U = V`** (free: `V = I₃`).

### 2. Free verdict: `S = I`, frame `B` einselected, `ρ` stays polarized — and this is FRAME-INDEPENDENT

For `U = e^{iφ} I₃`, `S = |U_ij|² = I` (runner D3). This is block-06's `[U,B]=0`
commuting limit: the **whole** record frame `B` is einselected, every `B`-basis
state is a stable pointer state, and a generic `ρ_color` relaxes to its own
diagonal — it **stays polarized**, it does **not** reach `I₃/3`.

Crucially this verdict is **frame-independent**: `U ∝ I₃` gives `S = I` in
**every** orthonormal frame `B = g{e_i}` (runner D4, 200 random frames; and any
explicitly named random frame `B` leaves `ρ` polarized). No record-frame choice
can make the free matter unitary primitive. The frame-smuggling guard is
therefore satisfied not by frame-dependence but by frame-**independence**: the
free-lane obstruction cannot be evaded by naming a clever frame.

### 3. Covariant verdict: primitive `S` (depolarization) but FRAME-DEPENDENT and presupposing `V`

A generic SU(3) link `V` has strictly positive `S = |V_ij|²` (runner D5), hence
primitive (Perron–Frobenius: a single unit-modulus eigenvalue and a strict
spectral gap `|λ₂| < 1`), so `Φⁿ(ρ) → I₃/3` — depolarization, recovering
block-06's primitive column (runner D5, D7). But:
- the verdict is **frame-dependent**: in the `V`-eigenframe `S = I` (reducible,
  no depolarization; runner D6), so for the covariant unitary the outcome is
  exactly *which frame einselection names* (loops back to instrument admission);
- the link `V ≠ I₃` is a **presupposed background SU(3) connection** — the very
  gauge-link object whose continuous-time dynamics this campaign seeks to induce.

### 4. Circularity gate and the order parameter

In this matter family the induced color unitary is exactly the per-edge link
(§1). The depolarization verdict is therefore a boolean function of the
presupposed link (runner D8, D11):

| matter color unitary | `S = |V_ij|²` | single-frame depolarization |
|---|---|---|
| free `V = I₃` (named free lane, no presupposed connection) | `I` (frame-independent) | **no** |
| covariant `V ∈ SU(3)` (presupposed connection) | primitive (generic frame) | yes, but `V`-eigenframe gives `S=I` |

So matter-lane single-frame depolarization **consumes** a presupposed background
connection: the named color-diagonal free hopping frame-independently does
**not** depolarize. The order parameter `P(ρ) = Tr(ρ²) − 1/3 = ‖traceless(ρ)‖²_F`
(the same as blocks 04/05/06) is preserved under the free step and driven
monotonically to `0` under the covariant step (runner D9).

### 5. Covariance is not contraction (guard, no hat discharged)

The block-03 free transport channel on local color densities
(`M' = cos²τ · M + sin²τ · V M' V†`, `V = I₃` for free hopping) is jointly
SU(3)-covariant yet inert on the color **frame**: it transports color density
between sites without rotating the basis (runner D10). Covariance never implies
depolarization — consistent with block-05 instrument I-B (color-blind = inert)
and block-03's instrument-inherited covariance. No hat is discharged.

## What this means for the four hats

- **ADM-1 (static frame redundancy):** untouched.
- **R1 (continuous-time link generator with arrow + rate):** untouched; not
  delivered.
- **R2 / relocated-ADM-2 (color depolarization that drives the heat-kernel /
  Ad-invariant-measure attractor):** **sharpened and bounded on the matter lane.**
  The relocated input "is the matter color unitary primitive?" resolves on this
  named matter family: the color-diagonal free hopping is frame-independently
  non-depolarizing
  (`S = I`), and the only matter color unitary in the named family that yields a
  primitive `S` presupposes a background SU(3) connection — the gauge link the
  campaign seeks to induce. So depolarization is not delivered by the named free
  matter lane; it is gated by a presupposed connection (a circularity for the
  induce-the-gauge-dynamics goal) or by which frame einselection names.
- **Blocking isometry:** untouched.

No `ST1`/`ST2` ranking is made or implied.

## Honest auditor read

- This is a **bounded obstruction**, not a derivation of depolarization from the
  axioms; it shows the **opposite** on the named free lane (no depolarization)
  and an exhibited circularity on the covariant lane. It discharges no hat.
- The result is conditional on the supplied `C³` carrier, a named record frame,
  and the two named block-01 Hamiltonians. It is not a statement about every
  conceivable matter realization — only that the named color-diagonal hopping
  is color-inert and that primitivity in this family requires `V ≠ I₃`.
- The covariant-lane depolarization is **conditional sufficiency** (a primitive
  `S` does depolarize) fenced behind a presupposed connection; it is explicitly
  **distinct** from the refuted annealed-twirl SUFFICIENCY and is not a delivery.
- `U = V` is the induced single-hop color transporter for this two-site edge
  model; a multi-site / multi-step interleaving could in principle compose links
  into a different effective `U`, but each composed link is itself a presupposed
  background connection on its edge — the circularity is inherited, not removed,
  by composition (the path this opens: quantify the composed-link effective `U`
  on a multi-edge carrier).

## Does NOT establish

- No derivation of color depolarization (`ρ_color → I₃/3`) from the axioms.
- No proof that any realized matter dynamics supplies a nontrivial color link
  `V` without presupposing a background connection.
- No continuous-time link generator (R1); ADM-1, R2-delivery, and the blocking
  isometry are untouched.
- Single-edge / single-frame color carrier; the connection reading (#3332) is
  unaudited and not consumed.

## No-Go Discipline Gate

This section gates the bounded negative leg: in the named hopping matter family,
the free lane is non-depolarizing and the depolarizing covariant lane consumes a
presupposed link.

- **N1 alternative routes:** (1) choose a clever record frame for free hopping —
  ATTEMPTED, fails by frame-independence (D4). (2) use a generic SU(3) link —
  ATTEMPTED, succeeds at depolarization but consumes the presupposed connection
  (D5/D8). (3) use the `V`-eigenframe — ATTEMPTED, gives `S = I` and no
  depolarization (D6). (4) rely on SU(3) covariance alone — ATTEMPTED, free
  transport is covariant but inert (D10). (5) compose multiple edges/steps —
  PARTIAL: possible effective-unitary route, but each nontrivial composed link
  in this model is still built from presupposed edge links; quantifying this is
  future work, not a closed universal no-go.
- **N2 wall independence:** the remaining walls are the supplied `C³` carrier,
  the named frame `B`, the named hopping Hamiltonian family, and the
  presupposed-link input for the covariant lane. None is silently collapsed into
  Record, SU(3) covariance, or the free hopping theorem.
- **N3 hidden-wall scan:** "connection", "record frame", "generic SU(3)", and
  "matter color unitary" are explicit named inputs. Stale retained-grade
  language is avoided; the block-01 and block-06 surfaces are cited as landed
  source surfaces pending independent audit, not consumed as retained-grade.
- **N4 residual matching:** the residual matches block 06 exactly: given a
  named frame, is the coherent matter color unitary primitive? The runner maps
  `U = I₃` to block-06's commuting/no-depolarization column and generic `U = V`
  to its primitive/depolarization column (D7).
- **N5 rhetoric audit:** the negative phrase is scoped to this named
  single-frame, single-edge hopping family. It is not a claim about every
  conceivable matter realization, multi-edge effective dynamics, or a future
  retained connection theorem.
- **N6 partial-closure scan:** a future retained derivation of the connection
  reading could supply `V`; that would move the covariant lane from
  presupposed to derived. This note does not call for a new axiom or primitive,
  and it does not treat an approved primitive as a bounded-status source.
- **N7 steelman:** a hostile reviewer can argue that multi-step matter dynamics
  might generate an effective primitive `U` without a fixed background link.
  Response: this note does not close that route universally; it shows only that
  in the two named block-01 Hamiltonians, the nontrivial color transporter is
  exactly the supplied link `V`.
- **N8 cross-cycle echo:** the result echoes the recent record-frame and
  color-depolarization repairs: a record frame or covariant form is not enough;
  the actual mixing unitary must be supplied or derived. This note preserves
  that boundary instead of promoting a support-only depolarization story.

## Reproduce

```
python3 scripts/frontier_color_einselection_matter_unitary_primitivity_2026_06_09.py
# TOTAL: PASS=26 FAIL=0
```
