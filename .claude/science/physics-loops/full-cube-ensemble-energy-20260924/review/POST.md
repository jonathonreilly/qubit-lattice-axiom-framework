# Released-source POST: full original cube ensemble energy and rare density

2026-09-24. This is a separate comparison after the immutable independent PRE was disclosed. It changes no PRE member, author source, publication, audit record or axiom. The model and reasoning effort were retained and no work was delegated. Imported scientific results remain conditional and unaudited. This report applies the scoped premise, proof and evidence checks in the physics-claim-reviewer skill; it is not an audit verdict.

## 1. Conclusion and provenance

The released root candidate agrees with the sealed PRE's ordinary full-ensemble mean and scaled second-moment/variance limits. I found no material mathematical defect within the stated fixed-cube, fixed-positive-parameter, canonical-input and original-instrument premises. The PRE's rate-free compact-age convergence plus age tightness is sufficient; the conclusion does not need the root's stronger quantitative convergence of the low input.

The additional first-high density limit and frozen-source Lyapunov balance in root section 8 are supported by the separate derivation in sections 4–5 below. Those are **POST implications reconstructed after release**, not claims that they appeared in my blind PRE. Their proof uses the PRE's full vector-profile estimates, not merely convergence of two scalar moments. No inverse Lyapunov operator, finite-spin decay gap, physical-time derivative limit, full-ensemble Fisher bound or conserving-apparatus construction is needed or established.

The independent PRE seal is SHA256 `ab052a8061d0103417c6ce431d132530951df70eea588e709c31f0f4bbc7995d`; its 34 members were reverified before and after this comparison. PRE.md remains SHA256 `3996a4a5d128545470b8636d88aef2d6b29e424eff8672bd3be125dc372258df`.

The released candidate is `FULL_CUBE_ENERGY_ANOMALY_PERSONAL_DERIVATION.md`, SHA256 `42570c118387059b66ad7a76c4b57bfdc7acdcb8c0c58aa2a5f0c622bd9cc723`, bound by AUTHOR_SEAL.json SHA256 `b1911b15a9271cedd3f75f5291ce26b145af79ec3d0b81f33ac5daca1e414efd`. The actual control-seal filename is CONTROL_SEAL.json, SHA256 `a8e9e3a9df291663235b06bcb5bff26b61b902ca37f6be6058de035aeb043fe2`; its runner is SHA256 `7354476b7b253e966f66bfe0b3d6cca32f3949b18c4208470de27951e33ad7c7`. Ten released files, including the full results, stdout, stderr, execution record, source pins and scope statement, were frozen under POST_sources. All released files and both author seals were read completely. A combined display of the long result was initially truncated; the result was then read separately in full. That truncated display is not relied upon as completed inspection.

The seven scientific note revisions and the explicitly supplied recent-birth PRE/seal match the PRE's exact source pins. The root manifest also lists its prior recent-birth personal derivation and that checker's POST/seal. These three additional declared dependencies were not imported or re-reviewed here. The explicitly supplied prior lower bound remains attributed to the recent-birth PRE, not counted as another independent discovery. The metadata-only changes reported for two publication working trees are outside this comparison; the previously authorized committed source bytes remain the dependencies.

## 2. Exact target and agreement with PRE

Fix delta,K,kappa>0, integer S tending to infinity with epsilon²S(S+1)=delta/K, lambda=0 compensation, the canonical Hermitian N=4 zero-field preparation, and the complete original resolved or coherent formation instrument. All limits below are uniform on any fixed `[t0,T]` with `t0>0`. No limit uniform down to t=0, out to infinite physical time, or as kappa tends to zero is asserted.

Let rho_e(t) be the trace-one full original ensemble and H_e its physical block-diagonal Hermitian Hamiltonian. Write

    chi4,e(s) = V4,e(s) U4,e Omega,
    x_i,e(s,t) = V6,e(t-s) sqrt(kappa) epsilon^-1 j_i chi4,e(s).

Then the exact N=6 block is the sum over original marks of the birth-time integrals of `|x_i,e><x_i,e|`. The N=4 block is the unnormalized no-first-birth pure block. The terminal N=8 block is included in the ensemble and has H8=0 exactly. There is no branch normalization or replacement of the continuously occurring first birth by a single prescribed marked amplitude.

Set

    u4(t) = exp(-24 kappa t) exp(-i t h4) Omega,
    L = -i delta Pi1(FF* - F*F)Pi1 - kappa Gamma1/2,
    r_i(t) = R_i u4(t),
    I(t) = sum_i integral_0^infinity ||exp(tau L) r_i(t)||² d tau.

The fast space is the complete physical first-high N=6 rotor matter/field space. The root's `Zfast` is the PRE's `L`. E_rot(t) in the root candidate is the PRE's E_low(t): the full common low-process mean, including the original N=4 and continuously born N=6 contributions. The shared conclusions are

    Tr(H_e rho_e(t)) -> E_rot(t) + kappa delta I(t),
    epsilon^4 Tr(H_e² rho_e(t)) -> kappa delta² I(t),
    epsilon^4 Var_(rho_e(t))(H_e) -> kappa delta² I(t),

with finite continuous I and `I(t) >= 36 exp(-48 kappa t)/kappa > 0`. The mean is bounded on each such interval, so subtracting its squared value after multiplication by epsilon^4 does not change the second-moment limit. The terminal sector's effect on a centered square has not been discarded: the variance is formed from the exact full first and second moments.

The root includes sqrt(kappa)/epsilon in its source coordinate z. My PRE used the raw j source and retained the prefactor kappa/epsilon² outside the density integral. After this conversion, the source orders and all energy factors agree. In particular the root's `O(epsilon³)` first-high jump-source remainder is the PRE's `O(epsilon^4)` raw-mark remainder.

The resolved and coherent instruments must retain their own sum-inside-mark definitions of R_i. Equality of the total loss or of `sum_i R_i*R_i=72 I` does not equate their injected densities or their total I(t). The full fixed-time ensemble result also does not establish a fixed-time variance limit for a separately normalized N=6 input prepared at time zero. A fixed-age ordinary-energy conclusion for a prepared N=6 state cannot remove the contribution from the continuously replenished recent-birth layer here.

## 3. Load-bearing proof comparison

### 3.1 Grading, actual pre-birth input and the stronger root estimates

The root's exact Riesz/intertwiner use is compatible with the PRE. The physical V_N is a contraction, and exact invariant block semigroups have a common forward-time bound after the uniformly bounded similarity. Thus initial high-coordinate estimates propagate for every birth time `0<=s<=T` without a weighted estimate on a long-propagated high component.

For the stronger root bound `E4,r U4 P4=O(epsilon^(r+2))`, the loss-parameter argument has the required hypotheses: at zero loss the product vanishes; the loss insertion has degree two and preserves bare grade; reaching bare row r from grade zero requires at least r degree-one hops. The grade-r coordinate therefore starts at degree r+2. Its full Riesz range is a uniformly bounded graph over that coordinate. The analytic resolvent and polar series have a common ordinary-norm radius, so this coefficient count gives an operator remainder bound, not only a matrix-element identity. Likewise `Pi_l J6^-1 j_i J4 Pi_r` requires at least `abs(l-r+1)` hops because j lowers grade by exactly one. Inverse series retain the same grading and parity.

The root's stronger O(epsilon²) low-coordinate convergence can be obtained in the stated domain. On the fixed graph,

    ||(spin shift - rotor shift) v|| <= C epsilon² ||w v||,
    w = 1 + sum_e E_e²,

including boundary and zero extension. The spin-box complement is also bounded by C epsilon²w on vectors. The D/C coefficient equals a fixed multiple of epsilon²D on the spin box; any anticommutator appearing in the bounded low remainder is consequently controlled by epsilon²w. After isolating the common unbounded free KD, variation of constants can be applied to the limiting weighted orbit. It is not a global norm convergence assertion for D. The initial coordinate error O(epsilon³) is smaller than the proposed O(epsilon²) accumulated error. For each fixed weight power, weighted contour and interaction-picture estimates supply the needed domain bounds; one common radius for all powers is not required.

These stronger refinements have a consistent derivation, but I do not make them additional blind-PRE claims. For the theorem and trace-norm conclusion I use the sufficient PRE estimates: uniform strong convergence without an assigned rate, a common w³ bound, bare grade-one pre-birth error O(epsilon³), and the remaining error O(epsilon^4).

### 3.2 Birth-source cancellation and second band

The cubic canonical second-high coefficient is

    j_i F³/6 - F j_i F²/2 + F² j_i F/2.

Its operator cancellation was independently reconstructed and checked in the PRE. Outward hops at different A sites commute, including the hard-core zero cases; `F_a²=0`; and `j_i P4=0`. Opposite shifts on the same edge are not interchanged. The cancellation therefore applies to actual spin weights as well as rotor shifts. Parity rules out degree four. Loss or compensation cannot change this leading cubic coefficient since three grade-changing hops are already needed.

The root uses the stronger all-grade initial bound and transformed-mark bound to improve the exact second-high L-source to O(epsilon^4). The degree minimization in its equation (12) is correct: over r>=1 the exponents are at least 2,3,4 for output grades 0,1,2 respectively. The low-column replacement J4-U4 also respects these orders; its bare grade-zero term begins at degree four, while positive bare grade k begins at k+2. No grading term of the stated lower orders has been omitted.

The PRE only needs the weaker second-high L-source O(epsilon³). Its Hermitian coordinate has that order, and the integrated mean and epsilon^4-scaled second moment are then O(epsilon²). The stronger second-high source exponent thus does not carry the shared conclusion. An ungraded O(epsilon²) L-source remainder in that band would be insufficient, which is why the cubic/source analysis cannot be replaced by a generic projector norm estimate.

### 3.3 Evolved source, genuine growing-time comparison and age integration

Both proofs correctly control the evolving N=4 field instead of replacing it by Omega. In the five-cycle Fourier representation the common w³ bound gives H^6 and hence C² control of each r_i(s). Explicit Cauchy–Schwarz reduces this to convergence of the lattice sum `(1+|n|²)^-4` in five dimensions. The parent slow-block/phase estimates therefore extend to this uniformly C² family by the derivative product rule, giving

    ||exp(tau L) r|| <= C (1+tau)^(-5/4),
    ||w exp(tau L) r|| <= C (1+tau)^(-1/4).

This is not a uniform decay assertion for every L² input. It is also not an independent re-proof here of the parent's full fiber classification or global singular-value certificate; those remain pinned conditional imports.

The exact finite-spin fast block, after removing its scalar carrier, has a common forward-time semigroup bound and generator difference at most C epsilon²w on the relevant vectors. Duhamel therefore bounds its difference from the rotor evolution by `C epsilon²(1+tau)^(3/4)`. Using this bound through tau=epsilon^-1 is justified by that explicit estimate, not by inserting a growing time into a compact-time convergence theorem.

At this age the leading fast profile has norm O(epsilon^(5/4)). Exact contraction through the intertwiner carries that bound to every older age; it makes no finite-spin spectral-gap assertion. In the root's L-source normalization, the propagated first-high amplitude is O(epsilon^(9/4)), so integrating old physical birth times and multiplying by epsilon^-4 gives O(epsilon^(1/2)). The Hermitian/Riesz difference adds only a uniform O(epsilon³) L-source amplitude and does not alter the leading integral.

The root's explicit recent-age source-freezing error `epsilon² tau` is legitimate because u4 has a bounded strong derivative on bounded intervals. Its square integrates to O(epsilon) through tau=epsilon^-1. The other two squared errors are O(epsilon^(3/2)) and O(epsilon³), as stated. Nevertheless the simpler sufficient PRE proof freezes the source only on each fixed compact age interval, then uses a uniform tail estimate. It establishes the limit without needing the stronger low-input rate or the explicit recent-age freezing rate.

### 3.4 Hermitian energy coordinates and low moments

Both arguments calculate moments in the orthogonal Hermitian clusters. They do not discard cross terms between nonorthogonal Riesz projectors. The first-high physical Hamiltonian is `delta epsilon^-4[I+O(epsilon²)]`; the all-age squared-profile bound makes the coordinate-replacement cross term negligible after energy scaling.

For the low L-source, the leading uniformly weighted vector has energy-vector norm O(1). Its ordinary error is O(epsilon²), while the low Hamiltonian has norm O(epsilon^-2). The expectation cross term and the error's self-expectation are each O(epsilon²), and the entire low energy-vector norm stays O(1). Strong convergence with common D-weighted bounds gives the low electric expectation limit. This specifically avoids using ordinary trace convergence alone to pass an unbounded energy expectation.

The N=4 first and aggregate higher Hermitian high amplitudes are O(epsilon³) and O(epsilon^4); their second moment is at most O(epsilon^-2) and vanishes after epsilon^4 scaling. N=8 contributes zero raw moments. These estimates suffice without importing a stronger N=4 fluctuation coefficient or solving a normalized N=6-start variance problem.

## 4. Separate POST reconstruction of the trace-norm extension

Let K be the fixed bare-grade-one physical rotor space and let U6,e^H be the complete Hermitian canonical cluster unitary. For `0<=tau<=t/epsilon²`, define

    f_i,e,t(tau) = [exp(i delta tau/epsilon²)/(sqrt(kappa) epsilon)]
                   Pi1 (U6,e^H)* x_i,e(t-epsilon² tau,t),

and set it to zero for larger tau. The finite-spin coordinate is extended by zero in K. The exponential is a scalar of modulus one; its precise phase has no effect on a rank-one density. Let

    f_i,t(tau) = exp(tau L) R_i u4(t),  tau>=0.

The PRE proof gives, uniformly for `t in [t0,T]`:

1. On every fixed `0<=tau<=L0`, f_i,e,t tends strongly and uniformly to f_i,t. This uses compact-age convergence of the exact block, the strong uniform low-source limit, and continuity of u4. It requires no prescribed rate of the low-source convergence.
2. The first-high profile has the uniform tail bound

       integral_L0^infinity ||f_i,e,t(tau)||² d tau
          <= C(1+L0)^(-3/2) + C_T epsilon^(1/2) + o(1).

   Here the additional coordinate/source error divided by epsilon is O(epsilon²); its square integrates over at most T/epsilon² to O(epsilon²). The main-profile tail is the PRE's young/old split. The limiting profile has the same integrable algebraic tail without the epsilon term.

Using `||f-g||² <= 2||f||²+2||g||²` in the tails and compact convergence on `[0,L0]` proves

    sum_i ||f_i,e,t-f_i,t||²_(L²([0,infinity);K)) -> 0.       (POST-1)

This statement concerns the vectors, not just their squared norms. The finitely many original marks can be collected in one direct-sum L² space.

For Hilbert vectors a,b,

    || |a><a| - |b><b| ||_1 <= (||a||+||b||) ||a-b||,

by writing the difference as `|a-b><a|+|b><a-b|`. Integrate this estimate, then apply Cauchy–Schwarz in age and in the finite mark index. Equation (POST-1) and the common L² bounds give convergence in trace norm of the integrated densities.

The change of variable `ds=epsilon² d tau` and source amplitude `sqrt(kappa) epsilon` give exactly

    epsilon^-4 rho6,high^coord(t)
        = kappa sum_i integral_0^infinity |f_i,e,t(tau)><f_i,e,t(tau)| d tau
        -> Sigma(t),

    Sigma(t) = kappa sum_i integral_0^infinity
                         |f_i,t(tau)><f_i,t(tau)| d tau.   (POST-2)

Thus root equation (23) holds under the PRE premises. Sigma is a positive trace-class operator and `Tr Sigma=kappa I(t)`. No low/high off-diagonal block limit is asserted. Coherent interference inside an original mark is retained before each rank-one operator is formed.

Every bounded observable on this common matter/field fiber has the corresponding leading rare-population coefficient. That conclusion does not by itself pass arbitrary unbounded observables. The energy conclusions additionally use the separately proved scaled first-high Hamiltonian limit and the low/other-band estimates from section 3.4. Sigma is an unnormalized coefficient of a vanishing sector probability, not a replacement normalized state for the full ensemble.

## 5. Separate POST reconstruction of the frozen-source balance

Fix physical t and set `A(t)=sum_i |r_i(t)><r_i(t)|`. It is positive, finite rank and trace class. The operator L is bounded on K, because the rotor shifts, finite matter matrices and loss are bounded. Define

    Phi(tau)=exp(tau L) A(t) exp(tau L*).

The source-family estimate gives `||Phi(tau)||_1=sum_i ||f_i,t(tau)||² <= C(1+tau)^(-5/2)`. Consequently the integral defining Sigma is a convergent trace-class Bochner integral. Boundedness of L gives the trace-norm derivative

    Phi'(tau)=L Phi(tau)+Phi(tau)L*,
    ||Phi'(tau)||_1 <= 2||L|| ||Phi(tau)||_1.

Integrating first over a finite age interval and then taking its endpoint to infinity is justified in trace norm. The upper endpoint vanishes. Therefore

    L Sigma(t)+Sigma(t)L* = -kappa A(t).                    (POST-3)

This proves root equation (24). No existence of a bounded inverse for the infinite-dimensional Lyapunov map is assumed; no uniqueness claim for arbitrary sources is made.

Trace cyclicity is legitimate for a bounded operator times a trace-class operator. Since `L+L*=-kappa Gamma1` and `Gamma1=2 Pbright`,

    -kappa Tr(Gamma1 Sigma) = -kappa Tr A(t),
    Tr A(t) = <u4(t),sum_i R_i*R_i u4(t)> = 72 exp(-48 kappa t).

Cancel the fixed positive kappa to obtain

    Tr(Gamma1 Sigma(t)) = 72 exp(-48 kappa t),
    Tr(Pbright Sigma(t)) = 36 exp(-48 kappa t).              (POST-4)

The positive dark contribution gives `Tr Sigma>=36 exp(-48 kappa t)`, equivalent to the supplied PRE lower bound on I. Equations (POST-3)–(POST-4) preserve all source factors and signs. The ordinary mean excess is delta Tr Sigma; the scaled variance coefficient is delta² Tr Sigma.

These are identities in the frozen-source age problem. They do not exchange an epsilon limit with differentiation in physical t. They do not identify physical bath energy, work, heat, initial apparatus coherence or a Hamiltonian-selection principle. No full-output QFI conclusion follows from the mixed-state variance.

## 6. Author controls, independent checks and their limits

The root runner was read in full but was neither imported nor executed here. Its source-algebra check explicitly imports the previous root helper `preparation-uniform-personal/mixed_preparation_controls.py`, hash `8f4320e1cb333098bb3a609b0a95366380ffc7f1c693cffb8342d757fbc7a09a`. Its current bytes match that pin. I did not re-review its body in this POST. These remain author controls; their helper reuse is not independent evidence. My PRE's separately written physical-word/contour arithmetic continues to supply the distinct primitive source check.

The complete author output contains 1,260 edge/mark/input checks across the rotor and S=2,3,7,21,100, with moving boundary words for finite S. The altered middle coefficient is nonzero in 1,239 cases. Both rotor residuals are zero in the implemented integer-coefficient arithmetic; the largest reported squared finite-spin identity residual is `6.310887241768095e-30`. These finite samples support the displayed algebra but do not prove a uniform analytic remainder, the smooth-source tail or the large-S theorem.

The other author control is explicitly a separate ten-state GKLS cascade. The source code corresponds to the stated model: a rotating initial doublet, a born low doublet, four fast dark/bright states, and a terminal doublet. One coherent first jump maps the initial doublet to low amplitude sqrt(kappa b)I and high amplitude sqrt(kappa) epsilon R. Its initial loss is kappa(b+epsilon²r). The bright second jump has rate 2kappa/epsilon². Vectorization is column-major, so its Liouville and source Kronecker products have the correct orientations. The scalar high Hamiltonian cancels from the density evolution but is retained in the physical H and H² moments.

Although the coherent first jump creates low/high off-diagonal density blocks, the block-diagonal Hamiltonian and losses leave the diagonal equations closed. Those off-diagonal blocks do not enter these energy moments or the terminal probability. Thus solving only the displayed diagonal blocks is valid for this toy. It does not establish a cube density approximation. In particular the toy has a strict fast gap (reported maximum real eigenvalue -0.06490027702708749), whereas the cube argument needs its five-dimensional algebraic tail and the finite-spin age split.

All 15 toy rows and all three complex covariance matrices were read. At epsilon=.01 the reported errors are:

| t | absolute mean error | absolute scaled-variance error | scaled high-density trace distance |
|---|---:|---:|---:|
| .4 | .00172988786 | .00192285277 | .00311706135 |
| 1.1 | .000789026655 | .000869717371 | .000937433988 |
| 2.3 | .000323950834 | .000350992454 | .00141779806 |

The scope statement's t=1.1 numeric prose has the correct rounding. The reported covariance distances obtained by incorrectly freezing the unevolved source are 1.7870471, 3.4752332 and 1.5584910; they are a toy sensitivity control, not new cube data. The smallest reported diagonal-block eigenvalue is -6.903658457278705e-14, correctly treated as floating-point diagnostic rather than an interval positivity result.

The author execution record reports exit 0 and 1.0780968328472227 seconds. Its script hash matches the frozen runner; stdout is byte-identical to the complete result, and stderr is empty. This is inspection of a supplied execution, not my independent reproduction of its source-algebra or cascade run.

The new `post_evidence_check.py` imports no author code and performs two narrow checks:

* It verifies PRE preservation, all released and live byte identities, both author seals, source-pin overlap, stdout/result equality, execution/source correspondence, every reported row's target factors and numeric prose. By separately transcribing the four-state toy matrices and evaluating its initial two-state unitary in closed form, it recomputes the reported covariance's Lyapunov residuals: 2.342e-15, 2.247e-15 and 1.209e-15. This is a literal-array residual check of supplied numerical answers, not a rerun of the author propagation or a new cube experiment.
* It checks a different two-state dark/bright balance in exact Gaussian-rational arithmetic. For `L=[[0,-ig],[-ig,-kappa]]`, source `kappa a |dark><dark|`, g,kappa,a>0, the covariance is

      Sigma = [[a/2+kappa²a/(2g²), i kappa a/(2g)],
               [-i kappa a/(2g), a/2]].

  Its determinant is a²/4, its bright trace is a/2, and its Gamma trace is a. The characteristic polynomial of L is lambda²+kappa lambda+g², so the finite two-state evolution decays and this solution equals its convergent covariance integral. Three rational parameter choices have exactly zero Lyapunov residual. Omitting the source factor kappa or reversing the current's imaginary sign gives a nonzero residual. At g=0 the dark source does not decay; its integral diverges and the dark diagonal Lyapunov equation is impossible. This last control shows why bounded dissipativity alone cannot replace the actual integrability premise. It is not a counterexample under the cube premises.

The new check had one successful execution, exit 0, with full stdout and empty stderr preserved. The result and all its new source/log bytes were read. No expensive primary run, parent control, complete finite-spin cube propagation or author builder was rerun. No failed scientific route or altered output is being concealed.

## 7. Required scope and disposition

No repair to the released mathematical conclusion is required on the checked conditional premises. The following qualifications carry the result and must remain visible in any synthesis:

* The ordinary excess and divergent variance belong to the complete continuously injected N=4-start original ensemble at fixed positive time. The normalized N=6-start pointwise variance problem remains distinct.
* Uniform source grading, the evolved input's weighted domain, the smooth rotor estimates and the all-age finite-spin comparison are indispensable. Compact-age convergence or total state-norm convergence alone would not establish these energy limits.
* The rare-density/Lyapunov extension is newly reconstructed in POST. It is not retroactively included in the blind PRE's provenance, and its bright balance is not an apparatus-energy or QFI balance.
* Parent theorem imports remain conditional/unaudited; source controls are finite checks; the root's reused helper and strict-gap cascade remain author evidence. There is no independent numerical reproduction of the full cube limit here.

The PRE's rate-free proof is the sufficient route I endorse for the shared theorem and for (POST-1)–(POST-4). All new files are separate from the immutable PRE packet. POST_SOURCE_PINS.json and POST_SEAL.json bind the source/evidence identities and these exact scope limits.
