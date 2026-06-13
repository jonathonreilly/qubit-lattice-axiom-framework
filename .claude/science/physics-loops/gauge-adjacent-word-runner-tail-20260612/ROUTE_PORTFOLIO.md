# Route Portfolio

## Route A - Patch the displayed verification tail

Disposition: selected. It directly matches the auditor request.

## Route B - Change runner counts

Disposition: rejected. The runner already passes `PASS=28 FAIL=0`; changing it
would be science churn and not the requested repair.

## Route C - Edit audit verdict

Disposition: forbidden for this branch. Independent audit owns row status.
