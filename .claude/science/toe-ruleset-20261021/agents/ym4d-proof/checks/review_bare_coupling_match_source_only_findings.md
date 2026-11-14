# Source-only mathematical findings: bare coupling match

This record is frozen before opening this unit's author manifest or receipt.
It is preserved unchanged even if the later packet check finds a defect.
No prior review packet or root status front was opened. This is a fresh
same-family reviewer context, requested as Astra/max by the coordinator.

Target: `BARE_COUPLING_MATCH_ASTRA.md`, all 670 lines, SHA256
`7663b556f147e7a4ff03b1f1089e0793f61f8cb6e7adf3d3ff4ce78c763b07ff`.
Actual read windows and exact byte hashes are in
[the frozen read record](review_bare_coupling_match_source_only_reads.json).
Methodology revision: `01589af3faf806b736c42dc2f3bd625e9edead9f`.
Observed main: `bcab5d2ee4a908fbb4e6025635fb878e6c157ebe`.
The installed skill entry points differed; the actual repository versions
were read and verified identical at those two repository revisions.

No blocking mathematical finding was found for the stated one-step,
source-free, fixed-N/fixed-L/fixed-kappa-interval result. A final LAND/HOLD
verdict is deliberately withheld until the separate author-packet stage.

## Independent reconstruction

1. **Normalizer and complete Schur square, target lines 28-147.** CB31-212
   supplies the actual centered brick lift, paired arithmetic contours,
   rooted tree measure and gap; FK53-313 supplies the constrained SU(N)
   saddle and the finite-t normalization. Writing the contour linearizations
   as ell_r, the order-two maximum gains `||Q A||_HS^2/(2N)` while the
   numerator contributes `(<B,Q A>-||B||_HS^2/2)/N`. The path second moments
   cancel. Completing the remaining square gives
   `H_cl=kappa I-kappa^2 Q(D_f^*D_f+kappa Q^*Q)^-1 Q^*`.
   The gap is on all `D(3L^4+1)T^4` free scalar coordinates. No colour,
   root, crossing or harmonic sector was removed. At T=2 the lifted brick
   excludes only the extra far seam in the coercivity construction, not a
   degree of freedom in the actual matrix. Coarse gradients and harmonics
   have zero Schur value; they do not justify deleting fine determinant modes.

2. **Fourier phases, aliases and infrared units, target lines 151-242.**
   Endpoint cancellation gives `Q_root=Q_str-d_c h_ax`. Conversion from
   tail links to midpoint links multiplies the straight symbol by
   `exp(-ip_mu/2) exp(iLq_mu/2)`, giving the displayed alias sign
   `(-1)^K_mu`. The extra `d_L(q_mu)` is required. Since
   `S_K hat q_K=D_L(q_K) hat p`, the fine longitudinal projector disappears
   only after the coarse transverse projection. Unitary fine/coarse Fourier
   sums contribute `L^-4` to the covariance. The zero-alias residue is
   `L^-4 L^2 L^2=1`, per colour. On an axis, differentiating the cotangent
   partial-fraction identity gives
   `sum csc^4(x+pi k/L)=L^4 csc^4(Lx)-(2/3)L^2(L^2-1)csc^2(Lx)`.
   This independently yields BM11's negative constant `-(1-L^-2)/6`.
   Thus the unit infrared coefficient is correct and does not identify
   the full symbol with Wilson. The physical integrated-link conversion
   cancels exactly in four dimensions.

3. **Finite-u coordinate-density action, target lines 246-308.** The relative
   coordinate is `a`, while the linear absolute field is `a+EB`. Every
   contour of EB equals B; hence `QE=I`, `B_sp E=0`, and the kernel has
   no mixed a/B term. The Haar Hessian acts on a alone. The exact precision
   is `K_u=K0+kappa(1-c_N)B_sp+N^2/(6u)I`. Eliminating a in this coordinate
   gives BM13, not an absolute-field mass. The identity
   `K0^-1-K_u^-1=K0^-1(K_u-K0)K_u^-1` proves BM14, with positivity obtained
   from inverse order rather than an invalid product-of-positive-matrices
   argument. FK18/FK24 give `u(K_u-K0)=D B_sp/2+N^2 I/6+O(u^-1)`.
   The local forcing vanishes at zero coarse momentum. Its O(P) factor on
   both sides pays the division by `lambda_P`, with a volume-independent
   gapped inverse and the finite stencil counts in lines 298-308.

4. **Actual axial tree and crossing count, target lines 310-360.** For a<b,
   start from `A_a=-x_b F/(2L^2)`, `A_b=x_a F/(2L^2)`. The increasing-order
   root path has the bilinear term `y_a y_b F/(2L^2)`. Subtracting its
   gradient makes internal b-links zero and every owned a-link equal to
   `-y_b F/L^2`. At a b-face the root moves by L and y_b changes h to -h;
   subtracting the brick field leaves `y_a F/L` there. This reproduces
   BM16, including the easily missed factor L on b-crossing links.
   The two square sums are `s_L^2` from L^4 a-links and `L s_L^2` from
   L^3 b-crossing links; tree links among them have zero values. Paired
   contour fluctuations give `2s_L^2/L^2`. In FLOW coordinates the leading
   action coefficient is consequently
   `(L^2-1)[D/(12L^2)+N^2(L+1)/72]`.
   This is a local infinite-lattice affine test identified by summable
   kernels, not an illicit affine field on a periodic torus. It is an
   action-coordinate contribution and is not itself a physical loop coefficient.

5. **Fixed-domain full-prefactor comparison, target lines 364-438.** FK's
   entire compact-cycle Laplace argument, including the SU scalar constraint,
   gives a uniform remainder on a fixed complex domain. IC129-314 and
   IC586-731 explicitly construct the row/column plus full-marked inverse,
   the critical fields and the trace-log family there. The required order
   is local radius/gap, fixed geometry R, then contraction/curvature/coarse
   radii, then u. The stationary tree action increment is quadratic in
   `b_u-b_T=O(sigma^2)`, so division by sigma^2 leaves O(sigma^2).
   The scalar contraction has the matrix mark and both vector marks.
   In the determinant series the j choices of marked factor cancel 1/j.
   These are connected coefficient bounds with coefficient suprema inside
   the sums, not total-volume or operator-only estimates. All scalar vacua
   in BM21 survive. Filling R-boxes into original cells and reducing beta0
   as in BM22 is valid; no arbitrary microscopic rate is supplied.
   FU54-400, CA27-237 and CD50-361 agree on the actual phase and common
   uniqueness ball when their fixed domains are intersected.

6. **Haar/precision conversion and symmetry, target lines 440-454 and
   521-558.** The exponential differential has determinant j_N, not its
   square root. Stationarity removes the second-coordinate-differential
   term, so the Hessian determinant gains `(product j_N)^2`, which
   cancels `-sum log j_N` against its half-log. IC30-31's quotient identity
   also retains the root-pinned gauge Gram with the correct denominator.
   Root-tree product Haar factorizations induce a Haar-preserving change
   of free-group coordinates; this gives the leading intrinsic Gamma_1
   its spatial symmetry. It does not make the finite-u critical density
   point invariant under nonlinear coordinate changes. The target explicitly
   avoids that false conclusion and uses beta_av for the exact P_u.

7. **Readers to unweighted moments, target lines 458-539.** Two FLOW-unit
   directions have HS norm sqrt(N). Two Cauchy circles of radius
   `rho0/(4sqrt(N))` give `16N/rho0^2`, even on one link. Connected support
   of |Y| original cells has at most `8D|Y|` scalar inputs and the relevant
   squared distance is bounded by `(8|Y|)^2`. Their product is
   `2^13 N D rho0^-2 |Y|^3`; `|Y|^3 <= 6 beta0^-3 exp(beta0|Y|)` fits
   below BM25's `2^16 N D/(rho0^2 beta0^3)`. The exponential variant has
   the stated `2^8 N D/(rho0^2 beta0)` cost. No sigma-sized Cauchy radius
   is used. The actual local patch/word construction supplies a common
   infinite-volume limit: a word detecting a closing seam must carry a
   long connected reader and its Hessian tail is exponentially small.
   Gauge covariance and the vanishing identity gradient give the Ward
   identity. Analyticity then forces Pi(0)=0; diagonal axis parity removes
   the first derivative. Thus division by lambda_P is legitimate after
   the volume limit. Flat holonomy/winding responses have not been dropped
   at finite T.

8. **Extraction and the complete unevaluated trace, target lines 507-608.**
   The theta average is `epsilon^2 Pi_mu mu(P e_nu)/4` per cell at field
   order two, giving exactly beta[Wilson]=1 under BM26. Each axis coefficient
   is bounded by the second moment (in fact the diagonal Taylor factor
   supplies 1/2). Applying this separately to Gamma_1 and E_pref proves
   `u'_pref=u+b1+O(u^-1)` on the stated fixed domain. Twice differentiating
   `Tr log K` gives `Tr(K^-1 K''-K^-1 K' K^-1 K')`; the factor 1/2 of
   LogDet cancels BM26's factor 2. Differentiating the full stationary
   equation gives each of BM29's b', b'', K' and K'' terms, including the
   critical-field motion. The trace runs over all d modes. Its value and
   sign have not been evaluated or supplied from a universal coefficient.

## Boundaries and imports

The fixed SU(N) Wilson/arithmetic-kernel model, odd L, probability Haar,
coordinate metric, integrated-link units and volume-first extraction are
explicit definitions/normalization and boundary conditions. They are not a
derivation of this dynamics from the repository's physical axioms. No Planck
scale, realized-state choice, fitted physical coupling or numerical one-loop
coefficient is an input to the checked mathematics. No physical primitive is
newly adopted. The minimum-axiom memo and primitive-registry procedure/data
were read solely to enforce this distinction.

The needed mathematics is supplied locally and reconstructed above. Primary
arXiv records for Bietenholz-Wiese hep-lat/9510026v2, Luescher-Weisz
hep-lat/9504006v1, and Dimock 1410.2798v3 were checked only for identity,
abstract and attribution context. No equation-level or full-paper read is
claimed by this reviewer, and no external paper lemma is a premise here.
Bałaban and Dimock retain the architectural credit stated in the source.

The target deliberately proves a projection of the critical prefactor.
It does not prove that this is the coefficient of the entire normalized cut
integral. WR684-803 confirms that its small-return norm excludes the actual
transported prefactor. The weight h=O(sigma) loses h^-2 in unscaled field-order
-two extraction; its O(sigma^2) bound alone gives only O(1), not o(1).
The target's O(u^-1) prefactor error instead uses its own fixed rho0.
The non-Wilson order-u symbol remainder, nonlinear effective-action class,
source/history return, iteration, continuum existence, non-freeness and
physical continuum mass gap are not discharged. Both physical targets remain
OPEN. No recursively complete upstream-DAG review is claimed.

No mathematical source, shared front, ledger or audit output was edited.
No scientific/numerical runner, subagent, Git write or fetch was used.
The only generated files so far are this findings record and its read record.

Source-only freeze time (UTC): 2026-10-30T13:07:04.529384+00:00
