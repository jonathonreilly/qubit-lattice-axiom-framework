# Criteria for gate c0-loc, kill test of (4.1b) and the row part of (3.4)

Written before any run, 2026-11-02. A run refutes or guides. It discharges nothing.

Why this test: the lc-u gate ran site paths only ("Bond kernels were not run"). (4.1b), the one-carry identity for bond rows, is the crux of `library/c0-loc.md`.

Setting: SU(2), d = 4, L = 3, actual log-average block map and axis-ordered combs, from `checks/gate_lc_u/path_coarsening.py` (imported, unchanged). Fields smooth, tube, noise at target a = 0.02, 0.01, then a random fine gauge transformation, so links are of order one and a dropped link is visible. N = 9 gives rows at level r = 1; N = 27 gives rows at r = 1 and r = 2. Sampled rows and random kernel terms (x_j, t_j at each level).

For each term: T := p_(r-1) ... p_0, the composite transport to the fine tail. Flags delta_j and points q_j as in (4.1b), with q_(j+1) = parent(q_j).

- **B1, one step.** err_j := |p_j V_j(b_j)^delta_j - V_(j+1)(c)^delta_(j+1) Gamma(q_(j+1), q_j)| <= 2^14 L^2 E_j(B+), with E_j(B+) the l^4 norm of level-j plaquette angles on the patch of the two endpoint blocks and their neighbours. FAIL if any term violates it.
- **B2, composite.** |T - V_r(c)^delta_r Gamma ... Gamma| <= sum_j err_j + 1e-9. FAIL if violated: that would be an uncancelled or branching term.
- **B3, depth.** S := max over terms of a row of |T(term) J_z(x)^-1 - T(term0) J_z(x0)^-1|, the spread that (3.4) calls one rotation O_c for the whole row, across delta_r = 0 and 1. At target 0.01, S/a at r = 2, N = 27 may not exceed 2 times S/a at r = 1, N = 9, for each field kind.
- **B4, linearity.** S/a at N = 27, r = 2 changes by at most 25 percent between targets 0.02 and 0.01.
- **B5, control.** Dropping the final factor V_r(c)^delta_r from the prediction must give an error at least 100 times the B2 error on terms with delta_r = 1. If not, the test cannot see the carry, and the run is void.

Pass: B1 to B5 all hold. Failure of B1, B2 or B3 would need a look by hand before any verdict. L = 3 is far below the file's L >= 16K, so the constants are not tested; only a trend or a broken identity can show.

## Amendment, 2026-11-02, after the first run (thresholds unchanged)

First run, `bond_carry.out`: FAIL by the written rule on B4, kind tube, N = 27, r = 2, with S about 5e-15 at both targets. The twelve random rows missed the tube, so S was round-off and the ratio has no meaning. The same flaw means the tube entries of B3 at N = 27 tested nothing, though they passed. The first output stands as the record.

Second run, `tube_rerun.py`, output `bond_carry_tube.out`: tube only, with every sampled row taken through the tube centre, at a random direction, and 400 terms per row. B1 to B5 as above with the same numbers. The other kinds are not rerun.
