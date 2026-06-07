# The Staggered Single-Clock Axis IDENTITY (S3) is Convention-Dependent; the Records-Arrow Sources the Unique Clock Axis — Narrow No-Go + Relocation

**Date:** 2026-06-06
**Claim type:** no_go (the staggered-η axis-identity is convention) + relocation (the records-arrow sources the axis)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/single_clock_axis_identity_convention_records_arrow_runner.py`](../scripts/single_clock_axis_identity_convention_records_arrow_runner.py)
**Cached output:** [`logs/runner-cache/single_clock_axis_identity_convention_records_arrow_runner.txt`](../logs/runner-cache/single_clock_axis_identity_convention_records_arrow_runner.txt)

## Audit context

The (unaudited) single-clock theorem's **S3** claims the temporal direction is the **unique**
lattice direction admitting reflection positivity (RP) on the staggered-Dirac action — i.e. "no
second clock," via the staggered phases + Sharatchandra fermion-reflection convention. This note
shows, via three machine-clean computations, that **S3's axis IDENTITY is convention-dependent**:
the staggered phases carry no axis-distinguishing invariant and the temporal axis is movable by a
site-local Z₂ field redefinition (gauge). It sharpens the matching retained no-go
[`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
(`retained_no_go`: Stone uniqueness is transfer- and τ-relative; "no second clock" needs a
*separate* axis/transfer-uniqueness premise) and **relocates** the genuine source onto the
records-arrow
[`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)
(`retained_bounded`).

## Safe statement

KS phases `η_μ(x) = (−1)^{x_0 + … + x_{μ−1}}`.

**Theorem.**

1. **No axis-distinguishing RP invariant.** The Sharatchandra–Thun–Weisz crossing-link
   `P_a(x) = η_a(x)·η_a(θ_a x)` (with `θ_a : x_a ↦ −1−x_a`) is `+1` **uniformly for all `d` axes**,
   because `η_a` omits the coordinate `x_a` so `θ_a` leaves it fixed and `P_a = η_a² = +1`. The
   action-level RP datum singles out **no** axis.

2. **Isotropic curvature.** The η-curvature 2-cocycle
   `Φ_{μν} = η_μ(x)η_ν(x+μ̂)η_μ(x+ν̂)η_ν(x) = −1` in **all** `C(d,2)` planes including the three
   **temporal** planes `(0,i)`. The class is `S_d`-isotropic — no plane/direction is the time.

3. **The temporal axis is gauge-movable.** The time↔space staircase relabel is an **exact
   site-local Z₂ field redefinition**: `s(x) = (−1)^{x_0 x_1}` gives `diag(s)·D·diag(s) = D_swap`
   exactly (max diff `0.0`), spectrum-preserving (hence taste-preserving). So "which axis is the
   clock" is a convention.

4. **The convention-independent residue is the COUNT (=1), not the identity.** The free staggered
   `D†D = m² + Σ_μ sin² p_μ` is identical under axis relabeling (the spectrum picks no clock); in
   *every* axis-frame exactly one positive-Hermitian transfer exists. So "a unique clock **exists**"
   is real; "it is physical direction X" is **not** delivered by S3.

5. **The records-arrow sources the unique AXIS, convention-independently.** Each spatial reflection
   `x_i ↦ −x_i` is an involution preserving the pairwise-distance multiset (the spatial `Z³` is a
   reversible group); a record count is strictly monotone (an append-only, non-invertible monoid).
   Only the record-accumulation direction is monotone — a direction the three reversible spatial
   axes **cannot carry** — so it is the unique clock axis, with **no** staggered-η and no 4th
   lattice axis.

## No-go discipline (N1–N8)

- **N1 (alternative routes).** Every gauge-invariant axis-distinguisher was checked and **none**
  singles out time: crossing-link (1), curvature class (2), `D†D` spectrum (4), and the gauge
  relabel (3). The single-step RP Gram is non-PSD in *every* direction (retained
  `rp_two_step_transfer_matrix_positivity`'s single-step failure), the 2-step transfer positive in
  *every* direction.
- **N2 (wall-independence).** The Z₂ relabel `χ → s(x)χ` leaves the gauge action `S_g[U]` inert, so
  the gauge-movability survives the **interacting** (fixed-`U` Wilson) level — not a free-only
  artifact.
- **N3 (hidden-wall scan).** The spin-statistics/CAR convention does **not** rescue S3: the
  antilinear reflection `Θ = K` commutes with the real Z₂ gauge (`K s K = s`), so the Grassmann
  reordering sign is axis-blind; the "−1" temporal sign in S3 eq.(7) is the hand-asserted CAR
  transposition sign (`η_0 ≡ 1` cannot flip), not a property of the η-cochain.
- **N4/N5 (residual matching, rhetoric).** The result is exactly the landed
  `single_clock_uniqueness_scope_boundary` (`retained_no_go`): Stone uniqueness is τ-relative; "no
  second clock" needs a separate premise — and S3 Step 4 *is* that premise, supplied by the
  gauge-removable η placement.
- **N6 (partial-closure).** The COUNT (=1 RP axis) survives convention-independently; the records-
  arrow supplies the AXIS. The no-go is on the *identity-via-η*, not on the existence of one clock.
- **N7 (steelman).** The taste-tied "physical" reading is refuted: the Z₂ sign gauge is
  **taste-preserving** (only the `Ω` spinor redefinition is taste-changing), so temporal-uniqueness
  is *separable* from the taste-4 reduction — convention.
- **N8 (cross-cycle echo).** Aligns with the retained `staggered_axis_symmetry_is_s3`
  (`retained_bounded`, the spatial-`S₃` Z₂-gauge precursor); the `S₄`/time↔space extension is the
  *additional* content of this runner (the `S₃`/`L³` row does not cover it).

## The genuine open piece (the path this opens)

The convention-independent statement *"from Z³ + Record a unique 4th time AXIS emerges"* is
**unbuilt**. The records-arrow delivers the axis but with two honest hedges: **(R1) conditional** —
the monotone needs a supplied (non-axiom) record-production dynamics, not an unconditional A_min
forcing; **(R2) parallel, not downstream** — S3's ledger deps contain no records note, so the
records-arrow is an *independent* source, not literally "S3 in disguise" (verified: an η-free
broadcast construction still gives a monotone). The orientation (`t ↦ −t`) is **not** records-
sourced (counts are word-reversal invariant — `post_record_arrow_orientation_firewall`,
`retained_no_go`); it is fixed only by the spectrum-condition `H ≥ 0` ⟺ low-record past hypothesis.
The open path: whether record-accumulation as a Lieb-Robinson/causal-cone monotone singles out the
unique evolution-generating direction (the framework's directional content lives there, since the
free+Wilson action is hypercubic-symmetric).

## Boundary (honest)

- A **no-go for S3's axis-identity-via-η** + a **relocation** to the records-arrow; it does **not**
  deny that one clock exists (the COUNT survives).
- S3 and the RP-umbrella it leans on are both `unaudited`, so nothing load-bearing rests on them;
  this verdict rests on `retained` anchors + machine-clean finite-lattice arithmetic.
- The records-arrow source is `retained_bounded` but carries R1/R2 + the orientation firewall;
  "emergent unique time axis from Z³+Record" remains the open object.
- Emergent time respected — no time axiom; S3 is flagged for adjoining the 4th axis `Z/L_τ` it then
  "uniquely" confirms (circular).

## Forbidden imports check

No new axiom. KS-phase arithmetic, a finite free/Wilson staggered Dirac operator, and the Z₂
field-redefinition are exact and reproven here; the records-arrow is `retained_bounded`. The
"emergent unique time axis" is named open, not asserted.

## Runner check breakdown

Class A: (1) `P_a = +1` all axes; (2) curvature `−1` all planes incl. temporal; (3) exact Z₂ gauge
time↔space swap (max diff 0.0), spectrum/taste-preserving; (4) `D†D` direction-symmetric; (5) the
records-arrow's reversible-space-vs-monotone-records distinction. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

Three machine-clean facts establish that the staggered η phases carry no axis-distinguishing RP
invariant (crossing-link `+1` everywhere; isotropic curvature) and that the temporal axis is
movable by a spectrum- and taste-preserving site-local Z₂ field redefinition — so S3's "unique
temporal RP axis" is convention-dependent for the axis identity, and circular (it adjoins the
temporal coordinate it then confirms). The convention-independent residue is only the count
(=1 clock exists); the convention-independent source of the unique clock axis is the records-arrow
(reversible spatial Z³ cannot carry a monotone direction), which is `retained_bounded` but
conditional, parallel-not-downstream, and orientation-firewalled. The result sharpens the retained
no-go single-clock scope boundary; the "emergent unique time axis from Z³+Record" is the named open
object. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/single_clock_axis_identity_convention_records_arrow_runner.py
```
