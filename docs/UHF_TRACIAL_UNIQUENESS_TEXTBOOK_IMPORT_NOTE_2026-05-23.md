# UHF Type 2^∞ Unique Tracial State — Textbook Import (Admitted External)

**Date:** 2026-05-23
**Type:** bounded_theorem
**Status:** admitted external import — see `docs/audit/data/external_import_nodes.json`
**Purpose:** Register, as a precisely-cited standard textbook theorem, the uniqueness of the tracial state on the UHF C*-algebra of type `2^∞` and the form of its finite-region restriction. This is a **named non-derivation import**: it makes no framework-specific claim and derives nothing about the qubit-lattice physics. It exists so that framework notes which legitimately rely on this standard operator-algebra fact can cite it as settled textbook upstream rather than re-deriving it or carrying it as a hidden assumption.

## Scope of the import (and only this)

**Imported theorem (standard).** Let `A = ⊗_{n∈ℕ} M_2(ℂ)` be the uniformly hyperfinite (UHF) C*-algebra of type `2^∞` (the inductive limit of `M_{2^k}(ℂ)` under the standard unital embeddings). Then:

1. `A` admits a **unique** tracial state `τ` (a state with `τ(ab) = τ(ba)` for all `a,b ∈ A`).
2. On each finite-level subalgebra `M_{2^k}(ℂ) ⊂ A`, the restriction of `τ` is the **normalized matrix trace** `τ(x) = 2^{-k} Tr(x)`.
3. The GNS representation of `(A, τ)` generates the hyperfinite type II₁ factor.

**Citations (exact).**
- R. T. Powers, *Representations of uniformly hyperfinite algebras and their associated von Neumann rings*, Ann. of Math. 86 (1967) 138–171.
- O. Bratteli and D. W. Robinson, *Operator Algebras and Quantum Statistical Mechanics* I–II — UHF/AF C*-algebra and tracial-state theory.
- Standard finite-dimensional fact: the unique tracial state on `M_d(ℂ)` is `d^{-1} Tr` (used at each finite level).

## What this note does NOT do

- It does **not** claim any of this is derived from A1+A2 or from any framework primitive. It is standard operator algebra, imported as-is.
- It does **not** identify the tracial state with the framework's pre-record reference state, or assign it any physical role. That identification, if made, lives in a separate framework note and must close on its own terms.
- It does **not** assert the framework's lattice is the UHF `2^∞` algebra; a framework note that wants to use this import must itself establish that its finite-region algebras are `⊗ M_2(ℂ)` (which is standard for the qubit lattice) within its own scope.

## Admitted-external-import status

This note is allowlisted in `docs/audit/data/external_import_nodes.json`. Per the carve-out in `AUDIT_AGENT_PROMPT_TEMPLATE.md` §4, a dependent framework note may cite this import as retained-grade upstream **for the stated imported result only** — it does not have to re-derive Powers' theorem. The dependent note's own load-bearing step must still close, and may use the import only within the scope above.

The load-bearing move in *this* note is a definitional registration of a standard theorem (it is, deliberately, not a first-principles derivation), so this note's own audited status is not the point — the carve-out is about whether *dependents* may cite it.
