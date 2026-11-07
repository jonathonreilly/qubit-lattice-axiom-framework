# PRINT-INVERSE: prior-work digest (FINISH 423; BP07)

Provenance: Codex, checkout `13edf59fa2ea5478e3c78779b47d9c6bf64c359d`.
Research reading and collation only. No new proof, independent proof check, audit, or status grant.
Paths below are relative to `ym4d-hard-route-20261030/`, unless absolute.
Credit Tadeusz Balaban for the printed construction, and Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text, for the outline and complete account.

## 0. Recovery checkpoint and source identities

`library/prior/pi-prior.md` was absent. The registry at `library/open-registry.md:428`
assigns PRINT-INVERSE to **print-inverse**, FINISH 424. This digest is FINISH 423;
it does not start that proof lane or the separately owned CO/OL, CM, or B99-W work.
`library/t0-tree.md:230` explicitly keeps the full BP07 statement OPEN despite P18.
The referenced `docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this checkout.
Only this digest is edited. No editable prompt files change.

Account files are in `/Users/jonreilly/ym4d-lead/sa/`. Their bytes match the source
identities recorded for `31a47c543775` in `library/lrb.md:16–21`:

| Source | SHA-256 |
|---|---|
| `YM4_sketch_500.tex` (SA) | `d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f` |
| `theorem_0_complete_account_raw_I.tex` (I) | `4cb5cb5e0af8dbddbee207926621300350e018c6cf1d6567a753167ce10e6e93` |
| `theorem_0_complete_account_raw_II.tex` (II) | `6a1f74b05f74ba44a2186c11fb08e139178d86b15c1494a95c434212944b2b8f` |
| `theorem_0_complete_account_raw_III.tex` (III) | `7e36523b85fb4f85aefdd45ab175420459f24e34fe56a4e83e53a6829c7a352d` |

The `sa/` directory is a source snapshot, not a Git checkout. The hash match, rather
than an invented local HEAD, identifies its revision. No history search was used.
Navigation began with `sa-index/README.md`, chunk-10's neighbouring propagator rows,
chunk-11's neighbouring field-Gram rows, and `obligations.md:605–640`.
The actual bounded SA passages read are cited in §4. Index labels alone establish nothing.
Search logs and intermediate inventories are in `/tmp/print-inverse-digest/`.

Current decision: prior work partly covers the target. Do not rebuild the real B14
Gram argument or uniform-layer P18 merely under a new name. The unresolved target
is their full layered complex, locally defined inverse-walk statement with its actual
scale factors, norms, and consumer-compatible constants. No counterexample is claimed.

## 1. Target and printed sources

### 1.1 The account's exact target

I:13144–13162, `4.5:rem-covariance-inverse-walks`, says:

> Let $U$ satisfy conditions (S1) and (S2) of Definition~\ref{4.5:def-admissible-pairs}.
> Here $U=e^{i\eta\mathfrak{a}}U_r$ is in general $G^c$-valued.

It sets $\mathsf q_0=(QG_0Q^*)^{-1}$. Here $G_0$ is the chapter's Green operator at
vanishing independent current, identified there with the earlier §3 operator $G$.
$Q^*$ is the analytic continuation of the real adjoint, hence the **bilinear transpose**.
The two requested properties are (3.132) and local generalized walks of type
(3.98)–(3.99), constructed as in Theorem 3.9, with hull dependence and (3.108)-type bounds.
I:13164–13173 explicitly says both are printed without proof. Its quotation is:

> The operators $(QGQ^*)^{-1}$, or $(QG_1Q^*)^{-1}$, can be analyzed in the same way as the
> operator $(Q'G'^2Q'^*)^{-1}$. We will not repeat these considerations here, let us write
> only bounds

The admission is exact, not an arbitrary small complex neighbourhood. I:12935–12973
requires real local gauges on cubes of side up to $12\mathfrak M$ in current-level units:
$\ell_j|A|<a_0$, $\ell_j^2|\nabla A|<a_0$, and $N_{U_r}(\mathfrak a)<a_1$.
The radii depend on $(d,L)$ only. S3 is irrelevant to $q_0$: no current-background
relation, (3.36), or (3.38) is assumed. I:13583–13595 defines
$G_0=(\Delta+D_URD_U^*+Q^*\ell^{-2}Q)^{-1}$.

### 1.2 OCR transcription and proof structure

The task later explicitly names `/Users/jonreilly/ym4d-lead/papers/{cmp99b,cmp96,cmp99a,cmp102}.txt`.
That specific source list was treated as a narrow exception to the preceding directory rule;
only the named `cmp99b.txt`, `cmp96.txt`, and `cmp102.txt` were read. No surrounding
papers directory was searched. `cmp99a.txt` was not needed. Bookkeeping hashes:

| OCR source | SHA-256 |
|---|---|
| `cmp99b.txt` | `0aed21d3bdcc4e114bec312577d1082a763f8489b58a158b0f60c3e8f045be4a` |
| `cmp96.txt` | `bf1292180c351670eae5075b1c4d6f5d0618a94807dbde34901049a61d75447e` |
| `cmp102.txt` | `78b973edee2f485e6c3c1eb49e9077bc244f5e13d720d432f25d949cd054203f` |

**Transcription limit.** These OCR files do not preserve the requested inequalities in full.
In particular, (3.99), (3.108) and (3.132) have almost empty mathematical lines.
The literal extracts below are exact **OCR text**, not claimed exact typesetting of the
printed paper. A mathematically exact transcription of those displays cannot be certified
from these bytes. No exponent, scale weight or rate fraction is filled in from memory.
The prior visual reading of (3.132) in `b99.md:119–140` is quoted separately below.
This is an unresolved source-verification issue for the proof lane, not a new mathematical gap.

#### Theorem 3.9 and (3.98)–(3.99), CMP99b pp.413, OCR 1340–1360

```text
1340: Theorem 3.9. For M sufficiently large, and a configuration U satisfying (3.35), the
1341: operator Q'Gf2Q'* has an inverse which can be represented as
1342: (Q'G'ϊQ'*)-1
1343: = ΣR'0(X0)R'aι(Xι) K
1344: n(Xn) (3.98)
1345: the sum is over walks ω = ((0,Xo), (al,Xi\...,{(xn,Xn)) satisfying Xi
1346: i=\,...,n. A term in this expansion corresponding to a walk ω depends on U
1347: restructed to X^uXlu... u l
1348: 5
1349: n
1350: , and has the following bound:
1351: R'jxn))(y,y')\ ύ
1352: y'eΛr
1353: . (3.99)
1354: The distance d(ω,y,y') is defined by (3.93), but the infimum is taken over j ^ G
1355: Let us remark that generally the operators R'
1356: a(X) act between different scales,
1357: for example K(h'Πί)G'Πιh'ΠιQ'* transforms functions defined on S 3 into
1358: functions defined on ^-lattice, hence not all combinations of indices αf are
1359: admissible. We have not included this fact into the description of the expansion
1360: (3.98) because it does not affect bounds.
```

Readable statement structure: for sufficiently large $M$ and real $U$ satisfying (3.35),
$Q'G'^2Q'^*$ has an inverse represented by products
$R'_0(X_0)R'_{\alpha_1}(X_1)\cdots R'_{\alpha_n}(X_n)$, summed over the labelled walks.
The readable overlap condition is $X_{i-1}\cap X_i\ne\varnothing$ for $1\le i\le n$.
Its symbols lost at 1345–1346 are supported by the preceding definition
(1311–1335), and the parallel explicit condition at 1530–1532. Each term reads only
$U$ on $X_0^5\cup\cdots\cup X_n^5$. It has the displayed bound (3.99), whose right
side **is not legible here**. The distance is (3.93) with intermediate points in the
successive localization domains (1354; that line too loses its final symbols).
Factors can map between different scales; not all formal index combinations are composable
(1355–1360). This qualification is part of the printed statement, not a new restriction.
At 1327–1337 the first factor is $R'_0(\square)=h_\square C_\square h_\square$,
zero for larger domains; later factors have kernel support in $X\times X$, read $U|_{X^5}$,
and have a (3.89)-type small bound, with possible scale powers.

#### (3.108), CMP99b p.416, OCR 1526–1541

```text
1526: operator G has the expansion
1527: G = ΣRoiXoWatXi) RJXn), (3.107)
1528: the sum is over walks ω = ((0, X
1529: o), (<x1,Xί)9...,(<xn, X
1530: n)) satisfying X{ _ x
1531: n Xt =/= 0 , i =
1532: 1,..., n. A term in this expansion, corresponding to a walk ω, depends on configuration
1533: U restricted to XQUXIKJ... u l
1534: 5
1535: w
1536: , satisfies the inequality
1537: >yy\9 xeΔ(yl (3.108)
1538: and the corresponding inequalities for norms on the left-hand sides of (3.42)-(3.47).
1539: The constant 0(1) depends on d and L only.
1540: From (3.108) it follows that the expansion (3.107) is convergent in all norms
1541: in the inequalities (3.42)-(3.47). This implies Theorem 3.3.
```

This is the **vector $G$** term estimate in Theorem 3.10, used as the type of estimate
requested for $q_0$; it is not itself a displayed $q_0$ estimate. The theorem retains
(3.42)–(3.47)'s corresponding norms and says its $O(1)$ depends on $d,L$ only.
Its hypothesis at 1520 literally reads “(3.95)”; the account explicitly reads this as
(3.35), I:13115–13116 (`rho3`). Do not silently cite the misprinted hypothesis as a
new regularity condition. The inequality itself is lost at OCR 1537.
The nearby (3.94) discussion (1173–1181) explicitly reserves an $O(M^{-1/2})$ factor
for walk summation and two further exponentials; it does not recover the missing
exact (3.108) fractions and scale powers.

#### Sentence before (3.132) and (3.132), CMP99b p.422, OCR 1864–1874

```text
1864: be arbitrarily small. The operators ( β G β * ) "1
1865: , or (QGig*)"1
1866: , can be analyzed in
1867: the same way as the operator (Q'G'2Q'*yι
1868: . We will not repeat these considerations
1869: here, let us write only bounds. We have
1870: ' ^ ϋ ' ' ^ ^ yfeλ
1871: r, (3.132)
1872: and the same for the operator with G
1873: x
1874: instead of G. The above inequality together
```

Here the formula is effectively lost at 1870–1871. The account's faithful prose quote
is reproduced in §1.1. The existing **visual PDF reading**, `b99.md:123–129`, records
its formula as

$$|(QGQ^*)^{-1}(y,y')|\le C s_y^{-2}s_{y'}^{-4}
               e^{-\delta_{\rm p}d(y,y')}.$$

That note identifies the paper's printed rate as $\delta_1$, here called
$\delta_{\rm p}$ to avoid confusing it with the account's later $\delta_0/32$.
This is a transcription in the repository's notation, with $C$ for the printed constant;
it is **not** an independent facsimile verification by this digest. It records physical
row densities. At unit row scale all its scale factors are one, which is why P18
alone cannot settle the general normalization. Do not turn (3.132)'s damaged OCR into
an exact formula for (3.99), and do not claim the latter has no walk-length factors.

### 1.3 CMP99b Theorem 3.9: printed proof structure

This is a reading of Balaban's argument, including its explicitly imported steps;
it does not re-prove or certify them. The narrow source ranges are OCR 1022–1110,
1113–1181,1187–1361. The local analytic comparison is 622–630 and 970–988.

1. **Two early scales and cut-down nests (1022–1080).** Choose the earlier
   $R_0,M_0$ satisfying the flat estimates, then $M=KR_0M_0$. Cover the layers by
   overlapping cubes, with a squared partition of unity. Enlarge a cube to
   $\square^n$, side $(2+2n)ML^j\eta$. Construct its cut-down sequence with early
   gaps $2R_0M_0$ and outer read inside $\square^5$. Its side is $12M$; this is why
   (3.35) must hold on those cubes. Corollary 3.6 supplies the local $G'_\square$,
   $C_\square$, $G_\square$ bounds. Their proof uses real local gauges and earlier
   complex-near-identity comparison, not a global gauge on the walk union.
2. **Parametrix (1081–1089,1187–1195).** Set
   $C_0=\sum h_\square C_\square h_\square$ using the local squared-site-Gram
   inverses. Multiply $Q'G'^2Q'^*C_0$ and split its error into the three sums in
   (3.95): leakage outside the cube, replacement $G'^2-G_\square'^2$, and the
   cutoff commutator. Formula (3.95)'s OCR is damaged but these three terms and
   their roles are independently explicit in the following prose.
3. **Small residual and a summed inverse (1197–1206).** Imports CMP96 (2.83)–(2.85)
   to bound $R$; obtains $C_0(I-R)^{-1}=\sum C_0R^n$ in (3.48)'s weighted sup norm.
   This is not yet the desired local expansion: its letters still include global $G'$.
   OCR (3.96) loses prime/square symbols at 1199; the operator is fixed by 1187–1195
   and Theorem 3.9, not a separate unsquared theorem.
4. **Change the partition near the error cube (1207–1223).** Replace its neighbourhood
   by $\square_0$, chosen from its own layer or the nearest next-layer cube, and
   remove intersecting old cubes. Construct $\mathcal D'$ and its cutoffs. Expand
   each remaining global $G'$ using (3.90) on this changed partition.
5. **First error sum (1224–1234).** Most letters are small
   $K(h')G'_{\square}h'$ factors. The two propagator-end factors and the $C$ factor
   lack smallness. The left leakage indicator and right cutoff are separated by
   $ML^j\eta$; spend part of their exponential decay to attach a small factor to
   each of those three letters. OCR loses the exact coefficient at 1232.
6. **Second error sum with a transition (1238–1248).** There may be no separation.
   If a $K(h')G'h'$ factor occurs, attach each nonsmall letter to a nearest such
   factor, grouping at most three nonsmall operators with one small one. Treat
   each resulting group as one walk factor. Its scale power must still be tracked.
7. **Second error sum without a transition (1249–1285).** Both local propagators
   then use $\square_0$. Since $h'_{\square_0}=1$ on the original cube, commute
   that cutoff left. Its commutator is $O(M^{-1})$. Combine the remaining term
   with the corresponding subtraction to form (3.97), a difference of propagators
   on two local domains. Imported domain-change bounds give an additional
   exponential in the distance to where the domains change, at least $M$ in
   current units. Spend it to obtain a small factor. This imported locality estimate
   is a real proof dependency, not established merely by this rearrangement.
8. **Third error sum (1286–1287).** It is already local; its cutoff commutator gives
   $O(M^{-1})$. No new global propagator is left in these letters.
9. **Label, localize and sum (1288–1361).** Each factor gets a connected union $X$
   of finitely many adjacent cubes and an index $\alpha$ for the finite alternatives.
   The largest listed grouped cube uses $5^d$ old cubes. Kernel support is $X\times X$;
   background read is $X^5$. Concatenate overlapping domains into labelled walks.
   Their term estimate is (3.99); its full displayed expression is lost in this OCR.
   Theorem 3.9 implies Theorem 3.2, rather than replacing the explicit local-letter
   construction by Theorem 3.2's summed bound.

**Vector proof leading to (3.108), OCR 1362–1541.** Its additional steps are:

1. Expand the covariant cutoff product (3.100). The commutators with $D^*D,DD^*$
   are first order with first/second cutoff differences. The local curvature remainder
   also contributes an $O(M^{-1})$ commutator (1362–1378).
2. Write $DRD^*=DD^*-DPD^*$. Estimate its nonlocal cutoff difference using the
   regular exponentially decaying kernel (3.49); this yields $P_1(dh)$ with a small
   cutoff factor, (3.101) (1379–1388).
3. Commute the block average through the cutoff, keeping its endpoint value and
   the explicit $S_j(dh)$ error, (3.102)–(3.103). Combine with the differential
   terms into $K(h)$ and $P_1(dh)$ in (3.104) (1389–1406).
4. Apply this to the local vector parametrix $G_0=\sum h_\square G_\square h_\square$.
   Equation (3.105) splits $I-R$ into local commutators, separated leakage of
   $DPD^*$, a domain-change difference, and its remaining cutoff term. The extra
   cutoff $\zeta_\square$ separates leakage by at least $M$. Prove the (3.85)-type
   residual bound with $O(M^{-1})$ replacing $O(\alpha_1)$, and obtain (3.106),
   $G=G_0\sum R^n$ (1407–1435). This $G_0$ is a **parametrix**, not the account's
   bare Green operator with the same subscript.
5. That summed inverse still contains global $P$. Expand
   $P=G'Q'^*(Q'G'^2Q'^*)^{-1}Q'G'$ by (3.90),(3.98), using the partition
   $\mathcal D'$ modified near each original error cube. When expanding at its
   distinguished large cube, modify again to $\mathcal D''$ and enlarge its boundary
   read (1440–1465). OCR loses some final enlargement superscripts here; do not
   assign a smaller read from its endpoints alone.
6. The leakage terms are small by separation; most domain-change terms are small
   by the same grouping as before. One term lacks smallness. Replace its distinguished
   cutoffs by $\zeta_\square$, paying separation for the differences, then replace
   its local $G'$ and $C$ by the original-cube versions, paying domain-change
   estimates for those differences (1466–1484).
7. Commute the remaining $\zeta_\square$ factors to the right; the commutators are
   small. The surviving nonsmall expression becomes the original local projection
   term and **cancels** its partner in (3.105) (1494–1515). All remaining factors
   are small and local; label their connected domains as before to obtain (3.107),
   hull dependence and (3.108) with all earlier norms (1516–1541).

These are the printed steps behind the type of estimate invoked for $q_0$;
the field-Gram adaptation itself has no printed proof at (3.132).

### 1.4 CMP96: what inverse is actually treated, and how

The requested single-prime expression needs a notation correction. CMP96 OCR
551–552 explicitly starts with **$Q'G'^2Q'^*$**, not $Q'G'Q'^*$.
Proposition 2.3 (711–720) concerns its inverse. The single-$G'$ site expression
appears inside its lower-bound proof at 615–638, not as the inverse theorem.
The field analogue **$(QGQ^*)^{-1}$** is separately proved in Proposition 2.7,
1140–1210. Confusing these would erase exactly the power change at issue here.

**Squared site Gram, pp.235–238; OCR 551–720.**

1. (2.68) bounds the Gram using the scalar Green estimates and CMP96 Lemma 2.1.
   Choose the physical layer Hilbert pairing (2.69); powers may be redistributed
   only by the level-distance bound (560–572).
2. Choose a second cube of size $4M$ around the cutoff cube. Invert the compression
   of the Gram built from the **local** $G'(\square)$, not the compression of the global
   inverse. Glue $C_\square$ by $\sum h_\square C_\square h_\square$ (578–593).
3. Rescale to unit lattice, separating the intermediate $Q''$ (594–606). The Gram
   quadratic form is a squared norm. Apply Bessel's inequality using characteristic
   functions of unit blocks (607–614).
4. Bound the single-$G'$ compressed form below by comparison with the full-lattice
   propagator, using (2.42), the earlier paper's representation, Fourier formula
   (2.75), and its bounds (2.50)–(2.51). This gives an absolute $\gamma_0>0$ at
   $a=1$ and, for large $M$, the local bound (2.77) (615–638). Combine it with
   Bessel and rescaling to obtain (2.78). These earlier Fourier bounds are imported;
   their proof is not printed again here.
5. Upper bound and exponential decay of the local Gram, with the lower bound, give
   inverse decay. Balaban offers either the earlier unit-lattice inverse theorem or
   conjugation by $e^{\langle a,x\rangle}$, whose error is $O(|a|)$, as arguments
   (643–655). The rate depends on $\delta_0,\gamma_0$.
6. Undo scaling (2.80); (2.81) has local inverse-density order $-d-4$ (656–666).
   The OCR splits its exponents but preserves that scaling law.
7. Multiply by the glued inverse to get $I-R$, (2.82). Estimate off-cube leakage
   by separation, replacement of local/global $G'^2$ by domain-change walks,
   and the commutator by $O(M^{-1})$ (667–709). Lemma 2.1 sums the residual.
8. Proposition 2.3 gives (2.86), $C(I-R)^{-1}=\sum_{n\ge0}CR^n$, and bound (2.87)
   (711–720). The OCR loses most of (2.85),(2.87); no exact exponents for those
   displays are asserted here. CMP99b refines this summed expansion by localizing
   its still-global letters, as described above.

**Field Gram, pp.248–249; OCR 1140–1210.**

1. Work in (2.69)'s physical $L^2$ pairing with bonds replacing sites; positivity
   gives a finite inverse. Decay of the Gram comes from (2.136), recorded as
   (2.142) (1140–1148).
2. Form local $C_\square$ and glue them as in (2.143). Rescale the local Gram and
   identify the new $Q''$ by the quadratic form in (2.112) (1149–1163).
3. Use the source integral (2.95) with $J=Q^*B$. This source is invariant under the
   kernel-$Q$ gauge transformations used between (2.95) and (2.129), so the terms
   caused by a non-invariant source drop out. This yields (2.145) (1164–1171).
4. The constrained $G_j$ term vanishes; $Q_jH_j=I$. The remaining form is the
   $C^{(j)}$ form on $B_1$, with axial-tree bonds removed, (2.146) (1172–1177).
5. Bound that covariance below by the inverse of an upper bound on its precision
   (2.120), and use $\|B_1\|^2\ge c\|B\|^2$. Obtain (2.147)'s positive
   $\gamma_0(d,L)$. Together with upper and decay bounds this controls the local
   inverse and its decay rate $\delta_4$ (1177–1197).
6. Repeat (2.82), replacing $Q',G'(\square)^2,G'^2$ by $Q,G_\square,G$.
   Balaban explicitly changes the scale powers **$+4,-4$ to $+2,-2$** in (2.83)
   (1198–1203); this is the printed instruction for the change of Gram order.
7. Proposition 2.7 gives the convergent (2.86)-type expansion and bound (2.149)
   (1204–1210). Its inequality is again damaged, not reconstructed here.

The last transfer instruction is legible verbatim at `cmp96.txt:1198–1203`:

> We form the equality for QGQ*C in exactly the same way as in (2.82) replacing only
> in the definition of Kα D , the operators g', G'(D)2
> , G/2 by β, GD, G. We have the
> same estimates now as before, but with powers of scaling factors changed properly
> (we replace +4 and -4 in (2.83) by +2 and -2), thus we have (2.85) and this
> implies

This is the zero-background/flat multiscale treatment. It is not the S1–S2 complex
background theorem in the task. Its gauge cancellation, local lower bound, weighted
pairing, residual estimates and scaling instructions are portable **with their hypotheses**.
CMP99b's perturbative background comparison must be carried through separately.

### 1.5 The complex extension and the notation change, as printed

CMP99b Theorem 3.4, OCR 622–630, gives an early $a_1>0$, analyticity in the twist,
and the same earlier bounds for the explicitly listed $G'$, site squared-Gram inverse,
$R$, and vector $G$. It does not explicitly list a field-Gram inverse in that theorem.
The proof at 970–988 uses a quantitatively small $V(A)G(U)$ and a Neumann expansion.
Thus an analyticity **method** is printed; the needed field-Gram instance still requires
its own quantitative reduction and local-data verification under S1–S2 alone.
The S1–S2 versus stronger classes are printed at 429–465: (3.35),(3.37) impose value
and first-derivative bounds, whereas (3.36),(3.38) add the extra derivative condition.

The symbol change before (3.132) is explicit, `cmp99b.txt:1828–1839`:
Balaban temporarily calls the earlier vector operator $G_0=(\Delta+DRD^*+Q^*aQ)^{-1}$,
then defines the current-corrected $G$ by (3.130). Lines 1855–1863 extend its earlier
norms and walks, except the Laplacian member, before the unproved inverse sentence.
The account's *bare* $G_0$ is not just that later $G$ with a renamed letter.
No assertion that S1–S2 forces the actual Wilson current to vanish is permitted.

CMP102's OCR 824–841 independently returns to the bare $\Delta_a$ operator,
its linear constrained minimizer $H_0=GQ^*(QGQ^*)^{-1}\ell^{-1}$ (129), its extra
Laplacian bound (130), and projection (131). This supports the account's distinction
between bare and corrected bounds. CMP102 imports the earlier bounds here;
it does not supply the omitted field-Gram local-walk proof at these lines.

## 2. Account consumers: complete direct-symbol inventory

Search: `rg -n 'covariance-inverse-walks|3\.132|q_0|q_\{0\}'` on all three raw files.
The complete raw hits are saved as `/tmp/print-inverse-digest/ca-rg-hits.txt`.
The meaningful operator hits use `\mathsf{q}_0`; bare `q_0` also denotes running-radius
exponents, a root cube, a stabilization index, and a root configuration. These are
excluded by their defining context, not treated as inverse consumers. Even
I:53070,53155,53258 uses `\mathsf{q}_0=0` for a level indicator, not this inverse.
There is no direct `covariance-inverse-walks` or inverse `\mathsf{q}_0` occurrence in II or III.
Those volumes consume the same operator under other names below.

### 2.1 Shared norm and constant contract

All §4.5 rows below concern **complex** S1–S2 backgrounds unless an explicit real
diagonal is stated. Independent $J$ obeys S3 where used; it is not an extra premise
for $q_0$. Norms are not interchangeable with an unweighted matrix norm.
I:13402–13458 defines $T\in\mathcal K_a(C,\delta)$ by

$$\sup_{\Delta(y)}|Tf|\le C\ell_j^a e^{-\delta d(y,y')}\sup|f|,
\qquad \operatorname{supp}f\subset\Delta(y'),\ y\in\Lambda_j.$$

The inverse is used as $\mathcal K_{-2}$. I:12739–12760 fixes
$|f|_{(\alpha)}=\sup_j\sup\ell_j^{-\alpha}|f|$, physical pairings $\eta^d$ on fine
sites and $\ell_j^d$ on layer rows, and bilinear transposes. The scale-weighted norm is $|f|_{(\alpha)}$;
the kernel algebra maps it to order $\alpha+a$, also with
$\rho(y)=e^{\kappa d(y,S)}$, $0\le\kappa\le\delta/2$.
Products spend decay; level absorption and shell summation require floors on
$R_1\mathfrak M$. The constants include $c_1,L^{d+4}$, not an unqualified norm-one rule.
$N_\beta$ controls the scaled potential and its first covariant derivative with the
specified local Hölder seminorm; $\beta\le\beta_0<1$. The $G_0,H_0$ Laplacian members
must be distinguished from the corrected-current operators' explicitly omitted ones.
Walk consumers require individual local analytic terms and absolute walk majorants;
decay of their sum cannot supply the zero-switch locality.
The constant contract is explicit at I:15110–15118,15155–15158: dependence only
on $d,L$, fixed powers of $L$, and geometric floors on $M_1,R_1$; no dependence
on $k,K,X,\{\Omega_j\}$, no product of constants over levels. Each §4.5 consumer
row below reads that shared contract unless it lists additional later parameters.

### 2.2 Every meaningful direct use, grouped only within the same argument

| Account lines (all direct hits included) | What is read: background; bound/norm; locality; constants |
|---|---|
| I:5307–5308 | The continued `4.4:prf-expansion-words` orders inverse-Gram walks before $H$, $H^*J$, the second correction and the $G_1$ inverse. Reads the selected local word families on the admitted settings, including complex settings; equality/cancellation of local letters, not merely a summed bound. The printed bound (3.132) labels both inverse stages. |
| I:5702 (context 5685–5717) | Walk hypothesis (f4) reads the coarse operator's entry bound term by term, and the $N_{\beta^\sharp}$ bounds for the field/lift terms on local complex data. Its constant is $c_{\rm vol}\kappa_\omega$, with the later corollaries' $B^\natural$. Explicitly excludes full differentiated-source and Laplacian claims. This is a hypothesis, not a proof of $q_0$ walks. |
| I:13143–13171 | Target, definition, two claimed properties and their printed-without-proof attribution; no consumer theorem is proved here. |
| I:13323 (context 13317–13340) | `rem-near-bound-frame` says inverse walks and analytic averaging derivatives stand essentially under the **complex** near bound (CMP109 (3.31)–(3.32)); frame construction is a further input. No new inverse estimate or constants are supplied. |
| I:13589; 13624–13627 | Background-propagator definition reads $q_0\in\mathcal K_{-2}$ and its generalized walks at complex $U$. |
| I:13640,13652,13657,13659,13664–13665 | Defines $H_0=G_0Q^*q_0\ell^{-1}$, $P_0=I-G_0Q^*q_0Q$ and proves algebraic constraint identities. Reads invertibility and bilinear symmetry; those identities themselves do not need walk bounds. |
| I:13675;13683 | Same definition ends with $N_\beta(H_0B)\le B_0|B|$, $N_\beta(\widetilde{\mathfrak G}_0f)\le B'_0|f|_{(-3)}$, $P_0^T\in\mathcal K_0$. Then free-current lemma explicitly assumes both inverse properties. These are uniform complex estimates and analyticity, not a real-only assertion. |
| I:13766;13787,13792–13793 | Free-current clauses J3/J8: $q_J\in\mathcal K_{-2}$ and local analytic walks for $q_0$, $q_J$, and the second corrected inverse, with (3.108)/(1.7)-type bounds in J2's listed norms. All side-branch domains are part of the read. Constants obey $C_Ja_\gamma\le1/2$, $C_\Theta a_\gamma B'_0\le1/2$. |
| I:13899–13909 | J3 factors $QG_\pi^JQ^*$ around $QG_0Q^*$, using the order $-2$ bound to make $q_0Q(G_\pi^J-G_0)Q^*$ small in $\mathcal K_0$. Needs uniform constants depending on $d,L$, so $a_\gamma$ can be chosen once. No new exact hull-locality is inferred from this norm estimate. |
| I:13915,13918 | J4 decomposes $H^J-H_0$ using $q_J-q_0$, obtaining $H^J\in\mathcal K_{-1}$ and $N_\beta(H^JB)\le B_0|B|$. Needs the $H_0$ bound inherited from $q_0$; complex and weighted as above. |
| I:13974–13975 | J8 uses the assumed $q_0$ walk family to expand the Neumann series without resumming, retaining local analytic dependence and side branches. Uniform convergence of current insertions uses the same two $1/2$ ceilings. |
| I:14377,14406,14441,14469,14471,14476 | Response-chart definition and representation: explicitly inserts $Q^*(q_0-a)\widetilde B$ and $Q^*q_0\widetilde B$. Algebra reads the inverse identity; existence and bounds of the chart additionally use the background-propagator estimates. Background and datum are complex; $\bar\varepsilon_4,c_9$ depend on early constants. |
| I:14655 | Analyticity part of chart existence invokes analyticity of $q_0$ and the composed operators on the full admitted complex domain. An unspecified finite-volume analytic neighbourhood would not suffice. |
| I:14715–14717,14733,14736,14761,14772–14774 | Linear chart bound K3 explicitly assumes both inverse properties; its actual inverse estimate is $|Q^*(q_0-a)\widetilde B|_{(-3)}\le C'|\widetilde B|_{(-1)}=C'|B|$. Needs $C'(d,L)$ and yields $N_\beta(\mathcal H^J)\le C^K_9|B|$, $|\Lambda^J|_{(-3)},|\mathfrak J|_{(-3)}\le C_{\mathfrak J}|B|$. Walk locality is in the premise, not separately used in this displayed norm step. |
| I:14831 | First variation inserts $Q^*(q_0-a)\ell^{-1}v$ in $\delta\Lambda^J[v]$. Reads the same order $-2$ bound and weighted decay for localized $v$, with $C'_9,C'_{\mathfrak J}$ uniform. No second response derivative is taken. |
| I:15271–15279,15347–15348 | Chart walk-localization K10: actual $q_0$ pieces, hulls and side branches get the product of all met cube switches. For $|s(\Delta)|\le e^{\kappa_1}$, $\delta_1M\ge\kappa_1$, primitives have $B_0e^{16\kappa_1}$ bounds and composites $B_0e^{c_{\mathbb K}\kappa_1}$ in the specified norms. Needs spare anchored-length exponentials, analytic terms and exact component locality at zero switches. Reads complex local data. Equal total operators at $s=1$ cannot replace this family. |
| I:15770,15796 | Diagonal-exactness proof uses $P_0^T\Delta_a=\Delta_a-Q^*q_0Q$ and the chart representation. Starts at the real on-shell minimizer and real $B$, then extends in complex $B$. Reads inverse algebra; the chart's prior existence/uniqueness estimates remain inputs. No new walk theorem. |
| I:19583,19617,19750 | Free-current operator theorem assumes BP07 explicitly, then imports J2–J8 and K10. Reads complex independent-current operators, (3.132)/(3.133)/(3.137), their local walks and switch bounds. The Laplacian member is kept only for $G_0,H_0$. Constants follow the section's early-radius, geometry-floor, later-datum-ceiling order. |
| I:166593–166594 | Dependency list: “printed without proof; cited as printed.” Status inventory, not a further bound or locality assertion. |
| II:54465,54513,54523,54526,54617–54622 | `5.8:prop-local-decay` renames $q_0$ as $C_Q$. Assumes real (3.35), $M\alpha_0\le a_0$, for the paired-cutoff backgrounds. Reads physical-density block kernels for $C_Q,H_0,\nabla H_0,\Theta=\ell^{-1}(C_Q-a)\ell^{-1}$ with exponential $e^{-8\delta_1d}$, $\delta_1=\delta_0/32$, sup norms and inherited Hölder norms where listed. This is spatial decay, not exact walk locality. It imports an additional local-decay lemma. The within-layer sentence at 54617–54620 conflicts with the prior visual reading in B99; see §3. |
| II:60313 | Chapter dependency list for two-cutoff comparisons and clause (v) lists (3.132)–(3.133) among background propagator inputs. No additional theorem, norm or constant is stated on this line; the applicable local statement is the preceding Chapter-5 package. |
| III:36359 | Perfect-action second jet uses the **$G_1$ inverse**, not bare $q_0$, on complex (3.37)–(3.38) data. Reads $|a^{(2)}_{\mathfrak B}(c,c';V)|\le C_2e^{-\delta_1d(c,c')}$ on $\mathbb D(r_c)$. Scale cancellation in $d=4$ at equal levels and CMP96 Lemma 2.1 absorb unequal levels. No exact hull locality is asserted. It also needs the current-correction extension; BP07 alone does not prove that entire package. |
| III:111329 | Closing printed-sentence list repeats BP07's attribution; no new proof or quantitative requirement. |

This inventory is exhaustive for the requested labels, equation citation and inverse symbol
in the pinned three files. It is not a claim that every indirect downstream consequence
has been independently checked.

## 3. Existing repository work and its checks

| Source and lines | What is already supplied; check standing; remaining difference |
|---|---|
| `library/chain-ca.md:298–316`, P07 at 308 | Dependency map only. Records inverse bounds/walks as a printed Balaban sentence bundle and points to I:14711 and 166593–166594. By Codex; FINISH 298 says “map only, not checked”. No inverse proof. |
| `library/b109.md:2966–3152`, P18, and result 3714–3730 | Claims LQ on a **uniform layer**, after P17's intrinsic local complex mixed inverses. Cutoffs (96), local mixed parametrix (97), commutator residual (98)–(99), patch contraction (100), inverse words (101), full-read tree majorants (102)–(103), then Schur elimination identify the negative multiplier block as $(QG_0Q^T)^{-1}$. Includes holomorphy on admitted local union data without a global extension. Unit coarse rows remove the layered scale issue. Its own first paragraph says “not yet the full layered field-operator package or B109”; its endpoint repeats that limit. By Codex; **P18 has no recorded independent check**. `gates/p20-gate.md:15` explicitly excludes P17–P18 from its reading. Do not call P20's check a P18 check. |
| `library/b99.md:306–386`, B1–B2 | Physical adjoints, scalar projection and constrained-energy/Schur algebra. Abstract Gram lower-bound reduction retains its smooth-lift premise. Not local analytic inverse walks. |
| `library/b99.md:1344–1593`, B13–B14 | B13 builds a smooth actual comb-row right inverse. B14 proves the **real** $G_0$ field Gram lower/upper bounds, exponential inverse entries and physical densities (52)–(59), then $H_0,\nabla H_0,\Theta$ bounds. Uses B102 O/H9–H13 and admitted boundary/nest hypotheses. Does not assert mixed second-derivative/Hölder members or analytic hull-local inverse words. By Codex. B13 **(47) only** checked by Claude in `b99-w.md:63–69`; B13 (48) and **B14 were not checked there** (`:71`). |
| `library/b99.md:1968–2207`, B17; 2281–2480 failed attacks; 2526–2565 result | Conditional intrinsic resolvent/root operation from a suitable local analytic precision family plus accretivity. It does not construct that premise or a bare layered $q_0$ family. Preserves the failed inferences: real positivity does not give large complex switch discs; operator-norm contraction does not give unsigned word sums; decaying entries need not depend only on nearby data. No counterexample to BP07. B99 remains only partly checked. |
| `library/b99.md:119–140` | Reports a **visual PDF** check of (3.132), physical-density scale $s_y^{-2}s_{y'}^{-4}$ and spatial $d(y,y')$, versus II:54617–54620's within-layer claim. Also warns that the $G$ preceding printed (3.132) is already current-modified by (3.120)/(3.130), whereas the account's $G_0$ is earlier. This is prior evidence, not a new PDF reading by this digest. Do not identify the two operators by typography. |
| `library/b99-w.md:1–91,740–764`; `gates/b99w-gate.md:179–194` | Claude's conditional Lemma W constructs **one true-current precision family** on Balaban nests, via unfolded local mixed inverses and two Schur stages. Codex gpt-6-astra checked the implication and prescribed repairs; FINISH 394 records those applied. Supplies useful local-inverse/branch/read-set machinery. Does not prove arbitrary independent-current/switch/assigned-sheet families or B17's local accretivity. A precision family's multiplier blocks are related machinery, not a stated theorem for BP07's complete bare S1–S2 scope. N1–N6 supplier qualifications remain. |
| `library/lrb.md:1–12,819–847`; `gates/lrb-gate.md:1–18`; FINISH 305 | Codex's local real-base/Gaussian comparison for the account's **preassigned** walk families, conditional on (a)–(d). Checked line by line by Claude, first failing step none, with repairs recorded in FINISH. Its opening explicitly says it does not prove the walk hypothesis or underlying positivity. Thus it cannot supply the inverse walks it consumes. |

### Every FINISH row naming these notes

Case-insensitive search was saved in `/tmp/print-inverse-digest/finish-all.txt`.
The row number and file line are separate. Related derivative rows are included even
where their task is not BP07. The uppercase “B99b” at row 382 is also retained.

| FINISH row (file line) | Evidence and check boundary |
|---|---|
| 298 (364), `chain-ca` | Map done by Codex, not checked. |
| 303 (369), `port-p1` | Uses chain-ca's tranche order; 14 base/combinatoric ports checked by Claude with three repairs. No inverse-walk proof. |
| 305 (371), `lrb` | Frozen local real base, checked by Claude, conditional on its declared walk/positivity premises. |
| 325 (391), `b109` | P1–P21 claimed with premises; full small-field theorem open; row does not record a P18 check. |
| 332 (398), `l17` | Failed complex curvature-only tower attacks; best bound uses b109 (110). Not an inverse proof. |
| 334 (400), `l17c` | Corrected tower admission from b109 (110); different obligation. |
| 336 (402), `l17c-gate` | Queued check of that consumer correction, not P18. |
| 340 (406), `p10-check` | Queued check of chain-ca A10/A15/A17/A19/A20 stability port; not BP07. |
| 351 (417), `wu-lrb` | Queued clean write-up from frozen lrb/gate; adds no walk supplier. |
| 366 (432), `p20-gate` | Queued row text; actual report exists and excludes P17–P18. Relevant P20 check is not blanket B109 verification. |
| 367 (433), `uses-lrb-lsc` | Digest of three LRB consumers plus last-scale consumers; lead spot-check, not inverse verification. |
| 368 (434), `lsc-uses-check` | Queued last-scale consumer check of that digest; no BP07 proof. |
| 376 (442), `prior-1` | Five prior digests including b99-w, all partly covered; reading records, not proof checks. |
| 377 (443), `b99-w` | Conditional true-current Lemma W; current limitations retained above. |
| 378 (444), `cm-gate` | Codex check of CM components; merger not established. B99 owns the cited conditioned-walk leaf; CM old-term O3 stays separate. |
| 382 (448), `ca-gate` | Names the B99b-T314 decoupling-bracket supplier among open admission dependencies; not a B99 inverse check. |
| 393 (459), `b99w-gate` | Codex: advance repaired conditional W; keeps accretivity, independent-current/switch families, assignment and O3 open. |
| 394 (460), `b99w-r1` | Codex repairs applied at `ea7e02d77`; lead read narrowed downstream claim/open table. |
| 400 (466), `bundle-value` | LRB deferred in outward-contribution ranking. This is a scope/value decision, not changed mathematical coverage. |

Rows 423–424 (489–490) assign this digest and the later proof respectively. Their
negative prior-search summary is a recorded search result, not a proof of nonexistence
of another argument. No separate original B99 FINISH row is present at this revision.

## 4. What ports, and what remains new

The outline does not supply a concealed full proof of this target. SA:10264–10287
announces flat bounds and real one-lattice comparisons. SA:11076–11110 proves a
**site** smooth-lift lower-bound mechanism for $Q'G'^2Q'^T$. It is a different Gram.
SA:11471–11506 gives the useful **field** duality reduction (PX136–PX139), conditional
on an actual smooth right inverse, a trace estimate and exponential cell Schur bounds.
It explicitly distinguishes the counting scale $\xi_c^{-3}\xi_d$ from the squared-site
Gram scale. The conditional argument and normalization calculation are portable;
they do not establish every actual nonflat complex premise or an intrinsic local family.

Already usable as attributed prior work: the real B14 Gram/lift bounds on their exact
class; P18's uniform-layer mixed-system construction subject to its unreviewed proof;
the checked conditional W machinery and its complete supplier reads; the frozen flat
suppliers; and Balaban's local-inverse/parametrix/walk construction once its hypotheses
and operator changes are checked. Do not repeat their proofs as if absent.

The new proof lane must supply or explicitly reduce the **layered** S1–S2 operator,
including complex twists, actual analytic transposes, boundary/nest geometry and physical
row pairings. It must retain all local model reads when eliminating the site projection.
It needs separate local inverses on the admitted local datum, not compressions of an
already global inverse. It must bound absolute transitions, count walk labels rather
than fine coordinates, prove convergence uniformly in mesh/depth/volume, and identify
the output as this $q_0$. The change from $G'^2$ to $G_0$ changes the block variables,
source/target spaces, lower-bound mechanism, scale normalization and cutoff residuals.
The complex extension needs quantitative relative perturbations on the full S2 ball;
holomorphy of finite matrices alone provides no uniform radius or bound.

Even a successful BP07 proof leaves the averaging-derivative input, current corrections,
local accretivity, account assignment and CM-O3 at their existing scopes and owners.
It must explicitly reconcile the (3.132) spatial-distance and current-modified-$G$
issues before asserting compatibility with all II/III consumers.

## 5. Exact first proof-lane step

First recover and verify the missing displayed formulas (3.99),(3.108),(3.132)
from a legible facsimile or an already verified complete transcription. The OCR
blocks above cannot set exact rates, scale powers or constants. This is source
preparation, not a request for computer-assisted proof.

The first mathematical step is then the **operator/normalization comparison**, before any new series:
write the account's $\Delta_a,G_0,Q,Q^T$ and the local mixed system whose multiplier
Schur complement is $-QG_0Q^T$, in the original physical layer pairings. Place beside
it the system used in Balaban Theorem 3.9 and P18 (66), with a row for every block,
boundary condition, scale multiplier and complete read set. Resolve which printed
$G$ occurs at (3.132) and state exactly why its asserted bound is the required bare
zero-current bound or needs a separate reduction. Keep OCR uncertainty explicit.

Then state the single target theorem once, with S1–S2, early radii, geometric floors,
all constants/dependencies, density-to-counting conversion and spare walk majorants.
Its first mathematical obligation is the uniform local layered mixed-inverse estimate
on cut-down cubes, extending P17–P18 while retaining the already proved real B14 lift
and the actual boundary class. Test that estimate against the consumer table before
attempting the parametrix. This digest supplies no proof of that obligation.

RESULT: Partly covered; real Gram bounds and uniform-layer/local-word machinery exist, but layered complex inverse walks remain open; exact display transcription is limited by damaged OCR at (3.99), (3.108), and (3.132).
