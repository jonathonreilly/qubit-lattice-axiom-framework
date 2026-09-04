# Block 190 transfer-theorem package: independent adversarial findings

Date: 2026-08-24

## Scope and method

This is a fresh rebuild from the dispatch equations. No repository runner,
script, scratchpad draft, ledger, or audit-data file was read or imported.
All matrix entries and polynomial computations use exact SymPy `Integer` and
`Rational` arithmetic; `nsimplify` is never used. The only science-source reads
were the permitted landed block-188 note and its named block-105 primary note,
solely to identify/cross-check the displayed shear-Hodge convention.

Status below defaults to **REFUTED** when a stated conjunction has any failed
part. Exact witnesses and narrower surviving subclaims are recorded.

## Hodge convention control

**FAILED / dependent numerical claims unverifiable as stated.** The permitted
block-105 note displays, at `q=5/13`, `s=12/13`,
using zero-based corner indices `0,1,2,3`,

```
B_105 = diag(12/13,13/12,13/12,13/12),
(B_105)12=(B_105)21=-5/12.
```

The literal unit-volume version of the dispatch's fallback characterization is

```
B_fallback = I_4,  (B_fallback)12=(B_fallback)21=-5/13,
```

with `P4 B_fallback P4^T` moving that shear to the `(0,3)` pair on the image
half. Neither rebuild gives the claimed even-core polynomial. Their exact
`T=12,t0=2` factorizations are respectively

```
B_105:
(1975z^2+1953z-2365)(2365z^2+1953z-1975)
(4746925z^4+6783420z^3+13155959z^2-6783420z+4746925)

B_fallback:
(475z^2+468z-565)(565z^2+468z-475)
(272425z^4+393120z^3+755774z^2-393120z+272425).
```

There is a diagnostic smoking gun. Every stated block-190 transfer fingerprint
is reproduced digit-for-digit if, instead, one inserts the different block

```
B_fingerprint = I_4 - 2c^2 E_11 - c(E_12+E_21)
              = B_fallback - (50/169) E_11.
```

That extra `-50/169` diagonal term is absent from both the displayed block-105
matrix and the dispatch's measured fallback characterization. It was not
assumed in the verdicts below; it was used only as a forensic diagnostic of
which hidden convention generated the listed coefficients.

The landed block-188 note's displayed control rational belongs to its distinct
link-route construction, whose complete anchor history is not specified in the
dispatch. I therefore could not honestly rebuild that rational from the allowed
equations. An available same-site auxiliary check also fails: block 188 reports
144 nonzeros in `Q_s-Q_s^T` at `T=8`, whereas all three reconstructions above
give exactly 160. Per the dispatch instruction, numerical claims depending on
this unresolved Hodge/control mismatch are treated as unverifiable, not guessed.

For completeness, every result below records both (i) the literal fallback
rebuild and (ii) the conditional `B_fingerprint` reproduction where it helps
locate the drift.

## Claim verdicts

### C1 — **CONFIRMED** (structural; survives the Hodge fork)

Using both `B_fallback` and `B_fingerprint` at `T=12`:

- `nnz(d_K^2)=0`, `nnz(P_s H P_s-H)=0`, and
  `nnz(P_s Q P_s-Q^T)=0`.
- The `{1,...,5}` by `{7,...,11}` block of `Q` has exactly 0 nonzeros.
- For each `t=1,2,3,4`, the adjacent-pair Gram is exactly symmetric, rank 8,
  and its eight leading principal minors have signs
  `(+,+,+,+,+,+,+,+)`.
- The full `{1,...,5}` Gram is exactly symmetric of rank 8. With the `{1,2}`
  core first, the exact `12x12` Schur complement has 0 nonzeros.

Thus the full Gram is PSD of rank 8, and every claimed adjacent core is PD.
These are exact rank/zero/sign certificates, not floating-point inertia calls.

### C2 — **CONFIRMED-WITH-CORRECTION**

The measurement is confirmed. Under the conditional fingerprint convention,
the exact asymmetry counts `nnz(L_k-L_k^T)` and first witnesses are:

| `t0` | `k` | count | exact witness `(row site,column site,value)` |
|---:|---:|---:|---|
| 1 | 1 | 48 | `((1,0),(1,1),145422475346195642490396923275718125571467225250000/1495093718038339281269037929170050261560040062626809)` |
| 1 | 2 | 40 | `((1,0),(1,1),-5403634372035016000000/4667643472401490244347629)` |
| 2 | 1 | 48 | `((2,0),(2,1),-14207636589760065369005704400467445466080528125000/1495093718038339281269037929170050261560040062626809)` |
| 2 | 2 | 40 | `((2,0),(3,0),-48761134991692534397695312500000000/2549481810650769003025848750664501408781)` |
| 3 | 1 | 48 | `((3,0),(3,1),-4076874963964405257649027298325687534907025000000/498364572679446427089679309723350087186680020875603)` |
| 3 | 2 | 48 | `((3,0),(3,1),533424551347324000000/518627052489054471594181)` |

The literal fallback gives the same count pattern. At `T=8`,
`[tau^2,Q]` has 224 nonzeros under `B_fingerprint` (208 under the fallback),
touching exactly 26 ordered slice pairs in either case; one exact common
witness is `[tau^2,Q]_(0,1)=-5/52`.

Correction: global symmetry of the full shifted pairing is equivalent to the
global commutator vanishing, but symmetry after restriction to one 8-vector
core only requires the corresponding projected commutator block to vanish.
Therefore `[tau^k,G] != 0` is not, by itself, a logical proof that every
restricted `L_k` is asymmetric. The six direct exact witnesses above are the
needed core-level proof.

### C3 — **REFUTED** (construction-control failure)

All stated factors reproduce exactly under `B_fingerprint`, including every
width/parity rigidity equality. They do not follow from the displayed/fallback
Hodge. For example, the fallback exact factors are:

- even core: the `(475,468,-565)`, `(565,468,-475)` quadratics and
  `(272425,393120,755774,-393120,272425)` quartic shown above;
- `T=12,t0=1`: quadratics
  `(1035215,929916,-1231361)` and `(1231361,929916,-1035215)`, with quartic
  `(14025095515625,33542482428000,151944801571006,-37076536879200,15502787315625)`;
- deep odd (`T=16,t0=3` and `T=20,t0=3,5`): the same fallback odd quadratics
  with quartic
  `(1080765625,2584764000,12011368478,-2584764000,1080765625)`.

The factor-degree pattern `(2,2,4)` and all stated width/parity equalities do
survive, but the claimed coefficients are tied to the unprovided
`-50/169 E_11` modification.

### C4 — **CONFIRMED** (structural; survives the Hodge fork)

Exact entrywise residual counts are

```
nnz(V2@T16 - V4@T16) = 0
nnz(V2@T12 - V2@T16) = 0
nnz(V1@T12 - V1@T16) = 0.
```

Meanwhile `K_c(2)-K_c(4)` at `T=16` has 64 nonzeros under the fingerprint
convention (56 under the fallback). A fingerprint-convention witness is

```
(K_c(2)-K_c(4))[0,0]
= 50486222621769227870194350340801954963498956737115692109077855728198836415842162500
  /625153395735588698406917309909394882686762786726111537781553541647600283119152251871.
```

### C5 — **CONFIRMED** (structural; survives the Hodge fork)

At both `T=12` (`V1` versus `V3`) and `T=16` (`V1` versus `V5`), the primitive
degree-8 coefficient vectors obey exactly

```
q_j = (-1)^j p_(8-j),  j=0,...,8,
```

with zero coefficient residual. Equivalently,
`q(z)` is proportional to `z^8 p(-1/z)`, proving
`spec(V_mirror)={-1/lambda: lambda in spec(V)}` with multiplicity.

### C6 — **REFUTED** (numerical package); structural core confirmed

Under `B_fingerprint`, the claim reproduces exactly at `t0=3,4`, and the third
probe `t0=5` gives the same result:

```
charpoly(W) proportional to
(22569375z^2-233631106z+22569375)^2
(39529825z^2-109432706z+39529825)^2.
```

Also, `nnz(W-V^2)=32` at each of `t0=3,4,5`. Exact witnesses are

```
t0=3: (W-V^2)[0,4] =  53601896033238042551256/229758595220483765728625
t0=4: (W-V^2)[0,4] = -46628656073521939366872/229758595220483765728625
t0=5: (W-V^2)[0,4] =  53601896033238042551256/229758595220483765728625.
```

But the literal fallback Hodge instead gives, identically at all three cores,

```
(164375z^2-1629374z+164375)^2
(272425z^2-755774z+272425)^2.
```

Thus parity independence, `W != V^2`, reciprocal form, and positivity survive;
the stated coefficients do not pass the construction control.

### C7 — **CONFIRMED** (structural coefficient identity)

For the conditional fingerprint data, the even-`V` quartic begins
`(a,b,c)=(39529825,55889280,109432706)` and the second `W` quadratic is exactly
`a z^2-c z+a`; `b` drops out. This is not an accident of those numbers: under
the literal fallback the corresponding data are

```
(a,b,c)=(272425,393120,755774),
second W factor = 272425z^2-755774z+272425.
```

The identity therefore survives the Hodge fork even though the headline
coefficients in C3/C6 do not.

### C8 — **REFUTED** as a numerical conjunction; grading structure confirmed

At `T=20,t0=3`, with `U(t,x)=(t,x+2)`, exact residuals under both Hodge forks
are

```
nnz(U^T K_c U-K_c)=0,   nnz(WU-UW)=0.
```

The `U=+1` and `U=-1` off-sector blocks are identically zero. Under
`B_fingerprint` their exact characteristic polynomials are respectively

```
(39529825z^2-109432706z+39529825)^2,
(22569375z^2-233631106z+22569375)^2,
```

so the stated assignment is internally reproduced. Under the literal fallback
they are instead

```
U=+1: (272425z^2-755774z+272425)^2,
U=-1: (164375z^2-1629374z+164375)^2.
```

The normalization qualifier does not cure the mismatch, because these
primitive coefficient ratios differ.

## Required adversarial probes

### P1 — transpose convention: **not robust if only `K` is changed**

There are two inequivalent readings, and they must not be conflated.

1. If the pairing convention is consistently transposed in both `K_c` and
   `L_2`, then `K'_c` and `W'` each differ entrywise from the originals (32
   entries for `K'_c-K_c` and 32 for `W'-W` at each deep core), but the exact
   monodromy characteristic polynomial is unchanged at `t0=3,4,5`.
2. If P1 is read literally as written—replace only `K_c` by the displayed
   `K'_c` while retaining the construction's `L_2`—the spectrum changes. At
   `t0=3` under `B_fingerprint`, one of the new exact factors is

   ```
   84948074055605768125 z^2
   -556793556943043965322 z
   +123585838980091336525,
   ```

   rather than either claimed monodromy quadratic; the full matrix difference
   has 64 nonzeros.

Therefore convention robustness holds only for a consistently transposed
pairing, not for the K-only alternative explicitly stated in P1.

### P2 — second commutant found, but it is not a Gram isometry

Let `S` be the unsigned one-site spatial shift on the core,

```
S e_(t,x) = e_(t,x+1).
```

At each `T=20` deep core `t0=3,4,5`, exactly

```
[W,S]=0,   S^2=U,   S^4=I.
```

So `S` is a genuine second commuting symmetry of `W`. It is not a symmetry of
the Gram: at `t0=3`, `S^T K_c S-K_c` has 64 nonzeros, with witness

```
(S^T K_c S-K_c)[0,0]
=4133693783848694625599413680814310785948633910277157575045033048666567162875000000
 /4288937012506223903627417645638392558627241831049416724940345615120154600004344003689.
```

The exact `S`-momentum blocks under `B_fingerprint` have characteristic
polynomials

| momentum `p` | exact primitive polynomial |
|---:|---|
| 0 | `39529825z^2-109432706z+39529825` |
| 1 | `22569375z^2-233631106z+22569375` |
| 2 | `39529825z^2-109432706z+39529825` |
| 3 | `22569375z^2-233631106z+22569375` |

Thus `S` resolves the `U` sectors into four momenta and organizes the doubled
factors. It does not by group theory alone force the extra equality between
the `p=0` and `p=2` blocks; that is an additional exact isospectrality.

I exhaustively tested 2,048 real signed-monomial candidates consisting of an
optional layer swap, every spatial dihedral action, and all relative sign
choices. Up to overall sign, the only `W` commuters were `I,S,U,S^3`; only
`I,U` were also `K_c`-isometries. In particular, no signed spatial reflection
and no grade-composed one-site shift supplied a second pairing-preserving
symmetry. An unsigned reflection already has a 16-entry commutator; for
`x -> -x`, one witness is `[W,R]_(0,5)=-16334218/7905965`.

### P3 — **CONFIRMED conditionally / structural parity independence survives**

At the third deep core `T=20,t0=5`, `charpoly(W)` is exactly identical to the
`t0=3,4` polynomial under each Hodge fork. Under `B_fingerprint` it is the
claimed product; under the literal fallback it is the corrected product stated
under C6.

### P4 — **CONFIRMED exactly for the displayed quadratics**

For the two claimed monodromy quadratics, the exact discriminants are

```
Delta_1 = 52545986939220736
        = 2^8*13*31*37*71*313^2*1979 > 0,
Delta_2 = 5725088884359936
        = 2^8*3^7*7*13*31*37*313^2 > 0.
```

Moreover `233631106>2*22569375` and
`109432706>2*39529825`. Hence each quadratic has two real positive roots;
its constant/leading ratio is 1, so the roots are reciprocal. The two trace
ratios are distinct because

```
233631106*39529825 - 109432706*22569375
= 6765568955757700 != 0.
```

Therefore all four roots are distinct, real, positive, and grouped into two
reciprocal pairs. The formulas
`2 cosh(theta_1)=233631106/22569375` and
`2 cosh(theta_2)=109432706/39529825` follow exactly. The same sign argument
also holds for the fallback quadratics; their discriminants are
`2546783069376` and `274332816576`.

## Bottom line

The transfer package is internally exact under `B_fingerprint`, and its
structural rigidity, mirror, monodromy, grading, third-core, and root-sign
mechanisms are real. It is not verified for the construction stated in the
dispatch: the listed coefficients require an unprovided exact diagonal change
`-50/169 E_11`, while the permitted block-105/fallback rebuilds give different
exact polynomials and do not reproduce the available block-188 site control.
Accordingly C3, the numerical part of C6, and the numerical part of C8 are
refuted/unverifiable as claims about the stated construction. P1 also needs the
explicit correction that `L_k` must be transposed together with `K_c` for
convention robustness.
