# NT-1″ independent referee record

## VERDICT: CONFIRMED WITH CORRECTIONS

The correct fixed campaign reading is **OPEN**.  Item (b″) is not met and, for
the Wilson kernel and open-time boundary condition actually used here, cannot
be met: every degree-one winding of the spatial Wilson-line circle encounters
an exact boundary-supported zero of $H_W$.  The fixed wording explicitly
requires transport around at least one admissible non-contractible loop, so
componentwise/vacuous integrability cannot count as a pass
(`TESTS.md:491-499`).

I independently confirm the worker's bulk numerical result for (b′), including
ν = 0.8691 ± 0.0644 and the L1 $1/L_x$ contrast.  I also confirm that the
saved clean-background edge data are extremely well described by $L_x^{-5}$
over the tested large sizes.  The latter means that (b′) passes only the
registered **bulk proxy**; it does not establish the uniform finite-volume
locality bound that motivated G-LEG(b).  The elementary divergence argument
does show that no gauge-invariant Ward current can cancel the anomaly's remote
Wilson-line response on every adjacent link.  What is not proved is the
asymptotic premise that the measured anomaly response has an algebraic lower
bound for all sufficiently large $L_x$; the data stop at $L_x=24$.  Thus the
universal statement "no measure on this geometry can be uniformly
exponentially local" remains strongly supported, not proved, exactly as the
worker ultimately labelled it at `REPORT.md:69-71`.

The corrections are therefore scope corrections, not a change of headline:

1. The "iff" zero-mode lemma is an iff statement for a mode supported wholly
   on the top or bottom row.  It does not exclude unrelated bulk-supported
   zeros at other fields.
2. Removing the forced zero points makes each fixed-plaquette Wilson-line
   fibre a union of intervals; the stronger claim that every full admissible
   component is contractible was not proved and is unnecessary.
3. The $L_x^{-5}$ law and the attribution of its exact power to edge states
   are finite-range numerical conclusions.  Bulk-edge physics explains the
   mechanism, but does not by itself prove that precise asymptotic power.
4. Periodic time is a valid and natural repair route, not a logical uniqueness
   theorem: a different boundary termination that gaps/removes the edge
   obstruction would also be new geometry and would require all gates to be
   redone.

## Correct fixed reading

| Fixed item | Referee reading | Reason |
|---|---|---|
| (b′), literal registered numerical proxy | **MET for the bulk statistic** | Four accepted sizes, ν/σ = 13.49, and $L_xP_{L1}$ constant within 8.2%. |
| (b′), intended Lüscher-uniform finite-volume locality | **NOT ESTABLISHED** | The same current/anomaly family has an algebraic-looking remote edge response; no uniform position-independent exponential bound is shown. |
| (b″) | **NOT MET AS WORDED; unmeetable on this open strip** | No admissible degree-one Wilson-line loop exists, while the fixed rule requires one. |
| Kernel step | **Correctly not triggered** | Both (b′) and (b″) had to pass (`TESTS.md:496-499`; `PREREG.md:143-146`). |
| Overall | **OPEN, naming (b″)** | This is forced by the fixed rule even if the literal bulk proxy for (b′) is accepted. |

Consequently NT-1′'s G-LEG(b) is still not closed on the open strip.  The old
negative matrices remain legitimate chart-local evidence, but they still do
not become a fixed-rule `CHI-RP-FAIL` result.

## Materials and independent checks

I read the fixed wording, the predecessor report and referee record, all of
`REPORT.md` and `PREREG.md`, every `nt1pp_*.py` file, the unchanged
`nt1p_lib.py`, the relevant saved outputs, and the torus support code.  I wrote
one small independent checker, `referee_checks.py`, and ran it once at a time
through `./capped.sh` with two numerical threads.  Its peak RSS was 114832 kB
(`referee_checks.out:13`).

The independent checks were deliberately different from merely rerunning the
worker scripts:

- explicit construction of covariantly constant one-row top and bottom
  spinors on nonuniform random gauge fields;
- a fresh weighted fit from the saved per-configuration arrays;
- fresh exponential and power fits to the saved large-$L_x$ edge data;
- a two-by-two Bloch-band FHS calculation, rather than the worker's full
  finite-torus occupied-subspace determinant;
- a direct check of the fundamental-theorem identity relating the integrated
  Wilson response `hbar` to the full anomaly difference.

## 1. Edge-zero-mode lemma

### Algebra

The implementation has diagonal Wilson term 2, mass $M=1$, spatial forward
and backward blocks $-\frac12(1\mp\gamma_x)$, and an antiperiodic factor on
the wrapping spatial hop (`scripts/nt1p_lib.py:17-45,65-79`).  On a fixed
boundary row let $T_x$ be the covariant spatial shift, including that wrapping
minus sign.  Its eigenvalues are $e^{ik'}$, with

\[
  k' = \frac{(2n+1)\pi+eW_{\rm edge}}{L_x}\quad (\mathrm{mod}\ 2\pi).
\]

For a spinor supported only on the top row, choose
$\gamma_t\chi=+\chi$.  The only matrix element that could create a component
one row inward is proportional to $1-\gamma_t$, hence vanishes.  On the
bottom row the corresponding choice is $\gamma_t\chi=-\chi$, killing the
$1+\gamma_t$ block.  The remaining row operator is exactly

\[
 (D-1)\psi
 =\left[1-\tfrac12(1-\gamma_x)e^{ik'}
          -\tfrac12(1+\gamma_x)e^{-ik'}\right]\chi
 =\left(1-\cos k' + i\gamma_x\sin k'\right)\chi .
\]

Moreover,

\[
 \left\|\left(1-\cos k'+i\gamma_x\sin k'\right)\chi\right\|^2
 =4\sin^2(k'/2)\,\|\chi\|^2.
\]

Thus a wholly boundary-supported zero exists iff $k'=0$ modulo $2\pi$,
which is equivalent to

\[
 eW_{\rm edge}=\pi\pmod{2\pi}.
\]

This derivation uses no interior link or plaquette.  For a nonuniform boundary
field the plane wave is simply replaced by the covariantly constant eigenvector
of $T_x$; only the boundary holonomy enters.  This proves the advertised
"for any plaquettes" statement for the boundary-supported mode
(`PREREG.md:251-254`; `REPORT.md:31-34`).

### Independent numerical checks

I tuned the top Wilson line of a nonuniform random $L_x=4,L_t=8$ field for
charge 1 and constructed the analytic $\gamma_t=+1$ edge vector.  I separately
tuned the bottom Wilson line of another nonuniform field for charge 2 and used
$\gamma_t=-1$.  The results were

| Case | ∥$H_W\psi$∥ | min ∥eig $H_W$∥ |
|---|---:|---:|
| top, $e=1$ | 1.90e-16 | 2.26e-16 |
| bottom, $e=2$ | 6.38e-17 | 1.33e-15 |

See `referee_checks.out:7-8` and the independent construction at
`referee_checks.py:11-52`.  The worker's zero-field scan and random-field
crossings are consistent: `scripts/B2A_Lx4.out:2-18`,
`scripts/B2A_Lx6.out:2-12`, and `scripts/B2A_Lx8.out:2-12`.

### Consequence for winding loops

A degree-one loop in the spatial Wilson-line circle makes the edge holonomy a
degree-one map to $S^1$, so it is surjective and hits $W_{\rm edge}=\pi$.
The charge-1 fermion alone therefore forces a zero; charge 2 adds crossings at
$W_{\rm edge}=\pi/2,3\pi/2$.  Allowing the plaquettes to move inside their
principal admissible cell does not change the winding degree of the edge
holonomy.  Hence every loop of the type demanded in (b″), not merely the 39
sampled representatives, leaves the gapped overlap domain.  The reported
counts 0/17, 0/11, 0/11 are correct but logically secondary to the lemma
(`scripts/nt1pp_b2a.py:31-60`; `scripts/B2A_Lx4.out:19`;
`scripts/B2A_Lx6.out:13`; `scripts/B2A_Lx8.out:13`).

### Is this known Chern-insulator behavior?

Yes, with one qualification.  Fourier transformation of the periodic bulk
gives

\[
 H_W(k)=\sin k_t\,\sigma_1-\sin k_x\,\sigma_2
       +(1-\cos k_x-\cos k_t)\sigma_3,
\]

whose bulk norm obeys
$|d|^2=1+2(1-\cos k_x)(1-\cos k_t)\ge1$.  This is the two-band Wilson/Qi-Wu-
Zhang Chern-insulator Hamiltonian.  Open boundaries supporting chiral Wilson-
fermion edge spectra are standard bulk-edge behavior; see S. Sen,
[*Phys. Rev. D* **102**, 094520 (2020)](https://doi.org/10.1103/PhysRevD.102.094520)
and Kaplan--Sen, [*Phys. Rev. Lett.* **132**, 141604
(2024)](https://doi.org/10.1103/PhysRevLett.132.141604).  The exact one-row
localization and the crossing pinned at the stated holonomy are special to the
present $M=r=1$ termination; the existence of edge spectral flow is the
general topological feature.

**Item 1 finding: confirmed, with the "iff" restricted to the explicitly
boundary-supported mode.**

## 2. Meaning of (b″)

The fixed sentence is existential, not universal: transport must be performed
around closed Wilson-line loops "including at least one non-contractible loop"
and must give trivial phase for 11112 while the anomalous control fails
(`TESTS.md:495`).  A statement that every existing admissible loop is
integrable does not supply the required non-contractible example.  Nor can the
L1 control fail the requested transport test when it is blocked by the same
edge zero.  The worker therefore applied the fixed rule correctly in
`PREREG.md:52-56,73-80` and `REPORT.md:74-80`.

At fixed admissible plaquettes, deleting the forced holonomy zeros cuts the
Wilson circle into intervals.  A straight-ray basis is integrable on the
particular contractible chart it covers, as already established in the
predecessor (`NT1P_REFEREE.md:206-229`).  That is useful substantive
information, but it neither passes the explicit (b″) test nor proves that every
full admissible component is contractible; other spectral-zero loci could
puncture a component.

**Item 2 finding: (b″) is unmeetable on this geometry and OPEN is forced.
Vacuous/componentwise integrability does not pass the fixed wording.**

## 3. Item (b′), bulk and edge

### Bulk proxy

Reloading `scripts/e1_Lx{4,6,8,10}.npy` and independently repeating the stated
weighted regression gives

\[
 \nu=0.869110,\qquad \sigma_\nu=0.064442,
 \qquad \nu/\sigma_\nu=13.49,
\]

with $L_xP_{L1}=(0.03510,0.03857,0.03948,0.03971)$
(`referee_checks.out:9`).  This reproduces `scripts/E1_FIT.out:1-6` and the
per-size means in `scripts/E1_Lx4.out:14`, `scripts/E1_Lx6.out:14`,
`scripts/E1_Lx8.out:14`, and `scripts/E1_Lx10.out:16`.  All four sizes have six
accepted fields except that two additional $L_x=10$ draws were rejected by
the pre-set gap/index gate.  The extra worker condition L1/11112 ≥ 10 misses
at $L_x=4$ (9.8), but that condition is not in the parent fixed wording.

The deterministic zero-plaquette central statistic provides a useful second
check: its local exponential rate stays near 0.83--0.75 through $L_x=22$,
while the central monopole response approaches $\ln2$
(`scripts/SUMMARY_E2_W0.3_Lt8.out:2-7,17-18`).  These data justify the phrase
"exponential bulk tail on the tested backgrounds."

### Edge tail

The saved edge statistic decreases from $1.699\times10^{-7}$ at $L_x=16$
to $2.262\times10^{-8}$ at $L_x=24$.  My independent fit on those five
points gives

\[
 p=4.9738,
 \quad \mathrm{RSS}_{\rm power}=4.32\times10^{-5},
 \quad \mathrm{RSS}_{\rm exp}=7.90\times10^{-3},
\]

so the finite-range description $L_x^{-5}$ is excellent
(`referee_checks.out:10`; raw table `scripts/SUMMARY_E2_W0.3_Lt8.out:8-16`).
The local rates fall from 0.290 to 0.218 over $L_x=16\to24$, while rate times
the midpoint is 4.93--5.03.  The edge `hbar` anomaly response has the same
pattern.  This is not a finite-difference artifact in the saved range: the
lean derivative agrees with the original at machine precision
(`scripts/nt1pp_lean_check.py:6-10`; `scripts/LEAN_CHECK.out:1-2`), and $L_x=16$
was reproduced (`PREREG.md:216-223`).

It remains a numerical finite-size statement, not a rigorous asymptotic bound.
The closing edge gap supplies a compelling mechanism, but neither the gap
$\sim1/L_x$ nor bulk-edge correspondence alone fixes the cancellation order to
be exactly $L_x^{-5}$.

### The "any current" argument

The report states the result but omits its derivation (`REPORT.md:69-71`).  The
correct short argument is as follows.  On the zero-plaquette family, put the
change of Wilson holonomy on a spatial seam at the antipode of a chosen edge
site; gauge invariance makes this equivalent to the uniform representative
used by the code.  If $j$ is a gauge-invariant Ward current,
$\partial^*j=\mathcal A$, then between holonomies 0 and $W$,

\[
 \partial^*\bigl[j(W)-j(0)\bigr]
 =\mathcal A(W)-\mathcal A(0)=W\,\bar h(W).
\]

The last equality is the fundamental theorem of calculus for the integrated
Wilson response at `scripts/nt1p_lib.py:243-269`.  I checked it directly at
$L_x=8,W=0.3$; the maximum residual is $2.02\times10^{-11}$
(`referee_checks.out:12`; independent check
`referee_checks.py:123-139`).  At a site, the divergence is a signed sum over
at most four incident links, hence

\[
 \max_{\ell\ni x}|j_\ell(W)-j_\ell(0)|
 \ge \frac{|W\bar h_x(W)|}{4}.
\]

(At an open edge the coordination is three, so $1/4$ is conservative.)  A
divergence-free counterterm can redistribute this response but cannot cancel
it on every incident link.  If a volume-independent exponential locality bound
held, moving the holonomy change to the antipodal seam would instead bound the
left side by a constant (or, for the whole seam, an $L_t$ factor) times
$e^{-L_x/(2\rho)}$.  Therefore an actual algebraic lower bound on
$\bar h_x$ would rule out every such local Ward current, not only the
particular right inverse $Q$.

The logical qualifier is important: the code demonstrates an algebraic-looking
sequence through $L_x=24$; it does not prove an asymptotic lower bound.  Thus
the structural inheritance lemma is correct, but the universal no-measure
conclusion is conditional on extrapolating that sequence (or on supplying an
analytic edge-response asymptotic).  It is also scoped to differentiable,
gauge-invariant currents satisfying the Ward identity, which is the relevant
Lüscher class.

**Item 3 finding: the E1 bulk fit and finite-range edge $L_x^{-5}$ behavior
are confirmed.  The literal bulk proxy passes; a uniform Lüscher bound is not
established.  The current-inheritance lemma is correct with the finite-$W$
normalization above, but it does not turn finite $L_x\le24$ data into an
asymptotic theorem.**

## 4. Torus Chern numbers

For the periodic bulk Hamiltonian above, the positive-energy band has Chern
number $-1$ in the worker's $(w_x,w_t)$ orientation.  My independent
two-band FHS calculation gives $-1.000000000000$
(`referee_checks.out:11`; `referee_checks.py:90-120`).  Charge $e$ makes the
toron map cover the Brillouin torus $e^2$ times, so

\[
 C_L(e)=-e^2,\qquad C_R(e)=+e^2.
\]

It follows independently that

\[
 C(11112)=4C_L(1)+C_R(2)=-4+4=0,
 \qquad C(L1)=C_L(1)=-1.
\]

The worker's full finite-torus calculation agrees at grids 16, 24 and 32
(`scripts/B2C_Lx4_Lt4_g16.out:1-6`,
`scripts/B2C_Lx4_Lt4_g24.out:1-6`,
`scripts/B2C_Lx4_Lt4_g32.out:1-6`).  The opposite sign between the reported L1
Berry-phase winding $+1$ and Chern number $-1$ is just the orientation used
for the loop versus the plaquette curvature (`scripts/nt1pp_b2c.py:35-47`).

Vanishing Chern number proves triviality of the determinant line bundle over
the toron torus.  It is necessary global evidence, but it is not by itself a
calculation of trivial holonomy for the worker's particular measure
connection; a flat connection can still have nontrivial Wilson phases.  The
worker correctly labels B2c descriptive and does not use it to pass the strip
gate (`PREREG.md:82-89`; `REPORT.md:48-57`).

**Item 4 finding: confirmed.**

## 5. Consequence for route 1 and periodic-time reflection positivity

Reflection positivity is well defined on an even periodic-time lattice.  A
link reflection of the time circle has two cuts, not one; the positive algebra
is supported on one half-torus, and the reflected kernel integrates the gauge
links crossing both cuts.  The copied K2c geometry already represents exactly
this structure: `Geom.crossing_mats()` adds the ordinary $0\to1$ links and
the antiperiodic temporal wrap $T\to -T+1$
(`scripts/lat2d.py:50-62`), and its torus quadrature includes both planes
(`scripts/lat2d.py:198-207`).  This is consistent with the standard finite-
lattice Osterwalder--Seiler framework; see Osterwalder--Seiler,
[*Annals of Physics* **110**, 440--471
(1978)](https://doi.org/10.1016/0003-4916(78)90039-8).

For the unchanged route-1 Wilson kernel, periodic time is therefore the clean
next geometry.  The fixed G-LEG(a) condition still requires $L_x\ge4$
(`TESTS.md:343-345`), whereas the available torus node construction is only
implemented for $L_x=2$ (`scripts/lat2d.py:198-208`).  A new result would
need, in this order:

1. an explicit global local torus measure (including its Wilson-line term),
   not just $C=0$;
2. its gauge invariance, locality, toron-loop integrability, and reflection
   condition on that torus;
3. W-matched periodic-time link-reflection kernels at $L_x\ge4$, with both
   reflection cuts integrated and the established power controls.

Thus `REPORT.md:79` is correct as a statement of the natural next computation.
It is slightly too exclusive if read as a theorem that periodic time is the
only possible repair: modified open boundary conditions or boundary terms
could in principle remove the exact edge obstruction, but would define a new
setup and require the same gates from scratch.

**Item 5 finding: periodic-time RP is well defined; periodic $L_x\ge4$
kernels are indeed new work and are the natural fixed-rule continuation, but
the torus measure must first be completed and periodic time is not the only
conceivable changed geometry.**

## Strongest correct statement

For the finite two-dimensional U(1) 11112 overlap system with $M=r=1$,
antiperiodic spatial fermions and the specified open-time termination, a mode
supported wholly on either time boundary is an exact zero of $H_W$ iff
$eW_{\rm edge}=\pi\pmod{2\pi}$; this is proved directly for arbitrary
plaquettes and independently reproduced on nonuniform fields.  Hence every
degree-one Wilson-line winding leaves the gapped admissible domain, so the
explicit fixed requirement (b″) cannot be exercised and the campaign reading is
unavoidably OPEN.  The registered central/bulk finite-volume statistic does
fall exponentially with ν = 0.869 ± 0.064 and the L1 control scales as
$1/L_x$, while the tested edge response is fitted extraordinarily well by
$L_x^{-4.97}$ through $L_x=24$.  The Ward identity forces any
gauge-invariant measure current to inherit some fixed fraction of a genuinely
algebraic remote anomaly response, so the edge data are strong evidence
against a volume-uniform local measure on this strip, but finite sizes do not
prove that universal asymptotic no-go.  On a periodic torus the independent
topological check gives $C(11112)=0$ and $C(L1)=-1$; link-reflection
positivity is well defined there, but a global local torus measure and new
$L_x\ge4$ periodic-time RP kernels are still required before route 1 can
receive a fixed-rule CHI-RP reading.
