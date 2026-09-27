---
claim_id: record_formation_a_sharp_one_site_lock_costs_the_energy_of_its_bonds_in_the_walkers_sea_about_two_point_four_lattice_energy_units_per_record_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied setting, none adopted: the sites carry a quantum state (the dynamics-clause kinematics) and a record at site x is formed by the compression update with rank-one Kraus operators on x (antipodal menu, or the sphere menu realised by the octahedral 3-design). (T1) For any state and any Hamiltonian of a finite system, the mean energy change of forming the record is Tr rho(Phi*(h_x) - h_x), where h_x is the sum of the terms touching x. (T2) For a unique ground state with gap Delta the cost is at least Delta sum_a w_a (p_a - p_a^2); the antipodal floor is (Delta/2)(1 - (r.n)^2) and the sphere floor Delta(3 - |r|^2)/6 >= Delta/3; the cost vanishes only if every locked branch is a ground state. (T3) In any SU(2)-singlet state of the Heisenberg dynamics clause, every menu costs -(2/3) J sum_{y~x} <sigma_x.sigma_y>: 2J for the singlet bond, 3.2134J and 3.7398J on the open 2x2x2 and 2x2x3 blocks. (T4) In the half-filled sea of the walker H = t sum_j sin k_j sigma_j (twisted boundaries; a comparator whose site is a four-dimensional Fock space, not the axiom's M_2(C)), every menu of rank-one locks with definite fermion parity removes exactly the hopping terms touching the site; its mean cost is the energy held in the site's six bonds, 2<|s(k)|>_BZ t = 2.387602 t (L = 256); when sum_k s(k) = 0 every outcome costs the same; about 96 % of it stays as the permanent record's own energy (the rest cannot relax below E0 + 2.30 t) and at most about 4 % can radiate; with the staggered mass the mean cost is 2<s^2/sqrt(s^2+m^2)> t, tending to 3t^2/m, with outcomes split. The massless sea's site is maximally mixed. (T5) Above a product (Fock-vacuum) ground state of a local, number-conserving quadratic fermion Hamiltonian the lowest one-particle band rises at most quadratically from its minimum, so such a theory's conical excitations cannot sit above its empty vacuum (a narrow lemma; BdG, bosonic, interacting and nonlocal carriers are outside it). (T6) A sharp record of a region's total content costs (bonds crossing its surface) x (bond energy), 2.39 R^2 t for an R-cube; a soft Gaussian record of the content weighted by the unit-amplitude profile exp(-r^2/2R^2), R >> 1, with resolution sigma >> |w_x - w_y|, costs about 0.415 R/sigma^2 t. (T7) Arithmetic with external reference constants (not premises): with t = hbar c/a, a single-site record in the sea costs 2.39e12 eV at a 1 TeV lattice scale and 4.7e9 J at the Planck scale. A conditional cost, not an impossibility: the identification of a record with a sharp collapse of one site's state is the supplied setting's, not derived from the axioms, and the walker's site is a four-dimensional Fock space, not the axiom's M_2(C). Finite exact checks and converged lattice sums; no interacting-vacuum theorem beyond the stated models."
upstream_dependencies:
  - minimal_axioms
  - dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
runner: scripts/record_formation_one_site_lock_costs_the_energy_of_its_bonds_2026_09_27.py
---

# A sharp one-site record costs the energy held in the site's bonds: in the walker's sea, about 2.4 lattice energy units per record

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact finite results and converged lattice sums in a supplied
setting; unaudited; independent checks recorded below.

## In one paragraph

Suppose a record is what the landed quantum setting says it is: a sharp lock
that collapses one lattice site onto one possibility. Then reading that site
cuts it off from its neighbours, and the links to the neighbours are where
the lattice keeps its energy. In the walker's sea, the vacuum that carries
the campaign's relativistic walker, those links are full. Each record then
costs about 2.4 units of the lattice's own energy. If the lock stays in
place, most of that stays in the record. On a lattice of qubits (the
axiom's own site) with the dynamics clause's Heisenberg bond, the cost is of
the same order: 2 to 3.7 bond energies (T3).
- If the lattice spacing is the Planck length (the memo's open gate), that
  is about five billion joules per record, and each permanent record weighs
  about 50 micrograms. Ordinary measurements show nothing of the kind. This
  is an empirical comparison, not a theorem.
- At a lattice energy of 1 TeV (an illustrative coarse tier), it is a bill
  of about half a microjoule per record, which whatever forms the record
  must pay. That is not excluded by this note alone.

So a record at a Planck-scale lattice cannot be a sharp collapse of one site.
It has to be weak or collective, a soft lock on something large, or not a
collapse at all.

The general rule (T4(h)): a record costs how uncertain its answer was, times
the energy between the alternatives. Whether a particle is in a given wave
packet is cheap to record. Which single site something occupies is the most
expensive question the lattice can be asked.

## Why this question

The Record axiom says "Records form. When present, a record locks exactly one
admissible local possibility. A site never carries more than one record".
The landed Bell note
([DYNAMICS_CLAUSE_BELL_VALUES_...](DYNAMICS_CLAUSE_BELL_VALUES_OF_RECORD_LAWS_RECORDS_ONLY_FORMATION_STAYS_AT_TWO_THE_DYNAMICS_CLAUSE_REACHES_TWO_ROOT_TWO_BOUNDED_THEOREM_NOTE_2026-09-24.md))
shows that formation conditioned on records alone is a local causal model:
its CHSH value never exceeds 2. The measured value is 2 sqrt 2. The only
setting in the repository that reaches it keeps a quantum state of the
unrecorded sites and forms records by the compression update (the landed
dynamics-clause construction). In that setting a record is a collapse of the
lattice's quantum state onto one possibility of one site. This note asks what
such a collapse costs in energy.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): the Lattice, Qubit,
  Admissibility and Record axioms, read in full.
- **Supplied setting** (the dynamics-clause kinematics and update, not
  adopted): a quantum state `rho` of the sites; a record at site `x` applies
  Kraus operators `K_a = sqrt(w_a) P_a` with `P_a` rank-one projectors on
  `x`'s possibility domain and `sum_a w_a P_a = 1_x`.
  - The antipodal menu `{n, -n}` has `w = 1`.
  - The sphere menu is realised exactly by the octahedral 3-design, `w = 1/3`
    on `+-e_1, +-e_2, +-e_3`.
  - The mean over outcomes uses the trace-rule odds. T4 also shows that in
    the sea every outcome costs the same, so the result does not rest on the
    odds.
- **Hamiltonians** (supplied comparators, not adopted):
  - the Heisenberg bond `J sigma_x . sigma_y` of the dynamics clause;
  - the walker `H = t sum_x sum_j [c_x^dag (sigma_j/2i) c_{x+e_j} + h.c.]`,
    whose Bloch form is `t sum_j sin k_j sigma_j`, optionally with the
    staggered mass `m (-1)^{x+y+z}` of block 139.
- **The energy unit.** The walker's group velocity at small `k` is `t a/hbar`.
  If the walker's cone is light's cone, then `t = hbar c/a`, where `a` is the
  lattice spacing.
- **Cost.** `Delta E` is the mean energy after the record, minus the energy
  before, with the same Hamiltonian.

## T1 — the cost identity

*Statement.* For a finite system, any state `rho`, any Hamiltonian
`H = sum` of local terms and any record at `x` as above,

`Delta E = Tr rho (Phi*(h_x) - h_x)`,  where  `Phi*(A) = sum_a w_a P_a A P_a`

and `h_x` is the sum of the terms of `H` whose support contains `x`.

*Proof.*
- The mean post-record state is `sum_a w_a P_a rho P_a`.
- So `Delta E = Tr rho (sum_a w_a P_a H P_a - H)`.
- A term `h` not touching `x` commutes with every `P_a`. Hence
  `sum_a w_a P_a h P_a = h sum_a w_a P_a = h`, and it drops out. ∎

The runner checks this on 60 random nearest-neighbour chains with random
states, on both menus (maximum deviation `1.2e-15`).

## T2 — floors from the gap

*Statement.* Let `|0>` be the unique ground state, with energy `E_0` and
gap `Delta` to the rest of the spectrum. Let `p_a = <0|P_a|0>`. Then:
- `Delta E >= Delta sum_a w_a (p_a - p_a^2)`;
- antipodal menu: `Delta E >= (Delta/2)(1 - (r.n)^2)`, where `r` is the
  site's Bloch vector;
- sphere menu: `Delta E >= Delta (3 - |r|^2)/6 >= Delta/3`.

The cost is zero only if every `P_a|0>` with `w_a p_a > 0` is itself a ground
state. With a degenerate ground space `Pi_0`, replace `p_a - p_a^2` by
`<0|P_a|0> - <0|P_a Pi_0 P_a|0>`. A record can then move the state within the
ground space at no cost.

*Proof.*
- `Delta E = sum_a w_a <0|P_a (H - E_0) P_a|0>`.
- `H - E_0 >= Delta (1 - |0><0|)`.
- `||(1 - |0><0|) P_a|0>||^2 = p_a - p_a^2`.
- For the antipodal menu, `p_+- = (1 +- r.n)/2`.
- For the octahedral menu, summing `(1/3)(p - p^2)` over the six directions
  gives `(3 - |r|^2)/6`. ∎

So a sharp record on a site that is entangled with its neighbours (`|r| < 1`)
always costs a fixed fraction of the gap. The sphere menu costs at least a
third of the gap even at a pure site. The runner checks both floors on 40
random gapped chains.

## T3 — the dynamics clause's Heisenberg ground states

*Statement.* In any state whose two-site correlations are rotation invariant,
`<sigma_x^a sigma_y^b> = C_xy delta_ab` (any SU(2) singlet). There, every
antipodal menu and the sphere menu cost the same:

`Delta E = -(2/3) J sum_{y ~ x} <sigma_x . sigma_y>`.

*Proof.*
- Antipodal along `n`: `Phi*(sigma_x . sigma_y) = (n.sigma_x)(n.sigma_y)`,
  whose mean is `C_xy`, against `3 C_xy` before.
- Sphere: `Phi*(sigma_x^a) = sigma_x^a / 3`.
- In both cases each bond loses two thirds of `J <sigma_x.sigma_y>`. ∎

*Values.*
- The singlet: `E_0 = -3J`. Either menu costs exactly `2J` (sympy). Every
  outcome costs `2J`: the post-record state is the product `|n>|-n>` with
  energy `-J`.
- The aligned record on the aligned ferromagnetic product state costs exactly
  `0`. For a unique ground state, T2 says this is the only way to cost
  nothing: every branch must itself be the ground state. Degenerate ground
  spaces, isolated sites and already block-diagonal branches are the other
  zero-cost cases.
- Open blocks (exact diagonalisation). Each ground state is a singlet, and
  each cost exceeds half the gap:

| block | site (neighbours) | cost | gap / 2 |
|---|---|---|---|
| `2x2x2` | corner (3) | `3.213393 J` | `1.640179 J` |
| `2x2x3` | corner (3) | `3.150188 J` | `1.316826 J` |
| `2x2x3` | middle layer (4) | `3.739807 J` | `1.316826 J` |

## T4 — the walker's sea

*Setting.* This is the walker comparator. Its site is a four-dimensional
Fock space: two fermion modes, the coin states. The axiom's one-site domain
is `M_2(C)`, a qubit. T3 is the qubit case; T4 is what the campaign's
walker, with its sea, does.

*Statement.* Take the half-filled ground state of the walker with twisted
boundaries (no zero modes).
- **(a)** Every menu of rank-one locks with definite fermion parity removes
  exactly the hopping terms touching the site. This includes the occupation
  patterns in any coin basis and parity-definite superpositions such as
  `(|0> +- |ud>)/sqrt 2`, which are the only locks fermion superselection
  allows. `c_x^dag c_y` (`y != x`) flips the site's parity, so it has zero
  diagonal blocks between parity-definite projectors. Every other term
  commutes with them.
- **(b)** The mean cost is minus the energy held in the site's six bonds.
  By translation invariance that is `6/(3N)` of the total energy, so

  `Delta E = 2 <|s(k)|>_BZ t`,  `|s(k)| = (sin^2 k_1 + sin^2 k_2 + sin^2 k_3)^{1/2}`.

  It equals `2.389890 t` on `8^3` and `2.387602 t` on `256^3`: the energy of
  about `2.4` hops. A parity-violating menu (forbidden) would still cost
  `3/4` of this.
- **(c)** When `sum_k s(k) = 0` (twisted boundaries on even sides, and the
  infinite lattice), every outcome costs the same, so no choice of odds
  lowers the cost. This is checked on the `2^3` and 8-site Fock spaces, in
  two coin bases, with odds `1/4` each.
- **(d)** About 96 % of the cost stays in the record. After the lock, the
  rest of the lattice cannot relax below `E_0 + 2.3035 t` (`12^3`;
  `2.2996 t` on `16^3`). A permanent record is therefore a defect whose own
  energy is about `2.30 t`. At most about `0.09 t` can be radiated.
- **(e)** With the staggered mass `m`, measured in units of `t`, the mean
  cost is `2 <s^2 / sqrt(s^2 + m^2)> t`. That is
  `2 t^2 <s^2 / sqrt(t^2 s^2 + m^2)>` in physical units, which tends to
  `3t^2/m` when `m >> t`
  (`0.029997 t` at `m = 100t`). The outcomes then split: the near-certain
  one costs about `3t^2/(2m)`, and the rare ones cost of order `2m`.
- **(f)** With the same condition (inversion-paired momenta: twisted even
  sides, or the infinite lattice), the massless sea's site is maximally
  mixed. Its one-body block is `(1/2) 1`, so it carries two bits of
  entanglement with the rest. On odd sides with generic twists it is not:
  the sol referee found a non-scalar block and unequal outcome costs
  `2.411, 2.425, 2.308, 2.411 t` for `L = 3`, twist `(0.3, 0.7, 1.1)`.

- **(g) The moving-records reading.** There a record is a particle at one
  site, not a lock on the sea. Adding a particle at one site of the sea puts
  it only into empty (upper-band) states: the weight is `1/2` for either
  coin. Its energy above the vacuum is `<|s|> = 1.19 t` (`8^3` and `12^3`,
  exact to `1e-9`). That is half the sharp-lock cost and still the lattice
  scale: localising anything to one site spreads it over the whole zone.

- **(h) The general rule for one mode.** Record the occupation `n_f` of
  any single mode `f` of the sea. Let `p` be `f`'s weight in the filled band,
  and `E_-` and `E_+` its mean energies in the filled and empty bands. Then
  the cost is exactly

  `Delta E = 2 p (1 - p) (E_+ + |E_-|)`.

  *Proof.* The dephasing removes `h`'s terms between `f` and its complement.
  In the sea `<c_a^dag c_b>` is the filled-band projector `P_-`, so
  `Delta E = -2 [f^dag h P_- f - (f^dag h f)(f^dag P_- f)]`. Split `f` into
  its two band parts. ∎

  In words, a record costs how uncertain its answer was, times the energy
  between the alternatives.
  - A packet inside the filled band, or inside the empty band, costs
    nothing: the vacuum already answers it with certainty. That is a
    particle's wave packet.
  - One site's coin mode is half in each band, with the whole bandwidth
    between them, and costs `<|s|> = 1.19 t`.

  The runner checks the formula against the direct evaluation on `6^3`,
  and against Fock-space brute force for a random mode on `2^3`.

*Proof of (a)–(b).* Parity, as in (a). Each of the `3N` bonds carries the same
mean energy, the site owns six of them, and `E_0 = -N <|s|> t`. ∎

*Evidence.* Fock-space brute force in the Jordan–Wigner representation equals
the correlation-matrix formula to `1e-9`:
- `2^3` (3D), `2^2` (2D), rings of 6 and 8;
- massless, and with `m = 0.7` and `m = 0.4`.

## T5 — for number-conserving free fermions, conical excitations cannot sit above the empty vacuum

*Statement.* Let `h(k)` be a local (trigonometric-polynomial) Bloch
Hamiltonian, shifted so that its Fock vacuum is the ground state, i.e.
`h(k) >= 0`. At any zero of the lowest band, that band rises at most
quadratically.

*Proof.* Let `h(k_0) v_0 = 0` with `|v_0| = 1`. Then:
- `lambda_min(k) <= v_0^dag h(k) v_0 =: f(k)`;
- `f` is smooth, `f >= 0`, and `f(k_0) = 0`;
- so `grad f(k_0) = 0` and `f(k) = O(|k - k_0|^2)`. ∎

So, within local number-conserving quadratic fermion theories, conical
excitations (the walker's `E = t|k|`) cannot sit above the empty product
vacuum. The walker's own stable vacuum is its filled sea, and the sea's
sites are entangled (T4(f)).

This is a narrow lemma. BdG, bosonic, interacting, composite and nonlocal
carriers are outside it. It is not a theorem that every relativistic vacuum
has entangled lattice sites. That is the generic expectation, not proved
here.

The runner checks the quadratic rise on 30 random range-one `2x2` Bloch
families: the ratio `e(2d)/e(d)` is within `9e-4` of 4, against 2 for a cone.

## T6 — larger records

*Statement.*
- **(a) Sharp.** A record of the total content of a region, a projection
  onto its eigenvalues, removes every hop crossing the region's surface. For
  an `R x R x R` cube in the sea it costs `6R^2 x (2.39/6) t = 2.39 R^2 t`.
  Checked exactly for `R = 1..4` on `12^3`.
- **(b) Soft.** Take a Gaussian record of a weighted content `sum w_x n_x`
  with resolution `sigma` (Kraus operators
  `exp(-(A - alpha)^2/(4 sigma^2))`). It multiplies each hop `x -> y` by
  `exp(-(w_x - w_y)^2/(8 sigma^2))`, which is exact. For the unit-amplitude
  profile `w = exp(-r^2/2R^2)`, with `R >> 1` and `|w_x - w_y| << sigma`, the
  cost is about
  `(bond energy) x (3/2) pi^{3/2} R / (8 sigma^2) = 0.415 R/sigma^2 t`,
  since `int |grad w|^2 = (3/2) pi^{3/2} R`. The runner's exact values are
  within 15 % of this at `sigma >= 1`.

So making a record coarse does not make it cheap. A sharp coarse record costs
more, by the area of its surface. A soft record of this profile is cheap only
when `sigma^2 >> 0.4 R`, i.e. when it cannot resolve the content to one unit.

## T7 — what the numbers mean (external reference inputs, not premises)

The comparison uses outside numbers only as reference: `hbar c`, the critical
density `7.7e-10 J/m^3` and the age of the universe `4.35e17 s`. The lattice
energy `t = hbar c/a` is unknown. The runner takes three tiers:

| lattice scale `hbar c/a` (illustrative tiers) | spacing `a` | one single-site record in the sea (for a lock that stays in place, about 96 % of it is the record's own energy) | largest vacuum formation rate the critical density allows |
|---|---|---|---|
| 1 TeV (an illustrative coarse tier) | `2.0e-19 m` | `2.4e12 eV = 3.8e-7 J` | `2.3e-104` per site per tick |
| `1e10 GeV` (the order of published quadratic Lorentz-violation bounds) | `2.0e-26 m` | `2.4e19 eV = 3.8 J` | `2.3e-139` per site per tick |
| Planck energy (the memo's open gate) | `1.6e-35 m` | `2.9e28 eV = 4.7e9 J` | `8.6e-185` per site per tick |

"Only records are readable": every observed outcome is fixed by records that
formed when the outcome became a fact. Under the supplied setting, each such
record, if it is a sharp lock on one site of the sea, puts at least the row's
energy into the lattice. If the lock stays on the site, as a permanent
record at the site would, about 96 % of that stays as the record's own
energy.

`Delta E > 0` means the lattice gains energy, so whatever forms the record
must supply it. The injected energy (T1) is the same when the record is a
reliable copy held in an ancilla: a perfect copy of the site's possibility
dephases the lattice in that basis. But an ancilla-held copy does not keep
the site locked afterwards. For it, the 96 % residue and the 4 % radiation
ceiling of T4(d) do not apply: the injected energy is free to spread.

The rows mean:
- **Planck spacing.** About `4.7e9 J` per record, and for a lock that stays
  in place a residue weighing about 50 micrograms. Ordinary measurements
  show neither. This is an empirical comparison (reference-level), not a
  theorem.
- **`1e10 GeV`.** About `4 J` per record. A detector counting a million
  events a second would draw megawatts. Excluded unless formation is
  collective.
- **1 TeV.** About `4e-7 J` per record, a bill that a powered apparatus could
  in principle pay. Not excluded by this note alone.

The vacuum-rate column applies only to spontaneous formation in empty space.
The memo's "records form" does not say where records form.

## What this does and does not say about the axioms

It prices one reading of the Record axiom: a record is a sharp, rank-one lock
of one lattice site's possibility, acting on the lattice's quantum state
through the landed compression update.
- **On the axiom's own sites** (qubits, `M_2(C)`) with the dynamics clause's
  Heisenberg bond, T3 gives the cost: 2 to 3.7 bond energies per record.
- **On the walker comparator's sites** (a four-dimensional Fock space), T4
  gives it: 2.39 hop energies.
- In both, it is the lattice's bond scale. The tier numbers use T4. With T3
  they are the same order, if the bond energy `J` is also of order `hbar c/a`,
  as it is when spin waves carry the light cone. At a Planck-scale lattice that reading
fails energy bookkeeping by a macroscopic margin, judged against ordinary
measurements. At the coarsest allowed
lattice it becomes an energy bill that every recording process must pay. The
axioms do not force this reading. The memo leaves the update law, the
measurement basis and physical-observable identification downstream. The
result is a conditional cost, not an impossibility theorem.

Readings that escape it:
1. **Weak or collective records.** A record locks a collective variable
   softly: a pointer made of many sites, resolved no finer than its
   macroscopic states differ. T6(b) prices this reading, which has the shape
   of the spontaneous-collapse models (Ghirardi–Rimini–Weber, Pearle).
   Their relativistic versions are known to excite the vacuum for the reason
   T6 shows; that literature is reference only. This reading changes the
   Record axiom's "one site" to "a region" and "locks exactly" to "locks
   softly".
2. **Records without collapse.** A record is a stable, redundantly copied
   fact produced by the unitary dynamics (decoherence), paid for by the
   dynamics' own energy flow. "Records form" then becomes a theorem about
   the dynamics, not an independent primitive. The memo's open gates on
   formation site, rate and unit would be computed rather than chosen.
3. **Records of quantities that commute with the local energy**
   (quantum-nondemolition records), or records within a degenerate ground
   space. They cost nothing (T2), but a single site's possibility is not
   such a quantity for the sea or for the Heisenberg bond.
4. **Apparatus-funded sharp records at a lattice far below the Planck
   scale** (the 1 TeV row). Every record then carries a lattice-scale
   residue. This is not excluded here.
5. **Other carriers.** BdG, bosonic, interacting or composite vacua, and
   other dynamics clauses, are outside T4–T5. T1–T3 still apply to them.
   Their site bonds would have to be computed.
6. **Records-only laws that are not local-causal.** The landed Bell note
   excludes only records-only formation that is local and causal with
   independently formed settings. Global-constraint laws, retrocausal laws
   and laws with setting dependence are not excluded by it. The static law
   conditioned on its setting records exceeds `2 sqrt 2`. Nothing here
   supports them either.

What it does not say:
- anything about the formation laws studied as mathematics (blocks 01–52),
  the static comparator, the gravity lane's clauses, or the moving-records
  kinematics;
- which of the escapes nature uses.

## Independent checks

- **Claude Fable 5.1 subagent.** Same vendor family, so this is not a
  referee. It worked from its own code without reading the runner. Verdict:
  confirmed with corrections.
  - It reproduced T4 by Wick conditioning of the Slater determinant and by a
    bit-level Fock brute force.
  - It reproduced the continuum constant by three quadratures: nquad
    `2.3876022429`, Gauss–Legendre `2.387602243`, Monte Carlo
    `2.387603 ± 0.000122`.
  - It reproduced T1, T3, T5 and T6(a).
  - It proved the equal-outcome claim: the conditional change of the rest's
    energy vanishes whenever `sum_k s(k) = 0`.
  - Its corrections are all applied in this revision: the parity scope and
    the `3/4` for parity-violating locks; the `sum_k s = 0` condition; the
    split outcomes with a staggered mass; the Fock-space-versus-qubit
    identification; and the stored-versus-radiated split (its `2.2996 t` of
    `2.3877 t` on `16^3`, confirmed here as check L).
  - T6(b) was not checked.
- **Codex `gpt-5.6-sol` referee**, at xhigh effort. Another vendor family;
  it read only the axioms memo, this note and the Bell note, and it did not
  run the runner.
  - **Its verdict on the first version:** the broad conclusion fails as a
    statement about the axioms or about relativistic vacua generally; the
    narrow calculations largely stand.
  - **Reproduced by its own method:** T1; the `-2/3` factor and the block
    values `3.213392916`, `3.150188162` and `3.739806569 J`;
    `2 <|s|> = 2.387602509` by independent quadrature; T5's lemma; T6(a);
    the T7 arithmetic.
  - **Corrections applied in this revision:**
    - T1 is for finite systems.
    - T2 needs a unique ground state (the degenerate form is now given).
    - "The only zero-cost case" is narrowed.
    - T4's maximal mixing and equal outcomes need inversion-paired momenta
      (its `L = 3` counterexample is quoted).
    - T5 is a narrow lemma, not a theorem about all relativistic vacua.
    - T6(b)'s profile hypotheses are stated.
    - Formation may be funded by an apparatus, so the 1 TeV row is a bill,
      not an exclusion.
    - The vacuum-rate bound applies only to spontaneous formation.
    - The records-only escape (non-local-causal laws) is restored.
    - The main conclusion is restated as a conditional cost, decisive at the
      Planck gate.
  - **Two points answered rather than applied:**
    - Its fatal point 7, that the axioms do not entail a Lüders projection,
      is accepted and is now the note's own framing. Its companion point,
      that the walker's site is not `M_2`, was already applied from the
      Fable check.
    - Its escape "an ancilla or quantum-nondemolition record that stores a
      result without dephasing the site" holds only for recorded quantities
      that commute with the local energy (escape 3). A reliable copy of a
      site's possibility dephases the lattice in that basis and costs the
      same `Delta E`, paid by whatever makes the copy (T7).

## Reproduction

```bash
python3 scripts/record_formation_one_site_lock_costs_the_energy_of_its_bonds_2026_09_27.py
```

Expected: `TOTAL: PASS=19 FAIL=0` (about 70 s).
