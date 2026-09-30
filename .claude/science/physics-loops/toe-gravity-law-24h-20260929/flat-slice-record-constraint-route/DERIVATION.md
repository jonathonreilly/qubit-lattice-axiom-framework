# Exact source-matching identity on a supplied flat slice

Author analytic result under CONTRACT faebd06dc7b4893561b4f81661ec469058b0f0435613d43e8e6f11255bcf4332. No independent-check verdict or scientific execution is asserted here. This is a conditional endpoint identity on a supplied continuous canonical carrier. It selects no matter law, gravitational record source, clock or axiom.

## Domain and literal endpoint constraints

Use the flat three-torus of any fixed side, normalized mean <.>, ordinary derivatives, real smooth symmetric pi, a>0, and supplied scalar/source momentum densities rho,j. At g=I the literal canonical gravity constraints in the provisional bd6f6e63 note reduce to

    C=a Q(pi)+rho=0,   J_i=-2 partial_j pi^(ij)+j_i=0,
    Q(S)=tr(S²)-(tr S)²/2.                                  (1)

These formulas are also fully specified definitions for the present calculation. No analytic evolution theorem, discrete product rule, short-time solution or physical source identification is used. A change of curvature would add a term and is outside this fixed-metric result.

The initial slice is pi0=lambda I, rho0=3a lambda²/2, j0=0, with arbitrary real lambda. It satisfies(1). An instantaneous endpoint change keeps g=I,j=0 and changes pi to pi0+sigma, rho to rho0+delta rho. Requiring the complete endpoint constraints gives

    div sigma=0,
    delta rho=a[lambda tr sigma-Q(sigma)].                    (2)

The coefficient lambda is exact: Q(lambda I+sigma)-Q(lambda I)=Q(sigma)-lambda tr sigma. In particular no truncation in sigma, small-event limit or discarded quadratic momentum term enters. Let E=<delta rho>.

## Fourier identity and homogeneous response price

Write sigma=sum_k S_k exp(ik.x), S_-k=conjugate(S_k), and S_0=<sigma>. Smoothness ensures absolute convergence and Parseval; the identity extends to square-integrable divergence-free fields if(2) is interpreted integrably. For k!=0 let

    P_k=I-k k^T/|k|², t_k=tr S_k,
    T_k=S_k-(t_k/2)P_k.

The Fourier momentum constraint says k^T S_k=0. Symmetry then gives S_k=P_k S_k P_k. P_k has rank2. Therefore T_k is transverse and traceless, Hilbert--Schmidt orthogonal to P_k, and

    ||S_k||_HS²-|t_k|²/2=||T_k||_HS²>=0.                    (3)

This is a complex Fourier identity with absolute squares; replacing them by unconjugated scalar squares would be incorrect. On the real field Parseval yields

    <Q(sigma)>=Q(S_0)+sum_(k!=0)||T_k||_HS².                 (4)

Decompose S_0=s I+A, tr A=0, with s=<tr sigma>/3. Then Q(S_0)=||A||²-3s²/2. Averaging(2) proves the exact finite-amplitude balance

    E/a=3lambda s+3s²/2-||A||²-sum_(k!=0)||T_k||².           (5)

Only the constant trace direction can pay a positive total increment; nonzero transverse-traceless modes and homogeneous anisotropy have the opposite sign. For E>0, (5) implies

    |s+lambda|>=sqrt(lambda²+2E/(3a)),
    |<tr sigma>|>=3[sqrt(lambda²+2E/(3a))-|lambda|]>0.        (6)

The latter bound is sharp within the supplied endpoint class. Choose sigma=s I, A=0, all nonzero modes0, and s with sign(lambda) on the branch nearest zero (either sign iflambda=0), so |s|=sqrt(lambda²+2E/(3a))-|lambda|. Then delta rho is the positive constant E and both endpoint constraints hold exactly. This response is spatially homogeneous. Equality in the first inequality permits nonzero pure transverse-trace Fourier modes T_k=0; it does not require a completely homogeneous field if the scalar source is allowed to vary and be signed.

When lambda=0, (6) is |<tr sigma>|>=sqrt(6E/a). At lambda!=0 and small positive E, the sharp mean-trace price is E/(a|lambda|)+O(E²). These are normalized-mean densities; a localized event with fixed TOTAL increment on a volume V has E=Delta E_total/V. No volume-independent local amplitude bound follows from(6), and the change may be distributed over the whole torus.

## A compact supported momentum update has zero mean

Assume supp sigma is contained in a compact subset of a proper flat coordinate chart, for example a ball which does not wrap around the torus. Choose a smooth periodic scalar chi_i which equals the coordinate x_i on a neighborhood of this support. Integration by parts and div sigma=0 give, for every i,j,

    <sigma_ij>=<partial_k chi_i sigma_kj>
             =-<chi_i partial_k sigma_kj>=0.                (7)

The first equality uses that sigma vanishes wherever chi_i ceases to be the coordinate. Thus S_0=0, not just its trace. Equations(5),(7) give the exact identity

    <delta rho>=-a sum_(k!=0)||T_k||²<=0.                    (8)

If delta rho is pointwise nonnegative, its mean and hence delta rho itself vanish. Equation(8) is conditional on this complete endpoint class. It does not say that gravity forbids positive-energy records: fixed metric, zero source momentum, initial homogeneous pi, locality of the momentum change, and the source interpretation are all additional choices.

## Null, signed and changed-hypothesis controls

For any smooth real bump f inside the coordinate chart, take

    sigma_ij=partial_i partial_j f-delta_ij Delta f.         (9)

It is divergence-free and compactly supported. Its nonzero Fourier coefficients are |k|² fhat(k) P_k, so T_k=0. In real space,

    tr sigma=-2Delta f,
    Q(sigma)=|Hess f|²-(Delta f)²,
    delta rho=a[-2lambda Delta f-|Hess f|²+(Delta f)²].       (10)

Two integrations by parts give <|Hess f|²>=<(Delta f)²>, proving E=0 directly. Hence the sign result is not a claim that every local momentum update vanishes. Nonzero signed local source rearrangements are allowed, and (9) is an exact null family for the integrated quadratic form. At lambda=0, a one-coordinate f gives Q=0 pointwise, though that periodic slab is not compact in a single three-dimensional chart; this additional algebraic control is not substituted for the support hypothesis(7).

The homogeneous update used after(6) permits E>0 and violates the compact-support condition. An exactly compensating source with delta rho=0 and sigma=0 also preserves both endpoints. If a local record plus its supplier has no net local stress-energy change, these constraints cannot distinguish their internal bookkeeping. A metric change introduces curvature and changes the divergence/pairing structure. Nonzero source momentum gives div sigma=delta j/2 and invalidates the transverse positivity premise. These are explicit unclassified alternative hypotheses, not routes excluded by this calculation.

The actual original formation-energy theorem concerns a supplied rotor Hamiltonian expectation and has no gravitational rho/j assignment. Its positive conditional first-event energy cannot be inserted into(2) without a separate common action and source map. Likewise the optional native marker models use changed GKSL laws and do not provide that map. The present result identifies an exact matching condition that such a proposed map must check; it retires no physical-law/clock/primitive import.

## Scope, novelty and exact next action

The linear seed already exposed a zero-mode source condition. Equations(3)--(8) add an exact finite-amplitude, divergence-free momentum identity at an arbitrary homogeneous expanding/contracting flat background, including the quadratic update and a sharp homogeneous-trace price. This is elementary constrained-momentum geometry, with no historical-novelty claim or full nonlinear gravity exclusion. It belongs in the research pack unless a wider coherent source-matching unit needs it. No milestone PR or negative-claim exhaustion certificate is proposed.

The precise remaining physical consumer is a selected total source map, including the apparatus/record energy and momentum, and an endpoint/evolution law preserving all gravitational constraints while respecting its actual locality and metric changes. That consumer is not proved by this identity. The current theorem requires an independent focused reconstruction before reuse; no numerical calculation is necessary for its universal quantifiers.
