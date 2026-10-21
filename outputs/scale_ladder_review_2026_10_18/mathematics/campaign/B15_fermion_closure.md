> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B15 findings: fermion matter in the curvature-member closure test



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
   - Closure against gravity's ξ = (sK/4α)ξ̃ requires v² = −sK/(4α) (C6). Hermiticity (Hermitian Clifford generators square to +1, so v² > 0) forces the Lorentzian sign s = −1, given the supplied K, α > 0 and a common relabelling orientation. The scalar needed c > 0 as a premise; here v² > 0 is derived.
   - So **v² = K/(4α), the same cone as the B14 scalar.** Every doubler gets the same v², with its own proper spin set τ (T7, exact). At the six doublers with one or two π components τ ≠ σ, so a G_f with the on-site spin term fails there at O(1); the lattice G_f needs momentum-dependent spin structure (check O5b).
2. **Specified nearest-neighbour/two-endpoint ansatz obstruction.**
   - At endpoint-mean timing, a range-2 lapse bilinear −(v²/16)(N_x M_{x+2e} − N_{x+2e} M_x)(|x⟩⟨x+2e| − h.c.) remains (T1b).
   - Same-sign diagonal pairs cancel at every timing. Mixed pairs ±(e_j−e_k) survive in proportion to w_a² − w_b², so they cancel only at the endpoint mean (check S3a).
   - Over the whole two-endpoint timing family, it vanishes only at w = 0 (T2).
   - The gravity relabelling fixes ξ up to constants (T3).
   - For the specified naive matter operator, lapse map and gravity relabelling, the displayed witness rules out an exact linear G_f repair: of any range, translation-covariant or not (T4; strengthened by check S3c and K2). Adding C(λ) or an on-site internal constraint does not help. The scalar closes exactly at order ε.
3. **Order of the obstruction.**
   - It is O(a²) at endpoint-mean timing and O(a) otherwise. The check proves both are non-absorbable by any translation-covariant G_f (O2, O3). Fitted slopes: 1.95 (t = ½), 1.08 (t = 1), 1.95 (doubler), 1.95 (Dirac with mass), 0.99 (Wilson).
   - In 1D it is not absorbable by any O(a²)-corrected relabelling (C4b). A free shift bilinear absorbs it (control, C4c).
4. **Timing and mass.**
   - The Dirac mass cross terms cancel iff the timing is the endpoint mean (T5), the same timing B14 needed for the scalar. For t ≠ ½ they are ξ̃-linear with a Clifford-odd coefficient, so they block only a Kosmann-class G_f. The endpoint mean is selected independently by the massless O(a) obstruction. The mass then drops out (T6a, C5b).
   - A Wilson term gives a Clifford-odd O(a) obstruction relative to a Kosmann-class G_f (T6b, C5a). The term is linear in κ, so a Clifford-odd O(a)-corrected G_f absorbs it; against a general G_f the obstruction is O(a²) (check O8).

## Derived vs supplied

- **Derived:**
  - the same cone K/(4α) for spin ½ as for spin 0;
  - the Lorentzian sign given Hermiticity, positive K and alpha and the common relabelling orientation;
  - the endpoint-mean timing;
  - the exact lattice no-go and its explicit monomial.
- **Supplied:** the matter operator, the G_f normalisation and the gravity sector. Newton's constant is not fixed.

## Caveats

- Flat background with no triad. A rotation (Gauss) constraint would enter with a triad.
- Tested only on the naive operator and two-endpoint timings. Geometric-mean timing and improved hoppings were not tested.
- The scaling runs are floating point with one configuration.
- **Not tested: the campaign's parameter-free Weyl step.** It is a unitary step (a QCA), not a Hamiltonian, so B15 does not directly fix K/(4α) = 2/9 in step units.

## Prior art (from memory, unchecked)

- Teitelboim 1973; Hojman–Kuchař–Teitelboim 1976; Kuchař 1974–76.
- Schwinger, Phys. Rev. 130, 800 (1963), already gives the continuum spin-0, ½ and 1 result. Nelson–Teitelboim 1978 (confirmed). Henneaux 1983 (unverified). Kosmann 1972.
- Koo–Saleur 1994 (lattice Virasoro closing only in the scaling limit); Bonzom–Dittrich arXiv:1304.5983; arXiv:2305.10097.
- New and narrow: the monomial, the no-go for any linear G_f, the timing and order classification, and the doubler spin caveat.
