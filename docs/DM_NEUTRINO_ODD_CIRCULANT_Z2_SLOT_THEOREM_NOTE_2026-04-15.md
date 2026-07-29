# Supplied `3 x 3` Hermitian-Circulant / `P_23` Even-Odd Algebra Theorem

**Claim type:** positive_theorem

**Date:** 2026-04-15  
**Status:** exact algebraic identity on the supplied finite-matrix convention

**Primary runner:**
[`scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py`](../scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py)

**Runner cache:**
[`logs/runner-cache/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.txt`](../logs/runner-cache/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.txt)

**Re-audit certificate:** the canonical cache header pins runner SHA-256
`f0b4cf68aef149efa7528d885017cfc8c754e0cb018ef72443a4e19521926cb9`
and a fingerprint of this declared note input. Its unabridged stdout section is
below the legacy `6,000`-character packet limit, includes all 37 named checks,
and terminates with `MUTATION KILLS=6/6` and
`PASS=37 FAIL=0`.

## Question

For the supplied cyclic shift `S` and exchange matrix `P_23`, what is the exact
real coefficient space of `3 x 3` Hermitian matrices commuting with `S`, how
does it split under `P_23`, and what identity is carried by the displayed
zero-based `01` entry?

## Typed theorem surface

**Input.** The displayed finite matrices `S` and `P_23`, zero-based indices,
the Hilbert-Schmidt pairing, and the three displayed basis matrices.

**Output.** The exact Hermitian commutant, unique coefficient extraction,
`P_23` parity multiplicities and odd coordinate, the displayed entry identity,
and the transformation behavior of the coefficient triple and raw `01`
coordinate polynomial.

## Supplied convention

Use zero-based matrix indices and

```text
S = [[0,1,0],       P_23 = [[1,0,0],
     [0,0,1],               [0,0,1],
     [1,0,0]],              [0,1,0]].
```

Then

```text
S^2 = [[0,0,1],     S^3 = I,
       [1,0,0],
       [0,1,0]],
```

`S^dag = S^2`, and `P_23 S P_23 = S^2`. Define the real Hermitian
basis

```text
B_0 = I,
B_+ = S + S^2,
B_- = i(S - S^2).
```

Thus

```text
B_+ = [[0,1,1],     B_- = [[ 0, i,-i],
       [1,0,1],            [-i, 0, i],
       [1,1,0]],            [ i,-i, 0]].
```

## Theorem

The real vector space of `3 x 3` Hermitian matrices commuting with the
supplied `S` is exactly

```text
span_R {B_0, B_+, B_-}.
```

Every member therefore has the unique form

```text
K(d,c_even,c_odd) = d B_0 + c_even B_+ + c_odd B_-,
```

with `d`, `c_even`, and `c_odd` real. For the Hilbert-Schmidt pairing
`<A,B> = Tr(A^dag B)`, the basis Gram matrix and coefficient formulas are

```text
G = diag(3,6,6),

d      = <B_0,K> / 3,
c_even = <B_+,K> / 6,
c_odd  = <B_-,K> / 6.
```

Conjugation by `P_23` gives

```text
B_0 -> +B_0,
B_+ -> +B_+,
B_- -> -B_-.
```

Its parity multiplicities on the Hermitian commutant are therefore
`(2 even, 1 odd)`, and `c_odd` is the unique odd coordinate.

In the displayed basis and entry convention,

```text
K_01 = c_even + i c_odd,
A_01(K) := Im[(K_01)^2] = 2 c_even c_odd.
```

Replacing `K` by `P_23 K P_23` fixes `c_even`, changes `c_odd` to `-c_odd`,
and gives the exact transformation identity

```text
A_01(P_23 K P_23) = -A_01(K).
```

## Exact derivation

The vectors `e_0`, `S e_0`, and `S^2 e_0` form a cyclic basis. A complex
matrix commuting with `S` is consequently a unique polynomial
`a I + b S + c S^2`. Hermiticity uses `S^dag = S^2` and forces
`a` to be real and `c = conjugate(b)`. Writing
`b = c_even + i c_odd` gives the displayed three-real-dimensional basis.

Direct Hilbert-Schmidt multiplication gives the diagonal Gram matrix
`diag(3,6,6)`, proving the coefficient formulas and uniqueness. Direct
conjugation gives the parity action `diag(1,1,-1)`. Finally, squaring the
actual displayed entry gives

```text
(c_even + i c_odd)^2
  = c_even^2 - c_odd^2 + 2 i c_even c_odd,
```

which proves the coordinate identity and its sign under `P_23`.

## Simultaneous basis transformation

For a unitary `U`, transform all supplied matrices together:

```text
K' = U K U^dag,       S' = U S U^dag,
P_23' = U P_23 U^dag, B_j' = U B_j U^dag.
```

Cyclicity of trace gives `<B_j',K'> = <B_j,K>` and preserves the Gram
matrix. The coefficient triple and parity multiplicities are therefore
unchanged. The raw polynomial `Im[(K'_01)^2]` is coordinate-dependent: its
value refers to the `01` entry in the transformed coordinate basis and can
differ from `A_01(K)`.

## Command

```bash
python3 scripts/frontier_dm_neutrino_odd_circulant_z2_slot_theorem.py
```

Expected certificate: `MUTATION KILLS=6/6`, `PASS=37 FAIL=0`.
