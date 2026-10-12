# VERDICT: CONFIRMED WITH CORRECTIONS

The worker's final **INCONCLUSIVE** reading is correct, and the invariant-form
classification, shear collapse, scalar Lemma A, and the core bounded-operator
lemma are substantial correct results. Material corrections are required:

- the fixed PASS and FAIL disjuncts are not individually met;
- the bounded-charge lemma does not force an infinite reciprocal tower, and
  failure of its equivariance hypothesis (C) need not select a physical frame;
- finite torus occupancy is not a density proof;
- the \(1/q^2\) runner transforms a continuous hyperboloid, not a discrete
  arithmetic orbit;
- Lemma A does not refute the local asymptotic hypothesis (E2); and
- the scalar lower count is a generic linear matching count, not a universal
  microscopic tuning theorem.

## 1. Invariant forms, Zariski density, and the TT statement

**Confirmed under \((\Gamma)+(\mathrm{E2})\), with the TT interpretation narrowed.** I reran
`r32_forms.py`; it exactly reproduced `r32_forms.out:1-38`. The arithmetic
group is a lattice in the connected Lorentz group (`R2-2_referee.md:9-16`), so
Borel density applies. Uniqueness of the second-order jet makes its coefficient
tensors Gamma-invariant, and a tensor stabilizer is Zariski closed; the passage
to Lorentz-invariant tensors at `R3-2_report.md:101-102` is therefore valid.

The exact results are 2 mass forms, 0 one-derivative forms, and 4
two-derivative forms, with no parity-odd scalar and one gauge-invariant kinetic
combination (`R3-2_report.md:103-108`; `r32_forms.out:24-27`). Thus the full
quadratic gauge-restoration codimension is

\[
2+(4-1)=5,
\]

after the separate tadpole/cosmological tuning, versus the registered
\(3+(9-1)=11\) hypercubic count. An independent exact Ward-variation check gives
zero mass nullity and the unique kinetic vector
\((1,-2,2,-1)\) (`referee_checks.py:39-72,85-91`;
`referee_checks.out:1`). The modular calculation uses only the displayed
generator subgroup (`r32_forms.py:143-150`), but this is sufficient: its fixed
space already has the Lorentz lower-bound dimensions 2 and 4, so the full
arithmetic group cannot have more.

On a transverse-traceless tensor, the Lorentz-invariant quadratic operator is
\((m_1+a q^2)h_{TT}^2\). Hence, if \(a\ne0\), a tuned massless spin-2 pole has the
background Lorentz cone with no independent leading \(c_T\) parameter. This is
an algebraic restriction, not yet a viable-wave theorem. The script uses
four-dimensional transversality and tracelessness at generic off-shell momentum
(`r32_forms.py:340-379`), leaving a five-dimensional subspace; it does not
count two physical helicities. Accordingly, “K1's 5 to 1” at
`R3-2_report.md:124,234` must retain the earlier qualification that K1's five
was an off-shell Euclidean-TT restriction rank, not a proved physical tuning
floor (`C4_K1_referee.md:3,9,15`). The statement \(c_T=c\) also presupposes a
nonzero healthy kinetic term and identification of the matter/light cone with
the same background cone; (E2) was stated only for the graviton
(`R3-2_report.md:61`).

## 2. Collapse of the \(E_g/T_{2g}\) split

**Confirmed for a Gamma-invariant \(C^2\) effective-action density.** Its
Hessian is a Lorentz-invariant mass form
\(a h_{\mu\nu}h^{\mu\nu}+b h^2\), and equal-norm spatial traceless diagonal and
off-diagonal strains both evaluate to \(a\). The runner's normalizations are
correct and give a maximum discrepancy \(1.079\times10^{-13}\)
(`r32_forms.py:395-416`; `r32_forms.out:29-38`). The cosmological expansion
ratio at `R3-2_report.md:136` is also correct.

Thus P0's two cubic shear coefficients collapse to one coefficient. Its zero
is the spin-2 masslessness condition when a viable spin-2 kinetic pole exists;
symmetry does not force it to zero. Calling it simply “the graviton mass” at
`R3-2_report.md:137-138` should be read in that conditional sense. The proof
also requires an invariant action density; it should not silently substitute a
frame-dependent Hamiltonian energy for that object.

## 3. Theorem \(T_\Gamma\), hypothesis (C), and the orbit computation

**The bounded-operator lemma is CLOSED after a convention repair; the tower
and frame dichotomy is not confirmed.** Let
\(F(c)=\sum_\mu c^\mu P_\mu\). Under a consistent vector/dual-vector covariance
law, \(\ker F\) is Gamma-invariant. Irreducibility of the standard Lorentz
representation restricted to a Zariski-dense subgroup makes the kernel zero or
all of four-space. In the injective case \(\lVert F(c)\rVert\) is a norm on a finite-
dimensional coefficient space. Unitary conjugation makes Gamma act by
isometries of this norm, impossible for the boost eigenvalue
\(8+3\sqrt7>1\). Therefore all bounded \(P_\mu\) vanish, contrary to H3_Gamma
(`R3-2_report.md:148-156`). No interaction is used.

The displayed indices are not mutually consistent as written. With line 64's
literal component matrix \(A=\Lambda^{-T}\), conjugating \(F(c)\) produces
\(F(A^Tc)=F(\Lambda^{-1}c)\), not \(F(\Lambda^{-T}c)\) as at line 150; the
eigenvalue rule at line 158 similarly needs a transpose/inverse repair. Using
the standard consistently ordered adjoint action fixes this without changing
the lemma.

(C) is natural if the gauge parameter is an ordinary spacetime vector, its
four constant generators form a closed nonredundant multiplet, and Gamma acts
equivariantly on that presentation. It is not implied merely by covariance of
the action at `R3-2_report.md:60`. Gamma could mix the selected generators with
additional or equivalent identities. Thus failure of (C) does not by itself
mean that the physical identity “picks a frame,” contrary to
`R3-2_report.md:169,223,269`. Unitary one-particle implementation is likewise
an additional reconstruction hypothesis; effective LRL dynamics was left open
by the prior referee (`R2-2_referee.md:20`). The eigenvalue variant at
`R3-2_report.md:158` additionally needs joint eigenstates/generalized states,
invariant domains, and uniformly bounded finite-dimensional symbols.

Most importantly, **unbounded charge does not imply an infinite fibre**. A
singular finite-matrix multiplier on a compact torus can be unbounded. R2-1's
actual tower proof used analyticity, winding, and a determinant to force
infinitely many eigenvalues at one fixed momentum
(`R2-1_report_unrefereed.md:113-121`); none of those steps occurs here.
Therefore `R3-2_report.md:169-171,225,268` proves only that the bounded,
unitarily implemented four-vector-charge class is empty, not that the
R2-1 tower is forced. The no-go stress test and open alternatives are recorded
in `NO_GO_DISCIPLINE_CHECKLIST.md:1-120`.

The orbit runner reproduces, including the \(1.6408\times10^5\) capped growth
and 256/256 versus 1069/1296 cell occupancies (`r32_orbit.out:1-19`). Exact
arithmetic verifies the boost and its eigenvalues (`referee_checks.out:2`). But:

- the matrix-entry cutoff at `r32_orbit.py:44` means this is a capped generated
  set, not a certified full word ball;
- finite grid occupancy does not prove a dense torus orbit or unbounded charge
  in every open region (`R3-2_report.md:164,171`);
- the shell residual printed at `r32_orbit.out:5` is \(0.0025024\) relative,
  i.e. about \(0.25\%\), not floating-point precision; exact preservation comes
  from the integer matrix identity instead; and
- the script assumes \(\tau=p\) (`r32_orbit.py:4-7`); it does not construct the
  charges of a matter law.

## 4. Lemma A, orbit nondecay, and the shell transform

**Scalar Lemma A is CLOSED with a small proof completion.** The Taylor
components at zero are Lorentz-invariant and hence polynomials in \(Q=p^2\).
On a sufficiently small \(U_{r'}=\{|Q|<r'\}\), analytic continuation gives
\(F=f(Q)\). For nonzero reciprocal \(G\), choose a null \(n\) with
\(n\cdot G\ne0\) and

\[
\lambda={c-Q(G)\over2n\cdot G}.
\]

Then both \(\lambda n\) and \(\lambda n+G\) lie in \(U_{r'}\), while periodicity
forces \(f(c)=f(0)\). The omitted last sentence is to continue this constant
from \(U_{r'}\) to the connected \(U_r\) (`R3-2_report.md:185-191`). The
“follow the light cone across a reciprocal step” argument is valid.

Two qualifications matter. First, \(Q\) is not a function on the torus: the
hypothesis is analyticity of the periodic lift on the **entire noncompact
lifted band** \(U_r\), not merely a local Euclidean germ near \(q=0\). Therefore
the lemma does not refute the local second-order asymptotic (E2) at
`R3-2_report.md:61`, and line 238 is too strong. Second, the proved scalar
conclusion is “constant on \(U_r\),” not globally constant or globally
nonanalytic. For example, the finite Gamma orbit of the half-reciprocal
two-torsion point \((\pi/\sqrt7,0,0,0)\) stays outside
\(|Q|<(2\pi)^2/28\); its periodic indicator is a pathological but literal
nonconstant invariant function that is identically analytic there
(`referee_checks.py:103-110`; `referee_checks.out:7`). It is zero almost
everywhere and is not a useful nonzero \(L^1\) multiplier, but it demonstrates
the logical gap. The matrix/covariant extension is itself labeled only a sketch
at `R3-2_report.md:193`, so line 196 cannot promote it to “every covariant
kernel.”

The important power-law correction **does survive in a narrower, decisive
form**. If a well-defined invariant scalar real-space kernel is nonzero at one
offsite displacement, it has the same nonzero value on that displacement's
infinite Euclidean-unbounded Gamma orbit. It therefore cannot obey any uniform
positive-power Euclidean decay bound. This refutes the supervisor's proposed
Gamma-invariant power-law tail at `TESTS.md:2655`; the operative result is
nondecay along an orbit (and infinitely many coupled sites), not merely the
generic phrase “unbounded valency.” Reindexing a Poincare series requires
absolute convergence or another invariant prescription, so “the orbit weights
converge” at `R3-2_report.md:197` remains unsupported.

The shell calculation itself is correct only as a **continuous comparator**.
`r32_orbit.py:105-112` Abel-regularizes the transform of the continuous unit
timelike hyperboloid at purely spatial momentum and obtains
\(4\pi K_1(k)/k\sim4\pi/k^2\); the values reproduce independently
(`referee_checks.out:8-9`). It does not transform the discrete arithmetic
measure \(\sum_{x\in\Gamma x_*}\delta_x\). No discrete-orbit equidistribution,
Fourier-distribution control, or error bound is supplied. Hence “each shell
contributes a \(1/q^2\) singularity” at `R3-2_report.md:198`, and the necessary
moment-sum-rule inference at lines 199 and 270, are not established.

## 5. Scalar sector and PPN reading

**The source-exchange calculation is confirmed; its interpretation is
conditional.** I reran `r32_scalar.py` and reproduced
`r32_scalar.out:1-28`. An independent analytic reduction gives, for kinetic
coefficients \(a,b,c,d\) multiplying F1--F4, zero TT mass, and any fixed
nonzero trace mass,

\[
{c_2\over c_1}=-{a+b\over4a+3b}.
\]

Thus the GR ratio \(-1/2\) generically imposes \(b=-2a\). With both masses zero,
putting \(A=a+b+c+d\), \(B=\sqrt3(c/2+d)\), \(C=a+3d\) gives

\[
{c_2\over c_1}=-{1\over3}+{aA\over3(AC-B^2)},
\]

and GR is the single condition
\((a+d)A-(c/2+d)^2=0\) (`referee_checks.py:66-81`;
`referee_checks.out:3-5`). This independently confirms that tuning only the TT
mass does not generically reproduce GR exchange.

The “erratic” nonzero-trace-mass scan has a precise cause: the worker chose
\(a=0.45,b=-0.6\), so \(4a+3b=0\) identically while scanning F4
(`r32_scalar.py:101-122`; `referee_checks.out:6`). Its huge values are a
higher-order/ill-conditioned pole, not generic numerical uncertainty.

Under universal metric coupling and an unscreened healthy linear regime, the
exchange ratio controls the PPN scalar admixture (and hence gamma), so a third
generic matching condition beyond spin-2 masslessness and the tadpole is real.
The runner does not establish positivity, stability, nonlinear screening, an
actual LRL PPN prediction, or a universal lower bound on independent
microscopic tunings. Therefore “observational count at least 3” at
`R3-2_report.md:213,237` is sound only as a generic linear coefficient-space
count.

## 6. FIXED reading

**INCONCLUSIVE is the correct registered reading, but not because one fixed
PASS disjunct and one fixed FAIL disjunct are simultaneously met.** The fixed
PASS at `TESTS.md:2679` asks for an actual Gamma-covariant matter-plus-graviton
law with an exact identity or no more than graviton-mass plus cosmological
tunings. No law is constructed; the full conditional gauge codimension is 5;
and generic conserved-source exchange adds a scalar matching condition. A
“TT reading” cannot replace the registered criterion, so
`R3-2_report.md:224,230` does not meet PASS(ii).

The fixed tower FAIL at `TESTS.md:2680` is also not met: only bounded vector
charges are excluded, while an unbounded singular finite-fibre charge and
non-(C) identity representations remain unclosed. Finally, “the count does not
improve” is not met either: if a symmetry-preserving second-order jet exists,
the operator codimension genuinely drops from 11 to 5 and the cubic shear
split disappears. With no fixed disjunct established, the result is
**INCONCLUSIVE**, containing a conditional counting improvement and a narrower
bounded-charge obstruction.

## Strongest correct statement

If a Lorentz-random-lattice realization admits a Gamma-covariant quadratic
graviton effective action with a symmetry-preserving expansion through
\(q^2\), its invariant coefficient space has two mass and four kinetic forms,
only the Einstein-Hilbert kinetic direction is gauge invariant, and the full
quadratic restoration codimension is 5 rather than 11; its two cubic shear
channels become one, and a tuned massless TT pole has the background Lorentz
cone without an independent leading speed coefficient. A nonzero four-vector
constant gauge charge cannot be represented by bounded operators under a
unitary Gamma action, even for free matter, but this neither forces an
infinite reciprocal tower nor makes every non-(C) identity select a frame. A
periodic invariant scalar analytic on the entire lifted band \(|p^2|<r\) is
constant on that band, while any nonzero invariant scalar coupling repeats
without Euclidean decay along an unbounded orbit, refuting the proposed
power-law-tail construction; the claimed discrete-shell \(1/q^2\) law remains
unproved. Generic conserved-source exchange adds one scalar matching condition
beyond spin-2 masslessness and the tadpole. Thus none of the FIXED PASS/FAIL
disjuncts is established, and R3-2 remains **INCONCLUSIVE**.
