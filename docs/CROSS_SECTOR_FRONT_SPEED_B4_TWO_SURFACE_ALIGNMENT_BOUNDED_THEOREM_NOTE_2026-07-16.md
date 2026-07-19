# Cross-Sector Orbit-Averaged Euclidean Marginal-Coefficient Alignment Under B4 (Two-Surface Bounded Theorem)

> **Key terms used in this doc** are indexed A–Z at `docs/KEY_TERMINOLOGY.md`;
> each row points to the canonical source-of-truth doc.

**Date:** 2026-07-16
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Premise weight:** conditional (two named supplied legs, declared below)
**Status authority:** independent audit lane. This source note does not set or
predict an audit outcome. Any `audit_status` and `effective_status` fields are
pipeline-derived.

**Primary runner:**
[`scripts/cross_sector_front_speed_b4_two_surface_alignment_2026_07_16.py`](../scripts/cross_sector_front_speed_b4_two_surface_alignment_2026_07_16.py)
**Cached runner output:**
[`logs/runner-cache/cross_sector_front_speed_b4_two_surface_alignment_2026_07_16.txt`](../logs/runner-cache/cross_sector_front_speed_b4_two_surface_alignment_2026_07_16.txt)

## What this is

This note does **not** amend, narrow, retire, or re-approve any registered
primitive (the kinetic-isotropy primitive
[`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
is unchanged), does not set the status of any lane row, and does not edit any
landed note. Conditional on two named supplied legs, it proves a **two-surface**
statement about the cross-sector quotient `R = r_F/r_G` of **Euclidean marginal
coefficient ratios**, where `r_alpha = sqrt(c_salpha/c_talpha)`. It does not
identify `r_alpha` with a Lorentzian pole, group, signal, or wavefront velocity:

- **On the `Z^4` `B4`-covariant regulated surface** (the surface the landed
  `ALLORDERS_B4` note supplies in its premise (A)): `B4` invariance pins **each
  sector's** diagonal marginal kinetic form isotropic, `c_t = c_s` per sector,
  order-by-order in the loop expansion. The kinetic normalizations `Z_F`, `Z_G`
  cancel exactly in the quotient, so `R = 1` identically, order-by-order.
  Per-sector `B4` pinning in one common **Euclidean** coordinate frame is
  sufficient; no inter-sector Ward identity is involved. Off-surface the
  time-fixing symmetry alone does not force equality of these marginal ratios
  (a symmetry-counting statement only; see below).
- **On the time-fixed surface** (`Z^3` plus continuous tick — the continuous-time
  horn where `B4` is broken): the same exact counting leaves each sector's
  `c_t/c_s` an independent singlet of the time-fixing subgroup, and
  `R = sqrt(a_F/a_G)` is not forced to `1` by symmetry — it is set by
  the two independent per-sector anisotropies through their quotient alone.
  This is **symmetry counting only**: whether dynamics fixes the quotient is a
  separate question, and the landed velocity-RG mutual-drag flow
  (`dv_F/dl = a (v_b − v_F)`, `dv_b/dl = b (v_F − v_b)`, `eta -> 1` for any
  `a, b > 0`) is a live dynamical route toward equality on this surface — not
  contradicted here. The two landed velocity-RG parentheticals are scoped (not
  contradicted, not edited) as broken-`B4`-surface symmetry statements.

Companion to the landed
[`VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md`](VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md),
[`VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`](VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md),
[`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md), and
[`TASTE_SECTOR_MARGINAL_LV_B4_PROTECTION_ON_OS0_BOUNDED_THEOREM_NOTE_2026-06-13.md`](TASTE_SECTOR_MARGINAL_LV_B4_PROTECTION_ON_OS0_BOUNDED_THEOREM_NOTE_2026-06-13.md).

## Supplied-context declaration (two theorem legs)

> **Declared supplied context — leg 1: the `ALLORDERS_B4` premise (A) surface.**
> The regulated `Z^4` action and measure used here (gauged staggered/Kähler-Dirac
> fermions with cos vertices and the seagull, on the Wilson gluon block) are
> taken exactly `B4`-invariant, as
> [`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md)
> supplies in its premise (A) (line 58): "**(A) The supplied regulated action and
> measure are exactly `B4`-invariant.**" That note weighs this premise plainly
> (lines 77–79): "This is the **load-bearing supplied premise**. Runner Part A
> checks the finite action/measure invariance claims used here, but the theorem
> does not derive the choice of regulator action from the repo axioms." The same
> weight applies here: the `B4`-invariant surface is supplied, not derived from
> the four axioms; it is not derived here, and every claim below is conditional
> on it.

> **Declared supplied context — leg 2: `uniform_hw2_orbit_average_context`.**
> The fermion-side mathematical object is defined to be the **uniform
> taste-orbit average** of the marginal curvatures: the mean of the dispersion
> curvatures of the honest observable (`G_hon = Dinv - Sigma`, per the landed
> taste note) over the six-element Hamming-weight-2 taste orbit `hw2`.
> This is a supplied averaging convention, not a claim that the orbit average
> is a physical observable. On a **single-taste** object the alignment theorem
> does **not** follow from this note: the per-taste marginal anisotropy is nonzero
> and kernel-dependent (runner V3). Every fermion-side claim below is conditional
> on this explicitly uniform average.

These are the note's two supplied theorem legs; beyond them, this note introduces
no import, axiom, or comparator of its own.

## Physical application walls (outside the theorem)

Everything computed here is a Euclidean marginal coefficient or an exact
representation-theory statement. A physical velocity comparison would require,
at minimum, two additional independent ingredients that are **not** supplied or
consumed here:

- one shared two-sector continuation/reconstruction with compatible pole sheets,
  one clock normalization, and one Lorentzian comparison frame; and
- a license selecting the relevant regulated surface and the physical fermion
  readout.

No pole, spectral function, continuation, OS/Wightman reconstruction, causal
characteristic, or wavefront limit is computed. In particular, a low-momentum
pole/group velocity would not by itself be a wavefront velocity. Current
`main`'s
`FREE_STAGGERED_POLE_RESIDUE_DIRAC_CARRIER_CAR_RELABELING_BOUNDED_THEOREM_NOTE_2026-07-17.md`
partially advances the free mathematical pole/carrier route but explicitly does
not supply the interacting/gauged two-sector OS/Wightman bridge used by such a
physical claim. The present theorem therefore remains Euclidean and bounded.

## Theorem (two-surface, conditional on the declared legs)

Per sector, the Euclidean marginal kinetic form is
`c_t p_t^2 + c_s (p_x^2+p_y^2+p_z^2)` with the dimensionless marginal
coefficient ratio `r = sqrt(c_s/c_t)`; the cross-sector quotient is

```text
R = r_F/r_G = sqrt( (c_sF/c_tF) / (c_sG/c_tG) )
  = sqrt( c_sF c_tG / (c_tF c_sG) ).
```

### L1. Exact invariant counting (runner V5, exact sympy rationals)

`B4` (the signed-permutation group of the four Euclidean axes,
`|B4| = 2^4 * 4! = 384`) acts on the diagonal marginal coefficient vector
`(c_0, c_1, c_2, c_3)` through its `S4` quotient (the signs act trivially on
`p_mu^2`). The Reynolds (group-average) projector has **rank 1** with image
proportional to `(1,1,1,1)`: a `B4`-invariant diagonal marginal kinetic form has
`c_t = c_s`, per sector, with one per-sector normalization `Z` as the surviving
invariant. The time-fixing subgroup (spatial `O_h`, i.e. `S3` on the spatial
axes with the temporal axis distinguished) has Reynolds **rank 2**: `c_t` and
`c_s` are independent singlets per sector — the image `(1,0,0,0)` survives. This
reproduces, per sector, the landed counting (`ALLORDERS_B4`, lines 81–85):

> **(B) `B4` leaves exactly one diagonal marginal kinetic coefficient.** The
> diagonal quadratic form `c_t p_t^2 + c_s (p_x^2 + p_y^2 + p_z^2)` has a
> one-dimensional `B4`-invariant subspace, so `c_t = c_s` is forced; the spatial
> cubic group `O_h` plus a free temporal coefficient leaves two.
> (Reynolds-operator rank; runner Part B.)

**Joint (taste, axis) representation lemma (runner V5).** The 4-vector
counting above is not, by itself, the fermion-side statement: the fermion
object is the **24-dimensional** coefficient array `c_{B,mu}` over the six
`hw2` tastes `B` and the four axes `mu`. Under the joint `S4` action
(`B -> B o p`, `mu -> p^{-1}(mu)`; the membership relation `mu in B` is
preserved) the invariant subspace has **rank 2**, spanned by the orbit
indicators `{mu in B}` and `{mu not in B}` — a per-taste anisotropy is
therefore symmetry-**allowed**, and V3 observes it (`O(0.2)`,
kernel-dependent). Uniform averaging over the six `hw2` tastes composed with
the `S4` Reynolds projector has **rank 1 with isotropic image**, because each
axis lies in exactly 3 of the 6 `hw2` tastes (runner-verified): the V3
orbit-sum zero is exactly this representation-forced projection, and it
consumes leg 2 (uniform orbit averaging) essentially — a non-uniform taste
weighting would not project to the isotropic line. Under the joint time-fixing
`S3` the invariant rank is **6** (six (taste-type, axis-role) orbits), and
uniform `hw2` averaging maps it to rank **2** (`c_t`, `c_s` independent):
time-fixing symmetry alone does not force `c_t = c_s`.

### L2. Symmetry transport to both 1PI channels of one action (leg 1 + `ALLORDERS_B4` (C))

On the leg-1 surface, the landed transport step (`ALLORDERS_B4`, lines 87–89)
applies:

> A symmetry of the regulated action **and** measure
> is a symmetry of the generating functional `Z[J]`, hence of the perturbative
> effective action `Gamma[phi]` order-by-order in the loop expansion.

Because both sectors' 1PI objects — the fermion self-energy and the gauge vacuum
polarization — are channels of the **same** `Gamma[phi]` of the **same** supplied
leg-1 action, L1 pins **each** sector's marginal kinetic form isotropic
order-by-order at once. On the fermion side the pinned object is the leg-2
orbit-averaged marginal form, and the joint representation lemma (L1) is the
transport: joint `B4` covariance of `c_{B,mu}` plus uniform `hw2` averaging
forces the averaged vector isotropic. No inter-sector identity is used: the
pinning is per-sector, by the shared rigid frame.

### L3. Marginal-ratio arithmetic (runner V6, exact sympy + numeric gates)

Per sector the marginal form carries a constant (momentum-independent) kinetic
normalization `Z_alpha` — the value at the marginal order; a momentum-dependent
normalization contributes beyond marginal order and does not enter `r_alpha`,
and a direction-dependent normalization at marginal order is precisely the
anisotropy `B4` forbids (L1). `Z_F` and `Z_G` cancel exactly in `R` (symbolic).
On the `B4`-pinned surface (`c_t = c_s` per sector) the quotient is
`1` **identically** — no tuning, no flow. On the time-fixed surface, with
`a_F = c_sF/c_tF` and `a_G = c_sG/c_tG`, the ratio `sqrt(a_F/a_G)` is not
fixed by the symmetry: it depends only on the quotient of the two independent
per-sector anisotropies (scale-invariant in `(a_F, a_G)`), and symmetry
counting alone admits any positive value. This is a statement about what
symmetry **forces**, not about what dynamics **selects**: the landed
velocity-RG mutual-drag flow drives `eta = v_F/v_b -> 1` for any `a, b > 0`
on this surface, and nothing here constrains or contradicts that route.

### L4. Computed one-loop instances (runner V2, V3, V6)

The two computed channels are representative `B4`-covariant one-loop instances
sharing the Wilson gluon block and the gauged cos-vertex/seagull rules; they
are **not** assembled at a single common parameter point. `Pi` uses the landed
seagull kernel with a massless fermion loop; `Sigma` is one-gluon exchange at
the IR-safe mass `M = 0.21`, with the fermion-line tadpole evaluated
separately in V4 (direction-blind on-surface, hence an isotropic marginal
renormalization there). Each channel's own `B4` covariance is what the theorem
consumes; the instances are witnesses, not the proof.

- **Gauge sector** (seagull-completed transverse `Pi`, `T_F = 1/2`): at the
  lattice-compatible external momenta with components in `{0, 2*pi/N}`, the
  normalized Ward residual `|khat.Pi|/(|khat||Pi|)` is below `1e-9` at `N=12`,
  while the bubble (no seagull) has residual above `0.5`; the **fully gauged
  anisotropic control** — `v_mu` in the propagators, the vertices, **and** the
  seagull (gauging `sum_mu v_mu sin(k_mu + A_mu)`) — also satisfies the exact
  grid-compatible Ward gate below `1e-9` at `eps = 0.10`.
  `piT(temporal) = piT(spatial)` holds within `1e-8` at isotropic input, and
  `eta = 1` is a fixed point (induced anisotropy within `1e-8` at zero
  deformation). No off-grid convergence claim is made.
- **Fermion sector** (orbit-summed observable, leg 2): three kernels — rainbow
  scalar-gluon; gauged cos-vertex on the Wilson block, Feynman `xi=1`; gauged
  cos-vertex, Landau `xi=0` — all give `hw2` orbit-summed marginal anisotropy
  within `1e-6` on-surface, at `N=12` and `N=10`, on the honest observable
  `G_hon` (the observable reads the taste shift: non-degeneracy gate `> 1e-4`;
  no `W_B`-conjugation define-away).
- **Numeric quotient gates:** `|r_F^2 - 1| < 1e-6`, `|r_G^2 - 1| < 1e-8`, and
  `|R - 1| = |sqrt(r_F^2/r_G^2) - 1| < 1e-6` from the computed
  curvatures and `piT` — primary gate on the gauged cos-vertex curvatures, with
  the rainbow curvatures as a labeled robustness gate.

### Scoped result

On the `Z^4` surface, conditional on the two declared legs, `R = 1`
order-by-order. In the tightest wording: **conditional on exact joint covariance
and uniform `hw2` averaging, the orbit-averaged Euclidean marginal coefficient
vector is isotropic; time-fixing symmetry alone does not force equality of the
two sectors' marginal ratios.** On the time-fixed surface the `B4`
diagonal-marginal/orbit-average pinning is absent, and `R` is the quotient of the
two per-sector anisotropies as far as symmetry counting is concerned. The
landed velocity-RG mutual-drag flow remains a live dynamical route toward
equality there (scoped below). No physical-velocity conclusion follows.

## Per-sector Euclidean pinning, not an inter-sector identity (runner V4)

The runner's off-surface controls (V4) are **symmetry-tracking witnesses**
(each sector's isotropy responds to its own kernel's
covariance) — they are not a dynamical-unconstraint claim:

- Deforming the temporal edge of the Wilson gluon block
  (`(2/xi) sin(xi q_0/2)`) revives the fermion orbit-summed anisotropy:
  `+0.0009` at `xi=0.7`, `-0.0013` at `xi=1.3` (a sign straddle across
  `xi=1`; two samples — no isolated-zero claim), and `-0.0003` at `xi=1.3`
  for the gauged-vertex kernel.
- Deforming the fermion velocity moves `Pi`: induced gauge-sector anisotropy
  `+0.0603` at `eps = 0.10` (fully gauged control: `v_mu` in the propagators,
  the vertices, and the seagull; transversality preserved under the
  deformation, V2).
- The tadpole direction test (`T_mu` = BZ-grid mean of the Landau-form tadpole
  integrand on the Wilson block — a declared normalization, used purely as a
  direction-sensitivity witness) is direction-blind on-surface (relative spread
  `< 1e-10`) and direction-sensitive off-surface (relative `|T_t - T_s| =
  0.0630` at `xi=1.3`).

Each sector's isotropy tracks its **own** kernel's `B4` covariance; nothing is
transferred between sectors. Additionally, the **unprotected** per-taste value
is kernel-dependent at matched `N=10`: rainbow `-0.1808`, gauged Feynman
`+0.2471`, gauged Landau `-0.0624` (minimum pairwise separation `0.1184`; the
signs differ). The orbit-summed zero is symmetry-driven, not kernel tuning.

## What is new relative to the landed notes

1. **Both 1PI channels from one kernel family.** The landed seagull note
   computed `Pi` from gauged staggered fermions; the landed taste note computed
   the fermion self-energy with a scalar-gluon rainbow kernel. Here the fermion
   self-energy uses the **same** gauged cos vertices and the **same** Wilson
   gluon block that the `Pi` computation gauges (V2 + V3); the two channels are
   not assembled at a single common parameter point (see L4). `ALLORDERS_B4`'s
   computed confirmations were fermion-side; its gauge-channel instance and the
   cross-sector ratio corollary were not stated there.
2. **Off-surface deformation-response witnesses** (V4): symmetry-tracking
   controls that distinguish per-sector Euclidean covariance from an
   inter-sector identity (each sector's isotropy tracks its own kernel's
   covariance; no dynamical-unconstraint claim).
3. **Exact Reynolds counting applied to the cross-sector quotient** (V5 + V6):
   rank 1 per sector pins `R = 1`; rank 2 per sector leaves it unpinned — the
   two-surface split as a theorem about the **coefficient quotient**, not just per-sector
   coefficients.
4. **Marginal-ratio arithmetic with exact `Z` cancellation** and the numeric
   `R - 1` gate (V6).
5. **Gauge robustness of the orbit-summed protection** (V3): the orbit-summed
   anisotropy is zero in **both** Feynman (`xi=1`) and Landau (`xi=0`) gauge.
   The seagull note's named open item (lines 86–90) is that "The **precise
   net** coefficient needs a **gauge-invariant fermion-velocity prescription**:
   the bare self-energy `Z` is gauge-dependent (Feynman vs Landau differ)". At
   the ratio/orbit-sum level of this note that concern does not bite — `Z`
   cancels exactly, and the protected zero is gauge-robust because both gauge
   fixings preserve the kernel's `B4` covariance, which is what the protection
   tracks. The magnitude prescription for the unprotected per-taste value stays
   open.
6. **Kernel-dependence of the unprotected per-taste value** (V3): three
   kernels, three distinct values, signs differ — a structural witness that the
   orbit-sum zero is symmetry, not tuning.

## Scoping the two landed parentheticals (derived; no landed text is edited)

The landed lane carries the same assertion in two places.
[`VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md`](VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md),
lines 30–35:

> Cross-sector front-speed alignment `v_fermion = v_gauge` is the last open
> residual of emergent Lorentz invariance: the `B4` custodial symmetry does **not**
> cover it (the relative speed `v_F/v_b` is a free `B4` invariant), and the only
> handle is the velocity-RG mutual-drag flow
> `dv_F/dl = a (v_b − v_F)`, `dv_b/dl = b (v_F − v_b)`, which gives `eta=v_F/v_b → 1`
> for any `a,b > 0`.

[`VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`](VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md),
lines 20–22:

> Cross-sector front-speed alignment `v_fermion = v_gauge` is the last open residual
> of emergent Lorentz invariance: `B4` does not cover it (the relative speed is a
> free `B4` invariant), and the only handle is the velocity-RG mutual-drag flow.

**Derived scope.** This note verifies only the Euclidean marginal-coefficient
content underlying those physical parentheticals. On the time-fixed surface the
acting symmetry is the time-fixing subgroup, its Reynolds rank is 2 per sector
(joint rank 2 after averaging, V5), each sector's `c_t/c_s` is an independent
singlet, and `R = sqrt(a_F/a_G)` is not fixed by the symmetry (V6). What is proved
is that **time-fixing symmetry does not force equality of the marginal
ratios** — not that dynamics leaves them free and not that they are physical
velocities. The parentheticals' own mutual-drag flow is a live dynamical
mechanism on that surface. This is the continuous-time horn where the landed
`ALLORDERS_B4` note (lines 178–184) already records:

> It does
> **not** address: non-perturbative effects; the `a -> 0` continuum limit; genuine
> taste-**breaking** or per-single-taste effects;
> or the continuous-time obstruction horn, where `B4` is **broken** (the temporal
> integral is uncut while the spatial Brillouin zone is cut), and the protection
> genuinely fails. It **consumes**, and does not derive, the
> `kinetic_isotropy_primitive` (`c_t = c_s`, OS0).

On the `Z^4` `B4`-covariant surface (leg 1) the same counting gives rank 1 per
sector and the **Euclidean marginal quotient** is pinned: `R = 1`
order-by-order (L2 + L3). This does not prove the quoted physical front-speed
claim because the reconstruction and surface-license walls remain open. Both
landed notes stand as written; this note narrows the exact Euclidean content and
edits neither.

The logflow note also states the demand (lines 116–117):

> Closing it needs a cross-sector custodial symmetry or an
> `O(1)` anomalous dimension the framework does not currently supply.

On the leg-1 surface, per-sector `B4` pinning supplies an exact Euclidean
coefficient-alignment corollary in a common Euclidean frame rather than an
inter-sector Ward identity (V4). It does **not** supply the requested physical
custodial mechanism. Closing that physical question still requires the common
two-sector reconstruction/clock/frame and a surface/readout license named in
the physical-application boundary above. The velocity-RG route is neither
retired nor replaced by this theorem.

## Honest boundary (auditor-first)

- **Both theorem legs are supplied, not derived.** Leg 1 carries the same weight
  the `ALLORDERS_B4` note assigns its premise (A) (quoted above). Leg 2 is a
  uniform mathematical averaging convention with no physical readout license.
  The runner computes finite-grid Euclidean marginal coefficients only. The
  landed taste note states the physical-interpretation dichotomy (lines
  229–235):

  > The **per-single-taste `O(0.2)` anisotropy is the genuine
  > residual**: whether it constitutes a physical Lorentz violation depends on the
  > physical interpretation of the taste label (if a single taste corner is a
  > physically distinguishable particle, the marginal anisotropy is physical; if only
  > taste-summed observables are physical, it cancels). This note does not settle that
  > interpretation; it reports the taste-sum protection and the per-taste residual
  > honestly.

  The single-taste object therefore remains open, and the alignment theorem
  does **not** apply to it.
- **Record supplies no readout selector at the minimal-axiom level.** The direct
  framework authority
  [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
  places observable identification and readout context downstream of the four
  axioms (notably its scope statements around lines 76–79 and 128–133).
  Accordingly, nothing in the record ontology is invoked here to justify
  orbit-summing; leg 2 is an explicit mathematical convention. This is not a
  no-go against a downstream dynamical or operational selector.
- **The time-fixed horn is symmetry-unprotected — a counting statement only.**
  What is proved on that surface is that time-fixing symmetry alone does not
  force `c_t = c_s` (joint averaged rank 2, V5); the ratio is then set by the
  quotient of the two per-sector anisotropies **as far as symmetry is
  concerned**. Whether dynamics selects equality there is untouched: the
  landed velocity-RG mutual-drag flow (`eta -> 1` for any `a, b > 0`) is the
  live route, and nothing here constrains it.
- **Physical reconstruction and surface license remain open.** Neither theorem
  leg supplies a common two-sector Lorentzian reconstruction/clock/frame or
  selects which surface and readout are physical. The current-main free-pole
  carrier note named above is a partial mathematical closure only; it explicitly
  leaves OS/Wightman and interacting/gauged closure open. The present theorem is
  a conditional Euclidean alignment on the `Z^4` surface plus an exact
  symmetry-nonforcing statement on the time-fixed surface.
- **Order and proxy level.** The gauge-sector computations are one-loop
  (seagull-completed `Pi`); the all-orders reach is the symmetry transport of
  `ALLORDERS_B4` (C) applied on leg 1, not a diagram-by-diagram computation.
  Magnitudes are structural/proxy-level; the logflow note's residual-D
  naturalness content (its `lambda`, `gamma`, and LV-bound sufficiency) is
  untouched. The seagull note's gauge-invariant fermion-velocity prescription
  stays open for magnitudes; this note bypasses it strictly at the
  ratio/orbit-sum level.
- **Representative channels, one kernel family.** The two computed one-loop
  channels share the Wilson gluon block and the gauged cos-vertex/seagull
  rules but are not evaluated at a single common parameter point (`Pi`:
  massless fermion loop, per the landed seagull kernel; `Sigma`: one-gluon
  exchange at `M = 0.21`); the fermion-line tadpole enters only as the V4
  direction-sensitivity witness. The theorem consumes each channel's own `B4`
  covariance, not a joint evaluation.
- **Declared tadpole normalization.** `T_mu` is the BZ-grid mean of the
  Landau-form tadpole integrand on the Wilson block, used as a
  direction-sensitivity witness, not as a physical renormalization.
- **No statuses, no primitive changes, no edits.** The kinetic-isotropy
  primitive is unchanged (consumed through the leg-1 surface's isotropic bare
  kinetic form, per `ALLORDERS_B4`); no landed note is edited; grading belongs
  to the independent audit lane.

## Load-bearing dependencies (cited at declared ledger grade)

| Source | Ledger `effective_status` | Role here |
|---|---|---|
| [`ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md`](ALLORDERS_B4_MARGINAL_PROTECTION_SYMMETRY_THEOREM_NOTE_2026-06-14.md) | unaudited | leg 1 (premise (A) surface); (B) counting; (C) all-orders transport |
| [`TASTE_SECTOR_MARGINAL_LV_B4_PROTECTION_ON_OS0_BOUNDED_THEOREM_NOTE_2026-06-13.md`](TASTE_SECTOR_MARGINAL_LV_B4_PROTECTION_ON_OS0_BOUNDED_THEOREM_NOTE_2026-06-13.md) | unaudited | honest observable `G_hon = Dinv - Sigma`, `hw2` orbit, rainbow kernel; per-taste dichotomy quoted |
| [`VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md`](VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md) | unaudited | scoped parenthetical (lines 30–35); custodial-demand sentence (lines 116–117) |
| [`VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`](VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md) | unaudited | seagull-completed `Pi` kernel (`T_F = 1/2`); scoped parenthetical (lines 20–22); gauge-prescription open item |
| [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) | meta (framework authority) | direct authority that observable/readout identification is downstream of the four axioms; why leg 2 is declared rather than derived |
| [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) | meta (registered primitive) | unchanged; consumed (not derived) through the leg-1 surface, per `ALLORDERS_B4` |

Graded rows in this lane — `taste_scalar_isotropy_theorem_note` (retained;
scope: the CW Hessian statement), `lorentz_violation_derived_note`
(unaudited), `dispersion_high_p_tiebreaker_note` (retained_bounded) —
are not load-bearing for this note and are not stretched beyond their declared
scopes.

## Runner verification map

| Part | Checks | What it certifies |
|---|---|---|
| V1 | 4 | Clifford algebra for both landed gamma conventions; `W_B` conjugation identity for all 16 taste shifts; gauged cos-vertex taste covariance |
| V2 | 5 | exact grid-compatible seagull-completed `Pi` Ward identity (normalized residual `< 1e-9` at `N=12`) vs large bubble (no seagull) violation; exact deformed-kernel Ward identity (`v_mu` in propagators, vertices, seagull; `eps = 0.10`); `B4` isotropy `piT(t) = piT(s)`; `eta = 1` fixed point; no off-grid convergence claim |
| V3 | 11 | honest-observable (`G_hon`) non-degeneracy (both kernels); per-taste anisotropy nonzero with kernel-dependent values and signs (three kernels, matched `N=10`); `hw2` orbit-summed anisotropy zero on-surface at `N=12` and `N=10`, Feynman and Landau |
| V4 | 7 | off-surface deformation-response witnesses: orbit anisotropy revives with a sign straddle across `xi=1` (two samples); `Pi` feels the fermion deformation; the gluon-edge deformation moves the fermion orbit sum; tadpole direction-blind on-surface, direction-sensitive off-surface |
| V5 | 9 | exact sympy Reynolds counting: `B4` (`S4` quotient) rank 1 with isotropic image; time-fixing subgroup rank 2 with `(1,0,0,0)` surviving; joint 24-dim `(hw2 taste, axis)` lemma — joint `S4` rank 2 (orbit indicators), each axis in exactly 3 of 6 tastes, uniform averaging composed with Reynolds rank 1 isotropic, joint time-fixing `S3` rank 6 mapping to averaged rank 2 |
| V6 | 5 | exact `Z_F`, `Z_G` cancellation; pinned-surface quotient `R = 1` identically; broken-surface quotient `sqrt(a_F/a_G)` depending only on the anisotropy quotient (scale-invariance gated); numeric `R - 1` gates — gauged cos-vertex primary, rainbow robustness |

Runner gates are tolerance bounds around structure (zero/nonzero/sign/rank);
gated prints are bound checks at pass tolerances (platform-stable output).

## Reproduce

```
python3 scripts/cross_sector_front_speed_b4_two_surface_alignment_2026_07_16.py
# expect: TOTAL: PASS=41 FAIL=0   (N=12 primary / N=10 secondary grids, ~7 s, low memory)
```
