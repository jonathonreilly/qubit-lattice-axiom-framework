# Actual first control failure and narrow fixture correction

The first run reached the final nonzero-remainder assertion and failed:
`AssertionError: fixture must exhibit the hard-core higher-occupancy correction`.
The complete source pin, row, evenness and Hessian assertions preceding it
had not raised an exception. The single four-site complete plane-S fixture
happened to have a zero nested-current lift remainder. That fixture cannot
serve as the planned negative control against deleting hard-core corrections.

All six original files are preserved byte for byte in
history/single-plane-zero-remainder/. No source theorem changed. The corrected
fixture consists of the complete actual plane-S rows at centers0 and e1+e2,
on their SIX physical sites. It retains actual signed pair coefficients and
computes the full64-dimensional hard-core action. Sparse multiplication skips
zero entries; this changes no operator. The same literal N2 lift is compared
on every occupation sector, and a nonzero N>=3 difference is required.
The original 10CPU/45wall/100MiB price and standard-library exact arithmetic
remain. The second run has not occurred at the time this correction is written.
