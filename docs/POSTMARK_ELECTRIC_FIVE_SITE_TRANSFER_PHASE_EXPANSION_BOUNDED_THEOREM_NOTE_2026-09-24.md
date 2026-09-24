---
claim_id: postmark_electric_five_site_transfer_phase_expansion_2026_09_24
claim_type: bounded_theorem
claim_scope: >-
  For the explicitly tabulated scalar Jacobi family, the determinant-one
  five-site transfer trace and locally oriented eigenphase have expansions
  through S^-2 with compact-uniform O(S^-3) remainders on regular bulk arcs.
  Its physical model identification and any global quantization or readout
  consequence remain conditional or open.
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: postmark_electric_core_and_boundary_bounded_theorem_note_2026_09_24
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
reachability_to_target: supports
conditional_surface_status: "conditional on identifying the scalar coefficient family defined here with the supplied one-vacancy model; that physical identification is not proved in this note"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The local transfer expansion is proved for the displayed scalar Jacobi family; its interpretation as the supplied finite-spin physics and its relation to the actual prepared readout remain open."
audit_required_before_effective_retained: true
bare_retained_allowed: false
artifact_role: theorem
next_trace_action: "Establish global phase-accurate propagation and prepared-overlap transport through the Bragg, central, turning, and endpoint layers, then control the all-alias two-index readout sum."
runner: scripts/postmark_electric_five_site_transfer_phase_expansion_2026_09_24.py
---


# Five-site transfer phase through second order for a scalar Jacobi family

**Date:** 2026-09-24
**Type:** bounded theorem
**Status:** proposed_retained

## Exact target

**Exact claim.** For the scalar Jacobi coefficient family defined below, on
every compact \(K_u\subset(-1,1)\) and compact \(K_k\subset\mathbb R\) with
\(|\sin(5k)|\ge\kappa>0\), the determinant-one five-site transfer trace and
its locally oriented eigenphase admit expansions through order \(S^{-2}\),
with remainders uniform in \(u=h/S\) and bounded by \(O(S^{-3})\).

Take integer \(S\), an interior cell \(n=5h+s\), \(s=0,\ldots,4\), and put

\[
u=h/S,\qquad w=1-u^2,\qquad z=\cos k,\qquad
\lambda=2w(1-z),\qquad \epsilon=S^{-1}.
\]

The domain excludes \(u\to\pm1\) and the repeated-root points
\(\sin(5k)=0\); no uniform estimate as either boundary is approached is
claimed. The trace expansion is

\[
\operatorname{tr}M_S(h,\lambda)
=\tau_0(u,k)+\epsilon\tau_1(u,k)
+\epsilon^2\tau_2(u,k)+O_{K_u,K_k}(\epsilon^3),
\]

and the local eigenphase \(\Phi_S\to5k\) has the corresponding expansion
through \(S^{-2}\). All statements below concern a single five-site cell; the
analytic remainder constant may depend on \(K_u,K_k,\kappa\).

## Proof dependency graph

| Obligation | Status here | Evidence or dependency |
|---|---|---|
| Five-residue scalar Jacobi coefficient family | Defined here | Exact integer arrays and rational functions are listed below; no physical identification is inferred from this definition. |
| Transfer recurrence, determinant, and multiplication order | Proved here | Direct substitution into the second-order scalar recurrence. |
| Coefficient and square-root expansions through \(S^{-2}\) | Proved here | Exact rational identity and uniform Taylor expansion with \(w\) bounded below. |
| Five-site trace coefficients | Proved here | Ordered matrix-product recurrence and exact symbolic reduction, checked by the paired runner. |
| Local phase coefficients | Proved here | Expansion of \(2\cos\Phi_S\) and inversion on charts with \(|\sin(5k)|\ge\kappa\). |
| Uniform \(O(S^{-3})\) remainder | Proved here | Compact analyticity for the five factors and a uniform implicit-function argument. |
| Global quantization, prepared overlaps, and the actual readout | Open | Requires transfer and spectral-weight control across nonregular layers and all aliases. |

## Exact five-site coefficients and transfer

Use the following exact residue arrays as the definition of this scalar
coefficient family:

\[
\ell=(0,1,0,1,1),\qquad
\rho=(0,0,0,1,0),\qquad
\pi=(-1,0,0,0,1),\qquad f(m)=m(m+1).
\]

For \(a\in\{-1,0,1\}\), define

\[
r_a=1-\frac{f(h+a)}{S(S+1)}.
\]

For every compact interior parameter set and all sufficiently large \(S\),
these link factors are positive, so the displayed square roots and transfers
are defined.

At site \(5h+s\), the diagonal and the outgoing staggered off-diagonal of
\(N_S\) are exactly

\[
d_s=r_{\ell_s}+r_{\pi_s},\qquad
a_s=-\sqrt{r_{\ell_s}r_{\rho_s}}.
\]

Thus solutions of the frozen-cell recurrence
\(a_n y_{n+1}+d_ny_n+a_{n-1}y_{n-1}=\lambda y_n\) obey

\[
\begin{pmatrix}y_{n+1}\\a_ny_n\end{pmatrix}
=T_{n,S}(\lambda)
\begin{pmatrix}y_n\\a_{n-1}y_{n-1}\end{pmatrix},\qquad
T_{n,S}(\lambda)=
\begin{pmatrix}(\lambda-d_n)/a_n&-1/a_n\\a_n&0\end{pmatrix}.
\]

Whenever \(a_n\ne0\), direct evaluation gives \(\det T_{n,S}=1\). The cell
product is ordered as

\[
M_S(h,\lambda)=T_{5h+4,S}(\lambda)\cdots T_{5h,S}(\lambda).
\]

At \(\epsilon=0\), \(a_s=-w\) and \(d_s=2w\). With
\(D(u)=\operatorname{diag}(1,w)\), the similar one-site transfer is
\(D^{-1}T_sD=M_0=\bigl(\begin{smallmatrix}2z&1\\-1&0\end{smallmatrix}\bigr)\),
so its frozen five-site trace is \(2\cos(5k)\). The same matrix \(D(u)\) is
used for the five sites in a given frozen cell; it is not held fixed when the
cell index \(h\) changes.

## Coefficient expansion

The exact scalar identity, expressed in \(u=h/S\), is

\[
r_a=1-\frac{(u+a\epsilon)(u+(a+1)\epsilon)}{1+\epsilon}
=w+\alpha_a\epsilon+\beta_a\epsilon^2+O_{K_u}(\epsilon^3),
\]

where

\[
\alpha_a=u^2-u(2a+1),\qquad
\beta_a=-a(a+1)+u(2a+1)-u^2.
\]

For each residue \(s\), let

\[
\begin{aligned}
b_s&=\frac{\alpha_{\ell_s}+\alpha_{\rho_s}}2,\\
c_s&=\frac{\beta_{\ell_s}+\beta_{\rho_s}}2
-\frac{(\alpha_{\ell_s}-\alpha_{\rho_s})^2}{8w},\\
d_{1s}&=\alpha_{\ell_s}+\alpha_{\pi_s},\\
d_{2s}&=\beta_{\ell_s}+\beta_{\pi_s}.
\end{aligned}
\]

Positivity of \(w\) on \(K_u\) and the square-root Taylor formula give
\[
a_s=-(w+b_s\epsilon+c_s\epsilon^2)+O_{K_u}(\epsilon^3),\qquad
d_s=2w+d_{1s}\epsilon+d_{2s}\epsilon^2+O_{K_u}(\epsilon^3).
\]

Writing \(D^{-1}T_{5h+s,S}D=M_0+\epsilon M_{1s}+\epsilon^2M_{2s}+O(\epsilon^3)\),
direct division yields

\[
M_{1s}=\begin{pmatrix}
 d_{1s}/w-2zb_s/w&-b_s/w\\
-b_s/w&0
\end{pmatrix},
\]

\[
M_{2s}=\begin{pmatrix}
 d_{2s}/w-d_{1s}b_s/w^2-2zc_s/w+2zb_s^2/w^2&-c_s/w+b_s^2/w^2\\
-c_s/w&0
\end{pmatrix}.
\]

The order-\(\epsilon^2\) product coefficient includes both one-site
second-order terms and all ordered pairs of first-order terms. Specifically,
if \(P_j^{(q)}\) denotes the order-\(\epsilon^q\) coefficient after the first
\(j\) factors have been applied, initialize
\(P_0^{(0)}=I, P_0^{(1)}=P_0^{(2)}=0\) and update

\[
P_{j+1}^{(0)}=M_0P_j^{(0)},\quad
P_{j+1}^{(1)}=M_0P_j^{(1)}+M_{1j}P_j^{(0)},\quad
P_{j+1}^{(2)}=M_0P_j^{(2)}+M_{1j}P_j^{(1)}+M_{2j}P_j^{(0)}.
\]

The runner checks the coefficient convolution in this ordered convention.

## Trace and local eigenphase

Define the polynomials

\[
T_5(z)=16z^5-20z^3+5z,\qquad
U_4(z)=16z^4-12z^2+1=\frac{\sin(5k)}{\sin k},
\]

and

\[
g_1(u,z)=\frac{u(5uz-5u-9z+8)}{w}.
\]

Multiplication of the five site matrices gives

\[
\tau_0=2T_5(z),\qquad \tau_1=-2U_4(z)g_1(u,z),\qquad
\tau_2=\frac{2P_5(u,z)}{w^2},
\]

with

\[
\begin{aligned}
P_5(u,z)={}&160u^4z^5-320u^4z^4+100u^4z^3+120u^4z^2-60u^4z\\
&-720u^3z^5+1232u^3z^4-188u^3z^3-516u^3z^2+183u^3z+9u^3\\
&+832u^2z^5-1168u^2z^4-84u^2z^3+556u^2z^2-102u^2z-25u^2\\
&-144uz^5+128uz^4+108uz^3-96uz^2-9uz+8u\\
&+64z^5-64z^4-48z^3+48z^2+4z-4.
\end{aligned}
\]

On the stated regular arc, \(\sin(5k)\ne0\), so the determinant-one cell
matrix is elliptic for sufficiently large \(S\), and its eigenphase has a
unique local lift \(\Phi_S\to5k\). Let

\[
g_2(u,z)=-\frac{\tau_2/2+T_5(z)g_1(u,z)^2/[2(1-z^2)]}{U_4(z)}.
\]

Expanding \(\operatorname{tr}M_S=2\cos\Phi_S\) then gives

\[
\Phi_S=5k+\frac{g_1(u,z)}{S\sin k}
+\frac{g_2(u,z)}{S^2\sin k}+O_{K_u,K_k}(S^{-3}).
\]

There are no denominators at zero on the specified domain: \(\sin k=0\)
would imply \(\sin(5k)=0\), and \(U_4=\sin(5k)/\sin k\) is bounded away
from zero there.

## Uniform remainder and regrouping

For \(u\in K_u\), \(w\ge w_0>0\). The exact coefficient functions extend
analytically to a common neighborhood of \(\epsilon=0\); their square-root
branches remain positive for sufficiently small \(\epsilon\). Their first
three derivatives are uniformly bounded on the compact parameter set.
Multiplying five factors preserves a uniform trace remainder
\(O_{K_u,K_k}(\epsilon^3)\). Since \(|\sin(5k)|\ge\kappa\), the derivative
of \(\cos\Phi\) at \(5k\) is bounded away from zero. The implicit-function
theorem applied on finitely many compact phase charts gives the displayed
uniform eigenphase remainder of the same order.

For three consecutive cells the exact, varying-coefficient identity is

\[
M_{15,S}(h,\lambda)
=M_S(h+2,\lambda)M_S(h+1,\lambda)M_S(h,\lambda).
\]

The three factors use their actual cell indices (and hence their actual
\(u\)-values, shifted by \(S^{-1}\). In general this product is not
\(M_S(h,\lambda)^3\). The runner checks the grouping identity on finite
spins with direct products of all fifteen actual site transfers.

## Physical and campaign scope

This is a local transfer-phase module for the supplied Jacobi coefficients.
It does not provide a global Bohr--Sommerfeld condition, an accumulated phase
error for the \(O(S)\) cells, a crossing or central connection matrix, a
turning-point match, prepared spectral-overlap transport, or a bound on the
two-index alias sum at time \(C/4\). It therefore does not prove a limit or
separated subsequences for the actual readout.

The theorem stops at the regular five-site expansion. The strongest
missing lemma for the fixed-time target is an alias-uniform \(o(1)\) estimate
for the exact prepared two-energy sum after global phase and overlap transport
through the Bragg, central, turning, and endpoint layers.

## Imports and open bridges

| Input | Role | Provenance | Open bridge |
|---|---|---|---|
| The integer residue arrays and rational link values displayed in this note | Complete mathematical definition of the scalar family | Defined explicitly above; no hidden coefficient file is read by the runner | None for the local scalar expansion |
| Identification of this scalar family with the one-vacancy physical model | Conditional model interpretation only | Campaign note `POSTMARK_ELECTRIC_FIVE_SITE_INTER_FIBER_PHASE_BOUNDED_THEOREM_NOTE_2026-09-24.md` supplies the signed-label reduction | This note does not re-derive that identification or connect the family to the prepared physical readout |

No axiom, approved primitive, empirical value, or fitted parameter enters the
scalar calculation. Standard Taylor expansion and the implicit-function
theorem are used only with the compactness and nondegeneracy bounds stated
above.

## Verification

The paired runner checks the exact rational expansion of each \(r_a\), the
square-root expansion by squaring its candidate series, determinant one,
all three trace coefficients against the displayed \(P_5\), and the phase
coefficient formulas. It also evaluates exact finite five-site products at
several interior cells and spins, tests the \(S^3\)-scaled trace and phase
remainders as diagnostics, and compares an exact fifteen-site product with
three consecutively shifted five-site products. These finite floating-point
checks corroborate the symbolic identities; the uniform \(O(S^{-3})\) bound
is supplied by the compact analytic remainder argument above.

```bash
python3 scripts/postmark_electric_five_site_transfer_phase_expansion_2026_09_24.py
```

The result JSON and canonical runner-cache record are stored under
`outputs/postmark_moving_index_2026_09_24/` and
`logs/runner-cache/`. No formal audit or independent review status is claimed.
