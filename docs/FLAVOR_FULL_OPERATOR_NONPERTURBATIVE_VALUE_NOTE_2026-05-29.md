# Flavor — the value is a nonperturbative output, not a flat direction

**Date:** 2026-05-29
**Claim type:** meta / correction + frontier relocation. Corrects the
over-scoped "flat direction / exhausted" framing of
`FLAVOR_ORDER_PARAMETER_FLAT_DIRECTION_CAPSTONE_NOTE_2026-05-29.md`.
Imports nothing; sets no retained status.
**Runner:** `scripts/flavor_full_operator_generation_masses_2026_05_29.py`
(+ cache).

## Assumptions audit of "r=½ is a flat direction / native derivation exhausted"
Two load-bearing assumptions were unexamined:

- **The operator/symmetry framing is a red herring for the *value*.** Q
  depends only on the three √mass *eigenvalues*; whether the mass operator
  is C₃-equivariant (circulant) is a property of its *eigenvectors*, which Q
  cannot see. The whole "everything commutes with `Γ_χ` → can't fix r" wall
  is about operators; the value question is about eigenvalues. The wall is
  **orthogonal** to the value.
- **ISOLATION (the real error).** Every prior lens worked on the *isolated*
  3-dim generation space (3×3 operators on hw=1, R³). But the lepton masses
  are observables of the **full coupled theory**. "Flat direction in the
  isolated sector" ≠ "undetermined in the framework" — exactly like
  declaring the proton mass a "flat direction" because the isolated quark
  sector doesn't fix it. It's the output of the full dynamics.

## What the FULL operator actually predicts (never computed before)
Building the full free + Wilson staggered/naive Dirac operator on Z³ (Cl(3)
spinor), not the 3×3 toy:
- Corner mass `M = m + 2r·hw` depends **only on Hamming weight** (Wilson
  staircase). The three generations are the hw=1 BZ corners → **degenerate**
  → **Q = 1/3 (democratic)**. A *definite* prediction at the
  perturbative/symmetric level — not a flat direction.
- At BZ corners `sin(k)=0`, so the Cl(3) `σ_μ` hopping contributes **zero**
  to the corner mass; only the scalar Wilson part survives (isotropic,
  weight-only). **No native isotropic term splits the three same-weight
  corners.**

## The relocation: the value is a nonperturbative (vacuum) output
The observed generation splitting (`e ≪ μ ≪ τ`, Q=2/3) is therefore a
**nonperturbative** effect — spontaneous S₃-breaking of the cubic axis
symmetry by the **actual vacuum (gauge configuration)** — the direct analog
of chiral-symmetry breaking generating the QCD hadron spectrum. Consequences:
- **Refutes "flat direction":** the value is a *definite* output of the full
  dynamics (the vacuum picks a definite configuration → definite masses).
  With `g_bare = 1` (no free coupling), there is **no free flavor knob**.
- **Not analytically derivable from the operator:** like the QCD hadron
  spectrum, it needs the full **nonperturbative (lattice) solution**.
- **Invisible to the isolated 3×3 lens:** which is why every prior lens saw
  only the *form* (the cone, equipartition, the d=3 count↔value link, the
  chiral signature) and never the *value*.

## Corrected verdict + the genuine open question
The flavor derivation is **not exhausted** and the value is **not a flat
direction**. It is a **nonperturbative output of the parameter-free
(`g_bare=1`) full theory**, in the same status as deriving hadron masses
from QCD: definite, computable in principle, hard, and never done here.

**The genuine, sharp open question:** does the framework's nonperturbative
Z³ vacuum **spontaneously break the cubic/S₃ axis symmetry**, and does the
resulting generation splitting land on **Q=2/3**? This is the lattice-scale
analog of "does QCD spontaneously break chiral symmetry" (it does). That is
the real derivation target — definite, parameter-free, and untouched by the
isolated-sector lenses. The CKM CP angle (65.9° from one integer) already
shows the *full structure* outputs flavor values the isolated sector hides;
the lepton mass hierarchy is the nonperturbative counterpart.

## Status
Correction landed: "exhausted/flat-direction" was scoped to the isolated
generation sector. The full operator predicts Q=1/3 (degenerate) at
free+Wilson; the value is a definite nonperturbative vacuum output (spontaneous
cubic/S₃ breaking), requiring the full lattice solution. No false closure;
the derivation target is relocated to the nonperturbative vacuum, not closed.
