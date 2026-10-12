---
claim_id: spatial_wilson_observation_map_and_mass_matching_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
runner: scripts/spatial_wilson_observation_map_2026_10_12.py
upstream_dependencies: []
claim_scope: "Conditional free spectra, weak-field magnetic response, leading tree emission, one-loop additive mass and finite local kinetic matching for one explicitly supplied spatial Wilson U(1) law; no empirical exclusion or physical pole identification."
---

# An observation map and radiative matching for a supplied spatial Wilson law

Status: proposed_retained

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit mathematical and perturbative consequences of a supplied Hamiltonian; the physical inference and full interacting matching remain open."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "Carry one-loop mass and local kinetic matching into a physical spectral/Pauli and measurement prescription before an observational likelihood; compare a protecting mechanism against the simpler relativistic null."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Target and supplied model

The target is a single candidate's forward map across photon propagation,
charged-particle radiation and magnetic resonance. The Wilson modification
removes the extra light free Dirac cones and changes both the kinematics and
the spin response. Its interaction also changes the bare-to-measured mass
map. These are restrictions on this candidate, not a reconstruction of a
unique microscopic law from the observations.

Use continuous Hamiltonian time and dimensionless spatial momenta on
\(\mathbb T^3=(-\pi,\pi]^3\). Supply four-component canonical fermions,
Dirac matrices \(\alpha_i,\beta_D\), and

\[
 h(p)=a\alpha\cdot\sin p+\beta_D[\mu+wW(p)],\quad
 W(p)=\sum_i(1-\cos p_i),\quad
 \omega(k)=2\|\sin(k/2)\|.                                      \tag{1}
\]

The finite choices were frozen before this route's numerical searches:
\(w=1,a^2=1-\mu,0<\mu<1\) is the primary tree model;
\(w=1,a=1\) is an unretuned comparator; \(w=0\) names the earlier
doubling comparator. No Wilson coefficient is fitted. The primary choice
makes the coefficient of \(p^2\) in the free squared electron energy equal
to the photon's. This matching is a supplied choice, not a protecting
symmetry or a consequence of an observed mass.

Gauge both spatial hopping terms with the same literal unitary link
\(U_{x,i}=\exp(ieA_{x,i})\). Supply the usual filled negative band,
positive-band particle interpretation, canonical transverse photon energy
\(H_\gamma=\frac12\sum(\Pi^2+\omega^2A^2)\), \([A,\Pi]=i\), and
mode coefficient \(1/\sqrt{2\omega V}\). Also supply the Born transition
rule and infinite-volume, long-time golden rule for the tree rate. For
virtual processes below, specify the noncompact Maxwell electric/curl
action and the usual U(1) Gauss constraint, including its Coulomb sector.
The Euclidean-time continuation is part of that conditional quantum model.
There is no independent Pauli/clover term or normal-order replacement of
the literal link exponential.

Physical energy units are \(\Lambda\), length units \(\hbar c/\Lambda\).
The unknown completion scale \(\Lambda\) is not a refit of the framework's
approved scale-reference primitive. A physical identification of those
scales would be an additional specialization. The approved scale ruler,
kinetic-isotropy premise and realized-state slot were checked at revision
`a13caa4885f547c8d206265b031ba7649e539fd9`; none is reclassified as missing.
They do not supply this Hamiltonian, its species, vacuum, quantum response
or detector interpretation. In particular this four-component Wilson
carrier is not identified with a retained blocked staggered carrier.

## Exact free pair stability and light-species count

Write \(X_i=1-\cos p_i\). In the primary setting the positive energy obeys

\[
 E_\mu(p)^2=\mu^2+2W+2\sum_{i<j}X_iX_j+\mu\sum_iX_i^2
           \geq\mu^2+\omega(p)^2.                              \tag{2}
\]

The cancellation of the quadratic mass correction in (2) uses
\(a^2=1-\mu\). The unretuned setting instead has
\(E^2-\mu^2-\omega^2=2\mu W+2\sum_{i<j}X_iX_j\geq0\).

For completeness, the complex chord vector
\(z_i(p)=e^{ip_i}-1\) has norm \(\omega(p)\), and
\(z(p+q)=z(p)+\operatorname{diag}(e^{ip_i})z(q)\). Thus
\(\omega(p+q)\leq\omega(p)+\omega(q)\). Apply the ordinary triangle
inequality in two dimensions to \((\mu,\omega(p))\) and
\((\mu,\omega(q))\). Equation (2) gives the full-torus result

\[
 E_\mu(p)+E_\mu(k-p)\geq\sqrt{4\mu^2+\omega(k)^2}>\omega(k).
                                                                    \tag{3}
\]

No free photon-to-pair opening exists in this family. This is a spectral
inequality; it does not prove stability in every interacting completion.
At a corner with \(j\) components equal to \(\pi\), the free gap is
\(|\mu+2wj|\), with multiplicity \(\binom3j\). At \(\mu=0,w=1\)
only the central corner is gapless, whereas \(w=0\) has eight cones.
One free Dirac cone is not a derivation of the Standard Model's chiral
matter content.

## Weak-field spin and cyclotron frequencies

This calculation takes an infinite-volume uniform field first, then
\(B\to0\) at fixed positive \(\mu\), fixed Landau level and longitudinal
momentum zero. With \(\Pi=-i\nabla-qA\) and
\([\Pi_x,\Pi_y]=iqB\), the continuum quadratic part of (1) is

\[
 H_2=\beta_D(\mu+w\Pi^2/2)+a\alpha\cdot\Pi.
\]

Since \((\alpha\cdot\Pi)^2=\Pi^2-q\Sigma\cdot B\), projection onto
the positive band to first order in \(B\) gives

\[
 H_+=\mu+\frac{a^2+\mu w}{2\mu}\Pi^2
           -\frac{a^2q}{2\mu}\Sigma\cdot B+O(B^2).
\]

Consequently the operational frequency ratio, not a rest-mass-normalized
magnetic moment with a different mass convention, is

\[
 \frac{g_{\rm op}}2=\frac{\Omega_s}{\Omega_c}
   =\frac{a^2}{a^2+\mu w},\quad
 \Omega_s=|qB|\frac{a^2}{\mu},\quad
 \Omega_c=|qB|\left(\frac{a^2}{\mu}+w\right).                 \tag{4}
\]

The primary value is \(1-\mu\); the unretuned value is
\(1/(1+\mu)\). For general \(w\), matching the quadratic speed would
require \(a^2=1-\mu w\), not \(1-\mu\). General \(w\) is only an
algebraic convention check here, not a fitted family.

An independent Landau-block check, for \(qB>0\), gives

\[
 E_n^\pm=\pm wqB/2+
       \sqrt{(\mu+wqBn)^2+2a^2qBn},
\]

with the unpaired \(n=0\) state \(\mu+wqB/2\) and the minus branch
starting at \(n=1\). These are exact eigenvalues of \(H_2\), not of the
full finite-field lattice hopping. Direct open-boundary lattice spectra
converge to (4) as the field decreases; their initialization, extents and
residuals are recorded with the checks. They are synthetic controls.

## Electron radiation: exact axis exception and global leading boundary

A Cherenkov opening means that some nonzero torus photon satisfies
\(E_\mu(p)>E_\mu(p-k)+\omega(k)\). For an axial incident momentum
\(p=(P,0,0)\), dropping the transverse components lowers both final
energies by (2). On that axis set

\[
 d_{\rm ax}(t)=(\sqrt{1-\mu}\sin t,\ \mu+1-\cos t).
\]

Then

\[
 \|d_{\rm ax}(P)-d_{\rm ax}(Q)\|^2
 =4\sin^2[(P-Q)/2]\{1-\mu\cos^2[(P+Q)/2]\}
 \leq4\sin^2[(P-Q)/2].                                      \tag{5}
\]

Reverse triangle proves no axial opening anywhere on the torus for
\(0<\mu<1\). Equality at exceptional momenta is not positive phase
space or a nonzero rate.

For nonaxis directions fix \(p=rn\), \(|n|=1\),
\(A=\sum_i n_i^4<1\), and \(\mu=br^2\) with fixed \(b>0\).
The exact dispersion expands as

\[
 E_\mu(p)^2=\mu^2+|p|^2+|p|^4/4-\sum_i p_i^4/3
                +O(|p|^6+\mu|p|^4).
\]

For \(q=yrn+r^2t\), \(t\cdot n=0\), \(0<y<1\), define

\[
 F_A(y)=\frac y4[(1-A)+(1-2A)y+(1-A)y^2],\qquad
 M_A=\max_{0\leq y\leq1}F_A(y).
\]

The leading energy excess is

\[
 \frac{E_\mu(p)-E_\mu(q)-\omega(p-q)}{r^3}
 =\frac{1-y}{2y}[F_A(y)-b^2]
   -\frac{|t|^2}{2y(1-y)}+o(1).                              \tag{6}
\]

This also controls the full-torus leading boundary. An opening forces
\(\omega(k)=O(r)\), hence \(k,q=O(r)\) because the photon has a unique
torus zero. Chord triangle and (2) give
\(\mu^2/[E(q)+\omega(q)]\leq E(q)-\omega(q)
 <E(p)-\omega(p)=O(r^3)\), so \(|q|\geq c r\) for fixed \(b>0\).
The leading triangle defect is \(O(r^3)\), forcing the transverse scale
in (6) for finite fractions. Its contribution is nonpositive. At the soft
endpoint, differentiation at fixed \(\mu\), before substitution, gives

\[
 |\nabla E_\mu(rn)|=1+\frac{r^2}2[F_A(1)-b^2]+O(r^4).
\]

For \(b^2>M_A\) its strict negative velocity margin excludes every
sequence \(|k|/r\to0\), while \(\omega(k)/|k|=1-o(r^2)\).
Compactness excludes the remaining fractions. For \(b^2<M_A\), a fixed
interior fraction with positive (6) supplies an opening for sufficiently
small \(r\). These are fixed-margin asymptotic statements, not an exact
finite-mass threshold or a unique finite-mass optimizer.

Put \(A_c=(8-2\sqrt2)/7\). Direct cubic maximization yields

\[
 \begin{array}{ll}
 A<A_c:& y_c=1,\quad M_A=(3-4A)/4,\\
 A_c<A<1:&
 y_c=\dfrac{1-A}{2A-1+\sqrt{A^2+2A-2}},\quad M_A=F_A(y_c).
 \end{array}                                                \tag{7}
\]

One verification factors \(4[F_A(y)-F_A(1)]\) as
\((y-1)[(1-A)y^2+(2-3A)y+(3-4A)]\), then compares the endpoint with
the smaller stationary root. At \(A_c\), \(y=1\) and
\(y=\sqrt2-1\) tie; higher terms may split that tie at finite momentum.
At \(A=3/4\), the soft criterion vanishes but \(y_c=1/3\) gives
\(M_A=1/108>0\). A group-speed test alone would miss that hard channel.
As a fixed direction approaches an axis, \(M_A\sim(1-A)^2/16\).
The leading relation \(r_{\rm th}^4\sim\mu^2/M_A\) is not uniform
when the direction approaches an axis with the mass.

The soft/hard phenomenon and this leading cubic are known quartic
Lorentz-violation kinematics: [Jacobson, Liberati and Mattingly,
hep-ph/0209264v2](https://arxiv.org/abs/hep-ph/0209264v2), equations
(25)–(29), specialize with \(\eta=(3-4A)/12,\xi=-A/12\).
The exact axis inequality and the full-symbol localization above provide
the scope for this candidate. No generic-threshold priority is claimed.

## Canonical tree width and distinct onset limits

For \(p\to q=p-k\), use a consistent unwrapped representative of \(q\)
in the link midpoint. For a real polarization \(\epsilon\perp\hat k\),
\(\hat k_i=2\sin(k_i/2)\), the charge-stripped current is

\[
 J_\epsilon=a\sum_i\epsilon_i\alpha_i\cos[(p_i+q_i)/2]
       +\beta_D\sum_i\epsilon_i\sin[(p_i+q_i)/2].
\]

Its exact Ward difference is \(\sum_i\hat k_iJ_i=h(p)-h(q)\).
Let \(d_p=(a\sin p,\mu+W(p))\), \(n_p=d_p/E_p\),
\(P_p=(1+n_p\cdot\Gamma)/2\), and \(J_\epsilon=v\cdot\Gamma\).
The unaveraged two-spin trace is

\[
 S_\epsilon=\operatorname{tr}(P_qJ_\epsilon P_pJ_\epsilon)
   =|v|^2(1-n_p\cdot n_q)+2(n_p\cdot v)(n_q\cdot v)\geq0.
\]

Nonnegativity follows from the squared matrix norm; the displayed terms
need not be separately nonnegative. Initial-spin averaging is already
included in the following prefactor, while final photon polarizations are
summed:

\[
 \Gamma(p)=\frac\alpha{4\pi}\sum_\epsilon\int_{\mathbb T^3}
    \frac{S_\epsilon}{\omega(k)}
    \delta_D(E_p-E_{p-k}-\omega_k)\,d^3k,
 \qquad\alpha=e^2/(4\pi).                                    \tag{8}
\]

Indeed a box amplitude is \(e u_q^\dagger J u_p/\sqrt{2\omega V}\).
Golden rule, the density \(V/(2\pi)^3\), and the initial factor \(1/2\)
give (8). There is no extra relativistic \(1/(2E)\) factor for these
unit-normalized band spinors and no eight-cone multiplicity.

For the limit in (6), restrict to fixed \(n,b\) with \(b^2<M_A\),
\(b^2\ne F_A(1)\), and no multiple interior zero of \(F_A-b^2\).
Then

\[
 \Gamma(rn)=\alpha r^3 K(A,b)+o(r^3),\qquad
 K=\int_{F_A>b^2}G(y)\,dy,\quad
 G=\frac{(1+y^2)(F_A-b^2)+(1-y)^2(b-y/2)^2}{2y}.             \tag{9}
\]

Strict opening implies \(K>0\). The Wilson contribution to the band
mass, \(M_p/E_p=r(b+1/2)+O(r^3)\), is essential for \(b-y/2\).
The Wilson part of the transverse current itself enters at higher order
in this limit, although it remains essential to the exact Ward identity.
The measure is \(r^5dy\,d^2t\), the energy delta contributes \(r^{-3}\),
and the transverse coarea integral is \(2\pi y(1-y)\). These factors
derive the coefficient; they are not a numerical fit.

Here is the endpoint control needed for (9). For \(k=\lambda u\),
\(\lambda<\varepsilon r\), \(\varepsilon<1/2\), the electron gradient
on its segment is \(q/|q|+O(r^2)\). The projection of the leading
unit vector \((p-su)/|p-su|\) on \(u\) decreases with \(s\);
no monotonicity of the exact electron gradient is required. Therefore
\(E(p)-E(p-\lambda u)\leq\lambda(n\cdot u+Cr^2)\).
On the shell, \(\omega(\lambda u)/\lambda=1+O(\lambda^2)\) then
forces \(n\cdot u\geq1-C'r^2\). Write
\(x=\lambda/r\), \(u=\sqrt{1-r^2|z|^2}n+rz\), \(z\perp n\).
Uniformly for bounded \(z\), down to \(x=0\),

\[
 \frac{E(rn)-E(r(n-xu))-\omega(rxu)}{r^3x}
 =\frac{F_A(1-x)-b^2-|z|^2}{2(1-x)}+O_{C_z^2}(r).           \tag{10}
\]

To justify the removable quotients, \(\mathcal E(r,v)=E_{br^2}(rv)/r\)
is smooth for \(|v|\geq1-\varepsilon\), by the elementary sine/cosine
Taylor expressions. The fundamental theorem of calculus removes the
quotient in \(x\). The remaining bracket and its first derivative in
\(r\) vanish at zero, so two integrations in \(r\) remove \(r^2\),
including two \(z\) derivatives. This proves the stated uniform remainder.
For the nonzero endpoint margin, (10) either excludes the soft shell or
gives a uniformly concave transverse shell with bounded coarea. Its angular
delta integral is at most \(C/\lambda\). The exact spin trace is at most
\(Cr^2\), and \(\omega\geq c\lambda\); the omitted soft contribution is
at most \(C\varepsilon r^3\). The final-electron endpoint was already
excluded in (6). Simple longitudinal roots have bounded two-dimensional
transverse coarea. Taking \(r\to0\), then \(\varepsilon\to0\), proves
(9) in its stated domain.

At fixed nonzero \(p,\mu\), a separate local result is

\[
 \lim_{\kappa\downarrow0}\frac{d\Gamma}{d\kappa}
   =\alpha\frac{|\nabla E_p|^2-1}{|\nabla E_p|},
 \quad |\nabla E_p|>1,\quad\kappa=|k|.                       \tag{11}
\]

It follows from \(P(\partial_i h)P=(\partial_iE)P\) and the angular
coarea of \(\nabla E_p\cdot\hat k=1\). Equality of the speed to one
is excluded; (11) does not determine the full finite-photon spectrum.

Only after taking the limit (9), let \(\delta=M_A-b^2\downarrow0\).
For \(A<A_c\), \(F_A'(1)=2M_A\), so
\(K\sim\delta^2/(4M_A)\). The corresponding radiated power is
\(\mathcal P\sim\alpha r^4\delta^3/(24M_A^2)\).
For \(A_c<A<1\), put \(\kappa_c=-F_A''(y_c)>0\) and
\(b_c=\sqrt{M_A}\). Stationarity gives
\(b_c=(y_c/2)\sqrt{(1-y_c)/(1+3y_c)}<y_c/2\), hence

\[
 K\sim\frac{(1-y_c)^2(b_c-y_c/2)^2}{y_c}
             \sqrt{2\delta/\kappa_c}.                        \tag{12}
\]

The hard contribution dominates the leading crossover's sequential onset.
No interchange of onset and \(r\) limits, finite-momentum tie splitting,
or uniform near-axis estimate is claimed. Physical rates would multiply
\(\Gamma\) by \(\Lambda/\hbar\), and power by \(\Lambda^2/\hbar\).
No propagation or detector likelihood is computed here.

## Interaction-level mass matching

This subsection sets the bare expansion point to \(\mu=0,a=w=1\).
It is the common zero-mass limit of the two frozen tree settings, with the
explicit Gauss/Maxwell completion above. It does not substitute a measured
electron mass into a bare interacting action.

In Euclidean conventions,
\(D(p)=i\gamma_0p_0+i\gamma_i\sin p_i+W(p)\). Put
\(E^2=\sum_i\sin^2k_i+W^2\), \(\omega^2=2W\), and
\(K=(k_0,2\sin(k_i/2))\). The covariant photon propagator is
\(D^\gamma_{ab}=\delta_{ab}/K^2+(\xi-1)K_aK_b/(K^2)^2\).
The charge-stripped vertices at external zero, internal \(-k\), are
\(V_0=i\gamma_0\) and
\(V_i=i\gamma_i\cos(k_i/2)-\sin(k_i/2)I\).

Expansion of the averaged inverse gives the inverse-propagator correction
\(e^2\langle T\rangle-e^2\langle V S V\rangle\), where the spatial
link seagull is \(\frac12\sum_iD^\gamma_{ii}\,I\). Thus its scalar
coefficient has a definite sign convention. In Feynman gauge the exchange
numerator is \(W(1+\sum_i\cos k_i)-\sum_i\sin^2k_i=4W-E^2\).
Continuous frequency integration yields

\[
 \delta m=e^2 C_W+O(e^4),\qquad
 C_W=\int_{\mathbb T^3}\frac{d^3k}{(2\pi)^3}
 \left[\frac3{4\omega}+\frac{4W-E^2}{2E\omega(E+\omega)}\right]
 =\int\frac{d^3k}{(2\pi)^3}
       \frac{E^2+3E\omega+8W}{4E\omega(E+\omega)}>0.           \tag{13}
\]

The integrand is \(1/|k|+O(1)\) at the origin and regular elsewhere;
the integral is finite. The positivity proves the one-loop sign, without
a numerical search. It does not establish an exact nonperturbative mass.
Numerical evaluation gives \(C_W=0.37434747251955\); the integral, not
the printed precision, is the defining result.

Gauge cancellation is pointwise. The Ward identity gives
\(\sum_aK_aV_a=-D(-k)\). The longitudinal exchange scalar is
\(-(\xi-1)W/(K^2)^2\); the seagull is
\((\xi-1)\omega^2/[2(K^2)^2]\). They cancel since \(\omega^2=2W\).
The remaining vector integrates to zero by oddness. A separate Coulomb
calculation gives seagull, instantaneous and transverse contributions
\(0.227672025822215\), \(0.090165777695639\), and
\(0.056509669001696\), respectively, with the same sum. The Feynman
split is \(0.341508038733323+0.032839433786227\). Individual diagrams
are not gauge independent. At \(w=0,\mu=0\) every scalar exchange trace
and scalar seagull vanish; the extra cones still remain.

The formal perturbative critical bare mass is
\(\mu_c=-e^2C_W+O(e^4)\). A calibrated light mass is measured relative
to that surface, with further matching corrections. Therefore the literal
tree assignment \(\mu=m_e/\Lambda\) is not automatically the interacting
bare parameter. This does not create a second independent mass datum: the
same mass calibration can fix the subtraction in a specified model. Nor is
it a quantitative naturalness probability or a universal impossibility
theorem. A tuned, symmetry-protected or otherwise matched model remains a
live possibility.

Additive Wilson mass renormalization is prior art.
[Hashimoto and Okamoto, hep-lat/0302012v1](https://arxiv.org/abs/hep-lat/0302012v1)
give Hamiltonian-limit mass subtraction and general vertices in section IV
and appendix A. Their conventional \(r_s=1\) SW limit becomes naive;
the fixed spatial Wilson term here corresponds to \(r_s/\xi=1\), with
no improvement terms. Their numerical table is not imported as this
coefficient. [Angelides et al., 2211.12169v3](https://arxiv.org/abs/2211.12169v3)
study a different, 1+1-dimensional Hamiltonian and support the distinction
between bare and renormalized mass, not a numerical identification here.

## Observation roles and the remaining inference

At tree level only, use \(\mu=m_e/\Lambda\) as an explicit calibration.
For the same photon, put \(v_i=\sin^2(k_i/2)\), \(S=\sum v_i\).
Differentiation gives \(|\nabla\omega|^2=1-\sum v_i^2/S\), so along
fixed direction \(n\),
\(1-v_\gamma/c=A E_\gamma^2/(8\Lambda^2)+O(E_\gamma^4/\Lambda^4)\).
Matching the conventional quadratic time-delay parameter gives
\(E_{\rm QG,2}=\sqrt{12}\Lambda/\sqrt A\). This conversion is repeated
context, not a new timing result. Eliminating \(\Lambda\) in (4) gives

\[
 |\delta(g/2)_{\rm tree}|=\frac{\sqrt{12}m_e}
   {\sqrt A\,E_{\rm QG,2}}\leq\frac{6m_e}{E_{\rm QG,2}}.      \tag{14}
\]

The pinned subluminal LHAASO value \(6.9\times10^{11}\) GeV and CODATA
rest energy \(0.00051099895069\) GeV make the right side
\(4.4434691\times10^{-15}\), or \(0.03418\) times Fan et al.'s
\(1.3\times10^{-13}\) standard uncertainty. This is a conditional tree
parameter comparison, not an interacting confidence bound or a fit of the
measured anomaly. Equation (13) makes the missing mass matching concrete;
the physical relative-speed prescription, Pauli coefficients and measurement
response also need matching before (14) has an interacting interpretation.

| Datum/source | Role here | Extraction and uncertainty boundary |
|---|---|---|
| NIST current 2022 CODATA electron rest energy and alpha | Calibration/comparator units | Joint adjusted parameters; alpha is not independent of magnetic-moment theory/data |
| [LHAASO 2402.06009v3](https://arxiv.org/abs/2402.06009v3), table 1, ML MINOS subluminal quadratic column | Conditional timing comparator | Same \(6.9\times10^{11}\) GeV limit as v2; cosmology, afterglow, EBL and detector assumptions remain; no reproduced likelihood |
| [Fan et al. 2209.13084v2](https://arxiv.org/abs/2209.13084v2), equations (3)–(6) | Magnetic-frequency comparator | \(g/2=1.00115965218059(13)\), after trap/cavity corrections; no unjustified combination with older measurements |
| [Parker et al. 1812.04130v1](https://arxiv.org/abs/1812.04130v1) | Separate recoil comparator | \(\alpha^{-1}=137.035999046(27)\); atomic/recoil, mass and Rydberg extraction, not a direct microscopic-charge measurement |
| [Morel et al. Nature 2020](https://doi.org/10.1038/s41586-020-2964-7) and same-collaboration Moriond/HAL03443551v1 | Separate conflicting recoil comparator | \(\alpha^{-1}=137.035999206(11)\); full Nature article was not obtained, only its publisher preview plus the proceedings' extraction equation and systematics |
| [H.E.S.S. 2411.08189v1](https://arxiv.org/abs/2411.08189v1) | Rejected survival shortcut | 40 TeV is an electron-like candidate endpoint; dominant hadron background above 3 TeV is not excluded, so no 40 TeV electron-survival bound is inferred |

The current PDG 2026 electron listing distinguishes its average from Fan's
single result and notes the independent-alpha tension. No covariance needed
for a new average is available here. Alpha inferred from Fan's same
magnetic result, including the published Volkov QED comparator, is not a
second datum. The revised Aoyama Set V contribution is a subset, not the
total tenth-order coefficient. Neither value is used to construct an
unperformed Standard Model residual fit.

All public data were known during model choice; there is no blind held-out
validation. No raw-event, joint-covariance or detector fit is performed.
The relativistic null remains the simpler empirical baseline because no
improved likelihood has been demonstrated. The Wilson candidate replaces
one species-count problem with explicit matching work; the numerical
controls do not rank it as a unique TOE. AIC, BIC or a Bayes factor would
require an actual likelihood and a justified parameter/selection measure,
which are not supplied here.

## Finite local kinetic matching and the regulator prescription

This continuation uses the same quantum action, with \(a=w=1\) and a
positive **bare infrared regulator** \(m\). Take external Euclidean
momentum derivatives at zero at fixed \(m\), then \(m\downarrow0\),
at the formal coefficient of \(e^2\). This is neither the tree curve
\(a^2=1-\mu\) at positive mass nor an on-shell mass prescription.
Write the fermion linear coefficients as \(Z_t=1+e^2z_t\) and
\(Z_s=1+e^2z_s\), and the photon electric/magnetic quadratic action
coefficients as \(Z_E=1+e^2z_E\), \(Z_B=1+e^2z_B\), to this order.
The gauge-fixing term is excluded from \(Z_E,Z_B\).

Put \(s_i=\sin k_i,c_i=\cos k_i,M=m+W\),
\(E^2=\sum s_i^2+M^2\), \(\omega^2=2W\), and let an overbar
denote a spatial average. Define

\[
 I_1=\frac1{2E\omega(E+\omega)},\quad
 I_2=\frac{2E+\omega}{4E^3\omega(E+\omega)^2},\quad
 A_i=1-2c_i^2+3c_i-2Mc_i,\quad
 B_i=2s_i^2(M-3+c_i)(M+c_i).
\]

These are the continuous-frequency integrals of
\([(\nu^2+E^2)(\nu^2+\omega^2)]^{-1}\) and its extra
\((\nu^2+E^2)^{-1}\) factor. The latter also follows by
\(-\partial_E I_1/(2E)\). Differentiating the complete inverse
propagator, including both midpoint vertices and the literal-link contact,
gives in Feynman gauge

\[
 z_t=\int_{BZ}\frac{d^3k}{(2\pi)^3}[-2I_1+4E^2I_2],\qquad
 z_s=\int_{BZ}\frac{d^3k}{(2\pi)^3}
     [\overline A I_1+\overline B I_2-1/(4\omega)].          \tag{15}
\]

For example, before frequency integration the spatial exchange coefficient
along \(i\gamma_j\), at general external \(p\), has numerator
\([3-\cos(2p_j-k_j)]\sin(p_j-k_j)
-M(p-k)\sin(2p_j-k_j)\), divided by
\((p_0-\nu)^2+E(p-k)^2\) and the photon denominator.
Its derivative supplies \(A_j/R+B_j/R^2\); the contact supplies
\(-1/(2K^2)\). This proves (15) and fixes its normalization.

For the photon let \(d=(s_1,s_2,s_3,M)\),
\(v_i=\partial_iE=s_i(c_i+M)/E\) and \(h_{ij}=s_is_j\).
The band current vector \(d_i'=\partial_i d\) has unit norm and
interband trace \(2(1-v_i^2)\). Frequency integration of its response,
and periodic integration by parts for a static transverse photon, give

\[
 z_E=\int_{BZ}\frac{d^3k}{(2\pi)^3}
      \frac{1-\overline{v_i^2}}{2E^3},\qquad
 z_B=\int_{BZ}\frac{d^3k}{(2\pi)^3}
      \frac{\overline{1-2h_{ij}^2+6h_{ij}v_iv_j-5v_i^2v_j^2}}
           {2E^3}.                                         \tag{16}
\]

The second average is over the six ordered \(i\ne j\) pairs. To verify
the derivative and integration-by-parts step directly, write
\(n=d/E,u=n\cdot d_j'=v_j\), with primes now denoting
\(\partial_i\), \(i\ne j\). The unintegrated static coefficient is
\([|n'|^2+u(n''\cdot d_j')-(n'\cdot d_j')^2]/(2E)
 +(1-u^2)E''/(4E^2)\). Integrating its second-derivative terms by
parts on the periodic torus gives (16). Equivalently the bubble trace is
\(-\tfrac12\int d\nu/(2\pi)\operatorname{tr}
(G h_iG h_jG h_iG h_j)\), with \(G=(i\nu+h)^{-1}\) and
\(h_i=\partial_i h\). Expansion in four Clifford matrices and the
elementary frequency moments gives the same expression. The electric
response is \(2(1-v_i^2)\Omega^2/[E(\Omega^2+4E^2)]\).
The contact cancels the constant photon term: the combined zero-momentum
integrand integrates to \(-2\int\partial_i^2E=0\).
It has no external transverse-momentum or frequency derivative, but must
remain in the parent response for this Ward consistency.

Let \(f_F(k,m)\) and \(f_P(k,m)\) be the differences of the spatial
integrands in (15) and (16). Their regulator limits require care. With
\(\rho=|k|\), \(E_c=\sqrt{\rho^2+m^2}\), the angular-averaged
continuum fermion difference is
\(m^2(3E_c+\rho)/[3E_c^3(E_c+\rho)^3]\). It vanishes pointwise
at \(m=0,\rho>0\), but its full radial integral is
\(1/(24\pi^2)\). The substitution \(v=\rho/E_c\) reduces the
dimensionless radial integral to
\(\frac13\int_0^1 v^2(3+v)/(1+v)^3\,dv=1/12\), with angular
factor \(1/(2\pi^2)\).

At exactly zero mass the photon difference has leading density
\(H(n)/\rho^3\), where \(H(n)=(5\sum_i n_i^4-3)/12\).
Its spherical mean vanishes, but its absolute integral diverges. The
finite-mass continuum expression is
\(H(n)\rho^4/E_c^7+m^2\rho^2/(6E_c^7)\). The second term has
full radial integral \(1/(60\pi^2)\). Thus the precise limits are

\[
 \Delta_f:=\lim_{m\downarrow0}(z_s-z_t)
   =\int_{BZ}\frac{d^3k}{(2\pi)^3}f_F(k,0)+\frac1{24\pi^2},
 \qquad
 \Delta_\gamma:=\lim_{m\downarrow0}(z_B-z_E)
   =\operatorname{FP}_{\rm spherical}\int_{BZ}
       \frac{d^3k}{(2\pi)^3}f_P(k,0)+\frac1{60\pi^2}.       \tag{17}
\]

The first massless integral is absolutely convergent. The second removes
a spherical small ball. For an explicit reproducible subtraction, use
\(k=(t,tu,tv)\), \(0<t<\pi,0<u,v<1\), multiply the octant-sector
integral by \(3/\pi^3\), and put
\(R=\sqrt{1+u^2+v^2},h=H((1,u,v)/R)/R^3\). The finite part is
the integral of \(t^2 f_P(t,tu,tv,0)-h/t\), plus the angular term
\(h\log R\). This term follows from the spherical lower boundary
\(t=\varepsilon/R\); the integrated \(h\) itself is zero.
Dropping it or either constant in (17) changes the limiting prescription.

A uniform justification is available before frequency integration.
Subtract the same continuum derivative kernels multiplied by a smooth
O(4)-radial function supported inside a small four-ball and equal to one
near zero. For \(R_m=\sqrt{\nu^2+|k|^2+m^2}\), propagators have
norm at most \(C/R_m\); the Wilson resolvent difference is bounded by
\(C|k|^2/R_m^2\). Dirac/vertex first-derivative corrections are
\(O(|k|)\), and the photon squared-denominator correction is
\(O(|k|^4)\). Each subtracted fermion first derivative and photon
second derivative is therefore bounded by
\(C(\nu^2+|k|^2)^{-3/2}\) or better, uniformly as \(m\downarrow0\).
For example, the fermion terms are bounded by
\((|k|/R_m^2+|k|^2/R_m^3)/(\nu^2+|k|^2)\) and
\(1/[R_m(\nu^2+|k|^2)]\). The photon derivative has four
propagator powers before one is replaced by its resolvent difference;
vertex-derivative terms are no more singular. These bounds are integrable
in four dimensions. Outside that ball the Wilson carrier is gapped and
the continuous-frequency tails converge. Dominated convergence applies
to the subtracted remainders, while the continuum pieces give exactly
the boundary terms in (17).

Numerically,

\[
 \Delta_f=-0.1327763348\ldots,\qquad
 \Delta_\gamma=+0.0118573122\ldots,\qquad
 \Delta_f-\Delta_\gamma/2=-0.1387049909\ldots.                \tag{18}
\]

The massless integrals before the additions in (17) are
\(-0.13699805078154\) and \(+0.01016862579586\).
Independent full-torus cubatures and direct positive-mass limits agree;
the digits are convergence estimates, not interval certificates.
The constants added in (17) are infrared **conversion terms**, distinct
from the link contacts already included in (15)–(16).

The fermion difference in (18) is independent of fixed finite covariant
gauge parameter. The exact Ward contraction reduces its longitudinal
variation to
\((\xi-1)[D(p)I_0-D(p)J(p)D(p)]\), where
\(I_0=\int (K^2)^{-2}\) and
\(J(p)=\int S(p-k)(K^2)^{-2}\), with the same infrared regulator.
These pieces are not separately claimed finite. Outside an infrared ball,
at zero mass the second term starts quadratically in external momentum;
the first is a common multiple of \(i\gamma_\mu p_\mu\).
Within the ball the common continuum subtraction is O(4) covariant, and
the integrable remainder bound above applies. Equivalently the leading
mass-scaled longitudinal difference is
\(2m^2(\nu^2-|k|^2/3)/[(\nu^2+|k|^2)^2
(\nu^2+|k|^2+m^2)^2]\), whose absolutely convergent four-dimensional
integral vanishes by angular symmetry; lattice corrections vanish in
that limit. The photon loop has no internal gauge propagator at this order.
This statement does not make every finite-mass off-shell coefficient
gauge independent.

Because a common O(4)-invariant infrared subtraction has zero coefficient
differences, (18) also defines the finite anisotropic **local** kinetic
matching in that prescription. It is unchanged by finite Lorentz-invariant
renormalizations; a deliberately added anisotropic finite counterterm
changes the supplied model or matching condition. The last combination
in (18) algebraically compares the normalized local fermion coefficient
with the photon square-root coefficient. It is not yet a physical
pole-speed theorem. Critical-mass tuning, the specified bare-speed choice,
nonlocal infrared logarithms, a charged-state/pole prescription and the
propagation measurement bridge remain necessary. If one preserves the
earlier tree curve \(a^2=1-\mu_{\rm bare}\) through
\(\mu_c=-e^2C_W\), it also adds \(+e^2C_W/2\) to the bare speed
at this order; (18) itself is for \(a=1\). No speed exclusion or
unmatched magnetic anomaly is inferred by silently mixing these settings.

## Verification and claim boundary

The paired runner and its observation/source record provide finite controls
of the exact identities, separately implemented band/field calculations,
the asymptotic rate, the loop integrals and regulator limits, and the unit conversion. Their live
results and execution provenance accompany this source. Analytic arguments
above carry the full-torus and limiting quantifiers; finite searches do not.
Focused checks were completed before extensive downstream use of each
critical step, with immutable pre-exposure derivations and comparison
manifests in the campaign runtime. Ordinary milestone review and formal
audit are distinct processes; no audit verdict is assigned by this note.

The magnetic check used a separately built finite-field Hamiltonian and
Landau blocks. The kinematic check supplied an independent full-torus
localization proof. The rate checker derived its normalization before
author exposure, differentiated a real-space link field, used explicit
eigenstates and a different soft-shell integration chart, and checked the
endpoint proof. The mass checker used instantaneous Coulomb plus transverse
exchange, independently of the author's covariant-gauge calculation.
The kinetic checker derived the original matrix derivatives, photon
bubble/contact cancellation, both infrared conversion terms and covariant
gauge limit before reading author radiative files. The author's final
limit-proof writeup followed receipt of the checker's early findings;
independence belongs to the preserved pre-exposure check, not to a claim
that both final expositions were written in isolation.
Shared supplied symbols and ordinary quantum rules limit that independence;
none of these checks is an observation of nature.

## No-Go Discipline Gate

This packet concerns the composite conditional statements above, including
free pair/axis closure and fixed-margin radiative boundaries. It does not
close the physical inverse problem. The proofs in this note are proposed
new evidence, not already audited retained authority. No route below is
marked `RULED OUT BY PRIOR`, and no procedural route count establishes
exhaustiveness among microscopic laws.

**N1 — Actual normalized attack routes.** The first six rows attack different
objects or terminal obligations in this note. Their failure to overturn the
specified result is justified by the displayed proof and corresponding live
runner controls, not by a claim of inherited retained authority.

| Family and marker | Concrete attempted attack | Result and exact evidence |
| --- | --- | --- |
| Global free spectral comparison — ATTEMPTED | A noncollinear torus partition or lifted corner could open pair decay despite a low-momentum comparison | The sum-of-nonnegative-terms identity and lifted chord inequality prove (3) on the whole torus; spectrum controls test random partitions and all corners |
| Magnetic oscillator and hopping spectrum — ATTEMPTED | The Wilson mass term might contribute equally to spin and orbital response, removing the operational deficit | Pauli reduction and the independently built Landau blocks in (4) separate the two frequencies; finite-field link spectra approach that limit. Finite-field corrections remain, so no exact finite-field ratio is claimed |
| Charged energy-shell variational problem — ATTEMPTED | Hard recoil, transverse motion, or a remote torus sector might defeat a soft-only Cherenkov boundary | Full-torus localization, transverse penalty and the cubic maximum in (6) include hard recoil; the exact vector contraction proves the axial exception (5). Hard recoil actually defeats the soft-only shortcut, which is rejected |
| Spin selection and canonical phase space — ATTEMPTED | An allowed energy shell might have a vanishing physical polarization matrix element or a wrong oscillator normalization | The exact Clifford trace, Ward identity and canonical coarea formula (7)-(10) yield positive K in the stated domain; independent real-space links and eigenstates check the current. These do not establish an interacting detector rate |
| Virtual scalar matching — ATTEMPTED | A longitudinal-gauge term or omitted seagull might cancel the scalar shift or change its sign | Equations (11)-(13) cancel the longitudinal pieces and give a strictly positive integral; an independent instantaneous Coulomb/transverse derivation agrees. The result is order e^2, not an all-coupling mass theorem |
| Regulated tensor matching — ATTEMPTED | Setting mass to zero early, changing cutoff shape, or dropping the photon contact might invalidate the finite anisotropy | Equations (14)-(18) retain both infrared conversion terms and the spherical finite part, with a uniform four-dimensional subtraction proof; original matrix derivatives, finite-positive-mass and static response controls agree. The massless-first shortcut gives different constants and is rejected |

Counterexamples to shortcuts are preserved rather than counted as failed
science. Alternative interacting phases, improvement operators, temporal
regulators and detector models remain live outside the frozen test action.

**N2 — Conditions and implication audit.** The Hamiltonian, canonical quantum
rules, filled-band state, noncompact Gauss sector and regulator prescriptions
are one supplied model setting; this calculation neither derives that
setting nor counts its clauses as independent walls. Group the remaining
physical obligations into native realization/identification (I), interacting
matching and physical charged-state interpretation (R), and observational
source/transport/detector/statistical forward model (O). Mass, speed and Pauli
matching are parts of R, not separate claimed independent walls. Source and
detector nuisances are parts of O. No independence or exhaustion count is
asserted:

| Pair | First closing implies second closing? | Reverse implication? | Disposition |
| --- | --- | --- | --- |
| I / R | unresolved | unresolved | Preserve both obligations without an independence assertion |
| I / O | unresolved | unresolved | A complete native measurement construction could affect both; none is supplied here |
| R / O | unresolved | unresolved | Their joint physical matching may overlap; no theorem separating them is claimed |

No known automatic implication is used to inflate this grouped set.
Calibrating the physical mass changes the bare-to-physical map; it does not
add another independent measurement or necessarily another free parameter.

**N3 — Hidden-condition scan.** A literal and close-variant reread classifies
"canonical" fermions, field normalization and the emission heading as
explicit supplied quantum normalization; "squared-amplitude" and transition
probabilities as the explicitly supplied statistical rule; "background" in
the HESS comparison as a detector nuisance, not a physical electron
identification; and "registered" primitives as the already approved
premises, not this action's derivation. Time, lattice frame, vacuum, coupling,
units, species and mass calibration, regulator order and absence of a Pauli
improvement term are explicit model or matching conditions grouped in N2.
There is no "standard QFT" shortcut supplying the displayed current,
seagull, scalar coefficient or tensor matching. No unlisted condition is
promoted into an implicit prediction.

**N4 — Residual matching.** No prior no-go is used to prove these new exact
or limiting statements. The contextual comparisons have the following
precise scope; nonmatches supply no negative witness:

| Witness and location | Residual actually addressed | Present residual | Match as a proof of the present result? |
| --- | --- | --- | --- |
| Jacobson et al., hep-ph/0209264v2, section III.B, equations (25)-(29) | Leading quartic Cherenkov threshold cubic | The leading cubic in (6), plus full-torus localization and exact-axis result | Yes for the credited leading cubic; no for the additional exact/localization claims |
| Beane et al., arXiv:1210.1847v2, fermion-action and magnetic-moment discussion | A spacetime Euclidean Wilson action | Continuous-time spatial Wilson frequency ratio (4) | No; different temporal action, no imported sign or magnetic coefficient |
| [Spatial Peierls logarithm note](SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md), finite-matching and physical-spectral scope | Logarithmic velocity flow for a different four-Weyl carrier | Finite local Wilson coefficients and a still-open physical pole map | No; contextual prior work only |
| Hashimoto and Okamoto, hep-lat/0302012v1, equations (2.2), (4.3), (4.31), (4.38)-(4.39), (A11), (A13)-(A20) | General anisotropic lattice action and one-loop integrals | The fixed spatial-Wilson continuous-frequency scalar shift | Partial action/integral correspondence only; its conventional fixed-r_s Hamiltonian limit is not this fixed spatial Wilson limit |

**N5 — Resolution and rhetoric.** Per-element Clifford and derivative
identities and per-mode free spectra are tested. Per-site finite-field link
Hamiltonians and per-block Landau matrices are tested controls of the stated
limit. The free pair and axis inequalities are analytic whole-torus
statements. Finite grids do not prove them. No exact interacting lattice-wide
phase, detector or all-coupling statement is tested or asserted. The primary
runner's cached stdout records all five resolution classes, with an explicit
unexecuted interacting-lattice qualifier. The width theorem has fixed
direction, fixed margin and the specified order of limits; its finite-rate
controls do not establish uniformity at excluded equality or a joint axial
limit. Statements denying a current physical identification concern the
missing construction, not a theorem that no such construction exists.

**N6 — Partial closure and approved primitives.** The checked registry is
`docs/audit/data/axiom_premise_nodes.json`, with source notes
`docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`,
`docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` and
`docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`. These approved premises
supply the unit reference, structural kinetic-form isotropy and pointwise
realized-state slot in their declared senses. They are not missing or
unapproved primitives. A units relabeling can retire a spurious ruler wall;
a mass renormalization condition can replace the tree bare-mass calibration
without predicting the observed mass; a chosen time regulator can make a
different coherent conditional model. No new axiom is said to be required.
A native construction, a matching calculation or an explicit observation
map can discharge corresponding imports through new mathematics/physics.
An eventual import-retirement audit is distinct from this ordinary review
and is not performed here.

**N7 — Strongest counter-route.** A hostile reviewer should insist: "Your
positive Wilson scalar shift and finite local anisotropy do not exclude the
action. Tune its critical mass with the same observed-mass datum, match the
bare kinetic parameter in a specified infrared scheme, and compute the
charged spectral/propagation observable and Pauli response from the same
action. A common low-energy propagation cone could then coexist with the
finite coefficients you computed; the remaining quartic terms could retain
falsifiable directional signals." Equations (13) and (17), their Ward
cancellations, and the contextual Peierls calculation provide concrete
support for this route. Its terminal obligation is a gauge-consistent,
infrared-controlled physical dispersion and magnetic response with an
explicit parameter/data count, followed by the source/detector map. It is
unclosed and is preserved in the campaign queue. Thus a broad interacting
exclusion remains a partial attempt, while this route does not contradict
the precisely fixed free-symbol or one-loop local statements.

**N8 — Cross-cycle echo and retirement mechanisms.** The repo was searched
for similar wall language and prior loop `NO_GO_LEDGER.md` files. The following
read records are historical scope evidence, not current audit verdicts:

| Prior record | Similar wall and retirement status | Mechanism considered here |
| --- | --- | --- |
| `lane2-atomic-scale-20260428/NO_GO_LEDGER.md` under the loop-pack root | Supplied mass/low-energy coupling and physical-unit map were separate from the dimensionless spectrum; the ledger itself does not establish full retirement | The registered scale-reference primitive already supplies its declared ruler. We do not repeat that as a missing primitive; observed m and alpha are explicit calibrations and their scheme/loop matching remains a calculation |
| `born-scattering-closure-20260710/NO_GO_LEDGER.md` | A phase-count functional alone did not supply a detector-centroid response; signed detector-adjoint weights were a named repair, with no full physical retirement established in the read record | Keep the detector functional explicit and do not identify a HESS candidate endpoint or tree shell with a measured survival bound |
| `toe-axiom-closure-block104-same-action-dk-os-20260814/NO_GO_LEDGER.md` | Flat massive action orientation was repaired by mI+iM0 and the same-action positive residue; finite-spacing asin/asinh identification remained separate | Preserve this action's continuous physical time. A transfer-first or different temporal action is a live changed-model route, not a contradiction or new-axiom necessity |
| Earlier block of this campaign, `NO_GO_LEDGER.md` and the photon/electron threshold note | Photon timing alone did not fix the charged spectrum; a species-resolved Wilson completion was a live repair | This block actually executes that repair: one light free cone and a positive pair gap, then magnetic/radiative costs. The naive species obstacle is removed at free-spectrum scope; physical identification is still open |

The scope-limited search makes no assertion that every historical wall was
found or that its ledger wording is a present audit grade. No candidate
retirement mechanism above is dismissed merely as a new axiom. Fresh main
was searched at `f1147ea1fa3fab12bf56ace37b62083cc2bfa405`; a scoped search of
all16 then-open proposal titles/bodies found no Wilson finite-matching lead.
That is priority hygiene, separate from this similar-wall check and not an
exhaustive novelty claim. The checklist is proposed review evidence for the
bounded packet, not a certificate of universal impossibility or an audit
verdict. The broader inverse problem stays open.
