# Integrated identities and exact non-small rate fluctuations

Personal derivation, 2026-09-15; exploratory support for the fixed-clock
campaign. These identities do not prove a spectral gap or a Gaussian limit.
Use exactly the carrier, potential, and generator in
BLOCK1_POSITIVE_HYBRID_GENERATOR.md, with oriented moves v=+/-h e_p.
Write q_v=v.A v and a_vw=v.A w. Expectations below are under the actual
centered filtered clock law, not the unrestricted Gaussian reference.

## 1. Exact rate moments

For any real k, let m_k(v)=E[c_v^k]. The Gaussian tails and bounded periodic
potential in a fixed box ensure finiteness. The exact carrier translation
identity for M(t)=E exp(t.z) gives

 M(t-A v)=exp[q_v/2-t.v] M(t),
 m_k(v)=exp[-k q_v/4] M(-k A v/2).

Therefore

 m_(k+2)(v)=exp[k q_v/2] m_k(v).                      (1)

In particular, for every integer n>=0,

 m_(2n)=exp[q_v n(n-1)/2],
 m_(2n+1)=exp[q_v n^2/2] m_1.                        (2)

The previously derived bound m_1<=exp[-q_v/8] coexists with

 E c_v^2=1,       E c_v^4=exp(q_v),
 Var(c_v)=1-(E c_v)^2 >= 1-exp[-q_v/4].              (3)

Thus these rates do not become small in L2 as beta grows, even though
their mean vanishes. This is an exact property of the proposed dynamics,
not evidence that the equilibrium model has a large defect density.
The exceptional large rates compensate their small probabilities.

For 0<=k<=2, the centered MGF bound gives

 m_k <= exp[q_v k(k-2)/8].                            (4)

More generally (4) holds for all real k, but its right side grows when
k lies outside [0,2]. For any 1<=k<2 it provides a decaying Lk norm.
Evenness and translation also imply m_k=m_(2-k). Neither (3) nor (4)
supplies a multiplication-operator bound for c_v on arbitrary functions.
Indeed c_v is unbounded on the carrier, already along exact directions
with P A v nonzero. On compactly supported functions concentrated at such
points, E[c_v f^2]/E[f^2] can be arbitrarily large. This rejects only a
specific unweighted perturbation estimate. A weighted argument remains open.

## 2. Mixed diffusion/jump identity

Let g=P grad f. For smooth compactly supported tests on the carrier,
integration by parts in the exact fibers and jump detailed balance give

 E[(L_c f)(L_j f)]
   = (1/2) sum_v E[c_v |g(z+v)-g(z)|^2]
     +(1/2) sum_v E[c_v g(z).(P A v) Delta_v f].       (5)

To verify the signs, differentiate the jump generator:

 P grad L_j f=sum_v c_v[Delta_v g-(P A v)Delta_v f/2].

Pairing the first term with -g and using reversibility yields the first
term in (5). Applying reversibility to the second term gives the equivalent
form with g(z) replaced by [g(z)+g(z+v)]/2. Its sign is not fixed.
Consequently the small mean-rate bound alone cannot discard this coupling.
The full integrated identity E Gamma2(f)=E(Lf)^2>=0 still holds; a positive
lower bound by E Gamma(f) is the separate spectral-gap obligation.

## 3. An admissible jump-pair weight

For two moves define r(v,w)=exp[-a_vw/4] and

 R(dz,v,w)=pi(dz)c_v(z)c_w(z)r(v,w).

All translations commute. The measure is invariant under exchanging v,w,
and under (z,v,w)->(z+v,-v,w). In fact

 c_w(z+v)/c_w(z)=exp[-a_vw/2],
 r(-v,w)=exp[+a_vw/4].

These identities, together with detailed balance, prove admissibility.
No sign assumption on the off-diagonal entries of A is necessary. The
usual four-corner change of variables then gives the exact identity

 E[(L_j f)^2]
   =(1/4) sum_(v,w) E[c_v c_w r(v,w)(Delta_v Delta_w f)^2]
     +sum_(v,w) E[c_v c_w(1-r(v,w))Delta_v f Delta_w f]. (6)

This is verified by expanding the squared second difference and applying
the two invariances to its terms. The second term is not manifestly positive.
The centered MGF nevertheless gives the volume-independent mean bound

 E[c_v c_w r(v,w)] <= exp[-(q_v+q_w)/8].              (7)

Indeed the exponent before taking the MGF is
-(q_v+q_w+a_vw)/4, and its MGF argument is -A(v+w)/2.
The quadratic upper bound adds (q_v+q_w+2a_vw)/8,
so the cross term cancels exactly. Equation (7) does not bound the
same weight multiplied by arbitrary squared derivatives of f.

## 4. Literature match and next obligation

Dai Pra and Posta, *Entropy Decay for interacting systems via the
Bochner-Bakry-Emery approach*, arXiv:1205.4599v3,
https://arxiv.org/html/1205.4599v3, section 2.3, supplies the general
admissible-move identity behind (6). Its sufficient estimate uses a
pointwise bound on weighted off-diagonal rates. Sections 3.1-3.2 treat
repulsive birth/death systems with a low-density condition, and one
special two-coordinate convex example. Those example hypotheses do not
match this hybrid constrained gauge law. Equations (1)-(7) above were
derived for this law; the paper does not establish its mixing or response.

A useful next result must control the residual in (5)-(6), or find an
alternative dynamics/representation with controlled source response.
Merely assuming that response, or replacing weighted expectations by
products of separate means, would reintroduce the original hard problem.

## Finite source challenge

The companion `../evidence/block1_integrated_rate_check.py` checks the exact
second/third/fourth rate moments, moment reflection, the admissible pair-weight
bound, and the integrated jump identity for four Fourier tests. It uses the
original clock-link/image source evaluator on three free three-cubes.
Maximum moment relative error is 5.12e-14; maximum integrated-identity relative
error is 2.33e-16. No sampling of the generator, asymptotic phase calculation,
or independent review is used.
