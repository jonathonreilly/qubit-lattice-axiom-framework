# Goal

Build a bounded-support firewall separating record history order and per-step
kernels from physical time/rate normalization.

The block should preserve the unbounded finite-history result while preventing
history length, counts, or transition kernels from being read as a physical
clock or rate law.
