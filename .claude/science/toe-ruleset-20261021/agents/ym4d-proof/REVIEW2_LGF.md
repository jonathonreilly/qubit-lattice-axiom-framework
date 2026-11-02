# Second independent hostile review of LGF

2026-10-29. Fresh Codex reviewer context; no authorship of the reviewed work.
This is same-family review, and the required reading exposed the earlier
verdicts. I treated their mathematical assertions and verification claims as
claims to test, not as proof. All paths below are relative to this directory.

**No material defect found in LGF's stated mathematical results or the kernel
input now consumed by Lemma FREE.** The findings below concern provenance and
the evidentiary scope of checks. This conclusion does not certify the rest of
TSE55, interacting Yang–Mills claims, or retained/audit status.

**Findings, ranked by severity**

1. **Low — the consumer quotations and pending-fix language describe an older
   TSE55 revision.** `LGF.md:534–576`, `LGF_LOG.md:108–110`, and
   `REVIEW_LGF.md:304–324` must not be read as descriptions of the current
   consumer. In particular, the quoted `IMPORTED-standard` statement is absent
   from current `TSE55.md:200–228`, and FREE is now at `229–238`, not `202–208`.
   I inspected the actual adoption diff from commit
   `88130072aa683af83562ecc78a64dcc71fe75c4c` and the current arguments. The
   historical quotations match the old text; the adopted inequalities match
   LGF, including both explicit constants and the torus domain. Thus this is
   **not a mathematical consumer mismatch**.
   **Fix:** identify LGF's consumer table explicitly as quotations from the
   old TSE55 hash, and add current consumer locators and adoption provenance
   when maintaining the live documentation. Preserve frozen historical reviews
   as historical records rather than silently rewriting their conclusions.

2. **Low — a copied checksum in the earlier review is malformed.**
   `REVIEW_LGF.md:29` gives a 62-character value for `checks/lgf_criteria.md`.
   The actual SHA-256, also correctly recorded in
   `checks/lgf_review.md:36` and `checks/lgf_source_manifest.json`, is
   `9c1c6fd66a7490d863dbdc08395b456246d12d8c2f3aaedd19b6cf97167e4729`.
   The manifest's value matches the file; the review-table transcription does
   not. This does not change any mathematical premise.
   **Fix:** correct the transcription in a separately authorized provenance
   correction; validate both checksum length and equality when copying receipts.

3. **Informational — some cited numerical gates cannot establish what their
   names might suggest.** At `checks/ts55_1_bubble.py:87–91`, both amplitude
   routes simplify to `S4/32`, with `S4=384` and the clover multiplicity supplied
   literally. The resulting A4 gate at `139–140` must pass with those literals;
   it does not enumerate a clover or test any Green function. At
   `checks/ts55_2_gauss.py:122–127`, G3's coupling-scaling equality is forced by
   homogeneity, although its nonzero condition can fail. The flow checks at
   `checks/ts55_3_flow.py:34–56,67–89` use finite endpoint searches and a
   six-term fine sum. None proves a uniform lattice Green estimate. These
   limitations were already identified in `CODEX_REVIEW_TSE.md:91–98`; code
   inspection independently confirms them.
   **Fix:** retain these as arithmetic/toy checks with their precise scope.
   Use a geometric enumeration if claiming an independent clover-count test.
   Do not use any of their PASS lines as evidence for LGF. LGF's proof does not
   depend on them, so this is not a blocker for LGF.

**Source identity and recovery checkpoint**

The review target is the working snapshot at HEAD
`9658cc870d82401001e56b29f351aec5f5f58fa1`. No remote refresh was performed.
The applicable workflow, reviewer skill, freshness instructions, and proof
governance reference were read and checked against local `origin/main`
`ca2bc7ddf64790da96cd43d42017d000fbfe4808`; their bytes match that ref.
Planning supplied no mathematical premise.

| Source | SHA-256 reviewed |
|---|---|
| LGF.md | `40ea604c79f17027129628bc8b31f5fd6209da21dded864bf45a422dad24505e` |
| LGF_LOG.md | `2619e256dde14d9b4be7657f288d12d0af8b44d7ba9d9cc7418eef0893134382` |
| REVIEW_LGF.md | `d6c9b4f4352bc2693ffdcabfbfa375dfc05dfa584bdd826a6a9afd1ae7ea455b` |
| TSE55.md, current adopted consumer | `a894d1b2439a7b83311175c9e6e30f6fb52cc015a74c6be7e839be8192a7869a` |
| CODEX_REVIEW_TSE.md | `b70b1236e525fe5e3c83cd99b9f7142801a0a215f7e4a34879cdca50917d3edf` |
| LINEAR_PACKAGE.md | `0a2649ff5dbda9963a65ac62770a831d5e9737b9694ea873f28f008496e8e7ad` |

The old TSE55 hash in LGF's manifest is
`d02cc8b265c20da5fc59812a59d68e12d3c9a550d9f9df0890db1c61a38f7340`.
It is historical, not a hash of the current consumer. All other source/artifact
entries in that manifest matched their files. No open mathematical obligation
was identified within LGF's quantified setting. Reopen affected conclusions if
these sources, conventions, domains, or consumer hypotheses change.

**What I re-derived**

1. **Operator, normalization, and Gaussian subtraction** (`LGF.md:14–100`).
   Fourier transformation of the graph operator gives
   `lambda(p)=sum_j(2-2 cos p_j)`, whose quadratic part is `|p|^2`.
   Integrating `(4 pi t)^-2 exp(-r^2/(4t))` using `u=r^2/(4t)` gives
   `Phi=1/(4 pi^2 r^2)`. Removing exactly the discrete zero mode gives
   `Delta G_T=delta_0-T^-4` and counting mean zero. This checks the factor of
   eight against the random-walk operator without importing a random-walk
   asymptotic. Unfolding the integrable Gaussian aliases gives the exact
   Fourier coefficient `f`, hence `E=G-f`. With `delta=q-lambda`, the identity
   `1/lambda=1/q+delta/q^2+delta^2/(q^2 lambda)` gives the error
   `q/360+q/36=11q/360` in (8). The quartic harmonic decomposition is correct;
   signed permutations do not eliminate its anisotropic part.

2. **The derivative ledger and infinite-lattice remainder**
   (`LGF.md:104–214`). I checked the reciprocal induction, mixed-index
   combinatorics, Gaussian derivative polynomial, alias separation, cutoff
   regularity and coefficient bounds. Grouping Leibniz terms by total order
   gives the factors `64 sum_{k>=1}1/(k!128^k)<1` and, away from zero,
   `256 sum_{k>=1}1/(k!512^k)<1`. The product estimates fit inside (9) and
   (14). Eight coordinate integrations give the two shell bounds
   `2^604 rho^(4+m)` and `2^612 rho^(4+m)(rho|x|)^-8`.
   Compact support removes shell boundary terms; periodicity removes outer
   boundary terms at integer x. Summing below and above `rho|x|=1` gives
   `|nabla^alpha E(x)| <= 2^700(1+|x|)^(-4-m)`. The geometric ratios are
   strictly below one for every requested `m=0,1,2`; there is no hidden
   logarithmic endpoint or dependence on the orientation.

3. **Discrete periodization, including the missing zero class**
   (`LGF.md:216–269`). Absolute Fourier convergence holds for each shell;
   finite-grid orthogonality therefore gives its image formula. Continuum
   frequencies `k=T l`, `l!=0`, contribute `+a_*T^-4` to `f_T` at integer
   points, so the sign in `E_T` must be negative. Positive-order differences
   kill this constant. Shells with `rho T<1` have no supported grid frequency
   and sum to `O(T^(-4-m))`. For the other shells,
   `|x+nT| >= 3T|n|/4`, and
   `sum_{n!=0}|n|^-8 <= 80(1+1/4)=100`.
   In particular, `100(4/3)^8<2^10`; the constant in line 260 is sufficient.
   Summing `rho^(m-4)T^-8` gives (20). The order-zero image prescription must
   remain shellwise. For positive orders, the absolute dyadic majorant is
   summable over images and permits the stated interchange.

4. **Uniform heat comparison and all finite-difference stencils**
   (`LGF.md:273–346`). Every oriented difference is an integral of a derivative
   along translated unit intervals. For `T>=4`, even a two-step stencil based
   at `|x|<=T/4` stays within `3T/4`; nonzero images remain at distance at
   least `T|n|/4`. Splitting the heat integral at `T^2` yields
   `T^(-2-m)` at both ends. In (22), the factors `16`, `2^21`, and `2^16`
   give `2^41`; (23) follows by integrating each nonzero Fourier mode.
   This supplies the three distinct corrections `T^-2,T^-3,T^-4`.
   For the infinite-volume comparison I differentiated `r^-2` through order
   four, bounded the displacement error by one further derivative, and checked
   the short heat tail. At `1<=r<4`, the proof uses the finite bound on `G(0)`
   instead of differentiating `Phi` across its singularity. The constants fit
   below the two separate `2^1000` coefficients. Tori with `T<4` have no point
   in the stated domain; the nonempty case `T=4` is covered.

5. **Orbit cancellation and the exact quadratic term**
   (`LGF.md:350–433`). On each orbit, the second moment is isotropic, so the
   Hessian coefficients cancel as `8/4-2=0`. Inversion cancels odd Taylor
   terms. The remaining fourth-order tail is bounded by
   `C|z|^4 T^-6 sum |n|^-6`, and its first two derivatives obey the analogous
   bounds. Third derivatives have an ordinary summable `|n|^-5` tail; the
   heat integral of their absolute values has the same decay. Thus the Fubini
   step in (31) is justified locally uniformly away from sources. All third
   derivatives of `K_T-S_T` vanish, so it is a single quadratic polynomial on
   the connected punctured ball. Symmetry leaves `C_T+b|z|^2`, and the source
   equation forces `-8b=-T^-4`. This proves the positive coefficient
   `b=1/(8T^4)`, not merely its order. Heat scaling and the small-time image
   estimate also give the stated bound on `C_T`. The polynomial is local;
   it is not being asserted to be a periodic function by itself.

6. **The order-zero counterexample** (`LGF.md:437–486`). The fifth-order
   boundary zeros make the proposed annular test C^4. For `T>=64`, its support
   and the required neighbor sites stay inside the annulus where the rejected
   estimate applies. The centered stencil cancels the harmonic second-order
   term of `Phi`, leaving `Delta Phi=O(T^-6)`, whereas
   `Delta phi_T=O(T^-2)`. A hypothetical `H_T=O(T^-3)` makes
   `sum H_T Delta phi_T=O(T^-1)`, but the other side tends to
   `-integral phi<0`. The arbitrary extension away from the common local
   stencil does not affect summation by parts. This refutes only the specified
   uniform order-zero estimate; it does not prove optimality at order one or
   an obstruction to a Yang–Mills construction.

7. **Gauge quotient and curvature signs** (`LGF.md:490–542`). Exterior
   multiplication/contraction and `(nabla_j^+)*=-nabla_j^-` give the scalar
   Hodge Laplacian. At a nonzero momentum, rotate the link vector
   `q_j=exp(ip_j)-1` to a coordinate axis: on transverse links the quadratic
   operator is `|q|^2`, and `q wedge` maps them onto a three-dimensional exact
   two-form space. Its covariance is the orthogonal projector onto that space;
   gauge and harmonic modes have zero curvature. As an algebraic discriminator,
   at `p=(pi,0,0,0)` on an even torus, the projector has eigenvalue one on
   planes 12, 13, 14 and zero on the other planes. A factor-of-eight error
   would fail this check. Independently taking the two position-space curls
   gives the four signs in (39), because a forward y-difference becomes a
   negative backward z-difference. The trace identity
   `sum_{mu<nu} G^F_{mu nu,mu nu}(z)=3(delta_0(z)-T^-4)` checks the zero mode
   and signs together. These are hand calculations, not numerical runs.

8. **The exact scalar input and its square** (`LGF.md:526–548`;
   `TSE55.md:185–238`; `CODEX_REVIEW_TSE.md:124–142,158–170`). The continuum
   tensor is exactly `-X/(4 pi^2)` with the same base points and increasing
   orientations. Four applications of (5) give `B(r^-5+T^-4)`, `B=2^1002`.
   With `|D|<=2^12 r^-4`, the cross term in the square is bounded by
   `2^1015(r^-9+r^-4 T^-4)`. The error square is bounded by
   `B^2[r^-9+(2+1/256)r^-4 T^-4]`, using both `r>=1` and `r<=T/4`.
   This verifies the explicit `2^2010` constant in the adopted consumer.
   Diagonalizing the continuum radial Hessian gives eigenvalues
   `(6,-2,-2,-2)/r^4`; the six two-form entries then have squared sum
   `6/(pi^4 r^8)`. The clover's four corners and two ordered orientations
   give `w_f=(1/4)sum_corners f`; Wick's two pairings give
   `12(N^2-1)/pi^4`. This derives the coefficient without using A4's PASS.

9. **The consumer's quantified range and scaling.** For two positively
   oriented plaquettes, each base-to-corner offset has coordinates zero or
   one. Their difference has Euclidean norm at most two, including different
   planes. Consequently the `D_-lambda/a-2` and `D_+lambda/a+2` bounds in
   `TSE55.md:231–234` are valid. Together with `L^(K-m)>=4/D_-`, its enlarged
   `R_0>=8(D_++1)` ensures `1<=r<=T/4` with `T=R/a`, uniformly in the specified
   indices. Multiplying
   the squared error by the test weights gives the powers `a/lambda` and
   `(lambda/R)^4` used in FREE. In physical units the kernel's finite-volume
   error is `O(R^-4)`, which does not disappear merely by taking `a` to zero
   at fixed R. The infinite-volume amplitude discussion at `TSE55.md:195–199`
   must retain the large-volume limit; FREE itself correctly retains the
   finite-volume error and chooses a sufficiently large fixed `R_0`.

**What I did not re-derive or independently establish**

- The full FREE test-function replacement and relative Riemann-sum constants,
  K-dec and its transitive RG estimates, FLOW-pw, PL-1L, Theorem TS as a whole,
  reconstruction, or any interacting Yang–Mills statement. I checked FREE's
  LGF interface, normalization, support range, and error powers. The remaining
  inputs in R9 stay separately conditional.
- The external books and papers in full. I inspected an excerpt of
  [Lawler–Limic §4.3](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
  [Uchiyama abstract](https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/greens-functions-for-random-walks-onn/080445758FA185A7BFEFB2B6A2E87C05),
  and [Spitzer publisher record](https://link.springer.com/book/10.1007/978-1-4757-4229-9)
  for attribution context. The Fukai–Uchiyama DOI and attempted publisher
  retrieval were inaccessible. No external theorem, remembered asymptotic,
  or load-bearing [m] step was used to close LGF's proof.
- Numerical outputs, historical criteria-before-script chronology, or formal
  proof-assistant certification. I read all three `ts55_*` scripts, criteria,
  and saved outputs; I did not rerun them or authenticate their execution
  history. There is no LGF numerical runner or numerical proof input.
  Hashing and source bookkeeping were the only executed Python operations.

The complete LGF proof, log, both preceding LGF reviews, briefs, criteria and
manifest were inspected. Necessary convention sources included LINEAR_PACKAGE
§1.1, its Weitzenböck pointer at `PROOF_session16_snapshot.md:953–963`,
`ROTDEF.md:98–125`, and OSLEAF55 D8/TR-0/TR-1. The reviewed consumer and its
adoption diff, rather than a historical review verdict, determine the matching
assessment above. More reviews or PASS lines supply no additional proof.

Only `REVIEW2_LGF.md` was written. No other source, prompt, audit or ledger
file was edited; no numerical job, commit or PR was made. The reviewed source
hashes were rechecked after report creation and remained unchanged.

VERDICT: CONFIRM
