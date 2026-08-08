# RG-invariance of the Koide modulus r, and two sharpenings

**Date:** 2026-06-05
**Type:** derivation / companion
**Claim type:** theorem
**Status:** no audit status set; the independent audit lane owns classification.
This is a narrow source-only companion (note + paired runner + cached log).
**Runner:** `scripts/koide_r_rg_invariance_2026_06_05.py`
(SUMMARY: PASS=27 FAIL=0).
**Cached log:** `logs/runner-cache/koide_r_rg_invariance_2026_06_05.txt`

## Context

The per-sector Koide modulus `r = |b|^2 / a^2` of the C3-circulant generation
mass operator `H = a I + b C + conj(b) C^2` is the open residual of the flavor
campaign. A prior "4-for-4 dynamics no-go" (variational / RG-scale /
self-consistency / and the static-functional family) left **one** candidate
un-killed: *a matter beta-function fixed-point FLOW could pick a generic value
of `r`.* This note closes that last candidate quantitatively and records two
reusable structural sharpenings. It anchors against the retained_no_go rows
`quark_c3_circulant_source_law_boundary` and
`koide_frobenius_isotype_split_uniqueness` (the singlet:doublet weight ratio is
free), reaching the same boundary from the renormalization-group side.

`r` is **degree-0 homogeneous** in the sqrt-mass amplitudes `(a, b)`: any
flavor-uniform rescaling `lambda -> f*lambda` leaves it exactly invariant.

## Result 1 — r is RG-invariant; the flow escape is closed

**The exact core.** In the SM 1-loop up-Yukawa RGE,
`16 pi^2 dY_u/dt = Y_u[(3/2)(Y_u^dag Y_u - Y_d^dag Y_d) + T - (17/20)g1^2 - (9/4)g2^2 - 8 g3^2]`,
every **flavor-uniform** term — the gauge terms (including the full `-8 g3^2`)
and the trace `T` — multiplies `Y_u` and so rescales all three sqrt-mass
amplitudes by a common factor. Being degree-0, `r` is **exactly invariant** under
all of them (runner: machine-precision under any uniform rescaling). Only the
**non-uniform** Yukawa terms can move `r`.

**The honest residual (numerical integration of the actual SM 1-loop RGE).**
Over ~33 e-folds from `M_Z` to the GUT/Planck scale:

| quantity | M_Z -> ~GUT | size |
|---|---|---|
| absolute top Yukawa `y_t` | 0.99 -> 0.46 | **~53%** (the quasi-fixed-point flow) |
| `r_up` (ratio) | 0.773 -> 0.786 | **1.6%** |
| `r_down` (ratio) | 0.597 -> 0.578 | **3.3%** |

`r_down` moves more than `r_up` because the down RGE carries the cross term
`-(3/2)Y_u^dag Y_u`, so the b-quark feels the **top** (with `|V_tb| ~ 1`) — a
genuinely non-uniform term. (A prior optimistic estimate of ~0.001% for `r_down`
omitted this cross term; the honest figure is a few percent.)

**The conclusion (closes the candidate).** The flow moves the **absolute** top
Yukawa by ~53% — that is the real quasi-fixed-point, which makes an *absolute*
coupling (the overall scale `a`, the top mass) UV-insensitive. But the same flow
moves the **ratio** `r` by only a few percent, because the uniform terms it
flows to **cancel in the ratio**. That residual is more than an order of
magnitude too small to carry `r` from a fixed point `{0, 1/2, 1}` to a generic
value (e.g. `1/2 -> 0.77` is a 54% gap). **A ratio quasi-fixed-point does not
exist; the IR-attractor mechanism that yields generic *absolute* values does not
yield a generic *ratio*.** The "flow picks a generic r" escape is closed.

## Result 2 — QCD RG-invariance of r, derived from color ⊥ generation

Because color and the generation `C3` orbit are **independent** Z3 structures
(color ⊥ generation; cf. `color_generation_independent_z3_structures_2026-06-05`,
unaudited), the QCD charge is the same on all three generations, so the QCD
anomalous dimension is **proportional to `I_3` in generation space**:
`gamma_singlet = gamma_doublet` under QCD running. Hence the `-8 g3^2` term is
flavor-uniform and `r` is **exactly** QCD-RG-invariant. This *derives* the
no-go's previously-asserted "gauge channel inert / uniform dressing leaves `r`
invariant" from the color ⊥ generation structure rather than positing it.

## Result 3 — overlap-integral category error (a no-go boundary)

The condensed-matter "crystal-field / hopping-overlap ratio fixes `r`" mechanism
**does not apply**. The three generations are the hw=1 Brillouin-zone corner
**momentum eigenstates** `{(1,0,0),(0,1,0),(0,0,1)}`, which are **orthonormal**:
`<k_i|k_j> = delta_ij` (runner: exact). The `C3` "hopping" `b` is a unitary
**permutation** of these orthogonal states — a Fourier-symmetry relabel, with
matrix entries in `{0,1}`, **not** a small spatial overlap integral. `r` is an
isotype-power ratio of the mass-generating operator with no spatial-overlap
content. This forecloses the whole class of "geometric/overlap ratio fixes `r`"
attempts.

## The next path this opens (not a closed enumeration)

These three results **narrow** where a generic-`r` mechanism could live, rather
than closing the search. The unifying lesson: **`r` is a degree-0 ratio, so no
flavor-uniform dynamics can fix it — every uniform term (gauge, trace, QCD, any
overall flow toward a quasi-fixed-point) cancels in the ratio.** A mechanism that
sets a generic `r` must therefore be intrinsically **non-uniform / relational**:
it must act on the singlet-vs-doublet isotype *balance* itself, not on any
overall scale or flavor-blind coupling. The live directions consistent with this
(a degree-0-ratio spectral/arithmetic invariant; a precision-stable cross-sector
source-law; or the reframing in which `r` is a recorded-outcome whose Born
*measure* over the dial is the object to derive) all share that property.

## Scope, targets, and discipline

- Four sector targets carried (labelled observational comparison, NOT derivation
  inputs): `r_lep = 1/2` (the one special/symmetric value), `r_up ~ 0.77`,
  `r_down ~ 0.597`, `r_nu ~ 0.238`.
- **Look-elsewhere / precision discipline honored.** No numerical coincidence is
  claimed as a mechanism here. `r_up` is **scheme-soft** at the ~2% level
  (`m_t` pole vs MSbar over [150, 173] GeV gives `r_up` in [0.760, 0.773]); the
  RG-invariance conclusion is robust to this since the flow residual (1.6%) and
  the scheme spread (~2%) are both far below the fixed-point-to-generic gap.
- No new axiom or import is adopted; the SM 1-loop RGE and PDG masses enter only
  as the comparison against which RG-invariance is demonstrated.
