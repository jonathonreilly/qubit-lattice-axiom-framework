# Goal

Repair the missing derivation in
`docs/CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md` from the
minimal current framework surface. The current-cycle target follows the
2026-07-25 independent-audit instruction: retain the exact local algebra and
shared-transport theorem, and remove the unsupported exhaustive route-closure
claim.

## Exact target contract

| Field | Contract |
|---|---|
| Target statement | For positive `R_pred`, `R_common`, `T_pred`, and `T_obs`, prove `1+D(T_pred,T_obs)=(T_pred/T_obs)[1+D(1,1)]`; recover exact deviation invariance for `T_pred=T_obs`. Preserve the already exact rank-`1+5` determinant/Casimir and fixed-spectrum countermodel results. |
| Quantifiers/domain | All four transport-law scalars are strictly positive; the determinant scalar is positive; the projector ranks and `T_F=1/2` normalization are explicit conditions. |
| Allowed premises | Elementary real algebra, finite-dimensional determinant/spectrum identities, and the two registered foundation notes used only to delimit framework content. |
| Forbidden weakenings | No observed mass, fitted exponent, selected scale, or QCD transport literal may become a proof input. No global scale-route closure may be inferred from the shared-scalar theorem. |
| Required edge cases | Unequal positive transports, the shared-transport specialization, and the historical crossed specialization `T_pred=1`, `T_obs=T`. Zero or negative transports are outside the physical ratio domain and are not silently included. |
| Completion witness | Symbolic runner checks the two-sided law, its factored deviation shift, both specializations, and all retained local algebra; canonical runner cache is fresh. |
| Outcomes that do not count as closure | A theorem deriving the physical `m_s/m_b -> |V_cb|` bridge, a unique `2 GeV` selector, or exhaustive classification of non-shared/nonmultiplicative evolution. Those remain outside this bounded theorem. |
