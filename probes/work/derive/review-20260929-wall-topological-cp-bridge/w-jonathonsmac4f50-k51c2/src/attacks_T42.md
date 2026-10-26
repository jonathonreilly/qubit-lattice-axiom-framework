# Attack on T42: Strong CP gauge side: the theta-free gauge weight is imported; no topological charge

Read: docs/MINIMAL_AXIOMS_2026-06-29.md and PRIMITIVE_REGISTRY_CHECK.md, both in full; the native positive-class, licence, narrowing, parity-gate, no-winding-carrier, recorded-set Gibbs and handed-rule notes; archive/chains/july-theta-era.md. Author: Claude Sonnet 5.5, same vendor family as the supervisor (Opus 5.5): same-family checks, not independent referees.

## Verdict in plain words
Not passed; the price is tighter. The zero of the gauge angle rests neither on the Wilson form nor on a whole-number winding count (W3 is idle). It rests on one premise, POS: the gauge-history measure has no complex phase, and that survives coarse-graining. The retained locality licence removes the textbook CP-odd terms but is not closed under unions of licensed terms, so it should not be the protector. POS comes free if gauge links are records under Admissibility (wall T27) and the Euclidean weight is the quantum weight (T15).

## The wall (checked)
- Plain: The strong-force twist angle comes out zero only because the gauge weight is assumed positive for every configuration; a weight carrying the twist would be complex. The axioms do not say so, and do not make force fields records. The winding count does not protect the zero.
- Precise: from the four axioms and registered primitives, derive that no CP-odd phase enters the quantum weight of SU(3) link histories (real theta_gauge, or a local CP-odd marginal term), in every effective description. A class choice fails.
- Real? Yes. Unsolved in docs/, archive/, 36 open PRs. Corrections: "Wilson-type" is stronger than needed (the theorem uses only non-negative masses, THETA_GAUGE_NATIVE_POSITIVE_CLASS...:100-102); W3 does not belong, being re-scoped non-gating (archive/notes/docs/THETA_RETIREMENT_BASIS_REMATCH_2026-07-04.md:140-144).

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| POS: history measure (with fermion determinant, T43) non-negative | supplied model | THETA_GAUGE_NATIVE_POSITIVE_CLASS...:36,64-102,132; WILSON_REAL_POSITIVE...:36 | e^{i theta q} weights allowed | audited theorem; marginals stay non-negative (:120) | derive from records (T27) |
| Licence P-FUND-1TICK | named conditional | PER_PLAQUETTE_LICENSE_ONE_TICK...:160-168 | clover, E.B allowed | 06-11 note; here | done |
| Proper rotations only | axiom | MINIMAL_AXIOMS:38 | improper symmetry gives theta in {0, pi} | PARITY_MEASURE...06-08:29-37; handed rules exist | owner (T23) |
| Gauge links are records; Euclid weight = quantum weight | hidden | MINIMAL_AXIOMS:60-62,82 | POS lacks axiom source | links need several qubits (2026-09-24) | none cheap |
| Integer Q exists (W3) | reading | THETA_GAUGE_SUBSTRATE...:82-95 | nothing changes | idle | Luscher price (done) |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 records-Gibbs | POS is Admissibility's probability, kept by coarse-graining | Wilson form, licence | links are records; Euclid weight = record law | missing identification lemma; checked: plaquette is a record clique in 0/24 orders; on the doubled lattice the licence equals a role-site neighbourhood, and role sites hold no records (09-04 note) | T27 + T15 | T42 becomes T27+T15; T28's Wilson form leaves the theta question | wounded (identification) |
| R2 outside: improper symmetry (Essin-Moore-Vanderbilt PRL 102, 146805 (2009); Vafa-Witten PRL 53, 535 (1984)) | exact P or T fixes theta in {0, pi} | POS | axiom-level improper symmetry | lemma: on planar supports proper covariance gives mirror invariance, for geometric link action (checked); star supports still carry P-odd operators | owner axiom | T23, T43 | wounded (symmetry must be imposed) |
| R3 misframed | ask: is the microscopic gauge measure non-negative and time-reflection symmetric? | Wilson form, Q | nothing new | theorem already holds under POS | cheap | T42 splits; W3 leaves | survives |

## Test run
- Pre-registered (T42_scratch/PREREG.md): licensed supports are star and plaquette only; no licensed E.B, E.curl E or clover; unions unlicensed; plaquette not a record clique; proper covariance kills sin(plaquette); under 1e-3 of canonical SU(3) plaquettes admissible at eps = 1/30.
- Scripts: T42_scratch/{census,parity,mc,comm_id}.py, outputs beside them.
- Result: Z^3 maximal licensed supports: 6-link star, 4-link plaquette (Z^4: 8-link star). E.B 0/1029; E.curl E 0/1764; clover 0/7203; two-plaquette 0/3084; no licensed two-object support spans 3 axes. Star plus plaquette: 0/12 licensed, 12/12 contain an E.B support. sin(plaquette) orbit sum is 0; 44/44 plaquette monomials P-even; E_z sin(P_xy) and E_x E_z(y) P-odd; abelian star: lowest P-odd degree 6; SU(2) E1.(E2 x E3): norm 6.93, cyclic-invariant, odd under arm swap. {sin P, circulation E} = -2i[H_E, cos P] (exact). SU(3) beta = 6, 4^4: <P> = 0.600 (anchor 0.5934), median ||1-U_p|| = 1.13; fraction below 0.5 is 6e-3, below 0.25 is 3e-5, below 0.1 none in 4.6e5.
- Reading: all as pre-registered. The licence removes marginal carriers only; P-odd star terms exist; Luscher-admissible sectors are priced out at canonical coupling.

## Outcome
PRICED. T42 rests on POS (with T15's Euclid-weight reading). Argument: Theorem T needs only non-negative masses, which survive marginalisation; the licence does not survive unions. The other closed protector is an exact improper symmetry (T23). Siblings moved: T27, T15, T23, T28, T43.

## Claims and labels
- Native positive-class theorem, marginal positivity: proved (retained_bounded, audited 2026-07-05).
- Licence census, E.B/clover exclusion, union failure, Gibbs non-clique, parity counts, SU(2) operator, commutator identity, plaquette statistics: checked.
- Second-order generation of E.B from licensed terms: suggested.
- POS from records; Z^4 events reading: reading. Luscher, Essin-Moore-Vanderbilt: templates only; 1/30 bound from memory, unused.
