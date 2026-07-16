# Exact antiunitary symmetry of the free staggered Hermitian lift

**Claim type:** positive_theorem

**Status authority:** independent audit lane only. This source note proposes
the bounded finite-lattice theorem below for independent re-audit; it does not
set or predict an audit verdict.

**Primary runner:** `scripts/frontier_cpt_exact.py`

## Scope

This note treats the free one-component staggered hopping operator on the
finite periodic lattice

```text
Lambda_L = (Z / L Z)^3,                 L even,
D_xy = (1/2) sum_mu eta_mu(x)
       [delta_{y,x+e_mu} - delta_{y,x-e_mu}],
eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}.
```

It distinguishes the real anti-Hermitian hopping operator `D` from its
physical Hermitian lift

```text
H = i D.
```

On the canonical site basis define the real unitaries

```text
C_xy = epsilon(x) delta_xy,             epsilon(x)=(-1)^{x_1+x_2+x_3},
P|x> = |-x mod L>,
```

and let `K` denote componentwise complex conjugation. The labels in this note
refer only to these explicitly defined finite-matrix operators. In particular,
the physical-Hamiltonian time-reversal representative is declared to be

```text
T_H := C K,
```

not bare `K`. The corresponding composite is

```text
Theta_H := C P T_H = P K,
```

where the last equality uses `[C,P]=0` and `C^2=I` on this even periodic
lattice.

## Theorem

For every even `L`:

1. `D` is real and anti-Hermitian, and `H=iD` is Hermitian with `H^*=-H`.
2. The unitary actions satisfy

   ```text
   C D C = -D,             P D P = -D,             C P D P C = D,
   C H C = -H,             P H P = -H,             C P H P C = H.
   ```

3. Bare conjugation and the old three-factor lift are sign flips of the
   Hermitian Hamiltonian, not symmetries:

   ```text
   K H K^{-1} = -H,
   C P K H (C P K)^{-1} = -H.
   ```

4. The declared physical-Hamiltonian representatives preserve `H`:

   ```text
   T_H H T_H^{-1} = (C K) H (C K)^{-1} = H,
   Theta_H H Theta_H^{-1} = (P K) H (P K)^{-1} = H,
   Theta_H = C P T_H.
   ```

5. Consequently the full and direction-resolved `Theta_H`-odd
   Hamiltonian-sector matrices vanish:

   ```text
   H_odd       = (H       - Theta_H H       Theta_H^{-1}) / 2 = 0,
   H_{mu,odd}  = (H_mu  - Theta_H H_mu Theta_H^{-1}) / 2 = 0.
   ```

The runner reconstructs these matrices and checks the identities entrywise on
`L=4,6,8`. Those computations are finite-instance witnesses; the all-even-`L`
statement follows from the algebra below.

## Proof

The entries of `D` are real. A hop in direction `mu` does not change any
coordinate entering `eta_mu`, so exchanging the endpoints reverses only the
forward-minus-backward sign. Thus `D^T=-D`, hence `D^dagger=-D`, and

```text
H^dagger = (iD)^dagger = -i D^dagger = iD = H,
H^* = (iD)^* = -iD = -H.
```

Every nonzero matrix element of `D` joins opposite sublattices. Therefore
`epsilon(x)epsilon(y)=-1` on every contributing link and `C D C=-D`.

For parity,

```text
(P D P)_{x y} = D_{-x,-y}.
```

Because `L` is even, `(-x_nu mod L)` has the same parity as `x_nu`, so
`eta_mu(-x)=eta_mu(x)`. Reversing both endpoints interchanges the forward and
backward Kronecker deltas, giving `D_{-x,-y}=-D_{x y}` and hence `P D P=-D`.
The same argument holds separately for each direction `D_mu`.

Also `epsilon(-x mod L)=epsilon(x)`, so `C` and `P` commute. Their two sign
flips therefore give `CP D (CP)^{-1}=D`. Multiplication by the scalar `i`
gives the stated unitary actions on `H`.

The antiunitary signs must instead carry `K(i)=-i`. Since `H^*=-H`,

```text
K H K^{-1} = -H,
(C P K) H (C P K)^{-1}
  = C P H^* P C
  = - C P H P C
  = -H.
```

By contrast, either single spectral-flip unitary cancels the conjugation
sign:

```text
(C K) H (C K)^{-1} = C H^* C = - C H C = H,
(P K) H (P K)^{-1} = P H^* P = - P H P = H.
```

Finally, using `[C,P]=0` and `C^2=I`,

```text
C P T_H = C P C K = P K = Theta_H.
```

The `Theta_H`-odd projections vanish immediately, direction by direction as
well as for their sum. This proves the theorem. ∎

## Discrete-action table on `H=iD`

| Operation | Action on `H` | In-scope conclusion |
|---|---:|---|
| `C` | `H -> -H` | unitary spectral flip |
| `P` | `H -> -H` | unitary spectral flip |
| bare `K` | `H -> -H` | not the declared `T_H` |
| `T_H=C K` | `H -> H` | antiunitary symmetry |
| `C P` | `H -> H` | unitary symmetry |
| `C T_H=K` | `H -> -H` | antiunitary spectral flip |
| `P T_H=P C K` | `H -> -H` | antiunitary spectral flip |
| `C P T_H=Theta_H=P K` | `H -> H` | antiunitary symmetry |

This table replaces the inconsistent table that treated the anti-Hermitian
`D` as a real physical Hamiltonian and consequently called bare `K` and
`CPK` symmetries of `H=iD`.

## Boundary

The theorem does not identify the zero `Theta_H`-odd hopping sector with a
complete canonically normalized Standard-Model Extension coefficient basis.
It does not cover interactions, CKM phases, gauge or Yukawa couplings, or the
continuum Wightman/Jost CPT theorem. It also does not infer physical parity or
charge-conjugation violation merely from the one-particle spectral flips.

`PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md` and
`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md` are
non-load-bearing consistency cross-checks for the same `i -> -i` algebra; the
proof above is self-contained.

## Verification

```bash
python3 scripts/frontier_cpt_exact.py
```

The runner rejects odd `L`, reconstructs `D` and `H=iD` independently for
`L=4,6,8`, and reports exact entrywise identities together with the explicit
counterchecks `K:H->-H` and `CPK:H->-H`.
