# Long physical prefixes invisible to loss AND every formal source adjoint

Authored analytic result under CONTRACT.md. This is not a generic-phase invariant-module theorem or an actual-source preparation claim. No scientific computation is used. The complete source-frame proof and its focused receipt are inputs, at their formal-range scope only.

## 1. Actual operators and the augmented observation

Use the supplied cubic rotor with q=0,+1,-1, oriented A-to-B links, integer E, and div E=q-1_A. All elementary hops are the unsigned qutrit/rotor partial isometries. For W=1, fixed odd k=N_B and total charge n=|A|, use the COMPLETE compensated operator

    H=C+[F,F*],   C=sum_a F_a* F_a Q_a.

Its checked cancellation identity, with P_h fixing the hole, is

    P_h H P_h=P_h(F_h F_h* - sum_(d(a,h)=2) F_a* F_a)P_h,
    P_a H P_h=P_a[F_a,F_h*]P_h.                         (1)

Here Q_a is the original eighteen-A-neighbor occupation gate, not the aligned-star projector introduced below. The original loss is G=2 times the number of empty B neighbors of the hole, with 0<=G<=12. The norm estimate ||H||<=744 is uniform in these finite tori and in fields; the looser checked 1092 would also suffice. Hole moves have lattice distance at most two. Distinct-intermediate terms in the off-diagonal commutator cancel, with their actual fields and signs. Moving-hole terms preserve the B occupation mask; the negative same-hole terms can move an occupied B and must generally be retained.

For each original mark mu at h, the formal positive source is

    B_(h,mu)=-F_h j_mu F_h P_0,

from W=0, N_B=k-3, with ALL physical input words allowed. P_0 here means W=0. The marks are separately either the resolved signs or the original unnormalized coherent sum at each edge. Define the bounded column observation

    O psi=(sqrt(G) psi, (B_(h,mu)* psi)_(h,mu)).         (2)

The second components are formal source-adjoint tests. They are NOT additional observed events in the original instrument.

Let A be the diagonal projector onto a hole with all six neighboring B sites occupied and all six charges equal, either all plus or all minus. The checked source frame proves exactly

    ker O = Ran A.                                     (3)

On the mixed full-star subspace its frame has lower bound 56 for resolved marks and 40 for coherent marks. No actual Omega-history density is used in (3). For a simple full-space upper bound, ||F_h||<=6 and ||j_mu||<=1 (resolved) or sqrt(2) (coherent) give

    sum_(h,mu) ||B_(h,mu)* psi||^2 <=15552 ||psi||^2,
    ||O||^2<=15564.                                    (4)

Indeed each B_(h,mu) has output hole h; the different P_h are orthogonal. At fixed h there are twelve resolved maps of norm at most36, or six coherent maps of norm at most36sqrt(2). This is deliberately cruder than the frame bound on full stars, since (4) includes bright outputs too.

## 2. A physical family, with complete charge and Gauss accounting

Let L=4s with integer s>=4. Set

    n=L^3/2=32s^3,       k=n-1,       q=s-1.

The symbol q in the rest of this proof is the integer detection order, not a site charge; site charges will be written sigma_x. Choose

    initial A hole h0=0,
    sole empty B site v=(2s,0,1),
    selected negative A site a=2q e_x=(2s-2,0,0).        (5)

All B sites other than v have charge +1. Every occupied A site with periodic l1 distance <=2q-2 from 0 has charge +1. Assign charge -1 to the selected site a, and choose the remaining A charges so that exactly

    r=(k-1)/2=n/2-1=16s^3-1

A sites carry charge -1. The other occupied A sites have charge +1.

This assignment exists. The ball radius 2q-2=2s-4 is below L/2, so its count is the unaliased Z^3 count. The number of nonzero even-parity sites through radius 2m, with m=s-2, is

    P_m=sum_(t=1)^m (16t^2+2)
       =(8/3)m(m+1)(2m+1)+2m < 16s^3=n/2.             (6)

There are n-1 occupied A sites, so exactly n/2 of them can be plus while retaining every required plus site. The selected a lies outside the required plus ball and can be one of the n/2-1 minus sites. No sign assumption is made on the other A sites outside that ball.

There are 2n-2 occupied sites. With r=(n-2)/2 negative charges their total charge is (2n-2)-2r=n. Therefore sigma_x-1_A(x) is an integer zero-sum divergence demand. On a spanning tree of this finite connected torus, solving the demands by subtree sums gives an integer link field E0 of exactly that divergence. No field cutoff or boundary deletion is needed. Let xi be this single physical charge/field basis word, normalized to one. It has finite electric support and every polynomial field moment on this finite graph, although no volume-uniform field-moment bound is asserted.

This is an admissible preparation in the supplied physical Hilbert space. It is NOT asserted to be an actual original-source output from Omega, or to have any positive history weight.

## 3. Literal Hamiltonian powers before the first mixed star

The distance from the initial hole to the B vacancy is

    d(0,v)=2s+1=2q+3.                                 (7)

Suppose a word is encountered before applying the jth H, with 1<=j<=q. Its hole has distance at most 2(j-1) from 0. Inductively its B occupation mask is still the initial mask. Consequently

    d(h,v)>=2q+3-2(j-1)>=5.                            (8)

Every B within distance three of h is therefore occupied. In (1), every outward-first term F_a*F_a with d(a,h)=2 is zero on that word: no B neighbor of a is empty. In F_h F_h*, filling h from a B makes just that B vacant within reach of F_h, so the only same-hole terms are the six exact returns. The remaining moving-hole terms are precisely the positive paths through a shared occupied B. Their reverse order is blocked. The distinct-intermediate paths have already canceled in (1).

Thus on ALL columns used through this qth power, the full H acts as six returns plus positive shared-B hole moves, with the actual transported charges and field translations. This is a restricted-column consequence of the full cancellation, not an asserted global factorization H=F F* or an invariant fixed-mask subspace.

For j<=q-1, every encountered A site has distance <=2j<=2q-2 from 0. Its initial charge is plus. All moves through order j therefore transport only plus charges, leaving the occupied B sites plus and the hole inside this plus region. Every such output is an aligned full-star word. It follows, as an exact identity on full physical fields, that

    (I-A) H^j xi=0,
    G H^j xi=0,   B_(h,mu)* H^j xi=0
                         for all h,mu and 0<=j<q.      (9)

Diagonal returns and multiple moving paths do not compromise (9); each individual surviving full word has the required star. Coherence among these paths is retained.

## 4. An exact first nonzero formal source-adjoint order

At the qth power, consider the output hole a=2q e_x. To reach this coordinate from 0 in q steps of H, each step must have x displacement +2. Every other allowed hole move has x displacement at most1, zero, or negative. No return is allowed in such a maximal-displacement path. Periodic wrapping cannot provide another q-step route: 2q=L/2-2, and the alternative x displacement 2q-L has absolute value L/2+2>2q. Wrapping in y or z also exceeds the total step budget.

The only possible sequence of hole centers is therefore

    0, 2e_x, 4e_x, ..., 2q e_x.                        (10)

Each axial pair has exactly one shared B site. Each step has the literal coefficient +1 in (1), and its charge and rotor translations have a unique inverse. All but the last transported A charge are plus. The last step moves the negative charge at a into b=(2q-1)e_x, while the original plus charge at b fills the previous hole. The final hole is at a; its B star has exactly one minus charge, at b, and five plus charges. The distant vacancy remains at distance three from a, so this output is a MIXED FULL star.

Let beta be the resulting complete physical word, including E. The preceding uniqueness proves

    <beta,H^q xi>=1,
    ||D_mix H^q xi||>=1.                               (11)

Other q-step outputs are allowed and do not affect this coefficient. In particular we have not replaced H^q by its chosen path. Applying the checked exact source frame gives

    sum_(h,mu) ||B_(h,mu)* H^q xi||^2 >= c,
    c=56 (resolved), c=40 (coherent).                   (12)

The source-adjoint observation first becomes nonzero at order q. Equation (12) is not an original-event probability or a statement that G becomes nonzero at that order. The selected beta itself is loss-dark.

## 5. Every physical cycle phase, not independently chosen hop phases

Use any spanning-tree Gauss decomposition E=E^(sigma)+sum_l c_l gamma_l, where the c_l are integer cycle coordinates and gamma_l are the fundamental integer cycle flows. Fourier transformation sets z_l=exp(i theta_l). The finite charge matrix H(z) has its actual Laurent monomials and original signs; theta comprises the physical cycle phases. The fixed word xi transforms into a monomial times a unit charge coordinate vector xi(z). Equations (9) hold as Laurent-polynomial identities because they were proved in the full integer-field basis.

For the selected final charge configuration in (11), there is only the one axial path, not several final electric words with phases that might cancel. Its coefficient in H(z)^q xi(z) is a SINGLE Laurent monomial of coefficient +1. On every physical phase |z_l|=1 it has modulus one. The imported full-Hilbert source-frame inequalities first pass to almost every fiber; their finite charge matrices are continuous Laurent matrices on the phase torus, so the inequalities extend to every phase by continuity. Hence (9)-(12) hold in every physical phase fiber, with the same normalized xi(z). The fiber statement does not treat a delta function at one phase as normalizable: the original xi is itself a normalizable full-field state and is the inverse transform of this bounded monomial section.

This construction is phase independent but preparation dependent. It neither chooses independent configuration-edge weights nor asserts a module invariant for all powers.

## 6. Consequences for proposed certificates and time-observation bounds

The augmented Laurent stack using I-A, or using G together with all B* rows, is rank deficient through power q-1 at EVERY physical phase and over the Laurent fraction field: xi(z) is an explicit nonzero polynomial null vector. Any full-rank certificate for this augmented observation in these sectors must reach at least

    R>=q=L/4-1.                                        (13)

This differs from the earlier G-only dimension count R>=ceil(n/6)-1. That count is not a count for the additional source-adjoint rows. Here geometry gives the new lower bound after all formal sources have been added. It does not bound the full-depth rank from above or prove an invariant null module.

The exact prefix also prices finite-time observation. Let

    S(t)=exp(t Z),   Z=-i delta H-kappa G/2,
    B0=744 delta+6 kappa,   delta,kappa>0.

By (9), Z^j xi=(-i delta)^j H^j xi for j<=q, and O Z^j xi=0 for j<q. Boundedness and the exponential-series tail give

    ||O S(t)xi|| <= sqrt(15564) exp(B0 t) (B0 t)^q/q!,
    integral_0^T ||O S(t)xi||^2 dt
      <=15564 T exp(2 B0 T) (B0 T)^(2q)/(q!)^2.         (14)

The same proof works in every phase fiber. For every fixed T and fixed delta,kappa, the upper bound tends to zero as L=4s tends to infinity. Thus no positive finite-horizon observability lower bound uniform in volume, phase and ALL physical initial states can hold, even with these additional formal source-adjoint tests. This is a counterexample to that stronger preparation-uniform inequality, not to fixed-volume generic absorption or the actual source-weighted microscopic consumer. The B* entries in (14) remain mathematical tests, not newly measured records.

## 7. Exact charge-domain compression of the surviving module

Write A=A_++A_-, splitting the two star polarities, and H_A=AHA. This compression is only a mathematical test operator; its evolution is not substituted for the original law. Put K=(I-A)HA. For an A-supported vector, the complete invariant-module condition is exactly

    K H_A^j v=0 for all j>=0.                           (15)

Indeed necessity follows from an H-invariant A orbit. Conversely (15) inductively implies H^j v=H_A^j v for every j. Cayley--Hamilton reduces the test to j<dim(Ran A) on each finite phase fiber. Thus the full charge-domain reduction retains the actual exit rows instead of simply evolving an assumed fixed background.

Some of these reduced blocks can be determined exactly without enumerating charges or fields. First,

    D_mix H A = sum_(h,a!=h) D_(a,mix)
                    sum_(b common to a,h) f_ab f_hb* A_h. (16)

There is no same-hole contribution to this mixed-full-star output. On an aligned input, F_h F_h* consists of six returns. In a negative term F_a*F_a, an outward hop fills some previously empty B site v; the second hop either undoes it, or removes a different occupied B site b. If b was a neighbor of h, the output is bright because that star is now missing b. If b was not a neighbor of h, the star at h is unchanged. In neither case is it a mixed FULL star. The moving-hole reverse order through a shared B is blocked on a full input star, giving exactly the positive term in (16); distinct intermediates cancel as in (1). These statements include arbitrary distant B vacancies, charge assignments and fields.

Second, every opposite-polarity internal edge is axial. An axial pair h,a=h+2 eta e_i has one shared B, b=h+eta e_i. A face-diagonal A pair has two shared B sites. A moving-hole path changes the charge of only its one selected shared B. The other shared B, if present, keeps the old polarity sigma, preventing the entire new star from having polarity -sigma. Same-hole terms cannot flip a full star either, by the previous argument. Therefore exactly

    A_- H A_+ = sum_(h,i,eta=+-1)
        A_(h+2 eta e_i,-) f_(h+2 eta e_i,b) f_(h,b)* A_(h,+),
    b=h+eta e_i,       A_+ H A_-=(A_- H A_+)*.           (17)

Each nonzero summand is the actual charge-controlled two-hop partial isometry, of coefficient +1 and its original rotor translation. No phase has been independently assigned to it. For a surviving path the five other B neighbors of h must be plus and the five other B neighbors of a must be minus; the charge at a before the move is minus. The common B changes plus to minus while h is refilled plus. These conditions follow from the projectors in (17), not from an assumed static domain.

There are at most six axial destinations and six axial predecessors for each hole block. The operator-valued row/column Schur estimate gives

    ||A_- H A_+||<=6,                                 (18)

in the full field space and at every physical phase. The within-polarity blocks still contain genuine same-hole B reshuffles outside the immediate star, so they are NOT fixed-mask scalar magnetic hopping matrices. The mixed exit rows (16) can have inputs of both polarities with the same complete output. Consequently the norm bound (18) or a theorem for just one polarity does not prove (15) has trivial kernel. A perturbative argument would need a separately proved inverse estimate strong enough for this actual coupling; no such estimate is imported.

## 8. What the invariant-ideal attempt still lacks

Let N_A(z) be the largest H(z)-invariant space in Ran A. The exact requested full question remains whether N_A is zero generically for every declared finite sector. The finite-matrix criterion already gives the equivalent full-depth Laurent condition

    no nonzero Laurent v with (I-A)H^j v=0
             for every j>=0.                          (19)

Generic failure would, by rational elimination and denominator clearing, yield a finite-field normalizable vector with an exactly invisible whole orbit. The earlier exact-phase criterion supplies this equivalence; it is not a new theorem here. The xi above deliberately fails (19) at j=q and is not such a vector.

Three distinct attempts were examined:

* Charge-domain propagation gives (9)-(12) for a single word. It does not allow one to eliminate the corresponding columns in a coherent null vector: another aligned input can feed the same complete mixed output. Both polarities and far charge patterns remain allowed.
* A global incidence-square argument would suggest charge-independent positivity, but it is unavailable: the negative same-hole B reshuffles in (1) are real. They vanish only on the expressly protected columns used above. Different occupation masks can have common F* intermediates, so proof-space input labels do not turn H into an orthogonal sum of fixed masks.
* Laurent extremal-support elimination might distinguish some field translations, but distinct original paths can have exactly the same total field translation and charge output. Actual cycle variables therefore do not give independent coefficients for every configuration-space path. No ordering that triangularizes all interfering opposite-polarity rows has been proved.

The precise surviving lemma is an all-polarity, all-mask elimination of (15)/(19), or an explicit nonzero Laurent invariant null vector. A basis-word path, a protected one-polarity theorem, the finite prefix here, and a sampled rank each fall short of that statement. No actual-history reachability, positive source weight, finite-spin extension, all-fast-time spatial tail or full microscopic limit has been inferred.
