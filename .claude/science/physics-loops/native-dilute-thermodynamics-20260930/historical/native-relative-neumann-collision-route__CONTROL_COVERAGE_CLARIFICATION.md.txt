# Frozen finite-control coverage clarification

The independent boundary checker identified a precise fixture-label limit.
check_boundary_pins.py counts837 complete S rows on the5^3 fixture because
it requires all four plane words to be present before retaining any of that
plane family's differences. The actual individual complete-row selection has
1017 rows (the checker independently counted180 additional boundary plane
differences). Thus the frozen JSON key actual_complete_S_rows describes a
strict positive subset of actual complete individual rows, not their full
inventory. No original source/result byte is changed.

The tested subset has the same five constant soft modes and all125 spectator
pin ranks equal nine. Extra positive rows preserve those conclusions. The
analytic boundary proof uses actual complete individual rows and relies only
on complete interior families for its kernel argument. This clarification
does not provide a numerical C_pin bound or extend the fixture to all boxes.
The checker report supplies its own independent detailed controls.
