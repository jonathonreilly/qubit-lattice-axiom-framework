# One selected exact fixture, declared before execution

Scientific execution count currently zero. One fixed diagnostic is authorized. No sweep, replay of a parent runner, or adaptive parameter selection is planned.

Fixture: the actual section7 geometry at L_b=8, Q=3, n_old=2, M=4; fixed f=(1/5,-1/7,2/9,0), q=1, r=1/12, h_d=1/4. Original c=v0 and e=e(v0), with Pc,Pe represented by their commuting sign eigenvalues only for this contraction check. All fixed original coordinates are generated from the literal site lists. Both fresh copies and every declared edge are generated as unit lattice segments.

Compute the complete finite one-particle matrices B, B±h_d|b><b| and invert them by generic exact Fraction Gauss–Jordan elimination, independently of the rank-one inverse formula used to select t_j. Check the rank-one formula and actual two-source quadratic response for every single-clock-position and all four Pauli signs. Check the actual vacuum-clock response and preserve a two-clock-occupation extra cross term. Check source-sign/one-mirror and missing-clock-counterterm mutations by explicit coefficients. Check fresh-site disjointness, original-site preservation, every unit edge, and all auxiliary/new-port degrees.

The source is exact rational arithmetic with no NumPy, selected float tolerance, or numerical diagonalization. A mismatch is a failure to retain, not a reason to retune this fixture. The complete program/input/source hashes are sealed before its single child execution. Full stdout, stderr, return code, exact response constants and geometry lists remain on disk.

This diagnostic does not construct or diagonalize the 2^(2m)-dimensional auxiliary space, evolve a time-dependent state, or numerically check the global residual. The full-sector kernel/gap, mixed corrector, arbitrary-H0 estimate and all-parameter coordinate proof remain analytic author claims awaiting independent checking. It is not an independent audit.
