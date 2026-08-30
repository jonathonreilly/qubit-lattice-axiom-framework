# Block21 controlling preregistration pin

The controlling corrected preregistration commit is
`d20a49e1a875aa45c1fad810f21cda914fdb45d1`. The initial trace commit is
`6fdaadd635a1c1004ccbb8e78fa208531943ba2c`.

The target runner must verify these SHA-256 values before executing science:

| packet artifact | SHA-256 |
|---|---|
| `GOAL.md` | `0e13ed4944ce6bae842484a349d67a6515eaa86391122a6708675921208a1ef9` |
| `AUTHORITY_GATE.md` | `d2f004885d7d3d6a6657762f3cd3739558c46a6271c775e8ee1afe3c796aee17` |
| `PREFLIGHT_WITNESSES.md` | `00cda1aec2794ec3e4d15072a869524f8c4d38cf1de77f071f661a24dab0a0c0` |
| `INDEPENDENT_PREREG_ATTACK.md` | `510c3b2e6d2194ada43046c4e933e0c619e8410a08e2c26e293c2440e60c49c5` |
| `APPROACH_REGISTRY.md` | `b653f914a4dda4608688998b99ea37549f8c0f760ee4bade7d35f7cb33cd094e` |
| `PANEL_RETURN.md` | `9e82303ccff75899ae4b004be1be49ebabe583e02c419140a5339d6342e018ee` |
| `NO_GO_DISCIPLINE_CHECKLIST.md` | `b8597fe431429ab357be096a2e7e43e3458ba25d4f4572c989f9a0ca5c44e321` |
| `PREFLIGHT_SUPPORT_CORRECTION.md` | `6a1b354941c1c289643256fd6a135c39e47c4a8cfa981b13227ccfc962120756` |

No Block21 target runner or cache existed at either preregistration commit.
Any mismatch is a hard failure; do not regenerate expectations from edited
packet text.
