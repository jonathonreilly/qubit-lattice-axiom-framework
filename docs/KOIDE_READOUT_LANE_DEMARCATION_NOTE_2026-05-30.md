# Koide Readout-Lane Demarcation: the readout supplies the formula, not r=1/2

**Date:** 2026-05-30
**Claim type:** bounded_theorem / route-demarcation (positive negative)
**Status:** route diagnostic. Approves no axiom and no import; sets no audit
verdict. One sub-claim is admission-contingent (flagged below). The audit lane
sets status.
**Primary runner:**
`scripts/frontier_koide_readout_lane_demarcation_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_readout_lane_demarcation_2026_05_30.txt`.

## Question

The charged-lepton Koide value reduces (retained
`koide_circulant_q_two_thirds_algebraic`) to `Q=(1+2r)/3`, `r=|b|^2/a^2`, so
`Q=2/3 <=> r=1/2`, the `(1,1)` center / block-count isotype weight vs the `(1,2)`
dimension weight. The remaining internal handle (named in
`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30`, since a
continuous `U(1)_b` algebra symmetry is forbidden by the retained `C^3=I`) was a
**`Q`-readout-functional factorization** through the `SO(2)/U(1)_b` doublet
quotient.

Can the physical mass-**readout** — the procedure mapping the operator/state to
the observed lepton masses and hence `Q` — supply the `(1,1)` weight / `r=1/2`
itself, or does it only fix the formula `Q=(1+2r)/3` and leave `r=1/2` to the
dynamics (what sets the coupling ratio `b/a`)?

## What the native readout DOES settle (derived, not posited)

The native readout is forced: the retained-bounded real anti-Hermitian staggered
Dirac `D` (`cpt_exact_real_anti_hermitian_d`) gives the Hermitian lift `H=iD` =
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
   doublet-symmetric family `Z=(1,t,t)` is `theta`-independent only at `t=0`
   (collapse). Physical residues are unit (`H` normal => orthonormal eigenbasis,
   canonical wavefunction renormalization), giving exactly the democratic reading
   `Q=(1+2r)/3` with `r` free. No non-degenerate, 3-mass residue pattern supplies
   `r=1/2`.

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

This closes the readout as a route to `r=1/2`; it does not close the broader
search. It hands the dynamics/coupling-ratio lane a sharp, self-contained target:
derive the `F1` (equal-block) extremization over `F3` (dimension) on
`(E_+, E_perp) = (3a^2, 6|b|^2)`. Per the no-imports policy, no new reference
state or extremization principle is asserted here; the two retained no-gos
(`koide_frobenius_isotype_split_uniqueness`, `action_normalization`) continue to
decline to rank `(1,1)` vs `(1,2)`, and this note does not rank them — it shows
the **readout** is not where the ranking is supplied.

## Relation to Koide

`KOIDE_REAL_REP_BLOCK_COUNT_PERMITTED_NOT_FORCED_NOTE_2026-05-30` showed the
real-structure / measure side does not force `(1,1)`; this note shows the
**readout** side does not either (it supplies only the formula, `theta`-quotient
factorization, and the signed readout class). Together they localize the
Koide-value pin entirely to the dynamics question: what sets `b/a` such that
`r=1/2`.
