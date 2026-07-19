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

| Route | Marker | Precise locator and result |
|---|---|---|
| Standalone `N^4` Euclidean algebra | ATTEMPTED | Statement items 1–4 and runner `part_1`–`part_3`; succeeds only on the declared finite objects. |
| Continuous-time/spatial-`Z^3` surface | ATTEMPTED | Standalone Scope and W1; no such kernel is coded, so the bridge remains open. |
| Retained blocked staggered carrier | ATTEMPTED | Import Ledger links and W2; retained `16 x 16` spin/taste structure is identified as a different carrier, not silently equated to the runner. |
| Exact torus external momentum | ATTEMPTED | Statement item 7 and runner `part_6`; `q=2*pi/N` restores the finite-sum Ward identity to the strict `1e-10` gate while preserving the positive proxy sign. |
| True anisotropic Wilson inverse | ATTEMPTED | Statement item 3 and W3; the current `D_w` is proven not to be that inverse for `w!=1`, so this viable route remains open. |
| Pole/on-shell velocity | ATTEMPTED | Standalone Scope and W4; no pole or physical-energy prescription is present. |
| Shell/counterterm/log extraction | ATTEMPTED | Statement items 6 and 8 plus W5; the runner exposes a fit diagnostic but does not extract an RG coefficient. |
| Finite-volume/probe/continuum control | ATTEMPTED | Statement items 5, 7, and 9 plus W6; finite samples and two exact torus momenta do not establish a limit. |
| Full nonabelian and coupled-flow routes | ATTEMPTED | W7–W8; omitted diagrams and fixed-background structure are explicit. |

The scoped standalone route succeeds. Every route needed to identify it with
the physical velocity-RG target remains visibly open.

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

| Candidate hidden premise | Resolution |
|---|---|
| “Same action surface” | Rejected explicitly: W1 separates periodic Euclidean time from the target surface. |
| “Same fermion carrier” | Rejected explicitly: W2 and the Import Ledger separate `4 x 4` naive spin matrices from the retained blocked `16 x 16` carrier. |
| “Color factor equals total multiplicity” | Rejected explicitly: `C_F,T_F` cover one color block only; taste/BZ/`N_f` matching remains W2. |
| “Finite coefficient ratio is physical speed” | Rejected explicitly: ratios are static definitions; W4 remains. |
| “Transverse at arbitrary external momentum” | Rejected explicitly: the strict claim is only for two tested `q=2*pi/N` orientations; W6 remains. |
| “Static sign is RG sign” | Rejected explicitly in Statement item 8 and W5. |
| “Declared `D_w` is a covariance” | Rejected explicitly in Statement item 3 and W3. |

No undeclared axiom is needed for the finite-object theorem; none of these
premises is smuggled into target reachability.

### N4 — Residual matching

| Comparison surface | Its residual | Output here | Match? |
|---|---|---|---|
| Exchange-matrix note | physical framework one-loop counterterms and positive `a,b` | static finite-grid ratios on another regulator/carrier | No; conceptual comparison only |
| Interacting parent | continuous-time/spatial-`Z^3` physical coefficient | periodic `N^4` Euclidean response | No |
| Log-flow row | full tensor/vertex/counterterm calculation | exact tensor/WTI plus declared non-covariance `D_w`, no counterterm | Partial method overlap, no closure |
| Seagull row | taste/doubler normalization | one unnormalized naive block over the full BZ | No; W2 |

Because no residual matches completely, `reachability_to_target` is `none`.

### N5 — Rhetoric audit

- “Exact” refers only to the explicitly gated finite algebra and finite sums.
- “Transverse” refers only to the two tested torus-compatible momenta and the
  `1e-10` normalized Ward gate.
- “Proxy,” “static,” “finite-grid,” and “standalone” are retained wherever a
  sign or contraction is discussed.
- “Velocity-RG coefficient,” “physical speed,” “chain action surface,” and
  “one-hop authority” are not claimed.
- The finite-grid trend language makes no `delta->0`, volume, or continuum
  inference.

### N6 — Partial-closure paths

No new axiom is proposed. Viable partial routes are: transfer the exact WTI
calculus to the retained carrier (W2), repeat V6 with a true anisotropic gauge
inverse (W3), define an on-shell speed observable (W4), and then perform the
counterterm/RG extraction (W5). Exact torus momenta already repair the narrow
finite-sum Ward gate but do not repair the remaining walls.

### N7 — Steelman

The strongest defensible reading is useful but narrow: exact V1–V3 algebra,
an exact torus-momentum Ward control, and two reproducible positive static
proxy signs form a good regression fixture. The retained blocked carrier's
spin-block decomposition suggests a taste-singlet extension may preserve the
sign, but only an explicit normalization and carrier calculation can establish
that. The current artifact itself stops before that inference.

### N8 — Cross-cycle echo

Current-main comparison exposes four recurring mechanisms, all reflected in
the corrected walls:

- the retained [blocked four-taste module](STAGGERED_OS0_SUPPLIED_ACTION_KS_BLOCKING_FOUR_TASTE_MODULE_NARROW_THEOREM_NOTE_2026-07-11.md)
  and [spin/taste core](ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md)
  motivate W2 without being substituted into this runner;
- `FREE_STAGGERED_POLE_RESIDUE_DIRAC_CARRIER_CAR_RELABELING_BOUNDED_THEOREM_NOTE_2026-07-17.md`
  keeps the pole/physical-observable route visible but is not consumed as
  retained authority, matching W4;
- `VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md`
  records the taste/doubler-normalization problem, now W2; and
- `velocity_rg_logflow_framework_internal_2026-06-21` records the missing
  counterterm/RG extraction, now W5.

The narrowed boundary therefore does not erase mechanisms already discovered
elsewhere.

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
