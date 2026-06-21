# Route Portfolio

| Route | Type | Dramatic-step score | Hard-residual pressure | Expected artifact | Decision |
|---|---|---:|---:|---|---|
| Register `diamond_sensor_prediction_note` with a bounded wrapper runner | exact runner / audit unblock | 3 | 1 | Runner metadata, wrapper, cache, generated row path | Selected |
| Register the existing prediction card printer directly | runner metadata only | 2 | 0 | Smaller diff, weaker gate | Rejected because the card printer has no assertions |
| Claim diamond/NV detectability | constructive theorem | 3 | 3 | Would need source-to-NV transfer and lab budget | Rejected: not supported by current surface |
| Bundle protocol, prediction, and signal-budget rows | aggregate runner | 2 | 1 | Larger PR touching multiple experiment cards | Deferred to keep this PR reviewable |

The selected route unblocks one high-priority bounded row while preserving the
open physical coupling and amplitude/noise bridges.
