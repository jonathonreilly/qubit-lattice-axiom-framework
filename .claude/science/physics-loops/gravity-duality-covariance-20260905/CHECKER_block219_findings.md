CHECKER VERDICT: PENDING

Independent refuting checker (Opus 5) for block 219 — the three-direction (4,4,4) bench at
the covariant witness. Work in progress; the verdict line is rewritten when the run closes.

Machinery: Block 213's `bench_matrix` / `bloch_matrix` / `raising_rules` / `transpose_rules`,
Block 214's `raising_matrix` / `principal_part`, Block 216's `measure_census` / `BRANCH_TABLE`,
Block 217's `formal` / `curve_moduli` / `moduli_as_g`, Block 218's `phase_matrix` conventions and
Block 211's `leading_minors`, imported read-only. Everything downstream — the Bloch blocks, the
pencil and form symbols, the similarity, the eigenvalue multisets, the seven quadric values, the
read-off, the rescaled constants, the control factor shapes and the overlap fold — is rebuilt in
this seat. The block-219 runner was read for its literals and conventions and never imported,
called or copied. Every Bloch phase is `sp.sympify`d before use.

---

## CK-01 — the bench at extent (4,4,4): 64 sites, 192 raising entries, 64 y-links, eight momenta

Note line 184-186, verbatim:

> bench       Block 213's bench_matrix at extent (4,4,4): 64 sites; raising bench matrix 192 nonzero entries, 64 of them between sites
>             differing only in y (the y direction now carries its link); Bloch momenta (z_t, z_x, z_y) in {1, i}^3, in Block 213's order
>             (1,1,1), (1,1,i), (1,i,1), (1,i,i), (i,1,1), (i,1,i), (i,i,1), (i,i,i) with kappa_z = (0,0,0), e_y, e_x, e_x+e_y, e_t, e_t+e_y,

Computed, on Block 213's `bench_sites`, `bench_matrix(raising_rules(lane_rules(3)), (4,4,4))` and
`bench_momenta((4,4,4))` built in this seat, with the site index decoded independently
(`idx -> (idx//16, (idx//4)%4, idx%4)`, checked against `b213.site_index` at all 64 sites):

- `len(bench_sites) = 64`; raising bench matrix shape `(64, 64)`; **192** nonzero entries.
- Nonzero entries joining sites that differ **only in y**: **64**. (Also measured, not claimed by
  the note: 64 differ only in t and 64 only in x — the 192 split 64/64/64, so the y direction
  carries exactly the same link count as t and x. This is the fact that makes "the y direction now
  carries its link" true rather than merely nonvacuous.)
- `bench_momenta((4,4,4))` returns exactly eight tuples, every entry in `{1, I}`, in the order
  `(1,1,1), (1,1,I), (1,I,1), (1,I,I), (I,1,1), (I,1,I), (I,I,1), (I,I,I)` with
  `kappa_of` giving `(0,0,0), (0,0,1), (0,1,0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)`
  = `0, e_y, e_x, e_x+e_y, e_t, e_t+e_y, e_t+e_x, e_t+e_x+e_y`.

Disposition: **CONFIRMS** (every literal in the sentence, including the momentum order and the
kappa assignment, reproduced exactly).

---

## CK-02 — the Bloch-point lemma at symbolic z with z_y live

Note line 217, verbatim:

> d_B(z) = sum_mu (z_mu - 1/z_mu)/2 * D(e_mu)      an exact 8 x 8 identity at symbolic z, z_y a free symbol of the Bloch block (measured);

and note line 221, verbatim:

> D(e_mu)^2 = 0, the D(e_mu) anticommute, hence D(kappa_z)^2 = 0 at all eight points, D(e_t + e_x + e_y)^2 = 0 included.

Computed at `z = (z_t, z_x, z_y)` as three sympy symbols (sympified), against
`sum_mu ((z_mu - 1/z_mu)/2) * D(e_mu)` with `D` = Block 214's `raising_matrix` substituted at the
unit kappas:

- residual after `sp.simplify` on all 64 entries: **0**. `z_y` is in the free symbols of BOTH
  sides, so the identity is not vacuous in y (the specific trap: a lemma stated at symbolic z but
  measured only where z_y = 1 would pass with `z_y` absent — it is present here).
- `D(e_t)^2 = D(e_x)^2 = D(e_y)^2 = 0`: True, True, True. All three anticommutators
  `D(e_a)D(e_b) + D(e_b)D(e_a)` vanish (ta/ty/xy): True, True, True.
- `D(e_t+e_x+e_y) = D(e_t)+D(e_x)+D(e_y)` (D is linear in kappa): True, and its square is 0.
- `D(kappa_z)^2 = 0` at all eight kappas: True at all eight.
- The raising Bloch block equals `i D(kappa_z)` at all eight points, `(i,i,i)` included: True at
  all eight, checked entrywise (not by charpoly).

Also measured, and worth recording because it is a live way to get the pencil wrong: the
transposed raising Bloch block is `-i D(kappa_z)^T` at all eight points, and at `(i,i,i)` it is
**not** equal to the transpose of the raising Bloch block (`i D^T` vs `-i D^T`). A checker or
runner that used `d_B.T` in place of Block 213's `transpose_rules` fold would build a different
pencil. The runner uses `transpose_rules`; this seat used `transpose_rules` too, after checking
that the two genuinely differ.

Disposition: **CONFIRMS**.
