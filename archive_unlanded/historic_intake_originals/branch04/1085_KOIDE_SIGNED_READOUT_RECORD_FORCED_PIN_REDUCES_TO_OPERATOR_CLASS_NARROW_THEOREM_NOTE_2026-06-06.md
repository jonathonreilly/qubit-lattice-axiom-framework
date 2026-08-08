# Koide Signed Readout is Record-Forced (given Hermitian); the Pin Reduces to the Operator Class — Narrow Bridge Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (narrow sharpening) + bounded reduction
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can
decide whether the candidate is retained.
**Primary runner:** [`scripts/signed_readout_record_forced_runner.py`](../scripts/signed_readout_record_forced_runner.py)
**Cached output:** [`logs/runner-cache/signed_readout_record_forced_runner.txt`](../logs/runner-cache/signed_readout_record_forced_runner.txt)

## Audit context

After [`PMNS_TRIMAXIMAL_PARTITION_IS_KCPT_ORBIT_AXIOM_DIRECT_NARROW_THEOREM_NOTE_2026-06-06.md`](PMNS_TRIMAXIMAL_PARTITION_IS_KCPT_ORBIT_AXIOM_DIRECT_NARROW_THEOREM_NOTE_2026-06-06.md)
showed the singlet⊕doublet partition is the RECORD K/CPT-orbit (axiom-direct), the Koide
"`δ=0` / K-reality / Brannen / chirality" pin reduces to the **signed (Hermitian-
eigenvalue, Brannen/det_R) vs singular-value (`|λ|`/Yukawa) readout class**
([`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29`](KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md),
`retained`: `Q(signed) = 2/3` is `θ`-independent at `r=1/2`; `Q(|λ|) ≤ 2/3`).

This note does two things. **(1) Land:** the record *forces* the signed readout **given a
Hermitian generation observable** — so the readout class is not a free choice, and the
residual is *purely* the operator class. **(2) Push:** the live welding route (the
generation `C^3` is the hw=1 *subspace* of the site-qubits, so the site K/CPT restricts
to it — escaping the factor-split no-go). It is **honest about the remaining gap** (the
`√m`-sign recorded-vs-absorbed question; the Dirac/SVD steelman) and does **not** claim
the operator class is settled.

## Safe statement

### Part 1 (Land) — the record forces the signed readout given Hermiticity

A recorded observable is self-adjoint (the readout `I` is a real scalar; central sectors
are real outcomes). A self-adjoint `H` has real spectrum, so each eigen-phase
`arg(λ_k) ∈ {0, π}` is a **`Z_2` sign**, not a continuous `U(1)` phase. Under the K/CPT
conjugation `K`, a real eigenvalue is **K-fixed** (its own orbit), so the RECORD axiom's
"outcome = K/CPT orbit" registers the **signed** eigenvalue. The singular-value `|λ|`
reading is a *further* reduction that **discards the K-fixed sign — a recorded datum**.

**Theorem 1.** Given a Hermitian generation observable, the signed (`λ_k`) readout is the
record-native one and `|λ_k|` is not. Hence the "signed-vs-singular readout class" is
**not a free choice** at the record level; the Koide residual is **purely the operator
class** — *which* operator the record registers, not *how* its spectrum is read.

### Part 2 (Push) — the live welding route

The generation space `C^3` is the **hw=1 subspace** of the three site-qubits
`(C^2)^{⊗3} = C^8` (the single-excitation states `|100>,|010>,|001>`), realized by an
isometry `V_1 : C^3 → C^8`. It is **not a tensor factor**. The site/qubit K/CPT (complex
conjugation on `C^8`) **restricts** to the generation K/CPT (conjugation in the corner
basis). The retained factor-split no-go
([`KOIDE_FACTOR_SPLIT_DOES_NOT_FORCE_CARRIER_VALUE_BRIDGE_NO_GO_NOTE_2026-06-02`](KOIDE_FACTOR_SPLIT_DOES_NOT_FORCE_CARRIER_VALUE_BRIDGE_NO_GO_NOTE_2026-06-02.md),
`retained_no_go`) is about product **factors**; its own steelman (N7) names this
single-carrier route — "one reality structure acting on both the site and generation
factors" — as the **live** missing welding link. The hw=1-**subspace** restriction is
exactly that route, and it is not a factor split.

On that subspace the generation circulant `M = aI + bC + b̄C²` is Hermitian
(`M = M^†` for real `a`), so its eigenvalues are the **signed** `√m_k`, the recorded
data of Theorem 1.

## The honest gap (not discharged)

The Dirac/SVD steelman
([`KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05`](KOIDE_DIRAC_MASS_FORCES_R_ONE_LR_COUPLING_BERRY_FLAT_BOUNDED_NO_GO_NOTE_2026-06-05.md),
`unaudited` bounded no-go) reads the masses as the **singular values** of `M`: the Dirac
operator `[[0, M],[M^†, 0]]` has eigenvalues `±(eig of M)`, and its positive spectrum is
`|eig(M)|` — which **absorbs the sign** (the standard chiral-phase convention that the
`√m` sign is unphysical, rotatable into `e_R`).

So the operator-class residual is, sharply: **is the `√m` sign RECORDED (the eigenvalue
sign of the Hermitian generation `M`) or ABSORBED (the SM chiral convention)?** The
record ontology favors *recorded* (the sign is the K-fixed eigenvalue of the recorded
observable; "absorb into `e_R`" is a Lagrangian-basis reconstruction, not a record
operation). But this is **not proven here** — the SVD/singular-value reading is a live
alternative. This note **reduces** the chirality pin to this single record-vs-
reconstruction question; it does **not** close it.

## Boundary

- **Does NOT settle the operator class.** Whether the `√m` sign is recorded vs absorbed
  is the open step (the Dirac/SVD steelman is live, `unaudited` bounded no-go).
- **Part 1 is conditional on Hermiticity.** It says signed-is-forced *given* a Hermitian
  observable; it does not by itself prove the native generation operator is Hermitian
  (the circulant is Hermitian by form; the records-mechanism Hermiticity is retained only
  on the site/spatial factor — `cpt_exact_real_anti_hermitian_d`, `retained_bounded`).
- **Does NOT derive the `δ=2/9` Brannen phase** (a separate gate; under guardrail G3 it is
  *registered* mass-pattern data, consistent with its retained no-gos that it is not
  convention-free-derivable).
- **Does NOT touch the Koide weight `r`** (separate registered datum, G3).

## Forbidden imports check

No new axiom or import. Uses the RECORD axiom's "outcome = K/CPT orbit" clause, the
retained hw=1 generation triplet, and finite matrix algebra. The note *removes* a
conflated piece (the readout-class choice) and *reduces* a residual; it adds no structure.

## Runner check breakdown

Class A finite-dimensional algebra: self-adjoint `H` has a signed real spectrum;
`Q(signed)=2/3` vs `Q(|λ|)≠2/3` (the `|λ|` reading discards the recorded sign); the
generation `C^3` is the hw=1 subspace (isometry, not a factor) and the qubit K restricts
to it; the Dirac `[[0,M],[M^†,0]]` has eigenvalues `±eig(M)` with positive spectrum
`|eig(M)|` (the sign-absorbing steelman). The two "honest gap"/synthesis lines are
documented `True` statements, not derivations. Expected `runner_check_breakdown =
{A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content is exact: signed-is-record-native-given-Hermitian (the K-fixed sign
is recorded; `|λ|` discards it), and the hw=1-subspace structure (not a factor). The
genuine advance is the *reduction*: it removes the readout-class as a separate residual
and isolates the chirality pin to one record-vs-reconstruction question (recorded vs
absorbed `√m` sign), with the hw=1-subspace welding route as the live escape the
factor-split no-go itself names. It does **not** discharge the gate: the Dirac/SVD
steelman is a live `unaudited` bounded no-go, and the records-mechanism Hermiticity is
retained only on the site factor. Effective status remains `unaudited` until the audit
lane assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/signed_readout_record_forced_runner.py
```
