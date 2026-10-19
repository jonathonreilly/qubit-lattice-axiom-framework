# A refined resource certificate for the finite seeded router

Claim type: bounded_theorem. Conditional mathematical result with distinct analytical component and combined-family checks, followed by source-exposed ROOT integration. No retained audit or native realization is asserted.

For every \(0<\epsilon\le1\) and supplied incident-load cap \(\Lambda>0\), the explicit family below has complete-output isometry error less than \(179\epsilon/256<\epsilon\) throughout a relative-width \(1/6\) observation interval. Its sufficient qubit count and dimensionless duration scale as \(\Theta(\epsilon^{-4})\), while its physical duration scales as \(\Theta(\Lambda^{-1}\epsilon^{-14})\). These are bounds for a particular exact supplied family, not optimal exponents, lower bounds or practical performance claims.

## Fixed device, input and output contract

Use the positive finite router defined by the [parent theorem](COMMON_PRODUCT_FINITE_SEED_ROUTER_BOUNDED_THEOREM_NOTE_2026-10-18.md), with its six-qubit microscopic program cell, two finite rays \(n=0,\ldots,M\), and compensated outer blocks
\[
B_r=Q_\gamma((r,M-1),(r,M))
 +(j-\gamma)n_{r,M-1}+(2j-\gamma)n_{r,M},
\]
where
\[
Q_c(x,y)=c(n_x+n_y-a_x^\dagger a_y-a_y^\dagger a_x),\quad
j=b^2/D_0,\quad a_0=2j,\quad D_1>D_0>2b.
\]
All remaining ray bonds have weight \(j\). The full positive blocks, including their double-occupation diagonals, are unchanged. \(B_r\) has norm \(3j\); with its inward bond, both outer one-head diagonals are \(2j\). This is the compensated source, not a graph obtained by deleting full Laplacian edges.

The actual initial isometry \(E_{\rm seed}\) places one encoded path head at emitter \(M\), prepares every other head vacant, and encodes legal program \(p\) as \(|ppp\rangle\). Arbitrary encoded coherence and passive-reference entanglement are allowed. Basis program/path seeds are occupation products; arbitrary superpositions are supplied logical inputs.

The complete output comparator is
\[
e^{-i2bt}J_{\rm out}\bigl(\beta_F(t)\otimes C\xi\bigr),\qquad
C=|0\rangle\langle0|\otimes X+|1\rangle\langle1|\otimes I.
\]
It retains unchanged encoded programs and a common normalized packet on \(0\le n\le\ell=M-1\), with both emitters and mediator vacant. Every actual output coordinate remains in the error. The packet is time dependent; the common physical scalar is not discarded.

## Exact family and same-metric comparison

Set
\[
\begin{gathered}
\rho=\epsilon/256,\qquad
u_0=10^{12}\rho^{-2}\epsilon^{-2},\qquad
\ell=\lceil100u_0\rceil,\quad M=\ell+1,\quad s=7\ell/8,\\
\eta^2=\frac{\epsilon}{256(1+s)},\quad \eta>0,\qquad
\zeta=\frac{\epsilon}{64(1+s)}=4\eta^2,\\
D_1=\Lambda/2,\quad D_0=\zeta D_1,\quad b=\eta D_0,\quad
j=\frac{\Lambda\eta^2\zeta}{2},\quad\gamma=\rho j,\\
t_0=u_0/j,\qquad t_- =3\ell/(4j),\qquad t_+=7\ell/(8j).
\end{gathered}
\]
These are exact prescriptions, including the ceiling and coefficient correlations. In particular
\[
\begin{gathered}
D_0=\frac{\Lambda\epsilon}{128(1+s)},\qquad
b=\frac{\Lambda\epsilon^{3/2}}{2048(1+s)^{3/2}},\\
j=\frac{\Lambda\epsilon^2}{32768(1+s)^2},\qquad
\gamma=\frac{\Lambda\epsilon^3}{8388608(1+s)^2},\qquad
t_+=\frac{32768s(1+s)^2}{\Lambda\epsilon^2}.
\end{gathered}
\]
The relative window width is exactly \((t_+-t_-)/t_-=1/6\). No Hamiltonian switch occurs at \(t_0,t_-\), or \(t_+\).

At fixed \(\Lambda\), the comparison with the separately checked baseline uses the same complete-output isometry accuracy argument, relative observation width, block architecture, input premises and incident-load convention:

| Quantity | Refined sufficient family | Checked baseline |
|---|---|---|
| Qubits and positive blocks | \(\Theta(\epsilon^{-4})\) | \(\Theta(\epsilon^{-8})\) |
| Dimensionless observation times \(jt_\pm\) | \(\Theta(\epsilon^{-4})\) | \(\Theta(\epsilon^{-8})\) |
| \(D_0\) | \(\Theta(\Lambda\epsilon^5)\) | \(\Theta(\Lambda\epsilon^9)\) |
| \(b\) | \(\Theta(\Lambda\epsilon^{15/2})\) | \(\Theta(\Lambda\epsilon^{18})\) |
| \(j\) | \(\Theta(\Lambda\epsilon^{10})\) | \(\Theta(\Lambda\epsilon^{27})\) |
| \(\gamma\) | \(\Theta(\Lambda\epsilon^{11})\) | \(\Theta(\Lambda\epsilon^{28})\) |
| Physical observation times | \(\Theta(\Lambda^{-1}\epsilon^{-14})\) | \(\Theta(\Lambda^{-1}\epsilon^{-35})\) |

The very large fixed constants remain in the exact prescriptions. This compares two sufficient parameter families, not measured speed, actual error or a fixed-device performance improvement.

## Integrating the exact source resonance

The exact outgoing source amplitude has the rational form
\[
F(k)=-i\sqrt{2/\pi}\,\rho\,
       \frac{e^{ik}}{A\cot k-i\delta},\qquad
A=2-\rho^2,\quad\delta=\rho^2,
\]
and the incoming amplitude is \(\overline F\). This is an equality of complex amplitudes, including phase, obtained by cancelling the conjugate linear factor in the source's quadratic spectral denominator.

Fix the real cutoff once: for \(x=|k-\pi/2|\), it is one through \(x=\pi/24\), equals \(Q((x-\pi/24)/(\pi/12))\) through \(x=\pi/8\), and is zero thereafter, with
\[
Q(z)=1-10z^3+15z^4-6z^5.
\]
It is \(C_c^2\), with \(\|\chi'\|_\infty<7.5\), \(\|\chi''\|_\infty<240\), and support strictly inside the conservative band \(|k-\pi/2|<\pi/6\). Thus \(v_-/j=\sqrt3\), \(v_+/j=2\). Let
\[
p=\|\chi F\|_2^2,\quad g=\chi F/\sqrt p,\quad G_r=\|g^{(r)}\|_1.
\]
The checked spectral tail gives \(P\le11\rho^2\) and \(p\ge1-P>1/2\). Positive normalization preserves the exact source phase.

The improvement comes from integrating the resonance instead of bounding every denominator by its minimum. With \(x=\cot k\), \(h=(Ax-i\delta)^{-1}\), \(L=\tan(\pi/6)\), \(S=\sec^2(\pi/6)\),
\[
\begin{aligned}
\|h\|_1&\le(2/A)\operatorname{asinh}(AL/\delta),\\
\|h'\|_1&=(2/\delta)\arctan(AL/\delta)\le\pi/\delta,\\
\|h''\|_1&\le(2/A)\log(1+(AL/\delta)^2)+4AS/\delta^2.
\end{aligned}
\]
These norms are over the conservative central interval. The first derivative's factor \(1+x^2\) cancels the Jacobian \(dk=|dx|/(1+x^2)\). Both terms
\[
h''=\frac{-2Ax(1+x^2)}{(Ax-i\delta)^2}
       +\frac{2A^2(1+x^2)^2}{(Ax-i\delta)^3}
\]
are included. Cutoff and \(e^{ik}\) product rules, followed by division by the same \(\sqrt p\), give the safe constants
\[
G_0<2,\qquad G_1\le100\rho^{-1},\qquad G_2\le2000\rho^{-3}.
\]
The raw incoming launch coefficient is exactly
\[
B_-=\sqrt p\,[G_1+(2/\sqrt3)G_0]\le200\rho^{-1}.
\]
The derivative source supplies explicit general-cutoff constants and all integrals. No cutoff narrowing or unproved \(\rho\)-uniform derivative estimate is used.

## An exact second-order rectangular residual

After subtracting only the common scalar \(2b\), split one legal program sector into the logical one-head space and mediator:
\[
h=\begin{pmatrix}A_p&B\\B^*&D_p\end{pmatrix},\quad
B=-b(|u\rangle+|v\rangle),\quad
A_p=K+a_p(|u\rangle\langle u|+|v\rangle\langle v|).
\]
Here \(a_0=2j,a_1=0\), and \(\|K\|\le4j\) for the actual finite compensated rays. Set
\[
\bar h=A_p-BB^*/D_p,\quad Jx=(x,0),\qquad
Tx=\begin{pmatrix}x\\-B^*x/D_p-B^*\bar h x/D_p^2\end{pmatrix}.
\]
The map \(T\) is not an isometry and is never prepared. Direct multiplication, with the orders retained, gives the exact identity
\[
hT-T\bar h=
\begin{pmatrix}-BB^*\bar h/D_p^2\\B^*\bar h^2/D_p^2\end{pmatrix}.
\]
The enabled \(\bar h\) equals the finite ideal router; the disabled difference from its target has norm \(2j\zeta\). Both sectors have \(\|\bar h\|\le4j\): in the disabled sector the modified central row has diagonal \(j(1-\zeta)\) and off-diagonal magnitudes \(j,j\zeta\), whose sum with that diagonal is \(2j\).

Using \(\eta=b/D_0\),
\[
\|T-J\|\le\sqrt2\eta(1+4\eta^2),\qquad
\|hT-T\bar h\|\le j(8\eta^2+16\sqrt2\eta^3).
\]
Rectangular Duhamel bounds the difference between the two evolutions of \(T\) directly by time times the residual; no \(\|T\|\) factor or isometry hypothesis is needed. Replacing \(T\) by \(J\) at both ends and comparing \(\bar h\) to the ideal finite router gives
\[
e_{\rm cell}^{(2)}(t)\le\min\{2,
2\sqrt2\eta(1+4\eta^2)+jt(8\eta^2+16\sqrt2\eta^3+2\zeta)\}.
\]
The cap two is applied only after returning to literal isometries. The bound includes actual mediator output, coherent programs and passive references, and charges the **entire elapsed time from the emitter seed**. For \(\eta\le1/8\), its sufficient ceiling is \(4\eta+11jt\eta^2+2jt\zeta\).

## Complete budget, normalization and load

The fixed window has late gap greater than \(\ell/4\), outgoing boundary gap \(\ell/4\), and early gap at least \(\ell/2\). The source's mixed-endpoint normalization satisfies \(d_L<1/2\), \(d_O<1\); launch has \(\delta_{\rm launch}<1\). The common packet is therefore defined throughout the interval by positive normalization of
\[
B_n(t)=\frac1{\sqrt{2\pi}}\int_0^\pi
e^{i[(n+\ell+1)k-tE(k)]}g(k)\,dk,
\quad E(k)=2j(1-\cos k),\quad 0\le n\le\ell.
\]
This retains source translation, scattering and dispersion phases and excludes both emitter sites.

All nine nonnegative ideal contributions are explicitly paid:

| Contribution | Sufficient ceiling |
|---|---|
| Early factorial comparison | \(3/(100u_0)\) |
| Source residual \(2R_0\) | \(2\epsilon^2/10^{12}\) |
| Incoming launch term \(2L_0\) | \(400\epsilon/10^6\) |
| Spectral tails \(4\sqrt P\) | \(4\sqrt{11}\epsilon/256\) |
| Right early tail \(2d_{\rm right}\) | \(208\epsilon/10^6\) |
| Early packet matching | \(300\epsilon/10^7\) |
| Integrated outer-boundary error | \((8100\cdot256/10^{12})\epsilon\) |
| Late incoming normalization \(2d_L\) | \(460\epsilon/10^7\) |
| Finite output normalization \(2d_O\) | \(920\epsilon/10^7\) |

Each is below \(\epsilon/16\), giving an ideal sum below \(9\epsilon/16\). The factorial remainder starts at degree \(\ell+2\); the boundary estimate retains the factor \(\rho^{-3}/u_0=256\epsilon/10^{12}\). These terms cannot be dropped when substituting improved derivatives.

The cell endpoint cost also needs its own check. Since \(s\ge87.5u_0\), one has \(1+s>16/\epsilon\), and hence
\[
4\eta<\epsilon/16,\qquad
11s\eta^2<11\epsilon/256,\qquad
2s\zeta<\epsilon/32.
\]
The physical-cell sum is below \(35\epsilon/256\). Combining the two parts proves the uniform statement
\[
\boxed{\sup_{t_-\le t\le t_+}
\left\|e^{-itH_{\rm phys}}E_{\rm seed}
-e^{-i2bt}J_{\rm out}(\beta_F(t)\otimes C)\right\|
<179\epsilon/256<\epsilon.}
\]
The unhalved channel discrepancy is below \(2\epsilon\); using the accuracy argument \(\epsilon/2\) gives channel accuracy \(\epsilon\) without changing the exponents. No actual output is projected, traced away or normalized.

There are \(8+2\ell\) qubits and \(9+2\ell\) positive blocks under the parent combined-block convention. The ratios satisfy \(\eta\le1/16\), \(\zeta\le1/64\). The incident sums \(D_1+2b\), \(3b+4j\), program loads \(2j,D_1-2b\), lead interior \(4j\), emitter-adjacent \(5j\), and emitter \(3j\) are all strictly below \(\Lambda\).

The smallest displayed positive scalar coefficient is \(\gamma\): \(\gamma<j\), \(j-\gamma>\gamma\), \(b/j=1/\eta>1\), and \((D_0-2b)/j=(1-2\eta)/\eta^2>1\), with the other coefficients larger. This is an exact coefficient magnitude, **not an allowed fabrication error, precision tolerance, minimal eigenvalue or coefficient-production cost**.

## Scope and checked evidence

The mathematical change is a tighter sufficient certificate for the same positive architecture and output contract. Exact blocks and coefficient correlations, occupation basis, roles, absent couplings, vacant-head preparation and encoded program/input coherence remain supplied. This does not derive native interactions, implement the old literal processor, create stationary output, capture or reset the head, or provide permanent halt. Finite returns remain possible after the certified window.

The [portable source manifest](../outputs/common_product_refined_resources_2026_10_18/SOURCES.json) contains the complete baseline, derivative, second-order and combined-family arguments and their distinct checks. It pins the unchanged parent packet, whose full composition, window, microscopic cell and scalar-reference qualifications remain premises at their stated scopes. The combined review reconstructs every simultaneous parameter choice, all nine ideal allocations, the literal endpoint cost and the physical cap. No microscopic-scattering proposal is imported.

ROOT suggested the refinements and combined choices and authored the second-order comparison map. The draft author also authored the derivative and combined-family sources. The distinct reviewers had access to the proposed arguments and shared components; these same-model checks are not blind or model-diverse replication. ROOT fully read the source/check arguments and the final synthesis. The integration record is not an additional independent science check or retained audit.

No scientific executable, symbolic solver, dynamics simulation, parameter sweep or evaluated numerical operating point supports the certificate. Source hashes, links and citation topology are mechanical publication checks. No physical axioms or editable prompts were changed.

## Portable finite controls

Primary runner: `scripts/common_product_program_controls_2026_10_18.py` (timeout: 120 seconds). Its literal declared input closure includes all ten canonical notes and their live proof dependencies. It checks finite physical matrices, complete scattering and explicit sufficient budgets; finite controls corroborate these supplied conditional theorems and do not establish native realization or replace their analytical proofs. Historical statements above about what was executed describe original authorship; this added primary has a separate owner capture.
