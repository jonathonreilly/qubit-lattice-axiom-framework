# Independent reconstruction before reading the outside-chart source

This is reviewer working evidence, frozen before the new source or its packaging
was opened. It is not an independent audit, a full-PR integration decision, or
a theorem-status promotion. The reviewer is a fresh same-family Codex context;
Astra/max was requested, and that request is not backend attestation.
Both full four-dimensional Yang--Mills existence and the physical continuum
mass gap remain OPEN.

The initial coordinator brief disclosed the proposed neighborhood-growth route,
its intended probability inequality, the suggested shrinking threshold, and
specific risks. Subsequent freeze messages disclosed the new source's name,
641-line size, hash f8e5ac755f106cf9419f81d3d3f683949c59abfe4f8ad1a250795fa6ec1c58d4,
claim labels, and a short claimed scope. No new-source text, checks, author
receipt, predecessor review, or other mutable author's argument has been read.
Headers in the actual CB/SA/CS sources mention their prior review status; those
mentions were visible but supplied no mathematical premise here.

Source coverage before this freeze:

- CUT_SECTOR_COERCIVITY_ASTRA.md: complete lines 1--617, SHA-256
  4e6c70786aa4458293c4fe7294767128253477176f9eea87b7720254d62a159e.
- COVARIANT_SOFT_BACKGROUND_ASTRA.md: complete lines 1--568, SHA-256
  87119008ccf754022b5da0836bb1bea8e0455a5535e589a4207ee49193682b74.
- COVARIANT_SOURCE_ACTIVITY_ASTRA.md: complete lines 1--722, SHA-256
  da22fc28cff8f822426ccd0458959dc24668f3d8854848f8ff83dbcda9f2ba54.
- No GC, RD, H, CC, or predecessor review source was read. Their statements
  mentioned in the three actual sources remain unverified beyond the displayed
  input interfaces, unless subsequently inspected and recorded.

HEAD was ddc0515e563507c74050d9c55201abb6981d4d69 and local origin/main was
01589af3faf806b736c42dc2f3bd625e9edead9f. The latter is the selected methodology
revision, read with git show without fetching. The task prohibits Git mutations.
PROCESS_LIGHT was read completely. Installed physics-loop/review-loop entry
points were read as routers, then the selected-revision entries and applicable
references were read. Early large methodology output was truncated; affected
claim-status, discovery, delivery, review setup/units/lenses/reporting, proof
search, and axiom/primitive readings were recovered with smaller reads.

## Rebuilt conditional law and localized filling

For d=4, SU(N), N>=2, odd L>=3, T>=2, u>=1, fixed positive kappa interval,
and real |e_p|<=rho<1, use probability Haar and the actual paired mean of
24L^4 words. Root-pinned axial-tree integration leaves m0=3L^4+1 independent
Haar free links per block; it removes neither roots nor harmonic/colour modes.
The compact energy is

  E^e=sum_p(1+e_p)s(U_p)+kappa sum_c[m(M_c)-<V_c,M_c>_n].

Its nonnegative terms do not include the centered normalizer. For replacement
set R the conditional retains every touching Wilson plaquette, every touching
actual paired mean, and every Ntilde_(kappa u)(M_c)^(-1). All other factors
cancel. The original interior cuts in R remain. Conditioning is in free W,
not in the original ungauged exterior variables.

The filling can be rebuilt by elementary coordinate commutations in a lifted
block/brick: each interchange contributes one conjugated plaquette, and a loop
of length ell uses at most ell times the box-width sum. Here ell<6L and width
sum<5L, so B=30L^2 suffices. T=2 uses the labeled lifted brick and excludes the
extra far seam. Telescoping products gives the squared normalized chord bound
2B^2 sum s. Comparing the root straight word S with the arithmetic mean M,
maximality gives d^2/2<=psi+d sqrt(q), hence d^2<=4psi+4q.
The crossing free-link bound is therefore 20B^2 sum_brick s+8psi.
Summing <=4L^4 internal links per block, L^3 crossings per face, and at most
eight labeled bricks per plaquette yields exactly

  C_F=8B^2 L^3(L+20), C_psi=8L^3,
  c=min((1-rho)/C_F,kappa_-/C_psi), E^e>=c sum q_e,
  q_e=|W_e-U0_e|_n^2.

The same lower bound is local ONLY if both endpoint blocks of every charged
crossing link and each complete block/brick filling lie in R. Every elementary
plaquette there contains a free edge owned in R (a tree cannot contain its
whole cycle), and every needed kernel is then retained. Thus charge on owners
N_(2j)(A) is legal in R_j=N_(2j+1)(A).

## Rebuilt shell reference and radius mechanism

A direct sum estimate is stronger than blindly inserting a shell maximum in
CS27. Replace all J_R links by U0. Let S be the sum of q_e over all exterior
free readers in N_1(R) minus R. A reference plaquette satisfies

  s(P_ref)<=|I-P0|_n^2+4 sum_(exterior occurrences) q_e,

and an actual word satisfies

  |P_word,ref-V_c|_n^2/2 <=(p_L/2) sum_(exterior occurrences)q_e,
  p_L=5L.

A free link occurs in six plaquettes. For the word estimate a conservative
bound counts at most eight mean labels and at most p_L occurrences in each
word, with the arithmetic average retained. Therefore a sufficient bound is

  A_ref <=a delta_V^2 |R|+C S,
  a=6(1+rho)m0,
  C=24(1+rho)+4kappa_+ p_L^2.

No small boundary or normalization cancellation is assumed. CS25 keeps the
Haar cap exponent D(m_R+k_R)/2, all scalar constants, and subtracts the paid
(1+zeta)A_ref. The cap lies in the original cut because interior plaquettes
are identity at U0 and move by at most four HS link radii.

For any nonempty prescribed owner set A with sum_(owned e)q_e>=q_* at each
owner, put Q_j=sum_(owners in N_(2j)(A))q_e and let S_j charge the outer shell
N_(2j+2)(A) minus N_(2j+1)(A). Then Q_0>=q_*|A|,
Q_(j+1)>=Q_j+S_j, and Q_K<=4m0(4K+1)^4|A|. If all S_j>theta Q_j,
then Q_K>(1+theta)^K q_*|A|, impossible when K is chosen so this exceeds the
compact polynomial bound. This K is independent of A, volume and u at fixed
q_*. Periodic identification only decreases neighborhood counts. When the
replacement region is the torus, the shell is empty and success is automatic.

For example take zeta=1, theta=c/(8C), and
  a delta_V^2(4K+3)^4<=c q_*/8.
At a successful radius A_ref<=c Q_j/4. But S_j<=theta Q_j is NOT an exterior
condition: Q_j varies under the conditional. The proof must instead use the
fixed-exterior threshold
  Q_j >=max(q_*|A|, S_j/theta),
and the constant bulk bound above. On that event the exponent retains at
least c q_*|A|/2 after reference payment. Summing over the common K radii
costs K, not a selection of K independent radii at every owner. It can be
absorbed as K<=K^|A| if the final coefficient is written b(u)^|A|.

An exterior insertion must be measurable in the complement of the UNION of
all possible replacement free coordinates. A claimed support label should
also contain each full Wilson/mean/coarse/source reader, one extra block
collar beyond the largest R. No arbitrary insertion reading an integrated
link may be called exterior. A source-independent cover is available because
q_e, shells, theta and bounds use V and the fixed rho, never the varying e.

## Rebuilt dependent avoidance and reference directions

A singleton estimate against every nonnegative function of distant free
coordinates implies the needed lopsided conditional estimate for avoidance
of distant owner events. No probabilistic dependency graph is assumed.
Let Gamma(x) include every owner whose event reads the replacement set for x.
If its degree is at most d and b<=x(1-x)^d, induction over the size of the
conditioning set proves P(E_x | avoidance of S)<=x: split S into near/far,
bound the far-conditioned numerator by b, and lower-bound the near-avoidance
denominator by (1-x)^d using smaller conditioning sets. Hence
P(all owner events avoided)>=(1-x)^(T^4). Choosing x=2b is sufficient when
b<=1/[4(d+1)]. This is a real positive-law statement.

For a chart conclusion, avoiding defects must actually imply that each
relative link has a unique traceless logarithm in the HS r_ch ball. The mere
existence of a matrix principal logarithm is insufficient for SU(N). One
sufficient threshold is q_*<4r_ch^2/(pi^2 N), with r_ch<pi/sqrt(N): first
q_*<4/N excludes the eigenvalue -1; then principal-log HS norm is bounded by
(pi/2)sqrt(N q_*)<r_ch, and its eigenangle sum has absolute value <pi, forcing
trace zero. Thus avoidance is a SUBSET of the chart and
  1<=Z_cut^e/Z_(cut,chart)^e <=(1-x)^(-T^4).
The extensive power cannot disappear.

For the actual SA cube, all q_e small must also imply
||sigma^(-1)K_*^(1/2)(a-b_0)||_infinity<=p with complete scalar row norm M_T.
Sufficient choices are q_*<=p^2/(pi^2 M_T^2 u) and
C_b delta_V<=sigma p/(2M_T), plus the independent chart condition above.
These give each log HS norm <=sigma p/(2M_T). The scalar-to-link conversion
and all colours remain in the row norm and q conversion. The original
SA15 fixed b_0,C_0,cube and original G/cut remain unchanged. Only then does
the same avoidance lower bound yield Z_cut^e/Z_sec^e<=(1-x)^(-T^4).
No Gaussian replacement or extra Haar factor enters that inequality.

For q_* of order p^2/u, K=O(log u) is available. The reference bulk budget
then requires delta_V=O(sigma p/K^2), with fixed N-dependent constants.
The resulting log b bound can be C(log u)^5-c' p^2. Suppression requires
p^2 dominate (log u)^5; the older alpha>1/2 observation for fixed local
regions does not suffice for this enlarged support. Such p can still obey
sigma p^3->0 and the source condition rho p^2 small.

## Binding limits for the upcoming source review

The core real bound appears mathematically feasible under the displayed
restrictions. This is a reconstruction, not a verdict on an unseen source.
The review must check the author's exact constants, threshold measurability,
reader radii, chart qualification, avoidance induction, and inequality
orientation. Returned-history extensions require the actual complete failure
reader condition and oscillation bound; they cannot be inherited as blanket
avoidance estimates. Complex absolute values can only compare with the real
Re(epsilon) law and cannot divide by a possibly zero complex denominator.
An interacting real probability estimate does not instantiate a product-
reference L1 activity theorem, establish connected analytic complement
activities, or prove either full continuum target.
