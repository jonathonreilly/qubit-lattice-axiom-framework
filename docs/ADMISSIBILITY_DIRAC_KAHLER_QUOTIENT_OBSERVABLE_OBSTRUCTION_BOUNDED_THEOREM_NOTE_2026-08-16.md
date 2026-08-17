---
claim_id: admissibility_dirac_kahler_quotient_observable_obstruction_bounded_theorem_note_2026-08-16
claim_type: bounded_theorem
claim_scope: "On the certified half-space OS package at both rational shear fixtures, no local routed U(1) current descends to a conserved observable on the quotient -- the site-resolved Ward recursion fails at every site with residual exactly the quotient compression of the commutator [E_z,Q], the current kernels map the OS null space out of itself and fail reflection-adjointness, and the obstruction is structural in the local routed class because routing changes shift the current only by a discrete curl leaving the divergence identity untouched -- while the compressed current values have the exact closed form rho^{2m} times an affine root-field residue (the geometric factor structural, the residues the falsifiable content), the whole-cell recursion is vacuous by construction and is labeled as such rather than claimed as a conservation law, the flux zero-masks are convention-dependent and displayed only with their exact conventions, and the stress-tensor source, non-local dressings, the populated open-carrier quotient, naturality, curved OS positivity, the completed ADM/history transporter, joint gravity, the gravity constraint quotient on a populated carrier, Records, retention, axiom amendment, obligation retirement, and TOE percentage movement are not claimed."
depends_on:
  - admissibility_dirac_kahler_constraint_quotient_coupling_bounded_theorem_note_2026-08-16
runner: scripts/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.py
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: admissibility_dirac_kahler_constraint_quotient_coupling_bounded_theorem_note_2026-08-16
target_blocker_text: "Prove or refute the Ward/transfer-covariance of the current bilinears on the OS quotient, then the populated sourced quotient on an open or background carrier, and the naturality classification."
source_of_blocker_text: handoff
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Pose the stress-tensor source and non-local current dressings on the open/background carrier; then the naturality classification and curved OS positivity."
conditional_surface_status: "audited_conditional expected (dependency_not_retained; Blocks 103-121 content-bound unaudited)"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact rank-one quotient-compression identity, exact nonzero site-resolved Ward residuals, exact OS-null-space and reflection-adjointness failures, exact routing-curl invariance, and exact rho^{2m} affine root-field current residues on the certified half-space package at both rational shear fixtures; dependencies are content-bound unaudited, so bounded"
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# The Quotient-Observable Obstruction

**Date:** 2026-08-16

**Campaign block:** 122

**Type:** `bounded_theorem`

**Audit authority:** none. Independent audit alone may assign a verdict.

**Constitutional effect:** none. No action is adopted and no axiom is edited.

**TOE accounting:** zero obligation retirement. No TOE percentage moves. The
retained-positive end-to-end theory count remains zero.

**Primary runner:**
[`scripts/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.py`](../scripts/admissibility_dirac_kahler_quotient_observable_obstruction_2026_08_16.py)

## 1. Result Up Front

[Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md)
closed onto the following handoff next gate, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md:16`
and elaborated at
`docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md:1157-1174`:

> Prove or refute the Ward/transfer-covariance of the current bilinears on
> the OS quotient, then the populated sourced quotient on an open or
> background carrier, and the naturality classification.

**THE OBSTRUCTION.** On the certified half-space OS package at each rational
shear fixture $c=5/13$ and $c=3/5$, none of the local routed U(1) currents
displayed in Block 121 defines a conserved observable on the positive
quotient. For every momentum $k=0,1,2,3$ and every one of the 32 sites, the
compressed site Ward residual is

\[
 \mathcal W_{k,z}
 =\frac{y_k^\dagger\widehat{[E_z,Q]}_k y_k}
        {y_k^\dagger y_k}\ne0 .                     \tag{1}
\]

The zero count is `0/32` in every momentum sector at both fixtures. This is
not a tolerance statement: the root-field reductions are exactly nonzero.
The same current kernels fail the two operator conditions required for an
observable on the OS quotient. They do not preserve the OS null space, and
they do not satisfy reflection-adjointness with respect to the reflection
form $K_{\Theta,k}$.

The failure is structural throughout the **LOCAL ROUTED** class. Changing a
route changes the current only by a discrete curl. The divergence remains
the endpoint identity

\[
 \Delta_t^-J_z+\Delta_x^-S_z
 =\bar\phi[E_z,Q]\psi .                              \tag{2}
\]

After quotient compression, the right-hand side of (2) remains nonzero at
every site. A curl cannot change it. Thus local rerouting cannot turn this
family into a conserved quotient observable.

**What survives.** Block 121's off-shell microscopic conservation identity
survives without qualification: (2) is the exact divergence-commutator
identity, and its divergence vanishes when both microscopic Euler equations
are imposed. The present negative quotient result does not revise that
theorem. The exact compressed scalar data also survive. For either current
component $O\in\{J,S\}$,

\[
 o_k(m,a,x)
 =\rho_k^{2m}\bigl(A^O_{ka}+B^O_{ka}\rho_k\bigr),
 \qquad m\ge0,                                      \tag{3}
\]

with exact affine residues in the quadratic root field of $\rho_k$. The
$\rho_k^{2m}$ factor is forced by rank-one quotient geometry. It is therefore
structural. The exact residues, their zero patterns, and their coordinate
hashes are the falsifiable content.

**What earns no theorem credit.** The whole-cell recursion

\[
 j_k(m+1)-\rho_k^2j_k(m)=-\nabla_x^-s_k(m)=0         \tag{4}
\]

is vacuous by construction: quotient propagation supplies the first zero,
and spatial uniformity supplies the second. It does not test the local Ward
law and is not claimed as a conservation law. Likewise, flux zero-masks
depend on the exact link and slice convention. They are displayed only with
those conventions, never as invariant zeros. The checker discipline is
plain: exact but automatic equalities are reported, labeled **VACUOUS**, and
excluded from the positive theorem count.

This theorem is deliberately narrow. The stress-tensor source, non-local
current dressings, the populated open-carrier quotient, naturality, curved
OS positivity, the completed ADM/history transporter, joint gravity, the
gravity constraint quotient on a populated carrier, Records, audit
retention, axiom amendment, obligation retirement, and TOE percentage
movement remain outside it.

## 2. Authority And Executed Contract

Current axiom authority is
[MINIMAL_AXIOMS_2026-06-29.md](MINIMAL_AXIOMS_2026-06-29.md) at
`origin/main 4e566b14a6352a9a62590252a9755c7a103c1b9e`, with axiom blob
`bc23300becfe4e4db57153c0e94cfcdf2338da71` and registry blob
`b93959cca4f7e26c673cdccbe601e50c3cb93daa`. The authority snapshot is
unchanged from Block 121.

The exact stacked parent is
[Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md)
commit `1714abeefcf3763c0bfe001f30fd14521c538622`, content-bound through
note blob `1e0013d0c6ab54e2f31aefeb5489796a28137e31`. Its relevant inherited
positive package comes from
[Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md).
No audit verdict is imported from either note.

The executed contract is:

1. the certified rank-one half-space OS package at both rational shear
   fixtures $c=5/13$ and $c=3/5$, all momenta $k=0,1,2,3$, and all 32
   site labels per momentum;
2. the exact compression of Block 121's routed time and spatial current
   kernels, with the antiperiodic signs and the inherited reflection cut;
3. the normalized quotient scalars and the rank-one projector identity;
4. every site-resolved ordinary Ward residual and every microscopic
   $\rho_k^2$-recursion residual;
5. left and right OS-null-space descent for both current components and
   reflection-adjointness with respect to $K_{\Theta,k}$;
6. the quadratic stable-root polynomials, the affine root-field reduction
   of every compressed value, and exact coordinate hashes;
7. the density and flux support masks with their conventions exposed;
8. the whole-cell recursion, classified as vacuous rather than as local
   conservation; and
9. one no-go only for the displayed package, fixtures, and **LOCAL ROUTED**
   U(1) class, leaving non-local dressings, the stress tensor, richer
   carriers, naturality, curved OS positivity, and gravity open.

The supplied exact computation was replayed. It ends with
`TOTAL: PASS=1908 FAIL=0`; the supplied scratch report records a runtime of
`298.340` seconds, and the independent replay took `313.419` seconds. Runtime
is not theorem content.

The replay's decision footer is reproduced exactly:

```text
DECISION: the compressed current has exact rho^(2m) whole-cell covariance, but the routed density/current family neither descends through the OS null space nor satisfies K_Theta reflection-adjointness; therefore it is not an OS-compatible conserved-current operator on the certified package.
RUNTIME_SECONDS: 313.419
TOTAL: PASS=1908 FAIL=0
```

The scope is the inherited finite half-space package, both fixtures, the four
momentum sectors, the displayed routed U(1) density/current kernels, and the
rank-one OS quotient. The source is still the U(1) proxy, not the physical
stress tensor. No open/background carrier is populated, no non-local
dressing is constructed, and no curved or gravity reconstruction follows.

## 3. The Compression And The Structural-Uniformity Lemma

For a routed kernel $O\in\{J,S\}$, define its momentum and reflection-cut
compression by

\[
 \widehat O_k(a,x)
 =C P_kF^\dagger O\bigl((a+4)\bmod8,x\bigr)
   FP_k^\dagger C^{\mathsf T}.                       \tag{5}
\]

Here $J$ is Block 121's routed temporal component and $S$ is its routed
spatial component. The certified reflection form in each momentum sector is
rank one:

\[
 K_{\Theta,k}=\Theta H_{00,k}=y_ky_k^\dagger,
 \qquad N_k:=y_k^\dagger y_k>0,
 \qquad P_k^{\rm OS}:=\frac{y_ky_k^\dagger}{N_k}.    \tag{6}
\]

The compressed quotient value is

\[
 \omega_k(O;a,x)
 :=\frac{y_k^\dagger\widehat O_k(a,x)y_k}{N_k}.      \tag{7}
\]

**Structural-uniformity lemma.** Let $e_i$ be the local Dirac--Kahler basis
vector and let $F_k$ be the momentum-$k$ embedding. For every site projector,

\[
 F_k^\dagger E_{(i,x)}F_k
 =\frac14 e_ie_i^{\mathsf T},
 \qquad\text{independently of }x.
\]

Thus every momentum-diagonal site compression is spatially uniform. This is
a symbolic projector identity, not a numerical finding. In addition, every
kernel $O$ on the displayed one-dimensional quotient obeys the rank-one
compression identity

\[
 P_k^{\rm OS}\widehat O_k(a,x)P_k^{\rm OS}
 =\omega_k(O;a,x)P_k^{\rm OS}.                      \tag{8}
\]

This is the rank-one projector identity. If a quotient state is propagated
$m$ cells, the stable multiplier $\rho_k$ occurs once in the ket and once in
the bra. Hence

\[
 \omega_k^{(m)}(O;a,x)
 =\rho_k^{2m}\omega_k(O;a,x).                       \tag{9}
\]

Equation (9) is geometric, not a Ward theorem. Any inserted kernel would
obey the same scalar covariance after compression to this rank-one carrier.
That is why the $m$-factor in (3) is structural.

The density values are stronger than a generic rank-one statement. At both
fixtures they are nonzero at every site:

\[
 \#\{z:j_k(0,z)=0\}=0
 \quad\text{for every }k=0,1,2,3.                  \tag{10}
\]

Equivalently, the density support mask in the ordered slice convention
$a=0,1,\ldots,7$ is `11111111` for every $k$. Each slice row is spatially
uniform, so (10) covers all $8\times4=32$ sites per momentum. The
nonvanishing is exact in the relevant quadratic root field.

Spatial uniformity has a limited consequence:

\[
 \nabla_x^-s_k(m,a,x)=0.                            \tag{11}
\]

It does not make the site commutator in (1) vanish. Confusing (11) with the
site-resolved identity discards precisely the local information that the
quotient-observable gate was designed to test.

## 4. The Residue Closed Form

Write $p(r)=p_0+p_1r+p_2r^2$. At $c=5/13$, the exact stable-root
polynomials are

\[
\begin{aligned}
 p_{\rm even}(r)={}&
 127417091906251505055019140625
 -3962371610825721602827025599106r\\
 &+127417091906251505055019140625r^2,\\
 p_{\rm odd}(r)={}&
 96695624036307976527392578125
 -238964531421974037129547858425706r\\
 &+96695624036307976527392578125r^2.
                                                               \tag{12}
\end{aligned}
\]

At $c=3/5$, they are

\[
\begin{aligned}
 p_{\rm even}(r)={}&
 8465566947515869140625
 -234369399320455883852546r\\
 &+8465566947515869140625r^2,\\
 p_{\rm odd}(r)={}&
 210922496818387890625
 -1098683146867769276340242r\\
 &+210922496818387890625r^2.
                                                               \tag{13}
\end{aligned}
\]

For even $k$, $\rho_k\in(0,1)$ is the stable root of $p_{\rm even}$; for
odd $k$, it is the stable root of $p_{\rm odd}$. Set
$\beta_k=\rho_k^2$. Exact reduction modulo the relevant quadratic gives

\[
 \operatorname{red}_{p_k}
 \!\left(
  \frac{y_k^\dagger\widehat O_k(a,x)y_k}{N_k}
 \right)
 =A^O_{ka}+B^O_{ka}\rho_k,                          \tag{14}
\]

and therefore the closed form

\[
 o_k(m,a,x)
 =\rho_k^{2m}\bigl(A^O_{ka}+B^O_{ka}\rho_k\bigr),
 \qquad O\in\{J,S\}.                               \tag{15}
\]

The coefficients in (14) are exact root-field coordinates, not fitted
floating-point values. In the runner's canonical coordinate order, their
certificate hashes are:

| fixture | kernel | hashes for $k=0,1,2,3$ |
|---|---|---|
| $5/13$ | $J$ | `19e4a95126aa7d05`, `4a7cd5a411384ac7`, `b74b954e6e3c1da2`, `7f3388a11f16bc96` |
| $5/13$ | $S$ | `29856de469aaa778`, `0504d5b22ccf77f3`, `f197586c480a5341`, `8508949b08472780` |
| $3/5$ | $J$ | `0f6a6b90843f3b84`, `370f8fd243a9a858`, `f031bebabd1e4305`, `20b7f257007efafb` |
| $3/5$ | $S$ | `cf221cabf3abd176`, `aa3ccfe695257acc`, `74f1bbd4d761c5b1`, `54100ebe9d928dd3` |

These residues are the positive, falsifiable part of the calculation. A
different exact affine coordinate, zero pattern, or coordinate hash would
falsify the corresponding row. By contrast, the common
$\rho_k^{2m}$ factor tests only the rank-one propagation geometry and earns
no current-conservation credit by itself.

## 5. The Two Flux Conventions

Two actual spatial-flux conventions must be separated before any zero is
interpreted. The **full routed flux** is Block 121's signed-crossing sum over
all routed action hops:

\[
 S^{\rm full}_\ell
 =\sum_{u,v}\epsilon^x_\ell(u,v)\,
   \bar\phi_uQ_{uv}\psi_v.                          \tag{16}
\]

The **same-slice range-one flux** keeps precisely the oriented, same-time,
range-one spatial monomials from that sum:

\[
 S^{\rm ss}_\ell
 =\sum_{\substack{u,v:\ t_u=t_v\\
                   \text{oriented range-one }x\text{ hop}}}
   \epsilon^x_\ell(u,v)\,\bar\phi_uQ_{uv}\psi_v.  \tag{17}
\]

For either convention $X\in\{\mathrm{full},\mathrm{ss}\}$, define the
support bit by $M^X_{k,a}=1$ exactly when the compressed flux is nonzero, and
define the zero bit by $Z^X_{k,a}=1-M^X_{k,a}$. The bit order is exactly
$a=0,1,\ldots,7$ after the reflection-cut shift $(a+4)\bmod8$ in (5); a bit
describes the common value across all four spatial sites. At both fixtures,

\[
\begin{array}{c|c|c|c|c}
 k&M^{\rm full}_k&Z^{\rm full}_k&M^{\rm ss}_k&Z^{\rm ss}_k\\ \hline
 0&11111111&00000000&11111111&00000000\\
 1&11110111&00001000&00000000&11111111\\
 2&11111111&00000000&11111111&00000000\\
 3&11110111&00001000&00000000&11111111
\end{array}.                                        \tag{18}
\]

The exact difference is the cross-slice/range-two hop contribution, namely
the routed terms outside the oriented same-time range-one convention:

\[
 S^{\rm full}-S^{\rm ss}=S^{\rm cross/r2}.          \tag{19}
\]

Thus the odd-sector all-zero mask in the same-slice convention does not say
that the full routed flux vanishes there. Conversely, the single zero slice
of the full odd-sector flux is not an invariant zero of every current
bookkeeping. The four apparent odd-sector null-descent successes in Section
7 occur at that full-flux zero slice and carry no positive descent content.

All cross-slice terms must be restored when the local divergence is formed.
Block 121's two full link routings, $\mathcal R_{t\to x}$ and
$\mathcal R_{x\to t}$, differ by a discrete curl, so the invariant statement
is

\[
 \Delta_t^-J^{x\to t}+\Delta_x^-S^{x\to t}
 =\Delta_t^-J^{t\to x}+\Delta_x^-S^{t\to x}
 =\bar\phi[E_z,Q]\psi.                              \tag{20}
\]

Equation (20), not either mask, is the current theorem. This is the
convention lesson: expose both exact masks and their definitions, identify
their difference as cross-slice hops, and attach invariant significance only
to the complete divergence identity.

## 6. The Microscopic Ward Failure

Block 121 proved (2) before the OS quotient. Compressing that operator
identity with (7) gives

\[
 \omega_k(\Delta_t^-J+\Delta_x^-S;z)
 =\frac{y_k^\dagger\widehat{[E_z,Q]}_k y_k}{N_k}
 =\mathcal W_{k,z}.                                 \tag{21}
\]

Every entry of (21) is nonzero. In the primary runner's canonical dressed-
commutator encoding, the exact hashes in momentum order $k=0,1,2,3$ are

| fixture | exact dressed-commutator hashes |
|---|---|
| $5/13$ | `8d566f391d075188`, `0cc6a0d11b849c0f`, `febe824efdab23ea`, `2ef1fb8a117f20ef` |
| $3/5$ | `dfb1b19f307eadc7`, `ec074662236ec6d2`, `f7c4ca4ba8027dd2`, `62b64e805b826194` |

For each table entry, the exact count is

\[
 \#\{z:\mathcal W_{k,z}=0\}/32=0/32.               \tag{22}
\]

The transfer-weighted microscopic recursion was checked separately. With the
slice and dressing conventions fixed above, its residual is identified
entrywise with the dressed compressed commutator in (21). Its zero count is
also `0/32` in every momentum sector. Thus the displayed hashes certify both
the residual identity and exact nonvanishing in the runner's normalization.

The local and whole-cell statements are therefore opposite in theorem
content. Site by site, the exact compressed commutator is a nonzero source.
After the site labels are erased and only the one-dimensional cell quotient
is kept,

\[
 j_k(m+1)-\beta_kj_k(m)=0,
 \qquad -\nabla_x^-s_k(m)=0.                        \tag{23}
\]

The first equality in (23) follows from (9); the second follows from spatial
uniformity. Neither side interrogates (21). Calling (23) a conservation law
would reward the checker for losing the site-resolved data. It is instead
the exact **VACUOUS WHOLE-CELL RECURSION**.

This failure does not contradict microscopic on-shell conservation. The OS
generator $y_k$ is a representative selected by the reflection-positive
quotient; it is not asserted to solve both independent microscopic Euler
equations appearing in Block 121. The quotient-observable question asks
whether the current kernels act compatibly with that quotient, and (21)
answers no.

## 7. The Descent And Adjointness Obstructions

Let

\[
 \mathcal N_k:=\ker K_{\Theta,k},
 \qquad P_k^{\rm OS}=K_{\Theta,k}/N_k.              \tag{24}
\]

For a kernel $\widehat O_k$ to induce an operator on the OS quotient, null
representatives must remain null. The exact left and right tests may be
written

\[
 K_{\Theta,k}\widehat O_k(I-P_k^{\rm OS})=0,
 \qquad
 (I-P_k^{\rm OS})\widehat O_kK_{\Theta,k}=0.        \tag{25}
\]

For $J$, the number of passing site components out of 32 is

\[
 \text{left/right descent for }J:
 (0,0,0,0)/(0,0,0,0)                               \tag{26}
\]

at each fixture. For $S$, it is

\[
 \text{left/right descent for }S:
 (0,4,0,4)/(0,4,0,4).                              \tag{27}
\]

The four entries counted for odd $k$ in (27) are precisely the identically
zero slice in (18). They are not nonzero current operators that descend.
Thus every nonzero displayed density or flux component maps the OS null
space out of itself.

Descent is necessary but not sufficient. Reflection-adjointness requires

\[
 K_{\Theta,k}\widehat O_k
 =\widehat O_{\theta,k}^{\dagger}K_{\Theta,k},       \tag{28}
\]

where $O_\theta$ is the reflected kernel in the same link convention. The
number of exact successes out of 32 is

\[
 \text{reflection-adjointness for }J=(0,0,0,0),
 \qquad
 \text{reflection-adjointness for }S=(0,0,0,0)      \tag{29}
\]

at both fixtures. Even the zero-flux locations in (18) do not turn (28) into
a passing reflection-adjointness row because the reflected partner is part
of the equality.

The exact witness hashes are:

| fixture | $J$ witness hashes for $k=0,1,2,3$ |
|---|---|
| $5/13$ | `790c9f7324da9627`, `5a3d5610b428a18c`, `e40dc23b10274230`, `4c767406297d5ed4` |
| $3/5$ | `2ffde5a0ec067e6c`, `4a7568b849d51c12`, `bb037259a12f86b9`, `26c77f0b6da4aed1` |

| fixture | $S$ witness hashes for $k=0,1,2,3$ |
|---|---|
| $5/13$ | `3dd8943ff9cd318c`, `52c4758f27443ab4`, `dcbcf8ef92104634`, `2e1913ec8f0def80` |
| $3/5$ | `13d6877b261ca691`, `e4aed960e4fa4e6c`, `82cb1cf6feff947f`, `09cd64d6e3f3e226` |

The same zero counts hold after $k\mapsto-k$ and for either temporal-link
orientation sign. These checks close two possible loopholes: the failure is
not caused by choosing only one momentum orientation, and a sign reversal
of the temporal link does not repair it.

## 8. The Structural Classification

Define the **LOCAL ROUTED** class to contain currents obtained by assigning
each nonzero action hop a finite lattice path between the same endpoints on
the fixed lift. Two representatives may differ by elementary plaquette
boundaries but not by a non-local quotient dressing or a change of $Q$.

For any two representatives $j$ and $j'$ in this class, the routing lemma
gives

\[
 j'-j=\operatorname{curl}K,
 \qquad
 \operatorname{div}(j'-j)=0.                       \tag{30}
\]

Consequently,

\[
 \operatorname{div}j'
 =\operatorname{div}j
 =\bar\phi[E_z,Q]\psi.                              \tag{31}
\]

Compression of (31) is pinned to the same nonzero residual (21). The
site-resolved failure is therefore routing-independent even though the
individual density and flux values, their improvement terms, and their zero
masks need not be.

This classification was also checked constructively: the time-first and
space-first current kernels were recomputed separately, their difference was
certified as the exact curl (30), and their quotient residual grids agreed
entrywise at both fixtures. Thus the routing conclusion does not rest only on
an abstract improvement slogan.

There are two honest repair classes:

1. add a **non-local dressing** whose quotient divergence cancels the
   compressed commutator while its complete kernel satisfies null descent
   and reflection-adjointness; or
2. modify the charge/action data so that the relevant quotient compression
   of $[E_z,Q]$ vanishes and then recheck descent and adjointness.

Neither repair is a local rerouting. The physical stress tensor is a
different source and must be posed independently; it is not obtained by
renaming the U(1) current.

For the constraint-quotient program, this closes the local U(1)-proxy
chapter on the certified package. Block 121's microscopic source continuity
remains exact, but the local routed proxy does not survive as an observable
on the quotient that Block 119 built. The stress-tensor source, non-local
dressings, and an open/background carrier remain live. The constraint-
quotient program itself is not closed by this result.

## 9. No-Go Discipline Gate

There is exactly one bounded quotient-observable wall.

- W1 — **LOCAL ROUTED QUOTIENT-OBSERVABLE WALL:** no local routed U(1)
  current yields a conserved observable on the certified quotient. The
  structural mechanism is

  \[
   P_k^{\rm OS}\widehat{[E_z,Q]}_kP_k^{\rm OS}
   =\mathcal W_{k,z}P_k^{\rm OS}\ne0               \tag{32}
  \]

  at every site, together with failure of OS-null-space descent and
  reflection-adjointness. A routing improvement is a discrete curl and
  leaves (32) unchanged.

W1 is narrow. It covers the certified rank-one half-space OS package, the
fixtures $c=5/13$ and $c=3/5$, Block 121's displayed action and current, and
the **LOCAL ROUTED** class defined in Section 8. It does not cover non-local
current dressings, another charge, the physical stress tensor, a richer OS
carrier, an open/background quotient, another action $Q$, naturality, a
curved carrier, or gravity.

W1 is not a statement that the microscopic current is nonconserved. Block
121's off-shell divergence-commutator identity and its on-shell consequence
remain exact. W1 says that the current kernels do not become a conserved
operator after passage to this certified quotient.

W1 is not an OS no-go and is not a curved OS no-go. It is an obstruction for
the displayed local routed operator class on one certified quotient only.

### N1 — Alternative Route Enumeration

Routes are normalized by (object, mechanism, terminal). Microscopic
continuity, quotient values, observable descent, and downstream source or
carrier repairs are kept separate.

1. **PROVED — strongest structural obstruction — local routed U(1) class /
   routing changes are divergence-free curls while the divergence is pinned
   by $[E_z,Q]$ / no conserved observable on the certified quotient.** Every
   route representative has the same nonzero compressed site residual.
2. **PROVED — site-resolved Ward residual / exact quotient compression of
   $[E_z,Q]$ / nonzero at all 32 sites in every momentum sector.** This holds
   at both rational shear fixtures, with exact root-field nonzero tests.
3. **PROVED — current-kernel compatibility / left and right null descent plus
   $K_\Theta$ reflection-adjointness / failure for every nonzero displayed
   component.** Density descent succeeds at `0/32`; spatial-flux descent has
   only its four trivial zero components for odd $k$; adjointness succeeds at
   `0/32` for both components.
4. **PROVED — positive exact residue data / quadratic reduction and rank-one
   propagation / $\rho_k^{2m}$ times an affine root-field residue.** The
   geometric factor is structural; the exact affine residues and hashes are
   falsifiable content.
5. **PROVED — checker-discipline exposure / compare local and whole-cell
   tests and bind masks to definitions / the whole-cell recursion is labeled
   vacuous and flux zero-masks convention-dependent.** These catches are
   credited as discipline, not as failed theorem construction.
6. **UNTESTED-LIVE — physical and non-local repairs / pose the stress tensor,
   add a non-local current dressing, or enlarge and populate the carrier /
   test a genuine quotient observable and source coupling.** The
   stress-tensor source, non-local dressings, and open-carrier population are
   the immediate live routes.

Naturality and curved OS positivity remain downstream of row 6. W1 consumes
none of those routes.

### N2 — Wall-Independence Audit

W1 is distinct from Block 121's wall, anchored at
`docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md:775-809`.

Block 121 studied **source population**. Its object was the closed-carrier
Gauss image; its mechanism was the mismatch between zero-sum periodic
solvability and a norm-valued total U(1) charge. That wall can be removed by
an open boundary, a boundary-flux sector, or a compensating background.

The present wall studies **observable descent**. Its object is the local
routed density/current family on the certified half-space quotient; its
mechanism is the nonzero compressed site commutator plus null-descent and
reflection-adjointness failure. It is already visible before any periodic
Gauss equation is posed. Opening the carrier removes Block 121's total-charge
zero mode but does not, by itself, repair (32).

There is an honest shared pin. Block 121 established
$\operatorname{div}j=\bar\phi[E_z,Q]\psi$ and identified the resolved
commutator as the nonvacuous part of its local coupling. This block compresses
that same exact identity and finds the commutator nonzero at every site. The
shared $[E_z,Q]$ is the trace connection between the two questions, not a
reuse of the closed-carrier source-population proof. The norm-charge and
periodic-incidence mechanism of Block 121 does no work in W1.

Conversely, quotient-observable failure does not imply the closed-carrier
zero-mode wall. A current might descend on another quotient and still fail a
periodic Gauss compatibility condition, or an open source sector might be
populated while its naive local current still fails descent. Neither wall
implies the other.

### N3 — Hidden-Wall And Phrase Scan

The required H-gate scope-certificate phrase scan is classified explicitly.
Every hit in the left column is lowercase as required.

| lowercase hit | classification |
|---|---|
| certified half-space os package | inherited rank-one package only |
| both rational shear fixtures | exactly $c=5/13$ and $c=3/5$ |
| no local routed u(1) current | only the local routed class of Section 8 |
| conserved observable | descent plus reflection-adjointness and Ward law |
| quotient | the certified rank-one OS quotient only |
| site-resolved ward recursion | the exact local test (21) |
| fails at every site | zero count `0/32` for each momentum and fixture |
| residual exactly | equality in the relevant quadratic root field |
| quotient compression | normalized $y_k$ matrix element (7) |
| commutator [e_z,q] | the inherited endpoint divergence in (2) |
| current kernels | the displayed $J$ and $S$ kernels only |
| os null space | $\ker K_{\Theta,k}$ in (24) |
| map the os null space out of itself | every nonzero component fails (25) |
| fail reflection-adjointness | exact failure of (28) at all sites |
| structural | forced by rank one or by routing-curl invariance |
| local routed class | finite endpoint paths on the fixed lift |
| routing changes | Block 121's allowed path improvements |
| discrete curl | equation (30) only |
| divergence identity | equation (31), unchanged by routing |
| compressed current values | normalized quotient scalars (7) |
| exact closed form | equation (15), not a floating approximation |
| rho^{2m} | ket-and-bra stable propagation factor |
| affine root-field residue | exact reduction $A+B\rho$ in (14) |
| geometric factor structural | rank-one propagation, no Ward credit |
| residues the falsifiable content | exact coordinates and hashes |
| whole-cell recursion | equation (23) after site resolution is erased |
| vacuous by construction | transfer covariance plus spatial uniformity |
| not claimed as a conservation law | explicit checker firewall |
| flux zero-masks | support complements in (17)--(18) |
| convention-dependent | tied to the cut, bit order, link, and route |
| exact conventions | definitions (5), (16), and (17) |
| stress-tensor source | physical gravity-source route remains live |
| non-local dressings | outside the local routed class |
| populated open-carrier quotient | untested-live source route |
| naturality | untested-live downstream classification |
| curved os positivity | explicit reconstruction firewall |
| not an os no-go | W1 is only a local-class observable obstruction |
| off-shell microscopic conservation | Block 121's identity remains exact |
| completed adm/history transporter | downstream construction firewall |
| joint gravity | explicitly not completed |
| gravity constraint quotient on a populated carrier | explicitly open |
| records | no Records claim |
| retention | independent-audit firewall |
| axiom amendment | explicitly not justified |
| obligation retirement | TOE accounting firewall |
| toe percentage movement | TOE accounting firewall |
| no axiom amendment is justified | constitutional firewall |
| zero obligation retirement | TOE accounting statement |
| no toe percentage moves | TOE accounting statement |
| retained-positive end-to-end theory count remains zero | audit accounting |
| actual adm/history transporter remains | standard partial-close statement |
| gravity constraint quotient remains unexecuted | populated-carrier firewall |
| n1 n2 n3 n4 n5 n6 n7 n8 | every discipline gate is present |
| w1 | the wall set has exactly one member |
| per_element per_site per_mode per_block lattice_wide | five N5 keys |

No phrase upgrades a local U(1) proxy into a stress-tensor source, extends W1
to a non-local dressing or another carrier, converts an automatic scalar
recursion into a conservation law, claims a populated quotient, asserts
naturality or curved OS positivity, completes the ADM/history transporter,
authorizes joint gravity, changes audit status, or moves TOE accounting.

### N4 — Residual Matching

The supplied historical Block 105 result line, carried by Block 121, is:

> Block 105 §12 item 4 moves on exact source conservation and constraint
> preservation, but not on propagating $d=2$ gravity or gravity-transfer
> selection.

| source anchor | exact inherited residual | current match |
|---|---|---|
| [Block 121 next gate](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md), `docs/ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md:16` | “Prove or refute the Ward/transfer-covariance of the current bilinears on the OS quotient, then the populated sourced quotient on an open or background carrier, and the naturality classification.” | answered negatively with structure for the local routed class: every site residual is the nonzero quotient compression of $[E_z,Q]$, and descent plus adjointness fail; open-carrier population and naturality remain |
| [Block 119 completion](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | a certified four-sector rank-one positive half-space quotient with contractive transfer | the quotient it built carries exact scalar current residues but no local routed U(1) conserved observable; non-local operators and richer carriers were not tested |
| Block 105 §12 item 4 | exact source conservation and constraint preservation, without propagating gravity or gravity-transfer selection | the local U(1) coupling chapter closes honestly: microscopic continuity survives, but its local routed proxy does not descend to the certified quotient; the physical stress-tensor chapter remains live |

This is a partial closure of Block 121's next gate, not a rewrite of its
positive microscopic theorem. “Answered negatively with structure” means
equations (21), (25), (28), and (31) on the displayed package. It does not
answer the non-local, stress-tensor, populated-carrier, naturality, or curved
OS questions.

### N5 — Rhetoric And Granularity Audit

The strongest permitted sentence is: “On the certified half-space OS package
at both rational shear fixtures, no current in the local routed U(1) class
descends to a conserved quotient observable, because every site retains the
exact nonzero quotient compression of $[E_z,Q]$, every nonzero current
component fails OS-null descent, and both current components fail reflection-
adjointness, while routing changes leave the divergence unchanged.”

Forbidden upgrades include “no conserved observable exists at all,” “the
constraint quotient is dead,” and “the whole-cell recursion is a conservation
law.” The first erases the explicit restriction to the local routed U(1)
class. The second erases the live stress-tensor, non-local, open-carrier, and
richer-carrier routes. The third assigns conservation content to two
automatic zeros that discarded the site-resolved residual.

Also forbidden are “the microscopic U(1) current is not conserved,” “the
flux zero is invariant,” “rank-one transfer covariance proves a Ward law,”
“the stress tensor has the same obstruction,” “open boundaries cannot help,”
“naturality is classified,” “curved OS positivity fails,” “gravity is
coupled,” “an axiom amendment is required,” and “audit retention follows.”
None is established by this calculation.

The runner specification's five resolution lines are reproduced verbatim:

```text
N5: per_element: exact compression, projector-lemma, residue, dual-convention flux, residual-identity, descent, and adjointness certificates are checked
per_site: one Grassmann mode per fine site on the antiperiodic reflection torus
per_mode: every momentum's compressed current is rho^(2m) times an exact affine residue while the site-resolved ward recursion fails at every site with residual the compressed commutator
per_block: no local routed u(1) current descends to a conserved observable on the certified quotient — the obstruction is structural in the routing class and the whole-cell recursion is contentless
lattice_wide: checked and not executed — the stress-tensor source, non-local current dressings, the populated open/background-carrier quotient, the naturality classification, curved OS positivity, the actual ADM/history transporter completion, joint gravity, the gravity constraint quotient on a populated carrier, Records, audit retention, and TOE closure remain open
```

### N6 — Partial-Closure Path Scan

No registered primitive is needed. The current decision closes the displayed
local routed U(1) observable route while preserving repairs that change the
operator class, source, or carrier.

| route | present status | remaining terminal |
|---|---|---|
| rank-one compression | exact projector identity | none for the displayed package |
| stable propagation | exact $\rho_k^{2m}$ factor | none for quotient scalar geometry |
| density support | nonzero at all 32 sites per momentum | none for the displayed convention |
| spatial-flux support | exact masks (18) | no invariant claim across conventions |
| affine residues | exact root-field reductions and hashes | none for the displayed kernels |
| whole-cell recursion | exact but vacuous | no conservation credit |
| ordinary site Ward residual | nonzero at every site | none for W1's local test |
| microscopic-$\rho^2$ residual | nonzero at every site | none for the displayed recursion |
| density null descent | `0/32` at every momentum | none for displayed nonzero densities |
| spatial-flux null descent | only four trivial zeros for odd $k$ | no nonzero descending component |
| reflection-adjointness | `0/32` for $J$ and $S$ | none for displayed kernels |
| alternate local routing | divergence differs by zero | cannot repair compressed commutator |
| local routed U(1) observable | structurally obstructed | none inside W1's class |
| non-local current dressing | untested-live | cancel residual and prove descent/adjointness |
| modified charge or $Q$ | untested-live | eliminate compressed commutator, then recheck |
| stress-tensor source | not executed | derive physical source and its Ward/descent laws |
| populated open/background quotient | not executed | add boundary flux or background and exhibit a state |
| richer OS carrier | untested-live | repeat the observable test above rank one |
| naturality classification | untested-live | classify the completion and dressed source |
| curved OS route | not executed | establish positivity on the honest curved package |
| gravity route | not executed | populate the source sector and form the quotient |

The scan finds no axiom-amendment route. The Ward/transfer-covariance part of
Block 121's handoff is answered only for the local routed U(1) family. The
stress tensor, non-local dressings, carrier population, naturality, curved OS
positivity, the completed transporter, and joint gravity remain open.

### N7 — Steelman

**Hostile steelman: the U(1) current was always only a proxy.** Gravity is
sourced by the stress tensor. A wall for local particle-number current need
not constrain the physical coupling, so why call this an obstruction for the
constraint-quotient program?

Agreed. Block 121 used the U(1) charge-density/current pair as an exactly
tractable proxy for source continuity and constraint preservation. The
physical source is the stress tensor. W1 closes the proxy's local routed
observable route and no more. The stress tensor can have different kernels,
different improvement freedom, and different quotient descent properties.
It is the first named next construction. This wall may therefore fail to bind
the physical coupling, and the note says so explicitly.

**Hostile steelman: the quotient is tiny.** The certified OS quotient has
rank one per momentum. Rank-one compression makes whole-cell covariance
automatic and may discard exactly the degrees of freedom needed for a local
current operator. A richer carrier might admit conserved observables.

Agreed. The projector identity (8) exposes, rather than hides, that
limitation. W1 applies to the rank-one package inherited from Block 119. It
does not prove that a higher-rank OS quotient, an open/background carrier, or
a boundary-extended source space has the same descent failure. Those carriers
remain open and must be checked without transporting the masks or the no-go.

These steelmen preserve narrow W1 while preventing two framework-wide
upgrades: the U(1) proxy is not sold as the physical source, and a rank-one
carrier obstruction is not sold as a theorem about every quotient.

### N8 — Cross-Cycle Echo

The immediate campaign chain narrowed the carrier before asking the present
observable question; the discipline held.

| campaign block | narrowing that leads to W1 and the live routes |
|---|---|
| [Block 119](ADMISSIBILITY_DIRAC_KAHLER_REFLECTION_INTERTWINER_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-16.md) | supplied the certified rank-one positive half-space quotient and contractive scalar transfer |
| Block 120 | showed that the displayed half-space completion does not transfer literally to the antiperiodic torus |
| [Block 121](ADMISSIBILITY_DIRAC_KAHLER_CONSTRAINT_QUOTIENT_COUPLING_BOUNDED_THEOREM_NOTE_2026-08-16.md) | proved microscopic routed-current continuity and the Gauss intertwiner, then found the closed-carrier source-population wall |
| Block 122 | compresses the resolved currents, preserves their exact residue data, and closes only their local routed quotient-observable route |

The present result stops at the first exact local-class obstruction. It does
not reuse Block 120's wrap defect, does not reuse Block 121's total-charge
zero-mode proof, and does not infer the stress-tensor answer from the U(1)
proxy.

**No-Go Discipline verdict:** **PASS** only for narrow W1: on the certified
half-space OS package at both rational shear fixtures, no local routed U(1)
current yields a conserved observable because the nonzero compressed
$[E_z,Q]$ residual is invariant under routing curls and the kernels fail both
null descent and reflection-adjointness. The exact affine residue data are
**POSITIVE** bounded-theorem content. The whole-cell recursion is
**VACUOUS**, and its exactness earns no conservation credit. **FAIL** for “no
conserved observable exists at all,” “the constraint quotient is dead,” a
stress-tensor obstruction, a non-local obstruction, a richer-carrier
obstruction, populated open-carrier failure, naturality, curved OS
positivity, a completed ADM/history transporter, joint gravity, axiom
necessity, audit retention, or TOE movement.

## 10. Axiom And TOE Disposition

No axiom amendment is justified. The rank-one projector identity, stable
root-field reduction, support masks, sitewise residuals, null-descent tests,
reflection-adjointness tests, and routing-curl classification are finite
consequences of the displayed carrier, fixtures, action, currents, and
certified quotient. No new primitive is assumed.

This is bounded route closure, not an audit-grade assignment. It retires no
end-to-end obligation. TOE accounting remains:

- zero obligation retirement;
- no TOE percentage moves; and
- retained-positive end-to-end theory count remains zero.

## 11. Next Decision

The shortest high-value sequence is:

1. pose the stress-tensor source on the open/background carrier and test its
   continuity, null descent, reflection-adjointness, and source population;
2. construct non-local current dressings and test whether they cancel the
   compressed commutator without sacrificing OS compatibility; and
3. classify naturality and execute curved-carrier OS positivity on whichever
   honest source package survives.

The actual ADM/history transporter remains unexecuted beyond the displayed
half-space positive package, its rank-one scalar transfer, the microscopic
routed-current identity, and the local quotient-observable obstruction.

Reflection positivity on the curved carrier remains unexecuted.

The gravity constraint quotient remains unexecuted on a populated carrier.
