# Wall mechanism — exact cheap probes

SymPy-exact throughout. Sites are time-major `(t,x)`, `t=0..7`, `x=0..3`; the positive half is `t=0..3`. Local order is `(00,01,10,11)`, unsigned `P4` swaps local time rows, and the x-minimal landing sum is divided by two. `d00` is real; the displayed `i` occurs in `Q`.

## Control

At the E02 seam, `s=1/5`, `m=9/20`, entrywise simplification gives `K=K.H` and `rank(K)=12`. Exact Hermitian congruence elimination gives

`inertia(K)=(+6,-6,0x4)`.

## P1 — kernel

Write `tx:z` for value `z` at site `(t,x)` and omit zeros. An exact basis, normalized by `vj(2,j)=1`, is

```
v0 = {01:-1303*i/90, 02:45/32, 10:1303*i/120, 11:-1303/160, 20:1}
v1 = {01:2606/135, 02:17369*i/696, 03:9387346/244755,
      10:-1303/90, 11:-1303*i/120, 12:-98775011/2365965, 21:1}
v2 = {00:14/25, 03:-70607*i/8325, 12:70607*i/11100,
      13:-70607/14800, 22:1}
v3 = {00:752704*i/34425, 01:36484/1215, 03:282428/24975,
      10:-473689/13770, 12:-70607/8325, 13:-70607*i/11100, 23:1}
```

Exact multiplication gives `K*vj=0`. The free data are the four `t=2` values; every kernel vector vanishes on wall-adjacent `t=3`. Supports form two `x -> x+2` orbits (`v0/v2`, `v1/v3`), although nonuniform amplitudes prevent translation symmetry. Anchored at `(2,j)`, sites of the anchor's `t+x` parity are real and the opposite parity purely imaginary.

Replacing E02 by the E13 (b5-type) seam leaves the kernel subspace identical at each fixed mass. For both seams, masses `9/20,1,2` retain rank 12, the four support masks, `t=3` vanishing, and the phase rule. Mass changes the rational amplitudes and the actual span: stability across mass is structural, not pointwise.

## P2 — odd moments

The fully reduced exact rationals have positive numerators and denominators:

`tr(K^3)>0`, `tr(K^5)>0`.

Their approximate sizes are `2.53065227834e-6` and `3.16365990791e-9`. The outermost positive eigenvalue is `0.0271171`, versus negative magnitude `0.0264239`; positive/negative odd-power magnitude ratios rise from `1.0610` (cube) to `1.1446` (fifth). The imbalance is a heavier positive outer tail, not an inertia-count imbalance.

## P3 — off-diagonal-block reading

For b185 I used the `4x4` physical lattice, positive order `(t,x)=(0,0..3),(1,0..3)`, staggered temporal edges `+/-1/2` with the `t=3 -> 0` antiperiodic flip, `eta_x=(-1)^t`, and the degree-raising part for degree `(t mod 2)+(x mod 2)`. `P0(t,x)=(3-t,x)`, `c=5/13`, `H_image=H=diag(1,c,c,1) tensor I4`; `A` contains the positive half plus both temporal seams. With the same `m=9/20`, let `J0=P0[-,+]` and `B185=G185[+,-]J0`. For

`M(a,b)=[[a,0,b,0],[0,a,0,b],[b,0,a,0],[0,b,0,a]]`,

the exact Gram is

`K185=B185=diag(M(48635600,13520000),M(126452560,35152000))/80718609`.

Its eigenvalues are `5200/6753`, `5200/11953`, `13520/6753`, `13520/11953`, each twice: inertia `(+8,0,0)`.

Structurally, b185 has `Q.T=P0 Q P0`: diagonal `G` half-blocks have 48/64 nonzeros, raw off-diagonal blocks 16/64, and reflection exposes four real-symmetric positive `2x2` parity blocks; the antisymmetric part is zero. b186 has `Q.H=Px Q Px`: every `16x16` `G` block has 160/256 nonzeros, and `B186=G186[+,-]Jx=K` is complex Hermitian. Exactly, `Re(B186)` is symmetric (64 nonzeros, rank 16) and `Im(B186)` real antisymmetric (96 nonzeros, rank 16), with disjoint supports, yet their Hermitian combination has rank 12. The imaginary chart part is therefore the interference channel creating the four zero modes and balanced indefiniteness, not a removable phase.

## Ten-line summary

1. The b186 E02 control is exactly Hermitian, rank 12, with inertia `(6,6,4)`.
2. Its kernel has the four exact anchored vectors displayed above.
3. All kernel vectors vanish on `t=3`; their free data live on `t=2`.
4. Kernel supports form two `x -> x+2` orbits with an exact checkerboard phase.
5. E02 and E13 give the identical kernel subspace at each fixed tested mass.
6. Masses `9/20,1,2` preserve nullity/support/phase but change the actual span.
7. Exact arithmetic gives `tr(K^3)>0` and `tr(K^5)>0`.
8. The odd-moment excess sits in the slightly heavier positive spectral tail.
9. b185 gives four sparse real positive `2x2` blocks; b186 is much denser.
10. b186's full-rank real-symmetric and imaginary-skew pieces cancel to rank 12.
