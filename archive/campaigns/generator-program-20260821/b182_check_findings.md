# Block 182 adversarial check — dual-patch pullback on the curved section frame

Method: independent exact-SymPy reconstruction from only the three bounded public sources named in the task. All equality, rank, nilpotence, commutator, nonzero-entry, and diagonal-gauge decisions are exact; no floating-point decision is used.

## C1 — corpus claim: CONFIRMED-WITH-CORRECTION

The Block 106 note itself records `reachability_to_target: closes`, quotes the Block 105 target (“uniformly bounded finite-range, transition-compatible nilpotent differential … invariant … same graded Ward action and signed staggered shifts”), and then states that all four terminal obligations are executed exactly. Equations (18), (24), (26), and (28)–(36) provide the descent/intertwining, Hodge pullback, same-action pullback, and signed-shift/shear-flip package. Its N4 table is explicit that Block 105 Section 12 item 1 is executed while items 2–4 remain open. Thus a blanket later statement that this blocker must “stay open” is wrong at the Block 106 corpus scope.

Correction: “Ward” here means the same graded Ward **operator action on** `range(A)`. The note expressly disclaims a Ward-contraction theorem, and it leaves the actual ADM/history transporter, reflection positivity/OS, joint gravity, and gravity quotient open. The closure must not be widened beyond that exact scope.

## C2 — isometry package: CONFIRMED

With the shift convention in the prompt, the independently built transported matrices `S_o d00 S_o^T` equal the four public-API matrices `chart_differential_cover(o)` for `o=(0,0),(0,1),(1,0),(1,1)` exactly. On dimensions `A: C^32 -> C^128` and `D_patch,H_patch,Q_patch: C^128 -> C^128`, exact SymPy multiplication gives

- `A^T A = I_32`;
- `D_patch A = A d00`;
- `A^T H_patch A = (1/4) sum_o S_o^T H S_o = Hs`;
- `A^T Q_patch A = m Hs + i(Hs d00 + d00^H Hs) = Q_s`.

The last identity holds coefficientwise for a positive symbolic `m`; no mass value or numerical normalization was substituted.

## C3 — grading package: CONFIRMED

For `N=diag((t mod 2)+(x mod 2))` on the `8 x 4` cover,

- `[N,d00]-d00=0`;
- after antiperiodic folding, `[N_q,d_q]-d_q=0`;
- `N_q` is entry-for-entry identical to Block 106 `core_objects(m)["N_glob"]`;
- the canonical four-block grade has block defect ranks `(0,16,16,16)`, hence total rank exactly `48`;
- the co-transported grade `diag(S_o N S_o^T)` has total defect rank `0` and obeys `diag(S_o N S_o^T) A = A N`.

Thus the rank-48 statement is correct, and its origin is visible blockwise: only the unshifted chart uses the fixed canonical census without a mismatch.

## C4 — signed lifts and flat symmetry: CONFIRMED

For `Ut~=diag((-1)^x) Ut` and `Ux~=Ux`, exact multiplication gives

- `Ut~ Ux~ = -Ux~ Ut~`;
- `(Ut~)^2=Ut^2` and `(Ux~)^2=Ux^2`;
- `[Ut^2,Q(I,d00)]=[Ux^2,Q(I,d00)]=0`.

The one-step plain shifts are not symmetries: the plain-time commutator has rank exactly `24`, as claimed, while the plain-space commutator has rank exactly `32`. For completeness, the signed-time and signed-space one-step commutators with this fixed-chart `Q(I,d00)` both have rank `32`; C4 does not claim otherwise.

## C5 — ADM shear flip on the curved cover: CONFIRMED

Extend `block105.overlap_field()` periodically from four to eight time slices and reconstruct
`H[g]=(1/4) sum_(t,x) E_(t,x) H_site(q_(t,x),v_(t,x)) E_(t,x)^T` independently. Then, exactly,

- `H[g]=curved_hodge_cover()`;
- `Ux H[g] Ux^T=H[T_x g]`;
- `Ut H[g] Ut^T=H[T_t g]`;
- `Ut~ H[g] Ut~^T=H[T_t Fg]`, `F(q,v)=(-q,v)`.

The signed-versus-unflipped residual and the plain-versus-flipped residual both have rank exactly `32`, the full cover dimension.

Why this does not conflict with Block 106’s rank `28`: on its `4 x 4` anchor-direct-sum carrier, the field has precisely two flat anchors, `(0,0)` and `(2,2)`. Fourteen nonflat independent anchor blocks each contribute rank two, giving `14*2=28`. The eight-time cover repeats those flats at `(0,0),(2,2),(4,0),(6,2)`, but `H[g]` is the overlap pullback on only 32 physical cover coordinates, not a direct sum of 32 independent four-component anchors. Every physical coordinate is still reached by neighboring nonflat patches; the exact residual has nullity zero and rank `32`.

## C6 — quotient descent of the geometry package: CONFIRMED

The quotient of the plain cover time shift is the expected orthogonal `16 x 16` antiperiodic shift: all four `t=3 -> t=0` wrap entries are exactly `-1`. With this `Utq`, the periodic `Uxq`, and `Hq=antiperiodic_quotient(H[g])`, exact folding gives

- `Uxq Hq Uxq^T = quotient(H[T_x g])`;
- `Utq Hq Utq^T = quotient(H[T_t g])` with the **plain** translated field;
- `(sgn_x_q Utq) Hq (sgn_x_q Utq)^T = quotient(H[T_t Fg])` with the flipped field.

Thus antiperiodic seam signs do not spuriously force a shear flip for the plain quotient translation; the flip enters only with the staggered sign field.

## C7 — two-step curved covariance: CONFIRMED

Independently rebuilding `Hs[f]=(1/4) sum_o S_o^T H[f] S_o` gives both Hodge identities
`Ut^2 Hs[g] (Ut^2)^T=Hs[T_t^2 g]` and `Ux^2 Hs[g] (Ux^2)^T=Hs[T_x^2 g]`. Since the fixed `d00` commutes with both two-step shifts, exact coefficientwise calculation for symbolic positive `m` yields

- `Ut^2 Q_s[g] (Ut^2)^T=Q_s[T_t^2 g]`;
- `Ux^2 Q_s[g] (Ux^2)^T=Q_s[T_x^2 g]`.

## C8 — signed conjugate classification: CONFIRMED

For `d'=Ut~ d00 Ut~^T`, exact SymPy classification gives

- `(d')^2=0`;
- `rank(d')=16`;
- `d'=sgn_x d10 sgn_x` exactly;
- `d' != d10`;
- `rank([N,d']-d')=16`, so `d'` is not `N`-graded.

The last rank supplies the exact non-grading number omitted from the supervisor statement.

## C9 — Ramond versus Neveu–Schwarz complexes: CONFIRMED

Block 106’s periodic fine differential has `rank(d_fine)=6`, `d_fine^2=0`, grade dimensions `(4,8,4)`, adjacent grade-map ranks `(3,3)`, and cohomology dimensions `(1,2,1)`. Hence the total harmonic dimension is `1+2+1=4`, exactly the torus Betti pattern.

The antiperiodic quotient has `rank(d_q)=8`, `dim ker(d_q)=8`, and `d_q^2=0`; therefore `im(d_q)=ker(d_q)` and its cohomology is zero. Its adjacent grade-map ranks are `(4,4)` and its grade cohomology dimensions are `(0,0,0)`. It uses the same diagonal `N` as Block 106.

The exact matrix difference `d_q-d_fine` has `32` nonzero entries. Exactly four are on the temporal seam, at `(row,column)=(12,0),(13,1),(14,2),(15,3)`, i.e. `t=3 <- t=0` at the four spatial sites. Negating only the `t=0 <-> t=3` entries of `d_fine` does not produce `d_q`.

No diagonal sign field can relate them. Two independent exact obstructions are decisive: (i) similarity by any invertible matrix would preserve rank, but `6 != 8`; and (ii) diagonal conjugation preserves support, while the supports already differ—for example `(d_fine)_(1,2)=-i/2` but `(d_q)_(1,2)=0`. Thus these are genuinely different periodic/Ramond and antiperiodic/Neveu–Schwarz complexes, not a seam-sign gauge choice. Their different cohomology is the corresponding nontrivial `Z2` spin-structure obstruction.

## Overall verdict: CONFIRMED-WITH-CORRECTION

All exact algebraic and rank claims C2–C9 are confirmed. C1 is confirmed at the note’s explicitly bounded corpus scope, with the necessary correction that “Ward closure” means same graded Ward-operator action on the invariant physical range, not a Ward-contraction, ADM/history, OS, or gravity theorem. No supervisor claim is refuted numerically; the main adversarial strengthening is that C9’s non-equivalence follows already from unequal rank and unequal support.

## Ten-line summary

1. C1: Block 106 explicitly closes the Block 105 transition-compatible descent target, but not Ward contraction, ADM/history, OS, or gravity.
2. C2: `A` is an exact isometry/intertwiner and pulls both `H_patch` and symbolic-`m` `Q_patch` back to `Hs` and `Q_s`.
3. C3: cover and quotient gradings close; canonical patch defect rank is `48=(0+16+16+16)`, transported defect rank is `0`.
4. C4: signed lifts anticommute and square to plain two-steps; plain one-step commutator ranks are time `24`, space `32`.
5. C5: all curved-cover covariance identities hold; both wrong-flip residuals have full rank `32` despite four repeated flat anchors.
6. C6: antiperiodic quotient covariance is plain for `Utq` and shear-flipped only for `sgn_x_q Utq`.
7. C7: both two-step curved `Q_s` covariance identities hold exactly for symbolic positive `m`.
8. C8: the signed conjugate is nilpotent rank `16`, equals `sgn_x d10 sgn_x`, differs from `d10`, and has grade-defect rank `16`.
9. C9: periodic rank/cohomology is `6/(1,2,1)` while antiperiodic rank/cohomology is `8/(0,0,0)`; no diagonal sign gauge exists.
10. Overall: every numerical identity survives; only C1 requires the explicit corpus-scope qualification.
