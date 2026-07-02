# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Route-2 endpoint algebra | Converts E-excess to `rho_E`, `q_E`, and `c_TE` | exact support | `QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md` | yes | yes | already present | used |
| SU(3) adjoint dimension `8` | Supplies the eight-dimensional projector space | exact support | Rconn/Fierz support bank | yes | yes for this route | already present as support | used |
| Single typed adjoint line | Selects a codimension-one complement | unsupported import / conditional primitive | block37 hypothesis | yes | yes | derive from source geometry or reject | open |
| Complement-rank E-center readout | Reads `e_E=7/8` from the selected line's complement | unsupported import / conditional primitive | block37 hypothesis | yes | yes | derive a readout-map theorem or reject | open |
| Comparator endpoint `21/4` | Used to verify consequence and uniqueness | comparator from open gate | `S3_TIME_PRIMITIVE_CHAIN_NOTE.md` | no proof input | no | keep comparator-only | guarded |
| Current typed source bank absence | Keeps actual status conditional | exact negative boundary | source-domain and E-center blindness notes | yes | yes | derive missing selector | still binding |
