# Independent finite-spin fast-response reconstruction before author exposure

Only the new CONTRACT has been read. Its title, target, proposed passive absorbing-output mechanism, weighted-smallness strategy and scope are disclosed exposure. New PRE_DERIVATION, REPORT, code and results remain unread. Prior exposure is substantial: the actual main compensation/formation laws and one-hole rotor cancellation were read in this continuing session, and the complete finite-k/periodic absorption source and focused receipt were just checked in the preceding local-response task. The complete polynomial-weighted response proof and independent receipt have now been freshly read. This is a new independent derivation of the transfer and its constants, not blind discovery of its proposed strategy.

Main30a9461ee19a49b99fa6628fe942f08e504e8903 and procedures7146 remain selected. The supplied quantum/rotor carrier, compensation, vacuum, rate, fast time, global odd k, norm and preparation are imports, not native selections. No new author conclusions are used below.

## 1. Common carrier, exact spin law and domains

Use W1 and fixed physical odd global N_B=k on Z3 in the finite-change representation, or even tori in the checked safe-volume regime: L>=max(6,4k) is sufficient, using direct-loss or the checked small-k theorem below k7. Put Q=1+sum_links |E| and C=S(S+1), integer S>=1.

On one integer rotor link define the locally zero-extended normalized spin shift by

    U_(S,sigma)|m> = a_S(m,sigma)|m+sigma>,
    a_S² = 1-m(m+sigma)/C if both endpoints lie in[-S,S],
           0 otherwise,         sigma=+/-1.

This is a local link extension, NOT multiplication of all terms by the global spin-box projection. The latter would create volume-dependent errors even on unrelated links. The product physical spin box P_S reduces the locally extended dynamics. On it the operators agree exactly with the finite-spin model, including forbidden boundary transitions.

Write the full compensated leading spin Hamiltonian as

    H_S = Hbar_S + Delta_S,
    Delta_S=sum_a [D_(a,infinity)-D_(a,S)]Q_a.

Hbar_S obeys the same exact hole-local cancellation as the rotor H, with every f replaced by its spin-weighted f_S. In particular it includes same-hole B reshuffles and shared-B commutators. It is bounded self-adjoint uniformly in volume/spin, with norm<=744. Delta_S is a nonnegative diagonal operator and is not dropped or uniformly bounded in unweighted norm. On Z3 it is defined first on finite-change words and then as its diagonal multiplication closure. On finite tori it is bounded by a volume-dependent constant. In both cases

    0<=Delta_S<=Q²/C.

Indeed each eligible link contributes1-a_S², bounded by |m|(|m|+1)/C, and the gated link sum is bounded by[(sum|E|)²+sum|E|]/C. Thus D(Q²) is contained in D(Delta_S). H_S is self-adjoint on D(Delta_S) by bounded perturbation. With G_S=J_S*J_S<=12, A_S=-i delta H_S-kappa G_S/2 generates a contraction semigroup with the exact original loss identity. No absorption or spectral-gap theorem for the spin dynamics is assumed.

## 2. Weighted coefficient estimates without a field cutoff

For every integer m and either sign,

    0<=1-a_S(m,sigma)<=|m|(|m|+1)/C.

Inside the box this is1-sqrt(1-x)<=x. For every excluded endpoint, |m|(|m|+1)>=C; the same bound holds. For a two-hop original word, let q be its initial Q. The first link error is at most q(q-1)/C; after one shift the second is at most q(q+1)/C. Since both spin weights are contractions, their product differs from its rotor unit coefficient by at most2q²/C. Hard-core blocking is common to both words; the spin zeros are included by these estimates.

A conservative row/column count for the cancelled one-hole Hamiltonian is19*36+60=744 two-hop words: nineteen diagonal blocks and at most thirty shared-B paths with two orderings. Each word is a partial permutation of actual charge/field basis vectors. Applying the weighted Schur bound to the complete matrix gives

    ||(Hbar_S-H)Q^-2|| <=1488/C,
    ||(H_S-H)Q^-2|| <=1489/C.                         (P1)

Using5 rather than2 for the elementary product estimate would also be safe; the sharper2 follows by retaining q(q-1)+q(q+1). These constants are independently chosen and need not coincide with the author.

For the actual resolved or coherent-edge stack, the two sign outputs on a fixed edge are orthogonal charge subspaces. Original edge labels remain distinct. Therefore its difference norm is computed by an input-diagonal squared-weight sum, yielding the safe estimate

    ||(J_S-J)Q^-2|| <=sqrt(12)/C.                     (P2)

The total birth loss on an eligible edge differs by at most2m²/C (including exterior-to-box fields); sum the six incident edges to obtain

    ||(G_S-G)Q^-2|| <=2/C.                            (P3)

Consequently, for D_S=A_S-A on D(Q²),

    ||D_S Q^-2|| <=d/C,       d=1489 delta+kappa.     (P4)

These are total-field-weight estimates. Replacing Q by a local weight or discarding far compensation is not justified by them.

## 3. Integrable rotor response and valid Duhamel formula

Use the checked fixed-k rotor estimate ||S(t)||<=C_k exp(-gamma_k t). The polynomial theorem gives graph-domain invariance and

    ||Q² S(t)psi||<= f(t)||Q²psi||,
    f(t)=C_k exp(-gamma_k t)R2(t),
    R2(t)=1+8 beta t+4 beta²t²,
    beta=5 C_k delta M,        M=1092.                (P5)

Both f and f² are integrable. In particular

    I1=integral f =C_k(1/gamma+8 beta/gamma²+8 beta²/gamma³),
    I2=(integral f²)^(1/2),

with I2² evaluated exactly by expanding R2² and integrating each monomial. At fixed k and couplings these are finite and independent of allowed volume. Their growth in k can be large; no extensive-background statement follows.

For psi in D(Q²), S(t)psi belongs to D(A_S), and D_S S(t)psi is continuous and integrable in Hilbert norm. The variation-of-constants identity is therefore valid despite unbounded Delta_S:

    w(t):=S_S(t)psi-S(t)psi
         =integral_0^t S_S(t-s)D_S S(s)psi ds.         (P6)

It follows first on this common graph domain by differentiating S_S(t-s)S(s)psi and then closing; it does not require a spin graph-norm growth estimate or a bounded unweighted generator difference.

## 4. Passive output comparison, including continuous timestamps and terminal survival

For horizon T define the actual original proof dilation

    V_(S,T)psi=(S_S(T)psi,
               {sqrt(kappa)j_(S,m)S_S(t)psi}_{m,0<t<T}),

and V_T similarly for the rotor. Both are isometries by loss conservation, regardless of spin eventual absorption. The L2 mark/time factor is a proof space, whose original time/mark measurement gives the classical L1 instrument. No trace-class diagonal multiplication operator in a nonatomic time Hilbert space is presumed.

For a forcing f_s at time s, the response at terminal T plus all its later original marks before T has norm||f_s||, by the same loss identity over[T-s]. Minkowski's inequality in the joint terminal/L2-output Hilbert space gives the passive estimate

    ||(w(T),sqrt(kappa)J_S w(.))||
                 <=integral_0^T ||D_S S(s)psi|| ds.    (P7)

This controls output error on arbitrarily long horizons without a spin decay theorem. The remaining direct output discrepancy is sqrt(kappa)(J_S-J)S(t)psi. Equations(P2),(P4),(P5) give uniformly for every T,

    ||(V_(S,T)-V_T)psi||
       <=[d I1+sqrt(12kappa) I2] ||Q²psi||/C.          (P8)

The terminal no-event component is included, and all original mark/time components remain separate. The two original instruments are compared separately. The same estimate holds with a spectator ancilla, by the same graph-domain and passive argument.

For a positive unit-trace input rho in the physical spin box with finite Tr(Q^4 rho), purification or a positive spectral sum and Cauchy–Schwarz yield the uniform trace-norm instrument bound

    sup_T distance(output_S(T),output_rotor(T))
       <=2[d I1+sqrt(12kappa) I2] sqrt(Tr(Q^4 rho))/C,  (P9)

capped by2. Output includes the terminal no-event quantum density and continuous first-mark/time quantum instrument. Partial traces and bounded record/field tests are contractions. Finite trace norm alone is not used to claim an unbounded output-energy estimate.

Letting T increase gives the same bound for the entire first-event instrument by monotone convergence of its nonnegative integrated distance. Rotor survival vanishes. Separately(P6) bounds the spin survival amplitude by d I1||Q²psi||/C asymptotically, hence its permanent no-event probability is at most(d I1/C)²Tr(Q^4 rho). No normalizable limiting quantum no-event state at T=infinity is assumed: finite-T terminal densities may keep rotating. Nor is exact spin absorption inferred from small missing mass.

## 5. Preparation and the physical spin interpretation

The common zero extension on arbitrary rotor vectors is only a comparison construction. The actual finite-spin statement requires an input in P_S, or an explicitly priced approximation to a rotor input. For a fixed rotor density rho with fourth Q moment m4, let p_S=Tr(P_S rho). The complement implies Q>=S+2, so1-p_S<=m4/(S+2)^4. If p_S>0, normalized rho_S=P_S rho P_S/p_S is physical and has moment at mostm4/p_S. Its trace distance from rho is at most2sqrt(1-p_S), by a projected purification. Combining this initial error with(P9) proves uniform-horizon convergence. No common-field projection deletes a physical transition; the box is invariant for the actual finite-spin generator.

The theorem is still a fixed-global-k leading fast-response transfer with total-field input control. It does not compose automatically with arbitrary distant backgrounds, the local response theorem, moving-high-field preparations, simultaneous holes, or the recurrent microscopic source. It does not prove moment convergence of the complete output unless that is established in a stronger weighted topology.

## 6. Initial exact-control price

One <=5CPU seconds/60MiB standard-library exact-rational control, hard CPU5seconds, BLAS/OpenMP1, original deadline and both STOP forms checked. Test the actual locally zero-extended squared spin weights including beyond-box inputs, compensation error, exact coherent/resolved loss, and two-shift weighted estimates for equal/different links and both signs. Rational comparison of squared weights avoids floating square-root tolerance. No author implementation is read/imported, no dense carrier is enumerated. The passive/domain theorem is analytic; finite samples are not substituted for it.
