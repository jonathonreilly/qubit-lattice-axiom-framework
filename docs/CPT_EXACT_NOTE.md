# Exact antiunitary symmetry of the free staggered Hermitian lift

**Claim type:** positive_theorem

**Status authority:** independent audit lane only. This source note proposes
the finite-lattice theorem below for independent re-audit; it does not
set or predict an audit verdict.

**Primary runner:** `scripts/frontier_cpt_exact.py`

## Scope

This note treats the free one-component staggered hopping operator on the
finite periodic lattice

```text
Lambda_L = (Z / L Z)^3,                 L positive and even,
D_xy = (1/2) sum_mu eta_mu(x)
       [delta_{y,x+e_mu} - delta_{y,x-e_mu}],
eta_mu(x) = (-1)^{sum_{nu<mu} x_nu}.
```

It distinguishes the real anti-Hermitian hopping operator `D` from its
Hermitian lift

```text
H = i D.
```

Write `D=sum_mu D_mu` for the three direction-resolved terms in the displayed
sum and `H_mu=iD_mu`. Below, `M^*` means entrywise complex conjugation, while
`M^dagger` means the Hermitian adjoint.

On the canonical site basis define the real unitaries

```text
C_xy = epsilon(x) delta_xy,             epsilon(x)=(-1)^{x_1+x_2+x_3},
P|x> = |-x mod L>,
```

and let `K` denote componentwise complex conjugation. The symbols `C` and `P`
mean only the displayed sublattice-sign and inversion matrices. For compact
algebraic notation define the antiunitary

```text
T_H := C K,
```

not bare `K`, and define the corresponding composite

```text
Theta_H := C P T_H = P K,
```

where the last equality uses `[C,P]=0` and `C^2=I` on this even periodic
lattice. The names `T_H` and `Theta_H` are labels for these declared matrix
representatives; they do not by themselves identify physical time reversal or
CPT.

## Theorem

For every even `L`:

1. `D` is real and anti-Hermitian, and `H=iD` is Hermitian with `H^*=-H`.
2. The unitary actions satisfy

   ```text
   C D C = -D,             P D P = -D,             C P D P C = D,
   C H C = -H,             P H P = -H,             C P H P C = H.
   ```

3. Bare conjugation and the old three-factor lift are sign flips of the
   Hermitian lift, not symmetries:

   ```text
   K H K^{-1} = -H,
   C P K H (C P K)^{-1} = -H.
   ```

4. The declared antiunitary representatives preserve `H`:

   ```text
   T_H H T_H^{-1} = (C K) H (C K)^{-1} = H,
   Theta_H H Theta_H^{-1} = (P K) H (P K)^{-1} = H,
   Theta_H = C P T_H.
   ```

5. On states, `C`, `P`, `CP`, `K`, `T_H=CK`, `Theta_H=PK`, `CPK`,
   `C T_H=K`, `P T_H=PCK`, and `CP T_H=PK` all square to `I`.
6. Consequently the full and direction-resolved `Theta_H`-odd `H`-sector
   matrices vanish:

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

For inversion,

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

The matrices `C`, `P`, and `CP` are real involutions. For any one of their
real unitary parts `U`, the antiunitary square is `(UK)^2=UU^*`; substituting
the unitary parts in the theorem gives `+I` for every listed antiunitary.

The `Theta_H`-odd projections vanish immediately, direction by direction as
well as for their sum. This proves the theorem. ∎

## Discrete-action table on `H=iD`

| Operation | Action on `H` | Square on states | In-scope conclusion |
|---|---:|---:|---|
| `C` | `H -> -H` | `+I` | unitary spectral flip |
| `P` | `H -> -H` | `+I` | unitary spectral flip |
| bare `K` | `H -> -H` | `+I` | not the declared `T_H` |
| `T_H=C K` | `H -> H` | `+I` | antiunitary symmetry |
| `C P` | `H -> H` | `+I` | unitary symmetry |
| `C T_H=K` | `H -> -H` | `+I` | antiunitary spectral flip |
| `P T_H=P C K` | `H -> -H` | `+I` | antiunitary spectral flip |
| `C P T_H=Theta_H=P K` | `H -> H` | `+I` | antiunitary symmetry |

This table replaces the inconsistent table that treated the anti-Hermitian
`D` as the Hermitian lift and consequently called bare `K` and `CPK`
symmetries of `H=iD`.

## Boundary

The theorem does not identify the zero `Theta_H`-odd hopping sector with a
complete canonically normalized Standard-Model Extension coefficient basis.
It does not cover interactions, CKM phases, gauge or Yukawa couplings, or the
continuum Wightman/Jost CPT theorem. It does not derive an axiom-level or
physical Hamiltonian identification for `H=iD`, and it does not identify the
declared `C`, `P`, `T_H`, or `Theta_H` matrices with physical charge
conjugation, parity, time reversal, or CPT. In particular, no physical
symmetry violation follows from the spectral flips.

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
counterchecks `K:H->-H`, `CPK:H->-H`, and the state-space squares of every
listed representative. The all-even proof includes the degenerate `L=2` case,
where the forward and backward hops coincide and `D=0`; the nonzero executable
witnesses begin at `L=4`.
