# Koide: the native Kähler-Dirac form-degree coupling is a Berry spectator on the generation doublet

**Date:** 2026-05-31
**Claim type:** bounded_theorem — narrow spectator/negative result with one positive structural addition
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status. Consistent with and strengthening
`koide_z3_equivariant_anticommuting_no_go` (retained_bounded).
**Primary runner:**
`scripts/frontier_koide_dkd_berry_spectator_2026_05_31.py`
with cache
`logs/runner-cache/frontier_koide_dkd_berry_spectator_2026_05_31.txt`.

## Result (one sentence)

The most native off-generation candidate for sourcing the Koide chiral monopole — the
**form-degree** structure of the native Kähler-Dirac field — genuinely realizes the
no-go's distinct-factor escape hatch (a native chiral grading), yet `i*D_KD` transmits
**zero** Berry curvature to the generation doublet, so it reproduces the `Q=1` default,
not `Q=2/3`.

## Context

This session reduced the charged-lepton Koide value to one criterion: `Q=2/3 <=>` the
generation mass is chiral (nonzero Berry monopole on the complex-`b` plane); `Q=1 <=>`
non-chiral (zero Berry). The chiral grading is forbidden on the generation `R^3` by
`C^3=I` (`koide_z3_equivariant_anticommuting_no_go`: `comm(C) ∩ anticomm(Gamma_chi)={0}`
inside `Sym(R^3)`). The open door is a tensor factor **distinct** from the generation
`R^3`; the most native candidate is the form-degree / Fock-parity factor.

## What is native (the positive)

On the 3-mode Jordan-Wigner Fock space `V = Lambda*(C^3)` (dim 8; CAR, `d^2=delta^2=0`,
`i*D_KD = i*sum_k(a_k^dag - a_k)` Hermitian — F1), the Fock/form-parity grading
`Gamma_F = (-1)^N` **anticommutes** with `i*D_KD`: `{i*D_KD, Gamma_F} = 0` (F2). This is
a genuine `Gamma_chi`-anticommuting chiral grading on a factor **distinct** from the
generation `R^3` — exactly escape-hatch II of the controlling no-go — and `C^3=I` does
not touch it.

## Why the native monopole is exactly zero (the spectator mechanism)

With the Koide circulant mass `M[b] = aI + bC + b-bar C^2` on `Lambda^1` (the generation
triplet), the two `b`-derivative directions **commute** (F3):
`[dH/dRe b, dH/dIm b] = [C+C^2, i(C-C^2)] = 0` (because `C` and `C^2` commute). The
native `d-delta` coupling of `Lambda^1` to `Lambda^0, Lambda^2` is **real and
`b`-independent**, so `b` enters only a real diagonal energy `a + 2 Re(b omega)`, never a
complex off-diagonal element — the `d`-vector traces a line (zero solid angle).
Consequently the Wilson-loop Berry phase of `H(b) = kappa*(i*D_KD) + M[b]` on the
complex-`b` plane is **0** for every `kappa` and every band (F4.1), while a positive
control (a chiral 2-band with non-commuting `b`-couplings) gives a nonzero monopole,
proving the method detects curvature (F4.2). The same `C_3`-equivariance that gives the
generation count `3` (`[i*D_KD, U_C]=0`) forbids the monopole — `i*D_KD` is a **Berry
spectator** on `b`.

Moreover the native grading `Gamma_F` restricts to the **scalar** `-I` on `Lambda^1`
(F5), so it cannot impose the Koide condition `<v|Gamma_chi|v>=0`; the grading that
reads Koide (`Gamma_chi=(2/3)J-I`, eigenvalues `+1,-1,-1`) lives on the generation `R^3`,
where `{C, Gamma_chi} != 0`.

## Boundary

This is **not** a closure of the Koide value. It is a clean, non-circular negative on
**one** off-generation factor (form-degree), with a real positive (the distinct-factor
escape hatch is genuinely realized natively). A nonzero off-generation monopole still
needs `arg(b)` in an **off-diagonal, complex, `b`-dependent** inter-grade coupling (a
relative-`i` breaking the CPT reality) — the **same** import the qubit route needs
(`KOIDE_QUBIT_BERRY_HOLONOMY_IMPORT_NOTE`), and which is `r`-non-selective even when
imported. So the form-degree route is **not** different from the qubit route on the
load-bearing point.

**The next path** (open, uncomputed): does emergent-time's complex unit `i`
(`single_clock_stone_finite_dim_uniqueness`, retained) land on the form-parity factor
and make the `Lambda^1 <-> Lambda^0/Lambda^2` coupling itself carry `arg(b)` — turning
the real diagonal energy into a complex off-diagonal inter-grade coupling — **without** a
chosen `sigma_x/sigma_y`? That is the one place the CPT reality could break without an
import. (Separately, what fixes `r=|b|^2/a^2=1/2` directly remains the deeper gate, which
even a working chiral grading would not by itself discharge.)

## Anchors (live-ledger tiers)

retained / retained_bounded: `koide_z3_equivariant_anticommuting_no_go` (retained_bounded),
`koide_anticommuting_operator_derivation`, `staggered_dirac_substep2_kahler_dirac_equivalence`
(retained_bounded), `single_clock_stone_finite_dim_uniqueness`,
`koide_circulant_q_two_thirds_algebraic`. Complements
`KOIDE_BERRY_MONOPOLE_BRIDGE_REDUCTION_NOTE` and `KOIDE_QUBIT_BERRY_HOLONOMY_IMPORT_NOTE`.
