# Weak bounded backgrounds for the counterterm-free mediator

Status: new conditional author extension, pending distinct check. The underlying source PROPOSAL.md, SHA256 `739a1961076d52b0e26364bd858f957a89a233bfa72aa652efa193ef54ac2cdd`, remains unchanged. ROOT has read that source and its distinct check is running. The calculation below uses its explicit full-space conjugation and remainder bounds, not an assumption of exact effective dynamics. It does not solve the clock-assembly problem.

## Scope and retained actual device

Let H be exactly the five-qubit positive Hamiltonian of the source,

    H=K+lambda(I+Y1Y_a)+lambda(I+Y2Y_b)
          +4n_m+sqrt(6)lambda(I+X1X_m),
    K=2I+Z1Z2, Q=X1X2Y_aY_b, 0<lambda<=1/1000.

Let B0 be bounded selfadjoint on old+a+b and optionally a finite spectator system S, acting as identity on m. Install the additional mathematical background lambda² B0. B0 need not commute with K, Q, either old parity, or either clock occupation. S may be initially correlated arbitrarily with the old and clock inputs. A further passive reference is unaffected throughout. The conclusions also hold for any bounded B0 commuting with n_m, replacing B0 in the selected target by its m=0 block; the physical premise considered here is the simpler identity-on-m case.

The actual generator is H_B=H+lambda² B0. Positivity and nearest-neighbor realizability of this background are separate supplier conditions stated below; bounded selfadjointness alone does not imply them.

## Conjugation and remainder

Use H0=K+4n_m, c=2lambda+sqrt(6)lambda and the source's anti-Hermitian S1,S2 and diagonal D2. With

    F=exp(lambda² S2)exp(lambda S1),

the source proves

    F(H−cI)F†=H0+lambda²D2+R,
    ||R||<=10^6 lambda³,
    f:=||F−I||<=30lambda+900lambda²<=31lambda.       (1)

Here F is extended by identity on S and all passive references. All estimates are full-space bounds. Define B0'=F B0 F†. A two-term subtraction gives

    ||B0'−B0||<=2f||B0||.

Thus exactly

    F(H_B−cI)F†
      = H0+lambda²D2+lambda²B0+R_B,
    ||R_B||<=10^6lambda³+2f lambda²||B0||.           (2)

This includes the effect of a noncommuting background. In particular, it is not legitimate simply to add B0 to the selected effective generator without paying the transformed-background term.

For any real t, Duhamel and the two endpoint F factors yield

    ||e^{-itH_B}
      −e^{-ict} e^{-it(H0+lambda²D2+lambda²B0)}||
      <=2f+|t|[10^6lambda³+2f lambda²||B0||].        (3)

Both compared generators are selfadjoint and bounded on the stated finite systems. Tensoring passive identities preserves this bound. It may be capped at 2.

## Selected mediator input and complete target

Let J0 xi=xi tensor |0>_m. H0 and D2 commute with n_m: D2 is diagonal in the four mutually disjoint H0 energy bands, whose projectors also have definite m. The assumed B0 commutes with n_m. Therefore the comparison generator in (3) preserves the m=0 space even when B0 mixes the two old-Z sectors. On that entire space the source derives D2=−2I−Q. Consequently

    e^{-ict} e^{-it(H0+lambda²D2+lambda²B0)} J0
       = e^{-it(c−2lambda²)} J0
             e^{-it[K+lambda²(B0−Q)]}.              (4)

No factorization of the last exponential into K and B0−Q is asserted: in general they do not commute. The common scalar phase is explicitly c−2lambda² and occurs once. The effective target preserves all old, clock, spectator and passive-reference information, with a common mediator |0> output. Actual leakage into m=1 is included in the error; it is not projected away.

Combining (3)-(4), for |t|<=a/lambda²,

    ||e^{-itH_B}J0
       −e^{-it(c−2lambda²)}J0
                       e^{-it[K+lambda²(B0−Q)]}||
      <= lambda[62+10^6 a+62a||B0||].               (5)

This is a complete isometry bound uniform over arbitrary joint old/clock/S inputs and their passive extensions. In particular lambda<=epsilon/[62+10^6a+62a||B0||], together with the original smallness and physical cap, suffices for vector error epsilon over the indicated interval. For mixed inputs, the unhalved complete channel distance is <=min(2,2epsilon). No assumption about a clock product seed is needed for this comparison. A lambda-dependent B0 is allowed only with its actual norm paid in (5); no uniform bound is inferred from bounded local terms in an expanding system.

## Positive blocks, caps, and clock specialization

For an actual positive nearest-neighbor realization, separately supply B0=sum_l b_l with each b_l positive on an allowed one- or two-qubit support, real if the real-block class is to be retained. The extra load at a site v is lambda² sum_{l incident v}||b_l||; add this to the original loads 3+2lambda+2sqrt(6)lambda on old1, 3+2lambda on old2, 2lambda on a,b, and 4+2sqrt(6)lambda on m. Blocks involving S also incur their own incident loads and geometric obligations. There is no claim that every abstract B0 admits the required geometry.

For a real symmetric matrix C acting only on the adjacent clock pair a,b, set b=max(0,−lambda_min(C)) and supply the positive block lambda²(C+bI). Then use B0=C+bI in (1)-(5). The complete target can be written

    exp[-it(c−2lambda²+lambda²b)]
       J0 exp[-it(K+lambda²(C−Q))],

with ||C+bI|| charged in the error and both clock-site caps. This specialization uses six positive blocks and five qubits, with the source geometry unchanged. Since C acts only on clocks, K commutes with C−Q, so the latter exponential can then be factored into literal old aging and the scaled clock dynamics. The fixed-difference clock-sector problem is therefore supplied as an approximate dynamical interface without an old-only counterterm. Its simultaneous common-output equations are still unsolved; the interface is not a successful clock assembly.

The mediator product state, its gap, the positive blocks and calibrated sqrt(6) ratio remain supplied. No native selection, cooling, initialization mechanism, common-output clock solution, dwell interval, capture, reset or permanent halt is established. A background not commuting with n_m would invalidate the simple target (4); it would require an explicitly different target or an additional error argument.

## Provenance and verification limits

ROOT proposed using the same F and an identity-on-m background. The derivation here is an elementary transformed-background subtraction and Duhamel estimate on the full space, followed by an explicitly invariant selected subspace. The original source was read in full during its authorship and its hash was refreshed for this extension. It is the sole mathematical dependency. This is shared-lineage author evidence, not an independent review. Only BACKGROUND.md was written; no source overwrite, scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication, or delegation occurred. A distinct check is required before downstream promotion.
