# Dark-vacuum two-body ladder: a certified on-shell approximation to W

Status: conditional mathematical support for a stationary scattering fiber.
The normalizable-input, all-future autonomous-operation theorem remains open.
This is an exploratory source proposal, with author calculations and a different
assembly/path check; it has no independent reviewer or retained audit status.

There is a concrete finite-coefficient, strictly nearest-neighbor two-body
Hamiltonian whose four elastic reflection amplitudes at one specified momentum
obey

    ||R(k0) - alpha(k0) W|| < 5.2e-13,
    W = ((9+12i)I + (-16+12i)X1X2)/25,
    alpha(k0) = r_(s=-1,p=-1)(k0), |alpha(k0)| = 1.

The bound is certified by exact rational residual calculations, not by the
optimizer's convergence report. Both old energies, both XX labels, all source
channels and the clock reflection phase are retained. No W is put in a hopping
bond. The source vacuum is exactly dark away from the two clock contacts.

This supplies a useful stationary ingredient for the renewal5 target. It does
not yet replace PR9657's external stop: a plane wave is not a normalizable ready
clock, the apparatus uses an infinite half-line, the added strength budget is
larger than PR9656's, and finite-time source return has not been bounded here.
No arbitrary-accuracy family follows from this one calibrated point.

## Source contract and provenance

The sole campaign contract is the frozen copy in `sources/TARGET_CONTRACT.md`,
originally at
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/TARGET_CONTRACT.md`.
This ROUTE file is the requested worker deliverable, not a replacement campaign
checkpoint. All writes are confined to this worker directory.

Scientific source revision: `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc` in
`correlation_worktree`. Supplied current-main authority:
`5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`. No network refresh was authorized.
`sources/MANIFEST.json` binds the saved exact source bytes. In particular:

- PR9656 note, `PRODUCT_SOURCE_MEDIATOR_BOUNDED_THEOREM_NOTE_2026-10-16.md`:
  SHA256 `4e68ea3c55620eb0ad3c721084780d2af44bc5eaa249cb8c205e516575189d20`.
  Its construction, scalar, product source, window, resource limits and
  controlling qualifications were read, principally lines17-220 and579-700.
- PR9657 note, `PRODUCT_SOURCE_CONTROLLED_STOP_BOUNDED_THEOREM_NOTE_2026-10-16.md`:
  SHA256 `b25d812dc1a4cdad2959f003ddd36346f2de0058292c74c7d0e07c9c5e395a4d`.
  Its overview, external-stop/C1 arguments and controlling qualifications were
  read, principally lines19-66,161-293,1123-1160. Its external switch-off and
  exact-zero endpoint are the interface being replaced, not resources obtained
  by this calculation.
- The current science workflow, physics-loop entry point and relevant
  Discovery/Claim Status/Delivery references were read. The installed skill
  entry point differed from the chosen repository revision; the repository
  entry point was then read and used. Its three read references were identical.
  The task's explicit no-network/no-commit/no-PR and sole-checkpoint instructions
  control delivery. No full campaign or audit workflow was launched.

The present scattering calculation does not import PR9656's perturbative
corrector theorem: it uses the literal K and target W as its design specification.
The registered primitive list was inspected. None of its units, kinetic-isotropy
or pointwise-state primitives supplies these dimensionless couplings, a ready
clock, a Hamiltonian law or a source preparation mechanism; those remain stated
conditional resources. No primitive or axiom is added.

A bounded local prior-art search at the supplied main ref used
`dark.{0,30}vacuum|vacuum.{0,30}dark|closed.{0,20}channel|multichannel.{0,20}scatter`
and `scattering.{0,30}(clock|mediator)|boundary.{0,30}reflection|reflection.{0,30}phase`
over `docs/*.md`. The returned lines concerned cosmology, unrelated channel
closure, reflection positivity, lattice-gas clocks or finite spin clocks.
They did not supply this dark-source stationary construction. This is not a
global novelty claim. The contract's existing half-line gate-bond clock remains
prior art for approximate completion, and is not rebranded as the present result.

## Physical operator and square-ladder embedding

Put old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0), and clock site
c_n=(n,2,0), n=0,1,... . Every non-onsite term below lies on a cubic nearest-
neighbor edge. There are six entrance qubits and an infinite blank clock tail.

Let n=(I-Z)/2 and a=|0><1|. Write h for the auxiliary hopping coefficient and
tau for physical time. Define

    K = 2I + Z1 Z2,
    L_AB = a_A^dagger a_B + a_B^dagger a_A,
    C = DeltaA nA + DeltaB nB + h(nA+nB-L_AB) + u nA nB,
    G = gA nA(I+X1) + gB nB(I+X2),
    H_clock = J n_c0
            + J sum_(n>=0)[n_cn+n_c(n+1)
                            -a_c(n+1)^dagger a_cn-a_cn^dagger a_c(n+1)],
    H = K + C + G + H_clock
        + lambdaA n_c0(I+XA) + lambdaB n_c1(I+XB)
        + mu0 n_c0 + nu(I-n_c1),       nu=-mu1>0.

Every displayed physical block is positive. The hopping block has source
eigenvalues 0,0,2h,2h; nA(I+X1), nB(I+X2) and the clock/source blocks are
positive because their commuting factors are positive. No projector on the
global one-head sector appears in H. Clock number is preserved, and the
operation is considered in its supplied one-head input sector.

In that sector H_clock is exactly `2J I - J(S+S*)` on the half-line, with a
Dirichlet boundary at -1. The endpoint `J n_c0` is essential for its constant
2J diagonal and is included in the resource count. Fixed clock-number sectors
are bounded, with `0<=H_clock<=4J N_clock`. Adding the finite old/source and
contact operators gives bounded positive restrictions; their orthogonal direct
sum is a nonnegative selfadjoint realization on the finite-excitation clock
representation. The infinite prepared tail and this representation are supplied.

For source vacuum v=|00>, `(C+G)(psi tensor v)=0` exactly for every old psi.
When neither clock contact is occupied, the source cannot be excited and the
added old interactions vanish on that sector. There is no persistent effective
old interaction hidden in a dark-sector energy shift. The old term remains
literal K. During a collision `[H,K]` need not vanish: the old-energy claim is
about asymptotic elastic channels, while the complete static H is conserved.

The positive vacancy block is `nu I + mu1 n_c1`. The scattering algebra below
subtracts only the explicitly retained common scalar nu. Physical time evolution
therefore has the extra factor `exp(-i nu tau)`, and physical total scattering
energies are the displayed E plus nu. This scalar must be part of the clock
output/comparator; it is not dropped as free phase control.

The supplier differs from PR9656's. It requires occupation-conditioned old X
couplings, source hopping/penalties, two clock/source contacts and specified
clock onsite projectors. This is an explicit conditional Hamiltonian, not a
derivation of those couplers from the microscopic axioms or original actuator set.

## Exact finite reduction and all channel thresholds

The full bulk internal Hamiltonian is B=K+C+G, dimension16. It commutes with
P=X1X2. For p=+/-1 choose the old basis so that ZZ=Z, X1=X and X2=pX.
For example its unnormalized s=+ and s=- vectors are respectively
`|00>+p|11>` and `|10>+p|01>`. In source order00,01,10,11 the resulting block is

    B_p = I4 tensor (2I+Z) + C_p tensor I + F_p tensor X,
    C_p = (DeltaA+gA)nA + (DeltaB+gB)nB
          + h(nA+nB-L_AB) + u nA nB,
    F_p = gA nA + p gB nB.

This 8x8 identity is checked exactly against a separately assembled full
four-qubit Pauli operator in `independent_check.py`. Its vacuum energies are
1 and3. Source excitation number is conserved by B, so its remaining eigenvalues
have the following exact description. Let

    aA=2+DeltaA+h+gA,  aB=2+DeltaB+h+gB,
    xA=lambda-aA,     xB=lambda-aB.

The four one-source-excitation eigenvalues are the four roots of

    (xA*xB+1+p*gA*gB-h^2)^2 - (xA+xB)^2
      - (gA*xB+p*gB*xA)^2 + (gA-p*gB)^2 = 0.

The remaining two are

    2+DeltaA+DeltaB+2h+u+gA+gB +/- sqrt(1+(gA+p*gB)^2).

The quartic is checked against the exact rational characteristic polynomial.
For the fixed coefficients, all sixteen bulk eigenvalues are, rounded here:

| p | Eight eigenvalues of B_p |
|---|---|
| +1 | 1, 3, 6.671573387110, 34.169062964188, 46.681890304244, 66.392282238574, 79.043854253349, 126.164916518934 |
| -1 | 1, 3, 14.130637131516, 18.540987107274, 58.828927362578, 75.065829307524, 86.098948786312, 106.458249971196 |

Every eigenvalue b supplies the bulk clock band `[b,b+4J]`, with the common nu
added physically. Full numerical band endpoints are saved in
`evidence/different_path_check.json`. Channel closure uses an analytic bound,
not those rounded eigenvalues. If Q excludes source vacuum, positivity gives

    Q B Q >= (1+min(DeltaA,DeltaB)) Q.

For this witness

    4J = 1.555612607490684,
    min(DeltaA,DeltaB) - 2 - 4J > 1.11106871217564,
    2 - 4J > 0.44438739250931.

Thus both entire incoming vacuum bands `[1,1+4J]` and `[3,3+4J]` lie below
every source-excited band; the two vacuum bands are also disjoint. The possible
release of two units by old relaxation is fully paid. For each fixed p, s and
interior k there is exactly one open channel at `E_s=2+s+2J(1-cos k)`.
At the certified k0, `E_-=2.553124953460740...` and
`E_+=4.553124953460740...`, before adding nu. Both parity sectors are included.

## Stationary reflection algebra

Set z=exp(ik), epsilon(k)=2J(1-cos k), and E=2+s+epsilon(k). For a bulk
eigenvalue b define D_b=b+2J-E and choose the solution of

    r_b + r_b^-1 = D_b/J

that is z in the single open channel and has |r_b|<1 in each closed channel.
For closed channels this gives the real branch

    F_b = -J/r_b = -(D_b+sign(D_b)*sqrt(D_b^2-4J^2))/2,

while the open value is `F_open=-J conjugate(z)`. Functional calculus gives
F_p(E) on the 8-dimensional bulk internal space. There are no open source
channels, so this accounts for every asymptotic channel.

Let `V_A=lambdaA(I+XA)+mu0 I` and
`V_B=lambdaB(I+XB)+mu1 I`, including identities on the old coordinates.
For incoming unit vector e_s in vacuum at reference site c1, the two boundary
vectors x0,x1 solve the exact finite system

    M_(s,p)(k) [x0;x1] = [0; 2iJ sin(k) e_s],
    M = [[E-2J-B_p-V_A, J I8],
         [J I8,          F_p(E)-V_B]],
    r_(s,p)(k) = <e_s,x1>-1.

The lead solution for n>=1 is the open incoming wave `z^(-(n-1))e_s`, its
outgoing reflected wave and all the decaying closed eigenchannels. This fixes
the orientation and common propagation phase. Invertibility of M at k0 is
certified below. A discrete-current identity for a Hermitian nearest-neighbor
Hamiltonian equates incoming and outgoing flux: the closed real roots carry
zero current and the endpoint carries none. Hence `|r_(s,p)|=1` exactly.
There is no channel to discard in this statement. The fiber operator R(k0) is
diagonal in the four joint (ZZ,XX) eigenstates and commutes with K.

Since W has eigenvalue `w_+=(-7+24i)/25` for p=+1 and `w_-=1` for p=-1,
the four certified scalar differences yield the displayed full old operator
norm bound. Tensoring a passive reference preserves that norm. This is a
stationary scattering-fiber assertion; it does not normalize a monochromatic
plane wave or create a finite ready state.

## Fixed rational witness and certificate

The following terminating decimals are exact inputs. Define

    q = 0.040021355301287,
    cos(k0)=(q^2-1)/(q^2+1), sin(k0)=2q/(q^2+1),
    epsilon0=2J(1-cos(k0)),
    DeltaA=2+epsilon0+1/20+1.143803166553335,
    DeltaB=2+epsilon0+1/20+1.063556366205592.

| coefficient | exact value |
|---|---:|
| J | 0.388903151872671 |
| gA | 19.999998155265832 |
| gB | 9.869584235578144 |
| h | 19.999999311960544 |
| lambdaA | 0.359303251635283 |
| lambdaB | 2.497330381697014 |
| u | 14.99540892430831 |
| mu0 | 0.520036275799164 |
| mu1 | -0.151066135275764 |
| nu | 0.151066135275764 |

The JSON stores exact fractions for every coefficient and energy. The source
penalties need more than the 10^15 coefficient grid because they contain the
rational epsilon0. These parameters are calibrated to the supplied target W;
no prediction or microscopic derivation of the numbers is claimed.

`certify_point.py` uses 90-decimal mpmath values only to propose matrices rounded
to denominator10^55. All certification arithmetic is exact Python Fraction
arithmetic. For each 6x6 source-excited block let

    D=B_Q+2J-E, A=D^2-4J^2 I, D>=d I, d>2J,
    S_hat = proposed positive square root,
    b=d-||S_hat-D||_infinity >0,
    a=d-2J >0.

The exact residual bounds the true positive square root S by

    ||S_hat-S||_2 <= ||S_hat^2-A||_infinity/(a+b).

Indeed `S_hat(S_hat-S)+(S_hat-S)S=S_hat^2-S^2`; the inverse Sylvester map is
the integral of `exp(-t S_hat) R exp(-t S)` and has norm at most1/(a+b).
Symmetry bounds the residual's spectral norm by its maximum row sum. Multiplying
the root error by3/2 safely bounds the 6x6 F-block infinity-norm error because
sqrt(6)<3. The other closed vacuum channel uses the analogous scalar residual.

For rational M_hat and inverse proposal N, exact
`gamma=||I-M_hat N||_infinity<1` gives
`L=||N||_infinity/(1-gamma)`. If the certified M error is delta and L*delta<1,
then `||M^-1||_infinity<=L/(1-L*delta)`. A separately rounded state x_hat obeys

    ||x-x_hat||_infinity
      <= [L/(1-L*delta)]
         (||M_hat x_hat-b_rhs||_infinity + delta ||x_hat||_infinity).

Complex row sums use `abs(real)+abs(imag)` as a conservative upper bound.
All positivity and Neumann conditions are asserted by exact comparisons.
The largest certified inverse bound is1033.45652395759; the largest resulting
reflection-amplitude certificate error is below9.7e-50. The larger target
error below5.2e-13 is the actual mismatch of the fixed rational design, not an
arithmetic uncertainty. Alpha is the exact unit-modulus r_(-1,-1), and the
certificate compares each amplitude with alpha*w_p; it does not fit away
separate old-energy phases.

The unrounded floating search, including failed starts, is preserved separately.
One contact did not match W in its stated bounded search; this is not a no-go.
Two contacts with nonnegative clock potentials reached a residual0.003368 in
the saved search. Allowing mu1<0 produced the saved floating fit, which motivated
the distinct positive vacancy-projector resource and the rational certificate.
Search success is not the certificate and search failure establishes no exclusion.

## Strength and preparation resources

These are sums of norms of the separately supplied incident positive blocks,
with literal old K additional. The source-edge hopping is counted as the one
displayed positive two-qubit block; splitting it into other actuators changes
that convention and must be recounted.

| site | added incident block-norm sum |
|---|---:|
| old1 | 2gA = 39.999996310532 |
| old2 | 2gB = 19.739168471156 |
| A | DeltaA+2gA+2h+u+2lambdaA = 100.460938482046 |
| B | DeltaB+2gB+2h+u+2lambdaB = 84.395918102446 |
| c0 | 3J+2lambdaA+mu0 = 2.405352234688 |
| c1 | 4J+2lambdaB+nu = 6.701339506160 |
| later clock sites | 4J = 1.555612607491 |

The old edge has norm3. All strengths are finite; there is no infinite-penalty
limit or hidden three-body cancellation. The original added cap2 is not met.
The precise couplings, calibration, occupation-conditional directions, source
product initialization, one-head clock input, infinite blank tail and energy/time
units remain supplied. Static coefficients have zero runtime slew; this says
nothing about fabrication, installation, source/clock preparation work or renewal.

## Different-path author check and actual execution

`independent_check.py` assembles the literal four-qubit Pauli operator, checks
vacuum darkness and the two symmetry blocks with exact fractions, and checks
the one-excitation quartics. It then solves full16-internal-channel finite leads
of lengths12,20,32. Only the open vacuum channel has an outgoing termination;
all closed channels terminate at a hard wall. This calculation never evaluates
the closed-channel surface square root. At length32 its two old-energy results
agree with the certified surface amplitudes within2.7e-13 in double precision;
the largest matrix dimension is512 and each solve has two right-hand sides.
The length12 lower-energy discrepancy2.89e-11 decreases at length20. These are
numerical checks of a different implementation/path, not independent review or
a proof of a finite-clock horizon.

All executed scientific programs exited0. Full stdout and stderr are retained
under `evidence/`; empty stderr files remain present. Versions: Python3.13.5,
NumPy2.4.4, SciPy1.17.1, SymPy1.14.0, mpmath1.3.0. Commands set
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`; no assertion about measured hardware
thread use is made. Search caps were80 and120 starts, each with SciPy
`max_nfev=350`, and a180-second checkpoint between starts. Finite-difference
calls are additional to SciPy's reported nfev; no total call count was measured.
Refinement used `max_nfev=12000` and reported nfev363. Source/internal/boundary
dimensions are16/8/16 as stated; the largest finite-lead solve is512. Actual
elapsed times and all optimizer results are in the respective JSON files.

Reproduce from this directory, in order:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 certify_point.py
    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 independent_check.py

The certificate uses the preserved refinement file to select its rational point.
The exact chosen point is also completely specified above and in its JSON. The
discovery programs `probe.py`, `probe_ladder.py`, `refine_ladder.py` are retained
for provenance, but do not need rerunning to inspect this fixed certificate.

## Precise next theorem and unproved joins

The next target is a full joint norm inequality for a normalized, independently
specified clock packet f initially placed a finite distance from the contacts:

    sup_(tau>=T_ready) || exp(-i tau H) J_f
       - [exp(-i tau K) W] tensor |00>_AB tensor chi_out(tau) || <= eta.

Here J_f appends the SAME source vacuum and clock f for every old/reference
input, and chi_out includes `exp(-i nu tau)`, actual reflection phase alpha(k),
clock dispersion and the chronology of launch. All outputs remain. This theorem
is not proved by the point certificate. Necessary steps are:

1. Certify a compact momentum interval around k0, separated from0,pi and all
   thresholds, on which all four boundary matrices stay invertible. The bulk
   closure inequalities above are already uniform over the whole clock band;
   they do not themselves bound a contact resonance or its derivatives.
2. Bound derivatives of the closed-channel roots, inverse matrices and the four
   reflection functions. Then bound
   `sup_k ||R(k)-alpha(k)W||` on the packet support. Narrowing support has a
   localization/time cost and does not convert this fixed nonzero calibration
   residual into arbitrary accuracy.
3. Construct normalized incoming/outgoing generalized-eigenfunction transforms
   with their exact normalization and phase orientation. Prove their comparison
   with the independent finite-distance product input. An exact scattering
   state is generally correlated near the contacts and cannot simply be called
   an independently prepared ready state.
4. Control all closed-channel, incoming and near-contact tails uniformly for
   every tau>=T_ready, including arbitrary old superpositions and references.
   Closed asymptotic channels mean zero outgoing excitation flux, not exactly
   zero source occupation at a finite time. A rate or explicit computable bound
   is still needed.
5. Account for localized/bound states, possible threshold singularities and
   the overlap of the actual finite-distance prepared packet with them. No
   bound-state inventory, absence theorem or uniform overlap estimate was run.
   A boundary inverse certified at one continuum energy does not settle this.
6. For a finite clock, replace the infinite-tail assertion by a quantified
   horizon and a finite-boundary error. The finite linear solves above are
   stationary cross-checks, not a dynamical recurrence or horizon theorem.

These are analytic and preparation obligations for this explicit model, stronger
than its stationary-fiber statement but substantially more specific than the
original arbitrary-supplier question. The exact calibration equation or a
certified tunable family would additionally be needed for arbitrary requested
accuracy below this fixed point's residual. Nothing here asserts finite-time
exact permanent capture, permanent classical Records, reset or indefinite reuse.

The next useful action is a fresh check of the rational certificate and the
channel/phase derivation, followed by a quantitative packet theorem for this
same fixed Hamiltonian. Source identities and the failed single-contact route
should be retained. No shared source, editable prompt, axiom, audit state, Git
commit, push, PR or other chat was changed by this worker.
