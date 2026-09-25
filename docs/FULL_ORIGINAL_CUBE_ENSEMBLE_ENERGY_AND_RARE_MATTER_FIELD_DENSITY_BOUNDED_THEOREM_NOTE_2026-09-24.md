---
claim_id: full_original_cube_ensemble_energy_and_rare_matter_field_density_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: For the supplied compensated cube, canonical N=4 input, fixed positive parameters and joint integer-spin
  limit, the full original ensemble has a finite ordinary-energy excess and a sharp epsilon^-4 mixed variance coefficient.
  A trace-class rare matter/field density governs both, with an exact frozen-age bright balance. No physical selection,
  reservoir cost or Fisher conclusion.
runner: scripts/full_original_cube_ensemble_energy_and_rare_density_2026_09_24.py
upstream_dependencies:
- actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- minimal_axioms
- ordinary_microscopic_cube_energy_after_the_birth_layer_bounded_theorem_note_2026-09-24
- recent_births_force_full_cube_energy_variance_bounded_theorem_note_2026-09-24
- sharp_actual_rotor_cube_energy_tail_bounded_theorem_note_2026-09-24
---

# Full original cube energy and the rare matter/field density

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

Continuously occurring births leave a rare first-high population whose
probability vanishes while its ordinary energy remains finite. This note
computes that contribution and the full mixed variance coefficient, retaining
the complete original matter/field generator and resolved or coherent
formation instrument. The model, compensation, preparation and scaling are
supplied; they are not selected by this theorem.

The author candidate was sealed before independent reconstruction. The
publication uses the independent PRE's sufficient rate-free age-tightness
proof, with the source grading made explicit from the separately checked
author argument. The density and frozen-age balance were reconstructed in
POST after release; they are not retroactively called blind PRE claims.
Parents remain conditional and unaudited. This is not retained audit status.

## 1. Supported statement and exact domain

Let rho_e(t) be the complete original compensated lambda=0 cube GKLS density from the canonical Hermitian N=4 zero-field input. Fix delta,K,kappa>0 and a finite interval `[t0,T]`, `t0>0`. Take the integer-spin sequence

```
epsilon^2 S(S+1)=delta/K,             S -> infinity.
```

Keep the full original resolved instrument, or the full original coherent edge instrument, throughout. The coherent mark is the sum of its two signs with the supplied normalization. Write H_e for the original physical Hermitian Hamiltonian.

The following limits are supported, uniformly on each such interval:

```
Tr(H_e rho_e(t)) -> E_low(t) + kappa delta I(t),                 (P1)
epsilon^4 Tr(H_e^2 rho_e(t)) -> kappa delta^2 I(t),               (P2)
epsilon^4 Var_(rho_e(t))(H_e) -> kappa delta^2 I(t).              (P3)
```

Here E_low is the full common rotor low-sector ensemble energy defined in (4) below. The additional function is

```
I(t)=sum_i integral_0^infinity ||exp(tau L) R_i u4(t)||^2 d tau,
L=-i delta G_1-kappa Gamma_1/2,
G_1=Pi1(FF*-F*F)Pi1             on physical N=6,W=1,
Gamma_1=2 P_bright,
u4(t)=exp(-24 kappa t) exp(-it H_rot,4) Omega.                   (P4)
```

All operators in this formula are the complete physical rotor operators, not one Fourier fiber. For a mark on edge `(a,b)`,

```
B_i=j_i F P4,
R_i=(j_i F^2/2-F j_i F)P4=-F_a j_i F_a P4.                     (P5)
```

I is finite and continuous on bounded physical-time intervals, and

```
I(t) >= 36 exp(-48 kappa t)/kappa > 0.                          (P6)
```

Consequently the full ordinary mean is bounded and converges, while the ordinary full mixed variance diverges with order epsilon^-4 at every fixed positive time. The limiting mean generally has a strictly positive contribution beyond E_low. The normalized N=6-start ordinary-energy theorem does not give that contribution: here fresh first births continue to enter at ages of order epsilon squared.

No numerical value or sharp closed form for I(t) is asserted. Its value can depend on the original resolved/coherent source density. A variance conclusion is not a Fisher-coherence conclusion. There is no result here about apparatus resources or the unresolved pointwise normalized N=6-start variance.

## 2. Premises, imports and review provenance

The exact model, canonical cluster coordinates, common low dynamics and
fast operator are supplied by the following pinned parents. The new estimates
extend their controlled finite-source calculations to the evolving input and
integrate over every birth age.

- [Actual Cube Birth Energy On The Fast Time Scale Bounded Theorem Note 2026-09-24](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Local Compensation Common Field Record Limit Bounded Theorem Note 2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Bounded Block Diagonal Compensation Target Bounded Theorem Note 2026-09-24](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Sharp Actual Rotor Cube Energy Tail Bounded Theorem Note 2026-09-24](SHARP_ACTUAL_ROTOR_CUBE_ENERGY_TAIL_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Ordinary Microscopic Cube Energy After The Birth Layer Bounded Theorem Note 2026-09-24](ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md).
- [Recent Births Force Full Cube Energy Variance Bounded Theorem Note 2026-09-24](RECENT_BIRTHS_FORCE_FULL_CUBE_ENERGY_VARIANCE_BOUNDED_THEOREM_NOTE_2026-09-24.md).

The complete source identities and independent PRE/POST remain in the review
packet. That discovery packet also consulted the separate no-first-birth and
mixed-preparation notes at their stated frozen revisions. The weaker N=4
transient orders needed here are proved explicitly below; the whole-field
source Gram identity is also present in the recent-birth parent. No stronger
apparatus/coherence theorem from those parallel branches is required.

## 3. Exact full-ensemble decomposition and the low candidate

Let `W` count vacant A sites and `P_N=Pi_(N,0)`. On the fixed cube

```
H_(N,e)=delta epsilon^-4 h_(N,e),
h_(N,e)=W+epsilon T_S+epsilon^2 C_S,
T_S=-(F_S+F_S*),
C_S=P_N(M_(N,S)+D_N/C)P_N,       C=S(S+1),
M_(N,S)=P_N F_S*F_S P_N,
V_(N,e)(u)=exp[u(-iH_(N,e)-kappa Gamma_(N,S)/(2epsilon^2))].    (1)
```

The compensation is exactly zero on every W>=1 cube grade. Gamma is the sum of the original j_i*j_i, is diagonal in the physical word basis, and commutes with W. The physical Hamiltonian is Hermitian; V is a no-event contraction, not a Hermitian energy evolution.

Put

```
chi4,e(s)=V_(4,e)(s) U_(4,e) Omega,
v_(i,e)(t,s)=V_(6,e)(t-s) j_(i,S) chi4,e(s).
```

Every birth increases N by two. The N=4 density is `|chi4,e><chi4,e|` and the complete N=6 density is

```
rho6,e(t)=kappa epsilon^-2 sum_i integral_0^t
                         |v_(i,e)(t,s)><v_(i,e)(t,s)| ds.       (2)
```

This includes the actual first-birth rate and no-second-birth survival without a branch normalization. N=8 is terminal and H_(8,e)=0 exactly. Therefore for p=1,2,

```
Tr(H_e^p rho_e(t))
 = <chi4,e(t),H_(4,e)^p chi4,e(t)>
   +kappa epsilon^-2 sum_i integral_0^t
           <v_(i,e)(t,s),H_(6,e)^p v_(i,e)(t,s)> ds.            (3)
```

The supplied recent-birth PRE establishes this exact decomposition and a positive compact-age lower bound. The task here is the rest of the age integral; compact-age convergence by itself cannot supply it.

Define the rotor low Hamiltonian and survival semigroup in each sector by

```
H_rot,N=K D_N-delta Z_(N,infinity)*Z_(N,infinity)/2,
Z_(N,S)=Pi2 F_S Pi1 F_S P_N,
T_N(u)=exp[u(-i H_rot,N-kappa Gamma_(B,N)/2)],
Gamma_(B,N)=sum_j B_(j,N)*B_(j,N).
```

D_N is the nonnegative diagonal polynomial of the local-compensation note. These Hamiltonians are self-adjoint on their diagonal domains, since the remaining term is bounded. In N=4, `D_4=sum_e E_e^2`, `Gamma_(B,4)=48I`, giving u4 in (P4). Set

```
x_i(t,s)=T_6(t-s) B_i u4(s),
E_low(t)=<u4(t),H_rot,4 u4(t)>
       +kappa sum_i integral_0^t <x_i(t,s),H_rot,6 x_i(t,s)>ds. (4)
```

The terminal rotor block also has zero energy. Thus (4) is the energy of the full common low GKLS ensemble, not a survival-normalized energy. Its finiteness and the passage of microscopic low moments to (4) are justified below.

## 4. Weighted low motion and uniform birth-time source orders

Use `w=1+sum_e E_e^2`. For any fixed positive integer m, a unit link shift has a uniform bound after conjugation by w^m, with a constant depending on m but not S. Diagonal W, Gamma and D/C commute with w; D/C has a common operator bound on the spin box. The finite-hop factors and their adjoints, resolvent series, canonical polar series and no-event intertwiners consequently have uniform bounds in both ordinary norm and the w^m-conjugated norm for sufficiently small epsilon. For the present proof m=3 suffices; claiming one common analytic radius for all m is unnecessary.

Write P^H_(N,r) for Hermitian cluster projectors, E_(N,r) for no-event Riesz projectors, and V^H_N for the canonical all-cluster unitary. The exact intertwiner and low coordinate are

```
J_N=(sum_r E_(N,r) P^H_(N,r)) V^H_N,
a4,e(s)=Pi0 J_4^-1 chi4,e(s).
```

The parent contour argument uses `[Gamma,W]=0` to show

```
E_(N,r)-P^H_(N,r)=O(epsilon^3),
J_N-V^H_N=O(epsilon^3).                                    (5)
```

Every exact diagonal no-event block semigroup has a common all-forward-time norm bound. It is a block of `J_N^-1 V_(N,e)(u) J_N`, and the middle factor is a contraction. Thus nonnormal transient growth is controlled without a diagonalizability or spectral-gap assumption.

The exact low generator in physical time has the form

```
K_(N,e,0)=-i K D_N-i delta H4_(N,S)
          -kappa Gamma_(B,N,S)/2+epsilon^2 R_(N,e,0),
H4_(N,S)=-Z_(N,S)*Z_(N,S)/2
          -{M_(N,S),D_N/C}/2.                              (6)
```

The bounded remainder and bounded part have common w^m-conjugated norms. The interaction-picture Dyson series about `exp(-iu KD_N)`, which commutes with w^m, then gives

```
sup_(0<=s<=T) ||w^3 a4,e(s)|| <= C_T,
sup_(0<=s<=T) ||a4,e(s)-u4(s)|| -> 0.                        (7)
```

Initial weighted bounds follow from the finite-support Omega and the weighted canonical/intertwiner series. Strong convergence follows by the same bounded interaction-picture series: normalized spin shifts converge strongly, D/C tends strongly to zero after zero extension, finite products have common bounds, and the remainder vanishes. The limiting u4 has the same w^3 bound. This controls the evolving field; it does not reset it to Omega or assume that it stays in a fixed finite word span.

### The N=4 transient retains useful grades

Here the necessary initial high orders follow directly from the uniform
analytic projector expansion. Multiply the loss insertion by a scalar
parameter. At zero loss, every product of a high no-event projector with the
Hermitian low column vanishes. Every surviving coefficient contains a loss
insertion of degree two, preserving bare grade. Reaching bare row r from
grade zero also requires at least r degree-one hops. The grade-r coordinate
therefore starts at epsilon^(r+2); its full Riesz range is a uniformly bounded
graph over that coordinate. The common analytic radius controls the operator
remainder, uniformly in S. Exact block propagation then gives, uniformly on
`0<=s<=T`,

```
||a4,e,1(s)||=O(epsilon^3),
sum_(r>=2)||a4,e,r(s)||=O(epsilon^4).                        (8)
```

Its stronger exponential first-high decay is not needed here. Initial orders in (8) come from the first loss-containing contour terms: the order-three difference contains one T and one Gamma, and can change grade by only one. Higher grades cannot appear before order four. Exact block propagation preserves these ordinary bounds.

Moreover `J_4 Pi0=E_(4,0) U_(4,e)`, and the order-three part of `J_4 Pi0-U_(4,e)` lies in bare grade one. Since each E_(4,1) range is an O(epsilon) graph over Pi_(4,1), (8) gives an exact decomposition with uniform bounds

```
chi4,e(s)=U_(4,e) a4,e(s)+d1,e(s)+drem,e(s),
d1,e(s) in ran Pi_(4,1),
||d1,e(s)||<=C_T epsilon^3,
||drem,e(s)||<=C_T epsilon^4.                               (9)
```

This is stronger information than an ungraded O(epsilon^3) remainder, but does not require a weighted estimate for the propagated high transient.

### Apply the actual mark before discarding any grade

The finite-spin birth coefficients are bounded operators on the entire low sector,

```
B_(i,S)=j_(i,S) F_S P4,
R_(i,S)=(j_(i,S) F_S^2/2-F_S j_(i,S) F_S)P4
       =-F_(a,S) j_(i,S) F_(a,S) P4.                       (10)
```

The last identity holds with the spin weights: remote outward centers commute with the mark and with one another, shared forbidden endpoints kill both orders, and F_a^2=0. No opposite same-link shifts are exchanged.

In canonical Hermitian coordinates the mark on a canonical low vector has the operator expansion

```
Pi0 (V^H_6)* j_i U4 =epsilon B_(i,S)+O(epsilon^3),
Pi1 (V^H_6)* j_i U4 =epsilon^2 R_(i,S)+O(epsilon^4),
Pi2 (V^H_6)* j_i U4 =O(epsilon^5).                         (11)
```

These are uniform operator remainders at finite S, not the replacement of finite-spin coefficients by their rotor constants on moving high-flux inputs. The first two are the canonical coefficients and parity. For the third, the only possible cubic coefficient is

```
j F^3/6 - F j F^2/2 + F^2 j F/2.                          (12)
```

On P4 it vanishes: all remote factors cancel from `exp(-epsilon F) j exp(epsilon F) P4`, and the remaining expression with F_a is quadratic because F_a^2=0 and jP4=0. Minimal outward order and W parity make the next possible row coefficient order five. Compensation, normalization and backtracking cannot change the minimal cubic coefficient. This repeats the algebraic mechanism of PR9057 as an operator statement, so it applies to the evolved a4,e(s), without dividing by a possibly small individual mark probability.

Now j lowers W exactly by one. In particular `j d1,e(s)` belongs to the N=6 bare low grade and has norm O(epsilon^3). The high rows of `J_6^-1 Pi0` are O(epsilon), so this transient changes each high no-event source by only O(epsilon^4). The drem term also has that order. Replacing `(V^H_6)*` by `J_6^-1` in the canonical source costs O(epsilon^3) times its O(epsilon) norm, again O(epsilon^4).

It follows that the exact source coordinates

```
b_(i,e,r)(s)=Pi_r J_6^-1 j_(i,S) chi4,e(s)
```

obey, uniformly over every birth time `s in [0,T]`,

```
b_(i,e,0)(s)=epsilon B_(i,S) a4,e(s)+O(epsilon^3),
b_(i,e,1)(s)=epsilon^2 R_(i,S) a4,e(s)+O(epsilon^4),
b_(i,e,2)(s)=O(epsilon^4),
||j_(i,S) chi4,e(s)||=O(epsilon).                          (13)
```

The displayed high source orders are sufficient; no optimal second-high exponent is claimed. An O(epsilon^3) bound in either high source would not suffice for the present full integral. A persistent source of that norm could contribute order one to both the ordinary mean and epsilon^4 times the second moment after integration over an O(1) birth-time interval. This is the specific loss of information avoided by (9)–(13).

## 5. Smooth-source rotor bounds and the all-age finite-spin estimate

Set `r_(i,e)(s)=R_(i,S) a4,e(s)`, zero extended to the common physical N=6,W=1 rotor space. Finite-hop weighted bounds and (7) give

```
sup_(i,0<=s<=T) ||w^3 r_(i,e)(s)|| <= C_T,
r_(i,e)(s) -> r_i(s)=R_i u4(s) uniformly in s.              (14)
```

No rate is assumed for the second assertion. Strong convergence of R_(i,S), its common bound and compactness of the limiting u4 orbit suffice.

The exact physical Fourier space is `L2(T^5;C^96)`. Electric fields are affine integer-linear functions of the five chord fields and the finite charge label. Hence w^3 is equivalent to the order-six Fourier Sobolev weight. In particular its bound controls the sup norms of the Fourier input and its first two derivatives: by Cauchy–Schwarz, the relevant lattice sum is bounded by a multiple of `sum_(n in Z^5)(1+|n|^2)^(-4)<infinity`. This explicit estimate avoids assuming finite support for the evolved input.

The sharp-tail fiber bound, together with the local slow-cluster derivative argument of PR9057, therefore implies for any input r in this bounded w^3 family

```
||exp(tau L) r|| <= C_T (1+tau)^(-5/4),
||w exp(tau L) r|| <= C_T (1+tau)^(-1/4).                  (15)
```

The constants depend only on the common input bound and fixed model parameters. To spell out why the parent proof extends: near each of the finitely many deficient phases, the exact slow block A(h) has A(0)=A'(0)=0 and semigroup bound `C exp(-c|h|^2 tau)`. Its first two differentiated exponentials are bounded by

```
C tau |h| exp(-c|h|^2 tau),
C(tau+tau^2|h|^2) exp(-c|h|^2 tau).
```

Multiplication by the uniformly C^2 input adds only lower derivatives. The five-dimensional Gaussian integral gives squared zeroth-order norm O(tau^-5/2) and squared second-derivative norm O(tau^-1/2). Stable complementary blocks and phases away from the exceptional set have an exponential bound with differentiated resolvents. The finite partition and small-tau range have common bounds. Thus (15) holds for (14), not only for the parent's one fixed zero-field birth vector. It is not a uniform decay assertion over all normalizable inputs.

After removing the scalar phase from the exact N=6 first-high block, its fast-time generator is

```
A_e=L_S+epsilon^2 R_e,       L_S=-i delta G_(1,S)-kappa Gamma_(1,S)/2,
sup ||R_e||<infinity,
sup_(tau>=0)||exp(tau A_e)||<=C.                           (16)
```

The last bound follows from the exact contraction and bounded intertwiner; it does not assert strict spectral decay of the finite-spin block. Extend the block by zero outside its spin box. The usual normalized-spin coefficient estimate, including the boundary and zero extension, gives

```
||(A_e-L)z|| <= C epsilon^2 ||w z||.                       (17)
```

Indeed each elementary spin shift differs from a rotor shift by at most `C^-1` times the quadratic field weight. Products telescope using common weighted shift bounds, and `C^-1=K epsilon^2/delta`. The bounded epsilon^2 remainder is also bounded by the right side because w>=1. No moving boundary vector is assigned a rotor weight.

Duhamel with the exact bounded semigroup on the left and (15) on the right now gives, uniformly over all sources in (14),

```
||[exp(tau A_e)-exp(tau L)]r_(i,e)(s)||
 <= C_T epsilon^2 integral_0^tau (1+v)^(-1/4) dv
 <= C_T epsilon^2(1+tau)^(3/4).                            (18)
```

This is a proved growing-time comparison, not a substitution into compact-time convergence.

Use the comparison age `tau_*=epsilon^-1`. For `tau<=tau_*`,

```
||exp(tau A_e) r_(i,e)(s)||
 <= C_T[(1+tau)^(-5/4)+epsilon^2(1+tau)^(3/4)].              (19)
```

At tau_* both terms are O(epsilon^(5/4)). For every later age use the semigroup law and (16), obtaining the same O(epsilon^(5/4)) norm bound. Consequently for every fixed L0>=1,

```
integral_(L0)^(t/epsilon^2)
 ||exp(tau A_e) r_(i,e)(t-epsilon^2 tau)||^2 d tau
 <= C_T (1+L0)^(-3/2)+C_T epsilon^(1/2),                   (20)
```

uniformly for `0<=t<=T` wherever the integral is present. To check the powers, the squared comparison-error integral up to tau_* is

```
epsilon^4 integral_0^(epsilon^-1) (1+tau)^(3/2) d tau
 =O(epsilon^(3/2)),
```

and the interval from tau_* to at most T/epsilon^2 contributes at most

```
(T/epsilon^2) O(epsilon^(5/2))=O_T(epsilon^(1/2)).
```

The same estimates give a uniform bound for the full integral from zero. This is the required tightness over all microscopic birth ages. Applying the uniform source-family estimates separately at each s is legitimate; no semigroup law is claimed for the s-dependent source itself.

## 6. Integrating the first-high physical energy

Let y_(i,e,1)(t,s) denote the exact Hermitian first-high coordinate of v_(i,e)(t,s). Equation (13), exact blocked propagation, and (5) give

```
y_(i,e,1)(t,s)
 =epsilon^2 exp[-i delta (t-s)/epsilon^4]
       exp[((t-s)/epsilon^2) A_e] r_(i,e)(s)
   +e_(i,e)(t,s),
sup_(0<=s<=t<=T)||e_(i,e)(t,s)||<=C_T epsilon^4.            (21)
```

For the Hermitian/no-event coordinate replacement, the propagated physical vector has norm O(epsilon), by no-event contraction and (13). Its multiplication by the O(epsilon^3) intertwiner mismatch therefore has norm O(epsilon^4), also included in (21).

Changing variables `s=t-epsilon^2 tau`, define

```
I_e(t)=epsilon^-6 sum_i integral_0^t ||y_(i,e,1)(t,s)||^2 ds. (22)
```

The normalized error in (21) is O(epsilon^2) in fast-age coordinates. Its squared integral over at most T/epsilon^2 is O(epsilon^2). The principal part has bounded squared integral by (20), so Cauchy–Schwarz makes its cross term with the error O(epsilon). Thus this coordinate replacement does not leave an extra leading coefficient. A pointwise error estimate times the full interval, without this integrated norm control, would not establish that fact.

On every fixed compact tau interval, (14), uniform continuity of u4 and bounded-generator convergence imply

```
exp(tau A_e) r_(i,e)(t-epsilon^2 tau)
       -> exp(tau L) R_i u4(t),                            (23)
```

uniformly for t in [t0,T]. No quantitative convergence rate of a4,e to u4 is needed. The uniform tail bound (20), its rotor counterpart from (15), and then taking L0 to infinity prove

```
sup_(t0<=t<=T) |I_e(t)-I(t)| ->0.                          (24)
```

The actual Hermitian first-high energy block satisfies, uniformly in spin,

```
H_(6,e,1)=delta epsilon^-4[I+O(epsilon^2)],
H_(6,e,1)^2=delta^2 epsilon^-8[I+O(epsilon^2)].
```

Inserting (22)–(24) into the exact source integral (3) therefore gives

```
M_(1,N6,first-high)(t) -> kappa delta I(t),
epsilon^4 M_(2,N6,first-high)(t) -> kappa delta^2 I(t).     (25)
```

Hermitian spectral blocks are orthogonal, so energy moments have no cross terms between different bands. This use of physical spectral coordinates is essential; no-event eigenvalues are not being called energies.

## 7. All remaining bands and the ordinary low-energy limit

The N=6 second-high no-event source is O(epsilon^4) by (13). It remains so for every age by the common exact block bound. Its Hermitian coordinate also differs by only O(epsilon^4). Its contribution to the ordinary ensemble mean is consequently O(epsilon^2), and to epsilon^4 times the second moment also O(epsilon^2): in both cases the relevant bounded factor is a constant times `epsilon^-6 integral_0^t O(epsilon^8) ds`. No finite-spin decay rate for that band is needed.

For the N=6 low coordinate, put

```
x_(i,e)(t,s)=exp[(t-s)K_(6,e,0)] B_(i,S) a4,e(s).
```

Equation (13) and exact low-block propagation write its Hermitian low coordinate as

```
y_(i,e,0)(t,s)=epsilon x_(i,e)(t,s)+d_(i,e)(t,s),
||d_(i,e)(t,s)||<=C_T epsilon^3.                           (26)
```

The leading vector has a common w bound on the compact triangle `0<=s<=t<=T`, by (6)–(7) and the weighted interaction-picture series. It converges strongly, uniformly on that triangle, to x_i(t,s) in (4). Strong semigroup convergence first on fixed vectors and then a finite net of the compact limiting source orbit proves this uniformity.

The exact Hermitian low Hamiltonian has

```
H_(6,e,0)=K D_6+delta H4_(6,S)+epsilon^2 R_H,
||H_(6,e,0)||=O(epsilon^-2),
||H_(6,e,0) x_(i,e)(t,s)||<=C_T.                           (27)
```

Because H_(6,e,0) is self-adjoint, the cross term in the low mean is bounded using the energy action on the leading vector:

```
|<epsilon x,H d>|=|<epsilon H x,d>|=O(epsilon^4),
|<d,H d>|<=O(epsilon^-2) O(epsilon^6)=O(epsilon^4).          (28)
```

After multiplying by the birth intensity epsilon^-2 and integrating over a bounded physical interval, these errors vanish. This avoids needing a weighted norm bound on the whole microscopic high transient. It also avoids the weaker estimate that would multiply H's norm into a leading-vector cross term.

To pass the remaining electric expectation, use

```
|<x_e,D x_e>-<x,D x>|
 <= ||x_e-x|| (||D x_e||+||D x||),                          (29)
```

with the uniform weighted bound, and use bounded strong convergence for H4_(6,S). Uniformity on the compact triangle permits the s integral. This proves convergence of the low N=6 mean to the second term of (4).

Equations (26)–(27) also give `||H_(6,e,0)y_(i,e,0)||=O(epsilon)`: the remainder costs at most `O(epsilon^-2)O(epsilon^3)`. Hence the complete low N=6 second moment is O(1) after its epsilon^-2 source prefactor, and disappears in (P2).

The same weighted argument for the N=4 no-first-birth block gives its mean limit `<u4,H_rot,4 u4>`. Its first-high norm is O(epsilon^3) and aggregate higher norm is O(epsilon^4), uniformly on bounded times. Thus its high mean is O(epsilon^2), and its total second moment is O(epsilon^-2). The sharper known N=4 coefficient is compatible with this estimate but is unnecessary here. Its contribution to epsilon^4 times the second moment vanishes. The exact N=8 energy moments remain zero.

Combining these estimates with (25) proves (P1) and (P2). Uniform boundedness of the ordinary mean gives `epsilon^4 [Tr(H_e rho_e)]^2 ->0`, proving (P3). There is no need to discard the terminal contribution to a centered square: the variance is obtained from the exact full first and second moments, including their common trace-one ensemble.

## 8. Positivity, precision and limits

At rotor order, the source maps satisfy `sum_i R_i*R_i=72I` for either complete original instrument. This whole-field identity follows from the local charge/translation paths proved in the recent-birth parent: two distinct charge-labelled unitary translations give each B source; the plus R paths add with amplitude -2, the minus paths give two orthogonal amplitudes -1, and the two signs are initially orthogonal. Thus the per-edge R Gram constants are 4I, 2I and 6I for plus, minus and coherent marks, respectively. Summing twelve edges gives 72I on arbitrary initial fields. Finite-spin source norms are not assigned that constant before the limit.

For every rotor vector z,

```
d/dtau ||exp(tau L)z||^2
 =-kappa <exp(tau L)z,Gamma_1 exp(tau L)z>
 >=-2kappa ||exp(tau L)z||^2.
```

Consequently the integrand summed over i is at least
`72 exp(-48 kappa t) exp(-2 kappa tau)`. Its integral gives (P6), agreeing with the explicitly supplied prior lower bound `36 delta^2 exp(-48 kappa t)` on epsilon^4 variance. The matching upper control and full integral limit are the additional conclusions here. The upper bound from (15) and compact source orbit also gives continuity and a common upper bound for I on [0,T]. These together make the order statement in (P3) uniform on any fixed [t0,T].

The order of limits is fixed: epsilon tends to zero along the joint integer-spin sequence, while physical parameters and [t0,T] are fixed. The age comparison is explicitly proved through tau=epsilon^-1 and then extended by exact bounded semigroups; no approximation is extrapolated to tau=t/epsilon^2. Constants may depend on T and the fixed positive parameters. Neither kappa tending to zero nor T tending to infinity is covered.

The full-ensemble limit need not be uniform down to t=0. At zero no first birth has occurred, while I(0)>0 in the limiting formula. This is an initial continuous-injection layer, not a contradiction. No moving observation-time scale or further expansion of this layer is claimed here.

All source sums retain the actual marked vectors. For a coherent mark, `R_i=R_++R_-` and `B_i=B_++B_-` remain inside each propagated vector. Equal losses do not authorize replacing that vector by a resolved mixture. Nor is the evolved u4(t) replaced by its initial zero-field value.

H need not be nonnegative, so the positive additional first-high energy cannot be inferred by dropping arbitrary signed low contributions. The proof computes the low mean separately. Conversely the variance result concerns a mixed density; it does not imply a matching energetic Fisher lower bound, identify stored heat or work, or establish an external supply cost. The canonical preparation, local compensation, original instrument, physical clock and joint scaling remain supplied premises. Moving high-flux preparations, growing support without the stated weighted bound, a changed graph, or a different microscopic instrument require new estimates.

## 9. Trace-norm rare matter/field density

For this section put x_i,e(s,t)=sqrt(kappa) epsilon^-1 v_(i,e)(t,s), using the raw-mark vector in (2), and identify U6,e^H with the canonical unitary V6^H above. Let K be the fixed bare-grade-one physical rotor space and let U6,e^H be the complete Hermitian canonical cluster unitary. For `0<=tau<=t/epsilon²`, define

    f_i,e,t(tau) = [exp(i delta tau/epsilon²)/(sqrt(kappa) epsilon)]
                   Pi1 (U6,e^H)* x_i,e(t-epsilon² tau,t),

and set it to zero for larger tau. The finite-spin coordinate is extended by zero in K. The exponential is a scalar of modulus one; its precise phase has no effect on a rank-one density. Let

    f_i,t(tau) = exp(tau L) R_i u4(t),  tau>=0.

The vector-profile proof above gives, uniformly for `t in [t0,T]`:

1. On every fixed `0<=tau<=L0`, f_i,e,t tends strongly and uniformly to f_i,t. This uses compact-age convergence of the exact block, the strong uniform low-source limit, and continuity of u4. It requires no prescribed rate of the low-source convergence.
2. The first-high profile has the uniform tail bound

       integral_L0^infinity ||f_i,e,t(tau)||² d tau
          <= C(1+L0)^(-3/2) + C_T epsilon^(1/2) + o(1).

   Here the additional coordinate/source error divided by epsilon is O(epsilon²); its square integrates over at most T/epsilon² to O(epsilon²). The main-profile tail is the young/old split above. The limiting profile has the same integrable algebraic tail without the epsilon term.

Using `||f-g||² <= 2||f||²+2||g||²` in the tails and compact convergence on `[0,L0]` proves

    sum_i ||f_i,e,t-f_i,t||²_(L²([0,infinity);K)) -> 0.       (D1)

This statement concerns the vectors, not just their squared norms. The finitely many original marks can be collected in one direct-sum L² space.

For Hilbert vectors a,b,

    || |a><a| - |b><b| ||_1 <= (||a||+||b||) ||a-b||,

by writing the difference as `|a-b><a|+|b><a-b|`. Integrate this estimate, then apply Cauchy–Schwarz in age and in the finite mark index. Equation (D1) and the common L² bounds give convergence in trace norm of the integrated densities.

The change of variable `ds=epsilon² d tau` and source amplitude `sqrt(kappa) epsilon` give exactly

    epsilon^-4 rho6,high^coord(t)
        = kappa sum_i integral_0^infinity |f_i,e,t(tau)><f_i,e,t(tau)| d tau
        -> Sigma(t),

    Sigma(t) = kappa sum_i integral_0^infinity
                         |f_i,t(tau)><f_i,t(tau)| d tau.   (D2)

This proves the trace-norm rare-density statement under the same premises. Sigma is a positive trace-class operator and `Tr Sigma=kappa I(t)`. No low/high off-diagonal block limit is asserted. Coherent interference inside an original mark is retained before each rank-one operator is formed.

Every bounded observable on this common matter/field fiber has the corresponding leading rare-population coefficient. That conclusion does not by itself pass arbitrary unbounded observables. The energy conclusions additionally use the separately proved scaled first-high Hamiltonian limit and the low/other-band estimates from sections 6–7. Sigma is an unnormalized coefficient of a vanishing sector probability, not a replacement normalized state for the full ensemble.

## 10. Frozen-source balance

Fix physical t and set `A(t)=sum_i |r_i(t)><r_i(t)|`. It is positive, finite rank and trace class. The operator L is bounded on K, because the rotor shifts, finite matter matrices and loss are bounded. Define

    Phi(tau)=exp(tau L) A(t) exp(tau L*).

The source-family estimate gives `||Phi(tau)||_1=sum_i ||f_i,t(tau)||² <= C(1+tau)^(-5/2)`. Consequently the integral defining Sigma is a convergent trace-class Bochner integral. Boundedness of L gives the trace-norm derivative

    Phi'(tau)=L Phi(tau)+Phi(tau)L*,
    ||Phi'(tau)||_1 <= 2||L|| ||Phi(tau)||_1.

Integrating first over a finite age interval and then taking its endpoint to infinity is justified in trace norm. The upper endpoint vanishes. Therefore

    L Sigma(t)+Sigma(t)L* = -kappa A(t).                    (D3)

This proves the frozen-source identity. No existence of a bounded inverse for the infinite-dimensional Lyapunov map is assumed; no uniqueness claim for arbitrary sources is made.

Trace cyclicity is legitimate for a bounded operator times a trace-class operator. Since `L+L*=-kappa Gamma1` and `Gamma1=2 Pbright`,

    -kappa Tr(Gamma1 Sigma) = -kappa Tr A(t),
    Tr A(t) = <u4(t),sum_i R_i*R_i u4(t)> = 72 exp(-48 kappa t).

Cancel the fixed positive kappa to obtain

    Tr(Gamma1 Sigma(t)) = 72 exp(-48 kappa t),
    Tr(Pbright Sigma(t)) = 36 exp(-48 kappa t).              (D4)

The positive dark contribution gives `Tr Sigma>=36 exp(-48 kappa t)`, equivalent to the lower bound in section 8 on I. Equations (D3)–(D4) preserve all source factors and signs. The ordinary mean excess is delta Tr Sigma; the scaled variance coefficient is delta² Tr Sigma.

These are identities in the frozen-source age problem. They do not exchange an epsilon limit with differentiation in physical t. They do not identify physical bath energy, work, heat, initial apparatus coherence or a Hamiltonian-selection principle. No full-output QFI conclusion follows from the mixed-state variance.

## 11. Evidence and publication scope

The primary runner embeds the author's previously pinned word helpers and
reruns the sealed source-algebra and rotating-input toy controls with disclosed
reuse. It checks 1,260 edge/mark/input cases, including moving finite-spin
boundary words. A changed cubic coefficient is detected in 1,239 cases.
The rotor coefficient residuals are zero in the implemented integer arithmetic;
the finite-spin residuals are floating-point corroboration, not interval or
uniform analytic certificates.

The second control is a separate ten-state GKLS cascade, with an evolving
initial doublet, a low doublet, a four-state fast block and a terminal doublet.
It retains the relevant coherent first jump and solves exact closed diagonal
density equations. Its fast block has a strict exponential gap, whereas the
cube proof uses its five-dimensional algebraic tail. At t=1.1 and epsilon=.01,
the toy mean is 2.877541 against 2.876752, the scaled variance is 3.265279
against 3.264409, and the scaled high-density trace distance is .000937434.
These are toy results, not a finite-spin cube simulation or an independent
numerical reconstruction.

The independent PRE used separately written exact physical-word/Riesz-series
controls for rotor and S=1 sources, retained a blocked boundary source, and
tested a separate scalar continuous-injection model. Its POST read the full
author results and separately checked rational dark/bright signs and factors.
The source-factor and current-sign mutations fail that distinct balance check;
a zero dark/bright coupling shows why an integrable source tail is a necessary
hypothesis of that calculation. Full execution records, limits and provenance
are preserved. The publication primary is not an additional independent check.

No initial physical-time layer, convergence of physical-time power, external
energy supply, mixed Fisher bound, physical selector or theory-of-everything
completion follows here. In particular a frozen-age Sylvester balance is not
an apparatus energy balance. The separately normalized N=6-start pointwise
variance problem remains open.

```bash
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/full_original_cube_ensemble_energy_and_rare_density_2026_09_24.py
```

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: full_original_cube_ensemble_energy_and_rare_matter_field_density_bounded_theorem_note_2026-09-24
target_blocker_text: "A recent-birth lower bound does not determine the full ordinary mean or the complete variance coefficient."
source_of_blocker_text: frontier_question
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Determine the initial energy layer, actual energy supply and physically selected dynamics without discarding the original instrument."
conditional_surface_status: "Fixed cube, supplied compensation and canonical preparation, original complete instrument, fixed positive parameters, and joint spin scaling."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Uniform evolved-source grading, smooth rotor decay and a proved all-age finite-spin comparison determine both full moments and a trace-class rare density."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Landing-review boundary and No-Go Discipline Gate

N1: supplied compensated cube, original complete instrument and fixed positive observation intervals. N2: moving high-flux inputs, unbounded times and changed graphs remain outside the result. N3: preparation, compensation, dynamics and scaling are supplied. N4: the sharp-tail and weighted parent estimates retain their input domains. N5: primitive, finite-cascade and frozen-source controls corroborate the analytic all-age proof. N6: no apparatus Fisher or physical-selection conclusion is inferred. N7: fourth-order source errors and the weighted evolved input are essential for full age integration. N8: the growing-time comparison is proved to epsilon^-1 and then continued with exact bounded semigroups; the frozen-age balance is not a physical-time energy supply identity.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Historical author reports remain provenance only. Complete originals remain recoverable at PR #9109 frozen head. No audit verdict or retained grade is applied.
