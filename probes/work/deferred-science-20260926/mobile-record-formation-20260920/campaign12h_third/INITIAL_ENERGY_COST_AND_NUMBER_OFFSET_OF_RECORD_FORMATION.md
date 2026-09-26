# Initial formation, energy injection, and a number-energy ambiguity

Status: author conditional calculation, independent check pending. This is a
diagnostic of the supplied spin-half record model and its specified prepared
family. It is not an impossibility theorem for fresh records, a statement
about all possible baths, or an integrated long-time heating result.

## 1. Precise initial-state calculation

Use the hard-core bosonic qutrit matter and spin-half links of
HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS.md, on an even cubic torus of
side at least six in fixed dimension \(d\). Let \(V\) be its site count,
\(M=dV/2\), and

\[
 H=\Delta N+tT,\qquad \epsilon=t/\Delta,\qquad
 J=2\Delta\epsilon^4.                                             \tag{1}
\]

For the sublattice model \(N=N_B\). For the homogeneous field-star model
\(N=N_{A,-}+N_{B,+}\), equal to \(\frac12\sum_x(\operatorname{div}E_x)^2\)
on the stipulated physical charge sector. Do not confuse this penalty \(N\)
with the total record number, denoted \(\mathcal N\) below.

Start from any ice density \(\rho=P\rho P\), including correlated or coherent
field states, and use the finite local preparation

\[
 \rho_\epsilon=Y_\epsilon^\dagger\rho Y_\epsilon                  \tag{2}
\]

from the now independently compared uniform-local packet. Its fixed-order
normal form, locality, parity, and number/Gauss preservation are reused.
The Hamiltonian and jumps themselves are the original supplied ones.
Let \(j_f\) denote a normalized birth operator on bond \(f\), either the
single coherent charge refinement or its two resolved channels. The
corresponding total loss is \(P_{{\rm vac},f}\) for spin-half links.
The birth strength is \(\beta>0\).

Define the instantaneous event rate and Hamiltonian-energy derivative at
this initial state:

\[
 {\cal R}_\epsilon=\beta\sum_f
          \operatorname{Tr}(j_f^\dagger j_f\rho_\epsilon),\qquad
 {\cal P}_\epsilon=\beta\sum_f
          \operatorname{Tr}({\cal D}_{j_f}^*(H)\rho_\epsilon).
                                                                    \tag{3}
\]

There is no Hamiltonian contribution to the derivative of its own energy.
At fixed dimension, as \(\epsilon\to0\),

\[
 \frac{{\cal R}_\epsilon}{V}
  =\beta\frac d2(2d-1)\epsilon^2+O(\beta\epsilon^4),                \tag{4}
\]
\[
 \frac{{\cal P}_\epsilon^{\,B}}{V}
  =\beta\Delta\,d(2d-1)\epsilon^2+O(\beta\Delta\epsilon^4),         \tag{5}
\]
\[
 \frac{{\cal P}_\epsilon^{\,\star}}{V}
  =\beta\Delta\,\frac d2(4d-3)\epsilon^2
                         +O(\beta\Delta\epsilon^4).               \tag{6}
\]

The remainder bounds in these density statements are uniform in volume and
in the initial ice density. They concern the initial derivative of (2);
no replacement of later states by (2) is assumed.

## 2. Derivation of the source and coefficients

Every code configuration has exactly \(d\) outgoing positive-flux edges
from each A site. A positive A record can hop to its vacant B neighbor along
each such edge, giving \(M\) eligible first hops. The first-order dressing is
minus the hopping amplitude divided by the unit penalty gap. Since \(j_fP=0\),

\[
 Y_\epsilon j_fY_\epsilon^\dagger P
       =-\epsilon j_fTP+O_{\rm local}(\epsilon^2).                \tag{7}
\]

After a hop \(e\), the emptied A site has \(2d-1\) other vacant B neighbors.
Formation on one of those bonds is allowed in exactly one charge orientation.
Of these choices,

* \(d\) create A-plus and B-minus, leaving the first transported plus
  record on B; their field-star penalty is \(1\);
* \(d-1\) create A-minus and B-plus, leaving two positive B records and
  one negative A record; their field-star penalty is \(3\).

Every output has two occupied B sites, so its sublattice penalty is \(2\).
This counting applies to every ice configuration, not just to an averaged
classical ensemble.

For a fixed observed birth bond \(f\), different prior hopping edges have
orthogonal output matter patterns. In the A-plus channel, the extra positive
B record identifies that hopping edge. In the A-minus channel, the birth
bond identifies one of the two positive B records and the other identifies
the hopping edge. The two charge channels are orthogonal. Once these edges
and the final field are known, undoing their two flips uniquely recovers
the initial field. There are consequently no uncounted interference terms,
even for coherent initial ice superpositions. With \(B_f=-j_fTP\),

\[
 \sum_f B_f^\dagger B_f=M(2d-1)P,\quad
 \sum_f B_f^\dagger N_B B_f=2M(2d-1)P,                            \tag{8}
\]
\[
 \sum_f B_f^\dagger N_\star B_f=M(4d-3)P.                         \tag{9}
\]

For resolved instruments the sum includes both charge labels. For the one
coherent refinement the same identities hold because the two output charge
patterns are orthogonal.

The transformed Hamiltonian satisfies

\[
 \Delta^{-1}Y_\epsilon HY_\epsilon^\dagger
     =N+\epsilon^2D_2+\cdots,\qquad
       PD_2P=-MP.                                                \tag{10}
\]

In the gain term of the transformed dissipator, inserting (7) and the
leading \(N\) gives \(\Delta\epsilon^2B_f^\dagger N B_f\).
The anticommutator is included: its expectation on the code first contributes
at order \(\Delta\epsilon^4\), since the transformed Hamiltonian on the code
starts at order \(\Delta\epsilon^2\), and its loss expectation starts at
order \(\epsilon^2\). The block-off-diagonal Hamiltonian remainder of the
chosen higher-order preparation does not change this leading coefficient.
Equations (8)-(10) give (4)-(6).

For completeness, these estimates can be made local before taking a density.
The adjoint dissipator on \(H\) is a sum over overlapping hopping/penalty
terms, because a birth term commutes with every disjoint Hamiltonian term.
There are a bounded number of these contributions per site. Conjugation by
the finite circuit leaves each in a bounded light cone and gives a uniformly
analytic function of \(\epsilon\). On the code, the constant and linear
coefficients vanish and the quadratic coefficient is the one just computed.
Conjugation by \(e^{i\pi N}\) implements \(\epsilon\mapsto-\epsilon\)
for the circuit and the Hamiltonian. Each sublattice birth has odd penalty
grade; each star birth has even grade. In either case its dissipator is
unchanged. Since the code has grade zero, the cubic coefficient vanishes.
A fixed-radius Cauchy remainder bound gives \(O(\epsilon^4)\) per indexed
local term. Summing and dividing by \(V\) proves the stated uniform density
remainders without assuming a product initial field state.

## 3. What the fixed-energy convention says

With the Hamiltonian in (1) fixed as written, the leading energy per
initial birth is

\[
 \frac{{\cal P}^{\,B}}{{\cal R}}
       =2\Delta+O(\Delta\epsilon^2),\qquad
 \frac{{\cal P}^{\,\star}}{{\cal R}}
       =\frac{4d-3}{2d-1}\Delta+O(\Delta\epsilon^2).               \tag{11}
\]

At fixed ring strength \(J\), the star expression becomes

\[
 \frac{{\cal P}^{\,\star}_\epsilon}{V}
       =\frac{\beta Jd(4d-3)}{4\epsilon^2}+O(\beta J).             \tag{12}
\]

Within this convention and initial family, a uniformly bounded initial
energy-injection density requires \(\beta=O(\epsilon^2)\); then the
initial event density is \(O(\epsilon^4)\). Conversely, choosing
\(\beta\asymp\epsilon^{-2}\) keeps the leading initial event density finite
and positive while the stated energy derivative grows as \(\epsilon^{-4}\).
This arithmetic does not prove that all finite-rate formation schemes heat,
nor that a later-time formation density obeys the same expression.

It also does not identify an observable energy cost until the following
number-energy freedom is fixed.

## 4. Exactly unchanged histories under a number-energy offset

The supplied processes obey

\[
 [H,\mathcal N]=0,\quad [\Gamma,\mathcal N]=0,\quad
 [\mathcal N,j_f]=2j_f.                                          \tag{13}
\]

For any real \(\mu\), replace the Hamiltonian by

\[
 H_\mu=H+\mu\mathcal N.                                          \tag{14}
\]

For every initial density block diagonal in total record number, the entire
marked quantum trajectory instrument is unchanged. To see this, a no-event
propagator in a number-\(n\) block acquires just the scalar phase
\(e^{-i\mu n s}\). Its action on a density cancels that phase. A birth maps
that block to number \(n+2\). Induction over all event times and labels gives
identical conditional densities and event probabilities; summing histories
also gives identical unconditional densities. The initial family (2) meets
this hypothesis because its dressing preserves record number.

This is stronger than equality of a few count moments, but does not cover
an initial coherence between different number sectors with an observable
sensitive to its relative phase.

The energy derivative, however, changes exactly:

\[
 {\cal P}_{\epsilon,\mu}
        ={\cal P}_\epsilon+2\mu{\cal R}_\epsilon,                  \tag{15}
\]

because \({\cal D}^*(\mathcal N)=2\sum_fj_f^\dagger j_f\).
Choosing a penalty-scale \(\mu\) can therefore cancel, reverse, or enhance
the leading mean in (11) while leaving the model's recorded histories
unchanged. The chemical-potential/record-rest-energy convention must be fixed
by extra physical information before calling (12) a measured heat flow.
Equations (4)-(6) remain correct for their specified Hamiltonians.

## 5. A channel energy separation that the uniform offset does not remove

The leading star source has penalty values \(1\) and \(3\), with conditional
weights \(d/(2d-1)\) and \((d-1)/(2d-1)\). Its variance is

\[
 \operatorname{Var}(N_\star\mid{\rm initial\ birth})
      =\frac{4d(d-1)}{(2d-1)^2}.                                 \tag{16}
\]

At fixed finite volume, the limiting distribution of the post-birth
Hamiltonian divided by \(\Delta\) has this same two-point form: the hopping
term divided by \(\Delta\) has norm tending to zero, and the normalized
source tends to the mixture specified by (7)-(9). Initial low-sector
energies divided by \(\Delta\) also tend to zero. Thus its leading
transition-energy variance is

\[
 \Delta^2\frac{4d(d-1)}{(2d-1)^2}+o(\Delta^2).                    \tag{17}
\]

An offset (14) shifts both birth energy changes by \(2\mu\), and cannot
change their separation or variance. In three dimensions the coefficient
is \(24/25\); in one dimension the second channel is absent and the
coefficient is zero. The sublattice model has a single leading penalty
value \(2\), so (16) is specifically a field-star diagnostic.

This distributional statement is fixed-volume. The uniform mean-density
argument of Section 2 is not silently promoted to a uniform variance theorem
for extensive energy in arbitrary correlated states. Further microscopic
reservoir assumptions would be needed to turn (17) into an apparatus-resource
bound. No such bath theorem is claimed here.

## 6. Checks and disposition

record_formation_energy_check.py enumerates actual local hopping and
formation outputs on six-site-periodic one-, two-, and three-dimensional
tori. For dimensions two and three it also uses two distinct ice fields
related by a plaquette flip and computes both off-diagonal Gram elements.
The exact source and energy Grams are scalar on these controls. The
three-dimensional case has \(V=216\), \(M=324\), 1620 leading source outputs
per tested field, of which 972 have star penalty one and 648 have penalty
three. The exact mean is \(9/5\) and variance \(24/25\).

The runner separately builds the complete nine-state physical square,
diagonalizes the actual original-number Hamiltonian, and evaluates all gain
and anticommutator terms in (3). It checks (15) at four number-energy offsets
for each parameter and penalty. These finite eigenvector controls use floating
arithmetic; they are not a substitute for the uniform local expansion.
The first successful source/mean-energy run is preserved before adding the
offset and variance controls. Neither run failed a scientific assertion.
Complete source, results, stdout, stderr and receipts are bound by the author
seal.

This note refines the interpretation of the earlier energy-source controls:
the specified generators permit a calculable initial energy derivative, but
record histories alone do not fix the relative energy zero of different
record-number sectors. Sustained finite-rate formation, its physical energy
accounting, and its influence on long-wavelength field dynamics remain open.
