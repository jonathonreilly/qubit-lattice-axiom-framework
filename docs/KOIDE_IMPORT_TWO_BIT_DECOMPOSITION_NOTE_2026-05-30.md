# Koide: the chiral import dissolves into a native Kähler triple + two independent bits

**Date:** 2026-05-30
**Claim type:** bounded structural localization (positive); corrects a prior framing
**Status:** structural result. Approves no axiom and no import; sets no audit verdict.
The audit lane sets status and the per-block-vs-per-dimension convention tier.
**Primary runner:**
`scripts/frontier_koide_import_two_bit_decomposition_2026_05_30.py`
with cache
`logs/runner-cache/frontier_koide_import_two_bit_decomposition_2026_05_30.txt`.

## Result (one sentence)

The charged-lepton "one chiral import" for `Q=2/3` is **not** a missing symplectic
form and is **not** (mostly) a chiral grading: the generation Kähler triple
`(g, J, omega)` is **fully native**, and the residual import decomposes into **two
provably-independent** scalar data — a `Z_2` **orientation** of `J` (`~20%`) and the
**modulus** `r=1/2` (a per-block-vs-per-dimension **measure** choice, `~80%`, the
load-bearing one).

## (1) The Kähler triple is native — correcting the "missing-ω" framing

The complex structure `Jcs = (C - C^2)/sqrt(3)` is **exactly** the `so(3)/Cl(3)`
generator of the `C_3` rotation about the `(1,1,1)` body diagonal (runner F1):
`exp((2pi/3) Jcs) = C` (residual `0`), with `(1,1,1)/sqrt3` its rotation axis
(`Jcs`'s `0`-eigenvector), `Jcs^2 = -P_doublet`. With the native (isotropic) metric
`g`, the Kähler 2-form `omega = g . Jcs` is a **forced native bivector** — a Kähler
2-form **is** `g∘J` by definition, so native `g` and native `J` make `omega` native
(F2). The holomorphic (Weyl) projector `P_weyl = (1/2)(P_doublet - i Jcs)` is native
and idempotent (F2.2), and the doublet has Frobenius-Schur indicator `0` — it is
**complex-type**, `End_R(doublet) = C` (F3).

This **corrects** the framing of
`KOIDE_GENERATION_HERMITIAN_NOT_KAHLER_NOTE_2026-05-30`: the generation **geometry**
is Kähler (`g, J, omega, P_weyl` all native), not "Hermitian-not-Kähler". That note's
verified fact — the condensate Berezin action `det M` is conjugation-even — is a
statement about the **dynamical action** (it carries no first-order kinetic / Berry
term), **not** about a missing geometric 2-form. The two `omega`'s are different
objects; the geometric one is native, the dynamical activation is the open question
below.

## (2) The residual import = two provably-independent bits

- **bit(i) — orientation.** Which of `±i` (i.e. `±Jcs`) is holomorphic / which Weyl
  half is "particle": `det_C` vs `det_R`, equivalently the signed-`sqrt(m)` sign. A
  single `Z_2` reality/readout datum (cf. `project_koide_signed_vs_singular_value`).
- **bit(ii) — modulus.** `r = |b|^2/a^2 = 1/2`, equivalently equal `C_3`-block energy
  `E_+ = 3a^2 = E_perp = 6|b|^2`, giving `Q = (1+2r)/3 = 2/3` (F6). This is a
  **measure/normalization** datum: the **per-`C_3`-block** count `(mu,nu)=(1,1)` gives
  `r* = nu/(2mu) = 1/2 -> Q=2/3`, the **per-real-dimension** count `(1,2)` gives
  `r*=1 -> Q=1`. It is **not** chirality.

**They are provably independent.** Every `C_3`-circulant mass operator
`H = aI + bC + b-bar C^2` commutes with `Jcs` at **all** `(a,b)`
(`max|[H,Jcs]| = 0`, F4): holomorphy/`det_C` holds at every `r`, so **orienting `J`
never forces `r=1/2`**. Hence no orientation principle (emergent-time arrow, records
pointer, magnetized-flux, spin-helicity, …) can close `Q=2/3` on its own — each
leaves the load-bearing modulus bit untouched.

## (3) The anticommuting-operator class is physically excluded

Over `Sym(R^3)` the anticommutant of `Gamma_chi = (2/3)J - I` is a **2-dim** family
(F5.1), and **every** member has spectrum `{-s, 0, +s}` — one exactly-zero
eigenvalue = a **massless generation** (F5.2). So even the non-`C_3`-equivariant
anticommuting class — the escape hatch of the retained_bounded
`koide_z3_equivariant_anticommuting_no_go` (which is scope-limited to the
`C_3`-equivariant class) — **cannot** be the charged-lepton mass operator. This is a
**physical** closure of that hatch (a massless charged lepton is excluded), distinct
from the formal equivariance obstruction. (Relatedly, the retained
`koide_anticommuting_operator_derivation` is an `iff` re-encoding of
`<v|Gamma_chi|v> = 0`, with its operator built **from** `v` — so "the only missing
object is an anticommutant" supplies the answer it seeks.)

## Boundary

This is **not** a closure of `Q=2/3`. It sharpens the residual from the diffuse "one
chiral import" to: `~80%` a per-block-vs-per-dimension **measure** choice (the
modulus, bit ii) and `~20%` a single **orientation** sign (bit i), with the entire
Kähler **geometry** native. The framework reproduces `Q=2/3` (`<0.05%`), so each bit
has a derivation to be found.

**Tier.** `W1 = koide_z3_equivariant_anticommuting_no_go` is retained_bounded and (by
its own `claim_scope` "inside `Sym(R^3)`", plus its line-21 disclaimer and line-186
escape hatch) is scope-limited to the `C_3`-equivariant class. The kappa-block
identities `E_+=3a^2`, `E_perp=6|b|^2` are retained. The measure-selection authority
is open: `koide_frobenius_isotype_split_uniqueness` (retained_no_go) states it "needs
an external authority fixing the isotype-weight ratio." Several previously-cited
walls on this question (the `anomaly_forces_time` / `a3_route3` / `abj_epsilon_index`
families) are **unaudited** on the live ledger — they are named for context, not
load-bearing here.

**The next path** (a single physics question, not a missing operator): does
emergent-time's quantization measure (`single_clock_stone_finite_dim_uniqueness`
retained; `staggered_dirac_substep2_kahler_dirac_equivalence` retained_bounded,
holomorphic first-order field) count the generation factor **per-complex-mode**
w.r.t. the native `Jcs` (one complex doublet mode + one real singlet mode = the
per-block measure `-> r=1/2 -> Q=2/3`) or **per-real-dimension** (`-> r=1 -> Q=1`)?
The bit-ii residual converts the "two canonical measures, rep theory ranks neither"
impasse into one concrete identification: which factor does emergent-time's `i` land
on. Do **not** route through the `arg(b)`/Goldstone/cubic sector (proven decoupled
from `r`) or through any `Gamma_chi`-anticommuting operator (forces a massless
generation).

## Anchors (live-ledger tiers)

retained / retained_bounded / retained_no_go: `koide_z3_equivariant_anticommuting_no_go`
(retained_bounded, scope-limited), `koide_frobenius_isotype_split_uniqueness`
(retained_no_go), `koide_circulant_q_two_thirds_algebraic`,
`koide_anticommuting_operator_derivation`, `single_clock_stone_finite_dim_uniqueness`,
`staggered_dirac_substep2_kahler_dirac_equivalence` (retained_bounded),
`cpt_exact_real_anti_hermitian_d`, `site_phase_cube_shift_intertwiner`.
