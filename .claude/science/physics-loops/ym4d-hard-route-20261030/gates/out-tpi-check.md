# Check of library/out-tpi.md and library/out-tpi-issue.md (outward TPI note)

Checked once, line by line, by Claude (Opus 5.5), 2026-11-08. One reading.
Not an audit. No status granted. Source: N = YM4_1400.tex at 2bc0658f
(local copy, 136637 lines, read only by grep and bounded ranges).

**Verdict: FIX.** Not BLOCK: N states the bound at 102280-102281 and does
not prove it anywhere. But N proves the key comparison step in another form
(CF12 at 5631-5634). The note misses it and claims that step as new. Apply
fixes F1-F9, then post. The math matches library/tpi.md.

## Findings

### 1. Is the bound proved in N? No. One missed supplier.

1. CONFIRMED. Every search in note §7 (note 464-485) reproduces exactly
   with rg over the whole of N. The 118 `L^{-4` hits match line for line.
2. CONFIRMED. Extra whole-file searches found no proof of
   |G_{k_1}(p,q)| <= C L^{-4k_1}: `\mathsf{W}_`, `\mathsf W_`, `W}_K`, `W_K`,
   `mathrm{bg}` (all 32 hits), `linear background`, `background curvature`,
   `coarse kernel`, `coarse complement`, `omitted coarse`, `terminal covariance`,
   `a_K^4`, `\eta_k^4`, `mathcal{H}_j`, `mathcal H_j`, `Q^{\mathrm{pl}}`,
   `plaquette average`, `C^{\mathrm{curv}}`, `mathsf V_`, `E_n(a)`,
   `eighted Cauchy`, `Green`. N 109329-109332 even says its estimate is
   proved "rather than assuming ... an all-depth unweighted covariance bound".
   N 110366-110375 says the projection identity "contains no spatial decay
   assertion". N 101070 names V_{j-1} = Cov(Q^pl F) but never bounds it.
   The terminal piece G_K = P_{W_K} is bounded nowhere. So the slice
   estimate alone cannot give the bound at once.
3. **MISSED SUPPLIER (FIX F1-F3).** N 5605-5634 (CF11-CF12), right after the
   cited contraction, defines E_k(a) = min{||dw||^2 : P^[k]w = a} and proves
   E_k(a) >= ||d_n a||^2. N 6522-6528 repeats this. E_k is the precision of
   the blocked potential law (N 5639: "the classical action part of the
   actual flat precision"). So note (9)-(10) is the covariance form of
   CF12. N uses CF12 only for the fluctuation gap (CF13), not for the
   background covariance. The new parts are: read CF12 as a covariance bound
   for B_j; bound its diagonal, (11)-(13); lift it pathwise, (14)-(15).
   N 100993 already gives |H_j(p,b)| <= C eta_j^2 e^{-delta...}, which sums
   to (8). So the proof is a short assembly of N's proved pieces plus a 4D
   lattice Green count. The issue is still correct. Its weight is smaller
   than "a variance comparison" suggests. The owner should weigh this in
   the value analysis.
4. CONFIRMED. CA-II 69927-69929, 69958-69965 and 70002-70016 read as note
   509-520 says. The CA-II proof sketch takes the same route
   ("the kernel of this composite and the covariance of B").

### 2. Claims about their text

5. CONFIRMED. N 102258-102291: G_j = C^bg_{K,K-j} (102259), G_j^o = G_j - G_{k_1}
   (102265), telescoping to (1/2)(G_{k_0}-G_{k_1})^2 (102277), separated bound
   (102278-102279), "the coarse covariance bound gives |G_{k_1}| <= CL^{-4k_1}"
   (102280-102281), error with (d^ L^-n)^4 + (d^ L^-n)^8 (102283-102289).
   The index check d/a_K L^{-k_1} = d^ L^{-n} holds. Later use: N 106650-106651.
6. CONFIRMED. Strong inverse: prop:hb-joint-strong-inverse at N 41990-42038
   (label 41991, bound 42001, formula 42030). Geometry N 41668-41677
   (integer side M >= 2, depth k >= 0). Rows N 41698-41702. Range identity
   N 25839-25854. Hodge identity N 41968-41969. Curvature identification
   N 100996-101019. Gauge comparison N 101043-101077. Fourier N 124100-124139.
   Contraction CF8-CF9 N 5568-5602.
7. CONFIRMED. Slice estimate displays: N 4337 and N 100994.
8. **FIX F4.** "Stipulated" (issue line 9; note 91, 432) is our task-spec word
   (items/tpi.txt). To them it says their estimate is unproved. N may prove
   it: N 6559-6575 (fx:flat-kernel-bounds) proves exponential bounds for the
   next-step flat covariance, and N 100993 plus N 101043-101077 transport it.
   I did not check that assembly. So do not judge it; just say we quote it.
9. **FIX F5.** Issue line 7, "The bound and the projection decomposition are
   already yours", sits next to "no proof" and can read as a contradiction.
10. MINOR (F8). Note 495: N 4325-4340 defines P_{W_j}; the name G_j first
    appears at N 102259. Note 23 cites 100996-101032 but its link is
    100989-101032. Harmless.

### 3. Mathematics vs library/tpi.md

11. CONFIRMED. §2-§4 match tpi.md (5)-(16) step for step: S_Q >= cI, (6) with
    Hölder 1/2, (7) h^2 d_h H_h, (8) row sums, (9)-(10), shells 80r^3,
    g_N(0) <= 5q(q+1)/(2N^2) <= 5/4, (14) pathwise, C_R = 5C_H^2/4, j = 0 and
    j = K. The Landau-gap sentence (note 136-140) adds only W2's description.
    No new unchecked step.
12. CONFIRMED. Dictionary: N's G_j = C^bg_{K,K-j} = P_{W_j} is tpi R_j;
    C_(j) = G_{j-1} - G_j is tpi G_j; a_{K-j} = L^{-(K-j)} = tpi a_j.
    Level shift: eta_{j-1}^4 = L^4 eta_j^4 and a_{K-j+1} = a_{K-j}/L are correct.

### 4. Scope and credit

13. CONFIRMED. "Does not cover" (note 434-444; issue line 11) is honest.
    The terminal level is included and G_K is not set to zero.
14. **FIX F6.** Note 20-22 says "Credit Ethan Sussman and Levent Alpoge ...
    Credit Tadeusz Balaban". The first is third person to the addressees and
    near the banned "credit belongs to them" form.
15. **FIX F7.** Internal process text must not go out: note 448-456 (checkout,
    library/prior, TP1-FREE registry, FINISH row 486, chunks, obligations.md),
    note 528-530 ("No issue was posted ... requested pinned-source draft"),
    and note 29-31 / the table at note 68-76 name files the readers cannot open.
    Issue line 9 "Your G_j is our R_j" points to a notation they never see.
    Note 529 also records that no live-repository or engagement check was
    made. The owner's posting rule requires that check before posting.

### 5. Writing

16. Mostly short, plain sentences. Fix "It keeps the terminal covariance"
    (issue line 11), which is unclear (F9). "Retained" in the issue title is
    our word; N says "coarse covariance bound".

## Exact replacement text

**F1 (note 12-15)** replace the paragraph with:
> Your CF12 at [N 5631–5634] already compares the classical blocked
> precision with the coarse Maxwell form: \(E_k(a)\ge\|\mathrm da\|^2\).
> We read this as a covariance bound for the actual blocked potential law.
> We then bound its diagonal on every coarse torus. Your curvature
> minimizer lifts this bound and gives the fourth power of the mesh.

**F2 (note 248)** replace "Your contraction proof, [N 5568–5605][contraction], applies to this map." with:
> Your contraction proof, [N 5568–5605][contraction], applies to this map.
> Its consequence CF12, [N 5631–5634], is the precision form of (10) below.

**F3 (note 428)** replace "The new comparison is (9)–(15)." with:
> The inequality (9)–(10) is the covariance form of your CF12.
> The new steps are the diagonal bound (11)–(13) and the pathwise lift (14)–(15).

Also add a §7 table row after 5568–5605:
> | 5605–5634; 6522–6528 | CF11–CF12: \(E_k(a)\ge\|\mathrm da\|^2\). The precision form of (10). Used there for the fluctuation gap, not for the background covariance. |

**F4.** Note 91: "we retain the **stipulated slice estimate**" → "we quote your slice estimate".
Note 432: "The slice estimate (4) remains stipulated and is not used to prove (15)." →
"We quote the slice estimate (4). We do not reprove it, and the proof of (15) does not use it."
Issue line 9: "Your slice estimate at lines 4337 and 100994 remains stipulated for the adjoining tower. The retained covariance proof does not use that estimate. Your \(G_j\) is our \(R_j\)." →
> We quote your slice estimate at lines 4337 and 100994 for the full tower.
> We do not reprove it. The proof of the bound does not use it.

**F5 (issue lines 2-7)** replace the first two paragraphs after the greeting with:
> At [YM4_1400 102280–102281](…#L102278-L102281) your free calculation uses
> \(|G_{k_1}(p,q)|\le CL^{-4k_1}\). We found this statement and its later
> uses. We did not find a proof of it in the pinned file. The note records
> the whole-file searches and the passages we read.
>
> [This note](@NOTE_LINK@) gives a proof at every level, the terminal level
> included, uniformly in mesh and volume. The statement is yours. So are the
> pieces: your CF12 precision bound (lines 5631–5634), your strong inverse
> and your curvature minimizer. The note reads CF12 as a variance bound for
> the blocked potential, bounds its diagonal, and lifts it to the fine
> lattice. This gives the coarse factor in your error at 102283–102289.
> The free-field method is Balaban's.

**F6 (note 20-22)** replace with:
> The ported results below are yours.
> The free-field minimizer method is due to Tadeusz Balaban.

**F7.** Delete note 448-456 and 528-530. Replace note 29-31 with public links
to library/tpi.md and gates/tpi-check.md in the public repo, or delete them.
Delete the dictionary table (note 68-76) unless tpi.md is linked. Delete
"Your \(G_j\) is our \(R_j\)." from the issue (done in F4).

**F8 (note 495)** "Defines \(G_j\) through projections" → "Defines \(P_{\mathsf W_j}\) through projections".

**F9 (issue line 11)** "It keeps the terminal covariance." → "The bound covers the terminal level. It does not set \(G_K\) to zero."
Issue title → "A proof of the coarse covariance bound at YM4_1400 line 102280".

After the fixes, note 31 may read: "Claude (Opus 5.5) also checked this note
against the pinned source once (gates/out-tpi-check.md)."
