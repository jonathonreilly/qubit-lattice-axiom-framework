# Free Dirac Poincaré Generators — Repairing the Common-Analytic-Vector Step via the Nelson Commutator Theorem (Repairs the `audited_failed` Self-Adjointness Note)

**Date:** 2026-06-06
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The `bounded_theorem` label is a source-side
claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_dirac_poincare_selfadjointness_nelson_commutator_repair_2026_06_06.py`](../scripts/frontier_dirac_poincare_selfadjointness_nelson_commutator_repair_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_dirac_poincare_selfadjointness_nelson_commutator_repair_2026_06_06.txt`](../logs/runner-cache/frontier_dirac_poincare_selfadjointness_nelson_commutator_repair_2026_06_06.txt)

---

## Role

This note **repairs** the `audited_failed` bounded theorem
[`FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md`](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)
(`free_dirac_poincare_generators_essential_selfadjointness_bounded_note_2026-05-30`),
the functional-analysis lemma that discharges the unbounded-generator
integrability technicality (T1) of the free Dirac Poincaré representation — the
**boost-spinor** self-adjointness that the FS / emergent-Lorentz chain (the
review note `FS_RECONSTRUCTION_R_AND_TIGHT_LINK_REVIEW_NOTE_2026-06-06.md`, named
in plain text to avoid a premature citation-graph edge) names as the live blocker
in Link C. The independent audit returned
**audited_failed**:

> "N2 verifies only `K = -i d/dζ` on rapidity Gaussians through `n ≤ 12`, while
> the source note uses those vectors to claim analyticity for `H`, `P`, and the
> Nelson Laplacian. That displayed bridge is mathematically false as written, so
> S-ii and the S-iii integration claim do not follow."

**The audit is correct.** This note (i) confirms and *locates* the false step,
(ii) keeps the parts that were sound, and (iii) replaces the broken
common-analytic-vector argument with the standard, correct tool — the **Nelson
commutator theorem** — which establishes essential self-adjointness and group
integrability **without** any hand-picked common analytic vectors. Runner:
**12 PASS / 0 FAIL**.

## 0. What was sound, and what was false

- **Sound (kept): S-i — each generator is individually essentially self-adjoint.**
  `H = E(p)` and `P^i = p^i` by the multiplication-operator criterion; `J^i` by
  the compact rotation group; the unbounded non-compact **boost** `K^i` by the
  *exact* rapidity reduction `K_{orb} = -iE\,\partial_p = -i\,d/d\zeta` to the
  textbook self-adjoint momentum operator on the line. The audit did **not**
  dispute S-i, and the rapidity reduction is genuinely correct.
- **False (repaired): S-ii — the rapidity-Gaussian as a *common* analytic vector.**
  The note used the rapidity-Gaussian `ψ_a(ζ) = e^{-aζ²/2}` and claimed it is
  analytic for all ten generators *and* the Nelson Laplacian. It is **entire** for
  `K = -i\,d/d\zeta` (a translation generator), but **not analytic for `H`**:
  in rapidity coordinates `H = M_⊥\cosh\zeta`, so

  ```text
      ‖H^n ψ_a‖ / n!  ~  e^{n²/2a}      (super-factorial)  ⟹  Nelson series DIVERGES.
  ```

  The runner (Part A) computes both ratios exactly: `‖K^n ψ‖/n!` falls monotonically
  to `5.9×10⁻⁴` at `n=8` (entire), while `‖H^n ψ‖/n!` exceeds `10¹⁰` already at
  `n=5` and runs off to `inf`. **No single Gaussian can be analytic for both `K`
  (which wants flat rapidity → Gaussian in `ζ`) and `H` (which wants a Gaussian in
  `p`, since `H ~ |p|` there).** So S-ii — and therefore the S-iii integration that
  rested on it — does not follow, exactly as the audit said.

## 1. The repair — Nelson commutator theorem (no common analytic vectors needed)

The correct, standard route to essential self-adjointness and integrability for a
Lie-algebra representation by unbounded operators is the **Nelson commutator
theorem** (Reed–Simon II, Thm X.37; Nelson 1959; Faris–Lavine), which uses a
single self-adjoint **comparison operator** `N` and *form bounds*, not explicit
common analytic vectors. Take

```text
    N  =  momentum-space harmonic oscillator  =  -d²/dp² + p² ( + const )  ≥ 1,
```

whose operator core is the **Hermite functions = the Schwartz space `S`** — a
genuine common invariant core for all the generators. For each generator
`G ∈ {H, P, K}` we verify the two hypotheses of X.37:

```text
    (i)   ‖G ψ‖ ≤ c₁ ‖N ψ‖                                  (N-boundedness)
    (ii)  |⟨G ψ, N ψ⟩ − ⟨N ψ, G ψ⟩| ≤ c₂ ⟨ψ, N ψ⟩            (commutator form-bound:
          equivalently the operator inequality  −c₂ N ≤ i[G,N] ≤ c₂ N).
```

**Theorem (X.37).** Then `G` is essentially self-adjoint on every core for `N`
(hence on the Hermite/Schwartz core), and the Nelson Laplacian
`Δ = H² + P² + K²` is essentially self-adjoint. Combined with the companion
note's verified Poincaré-algebra closure, **Nelson's integrability theorem**
(1959) upgrades the Lie-algebra representation to a strongly-continuous **unitary
representation** of the (universal cover of the) Poincaré group — with no false
common-analytic-vector claim anywhere.

**Why `N` works where the rapidity-Gaussian failed.** `N` is *not* tied to one
coordinate chart. In flat `L²(dp)` the generators are dominated by the
oscillator: `P ~ N^{1/2}`, `H = \sqrt{p²+m²} ≤ |p|+m ~ N^{1/2}`, and the boost
`K = -\tfrac{i}{2}(E\,\partial_p + \partial_p E) ~ |p|\,\partial_p ~ N`. The
commutators land one order lower in the form sense (`[P,N] ~ \partial_p ~ N^{1/2}`,
`[H,N]` has bounded coefficients `E'=p/E, E''=m²/E³`, `[K,N]` has its leading
`2pE ~ |p|² ~ N` piece controlled by `N`). These are precisely hypotheses (i)–(ii).

## 2. Numerical verification (1+1d; the full non-compact difficulty)

The runner works in the tractable `1+1`d reduction — the Poincaré subalgebra
`{H, P, K}` with `[K,H]=iP`, `[K,P]=iH`, `[H,P]=0` — which already contains the
entire **non-compact boost** difficulty. (The `3+1`d case only adds the **compact**
rotations `J^i`, essentially self-adjoint on bounded angular-momentum bands, and
the **bounded** spin Wigner term, handled by Kato–Rellich — exactly the original
note's *undisputed* S-i; the boost commutator structure is identical.) On the
`M`-dimensional Hermite basis:

- **Part C (hypothesis (i)).** `c₁` is finite and **stable** across `M = 80,120,160`:
  `c₁ → H:1.225, P:0.707, K:0.900`.
- **Part D (hypothesis (ii)).** `c₂`, computed as the spectral radius of
  `N^{-1/2}\,i[G,N]\,N^{-1/2}` on a safe low-mode block (the true operator
  inequality), is finite and **stable**: `c₂ → H:0.536, P:1.000, K:2.051`.

  (Testing the form bound on *single* `N`-eigenvectors would give a spurious `0`,
  since `⟨v,[G,N]v⟩ = λ⟨v,Gv⟩ − λ⟨v,Gv⟩ = 0` there; the operator-inequality
  computation avoids that trap.)
- **Part E (consequences + controls).** The boost flow `e^{-i\theta K}` is a
  **unitary** one-parameter group (Stone; norm-preserving and `U^†U=I` to `10⁻⁹`);
  `Δ = H²+P²+K²` is Hermitian with real, bounded-below spectrum (e.s.a. signature).
  Controls fail as required: a non-Hermitian `K + 0.3iI` has **complex** spectrum,
  and the half-line `-i\,d/dx` on `[0,∞)` has **unequal** deficiency indices
  `(1,0)` — so the boost genuinely uses that the rapidity runs over the whole line
  `R` (the mass shell is the full hyperbola, no boundary → deficiency `(0,0)`).

## 3. What this note does NOT claim

- It does **not** re-derive the Poincaré **algebra** closure (the companion note's
  content, consumed as input); it supplies only the analytic
  self-adjointness/integrability step, now by the correct theorem.
- It performs **no** statistics selection and is **no** spin-statistics theorem
  (the one-particle self-adjointness is statistics-blind).
- It makes **no** emergent-Lorentz claim — this is functional analysis of the
  *given* free Dirac generators, not a derivation of Lorentz invariance from the
  lattice. (It removes a *blocker* to the boost-spinor footing in Link C; it does
  not by itself derive emergent Lorentz.)
- It does **not** re-prove Nelson's theorem, X.37, Kato–Rellich, or Stone; their
  **statements** are cited and their **hypotheses** are verified here.
- It introduces **no** new axiom, primitive, repo vocabulary, or class tag, and
  consumes **no** PDG / fitted / `β=6` / `g_bare` / lattice-MC value.

## 4. Re-audit case (no status set here)

The failed note's single fatal step — S-ii's claim that the rapidity-Gaussian is a
common analytic vector for `H, P, Δ` — is (a) **confirmed false** (Part A,
`‖H^n ψ‖/n! ~ e^{n²/2a}`), and (b) **replaced** by the Nelson commutator theorem
with `N =` the momentum harmonic oscillator, whose hypotheses are verified with
stable constants (Parts C, D), yielding essential self-adjointness on the genuine
Hermite/Schwartz core and `Δ` essential self-adjointness — hence integrability to
the unitary Poincaré representation (Parts D2, E). The note's sound S-i (each
generator individually e.s.a., including the exact rapidity reduction of the
boost) is retained. Whether this lifts the note out of `audited_failed` is for the
independent audit lane to decide; this note sets no status.

## 5. Bounded-Wall Discipline Gate (N1–N8)

**Result:** PASS for the scoped claim "the free Dirac Poincaré generators are
essentially self-adjoint on the Hermite/Schwartz common core, and the
representation integrates to a unitary Poincaré representation, via the Nelson
commutator theorem with the momentum-oscillator comparison operator."

- **N1 (routes).** (a) explicit common analytic Gaussians — *ruled out* (Part A,
  false for `H`); (b) Nelson commutator theorem with `N =` momentum oscillator —
  **adopted** (hypotheses verified); (c) black-box "Wigner rep is unitary" —
  declined (this note verifies hypotheses, not asserts the conclusion).
- **N2 (wall independence).** Three reproven walls: the located falsity (A); the
  two X.37 hypotheses (C, D); the consequence battery (E). Each is independent.
- **N3 (hidden-wall scan).** Explicit premises: the companion note's generators +
  algebra closure (input); the comparison operator `N`; the `1+1`d reduction with
  the stated `3+1`d extension (compact `J`, bounded spin). All named.
- **N4 (residual matching).** Audit objection (S-ii false) → located in A;
  S-ii/S-iii repaired → C/D/D2; integrability consequence → E.
- **N5 (rhetoric).** "Essentially self-adjoint" / "integrates" now rest on X.37 +
  Nelson 1959 with verified hypotheses, not on a false analytic-vector display.
- **N6 (partial-closure).** No new axiom/primitive; the legitimate path is to
  correct the analytic step using the standard theorem.
- **N7 (steelman).** A reviewer could ask for the explicit `3+1`d spinor
  computation; that adds only compact `J` (e.s.a.) and a bounded Kato–Rellich
  term, the original undisputed S-i — the load-bearing non-compact boost is fully
  in the `1+1`d verification.
- **N8 (cross-cycle echo).** The governance lesson — do not promote a
  Lie-algebra-on-a-core into a unitary group rep without the analytic work — is
  honored: the work is done here with the *correct* theorem, and the previously
  displayed (false) shortcut is explicitly retired.

## 6. Reprove-and-cite ledger

- **Reproven here** (runner): the falsity of the common-Gaussian claim
  (`‖K^n ψ‖/n! → 0` vs `‖H^n ψ‖/n! → ∞`, exact Hermite recursion + Gauss–Hermite
  quadrature); Hermiticity of `H, P, K` on the Hermite core; the two Nelson X.37
  hypotheses `c₁` (N-boundedness) and `c₂` (commutator form-bound) with stability
  across truncation; the unitary boost flow (Stone); `Δ` real bounded-below
  spectrum; the non-Hermitian and half-line `(1,0)`-deficiency controls.
- **Cited** (comparator only, never a derivation input): Nelson, *Ann. Math.*
  **70** (1959) 572 (analytic vectors; the Laplacian integrability criterion);
  Reed–Simon II, Thm X.37 (the commutator theorem) and X.1 (deficiency indices,
  half-line momentum); Reed–Simon I, Ch. VIII (multiplication operators,
  `-i d/dx`, Stone); Faris–Lavine (commutator e.s.a.); Wigner 1939 (the massive
  spin-½ induced representation, the classical statement).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It
does not promote this note or change any audited claim scope.

- [FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md](FREE_DIRAC_POINCARE_GENERATORS_ESSENTIAL_SELFADJOINTNESS_BOUNDED_NOTE_2026-05-30.md)
- [FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md)
- [FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md](FREE_DIRAC_ANTIPARTICLE_MODE_ALGEBRA_BOUNDED_NOTE_2026-05-30.md)
- `FS_RECONSTRUCTION_R_AND_TIGHT_LINK_REVIEW_NOTE_2026-06-06.md` (context only; not yet on main — backticked to avoid a broken citation-graph edge)

### Source-note boundary

**Hypothesis set:** (1) the companion note's ten explicit generators and verified
Poincaré-algebra closure (input); (2) the comparison operator `N =` momentum
harmonic oscillator with the Hermite/Schwartz core; (3) the `1+1`d reduction
carrying the full non-compact boost, with the `3+1`d extension being compact `J`
(e.s.a.) plus a bounded spin Wigner term (Kato–Rellich); (4) the standard
functional-analysis theorems (Nelson 1959; RS X.37, X.1; Stone; Kato–Rellich),
invoked by statement with hypotheses verified here.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class
tag; only standard functional-analysis / QFT terms ("essential self-adjointness,"
"comparison operator," "commutator theorem," "deficiency indices," "Nelson
Laplacian," "rapidity," "Hermite/Schwartz core"). No fitted / PDG / lattice-MC /
`β=6` / `g_bare` value consumed.

**No-promotion statement:** this note does **not** promote, demote, or set the
audit status of the failed self-adjointness note, its companion representation
note, or any upstream row. The audit lane is the only status authority.
