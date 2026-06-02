# Flavor — the doublet field-space metric, computed: Axiom 1's coherent-state metric is reading-neutral diag(3,6,6); the A1 default is det_R → r=1 → Q=1 (maximal hierarchy); r=1/2 (Q=2/3) needs a complex structure J on b that A1 doesn't supply and whose continuous form is the forbidden U(1)_b

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** positive determination (the A1 default mode-count) + a sharp open residual. Not a closure of r=1/2.
**Runner:** `scripts/flavor_doublet_metric_default_is_detR_2026_06_02.py` (SCORECARD 6/6).
**Source:** workflow `wf_eaa42dc4` — 5 compute routes + 3-lens adversarial verification + synthesis (18 agents).

## The calculation
The panel (`wf_9028152c`) reduced the charged-lepton lane to a single binary: is the C₃ doublet
coefficient `b` **one complex mode** (det_C → `r=1/2` → `Q=2/3`) or **two real modes** (det_R → `r=1` →
`Q=1`)? This derives the field-space metric on the mass-operator coefficients from Axiom 1's qubit
coherent-state resolution-of-identity, restricted to the hw=1 C₃ orbit, to decide it.

## Result: the A1 default is det_R → r=1 → Q=1 (and the metric alone can't decide)

### The metric is reading-NEUTRAL — diag(3,6,6)
The induced coherent-state / Hilbert-Schmidt metric on `(a, Re b, Im b)` is exactly **diag(3,6,6)**
(verified M1): `{I, C, C²}` are HS-orthogonal, each norm² = 3, so the doublet line element is
`6(dRe b² + dIm b²) = 6|db|²`. This is **simultaneously** "two real modes" and "one complex mode" — the
metric *value* cannot adjudicate `r=1` vs `r=1/2`. The decision lives entirely in the **mode-count**
(whether one equips the doublet plane with a complex structure J), a polarization choice *on top of* the
metric, not a metric invariant.

### Axiom 1's default mode-count is REAL (det_R)
A1 natively supplies the **Hilbert-Schmidt trace pairing** as the canonical operator metric (from the
resolution of identity). It is a **real** bilinear form on the Hermitian algebra: it presents the two
doublet deformations `C+C²` and `i(C−C²)` as **two independent, HS-orthogonal, equal-norm (=6) real
Hermitian directions**. Nothing in A1 + HS + Hermiticity fuses them into one complex mode. Equal power
per real dimension → `3a² = 6(Re b)² = 6(Im b)²` → `|b|²=a²` → **`r=1` → `Q=1`** (verified M3). The
no-extra-structure default is **maximal hierarchy** — one heavy + two (near-)massless — *not* democratic,
*not* 2/3. (Surprising, and specific.)

### Why r=1/2 (Q=2/3, the observed value) needs an imported J — and the obvious J is forbidden
Reaching det_C requires a complex structure J fusing `(Re b, Im b)` into one complex mode `b` (with
`δ=arg b` a Kähler/gauge fiber). Two independent obstructions (verified):
- **Descent no-go (M2):** the map `b ↦ H_lin(b) = bC + conj(b)C²` is **real-linear but not
  complex-linear** (`‖H_lin(ib) − i·H_lin(b)‖ = 3.46 ≠ 0`), forced by Hermiticity (the operator contains
  *both* `b` and `conj b`). Multiplication-by-i (the candidate J) sends Hermitian → anti-Hermitian, so it
  is **not an endomorphism of the observable algebra**. Axiom 1's CP¹ Fubini-Study J lives on the *intra-site*
  state coordinate `z`; `b` is the *inter-site* generation Fourier coefficient — a different tensor
  factor. The qubit's J does **not** descend to `b`.
- **C³=I forbids the only continuous J (M6):** a continuous doublet rephasing `C → e^{iα}C` requires
  `α ∈ {0, 2π/3, 4π/3}` (discrete C₃), so the continuous U(1)_b that would make `b` a single gauge-phase
  mode is forbidden. Hence det_C's required J is **both** undescended-from-A1 **and** continuous-forbidden.

Consistently, **δ = arg b is physical** under the A1 default (M5): individual masses `m_k` depend on δ
(spectrum-observable), as they must when there is no U(1)_b to gauge it. (δ would be a gauge/Kähler fiber
only in the det_C reading.)

### Honest scope caveat (the one verification refutation)
The descent no-go is an *operator/symbol-level* statement; the binary was posed at the *field-space
kinetic-metric* level, and operator-level real-linearity is consistent with a holomorphic kinetic term
too. So the descent no-go alone does not *prove* det_R at the kinetic level — but the kinetic level is
then settled by the **metric-neutrality** (det_C needs J as a named ingredient) **plus** the U(1)_b
prohibition. Across *both* venues the conclusion is identical: A1 alone delivers the real metric; the
holomorphic polarization is an unforced, and as-continuous forbidden, extra ingredient. (A pro-det_C
route — "`b` is the doublet Fourier mode of a *holomorphic* amplitude `f`" — was caught as a tautology
that posits a single global J phase-locked across the orbit, never deriving it from the three independent
per-site qubit J's: a textbook wrong-escape-via-citation, refuted 3/3.)

## Net standing
The charged-lepton lane now reduces to **one sharp open question**: *a complex structure J on the
generation-doublet coefficient `b` that (a) does not reduce to the forbidden continuous U(1)_b and (b)
genuinely descends from A1.* Axiom 1's coherent-state structure answers the default — **two real modes, det_R,
`r=1`, `Q=1` (maximal hierarchy)** — and `r=1/2` (`Q=2/3`) is **not closed**; it is exactly this J.

## Relation to prior work (attribution)
The lane parametrization itself is **not novel**: the `(scale a, ratio |b|, phase δ)` circulant
decomposition and the `Q ∈ [1/3, 1]` range (1/3 democratic, 1 hierarchical, 2/3 the midpoint) are Koide's
own **Z₃-symmetric parametrization** (Koide & Nishiura, arXiv:1301.4143), with different sectors at
different ratio values; Brannen's circulant density-matrix work is the parallel thread. Those
phenomenological frameworks leave the per-sector ratio a **free fit** (they do not derive why charged
leptons sit at Q=2/3). The framework's contribution is (i) the **axioms-up derivation** of that circulant
lane structure (carrier = hw=1 BZ corners from the spectral theorem; circulant from C₃-equivariance), and
(ii) **this determination of the default mode-count** (det_R → Q=1), which the phenomenological fits do
not address. The open residual (the J on `b`) is the genuine research frontier — open for everyone, not
just this framework.

## Provenance (verified 2026-06-02)
- Metric diag(3,6,6), descent no-go, det_R/det_C → r=1/r=1/2, δ-physicality: verified directly (runner 6/6).
- C³=I forbids continuous U(1)_b: prior retained result (the order-3 relation quantizes the rephasing).
- Lane parametrization attribution: Koide & Nishiura arXiv:1301.4143; Brannen circulant density-matrix.
- Does not load-bear on `closure_c_staggered_dirac_gate` / `koide_phase_aps_eta_parity_route`.
