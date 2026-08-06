# Historic intake: Clean Derivation: R = Omega_DM/Omega_b = 5.48 from Cl(3) on Z^3

Date: 2026-08-05
Authority: none
Audit: unset
Claim type: historic_bounded
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

Original verdict: The DM lane is BOUNDED, not closed, and this is not a zero-parameter prediction because g_bare is a bounded input.
Scope: Step count is 4 EXACT, 7 DERIVED, 2 BOUNDED; two irreducible bounded inputs (g_bare = 1 from Cl(3) normalization, and spatial flatness k = 0) plus one observational input (eta = 6.12e-10, entering Omega_b only); the lattice spacing a = l_Pl is the unique physical scale with no continuum limit taken.
Escape conditions (negative claims): The bounded steps name their escape conditions: g_bare = 1 is honestly bounded and the objection is conceded — the Cl(3) normalization makes g = 1 canonical but whether that is a constraint or a convention is foundational and it is NOT derived from a dynamical principle. The Stosszahlansatz objection is answered by two independent proofs on Z^3_L for the FREE massive field (spectral gap + Combes-Thomas + Wick, error < 1e-22000; direct matrix inversion, error < 1e-45000) with the caveat that the interacting-theory extension requires spectral gap persistence. k = 0 is observationally confirmed but not derived from the lattice, and is tied theoretically to S^3 compactification.

## Why pulled (supervisor decision, on the record)

R = 5.483 vs 5.469 (0.25%) via the 13-step chain, with the honest boundary: NOT zero-parameter (g_bare bounded import) — the DM flagship claim surface, priced by its own text.

## Provenance (pinned)

- Original path: `docs/DM_CLEAN_DERIVATION_NOTE.md`
- Source commit: `5205806e8a36f67603cf931a82941ef37c9fd739`
- git blob: `584c0059aa91ccc22a954e2195ff52906f308287`
- sha256: `fc122e8199ad0d276ac2788f49c2a11f252e89528f4b6decd7f4e2963cf96b45`
- Lines: 412; runners named: scripts/frontier_dm_clean_derivation.py

## Attached evidence (registered with, not as, this claim)

- `docs/DM_CLEAR_BLOCKER_NOTE_2026-04-14.md` — Blocker analysis (normalization-as-physical question).
- `docs/DM_DENOMINATOR_BLOCKER_NOTE_2026-04-14.md` — Self-superseded denominator blocker; CONTRADICTS any zero-import reading of R=5.48 — must ride the pull as adverse evidence.
- `docs/DM_DIRECT_OBSERVABLE_EXECUTION_NOTE_2026-04-14.md` — Workstream decision note; flags the authority mismatch inside the DM set.
- `docs/DM_DIRECT_OBSERVABLE_NOTE.md` — The strongest response (T-matrix route dissolves g_bare) — a reframing, self-stated; rides the pull.
- `docs/DM_NUMERATOR_DIRECT_OBSERVABLE_AUTHORITY_NOTE.md` — Numerator authority consolidation pointer.

## Cross-stratum flags

- Cross-stratum reference from branch01 idx 237 (`docs/CODEX_DM_RESPONSE.md`, decision LEAVE) — DM objection scorecard: g_bare assumed + sigma_v imported STAND — adverse evidence for the DM flagship wrapper.

## Flags carried

Explicit NOT-claimed list, including that the DM lane is not closed and g_bare = 1 is not derived from a dynamical principle; the Stosszahlansatz proof covers only the free theory.

## Audit fields

```yaml
audit_required_before_effective_retained: true
bare_retained_allowed: false
historic_intake: true
intake_directive: owner_2026-08-05
```

Independent audit still required.
