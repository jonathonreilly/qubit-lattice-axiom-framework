# RESULTS — block 218, the cone's shape on a two-direction bench at the covariant witness (Fable primary seat)

Runner: `scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py`
Note: `docs/ADMISSIBILITY_DIRAC_KAHLER_TWO_DIRECTION_BENCH_COVARIANT_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-05.md`
Exact arithmetic only (SymPy integers, rationals, symbols, `QQ(sqrt 6)` and `QQ(sqrt 6, i)`; exact charpolys of `8 x 8`
and `32 x 32` matrices over algebraic number fields; factorization over `QQ` and `QQ(sqrt 6)`; matrix identities at
symbolic Bloch phases); gate I measures zero `sp.nsimplify`, zero float literals and zero float call sites in the
runner's own source.

## Headline

The contract's "(4,4) bench" for the eight-corner cell is Block 213's `bench_matrix` at extent `(4,4,2)` (32 sites, not
128: each site is one corner; the `y` direction at extent 2 carries no link), and its `bench_momenta` DO contain the
mixed fine point `(i, i, 1)` — said first, per (f). On it the raising Bloch block was MEASURED before any identity was
asserted: `d_B(z) = sum_mu (z_mu - 1/z_mu)/2 D(e_mu)` at symbolic `z`, so the block is `i D(kappa_z)` at every point —
the two fine momenta enter ADDITIVELY and at the mixed point the block is `i D(e_t + e_x)` exactly. The onsite Hodge
Bloch block is `Z^-1 H0 Z`, and with `d^2 = 0` (the `D(e_mu)` square to zero and anticommute) the onsite pencil block
charpoly equals the charpoly of `(H0^-1 M(kappa_z))^2` at EVERY point — `e_t`, `e_x` and, at the mixed point,
`e_t + e_x` — at the witness, the all-plus control and the flat cell: THE MIXED-POINT IDENTITY HOLDS EXACTLY (an exact
finite identity at the fine momentum `pi/2`, not a small-`k` limit). It fails for the form reading and for the overlap
assembly at every nonzero point. At L+-'s covariant cell (mask 2, the curve moduli) with the parameters at the
star-line point `(0, 1/4, -1/4, 1/4)` the onsite pencil block multisets are `{9/8 x2, 16/11 x2, 18/11 x4}` at both pure
points and `{3/2 x2, 64/33 x2, 24/11 x4}` at the mixed point: at each of the three points EVERY nonzero eigenvalue is a
Block 216 branch constant `{1, 128/99, 16/11 x2}` times `k^T G1 k` at `kappa_z` (`9/8, 9/8, 3/2`), the cross term
`G1_tx = (3/2 - 9/8 - 9/8)/2 = -3/8` is isolated from the three points and equals the entry of `G1 = D1/D0` — THE
CONE'S SHAPE RESTRICTED TO THE `(t, x)` PLANE IS VISIBLE TO A BENCH (Block 217's REOPEN item 3, answered at one
witness); `det M` on the line is one quadric to the fourth power (`81/64, 81/64, 4`). At the all-plus `W1` control the
identity still holds (it is structural) but the shape statement fails exactly thus: one rational branch `k^T G1 k`
(`16/15, 16/15, 8/5`, reading W1's `G1_tx = -4/15`) and the other three eigenvalues the roots of an irreducible cubic at
the pure-`t` and mixed points and `256/385` plus an irreducible quadratic at the pure-`x` point; `det M` on the line is
two distinct quadrics each squared. Under the overlap assembly the Bloch fold at symbolic signs, moduli and parameters
is parameter-free at both pure points and at the mixed point sees ALL FOUR parameters through the signed sum
`(-D07 - D16 + D25 + D34)/4` on the parity block (Block 217's `s` at the zero point; `-lam` on the star line), so the
overlap bench charpolys at the line point equal the zero-parameter ones at the pure points and differ at the mixed
point; and the overlap bench distinguishes `t` from `x` at the witness (form `{36481/55296, 89401/55296}` against
`{51529/55296, 69169/55296}`; pencil R5's `{1 x8}` against `{227/263, 263/227}`) where the onsite bench does not —
Block 217's `x`-axis `D4` seen by a bench (REOPEN item 4). All twenty degree-32 charpolys have Bloch union = direct;
every direct `32 x 32` charpoly under 2 s. Nothing selected; the covariance antecedent stays a reading; no
dispersion-law, Lorentzian, light-cone or continuum reading.

## Run record (every run's summary line)

| run | command | summary | exit |
| --- | --- | --- | :---: |
| probe 1 (scratch, 19:15Z) | `probe1.py` | momenta `(1,1,1),(1,i,1),(i,1,1),(i,i,1)`, 32 sites, 0 `y`-links, 64 raising entries; raising block `= i D(kappa_z)` at all four points and the symbolic sine identity True; `D_mu^2 = 0`, anticommute, `D(e_t+e_x)^2 = 0`; onsite `H_B = Z^-1 H0 Z` at all points (witness, W1); 14 bench charpolys, all Bloch = direct, direct `0.03-1.6 s`, union `0.2-0.8 s`; identity table (onsite pencil True at all four points at three cells; form/overlap False at nonzero points, flat overlap mixed); ratios `{1, 128/99, 16/11}` at all three points at the witness, `G1_tx = -3/8`; W1 shapes; `det M` factors `[(2,4)]` (witness) and `[(2,2),(2,2)]` (W1); overlap fold parity blocks per point — 35.7 s total | 0 |
| harness run 1 (1edb805ad4, 19:32Z) | full runner | measurement complete (`bench 17.6 s`, `shape 5.8 s`, `control 5.7 s`, 34 s); `INTERNAL-EXCEPTION: TypeError: keywords must be strings` in `build_claims` — defect 1 | 1 |
| harness run 2 (6fbbfa6ff3, 19:34Z) | full runner | `TOTAL: PASS=25 FAIL=1` in 33.7 s: only `I-1` (the note's fence not yet written) | 1 |
| certification 1 (d95234265a, 19:38Z) | `runner_cache.execute_and_write_cache(..., 600)` | on the 608-line note; superseded by the recertification on the note under the 600-line cap (below) | see below |
| certified baseline | `runner_cache.execute_and_write_cache(..., 600)` | see "Certified baseline" below | see below |
| mutations | `--mutation <name>` x 27, one helper invocation per mutation (`run_mutation.sh`), batches of four, after the certification | see the table below | see below |

## Defects found in this seat's own drafts (before certification) and fixed

1. Two mutation flips (`break_control_multisets`, `break_control_failure`) built their wrong dictionaries with
   `dict(base, **{tuple_key: value})`, which Python rejects (keyword keys must be strings); rewritten as
   dict-unpacking literals `{**base, tuple_key: value}`. No measurement or literal changed.
2. The note's first complete draft was 614 lines (cap 600); the one-sentence summary and the interpretations-fence
   word list were tightened. No number changed; the fence line untouched.

## Modelling choices not forced by the landed chain

- The bench: the contract's "(4,4)" read as Block 213's `bench_matrix` at extent `(4,4,2)` — the two-direction bench
  of the three-direction chain (Block 213's literal `(4,4)` is the two-direction lane on four-corner cells, which
  cannot carry the eight-corner cell form). Declared first and gated (`C-1`); the direct `32 x 32` charpoly fits,
  so no substitute consistency gate was needed; Block 217's `(4,2,2)` identity is re-run at the witness anyway (`C-2`).
- The cells: Block 217's `bench_cells` (the same function), plus the flat cell at zero parameters as the R5 control.
- The identity: the Bloch block charpoly against the charpoly of `(H0^-1 M(kappa_z))^2` with the principal part
  squared symbolically then evaluated at `kappa_z in {e_t, e_x, e_t + e_x, 0}` — an exact polynomial identity, the
  mechanism (`Z D Z^-1 = i D`, `d^2 = 0`) written in the note and the identity measured rather than derived.
- The shape test: the block multiset divided by `Q(kappa_z) = kappa_z^T G1 kappa_z` compared to Block 216's
  `BRANCH_TABLE[("L+-", "line 1/4")]`; the cross term read from the smallest nonzero eigenvalue at each point (the
  constant-1 branch), which is the bench-only reading.
- The control's failure stated through factor shapes over `QQ` (the rational roots and the irreducible degrees)
  rather than through a numerical comparison.
- The overlap fold at symbolic signs, moduli and parameters at each Bloch point (Block 214's `formal_cell` with
  Block 217's sign symbols), the parity block's nonzero entry declared as a string literal.

## What could NOT be established (honest list)

- The `y` direction: `G1_ty`, `G1_xy`, `G1_yy` are not read (the bench samples the `(t, x)` plane); the cone's shape
  in all three directions needs an extent with `N_y = 4` (64 sites), not run.
- The other seven rule-A cells, symbolic parameters on the bench, other line multiples or `D07 != 0`: not run.
- The flat cell's overlap identity pattern (True at `(1,i,1)` and `(i,i,1)` for the form, at `(i,i,1)` for the pencil):
  measured and recorded, not explained and not claimed.
- The overlap mixed-point charpolys at the line point (an irreducible quartic squared for the form,
  `(17837 lam^2 - 58604 lam + 48020)^4` for the pencil): declared by shape; no closed form in the signed sum.
- The refuting checker: pending (`CHECK_VERDICT = "FABLE-PRIMARY-REFUTING-CHECKER-PENDING"`); the independence class
  is left to the supervisor.
