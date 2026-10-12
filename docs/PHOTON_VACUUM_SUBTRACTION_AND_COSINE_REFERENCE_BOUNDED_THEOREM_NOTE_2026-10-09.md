---
claim_id: photon_vacuum_subtraction_and_cosine_reference_bounded_theorem_note_2026-10-09
claim_type: bounded_theorem
claim_scope: "For a supplied nonzero-mode bosonic harmonic reference on every periodic cubic lattice L>=3 and k!=0, exact complete vacuum-subtracted order-g^4 coefficient and uniform two-insertion full-cosine form bounds for 0<g<=1/2. The reference resolvents, carrier, geometry and normalization are explicit. Compact spectral identification and higher-interaction remainder estimates are separate research targets."
upstream_dependencies: []
runner: scripts/photon_vacuum_subtraction_and_cosine_reference_2026_10_09.py
---

# Vacuum-subtracted photon coefficients and two-insertion cosine bounds

**Type:** bounded_theorem

**Status:** proposed_retained

The mathematical results below concern a specified bosonic harmonic reference.
Their current surface status is conditional-support. Independent retained-status
audit has not occurred.

## Exact target and supplied inputs

For every periodic cubic lattice of integer side length $L\ge3$ and nonzero
momentum $k$, compute the complete vacuum-subtracted formal order-$g^4$ gap
coefficient and bound the reference functional with two full cosine insertions.
Use the momentum grid $\mathcal K_L=(2\pi/L)\{0,\ldots,L-1\}^3$,
with momentum sums taken modulo $2\pi$, and define

$$\omega(k)=\left(\sum_{i=1}^3|e^{ik_i}-1|^2\right)^{1/2},
\qquad c_L=\frac1{3L^3}\sum_{k\in\mathcal K_L\setminus\{0\}}\omega(k).$$

The conclusions are

$$D_4(k)=-\frac{c_L^2}{32}\omega(k)I-K_-(k)-K_+(k),$$
$$-\frac{65}{48}\omega(k)I\preceq D_4(k)\preceq-\frac{1}{96}\omega(k)I,$$
$$\frac{g^4}{192}\omega(k)I\preceq S_g(k)\preceq5g^4\omega(k)I
\qquad(0<g\le1/2).$$

The supplied research Hamiltonian motivating the reference is
$H_g=(g^2/2)\sum E_l^2+g^{-2}\sum_p(1-\Re U_p)$, with periodic cubic
geometry, Gauss law, zero electric winding, no matter, and specified units and
clock. These are model choices. The actual theorems use the explicitly defined
Fock reference below, including its omission of zero-frequency modes.

The Gaussian formula defining $D_4$ is a mathematical coefficient definition.
Identifying it with an asymptotic expansion of the compact Hamiltonian, or
controlling a remainder uniformly in volume, is a separate research target.
$S_g$ uses the free reference resolvent between two exact cosine vertices:

$$W_g=\sum_p\left[\frac{1-\cos(gB_p)}{g^2}-\frac{B_p^2}{2}\right].$$

No observation, fitted constant or new framework axiom is used. The adjacent
fixed-volume compact analysis is
`docs/EXACT_GAUSS_REDUCTION_AND_FIXED_VOLUME_WEAK_COUPLING_SPECTRUM_BOUNDED_THEOREM_NOTE_2026-09-13.md`;
it is contextual and is not an imported lemma. Every estimate needed for these
two reference results is proved in this note. No priority claim is made for
normal ordering, perturbation theory, or the commutator method.

## Proof-obligation map

The reference Gram and covariance identities define the normalization. The
chord inequality proves positivity of the restricted energy denominators.
Normal ordering and the oscillator commutator yield the entire coefficient,
including spectator exchange and interference. Ordered tensor estimates bound
its two positive forms. For the full cosine, convergent Fock expansions and the
integrated real covariance identity control the interference before estimating
the two connected forms. Each of these obligations is proved below.

Labels T1, T2 and T3 in the proof mean, respectively, the exact coefficient,
its displayed uniform bounds, and the displayed full-cosine bound. They are
local equation references, not separate claim classes.

## Complete reference and domain definitions

Write N=L^3, p=(x,i<j) for the 3N oriented plaquettes. The real link-start
curl C maps link variables to plaquette circulations. Its positive normal
modes u_mu are real orthonormal eigenvectors of C^T C, with eigenvalues
w_mu^2>0, mu=1,...,2(N-1). Define

```text
v_(p,mu)=(C u_mu)_p/sqrt(2w_mu),
B_p=sum_mu v_(p,mu)(a_mu+a_mu^dag),
[a_mu,a_nu^dag]=delta_(mu,nu), H0=sum_mu w_mu a_mu^dag a_mu.
```

The carrier is bosonic Fock space over these modes; Omega is its vacuum.
Gradient and harmonic zero modes have not been turned into oscillators.
This omission defines the reference and does not dispose of compact torus
holonomies or electric winding in the original model.

The real normal modes may equivalently be Fourier transformed. For
k in (2pi/L){0,...,L-1}^3 modulo 2pi, k!=0, put d_i=exp(i k_i)-1. Choose
any two Hermitian-orthonormal polarizations e_lambda perpendicular to d.
Then

```text
b_(ij,lambda)=d_i e_(j,lambda)-d_j e_(i,lambda),
sum_(i<j) conjugate(b_(ij,lambda)) b_(ij,rho)
              =omega(k)^2 delta_(lambda,rho),
v_(x,ij;k,lambda)=exp(i k.x)b_(ij,lambda)/sqrt(2N omega(k)).
```

In this Fourier basis B_p=sum_alpha[v_(p,alpha)a_alpha+
conjugate(v_(p,alpha))a_alpha^dag]. Complex polarizations need not be
continuous in momentum. Results are basis independent. The real construction provides the conjugation used
below; it also includes self-inverse zone-boundary momenta without any
extra factor of two.

Two identities, directly from C^T C and Fourier orthogonality, are

```text
sum_p v_(p,mu)v_(p,nu)=(w_mu/2)delta_(mu,nu),
sum_mu v_(p,mu)^2=c_L, independently of p.                (R1)
```

The second follows by translation/cubic symmetry and summing over p.
The average of omega^2 over the full grid is exactly 6; omega<=sqrt(12).
Thus mean(omega)>=sqrt(3), mean(omega)<=sqrt(6), and

```text
1/sqrt(3)<=c_L<=sqrt(2/3).                               (R2)
```


Let f be any normalized one-photon state of total momentum k!=0, with
energy w=omega(k). Write a_f^dag=sum_mu f_mu a_mu^dag and
v_(p,f)=sum_mu v_(p,mu)f_mu. Then sum_p |v_(p,f)|^2=w/2.
Coefficient conjugation J in the real occupation basis sends f to momentum
-k with energy w and acts on every Fock sector.
Let P_(1,k) be the two-dimensional one-photon space. Q_k is the remaining
ODD-particle subspace at the SAME total momentum k. Set

```text
R_k=(H0|_(Q_k)-w)^-1.
```

Translation permutes the plaquettes, so every interaction sum preserves total
momentum. Each interaction is even in the fields. Its centered vacuum vector
therefore has zero total momentum and even particle parity. These facts fix
the sectors in the subsequent resolvent identities.

Only this restricted inverse is used. No inverse over all momenta is meant.
For vacuum excitations use H0^-1 on the non-vacuum subspace.

## Denominator lemma and existence of the restricted inverse

For p,q in the d-dimensional continuous momentum torus, put
x_j=exp(i p_j)-1, y_j=exp(i p_j)(exp(i q_j)-1),
a=||x||, b=||y||, gamma=||x+y||. If a b=0 the following bound is immediate.
Otherwise let z=y-(b/a)x. Since the phases have unit modulus,

```text
Re sum_j exp(-i p_j)z_j=-b(a+b)/2,
```

so ||z||^2>=b^2(a+b)^2/(4d). But

```text
||z||^2=2b^2[1-Re<x,y>/(ab)].
```

Consequently (a+b)^2-gamma^2>=ab(a+b)^2/(4d), and division by
(a+b+gamma)<=2(a+b) proves

```text
omega(p)+omega(q)-omega(p+q)
    >=omega(p)omega(q)[omega(p)+omega(q)]/(8d).           (R3)
```

It is positive for nonzero p,q, even if their sum vanishes. All sums are
modulo 2pi, so wrapping and opposite momenta are included.

For n>=3 nonzero momenta let alpha>=beta>=gamma be the three largest
frequencies. Pair the largest two first, and use ordinary triangle
inequality for the rest. With Delta_n=sum_j omega(q_j)-omega(sum_j q_j),

```text
Delta_n>=alpha beta(alpha+beta)/(8d)>0,
product_j omega(q_j)/Delta_n<=4d(2sqrt(d))^(n-3).         (R4)
```

Here gamma/(alpha+beta)<=1/2 and each remaining frequency is <=2sqrt(d).
At fixed L the smallest nonzero w_mu is positive. For bounded H0 energy
there are only finitely many occupation states; (R3) excludes equality at
fixed momentum. Hence R_k is a bounded positive inverse at each fixed L,
although its norm need not be bounded uniformly in L. We will bound the
specific interaction forms instead. k=0 and oscillators of zero energy are
excluded from every result; there is no division-by-zero convention.

## Define the entire order-g^4 gap coefficient

The harmonic expansion has coefficients

```text
V4=-(1/24)sum_p B_p^4, V6=(1/720)sum_p B_p^6.
```

Normal ordering is with respect to Omega and the stated CCR. In particular,

```text
B^4=:B^4:+6c_L:B^2:+3c_L^2,
B^6=:B^6:+15c_L:B^4:+45c_L^2:B^2:+15c_L^3.
```

Using (R1) gives exact compression identities

```text
P1[V4-<V4>_Omega]P1=-(c_L/4)H0|_(P1),
P1[V6-<V6>_Omega]P1=(c_L^2/16)H0|_(P1).                (R5)
```

The order-g^2 coefficient is therefore D2(k)=-(c_L/4)w I.

The order-g^4 matrix is DEFINED by the finite Gaussian perturbation formula

```text
<f,D4(k)f>=<f,V6 f>-<Omega,V6 Omega>
           -<Q_k V4 f,R_k Q_k V4 f>
           +<v0,H0^-1 v0>,
v0=(V4-<V4>_Omega)Omega.                               (R6)
```

There is no claim here of an analytic compact-model eigenbranch or an
error term in a physical expansion. The notation w I+g^2 D2+g^4 D4 denotes
these coefficients, not an established approximation with a remainder.
All vectors in (R6) have finite particle support, so their domains are exact.

Put B_(p,+)=sum_mu v_(p,mu)a_mu^dag. Normal ordering gives

```text
v0=-(c_L/4)sum_p B_(p,+)^2 Omega
                      -(1/24)sum_p B_(p,+)^4 Omega,
C_f=-(1/6)sum_p v_(p,f) B_(p,+)^3 Omega,
s_f=a_f^dag v0,
Q_k V4 f=s_f+C_f.                                    (R7)
```

The last identity follows either from Wick expansion or
[V4,a_f^dag]=-(1/6)sum_p v_(p,f)B_p^3; its one-particle part is precisely
-(c_L/4)w f and is removed by Q_k. Thus no spectator channel is discarded.

## Exact cancellation, including exchange and interference

The oscillator commutator gives

```text
R_k a_f^dag v0=a_f^dag H0^-1 v0.                       (R8)
```

Since a_f a_f^dag=1+a_f^dag a_f and
 a_f H0^-1=(H0+w)^-1 a_f,

```text
<s_f,R_k s_f>-<v0,H0^-1 v0>
  =<a_f v0,(H0+w)^-1 a_f v0>.
```

Furthermore

```text
a_f v0=-(c_L w/4)Jf+J C_f.
```

The two terms have particle numbers 1 and 3 and are orthogonal. Conjugation
commutes with H0. Define

```text
K_-(f)=<C_f,(H0-w)^-1 C_f>,
K_+(f)=<C_f,(H0+w)^-1 C_f>,
```

with the first inverse only in three-particle momentum-k space. We obtain

```text
<s_f,R_k s_f>-<v0,H0^-1 v0>=c_L^2 w/32+K_+(f).        (R9)
```

This is the finite Bose-exchange remainder after the extensive cancellation.

The interference is also explicit. Its degree-two part is the only one
that can contribute:

```text
<s_f,R_k C_f>=<H0^-1 v0,a_f C_f>,
(H0^-1 v0)_(2)=-(c_L/16)sum_mu (a_mu^dag)^2 Omega,
a_f C_f=-(1/2)sum_p |v_(p,f)|^2 B_(p,+)^2 Omega.
```

The contraction <Omega,(sum_mu a_mu^2)B_(p,+)^2 Omega>=2c_L and (R1) give

```text
<s_f,R_k C_f>=c_L^2 w/32.                            (R10)
```

The cross term in the squared norm is TWICE (R10). Combining (R5), (R9),
(R10) and K_- proves (T1).
Each step holds for every complex f in the two-dimensional momentum space;
polarization therefore gives the Hermitian matrix identity, including all
off-diagonal matrix elements and polarization degeneracies.

## Uniform bounds on K_- and K_+

For an ordered, momentum-matched triple alpha_j=(q_j,lambda_j), define

```text
T_(alpha1,alpha2,alpha3;f)=sum_p v_(p,f)
                                    product_j conjugate(v_(p,alphaj)).
```

The exact contraction factor is

```text
K_±(f)=(1/6)sum_ORDERED |T|^2/[sum_j omega(q_j) ± w].   (R11)
```

Repeated modes are included: the symmetric creation tensor has squared norm
3! times its ordered tensor norm, multiplied by (1/6)^2 from (R7).
The plus denominator is used for K_+, the minus denominator for K_-.

For a matched triple, Fourier summation and Holder's inequality on the
three plaquette orientations give

```text
|T|^2<=w product_j omega(q_j)/(16N^2).
```

There are at most N^2 ordered momentum pairs and 2^3 polarization choices.
For K_-, (R4) at d=3,n=3 bounds the frequency quotient by 12, giving K_-<=w.
For K_+, set Omega_max=2sqrt(3). Since each frequency is <=Omega_max,

```text
product_j omega(q_j)/(sum_j omega(q_j)+w)<=Omega_max^2/3=4.
```

Thus K_+<=w/3. Both forms are positive. Together with (R2), these inequalities
prove (T2). The proof holds for every finite L and every nonzero external
momentum, not merely the smallest momentum or sampled boxes.

## Separate extension: full-cosine second Born functional

Fix g>0 and write c=c_L, y=g^2 c, r=exp(-y/2), t=(r-1)/2.
Let W_g be the exact interaction defined in the target statement above. Put

```text
v_g=(W_g-<W_g>_Omega)Omega,
S_g(f)=<Q_k W_g f,R_k Q_k W_g f>-<v_g,H0^-1 v_g>.       (F1)
```

This is a difference of two positive reference forms, not a physical
spectral gap. At fixed L all the vectors below have convergent Fock series:
||(B_(p,+))^m Omega||=sqrt(m! c^m), and the cosine coefficients have m!
in their denominators. Polynomial energy/number weights also converge.
Thus the creation/annihilation operations, the finite-volume resolvents
and the following convergent form sums are defined.

The normal-order identity exp(i g B)=r:exp(i g B): gives

```text
P1[W_g-<W_g>_Omega]P1=t H0|_(P1),
v_g=t sum_p B_(p,+)^2 Omega
     +sum_(even m>=4) A_m sum_p B_(p,+)^m Omega,
A_m=r(-1)^(m/2+1)g^(m-2)/m!.
```

Its connected part C_(g,f) has odd n>=3 with coefficients

```text
r(-1)^((n+1)/2+1)g^(n-1)/n!
times sum_p v_(p,f) B_(p,+)^n Omega.
```

The same commutator as (R7) gives Q_k W_g f=a_f^dag v_g+C_(g,f).
Moreover a_f v_g=t w Jf+J C_(g,f). Therefore the EXACT cancellation identity
is

```text
S_g(f)=t^2 w/2+K_(g,-)(f)+K_(g,+)(f)+2 Re X_g(f),
K_(g,±)=<C_(g,f),(H0±w)^-1 C_(g,f)>,
X_g=<H0^-1 v_g,a_f C_(g,f)>.                          (F2)
```

The minus inverse remains restricted to momentum k and odd particle number
>=3. There is no exclusion of spectator terms in S_g; the decomposition
merely lets their extensive part cancel exactly.

## The interference kernel and its sign-controlled bound

Define the REAL covariance kernel in the real normal-mode basis,

```text
G_tau(p,q)=sum_mu v_(p,mu)v_(q,mu)exp(-tau w_mu).
```

Cauchy-Schwarz gives |G_tau(p,q)|<=c. Equation (R1) also gives the exact
sum/integral identity

```text
sum_p integral_0^infinity G_tau(p,q)^2 d tau=c/4.        (F3)
```

Indeed summing over p leaves
sum_mu v_(q,mu)^2(w_mu/2)exp(-2tau w_mu), whose integral is c/4.

For even m>=2 put

```text
J_m(f)=sum_(p,q) |v_(q,f)|^2 integral_0^infinity
                                             G_tau(p,q)^m d tau.
```

These quantities are nonnegative, since m is even. We have

```text
J_2=c w/8,  0<=J_m<=c^(m-1)w/8.                       (F4)
```

The exact m-particle resolvent contraction is m! times the covariance
integral. For m=2 the interference is therefore

```text
X_2= -t r y w/8 >=0.
```

For every even m>=4 the two cosine coefficients have OPPOSITE signs, giving

```text
X_m= -r^2 g^(2m-2)J_m/m! <=0.
```

Consequently, with X_high=sum_(even m>=4)X_m,

```text
-[r^2 w/(8y)](cosh(y)-1-y^2/2)<=X_high<=0.             (F5)
```

These estimates justify absolute summation and show why simply omitting
interference, or assuming that every interference term has the same sign,
would be incorrect. The g^4 limit recovers (R10); higher cross terms begin
at order g^6.

## Full connected forms and an explicit uniform result

Let x=Omega_max g^2, Omega_max=2sqrt(3). An n-photon ordered vertex has

```text
|T_n|^2<=N^(1-n)w product_j omega(q_j)/2^(n+1),
```

with at most N^(n-1)2^n momentum/polarization choices. The coefficient and
boson contraction leave r^2 g^(2n-2)/n!. Applying (R4) gives

```text
K_(g,-)<=w F_-,
F_-=6r^2 g^4 [sinh(x)-x]/x^3.
```

For the plus denominator,

```text
product_j omega(q_j)/(sum_j omega(q_j)+w)
                              <=Omega_max^(n-1)/n,
```

which gives

```text
K_(g,+)<=w F_+,
F_+=(r^2/2)sum_(odd n>=3) x^(n-1)/(n n!).              (F6)
```

Both series converge for every finite g. The first bracket has value 1/6
at x=0; F_+ is defined by its entire series, so no special function import
is needed.

Writing

```text
A0=t^2/2-t r y/4,
H=r^2[cosh(y)-1-y^2/2]/(4y),
```

(F2)-(F6) establish the sharper all-g two-sided form bound

```text
(A0-H)w <= S_g(f) <= (A0+F_-+F_+)w.                  (F7)
```

All these are matrix inequalities since f is arbitrary. Values at g=0
are defined by continuity and are zero.

For 0<g<=1/2, (R2) gives 0<y<1/4 and 0<x<1. Since

```text
1-r>=yr/2, cosh(y)<=2,
cosh(y)-1-y^2/2<=y^4 cosh(y)/24,
```

we obtain

```text
A0-H>=r^2 y^2(1/32-y/48)>=r^2 y^2/48.
```

Also r^2=exp(-y)>=1-y>=3/4 and c^2>=1/3, so

```text
A0-H>=g^4/192.
```

For the upper bound, |t|<=y/4 implies A0<=3y^2/32<=g^4/16.
Comparing factorials in (F6) with the exponential series gives

```text
F_-<=g^4 exp(x)<3g^4,
F_+<=(g^4/3)exp(x)<g^4,
```

where exp(x)<exp(1)<3 follows directly from its factorial series. Hence
A0+F_-+F_+<5g^4. This proves (T3) without a fitted constant, sampled-volume
argument or a compact-spectrum identification.

## Remaining physical target and boundary cases

The strongest next obligation is a compact-state construction with justified
vacuum subtraction and volume-uniform control beyond two bare insertions,
retaining Gauss, winding and torus holonomy. Such an expansion route may be
stronger than existence of a photon phase; no equivalence is asserted.
A variational spectral-measure route with a dressed trial state is another
live approach. This note supplies upstream reference estimates for those
consumers, without a physical spectrum or residue claim.

Zero momentum and zero-frequency oscillators are excluded explicitly. The
proof includes repeated nonzero modes, complex polarizations and self-inverse
zone-boundary momenta. The coupling restriction applies to the final simple
constants; the preceding functional bound is stated for every finite $g$.
There is no general impossibility or exhaustive route-exclusion claim.

## Reproduction and review record

Primary runner:
[scripts/photon_vacuum_subtraction_and_cosine_reference_2026_10_09.py](../scripts/photon_vacuum_subtraction_and_cosine_reference_2026_10_09.py).
It declares a 120-second audit timeout and uses the standard library and NumPy.
Exact occupation-monomial calculations evaluate complete quartic/sextic matrix
elements separately from the analytic commutator proof. Independent copies
change the extensive vacuum term while preserving the gap coefficient.
Fourier checks sample $L=3,4$ and six momenta. Full-cosine one-mode truncations
are convergence diagnostics, not an infinite-series remainder certificate.
The uniform mathematical claims rest on the proofs, not the sampled boxes.

The final runner is executed through the repository cache envelope. Independent mathematical review rederived the complete coefficient,
complex-polarization conjugation, all-volume bounds and convergent cosine
interference estimates. Separate normalized-oscillator, real-space curl and
Gaussian-quadrature calculations supported that review. The reviewer caught
an omitted dispersion/variance definition in the initial packaging; both
explicit definitions are restored above.

Scratch mutations exposed a Fourier combinatorial-factor diagnostic that
was too weak. The runner now also contracts unordered occupation monomials
with factorial weights. It rejects both a doubled ordered Fourier coefficient
and incorrect occupation factorials. The final baseline has 41 passing finite
checks. These diagnostics support the analytic proof without replacing it. No Lean proof
is claimed. Finite CCR identities and the chord lemma are possible scoped Lean
audit targets; the infinite Fock and compact-model obligations remain distinct.

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Control periodic weak-coupling photon corrections with vacuum subtraction."
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Construct a compact-state comparison and control higher interacting contributions."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Uniform reference-model estimates with explicitly supplied geometry and carrier."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```
