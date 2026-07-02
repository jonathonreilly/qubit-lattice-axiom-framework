# No-Go Ledger

| Route | Result | Scope | Artifact | Reopen Condition |
|---|---|---|---|---|
| E-center-blind endpoint class derives target endpoint | no-go | E-center-blind primitives cannot distinguish the needed nonblind center information | `docs/QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md` | Supply a nonblind source/readout primitive |
| Color-only typed magnitude bridge | no-go | Current color-only/E-center-blind primitives do not derive `|center T/E| = R_conn` | block53 PR | Supply typed nonblind bridge data |
| Single measured `SIZE=15` calibration implies exact limit | no-go | One finite-box datum cannot identify an infinite-volume limit | block55 note and runner | Supply box-size scan, convergence theorem, or independent source theorem |

## Block55 Boundary

The block55 no-go must not be read as a no-go for measured calibration itself.
It only rejects exactification from one finite-box point.

