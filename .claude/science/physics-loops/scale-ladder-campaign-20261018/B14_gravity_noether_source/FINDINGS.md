# B14 findings: does constraint closure make matter's stress the Noether source? (gravity lane, P-G3/G2)

Provenance: a worker of the same model family; not independently checked. Saved by the supervisor from the hand-back. Runners:
- `b14_lattice_closure.py`, exact rational arithmetic, PASS=9 FAIL=0 on 4³ and 5³;
- `b14_continuum_leading_order.py`, exact sympy, PASS=7 FAIL=0.

## Setup

- **Gravity:** the 09-24 curvature member (block-62 placement, R1, kinetic term at β = −α, four-corner face timing, relabelling G_g).
- **Matter (supplied):** a site scalar, H_m(N) = Σ N(π²/2 + μφ²/2) + Σ_bonds N̄(c/2)(Δφ)², with relabelling G_m.
- **Coupling ansatz:** 18 cubic-covariant nearest-neighbour forms.

## Results

1. **E1.** The 09-24 closure is reproduced.
2. **E2, exact at order ε.**
   - {H_m(N), H_m(M)} = G_m[−cξ̃] holds only with endpoint-mean bond timing.
   - The total closes iff c = −sK/(4α). So the curvature term must carry the GR sign, C = kin − K·R1 + H_m; the 09-24 runner's +K·R1 is wrong once matter is present.
   - Two species close only if c₁ = c₂ = K/(4α). **There is one matter cone, shared by every species**, and K = 4α gives speed 1.
3. **E3.** At order Pφ², cross terms vanish only with lapse timing matched to the gravity kinetic term.
4. **E4.** At order hφπ, with the structure function free, only the trace coupling (a lapse rescaling) and h_jj·φ² close exactly. The lattice metric stress fails exact closure.
5. **E5.** No coupling in the ansatz closes {G,C} at order φ². The obstruction is an O(a²) lattice-artefact term, π_x π_{x+e} ξ_b (N_{x+e} − N_x).
6. **E6.** With the lattice GR stress, the {G,C} residual falls 0.35 → 0.14 → 0.048 at L = 12, 16, 24. Without coupling it stays near 1.1. No power law was fitted.
7. **Continuum, leading order.**
   - {C,C} forces c = K/(4α).
   - {G,C} forces the coupling to be the metric-variational stress of H_m(g) with unit strength for every species, plus one shared free trace λ.
   - A scalar lapse sets λ = 0, so the coupling is unique, and the structure function is g^ij = δ − h.

## What is derived and what is supplied

- **Derived:**
  - a common matter cone for every species, K/(4α);
  - the curvature-term sign;
  - universal Noether-stress coupling at leading order;
  - the structure function;
  - the lapse timings.
- **Supplied:** the matter Hamiltonian and its relabelling, δ_ξh = 2∂ξ, the scalar-lapse rule, and the ansatz.
- **Not fixed:** Newton's constant.
- **Prior art:** Kuchař; Hojman–Kuchař–Teitelboim 1976.
- **Lattice-specific:** exact closure holds only at order ε; it fails at O(a²) once matter couples to h.

## Caveats

- Linearised, at flat strain.
- Only a scalar was tested.
- One finite ansatz, small tori, and sampled lapses.
