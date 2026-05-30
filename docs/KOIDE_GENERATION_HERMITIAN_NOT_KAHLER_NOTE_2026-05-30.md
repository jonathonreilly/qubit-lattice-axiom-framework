# Koide: the native generation geometry is Hermitian, not Kähler

**Date:** 2026-05-30
**Claim type:** bounded_theorem / structural localization (positive)
**Status:** structural result. Approves no axiom and no import; sets no audit
verdict. The audit lane sets status and the Hermitian-vs-Kähler convention tier.
**Primary runner:**
`scripts/frontier_koide_generation_hermitian_not_kahler_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_generation_hermitian_not_kahler_2026_05_30.txt`.

## Result (one sentence)

The whole charged-lepton Koide-value pin — the value `Q=2/3`, the field-count,
the isotype weight, and the generation chirality — reduces to a single
differential-geometric object: whether the native generation matter geometry is a
**Hermitian pair** `(g, J)` or a **Kähler triple** `(g, J, omega)`. The framework's
native action supplies `(g, J)` but **not** the symplectic form `omega`, and that
missing `omega` is exactly the chiral import.

## The reduction

The charged-lepton value is `Q=2/3 <=> r=|b|^2/a^2=1/2`, where `a` is the uniform
(singlet) and `b in C` the doublet `C_3`-isotype amplitude of `Y = a I + b(J-I)`
on the `hw=1` generation triplet. This holds in the native signed (Brannen/`det_R`)
readout `Q=(1+2r)/3`, which is **`theta=arg(b)`-independent**. The value is
therefore set by the doublet **field-count**:

- `b` carried as **one complex/holomorphic field** (`theta` = the momentum
  conjugate to `|b|`, not an independent coordinate): field-count 1, `r=1/2`,
  `Q=2/3`, and `b` is chiral.
- `b` carried as **two real fields** (`Re b, Im b` independent): field-count 2,
  `r=1`, `Q=1`.

## What the native dynamics supplies, and what it lacks

Verified (runner):

1. **Complex structure `J`.** `J = (C - C^2)/sqrt(3)` satisfies `J^2 = -P_doublet`
   and `J P_singlet = 0`: a genuine complex structure on the doublet, and the
   generator of the `theta=arg(b)` rotation.
2. **Kähler metric `g`.** The doublet Frobenius norm is **isotropic**:
   `||M_perp||_F^2 = 6|b|^2 = 6(x^2+y^2)` (`b=x+iy`), i.e. a flat Kähler metric
   `g = 6(dx^2 + dy^2)`.
3. **No symplectic form `omega`.** The native condensate effective action
   `S = -log det M` over the retained **real** anti-Hermitian Dirac operator
   (`cpt_exact_real_anti_hermitian_d`, `spin_statistics_berezin_determinant`,
   both retained_bounded) is **conjugation-even**: `det M(conj b) = det M(b)`
   identically (`det M = a^3 - 3a(x^2+y^2) + 2x^3 - 6xy^2`). A conjugation-even
   real scalar action carries no first-order (time-antisymmetric) Berry term,
   hence no `omega = dRe(b) ^ dIm(b)`.

So the native geometry is `(g, J)` **with no `omega`**: a Hermitian pair, not a
Kähler triple. Without `omega` the `J`-flow (the `theta`-orbit) is an **isometry**,
not a Hamiltonian flow; `theta` then has its own second-order kinetic term and its
own conjugate momentum `p_theta != |b|^2` — an **independent coordinate** —
field-count 2 — `Q=1`.

This matches the spectrum: at the value point, turning `theta` on at fixed `|b|`
splits the doublet into three genuinely distinct masses while `Q` stays `2/3`
(verified `theta`-invariant), and the observed `m_mu != m_tau` forces `theta != 0`
populated — the textbook signature of `theta` being an independent recorded
coordinate (count 2).

## The missing object is the chiral import (one object, shared gate)

`omega` present `<=>` field-count 1 `<=>` `Q=2/3` `<=>` `b` chiral. Supplying
`omega` is equivalent to a chiral bilinear with a generation grading `Gamma_chi`
anticommuting with the native coupling `B = C + C^2`. This is **non-native**:
`B` has spectrum `{2, -1, -1}`, which is not `lambda <-> -lambda` symmetric
(`spec(B) != spec(-B)`), so no `G` with `G^2=I` anticommutes with `B` (runner) —
the `koide_z3_equivariant_anticommuting_no_go` wall, re-derived at the
field-reality level. The only continuous `U(1)` touching `b` natively is `U(1)_V`,
under which the neutral bilinear `b` is invariant (not its Goldstone); the
corner-momentum translation is a discrete `Z_2`. So `theta` has no native
continuous `U(1)` to make it a conjugate momentum.

The same missing `omega` is the grading the **generation-identification chirality**
gate needs: the two are one object.

## Boundary

This is **not** a no-go on `Q=2/3`. It localizes the pin: the native *retained*
action is Hermitian (`omega` absent), so the *retained* surface gives field-count
2 (`Q=1` by the dimension reading). But the framework reproduces `Q=2/3` to
`<0.05%`, so the **true** (as-yet-underived) matter action is Kähler — it has
`omega`. The note does **not** privilege `Q=1`: the block-count reading giving the
observed `2/3` is unsupplied, not refuted (the trace-vs-block-count weight remains
unranked, `koide_q23_block_weight_frontier`).

The next path (a distinct program, not claimed here): build the **bridge-gap
matter action** from `A1+A2` (`Cl(3)/Z^3`, the HK/Casimir-native candidate, not the
imported Wilson) and test whether its generation sector is **Kähler** — in
particular whether the **emergent (records/growth) time** gives `b` a *first-order*
(Schrödinger/Bargmann) kinetic term `int b-bar i d_tau b` (which *is* `omega`)
rather than a second-order relativistic one, and whether its `beta`-function has an
`r=1/2` fixed point.

## Relation to Koide

This supersedes the diffuse "which measure / which counting rule" framing of the
charged-lepton value with one exact statement: the value, the chirality, and the
field-count are a single fact about the generation matter action — **is its
generation sector Kähler (`omega` present) or only Hermitian?** Counting is not a
measure one chooses; it is fixed by whether the action carries `omega`.
