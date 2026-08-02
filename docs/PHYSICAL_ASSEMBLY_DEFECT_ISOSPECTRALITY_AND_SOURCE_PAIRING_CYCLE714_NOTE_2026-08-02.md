# The mixed-frame assembly defect is spectrally invisible and is registered only in the source pairing, which takes exactly four coset values — Cycle 714

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed, joined Cycle-696 compiler contract inventoried below; that compiler is a
landed but audit-excluded support surface, not an independent audit authority.

The preceding cycles measured the mixed-frame assembly defect entry by entry: a
swap law for the exact comparator stencil, a per-magnitude census, and a complete
weight law. This cycle asks what the defect *does*. The answer is a dichotomy.
Against every spectral observable the defect is exactly nothing — the mixed-frame
reassembly is a relabelling of degrees of freedom, so the assembled operator is
carried to a permutation conjugate of itself and its spectrum does not move at
all. Against the pairing with a source the defect is order one — and the 24
pairings do not take 24 values. They take exactly **four**, constant on the four
right cosets of the constant-sign sextet, which is here derived to be a subgroup
of order 6. In framework vocabulary the defect is registered, not read: it has no
pre-pairing magnitude that a spectral reconstruction could recover, and it becomes
a number only once a source that does not transport with the frame is supplied.

## Theorem I — the coframe relabelling is a faithful action by permutations

For each of the 24 proper rotations `g` the compiler's mixed-frame reassembly acts
on the degree-of-freedom index by a map `m_g`, built from the frame's site map
composed with the class relabelling `v -> |g v|` and the negative-part anchor shift
`x -> x + min(g v, 0)`.

- `m_g` is a **bijection** of the dof set for all 24 frames at `L = 3, 4, 5, 6`:
  zero dofs land outside the index and the image count is the full dof count
  `n = 98 279 604 1115`, matching the open-box formula
  `n(L) = 3(L-1)L^2 + 3(L-1)^2 L + (L-1)^3`.
- The identity frame (frame index 23) gives the identity relabelling.
- The composition law `m_{gh} = m_g` after `m_h` holds in **576 of 576** ordered
  pairs at `L = 3` and at `L = 4`. The action is therefore a genuine group action,
  not a per-frame coincidence.

**Rejector (the anchor shift is load-bearing).** Dropping the negative-part anchor
and relabelling by the site map alone destroys bijectivity: at `L = 3`, 45 of 98
dofs land outside the index and only 53 distinct images remain. The bijectivity
above is a fact about the compiler's stated anchor convention, not an artefact of
any relabelling whatever.

## Theorem I' — hence exact isospectrality, and the defect's power sums vanish

Because `m_g` is a bijection, the reassembled operator is `Q_g = P Q P^T` with `P`
the permutation matrix of `m_g`. Every spectral consequence follows exactly and is
measured:

- The spectrum is unchanged. Worst eigenvalue deviation over the mixed frames:
  `1.9e-13` (18 frames, `L = 3`), `4.8e-13` (18 frames, `L = 4`), `4.0e-13`
  (4 frames, `L = 5`), `9.4e-13` (2 frames, `L = 6`).
- The defect `E_g = Q_g - Q` is traceless to `0.0e+00` at `L = 3` and `L = 4` over
  all 18 mixed frames — exactly, not to tolerance.
- The second power-sum identity `tr(Q E) + tr(E^2)/2 = 0` holds to `9.1e-13`, and
  the third power-sum identity `3 tr(Q^2 E) + 3 tr(Q E^2) + tr(E^3) = 0` to
  `1.2e-10`. These are the **computational identities** that force every symmetric
  function of the eigenvalues to be defect-blind, not merely the first few.
- Eigenvectors are transported rather than mixed: the relabelled top and bottom
  eigenvectors satisfy the reassembled eigenvalue equation to `2.6e-14`.

**Rejector (isospectrality is not a smallness statement).** Take the defect's own
support pattern, keep every entry magnitude, and resign the entries symmetrically
at random. The resulting perturbation has the identical Frobenius norm and the
identical sparsity pattern, and it moves the spectrum by at least `8.92e+00` at
`L = 3` and `9.36e+00` at `L = 4` over three seeds. The defect is large; it is the
*sign structure*, fixed by the permutation, that makes it spectrally invisible.

## Theorem II — the exact Frobenius weight law, reassembled from the landed census

Writing `u = L - 1`, every mixed frame carries the same defect weight

`||E_g||_F^2 = 800 u^3 + 224 u^2 + 32 u`

with no dependence on which of the 18 mixed frames is chosen. The three
coefficients are **derived**, not fitted: pairing the complete per-magnitude census
of the preceding cycle with its magnitude menu and doubling for symmetry gives
`2(16*8 + 12*8 + 8*12 + 4*20) = 800` for the cubic term, `2(8*16 + 4*(-8) + 1*16)
= 224` for the quadratic, and `2(4*4) = 32` for the linear. The runner reassembles
those three integers from the census table and then checks the law against the
compiled operator:

| `L` | `800 u^3 + 224 u^2 + 32 u` | mixed frames checked | worst relative deviation |
|---|---|---|---|
| 3 | 7360 | 18 | `3.4e-09` |
| 4 | 23712 | 18 | `2.1e-09` |
| 5 | 54912 | 18 | `1.5e-09` |
| 6 | 105760 | 18 | `1.1e-09` |
| 7 | 181056 | 18 | `8.2e-10` |
| 8 | 285600 | 3 | `6.4e-10` |

The gate is relative because the compiler assembles by finite differences; the
residuals sit at that stated precision floor and shrink as the law's value grows,
which is the signature of a compiler-noise residual rather than a model error.

The six constant-sign frames carry **no** defect at all — ceiling `2.9e-17` over
`L = 3, 4, 5, 6`. And the defect does not wash out with box size: the relative
weight `||E||_F^2 / ||Q||_F^2` climbs monotonically `0.1029 0.1271 0.1454 0.1596
0.1709 0.1802` across `L = 3` to `L = 8`. A growing fraction of the operator is
rewritten by a mixed frame, and the spectrum still does not move.

## Theorem III — the source pairing, and the four-value collapse

Let `b` be a supplied source and consider the pairing `b . Q_g^{-1} . b`.

1. **Exact transfer.** `b . Q_g^{-1} . b = (P^T b) . Q^{-1} . (P^T b)` for all 24
   frames, to `1.1e-16` at `L = 3` and `3.4e-14` at `L = 4`. Reassembling the
   operator is the same thing as relabelling the source.
2. **The dichotomy.** A source transported with the frame reproduces the reference
   solution exactly — worst relative deviation `4.2e-14`. A source held fixed while
   the frame turns does not: the smallest relative deviation over the tested frames
   is `2.6671`, and the spread of the pairing over the frames, in units of the
   reference pairing, is `1.6928` at `L = 3`, `7.3335` at `L = 4` and `10.5157` at
   `L = 5`. The defect is invisible to the operator's own spectrum and order one in
   the pairing.
3. **The sextet is a subgroup.** The six constant-sign frames are closed under
   composition, have order 6, contain the identity frame, and carry the trace
   multiset `[-1, -1, -1, 0, 0, 3]` — the identity and the two three-fold
   rotations about a body diagonal (traces 3, 0, 0) together with the three
   two-fold rotations about axes meeting it (traces -1), i.e. the six-element
   proper stabilizer of that diagonal.
4. **Four right cosets, four values.** The subgroup has four right cosets, of sizes
   `6 6 6 6`. The pairing is constant on each: worst variation within a coset
   `6.2e-10`, against a nearest pair of distinct coset values `0.0027` apart. The
   24-frame scan therefore takes exactly `4 4 4 4` distinct values at
   `L = 3, 4, 5, 6`. The cosets are *right* cosets because the dof relabelling is
   an anti-homomorphism in the permutation matrices — `P_g P_h = P_{hg}` — so the
   stabilizer acts on the source label from the left.
5. **Averaging.** A source averaged over all 24 relabellings is exactly frame-blind:
   spread `4.4e-16`. Averaging over the sextet alone is **not** enough — the
   smallest remaining spread is `0.0176`. Partial invariance of the source does not
   buy frame-blindness of the pairing; the coset structure survives it.

## What this fixes, and what it does not

The assembled operator is nonsingular and indefinite in this fixed compiler
contract — negative/positive eigenvalue counts `96/2`, `265/14`, `569/35` at
`L = 3, 4, 5`, smallest magnitude `3.2e-03`. The pairing is therefore a *signed*
quantity and no positivity or energy reading of it is licensed here.

Two consequences follow for the lane, and both are structural rather than
numerical. First, any spectral proxy for the minus-branch floor is exactly blind to
the mixed-frame assembly defect — Theorem I' says so with no tolerance attached, so
a floor built from eigenvalues alone cannot see the object the preceding three
cycles measured. Second, the floor's all-frame scan is not a 24-fold problem: by
Theorem III it collapses to **four** evaluations, one per right coset, with the
coset representatives fixed by the sextet.

## Boundary (honest limits)

- Frame coverage is complete (all 18 mixed frames) for the Frobenius law at
  `L = 3` through `L = 7` and for isospectrality at `L = 3, 4`; at larger sizes the
  scan is partial by design — 4 mixed frames at `L = 5`, 2 at `L = 6`, 3 for the
  weight law at `L = 8`. The sizes were capped by available memory on the host, not
  by any structural limit; the untested frames are untested, not excluded.
- Every floating-point row is **measured, not derived**, against the fixed
  Cycle-696 compiler contract with its stated finite-difference step. The three
  Frobenius coefficients are the exception: they are reassembled arithmetically
  from the preceding cycle's census and then confirmed against the compiler.
- The four-value collapse is verified at four box sizes with one pseudo-random
  source per size. Coset-*constancy* is source-independent by Theorem I' — it
  follows from the permutation similarity — but the specific four values, and the
  separation `0.0027` between the nearest pair, are properties of the tested source.
- This is the static spatial sector of the compiler only. Nothing here speaks to
  the temporal classes, to the wrapped box, or to any dynamical statement.
- The subgroup and coset facts are statements about the 24 proper rotations acting
  through this compiler's relabelling. They are not claims about a symmetry of the
  underlying axioms.

## The next paths opened

- Identify the four coset values against the source-stabilizer structure of the
  preceding sign law: the sextet's four right cosets and that law's coset quartet
  are both four-element collapses of the same 24-element scan, and a shared
  representative set would fuse the two statements into one.
- Solve the minus-branch floor on the four coset representatives rather than the
  full frame set, and check whether the floor is itself coset-constant.
- Ask which source classes make the pairing frame-blind. The fully averaged source
  is blind and the sextet-averaged one is not; the intermediate condition is a
  linear condition on the source and is directly computable.
- Test whether the growing relative weight `||E||^2 / ||Q||^2` has a closed form:
  the numerator is exact, so the question reduces to a closed form for `||Q||_F^2`,
  whose measured values already grow smoothly with the box.

## Dependency inventory

Load-bearing landed source, cited as a dependency:
[the all-24 frame sign law of the source-driven K field](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md).

Context only, not dependency edges: the Cycle-696 open-coframe endpoint compiler
supplies the assembly and the frame set; the census inputs to Theorem II come from
`PHYSICAL_MIXED_FRAME_COMPARATOR_EXACT_STENCIL_SWAP_LAW_CYCLE711_NOTE_2026-08-02`,
`PHYSICAL_MIXED_FRAME_DEFECT_CENSUS_FAMILY_LAW_CYCLE712_NOTE_2026-08-02` and
`PHYSICAL_DEFECT_WEIGHT_LAW_AND_COMPLETE_CENSUS_CYCLE713_NOTE_2026-08-02`, all of
which are in flight and unaudited at the time of writing; the minus-branch floor
referenced above is `LOCAL_SEAM_SIGNED_CLIFFORD_PHYSICAL_M2_COMPILER_CYCLE709_BOUNDED_THEOREM_NOTE_2026-07-26`.

## Runner

`scripts/physical_assembly_defect_isospectrality_and_source_pairing_cycle714_2026_08_02.py`
prints `TOTAL: PASS=39 FAIL=0`.
