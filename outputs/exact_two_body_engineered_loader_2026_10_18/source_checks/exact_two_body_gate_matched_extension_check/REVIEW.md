# Matched diamond and real rail mixers: distinct check

Disposition: SUPPORT for the corrected source's exact one-head scalar reductions and local interface accounting. One phase-convention ambiguity in the original was raised and corrected during review. No further required correction found. No full composed network, finite transfer policy or native realization is established.

## Sources, revision and exposure

The original full read was `exact_two_body_gate_matched_extension/PROPOSAL.md`, supplied SHA256 `75a0a4a77db138f4ee2bbd1cc5b1c42ecf2a4e9f767573e352f2b72478d8a2f6`. It first described the scalar chain with diagonal 2J+mu and then said to multiply scalar-chain evolution by exp(-i mu t), leaving a possible double counting. I raised the ambiguity. ROOT preserved that version as `PROPOSAL_original_75a0.md` and corrected the live source. I then read the complete corrected source and verified SHA256 `a1157d95d06e7eeced6217ec2fb7b43247619a74cd9aded3eeb811a68ba6075e`. This review targets that corrected identity. Paths are under `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261017_110934`.

The prerequisite is the immediately preceding fully read diamond source `7fa888681833216ded21fab0028f18ad079fde94b7f884a391c83196fb5a3e33` and my review `da5cbc9bcb0f66442da600191c4b863ed7c22a5a4bba0d024a0c683cf71b1945`. Their exact six-block positivity, one-head arm rotation and X gauge are reused at that scope. No earlier finite/scattering theorem supplies the matching step. ROOT authored this extension and exposed its proposed formulas; I reconstructed the diagonals, gauges, loads and mixer matrices below. This is source-exposed same-model analytical checking, not blind replication or formal retained audit.

## 1. Actual diagonals and the single scalar phase

Set a=J/sqrt(2), g=J. The four diamond head-head blocks contribute 2a=sqrt(2)J to each diamond site's one-head diagonal. At L/R, precisely one additional ordinary Q_J attachment contributes J, giving (sqrt(2)+1)J. At the arms, the two contacts give physical diagonals (sqrt(2)+1)J plus or minus JX. After the B/C arm rotation their common scalar diagonal is also (sqrt(2)+1)J; the difference appears as JX off-diagonal. No mu occupation is required or permitted by this matching prescription on any of these four internal physical heads.

An ordinary exterior interior site receives two Q_J occupations and its added positive mu n, giving 2J+mu. With mu=(sqrt(2)-1)J, this equals the internal scalar diagonal exactly. The three internal chain hoppings after the data gauge are -J,+J,-J. All external hoppings are -J.

Let S be the scalar sign gauge equal to -1 on C,R and every right-extension coordinate, and +1 on the left and B. It changes the central +J to -J. Every other link either has two unchanged signs or two flipped signs, so it remains -J. The data gauge W and S commute. Their product G has values I on the left/B and -X on C/right. Thus, in the rotated one-head coordinates,

    G* H G = h_uniform tensor I_D + mu I,

where h_uniform has diagonal 2J and all hopping entries -J. Consequently

    exp(-itH) = G exp(-i mu t)
                    (exp(-it h_uniform) tensor I_D) G*.

This is equivalently G exp[-it(h_uniform+mu I)]G*, with no further scalar factor. The corrected source now makes this convention explicit. Starting on the left, a physical right amplitude is minus the scalar amplitude times X; left amplitudes carry I. The physical u/v amplitudes still combine I and X and need not factor from the data. The scalar shift is a one-head statement: it is not a full-Hilbert-space vacuum energy. All installed blocks, including mu n, annihilate the full head vacuum.

## 2. Finite endpoints and full-support loads

The infinite one-head uniform operator is bounded; its diagonal and two-neighbor hopping sums are uniformly finite. The arm/data/sign maps are bounded unitaries, so no domain or scattering-completeness premise is hidden in the conjugacy.

For finite extensions, write h_fin for the scalar comparator with its actual source or cap blocks and WITHOUT the added mu occupations. On every exterior source/cap coordinate the physical construction adds exactly mu n, while the four internal transformed coordinates already have their required extra mu diagonal. Therefore the exact reduction is h_fin+mu I on the one-head space, provided the source/cap blocks are data-independent and attached on the designated side. Weak endpoint hopping and exceptional endpoint diagonals remain exactly those of h_fin. They are not replaced by uniform bonds in claiming this equivalence. No scalar endpoint-seed theorem, launch time or high-success window is obtained merely from the equivalence.

A Q_a block has full norm 2a. At each internal L/R the two diamond bonds and one attachment give 4a+2J=(2sqrt(2)+2)J. At each arm the two diamond bonds and contact give 4a+2g, the same value. The data incident sum is 4g=4J. At an ordinary exterior head, two Q_J bonds and mu n have sum 4J+mu=(3+sqrt(2))J. These are sums of full-support block norms, not one-head row sums. Termination modifications must replace the relevant ordinary inventory and be counted separately, as the source requires. A chosen cap Lambda must pay these loads; the statement does not silently impose J=Lambda.

## 3. Identity and gated parallel lanes

For X=I the u contact becomes 2J n_u and the v contact vanishes. The B/C scalar matrix is unchanged. The right sign is now -I instead of -X. The omitted zero contact has no norm load; the former data qubit is unnecessary in this identity lane. The remaining arm loads do not exceed the displayed gated bounds.

For two disconnected otherwise identical lanes, scalar evolution is the same in each lane at every time. On the right their exact data map is

    -[|0><0|_rail tensor I + |1><1|_rail tensor X],

with the same scalar head profile in both lanes. The shared minus is a retained scalar phase. This equality supports coherent superpositions and passive references, not just a classical choice of lane. Only the gated lane couples to D. It requires matched scalar terminations and no undeclared cross-lane interaction. It is not by itself a gauge proof for a serial network with subsequent noncommuting gates.

## 4. Hadamard and permutation mixers

For the signed four-edge mixer each edge has weight J/sqrt(2) and hopping -s J/sqrt(2). With s given by the entries of sqrt(2)H_2, the complete cross matrix is exactly -J H_2. Every mixer head meets two such edges, hence its internal diagonal is sqrt(2)J, independent of hopping signs. Its one ordinary attachment adds J. This yields 2J+mu without an additional occupation term on the mixer heads. The four blocks are positive on full two-head support and annihilate vacuum by the same Q_s calculation as the diamond.

Apply the identity on the left rail pair and H_2 on the right pair, and extend that same rail basis change throughout the identical right continuations. Since H_2 is real orthogonal and H_2^2=I, the cross matrix becomes -J I_2. Scalar onsite matrices and identical continuation matrices remain scalar in rail space. The result is two identical scalar chains with the common mu shift, with physical right rail action H_2. Applying the basis change only at R0/R1 and leaving their adjacent continuations in the original basis would not prove this statement; its extension along the identical right rails is essential.

The mixer head's full-support incident sum is 2*(2J/sqrt(2))+2J=(2sqrt(2)+2)J. There are exactly four internal Q blocks, four separately counted attachments, and no data contact or internal onsite repair. Ordinary exterior occupations are counted once.

For identity or swap, the internal permutation matrix consists of two disjoint Q_J edges. Each mixer head has internal diagonal J and one attachment supplies another J. Installing mu n on these mixer heads therefore gives 2J+mu, unlike the Hadamard case. Their incident sum is 4J+mu=(3+sqrt(2))J, smaller than (2sqrt(2)+2)J because sqrt(2)>1. The cross matrix is -J times the permutation. Extending its orthogonal rail gauge down the corresponding right continuations reduces it exactly to -J I_2. The two internal bonds and four one-body repairs must both be retained in that variant's inventory.

## 5. Serial boundary accounting and remaining obligations

If a single physical Q_J cable edge joins one module's R endpoint to the next module's L endpoint, it supplies J to each endpoint's diagonal and norm 2J to each endpoint's incident sum. It is one block, not two duplicated attachment blocks. A diamond or Hadamard endpoint already has internal diagonal sqrt(2)J, so this cable completes it to 2J+mu with no extra mu term there. An identity/permutation endpoint has internal diagonal J and therefore still needs its stated mu repair. An ordinary cable-interior coordinate has two ordinary bonds and receives one mu occupation. These rules are consistent whether a cable has interior sites or consists of one direct edge.

The diamond's B/C rotation preserves its physical L/R ports. The subsequent rail/data gauges act on port fibers; in particular the Hadamard rail gauge mixes the two R coordinates. The source's statement about internal transforms preserving port coordinates is used in this distinction, not as an assertion that the rail Hadamard fixes individual R0/R1 basis vectors. This is why a complete cumulative ordered gauge, and its action on each physical interconnection, remains necessary before composition. Equal scalar lane lengths, absence of bypasses, all shared-data interactions and all endpoint loads must be checked in any later network.

For X=Z_D the same local proof holds because Z_D is a real Hermitian involution. The suggested Hadamard-conjugated rail control and an eventual SWAP/record word are still prospective interfaces, not results proved here. The exact rare-event conditional action follows from the already checked branch factorization, with the newly retained common phase and minus; no success probability guarantee follows.

The scope remains supplied real positive two-body blocks with exact symmetric coefficients, identical scalar extensions and freely degenerate data. This review does not supply a cubic nearest-neighbor layout, native coefficients, robustness, cooling, an autonomous endpoint preparation, an active-environment interface, capture/reset or permanent storage. No existing finite resource policy is transferred by analogy.

Only this REVIEW.md was created. Work consisted of analytical reconstruction, complete source reads and deterministic hash/directory bookkeeping. No scientific executable, solver, simulation, sweep, delegation, Git/publication/W/checkpoint/axiom/editable-prompt change or model override occurred. No editable prompt file changed. The author, not this reviewer, made the disclosed source correction.
