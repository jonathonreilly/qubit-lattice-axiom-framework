# Goal

Repair the audited-conditional `poisson_self_field_note` source surface without
auditing or retagging it.

The objective is to preserve the useful finite computation while removing the
over-broad implication that the repo has derived a gravity field law. The PR
extracts a bounded supplied-branch core: given the supplied 2D Poisson equation,
source, boundary, normalization, readout, and longitudinal factor, the finite
runner verifies TOWARD shifts, near-linear F~M, active-branch Born cancellation,
and the exact `s=0` null.
