# Independent mathematical review of CHARGE

The new real extensive-sector estimates and the bare-action saddle calculation
survive independent written checks. Three narrow corrections are required in
the proposed renewal framework: its uniform contraction constant, the
orientation of the creation-map sum, and the object whose nonvanishing a
polymer expansion establishes. These are corrections to the formulation of
still-open work; they do not refute the positive charging estimates or prove
failure of the soft route.

## Identity, independence and limits

- Candidate: `CHARGE.md`, 630 lines, SHA256
  `c73a3bda6e32392fb68fcc9094bdaddb260d77206248a29df14afc636a73e8ea`.
  It is byte-identical to `checks/charge_review_base.md`. All line references
  below refer to this frozen candidate.
- Worktree HEAD: `114cc809e9eca45a98dd0932b133457fa1f60ede`; local
  `origin/main`: `01589af3faf806b736c42dc2f3bd625e9edead9f`.
  All 20 entries in `checks/charge_sources.json` matched their recorded
  hashes. Remote freshness remains unverified: the recorded fetch could not
  write FETCH_HEAD. This review does not claim current remote-main coverage.
- This is a same-family, context-separated Codex review, not a cross-family
  review or formal retained-status audit. The reviewer did not author the
  candidate. The initial input was the bounded review brief and source
  identities. After preliminary findings were sent to the author, the author
  also highlighted the N2 circularity risk; F3 below was independently checked,
  but that item is not blind with respect to the author's alert.
- Applied the repository-local physics-claim-reviewer procedure and its
  focused-review/proof-obligation references at the identified local revision.
  Applied no-go discipline to the scoped negative statements. PROCESS_LIGHT's
  review requirement is honored; the explicit author allowlist takes
  precedence over the review brief's incompatible `REVIEW_CHARGE.md` path.
- No numerical computation, simulation, numerical runner, priority workaround,
  or further delegation was used. The recorded nice-priority denial remains
  decisive. Independent evidence below consists of written derivations;
  deterministic source hashes are provenance, not mathematical tests.
- The only file written by this reviewer is `checks/charge_review.md`.
  No source, prompt, audit, ledger or platform instruction was changed, and
  no commit was made.

## Binding findings

### F1 — make the window margin explicitly uniform

**FORMULATION FIX / PROOF OBLIGATION — lines 490–507, especially C24.**
The text introduces a constant `theta<1`, but C24 never bounds its window
by that theta. Its middle line ends only in a strict `<1`. The subsequent
`m B_0/(1-theta)` conclusion requires a single nonnegative theta below one
uniformly over starting level, volume, depth, admitted history and domain.

This distinction matters. On one-dimensional normed spaces take
`C_j=(j+1)/(j+2)`, `m=1`, and `S_j=0`. Every one-step norm is strictly below
one and the empty-prefix bound is one, but

    |C_(j+r-1)...C_j|=(j+1)/(j+r+1),

whose sum over r diverges. Thus pointwise strict inequality cannot be the
antecedent of the stated geometric estimate. This is an abstract diagnostic,
not a counterexample to the proposed Yang–Mills construction.

**Required fix:** write the middle condition explicitly as

    ||C_(j+m-1)^irr...C_j^irr||
      <= theta_coh + sum_l b_l exp(-q_l) <= theta < 1,
    0 <= theta < 1,

with the indicated bounds uniform in all claimed parameters. Alternatively
take the supremum over those parameters before comparing to theta. The
existing OPEN status should remain. No new analytic proof is required merely
to correct this sufficient-condition statement.

### F2 — a per-birth lifetime sum is not a fixed-terminal accumulation bound

**SCOPE FIX / PROOF OBLIGATION — lines 509–521 and its use at 544, 553, 617.**
C25 is a meaningful proposed estimate: for each birth index j it bounds the
sum over all future lifetimes r. Uniformity in j does not, by itself, bound
the contribution of all different birth indices at a single output level k.
The phrase “asks only” and its presentation as an alternative for next-step
closure need this distinction stated explicitly. The separate nonlinear
closure requirement is correctly retained, but it does not convert C25 into
the missing linear accumulation estimate by algebra.

Here is a written scalar diagnostic with uniformly bounded one-step maps.
Partition the nonnegative time indices into consecutive finite intervals
`[a_n,b_n]` of unbounded lengths. Set

    C_j=2 for a_n<=j<b_n,    C_(b_n)=0,
    A_j=2^(-(b_n-j)) for a_n<=j<=b_n.

For each birth j in that interval, its product at lifetime r is
`2^(r-(b_n-j))` for `0<=r<=b_n-j`, and is zero afterward. Hence its C25
sum is less than two, uniformly in j. At terminal time `b_n`, however,
every birth in that interval contributes exactly one. The sum over births
is `b_n-a_n+1`, which is unbounded. This distinguishes the two quantifiers
without any numerical experiment or claim about the actual SU(N) maps.

**Required fix:** label C25 as a per-birth forward lifetime estimate and,
where it is proposed for fixed-output closure, retain an additional open
estimate such as

    sup_k sum_(j<=k) ||C_(k-1)^irr...C_j^irr A_j|| < infinity,

in the same output norm, or require a common summable lifetime envelope
`||C_(j+r-1)^irr...C_j^irr A_j||<=a_r`, with `sum_r a_r<infinity`
uniformly in j and all other parameters. The stronger example at lines
516–518, `a_r=B^r exp[-lambda b^r]`, would control both sums if established
with uniform B and positive lambda. Preserve that useful example and its
OPEN actual-model status. Returned sectors and nonlinear invariance still
need their already named separate estimates.

### F3 — identify the reference before using a gas logarithm to prove its existence

**REFERENCE/CIRCULARITY FIX — lines 576–582, especially 578–580.**
The asserted implication from J and C26 to “the reference logarithm and hence
that part of Z” does not identify which exact object has a gas representation.
J is C14's matched complex integral, and those matched objects may already
contain division by the actual `Z_A`. A convergent expansion for a normalized
gas or for `R_h/Z_A` proves a logarithm/nonvanishing for that represented
object. It does not thereby prove nonvanishing of the base `Z_A` used to
define it. For the elementary analytic pair `R(z)=Z(z)=z`, the quotient on
the punctured domain extends as the nonzero function one, while Z still
vanishes at zero. This is an object/logic diagnostic, not a claimed Wilson
partition-function zero.

JMBRA lines 244–260 require an exact representation, coefficient
factorization, the complete mixed integral bound, holomorphic data, fixed
selectors and integration envelopes. Lines 303–310 prove nonvanishing of
that gas and explicitly do not instantiate the result on the denominator
in A2. C26 alone cannot omit these prerequisites or change the represented
object.

**Required fix:** say that J/C26 can construct the logarithm of the exact gas
to which all those hypotheses apply. To establish actual `Z_A` nonvanishing
this way, require a separate exact pre-normalization representation
`Z_A=P_A G_A` with a known nonzero prefactor and bounds proved without
division by the unknown `Z_A`. Otherwise keep actual base-reference
nonvanishing as an open antecedent. Local total-variation control also
remains quantitative work; mere nonvanishing is insufficient. This clarifies
the existing OPEN clause 3 rather than adding an independent obstacle count.

## Per-item disposition

| Candidate item and lines | Verdict | Fix or retained limitation |
|---|---|---|
| Fixed model, original density and flux orbit, 36–92 | CONFIRMED | No binding fix. The density is inherited, Haar is normalized, and N is fixed when constants are used. |
| Geometric credits and history entropy, 96–151, C5–C8 | CONFIRMED | Raw all-terminal-integrated scope only; no arbitrary localized-defect estimate follows. |
| Actual real all-cut comparison, 153–193, C9 | CONFIRMED | Both terminal kernel debits and the global cap entropy are retained. |
| Coupling/cut conditions and depth bound, 195–217, C10–C11 | CONFIRMED CONDITIONAL RESULT | Keep the supplied ordering `u_*<=u_j<=u_0`, lower cut bound and finite omitted levels. No flow theorem is supplied. |
| Filled-volume summability and local remainder, 219–266, C12–C14 | CONFIRMED / OPEN AS LABELED | The summable family grows its original charged volume with depth; C13 is failure of a sufficient local majorant, not a divergence lower bound. |
| Flat torons, periodic topology and twisted route, 270–304 | CONFIRMED | No gauge equivalence to a flat toron and no disconnected unrestricted-link component are shown correctly; admissibility-sector topology remains outside scope. |
| Bare Wilson saddle and BFT restrictions, 306–355 | CONFIRMED | The full fixed-output soft Hessian remains uncomputed. BFT is used only to check hypotheses, not as an arbitrary-background theorem. |
| Sector splitting/translation, 357–393 | CONFIRMED algebra / ARGUED application | No sector mass is reusable after conditioning; the non-Gaussian/extracted estimates remain open. |
| Fixed-terminal first return, relative transfer and reader integration, 397–451 | CONFIRMED finite real algebra | Future full transfers and both endpoint reference multipliers must stay. No locality or complex norm estimate follows. |
| Forward gap, future tilt and scalar creation price, 453–486 | CONFIRMED diagnostic | The forward cap price is not a matched all-cut norm estimate; fixed-horizon weak-coupling persistence is the correct limit. |
| Finite-window criterion, 490–507 | FIX REQUIRED | F1: bind the displayed window sum to one uniform theta. |
| Creation-map alternative, 509–521 | FIX REQUIRED | F2: distinguish the lifetime sum from accumulation at a common terminal level. |
| Mixed budget and invariant scalar arithmetic, 523–535 | CONFIRMED as conditional requirements | Complete coefficient-weighted mixed bounds, exact factorization, analytic hypotheses, nonnegative recurrence constants and actual invariant inputs remain required. |
| Clause table and soft/hard recommendation, 537–565 | CONFIRMED OPEN/ARGUED classification, subject to F2 | No closure of clauses 2–5, no reason to assert failure after charging, and no universal hard/soft comparison is proved. |
| N1–N8 scope, 567–625 | HONEST PARTIAL SCOPE, with F3 REQUIRED | No five-route or exhaustion-certificate PASS; correct the reference-log implication in N2. |
| Resource/provenance statements, 627–630 | CONFIRMED within recorded limits | No numerics ran; this report supplies a written independent check, not audit authority. |

## Independent load-bearing derivations

1. **Flux mean and maximizer.** Work directly with the parity exponents of
   g. In direction 1, translation of the return axial leg by `L e_1`
   leaves its fine links unchanged, so the axial factors cancel and the
   central leg has exponent `X_2+r_2+a`. In direction 2 the translated
   axial leg changes every direction-1 factor by g; the signed count is
   `r_1-(L-1)/2`. The direction-2 central leg supplies d. These facts hold
   for every coordinate ordering because all template factors commute.
   Odd L gives one more even than odd offset, yielding exactly C4's means.
   For `M=WP`, let `A=W*V`. Then
   `tr P-Re tr(A*P)=sum_i p_i(1-Re A_ii)`, with each summand nonnegative.
   Equality forces every diagonal entry to be one and hence A=I by
   unitarity. Expanding the squared trace also gives the exact identity at
   candidate line 86.
   Thus the mean maximizer is unique, and it retains g plaquette curvature.
   A point maximum is not a probability. The additional RENEW tube argument
   uses a finite contour Lipschitz constant, recursively shrinking radii,
   the cap gap bound and a finite union bound. Its limit is at fixed finite
   horizon and lattice, as CHARGE states.

2. **Raw reserve and entropy.** If every link changes by at most delta,
   four-factor telescoping changes each plaquette by at most `4 delta`.
   The n_0 original 12 plaquettes therefore each have operator defect at
   least `2-4 delta`. The exact identity
   `2N s(U)=||I-U||HS^2>=||I-U||op^2` gives C5. Positivity of all remaining
   plaquette energies is essential. The geometric fractions in C6 sum to
   `1-b^(-(R+1))`, so the reserve is allocated at most once and its level-l
   credit equals a constant times `u_0 n_l`. For C8, first use the bound
   on each w_h and `sum_h I_h=1`; split
   `e^(-S_0)=e^(-theta S_0)e^(-(1-theta)S_0)`. C5 bounds the first factor,
   while the second factor integrates to at most one after reverse-time
   kernel integration. Finally `sum_l n_l<=n_0/(1-b^(-1))`. No factor
   counting the physical partition labels is introduced. This also covers
   theta=1 and R=0. The fixed B bill is affordable under the stated
   sufficient inequality. Neither proof refreshes action at a coarse level.

3. **Actual denominator comparison.** Trace duality and `||M||op<=1` give
   `|h_M|<=1`, hence `e^(-2t)<=k_t<=e^(2t)`. There are `4 n_(j+1)` last
   output links. Removing just their upper envelope leaves earlier
   normalized kernels, so
   `R_(E,j)<=exp[-c_delta u_0 n_0+8 kappa u_j n_(j+1)]`.
   An entry-coordinate cell of side `zeta/(2N)` has Hilbert–Schmidt
   diameter at most `zeta/sqrt(2)`; occupied-cell representatives give
   a cover by at most `(1+4N/zeta)^(2N^2)` equal-mass Haar balls. Thus the
   product cap over `4 n_j` links costs at most
   `8N^2 n_j log(1+4N/zeta)`. Every retained interior plaquette passes
   because `4zeta<epsilon_j`. Its energy is at most `8zeta^2`, so all
   `6 n_j` plaquettes cost at most `48u_j zeta^2 n_j`. The denominator
   retains the lower envelope of all last kernels. Division therefore
   costs `16 kappa u_j n_(j+1)`, exactly C9, not half that amount.
   This is the actual bare level-j all-cut denominator, not the normalized
   Wilson law or a conditioned history mass.

4. **Depth uniformity and its scope.** With `zeta=u_j^(-1/2)`, the two
   positive terms in the exponent of C9, divided by `u_0 n_0`, are bounded
   by

       b^(-j) sup_(u>=u_*) [48+8N^2 log(1+4N sqrt(u))]/u
       and 16 kappa b^(-(j+1)),

   using `u_j/u_0<=1`. C10 bounds each by `c_delta/4`. The supremum of
   the first ratio tends to zero as u_* grows, and the kernel term is
   made small by j_*. The cut hypothesis implies `4zeta<epsilon_j`.
   This proves C11 precisely on its declared range. For fixed terminal
   volume `n_R`, the original volume is `b^R n_R`; the ratio of successive
   C12 terms tends to zero. The estimate uniformly dominates `n_R>=1`.
   It compares different compatible finite lattices and does not take
   an infinite-time persistence limit. The local numerator analogue
   leaves `-tau m+d_j n_j`, so the displayed global comparison cannot
   certify a local full-support price when `n_j/m` grows.

5. **Saddle and topology.** Along C15 the plaquette phase is
   `-pi+2eta(-1)^x_2` modulo `2pi`, including the seam because T_2 is
   even. Taking the two nontrivial eigenvalues gives C16 and second
   derivative `-8u n/N`. For an arbitrary link tangent the first
   variation of a plaquette is `i B P` after cyclic transport, with B
   Hermitian and P equal to I or g, hence Hermitian. Its trace has zero
   real derivative. Thus the background is critical for all variations.
   A single direction-1 link meets two g plaquettes and four identity
   plaquettes. Their energy changes are respectively
   `-2(1-cos eta)/N` and `+2(1-cos eta)/N`, giving C17 and positive
   second derivative `4u/N`. A gauge tangent at a critical point cannot
   have the nonzero negative Hessian value found above. The bare Hessian
   is therefore indefinite, with no inference about the additional
   fixed-output soft terms. Separately, even cycle lengths make every
   cycle holonomy and plane product trivial, while local g curvature
   remains nontrivial under conjugation. The explicit path to identity
   is a legitimate periodic link assignment even though its seam
   plaquettes cease to be uniform along the path.

6. **Exact transfer and normalization.** Expand the noncommuting product
   `T_(j+R-1)...T_j` using `T_l=C_hat_l+S_hat_l`, classify each word by
   its earliest S, and leave all subsequent choices summed into T.
   This proves lines 413–415, including the empty-product cases. Omitting
   the future T factors would describe stopped outputs at different
   times, not the fixed-terminal law. Conjugating each transfer by its
   positive input and output reference multiplication operators telescopes
   only the internal multipliers, giving C20 with both endpoints intact.
   The replacement identity C21 follows by integrating old good
   interiors first, canceling their actual C_Y masses, and summing the
   disjoint good/bad choices. Fubini elimination multiplies all readers
   of a variable before integrating. Only a genuinely unread output of
   a normalized creator integrates to one; fixed-terminal kernels and
   Wilson/history factors remain integrands. None of this makes nu_A
   a product law.

7. **Gap and tilt.** For t>=1, the 1/t ball about a maximum has
   `h_M>=max h_M-1/t`. Its mass lower bound therefore gives
   `int exp(-t psi)>=e^(-1)(1+4Nt)^(-2N^2)`. The event numerator is at
   most `e^(-t a)`, which yields C22. Conditional multiplication for
   distinct past-adapted outputs uses backward iterated expectation;
   it does not permit a future condition to be erased. Bayes' formula
   with future weight H gives C23, and H=1_E makes the tilted event
   certain. Homogeneity cancels a scalar creation epsilon from an
   operator ratio. These facts establish exactly the diagnostics stated,
   not a negative theorem about weighted or extracted renewal.

8. **Conditional cluster and invariant arithmetic.** Under JMBRA's exact
   mixed representation, selected labels partition uniquely into complete
   overlap components, so disjoint joint integrals factor into a polymer
   gas. The absolute product bound must hold on every component, including
   its coefficient and local total variations. With
   `v_i=e^((mu+1)|H_i|)alpha_i` and
   `b_i=e^((mu+2)|H_i|)alpha_i`, the overlap sum is at most `Q|H_i|`.
   Thus b_i dominates the positive rooted-tree recursion. A second
   connected-graph/tree bound spends the other support exponent and
   yields the logarithm under the exact analytic prerequisites. This
   verifies the source criterion, not its instantiation on CHARGE's
   references; F3 preserves that distinction. For the scalar invariant
   estimate, `C x^2<=CMx` on `0<=x<=M`, with nonnegative C,e and a norm
   majorant theta, proves the stated sufficient bound on x'. Relevant
   coefficients and actual invariant-domain estimates are separate.

## Source checks and negative-claim scope

The full candidate was read. Necessary arguments were checked directly in
RENEW 1–290 and 338–559; REVIEW_RENEW 65–145 and 170–248; JMBRA 25–225,
239–454 and 564–622; JMBRB 126–227, 319–377 and 595–686; LFPRICE 202–237
and 654–708; RD3 98–168, 306–423 and 559–588; and RD4 25–75, 336–461
and 521–574. The author log was read in full. Source hashes do not stand
in for reading, and no full recertification of the predecessor packages
is claimed.

The BFT scope checks used BFT_A 20–48, 129–172 and 210–274; BFT_B 72–102,
4313–4360, 4565–4625 and 4750–4782; and REVIEW_BFT_B_S9_S10 385–410.
The actual inequalities require small curvature/global or controlled local
frames, their slice/inverse hypotheses, and additional unproved transport
inputs. C4's plaquette distance two is not covered. CHARGE appropriately
does not rely on the late BFT author's broader status labels as proof.

The located existence file was checked at 3193–3228, 3437–3453,
3523–3556 and 3623–3650. It concerns flat toron moduli, conditional
fixed-torus Polyakov estimates, and an explicitly argued changed twisted
problem. None prices the nonflat C4 family. SOFTHARD's operative comparison,
G1/G2, and HRT status/closure statements were checked at 27–45, 69–148,
285–300, 502–534 and 622–651, with truncated load-bearing passages reread
in smaller slices. Its smoothing is a raw-integral result and its hard
return remains open. Hardening to this same unique maximizing map preserves
the exhibited rough orbit by the directly checked mean calculation.

The two primary abstracts independently confirm the limited attribution:
Dimock's exposition of Balaban's method treats scalar phi^4 in dimension
three, not a supplied four-dimensional gauge theorem
([Large fields](https://arxiv.org/abs/1212.5562),
[Convergence](https://arxiv.org/abs/1304.0705)). No external analytic lemma
is used as a proof leaf here.

No-go discipline disposition: N1 honestly records three actual route
families and leaves alternatives live, so it is not a five-route packet
PASS or an exhaustion certificate. N2 correctly avoids an independent-wall
count but needs F3. N3 retains the supplied model, extensive geometry,
coupling ordering and cut conditions; no framework primitive is used to
close an analytic estimate. N4 matches the earlier witnesses to their real
scopes: RENEW concerns forward input-uniform return, B-MASS concerns
unchanged positive mass, and the saddle concerns only the bare action.
N5 keeps link, mode, tower and lattice-wide claims distinct. N6/N7 retain
sector integration, matched references, weighted norms, extraction and
charged-ancestor mechanisms without calling them new axioms. N8 preserves
the earlier normalization, reader and background corrections; no universal
novelty or all-route search is inferred. These scope checks do not claim
formal negative-packet compliance or audit status.

## Binding disposition

Apply F1, F2 and F3 in place and submit the exact changed candidate for
affected-fix confirmation. No repair to C5–C12, C16–C17 or the fixed-terminal
first-return identity is required by this review. Keep R1 general renewal,
R2 renewal estimates, R3 and LF-JMBR clauses 2–5 OPEN. The report holds
readiness only for the three identified formulation/logic corrections,
not because those explicitly open scientific obligations remain unsolved.

VERDICT: HOLD

## Affected-fix confirmation of the revised candidate

**All three binding findings are resolved.** This confirmation applies only to
the revised `CHARGE.md`, 650 lines, SHA256
`8c5a5ecdb95a32089f2005bf6597d4aedefa660b9b9f8c1cc7b7a01374afc1ef`.
The initial HOLD above remains the record for the original 630-line candidate.

The reviewer read every changed passage and its affected context, including
the complete revised section 4.3, clause table, recommendation and N2/N7
statements. Deterministic regeneration confirms that
`checks/charge_revision.diff` is the complete actual delta from
`checks/charge_review_base.md`; the diff SHA256 is
`23e7da05ea232ed12fab9214cf5ba9a54cb88c9b097ae59982a0d865059c092e`.
Candidate lines 1–489 are byte-identical to the original reviewed version.
All 20 manifest source hashes still match, so the independent checks of
unchanged proofs and the source prerequisites above remain applicable.

| Finding / affected revised lines | Confirmation |
|---|---|
| F1, 490–509 | RESOLVED. C24 now requires one `0<=theta<1`, explicitly bounds the complete window majorant by it, and quantifies uniformity in starting level, volume, remaining depth, admitted history and D_*. The text expressly distinguishes this from a pointwise strict bound. |
| F2, 511–533; dependent uses 556, 561–569, 632–639 | RESOLVED. C25 is labeled per-birth lifetime control. C25a separately requires fixed-terminal accumulation. A common summable envelope is a sufficient condition for both; all actual-model estimates, returned-sector estimates and nonlinear closure remain open. The clause table, recommendation and counter-route now carry both sums. |
| F3, 589–602; clause 3 at 554 | RESOLVED. The gas logarithm is assigned only to its represented object. Actual base-reference nonvanishing remains an open antecedent unless a separately controlled pre-normalization representation with a known nonzero prefactor is supplied. The local-TV requirement is not inferred from mere nonvanishing. |
| Scalar invariance clarification, 543–547 | CONFIRMED. The added `C,e>=0` and `0<=x<=M` make the elementary majorant's sign and interval hypotheses explicit; its analytic inputs and relevant/marginal recursions remain unproved. |

The affected implications were checked directly. For C24, split an ordered
length-r product with `r=qm+s`, `0<=s<m`, into q adjacent windows and one
remaining prefix. Uniformity in the starting index and submultiplicativity
give `B_0 theta^q`; summing q and s gives `m B_0/(1-theta)`. For the common
creation envelope, the per-birth bound is its direct sum, while at terminal k
the reindexing `r=k-j` bounds the sum over births by the same complete
envelope sum. These are different sums with one sufficient common bound,
exactly as the revised text states. For F3, nonvanishing of `P_A G_A`
follows only when both the nonzero prefactor and an independently controlled
nonzero gas representing the actual base reference are supplied; no such
construction is claimed complete. Finally `C x^2<=CMx` gives
`x'<=theta M+CM^2+e<=M` under the displayed invariant-bound hypotheses.

No remaining binding correction was found in this exact revised candidate.
The positive result remains the real extensive-sector charging comparison
under its explicit conditions, together with the stated finite algebra and
bare-action saddle. General matched renewal, its complex/local references,
the actual extracted operator estimates and LF-JMBR clauses 2–5 remain OPEN.
LAND here means readiness of this honestly scoped research note; it grants
no formal audit status, full renewal theorem, existence theorem or mass gap.

The original same-family/context-separation disclosure and remote-freshness
limit remain in force. No numerical computation, source edit, additional
delegation or commit was performed. This review file is still the reviewer's
only modified path.

VERDICT: LAND
