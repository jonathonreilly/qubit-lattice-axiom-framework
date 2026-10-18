# Focused local-dynamics remainder check

Disposition: PASS conditional on the supplied exact dressed decomposition and interaction-norm hypotheses. The claimed exponent additionally requires bounded operator norm of the observable. No repository edits or formal audit.

Assume H'=B+R with B=2N+D_m, [N,D_m]=0, fixed finite m, and a volume-independent finite-range/exponentially weighted interaction norm of D_m bounded by C_m lambda. Assume R=sum_Z R_Z has an exponentially local interaction norm bounded by C_m lambda^(m+1). The norm must at least control sup_y sum_(Z containing y)||R_Z||; the usual weighted norms controlling LR propagation are sufficient. The underlying graph has three-dimensional polynomial volume growth.

## Remove the fast commuting evolution without a fast cone

The nearest-z projectors in N commute. Terms not meeting the original support X commute with O and with every term that does meet it. Therefore exp(it2N) O exp(-it2N) is supported on X plus its immediate longitudinal neighbors, uniformly for all t. Its norm equals ||O|| and the enlarged support has cardinality at most3|X|. There is no iterative fast-time growth of that support.

Since [N,D_m]=0,

    tau_B(s)O=tau_D_m(s)(tau_2N(s)O).

Thus a Lieb-Robinson bound for D_m, whose velocity is O(lambda), applies to an observable of uniformly bounded enlarged support. The exact commutation hypothesis is essential here.

## Linear support factor and polynomial cone

Let X+ be that enlarged support. A standard pair-sum LR estimate and the trivial commutator bound together give, after absorbing fixed constants,

    ||[R_Z,tau_B(s)O]||
      <= C ||O|| ||R_Z||
         min(1, sum_(x in X+,y in Z) exp[-mu*d(x,y)+v_m*lambda*|s|]).

For nonnegative a_j, min(1,sum a_j)<=sum min(1,a_j). Apply this BEFORE summing supports. Then

    sum_Z ||[R_Z,tau_B(s)O]||
      <= C_m ||O|| lambda^(m+1)
         sum_(x in X+, y) min(1, exp[-mu*d(x,y)+v_m*lambda*|s|]).

The interaction sum at each fixed y is bounded by the local norm of R. On a three-dimensional lattice, the remaining y sum is at most C_m(1+lambda*|s|)^3: inside the cone it is a ball volume; outside the cone its exponentially weighted shells have the same polynomial bound. Fixed LR prefactors only shift the radius by a constant. Consequently

    sum_Z ||[R_Z,tau_B(s)O]||
      <= C_m ||O|| |X| lambda^(m+1)(1+lambda*|s|)^3.

There is only one sum over X. No second |X| factor is needed, and retaining the min bound prevents the spurious exp(C lambda t) growth. Exponential locality of R also makes the interaction sums well-defined in the infinite-volume limit.

## Duhamel estimate

The exact Duhamel formula writes the difference of evolutions as an integral of the above commutator conjugated by a unitary automorphism. Its norm is therefore bounded by

    ||tau_H'(t)O-tau_B(t)O||
      <= C_m ||O|| |X| lambda^(m+1)
         |t| (1+lambda*|t|)^3.

The same argument applies to negative times with |t|. Constants depend on fixed m, interaction ranges/weighted norms, and lattice geometry, not system volume or the shape/diameter of X. It does not assume that t is small compared withlambda^-1.

## Proposed scaling and normalization qualification

For m=20, |t|=O(lambda^-4), |X|=O(lambda^-2/3), and ||O||=O(1), the exponent is

    21-4-9-2/3=22/3,

so the error is O(lambda^(22/3))=o(lambda^6). This arithmetic is correct.

However, “normalized observable” must mean a uniform OPERATOR-NORM bound for that exponent. Variance normalization or division of a local sum by sqrt(|X|) need not give ||O||=O(1). A sum of commuting bounded terms divided by sqrt(|X|) can have norm O(sqrt(|X|))=O(lambda^-1/3); the displayed bound would then be O(lambda^7), still o(lambda^6), but not the asserted22/3 power. Retain the explicit ||O|| factor until the actual observable is specified.

## Scope and source

This checks a dynamical consequence of an already established exact finite-order dressed decomposition. It does not itself prove that decomposition for commuting-bond N or import an onsite theorem unchanged. The ADHH paper [A Rigorous Theory of Many-Body Prethermalization for Periodically Driven and Closed Quantum Systems](https://arxiv.org/abs/1509.05386) provides relevant background, but the argument above is the explicit local Duhamel/LR proof under the supplied hypotheses, not a claim that its onsite theorem directly covers this bond setting.

The reference evolution retains ALL of D_m. Replacing it by D_4 or a preferred scalar block would introduce additional errors from D5 through D20 not bounded here. The estimate also does not supply state selection, source identification, a spectral pole, or control of an infinite-time Fourier transform. If the exact dressing maps an original local observable into a quasi-local one, its tails must be handled separately or summed with the same norm estimate; the finite-support assumption cannot silently be retained after dressing.
