# Local first-original-mark response in arbitrary distant rotor background

Authored research, September30,2026. This is a provisional proof with exact controls, awaiting a focused independent check. It is not a formal review/audit, microscopic-limit theorem, finite-spin theorem, or native-law adoption.

The actual leading one-hole rotor response admits an **all-fast-time local instrument comparison controlled by an initial regional excitation count**, rather than the global occupation of its distant background. The count is

    K_D=N_B(D)+|Q_D|,  Q_D=sum_(x in D)(q_x-1_A(x)).     (1)

For charge-neutral D this is just its occupied-B count. The hole must initially lie well inside D and the state must have a stated cap on (1). The exterior may have arbitrary occupation, fields and coherence, including entanglement with D. No empty annulus, field cutoff, zero electric preparation or static B mask is needed. The comparison retains the original first-mark/time labels and bounded local postmark charge/field readouts, also with a noninteracting reference ancilla.

The two new steps are a Gauss-compatible CP reference completion preserving the physically allowed regional coherences, and an exact marked-prefix comparison whose late tail is controlled by the checked finite-excitation absorption theorem. The full microscopic source still needs probability/moment estimates placing its actual defects in this local class, as well as multiple-hole and finite-spin control.

## 1. Source, actual law, and reference theorem

Scientific main was refreshed to `30a9461ee19a49b99fa6628fe942f08e504e8903`; the selected campaign procedure remains `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. Exact source/proposal identities and read coverage are in SOURCE_IDENTITIES.json. The original narrower CONTRACT.md was frozen before its prefix controls. GENERALIZED_CONTRACT.md was frozen separately before the new Gauss-completion controls; neither historical target is rewritten.

Use the supplied A/B qutrit sites and integer rotors, oriented A to B, with div E+1_A-q=0. On an even cubic torus let W count vacant A sites. The unsigned hop f_ab takes an occupied A charge q_a into an empty B and shifts its link by -q_a. Its adjoint reverses that map. With F_a=sum_(b~a)f_ab and Q_a the occupation product over the eighteen other distance-two A centers, the actual leading compensated rotor coefficient and original loss are

    H=C+[F,F†],       C=sum_a F_a†F_a Q_a,
    G=sum_m j_m†j_m
      =2*(empty B neighbors of the unique A hole),
    A=-i delta H-kappa G/2,   S(t)=exp(tA).              (2)

Here delta,kappa>0 and t is the leading fast time. The original marked maps are sqrt(kappa)j_m S(t). A mark is either the stipulated resolved sign or the stipulated unnormalized coherent edge sum. Their losses agree; their recycling maps are retained separately. The dynamics stops at its first original mark in this response problem.

The exact hole-position blocks, including every charge/field translation, are

    P_h H P_h=P_h[F_h F_h†
                -sum_(a:dist(a,h)=2)F_a†F_a]P_h,
    P_a H P_h=P_a[F_a,F_h†]P_h  (a!=h).                (3)

The second line vanishes unless a,h share a B. Distinct-B cross paths cancel; same-hole terms can reshuffle a B particle. All variables accessed by a row with input hole h lie within graph distance three of h, while the output hole moves at most two. Local operator norms give ||H||<=744; use M=1092 as a convenient checked upper bound. Thus, on W1,

    ||A||<=b:=delta*M+6kappa,   0<=G<=12,
    ||J||<=sqrt(12),   J=(j_m)_m.                      (4)

These bounds are uniform in total B occupation, fields and volume. No extensive F norm is used. On W0 the rotor coefficient (2) is exactly zero: C cancels F†F and F† annihilates that sector. For proof-space comparisons the W1 operators can simply be extended by zero outside W1; this bounded extension changes none of the physical one-hole evolutions considered here.

The fully read focused receipt independent-finite-cluster-absorption-check/REPORT.md `d3ba3e9cc28a3062663cb9c6f3acc79b533f945dbd403734affef3c8910917e1` checks author REPORTf0947fc4 and periodic refinementb636eb31. Their relevant result is: for every physical odd global j, on even sides L>=4j (with the direct-loss small-j cases understood), the same actual S has

    ||S(t)||_(W1,N_B=j)<=C_j exp(-gamma_j t),
    C_j>=1, gamma_j>0, log(gamma_j^-1)=O(j).            (5)

For j<=5 one may take C_j=1 and gamma_j=kappa(6-j). For larger j use the explicit periodic-height constants in the checked source. Put

    C_K=max_(odd 1<=j<=K) C_j,
    gamma_K=min_(odd 1<=j<=K) gamma_j.                  (6)

They bound the full direct sum over j<=K, including its coherences and arbitrary spectator ancillas. In particular C_K<=exp(1/4), and at fixed delta,kappa the inverse gamma_K grows at most exponentially in K. This checked input is used at its actual scope, not as an assumed arbitrary-background absorption theorem.

## 2. Precise initial support and output topology

Fix an A-centered graph ball B_r contained in D=B_R, with integers R>=r+1, K>=1, and an even side

    L>=max(2R+6,4K).                                  (7)

The regional tensor factor consists of sites in D and links with **both** endpoints in D. Crossing links belong to the exterior. The geometric condition makes this ball and its relevant local paths unaliased. The input rho, possibly entangled with an arbitrary noninteracting ancilla Z, is a physical trace-one density in global W1, supported on

    hole in B_r,          K_D<=K.                      (8)

Only (8) is assumed about its regional occupations. B sites in the annulus may be occupied; their number is included in (1). A charges, all electric fields and the exterior B count are otherwise unrestricted, subject to the physical Gauss constraints. In particular the exterior need not be classical or independent of the interior. Nothing projects onto (8) as an additional observed record; it is a mathematical input hypothesis. Section8 gives a probability-error version for an input not entirely in this subspace.

For any retained local cell set X inside D, retain the original mark m, its first time t, and the postmark density on X and Z. The subnormalized instrument density is

    sigma_m^rho(t)=kappa Tr_(system outside X)
                   [j_m S(t)rho S(t)† j_m†].            (9)

The response distance is

    sum_m integral_0^infinity
             ||sigma_m^rho(t)-sigma_m^ref(t)||_1 dt.    (10)

On each finite torus A and the complete marked stack are bounded on W1. The densities in (9) are trace-norm continuous and their positive total trace integrates to at most one by the loss identity. Thus these are genuine trace-class integrals and normal CP instrument maps into the classical-time/mark L1 space. No operator-norm measurability premise for an unbounded electric generator is being borrowed from the effective-law locality source.

It controls all bounded measurable functions of the actual first mark/time and every bounded local charge/field test, including spectral projectors. It also controls the deficit of total first-mark probability. It does not weight late times or arbitrarily large electric values by an unbounded function. The exterior postmark state is traced out; it is not silently identified with an unchanged actual global state.

The constants below hold after every ancilla amplification. Equivalently they bound the induced completely bounded trace norm on this physical input class. A bound for positive unit-trace amplified states extends to Hermitian trace-class inputs by positive/negative parts and to general inputs by the usual Hermitian off-diagonal block embedding. No finite local rotor dimension is assumed.

## 3. Physical boundary deficits and a coherence-preserving completion

For a regional site define

    d_x=q_x-1_A(x)-div_internal E_x.                    (11)

The operators d_x commute and have integer spectrum. Interior Gauss forces d_x=0 away from the boundary. At a boundary site, physical Gauss equates d_x to the signed divergence of its crossing-link fields, which act entirely on the exterior tensor factor. Let P_d denote the joint regional spectral projections of the boundary vector d.

For a physical global state, distinct d sectors are accompanied by orthogonal exterior crossing-divergence sectors. Therefore the reduced state on D and Z satisfies exactly

    sigma_DZ=sum_d (P_d tensor I_Z) sigma_DZ
                         (P_d tensor I_Z).             (12)

This follows by inserting the matching regional/exterior spectral projections on both sides of rho and tracing the exterior; an off-diagonal pair of orthogonal exterior projections has zero partial trace. It does not assume the global state is diagonal or separable. Coherences within each d block, including arbitrary ancilla coherences, remain. Also sum_x d_x=Q_D, since internal edge divergences cancel.

For each allowed d, put Q=sum_x d_x. Construct a fixed exterior physical basis completion as follows:

1. Keep every exterior A plus. At |Q| predetermined, distinct exterior B sites put charge -sign(Q); leave all other exterior B vacant.
2. At each regional boundary site x choose one crossing edge and assign its flow so the outward crossing divergence is d_x.
3. On a connected exterior spanning tree solve the remaining integer divergence with the chosen exterior charges. Its total is zero: the added charges total -Q and the crossing flows contribute total -Q to the exterior divergence, so their residual cancels.

These operations define an exterior basis vector chi_d depending only on d, not on the detailed internal word. Integer tree-flow solutions exist for every zero-sum integer divergence, with no bound on the sizes of d_x. The large opposite boundary fluxes allowed by Gauss are not truncated.

Here is a concrete geometry check on existence. Since R<L/2, the complement of B_R is connected: from any exterior vertex, move a nonzero coordinate away from zero to its opposite torus plane, never decreasing its distance from zero; use that exterior plane to join the other opposite-coordinate planes and a chosen root. A boundary site has a neighbor outside D. The plane x=L/2 lies outside D and contains L²/2 B sites, at least K under (7). It supplies the needed |Q|<=K completion sites. A fixed exterior tree can include those sites and every crossing endpoint. No boundary condition is changed in the actual model.

Let V_d append chi_d. On admissible regional states define the normal CP extension

    E_D(sigma)=sum_d V_d P_d sigma P_d V_d†.            (13)

It is trace preserving on the supported class in (8), and its regional partial trace is sigma by (12). The same identity holds on D and Z after tensoring the identity on Z. The countable sum converges in trace norm on positive trace-class inputs and extends normally; restricting its input to the physical/interior-Gauss and (8) support gives a CP trace-nonincreasing extension to arbitrary trace-class inputs if one is desired.

There is no cloning of an arbitrary electric-field state. A completion conditional on a nonsuperselected fine field value could destroy local coherences and would be invalid. Equation (13) conditions only on d, across which the physical reduced state is already block diagonal, and appends the **same** chi_d to every word within that block. These are mathematical Kraus/block labels, never extra observed record labels.

Every resulting global reference word satisfies Gauss, has W1 and has

    N_B^ref=N_B(D)+|Q_D|=K_D<=K.                       (14)

The parity is automatic. On a regional one-hole word, Q_D is congruent to N_B(D)-1 modulo two; hence the right side of (14) is odd. Coherences between different N_B(D) values with the same d are preserved, and (5)-(6) apply on their entire direct sum. Arbitrary individual boundary fluxes may make the reference fields large, but the bound (5) is field uniform. No exponential or polynomial electric preparation norm has entered.

The reference input is rho_ref=(E_D tensor I_Z)(sigma_DZ), on the **same torus and same original law and mark set**. Its exterior preparation is a comparison construction, not a claim that the actual exterior was reset or that the source supplies this state.

## 4. Exact local no-event and marked prefixes

Let

    m=floor((R-r-1)/2),       n=m+1.                   (15)

Starting with its hole in B_r, a word of j factors A can move the hole at most2j. At the next factor, (3) accesses only radius three about its current hole. Consequently every coefficient through degree j>=1 changes or depends on variables only in B_(r+2j+1). Its fields and B occupations may reshuffle; the support statement does not require a static mask. The original j_m after j factors accesses at most the same B_(r+2j+1), because it fills the current hole and one neighbor. For j=0 its support is in B_(r+1).

Thus all no-event coefficients A^j and marked coefficients j_m A^j through j=m, on the input hole support, are the same regional operators in D for actual and reference states. An edge mark outside D has zero coefficient through this order. The cancellation (3) is essential: one cannot replace it by a divergent global F series, an extensive norm bound, or an exterior Hamiltonian acting independently before the hole arrives.

For completeness, the comparison of arbitrary entangled states is legitimate, not classical conditioning on their exterior. The actual and reference states have exactly the same reduction on D and Z by (13). Purify both and align their exterior purifications by an isometry, enlarging the unobserved exterior if needed. This follows directly from their common spectral decomposition/Schmidt coefficients on D and Z; it acts as the identity there. After alignment their initial purified vector is the same. Exterior conjugation commutes with every early regional coefficient just described, so their no-event and marked vector coefficients agree through j=m.

This alignment is only a proof-space identification. Each physical evolution before identification is the full original rotor model. Their bounded W1 generators, extended by zero if necessary before conjugation, have the same bound b in (4), and their marked stacks have norm sqrt(12). Partial trace of the unobserved exterior after alignment leaves the retained X and Z output unchanged. The alignment may depend on the input state; the resulting uniform bound holds for every state and every ancilla, which is sufficient for (10). No single state-independent unitary resetting the real background is asserted.

For t>=0 define the scalar exponential remainder

    u_n(t)=exp(bt)*(bt)^n/n!.

Taylor's series and prefix agreement give on these aligned unit vectors

    ||S(t)psi-S_ref(t)psi||<=2u_n(t),
    ||J S(t)psi-J_ref S_ref(t)psi||<=2sqrt(12)u_n(t).
                                                               (16)

These estimates hold on the complete carrier with actual electric translations. Neither generator was compressed to D and no hole-exit measurement was inserted. This matters: such compression could remove the coherent paths responsible for the reference absorption.

## 5. All-time original-instrument localization

Choose

    T=n/(8b),          q=exp(9/8)/8<1.                 (17)

The elementary factorial bound n!>=(n/e)^n gives u_n(t)<=q^n for 0<=t<=T. The first-mark prefix and its original no-event-at-T component have the proof dilation

    V_T psi=(S(T)psi,
             {sqrt(kappa)j_m S(t)psi}_{m,0<t<T}).       (18)

Its squared norm is one by the original loss identity. The L² time/mark space in (18) is a mathematical dilation of the existing timestamp instrument; it does not declare different event times to be an extra coherent readout. Applying its spectral time/mark readout into the classical L1 output space, and tracing unwanted system factors, are contractions. No trace-class diagonal multiplication operator on a nonatomic time Hilbert space is asserted.

Equations (16)-(18) imply

    ||V_T psi-V_T,ref psi||
                   <=2 sqrt(1+12kappa T) q^n.          (19)

The trace-norm difference of the two finite-prefix instrument outputs is therefore at most twice this number. Independently, the checked reference bound gives

    ||S_ref(T)psi||<=C_K exp(-gamma_K T),
    ||S(T)psi||<=a_K,n:=C_K exp(-gamma_K T)+2q^n.       (20)

No decay assumption was made about the unrestricted actual background. Its probability of any first mark after T is at most its surviving norm squared at T, even if some of the remainder never produces a mark. The reference late mass is at most C_K² exp(-2gamma_K T). Combining the early difference with these two positive late tails proves

    sum_m integral_0^infinity
          ||sigma_m^rho(t)-sigma_m^ref(t)||_1dt
       <= eta_K,n,

    eta_K,n=min{2,
          4 sqrt(1+12kappa T) q^n
          +[C_K exp(-gamma_K T)+2q^n]^2
          +C_K² exp(-2gamma_K T)}.                     (21)

For fixed K this tends to zero as R-r increases, uniformly over all allowed torus volumes, distant occupations, charges and electric states. It has an explicit spatial response length of order b/gamma_K, up to the displayed constants and logarithmic/polynomial factors. This can grow exponentially with K. There is no efficiency claim about the deliberately conservative reference rate.

In particular two actual inputs with the same regional reduction and satisfying (8), but completely different distant backgrounds, have response distance at most2eta_K,n by their common reference. This is the promised all-time exterior-independence statement at a declared local excitation cap; it is not a global-k restatement.

The original spatial mark itself also localizes. Every mark with at least one endpoint outside D has zero prefix coefficients through m. Hence its pre-T mass is at most12kappa T q^(2n). All later mass and any permanent no-first-mark deficit are bounded by (20). Therefore

    Pr(first original mark outside D)
       +Pr(no original mark ever)
        <=12kappa T q^(2n)+a_K,n².                    (22)

The second term is a mathematical missing-mass bound, not an added detector channel. Equivalently an original first mark inside D occurs with probability at least one minus the right side. No probability of an unobserved quantum first exit has been defined. Likewise surviving no-event local states can be compared uniformly at all times: use (16) up to T and the sum of the two surviving masses from (20) after T.

## 6. Why this is not a static-cluster or infinite-moment theorem

The count (1) is an **initial** support condition. H can change N_B(D) and Q_D by moving across the boundary, and can rearrange B occupations without moving the hole. For example with hole0 and occupied b=e_x, the actual positive term f_(0,e_y) f_(0,e_x)† moves that B charge to e_y while leaving the hole at0. The exact integer-field control gives matrix element+1; other paths have different actual field words. Thus a proof treating the B mask or an initially empty shell as invariant would be false.

An exterior resolvent/absorbing-boundary approach would require a quantitative bound on the full interface response, retaining these moving charges and field translations. A scalar damping rate assigned permanently to an initially empty geometric shell would not supply it. The present proof instead permits all such motion, bounds the exact finite prefix before distant data can act, and uses the physical finite-excitation reference to cap the total late mass. This avoids the unresolved interface-resolvent hypothesis for the bounded topology (10).

Equation (21) is a norm estimate for bounded outputs. A small late mass does not by itself control a positive waiting-time moment or an unbounded local electric-energy moment carried by that mass. The proof establishes neither an actual-background exponential waiting tail nor a weighted-field response bound uniform over arbitrary distant preparations. The previous periodic near-dark and filled-island results warn against replacing those missing estimates by an unconditional damping premise; they are not, by themselves, counterexamples from an input satisfying the useful small-error regime of (8),(21).

## 7. Exact source controls and their limits

check.py uses the previously checked elementary charge/rotor conventions, implemented locally without importing or executing an older runner. It keeps Gaussian-integer coefficient pairs, not floating complex arithmetic. It compares the actual generator A=-iH-G/2 on a finite physical core with the same core plus a distant original two-B birth word and an exterior integer electric loop of flux19.

For the k=1 core, the degree0/1/2 no-event vectors have1,61,1832 words. All coefficients agree after stripping the unchanged exterior. Both actual original instruments agree with their reference coefficients through the same degree; degree2 has21,366 marked output words. The complete stacked original jump norm equals the diagonal G form, including all coherent additions, at every tested degree. For k=7, the degree1 comparison has160 no-event words and480 marked words. All generated states satisfy Gauss. Hole displacement and changed-cell support obey the exact radius bounds, and the non-static B reshuffle above has coefficient1. Runtime:5.772782 CPU seconds,5.781939 wall seconds,124,993,536 bytes peak RSS, under the declared30 CPU second/150 MB price and one-thread environment.

check_completion.py is a separate integer spanning-tree construction on L32, D=B3. It verifies20 complete physical words, with local B counts0 through7, positive/negative/zero regional charge, and opposing boundary deficits of size100003 or100005. The reference global counts are exactly N_B(D)+|Q_D| and always physical odd values1,3,5,7. Every Gauss equation on all32³ sites is checked. Each pair of regional words differs by a nonzero internal electric circulation but has the same d; its exact exterior completion is identical, so its within-sector off-diagonal coefficient is preserved. The exterior graph has32,705 vertices and is connected. Runtime:1.991058 CPU seconds,1.992612 wall seconds,62,259,200 bytes peak RSS. The arbitrary-field CP and ancilla claims rest on the spectral proof in section3, not these finite samples.

RESULTS.json and COMPLETION_RESULTS.json bind their runner hashes and actual resource measurements. No dense physical Hilbert enumeration, tolerance fit, truncated rotor transition or failed-control suppression was used. These are source-specific corroborations of the new proof; they are not independent review.

## 8. An approximate support version without adding a measurement

Within the leading physical W1 input class let P be the commuting projection onto the hole-in-B_r and K_D<=K conditions. If epsilon=Tr[(I-P)rho], set rho_good=P rho P. The trace inequality

    ||rho-rho_good||_1<=2sqrt(epsilon)                 (23)

follows by purification and contraction and includes all good/bad coherences. The exact original first-mark map is CP and trace nonincreasing, hence trace-norm contractive on Hermitian inputs. Apply (21) to the subnormalized good input. This gives the actual comparison with its good-reference response bounded by

    2sqrt(epsilon)+eta_K,n Tr(rho_good).               (24)

The projection is used only to bound a state difference; it is not physically performed and does not resolve an additional mark. The required probability epsilon is still an input/source estimate, not supplied by the response theorem. In particular one cannot label the actual microscopic ensemble a mixture of independent classical clusters on the strength of (24).

## 9. Remaining source-weighted bridge and closest prior scope

This proof supplies a genuine leading rotor local-response component with arbitrary distant background. Its local cap includes the charge-completion cost; a small B count alone does not control an unrestricted regional charge deficit. For a neutral source component it reduces to its local B count. The hypotheses and the all-time bounded-output conclusion are weaker than the full microscopic original-output objective, not a hidden restatement of it.

To obtain useful source-weighted bounds one still needs actual estimates on spatial hole support and the regional distribution of N_B(D)+|Q_D|, with coherent correlations retained. The dependence on R and K must be checked together: at fixed positive excitation density one expects counts growing with the region, while the present inverse gamma_K can grow exponentially in K. Simply letting R grow with K proportional to R³ does not make the displayed error small. An independently checked source expansion or improved typical-cluster response estimate is needed to address that issue.

Multiple simultaneous holes, coupling of the fast response to later source formation, finite-spin zero boundary amplitudes and compensation, the microscopic preparation/remainders, and unbounded local field-energy integrability remain separate. No physical M4 law, record interpretation, compensation or clock selection follows from the supplied mathematics.

The closest landed locality source, LOCAL_VOLUME_DYNAMICS_WITH_COMMUTING_ELECTRIC_TERMS..., was read fully. It concerns finite-horizon locality of the A-occupied effective target with an unbounded commuting electric term. The refreshed PR9399 thermodynamic source sections4-7 were read fully: they construct finite-horizon effective local maps and original regional timestamp instruments by connected series, while leaving microscopic elimination open. Those arguments do not provide (21), which uses the distinct bounded W1 cancellation, physical Gauss completion and finite-excitation absorption. No external theorem with unchecked continuity or finite-dimensional hypotheses is imported here, and no exhaustive novelty claim is made.
