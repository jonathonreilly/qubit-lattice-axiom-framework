# A Cubic O_h-Anisotropic Weight Breaks SO(3) Graviton Orbit-Flatness — Opening a Frame-Sectioning Channel the Isotropic Case Forecloses (spin-2 ↓ O_h = E ⊕ T2)

**Date:** 2026-06-17
**Type:** bounded_theorem
**Claim type:** bounded_theorem (positive structural theorem; bounded by the retained-bounded cubic `O_h` lift dependency)

**Claim scope:** On `Sym^2(R^4)` with the SO(3) spatial action `R = 1 ⊕ R_3` (temporal index
fixed), restricted to the spin-2 spatial complement `Sym^2_0(R^3)` (5-dim, the traceless-symmetric
graviton block): **(1)** the space of `O_h`-invariant quadratic weights is **2-dimensional**
(spin-0 Frobenius ⊕ spin-4 cubic harmonic), whereas the SO(3)-invariant weights are
**1-dimensional** (Frobenius only) — the gap is exactly one cubic-harmonic direction `G_aniso`.
**(2)** `G_aniso` splits the SO(3) spin-2 irrep into its `O_h`-irreps **E (2-dim) ⊕ T2 (3-dim)**
with distinct weights (eigenvalues `+√(3/10)` on E with multiplicity 2 and `−√(2/15)` on T2 with
multiplicity 3 — `2·√(3/10) − 3·√(2/15) = 0`, traceless), so the
`G_aniso`-weighted complement energy is **NOT** SO(3)-orbit-flat — while the SO(3)-isotropic weight
**is** orbit-flat, reproducing the retained
[`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md).
**(3)** The cubic lattice supplies a **nonzero** weight in exactly the `G_aniso` direction: the
leading rotational-symmetry breaking of the lattice-Laplacian dispersion `ω(k)=6−2Σ_i cos k_i` is
the `l=4` cubic harmonic, whose axis 4-tensor `C_ijkl = Σ_a e^a_i e^a_j e^a_k e^a_l`, as a quadratic
form on the graviton, has anisotropic part **equal to `G_aniso`** (computed residual `1.8e-16`); the
`l=4` harmonic is nonzero on the active lattice shells (the unaudited lattice-solved anisotropic orbit
mode `c_aniso`; the `l=4` anisotropy is recomputed here from `H`, not cited blind). **Consequence:**
the cubic lattice **opens a frame-sectioning channel**: the anisotropic-weighted graviton complement
energy is provably not SO(3)-orbit-flat — that the SO(3)-isotropic continuum forecloses; this is the
value-free structural lever, and the action-level activation of this weight into an actual frame
selection is the named follow-on (§4).

**Status authority:** independent audit lane only. This source note does not set, predict, or
estimate any audit outcome; effective status is pipeline-derived after independent audit.
**Loop:** science-fix lane 2026-06-17 (audit-frontier sweep → verified fourth lever).
**Runner:**
[`scripts/cubic_anisotropy_sections_so3_frame_2026_06_17.py`](../scripts/cubic_anisotropy_sections_so3_frame_2026_06_17.py)
**Cached log:**
[`logs/runner-cache/cubic_anisotropy_sections_so3_frame_2026_06_17.txt`](../logs/runner-cache/cubic_anisotropy_sections_so3_frame_2026_06_17.txt)
(`TOTAL: PASS=22 FAIL=0`, deterministic — SO(3) orbit probes use a fixed RNG seed while invariant
dimensions are checked by exact Lie-generator equations; runtime well under one minute; imports only numpy).
**Authority role:** source-note proposal. If independently ratified, supplies the value-free structural fact that a
cubic `O_h`-anisotropic background weight breaks SO(3) graviton orbit-flatness — opening a
frame-sectioning channel the isotropic case forecloses — filling the anisotropic-weight seam that the cited orbit-flat / scalar-trace / Casimir-class
results explicitly leave open.

## 1. The retained criterion this extends

[`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md)
(**retained**) proves that for any **isotropic** spatial weight `d = (d_0, d_s, d_s, d_s)`, the
diagonal-weighted complement energy `‖Π_perp(h)‖²_d` is **orbit-flat** (SO(3)-invariant), so no
stationarity of the quadratic energy selects a complement-frame section. Its own boundary states
the open seam verbatim: *"Whether anisotropic spatial weights yield a different selection picture …
non-isotropic backgrounds are outside the present scope."* This note answers that exact question for
the cubic `O_h` class supplied by the lattice.

## 2. Load-bearing inputs (one hop, fresh statuses on origin/main)

| Input | Role | Status |
|---|---|---|
| SO(3) orbit-flatness for isotropic weights (the criterion) | §1, [FLAT] isotropic leg recomputed | [`UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT…`](UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT_NARROW_THEOREM_NOTE_2026-05-10.md) — **retained** |
| cubic `O_h` action = signed coordinate permutations (from the Cl(3) axis structure on Z³) | the `O_h` group; [REP] | [`CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26`](CL3_OH_CUBIC_LIFT_FAITHFUL_NARROW_THEOREM_NOTE_2026-05-26.md) — **retained_bounded** |
| Z³ nearest-neighbour adjacency / lattice Laplacian `H = 6I − A` | [LATTICE]; dispersion recomputed here, not cited | [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md) — Lattice axiom |

Reader context only, not a load-bearing dependency: the lattice-solved anisotropic orbit mode
`c_aniso` on shells `(3,3,0),(4,1,0)` appears in
`LATTICE_LAPLACIAN_SHELL_LOCALIZATION_IDENTITY_BOUNDED_THEOREM_NOTE_2026-06-16.md`, which is
unaudited as of this note. This theorem does not cite that note as authority; it recomputes the
`l=4` anisotropy directly from `H = 6I - A`.

No fitted parameters, no observed values, no new axioms, no imports beyond numpy.

## 3. The theorem (computed; runner blocks [REP],[SPLIT],[FLAT],[LATTICE])

Let `h ∈ Sym^2_0(R^3)` be the spin-2 graviton block (5-dim), with the SO(3) spin-2 action and the
`O_h` = cubic rotation group (24 elements) action by `h → R h R^T`.

- **[REP]** The `O_h`-invariant symmetric quadratic forms on the spin-2 space are **2-dimensional**;
  the SO(3)-invariant ones are **1-dimensional** (and equal the Frobenius identity, residual `<1e-9`).
  The one extra `O_h` direction is `G_aniso` (the cubic-harmonic / spin-4 weight). This is the
  Schur-lemma fact `spin-2 ↓ O_h = E ⊕ T2`: two `O_h`-irreps ⇒ two independent `O_h`-invariant
  weights, vs one SO(3)-irrep ⇒ one SO(3)-invariant weight. **Non-triviality contrast:** the spin-1
  vector block (`h_{0i}`) restricts to the *irreducible* `O_h`-irrep `T1`, so by Schur its
  `O_h`-invariant weights are **1-dim = SO(3)** (Schur-forced isotropic) — a cubic background does
  **not** section the vector modes. The sectioning is therefore **mode-specific** to the spin-2
  tensor (the `E ≠ T2` split), not the tautology "any non-SO(3) weight breaks flatness".
- **[SPLIT]** `G_aniso` has exactly two distinct eigenvalues with multiplicities `{2, 3}` =
  `E ⊕ T2`, and is traceless — a genuine anisotropy, not an overall rescaling.
- **[FLAT]** The isotropic (Frobenius) complement energy is SO(3)-orbit-flat (max orbit-variation
  `1.2e-15` over 200 random SO(3) rotations — reproducing the retained theorem). The
  `O_h`-anisotropic energy `‖·‖²_{I + ½G_aniso}` is **NOT** orbit-flat (max orbit-variation `0.19`),
  yet the weight is **exactly** `O_h`-invariant (residual `<1e-9` over all 24 `O_h` elements). So the
  breaking is genuine and lives strictly within the `O_h`-allowed class: the anisotropic background
  opens the SO(3) frame-sectioning channel.
- **[LATTICE]** The cubic axis 4-tensor `C_ijkl = Σ_{a=1,2,3} e^a_i e^a_j e^a_k e^a_l` (the unique
  lowest `O_h`-invariant, SO(3)-non-invariant harmonic — the `l=4` cubic harmonic), as a quadratic
  form on the graviton, has anisotropic (traceless) part **equal to `G_aniso`**: `‖C_dev − 1.0954·G_aniso‖
  = 1.8e-16`. The `l=4` cubic harmonic `H_4(k)=Σ k_i^4 − (3/5)|k|^4` is nonzero on the active lattice
  shells (`(3,3,0): −32.4`, `(4,1,0): +83.6`, …), and the lattice dispersion's leading anisotropy is
  exactly this channel (`ω = |k|² − (1/12)Σ k_i^4 + O(k^6)`, and `Σ k_i^4 = (3/5)|k|^4 + H_4`). Hence
  the lattice's leading rotational-symmetry breaking and the graviton orbit-flat-breaking weight are
  **the same `O_h` object**, and the nonzero values above witness that the lattice activates it.

## 4. What this does and does not establish (the bound)

**Establishes (firewall-clean, value-free):** the binary structural fork is resolved in the positive
direction — a cubic `O_h`-anisotropic background weight on the graviton spin-2 complement is **not**
SO(3)-orbit-flat (the isotropic case is), and the lattice supplies a nonzero weight in precisely the
sectioning direction. The cubic lattice therefore opens the frame-sectioning channel — by breaking
the SO(3) orbit-flatness — that the isotropic
continuum forecloses, using only the Lattice axiom, the retained `O_h` lift, the retained isotropic
orbit-flat criterion, and finite representation theory.

**Does NOT establish (the honest bound, matching the lattice-shell note's own disclaimer):** this is
the value-free structural orbit-flat-breaking statement only. It does **not** supply a tensor-valued
GR matching VALUE (which is import-bounded — any specific matching number requires data the framework
does not derive); it does **not** supply the nonlinear / derivative-dependent GR action needed for an
actual Einstein-Hilbert completion; and it does **not** by itself close the polarization-frame-bundle
program. It identifies the **mechanism** (the `l=4`/spin-4 channel) by which a cubic background can
break SO(3) orbit-flatness in the frame sector, and proves that channel is open and lattice-activated.

## 5. The no-go seam this fills (each cited result explicitly disclaims this region)

Three route-results bracket — and explicitly leave open — exactly the anisotropic structural fork
proved here (statuses fresh on origin/main; the unaudited ones are used only as scope maps, their
arithmetic is not consumed):

- `UNIVERSAL_GR_SO3_ISOTYPIC_ORBIT_FLAT…` (**retained**): closes only the **isotropic** weight
  `d=(d_0,d_s,d_s,d_s)`; disclaims "whether anisotropic spatial weights yield a different selection
  picture." → this note answers it: they do.
- `SCALAR_TRACE_TENSOR_NO_GO_NOTE` (**unaudited**): closes only scalar-data repackaging; states "the
  only honest positive route left is a new **tensor-valued** matching law." → this note works in the
  tensor (`Sym^2`) sector, not the scalar one.
- `UNIVERSAL_GR_TENSOR_ACTION_CASIMIR_EQUIVARIANT_CLASS_NOGO_NOTE_2026-05-17` (**unaudited**): closes
  only **linear** Casimir-projector actions; explicitly lists as open "a NONLINEAR functional of h …
  derivative-dependent functionals." → the `G_aniso` weight is an `O_h`-equivariant quadratic form
  outside the linear Casimir-projector class; the full nonlinear/derivative GR action remains the
  named open follow-on (the bound in §4).

## 6. Boundary / honest-auditor read

The load-bearing content is finite, exact representation theory (block [REP]/[SPLIT], dimensions and
eigenvalue multiplicities at machine precision) plus the exact lattice→graviton tensor identity
(block [LATTICE], residual `1.8e-16`); the SO(3) orbit-variation probes ([FLAT]) are seeded but the
contrast (isotropic `~1e-15` vs anisotropic `~0.19`) is robust and convention-independent (it follows
from `E ≠ T2` by Schur). The result is a **positive structural lever**, not a completed GR matching;
the matching VALUE and the nonlinear action remain import-bounded / open, exactly as §4 states.
Whether this lever should be read as the mechanism that discharges the polarization-frame-bundle
selection blocker is for the independent audit lane and downstream work to decide; this note proves
only the orbit-flat-breaking fact and its lattice activation.
