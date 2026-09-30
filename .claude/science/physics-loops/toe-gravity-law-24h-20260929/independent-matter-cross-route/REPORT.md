# A finite local repair of the matter CC bracket, and its mixed-bracket limit

Research status: **bounded-support; author construction and focused exact checks,
not a formal review or audit verdict**. No axiom, primitive, source status, or
canonical convention is adopted or changed by this report.

The flat matter CC equation has a finite solution for the actual averaged
walker energy and bond current, with the canonical current sign specified
below. An explicit Hermitian, proper-cubic, time-reversal-compatible solution
has radius four on the actual staggered gravity slots. It cancels every
relative-lapse coefficient, including the nonadjacent delta-lapse witness.

It does **not** complete the coupled algebra. The next necessary GC equation
fails already for a constant shift: its first lapse moment has a nonzero
three-step walker coefficient, while a scalar transformation of the lapse
has none. All regular finite-range gravity cross terms vanish at that lapse
order. Thus the supplied flat energy and current cannot be retained together
in the stated strong, scalar-smearing hypersurface algebra merely by adding
the momentum-linear matter term, or higher regular local gravity couplings.
Changing that generator/current identification is a concrete remaining route.

## Source identity and prior art

Selected procedure/science source is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`.
Refreshed main used for the source check is
`e75578f7136401d4bd750131671aed9212c06291`. Every scientific/procedural path
listed in [SOURCE_IDENTITIES.json](SOURCE_IDENTITIES.json) has identical bytes
at those two revisions and in the working tree. The campaign HEAD is a
separate pack-bearing revision recorded there; it is not asserted to be the
selected source revision. The parent snapshot `open_prs_2352.json` binds the
open-proposal inventory. Actual PR9363 source was read at
`fd51a1f4c7f38c124d6f0f7dde396198eadf8b36`, including T5's full argument.

Read scientific definitions: blocks62/101/112, blocks135/136/139, the pack's
`NONLINEAR_CONTRACT.md`, `INDEPENDENT_SEED_CHECK.md`, and
`independent-matter-route/REPORT.md`. The full block136 energy/current stencils
are used; its prescribed-source invariance is not treated as an off-shell
matter gauge action. The incidence-scalar Ward note concerns a different
carrier and is not used as a walker proxy.

Relevant prior art is substantive. PR9363 T5 gives the walker-only CC defect,
its low-lapse-momentum expansion, and an extreme-hop obstruction when no
gravity cross term is allowed. Its full cross equation remains open there.
The finite curvature-ideal construction below supplies that cross term rather
than extending the walker-only obstruction. Landed block106 already derives
the periodic momentum derivative and the factor `cos(2k)`. The exact-boost
note T2 also derives `i[D_i,P_j]=-delta_ij cos(2k_j)H`. Those exact arguments
were read during the prior-art refresh. The multiplier is not new here; the
additional step is proving that it survives all regular flat gravity cross
terms in the declared GC equation. All these identities are reconstructed
below; no provisional PR theorem is a load-bearing lemma.

## Fixed target, domain, and signs

Use finite-support fields and smearings on the infinite integer lattice,
with identities understood as finite local coefficient identities. Constant
shift and lapse probes are also allowed: their quadratic forms are defined
on finite-support walker states. Equivalently, any candidate of a fixed
finite radius must satisfy the identities on every sufficiently large torus.
There is no restriction to on-shell states, low momentum, one species,
nonzero lapse modes, or gradient-only shifts.

Six real gravity canonical pairs have `{h_A,P_B}=delta_AB`: diagonal slots
at integer vertices and off-diagonal `ij` slots at `x+(e_i+e_j)/2`, anchored
at integer base `x`. The matrix momentum's off-diagonal entries are `P_ij/2`.
The walker is a supplied complex two-component canonical amplitude with
`{psi_a(x),psi_b*(y)}=-i delta_ab delta_xy`, independent of the gravity pairs.
Consequently

\[
 \{\psi^*A\psi,\psi^*B\psi\}=\psi^*(-i[A,B])\psi,
 \qquad \{\psi,\psi^*A\psi\}=-iA\psi.                 \tag{1}
\]

The pure gravity seed is `C1[N]=-K<R1 h,N>`, `K!=0`, and positive spatial
Lie `G1[xi]=P.Rxi`. Its verified bracket has

\[
 F_{0,j}(N,M)=\lambda(N_xM_{x+e_j}-M_xN_{x+e_j}),\qquad
 \lambda=K/(4\alpha).
\]

We use `lambda=1` for the construction. In particular, the sign opposite to
the block112 source prose is not silently imported. Its curvature gradients
have symbols

\[
 r_{jj}(x)=\sum_{i\ne j}(2-x_i-x_i^{-1}),\qquad
 r_{ij}(x)=2(1-x_i)(1-x_j),\quad i<j.                 \tag{2}
\]

Let `T_j psi(x)=psi(x+e_j)`, `S_j=(T_j-T_j^-1)/(2i)`,
`C_j=(T_j+T_j^-1)/2`, `H=sum sigma_j S_j`, `P_j=S_j C_j`.
The actual source energy is `E_N={f_N,H}/2`, `f_N=C1 C2 C3 N`.
The actual bond density is block136's `P^B=(P''+Q)/2`, with
`P''_j=((1+T_j)/2) prod_(l!=j) C_l Re(psi* P_j psi)` and

\[
 Q_j=C_1C_2C_3 Q_j^b,\quad
 Q_j^b(a)=\tfrac12\operatorname{Re}\{
 \psi^*(a+e_j)\sigma_j(H\psi)(a)
 +(H\psi)^*(a+e_j)\sigma_j\psi(a)\}.
\]

The summed current is exactly `P_j`, so `+P^B[xi]` generates
`delta psi=-i xi_j P_j psi` for constant `xi`. At smooth momentum this is
`-xi.partial psi`. The canonical matter generator with the **positive**
spatial Lie orientation instead is

\[
                         J[\xi]=-P^B[\xi].           \tag{3}
\]

This sign is fixed by (1) and the transformation convention, not fitted to
CC. Its exact staggered action is `delta psi=+i B[xi]psi`; it is only a
long-wavelength spatial Lie derivative. For real shifts, `B[xi]` is Hermitian.
Block136 displays a prescribed-source term `-N.P^B` with Fourier factors of
`i` absorbed. It does not establish the real-space matter canonical action
(1). If its displayed sign is read literally as a real canonical shift
Hamiltonian, it gives `J=+P^B`, a separate branch considered below.

The candidate canonical Hamiltonian is

\[
 C[N]=C_g[N]+\psi^*E_N\psi+
 \sum_A h_A\psi^*V_{N,A}\psi+
 \sum_A P_A\psi^*A_{N,A}\psi+\cdots.                \tag{4}
\]

`A` is linear in the lapse, quadratic in matter amplitude, regular at
`h=P=psi=0`, translation-covariant, finite-range and Hermitian for real lapse.
Its coefficient is odd under spin time reversal `Theta=i sigma_y K`, so the
constraint term `P.A` is even. This fixes the operator ordering as the
classical bilinear `P_A psi* A psi`. No quantum gravity ordering is inferred.
“Minimal” here means the first momentum-linear field order, not minimal
radius or minimal coefficient count.

At zero gravity fields and degree two in matter, (4) gives precisely

\[
 K\sum_A(r_{N,A}A_{M,A}-r_{M,A}A_{N,A})
   =D(N,M):=-i[E_N,E_M]-J[F_0(N,M)].                \tag{5}
\]

The source response `V` is left arbitrary; it cannot enter (5).

## Exact symbols and the finite local construction

Set `x=e^(iq)`, `y=e^(ip)`, `z=e^(ik)`, where `q,p` are the two lapse
momenta and `k` is the ket momentum. Operators send `k` to `k+q+p`.
With `c(q)=prod cos q_l`,

\[
 E(q;k)=\tfrac12c(q)[H(k+q)+H(k)],
\]
\[
 B_j(Q;k)=\tfrac12\left[
 \tfrac{1+e^{-iQ_j}}2\prod_{l\ne j}\cos Q_l\,
       \tfrac{P_j(k)+P_j(k+Q)}2
 +\tfrac{c(Q)}4(e^{-i(k+Q)_j}+e^{ik_j})
       (\sigma_jH(k)+H(k+Q)\sigma_j)\right].        \tag{6}
\]

The first term is scalar in coin space; matrix order in the second is as
written. Thus the defect actually constructed is

\[
 D(x,y,z)=-i\{E(q;k+p)E(p;k)-E(p;k+q)E(q;k)\}
             -\sum_j(x_j-y_j)B_j(q+p;k).           \tag{7}
\]

There is a simple finite-Laurent solvability criterion. In the Laurent ring
over `Q(i)` with matrix coefficients, let `m_x=(x_1-1,x_2-1,x_3-1)`.
Equation (2) generates exactly `m_x^2`. Indeed, for `d_i=2-x_i-x_i^-1`,

\[
 d_i=(r_{jj}+r_{kk}-r_{ii})/2,\quad
 (x_i-1)^2=-x_i d_i,\quad
 (x_i-1)(x_j-1)=r_{ij}/2.                          \tag{8}
\]

The relevant pair ideal is `m_x^2+m_y^2`. Its normal remainder consists
only of `1`, `x_i-1`, `y_j-1`, and `(x_i-1)(y_j-1)`, with Laurent coefficients
in `z`. For (7) every remainder coefficient vanishes.

This cancellation also has a short analytic verification. With one lapse
uniform, the Clifford square `H(k)^2=|sin k|^2 I` and (6) give exact equality
of the energy commutator and the current. In particular the constant and
single-lapse first jets of `D` vanish. Write `H_i=partial_i H`.
The mixed physical derivatives of the energy commutator at `q=p=0` are

\[
 -\tfrac i4[H_i,H_j]
   =\tfrac12\epsilon_{ij\ell}\cos k_i\cos k_j\,\sigma_\ell.
\]

For `i!=j`, the vector part of `partial_(Q_j) B_i(0;k)` is
`-i epsilon_(ij ell) cos k_i cos k_j sigma_ell/4`.
The mixed derivative of `sum(x_j-y_j)B_j(q+p;k)` is therefore the same.
The `i=j` term is zero in both. Hence (7) is in the pair ideal, for every
walker momentum, without dividing by a momentum or dropping zero modes.

For completeness, the actual finite quotient is obtained by ordered divided
differences. Set preceding variables to one successively and define

\[
 f-f(1)=\sum_i(x_i-1)\mathcal D_i f.
\]

Each `D_i` is finite Laurent because `(x^n-1)/(x-1)` is a finite signed
geometric sum for every integer `n`, including negative `n`. Apply the same
identity to `D_i f-(D_i f)(1)` to obtain

\[
 f-T_x f=\sum_{i,j}(x_i-1)(x_j-1)\mathcal D_j\mathcal D_i f,
\]

where `T_x` is the total first Taylor jet in `x`. Apply this first to `D`
in `x`, then to `T_x D` in `y`. The remainder `T_y T_x D` is zero. Use
(8) to write `D=sum r_t(x) f_t + sum r_t(y) g_t`. Since `D(y,x,z)=-D(x,y,z)`,

\[
             K A_t(x,y,z)=\tfrac12\{f_t(x,y,z)-g_t(y,x,z)\}             \tag{9}
\]

solves (5). No infinite inverse, sampled fit, or hypothesis that a lattice
Leibniz rule holds enters this construction.

Every Laurent quotient is an actual local canonical coupling. A monomial
`x^a y^b z^c` in `A_t` corresponds, at the base of gravity slot `t`, to

\[
       M_{b-a}\,\psi^*_{-a}\,({\rm coin\ matrix})\,\psi_{c-a}.
\]

Hermitian conjugation swaps bra/ket endpoints and conjugates the matrix.
Project (9) to its Hermitian, time-reversal-odd part. Then average over all
24 proper cubic rotations, rotating the Pauli matrices and the canonical
tensor slots and reanchoring negatively oriented faces. These operations
preserve (5); the code also verifies this directly. The resulting explicit
`K A` is [coupling_KA.json](coupling_KA.json), SHA256
`9bc29d9f43e5d83993922ec83402b9f6237c956689ce00e56bf14d9dd28a900e`.
It has **82,332** nonzero rational Pauli/Laurent coefficients. The maximum
physical Chebyshev radius from either its lapse anchor or its `P` slot is
**4**; diagonal component radii are 4 and shear component radii 7/2.
The maximum coordinate diameter of any term is also 4. No minimality is
claimed.

There is an explicit common first-order canonical action for this partial
construction:

\[
 S=\int dt\,[\sum_A P_A\dot h_A+
 \tfrac i2(\psi^*\dot\psi-\dot\psi^*\psi)-C[N]-G[\xi]].              \tag{10}
\]

Here insert (4),(9) and `G=G_g+J+...`. Thus the cross term is a specified
local action term, not a cancellation matrix with no phase-space meaning.
Equation (10) by itself neither makes the constraints first class nor
identifies its sources with physical stress. The next calculation shows a
necessary bracket that it cannot satisfy while preserving the flat data.

## The mixed GC obstruction after allowing gravity cross terms

Keep the direct-product canonical pairing, `C1=-K R1`, the flat `E_N` and
`J=-P^B`. Allow arbitrary regular finite-range higher field coefficients in
both `C` and `G`, including `G` terms linear in gravity momentum and quadratic
in matter. Preserve the fixed `G1=P.Rxi` and require strong closure

\[
                 \{G[\xi],C[N]\}=C[U_0(\xi,N)]+\cdots,             \tag{11}
\]

where the flat structure kernel `U0` is a scalar, translation-covariant,
finite-range bilinear map of the smearings, independent of the walker ket
momentum. Higher structure functions are regular field Taylor terms as in
the campaign contract. No choice of `U0`, even with unrestricted finite
radius and without imposing its continuum normalization, solves (11).

**Proof.** Set `xi=e_j` constant and `h=P=0`, and retain matter degree two.
The linear gravity action vanishes exactly: `R xi=0`. Consequently arbitrary
`h.psi^2` terms in `C` have zero cross bracket with `G1`; the new `P.psi^2`
term in `C` cannot help either. Any `P.psi^2` term in `G` can contribute only
through `+K r_N` times its finite kernel. Every component of `r_N` has zero
constant and first lapse moment by (2). All higher regular gravity terms
vanish at this flat field order. Matter terms of degree four or above also
vanish at matter degree two. The only surviving first lapse jet is therefore
the actual matter commutator.

For the constant shift, `J=-P_j(k)I`. With `N=e^(iq.x)`,

\[
 -i[J,E_N](q;k)=i\{P_j(k+q)-P_j(k)\}E(q;k).        \tag{12}
\]

Translation covariance puts `U0(e_j,N)=u_j(q)N`. The uniform-lapse equation
forces `u_j(0)=0`. Differentiate in the lapse Laurent variable `x_j` at
`x=1`; (12) becomes

\[
            \frac{z_j^2+z_j^{-2}}2\,H(z),          \tag{13}
\]

while the right side of (11) is `c_j H(z)` for a scalar constant `c_j`.
The `sigma_j z_j^3` coefficient of (13) is **`-i/4`**. The corresponding
coefficient of `c_j H(z)` is zero for every `c_j`. Every gravity cross term
has already vanished at this first moment. This is an exact contradiction.
Equivalently, a physical `q_j` derivative would require the scalar
`u'_j(0)=i cos(2k_j)` at every `k`, which is impossible. ∎

This is a first-moment consequence of the known periodic-momentum factor,
but includes the full allowed gravity cross terms at the relevant order.
It therefore does not rest on a walker-only CC calculation. It excludes
arbitrary finite support in this *specified* completion class, not all
common actions or all gravity. Constant lapse and constant shift separately
still commute correctly; the failure needs a nonuniform lapse. Constant
shifts are part of the arbitrary-shift target and are not gradients of
periodic scalar functions. A gradient-only shift target is not substituted
for that target or classified by this constant-shift proof.

Canonical Poisson Jacobi remains exact for (10). Failure of (11) means that
no claimed hypersurface-algebra Jacobi statement or GG completion follows
from the successful CC calculation. GG was not solved; another unsolved
bracket is not needed to invalidate the declared full closure.

## Mass, normalization, and other boundaries

The block139 staggered mass does not change the CC construction. With
`epsilon(x)=(-1)^(x1+x2+x3)`, `E_f(m)={f,H}/2+m epsilon f`.
For commuting multiplication operators `f,g`, write `A_f={f,H}/2`.
The exact mass cross term is

\[
 [A_f,\epsilon g]+[\epsilon f,A_g]
   =\epsilon(\{f,A_g\}-\{A_f,g\})=0,
\]

using `{epsilon,H}=0`; the `m^2` term is zero too. Thus the full pair
commutator is independent of every real `m`, not merely a tested mass.
The actual current remains block139's `P^B`. The same `A` solves CC.
For GC, `P_j(k+pi)=P_j(k)` in the doubled staggered representation, so (13)
is `cos(2k_j) H_m(k)`. Its massless `sigma_j z_j^3` coefficient remains and
cannot be a scalar multiple of `H_m`. The fixed staggered background is
kept explicitly; one-site translation symmetry of a fixed nonzero `m`
background is not silently asserted.

For `J=-P^B`, the first lapse jet of CC forces `lambda=1`. For the literal
`J=+P^B` branch with the same positive canonical gravity seed, it instead
forces `lambda=-1`. The physical normalization in the campaign has positive
`K,alpha`, so the latter cannot hold. At `lambda=+1` its exact quotient
remainder has 84 nonzero terms: there is no finite local `A` even for CC.
These are separate sign branches, not a redefinition of the frozen seed.

The proof does not cover a changed flat current/gauge generator, nonlocal
singular cross kernels, additional phase-space carriers, a noncanonical
mixed symplectic form, extra constraint-valued tensor/operator smearings,
weak on-shell closure, or a restricted low-momentum state sector. A physical
current need not equal the generator of spatial relabellings. Distinguishing
them while constructing the resulting conserved stress and common action is
an actual open alternative, not excluded by the coefficient certificate.

## Exact evidence and compute record

The construction was priced as direct finite Laurent multiplication and
division, rather than a radius-enumeration linear system: 96 energy terms,
at most order `10^4` raw pair terms, then finite quotient/symmetry growth.
Single-thread standard-library rational arithmetic was used. Actual peak
RSS for the full construction was 194,396,160 bytes and elapsed time 135.2s.
The initial rough 100MB expectation was exceeded by cubic symmetrization;
there was no unbounded worker or dense solve. The campaign deadline and stop
sentinel were checked before this work; the original deadline remained and
no stop request was present. No source runner, audit, or GitHub mutation ran.

Reproduction, each command from this directory:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 laurent_completion.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 position_check.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 mixed_certificate.py
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 mass_check.py
```

- [laurent_completion.py](laurent_completion.py), [run.log](run.log),
  [results.json](results.json): exact normal remainder zero; quotient
  recombination; antisymmetry; Hermiticity; time reversal; all 24 rotations;
  full CC residual zero; explicit coefficient export and support pricing.
- [position_check.py](position_check.py), [position.log](position.log): a
  second implementation uses literal real-space `2x2` matrix entries and
  source anticommutators, importing no constructor primitives. All **15,168**
  defect matrix coefficients on **188** nonzero relative lapse displacements
  match (7). `N=delta0,M=delta2e1` has 16 nonzero spatial blocks and the
  spin-up `(-1,-1,-1)` to `(1,-1,-1)` coefficient is `i/1024`. Runtime 0.86s,
  peak RSS 34,914,304 bytes. No torus folding or floating tolerance is used.
- [mixed_certificate.py](mixed_certificate.py), [mixed.log](mixed.log):
  reconstructs (13) from the literal energy stencil for each of three axes;
  checks the nonzero three-step coefficient and the six curvature stencils'
  zero zeroth/first moments. It shares the position source-stencil function,
  not the Laurent/homotopy implementation.
- [mass_check.py](mass_check.py), [mass.log](mass.log): expands all
  mass-dependent real-space pair products with the actual translated
  staggered signs; every linear/quadratic mass coefficient cancels.
- [support_results.json](support_results.json): support measured using
  doubled physical face coordinates from both lapse and momentum anchors.

These independent implementations share the stated mathematical definitions
and this author. They are not independent-agent review coverage. Exact local
coefficient comparison supplies the infinite-lattice lift; a sampled torus
rank result is not being promoted to one.

## Family tuple, terminal strength, and negative-claim discipline

Family tuple: **(local canonical matter/gravity Laurent kernels;
curvature augmentation-square ideal and first-moment projection;
CC ideal membership followed by simultaneous GC/GG closure)**.

The CC necessary subproblem is constructively closed for the explicitly
supplied branch (3), with a strictly weaker result than full common-action
closure. The fixed-flat-data strong GC completion is obstructed by the
displayed coefficient. There is no remaining existence lemma inside that
same completion class to declare “almost solved.” The useful terminal
question is now: construct a different matter spatial generator or enlarged
canonical carrier, with actual conserved energy/current bookkeeping, for
which all flat CC/GC/GG identities and subsequent field orders hold. For
the overall coupled-gravity target that obligation is **target-equivalent**
at the common-action algebra level; merely naming a new generator would not
advance it. The successful CC homotopy is reusable evidence, not a claim
that this larger obligation is near completion.

N1: Real attacks tested here are the curvature-ideal momentum coupling
(successful for CC), Hermitian/cubic projection (successful), the opposite
current sign (fails the necessary first jet with positive normalization),
and the mixed first-moment gravity-cross cancellation test (fails GC).
These are not inflated into five materially distinct discovery families.
The five-family formal packet quota is therefore not certified; this local
research report is not a negative-theorem submission or formal PASS.

N2: There is one scoped GC coefficient contradiction, not a counted list of
independent walls. No implication or independence between physical-source
selection and canonical completion is claimed.

N3: Load-bearing supplied conditions are the direct-product canonical
pairing, regular expansion, exact flat energy/current, curvature seed,
arbitrary shifts, finite locality and scalar-smearing strong closure.
Registered units, kinetic isotropy, and realized-state primitives do not
supply these structures. They are not introduced as new primitives.

N4: PR9363's extreme-hop CC residual is a different residual; it is prior
art, not a witness against (5). Block106 and the boost note give the same
momentum derivative but do not themselves discharge the gravity-cross
argument in (11). The scoped obstruction is proved here without importing
either earlier negative conclusion.

N5: The code checks exact matrix elements, all relative-lapse supports of
the actual flat CC operator, full coin blocks and formal first moments.
Lattice-wide conclusions use finite Laurent coefficient identities. No
individual plane wave normalization, finite-state sampling, or untested
nonlinear/physical-observable conclusion is substituted for these checks.

N6: No result says a new axiom is required. Changing which current is the
canonical gauge generator, or supplying a larger common-action model, is
an explicit alternative. Such a model would need its own derivation and
source identification; no convention label alone cancels coefficient (13).

N7: Strongest objection: “The conserved symmetric source current need not
be the spatial gauge generator. Retain it in the source identity and use a
different connection/embedding action or canonical map, so a constant shift
also moves the variables on which the source depends.” This is concrete and
outside the fixed direct-product/flat-generator hypotheses. The report
leaves that route open; it defeats any broader claim that no common action
exists, but does not invalidate the scoped first-moment proof.

N8: The earlier block106 force claim was narrowed on landing to a formal
band derivative and a restricted representation result; its lesson is
preserved here. The boost note also explicitly avoids calling conserved
charges a full lattice symmetry algebra. The earlier campaign's discrete
calculus route priced carrier/support enlargement rather than declaring all
local models impossible. None of those cautionary boundaries is promoted
to a universal gravity prohibition.
