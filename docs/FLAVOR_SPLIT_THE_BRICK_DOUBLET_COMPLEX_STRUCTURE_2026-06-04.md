# Flavor — split the brick: the generation factor carries a commuting C₃-equivariant complex structure J on its doublet (holomorphic-readout scaffolding that exists), distinct from the forbidden anticommuting grading; the "three-gate brick" is three objects, and strong-CP decouples to a spacetime reality structure

**Date:** 2026-06-04
**Claim type:** a structural reframe + a positive theorem (the doublet complex structure exists and is distinct from the no-go object; the three gates decouple). Not a value derivation — J is necessary scaffolding, not sufficient for Q=2/3.
**Status authority:** independent audit lane only. This note sets no audit status and assigns no grade. It does not edit, re-cite, or promote any existing row.
**Runner:** `scripts/flavor_split_the_brick_doublet_complex_structure_2026_06_04.py` (SCORECARD 7/7).

## The reframe
A reconnaissance warm-up (assumptions / first-principles / literature / mathematics / semantics, with a
citation-integrity pass) found that the supposed single "chiral/holomorphic grading on the generation R³
factor" shared by three gates (strong-CP, Koide Q=2/3, generation-ID) is **three distinct objects**, and
the genuinely-useful one **already exists**. This note proves it.

## The positive theorem — the doublet complex structure exists
On the generation factor `R[Z₃] = ℝ ⊕ ℂ`, define
```
J = (C − Cᵀ)/√3 = (C − C²)/√3 .
```
Verified (runner 7/7):
- `J` is **antisymmetric** (`Jᵀ=−J`) with `eig(J)={0, +i, −i}`;
- `J² = −I` on the **2-dim doublet** and `0` on the **all-ones singlet** — an **almost-contact** structure
  (a genuine complex structure on the doublet distribution; the all-ones vector is the real "Reeb" axis).
  This is the *odd-dim-correct* substitute for the (nonexistent) global `J` on `R³`;
- `J` is **C₃-equivariant** (`[J,C]=0`);
- `J` **commutes** with every circulant mass operator `H = aI + bC + b̄C²` (`[J,H]=0`, `{J,H}≠0`).

So `J` is a **holomorphic-readout** object — *not* an anticommuting chiral grading. It lives entirely
**outside** both obstructions that made "the brick" look hard:
- the **odd-dim wall** (no `J²=−1` on `R³`): `J` lives on the *even-dim* doublet, with the singlet as the
  real Reeb axis — no global-`J`-on-`R³` is needed or claimed;
- the **retained anticommuting no-go** (`koide_z3_equivariant_anticommuting_no_go`): that no-go forbids a
  C₃-equivariant operator *anticommuting* with a grading; `J` **commutes** with `H`, so the no-go never
  applied to it.

## Two objects, not one
The no-go's `Γ_χ = (2/3)J_allones − I` (eig `{1,−1,−1}`, `Γ_χ²=I`) is a **different** object: it too
**commutes** with every circulant `H` (so it never graded `H` chirally), and `Γ_χ ≠ J`. The "brick" framing
**conflated** the commuting holomorphic `J` (which exists) with a (non-existent) anticommuting grading —
importing the worst obstruction onto a problem that does not have it. "Generation chirality" has no lab
referent (e/μ/τ are not L/R partners); the borrowed word, not the physics, created the obstruction.

## Strong-CP decouples
The strong-CP reality antiunitary is a **spacetime/Dirac ε-grading** object (`εD + Dε = 0` on the
spacetime factor), C₃-trivial on the generation index — **not** a generation-factor structure (the
framework's audited strong_cp runner and the Nelson-Barr / Vecchi-2025 templates locate it on
spacetime+fields). Verified here that the generation factor carries **no** anticommuting chiral object for
a circulant `H` (`comm(C) ∩ anticomm(Γ_χ) = {0}`), consistent with strong-CP not living there.

## The corrected map and the sole residual
The "one brick, three gates" picture is replaced by:
- **strong-CP** = a *spacetime* reality structure (separate problem; Nelson-Barr-type template);
- **Koide-scaffolding + gen-ID-orientation** = the **doublet `J`** (exists, proved here);
- the **only genuinely-open residual** = a single **discrete bit**: signed/`det_C` (→ r=1/2 → **Q=2/3**)
  vs unsigned/`det_R` (→ r=1 → **Q=1**) readout.

**Honest boundary:** `J` is necessary scaffolding but **not sufficient** — it does *not* pin
`|b|²/a² = 1/2`. Both readings sit on the *same* `J`; the value is the one discrete readout bit. So the
prize is no longer "build a chiral grading" (mis-posed, obstructed) — it is the sharp, well-isolated
question: **is the RECORD axiom's additive scalar readout sign-sensitive** (→ signed/`det_C` → Q=2/3) **or
sign-blind** (→ Born/`det_R` → Q=1)? That is the dedicated follow-on target.

## Verified literature context (citation-integrity-checked)
- Nelson-Barr (arXiv:2203.09002, 2010.02891): θ̄=0 from a spontaneously-broken reality structure with
  calculable `arg det M` — the template for the decoupled strong-CP half.
- Connes NCG SM (hep-th/0705.0489): the chiral grading sits on the L/R qubit factor with generations as a
  trivial 3-fold multiplicity — independently mirrors "γ inert on generations."
- Non-holomorphic modular flavor (arXiv:2406.02527): holomorphy is *optional* (real models fit lepton
  data) — corroborates "signed/`det_C` vs real/`det_R` is a free measure choice," i.e. the residual bit.

## The next paths this opens (not closing)
- **The residual bit:** is the RECORD readout sign-sensitive? (the dedicated value-forcing attack).
- **Strong-CP (decoupled):** a native, no-new-fields Nelson-Barr-type reality structure on spacetime+fields.

## Provenance (verified 2026-06-04)
- `J` antisymmetric, `eig(J)={0,±i}`, `J²=−I` on doublet / `0` on singlet, `[J,C]=0`, `[J,H]=0` with
  `{J,H}≠0`; `Γ_χ` commutes with `H` and `Γ_χ≠J`; no circulant anticommutes with `Γ_χ`: verified directly
  (runner 7/7). Retained anchor on origin/main: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded),
  whose §4 self-lists the escapes used here (commuting object / even-dim sub-factor).
- This note sets no audit status; it proves the doublet complex structure, splits the conflated brick into
  three objects, decouples strong-CP, and isolates the one discrete residual bit.
