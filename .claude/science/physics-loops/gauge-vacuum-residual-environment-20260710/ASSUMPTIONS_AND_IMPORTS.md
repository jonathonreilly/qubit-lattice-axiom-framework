# Assumptions And Imports

## Minimal allowed premise set

`A_min` for the stretch attempt is:

- a finite oriented spatial lattice/cell complex once its geometry and
  boundary conditions are explicitly named;
- one `SU(3)` Haar variable per independent link;
- the Wilson plaquette weight
  `exp[(beta/3) sum_p Re tr U_p]` at `beta > 0`;
- one marked plaquette with boundary holonomy `W` held fixed;
- product Haar measure, compactness, Fubini/Tonelli, and Peter-Weyl
  orthogonality;
- the exact marked half-slice multiplier and source recurrence only at the
  scope actually established by their source notes.

## Forbidden imports

- the canonical or Monte Carlo plaquette value as derivation input;
- a fitted or hand-picked `rho_(p,q)` sequence;
- single-link Wilson coefficients identified with a multi-link environment
  without an explicit contraction theorem;
- the L_s=2 all-forward candidate-rho ansatz as a Wilson orientation theorem;
- the L_s=3 link-orbit-tied diagnostic quotient as an exact contraction;
- positivity, self-adjointness, or conjugation symmetry used as a uniqueness
  selector;
- an unproved claim that all non-marked mixed-link factors reduce to a
  representation-independent scalar.

| Item | Role in claim | Current class | Source surface | Load-bearing? | Needed for target status? | Retirement path | Disposition |
|---|---|---|---|---|---|---|---|
| finite `SU(3)` Wilson product measure | defines the actual environment marginal | retained-support target surface plus explicitly selected finite geometry | [`GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`](../../../../docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md) | yes | yes | explicit integral on the named Wilson surface | allowed; not a minimal-axiom primitive |
| finite spatial geometry/boundary condition | fixes which environment is meant | unsupported import in the target note | later L_s=2/L_s=3 notes disagree in scope | yes | yes | state and derive one exact target geometry | open |
| marked/local mixed-kernel factorization | permits stripping before identifying the environment | support-only finite packet | local-factor note explicitly leaves actual compression open | yes | yes | operator theorem from the Wilson integral | open |
| multi-link Haar/intertwiner contraction | computes actual boundary coefficients | support-only / incomplete tooling | tensor-transfer and cube notes | yes | yes for coefficient closure | exact contractor or certified bounded contraction | open |
| single-link `rho_(p,q)(6)` packet | finite local coefficient input | computed lattice input | bounded coefficient companion | no for actual environment | no | keep as local input only | allowed with firewall |
| generic positive witness | prior algebraic behavior check | unsupported import | historical runner behavior | yes if injected | no | remove entirely | forbidden |
| observed `P(6)` | comparator | observational comparator | publication surface | no | no | never use in proof | forbidden as input |
| `beta=6`, PBC, `L_s=2` | defines the bounded direct-computation target | admitted target geometry/coupling on the Wilson surface | bounded MC companion | yes for that packet | no for the exact geometry no-go | repeat on other declared geometries | explicit |
| four seeds; hot/cold starts; 4000 burn sweeps; 16000 sample sweeps; thinning 4; proposal step 0.8 | stochastic protocol choices | support-only numerical protocol | bounded MC runner | yes for the reported estimate | no for exact theorem | autocorrelation/batch-stability study or exact contractor | explicit |
| 20 batches per chain and nominal batch standard error | uncertainty diagnostic | support-only, not a calibrated confidence interval | bounded MC runner | yes for quoted `+/-` diagnostic | no for exact theorem | blocking stability, integrated autocorrelation time, ESS | explicit |
| 4/5/8/20-error-unit diagnostic thresholds | runner PASS heuristics for controls, signal, chain spread, and packet discrimination | support-only heuristic | bounded MC runner | yes for PASS labels only | no | replace with pre-registered statistical certificate | explicit |

## Cycle 2 dispositions

- The suppressed finite-geometry import is exposed and cannot be retired by a
  universal sequence: exact triality filling gives a positive cubic term at
  `L_s=2` PBC and vanishing through fourth order at `L_s=3` PBC.
- Selecting standard `L_s=2` PBC retires the geometry ambiguity only for the
  bounded Monte Carlo packet. It does not select the APBC five-unmarked-
  plaquette staging object used elsewhere.
- The actual `L_s=2` PBC fundamental coefficient is computed directly from
  the 23-plaquette unmarked measure with batch-error bounded support.
- The marked/local temporal mixed-kernel compression remains load-bearing and
  open; neither new runner assumes it.
