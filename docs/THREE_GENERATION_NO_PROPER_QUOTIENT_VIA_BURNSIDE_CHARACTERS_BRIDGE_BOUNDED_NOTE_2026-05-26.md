# Three-Generation No-Proper-Quotient via Burnside + Characters Bridge

**Date:** 2026-05-26
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; audit verdict and
effective status are set by the independent audit lane.
**Primary runner:** [`scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py`](../scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py)

## Claim

Given two existing retained narrow theorems — the distinct-translation-
characters narrow theorem (which supplies the three commuting diagonal
involutions `T_x = diag(-1, +1, +1)`, `T_y = diag(+1, -1, +1)`,
`T_z = diag(+1, +1, -1)` on `C^3` with distinct joint sign characters)
and the M_3(C) Burnside narrow theorem (which supplies the
algebra-generation conclusion that `<C, T_1, T_2, T_3>_alg = M_3(C)`
for any order-3 cyclic permutation `C` of the basis) — the
**no-proper-quotient** statement on the finite-dimensional `C^3`
carrier follows by a single composition step:

> Let `H ≅ C^3` be any 3-dimensional complex Hilbert space with a
> chosen ordered basis `(X_1, X_2, X_3)`. Let `P_{X_i}` be the
> diagonal projector onto `span{X_i}` and let `sigma` be the order-3
> cyclic permutation `X_1 → X_2 → X_3 → X_1`. Then no nonzero proper
> subspace `0 ≠ V ⊂ H` is simultaneously invariant under
> `{P_{X_1}, P_{X_2}, P_{X_3}}` and under `sigma`.

The proof-walk uses only:

1. The retained distinct-translation-characters narrow theorem (T_x,
   T_y, T_z mutually distinct involutions with three rank-1 joint
   eigenlines summing to I_3).
2. The retained M_3(C) Burnside narrow theorem
   (`<sigma, T_1, T_2, T_3>_alg = M_3(C)` from rank-1 eigenline
   projectors + cyclic permutation).
3. Standard linear algebra (invariance under all rank-1 diagonal
   projectors forces a coordinate subspace, and the 3-cycle has no
   nonempty proper invariant coordinate subset).

The bridge is **independent of the open staggered-Dirac realization
gate**: both retained narrow theorems are pure abstract-`C^3`
statements with no lattice/staggered-Dirac/taste-cube/BZ-corner input.
The hw=1 carrier interpretation of `(X_1, X_2, X_3)` is downstream of
this bridge and does not enter the load-bearing chain. **No new
admissions are introduced** — all inputs come from already-retained
narrow theorems on abstract `C^3`.

This is a bounded proof-walk satisfying the auditor's explicit
"missing_bridge_theorem" hint on the parent
[`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)
(`notes_for_re_audit_if_any`: "provide a retained-grade bridge theorem
establishing the finite hw=1 C^3 carrier, exact translation-character
projectors, and C_3[111] cycle as closed inputs independent of the open
staggered-Dirac/framework-carrier identification"). The bridge supplies
all three named inputs (finite C^3 carrier, translation-character
projectors, cyclic permutation) by composing two retained abstract-C^3
narrow theorems with no routing through the staggered-Dirac gate.

## Proof-walk

| Step | Statement | Load-bearing input |
|---|---|---|
| (B1) | T_x, T_y, T_z mutually distinct commuting diagonal involutions on `C^3` with three distinct joint sign characters `chi(X_i)` | Retained distinct-translation-characters narrow theorem |
| (B2) | Joint sign-projectors `P_i = ((I ± T_x)/2)((I ± T_y)/2)((I ± T_z)/2)` are three rank-1 self-adjoint orthogonal projectors with `Σ P_i = I_3` | (B1) + standard projector arithmetic |
| (B3) | `P_i = P_{X_i}` (the diagonal projector onto `span{X_i}`) | (B2) + rank-1 projector identification |
| (B4) | The order-3 cyclic permutation `sigma: X_1 → X_2 → X_3 → X_1` is well-defined on `H = C^3` for any ordered basis | standard linear algebra |
| (B5) | `<sigma, T_x, T_y, T_z>_alg = M_3(C)` (full matrix algebra generation) | Retained M_3(C) Burnside narrow theorem |
| (B6) | `<sigma, P_{X_1}, P_{X_2}, P_{X_3}>_alg = M_3(C)` (since the P_i are polynomials in the T_a by (B2)) | (B3) + (B5) |
| (B7) | Any subspace `V ⊂ H` invariant under all three rank-1 projectors `P_{X_i}` is a coordinate subspace `span{X_i : i ∈ S}` for some `S ⊆ {1,2,3}` | standard linear algebra |
| (B8) | The order-3 cycle `sigma` has no nonempty proper invariant subset `S`, so no nonzero proper subspace `0 ≠ V ⊂ H` is invariant under both `{P_{X_1}, P_{X_2}, P_{X_3}}` and `sigma` | (B4) + (B7) |

The proof-walk does not cite the Wilson plaquette action, staggered
phases, Brillouin-zone labels, link unitaries, lattice scale `u_0`, a
Monte Carlo measurement, a fitted observational value, the
staggered-Dirac realization gate, the taste-cube `S_3` decomposition,
or any framework-physical-carrier identification.

## Exact arithmetic check

Joint sign-projectors (verified by direct multiplication on diagonal
T_x, T_y, T_z):

```text
P_1 = ((I - T_x)/2)((I + T_y)/2)((I + T_z)/2)
    = diag(1, 0, 0),
P_2 = ((I + T_x)/2)((I - T_y)/2)((I + T_z)/2)
    = diag(0, 1, 0),
P_3 = ((I + T_x)/2)((I + T_y)/2)((I - T_z)/2)
    = diag(0, 0, 1).
```

These are exactly the diagonal rank-1 projectors `P_{X_i}` onto the
basis elements.

Cyclic permutation:

```text
sigma  =  [[0, 0, 1],
           [1, 0, 0],
           [0, 1, 0]].
```

Matrix-unit generation (per retained Burnside narrow T2, using
1-indexed indices modulo 3): since `P_j = E_jj` and
`sigma X_j = X_{j+1}`, for `k ≡ i - j (mod 3)` one has

```text
P_i sigma^k P_j = E_ij.
```

Equivalently, `sigma^k P_j = E_ij`; the left factor `P_i` records the
target row and matches the retained Burnside formula. The retained
Burnside narrow theorem proves this generation explicitly; this bridge
just consumes the conclusion.

No-proper-quotient, with the zero-subspace boundary explicit: any
subspace `V ⊂ C^3` invariant under all `E_ij` is invariant under all of
`M_3(C)` (since the `E_ij` span `M_3(C)` as a vector space), and the
regular `M_n(C)`-action on `C^n` has no nonzero proper invariant
subspaces (a standard fact: `M_n(C)` acts irreducibly on `C^n`).
Therefore `V` is either `{0}` or `C^3`, so there is no nonzero proper
invariant subspace.

Equivalently, using only the displayed `P_i` and `sigma`: if `V` is
invariant under all `P_i`, then every component `P_i v` of every
`v ∈ V` also lies in `V`, so `V` is the span of the subset of basis
lines it contains. Invariance under `sigma` forces that subset to be
fixed by the 3-cycle, leaving only the empty subset and all three
basis lines.

## Dependencies

- [`THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md`](THREE_GENERATION_OBSERVABLE_NO_PROPER_QUOTIENT_NARROW_THEOREM_NOTE_2026-05-02.md)
  — the parent whose finite-C^3-carrier-without-staggered-Dirac repair
  hint this bridge closes.
- [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained narrow theorem supplying the three distinct joint sign
  characters and rank-1 sector projectors.
- [`THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_OBSERVABLE_M3C_BURNSIDE_NARROW_THEOREM_NOTE_2026-05-10.md)
  — retained narrow theorem supplying `<sigma, T_1, T_2, T_3>_alg = M_3(C)`.

These are imported authorities for a bounded theorem. The row remains
unaudited until the independent audit lane reviews this note, its
dependencies, and the runner.

## Boundaries

This bridge does **not** close:

- the physical hw=1 carrier identification with the framework
  staggered-Dirac sector (downstream of this bridge — bridge's claim is
  about abstract C^3, valid for any hw=1 realization);
- physical-species interpretation of the three sectors
  `(X_1, X_2, X_3)` (separate downstream identification);
- closure of the broader three-generation matter-content lane;
- any continuum-limit numerical claim such as plaquette, mass, or
  coupling values.

Downstream rows needing the no-proper-quotient property on any finite
`C^3` carrier — including but not restricted to the framework's hw=1
carrier — can now cite this composition bridge directly rather than
routing through the parent's open staggered-Dirac dependency.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/three_gen_no_proper_quotient_via_burnside_characters_runner.py
```

Expected:

```text
TOTAL: PASS=8 FAIL=0
VERDICT: bounded bridge passes; no nonzero proper invariant subspace on
C^3 follows from retained distinct-translation-characters narrow +
retained M_3(C) Burnside narrow by abstract linear algebra.
```
