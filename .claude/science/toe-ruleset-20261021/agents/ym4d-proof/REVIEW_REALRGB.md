**Independent hostile review of REALRGB.md — 2026-10-30**

Reviewed the 750-line report with SHA-256
`80d4f1216e39c9d5cd661c7eced48f3ac480c0d1443e556208a1b2684890d640`
under `briefs_q/REALRGB/REVIEW.md`. Line references below are to that report
unless another file is named. This is fresh-context Codex review of Codex
work, hence same-family review, not cross-family verification. The earlier
review's verdict was not used as a mathematical premise.

**Disposition: LAND as an accurately scoped partial research report.** The
uniform local RG step remains OPEN. I found no binding mathematical defect
in the positive results at their stated scopes. In particular, G27 is an
estimate for a filled original flux sector against the specified all-cut
denominator; it is not a small local activity theorem or an extracted
continuation contraction.

1. **Task scope and statuses — PASS; full target correctly OPEN.**
   **Lines 3–22, 680–718, 720–744.** The author brief's claim that the
   predecessors stall only at complex norms is contradicted by
   `REALONLY.md:3–9,425–428` and `CHARGE.md:240–265,549–556`. REALRGB
   correctly rejects that premise. PROVEN is reserved for displayed
   implications or finite-model results; the proposed construction at
   lines 708–718 is ARGUED. No audit classification, completed Yang–Mills
   theorem, or general no-go follows or is claimed.
   **Fix:** none. Retain the OPEN target and all conditional qualifiers.

2. **Real norm and derivative order — PASS.**
   **Lines 27–65 (G1).** For each order m, Leibniz gives the convolution
   of derivative bounds, and division by m! converts its binomial
   coefficients into `1/(l!(m-l)!)`. The truncated convolution is bounded
   by the product of the two nonnegative Taylor sums. Thus the scalar jet
   norm is submultiplicative. Fixed-mask regrouping commutes with these
   derivatives by linearity; it needs no complex Cauchy estimate.
   The l1 direction norm bounds individual labelled mixed derivatives
   without an ambient coordinate count. It does not bound their rooted
   sums. The exclusion of eta derivatives and the distinction between
   the source window rho and jet weight h are explicit. Four derivatives
   cover the finite subset-jet algebra in `REALONLY.md:139–179`; they do
   not provide its all-order reconstruction estimates.
   **Fix:** none; no invariant actual RG norm is established by G1 alone.

3. **Failed history, the two normalizations, and positivity — PASS.**
   **Lines 67–147 (G2–G5).** These definitions match
   `RD3.md:25–89,100–168`. With L>=3, each marked direction-one link has
   every incident plaquette inside its block. Varying every old link
   within its radius-1/16 ball changes each plaquette by less than 1/4.
   Exactly the two specified blocks remain bad; their size exceeds the
   cutoff, independently of U1. This is a positive product-Haar set,
   including all the identity-centered link balls. It proves positivity
   of the inherited density on every U1 fibre in this example. Current
   interior identity balls prove D_h>0 independently of frozen eta;
   a marked interior link similarly proves N_h>0. A full current identity
   cap proves Z_A>0 for any fixed set of retained cuts. The report does
   not extend this good-fibre argument to arbitrary histories.

   Integrating K1 over V gives `int R_h=A_h`, so `p=R_h/A_h` is a
   conditional probability density. Z_A is instead the source-free bare
   all-cut reference. The factor `A_h/Z_0` must remain outside p in an
   unconditional history sum, exactly as stated. Substituting
   `rho=b_1 J_h` leaves the exterior inverse a_B in D_h; only r_h cancels
   it. The full conditional convention retains O D_h.

   Independently, the entry-cell cover uses at most
   `(1+4N/zeta)^(2N^2)` balls. On the product cap, `s(U_p)<=8 zeta^2`.
   The 6n_j plaquettes, 4n_j link masses and 4n_(j+1) kernel lower bounds
   give precisely G5. This lower bound is extensive. TV=1 follows only
   after dividing a positive measure by its own mass.
   **Fix:** no binding correction. For notation clarity, rename the size
   cutoff at line 68 to `n_cut,0`; n_0 later denotes original lattice
   volume (lines 135–140 and 472–505). Explicitly stating
   `n_j=|Lambda_j|=n_0 b^(-j)` there would remove this harmless collision.

4. **Positive-integral derivative calculus — PASS.**
   **Lines 149–206 (G6–G8).** Differentiating `exp H` assigns the labelled
   directions to set partitions. Positive normalization then bounds
   `D^m Z/Z` by M_m. Differentiating `Z*(1/Z)=1` gives the independent
   reciprocal majorant recurrence

       I_0=1,
       I_m=sum_(k=1)^m binom(m,k) M_k I_(m-k).

   Expansion of the logarithm gives coefficient
   `(-1)^(r-1)(r-1)!` for a partition with r blocks; the reciprocal gives
   `(-1)^r r!`. These reproduce all the displayed L_m and I_m. Leibniz
   then gives C_m. In particular,

       I_4=B+21B^2+78B^3+75B^4,
       C_4=2B+42B^2+156B^3+150B^4,
       P_4(1,1)=1+2+8/2+46/6+350/24=117/4,
       sum_(m=1)^4 L_m(1)/m!=1+3/2+13/6+77/24=63/8.

   The rescaling `h<=1/(1+B)` bounds every `h^m B^l`, l<=m, by one.
   There is no missing rare-mass inverse: relative derivatives are
   expectations under the positive normalized law. The zeroth-order
   size of F remains a separate factor in G8. Signed coefficients and
   moving supports are correctly excluded.
   **Fix:** none.

5. **Application to the actual soft kernel — PASS at fixed sectors.**
   **Lines 208–266 (G9–G11).** For q=(epsilon,X), the opened integrand's
   only differentiated terms are the original coefficient perturbation
   and the terminal numerator `t_j Re tr(exp(-X)Vbar* M)/N`.
   The terminal kernel normalizer depends on its fine input, not V;
   earlier kernels and the old history are also q-independent. They
   therefore belong to w_0 rather than being omitted.

   Iterated variation of constants expresses `D^m exp X` as m!
   ordered-simplex integrals with total simplex volume 1/m!. The
   intervening exponentials are unitary for anti-Hermitian X, so their
   operator norms are one. Trace duality and `||M||<=1` give first-order
   bound `2u_0 sum|a_p|+t_j sum||A_c||` and higher-order bound
   `t_j sum_c product_i ||A_(i,c)||`. Both are bounded by G6 with
   `B_j=max(2u_0,t_j)`. This is uniform in coordinate count and fixed
   history, but remains coupling-dependent. Compact integration and
   fixed bounded predicates justify differentiation. G11 matches
   `RD3.md:66–85,130–143` and is correctly classified as an insufficient
   upper bound, not evidence of a large optimal activity.
   **Fix:** none. In particular, do not substitute u_j for the original
   source coefficient u_0 in a later application.

6. **Spatial locality and moving selectors — PASS diagnostics; OPEN
   actual bounds.** **Lines 270–314 (G12–G13).** Differentiating the
   complete positive integral yields `-u_0 E s_p` and
   `u_0^2 Cov(s_p,s_q)`, including differentiation of its law. Since
   `0<=s<=2`, each covariance has modulus at most one. This is not a
   sum over q. If supported logarithmic activities had budget k_* and
   fixed source incidence c_p, G1 would give

       sum_q |partial_p partial_q log R_h|
       <=2 c_p h^(-2) sup_(n>=1)(n exp(-mu n)) k_*.

   The conditioned-sign law has log-MGF `log cosh(sum z_i)`, and every
   entry of its Hessian at zero is one. Its row sum grows with m despite
   bounded relative derivatives in l1 directions. This refutes precisely
   the claimed general inference, not the Wilson estimate. The moving
   indicator example integrates to |x| and correctly defeats automatic
   differentiation through a selector. The successful eta=I patch agrees
   with `RD3.md:123–128`. No actual-sector singularity is asserted.
   **Fix:** none; G13 and selected-sector C4 regularity stay OPEN.

7. **Hole norm transfer — PASS, including its obstruction scope.**
   **Lines 316–340 (G14).** The 81-point hole has eight disjoint outside
   faces of 27 points each, hence a closed face-neighbourhood of 297
   points. Saturation adds at most 81 vertices. An inactive output root
   can be charged to one of those 297 input roots; retaining unchanged
   inactive terms adds the leading one in G14. The argument applies
   separately to every derivative. For holes of size at most M, at most
   `8|X|` holes touch X and at most 9M input-root witnesses are needed;
   this recovers `(1+9M)||K||_((1+8M)mu,4,h)` from
   `LIB1.md:377–419`.

   With a sole active vertex v and constant activity on {v}, saturation
   produces the entire connected torus. The norm ratio is exactly
   `exp(mu(|Gamma|-1))`. This is a valid counterexample to an unrestricted
   fixed-mu saturation bound, not to a bound on actual weighted histories.
   **Fix:** none; bounded-hole or additional-weight hypotheses cannot be
   dropped when consuming G14.

8. **Raw action, fresh gaps, and geometric badness — PASS.**
   **Lines 344–385 (G15–G16).** The identity
   `2N s(W)=||I-W||_HS^2` gives the owned-plaquette charge, with overlap
   fractions allocated once. For a gap event, a 1/t cap around a maximizer
   gives denominator `>=exp(-1)(1+4Nt)^(-2N^2)` and tail numerator
   `<=exp(-ta)`. This proves G15 with its normalizer intact. Conditional
   multiplication is valid for distinct outputs and past-adapted choices,
   as in `JMBRB.md:178–221`; it does not apply without a future-tilt bill.

   Sweeping the straight leg across at most `3L(L-1)/2` plaquettes proves
   the mean comparison by telescoping conjugated unitary factors. On the
   smooth branch, bad coarse curvature forces one link distance at least
   epsilon/8. The resulting gap is at least
   `epsilon^2/(128N)-2A_L eta_1>=epsilon^2/(256N)`.
   At most six plaquettes can select the same witness link, giving the
   stated `4^n p_gap^(n/6)` union bound. The rough-input charge based only
   on this smaller threshold is of order `u^(2delta_c-1)`; its failure to
   diverge is correctly a failure of that estimate. These constants and
   branches match `JMBRB.md:230–307` and `LFPRICE.md:639–648`.
   **Fix:** none.

9. **Derivative prices, future tilts, and seams — PASS conditional
   implications.** **Lines 387–428 (G17–G19).** G17 follows by applying
   G8 to the same positive ratio already bounded at order zero. The
   source-only and moving-terminal-selector distinction is necessary and
   present. For a future reader, direct division by KH proves G18;
   H=1_E indeed makes the tilted event probability one whenever KH>0.
   Replacing a source-free Wilson plaquette costs at most 2u and replacing
   a complete kernel at most 4t, including both normalizers, consistent
   with `JMBRB.md:381–413`. The order-u seam estimate cannot pay a
   sublinear threshold by itself. G19's geometric series is valid only
   after every matching, reader and derivative cost is included. No
   actual theta_gap<1 is supplied.
   **Fix:** none for the displayed bare/current-reference comparison.
   If the seam formula is later used on original perturbed factors,
   retain their coefficient magnitudes: the uniform plaquette bill is
   `2u_0(1+rho)P`, or a separately paid source comparison, not `2u_0 P`.
   G24 already retains its explicit original-source debit.

10. **Persistent flux and nonuniform forward return — PASS at the stated
    finite horizon.** **Lines 430–481 (G20–G22).** Using the paired paths
    in `RENEW.md:35–42,163–178`, direction-one axial contributions cancel
    and direction-two translation contributes `r_1-(L-1)/2` powers of g.
    The odd offset sum gives the displayed P. For A=W*V unitary,
    `tr(A* P A)=tr P`; expanding the quadratic form proves the gap
    identity even when A and P do not commute. Since P>=I/L, W is the
    unique maximizer and the rough orbit repeats.

    A contour has at most `4(L-1)+L=5L-4` links. The tube recursion gives
    mean error at most p_L delta_j and hence gap
    `delta_(j+1)^2/(2NL)-2p_L delta_j=delta_(j+1)^2/(4NL)`.
    G15, a union bound and successive conditioning prove G21. Couplings
    tend to infinity at fixed finite horizon and compatible volume;
    no infinite-depth probability limit is taken. Thus a uniform plain
    forward finite-window curvature-return margin on all inputs is
    actually excluded. Extracted or restricted-history operators are
    not excluded. The original tube has n_0 charged 12 plaquettes, giving
    G22; the fractions alpha_l sum to less than one.
    **Fix:** none. Preserve the finite-horizon and one-use-charge scope.

11. **Filled-sector source and fourth-jet estimate — PASS; principal
    positive result verified.** **Lines 483–542 (G23–G27).** On the real
    source window, `-u_0 sum epsilon_p s_p<=12rho u_0 n_0`. Dropping
    optional history selectors increases the scalar numerator. Bounding
    the last kernel costs `8kappa u_j n_(j+1)`; earlier kernels then
    integrate to one, and the original tube costs `c_delta u_0 n_0`.
    Dividing by G5 adds another `8kappa u_j n_(j+1)` and its cap costs.
    This gives exactly d_j in G24. No division by a rare history mass
    occurs. The argument matches `CHARGE.md:153–217`, now with the
    explicit source penalty.

    With zeta=u_j^(-1/2), n_j/n_0=b^(-j), and u_j<=u_0, G25 bounds
    `d_j n_j/(u_0 n_0)` by c_delta/2. The source penalty is at most
    c_delta/4. Therefore `sup Q<=exp(-c_delta u_0 n_0/4)`. For a fixed
    selector independent of terminal V, both complete integrands satisfy
    G6, so G8 proves G26 for all mixed derivatives through order four.
    The text correctly does not differentiate a current moving selector
    or exchange a sum of history suprema with the supremum of their sum.

    Finally B_j<=c u_0 and positivity of the polynomial coefficients give
    `P_4(h,B_j)<=P_4(h,c)u_0^4`. Splitting the exponential in G26 and
    using n_0>=1 leaves `u_0^4 exp(-c_delta u_0/8)`, whose maximum is
    `[32/(e c_delta)]^4`. This proves the stated fixed-h G27. Its
    constants are independent of volume, depth and holes under G25.
    It covers arbitrary fixed hole masks because the denominator cap
    varied all current links; it is not a theorem with arbitrary frozen
    exterior links. The finitely many excluded early levels are not
    silently assigned G27.
    **Fix:** none. Coupling ordering, positive cut lower bounds, source
    restriction and the filled original sector remain binding hypotheses.

12. **Creation envelope versus localized weights — PASS.**
    **Lines 544–566 (G28–G29).** After the separately hypothesized
    `exp(s n_0)` support/type cost, substituting `n_0=b^R n_R` proves
    G28. Its successive-term ratio tends to zero for fixed n_R, and
    n_R>=1 supplies a common summable envelope. This costs the original
    reserve once. The local-core analogue retains the extensive
    `d_j n_j`, so it gives no volume-uniform small local bound as n_j/m
    grows. Neither inference is reversed into an actual lower bound.
    The restrictions agree with `CHARGE.md:219–251,511–529`.
    **Fix:** none; G28 is not G35 for every creation.

13. **Joint cluster theorem — PASS with its full antecedents.**
    **Lines 570–605 (G30).** Factorization is required of the complete
    integrated coefficients A_I before logarithms. Their jet norms,
    rather than just scalar probabilities, are bounded. Thus each
    connected selected set produces a polymer on the union of all its
    readers, including prefactor and measure readers.

    In the first positive tree majorant, the child sum at i is bounded
    by `Q_4 |H_i|`, so `b_i=e^((mu+2)|H_i|)alpha_i` is a supersolution.
    Marking an atom through the spatial root bounds the integrated
    polymer budget at exponent mu+1 by Q_4. For the logarithm, order
    incompatibility edges. Graphs with a fixed Kruskal tree have exactly
    the optional edges later than every edge on their tree path; their
    alternating sum has modulus at most one. A second rooted tree bound
    spends the remaining unit of support exponent and gives log budget
    <=Q_4 in the same submultiplicative jet norm. Repeated polymer labels
    in logarithmic tuples are covered by that positive tree majorant.
    The auxiliary atom multiplier z preserves convergence for |z|<2;
    equality with the exponential near zero extends to z=1. Real
    coefficients yield the positive real gas and its real logarithm.
    This imports no complex physical-source domain. The construction
    matches `JMBRA.md:239–310`, `JMBRB.md:479–556` and
    `REALONLY.md:430–459` without assuming their actual-model hypotheses.
    **Fix:** none. Full supports, exact factorization, joint jet bounds
    and separate empty-support normalization are essential.

14. **Local logarithms, support cost, and the next output — PASS
    conditional arithmetic; actual estimates OPEN.**
    **Lines 607–678 (G31–G35).** Restriction to epsilon=0 maps a direction
    `(a,A)` to `(0,A)`, a contraction in the declared l1 norm. It retains
    coarse derivatives. The difference of the two supported logs and
    this restriction therefore costs the stated factor two. Applying
    G14 gives exactly G32. Integrating the terminal reference against
    Q_h gives `A_h/Zbar_A`, not p or Q_h, so that distinct consumer still
    requires its own estimate.

    Multiplying the joint size-n price, boundary, derivative, full-support
    and type bounds gives `r_4^n`; summing proves G33 if those inputs
    exist. Positivity removes a TV debit, not the reference comparison.
    For the nonnegative norm bounds in G34, `x_j^2<=M x_j` proves
    invariance directly. Splitting r=qm+s gives the continuation sum
    `m B_0/(1-theta_win)`; first-return sums additionally carry D_ret,
    as in `RENEW.md:409–437`. A common a_r in G35 bounds both forward
    lifetimes and fixed-terminal accumulation by reindexing r=k-j.
    Separate bounded lifetime sums do not give that common envelope.
    None of these actual extracted operators or invariant C4 maps is
    asserted to have been constructed.
    **Fix:** none. The missing estimates are substantive open work,
    not a reason to relabel these conditional implications as closure.

15. **Clause accounting and negative assertions — PASS.**
    **Lines 682–706.** The real dispositions match the obligations in
    `LFPRICE.md:654–699`: clause 2 has a filled-sector instance but lacks
    the general matched joint bound; clause 3 gains positivity and
    relative derivatives but lacks a local log budget; clause 4 has
    conditional algebra but lacks actual small joint weights; clause 5
    lacks extraction and invariant return estimates. The clause-1
    replacement identity agrees with `JMBRA.md:79–115`: integrating the
    old good interiors cancels precisely their C_Y factors, and summing
    chi/zeta sectors restores one. It does not make the interacting
    reference a product measure.

    The normalized mandatory atom has integral one, giving the stated
    genuine smallness failure. The direct-Haar row explicitly concerns
    `alpha_p=sup|exp(-u_0 s_p)-1|`: setting one unrestricted link to g
    gives s_p=4/N and the displayed threshold. This does not lower-bound
    a jointly integrated coefficient. The cap, covariance, hole and
    forward-return rows have precisely the narrower dispositions checked
    above. There is no unsupported general obstruction or hidden GO.
    **Fix:** none.

16. **Sources, checks and review provenance — PASS at the recorded scope.**
    **Lines 19–23, 746–750; REALRGB_LOG.md:41–74,113–181.** I checked the
    relevant mathematical passages in all nine named reports, the RD
    source/selector definitions, AUTHOR.md and PROCESS_LIGHT.md. REALRGA.md
    is absent. The report's local equation and section references resolve
    to the objects described above. No quoted external theorem carries
    a proof step; Balaban and Dimock receive methodological attribution.

    Read-only `shasum -a 256 -c checks/realrgb_input_sha256.txt` verified
    all twelve recorded inputs. The current criteria and check script
    hashes match the receipt, as do the report and earlier review hashes
    recorded in the log. The stored result reports nine passing exact
    checks, seven resource samples and empty stderr; the script's
    algebraic recurrences and geometry construction agree with those
    claims. These are existing author-run receipts, not a fresh run or
    an independent proof of local RG estimates. I rebuilt the relevant
    algebra and geometry above without executing that writing script or
    any new numerical experiment. Historical preregistration timing and
    agent-launch independence cannot be independently certified from
    this snapshot; this review does not rely on either for its science
    verdict. The existing review's final line was checked only after
    completing the mathematical assessment.
    **Fix:** none. Keep the recorded finite-check and same-family limits.

**Binding fixes: none.** The cutoff/volume notation suggestion in item 3
is editorial. The source-dependent seam qualification in item 9 governs
any future extension of that comparison; it does not affect the explicitly
source-debited G24–G27 proof. The OPEN local joint coefficients, moving-sector
regularity, arbitrary-hole control and extracted iteration are not supplied
by this landing decision.

Only REVIEW_REALRGB.md was created. No other file was edited and no commit
was made.

VERDICT: LAND
