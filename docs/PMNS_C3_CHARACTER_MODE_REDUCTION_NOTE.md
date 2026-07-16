# PMNS `C3` Character-Mode Reduction
**Type:** bounded_theorem (axiom-reset retag 2026-05-03; was positive_theorem)
**Admitted context inputs:** staggered-Dirac realization derivation target (canonical parent: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`).

**Status:** support - structural or confirmatory support note
**Script:** `scripts/frontier_pmns_c3_character_mode_reduction.py`

## Question

For the supplied reduced-cycle matrix family and the supplied `C3`
character-functional triple, what is the exact Fourier-mode reduction?

## Answer

It is smaller than the raw `3`-real reduced-cycle family.

On the graph-first reduced forward-cycle channel

\[
A_{\mathrm{fwd}}(u,v,w)
=
(u+i v)E_{12}+wE_{23}+(u-i v)E_{31},
\]

the supplied `C3` character-functional triple has discrete Fourier modes

\[
z_0 = w,\qquad
z_1 = u-i v,\qquad
z_2 = u+i v.
\]

Thus this supplied matrix family is parametrized by:

- one real trivial-character amplitude `w`
- one complex nontrivial character amplitude `chi := z_2 = u + i v`

with

\[
z_1=\overline{\chi}
\]

on the residual graph-first antiunitary slice.

## Checked-route boundary

The three named route blocks exercised by the runner annihilate the
nontrivial character coordinate:

\[
\chi = 0
\]

on each of:

- the sole-axiom free route
- the sole-axiom `hw=1` source/transfer route
- the retained scalar route

These are route-wise matrix checks, not an exhaustive current-bank theorem.
They show that the three named examples do not supply a nonzero `chi`; they do
not establish a physical `hw=1` carrier, a Record-compatible readout, or a law
selecting a block or its values.

The corresponding positive bridge target is therefore conditional:

> after a physical carrier/readout and matrix-construction law are supplied,
> derive a state or selector law producing nonzero `chi`.

## Meaning

The exact content is a change of coordinates on a supplied three-real matrix
family. The character transform is invertible, and the residual
swap-conjugation slice makes the two nontrivial modes conjugate. Neither fact
selects a physical matrix or upgrades the supplied functionals to observables.

## Verification

```bash
python3 scripts/frontier_pmns_c3_character_mode_reduction.py
```

Expected:

```text
PASS=15 FAIL=0
```


## Hypothesis set used (axiom-reset 2026-05-03)

Per `MINIMAL_AXIOMS_2026-05-03.md`, this note depends on the **staggered-Dirac realization derivation target**, which is currently an open gate. The note's load-bearing claim defines or relies on fermion fields, fermion-number operators, fermion correlators, fermion bilinears, the staggered Dirac action, the BZ-corner doubler structure, the `hw=1` triplet, charged-lepton sector content, neutrino sector content, quark / hadron content, the Koide / PMNS / CKM observable surfaces, or the Grassmann CAR boundary structure — all of which depend on the staggered-Dirac realization derivation target listed in `MINIMAL_AXIOMS_2026-05-03.md`.

Canonical parent note: `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` (`claim_type: open_gate`). In-flight supporting work (see `MINIMAL_AXIOMS_2026-05-03.md`):

- `PHYSICAL_LATTICE_NECESSITY_NOTE.md`
- `THREE_GENERATION_STRUCTURE_NOTE.md`
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`
- `scripts/frontier_generation_rooting_undefined.py`
- `GENERATION_AXIOM_BOUNDARY_NOTE.md` (preserved)

Therefore `claim_type: bounded_theorem`. Closure of that historical gate alone
would not promote this row: the physical carrier, Record-compatible readout,
matrix-construction, and numerical-selection bridges named above would still
require separate derivations and independent audit.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [pmns_c3_character_holonomy_closure_note](PMNS_C3_CHARACTER_HOLONOMY_CLOSURE_NOTE.md)
- [pmns_current_bank_value_selection_nogo_note](PMNS_CURRENT_BANK_VALUE_SELECTION_NOGO_NOTE.md)
- [pmns_sole_axiom_hw1_source_transfer_boundary_note](PMNS_SOLE_AXIOM_HW1_SOURCE_TRANSFER_BOUNDARY_NOTE.md)
- [staggered_dirac_realization_gate_note_2026-05-03](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
