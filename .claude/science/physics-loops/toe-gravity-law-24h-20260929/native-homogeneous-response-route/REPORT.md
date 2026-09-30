# Homogeneous density weight beyond a gap-or-degeneracy alternative

Frozen author discovery candidate for the explicitly supplied full-site M2
Hamiltonian H0=S+mu D+W. Two new results are proved here. They have not yet
received root's focused comparison; no formal review, audit, phase selection,
PR or retained status is claimed. Mainfb5da8dd and selected methodology7146
are bound exactly. All twelve method/foundation files remain byte identical.

The first result forces actual local density spectral weight OUTSIDE the full
ground space. The second forces long-wave density weight below a frequency
cutoff tending to zero in a JOINT dilute/long-wave limit. The second result
is substantially stronger than the first and has its own contract/proof.
Neither repeats the earlier finite-distance pair coherence or moves a
nearby-field response to zero field without a new argument.

## Actual state, carrier and first result

Let Gamma be any ground density matrix of Hnu=H0-nu N on a cubic torus,
with the actual complete S term, fixed supplied mu,tau>0, and rho=<N>/V.
The expectation rule, chosen law/basis and ground-state family are supplied
mathematical objects, not a foundation selection. Translation averaging makes
Gamma homogeneous. No tensor identification or original-rotor record law is
being imported into this different native Hamiltonian.

Use Q=1-P0 for the COMPLETE ground projection of Hnu. The on-site positive-
frequency measure is

 sigma(domega)=V^-1 sum_x Tr Gamma n_x Q dP_(Hnu-E0)(omega) Q n_x.

For L>=5, beta=2mu/3-2nu>0, b=3mu+24tau and C2=1296b²,

 M1>=beta rho, M2<=C2 rho,
 M0>=beta² rho/C2, M_-1>=beta³ rho/C2².                  (R1)

Thus a fixed fraction of local density weight is genuinely inelastic even
if the ground space is degenerate. For 0<nu<=mu/6 one can use beta>=mu/3.
The actual finite-window lower is

 sigma([beta/4,2C2/beta])>=beta² rho/(8C2).              (R2)

This interval is bounded away from zero. It can be optical/high-momentum
weight. 'Homogeneous' refers to the state, NOT the probe momentum; the N
observable at q=0 has no positive-frequency response.

The complete proof is ONSITE_PROOF.md. Its decisive exact pin is
p_x S p_x>=(2mu/3)p_x on the eighteen physical graph edges incident at x.
Axial entries are diagonal2mu/3; each plane is the four-cycle with diagonal
3mu/2 and off-diagonal+mu/4. Sum_x p_x=2I is essential. The literal on-site
f-sum and D=N-2P+V3/mu then give

 sum_x m1(n_x)>=(2mu/3)<N>-2<H0>+(4mu/3)<D>+(2/3)<V3>.

The current norm uses actual B_e*B_f and a weighted Cauchy bound; no
factorization of separated currents or bosonic pair algebra is assumed.
An early weak mechanism brief discarded one endpoint multiplicity; root's
independent precomparison restored it before this proof/control freeze.
Root's subsequent full-S+W monitoring construction was mentioned but not
read or used. This packet retains the independently derived S-only bound.

## New long-wave consequence at the homogeneous point

For L>=25 and nonzero reciprocal q let A_q=sum exp(iq.x)n_x. Symmetrize the
q and -q positive-frequency measures with factor1/(2V), removing the same
FULL ground projection. All explicit constants are in LONGWAVE_PROOF.md L1.
They depend only on supplied mu,tau and are deliberately large. There exist
explicit nu_*,q_*,C_E,C_N>0 such that at 0<nu<=nu_*,0<|q|<=q_*,

 m1(q)>=(tau/4)rho|q|²,
 m3(q)<=rho|q|²(C_E nu+C_N|q|²).                        (R3)

Writing Omega(nu,q)=sqrt[(8/tau)(C_E nu+C_N|q|²)],

 integral_(0,Omega] omega sigma_q(domega)>=(tau/8)rho|q|²,
 sigma_q((0,Omega])>=tau rho|q|²/(8Omega),
 integral_(0,Omega] omega^-1 sigma_q(domega)
                             >=tau rho|q|²/(8Omega²).  (R4)

The bounds hold at each admissible finite volume, so ANY joint sequence
nu->0,q->0 has Omega->0 with the stated positive normalized mass. The source's
existing density lower bound ensures rho>0 and is not differentiated. At
fixed nu>0 this cutoff retains a nonzero term proportional to sqrt(nu).
Nothing here proves fixed-density sound, a quasiparticle pole, ODLRO,
uniqueness, a selected polarization, or a physical clock/source mechanism.

The full proof is LONGWAVE_PROOF.md, with its separate LONGWAVE_CONTRACT.md
and root's separate precomparison boundary. Its load-bearing new steps are:

* Keep the exact nine-edge pair-center symbol and endpoint factor
  F_q(d)=2cos(q.d/2). The symbol is real/even; the actual low Hessian is
  positive. Its fourth derivatives and high-channel energy yield the LOWER
  f-sum, not only the older upper f-sum.
* Express m3 as the local double-current expectation. Each connected term
  lives in B10 and has norm O(|q|²). Extract its literal N2 matrix and lift
  through the actual hard-core pair words. The difference has two-sided
  support on local N>=3. It is NOT discarded.
* An occupied site in that ball is either isolated (D cost) or supplies an
  actual pair and a third occupied spectator. Translating that SAME pair
  until it hits the spectator gives n_z B_(e+r)=0. A finite telescope with
  n_z kept on the left controls the summed crowded projector by C_10 H0.
  Radius10 is fixed; no volume/global cluster probability is substituted.
* The exact N2 current is O(|q|(|k|+|q|)), since h'(0)=0. Its moment is
  O(q² e+q^4 rho), while the full hard-core remainder costs O(q² e).
  Ground e<=nu rho then gives (R3); positivity of the spectral measure gives
  (R4). The complete many-body ground projection remains removed throughout.

The local triple-current correction is the consequential interaction step.
Ordinary locality alone would leave m3<=C rho q², with no shrinking cutoff.
The finite-density remaining condition is stronger: a genuine further
cancellation/restriction of the q²e contribution, or another actual
long-wave theorem. The present crowded-projector bound does not do that.
ATTEMPTS.md preserves this failed weaker estimate and the remaining scope.

## Source closure and actual controls

The current-main native density source7180c065 was reread completely. It
supplies the actual SOS identity and H0>=mu D+a Egrad. The previous native
phase and dilute-phase reports were read completely, with their finite-mode
and ODLRO boundaries retained. The previous density-response proof's actual
current/row arguments were reread; its nearby-field alternative is not a
premise. The old pair symbol is rederived in the current proof and checked
from source words. PR9413's unchanged exact source was read previously and
is current prior art only; no EOS derivative is imported. The main Gaussian
full-star infrared note was read completely and excluded as a different
carrier/reference. SOURCE_BINDINGS.json and PRIOR_REFRESH.json record this.

The standalone exact control rebuilt11,662 literal S/W rows and verified the
pinned matrix, actual row sums, center displacement/evenness, and six Hessian
directions. A six-site/64-dimensional full M2 fixture from two overlapping
actual plane-S stars shows275 nonzero rational higher-occupancy remainder
entries, while every N<=2 input/output block agrees with the literal lift.
For example R_(7,7)=99/32 and R_(13,13)=-6033/64. This rejects simply treating
the nested current as a free-pair quadratic operator.

The corrected run returned TOTAL PASS=7 FAIL=0 (seven finite control families)
in8.403099CPU/8.428339wall seconds with23,871,488 bytes peak RSS. The first
single-plane fixture FAILED its nonzero-remainder discriminator because that
special fixture's remainder was zero. Original code/output/receipt are kept
verbatim under history/single-plane-zero-remainder; FIXTURE_CORRECTION.md
records the pre-rerun repair. No analytic theorem was changed for that
fixture issue. CONTROL_ANALYSIS.md distinguishes every actual check from
the analytical all-volume proof. No run was fabricated or repeated merely
to attach source labels; POST_EXEC_INPUT_BINDING.json is explicitly metadata.

Both full proof files and the complete corrected control output were cold
read by the author before this freeze. Root received mechanism briefs and
froze separate on-site and long-wave PREs before full proof/code/results
exposure. Those are pending focused comparisons, not already granted review
credit. No descendant consequence is adopted before that check.
