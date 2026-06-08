# Goal

Repair the conditional audit blocker on
`gauge_vacuum_plaquette_tensor_transfer_perron_solve_note` without adding an
axiom, changing audit results, or claiming the physical plaquette value.

The concrete blocker was an imported finite Schur `L_s=2` value. The repair
must make that finite calculation source-visible and executable in the
primary gauge runner itself.
