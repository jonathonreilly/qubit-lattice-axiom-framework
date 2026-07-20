# Four-Dimensional Euclidean Gauge Tensor, Exact Lattice WTI, And Xi-Affine Static Proxies (Bounded)

**Date:** 2026-07-17

**Claim type:** bounded_theorem

**Type:** bounded exact algebra plus labeled finite-grid static proxies

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py`](../scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py)

**Cached runner output:**
[`logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt`](../logs/runner-cache/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.txt)

```yaml
actual_current_surface_status: bounded-support
trace_class: frontier_discovery
reachability_to_target: none
conditional_surface_status: "On one declared periodic N^4 Euclidean naive-Dirac reconstruction, the runner proves the Wilson gauge tensor block, midpoint lattice WTI, xi-affinity of a declared gauge-line family, and a tadpole closed form, and records positive fixed-probe static-response proxy signs. The result is not a bridge to the framework's continuous-time/spatial-Z^3 target, retained blocked 16x16 staggered carrier, physical pole speed, or RG coefficients."
hypothetical_axiom_status: null
admitted_observation_status: null
proposal_allowed: false
proposal_allowed_reason: "This is a standalone finite-object calculation, not a target-surface or carrier bridge. It cannot supply the physical mutual-drag coefficients of the velocity-RG chain."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Standalone Scope And Comparison Boundary

The runner studies a declared four-periodic `N^4` Euclidean lattice. Its
fermion matrix is `4 x 4` at each momentum and its loop grid covers the full
naive-fermion Brillouin zone. Color is one `su(2)` fundamental block. The
calculation does **not** implement:

- the continuous-time plus spatial-`Z^3` action surface of the velocity-RG
  target;
- the retained blocked `16 x 16` staggered carrier, its four-dimensional taste
  commutant, a reduced-zone Jacobian, or a matched taste/`N_f` normalization;
- a pole, on-shell, group-velocity, or other physical-speed observable; or
- a shell derivative, counterterm split, or beta-function extraction.

The filenames
`EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md`,
`EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md`,
`velocity_rg_logflow_framework_internal_2026-06-21`, and
`VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`
are therefore comparison surfaces only. Their open residuals motivate the
diagnostic, but they do not supply premises to this theorem and this note does
not close or partially close any of them. In particular, “positive mutual
drag” below always means positivity in the standalone fixed-probe proxy
algebra, never positivity of physical RG coefficients `a,b`.

## Statement

### Exact tier on the declared finite objects

1. **Gauge tensor.** In the link-midpoint mode convention, direct plaquette
   summation gives
   `M_mn = K delta_mn - qhat_m qhat_n`, `K = sum_m qhat_m^2`, including the
   exact gauge zero mode and covariant-gauge inverse. The tested modes are
   non-self-conjugate, for which the real-mode normalization is `V/4`.
   The runner also verifies `tr(T^a T^b) = delta^{ab}/2`.
2. **Lattice WTI.** For arbitrary tested anisotropic coefficients `v_mu`, the
   midpoint vertex obeys
   `khat.Gamma(p,p-k) = S0^-1(p) - S0^-1(p-k)` to the `1e-11` gate. A
   no-half-shift control fails at order one.
3. **Declared xi-family.** The loop calculation defines
   `D_w(xi)_mn = [delta_mn - (1-xi) qhat_m qhat_n/K_w]/K_w`, with
   `K_w = sum_m w_m qhat_m^2`. At `w=1` this is the covariant inverse for
   `xi>0` and its Landau-limit pseudoinverse at `xi=0`. At `w!=1` it is neither
   the inverse of an anisotropic Wilson tensor nor generically transverse; at
   some momenta its `xi=0` form is indefinite. These are defining limitations,
   not properties of a physical gauge covariance.
4. **Affine identities.** On this declared family, the rainbow response is
   exactly affine over `xi in {0,0.5,1.0,1.7}` and its slope agrees within
   `1e-10` with the WTI-reduced longitudinal expression assembled without
   vertex functions. The fermion-line seagull satisfies exactly
   `(out_s-out_t)_tad = (1-xi)(C_s-C_t)`. The total proxy keeps one sign only
   on the sampled `xi` window; its affine zero is near `xi=26`, so no all-`xi`
   claim is made.

### Labeled finite-grid witness tier

5. At `N=10`, the rainbow xi-slope at `delta=0.05` is within relative `5e-3`
   of the gauge-line integral `C_s-C_t`. Through `N=24`, the individual
   `C_s,C_t` terms still grow while the increments of their difference shrink.
   This is a finite-grid trend, not a continuum limit.
6. On the stated fit window, the xi-shift is constant-dominated and the total
   rainbow-plus-tadpole xi-slope decreases through the four sampled probes.
   The log/constant split is pivot-dependent and is not an RG-coefficient
   extraction.
7. In one shared Euclidean sign convention, two separate reconstructions give
   positive static-response directions:

   - gauge weights with exact offset `dv_B=+0.05131` give a fermion response
     `dv_F=+0.00098 g^2`;
   - fermion coefficients with offset `dv_F=+0.10526` give a gauge response
     `dv_B=+0.02177 g^2` at `N=12` and exact torus momentum
     `q=2*pi/N=0.52360`.

   At the two tested torus-compatible external momenta, the normalized Ward
   residual is below `1e-10` (roundoff-level in the live run). Reading the
   transverse component at these two momenta therefore does not rely on the
   former percent-level off-grid tolerance.
8. Dividing by the declared deformation offsets gives standalone proxies
   `a_proxy=+0.0191 g^2` and `b_proxy=+0.2068 g^2`. The associated purely
   algebraic `2 x 2` proxy matrix has eigenvalues
   `{0,-(a_proxy+b_proxy)}`, common-direction null vector `(1,1)`, and proxy
   contraction rate `+0.2259 g^2`. This arithmetic does not instantiate the
   exchange matrix of any retained physical chain.
9. The signs remain stable under `N=10 -> 12` for the sampled fermion probes,
   and the total fermion proxy retains its sign and decreases in magnitude
   when the gauge deformation is halved.

## Sign Bookkeeping On The Declared Euclidean Reconstruction

All two-point objects in this section are calculational reconstructions, not
registered framework observables. The bookkeeping starts from

```text
Z = Int dA dpsibar dpsi exp(-S_G[A] - psibar Dslash[A] psi).
```

At quadratic abelianized order, `S_G` is the four-dimensional Wilson
plaquette form and `Dslash` is the midpoint-gauged naive-Dirac kernel. The
one-gluon vertex is `v_mu cos(k_mu+q_mu/2)` and the seagull is
`-v_mu sin(k_mu)`.

- Expanding the fermion propagator gives
  `S^-1=S0^-1-Sigma`, with rainbow and fermion-line seagull insertions. Near
  the declared probe, `v_mu -> v_mu-g^2 C_F out_mu`, so the ratio proxy obeys
  `dv_F=-g^2 C_F(out_s-out_t)`. The runner derives `C_F=3/4` from the three
  fundamental `su(2)` generators.
- Integrating the declared fermion block gives
  `S_eff=S_G-tr log Dslash`. Its second variation has the coded bubble and
  seagull signs, and one fundamental color trace supplies `T_F=1/2`. At the
  exact torus momenta used in item 7, the complete finite sum is transverse to
  roundoff and its selected component has the stated positive sign.
- The fermion-side loop replaces the covariance by the declared `D_w(xi)`
  family, while the gauge-side loop uses the deformed naive-Dirac kernel.
  Thus the two signs share formal sign bookkeeping but are not derived from a
  single established positive functional integral at `w!=1`.

The `4 x 4` spin matrix, full naive Brillouin zone, and one fundamental color
block are exactly what is coded. No taste multiplicity, number of physical
flavors, reduced-zone Jacobian, or gauge-coupling matching factor should be
inferred from `C_F` or `T_F`.

## What This Supplies

This note supplies a reproducible finite-object theorem: the Wilson tensor,
midpoint WTI, affine `xi` identities, an exact finite-torus Ward gate at two
external momenta, and static proxy signs on one declared four-dimensional
Euclidean naive-Dirac reconstruction. It is useful as a test fixture for a
future calculation that explicitly supplies the missing bridges.

It supplies **no direct target reachability**. In particular, it does not
convert the static ratios into physical speeds, determine physical `a,b`, or
show that the proxy signs survive target-surface, carrier, normalization,
true-inverse, counterterm, volume, or on-shell matching.

## What Remains Open: Corrected Independent Wall Set

- **W1 — target surface:** bridge from the periodic `N^4` Euclidean kernel to
  the continuous-time/spatial-`Z^3` target action.
- **W2 — carrier and normalization:** embed the calculation in the retained
  blocked `16 x 16` staggered carrier and derive taste, reduced-BZ Jacobian,
  `N_f`, and coupling normalization.
- **W3 — true gauge inverse:** replace `D_w(xi)` by the inverse of the actual
  anisotropic gauge tensor and establish the appropriate gauge-independence
  statement.
- **W4 — physical speed:** define and control a pole/on-shell or otherwise
  physical velocity observable; the finite Euclidean coefficient ratios are
  off-shell reconstruction definitions.
- **W5 — RG extraction:** perform shell/counterterm/log extraction and derive
  the signs and magnitudes of physical RG coefficients `a,b`.
- **W6 — limits and probes:** control finite-volume, external-momentum,
  deformation, probe, and continuum limits. Exact transversality has been
  shown only at the two tested torus momenta.
- **W7 — nonabelian completion:** include the omitted nonabelian gauge
  self-interactions and all diagrams at the claimed order.
- **W8 — coupled flow:** replace the two fixed-background responses with a
  self-consistent coupled flow.
- **W9 — spatial coefficient:** derive the spatial-only power-divergent mixing
  coefficient required by the comparison chain.
- **W10 — anomalous dimension:** derive the relevant fixed-point anomalous
  dimension.
- **W11 — LV sufficiency:** complete the quantitative Lorentz-violation bound
  comparison.

Closing any one wall does not close the others. The complete independence
record appears in N2 below.

## Import Ledger

| Input | Role | Class | Disposition |
|---|---|---|---|
| Periodic `N^4` Euclidean lattice, Wilson quadratic form, midpoint-gauged `4 x 4` naive-Dirac kernel | complete calculation surface | declared reconstruction definition | disclosed; not the target action |
| Full half-integer loop grid `k=((n+1/2)/N)2*pi-pi` | zero-mode-avoiding finite sum | declared sampling convention | disclosed; no boundary-condition or continuum claim |
| Exact external probe `q=2*pi/N` in V6 | finite-torus Ward-compatible momentum | finite-grid control | discharged at the two tested orientations; broader limit remains W6 |
| `C_F=3/4`, `T_F=1/2` | one `su(2)` fundamental color block | exact group arithmetic | discharged; no taste or `N_f` factor inferred |
| Blocked staggered spin/taste structure | boundary against carrier identification | retained boundary authority: [blocked four-taste module](STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md) and [spin/taste Clifford core](ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md) | not consumed as this runner's carrier; W2 open |
| `D_w(xi)` | propagator-shaped object in V3–V7 | declared definition; true inverse only at `w=1` | W3 open |
| `v_F=v_s/v_t`, `v_B=sqrt(c_s/c_t)` | static direction proxies | reconstruction definitions | not physical pole speeds; W4 open |
| Positive physical mutual drag | conceptual comparison residual | not imported | not discharged; W1–W8 remain |
| Spatial coefficient, anomalous dimension, LV bound | downstream comparison inputs | not imported | W9–W11 remain |

## No-Go Discipline Gate

This gate audits the boundary of the narrowed standalone claim. It does not
claim that the eleven physical walls are no-go results.

### N1 — Alternative routes

The counted rows below are normalized by primary object, load-bearing
mechanism, and terminal obligation. They are executed mathematical attacks,
not different agents, phrasings, or statements that a calculation is absent.

| Normalized attack route | Marker | Executed test and exact boundary | Retained authority that fixes the residual boundary | Unaudited comparison locator (context only; not N1 support) |
|---|---|---|---|---|
| Finite Euclidean tensor algebra / explicit `4 x 4` matrices / verify the declared identities | ATTEMPTED | Runner `part_1`–`part_3` reconstructs the matrices, projectors, `D_w(xi)`, and affine split exactly. It succeeds for the declared finite objects, but that success has no carrier-identification step. | `STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md:163-185` (`retained_bounded`) proves an explicitly intertwined `16 x 16` four-taste module, not this naive block. | None. |
| External-momentum Ward route / exact finite-torus shifts / establish transversality | ATTEMPTED | Runner V6 tests both temporal and spatial `q=2*pi/N` orientations at the `1e-10` gate; the in-memory off-grid `q=0.3` mutation fails that gate. The result therefore establishes only the exact finite-torus statement. | `CONTINUUM_LIMIT_NOTE.md:3-50` (`retained_bounded`) is the repo's retained boundary that finite-resolution trend evidence does not promote to a strict limit without a separate convergence theorem. | `VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md:87-93` is unaudited and used only to name the downstream physical prescription. |
| Contact-term route / midpoint seagull completion / protect the Ward identity | ATTEMPTED | The omitted-seagull mutation fails V6, while the completed bubble-plus-seagull tensor passes. This distinguishes the contact-term mechanism but does not construct an interacting counterterm. | `GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md:7-19,273-277,289-307` (`retained`) fixes an abstract compact-group Wilson mixed-kernel theorem and explicitly separates that theorem from fermion and gauge-normalization gates; the finite seagull test supplies neither that action/kernel placement nor a fermion counterterm. | `EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md:98-111` is unaudited and used only to name the proposed counterterm bridge. |
| Gauge-line route / test `D_w(xi)` as a true anisotropic inverse / obtain a physical covariance | ATTEMPTED | V3 plus an independent temporal-mode calculation at `w=(0.95,1.05,1.05,1.05)` gives nonzero `||qhat^T D_w(0)||` and one negative eigenvalue. Thus the declared family is not a true anisotropic covariance for `w!=1`; W3 remains a constructive replacement route. | The retained Wilson-kernel theorem at `GAUGE_TEMPORAL_GAUGE_MIXED_KERNEL_SPATIAL_LINK_FACTORIZATION_NARROW_THEOREM_NOTE_2026-05-10.md:27-39,138-140,179-220` derives an abstract mixed kernel from a Wilson action, normalized Haar measure, and compact-group convolution. The declared indefinite `D_w` does not instantiate that action/Haar construction and supplies no inverse theorem. | `VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md:121-133` is unaudited and used only to name the full tensor/vertex comparison. |
| Carrier/taste route / compare the naive block with retained staggered structure / fix multiplicity and taste normalization | ATTEMPTED | The runner independently verifies only one `su(2)` color block (`C_F=3/4`, `T_F=1/2`); the import comparison then checks that the retained carrier has a four-dimensional taste commutant. The dimensions and commutants differ, so no identification or multiplicity is inferred. | `ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md:57-80` (`retained_bounded`) proves the `16`-dimensional commutant/taste dressing, while `NAIVE_LATTICE_FERMION_TWO_POWER_D_SPECIES_COUNT_NARROW_THEOREM_NOTE_2026-05-10.md:5-34` (`retained`) fixes the naive `2^d` species multiplicity. | The gauge-seagull lines 91-93 are unaudited and used only as a comparison warning. |
| Scale-extraction route / vary the probe and fit the affine response / obtain an RG logarithm | ATTEMPTED | V5 computes several finite probes and a pivot-dependent diagnostic slope; decreasing-probe values change and no shell derivative is invariantly extracted. The executed trend test therefore fails to supply a counterterm or log coefficient. | `CONTINUUM_LIMIT_NOTE.md:3-50,210-221` (`retained_bounded`) confines finite-resolution trends to finite evidence absent a retained convergence/extrapolation theorem. | `VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md:121-133` is unaudited and used only to name the proposed one-loop extraction. |
| Dynamic mutual-drag route / insert the two static signs into the exact `2 x 2` proxy / establish target attraction | ATTEMPTED | V6 checks both positive static responses and the abstract proxy eigenvalues; reversing the static-response sign triggers three failures. No time-dependent flow, on-shell observable, or coupled beta function is produced, so the physical inference is rejected. | `LINEAR_RESPONSE_TRUE_KUBO_NOTE.md:13-21,174-194` (`retained_bounded`) separates a literal first-order response formula and dynamic conditions from heuristic/static agreement; `PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md:15-24,198-208` (`retained_bounded`) separately gates physical-Hamiltonian identification. | `EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md:98-121` is unaudited and used only as the target comparison. |

Continuous-time/spatial-`Z^3`, pole/on-shell, full nonabelian, and coupled-flow
constructions remain **OPEN ROUTES (not counted as ATTEMPTED)**. Their absence
is a wall disclosure, not evidence that they fail or cannot be completed. The
seven counted attacks support only the bounded standalone surface.

### N2 — Wall independence

For each pair, `N/N/I` means closing the left wall does not close the right,
closing the right does not close the left, and no shared unresolved premise
makes them duplicates.

| Left wall | Later-wall pairs, all `N/N/I` |
|---|---|
| W1 | W2, W3, W4, W5, W6, W7, W8, W9, W10, W11 |
| W2 | W3, W4, W5, W6, W7, W8, W9, W10, W11 |
| W3 | W4, W5, W6, W7, W8, W9, W10, W11 |
| W4 | W5, W6, W7, W8, W9, W10, W11 |
| W5 | W6, W7, W8, W9, W10, W11 |
| W6 | W7, W8, W9, W10, W11 |
| W7 | W8, W9, W10, W11 |
| W8 | W9, W10, W11 |
| W9 | W10, W11 |
| W10 | W11 |

### N3 — Hidden-assumption scan

A literal scan of this note, its primary runner, and its committed cache used
the complete No-Go Discipline N3 trigger list. The only substantive source
hits or close variants are classified here; none is silently promoted to
authority.

| Literal hit / locator | Classification | Resolution |
|---|---|---|
| “registered framework observables” in Sign Bookkeeping (source line 121 before this checklist) | non-load-bearing comparison context | It names what would be required downstream; this note explicitly supplies only static direction proxies and leaves W4–W5 open. |
| “fixed-background responses” in W8 (source line 185 before this checklist) | explicit hidden condition promoted to W8 | The background is not evolved. W8 is already one of the eleven disclosed walls, and the N2 count includes it. |

The conceptual premise scan then rejects same-action, same-carrier,
color-equals-total-multiplicity, finite-ratio-equals-speed,
arbitrary-momentum transversality, static-sign-equals-RG-sign, and
`D_w`-equals-covariance readings through W1–W6. Promoting the fixed-background
condition does not change the wall count because it is exactly W8.

### N4 — Residual matching

| Witness locator | Residual attacked by witness | Residual tested here | Exact match? / disposition |
|---|---|---|---|
| `EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md:98-121` | interacting vertices/counterterm must supply physical positive `a,b` and LV-bound sufficiency | two static finite-grid responses on a declared different regulator/carrier | No; drop as closure witness, retain only as comparison boundary. |
| `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md:18-27,34-45` | continuous-time/spatial-`Z^3` physical coefficient and anomalous-dimension bridge | periodic `N^4` Euclidean sums with no continuous-time action | No; drop as closure witness. |
| `VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md:121-133` | full gauge tensor, vertex, and one-loop counterterm | exact declared tensor/WTI plus a deliberately non-covariant `D_w`; no counterterm | No; method overlap is not residual closure, so drop as closure witness. |
| `VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md:87-93` | gauge-invariant velocity prescription plus taste/doubler normalization | one unnormalized naive color block over the full BZ | No; drop as closure witness. |

Recount after dropping all four non-matches: exact target-closure witnesses
`= 0`. They remain citations only for boundary accounting. Therefore
`reachability_to_target` stays `none`; the bounded finite-object results do not
inherit any comparison row's stronger residual.

### N5 — Rhetoric audit

| Negative or limiting phrase | Per-element / site resolution | Mode resolution | Block resolution | Lattice-wide resolution | Narrowest supported wording |
|---|---|---|---|---|---|
| `D_w` is not a true anisotropic covariance for `w!=1` | not a site claim | one explicit temporal momentum falsifies transversality | full `4 x 4` eigenvalue/inverse test at that mode | no all-momentum classification attempted | the declared family is generally non-covariant, witnessed by an explicit mode; no impossibility theorem for another covariance is claimed |
| finite static sign is not an RG coefficient | integrand contributions are summed, not interpreted separately | several finite probe values are tested | one naive spin/color block only | `N=10,12` finite-grid averages only | this artifact does not perform a shell derivative, counterterm, or log extraction; it does not claim none can exist |
| torus transversality is not arbitrary-momentum transversality | not a site claim | exactly two `q=2*pi/N` orientations pass and the off-grid mutation fails | complete declared tensor at those modes | one finite torus per test | transverse only at the two gated finite-torus momenta; no continuum statement |
| naive block is not the retained physical carrier | not a site claim | no pole-mode identification attempted | `4 x 4` naive block compared with retained `16 x 16` spin/taste structure | no interacting physical lattice model assembled | carriers are distinct until an explicit intertwiner, multiplicity, and normalization are supplied |
| static proxy is not physical speed | not a site claim | no on-shell dispersion is solved | ratios use one declared block | finite-grid direction averages only | static direction proxy only; no pole speed or beta function |

Thus “exact” refers only to gated finite algebra/sums; “proxy,” “static,”
“finite-grid,” and “standalone” stay attached to every sign statement. Untested
resolutions are reported as open, never converted into universal negatives.

### N6 — Partial-closure paths

No new axiom is proposed. Viable partial routes are: transfer the exact WTI
calculus to the retained carrier (W2), repeat V6 with a true anisotropic gauge
inverse (W3), define an on-shell speed observable (W4), and then perform the
counterterm/RG extraction (W5). Exact torus momenta already repair the narrow
finite-sum Ward gate but do not repair the remaining walls.

### N7 — Steelman

**Hostile reviewer steelman.** The strongest attack on this boundary is that
the retained blocked carrier already decomposes into four intertwined
four-dimensional spin summands, while the retained Clifford core identifies a
taste-singlet spin algebra (`STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md:163-185` and
`ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md:57-80`). A careful
taste-singlet lift could therefore preserve the finite Ward and sign
calculation, defeating any suggestion that the naive block is useless. The
terminal obligation is concrete: construct the intertwiner on the retained
carrier, include the correct taste/BZ multiplicity and true anisotropic gauge
inverse, and recompute the on-shell counterterm. This route is unclosed, so the
note makes no no-go claim against it; it ships only the finite regression
fixture and names that lift as the next constructive test.

### N8 — Cross-cycle echo

Both `docs/` and all repository `NO_GO_LEDGER.md` files were searched for
velocity, anisotropy, carrier, normalization, counterterm, pole, taste,
doubler, static, and continuous-time echoes.

| Prior echo and locator | Since retired? | Mechanism / applicability here |
|---|---|---|
| Retained blocked module and spin/taste core cited above | Partially advanced, not retired | Exact decomposition and commutant now supply a constructive carrier-lift route, but no velocity counterterm or normalization. This is W2's escape, not closure. |
| `FREE_STAGGERED_POLE_RESIDUE_DIRAC_CARRIER_CAR_RELABELING_BOUNDED_THEOREM_NOTE_2026-07-17.md` | Bounded carrier theorem exists; physical identification remains open | It keeps the pole/CAR route available, matching W4, but is not imported as target closure. |
| `VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md:87-93` and `VELOCITY_RG_LOGFLOW_FRAMEWORK_INTERNAL_2026-06-21.md:121-133` | Not retired | They name gauge-invariant prescription, taste normalization, full tensor/vertex, and counterterm routes; these are W2–W5. |
| `.claude/science/physics-loops/free-dirac-carrier-retirement-20260717/NO_GO_LEDGER.md:7-12` | Narrow carrier result only; Wightman/physical lift not retired | Its “Euclidean 2-point is not Wightman reconstruction” boundary directly forbids promoting this finite Euclidean fixture. |
| `.claude/science/physics-loops/planck-clifford-carrier-closure-20260710/NO_GO_LEDGER.md:10-12` | Partial constructive route, not retired | A native taste extension exists, but temporal operator/copy selection remains open; this reinforces the steelman rather than a no-go. |
| `.claude/science/physics-loops/gauge-wilson-isotropy-boundary-closure-20260710/NO_GO_LEDGER.md:6-8` | One eta-product route closed; broader anisotropic dynamics explicitly open | The retirement mechanism is exact parity/isotropy on a specified operator, not applicable to this missing interacting counterterm. |
| `.claude/science/physics-loops/conformal-causal-source-repair-block01-20260716/NO_GO_LEDGER.md:3-28` | Abstract word/count-to-clock shortcut blocked; dynamics escape open | It confirms that finite ordering/rate proxies do not supply a physical clock, matching the refusal to infer a beta flow from static responses. |

No prior ledger records a convention, ratification, or theorem that retires
W1–W8 for this target. The mechanisms that did retire narrower routes have all
been considered: carrier decomposition becomes the explicit W2 lift; exact
operator parity does not construct the counterterm; and a dynamics/clock input
remains required for a physical flow.

**Overall N1–N8 status for the narrowed standalone claim: PASS.**

## Verification

Run:

```bash
python3 scripts/velocity_rg_gauge_tensor_wti_xi_affine_drag_2026_07_17.py
```

Expected final line:

```text
TOTAL: PASS=25 FAIL=0
```

The runner declares `AUDIT_TIMEOUT_SEC = 280` and its output is deterministic
under the repository cache contract.

## Audit Boundary

This note does not run audit, set audit status, or promote any chain row. An
independent audit may evaluate only the bounded standalone surface stated
here. No audit status should propagate from this candidate to any velocity-RG
parent or comparison row.
