# Far charged-pair scattering: focused analytical check

PASS for the proposed leading coefficient operator, conditional on the independently checked complete order-ten potentials. The microscopic finite-time conclusion is available with explicit time/error restrictions below; a fixed-lambda full-H scattering theorem does not follow.

## Domain and coercivity

After excluding lower Q sectors, lower Q8 perimeters, and all order-eight-shifted shapes, the remaining ordered two-column relative domain is exactly D=Z²\F, where F is the Manhattan ball |x|+|y|<=4 with the four axis-distance-four points removed from F. In particular (3,1) must be removed; keeping it as a zero-shift state would give a different domain. The (2,2) repulsive states, axial-three molecules, odd rods and T shapes are also eliminated by order-eight gaps. The nonminimal infinite rod family therefore does not remain an unaccounted zero-shift continuum channel, assuming the supplied exhaustive D8 classification.

At COM zero the two ways of moving a relative endpoint give nearest-neighbor hopping t=2gamma10. After shifting the far rest and kinetic bottom, K=t(4−adj_D)+U. The only boundary types modulo D4 are (4,0), (4,1), (3,2); they have respectively 1,1,2 neighbors in F. The supplied negative ratios are U40/t=−1144/2431 and U41/t=−572/2431; U32 is positive. Thus, for K_D=t(4−adj_D),

 K >= (1−1144/2431) K_D = (1287/2431) K_D.

Indeed the Dirichlet form is t times internal unordered-edge differences squared plus t times missing-neighbor counts times |psi|². The negative potential consumes less than the indicated fraction of the boundary term. This proves nonnegativity, excluding any negative-energy bound state of this leading far-channel operator, without a Birman-Schwinger numerical test.

## Bounded threshold solutions

The bound also excludes a nonzero bounded zero-energy solution, not only an l2 eigenvector. Take a logarithmic cutoff chi_R equal to one near F and tending to zero over an expanding annulus with sum_edges|grad chi_R|² tending to zero. The discrete localization identity for Kpsi=0 bounds <chi_R psi,K chi_R psi> by C||psi||infinity² times that cutoff energy. The potential is diagonal and causes no cutoff error. Coercivity then forces every fixed local edge gradient and every missing-neighbor boundary value to vanish as R grows. Connectedness of D forces psi to be constant, and the nonempty absorbing boundary forces that constant to be zero. This proves the requested absence of a bounded zero-energy resonance. It does not exclude the logarithmically growing zero-energy scattering solution, which is expected and required for two-dimensional scattering.

## Threshold T convention and coefficient

Use ordered-relative plane waves with lattice Fourier measure d²k/(2pi)² and outgoing resolvent (E+i0−K0)^−1, K0=t(4−adj_Z²). Near zero K0(k)=t|k|²+O(|k|4), and its finite-support Green matrix has common singular part

 −[log(t/E)+i pi]/(4pi t) times the all-ones matrix.

The remaining finite-support matrix has a finite zero-energy limit. Treat the obstacle by finite-rank elimination (or the positive onsite-penalty limit), together with U. Absence of a bounded zero solution prevents a transparent/threshold-exceptional cancellation of this monopole channel. The finite-dimensional resolvent identity then gives the ordered-relative on-shell monopole T amplitude

 T(E;k',k)=4pi t/[log(t/E)+O(1)+i pi] + o(1/log(t/E)),

so its leading real coefficient is 4pi t/log(t/E). The real O(1) term is shape/potential dependent and is not determined by coercivity alone. The imaginary sign reverses with the incoming/resolvent convention; define T=V+V(E+i0−H)^−1V or the equivalent outgoing Lippmann-Schwinger convention before reporting signs. This amplitude is not a physical symmetrized rate, cross section, or unit-normalized bosonic matrix element. Projection to even relative states requires its own normalization and incident/outgoing-channel convention.

For background on discrete threshold resolvent expansions, the primary analysis by Komech–Kopylova–Vainberg is available at https://www.mat.univie.ac.at/~komech/articles/KKV07.pdf. No continuum theorem or generic ground-state stability result has been imported as a microscopic scattering proof here; the logarithmic coefficient above follows from the lattice symbol and finite-rank reduction.

## Actual finite-box evolution

The useful transfer is a matched block/unitary comparison. If the author establishes, after all reductions and common-energy subtraction,

 H_eff/(Jlambda10)=K_R + B_lambda,R,
 ||B_lambda,R||<=C lambda² + C R²lambda^(M−10),

then Duhamel gives norm error <=|tau|[C lambda²+C R²lambda^(M−10)] for physical time tau/(Jlambda10), in addition to state-identification/source errors. Finite-Q relative locality is the needed reason the retained lambda² term is volume independent; a global extensive norm estimate would not suffice. The order-eight elimination itself has mixing O(lambda²) and second-order correction order lambda12, consistent with this bound. The exact low-energy wall embedding and exact momentum/charge restriction remain required.

Thus fixed scaled time, or tau=o(lambda^−2), can be transferred on polynomial grids once M is sufficiently large. Coefficient-model scattering wavepackets can be approximated for suitably growing observation times before boundary return; this needs a separate finite/infinite-volume propagation estimate. One cannot infer arbitrarily low-energy scattering from the lambda² remainder alone: for a packet of scale E~lambda^(2a) observed for tau~1/E, its phase error is lambda^(2−2a), requiring a<1 (or a sharper subtraction/control). In particular first-grid energy E~R^−2 with p>1 does not meet that simple comparison. Errors small compared with the logarithmically small scattering signal require the corresponding stronger comparison, not merely norm-o(1).

No fixed-lambda microscopic wave operators, infinite-time S-matrix, complete scattering of all channels, or interaction-free physical bosons are proved by this leading coefficient model. This is a viable controlled finite-time route, with the stated time and precision limitations.

## Coefficient-check update

The independently certified ratios simplify to U40/t=−8/17, U41/t=−4/17 and U32/t=30305/161109>0. Thus the same form bound is exactly K>=(9/17)K_D. The preceding unsimplified fractions are equivalent. The reported numerical finite part B and scale exp(4pi B) were not independently replayed in this analytical check; they are not needed for the universal leading logarithm or no-resonance proof. Keep such a finite part labeled as numerical coefficient-model data until separately controlled.
