# Naimark Dilation of a POVM — Textbook Import (Admitted External)

**Date:** 2026-05-23
**Type:** bounded_theorem
**Status:** admitted external import — see `docs/audit/data/external_import_nodes.json`
**Purpose:** Register, as a precisely-cited standard textbook theorem, the Naimark dilation of a POVM and the canonical-dilation Kraus form for a projective measurement. This is a **named non-derivation import**: it makes no framework-specific claim. It exists so that framework notes which rely on the canonical Naimark/Lüders dilation can cite it as settled textbook upstream rather than carrying it as a hidden assumption.

## Scope of the import (and only this)

**Imported theorem (standard).** Let `{E_r}` be a POVM on a Hilbert space `H_S` (`E_r ≥ 0`, `Σ_r E_r = 𝟙`). Then:

1. **Naimark dilation.** There exist an ancilla space `H_A` with orthonormal basis `{|r⟩_A}`, a unit vector `|0⟩_A ∈ H_A`, and a projective measurement `{𝟙_S ⊗ |r⟩⟨r|_A}` together with an isometry `V : H_S → H_S ⊗ H_A` such that `⟨ψ| E_r |ψ⟩ = ‖(𝟙_S ⊗ ⟨r|_A) V |ψ⟩‖²` for all `|ψ⟩`. Equivalently, the POVM is the compression of a PVM on the dilated space.
2. **Canonical dilation of a projective measurement.** If the POVM is itself a projective measurement `E_r = P_r` (orthogonal projections, `Σ_r P_r = 𝟙`), the canonical dilation `U_int(|ψ⟩_S ⊗ |0⟩_A) = Σ_r (P_r|ψ⟩)_S ⊗ |r⟩_A` is unitary, and the associated Kraus operators are `K_r = (𝟙_S ⊗ ⟨r|_A) U_int (𝟙_S ⊗ |0⟩_A) = P_r`.
3. **Frame freedom.** Replacing `U_int` by `(U_S ⊗ V_A)·U_int` yields Kraus operators `K_r = U_S P_r` for the same POVM (Stinespring/dilation freedom): different dilations of the same channel are related by a partial isometry on the dilation space.

**Citations (exact).**
- M. A. Naimark, *Spectral functions of a symmetric operator*, Izv. Akad. Nauk SSSR Ser. Mat. 4 (1940) 277–318.
- A. S. Holevo, *Probabilistic and Statistical Aspects of Quantum Theory*, Ch. III (Naimark/dilation theory).
- J. Watrous, *The Theory of Quantum Information*, Sec. 2.4 (Naimark/Stinespring representations).
- W. F. Stinespring, *Positive functions on C*-algebras*, Proc. AMS 6 (1955) 211–216 (dilation freedom).

## What this note does NOT do

- It does **not** claim any of this is derived from A1+A2 or from any framework primitive. It is standard measurement theory, imported as-is.
- It does **not** *select* `K_r = P_r` as the framework's instrument or assert it is the physically correct frame. That selection/derivation lives in a separate framework note (the LSP-projective derivation), which must argue the frame choice on its own terms; this import only supplies that the canonical dilation has Kraus form `P_r` and that `U_S·P_r` are the frame alternatives.
- It does **not** address non-projective POVM instrument selection, sequential-product non-uniqueness, or apparatus back-action.

## Admitted-external-import status

This note is allowlisted in `docs/audit/data/external_import_nodes.json`. Per the carve-out in `AUDIT_AGENT_PROMPT_TEMPLATE.md` §4, a dependent framework note may cite this import as retained-grade upstream **for the stated imported result only** — it does not have to re-derive Naimark/Stinespring. The dependent note's own load-bearing step (e.g. *why* the canonical frame is the framework's choice) must still close, and may use the import only within the scope above.

The load-bearing move in *this* note is a definitional registration of a standard theorem, so this note's own audited status is not the point — the carve-out is about whether *dependents* may cite it.
