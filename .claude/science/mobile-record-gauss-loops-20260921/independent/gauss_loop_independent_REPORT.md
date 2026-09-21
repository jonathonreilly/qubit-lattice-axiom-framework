# Independent Gauss-loop construction and source comparison

The supplied collective construction preserves exact centered divergence,
immutable labels and hard site capacity, and permits departure followed
by fresh formation. Its first fixed-volume fugacity coefficients are as
given below. The authorized primary note and two checkers agree with the
independent calculation. I found no unresolved mathematical discrepancy
in their stated finite claims.

This is a conditional construction check, not a phase theorem or audit
verdict. The first derivation and ten exact control groups were sealed
before reading any primary Gauss-loop file. BLIND_DERIVATION.md contains
the detailed proof; this report incorporates the results and the subsequent
complete comparison with the five authorized files.

## 1. Local constraints and immutable collective events

For a signed record at r along axis i, D2 sees the incidence of the
length-two link with endpoints r-e_i and r+e_i. The supplied four-record
loop cancels its eight incidence terms pairwise at the four plaquette
corners. Thus D2E=D2B=0, for either species, every plane and both
circulations.

With unnormalized lattice l2 norm and D=D2/2, a nearest-neighbor swap has

    ||delta DE||^2+||delta DB||^2
       =|E(arriving)-E(departing)|^2
        +|B(arriving)-B(departing)|^2.

The impulse columns for different components have disjoint supports, and
each has four coefficients of magnitude 1/2. Distinct labels therefore
give squared norm 1, 2 or 4 in the thirteen-state menu. For D2 these squared
norms are four times larger. A norm averaged over volume is smaller by V.
This is a statement about one swap with this encoding, not other encodings
or collective moves.

Every one-step translation of the whole loop has four disjoint vacant
targets and transports each label unchanged. The difference between
translated and original loops is divergence-free. Simultaneous reversal
by the two opposite-site swaps is also divergence-free; either half by
itself is not. A constrained Markov reversal must be a joint event.

A verified history is empty -> A loop at c -> same A records at c+e3 ->
new B loop at c, using an e1/e2 loop. The final eight sites are distinct
and both fields remain divergence-free. No existing record is erased.
In a background configuration all stated target-vacancy conditions are
essential; uncongested mobility does not imply mobility at arbitrary density.

## 2. Fixed-volume fugacity law and complete leading covariance

Let V=N^3, with N odd and N>=7, and put
mu_z proportional to zA^nA zB^nB 1[D2E=D2B=0].
The following are expansions at fixed N near (zA,zB)=(0,0), with
q=|zA|+|zB|:

    Z_N=1+6V(zA^4+zB^4)+O_N(q^6),
    E_mu[nA]/V=24zA^4+O_N(q^6),
    E_mu[nB]/V=24zB^4+O_N(q^6).

Proof of the minimal-support count: for each species a balanced directed
flow on the step-two graph decomposes into cycles. Multiplication by two
is invertible modulo odd N. On this cubic N-torus, N>=7 excludes cycles
of length three or five; every four-cycle is a coordinate plaquette.
The capacity rule forbids using both orientations of one edge. The
minimal nonempty fields are therefore the 3V plaquettes in two
orientations, giving 6V states per species. Each nonempty species costs
at least four records. Normalization affects no displayed leading term.

Use Ehat(k)=V^-1/2 sum_x exp(-ik.x)E(x), k=2pi m/N, and the same convention
for Bhat. Both means are zero. The E/B cross covariance is exactly zero,
since flipping all E labels is a symmetry without changing B. Translation
invariance makes the Hermitian covariance diagonal in the wave vector.

For s_i=sin(k_i),

    Cov(Ehat(k))=8zA^4 (|s|^2 I-s s^T)+O_N(q^6),
    Cov(Bhat(k))=8zB^4 (|s|^2 I-s s^T)+O_N(q^6).

Indeed an ij loop has amplitude
(2i/sqrt(V))exp(-ik.c)(s_j e_i-s_i e_j). Summing all centers and both
circulations gives the displayed factor eight. The independent checker
verifies the entire tensor as exact Laurent coefficients, without
floating Fourier tolerances. The component variance at one site is
8zA^4 (or 8zB^4), consistent with density divided by three.

For every nonzero mode the exact constraint is s.Ehat=s.Bhat=0, and the
leading matrix has rank two. The amplitude is proportional to |s|^2;
it is not a constant-amplitude transverse projector at small k.

**The zero mode requires its own expansion.** Odd N eliminates staggered
zeros of the centered symbol, but its k=0 zero remains. A straight winding
line of N equally oriented records is admissible and has total vector
+/-N e_i. The first nonzero zero-mode coefficients in the full constrained
ensemble are

    Cov(Ehat(0))=2N zA^N I+O_N(q^(N+2)),
    Cov(Bhat(0))=2N zB^N I+O_N(q^(N+2)).

For each axis there are N^2 lines and two orientations, each contributing
N^2/V to that covariance. A nonzero total flow is a multiple of N and
requires at least N records; equality forces a straight line. Population
N+1 is excluded by the parity of the total signed step counts. These
facts also control the next possible order. Direct N=7 summation gives
14I from 294 winding configurations per species.

This does not contradict the primary checker's zero quartic coefficient
at k=0; it prevents interpreting that coefficient as an identically zero
mode of the full ensemble.

## 3. Exact compact-phase integral; no independent XY factorization

The exact Kronecker-delta representation is

    Z_N = integral product_x [dtheta_x dphi_x/(2pi)^2]
          product_r [1
            +2zA sum_i cos(theta_(r-e_i)-theta_(r+e_i))
            +2zB sum_i cos(phi_(r-e_i)-phi_(r+e_i))].

Each phase lies in [0,2pi). Global phase-shift redundancies add no missing
normalization. The hard capacity rule gives a sum of the vacancy and
twelve occupied alternatives at each site, not independent A and B
factors or independent bond factors.

For zA+zB<1/6 all local factors are positive. This yields a positive
coupled compact-phase weight in that range, whose logarithm includes
mixed-species and multi-bond terms. It does not yield a factorized
positive XY measure. For general positive fugacities even the full
integrand need not be nonnegative.

An explicit global phase assignment, not merely independently chosen
one-site arguments, proves this: on N=7 take theta=pi at +e1,+e2,+e3
and zero elsewhere, phi=0 everywhere, zA=1/4,zB=1/100. The product
has one factor -11/25, three factors 14/25, nine factors 39/25 and
330 factors 64/25, hence is negative.

As a separate exact capacity control, enumerate all 13^4 assignments on
one diamond and hold all other sites vacant. Only the empty state and
the two A/two B circulations survive, giving
Z_restricted=1+2zA^4+2zB^4. Species factorization would introduce the
forbidden term 4zA^4 zB^4.

## 4. Dynamical and thermodynamic scope

The full constrained fugacity ensemble and the states accessible from
empty are different objects. Loop translations and reversals preserve
all label counts; each loop birth increases one species count by four.
All permitted births have zero total vector. Thus empty-start dynamics
preserves zero total E and B and nA=nB=0 modulo four. The full mu_z
contains nonzero winding sectors and admissible six-record rectangles
with zero flux but species population six. The latter is an explicit
counterexample to accessibility even after merely restricting to zero
global flux.

With births off, the primary note's equal-rate reverse translations and
self-inverse reversals give eventwise detailed balance for every homogeneous
positive product law. Conditioning on any nonempty charge sector preserves
that property. In particular mu_z is an invariant conservative law. This
does not prove uniqueness, sector mixing or convergence from a specified
initial state. With births on it is not invariant: the empty state has
outgoing births and no incoming transition. The primary note correctly
separates these statements.

The geometry and swap norm in the primary note require only its stated
N>=5. The stronger odd N>=7 hypothesis is needed for the simple fugacity
remainder above: N=5 has winding terms of degree five; even tori have
extra centered-symbol zeros and can have shorter step-two winding cycles.
No coefficient uniformity or thermodynamic claim should silently extend
across those distinctions.

The fixed-volume series does not establish a uniform thermodynamic
expansion, phase stiffness, a Coulomb covariance, algebraic long-distance
correlations, or a collective wave. Its remainders are not controlled
uniformly in N. A uniform expansion or separate phase/mixing theorem
would be needed. This check does not undertake that remaining problem.

## 5. Complete authorized-source comparison

After the blind seal, I fully read the 231-line primary note, 134-line
local checker, 84-line fugacity checker and both complete RESULTS JSON.
No other primary campaign source was accessed.

The finite claims agree. In particular:

- The primary note explicitly changes the old fifteen-state alphabet to
  the new thirteen-state one. Its fifteen-label impulse check is a
  separate application of the universal norm identity, not accidental
  use of the old B cube orbit in loop counting.
- Atomic translations, joint reversal, target capacity and persistent
  identity history are correctly stated. Full signed-cubic covariance
  holds for polar A and axial B templates. An additional exact control
  checks actual template membership under all 48 actions at N=5 and 7.
- The conservative conditional-law proof is valid despite reducibility.
  On macroscopic time the total density rate is
  16beta sum_planes P(four vacant sites), giving 48beta initially.
  No product closure is used.
- The loop birth bracket is
  Q_E=Q_B=8beta(|s|^2 I-s s^T), Q_EB=0 at vacancy. At another state
  each positive-semidefinite template contribution is multiplied by its
  vacancy indicator. The stated upper bound and combined trace
  32beta|K|^2/N^2 at k=K/N follow. This proves a noise bound, not a
  fluctuation limit or state-selection theorem.
- The isolated loop center has eigenvalue
  -2kappa sum_i(1-cos k_i). The source correctly specifies a center
  observable. A circulation-odd observable also has reversal decay
  -2nu; the selective check makes this distinction explicit.
- The fugacity checker counts 2058 four-record states at N=7 and obtains
  the same density and covariance coefficients. Its numerical Fourier
  comparisons are labeled numerical. Its phase test is explicitly
  one-site algebra; the independent global signed example above is
  additional evidence, not a correction to that stated scope.

The checker-results hashes match their scripts and record 13 and six
successful primary groups. I authenticated them rather than rerunning
for counts. The new post-seal checker completed seven selective groups.
Neither those counts nor byte identities replace the proofs.

No scientific correction to these frozen primary files is required by
this review. Their then-current phrase “independent reconstruction pending”
can be updated to reference the completed evidence; that is provenance,
not a mathematical repair. The zero-mode, accessibility and phase
distinctions above should accompany any extension or publication of the
fugacity claims.

## 6. Identities and evidence

Blind derivation SHA-256:
0f129dafac85c925d18e822ee88e009731af50febbfbf91c8d1aa3c5cb5898fe

Pre-source seal SHA-256:
c08bc205347df4c93f12439738293e336361935e6192f2cc1544ee02e67de817

Authorized primary source SHA-256 values:

    MICROSCOPIC_GAUSS_IMPULSE_AND_RECORD_LOOPS.md
    684f10acda3ebf659ed4b1b47e3fbe35a29c92dfbe1fee77e9cd9469b27f0c30
    microscopic_gauss_record_loop_check.py
    dea415ec4d6be7662efff041bd7e303c03c9b0243548cbc429552f4478f616b9
    gauss_loop_fugacity_check.py
    f1c6921b5dc887b4de59bbfccee5e5cad1e11dfd97270864472dfdab426908e0
    MICROSCOPIC_GAUSS_RECORD_LOOP_RESULTS.json
    3d5a46d78fd0958df7d5b79bbdcb6ed15e9ee35decb073989d2d6fd5474987b3
    GAUSS_LOOP_FUGACITY_RESULTS.json
    1a0d8e2a71b53a28ef574998c7b297f8c7062cffc4b98da616bbe2323c761cdb

blind_check.py and comparison_check.py are independently written and
reproducible from this directory. Their complete raw logs and JSON outputs
are preserved. There were no failed executions. PRE_SOURCE_SEAL.json
binds the four blind artifacts; FINAL_SEAL.json binds every final artifact
and the authorized source identities. No external literature, additional
agent, production edit, Git/PR/audit action or model change was used.
