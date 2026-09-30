# Actual rotor response geometry and a fixed-source resummation

Authored discovery, September 30, 2026. These are provisional proofs and sparse controls requiring focused independent checking. They are not formal review, audit, axiom adoption, a source-law selection, or a microscopic local-limit theorem.

Three distinct statements follow from the actual compensated one-hole rotor. First, normalizable physical slab states have survival time at least a constant times their finite global B count. Second, the local exposed-star class has a bounded reward and original-output forcing estimate even though it does not reduce the dark Hamiltonian. Third, a directed moving-tube expansion converges on the ACTUAL short-time effective source ensemble at a fixed sufficiently small positive source time. It gives a source-specific algebraic inverse modulo bright forcing, and a full terminal-plus-original-mark L2 estimate for arbitrary fast-time forcing of that FIXED source preparation.

The last statement handles evolving B masks in the fast Hamiltonian rather than replacing them by static occupied components. It does not yet make the original output spatially summable. The bright remainder's spatial response, changing source preparations, unbounded electric outputs and the microscopic source state remain substantive missing pieces.

## 1. Bound sources, carrier and domains

Main was refreshed before this route and remained `30a9461ee19a49b99fa6628fe942f08e504e8903`. Selected procedures are `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The actual original compensation, pair-form, formation, fast-vacancy and commuting-electric sources are bound in SOURCE_IDENTITIES.json; their complete earlier reads and unchanged source closure are reused. The refreshed open inventory is OPEN_PRS.json. Open PR9399's connected local-generator count is credited as closest proposal context, not imported as a thermodynamic theorem. The checked connected-source proof reconstructs its required count directly from landed operators.

The closest checked arguments are the finite-global-k clipped-height theorem f0947fc4, the local sparse-dark multiplier 96c08bd2, the effective source resummation aef8e04a with focused receipt f64caacd, and the dynamic buffer theorem a978c0bd with focused receipt 0b935a1f. The old buffer theorem has a source-time-to-zero composition; this report does not relabel it as a fixed-time result. No new local-field result from the other agents is used. Their separate candidate circulation/current obstruction was disclosed during this work but is not a premise.

Use the original cubic A/B bipartition, charges q=0,+1,-1, occupation n=q², integer A-to-B rotor fields, and Gauss div E=q-1_A. Bare Omega has A+, B empty and E=0. The unsigned f_ab moves q_a from occupied a to empty b and shifts E_ab by -q_a. With F_a=sum_(b~a) f_ab and Q_a the product of occupation at the eighteen distance-two A neighbors,

    H=C+[F,F†],    C=sum_a F_a†F_a Q_a.                    (1)

On W=1, write P_h for the hole-position projection. The exact compensation cancellation gives

    P_h H P_h=P_h[F_h F_h†-sum_(a:dist(a,h)=2) F_a†F_a]P_h,
    P_c H P_h=P_c[F_c,F_h†]P_h, c!=h.                     (2)

Only shared-B paths remain in the second line. This includes negative same-hole B reshuffles, all charges, fields and compensation gates. Its block Schur bound is 19*36+60=744. Use the loose M=1092. For either ORIGINAL resolved instrument or ORIGINAL unnormalized coherent-edge instrument, separately,

    G=J†J=2*(empty B neighbors of the hole),
    0<=G<=12,  A=-i delta H-kappa G/2,  delta,kappa>0,
    S(u)=exp(uA),  ||A||<=b:=delta M+6kappa.               (3)

No new mark, measured dark label, scalar loss replacement, or independent-hole approximation is supplied. Norm estimates using G always retain the actual stack J in the output.

There are three different domains. The slab states live on the physical finite-change Z3 representation, or on a specified sufficiently large torus for each fixed slab. The exposed-star identities hold on arbitrary one-hole backgrounds on Z3 and nonaliased even tori, e.g. L>=12. The directed infinite series lives in the one-hole module of the ACTUAL short-time effective source state on Z3; it is not claimed uniformly over every all-time finite-torus sector. Finite-torus prefix statements require an explicit no-wrap bound below. No finite-spin unit selected-path amplitude is imported.

## 2. A physical slab quasimode: full residual, not only energy

Let R>=4 be even. Use coordinates (x,m=y+z,z) and the phase i^x(-1)^z. Conjugating ordinary nearest-neighbor cubic adjacency by this phase gives

    L=i(T_x-T_x^-1)+T_m(1-T_z)+T_m^-1(1-T_z^-1).          (4)

Thus L annihilates every function of m alone. Let a_R(n)=(1-(n/R)²)_+² and put, on A sites,

    f_R(x,y,z)=i^x(-1)^z a_R(x)a_R(z) 1_(y+z=0).          (5)

The restriction to A means x is even. Fill precisely the B sites

    |x|<=R+3, |z|<=R+3, |m|<=3,

except the B corner (x,z,m)=(R+3,R+3,2). Their number is

    k_R=(7R+24)(2R+7)-1=14R²+97R+167,                    (6)

which is odd. The removed corner is at least distance seven from the closed support rectangle of (5). Every B site within distance three of an input hole is therefore occupied. On EACH such input, all negative F_a†F_a terms in (2) have blocked first hops. The six diagonal returns and every positive shared-B hole move are exactly K†K, where K is A-to-B adjacency. Consequently the FULL H action on the explicitly derived charge-symmetric fiber below equals K†K f_R; no output is deleted at a slab boundary.

Here is an elementary uniform bound on its full norm. For the unrestricted one-dimensional sequence a=a_R, ||a||²>=(81/256)(R+1). Its continuum cutoff has |a'|<=4 and Lipschitz first derivative with constant8 after extension by zero. Finite differences and their support lengths consequently give

    ||(T-T^-1)a|| <=22 R^-1||a||,
    ||(1-T)a||, ||(1-T^-1)a|| <=11 R^-1||a||,
    ||(T²-2+T^-2)a|| <=92 R^-2||a||,
    ||(1-T)^2 a||, ||(1-T^-1)^2 a||,
    ||(2-T-T^-1)a|| <=22 R^-2||a||.                       (7)

For example, before rounding, the first and last bounds are
(128/9)sqrt((2R+3)/(R+1))/R and the same constant/R²; the step-two second difference has (512/9)sqrt((2R+5)/(R+1))/R². The forward first difference has (64/9)sqrt(2)/R. All quoted rounded constants hold for R>=4.

Write L=X+Y+Z as in (4). Its commuting-square expansion and (7) bound the unrestricted product in (5) by

    ||L² f_all|| <=[92+4*22*11+4*22] R^-2||f_all||
                  =1148 R^-2||f_all||.

The unrestricted/even-x norm ratio is at most4: there are at least R/2 even integers in [-R/2,R/2], each with a>=9/16, whereas the unrestricted squared norm is at most2R+1. Since K² preserves the A/B parity, restricting the OUTPUT to A removes every contribution from the odd-x INPUT. Hence

    ||K†K f_R|| <=8192 R^-2||f_R||.                     (8)

This proves a full operator residual O(R^-2), including the plane edges and every output outside the initial plane. It is stronger than a small expectation or an O(R^-1) bound for Kf_R.

For the physical embedding, take the finite connected induced graph

    Gamma_R={|x|,|z|<=R+4, |m|<=4}.

It contains all occupied B sites and all local paths used above. It is connected: move x to zero, use y to bring m to zero, then undo z with alternating z and y steps while |m|<=1. All A sites in this graph except h are occupied; outside it retain A+, B empty. For each hole h in (5) and each output pattern needed in (8), use the NORMALIZED equal-amplitude sum over all assignments of exactly (k_R-1)/2 minus charges among the occupied sites of Gamma_R. Their number of occupied sites is independent of h. Every allowed charge-preserving hop maps these assignments bijectively, with the same binomial normalization. At zero cycle angle its coefficient is one. There are no fermionic signs in the supplied occupation carrier. Relative total charge is k_R-1-2*(k_R-1)/2=0, so each such charge word has an integer Gauss flow supported in a spanning tree of Gamma_R.

Choose that tree. Every physical field with zero exterior support is its charge-dependent tree flow plus integer cycle flows. Fourier transformation of the finitely many cycle coordinates gives a torus of angles. Tree-edge hops have no phase; each non-tree edge has phase exp(plus/minus i theta_e). The preceding Dicke embedding is exact at theta=0, but that single fiber is NOT itself a normalizable rotor vector.

Choose a normalized smooth packet g_eta supported in |theta_e|<=eta in every cycle coordinate, multiplying the normalized charge/hole vector. This is a normalizable physical finite-change vector Psi_(R,eta), with every finite polynomial electric moment for each fixed R,eta. No uniform electric-moment bound is asserted as R grows or eta decreases. The complete local block formula (2), rather than an extensive global F norm, gives

    ||[H(theta)-H(0)] Psi_0|| <=1488 eta:
    19*72 eta=1368 eta for the diagonal blocks,
    30*4 eta=120 eta for the shared-B commutators.          (9)

Each elementary phase differs from one by at most eta. All relevant paths stay in Gamma_R; the same estimates apply to the full output vector. Take eta=1/(1488 R²). Then

    G Psi_R=0,  ||Psi_R||=1,  ||H Psi_R||<=8193/R².        (10)

Contractivity gives ||S(u)Psi_R-Psi_R||<=delta*8193*u/R². In particular, at u_R=R²/(4*8193delta), and at every earlier time,

    ||S(u)Psi_R||²>=9/16.                               (11)

Since k_R<=49R², u_R>=k_R/(1,605,828delta). A proposed bound ||S(u)||<=C exp(-gamma_k u) with C independent of k and fields therefore needs gamma_(k_R)<=1,605,828delta log(4C/3)/k_R. Every positive waiting-time moment p has lower bound (9/16)u_R^p on these inputs. The existing exponential-in-k upper price is consistent with this. Polynomial or subexponential improvements are NOT ruled out.

For each fixed R, an even cubic torus L>=4R+40 contains the complete construction without aliasing. L is not held fixed as R tends to infinity. On Z3 this is a finite-change vector for each R. These charge-symmetric smooth field packets are not claimed to have uniformly priced preparation under the bare-Omega source law. This is a necessary-rate discriminator, not a source-weighted local-limit counterexample.

## 3. A larger local reward without an invariant dark block

Let D=1_(G=0), B=I-D. For a hole h and each of the six unit directions d, define the five-site group

    S_d(h)=N(h+2d) minus {h+d}.                          (12)

The six groups are disjoint, lie on the radius-three B shell, and contain30 sites. Let

    P=D*1_(at least one S_d(h) has no occupied B site),
    Q=B+P.                                               (13)

Choose the first empty group in a fixed ordering and use the actual positive path f_(h+2d,h+d) f_(h,h+d)†. Its output has exactly one occupied B neighbor and therefore G=10. Call this partial isometry V. The output hole c and its sole occupied neighbor b uniquely recover h=2b-c, d, charges and fields. The all-dark inverse-row argument excludes EVERY other dark input: a same-hole reshuffle can remove at most one of six star occupants; a nonaxial alternative shared-B path would require a second occupied neighbor at c. Thus

    V†V=P, VV†<=B, GV=10V, V†HD=P.                       (14)

No bound on other occupied sites is needed.

P does NOT reduce DHD. A physical k=13 example starts at h=0, with N(0), the five sites3d for d!=+e_x, the corner(1,1,1), and the remote B site(11,0,0) occupied. The +x group alone is empty. The actual negative term at a=(1,1,0) moves the corner record to (2,1,0), with coefficient-1 and the original link shifts. All six groups then contain a record, while the central star remains full. The other common A intermediary is distance four from h and its negative term is cancelled by compensation. The exact control checks this full charge/field word. A reducing-block proof from the older N3<=9 class cannot be reused here.

There is a different storage argument. Put c=M+5kappa/delta. Equation (14) implies

    ||P psi||<=delta^-1||B A psi||+c||B psi||,
    P<=delta^-2 A†G A+c²G.                              (15)

The second inequality uses G>=2B and (a+b)²<=2a²+2b². For L(T)=A†T+TA,

    L(I)=-kappa G, L(A†A)=-kappa A†G A,
    T_P=[delta^-2 A†A+c²I]/kappa,
    T_Q=T_P+I/(2kappa), L(T_Q)<=-Q.                      (16)

These are bounded positive operators on the full one-hole space; no commutation with P is asserted. Consequently integral_0^infinity ||Q S(u)psi||²du<=||T_Q||||psi||², with ||T_Q||<=[b²/delta²+c²+1/2]/kappa. This is a partial reward, not a full lifetime bound.

A separate resolvent argument handles forcing. Let R(z)=(z-A)^-1, Re z>0, and y=R(z)f with Pf=f. Since V†f=0,

    ||P y||<=[M+(|z|+5kappa)/delta]||B y||.

For |z|<=2b use L0=3M+17kappa/delta. Passivity gives kappa||Jy||²<=2||Py||||f|| and hence

    ||P R(z)P||<=L0²/kappa.                             (17)

For |z|>2b the Neumann bound ||R(z)||<=1/b is smaller than this constant. Causal Laplace/Plancherel and the exact energy identity therefore yield, for y'=Ay+f, y(0)=0, Pf=f,

    ||y(T)||²+kappa integral_0^T ||Jy||²
                         <=2 L0²/kappa ||f||_L²(0,T)².  (18)

One may first use an exponential Laplace weight, bound Py in L², and let that weight decrease to zero; all finite-horizon mild solutions exist because A is bounded. Bright forcing separately costs2/kappa. Splitting Qf into Bf+Pf and recombining their ACTUAL output vectors coherently gives

    ||y(T)||²+kappa integral_0^T ||Jy||²
                     <=2(1+L0²)/kappa ||f||_L²(0,T)²,
    Qf=f.                                               (19)

No new observed good/bad label has been introduced.

For the actual positive-grade source B_mu^+=-F_a j_mu F_a P0, three distinct star B sites are added and no outer sites change. The new uncontrolled projection D-P therefore pulls back to

    chi6=1_(N_star=3) product_(six d)1_(N_B(S_d)>=1),
    (D-P)B_mu^+=(D-P)B_mu^+ chi6,
    sum_mu B_mu^+†(D-P)B_mu^+<=240 chi6.                 (20)

The last bound is the checked original all-field row20/stacked-column12 estimate, retaining every coherent path. It is not a lower bound or a claim that every allowed input has nonzero bad amplitude. There are at least NINE distinct pre-existing B records. Thus the effective ordinary formation grading requires at least FIVE prior gains, instead of four for the older bad projection. Its support is36 cells, so the checked connected effective source count gives

    <chi6>_t<= y^5/[(1-x)^5(1-x-y)],
    x=16641*46656delta*t, y=16641*1200kappa*t.             (21)

A factorial majorant has binom(6,3)*5^6=312,500 nine-record terms. This improves the source split; it does not discard the still nonzero dense source or price its full response.

## 4. Moving tubes for the actual directed inverse

Return to a FIXED +x selected path V on ALL dark words: h -> h+2e_x through b=h+e_x. Here V†V=D but its range need not be bright. For real lambda define, on the dark subspace,

    W_lambda=D(H-lambda)V-I_D.                          (22)

Cancel the unique exact reverse axial path giving I_D BEFORE estimating the remaining paths. This is the adjoint orientation of the checked finite-k triangularity. Every remaining nonzero elementary path starting with dark hole h ends at another dark hole h' with:

- h'_x-h_x in {1,2,3,4}, L1 displacement at most4;
- either the B mask is unchanged, or h'=h+2e_x and at most one B record is moved between two sites sharing an A;
- every tested/changed B site lies in B5(h), which has146 B sites.

The term -lambda DV also advances by two and changes no B mask. The actual charge translations and negative coefficients are retained. Formula (2) decomposes into at most684 diagonal and60 shared-B elementary partial permutations, each norm<=1. They are indexed relative to the input hole. Their controlled sums over hole positions are still partial permutations: the fixed displacement recovers the initial hole, and elementary charge/field moves are injective. After exact identity cancellation, a safe absolute coefficient budget is

    B_Lambda=M+Lambda+1,  |lambda|<=Lambda.              (23)

This is an absolute PATH budget, not an inference of an l1 budget from a bare operator norm. It follows from the explicit 684+60 terms; the looser M suffices.

Fix a nonzero length-n elementary path and let U be the UNION of its n actual B5 balls. Then |U|<=146n. Every B reshuffle has both endpoints in U, so k_U=N_B(U) is conserved along that path, despite motion/rearrangement of the occupied mask. Define the height using only this fixed union,

    Phi_j=sum_(b occupied in U) clip(h_(j,x)-b_x,-5,5).

It lies between -5k_U and5k_U. If the mask is unchanged, the six occupied star sites at h_j contribute exactly6d for hole advance d; all other summands are nondecreasing. For a same-output-hole B swap, advance two contributes at least12 and the one length-two swap subtracts at most2. The spectral term has increment at least12. Thus EVERY nonzero step raises Phi by at least6, and

    k_U>=ceil(3n/5).                                   (24)

This uses a dynamically explored tube, not an initial static component and not all of B_(4n). Spectators outside U never enter the height and cannot spoil the estimate. All charges and fields remain arbitrary.

## 5. Fixed positive source time and the correct source representation

The only source ensemble used here is the supplied leading W0 process FROM bare Omega, with its actual H4, commuting electric form and original formation operators. The checked connected proof gives on a common interval x<=1/4,y<=1/8, for every finite m-site B set Z,

    omega_t(product_Z n_b)<=(8/3) eta(t)^m,
    eta(t)=(8/3)^(1/129) sqrt(8y/3).                     (25)

This is an actual all-history quantum expectation, not an independent dilution law. Its connected proof also constructs compatible local normal limits on Z3. We use that state omega_t and its GNS representation, not a nonexistent global finite-particle density matrix at positive density.

For completeness the one-hole module in this representation is legitimate. Omega_t obeys n_a Omega_t=Omega_t for every A site. The commuting products of n_a over finite sets have strong projection limits. The mutually orthogonal projections P_h onto exactly one missing A occupation are defined by these limits. Local source vectors B_mu^+ Omega_t lie in P_a. The closure of their finite local charge/field operations with one hole is a subspace of the direct sum of the P_h ranges. The cancelled blocks (2) define a bounded self-adjoint H there by the same row/column Schur estimate744. G, the countable original stack J and V are bounded with the same identities. Physical Gauss relations hold locally; no global sum of an infinite charge density is taken. Along each finite path starting at a, the controlled global hole projections reduce to local occupation tests on that path, so all approximants below are genuine bounded local operators applied to Omega_t. Tensoring retained ancillas or keeping the original past-record representation does not change the occupation expectation or the bounds.

Let F_t be the finite-column map whose columns are the actual B_mu^+ Omega_t at one source center a, with whatever original mark register is actually retained. This column space is proof bookkeeping, not a new observation. The checked unrestricted stack estimate gives ||F_t||<=||F_t||_HS<=sqrt(4800). Define F_D=D F_t. Coherence between original columns can be retained because an operator norm is bounded by the Hilbert-Schmidt column norm; no mixture over occupation masks is assumed.

For one path in W_lambda^n, every three newly added source sites lies in its first tube ball. By (24), its input before B_mu^+ must therefore have at least

    s_n=(ceil(3n/5)-3)_+

occupied B sites in U. This is a support identity on the COMPLETE source operator, so it removes complementary coherent inputs before estimating a norm. The source4800 bound and a union bound over subsets of U, followed by (25), imply

    ||T_path F_D||_HS²
       <=12800 *2^(146n) *eta(t)^(s_n).                 (26)

When s_n=0 the probability-one bound is even smaller than the displayed expression. U is fixed by the relative displacement choices of that elementary path, not selected randomly after measuring a state. Summing the absolute path coefficients using (23), rather than declaring paths incoherent, gives for any eta(t)<=eta0<1

    ||W_lambda^n F_D||_HS <=C_* theta^n,
    C_*=sqrt(12800) eta0^(-3/2),
    theta=B_Lambda 2^73 eta0^(3/10).                    (27)

Indeed s_n/2>=3n/10-3/2, including the small-n cases after the probability-one bound. This is uniform for |lambda|<=Lambda and 0<=t<=t0. It includes every original path interference and the changing B masks.

For example choose eta0 so theta<=1/2, and fix any strictly positive t0 satisfying

    t0<=1/(4*16641*46656delta),
    t0<=1/(8*16641*1200kappa),
    t0<=eta0²/[(8/3)^(1+2/129)*16641*1200kappa].          (28)

These constants are extremely conservative. Nevertheless t0 is FIXED and positive for fixed delta,kappa; no source time is sent to zero as spatial radius grows.

The norm-convergent series

    g_lambda=sum_(n>=0)(-W_lambda)^n F_D,
    Q_lambda=V g_lambda,
    ||Q_lambda||<=C_*/(1-theta)=:Q_*,
    D(H-lambda)Q_lambda=F_D                             (29)

is now valid on the stated source representation. Uniform convergence makes Q_lambda continuous in real lambda on the compact interval. Telescoping uses ||W_lambda^(n+1)F_D||->0; no globally bounded inverse of I+W_lambda is asserted. In particular,

    F_D=(H-lambda)Q_lambda-R_lambda,
    R_lambda=B(H-lambda)Q_lambda,
    ||R_lambda||<=(M+Lambda)Q_*.                         (30)

The n-term approximants to Q_lambda and R_lambda are supported within radius4n+8 of a. Their norm errors on the source representation are at most Q_* theta^(n+1) and (M+Lambda)Q_*theta^(n+1), respectively (with an immaterial one-term indexing enlargement). This is genuine exponential spatial approximation of an ALGEBRAIC source conversion. It is not yet spatial approximation of the subsequent marked response of R_lambda.

On a finite torus, (24)-(27) are valid for the prefix n only when its entire radius4n+6 geometry is unwrapped, for example even L>8n+12 in a centered chart. The full infinite series is a Z3 source-state statement. It must not be asserted simultaneously for all n on one fixed torus; the known dense periodic approximate-dark fibers make such a shortcut particularly unsafe. The construction takes the local effective thermodynamic limit first. Finite-time one-hole dynamics on that limit is well defined by (2)-(3); all-fast-time claims below use this ordered domain.

## 6. An actual consumer: fixed-source coherent forcing, with one response price

The algebraic result has a useful consumer stronger than just a formal inverse. Freeze one t in [0,t0], its preparation and retained ancillas, and the center a. Allow arbitrary L² fast-time coefficients c(u) in the finite original source column space. Consider

    y'=Ay+F_t c(u), y(0)=0.                              (31)

This is a Duhamel response with the original H and J. It is not a replacement stochastic source or a claim that the complete microscopic forcing has this frozen-column form.

Here is an explicit horizon-independent bound. Set Lambda=2b/delta in (23)-(28), F_*=sqrt(4800), and define

    Z_*=[sqrt(4b+12kappa)+2sqrt(b)]/delta
             +sqrt(2/kappa)[M+Lambda+6kappa/delta],
    K_D=max(Z_* Q_*,sqrt(6/b) F_*),
    K_source=K_D+sqrt(2/kappa)F_*.                        (32)

For z=epsilon+i omega, epsilon>0, write R(z)=(z-A)^-1 and

    L_epsilon v=(sqrt(2epsilon)v,sqrt(kappa)Jv).

The exact passive identity gives, without a full resolvent bound at epsilon=0,

    ||L_epsilon R(z)||<=sqrt(2/epsilon),
    ||L_epsilon R(z)B||<=sqrt(2/kappa).                  (33)

For the second inequality use 2Re<y,Bf><=sqrt(2)||Jy||||f|| and ||L_epsilon y||>=sqrt(kappa)||Jy||. This is a joint terminal-damping/original-mark estimate, not merely a population estimate.

In the region epsilon<=2b, |omega|<=2b, set lambda=-omega/delta. Equations (29)-(30) imply the exact identity

    R(z)F_D=Q_lambda/(i delta)
       -R(z)[epsilon Q_lambda/(i delta)
               +kappa GQ_lambda/(2i delta)+R_lambda].    (34)

The last two terms in the bracket are BRIGHT. Apply (33), ||G||<=12, and
||L_epsilon Q_lambda||<=sqrt(2epsilon+12kappa)Q_*. It follows that

    ||L_epsilon R(z)F_D||<=Z_* Q_*.

Outside that region |z|>2b. The elementary bound ||R(z)||<=1/(|z|-b), epsilon<=|z|, and12kappa<=2b give

    ||L_epsilon R(z)F_D||
       <=sqrt(2epsilon+12kappa)F_*/(|z|-b)
       <=sqrt(6/b)F_*.

Thus ||L_epsilon R(z)F_t||<=K_source for ALL epsilon>0 and real omega, adding the bright source part coherently via (33). No extra good/bad record has been supplied.

To convert this frequency estimate, extend c by zero after a finite horizon T. Laplace/Plancherel gives

    2 Re integral_0^T exp(-2epsilon u)<y,F_t c>du
                   <=K_source² ||exp(-epsilon u)c||_L²².

Equivalently its left side is the joint passive output integrated over all fast time with the exponential weight. Let epsilon decrease to zero. The forcing integral has finite support and a continuous mild solution, so the left limit exists directly. The exact UNWEIGHTED energy identity up to T now yields

    ||y(T)||²+kappa integral_0^T ||J y(u)||²du
                      <=K_source² ||c||_L²(0,T)².        (35)

This includes the full terminal no-event amplitude and every ORIGINAL first-mark/time amplitude. Original resolved/coherent instruments stay separate. The norm is the standard proof norm for cq first-mark amplitudes; no nonexistent trace-class dephasing on a nonatomic coherent-time Hilbert space is postulated. The source columns and their cross terms are handled linearly before the norm bound.

Equation (35) is a fixed-positive-small-SOURCE-time, source-weighted all-FAST-time response bound on its precise ordered Z3 domain. It pays the moving-tube conversion once, rather than an inverse global-k gap at every ordinary source order. It is stronger than a theorem assuming the source lies in the exposed class Q. It is weaker than the requested spatially summable original-output kernel and much weaker than microscopic M4.

## 7. What the construction does not settle

The exponentially local objects in (29)-(30) are Q_lambda and its bright remainder R_lambda. Bright forcing has a uniform TOTAL passive output cost, but its spatial record distribution and unbounded field moments need not follow from that cost. It can revisit dark, dense configurations. Replacing the marked response of R_lambda by its local support would be exactly the missing dynamical step.

A concrete remaining lemma is a weighted spatial marked-transfer estimate for these actual correlated bright remainders (or a suitable two-sided weighted resolvent estimate), with a weight strong enough to sum over source centers in three dimensions, uniformly in the actual retained source preparation. That lemma is weaker than the entire microscopic theorem because it concerns this leading W1 response and a specified source family, but it is not a routine consequence of passivity or (35). No spatial summability, waiting-time moment or electric uniform integrability is claimed here.

The source state is also frozen while the fast forcing varies in (31). An actual microscopic elimination has time-dependent slow preparations, same-original-mark off-grade coherences, further returns and several holes. One cannot write it as (31) with a uniform coefficient norm by definition. The effective occupation estimate (25) is not a microscopic conditional source estimate. Controlling the real slow/source perturbations and local electric commutators remains necessary; the checked global count tilt cannot be restricted to a moving island without proof. Spin boundaries, finite-spin compensation and transfer need their own checked estimates.

There is no all-time finite-volume uniformity assertion for arbitrary periodic backgrounds. The source thermodynamic limit precedes the infinite directed series. Finite-prefix approximation is compatible with each fixed fast-time limit; interchanging every volume and infinite-response operation would require an additional argument. These distinctions prevent the new source response from silently importing a false all-background gap.

The slab result only rules out too-fast uniform-prefactor finite-k rates; it does not refute the source-weighted target or polynomial rates. The exposed-star result removes the reducing-dark-block hypothesis for one partial reward; it does not prove full absorption from arbitrary dense background. The moving-tube result is the genuinely new many-record discriminator: it localizes the triangularity budget to the dynamically visited sites and consumes actual all-history source factorials, without assuming a static cluster.

## 8. Controls, failures retained, and source evidence

CONTRACT.md and PRE_DERIVATION.md were frozen in PRE_FREEZE.json before the new control. TARGET_EXTENSION.md records the later analytic fixed-source forcing consumer without rewriting that pre-control history. The standalone check.py imports no earlier builder and uses only sparse integer/rational computations. Its actual run used2.083188 CPU seconds,2.0845385 wall seconds and28,409,856 bytes peak RSS, one BLAS thread; no failure, retry, worker or resource overrun occurred. The declared initial price was30CPU/90wall/120MiB; CPU has a hard process limit and deadline/STOP/wall/RSS are checked at bounded checkpoints.

Six slab radii4,6,8,12,16,24 have exact full locally cancelled-H output equal to K²; every negative first hop is explicitly checked blocked. Their exact squared norm ratios are in RESULTS.json; R²||Hf||/||f|| ranges26.38 to32.55, corroborating rather than proving the deliberately loose8192 bound. The proof of all R is (7)-(8). Physical charge-Dicke bijectivity is also checked in42 finite combinatorial cases,508 assignments; the all-size normalization is the analytic bijection above.

The literal charge/rotor runner constructs physical Gauss flows and tests the k13 negative transition which breaks enlarged-P invariance. Selected exposed rows at k7 and13 have68 and75 complete reverse words, respectively, and precisely their one dark input. A filled local k45 row has136 total outputs and37 other dark words:29 with the selected output hole and8 with a moving hole. Every such word satisfies Gauss, the exact tube B-count conservation, positive x advance and clipped-height increment. The all-background path/series theorem is proved analytically, not inferred from these finite samples.

Failed shortcuts are retained explicitly: static initial occupied components are not conserved; the enlarged exposed class does not reduce DHD; the zero-angle fiber needs a normalizable packet; a small expectation does not prove the required norm residual; a convergent dark-to-bright source conversion is not a spatial bound on the bright output; a finite-torus prefix is not its all-n series. No parameter scan or altered operator was used to avoid these issues.

SOURCE_IDENTITIES.json binds the exact main and prior proof/check bytes, source paths, current open inventory and authored control. All final packet hashes appear in FREEZE.json. The working campaign HEAD is recorded separately from the selected main source. No source, prior report, reviewer file, shared authority, audit or remote record was changed. Independent checking is required before new load-bearing downstream use.
