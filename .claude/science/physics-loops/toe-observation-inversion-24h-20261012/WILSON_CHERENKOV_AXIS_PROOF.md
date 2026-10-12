# Exact Wilson axis non-opening lemma — author derivation

2026-10-12, before focused checker exposure. Same w=1, a²=1−mu, 0<mu<1 target. This is not a general-direction no-go.

Write v_i=1−cos p_i. The matched electron square is e²=mu²+2 sum v_i+2 sum_(i<j) v_i v_j+mu sum v_i². It is strictly increasing in every v_i≥0. For incoming p=(P,0,0), any transverse photon momentum k_y,k_z adds nonnegative v_i to both outgoing electron p−k and photon k, and cannot lower their combined energy. Thus minimizing the emitted two-body energy may set k_y=k_z=0, on the full torus.

On that axis define the two-component Bloch vector d(P)=(sqrt(1−mu)sinP,mu+1−cosP), so e(P)=|d(P)|. The reverse norm inequality gives
 e(P)−e(Q) <= |d(P)−d(Q)|
 <= sqrt[(sinP−sinQ)²+(cosP−cosQ)²]
 =2|sin((P−Q)/2)|=omega(P−Q).
The second inequality uses0<mu<1. Therefore no strict Cherenkov energy opening exists for an exactly axial incoming momentum, including arbitrary torus outgoing momenta. At P=pi,Q=0 equality holds: e(pi)=mu+2, e(0)=mu, omega(pi)=2. Equality at a finite isolated partition is not a positive phase-space decay theorem. For mu>0, nontrivial equality in the second inequality requires sinP=sinQ, and equality in the first further requires collinear Bloch vectors; apart from zero photon momentum, the opening-direction equality is precisely the corner-to-center axial configuration (modulo torus/reflection). Do not infer finite width there.

This proof is stronger than the leading-A4=1 quartic result and uses a norm contraction, not a failed search. The corresponding contraction does not hold for general directions because the Wilson beta component sums the cosine differences before squaring; cross terms can be positive. A separate fixed-direction Cherenkov threshold is therefore consistent with this axis exception.
