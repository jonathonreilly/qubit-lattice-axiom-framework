# Assumptions And Imports

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| Prior `I_1 = I_S` reduction | Defines the citation row's symbolic input | retained support | `logs/retained/yt_p1_i1_lattice_pt_symbolic_2026-04-17.log` | yes | yes | already exposed; this PR does not recertify it | preserved |
| `C_F = 4/3` color factor | Maps `I_S` to P1 arithmetic | retained support | `YT_P1_COLOR_FACTOR_RETENTION_NOTE_2026-04-17.md` and cache | yes | yes | already exposed; this PR does not recertify it | preserved |
| Literature bracket `I_S in [4,10]` | Conditional comparison arithmetic | supplied/literature comparator | `YT_P1_I_S_LATTICE_PT_CITATION_NOTE_2026-04-17.md` | no for quarantine; yes for the conditional arithmetic row | no for demotion | replace with a corrected native derivation or keep conditional | preserved as conditional only |
| Historical `I_S_native = 3.902` | Former native replacement route | unsupported import after correction | older native-BZ route text; current note records it as obsolete | no | yes, as a route to reject | retire by explicit quarantine | rejected |
| Corrected scalar `I_S ~ 32.4` | Evidence that old `3.902` route is invalid | computed lattice input | `frontier_yt_p1_bz_quadrature_full_staggered_pt.txt`; correction cache | yes | yes | already computed; future controlled matching must rederive full lane | used as quarantine evidence |
| Fermion regulator dependence | Evidence old Delta_R matching is uncontrolled | computed lattice input | `yt_p1_fermion_regulator_verification_memsafe.txt` | yes | yes | full-doubler controlled matching route | used as quarantine evidence |
| Canonical alpha certificate | Arithmetic constant for conditional map | retained/bounded support | `CANONICAL_PLAQUETTE_ALPHA_LM_VALUE_CERTIFICATE_BOUNDED_NOTE_2026-06-16.md` | yes for arithmetic checks | yes | parent plaquette surface remains separate | preserved |
