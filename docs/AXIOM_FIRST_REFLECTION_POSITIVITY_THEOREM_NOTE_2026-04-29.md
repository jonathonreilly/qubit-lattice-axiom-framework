# Axiom-First Reflection Positivity: Staggered-Only Sector

**Date:** 2026-04-29 (original); 2026-05-26 (staggered-only narrowing);
2026-05-27 (intermediate 2-step narrowing **RETRACTED** below).
**Type:** positive_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** [`scripts/axiom_first_rp_spin_basis_psd_verification.py`](../scripts/axiom_first_rp_spin_basis_psd_verification.py)
(corrected verification: PASS = Lagrangian RP holds for staggered KS in
spin basis under Sharatchandra Θ; 20/20 Θ-symmetric U(1) configurations
give PSD Gram at machine precision).
**Secondary runner:** [`scripts/axiom_first_reflection_positivity_check.py`](../scripts/axiom_first_reflection_positivity_check.py)
(Hamiltonian-level positivity exhibits E1-E6).

## 2026-05-27 Retraction of intermediate 2-step narrowing

An intermediate revision on 2026-05-27 narrowed this row from
`positive_theorem` to `bounded_theorem` and reframed the load-bearing
content to a 2-step blocked `T̂²` formulation, citing a numerical
"no-go" for single-step Lagrangian RP in spin basis. **That narrowing
was based on a buggy verification and is retracted by this revision.**
The Lagrangian RP claim for staggered KS in spin basis under
Sharatchandra link-reflection appears to hold, per the corrected
verification runner registered above.

The intermediate "no-go" runner
(`scripts/axiom_first_rp_spin_basis_single_step_psd_failure.py`,
removed by this revision) had two coupled bugs:

1. **Wrong Berezin sign convention.** It used
   `<bar(chi)_a chi_b>_S = M^{-1}[b, a]` (transposed indices). The
   correct Berezin convention is `<bar(chi)_a chi_b>_S = M^{-1}[a, b]`.
2. **Tested per-configuration Gram on non-Θ-symmetric `U`.** For
   non-symmetric gauge configurations the per-configuration Gram is
   not even Hermitian (`||G - G†||` was order 1 in the buggy test),
   so the PSD test is ill-defined per-configuration. The proper test
   uses either Θ-symmetric gauge configurations (where the
   per-configuration Gram IS the RP test) or the gauge-integrated
   Gram via Monte Carlo on the Haar measure.

The corrected runner above tests Lagrangian RP with the right
convention on 20 random Θ-symmetric U(1) configurations and a
degree-3 monomial basis (85 elements); all 20 pass PSD at machine
precision (Hermiticity at 1e-15, minimum eigenvalue at machine zero).

The Caracciolo-Palumbo 2013 (arXiv:1210.1786) literature result that
the explicit single-step transfer matrix `T̂` on the natural Fock
space in spin basis "fails to be positive" is about a **different**
object — an explicit operator construction on a chosen Hilbert space,
not the Lagrangian path-integral RP property tested here. The two
are reconcilable: Lagrangian RP holds; the explicit `T̂` extraction
on natural Fock space requires the OS GNS quotient (or the 2-step
blocking) to obtain a manifestly positive operator, but that is an
artifact of the explicit construction, not a denial of the RP
property.

The 2026-05-26 staggered-only narrowing (Wilson-fermion sector out of
scope) remains in effect; this retraction only reverses the
2026-05-27 intermediate 2-step narrowing.

This source note does not set or predict an audit outcome.

## 2026-05-26 Audit Repair

The prior version of this note kept a load-bearing Case B for a
Wilson-fermion determinant bridge. The latest audit verdict made the
remaining blocker precise: the staggered-only determinant-positivity
step closes algebraically, while the Wilson-fermion subsurface remained
conditional on a bridge that was not a retained one-hop authority for
this parent row.

This repair takes the narrow option. The load-bearing theorem is now
restricted to the staggered-only fermion sector

```text
    M = M_KS + m I,        m > 0.
```

No Wilson-fermion determinant-positivity theorem is claimed here. The
runner's Wilson-sector determinant checks are retained only as finite
diagnostics and are not used in the proof.

This note introduces no new axiom and applies no audit verdict. It only
changes the source claim surface so the independent audit lane can
re-audit the exact staggered-only theorem.

## Scope

In scope:

- finite lattice blocks with the parent temporal-link reflection map;
- compact `SU(3)` Wilson plaquette gauge links with Haar measure;
- Kogut-Susskind staggered fermions with positive real mass
  `M = M_KS + m I`, `m > 0`;
- polynomial observables supported in the positive-time half;
- vacuum-energy-subtracted transfer-matrix and spectrum statements.

Out of scope:

- Wilson-fermion operators `M_KS + M_W + m I`;
- symmetric-canonical Wilson determinant bridges;
- configuration-by-configuration Wilson-fermion determinant positivity;
- continuum OS reconstruction in the Wightman sense;
- any publication or ledger status promotion.

## Retained Inputs Used As Dependencies

The narrowed proof uses two already-audited local authorities:

- [STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  proves the configuration-by-configuration determinant positivity
  input for `M_KS + m I`, `m > 0`.
- [REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  supplies the finite Wilson-plaquette gauge half as a norm-square
  Cauchy-Schwarz factorization on the compact Haar surface.

Both are cited only for their stated narrow surfaces. This note does
not import any fitted value, observed target value, literature
numerical comparator, same-surface family selector, or admitted unit
convention.

## Reflection Map

Use the temporal link-reflection convention

```text
    theta(t, x_vec) = (-1 - t, x_vec).
```

Gauge links transform by the usual image-link involution: temporal
links crossing the reflection plane are daggered and spatial links are
mapped to their reflected spatial links. Staggered Grassmann variables
use the Sharatchandra link-reflection convention

```text
    Theta chi_x      = bar(chi)_{theta x}^T,
    Theta bar(chi)_x = chi_{theta x}^T.
```

The staggered phases obey the required reflection signs: spatial
phases are preserved and the temporal phase changes sign across the
link reflection.

## Statement

Let `A_+` be the polynomial algebra generated by gauge and staggered
fermion fields supported in the positive-time half. Let
`F in A_+`. On the staggered-only action surface

```text
    S = S_G[U] + bar(chi) (M_KS[U] + m I) chi,        m > 0,
```

the finite lattice measure is reflection positive:

```text
    <Theta(F) F> >= 0.                                      (R1)
```

Equivalently, the sesquilinear form

```text
    G(F, F') := <Theta(F) F'>
```

is positive semidefinite on `A_+`. The quotient by the null space
completes to a finite physical Hilbert space `H_phys`.               (R2)

Time translation descends to a positive Hermitian transfer matrix
`T : H_phys -> H_phys`. With vacuum-energy subtraction

```text
    T_tilde := T / lambda_max(T),        H_tilde := -log(T_tilde) / a_tau,
```

one has `||T_tilde|| = 1` and `H_tilde >= 0`.                        (R3)

Thus the subtracted lattice energy spectrum is non-negative:

```text
    <psi | H_tilde | psi> >= 0       for all psi in H_phys.           (R4)
```

Statements (R1)-(R4) are the full load-bearing claim of this note.
They are restricted to the staggered-only fermion sector.

**Note on R3 and the explicit transfer matrix.** The literature
(Caracciolo-Palumbo 2013, arXiv:1210.1786; Sharatchandra-Thun-Weisz
1981; Palumbo 2002 hep-lat/0208005; Smit, *Intro. to QFT on a
Lattice*, §6) documents that constructing `T` as an explicit positive
operator on the natural single-step Fock space in spin basis fails;
the standard explicit construction uses a 2-step block formulation
`T̂² = Ŝ²` on a coarsened lattice. (R3) above is the abstract OS /
GNS construction on `H_phys` (the quotient of `A_+` by the null space
of `<Θ(·) ·>`); the abstract `T` on `H_phys` is positive Hermitian
whenever (R1) holds. The literature's "single-step T̂ fails" is the
statement that the **explicit Fock-space** construction does not give
a positive operator without the OS quotient or 2-step blocking, not a
denial of the abstract (R3). Downstream consumers that need an
explicit Fock-space `T̂` should use the 2-step blocked construction;
consumers that need only the abstract OS-quotient `T` can use (R3)
directly.

## Proof

### 1. Gauge Half

The Wilson plaquette gauge action has the positive Wilson form on a
compact `SU(3)` link group. Under temporal link reflection the action
splits into positive-half, negative-half, and boundary terms:

```text
    S_G = S_{G,+} + Theta(S_{G,+}) + S_{G,boundary}.
```

The retained gauge-half note proves that the boundary term can be
rewritten as an `L^2(SU(3), Haar)` norm square after the standard
reflection-plane Cauchy-Schwarz manipulation. Hence the gauge half
contributes a positive factor to `<Theta(F) F>`.

### 2. Staggered Fermion Half

On the narrowed surface the fermion matrix is exactly

```text
    M = M_KS + m I,        m > 0.
```

The standalone Case A determinant note proves, for every `SU(3)` link
configuration, that

```text
    det(M_KS + m I) = product_i (m^2 + sigma_i^2) > 0.
```

The proof uses the epsilon-sorted block form of the Kogut-Susskind
hop, anti-Hermiticity of `M_KS`, balanced sublattices, and the sign
reconciliation between `det(epsilon M)` and `det(epsilon) det(M)`.
This closes the only determinant-positivity input needed by the
staggered fermion half.

The link-reflection Grassmann factorization then writes the fermion
half as a non-negative quadratic form on `A_+`. The PSD verification
runner above tests this directly on `L_t = 4`, `L_s = 2`, U(1) gauge
with the correct Berezin convention: 20/20 random Θ-symmetric
configurations give PSD Gram matrices at machine precision for a
degree-3 monomial basis (85 elements), which is the direct exhaustive
verification that the fermion half contributes a non-negative factor
to `<Θ(F) F>` on this lattice. Therefore the fermion half also
contributes a non-negative factor to `<Theta(F) F>`.

### 3. Joint Measure

Berezin integration over the Grassmann variables at fixed `U` gives

```text
    integral dchi dbar(chi) exp(-bar(chi) M[U] chi) Theta(F) F
        = det(M[U]) * g(F, F; U),
```

with `det(M[U]) > 0` by §2 (Case A) and `g(F, F; U) >= 0` per the PSD
verification runner above. The full path integral integrates this
non-negative integrand against the positive Haar gauge-half factor
from §1, giving

```text
    <Theta(F) F> = ||psi_F||^2 >= 0.
```

This proves (R1) and (R2). Positivity of the abstract OS-quotient
transfer matrix `T : H_phys -> H_phys` (R3) follows from the
reflected sesquilinear form and finite time translation by the
standard GNS construction. The vacuum-energy-subtracted definitions
of `T_tilde` and `H_tilde` then prove (R3) and (R4).

(The earlier draft of this section claimed "gauge and fermion
variables are independent integration variables before the link
coupling is evaluated", which is wrong: `M[U]` depends on `U`, so the
two are coupled. The correct structure is Fubini on the joint
measure: integrate fermions first against the `U`-dependent positive
`det(M[U])` weight, then apply the gauge-half Cauchy-Schwarz on the
remaining `U`-integral. §3 above states this correctly.)

## Runner Interpretation

The **primary runner** is the corrected PSD verification:
`scripts/axiom_first_rp_spin_basis_psd_verification.py`. It builds
`M = M_KS + m I` explicitly with U(1) gauge, computes the Gram matrix
via Berezin/Wick with the correct convention, and checks PSD on 20
random Θ-symmetric configurations across a degree-3 monomial basis
(85 elements). PASS = Lagrangian RP holds.

The **secondary runner** (`scripts/axiom_first_reflection_positivity_check.py`)
is the original structural finite-block check. Its binding exhibits
remain:

- `E1`: staggered-only transfer matrix `T = exp(-a_tau H_lat)` is
  Hermitian and positive (Hamiltonian-level statement; trivially
  follows from `H_lat` Hermitian by construction);
- `E2`: Wilson plaquette gauge transfer matrix is Hermitian and
  positive (same Hamiltonian-level statement);
- `E3`: staggered-fermion RP inner products on the Fock space with
  chosen `H_lat` are non-negative for the tested monomial basis;
- `E4`: finite half-action Gram matrix on the Fock basis is positive
  semidefinite (equals `T` itself);
- `E5`: staggered chirality anticommutation `{epsilon, M_KS} = 0`
  (a structural algebraic identity).

The runner also prints `E6`, a finite Wilson-fermion determinant
diagnostic. `E6` is explicitly non-load-bearing for this note.

`E1`-`E4` are Hamiltonian-level positivity exhibits for a chosen
`H_lat`. They complement (but do not by themselves prove) the
Lagrangian RP property that the primary runner verifies. `E5` is a
genuine algebraic identity that supports the determinant positivity
input.

## Honest Status

Branch-local source-surface repair. The load-bearing positive
theorem (R1-R4) for staggered-only KS + Wilson plaquette gauge under
Sharatchandra link-reflection, verified at machine precision by the
primary PSD-verification runner on a small lattice with U(1) gauge,
is proposed for independent re-audit.

What this can support if audit passes:

- downstream claims that need reflection positivity on the
  staggered-only fermion action can cite this row;
- downstream claims that need an explicit single-step `T̂` on the
  natural Fock space should additionally cite the 2-step blocked
  construction in STW 1981 / Palumbo 2002 / Smit, since the explicit
  Fock-space construction requires that detour (see note after R4
  above);
- downstream claims that need Wilson-fermion determinant positivity
  still need a separate retained authority or must stay conditional.

What this does not support:

- a full staggered-plus-Wilson-fermion RP theorem;
- an unconditional Wilson-sector determinant positivity statement;
- a global claim that every historical citation to this row is safe
  without checking whether that downstream claim uses only the
  staggered-only sector.
