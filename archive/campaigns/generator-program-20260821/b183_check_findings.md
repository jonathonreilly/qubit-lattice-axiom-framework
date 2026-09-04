# Block 183 adversarial check — derived reflection and seam-dual frame

All decision-bearing calculations use exact SymPy expressions. No floating-point
value is used. The construction imports the named Block-128 public module from
`mirror/scripts/` and calls only the APIs permitted in the prompt. The two note
reads were restricted to the specified Section 9 and reflection-construction
line windows. No supervisor scratch artifact was read or imported.

## S1 — algebra of `R`, reflected grading, and flat controls

**Verdict: REFUTED.** Two conjuncts are false, although all three flat/nilpotency
controls survive.

- Exact multiplication gives `R^2 = -I_32`, not `I_32`:
  `nnz(R^2 + I_32)=0` and `nnz(R^2-I_32)=32`. Consequently
  `R^{-1}=-R=R^T`; it is still an exact real orthogonal/unitary matrix.
- The reflected differential `d_ref=R d00 R^{-1}` is nilpotent:
  `nnz(d_ref^2)=0`.
- It is **not** grade-raising for the stated fixed
  `N_deg=diag(t mod 2+x mod 2)`. Whereas `d00` has 32 nonzero entries, all
  with grade jump `+1`, `d_ref` has the exact jump census
  `{-1:16,+1:16}`. Equivalently,
  `nnz([N_deg,d_ref]-d_ref)=16`. The precise repair is to transport the
  grading too: for `N_ref=R N_deg R^{-1}` one instead has
  `nnz([N_ref,d_ref]-d_ref)=0`.
- With real positive symbolic `m`, the flat control is exact:
  `nnz(R Q(I,d00) R^{-1}-Q(I,d00))=0`.
- For `R_x=P_edge xpar`, both asserted comparisons are exact:
  `nnz(R_x Q(I,d00) R_x^{-1}-Q(I,d00)^dagger)=0` and
  `nnz(R_x Q(I,d00) R_x^{-1}-Q(I,d00)^T)=0`; also
  `nnz(Q(I,d00)^dagger-Q(I,d00)^T)=0`.

## S2 — naive reflections and diagonal-intertwiner obstruction

**Verdict: CONFIRMED.** I fixed the spot-check convention explicitly. Let
`P_a` be the undressed site permutation `t -> a-t (mod 8)`. Its induced cell
field is `g_a(t,x)=g((a-1-t) mod 4,x)`, and its reflected differential is
`d_a=P_a d00 P_a^{-1}`.

- For both `a=7` (the edge reflection in the prompt) and `a=0` (the adjacent
  site-axis reflection), the same-Hodge residuals are
  `nnz(P_a H[g] P_a^{-1}-H[g_a])=144` and
  `nnz(P_a Q(H[g],d00)P_a^{-1}-Q(H[g_a],d_a))=320`.
  Thus two undressed curved-action checks fail at the advertised order of
  magnitude. As a supplementary diagnostic, comparison to the dual target
  gives 56 Hodge and 168 action nonzeros for either axis; undressing is not
  rescued by simply naming the target dual.
- An invertible diagonal similarity cannot change matrix support. For each of
  `k=0` and `k=2`, the support symmetric difference between `d_ref` and
  `Ut^k d00 Ut^{-k}` is exactly 32 entries; it is also exactly 32 against the
  dagger of that candidate. Hence no invertible diagonal intertwiner exists
  for either selected `k`. (The exact direct-candidate support mismatch is 32
  for every `k=0,...,7`; the dagger mismatch is 32 for even `k`, 64 for odd
  `k`.)

## S3 — cellwise seam-dual frame

**Verdict: CONFIRMED.** All 32 cells satisfy, entrywise,

`R cover_embedding(t,x) = cover_embedding((6-t) mod 8,x) (s_t M)`

with the assignment as written in the claim: `s_t=(-1)^t`, so even `t` has
`+1` and odd `t` has `-1`. There are zero failed cells. The same displayed
`M` works at every `t,x`, and exact multiplication gives
`nnz(M^2+I_4)=0` and `nnz(M^2-I_4)=4`; hence `M^2=-I_4`. This is consistent
with the corrected S1 result `R^2=-I_32`.

## S4 — symbolic dual Hodge block

**Verdict: CONFIRMED.** For real symbolic nonzero `q,v` (as an identity of
rational functions, away from their poles), direct API evaluation and exact
simplification give

```text
M shear_hodge(q,v) M^T =
[[-v/(q^2-1), 0,   0, -qv/(q^2-1)],
 [0,            1/v, 0,  0],
 [0,            0,   v,  0],
 [-qv/(q^2-1),  0,   0, -v/(q^2-1)]].
```

The residual against the claimed matrix has zero nonzeros. Its exact
symbolic difference counts against, in order,
`H(q,v)`, `H(-q,v)`, `H(q,v)^{-1}`, `H(-q,v)^{-1}`,
`H(q,1/v)`, and `H(-q,1/v)` are `8,8,7,7,8,8`. For example, the `(0,0)`
difference from either first candidate is
`-q^2 v/((q-1)(q+1))`, already disproving symbolic identity.

## S5 — landed-field Hodge reflection

**Verdict: CONFIRMED.** The independently parameterized `H[g]` first agrees
with the public zero-argument cover builder exactly:
`nnz(H[g]-curved_hodge_cover())=0`. At the landed public
`block105.overlap_field()`, with `theta_cell g(t,x)=g((2-t) mod 4,x)`,

`nnz(R H[g] R^{-1} - H_dual[theta_cell g]) = 0`.

## S6 — failure of the four-origin equal-weight section point

**Verdict: CONFIRMED.** Let
`A={I,Ux,Ut,Ut Ux}` and use real positive symbolic `m`. With `H_s` and its
dual built using this same ordered set, the exact counts are

- `nnz(R H_s[g] R^{-1}-H_{s,dual}[theta g])=96`;
- `nnz(R Q(H_s[g],d00)R^{-1}-Q(H_{s,dual}[theta g],d_ref))=256`.

Thus the claimed 256-entry action failure is exact. The origin mechanism is
also explicit: conjugation sends `A`, modulo irrelevant scalar signs, to
`A_ref={I,Ux,Ut^{-1},Ut^{-1}Ux}`. Using that reflected set on the dual side
makes both the Hodge and action residuals exactly zero; it is specifically the
same-set demand that fails.

For the requested related undressed diagnostic, I used
`P_edge:t->7-t`, the original `H_s[g]`, the appropriately reflected field
`theta g`, **plain** (not dual) Hodge blocks, and `A_ref` on the target. This
gives exactly
`nnz(P_edge H_s[g]P_edge^{-1}-H_{A_ref}[theta g])=160`.
At action level, with `d_P=P_edge d00 P_edge^{-1}`, the corresponding count is
336. (Using the same set `A` rather than `A_ref` also gives 160 at Hodge
level.)

## S7 — full-orbit symmetrization

**Verdict: CONFIRMED-WITH-CORRECTION.** All algebraic statements hold, but
part (c) is a formal corollary rather than an independent theorem.

- For `A_16={Ut^k Ux^xo: k=0,...,7; xo=0,1}`, exact evaluation gives
  `nnz(R H_sym[g]R^{-1}-H_sym,dual[theta g])=0` with the same 16 shifts on
  the dual side.
- All 32 leading principal minors of `H_sym[g]` are exact positive rationals,
  so Sylvester's criterion proves positive definiteness without numerical
  eigenvalues. The first is `1993177451/1877439200`. The determinant (the
  32nd minor) has the compact exact positive factorization

  ```text
  (23*173*1208033*3451009*38767651199*4101468900869
   *45634836475924259*57826582318649980836067)^4
  -----------------------------------------------------------------
  2^248 3^32 5^64 7^32 13^24 17^32 29^16 37^24 41^16 .
  ```

  Direct exact sign inspection found positive numerator and denominator for
  every one of the 32 minors (`32/32`).
- Fixing the field-move convention as
  `g_{+2}(t,x)=g((t+2) mod 4,x)`, the covariance residuals are
  `nnz((Ut^2)^T d00 Ut^2-d00)=0`,
  `nnz((Ut^2)^T H_sym[g]Ut^2-H_sym[g_{+2}])=0`, and
  `nnz((Ut^2)^T Q(H_sym[g],d00)Ut^2-Q(H_sym[g_{+2}],d00))=0`.
- The S7(c) residual is exactly zero. Logically, however, it follows from
  S7(a), `d_ref=R d00 R^{-1}`, the unitarity `R^{-1}=R^dagger`, and ordinary
  distribution of conjugation over products and sums. In particular,
  `R d00^dagger R^{-1}=d_ref^dagger`. Therefore (c) adds no independent
  constraint once (a) and the definitions are established; it should be
  labeled an exact action-level corollary of (a).

## S8 — attack on the full-orbit selection reading

**Verdict: REFUTED.** Reflection closure does not uniquely select the
16-shift equal-weight point. It admits it, but also admits strictly smaller
sets, including the first candidate in the prompt.

Exact conjugation gives

```text
R Ut R^{-1} = -Ut^{-1},       R Ux R^{-1} = Ux,
R (Ut^k Ux^xo) R^{-1} = (-1)^k Ut^{-k} Ux^xo.
```

The first and third identities have respectively 0 and 0 residual nonzeros
(comparison of the first identity to `+Ut^{-1}` has 32). For Hodge averages,
the scalar sign is immaterial because `(-S)^T H(-S)=S^T H S`. Thus a plain
shift set is closed at the congruence level precisely when its temporal
weights obey `w_{k,xo}=w_{-k,xo}`. For odd `k`, literal matrix-set closure
uses the dressed partner `-Ut^{-k}Ux^xo`; replacing it by the plain positive
shift produces the identical average.

The exact landed-field tests were:

| shifts averaged | terms | H closure nnz | Q closure nnz | positive leading minors | `t+2` Q covariance nnz | `x+2` Q covariance nnz |
|---|---:|---:|---:|---:|---:|---:|
| `{I}` | 1 | 0 | 0 | 32/32 | 0 | 0 |
| `{I,Ux}` | 2 | 0 | 0 | 32/32 | 0 | 0 |
| `{I,Ux,Ut^4,Ut^4Ux}` | 4 | 0 | 0 | 32/32 | 0 | 0 |
| `{0,+-1}` temporal exponents crossed with `{I,Ux}` | 6 | 0 | 0 | 32/32 | 0 | 0 |
| `{0,+-2}` temporal exponents crossed with `{I,Ux}` | 6 | 0 | 0 | 32/32 | 0 | 0 |
| `{0,+-3}` temporal exponents crossed with `{I,Ux}` | 6 | 0 | 0 | 32/32 | 0 | 0 |

Here H closure is the S5-style same-set dual identity, Q closure uses
`d_ref`, and covariance uses the same exact field-move convention as S7.
The checker additionally verified `d00` invariance under both `Ut^2` and
`Ux^2` (zero nonzeros).

The complete temporal orbit decomposition modulo the harmless sign is
`{0}`, `{4}`, `{1,7}`, `{2,6}`, `{3,5}`. If identity and the x-origin pair
are required, every union containing `{0}`, crossed with `{I,Ux}`, works:
there are `2^4=16` such equal-weight sets, 15 of them smaller than the full
orbit. More generally, any normalized positive weights constant on these
reflection orbits close and stay positive definite. If no x-origin-pair
condition is imposed, `{I}` is the identity-containing cardinality-one
minimum (and each fixed singleton among `I,Ux,Ut^4,Ut^4Ux` also closes).
If the x pair is imposed, `{I,Ux}` is the cardinality-two minimum.

Therefore S6 only rules out its non-closed four-set; S7 supplies one working
closed set. Their conjunction supports **“reflection closure admits the
full-orbit point,” not “selects it uniquely.”**

## Overall verdict

**REFUTED.** The seam-dual cell identity, symbolic dual block, landed-field
closure, four-origin failure, and full-orbit construction are sound. The
compound supervisor package is nevertheless false as stated: S1 has the wrong
square and wrong fixed-grading claim, S7(c) is not independent of S7(a), and
S8 disproves the advertised uniqueness/selection reading by exact smaller
positive-definite covariant examples.

## Ten-line summary

1. S1 REFUTED: `R^2=-I_32`, not `+I_32`, and `d_ref` has 16 raising plus 16 lowering entries for fixed `N_deg`.
2. S1 controls CONFIRMED: `d_ref^2=0`; the `R` flat residual and both `P_edge*xpar` dagger/transpose residuals are zero.
3. S2 CONFIRMED: two explicit undressed curved-action residuals are 320, and `k=0,2` each have 32-entry support obstructions to both targets.
4. S3 CONFIRMED: all 32 cells use `s_t=(-1)^t` and the same `M`, with `M^2=-I_4`.
5. S4 CONFIRMED: the displayed symbolic dual block is exact and differs symbolically from all six named alternatives.
6. S5 CONFIRMED: the landed-field seam-dual Hodge residual has zero nonzeros.
7. S6 CONFIRMED: the same-set Hodge/action failures have 96/256 nonzeros; the specified undressed reflected-set Hodge diagnostic has 160.
8. S7 CONFIRMED-WITH-CORRECTION: closure, 32/32 positive exact minors, and two-step covariance hold, while (c) follows formally from (a).
9. S8 REFUTED: `{I}`, `{I,Ux}`, the four-shift `k=4` set, and all tested `+-k` sets close, stay PD, and remain two-step covariant.
10. Honest restatement: reflection closure admits the 16-shift point but does not select it uniquely; the x-paired minimum found is `{I,Ux}`.
