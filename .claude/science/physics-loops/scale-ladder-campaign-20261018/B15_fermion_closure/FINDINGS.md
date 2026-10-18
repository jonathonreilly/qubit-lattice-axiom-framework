# B15 findings: fermion matter in the curvature-member closure test

Provenance: a worker of the same model family; not yet checked. Saved by the supervisor from the hand-back. Runners:
- `b15_lattice_exact.py`: PASS=10 FAIL=0 at L=5; T7 also passes at L = 4 and 6.
- `b15_continuum.py`: PASS=10 FAIL=0.
- `b15_scaling.py`: PASS=5 FAIL=0.

First-run logs are kept for two corrected expectations: the diagonal next-neighbour pairs cancel, and a sign error in the doubler spin orientation. A mod-L indexing bug was fixed before the reported runs.

## Setup (supplied)

- **Matter:** a naive nearest-neighbour two-component Weyl field, h_N = Σ_b w̄_b (−iv/2)(σ^j|x⟩⟨x+e| − h.c.), giving H = vσ·sin p. Doublers are kept. A Dirac variant adds mass and Wilson terms.
- **Bond timing:** w̄ = w_a N_x + w_b N_{x+e}.
- **Bracket:** Grassmann bracket {ψ̄Aψ, ψ̄Bψ} = −iψ̄[A,B]ψ, checked exactly (T0).
- **Relabelling G_f:** normalised by {ψ, G_f[ξ]} = L_ξψ. The spin term (i/4)(∇×ξ)·σ is fixed by rotation invariance of σ·∇; this is the Kosmann value (C1).
- **Gravity:** the 09-24 curvature member, as in B14.

## Results

1. **Leading order.**
   - Continuum: [h_N, h_M] = −v² L_w, with w = N∇M − M∇N (C2). The spin term comes out of the bracket automatically.
   - Lattice: the O(a⁰) part has the same form for every timing (C3a).
   - Closure against gravity's ξ = (sK/4α)ξ̃ requires v² = −sK/(4α) (C6). Hermiticity (real v) forces the Lorentzian sign s = −1 by itself.
   - So **v² = K/(4α), the same cone as the B14 scalar.** Every doubler gets the same v², with spin set τ = (σ¹, −σ², −σ³) (T7, exact).
2. **No exact lattice closure.**
   - At endpoint-mean timing, a range-2 lapse bilinear −(v²/16)(N_x M_{x+2e} − N_{x+2e} M_x)(|x⟩⟨x+2e| − h.c.) remains (T1b). The diagonal pairs cancel through {σ^j, σ^k} = 0.
   - Over the whole two-endpoint timing family, it vanishes only at w = 0 (T2).
   - The gravity relabelling fixes ξ up to constants (T3).
   - So no linear, translation-covariant G_f closes the algebra exactly (T4). The scalar closes exactly at order ε.
3. **Order of the obstruction.**
   - It is O(a²) at endpoint-mean timing and O(a) otherwise. Fitted slopes: 1.95 (t = ½), 1.08 (t = 1), 1.95 (doubler), 1.95 (Dirac with mass), 0.99 (Wilson).
   - In 1D it is not absorbable by any O(a²)-corrected relabelling (C4b). A free shift bilinear absorbs it (control, C4c).
4. **Timing and mass.**
   - The Dirac mass cross terms cancel iff the timing is the endpoint mean (T5), the same timing B14 needed for the scalar. The mass then drops out (T6a, C5b).
   - A Wilson term gives a Clifford-odd O(a) obstruction (T6b, C5a).

## Derived vs supplied

- **Derived:**
  - the same cone K/(4α) for spin ½ as for spin 0;
  - the Lorentzian sign, from Hermiticity alone;
  - the endpoint-mean timing;
  - the exact lattice no-go and its explicit monomial.
- **Supplied:** the matter operator, the G_f normalisation and the gravity sector. Newton's constant is not fixed.

## Caveats

- Flat background with no triad. A rotation (Gauss) constraint would enter with a triad.
- Tested only on the naive operator and two-endpoint timings. Geometric-mean timing, improved hoppings, and an O(a)-corrected G_f for t ≠ ½ were not tested.
- The scaling runs are floating point with one configuration.
- **Not tested: the campaign's parameter-free Weyl step.** It is a unitary step (a QCA), not a Hamiltonian, so B15 does not directly fix K/(4α) = 2/9 in step units.

## Prior art (from memory, unchecked)

- Teitelboim 1973; Hojman–Kuchař–Teitelboim 1976; Kuchař 1974–76.
- Schwinger 1962–63; Nelson–Teitelboim 1978; Henneaux 1983; Kosmann 1972.
- New and narrow: the lattice no-go, the obstruction monomial, the diagonal cancellation, and the timing selections.
