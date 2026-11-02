# TQ2 — fresh hostile review

**Disposition: LAND as a conditional UNDECIDED research note only.** The
pressure construction, boundary comparison, secant estimates and common
diagonal are valid under their displayed hypotheses. No actual Wilson
no-cusp, extensive-source comparison, all-observable orientation theorem,
or Yang–Mills construction has been established. There is no remaining
blocking finding in the reviewed revision.

Reviewed source: [TQ2.md](../TQ2.md), 650 lines, SHA-256
`3d9342a392f01d3e705e5fe381ca88aed20e4dd06c8138751be23e768e96e38a`.
Date: 2026-10-30. This is a filesystem-snapshot review; the workspace does
not contain Git metadata. No commit is attributed to a revision.

I am a fresh Codex reviewer in a separate agent context. This is
**same-family, context-separated review**, not cross-family review, a
formal audit, or a retained-status grant. I received the author task and
source-update notices, read the complete target, and independently rebuilt
the steps below. I did not author or edit the target. The only file I wrote
is this report. No scientific numerics, scripts, worker launches, source
edits, ledger changes or commits were performed. Method credit remains
with Tadeusz Balaban and Jonathan Dimock for the constructive RG programme.
No recalled literature theorem carries a proof step in this review.
I also checked briefs_q/TQ2/REVIEW.md's substantive checklist. This report's
location follows the author's explicit file allowlist and the parent task's
narrower instruction to write only `checks/tq2_review.md`.

## 1. Fixed-cutoff source and tilted-torus boundary argument — CONFIRMED

Attachments: TQ2 lines 183–260, §§3.1–3.2, equations (4)–(8).
**Fix:** none; retain LOC and the fixed-cutoff scope.

For a real bounded approximant, let `N=V/a^4` and
`A=a^4 sum_x tau_x Y`. Differentiation under the finite compact integral
gives `p'(0)=a^4 N E[Y]/V=E[Y]` and
`p''(t)=Var_t(A)/V`. The source translates the entire observable product,
so this first derivative is the specified n-point moment. It is not the
claim that a one-point source determines every moment by a first
derivative. LOC is essential: the function, its subtractions and its
finite lattice range must be independent of volume once embedded.

Here is an independent reconstruction of the geometric step. Work in grid
coordinates, at fixed `a,F`. The quotient is by an integral period matrix
on a cofinal commensurate set. Assign the four positively oriented bond
variables at a site to that site. A retained `b`-cube then owns a disjoint
set of integration variables. Haar measure is a product probability
measure; there is no gauge-fixing constraint coupling the retained cubes.
After deleting every interaction crossing cubes or the outside strip,
its integral is `Z_b(t)^K` times unused Haar factors equal to one.

An interaction can cross an interior face only when its anchor is within
its range `d` of that face. Those anchors number at most `C L^4 d/b`.
The incomplete cubes and wrapped interactions lie within distance
`C(b+d)` of the finitely many parallelepiped faces, giving
`C_P(b+d)L^3` more anchors for large `L`. This argument applies to each
fixed tilted period matrix; no bound uniform over degenerating shapes is
claimed. Bounded Wilson and source terms turn this count into a sup norm
action error. The elementary inequalities for two actions differing by
at most `B` imply `|log Z_1-log Z_2|<=B`.

To check the normalization explicitly, set
`q_b(t)=[log Z_b(t)-log Z_b(0)]/(a^4 b^4)`. Comparing at both `t` and zero
shows that `p_R(t)` differs from `(K b^4/L^4)q_b(t)` by the stated boundary
error. Also `|q_b(t)|<=M_(a,F)|t|`, and the missing-volume fraction is
`O_P(b/L)`. This proves (8). For fixed `b`, two large tori are close to
the same `q_b`; their limiting upper/lower gap is at most `C d/b`.
Letting `b` tend to infinity proves existence and period independence.
The Lipschitz estimate gives compact-real-source uniformity by finite
nets. All constants may deteriorate with the cutoff. No derivative
convergence, phase uniqueness, infrared decay or mass gap has entered.

## 2. Convex recovery and one common sequence — CONFIRMED

Attachments: TQ2 lines 284–390, §§4.1–4.2, equations (10)–(14).
**Fix:** none; preserve the named continuity and common-selection inputs.

For differentiable convex `f` with `f(0)=0`, the tangent inequality at
zero gives `-f(-t)/t <= f'(0) <= f(t)/t`. If two finite-volume pressures
are within `delta` of the same thermodynamic pressure at both source
signs, their derivatives therefore differ by at most

`[p_infinity(t)+p_infinity(-t)+2 delta]/t`.

This gives (11) with `delta=1/j`. The source is held at each fixed
`t_l>0` until after the cutoff limsup, so `2/(j t_l)` disappears before
`t_l` goes to zero. NC is exactly sufficient for this argument. No
interchange of the three limits is being presumed.

The extensive source obeys the same coordinate transport as the original
observable: anchors, product supports and normalization all rotate.
Consequently (12) holds. In the upper bound for
`m(F_Q)-m(F)`, only the positive-source pressure for `F_Q` needs PC; in
the reverse bound, only its negative-source pressure does. Thus the
`max_+/- epsilon` in (13), rather than an omitted extra factor, is
correct. PC alone does not force equality of zero-source derivatives at
a cusp. The note correctly requires NC as well.

The diagonal is legitimate because every finite list of observables,
frames, periods and source signs has a finite volume threshold at each
fixed cutoff. Taking a common compatible radius above that finite list
gives one sequence for all fixed finite product orders. Each fixed tuple
is eventually included; no uniform constant over all orders is used.
The rational rotation admits arbitrarily large common even periods.
COMMON must continue to supply extraction, extension, RP and witness
compatibility on this selected family, as the note expressly requires.
The argument does not repair incompatible preassigned regulator sequences.

For completeness, the dense-group step can be checked without an
algebraic-integer closure theorem. If `z=(3+4i)/5` had finite order `n`,
then `(3+4i)^n=5^n`. The homomorphism from Gaussian integers to integers
modulo 5 sending `i` to 2 sends these sides to 1 and 0, respectively.
Thus the angle is irrational. Pigeonholing its powers gives arbitrarily
small nonzero steps; multiples of such a step approximate every circle
angle. Hypercubic conjugates give each coordinate-plane circle, and
successive plane eliminations generate SO(4); a coordinate reflection
supplies O(4). Group stability and the named continuity are needed for
the extension. Lattice translations plus equicontinuity supply continuous
translations. Separated tests alone still supply no collision extension.

Finally integrating U-all gives precisely
`integral tau = m(F)-m(F_Q)+integral e`. Thus torque identification needs
U-all, but no convergence of derivatives of limiting moments. The
pressure comparison alone is a separate endpoint symmetry argument.

## 3. NC, source admissibility and shrinking radii — CONFIRMED with OPEN inputs

Attachments: TQ2 lines 262–280 and 392–485, §§3.3, 4.3–4.4.
**Fix:** none in the final revision; retain the added source-admissibility
qualification and all radius/error and TAIL conditions.

The two-state example is exact: opposite biases of size `H_R=R^3`
change pressure by at most `2H_R/V`, while the two zero-source slopes
are `+/-tanh H_R`. Since `H_R/V` tends to zero, both pressure limits
are `|t|`. This refutes the claimed implication from small pressure or
surface errors to local-moment agreement in the stated comparison class.
It is not a finite-coupling Wilson counterexample. Its unbiased version
also shows that an invariant selected state can coexist with a source
cusp. NC is a stronger sufficient condition than the selected-state
invariance target in this architecture, not a necessary condition for
every symmetry argument.

The revised text correctly separates the thermodynamic phase-response
burden from possible UV/tail failure of a fixed real source interval.
For Gaussian `X`, every polynomial moment is finite, but for `t>0`,
`t x^4-x^2/2 >= t x^4/2` once `x^2>=1/t`, so the positive exponential
moment diverges. Finite-cutoff compactness supplies finiteness separately
at every cutoff, not a uniform interval in the continuum limit. This
warning is essential for sources of arbitrary products and is now
explicit. It is not asserted to prove Wilson source divergence.

The optional SUS calculation is also correct: twice integrating the
variance identity yields the triangular kernel with integral `t^2`.
Translation invariance of the real tilted law gives exactly
`Var(A)/V = a^4 sum_y Cov(Y,tau_y Y)`. Uniform summability would be
sufficient, but includes overlapping supports and all real tilts; the
reviewed separated SRC estimates do not supply it.

For moving radii, the correct error is pressure error divided by the
actual `t_(j,F)`. MS includes both this condition and vanishing chord
width. At step `j`, include the needed pressures for `F` and its
transported `F_Q` at the same `+/-t_(j,F)`, with error at most
`t_(j,F)/j`; the finite maximum of their volume thresholds exists.
The resulting bounds are exactly `w_(j,F)+2/j` and
`w_(j,F)+e_(j,F)+2/j`. No favorable competition between shrinking
radius and UV comparison error is automatic. The entire SP/VAC bound,
including its scalar term, must be `o(t_(j,F))`.

The clipping alternative is valid at the auxiliary lattice level.
Integer clipping thresholds already form a sufficient countable family
for the joint diagonal. For each threshold, compare clipped expectations
first; the two original-minus-clipped expectation errors then bound the
remaining difference by the triangle inequality. TAIL is precisely the
needed transfer. Absolute uniform integrability is sufficient but is
stronger than the displayed signed expectation condition. Neither a
continuum clipping operation nor tail control is imported from SRC-E′.

## 4. Extensive conditional comparison and vacuum constants — CONFIRMED

Attachments: TQ2 lines 97–125 and 489–559, §§2.1 and 5.1–5.2,
equations (2), (SP), (VAC), (16).
Source check: UNIV55 §2.1/E5; CODEX_REVIEW_UNIV §1.
**Fix:** none; source-dependent vacuum matching remains a separate premise.

Write total partition functions `Q_G(t)=integral Z_G(t,V_c) dV_c`.
Forward normalization of the kernel identifies these with the original
fine partition functions. SP gives

`|log Q_I(t)-log Q_Q(t)-c(t)| <= N_b eta(t)`.

Subtracting the same assertion at zero and dividing by `V` gives (16).
There is no total-variation exponent because the logarithm is taken
before division by volume. The ratio `N_b/V`, not `N_b`, is the relevant
coefficient. Positivity and a common reference coarse measure are the
only integration facts used.

The source-dependent scalar term cannot be dropped. For example,
`Z_I(t,V_c)=exp(V t) Z_Q(t,V_c)` satisfies a zero-error SP with
`c(t)=Vt`, yet its normalized pressures differ by `t` and its slopes by
one. VAC explicitly rules out this missing contribution. Constants
independent of coarse data are not necessarily independent of source.

The original Proposition T estimate follows instead by normalizing the
density ratio, bounding it between `exp(-2 delta_d)` and
`exp(2 delta_d)`, and splitting image and density errors. TQ2 correctly
retains both all-data hypotheses, and requires actual truncation
comparison and tails for unbounded approximants. Kernel normalization
does not prove them. SP/VAC adds volume-uniform, extensive, all-product
source information and all-coarse-field control; it is not an output of
the reviewed bounded-local-observable proposition or SRC linear source
theory. The counterexample arrays `aR` and `1/(aR)` correctly show why
the separate old iterated limits do not alone supply a common diagonal.

## 5. Averaging finding and author correction — RESOLVED

Attachment: TQ2 lines 127–179 and 614, §2.2 and §7 status table.
**Binding fix:** the AN equivalence correction below was required and has
been applied by the author; no binding fix remains open.

I reported one narrow overstatement during this review: an invariant
averaged limit alone makes AN sufficient for invariance of the original
limit, but does not make AN equivalent to that invariance. Equivalence
also needs identification with the Haar average of the same original
limiting functional. Two separately invariant states can have different
moments. The author corrected both the paragraph and status table in
place; I reread the final wording at lines 146–152 and 614. This finding
is closed in the source hash recorded above.

For an already specified continuous state, the Haar-average argument is
valid by translation of the group integration variable. Equality with its
own Haar average is equivalent to invariance. The RP statement now gives
the sufficient common-plane convexity condition without incorrectly
calling it necessary. PANEL_P2 §2 supports the stated caution about
unrestricted rotational averaging; it is not used to exclude all possible
RP averaging constructions.

The bounded vector example is also exact: the second moment is `|v|^2`,
the fourth is `4 sum_i v_i^4`, and at `(3e_1+4e_2)/5` it is `1348/625`.
Rotational averaging gives `mu=3 nu` and `4mu+12nu=16`, hence `mu=2`.
Constant fields allow distinct spatial insertion points without changing
these moments. The example tests a probability inference; it does not
claim to lie on the scalar Wilson premise set.

## 6. Source interfaces and scientific disposition — CONFIRMED as scoped

Attachments: TQ2 lines 28–93 and 561–650, §§1, 6–7.
**Fix:** none; the OPEN application inputs and UNDECIDED route verdicts
must remain explicit.

I checked TQ §5 and REVIEW_TQ's endpoint/dense-group discussion;
UNIV55 Proposition T/E5 and CODEX_REVIEW_UNIV §1; N5B §2.1 and
REVIEW_N5B item 1; ROTDEF §§6–7 and E4–E6; SRCCD55 §§3.3–3.5 and
CODEX_REVIEW_SRCCD §§5–6; ASSEMBLY55 N4/N10/N11/N12/N14 and its common
algebra discussion; AUDIT's FT/FA, SS/SP/SR and ten-route mapping; and
PANEL_P2 §2. Source labels were not substituted for the calculations
above. I read AUTHOR.md and PROCESS_LIGHT.md first.

TQ2 does not upgrade the pair source/torque result to every product.
It retains SRC-W′ contacts, the corrected averaged conditional-decay
scope, and the separate product-image moment obligation. The stated
state-dependent centering derivative is correct: a product of more than
two centered factors leaves lower products whose expectations need not
vanish. LOC's state-independent prescription or a proved matching
reduction is therefore substantive.

For the sphere, total covariance and Cauchy–Schwarz give N5B's displayed
`delta(J)+C(J) tau(a,J)` bound, with fixed `J` before removing the cutoff.
But its observable-image L2 bound and fine covariance sum are averaged
under the actual law. The all-data seam bound does not change those
quantifiers. TQ2 correctly preserves REVIEW_N5B's HOLD on the stronger
fully conditional UV-only characterization and leaves the sup/terminal-
datum strengthenings OPEN. It does not infer that infrared decay is
necessary for the averaged alternative.

The signed-shell power count uses bounded shell coefficients and
four-dimensional shell volume to turn `r^(-4-epsilon)` into
`r^(-epsilon)`; it is a sufficient all-product estimate, not a mass-gap
requirement. Route counts remain counts of the ten declared chains.
Neither failure of NC/SP nor the toy examples establish a Wilson NO-GO.

What may be retained from this note is the fixed-cutoff pressure limit,
the conditional all-product secant/diagonal theorem, the extensive
conditional-to-pressure comparison with its scalar terms, and the
corrected averaging/source-domain warnings. COMMON, NC or MS, PC or
SP/VAC, any clipping transfer, and the actual all-observable Wilson
application remain unproved. Flat versus sphere remains UNDECIDED.

VERDICT: LAND
