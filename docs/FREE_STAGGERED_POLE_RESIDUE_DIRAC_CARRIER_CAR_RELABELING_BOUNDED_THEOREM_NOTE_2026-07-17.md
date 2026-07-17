---
claim_id: free_staggered_pole_residue_dirac_carrier_car_relabeling_bounded_theorem_note_2026-07-17
claim_type_author_hint: bounded_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Free-Staggered Pole-Residue Dirac Carrier And Finite CAR Relabelling (Bounded)

**Date:** 2026-07-17
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note proposes a
bounded claim type; it does not set or predict an audit verdict or effective
status.
**Primary runner:**
[`scripts/free_staggered_pole_residue_dirac_carrier_car_relabeling_2026_07_17.py`](../scripts/free_staggered_pole_residue_dirac_carrier_car_relabeling_2026_07_17.py)
**Runner cache:**
[`logs/runner-cache/free_staggered_pole_residue_dirac_carrier_car_relabeling_2026_07_17.txt`](../logs/runner-cache/free_staggered_pole_residue_dirac_carrier_car_relabeling_2026_07_17.txt)

## 0. Why this is a new bridge

The existing free-Dirac/Poincare support runner starts with the continuum mass
shell, its standard boosts, the measure `d^3p/(2E)`, and a CAR
particle/antiparticle mode split. Rechecking those continuum identities does not
explain why those are the correct objects on the repo's free-staggered surface.

This note instead starts with the finite-spacing blocked symbol already
established by the retained bounded Clifford-core authority,

```text
    D_a(q) = m I_16 + i sum_(mu=0)^3 alpha_mu sin(a q_mu)/a,
    {alpha_mu, alpha_nu} = 2 delta_(mu nu) I_16,
```

and derives the continuum carrier from its complex-energy pole, its pole
residue, and its Hamiltonian spectral projectors. The registered
kinetic-isotropy primitive is load-bearing: it identifies the temporal kinetic
coefficient with the already normalized spatial coefficient. The invariant
mass-shell density is therefore an output of the residue calculation rather
than an imported continuum convention.

The last step constructs the finite CAR representation and the negative-branch
hole relabelling explicitly. That construction supplies the *given-CAR* finite
mode algebra used by the downstream bounded runner. It does not assert that the
four framework axioms select CAR statistics.

## 1. Inputs and exact authority boundary

Load-bearing one-hop authorities are:

- [`ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md`](ABJ_P_REC_SPINTASTE_CLIFFORD_CORE_BRIDGE_NOTE_2026-06-18.md)
  — supplies the finite `16 x 16` blocked free-staggered symbol, the four
  Euclidean Clifford generators, the rank-16 spin algebra, and the rank-16
  taste commutant. Its current audit-pipeline effective status is
  `retained_bounded`.
- [`KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
  — registered primitive supplying only equality of temporal and spatial
  kinetic form, `c_t=c_s`. Since the retained symbol has spatial coefficient
  normalized to one, the temporal coefficient is one on this surface.

These roles do not duplicate one another. The retained parent displays the
symmetric four-label Euclidean formula as a finite algebraic free surface, but
its audit boundary does not identify the `mu=0` regulator label with the
framework's emergent physical-time normalization. All finite Clifford and
projector identities below use the parent alone. The registered primitive is
consumed only when `q_0` is continued as the physical energy coordinate and
its coefficient is compared with the three `Z^3` spatial coefficients. Without
that identification the allowed replacement is the `lambda`-deformed temporal
term in Section 6.1, and the target mass shell does not follow.

Non-graph comparison:
`FERMION_PARITY_PAULI_TENSOR_INVOLUTION_NARROW_THEOREM_NOTE_2026-05-10.md`
checks occupation and parity identities on a *given* finite qubit tensor
product. It supplies neither that tensor product as a physical composition nor
cross-mode CAR, and the Pauli/Jordan-Wigner identities needed here are derived
again in Section 5. It is therefore context, not a load-bearing dependency.

The actual Lattice+Qubit+Admissibility+Record surface is fixed by
`MINIMAL_AXIOMS_2026-06-29.md`. It is boundary context rather than a
load-bearing dependency of this bounded theorem: Qubit supplies a one-site
`M_2(C)` possibility algebra, but the axiom memo explicitly supplies no
dynamics, kinetic branch, global composition theorem, or statistics selector.
The finite mode tensor product in Section 5 is consequently a constructed
given-CAR carrier, not a claimed axiom consequence.

No literature result, observed/fitted value, audit verdict, new axiom, or new
primitive is an input.

## 2. Finite-spacing pole and residue

Fix an arbitrary mass parameter `m>0` and lattice spacing `a>0`. Write

```text
    s_i(a,p) = sin(a p_i)/a,
    omega_a(p) = sqrt(m^2 + sum_i s_i(a,p)^2).
```

Analytically continue only the Euclidean energy variable to `q_0=i E`. Since
`sin(i a E)=i sinh(aE)`, the scalar denominator of `D_a(q)^(-1)` is

```text
    Delta_a(iE,p)
      = m^2 + sum_i s_i(a,p)^2 - sinh(aE)^2/a^2.
```

On the principal low-energy time patch `q_0=iE` with `E>0`, it has the unique
pole

```text
    E_a(p) = asinh(a omega_a(p))/a.                         (2.1)
```

This is not inserted as a continuum dispersion. It is the positive complex
pole of the finite-spacing retained symbol on that patch. Periodically shifted
temporal images are not claimed absent; they belong to the blocked
taste/doubler structure and are outside this single-patch pole extraction.

The derivative of the scalar denominator at the pole is

```text
    partial_(q_0) Delta_a |_(q_0=iE_a)
      = 2 i omega_a(p) cosh(a E_a(p)).                      (2.2)
```

Therefore the positive-pole scalar residue density is

```text
    rho_a(p) = 1 / (2 omega_a(p) cosh(a E_a(p)))
             = 1 / (2 omega_a(p) sqrt(1+a^2 omega_a(p)^2)). (2.3)
```

Both `E_a` and `rho_a` are outputs of one finite-spacing denominator.

## 3. Dirac spectral fibers at finite spacing

Use the Euclidean-to-Minkowski Clifford identification on the retained
generators,

```text
    gamma^0 = alpha_0,
    gamma^i = i alpha_i,
```

and define the finite-spacing Hamiltonian symbol

```text
    H_a(p) = m alpha_0 + i sum_i alpha_0 alpha_i s_i(a,p).  (3.1)
```

The retained Euclidean Clifford relations imply, without a diagonalization
assumption,

```text
    H_a(p)^dagger = H_a(p),
    H_a(p)^2 = omega_a(p)^2 I_16.                           (3.2)
```

Hence

```text
    P_(a,+)(p) = (I_16 + H_a(p)/omega_a(p))/2,
    P_(a,-)(p) = (I_16 - H_a(p)/omega_a(p))/2               (3.3)
```

are orthogonal rank-eight spectral projectors. The rank is two spin states
times the retained fourfold taste multiplicity. No single physical taste is
selected.

At `q_0=iE_a`, the Euclidean numerator factorizes as

```text
    m I_16 + alpha_0 omega_a - i sum_i alpha_i s_i
      = 2 omega_a P_(a,+) alpha_0.                          (3.4)
```

Thus the spinor pole residue is the positive spectral fiber multiplied by the
same scalar derivative that produced `(2.3)`. The positive carrier and its
measure are two parts of one pole calculation.

The fiber trivialization need not be chosen as an external spinor convention.
Put

```text
    A_i = i alpha_0 alpha_i,
    Q_0 = (I_16+alpha_0)/2,
    T_a(p) = [omega_a+m+sum_i A_i s_i(a,p)] Q_0
             / sqrt(2 omega_a(omega_a+m)).                 (3.5)
```

The same Clifford multiplication gives the exact partial-isometry identities

```text
    T_a(p)^dagger T_a(p) = Q_0,
    T_a(p) T_a(p)^dagger = P_(a,+)(p).                     (3.6)
```

Because `T_a` is made only from the spin Clifford generators, it commutes with
the retained taste commutant. Equations `(3.5)`-`(3.6)` therefore identify
every finite-spacing positive pole fiber with one fixed rank-eight rest fiber,
without importing a measurable frame or continuum spinor basis.

The rest-fiber little-group action is also internal to the same Clifford
factor. With spatial indices `j,k in {1,2,3}`, define

```text
    J_i = -(i/4) sum_(j,k) epsilon_(ijk) alpha_j alpha_k.   (3.7)
```

The Clifford relations give

```text
    [J_i,J_j] = i epsilon_(ijk) J_k,
    sum_i J_i^2 = (3/4) I_16,
    [J_i,Q_0] = 0.                                        (3.8)
```

Each `J_i` commutes with the taste commutant as well. Hence its restriction to
`Ran Q_0` is exactly four spectator-taste copies of the spin-one-half `SU(2)`
carrier; this is derived from the retained Clifford block rather than attached
as an external spin label.

## 4. Continuum carrier and Poincare action

For any fixed compact momentum set `K subset R^3`, Taylor expansion is uniform
on `K`. With `S_4(p)=sum_i p_i^4`, the first two scalar expansions are

```text
    E_a(p) = E(p)-a^2 [E(p)^3/6+S_4(p)/(6E(p))]+O_K(a^4),
    rho_a(p) = 1/(2E(p))
               +a^2 [S_4(p)/(12E(p)^3)-E(p)/4]+O_K(a^4).  (4.1)
```

Consequently,

```text
    s_i(a,p) = p_i + O_K(a^2),
    E_a(p) = E(p) + O_K(a^2),
    rho_a(p) = 1/(2E(p)) + O_K(a^2),
    P_(a,+)(p) = P_+(p) + O_K(a^2),                         (4.2)
    E(p) = sqrt(m^2 + |p|^2).
```

The exact maps `T_a(p)` converge uniformly on the same compact sets to
`T(p)`, obtained from `(3.5)` by replacing `(omega_a,s_i)` with `(E,p_i)`.
They identify the limiting fibers with `Ran Q_0`, which the retained
spin/taste factorization identifies as `C^2_spin tensor C^4_taste`. The
limiting positive one-particle carrier is therefore

```text
    h_+ = L^2(R^3, d^3p/(2E(p)); C^2_spin tensor C^4_taste). (4.3)
```

The explicit `T(p)` is an isometry from the displayed spin/taste coefficient
fiber onto `Ran P_+(p)`, so `(4.3)` is equivalently the direct integral of the
spectral fibers in `(3.3)`. Its base is the positive sheet

```text
    H_m^+ = { p in R^(3,1) : (p^0)^2-|p|^2=m^2, p^0>0 }.
```

The measure in `(4.3)` was not chosen by covariance. It is the `a -> 0` limit
of the finite-spacing residue `(2.3)`. Once this pole-derived quadratic form
and positive sheet are present, their connected linear stabilizer is the
proper orthochronous Lorentz group. A boost in direction `i` has tangent field
`E partial_(p_i)`, and

```text
    div_p( (1/(2E)) E e_i ) = 0,                            (4.4)
```

so the pole-derived limiting measure is invariant. Flat `d^3p` fails because
`div_p(E e_i)=p_i/E`.

On the derived positive sheet, the rotation-free positive symmetric Lorentz
map from rest to `p` is fixed algebraically by

```text
    L(p)^0_0 = E/m,
    L(p)^0_i = L(p)^i_0 = p_i/m,
    L(p)^i_j = delta_ij + p_i p_j/[m(E+m)].                 (4.5)
```

Direct multiplication gives `L(p)^T eta L(p)=eta` and
`L(p)(m,0)=(E,p)`; no boost matrix is imported before the shell is derived.
For a Lorentz transformation `Lambda`,

```text
    W(Lambda,p) = L(Lambda p)^(-1) Lambda L(p)
```

fixes `(m,0)` and is a spatial rotation. The `SU(2)` lift derived in
`(3.7)`-`(3.8)`, transported from `Ran Q_0` by `T(p)`, carries that Wigner
rotation while the taste commutant is a spectator. Thus the pole-derived
carrier supports the induced action

```text
    (U(y,Lambda) psi)(p)
      = exp(i y.p) D^(1/2)(W(Lambda,Lambda^(-1)p))
        psi(Lambda^(-1)p),                                 (4.6)
```

diagonally on taste. Measure invariance gives unitarity. Direct cancellation
of the adjacent standard boosts gives

```text
    W(Lambda_2 Lambda_1,p)
      = W(Lambda_2,Lambda_1 p) W(Lambda_1,p),               (4.7)
```

which gives the group law. Equations `(4.6)`-`(4.7)` are consequences on the
derived carrier, not the starting point of the derivation.

This bounded statement does not claim essential self-adjointness of
infinitesimal generators, a common analytic core, or OS/Wightman
reconstruction.

## 5. Finite CAR construction and antiparticle relabelling

Take any finite momentum/spin/taste truncation of the positive and negative
projector fibers. Let its ordered mode list have length `N`. On the explicit
finite qubit tensor space `(C^2)^(tensor N)`, define

```text
    sigma_+ = [[0,1],[0,0]],    sigma_- = sigma_+^dagger,
    c_r = (product_(s<r) Z_s) sigma_+^(r),
    c_r^dagger = (product_(s<r) Z_s) sigma_-^(r).            (5.1)
```

With this displayed basis convention, `c_r^dagger c_r=diag(0,1)` on mode
`r`; the `+/-` labels on the Pauli ladders carry no unstated occupancy
convention.

Direct Pauli multiplication gives

```text
    {c_r,c_s}=0,
    {c_r^dagger,c_s^dagger}=0,
    {c_r,c_s^dagger}=delta_(rs) I.                          (5.2)
```

The strings are load-bearing: without them, distinct-factor ladders commute
and the off-site anticommutator is twice their nonzero product.

Any unitary spectral/Fourier change of basis `d=V^dagger c` preserves `(5.2)`.
The `+omega_a/-omega_a` eigenspaces label the two branches, while the positive
transfer-energy weight of each pair is the pole value `E_(a,r)` from `(2.1)`.
The diagonal finite-mode Hamiltonian before the hole relabelling is therefore

```text
    H_raw = sum_r E_(a,r)
              (d_(+,r)^dagger d_(+,r)
               - d_(-,r)^dagger d_(-,r)).                  (5.3)
```

Define

```text
    a_r = d_(+,r),
    b_r^dagger = d_(-,r),
    b_r = d_(-,r)^dagger.                                  (5.4)
```

Then `(5.2)` implies

```text
    d_-^dagger d_- = b b^dagger = I-b^dagger b.
```

After subtracting the filled-negative-branch vacuum energy, equivalently
adding `sum_r E_(a,r)` to `(5.3)`, the normal-ordered Hamiltonian is

```text
    H_N = sum_r E_(a,r)
            (a_r^dagger a_r + b_r^dagger b_r) >= 0.         (5.5)
```

This is the exact finite CAR particle/antiparticle relabelling used by the
downstream bounded runner. It is derived here from the pole-defined spectral
split plus `(5.1)`-`(5.2)`.

The construction is not a statistics-selection theorem. The four axioms do not
state that the physical global algebra is this tensor/exterior CAR functor, and
the comparison parity theorem likewise assumes its tensor product. This note
supplies a concrete given-CAR carrier for the bounded free-mode calculation; it
does not claim that Qubit alone forces CAR over commuting hard-core
alternatives.

## 6. Load-bearing falsifiers

### 6.1 Temporal kinetic anisotropy

For `lambda>0`, replace the temporal term by
`i lambda alpha_0 sin(aq_0)/a` while keeping the
retained spatial normalization fixed. The pole becomes

```text
    E_(a,lambda) = asinh(a omega_a/lambda)/a
      -> omega_0/lambda.
```

For `lambda != 1`, the limiting shell is

```text
    lambda^2 (p^0)^2-|p|^2=m^2,
```

not the target quadratic form in the registered space-time normalization. The
residue also gains the corresponding `1/lambda` factor. Therefore the
kinetic-isotropy primitive is necessary for this exact bridge; it is not
decorative.

### 6.2 Missing Jordan-Wigner strings

With `c_r=sigma_+^(r)` on disjoint tensor factors,

```text
    {c_r,c_s}=2 sigma_+^(r) sigma_+^(s) != 0,   r != s.
```

Thus local qubit ladders and parity alone do not supply CAR. The string/exterior
construction in Section 5 is necessary for the relabelling theorem.

### 6.3 Noncompact momentum scaling

The uniform convergence in `(4.1)`-`(4.2)` is on fixed compact
physical-momentum sets.
If momenta scale to Brillouin-zone corners as `a -> 0`, the other taste/doubler
patches remain. The same caution applies to periodic temporal pole images away
from the principal time patch. The theorem therefore supplies four taste
copies of the continuum free carrier; it does not prove a single-taste
physical selector.

## 7. Exact claim surface

This note claims only:

1. the exact finite-spacing pole, residue density, Hamiltonian, spectral
   projectors, rest-fiber partial isometry, and spin-one-half rest action
   derived from the retained blocked free-staggered Clifford symbol;
2. compact-momentum `O(a^2)` convergence to the free massive Dirac positive
   mass shell, the measure `d^3p/(2E)`, and its rank-two-times-four-taste
   spectral fiber;
3. the induced free one-particle Poincare carrier on that pole-derived limit;
4. an explicit finite Jordan-Wigner CAR realization and exact
   particle/antiparticle hole relabelling on finite mode truncations;
5. the temporal-anisotropy and no-string falsifiers showing that kinetic
   isotropy and the CAR construction are load-bearing.

It does **not** claim:

- that Lattice+Qubit+Admissibility+Record selects the canonical free-staggered
  action or any dynamics;
- that the framework selects CAR statistics, a physical global tensor
  composition, or spin-statistics;
- a physical single-taste selector;
- OS/Wightman reconstruction, microcausality, generator-domain or essential
  self-adjointness results;
- an interacting, gauged, or radiatively complete Lorentz theorem;
- a new axiom, primitive, observed input, fit, literature proof input, audit
  verdict, or publication-status change.

Those exclusions do not block the narrower downstream use. The target
free-Dirac/Poincare row already excludes lattice emergence, statistics
selection, OS reconstruction, and domain/exponentiation claims. It needs a
one-hop authority for the continuum carrier and the *given-CAR* relabelling
used by its runner; Sections 2-5 provide exactly that bounded surface, subject
to independent audit.

## 8. Validation

Run:

```bash
python3 scripts/free_staggered_pole_residue_dirac_carrier_car_relabeling_2026_07_17.py
```

The runner checks:

1. dependency/premise classes and the downstream one-hop source edge;
2. the exact blocked `Cl_4` algebra, spin-one-half rest action, and
   fourfold-taste spectral multiplicity;
3. the complex pole equation and scalar residue derivative;
4. the pole-numerator/projector identity and explicit rest-fiber partial
   isometry;
5. `O(a^2)` compact-momentum convergence of energy, residue, and projector;
6. the anisotropic-temporal falsifier;
7. invariance of the pole-derived limiting measure and failure of flat measure;
8. exact finite Jordan-Wigner CAR plus the no-string counterexample;
9. CAR preservation under Hamiltonian spectral diagonalization;
10. exact hole relabelling and nonnegative normal-ordered spectrum;
11. source boundary and dependency-edge guardrails.

Expected summary: `SCORECARD PASS=11 FAIL=0`.
