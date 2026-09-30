# Finite-excitation multiple-hole rotor absorption and the original-mark cascade

Authored research, September30,2026. This is a provisional proof and exact sparse control packet, awaiting focused independent checking. It is not a formal review/audit, microscopic-limit theorem, finite-spin theorem or native-law adoption.

On the physical finite-change rotor representation over Omega on **Z³**, every fixed finite sector W=m>=1,N_B=k has an explicit first-original-event absorption rate, uniform over positions, charge assignments and all normalizable electric states. The full compensation gates and every overlapping hole are retained. The actual original-mark cascade then reaches W0 after exactly m original events almost surely, with explicit completion-time bounds and polynomial electric-output controls under the stated input moment condition.

This is not an independent-hole approximation. Summing one-hole compensation formulas gives the wrong operator. The new proof uses the rightmost hole to order **all** coherent reverse paths, including paths moving a different hole, and treats the overlapping compensation centers as a union. Periodic densely occupied sectors can remain dark; no arbitrary-periodic-volume theorem is inferred.

## 1. Actual source and physical finite-excitation carrier

The scientific main is `30a9461ee19a49b99fa6628fe942f08e504e8903`, freshly fetched at this route's start. The selected campaign procedure remains `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. SOURCE_IDENTITIES.json records actual source bytes, prior proof/check identities, current open proposals and read coverage. CONTRACT.md was frozen before the new computation. All earlier reports remain immutable.

The A/B cubic sites have charges q=0,+1,-1 and occupations n=q². Links are integer rotors oriented A to B, with physical Gauss law div E+1_A-q=0. Bare Omega has A plus, B empty, E=0. The elementary unsigned f_ab moves an occupied A charge into an empty B and shifts E_ab by -q_a. Write

    F_a=sum_(b~a) f_ab,
    Q_a=product_(c in A,dist(a,c)=2) n_c,
    C=sum_a F_a†F_a Q_a,
    H=C+[F,F†],     F=sum_a F_a.                       (1)

The eighteen-center gate in (1) is the actual supplied rotor compensation. It is not replaced by a sum of independent one-hole gates. The sign of the commutator follows from the same canonical rotation F†-F as in the source. The original birth j_(a,b,s) fills an empty a,b with charges s,-s and shifts E_ab by s. Marks are either the original resolved s labels or the original unnormalized coherent sum of the two signs for each edge. Distinct edges remain distinct marks. The loss is

    G=sum_mu j_mu†j_mu
      =2 sum_(h an A hole) #(empty B neighbors of h).    (2)

The sign outputs on a coherent edge are orthogonal in their final A charge, so (2) holds for either instrument. Their full recycling maps are retained separately throughout.

The Hilbert space is the completion of physical basis words differing from Omega at finitely many sites and links, with fixed finite W=m and N_B=k. Summed Gauss gives total relative charge zero. The total number of minus records is therefore (k-m)/2; nonempty physical sectors require

    k>=m,     k-m even.                                (3)

Arbitrary coherent superpositions in this representation are allowed. Finite change of basis words does not impose a finite electric moment on every completed vector; the unweighted result below needs only normalizability. Infinite-density backgrounds or different infinite-flux representations are not silently included.

There is no global unbounded F applied to infinite Omega. The next section derives the exact finite-sum cancellation and uses it to define the bounded operator H on this sector.

## 2. Exact hole-mask blocks, with overlapping gates counted once

Let Z be the finite set of A-hole positions, |Z|=m, and P_Z its occupation projection, leaving every charge/electric degree of freedom intact. On the diagonal hole-mask block,

    P_Z H P_Z=P_Z[
         sum_(h in Z) F_h F_h†
          -sum_(a notin Z,dist(a,Z)=2) F_a†F_a]P_Z.     (4)

The negative sum is over a **set**, not over one copy for each adjacent hole. For an occupied a the actual Q_a equals zero precisely when at least one other A hole is within distance two. Thus C cancels -F_a†F_a whenever no hole is nearby, and leaves one copy otherwise. At an already empty a, F_a†F_a vanishes on the input. This proves the gate multiplicity in (4).

Every off-diagonal hole-mask block moves exactly one hole h into an occupied distance-two A center a:

    Z'=(Z\{h}) union {a},   h in Z, a notin Z,
    P_Z' H P_Z=P_Z'[F_a,F_h†]P_Z.                      (5)

It vanishes unless a,h share a B neighbor. In the two products, paths using distinct intermediate B sites commute exactly and cancel, including their charge transfers and rotor translations. A two-hop term cannot move two distinct holes. The compensation itself preserves every A occupation. These facts classify the full operator, not just a selected positive submatrix.

Each elementary f has norm one and ||F_a||<=6. There are at most m positive products and18m occupied centers in the union of negative terms, giving diagonal block norm<=684m. For each hole there are six axial neighbors with one shared B and twelve face-diagonal neighbors with two. Each shared-B commutator has norm<=2; both row and column sums of off-diagonal hole-mask block norms are at most60m. Hence

    ||H||_(m,k)<=744m<=M_m:=1092m,
    0<=G<=g_m:=12m.                                   (6)

Equations (4)-(5) give finite rows on the physical core and a bounded symmetric operator. It has a unique bounded self-adjoint extension. Gauss, m and k are preserved. This is an infinite-lattice construction without a finite electric box or spatial boundary deleting transitions. The constants do not depend on positions or a volume regulator. They do **not** claim the same decay on arbitrary finite periodic/open graphs.

The naive additive-hole expression replaces the negative term by a multiplicity-weighted sum and is false. In the exact two-hole control at k=10 it differs from (4) on69 basis words, with squared norm852 on the tested unit input. The literal full C+[F,F†] instead agrees with (4)-(5) on all245 output words. The interaction from overlapping gates is thus both retained analytically and discriminated computationally.

## 3. Extremal-hole reverse rows and an exact bounded height

Let D=1_(G=0). A dark basis word alpha has hole set Z and occupied B set S containing the complete six-site star of **every** hole. Select the lexicographically maximal h in Z. In particular h_x=max_(z in Z)z_x. Put

    b=h+e_x,       c=h+2e_x.

The center c is occupied because it is farther in x than any input hole. The actual path f_cb f_hb† refills h from its occupied neighbor b and then empties c into that newly vacated B site. Its H matrix element is +1; the reverse same-b order is blocked. The axial pair has only this shared b. No compensation term changes the hole mask.

Let V send alpha to this exact output beta, keeping the actual charges and integer link shifts. V is an isometry on the entire dark basis span. The output c is the unique hole with greatest x, two steps beyond every retained hole. It therefore identifies h=c-2e_x and the entire input hole set uniquely; the charge exchange and both field shifts have a unique inverse. This selection is a proof device, not an observed hole label.

Define

    x_*(Z)=max_(h in Z)h_x,
    chi(s)=max(-5,min(5,s)),
    Phi(Z,S)=sum_(b in S)chi(x_*(Z)-b_x),
    -5k<=Phi<=5k.                                     (7)

Fix a row alpha and its selected output beta with hole set Z'=(Z\{h}) union {c}. Examine every other dark source alpha' feeding beta under H. This reverse-row examination is essential to control destructive interference.

**The move creates the output hole c.** The source has hole set (Z'\{c}) union {z}, where z is a distance-two neighbor of c. Its smallest possible x coordinate is h_x, attained only by z=h. That is the selected original hole set, whose inverse charge/field path is unique. Every other source in this case has z_x=h_x+d, d=1,2,3,4; it is its rightmost hole. The B mask remains S. The original six occupied star sites about h have relative x coordinates -1,+1,0,0,0,0. Their total clipped increment under this shift is exactly6d, and every other B site contributes a nonnegative increment. Thus Phi(alpha')-Phi(alpha)>=6.

**A different hole moves, retaining c.** The source already contains c; it replaces another output hole a, whose x coordinate is at most h_x, by a neighbor z of a. Therefore z_x<=h_x+2=c_x, and the source rightmost x is exactly c_x. Its B mask remains S. The same original star gives a height increment at least12. This is the new interference class absent from the one-hole proof; it is not discarded even when holes strongly overlap.

**The hole mask stays Z'.** The terms in (4) keep S or change it by one B move between sites sharing an A, at graph distance at most two. Their center may be near any of the holes, not just c. Moving the maximum hole coordinate from h_x to c_x first increases Phi by at least12. Because chi is one-Lipschitz, that one B reshuffle can decrease the sum by at most two. The total increase is therefore at least10. Charge swaps and all field translations are allowed in this case.

Finally, the spectral term -lambda V†D can feed this row only from beta when beta is dark. It raises the height by at least12. Consequently

    V†(H-lambda)D=I_D+U_lambda,                        (8)

where every nonzero U block has source height at least six larger than its row height. With

    n_k=floor(5k/3)+1,

the finite range in (7) gives exactly U_lambda^(n_k)=0. This is finite block triangularity of a bounded operator on the full infinite charge/field space, not finiteness of its configuration graph. For |lambda|<=M_m, ||U_lambda||<=2M_m+1. Define

    R_mk=sum_(j=0)^(n_k-1)(2M_m+1)^j.

The finite Neumann inverse of (8) proves

    ||psi_D||<=R_mk||(H-lambda)psi_D||.                (9)

An empty dark subspace is harmless; (9) is then read on the zero space. The proof uses one selected extremal hole to order all sources, but nowhere factorizes the dynamics of the m holes.

## 4. Explicit first-event absorption

Let x=||G^(1/2)psi|| and z=||(H-lambda)psi||. On B=I-D, G>=2, so ||Bpsi||<=x/sqrt(2). Equation (9) and ||H-lambda||<=2M_m yield

    ||psi||²<=2R_mk² z²+(4M_m² R_mk²+1/2)x².

Put

    c_mk=1/max(2R_mk²,4M_m² R_mk²+1/2).

Then, for every real lambda,

    ||(H-lambda)psi||²+||G^(1/2)psi||²
                        >=c_mk||psi||².               (10)

Outside [-M_m,M_m], the spectral theorem compares the first term with the nearest endpoint, extending the inequality. No isolated spectrum or eigenbasis is needed.

Here are constants for the actual no-event semigroup S_mk(t)=exp[t(-i delta H-kappa G/2)]:

    a_mk=min(1,delta²)c_mk,
    T_mk=2*pi/sqrt(a_mk),
    c_U,mk=3*a_mk*T_mk/8,
    b_mk=min(1/2, kappa*c_U,mk/(1+6kappa*m*T_mk)²),
    C_mk=exp(b_mk/2),     gamma_mk=b_mk/(2T_mk).        (11)

To verify rather than import the conversion, apply the scaled (10) at all real Fourier frequencies to sin(pi t/T)exp(-i delta Ht)psi on [0,T], zero outside. Hilbert-valued Plancherel and the derivative of the sine factor give

    integral_0^T ||G^(1/2)exp(-i delta Ht)psi||²dt
       >=(a_mk*T/2-pi²/(2T))||psi||².

At T=T_mk this is c_U,mk||psi||². In the original-loss Duhamel comparison, g_m=12m gives the Volterra factor1+kappa*g_m*T/2=1+6kappa*m*T. Since d||S_mk(t)psi||²/dt=-kappa||G^(1/2)S_mk(t)psi||², the interval contraction is ||S_mk(T_mk)||²<=1-b_mk. Iteration and contraction on the final fractional interval prove

    ||S_mk(t)||<=C_mk exp(-gamma_mk t).                 (12)

All couplings are fixed positive numbers. The prefactor is at most exp(1/4), while

    log(gamma_mk^-1)=O(k log(m+1)).                    (13)

The constants are intentionally conservative, not a short-relaxation prediction. Equation (12) excludes a nonzero invariant dark subspace in this declared finite-change, finite-(m,k) Z³ sector. It does not exclude the previously constructed periodic dense sectors or arbitrarily long lifetimes as k grows.

The stacked original mark map has norm at most sqrt(12m). Integrating the exact loss identity and using (12) gives, for every normalized input,

    integral_0^infinity kappa sum_mu
                    ||j_mu S_mk(t)psi||²dt=1.          (14)

Thus the first event is an actual original mark almost surely. The result is field uniform and does not require a field-moment preparation assumption.

## 5. The finite original-mark cascade, with no independence assumption

Every original j_mu maps

    (m,k) -> (m-1,k+1),                               (15)

preserving Gauss and the actual resolved/coherent convention. Neither the coherent sum nor an overlapping neighboring hole changes (15). Set initial m=m0,k=k0 and, before event ell+1,

    m_ell=m0-ell,     k_ell=k0+ell,
    ell=0,...,m0-1.                                   (16)

The quantity m+k is fixed by this **leading** cascade. It is not a conservation law for the omitted microscopic hopping F+F†. Conditions (3) continue to hold at every stage. On the direct sum of these finitely many sectors, H and the complete stacked J remain bounded. Even on Z³ the countable marked gain is a bounded normal CP map, because J†J=G<=12m0. The associated leading GKSL evolution and its first-event instrument are therefore well defined with no infinite global event rate.

At each stage (14) applies to every postmark density, whatever its spatial overlap, field coherence or correlations with earlier recorded times and marks. Compose the exact CP first-event maps. Induction gives a trace-preserving total map to W0 after exactly m0 marks. Its Kraus densities in interarrival times tau_1,...,tau_m0 are the actual products

    kappa^(m0/2) j_mu_m0 S_(1,k0+m0-1)(tau_m0)
           ... j_mu_1 S_(m0,k0)(tau_1).                (17)

Summing the stipulated labels and integrating tau_i>0 yields trace one. The chronological timestamps are their partial sums, so no original time/order information is replaced. Stage number is simply the count of already recorded original marks, not an additional measurement. At W0, the leading H in (1) and all bare j_mu vanish. Slow effective dynamics and further microscopic formation are outside this fast-cascade statement.

One can bound the completion time without treating the waiting times as independent. Let C_ell,gamma_ell be (11) at (16). For 0<a<2gamma_ell, integration by parts of its survival probability gives the uniform one-step exponential-moment bound

    E[e^(a tau_(ell+1)) | prior original record state]
       <=B_ell(a):=1+a C_ell²/(2gamma_ell-a).           (18)

Equivalently the CP first-event map weighted by e^(a tau) has trace norm at most B_ell(a) on positive inputs. Composing those maps, rather than an independent waiting law, proves

    E[e^(a T_finish)]<=product_ell B_ell(a),
          0<a<2 min_ell gamma_ell.                    (19)

With gamma_*=min_ell gamma_ell, for example,

    Pr(T_finish>t)<=(1+exp(1/2))^m0 exp(-gamma_* t),
    E[T_finish]<=sum_ell C_ell²/(2gamma_ell).           (20)

Every finite waiting-time moment exists. The inverse gamma_* is at most exp[O((k0+m0)log(m0+1))] at fixed couplings. These are leading fast-time estimates and do not justify an independent-excursion model for the full microscopic ensemble.

## 6. Original marked field outputs through the cascade

Let Q=1+sum_links|E_link| on the finite-change basis and close it spectrally. H has integer Q bandwidth at most two, G commutes with Q, and the actual J between successive sectors has Q bandwidth at most one. On stage(m,k), the five H bands each have norm at most M_m. Thus

    ||ad_Q^r(-i delta H-kappa G/2)||<=5 delta M_m 2^r,
                                                        r>=1.

The bounded-band graph-domain proof already independently checked for the one-hole source applies with these verified new constants: the binomial identity for Q^p A is first valid on finite words, then closes because Q^p is closed; A is bounded on its graph norm, and the graph-space exponential agrees with S. No field-box boundary is deleted. Its iterated Duhamel recurrence gives

    P_0(t)=1,
    P_r(t)=2^r Touchard_r(5 C_mk delta M_m t), r>=1,
    R_p,mk(t)=sum_(r=0)^p binom(p,r)P_r(t),

    ||Q^p S_mk(t)psi||
       <=C_mk exp(-gamma_mk t)R_p,mk(t)||Q^p psi||.     (21)

For the actual marked stack, its three bands and Q>=1 imply

    ||Q_out^p J Q_in^-p||<=3 sqrt(12m) 2^p.

For every integer p>=0 and 0<=a<2gamma_mk define the explicit finite constant

    A_p,mk(a)=108 kappa m 4^p C_mk²
       *integral_0^infinity exp[-(2gamma_mk-a)t]
                                  R_p,mk(t)²dt.        (22)

The one-step original output has

    integral_0^infinity e^(a t) kappa sum_mu
       ||Q_out^p j_mu S_mk(t)psi||²dt
                       <=A_p,mk(a)||Q^p psi||².        (23)

It extends to positive mixed inputs with finite Tr(Q^(2p)rho) by positive spectral sums and bounded observable cutoffs. No Loewner monotonicity of density compressions is assumed. Applying (23) successively to the actual CP instrument densities in (17) yields

    sum_histories integral e^(a T_finish)
                   Tr[Q_final^(2p) rho_history]
      <=[product_ell A_p,m_ell,k_ell(a)]
                   Tr[Q_initial^(2p)rho_initial],
         0<=a<2gamma_*.                               (24)

Here rho_history includes the actual kappa factors, mark coherence and ordered integration density. The integral in (22) is a finite polynomial Laplace integral, so all constants are explicit. At p=0,a=0, trace preservation from section5 gives the sharper exact value one. Equation (24) supplies controlled polynomial field outputs and weighted completion-time moments for this finite leading cascade. It does not assert that the evolving microscopic source provides the required initial moment, or extend to a positive-density/infinite-excitation state.

## 7. Exact controls, including the failed additive formula

check.py uses exact integer charges, link fields and coefficients, with elementary conventions from our previously checked rotor source. It imports or executes no earlier runner. The literal test forms finite sums of C+F F†-F†F over thirty A anchors containing every hole and every distance-two hole neighbor, plus two remote anchors. Terms at all further A centers cancel by the disjoint-path identity; the retained remote terms also cancel in the explicit computation. This is a matrix-element cancellation control, not a finite-region dynamics with a new reflecting boundary.

At(m,k)=(2,10), the literal expression and (4)-(5) agree on245 output words. The deliberately wrong additive-hole formula differs on69 words with squared norm852. The discrepancy is kept in RESULTS.json as a failed route, not hidden by redefining the compensation.

Selected-path/reverse-row controls cover

    (m,k)=(2,10),(2,12),(2,146),(3,147),(4,146).

All selected coefficients and inverse words are exactly one. The last three cases contain respectively30,58,86 dark reverse inputs that **retain** the selected rightmost output hole while moving another hole; these are the new multi-hole interference terms. Each also has33 same-mask dark sources and15 sources moving the selected output hole. Every height increase has the stated positive sign. In total934 complete reverse words satisfy Gauss and preserve(m,k). The dense masks are finite B balls, not filled periodic backgrounds.

The original birth controls retain both charge signs and check the exact output sectors and Gauss. A separate actual two-mark basis word has grades(2,2)->(1,3)->(0,4), with final H=G=0. It corroborates the operator grading, not the quantified almost-sure cascade theorem, which rests on sections4-5.

The run completed in4.810415 CPU seconds,4.820904 wall seconds, peak42,631,168 bytes, with one thread and the declared30 CPU second/150 MB cap. RESULTS.json binds the runner. There was no dense full carrier, field truncation, fitted tolerance or suppressed failed assertion. All general claims depend on the analytic reverse-row, bounded-operator and CP-composition arguments, not finite sampling.

## 8. Alternative domains and remaining bridge

The already independently checked periodic sector with W2 and every B occupied is a real alternative: there F=0 on the input, C=0, G=0, and H=F F† leaves the filled-B sector invariant. Its leading dynamics can change an actual bounded field readout while producing no bare original mark. It is physical and source-accessible at finite volume; its first dressed jump gives an order-one physical-time escape. That result is neither contradicted nor weakened here. It is outside the finite-global-k Z³ representation, and a periodic wrap destroys the global extremal-hole ordering. No periodic extension of the present theorem is asserted.

Finite B-filled islands in Z³ can also have arbitrarily long dark prefixes as their size grows. This is consistent with a positive rate for each fixed(m,k) whose inverse worsens as in(13). A statement uniform over all backgrounds or all k would be false; it is not used. The present proof does retire a finite-excitation **multiple-hole** leading rotor absorption/cascade obligation, including arbitrary overlaps and coherent fields, beyond the previously checked W1 result.

The microscopic local-output bridge still needs actual source-weighted localization/decomposition for these finite sectors, control of coupling to later formation and higher normal-form terms, initial field moments, and the independent finite-spin transfer with its zero boundary weights. The selected path in section3 is unit-weight only for the rotor. The one-hole local-response packet is separately frozen and under its own check; no unverified multi-hole local-response extension is used here. Quantum dynamics, compensation, instruments, clock and record interpretation remain supplied mathematical premises.

Closest actual prior arguments are recorded in CONTRACT.md and SOURCE_IDENTITIES.json. The finite-star/repeated-record and periodic crowded-sector results have different graphs, laws or global sectors. The checked one-hole proof supplies a method and its scoped benchmark, not an assumed multi-hole completion. Refreshed PR9399 supplies an effective A-occupied thermodynamic process, not this fast cascade. New PR9400 was inspected through its actual body and file inventory and is an unrelated fixed-population ring estimator study. No exhaustive novelty claim or status promotion is made.
