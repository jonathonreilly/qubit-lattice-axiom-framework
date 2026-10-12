# Independent referee report: C5 probe R6-4

## VERDICT

**CONFIRMED WITH CORRECTIONS.**  The central result is sound: a nonempty
smeared Newtonian continuous-CQ region is exhibited, the unregulated local
point-particle limit has a genuine UV obstruction in the stated class, and the
covariant family remains open.  Most importantly, the worker is right that
OSSW's published torsion-balance reduction from F6 to F8--F10 is invalid.  The
published **"32-decade empty window" falls**.  It must not be retained as an
experimental result.  The corrections are that the DP radiation radius was
imported with a normalization mismatch, the claimed 10-micrometre ISL endpoint
was not obtained from an apparatus fit, LPF is not a kernel-independent floor
and has a one-sided/differential factor of two, the cosmology claims are
conditional more narrowly than stated, and a
classical metric trajectory is not automatically a Set-A record without a new
readout/permanence bridge.

## Scope and verification

I audited the worker's H1--H6 class, not all classical--quantum theories.  The
key restrictions are homogeneous Markovian Gaussian kernels, additive direct
and feedback dephasing with no cross-correlation, a Gaussian coupling form
factor, and point particles (`R6-4_report.md:49-68`).  The no-go below therefore
has the same walls.  The supplied calculation reruns byte-for-byte: the original
and rerun SHA-256 are both
`c0975312ec531d7a29202ad143baf1b46f9af4fdc8f5e77a173176a62c23c897`.
Independent calculations are in `scripts/r64_referee_checks.py` and
`scripts/r64_referee_checks.out`.

## Findings

### 1. Lemmas T, F and R; Corollary U

**Lemma T is correct in the stated Fourier-diagonal class.**  OSSW's CP block
is `[[2D2,D1],[D1,D0]] >= 0` (`text/opp2203.txt:728-745`).  With
`P_J=2D2`, Newtonian drift `D1=-g/2`, and the effective kernel on the bare mass
density, its determinant gives

`P_J(k) D0(k) >= |g(k)|^2/4`.

For kernels with zero modes this is a support/generalized-inverse statement,
not an ordinary inverse on the null space.  Layton et al. give the same kernel
condition as `4D2 >= D0^{-1}`
(`sources_untrusted/source_Layton_2307.02557.clean.txt:938-952,1483-1501`).

**Lemma F is correct under H4, but is not class-wide beyond H4.**  Adding the
direct Lindblad kernel and random-potential dephasing gives

`K = D0 + (4 pi G)^2 |g|^2 P_J/(hbar^2 k^4)`.

The CP product and AM--GM give `K >= (4 pi G/hbar)|g|^2/k^2`, with equality at
the worker's stated kernel.  This is the standard least-decoherence/DP kernel.
Cross-correlated, non-Markovian, field-dependent, or non-Gaussian models are
outside the proof; the worker listed those exclusions (`R6-4_report.md:62-68`).

**Corollary U is correct, narrowly.**  With `g=1` and a point mass, the floor
implies `d<p^2>/dt >= 4 pi G hbar m^2 int d^3k/(2pi)^3`, a cubic UV divergence
(`scripts/r64_checks.out:6-11`).  The valid conclusion is: no cutoff-free,
homogeneous, Markovian Gaussian realization satisfying H1--H5 has finite
point-particle heating.  It does **not** exclude finite-size matter, a covariant
UV completion that changes the high-k Newtonian limit, colored noise,
field/position-dependent kernels, correlated direct/feedback noise, or the
discrete-jump class.

**Lemma R's inequality is correct; its equality sentence needs qualification.**
For the direct monitoring channel,
`-ln BC <= Gamma_direct t` follows immediately from Lemma T.  At CP saturation
that direct-channel inequality is an equality.  The physical reduced-matter
visibility also contains feedback/potential-noise dephasing from Lemma F, so
the total visibility generally obeys a strict inequality; complete positivity
is compatible with O4's `V <= BC`, but is not by itself an ontological record
theorem.

### 2. The smearing window and laboratory numbers

**Rerun and core arithmetic.**  The supplied script is reproducible.  Its Earth
heat floor, `ell >= 5.0e-12 m`, is correct
(`scripts/r64_checks.out:15`; `scripts/r64_referee_checks.out:4`).  Panda et al.
indeed report a 1.9-micrometre separation and coherent phase accumulation up to
70 s (`sources_untrusted/source_Panda_2210.07289.txt:146-153`); treating
`1/70 s` as a decoherence ceiling is conservative, not a fitted collapse-model
limit.  The cited LPF differential ASD, 1.74 fm s^-2/sqrt(Hz), is the published
number.  The least-decoherence predictions are many orders below these bounds,
so the conclusions do not depend on order-one PSD conventions.

**DP radiation mapping: correction required.**  The worker's master equation
uses the standard position-space DP coefficient `-G/(2 hbar)`.  Figurato and
Donadi use `-4 pi G/hbar`
(`sources_untrusted/source_Figurato_2406.18494.clean.txt:101-150`;
`sources_untrusted/source_Donadi_2111.13490.clean.txt:138-175`), a rate larger
by `8 pi` at the same Gaussian radius.  Therefore their rounded
`R0 >= 4e-10 m` maps to about `ell >= 1.37e-10 m`, not exactly 4e-10 m, in the
worker's normalization (`scripts/r64_referee_checks.out:1-3`).  The direct
Majorana paper states `R_DP > (2.54 +/- 0.03)e-10 m`, which maps to
`8.67e-11 m` (`sources_untrusted/source_Majorana_2202.01343.clean.txt:476-506`).
Using 4 Angstrom for `ell` is conservative, but the worker's assertion that
only `gamma=1` survives there is not: the same normalization factor must enter
the gamma window.

**LPF: scope and factor-two corrections, immaterial to the exhibited window.**
There is no kernel-independent LPF force-noise floor at fixed `g`: CP constrains
the product `P_J D0`, so `P_J` may be reduced by increasing direct decoherence.
The worker's `S_a_floor` is the `gamma=1` least-decoherence prediction, not a
bound for every kernel.  Even for that prediction, one test mass, one axis, and
a one-sided PSD has prefactor `(4 pi/3)G hbar`, while the independent two-mass
differential PSD has `(8 pi/3)G hbar`.  The worker uses the latter against half
the measured differential PSD (`scripts/r64_checks.py:61,93-102`),
overconstraining by two (`scripts/r64_referee_checks.out:19`).  Its ultra-local
Cs-times-LPF `1/6` product prefactor is nevertheless correct because the squared
branch-density difference supplies the compensating factor two
(`scripts/r64_referee_checks.out:20`).

**ISL upper endpoint: not established.**  A Gaussian-smeared point potential
has fractional potential deficit `erfc(x)`, but an ISL experiment measures the
force, whose ratio is
`erf(x) - 2x exp(-x^2)/sqrt(pi)`, `x=r/(2 ell)`.  At the 52-micrometre minimum
separation, the force deficits are `3.64e-3` at 10 micrometres and `0.111` at
15 micrometres, not the worker's potential deficits
(`scripts/r64_referee_checks.out:11-18`).  Lee et al. fitted patterned,
extended-body Newtonian and Yukawa torques, not this point-potential model; they
report no smaller than 52 micrometres and an alpha=1 Yukawa limit of 38.6
micrometres (`sources_untrusted/source_Lee_2002.11761.txt:385-420,428-431`).
A dedicated geometry fit is required to claim `ell <= 1--1.5e-5 m`.

**Window conclusion.**  The exact advertised endpoints are not confirmed, but
the **VIABLE** label is: the worker explicitly exhibits a least-decoherence
kernel, and the conservative interval `4e-10 m <= ell <= 5e-6 m` is already
nonempty and safely inside both the radiation normalization and the ISL scale.
The likely lower edge in the worker's convention is about `0.9--1.4e-10 m`;
the actual upper edge remains open pending the Lee-geometry fit.

### 3. OSSW F6--F10 and the prior "32 decades"

**The worker's diagnosis is correct, including for the published paper.**  For
a local delta kernel, OSSW F6--F7 first gives the square of the *total body's*
Newtonian field integrated over the noise point
(`text/opp2203.txt:2967-3024`).  OSSW then asserts that `i=j` nuclear self terms
dominate and replaces that spatially varying field by the nuclear interior
scale throughout `V_b` (`text/opp2203.txt:3025-3069`).  This loses the coherent
`i != j` body field and its `1/r^2` falloff.  The paper consequently declares an
all-space divergence and obtains `D2 <= 1e-41`
(`text/opp2203.txt:3043-3075`).  The Nature Communications version repeats the
same equations and conclusion ([published OSSW](https://pmc.ncbi.nlm.nih.gov/articles/PMC10696068/)).

For a uniform sphere of mass `M` and radius `R`, F6 instead contains

`int d^3x' |int d^3x m(x)(x-x')/|x-x'|^3|^2 = 24 pi M^2/(5R)`.

The inside contribution is `4 pi M^2/(5R)` and the outside contribution is
`4 pi M^2/R`; the latter is finite.  Hence

`sigma_a^2 = (48 pi/5) G^2 D2/(R T)`.

For the paper's proxy values `R=0.05 m`, `T=100 s`, and
`sigma_a=1e-7 m s^-2`, this gives the illustrative upper bound
`D2 <= 3.72e5 kg^2 s m^-3`
(`scripts/r64_referee_checks.out:5-7`).  The detailed F8--F10 substitution is
too strong by `9.45e44`; relative to the paper's rounded `1e-41` headline the
new number differs by `3.72e46` (`scripts/r64_referee_checks.out:8-10`).  The
worker's "about 45 decades" is therefore a fair comparison to its reproduced
F9 arithmetic, though the rounded published headline differs by about 46.6.
The `3.72e5` value is a uniform-sphere proxy, not a replacement experimental
torsion-bound analysis; real differential geometry and correlations must be
modeled.

**Disposition of R3-4:** the numerical **32-decade empty window falls**.  Its
lower `D2` bound no longer conflicts with this corrected proxy upper bound; the
proxy leaves roughly fourteen decades rather than an empty interval.  The
qualitative statement that an exactly unregulated, homogeneous local
point-particle model fails can be retained only on the new, explicitly narrow
Corollary-U basis.  The worker's 6.2-decade Cs-times-LPF calculation is
internally consistent (`scripts/r64_checks.out:40-42`), but depends on its
nucleon/test-mass form-factor model, white noise, and ignored electrons.  It is
useful supporting arithmetic, not a literature-grade universal replacement
for the retracted 32-decade torsion squeeze.

### 4. Variant (ii) and Layton et al.

Layton et al. really do choose an ultra-local DeWitt kernel
(`sources_untrusted/source_Layton_2307.02557.clean.txt:1023-1037`) and derive the
local Newtonian action with mass decoherence and a stochastic Poisson residual
(`sources_untrusted/source_Layton_2307.02557.clean.txt:1097-1144`).  In that
Newtonian subset, `beta <= 1` supplies positivity.  They expressly state that
finite-c consistency, stability, and preservation of the Newtonian limit have
not been shown (`sources_untrusted/source_Layton_2307.02557.clean.txt:1145-1158`).

Thus the literal **unregulated local Newtonian limit**, extrapolated to point
particles at arbitrary k, is **EXCLUDED within H1--H5** by Corollary U.  It is
not valid to promote this to exclusion of every local covariant completion:
relativistic/UV terms may invalidate that extrapolation, exactly the issue
Layton et al. leave open.  Variant (ii) is therefore **OPEN overall**, as fixed
by `TESTS.md:3170-3177`.  Its published citation to experimental exclusion
(`sources_untrusted/source_Layton_2307.02557.clean.txt:1886-1896`) inherits the
failed OSSW torsion step and cannot independently restore the 32-decade claim.

### 5. Lambda and H-cosmo

`E[J]=0` proves no *additive mean source* in the linear Newtonian Poisson
equation.  It does not generally rule out noise-induced drift from
field-dependent coefficients, nonlinear metric averaging, or the stress of
fluctuations, all outside H2--H3.  The quoted `1.75e-26 J m^-3` over a Hubble
time is correctly reproduced for the **minimum**, `gamma=1`, kernel
(`scripts/r64_checks.out:50-54`); it is not the largest possible matter-side
exchange merely because Lemma F is a floor.  A more conservative universal
comparison using the entire observed Earth heat budget is still about eleven
decades below dark-energy density, subject to assuming the same per-mass
coupling cosmologically.

The H-cosmo arithmetic is reproducible, but the conclusion is conditional twice
over.  It identifies the gauge-fixed negative conformal-momentum term in OSSW
F25 (`text/opp2203.txt:3272-3299`) with a locally gravitating, secular energy
density, and it turns the 52-micrometre experiment into a hard statement
`g(k) approximately 1` up to `1/(52 micrometres)`.  Neither step has been
established.  Consequently the 6.7-decade minimum overshoot is **not an
exclusion** of variant (i); it is a diagnostic conditional on H-cosmo and a
specific response assumption.

### 6. Record reading

The Gaussian information inequality in Lemma R is a sound compatibility check,
not a record-construction theorem.  A sampled classical field history supplies
one classical value per spacetime event only after choosing events, an
unravelling, persistence, and a physical readout map.  Set A instead fixes
sites as `Z^3` nearest-neighbour sites, the one-site algebra as `M2(C)`, and a
permanent one-record-per-site rule
(`MINIMAL_AXIOMS_2026-06-29.md:35-61,75-95`).  The axioms also explicitly leave
record production, persistence dynamics, time metric, and local observability
open (`MINIMAL_AXIOMS_2026-06-29.md:173-190`).

Therefore variant (iii) is correctly described only as a **reading with
prices**, not a realization of unchanged Set A.  At minimum it prices Lattice
(`Z^3` sites become continuum events), Qubit (a commutative classical factor is
added), Admissibility (the law is no longer the fixed nearest-neighbour rule),
and Record (continuous noisy field values replace locks of one local
possibility), plus a new source/readout/permanence bridge.  The worker identifies
the first four prices (`R6-4_report.md:241-250`) but states the block-record
identification too categorically (`R6-4_report.md:237-239`).

### 7. Fixed readings and labels

| Variant | Referee reading | Strongest warranted basis |
|---|---|---|
| (i) Smeared Newtonian CQ | **VIABLE** | An explicit least-decoherence kernel passes the stated bounds on a conservative nonempty subwindow, at least `4e-10` to `5e-6 m`; the exact lower normalization is nearer `0.9--1.4e-10 m`, and the true ISL upper edge needs a geometry fit. Prices H1--H6 and P-i1--P-i4 remain. H-cosmo is not an exclusion. |
| (ii) Covariant CQ-GR candidate | **OPEN overall** | Its literal cutoff-free local Newtonian point-particle limit is **EXCLUDED within H1--H5**, but the full finite-c/UV theory is not. |
| (iii) Metric history as records | **Reading with prices** | Compatible with `V <= BC`, but requires changes to Lattice, Qubit, Admissibility, Record, and an explicit readout/permanence bridge. |

These preserve the fixed rule in `TESTS.md:3170-3177`.  No fixed reading was
edited.  A positive gravity-mediated-entanglement result remains a falsifier of
the classical-channel subclass, subject to the exact channel assumptions of
the earlier Lemma N.

## Strongest correct statement

Within homogeneous Markovian Gaussian continuous CQ Newtonian gravity with
additive direct and feedback dephasing, complete positivity enforces
`P_J D0 >= |g|^2/4` and hence the standard DP least-decoherence floor; exact
unsmeared coupling to point masses then has cubic UV heating, whereas a Gaussian
smeared model has an explicit, experimentally unexcluded nonempty window (a
conservative demonstrated subwindow is about 4 Angstrom to 5 micrometres, with
the lower conversion convention-dependent and the upper endpoint awaiting a
dedicated ISL geometry fit).  OSSW's F8--F10 replacement of the total body's
falling field by a nuclear interior field over `V_b` is invalid in both the
preprint and published paper, so the R3-4 "32-decade empty window" falls rather
than merely shifts; only the narrower cutoff-free point-particle exclusion and
model-dependent supporting bounds survive.  Layton et al.'s unregulated local
Newtonian limit lies in that narrow excluded class, but its covariant finite-c
completion remains open, the H-cosmo overshoot is conditional rather than an
exclusion, and treating the classical metric history as Set-A records requires
explicit changes to Lattice, Qubit, Admissibility and Record plus a
readout/permanence bridge.
