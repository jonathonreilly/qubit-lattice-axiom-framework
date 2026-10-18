# Native N2 probe-loop check

Disposition: PASS for the singleton-labelled channel and loop/source statement, with the important three-spin labelling correction below. Exact physical-bit and symbolic-path scratch controls were independently executed; no repository edits.

## Physical classification and signs

At periodic longitudinal length four, N=2 means exactly one column has one contiguous nontrivial interval (length1,2,or3) relative to an aligned reference; all other columns are aligned. A length-three interval relative to background s is a singleton relative to the background with that column fully reversed. It is NOT a separate hopping branch with the original length-three background held fixed. For example, flipping its missing-layer site and a neighbor creates a fully reversed first column and a singleton on the neighbor. The appropriate invariant K1 labels are background s, singleton layer z, and singleton position i. In those labels every length-three configuration is already represented after complementing its background column. Half-column length-two states have no K1 transition and are static at first order.

For an initial singleton, XX gives -Jlambda and mixed YY gives -Jlambda s_i s_j. Every other transverse flip either leaves the N2 sector or is the reverse of one of these hops. Thus the asserted fixed-background singleton Hamiltonian is

 T=-sum_x hopping -sum_y Zbar_i Zbar_j hopping.

I checked exact physical-bit actions on R6 by R6 by4 for 24 singleton/background cases and 24 half-interval cases, including arbitrary aligned signs: all agree, with no omitted N2 outputs. The background basis labels the actual physical states, not an independent gauge Hilbert space.

## Return polynomial

The two y links of an elementary square supply the four corner signs; x links contribute no sign factor. Four minus hopping signs cancel. The elementary loop product is precisely P_p. Among four-step returns on the square lattice, 28 backtracking/retracing paths have trivial sign, and the eight oriented square loops give twice each of the four incident plaquettes. An independent exact Z-mask path enumeration gives

 <i|T^4|i>=28 I+2 sum_(p incident i) P_p.

Periodic transverse R>=5 excludes extra four-step winding paths. For the O(tau^6) return expansion it is safer, as proposed, to use even R>=6: bipartiteness then excludes every odd return. On R5 a five-step winding return could produce an O(tau^5) term even though the fourth moment remains correct.

## Prepared transition and its interpretation

For distinct orthogonal background-mode states beta and beta-prime, the zeroth-order and two-step return pieces are scalar (the latter is4I) and have zero transition matrix element. The four-step term in exp(-i tau T) has coefficient (-i)^4/4!=1/24. Consequently

 <i,beta-prime|exp(-i tau T)|i,beta>
 =tau^4/12 <beta-prime|sum_incident P_p|beta>+O(tau^6)

for the even transverse geometry. This is an amplitude coefficient, not a probability or a guarantee that every chosen pair of modes has nonzero overlap. Selection rules or a vanishing plaquette matrix element can make it zero. For nonorthogonal or identical mode states, retain the scalar return terms.

At FIXED finite geometry a gapped-wall analytic reduction of the N2 cluster gives H_eff=common scalar+Jlambda T+O(Jlambda^2). Duhamel at physical t=hbar tau/(Jlambda) gives O_tau(lambda) norm error after removing the common fast phase. The preparation/readout must be stated in the same dressed channel embedding, or explicitly include the O(lambda) changes from bare preparation. Constants depend on the box; no uniform growing-size transfer follows automatically. Combining this error with the small-tau expansion gives the proposed O(tau^6)+O_tau(lambda), and resolving the tau^4 term in a joint tau/lambda limit would require lambda small compared with tau^4.

This derives access to the existing neutral plaquette operator through a native heavy return path. It does not establish equality between a vacuum collective ground and the heavy-sector dressed ground, nor a new independent gauge field, a three-dimensional fermion, universal matter coupling, an actual detector implementation, or empirical identification.

Scratch: /tmp/neutral_probe_loop_reviewer.py and /tmp/neutral_probe_loop_reviewer.json. Exact controls use R6 only and do not diagonalize the microscopic Hilbert space.
