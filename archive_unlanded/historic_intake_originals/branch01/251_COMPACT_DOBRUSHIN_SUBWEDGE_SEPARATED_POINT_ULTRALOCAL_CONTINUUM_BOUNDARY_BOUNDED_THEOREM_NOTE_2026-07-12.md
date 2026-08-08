# Compact-interior Dobrushin trajectories have only contact-supported gauge-invariant continuum correlations

**Date:** 2026-07-12  
**Type:** no_go  
**Status:** unaudited candidate; effective status is pipeline-derived only after independent audit.  
**Primary runner:** [`scripts/compact_dobrushin_subwedge_ultralocal_continuum_boundary_2026_07_12.py`](../scripts/compact_dobrushin_subwedge_ultralocal_continuum_boundary_2026_07_12.py)  
**Cached output:** [`logs/runner-cache/compact_dobrushin_subwedge_ultralocal_continuum_boundary_2026_07_12.txt`](../logs/runner-cache/compact_dobrushin_subwedge_ultralocal_continuum_boundary_2026_07_12.txt)

## 0. Result

Let `a_j->0` be isotropic lattice spacings for the supplied massive
Wilson--staggered model. Suppose `(beta_j,m_j)` stays in a compact subset `K`
of the strict
[Dobrushin spatial-uniqueness wedge](MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md):

```text
kappa(m)=14/(m^2+2),
alpha(beta,m)=18beta +(3/2)kappa^2(2-kappa)/(1-kappa)^2<1.             (0.1)
```

Then there are constants `lambda_K>0` and `c_K>0`, independent of `j`, such
that:

1. connected gauge-invariant local observable families separated by physical
   distance `R>0` obey
   `C L_F(a_j)L_G(a_j) exp(-lambda_K R/a_j+O(1))`;
2. if their support complexity, coefficient norm, and multiplicative
   normalization satisfy
   `log[L_F L_G |Z_F Z_G|]=o(1/a_j)`, their separated-point connected
   functions vanish;
3. the gauge-invariant OS Hamiltonian gap obeys
   `Delta_OS,j>=c_K/a_j` and therefore diverges;
4. `m_j` is bounded below by a positive constant, so the dimensionful bare
   mass parameter `m_j/a_j` diverges and direct fermionic propagation
   decouples at fixed physical separation. No pole-mass identification is
   asserted.

Thus every compact-interior trajectory has a **separated-point ultralocal**
scaling boundary for this controlled observable class. Any tight accumulation
functional tested on the covered observable families factorizes across
separated regions, so only contact-supported correlations can survive.
Contact terms, non-Gaussian
contact cumulants, and white-noise-type distributional limits may remain.
This does not assert existence of a full distribution-valued continuum field,
Gaussianity, or absence of every continuum measure.

This is the first controlled lattice-spacing classification for the coupled
model, but it is a negative boundary for a narrow trajectory class. A
continuum with nonzero separated correlations under the covered
subexponential normalizations must leave every compact interior subset: its
correlation length in lattice units must diverge, so it must approach a
critical/uniqueness boundary or use another controlled RG regime. The theorem
does not prove that such routes fail.

No Lorentz/QFT, Standard Model, GR, action-selection, or physical-probability
closure follows. No axiom-update stop is established.

## 1. Uniform weighted comparison on a compact subwedge

The direct dependency proves that at each `(beta,m)` with `alpha<1`, the
link-influence matrix has an exponential moment below one for sufficiently
small positive weight. The row majorants are continuous in `(beta,m,lambda)`
where `lambda` is the exponential distance weight.

Compactness of `K` and strictness of the inequality give

```text
sup_K alpha(beta,m)=1-epsilon_K<1,
sup_K kappa(m)=kappa_K<1.                                             (1.1)
```

Uniform continuity then supplies one `lambda_K>0` such that the weighted
influence row remains below one on all of `K`. The weighted Dobrushin
comparison theorem gives, for translated fixed local polynomials `F,G`,

```text
|omega_j(FG)-omega_j(F)omega_j(G)|
 <=C_(F,G,K) exp[-lambda_K dist_lattice(supp F,supp G)].              (1.2)
```

The cross-Wick/off-diagonal inverse proof in the dependency makes (1.2) valid
for fixed-degree local gauge--fermion polynomials, not only gauge functions.

## 2. Fixed physical separation

Embed the supports near two physical points separated by `R>0`. Their lattice
distance is at least `R/a_j-O(1)`. Equation (1.2) gives

```text
|connected_j(F,G)|<=C'_(F,G,K)exp(-lambda_K R/a_j).                   (2.1)
```

For every `N`, `a_j^(-N)exp(-lambda_K R/a_j)->0`. More generally, let
`L_F(a),L_G(a)` bound the aggregate coefficient norm and support multiplicity
of the observable families. If

```text
log[L_F(a_j)L_G(a_j)|Z_F(a_j)Z_G(a_j)|]=o(1/a_j),                    (2.2)
```

then the renormalized connected function also tends to zero. This includes
fixed local observables, power and power-times-log renormalizations,
polynomially many lattice terms, and ordinary Riemann-sum smearings with
separated physical supports. Exponentially large field rescalings,
exponentially complex supports, and nonlocal/macroscopic loop families are not
classified.

Equation (2.1) controls separated points only. It does not control coincident
contact distributions, composite-operator subtractions, or arbitrary
volume-growing observables.

## 3. Divergent physical OS gap and fermion decoupling

Uniform weighted clustering gives one `rho_K<1` for the two-step OS
contraction on every member of the family:

```text
spec(T_(2,j)|Omega_j^perp) subset [0,rho_K].                           (3.1)
```

For isotropic `a_tau,j=a_j`, spectral calculus gives

```text
Delta_OS,j>=-(2a_j)^(-1)log rho_K=:c_K/a_j -> infinity.               (3.2)
```

If a supplied anisotropic regulator is used instead, the exact statement is
`Delta_OS,j>=c_K/a_tau,j`; comparison with `1/a_j` then needs a separately
controlled spacing ratio.

Compactness of `K` also gives `m_j>=m_K>5.809...`. Hence the dimensionful
bare mass parameter is at least `m_K/a_j`, and the hopping bound gives
propagation at physical separation `R` of order
`(4/m_K)^(R/a_j)`. It vanishes exponentially.

Fixed-mass closed determinant loops nevertheless remain order one in lattice
units and can renormalize local gauge, contact, and vacuum terms. Propagating
fermion decoupling does not imply that the gauge marginal becomes the pure
Wilson measure.

The divergent lower bound is not a continuum Yang--Mills mass-gap result and
does not identify operators across the varying OS Hilbert spaces. It says the
opposite of a finite propagating mass scale: every non-vacuum gauge-invariant
excitation is pushed to infinite physical energy along this compact-interior
trajectory.

## 4. Why this does not close the continuum campaign

The usual propagating lattice continuum mechanism with nonzero separated
correlations requires a correlation
length in lattice units that diverges as `a->0`. Here the uniform Dobrushin
margin bounds that correlation length uniformly. Therefore a propagating route
in the covered subexponential local class must violate at least one
compact-interior hypothesis. Live possibilities include:

- approaching `alpha=1` so the certified decay rate can vanish;
- leaving the one-link Dobrushin wedge while remaining in a larger block or
  polymer-controlled region;
- tuning toward light mass, where the present absolute loop expansion loses
  its margin;
- a constructive RG trajectory, including the weak-bare-coupling region not
  reached by this small-`beta` certificate;
- different microscopic dynamics if the axioms eventually select another
  admissible carrier.

Nothing here proves that a new axiom or primitive is needed.

In particular, the standard Wilson weak-bare-coupling/light-lattice-mass
scaling direction lies outside this wedge: `beta=6/g_0^2->infinity` and a
fixed physical fermion mass requires `m_lat=a m_phys->0`, whereas here
`beta<1/18` and `m_lat>5.809...`. The existing free tuned continuum is
therefore a counterexample to
any broader claim that lattice scaling itself must be ultralocal.

## 5. Runner contract

Run:

```bash
python3 scripts/compact_dobrushin_subwedge_ultralocal_continuum_boundary_2026_07_12.py
```

The runner checks compact-margin examples, uniform weighted-radius continuity,
faster-than-power separated-point decay, subexponential-renormalization decay,
the `1/a` gap lower bound, fermion decoupling, and the source/N1--N8 boundary.
The weighted comparison and OS spectral theorems are analytic machinery; the
runner checks their scaling consequences.

## 6. No-Go Discipline N1--N8

This theorem has a negative continuum boundary, so all eight checks are
load-bearing.

### N1 — alternative-route enumeration

| Route | Status | Test and result | Why it remains live outside the claim |
|---|---|---|---|
| Compact strict Dobrushin interior | `ATTEMPTED` | Uniform exponential clustering proves separated-point ultralocality. | This is exactly the narrow class closed here. |
| Approach the Dobrushin boundary | `ATTEMPTED` | The uniform `lambda_K` proof fails when the margin tends to zero. | Diverging correlation length remains possible. |
| Block-Dobrushin criterion | `ATTEMPTED` | One-link failure does not imply block failure. | A larger controlled region may support tuning. |
| Polymer/cluster expansion | `ATTEMPTED` | Existing small-coupling routes use different norms. | Their boundary behavior is not classified here. |
| Light-mass constructive RG | `ATTEMPTED` | The absolute `R` loop margin is lost. | Cancellation-based RG remains live. |
| Weak-bare-coupling gauge scaling | `ATTEMPTED` | The present small-`beta` wedge does not reach it. | Standard asymptotic-scaling logic is outside scope. |
| Exponential field renormalization | `ATTEMPTED` | Condition (2.2) excludes it. | Such a normalization would need separate locality/temperedness control. |
| Alternative microscopic carrier/action | `ATTEMPTED` | The Wilson-staggered action is supplied, not axiom-selected. | A different derived dynamics can have another critical surface. |

### N2 — wall-independence audit

| Left condition | Right condition | Left closes right? | Right closes left? | Independent? |
|---|---|---:|---:|---:|
| compact strict Dobrushin interior | controlled subexponential local observable class | No | No | Yes |
| compact strict Dobrushin interior | uniform lattice correlation length | Yes | No | No |
| compact strict Dobrushin interior | propagating continuum with covered nonzero separated correlations | No | No | Yes |
| compact strict Dobrushin interior | axiom-selected action | No | No | Yes |
| controlled subexponential local observable class | uniform lattice correlation length | No | No | Yes |
| controlled subexponential local observable class | propagating continuum with covered nonzero separated correlations | No | No | Yes |
| controlled subexponential local observable class | axiom-selected action | No | No | Yes |
| uniform lattice correlation length | propagating continuum with covered nonzero separated correlations | No | No | Yes |
| uniform lattice correlation length | axiom-selected action | No | No | Yes |
| propagating continuum with covered nonzero separated correlations | axiom-selected action | No | No | Yes |

The compact-interior hypothesis supplies the uniform correlation-length bound;
they are not counted as two independent walls. Uniform mixing excludes
nonzero separated correlations only after the controlled observable and
normalization class is also imposed. Neither condition selects the microscopic
action or closes boundary-tuned, block, polymer, or RG routes.

### N3 — hidden-condition phrase scan

| Mandated phrase | Classification |
|---|---|
| `we assume` | No load-bearing hit. |
| `by construction` | No proof-substitute hit. |
| `as is standard` | No hit. |
| `the framework provides` | No hit. |
| `bridge context` | No hit. |
| `background` | No hidden background premise. |
| `naturally` | No hit. |
| `obviously` | No hit. |
| `standard QFT` | No hit. |
| `registered` | No premise-granting hit. |
| `canonical` | No unqualified use. |

### N4 — citation/residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---:|---|
| [Dobrushin uniqueness and OS-gap wedge](MASSIVE_WILSON_STAGGERED_DOBRUSHIN_SPATIAL_UNIQUENESS_WEDGE_BOUNDED_THEOREM_NOTE_2026-07-12.md) | Uniform weighted clustering and fixed-lattice gap at each strict-wedge point | Uniformize those bounds on compact `K` and scale `a->0` | Yes | Sole direct dependency. |
| Free staggered scalar continuum theorem | Free pole/dispersion scaling | Coupled compact-interior scaling | No | Context only. |
| Beta-six plaquette work | Bulk observable at fixed regulator coupling | Small-beta continuum scaling | No | Context only. |
| Dobrushin 1968 | Weighted comparison decay | Scaling consequence after compact uniformization | Yes | Transitive external machinery. |

### N5 — rhetoric and resolution audit

| Resolution | Tested? | Permitted conclusion |
|---|---:|---|
| Fixed separated local observables | Yes | Connected functions vanish. |
| Power/log field renormalizations | Yes | Still vanish. |
| Exponential field renormalizations | No | No claim. |
| Coincident/contact distributions | No | No full continuum-field existence claim. |
| Compact strict subwedge trajectories | Yes | Separated-point ultralocal boundary. |
| Boundary-tuned or outside-wedge trajectories | No | No triviality claim. |
| Gauge-invariant OS sector | Yes | Physical gap diverges. |
| Charged/unconstructed sectors | No | No gap or decoupling claim. |

### N6 — partial-closure and primitive scan

The result is a scaling theorem, not a convention. Isotropic spacing is part
of the supplied regulator trajectory; an anisotropic alternative is stated
separately. Approved primitives add no dynamics, coupling flow, field
normalization, or continuum theorem. No primitive is enlarged and no
axiom-update stop is triggered.

### N7 — hostile steelman

A hostile reviewer should say that vanishing bare connected functions does not
prove triviality after arbitrary wave-function renormalization. Correct: the
theorem explicitly covers only (2.2), including power/log normalizations, and
leaves exponentially large rescalings and contact distributions open.

The stronger hostile point is that all interesting continuum limits approach
criticality, while `K` is compactly separated from it. That is precisely the
theorem's value and limitation: it proves the controlled interior cannot be
the desired propagating continuum and directs the campaign to boundary-tuned
control.

### N8 — cross-cycle echo

| Prior surface | Similar wall | Lesson here |
|---|---|---|
| Free staggered continuum | Pole scaling survived because the mass/spacing trajectory was tuned | Fixed large lattice mass here instead diverges physically. |
| Spatial DLR accumulation | Existence alone did not select a phase | Uniform uniqueness now selects a phase but also bounds correlation length. |
| Dobrushin uniqueness wedge | Strict decay gave a fixed-lattice gap | Compact uniformization makes the physical gap diverge as `a->0`. |
| Beta-six strong-coupling work | Fixed-coupling control did not supply continuum scaling | This theorem states the scaling consequence rather than importing one. |

The negative boundary is trajectory-specific and leaves all critical/RG routes
open.
