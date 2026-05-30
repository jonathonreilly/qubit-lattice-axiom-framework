# BH Entropy RT-Ratio Widom No-Go Theorem

**Date:** 2026-04-17 (last rigorization 2026-05-10; 2026-05-18:
claim_scope narrowed per audit verdict "Claim boundary until fixed"
instruction; 2026-05-25: claim further narrowed to finite-`L ≤ 64`
numerical-fit evidence per audit verdict "the runner's THEOREM check
is only a numerical fit check and does not prove the asymptotic
statement.").
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-25 narrowing):** the load-bearing content
of this note is **the Widom entropy coefficient `1/6` on the
self-contained free-fermion carrier defined intrinsically in
§"Self-contained carrier definition"** plus the **finite-`L ≤ 64`
numerical-fit evidence against the exact `1/4` ratio** under the
stated `10^-6` relative singular-value threshold on the OBC
half-filled square-lattice carrier. The runner is a **numerical fit
check** at finite `L ≤ 64`; it does **not** prove any asymptotic
statement. Consistent with the audit verdict
("the runner's THEOREM check is only a numerical fit check and
does not prove the asymptotic statement"), the asymptotic
`lim_L r(L) = c_Widom != 1/4` is **moved out** of the retained
no-go and into open admission OA-1 below. The L ≤ 96 probe claim
(via `scripts/probe_bh_rt_ratio_asymptotic.py`) is **explicitly
deferred** as cache-not-in-packet, pending a future runner extension
that ships the probe cache alongside the note. The `d = 3`
normalization wording will be corrected or split in a separate
revision before any future retained-grade promotion attempt.
**Status authority:** independent audit lane only.
**Status:** narrow finite-`L ≤ 64` numerical-fit-evidence no-go on a
self-contained free-fermion carrier
**Runner:** `scripts/frontier_bh_entropy_rt_ratio_widom.py`
**Authority role:** canonical closure of the "is RT ratio = 1/4 exact?" question
on the self-contained carrier defined intrinsically below. The existing
BH entropy companion (`BH_ENTROPY_DERIVED_NOTE.md`, downstream consumer;
backticked to avoid length-2 cycle — citation graph direction is *downstream → upstream*)
is a downstream citation, not an upstream dependency.

## Audit-driven scope narrowing (2026-05-10)

The 2026-05-05 audit verdict (`audited_conditional`,
`auditor_confidence: high`) ruled the no-go *internally* sound (the Widom
diamond integral closes, the runner is substantive) but flagged that the
*carrier-and-readout* definition was being **imported** from the
`audited_conditional` upstream `BH_ENTROPY_DERIVED_NOTE.md`. The audit's
explicit repair instruction:

> "dependency_not_retained: retain or replace
> docs/BH_ENTROPY_DERIVED_NOTE.md as the carrier/readout authority,
> **or provide a self-contained bridge proving that the runner's
> lattice, cut, chi_eff=L readout, and Widom asymptotic are exactly
> the current lane's objects.**"

This revision takes the second path: the carrier, cut, and chi_eff readout
are now **defined intrinsically inside this packet** (see Section "Self-
contained carrier definition" below), and the "Self-contained carrier
bridge" section establishes the carrier-Widom match using only standard
free-fermion Bloch theory + cited classical Widom-Sobolev theorems, both
of which were already on the note's accepted-authority list. The bounded
lane in `BH_ENTROPY_DERIVED_NOTE.md` is now relegated to a downstream
observational citation: it cites this no-go as the reason it cannot
promote, but this no-go does not import its carrier from there.

## 2026-05-19 audit-conditional repair

A follow-up audit pass on this `audited_conditional` row of the
publication surface (post-2026-05-18 campaign) confirmed the prior
2026-05-18 narrowing direction but identified two specific load-bearing
claims that are **not** discharged by the in-packet material to the
standard required for retained-grade closure. They are therefore moved
to **open admissions** here; the retained scope of the note is
correspondingly tightened.

### Open admission OA-1: asymptotic all-L no-go

The leading no-go statement of the form

```
        lim   r(L)   =   c_Widom   !=   1/4
       L->inf
```

(equations preceding (B-4.4) and the "Conclusion of the no-go"
paragraph) is **promoted to an open admission**. The 2D diamond-integral
evaluation `c_Widom(2D) = 1/6` is exact and is retained; what is
admitted-open is the **all-L limit** identification of `r(L)` with
`c_Widom`. The classical Widom-Gioev-Klich theorem (W-1) is cited in
the form rigorously proved by Helling-Leschke-Spitzer 2011 on `R^d` and
its uniform extension to the lattice setup (C-1)-(C-6) is *asserted*
in bridge step (B-2). A fully audited lattice specialization with
uniform error bounds against the OBC straight-cut geometry (C-5) is
**not** carried in this packet. The asymptotic statement therefore
ceases to be load-bearing for retained-grade closure; it is reverted
to the status of an audited-conditional conjecture, conditional on a
future packet that supplies the missing uniform OBC-lattice version of
(W-1) with explicit subleading bounds.

### Open admission OA-2: C-7 / B-3 threshold bridge

The intrinsic boundary-layer transfer-rank statement

```
       chi_eff(L)  =  L^{d-1} (1 + o(1)),       lim  chi_eff(L) / L^{d-1} = 1
                                                L->inf
```

i.e., bridge step (B-3), is **promoted to an open admission**.
Section "Self-contained carrier definition" (C-7) defines `chi_eff(L)`
by the *non-standard* singular-value threshold
`sigma_k / sigma_max > 10^{-6}`, and (B-3) argues by appeal to
"standard free-fermion area-law scaling" plus Widom log-violation that
the boundary-layer cross-correlation matrix saturates rank
`L^{d-1}`. The numerical observation `chi_eff(64) = 64` (2D, OBC,
half-filling, threshold `10^{-6}`) is retained as **finite-`L`
evidence**, but the all-`L` saturation argument is not closed at
retained grade inside this packet: a proof would require either (i)
diagonalization of the transverse-mode boundary-layer transfer operator
and explicit lower bounds on its `L^{d-1}` significant singular values
above the `10^{-6}` cutoff, or (ii) an independent reduction to a known
exact-rank statement for the half-filled NN-hopping ground state's
boundary-layer correlator. Neither is supplied here. The threshold-
bridge step is therefore admitted-open; the **finite-`L` numerical
saturation `chi_eff(L) = L` for `L <= 64`** is retained as evidence,
not as theorem.

### Retained scope (post-2026-05-19)

After the two admissions above, the **retained** load-bearing content
of this note is restricted to:

- **R1.** The exact 2D diamond-integral evaluation
  `c_Widom(2D, diamond, straight cut) = 1/6` (Section "What is proved",
  Step 2), as a direct evaluation of the cited Widom-Gioev-Klich
  coefficient integral on the `|k_x| + |k_y| = pi` Fermi surface with
  the straight-cut unit normal `n_x = (1, 0)`. This step uses only
  Euclidean geometry of the diamond and the explicit formula
  `(1/(12 (2 pi)^{d-1}))` from (W-1) and is independent of
  admissions OA-1, OA-2.
- **R2.** The **finite-`L ≤ 64` numerical-fit evidence** for the
  no-go (`L = 8, 12, ..., 64`, OBC, half filling, straight cut,
  threshold `10^{-6}`, runner cache in packet): `r(64) = 0.2112`, the
  two-parameter fit `r(L) = c_inf + a / ln L` over `L >= 32` gives
  `c_inf = 0.1601` (3.94% from `1/6`, 35.96% from `1/4`). This is
  finite-`L` numerical-fit evidence (not a theorem) inconsistent with
  the `1/4` value within the stated lattice range, and is retained as
  bounded numerical-fit evidence on `L <= 64`. The runner's `THEOREM`
  label denotes the numerical fit-form check at finite `L`; it is
  **not** a proof of the asymptotic statement.

The retained statement reads:

> On the OBC half-filled NN-hopping square lattice (C-1)-(C-8) with
> threshold `10^{-6}`, the dimensionless RT ratio `r(L)` is bounded
> through `L = 64` by `r(L) <= 0.224`, decreases monotonically for
> `L >= 28`, and a two-parameter Widom-form fit on `L >= 32` gives
> `c_inf = 0.1601` (3.94% from the 2D diamond-integral value `1/6`
> and 35.96% from `1/4`). The exact 2D diamond-integral Widom
> coefficient is `c_Widom(2D, diamond, straight cut) = 1/6` by
> direct evaluation of the cited Widom-Gioev-Klich integral.

**Deferred (cache-not-in-packet):** the extended `L <= 96` probe
(via `scripts/probe_bh_rt_ratio_asymptotic.py`) reporting
`c_inf = 0.163` (2.1% from `1/6`, 34.7% from `1/4`) is **explicitly
deferred** from the retained scope of this note: the L ≤ 96 cache
is not bundled in the current audit packet, so any claim sourced
from that probe is pending a future runner extension that ships
the probe cache alongside the note. Until then, the retained
finite-L numerical-fit evidence is the `L <= 64` runner cache
only.

### No-go discipline notes

This narrowing is a **strict shrinkage of the no-go scope**, not a
broadening, in conformance with the N1-N8 no-go discipline:

- the asymptotic claim `lim_L r(L) != 1/4` is **moved out** of the
  retained no-go and into an open admission (OA-1) — the no-go is
  **less ambitious**, not more
- the C-7 / B-3 threshold-bridge step is **moved out** of the retained
  no-go and into an open admission (OA-2) — the no-go's reach is
  **smaller**, not larger
- the only retained claims (R1, R2) are weaker than the prior
  asymptotic statement: R1 is an exact evaluation of a classical
  integral, R2 is a finite-`L` numerical-fit evidence bound through
  `L = 64` (the L ≤ 96 probe is explicitly deferred as cache-not-in-
  packet, per the 2026-05-25 narrowing)
- no new asymptotic conclusion, no new universal reach, and no new
  class of carriers is added; the carrier class (C-1)-(C-8) is left
  intact and the open-admissions OA-1, OA-2 are explicitly named
  conditional inputs

Consequently, every prior consumer of this note (the bounded BH-entropy
companion `BH_ENTROPY_DERIVED_NOTE.md` chief among them) inherits a
**narrower** obstacle than before, not a broader one: the narrowed no-go
forbids the `1/4` value only on `L <= 64` (the runner cache in packet)
in the OBC half-filled NN-hopping carrier and only at the level of the
diamond-integral Widom coefficient `1/6`, leaving the all-`L`, the
threshold-bridge, and the `L <= 96` probe questions explicitly open
for future packets to close.

**N1-N8 review-loop gate (2026-05-25).** PASS for the narrowed
finite-`L <= 64` evidence boundary only.

- **N1 alternative routes considered.** (1) all-`L` Widom/OBC
  asymptotic bridge: not closed, moved to OA-1; (2) thresholded
  `chi_eff` rank saturation: not closed, moved to OA-2; (3) extended
  `L <= 96` probe: not in packet, deferred as cache-not-in-packet; (4)
  alternate carriers / fillings / cuts that could hit `1/4`: explicitly
  outside this carrier-specific packet; (5) physical Einstein-Hilbert
  `1/4` route: outside scope; (6) in-packet finite-`L <= 64` runner
  evidence: retained as bounded numerical-fit evidence only.
- **N2 wall independence.** OA-1 and OA-2 are distinct missing bridges;
  the `L <= 96` issue is an artifact-packet/cache gap, not an independent
  physics wall.
- **N3 hidden-wall scan.** Prior "standard free-fermion area-law" and
  "direct lattice specialization" language is no longer hidden
  authority; those steps are explicitly assigned to OA-1/OA-2.
- **N4 residual matching.** The retained residual is finite
  `L <= 64` inconsistency with exact `1/4` under the runner's declared
  fit/readout. The note no longer uses that residual as proof of an
  all-`L` asymptotic no-go.
- **N5 rhetoric audit.** Publication wording is narrowed away from
  "hard obstacle" and all-`L` "asymptotic value is..." phrasing.
- **N6 partial-closure path scan.** No new axiom is requested. The repair
  path is mathematical: supply uniform OBC-lattice Widom specialization
  and threshold-rank bounds, or change the carrier/readout.
- **N7 steelman.** A hostile reviewer can object that finite `L <= 64`
  fits do not prove `lim_L r(L) != 1/4`; this objection is accepted and
  the asymptotic statement is moved out of the retained scope.
- **N8 cross-cycle echo.** Prior area-law/no-go packets overclosed
  selector/carrier claims from finite numerics. This narrowed packet
  preserves the finite evidence without using it to foreclose future
  asymptotic or alternate-carrier work.

## Self-contained carrier definition

Independent of any other note in the repo, define the carrier as follows.

**(C-1)** The lattice: the open-boundary square lattice `Lambda_L = {0,
1, ..., L-1}^2` with `L >= 8` even, and its 3D analogue `Lambda_L^{(3)}
= {0, ..., L-1}^3`.

**(C-2)** The Hamiltonian: the standard free-fermion nearest-neighbor
tight-binding Hamiltonian with hopping `t = 1`, in second-quantized
form

```
H = -t * sum_{<i,j>} (c_i^dag c_j + c_j^dag c_i)            (C-2.1)
```

where `<i,j>` runs over nearest-neighbor pairs of `Lambda_L`. Concretely
this is a real symmetric `N x N` matrix `H_{ij} = -t` if `i,j` are
nearest neighbors and `0` otherwise, with `N = L^d` (`d in {2, 3}`).

**(C-3)** The state: the ground state at half filling. With single-
particle eigenpairs `(epsilon_alpha, |phi_alpha>)` from `eigh(H)`,
the half-filled ground state is the Slater determinant of the lowest
`N/2` orbitals, i.e. fill all states with `epsilon_alpha < 0`.

**(C-4)** The single-particle correlation matrix:

```
C_{ij} = <c_i^dag c_j>  =  sum_{alpha=1..N/2} phi_alpha(i) phi_alpha(j).
                                                              (C-4.1)
```

This is the unique input the entanglement entropy depends on, by
Peschel's theorem (Peschel 2003).

**(C-5)** The cut: the straight bipartition with subsystem
`A = {(x,y) in Lambda_L : x < L/2}` (and its 3D analogue with the
straight plane `x < L/2`).

**(C-6)** The entanglement entropy from the Schur-complement /
determinant formula:

```
S_ent(L)  =  - tr_A [ C_A log C_A + (I - C_A) log (I - C_A) ]
                                                              (C-6.1)
```

where `C_A` is the principal submatrix of `C` indexed by `A`. This is
the standard free-fermion entanglement entropy via the restricted
correlation matrix (Peschel 2003; Cheong-Henley 2004).

**(C-7)** The transfer rank: define the layer `L_x = {(x, y) : y =
0, ..., L-1}` for fixed `x`. The free-fermion transfer matrix between
adjacent layers `T_{x | x-1}` is the principal submatrix of `C` with
rows in layer `L_x` and columns in layer `L_{x-1}`. Define

```
chi_eff(L)  =  #{ singular values sigma_k(T)
                  with sigma_k / sigma_max > 10^{-6} }.        (C-7.1)
```

For the free-fermion ground state above this is the boundary-layer
rank. The runner verifies the finite-`L <= 64` 2D saturation used by
the numerical-fit evidence; the all-`L` leading-order statement
`chi_eff(L) = L` (resp. `L^{d-1}` in 3D) is part of open admission
OA-2, not retained by this packet.

**(C-8)** The dimensionless RT-ratio:

```
r(L)  =  S_ent(L) / (L * ln chi_eff(L))            (in 2D)     (C-8.1)
r(L)  =  S_ent(L) / (L^{d-1} * ln chi_eff(L))    (in d dims).  (C-8.2)
```

This is the **only** dimensionless number this narrowed packet is about.
It is fully determined by the data (C-2)-(C-7); no external lane
authority is needed to specify any of the seven inputs.

## Safe statement (narrowed)

Let `r(L)` be defined exactly by (C-1)-(C-8) above. The retained
safe statement in this packet is finite:

- the 2D diamond Widom coefficient evaluates exactly to `1/6` for the
  half-filled square-lattice Fermi surface and straight cut;
- the paired runner gives finite-`L <= 64` numerical-fit evidence
  against the exact `1/4` ratio on the stated OBC carrier and threshold;
- the all-`L` bridge from the carrier and thresholded `chi_eff` readout
  to `lim_L r(L) = c_Widom` is open admission OA-1/OA-2, not retained
  by this packet.

On the 2D square-lattice half-filled Fermi surface (the diamond
`|k_x| + |k_y| = pi`):

```
        c_Widom(2D, diamond, straight cut) = 1 / 6
```

exactly (see Section "What is proved", Step 2). The 3D cubic
half-filled analogue gives `c_Widom(3D) ~ 0.105` as a numerical
consistency check, but no 3D all-`L` no-go is retained here.

**Finite conclusion.** On the self-contained carrier (C-1)-(C-8), the
in-packet runner supports the statement that the tested finite range
`L <= 64` is inconsistent with an exact `1/4` RT ratio under the stated
fit/readout protocol. The stronger asymptotic statement is deferred to
future work that supplies OA-1 and OA-2.

## Open self-contained carrier bridge

The audit-driven repair of 2026-05-10 demanded a self-contained
carrier-to-Widom asymptotic bridge. The following subsections record the
proposed route and identify which pieces are exact versus open. They are
not retained as an all-`L` asymptotic proof by this packet; OA-1 and OA-2
above name the missing uniform OBC-lattice and threshold-rank work.

**Bridge step B-1 (carrier symbol identification).** The
nearest-neighbor tight-binding Hamiltonian of (C-2) on the infinite-
volume `Z^d` lattice is translation-invariant, so its Bloch
diagonalization gives the dispersion

```
epsilon(k) = -2 t (cos k_1 + cos k_2 + ... + cos k_d),
       k in BZ = (-pi, pi]^d,                                  (B-1.1)
```

with eigenvalues filling `[-2 t d, +2 t d]`. At half filling the Fermi
energy is `epsilon_F = 0`, so the Fermi surface is

```
F = {k in BZ : cos k_1 + cos k_2 + ... + cos k_d = 0}.         (B-1.2)
```

In `d = 2` this is the open diamond `|k_1| + |k_2| = pi` (perimeter
`4 sqrt(2) pi`). In `d = 3` it is a smooth surface bounded by the
hyperplane `cos k_1 + cos k_2 + cos k_3 = 0` (numerically a "rounded
cube"). Both are precisely the surfaces appearing in the Widom
asymptotic of (W-1) below.

**Bridge step B-2 (free-fermion entanglement reduces to truncated
Wiener-Hopf).** By Peschel's theorem (Peschel 2003) and its standard
extension to gapless free fermions, the entanglement entropy (C-6) of
a Slater determinant is fully determined by the spectrum of the
restricted correlation matrix `C_A`. The asymptotic spectral density
of `C_A` for a Bloch-translation-invariant correlation kernel
restricted to a domain `Omega = (a/L)^d * (subset of [0,1]^d)` is the
content of the Widom-Sobolev / Gioev-Klich / Helling-Leschke-Spitzer
theorem, which states

```
S_Omega(L; F) = (1 / (12 (2 pi)^{d-1}))
              * (integral_{∂Omega rescaled} integral_{∂F} |n_x . n_k|
                                               dS_k dS_x) * L^{d-1} ln L
              + o(L^{d-1} ln L)                                (W-1)
```

uniformly in the volume `L^d` and over Lipschitz domains `Omega`.
This is Theorem 1.1 of Helling-Leschke-Spitzer 2011 (the rigorous proof
of the Widom 1982 / Gioev-Klich 2006 conjecture on `R^d`). The
specialization to the OBC lattice setup (C-1)-(C-6) with explicit
uniform error bounds is the open OA-1 bridge, not a retained conclusion
of this packet.

**Bridge step B-3 (chi_eff = L scaling, intrinsic).** The transfer
rank (C-7) on a half-filled free-fermion ground state is determined
by the boundary layer's restricted correlation matrix. For the open-
boundary lattice (C-1) with the straight cut (C-5), the boundary
layer `L_{L/2}` has `L^{d-1}` sites. Standard free-fermion area-law
scaling implies the cross-layer correlation matrix `T_{L/2 | L/2-1}
= C[L_{L/2}, L_{L/2-1}]` has `O(L^{d-1})` significant singular
values: the entanglement spectrum cannot have rank exceeding the
layer dimension itself, and the Widom log-violation of the area law
forces the rank to saturate `L^{d-1}` to leading order. Numerically
verified at `L = 64` (2D): `chi_eff(64) = 64` exactly, with the
threshold `sigma_k / sigma_max > 10^{-6}` holding for all `k =
1..L`. Thus

```
chi_eff(L) = L^{d-1} (1 + o(1))                                (B-3.1)
ln chi_eff(L) = (d-1) ln L (1 + o(1)).                         (B-3.2)
```

This would be intrinsic to the carrier (C-1)-(C-7) once proved, but the
uniform threshold-rank bridge is OA-2 and remains open in this packet.

**Bridge step B-4 (carrier-Widom match).** Combining (W-1), (B-1.2),
(C-5), and (B-3) on the carrier (C-1)-(C-8):

```
S_ent(L)        = c_Widom(d, F_d, straight cut) * L^{d-1} * ln L
                  + o(L^{d-1} ln L)                            (B-4.1)
L^{d-1} * ln chi_eff(L)
                = (d-1) * L^{d-1} * ln L + o(L^{d-1} ln L)     (B-4.2)
```

In `d = 2` (which the runner uses as the primary verdict): `(d-1) =
1`, so

```
r(L) = S_ent(L) / (L * ln chi_eff(L))
     = c_Widom(2D) + a / ln L + b / L + ...                    (B-4.3)
     -> c_Widom(2D)  as L -> inf.                              (B-4.4)
```

In `d = 3` the analogous combination gives `r(L) -> c_Widom(3D) /
(d - 1) = c_Widom(3D) / 2` under the (C-8.2) normalization
(numerator `L^{d-1} ln L = L^2 ln L`, denominator `L^{d-1} *
ln chi_eff = L^2 * (d-1) ln L = 2 L^2 ln L`). With `c_Widom(3D)
~ 0.105`, this gives `r_inf(3D) ~ 0.053`, comfortably distinct
from `1/4 = 0.25`. These are open asymptotic consequences conditional
on OA-1/OA-2, not retained no-go statements in this packet.

The proposed bridge (B-1)-(B-4) no longer imports from
`BH_ENTROPY_DERIVED_NOTE.md` (or any other lane note), but the
carrier-Widom all-`L` match still requires the missing OA-1/OA-2 proof
work before it can become retained-grade.

## What is proved

Retained within this packet, on the self-contained carrier (C-1)-(C-8):

1. The Widom-Gioev-Klich theorem for free fermions in `d >= 1` gives

       S_Omega(L; Gamma) = C(d, F, Omega) * L^{d-1} * ln L + o(L^{d-1} ln L)

   with

       C(d, F, Omega)
          = (1 / (12 (2 pi)^{d-1}))
             * integral_{∂Omega} integral_{∂Gamma} |n_x . n_k| dS_k dS_x

   where `∂Omega` is the rescaled unit-domain boundary of the subsystem and
   `∂Gamma` is the Fermi surface in the Brillouin zone.

2. For the `d = 2` carrier (C-1)-(C-8), bridge step (B-1.2) gives the
   Fermi surface `∂Gamma = {|k_x| + |k_y| = pi}` of perimeter
   `4 sqrt(2) pi`, and the cut (C-5) gives the unit-rescaled
   straight-cut boundary `∂Omega = {1/2} x [0, 1]` of length `1`.
   The unit normal to each of the four Fermi-surface segments dotted
   with `n_x = (1, 0)` is `1/sqrt(2)`, so

       integral_{∂Gamma} |n_x . n_k| dS_k  =  4 sqrt(2) pi * (1 / sqrt(2))
                                           =  4 pi,

   hence

       c_Widom(2D) = (1 / (12 * 2 pi)) * 4 pi = 1 / 6.

3. Deferred from retained scope: in the ratio
   `r(L) = S_ent(L) / (L * ln chi_eff(L))` (definition (C-8)) with
   `chi_eff = L`, both `S_ent` and `L * ln chi_eff = L * ln L`
   would scale as `L * ln L` to leading order if OA-1/OA-2 were
   supplied, so

       r(L)  =  c_Widom + a / ln L + b / L + ...
             ->  c_Widom  =  1 / 6    as L -> inf.

   This asymptotic conclusion is not retained by the current packet.

4. Numerical-fit evidence on `L = 8, 12, ..., 64` (dense `eigh`, OBC,
   half filling, straight cut; runner cache in packet) shows `r(L)`
   decreasing monotonically for `L >= 28` from `r(28) = 0.2232` to
   `r(64) = 0.2112`, with the two-parameter fit
   `r(L) = c_inf + a / ln L` over `L >= 32` giving `c_inf = 0.1601`,
   which agrees with `1 / 6 = 0.1667` to `3.94%` and disagrees with
   `1 / 4` by `35.96%`. This is a finite-`L` numerical fit check at
   `L ≤ 64`, not a proof of the asymptotic statement. The extended
   `L <= 96` probe (via `scripts/probe_bh_rt_ratio_asymptotic.py`)
   is **explicitly deferred** as cache-not-in-packet (see "Deferred
   (cache-not-in-packet)" above); any L ≤ 96 numerical claim is
   pending a future runner extension that bundles the probe cache
   into this packet.

5. On the 3D analogue of the carrier (C-1)-(C-8) (cubic lattice
   `Lambda_L^{(3)}`, `L = 4, 6, 8, 10`) the RT ratio is further from
   `1 / 4` still (`r(L=10) ~ 0.098`) and extrapolates to `~0.058`,
   comfortably consistent with the 3D Widom value `c_Widom(3D) ~
   0.105` (up to finite-size bias at these small `L`) and comfortably
   far from `1 / 4`.

## What is not proved

This note does **not** claim:

- that the Widom value `c_Widom` is forbidden from matching `1 / 4` for
  *every* possible discrete carrier. One can invent a multi-pocket Fermi
  surface whose projected-width integral hits `6 pi` and so whose
  `c_Widom` is exactly `1 / 4`. Such a carrier is **outside the
  carrier class (C-1)-(C-8)** and the no-go does not apply to it.
  Symmetrically, a carrier with a different lattice geometry (e.g.
  triangular), a different filling (away from half), or a non-straight
  cut would yield a different `c_Widom`; the no-go does not apply to
  it without an explicit re-evaluation of (W-1).
- that Bekenstein-Hawking entropy does not equal `A / (4 l_P^2)` as a
  physical statement. The `1 / 4` in the physical `S_BH` comes from the
  Einstein-Hilbert normalization `1 / (16 pi G_N)`, not from a lattice
  bond-usage ratio. The no-go is about the *derivation path* used by
  any lane whose carrier coincides with (C-1)-(C-8), not about the
  target formula.
- that the free-fermion carrier (C-1)-(C-8) is the unique or best path
  to lattice Bekenstein-Hawking on `Cl(3)/Z^3`. A carrier that embeds
  a gravitational coupling on the lattice (e.g., a bulk/boundary setup
  with an explicit Einstein-Hilbert sector) can still yield `S = A /
  (4 l_P^2)` through a different mechanism. The no-go does not
  preclude such alternative carriers; it precludes only the specific
  RT-bond-dimension route inside the carrier class (C-1)-(C-8).
- that the bridge (B-1)-(B-4) closes the *physical* identification
  `S_lat = S_BH` for any specific lane, or even the all-`L`
  asymptotic value of the dimensionless RT ratio (C-8) on
  (C-1)-(C-8). Any lane that wishes to identify `S_lat` with `S_BH`
  must supply its own lane-specific identification step; any lane that
  wants to use this carrier as an all-`L` obstacle to exact `1/4` must
  first close OA-1/OA-2.

## Why it matters on `main`

The BH entropy lane is currently carried as a **bounded companion** in
`PUBLICATION_MATRIX.md` and
`CLAIMS_TABLE.md` on the basis of an
observed numerical RT ratio `~0.24` on lattices up to `L = 32`, explained as
"expected regulator dependence". This narrowed note does not close the
all-`L` question. It records the exact 2D Widom coefficient and the
finite-`L <= 64` numerical-fit evidence showing that the current
in-packet carrier/readout does not establish an exact `1/4` ratio.
Any downstream lane whose carrier coincides with (C-1)-(C-8) inherits
this bounded obstacle, while the all-`L` no-go awaits OA-1/OA-2.

Concrete consequences for the publication surface:

- the existing bounded companion row remains bounded, with this finite
  evidence and the open OA-1/OA-2 bridge cited as the reason it cannot
  be promoted while its carrier coincides with (C-1)-(C-8)
- the row's "5.4% deviation" framing on `L <= 32` is replaced by the
  narrower statement "the `L <= 64` in-packet runner fits toward
  `c_inf = 0.1601`, which is 35.96% from `1/4`; the all-`L` bridge
  remains open"
- any future attempt to promote a free-fermion BH-entropy-from-RT lane
  needs either to close OA-1/OA-2 on this carrier/readout or change the
  carrier/readout and re-evaluate the coefficient.

## Classical results applied

- Widom-Sobolev conjecture for free-fermion entanglement entropy
  (Widom 1982; Gioev-Klich 2006 conjecture; Helling-Leschke-Spitzer 2011
  rigorous proof on `R^d`)
- Calabrese-Cardy `c/6` log coefficient for open-boundary free-fermion
  chains
- Standard Schur-complement / determinant formula for free-fermion
  entanglement entropy from the restricted correlation matrix

## Framework-specific step

- intrinsic definition of the carrier (C-1)-(C-8) directly inside this
  packet: open-boundary square (or cubic) lattice, NN-hopping
  Hamiltonian, half-filled Slater determinant, straight cut, transfer
  rank from the layer-coupling submatrix of `C`, RT ratio (C-8)
- proposed self-contained carrier-Widom bridge (B-1)-(B-4): Bloch
  diagonalization of (C-2) gives the diamond (2D) / hyperplane (3D)
  Fermi surface (B-1.2); free-fermion entanglement entropy reduces to
  the truncated Wiener-Hopf operator whose asymptotic spectrum is
  governed by Widom-Gioev-Klich (B-2); transfer rank saturation of the
  boundary layer dimension is open (B-3 / OA-2); their combination
  would yield (B-4.4) after OA-1/OA-2 are supplied
- explicit evaluation of the Widom integral for the diamond
  (`2D`, exact `1/6`) and its 3D analogue (Monte Carlo `~0.105`)
- explicit statement that the all-`L` conclusion
  `lim_L r(L) = c_Widom != 1/4` is deferred pending OA-1/OA-2; the
  retained content is finite-`L <= 64` numerical-fit evidence plus the
  exact 2D Widom coefficient calculation

## Verification

Run:

```bash
python3 scripts/frontier_bh_entropy_rt_ratio_widom.py
```

The runner instantiates the carrier (C-1)-(C-8) directly (it does not
import from `BH_ENTROPY_DERIVED_NOTE.md` or any other lane note), and:

1. computes the analytic `c_Widom(2D) = 1/6` from the diamond integral
   (B-1.2)
2. computes `c_Widom(3D)` numerically from the Fermi surface Monte Carlo
3. measures `r(L)` on the OBC `L x L` lattice for `L` up to `64`
   (about 13 s on a laptop)
4. fits `r(L) = c_inf + a / ln L` on `L >= 32` and reports `c_inf`
5. compares `c_inf` against `1/6` (the exact 2D Widom coefficient) and
   `1/4` (the hypothesized lane-claim coefficient)
6. passes iff `|c_inf - 1/6| / (1/6) < 0.10` and
   `|c_inf - 1/4| / (1/4) > 0.20` for the finite-`L <= 64` fit

Current runner output: `PASS = 11, FAIL = 0`, with `c_inf(L>=32) = 0.1601`
(3.94% below 1/6, 35.96% below 1/4).

Extended `L <= 96` probe via
`scripts/probe_bh_rt_ratio_asymptotic.py` (L up to 96, ~3 min) is
available but its cache is **not bundled** in the current audit
packet, so any claim sourced from the probe is **explicitly
deferred** from the retained scope of this note per the 2026-05-25
narrowing. The retained finite-`L` numerical-fit evidence is the
in-packet runner cache (`L <= 64`) only. Re-shipping the probe cache
inside this packet (a future runner extension) is the named
condition for any L ≤ 96 claim to re-enter the retained scope.

## Relation to the current BH entropy lane

The dependency direction between this no-go and the bounded BH entropy
companion is now explicit and one-directional, **upstream-to-downstream**:

- this narrowed packet is logically prior for its finite content. Its
  mathematical content (the carrier (C-1)-(C-8), the exact
  Widom-coefficient evaluation, and finite-`L <= 64` runner evidence)
  is fully contained inside this packet. It does not depend on
  `BH_ENTROPY_DERIVED_NOTE.md` for any load-bearing input.
- the bounded companion authority
  `BH_ENTROPY_DERIVED_NOTE.md` is
  downstream: its carrier coincides with (C-1)-(C-8), so this packet's
  finite evidence and open OA-1/OA-2 all-`L` bridge are blockers to
  promotion. The bounded lane therefore stays bounded unless OA-1/OA-2
  close or the carrier/readout changes.
- the bounded companion cites this no-go in its prose. **This no-go
  does not cite the bounded companion as authority.** The 2026-05-10
  rigorization removed the load-bearing carrier import and replaced
  it with the intrinsic definition (C-1)-(C-8) plus the bridge
  (B-1)-(B-4).

This audit-driven repair closes the dependency direction the
2026-05-05 audit verdict flagged. The no-go's status no longer
inherits from `BH_ENTROPY_DERIVED_NOTE.md`'s status.

## Safe wording for the publication surface

Safe manuscript wording (if the no-go is referenced):

> On the half-filled NN-hopping free-fermion carrier on the open-boundary
> square lattice with a straight cut and bond-rank `chi_eff = L` (the
> carrier (C-1)-(C-8) of `BH_ENTROPY_RT_RATIO_WIDOM_NO_GO_NOTE.md`),
> the in-packet `L <= 64` RT bond-dimension fit gives
> `c_inf = 0.1601`, close to the exact 2D diamond Widom coefficient
> `1/6` and far from `1/4`. The all-`L` bridge from this OBC carrier
> and thresholded `chi_eff` readout to `lim_L r(L) = c_Widom` remains
> open pending a uniform lattice/Widom and threshold-rank proof. The
> framework therefore has not derived the coefficient `1/4` in
> `S_BH = A / (4 l_P^2)` from free-fermion entanglement on this carrier.

Explicitly unsafe wording:

> The framework derives `S_BH = A / (4 l_P^2)` exactly from free-fermion
> lattice entanglement.
