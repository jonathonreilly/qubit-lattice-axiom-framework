# Focused check: polynomial-weighted original fast absorption

The polynomial extension's mathematical conclusion is supported at its stated sector. Its displayed constants and recurrence agree with an independent graph-norm/Duhamel derivation. A finite Q^p norm suffices; exponential-field integrability is unnecessary for this polynomial-weighted surviving/first-output estimate. This is a focused independent mathematical check, not formal review, audit status or a full microscopic closure.

## Independence and exact scope

PRE.md was frozen at SHA256 `6af203a5cb3495fbbd21189d9961642b6e524b81476f9ae2075a67a24bf59cea`. It discloses all formulas supplied in the parent brief, including the proposed h_r, Touchard recurrence and output constant. No claim of blind coefficient prediction is made.

INDEPENDENT_DERIVATION.md was then frozen at SHA256 `9b815841ed41c4bcac1217edb4041b7c66c6a55765a62f7a42f87437d7deddaa`, before reading either FAST_ONE_HOLE_ABSORPTION.md or the root extension. It proves graph-domain invariance for the original generator and directly derives a recurrence for Q^p S(t). The author's extension instead organizes the estimate by iterated commutators of S(t); the derivations meet at the same generating function. No author code or finite-carrier proxy was imported.

After that freeze I read the complete frozen FAST_ONE_HOLE_ABSORPTION.md, SHA256 `3950bd73aea13b20fac74585c639fb5903bde25cac1a7d2f9308ab771ce6371c`, and complete DARK_WORD.md. I subsequently read the complete root polynomial-fast-absorption-extension/REPORT.md, initially bound at SHA256 `171cf39e8ea5cb87a924c768fd951e1867e565e8f08af4df50ea375a254d59c8`, and its FREEZE.json. This final receipt binds the corrected source SHA256 `93adfdad602cfbc0c5b5cb48a38fd1c67693208856a9e1e0d53f2f236bd85f15`: I inspected its entire exact diff, consisting only of the two wording clarifications recorded below; formulas and hypotheses are unchanged. The parent's separate small-sector independent report was mentioned in the brief but not read or used as proof here. The checker's own large-background fast-route report is not a premise.

The sector is the actual supplied rotor/qutrit/Gauss carrier on each even cubic torus L>=6, W=1 and GLOBAL N_B<=9, fixed delta,kappa>0. H is the actual compensated second-order rotor coefficient, G the actual original loss, and the jump stack retains either resolved signs or the original unnormalized coherent-per-edge signs. This result does not concern arbitrary global backgrounds, finite-spin generator replacement, many holes, or the full process from bare Omega.

## 1. Reconstructed source hypotheses

The actual sign is H=C+[F,F†] for T=-F-F† and first generator F†-F. It commutes with W and total N_B. At rotor order C=sum_a F_a†F_a Q_a with the original eighteen-neighbor occupancy gate. This is not the low-P coefficient used outside P.

The source's incidence estimate ||F_a||²<=12 is justified directly: in a local block with m occupied B neighbors, an input has at most6-m outward paths, and an output has at mostm+1 refilling paths. The matrix is a phase-weighted incidence matrix with norm² at most(6-m)(m+1), whose maximum is12. Distinct m blocks are orthogonal. Electric translations and charges do not increase these row/column degrees. This yields the source's quadratic-form estimate

    |<psi,H psi>| <= [12+18*12+2*18*24]<psi,W psi>
                   =1092<psi,W psi>.

The cross commutator has norm at most24 and is supported on the possibility of a hole at one of its two A centers on both sides. The eighteen-neighbor sum gives the displayed factor. On W=1, M=1092 is therefore uniform in volume and field. The original rotor loss is diagonal with value twice the number of empty B neighbors of the hole, so0<=G<=12.

For a dark input with6<=N_B<=9, two distinct six-neighbor A stars have union size at least10. Hence a B mask has at most one dark center. Its six axial distance-two outputs preserve that mask, have different hole positions and at most4 occupied B neighbors. Each selected output is reached by one unit, invertible charge/field path. Other hole-moving inputs would require a second dark center in the same mask; fixed-hole reshuffles can remove at most one of six occupied neighbors and cannot reach an output with only4. Thus the full coherent dark subspace satisfies the source's lower bound ||G^(1/2)H psi_D||²>=24||psi_D||². This is not an incoherent basis-only argument.

For arbitrary psi, x=||G^(1/2)psi|| and y=||G^(1/2)H psi|| give

    ||psi||² <= y²/12+(M²+1)x²/2,
    G+HGH >= [2/(M²+1)]I.

For N_B<=5 direct loss already implies the needed bound. Empty physical sub-sectors cause no exception.

I checked every numerical factor in the source's decay construction. The Gram matrix of1,u on[0,tau] has determinant tau^4/12, trace<=4tau/3 for tau<=1, hence minimum eigenvalue>=tau³/16. The unitary Taylor remainder is at most R0 u² with R0=delta² sqrt(12)M²/2. Its chosen tau ensures the integrated remainder loss is at most c_delta tau³/64 after the factor1/2 inequality, yielding c_U=c_delta tau³/64. Volterra comparison contributes1+6kappa tau. The norm-loss identity then gives ||S(tau)||²<=1-a0, and iteration gives exactly C0=exp(a0/2), gamma=a0/(2tau). All constants are positive for the stated delta,kappa and uniform in volume/field; no spectral finite-box approximation is used.

Finally every term in H has at most two elementary link shifts, giving Q bandwidth2 for Q=1+sum|E|. The actual original birth has bandwidth1. G commutes with Q. These are the precise hypotheses needed below.

## 2. Independent bounded-domain argument

For fixed spectral difference d, define H_d=sum_n P_(n+d) H P_n. Orthogonal output spaces give ||H_d||<=||H||, with no absolute row-sum assumption. Thus for r>=1,

    K_r=ad_Q^r(A)=-i delta sum_(d=-2)^2 d^r H_d,
    ||K_r||<=2 delta M(1+2^r)<=5 delta M 2^r=:h_r,
    A=-i delta H-kappa G/2.

The finite-field core is invariant under this same A. On it,

    Q^p A=AQ^p+sum_(r=1)^p binom(p,r)K_r Q^(p-r).

Q>=1 controls every lower Q power by Q^p. Approximating the input in the graph norm and using closedness of Q^p proves that A maps D(Q^p) into itself and is bounded on the complete normed space with norm||Q^p psi||. Its graph-space exponential is the same Hilbert-space power series S(t). This proves domain preservation before differentiation. There is no silent assumption that Q is bounded and no generator with deleted electric-boundary transitions.

Variation of constants gives

    Q^p S(t)psi=S(t)Q^p psi
      +sum_(r=1)^p binom(p,r) integral_0^t
             S(t-s)K_r Q^(p-r)S(s)psi ds.

Induction gives the claimed bound with R_0=1 and

    R_p(t)=1+C0 sum_(r=1)^p binom(p,r)h_r
                                     integral_0^t R_(p-r)(s)ds.

Its formal generating function is

    sum_p R_p(t)z^p/p! = exp[z+x(exp(2z)-1)],
    x=5 C0 delta M t.

Consequently P_p=2^p Touchard_p(x), R_p=sum_r binom(p,r)P_r, exactly as in the root extension. In particular R_0=1, R_1=1+2x, R_2=1+8x+4x² and R_3=1+26x+36x²+8x³. The use of a formal exponential generating function does not assume an exponential-field norm for psi.

The root's alternative identity for C_p(t)=ad_Q^p S(t) also checks: differentiate the commutator on the common graph domain to obtain C_p'=AC_p+sum_(r>=1)binom(p,r)K_r C_(p-r), with C_p(0)=0. Duhamel and induction supply its bounded extension. The two factors C0 give C0² inside the integral; the recurrence absorbs exactly one, leaving the stated C0 outside. There is no missing factor of C0 or2.

## 3. Original output, moments, and interpretation

The actual labelled stack J has J†J=G<=12. Decomposing into three rectangular Q_out/Q_in bands gives norm<=sqrt(12) for each. On a nonzero band from n to n+d, n>=1 and |d|<=1 imply(n+d)/n<=2. Therefore

    ||Q_out^p J Q_in^-p||<=3 sqrt(12)2^p.

Closing this identity on finite-field inputs also proves that J preserves the required input/output weighted domains. The direct sum is over actual original marks; coherent signs within one edge remain coherent.

Squaring this bound and using the verified semigroup estimate gives exactly

    kappa sum_m integral_0^infinity ||Q_out^p j_m S(t)psi||²dt
      <=108 kappa 4^p C0² I_p ||Q_in^p psi||²,
    I_p=integral_0^infinity exp(-2gamma t)R_p(t)²dt.

For R_p²=sum_j d_j t^j, I_p=sum_j d_j j!/(2gamma)^(j+1). All terms are finite and nonnegative. Additional NONNEGATIVE integer waiting-time moments r use(j+r)!/(2gamma)^(j+r+1); negative waiting-time moments are not established. The time convention is exactly that of S(t), with original absorption density kappa||J S(t)psi||². Unweighted total absorption equals||psi||² by norm loss and the survival limit; the p=0 weighted constant is a loose upper bound, not a normalized probability.

The moment here is the2p-th total absolute-field weight of the surviving state or its FIRST original absorbing output. It is not an unbounded-observable consequence inferred from trace-norm convergence. Finite Tr(Q^(2p)rho) is sufficient for positive mixed inputs: diagonalize rho, note that every positive-weight eigenvector lies in D(Q^p), apply the pure-input inequality and sum by Tonelli. The same proof gives Tr(Q^(2p)S rho S†)<=C0² exp(-2gamma t)R_p² Tr(Q^(2p)rho).

One documentary precision was sent to the author: the initial extension's phrase 'Monotone finite-rank/finite-field approximation' must not be read as claiming P_R rho P_R increases in Loewner order. Such state cutoffs are generally not monotone. The spectral-density sum above is already a complete proof; monotone bounded field-OBSERVABLE cutoffs plus positive spectral finite-rank sums are an equivalent valid formulation. The corrected source explicitly states this valid formulation and disclaims state-cutoff Loewner monotonicity. It also now explicitly restricts additional integer waiting-time moments to nonnegative integers. Both clarifications are resolved in the final bound bytes.

## 4. Exact controls and limits

check_coefficients.py builds R_p directly by the graph-norm recurrence and independently builds Stirling/Touchard coefficients by finite-set-partition recurrence. All coefficients and the P recurrence agree through p=16. Exact rational substitutions verify placement of C0, the bandwidth factor2, and the finite moment-integral formula; negative controls detect omission of either factor. These are algebraic coefficient tests, not rotor simulations and not evidence for the domain theorem by finite approximation.

Execution used0.041975 CPU seconds and18,956,288 bytes peak RSS. It used only standard-library exact rational arithmetic under one-thread environment variables, a hard30-second CPU limit, the original campaign deadline and STOP check, and a150 MB memory assertion. No failed run or relaxed threshold occurred.

This check finds no material discrepancy in the corrected polynomial theorem. The two sentence-level qualifications above are incorporated in the final source. The actual low-global-excitation decay proof was reconstructed at its original scope. No uniform finite-spin replacement, extensive-background estimate, independent-excursion decomposition or full microscopic original local-output convergence has been supplied. Those remain distinct load-bearing obligations; the polynomial extension does not silently assume them.
