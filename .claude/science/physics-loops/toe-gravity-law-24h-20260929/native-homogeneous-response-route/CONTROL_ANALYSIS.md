# Actual finite controls and their exact role

The corrected run exited0 with literal TOTAL PASS=7 FAIL=0, seven declared
families rather than seven many-body theorems. It used8.403099 child CPU
seconds,8.428339250036515 wall seconds,23,871,488 bytes peak child RSS; all
within the predeclared10CPU/45wall/100MiB envelope. Both STOP sentinels and
the original campaign deadline were checked by the managed wrapper. No
unmanaged worker or full-torus density diagonalization was started.

The literal source expansion visits11,662 S/W rows near the reference
edges. It verifies the eighteen-edge pinned S matrix exactly. Actual merged
absolute row sums are mu*(2,2,2,3,3,3,3,3,3) and tau*(16,16,16,24,24,24,24,24,24),
inside the analytical3mu+24tau bound. The pair-center coefficients are even
under displacement reversal and have l1 displacement at most3. Their zero
symbol and six exact rational quadratic-direction coefficients agree with
the displayed physical nine-edge blocks, including both plane centers.

The final fixture is the full64-dimensional M2 tensor product of the six
sites in two overlapping ACTUAL plane-S stars at centers0 and e1+e2. It
checks the summed endpoint double-commutator identity as an entire operator,
then computes the nested current and subtracts its literal N2 pair lift.
The difference vanishes in every block having N<=2 on either side and is
NONZERO in higher sectors. There are 275 nonzero rational entries. For example,
R_(7,7)=99/32; the occupied mask7 means(-1,0,0),(0,-1,0),(0,1,0), and
R_(13,13)=-6033/64. Thus the remainder is neither identically zero nor
silently replaceable by a positive correction. These are actual finite
operator witnesses, not physical ground states or a phase test. The mask7
occupation triangle has all graph degrees2, so Ddiag alone would not pay
for every local crowded configuration; the gradient pin is necessary in
the analytical local-occupancy estimate.

The first four-site single-plane run FAILED the nonzero-remainder assertion
because that specially symmetric fixture had zero remainder. It is retained
verbatim with code, plan, wrapper and metrics in
history/single-plane-zero-remainder/. FIXTURE_CORRECTION.md records the narrow
repair before the second run. No analytic theorem was altered because of
this finite-fixture inadequacy. No failure was converted into a PASS.

These controls check source conventions and the dangerous local lift. They
do not prove the all-volume derivative constants, positivity for an unknown
many-body ground state, or the spectral-tail inequality. Those are the
explicit analytical arguments in the two proof files. No finite check
selects a native phase, clock, state or physical record mechanism.
