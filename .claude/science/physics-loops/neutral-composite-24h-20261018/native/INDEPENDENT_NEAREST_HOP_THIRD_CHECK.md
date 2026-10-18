# Independent nearest-hop third-order check

Disposition: PASS in the canonical N2 effective-block gauge. Independent exact all-background sign-monomial enumeration confirms the stated coefficients. No repository edits.

For P onto the entire degenerate H0 energy4 (N2) space and R=Q/(4-H0), the canonical Hermitian third coefficient is PV R V R VP - {PV R^2 VP,PVP}/2. The two half-folds are required; P includes all N2 configurations, not merely a selected singleton branch. The root code uses signed denominators 4-2N and both folds with the correct factor1/2 and physical YY phases.

I independently enumerated ordered triples of native bond flips. The first two flips determine the third by its required final bit mask. Terms with two Q intermediates contribute the raw inverse-denominator product; terms with first-P/second-Q or first-Q/second-P contribute their corresponding half-fold squared denominator. Every YY insertion is represented as a formal background Z-mask times its explicit flip-dependent sign, so this checks every aligned background simultaneously rather than a sample. On R6 the results are:

- x ordinary: raw -299/64 I+(P_up+P_down)/64; fold -307/64 I+(P_up+P_down)/64; total I/8.
- x both endpoint columns complemented: raw -1/4, fold0.
- y ordinary: the analogous expression times endpoint ZiZj; total ZiZj/8.
- y complemented: raw ZiZj/4, fold0.

The same-background plaquette terms therefore cancel exactly. The ordinary x hopping block is -lambda I+lambda^3 I/8. Including the complemented output gives lambda^3(-Xbar_i Xbar_j/4). In y the complemented action has matrix element si sj/4, equivalently -Ybar_i Ybar_j/4. Logical YY convention matters: YY acting on Z signs gives -si sj times the double flip. Restoring energy units multiplies by J.

## Nearest-endpoint completeness

Each native insertion changes an even number of spins in every longitudinal layer. Starting from a singleton at layer z, any final singleton must have the same z; half-column intervals have a different layer-parity signature and cannot be reached. Distinct aligned-background labels must differ on an even number of whole columns. Three insertions supply at most six changed spin sites. For a fixed neighboring endpoint j, an unchanged background differs in two sites; complementing both endpoint columns differs in six; complementing two columns with only one endpoint differs in eight, and neither endpoint differs in ten. Thus only the ordinary and both-endpoint-complemented outputs are possible. No other nearest-endpoint background channel is omitted.

This exhausts nearest-endpoint entries, not all third-order transitions at other endpoints. It also uses singleton labels in their complemented-background convention; a three-flip interval is not an additional independently labelled branch.

## Size locality and gauge

For ordinary endpoints the XOR of three edges must equal the direct edge. The possibilities are a repeated edge plus the direct edge, or the three remaining sides of a transverse plaquette. A remote repeated edge is a disconnected vacuum excursion; its additive excitation costs give equal raw and folded contributions, canceling identically. The remaining overlapping repeated edges and plaquette paths lie within a fixed local neighborhood. For complemented endpoints the six required flips exhaust the budget: the connecting edge at the three other layers is used once each. There are no remote paths. Thus these coefficients extend beyond the finite controls whenever the transverse periods avoid short wrapping cycles (R>=5 is sufficient here); R6/R7 agreement alone is not being used as the proof.

The displayed coefficient is a matrix element in the canonical energy-N2 block. A separately chosen local normal-form or nonlocal internal block gauge can change the apparent third-order hopping by lower-order commutators. Do not identify it with a different gauge without transforming the prepared states and observables consistently. Within this canonical frame it is a genuine derived neutral edge-operator entry; the canceled ordinary plaquette loop term must not be retained as a separate third-order vertex.

For an orthogonal prepared pair of background-mode states, the identity entry is elastic and the x complemented entry gives the matrix element -Jlambda^3 <beta-prime|Xbar_i Xbar_j|beta>/4. Nonzero response still requires that actual matrix element, matched heavy/background preparation and consistent dressing. It does not establish equality of vacuum and heavy-sector ground states, a complete on-shell scattering amplitude, universal coupling, or a fermionic matter interpretation.

## SHA-256 identities

- `/tmp/neutral_third_order_element.py`: `1ef1b872fec19892e024ccaa7e03aeb042e893a22086e85e3257a9492a691af6`
- `/tmp/neutral_third_order_element.json`: `8fca6749634db037edda48f05d530138daecff9c9f0e6098b244309d467e8f0e`
- `/tmp/neutral_third_reviewer.py`: `89395b9ece160871bcc89e3178691d947e4d9d48af0a32f2641742f109fb9132`
- `/tmp/neutral_third_reviewer.json`: `645cc7803b50232d5dbb3bd57f4047f4e173234b7edff007d05961dd91e2c068`
