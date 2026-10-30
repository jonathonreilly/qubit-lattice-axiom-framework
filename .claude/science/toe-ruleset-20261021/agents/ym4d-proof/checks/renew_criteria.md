# RENEW numerical-check criteria

Registered before any numerical script or experiment. Written proofs are
separate evidence and do not require numerical pre-registration.

1. A paired-contour enumeration, if run, must use block centers
   `LX+(L-1)/2`, all 24 coordinate orders, every point of the block, and
   every direction. Test the involution field for odd L=3,5,7 and both
   constant sign labels. Exact rational matrix entries must agree with the
   stated arithmetic mean in every case; any mismatch is a failure.
2. A linear-mode probe, if run, must agree with the independently derived
   ratio `[sin(L k/2)/(L sin(k/2))]^4` to absolute error <=1e-10 away from
   k=0. It is a diagnostic of action contraction, not a uniform proof.
3. No probability sampling can certify a depth-uniform renewal estimate.

Execution requires a numerical lock, effective nice priority, all BLAS/OMP
threads=1, RSS below 1 GB, load below 8 and at least 30% memory free. No pools
and no RLIMIT_AS. A failed guard blocks execution and is reported as such.
The initial nice probe was denied by the sandbox. No numerical script has
been created or executed and no numerical PASS is claimed.
