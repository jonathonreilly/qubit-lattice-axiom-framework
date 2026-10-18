# Exactly matched mediator spectrum and uniform complete-output simulation

Status: new analytical candidate, pending distinct check. This uses a DIFFERENT calibrated mediator coupling from the frozen second-order family. It proves exact spectral matching and a uniform all-time full-space propagator estimate. An exact dressing also supplies a weak-background bound. These statements do not solve the clock common-output equations or establish halt, capture, or preparation.

ROOT proposed the characteristic-invariant matching, the projector estimate, and subsequently the polar-dressing route. I reconstructed the sectors, signs, matching equation, constants and operator spaces below. This is shared-design author work, not independent validation. Earlier files remain unchanged.

## Actual positive device and exact new prescription

Use the same five-qubit geometry: old1=(0,0,0), old2=(1,0,0), a_clock=(0,1,0), b_clock=(1,1,0), m=(0,0,1). To avoid confusing clock labels with scalar coefficients, Y_a,Y_b below refer to the clock qubits, while a_eff,b_eff are scalar energies. Set

    Z=Z1Z2, K=2I+Z, Q=X1X2Y_aY_b,
    Z_m=I−2n_m, l=lambda², 0<lambda<=1/1000,
    x=3l(2−l)/(1−l), g=sqrt(x), c=2lambda+g,
    A0=4+2l+x,
    a_eff=[sqrt(A0+4l)+sqrt(A0−4l)]/2,
    b_eff=[sqrt(A0+4l)−sqrt(A0−4l)]/2.              (1)

Install precisely

    H=K+lambda(I+Y1Y_a)+lambda(I+Y2Y_b)
                 +4n_m+g(I+X1X_m).                (2)

All five blocks are real positive and nearest-neighbor on their full supports. The full loads are old1:3+2lambda+2g; old2:3+2lambda; clocks:2lambda each; m:4+2g. Thus any Lambda>4 admits sufficiently small lambda satisfying the incident cap. Counts remain five qubits and five blocks. K occurs once; no old-only counterterm or selected mediator input is supplied.

The exact relation in (1) replaces g=sqrt(6)lambda. In particular it is not an exact-all-time claim for the old prescription. The installed coupling, gap and functional calibration remain explicit suppliers.

## Conserved sectors and actual four-state chains

Write T1=Y1Y_a, T2=Y2Y_b, M=X1X_m and

    H=(4+c)I+A,
    A=Z−2Z_m+lambda(T1+T2)+gM,
    R=ZQZ_m.

R is a selfadjoint involution commuting with A. The YY terms anticommute separately with Z and Q and commute with Z_m. M anticommutes with Z and Z_m and commutes with Q. Hence both kinds commute with their product R. Also

    [lambda(T1+T2)]²=2l(I−ZQ)=2l(I−R Z_m).

In the r=+1 sector the YY term vanishes on Z_m=+1 and is 2lambda times an involution on Z_m=−1. M flips both Z and Z_m. Consequently the four vertices, listed as (Z,Z_m), form a path

    (−,+) -- (+,−) -- (−,−) -- (+,+),

with diagonal energies (−3,3,1,−1) and edge magnitudes (g,2lambda,g). Each vertex has dimension four. Each normalized nonzero edge map is an isometry onto the adjacent vertex: M is an involution; the normalized YY term on its active subspace is an involution. Choosing a basis at one endpoint and propagating it along this path removes all edge matrices. There is no cycle consistency condition. Thus A in this sector is unitarily equivalent to four copies of the real symmetric matrix

    C_+ = [ -3    g       0       0
             g    3    2lambda    0
             0  2lambda   1       g
             0    0       g      -1 ].              (3)

The r=−1 path can be listed with diagonal (3,−3,−1,1) and the same edge magnitudes. Alternating signs on a path reverse all edge signs, so this matrix is orthogonally similar to −C_+. This construction also establishes the full multiplicities; no nontrivial data fiber is silently omitted.

## Characteristic matching

For C_+, direct path calculations give

    tr C_+=0,
    tr C_+²=20+8l+4x,
    tr C_+³=48l,
    det C_+=9+10x+x²−12l.                           (4)

For example the third trace is the diagonal-cube sum, which vanishes, plus 3 sum_edges edge²(d_i+d_j); only the middle edge contributes, giving 3(4l)(4)=48l. The leading principal determinants are −3, −9−x, −9−x+12l, then the last expression in (4).

Consider the commuting target

    A_eff=Z−a_eff Z_m−b_eff Q.                      (5)

Within r=+1 one has Q=ZZ_m. Its four eigenvalues at the vertices of (3) are

    −1−a_eff+b_eff,
     1+a_eff+b_eff,
    −1+a_eff−b_eff,
     1−a_eff−b_eff.

Their trace is zero, with invariants

    tr A_eff²=4(1+a_eff²+b_eff²),
    tr A_eff³=24a_eff b_eff,
    det A_eff=(a_eff²+b_eff²−1)²−4a_eff²b_eff².

Definition (1) gives a_eff²+b_eff²=A0 and a_eff b_eff=2l, matching both traces. The determinant equality reduces to

    24l−4x−12l²+4lx=0,

whose solution is exactly x=3l(2−l)/(1−l). For a four-by-four matrix of trace zero, the characteristic polynomial is

    z^4−(tr C²/2)z²−(tr C³/3)z+det C.

Thus (4)-(5) have identical characteristic polynomials. In r=−1 the target spectrum is the negative of the r=+1 spectrum under (Z,Z_m)->(−Z,−Z_m); Q also changes sign. The matching therefore holds in both sectors, with all multiplicities. Equality of spectra alone is not the dynamical estimate; eigenprojectors are controlled next.

## Eigenvalue labels and projector distances

For 0<l<=10^{-6}, x<=7l. From (1), a_eff>=sqrt(A0/2)>=sqrt(2) and b_eff=2l/a_eff<=sqrt(2)l. Then

    a_eff²=A0−b_eff²>=4+2l+x−2l²>=4,
    a_eff>=2, 0<b_eff<=l,
    0<=a_eff−2<=9l/4.                              (6)

Here a_eff²<=A0<=4+9l was used for the last bound. Hence every target eigenvalue differs from its corresponding bare eigenvalue of Z−2Z_m by at most 13l/4<1/2. The four bare values are −3,−1,1,3, so the correspondence is unique. The actual perturbation V=lambda(T1+T2)+gM has norm

    E<=2lambda+g<= (2+sqrt(7))lambda<5lambda.

It too is much smaller than 1/2. Spectral matching and these disjoint neighborhoods identify the actual and target eigenvalues by the same bare labels, not by an arbitrary permutation.

In each r sector let P_j^0 be the four bare spectral projectors, which are also the target projectors by (5)-(6), and P_j the corresponding actual spectral projectors. Use the radius-1/2 circle about the j-th bare eigenvalue. On this circle the bare resolvent has norm <=2 and the perturbed one <=1/(1/2−E), by the resolvent Neumann series. The resolvent identity and contour length give

    ||P_j−P_j^0||<=E/(1/2−E).                     (7)

The formula applies equally to the rank-four projectors; no simple-eigenvector assumption is used. Since the corresponding eigenvalues agree exactly, their evolution phases agree for every real t. Summing the four projector differences gives, sectorwise and hence on the full direct sum,

    ||e^{-itA}−e^{-itA_eff}||
       <=4E/(1/2−E)<=41lambda, for every real t.    (8)

The final constant uses E<5lambda and lambda<=.001: 20/(.5−.005)<41. There is no time-growing eigenvalue remainder.

## Full complete-output target and mediator aging

Combining (2),(5),(8), define c_eff=c+2−a_eff. Then

    ||e^{-itH}
       −e^{-it c_eff} e^{-it(K−b_eff Q)}
                         tensor e^{-it 2a_eff n_m}||
       <=min(2,41lambda), for all real t.           (9)

Indeed (4+c)I+A_eff=c_eff I+K−b_eff Q+2a_eff n_m. The scalar appears once and K retains its original 2I. The estimate is full-space, including arbitrary correlations and passive extensions. For mixed states the unhalved complete channel distance is <=min(2,82lambda).

No initial mediator state is selected. Independent mediator input gives a common independent evolved mediator factor; correlated input remains correlated under the stated product-unitary target. The mediator aging frequency is the explicit EFFECTIVE 2a_eff, not the bare installed gap 4. Removing that effective shift is not free, especially over arbitrarily long times. There is no mediator reset or all-time fixed output.

For completeness b_eff/l=2/a_eff ->1 as lambda->0, so a prescribed mediated angle has time scale proportional to lambda^{-2}. At that scale (9) still costs only 41lambda. This is simulation of the full Q interaction; it is not a proof that a real product clock implements the literal W with common output.

## Exact dressing and a weak-background corollary

Within each r sector form S=sum_j P_j P_j^0. Then

    ||S−I||<=sum_j||P_j−P_j^0||<=41lambda=:d<1.

Thus S is invertible. Moreover S P_j^0=P_j S and S†S commutes with all P_j^0. The polar factor

    U=S(S†S)^{-1/2}

is unitary and exactly intertwines these projectors. Its singular-value bound is elementary: all singular values of S lie in [1−d,1+d], hence ||U−S||<=d and ||U−I||<=2d<=82lambda. Take the direct sum of these U over r. It follows on the full space that

    H=c_eff I+U H_eff U†,
    H_eff=K−b_eff Q+2a_eff n_m.                    (10)

All matrices used to construct projectors and S are real, so this dressing can be chosen real orthogonal; it is a proof transformation, not an installed operation.

For any additional bounded selfadjoint B, including finite spectators, conjugating B gives ||U†BU−B||<=2||U−I||||B||. Two endpoint terms plus Duhamel give

    ||e^{-it(H+B)}−e^{-it c_eff}e^{-it(H_eff+B)}||
       <=min{2,164lambda(1+|t|||B||)}.              (11)

If B=b_eff B0 and |t|<=A/b_eff, this is <=164lambda(1+A||B0||). When B0 acts trivially on m, the comparison factors into mediator aging e^{-it2a_eff n_m} and the old+clock/spectator generator K+b_eff(B0−Q), retaining the scalar c_eff. Noncommutation with K is allowed, but that latter exponential must not be split without justification.

As elsewhere, an actual positive real nearest-neighbor background must be supplied as such, with full-support incident loads paid. For a real clock-pair matrix C, b_eff(C+d0I), d0=max(0,−lambda_min(C)), is a positive sixth block. Charge b_eff||C+d0I|| to both clocks, use ||C+d0I|| in (11), and add b_eff d0 to the common target scalar when writing its generator with C. This gives a clock-background interface; it does not solve its fixed-difference matrix equations.

## Limits, provenance and frozen-source separation

This exact new functional calibration and effective b_eff replace the previous g=sqrt(6)lambda and second-order coupling lambda². Neither numerical precision of the relation nor immunity to coefficient mistuning is asserted. The installed positive gap, literal K, block signs and coefficient supply remain premises. All-time operator simulation means tracking a nontrivially evolving target; it does not mean permanent halt, stationary output, or completed literal gate at all times.

Source context: PROPOSAL.md SHA739a1961076d52b0e26364bd858f957a89a233bfa72aa652efa193ef54ac2cdd and ALL_MEDIATOR_INPUTS.md SHA206d91616f9b66da958c73caf2b723733fe850fa03ca7b16b83fd78e955290e9 supply the previous actual geometry and notation, not a premise for the newly matched spectrum. Their full arguments were authored/read earlier and remain unchanged. This note reconstructs its own exact chain, invariants, projector proof and dressing. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication or delegation was used. Only this new source was written. Independent checking is required before promotion.
