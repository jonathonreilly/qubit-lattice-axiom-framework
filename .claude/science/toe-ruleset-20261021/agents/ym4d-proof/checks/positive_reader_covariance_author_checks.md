# Author-only algebra checks for the positive reader covariance

These are written checks by the author, not an independent review, a numerical
experiment, or an audit. They check the complete construction in
../POSITIVE_READER_COVARIANCE_ASTRA.md. No sampled matrix is used to certify the
actual Yang--Mills Hessian, and no numerical runner was launched.

1. **Zero-extension identity and sign.** With J_A the coordinate injection and
   D_A^chi the diagonal cutoff (not the positive matrix component),
   chi K J_A=chi J_A K_A because every nonzero row of chi lies in A. Thus
   chi K G_A chi=chi^2, while K chi=chi K+[K,chi]. Summing chi^2=I yields
   I-KP=-sum[K,chi]G_A chi. Right multiplication by (I-Rcal)^-1 gives
   K^-1=P(I-Rcal)^-1, in that order. The collar ensures the residual's
   endpoints lie in A; it is not needed to erase a boundary error.

2. **Positive whole components.** For real data, the principal compression
   spectral interval is [gamma,B], so G_A-c0 I_A>=c0 I_A when c0=1/(2B).
   The congruence by the scalar cutoff preserves positivity. Sum chi_A^2=I
   gives the exact c0 I remainder. The theorem weakens each entire
   full-colour component D_A, never its individual entries.

3. **Endpoint sums versus operator norm.** The residual row pays <=2J
   differences for each K-neighbor pair; the residual column pays <=J
   nonzero final cutoffs. The per-patch estimate is C_chi r0 b_abs g/R.
   The entrywise sup envelope b_abs explicitly pays vK=n0*5^4. Without it,
   a bound on sup_V sum_j |K_ij(V)| would not automatically justify a sum
   of entry suprema. The final source uses the larger valid envelope.

4. **Marked incidence and all colour factors.** A label contains <=s_R
   cells and thus <=n_R=n0 s_R scalar rows. A fixed mark belongs to <=J
   labels. Apply the per-patch bound before this sum. The geometric J is
   independent of R,T; n_R is finite but may be large. Products retain a
   shared scalar index in successive labels, giving connectivity and the
   two-term marked algebra with both row and column norms.

5. **Smallness order and symmetry.** With beta=1/s_R, exp(beta s_R)=exp(1)
   is fixed before choosing R. Therefore p and C_R are independent of R.
   Choosing r<=min(1/4,c0/(32p)) gives p r/(1-r)<=c0/24<c0/16. Transposing
   an atom exchanges its row/column bounds; symmetrizing with factor 1/2
   preserves those bounds and the exact symmetric sum K^-1-P. Independent
   weakening is applied after that symmetrization.

6. **Small tori and real/complex distinction.** For T<16R, one whole-torus
   patch has chi=1, P=K^-1 and Rcal=0; its support and scalar mode counts
   are still <=s_R and n_R. On complex coarse data, the local core is
   compared to its real positive value by the resolvent identity. Its
   change costs <c0/8, residual atoms <=c0/16, leaving >=13c0/16. No
   complex PSD assertion is made. Re C^-1=C^{-*}(Re C)C^-1 supplies the
   weaker precision constant a_C/U^2; the old PS gamma is not reused.

7. **Complete-reader endpoint test.** Any spanning tree on a label that
   meets two partition parts has a crossing edge. Setting all crossing
   variables to zero removes the whole matrix atom, including diagonal
   entries that read outside their owner's part. Each surviving covariance
   block then uses only actual data in its own part. The principal matrix
   logarithm is a direct sum there, so the exact normalized Gaussian
   density factors, not merely its exponent. Hard histories do not thereby
   acquire local factorization.

8. **Derivative and rate restrictions.** Ordered derivative indices belong
   inside the atom sum before taking an endpoint supremum; the final PC30
   states that norm explicitly. A degree-|S|-1 monomial has at most |S|^k
   ordered derivative choices. Losing beta-beta' bounds them by
   k!/(beta-beta')^k. This controls covariance coefficients only. The full
   Gaussian density variation has (1/2)sum_ij dot C_ij partial_i partial_j;
   a subsequent forest-path choice needs its full chain rule. All chart
   surfaces and reference cancellations remain unresolved. RD R16's
   mu_0+2 input rate cannot be silently supplied by beta=(16R)^-4.

The failed sufficient estimate from PS (independently perturbing the entire
non-small inverse atom family) is not restamped as a no-go. This new argument
uses a positive local matrix core and a small residual family instead. Its
successful covariance-level calculation does not certify an integrated
probability-sensitive return theorem. A fresh hostile review is required.
