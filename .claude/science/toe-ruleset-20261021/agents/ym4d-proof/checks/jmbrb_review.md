# JMBRB fresh hostile review

Reviewed 2026-10-30 by a fresh-context Codex reviewer. This is **same-family
review: Codex reviewing Codex**. I did not author the note. The verdict
accepts a scoped OPEN research note and its conditional mathematical
lemmas; it does not certify LF-JMBR or a completed Yang--Mills proof.

The initially supplied file was verified as 753 lines with SHA256
`f26d7e5c366b87eb26b6d8c2f5dc4fda03b7c0e1bf507c75f2ec6ab16ecde030`.
The author made explicit hypothesis and scope corrections during review.
The final candidate reviewed here is **766 lines**, SHA256
`6320af2da97d532fbf802f2405541de8e20f6d350b575b46462fefb4c849bb0a`.
All JMBRB line locators below refer to that candidate. I reread each
affected argument after its correction.

I read `briefs_q/JMBRB/AUTHOR.md`, `PROCESS_LIGHT.md`, the standalone
review brief, and the complete initial JMBRB note. I checked the relevant
source passages using bounded reads after locating them with `rg -n`.
I independently re-derived the mathematical steps below. No numerical
experiment was necessary or run. This reviewer wrote only this file;
no source, log, audit, ledger, axiom or Git operation was changed.
The AUTHOR allowlist and parent task resolve the review-path conflict
in favor of `checks/jmbrb_review.md`.

## Item verdicts

### 1. Kernel, action and actual reference — CONFIRMED

**Locators:** `JMBRB.md:32-82`; `PROOF.md:2453-2457`;
`RD3.md:332-377`; `RD4.md:55-75`.

The arithmetic paired-contour mean is the supplied Decision-4 mean.
Removing the common `exp(-t)` from numerator and normalizer gives B1.
Consequently the negative logarithm is exactly
`S-t sum h_M+sum log Z_t(M)`. The U-dependent normalizer has not been
dropped. Higher effective actions are expressly distinguished from the
bare Wilson action.

B3 retains the particular all-cut denominator of RD3. The full-chain
partition function and an unrelated Gaussian reference are not used
in its place. B4 includes inactive vertices and original source readers;
the final explicit `mu>=0` agrees with RD4 and is needed by the support
weight inequalities. From
`s(U)=||I-U||_HS^2/(2N)>=||I-U||_op^2/(2N)`, the bare charge at the
raw cut is `u epsilon(u)^2/(2N)=u^delta/(2N)`. A cut on rescaled
curvature costs `p(g)^2/(2N)`, as stated.

**Fix:** none remaining. Any later application must retain this same
reference, source domain and effective-action scope.

### 2. B-RB and B-MASS — CONFIRMED at their stated real-measure scope

**Locators:** `JMBRB.md:86-172`; `RD3.md:366-377`.

Summing the exact sector partition before integrating gives B7 by
kernel normalization. The support elimination rule joins all factors
reading an integrated variable and retains every surviving reader.
This gives an exact support, which can be extensive. It does not imply
local smallness. Absence-of-other-failure conditions are retained.

Under the joint law `mu(dU)K(U,dV)`, the transported insertion is
`E[a(U)|V]`. Its integral equals `int a dmu`, and for nonnegative a this
is also its L1 norm. Thus a strict multiplicative decrease of the total
positive mass of all descendants is impossible. A constant insertion
is fixed. Conditioning an event of mass p produces `1_E/p`, whose
L1 norm is one. These are exact obstructions to the specified repeated
mass-pricing inference, not to an extracted RG transformation.

For the SU(2) diagnostic, Haar stationarity and `U=VW` reduce the
backward conditional average to `E_t W=lambda_t I`. Conjugation
invariance gives a scalar matrix and inversion makes it real. The
positive Haar neighborhood of the identity bounds the mass outside
`f>1-eta` by `m_eta^(-1) exp(-t eta/2)`. Therefore `lambda_t->1`.
This rules out the proposed uniform contraction for that diagnostic
kernel; the author correctly does not identify it with the full block
map or the renormalized irrelevant operator.

**Fix:** none remaining. Extraction or discarded/returned sectors must
be represented explicitly before invoking contraction instead of B9.

### 3. B-GAP and repeated fresh events — CONFIRMED

**Locators:** `JMBRB.md:176-226`; `CODEX_REVIEW_LARGE.md:35-45`;
`REVIEW_RLARGE_V3.md:99-142`.

There are at most `(1+4N/r)^(2N^2)` entry boxes, with Hilbert--Schmidt
diameter at most `r/sqrt(2)`. Representatives in occupied boxes cover
SU(N) by operator-norm r-balls. Left invariance gives equal Haar
volumes, so the covering proves B10. The non-sharp ambient exponent
`D=2N^2` is valid; no intrinsic-dimension estimate is imported.
Trace duality makes h_M one-Lipschitz. The `1/t` ball about a maximizer
then gives the denominator `e^(-1)(1+4Nt)^(-D)` and the stated pointwise
and probability gap bounds for `t>=1`.

Distinct output links are conditionally independent given the full
input. Integrating the latest prescribed event first proves B12 by
the tower property, including past-measurable adaptive selections when
their bounds are uniform. It does not allow conditioning on a future
history for free. The note explicitly retains that restriction and
does not convert a positive real bound into B4's complex activity norm.
At `a=a_0 u^(delta-1)`, the exponent is
`kappa a_0 u^delta-O(log u)`.

**Fix:** none remaining. The future-conditioned bridge remains an
actual missing input, as required by the cited RLARGE review.

### 4. B-GEOM, ribbon geometry and multiplicity — CONFIRMED

**Locators:** `JMBRB.md:228-315`; `RLARGE.md:964-1009`.

An axial path has at most `3(L-1)/2` transverse edges. Commuting its
length-L leg past one such edge uses L plaquettes, giving
`A_L=3L(L-1)/2`. Successive attachments multiply conjugated plaquette
holonomies; unitary telescoping proves the bound without commuting
nonabelian matrices. The central square uses `L^2` plaquettes.

The gap comparison is
`psi_M(V)>=||V-S||_op^2/(2N)-2||M-S||_op`.
On the smooth-input branch, B16 gives `L^2 eta_1<=epsilon/2`, so a bad
coarse plaquette has a link distance at least `epsilon/8`. The gap is
then at least
`epsilon^2/(128N)-epsilon^2/(256N)=epsilon^2/(256N)`.
This verifies all constants in the dichotomy.

A link belongs to at most six distinct geometric plaquettes in four
dimensions. Thus n selected plaquettes use at least n/6 distinct
witness links. The `4^n` union bound gives B17 and dividing the gap
price by six gives B18's coefficient `kappa/(1536N)`. It does not assume
independence of plaquettes. Periodic projection does not improve the
ribbon area: repeated plaquettes must still be counted with
multiplicity, as the note requires.

The rough-input branch is not a new kernel gap event. For small
epsilon the present estimate uses `eta_1` proportional to epsilon^2,
so the available bare threshold lower bound scales as
`u eta_1^2` proportional to `u^(2delta-1)`. This identifies an insufficient
majorant when `delta<=1/2`; it is not a lower bound on the integrated
rough-input weight. The M=0 example is correctly limited to a mean-domain
diagnostic, not an asserted actual history.

**Fix:** none remaining. A sharper geometric theorem or a controlled
rough-input return remains necessary for actual closure.

### 5. B-RENEW, B20 and the frozen comparator — CONFIRMED implications

**Locators:** `JMBRB.md:319-377`; `F17.md:225-255,261-305`.

Given a new per-step bound on the same absolute integral, multiplying
r factors bounded by theta and summing r proves B19's
`theta/(1-theta)`. This is expressly a non-branching estimate. It does
not count arbitrary merger or branching histories for free.

For B20, a coarse root y has at most `L^4` fine preimages. Every support
whose image contains y contains at least one such preimage. Apply the
triangle inequality and `exp(mu|pi(S)|)<=exp(mu|S|)` and sum over those
preimages. The final unchanged-function-supremum premise is essential.
The conclusion does not apply to a changed field map, source domain,
halo or norm without its additional cost.

Under B21, `c u^delta` dominates `d log(1+u)` and every fixed per-step
entropy. This permits n=1 conditionally. In B22 the upper flow bracket
makes the negative term only order `r^delta`, while the volume/boundary
term grows linearly in r. The displayed fixed-size majorant therefore
fails. For a final linear price the lower bracket instead gives the
stated strict sufficient condition. F17's critical polynomial correction
concerns the linear-price equality case; the final comparison table
now distinguishes that case from sublinear B22.

**Fix:** none remaining. The actual full-reader, same-reference renewal
bound is still OPEN, exactly as the note says.

### 6. B-SEAM, B-MATCH, complex TV and B27 — CONFIRMED scoped bounds

**Locators:** `JMBRB.md:381-477`; `LFPRICE.md:202-237,319-357`;
`RD4.md:352-397`; `SOFTHARD.md:291-295`.

Since `|h_M|<=1`, normalized kernels lie between `exp(-2t)` and
`exp(2t)`. Changing M by d changes log Z by at most td and log k by
at most 2td. Arbitrary replacements cost at most 4t per kernel and
2u per Wilson factor. This yields B24 with identical measures and
hard selectors. It cannot compare different hard supports or bound
complex cancellation. An order-u upper debit cannot be paid from the
displayed sublinear threshold using this envelope.

The raw action allocation is legitimate: allocating distinct owned
witnesses gives a dimensionless Wilson energy at least
`theta_c epsilon^2 n/(2N)`, hence an exponent with an additional u.
The remaining original integral divided by Z_A is still owed. It is
not legitimate to charge that fraction again after reblocking.

For B25, every differing supported coefficient meets Bdy. Summing over
one such vertex and then over all Bdy bounds the difference by
`2(q+b)|Bdy|`. The final text now explicitly cancels equal nonzero
empty-support prefactors or pays their ratio separately. Geometric
proximity alone does not supply equality of logarithmic coefficients.

The two-point complex example has denominator d and numerator
`exp(h)-1+d`, giving exactly the claimed divergent ratio as d tends
to zero. This verifies the need for total variation or comparable
cancellation control; it makes no assertion about zeros of actual Z_A.

Writing `A=W^*M`, the real part of the holomorphic exponent at `We^X`
is `(t/N) Re tr(cosh(X)A)`. Positivity of `cosh(X)-I` proves B27.
For fixed rho and `t>=1`, the natural width has cost at most
`rho^2 cosh(rho)/2` per link. The corrected lower bound on t is
needed for this uniform statement. Neither this numerator estimate
nor SOFTHARD G2 proves a nonzero analytic denominator.

**Fix:** none remaining. Actual matching, complex reference control,
fixed selectors and source analyticity remain required.

### 7. B-JOINT — CONFIRMED, including convergence and conditional nonvanishing

**Locators:** `JMBRB.md:481-571`; `RD4.md:211-258`;
`REVIEW_LFPRICE.md:190-230`.

Expanding the finite product first is exact. A selected set decomposes
uniquely into overlap components. Their integrals factor only after
all readers are included, because only then are their coordinate sets
disjoint. The final coefficient extension now explicitly requires an
empty coefficient of one, componentwise factorization, component-local
readers, and holomorphy or parameter independence with envelopes.
These prevent a hidden global selector, empty scalar or nonholomorphic
coefficient from evading the theorem. Unvisited normalized cells are
integrated before absolute values; B29 pays total variation on visited
cells and controls every overlapping selected family jointly.

For the first tree estimate, set
`v_i=e^((mu+1)|S_i|)alpha_i`, `b_i=e^((mu+2)|S_i|)alpha_i`.
The child sum at i is at most `Q|S_i|`, so
`v_i exp(sum_overlap b_j)<=v_i exp(|S_i|)=b_i`.
Iteration from zero bounds the rooted tree series. Every connected
selection has a spanning tree; allowing repeated labels increases
the positive tree sum. Marking an atom at the spatial root gives the
gas norm at exponent `mu+1` at most Q.

For the logarithm, fix an incompatibility graph on the tuple, including
repeated polymer labels. A graph with Kruskal tree T may add precisely
the available edges larger than every edge of their T-path. Thus its
fiber is the interval `[T,R(T)]`; its alternating sum has modulus at
most one. The spanning-tree bound follows. The second rooted recursion
spends the remaining unit of support weight and gives log norm at mu
at most Q. Root marking changes `1/m!` to `1/(m-1)!` and does not
remove repeated labels.

Scaling every original atom by z replaces its alpha by `|z|alpha`.
Both supersolution arguments still hold at `|z|<=2` with
`Q_z<=2Q<=1/2`. The exponential of the connected series agrees with
the finite gas near zero by the finite formal expansion and then
throughout the disc by analytic continuation. This proves nonvanishing
at z=1 without assuming it. Physical-parameter holomorphy separately
uses the corrected atom, density, coefficient and envelope hypotheses.

The remote shared-sign example also checks: the connected difference
is exactly `epsilon^2 s^2`. A spatially remote shared reader cannot be
deleted before the grouping. B28's formal expansion of hard indicators
does not establish B29's smallness.

**Fix:** none remaining. The actual matched product representation,
joint budget and full-reader bounds for R_h/Z_A are not constructed.

### 8. B30's joint price and count budget — CONFIRMED implication

**Locators:** `JMBRB.md:573-591`; `RD4.md:399-413`.

At each charged size n, the hypothesized root sum is bounded by
`A^n exp(((mu+2)c_s-nu_j)n)=r_j^n`. Summing from n=1 gives
`r_j/(1-r_j)` in the final explicit domain `r_j<1`. At `r_j<=1/9`
this is at most 1/8, which together with a small-field budget 1/8
gives Q<=1/4. All reference, boundary, TV and continuation debits are
subtracted from the same joint exponent. The note correctly avoids
combining scalar prices from unrelated laws.

**Fix:** the missing convergence-domain qualification was supplied and
verified. No fix remains. The assumed count A and full support bound
c_s are not obtained from a static shape count, especially for old
source readers.

### 9. B31 and B-ITER/B33 — CONFIRMED implications

**Locators:** `JMBRB.md:595-686`.

On any complex radial disc, the first three vanishing Taylor terms
make `F(wz)/w^3` holomorphic at zero. The maximum principle gives
`|F(az)|<=a^3 M`. With `a=L^(-2)`, multiplication by L^4 gives
`L^4 L^(-6)=L^(-2)`, exactly B31. The note explicitly restricts this
to the defined ideal dilation and does not identify it with the
fluctuating, source-dependent or boundary-dependent RG operator.

Under B32 and the final nonnegative-majorant assumptions,
`C x_j^2<=C M x_j` on `[0,M]`, hence
`x_(j+1)<=theta x_j+B epsilon_*`.
B33 makes `[0,M]` invariant; summing the affine recurrence gives the
displayed sharper estimate. The final feasibility statement now
requires bounded B,C and a fixed contraction margin. For a margin
sigma, choose M with `C M<=sigma/3`, then choose the coupling ceiling
so `B s_*<=sigma/3` and `B epsilon_*<=sigma M/3`. This supplies the
claimed conditional singleton mechanism, subject also to `x_0<=M`.

Every completion/chart/coherent-input failure has an assigned term.
No unpriced failed singleton disappears by relabeling or by fictitiously
enlarging its charged support. B12 alone proves neither the complex
continuation norm s_j nor the remaining-failure norm eta_j. The actual
operator estimate, relevant/marginal recursion and domain induction
remain open. A future-conditioned reference needs the separate ordered
induction stated in the text.

**Fix:** none remaining. B31 and B33 are not evidence that those missing
operator hypotheses hold for the actual model.

### 10. All five clause statuses — CONFIRMED as OPEN

**Locators:** `JMBRB.md:692-701,729-755`;
`LFPRICE.md:654-699`.

| Clause | Review verdict | Required scientific construction before promotion |
|---|---|---|
| 1 | OPEN; exact raw sectors are PROVEN | Construct the local adapted representation, actual charts/cuts and reference agreeing with this Z_A off the full boundary. |
| 2 | OPEN | Control the rough-input branch and the joint charged/reference/boundary integral; raw Wilson allocation and smooth-input kernel events do not supply it. |
| 3 | OPEN | Build a common nonzero complex reference and local TV accounting on the actual original-source/coarse domain; B27 alone cannot do this. |
| 4 | OPEN at quantitative scope; overlap algebra is PROVEN | Supply actual joint atom budgets, integrated type counts and full supports, including inactive/source/tail readers. |
| 5 | OPEN; proposed construction is ARGUED | Prove the extracted return operator, all failed-return bounds, coefficient recursion and invariant domain/norm. |

The five rows match the actual LF-JMBR consumer. Some obligations may be
proved together by one reference expansion; the note does not claim
five logically independent obstructions. FR, KR and TC remain named
inputs whose actual scopes must cover these integrals. The brief's
desired actual singleton theorem has not been proved, and the note
does not report that it has.

**Fix:** none required to land this OPEN research note. The constructions
in this table are binding before a future PROVEN claim for LF-JMBR.

### 11. Literature, Route A comparison and no-go discipline — CONFIRMED

**Locators:** `JMBRB.md:19-28,703-725,757-766`;
`LARGE55.md:488-514,725-734`;
`CODEX_REVIEW_LARGE.md:35-69,193-229`;
`REVIEW_RLARGE_V3.md:99-142`.

Direct primary-source inspection confirms that the two cited Dimock
papers treat scalar phi^4 theory in d=3. Part II section 3.3, Remark 3,
distinguishes Balaban's recycling contribution from what that model
requires. This supports the note's limited attribution, not a
four-dimensional nonabelian theorem. See [Dimock, Part II, section 3.3](https://arxiv.org/html/1212.5562)
and [Dimock, Part III, abstract](https://arxiv.org/abs/1304.0705).

LARGE55 section 6.3 actually freezes large components and failed
returns. E13 restores a boundary debit but leaves its application
ARGUED. Its review retains the geometric, normalization, complex-ratio
and failed-return gaps. RLARGE review S-1/S-2 explicitly requires a
future-tilt bridge and a noncircular induction order. JMBRB reports
these sources accurately and does not use their unproved applications
as evidence for closure.

My targeted hidden-file filename search under
`/Users/jonBridger/ym4d-lanes` also found no JMBRA report. The comparison
is correctly labeled as one with LFPRICE's frozen-component architecture;
it is not a review of unseen Route A work. I did not independently
verify the conversational assertion that the user was asked for its
location; that assertion carries no mathematical weight.

The failed estimates B22, the crude seam debit and the eta_1 threshold
are not represented as lower bounds on actual Yang--Mills weights.
The exact counterarguments concern transported positive mass and an
uncontrolled complex ratio. No exhausted-route or physical no-go
conclusion follows, and none is claimed.

**Fix:** none remaining at this scope.

## Binding fixes and final scope

**No unresolved binding defect remains in the final candidate's scoped
claims.** The following corrections were checked during review:

- B4 and B20 now specify nonnegative support rate, the output family,
  unchanged function suprema and the limits of support relabeling.
- B-MATCH now separates the empty-support prefactor from its supported
  boundary-log estimate.
- B27's uniform natural-width cost now requires fixed rho and `t>=1`.
- B-JOINT now makes the coefficient extension's empty term, readers,
  factorization, holomorphy and envelope premises explicit.
- B30 now requires `r_j<1` for its geometric-sum formula.
- B-ITER now states nonnegative majorants and positive B,M; its
  feasibility sentence fixes the contraction margin and bounds B,C.
- The comparison table distinguishes the linear critical-prefactor
  alternative from the failed fixed-size sublinear majorant.

These changes were made by the author and rechecked in the final
SHA256-identified file. No commit was made or requested. Their acceptance
does not discharge the OPEN model constructions in item 10.

The note can land as an honest research result: it establishes exact
bookkeeping, fresh-event pricing at the stated real-law scope, a
conditional geometric branch, and sufficient renewal/connected-expansion
contracts. The actual matched boundary-return lemma remains OPEN.

VERDICT: LAND
