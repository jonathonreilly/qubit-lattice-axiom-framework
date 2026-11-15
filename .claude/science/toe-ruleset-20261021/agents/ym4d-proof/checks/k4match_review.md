# Independent hostile review of K4MATCH

Review date: 2026-10-30 UTC. This is a fresh, separate-context **same-family
review: Codex reviewing Codex**. It is not an independent model-family
check and is not an audit-grade promotion.

Reviewed author document: `K4MATCH.md`, SHA-256
`0c8cc36aab726c9b86e790ca53417f77cde06548bb0706df67ffbf4ef7bb28f6`.
Line locators below refer to that version. I read the author brief,
PROCESS_LIGHT, the criteria, checker, watchdog, all three result files,
resource receipt, source manifest and the necessary source passages.
All 13 source-file hashes in `k4match_sources.json` match the files read.
The current criteria and checker hashes match the successful receipt.
The author applied the two local wording fixes identified below and
added the free-source-radius proof during review. I separately read
those changed passages and bound this final review to that revision.

**Disposition:** the conditional mathematical reduction is sound at its
named-input scope. The requested actual interacting `O(g^2)` sign/size
and perturbative non-cancellation check is **not achieved**. The author
says this honestly. Accordingly, this review does not approve completion
of AUTHOR item 3; its final HOLD is not a claim that the conditional
theorem is false.

## Review method and execution scope

I re-derived the finite cumulant, source, Gaussian-cycle, scale-sum,
Cauchy and perturbation identities below. I did **not** execute new
numerical checks or rerun the author's scripts. Thus there is no new
numerical registration, result or claim of independent numeric
replication. Reading, hashing and metadata inspection do not supply
scientific coefficient evidence. The only file created by this review
is `checks/k4match_review.md`; no author, source, audit or ledger file is
edited and no commit is made. Balaban and Dimock are credited for the
constructive RG method; their work is not used as an unstated estimate.

## Per-item findings

### R1. Observable, Gaussian normalization and fixed tests — PASS

Locators: K4MATCH 22–74; CUMUL 28–49, 173–212, 216–227, 257–322;
TSE55 129–144.

Counting each unoriented plaquette in the two ordered orientations gives
`O(f)=(1/2) sum_p sum_corners f(x) s(U_p)`. With
`tr(t^a t^b)=delta_ab/2` and `U=exp(i sqrt(2N) B^a t^a)`, the quadratic
term of `s` is `(1/2) sum_a(dB)^2`. The insertion weight is therefore
`w_f=(1/4)sum_corners f`, while the quadratic action has coefficient
`u/2`. These factors agree with the stated `u=2N/g_std^2`; no missing
`2N`, clover factor or lattice `a^4` remains.

For coupling-one continuum curvature,
`G(z)=Lambda^2(I-2zz^T/|z|^2)/(pi^2|z|^4)`. Its two-form reflection
matrix has squared trace norm six. Two connected Wick pairings give
the two-point coefficient `12d/pi^4`. Connected pairings of four
quadratic vertices are precisely the three undirected four-cycles,
with `2^4` leg choices per cycle and one colour loop: `16d` per trace.
The point coefficient is `96(1/81+1/256+1/20736)=169/108`, and division
by `12^2` gives `169/15552`, before the overall `1/d`.

I also checked CUMUL's smooth-support argument rather than treating the
point value as the smooth coefficient. Its operator perturbation below
`1/250` yields the trace-product factors `1 +/- 1/60`. Multiplying
`169/108` by `59/60` and `61/60` gives precisely `9971/6480` and
`10309/6480`. The two-point radial bounds give the stated interval
inside `(11,13)`. Hence `3/(338d)<R0<5/(363d)` is valid. The ratio
target alone would not imply absolute matching; the document correctly
uses the stronger two separate matched estimates.

### R2. Fourth conditional cumulant and chain telescoping — PASS

Locators: K4MATCH 107–146; SRC2_55 142–153; SRCCD55 588–604.

The normalized Markov chain supplies
`E[E[O|U_i]|U_(i+1)]=E[O|U_(i+1)]`, even though these individual
sigma-fields need not be nested. Taking differences of ordinary
fourth cumulants and retaining the terminal cumulant telescopes
exactly. In the distinct-source nilpotent ring, expansion of
`log E exp(sum_B c_B z_B)` gives one outer cumulant per set partition.
Their multiplicities are `1,4,3,6,1`; removing the all-singleton
partition leaves exactly the fourteen terms in (5), with no factorial
and no positivity inference. The Gaussian variance-mixture example
correctly gives `3 Var(T)=3` while the conditional fourth cumulants
vanish. This example is used only to expose an invalid algebraic
omission, not as a separated-YM model.

### R3. Source recursion and information beyond two insertions — PASS
after scope correction

Locators: K4MATCH 150–187; SRC2_55 138–153, 198–228, 306–343;
SRCAN55 198–239; SRCCD55 588–604.

The sign and factor of the coupling-field shift in (6) are correct.
Holding all transition kernels and their normalizers fixed gives the
claimed conditional source-log recursion. Applying the same partition
expansion gives (7) and its 15 nonempty subset jets. The document
correctly distinguishes those source jets from the conditional
cumulants of first images in (5). In `P_t`, summing any unrepresented
sign variable annihilates the four-sign perturbation; all proper-subset
moments agree and the fourth cumulant is `t`. This proves the stated
information-content limitation, without purporting to refute a YM
implication with additional dynamics.

SRC2_55 indeed states an all-n representation and only conditional
upper estimates; it supplies neither relative matching nor an
unconditional quantum source theorem. SA-K is expressly a conditional
tree-level statement. The shared-input classification is accurate.

**B1 — fixed and re-reviewed:** K4MATCH 177–179 now specifies that
the continuum free-curvature reference has vanishing separated third
cumulant, and explicitly excludes an inference that finite-lattice or
conditional triple jets vanish. CUMUL's Hodge-star proof concerns that
continuum kernel. It is not a reason to delete any finite-chain triple
jet. The argument retains those jets, and the corrected scope is sound.

### R4. Mixed-slice Gaussian reference — PASS

Locators: K4MATCH 193–214; TSE55 146–166; CUMUL 474–501.

The free slices are positive covariance matrices summing to `P_ex`.
They admit independent Gaussian realizations. Conditioning a quadratic
observable of their sum on the remaining independent tail leaves the
same quadratic form in that tail plus a deterministic contraction.
Constants disappear from the fourth cumulant. The Gaussian
counterparts of the chain increments are consequently exactly
`F4(H_i)-F4(H_(i+1))`. Expanding each four-edge product assigns every
scale tuple to its minimum index, including mixed slices and the
terminal tuple. No same-slice substitution is being made.

### R5. FLOW and LGF transfer, coarse tails and summation — PASS
as a conditional theorem

Locators: K4MATCH 218–302; TSE55 253–309; LGF 42–52, 488–546;
FLOW 418–453.

For fine slices, FLOW gives `u_i>=u-R_F>=u/2` and the cross-support
exponential is summable even after the `L^(4(k-i))` factor. For coarse
slices, up to `floor((u/2-R_F)/b_+)` the same lower bound applies;
beyond that point, `u_i>=u_min` and the geometric spatial factor
absorbs every fixed inverse power of `u`. Applied to the exact inverse
coupling difference, this gives (9), uniformly in the regulator.
The terminal bound has the same coarse envelope.

A four-factor product difference has four terms. Summing three cycles
and their `16d` prefactors gives `192d`; the four weight sums contribute
at most `12^4 a^-16`. The scale identity
`lambda^16 a^-16 L^-16k=1` then gives exactly the power and displayed
constant in (10). LGF's order-two error rescales to
`O(L^-k)+O((lambda/R)^4)` on these separated supports. Bounded smooth
tests and kernel derivatives justify the clover and Riemann errors.
No fourth spatial derivative estimate is required.

For coarse increments, a tail cross-kernel is bounded by
`C L^-4i/u_i`; when `u_i` is below the large-u threshold the same bound
follows by enlarging C using `u_min`. Four factors give the sufficient
exponent 16. Fine increments retain at least one fine cross-edge.
The near/far sum with exponent 16 proves (13) for every fixed `s>0`.
The interacting error (14) is not derived by this reasoning and is
correctly left OPEN. K-dec's upstream coercivity/response assumptions
are consumed as assumptions here, not independently promoted by this
review.

### R6. Projected source norm and Cauchy extraction — PASS conditional,
after source-locator correction

Locators: K4MATCH 308–371; TSE55 365–395.

Inclusion-exclusion in (15) removes exactly monomials missing a source.
Its derivative at multi-index `(1,1,1,1)` is unchanged. Because
`X_r=u lambda^4 O_r`, this derivative of the log difference equals
`u^4(P-P_run)`. Iterated Cauchy contributes the product of inverse
radii and no `4!`, proving (16). A bound on the unprojected difference
costs at most 16 on projection. The quantum logarithmic domain and
uniform projected bound remain explicit sufficient inputs; no
existing upper estimate silently supplies them. The free logarithmic
domain is established by the added proof reviewed below.

**B2 — fixed and re-reviewed:** K4MATCH 362 now attributes the
relative-source notation to TSE55 §4.4(a)/§5.1. TSE55 369 and 387–388
give the radius used here; WITNESS contains no definition of this
relative polydisc. The factor-four discussion is valid as a
triangle-inequality statement in the same specified norm; it is not a
propagation theorem for that norm.

### R7. Conditional matching, limit order and fixed-scale witness — PASS

Locators: K4MATCH 375–409; CUMUL 392–455; WITNESS 474–595.

Either summed (14), Cauchy (16), or the directly assumed PL-4C error
gives a relative fourth error `O(u^-1)+O(u^-theta4)` plus cutoff and
volume errors. PL-1L_Sigma for the actual denominator pair gives the
second-order counterpart. Dividing by the positive A coefficients and
using `u>=U_-(m)` gives (17). Direct expansion of
`(1+delta4)/(1+delta2)^2-1` gives (18).

The limits are correctly ordered: first common-sequence cutoff/volume
limits at fixed m, then short scale. For the fixed-scale witness,
relative errors at most `1/4` give the numerator factor `3/4`,
denominator factors between `3/4` and `5/4`, ratio factor at least
`12/25`, and at most `20/9`. The lower smooth bound then gives
`18/(4225d)`. The positive finite `U_+(m_star)` is essential for the
absolute lower bound and is included. Actual convergence of the seven
centred moments, or all 15 uncentred subset moments, is separately
required. Neither weak convergence alone nor new subsequences are used.

### R8. Formal perturbation identity — PASS as a universal identity;
not an evaluated YM coefficient

Locators: K4MATCH 415–467.

Writing `A(t)=sum t_r X_r1-V1` and `B(t)=sum t_r X_r2-V2`, normalized
logarithmic expansion gives
`h<E A>_t+h^2[<B>_t+kappa_t(A,A)/2]` with the zero-source subtraction.
Differentiation yields precisely the five families in (21): one X2,
two distinct X1, one X1 with V1, one V2, and two V1. The respective
signs and the final factor `1/2` are correct. Parity removes the linear
term for the stated parity-preserving formulation. This finite formal
identity needs no convergent interacting series.

However, no actual `X_r1`, `X_r2`, `V1` or `V2` for the matched YM
scheme is specified or evaluated. In particular `h=g_FLOW,k` is a
matched coupling, while the microscopic Wilson action uses `u_0`;
using `h^-2 sum s(U_p)` to read vertices of the original law requires
the stated matching/counterterm prescription, not an identification
`u_0=u_k`. This is not an error in the universal identity, but prevents
calling it the completed YM one-loop calculation.

### R9. Actual sign, size and perturbative non-cancellation — HOLD / OPEN

Locators: AUTHOR 4–11, especially item 3 at line 9; K4MATCH 3–11,
469–531, 545, 556–562; checker 192–231 and results' scope fields.

The formal ratio correction `a-2b` is correct. The running-factor
ratio and common field-factor cancellation are also exact. They do
not evaluate either the four-point or two-point geometry-dependent
YM insertion coefficient. Signs of insertion terms are not signs of
their joint cumulant integrals. The polynomial controls are expressly
not YM vertices. Consequently no sign of a or `a-2b`, no uniform M4
or M2, and no actual scale threshold follow from the submitted checks.

The bound (24) would imply non-cancellation: its displayed threshold
makes each of its three contributions at most `1/16`, `1/16`, `1/8`,
respectively. But the constants and uniform remainder bound are
assumptions, not results of an interacting check. A formal finite-cutoff
coefficient alone would also be insufficient if its logs grew without
control along the common sequence.

**Binding completion requirement B3:** to mark AUTHOR item 3 achieved,
specify the regulator, gauge/zero-mode prescription, matched coupling
and observable scheme; instantiate all five coefficient families for
these four fixed bumps and the denominator pair; determine the actual
renormalized coefficient's sign and a proved size bound with controlled
cutoff/scale dependence; then apply a concrete non-cancellation
threshold at the stated scales. Keep a perturbative coefficient check
distinct from the still-open nonperturbative remainder. Exact or
rational enclosures are required for any numerical sign decision.
Alternatively retain the present honest incomplete disposition; that
preserves a useful reduction but does not satisfy item 3. Rewording a
generic identity or passing further proxy algebra tests cannot close it.

### R10. Numerical evidence and process — PASS for algebra only

Locators: criteria 1–59; checker 70–111, 122–143, 192–252, 255–289;
watchdog 29–75; K4MATCH 568–581; all three result files.

The 64 assertions decompose into eight free/partition controls, two
slice controls, four perturbative controls, and fifty normalization,
ratio and projection controls. The normalized-moment expansion and
five-family sum exercise distinct order-h bookkeeping, although they
share finite cumulant machinery. The written proofs remain necessary.
Criteria metadata precedes checker and result metadata, and the
recorded hashes agree. The successful receipt records nice 20, all
five thread variables one, the three exclusive numeric locks, load
below 2.01, native free memory 49%, and combined monitored RSS
41,697,280 bytes under the 800 MiB cap. No pools are present.

Both prior attempts have `passed:false`, zero checks and the RSS-limit
exception. They are preserved and reported as failures, not silently
discarded scientific results. The successful run supports its stated
finite algebra scope only. It supplies no interacting coefficient,
uniform analyticity bound, original-law error or moment convergence.

## Free-source refinement added during review — PASS conditional

The author added K4MATCH 326–349 during review, reducing the
**free-reference holomorphy** assumption in (15). I examined the
inserted proof separately. This refinement is sound from the already
named inputs. Let
`G_fine=sum_(i<=k) K_i/u_i` and `G_coarse=sum_(i>k) K_i/u_i`.
Positivity of the slices and their sum `P_ex` give
`G_fine<=2P_ex/u<=2I/u`, hence

    u lambda^4 ||sqrt(W_r) G_fine sqrt(W_r)|| <= 2 ||f_r||_infinity.

For a coarse slice, weighted Schur on the positive-weight support,
using weight vector `sqrt(w_r(p))`, gives

    u lambda^4 ||sqrt(W_r) G_coarse sqrt(W_r)||
      <= 12 M sum_(n>0) (u/u_(k+n)) L^-4n.

The near/far FLOW split bounds this sum uniformly, including the
terminal term. Equality of nonzero spectra transfers the bound to
`u lambda^4 G_run^(1/2) W_r G_run^(1/2)`. Thus sufficiently small fixed
source radii ensure the complex operator
`2 sum_r t_r u lambda^4 G_run^(1/2) W_r G_run^(1/2)` has norm below one.
The finite Gaussian determinant logarithm, defined by its convergent
operator power series, is holomorphic there. Colour multiplicity
changes its trace prefactor, not this radius.

This establishes a free logarithmic domain. It proves neither a
uniform projected log-difference bound nor a quantum source radius,
and it does not evaluate the coefficient required in B3. The inserted
text keeps those limitations explicit and does not change the review's
completion disposition.

## Final disposition

The independent algebra supports the conditional reduction and the
explicit list of remaining fourth-source obligations. B1 and B2 were
fixed and re-reviewed; the added free-radius proof also passes. B3 is
the outstanding scientific deliverable. No unconditional YM
lower-matching, interacting sign,
non-cancellation or full-existence claim is approved by this review.

## Narrow affected-text follow-up

Final manuscript reviewed: `K4MATCH.md`, SHA-256
`2f795c75609075e6d48096abf5ba8572a80f6271a554889f7212c4be75827604`.
This follow-up examines only the two post-review edits; the preceding
item locators remain attached to their stated earlier version.

- **PASS — bare/matched coupling clarification, final lines 415–431.**
  The microscopic action now uses `h_0=u_0^-1/2`, explicitly distinct
  from `h=u_k^-1/2`. Carrying parity to the matched expansion requires
  the supplied effective action, gauge/IR prescription and matching
  counterterms. This resolves R8's notation caution without implying
  that those vertices or a uniform expansion have been produced.
- **PASS — closing review status, final lines 597–607.** The text
  accurately records the conditional pass, overall HOLD, same-family
  disclosure and outstanding B3 coefficient/non-cancellation task.
  The verification JSON link is prospective at this follow-up; this
  review does not certify the contents of that parent-created receipt.

No unchanged science was re-reviewed, no tests were rerun, and no file
other than this review was edited. B3 and the overall verdict remain
unchanged.

VERDICT: HOLD
