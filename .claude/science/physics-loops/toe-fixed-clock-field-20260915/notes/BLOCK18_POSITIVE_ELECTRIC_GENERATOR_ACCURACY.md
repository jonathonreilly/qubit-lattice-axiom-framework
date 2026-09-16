# Positive cyclic electric generators and an accuracy tradeoff

Personal derivation, 2026-09-15. PROVISIONAL; personal checks and review complete. No independent
audit. This is a full-class statement for a specified local electric
generator, not a no-go for positive histories, finite spins or the TOE.

## 1. Precisely which positivity is required

On one odd cyclic link N=2S+1, require a translation-invariant Hermitian
electric Hamiltonian H_E in the CLOCK-PHASE basis, with

                exp(-t H_E) entrywise nonnegative for EVERY t>=0. (1)

Subtract its constant-mode energy so that H_E 1=0. This scalar convention
does not alter positivity. Condition(1) holds if and only if every off-diagonal
entry of H_E is nonpositive. Necessity follows by differentiating an
off-diagonal heat-kernel entry at t=0. For sufficiency choose R so that
R I-H_E is entrywise nonnegative, and use
exp(-tH_E)=exp(-Rt) sum_k t^k(R I-H_E)^k/k!.

Translation invariance and Hermiticity then give symmetric nonnegative jump
rates. In the electric Fourier basis n, its complete form is

 lambda(n)=sum_(j=1)^S gamma_j[1-cos(j theta)],
 theta=2pi n/N,                 gamma_j>=0.             (2)

The rate for each signed jump j is gamma_j/2. This derivation characterizes
the entire stated finite-dimensional cone; it is not a search over several
chosen stencils. It is elementary finite Markov-generator mathematics.
The positive cyclic parent uses its nearest-neighbor member.

Calibrate the continuous Fourier symbol at theta=0 to the same supplied
quadratic electric curvature k n^2, k=g^2 w/(2a). Explicitly impose

 sum_j gamma_j j^2=Gamma,
 Gamma=k N^2/(2pi^2)=g^2 w N^2/(4a pi^2).               (3)

The calibration is the curvature of this trigonometric symbol. At very
small N it is not equivalent to fitting its value at the first nonzero
electric level; changing that calibration is outside the comparison.

## 2. Nearest-neighbor jumps maximize the whole calibrated dispersion

The finite geometric series gives, for every real theta and integer j>=1,

 |1-exp(i j theta)|<=j|1-exp(i theta)|,
 1-cos(j theta)<=j^2[1-cos(theta)].                      (4)

Combining(2)-(4) gives the pointwise operator bound

 0<=lambda(n)<=Gamma[1-cos(theta)]=lambda_nn(n).         (5)

If any gamma_j>0 with j>1, inequality is strict for every nonzero cyclic
character n. Equality in the triangle inequality would require all
1,exp(i theta),...,exp(i(j-1)theta) to have the same phase, which requires
theta=0 modulo2pi. This also handles composite N and reducible jump choices.

Thus adding longer positive phase jumps cannot improve the electric
underestimate at fixed curvature. Taylor expansion at each fixed N makes
the local obstruction explicit:

 lambda(theta)=Gamma theta^2/2-M4 theta^4/24+O(M6 theta^6),
 M4=sum_j gamma_j j^4>=Gamma.                           (6)

The quartic coefficient cannot vanish for a nonzero generator. Equality
in M4>=Gamma holds only for nearest-neighbor jumps. No uniform Taylor
remainder is claimed for arbitrary N-dependent distributions of long jumps;
the exact pointwise bound(5) needs no such moment assumption.

With the magnetic and matter terms unchanged, summing(5) on links gives
H_general<=H_nn on the same exact modular physical space. Ordered
eigenvalues satisfy the corresponding min-max inequality. Differences
between consecutive eigenvalues do not inherit that ordering automatically.

On the pure one-plaquette family of Block17, any such calibrated rate family
satisfies, if g->0, N->infinity and gN->ell in(0,infinity),

 limsup E0_general(g,N)<=E0_nn(ell)<1.                  (7)

No limit for the general family is assumed. The nearest-neighbor result
already bounds it from above. In the subsequent large-ell comparison its
ground-energy underestimate is at least pi^2/(8ell^2)+O(ell^-4). This is
the declared positive electric/magnetic energy convention, not an invariant
claim about a particle gap. Block17's Gaussian support and alias tests
provide separate state-level discriminators. No photon exclusion follows.

## 3. A concrete escape: a positive Hamiltonian with signed phase jumps

Drop the all-small-time entrywise requirement but keep Hermiticity,
translation invariance, quadratic calibration and nonnegative energy.
For N>=5 consider

 lambda_imp(theta)=Gamma[(4/3)(1-cos theta)
                              -(1/12)(1-cos2theta)]
                  =Gamma[b+b^2/6], b=1-cos theta>=0.   (8)

It is nonnegative and has the same curvature. Its quartic term cancels:

 lambda_imp/Gamma=theta^2/2-theta^6/180+O(theta^8).      (9)

However its clock-phase H_E has H_(q+2,q)=+Gamma/24, so

 [exp(-tH_E)]_(q+2,q)=-t Gamma/24+O(t^2)<0             (10)

for sufficiently small positive t. The Hamiltonian is valid and positive;
its phase heat kernel does not satisfy(1). In particular a determinant-paired
matter factor cannot by itself remove a negative independent electric step
weight in the parent's chosen history decomposition. This is a failure
of that specific decomposition, not a proof that every auxiliary or
reorganized representation must have negative weights.

It is not merely a negative entry that disappears on imposing a closed
history. Three small-time phase moves +2,-1,-1 return the link to its initial
value and have a negative product: the length-two jump is negative while
both length-one jumps are positive. Keep all other links fixed and choose
the identity final Gauss twist. Diagonal magnetic weights are positive.
Already in pure gauge this is an admissible negative closed history in that
specific decomposition. Summing histories still yields a positive operator
trace; no contradiction with a valid Hamiltonian is involved.

## 4. The improvement survives the one-plaquette spectral test

The finite-ell limit of(8) on the one-plaquette model is the periodic
Schrödinger operator -.5 d^2/dx^2+V_imp,ell(x), where

 V_imp,ell=(ell^2/pi^2) F(2pi x/ell),
 F(theta)=(4/3)(1-cos theta)-(1/12)(1-cos2theta).

Direct differentiation gives

 1-F''(theta)=(2/3)(1-cos theta)^2>=0.

Since F(0)=F'(0)=0, integration twice and 1-cos theta<=theta^2/2 give

 0<=theta^2/2-F(theta)<=theta^6/180,
 0<=2x^2-V_imp,ell(x)<=16pi^4 x^6/(45ell^4).            (11)

These hold for all real theta/x, not merely as a formal series. Also
V_imp>=V_nn>=8x^2/pi^2 on the centered period. The periodized-Gaussian
argument of Block17 applies to(11), giving

              E0_nn(ell)<=E0_imp(ell)<1.               (12)

The leading improvement can be proved without assuming a formal
perturbation series. Let psi_ell be the normalized positive periodic ground
function. For the periodic Lipschitz multiplier f(x)=|x|^r on the centered
period, the ground-state transform gives

 <f psi,H f psi>=E0_imp<f^2>+(1/2)<|f'|^2>.

Since E0_imp<1 and V_imp>=c x^2, c=8/pi^2, its even moments obey

 c M_(2r+2)<=M_(2r)+(r^2/2)M_(2r-2), r>=1,
 M0=1, M2<=1/c.                                       (13)

The multiplier has matching values at the two endpoints; its derivative
need not match there for this quadratic-form identity. Thus all fixed
even moments are bounded uniformly in ell. The r=0 case directly bounds
M2. No artificial seam derivative or unbounded test operator is inserted.

Take a smooth cutoff chi_ell that is one for |x|<=ell/4 and vanishes near
|x|=ell/2, with |chi'|<=C/ell. Its kinetic error is bounded by arbitrarily
high inverse powers of ell using(13). Applying the full-line oscillator
bound to chi psi gives

 1<=E0_imp+[int chi^2(2x^2-V_imp)|psi|^2
                         +(1/2)int|chi'|^2|psi|^2]/||chi psi||^2.

Equation(11) therefore gives 1-E0_imp=O(ell^-4). The cutoff ground vectors
have oscillator Rayleigh quotient tending to1; the full oscillator gap2
forces their normalized vectors to converge, up to phase, to exp(-x^2).
The uniform higher moments ensure convergence of the sixth moment to15/64.
Finally ell^4(2x^2-V_imp)->(16pi^4/45)x^6 pointwise, dominated by the
right side of(11). This gives the lower energy bound with its limiting
coefficient. The matching upper bound follows by inserting a cutoff full
Gaussian as a trial state. Hence

            lim_(ell->infinity) ell^4[1-E0_imp(ell)]
                         =pi^4/12.                    (14)

This is an actual leading spectral-error result for the limiting periodic
operator. In contrast, the positive nearest-neighbor parent has
ell^2[1-E0_nn(ell)]->pi^2/8. The improved positive Hamiltonian escapes the
order-ell^-2 error at the cost of(1). Finite-g magnetic difference errors
are additional; no joint finite-g,N rate is inferred from(14).

## 5. What the wall does and does not require

Within this translation-invariant single-link, all-time nonnegative phase
kernel and fixed-curvature class, the nearest-neighbor electric dispersion
is pointwise optimal. Searching more positive long-jump weights cannot
remove the cosine quartic error. That exact class-wide statement is a useful
stop condition for this particular proposed improvement.

Live escapes include changing the electric calibration or kinetic law,
accepting signed local history weights, using a different basis, adding
auxiliary states with a new effective-generator proof, allowing nonlocal
electric interactions, or requiring positivity only at selected finite
times. None has been ruled out by(5). Even within the original positive
family one may simply increase gN and retain the oscillator limit.

The theorem does not make positivity an axiom, prescribe an axiom update,
or establish a preferred regulator from the framework. It does not imply
that a signed simulation is impossible or that a positive representation
must exist. The physical Hamiltonian and representation assumptions remain
explicit supplied choices.

## 6. Personal verification

Fifteen dense positive-rate fixtures at prime and composite N=5,7,9,15,31
obey the exact all-character envelope. Direct phase matrices and Fourier
symbols agree to2.6e-16. Their heat kernels at three times have nonnegative
entries and unit column sums within roundoff. These examples are checks;
the full-class conclusion comes from(4), not a random search.

All five improved Hamiltonians are positive semidefinite to numerical
precision, while their time1e-5 phase kernel has a negative length-two
entry of about-4.17e-7. The closed +2,-1,-1 history has negative product
about-1.85e-17. Exact symbolic differentiation verifies(9),(11), and Gaussian
integration gives <x^6>=15/64 and the coefficient pi^4/12 in(14).

Two Fourier truncations agree within5.1e-12 on the checked periodic spectra.
At ell=24 the improved scaled error ell^4(1-E0) is about8.03, compared with
the analytic limiting8.1174; the nearest-neighbor scaled error ell^2(1-E0)
is about1.236, compared with pi^2/8=1.2337. These finite comparisons have
not been turned into certified remainder estimates. No scientific check
failed. All verification is personal and awaits independent review.
