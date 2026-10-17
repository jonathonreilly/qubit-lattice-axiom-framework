# Explicit finite readiness and finite-apparatus horizons

Provisional root extension of CANDIDATE_V2.md. Not yet independently checked.
This derives quantitative replacements for the density statement in section6;
it does not change the infinite-tail theorem or turn a finite clock into a
permanent halt device. All symbols use the candidate's conventions.

## 1. Finite-support ready packet

Use (20), so A_T=||a_-T||>=3/4, and choose 0<eta_p<=1/2. For n>2JT the
phase -kn+E(k)T has derivative magnitude at least n-2JT. Integrating by
parts with the same compact support as the candidate gives

    |a_-T(n)| <= [F1/(n-2JT)+2JT F0/(n-2JT)^2]/sqrt(2pi).

Let N be an integer and d=N-2JT>=max(1,2JT). Then for every n>=N the
second term is bounded by F0/(n-2JT). Summing the squares gives

    ||1_(n>=N) a_-T|| <= (F1+F0)/sqrt(pi d).                 (A1)

For any nonzero vector a with ||a||=A and a nonzero orthogonal truncation P a,

    ||a/A-Pa/||Pa|||| <=2||(I-P)a||/A.                       (A2)

The normalization is positive real, preserving phase. By A_T>=3/4, the
right side here is at most4||(I-P)a||. Therefore it is sufficient to take

    N=ceil[2JT+max{1,2JT,16(F1+F0)^2/(pi eta_p^2)}],
    chi_N=1_(0<=n<N) a_-T / ||1_(0<=n<N) a_-T||.             (A3)

This guarantees ||chi_N-chi||<=eta_p. The discarded norm is at mosteta_p/4,
so the truncated vector is nonzero. Because the physical dynamics is unitary,
the infinite-clock theorem with this finite-support independent ready state
has isometry error at mostepsilon+eta_p for every t>=2T. Trace error is at
most2(epsilon+eta_p), capped at2. No clock/source part is discarded.

Equation(A3) supplies an explicit finite vector through ordinary one-dimensional
integrals; those integrals are computable but are not asserted to be exactly
emitted coefficients of a finite machine. A separately certified prepared
vector within eta_a of chi_N costs at mosteta_a uniformly in later time.
The input support size is O(JT+1/(sigma eta_p^2)); under(20) it is
O(epsilon^-3+epsilon^-1 eta_p^-2). This is a resource upper bound, not an
optimized preparation cost or a native packet-preparation theorem.

## 2. Finite chain through a stated physical observation horizon

For M>=N use clock sites0,...,M-1 and add the positive far-end term J n_(M-1)
to (21), preserving the constant2J diagonal in its one-head matrix. Let
h_w,M be the resulting finite one-head operator with the same boundary w.
Its spectrum and the infinite spectrum lie in[0,4J+w], hence both lie in
[0,17J/3] for w=0 or J<=w<=5J/3. Set c=Rho=17J/6 and

    A_infinity=(h_w-cI)/Rho, A_M=(h_w,M-cI)/Rho.

Both are selfadjoint contractions. For any input supported on0,...,N-1,
degree k<d_M=M-N+1 polynomials in these operators give identical vectors
after embedding the finite chain: a path of that degree cannot reach the
first removed site M. This includes the boundary potential and the diagonal
shift, which do not propagate support.

Use the Jacobi-Anger/Chebyshev expansion

    exp(-ixA)=J0(x)I+2 sum(k>=1)(-i)^k Jk(x) Tk(A).

The common scalar exp(-ict) is retained. Since ||Tk(A)||<=1, subtracting the
two evolutions gives

    ||exp(-ith_w)chi_N-embed exp(-ith_w,M)chi_N||
       <=4 sum(k>=d_M)|Jk(Rho t)|
       <=4 exp[-mu d_M+Rho t sinh(mu)]/[1-exp(-mu)], mu>0.    (A4)

The last bound follows by shifting the Bessel generating-function contour;
equivalently it is the same contour inequality proved in section5 of the
existing native half-line clock note, with the actual spectral radius here.
It is uniform on0<=t<=Tobs after replacing t by Tobs. It is not a claim that
individual Bessel absolute values are monotone in time.

Given zeta>0 and Tobs>=2T, choose

    M>=N, and M-N+1 >=
      [Rho Tobs sinh(mu)+log(4/((1-exp(-mu))zeta))]/mu.       (A5)

Then on the complete old/clock/reference output, for every2T<=t<=Tobs,

    isometry error <=epsilon+eta_p+zeta,
    trace norm error <=min(2,2(epsilon+eta_p+zeta)).          (A6)

For a prepared-vector error eta_a add it separately. The old K evolution
commutes with this comparison and uses actual elapsed t throughout. The
finite and infinite clock spaces are compared by the natural isometric
embedding; the target beta_(t-T) remains the stated normalized half-line
vector. This is an operational distance with an explicit embedding, not a
claim that the finite apparatus literally contains omitted output sites.

At fixed mu, the sufficient finite clock size is linear in J Tobs plus N
and log(1/zeta). The added far-end load is3J; other local loads are unchanged.
The whole finite-qubit clock operator norm grows with M, while the prepared
one-head energy bound remains fixed. Finite M has a stated horizon only;
later returns to the entrance are outside(A6). Infinite blank tail, supplied
three-body boundary hardware and readiness remain explicit resources.
