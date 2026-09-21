# The source link in the amplitude layer — state of knowledge for the owner (blocks 53–55; 2026-09-21)

**What this is.** One page on what three blocks established after the instruction "ok lets work the source link into the amplitude layer". Nothing here is adopted; every block is an open hand-off PR against `main`; PR numbers are evidence addresses, not status. Author checks only; no independent review has taken place on any of it. The axioms memo and the parked-decisions registry were read in full before the first block.

**The starting point.** The record layer supplies the source (the record count) and not the carrier (decision record of blocks 39–52, #8555). The weak-field packet on `main` is three *supplied* pieces: a field equation (`−Δ_lat` with the zero mode projected out), a source (`ρ = |ψ|²`), and a test response (`S = L(1 − φ)`, force `+m∇φ`). The axioms contain no time metric, no amplitude dynamics and no conserved energy.

## Three supplied clauses

| | clause, in one sentence | what it copies or fills |
|---|---|---|
| A | **No master clock.** Every site has a tick rate; a site's rate is set by its six neighbours' rates through one covariant rule; only ratios of rates mean anything. | the Admissibility axiom's form (one covariant nearest-neighbour rule); the memo's silence on a time metric |
| B | **The phase is timed by the local clock.** One moving record is an amplitude over sites with the site's qubit as its content; at each site it advances in that site's own time. | the open gate on update laws; the owner's reading that records move; block 44's "content = direction of travel" |
| C | **The books balance.** The rate field obeys a static law and, together with the amplitudes it times, keeps a ledger. | nothing in the axioms; a plain premise |

## What is established (exact unless marked executed)

| # | Statement | Evidence address |
|---|---|---|
| 1 | Under A every rule, linear or not, has the same weak-field form: `log w` at a site = the average over its neighbours. No mass term (it would single out a rate). On a closed lattice only the zero-sum part of a source enters; the constant of `log w` is the unit of rate, which no ratio sees. | block 53, #8568 |
| 2 | Under A a record cannot pin a rate; it enters as a ratio `κ` to its neighbours' mean, that is as the additive source `log κ`: exact superposition, symmetric pair term, clocks slow near records if `κ < 1`. The second order of the rule is not fixed by A. | block 53, #8568 |
| 3 | A record whose *waiting time* is timed by the local clock gathers where clocks run slow (stationary law `1/w`): a drift, with no inertia. | block 53, #8568 |
| 4 | Hermitian, rotation-covariant nearest-neighbour generators on two-component amplitudes form a three-parameter family; one term couples content to motion, and its velocity operator is the content. If lattice inversion is *added* as a symmetry (the axiom names proper rotations only) and the content reverses under it, that term is all there is: a walk with the qubit as its coin. **One walker has no rest energy** — nothing in `M₂(ℂ)` anticommutes with the three content matrices. | block 54, #8570 |
| 5 | Under B the generator is `wH`; the conserved quantity is `Σ|ψ|²/w` (the same `1/w` as row 3). In a uniform gradient a translated packet evolves faster by exactly the ratio of the clocks, and the wave vector falls at `(ratio − 1) × energy` in every state: **force = energy × gradient, exactly.** | block 54, #8570 |
| 6 | Rays fall at `−w²M∇u + 2(v·∇u)v`; `M` is the unit matrix at long wavelength for the walk, *because the content matrices anticommute*: weight and inertia are tied by the qubit. A walker with decoupled content falls at (weight)/(inertia), two unrelated numbers. On the lattice `M = diag(cos 2k_j)`: direction dependence of second order in the wave vector (16 % at 0.5, 4 % at 0.25; block 51's wind: 30 % at every distance). | block 54, #8570 |
| 7 | Executed: packets follow clouds of rays to 5 parts in 10⁴ (line) and 2 parts in 10³ (three dimensions). **They also drift sideways** by `gT/(2k)` along (gradient) × (motion), the same in five orientations: a wave correction that depends on the wave number and the walk's handedness. "Everything falls alike" is a statement about rays. | block 54, #8570 |
| 8 | Under C the source is not a separate choice: `d⟨H_w⟩/du_x = e_x`, the amplitude's **energy density**; the ledger is kept with that source (mean removed), and with any other source `s` it moves at the exact rate `Σ(e − s) du/dt`. A body at rest has `e = m w |χ|²` — the packet's `|ψ|²` times the rest energy and the local rate; a moving body sources its energy. | block 55, #8571 |
| 9 | Every pull is matched by an equal and opposite pull iff each body sources in proportion to its energy. With sources that count bodies, a heavy and a light body left alone would push themselves along. Executed: with the probability density as source the two wave vectors' changes fail to cancel by one half; with the energy density they cancel to 3 parts in 10⁵ and the ledger holds to 10⁻¹¹. | block 55, #8571 |
| 10 | A and C together: the field's own energy has weight one; the unit of rate cannot be a variable of the ledger (so the source enters with its mean removed — the packet's projection a second time); the coupling `γ` is a pure number; the second order that row 2 left free is fixed — through second order the law is the averaging law for `√w`. In the continuum this is Einstein's second static theory of 1912, which he reached by the same action-and-reaction argument. | block 55, #8571 |

## The weak-field packet, piece by piece (correspondence of form; no gravitational claim)

| supplied on `main` | within the clauses |
|---|---|
| operator `−Δ_lat`; zero mode projected out | A (row 1); again from A + C (row 10) |
| test response `S = L(1 − φ)`, `F = +m∇φ` | B (row 5): `φ = −log w`, `m` = the body's energy |
| inertia — not in the packet | B + the qubit (row 6) |
| source `ρ = |ψ|²` | C (row 8): energy density; `m w |χ|²` for a body at rest |
| coupling and units | one pure number `γ`; row 2's `κ = exp(−(γ/6) E/w̄)` if records are pulled as amplitudes are |

With all three: a body of energy `E` draws every long-wavelength packet at `γ E w̄/(4πr²)`, whatever the packet's energy and direction.

## The forks that are the owner's

1. **Do sites have clocks?** A tick rate per site is a new object. A is a candidate filling of the time-metric gate; it copies the Admissibility axiom's form and adds "only ratios".
2. **Is a moving record an amplitude over sites?** B needs that. The axioms have no amplitude dynamics. Within B the generator is forced up to three numbers; the walk needs a soldered content and, for exactness, inversion as an added symmetry.
3. **Do the books balance?** C is a plain premise. Without it nothing constrains the source.
4. **Does an amplitude that has formed no record source anything?** Row 8 says what the source is *if* it does. "Only records are readable" points the other way; then rows 9 and 2 give `log κ = −(γ/6)E` for records, and what happens to the ledger when a record forms is open. The parked statistical postulate is not used and is not re-raised here.
5. **Rest energy.** One walker has none. In the executed runs it is motion across the gradient. Whether binding two walkers supplies one inside `M₂(ℂ)` is queued on `ai/probes`; the parked enlargement (entry 4) is not touched.
6. **Lengths.** B times phases and says nothing about distances. A field of clock rates gives the fall of slow bodies in full and *half* of the comparator's bending of light. A clause for lengths is not proposed.
7. **Delay.** The law of A and C is static: it acts at a distance. A field with its own motion is not worked.
8. **`γ`.** One pure number; nothing in the clauses fixes it.

## What is simple enough to say to a layman
There is no master clock; each place keeps its own time and only comparisons count. Then a place's clock rate is the average of its neighbours', and things that slow clocks add up. A moving thing whose phase keeps local time is pulled towards slow clocks, harder the more energy it has — and because of how a qubit's three directions multiply, its inertia grows in the same proportion, so everything falls alike. If the books are to balance and every pull is to be answered by an equal pull, the thing that slows the clocks has to be energy. One number is left over.

## Integration order
#8568 → #8570 → #8571, each independent against `main` (each appends to the shared pack records; rebuild in that order). Follow-ups are on `ai/probes` (the ray limit as a theorem with its sideways correction; composite bodies; a clause for lengths; `κ`; discrete-step walks; a sideways-drift grid).
