lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T12:38Z

# Check of library/ol.md round 4 (OL-transfer)

Provenance: Claude Opus 5.5, max effort, Mac mini worker, checkout 58c890225, 2026-11-06. One line-by-line reading by one model. Not an audit; grants no status.

Moves: row 339, the Gaussian supplier of CA-I 4.2:lem-one-loop (hypothesis (b) of 4.19:prop-clause-zero) and the absolute interval bound read by CA-II 5.14.

Status: in progress. Sections are written as the check proceeds.

## 1. c_0 against the account's normalization (settled)

Verdict: CORRECT. The value c_0 = (11 N^2/(12 pi^2)) log L in the Result is the account's c_0 (CA-I 634-636, 3897-3899), and it agrees with the textbook coefficient.

Sources read: CA-I 606-680 (couplings, flow constants), the Wilson action definition (1.1:def-wilson-action), 3764-3926 (increment, definitions before Lemma 4.2, the lemma), 3928-4029 (outline of (b)); ol.md §2.1, §2.3-2.4, §3.

1. The bare density is exp[-g_0^{-2} sum_p (1 - Re tr U(dp))] with tr 1 = 1 (CA-I 1.1:eq-wilson-action-2, -4). The usual Wilson form is beta_W sum_p (1 - N^{-1} Re Tr U_p) with beta_W = 2N/g_std^2, where Tr(T_a T_b) = delta_ab/2. Since tr = N^{-1} Tr, the account's x = g^{-2} is beta_W:
   g^{-2} = 2N g_std^{-2}.
2. Textbook: mu dg_std/dmu = -b_0 g_std^3, b_0 = (11N/3)/(16 pi^2). So d(g_std^{-2})/d log mu = 2 b_0 = 11N/(24 pi^2).
3. Hence d(g^{-2})/d log mu = 2N * 11N/(24 pi^2) = 11 N^2/(12 pi^2). One step changes the scale by L, which gives c_0 = (11N^2/(12 pi^2)) log L. Check at N = 3: 33/(4 pi^2) per unit log, the known one-loop running of beta_W = 6/g^2.
4. The account's second route agrees. In the basis t_a = sqrt(2N) T_a, orthonormal for <X,Y> = tr(XY), the action is (1/(4g^2)) sum_x sum_{mu nu} F^a F^a. Then d(g^{-2})/d log mu = 11 C/(24 pi^2), with C the Casimir in that basis. This form does not change when the inner product is rescaled. ol.md §2.1 computes C_g = 2N^2 by hand from the completeness identity sum_a (t_a)_ij (t_a)_kl = N d_il d_jk - d_ij d_kl. I rechecked that identity, sum_a t_a^2 = (N^2-1)1, sum_a [t_a,[t_a,X]] = 2N^2 X, and (2.2): sum_{i<j} lambda_ij^2 = N^2 for t = sqrt(N/2) diag(1,-1,0,...). All hold.
5. The extractor is normalized so that b[g^{-2} A] = g^{-2}. For the unit-lattice Wilson action, the bond Hessian Pi_{mu nu}(u), mu != nu, is +1 at u = -e_mu and u = e_nu, and -1 at u = 0 and u = e_nu - e_mu. Only u = e_nu - e_mu has u_mu u_nu != 0, and it gives sum_u u_mu u_nu Pi_{mu nu}(u) = (-1)(-1) = 1. So beta^0 is an increment of x = g^{-2} in the same units, and x_{k+1} = x_k - beta_{k+1} (CA-I 1.2:eq-couplings-1) has the asymptotic-freedom sign for beta ~ c_0 > 0.
6. The table in ol.md §2.3 (spin 4C_g, four orbital directions -2/3 C_g, ghost +1/3 C_g, total 11/3 C_g) agrees with the textbook paramagnetic/diamagnetic split 4 - 4/6 + 1/3 = 11/3. With I_2(z) = (16 pi^2)^{-1} log(1/z) + O(1) and z = eta^2, the per-log(1/eta) coefficient is 2 * (11/3) C_g/(16 pi^2) = 11 C_g/(24 pi^2), and log(1/eta) = k log L.

The constant in the Result also agrees with the account's. CA-I 4002-4006 sets c_2 = C_det + C_cmp/2. ol.md (3.14) sets c_2 = C_E + C_R + C_M with C_cmp = 2(C_E + C_M) and C_R in the role of C_det.

Notation only: row 339 writes "k c_0 log L" with c_0 = 11N^2/(12 pi^2), so there c_0 is the coefficient per unit log. In the account and in the Result, c_0 already contains log L. The Result's display, k (11N^2/(12 pi^2)) log L, is the account's k c_0. There is no factor error.
