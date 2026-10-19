# Supporting mathematical source

Scope of this supporting source: exact constructive identities retain their stated mathematical validity. Any terminal exclusion developed below is preserved as deferred science, pending its required promotion packet; it is not promoted by this extract or used to strengthen the active canonical claim.

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_ZONE_CROSSOVER_CHECK.md`, SHA256 `eddee71d0d1db67e9221c47c7b1e06520d14ecfa6e16ac6089e8cf384a13a00f`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Conditional zone-boundary crossover check

The stated threshold determinant, its two admissible roots, and the upper-source-mode curvature208/27 check. Within the specified infinite half-line crossover operator, the complete number of modes strictly ABOVE its essential spectrum is two, then one, then zero as positive kappa passes the two thresholds. This is a statement about the derived candidate operator; it is not a native uniform-limit or stability theorem. No root files were changed.

## Operator and upper threshold

The host has bulk diagonal -1/2, nearest hopping kappa, next-nearest hopping1/4, and endpoint diagonal+1/2 (defect+1). The extra d state has diagonal-2 and couples to host site1 with -sqrt(2). The other supplied flat dark states at-2 are not upper bound modes and do not change the following analysis if they are decoupled as stated.

For bulk wave e^(ikn), x=cos k gives E=x²+2kappa*x-1. Its maximum is2|kappa|. For positive kappa, at the upper threshold E=2kappa the bulk recurrence has bounded solutions A+B r^n, where r in(-1,0) and r+r^-1=-4kappa-2. The additional linearly growing solution from the double root1 is inadmissible as a bounded threshold solution.

Eliminating d at E=2kappa gives host-site1 self-energy eta=2/(E+2)=1/(kappa+1). The two boundary equations in the (A,B) amplitudes are exactly

[[kappa-3/4, kappa/r+1/(4r²)-1],
 [1/4-eta, 1/(4r)-eta*r]].

I independently simplified the determinant after kappa=-(r+1)²/(4r), obtaining

-(16r^4+92r³+39r²-2r-1)/(16r²(r-1)).

An exact polynomial root count gives exactly two roots in(-1,0). All four roots are approximately -5.28471154861342, -.455268224716236, -.166262228118771, and .156242001448431. Only the middle two are admissible decaying roots here. They correspond to kappa=.162943892684775 and1.045214358255971. There is no denominator singularity inside(-1,0). The roots are simple.

## Complete upper-mode count

A monotonicity argument completes the finite-matrix observation. Let F(kappa)=M(kappa)-2kappa I on host plus d. Its derivative is T+T†-2I on the host and -2 on d, hence negative semidefinite. In fact its quadratic form on any nonzero square-summable vector is negative. The number of strictly positive discrete eigenvalues of F therefore cannot increase with kappa.

At kappa0, the odd chain supplies9/16 and the even-chain/d system supplies its upper root(-38+16sqrt10)/31>0, giving exactly two upper modes. The other even-system root is below the host continuum. To show that none remain indefinitely, one can bound F explicitly rather than relying on a finite cutoff. The zero-kappa host operator obeys Hhost(0)<=P0, since its bulk next-nearest term is bounded above by+1/2. The nearest-neighbor form is

<f,(2I-T-T†)f>=|f0|²+sum_(n>=0)|f_(n+1)-f_n|².

Eliminating the strictly negative d block of F adds |f1|²/(1+kappa). Using |f1|²<=2|f0|²+2|f1-f0|² gives the sufficient upper bound

<F> <= [1-kappa+2/(1+kappa)]|f0|²
       +[-kappa+2/(1+kappa)]|f1-f0|²
       -kappa sum_(n>=1)|f_(n+1)-f_n|².

For kappa>sqrt3 all coefficients are negative, so there are no strictly positive eigenvalues. Every disappearance into the upper continuum must admit a bounded threshold solution of the finite-range recurrence, hence occur at one of the two determinant zeros. Each simple zero has a one-dimensional boundary kernel and supports one threshold crossing. Since exactly two modes must disappear and there are exactly these two possibilities, the count is

2 for0<=kappa<.162943892684775,
1 for.162943892684775<kappa<1.045214358255971,
0 for kappa>1.045214358255971.

At the threshold itself the disappearing solution has a nondecaying constant component and is not an ordinary normalizable bound state; the count of STRICT upper modes has already lost that state. The two threshold columns do not vanish simultaneously in a way that leaves a pure decaying embedded-edge eigenvector. Negative kappa is unitarily equivalent by alternating host signs (and a compensating d sign), so the count depends on |kappa|.

## Upper source-mode curvature

At zero kappa the normalized odd-chain eigenvector is sqrt(15/16)(1/4)^n. Nearest hopping couples it into the even host with forcing f_n=f0 r^n, r=1/4 and f0=(5/4)sqrt(15/16). The even-host resolvent at E=9/16 includes d self-energy2/(E+2)=32/41 at its boundary. Solving with y_n=(A+Bn)r^n gives B=(16/15)f0 and A=(656/135)f0. Therefore

<f,y>=f0²[(656/135)/(1-r²)+(16/15)r²/(1-r²)²]=208/27.

The eigenvalue is isolated from the other upper level at kappa0 and is even under kappa sign reversal. Hence its analytic expansion is9/16+(208/27)kappa²+O(kappa^4). This coefficient is not a bare hopping or an inference from finite differences; it includes the side-state boundary resolvent. The finite-N curvature quoted by root is consistent with it.

## Limits and remaining assumptions

The infinite half-line operator has been analyzed mathematically here. The source script uses a finite host N400, whose top finite eigenvalues need not represent bound modes after the threshold: ordinary continuum approximants remain discrete. Source residue and localization are helpful diagnostics but are not substitutes for the recurrence/count argument above.

The physical double scaling q=pi-lambda*kappa requires a compatible sequence of allowed momenta as L grows. At fixed L the nonzero q offset cannot vary continuously through these values. In particular a formal finite-volume Taylor coefficient or an exact all-length symmetry count does not establish a uniform Schrieffer-Wolff remainder in the simultaneous L→infinity, lambda→0 limit. Near either disappearance threshold, localization length diverges and finite-size convergence is nonuniform even within the candidate operator.

The stated O(lambda^4) remainder in Hgap/Jz=8+lambda² M(kappa)+... must remain formal unless its coefficient structure and a uniform bound are derived. Higher native bands, state/source dressing and additional effective terms can matter before promoting these upper levels to physical native modes. No bulk scalar, exact native lifetime, cosmological bridge, or empirical test follows from this conditional crossover calculation.
