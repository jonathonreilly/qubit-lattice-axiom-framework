# Independent check: confined fast endpoint resolvent in an O(f) lower strip

The proposed transfer-matrix argument is valid with a fixed interior ellipticity margin and a self-adjoint tail. It proves uniform upper and lower bounds, not convergence of the endpoint resolvent.

## Boundary and resolvent signs

Let H have hopping -2 on n>=1 and v_n=f(n+1), and let u=(z-H)^-1|1>, z=x-i eta, eta>0. At n=1,

(z-v_1)u_1+2u_2=1.

Thus setting u_0=-1/2 makes the homogeneous recurrence

(u_(n+1),u_n)^T=T_n(u_n,u_(n-1))^T,
T_n=[[(v_n-z)/2,-1],[1,0]]

valid from n=1 onward. In particular u_1=g has positive imaginary part in the lower half-plane, and the exact self-adjoint resolvent identity is

Im g = eta ||(z-H)^-1|1>||^2 = eta sum_(n>=1)|u_n|^2.

Both signs in the proposal are correct.

## Uniform transfer estimate

Choose c>0 and a compact x interval such that |v_n-x|<=4-delta for 1<=n<=M=floor(c/f), with delta>0 independent of small f. The example |x|<=1, c=1/2 satisfies this generously. The real transfer matrix has eigenvalues exp(+/-i theta_n), where cos theta_n=(v_n-x)/4. The matrix with columns (exp(+/-i theta_n),1)^T diagonalizes it, has uniformly bounded inverse, and varies by O(f) per step. The actual complex transfer differs from the real one by O(eta).

In these moving bases every step has norm at most 1+C(f+eta); consecutive basis changes satisfy the same estimate. Therefore every prefix product obeys

||T_m ... T_1|| <= C exp(C m(f+eta)) <= C_*

for all m<=M when eta<=c1 f. All constants depend only on the fixed ellipticity margin, c and c1. The inverse products obey the same bound, either by the corresponding moving-basis argument or by det T_n=1: a 2x2 complex matrix of determinant modulus one has reciprocal singular values, hence equal operator norms for it and its inverse.

Consequently each pair (u_(m+1),u_m), m=1,...,M, has squared norm at least C_*^(-2)(|g|^2+1/4). Summing these pairs and counting each physical component at most twice yields

sum_(n>=1)|u_n|^2 >= M/(2 C_*^2) (|g|^2+1/4).

For sufficiently small f, M>=c/(2f). If eta>=c0 f, this gives

Im g >= alpha (|g|^2+1/4), alpha=c0*c/(4 C_*^2)>0.

Since Im g<=|g|, it follows, for example, that alpha/4<=|g|<=1/alpha and Im g>=alpha/4. These bounds are independent of f and the detailed tail. The proof uses only physical components up to M+1; a finite self-adjoint chain must have N>=M+1. For the infinite confining Jacobi operator the nonreal resolvent exists and the same argument applies. The claim does not extend to arbitrary absorbing/non-self-adjoint tails without replacing the resolvent identity.

## Consequences and limits

If an independently established outgoing host Green function satisfies |G_d(z)| growing as log(1/lambda), while z=O(lambda), and f=lambda^3/16 with c0<=eta/f<=c1, then the proven bounds imply

|g(z) G_d(z)| -> infinity, and |z/g(z)| -> 0.

No pointwise limiting value of g is required. The fast confining arm resolvent here is its ordinary meromorphic/self-adjoint resolvent in the lower half-plane; the open host function must separately use the outgoing continuation appropriate to a resonance. Conflating that host continuation with the lower-half-plane physical-sheet value would change the resonance construction.

The strip condition must hold for the actual spectral points being used. It cannot itself prove existence of a pole with eta proportional to f: that would be circular if the claimed pole width were the only justification for the condition. It supplies a uniform estimate on the whole prescribed strip, available for a subsequent resonance existence/asymptotic argument.

This does not control eta/f tending to zero, nor the real-axis pointwise line shape. The confined arm has real discrete poles and zeros; real-axis limits can be highly nonuniform. It also does not establish the logarithmic host asymptotic, the final source formula, or validity of omitted native terms. Those remain separate inputs. Within these qualifications, there is no hidden gap, adiabatic theorem, or large-volume assumption beyond enough chain length to contain the explicitly controlled initial segment.
