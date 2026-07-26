# Promotion Value Gate — Cycle 708

## Prior-art sweep

Ref refreshed; searched commit `70e8153ec2`. Searched on the statement:
`"two-sided inverse|inverse exists|invertib"`, `"(zero mode|constant
mode).*(invert|singular|inverse)"`, `"pseudo-?inverse|zero-mean|neutral
sector|dirichlet"`.

Classification of hits: `BELL_INEQUALITY_DERIVED_NOTE` — **prior art this note
depends on**, quoted as the repo's periodic convention ("graph Laplacian
pseudoinverse … excluding the zero mode"); `ACPHILAMBDA_CYCLE_FLUX_TRANSPORT`
— pseudoinverse on an `N=3` ring, different object; `VELOCITY_RG_…` — gauge
zero mode, different operator. **No landed note checks A2's stated proviso.**

## V1 — the claim

On any finite translation-covariant lattice `G_0 = H^{-1}` does not exist
(the constant is an exact kernel vector), so A2's stated two-sided-inverse
proviso cannot be met; under the repo's own periodic convention the identity
is unsatisfiable rather than merely unproven; and covariance — already
supplied by Admissibility — repairs it, forcing `A=0, B=-1` from the
zero-mean sector alone.

## V2 — new at `70e8153ec2`?

Yes. The proviso is written in the ledger's `verdict_rationale` and, per the
sweep, has never been tested. The cross-lane inconsistency between the gravity
row's "two-sided inverse" and the Bell lane's pseudoinverse is not recorded
anywhere.

## V3 — load-bearing?

On a `criticality: critical` root row (`deps: []`, 773 transitive
descendants). It does not close the row's `missing_bridge_theorem`, but it
changes what a derivation of A2 must do: name which `G_0` it means and on what
space. W3 upgrades the status of the identity under the implemented convention
from "underived" to "no solution".

## V4 — cost

No axiom, primitive, dimensionless import or convention. The repair (W5) uses
the landed covariant classification and Admissibility covariance, both already
framework content. Maradudin is cited only to **scope** W2 away from infinite
`Z^3`, not to support it.

## V5 — thin?

Defences: exact rational linear algebra throughout, including an explicitly
constructed pseudoinverse checked against `H·H⁺ = I − J/n`; two controls that
price the alternative repairs rather than only complaining; and a positive
result (W5) that closes the gap with existing framework content.

**Risks I would flag myself:** (1) the periodic zero mode is elementary and a
reviewer may call W1/W2 a known technicality — the non-obvious parts are W3
(unsatisfiable under the implemented convention) and W7 (the Dirichlet repair
contradicts a property the parent note *derives* from A2); (2) W2 does not
apply to infinite `Z^3`, which may be what the lane intends, and the note says
so in Scope; (3) W5 assumes membership in the range-1 covariant family.

## Step 11 — inference audit

`inference_audit_lint.py`: **clean**. Claim ledger complete, seven rows. Two
defects were caught during the cycle: a `pinv_annihilates_const = True`
hardcode (replaced by an explicit construction) and a prose claim about A2's
antecedent that no ledger row covered (W2 rewritten to state it). Running the
audit also exposed two bugs in the linter itself, both fixed on
`methodology/inference-audit-20260726`.

## Verdict

Proceed to cluster-cap evaluation. 7 PASS / 0 FAIL, cold-run at `c732a93612`,
PIN MATCH `e824f3df…`.
