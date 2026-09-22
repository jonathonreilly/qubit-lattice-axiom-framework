# J:derive:the-exchange-sign-from-the-coin:a1 — w-macbookpro90c72-j3430

Attempt 1 of 3, by claude-opus-5-5 (all of `check.py` and this file). `python3 check.py` prints 6 `ok` lines, exits 0
with `FAIL` empty, and runs in about 2 s.

Exact arithmetic:
- `2H` has Gaussian-integer entries, so every product below is a Gaussian integer of small modulus. complex128 carries
  these exactly, and `gi()` asserts integrality whenever a value is read off.
- The one-site algebra is done in sympy.

Nothing is adopted. Comparators (spin–statistics, hard-core bosons, Jordan–Wigner) are named as comparators, never as
premises.

**Sources.**
- The axioms memo on `main`, `docs/MINIMAL_AXIOMS_2026-06-29.md`, quoted exactly:
  - **Qubit:** "The full one-site possibility domain has algebraic presentation `M_2(C)`. A `Cl(3,0)`-compatible
    real-algebra presentation may be used equivalently and adds no further primitive structure. No possibility is
    privileged."
  - **Record:** "A site never carries more than one record; records are permanent. … A readout value is determined
    by record content alone."
  - **Qualification:** "A choice not fixed by the supplied structure remains a named conditional or open dependency."
  - Among the "Open Gates Outside The Axioms": "the staggered-Dirac/finite-Grassmann realization".
- The walk is block 54's `H = Σ_a σ_a S_a` (PR #8570), with `S_a = p_a = −i(T_a − T_aᵀ)/2`, the symmetric one-step
  difference whose symbol is `sin k_a`. On rings it is block 78's reduced walk `H = σ₃ p` (PR #8613), whose values
  check.py reproduces (hard-core `tr H²/dim = 2/3`, and fourth traces `5/6` and `7/6` at `N = 4`).
- Context:
  - the fork probe's §4.1 (`FORK_PROBE_source_link_20260922.md`, decision record #8572);
  - three landed notes on `main`:
    - the statistics-agnostic no-go (`STAGGERED_DIRAC_SUBSTEP1_STATISTICS_AGNOSTIC_NO_FORCING_NOTE_2026-05-25.md`);
    - the rotation-exchange no-go (`FS_ROTATION_EXCHANGE_DISCRETE_INSUFFICIENCY_NARROW_NO_GO_NOTE_2026-05-28.md`);
    - the ring-monodromy note (`RING_MONODROMY_DOES_NOT_FORCE_CAR_NOTE_2026-06-04.md`).

  These are in the operator-algebra picture; this attempt works in the source-link direction's amplitude picture.
  PR #7829 (the composition gap, closed and not on `main`) reached the same boundary at the algebra level.

## 1. Statement attempted

**(a) What a composition rule for two records is.**
- One moving record is an amplitude `ψ ∈ V = ℂ^sites ⊗ ℂ²`: the qubit is its content, the walk moves it.
- Two records live in `V ⊗ V`. The exchange `P(u⊗w) = w⊗u` relabels which record is which.
- The Record axiom confines them to the hard-core space `HC = span{e_{x,a} ⊗ e_{y,b} : x ≠ y}`, which has dimension
  `4n(n−1)` on `n` sites.
- The free generator `H⊗1 + 1⊗H`, compressed to `HC`, is `H₂`.
- A **composition rule** is a choice of a `P`-invariant, `H₂`-closed subspace `K ⊆ HC`.
- The **exchange sign** `ε = ±1` is defined when `K ⊆ ker(P − ε)`:
  - `K₊ = HC ∩ Sym` gives `ε = +1`;
  - `K₋ = HC ∩ Alt` gives `ε = −1`;
  - `K₀ = HC` (the records labelled by their history) is sign-free.
- *Distinguishable by history.* A readout is determined "by record content alone". So a two-record readout is a function
  of the unordered set of (site, content) pairs, and every readout operator commutes with `P`.
  - Hence `K₊` and `K₋` are superselection sectors.
  - A history label that no readout sees makes `K₀` observationally a mixture of `K₊` and `K₋`.
  - So the exchange sign is exactly the question of which sector the records occupy.

**(b) The derivation, attempted.** It asks for a definite `ε` from four sources:
- the Record axiom;
- the Qubit axiom's `Cl(3,0)` presentation and its grading;
- "no possibility is privileged";
- the spin–statistics connection, treated as a comparator only.

**(c) The answer: no derivation is available.**
- `K₊` and `K₋` are two composition rules. Each is compatible with every axiom sentence (table in S5).
- They are different theories: on the 3-torus of side 5, `tr H₂⁴/dim = 9135/496` on `K₊` against `9183/496` on `K₋`.

**(d) The order and the observable.** Under exclusion:
1. `tr_{K₊} H₂^k = tr_{K₋} H₂^k` for `k = 1, 2` on every nearest-neighbour graph, and for `k = 3` on bipartite ones.
2. On `Z²` and `Z³` the sign first shows at `k = 4`:
   - `tr_{K₊}H₂⁴ − tr_{K₋}H₂⁴ = tr(P H₂⁴) = −8` per plaquette, i.e. `−8` per site on `Z²` and `−24` per site on `Z³`;
   - per pair of records the coin-summed exchange amplitude `Σ_{a,b} ⟨Ps|H₂⁴|s⟩` is `−2` for neighbours, `−1` for
     face diagonals and `0` at distance 2 on a line.
3. On rings of `N` sites it is `0` below order `N`, and nonzero at order `N` for even `N`. For odd `N` the two sectors
   are unitarily equivalent, so the sign is invisible to every spectral quantity at every order.

## 2. Steps

### S1 — the objects. PROVED; CHECKED
- `HC` is `P`-invariant, `P² = 1` and `[P, H₂] = 0` on `HC`.
  - `P` maps a two-different-sites configuration to one.
  - The free generator commutes with `P`, and so does the projector onto `HC`.
- So `K₊` and `K₋` are each closed under the dynamics. CHECKED on the ring of 4 and on the 3-torus of side 5
  (`31000 + 31000`), together with `H = H†` and `H₂ = H₂†`.
- Readouts commute with `P`; the argument is in §1(a).

### S2 — the Record axiom. PROVED
- "A site never carries more than one record" gives `K ⊆ HC`.
- "Records are permanent" gives conservation of the record number: `H₂` is compressed within the two-record sector.
- Both `K₊` and `K₋` satisfy both clauses. The Record axiom therefore gives exclusion and no sign.
- Block 78 T1 already shows exclusion is not a free pair of either sign: `N` fewer states than the free antisymmetric
  pair, and a different `tr H²/dim`.

### S3 — lattice covariance and the discrete exchange rotation. PROVED; CHECKED
- Every lattice symmetry acts on one record as a unitary `W`, and on two records as `W⊗W`, which commutes with `P`.
  So both sectors are covariant.
- The spin–statistics comparator's ingredient is present. The symmetry `g` = (shift by `e₁`) ∘ (rotation by `π` about `e₂`
  at site 0) exchanges sites 0 and `e₁`. CHECKED:
  - it commutes with the walk on the 3-torus;
  - on one record `W_g² = −1`, the coin's spinor sign, since `D = −iσ₂` and `D² = −1`.
- On two records `(W_g⊗W_g)² = (−1)(−1) = +1`, on `K₊` and on `K₋` alike (PROVED from `W_g² = −1`).
- The discrete exchange therefore carries no sign.
  - The comparator argument that would convert the spinor sign into an exchange sign is Finkelstein–Rubinstein's. It
    needs a continuous configuration space and a homotopy between exchange and a `2π` rotation.
  - The axioms supply sites and discrete rotations only. This is the landed rotation-exchange no-go, here restated in
    the amplitude picture.

### S4 — "no possibility is privileged". PROVED
- Relabelling a record's possibilities is an automorphism of `M₂(ℂ)`: `Ad U`, or the antilinear `α` below.
- On two records it acts as `Ad(U⊗U)`, which commutes with `P`. Both sectors are invariant, so the sentence selects neither.

### S5 — the model pair (answer to (c)). PROVED; CHECKED

| axiom sentence | `K₊` (`ε = +1`) | `K₋` (`ε = −1`) |
|---|---|---|
| Lattice: `Z³`, translations, proper rotations; no site privileged | covariant (S3) | covariant (S3) |
| Qubit: one-site domain `M₂(ℂ)`, `Cl(3,0)` presentation | content `ℂ²` per record, unchanged | same |
| Qubit: no possibility privileged | invariant under `Ad(U⊗U)` and `α⊗α` (S4) | same |
| Admissibility: one fixed nearest-neighbour rule; site distributions | untouched: a composition rule adds no one-site data | same |
| Record: records form; one per site; permanent | `K₊ ⊆ HC`; the two-record sector is conserved | same |
| Record: readout by content alone | readouts commute with `P`, so act within `K₊` | within `K₋` |
| Qualification: a choice not fixed stays a named conditional | the choice between them is exactly such a choice | — |

- Both rules satisfy every sentence.
- They are different: the fourth moments differ (S7, CHECKED).
- So `ε` is not a consequence of the axioms. This is a counterexample to derivability, in the amplitude picture.

### S6 — the Clifford grading, the route the task names. PROVED; CHECKED

Setting: the presentation `Cl(3,0) ≅ M₂(ℂ)` (with `e_a = σ_a`) carries the grading `α(x) = σ₂ x̄ σ₂`.
- `α` fixes `1` and `iσ_a`, so the even part is span{`1`, `iσ_a`} ≅ ℍ.
- `α` negates `σ_a` and `i·1`, so the odd part is span{`σ_a`, `i`}.
- `α` is an antilinear automorphism. CHECKED, including multiplicativity on generators.

The route: "a Clifford algebra carries a grading; records are odd; odd objects at distinct sites anticommute; hence
`ε = −1`". It fails at "records are odd", in three ways.

1. **A record state has no parity.**
   - A pure record state `(1 + u·σ)/2` has even part `1/2` and odd part `u·σ/2`, never zero. CHECKED.
   - On the content space `ℂ²` there is no involution `Γ` (`Γ² = 1`, linear or antilinear) with `Γσ_aΓ⁻¹ = −σ_a` for
     all `a`. CHECKED with sympy:
     - linear: the only solution of `Γσ_a = −σ_aΓ` is `Γ = 0`;
     - antilinear `Γ = MK`: `M σ̄_a = −σ_a M` forces `M = c·σ₂`, and then `Γ² = M M̄ = −|c|² ≠ 1`.
   - So `ℂ²` is not a graded `Cl(3,0)`-module, and the grading assigns a single record no parity.
2. **Graded records need a larger site algebra.** (PROVED)
   - In a graded module `M₀ ⊕ M₁`, the pseudoscalar `ω = e₁e₂e₃` (odd, central, `ω² = −1`) maps `M₀` isomorphically onto `M₁`.
   - `M₀` is a module of the even part ℍ, so `dim_ℝ M ≥ 8`.
   - The minimum `ℂ⁴` is realised by `Γ = 1⊗σ₃` and `e_a = σ_a⊗σ₁` (CHECKED).
   - The full algebra on `ℂ⁴` is `M₄(ℂ)`: the larger site algebra that is parked and not touched here.
3. **The graded composite is not the complex one.**
   - The composite suggested by the Clifford presentation, `Cl(V_x ⊕ V_y) = Cl(3,0) ⊗̂ Cl(3,0) = Cl(6,0)`, has real
     dimension 64 (CHECKED: rank 64 from three-qubit Majoranas). Each site's subalgebra there has rank 8 with central
     `ω² = −1`, i.e. is `M₂(ℂ)`. But `ω_xω_y = −ω_yω_x`: the two sites' complex units anticommute.
   - The complex composite `M₂(ℂ) ⊗_ℂ M₂(ℂ) = M₄(ℂ)` has real dimension 32 and one shared `i`.
   - The Qubit axiom says the real presentation "adds no further primitive structure". But the two presentations lead
     to different composites, and no axiom sentence names a composite.
   - Choosing the graded one is a clause, not a consequence. That clause is PR #7829's "graded product", closed and not
     on `main`.

### S7 — where the sign shows (answer to (d)). PROVED; CHECKED
- **Orders 1 and 2 on every nearest-neighbour graph (PROVED).**
  - `tr_{K±}X = ½[tr_{HC}X ± tr_{HC}(PX)]` for `X` commuting with `P`, so the sectors differ exactly by `tr(P H₂^k)`.
  - That is a sum over `k`-hop hard-core paths from `(x,y)` to `(y,x)`. Each record must reach the other's site.
  - With 2 hops each record hops once, directly onto the other's still-occupied site. No path exists.
- **Order 3 on bipartite graphs (PROVED).** Each hop moves one record to the other sublattice. The two records need
  either both an even or both an odd number of hops, so the total is even.
- **Order 4 on `Z²` and `Z³` (CHECKED).** Two ways, which agree:
  - exact traces on the tori of side 5, where no winding path has fewer than 5 hops:
    - `tr(P H₂⁴) = −200` over 25 sites (`Z²`);
    - `−3000` over 125 sites (`Z³`);
  - an independent local enumeration on the infinite lattice, which also shows orders 2 and 3 are zero there.

  The coefficient is `−8` per plaquette: `Z³` has 3 plaquette orientations per site, so `−24` per site.

  Per pair, coin-summed, `Σ⟨Ps|H₂⁴|s⟩ = −2` (neighbours), `−1` (face diagonals), `0` (distance 2 on a line). For the
  localised pair state `ψ± = (|s⟩ ± |Ps⟩)/√2`, `⟨ψ±|H₂⁴|ψ±⟩ = ⟨s|H₂⁴|s⟩ ± Re⟨Ps|H₂⁴|s⟩`. Averaged over coins, the two
  signs differ by exactly `−1` for neighbours and `−1/2` for face diagonals, in units where one hop has amplitude `1/2`.

  **The observable is this fourth moment of the two-record energy of a localised pair**: equivalently the `t⁴`
  coefficient of its return amplitude. The four-hop plaquette exchange is the first process that sees `ε`.
- **Rings (block 78's reduced walk).**
  - Even `N`, CHECKED for `N = 4, 6, 8`:
    - `tr(P H₂^k) = 0` for `k < N`;
    - at `k = N`, `tr(P(2H₂)^N) = 128`, `−1248` and `7680` respectively;
    - an exchange on a ring must wind: the two records' hops total at least `N`.
  - Odd `N`: the sectors are unitarily equivalent (PROVED; CHECKED exactly on `N = 5, 7`).
    - `J` = the sign of the order of the two positions. It anticommutes with `P`. Under exclusion only a hop across
      the bond `(N−1, 0)` changes the order, so `J H₂ J` is `H₂` with that bond flipped, i.e. the antiperiodic walk.
    - `G = (−1)^x` on each record maps the antiperiodic walk to `−H` when `N` is odd.
    - `σ₁` on each coin maps `−H` back to `H`.
    - So `U = (σ₁⊗σ₁)(G⊗G)J` satisfies `U H₂ U* = H₂` and `U P U* = −P`, and maps `K₋` onto `K₊`.
    - Hence on odd rings the sign is invisible to every spectral quantity at every order. This is block 78's executed
      observation, now shown for all orders.
    - On even `N`, `G` does not remove the flip, and the sectors differ at order `N`.

## 3. Where the route fails

- The derivation of (b) fails at its **first** step and at every later one:
  - the Record axiom gives exclusion, not a sign (S2);
  - covariance and "no possibility is privileged" act as `W⊗W`, which commutes with `P` (S3, S4);
  - the discrete exchange rotation squares to `+1` on both sectors (S3);
  - the Clifford grading does not reach a record's content (S6.1).
- S5 shows this is not a weakness of the route. The two rules satisfy every axiom sentence, so no route from these
  sentences to `ε` exists.
- The sign is an input, of the kind the Qualification calls "a named conditional". Its two natural suppliers are:
  - a composition clause (the graded product);
  - the parked larger site algebra `M₄(ℂ)`, in which records can carry parity (S6.2).

## 4. What would finish it
- **A physical fourth-order measurement.** For a derived rather than supplied sign, some framework law would have to
  fix the plaquette exchange amplitude's sign (S7). No current clause does. A clause fixing `ε` would be checked there
  first: its prediction is `∓1` in the coin-averaged fourth moment of a neighbouring pair.
- **A decision on the parked items.**
  - Adopting the graded product at the site level (PR #7829's clause) supplies `ε = −1`.
  - Adopting `M₄(ℂ)` makes graded records possible.
  - Either is an owner decision, not a derivation.
- **Many records.** Under exclusion the sea of the axioms' records is interacting (block 78). The same order analysis
  for three or more records would show at which order the sign first matters for the ledger's source (block 55's
  energy density).
