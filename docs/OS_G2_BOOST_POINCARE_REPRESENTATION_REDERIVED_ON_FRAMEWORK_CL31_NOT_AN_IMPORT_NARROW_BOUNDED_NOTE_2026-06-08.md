# The OS Boost Sector G2 (Poincaré Representation) Re-Derived on the Framework's Surface — Not an Import

**Date:** 2026-06-08
**Claim type:** bounded_theorem (re-derivation removing an import)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_os_g2_boost_poincare_rederived_on_framework.py`](../scripts/frontier_os_g2_boost_poincare_rederived_on_framework.py)
**Cached log:**
[`logs/runner-cache/frontier_os_g2_boost_poincare_rederived_on_framework.txt`](../logs/runner-cache/frontier_os_g2_boost_poincare_rederived_on_framework.txt)
(TOTAL: PASS=9 FAIL=0)

## 0. What this removes

The OS→Wightman reconstruction's last residual was **G2** — the full positive-spectrum Poincaré
representation (boosts as self-adjoint operators on the reconstructed Hilbert space). The conditional
reconstruction note carried it on the **textbook** OS theorem: "the abstract OS reconstruction
theorem delivering the full positive-spectrum Poincaré representation … is cited as textbook
methodology, **not re-derived on the framework's surface**." That phrasing is exactly the criterion
for an **import**.

This note re-derives the **generators, their algebra, the Dirac covariance, and the positive
spectrum on the framework's own surface**, leaving only the standard *Lie-algebra→group integration*
(Nelson's theorem) as a cited **method**. With the physics content framework-native and only the
mathematical method cited, **G2 is a derivation, not an import** — the keystone's last OS residual
carries no physics import.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| `Cl(3,0)→Cl(3,1)=M_4(R)` — the Clifford algebra whose **bivectors are the Lorentz generators** | [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md) | `retained` | framework-native generators |
| the 4-component Dirac `iso(3,1)` (Poincaré) support incl. translations | [`FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30`](FREE_DIRAC_POINCARE_REPRESENTATION_BOUNDED_NOTE_2026-05-30.md) | `retained_bounded` | framework-native translations |
| positive spectrum `Ĥ ≥ 0` (CAR/T1) | companion `KEYSTONE_MASSIVE_DIRAC…_VIA_T1_2026-06-08` | (this session) | the spectrum condition |
| Nelson's theorem (analytic-vector Lie-algebra→group integration) | Nelson, *Ann. Math.* 1959; Reed-Simon II | **methodology only** | the integration step |

No PDG value is load-bearing. No new axiom, import, or vocabulary.

## 2. The generators are framework-native (verified)

All Lorentz generators are bivectors of the **retained** `Cl(3,1)`: `S_{μν} = (1/4)[γ_μ, γ_ν]`,
rotations `J_i = (1/2)ε_{ijk}S_{jk}`, boosts `K_i = S_{0i}`. The runner verifies, on the framework's
surface:

- **(SO13)** the bivectors generate `so(1,3)`: `[J_i,J_j]=ε_{ijk}J_k`, `[J_i,K_j]=ε_{ijk}K_k`,
  `[K_i,K_j]=−ε_{ijk}J_k` (the non-compact sign).
- **(VECTOR)** `[S_{μν}, γ_ρ] = η_{νρ}γ_μ − η_{μρ}γ_ν`: the Dirac gammas are a Lorentz 4-vector, so the
  Dirac operator `γ^μ p_μ` is **Lorentz-covariant**.
- **(FINITE)** the finite spinor boost `S(χ)=exp(χK_1)` acts as a genuine Lorentz boost:
  `S(χ)^{-1}γ^0 S(χ) = cosh χ · γ^0 + sinh χ · γ^1`.
- **(HERM)** rotations are unitary (`iJ_i` Hermitian) and boosts are the correctly **non-unitary**
  finite-dim spinor boosts (`K_i` Hermitian, real boost parameter) — the expected `SL(2,ℂ)`-type
  representation.
- **(POS)** the single-particle spectrum is `±E`; the many-body `Ĥ ≥ 0` by CAR/T1 (companion note).

With the retained `iso(3,1)` translations, the **entire generator content** of the Poincaré
representation — `H, P_i, J_i, K_i`, their algebra, the Dirac covariance, and the positive spectrum —
is framework-native.

## 3. Only the integration method is textbook

What the abstract OS theorem supplies is one standard step: integrating a Lie-algebra representation
to a **group** representation with **self-adjoint** generators on the Hilbert space. This is
**Nelson's theorem**: a Lie-algebra representation by symmetric operators sharing a dense domain of
analytic vectors, with the algebra closing, integrates to a unitary representation of the
simply-connected group, with self-adjoint generators. For the free field the Fock space of smooth
vectors furnishes the analytic-vector domain, the algebra closes (§2), and `Ĥ ≥ 0` gives the
positive spectrum.

Nelson's theorem is a **mathematical method** — the same status as "use linear algebra" or "use the
spectral theorem." It supplies no physics input: the generators, the algebra, the covariance, and
the spectrum are all framework-native (§2). Citing it is methodology, **not** importing the physics
conclusion.

```text
framework-native:  generators (Cl(3,1) bivectors + retained iso(3,1) translations),
                   so(1,3) algebra, Dirac covariance, finite boost, H >= 0
cited METHOD only: Nelson's Lie-algebra -> group integration -> self-adjoint boosts
=>  G2 is a DERIVATION (textbook = method), not an import.
```

## 4. Where this leaves the keystone

With G2 re-derived, the free emergent-time massive Dirac field — the keystone — has **every piece
framework-native at the retained-bounded tier, with no physics import**:

| Keystone piece | Status |
|---|---|
| chiral grading / partner chirality | retained (`Cl(3,1)`) + supplied |
| positive energy + microcausality | forced (T1/CAR) |
| OS2 / reflection positivity | derived (E2) |
| n-point hierarchy + continuum limit (G1) | established (E5) + reduces to rung A |
| **boost sector / Poincaré rep (G2)** | **re-derived on the framework; Nelson's theorem cited as method** |

The only textbook items remaining are *mathematical methods* (OS reconstruction, Nelson integration),
not imported physics conclusions.

## 5. Scope — what this establishes and what remains

**Establishes (exact / finite):**
- The Lorentz generators are the retained `Cl(3,1)` bivectors; `so(1,3)` closes; the Dirac operator
  is covariant; the finite framework boost is a genuine Lorentz boost; the spectrum is positive.
- The only textbook input is the Lie-algebra→group integration method (Nelson's theorem).
- Hence G2 is a framework derivation, not an import.

**Remains:**
- **Free `U=1` only** — interacting theory out of scope (the reconstruction note's G5).
- Nelson's theorem's analytic-vector domain is the standard free-field smooth-vector domain; the
  *method* is cited (not the physics). Does **not** touch the firewalled `r=1/2`.

## 6. Honest verdict

G2 — the keystone's last residual — was carried on the textbook OS theorem "not re-derived on the
framework's surface," which is the definition of an import. This note re-derives it: the Poincaré
generators are the framework's retained `Cl(3,1)` bivectors plus the retained `iso(3,1)`
translations; the Dirac operator is covariant under them; the spectrum is positive (companion T1).
The single textbook item — Nelson's Lie-algebra→group integration — is a *method*, supplying no
physics. So G2 becomes a framework derivation citing textbook methodology, and the keystone stands
built at the retained-bounded tier with **no physics import** anywhere in its construction.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded re-derivation. It does **not** claim the interacting theory; it
removes the import status of the free-field boost sector.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| G2 generators imported from the OS theorem | RULED OUT | generators are the retained `Cl(3,1)` bivectors + `iso(3,1)` |
| boosts not realizable on the framework | RULED OUT | finite framework boost is a genuine Lorentz boost (verified) |
| spectrum positivity imported | RULED OUT | `Ĥ ≥ 0` from CAR/T1 (companion, framework-native) |
| Lie-algebra→group integration | METHOD (cited) | Nelson's theorem — mathematical, no physics input |

**N2 — Wall-independence.** The generators/algebra (this note) and the integration method (Nelson)
are distinct; the framework supplies the former, textbook the latter.

**N3 — Hidden-wall scan.** Uses only the `Cl(3,1)` bivector algebra and the Dirac covariance; the
analytic-vector domain for Nelson is the standard free-field one, named not hidden.

**N4 — Residual matching.** The remaining items are the interacting theory and the (cited) Nelson
method — not an imported boost conclusion.

**N5 — Rhetoric audit.** The claim is a *re-derivation removing import status*, not a new physics
result; the boost sector's content was always standard — the point is it is now framework-native.

**N6 — Partial-closure path scan.** Beyond the free field, the interacting Poincaré representation is
the next program; not claimed here.

**N7 — Steelman.** A reviewer may hold that citing any theorem (Nelson, OS) is an import. The line
this note draws: importing a *physics conclusion* (e.g. "assume the boosts are self-adjoint") is an
import; citing a *mathematical method* that operates on framework-native inputs (generators, algebra,
positive `H`) is methodology — the same status as linear algebra or the spectral theorem, which the
repo's runners use throughout.

**N8 — Cross-cycle echo.** Consistent with the retained `Cl(3,1)`, the retained-bounded
`free_dirac_poincare_representation`, the companion T1 spectrum closure, and the OS reconstruction
note's G2 — converting its textbook-carried boost sector into a framework derivation without
overruling any by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the retained `Cl(3,1)`, the retained-bounded
  `iso(3,1)`, and the companion positive-spectrum closure; Nelson's theorem is cited as a
  mathematical method only.
- **No PDG/fitted load-bearing input; no new transcendental; no forcing of `r=1/2`.**

## 9. Command

```bash
python3 scripts/frontier_os_g2_boost_poincare_rederived_on_framework.py
```

Expected: `TOTAL: PASS=9 FAIL=0`. numpy + stdlib, deterministic, 4×4 (memory-safe). The runner
verifies the `so(1,3)` algebra of the `Cl(3,1)` bivectors, the Lorentz-vector covariance of the
gammas, the finite Lorentz boost, the unitary/non-unitary Hermiticity structure, and the `±E`
spectrum.
