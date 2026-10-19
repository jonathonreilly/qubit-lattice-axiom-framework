> Source-use boundary (2026-10-18 packaging): The complete mathematical body below remains inspectable supporting material at its explicit hypotheses. Historical author/check status, acceptance and execution narratives are provenance only; they confer no present verdict. Original byte-exact recovery is in `archive/product_continuation_four_review_2026_10_18/MANIFEST.json`. References to earlier hashes identify original versions; the live input closure binds current portable sources.

# Finite-network one-head interface with a compensated vacancy shift

Status: new bounded author addendum, pending distinct check. ROOT proposed extending the pair dressing by identity and using the global one-head sector. This note reconstructs that extension and pays the full network background norm. It does not construct a released literal gate or establish retention/halt.

Dependency: VACANCY_HOPPING_PROBE.md SHA `7ce327a279b7c89e6ee48dd94555a78bdb357dd183b4333618f958e4d387da00`, and its exact physical-mediator dependency EXACT_ALL_TIME.md SHA `37e2cf2c776d6425c93b113b92bc114b8e478db779d1dc6f0d28cc33a925ca34`. The first remains pending distinct check at this author's freeze; ROOT reports the exact mediator interface checked. All predecessor files remain unchanged. Shared-design author evidence is not an independent review.

## Finite network and exact pair dressing

Take L>=2 clock qubits, including adjacent sites a,b. Let N=sum_j n_j and P1 the global one-head projector. Use X=X1X2 on the old pair, K=2I+Z1Z2, T=Y_aY_b, J_ab=|01><10|+|10><01| on a,b. Let P00 and P11 denote their local vacancy and double-occupancy projectors, tensored with identity on every other clock.

Let B be a bounded selfadjoint clock-network operator with [B,N]=0, acting trivially on the old pair and mediator. It may move a head into or out of a,b. It need not preserve the local no-double subspace on general many-head inputs.

For U>0 define H_pair=U P11−X T and r=(sqrt(U²+4)−U)/2. Extend the predecessor's exact real orthogonal pair rotation D by identity on the other clocks and all passive systems. Its full-space identities remain

    H_pair=D H_diag D†,
    H_diag=−X J_ab−r P00+(U+r)P11,
    ||D−I||<=1/U.

The same transformed-background calculation therefore gives, on the entire network Hilbert space,

    ||exp[−is(H_pair+B)]−exp[−is(H_diag+B)]||
       <=min{2,(2/U)(1+|s|||B||)}.                 (1)

Nothing in this proof requires B to preserve the local no-double subspace. The actual evolution need not conserve global N, since the pair term creates/annihilates two clock excitations. Its leakage is included in (1).

## Global one-head comparison

H_diag and B both commute with global N. Thus their comparison evolution preserves P1. On that sector, P11=0 and P00=I−n_a−n_b, so the exact restricted target generator is

    H_one=−X J_ab+B|_{P1}−r I+r(n_a+n_b).           (2)

In particular B may move the head outside the pair while (2) remains valid. This is the distinction from a restriction to the pair's local one-head sector. The phase/onsite shift in (2) must be retained if it is not compensated.

For the optional positive compensation define

    B_comp=r sum_{j outside {a,b}} n_j.

It is number-conserving and positive. On P1 it equals r(I−n_a−n_b), canceling the entire vacancy term in (2). Therefore with the actual background B+B_comp, the restricted comparison generator is exactly

    H_one,comp=−X J_ab+B|_{P1}.                    (3)

This is an exact equality only on the global one-head sector. On the full clock Hilbert space,

    ||B_comp||=r(L−2),
    ||B+B_comp||<=||B||+r(L−2).                    (4)

The norm in (4) is paid in (1); no one-head norm substitution is made in its full-space conjugation argument. In particular, large L is not free. Without compensation use (2), with B alone in the estimate.

## Actual positive physical composition

Retain the same exact calibrated five-qubit mediator device on old1,old2,a,b,m. Write its parameters as b_eff>0, a_eff and c_eff, exactly as defined in the pinned exact source. It has g<3lambda, b_eff<=lambda², 0<lambda<=1/1000 and the complete weak-background bound 164lambda(1+|t|||B_actual||).

Embed these sites in a finite specified nearest-neighbor clock graph containing the edge a-b. The other clock qubits occupy additional distinct sites. The interface assumes a supplied embedding and a listed positive real number-conserving clock inventory

    B=sum_{ell=1}^q B_ell.

Each B_ell has allowed one- or nearest-neighbor two-site support; total B commutes with N. If a proposed network lacks such a geometry or decomposition, this note does not supply it.

Add the actual positive blocks

    b_eff U n_a n_b,
    b_eff B_ell for every ell,
    b_eff r n_j for each of the L−2 outside clocks   (optional compensation).

With compensation there are L+3 qubits and 5+1+q+(L−2)=L+4+q listed positive blocks. Without it there are L+3 qubits and 6+q blocks. L=2 has no compensation terms. Repeated supports, if present in the listed B inventory, retain their separate load contributions; they are not silently merged to reduce a count.

The baseline loads remain 3+2lambda+2g on old1, 3+2lambda on old2 and 4+2g on mediator m. Each of a,b has load

    2lambda+b_eff U
                  +b_eff sum_{ell incident a or b separately}||B_ell||.

For clarity the sum in that formula is evaluated for each individual endpoint, not their union. An outside clock j has load b_eff sum_{ell incident j}||B_ell||, plus b_eff r if compensated. All must obey the supplied cap. The pair and onsite additions are positive real local blocks. The proof rotation D is not physically installed.

## Full-output comparison, phase and explicit feasible budget

Let B_tot=B or B+B_comp, and define

    M_B=||B||                  without compensation,
    M_B=||B||+r(L−2)            with compensation.

Set s=b_eff t. Combining the physical exact-mediator bound with (1), the actual complete evolution on initial global one-head clock states is within

    E(s)=164lambda[1+|s|(U+M_B)]
                         +(2/U)(1+|s| M_B)         (5)

of

    exp(−it c_eff) exp(−itK)
        exp(−is H_one) tensor exp(−it2a_eff n_m),

or the same expression with H_one,comp when compensated. The expressions are isometries from the global one-head input space into the complete physical output space. All actual pair-created extra heads and mediator errors are included in (5). There is no final projection or trace-out in the vector comparison.

K commutes with the target clock generator because B is clock-only and [K,X]=0. The mediator factor is its prescribed effective aging, not a reset or bare-gap identification. Arbitrary old/clock/mediator correlations supported in the initial one-head sector and all passive extensions are allowed. A definite one-head basis seed |1 at j0,0 elsewhere> is a real product clock input satisfying the hypothesis. For such a seed, subsequent head propagation can depend coherently on the old state; this primitive does not yet prove a common output head profile or a completed logical gate.

A simultaneous sufficient parameter choice can be made for any fixed finite network, scaled horizon S>=0 and 0<epsilon<=1. Put b_norm=||B|| and d=L−2 if compensated, d=0 otherwise. Choose

    U>=max{1,16(1+S b_norm)/epsilon,
                    sqrt(16 S d/epsilon)}.

Since r<=1/U, the clock error in (5) is at most

    2(1+S b_norm)/U+2S d/U²<=epsilon/4.

Next choose

    lambda<=min{1/1000,
        epsilon/[656(1+S(U+b_norm+d/U))]}.

This makes the mediator contribution <=epsilon/4 and hence E(s)<=epsilon/2 for |s|<=S. The complete unhalved channel error is <=epsilon. These are sufficient bounds, not optimized scaling laws.

For explicit cap feasibility put C_load=U+sum_ell||B_ell||+d/U. Any Lambda>4 permits the further choice

    lambda<=min{(Lambda−4)/16,
                     sqrt((Lambda−4)/(2 C_load))}.

The crude full-site bound 4+8lambda+lambda² C_load is then <=Lambda. This upper bound also covers every new outside clock site. Full network size is paid both in the inventory and, where needed, in d/U and the background norm. No claim about a growing-network limit is made without evaluating these quantities.

## What remains open

Equation (3) supplies a conditional old-X-controlled hopping link inside an otherwise specified number-conserving clock network, with no uncompensated vacancy shift in the one-head target. It permits a head to leave the pair in that target and pays actual pair-creation leakage over a stated horizon. It does not specify a network that implements literal W, releases a completed head with a common profile, or prevents its return. Combining several mediated links sharing the same old gap is also not justified by this single-link proof.

An actual released-gate construction still needs its explicit graph, ordered logical action, arrival and return bounds, all-output factorization and finite-horizon retention contract. Supplied positive coefficients, geometry, initial one-head support and calibration remain premises; no native initialization, capture, reset or permanent halt is claimed.

ROOT proposed the global-one-head and positive compensation steps. Their algebra and full norm cost are derived above. The source/status pins are exposed rather than represented as fresh independent review. No scientific executable, external search, Git, canonical/checkpoint/editable-prompt/model change, publication, delegation or predecessor edit occurred. Only this addendum was written. Distinct checking is required.
