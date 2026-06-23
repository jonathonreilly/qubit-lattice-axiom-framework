# d = 3 Native Unblock Proposal: Retire The Imported Continuum Potential Family, Expose The Carrier Bit, Compose The Native Two-Sided Pinch

**Type:** PROPOSAL
**Status:** hypothetical_axiom_status (`proposal_allowed = false`)
**Status authority:** the independent audit lane + owner ONLY. **This note
sets NO audit status** — it neither asserts, predicts, promotes, nor demotes
any audit outcome or effective status.
**Date:** 2026-06-23

> **This note touches NO canonical, audit, or publication file.** It does not
> edit any `MINIMAL_AXIOMS_*`, `AUDIT_LEDGER.md`, `AUDIT_QUEUE.md`,
> `MISSING_DERIVATION_PROMPTS.md`, any `*_EFFECTIVE_STATUS.md`, or any
> `docs/audit/data/**` file. It registers no primitive and changes no axiom
> memo. It is a source-side proposal only; the independent audit lane is the
> sole status authority.

---

## PURPOSE

The d = 3 (spatial-dimension) derivation is currently blocked from independent
audit by two textbook IMPORTS and one hidden hypothesis. This proposal unblocks
it by making every load-bearing step framework-internal-or-explicitly-named:

1. **Replace the lower leg's imported continuum potential family** (`phi ~ -Mr`
   / `-M log r` / `-M/r^{d-2}`, injected as Runner Surface step 2 of
   [`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md)) with the
   **native `Z^d` lattice-Laplacian transience computation**: the inverse of the
   Lattice axiom's nearest-neighbor graph Laplacian `L`. The continuum family is
   exactly the `a -> 0` limit of the native kernel, so the import added nothing
   and is deleted.

2. **Make the upper leg's carrier hypothesis explicit.** The native algebraic
   core ([`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md))
   forces `d <= 3` **only within the first-order Dirac-square carrier class**.
   That carrier-class membership is one explicit bit (`phi = -1`), not an axiom.
   This proposal exposes the bit with its computed countermodel rather than
   hiding it inside an orbit-stability import.

3. **Compose the native two-sided pinch** `{d >= 3} ∩ {d <= 3} = {3}` with every
   hypothesis named, every imported number replaced by an in-runner analytic
   constant, and the honest posit count stated up front.

**Headline caveat, stated first and not buried.** The Lattice + Quantum axioms
**alone derive nothing about d.** What this proposal achieves is **compression,
not closure**: it reduces "why d = 3" to a small, explicit, named dynamics
fragment with concrete countermodels at each open joint, replacing two textbook
imports with framework-internal computations modulo those named posits. The
d = 3 result is exactly as strong as the conjunction of the three named posits
{Clause A `phi = -1` (UNAUDITED), Clause B P-DECAY (posited, non-unique),
Clause C static-field-law `L^{-1}` (posited)}. This respects the #2586 /
[`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md)
line-117/line-180 guardrail: `M_2(C) = Cl(3,0)` is a **consistency, not a
derivation of spatial d**, and nothing here relocates d = 3 onto the
matter/Dirac dynamics.

---

## THE COMMON OBJECT

Both legs are two faces of the **same combinatorial graph Laplacian** built from
the Lattice axiom alone:

```text
    L := 2d * I - A,      (A f)(x) = sum_{|y-x|=1} f(y),
    (L f)(x) = 2d f(x) - sum_{|y-x|=1} f(y).
```

The coordination number `2d` and the nearest-neighbor sum are the ONLY inputs
(no metric, spacing, dynamics, or continuum limit). The Lattice axiom's standard
translation action Fourier-diagonalizes `L` with symbol

```text
    lambda(k) = 2d - 2 sum_{i=1}^d cos(k_i)
              = 2 sum_{i=1}^d (1 - cos k_i)
              = |k|^2 + O(|k|^4),      k in [-pi, pi]^d,
```

a single zero at `k = 0`, positive elsewhere on the compact Brillouin zone. The
two legs consume different FACES of this `L`:

- **Upper:** `L` as the square of a first-order carrier, `D^2 = I (x) L`.
- **Lower:** `L^{-1}` as the kernel of the static point-source response.

**Honest correction to the "shared `L`" framing (verifier MINIMALITY must-fix).**
The unification is an **IR / continuum-symbol match, not a lattice operator
identity.** The Dirac-square block has symbol `D(p)^2 = -(sum_mu sin^2 p_mu) I`
(the naive doubler Laplacian), whereas the lower leg inverts the combinatorial
Laplacian with symbol `2 sum_mu (1 - cos k_mu)`. These coincide ONLY in the
leading IR symbol (`sin^2 p` and `2(1 - cos p)` both `-> |k|^2` as `k -> 0`),
not as lattice operators (`sin^2 p != 2(1 - cos p)` away from `0`). The
convergence dichotomy below lives entirely in that leading IR symbol, so the
pinch survives; but the "one operator `L`, two faces" rhetoric is downgraded to
"the two legs share `L` only via the leading continuum symbol."

---

## NATIVE LOWER LEG (d >= 3)

### The transience derivation (native to the Lattice axiom)

The static response to a unit point source at the origin solves `L G = delta_0`.
The infinite-volume kernel is the Watson-type oscillatory integral

```text
    G(x) = (2 pi)^{-d} integral_{[-pi,pi]^d} e^{i k.x} / lambda(k) d^d k.
```

**(1) Coincidence limit and the convergence dichotomy.**

```text
    G(0) = (2 pi)^{-d} integral_{[-pi,pi]^d} d^d k / ( 2 sum_{i=1}^d (1 - cos k_i) ).
```

The only possible divergence is the IR point `k -> 0`, where the integrand
behaves as `1/|k|^2`. In d-dimensional spherical measure `d^d k ~ k^{d-1} dk`,
the IR integrand is `~ k^{d-1}/k^2 = k^{d-3} dk`. This converges iff
`d - 3 > -1`, i.e. **`d >= 3`** (`d = 3` is the marginal converging case; the
zone boundary is always finite since `lambda > 0` away from `0`). Hence:

| d | IR behavior of G(0) | reading |
|---|---|---|
| 1 | `~ integral_0 k^{-2} dk` — LINEAR divergence (`G(0)` doubles per box-doubling) | no normalizable kernel |
| 2 | `~ integral_0 k^{-1} dk` — LOGARITHMIC divergence, exact coefficient `ln(2)/(2 pi) = 0.1103178` per L-doubling | no normalizable kernel |
| >= 3 | CONVERGES; at d = 3 the Watson integral `G(0) = 0.2527310` | normalizable kernel exists |

This is exactly the **Polya recurrence/transience dichotomy**. `G(0)` is the
expected number of visits to the origin of the simple symmetric random walk,
and the return probability is `p_return = 1 - 1/(2d * G(0))`, a valid
probability in `(0,1)` iff `G(0)` is finite. Recurrence (`d <= 2`) `<=>`
`G(0) = infinity` `<=>` NO normalizable static kernel; transience (`d >= 3`)
`<=>` `G(0)` finite `<=>` a decaying point-source kernel exists. Mediator-response
normalizability and random-walk transience are THE SAME statement.

**Watson closed form (analytic-constant must-fix applied).**

```text
    G(0)|_{d=3} = ( sqrt(6) / (192 pi^3) ) Gamma(1/24) Gamma(5/24) Gamma(7/24) Gamma(11/24)
               = 0.2527310.
```

The previously circulated prefactor `sqrt(6)/(32 pi^3)` is **WRONG** — it equals
`1.516386`, a factor of exactly 6 too large. The `/192` normalization is the
correct one and is verified in-runner; `0.2527310` is the retained cross-check.

**(2) Off-diagonal decay.** Subtracting the singular `k = 0` mode, the leading
large-`|x|` behavior is the inverse FT of `1/|k|^2` in d dimensions:

| d | off-diagonal | reading |
|---|---|---|
| >= 3 | `G(x) ~ C_d |x|^{2-d}` (d = 3: `1/(4 pi |x|)`) | decays to 0 |
| 2 | relative potential `a(r) = G(0) - G(r) ~ +(1/(2 pi)) log|x|` | GROWS (confining log) |
| 1 | `a(r) = r(L-r)/(2L)` on the L-torus `-> |x|` | GROWS LINEARLY (confining) |

The static response decays iff `d >= 3`; for `d <= 2` it is
non-normalizable/confining. **(`d = 1` example with EXPLICIT torus size, must-fix
applied):** `a(r) = r(L-r)/(2L)` at `r = 16,32,64,128` gives `[7.75, 15, 28, 48]`
at **L = 512** and `[7.5, 14, 24, 32]` at **L = 256** — the quadruples are
L-specific and must be labeled. The closed form is exact (matched to `1e-13`).

### The removed import

```text
REMOVED: the continuum analytic potential family
    phi ~ -M r       (d = 1)
    phi ~ -M log r   (d = 2)
    phi ~ -M / r^{d-2}  (d >= 3)
injected as Runner Surface step 2 of DIMENSION_SELECTION_NOTE.md.

REPLACED BY: the native kernel L^{-1} of the Lattice axiom's graph Laplacian,
whose IR power-counting (integrand ~ k^{d-3} dk) gives the SAME three regimes as
exact consequences, with the continuum family recovered only as the a -> 0
limit. Each imported line is exactly the |x| -> infinity / continuum limit of
the native lattice kernel:
    d=1 native a(r) -> |x|              == imported -M r;
    d=2 native a(r) -> -(1/2pi) log|x|  == imported -M log r;
    d>=3 native G(x) -> C_d |x|^{2-d}   == imported -M/r^{d-2}.
The import supplied nothing the L-Laplacian did not already give.
```

**Sever the corroboration (compose-verifier must-fix).** This native leg
**replaces** (does not merely restate) the landed
[`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md) lower leg, whose
pass-set `{3,4,5}` is produced by the imported potential family + a
**sign-SENSITIVE attractive-gravity / `beta ~ 1`** criterion. The native
P-DECAY is **sign-BLIND**. The two agree on the set `{3,4,5}` for **inequivalent
reasons**; presenting their numerical agreement as mutual confirmation would
re-import the very potential family being retired. The native kernel-decay leg
must be recorded as **standalone**, inheriting NO confidence from the
import-based row, and inheriting the UNAUDITED status of
[`D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md`](D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md)
as the new load-bearing path.

### The named selection posits (the lower leg rests on TWO, not one)

**Clause C — P-FIELD (static field law).** "The static mediator response is
governed by `L^{-1}`." This is a static Poisson-type field equation
`L G = delta_0` whose kinetic operator is the Lattice axiom's graph Laplacian.
The Lattice axiom gives adjacency and the Quantum axiom gives the carrier;
**NEITHER supplies a field equation.** This is therefore **POSITED**, not
axiom-internal. (Import-smuggling must-fix: it was previously mislabeled
AXIOM-INTERNAL; the axiom memo's open-gates section explicitly defers
"source/action and physical-observable identification," which this is.) It does
not smuggle gravity (no sign, no `1/r`, no coupling) but does posit that the
mediator obeys a Laplacian field equation.

**Clause B — P-DECAY (normalizability selector).** "The static response `L^{-1}`
is normalizable: `G(0) < infinity`" (equivalently `1/lambda in L^1`,
equivalently SSRW transience); `G(x) -> 0` then follows by Riemann-Lebesgue
(cited, not asserted bare). This is **POSITED**, not axiom-derived. It is
**sign-blind** (admits a repulsive decaying mediator equally), references no
inverse-square force, no coupling, no `1/r` form — strictly weaker and more
explicit than the discarded attractive-gravity/`beta ~ 1` bundle, which fixed a
sign AND a mass exponent. Replacing that bundle is a genuine de-smuggling.

**P-DECAY is NOT the unique legitimate normalizability formulation
(necessity-of-decay must-fix).** The exclusion of `d = 1, 2` holds ONLY under
self-energy / asymptotic normalizability (`G(0) < infinity` and/or `G(x) -> 0`).
An equally-legitimate **finite-relative-response** reading — `a(r) = G(0) - G(r)`
finite at finite `r` — is satisfied in ALL `d >= 1` (e.g. d = 2: `a(r)` is
finite at every finite `r`) and would admit `d = 1, 2`, collapsing the bound.
So P-DECAY's exclusion of `d <= 2` is contingent on choosing self-energy /
asymptotic normalizability over relative-response finiteness — a defensible but
**choosable** formulation, which must be stated as the explicit selection input,
not as the only legitimate one. The **"finite self-energy" / "finite-energy"
gloss must be struck** (the Lattice + Quantum axioms supply no energy
functional): the defensible bare statement is `G(0) < infinity`.

### Lower-leg runner spec (RUNNER 2)

Deterministic, per-`d` over `{1,2,3,4,5}`, NO fitted parameters, NO empirical
constants (the only numbers, `ln(2)/(2 pi) = 0.1103178` and the Watson constant
`0.2527310`, are computed analytic lattice constants).

- **(A) Coincidence-limit convergence.** On the periodic box `(Z_L)^d` for an
  increasing L-sequence (cap `L^d <= ~3e5`: e.g. d=1 `L=64,128,256,512`; d=2
  `L=16,32,64,128`; d=3 `L=8,16,24,32`; d=4 `L=6,8,10,12`; d=5 `L=4,6,8,10`),
  form `lambda(k) = 2 sum_i (1 - cos k_i)` on the FFT grid, remove the single
  `k = 0` mode, compute `S_d(L) = (1/L^d) sum_{k != 0} 1/lambda(k)`. PASS
  conditions: d=1 ratio `S(2L)/S(L) -> 2` (within 2%) [linear]; d=2 increment
  `S(2L) - S(L) -> ln(2)/(2 pi)` (within 0.005) [log]; d=3,4,5 increment
  sequence strictly shrinking and Cauchy, d=3 within 0.01 of `0.2527310`
  [convergence].
- **(B) Off-diagonal dichotomy.** d=1: assert `a(r) = r(L-r)/(2L)` to `1e-8` at
  an **EXPLICITLY LABELED L**. d=2: assert increments `a(2r) - a(r) ->
  ln(2)/(2 pi)` across `r = 4,8,16,32`. d=3: using the **infinite-volume Bessel
  representation** `G(x) = integral_0^inf prod_mu e^{-2t} I_{x_mu}(2t) dt`,
  assert `4 pi r G(r) -> 1` monotonically (`1.0198, 1.0041, 1.0010` at
  `r = 4,8,16`) and `G(0) = 0.2527310` to `1e-4`. **Warning (math-correctness
  must-fix): the periodic-FFT torus must NOT be used for the d = 3 tail** — it
  gives a spurious too-fast-decaying `0.84, 0.65, 0.33` on finite L (zero-mode
  subtraction + periodic images). Use the Bessel route only.
- **(C) Polya equivalence.** Assert `{d : S_d converges} = {3,4,5}` equals
  `{d : SSRW on Z^d transient}` via `p_return = 1 - 1/(2d G(0))` being a valid
  probability in `(0,1)` iff `G(0)` finite (d=3: `0.3405`).

Expected: convergence/decay pass-set `= {3,4,5}`; failure set `= {1,2}`; the
selector P-DECAY admits exactly `{d >= 3}` on the tested range. The runner sets
no audit status and reads no empirical constant. *(Numerics independently
reproduced 2026-06-23: d=1 `5.33,10.67,21.33,42.67` exact doubling; d=2
increments `0.1104,0.1103,0.1103`; d=3 `0.2246,0.2386,0.2433,0.2457` increments
shrinking; Polya p_ret(d=3) `= 0.3405`.)*

---

## NATIVE UPPER LEG (d <= 3)

### The algebraic core (native to the Quantum axiom, complete)

Source:
[`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md)
(T1, T2, T3; runner `scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py`,
SCORECARD PASS=18, FAIL=0).

**(T1) Maximality.** In `M_2(C)` any family of mutually anticommuting
self-adjoint unitaries has AT MOST 3 members.
- *(a) Tracelessness.* If `P` is an invertible (here unitary) self-adjoint
  operator and `{X,P} = 0`, then `X = -P X P^{-1}`, so `tr X = -tr X` by
  cyclicity; since `char(C) = 0`, `tr X = 0`.
- *(b) Bloch form.* A traceless self-adjoint unitary on `C^2` is `n.sigma` with
  `n in R^3`, `|n| = 1` (`(n.sigma)^2 = I` iff `|n|^2 = 1`).
- *(c) Anticommutation = orthogonality.* `{n.sigma, m.sigma} = 2(n.m) I`, so a
  mutually anticommuting family corresponds to pairwise-orthogonal unit vectors
  in `R^3`, of which there are at most `dim R^3 = 3`.
- *(d) The 4th element is exactly 0, even non-unitary.* Stacking
  `{X, sigma_a} = 0` (a = 1,2,3) as a 12x4 real-linear map on `vec(X)` gives
  nullspace dimension `= 4 - rank = 0`; symbolic solve returns the unique
  `X = 0`. This is the saturation wall.

**(T2) Cross-term forcing.** A first-order translation-covariant NN operator
`D = sum_{mu=1}^d gamma_mu (x) nabla_mu` (with `nabla_mu` the antisymmetric NN
difference, symbol `i sin p_mu`) satisfies

```text
    D^2 = I (x) Laplacian       (no spin-lattice cross terms),
    D^2 = sum_mu gamma_mu^2 (x) nabla_mu^2 + sum_{mu<nu} {gamma_mu,gamma_nu} (x) nabla_mu nabla_nu,
```

IFF the `gamma_mu` are mutually anticommuting self-adjoint unitaries (the cross
terms must vanish). The hostile witness `gamma_2' = (sigma_1 + sigma_2)/sqrt(2)`
— itself a self-adjoint unitary but not anticommuting with `sigma_1` — grows
nonzero cross terms.

**(T3) The bound.** A Dirac-square NN carrier on the one-qubit-per-site lattice
needs `d` mutually anticommuting self-adjoint unitaries (T2); `M_2(C)` caps that
at 3 (T1). Hence **`d <= 3`**, with `Z^3` saturating (Pauli frame
`gamma_mu = sigma_mu`). Explicit `d = 1, 2` Dirac-square carriers also exist
(runner Part F), so the number 3 enters ONLY through the `M_2(C)` anticommutant
cap, **never through an assumed spatial dimension** — no circularity.

### The explicit carrier forcing chain (the conditional part)

| Link | Statement | Status |
|---|---|---|
| L1 | Quantum axiom `-> dim_C H_x = 2` (`A_x = M_2(C) = Cl(3,0)`) | axiom-internal |
| L2 | dim 2 `->` single Grassmann mode (not bosonic Fock, dim infinity) | positive WITHIN the two-candidate surface; **NOT statistics-forcing** (hard-core-boson frame ties on per-site dim 2; excluding it needs the UNAUDITED `axiom_first_spin_statistics_theorem`, B-stat hatch) |
| L3 | {dim 2, Locality} `->` Kogut-Susskind staggered scheme (Wilson/naive need per-site dim `2^4 = 16`; overlap/domain-wall nonlocal) | bounded_theorem, landed-but-UNAUDITED (`STAGGERED_SCHEME_FORCED_..._2026-06-06`) |
| **L4** | **THE LOAD-BEARING BIT: first-order Dirac (`phi = -1`/K1) vs second-order scalar (`phi = +1`/K0)** | **NOT forced; K0 is the computed countermodel** ([`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md) B-BIT; [`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md)) |

The two-flux-class theorem collapses the a-priori infinite charge-conserving NN
kinetic family (under translation + 24-element proper-cubic covariance up to
site-local `U(1)` frame) to EXACTLY TWO frame classes distinguished by the
frame-invariant uniform plaquette flux `phi in {+1, -1}`:

```text
K0 :  phi = +1   representative t == 1   (scalar tight-binding, extensive zero surface
                                          = the SECOND-ORDER / Klein-Gordon branch)
K1 :  phi = -1   representative eta^0     (Kawamoto-Smit staggered system, 8 isolated
                                          Dirac zeros = the FIRST-ORDER / Dirac branch)
```

The absorbing-frame theorem then DISCHARGES P-SD on K1: a per-site 2-component
spinor would need a faithful CAR(2) module `= M_4(C)` (dim 16 > 2), so the Cl(3)
vector vertex must be absorbed by site-local frames
`T(x) = sigma_1^{x1} sigma_2^{x2} sigma_3^{x3}`, forced into flux `-1`
(`gamma_nu gamma_mu gamma_nu gamma_mu = -I`), unique up to gauge x global frame.

### The honest carrier boundary

The final selector K1 vs K0 is **NOT forced** by the specified constraint set.
K0 is the explicit countermodel: Hermitian, exactly translation- and
24-rotation-invariant, charge-conserving, fermion-parity-even, and NOT
frame-equivalent to K1. The index-pairing no-go independently exhibits the
spectator `H(p) = (sum_mu cos p_mu) I_2`: local, full-`O_h`-covariant including
spatial inversion (`cos` is parity-even), Hermitian, and `[H, sigma_i] = 0`
exactly — **the qubit GENUINELY SPECTATES.** On the `phi = +1` branch the bound
is **VACUOUS.** No axiom-permitted selector picks first-order non-circularly:
Record gives no dynamics; positivity/stability does not select (the naive
first-order Dirac symbol has a negative branch, the scalar Laplacian is
bounded); Nielsen-Ninomiya bites within the first-order class; the only thing
forcing first-order is the isotropic linear Lorentz cone `|E| = |p|`, which is
itself the Dirac assumption — circular.

**Therefore the `d <= 3` bound is exactly conditional on the single bit
`phi = -1`. Given that bit, L3-L4 deliver a single-mode site-local Dirac-square
carrier and T1-T2 cap it at `d <= 3`, with `Z^3` saturating. Without that bit
the qubit spectates and the bound is vacuous.** The certified algebra (18/18)
must NEVER be mistaken for closure of the kinetic-order bit; the WHOLE upper leg
is graded by the UNAUDITED `phi = -1` selector.

**Framing guardrail (carrier-circularity must-fix).** Every statement of
`d <= 3` must carry the qualifier "**within the translation-covariant NN
Dirac-square carrier class, conditional on `phi = -1`**" — never bare "`d <= 3`
FORCED by the Quantum axiom" — to respect the #2586 / INDEX_PAIRING line-117
guardrail (`M_2(C) = Cl(3,0)` is a consistency, not a derivation of spatial d).

### Upper-leg runner spec (RUNNER 1)

An extension/restatement of the verified
`scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py`. Inputs: the three
Pauli matrices and `I_2`; symbolic `X = [[a11,a12],[a21,a22]]` over `C`;
symbolic momenta. All exact (sympy for 2x2 algebra and symbolic solve;
integer/GF(2) for ranks).

- **(R1)** `{n.sigma, m.sigma} - 2(n.m) I == 0` symbolically.
- **(R2)** `(n.sigma)^2 = I` iff `n1^2 + n2^2 + n3^2 = 1`.
- **(R3)** `tr(P X P^{-1}) - tr X == 0` for `P = sigma_1`, and `tr X == 0` on the
  full solution space of `{X, sigma_1} = 0`.
- **(R4) CENTRAL** — build `M_sys = vstack` over `a = 1,2,3` of
  `[ kron(sigma_a^T, I_2) + kron(I_2, sigma_a) ]` (12x4 acting on `vec(X)`);
  assert nullspace dim `= 4 - rank = 0`; cross-check symbolic solve returns the
  unique `X = 0`.
- **(R5) Gram obstruction** — `I_4` has rank 4 but any Gram of vectors in `R^3`
  has rank `<= 3`, so no 4 pairwise-orthonormal Bloch vectors exist.
- **(R6) Dirac-square forcing** — `D(p) = sum sigma_mu i sin p_mu`,
  `D(p)^2 = -(sum_mu sin^2 p_mu) I` for the Pauli frame; FAIL-witness: replacing
  `sigma_2` by `(sigma_1+sigma_2)/sqrt(2)` makes the residual provably nonzero.
- **(R7) Bound assembly** — anticommuting size-`d` family exists for `d <= 3`,
  not for `d = 4` (from R4); conclude `d <= 3`.
- **(R8) Carrier-independence boundary (must be PRINTED, not hidden)** — exhibit
  `H(p) = (sum_mu cos p_mu) I_2`, verify `[H(p), sigma_i] = 0` and `H(-p) = H(p)`
  (parity-even spectator); print
  `CARRIER-RESIDUAL (declared-open): first-order Dirac (phi=-1) assumed; phi=+1 scalar countermodel spectates`.

**Hardening promoted from recommended to REQUIRED for auditability
(algebra-verifier + compose must-fix):** (i) add an explicit check that
self-adjoint unitaries with trace `+-2` (i.e. `+-I`) are central and excluded
from any size-`>= 2` anticommuting family, exhibiting the Bloch step's
restriction to traceless members; (ii) replace any random-matrix rank proxy with
the direct statement `rank(I_4) = 4 > 3 >= rank(any R^3 Gram)`; (iii) make the
Laplacian sign convention uniform in prose (runner gives
`D(p)^2 = -(sum sin^2 p) I`). The cap "3" must be seen to rest on the R4
nullspace computation, not on Bloch-orthogonality prose alone.

Expected: SCORECARD all PASS, FAIL=0, plus exactly one declared-open
CARRIER-RESIDUAL line. *(Numerics independently reproduced 2026-06-23: R4
nullspace dim 0 over the full Pauli frame, dim 1 (the `sigma_3` ray) with
`{sigma_1,sigma_2}` only; R6 residual `~1e-18`, witness residual nonzero; R8
`[H,sigma_i] = 0` exactly.)*

---

## THE PINCH AND THE MINIMAL DYNAMICS POSIT

```text
    {d >= 3} (lower)  ∩  {d <= 3} (upper)  =  {3}     exactly,
```

with `d = 4, 5` excluded ONLY by the upper leg and `d = 1, 2` excluded ONLY by
the lower leg — a genuine two-sided, non-redundant composition. **Neither leg
alone selects 3**; uniqueness is the intersection.

### The minimal dynamics fragment: A1 + A2 + [one named posit] => d = 3

The minimal dynamics fragment beyond the Lattice + Quantum axioms is

> **[P-DYN]** "There is a realized LOCAL, FIRST-ORDER kinetic carrier on the
> lattice whose induced static point-source response is normalizable/decaying."

It reads as one coherent stencil because the SAME `L` appears as `D^2` (upper)
and as the static-kernel generator (lower). Given P-DYN:

- **UPPER LEG `d <= 3`** follows from Quantum + Clause A alone (first-order `->`
  Dirac-square `->` anticommuting gammas `->` `M_2(C)` cap 3).
- **LOWER LEG `d >= 3`** follows from Lattice + Clause C + Clause B (`L` fixed by
  adjacency `->` `L^{-1}` static law `->` IR convergence iff `d >= 3`).

### Honesty on one-vs-two-vs-three posits (NOT one posit)

**Brutally honest: it is THREE clauses, at least TWO provably independent, and
the "single coherent posit" framing is partly cosmetic (held together only by
the shared `L`).** This three-count is the HEADLINE, not a buried concession.

```text
Clause A  P-ORDER   the realized NN kinetic operator is FIRST-ORDER (phi = -1):
                    the qubit is kinetically ACTIVE ([D,sigma_i] != 0), not a
                    spectator. Delivers the upper leg (d <= 3).
Clause B  P-DECAY   the static response L^{-1} is normalizable (G(0) < infinity).
                    Delivers the lower leg (d >= 3).
Clause C  P-FIELD   the static response IS governed by L^{-1} (a Poisson-type
                    field law with the graph Laplacian as kinetic operator).
                    Structural premise of the lower leg.
```

1. **Clause A and Clause B are INDEPENDENT** — neither implies the other.
   *(a)* First-order does NOT imply decay: the `d = 1, 2` first-order
   Dirac-square carriers exist yet their `L` has a non-normalizable inverse.
   *(b)* Decay does NOT imply first-order: the second-order scalar branch
   (`phi = +1`) lives on the same `L` and has the same normalizable `L^{-1}` for
   `d >= 3`. The two clauses are logically orthogonal. So "the lower leg rests on
   exactly ONE selecting posit" is true only for the lower leg **in isolation**;
   the full fragment yielding both legs needs A and B independently. *(Caveat:
   "independent" is precise only relative to the present decomposition; a future
   single off-staggered RP / graded-locality principle could conceivably fuse A
   and B by entailing both the order bit and a transience/spectral property.)*

2. **Within the lower leg, conflating `G(0) < infinity` and `G(x) -> 0` into one
   clause IS legitimate** (for the positive translation-invariant `Z^d`
   Laplacian, `G(0) < infinity <=> 1/lambda in L^1 => G(x) -> 0` by
   Riemann-Lebesgue). BUT P-DECAY is ONE specific normalizability formulation;
   the finite-relative-response reading admits all `d >= 1`, so the exclusion of
   `d <= 2` is contingent on the choice, not inevitable.

3. **Clause C is a THIRD, separately-posited input** — a static field law NOT
   derivable from the Lattice + Quantum axioms, previously mislabeled
   axiom-internal.

**Net minimal residual `= 1` (Clause A `phi = -1`) `+ 1` (Clause B P-DECAY)
`+ 1` (Clause C P-FIELD) `= THREE named posits**, reducible in PRESENTATION to
"a local first-order carrier whose adjacency-Laplacian static response is
normalizable" but NOT reducible in LOGICAL content below {A, B, C}. Calling it
"one coherent posit" overstates unity.

### Relation to the panel's missing dynamics axiom

The blind panel's flagged **MISSING DYNAMICS AXIOM** is exactly the gap P-DYN
fills, and the three clauses map one-to-one onto the three things the axioms
explicitly do NOT supply (`MINIMAL_AXIOMS_2026-06-05.md`: Lattice "does not
supply a dynamics ... causal cone"; Quantum "does not supply a dynamics,
composition theorem ... gauge group, particle content"; open-gates lists
"source/action and physical-observable identification"; Record supplies no
dynamics):

```text
Clause A (P-ORDER, phi = -1) = the kinetic-order bit B-BIT
                             = the "first-order vs second-order" selector
                               the missing-dynamics axiom must fix      [UPPER leg]
Clause C (P-FIELD, L^{-1})   = the "source/action and equation-of-motion
                               identification" the axiom memo defers     [LOWER leg]
Clause B (P-DECAY)           = a selection criterion on the realized
                               dynamics (the response does not confine)  [LOWER leg]
```

The pinch's value is that it **isolates the minimal dynamics fragment from the
full missing axiom**: everything else a full dynamics axiom carries (arrow,
measurement, Born weights, record production, the action's coupling constant,
time metric, the Lorentz cone) is NOT needed for d = 3 and is left open. Because
Clause A and Clause B are independent faces, the missing axiom must supply BOTH a
kinetic-order bit AND a normalizability selector. The `phi = -1` bit is the
single most load-bearing piece and is the one the repo's own no-go (B-BIT) flags
as undischarged; candidate future closers named there (off-staggered
reflection-positivity, spin-statistics/graded-locality, a relativistic-cone
principle) would retire Clause A but would still leave Clauses B and C posited
unless the same principle also fixed the static field law and its
normalizability.

---

## AUDIT-UNBLOCK CHECKLIST

What the independent audit lane must verify (the two deterministic runners plus
the analytic and relabel fixes):

1. **RUNNER 1 (UPPER, native algebra).** Re-run
   `scripts/adjacency_rank_qubit_clifford_bound_2026_06_10.py` (expect SCORECARD
   PASS=18, FAIL=0). Verify R3 (tracelessness from cyclicity + `char(C) = 0`),
   R1, R4 (12x4 map rank 4, nullspace 0, symbolic `X = 0`), R6 (Pauli-frame
   Dirac square `= -(sum sin^2 p) I` and the hostile-witness nonzero cross
   terms), R8 (spectator `[H, sigma_i] = 0` with the printed CARRIER-RESIDUAL
   line). Apply the three REQUIRED hardenings (trace-`+-2` central exclusion;
   `I_4`-vs-`R^3`-Gram rank; uniform Laplacian sign).

2. **RUNNER 2 (LOWER, native Green function).** Deterministic per-`d` over
   `{1,2,3,4,5}`, NO fitted params, NO empirical constants (only `ln2/2pi` and
   the Watson constant, both computed in-runner). (A) finite-torus `G(0)` —
   d=1 ratio `-> 2`; d=2 increment `-> ln2/2pi` within 0.005; d=3,4,5 increments
   strictly shrinking, d=3 within 0.01 of `0.2527310`. (B) off-diagonal — d=1
   `a(r) = r(L-r)/(2L)` to `1e-8` at an **EXPLICITLY LABELED L**; d=2 increments
   `-> ln2/2pi`; d=3 via the **infinite-volume Bessel representation**
   `4 pi r G(r) -> 1` PLUS the one-line warning the periodic-FFT torus must NOT
   be used for the d=3 tail. (C) Polya — `{d : S_d converges} = {3,4,5} =
   {d : SSRW transient}`.

3. **ANALYTIC FIX.** Certify the d=3 Watson closed form reads
   `sqrt(6)/(192 pi^3) Gamma(1/24) Gamma(5/24) Gamma(7/24) Gamma(11/24) =
   0.2527310` (NOT `/32`, which equals `1.516386`, a factor 6 too large). Retain
   `0.2527310` as the numerical cross-check.

4. **THE ONE UNAUDITED CARRIER DEPENDENCY (weakest link, grade as such).**
   Re-run `scripts/staggered_dirac_kinetic_class_forcing_check_2026_06_10.py`
   (expect TOTAL PASS=28, FAIL=0); verify the two-flux-class collapse to
   `{phi=+1 (K0), phi=-1 (K1)}`, the absorbing-frame existence/uniqueness on K1,
   and CRITICALLY the B-BIT countermodel (K0 Hermitian, exactly translation- and
   24-rotation-invariant, fermion-parity-even, NOT frame-equivalent to K1).
   Record that `phi = -1` (Clause A) is a posited selector and grade the WHOLE
   upper leg by this UNAUDITED dependency; never let the 18/18 + 28/28 certified
   algebra be mistaken for closure of the kinetic-order bit.

5. **RELABEL.** Confirm hypothesis "static response `= L^{-1}`" (Clause C) is
   reclassified AXIOM-INTERNAL `->` POSITED (a static Poisson field law),
   resolving the contradiction with the deferral of "source/action and
   equation-of-motion identification." The lower leg rests on TWO posits
   (Clause C + Clause B), not "P-DECAY is the entire selecting content."

6. **NECESSITY-OF-DECAY.** P-DECAY must be stated as ONE of (at least) two
   inequivalent legitimate normalizability formulations; the exclusion of
   `d = 1, 2` holds ONLY under self-energy/asymptotic normalizability, NOT under
   finite-relative-response (`a(r)` finite at finite `r`, satisfied for all
   `d >= 1`). Strike the "finite self-energy"/"finite-energy" gloss (the axioms
   supply no energy functional); reduce P-DECAY to bare `G(0) < infinity` with
   `G(x) -> 0` following by Riemann-Lebesgue (cited).

7. **INHERITED-CONDITIONALITY LEDGER.** The composed pinch inherits
   `D3_PINCH_..._2026-06-11` (UNAUDITED) and, through the upper leg,
   `STAGGERED_SCHEME_FORCED_..._2026-06-06`,
   `STAGGERED_DIRAC_SUBSTEP1_GRASSMANN_FORCING_..._2026-05-16` (statistics
   hatch: hard-core-boson frame ties on per-site dim 2, needs UNAUDITED
   `axiom_first_spin_statistics`), and the L-EQ licensing lemma (translation +
   24-proper-cubic covariance up to site-local `U(1)` frame — load-bearing for
   the two-flux collapse, a named premise of equal standing to `phi = -1`). The
   d=3 leading constant `1/(4 pi)` and exact `|x|^{2-d}` rate inherit UNAUDITED
   status from `LATTICE_GREENS_1_OVER_R_..._2026-06-07` (direct local-CLT
   tail-domination step open). **Only the convergence DICHOTOMY is fully native
   and elementary; keep it separate from the unaudited tail constant when
   grading.**

8. **SEVER CORROBORATION.** Record the native lower leg as **standalone**, NOT
   inheriting the `{3,4,5}` pass-set of the import-based `DIMENSION_SELECTION_NOTE`
   as corroboration (sign-blind P-DECAY vs sign-sensitive attractive gravity;
   agreement is for inequivalent reasons).

---

## WHAT THIS DOES NOT CLAIM / HONEST RESIDUALS

- **The Lattice + Quantum axioms alone do not give d = 3.** This is the correct
  headline caveat. The pinch achieves COMPRESSION (reduces "why d = 3" to a small
  named dynamics fragment with concrete countermodels), not CLOSURE. The d = 3
  result is exactly as strong as the conjunction {`phi = -1` UNAUDITED, P-DECAY
  posited-non-unique, `L^{-1}` field-law posited}.

- **Does NOT claim d = 3 is forced by either leg alone.** P-DECAY gives only
  `d >= 3` (`d = 4, 5` pass it); the algebraic cap gives only `d <= 3` (`d = 1, 2`
  carriers exist). Uniqueness `{3}` is the intersection.

- **Does NOT derive the carrier bit `phi = -1`** from the axioms. K0
  (`phi = +1`, scalar `H(p) = (sum cos p_mu) I_2`) is an explicit
  constraint-satisfying countermodel; the qubit spectates (`[H, sigma_i] = 0`).
  The whole upper leg is graded by this UNAUDITED bit (B-BIT,
  `STAGGERED_DIRAC_KINETIC_CLASS_FORCING_..._2026-06-10`). The bound's
  **non-vacuity** (not just its conditionality) is UNAUDITED: all carrier-class
  suppliers are landed-but-unaudited.

- **Does NOT derive P-DECAY or P-FIELD** from the axioms. Both are posited;
  P-DECAY is non-unique (finite-relative-response admits `d = 1, 2`); P-FIELD is
  a static field equation the axiom memo defers as open.

- **Does NOT claim the d = 3 leading constant `1/(4 pi)` or the exact `|x|^{2-d}`
  off-diagonal rate are audited** — they inherit UNAUDITED status from
  `LATTICE_GREENS_1_OVER_R_..._2026-06-07`. ONLY the convergence dichotomy
  (`G(0)` finite iff `d >= 3`) is fully native and elementary.

- **Does NOT claim a physical `G_Newton`, SI calibration, lattice-to-meter
  scale, or any gravity coupling.** The kernel is in dimensionless lattice units;
  P-DECAY is sign-blind and does not encode "gravity," only "a non-confining
  static sector exists."

- **Does NOT identify the mediator with the graviton or assert an
  equation-of-motion** beyond Clause C; the matter-is-Grassmann reading needs the
  UNAUDITED spin-statistics input (hard-core-boson hatch, upstream of the
  kinetic-order bit, does not flip `phi`).

- **Does NOT claim carrier-independence.** The upper bound is explicitly
  carrier-DEPENDENT: a second-order scalar carrier evades it entirely.

- **Does NOT exclude** non-site-local (taste-basis multi-site spinor)
  realizations (B-SL), pairing/NNN terms (B-S1/B-S2), or `d = 1, 2` by any
  orbit/atomic/Bertrand textbook route (not consumed).

- **Does NOT set, predict, or promote any audit status.** Source-side proposal
  only.

### Strongest objection, and the honest answer

> "You claim a single dynamics fragment, then admit it is three independent
> clauses — so the 'minimal posit' is a fiction; the honest object is a 3-tuple
> {A, B, C} and the unifying prose adds nothing."

Largely CORRECT and not hidden. The unification is real in exactly one respect
(the same `L` appears as `D^2` and as the static-kernel generator, so one
sentence names both legs' dependence on `L` — and even that is only an IR-symbol
match, not a lattice operator identity) and cosmetic in all others. The selecting
content is irreducible to {A, B, C}: A and B are provably orthogonal, and C is a
third input neither supplies. The defensible claim is "**one dynamics stencil
spanning three separable clauses, unified only by sharing `L` in the leading
continuum symbol.**" The convergence dichotomy and the `M_2(C)` cap are the only
fully-native, elementary, runner-certified pieces; the d = 3 tail constant
`1/(4 pi)` remains UNAUDITED. This is a strict auditability improvement over two
textbook imports, not a closure.

---

## CROSS-REFERENCES

- [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) — the Lattice
  and Quantum axioms; open-gates section deferring source/action and
  equation-of-motion identification. (Canonical; **not edited.**)
- [`ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md`](ADJACENCY_RANK_QUBIT_CLIFFORD_BOUND_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the native upper-leg algebraic core (T1-T4); landed but UNAUDITED.
- [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
  — the two-flux-class collapse, absorbing-frame, and the B-BIT (`phi = -1`)
  countermodel; the weakest-link carrier dependency; bounded_theorem, UNAUDITED.
- [`INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md`](INDEX_PAIRING_NOT_FORCED_KINETIC_ORDER_SELECTOR_NO_GO_NOTE_2026-06-08.md)
  — the kinetic-order selector no-go, the spectator `H(p) = (sum cos p) I_2`, and
  the #2586 guardrail (line 117/180: `M_2(C) = Cl(3,0)` is consistency, not a
  spatial-d derivation).
- [`DIMENSION_SELECTION_NOTE.md`](DIMENSION_SELECTION_NOTE.md) — the lower leg
  whose imported continuum potential family (Runner Surface step 2) this proposal
  retires; retained_bounded.
- [`D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md`](D3_PINCH_NATIVE_UPPER_LEG_DIMENSION_SELECTION_COMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-11.md)
  — the native Z^d transience surrogate promoted here to PRIMARY lower leg;
  bounded_theorem, UNAUDITED.
- [`LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md`](LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md)
  — the lattice heat-kernel/Bessel resolvent and the `1/(4 pi)` tail constant;
  landed but UNAUDITED (local-CLT tail-domination step open).
- [`LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
  — the stencil and the `retained_bounded` `1/(4 pi r)` asymptotic.
- [`DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md`](DIMENSION_SELECTION_UPPER_BOUND_TEXTBOOK_IMPORT_NOTE_2026-05-17.md)
  — the RETIRED orbit-stability upper route (self-admits "`Cl(3) (x) Z^3` has
  d = 3 built into the substrate ... complementary self-consistency check, not a
  framework derivation"); superseded by the native ADJACENCY_RANK leg, NOT
  load-bearing here.

**No-promotion statement:** this note does not promote, demote, or set the audit
status of any dependency. It changes no axiom memo and registers no primitive.
The independent audit lane is the only status authority.
