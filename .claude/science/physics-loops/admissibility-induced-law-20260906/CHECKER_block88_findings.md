# Block 88 — control and findings (2026-09-22)

1. Disjoint machinery (`specs/supervisor_control_block88_two_instabilities.py`): floating-point spectra on rings and zone sums; the runner is symbolic.
2. **A normalisation artefact removed (supervisor).** The raw second-order response to `cos(qx)` jumps by a factor two at `q = π`; per unit modulation power (½ for a cosine, 1 for the alternation and a uniform shift) it is continuous. All comparisons are per unit power.
3. **First-order cancellation made symbolic**: the anisotropy's first-order integrand's cyclic images sum to zero; the direct first difference on `32³` is `2·10⁻⁵`.
4. **A sign error caught by the runner's own check**: a first draft asserted the cost's second derivative was `−α cos q`; it is `α cos q`.
5. **Endpoint property executed, not proved**: `0` of `301` values of `α` give an interior maximiser of the single-axis balance.
6. Finding: the anisotropy's threshold `β = χ_a/72` is `α`-free — only the perpendicular coupling keeps the lattice isotropic — while the alternation's is `α + 2β = χ/12`; the single-axis race between them is decided by `α = 0.076`.
7. **Corrigendum (2026-09-23, supervisor; block 89, PR #8678).** The balances wrote the rates as linear in block 59's variable; at the law's own unit (mean log rate) the thresholds are `α + 2β < 0.228` and `β < (χ_a + 2⟨|s|⟩)/72 = 0.059`. Text-only qualifiers added; no theorem, check or number changed.
