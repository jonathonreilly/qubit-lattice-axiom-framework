# Fixed-rate geometric formation: declared follow-up and research assessment

2026-09-21. Author interpretation of a prespecified finite-size experiment,
with separate selective source, endpoint and statistical checks. This is
numerical evidence about the supplied classical geometric process, not a
phase theorem or an empirical prediction about nature.

## What was run

The unchanged source, protocol and analysis plan define twelve cells:
periodic cubic side lengths N=16,32,64,128, slide rate kappa=1, and paired-birth
rates beta=.1,1,10. There are256 independent seeded histories per cell for
N<=64 and64 per cell at N=128, for2496 histories total. Each begins empty
and stops at its first completed matching. The event cap is10^9 and the
post-filling plaquette rate is nu=0. Every declared history completed; none
was capped, replaced, excluded or left unstarted.

The simulator samples the geometric projection with permanent paired record
identities. It does not sample the continuum of projector contents or implement
unknown-qubit recognition. The earlier construction gives an autonomous
geometric law because its neighbor-dependent content distribution integrates
to the specified beta on each vacant edge. That model bridge remains supplied.

The source and receipt identities are:

- C++ source: 5e24d66b068740dd58dd8aeb9d88f6cfc90238105b7266563bc37ecc2532b716.
- Executable: ffc3e77cf1793b5acb6fdb792563ee13db11ed73a698b2652dbff79300b4f10d.
- Protocol: 4dae8ad738bf49af9b01ac6dada4f8f35383f317d6716b9e4de279797b999d48.
- Analysis plan: 13db5d01088ff610b4787b89b42c04cc048e0322fb666a0985141011352e13ab.
- Corrected analyzer: 9da84212404a18f7a1eaf6be7ddef3bfab657d6d8f5c201bba5778ac4720597a.
- Production manifest: 5ef3455f4902be019f0863754c14b44b447914eed3f3219a17891fa29c6a00e2.
- Production summary: 310e9bc256bbad3e03cefd5d44258d781ea431e42b5e253114eedfbc4a948ea0.
- Frozen analysis results: 51b2f9b5174877030b7ebb8baa345dd030dbeb23b3ca3072f6525fb73ed79c86.
- Full per-history table: 2bfcb1b31f4d4010488920652cd43163c624121f5d8826bbf10417baa398aa88.

The complete declared estimates, standard errors and intervals are in
geometric_fixed_rate_results/RESULTS.json and TABLE.md. PER_HISTORY.json
preserves the history-level statistics. Large physical arrays remain in the
external production directory, bound by the manifest, receipts and complete
independent file-hash inventory.

## Observable and uncertainty definitions

At completion, n_i(x) indicates a matching edge from x to x+e_i and
sigma(x)=(-1)^(x_1+x_2+x_3). The readout

    F_i(x)=sigma(x)[n_i(x)-1/6]

has exact lattice divergence zero. With orthonormal Fourier normalization
V^-1/2, the transverse power is half the total power after subtracting the
lattice-longitudinal component. S_q averages it within each history over
the declared nonconjugate modes with squared integer wave number q.
There are3,6,4,3 modes in shells q=1,2,3,4. The integer winding flux through
a coordinate plane is Phi_i, and W=sum_i Phi_i^2/(3N).

Every inferential unit is one complete history. The10000 paired bootstrap
draws resample whole histories, preserving the covariance between observables.
All reported95% intervals are pointwise percentile intervals. They account
for across-history sampling variation; they do not include finite-size bias,
possible simulator bias or a simultaneous multiple-comparison guarantee.
Means use sample SEs; ratios use paired delta-method SEs. All144 declared
metrics and intervals are defined in this production run. The analyzer's
pre-data corrections preserve explicit undefined-ratio and noncompletion
behavior, with independent acknowledgments.

A flat isotropic Gaussian transverse-field ansatz gives the conditional
comparison values S_2/S_1=S_3/S_1=S_4/S_1=W/S_1=1, individual-mode
fourth-moment ratio3/2, axis-shell ratio7/6 and winding ratio5/3.
Those constants require the assumptions written in the analysis plan.
They are comparison references, not proven properties of the process.

## Observations

The longest-mode amplitude S_1 stays around.19 as N increases from16 to128
at all three fixed rates. Increasing N lowers the measured wave number;
this data window shows no collapse of that amplitude toward zero.
The low-shell and winding ratios remain of order one. Some pointwise
intervals exclude their flat-spectrum or Gaussian reference values, including
some fourth-moment diagnostics. The data therefore should not be described
as proving Gaussianity or equality to a uniform equilibrium measure.

At N=128, the declared estimates are:

| beta/kappa | S_1, pointwise95% interval | W/S_1, pointwise95% interval | S_4/S_1, pointwise95% interval |
|---:|---:|---:|---:|
|0.1|0.196523 [0.179043,0.214742]|0.847041 [0.676151,1.039442]|1.100027 [0.964667,1.254290]|
|1|0.176622 [0.159376,0.193322]|1.175624 [0.897304,1.517717]|1.092418 [0.975947,1.232894]|
|10|0.204868 [0.187116,0.222454]|0.959913 [0.784888,1.159529]|0.925617 [0.828876,1.033048]|

The mean formation time divided by volume is also roughly stable over the
declared sizes at a given rate. At N=128 it is.935359,.118250,.0361218
for beta=.1,1,10 respectively. This is a finite-size observation, not an
asymptotic time law. Slides per site increase over the same range; no power
or logarithmic fit was declared or performed.

At N=128 the fraction of sites with more than one record born there is
.2621917,.2262062,.1213256 at those rates. These fractions vary little with
size in this experiment. This directly exhibits the intended reuse mechanism:
an old record leaves and a later record forms on the same site. The record
contents and identities remain permanent. On this closed finite lattice,
total records at completion equal V, so sites with repeated births are
balanced by sites with no births. Reuse does not permit unlimited total
creation on a fixed finite number of single-capacity sites.

The companion figure displays six of the declared observables, without
introducing a new selection rule or fitted model:

![Declared fixed-rate follow-up](geometric_fixed_rate_results/fixed_rate_formation.png)

## What the independent checks establish

The prior source review examined the generator, event catalogs, Fourier and
winding conventions, and paired bootstrap mechanics. Its three analyzer
findings were corrected and separately acknowledged before production values
were inspected. That history remains preserved.

The production checker fixed replicate indices17 and41 in every cell before
opening any production outputs. It reconstructed24 physical endpoints from
their compressed partner, identity and site-birth arrays, including exact
integer Gauss law, winding, record pairing, site reuse and384 Fourier modes.
Its separable Fourier contractions were independent of the C++ direct sums
and the author's full FFT. Maximum mode-power differences were8.16e-14
against C++ and1.33e-15 against the author FFT.

It authenticated all14976 receipt-listed files for all2496 histories, then
reconstructed the full saved sufficient-statistics table from the per-case
outputs and certificates. Independent compensated sums and covariance
quadratic forms reproduce all144 point estimates and144 standard errors,
with largest absolute differences5.55e-15 and1.94e-16. The checker did not
replay all trajectories, independently decode the other2472 endpoints, or
rerun the production bootstrap quantiles. Hash authentication is distinct
from those missing checks. No claim about interval coverage was reviewed.

Production report SHA:
4e75c9c5449119f44b2f5affde6153a705cbf8b4f2edf7fa75c06cda75cc99f8.
Final seal SHA:
1cf42bdc87fc279bbc94b815b40fda9145ea73e0b4f9f0ca432e38b369cd0504.
Root read the complete report, prereconstruction formulas and all three
scripts and authenticated all staged seals; its receipt is
GEOMETRIC_FIXED_RATE_PRODUCTION_ROOT_VERIFICATION.json.

## Research judgment

This is a promising route for producing constrained, spatially extended
fluctuations by local formation and immutable-record motion. The combination
of exact geometric constraints, substantial long-wavelength fluctuations
and actual site reuse warrants a direct attack on its dynamics. It is more
specific than obtaining a formal divergence-free readout alone.

The practical fixed-rate data are distinct from the proved slow-birth limit.
The sufficient schedule (beta/kappa)K^12->0 is conservative and is not a
necessary condition inferred from these experiments. Neither its failure
at fixed beta nor the encouraging finite data decide the thermodynamic law.

The main unresolved step is now dynamical: the simulated nu=0 process freezes
once full. These histories establish no propagating disturbance. A successful
continuation must specify local immutable-record moves on the formed state,
identify the stationary or evolving ensemble they actually preserve, and
derive a transverse dispersion law there. Separately matching a static
constrained ensemble and a wave model on another state space does not meet
that requirement. An operational quantum bridge and a principle selecting
the supplied laws remain further obligations.

