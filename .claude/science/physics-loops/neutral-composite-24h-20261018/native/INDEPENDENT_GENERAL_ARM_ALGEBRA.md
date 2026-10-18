# General fixed-range arm: independent algebra/domain check

Checked 2026-10-18. Scope: steps 1–3 of `/private/tmp/neutral_general_band_strip_root.md`; no certification of subsequent transfer/local-source steps or a microscopic pole. The algebra works, with the explicit qualifications and signs below.

## 1. Global extension and inverse

For a polynomial correction of fixed degree with coefficients O(lambda), choose a fixed cutoff equal to one on a neighborhood of [-2,2]. Then g_lambda is compactly supported and O(lambda) in every fixed C^k norm. For sufficiently small lambda, |g'|<1, so ptilde'=-2+g' lies in (-3,-1) and ptilde is a global decreasing diffeomorphism. With v(n)=f(n+1)+a,

    A_n=ptilde^-1(x-v_n)

is real, grows linearly with n, and satisfies f/3 <= A_(n+1)-A_n <= f. In particular ||[A,T]||<=2f. Since g(T) equals the polynomial correction on the spectrum of T, the equality H0-x=ptilde(T)-ptilde(A) is exact on D(A). The assumptions x-a=O(lambda) and small fixed c ensure |A_n| is bounded strictly below 2 on the first M=floor(c/f) sites. No global ellipticity at arbitrarily large n is asserted or needed.

## 2. Fourier-Duhamel identity

Using a consistent inverse-Fourier normalization,

    exp(itT)-exp(itA)
      = i integral_0^t exp(i(t-s)T) L exp(isA) ds,
    L=T-A.

Moving L to the right gives exactly the stated B L plus an error whose integrand contains [L,exp(isA)]. This commutator has norm <=|s| ||[T,A]||. Thus ||B||<=integral |g_hat(t)| |t| dt=O(lambda), while ||E||<=const f integral |g_hat(t)| |t|^2 dt=O(lambda f). Negative t is handled with oriented integrals and the same absolute bounds.

Likewise [L,T]=-[A,T] and [L,A]=[T,A] are bounded O(f). Duhamel commutator estimates inside the B integral show [L,B]=O(lambda f). The same argument shows [A,B]=O(lambda f), which is useful for domains.

Let B_s=(B+B dagger)/2 and B_a=(B-B dagger)/2. Since g(T)-g(A) is Hermitian, averaging the identity with its adjoint gives

    g(T)-g(A)
      = (B_s L+L B_s)/2 + [B_a,L]/2 + (E+E dagger)/2.

The second term is bounded O(lambda f). There is no discarded unbounded B_a L term. This is the precise reason the symmetrization is valid.

## 3. Congruence, signs, and error size

C=2I-B_s is positive with C=2I+O(lambda). Its commutator with L is O(lambda f). Also

    [C,[C,L]]=[C-2I,[C,L]]=O(lambda^2 f).

The double-commutator square-root identity gives

    (CL+LC)/2 - sqrt(C)Lsqrt(C)
      = (1/2)[sqrt(C),[sqrt(C),L]].

Bounded functional calculus with C uniformly separated from zero bounds the right side by a constant times ||[C,[C,L]]||, hence O(lambda^2 f). One can also obtain a sufficient O(lambda f) bound directly from the first commutator. The earlier E' error dominates, so

    H0-x = -sqrt(C)Lsqrt(C)+R,
    ||R||=O(lambda f).

For the physical lower-half-plane z=x-i eta,

    (z-H0)^-1 = C^-1/2
      [L-i eta C^-1-C^-1/2 R C^-1/2]^-1 C^-1/2.

Thus the stated base inverse is (L-i eta/2)^-1, whose imaginary quadratic form is positive, consistent with the physical lower-half-plane resolvent. Relative to that base, the bounded perturbation is

    -i eta(C^-1-I/2)-C^-1/2 R C^-1/2.

Its norm is O(lambda eta)+O(lambda f)=O(lambda eta), using eta/f>=c0>0. Since the base inverse norm is <=2/eta, the global Neumann series converges for small lambda, uniformly in f. No lambda<<eta or lambda<<f condition is needed. Constants depend on the fixed positive strip bounds for eta/f.

A global Neumann estimate alone does NOT yet give bounded endpoint entries: its crude error is O(lambda/eta). The later localized-source estimates must still be supplied to improve this to O(lambda). The root's steps 4–5 are correctly tasked with that issue.

## Domains and finite-volume passage

T is bounded and A is a real diagonal operator, so L is self-adjoint on D(A). The Fourier construction gives bounded [A,B], and hence C and C^-1/2 preserve D(A); bounded commutator functional calculus gives the same for sqrt(C). Consequently the congruence identities hold on D(A), not just as formal words. The transformed operator is L plus bounded perturbations on that domain. Finite sections give the same estimates uniformly and provide an alternative route to the infinite operator via strong-resolvent/core limits. No operator norm bound on A itself is needed.

Minor wording correction: the opening phrase 'uniformly small lambda/f' should be replaced by 'small lambda, uniformly in f with eta/f in the stated compact interval.' The argument specifically avoids requiring lambda/f small.

Conclusion: steps 1–3 pass for the stated fixed-degree, small-coefficient kinetic perturbation and linear confining potential. They reduce the problem to a nearest-neighbor Jacobi resolvent with a relative O(lambda) perturbation on the nonreal strip. Endpoint Green bounds still require the subsequent local estimates, and none of this establishes a real-axis limit or full-native resonance.
