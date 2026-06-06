# Emergent Lorentz — Mathematics Sector Search (Exercise Four)

Governing fact: every time-bearing construction in the repo introduces an independent temporal
spacing `a_τ` by hand (`H = −(1/a_τ) log T̂`; Wick `n·a_τ → it`). The ratio `c_t/c_s = a_τ/a` is
exactly the marginal coefficient. Any lens that CONSUMES H / the wedge vacuum / the continuum
measure inherits the chosen `a_τ` and cannot bootstrap the ratio. This filter kills the
"decisive-looking" lenses.

| Sector | Reframe | Tool/theorem | How it attacks | Falsifier | First artifact |
|---|---|---|---|---|---|
| **Modular / Bisognano–Wichmann** | boost = modular flow of wedge algebra | BW 1975-76; Tomita–Takesaki; KMS | if Record's KMS Δ acted geometrically (a boost) it'd fix the metric → c_t=c_s | Δ acts as energy translation, not geometric; depends on input a_τ | modular-flow geometric test on lattice wedge state |
| **RG / dynamical systems** | c_t/c_s = anisotropy coupling ξ; attractive IR fixed point? | Symanzik; Karsch anisotropy; Nielsen-Ninomiya β | dξ/d log b < 0 ⇒ c_t=c_s forced (given dynamics) | β=0 marginal line ⇒ a_τ stays free | block-spin dξ/d log b on free + β=6 plaquette vertex |
| **Reflection positivity / OS** | does OS constrain time-norm vs space? | OS; Osterwalder–Seiler | if RP held only at c_t=c_s | RP holds for a RANGE of a_τ>0 (it does) | inspect T=e^{−a_τ H} PSD ∀ a_τ (yes → no constraint) |
| **Rep theory / branching** | O_h⊂SO(3)⊂SO(3,1); Cl(3,0)→Cl(3,1) | branching; sign-branch | fixes the boost GENERATOR (not the metric ratio) | ε=+1 admissible (so(4)) | already built (boost-from-bivectors) |
| **Information geometry** | c_t=c_s as Record-additivity extremum | Fisher; large deviations | if isotropy were the unique additivity-compatible norm | additivity is scale-blind in a_τ | test I-additivity vs a_τ/a (expected: no constraint) |
| **Index / Nielsen-Ninomiya** | no-doubling ↔ dispersion shape | NN homotopy | forces dispersion SHAPE near poles | says nothing about τ/space ratio | naive-fermion species note (exists) |
| **Convexity / SDP** | c_t=c_s = unique positivity extremum | SDP feasibility; moment problems | if feasible region collapses to diagonal | feasible region is a 2D cone (it is) | SDP feasibility on the moment matrix |
| **Category** | Minkowski = terminal object given Z³+Record | universal properties | if SO(3,1) is unique completion | not unique without a metric input | sketch universal arrow fixing a_τ |

## Top-2 (with teeth) + assessment
- **#1 Modular / Bisognano–Wichmann — turns into a NO-GO (circular).** BW says the modular flow of a
  wedge algebra in an *already-relativistic* vacuum IS the Lorentz boost. The repo's Unruh/KMS notes
  invoke BW only AFTER assuming the retained boost generator + Minkowski-limit Rindler wedge. On the raw
  lattice the modular Hamiltonian is `K=βD=a_τ·L_τ·H` whose flow is ENERGY translation, not a geometric
  boost, carrying a_τ as a free input. Geometric modular action ⇔ relativistic normalization (Buchholz–
  Summers "geometric modular action"): they are the SAME condition. So BW presupposes c_t=c_s; it cannot
  force it. First artifact: modular-flow geometric test (predict: geometric only as ξ→1, a→0).
- **#2 RG anisotropy fixed point — the only path to FORCING c_t=c_s, but needs dynamics.** ξ=c_t/c_s is a
  marginal coupling; the decisive question is sign(β). Interactions can drive ξ→1 (irrelevant once an
  anomalous dimension appears). But {Lattice, Quantum, Record} contain NO dynamics → no β to compute
  until a kinetic term + interaction (the β=6 plaquette) is supplied. First artifact: one block-spin step
  on `c_t p_τ²+c_s|p|²`, extract dξ/d log b at the free fixed point, then add the framework's quartic.

## Honest assessment
No sector forces `c_t=c_s` from {Lattice, Quantum, Record} with no new principle: the ratio `a_τ/a` is a
DYNAMICAL normalization and the axioms contain NO dynamics. Lenses with apparent teeth (modular/BW, OS/RP,
KMS, Unruh) all CONSUME a chosen a_τ. The **boost GENERATOR** (distinct from the metric ratio) is in much
better shape — Cl(3,0)→Cl(3,1) gives K_i=iσ_i/2 with [K,K]=−εJ, faithful-Weyl selected over scalar; the
only open generator item is the massive partner-chirality + the ε=−1 signature. The cheapest forced
addition (if one insists) is a Euclidean kinetic-normalization / 4D-hypercubic premise; the RG lens is the
only route that could UPGRADE it from a bare stipulation to a derived attractor — given the framework's own
β=6 plaquette dynamics. Net: the BUILT result (route-selection to continuous time) avoids needing any of
these by removing a_τ entirely at the free/structural level; RG (interacting) is the next real frontier.
