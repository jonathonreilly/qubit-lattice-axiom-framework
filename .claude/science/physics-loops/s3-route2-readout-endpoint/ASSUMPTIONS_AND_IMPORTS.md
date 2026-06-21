# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Restricted Route-2 carrier columns | Exact basis for E/T shell and center columns | framework-derived | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already supplied by parent note and runner | imported as exact parent surface |
| Readout family `P(rho_E)` | Determines which carrier directions see unresolved E-center entry | framework-derived with one open parameter | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | E-center/source/readout theorem | used only for dependency classification |
| T-side entries | Permit the reduced two-row family used by current notes | conditional parent surface | Route-2 endpoint notes | yes | yes | separate positive theorem or admitted parent condition | granted as parent context, not newly claimed |
| `Lambda_R` and `V_R(t)` | Safe time-channel consumers | framework-derived | `QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md` | yes | yes | already supplied by parent note | safe direct consumer |
| Factor-rigidity theorem | Localizes ambiguity in spatial prefactor | exact support | `S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md` | yes | yes | already supplied by parent note | used as source anchor |
| E-center blindness no-go | Proves blind constraints cannot see the missing direction | exact negative boundary | `QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md` | yes | yes | positive E-center rule | used to guard dependent consumers |
| Physical readout primitive | Needed for final physical use | open import | none on current branch | no for this block | no | source-domain theorem, bridge, or explicit convention | remains open |

No endpoint value is used as proof input in this block. The comparison with
`rho_E = 21/4` is only a classifier showing which columns change when the
unresolved parameter changes.
