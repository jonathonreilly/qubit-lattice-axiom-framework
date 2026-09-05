CHECKER VERDICT: PASS-NO-BLOCKER

Every load-bearing claim of the block-218 note that I could reach in the budget was rebuilt from
scratch (my own periodic bench, my own Bloch fold, my own `Z`-conjugation similarity, sympy
`factor_list`/`charpoly` in place of the runner's `DomainMatrix` charpolys) and reproduced exactly;
two items are CORRECTS-grade precisions of wording, none of them touches a number.

Method note. Parent runners were imported read-only for their landed primitives only
(`b213.lane_rules/raising_rules/transpose_rules/onsite_rules/overlap_rules/formal_family/
metric_candidates/quadratic_form/bench_momenta/multiset_of`, `b214.raising_matrix`,
`b216.formal/moduli_as_g/W1_MODULI/FLAT_MODULI/BRANCH_TABLE`, `b217.curve_moduli`). The block-218
runner `scripts/admissibility_dirac_kahler_two_direction_bench_covariant_witness_2026_09_05.py` was
read but never imported, called or copied. The bench, the Bloch blocks, the phase matrix `Z`, the
identities, the ratios, the cross term, `det M`, the control's factor shapes, the overlap fold and
the `32 x 32` charpolys are my own code in the checker scratch (`b218check/ck.py`, `a.py`-`g.py`).

---

### CK-01 — the bench at extent (4,4,2)  — CONFIRMS

Note line 181, verbatim:
> `bench       Block 213's bench_matrix at extent (4,4,2): sites 32; raising bench matrix 64 nonzero entries, 0 between sites differing`

and line 182:
> `            only in y; Bloch momenta z = (1,1,1), (1,i,1), (i,1,1), (i,i,1) with kappa_z = (0,0,0), (0,1,0), (1,0,0), (1,1,0);`

Computed: my own periodic bench (site loop, step wrapped modulo the extent, aliases added) on
`raising_rules(lane_rules(3))` at `(4,4,2)`. **32 sites; 64 nonzero entries; 0 entries between
sites differing only in `y`.** My bench equals `b213.bench_matrix` entrywise (a cross-check of my
own construction, not a premise). My own momenta `exp(2 pi i m/N)`, `m < N/2`, reproduce
`b213.bench_momenta((4,4,2)) = ((1,1,1), (1,I,1), (I,1,1), (I,I,1))` — the mixed fine point
`(i,i,1)` is present. Independently: the declared witness face signs `(+,+,+,+,-,+)` satisfy
Block 213's rule A (`S1 = -E S0 E`, residual zero on the symbolic family).

### CK-02 — the raising Bloch block, additivity, `d^2 = 0`  — CONFIRMS

Note lines 211-213, verbatim:
> `d_B(z) = sum_mu (z_mu - 1/z_mu)/2 * D(e_mu)      an exact 8 x 8 identity at symbolic z (the lane's forward +eta/2 and backward -eta/2`
> `                                                  links along mu add to (eta/2)(z_mu - 1/z_mu) on the graded entries; D(e_mu) = eta);`
> `at z_mu = i:  (i - (-i))/2 = i;   at z_mu = 1:  0;   so d_B(z) = i D(kappa_z),  kappa_z = e_t [z_t = i] + e_x [z_x = i]:`

Computed on my own Bloch fold at symbolic `z = (zt, zx, zy)`: `d_B(z) - sum_mu (z_mu - 1/z_mu)/2
D(e_mu) = 0` exactly (8 x 8 zero matrix). `D(e_t)^2 = D(e_x)^2 = D(e_y)^2 = 0`; all nine
anticommutators `D(e_mu)D(e_nu) + D(e_nu)D(e_mu) = 0`; `D(e_t + e_x) = D(e_t) + D(e_x)` and
`D(e_t + e_x)^2 = 0`. At the four points `d_B - i D(kappa_z) = 0`, mixed point included.

### CK-03 — the transposed Bloch block and the sign bookkeeping  — CONFIRMS (item 3 recheck)

Note lines 233-235, verbatim:
> `to `0` (the row grade is one higher), so `Z D Z⁻¹ = i D` and`
> ``Z Dᵀ Z⁻¹ = −i Dᵀ`, and the conjugated operator is `−(D − H0⁻¹ Dᵀ H0)` with`
> ``D = D(κ_z)`; its negative square is `−(D − H0⁻¹ Dᵀ H0)² = (D + H0⁻¹ Dᵀ H0)²`

Computed explicitly at all four points: `bloch(transpose_rules(raising), z)` equals
`d_B(1/z)^T` **and** equals `-d_B(z)^T` **and** equals `-i D(kappa_z)^T`. So the transposed block
is the Hermitian transpose at a unimodular point, and the sign bookkeeping is:
`Z d_B Z^-1 = i (i D) = -D`, `Z d_B^dag Z^-1 = -i (-i D^T) = -D^T`, `Z H_B Z^-1 = H0`, hence
`Z (d_B - H_B^-1 d_B^dag H_B) Z^-1 = -(D - H0^-1 D^T H0)`, verified as a matrix identity (not by
charpoly) at every point, at the witness, at `W1` and at the flat cell. `A = H0^-1 D^T H0` satisfies
`A^2 = 0`, so `-(D-A)^2 = (D+A)^2 = (H0^-1 M(kappa_z))^2` — verified as matrices, both sides.

### CK-04 — the onsite Hodge block is a similarity  — CONFIRMS (strengthened)

Note lines 224-225, verbatim:
> `z^{c_j − c_i}`, so `H_B(z) = Z⁻¹ H0 Z` with `Z = diag(z^c)` — measured True at`
> `all four points at the witness, the control and the flat cell. Mutation `break_onsite_similarity`.`

Computed at **symbolic** `z = (zt, zx, zy)` (stronger than the four measured points):
`H_B(z) - Z^-1 H0 Z = 0` at the witness line cell, the `W1` line cell and the flat line cell.

### CK-05 — the mixed-point identity  — CONFIRMS

Note lines 244-245, verbatim:
> `**The mixed-point identity holds exactly**: the onsite pencil Bloch block at`
> ``(i, i, 1)` has the charpoly of `(H0⁻¹ M(e_t + e_x))²` at the witness, the`

Computed by DIRECT SIMILARITY, not by charpoly comparison:
`Z (-(d_B - H_B^-1 d_B^dag H_B)^2) Z^-1 - (H0^-1 M(kappa_z))^2 = 0` at all four points and all
three cells (witness line, `W1` line, flat line); the charpolys agree as a corollary. Eigenvalue
multisets of `-(operator)^2` at the witness, by `factor_list` over `QQ(sqrt 6)` on my own 8 x 8
charpoly, matching `(H0^-1 M)^2` term by term:

```
(i,1,1) and (1,i,1):  {9/8 x2, 16/11 x2, 18/11 x4}
(i,i,1):              {3/2 x2, 64/33 x2, 24/11 x4}
(1,1,1):              {0 x8}
flat: {1 x2, 16/15 x6} at both pure points, {2 x2, 32/15 x6} at the mixed point
```

The form reading fails at every nonzero point (witness and `W1`): its charpoly differs from the
principal part's at each of `(1,i,1)`, `(i,1,1)`, `(i,i,1)`. Overlap: see CK-09.
