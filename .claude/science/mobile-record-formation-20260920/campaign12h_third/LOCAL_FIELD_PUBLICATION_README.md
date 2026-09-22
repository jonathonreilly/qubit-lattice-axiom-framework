# Mobile permanent records: a prepared local field limit

This draft packages one conditional result: a specified quantum model of
records moving through vacancies generates gauge-loop dynamics, while fresh
record formation remains enabled. With a supplied local preparation and a
decreasing formation rate, the field in any fixed small region approaches
the loop dynamics uniformly as the surrounding cubic lattice grows.

The scientific sources have independent reconstruction and comparison
coverage. They are not formally audited or retained. This branch does not
change the framework's axioms, adopt its extra structures, or establish a TOE.
The original author notes and evidence are frozen byte-for-byte; their
historical “independent reconstruction pending” lines precede the final
comparisons linked below.

## Read the claim and its premises together

1. [Hard-core motion and the fourth-order loop](HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md)
   derives the normalized coefficient, the constant diagonal contribution,
   the dependence on statistics, and a fixed-volume live-formation limit.
2. [Homogeneous field-star penalty](HOMOGENEOUS_FIELD_STAR_PENALTY_FOR_MOBILE_RECORDS.md)
   replaces the explicitly staggered energy penalty by a homogeneous
   field-divergence penalty. The selected background and initial sector
   still have a checkerboard pattern.
3. [Uniform local field dynamics](UNIFORM_LOCAL_RING_DYNAMICS_WITH_SLOW_RECORD_FORMATION.md)
   supplies the finite-depth preparation and proves the local, uniform-volume
   comparison, including the full birth backaction.
4. [Uniform record density](UNIFORM_RECORD_DENSITY_WITH_LIVE_FORMATION.md)
   separately bounds the mean amount of formation. Its small-density result
   alone is not a field-dynamics theorem.

The local-field theorem uses fixed dimension d >= 2 and a cubic torus with
all sides even and at least six. Every matter site has three orthogonal states: vacancy, a plus
record, and a minus record. Every link has a separate spin-half quantum
degree of freedom. A record's charge/content is unchanged by hopping; there
is at most one record per matter site. Initially, identical bosonic plus
records occupy one sublattice and the other is vacant. No individually
readable identity tags are included.

With an oriented link \(e:x\to y\), \(a^\dagger_{x,q}=|q\rangle\langle0|\),
and the partial spin-half raising operator \(U_e\), the supplied motion is

\[
 T=-\sum_{e,q}\big(a^\dagger_{y,q}a_{x,q}U_e^{-q}+{\rm h.c.}\big).
\]

Here the exponent denotes raising or lowering, not an inverse of a unitary.
The supplied Gauss sector is

\[
 \operatorname{div}E_x+1_A(x)-q_x=0.
\]

For clarity, the birth maps referred to by the notes are

\[
 j_{e,\sigma}=a^\dagger_{x,\sigma}a^\dagger_{y,-\sigma}U_e^\sigma,
 \qquad \sigma=\pm1.
\]

They act only on two vacancies. One may use the two charge-resolved jumps,
each at strength \(\sqrt\beta\), or the single coherent jump
\(\sqrt\beta(j_{e,+}+j_{e,-})\). Their total loss is
\(\beta P_{{\rm vac},e}\). Including two coherent signs at that same strength
would double the rate and is not this convention. The independent physical
sector builder reconstructs these maps directly.

Quantum amplitudes, the clock, bosonic statistics, link tensor factors,
background/Gauss sector, Hamiltonian, and initial preparation are supplied.
These are not consequences established here from one possibility qubit per
native site or from the static conditional content rule.

## Exact scope of the strongest result

Set \(\epsilon=t/\Delta\), fix \(J>0\), and use

\[
 \Delta=\frac{J}{2\epsilon^4},\qquad
 t=\frac{J}{2\epsilon^3},\qquad
 \beta=\beta_0\epsilon^{2d}.
\]

There is a number- and Gauss-preserving circuit whose depth and range do not
grow with volume. Start in its prescribed dressing of any ice-field density,
including correlated states. For every bounded local field observable and
fixed time interval, its expectation under the complete open dynamics differs
by \(O(\epsilon)\) from the pure loop Hamiltonian

\[
 H_{\rm ring}=-J\sum_p(W_p+W_p^\dagger),
\]

with a constant independent of the surrounding volume. The proof uses a
finite-order local normal form, a finite-range Lindblad locality estimate,
and a state-dependent bound that includes both jumps and waiting without a
jump. It does not condition the actual process on having no births anywhere.

Formation is positive at every finite parameter value when \(\beta_0>0\),
but decreases to zero in this limit. The theorem does not cover an undressed
quench, fixed positive formation rate, growing time windows, a practical
native preparation circuit, or a photon/Coulomb phase. It does not show a
stationary phase with nonzero continuing record production.

## Independent coverage and preserved failures

The [hard-core/density/star comparison](hardcore_live_density_independent/COMPARISON.md)
covers the first, second, and fourth notes, after its
[blind reconstruction](hardcore_live_density_independent/REPORT.md).
Its final source seal is
\(656e03ef2bc63bb3aafa27741bd0f2db9cb7df0f292eb84359f9b6a478df26b0\).

The [uniform-local comparison](uniform_local_dynamics_independent/COMPARISON.md)
covers the third note, after a different
[blind local-dynamics reconstruction](uniform_local_dynamics_independent/REPORT.md).
Its final seal is
\(cc213db7ba3b00cce3ae52d8206878219257bda27b831bfdad93129a9dbcafcf\).
It independently recompiles the stored rational gate series and checks the
stronger formation schedule. Neither comparison requested a source correction.
The original PRE seals are unchanged.

These are selective scientific checks, not a new formal audit verdict.
Numerical high-precision exponentials in the author tables are authenticated
and their table arithmetic checked by the reviewer; they were not independently
rerun. Uniform-volume conclusions come from the complete locality proofs,
not from the small matrix examples.

Failures remain in their original evidence directories. In particular, an
initial guessed remainder threshold failed; its replacement derives the exact
first omitted coefficient. Integer-dtype, structural-equality, and floating
replay helper failures are also preserved with their diagnoses.

## Reproduction and source portability

The [publication manifest](PUBLICATION_UNIT_LOCAL_FIELD.json) maps every
copied artifact to its original path, byte count, and SHA-256. It also lists
context-only references and downloaded primary sources intentionally omitted
from this publication. No third-party PDF or HTML source is redistributed.
Primary-source URLs, versions, read scope, and download identities remain in
the corresponding receipts. The geometric helper is included unchanged
because the ring runner imports its cubic-graph builder; its unused cooling
routines are not additional claims of this unit.

From this directory, run:

    python3 verify_local_field_publication.py

This validates the manifest against this checkout without using the author's
absolute filesystem paths. It checks bytes and provenance, not mathematics.

The scientific runners require Python, NumPy, SciPy, SymPy, and mpmath. The
recorded runtime uses Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1, and SymPy
1.14.0. The author runners are:

    python3 hardcore_record_ring_and_formation_check.py
    python3 record_density_and_fast_defect_check.py
    python3 homogeneous_field_star_record_check.py
    python3 local_normal_form_record_check.py
    python3 finite_circuit_normal_form_record_check.py

Run them in a disposable copy: they write result files beside their source,
including timestamps, and would replace the frozen evidence in this checkout.
The independent pre-comparison algebra can be reproduced from its own
fourth_order_paths.py, finite_sector_check.py, density_bound_check.py, and
normal_form_check.py in the respective independent directories.

Historical post-seal comparison/sealing utilities deliberately retain original
absolute paths and primary-source-cache checks. Directly rerunning those
utilities in another checkout requires an explicit path/cache remapping.
The portable verifier does not pretend to have repeated those original
comparisons.

This draft is an addition on top of main, with no generated audit-state
changes. Any future landing still needs the repository's current-base
integration checks and final publication-surface review.
