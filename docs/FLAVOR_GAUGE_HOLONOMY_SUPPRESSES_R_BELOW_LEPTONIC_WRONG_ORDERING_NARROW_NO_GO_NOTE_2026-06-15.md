# Gauge-holonomy character cap on the Koide ratio: the algebraic bound r_R ≤ r₀ (narrow no-go, cap-only)

**Date:** 2026-06-15
**Type:** no_go
**Status:** source note awaiting independent audit handling.
**Status authority:** independent audit lane only. This source note does not set
status.

**Scope (narrowed 2026-06-20):** The source claim is the **conditional
algebraic character cap** `r_R ≤ r₀` for a supplied closed-holonomy tensor
dressing and normalized fibre trace. The inequality follows from
`|χ_R(U)| ≤ d_R`; the cited sources do not derive that dressing. The further
*physical* no-go statement — "a gauge holonomy suppresses the
**observed lepton/quark** Koide ratio below the leptonic value and so gives the wrong ordering for the
observed sector spread" — requires a bridge that (i) assigns the physical colourless-lepton sector to
the trivial gauge representation and the coloured-quark sectors to nontrivial representations, and
(ii) identifies the fibre-averaged ratio `r_R` with the registered physical Koide dial of each sector.
That bridge is **not supplied here**; the physical ordering reading is therefore **open**
and is presented below only as a consequence *if* the standard assignment and the readout
identification were established. The firewall holds throughout: no value of r is forced; r₀ is a free
bare coupling.
**Primary runner:** [`scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py`](../scripts/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py)
**Cached output:** [`logs/runner-cache/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.txt`](../logs/runner-cache/frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.txt)
**Kernel support:** [`FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md)
**Kernel runner/cache:** [`scripts/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py`](../scripts/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.py),
[`logs/runner-cache/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.txt`](../logs/runner-cache/flavor_gauge_holonomy_character_suppression_kernel_2026_06_18.txt)

## Claim

The sector dial `r = |b|²/a²` (Koide Q = 1/3 + 2r/3) sits at different values per fermion sector
(charged leptons r = 1/2, down-quarks r ≈ 0.597, up-quarks r ≈ 0.773). One proposed origin — the
"colour-dressed" channel left open by the unaudited
`flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (context only, no dep edge)
— is a supplied tensor construction in which a closed based holonomy dresses
the `b` coefficient while `a != 0` is left onsite and unchanged. The cited
Gamma-axis and covariant-hopping notes motivate this construction but do not
derive the bridge from the internal taste return to that spatial holonomy
([`matter_gauge_minimal_coupling_fiber_frame_forces_connection`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md),
[`fiber_frame_local_redundancy_bridge`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md)).

**The source content of this note is the conditional algebraic cap `r_R ≤ r₀`.** Dressing
the hop with a closed based holonomy `U` (or an endpoint-identified
transporter) in gauge representation `R` and forming the conjugation-invariant
fibre-traced effective generation operator yields

> b_eff = b · χ_R(U)/d_R,  a_eff = a,  hence **r_R = r₀ · |χ_R(U)/d_R|²**,

where χ_R(U) = Tr_R(U), d_R = dim R, and r₀ = |b|²/a² is the trivial-rep value. Because
|χ_R(U)| ≤ d_R for every unitary (a sum of d_R unit-modulus eigenvalues), the
normalized character satisfies |χ_R(U)/d_R| ≤ 1, so

> **r_R ≤ r₀ for every representation and every such holonomy, with equality
> iff `U_R` is a scalar phase on the chosen representation.**

For a nonfaithful representation this representation-level equality condition
does not imply that the underlying group element is central.

This is the bounded algebraic inequality the row carries conditional on the
supplied closed-holonomy dressing. It forces **no** value of `r`: `r₀` is a
free bare coupling. No framework-native hopping-holonomy construction is
claimed here.

**Conditional physical reading (open — unsupplied bridge).** *If* one adopts the standard
identification "colourless lepton ↔ trivial rep, coloured quark ↔ nontrivial rep" *and* identifies the
fibre-averaged ratio `r_R` with the registered physical Koide dial of each sector, *then* the cap reads
as: a gauge holonomy could only suppress the coloured Koide ratio *below* the leptonic value, whereas
the observed quarks sit *above* it (r_down ≈ 0.597 > 1/2, r_up ≈ 0.773 > 1/2), so the holonomy channel
would give the wrong ordering for the observed spread. **Both of those bridging steps are not
established here** (no theorem assigns the physical sectors to the gauge representations, and the
fibre-averaged-ratio → registered-dial identification is the open readout import). The physical
"wrong-ordering / falsified-as-spread-source" conclusion is therefore **conditional on that
unsupplied bridge** and is *not* part of the source algebraic content.

## 2026-06-18 finite kernel update

[`FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md`](FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md)
isolates the exact finite-algebra part of the argument. Conditional on a
supplied closed-holonomy tensor dressing and normalized fibre trace, it proves
that the generation-hop coefficient is multiplied by `chi_R(U)/d_R`, and that

```text
    d_R^2 - |chi_R(U)|^2 = sum_{i<j}|z_i-z_j|^2 >= 0
```

for the unit-modulus eigenvalues of the finite unitary link representation.
This replaces the prior appeal to a standard lattice-gauge character
suppression fact with an on-surface finite proof and runner/cache.

This update proves only the conditional character-suppression kernel. The
framework dressing and the physical
sector-to-representation/readout bridge remains open: it does not derive the
colourless-lepton/trivial-representation or coloured-quark/nontrivial-representation
assignment, and it does not turn the observed sector ordering into a
framework-native readout.

## The No-Go (Algebraic Cap Source Content)

**(N-bound) The character inequality caps r_R at r₀.** For any representation
`R` and any supplied closed based unitary holonomy `U_R`,
`|χ_R(U)| ≤ χ_R(I) = d_R` (proved in the 2026-06-18 finite
kernel note from the eigenvalue identity
`d_R^2 - |χ_R(U)|^2 = sum_{i<j}|z_i-z_j|^2 >= 0`).
The on-site a-term carries no link (a_eff = a, independent of U; verified in the runner), while the
hop-return b-term carries the link, so the gauge-invariant effective doublet coupling is
character-normalized: b_eff = b·χ_R(U)/d_R. Hence r_R = r₀·|χ_R(U)/d_R|² ≤ r₀, with equality only when
`U_R` is a scalar phase in the chosen representation. The runner confirms r_R ≤ r₀ over 800 random unitaries across reps d ∈ {1,2,3,8},
the representation-level equality condition, and strict suppression for generic matrices. The separate
kernel runner checks the finite identity and the fibre-average coefficient directly on deterministic
phase grids, so the suppression step is not an imported textbook input. **This is the bounded
algebraic inequality that the row carries — it is rep-agnostic and makes no use of any physical
sector-to-representation assignment.**

**(N-either-horn) Conditional alternatives.** If the supplied `b`-term
*does* carry the closed-holonomy dressing, it is character-capped (N-bound).
If the b-term carries *no* link (the reading on which the circulant C is a linkless generation
relabeling), then U never enters and r_R = r₀ is rep-independent — **no spread at all** (runner:
U = I gives r_R = r₀ for every rep). In these two displayed cases, the algebraic ratio `r_R` is bounded above by `r₀`.

## Conditional Physical Ordering (Open Bridge, Not Source Content)

**(N-order, CONDITIONAL) The observed spread would violate the cap *if* the bridge held.** The two
bridging steps below are *not* established in this note; the statement is conditional on them.

> *Bridge premise (open):* (i) the physical colourless-lepton sector is the trivial gauge
> representation and the physical coloured-quark sectors are nontrivial representations; (ii) the
> fibre-averaged ratio `r_R` is the registered physical Koide dial of each sector.

*If* (i) and (ii) held, then the colourless leptons would realize the uncapped bound r_lep = r₀ while
any coloured sector would be bounded by r_coloured ≤ r₀ = r_lep, whereas the observed ordering is the
reverse (r_lep = 1/2 < r_down ≈ 0.597 < r_up ≈ 0.773) — so the holonomy mechanism would predict
coloured sectors with *smaller* r than leptons while reality has *larger*, the wrong sign of the
spread. **Because the bridge premise is unsupplied, this physical falsification is conditional/open
and is not part of the source algebraic content.** No theorem here assigns the physical sectors to
the gauge representations, and the fibre-averaged-ratio → registered-dial identification is the open
readout import.

## Significance

The source content is the **direction** of the algebraic cap: a gauge-invariant holonomy on the
fibre-averaged generation operator can only push the ratio `r_R` *down* toward the degenerate r = 0
endpoint, never *up* above the trivial-rep value `r₀`. It resolves a genuine ambiguity about the
"colour-dressed" covariant-hopping channel: the holonomy neither trivially cancels (it does enter
`r_R`, via the normalized character) nor opens a free spread (it is bounded above by `r₀`).

*Conditional on the unsupplied sector-to-representation and registered-dial bridge* (see (N-order)),
this would close the "colour-dressed" covariant-hopping channel — the one open path named by the
preceding sector-blindness no-go — as a source of the observed coloured-above-leptonic spread, and
would point the splitter that raises r for coloured sectors toward a channel that is **not** a
gauge-invariant hopping holonomy — i.e. the within-sector measure / weighting prior (where the records
campaign localized it: PRs #4006/#4009/#4010/#4020) or an electroweak-partner (within-doublet,
T₃-asymmetric) channel. **Until that bridge is supplied, this channel-closure reading is conditional**;
the source result is the algebraic cap `r_R ≤ r₀`.

## Boundary (honest)

- **Source-side content = the conditional algebraic cap `r_R ≤ r₀`.** Forces **no** value of r; r₀ is a free bare
  coupling and the result is the inequality r_R ≤ r₀, rep-agnostic (any nontrivial rep is capped by
  the trivial one). Does not derive or force r = 1/2 (the firewall holds: r is registered,
  sector-dependent data).
- **The physical "closes the hopping-holonomy channel as the observed spread source" reading is
  open.** It depends on the unsupplied bridge that (i) assigns the physical
  colourless-lepton sector to the trivial gauge representation and the coloured-quark sectors to
  nontrivial representations, and (ii) identifies the fibre-averaged ratio `r_R` with the registered
  physical Koide dial of each sector. Neither step is established here. *Conditional on that bridge*,
  the cap would close the holonomy channel as the spread source and leave the within-sector measure /
  weighting-prior channel and an electroweak-partner channel as the next paths; the algebraic cap
  itself makes no such claim.
- The conditional physical reading uses the standard identification "colourless lepton ↔ trivial rep,
  coloured quark ↔ nontrivial rep." The bound r_R ≤ r₀ is rep-agnostic, so *only* the labelling of
  which physical sector is uncapped would use that identification — and that labelling is precisely
  the unsupplied bridge. The 2026-06-18 kernel update makes this boundary sharper:
  the character-suppression identity is exact conditional algebra, while the
  tensor dressing and physical sector-to-representation/readout bridge remain
  open.
- The fibre-average is the gauge-invariant (colour-singlet) effective generation operator; an
  un-traced coloured amplitude is gauge-variant (not a registered observable). A colour-*resolved*
  spectral/conjugacy-class reading is a distinct gauge-invariant object that does not equal the
  fibre-averaged operator. Such class-function or conjugacy-spectrum readouts are a distinct route
  outside this theorem and are not assessed here. The proved bound is only on the normalized-trace,
  colour-singlet generation operator defined above.

## Cited Source Context

These notes motivate the supplied construction; they do not authenticate its
closed-holonomy dressing or upgrade their current audit status:
- [`matter_gauge_minimal_coupling_fiber_frame_forces_connection`](MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md) — the covariant-hopping form H_cov = Σ aₓ† U_μ(x) a_{x+μ} + h.c. (the link rides the hop, not the on-site term).
- [`fiber_frame_local_redundancy_bridge`](FIBER_FRAME_LOCAL_REDUNDANCY_BRIDGE_NARROW_THEOREM_NOTE_2026-06-09.md) — the link law U_xy → gₓ U_xy g_y† and the fibre V_x.
- [`koide_gamma_axis_covariant_full_cube_orbit_law`](KOIDE_GAMMA_AXIS_COVARIANT_FULL_CUBE_ORBIT_LAW_NOTE_2026-04-18.md) — internal hop-return context; it does not derive the spatial closed-holonomy dressing used here.
- [`koide_circulant_character_bridge`](KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md) — the abstract form `H = aI + bC + b̄C²` and ratio definition `r = |b|²/a²`. The separately located `KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md` proves only an abstract Fourier-coordinate identity and is not physical carrier/readout authority for this no-go.
- [`three_generation_observable_theorem`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) — the gauge-uniform shared M₃(ℂ) generation carrier (the link acts on the fibre, not the generation index).

Source-side kernel support (audit required before any effective status change):
- [`flavor_gauge_holonomy_character_suppression_kernel`](FLAVOR_GAUGE_HOLONOMY_CHARACTER_SUPPRESSION_KERNEL_NARROW_THEOREM_NOTE_2026-06-18.md) — conditional finite proof and runner/cache for the normalized-character suppression kernel under the supplied dressing.

Context (no edge): `flavor_max_record_entropy_is_sector_blind_cannot_derive_the_koide_dial` (unaudited;
the note whose open "colour-dressed" path this closes in its holonomy form);
`flavor_hw1_staggered_projection_democratic_r0` (cited context; the bare undressed generation hop
gives r = 0 — the r₀ → 0 endpoint the suppression points toward).

## Forbidden-imports check

No new axiom. The covariant-hopping vehicle and closed-holonomy tensor dressing
are supplied conditions, not derived authority. Within those conditions the
bound holds for every `U`, so no background value is assumed or fitted. The character-suppression kernel is proved
directly on the finite link representation, not imported from textbook lattice gauge theory. The
observed r values enter only as anchors
for the conditional ordering reading, never as derivation inputs. r₀ and the per-sector couplings are
free symbols; no r value is computed or forced; Q = 1/3 + 2r/3 is the standard Koide-block relation.

## 2026-06-20 Source Repair: Algebraic Cap Narrowing

**Action taken: narrowed the row to the algebraic `r_R ≤ r₀` cap.** The
unsupplied bridge is *not* supplied; instead the physical sector-to-representation assignment and the
fibre-averaged-ratio → registered-Koide-dial identification are marked explicitly open,
and the physical "gauge holonomy suppresses the observed lepton/quark r below leptonic / wrong
ordering" conclusion is presented only as a consequence conditional on that bridge.

The title, claim, no-go section, significance, and boundary language now use
the cap-only boundary. The physical wrong-ordering conclusion is carried only in
the open-bridge conditional section, not as source content of the no-go.

Runner narrowing (`frontier_gauge_holonomy_suppresses_r_wrong_ordering_2026_06_15.py`): the check that
asserted the physical sector assignment — section [4], which compared the observed quark r values to
the leptonic "ceiling" as a falsification — was relabelled and re-scoped to a **conditional** check
that asserts only the algebraic arithmetic *if* the bridge premise held (the algebraic cap value and
the numeric ordering of the anchors), with explicit notes that the lepton↔trivial / quark↔nontrivial
assignment and the `r_R` → registered-dial identification are unsupplied bridge premises, not derived.
No derived value changed; all algebraic-cap checks ([1], [2], [3], [5], [6]) are unchanged. Runner
re-run deterministic, per-check PASS:/FAIL:, final TOTAL PASS=N FAIL=0; SHA-pinned cache regenerated.

**Caveat:** This is a source-side narrowing only. It does *not* supply the sector-to-representation
bridge or the registered-r-observable identification, and it does not set
status.
