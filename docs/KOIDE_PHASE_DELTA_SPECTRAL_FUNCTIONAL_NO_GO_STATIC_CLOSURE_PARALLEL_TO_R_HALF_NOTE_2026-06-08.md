# Koide Phase δ Is an Admission — Spectral-Functional No-Go (Static Closure Parallel to r=1/2) Note

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-08
**Type:** named-obstruction no-go (general spectral-functional closure)
**Claim type:** no_go
**Status:** no-go proposal. Closes the **spectral/variational** route to the
Koide C₃-breaking phase `δ ≈ 2/9` (which sets the charged-lepton mass *values*),
completing the static `δ` closure parallel to the `r = 1/2` closure. The
irreducible residual is a CP-odd, non-spectral scale gated on the un-derived
staggered-Dirac / `F̃F` action-class — the **same** gate as `θ_gauge`. Adds no
axiom, no fitted/imported value. Audit verdict set by the independent audit lane.
**Authority role:** no-go source proposal (the AC_φλ phase parameter).
**Primary runner:**
[`scripts/koide_delta_spectral_functional_no_go_2026_06_08.py`](../scripts/koide_delta_spectral_functional_no_go_2026_06_08.py)
(exact sympy/numpy, PASS=9).

## The phase

The charged-lepton generation Yukawa is the Hermitian C₃ circulant
`M = a I + b C + b̄ C²` with `b = |b| e^{iδ}`; eigenvalues
`λ_k = a + 2|b| cos(δ + 2πk/3)` (real). With the `r = 1/2` amplitude
`|b|/a = 1/√2` the Brannen form `√m_k ∝ 1 + √2 cos(δ + 2πk/3)` reproduces the PDG
charged-lepton √-mass ratios at `δ ≈ 2/9` rad (`u_phys = cos(2/3) ≈ 0.786`). So
`δ` is the physical knob that sets the actual lepton mass values — the phase half
of the highest-leverage Tier-A admission `AC_φλ` (the magnitude half `r = 1/2`
was closed separately:
[`KOIDE_R_HALF_DYNAMICAL_DIRAC_GATE_CLOSED_FULLY_RESOLVED_ADMISSION_NO_GO_NOTE_2026-06-08.md`](KOIDE_R_HALF_DYNAMICAL_DIRAC_GATE_CLOSED_FULLY_RESOLVED_ADMISSION_NO_GO_NOTE_2026-06-08.md)).

## Result: no framework-native spectral functional selects δ

**The `cos 3δ` collapse.** Every symmetric/spectral function of `M` is a function
of the single coordinate `u = cos 3δ`: `e₁ = 3a` and `e₂ = 3(a²−|b|²)` are
`δ`-independent, and `e₃ = det M = a³ − 3a|b|² + 2|b|³ u` is **affine** in `u`
(circulant-determinant identity `det circ(a,b,b̄) = a³+b³+b̄³−3a|b|²`, with
`b³+b̄³ = 2|b|³ cos 3δ`). By Newton's identities the power sums `p₁..p₆` — hence
*every* symmetric functional — depend on `δ` only through `u`.

**Monotone canonical functionals → degenerate boundary only.** The two canonical
framework readouts — `det M` and the Coleman-Weinberg modulus `Tr log|M|` — are
**monotonic** in `u` (`d(det)/du = 2|b|³ > 0`; `d(Tr log)/du = 2|b|³/det > 0`).
Their `δ`-gradient is `−3 sin 3δ · F'(u)`, which vanishes **only** at `sin 3δ = 0`,
i.e. `δ = k·60°` — exactly the **degenerate** spectra (two equal masses). The
physical non-degenerate `δ ≈ 2/9` sits at strictly interior `u ≈ 0.786` and is
never a stationary point.

**The last spectral hatch (the unique non-monotone functional).** The squared-
Vandermonde discriminant `D = ∏_{i<j}(λ_i−λ_j)²` is the *only* in-range
non-monotone spectral functional (it is quadratic in `e₃`, hence in `u`). Its
interior extremum is at `u* = 0`, i.e. `δ = 30°`, **amplitude-independent** (a
concave maximum — maximal generation spread at the symmetric midpoint), *not* the
physical `2/9`. So even the one functional that could in principle have an
interior stationary point lands on the symmetric `30°`, never `cos(2/3)`.

**Interior selection is circular.** A spectral functional stationary at the
interior `u_phys ≈ 0.786` would need `F'(u_phys) = 0` — a bespoke non-monotone `F`
whose extremum is hand-tuned to `cos(2/3)`, i.e. `2/9` **encoded**, not derived.
An exhaustive search for `A cos(2/3) + B sin(2/3) + C = 0` over natural framework
constants returns zero hits, confirming the tuning is transcendental.

## The escape class (CP-odd / non-spectral) collapses into the graveyard

An eight-lens adversarial red-team hunted every framework-native object that
*escapes* the spectral class (CP-odd / labeled / odd-in-`δ`). **Zero** selected
`δ ≈ 2/9` non-circularly; each collapses into an already-closed residual:

- **APS-η / spectral-flow.** `η(1,2;3) = 2/9` is exact (`(ω−1)(ω²−1) = 3`) and
  genuinely a labeled rep-theory index (correctly outside the spectral no-go) —
  **but** it is the dimensionless *rational* `2/9`; the index *phase* `2π·η =
  2π/9` gives unphysical negative masses, and reading `2/9` as a *radian* is the
  radian-bridge obstruction (`{qπ : q∈ℚ} ∩ ℚ = {0}`; already
  `KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY` and
  `KOIDE_PHASE_APS_ETA_PARITY_ROUTE_NARROW_THEOREM_NOTE_2026-05-23`).
- **CP-odd / θ-vacuum term, discriminant `Δ ∝ sin 3δ`, generation-loop phase
  `arg(b³) = 3δ`.** Each is genuinely odd in `δ` (escapes the spectrum's even/
  sign-blindness) but requires an absolute CP-odd **scale** the framework does
  not supply: it is **gated** on the un-derived staggered-Dirac `γ₅` / `F̃F`
  action-class (`KOIDE_PHASE_DELTA_CLEAN_MODULUS_ONLY_DEGENERATE`), the *same*
  gate as `θ_gauge`.
- **Berry holonomy.** The generation eigenframe is the `δ`-independent DFT (zero
  curvature); the qubit-loop latitude is `δ`-blind (a function of `r` only), and
  the open-arc readout returns the input (tautology). No native latitude lands on
  `2/9`.
- **K-reality + a second condition.** K-reality forces `δ = 0` (degenerate); the
  available second conditions give `30°` (discriminant) or `45°` (HS-norm
  balance), never `2/9`.
- **Z₂ orientation (Cl(3) pseudoscalar).** The spectrum is **even** in `δ`
  (`δ → −δ` relabels `k → −k`), so the alternating Vandermonde `Δ ∝ sin 3δ`
  carries only **sign(δ)** — a single Z₂ bit (the handedness residual), provably
  unable to encode the continuous magnitude `|δ|`.

## The shared gate with θ_gauge (obstruction, not value)

Both `δ` and `θ_gauge` are blocked by the **same** missing object: an
axiomatically-supplied CP-odd action class (`F̃F` slot / staggered-Dirac `γ₅`).
`θ_gauge` is itself an admission
([`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md`](STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07.md)).
This is a real **common-cause unification of the two obstructions** — but **not**
a value link: (i) the splice was already pruned
(`STRONG_CP_JOINT_BRIDGE_FAILS_HOLOMORPHIC_RESIDUAL_2026-06-04`); (ii) **sector
mismatch** — `θ̄` enters via the axial-U(1)–SU(3)_c² anomaly with coefficient the
color Dynkin index, and charged leptons are color singlets, so strong-CP places
**zero** constraint on the lepton phase; (iii) `arg(b³) = Koide Q` is a
*det_C-class coincidence* (`2/3 = 3·(2/9)` only at the physical point; `Q = 2/3`
on the whole cone while `3δ` varies), **not** a functional identity. Ship the
shared-obstruction statement; do **not** ship a `δ ↔ θ_gauge` value derivation.

## Verdict

The framework derives the *structure* around `δ` (the `cos 3δ` collapse, the
Brannen form, the spectral-functional no-go) but **not the value** `δ ≈ 2/9`.
Clean spectral/variational dynamics give the trivial/degenerate result
(`δ = k·60°`, or the symmetric `30°`), exactly as clean dynamics give `r = 1` for
the magnitude. **The Koide phase `δ` is an admission**, parallel to `r = 1/2`;
together they confirm the framework does not derive the charged-lepton mass
ratios. The residual is a single CP-odd, non-spectral scale, gated on the
un-derived staggered-Dirac / `F̃F` action-class — the same open primitive as
`r = 1/2` and `θ_gauge`.

## What is and is not claimed

- **Is:** no framework-native spectral functional selects the non-degenerate
  `δ ≈ 2/9` (monotone → degenerate boundary; the unique non-monotone discriminant
  → `30°`; interior selection is circular); every CP-odd/non-spectral escape
  collapses into the radian-bridge, the gated CP-odd action-class, sign-only
  orientation, or a label-dependent (non-Record) readout; `δ` and `θ_gauge` share
  one obstruction gate (not a value link).
- **Is not:** does **not** prove the metaphysical impossibility of any conceivable
  selector (the residual is genuinely open, gated on un-derived dynamics); does
  **not** re-ship the APS-η / radian-bridge / Wilson-eigenline / cobordism routes
  (already closed); does **not** claim `arg(b³) = Koide Q` as a functional
  identity; introduces no axiom; changes no prediction.

## Load-bearing inputs

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the C₃
  generation circulant structure and the Record symmetric/spectral readout (with
  its negative list disclaiming weighting/arrow/winding); all algebra (the
  circulant-determinant identity, `eₙ` and `pₙ` as functions of `u = cos 3δ`, the
  discriminant critical point, the even-in-`δ` spectrum) is reproven in the runner.

Companion + context (plain references, not load-bearing deps):
`KOIDE_R_HALF_DYNAMICAL_DIRAC_GATE_CLOSED_FULLY_RESOLVED_ADMISSION_NO_GO_NOTE_2026-06-08`,
`KOIDE_PHASE_DELTA_CLEAN_MODULUS_ONLY_DEGENERATE_NARROW_NO_GO_NOTE_2026-06-04`,
`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24`,
`KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_NOTE_2026-04-24`,
`KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_NOTE_2026-04-24`,
`STRONG_CP_GAUGE_THETA_NOT_FORCED_BY_REALITY_POSITIVITY_OR_CPT_BOUNDED_NOTE_2026-06-07`,
`ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23`.

## Forbidden-imports check

No PDG / fitted / literature numerical comparator is consumed as a derivation
input. The circulant-determinant identity, the `u = cos 3δ` collapse of every
symmetric function (Newton), the monotonicity of `det`/`Tr log`, the discriminant
critical point `u* = 0`, and the even-in-`δ` spectrum are reproven in the runner.
`δ ≈ 2/9` and `cos(2/3) ≈ 0.786` appear **only** as the downstream comparator
(D7), never as an ingredient; the exhaustive natural-constant smuggle test
returns zero hits. Brannen, Koide, and APS are named as comparators/context, not
derivation inputs.
