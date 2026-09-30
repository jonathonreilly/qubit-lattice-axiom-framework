# Finite-excitation rotor absorption and a periodic boundary obstruction

Authored research, September 30, 2026. This is a provisional proof and exact sparse control packet, not a formal review, audit, microscopic-limit theorem, or axiom adoption. It needs a focused independent check before downstream reuse.

On the physical finite-change rotor representation over bare Omega on **Z³**, the actual compensated one-hole fast Hamiltonian has an explicit absorption bound for every fixed finite global B occupation k. The bound includes arbitrary coherent charge and electric-field states and depends exponentially on k, with no diameter or position dependence. A clipped configuration height handles the same-hole B reshuffles that invalidate the previous unique-star argument above k=9.

The geometry restriction is real. On the **L=8 periodic torus**, at the fixed physical occupation k=255, the same original Hamiltonian and loss admit normalizable approximate-dark vectors. Consequently their no-event semigroup has operator norm one at every finite time on that sector. This is proved using physical smooth cycle-angle packets around an exactly dark fiber, not by calling the fiber itself a normalizable rotor state. These two results concern different domains and are compatible.

Neither establishes failure or convergence of the original microscopic process from Omega. No finite-spin absorption theorem or quantum/native-axiom derivation is claimed.

## 1. Source and exact carrier

The selected scientific main is `30a9461ee19a49b99fa6628fe942f08e504e8903`; the selected procedure is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. SOURCE_IDENTITIES.json records exact source bytes, working HEAD separately, and provisional prior evidence. Main was freshly fetched before the target and again after the controls; it remained unchanged. CONTRACT.md and TARGET_UPDATE.md were frozen in PRE_CONTROL_FREEZE.json before the new runner was executed.

Use the actual cubic bipartition A/B, charges q=0,+1,-1, occupation n=q², and integer rotors on oriented A-to-B links. The physical law is div E+1_A-q=0. Bare Omega has all A charges +1, B charges zero and E=0. An unsigned elementary f_ab moves the charge at occupied a to empty b, shifting E_ab by -q_a. Its adjoint reverses this operation. Write

    F_a=sum_(b~a) f_ab,    W=sum_A(1-n_a),
    Q_a=product_(c in A,dist(a,c)=2) n_c,
    C=sum_a F_a†F_a Q_a,    H=C+[F,F†].                 (1)

The sum in Q_a has eighteen centers. Equation (1) is the rotor coefficient; it does not drop the finite-spin diagonal compensation and then claim a finite-spin result. The canonical microscopic rotation gives this sign of the commutator, with F increasing W. After removing the scalar penalty phase on W=1, the actual leading fast no-original-event evolution is

    S(t)=exp[t(-i delta H-kappa G/2)],   delta,kappa>0,
    G=sum_m j_m†j_m
     =2*(number of empty B neighbors of the hole).       (2)

The original marked absorbing maps are sqrt(kappa) j_m S(t). The marks are either the actual resolved signs or the actual unnormalized coherent edge sum. Their losses agree because the output charge signs are orthogonal; their recycling instruments are not identified. No extra occupation, charge, field, or dark-sector measurement is supplied.

For Z³, take the span of basis words with finitely many changes from Omega and finite-support integer fields satisfying Gauss, restrict to W=1 and N_B=k, then complete in the supplied Hilbert norm. This includes all coherent superpositions in that representation. It does not include a different infinite-density or infinite-flux representation by fiat. Summing Gauss on a finite-change word gives total relative charge zero. Its total record increment is k-1, so its total number of minus records is (k-1)/2. Thus only odd k are physical; the first nonempty sector above nine is eleven.

One must not use a divergent global F on infinite Omega. Define H on this core by the following exact cancellation of the finite-volume expression (1). If P_h fixes the unique A-hole position, then

    P_h H P_h=P_h(F_h F_h†
                  -sum_(a:dist(a,h)=2) F_a†F_a)P_h,
    P_a H P_h=P_a[F_a,F_h†]P_h,  a!=h.                 (3)

The second line vanishes unless a,h share a B neighbor. Indeed C cancels -F_a†F_a when Q_a=1; it leaves the eighteen indicated terms. For different A centers, two paths using distinct B intermediates commute exactly and cancel. This is an operator identity including charges and link translations.

Every single-edge f has norm one and ||F_a||<=6. The diagonal hole-position blocks in (3) have norm at most19*36=684. There are six axial A neighbors with one shared B and twelve face-diagonal neighbors with two; each shared-B commutator has norm at most2. Both row and column block-norm sums are at most60. The operator Schur bound therefore gives ||H||<=744. We use the deliberately looser constant

    M=1092,     ||H||<=M,     0<=G<=12.                 (4)

The bounded symmetric core operator in (3) has a unique bounded self-adjoint extension. All subsequent infinite-volume statements refer to this extension. There is no electric box with deleted transitions. Equation (3) also proves that H preserves k, that every hole move preserves the entire B occupancy mask, and that a same-hole term changes that mask by at most one B-particle move of graph length two.

## 2. Clipped height defeats coherent reverse-path cancellation

Let D=1_(G=0) and B=I-D. A dark word alpha has hole h and an occupied B set S containing all six sites of N(h). Set

    b=h+e_x,     c=h+2e_x.

Select the actual positive path f_cb f_hb†: refill h from b, then empty c into the newly vacated b. Its matrix element in H is +1. The reverse same-b order is blocked, since b was occupied. Distinct-b paths cancel in the commutator. The axial stars share exactly this b.

Let V map alpha to that exact resulting basis word beta, with its actual charges and electric translations. V is an isometry D Hspace -> Hspace. The output hole c determines h=c-2e_x; the output B mask is unchanged; the charge exchange and both field shifts have a unique inverse. Thus no two distinct inputs map to the same output. V is a proof device, not an extra observed channel.

Define an integer, translation-invariant height

    chi(s)=max(-5,min(5,s)),
    Phi(h,S)=sum_(b in S) chi(h_x-b_x),
    -5k<=Phi<=5k.                                      (5)

Fix a row alpha, and examine **every other dark input alpha'** that can feed its selected output beta in H. This reverse-row argument is necessary: finding a nonzero path from each basis input would not rule out coherent cancellation.

First suppose alpha' has hole a' different from the output hole c. By (3) its B mask is the same S, and a' is one of the eighteen distance-two neighbors of c. Its x coordinate has minimum h_x, attained only at a'=h. That minimum case has the unique inverse path already selected; any other dark input in it has zero matrix element. All other possible centers have a'_x-h_x=d in {1,2,3,4}. For the six original occupied star sites, the values h_x-b_x are -1 once, +1 once and zero four times. Shifting the hole by d raises their total clipped height by exactly6d: none leaves [-5,5]. Every other occupied B contributes a nonnegative increment because chi is monotone. Therefore

    Phi(alpha')-Phi(alpha)>=6.                          (6)

Next suppose alpha' already has its hole at c. A same-hole term in (3) either keeps S or changes it by one B move between sites sharing an A. Their x coordinates differ by at most two. Shifting h to c with mask S adds at least12 to (5); replacing one B site can subtract at most2 because chi is one-Lipschitz. Hence in this case

    Phi(alpha')-Phi(alpha)>=10.                         (7)

This includes diagonal electric/charge terms and the full negative compensation remainder, not just positive hole hopping. Finally, the spectral term -lambda V†D can contribute at this row only from alpha'=beta, when beta is dark; its height is at least12 larger than alpha's.

Consequently, for real lambda,

    V†(H-lambda)D=I_D+U_lambda,                         (8)

and every matrix block of U_lambda has source height at least six larger than its row height. Because (5) has only finitely many integer levels, this statement is an exact operator triangularity, even on the infinite charge/field Hilbert space. In particular, putting

    n_k=floor(5k/3)+1,

gives U_lambda^(n_k)=0: n_k successive decreases by at least6 cannot fit in a height range of length10k. There is no assertion that the individual configuration graph is finite.

For |lambda|<=M, ||U_lambda||<=2M+1. Define

    R_k=sum_(j=0)^(n_k-1) (2M+1)^j.

The finite Neumann inverse of (8) proves, for every dark coherent vector,

    ||psi_D||<=R_k||(H-lambda)psi_D||.                  (9)

This is the new load-bearing nonlinear discriminator: the bounded height orders all interfering original paths. It is stronger than basis accessibility or a support-only escape argument, and does not require a connected B mask or a bound on its diameter.

## 3. Uniform real-frequency observability and actual absorption

Write x=||G^(1/2)psi|| and z=||(H-lambda)psi||. Since G>=2 on B, ||Bpsi||<=x/sqrt(2). Equation (9), ||H-lambda||<=2M and orthogonality of D/B give

    ||Dpsi||<=R_k(z+sqrt(2)M x),
    ||psi||²<=2R_k² z²+(4M²R_k²+1/2)x².

Thus, with

    c_k=1/max(2R_k²,4M²R_k²+1/2),

we have the real-frequency inequality

    ||(H-lambda)psi||²+||G^(1/2)psi||²
                      >=c_k||psi||².                  (10)

For lambda outside [-M,M], the spectral theorem compares |H-lambda|² with the corresponding endpoint |H-M|² or |H+M|², so (10) holds for every real lambda. If D is empty the same argument is read on the zero subspace, or follows directly from G>=2. No positive-energy or spectral-gap assumption was imported.

Here is an elementary conversion to time observability, including constants. Set

    a_k=min(1,delta²)c_k,    T_k=2*pi/sqrt(a_k),
    c_U,k=3*a_k*T_k/8.                                 (11)

Let U(t)=exp(-i delta Ht) and chi_T(t)=sin(pi t/T) on [0,T], zero outside. Its zero extension is H¹. Apply the scaled version of (10) at every real Fourier frequency to w(t)=chi_T(t)U(t)psi. With the Fourier convention making i*d/dt the frequency multiplier,

    (i*d/dt-delta H)w=i*chi_T'(t)U(t)psi.

Hilbert-space Plancherel, integral chi_T²=T/2, integral |chi_T'|²=pi²/(2T), and chi_T²<=1 yield

    integral_0^T ||G^(1/2)U(t)psi||² dt
             >=(a_k*T/2-pi²/(2T))||psi||².

At T=T_k this is c_U,k||psi||². All operators are bounded; no unproved domain/resolvent theorem is needed.

Duhamel and G<=12 imply

    ||G^(1/2)U(.)psi||_L²(0,T_k)
      <=(1+6*kappa*T_k)||G^(1/2)S(.)psi||_L²(0,T_k).

Indeed the Volterra kernel has operator norm at most6*kappa, and its L² integration norm is at most T_k. The original loss identity d||S(t)psi||²/dt=-kappa||G^(1/2)S(t)psi||² now gives, with

    b_k=min(1/2, kappa*c_U,k/(1+6*kappa*T_k)²),
    C_k=exp(b_k/2),     gamma_k=b_k/(2*T_k),             (12)

the bound

    ||S(t)||<=C_k*exp(-gamma_k*t),     t>=0.             (13)

To check the prefactor, iterate ||S(T_k)||²<=1-b_k and use contraction during the last fractional interval. At fixed positive delta,kappa, log(gamma_k^-1)=O(k), and C_k<=exp(1/4). These deliberately crude constants make no short-time or experimentally accessible relaxation claim.

For every normalized input in this exact sector,

    integral_0^infinity kappa sum_m ||j_m S(t)psi||²dt=1. (14)

Equation (14) uses the original marked maps with their coherence intact. It is a leading, standalone one-hole first-event theorem. It does not assert that each microscopic defect constitutes an independent excursion of this semigroup.

## 4. Actual polynomial field outputs

The already focused-checked polynomial-weight argument applies to (13) at the present abstract bounded-band level. For clarity, its hypotheses can be checked here without a finite-volume electric cutoff. Let

    Q=1+sum_links |E_link|

on the physical finite-change basis, then close it spectrally. H has integer Q bandwidth at most2, G commutes with Q, and the actual stacked J=(j_m)_m has input/output Q bandwidth at most1 and norm at most sqrt(12). Infinite countable mark labels cause no extra factor: J†J=G. The five H bands, defined by phase averaging against Q, each have norm at most M. Consequently

    ||ad_Q^r(-i delta H-kappa G/2)||<=5*delta*M*2^r,
                                                     r>=1.

On the finite-word core, the binomial commutator formula expresses Q^p A in terms of bounded commutators times Q^(p-r). Closing Q^p makes A a bounded operator on its graph norm. Its graph-space exponential equals S(t) by uniqueness in the original Hilbert space, proving preservation of D(Q^p); no transitions are deleted. Iterated Duhamel then gives, for integer p>=0,

    P_0(t)=1,
    P_r(t)=2^r Touchard_r(5*C_k*delta*M*t),  r>=1,
    R_p(t)=sum_(r=0)^p binom(p,r) P_r(t),
    ||Q^p S(t)psi||<=C_k*exp(-gamma_k*t)*R_p(t)||Q^p psi||.
                                                               (15)

The recurrence is P_p'=C_k sum_(r=1)^p binom(p,r)(5 delta M 2^r)P_(p-r), with P_p(0)=0 for p>0. The original J's three Q bands and Q>=1 imply ||Q_out^p J Q_in^-p||<=3 sqrt(12) 2^p. Therefore

    integral_0^infinity kappa sum_m
       ||Q_out^p j_m S(t)psi||²dt
      <=108*kappa*4^p*C_k²
         [integral_0^infinity exp(-2 gamma_k t) R_p(t)²dt]
         ||Q^p psi||².                                  (16)

For any fixed p the explicit bracketed constant grows at most exp(O_(p,delta,kappa)(k)). Additional nonnegative integer waiting-time moments insert t^r in the same convergent integral. Positive spectral sums extend (16) to mixed inputs with finite Tr(Q^(2p)rho); bounded field-observable cutoffs avoid any claim of Loewner monotonicity for P_R rho P_R. This is not an exponential-field preparation assumption. It also does not bound the weighted norm of an actual extensive microscopic source input by a k-independent quantity.

The precise prior receipt is independent-polynomial-absorption-check/REPORT.md0db18709..., bound to corrected polynomial-fast-absorption-extension/REPORT.md93adfdad.... The new ingredient used here is (13); its independent check is pending for this packet.

## 5. Why the same theorem cannot silently cover every periodic volume

First, the proof itself has a concrete failed extension. On L=8, use a minimum-image x difference in [-4,3]. Take h=0, the six-site star N(0), and three additional occupied B sites (5,0,0),(5,1,1),(5,2,0). This physical odd-k mask has k=9. Its clipped minimum-image height is9 at h=0 and3 at c=2e_x, a decrease of six. The cut invalidates monotonicity. The old low-k torus theorem is still valid by its different proof; this is a failure of this attempted height extension, not a dark state.

A stronger, separate periodic result uses the full actual physical rotor and shows that a field-uniform decay theorem on all periodic sectors would be false.

Take L=8, |A|=|B|=256, W=1 and a sole vacant B site b0=(1,0,0), so k=255. There are510 occupied records. Total charge256 fixes127 minus charges, an allowed physical sector. For each two-vacancy pattern, form the normalized equal-amplitude sum over every assignment of these127 minus charges to the510 occupied sites. At zero cycle flux, each elementary allowed charge-preserving hop maps this Dicke vector bijectively to the Dicke vector with the relocated vacancy. All patterns have the same binomial normalization and each assignment occurs once. The coefficient is exactly one, including intermediate W=0 or W=2 vacancy patterns. Q_a depends only on the vacancy pattern, so C also respects this explicitly derived subspace at that fiber.

Put a hole wave on A,

    f(x,y,z)=i^x*(-1)^z*1_((y+z) mod8=4),              (17)

and keep b0 as the other vacancy. On the support x is even, so the32 nonzero amplitudes are real +1 or -1. The A-to-B nearest-neighbor adjacency K kills f: the two x terms cancel through i+i^-1=0, and the y and z terms cancel pairwise because the z sign reverses. Every supported hole is at periodic graph distance at least five from b0, so every B within distance three of that hole is occupied.

On each of these inputs, the negative terms -F_a†F_a in (3) vanish. The remaining terms are the diagonal six return paths and the positive shared-B hole moves, exactly K†K on the derived symmetric-charge fiber, with b0 fixed. Hence its normalized vector psi_0 satisfies

    H(0)psi_0=0,     G psi_0=0.                         (18)

The runner independently checks (18) by the **literal full** C+F F†-F†F: F†psi_0=0, while Cpsi_0 and F†Fpsi_0 have608 equal nonzero vacancy coefficients and cancel. It does not merely insert K†K as the definition of H.

To turn (18) into a physical Hilbert-space statement, orient the finite graph and choose a spanning tree. For each charge word q of total charge256, choose the unique integer tree flow E^q of divergence q-1_A, with all non-tree entries zero. Every physical integer field is E^q plus an integer divergence-free cycle flow. Its non-tree values are free integer coordinates; the dimension is

    d=|links|-|sites|+1=1536-512+1=1025.

Fourier transformation in these coordinates gives the physical direct integral over the d-dimensional angle torus. A tree-edge hop has no cycle phase. A non-tree hop changes its own cycle coordinate by plus or minus one and multiplies the fiber matrix by exp(plus or minus i theta_e). At theta=0 the actual matrix is precisely the one used in (18). No charge/Gauss projection was dropped.

Choose a normalized smooth angle packet g_eta supported in |theta_e|<eta for every non-tree coordinate, and define

    Psi_eta(theta)=g_eta(theta)psi_0,   ||Psi_eta||=1.

This is a normalizable physical rotor state and G Psi_eta=0 exactly. A conservative finite-volume Lipschitz estimate suffices. With N=|A|, ||F_a(theta)||<=6 and ||F_a(theta)-F_a(0)||<=6 eta. Thus

    ||H(theta)-H(0)||<=C_L eta,
    C_L=72N+144N²=9,455,616,
    ||H Psi_eta||<=C_L eta.                            (19)

The first term bounds all compensation products, and the second bounds both products in the global commutator; the gates are phase-independent. A tighter local constant is unnecessary. Smoothness gives Psi_eta every finite polynomial electric moment, although these moments are not bounded uniformly as eta tends to zero.

The contraction generator A=-i delta H-kappa G/2 now obeys ||A Psi_eta||<=delta C_L eta. The exact integral S(t)Psi_eta-Psi_eta=integral_0^t S(s)A Psi_eta ds gives

    ||S(t)Psi_eta||>=1-delta C_L eta t.                 (20)

For each fixed t, let eta tend to zero. Contractivity and (20) prove

    ||S(t)||_(L8,W1,k255)=1,     every finite t>=0.       (21)

There is consequently no estimate with fixed finite prefactor and positive exponential rate uniform over all electric states of this fixed periodic sector. Nor can any fixed finite sum sum_(r=0)^n H^r G H^r have a strictly positive scalar lower bound there: for r>=1, ||G^(1/2)H^r Psi_eta||<=sqrt(12) M^(r-1) C_L eta, and r=0 vanishes. We have **not** proved that an exactly invariant dark state is normalizable; a zero-angle delta is not a state. Pointwise eventual absorption or an estimate with a stronger field-weighted input norm is not excluded by (21). No claim of accessibility of these particular smooth packets with uniform source weight is made.

## 6. Distinct attempts, failed shortcuts, and exact controls

The first extremal-coordinate attempts used an unclipped dipole or a quadratic radius. Their reverse-row ordering is useful but their height range grows with separation of spectator B particles; it does not give the desired k-only inverse. Restricting to connected clusters would add a new hypothesis and give worse constants. The clipped function in (5) retains the forced six-star increment while bounding every spectator's contribution. This is the successful configuration-space family.

The exact charge/cycle-angle fiber construction is a second mathematical family. It finds a coherent cancellation available on a dense periodic geometry, then checks the normalizability gap by smooth packets. It does not replace the arbitrary-field analysis of sections2-4.

A separate failure of the low-k proof is preserved. Start with all44 odd sites of l1 radius one or three; remove six axial sites plus/minus3e_i and the four cube corners whose coordinate product is+1. The34 remaining sites fill the star at zero and give exactly five occupied neighbors to each of the18 surrounding A centers. Add an isolated B at(15,0,0), making physical k=35. Every H-output from the tested physical dark word has G<=2. Thus projecting only onto the old G>=4 selected output rows misses H entirely on this input. This does not say G^(1/2)H vanishes or that its dark subspace is invariant.

check.py imports no earlier builder. It uses integer site charges, oriented rotor shifts and full sparse physical basis words. For k=7,11,35,45 it constructs a Gauss-law tree flow, applies (3), and then computes every reverse row of the chosen output. The selected coefficient is one. Every other dark source has the required height increase; the k=11 and45 controls include actual same-hole B reshuffles, and k=45 includes other hole-moving dark sources. Every generated word satisfies Gauss and preserves k/W. The general proof does not depend on these finite samples.

The same runner independently checks the local height geometry, the periodic minimum-image counterexample and the shielding mask. Its separate L8 sparse routine uses literal global C+[F,F†] on the exactly derived symmetric-charge vacancy fiber; no dense full charge or electric enumeration is used. It also checks finite Dicke bijections as a corroboration of the analytic normalization argument. Run results: 2.590619 CPU seconds, 2.592396 wall seconds, 26,607,616 bytes peak RSS, one thread; RESULTS.json binds the exact runner hash. No resource retry, failed assertion, deleted transition, or fitted tolerance was used. The failed mathematical shortcuts above are retained as failures.

## 7. Precise remaining microscopic obligation

The new finite-k theorem is strictly weaker than the actual volume-uniform local microscopic-output objective, and supplies a real dynamical component rather than assuming that objective. It retires the need for a new absorption lemma for a **single leading rotor hole in the specified infinite-lattice finite-global-excitation representation**. It does not retire the following obligations:

- An actual source-weighted local decomposition or connected-cluster estimate must control coherent overlapping B backgrounds, not simply replace extensive global N_B by a local count. To use the exp(O(k)) constants, its cluster weights must dominate the required weighted response constants uniformly in volume. Bare occupation density or O(epsilon²) defect population alone supplies neither statement.
- Several simultaneous holes, their interference/contact losses, and coupling to the nominally slow source are outside this one-hole theorem. The previously constructed dense W=2 leading dark sector remains relevant at its own scope.
- Finite-spin boundary zeros, exact finite-spin compensation, dressed original jump corrections, preparation from Omega, and microscopic remainder accumulation require their own estimates. The unit selected rotor path is essential to (8); it cannot be silently retained at spin boundaries.
- Passing from large periodic volumes to the Z³ finite-excitation representation for a local response requires an explicit localization/limit argument. Equation (21) prohibits declaring arbitrary periodic-volume, arbitrary-field uniformity on the strength of (13). It does not refute a local limit with actual controlled source and field tails.

A sufficient next lemma would bound the actual local marked/field response expansion by summable connected finite-excitation contributions with the constants in (16), together with a controlled error for multiple holes, finite-spin transfer and the microscopic normal-form remainder. Proving that full lemma is comparable in strength to the remaining local-output bridge; it is stated as missing, not inserted as an assumption and called closure. The independent source-weight route may supply one factor, but its multiplication with this response bound is not automatic in a coherent many-body process.

Closest prior results and the refreshed open-proposal inventory are recorded in CONTRACT.md and SOURCE_IDENTITIES.json. The old global-k<=9 absorption theorem is contained at its declared geometry but has a different proof. The finite-island result supplies lower lifetimes as k grows and is consistent with the present exponentially small k-dependent upper rate. PR9399's actual effective thermodynamic construction explicitly leaves microscopic elimination open; only its inspected scope/premise sections are used here. No exhaustive external novelty claim is made.
