# Koide Q = 2/3 from Retained Frobenius-Extremum Bridge

**Date:** 2026-05-25
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/koide_q_two_thirds_frobenius_extremum_runner.py`](../scripts/koide_q_two_thirds_frobenius_extremum_runner.py)

## Claim

Given three retained authorities — the `C_3` Fourier decomposition
of the cyclic Hermitian circulant `H = aI + bC + b̄C²` (R3), the
equal-weight Frobenius-block-total extremum at `a² = 2|b|²` (kappa
T3), and the cone-algebraic equivalence `Q(v) = 2/3 ⟺ a₀² = 2|z|²` —
the Koide ratio of the **eigenvalue vector** `λ = (λ_0, λ_1, λ_2)` of
`H` evaluated at the equipartition extremum satisfies

```text
Q(λ)  =  (λ_0² + λ_1² + λ_2²) / (λ_0 + λ_1 + λ_2)²  =  2 / 3.
```

The proof-walk uses only:

1. The retained circulant eigenvalue formula
   `λ_k = a + 2 |b| cos(arg(b) + 2 π k / 3)` (R3).
2. The retained equipartition extremum `a² = 2 |b|²` (kappa T3).
3. The retained cone-algebraic equivalence
   `Q(v) = 2/3 ⟺ a₀(v)² = 2 |z(v)|²` (cone narrow theorem).
4. The Fourier algebra `a₀(λ) = √3 · a` and `z(λ) = √3 · b`,
   established by direct substitution into the cone theorem's
   Fourier definitions (D2)/(D3) and the root-of-unity sum identity
   `Σ_k ω^k = 0` already retained in (kappa T1)-companion content.

The proof-walk introduces **no new admissions**. The choice of
equal-weight log-functional `S(H) = log E_+(H) + log E_⊥(H)` whose
extremum supplies `a² = 2|b|²` is the admission already present in the
retained kappa T3 statement (its own "Open derivation gap" records that
the canonical-extremum choice is unresolved); this bridge inherits that
admission rather than introducing a new one. The framework-specific
identification `λ_k = √m_k` for charged-lepton masses is **out of
scope** for this bridge — the claim is about `Q(λ)`, not `Q(√m)`.

This is a bounded proof-walk satisfying the auditor's explicit
"missing_bridge_theorem" hint on the parent
[`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md`](CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md)
(`notes_for_re_audit_if_any`: "provide retained-grade bridge theorems
closing the Q = 2/3 Frobenius extremal principle …"). It closes the
**Frobenius extremal principle** half of the auditor's request; the
**`δ = 2/9` physical Brannen-phase identification** half remains
foreclosed per the retained radian-bridge no-gos
(`koide_a1_radian_bridge_irreducibility_audit_note_2026-04-24` and
`koide_selected_line_local_radian_bridge_no_go_note_2026-04-20`).

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | `λ_k = a + 2 |b| cos(arg(b) + 2 π k / 3)` for `k = 0, 1, 2` | R3 circulant eigenvalue formula |
| (B2) | `λ_0 + λ_1 + λ_2 = 3 a` (root-of-unity sum cancels the cosines) | Σ_k cos(δ + 2πk/3) = 0 identity |
| (B3) | `a₀(λ) = (1/√3)(λ_0 + λ_1 + λ_2) = √3 · a` | Fourier definition (D2) + (B2) |
| (B4) | `z(λ) = (1/√3) Σ_k ω̄^k λ_k = √3 · b` | Fourier definition (D3) + Σ_k ω^k = 0, Σ_k ω^{2k} = 0 |
| (B5) | `|a₀(λ)|² = 3 a²` and `|z(λ)|² = 3 |b|²` | rational arithmetic on (B3)/(B4) |
| (B6) | Equipartition extremum `a² = 2 |b|²` (kappa T3) | retained kappa T3 |
| (B7) | Substitute (B6) into (B5): `|a₀(λ)|² = 3 a²`, `2 |z(λ)|² = 2 · 3 |b|² = 3 a² = |a₀(λ)|²` | rational arithmetic |
| (B8) | Cone theorem: `Q(λ) = 2/3 ⟺ a₀(λ)² = 2 |z(λ)|²` | retained cone narrow theorem |
| (B9) | Combine (B7) + (B8): `Q(λ) = 2/3` at the equipartition extremum | rational arithmetic |

The proof-walk does not cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, lattice scale `u_0`, a
Monte Carlo measurement, or a fitted observational value. It also does
**not** assert `λ_k = √m_k` for any physical lepton mass.

## Exact arithmetic check

```text
λ_0 + λ_1 + λ_2  =  3 a + 2 |b| · Σ_k cos(δ + 2 π k / 3)
                 =  3 a + 2 |b| · 0           [root-of-unity sum]
                 =  3 a.
```

Fourier components of `λ` per cone-theorem definitions (D2)/(D3):

```text
a₀(λ)  =  (λ_0 + λ_1 + λ_2) / √3              =  3 a / √3   =  √3 · a,
z(λ)   =  (λ_0 + ω̄ λ_1 + ω λ_2) / √3.
```

For `z(λ)`, expanding `λ_k = a + b · ω^k + b̄ · ω^{-k}` (write `b = |b| e^{iδ}`):

```text
z(λ)   =  (1/√3) Σ_k ω^{-k} (a + b · ω^k + b̄ · ω^{-k})
       =  (1/√3) [ a · Σ_k ω^{-k}  +  b · Σ_k 1  +  b̄ · Σ_k ω^{-2k} ]
       =  (1/√3) [ 0  +  3 b  +  0 ]            [Σ_k ω^{±k} = Σ_k ω^{±2k} = 0]
       =  √3 · b.
```

So `|z(λ)|² = 3 |b|²` and `a₀(λ)² = 3 a²`. The equipartition extremum
`a² = 2 |b|²` (kappa T3) gives

```text
a₀(λ)²  =  3 a²,
2 |z(λ)|²  =  2 · 3 |b|²  =  6 |b|²  =  3 (2 |b|²)  =  3 a²  =  a₀(λ)².
```

So `a₀(λ)² = 2 |z(λ)|²` is verified at the extremum. The cone narrow
theorem then gives `Q(λ) = 2/3`.

## Dependencies

- [`CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md`](CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md)
  — the parent whose Q = 2/3 Frobenius-extremal-principle gap this
  bridge closes.
- [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained narrow theorem supplying the equipartition extremum
  `a² = 2 |b|²` (T3) at the equal-weight log-functional. This bridge
  inherits T3's open-derivation-gap on which extremum is canonical; no
  new admission is introduced.
- [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained narrow theorem supplying `Q(v) = 2/3 ⟺ a₀(v)² = 2 |z(v)|²`
  for abstract positive 3-vectors.
- [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md)
  — supplies R3, the circulant Hermitian decomposition and eigenvalue
  formula `λ_k = a + 2 |b| cos(arg(b) + 2 π k / 3)`.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This bridge does **not** close:

- the **`δ = 2/9` physical Brannen-phase identification** (the other
  half of the auditor's request — foreclosed per the cited retained
  no-gos);
- the framework-specific identification `λ_k = √m_k` for charged-lepton
  masses (the bridge claim is about `Q(λ)`, not `Q(√m)`; the physical
  Koide-spectrum identification is downstream of this bridge and
  remains open);
- the question of which Frobenius extremal principle is canonical (the
  retained kappa T3's "Open derivation gap"; this bridge inherits T3's
  choice but does not select it);
- any retained closure of `δ = 2/9` from this bridge alone.

Downstream rows that need `Q(λ) = 2/3` purely as an algebraic identity
on cyclic Hermitian circulant eigenvalues at the equipartition extremum
can now cite this companion directly; rows needing the physical
`Q(√m) = 2/3` Koide ratio on charged-lepton masses must additionally
import the open `λ_k = √m_k` identification.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/koide_q_two_thirds_frobenius_extremum_runner.py
```

Expected:

```text
TOTAL: PASS=7 FAIL=0
VERDICT: bounded bridge passes; Q(λ) = 2/3 follows from retained
R3 + kappa T3 + cone narrow theorem at the equipartition extremum
a² = 2|b|², for all tested (a, b) pairs.
```
