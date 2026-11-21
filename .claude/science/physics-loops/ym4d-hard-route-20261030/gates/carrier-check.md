# Carrier check, queue row 218
Provenance: Codex (GPT-6; exact runtime model ID unavailable), xhigh queue assignment; checkout `f1b3820479af78e39a9b0dca6742a585beda174f`; Sussman–Alpoge `31a47c543775`; research text, not an audit; grants no status.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline (`SA`). This checks Claude's `library/carrier-adopt.md`, Sections 2–6, by hand. Inputs from A2 and repaired h-walk remain premises.

## Section 2: which series?

- **WRONG:** “constructs none for the covariance,” hence “nothing to conflict with.” First failure: omission of SA 10533–10550. Mechanisms (f)–(g) construct local parametrices and tree expansions; (h) places `C^(k)(Y)` in the enlarged inverse system. SA 10477 explicitly applies those mechanisms to that covariance. SA 10311–10338 already prescribes its walk terms, bounds and locality. These passages give a construction scheme, not a proof checked here. Missing details do not make the stored series unassigned.
- **CORRECT-NO-ADVANCE:** SA 17540–17564 adds no new coefficient formula; it uses the preceding walk/resolvent series. Completing the square fixes the full Schur complement, not either part of its cut. First failing step none.
- **CORRECT-NO-ADVANCE:** Definition D changes the indexing and term bounds; (4.1) concerns that replacement. The distinction between uncut hulls and field carriers is explicit at SA 10210 and 10558. First failing step none. Thus adoption needs a replacement argument; it is not merely filling an unspecified covariance formula.

## Section 3: readers

- **CORRECT-NO-ADVANCE:** The listed cut readers use carriers, locality, holomorphy, absolute bounds and coercivity. None directly requires the walk index or a separate `M_1^{-1/2}` factor. Checked against the cited passages; first failing step none. SA 10558–10560 uses that factor for the original torus construction. Lemma L supplies a different construction for D.
- **WRONG:** The stored-Gaussian row sets `beta=a/2`. First failure: `K>=a/2` gives `exp(-<A',KA'>/2)<=exp(-a||A'||²/4)`. Use `beta=a/4`, or `a/8` when half the exponent pays witnesses. This preserves a constant cost per coordinate. The other witness rows correctly require a gap; they do not prove the remaining admission or envelope inputs.

## Section 4: Definition D and lemmas

Checked line by line by Codex:

| Statement | Verdict | First failing step |
|---|---|---|
| Definition D and property (T), as a new series | ADVANCE | None. Endpoints join the factor trees; transposition preserves carriers and moments. |
| Lemma L(a)–(c) | ADVANCE | None, under the stated h-walk locality/covariance inputs. Every read in `N^n(x,y)` lies within `nr+R_h` of `x`. Fixed polynomial coefficients preserve the asserted symmetries. |
| Lemma P | ADVANCE | None. Rejection gives `l>=s/2`; the cube count gives `d<=32+256l/(LM)`. The four-quarter allocation leaves `exp(-theta*s/16)(LM+1)^4`, bounded by a constant times `exp(-theta*s/32)`. |
| Lemma C(a)–(b) | ADVANCE | None. With `w=-A_JJ^{-1}A_JI v`, `(v,w)^*A(v,w)=v^*Sv`. The absolute row and column tails then cost at most `W exp(-kappa*s)`. No symmetry is needed. |

## Section 5: adoption and Theorem A

- **WRONG** as a claim that D merely specifies an unconstructed outline series. First failure: Section 2 above. **ADVANCE** as an explicit replacement with the proved properties. It changes both kept and rejected parts; their sum remains the same Schur complement.
- **ADVANCE: Theorem A(i)–(iii).** First failing step none for D. `D(carrier)<=l+2R_*` and inv-root (11), (15) give the stated `W_A,W_C,kappa=theta/2`. Product moments give `W_*=W_A+W_A²W_C`. Rejected diameter is at least `s`; hence `||S-K||<=W_*exp(-theta*s/2)`. Lemma C yields `Re K>=a/2` at the stated floor. At real pairs this is `K>=a/2`. This proves (4.1) for D, not for a different assigned series.
- **ADVANCE: Theorem A(iv)–(v) and constant order.** First failing step none under Lemma P's geometric floors and the stated locality inputs. Length moments give the pinned bounds; local holomorphy gives the pair dependence. All added conditions are later floors on `M`. No remaining 2.13 envelope or admission claim follows.

## Section 6: um-envelope (6)

**ADVANCE, for the specified inv-root series; checked line by line by Codex, first failing step none.** Integration gives `r(1)=A^{-1/2}` and moment `U=2p_r/sqrt(lambda)`. Two tags cost at most `exp(32*kappa-bar+C_g*kappa-bar*(l_1+l_2)/M)`. A varied product crosses the collar, so its norm is at most `WU exp(32*kappa-bar-dM)`. Cauchy bounds for the two field changes contribute `2WU*epsilon/h+4WU*epsilon/h`. Thus (6) holds with `R=U`, `B=W`, and `T=2WU+6WU/h`, with the stated coefficient-ratio enlargement.

At `s=1`, symmetry gives the required Schur identity. Normal convergence gives parameter holomorphy; real coefficients give the real reference. These are the readers at SA 14160–14243. Constants precede `M,kappa-bar`, so the conditional order gives `C_0^UM<=1` and `Theta=O(1)`. Equality with another series at `s!=1` is neither proved nor needed for these readers. The A2, h-walk and remaining constant-table inputs stay premises.
