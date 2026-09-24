# Assumptions and imports

| Item | Role | Provenance | Open bridge / consequence |
|---|---|---|---|
| Lattice axiom | Framework background | `docs/MINIMAL_AXIOMS_2026-06-29.md`; unchanged between selection main `5efa36e7c357ae2a62ee586a5407f90982f6ded9` and latest reviewed main `8cc5f114f0d703100d6a7a764a1c689c7a56d65f` | Does not derive a finite ring geometry or its embedding in the cubic lattice. |
| Qubit axiom | Framework background | Same source revisions as the lattice-axiom row | Does not derive the three-state hard-core matter carrier or integer-spin link spaces. |
| Admissibility axiom | Framework background | Same source revisions as the lattice-axiom row | Does not supply a transition law, Hamiltonian, or time evolution. |
| Record axiom | Framework background | Same source revisions as the lattice-axiom row | Does not fix formation location/rate, the marked output, or this observable map. |
| Scale-reference, kinetic-isotropy, realized-state primitives | Approved primitives checked in the registry | `docs/audit/data/axiom_premise_nodes.json`; primitive registry unchanged between the selection and latest reviewed main | Supply units/form/pointwise slot only; none supplies the dimensionless dynamics or selected output used here. |
| Six-site staggered hard-core model and Gauss background | Imported conditional Hamiltonian and carrier | Open PR #8831 exact head `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`, stacked on open PR #8672 head `fe6dc2c5ef061fa1e0051063d49178f23b872c13` | Neither dependency is landed on main. The present result is conditional on this sector and representation. |
| Integer-spin normalized link shift `-sqrt(1-m(m+a)/C)` | Imported representation rule, then expanded here | `FAST_VACANCY_MOTION_AFTER_FORMATION.md` at the recorded #8831 head | Other link representations need a new derivation. |
| First-mark output `(q,E)=((1,-1,1,0,1,1),(1,0,0,0,0,1))` | Imported initial vector, frozen before propagation | Same #8831 source file and exact SHA256 `76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb` | Other states may have different tails and observable values. |
| Vacancy projector at site B3; `K=delta=1`; times `1/4,1/2,1` | Frozen target conventions | `../postmark-electric-validity-20260923/TARGET.md` | A chosen test, not a framework-derived physical readout. |
| `H2,S`, `H4,S`, rotor path, and one-vacancy identity `H4,S=M_S^2` | Supplied model operators with the path reconstruction checked in this block | Exact legal-hop enumerations and dense cross-check in the adjacent science evidence directory | Full fixed-time generator comparison remains open. |
| Exact zero mode and fixed-index Gegenbauer form limit | Derived conditionally from the supplied `A_S` hop map; no new operator convention | `ZERO_MODE_AND_GOEGENBAUER_LIMIT_2026-09-24.md`; residue identities and endpoint compactness argument | Analytic result, not implemented by the runner's finite-spin eigensolver; moving-index phase control remains open. |
| Taylor expansion, matrix calculus, finite Jacobi spectral theorem, Friedrichs extension, strong convergence of uniformly bounded functional calculus | Mathematical machinery | Standard named mathematical methods; no literature conclusion imported | Each use is stated with its hypotheses in the notes; essential self-adjointness and finite-spin selection remain open. |
| SciPy/NumPy eigensolvers and double precision | Numerical tools for diagnostics only | `spectral_fixed_time_probe.py` runtime environment | No enclosure, asymptotic proof, or tail theorem. |

The primitive-registry check found no registered primitive supplying the imported Hamiltonian, spin-link representation, actual formation output, dynamics, or observable map. No axiom update is proposed.
