# Assumptions and imports

| Item | Role | Current provenance | Open bridge / consequence |
|---|---|---|---|
| Four framework axioms and registered primitives | Framework background | Current origin/main e37967e326c2bdb429bd3106d34158bd5420e9c0; the source notes do not modify them | They do not derive the finite ring, Hamiltonian, spin-link representation, first-mark output, or observation map used in this campaign. |
| Six-site staggered hard-core model and Gauss background | Supplied conditional Hamiltonian and carrier | Canonical finite-model notes on current main, including FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md and POSTMARK_ELECTRIC_CORE_AND_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-24.md; historical PRs #8831/#8672 are closed without merge | The results remain conditional on this supplied model and sector; no axiom derivation is claimed. |
| Integer-spin normalized link shift -sqrt(1-m(m+a)/C) | Supplied representation rule, expanded in the finite-spin notes | Canonical fast-vacancy and zero-mode notes on current main | Other link representations need separate derivations. |
| First-mark output q=(1,-1,1,0,1,1), E=(1,0,0,0,0,1) | Frozen initial state | Canonical supplied-model and post-mark notes on current main | Other preparations can have different tails and readouts. |
| Vacancy projector at site B3; K=delta=1; times 1/4, 1/2, 1 | Frozen target conventions | TARGET.md in the pushed campaign packet | A selected test, not a framework-derived physical readout. |
| H2,S, H4,S, rotor path, and one-vacancy identity H4,S=M_S^2 | Supplied operators plus the scoped path reconstruction | Canonical post-mark core note and paired runner on current main | Fixed-time exact-versus-candidate comparison remains open. |
| Exact zero mode, fixed-index Gegenbauer limit, moving-index symbol, central match | Conditional finite-model theorems | Canonical notes integrated on main in commits d7a3aa92b0b2f99e9a451efbbccda77de4625f68 and ddb9249c52edf56a20a13d28266f6a333c08c800 | These do not control the interior T~S^2 scalar or establish the physical readout. |
| Candidate Friedrichs realization, extension choice, H4/output passage | Downstream comparison | Candidate source in the campaign packet | Selection by the finite-spin sequence and full comparison remain open. |
| SciPy/NumPy eigensolvers and double precision | Diagnostics only | Paired runners and historical scan outputs | No enclosure or asymptotic proof. |

No source axiom or registered primitive is changed by this campaign.
