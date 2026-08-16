---
claim_id: admissibility_dirac_kahler_floquet_monodromy_action_pairing_bounded_theorem_note_2026-08-16
claim_type: bounded_theorem
claim_scope: "On the primary finite carrier at both rational shear fixtures, the fixed-momentum action is pentadiagonal in fine time with slice-varying two-slice companions whose four-step Floquet monodromy has determinant one exactly and real rational trace below minus two, so both eigenvalues are strictly negative and every one-step homogenizing gauge carries a non-real quarter-turn fourth root -- no reflection-real one-step-stationary gauge exists and the Block 117 window obstruction is structural for reflection-covariant one-step windows, with the exact dressed identity expressing the Block 117 constants through the action covariance and the dressing corrections; the undressed torus pairing is non-Hermitian, the half-space stable-split pairing is an exactly geometric-Hankel rank-one non-Hermitian form whose window pencil vanishes identically while its one-dimensional moment quotient carries the contractive root rho^2 in (0,1); and the reflection-intertwiner completion, a positive OS Hilbert space, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_self_chart_emptiness_stationarity_bounded_theorem_note_2026-08-16
runner: scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_self_chart_emptiness_stationarity_bounded_theorem_note_2026-08-16
target_blocker_text: "Derive the stationary (Toeplitz-window) action pairing; then the gravity constraint quotient."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Construct the reflection intertwiner that completes the rank-one geometric-Hankel action pairing to a Hermitian positive OS package; then the gravity constraint quotient."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-117 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact pentadiagonal and two-slice companion reconstruction, exact determinant-one four-step monodromy, exact rational traces below minus two and exact isolation of both negative roots at both fixtures, exact inverse reproduction and translation-residual ranks, exact dressed micro-motion identity and additive splits, exact non-Hermitian and rank-one degeneration certificates, and exact minimal polynomials and isolating intervals for the one-dimensional quotient root; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Floquet Monodromy And The Reflection-Covariant Stationarity Obstruction

**Date:** 2026-08-16

**Campaign block:** 118

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py`](../scripts/admissibility_dirac_kahler_floquet_monodromy_action_pairing_2026_08_16.py)

## 1. Result Up Front

[Block 117](ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:16`
and elaborated at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:778-792`:

> Derive the stationary (Toeplitz-window) action pairing; then the gravity
> constraint quotient.

**Floquet monodromy theorem.** On the primary `Z8_t x Z4_x` carrier, at
each of the rational shear fixtures \(c=5/13\) and \(c=3/5\), the
fixed-momentum action is pentadiagonal in fine time. Its four two-slice
reduction steps have slice-varying companions \(T_{k,n}\), \(n=0,\ldots,3\).
Their four-step monodromy

\[
 M_k=T_{k,3}T_{k,2}T_{k,1}T_{k,0}                    \tag{1}
\]

obeys

\[
 \det M_k=1,\qquad \operatorname{tr}M_k\in\mathbb Q,
 \qquad \operatorname{tr}M_k<-2.                     \tag{2}
\]

The two eigenvalues of every displayed \(M_k\) are therefore real,
distinct, reciprocal, and strictly negative. Exact rational endpoint
tests give eight isolating intervals for the four parity-fixture spectra.

**Reflection-covariant gauge obstruction.** A one-step homogenization of a
four-step Floquet eigenline must choose a number \(\mu\) satisfying
\(\mu^4=\lambda\). Since every \(\lambda<0\),

\[
 \mu=\lvert\lambda\rvert^{1/4}
       \exp\!\left({(2j+1)\pi i\over4}\right),
 \qquad j=0,1,2,3.                                    \tag{3}
\]

Every choice carries a non-real quarter-turn phase. An abstract complex
Floquet gauge exists, but none is reflection-real. Thus no
reflection-real one-step-stationary gauge exists for these action
eigenlines, and the Block 117 adjacent-window obstruction is structural
for reflection-covariant one-step windows rather than an omitted real
gauge choice.

The Block 117 constants are nevertheless reproduced exactly by the
dressed action covariance:

\[
 q_k:=Y_{01}-Y_{12}
 =\overline{(A_kW_k)_{4,2}-(A_kW_k)_{5,1}},
 \qquad
 {\partial q_k\over\partial\tau_a}=0
 \quad(a=0,1,2).                                      \tag{4}
\]

The two self-conjugate momentum splits make the dressing contribution
visible. At \(c=5/13\), with the common denominator
\(1026791823428467\),

\[
\begin{aligned}
 q_0&=355348797912000
     =293040926496000+62307871416000,\\
 q_2&=228512035080000
     =293040926496000-64528891416000.
\end{aligned}                                        \tag{5}
\]

At \(c=3/5\), with the common denominator \(250649423107\),

\[
\begin{aligned}
 q_0&=86496072000=62924832000+23571240000,\\
 q_2&=35364504000=62924832000-27560328000.
\end{aligned}                                        \tag{6}
\]

Every integer in (5) and (6) is divided by its displayed common
denominator. The first addend is the raw, momentum-independent defect; the
second is the \(A_k\)-dressing correction. The undressed equality fails,
so the dressing is essential rather than cosmetic.

The attempted action pairings have an exact degeneration ledger.

1. The antiperiodic torus kernel is reproduced exactly as
   \(W_k=Q_k^{-1}=G_k\), but the undressed pairing is non-Hermitian.
2. Its one- and four-fine-slice translation residuals have full rank
   eight, while the eight-slice residual vanishes exactly.
3. The stable-split half-space kernel is geometric-Hankel and rank one,
   but remains non-Hermitian; its anti-Hermitian part has rank two.
4. Its two-window determinant pencil vanishes identically.
5. After quotienting the common moment radical, the remaining
   one-dimensional shift is multiplication by
   \(\beta_k=\rho_k^2\in(0,1)\).

This \(\rho^2\) is the first contractive transfer value found in the
campaign. It is not yet an OS contraction: neither displayed pairing
supplies a positive Hermitian form. The live repair is the simultaneous
reflection intertwiner that could complete the rank-one
geometric-Hankel action pairing to a Hermitian positive OS package.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The authority snapshot is
unchanged from Blocks 115--117.

The exact stacked parent is
[Block 117](ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md)
commit `f800356aec0989b6e0fa80ed43274794243b1ca2`, content-bound through
note blob `9dab24a21193fb763f65344df89a66e17e7a2d40`. No audit verdict is
imported.

The executed contract is:

1. the inherited Blocks 107--117 `d=2` one-fine-mode carrier on
   `Z8_t x Z4_x`, with antiperiodic time closure and the link-centered
   reflection `theta(t)=-1-t`;
2. the fixed-momentum fine-time action matrices \(Q_k\), \(k=0,1,2,3\),
   at the rational shear fixtures \(c=5/13\) and \(c=3/5\);
3. the exact pentadiagonal support, four-cell two-slice reduction,
   slice-varying companion matrices, and four-step Floquet monodromy;
4. the telescoping companion determinants, exact rational traces, exact
   characteristic polynomials, negative-root theorem, and eight rational
   isolating intervals;
5. the exact antiperiodic Green-kernel formula, Schur reconstruction, and
   entrywise reproduction \(W_k=Q_k^{-1}=G_k\);
6. the exact one-, four-, and eight-slice translation-residual ranks and
   the displayed nonzero sample entries;
7. the exact dressed micro-motion identity, vanishing parameter
   derivatives, two raw-plus-dressing splits, and shared-denominator
   fingerprints;
8. the exact torus non-Hermiticity and the stable-split
   geometric-Hankel, rank, anti-Hermitian-rank, zero-pencil, and
   one-dimensional moment-quotient certificates; and
9. the no-go conclusion only for reflection-real one-step-stationary
   gauges and the naive displayed action pairings, while leaving the
   reflection intertwiner live.

The exact certificate report used for the displayed constants ends with
`TOTAL: PASS=562 FAIL=0`. The task-level request for literal four-step
stationarity is reported honestly as a failed proposed identity: its
residual has full rank. The certificate succeeds because it proves and
records that non-equality rather than masking it.

The exact scope is the primary finite carrier, both rational shear
fixtures, all four fixed momenta, the fine-time action and two-slice
companions, the naive torus pairing, and the displayed stable-split
half-space construction. The reflection-intertwiner completion, a positive
OS Hilbert space, curved OS positivity, the completed ADM/history
transporter, joint gravity, the gravity constraint quotient, Records,
retention, axiom amendment, obligation retirement, and TOE percentage
movement are outside the executed contract.

## 3. The Pentadiagonal Structure And The Companions

Fix a spatial momentum \(k\in\{0,1,2,3\}\). In the ordered fine-time
basis, the exact action matrix \(Q_k\) has support only at fine-time
separations

\[
 t'-t\in\{-2,-1,0,1,2\},                              \tag{7}
\]

with the declared antiperiodic signs on entries that cross the time seam.
Thus the action is pentadiagonal in fine time. This is a support statement
about \(Q_k\), not a claim that its coefficients are constant from slice
to slice.

Group the eight fine times into four ordered two-slice cells. The exact
Schur reduction of the pentadiagonal equation gives, in the certificate's
normalization, a second-order cell recurrence

\[
 C_{k,n}u_{n+1}+B_{k,n}u_n+C_{k,n-1}u_{n-1}=0,
 \qquad n=0,1,2,3,                                    \tag{8}
\]

with every \(C_{k,n}\ne0\). The associated two-slice companion is

\[
 \binom{u_{n+1}}{u_n}
 =T_{k,n}\binom{u_n}{u_{n-1}},
 \qquad
 T_{k,n}=
 \begin{pmatrix}
  -B_{k,n}/C_{k,n}&-C_{k,n-1}/C_{k,n}\\
  1&0
 \end{pmatrix}.                                      \tag{9}
\]

The exact entries vary with \(n\). A constant companion was not inserted
to manufacture stationarity. Instead, the ordered products retain the
micro-motion:

\[
 U_k[n,m]:=T_{k,n-1}\cdots T_{k,m},
 \qquad
 U_k[m,m]:=I,
 \qquad M_k=U_k[4,0].                                 \tag{10}
\]

For \(e_1=(1,0)^{\mathsf T}\), antiperiodic closure gives the exact reduced
Green kernel

\[
\begin{aligned}
 K_k[n,j]
 ={1\over C_{k,j}}e_1^{\mathsf T}
 \big(&{\bf1}_{n>j}U_k[n,j+1]\\
      &-U_k[n,0](I+M_k)^{-1}U_k[4,j+1]\big)e_1 .
                                                               \tag{11}
\end{aligned}
\]

This is the reported construction formula. Reversing the exact Schur
elimination reconstructs the full \(8\times8\) fine-time kernel \(G_k\).
Section 5 verifies that reconstruction against the direct inverse, so
(8)--(11) are not merely a formal recurrence detached from the action.

## 4. The Monodromy

The companion determinant in (9) is

\[
 \det T_{k,n}={C_{k,n-1}\over C_{k,n}}.                \tag{12}
\]

Consequently the four-step product telescopes around the full cell cycle:

\[
\det M_k
 =\prod_{n=0}^{3}{C_{k,n-1}\over C_{k,n}}
 =1.                                                   \tag{13}
\]

No floating determinant or post hoc rescaling enters (13).

Write the characteristic polynomial in primitive exact form as

\[
 \chi_{k,c}(\lambda)
 =a_{k,c}\lambda^2+B_{k,c}\lambda+a_{k,c},             \tag{14}
\]

and put \(\rho=-\lambda\). The stable-magnitude polynomial is therefore

\[
 p_{k,c}(\rho)
 =a_{k,c}\rho^2-B_{k,c}\rho+a_{k,c}.                  \tag{15}
\]

The exact coefficient pairs are

\[
\begin{array}{c|c|r|r}
 c&k&a_{k,c}&B_{k,c}\\ \hline
 5/13&0,2&
 127417091906251505055019140625&
 3962371610825721602827025599106\\
 5/13&1,3&
 96695624036307976527392578125&
 238964531421974037129547858425706\\
 3/5&0,2&
 8465566947515869140625&
 234369399320455883852546\\
 3/5&1,3&
 210922496818387890625&
 1098683146867769276340242
\end{array}                                           \tag{16}
\]

Thus

\[
 \operatorname{tr}M_{k,c}=-{B_{k,c}\over a_{k,c}}.    \tag{17}
\]

In full, the four distinct parity-fixture traces are

\[
\begin{aligned}
 \operatorname{tr}M_{0,2;5/13}
  &=-{3962371610825721602827025599106
       \over127417091906251505055019140625},\\
 \operatorname{tr}M_{1,3;5/13}
  &=-{238964531421974037129547858425706
       \over96695624036307976527392578125},\\
 \operatorname{tr}M_{0,2;3/5}
  &=-{234369399320455883852546
       \over8465566947515869140625},\\
 \operatorname{tr}M_{1,3;3/5}
  &=-{1098683146867769276340242
       \over210922496818387890625}.
                                                               \tag{18}
\end{aligned}
\]

Exact integer comparison gives \(B_{k,c}>2a_{k,c}>0\) in every row.
Therefore

\[
 \operatorname{tr}M_{k,c}<-2,\qquad
 (\operatorname{tr}M_{k,c})^2-4>0.                   \tag{19}
\]

Since the product of the two roots is one and their sum is below minus
two, both roots are strictly negative. Denote the root nearest zero by
\(\lambda^{\rm s}_{k,c}\) and its reciprocal by
\(\lambda^{\rm u}_{k,c}\). Exact substitution of the rational endpoints
into (14) gives the following eight isolating intervals:

\[
\begin{array}{c|c|c|c}
 c&k&\lambda^{\rm s}_{k,c}&\lambda^{\rm u}_{k,c}\\ \hline
 5/13&0,2&
 (-321901/10^7,-321900/10^7)&
 (-310655/10^4,-310654/10^4)\\
 5/13&1,3&
 (-405/10^6,-404/10^6)&
 (-2471307/10^3,-2471306/10^3)\\
 3/5&0,2&
 (-361679/10^7,-361678/10^7)&
 (-276489/10^4,-276488/10^4)\\
 3/5&1,3&
 (-192/10^6,-191/10^6)&
 (-5208943/10^3,-5208942/10^3)
\end{array}                                           \tag{20}
\]

For each stable interval the endpoint signs of \(\chi\) are \((-,+)\);
for each unstable interval they are \((+,-)\). The roots are isolated
exactly, not inferred from printed decimals. In particular,

\[
 -1<\lambda^{\rm s}_{k,c}<0,
 \qquad
 \lambda^{\rm u}_{k,c}<-1,
 \qquad
 \lambda^{\rm s}_{k,c}\lambda^{\rm u}_{k,c}=1.        \tag{21}
\]

The parity coincidences in (16)--(20) mean that each displayed interval
serves the two named momenta. They do not collapse the four momentum
checks: all four sectors were reconstructed and compared independently.

## 5. The Reproduction And The Stationarity Ledger

The exact antiperiodic formula (11), followed by Schur reconstruction,
agrees entrywise with both the direct action inverse and the independently
assembled Green kernel:

\[
 W_k=Q_k^{-1}=G_k,\qquad k=0,1,2,3.                   \tag{22}
\]

The exact matrix digests, ordered by \(k=0,1,2,3\), are

\[
\begin{array}{c|c}
 c&\text{digests}\\ \hline
 5/13&
 (\mathtt{a838a33ce20e5bc2},\mathtt{1f68c1cc9f82ab84},
  \mathtt{4a80284310f96ec9},\mathtt{d3120e1868f3b27c})\\
 3/5&
 (\mathtt{77ee56d12798196c},\mathtt{392c62215fb90500},
  \mathtt{179751538358f832},\mathtt{7ea05f946a899a53})
\end{array}                                           \tag{23}
\]

Let \(S\) be the one-fine-slice antiperiodic translation and define the
simultaneous-translation residual

\[
 D_s(k):=S^sW_k(S^s)^\dagger-W_k.                    \tag{24}
\]

Literal one-step and half-cycle stationarity both fail at full rank:

\[
\begin{array}{c|c|c|c}
 c&\operatorname{rank}D_1&
   \operatorname{rank}D_4&\operatorname{rank}D_8\\ \hline
 5/13&(8,8,8,8)&(8,8,8,8)&(0,0,0,0)\\
 3/5 &(8,8,8,8)&(8,8,8,8)&(0,0,0,0)
\end{array}                                           \tag{25}
\]

The displayed representative nonzero entries are

\[
\begin{array}{c|c|c}
 c&D_4(0,1)&D_1(0,0)\\ \hline
 5/13&
 {238394787508800\over1026791823428467}&
 -{21117345408000\over1026791823428467}\\
 3/5&
 {94899211200\over250649423107}&
 -{11700495360\over250649423107}
\end{array}                                           \tag{26}
\]

By contrast,

\[
 D_8(k)=0\quad\hbox{entrywise for every }k             \tag{27}
\]

is the exact full-torus closure. Equation (27) is not a one-step
stationarity theorem. Equations (25) and (26) separate the exact Floquet
reorganization from the stronger proposed translation identity: the
four-step companion product is exact, but neither one- nor four-fine-slice
translation makes the reconstructed pairing stationary.

## 6. The Gauge Obstruction Theorem

The relevant elementary fact is a fourth-root lemma.

**Fourth-root lemma.** Let \(M\) be a real \(2\times2\) matrix with
\(\det M=1\) and \(\operatorname{tr}M<-2\). Then \(M\) has two distinct
negative real eigenvalues. Every scalar fourth root on either eigenline
has a non-real quarter-turn phase. Moreover, \(M\) has no real
\(2\times2\) fourth root.

The first assertion is (19)--(21). If \(\lambda<0\), all solutions of
\(\mu^4=\lambda\) are exactly those in (3), and none is real. For the last
assertion, suppose a real \(2\times2\) matrix \(L\) obeyed \(L^4=M\).
The eigenvalues of \(L\) that map to a negative number must be non-real.
A real matrix supplies them as a complex-conjugate pair, whose fourth
powers are equal. But \(M\) has two distinct negative eigenvalues. This is
a contradiction.

Now let a one-step Floquet homogenization have the standard form

\[
 \binom{u_{n+1}}{u_n}=P_{n+1}L P_n^{-1}
                      \binom{u_n}{u_{n-1}},
 \qquad P_{n+4}=P_n.                                  \tag{28}
\]

Multiplying four steps shows that \(M_k\) is similar to \(L^4\). Over
\(\mathbb C\), a choice of fourth roots produces such an abstract
homogenizing gauge. A reflection-real gauge, however, must preserve the
reflection-real two-slice structure; in a reflection-real basis its
one-step matrix \(L\) is real. The fourth-root lemma therefore rules it
out for every spectrum in (20).

Hence, on the declared carrier and fixtures,

\[
 \boxed{\text{no reflection-real one-step-stationary gauge exists
 for this action.}}                                  \tag{29}
\]

The qualifier is essential. Equation (29) does not rule out a complex
Floquet gauge, a nonlocal construction, a larger doubled real carrier, or
a pairing completed by an additional reflection intertwiner. It says that
the Block 117 Toeplitz-window repair cannot be obtained by a
reflection-covariant real one-step gauge of the displayed two-slice
action.

This is why the Block 117 mismatch survives action reconstruction. A
complex quarter-turn can flatten the micro-motion algebraically, but it
does not furnish a reflection-real translation on which the desired
one-step OS windows could be based. The obstruction is structural for
reflection-covariant one-step windows and no broader.

## 7. The Dressed Micro-Motion Identity

Let \(W_k\) be the exact inverse in (22), and let \(A_k\) denote the
declared action-covariance dressing in the finite-carrier reconstruction.
The adjacent-window mismatch from Block 117 is reproduced by

\[
\begin{aligned}
 q_k
 &:=Y_{01}-Y_{12}\\
 &=\overline{(A_kW_k)_{4,2}-(A_kW_k)_{5,1}}.
                                                               \tag{30}
\end{aligned}
\]

Exact differentiation after substitution gives

\[
 {\partial q_k\over\partial\tau_0}
 ={\partial q_k\over\partial\tau_1}
 ={\partial q_k\over\partial\tau_2}=0.                \tag{31}
\]

Thus the parameter independence diagnosed in Block 117 is recovered
inside the action calculation. It is not imported as an expected
constant.

To expose the role of the dressing, split

\[
 q_{k,c}=R_c+\delta_{k,c},                             \tag{32}
\]

where \(R_c\) is the undressed adjacent-time defect and
\(\delta_{k,c}\) is the \(A_k\)-correction. At the primary fixture,

\[
\begin{array}{c|c|c|c}
 k&q_{k,5/13}&R_{5/13}&\delta_{k,5/13}\\ \hline
 0&
 {355348797912000\over1026791823428467}&
 {293040926496000\over1026791823428467}&
 {62307871416000\over1026791823428467}\\
 2&
 {228512035080000\over1026791823428467}&
 {293040926496000\over1026791823428467}&
 -{64528891416000\over1026791823428467}
\end{array}                                           \tag{33}
\]

At the second fixture,

\[
\begin{array}{c|c|c|c}
 k&q_{k,3/5}&R_{3/5}&\delta_{k,3/5}\\ \hline
 0&
 {86496072000\over250649423107}&
 {62924832000\over250649423107}&
 {23571240000\over250649423107}\\
 2&
 {35364504000\over250649423107}&
 {62924832000\over250649423107}&
 -{27560328000\over250649423107}
\end{array}                                           \tag{34}
\]

The equal middle entries of the last two columns in (33) and (34) are the
momentum-independent raw defects. The common denominators within each
fixture are a useful exact fingerprint: the dressed constant is obtained
by an additive correction in the same rational action field, not by
fitting or separately normalizing the two windows.

The corrections differ in both sign and magnitude between \(k=0\) and
\(k=2\). Therefore the undressed proposed equality fails, and the action
dressing is essential to reproduce the Block 117 constants. Conversely,
(30)--(34) do not make the full pairing stationary: they explain the
nonzero mismatch exactly. Together with (25), the identity locates that
mismatch in the slice-dependent Floquet micro-motion.

## 8. The Degenerations And The Moment Quotient

There are two distinct action-pairing attempts, and neither is a positive
OS package.

**Undressed torus pairing.** Equation (22) implies

\[
 \operatorname{rank}Q_k=\operatorname{rank}W_k=8
 \quad(k=0,1,2,3),                                    \tag{35}
\]

at both fixtures. The torus translation-rank ledger is exactly (25):
\(D_1\) and \(D_4\) have rank eight in every sector, while \(D_8=0\).
The undressed torus form is non-Hermitian,

\[
 W_k-W_k^\dagger\ne0.                                 \tag{36}
\]

Full rank in (35) does not repair (36). A non-Hermitian form has no
positive-definite Hermitian inertia, so this inverse kernel does not
supply an OS Hilbert space.

**Half-space stable split.** Put

\[
 \rho_{k,c}:=-\lambda^{\rm s}_{k,c}\in(0,1).
                                                               \tag{37}
\]

With eight internal modes per full cell, organized as \(2\times4\), the
exact stable-split blocks obey

\[
 H_k[m,n]_{r,s}
 =\overline{B_k[-(m+n+1)]_{r,\,7-s}}
 =\rho_{k,c}^{\,m+n}H_k[0,0]_{r,s}.                  \tag{38}
\]

Thus the half-space form is geometric-Hankel exactly. Its local rank
ledger is

\[
 \operatorname{rank}H_k[0,0]=1,\qquad
 \operatorname{rank}\!\left(H_k[0,0]-H_k[0,0]^\dagger\right)=2.
                                                               \tag{39}
\]

In particular, \(H_k[0,0]\) is non-Hermitian; Hermitian inertia is
undefined and positive definiteness fails. The assembled two-moment
super-window also has rank one. If \(\mathcal H^{(0)}_k\) is the source
window and \(\mathcal H^{(1)}_k\) is the window with both half-space
indices advanced once, then

\[
 \mathcal H^{(1)}_k=\rho_{k,c}^2\mathcal H^{(0)}_k,
 \qquad
 \det\!\left(
  z\mathcal H^{(0)}_k-\mathcal H^{(1)}_k
 \right)\equiv0.                                     \tag{40}
\]

The determinant pencil vanishes because both windows share the same
rank-one range and radical. It does not return a nonsingular transfer
spectrum.

Quotient that common radical only as a moment-space algebraic operation.
The resulting one-dimensional quotient is multiplied by

\[
 \beta_{k,c}:=\rho_{k,c}^2.                           \tag{41}
\]

Using the exact pairs \((a_{k,c},B_{k,c})\) in (16), elimination of
\(\rho\) from (15) and \(\beta=\rho^2\) gives the exact minimal
polynomial

\[
 m_{k,c}(\beta)
 =a_{k,c}^2\beta^2+
   (2a_{k,c}^2-B_{k,c}^2)\beta+a_{k,c}^2.             \tag{42}
\]

The exact isolating intervals printed by the certificate are

\[
\begin{aligned}
 \beta_{0,2;5/13}\ &\in
 \left(
 {1036202268192599364481\over1000000000000000000000000},
 {10362022682569795561\over10000000000000000000000}
 \right),\\
 \beta_{1,3;5/13}\ &\in
 \left(
 {40934256022421281\over250000000000000000000000},
 {163737024898973761\over1000000000000000000000000}
 \right),\\
 \beta_{0,2;3/5}\ &\in
 \left(
 {81757155275609062921\over62500000000000000000000},
 {1308114484482080737449\over1000000000000000000000000}
 \right),\\
 \beta_{1,3;3/5}\ &\in
 \left(
 {1474215264951121\over40000000000000000000000},
 {2303461375483321\over62500000000000000000000}
 \right).
                                                               \tag{43}
\end{aligned}
\]

Every interval in (43) is a subset of \((0,1)\). There are no higher
stable-root products on this rank-one quotient:

\[
 \boxed{\text{the quotient root is exactly }\beta=\rho^2\in(0,1).}
                                                               \tag{44}
\]

This is the first contractive transfer value of the campaign, but the
logical firewall is absolute: **there is no positive OS space in this
construction yet.** The source form is non-Hermitian before the quotient,
and no positive Hermitian form on the quotient has been constructed.
Accordingly, (44) is a moment-quotient contraction factor, not an OS
contraction. A reflection intertwiner must first turn the geometric-Hankel
kernel into a Hermitian positive package and must do so simultaneously in
the declared sectors.

## 9. No-Go Discipline Gate

There is exactly one bounded finite-carrier wall.

- W1 — **REFLECTION-REAL ONE-STEP STATIONARITY AND NAIVE-PAIRING
  WALL:** no reflection-real one-step-stationary gauge exists for the
  displayed action. The exact determinant-one monodromies have two
  distinct negative eigenvalues, so every eigenline fourth root carries a
  non-real quarter-turn phase and no real two-by-two fourth root exists.
  Independently, the displayed naive action pairings furnish no positive
  OS Hilbert space: the torus inverse is non-Hermitian, and the
  stable-split geometric-Hankel form is rank one but non-Hermitian with
  rank-two anti-Hermitian part and an identically zero window pencil.

The wall is narrow. It concerns the primary finite carrier, the two
rational shear fixtures, the four fixed momenta, reflection-covariant
one-step windows, and the two displayed naive action pairings. Its
strongest mechanism is the fourth-root lemma applied to the exact
monodromy spectra in (16)--(21).

W1 is not an OS no-go and not an impossibility theorem for the OS
package. It does not rule out
a complex Floquet gauge, a larger real carrier, a nonlocal completion, or
a reflection intertwiner. It does not turn the quotient factor
\(\rho^2\) into an OS contraction. The simultaneous reflection-intertwiner
completion is live and named.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). The gauge wall,
the underlying spectrum, the inverse reconstruction, the degenerations,
the dressed identity, and the live completion are kept separate.

1. **PROVED — one-step homogenizing gauge / negative-eigenvalue
   fourth-root lemma / no reflection-real one-step-stationary gauge.**
   Equations (3) and (28)--(29) are the strongest row. Every eigenline
   fourth root has a non-real quarter-turn phase, and a real two-by-two
   fourth root would force the two distinct negative eigenvalues to
   coincide.
2. **PROVED — four-step two-slice monodromy / telescoping companion
   determinant and exact trace inequality / reciprocal strictly negative
   eigenvalue pair.** Equations (12)--(21) give determinant one, rational
   trace below minus two, and the eight exact isolating intervals at both
   fixtures.
3. **PROVED — antiperiodic action inverse / exact Green-kernel
   reconstruction and translation residuals / reproduction plus
   stationarity ledger.** Equations (22)--(27) prove
   \(W_k=Q_k^{-1}=G_k\), full-rank \(D_1,D_4\), and exact \(D_8=0\).
4. **PROVED — naive torus and stable-split pairings / exact Hermiticity,
   rank, Hankel, and pencil tests / degeneration ledger with the
   one-dimensional quotient contraction.** Equations (35)--(44) prove
   non-Hermiticity, rank one, zero determinant pencil, and
   \(\beta=\rho^2\in(0,1)\) without a positive OS form.
5. **PROVED — Block 117 adjacent-window constants / exact dressed action
   covariance and additive raw-plus-correction splits / action-level
   reproduction of the non-stationarity.** Equations (30)--(34) give the
   exact shared-denominator fingerprints and show that the dressing is
   essential.
6. **UNTESTED — LIVE — simultaneous reflection intertwiner / complete
   the geometric-Hankel kernel to a Hermitian positive form in every
   declared sector / candidate positive OS package.** This
   UNTESTED-LIVE route remains open and is not counted as an attempted
   route beyond W1.

### N2 — Wall-Independence Audit

There is one current wall, so no pairwise current-wall table is needed. It
is distinct from Block 117's W1, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:508-533`.

Block 117 studied an algebraic family of displayed Gram charts. Its wall
was a window identity: equal middle diagonals collapsed the pencil value
at one to a fixed nonzero negative square, so every positive point in the
displayed families had roots strictly straddling one. That is a
chart-family statement about candidate Gram data.

The present wall studies a different object. It starts from the
fixed-momentum action, derives its two-slice companions and monodromy, and
asks whether their four-step micro-motion can be made
reflection-real and one-step stationary. The obstruction is the negative
Floquet spectrum and its unavoidable quarter-turn fourth roots. It is a
gauge/action statement, not an equal-diagonal chart identity.

The connection is explanatory rather than circular. The dressed identity
(30) reproduces Block 117's constants from the action covariance, while
the full-rank residuals and fourth-root lemma explain why a real
one-step Toeplitz repair does not emerge from this action. Block 117 does
not imply the monodromy spectrum, and the monodromy spectrum does not
re-prove the full displayed self-chart classification.

The naive-pairing failures are independent again. They follow from direct
non-Hermiticity and rank calculations, not from the negative-square window
identity. The moment quotient's \(\rho^2\) root survives those
degenerations algebraically but carries no positive form.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.

| lowercase hit | classification |
|---|---|
| primary finite carrier | exact bounded carrier, not a continuum statement |
| both rational shear fixtures | exactly \(c=5/13\) and \(c=3/5\) |
| fixed-momentum action | four independently reconstructed momentum sectors |
| pentadiagonal in fine time | exact support statement (7) |
| slice-varying two-slice companions | exact Schur-reduced recurrence, not a constant companion |
| four-step Floquet monodromy | ordered product (1), not one-step stationarity |
| determinant one exactly | telescoping exact identity (13) |
| real rational trace below minus two | four exact trace values (18)--(19) |
| both eigenvalues are strictly negative | exact consequence of trace and determinant |
| eight isolating intervals | exact rational endpoint tests in (20) |
| non-real quarter-turn fourth root | exact fourth-root phases (3) |
| no reflection-real one-step-stationary gauge exists | narrow gauge theorem (29) |
| reflection-covariant one-step windows | exact scope of the gauge obstruction |
| Block 117 window obstruction is structural | action-level explanation, not a new chart classification |
| exact dressed identity | covariance identity (30) with exact derivatives |
| Block 117 constants | exact values reproduced, not imported as targets |
| action covariance | the exact \(A_kW_k\) entries in (30) |
| dressing corrections | additive terms in (33)--(34) |
| shared-denominator fingerprint | exact rational-field check at each fixture |
| undressed torus pairing is non-Hermitian | explicit failure (36) |
| half-space stable-split pairing | displayed stable-eigenline construction only |
| exactly geometric-Hankel rank-one non-Hermitian form | identities (38)--(39) |
| window pencil vanishes identically | rank-one degeneration (40) |
| one-dimensional moment quotient | radical quotient only, not an OS completion |
| contractive root rho^2 in (0,1) | exact quotient factor (41)--(44) |
| first contractive transfer value of the campaign | algebraic quotient result with firewall |
| no positive pairing yet | explicit OS firewall |
| reflection-intertwiner completion | untested-live construction route |
| positive OS Hilbert space | explicitly not constructed |
| curved OS positivity | explicit reconstruction firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting firewall |
| no TOE percentage moves | TOE accounting firewall |
| retained-positive end-to-end theory count remains zero | audit-status accounting |
| actual ADM/history transporter remains | partial-closure statement only |
| gravity constraint quotient remains unexecuted | downstream gravity firewall |
| N1 N2 N3 N4 N5 N6 N7 N8 | every discipline gate is present |
| W1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | the five N5 resolution keys |

No phrase upgrades the reflection-real gauge wall into impossibility of the
OS package, asserts that no intertwiner exists, treats the quotient factor
as an OS contraction, supplies a positive Hilbert space, completes curved
OS reconstruction, authorizes gravity, or moves TOE accounting.

### N4 — Residual Matching

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 117 Next Decision](ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md), docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:778-792 | derive the stationary Toeplitz-window action pairing, re-run the transfer program, then form the gravity constraint quotient | the action pairing is derived exactly, but its Floquet spectrum bars a reflection-real one-step-stationary gauge and both naive forms fail Hermiticity; the reflection intertwiner and gravity remain |
| [Block 117 stationarity diagnosis](ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md), docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:437-506 | explain the fixed adjacent-window mismatch and construct an action-derived Toeplitz repair | the dressed identity reproduces the fixed mismatch, while full-rank \(D_1,D_4\) and the fourth-root obstruction show why the naive action inverse is not that repair |
| [Block 116 chart wall](ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md), docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md:467-492 | the displayed transfer data did not furnish a stationary one-step semigroup and left the modular/action route open | the four-cell Floquet micro-motion and its non-real fourth roots explain the inherited non-semigroup behavior without claiming that every completion fails |
| [Block 115 windows](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md), docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md:194-217 | compare consecutive positive one-step windows and seek a contractive transfer | the full stable-split pencil degenerates identically, while its one-dimensional moment quotient has the exact factor \(\rho^2\in(0,1)\) but no positive OS form |

Every inherited residual reaches exactly its stated interface. No citation
is used as an audit verdict.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the primary finite carrier at
both rational fixtures, the exact four-step monodromy has determinant one
and rational trace below minus two, so no reflection-real
one-step-stationary gauge exists; the naive torus and stable-split action
pairings furnish no positive OS package, although the rank-one moment
quotient has the exact contractive factor \(\rho^2\in(0,1)\).”

Forbidden upgrades include “the OS package is impossible,” “no intertwiner
exists,” and “the contraction is an OS contraction.” Also forbidden are
“no stationary construction exists,” “every Floquet completion is
non-Hermitian,” “the quotient is already a positive Hilbert space,” “the
ADM/history transporter is finished,” “the gravity constraint quotient can
now be executed,” “an axiom amendment is required,” and “audit retention
follows from this note.”

The five resolution lines from the runner specification are reproduced
verbatim:

```text
N5: per_element: exact pentadiagonal, companion, monodromy, inverse, stationarity-residual, dressed-identity, rank, and root-isolation identities are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: all four fixed momenta at c=5/13 and c=3/5 have determinant-one negative Floquet spectra, with exact inverse and degeneration ledgers
per_block: no reflection-real one-step-stationary gauge exists for this action, while the one-dimensional moment quotient has beta=rho^2 in (0,1) without a positive OS form
lattice_wide: checked and not executed — the reflection intertwiner, positive OS Hilbert space, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The remaining decisions are completion
of the pairing and downstream reconstruction problems.

| route | present status | remaining terminal |
|---|---|---|
| pentadiagonal action | exact four-cell two-slice reduction at both fixtures | none for displayed support and recurrence |
| Floquet determinant | exact telescoping determinant one | none for the displayed monodromies |
| Floquet spectrum | exact traces below minus two and eight negative-root intervals | none for the displayed spectra |
| reflection-real gauge | ruled out by the fourth-root lemma | none for narrow W1 |
| inverse reproduction | exact \(W_k=Q_k^{-1}=G_k\) in all four modes | none for the torus reconstruction |
| stationarity ledger | \(D_1,D_4\) full rank and \(D_8=0\) | none for the displayed translation tests |
| dressed micro-motion | exact Block 117 constants and additive splits | none for the displayed identity |
| undressed torus pairing | full rank but non-Hermitian | naive route supplies no positive OS form |
| stable-split pairing | geometric-Hankel, rank one, non-Hermitian, zero pencil | complete Hermiticity and positivity |
| moment quotient | exact one-dimensional factor \(\rho^2\in(0,1)\) | construct a positive form before any OS interpretation |
| reflection intertwiner | untested-live | find one canonical simultaneous intertwiner for all declared sectors |
| OS axioms | not executed on a completed pairing | re-run Hermiticity, positivity, reflection, and composition |
| gravity route | not executed | complete transport, then form the gravity constraint quotient |

The scan finds no axiom-amendment route. The Block 117 action-pairing
opening is partially closed: the action covariance, monodromy, exact
inverse, and quotient factor are now determined. The desired
reflection-real one-step gauge and the two naive positive-pairing routes
close by exact mechanisms. The reflection-intertwiner completion stays
live, so positive OS reconstruction and gravity do not close.

### N7 — Steelman

**Hostile steelman against the gauge wall.** An abstract homogenizing gauge
does exist over \(\mathbb C\). Choosing one of the four roots in (3) on
each eigenline flattens the four-step dynamics. Therefore a statement that
“no one-step gauge exists” would be false.

The exact answer keeps the reflection-reality qualifier. The theorem bars
only a reflection-real two-by-two one-step gauge on the declared action.
The non-real quarter-turn is the mechanism, not evidence against complex
Floquet theory, enlargement of the carrier, or a different completed
pairing.

**Hostile steelman against the quotient firewall.** The scalar
\(\beta=\rho^2\) is exact and lies strictly between zero and one. In a
one-dimensional positive Hilbert space that would be a perfectly good
contraction. Why not call it an OS contraction now?

Because the form from which the quotient was taken is non-Hermitian, and
the certificate has not supplied a positive Hermitian form on the quotient.
Contractivity is a norm statement, not only a scalar inequality. Equation
(44) is therefore an algebraic moment-quotient transfer value until a
positive form is constructed.

**Hostile steelman for the live route.** A reflection intertwiner might
exist trivially pointwise. Each rank-one block can often be made Hermitian
after a basis-dependent left-right identification. Thus the remaining
construction may be much easier than the wall suggests.

That possibility is preserved. The open question is not pointwise
existence for one matrix; it is a canonical simultaneous intertwiner that
respects reflection, the action covariance, both fixtures, all declared
momenta, and the translation/composition structure. This block neither
constructs nor rules out that object.

These steelmen do not weaken narrow W1. A reflection-real two-by-two
fourth root is impossible for every exact spectrum in (20), and the two
displayed naive forms fail the stated Hermiticity tests exactly. They do
prevent any upgrade to a global OS no-go or to an OS interpretation of
\(\rho^2\).

### N8 — Cross-Cycle Echo

The twelve prior campaign blocks each narrowed the hunt; the discipline
held.

| campaign block | narrowing that led to the present wall |
|---|---|
| Block 106 | fixed the local dual-descent entry and preserved the action-to-Gram order |
| Block 107 | isolated the finite two-history seam carrier |
| Block 108 | tested the locality reach of involutive seam dressing |
| Block 109 | forced the dressing search to global support |
| Block 110 | restricted the viable signature to the even sector |
| Block 111 | factorized the positivity frontier and displayed the self-block involution families |
| Block 112 | exposed the paired even-parity branch and its count |
| Block 113 | refuted the paired floor and located the mixed-circle crossing |
| Block 114 | supplied the exact positive chart and endpoint beyond the certified crossing |
| [Block 115 transfer gap](ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md), docs/ADMISSIBILITY_DIRAC_KAHLER_TRANSFER_SPECTRUM_SELECTION_GAP_BOUNDED_THEOREM_NOTE_2026-08-15.md:194-338 | separated Hilbert positivity from transfer contractivity on the displayed windows |
| [Block 116 chart wall](ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md), docs/ADMISSIBILITY_DIRAC_KAHLER_CHART_INVARIANT_CONTRACTIVITY_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-08-15.md:467-492 | proved the paired-chart freeze and left self-block and action routes open |
| [Block 117 stationarity wall](ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md), docs/ADMISSIBILITY_DIRAC_KAHLER_SELF_CHART_EMPTINESS_STATIONARITY_BOUNDED_THEOREM_NOTE_2026-08-16.md:43-114 | closed the displayed self charts by exact negative squares and diagnosed Toeplitz stationarity as the next construction |

The current block follows the same discipline. It constructs the declared
finite action pairing, keeps its slice-varying micro-motion, proves the
negative Floquet spectrum, reports the failed stationarity identities,
reproduces the prior mismatch through the dressing, and retains the
\(\rho^2\) quotient only behind a non-Hermiticity firewall. The wall stays
narrow and the reflection-intertwiner route stays live.

**No-Go Discipline verdict:** **PASS** only for narrow W1: no
reflection-real one-step-stationary gauge exists for the displayed action,
and the displayed naive torus and stable-split pairings furnish no positive
OS package by their exact non-Hermiticity and rank mechanisms. **FAIL**
for impossibility of the OS package, nonexistence of an intertwiner, an OS
interpretation of the quotient contraction, a completed positive Hilbert
space, a completed ADM/history transporter, gravity, axiom necessity,
audit retention, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. The pentadiagonal support, companion
reduction, telescoping determinant, rational traces, negative-root
isolations, inverse reproduction, residual ranks, dressed identities,
non-Hermiticity, geometric-Hankel factorization, rank certificates, zero
pencil, quotient minimal polynomials, and \((0,1)\) isolations are finite
consequences of the displayed carrier and fixtures. No new primitive is
assumed.

This is bounded route progress, not an audit-grade assignment. It retires
no end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. construct the reflection intertwiner that completes the rank-one
   geometric-Hankel action pairing to a Hermitian positive package;
2. re-run the OS axioms on that completed pairing, including reflection,
   positivity, translation, and composition; and
3. then form the gravity constraint quotient.

The actual ADM/history transporter remains unexecuted beyond the displayed
Floquet monodromy theorem, reflection-real gauge obstruction, exact
dressed identity, and algebraic moment quotient.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted.
