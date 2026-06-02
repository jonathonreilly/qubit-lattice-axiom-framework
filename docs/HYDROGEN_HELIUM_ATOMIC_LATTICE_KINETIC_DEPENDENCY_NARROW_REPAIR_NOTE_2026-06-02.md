# Hydrogen/Helium Atomic Companion — Lattice-Kinetic + Coulomb-Kernel Dependency Edge Repair (Narrow Companion)

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. The `bounded_theorem`
label is a source-side claim-boundary declaration, not an audit verdict.
**Primary runner:** [`scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py`](../scripts/frontier_hydrogen_helium_atomic_lattice_kinetic_dependency_narrow_repair_verifier.py)

**Authority role:** narrow companion to the `audited_conditional` parent
[`work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18`](work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18.md).
Supplies three narrow repairs targeted by the parent's `audited_conditional`
`missing_dependency_edge` verdict (2026-05-31, `load_bearing_score = 5.17`):

- **(R-A) Lattice-kinetic dependency edge.** Wires the retained-bounded
  [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  as the framework-local authority for the nearest-neighbor `Z^3`
  graph Laplacian `(-Delta_lat)` stencil. Replaces the parent's
  plain-text reference to `BROAD_GRAVITY_DERIVATION_NOTE.md` Step 1
  (whose own audited scope is conditional `k`-cancellation algebra,
  not a kinetic-operator derivation).
- **(R-B) Coulomb-kernel dependency edge with inline arithmetic.**
  Same Maradudin row supplies the asymptote `G(r) -> 1/(4 pi r)`; the
  corollary `V(r) = -g/|r|` is the four-line class-A identity proved
  inline (§2 Lemma R-B.1).
- **(R-C) Scope narrowing on two unsupported framings.** Drops the
  parent's "Cl(3) on Z^3 uniquely gives the staggered Dirac
  Hamiltonian whose square is the negative graph Laplacian" wording
  (§3.1, with explicit runner counterexample `H_Dirac^2 != -Delta_lat`)
  and the parent's "confirms d=3 gives finite Rydberg series" line
  (§3.2, replaced by honest numerical-readout framing).

## Honest scope (read this first)

- **Three narrow repairs only**; no other parent content touched.
- **Does NOT modify parent text.** Parent keeps current
  `audited_conditional` ledger row and on-disk wording.
- **Does NOT lift parent's `audited_conditional` status.** Lift would
  additionally require helium Hartree + Jastrow runner caches (out of
  scope; residual R-D in §5) and auditor's re-audit decision.
- **Does NOT re-derive `-Delta_lat` from Cl(3)+`Z^3`.** No retained
  source on origin/main derives the unsigned scalar graph Laplacian as
  a uniqueness consequence of Cl(3)+`Z^3` axioms. What is retained is
  the staggered Hermitian-lift `H_Dirac = i D` with KS phases — a
  different operator (§3.1). Maradudin authority supplies
  `(-Delta_lat)` as the framework's *named* nearest-neighbor Laplacian
  convention with retained-bounded Green-function normalization, and
  the companion runners use exactly that operator. The "uniqueness
  from Cl(3)" framing is dropped (R-C.1); dependency-edge framing
  used instead (R-A).
- **Prove-textbook-inline discipline.** Coulomb-kernel corollary
  `V(r) = -g/|r|` is load-bearing and proved inline class-A (Lemma R-B.1).
  No textbook citation is load-bearing that isn't already wrapped in a
  retained_bounded note on origin/main (the Maradudin asymptote
  `G(r) -> 1/(4 pi r)` is the one upstream input, and it lives in
  `LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18` at
  `retained_bounded`, not cited raw here).
- **No new admissions, axioms, or imports**; all cited authorities
  already on origin/main at the stated status.

---

## §0. Why this companion exists

The 2026-05-31 audit re-pass on the parent row issued the verdict:

> *missing_dependency_edge: re-audit with the current axiom premise, a
> retained lattice-kinetic authority that actually derives `-Delta_Z^3`
> from Cl(3)/Z^3, the Coulomb-kernel authority source/cache, complete
> Hartree/Jastrow runner sources and SHA-pinned cached stdout, and
> either remove or justify the d=3 finite-Rydberg-series bound-state
> statement.*

Five sub-targets. This companion closes three (R-A operator routing,
R-B kernel arithmetic, R-C scope narrowing); the helium-runner-cache
deposition (R-D) and the parent-text edit (R-E) are out of scope (§5).

The parent's `open_dependency_paths` cites only `MINIMAL_AXIOMS_2026-04-11`
(meta; superseded by current `MINIMAL_AXIOMS_2026-05-20`),
`GRAVITY_CLEAN_DERIVATION_NOTE` (audited scope is conditional
weak-field implication, **not** `-Delta_Z^3` derivation), and the
Coulomb-from-lattice script. None is a retained lattice-kinetic
authority. This companion routes through the actual retained-bounded
`lattice_greens_function_maradudin_textbook_import_note_2026-05-18`.

---

## §1. Cited dependencies (load-bearing on origin/main)

| Authority | Status | Role here |
|---|---|---|
| [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md) | meta | A1 (qubit per site ≡ Cl(3)) + A2 (`Z^3` substrate); replaces parent's stale `MINIMAL_AXIOMS_2026-04-11` reference |
| [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md) | retained_bounded | (R-A) `(-Delta_lat)` stencil; (R-B) `G(r) -> 1/(4 pi r)` asymptote |
| [`STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md) | retained_bounded | scope-disambiguation (§3.1): `H_Dirac = i D` with KS phases is a *different* operator from scalar `-Delta_lat` |
| [`GRAPH_LAPLACIAN_CORE_CARD_NOTE.md`](GRAPH_LAPLACIAN_CORE_CARD_NOTE.md) | retained_bounded | sidecar context (not load-bearing for R-A/R-B) |
| Parent [`work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18`](work_history/atomic/HYDROGEN_HELIUM_ATOMIC_COMPANION_NOTE_2026-04-18.md) | audited_conditional | parent (companion ships R-A+R-B+R-C without modifying parent text) |

No other dependency is load-bearing. No textbook citation is
load-bearing. No new framework primitive is introduced.

---

## §2. Repair (R-A) + (R-B): kinetic + Coulomb dependency edges with inline kernel arithmetic

### Setting (parent objects re-used verbatim)

```text
    H_g  :=  -Delta_lat  -  g/|r|                              (parent eq H_g)
```

on `l^2((Z mod L)^3)` with Dirichlet BC (parent runners), `g > 0`
dimensionless, `r := x - x_0`. Both operators are supplied by the
retained-bounded Maradudin authority:

- **(R-A) Operator stencil.** The Maradudin note's framework-local
  statement defines

  ```text
      (-Delta_lat f)(x)  =  6 f(x)  -  sum_{|y - x| = 1} f(y).    (Maradudin stencil)
  ```

  Runner cross-check `A.maradudin.stencil_match` exhibits the
  companion runners' `build_graph_laplacian(N)` matches this stencil
  matrix-element-by-matrix-element at audit precision on `N = 4`.

- **(R-B) Green-function asymptote.** The same Maradudin note
  (audited scope) supplies

  ```text
      G(r) := (-Delta_lat)^{-1}(r)  ->  1/(4 pi |r|)    as |r| -> infinity.   (Maradudin asymptote)
  ```

### Lemma R-B.1 (`V(r) = -g/|r|` from the Maradudin asymptote)

For `H_g = -Delta_lat - g/|r|`, the potential term `V(r) := -g/|r|`
is the far-field continuum limit of the lattice potential
`V_lat(r) := -4 pi g G(r)` from a unit negative point-source `-g` at
`x_0`.

**Proof (class-A, four lines).**

Step 1 (definition). Lattice Poisson equation for `V_lat` sourced by
`-g` at `x_0`:

```text
    (-Delta_lat) V_lat  =  -4 pi g  delta_{x, x_0}.                          (Pois)
```

(Factor `4 pi` is the framework's adopted flux convention; verified
in the Maradudin runner via `assert_continuum_flux_normalization`.)

Step 2 (Green's-function solution). By definition
`G(r) := (-Delta_lat)^{-1}(r, 0)`, so (Pois) gives
`V_lat(r) = -4 pi g G(r)`.

Step 3 (asymptote substitution). Apply (`Maradudin asymptote`):

```text
    V_lat(r)  =  -4 pi g G(r)  ->  -4 pi g · 1/(4 pi |r|)  =  -g/|r|.        (V-asymp)
```

Step 4 (matching parent's statement). The right side of (V-asymp) is
exactly the parent's `V(r) = -g/|r|` in (`parent eq H_g`). ∎

### Corollary R-B.2 (helium kernels `V_nuc`, `V_ee` from the same row)

The parent's helium runners use `V_nuc(r) = -Z g_EM / |r|` and
`V_ee(r_1, r_2) = +g_EM / |r_1 - r_2|`. Both follow from (Pois)+(V-asymp):

- (V_nuc): charge replacement `-g -> -Z g_EM`; same kernel, same proof.
- (V_ee): sign + translation. Replace `-g -> +g_EM` (positive
  source: same-sign repulsion). Translation invariance of
  `(-Delta_lat)` on `Z^3` (R-A stencil is translation-invariant by
  inspection) gives
  `(-Delta_{lat,1}) V_ee(r_1 - r_2, ·) = (4 pi g_EM) delta_{r_1, r_2}`,
  which by (V-asymp) gives the stated `+g_EM/|r_1 - r_2|`. ∎

(Class-A; runner exhibits the kernel arithmetic at finite-`N`
precision; see `B.coulomb.charge_subst` and `B.4.coulomb.translation_invariance`.)

### Repair statement (R-A) + (R-B)

The parent's load-bearing operator content for the three companion
runners' kinetic + Coulomb pieces is now routed through the
retained-bounded Maradudin authority as a one-hop markdown-linked
dependency, with the Coulomb-kernel corollary supplied by inline
arithmetic (Lemma R-B.1). The parent's plain-text "DERIVED —
`BROAD_GRAVITY_DERIVATION_NOTE` Step 1" attribution for the kinetic
operator and plain-text "lattice potential theory theorem" attribution
for the Coulomb kernel are replaced at the dependency-edge level (not
the parent-text level) by the named authority + Lemma R-B.1.

---

## §3. Repair (R-C): scope narrowing on two unsupported parent framings

### (R-C.1) Drop "Cl(3) on Z^3 uniquely gives the staggered Dirac whose square is `-Delta_lat`"

Parent runner `frontier_atomic_hydrogen_lattice_companion.py` (lines
16–19) asserts: *"Cl(3) on Z³ uniquely gives the staggered Dirac
Hamiltonian whose square is the negative graph Laplacian:
`H_free = -Δ_Z³`."* This is incorrect as stated. The retained staggered
surface is the Hermitian-lift `H_Dirac := i D` of the real
anti-Hermitian KS-phased hopping operator `D` (KS phases
`eta_1=1, eta_2(x)=(-1)^{x_1}, eta_3(x)=(-1)^{x_1+x_2}`), per
[`STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md`](STAGGERED_HAMILTONIAN_DIRECTION_DECOMPOSITION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md).
Then `H_Dirac^2 = -D^2` is a strictly different matrix from the
Maradudin `-Delta_lat`. Runner exhibits on a 4×4×4 periodic torus
(Frobenius gap `||H_Dirac^2 - (-Delta_lat)||_F = 41.57`):

- **Diagonal mismatch.** `H_Dirac^2[x, x] = 1.5`; `-Delta_lat[x, x] = 6`
  (`C.staggered.diagonal_disagreement`).
- **Nearest-neighbor mismatch.** `H_Dirac^2[NN] = 0` (KS-phase
  cancellation); `-Delta_lat[NN] = -1`
  (`C.staggered.nn_disagreement`).
- **Distance-2 axis mismatch.** `H_Dirac^2[(0,0,0)<->(0,0,2)] = -0.5`
  (two-hop composition); `-Delta_lat[same] = 0` (Maradudin stencil has
  no distance-2 entries) (`C.staggered.axis2_in_H2_only`).

Repair: drop the "uniquely gives the staggered Dirac" line and replace
with the honest framing — the companion runners compute spectra of the
scalar `H_g = -Delta_lat - g/|r|` with `-Delta_lat` per Maradudin
stencil and `-g/|r|` per Lemma R-B.1; `H_Dirac` is a different operator
on the spin-doubled space and is **not** used here. Numerics unchanged.

### (R-C.2) Replace "d=3 gives finite Rydberg series" with numerical-readout framing

Parent runner line 110 asserts: *"5. Bound state count: confirms d=3
gives finite Rydberg series"*. The companion's output exhibits
`E_n/E_1 ~ 1/n^2` for `n in {1,2,3,5,6}` at `N=60, g=1` with deviations
`+3.43%, +0.19%, -3.57%, +4.25%` (parent's pinned readouts). This is a
finite-box numerical observation, not a derived theorem; the continuum
textbook fact (continuum-`R^3` `1/r` attraction has *infinitely* many
bound states) is the **opposite** of the parent's "finite" claim. The
parent's "finite" refers only to finite-box truncation, a grid
artifact. Repair: replace with — finite-box numerics exhibit
`E_n/E_1 ~ 1/n^2` for the first six levels with `O(1/N^2)` deviations
from finite-`Lambda` Dirichlet-cube discretization; this is a spectral
readout, not a derivation of bound-state series finiteness.

### Repair statement (R-C)

Both unsupported framings dropped from load-bearing chain. Numerics
unchanged; dependency-edge text corrected.

---

## §4. Restated load-bearing chain

| Load-bearing piece | New routing | Status |
|---|---|---|
| `(-Delta_lat)` stencil on `Z^3` | Maradudin authority (R-A) | retained_bounded |
| `G(r) -> 1/(4 pi |r|)` asymptote | Maradudin authority (R-B) | retained_bounded |
| `V(r) = -g/|r|` corollary | Lemma R-B.1 inline | proved inline class-A |
| `V_nuc, V_ee` corollaries | Corollary R-B.2 inline | proved inline class-A |
| `build_graph_laplacian(N)` ↔ Maradudin stencil | runner `A.maradudin.stencil_match` | numerical exact at audit precision |
| `build_coulomb_potential(N,g)` ↔ (V-asymp) | runner `B.3.coulomb.kernel_form` | numerical exact at audit precision |
| Scalar `-Delta_lat` ≠ `H_Dirac^2` | runner `C.staggered.square_is_not_minus_laplacian` (R-C.1) | numerical counterexample |

This does **not** lift the parent's `audited_conditional` status; it
closes three of the five sub-targets of the 2026-05-31 verdict cleanly
(R-A axiom premise update, R-B Coulomb-kernel via Lemma R-B.1, R-C scope
narrowing). The remaining auditor sub-target 2 (a retained Cl(3)+Z^3
→ -Delta_lat derivation) is reframed-with-honest-disclosure in §5 — no
such retained derivation exists on origin/main; the companion routes
through Maradudin as a retained_bounded authority instead. R-D and R-E
remain open (§5).

---

## §5. What this note does NOT claim; remaining residuals

This note does not (a) modify the parent's on-disk text, (b) lift its
`audited_conditional` status, (c) re-derive `-Delta_lat` from
Cl(3)+`Z^3` axioms (no retained derivation exists on origin/main),
(d) ship helium-runner caches, (e) claim continuum-limit closure,
absolute-eV predictions, exact helium ground state, isoelectronic
predictions, periodic-table promotion, or any retained atomic chain.

Open residuals from the auditor's five sub-targets:

- **(R-D) Helium runner caches.** No cached stdout for
  `frontier_atomic_helium_hartree_companion.py` or
  `frontier_atomic_helium_jastrow_companion.py` exists under
  `logs/runner-cache/` on origin/main as of 2026-06-02. Source files
  exist; only deterministic run + cache deposition needed. **Separate
  companion.**
- **(R-E) Parent-text edit.** Whether parent body should reflect R-C
  scope narrowing inline (vs only via companion routing) is an
  audit-lane / parent-owner decision; companion does not modify parent
  body per established companion-only repair pattern.

---

## §6. No-Go Discipline Gate

- **N1 alternative routes.** (1) Route through Maradudin + inline
  arithmetic (chosen); (2) attempt new retained derivation
  `Cl(3)+Z^3 ==> -Delta_lat` (no retained candidate exists; would
  require new source theorem); (3) reframe parent as using `H_Dirac^2`
  (false — runner exhibit shows `H_Dirac^2 != -Delta_lat`).
- **N2 wall independence.** R-A, R-B, R-C are three independent
  repairs.
- **N3 hidden-wall scan.** Maradudin authority is `retained_bounded`
  with scope exactly matching parent's load-bearing operator content.
- **N4 residual matching.** Three of five sub-targets closed; R-D, R-E
  listed (§5).
- **N5 rhetoric audit.** "Scope narrowing" drops "uniqueness from
  Cl(3)" framing from load-bearing chain; framework axioms unchanged,
  companion Hamiltonian unchanged.
- **N6 partial-closure scan.** Partial closure piece; R-D, R-E open.
- **N7 steelman.** Parent might intend `H_Dirac^2` reduces to
  `-Delta_lat` on some subspace. Not established on retained surface;
  4×4×4 runner exhibit shows matrices differ. Future retained theorem
  could revisit R-C.1.
- **N8 cross-cycle echo.** Narrow source repair for a known
  `audited_conditional` parent; not an audit verdict; not a status lift.
