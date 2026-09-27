---
claim_id: record_formation_one_site_lock_costs_the_energy_of_its_bonds_a_relativistic_vacuum_makes_every_single_site_record_cost_the_lattice_scale_bounded_theorem_note_2026-09-27
claim_type: bounded_theorem
claim_scope: "Supplied setting, none adopted: the sites carry a quantum state (the dynamics-clause kinematics) and a record at site x is formed by the compression update with rank-one Kraus operators on x (antipodal menu, or the sphere menu realised by the octahedral 3-design). (T1) For any state and any Hamiltonian, the mean energy change of forming the record is Tr rho(Phi*(h_x) - h_x), where h_x is the sum of the terms touching x. (T2) For a ground state with gap Delta the cost is at least Delta sum_a w_a (p_a - p_a^2); the antipodal floor is (Delta/2)(1 - (r.n)^2) and the sphere floor Delta(3 - |r|^2)/6 >= Delta/3; the cost vanishes only if every locked branch is a ground state. (T3) In any SU(2)-singlet state of the Heisenberg dynamics clause, every menu costs -(2/3) J sum_{y~x} <sigma_x.sigma_y>: 2J for the singlet bond, 3.2134J and 3.7398J on the open 2x2x2 and 2x2x3 blocks. (T4) In the half-filled sea of the walker H = t sum_j sin k_j sigma_j (twisted boundaries), a record that fixes the site's occupation removes exactly the hopping terms touching the site; its cost is the energy held in the site's six bonds, 2<|s(k)|>_BZ t = 2.387602 t (L = 256), every outcome costing the same (checked on the 2^3 and 8-site Fock spaces); with the staggered mass the cost is 2<s^2/sqrt(s^2+m^2)> t, tending to 3t^2/m. The massless sea's site is maximally mixed. (T5) Above a product (Fock-vacuum) ground state of a local, number-conserving quadratic Hamiltonian the lowest one-particle band rises at most quadratically from its minimum, so conical (relativistic) low-energy excitations require a filled-sea vacuum. (T6) A sharp record of a region's total content costs (bonds crossing its surface) x (bond energy), 2.39 R^2 t for an R-cube; a soft Gaussian record of a smooth region of width R with resolution sigma costs about 0.415 R/sigma^2 t. (T7) Arithmetic with external reference constants (not premises): with t = hbar c/a, a single-site record in the sea costs 2.39e12 eV at a 1 TeV lattice scale and 4.7e9 J at the Planck scale. Finite exact checks and converged lattice sums; no interacting-vacuum theorem beyond the stated models; the physical identification of records with collapses is the supplied setting's, not derived."
upstream_dependencies:
  - minimal_axioms
  - dynamics_clause_bell_values_of_record_laws_records_only_formation_stays_at_two_the_dynamics_clause_reaches_two_root_two_bounded_theorem_note_2026-09-24
runner: scripts/record_formation_one_site_lock_costs_the_energy_of_its_bonds_2026_09_27.py
---

# Forming one record costs the energy held in the site's bonds; in a relativistic vacuum every single-site record costs the lattice scale

**Date:** 2026-09-27
**Type:** bounded_theorem
**Status:** exact finite results and converged lattice sums in a supplied
setting; unaudited; independent checks recorded below.

## In one paragraph

To read one site you have to cut it off from its neighbours, and the links to
the neighbours are where the lattice keeps its energy. In any vacuum that
carries light, those links are full. So locking a single site's possibility
releases energy at the lattice's own scale: at least a TeV even for the
coarsest lattice experiment allows, and a few billion joules if the lattice
spacing is the Planck length. Nothing like that happens when anything is
observed. A record therefore cannot be a sharp lock on one lattice site of an
entangled quantum state. It has to be a soft lock on something large, or not
a collapse at all.

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

*Statement.* For any state `rho`, any Hamiltonian `H = sum` of local terms
and any record at `x` as above,

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

*Statement.* Let `|0>` be a ground state with energy `E_0` and gap `Delta`
to the rest of the spectrum. Let `p_a = <0|P_a|0>`. Then:
- `Delta E >= Delta sum_a w_a (p_a - p_a^2)`;
- antipodal menu: `Delta E >= (Delta/2)(1 - (r.n)^2)`, where `r` is the
  site's Bloch vector;
- sphere menu: `Delta E >= Delta (3 - |r|^2)/6 >= Delta/3`.

The cost is zero only if every `P_a|0>` with `w_a p_a > 0` is itself a ground
state.

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
  `0`. This is the only zero-cost case: no entanglement, and the lock is
  aligned.
- Open blocks (exact diagonalisation). Each ground state is a singlet, and
  each cost exceeds half the gap:

| block | site (neighbours) | cost | gap / 2 |
|---|---|---|---|
| `2x2x2` | corner (3) | `3.213393 J` | `1.640179 J` |
| `2x2x3` | corner (3) | `3.150188 J` | `1.316826 J` |
| `2x2x3` | middle layer (4) | `3.739807 J` | `1.316826 J` |

## T4 — the walker's sea

*Statement.* Take the half-filled ground state of the walker with twisted
boundaries (no zero modes). Let the record fix the site's occupation in some
coin basis. That holds for every rank-one lock of the site's full possibility,
since it fixes the site's Fock state.
- **(a)** The record removes exactly the hopping terms touching the site and
  keeps the on-site terms. `Phi*(c_x^dag c_y) = 0` for `y != x`, because the
  term changes the site's occupation by one.
- **(b)** The cost is minus the energy held in the site's six bonds. By
  translation invariance that is `6/(3N)` of the total energy, so

  `Delta E = 2 <|s(k)|>_BZ t`,  `|s(k)| = (sin^2 k_1 + sin^2 k_2 + sin^2 k_3)^{1/2}`.

  It equals `2.389890 t` on `8^3` and `2.387602 t` on `256^3`: the energy of
  about `2.4` hops.
- **(c)** With the staggered mass `m`:
  `Delta E = 2 <s^2 / sqrt(s^2 + m^2)> t`, which tends to `3t^2/m` when
  `m >> t`. At `m = 100t` it is `0.029997 t`.
- **(d)** The massless sea's site is maximally mixed: its one-body block is
  `(1/2) 1`, so it carries two bits of entanglement with the rest.
- **(e)** In the massless sea every outcome of the record costs the same.
  Checked on the `2^3` and 8-site Fock spaces, in two coin bases, with odds
  `1/4` each. So no choice of odds lowers the cost.

*Proof of (a)–(b).*
- `c_x^dag c_y` shifts the occupation of `x`, so it has zero diagonal blocks
  between occupation eigenspaces of `x`.
- Every other term commutes with the site's occupation projectors.
- Each of the `3N` bonds carries the same mean energy. The site owns six of
  them. The total is `E_0 = -N <|s|> t`. ∎

*Evidence.* Fock-space brute force in the Jordan–Wigner representation equals
the correlation-matrix formula to `1e-9`:
- `2^3` (3D), `2^2` (2D), rings of 6 and 8;
- massless, and with `m = 0.7` and `m = 0.4`.

## T5 — a relativistic vacuum is not a product state

*Statement.* Let `h(k)` be a local (trigonometric-polynomial) Bloch
Hamiltonian, shifted so that its Fock vacuum is the ground state, i.e.
`h(k) >= 0`. At any zero of the lowest band, that band rises at most
quadratically.

*Proof.* Let `h(k_0) v_0 = 0` with `|v_0| = 1`. Then:
- `lambda_min(k) <= v_0^dag h(k) v_0 =: f(k)`;
- `f` is smooth, `f >= 0`, and `f(k_0) = 0`;
- so `grad f(k_0) = 0` and `f(k) = O(|k - k_0|^2)`. ∎

So conical low-energy excitations (the walker's `E = t|k|`) cannot sit above
a product vacuum. They need a filled sea, and the filled sea's sites are
entangled. That is T4(d).

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
  `exp(-(w_x - w_y)^2/(8 sigma^2))`. For smooth weights of width `R` the cost
  is about `(bond energy) x (3/2) pi^{3/2} R / (8 sigma^2) = 0.415 R/sigma^2 t`.
  The runner's exact values are within 15 % of this at `sigma >= 1`.

So making a record coarse does not make it cheap. A sharp coarse record costs
more, by the area of its surface. A soft record is cheap only if its
resolution is coarse compared with the region's own quantum fluctuations: it
must fail to resolve single quanta.

## T7 — what the numbers mean (external reference inputs, not premises)

The comparison uses outside numbers only as reference: `hbar c`, the critical
density `7.7e-10 J/m^3` and the age of the universe `4.35e17 s`. The lattice
energy `t = hbar c/a` is unknown. The runner takes three tiers:

| lattice scale `hbar c/a` | spacing `a` | one single-site record in the sea | largest vacuum formation rate the critical density allows |
|---|---|---|---|
| 1 TeV (a floor any collider-safe lattice must exceed) | `2.0e-19 m` | `2.4e12 eV = 3.8e-7 J` | `2.3e-104` per site per tick |
| `1e10 GeV` (the order of published quadratic Lorentz-violation bounds) | `2.0e-26 m` | `2.4e19 eV = 3.8 J` | `2.3e-139` per site per tick |
| Planck energy (the memo's open gate) | `1.6e-35 m` | `2.9e28 eV = 4.7e9 J` | `8.6e-185` per site per tick |

"Only records are readable": every observed outcome is fixed by records that
formed when the outcome became a fact. Under the supplied setting, each such
record, if it is a lock on one site of an entangled vacuum, releases at least
the first row's energy. Detectors register single optical photons, of order
1 eV, with no such release.

## What this does and does not say about the axioms

It says that one reading of the Record axiom fails energy bookkeeping by at
least twelve orders of magnitude. That reading is: a record is a sharp,
rank-one lock of one lattice site's possibility, acting on the lattice's
quantum state.

The readings that survive:
1. **Soft records of large things.** A record locks a collective variable
   softly: a pointer made of many sites, resolved no finer than its
   macroscopic states differ. T6(b) prices this reading. It is the shape of
   the known spontaneous-collapse models (Ghirardi–Rimini–Weber, Pearle).
   Their relativistic versions are known to excite the vacuum for the same
   reason T6 shows; that literature is reference only. This reading changes
   the Record axiom's "one site" to "a region" and "locks exactly" to "locks
   softly".
2. **Records without collapse.** A record is a stable, redundantly copied
   fact produced by the unitary dynamics (decoherence). Then no energy is
   injected, and "records form" becomes a theorem about the dynamics, not an
   independent primitive. The formation site, rate and unit, which the memo
   lists as open gates, would be computed rather than chosen.
3. **Records without a quantum state.** Excluded by the landed Bell note:
   such records cannot reach the measured correlations.
4. **Records only at unentangled sites.** In a relativistic vacuum there are
   none (T4(d), T5). A massive medium makes a record cheap only as `3t^2/m`
   (T4(c)). A record costing 1 eV at a 1 TeV lattice would need
   `m ~ 10^{12} t`, a medium that carries nothing relativistic.

It does not say:
- anything about the formation laws studied as mathematics (blocks 01–52);
- anything about the static comparator, the gravity lane's clauses or the
  moving-records reading's kinematics;
- anything about interacting vacua beyond the stated models (the Heisenberg
  blocks are one interacting check);
- which of readings 1 and 2 is right.

## Independent checks

To be recorded after the independent checks return (see the PR body).

## Reproduction

```bash
python3 scripts/record_formation_one_site_lock_costs_the_energy_of_its_bonds_2026_09_27.py
```

Expected: `TOTAL: PASS=15 FAIL=0` (about 45 s).
