# Goal

Repair the beta6 resummation harness conditional audit blocker without claiming
beta=6 closure.

The audit concern was that the harness classifications depend on exact
`d_6..d_11`, but the harness only exposed those values as embedded constants.
This block wires the harness to the paired exact d11 coefficient source runner
and verifies the paired cache is source-SHA fresh.
