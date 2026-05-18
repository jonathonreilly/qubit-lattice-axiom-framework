# Physical Hermitian Hamiltonian And SME Bridge

**Date:** 2026-04-30 (2026-05-18: claim_scope narrowed to the
conditional lattice Theta_H antiunitary statement + zero
Theta_H-odd Hamiltonian-sector proxy per audit verdict boundary
instruction).
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-18 narrowing):** the load-bearing content
of this note is **conditional**: it retains **(i) the lattice theorem
that the free staggered `H = iD` has a valid antiunitary symmetry
`Theta_H = P K`** (where `P` is the standard staggered parity and
`K` is complex conjugation on the canonical staggered basis), and
**(ii) the Hermitian-sector identity `Theta_H · (Theta_H-odd projection
of H) · Theta_H^{-1} = -(...) = 0`** showing that the Theta_H-odd
projection of the free staggered Hermitian Hamiltonian vanishes on
the substrate as a finite matrix proxy. **The further identification
"this implies all CPT-odd SME bilinear coefficients vanish" is
explicitly NOT retained as load-bearing here**: it requires a
separate retained SME bilinear-operator-basis-on-staggered-substrate
derivation showing the proxy spans every CPT-odd bilinear source
under canonical normalization and basis completeness — which the
audit verdict names as a substantive missing-bridge. SME-coefficient
zero statements in the body should be read as **"Theta_H-odd
Hamiltonian-sector proxy vanishes"** under the narrowed scope, not
as unconditional SME-coefficient-zero claims, until the SME basis
representation is separately retained.
**Status authority:** independent audit lane only. The
`proposed_retained` label below is a source-side proposal placeholder,
not an audit verdict; the independent audit lane has classified this
row `audited_conditional` pending the SME basis-completeness
derivation.
**Status:** proposed_retained bridge theorem; audit pending
**Runner:** `scripts/frontier_physical_hermitian_hamiltonian_and_sme_bridge.py`

## Purpose

The existing CPT exact theorem proves the exact staggered identities for the
real anti-Hermitian hopping operator `D`, but its stated claim is about the
physical Hermitian Hamiltonian and vanishing CPT-odd SME sector. The audit gap
is the Hermitization step:

```text
D anti-Hermitian  ->  H physical Hermitian.
```

Because CPT is antiunitary, the factor `i` in `H = i D` must be carried
explicitly. Reusing the `D`-level `CP K` representative without modification
flips `H`; that was the real gap. This bridge records the physical Hermitian
lift and checks the SME-zero statement on that lift.

## Inputs

- The `D`-level staggered identities reconstructed directly by this bridge
  runner: `C D C = -D`, `P D P = -D`, and `CP D CP = D` on even periodic
  lattices.
- The framework Hamiltonian convention used throughout the staggered runners:

  ```text
  H = i D
  ```

  where `D` is the real anti-Hermitian nearest-neighbor staggered hopping
  operator. For example, the generation runners diagonalize
  `h_herm = 1j * staggered_h_antiherm(k)`.

No Standard-Model numerical value, external SME coefficient, fitted selector,
or continuum input is used.

## Theorem Statement

Let `D` be the real anti-Hermitian staggered hopping operator on an even
periodic `Z^3` lattice, and let

```text
H = i D.
```

Let `C` be the staggered sublattice/spectral-flip unitary and `P` the even
periodic inversion unitary, so that

```text
C D C = -D,
P D P = -D,
CP D CP = D.
```

Then:

1. `H` is Hermitian.
2. The naive antiunitary `CP K` that is useful on `D` sends `H` to `-H`, so it
   is not the physical Hermitian CPT representative.
3. The Hermitian Hamiltonian lift uses the antiunitary representative

   ```text
   Theta_H = P K
   ```

   equivalently `Theta_H = C P T_H` with `T_H = C K`. This is the same
   staggered `C/P` algebra with the exact spectral-flip unitary absorbed into
   the antiunitary time-reversal representative to compensate `K(i)=-i`.
4. `Theta_H H Theta_H^{-1} = H`.
5. The CPT-odd Hamiltonian sector

   ```text
   H_odd = (H - Theta_H H Theta_H^{-1}) / 2
   ```

   vanishes identically, including the direction-resolved hopping sectors.
   Therefore all SME coefficients sourced by CPT-odd bilinear Hamiltonian
   terms are zero on this substrate.

## Derivation

### 1. Hermitization

The staggered hopping operator satisfies

```text
D^\dagger = -D.
```

Therefore the physical complex Hilbert-space Hamiltonian is

```text
H = iD,
H^\dagger = (-i)D^\dagger = iD = H.
```

This is the convention already used by the framework's staggered generation
runners when they diagonalize the physical spectrum.

### 2. Why The Naive Lift Fails

The `D`-level combined operation is `CP K`. Since `D` is real and `CP D CP =
D`,

```text
CP K D K CP = D.
```

But

```text
CP K (iD) K CP = CP (-iD) CP = -iD = -H.
```

So the audit concern is valid: `D`-level CPT invariance does not automatically
prove physical-Hamiltonian CPT invariance unless the antiunitary `i` factor is
handled.

### 3. Physical Hermitian CPT Representative

The staggered algebra already has two exact spectral-flip unitaries:

```text
C D C = -D,
P D P = -D.
```

Therefore either `C K` or `P K` is an antiunitary symmetry of `H = iD`, because
the complex conjugation contributes one minus sign and the spectral flip
contributes the second:

```text
P K (iD) K P = P (-iD) P = -i(-D) = iD = H.
```

Choosing `T_H = C K` gives

```text
C P T_H = C P C K = P K
```

on the even periodic lattice, where `C` and `P` commute. Thus the physical
Hermitian CPT representative is the antiunitary `Theta_H = P K`.

This is not an extra symmetry assumption. It uses only the exact `C` and `P`
operators already constructed in the `D`-level theorem, plus the mandatory
antiunitary action `K(i)=-i` in the Hermitization map.

### 4. SME Compatibility

On the substrate Hamiltonian, CPT-odd SME bilinears would appear as the
`Theta_H`-odd part of the Hermitian Hamiltonian or of its direction-resolved
hopping components:

```text
H_odd    = (H    - Theta_H H    Theta_H^{-1}) / 2,
H_mu,odd = (H_mu - Theta_H H_mu Theta_H^{-1}) / 2.
```

The bridge runner checks that all these matrices vanish at machine precision
on even periodic lattices. Direction-resolved trace coefficients, the lattice
analogues of `a_mu`-type CPT-odd bilinear coefficients, are also zero.

## Claim Boundary

This bridge claims only the free staggered Hamiltonian-sector result:

- `D -> H=iD` is Hermitian;
- exact substrate `C/P` identities lift to an antiunitary physical-Hamiltonian
  CPT representative;
- CPT-odd bilinear SME coefficients are zero on that Hamiltonian substrate.

It does not claim:

- interacting CKM-sector CP violation;
- continuum Wightman/Jost CPT theorem replacement;
- full SU(3) Wilson-plaquette operator-level CPT audit;
- any numerical Standard-Model fit.

## Verification

Run:

```bash
python3 scripts/frontier_physical_hermitian_hamiltonian_and_sme_bridge.py
```

Current output:

```text
Summary: PASS=10  FAIL=0
Verdict: PASS.
```

The checks verify:

1. `D^\dagger=-D` and `H=iD` is Hermitian;
2. `C D C=-D`, `P D P=-D`, and `CP D CP=D`;
3. naive `CP K` flips `H`, reproducing the old audit gap;
4. the physical Hermitian antiunitary representative `Theta_H=P K` preserves
   `H`;
5. full and direction-resolved CPT-odd SME sectors vanish.
