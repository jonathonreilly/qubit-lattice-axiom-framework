---
claim_id: koide_readout_lane_demarcation_note_2026-05-30
claim_type_author_hint: no_go
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Koide Readout-Lane Demarcation: the readout supplies the formula, not r=1/2

**Date:** 2026-05-30
**Claim type:** no_go / narrow route-demarcation.
**Status authority:** independent audit lane only. This source note adds no
axiom and no import, and it sets no audit outcome. One sub-claim is
admission-contingent and is explicitly non-load-bearing.
**Primary runner:**
`scripts/frontier_koide_readout_lane_demarcation_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_readout_lane_demarcation_2026_05_30.txt`.

## Question

The charged-lepton Koide value reduces
([`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md))
to `Q=(1+2r)/3`, `r=|b|^2/a^2`, so
`Q=2/3 <=> r=1/2`, the `(1,1)` center / block-count isotype weight vs the `(1,2)`
dimension weight. The remaining internal handle (named in
[`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md`](KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30.md),
since a continuous `U(1)_b` algebra symmetry is forbidden by the retained
`C^3=I` boundary) was a
**`Q`-readout-functional factorization** through the `SO(2)/U(1)_b` doublet
quotient.

Can the physical mass-**readout** — the procedure mapping the operator/state to
the observed lepton masses and hence `Q` — supply the `(1,1)` weight / `r=1/2`
itself, or does it only fix the formula `Q=(1+2r)/3` and leave `r=1/2` to the
dynamics (what sets the coupling ratio `b/a`)?

## What the native readout DOES settle (derived, not posited)

The native readout is forced: the retained-grade bounded real anti-Hermitian
staggered Dirac `D`
([`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md))
gives the Hermitian lift `H=iD` =
the `C_3` circulant `aI + bC + conj(b)C^2`, hence a real **signed** spectrum
`lam_k = a + 2|b| cos(theta + 2 pi k/3)` (the Brannen / `det_R` reading,
`sqrt(m_k) = lam_k`, `m_k = lam_k^2`), fed into the standard 3-mass Koide
functional. With unit (canonical) spectral residues it supplies:

1. **the formula** `Q = (1+2r)/3` (`r=|b|^2/a^2`);
2. **`theta`-independence** — the readout factors through the `SO(2)`/`arg(b)`
   phase quotient at the formula level (root-of-unity sums `sum cos = 0`,
   `sum cos^2 = 3/2` kill all `theta`);
3. **the readout class** — among native readings only the signed/Hermitian
   (`det_R`) one is comparator-compatible; the singular-value/Yukawa reading is
   `theta`-dependent and `<= (1+2r)/3` (it drops once an eigenvalue goes
   negative).

## What it does NOT settle: r=1/2 (proven three ways)

`r=1/2` was tested as a hypothesis, never assumed.

1. **No readout stationarity.** `dQ/dr = 2/3` identically (linear, monotone);
   `r=1/2` is an ordinary interior point, indistinguishable to the readout from
   any other `r`.

2. **The residue degree of freedom is exhausted.** Allowing arbitrary spectral /
   pole-residue weights `(Z_0, Z_1, Z_2)` in
   `Q = (sum Z_k lam_k^2) / (sum Z_k lam_k)^2`, the only weights that make `Q`
   both `r`-independent and equal to `2/3` are **single-pole collapses** (two of
   the three `Z` zero) — which destroy the three distinct physical masses. The
   doublet-symmetric family `Z=(1,t,t)` has two theta-independent endpoints:
   `t=0` is a single-pole collapse (`Q=1`, mass loss), while `t=1` is the
   physical unit-residue/democratic branch. The `t=1` branch gives exactly
   `Q=(1+2r)/3` with `r` free; it is not an `r`-independent `2/3` selector.
   Non-endpoint choices such as `t=1/2` remain `theta`/`r` dependent. No
   non-degenerate, nonunit, 3-mass residue pattern supplies `r=1/2`.

3. **The measurement weight lands on `(1,2) -> Q=1`.** Einselection picks the
   pointer basis = eigenbasis of `H`; the Born weight of each pointer state under
   the tracial pre-record reference `rho = I/3` is uniform `p_k = 1/3` (trace
   unitarily invariant), i.e. block-resolved `(singlet, doublet) = (1/3, 2/3)` =
   the **dimension / Plancherel `(1,2)`** weight, `r=1`, `Q=1`. So the measurement
   readout, far from supplying `r=1/2`, actively lands on `Q=1`.
   **Admission-contingent:** this sub-claim depends on identifying the physical
   pre-record reference state with the tracial `rho=I/3`, which is a demoted open
   admission, not theorem-strength. It is included as a convergence indicator
   (it matches the independent "measure & trace -> Q=1" findings), not a proof.

## Demarcation (the result)

The `(1,1)` weight that yields `r=1/2` lives only in the choice to extremize
`F1 = log E_+ + log E_perp` (extremum at `r=1/2`) over the equally legitimate
`F3 = log E_+ + 2 log E_perp` (extremum at `r=1`), where
`E_+ = 3a^2`, `E_perp = 6|b|^2` are the two `C_3` block energies. Both are
functions of the same readout `sqrt`-mass vector; **the readout procedure selects
neither.** That `F1`-vs-`F3` selection is the `(1,1)`-vs-`(1,2)` weight question,
and it is a property of what physically sets the coupling ratio `b/a` — i.e. the
**dynamics** lane, not the readout.

## Boundary

This closes only the tested native readout route to `r=1/2`; it does not close
the broader search. It hands the dynamics/coupling-ratio lane a sharp,
self-contained target:
derive the `F1` (equal-block) extremization over `F3` (dimension) on
`(E_+, E_perp) = (3a^2, 6|b|^2)`. Per the no-imports policy, no new reference
state or extremization principle is asserted here; the two retained no-gos
([`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`](KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md),
[`ACTION_NORMALIZATION_NOTE.md`](ACTION_NORMALIZATION_NOTE.md)) continue to
decline to rank `(1,1)` vs `(1,2)`, and this note does not rank them — it shows
the **readout** is not where the ranking is supplied.

## Relation to Koide

`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30` showed the
real-structure / measure side does not force `(1,1)`; this note shows the
**readout** side does not either (it supplies only the formula, `theta`-quotient
factorization, and the signed readout class). Together they localize the
Koide-value pin entirely to the dynamics question: what sets `b/a` such that
`r=1/2`.

## No-Go Discipline Gate (N1-N8)

**N1 — Alternative route enumeration.** Five readout-side routes were checked:
(1) unit spectral residues give `Q=(1+2r)/3` and `dQ/dr=2/3`, so no readout
stationarity selects `r=1/2`; (2) arbitrary non-degenerate spectral residues do
not make `Q` `r`-independent, except mass-losing single-pole collapse; (3) the
center-mimicking residue `Z=(1,1/2,1/2)` remains `theta`/`r` dependent and does
not pin `2/3`; (4) the tracial pre-record route, if admitted, gives the
dimension `(1,2)` weight and `Q=1`, not `2/3`; (5) readout-derived block
energies allow both `F1` and `F3`, so the readout itself supplies no rule
selecting equal-block over dimension weighting.

**N2 — Wall-independence audit.** The raw walls collapse to one residual:
native readout supplies the formula/readout class but no block-weight selection
principle. Closing the tracial-reference admission would not close the
`F1`-vs-`F3` selection; finding a dynamics principle for `F1` would close the
target without changing the readout no-go.

**N3 — Hidden-wall scan.** "Native" is grounded in the cited real
anti-Hermitian `D` and signed/Hermitian readout surface. "Unit residues" relies
on normality/orthonormal spectral projectors for the Hermitian lift. "Tracial
pre-record reference" is an explicit admission-contingent convergence check and
is not load-bearing for the no-go.

**N4 — Residual matching.** The real-representation block-count note attacks
the measure/real-structure residual, not readout; this note attacks only the
readout residual. The Frobenius-isotype and action-normalization no-go rows are
cited only for the already-known absence of an in-repo ranking principle between
`(1,1)` and `(1,2)`.

**N5 — Rhetoric audit.** "Readout does not supply `r=1/2`" means the tested
native signed/Hermitian mass readout, spectral-residue variations, and
tracial-reference measurement check. It does not mean no dynamics, coupling, or
future pole-residue theorem can supply `r=1/2`.

**N6 — Partial-closure path scan.** A future source-reference theorem,
pole-residue certificate, or dynamics extremization principle could still pick
`F1`. This note does not require a new axiom and does not foreclose import
retirement through a later bounded theorem.

**N7 — Steelman.** A hostile reviewer could argue that physical residues are
not exhausted by the simple spectral weights tested here: a future transfer or
source-response theorem might derive nontrivial pole residues or a reference
state that effectively selects `F1` while remaining native. This note leaves
that path open and assigns it to the dynamics/evidence lane.

**N8 — Cross-cycle echo.** The same `(1,1)` vs `(1,2)` wall appears in the
real-representation block-count note and in the retained no-go rows cited
above. Those rows have not been retired by a convention reframe; this note keeps
the wall narrow and does not re-label it as an axiom gap.
