# REALRGB fresh hostile review

Date: 2026-10-30. Reviewer: a separate fresh-context Codex reviewer of a
Codex author, **same-family review**. This is not cross-family review, and
no independently verified model or reasoning-effort designation is claimed.
I did not author the report, edit its sources, or run the author's checks.
The verdict below concerns the correctness and honest scope of the author
report; it does not certify closure of its explicitly OPEN uniform RG target.

Reviewed source: [REALRGB.md](../REALRGB.md), SHA-256
`80d4f1216e39c9d5cd661c7eced48f3ac480c0d1443e556208a1b2684890d640`.
This includes the author's repaired direct-Haar diagnostic, corrected
source-only normalization explanation, and final table-formatting edit.
Locations below refer to that version.

## Contract and source coverage

I read [AUTHOR.md](../briefs_q/REALRGB/AUTHOR.md),
[PROCESS_LIGHT.md](../PROCESS_LIGHT.md), the supplied machine instructions,
and `/Users/jonBridger/AGENTS.md`. The explicitly bounded lane governs this
review. The installed review-loop skill was inspected for applicability;
its separate branch/landing/audit-pipeline workflow is not invoked for this
standalone, review-only lane. No commit, audit, ledger, source edit, further
agent, or numerical experiment was made. This new review is my only write.

I read the complete author argument and inspected these actual source
arguments, rather than accepting their status labels as evidence:

| Source | Material checked |
|---|---|
| [REALONLY.md](../REALONLY.md) | Sections 3 and 6–7: finite versus all-order jets, positive references, joint-jet hypothesis, cluster and continuation interfaces. |
| [CHARGE.md](../CHARGE.md) | Sections 1–2: actual reference, flux field, one-use allocations, cap comparison C9, coupling/cut hypothesis C10, local-versus-extensive distinction. |
| [RENEW.md](../RENEW.md) | Actual paired contours; sections 3 and 5: nonlinear flux orbit, finite-horizon tube proof, conditional window arithmetic. |
| [RD3.md](../RD3.md) | Sections 1–3 and 6: complete failed history, positive fibres, actual local/full normalizers, current-history sum, 81-block hole conversion. |
| [RD4.md](../RD4.md) | Sections 1–3: stable-domain obligation, full-reader supports, conditional joint expansion, direct-Haar diagnostic, local budget and gluing obligations. |
| [JMBRA.md](../JMBRA.md) | Sections 1–3 and 6: exact replacement against Z_A, complete-reader elimination, factorization scope, actual matching cost and supremum-majorant diagnostic. |
| [JMBRB.md](../JMBRB.md) | B-GAP, B-GEOM, B-SEAM and B-JOINT: normalized tail, smooth/rough dichotomy, seam debit, two-stage cluster proof. |
| [LFPRICE.md](../LFPRICE.md) | LF1, LF2, LF4, LF10 and LF-JMBR: units, one-use charge, polynomial absorption, failed returns and the five required clauses. |
| [LIB1.md](../LIB1.md) | Sections 1–2 and 5: fixed masks, exact resummation, inactive terms, full versus active norm and bounded-hole cost. |

No external literature result carries proof weight in this review. The
large-field organization/exposition is credited to Tadeusz Balaban and
Jonathan Dimock, as in the author report. REALRGA.md was absent when checked;
the author's explicit candidate norm therefore has no claimed agreement
with a separate parallel norm contract.

## Material finding and affected-fix confirmation

**Resolved finding: the pointwise Haar diagnostic initially overreached
the integrated coefficient criterion.** In the original section 7 row,
setting one integration link to g was used to assert a lower bound on
G30's Q_4. That construction lower-bounds a pointwise supremum; it does
not lower-bound a fully integrated coefficient or its optimal joint-jet
majorant. RD4 C10 and JMBRA A23a use the particular supremum majorant.

I required the diagnostic to name that choice and retain joint integrated
estimates, including estimates under the same reference, as a live route.
The author repaired this directly. **Final line 700 passes:** it defines
Q_sup, specifies alpha_p as the pointwise supremum (or its larger sup jet
norm), and expressly distinguishes G30's integrated coefficients/optimal
Q_4. The displayed threshold is correct for this chosen majorant. I also
read the final `abs(...)`/`card(...)` table edit; it changes no claim.

The author separately corrected source-only normalization during self-check.
I verified final lines 613–617: setting epsilon to zero does not annihilate
pure coarse derivatives. The restriction is composition with the projection
(a,A) -> (0,A), whose operator norm in G1 is at most one. Its C^4 norm is
therefore at most the original norm, so subtraction still costs at most two.
This is now an adequate proof of G31 for source-only normalization.

**No blocking defect remains in the reviewed version.** The mathematical
checks below are independent written derivations. My core conclusions were
obtained before reading the author's execution result; they do not rely on
that result or on a second run of the same implementation.

## Independent derivative reconstruction: G6–G10

For normalized unit directions, write M_m for the relative mth derivative
majorant of a positive integral and I_m for the inverse majorant. Marking
one derivative in D(e^H)=e^H DH gives an alternative to the author's
set-partition calculation:

    M_0=1,
    M_(m+1)=B sum_(r=0)^m binom(m,r) M_r.

For mixed derivatives, choose the subset of the other directions falling
on e^H; each remaining derivative of H is bounded by B. Integrating the
absolute derivative and dividing by Z uses its own positive probability
law. It does not use a lower bound on the mass of the selected event.

Differentiating Z(1/Z)=1 gives

    I_0=1,
    I_m=sum_(r=1)^m binom(m,r) M_r I_(m-r).

Finally D log Z=(DZ)/Z and Leibniz give

    L_m=sum_(r=0)^(m-1) binom(m-1,r) M_(m-r) I_r,
    C_m=sum_(r=0)^m binom(m,r) M_r I_(m-r).

These are bounds in the multilinear operator norm, not only along a common
scalar direction. Written expansion through order four yields:

| m | M_m | I_m | L_m | C_m |
|---|---|---|---|---|
| 1 | B | B | B | 2B |
| 2 | B+B^2 | B+3B^2 | B+2B^2 | 2B+6B^2 |
| 3 | B+3B^2+B^3 | B+9B^2+13B^3 | B+6B^2+6B^3 | 2B+18B^2+26B^3 |
| 4 | B+7B^2+6B^3+B^4 | B+21B^2+78B^3+75B^4 | B+14B^2+36B^3+26B^4 | 2B+42B^2+156B^3+150B^4 |

Thus every polynomial in the author's table is reproduced. At B=1,
C_0,...,C_4 are 1,2,8,46,350; their factorial-weighted sum is 117/4.
The corresponding positive-order log sum is
1+3/2+13/6+77/24=63/8. Since each power B^l has l<=m, the stated
h<=1/(1+B) bound follows term by term. G8 correctly retains sup(N/D):
the estimate is relative and does not make an arbitrary returned activity
small. Signed coefficients require their separate joint norm hypothesis.

For the actual opened integral, all source dependence is
-u_0 sum epsilon_p s_p, and all terminal-field dependence is in
t_j sum Re tr(exp(-X_c)Vbar_c^* M_c)/N. In the ordered-simplex formula for
D^m exp(-X), the intervening exponentials are unitary. The m! orders cancel
the simplex volume 1/m!, bounding the derivative by the product of direction
norms. Trace duality and norm(M_c)<=1 then give

    first order <= 2u_0 sum_p abs(a_p)+t_j sum_c norm(A_c),
    higher orders <= t_j sum_c product_i norm(A_(i,c)).

The latter sum is bounded by the product of the corresponding l1 sums.
Consequently B_j=max(2u_0,t_j) works in every mixed order through four.
This checks the absence of a volume, depth or hole-count factor in G10.
It also checks that the original u_0 cannot be replaced by u_j.

Earlier kernels, their mean-dependent normalizers, old selectors, and hole
fields really remain integration data. The last kernel normalizer is
independent of the terminal output. The source-free Z_A and terminal-free
A_h simply omit the respective score. Compact real integration and fixed
bounded predicates justify the derivatives. Frozen eta is not differentiated.
The current selected predicate, if it reads V, is outside this proof.

## Independent reference and charging reconstruction: G24–G27

Here n_0 denotes the number of original lattice sites, not the earlier
illustrative size cutoff also written n_0 in G2's discussion. The source
uses n_j=n_0 b^(-j), b=L^4.

The group-entry cover proves Haar(B_zeta)>=
(1+4N/zeta)^(-2N^2): each entry cell has operator diameter strictly less
than zeta, its representative gives a translated ball, and invariance
makes all such ball masses equal. On the all-identity current cap,
norm(I-U_p)<=4zeta and s(U_p)<=8zeta^2. There are 6n_j plaquettes,
4n_j current links and 4n_(j+1) output kernels. Since each normalized
kernel is between exp(-2t_j) and exp(2t_j), this independently gives

    Z_(j,A)>=exp[-(48u_j zeta^2+8N^2 log(1+4N/zeta))n_j
                     -8kappa u_j n_(j+1)].

Every retained cut passes when 4zeta is below it; removing cuts to make
arbitrary holes does not spoil this cap. This is a bound for the actual
bare all-cut denominator, not a conditioned history mass.

On a fixed original flux tube, the n_0 distinct 12 plaquettes have distance
at least 2-4delta. Expanding the Wilson action gives
S_0>=c_delta u_0 n_0, with c_delta=(2-4delta)^2/(2N).
The original-source perturbation costs at most 12rho u_0 n_0 because
there are 6n_0 plaquettes and 0<=s<=2. Strip only the last kernel upper
bound, integrate all earlier normalized kernels in reverse order, and
finally integrate probability Haar. The numerator is at most

    exp[-(c_delta-12rho)u_0 n_0+8kappa u_j n_(j+1)].

Dividing by the displayed lower bound gives G24, including its
16kappa u_j/b term. Nonnegative fixed previous-history subsets are bounded
by the same integral; disjoint histories may be summed before this bound.
There is no inference concerning a sum of separate suprema, and no old
history mass is extracted and charged a second time.

With zeta=u_j^(-1/2), G25 gives

    d_j n_j/(u_0 n_0)
      <= b^(-j) sup_(u>=u_*) [48+8N^2 log(1+4N sqrt(u))]/u
                       +16kappa b^(-(j+1))
      <= c_delta/2.

Here both u_j/u_0<=1 and n_j/n_0=b^(-j) are used. The stipulated cut
condition is more than sufficient for the cap, and u_*>=4 ensures
zeta<=1. Taking rho<=c_delta/48 leaves c_delta/4 of the original
exponent. Applying the already rebuilt relative quotient estimate gives
G26 for all mixed original-source and terminal-coarse derivatives.

For fixed h, put c=max(2,kappa). The positive coefficients and degree at
most four imply P_4(h,B_j)<=P_4(h,c)u_0^4 since u_0>=1. Split the remaining
exponential in half and use n_0>=1:

    u_0^4 exp[-c_delta u_0 n_0/8]
      <= sup_(u>0) u^4 exp[-c_delta u/8]
      =[32/(e c_delta)]^4.

This proves G27 with the reported constant and fixed, coupling-independent
h. The loss from c_delta/4 to c_delta/8 is paid explicitly, as required
by LFPRICE LF10. The proof applies to the specified extensive creation
family; it provides neither a local-core norm nor a homogeneous
continuation contraction. G29 correctly exposes the unremoved extensive
reference debit for a small core in a large volume.

## Quantifier, locality and next-step stress tests

- **Failed history and fibres, lines 67–128.** The two marked interior
  links produce exactly the two old bad blocks on the stated open cap.
  Their size already forces failure, so no unseen completion test or
  absence predicate invalidates this witness for any real U_1. The good
  local cap depends only on interior links, so it works at every frozen
  eta in this particular example. The report correctly restricts general
  history positivity to admitted nonzero fibres and does not divide by
  a zero mass. R_h sums current outcomes; a selected current child is a
  different object. A_h and Z_A are kept distinct throughout.

- **Locality, lines 270–314.** The source Hessian is u_0^2 times the
  conditioned covariance. The covariance bound is pointwise, whereas a
  local supported C^4 expansion implies a rooted sum such as G13. The
  all-equal-sign example has unit mixed covariances and a sum growing as
  the number of signs, while its score has a dimension-independent l1
  bound. It is a valid counterexample to the general inference, explicitly
  not a Wilson counterexample. Moving-selector boundary derivatives are
  correctly left open. The integral yielding abs(x) is only a regularity
  diagnostic, not a claimed singularity of the actual history density.

- **Holes, lines 316–340.** Saturation for the one hole adds at most 81
  vertices. An inactive root charges to one of 81+8*27=297 original
  roots, yielding G14 also for each derivative. For holes of size at most
  M, at most 8 times the input size holes attach, giving rate (1+8M)mu
  and the stated 1+9M total-family factor. A sole active vertex makes the
  complement one connected hole and sends a singleton support to the
  whole torus; the exact norm ratio exp(mu(card(Gamma)-1)) is unbounded
  for mu>0. This refutes that unrestricted transfer map, not all possible
  history-weighted or differently normed treatments of holes.

- **Fresh prices, lines 344–428.** The cap at a maximizer gives G15 with
  the actual normalizer. On the smooth-input branch the coarse plaquette
  inequality forces a link distance at least epsilon/8. Subtracting the
  two mean errors leaves epsilon^2/(256N), and each link is a witness for
  at most six distinct plaquettes. This reproduces G16 and the union
  bound. The rough branch, future reference tilt G18, and O(u) seam
  comparison are not erased by positivity. G17/G19 are valid conditional
  derivative/iteration implications, not evaluated matched activity bounds.

- **Persistent flux, lines 430–467.** The paired paths on the even
  compatible torus give the stated means: translated direction-one legs
  cancel, direction-two translation changes each direction-one link by
  g, and the odd offset sum is one. The positive-P trace identity holds
  without commuting V with P. Its minimum eigenvalue is at least 1/L.
  A contour error p_L delta_j and two trace errors leave
  delta_(j+1)^2/(4NL), so the union bound proves G21. Its limit is at
  fixed finite horizon and volume as the couplings grow. It disproves
  the stated uniform plain-forward margin on all inputs; it does not
  exclude weighted extraction or an invariant restricted class.

- **Conditional joint cluster theorem, lines 570–605.** Every selected
  integrated coefficient is assumed C^4, fully supported, and bounded
  jointly. Exact factorization over complete overlap components gives
  the hard-core gas. Allowing repeated atom labels enlarges the positive
  tree bound; the supersolution b_i works because its child sum is at
  most Q_4 times the support size. Marking an atom through a root gives
  the gas norm at exponent mu+1. Kruskal grouping bounds each connected
  alternating graph coefficient by spanning trees. Repeating the root
  bound with one further unit of support weight gives the logarithm
  norm at mu. Replacing alpha_i by abs(z)alpha_i for abs(z)<2 preserves
  these estimates, proving agreement with the finite gas at z=1 and
  hence positivity for real coefficients. This uses an auxiliary
  counting variable, not complex physical fields. The differentiated
  measure, prefactors and selections are part of the premise; G8 or
  G27 cannot supply that premise for signed mixed groups.

- **Normalization and further integration, lines 607–628.** G31's
  repaired restriction argument retains coarse derivatives and all
  original supports. Both numerator and reference are fully integrated
  before their logarithms are compared. G32 then pays the actual full
  hole cost. The distinct A_h/Zbar_A comparison is not inferred from a
  pointwise local quotient or from the previous logarithm.

- **Iteration, lines 630–678.** G33 requires paid full-support and type
  sums on the same matched reference. G34 is only invariant-region
  arithmetic, using x_j^2<=M x_j; all actual operator/extraction/domain
  inputs remain open. The window sum follows by writing r=qm+s and
  bounding the ordered product by B_0 theta_win^q. A common summable
  lag envelope in G35 bounds both a birth's lifetime and the sum of
  past births at a fixed terminal level; individual summability without
  that common envelope would not. The report makes this distinction.
  A fourth-order norm is not promoted to an all-order reconstruction
  theorem, nor is fixed-sector regularity promoted to an invariant
  selected-sector C^4 map.

## Disposition

The strongest proved addition is the source-debited, fixed-weight C^4
filled-flux estimate G27 against the actual all-cut reference. The report
does not establish the author brief's uniform returned-activity theorem.
Its status table correctly leaves the actual local mixed estimate G30,
selected-sector boundary regularity, arbitrary-hole control, complete local
normalizer budgets, and extracted next-step/creation bounds open. Those
are substantive real-field obligations, not solely complex-norm issues.

The requested scientific target remains OPEN. That is disclosed and is
not a blocking defect in this accurately scoped research report. The
resolved diagnostic issue has been rechecked in the final source above;
there are no remaining required repairs for this review scope. This is
a landing recommendation for the report, not a target-closure claim,
an audit verdict, or permission to publish a consolidated Yang–Mills proof.

VERDICT: LAND
