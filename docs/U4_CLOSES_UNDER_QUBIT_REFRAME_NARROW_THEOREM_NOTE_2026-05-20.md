# U4 Closure Under the 2026-05-20 Qubit Reframe (Narrow)

**Date:** 2026-05-20
**Type:** axiom-unpacking support note (not a new theorem-grade derivation)
**Claim type:** positive_theorem
**Status:** source-side proposal — independent audit lane owns the verdict
**Script:** `scripts/frontier_u4_qubit_reframe_closure.py`
(source-side verifier; PASS=15 FAIL=0 on current source)
**Purpose:** Make explicit that the **U4 bridge** ("the framework's
per-site Hilbert space on the Z^3 substrate IS the Cl(3) faithful
complex irrep on per-site `V`") — open under the pre-2026-05-20 Cl(3)
framing — is **directly given by the qubit-per-site baseline** of
the current Quantum axiom
([`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)).

**Audit-dispatch parent candidate:** If a future independent audit
evaluates whether this U4 closure note is a non-chain-closing
alias/decorative handle, the candidate parent is
[`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md).
This is source-side routing context only; it does not assert an
`audit_status` or `effective_status`.

## Source boundary (2026-06-12)

**Boundary:** axiom-unpacking / renaming support only. The load-bearing move
is the identification of the older U4 bridge with the one-qubit-per-site
baseline already supplied by the accepted axiom wording.

This note may be cited only as a compatibility/alias map: under the qubit
baseline, the older U4 open bridge is no longer a separate input. It may not
be cited as an independent first-principles derivation of the qubit baseline,
of `M_2(ℂ) ≅ Cl(3,0)`, of the unique faithful module, or of any downstream
staggered-Dirac substep beyond this alias map.

Promotion beyond renaming support requires a separate theorem whose proof
does not simply restate the accepted qubit-per-site baseline.

Under the new axioms, U4 is no longer an open admission. The
single-faithful-Cl(3)-module-per-site selection is what the
qubit-per-site baseline *means*.
Conditional sub-claims on a number of substep-1 narrow theorems
become unconditional.

## Honest scope

This note **does not re-derive the qubit-per-site baseline**. It
records the immediate logical consequence: the qubit-per-site baseline
(qubit at every site, equivalently per-site `M_2(ℂ) ≅ Cl(3,0)`)
directly closes the U4 bridge.

If audit-retained, this row supplies a candidate upstream support for
moving the U4-conditional sub-claims of several substep-1 narrow
theorems (`staggered_dirac_substep1_u4_conditional_single_module`,
`staggered_dirac_substep1_grassmann_forcing_bridge`,
`staggered_dirac_substep1_jw_bridge`) from conditional to unconditional
under the current Quantum axiom. It does not by itself close the parent
`staggered_dirac_realization_gate_note_2026-05-03` (which has additional
substeps beyond U4) or retag any downstream row.

## Claim

By the qubit-per-site baseline in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
("At each site `x`, the primitive physical local degree of freedom is
one qubit; equivalently, the primitive one-site operator algebra is
`A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading."):

**Axiom-unpacking statement (narrow).** For every lattice site `x ∈ Z^3`, the per-site
Hilbert space `H_x` is `ℂ²`, the unique faithful complex irreducible
module of the per-site operator algebra `M_2(ℂ) ≅ Cl(3,0)`. The
multiplicity `k(x)` of the per-site Cl(3) module is exactly `1` (a
single faithful complex irrep, not a direct sum).

**Equivalent formulations.** This is the same content as:

- **(U4)** the framework's per-site physical Hilbert space on the Z^3
  substrate IS the Cl(3) faithful complex irrep on per-site `V` (the
  open bridge listed on the pre-qubit-reframe staggered-Dirac gate).
- **(C1)** of `STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17`:
  "if the per-site Hilbert space carries a single faithful Cl(3) module
  (k = 1), then `dim_C H_x = 2` exactly."
- **(D2)** of `CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02`:
  "per-site Hilbert dim = 2 with Pauli realization `γ_i = σ_i`."

Under the qubit-per-site baseline, the conditional in (C1) (`if k = 1`)
is no longer required: the baseline specifies a single qubit per site,
which is precisely the
single-faithful-complex-irrep selection.

## Setup

The pre-2026-05-20 Cl(3) framing carried per-site primitives:
- per-site algebra `A_x = M_2(ℂ) ≅ Cl(3,0)` (real-algebra
  isomorphism, retained via
  [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
  §(K2)+(K3))
- per-site Hilbert `H_x = ?` (open: how `A_x` acts on `H_x`)

The **U4 bridge** under the pre-qubit-reframe framing was the open
identification: "the per-site Hilbert `H_x` is the dim-`2k(x)` Cl(3)
module with `k(x) = 1` (single faithful complex irrep), not a multi-copy
direct sum." Without the qubit-per-site baseline, both `k = 1` and
`k ≥ 2` are admissible Cl(3)
modules (formally represented on the algebraic surface by
[`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md)
§(K4) plus standard semisimple finite-dimensional representation
theory). Selecting `k = 1` required an
additional physical premise — the staggered-Dirac/Grassmann
one-particle-per-site realization — that lived in the open
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03` gate's substep 1.

The current Quantum axiom, introduced by the 2026-05-20 qubit reframe and
carried by the 2026-06-05 three-axiom memo, replaces this two-step
"abstract Cl(3) + open bridge" structure with a single-axiom commitment.

## Step 1 — The qubit-per-site baseline specifies the per-site object directly

The qubit-per-site baseline in `MINIMAL_AXIOMS_2026-06-05.md` reads
(as recorded in the canonical
axiom doc):

> "At each site `x`, the primitive physical local degree of freedom is
> one qubit; equivalently, the primitive one-site operator algebra is
> `A_x ~= M_2(C)`, equivalently `Cl(3,0)` in its real-algebra reading."

The word "qubit" carries content: a qubit is, by standard quantum-
information definition, a 2-dim complex Hilbert space `ℂ²` with the
algebra of bounded operators `M_2(ℂ)` acting irreducibly on it.

So the qubit-per-site baseline **directly specifies**:
- per-site Hilbert `H_x = ℂ²` (dim 2)
- per-site algebra `A_x = M_2(ℂ)` acting irreducibly on `H_x`
- multiplicity index `k(x) = 1` (single faithful complex irrep)

This is not a *derivation* under the baseline; it is the *content* of
the baseline.

## Step 2 — U4 follows immediately

The U4 bridge becomes:

```text
H_x (per-site physical Hilbert)
  = ℂ²                               (by the qubit-per-site baseline)    (1)
  = single faithful complex          (by simple-matrix-algebra theory:
    irrep of M_2(ℂ)                   M_2(ℂ) has a unique faithful
                                      irreducible module up to iso)
  = single faithful complex          (using the baseline's stated equivalence
    irrep of Cl(3,0)                  M_2(ℂ) ≅ Cl(3,0))
```

There is no open admission step. (1) is the axiom content; the unique-
faithful-irrep step is standard finite-dim simple-matrix-algebra theory
(Schur's lemma + Wedderburn).

## Step 3 — Downstream consequences

Under the qubit-per-site baseline, the following sub-claims previously listed as
conditional/open become unconditional:

- **Substep-1 U4 conditional (C1)** of
  `STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17`:
  the `k = 1` selection is given by the qubit-per-site baseline; (C1)
  becomes unconditional.
- **Substep-1 Grassmann-forcing bridge U4 admission** of
  `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16`:
  the per-site identification with the Cl(3) faithful complex irrep on
  the Z^3 substrate is supplied directly by the qubit-per-site baseline.
- **Substep-1 JW bridge U4 admission** of
  `STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17`:
  same as above.
- **Per-site Hilbert dim 2 theorem** of
  `CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02`: derivable
  in one line from the qubit-per-site baseline instead of from the
  Cl(3) per-site uniqueness
  chain.

The staggered-Dirac gate's substep 1 thus has only the cross-site
anticommutation half (JW bridge) and the dimensional-matching half
(Grassmann forcing bridge) as substantive content — the U4 bridge is
no longer open under the qubit reframe.

## What this can support after audit

- **Closure of the U4 conditional on substep-1 narrow theorems** under
  the current Quantum axiom. If retained, the three named substep-1
  notes can be re-audited with their U4 admission marked closed by the
  qubit-per-site baseline,
  potentially promoting their bounded status.
- **Cleaner derivation chain** for downstream notes that previously
  required the Cl(3) per-site uniqueness chain (now: cite the
  qubit-per-site baseline directly).
- **One open piece** of the staggered-Dirac realization gate's substep
  1 (the U4 bridge). The other substeps (Grassmann partition forcing
  from the qubit-per-site plus `Z^3` substrate baseline, Kawamoto-Smit
  taste structure, substrate-fundamentality,
  physical-species bridge) remain in their own scopes.

## What this does not close

- **The staggered-Dirac realization gate itself** — substeps 2, 3, 4
  remain open; substep 1's cross-site anticommutation (JW) and
  dimensional-matching (Grassmann forcing) halves remain in their own
  audit status (addressed via PRs that route their deps through the
  retained `cl3_complexification_split` parent).
- **The Kawamoto-Smit gamma-matrix taste structure forcing from the
  qubit-per-site plus `Z^3` substrate baseline** — this is the
  substantive substep-2 content; the qubit-per-site baseline specifies
  the per-site qubit but not the staggered-Dirac global taste structure.
- **Re-derivation of "M_2(ℂ) has a unique faithful complex irrep"** —
  standard simple-matrix-algebra theory (Schur + Wedderburn), cited.

## Admitted inputs

1. **Qubit-per-site baseline of MINIMAL_AXIOMS_2026-06-05** —
   qubit at every site,
   equivalently per-site `M_2(ℂ) ≅ Cl(3,0)`. The axiom is the input,
   not derived here.
2. **Standard simple-matrix-algebra unique-faithful-irrep result** —
   on `M_d(ℂ)`, the unique (up to isomorphism) faithful irreducible
   complex module is `ℂ^d`. Standard finite-dim representation theory
   (Schur's lemma + Wedderburn-Artin classification). Cited as named
   non-derivation.

## Risk classification

`positive_theorem` candidate at narrow-theorem granularity. The narrow
contribution is making the U4 closure under the qubit reframe **explicit
and citeable** — recording that the current Quantum axiom retires the
U4 open bridge that the pre-qubit-reframe framing carried.

Granularity matches the retained
`cl3_complexification_split_narrow_theorem_note_2026-05-10` and the
landed Gleason / Busch / Kraus-Choi / Stinespring / Powers /
Tomita / Inner-aut qubit-lattice companions: standard math + framework
axiom applied to make the framework's commitments explicit.

## Citation-graph note

**Upstream framework dependencies** (load-bearing; markdown links):

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — current axiom memo; supplies the Quantum axiom (one qubit per site = `M_2(C)`, equivalently `Cl(3,0)`)
- [`CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md`](CL3_COMPLEXIFICATION_SPLIT_NARROW_THEOREM_NOTE_2026-05-10.md) — retained; §(K2) `M_2(ℂ) ≅ Cl(3,0)` real-algebra isomorphism, §(K4) two-dim irrep dimensional readout

**Upstream standard-math imports** (named non-derivation):

- Schur's lemma + Wedderburn-Artin classification for simple matrix algebras
- Standard finite-dim representation theory (any modern algebra textbook)

**Plain-text pointer references** (NOT load-bearing deps):

- `STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` — open-gate parent; substep 1's U4 bridge is the named open piece this note addresses
- `STAGGERED_DIRAC_SUBSTEP1_U4_CONDITIONAL_SINGLE_MODULE_NARROW_BOUNDED_NOTE_2026-05-17.md` — substep-1 conditional sub-claim (C1) becomes unconditional under the qubit-per-site baseline
- `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md` — substep-1 dimensional-matching bridge with U4 admission
- `STAGGERED_DIRAC_SUBSTEP1_JW_BRIDGE_NARROW_THEOREM_NOTE_2026-05-17.md` — substep-1 cross-site anticommutation bridge with U4 admission
- `CL3_PER_SITE_HILBERT_DIM_TWO_THEOREM_NOTE_2026-05-02.md` — pre-reframe theorem now derivable in one line from the qubit-per-site baseline
- `A1_QUBIT_INTERPRETATION_NOTE_2026-05-20.md` — companion meta on the qubit identification
- `MINIMAL_AXIOMS_2026-05-20.md` — historical axiom memo that introduced the qubit-reframe wording, superseded by the current three-axiom memo above

## What this file is not

- Not a re-derivation of the qubit-per-site baseline
- Not a closure of the staggered-Dirac realization gate (other substeps remain open)
- Not a closure of substep-1's cross-site anticommutation or dimensional-matching halves (those are separate narrow theorems)
- Not an automatic promotion of any audited_conditional or unaudited row (auditor-owned)
- Not a numerical-prediction change
