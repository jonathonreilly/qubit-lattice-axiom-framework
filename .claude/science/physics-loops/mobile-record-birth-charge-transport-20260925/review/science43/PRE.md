# PRE43: escape from the nearest-neighbor grouping union after one original birth

Blind independent reconstruction, 25 September 2026. Conditional mathematics of the supplied finite common rotor law. No author43 source, candidate42, charge-force41 packet, publication candidate, other active checker or campaign checkpoint was read. Historical exposure to the earlier charge/threshold work is disclosed; none of its scientific code or results is imported into this calculation.

## Result and distinctions

The projector \(P_{\rm nn}\) specified in the request is **not invariant**. The failure survives the freedom to reassign either positive B charge to the A defect. There are explicit Gauss-legal magnetic paths from each actual resolved first-mark output to a state whose unique negative A site has graph distance three from both positive B sites. The stipulated coherent edge output also escapes. This is already a Hamiltonian transport effect inside the first-postbirth number sector, in addition to the simpler fact that another birth leaves that number sector.

Let \(\Pi_2\) denote the **record-number** sector \(N=n+2\), not the vacancy-sector notation used in part of the parent Schur derivation. Set \(Q=\Pi_2-P_{\rm nn}\). For the normalized actual resolved or coherent output \(\psi\) defined below, evolve the complete original common GKLS law. Then, at fixed finite even cubic \(L\ge4\) and fixed positive \(K,\delta,\kappa\),
\[
p_\psi(t):=\operatorname{Tr}\bigl(Q\,e^{t\mathcal L}|\psi\rangle\langle\psi|\bigr)
 =\delta^2t^2\|QH_4\psi\|^2+O(t^3).                     \tag{1}
\]
The coefficient is strictly positive. Recycling is included in the full state; it contributes to higher number sectors and cannot return to \(\Pi_2\). Equation (1) is an unconditioned probability in that full evolution, not a renormalized no-event approximation.

An explicit error bound and positive time interval are proved in Section 5. The universal lower bounds on the coefficient, established by local witnesses rather than volume extrapolation, are
\[
\|QH_4\psi_+\|^2\ge\frac45,\qquad
\|QH_4\psi_-\|^2\ge\frac{16}{5},\qquad
\|QH_4\psi_{\rm coh}\|^2\ge2.                            \tag{2}
\]
They are deliberately weak. Finite primitive controls give much larger coefficients, with genuine small-period differences. No coefficient from one torus is promoted to every volume.

This result concerns the explicitly supplied zero-electric state immediately before a mark. It does not identify that state with the field at a randomly timed actual first event. It averages over no unknown event time, makes no microscopic derivative-limit interchange, and supplies no claim of long-time dissociation, particle nonexistence, absorption, or physical preparation/selection.

## 1. Exact parents and retained model

Only these three scientific parents are imported, all checked against the named git objects at 60c5f194d940a7bbaf1cdd545296e31d74a02f1a and their unchanged campaign-working bytes:

| Parent, standard 2026-09-24 bounded-theorem suffix | SHA256 |
|---|---|
| LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS | 7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a |
| LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT | c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b |
| FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES | 2ae8d264eaff3ab47ecf4ec41fa21178ff444546bcc2e36d885d092732e30516 |

Their complete relevant arguments were read. The first batched tool display truncated the source text, so all three were reread separately in full. The workflow and applicable instruction identities remain unchanged and are pinned in SOURCE_PINS.json. The supplied quantum space, unsigned tensor hard-core algebra, unit rotor shifts, Gauss law, Hamiltonian, jumps and probability interpretation remain conditional premises. No audit status is imported.

Take the cubic torus \((\mathbb Z/L\mathbb Z)^3\), equal even sides \(L\ge4\), with A the even sublattice, \(n=|A|=L^3/2\), and all A sites occupied in the effective P space. Choose each edge orientation from A to B; \({\bf e}_{xy}\) denotes \(+1\) on the edge \(x\in A\) to \(y\in B\). The physical constraint is
\[
\operatorname{div}E=q-\mathbf1_A.
\]
An outward hop of charge \(s=\pm1\) from A to B changes its field by \(-s{\bf e}_{xy}\); its return changes it by \(+s{\bf e}_{xy}\). Pair creation with sign \(\sigma\) makes charges \(\sigma,-\sigma\) at the A/B endpoints and changes the field by \(+\sigma{\bf e}_{xy}\).

The entire Hamiltonian and instrument remain
\[
h=KD+\delta H_4,\qquad
H_4=-2\sum_{\{x,y\}\subset A:\,N(x)\cap N(y)\ne\varnothing}
           (F_yF_xP)^*(F_yF_xP),
\]
\[
D(q,E)=\sum_{\substack{x\in A,\ y\sim x\\q_y=0}}
                  E_{xy}(E_{xy}-q_x),\qquad
L_{xy,\sigma}=\sqrt\kappa\,B_{xy,\sigma},
\quad B_{xy,\sigma}=Pj_{xy,\sigma}F_xP.                 \tag{3}
\]
The coherent alternative is the specified \(L_{xy}=\sqrt\kappa(B_{xy,+}+B_{xy,-})\), with no \(1/\sqrt2\) inserted. All charge-dependent empty-B gates in \(D\) and all magnetic matter outputs are retained. The integer-field basis is used throughout; no flat-angle field compression occurs. In particular zero electric flux has harmonic-angle Haar measure, not a point at zero angle.

In \(\Pi_2\) there are exactly two occupied B sites and one negative label. The given \(P_{\rm nn}\) includes every integer field compatible with a matter word having either its minus on B, or its minus on an A site adjacent to at least one of the two positive B records. It is a diagonal bounded projector in the physical basis. It strongly commutes with \(D\); it need not commute with magnetic motion or the loss operator.

## 2. Actual marked inputs and the complete loss term

Set
\[
a=(0,0,0),\quad b=(-1,0,0),
\]
with coordinates understood modulo \(L\). Let \(\Omega\) be the normalized all-A-plus/B-empty/zero-electric basis vector. The actual unnormalized mark vector
\[
\xi_\sigma=B_{ab,\sigma}\Omega
 =\sum_{c\in N(a)\setminus\{b\}}|q_{\sigma,c},E_{\sigma,c}\rangle
\]
has, for each of its five branches,
\[
q_a=\sigma,\quad q_b=-\sigma,\quad q_c=+1,\qquad
E_{\sigma,c}=\sigma{\bf e}_{ab}-{\bf e}_{ac}.           \tag{4}
\]
All other A charges are plus and all other B sites are empty. Equation (4) obeys Gauss exactly. Its branch states are mutually orthogonal, and the two signs are also orthogonal. Thus
\[
\|\xi_\sigma\|^2=5,\qquad
\|\xi_++\xi_-\|^2=10,
\]
\[
\psi_\sigma=\xi_\sigma/\sqrt5,\qquad
\psi_{\rm coh}=(\xi_++\xi_-)/\sqrt{10}.                \tag{5}
\]
The original selected intensities are \(5\kappa\) and \(10\kappa\). Conditional normalization of the output density in (5) does not renormalize the jump operator. All these inputs lie in \(P_{\rm nn}\). Every nonzero field edge in (4) ends at an occupied B site, so the actual gate in (3) gives \(D\xi_\sigma=0\).

Write \(\Gamma=\sum_\mu L_\mu^*L_\mu=\kappa\Gamma_0\). For the same edge the two sign ranges have orthogonal endpoint colors:
\[
B_{xy,+}^*B_{xy,-}=0=B_{xy,-}^*B_{xy,+}.
\]
Consequently the resolved and stipulated coherent instruments have exactly the same loss operator on the full P space. The recycling maps need not be equal.

Let \(\nu_x\) count vacant B neighbors of \(x\) before an outward hop. In its one-A-vacancy intermediate state,
\[
\sum_{y\sim x,\sigma} j_{xy,\sigma}^*j_{xy,\sigma}
 =2(1-n_x)\sum_{y\sim x}(1-n_y).
\]
An outward hop decreases that vacancy count by one. Hence
\[
\Gamma_0=2\sum_{x\in A}(\nu_x-1)\,PF_x^*F_xP.         \tag{6}
\]
The factor \(\nu_x-1\) commutes with \(PF_x^*F_xP\), which preserves the number of occupied B neighbors of \(x\). When \(\nu_x=0\), \(F_x\) vanishes; when \(\nu_x=1\), there is no room for the birth. There is no negative loss contribution from these cases.

One term of (6) moves at most one B record and possibly exchanges its color with its A anchor. This proves the input-specific fact
\[
Q\Gamma_0\xi_+=Q\Gamma_0\xi_-=0.                      \tag{7}
\]
For \(\xi_-\), both original positive B sites neighbor the negative A site \(a\). A loss term anchored elsewhere can move only one, leaving the other as a neighbor. A term at \(a\) either returns the same negative record or puts its negative color on B, which is inside the union. For \(\xi_+\), the negative label stays on B unless a return moves it to an A anchor \(x\); in that event the positive record just moved outward from \(x\) is still at a neighboring B site. Thus it is inside the union as well. This argument is about every output word, including its actual electric shift; it does not dephase anything.

Equation (7) is not the operator claim \(Q\Gamma P_{\rm nn}=0\) for all allowed groupings. A general grouping may have only one adjacent positive B site. Nor does (7) remove loss from the no-event evolution: \(\Gamma\) contributes to the remainder, survival and later motion.

For reference, the exact initial mean losses can also be counted. For one branch with occupied B pair \(\{b,c\}\), the diagonal contribution to \(\Gamma_0\) is
\[
2\sum_x(6-r_x)(5-r_x)=60n-240+4|N(b)\cap N(c)|,
\]
where \(r_x\) counts how many of these B sites neighbor \(x\). Averaging the five possible \(c\)'s gives \(60n-232\) at \(L=4\), and \(60n-1164/5\) at every even \(L\ge6\). For \(\xi_+\), the emitter loss term connects its twenty ordered distinct branch pairs with coefficient six, adding \(24\) after normalization. For \(\xi_-\) these off-diagonal overlaps are absent: the color changes; other anchors leave distinguishable electric edges. The opposite signs have no loss overlap because one \(F_x^*F_x\) term cannot replace the color of an already occupied marked B site while leaving it occupied. Therefore
\[
\frac{\langle\Gamma\rangle_-}{\kappa}
=\begin{cases}60n-232,&L=4,\\60n-1164/5,&L\ge6,\end{cases}
\quad
\langle\Gamma\rangle_+=\langle\Gamma\rangle_-+24\kappa,
\quad
\langle\Gamma\rangle_{\rm coh}
=\tfrac12(\langle\Gamma\rangle_-+\langle\Gamma\rangle_+).
                                                               \tag{8}
\]
This finite-input loss calculation is separate from the leakage coefficient.

## 3. Two complete Gauss-legal transport witnesses

Use the branch \(c=(0,0,1)\) in (4). All coordinates below are valid modulo every even \(L\ge4\). The displayed final sites remain distinct, and their quoted shortest torus distances are unchanged at \(L=4\).

### Negative resolved sign

Initially the minus is at \(a\), with positive B sites \(b,c\). Put
\[
d=(1,1,0),\qquad u=(1,0,0),\qquad v=(0,1,0).
\]
The two A stars \(a,d\) overlap at \(u,v\). In their retained \(S_{ad}^*S_{ad}\) term choose:

1. Move the negative charge \(a\to u\).
2. Move the positive charge \(d\to v\).
3. Return the negative charge \(u\to d\).
4. Return the positive charge \(v\to a\).

The final word \(w_-\) has its minus at \(d\), the same two positive B sites \(b,c\), and field
\[
E_-^{\rm out}
=-{\bf e}_{ab}-{\bf e}_{ac}
+{\bf e}_{au}-{\bf e}_{dv}+{\bf e}_{av}-{\bf e}_{du}.    \tag{9}
\]
Its divergence is \(-2\) at \(d\), \(+1\) at \(b,c\), and zero elsewhere. At \(a\), the initial \(-2\) is canceled by the two positive incident field contributions. The intermediate B sites \(u,v\) have zero final divergence and are vacant. Thus every final Gauss equation holds, not just total charge.

Both \(b\) and \(c\) are at torus distance three from \(d\). No reassignment can put \(w_-\) inside \(P_{\rm nn}\). Exchanging \(u,v\) in the two outward choices gives a second legal path with exactly the same final charge and integer-field word. Each path has coefficient \(-2\) in \(H_4\).

### Positive resolved sign

Initially the minus is at the marked B site \(b\), with the other positive B site \(c\). Define
\[
d=(-1,1,0),\quad e=(0,2,0),\quad
u=(-1,2,0),\quad v=(0,2,1).
\]
The A stars \(d,e\) overlap, and the following path occurs in their retained pair term:

1. Move the positive charge \(d\to u\).
2. Move the positive charge \(e\to v\).
3. Return the positive charge \(u\to e\).
4. Return the negative charge \(b\to d\).

The final word \(w_+\) has its minus at \(d\), positive B sites \(c,v\), and
\[
E_+^{\rm out}
={\bf e}_{ab}-{\bf e}_{ac}
-{\bf e}_{du}-{\bf e}_{ev}+{\bf e}_{eu}-{\bf e}_{db}.    \tag{10}
\]
At \(b\) the initial negative divergence is canceled by the negative return edge; \(u\) also has zero final divergence. At \(d\) it is \(-2\), at \(c,v\) it is \(+1\), and elsewhere it is zero. The two remaining positive B sites are each at distance three from \(d\), so \(w_+\) is also outside the entire reassignment union.

All primitive amplitudes in the specified tensor hard-core/rotor convention are nonnegative before the common factor \(-2\) in \(H_4\). The marked inputs in the integer-field basis also have positive branch amplitudes. Other permitted pair paths therefore cannot cancel either displayed contribution. Uniformly for all claimed tori,
\[
\langle w_-|H_4\xi_-\rangle\le-4,\qquad
\langle w_+|H_4\xi_+\rangle\le-2.                     \tag{11}
\]
The two final states have different minus locations and are orthogonal. The same-sign contributions add, without cancellation, when the input is \(\xi_++\xi_-\). Equations (5) and (11) imply all bounds in (2).

The finite controls at \(L=4,6,8\) separately find the exact matrix elements \(-4,-2\), with zero opposite-sign contribution to these particular targets. A second representation independently reconstructs every matching four-hop path for those targets. The universal lower-bound proof only needs the displayed paths and their common sign; it does not extrapolate absence of further matching paths from three periods.

There is also a saved reassignment discriminator: a physical word with minus at \(a\), positive B sites \(c=(0,0,1)\) and \(v=(0,2,1)\), and field
\[
-{\bf e}_{ac}-{\bf e}_{a u'}+{\bf e}_{e u'}-{\bf e}_{ev},
\quad u'=(0,1,0),\ e=(0,2,0).
\]
It is correctly kept inside the union because \(c\) remains adjacent, even though \(v\) is not. The test is therefore not secretly freezing one assigned dressing partner.

## 4. Full GKLS block identity, including recycling

The parent number identities hold for both instruments:
\[
[N,h]=0,\qquad [N,L_\mu]=2L_\mu,\qquad [N,\Gamma]=0.
\]
Starting at the definite sector \(\Pi_2\), every recycled contribution has larger record number and no subsequent term lowers it. The exact \(\Pi_2\) block of the full density is consequently
\[
\Pi_2\rho(t)\Pi_2
=e^{tG}|\psi\rangle\langle\psi|e^{tG^*},
\qquad G=-ih-\Gamma/2,                               \tag{12}
\]
with the restriction to \(\Pi_2\) understood. This follows directly from the number-block master equation or its bounded-jump Dyson expansion. It is not an assumption that subsequent events are forbidden. The full density remains trace one; all recycling probability is present in the higher blocks.

Since \(Q\le\Pi_2\),
\[
p_\psi(t)=\|Qe^{tG}\psi\|^2.                         \tag{13}
\]
Using \(Q\psi=0\), \(D\psi=0\), and (7),
\[
QG\psi=-i\delta QH_4\psi.
\]
The generator derivative therefore gives (1). There is no loss-linear or gain-linear term in this particular within-sector escape probability. This does not say that the full density is stationary to first order.

Let \(s(t)=\operatorname{Tr}(\Pi_2\rho(t))=\|e^{tG}\psi\|^2\). Then
\[
1-s(t)=\langle\Gamma\rangle_\psi\,t+O(t^2)
\]
is the probability of at least one additional birth by time \(t\). The probability of being outside the projector \(P_{\rm nn}\) in the full state is
\[
1-\operatorname{Tr}(P_{\rm nn}\rho(t))=1-s(t)+p_\psi(t).
\]
Thus leaving the first-postbirth sector is a distinct linear effect, while (1) demonstrates failure of the proposed grouping even among states that still have exactly one birth. If one chooses additionally to condition on that number sector, its escape probability is \(p_\psi(t)/s(t)\), with the same positive quadratic leading coefficient. Equation (13) itself involves no such conditioning.

For the raw selected output \(|\xi_\sigma\rangle\langle\xi_\sigma|\) or \(|\xi_++\xi_-\rangle\langle\xi_++\xi_-|\), the corresponding evolved weight is respectively five or ten times the normalized probability in (13). Including the original jump prefactor multiplies those weights by \(\kappa\). None of these factors is identified with an exact continuum time step.

## 5. Domains and a controlled probability bound

The finite-graph parent constructs the self-adjoint \(h\) on the multiplication domain of \(D\). The positive bounded \(\Gamma\) gives the contraction semigroup with generator \(G=-ih-\Gamma/2\) on that domain. The inputs in (5) are finite sums of physical integer-field basis words. The diagonal \(D\), every finite magnetic word and every bounded jump/loss word send such vectors to finite sums again. Therefore these particular inputs lie in \(D(G^k)\) for every finite \(k\). No assertion that arbitrary vectors in the possibly degenerate domain \(D(D)\) remain there under every shift is needed.

For any one of these normalized inputs let
\[
\alpha=\|QG\psi\|=\delta\|QH_4\psi\|,\qquad M_\psi=\|G^2\psi\|.
\]
Twice integrating the contraction-semigroup derivative gives, for every \(t\ge0\),
\[
\|Qe^{tG}\psi-tQG\psi\|\le\tfrac12M_\psi t^2.
\]
Hence
\[
(\alpha t-\tfrac12M_\psi t^2)_+^2
\le p_\psi(t)\le(\alpha t+\tfrac12M_\psi t^2)^2,        \tag{14}
\]
\[
|p_\psi(t)-\alpha^2t^2|
\le\alpha M_\psi t^3+\tfrac14M_\psi^2t^4.
\]

A deliberately loose, explicit bound makes the short-time scope concrete. The permitted local-pair norm bound at degree six gives
\[
\|H_4\|\le38880n,\qquad
\|\Gamma\|\le 2(6n)\kappa(6-1)^2=300\kappa n.
\]
The same loss bound applies to the coherent instrument because its loss equals the resolved loss. Define
\[
\mathfrak b=n(38880\delta+150\kappa),\qquad
M=\mathfrak b(\mathfrak b+180Kn).                     \tag{15}
\]
Since \(D\psi=0\), \(\|G\psi\|\le\mathfrak b\). Initial fields have edge magnitude at most one. A magnetic word has four unit shifts; a loss word has at most four before any cancellation. Thus \(G\psi\) is supported where every \(|E_e|\le5\). On that field box every occupied-B-gated electric summand is bounded by \(5\cdot6=30\); there are \(6n\) edges. It follows that \(M_\psi\le(\mathfrak b+180Kn)\mathfrak b=M\).

Let
\[
\ell_+=2\delta/\sqrt5,\quad
\ell_-=4\delta/\sqrt5,\quad
\ell_{\rm coh}=\sqrt2\,\delta.
\]
Replacing \(\alpha\) below by the appropriate proved lower bound and \(M_\psi\) above by (15) yields the controlled full-state probability inequality
\[
p_\psi(t)\ge(\ell_\psi t-\tfrac12Mt^2)_+^2.
                                                               \tag{16}
\]
In particular, for \(0<t\le\ell_\psi/M\),
\[
p_\psi(t)\ge\tfrac14\ell_\psi^2t^2>0.
                                                               \tag{17}
\]
This is a graph- and coupling-dependent local-in-time guarantee. The bound is not advertised as sharp or useful on macroscopic time scales. No uniform large-volume or weak-coupling time window follows from it.

## 6. Independent primitive controls and retained evidence

All code is newly written in this packet and imports no scientific code from the parents, earlier40 packet, or an author/checker. The main control uses explicit occupied/minus bitsets and sparse integer fields. It sequentially performs each legal outward/outward/return/return path with exact integer amplitudes and sums equal full physical words before taking norms. It includes every retained pair whose star union meets either initially occupied B site.

That restriction is exact for \(QH_4\xi_\sigma\). A pair whose union misses both B sites also misses the initial negative label: for the minus-sign input a pair containing its negative A emitter would necessarily contain those B neighbors in its union. Such an omitted pair sees only plus A charges and empty B destinations. Its two returns leave the initial matter word unchanged, although they may change the field by a circulation. It is therefore annihilated by \(Q\). No matter-changing term is omitted from the leakage action.

All A stars are retained in the loss action. At \(L=4,6\), a separate explicit composition of every original resolved \(B_\mu^*B_\mu\) and every stipulated coherent-edge loss also reproduces formula (6) on both actual sign outputs. This tests the loss against the full instrument, not just a scalar expected rate.

The complete exact finite coefficients are:

| Side \(L\) | \(C_+=\|QH_4\psi_+\|^2\) | \(C_-=\|QH_4\psi_-\|^2\) | \(C_{\rm coh}=\|QH_4\psi_{\rm coh}\|^2\) |
|---:|---:|---:|---:|
| 4 | 1584 | 816 | 1200 |
| 6 | \(8816/5\) | \(3296/5\) | \(6056/5\) |
| 8 | 1764 | 640 | 1202 |

These are exactly the \(\delta^2t^2\) coefficients in (1) on the three computed tori, with all electric fields retained. The cross-sign inner product of the two leakage vectors is zero in these controls. The general result does not infer this orthogonality or a stabilized coefficient for uncomputed volumes.

The controls retain a useful falsifier of premature dephasing: replacing the coherent sum over the five transfer destinations within the plus-sign output by its mixture changes \(C_+\) from 1584 to 1536 at \(L=4\), from \(8816/5\) to \(8624/5\) at \(L=6\), and from 1764 to \(8628/5\) at \(L=8\). The original path interference is therefore load-bearing. The side-dependent values also prevent an unnoticed replacement of the small tori by an unwrapped lattice.

The independent read-only verifier uses sparse charge maps rather than the control's bitsets to reconstruct the two complete witness matrix elements. The changed minus location identifies all possible A-pair terms that could contribute; it enumerates every outward and return choice for those pairs and every original birth branch. It recovers the two matching negative-sign paths, the one positive-sign path, and the zero opposite-sign contributions at each tested volume.

It also consumes every stored physical row, checks the full Gauss divergence, verifies the actual union projector, recomputes all norms and loss expectations from saved integer coefficients, and checks all source/stdout/receipt bindings. Its 18,782 checked rows count serialized occurrences, including coherent rows and witness intermediates, not that many distinct independent states. Complete source and outputs are retained:

| Evidence | SHA256 |
|---|---|
| primitive_transport.py | fe7c37c69b5fbff754b487a74375fb357b40542bbfda6319451de662c277e1d9 |
| L4_RESULTS.json | 2e896ec6eded7299c0b7e0102fff2805a5927101d3b704e56d8a846e7c8e7924 |
| L6_RESULTS.json | 0ba30fb5223f0148bcf86ae19058e6a9a48909997c0e1ad69c80f5d3d2f34952 |
| L8_RESULTS.json | adf385dc98dbf8477ff6c11b33ed1e6c5d67a73120070f554031cf85d748c21f |
| verify_read_only.py | db0e74ea33278f26bee2c5fcbfb68e01e8aa94a28510ce5321c043b6ef34cded |
| verification.stdout.txt | d95633c06ab117b62e6a4f287335dffb4266c59fcb3c797340ff6e826a813c62 |

The controls took about 0.90, 1.76 and 1.49 seconds externally; the independent read-only check took about 2.52 seconds. All recorded executions exited zero with empty stderr. No parent program, author program, finite-spin calculation or time integrator was run. The finite-time conclusion is proved by the semigroup estimate, not inferred from a truncated numerical propagator.

## 7. Scope stress test and remaining limits

The constructive conclusion is positive escape probability from this exact supplied projector and preparation. It is not a broad particle no-go.

- The union includes either positive B neighbor and every compatible electric state; a failure of a fixed arbitrary partner assignment is not substituted.
- The witnesses preserve all charges, the A background, integer Gauss flow and the original unsigned amplitudes. No zero-angle or color compression is used.
- Electric dynamics, anticommutator loss and recycling remain in the full law. Their precise leading-order roles are proved, not discarded.
- Another birth, conditional survival, within-\(\Pi_2\) transport and the full trace-one probability are distinct.
- The universal theorem uses explicit local paths valid also on \(L=4\); the large finite coefficients are confined to their actual three tori. No cutoff extrapolation supplies a volume theorem.
- The finite-support domain justifies the derivatives and controlled error. No arbitrary high-field state or growing-Hamiltonian approximation theorem is imported.
- A state at an unknown random event time, larger/time-dependent grouping radii, longer-range dressed preparations, scattering or binding, microscopic derivative limits, dynamics selecting a charge preparation and physical calibration remain separate questions.
- No audit verdict, new axiom, publication/repository mutation, model/effort change or delegation occurred.

There were no failed executions or unresolved proof obligations for the bounded escape statement above. The rejected simplifications—fixed dressing partner, dephased birth branches, ignoring occupied-B gates, extrapolating the \(L=4\) coefficient, or equating sector exit with the transport diagnostic—are explicitly distinguished. Work stops after this PRE seal, before any author43 disclosure.
