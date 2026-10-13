# Charge reconstruction: results and scope

Direct parent scientific authorship. Status: conditional-support. The first
frozen execution ran 2026-10-13T01:21:55.626108Z to 01:21:56.388849Z, exit 0,
empty stderr and unchanged source. No unsuccessful calculation was omitted.
The four executed inputs and their byte identities are frozen in FREEZE.json
and evidence_v1/source_snapshot. Independent scientific review is pending.

## Exact mathematics and implemented controls

The Yukawa and anomaly equations leave no one-generation hypercharge freedom
without the singlet neutrino, after supplying the stated representations,
Higgs and mass couplings. With Dirac singlet neutrinos they leave
Y=2h[Y_SM+epsilon(B-L)] and Q=Q_SM+epsilon(B-L). The supplied Majorana or
Weinberg mass operator instead fixes epsilon=0 in the common-charge family.

The implementation checked all 364 symmetric cubic triples of the 12 gauge
generators in the 16-dimensional left-handed representation, with exact
symbolic entries, plus every mixed gravitational trace. All vanish after
the stated weak-anomaly relation. Removing the neutrino or using a fundamental
rather than antifundamental conjugate quark gives the expected nonzero
traces; these are deliberate sensitivity controls, not failed executions.

All 45 rational cases, spanning three odd color counts, three Higgs
normalizations and five deformations, satisfy the respective algebraic
identities. All 512 three-by-three bipartite graphs obey incidence rank
6 minus component count; 205 are connected. The graph controls do not assert
unitarity of arbitrary support patterns or constitute mixing data fits.
The disconnected three-family counterexample passes the total anomalies.

All 37 fixed-lattice cases reproduce the direct-product and Z2/Z3/Z6
congruence sets. The fixed primitive z=6Y, z_H=3 hypothesis permits
half-integer epsilon in the product and epsilon in 3Z in the Z6 quotient.
On epsilon>-1 the smallest nonzero absolute neutron charges in electron
units are respectively 1/3 and 3/4. These are conditional gaps for fixed
embeddings, not consequences of unspecified compactness.

Four explicit primitive compact representations with epsilon=10^-k,
k=3,6,12,22, preserve Yukawa/anomaly identities while giving nonzero charge
1/(10^k+1). Their integer Higgs weights and global primitive lattices vary.
This keeps both the local algebra and the global-group limitation explicit.
No gauge algebra, multiplicity, generation count or native chiral phase is
derived, and not every possible global anomaly has been classified.

## Observation mapping and fit/test separation

All values below use units of 10^-21 times the electron charge. Both historical
primary summaries were exposed before choosing this calculation. They are
not blind holdouts, latest-limit claims or raw-data likelihoods.

Only the neutron summary -0.4 +/- 1.1 calibrates delta=q_neutron/|q_e|.
The candidate predicts x=(q_p+q_e)/|q_e|=0 and q_nu/|q_e|=-delta.
The SF6 signal is s=(70x+76delta)/146. Its frozen transfer prediction is
-0.20821917808219179, with propagated uncertainty 0.5726027397260274,
compared with the exposed measured summary -0.1 +/- 1.1. Under the explicit
independent Gaussian summary approximation, the residual is 0.10821917808219178,
combined uncertainty 1.240110437639226 and standardized residual
0.087265758595022. This agreement does not establish a nonzero charge.

The separately labelled optional joint refit treats both summaries as
calibration: delta=-0.3556769526059353 +/- 0.9757195514807966,
chi-square 0.007615312623164653 with one residual degree of freedom.
It is not the preceding fixed transfer comparison, and no p-value or new
confidence region is claimed.

Without imposing the candidate x=0, the two-summary inversion gives
(x,y,q_nu/|q_e|)=(0.22571428571428567,-0.4,0.6257142857142858), with
uncertainties (2.586516055647529,1.1,3.2446099731017015). Its full correlated
rank-two covariance is in RESULTS.json. The inferred neutrino quantity uses
beta charge conservation; it is not an independent neutrino measurement.

The acoustic paper's special x=y interpretation assumed a neutral
antineutrino. We instead use its molecular response, nominal composition and
calibration. Its polarity half-sum is -0.1, uncorrelated uncertainty about
1.063 rounded by the paper to 1.1; the half-difference 9.2 is the odd nuisance.
An unconstrained even-polarity offset would be degenerate with the signal.
The published calibration/subtraction assumptions and lack of raw event or
systematic covariance information limit the transfer test.

## Source failure and scientific boundary

Opening the neutron full-text endpoint through the web tool returned
InternalError. The source import is explicitly limited to the primary journal
abstract's result. This access failure is not a successful full-text read,
an event-level validation or a scientific rejection. The useful local route
uses the available summary with its limitation preserved.

The hypercharge family and global-group distinction have established prior
art. The original work here is the explicit, reproducible campaign
reconstruction and its source-to-observable bookkeeping, not a novelty claim
for standard gauge theory. Matter can be embedded in the previously supplied
physical metric, but anomalies do not fix its gravitational couplings,
Yukawa matrices, masses, renormalized trace response or quantum state.
A common microscopic matter/gravity construction remains open.
