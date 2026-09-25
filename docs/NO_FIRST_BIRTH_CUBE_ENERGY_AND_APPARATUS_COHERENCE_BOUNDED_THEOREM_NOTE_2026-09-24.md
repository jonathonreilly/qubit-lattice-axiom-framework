---
claim_id: no_first_birth_cube_energy_and_apparatus_coherence_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: 'Original compensated cube from its canonical N=4 input: fixed-positive-time no-first-birth survival
  and physical energy variance, and necessary finite initial apparatus Fisher coherence and bandwidth for o(epsilon^3)
  quantum-output approximation under additive energy conservation. A supplied one-block state-preparation relaxation
  attains the leading resource coefficients. No N=6-start pointwise variance result, full-process sufficiency, physical
  selector or new axiom.'
upstream_dependencies:
- actual_cube_birth_apparatus_coherence_and_energy_range_bounded_theorem_note_2026-09-24
- actual_cube_birth_energy_on_the_fast_time_scale_bounded_theorem_note_2026-09-24
- bounded_block_diagonal_compensation_target_bounded_theorem_note_2026-09-24
- local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
- minimal_axioms
runner: scripts/no_first_birth_cube_energy_and_apparatus_coherence_2026_09_24.py
---

# Energy and apparatus coherence before the first cube birth

**Type:** bounded_theorem

**Status:** conditional mathematical result; unaudited.

Conditional bounded theorem; selective independent reconstruction,
not a retained audit verdict. The quantum model, local compensation, time,
preparation, scaling and original formation instrument remain supplied.

The original continuous ensemble contains an N=4 sector in which no first
birth has occurred. Its probability stays nonzero at every fixed finite time.
The sector approaches the common low dynamics in norm, but a small coherent
first-high component gives a divergent physical energy variance. This supplies
a necessary apparatus resource bound for a precise quantum-state approximation
of the original continuous process at one observation time.

For fixed positive delta,K,kappa and epsilon^2 S(S+1)=delta/K, uniformly on
every fixed [t0,T] with t0>0,

    p4,epsilon(t) -> q(t)=exp(-48 kappa t),
    epsilon^2 Var_H(phi4,epsilon(t)) -> 48 kappa^2,
    epsilon^2 p4,epsilon(t) F_H(phi4,epsilon(t))
          ->192 kappa^2 exp(-48 kappa t).                    (P1)

Here phi4 is the normalized N=4 no-first-birth ket and energetic SLD Fisher
information obeys F_H(pure)=4 Var_H. The full original N=4-start ensemble
therefore has liminf epsilon^2 variance at least 48 kappa^2 q(t); this is a
lower bound, not a full-ensemble asymptotic.

For a finite initially independent apparatus including all phase references,
exact additive-energy-conserving processing and covariant readout, unhalved
trace error eta=o(epsilon^3) for the original output's N=4 block forces

    liminf epsilon^2 F_R >=192 kappa^2 exp(-48 kappa t),
    liminf epsilon^4 B_coh,R >=delta.                        (P2)

Whole-output quantum approximation implies this block approximation. Merely
matching classical record probabilities does not. A supplied preloaded-state
SWAP attains these leading coefficients for the one-block relaxation using
one O(epsilon^4) error sequence and bounded mean energy. It does not construct
the full process, its other number sectors, or an apparatus working on every
input. An interacting conserved total is a different premise from additive
energy conservation. No stationary-apparatus or formation impossibility is
claimed.

The source construction is the [actual fast-birth parent](ACTUAL_CUBE_BIRTH_ENERGY_ON_THE_FAST_TIME_SCALE_BOUNDED_THEOREM_NOTE_2026-09-24.md),
the [bounded compensation target](BOUNDED_BLOCK_DIAGONAL_COMPENSATION_TARGET_BOUNDED_THEOREM_NOTE_2026-09-24.md),
and the [common field/record limit](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md).
The finite resource machinery is restated from the provisional
[actual-birth apparatus parent](ACTUAL_CUBE_BIRTH_APPARATUS_COHERENCE_AND_ENERGY_RANGE_BOUNDED_THEOREM_NOTE_2026-09-24.md),
PR9079 at e846ee9d4133f65d3778fa4dc36524a9ada6db6b, on which this PR is stacked.
The weighted method and included author matrix definitions were also developed
in [PR9057 at its pinned revision](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/c234d47c9d99b7fd5590957ec08d9083877d25e6/docs/ORDINARY_MICROSCOPIC_CUBE_ENERGY_AFTER_THE_BIRTH_LAYER_BOUNDED_THEOREM_NOTE_2026-09-24.md).
Its N=6 tail theorem is not required here: the needed N=4 weighted construction
and first-high damping are derived below. No supplied readings from other
open dynamics-clause PRs are adopted or used.

The root sealed its proof, controls and limited-attainment supplement before
the independent PRE was disclosed. The following exposition incorporates the
independent reconstruction's Hermitian-coordinate proof and detailed weighted
argument, with that contribution explicitly attributed. The primary controls
remain root-authored; their reuse is not independent evidence.

## 1. Domain, sources, and the exact N=4 block

The cube has `A={0,3,5,6}`, `B={1,2,4,7}` and its twelve edges. For the word
proof we orient every edge from A to B; reversing an original link orientation
just reverses its electric coordinate. The record values are `0,+1,-1`.
The physical Gauss law is `div E=q-1_A`. The input word `Omega` has one positive
record at every A site, no B records, and zero electric fields. Integer spin
`S>=1` is used, and

```
C=S(S+1),             epsilon^2 C=delta/K,
H=delta epsilon^-4 h, h=W+epsilon T+epsilon^2 C_S,
T=-(F+F*),           L_j=sqrt(kappa) epsilon^-1 j,
delta,K,kappa>0 fixed, epsilon -> 0.                         (1)
```

`C_S` is the supplied local compensation, not the scalar `C`. The choice
lambda=0, the compensation, quantum spaces, preparation and instruments are
supplied premises. Their physical selection is not derived. All imported
scientific statements retain conditional/unaudited status.

`W` counts vacant A sites. `P=Pi0` is its zero grade. The actual input is the
canonical **Hermitian** low-band vector `psi_epsilon=U_epsilon Omega` in N=4.
The Hamiltonian preserves N. Every original birth raises N by two, so it is
impossible for a jumped path to return to N=4. Put `Gamma=sum_j j*j`. The
resolved and coherent instruments have the same Gamma because their two sign
outputs on each edge are orthogonal. The exact original ensemble therefore
has

```
rho4(t) = P_(N=4) rho(t) P_(N=4) = |chi(t)><chi(t)|,
chi(t)  = exp[t(-iH-kappa Gamma/(2epsilon^2))] U_epsilon Omega.
p4(t)   = ||chi(t)||^2.                                      (2)
```

This is a sector of the original continuous law, not a replacement mark or an
effective jump channel. There is no first-event time to integrate in (2).
`Gamma P=0`; Gamma commutes with W. The original ensemble is block diagonal
in N=4,6,8, and H preserves these sectors. The N=8 Hamiltonian is zero, as in
the supplied model, but that fact is not needed for the N=4 lower bounds.

The earlier fast-time and ordinary-energy investigations mostly analyze actual N=6 birth
outputs. They do not themselves assert (P1). What is reused here is their
graded contour construction and weighted low-block method. The N=4 hypotheses
are checked next. No compact-fast-time statement is evaluated at a growing
fast time.

## 2. Cube identities specific to N=4

The total charge is four. In N=4 every occupied site therefore has positive
charge. At W=0 the occupied set is exactly A. On the rotor low space, one
outward hop along an edge `(a,b)` leaves vacancy a, occupies b, and decreases
that edge field by one. The resulting charge word identifies `(a,b)` uniquely,
and its electric word then identifies the input. Thus the twelve one-hop
isometries have mutually orthogonal ranges, including for superpositions of
arbitrary physical rotor low words. Consequently

```
F_infinity* F_infinity = 12 I.                              (3)
```

Each such one-hop word has one vacant A site, and exactly two of that site's
neighbors remain empty B sites. At rotor order each empty edge has two unit
birth weights. Thus, on the whole low rotor space, not merely at Omega,

```
Gamma_1,infinity F_infinity = 4 F_infinity,
Gamma_B,infinity = F_infinity* Gamma_1,infinity F_infinity = 48 I,
||Gamma_1,infinity F_infinity u||^2 = 192 ||u||^2.              (4)
```

At Omega these coefficients also hold exactly at every finite spin: the hop
is `0 -> -1`, its normalized weight is one, and all birth-enabled links in
the resulting word still have field zero. This is an exact word statement,
not a finite-S substitute for the operator rotor limit.

There is a separate **global finite-spin lower bound on W=1**. An arbitrary
N=4,W=1 charge word has one vacant A and one occupied B. It has either two
or three empty edges incident to that vacant A. On an empty edge with field m,
the two original birth weights have squared sum

```
g_S(m) = [1-m(m+1)/C]+[1-m(m-1)/C]
       = 2-2m^2/C >= 2/(S+1),             |m|<=S.             (5)
```

Boundary-forbidden moves have zero weight in this formula. In particular no
rotor weight is silently assigned at a spin boundary. Hence, on the entire
physical N=4,W=1 space,

```
Gamma_1,S >= 4/(S+1) I.                                    (6)
```

This lower bound uses both original sign contributions. A single sign alone
can have zero boundary loss. It would not justify (6). No analogous uniform
fast-decay assertion is made for every higher grade: W=4 has no empty birth
edge and its bare Gamma is zero.

The local compensation gate vanishes on all W>=1 cube sectors. With exactly
one A vacancy, every other A term is killed by its gate, while the term at the
vacant A has zero bracket. With more vacancies every relevant gate is zero.
Thus `C_r=0` for `r>=1`, and on P

```
C_0=M_S+Q_S,  M_S=P F_S*F_S P,  Q_S=D/C.
```

Gauss law at W=0 makes the sum of the linear electric terms zero, giving
`D=sum_e E_e^2` in this N=4 sector. In fact its one-hop outputs are orthogonal
at finite spin too, so `M_S=12 I-Q_S` and `C_0=12 I` here. Uniform boundedness
of T, C_S, Gamma and their adjoints follows from the fixed finite graph and
normalized shifts. W has the fixed integer grades 0 through 4. These are the
needed N=4 graded hypotheses.

## 3. Hermitian energy bands versus no-event bands

Set `gamma=kappa/(2delta)` and

```
h_eff = W+epsilon T+epsilon^2(C_S-i gamma Gamma).
```

Let `P_r^H` and `P_r^eff` be the exact Hermitian and no-event Riesz projectors
near W grade r. Fixed disjoint contours about the five integer grades give
uniform analytic expansions. Their difference begins at order epsilon cubed:
the order-epsilon-squared difference integrates a grade-diagonal Gamma between
two resolvents, hence only double poles, with zero contour integral. Therefore

```
S_e = sum_r P_r^eff P_r^H = I+O(epsilon^3),
J_e = S_e V_e,                                               (7)
```

where `V_e` is the canonical unitary from W grades to Hermitian bands and its
low column is U. `J_e` exactly block diagonalizes the no-event generator.
Every exact transformed band propagator has a common all-time bound: it is
a block of `J_e^-1 exp[t(-iH-kappa Gamma/(2epsilon^2))] J_e`, and the middle
propagator is a contraction. These ordinary norms are uniform in S and small
epsilon. W parity makes diagonal band expansions even in epsilon.

The order and sign of the low-to-first-high mismatch can be obtained without
identifying a non-Hermitian eigenvalue with energy. In Hermitian coordinates,
the leading low column of V is `P+epsilon F_S P`. Since `Gamma P=0`,

```
(V_e* Gamma V_e)_10 = epsilon Gamma_1,S F_S P+O(epsilon^3).
```

The off-diagonal no-event block is consequently
`-i gamma epsilon^3 Gamma_1,S F_S+O(epsilon^5)`. Its low invariant graph Y
satisfies the block Riccati equation. The first-high/low gap is one at
epsilon=0, so its leading equation is `h_eff,10+Y_10=0`. It follows that

```
(V_e* S_e V_e)_10 = i gamma epsilon^3 Gamma_1,S F_S P
                       +O(epsilon^5),
(V_e* S_e V_e)_(r0) = O(epsilon^4),             r>=2.          (8)
```

The first remainder is odd by W parity. For the second assertion the first
projector difference at order epsilon cubed contains one T and one Gamma,
so changes grade by only one; grade two cannot occur before order four.
These expansions do not use the special N=6 second-birth cancellation.

Let `a_r(t)=Pi_r J_e^-1 chi(t)` be the exact no-event coordinates. Because the
initial vector belongs exactly to the Hermitian low band, (7)-(8) give

```
a_0(0)=Omega+O(epsilon^3),
a_1(0)=-i gamma epsilon^3 Gamma_1,S F_S Omega+O(epsilon^5),
sum_(r>=2)||a_r(0)||=O(epsilon^4).                            (9)
```

All initial remainders are uniform in spin. The high initial coordinates
propagate separately. In particular the first-high physical-time generator is

```
K_1 = -i delta epsilon^-4 I
      +epsilon^-2[-i delta G_1,S-kappa Gamma_1,S/2]+R_1,
G_1,S = Pi1(F_S F_S*-F_S* F_S)Pi1,     ||R_1||<=constant.      (10)
```

G_1,S is self-adjoint; the two virtual denominators have opposite signs.
The logarithmic-norm estimate using (6) gives

```
||exp(t K_1)|| <= exp[(-2kappa/(epsilon^2(S+1))+constant)t]
               <= exp(-c t/epsilon)                         (11)
```

for all sufficiently small epsilon on the stated joint sequence and some
`c>0`. Here `epsilon(S+1)->sqrt(delta/K)`. Thus the entire first-high initial
transient is `O(epsilon^3 exp(-ct/epsilon))`. This proves what is needed at
fixed physical time directly; no growing tau is substituted into a
compact-tau limit. For r>=2 the common contraction-similarity bound and (9)
suffice to keep `a_r=O(epsilon^4)` at all later times.

Writing `y=V_e* chi`, (8)-(11) imply, uniformly on fixed `[t0,T]`,

```
y_1(t)=i gamma epsilon^3 Gamma_1,S F_S a_0(t)
            +O(epsilon^5)+O(epsilon^3 exp(-ct/epsilon)),
sum_(r>=2)||y_r(t)||=O(epsilon^4),
||y_0(t)-a_0(t)||=O(epsilon^3).                              (12)
```

Only the leading band-one mismatch is used below. Treating chi as lying in
the **Hermitian** low band after its initial transient would erase precisely
the term in (12).

## 4. Weighted N=4 low motion and its limit

The N=4 low generator follows the finite-grade Schur/canonical calculation: the fourth-order paths visit at most grade two.
The no-event loss at this order is obtained by its grade-one insertion.
Using `C_0=M+Q`, `C_1=0`, and `Z=Pi2 F Pi1 F P`, one obtains

```
K_0 = -i K D-i delta H4_S-kappa Gamma_B,S/2+epsilon^2 R_0,
H4_S = -Z_S*Z_S/2-(M_S Q_S+Q_S M_S)/2,
Gamma_B,S=P F_S* Gamma_1,S F_S P.                            (13)
```

The corresponding exact Hermitian low Hamiltonian is

```
H_H,0 = K D+delta H4_S+epsilon^2 R_H,
||H_H,0||=O(epsilon^-2).                                    (14)
```

The fourth-order imaginary term in (13) is `-kappa Gamma_B,S/2` in physical
time, not a new dissipator placed into the model. The similarity (7) agrees
with the canonical Hermitian coordinates sufficiently far to leave these
displayed coefficients unchanged. Even parity gives the indicated next
physical-time remainder. More explicitly, the Hermitian-coordinate diagonal
loss is `(V_e* Gamma V_e)_00=epsilon^2 Gamma_B,S+O(epsilon^4)` because
`Gamma P=0`. Its multiplication by `-i gamma epsilon^2` supplies precisely
the order-four term. Further low/high elimination involves two off-diagonal
terms of order epsilon cubed, so it first changes the low block at order six.

To control actual energies, use `w=1+sum E_e^2`, not ordinary density
convergence alone. A unit change of one integer field gives a weight ratio
at most three: `1+(m+/-1)^2 <= 3(1+m^2)`, with the other field squares carried
along. All finite sums of normalized shifts and adjoint shifts therefore have
uniform bounds after w conjugation. W, its grade projections, Gamma and Q_S
are diagonal and commute with w; `Q_S=D/C` is uniformly bounded on the spin box.
Finite products preserve these bounds. The resolvent Neumann series, canonical
polar series (including all adjoint factors), S_e, its inverse, and their
remainders thus converge in both the ordinary and w-conjugated norms at a
common small epsilon. In particular `R_0,R_H` and their w conjugates are
uniformly bounded. This verifies the weighted machinery specifically on N=4.

The canonical input is a fixed finite-support word, so
`sup ||w a_0(0)||<infinity`. Write `K_0=-iKD+B_e`; both `B_e` and `w B_e w^-1`
are uniformly bounded. The interaction-picture series about `exp(-itKD)`,
which commutes with w, proves

```
sup_(0<=t<=T)||w a_0(t)|| <= C_T.                            (15)
```

Embed the spin boxes in the common physical rotor low space. Outside each
box extend the generator by `-iKD` and B_e by zero. This does not alter a
finite-spin trajectory. The normalized shifts and adjoints converge strongly,
`Q_S->0` strongly, and all their finite products have common bounds.
The remainder `epsilon^2 R_0` tends to zero in norm. Termwise strong
convergence of the bounded interaction-picture series, with a common tail
bound, then gives, uniformly on every compact physical-time interval,

```
a_0(t) -> u(t)=exp(-24 kappa t) exp(-it H_rot,4) Omega,
H_rot,4=K sum E_e^2-(delta/2) Z_infinity* Z_infinity.          (16)
```

The limiting loss is scalar by (4), and H_rot,4 is self-adjoint on the
diagonal D domain by bounded perturbation. No free-field substitution after
a birth is being made. The familiar plaquette expression for this N=4
Hamiltonian is available in the pinned local parent, but its scalar/plaquette
coefficients are unnecessary for the present leading resource bound.

It follows that `p4(t)->||u(t)||^2=q(t)` uniformly on `[0,T]`, and, by bounded
strong convergence applied to the compact path u,

```
||Gamma_1,S F_S a_0(t)||^2 -> 192 q(t).                       (17)
```

Equation (15) also gives `||H_H,0 a_0(t)||=O(1)`. Replacing a_0 by the physical
Hermitian coordinate y_0 costs only
`O(epsilon^-2) O(epsilon^3)=O(epsilon)` in the **energy vector norm**, by
(12) and (14). Hence `||H_H,0 y_0(t)||=O(1)`. This is stronger than passing
an expectation through trace-norm convergence and is the required low-energy
domain estimate for the second moment.

## 5. Physical energy variance and the full-ensemble lower bound

From (12) and (17), uniformly on `[t0,T]`,

```
epsilon^-6 ||y_1(t)||^2 -> (48 kappa^2/delta^2) q(t).        (18)
```

Hermitian spectral bands are orthogonal. Their physical Hamiltonian blocks
satisfy

```
H_H,r = delta epsilon^-4 [r I+O(epsilon^2)],       r>=1.
```

The low contribution to `||H chi||^2` is O(1). The r>=2 contribution is O(1),
since its vector norm is O(epsilon^4). The band-one contribution, using (18),
therefore yields

```
epsilon^2 <chi,H^2 chi> -> 48 kappa^2 q(t).                 (19)
```

The band-one mean is O(epsilon^2), the other high-band means are O(epsilon^4),
and the low mean is O(1). Thus `<chi,H chi>=O(1)`. Since p4 stays uniformly
away from zero on `[0,T]`, dividing by p4 and subtracting the squared bounded
normalized mean proves the variance statement in (P1). The input's own Fisher
information is bounded as well: `D Omega=0` and (14) give

```
F_in=F_H(U_e Omega)=4 Var_H(U_e Omega)=O(1).                  (20)
```

For the original ensemble, block additivity of Fisher information under the
H-invariant N decomposition gives

```
F_H(rho(t)) = sum_N p_N F_H(rho_N(t)) >= p4 F_H(phi4).
```

The same sector gives `Var_H(rho(t))>=p4 Var_H(phi4)` by the law of total
variance. Consequently this note supplies lower bounds

```
liminf epsilon^2 F_H(rho(t)) >= 192 kappa^2 q(t),
liminf epsilon^2 Var_H(rho(t)) >= 48 kappa^2 q(t).             (21)
```

Neither is an equality for the full ensemble in this note. Nothing here
computes the N=6 contribution, its conditional pointwise variance, a total
ensemble upper bound, or a larger possible resource divergence. The
ordinary-energy parent's full-ensemble statement starts after an actual birth;
it is not silently re-labelled as a variance theorem for the present
pre-first-birth ensemble.

## 6. Finite apparatus Fisher bound, including approximation

At the fixed known observation time let R include every phase reference,
clock resource and auxiliary state used by the implementation. Its initial
state is `sigma_R`, independent of `psi_epsilon`; it may be mixed and its
finite dimension/Hamiltonian may depend on epsilon. The processing unitary V
obeys exact `[V,H+H_R]=0`. Subsequent readout uses zero-energy flags or other
covariant operations and discarding. Any omitted coherent controller would
fall outside these hypotheses. The output comparison is the quantum density
matrix or its selected subnormalized N=4 block, not a scalar record law.

For finite dimensions define

```
F_H(rho)=2 sum_(a,b;lambda_a+lambda_b>0)
              ((lambda_a-lambda_b)^2/(lambda_a+lambda_b)) |H_ab|^2.
```

The SLD is the solution of `-i[H,rho]=(L rho+rho L)/2` on the support pairs.
It has zero mean, and `F=Tr rho L^2`. On a product its SLD is the sum of the
factor SLDs, proving additivity. For a pure state the displayed formula is
four times variance; generally it is at most four times variance. Exact
conservation makes processing covariant for the joint time-translation
parameter. Fisher monotonicity, or SLD Cauchy-Schwarz after pulling an output
observable through the channel, then gives

```
F_R+F_in >= F_H(output).
```

N measurement commutes with H. Exact matching of the N=4 block therefore
already gives `F_R>=4p4 Var_H(phi4)-F_in`. This explicitly accounts for the
nonzero success probability and initial input coherence.

For approximation one must not invoke uniform continuity of QFI under a
growing H. Instead let `x=P_0^H chi`, `z=P_1^H chi`, `l=||x||`, `b=||z||`,
`a=x/l`, `c=z/b`, and set

```
A_e=i(|c><a|-|a><c|),
d_e=2 l b |<c,Hc>-<a,Ha>|,
v_e=l^2+b^2.
```

Extend A_e by zero on the other Hermitian bands and N sectors. Its norm is
one. Its target commutator expectation has magnitude d_e and its target
second moment is v_e. By the preceding estimates,

```
epsilon d_e -> 8 sqrt(3) kappa q(t),
v_e -> q(t),
2 l b / epsilon^3 -> (8 sqrt(3) kappa/delta) q(t).             (22)
```

Let `eta_e=||sigma_out-rho(t)||_1`, or simply the trace norm of the difference
of their N=4 compressions. Both are unhalved trace norms; the first bounds the
second. Put `h_e=min_c ||H_(N=4)-cI||=O(epsilon^-4)`. The norm bounds
`||i[H,A_e]||<=2h_e`, `||A_e^2||=1` and the finite SLD inequality
`F_H(sigma)>=|Tr sigma i[H,A_e]|^2/Tr sigma A_e^2` give the quantitative bound

```
F_R >= [d_e-2h_e eta_e]_+^2/(v_e+eta_e)-F_in.                (23)
```

An output sector flag may be used to read (23); the other outcomes need not
be specified. Equations (20),(22),(23) prove the first claim in (P2) for
`eta_e=o(epsilon^3)`. The same sufficient order applies to a normalized N=4
state error when its probability error is also o(epsilon^3), because p4 has
a nonzero fixed-time limit. The target p4 is not an arbitrarily small marked
amplitude.

The apparatus variance consequently obeys the necessary lower bound
`liminf epsilon^2 Var_(sigma_R)(H_R)>=48 kappa^2 q(t)`. The Fisher condition
is stronger in meaning: an energy-diagonal apparatus has zero F_R even if
its classical energy variance is arbitrarily large. A diagonal mixture at
widely separated energies illustrates why variance alone is not energetic
coherence.

## 7. Finite frequency support and energy range

For a finite Hamiltonian, decompose operators into exact Bohr frequencies.
An exactly covariant map preserves each frequency, as follows by Fourier
averaging its covariance identity. Product frequencies add. No periodicity,
iid limit, or energy lattice assumption is required.

Define B_coh(sigma_R,H_R) as the largest absolute energy difference E-E'
for which the initial density block P_E sigma_R P_E' is nonzero. It is zero
for a stationary density and never exceeds the spectral diameter of H_R.

The initial system vector lies exactly in the Hermitian low band. Let B_in
be the width of that band's spectral interval; (14) implies
`B_in=O(epsilon^-2)`. Let G_e be the distance between the ordered first-high
and low energy intervals in N=4. Their separation is

```
G_e=delta epsilon^-4+O(epsilon^-2).                         (24)
```

If `B_coh(sigma_R,H_R)+B_in<G_e`, every input frequency is too small to create
the band-one/low output block. Thus `P_1^H sigma4 P_0^H=0`. The Hermitian
unit-norm observable `|c><a|+|a><c|`, aligned with the actual target vectors,
then has target expectation `2lb` and implemented expectation zero. Hence

```
||sigma4-rho4||_1 >= 2lb
  = [(8sqrt(3)kappa/delta)q(t)+o(1)] epsilon^3.               (25)
```

For error o(epsilon^3), (25) forces `B_coh+B_in>=G_e` eventually, and proves
the second claim in (P2). Having this bandwidth is necessary, not sufficient.
An apparatus may have a huge spectrum and variance but no density-matrix
frequency component near the required gap. Scalar energy shifts change none
of the Fisher, bandwidth, variance or gap statements.

## 8. Error sensitivity, mean energy, and sector limits

The exponent in (23) is a sufficient robust scale with an explicit cause:
the signal is O(epsilon^-1), while the commutator error is bounded by
`O(epsilon^-4 eta_e)`. It is not obtained by unproved continuity of unbounded
moments. Exact Hermitian-band pinching of just rho4 removes its leading
low/high coherence with trace error

```
||rho4-sum_r P_r^H rho4 P_r^H||_1
       =[(8sqrt(3)kappa/delta)q(t)+o(1)] epsilon^3.            (26)
```

The additional r>=2 cross terms are O(epsilon^4). Pinching preserves every
energy moment, including the divergent variance. It removes the divergent
N=4 Fisher contribution: the low energy vector is bounded, and the centered
Hamiltonian width within each high band is only O(epsilon^-2), giving at
most O(1) subnormalized N=4 Fisher information after pinching. This shows
that this sector's coherence witness can be lost at order epsilon cubed even
while its variance survives. It does **not** show that the full original
ensemble has bounded QFI, or that its apparatus requirements disappear at
that tolerance; the N=6 sector may impose independent constraints.

No diverging ordinary apparatus mean follows from the N=4 requirement.
There is a finite state-preparation comparison for this sector alone. Copy
the relevant system energy space into the apparatus, prepare the state
`rho4(t)` plus complementary probability in the zero-energy N=8 terminal
state, and perform an energy-conserving SWAP. The actual input belongs to
this copied space. The output has exactly the required N=4 block, with the
other probability deliberately assigned to N=8. This is one-input state
preparation with freely chosen other sectors; it generally has the wrong
N=6 output and does not implement the original continuous process.

Its initial Fisher information equals `p4 F_H(phi4)` and its mean energy is
bounded. For a ground-relative statement, the exact low band is bounded
below by a constant through (14), since `D>=0` and H4_S and the remainder
are uniformly bounded; all high bands are positive at small epsilon. A
zero-field low vector gives a matching O(1) upper bound on the minimum.
Together with the bounded N=4 mean above and zero terminal energy, the
apparatus's ground-relative mean is O(1). The rare weight O(epsilon^6) in
the high energy band costs O(epsilon^2) in ordinary mean while it costs
O(epsilon^-2) in variance/Fisher information.

If desired, restrict that comparison to the exact Hermitian bands zero
and one plus the terminal state. The system input remains in this invariant
space; the SWAP on it and identity on its complement still commute with
the additive Hamiltonian. Renormalizing the N=4 vector after removing the
r>=2 tail incurs O(epsilon^4) trace error. The resulting apparatus has
spectral diameter `delta epsilon^-4+O(epsilon^-2)`, the leading Fisher
coefficient in (P2), and bounded ground-relative mean. This demonstrates
attainment within the error class o(epsilon^3) by an O(epsilon^4) sequence
for the **sector-only relaxation**. It does not assert attainment for every
tighter prescribed tolerance, exact spectral-diameter optimality, or full
original-ensemble/process sufficiency.

At t=0 the input is exactly in the Hermitian low band and its Fisher
information is bounded. The fixed-positive-time high component in (12)
has an initial transient, so the leading assertion is not uniform down to
zero. Nor is any assertion made for observation times tending to infinity,
for moving high-flux inputs, for a removed compensation, for a different
single-sign instrument, for an initially correlated apparatus, or for a
readout/controller whose coherence is left uncounted.

## 9. Computation and independent scope

The primary runner includes three root controls. The geometry part enumerates
all 70 four-particle occupancy words, three divergence-free electric inputs and
the original two-sign edge losses at spins 1,2,3,10,40. It checks the factors
12,48,192 and the boundary lower bound. The separate two-level model has an
exact Hermitian zero-energy input and is evolved at fixed physical time; at
epsilon=.02,kappa=.07,t=.3 its scaled conditional variance is about .232958,
toward .2352, and weighted Fisher is about .341712,toward .343343.

The third control uses the actual 3197-dimensional S=1 physical N=4 cube and
the canonical polar input. It approximates all five Riesz components using
32-point contours at epsilon=.1,.06,.035. At the last value the first-high
norm divided by epsilon^3 is about 4.84729 versus 4.84974. The low energy-vector
error decreases but is still about 3.03414; its scaled squared norm is 32.0717
versus 23.52. The decomposition residual is below 3e-15. These are limited
fixed-S corroborations of coefficients, not a numerical proof of the joint
limit or a full cube propagation at a later physical time. No fixed-S sample
is relabeled as a growing-spin theorem.

The included matrix, contour and canonical-preparation definitions are copied
from the pinned root runner SHA256
4bdb0a05140d30e98f1afa85ccbba6c4684626c492550ec0625896d946356c5d.
They are embedded here with no runtime source import. The source adaptation
and genuine primary execution are bound by the publication evidence.

The blind independent checker used primitive physical words, rational boundary
weights and a separately written 70-digit two-band exponential. It imported
no author builder. Its sample first-high graph ratio tends to one; at its
finest epsilon=.005 the scaled conditional variance is .0431741 versus .0432.
Deleting the loss's off-diagonal energy-basis entries removes that toy's high
component. Pinching preserves its moments while removing its energy coherence.
Those controls check mechanisms and constants; the argument supplies the
uniform cube theorem. The checker did not rerun the unchanged large cube work.
The full PRE, scoped released POST and final publication comparison are in
the accompanying review packet, with distinct source and result identities.

## 10. Remaining obligations

The normalized actual-birth N=6 pointwise variance remains separate and open.
This note gives no full-ensemble upper variance/Fisher bound, optimal resources
for the full original output, uniform-in-time or multi-time sufficiency,
selected physical reservoir, irreversible record mechanism, local bounded-
strength implementation, or native derivation of the quantum premises.
At order epsilon^3 error the N=4 coherence witness can disappear, while its
variance remains. No uniform assertion down to t=0 follows, and the selected
positive observation time cannot be sent to infinity without a new estimate.
The finite-spin first-high proof uses both original signs, not a single-sign
loss, and makes no claim about moving high-flux preparations.

Formal retained status, combined integration, strict audit lint and
changed-evidence landing checks remain separate from this selective review.
No merge, audit verdict or new axiom is applied by this publication.

## Landing-review boundary and No-Go Discipline Gate

N1: canonical N=4 start and fixed positive observation times. N2: the normalized N=6-start variance and full-process sufficiency remain separate. N3: compensation, time, preparation and additive covariance are supplied. N4: all parent results retain their stated hypotheses. N5: finite geometry, spin-boundary and band controls supplement the weighted analytic limit. N6: the state-preparation comparison attains one block only. N7: the first-high damping bound needs both original signs; high bare grades need not dissipate. N8: the positive-time result is not uniform down to zero or at diverging observation times.

- [Repository premise boundary](MINIMAL_AXIOMS_2026-06-29.md): does not derive the supplied dynamics.

Historical author checks remain provenance only. Complete original source remains recoverable at PR #9101's frozen head. No audit verdict or retained grade is applied.
