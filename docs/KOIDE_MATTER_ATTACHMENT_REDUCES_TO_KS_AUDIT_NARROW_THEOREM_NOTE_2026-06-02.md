# Matter-Attachment Reduces to the Kawamoto-Smit Audit

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** bounded localization. The native single-component staggered
operator and operator-frame merger do not by themselves force a matter-state
spinor law; the positive route isolated here runs through the separate
Kawamoto-Smit reconstruction surface. This note does not apply or set any
audit verdict, does not promote Kawamoto-Smit beyond its own audited scope, and
does not force matter attachment on the current surface.
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
force the matter-attachment without the separate Kawamoto-Smit
reconstruction?

## Claim

The matter-attachment is **not forced Kawamoto-Smit-free**. It reduces to a
separate Kawamoto-Smit/state-law bridge question: the route identified here that
can carry an on-site `C^2` matter spin-1/2 reading goes through
`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`, with an
admitted-not-forced elementary fallback. Consequently faithfulness does NOT
collapse to the `(3,1)` signature plus carrier-identification; the
matter-attachment survives as a live pin unless a KS-to-physical-state-law
bridge or an elementary state-law theorem is supplied.

Three facts, all verified by the runner and non-circular (the faithful rep
and `Q = 2/3` are never assumed):

### A. The native `D` is single-component and spin-blind on `C^2`

The native first-order real anti-Hermitian operator
(`cpt_exact_real_anti_hermitian_d_narrow_theorem_note_2026-05-10`,
cited bounded authority; `H = iD`) is single-component scalar hopping on
`C^N` indexed by SITES, with NO per-site spinor index:

```text
D real antisymmetric  (H = iD Hermitian),
-D^2 = scalar lattice mass-shell {0, 1, 2, 3}    (normalized 1/2 hopping; no spinor structure),
[H (x) I_2, I (x) sigma_i/2] = 0                  (spin-blind on the C^2).
```

The older displayed `{0,4,8,12}` spectrum is the unscaled finite-difference
convention. The runner now checks both conventions explicitly and uses the
normalized convention in the statement above.

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
translating a spinor kinetic frame into the single-component phase field is
`Omega` -- the Kawamoto-Smit reconstruction
(`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07`; upstream
`staggered_dirac_grassmann_forcing_theorem_note_2026-05-07`). Those supplier
rows carry their own bounded surfaces and audit-owned status; this note only
uses them as the named bridge surface and does not broaden them. KS Step 4
runs in the OPPOSITE direction: the per-site
dim-2 carries a SINGLE Grassmann occupation mode, NOT a two-component
matter spinor (spin diagonalized into local phases; the Dirac index rebuilt
from the `(Z_2)^3` corner/taste cube).

The matching dynamical fact: under a spatial lattice rotation the native `D`
is restored to invariance by a purely single-component diagonal sign field
`W in {+1, -1}` (no `C^2` index) -- a `C^2` spin rotation `U(R)` is NOT
required. The `C^2`-spin reading of that compensator is available only
through `Omega`. So the dynamics route to matter-spin-1/2 is not KS-free.

## What is landable, and what is not

**Landable (this note):** the matter-attachment is not obtained from native
`D` plus the operator-frame merger alone. The positive bridge surface isolated
here is Kawamoto-Smit reconstruction, with an explicit admitted-not-forced
elementary fallback and with the physical matter-state law still requiring its
own bridge statement.

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

Two disjoint discharge routes, neither of which closes the current surface
without a further state-law bridge:

- **(B, the bounded bridge route)** reconstruct the matter-spinor index from
  the staggered corner/taste structure of the spin-blind single-component
  native `D` = `staggered_dirac_kawamoto_smit_forcing`, together with the
  upstream `staggered_dirac_grassmann_forcing` surface. This route is reusable
  only at the suppliers' own bounded scopes and still needs a physical
  matter-state spinor-law bridge before it can force the attachment on the
  current surface.
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

Separate supplier rows, not promoted by this note:
`staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07` and
`staggered_dirac_grassmann_forcing_theorem_note_2026-05-07`.

## Non-circularity

The forward checks are tier verification, prose verification, and direct
computation, none of which uses the faithful representation or `Q = 2/3`.
The KS-bridge identity and the spin-blindness of `D` are basis-independent
matrix facts. The reduction is stated as a localization, not a forcing.

## Next paths this opens

- Supply a direct KS-to-physical-matter-state spinor-law bridge. The current
  KS/Grassmann suppliers make Route B a bounded bridge surface, but they do
  not by themselves identify the physical matter-state law required by the
  attachment.
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

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [staggered_dirac_kawamoto_smit_forcing_theorem_note_2026-05-07](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
- [staggered_dirac_grassmann_forcing_theorem_note_2026-05-07](STAGGERED_DIRAC_GRASSMANN_FORCING_THEOREM_NOTE_2026-05-07.md)
