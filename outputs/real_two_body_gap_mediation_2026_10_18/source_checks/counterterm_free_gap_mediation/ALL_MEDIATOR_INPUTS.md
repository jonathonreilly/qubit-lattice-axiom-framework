> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Full mediator-space cancellation and joint output

Status: new author extension, pending distinct check. ROOT noticed that the other mediator sector may have the same canceled old self-energy. The calculation below verifies that observation and upgrades the comparison to all joint inputs using the already full-space remainder proof. PROPOSAL.md SHA `739a1961076d52b0e26364bd858f957a89a233bfa72aa652efa193ef54ac2cdd`, BACKGROUND.md SHA `20e79f3fdb1243975efb2165301940eef886d3e75f333ab1f137806c1f3f4c35`, and UNEQUAL.md SHA `f8aa102e2b8575f5da23933747c660c1aad3b81090014d91acb600d6faaf0256` remain unchanged. Shared author/design exposure is explicit; this extension requires its own distinct check.

## Same actual positive device

Retain exactly the five blocks and geometry of the base source:

    H=K+lambda(I+Y1Y_a)+lambda(I+Y2Y_b)
             +4n_m+sqrt(6)lambda(I+X1X_m),
    K=2I+Z1Z2, Q=X1X2Y_aY_b,
    0<lambda<=1/1000, c=2lambda+sqrt(6)lambda.

Write Z_m=I−2n_m. No initial restriction on the mediator is imposed in the result below. The actual five-qubit, five-positive-block inventory and full-support incident caps remain unchanged: old1 has load 3+2lambda+2sqrt(6)lambda, old2 3+2lambda, a,b each 2lambda, and m 4+2sqrt(6)lambda. The supplied gap and coupling relation remain essential premises.

## Reconstructing every diagonal band

H0=K+4n_m has the four distinct energies 1,3,5,7. The base source constructs a full-space real orthogonal F and diagonal D2 satisfying

    F(H−cI)F†=H0+lambda²D2+R,
    ||F−I||<=31lambda, ||R||<=10^6lambda³.           (1)

No mediator-input restriction was used in these estimates. It was only used in identifying the previously stated target.

Fix old Z=z and mediator occupation m=0 or 1. The YY intermediate state has the same mediator occupation and opposite old Z, so its denominator is 2z. Its selected diagonal contribution to D2 is z−Q in either mediator sector. The normalized mediator exchange sqrt(6)X1X_m has denominator 2z−4 when m=0 and 2z+4 when m=1. Therefore its contributions are respectively

    6/(2z−4)=−2−z,
    6/(2z+4)= 2−z.

Mixed YY/mediator terms change mediator occupation once. They cannot end in the same H0 energy band because the two sets {1,3} and {5,7} are disjoint. They contribute no diagonal term. Summing gives

    D2|_{m=0}=−2I−Q,
    D2|_{m=1}= 2I−Q,
    D2=−2Z_m−Q                                    (2)

on the entire Hilbert space. Q commutes with old Z and with every mediator operator, so (2) respects all four energy projectors. There is no omitted old-parity-dependent scalar in the m=1 sector.

## Full operator comparison and complete phase

The same two endpoint conjugations and Duhamel as in the base source now give

    ||e^{-itH}
       −e^{-ict} e^{-it(K−lambda²Q)}
                   tensor e^{-it(4n_m−2lambda²Z_m)}||
       <=min{2,62lambda+10^6|t|lambda³}.            (3)

The displayed tensor product separates old+clock from mediator; arbitrary passive identities may be appended. Equivalently the complete target is

    exp[-it(c−2lambda²)]
          e^{-it(K−lambda²Q)}
                   tensor e^{-it(4+4lambda²)n_m}.  (4)

These are two equivalent phase conventions, not two phases to multiply together. Both retain the scalar 2I inside K. At |t|<=A/lambda² the error is at most (62+10^6 A)lambda, uniformly over ALL joint initial states, including coherent mediator superpositions and correlations with the old pair, clocks and passive references. Mixed-state complete channel distance is at most twice this operator bound, capped at 2.

No mediator vacuum, basis state, purity, or independence is needed for (3). For an initially independent mediator state sigma_m, the target factor is its explicit unitary evolution under (4), and it is independent of the old/clock input. For initially correlated states the correct target is the corresponding tensor-product unitary acting on those same correlations. It is not a tensor-product output state and does not erase or relocate correlations.

The mediator generator in (3)-(4) is an EFFECTIVE aging generator including the virtual energy shift. The actual isolated mediator block installed in H is 4n_m. If the target is instead required to use precisely exp(−it4n_m), one must pay the relative phase shift: in convention (4) the additional operator cost is 2|sin(2lambda²t)|<=min(2,4lambda²|t|). This is generally order one on the mediated timescale. Thus removal of the initial-state supplier is a full joint-output result with the explicitly prescribed effective mediator evolution, not an identification of that evolution with the bare free mediator Hamiltonian.

## Weak backgrounds

Let B0 be bounded selfadjoint on old+clock and optionally finite spectators, acting identically on m. Add lambda² B0 to the actual H. As in BACKGROUND.md,

    ||F B0 F†−B0||<=2||F−I||||B0||.

Using (1)-(2) gives the full-space bound

    ||e^{-it(H+lambda²B0)}
       −exp[-it(c−2lambda²)]
          e^{-it[K+lambda²(B0−Q)]}
                    tensor e^{-it(4+4lambda²)n_m}||
       <=min{2,62lambda+|t|lambda³(10^6+62||B0||)}. (5)

Here B0 need not commute with K or Q, and the old+clock exponential is not split into noncommuting factors. The entire mediator factorization follows from B0 acting trivially on m. Equation (5) holds for arbitrary initial joint correlations, not just a selected isometry. At |t|<=A/lambda² its error is <=lambda[62+10^6 A+62A||B0||]. Positivity, real nearest-neighbor block decomposition, spectator geometry and incident loads of the background must be supplied and paid exactly as in BACKGROUND.md; bounded selfadjointness alone is not a hardware construction.

For a clock-only real symmetric matrix C, installing lambda²(C+bI) with b=max(0,−lambda_min(C)) makes that pair block positive. The scalar in (5) then becomes c−2lambda²+lambda²b and the old+clock generator is K+lambda²(C−Q), with ||C+bI|| used in the bound. This supplies the same unsolved fixed-difference clock interface without requiring an initially blank mediator. It does not exhibit clock vectors or solve the common-output equations.

## Relation to unequal couplings and scope

The same calculation also identifies, without altering the frozen unequal note, the full unequal second-order diagonal correction as

    −(g²/3)Z_m−uv Q+delta Z,
    delta=(u²+v²)/2−g²/6.

Thus the cancellation relation g²=3(u²+v²) cancels the old-only shift in both mediator sectors, rather than only m=0. This identity is a direct band calculation; the primary quantitative result here is the equal-coupling bound (3)-(5). All unequal normalization and horizon conditions remain those of UNEQUAL.md and are not improved by this observation.

This extension removes a selected mediator-state premise for the stated joint-output comparison. It does not prepare, reset or return an arbitrary mediator to its input state. It does not make arbitrary correlated apparatus independent of an unknown logical input. The clock inputs, literal K, positive blocks, supplied coefficients and gap still have their explicit roles; no native derivation, standalone literal W, all-time completion flag, dwell, capture or permanent halt is inferred.

The four band contributions and factorization were reconstructed here. The base remainder and background inequalities were read and proved in the preceding tasks and are reused at unchanged hashes and hypotheses. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication, delegation, or old-source edit occurred. Only this addendum was written. This is author evidence pending a distinct check.
