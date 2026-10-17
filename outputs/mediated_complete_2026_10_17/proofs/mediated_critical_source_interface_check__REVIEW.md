# Distinct check of the mediated critical-source interface

Disposition: **the integer-length ratios, fixed-port gauge and finite-energy mediator formulas are supported; one port-installation convention requires correction before the claimed unchanged-background construction is accepted.** The literal instruction to add the proposed path terms to the already capped emitter-free background double-counts its retained j n_p term. The intended positive construction is obtained by replacing that cap, as specified below. This is a stationary interface only. No dressed preparation, source concentration, linewidth, complete output or temporal performance is established.

The complete reviewed target is `mediated_critical_source_interface/PROPOSAL.md`, 14,157 bytes, SHA256 `2972451d77aae751d5cf64c7022468e372d078a5bfda36b7a9c7b8477036596e`. I did not author it or the isolated bipartite mediator proposal. I have authored and checked related source, phase, full-fiber recovery and temporal-composition ancestors. This is a distinct, exposed analytical reconstruction, not blind review or independent recertification of those ancestors. The isolated mediator source and its distinct root review were both read completely. The actual source-port convention was checked against the complete three-site attachment/check and the explicit two-site attachment passages defining H_bg.

## 1. Required port correction

The reviewed proposal says to start with the “unchanged emitter-free processor Hamiltonian” already retaining its original j n_p contribution, then add the mediator bonds and (j-gamma3)n_p. The referenced attachment defines H_bg by **principal compression**, including the endpoint occupation left by the removed source block. Its port already has diagonal 2j: j from the unchanged input bond and j from that retained cap. This is explicit in `two_site_actual_attachment/PROPOSAL.md`, sections 2–3, and in the three-site check's diagonal and compression calculations.

Let H_path denote all the newly listed mediator/source Q blocks and occupations, including the proposed port occupation. Compression off every new source and mediator head gives

    P H_path P=gamma3 n_p+(j-gamma3)n_p=j n_p.

Consequently literal addition to the checked background yields

    P(H_bg+H_path)P=H_bg+j n_p,

and a port diagonal 3j, not 2j. The physical zero-energy background and its G kernel are then changed. This discrepancy is not a small finite-energy self-energy or an allowed common scalar; it is an additional port occupation.

The precise intended replacement is:

    remove the existing retained port cap j n_p;
    install the proposed path bonds and all its stated occupations;
    retain the original input bond and every other background term.

Equivalently, as bookkeeping on the enlarged one-head space, use the uncapped base H_bg-j n_p and the proposed H_path, with the unchanged shared internal/scalar terms extended once. Then

    P[(H_bg-j n_p)+H_path]P=H_bg,
    port diagonal=j+[gamma3+(j-gamma3)]=2j.

Removing the old positive cap is an installation replacement; it does not require a negative physical occupation block. In a full positive decomposition the uncapped base is obtained by omitting that old cap, and all newly installed blocks remain positive. If the author intended “original j n_p contribution” to mean only the input bond's contribution, the starting operator must be named the uncapped base rather than the checked H_bg. Either explicit formulation resolves the issue. The abstract mediator formulas and ratios below do not depend on this wording, but their advertised reuse of the old background does.

No original source was changed in this review. Root was notified of this discrepancy and agreed that literal double-addition must not be supported. The following installation conclusions are conditional on the replacement convention just stated.

## 2. Lengths, ratios and fixed physical phases

Write J_med for the target's mediator strong-bond symbol J in this review. It is a newly supplied mediator coefficient. All formulas and the constraint J_med+q<=2j<.006 refer to that local coefficient; no identification with a processor coefficient of the same name is derived or required.

Each mediator has 2n_l internal vertices, with n_l strong bonds and n_l-1 weak bonds. Its zero-energy off-diagonal self-energy is

    t_l(0)=(-1)^(n_l-1) gamma_l^2 q^(n_l-1)/J_med^n_l.

For n1=n2=2m-1 and n3=m, m>=1, the first two signs are positive and the third is (-1)^(m-1). Their exponents are 2m-2, 2m-2 and m-1. With r=q/J_med and

    lambda_m=sqrt(3) gamma1^2 r^(2m-2)/J_med,

the first magnitude is lambda_m/sqrt(3). The supplied ratio gamma2/gamma1=8^(1/4) makes the second larger by sqrt(8), hence lambda_m sqrt(8/3). Finally

    |t3(0)|^2
      =(gamma3^4/J_med^2) r^(2m-2)
      =3j lambda_m

uses exactly gamma3^4=3sqrt(3)j J_med gamma1^2. The powers and dimensions agree. The correlations are supplied coefficient identities, not consequences of increasing length. Successive m values multiply lambda_m by r^2; selecting even m only multiplies successive allowed values by r^4. An arbitrary prescribed positive lambda is not thereby available.

Fixing g_p=1, the stated endpoint signs give

    g_s2 sign(t3)=-1,
    g_s1 g_s2=-1,
    g_s0 g_s1=-1.

Thus conjugation by G_end makes all three selected bandcenter Hamiltonian hoppings negative. The m=1 case has three positive Schur entries and endpoint signs (-,+,-,+) in source-to-port order; it satisfies the same rule. There is no missed endpoint exception.

If the canonically signed endpoint vector is |s0>_can=g_s0|s0>_phys, then the physical seed is (-1)^m|s0>_can. The fixed port has no compensating sign. Therefore a seed-to-port amplitude in the physical basis is (-1)^m times the canonical negative-hop amplitude, before accounting for the other physical phases. This sign must remain in any eventual phase-sensitive target. It is not an input-dependent correction or a freely fitted phase.

Extending the coordinate gauge by identity on the mediators is a legitimate change of representation. Some endpoint-to-mediator matrix entries then change sign in that representation, while the physical implemented Q bonds remain negative hoppings. A path has no cycle consistency obstruction, but that does not erase the reference-plane or seed convention. For real |z|<a the finite-energy t_l(z) have the same signs as t_l(0), so the same fixed gauge also makes their selected-band off-diagonal entries negative. This last statement is restricted to that gap interval, not all complementary channels.

## 3. Positive blocks, equal diagonals and local counts

For Q_b=b(n_i+n_k-X_ik), the full two-qubit eigenvalues are 0,0,2b,2b. It is positive and number preserving; the double-occupation sector has energy 2b, so this is a full physical-block check rather than only a one-head matrix check. The occupation operators are also positive under the displayed coefficient inequalities.

At the retained source endpoints the sums are

    s0: gamma1+(2j-gamma1)=2j,
    s1: gamma1+gamma2+(2j-gamma1-gamma2)=2j,
    s2: gamma2+gamma3+(2j-gamma2-gamma3)=2j.

At an internal mediator endpoint the incident sum is J_med+gamma_l; at any remaining internal site it is J_med+q. For n_l=1 both internal vertices are endpoint-type, and there is no weak bond. The same sufficient inequalities cover that case. Adding the stated nonnegative occupations therefore puts every mediator diagonal at 2j. At p the corrected cap replacement gives the 2j total derived above.

Compatibility of all positivity constraints with the gamma identities is genuine. Choose fixed 0<q<J_med<2j with J_med+q<2j. Then gamma2 is a constant times gamma1 and gamma3 is a constant times sqrt(gamma1). Both tend to zero with gamma1. Hence a sufficiently small fixed positive gamma1 satisfies the finite list of strict upper bounds, including gamma3<=j and, if desired, gamma_l<=a/4. This is a conditional existence argument for supplied coefficients. It supplies no native mechanism enforcing the common onsite values, gamma correlations or bond/occupation correlations.

The occupations and Q blocks vanish on all-blank head vacuum. They add no vacuum scalar. In the one-head sector the common onsite carrier is 2j; it cannot be removed as a full-qubit scalar across different head-number sectors. The pre-existing c_att and shared B remain separate and must be retained.

The internal vertex count is

    2(n1+n2+n3)=2(5m-2)=10m-4.

Adding four distinct retained endpoints gives 10m local heads. Summing the three path edge counts gives 2(n1+n2+n3)+3=10m-1. Counting one listed occupation for every local head, including p and possible zero coefficients, gives at most 20m-1 listed positive blocks. These are local counts including the already existing port, not net new apparatus counts or a resource saving. The original cap is replaced, not additionally retained.

Disjoint interiors and an appropriate supplied nearest-neighbor embedding are essential. Concatenating the three paths gives one longer abstract path and admits a straight embedding when the required ambient sites are available. It cannot insert arbitrarily many NN vertices between the three old source coordinates while keeping those coordinates and distances unchanged. The target appropriately leaves the concrete external embedding and total apparatus inventory open.

## 4. Exact finite-energy rational functions

Let A_l be the real symmetric positive-weight internal adjacency. In odd/even order it has blocks B_l=J_med I+qS_l and B_l^T. Since ||S_l||<=1,

    ||B_l x||>=J_med||x||-q||S_l x||>=a||x||,
    a=J_med-q>0.

Its singular values sigma_l,r are at least a, and A_l has eigenvalues +/-sigma_l,r. For C_l mapping the two endpoint coordinates to the internal ends, the physical equations with negative endpoint hoppings are

    (zI+A_l)chi=-gamma_l C_l psi,
    z psi=-gamma_l C_l^T chi.

They give z psi=Sigma_l(z)psi with the positive self-energy sign stated in the target. In the resolvent Schur matrix E-H this contribution is subtracted: zI-Sigma_l(z). References to “added diagonal” must be understood as additions to the energy-dependent effective Hamiltonian, not positive additions to E-H.

Reflection interchanges the internal ends, so their diagonal resolvent entries agree. The bipartition reverses the sign of A_l. It follows that the diagonal part s_l(z) is odd and the off-diagonal part t_l(z) is even, throughout the pole-free complex disk. This is an exact algebraic symmetry, not a real-axis approximation.

For the tridiagonal internal path, the opposite-end cofactor is the nonzero constant

    -J_med^n_l q^(n_l-1).

Meanwhile

    det(zI+A_l)=product_r(z^2-sigma_l,r^2),
    det A_l=(-1)^n_l J_med^(2n_l).

Dividing the off-diagonal inverse at z by its value at zero yields exactly

    t_l(z)/t_l(0)
      =product_r(1-z^2/sigma_l,r^2)^(-1).

This verifies the determinant ratio, including its sign. For n_l=1 it reduces to t_l(z)=(gamma_l^2/J_med)/(1-z^2/J_med^2), an explicit check of both the numerator and denominator convention. For real |z|<a every factor in the denominator is positive and at most one, so the ratio is real and >=1.

The inverse expansion is

    (zI+A_l)^-1=A_l^-1-zA_l^-2+z^2A_l^-3-... .

The endpoint diagonal of A_l^-1 vanishes. Applying A_l^-1 to either internal end gives successive components J_med^-1(-q/J_med)^r on the opposite sublattice, proving

    d_n=J_med^-2 sum_(r=0)^(n-1)(q/J_med)^(2r),
    s_l'(0)=-gamma_l^2 d_n.

For complex |z|<=w<a, ||A_l^-1||<=1/a and the Neumann series converge in operator norm. The resolvent identity yields gamma_l^2|z|/[a(a-w)] for the whole self-energy difference and hence for |s_l(z)|. The even off-diagonal difference begins at order z^2; summing a looser full geometric tail gives gamma_l^2|z|^2/[a^2(a-w)]. The odd diagonal remainder after -gamma_l^2 d_n z begins at order z^3 and is bounded by gamma_l^2|z|^3/[a^3(a-w)]. Finally genuine differentiation gives Sigma_l'=-gamma_l^2 C_l^T(zI+A_l)^-2 C_l and norm <=gamma_l^2/(a-w)^2. All five displayed absolute envelopes are valid; no norm inequality has been differentiated.

For the relative bound, expand the product inverse in z^2. Its coefficients are nonnegative real sums of products of sigma_l,r^-2. The absolute sum of its nonconstant terms is therefore at most its value at w^2 minus one, and then at most

    (1-w^2/a^2)^(-n_l)-1.

This argument also covers complex z. It does not divide an absolute O(gamma_l^2) error by the exponentially small t_l(0). It is a finite-length bound whose useful smallness still requires a bandwidth/length condition. In particular the target makes no uniform small-relative-error assertion as m tends to infinity with fixed w>0.

## 5. Shared endpoints, full fibers and the remaining ordered matrix

The internal mediator ranges are disjoint, so eliminating their direct sum adds their self-energies on shared endpoint coordinates. This gives exactly the effective-Hamiltonian diagonal

    diag(s1, s1+s2, s2+s3, s3)

and off-diagonal entries t1,t2,t3 in endpoint order s0,s1,s2,p. Shared endpoints do not justify treating the three complete cells as independent systems, but they do justify this additive Schur contribution from disjoint eliminated interiors.

The fiber extension requires the additional physical premise that the same B acts while the head is at every mediator site, with no new contacts. Then the internal operators are D tensor I+I tensor A_l, where D=(E-c_att-2j)I-B. The resulting s_l(D) and t_l(D) are functions of the same D and commute with one another. They need not commute with the actual processor kernel G(E).

The relevant selected condition is d<a. It is not implied by positivity alone and is correctly kept as an additional bandwidth condition. On complementary channels, the inherited |x|>=.185 and J_med+q<=2j<.006 give

    dist(-x,spec A_l)>=|x|-(J_med+q)>.179,
    ||(xI+A_l)^-1||<1/.179.

Thus bare internal mediator poles are absent on these windows. This does not control zeros after endpoint/background loading. The complementary self-energies are their actual real functions at x, and generally are neither their bandcenter values nor subject to the selected sign statement.

An explicit ordered description makes the missing bridge clear. With the corrected background convention, define, only where the indicated inverse exists,

    G_tilde(E)=V_p^*[E-H_bg-V_p s3(D)V_p^*]^-1 V_p.

Where the equivalent finite-fiber inverses exist, the resolvent identity gives

    G_tilde=(I-G s3)^-1 G=G(I-s3 G)^-1.

No commutation is used. Eliminating this loaded background leaves the following exact three-source E-H Schur operator in the original physical endpoint signs:

    [ D-s1(D)           -t1(D)                         0             ]
    [ -t1(D)            D-s1(D)-s2(D)                 -t2(D)         ]
    [ 0                 -t2(D)     D-s2(D)-s3(D)-t3(D)G_tilde t3(D) ].

The two t3 factors retain their positions. At the real windows the mediator functions are real on all relevant reference channels, but that fact does not make them commute through G_tilde. On complex continuation the repeated factor is the analytic t3(D), not an inserted conjugate-adjoint value. The fixed endpoint sign gauge conjugates this entire matrix consistently.

This display is an exact stationary identity with an explicit existence proviso, not a bound on G_tilde or on the resulting source inverse. It shows why the old constant-coefficient Q cannot simply be reused. The port acquires s3(D), source diagonals acquire different energy-dependent functions, and all three couplings vary with energy. Even at a selected D=0, complementary functions remain nonzero and can affect the selected loaded response through the actual mixing kernel. Exact selected bandcenter ratios do not imply equality of the full loaded Green operator with the nominal critical source.

## 6. Preparation and scope

The isolated-cell premise gamma_l<=a/4 bounds dressing for one cell with two isolated endpoints. Adjacent endpoints are shared here, and p is attached to the processor. The complete perturbation, low subspace and prepared-state measure are different. Neither the three isolated bounds nor their product establishes a preparation estimate for this apparatus. In particular attaching a continuum cannot preserve the isolated-cell spectral gap merely because each bare mediator interior is gapped.

The old product-seed moment formula also does not transfer. The physical first hop from s0 now has magnitude gamma1. With the retained vacuum/energy-center conditions its centered second moment is gamma1^2, rather than t1(0)^2. Thus replacing physical prefix steps by zero-energy Schur hoppings would already fail at the second moment, before the old sixth-moment calculation. Any high-energy mediator population, omitted-state norm, effective pulse or actual linewidth requires a fresh prepared-column analysis.

The claimed limited benefit is correctly identified: bipartite symmetry makes each constant endpoint diagonal self-energy vanish at the common center, so no length-dependent exponentially small diagonal counterterm is needed **at that center**. It does not remove equal onsite matching, ordinary occupation compensation, algebraic gamma correlations, graph installation, fixed signs, gap and bandwidth conditions, or full-fiber loading/preparation obligations. It does not show arbitrary continuous tuning, a native supplier, reduced complete resources, irreversible capture or permanent halt.

No new source variant, late addendum, apparatus tolerance theorem or temporal operating point was imported into this check. The source remains a conditional stationary construction after the port replacement is made explicit. The required next mathematical bridge is an actual full loaded-matrix and prepared-state estimate for this energy-dependent interface, not another substitution of its zero-energy ratios into the earlier runtime theorem.

## 7. Evidence and exposure limits

All target-listed source identities were verified against actual bytes. The extra two-site attachment pin was verified because it explicitly defines the retained cap and H_bg. The complete target, isolated mediator source/check and three-site attachment check were read in this task; the necessary two-site port passages were read in full. The unchanged three-site attachment source and ordered-inverse source/check were reused from immediately preceding complete reads at their verified hashes. I did not rerun their science or claim a new independent check of the original physical calibration.

Only text inspection, analytical reconstruction and deterministic hash bookkeeping were performed. No spectrum calculation, dynamics, sweep, numerical quadrature, scientific source execution, original-source edit, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this review was written. It gives no retained-status or audit verdict.

Paths are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

| Source | SHA256 |
|---|---|
| mediated_critical_source_interface/PROPOSAL.md | 2972451d77aae751d5cf64c7022468e372d078a5bfda36b7a9c7b8477036596e |
| bipartite_mediator_supply/PROPOSAL.md | 836caee25d87e31c757e8965b4de85d5998a613dcc5862072d6cddc2a380c8dc |
| bipartite_mediator_supply_check/REVIEW.md | 78af05b19696d2cae2cf147c1e666c9c1a39ca0a2ba9c67a8d1746c12c72de8f |
| three_site_actual_attachment/PROPOSAL.md | 4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006 |
| three_site_actual_attachment_check/REVIEW.md | ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d |
| two_site_actual_attachment/PROPOSAL.md | 2c0e8fe8dac3dd70f50fbc945aa0fd29a5eacbac63468ff5983cc7abd5343f49 |
| three_site_loaded_inverse/PROPOSAL.md | 7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672 |
| three_site_loaded_inverse_check/REVIEW.md | 8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2 |
