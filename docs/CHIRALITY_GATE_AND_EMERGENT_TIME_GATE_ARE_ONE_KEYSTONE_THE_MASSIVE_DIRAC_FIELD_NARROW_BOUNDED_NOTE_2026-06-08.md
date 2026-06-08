# The Koide Chirality Gate and the Emergent-Time Gate Are One Keystone — the Massive Dirac Field

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a retention-roadmap reduction / keystone locator)
**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit verdict. Effective status is pipeline-derived after independent audit and
dependency closure.
**Primary runner:**
[`scripts/frontier_chirality_gate_emergent_time_massive_dirac_keystone.py`](../scripts/frontier_chirality_gate_emergent_time_massive_dirac_keystone.py)
**Cached log:**
[`logs/runner-cache/frontier_chirality_gate_emergent_time_massive_dirac_keystone.txt`](../logs/runner-cache/frontier_chirality_gate_emergent_time_massive_dirac_keystone.txt)
(TOTAL: PASS=11 FAIL=0)

## 0. The reduction

Several of the framework's deepest residuals are routinely described as separate deep gates:
the Koide **chirality gate** (the chiral grading needed for `Q=2/3` Dirac mass generation),
**generation identification** (the chiral labeling), and the program's highest-descendant open
gate, the **emergent-time** `s3_time` slice coupling (~819 desc). This note shows they are **one
keystone**, and that its **algebra is already retained** — the residual is purely field-theoretic.

Two facts collapse them:

1. **The chiral grading is retained, not missing.** The retained
   [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md)
   supplies the `Cl(3,0)→Cl(3,1)=M_4(R)` doubling (`e_4`, `e_4²=−1`), i.e. the 4-component Dirac
   bispinor with the chiral grading `γ_5` on the **separate** L/R factor. And the
   [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
   (`retained_bounded`) is **narrow**: it forbids only the *hybrid* identification
   `γ_CL = Γ_χ` on a single generation `R³` — it **explicitly does not** address the standard
   separate-factor structure `R³ ⊗ (H_L ⊕ H_R)`, `γ_5 = I_3 ⊗ σ_3`. So the chiral grading the
   "wall" supposedly blocks is the wrong object.

2. **The retained Cl(3,1) supplies the complete massive-Dirac algebra** (verified): the
   positive-energy spectrum, the chiral grading, and the chiral mass coupling. Nothing algebraic
   is missing.

Therefore the chirality gate's only residual is the **field-theoretic realization** — exactly the
"partner-chirality / massive doubling" residual named by the retained-bounded
[`KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md)
— which **is** the emergent-time gate. **One keystone.**

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| `Cl(3,0)→Cl(3,1)=M_4(R)` (`e_4`, `e_4²=−1`): the chirality-doubling step | [`CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27`](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md) | `retained` | supplies the chiral grading on the separate factor |
| the no-go is narrow: only the hybrid `γ_CL=Γ_χ` on one `R³`; separate-factor structure untouched | [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md) | `retained_bounded` | scopes the "wall" |
| the partner-chirality / massive-doubling field residual | [`KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02`](KOIDE_ONSITE_BOOST_RECONSTRUCTION_WEYL_FAITHFUL_VS_SCALAR_SELECTION_NOTE_2026-06-02.md) | `retained_bounded` | names the residual |
| `H=iD` real anti-Hermitian / CPT structure | [`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained_bounded` | the massless dynamics |

No PDG value is load-bearing. No new axiom, import, or vocabulary.

## 2. The retained Cl(3,1) supplies the complete massive-Dirac algebra (verified)

The runner builds the 4-component Dirac matrices realized by `Cl(3,1)` and verifies:

- **(ALG)** `{α_i,α_j}=2δ_{ij}`, `{α_i,β}=0`, `β²=I`; and `H = α·p + βm` gives
  `H² = (p²+m²)I` → **positive-energy** spectrum `±√(p²+m²)` (two `+E`, two `−E`; bounded below
  under CAR).
- **(CHI)** `γ_5` is a chiral grading: `γ_5²=I`, `Tr γ_5 = 0` (balanced L/R); it **commutes** with
  the massless `H=α·p` (chirality conserved) and **anticommutes** with the mass term `β` — so `β`
  couples `L↔R` (`P_L β P_L = 0`, `P_L β P_R ≠ 0`): a genuine **chiral Dirac mass**.
- **(SEP)** `γ_5` lives on the **separate** 2-dim L/R factor (`γ_5 = I_3 ⊗ σ_3` on
  `R³ ⊗ (H_L⊕H_R)`); the no-go's `Γ_χ = (2/3)J − I` lives on the 3-dim **generation** factor —
  different operators on different spaces. The narrow no-go does not touch the separate-factor
  `γ_5`.

So the massive Dirac **algebra** — positive-energy spectrum, chiral grading, chiral mass — is
present and retained.

## 3. One keystone

With the algebra discharged, the chirality gate's only residual is the **field-theoretic
realization**: the framework's emergent-time field on `Z³` realizing the retained `Cl(3,1)`
doubling as a **positive-energy, microcausal, boost-covariant massive Dirac field** (the
onsite-boost partner-chirality residual). That realization is precisely the emergent-time
`s3_time` slice/coupling gate. Hence:

```text
  Koide chirality gate  =  Q=2/3 chiral-mass mechanism  =  generation-ID chirality
                        =  the #1 emergent-time s3_time gate
                        =  ONE keystone: the emergent-time massive Dirac field.
```

This is the single highest-leverage retention target: building it would retire the chirality gate
and its dependents (the Koide-Q mechanism, generation-ID) **and** the program's largest open-gate
subtree at once.

## 4. The retention roadmap this locates

Full unbounded retention of the charged-lepton flavor sector reduces to a small, explicit set,
with this keystone dominating:

| Item | Current status | What retention needs |
|---|---|---|
| cone `r=1/2 ⟺ Q=2/3` | **firewalled (registered)** | nothing — registered pattern, not a derivation target |
| `\|δ\|=2/9=L₃(1,2)` | retained_bounded | discharge the bridge to a concrete `Z_3`-equivariant Dirac η |
| chiral grading | **retained** (`Cl(3,1)`) | nothing — supplied on the separate L/R factor |
| **chirality gate = emergent-time massive Dirac field** | **the keystone** (algebra retained; field residual) | **build the positive-energy massive field on `Z³`+emergent-time** (this note's target) |
| radian unit (`2/9` rad vs `2π/9`) | admission | a period-1 normalization theorem |
| EW scale (`m_W/256`), magnitude `I1` readout | admitted/empirical | separate derivations |

## 5. Scope — what this establishes and the residual

**Establishes (exact / finite):**
- The chiral grading is retained (`Cl(3,1)`, separate factor); the narrow no-go does not block it.
- The retained `Cl(3,1)` supplies the complete massive-Dirac algebra (positive-energy spectrum,
  chiral grading, chiral mass coupling) — verified.
- Therefore the chirality gate, the `Q=2/3` mechanism, generation-ID, and the emergent-time gate
  reduce to **one** field-theoretic keystone.

**Does NOT establish (the keystone itself — the deep remaining work):**
- It does **not** build the emergent-time massive Dirac field (positive-energy, microcausal,
  boost-covariant) on `Z³`+emergent-time. That is the named residual and the real frontier.
- It does **not** force or touch the firewalled `r=1/2`.

## 6. Honest verdict

The "chirality wall" is a scoping illusion: the chiral grading is retained (`Cl(3,1)`, separate
L/R factor), the blocking no-go is narrow (only the hybrid identification), and the retained
algebra is a complete massive-Dirac structure. What actually remains — the chirality gate's true
residual — is **one keystone**: the emergent-time field realizing the doubling as a
positive-energy massive Dirac field. Building it would retire the chirality gate, the `Q=2/3`
chiral-mass mechanism, generation-ID, and the program's #1 emergent-time gate together. This note
discharges the algebra and locates the keystone; constructing the emergent-time massive field is
the deep frontier work it points to.

## 7. No-Go Discipline Gate

**Status:** PASS for this bounded reduction. It does **not** claim the keystone is built or that
the field realization is easy; it claims the algebra is complete and the residual is purely
field-theoretic.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| chiral grading is missing / blocked | RULED OUT | retained `Cl(3,1)`; no-go is narrow (hybrid only) |
| massive-Dirac algebra incomplete | RULED OUT | positive-energy spectrum + chiral grading + chiral mass verified |
| chirality gate, gen-ID, emergent-time as separate gates | UNIFIED | one keystone: the emergent-time massive field |
| build the emergent-time massive field | OPEN KEYSTONE | the named residual / the frontier |

**N2 — Wall-independence.** The algebra (this note) and the field realization (the keystone) are
distinct; discharging the first does not build the second.

**N3 — Hidden-wall scan.** Uses only the Dirac-Clifford algebra of the retained `Cl(3,1)` and the
no-go's explicit scope; no hidden field-theoretic premise.

**N4 — Residual matching.** The residual is exactly the emergent-time positive-energy massive
Dirac field, not an algebraic gap.

**N5 — Rhetoric audit.** The claim is a *reduction* (algebra retained + residual located), not a
derivation of the keystone.

**N6 — Partial-closure path scan.** The next step is the emergent-time massive-field construction
(spectrum condition + microcausality + boost covariance on the reconstructed Hilbert space). No
new axiom requested.

**N7 — Steelman.** A reviewer may hold the narrow no-go still threatens the *generation*-factor
chirality. Granted only for the hybrid identification; the standard `γ_5 = I_3 ⊗ σ_3` chirality on
the separate factor (which the massive Dirac field uses) is untouched — verified.

**N8 — Cross-cycle echo.** Consistent with retained `Cl(3,1)`, the retained-bounded onsite-boost
residual, the narrow no-go, and the retained CPT structure — unifying them without overruling any
by prose.

## 8. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained / retained-bounded rows
  plus the textbook Dirac-Clifford algebra.
- **No PDG/fitted load-bearing input; no new transcendental; no forcing of `r=1/2`.**

## 9. Command

```bash
python3 scripts/frontier_chirality_gate_emergent_time_massive_dirac_keystone.py
```

Expected: `TOTAL: PASS=11 FAIL=0`. numpy + stdlib, deterministic, 4×4 / 3×3 (memory-safe). The
runner verifies the Dirac-Clifford relations, the positive-energy massive spectrum `H²=p²+m²`, the
chiral grading `γ_5` (commutes massless, anticommutes mass, balanced L/R), and the separate-factor
distinction from the no-go's generation grading `Γ_χ`.
