# PRE: a polynomial lower bound for the three actual rotor energy curves

For each of the three stipulated zero-field first marks, and each fixed
`delta,kappa>0`, there is a constant `c_i>0` such that

    f_i(tau) >= c_i (1+tau)^(-5/2)              for every tau>=0.       (1)

Consequently no finite A and positive a can satisfy
`f_i(tau)<=A exp(-a tau)` for all sufficiently large tau. The constants may
depend on delta,kappa and the specified input. This is a lower bound, not a
sharp asymptotic or a matching upper bound. It is compatible with the supplied
strong-decay theorem `f_i(tau)->0`.

This independent PRE did not access the new rate-author directory, campaign
CHECKPOINT, external personal calculations or current peer POST contents.
Prior full-fiber proofs and certificate sources were supplied in the brief;
the new rate proof and local-matrix control were written here. Expected prior
flat-mode and first-mark values were known before the control and are disclosed
as supplied comparison targets, not discoveries of this control.

## 1. Exact premises and physical input

The supplied physical sector is the rotor cube with A={0,3,5,6}, B={1,2,4,7},
N=6, total charge four, W=1 and Gauss law div E=q-1_A. Its complete physical
Hilbert space is unitarily `L2(T^5;C^96)` with normalized Haar measure. Use the
A-to-B edge order

    (01,02,04,31,32,37,51,54,57,62,64,67)

and the supplied five chord indices (0,5,7,8,10). The unique integer tree
reference fields have zero chord fields, so the cycle coordinates of a
physical word are exactly its five chord electric fields. The fiber generator is

    A(theta)=-i delta G(theta)-kappa P_b,
    G(theta)=Pi1(F(theta)F(theta)*-F(theta)*F(theta))Pi1.              (2)

Here `Gamma=2P_b`, where the bright space has adjacent vacancies and dimension
72; the opposite-vacancy dark space has dimension24. This loss operator is the
same for the stipulated resolved and coherent instruments. Their marked
channels are not identified. All fiber semigroups are contractions.

The supplied finite-fiber statements, rechecked at zero by the new local
control, are

    P_d G(theta) P_d=0,
    rank(P_b G(0)P_d)=23,
    u=(equal sum of the24 dark charge labels)/sqrt24,
    G(0)u=Gamma u=0.                                                (3)

The full Laurent cancellation and physical Gauss-coordinate identification
remain supplied verified structure; they are not newly claimed as an
independent global reconstruction here. The new code enumerates the complete
168-label N=6 sector directly from all local charge words, builds the full
outward matrix F(0), forms FF*-F*F before its W=1 compression, and exactly
checks the flat identities and rank in (3). It imports no campaign builder.

For each first mark define `r_i(theta)=Rhat_i(theta)/sqrt(b_i)`. The actual
finite physical words are built from the all-A-plus, B-empty, E=0 state Omega:

    B_i=j_i F Omega,       R_i=-F_0 B_i.

The three j_i are the original edge01 plus, minus and their stipulated coherent
sum (that is, j_coherent=j_plus+j_minus, with relative sign +). R_i is the
already derived high-band coefficient, not an added physical postselection.
The new control retains every integer field word and obtains

| mark | b_i | ||R_i||² | alpha_i²=||u u* r_i(0)||² | M_i | d_i |
|---|---:|---:|---:|---:|---:|
| resolved plus |2|4|1/12|sqrt2|sqrt2|
| resolved minus |2|2|1/12|sqrt2|sqrt2|
| coherent sum |4|6|1/6|2|2|

Here the explicit finite-word estimates are

    ||r_i(theta)||<=M_i,
    ||r_i(theta)-r_i(0)||<=d_i |theta|.                              (4)

For a physical Fourier coefficient c_E these follow from
`|exp(i theta.n)-1|<=|theta| |n|`, summing `|c_E|` and `|c_E| |n|` before
dividing by sqrt(b_i). The stored output gives the actual charge/field words.
As a discriminator, changing the coherent relative sign to minus produces
zero projection onto u. That different mark is outside this conclusion; the
present argument cannot be applied by pretending all inputs have alpha_i>0.

The normalized Haar identity is exactly

    f_i(tau)=integral ||exp[tau A(theta)] r_i(theta)||²
                                d^5theta/(2pi)^5.                 (5)

The vectors in (5) are fixed physical inputs. No tau-dependent input wave
packet or delta-distribution Fourier state is substituted.

## 2. A first independent route: contractive Duhamel gives power five

There is a useful weaker proof that does not need spectral simplicity. Each
of the twelve link transport partial isometries has norm at most one. Only
five link phases vary in the chosen coordinates. Thus, with Euclidean
|theta| in a coordinate ball around zero,

    ||F(theta)||<=12,
    ||F(theta)-F(0)||<=5|theta|,
    ||G(theta)-G(0)||<=240|theta|,
    ||A(theta)-A(0)||<=L|theta|,             L=240 delta.             (6)

The product-difference estimate has two products, each contributing at most
`(12+12)*5|theta|`. These are conservative operator bounds, not fitted norms.
Since u is also a left null vector of A(0), contractive Duhamel gives

    |<u,exp[tau A(theta)]r_i(theta)>-<u,r_i(0)>|
       <= (d_i+tau L M_i)|theta|.                                  (7)

Set `s_i=min(1,alpha_i/[2(d_i+L M_i)])`. On the five-dimensional ball
`|theta|<=s_i/(1+tau)`, the final amplitude in (7) has magnitude at least
alpha_i/2. This ball has positive Haar measure for every finite tau. Its
volume is `(8pi²/15)[s_i/(1+tau)]^5`. Integrating (7) in (5) already proves

    f_i(tau)>=alpha_i² s_i^5/(240pi³) * (1+tau)^(-5).                (8)

Equation (8) alone excludes every eventual exponential upper bound for these
fixed inputs. It does not infer their rate merely from absence of operator-norm
decay. The sharper (1) uses more of the exact flat-fiber structure.

## 3. The flat zero eigenvalue is algebraically simple

Let A0=A(0), P0=u u*. Both A0 u and A0* u vanish, so `u-perp` is invariant and
A0 is an orthogonal direct sum of zero and a95-dimensional matrix B0.
If A0 v=0, dissipativity gives

    0=Re<v,A0v>=-kappa||P_b v||².

Thus v is dark; projecting to the bright space gives
`-i delta P_bG(0)P_d v=0`. By the exact rank23 in (3), v is a multiple of u.
Therefore B0 has trivial kernel and is invertible. A generalized zero vector
would require a nontrivial nilpotent zero block inside B0 or a coupling into
u; the former contradicts invertibility and the latter the orthogonal direct
sum. Hence zero is algebraically simple without assuming A0 normal.

Write

    m=||B0^(-1)||,             rho=1/(2m).                          (9)

These are finite positive constants at the stipulated fixed delta,kappa. For
`|z|=rho`, the resolvent on u is z^-1, while on the complement the Neumann
series for `z-B0` yields norm at most2m. Hence

    ||(z-A0)^(-1)||<=2m.                                           (10)

No numeric spectral gap estimate is needed for the proof.

## 4. Nearby eigenprojections and quadratic real-part loss

Suppose `L|theta|<=1/(16m)`. Another resolvent Neumann series gives
`||(z-A(theta))^-1||<=4m` on the same contour. Define the Riesz projection by
its explicit finite-matrix contour integral

    P(theta)=(1/(2pi i)) integral_(|z|=rho) (z-A(theta))^-1 dz.

The resolvent identity and (10) give

    ||P(theta)-P0|| <= rho*(4m)*(L|theta|)*(2m)
                     =4mL|theta| <=1/4.                           (11)

The contour projector has rank one: the separating contour stays invertible
along the segment from0 to theta, the projector varies continuously, and its
integer rank cannot change. These facts also follow by integrating the finite
Jordan resolvent; this invocation does not assume a rate theorem. Let lambda(theta)
be its sole eigenvalue and `v(theta)=P(theta)u`. Then

    ||v(theta)||>=3/4,       ||P_b v(theta)||<=4mL|theta|.

The generator's dissipative identity, applied to this eigenvector, is exact:

    Re lambda(theta)=-kappa ||P_b v(theta)||²/||v(theta)||²
                    >=-beta |theta|²,
    beta=64 kappa m² L².                                          (12)

The factor64 is a deliberate overestimate. This derives quadratic damping
from the actual loss operator and the dark zero vector. It does not assume
that an eigenvalue is real, that G and Gamma commute, that all other
exceptional phases are isolated, or that the quadratic form is positive
definite. Further degeneracy could make decay slower and would not harm (1).

## 5. Projection of the fixed inputs and integration

Define the positive radius

    eta_i=min(1,1/(16mL),
                alpha_i/[2(4mL M_i+d_i)]).                         (13)

For `|theta|<=eta_i`, equations (4) and (11) give

    ||P(theta)r_i(theta)-P0 r_i(0)||
      <=(4mL M_i+d_i)|theta| <=alpha_i/2,
    ||P(theta)||<=2.

Since the spectral projector commutes with the generator and has rank one,

    P(theta)exp[tau A(theta)]r_i(theta)
                  =exp[tau lambda(theta)]P(theta)r_i(theta).

This yields a lower bound on the full output norm even for a nonnormal
matrix or destructive interference among other components:

    ||exp[tau A(theta)]r_i(theta)||
       >= ||P(theta)exp[tau A(theta)]r_i(theta)||/||P(theta)||
       >= (alpha_i/4) exp[-beta tau |theta|²].                      (14)

Now integrate only over `|theta|<=eta_i/sqrt(1+tau)`. The ball lies in the
coordinate chart since eta_i<=1<pi, and `tau |theta|²<=eta_i²`. Normalized
five-ball volume is `r^5/(60pi³)`. Thus (5) and (14) prove (1) with the fully
specified positive constant

    c_i=alpha_i² eta_i^5 exp[-2beta eta_i²]/(960pi³).                (15)

The chosen spectral neighborhood and each input are fixed; only the portion
of the integral used to bound it shrinks with tau. This distinction resolves
the strongest possible measure-zero objection to a flat-fiber witness.

If an exponential upper bound held eventually, (1) would imply
`c_i exp(a tau)/(1+tau)^(5/2)<=A` there. The left side diverges, a contradiction.
No uniform positive lower value is claimed. The supplied strong-decay theorem
still gives f_i(tau)->0, with the lower bound constraining how rapidly it can
approach zero.

## 6. Exact control, limits, and independent scope

`local_rate_control.py` reconstructs the complete flat matrix, dark/bright
partition, rank23, physical first-mark words and nonzero normalized overlaps.
It also checks the left/right eigenvector dissipative identity and near-zero
projections numerically at three parameter pairs and three phase radii. Those
samples are illustrations of the proved perturbation structure, not a
sharp-power fit, exceptional-set classification or proof by numerical gaps.
The code never imports the prior author control. Its outputs and execution
receipt are preserved in full; no failed execution or relaxed assertion has
occurred. The alternate-relative-sign input discriminator is retained.

The physical direct-integral and prior strong-decay statements are supplied
premises identified in SOURCE_BINDINGS.json. Their source paths/hashes remain
exact. The separate compact-time microscopic identification is bound to note
`f71515321246fd2900b1ca801eb12e816b0a7ab2a1d8f820ae75bb87e28df02a`
and its released completed comparison seal
`5824c37555272e57a1b5b0b1214bcb5441a86dd9362f18bb157bbeec960a4ef5`.
The principal tail note is
`9d73530905763400ce31f66188c5eb9c5c1a0336e0c444bbe4f1c23c0c19fc7a`,
with author seal
`646d5a33082c0d44a8af5a25a22b61da9b8ca89275651f80458c2a9c7f7f02e6`.
The released independent prior PRE is
`4fac5d28f39bfe747f50c2a8ca083353a92f6a58bddaf46456127d9770d0e5de`.

This result concerns the rotor curves after the compact-time joint limit has
already been taken. Neither lower bound permits inserting tau=t/epsilon² in
that compact-time theorem. It says nothing new about fixed-positive-time
microscopic energy, finite-spin infinite-time decay, unbounded energy moments,
heat transfer, bath realization, reservoir requirements or physical selection.
It does not claim a universal polynomial lower bound for arbitrary physical
inputs. The constants can deteriorate as delta or kappa approaches zero; those
excluded degenerate cases have different nondecay mechanisms.

The proof does not provide a matching upper power, a leading coefficient, a
complete exceptional set, optimal constants, or the exact exponent. Those
questions remain outside the requested bounded check. No audit verdict,
publication action, axiom adoption or source comparison with the new root rate
work has occurred. The restricted scope stress test is in
NO_GO_DISCIPLINE_CHECKLIST.md; it supplies no additional scientific premise.
