# No-Go Ledger

## NG-001: Expectation-only certificate

Route:

```text
expected post-record frequency
  => concentration certificate
```

Verdict: rejected.

Reason: exact finite laws can share expected counts and one-time marginals but
have different tail probabilities.

## NG-002: Wrong-law certificate transport

Route:

```text
iid certificate
  + different law with same expected counts
  => valid certificate
```

Verdict: rejected.

Reason: the runner verifies that the iid `epsilon=1/4` certificate is valid
when `P(event)=1/8`, but invalid under the correlated law where `P(event)=1`.

## NG-003: Stable location as p-value

Route:

```text
stable dial location
  => calibrated audit p-value
```

Verdict: rejected in this block.

Reason: stability needs a supplied score/rule/law; calibration needs a supplied
law or concentration theorem. Neither is supplied by Record alone.
