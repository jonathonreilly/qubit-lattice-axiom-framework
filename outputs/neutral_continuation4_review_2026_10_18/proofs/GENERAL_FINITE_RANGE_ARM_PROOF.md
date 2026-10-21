<!-- Owning original: PR9750; source SHA256 4b8988bd444a2738296596657e872b110ad8562cf792acfce45c00622490e084. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Root extension: any fixed-range near-nearest arm

Goal: H_lambda=p_lambda(T)+v(n)+F_lambda, T=S+S*, p_lambda(t)=-2t+O(lambda) polynomial of fixed degree with uniformly O(lambda) coefficients for the correction, v(n)=f(n+1)+a, f>0, x-a=O(lambda), eta/f in a fixed positive compact interval. F_lambda is a fixed-endpoint Hermitian matrix O(lambda). Prove bounded endpoint Green entries and positive Im at e1 for z=x-i eta, for small lambda uniformly in f at fixed eta/f; no lambda<<eta condition. This would cover finite-order long-arm kinetic corrections without assuming the earlier quadratic form.

1. Choose a fixed smooth compact-support function g_lambda(t)=O(lambda) in every C^k norm, agreeing with p_lambda(t)+2t on [-2,2], with ||g'_lambda||<1. Define ptilde=-2t+g_lambda(t); it is globally strictly decreasing. Set A(n)=ptilde^-1(x-v(n)). Then A increments O(f) globally, A grows linearly, and p_lambda(T)+v-x=ptilde(T)-ptilde(A) since spectrum(T)subset[-2,2]. Put L=T-A. Its first M~c/f sites remain uniformly elliptic for fixed smallc.

2. Fourier-Duhamel identity gives
 g(T)-g(A)=B L+E,
 B=integral ĝ(t) i integral_0^t exp(i(t-s)T)exp(isA) ds dt,
 ||B||=O(lambda), ||E||=O(lambda f).
Indeed moving L past exp(isA) costs O(f|s|), and all Fourier moments are finite. Also [L,B]=O(lambda f), since [L,T] and [L,A] are O(f). For Hermitian g(T)-g(A), symmetrize the identity:
 g(T)-g(A)=(B_s L+L B_s)/2 + E',
 with B_s=(B+B*)/2 and ||E'||=O(lambda f). The discarded antisymmetric part gives a commutator [B_a,L], bounded O(lambda f), not an unbounded product B_a L.

3. C=2I-B_s is bounded positive and C-2I=O(lambda). Thus H0-x=-(CL+LC)/2+O(lambda f). The square-root doublecommutator bound gives
 H0-x=-sqrt(C)Lsqrt(C)+R, ||R||=O(lambda f),
 since [C,L]=O(lambda f), [C,[C,L]]=O(lambda² f). Here the error E' already dominates. The exact transformed resolvent is (z-H0)^-1=C^-1/2 [L-i eta C^-1-C^-1/2 R C^-1/2]^-1 C^-1/2. Relative to L-i eta/2, the error is O(lambda eta), so the global Neumann series converges for smalllambda.

4. L is a standard nearest-neighbor Jacobi operator. Its transfer products and inverses on first M~c/f are bounded. The physical lower-half-plane resolvent appropriate to the sign above has a uniformly bounded first entry and positive dissipation; the sign conventions must be tracked explicitly. Recurrences then give uniformly bounded g_ij for ALL i,j<=M, not only fixed endpoints: the left and Weyl solutions propagate via bounded transfer products. Consequently local source estimates use the l1 norm on this segment, with ||R0 v||<=C||v||1/sqrt(eta).

5. B has arbitrarily high uniform offdiagonal moments O(lambda): e^{itT} has polynomial weighted row/column bounds growing polynomially in |t|, e^{isA} is diagonal unitary, and ĝ has all moments. C^-1/2 is therefore (1/sqrt2)I+O(lambda) in any fixed polynomial-weighted Schur norm, by its convergent power series for sufficiently smalllambda. The transformed endpoint source tends to delta_j/sqrt(2) and has l1 tail beyond M bounded C_p lambda M^-p. Its crude global error divided byeta tends to zero for p>1, sinceM~1/f. The finite segment contribution is controlled by the uniform Green kernel and differs O(lambda) from the original endpoint. This establishes bounded endpoint entries and positive directional Im, after the O(lambda eta) perturbation. Finally F_lambda is finite-rankO(lambda), handled by bounded endpoint Green matrices.

Status: bounded-support; independent algebra and boundary checks PASS. No full native resonance or source identification. Need careful signs in step3/4, exact Fourier normalization cancels if consistently used, and domain closure via finite sections. Fixed polynomial degree/endpoint support and smallcoefficients are essential. The result concerns ordinary selfadjoint arm resolvent in the prescribed nonrealstrip, not outgoinghost or realaxislimit.
