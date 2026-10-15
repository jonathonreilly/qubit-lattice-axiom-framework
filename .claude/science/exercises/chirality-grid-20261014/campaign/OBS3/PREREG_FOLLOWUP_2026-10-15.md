# OBS-3 dated follow-ups to PREREG.md (PREREG.md itself is unedited)

## 2026-10-15 12:22Z (after controls C1-C3, the first R1 run and the first R2b run; reading rules unchanged)

1. **Controls passed before anything new** (`scripts/ctl.out`): C1 reproduces OBS-2 branch-B c_TT^d = -2.10666612e-8
   (worker path, identical digits) vs the referee's independent -2.10666629e-8 (8e-8 relative) at N = 24, m0 = 0.1,
   Delta = 0; Delta = 0.5 likewise. C2 and C3 pass. C3b's first version compared the lepton fields (not permuted, residual
   = roundoff) and reported a spurious 0.26 mismatch; restricted to the quark fields it is 3e-15. Fixed before any reading.
2. **Roundoff floor.** For realisations with a non-universal y_t^2 part (residual ~1e-3), double precision limits the
   exact-zero rows to ~1e-20 absolute (ratio ~1e2 against 1e-22). Where a row is zero by an algebraic identity (flat
   column, S3-invariant data) I state the identity as the result and quote the numerical value as roundoff, with the
   residual/universal ratio as the numerical check.
3. **Added analyses (not in the PREREG run list, prompted by S3/S5 results):**
   - `univ.py` A: model M1 with right-handed rotations that make the corner-diagonal Yukawas corner-constant;
   - `univ.py` B: model M2 with equal-modulus corner textures (diagonal equal, all off-diagonal moduli equal) fitted
     to mass ratios, |V_ij| and |J|. Literature comparator found by search after S3: the "universal strength of
     Yukawa couplings" (USY) ansatz (Branco, Silva-Marcos, Rebelo, PLB 237 (1990) 446; Branco, Colaco Ferreira,
     Hessler, Silva-Marcos, arXiv:1101.5808, JHEP 05 (2012) 001: USY fits CKM moduli but not the size of CP violation).
     Abstract-level reading only.
   - `algebra.py`: kernel comparison, dephased-Hadamard check, CKM Latin-square test, column-flatness bounds.
   - `yuk_lv3.py` / `run_r2.sh`: range-2 symbol tables (registered in the PREREG model section; run after R2b).
4. **R2b optimiser caveat.** The up-flat minimisation (`upflat.py`, Powell, 2 random starts x 6 generation orders per
   carrier/split/placement) is a local search. Its "bracket-robust" minima are upper bounds on the true minimum, not
   lower bounds; they are not used for a FORCED reading.

## 2026-10-15 13:04Z (all runs done; reading rules unchanged)

5. **Runs completed:** `escape.out` (R1, flat-light E1), `upflat.out` (R2b), `univ.out` (A: M1 diagonal equalisation;
   B: equal-modulus fits B-gen, B-sym, B-gen120), `structure2.out` (kernel identity, up-flat on-site scan, word
   spreads), `run_r2.sh` + `r2_ctl.out` + `r2check.out` (range-2 symbol tables N = 48, 96, full bracket; C3 violation
   1.2e-14; shared entries identical to OBS-2's tables), `algebra.out`. Archive: `obs3_archive.npz` (63 arrays).
6. **New exact identity found (not anticipated in the PREREG):** for covariant on-site carriers the flavon kernel is the
   Higgs on-site kernel of the INTERNAL corner, K_fl(c,c',a) = I_00(c',a), to 8e-13 over N = 32..96 and the bracket
   (`structure2.out:1`). It is used in the report's structure statement S2.
7. **r2check first version** evaluated realisation A (built for M1 only) also with M2 carriers and printed a spurious
   non-universal result; restricted to M1 as registered for A, then rerun. Recorded here before reading.
8. **No reading rule changed.** The C2' finding (non-Hermitian circulant textures are C3- but not S3-invariant in M2:
   per-corner isotropic residual 6e-16, transverse residual 3e-4 relative) is a side result.
9. Other python processes visible in `ps` (runner.py, nt1p_kernel.py, servers) belong to other campaign agents, not to OBS-3.
