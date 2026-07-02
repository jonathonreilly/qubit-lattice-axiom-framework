# AC_phi_lambda Projective Equivariance And The K-Odd Equivariant Trace

**Date:** 2026-07-02
**Claim type:** bounded theorem / mechanism assembly
**Status authority:** independent audit lane only. This note does not set an audit verdict, edit registries, register primitives, change axioms, or claim `AC_phi_lambda` retirement.
**Primary runner:** [`scripts/acphilambda_projective_equivariance_k_odd_trace_2026_07_02.py`](../scripts/acphilambda_projective_equivariance_k_odd_trace_2026_07_02.py) (`TOTAL: PASS=60 FAIL=0`, deterministic, measured below).

## Claim

T10-1 realizes the projective seed on a concrete retained-class operator: the projective equivariance is realized exactly on the retained-class two-component surface (`R2^3 = -I`). On the even torus used for the dense check, `[R2, H_D] = 0` and `R2^3 = -I` hold to exact dense arithmetic, while the heat traces obey `Tr(f(H_D) R2^2) = -Tr(f(H_D) R2)`.

T10-2 identifies the branch structure on the `[111]` diagonal fixed momenta. The spin lift supplies `Z_6` weights `exp(-i pi/3)` and `exp(+i pi/3)` on the two `n.sigma` branches, and the sector-distinguishing weights are torsion phases (`+- pi/3`), so at zero flux no R-valued off-locus datum appears.

T10-3 composes the projective carrier with a diagonal flux dial. For the naive Wilson-free operator, on even diagonal grids the naive K-odd trace vanishes identically: the doubler pairing annihilates it. Odd rings and Wilson-type pairing-breaking terms evade that cancellation; the K-odd observable exists at the generation ring size `N = 3` and requires doubling-pairing breaking elsewhere, but what value it registers remains the wall. This is not a terminal no-go.

## Frame And Retained Inputs

The load-bearing markdown dependency is [docs/STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md).

Ledger scope quote (retained_bounded): "On the adjacency-licensed Q-conserving nearest-neighbor bilinear surface over per-site C^2, imposing translation and proper-cubic covariance up to local U(1) frame gives exactly two gauge/scale classes K0 and K1; the K1 branch has the stated site-local absorbing frame uniqueness, and K0 shows the flux(-1) selector is not forced."

Campaign context is PR #4783 `ACPHILAMBDA_DEFECT_IDENTITY_UNIT_RESCALE_OBSTRUCTION_2026-07-01`; PR #4788 `ACPHILAMBDA_REGISTRABLE_CYCLE_HOLONOMY_NORMAL_FORM_2026-07-01`; PR #4789 `ACPHILAMBDA_REAL_HOLONOMY_LOCUS_IDENTITY_2026-07-01`; PR #4794 `ACPHILAMBDA_FLUXED_RING_SPECTRAL_FUNCTIONAL_ROUTE_NO_GO_2026-07-02`; PR #4798 `ACPHILAMBDA_POINTER_LABELED_REFINEMENT_FINER_RECORD_CLOCK_2026-07-02`; PR #4803 `ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02`; PR #4831 `ACPHILAMBDA_AMBIENT_SCALAR_K_BLINDNESS_PROJECTIVE_CARRIER_2026-07-02`; and PR #4835 `ACPHILAMBDA_K1_STAGGERED_K_BLINDNESS_REAL_LIFT_2026-07-02`.

The calculational carrier is the naive two-component nearest-neighbor Dirac bilinear on the finite `Z_N^3` torus:

```text
H_D = sum_mu sigma_mu (x) (T_mu - T_mu^T) / (2 i).
```

Here `T_mu` are periodic shifts, `sigma_mu` are the Pauli matrices, `U = (I - i(sigma_x + sigma_y + sigma_z))/2`, `R` is the `C3[111]` site rotation cycling the axes, and `R2 = U (x) R`.

This `H_D` is a retained-CLASS representative used as a reconstruction device and calculational carrier. Its physical selection is not claimed. The kinetic-class row's one-bit selector and absorbing-frame content are not consumed beyond the licensed per-site `C^2` nearest-neighbor bilinear surface.

The only wall names used here are `W_cycle_holonomy_value`, `W_defect_identity_unit`, and `W_defect_readout_selection`. The observable introduced below is an observable type, not another wall.

## Projective Equivariance Realized (T10-1)

The spin lift satisfies `U^3 = -I`. Its adjoint action cycles the Pauli matrices:

```text
U sigma_x U^* = sigma_y,
U sigma_y U^* = sigma_z,
U sigma_z U^* = sigma_x.
```

The site rotation cycles the shift operators in the same order. Therefore the full two-component lift satisfies `[R2, H_D] = 0`, and the cube is projective:

```text
R2^3 = -I (x) I.
```

At `N = 4`, the dense runner checks these identities on the full `128`-dimensional two-component lattice. For heat weights `f(x) = exp(-t x)`, it also checks:

```text
t = 0.5:  Tr(f(H_D) R2) =  4.798063...,  Tr(f(H_D) R2^2) = -4.798063...
t = 1.0:  Tr(f(H_D) R2) =  7.829155...,  Tr(f(H_D) R2^2) = -7.829155...
```

The sign is the projective sign identity from PR #4831 realized on the full lattice operator. The scalar one-component comparator at the same `N` has `Tr(f(H) R) = Tr(f(H) R^2)`, so the two-component projective sign is a genuine discriminator.

## Branch Structure And Torsion Weights (T10-2)

On the `[111]` diagonal momenta, the fixed set used by PR #4803 remains fixed after tensoring with the spinor factor. The Bloch Hamiltonian is

```text
H(kappa) = sin(kappa) (sigma_x + sigma_y + sigma_z)
         = sqrt(3) sin(kappa) (n.sigma).
```

Since `U` is a function of the same `n.sigma`, the Bloch Hamiltonian commutes with `U`. The `n.sigma = +1` branch carries `U`-weight `exp(-i pi/3)` and the `n.sigma = -1` branch carries `U`-weight `exp(+i pi/3)`.

The dense trace reduces to the diagonal fixed-momentum sum:

```text
Tr(f(H_D) R2)
  = sum_kappa [
      f(+sqrt(3) sin kappa) exp(-i pi/3)
    + f(-sqrt(3) sin kappa) exp(+i pi/3)
    ].
```

The runner derives the branch weights symbolically, verifies the dense-versus-reduction equality at `N = 4` for `t = 0.5` and `t = 1.0`, and checks that setting the spinor weights to `1` breaks the equality.

This is the radian-note division of labor at zero flux. Torsion/root-of-unity phases are `q*pi` Type-A objects. They distinguish projective sectors but do not supply an R-valued off-locus datum. The off-locus content must come from the flux dial.

## The Composed K-Odd Observable (T10-3)

Thread a uniform `[111]` flux by the diagonal twist: every forward hop receives phase `exp(i phi/N)`, and every backward hop receives the conjugate phase. Define

```text
A(phi) = Im Tr(exp(-t H(phi)) R2).
```

The dense flux trace matches the diagonal reduction at `N = 3` and `N = 4`. The reduction replaces `sin(kappa)` by `sin(kappa + phi/N)`.

Gate 1 is the doubler-cancellation theorem. On even diagonal grids, `kappa -> kappa + pi` is a bijection, the sine flips sign, and the two branches swap. The imaginary parts cancel pairwise for all flux. The runner proves the symbolic `N = 4` pair cancellation and checks `A_naive(4, 0.7) = 0` and `A_naive(6, 0.7) = 0`.

Gate 2 is the odd-ring witness. For `t = 0.7`, the naive operator has

```text
A_naive(3, 0.7) = -0.272282888817,
A_naive(3, -0.7) = -A_naive(3, 0.7),
A_naive(3, 0) = 0.
```

The odd diagonal grid is not invariant under the pi-shift, so the K-odd trace is generically nonzero and flux-odd.

Gate 3 is pairing-breaking on even rings. Add the Wilson-type on-site spin-identity term

```text
W(k) = r * 3 * (1 - cos k).
```

It is a real function of the scalar lattice Laplacian tensored with identity, so it preserves `R2` covariance. At `r = 1/2` and `t = 0.7`, the runner checks

```text
A_wilson(4, 0.7) = -0.017277781723,
A_wilson(4, -0.7) = -A_wilson(4, 0.7),
A_wilson(4, 0) = 0,
A_wilson(3, 0.7) = 0.126068832665.
```

At the special point `r = 1`, `t = 1`, even-`N` values can vanish accidentally; the runner observes this at `N = 6`, while the generic gate at `(r, t) = (1/2, 7/10)` is nonzero. This special-point vanishing is an observed curiosity, unexplained and not load-bearing.

Gate 4 is finite-ring nativeness. At fixed `(phi, t) = (0.7, 0.7)`, the observed naive magnitudes satisfy

```text
|A_naive(3)| > |A_naive(5)| > |A_naive(7)|.
```

No asymptotic claim is made. The largest tested instance is at `N = 3`, the generation ring.

Rescale honesty remains unchanged: nothing pins `phi` or a value. PR #4783 applies. The runner checks that replacing `H` by `lambda H` while replacing `t` by `t/lambda` reproduces `A`.

The consequence is narrow. The composed K-odd observable exists on the two-component surface, but it requires doubling-pairing breaking through odd rings or Wilson-type terms on even lattices. Wilson/torsion structures here only break the pairing so the R-valued flux content can register; the `q*pi` Type-A restriction on torsion phases as value sources is untouched. What value it registers remains the wall.

## What This Moves

| Input shape | This assembly moves it to |
|---|---|
| projective seed, algebraic | realized exact equivariance on a retained-class operator |
| K-breaking existence | constructive observable: K-odd and flux-odd |
| mechanism shape | assembled: projective carrier x flux dial |

## What Does Not Move

| Boundary | Status here |
|---|---|
| value | not derived; the flux value = the wall |
| carrier physical-selection | not derived; `H_D` is a class representative |
| occurrence | not derived; whether the surface is realized remains separate |
| chirality/K-reality admissions | not consumed as closed premises |
| `W_cycle_holonomy_value` | still open as value content |
| `W_defect_identity_unit` | still open as unit content |
| `W_defect_readout_selection` | still open as readout-selection content |

## Audit Consequence If Retained

If retained, this note changes the source-side map by realizing the PR #4831 projective seed and the PR #4835 two-component requirement on a concrete retained-class operator. It also names and gates the K-odd observable that the flux dial can feed.

It does not retire `AC_phi_lambda`, derive a numerical `phi`, select the physical dynamics, or alter the audit lane. The value problem is explicitly still carried by the named wall structure.

## Non-Claims

- This note does not claim `H_D` is the physical dynamics.
- This note does not claim the K1 absorbing frame was used.
- This note does not derive `phi`.
- This note does not claim occurrence of the two-component carrier in realized records.
- This note does not claim a value for `A(phi)`.
- This note does not edit any registry, queue, primitive list, axiom text, or audit verdict.

## No-Go Discipline Gate

**Status:** PASS bounded; not a terminal no-go.

- **N1 alternative routes.** Zero-flux two-component route gives torsion-only K-breaking, no R-valued datum, as shown here. Composed flux route remains open as the assembled shape with value = the wall. Occurrence lane remains open separate. Owner primitive remains GOVERNANCE.
- **N2 wall independence.** The K-odd observable is an observable type, not a wall. The existing wall names remain `W_cycle_holonomy_value`, `W_defect_identity_unit`, and `W_defect_readout_selection`.
- **N3 hidden-wall scan.** `H_D` is a retained-class representative and reconstruction device. `diagonal twist` is the holonomy dial in ambient form. `K-odd trace` is a defined object. `torsion weights` are group theory.
- **N4 residual matching.** PR #4831 and PR #4835 supply the seed and requirement now realized. PR #4789 and PR #4798 move from K-breaking vocabulary to a constructive observable. PR #4794 and PR #4783 remain value untouched, with rescale freedom persisting.
- **N5 proven.** Exact equivariance, exact projective cube, diagonal reduction, and the four `A(phi)` gates at the stated `N` are proven or instance-gated by the runner.
- **N6 live paths.** Compute what the K-odd observable registers on the record-facing surface. Occurrence remains live. Owner primitive remains live.
- **N7 steelman.** A hostile reviewer can say "`H_D` is a choice, not a derivation." Reply: it is the canonical retained-CLASS representative and only the class license is consumed; the assembly statement is class-level, because any covariant member realizes the projective equivariance. Concession: physical selection and value are not derived.
- **N8 echo.** This follows the assembly-after-localization pattern. The lesson is to name the observable type first, then test what content it can register.

## Verification

Run:

```text
python3 scripts/acphilambda_projective_equivariance_k_odd_trace_2026_07_02.py
```

Measured close on 2026-07-02: `TOTAL: PASS=60 FAIL=0`, runtime under 90 seconds.
