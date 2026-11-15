**Searches run.**

- Read `ref/README.md` first. It identifies “Ledger rows: main/docs/audit/data/ledger/” (`ref/README.md:2`).
- Initial terms: `K-INV`, `invariant-algebra`, `invariant algebra`, `dyadic`, `Peter.Weyl`, `block.*homomorphism`, `decimation`. Searched `ref/main/docs`, `ref/pr*/`, `ref/ym/`, and the TOE folder.
- Follow-ups: `Bratteli`, `AF.algebra`, `invariant.*embedding`, `embedding.*invariant`, `characterless`, `good.sector`, `level-matched`, `refinement`, `H-BLOCK`, `block.*map`, `gauge.*averag`. Included other TOE parts, drafts, referee reports, prior digests and `LIT_*.md`. Used only the permitted read commands. No internet, git or edits.
- Path abbreviations below:
  - `T` = `repo/.claude/science/physics-loops/toe-assembly-20261104`
  - `M` = `ref/main/docs`
  - `Y` = `ref/ym/.claude/science/physics-loops/ym4d-hard-route-20261030/library`
  - `G` = `ref/pr10126/docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md`
  - `D` = `M/DYADIC_EVEN_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md`

**Already in the repo.**

- **The target is kinematic.** K-INV asks for a coarse-to-fine invariant-algebra embedding, independently of states and updates. The owner requires a “unital injective *-homomorphism,” cell covariance and exponential locality. Charged fields and Gauss generators receive no map. (`T/TOE_ASSEMBLY.md:252`; `T/ZM1INV.md:29–30`, “independently of states and updates”.) The brief asks for an instance on a U law and on O, or an obstruction for a named class. (`briefs/KINV.txt:1`, “construct such a map … or prove none exists for a named class”.)

- **The immediate predecessor remains open.** ZM1INV is frozen author-side mathematics; R1–R6 are “referee closures, unrefereed.” It neither constructs the zoom nor proves impossibility. (`T/ZM1INV.md:5`, “The target remains open”.) The referee records “None to ZM1-I1[INV] or to K-INV” under counterexamples. (`T/ZM1INV_REFEREE.md:311`.)

- **Characters and the locked-vacuum reduction are already available.** Theorem 2.1 supplies characters for locked even-register U and O witnesses. R1 supplies an oriented, base-tick-stationary character for every odd U register. (`T/ZM1INV.md:42`, “is a character”; `:56`, “invariant under the base tick”.) Character pairs have zero truncated invariant correlations. Theorem R therefore reduces the locked base-tick zoom to K-INV for any coarse register; R2 supplies the O-fine/U-coarse reduction. (`T/ZM1INV.md:50`, “both truncated functions vanish”; `:70`, “holds exactly when K-INV holds”; `:76`, “equivalent to K-INV(O; m₁, L)”.) Plaquette updates require separate stationarity. (`T/ZM1INV.md:74`, “not included”.)

- **The old trace obstruction does not transfer directly.** R3 gives at least two tracial states on each coarse invariant algebra, for every U register and O. The old argument also used the removed generator identity G1. (`T/ZM1INV.md:86`, “at least two tracial states”; `:90`, “cannot be applied directly”.) This leaves other trace arguments open. (`T/ZM1INV.md:90`, “does not disprove every possible trace obstruction”.)

- **Neutral full-matrix registers are excluded, with stated scope.** Theorem N and R5 exclude unital embeddings of characterless algebras into even-register U and O invariant algebras, regardless of localization. (`T/ZM1INV.md:96`, “no unital `*`-homomorphism”.) GB1Z2L5 makes the odd-register extension explicit and excludes the stated Z₂ source. Its frozen results confer “no retained or audit status.” (`T/GB1Z2L5.md:5,7,59`.) This does not exclude K-INV: the coarse invariant algebras themselves have characters. (`T/ZM1INV.md:98`, “R5 gives no obstruction to K-INV”; `T/GB1Z2L5.md:13`, “K-INV is unaffected”.)

- **Noncommutative corners remain available.** For every U register, Theorem 8 constructs a nonzero corner containing an M₂ algebra, with the corner projection as unit. (`T/GB1Z2L5.md:89`, “admits a non-unital embedding of M₂”.) The locality theorem separately forces a nonzero map to be globally unital under its uniform-locality and separating-block hypotheses. (`T/GB1Z2L5.md:75`, “is unital, even if unitality is not assumed”.)

- **A positive path-sector construction exists.** At `m=m₁=1`, Theorem S identifies the good sector of a fine path with a coarse link factor and interior colour factors. Its interior-gauge commutant is the full coarse link algebra. (`T/ZM1INV.md:114–119`, “full coarse link algebra on the first factor”.) A global extension remains open. (`T/ZM1INV.md:124`, “Compatibility across local supports and defect sectors remains to be constructed”.)

- **Orthogonal projection images constrain localization.** Theorem F′ excludes disjoint exact supports for two nonzero orthogonal coarse projections. R6 gives the exponential-locality version: their distances to two disjoint fine-region algebras sum to at least one half. (`T/ZM1INV.md:130,134–142`, “`δ₁+δ₂≥1/2`”.) This does not establish literal common support for exponential tails. (`T/ZM1INV.md:144`, “does not establish literal common support”.)

- **Exact regrouping is available with larger content.** Z0 regroups the base law exactly, preserves fine gauge transformations and has content growing exponentially in block volume. (`T/ZM1.md:97–103`, “the pair is exact”, “`exp(c L^3)`”.) Z1 and Z2 concern narrower free constructions; they do not settle nonlinear interacting embeddings. (`T/ZM1.md:143`, “not decided here”; `:279`, “not … arbitrary separated local block observables”.) Their status is conditional author-side mathematics, “not independent audit status.” (`T/ZM1.md:18`.)

- **A coherent even-algebra refinement exists in a different model.** The supplied one-dimensional massive chain has unital injective even embeddings with exact composition and preserved physical interval support. (`D:130–155`, “unital injective isometric *-map”, “`rho_(l,m)rho_(m,n)=rho_(l,n)`”.) Its scope excludes interacting and higher-dimensional conclusions. (`D:793`, “no … interacting or higher-dimensional theorem”.) Ledger status: `"effective_status": "unaudited"`. (`M/audit/data/ledger/dy/dyadic_even_refinement_bounded_theorem_note_2026-10-12.json:33`.)

- **Later chain refinements separate state, dynamics and geometry.** State-adapted refinement preserves the chosen state and the geometric section limit, while finite-scale locality and exact energy-flow compatibility fail. (`M/STATE_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:5,45–50`, “infinite support”, “failure of exact energy-flow intertwining”.) Energy-adapted refinement preserves state and energy exactly, but its stated maps fail exponential coefficient decay and spatial intertwining. (`M/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:5,320,336`, “rules out exponential”, “translations fail exact intertwining”.) Both ledger rows remain `"unaudited"`. (`M/audit/data/ledger/st/state_adapted_refinement_bounded_theorem_note_2026-10-12.json:34`; `M/audit/data/ledger/en/energy_adapted_refinement_bounded_theorem_note_2026-10-12.json:34`.)

- **Two gauge-refinement analogues are recorded.** RC-6 constructs a finite-group, one-dimensional pure-gauge refinement that is “unital, injective, of finite range and translation covariant,” with gauge equivariance but not G1. It is explicitly an analogue, not the five-mode construction. (`T/ZM1I1A.md:130–144`.) Consolidated #9928 supplies a gauge-, winding- and translation-covariant level-matched polar isometry in a 2+1D Z₃ toy. Its scope is “an isometry in a 2+1D Z_3 toy,” with no register continuum limit. (`G:287,295,310–311`.) Consolidation status: “author statements for review.” (`G:11`.)

- **Finite-region approximation retains boundary sectors.** The Peter–Weyl note supplies spatial and register-cutoff error bounds for a supplied SU(3) Hamiltonian with finite local energy. It is “not a free deterministic encoder” and makes no uniform all-energy fixed-cutoff claim. (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:73–75`.) Its cutoff “does not project onto a boundary singlet.” (`same file:83`.) Ledger status is `"unaudited"`. (`M/audit/data/ledger/ga/gauge_wilson_local_observable_finite_region_pw_approximation_bounded_theorem_note_2026-09-07.json:30`.)

**Failed attempts on file.**

- **Neutral matrix registers:** composition with a fine character would produce a character of M_D. This is the failing step of Theorem N/R5. (`T/ZM1INV.md:94–98`, “Compose with the character”.)

- **End-equivariant link decimation:** independent first/last fine-end spectra cannot realize the prescribed coarse-link spectrum along a multi-link path. One-link paths fail cell covariance for `L≥2`. (`T/ZM1INV.md:102–110`, “a contradiction”, “impossible for `L≥2`”.) This tests a factorwise full-link construction; the O argument is not covered. (`T/ZM1INV.md:112`, “O parity case is not covered”.)

- **Good-sector decimation with representative end data:** coarse incompatible end-number projections multiply to zero, while the prescribed images on distinct fine links have nonzero product. (`T/ZM1INV.md:126–128`, “A homomorphism preserves products”.) Extending the good-sector map by zero fails unitality. (`T/ZM1INV.md:124`, “is not unital”.)

- **Old full-algebra Gauss embedding:** trace covariance forces adjacent representatives; locality and density then force `L=1`. The failure is G1 together with locality and the fixed coarse form. (`T/ZM1I1A.md:40–46`, “`L=1`”, “exact generator identity (G1)”.) Those are replaced owner conditions, not a K-INV obstruction. (`T/TOE_ASSEMBLY.md:252–254`, “Neither full-algebra obstruction … applies directly”.)

- **Transported linear charged fields:** ZM1 Attack 1 fails when declaring the transported sum a fermion field. (`T/ZM1.md:384`, “`Psi_u` is a fermion field”.) Attack 2 fails when assuming link operators act as c-numbers; its stated coherence criterion is excluded. (`T/ZM1.md:386`, “does not rule out every state-dependent approximation”.)

- **Conserved-projection compression:** the assumed tile-local Gauss projection uses boundary links owned by neighbouring tiles. The classification and rank inference remain unproved. (`T/ZM1.md:390–392`, “No exhaustive classification is shown”, “No general conclusion on bounded content follows”.)

- **Vacuum-only matching in #9928:** the vacuum-carrying isometry sends parent excitations outside the child low-energy window. Level matching is the recorded repair. (`G:311`, “Carrying the vacuum is not enough”.)

- **Exact compatibility for fixed Haar refinement:** the chain supplies a strict state-expectation counterexample and a nonzero flow-generator discrepancy. (`D:553`, “exact scalar counterexample”; `D:577`, “The flows cannot intertwine for all t”.) The later adapted refinements above retain their own locality or covariance failures.

- **Fine-to-coarse one-qubit morphism compression:** the older block-spin note excludes the direction M₂₅₆→M₂ by matrix divisibility. (`M/BLOCK_SPIN_CP_COMPRESSION_COLOR_REEMERGENCE_NARROW_NO_GO_NOTE_2026-06-08.md:27–32`, “`256 ∤ 2`”.) This differs from K-INV’s coarse-to-fine invariant embedding. Its ledger remains `"unaudited"`. (`M/audit/data/ledger/bl/block_spin_cp_compression_color_reemergence_narrow_no_go_note_2026-06-08.json:32`.)

The three K-INV attacks do not exhaust invariant-only embeddings. The referee also records that two share the representative-end premise. (`T/ZM1INV.md:167`, “None rules out arbitrary invariant-only embeddings”; `T/ZM1INV_REFEREE.md:314`, “share the premise”.)

**Overlap with this lane's results.**

not run. The brief says “KINV … pass 1”; K-INV remains listed as open. (`briefs/KINV.txt:1`; `T/ZM1INV_REFEREE.md:313–315`, “Open by name”.)

**Missed inputs.**

- **The character tool was already used.** The brief calls it a tool “the three failed attacks did not use,” but neutral-register failure already composes with the character. (`briefs/KINV.txt:1`; `T/ZM1INV.md:94–98`, “Compose with the character”.) This changes the starting inventory: character obstruction is an existing constraint, not an untried neutral-register attack.

- **Do not replace the invariant algebra by an abelian algebra.** The brief’s “abelian structure it forces” needs the corner qualification: GB1Z2L5 explicitly contains a non-unital M₂ corner. (`briefs/KINV.txt:1`; `T/GB1Z2L5.md:89`, “non-unital embedding of M₂”.) A construction must reconcile those corners with the global unit and character sectors.

- **Use S together with its unresolved extension.** The path-sector isomorphism supplies a concrete local building block. The missing input is a “unital, globally compatible extension … to defect sectors.” (`T/ZM1INV.md:16,114–124`.) R6 requires handling incompatible end data jointly rather than placing both images near disjoint representatives. (`T/ZM1INV.md:142`, “cannot both be approximated to better than `1/4`”.)

- **Use coherent refinement examples without importing their missing interfaces.** Dyadic refinement supplies exact composition. RC-6 supplies a gauge-equivariant finite-group analogue. Energy-adapted refinement shows that exact state and energy matching can coexist with failed exponential decay and translations. (`D:150`, “proves … composition”; `T/ZM1I1A.md:134`, “translation covariant”; `M/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md:320,336`, “rules out exponential”, “fail exact intertwining”.) These change which properties require separate verification.

- **Retain boundary representations in finite-region encodings.** A forced boundary-singlet projection discards the Peter–Weyl note’s valid global physical loop state “with probability1.” (`M/GAUGE_WILSON_LOCAL_OBSERVABLE_FINITE_REGION_PW_APPROXIMATION_BOUNDED_THEOREM_NOTE_2026-09-07.md:79–83`.) Local invariance and support on invariant vectors cannot be substituted for each other.

**Consumers.**

- **ZM1-I1[INV] in locked base-tick vacua:** the weakest sufficient handoff is precisely a K-INV map for some allowed coarse register and `L≥2`; the character comparison then vanishes. (`T/ZM1INV.md:50,70`, “both truncated functions vanish”, “holds exactly when K-INV holds”.)

- **ZM1-I1[INV] in non-character vacua:** K-INV supplies only the map. The consumer additionally needs class-(a) comparison on its actual images. ER requires relative envelope matching; named fine channels are not automatically in the image. (`T/ZM1INV.md:167`, “does not prove that a named channel is in the image”; `T/ZM1_OBS.md:284–292`, “tail envelopes … agree to relative order”.)

- **LZ1-i:** useful invariant dynamical data require the separate spectral-transfer hypotheses. K-INV alone supplies no speed statement, and a character vacuum has no centered invariant sector. (`T/ZM1INV.md:177`, “does not establish a common speed”, “centered physical sector is zero”.)

- **GA2, ZM1-G and T0-start:** they need a specified observable dictionary, state and quantified comparison with the relevant group-valued theory. (`T/GA2_Y2.md:176`, “controlled gauge-invariant correlator comparison”, “with quantified errors”.) Composition requires “a common dictionary and propagated errors.” (`T/ZM1_OBS.md:176`.)

- **YM H-BLOCK:** the minimum interface is a countable block/smeared family whose convergent expectations supply a joint limiting state. It remains a named hypothesis, “not a consequence of curvature cumulant bounds.” (`Y/port/p8b-limits.md:57`; `Y/open-registry.md:679`, “H-BLOCK”.) That port is research text, “not yet checked by another model.” (`Y/port/p8b-limits.md:3`.)

- **Full ZM1 and assembly:** a one-step map must eventually belong to a compatible trajectory with controlled content. Full ZM1 requires a “fixed point or a controlled trajectory”; AS0 requires “one law,” “one zoom” and “one vacuum.” (`T/TOE_ASSEMBLY.md:314,702`.)

- **R-CS, MT1-S and CG1’s charged 16:** they require a separate charged-sector bridge. The owner states they “get no zoom from this map.” Finite invariant strings do not supply a uniform straight-string limit. (`T/TOE_ASSEMBLY.md:255`; `T/ZM1INV.md:175`, “no uniform-in-length bound”.)