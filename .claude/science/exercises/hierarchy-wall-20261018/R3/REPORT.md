I read four documents in full before reaching any conclusion: `docs/MINIMAL_AXIOMS_2026-06-29.md`, `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md`, `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`, and `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`, which matters for this route. I read all of `docs/audit/data/derivation_obligations.json`. It has three entries (AC occupancy grain, AC R-η readout, θ determinant) and none of them concerns the hierarchy.

## Plain answer

The framework's laws contain no large number. Z³ is infinite and has no scale, each site has two states, and the rule is nearest-neighbour.

The only large numbers available are counts of history: ticks since the start, or sites, records or events inside a horizon. None of these is law output, for two reasons:

- **They are history data.** Records form, but no site or rate of formation is supplied, so different admissible histories have different counts. The realized-state primitive classes any value that would change under another admissible history as registered data, not derivation.
- **They keep growing.** Records are permanent, so counts in a growing causal region only rise.

Tying v/M_Pl to a growing count fails badly. Today v would drift about 10⁵ times faster than atomic clocks allow, and at nucleosynthesis v would have been about 7×10⁴ times its present value.

A frozen count escapes the drift but is still registered data. The best frozen candidate is the de Sitter radius R_Λ/a ≈ 10⁶¹. It would fix Λ and v together, which merges this wall into the open Lane 5 number rather than removing an input.

## Prior art (checked by grep on origin/main)

None of the 63 HIERARCHY notes uses a count, cosmological history, holography, a Dvali-type species bound or a swampland argument. There are zero hits for Dirac's large-number hypothesis, swampland, Festina Lente, Nnaturalness or relaxion. Related notes, none of which is my result:

- **Species count as exponent:** `HIERARCHY_ALPHA_LM_EXPONENT_SPECIES_COUNT_BRIDGE_REGULATOR_DEPENDENCE_NO_GO_NOTE_2026-05-10.md`. This treats 16 = 2⁴ as an exponent, not as a cutoff bound.
- **Lane 5:** `HUBBLE_LANE5_COSMIC_HISTORY_RATIO_NECESSITY_NO_GO_NOTE_2026-04-26.md` shows R_Λ/a is not derived from the baseline.
- **S³ identity:** `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md` gives Λ = 3/R² (conditional) and leaves R open.

## Route 1: the growing count (Dirac's large number, records version)

**Object.** Any count N(t): ticks t/t_P, sites inside the particle horizon, horizon area/4, or lattice events in the causal past. The hypothesis is v/M_Pl = F(N).

**Lemma A (proved, elementary).**
- In general, d ln(v/M_Pl)/dt = e · d ln N/dt, where e = d ln F/d ln N.
- For a power law fitted to today's value, e = −ln(M_Pl/v)/ln N₀.
- If N ∝ t^k starting from N(t_P) ≈ 1, then |drift| = ln(M_Pl/v)/(t₀ ln(t₀/t_P)) = 1.99×10⁻¹¹/yr, whatever the values of k and p.

**Lemma B (proved).** Suppose the count freezes at the epoch v itself sets, in the radiation era: N = c(M_Pl/T*)^k with T* = c′v. Then (v/M_Pl)^{1−kp} = c^{−p}c′^{kp}. This is O(1) unless kp is tuned to within about 1/38 of 1. Freezing at the weak epoch therefore supplies no large number.

**Number it would fix:** v/M_Pl. It is not supplied, for the history-data and growth reasons above.

**Test (checked, run).** I used a ΛCDM background (H₀ = 67.4, Ω_m = 0.315). Comparator bounds, taken conservatively: |μ̇/μ| < 10⁻¹⁶/yr from clocks, and |Ġ/G| < 1.5×10⁻¹³/yr from lunar laser ranging. The mapping d ln μ/d ln v = −7/9 is the one-loop threshold estimate.

| Count | log₁₀N₀ | drift of v (/yr) | × clock bound | × LLR bound | v_BBN/v₀ |
|---|---|---|---|---|---|
| ticks | 60.9 | −2.0e-11 | 1.6e5 | 59 | 6.8e4 |
| horizon sites | 184.9 | −2.5e-11 | 1.9e5 | 73 | 6.9e4 |
| horizon area/4 | 122.4 | −8.9e-12 | 6.9e4 | 26 | 5.5e4 |
| causal-past events | 242.8 | −1.9e-11 | 1.5e5 | 55 | 6.9e4 |

At recombination v would be 16–19 times its present value. The present elasticity allowed is e ≤ 0.5–2×10⁻⁶. At constant elasticity, a count can carry at most about 1.5×10⁻⁵ of ln(M_Pl/v).

The same kill covers transport-over-the-age variants (suggested). For example, coarsening with L ∝ t^{1/4} lands near the weak scale today but drifts at 1/(4t).

- **Strongest objection:** F could saturate. Lemma B and the realized-state rule answer it.
- **Kill condition:** met for every growing count. The route revives only if someone finds a count that is fixed by the law, independent of time, and at least 10³³.

## Route 2: the frozen patch capacity (holographic quarter-power law)

**Object.** R_Λ/a = 1.03×10⁶¹, where S_dS = 3.3×10¹²² and the S³ of that radius holds 2×10¹⁸⁴ sites. The proposed law is v = κ M_Pl (a/R_Λ)^s. At s = 1/4 this reads v⁴ ≈ κ⁴ M_Pl³ H_Λ: one Planck mass per horizon pixel, spread over the patch.

**Fit (checked).** s* = 0.265–0.279 and κ(s = 1/4) = 0.02–0.12, depending on convention (M_Pl or reduced M_Pl; v or m_h). Λ is constant, so this law does not drift.

**Lemma C (proved, given the 4D scalar unitarity bound Δ ≥ 1; Mack 1977 as template).**
- Take a local, reflection-positive mechanism whose only infrared scale is the patch size or the horizon temperature. Then ⟨O⟩ ∝ a^{−d_O}(a/L)^Δ, so v ∝ M_Pl(a/L)^{Δ/d_O}.
- The fit then requires Δ = d_O · s*.
- An order parameter of dimension 1, 2 or 3 would need Δ = 0.27, 0.55 or 0.82. All three violate the bound.
- A dimension-4 density needs Δ ≈ 1.06–1.12. That is allowed, but only just above the free-field value.
- The version with κ = 1 and Δ = 1 predicts H_Λ = v⁴/M_Pl³ = 2.0×10⁻⁴⁸ GeV, against 1.19×10⁻⁴² GeV observed. It is excluded by a factor of 6×10⁵ (checked).

**Comparator template.** This law is the same as ADD with two compact dimensions of radius about Λ^{−1/4}. Equivalently, it is a species bound with N ≈ (M_Pl/v)² Kaluza–Klein species. The framework has no extra dimensions.

**Why it is not supplied.** Z³ is infinite, and no Λ, horizon or time metric is derived. Lane 5 already records R_Λ/a as underived.

- **Strongest objection:** it trades 10¹⁷ for 10⁶¹. With s and κ free, it is a one-point fit.
- **Kill condition:** the route is dead if no framework operator of dimension 4 has an infrared one-point exponent Δ ∈ [1.06, 1.12], or if a non-relativistic sector evading unitarity is the only way in. It is also dead if the framework derives R_Λ/a and the fit fails.
- **Cheapest next test:** measure finite-size one-point exponents of the framework's gapless sectors. My suggestion, not yet checked: the diffusive "massless odds field" gives the half-power scale (M_Pl H)^{1/2} ≈ meV, not v.

## Side checks

- **Species bound.** It needs N = (M_Pl/v)² = 2.5×10³³ species, or 9.8×10³¹ with the reduced Planck mass. A free nearest-neighbour rule with one two-state site per cell gives at most 32 species: 2⁴ doublers times 2 bands (checked against the 2^d theorem on main). An interacting rule would need a cell enlarged to at least 10³³ sites, about 10¹¹ a across, and that is itself a hierarchy (suggested).
- **Swampland (comparator).** The weak gravity conjecture needs g ~ 10⁻¹⁷, which is an extra small number. Festina Lente gives only a lower bound at the half-power scale (about meV). These conjectures set bounds; they do not fix values.

## Net for the wall

Proved within the counting class: no record, qubit or tick count can be derivation output for v/M_Pl, and every count that is still growing is ruled out by observation. The extra number this class cannot avoid is one frozen cosmological number. The cheapest is R_Λ/a, which is already open in Lane 5.

This is not a general proof that the hierarchy needs an extra number. Law-level exponentiation routes, such as α_LM¹⁶, lie outside this class.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/R3/`:
- `count_route_test.py`
- `count_route_test.out`

The run peaked at 115 MB. No processes are left running.