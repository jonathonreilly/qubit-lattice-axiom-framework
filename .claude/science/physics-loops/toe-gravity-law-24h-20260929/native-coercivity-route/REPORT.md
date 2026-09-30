# Finite-volume kernel and density coercivity of the mobile native pair law

**Status:** conditional mathematical discovery, with exact finite controls;
not a formal review/audit verdict, selected physical law, or tensor-phase
claim. The full proof is below. Independent checking is pending at freeze.

For the explicitly supplied mobile Hamiltonian, the finite-torus zero
kernel is exactly the vacuum plus five zero-momentum pair states. More
strongly, with `V=L³`, `L>=5`,

\[
 H_{\rm mob}\ \ge\ \frac{a}{99\,090\,432}\frac{N(N-2)}{V},
 \qquad a=\min\{\tau,\mu/12\}>0.                                  \tag{1}
\]

The constant is deliberately conservative. The proof uses the full
hard-core carrier, spectator-pinned pair amplitudes, a three-dimensional
box Poincare bound, and a partition by occupation density. It does not
replace the spin operators with bosons or assume a phase.

A chemical-potential perturbation `Hmob-nu N` consequently has ground-state
density tending to zero as `nu` decreases to zero. Explicit separated pair
wavepackets also give a positive density lower bound for each `nu>0` in
large volumes. This rules out the compact-pair density jump of the immobile
stabilized law for this mobile deformation. It does not determine its
finite-density excitations, symmetry breaking, tensor content, or records.

## 1. Fixed input and conventions

The source is the frozen
`native-stability-route/REPORT.md`, SHA256
`7eba7d0092eb4990f5ae1a46825e015c6edc18692c09cab69ad5cd3ed4d24ca9`,
with its explicit operators and source bindings. The original native report
and independent native check were read completely in the preceding route.
Main is `e75578f7136401d4bd750131671aed9212c06291`; selected campaign procedure
is `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`. The parent reported a manual
reconstruction of the stabilizer, incidence, packing and gap arguments and
supplied the zero-kernel argument for independent inspection here. Those
communications are provisional scientific checks, not formal status.

Use one ordinary qubit per physical site on the cubic torus, commuting
different-site factors, `b_x=|0><1|`, `n_x=b_x†b_x`, and `N=sum n_x`.
The graph `G` has the eighteen neighbor displacements
`±2e_i` and `±e_i±e_j`, and `m_x=sum_(y~Gx)n_y`.
All these neighbors are distinct for `L>=5`.

The fifteen bare pair annihilators at each center are

\[
 d_i(x)=b_{x+e_i}b_{x-e_i},\qquad
 v_{ij}^{st}(x)=st\,b_{x+s e_i}b_{x+t e_j}\quad(i<j;s,t=\pm1).
\]

Their five collective components are

\[
 Q_{E1}=(d_1-d_2)/\sqrt2,\quad Q_{E2}=(d_1+d_2-2d_3)/\sqrt6,
 \qquad Q_{Tij}=\tfrac12\sum_{s,t}v_{ij}^{st}.
\]

Put `D0(x)=d_1+d_2+d_3` and define the nonnegative diagonal operator

\[
 \mathcal D=\tfrac12\sum_x n_x(m_x-1)(m_x-2).
\]

The closing Hamiltonian with the three-body stabilizer and positive pair
hopping is exactly

\[
 H_{\rm mob}=\mathcal A+\mu\mathcal D+W_\tau,\qquad \mu,\tau>0,     \tag{2}
\]
\[
 \mathcal A=\frac{2\mu}{3}\sum_xD_0^\dagger D_0
 +\frac\mu4\sum_{x,i<j}\sum_{a<b}(v_{ij}^a-v_{ij}^b)^\dagger
                                         (v_{ij}^a-v_{ij}^b),
\]
\[
 W_\tau=\tau\sum_{x,k,A}[Q_A(x+e_k)-Q_A(x)]^\dagger
                              [Q_A(x+e_k)-Q_A(x)].
\]

Equivalently it is

\[
 \mu N-2\mu\sum P_E-\mu\sum P_T
       +\mu\sum_x n_x\binom{m_x}{2}+W_\tau.
\]

The earlier unrestricted operator completion of squares gives (2); every
summand is positive. The diagonal polynomial is nonnegative on the integer
spectrum `m_x=0,...,18`. This route uses exactly this law and its full
particle sectors. It supplies no Hamiltonian selection or record instrument
from the axioms/primitives.

## 2. Independent reconstruction of the exact zero kernel

If a vector has zero energy, each square in (2) annihilates it. In
particular `Q_A(x)psi` is constant in `x`. The `D0` square gives
`(d_1+d_2+d_3)(x)psi=0`; inversion together with the constant E doublet
makes each `d_i(x)psi` constant in `x`. The three plane-difference sums
make all four signed words in a fixed plane equal at each center; together
with constant `Q_Tij`, each `v_ij^st(x)psi` is constant in `x` too.

In a sector `N>=3`, fix an output occupation word `eta` of `N-2` particles.
Choose an occupied site `y` of that word. For any bare annihilator type with
endpoints `x+u,x+v`, choose `x=y-u`. Its output amplitude on `eta` is zero:
annihilation at `y` always leaves that site empty, whereas `eta` occupies it.
Since the amplitude was constant in the center, it vanishes at every
center. This works for every output word and every type, so all pair
annihilators kill `psi`. Its energy is then
`〈mu N+V3〉`, which is strictly positive for a nonzero vector with `N>=3`.
There is no such zero vector. This reasoning uses the actual hard-core
output and requires no selected spectator position or dilute approximation.

In `N=1` the energy is `mu`. In `N=2`, diagonal positivity removes all pair
words outside graph G: both particles would have `m=0`. The remaining
pair amplitudes are the center-independent three opposite-pair amplitudes
with one sum constraint, and one signed amplitude for each of the three
orthogonal planes. Their shared-center signs agree. Thus this kernel has
dimension five and is precisely `Q_A(q=0)†Omega`. These vectors are nonzero:
their Gram is `diag(1,1,2,2,2)`, up to the common volume normalization.

Therefore for every stated finite torus

\[
 \ker H_{\rm mob}=\operatorname{span}\{\Omega,
                          Q_A(q=0)^\dagger\Omega:A=1,...,5\}.       \tag{3}
\]

This confirms and sharpens the parent's argument. The number-sector
decomposition is legitimate because the supplied Hamiltonian conserves N.
Equation (3) is a finite-volume statement, not a claim that the uniform
pair waves are normalizable vectors in the infinite vacuum Hilbert space.

## 3. Bare-pair gradients controlled by the actual energy

For a fixed vector `psi`, let

\[
 \mathcal E(\psi)=\sum_{x,k,t}
       \|(B_t(x+e_k)-B_t(x))\psi\|^2,                              \tag{4}
\]

where `t` runs over all fifteen bare types `d_i,v_ij^st`. The E doublet
together with `D0/sqrt3` is an orthonormal transformation of the three
opposite-pair amplitudes. In each plane, `Q_T=(sum v)/2` is the normalized
singlet and the other three directions are orthogonal to it. Thus the
opposite singlet has energy coefficient `2mu`, while each plane complement
has coefficient `mu` in `A`.

For any Hilbert-space-valued function on the torus,

\[
 \sum_{x,k}\|f(x+e_k)-f(x)\|^2\le12\sum_x\|f(x)\|^2.
\]

This follows directly by bounding each squared difference by twice the two
endpoint norms. Applying it to the uncontrolled internal components gives

\[
 \mathcal E\le\frac6\mu\langle\mathcal A_E\rangle
               +\frac{12}\mu\langle\mathcal A_T\rangle
               +\frac1\tau\langle W_\tau\rangle.
\]

Consequently, with `a=min(tau,mu/12)`, the useful simultaneous bound is

\[
       \langle H_{\rm mob}\rangle\ge
             \mu\langle\mathcal D\rangle+a\mathcal E.              \tag{5}
\]

No bosonic commutator or assumed canonical tensor algebra enters this
internal linear change of amplitudes.

## 4. A uniform point-pinned Poincare bound in three dimensions

Let C be a rectangular grid of side lengths `s1,s2,s3`, with largest side
at most twice its smallest. Use only its ordinary free-boundary nearest
neighbor edges. For a complex function `f` with `f(p)=0` at any vertex,

\[
       \sum_{x\in C}|f(x)|^2
          \le448\,|C|\sum_{\{x,y\}\in E(C)}|f(x)-f(y)|^2.          \tag{6}
\]

Here is an explicit spectral proof of the numerical constant. Normalized
Neumann cosine modes have squared absolute value at most `8/|C|` and
eigenvalues

\[
 \lambda_n=4\sum_i\sin^2\frac{\pi n_i}{2s_i}
              \ge4|n|^2/s_{\max}^2,
 \quad 0\le n_i<s_i.
\]

For two vertices, Cauchy–Schwarz in this orthonormal basis bounds their
squared difference by the Dirichlet energy times

\[
 \sum_{n\ne0}\frac{|\phi_n(x)-\phi_n(p)|^2}{\lambda_n}
 \le\frac{8s_{\max}^2}{|C|}\sum_{n\ne0}\frac1{|n|^2}
 \le56\frac{s_{\max}^3}{|C|}\le448.                              \tag{7}
\]

The middle inequality counts nonnegative integer modes by their largest
coordinate: at radius r there are `(r+1)^3-r^3<=7r²` such modes, each with
`|n|²>=r²`. The final inequality uses the aspect-ratio condition. Summing
the pointwise estimate over x gives (6). It also holds componentwise for
vector amplitudes. The dimension three is material to this volume-uniform
point-resistance estimate.

When a rectangle is a cyclic interval subset of a torus, choose the free
path order on each interval and omit its closing edge. For the whole torus,
choose one cut per coordinate and apply the same cube bound. All edges
used in (6) are actual torus edges; none is added.

## 5. Local occupation counting creates the pins

Work first in a fixed `N>=3` sector with a normalized vector. For a bare
pair type t and an output occupation word eta, define

\[
                    f^t_\eta(x)=\langle\eta|B_t(x)|\psi\rangle.
\]

Let B be an inner rectangular box and let C be its enlargement by one
site in every coordinate, as a set of distinct torus sites. Restrict the
output words to those with at least one occupied site in B. Choose such
a site y. If the fixed type has endpoint offset u, its amplitude is pinned
to zero at `x=y-u`, which lies in C. Hence (6), separately for every
allowed eta and every type, gives

\[
 M_C^{B,+}:=\sum_{t,x\in C}\sum_{\eta:\,|\eta\cap B|\ge1}
                     |f^t_\eta(x)|^2
       \le448\,|C|\,\mathcal E_C,                                \tag{8}
\]

where `E_C` sums the bare gradients on the free grid edges of C, with all
output words. The restriction on eta is independent of the center x;
it can therefore be dropped from the positive gradient sum after applying
Poincare. No number projector is moved through a noncommuting annihilator.

Put `N_B=sum_(x in B)n_x`. On each occupation configuration,

\[
 1\le\tfrac12(m-1)(m-2)+m\quad(m=0,...,18).
\]

If `N_B>=3`, removing any near pair leaves at least one occupied site
of B in the residual word. Every graph-G edge incident to B occurs
as a bare pair word centered in C. Each oriented count `sum_(x in B)n_xm_x`
counts a given undirected edge at most twice; the bare word count counts
it at least once. Taking expectations therefore gives the exact inequality

\[
 \langle N_B\mathbf1_{N_B\ge3}\rangle
       \le\langle\mathcal D_B\rangle+2M_C^{B,+}
       \le\langle\mathcal D_B\rangle+896\,|C|\mathcal E_C.          \tag{9}
\]

Here `D_B` is the summand of D with center in B; its neighbors are still
the actual full-torus neighbors. It is not an artificially truncated box
Hamiltonian. This is the step that allows many spectator particles to be
used without falsely assuming that arbitrary pin sets have additive
electrical capacity.

## 6. Partition and the explicit coercivity constant

For `N>=4`, choose

\[
                         q=\lfloor(N/4)^{1/3}\rfloor\ge1.
\]

Partition each coordinate circle into q consecutive intervals whose
lengths differ by at most one; their products are `q³` disjoint inner
boxes. When `q=1`, take the expanded box to be the whole torus, with no
duplicated sites. Otherwise enlarge each interval by one at each end,
capping its length at L. The resulting rectangles have aspect ratio at
most two. A vertex belongs to at most three expanded intervals per
coordinate, so any torus edge belongs to at most `3³=27` of the chosen
free rectangle edge sets. Thus

\[
 \sum_B\mathcal D_B=\mathcal D,\qquad
 \sum_C\mathcal E_C\le27\mathcal E.
\]

The largest expanded volume obeys a deliberately rough bound:

\[
 |C|\le(\lceil L/q\rceil+2)^3\le64V/q^3\le2048V/N.               \tag{10}
\]

The whole-torus `q=1` case also satisfies it. We used `L/q>=1` and
`q>=((N/4)^(1/3))/2`. On the other side,

\[
 \sum_B\langle N_B\mathbf1_{N_B\ge3}\rangle
       \ge N-2q^3\ge N/2.                                       \tag{11}
\]

Summing (9) and using (10)–(11) yields

\[
 N/2\le\langle\mathcal D\rangle+
              B_*\frac VN\mathcal E,
 \qquad B_*=2\cdot448\cdot27\cdot2048=49\,545\,216.
\]

Since `a<=mu/12`, `N<=V`, and `B_*>1`, (5) bounds the right side by
`B_* V〈Hmob〉/(aN)`. Hence for `N>=4`,

\[
                   \langle H_{\rm mob}\rangle
                         \ge\frac{aN^2}{99\,090\,432\,V}.          \tag{12}
\]

For `N=3`, every output word already supplies a pin on the whole torus.
Writing `M=sum_(x,t)||B_t(x)psi||²`, the same counting gives `N<=〈D〉+2M`,
while (6) gives `M<=448 V E`. Therefore

\[
                       \langle H_{\rm mob}\rangle
                             \ge\frac{aN}{896V}\quad(N=3).        \tag{13}
\]

This is stronger than (1) in that sector. For `N=0,2`, its right side is
zero; for `N=1` it is negative and the actual energy is `mu`. Positivity
therefore covers those sectors. Since both sides commute with N, the
sector inequalities prove the operator statement (1), including arbitrary
coherent superpositions of sectors.

The finite controls below test geometry and constants, not a truncation
of the many-body Hilbert space. Equations (4)–(13) are the all-volume proof.

## 7. Consequences for finite density and a concrete onset test

Let `c0=1/99,090,432`. For any finite-volume state, Jensen's elementary
variance inequality and (1) give

\[
 \frac{\langle H_{\rm mob}\rangle}{V}
       \ge c_0a\left(\rho^2-\frac{2\rho}{V}\right),\qquad
 \rho=\langle N\rangle/V.                                        \tag{14}
\]

For an infinite translation-invariant state with density rho, the same
bound on energy density is `e>=c0 a rho²`: restrict to cubes, apply (14)
to the reduced finite state, and note that replacing open by periodic
boundary terms changes energy by only `O(L²)` in this fixed finite-range,
bounded local model. Thus a fixed positive density cannot have the vacuum's
zero energy density at the closing. This is a ground-energy separation,
not a dispersion theorem about dense states.

Now explicitly change the law to `Hnu=Hmob-nu N`. For any finite-volume
ground state, comparison with the vacuum and (14) gives

\[
                        \rho_0\le\frac{\nu}{c_0a}+\frac2V
                         \qquad(\nu>0).                          \tag{15}
\]

A trial state proves a complementary positive lower bound without a
condensation hypothesis. In a cube of R centers, choose a normalized E1
pair wavepacket with coefficients proportional to
`prod_i sin(pi x_i/(R+1))`, `1<=x_i<=R`, and zero elsewhere. The compact E
pair states at different centers are orthonormal. The immobile stabilized
Hamiltonian annihilates every such superposition, while its exact mobile
energy is

\[
          \tau\,6(1-\cos(\pi/(R+1)))
                            \le\frac{3\pi^2\tau}{(R+1)^2}.        \tag{16}
\]

Choose R so that the last expression is at most nu. Each packet has two
particles and hence trial `Hnu` energy at most `-nu`. Its physical support
is contained in a cube from 0 to `R+1` in each coordinate. Pack such cubes
at spacing `B=R+6`. Distinct physical supports are separated by at least
five sites; no interaction of diameter at most four sees two packets.
The product expectation is therefore the sum of the isolated packet
expectations, with all hard-core exclusions preserved. On a torus one can
place `floor(L/B)^3` packets; the final periodic gap is at least five too.

Using `Hmob>=0`, so `Hnu>=-nu N`, gives

\[
 E_0(H_\nu)\le-\nu\lfloor L/B\rfloor^3,\qquad
 \rho_0\ge\frac{\lfloor L/B\rfloor^3}{V}.                         \tag{17}
\]

For fixed `nu>0` and large volumes, the lower bound tends to `B^-3>0`.
As `nu` decreases to zero one may choose `R=O(sqrt(tau/nu))`, so this
explicit lower bound is of order `(nu/tau)^(3/2)`, while (15) is linear
in nu. In particular all ground-density accumulation values tend to zero
at this onset. This is a rigorous continuous-onset bound at `nu=0`, not
continuity at every chemical potential or an identification of the
finite-density phase. For `nu<0`, positivity gives the unique vacuum.

The parent proposed a separate finite-time local-unitary variational route
which might improve the small-nu lower bound to order nu. That proposal is
not used in (1) or (14)–(17) and has not been checked in this artifact.

## 8. Scope correction and unresolved physics

The predecessor's product rotation `Utheta` is an ordinary unitary on each
finite torus. On `Z³`, a nonzero-density rotated product generally defines
a quasi-local algebra automorphism and a different state representation;
it is not generally a unitary or normal vector in the finite-particle
vacuum Hilbert space used in its section6. This clarification does not
alter its finite-torus spectra or any argument here. The frozen predecessor
has not been edited.

The five exact dilute branches of Hmob remain quadratic. Coercivity does
not turn them into two linear tensor branches, establish a condensate,
eliminate every possible collective low-energy partner in another phase,
or derive continuum gauge constraints. The native finite-density state
and actual readable-record instrument remain unspecified. The earlier
conditional temporal occupation protocol uses an explicitly supplied
Hamiltonian, timing and Born measurement; it is not a framework record law.

Family tuple: **(full hard-core pair amplitudes indexed by residual particle
words; hard-core pins plus three-dimensional box resistance and occupation
localization; uniform density coercivity)**. The finite-density stability
lemma (1) is now closed within this supplied model. It is strictly weaker
than a two-linear-tensor phase and common record/source/action bridge.

A useful next question changes the dynamics/state rather than naming the
desired phase as a premise: in the concrete small-positive-nu law, determine
the symmetry and number of low-energy collective channels with a controlled
finite-density analysis, preserving the full carrier. That is not answered
by the bounds here. A claim of a tensor phase would require new spectral
and observable evidence; no target-equivalent “emergence lemma” is imported.

## 9. Reproduction and evidence coverage

The one priced job was [check_geometry.py](check_geometry.py): under 100 MB
and 30 s estimated, no dense N=3 particle space. It used 0.215 s internally
and 20,004,864 bytes peak RSS on this machine. It independently checks all
admissible partition counts on `L=5,...,64`, distinct expanded sites,
pins inside the expanded interval, free-edge/vertex overlap, volume bounds,
the exact internal projectors, and the integer occupation inequalities.
It also solves ordinary finite graph Laplacians over rational numbers on
boxes of at most 27 vertices to control the resistance conventions, and
checks the constant pair-word geometry on `L=5,6`. The general Poincare
bound is proved analytically, not inferred from those small boxes.

The deadline and stop sentinel were checked before the run; no stop was
requested. BLAS/OpenMP thread counts were one. Actual outputs and resource
use are in [results.json](results.json) and [results.log](results.log).
No source runner, many-body eigensolver, unmanaged worker, PR or audit ran.
The supplied-model assumptions and unchanged main/proposal/primitive
bindings are recorded in [SOURCES.json](SOURCES.json). Files in the earlier
native directories remain untouched.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python3 \
  .claude/science/physics-loops/toe-gravity-law-24h-20260929/native-coercivity-route/check_geometry.py
```
