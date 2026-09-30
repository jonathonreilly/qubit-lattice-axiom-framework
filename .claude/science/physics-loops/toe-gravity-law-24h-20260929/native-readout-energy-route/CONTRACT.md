# Contract: energy injection by a supplied occupation readout

Status: author discovery, conditional mathematical candidate; no formal review, audit, retained status or physical-record selection.

## Exact setting and target

Keep the actual full tensor-product qubit Hamiltonian H0 of the landed native density-onset note, on every cubic torus L>=5 with arbitrary supplied mu,tau>0. Keep its number N, occupation basis b=|0><1|, and positive decomposition H0=sum_x h_x^+=S+mu Ddiag+Wtau. The state is any density matrix, including coherent, mixed and particle-number-indefinite states. Supply the complete occupation Lüders instrument, or the Lüders instrument on a stated set B. These instruments, Born probabilities and instantaneous state update are additional conditions; permanence and occurrence are not inferred.

Derive the exact diagonal Hamiltonian and the best volume-independent lower constant c in D(H0)>=cN. Translate it into an actual expected system-energy injection, and test whether the already landed exact unitary trial and small positive chemical-potential ground states require positive extensive injection. Prove a local version from the actual positive local terms if all boundary terms can be retained honestly. Identify the additional apparatus and endpoint assumptions required to call this supplied energy or work.

## Frozen expected derivation, before controls

Let E_a and E_p count unordered occupied axial graph edges (offset +/-2e_i) and plane graph edges (offset +/-e_i+/-e_j). The candidate identity is

    D(H0)=mu Ddiag+(2mu/3+4tau) E_a+(3mu/2+3tau) E_p.

Equivalently it is mu N+V3+(4tau-4mu/3)E_a+(3tau-mu/2)E_p. Each axial pair has one center, each plane pair two; an identical pair has no adjacent centers, so every cross-center term in a gradient has zero diagonal. This is to be checked directly on odd and even tori without a global parity assumption.

The candidate sharp constant is c_read=min(mu,mu/3+2tau). For occupied degree m, use f(m)=(m-1)(m-2)/2 and half of each incident edge weight. The isolated monomer and isolated axial dimer should saturate its two branches. The resulting full-readout injection is at least c_read<N>-<H0>. It is not asserted positive on arbitrary inputs; a diagonal input has zero injection.

For a set B, define B^-3={x: the torus graph-distance ball of radius3 about x lies in B}, B^+2={x: distance(x,B)<=2}. Group the actual positive squares and diagonal term into h_x^+ with support in the radius2 ball about x. Candidate local estimate:

    Tr H0(D_B rho-rho) >= c_read <N_(B^-3)> - <sum_(x in B^+2) h_x^+>.

The proof must allocate the complete diagonal weight of every graph edge incident to B^-3 from actual wholly-inside squares; it must not delete physical neighbors inside Ddiag or assume a modified-boundary Hamiltonian is positive. For translation-invariant rho, this would imply c_read rho_density |B^-3|-e |B^+2|. No restricted-state/independent-dimer replacement is allowed.

Use only the landed trial bounds E/V<=A u^4 and N/V>=2u^2-B0 u^4, and the landed H0-nu N onset estimates, for low-energy consequences. Do not consume the open EOS. An energy-conserving implementation can price the system injection against apparatus loss only with the full interaction-energy endpoint ledger stated. Entropy, general measurement work, a universal per-record price, autonomous implementation and native permanent records remain open.

## Distinction from prior work and independence

Parent brief exposed the proposed two edge weights, without a proof or accepted outcome. This author independently reconstructed them from the literal Q words. Prior author roles include full-carrier lower/upper packets and the recent native record-compatibility packet. This is a new author derivation, not an independent audit. Prior generic occupation pinching removes offdiagonal hopping, and rank-one locked-output CP operations have a measure-and-prepare normal form; neither is claimed new here. The present target is the quantitative, sharp full-carrier energy and spatial debit for this unchanged pair Hamiltonian.

## Controls and resource freeze

Before any numerical execution, freeze a standard-library exact Fraction runner and expected checks: (1) literal integer pair-word squared rows for original Q attractions, positive S and actual gradients; (2) all pair diagonal weights and absent adjacent-center repeats on L5 and L6; (3) direct configuration diagonals versus the degree identity and all integer degree inequalities, including monomer/dimer equality; (4) local row support and complete incident edge coverage at radius3, with a radius2 adversarial fixture; (5) a nonzero coherent pair example distinguishing energy injection from occupation distribution. Controls support, and do not prove, the all-volume statements.

One sequential sparse job, initially at most30 CPU seconds/90 wall seconds/150 MiB, BLAS threads1. Deadline/STOP checked before launch and during managed execution. Price must be coordinated with root before launch. No dense many-body matrix and no author-source runner import. Preserve any failure with original source/output before a correction. No new computation is needed for elementary apparatus conservation.

## Source and process boundary

Current main refreshed to fb5da8dd5ac1b001b0c619070f27e5b7f8fe4be7; selected procedures7146fe17a76de41badcaca3c3c7cac6d11eb2a00. Current minimal axioms and primitive registry/sources remain the premise authority. No basis, Born rule, H0, sharp instrument, controller, state preparation or work reference is derived from them. Main and open relevant proposals were refreshed and read to the stated source scopes; exact bindings follow separately. Writes stay in this new directory. No git, source-authority, PR or audit mutation. Original deadline2026-09-30T22:41:00.557005Z and runtime STOP sentinel remain binding.
