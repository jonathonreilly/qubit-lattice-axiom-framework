# Historic intake: Clean Derivation: R = Omega_DM/Omega_b = 5.48 from Cl(3) on Z^3

**Primary runner:** `scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py`


Date: 2026-08-05
Authority: none
Audit: unset
Claim type: bounded_theorem
Stratum: pre_seeding_mainline_deleted
Era: april_pre_reset — dated 2026-04-13; assumes axioms A1-A5 (Cl(3) on Z^3 with SU(3)xSU(2)xU(1) staggered fermions; a = l_Pl the unique scale)

Status: HISTORIC INTAKE under the 2026-08-05 owner directive (pull historic
science iff relevant and/or valuable; pulled items enter the ledger and are
audited). This wrapper registers a claim from the repo's unledgered history.
The wrapper asserts nothing beyond what the pinned original states; the
original's own scope, caveats and era conventions govern. Independent audit
required before any effective status.

## The claim (as stated by the original, supervisor-compressed)

A 13-step chain from Cl(3) on Z^3 gives the dark-matter-to-baryon ratio R = (3/5)*(155/27)*S_vis = 3.444 * 1.592 = 5.483 against R_obs = 0.268/0.049 = 5.469, a 0.25% deviation. The exact backbone is the taste decomposition 1+3+3+1 (Burnside on the Z_2^3 action), visible sector T_1+T_2 = 6 gauge-charged states versus dark sector S_0+S_3 = 2 gauge singlets, mass-squared ratio 9/15 = 3/5 from Hamming weights, and Casimir channel weighting 155/27; alpha_s = 0.0923, S_vis = 1.592, and x_F = 25 are derived.

## Corrigendum (2026-09-30)

Three parts of the claim above, as the original states them, are wrong. The pinned original is unchanged.

**1. `S_vis = 1.592` and `R = 5.483` at `alpha_s = 0.0923`.** The thermal kernel behind these numbers used the Sommerfeld factor `S = pi z / (1 - e^{-pi z})`, `z = alpha / v`, where `v` is the relative speed carried by the weight `v^2 e^{-x_f v^2 / 4}`. For a pair of reduced mass `m/2` the s-wave Coulomb factor from the radial Schroedinger equation (wave number `k = m v / 2`, Coulomb parameter `eta = alpha / v`) is `S = 2 pi z / (1 - e^{-2 pi z})`. The old form is the textbook formula written for the per-particle centre-of-mass speed `v/2`; at fixed relative speed it is the correct function at half the coupling, `S_pi(alpha) = S_2pi(alpha/2)`. With the corrected kernel `S_vis = 2.342`
and `R = 8.067` at `alpha_s = 0.0923` (`R = 7.972` at `alpha_LM = 0.09067`). The half-argument values `1.592` and
`5.483` are the corrected values at `alpha_s / 2`. The coupling that gives `R = 5.469` with the corrected kernel is
`0.0459`.

**2. `R_obs = 0.268 / 0.049 = 5.469`, "a 0.25% deviation".** The comparison values used in this lane (`5.469` from the rounded `0.268 / 0.049`, `5.47`, `5.375` / `5.38`, and `5.448` from `0.268` over the BBN `Omega_b`) are not the physical density ratio. The Planck-2018 physical densities, which cancel `h`, give `R_obs = (Omega_c h^2)/(Omega_b h^2) = 0.1200 / 0.02237 = 5.364 +/- 0.065` (`Omega_c h^2 = 0.1200 +/- 0.0012`, `Omega_b h^2 = 0.02237 +/- 0.00015`, TT,TE,EE+lowE+lensing; external comparator recalled from Planck 2018 results VI, not re-fetched; errors propagated as independent, the posterior correlation is not applied). Against that, the archived endpoint ratios `5.442` and `5.483` were `+1.5%` and `+2.2%` (`+1.2` and `+1.8` sigma) misses, not the `0.25%` agreement obtained against `5.469`. The runner comparator `5.4479` (`0.268` over the BBN `Omega_b` for `eta = 6.12e-10`) is itself `+1.6%` (`+1.3` sigma) above `5.364`.

**3. "dark sector `S_0 + S_3` = 2 gauge singlets".** In the base x fibre embedding the later mass step uses
(`CL3_COLOR_AUTOMORPHISM_THEOREM`), every taste state is a weak-doublet component and no taste state is a gauge
singlet (smallest eigenvalue of `C_3 + C_2` is `0.75`); `|000>` and `|111>` are colour fundamentals with `Y = +1/3`.
The April Steps 2-3 (Hamming-weight grading, `S_0` and `S_3` singlets) and the May mass step (`|111>` a colour
fundamental) use incompatible embeddings. The lane's other candidate, the lightest right-handed neutrino, decays in
about `3.5e-30 s` by its own note's washout parameter. This is conditional on the embedding, which is itself an
unaudited input. See `scripts/dm_dark_candidate_consistency_check.py`.

**Evidence.** `scripts/dm_sommerfeld_kernel_radial_schrodinger_verification.py` (radial Schroedinger equation integrated numerically with no closed form, mpmath Coulomb function, independent quadrature; it reproduces the archived numbers as the corrected ones at half the coupling) and `scripts/dm_ratio_comparator_planck_central_values_check.py`. Both are same-family checks by their author, not independent referees. No audit verdict, effective status or status field is changed by this corrigendum. The exact backbone (`1+3+3+1`, `3/5`, `155/27`, `R_base = 31/9`) is unaffected.

## Why pulled (supervisor triage decision of 2026-08-05, provenance not authority)

The reasons below are the supervisor's selection rationale; they carry no claim status and are not evidence about the original's validity.

R = 5.483 vs 5.469 (0.25%) via the 13-step chain, with the honest boundary: NOT zero-parameter (g_bare bounded import) — the DM flagship claim surface, priced by its own text.

## Provenance (pinned)

- Original path: `docs/DM_CLEAN_DERIVATION_NOTE.md`
- Source commit: `5205806e8a36f67603cf931a82941ef37c9fd739`
- git blob: `584c0059aa91ccc22a954e2195ff52906f308287`
- sha256: `fc122e8199ad0d276ac2788f49c2a11f252e89528f4b6decd7f4e2963cf96b45`
- Archived original (byte-exact, sha256-verified at generation): [../../archive_unlanded/historic_intake_originals/recovery/3594_DM_CLEAN_DERIVATION_NOTE.md](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/e69519ec7a37f19c096737dab2208de5ce15c192/archive_unlanded/historic_intake_originals/recovery/3594_DM_CLEAN_DERIVATION_NOTE.md)
- Lines: 412; runners named: historic runner (unpinned, not in this packet): `scripts/frontier_dm_clean_derivation​.py`
- Note: `.py` tokens in this wrapper's rendered fields are display-neutralized with a zero-width split for citation-graph hygiene (no current-tree runner may bind); the byte-exact original wording is pinned in the triage decisions/extraction JSONL files and in the archived original.

## Attached evidence (registered with, not as, this claim)

- `docs/DM_CLEAR_BLOCKER_NOTE_2026-04-14.md` — Blocker analysis (normalization-as-physical question).
- `docs/DM_DENOMINATOR_BLOCKER_NOTE_2026-04-14.md` — Self-superseded denominator blocker; CONTRADICTS any zero-import reading of R=5.48 — must ride the pull as adverse evidence.
- `docs/DM_DIRECT_OBSERVABLE_EXECUTION_NOTE_2026-04-14.md` — Workstream decision note; flags the authority mismatch inside the DM set.
- `docs/DM_DIRECT_OBSERVABLE_NOTE.md` — The strongest response (T-matrix route dissolves g_bare) — a reframing, self-stated; rides the pull.
- `docs/DM_NUMERATOR_DIRECT_OBSERVABLE_AUTHORITY_NOTE.md` — Numerator authority consolidation pointer.

## Cross-stratum flags (inert text; machine-readable relations in the audit fields)

- Cross-stratum reference from branch01 idx 237 (`docs/CODEX_DM_RESPONSE.md`, decision LEAVE) — DM objection scorecard: g_bare assumed + sigma_v imported STAND — adverse evidence for the DM flagship wrapper.
- Named non-pulled evidence (provenance only): idx 237 `docs/CODEX_DM_RESPONSE.md` — archived byte-exact at `archive_unlanded/historic_intake_originals/branch01/237_CODEX_DM_RESPONSE.md`, sha256 `bc84dda2f8587472dd73c463d0a17ebf32866ba28a0fae541028be571ebea643`

## Triage extraction notes (2026-08-05/08, not from the original)

Written at triage/extraction time; NOT part of the pinned original, carries no authority, and is input for the future auditor only.

- Extraction verdict (triage compression; may reflect later context): The DM lane is BOUNDED, not closed, and this is not a zero-parameter prediction because g_bare is a bounded input.
- Extraction scope (triage compression; may reflect later context): Step count is 4 EXACT, 7 DERIVED, 2 BOUNDED; two irreducible bounded inputs (g_bare = 1 from Cl(3) normalization, and spatial flatness k = 0) plus one observational input (eta = 6.12e-10, entering Omega_b only); the lattice spacing a = l_Pl is the unique physical scale with no continuum limit taken.
- Extraction escape conditions (negative claims; triage compression): The bounded steps name their escape conditions: g_bare = 1 is honestly bounded and the objection is conceded — the Cl(3) normalization makes g = 1 canonical but whether that is a constraint or a convention is foundational and it is NOT derived from a dynamical principle. The Stosszahlansatz objection is answered by two independent proofs on Z^3_L for the FREE massive field (spectral gap + Combes-Thomas + Wick, error < 1e-22000; direct matrix inversion, error < 1e-45000) with the caveat that the interacting-theory extension requires spectral gap persistence. k = 0 is observationally confirmed but not derived from the lattice, and is tied theoretically to S^3 compactification.
- Extraction red flags: Explicit NOT-claimed list, including that the DM lane is not closed and g_bare = 1 is not derived from a dynamical principle; the Stosszahlansatz proof covers only the free theory.
- Supersession (as known at extraction): Written as a response to a Codex objection map on three named objections (Boltzmann/Stosszahlansatz, radiation-era expansion bridge, g_bare normalization).

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
historic_claim_class: historic_bounded
intake_directive: owner_2026-08-05
cross_reference:
- "idx 237 (not pulled; branch01) docs/CODEX_DM_RESPONSE.md"
```

Independent audit still required.
