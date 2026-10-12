# A common scalar spectral response and quantum coherence construction

Author status: conditional-support. Intended claim type: bounded_theorem for
the specified linear mediator and source channels. Observation-level fitting,
nonlinear continuum completion and microscopic selection remain open.

## Why this mechanism is being tested

Light travel time, nonrelativistic force and freely propagating waves sample
different parts of a mediator's response. Their simultaneous interpretation
therefore requires a specified response law. Quantum interference adds a
second requirement: the mediator must have an admissible correlation function,
not merely a chosen mean Green function. A canonical quantum scalar family
provides both with one spectral measure. A massless metric sector is supplied
separately; the scalar is a proposed shared modification across matter sectors.

This construction uses familiar free-field and coherent-state machinery.
Its target is an explicit common-parameter observation map with calculable
force/coherence relations, not novelty of the spectral representation itself.
Current-main and matching PR9476 source searches are recorded in runtime
`gravity/quantum_prior_search.txt` and `quantum_open_pr_search.txt`. The exact
Q1 referee's positive-energy argument concerns a different configuration-label
model and a vacuum-absorption question; it supplies no formula used here.

The immutable model contract is `SCALAR_CONTINUUM_CONTRACT.json`, SHA-256
`cfaf1f7412a964895958dd36f2eb63ce0d66974f65730261e8e43cc0c0d6fe79`.
No experimental outcome was fitted by this mathematical construction.

## Field, couplings and admissibility

Use natural units ℏ=c=1 in this section. Let ν be a finite normalized positive
measure on masses μ≥0. Independent canonical Klein–Gordon fields define a
Gaussian field Φ whose vacuum two-point function is

    W(x−y)=∫ν(dμ)∫d³k/[(2π)³2ωμ(k)]
                     exp[−iωμ(k)(t_x−t_y)+ik·(x−y)],
    ωμ(k)=√(k²+μ²).

For a test function f, W(f*,f) is an integral of nonnegative squared Fourier
amplitudes divided by 2ω. This directly proves the two-point positivity needed
for the Gaussian Fock construction. Each mass has positive energy, stable
frequency and a commutator supported on/inside the Minkowski cone; positive
integration preserves those properties, in the distributional sense. The
Gaussian higher correlations are Wick contractions of this same W.

With Fourier convention W(t,k)=∫dω/(2π)e^(−iωt)W̃(ω,k),

    χ_R(ω,k)=∫ν(dμ)/[k²+μ²−(ω+i0)²],
    W̃(ω,k)=2π θ(ω)∫ν(dμ)δ(ω²−k²−μ²),
    Ñ(ω,k)=π∫ν(dμ)δ(ω²−k²−μ²)
           =sign(ω) Im χ_R(ω,k).

Here N is the half-anticommutator covariance. These factors follow from the
canonical mode expansion. The equality is a vacuum statement. A thermal state
multiplies the symmetric spectral measure by coth(β|ω|/2); a general occupied
or nonstationary state needs its own correlation law. The retarded response
alone is not a state specification.

A common matter coupling has the form Φ Σ_a d_a O_a/M_*, where the declared
O_a can be dimension-four mass, electromagnetic and gluonic operators. All
sectors see this same Φ and ν; their charges are derivatives of their energies
with respect to that fixed coupling-basis vector. They are not independently
chosen noise strengths. Deriving the d_a, SM operators or M_* is not part of
this construction. A body's linear scalar charge g_A is dimensionless in the
worldline interaction g_A∫dt Φ(x_A). This charge and its finite spatial profile
must be calculated before comparing a particular material or clock.

## Static field and a three-parameter spectral family

Exchange between ideal point charges gives

    V_AB(r)=−g_Ag_B/(4πr) Y(r), Y(r)=∫e^(−μr)ν(dμ).

An extended source requires convolution of this pair kernel with its charge
density. For compact spherical sources the exterior form factor in
`DERIVATION.md` applies mass by mass. The point formula is not silently used
for a finite source at separations comparable to its size.

Choose the candidate family

    ν(dμ)=ell^s μ^(s−1)e^(−ell μ)dμ/Γ(s),  s>0, ell>0.

The normalized gamma integral gives exactly

    Y(r)=[ell/(ell+r)]^s,
    K_F(r)=Y(r)[1+s r/(ell+r)].

For r≫ell the additional force scales as r^(−2−s). An overall strength and
a fixed matter-coupling vector complete the linear model. The same s and ell
also fix the correlation spectrum below. No separate frequency exponent is
introduced to match a coherence observation. The exponential in mass μ is
not a momentum ultraviolet regulator; apparatus smearing/switching remains
necessary for pointlike correlation observables.

## Fixed two-position source: exact reduced coherence

The benchmark prepares an equal-charge superposition at two stationary
positions x₁,x₂ separated by d. Each has Gaussian spatial form factor
f̃_a(k)=exp(−a²k²/2), with a>0, and the coupling is present for 0<t<T.
Preparation, trapping and recombination are external operations, explicitly
supplied. This is not a Talbot–Lau trajectory or a model of all interferometers.

For each oscillator, the conditional field evolution displaces the vacuum.
The displacement difference is

    Δα_(μ,k)=−ig f̃_a(k)(e^(−ik·x₁)−e^(−ik·x₂))
                 [∫₀ᵀe^(iωt)dt]/√[(2π)³2ω].

The magnitude of the conditional vacuum overlap is exp(−||Δα||²/2).
Angular integration and |∫₀ᵀe^(iωt)dt|²=4sin²(ωT/2)/ω² give

    |ρ₁₂(T)/ρ₁₂(0)|=exp[−D(T)],
    D(T)=g²/π² ∫ν(dμ)∫₀∞dk k² e^(−a²k²)
          [1−sinc(kd)] sin²(ωμ(k)T/2)/ωμ(k)³.             (1)

This channel is completely positive because it is the partial trace of the
specified unitary source–field evolution. Formula (1) is not an independent
classical random-force ansatz. The same g_Ag_B and ν already occur in V_AB.

For every μ≥0, T≥0 and any normalized positive ν, ωμ(k)≥k and
0≤1−sinc(x)≤min(x²/6,2). Consequently

    0≤D(T)≤(g²/π²) B(d/a),
    B(z)=[1−exp(−12/z²)]/(12/z²)+E₁(12/z²), z>0,
    B(0)=0.                                                (2)

To obtain (2), split the dominating integral at k=√12/d, use x²/6 on the
first interval and 2 on the second, then integrate e^(−a²k²)k and
e^(−a²k²)/k. The simpler bound B(z)≤z²/12 also follows directly. The bound
requires finite a; taking a→0 at fixed d is not covered. At d=0 the two
conditional currents coincide and D=0 exactly. The results also cover g=0,
T=0, a massless atom in ν and arbitrary finite mixtures.

The integrable bound above permits dominated convergence over μ. For each
μ, transform the cosine term in sin²=(1−cos)/2 to frequency and apply the
Riemann–Lebesgue lemma to its integrable density. This yields

    D(∞)=g²/(2π²) ∫ν(dμ)∫₀∞dk k² e^(−a²k²)
                   [1−sinc(kd)]/ωμ(k)³.                  (3)

Equation (3) describes finite switching/field-distinguishability loss for this
fixed hold. It is not a zero-decoherence claim. Source motion, thermal
occupations, repeated switching and different preparation are distinct tests.

## A cross-domain exponent fixed by the same measure

For a spatially smeared local field, define its positive-frequency density
by W_a(t)=∫₀∞j_a(ω)e^(−iωt)dω. Direct integration over momentum gives

    j_a(ω)=1/(4π²) ∫₀^ω ν(dμ)√(ω²−μ²)
                         exp[−a²(ω²−μ²)].

For the spatial difference Φ_a(x₁)−Φ_a(x₂), multiply the mass integrand
by 2[1−sinc(d√(ω²−μ²))]. Substituting μ=ωu proves, at fixed s>0,
ωell,ωa,ωd→0,

    j_a(ω) = ell^s B(s/2,3/2) ω^(s+1)/(8π²Γ(s))
                ×[1+O(ωell+(ωa)²)],
    j_diff(ω) = ell^s d² B(s/2,5/2) ω^(s+3)/(24π²Γ(s))
                ×[1+O(ωell+(ωa)²+(ωd)²)].               (4)

The remainder follows uniformly on 0≤u≤1 from the exponential and sinc
Taylor bounds; fixed positive s makes the beta integrals finite. Thus the
same supplied s controls the far-field static force power 2+s, local vacuum
noise power 1+s and spatial-difference noise power 3+s. These powers apply
in different declared asymptotic windows, not at arbitrary measured scales.
They provide falsifiable relations for a common mediator if the apparatus
and state assumptions can be established.

For a clock with two internal charges q₁,q₂ at the same location, replace
the spatial-difference spectrum by (q₁−q₂)²j_a. The exact Ramsey envelope is

    D_clock(T)=2(q₁−q₂)²∫₀∞j_a(ω)sin²(ωT/2)/ω² dω.

For this gamma continuum with s>0 and a>0, its large-T limit is finite,
since j_a/ω²∼ω^(s−1) at zero and the smeared/mass-cutoff ultraviolet
integral converges. For a strictly massless field the local exponent instead
has logarithmic growth. A moving neutrino samples a worldline spectrum;
its response cannot be obtained by substituting a neutrino charge into the
stationary-clock density without deriving the trajectory map.

## Finite-field completion and remaining obligations

A finite positive atomic ν=Σ_j w_j δ(μ−μ_j) has an explicit local canonical
multi-scalar action with Φ=Σ_j√w_j φ_j. Coupling these finitely many fields
to an Einstein metric and declared matter operators gives an ordinary
effective-field-theory candidate below its supplied cutoff. All formulas
above specialize directly, except the continuum infrared powers in (4).

The continuum Gaussian field itself is a valid linear response/correlation
construction. Its fully dynamical covariant stress tensor, gravitational
backreaction, renormalization and interacting continuum completion need a
separate analysis; an integral of free responses is not that proof. Finite
spectral approximations must be tested jointly for force and coherence: a
lowest discrete mass changes the very-low-frequency noise even when a finite
static-distance window is approximated accurately.

The first numerical probe has 40 passing checks and zero failures: direct
mass quadrature for static kernels; phase-space low-frequency coefficients;
finite-time positivity/bounds, long-hold approach and zero separation. These
are numerical challenges to an analytic construction, not a substitute for
its proof. A separate source-normalization and coherent-state derivation is
in progress. No comparison to observed fringe visibility is claimed yet.
