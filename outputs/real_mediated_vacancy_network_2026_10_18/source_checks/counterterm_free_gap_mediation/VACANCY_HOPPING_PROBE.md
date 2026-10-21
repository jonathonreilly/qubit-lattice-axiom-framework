> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Repulsion-protected vacancy and controlled clock hopping

Status: new bounded author interface, pending distinct check. ROOT proposed suppressing the clock-pair creation channel with a positive double-occupancy penalty. The exact calculation below proves a complete-output primitive with an explicit virtual vacancy phase. It is not an outgoing release construction, a completed gate, or a halt theorem.

The physical composition uses EXACT_ALL_TIME.md SHA `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`. ROOT reports its distinct check accepted; this note reuses its exact stated operator/dressing interface, not a new independent audit. The new clock calculation is derived here with shared ROOT design exposure.

## Exact finite clock Hamiltonian

Let X=X1X2 on the old pair, T=Y_aY_b, and write clock projectors P0=|00><00|, P2=|11><11|. Let

    J_hop=|01><10|+|10><01|,
    N=n_a+n_b,
    H_U=U P2−X T,  U>0.                            (1)

The one-head clock subspace span{01,10} is exactly invariant and H_U there is −X J_hop. On the even clock subspace, conditional on X=p, T|00>=−|11> and hence H_U is

    [ 0   p
      p   U ].                                     (2)

Define

    Omega=sqrt(U²+4), r=(Omega−U)/2=2/(Omega+U),
    alpha=arctan(r), 0<r<=1/U.

The eigenvalues of (2) are −r and U+r. Its normalized lower eigenvector is cos(alpha)|00>−p sin(alpha)|11>. On the even subspace define the real orthogonal matrix

    D_p=[ cos(alpha)    p sin(alpha)
         −p sin(alpha)   cos(alpha) ],

and use identity on the one-head subspace. Combining the two old-X sectors defines a real orthogonal D on the complete old+clock space. Direct multiplication, using r(U+r)=1, gives

    H_U=D H_diag D†,
    H_diag=−X J_hop−r P0+(U+r)P2,
    ||D−I||=2sin(alpha/2)<=alpha<=r<=1/U.           (3)

This is exact; the rotation depends on the old operator X but is only a proof transformation. It is never installed as a higher-body gate.

## Uniform full-output bound and the vacuum phase

In the one-head sector the actual and diagonal propagators agree exactly. In (2), their scalar U/2 and frequency Omega/2 agree; only their Pauli axes differ by angle 2alpha. Consequently the exact full-space difference is

    ||e^{-isH_U}−e^{-isH_diag}||
       =2sin(alpha)|sin(Omega s/2)|<=2/U            (4)

for every real scaled time s. Passive identities preserve the norm. In particular the target on the no-double-occupancy subspace P=P0+|01><01|+|10><10| is the number-conserving generator

    H_low=−X J_hop−r P0.                            (5)

Equation (4) bounds the full output, including actual double-occupancy amplitude, when the initial state is in P. No projection, measurement, or reset is applied. Arbitrary old/clock correlations within P and passive references are allowed.

The virtual shift −r is independent of p because the off-diagonal amplitude in (2) enters through p²=1. For a pure vacancy input the target clock remains |00> and contributes the old-input-independent phase exp(+irs). For a coherent superposition of vacancy and one-head clock states, −r P0 is not a global scalar and must be retained. If one insists on comparing with only −X J_hop, the extra cost is at most |s|r (or exactly 2|sin(rs/2)| on the vacancy component). It is generally not small over arbitrarily long times. Calling the vacancy completely inactive without this qualification would lose a relative phase.

The one-head controlled hopping is exact at the clock level. The protected vacancy is approximate in the actual Hamiltonian and has the explicitly retained virtual energy. Neither statement provides a mechanism that turns a departing clock head into a lasting completed output.

## Bounded number-conserving clock background

Let B be bounded selfadjoint on the same two clock qubits, with [B,N]=0, acting trivially on the old pair. It may mix 01 and 10 arbitrarily. Then H_diag+B preserves P. From (3),

    H_U+B=D(H_diag+D†BD)D†,
    ||D†BD−B||<=2||D−I||||B||.

The two endpoint rotations plus Duhamel give

    ||e^{-is(H_U+B)}−e^{-is(H_diag+B)}||
       <=min{2,(2/U)(1+|s|||B||)}.                 (6)

This also controls the complete no-double-input isometry with target H_low+B|_P. The restriction to a local two-clock number-conserving B ensures P is invariant. A background on a larger head system that conserves only total head number need not preserve this local P; such a network requires its own analysis. No such larger release network is inferred here.

For B=0, the stronger exact all-time bound (4) is available. Equation (6) is a sufficient background estimate, not an assertion that every background causes secular error.

## Actual five-qubit composition and cap

Use the exact mediator parameters from the pinned source:

    l=lambda², x=3l(2−l)/(1−l), g=sqrt(x),
    A0=4+2l+x,
    a_eff=[sqrt(A0+4l)+sqrt(A0−4l)]/2,
    b_eff=[sqrt(A0+4l)−sqrt(A0−4l)]/2,
    c_eff=2lambda+g+2−a_eff,
    0<lambda<=1/1000.

The actual mediator device has K=2I+Z1Z2, two positive YY exchanges, 4n_m and the positive gXX_m exchange, exactly as in the source. Add the positive two-clock block b_eff U P2. If B is also desired physically, separately supply a decomposition B=sum_l B_l into positive real allowed clock blocks; charge their full norms and supports. Without such a decomposition, (6) is only a mathematical background statement, not a positive hardware realization.

For B=0 this is five qubits and six positive real nearest-neighbor blocks. The clock pair a,b already occupies adjacent sites. Each clock-site load becomes 2lambda+b_eff U; the other original loads remain old1:3+2lambda+2g, old2:3+2lambda, and m:4+2g. With positive B blocks add b_eff sum_{l incident v}||B_l|| to the relevant sites. Nothing projects out physical |11>.

Put s=b_eff t. The exact mediator weak-background interface, now using the full clock norm U+||B||, compares the actual complete evolution with

    exp(−it c_eff) exp(−itK)
       exp[−is(H_U+B)] tensor exp(−it2a_eff n_m)

with error at most 164lambda[1+|s|(U+||B||)]. The old aging factor is justified because [K,X]=0 and B is clock-only. Combining with (6), for initial clock support in P, gives the full no-double-output target

    exp(−it c_eff) exp(−itK)
       exp[−is(H_low+B|_P)] tensor exp(−it2a_eff n_m),

with complete vector/isometry error at most

    164lambda[1+|s|(U+||B||)]
                   +(2/U)(1+|s|||B||).            (7)

The initial mediator is arbitrary and can be correlated with the old system and clock. Its target retains the prescribed effective aging, not bare-gap aging or a reset. Passive reference extensions are included. Scalar shifts already present in B remain in its exponential; they must not also be added as an extra phase.

For a fixed scaled horizon |s|<=S and tolerance 0<epsilon<=1, one explicit sufficient allocation is

    U>=8(1+S||B||)/epsilon,
    lambda<=epsilon/[656(1+S(U+||B||))],
    lambda<=1/1000, plus the physical incident cap. (8)

Then (7)<=epsilon/2 and the unhalved complete channel error is <=epsilon. This pays the large repulsion norm in the mediator estimate. It does not treat U as a free infinite projection.

To make cap feasibility explicit, set L=U+sum_l||B_l|| (L=U if B=0). For any Lambda>4 it suffices additionally to take

    lambda<=min{(Lambda−4)/16,
                        sqrt((Lambda−4)/(2L))}.

Indeed g<3lambda and b_eff<=lambda²; every incident load is <=4+8lambda+lambda²L<=Lambda. These small-parameter prescriptions demonstrate simultaneous feasibility, not optimized runtime. The physical repulsion strength is b_eff U and its block norm is charged at both clock sites. No new qubits are needed for this local primitive; a release network would add resources and new proof obligations.

## Next positive interface and limits

The useful new interface is an old-X-controlled one-head hop with a protected, old-input-independent vacancy channel, up to a known vacancy energy. A possible next construction could connect these hops to additional clock positions so that an outgoing head leaves the logical coupling region. That requires an actual larger positive geometry, a full multi-position effective comparison, return/reflection control, and a joint output contract retaining the vacancy phase. The present two-clock calculation does not supply those ingredients or justify summing shared mediator gadgets.

No common-output literal W gate, autonomous release, retention interval, capture, reset, or permanent halt is proved. The supplied local gap, exact mediator calibration, clock repulsion, initial no-double support, positive blocks and observation horizon remain explicit assumptions. This is a new primitive-level derivation and conditional composition, not publication or native dynamics.

ROOT exposed the repulsion route. The even-sector spectrum, rotation, all-time error and background comparison were reconstructed here. The exact mediator interface is reused at the pinned scope; no new independent status is claimed. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication or delegation was used. Only this new source was written; all predecessors remain frozen. Distinct review is required.
