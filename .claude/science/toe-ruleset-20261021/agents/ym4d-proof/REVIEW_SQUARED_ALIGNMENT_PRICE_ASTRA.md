# Independent review of the recovered linear threshold and bare energy allocation

**VERDICT: LAND**, solely as the bounded finite-lattice, one-bare-step result
stated in [the source](SQUARED_ALIGNMENT_PRICE_ASTRA.md). There are no blocking
findings and no required source fixes. The squared alignment lemma and exact
linear threshold are recovered existing results; the useful synthesis is the
explicit simultaneous coarse-plaquette allocation with complete original
readers. Full SU(N), d=4 continuum existence and the physical mass gap remain
**OPEN**.

## Source identity and independent-input boundary

The complete reviewed source has 398 lines, 20,270 bytes, SHA256
`cd2df445d61018ade1f4050612b0616800f4c87c83cea9de27d3ab7b8ac00905`.
The invocation was configured as `gpt-6-astra`, `reasoning_effort=max`,
`fork_turns=none`, according to the coordinator's dispatch. This is configuration
reporting, not backend attestation. This is a same-family, fresh-context hostile
review. It does not claim cross-family independence.

The complete target and necessary actual CS/CB/OC/JMBRB/LFPRICE/RENEW inputs
were read before opening the target author packet. The full independent
derivations were first frozen in the distinct, immutable
[pre-packet findings snapshot](checks/review_squared_alignment_price_prepacket_findings.md),
SHA256 `325f1c9ede4e3087d1c5236537018c5972fccd1699677c27b95b06df694bc687`.
That hash names the snapshot path, **not this final review**. The corresponding
[actual-read manifest](checks/review_squared_alignment_price_reads.json),
SHA256 `395aca8915331cc11406482fece96fe92fcc81d4a071d37c1a66c663e742744d`,
records complete/partial coverage and full input identities. Whole-file hashes
do not pretend that unrelated chapters were read.

[REVIEW55_ARS r55a-F10](REVIEW55_ARS.md) and
[CODEX_REVIEW_KN F4](CODEX_REVIEW_KN.md) are necessary mathematical inputs to the
recovery/novelty question. Their trace-difference arguments were inspected
before freezing. Their verdicts were not used as proof. The coordinator later
raised the coordinate-origin question examined below; its favorable impression
of other constants was not used to determine the result.

## Mathematical findings

**Alignment and exact threshold — confirmed.** At source lines 94–114,
the normalized real Hilbert inner product gives
`<S-V,S>_n=|S-V|_n^2/2`. Since S is an admissible SU(N) competitor and
`|M-S|_n<=sqrt(q)`,

    psi_M(V)>=d^2/2-d sqrt(q)>=d^2/4-q.

The last difference is `(d/2-sqrt(q))^2`. No invertibility, polar maximizer or
uniqueness assumption is hidden. This is CS10 rearranged. The intermediate
bound gives `psi>=d^2/4` when `sqrt(q)<=d/4`.

For a coarse defect at least epsilon, the smooth square contributes at most
`L^2 eta<=epsilon/2`, leaving some link with operator mismatch at least
`epsilon/8`. Its normalized HS mismatch is at least `epsilon/(8 sqrt(N))`.
The ribbon bound `sqrt(q)<=A_L eta` therefore proves the exact threshold

    eta=min{epsilon/(2L^2),epsilon/(32 sqrt(N) A_L)},
    psi>=epsilon^2/(256N).

This checks SAP9–10, including strict/non-strict cases and every N factor.
The same threshold and gap are already explicitly derived in r55a-F10.
The source honestly distinguishes this recovery from JMBRB B15–B18's weaker
separate-error estimate. The rough-input alternative is an original Wilson
action charge, not a forward kernel probability.

**Actual paired geometry and every original reader — confirmed.** At lines
118–207, adjoining one transverse edge of the axial path changes the leg by
an ordered L-plaquette strip; a parallel edge cancels by backtracking. Both
signs work and no matrix factors commute. There are at most 3h transverse
edges, giving `A_L=3Lh`. Telescoping and Cauchy–Schwarz pay every repeated
plaquette occurrence before the unique-label Wilson sum is formed.

The three incidence bounds are distinct and valid: a fine plaquette lies in
at most one root square; a positive coarse edge belongs to six coarse
plaquette labels; a fine plaquette belongs to at most eight labelled bricks.
At T=2, the opposite face labels are distinct and each lifted brick omits the
other periodic seam. A torus-induced two-block graph would be the wrong
object. The source uses the correct lift. The resulting membership bound
`1+6*8=49` is valid.

All complete kernel words, their normalizers, their coarse links, all fine
links in the square/brick plaquettes and every corresponding original source
coefficient are retained. The four endpoint blocks contain at most
`4L^4|A|` fine vertices, proving the `24L^4|A|` plaquette-reader and
`16L^4|A|` positive-link-reader bounds. These are not independence or
integration-variable counts. Nothing replaces the full history readers by a
coarse geometric shadow.

**Coordinate-origin clarification — nonblocking.** The centered CS/CB/SAP
convention matches RENEW's earlier offset convention by the single translation
`a=(h,h,h,h)`:

    U_center(x,mu)=U_offset(x+a,mu),
    e_center(x;mu,nu)=e_offset(x+a;mu,nu),
    V_center(X,mu)=V_offset(X,mu).

It sends blocks, roots, signed path words, plaquette/source labels, cuts and
brick/square readers bijectively to their counterparts; product Haar and all
normalizers are identical. The source does not display this relabeling, but
its definitions determine it. This is an optional clarity addition, not a
mathematical defect. Translating only U while freezing the old source-label
assignment would not be the same source-dependent model.

**Forward normalization and aggregate constants — confirmed.** SAP11's grid
cover has cell HS diameter at most `r/sqrt(2)` in `2N^2` real coordinates.
Bi-invariance of probability Haar and the 1-Lipschitz normalized trace give
the displayed lower bound on the *actual* centered normalizer for t>=1.
The `4^|A|` union bound and at least `|A|/6` distinct witness links give
SAP12–13 only under the stated smooth-input plain product kernel. No
independence of coarse plaquettes or future-conditioned outputs is used.

For SAP15, the per-plaquette five-term inequality followed by SAP6 gives

    |I-V_P|_n^2<=10L^2 sum_Sigma(P) s
                    +20 sum_boundary(P) psi
                    +40 A_L^2 sum_boundary(P) sum_brick(c) s.

Summing with the one/six/eight incidences gives exactly
`C_F=10L^2+1920 A_L^2` and `C_psi=120`. With
`c_SAP=min{(1-rho)/C_F,kappa_-/120}`, positivity proves
`E_A^e>=c_SAP sum_A |I-V_P|_n^2`, hence
`E_A^e>=c_SAP epsilon^2 |A|/N` on simultaneous badness. Overlapping
plaquettes are covered; A itself consists of distinct labels. Empty A,
singular means and winding fields cause no exception.

**Exact raw allocation and its open consumer — confirmed.** SAP18–19 retain
every original `Ntilde_(kappa u)(M_c)^(-1)`. Reducing selected numerator
exponents by theta does not replace t in any denominator. Their remainder
has nonnegative uncharged energy but may retain the full exterior dependence.
The ratio R/w has the stated finite reader set; the integrated remainder
does not thereby become a local activity. Cuts and nonnegative H remain on
both sides, and complex original sources give an absolute envelope only.
The same specified Z_ref divides both sides; its remaining ratio is
explicitly unestimated. Shared action cannot be spent again at a later step.

LFPRICE section 6 clause 2 still requires the joint remaining-reference
estimate with actual all-cut normalization. Its clauses 3–5, RENEW-MATCH,
effective-density coercivity and multilevel renewal are not proved. RENEW's
actual rough flux orbit has rough maximizing outputs with zero fresh gap,
and its open tubes persist at the stated finite-horizon scope. SAP15 charges
the original fine action and is compatible with that example. It neither
reprices inherited histories nor substitutes a bare law at an effective level.

The source's u is the displayed CS/JMBRB Wilson convention. It explicitly
does not identify this with PROOF's separate `beta=2N/g^2` convention.
No extra 2N, physical coupling identification or new framework primitive is
being supplied by this review. The model remains explicitly supplied
mathematical data. Bałaban and Dimock are credited; external literature is
not carrying an unrebuilt proof step.

## Packet inspection and final disposition

After the independent freeze, the four target author metadata/check files
were read in full. Their source/packet bindings, all 16 author input pins,
and eight local source links match current bytes. The
[post-packet check](checks/review_squared_alignment_price_postpacket.json)
has SHA256 `2d362c002cb8e0baf5aceda8eca7326984aeea6ad368810ed491367bc936eeb0`.
No mathematical finding changed after that inspection. The author checks
properly label themselves reconstruction and provenance rather than independent
review. Their hashes do not establish any theorem.

One review iteration; zero blocking findings; zero source fixes; one optional
coordinate/source-label clarification. Proof obligations are closed for
SAP1–SAP19 at the stated supplied-model scope. No broader theorem is certified.
No scientific numerics, extra workers, source edits, Git mutations, PR/front
updates or audit/ledger operations were performed. Current-main integration,
source-preservation and combined repository gates remain with the coordinator;
this is a bounded source verdict, not an assertion that those gates ran.

VERDICT: LAND
