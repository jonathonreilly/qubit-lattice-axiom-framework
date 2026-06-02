# Matter-Attachment Reduces to the Kawamoto-Smit Audit

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded localization. The native single-component staggered
operator and operator-frame merger do not by themselves force a matter-state
spinor law; the only forcing route identified here runs through the unaudited
Kawamoto-Smit reconstruction. This note does not apply that audit, promote
Kawamoto-Smit, force matter attachment, or set an audit verdict.
**Primary runner:** [`scripts/frontier_koide_matter_attachment_reduces_to_ks.py`](../scripts/frontier_koide_matter_attachment_reduces_to_ks.py)
## Context

The charged-lepton carrier-frame program reduced the faithfulness leg
(the matter operator `M` in a faithful boost-acting Weyl representation
versus the trivial `J = K = 0` scalar) to a single upstream
**matter-attachment** posit, recorded in the companion faithfulness note:

> matter FIELD index = the per-site `C^2` qubit STATE carries the
> `j = 1/2` SPINOR rep of the PHYSICAL spatial rotation as its
> transformation LAW.

The internal-external `su(2)` merger
(`internal_external_su2_merger_from_universal_property_narrow_theorem_note_2026-05-27`,
cited bounded authority) and `per_site_su2_spin_half_theorem_note_2026-05-02`
establish the OPERATOR-FRAME fact that `S_i = sigma_i/2` and
the Clifford `Spin(3)` bivector triple are the same operator triple on
`C^2`, with `U(R)` acting by CONJUGATION on the gamma operators. This note
asks the sharp question one level higher: does the native first-order real
anti-Hermitian `D`, together with the merger and emergent Lorentz structure,
force the matter-attachment without the unaudited Kawamoto-Smit
reconstruction?

## Claim

The matter-attachment is **not forced Kawamoto-Smit-free**. It **reduces to
the Kawamoto-Smit audit**: the only route identified here that forces the on-site `C^2` to
carry the matter spin-1/2 rides the unaudited
`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`, with an
admitted-not-forced elementary fallback. Consequently faithfulness does NOT
collapse to the `(3,1)` signature plus carrier-identification; the
matter-attachment survives as a live pin whose only forcing route is the KS
audit.

Three facts, all verified by the runner and non-circular (the faithful rep
and `Q = 2/3` are never assumed):

### A. The native `D` is single-component and spin-blind on `C^2`

The native first-order real anti-Hermitian operator
(`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`,
cited bounded authority; `H = iD`) is single-component scalar hopping on
`C^N` indexed by SITES, with NO per-site spinor index:

```text
D real antisymmetric  (H = iD Hermitian),
-D^2 = scalar lattice mass-shell {0, 4, 8, 12}   (no spinor structure),
[H (x) I_2, I (x) sigma_i/2] = 0                  (spin-blind on the C^2).
```

So nothing in `D` itself attaches a spinor index to the on-site `C^2`.

### B. The merger is OPERATOR-FRAME (adjoint), one level below the matter-state law

The merger delivers the ADJOINT action: `U(R) = exp(i theta . S)` rotates
the gamma OPERATORS as a 3-vector by conjugation,

```text
U(R) sigma_i U(R)^dag = R_ij sigma_j.
```

This is the covariance of the operators, not a transformation LAW on the
matter ket. `per_site_su2_spin_half` withholds exactly the upgrade to a
matter-state law: its disclaimer is TWO carve-outs joined by "or" -- the
first ("the physical spin generator of every matter excitation") is
unrestricted, not merely a composites carve-out -- and its C3 boundary
states it "does not derive the physical rotation generator on multi-site
states." So the elementary single-site attachment is neither asserted nor
refuted by the retained stack.

### C. The Kawamoto-Smit bridge supplies the matter-state spinor

The `C^2`-spinor structure of the naive two-component Dirac operator is
diagonalized AWAY into the single-component staggered phases by the
Kawamoto-Smit operator
`Omega(x) = sigma_1^{x_1} sigma_2^{x_2} sigma_3^{x_3}`:

```text
Omega(x)^dag sigma_mu Omega(x + e_mu) = eta_mu(x) I,
```

where `eta_mu(x)` is the staggered phase (a SCALAR). The matrix spinor
generator `sigma_mu` becomes a scalar lattice phase. So the operator
translating "spin-rotation `U(R)`" into the single-component "sign field"
IS `Omega` -- the Kawamoto-Smit reconstruction
(`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`,
**unaudited**; upstream `staggered_dirac_grassmann_forcing_theorem_note_2026-05-07`,
**unaudited**). KS Step 4 runs in the OPPOSITE direction: the per-site
dim-2 carries a SINGLE Grassmann occupation mode, NOT a two-component
matter spinor (spin diagonalized into local phases; the Dirac index rebuilt
from the `(Z_2)^3` corner/taste cube).

The matching dynamical fact: under a spatial lattice rotation the native `D`
is restored to invariance by a purely single-component diagonal sign field
`W in {+1, -1}` (no `C^2` index) -- a `C^2` spin rotation `U(R)` is NOT
required. The `C^2`-spin reading of that compensator is available only
through `Omega`. So the dynamics route to matter-spin-1/2 is not KS-free.

## What is landable, and what is not

**Landable (this note):** the matter-attachment REDUCES TO AUDITING the
Kawamoto-Smit reconstruction, with an explicit admitted-not-forced fallback.

**Not landable (false):** "the faithfulness value collapses to the `(3,1)`
signature plus carrier-id." The clean-looking elementary route is
admitted-not-forced, so the value does not collapse to the signature alone.

## The precise residual

ONE binary fact: does the matter FIELD index = the per-site `C^2` qubit
STATE carry the `j = 1/2` SPINOR (fundamental / left) rep of the PHYSICAL
spatial rotation as its transformation LAW, versus the operator-frame
3-vector CONJUGATION covariance the merger actually proves? This residual
sits exactly one level ABOVE the merger (which is clean for what it proves):
the gap is

```text
operator-frame  J = sigma/2   (adjoint, conjugation on gamma operators)
        -->     matter-STATE spinor law   (fundamental, action on the ket),
```

and that upgrade is precisely what the Kawamoto-Smit reconstruction
supplies.

Two disjoint discharge routes, neither currently reusable as retained-grade:

- **(B, the forcing route)** reconstruct the matter-spinor index from the
  staggered corner/taste structure of the spin-blind single-component native
  `D` = `staggered_dirac_kawamoto_smit_forcing` (**unaudited**; upstream
  `staggered_dirac_grassmann_forcing` **unaudited**). The pin reduces to the
  KS audit.
- **(A, the elementary route)** posit directly that the single-site
  excitation STATE index is the spatial-rotation spinor =
  **admitted-not-forced**, at the `per_site` C3 open scope-boundary, supplied
  by no retained row.

`cl3_to_cl31_spinor_extension_narrow_theorem_note_2026-05-27`
independently forecloses substituting the `(3,1)` Majorana `R^4` boost
spinor for the per-site `C^2`: the per-site Hilbert space stays `C^2`-valued;
the `M_4(R)` action lives on the abstract real Clifford algebra, not the
per-site site module.

## Load-bearing authorities

[INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md](INTERNAL_EXTERNAL_SU2_MERGER_FROM_UNIVERSAL_PROPERTY_NARROW_THEOREM_NOTE_2026-05-27.md),
[PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md](PER_SITE_SU2_SPIN_HALF_THEOREM_NOTE_2026-05-02.md),
[CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md),
[CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md](CL3_TO_CL31_SPINOR_EXTENSION_NARROW_THEOREM_NOTE_2026-05-27.md),
and
[FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md](FERMION_PARITY_Z2_GRADING_THEOREM_NOTE_2026-05-02.md).

Non-load-bearing audit targets remain plain text:
`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` and
`staggered_dirac_grassmann_forcing_theorem_note_2026-05-07`.

## Non-circularity

The forward checks are tier verification, prose verification, and direct
computation, none of which uses the faithful representation or `Q = 2/3`.
The KS-bridge identity and the spin-blindness of `D` are basis-independent
matrix facts. The reduction is stated as a localization, not a forcing.

## Next paths this opens

- Audit `staggered_dirac_kawamoto_smit_forcing` (and upstream
  `staggered_dirac_grassmann_forcing`). If they pass, Route B becomes
  reusable modulo the merger and KS bounded tiers, and forces the
  matter-attachment.
- Derive a new retained state-level rotation-covariance theorem that
  promotes the merger's operator-frame conjugation covariance to a
  matter-STATE spinor transformation law -- a "fundamental-action" theorem
  coupling `D`'s single-component hopping to the per-site `su(2)` as the
  elementary lepton FIELD index. Route A then becomes clean.
- Test whether emergent Lorentz / the boost lever can promote the
  operator-frame automorphism to a state-level law without the corner cube;
  if it cannot, the attachment is an independent posit.
- Derive a principle privileging the genuine spin-lift `U(R)` over the
  spin-blind scalar sign field `W` (forcing the per-site qubit to BE the
  diagonalized Dirac spinor rather than a spectator).

This is a localization of the matter-attachment pin to a concrete tiered
target, not an enumeration of routes.
