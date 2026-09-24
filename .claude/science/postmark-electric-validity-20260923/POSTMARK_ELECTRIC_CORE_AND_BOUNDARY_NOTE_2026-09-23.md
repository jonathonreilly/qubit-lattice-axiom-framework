# Post-mark finite-spin correction and interior edge limit

**Type:** bounded_theorem

This note proves a finite-support correction and a residue-resolved interior edge limit for a supplied six-site model. The selected state's fixed-laboratory-time observable comparison remains open. The construction is conditional on the supplied model and output; it neither establishes a TOE result nor changes an axiom. Independent review and audit remain pending.

**Exact claim.** For the supplied six-site alternating-ring model and frozen first-mark output, every fixed finite-support matrix entry satisfies \(C(H_{2,S}-H_{2,\infty})\to D\), and every fixed-residue interior sequence \(n/S\to\xi\), \(|\xi|<5\), has the complete-generator edge limit displayed below; in particular, \(S=n=15k\) gives the edge limit \(-196/625\). These coefficient statements do not assert convergence or separation of the frozen vector's fixed-time bounded-observable expectation.

## Source identity and scope

The framework checkout was current at Physics `main` `5efa36e7c357ae2a62ee586a5407f90982f6ded9` when the block was selected and the derivation began. During execution, `origin/main` advanced to `6bf62ae06ccbea85255e791d7e57b2b800ef4710`; its new bounded moving-record notes use other supplied laws and do not alter this six-site source or the four axioms. The construction depends on open, non-draft [PR #8831](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8831) at exact head `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`, whose base is open PR #8672 at `fe6dc2c5ef061fa1e0051063d49178f23b872c13`. The source model is [FAST_VACANCY_MOTION_AFTER_FORMATION.md](../mobile-record-formation-20260920/campaign12h_third/post_birth_fast_motion_author/FAST_VACANCY_MOTION_AFTER_FORMATION.md); its SHA256 is `76d7f2faf3a0b4635499ddff1d8a88868d691d58c035780af737129701e30eeb`.

The state is the supplied resolved first-mark output
\[
q_*=(1,-1,1,0,1,1),\qquad E_*=(1,0,0,0,0,1),
\]
on the six-site alternating ring. The observable frozen before propagation was the bounded projector \(O=\mathbf1[q_3=0]\), and the target compares the exact finite-spin generator \(C H_{2,S}+H_{4,S}\) to \(C H_{2,\infty}+D+H_{4,\infty}\) at fixed times \(1/4,1/2,1\), with \(C=S(S+1)\), \(K=\delta=1\). The complete frozen comparison is [TARGET.md](TARGET.md).

The minimal framework axioms do not supply this ring Hamiltonian, its spin-link representation, first-mark preparation, or the observable map. All claims below are conditional on those separately supplied objects. In particular, they do not derive electromagnetic dynamics or update a framework axiom.

## Exact finite-support correction

Write a physical basis state as \((q,E)\), with integer link flux satisfying the supplied Gauss constraint. A legal matter hop across a link changes its flux \(m\) by \(a\in\{-1,1\}\). Its normalized spin amplitude is
\[
t_S(m,a)=-\sqrt{1-\frac{m(m+a)}{C}}.
\]
On each fixed finite-flux state, Taylor expansion gives
\[
t_S(m,a)=-1+\frac{m(m+a)}{2C}+O(C^{-2}).
\]
Since \(H_{2,S}=-P T_S\Pi_1T_SP\), each ordered two-hop path \(p\) with intermediate flux data \((m_1,a_1),(m_2,a_2)\) contributes
\[
(H_{2,\infty})_p=-1,\qquad D_p=\frac{m_1(m_1+a_1)+m_2(m_2+a_2)}2
\]
to the zeroth and first coefficients. Thus on every fixed finite-support matrix entry,
\[
C\bigl(H_{2,S}-H_{2,\infty}\bigr)\longrightarrow D.
\]
The remainder is entrywise on a fixed finite set; no uniformity in flux or in propagated states is implied.

The reconstruction enumerates all ordered legal \(P\to\Pi_1\to P\) paths in the physical charge/flux basis, retaining both return paths and every distinct endpoint. There are 15 allowed \(P\)-charge words in this sector. From the actual output, the four paths give two diagonal returns and two distinct neighbors, hence \(H_{2,\infty}\) has diagonal \(-2\) and neighbor entries \(-1,-1\). The connected rotor component is indexed by \(n\in\mathbb Z\), with \(n=0\) at the actual output and
\[
H_{2,\infty}=-2I-U-U^*,
\]
where \(U|n\rangle=|n+1\rangle\). The exact rational entries of \(D\), including all 15 residue classes of the winding coordinate, are in [D_RESIDUE_POLYNOMIALS.json](D_RESIDUE_POLYNOMIALS.json); the independently enumerated path entries are in [CORE_D_RESULTS.json](CORE_D_RESULTS.json).

An independent dense assembly of the full physical finite-spin matrices gives maximum path-matrix discrepancies below \(9\times10^{-16}\) for \(H_2\) and \(9\times10^{-16}\) for \(H_4\) at \(S=2,3,4,6\), with no coupling from this component to other \(P\)-components. These floating matrix comparisons check the separate assembly, not the analytic limit. The exact path Taylor coefficient is the derivation of the core limit; see [FULL_SECTOR_CROSSCHECK.json](FULL_SECTOR_CROSSCHECK.json).

## The formal correction has a semibounded realization

Let \(d_n=D_{n,n+1}\), \(v_n=D_{n,n}\). In the unitary gauge \(G|n\rangle=(-1)^n|n\rangle\), the off-diagonal entries become \(-d_n\). On finitely supported vectors the quadratic form is exactly
\[
\langle\psi,GDG\psi\rangle=
\sum_n d_n|\psi_{n+1}-\psi_n|^2+
\sum_n r_n|\psi_n|^2,
\qquad r_n=v_n-d_{n-1}-d_n.
\]
The residue table proves that if \(n=15k+r\), then \(d_n\) is a quadratic polynomial with leading coefficient 9, \(d_n\ge k^2\) for \(|k|\ge3\), and
\[
r_{15k+r}=\alpha_r k+\beta_r,\quad
\sum_{r=0}^{14}\alpha_r=0,\quad \sum_{r=0}^{14}\beta_r=3,
\quad |\alpha_r|,|\beta_r|\le3.
\]
At fixed residue, every link flux is affine in the winding variable \(k\), so each two-hop coefficient is quadratic. The identities follow by exact rational interpolation of the path coefficients, followed by checks at \(k=-1,0,1,2,3\); the polynomials are quadratic, so those checks determine and verify them. The full coefficients and verification script are retained next to this note.

For completeness, group a vector into cells \(\psi_{k,r}=u_k+\eta_{k,r}\), where \(u_k=15^{-1}\sum_r\psi_{k,r}\) and \(\sum_r\eta_{k,r}=0\). Drop the nonnegative edges between cells. The 14 internal edges have weights at least \(k^2\) for \(|k|\ge3\), so the path-graph Poincare inequality gives a contribution at least \(\lambda k^2\|\eta_k\|^2\), where \(\lambda=2(1-\cos(\pi/15))>1/25\). The residue potential has cell mean \(3|u_k|^2\); its fluctuation is bounded below by \(-3(|k|+1)\|\eta_k\|^2-6\sqrt{15}(|k|+1)|u_k|\|\eta_k\|\). For \(|k|\ge200\), the first term absorbs the negative \(\eta\)-term and Young's inequality leaves a finite constant times \(-|u_k|^2\). For \(|k|<200\), the cell potential is bounded below by \(-600\|\psi_k\|^2\). Summing yields a uniform lower bound on the form over finitely supported vectors. The associated symmetric operator therefore has a Friedrichs extension.

Because \(H_{2,\infty}\) is bounded and the fixed-sector \(H_{4,\infty}\) is bounded, \(K C H_{2,\infty}+K D_F+\delta H_{4,\infty}\) is self-adjoint on the domain of this Friedrichs extension for fixed \(S,K,\delta\). This establishes one natural self-adjoint realization of the candidate. It does not establish essential self-adjointness, uniqueness of the extension, or that the finite-spin dynamics selects this extension.

## Boundary behavior under the zero embedding

For integer spin \(S\), the physical path interval is \(I_S=[-5S,5S-4]\). Put \(n_+=5S-4\). Exact substitution in the 15-residue formula gives
\[
D_{n_+,n_++1}=S^2.
\]
Indeed, for \(S=3m,3m+1,3m+2\), the relevant residue polynomials are respectively \(9(k+1)^2\), \((3k+1)^2\), and \((3k+2)^2\), with the corresponding boundary values of \(k\). Also \((H_{2,\infty})_{n,n+1}=-1\), while \((H_{4,\infty})_{n,n+1}=4\) in this one-vacancy sector, where the two-A-vacancy term vanishes and \(H_{4,\infty}=(2I+U+U^*)^2\).

The exact finite-spin generator has no state or edge beyond \(n_+\). For the finite-interval comparison, let \(Q_{I_S}\) be the projection onto \(I_S\), and compare the finite matrix \(Q_{I_S}G_S^{\rm app}Q_{I_S}\) with \(G_S\). Across the missing boundary edge, the exact matrix entry is zero, whereas the compressed candidate has entry
\[
-C+S^2+4=4-S.
\]
The boundary matrix element is therefore exactly \(4-S\). This is an exact entry identity for the declared zero embedding. It says nothing by itself about the selected state's fixed-time observable. The next section gives an interior coefficient witness using two states strictly inside the physical interval.

## Interior macroscopic-flux mismatch

The discrepancy is not confined to the artificial zero-extension edge. In this one-vacancy sector, the two-A-vacancy block vanishes exactly. If \(M_S=-H_{2,S}\), then \(H_{4,S}=M_S^2\), so the exact generator is the polynomial \(G_S=M_S^2-CM_S\) of a tridiagonal Jacobi matrix. The rotor counterpart is \(G_S^{\rm app}=C H_{2,\infty}+D+H_{2,\infty}^2\).

The exact edge and return-path factors for all 15 residues are tabulated in [FINITE_SPIN_JACOBI_COEFFICIENTS.json](FINITE_SPIN_JACOBI_COEFFICIENTS.json); explicitly, \((M_S)_{n,n+1}=\sqrt{(1-x_1/C)(1-x_2/C)}\) and \((M_S)_{n,n}=2-(y_1+y_2)/C\), where \(x_1,x_2\) are the two edge factors and \(y_1,y_2\) are the return factors. They imply the local macroscopic symbol
\[
m(\xi,p)=2(1-\rho)+2(1-\rho)\cos p
=4(1-\rho)\cos^2(p/2),\qquad \rho=\xi^2/25,
\]
for \(M_S\) when \(n/S\to\xi\) with \(|\xi|<5\). The leading symbol for \(G_S\) is \(-C m(\xi,p)\); its group velocity in the scaled coordinate \(\xi=n/S\) is of order S for generic p. This is a semiclassical scaling diagnosis, not a theorem about the localized state. It explains why fixed-flux Taylor control cannot simply be integrated over fixed laboratory time and points to long-time spectral asymptotics as the missing step.

For the unique path contributing to the \(n\to n+1\) entry, write its two link factors as \(x_1=m_1(m_1+a_1)\), \(x_2=m_2(m_2+a_2)\). At fixed residue \(r=n\bmod15\), each is quadratic in \(k=(n-r)/15\), with leading coefficient 9. Their linear-coefficient difference \(\gamma_r\) is 6 for \(r\in\{1,4,6,9,11,14\}\) and 0 otherwise; the complete exact polynomials are in [MACROSCOPIC_FLUX_SYMBOL.json](MACROSCOPIC_FLUX_SYMBOL.json).

For \(|\xi|<5\) and sequences with \(n/S\to\xi\) at fixed residue, put \(\rho=\xi^2/25\). Then \(x_i/C\to\rho\), and the exact identity for the \(C H_2\) plus \(D\) edge difference is
\[
C\left[1-\frac{x_1+x_2}{2C}-\sqrt{\left(1-\frac{x_1}{C}\right)\left(1-\frac{x_2}{C}\right)}\right]
=\frac C2\left(\sqrt{1-x_1/C}-\sqrt{1-x_2/C}\right)^2.
\]
Its limit is \(\gamma_r^2\xi^2/[1800(1-\rho)]\). In the one-vacancy sector \(H_{4,S}=M_S^2\), where \(M_S=-H_{2,S}\) is tridiagonal. The two return paths give \((M_S)_{nn},(M_S)_{n+1,n+1}\to2(1-\rho)\), and its connecting edge tends to \(1-\rho\). Therefore the full generator edge difference has the limit
\[
\lim_{S\to\infty}\bigl(G_S-G_S^{\rm app}\bigr)_{n,n+1}
=\frac{\gamma_r^2\xi^2}{1800(1-\xi^2/25)}-\frac{8\xi^2}{25}+\frac{4\xi^4}{625}.
\]
For example, along the physical sequence \(S=15k,n=15k\), \(\xi=1,r=0,\gamma_r=0\), so the edge difference tends exactly to \(-196/625\). Both endpoints lie strictly inside \(I_S\). For each such \(S\), this matrix entry is a lower bound in magnitude on \(\|Q_{I_S}G_S^{\rm app}Q_{I_S}-G_S\|\). This is an interior finite-matrix coefficient witness on the stated sequence. It does not determine whether the frozen \(n=0\) preparation has nonvanishing amplitude near \(n/S=1\) at any predeclared time, nor whether its fixed-time observable differs in the limit.

## Frozen numerical probe and disposition

In the path labeling, the actual projector is 1[q3=0] = 1[n mod 3 = 0]: the 15 exact charge words have a B3 vacancy precisely at residues 0,3,6,9,12 modulo 15, and this winding pattern repeats. Let omega = exp(2*pi*i/3) and define V|n> = omega^n |n>. The projector has the exact Fourier decomposition

    O = (I + V + V*)/3,     <O>_psi = 1/3 + (2/3) Re <psi,V psi>

for every normalized path state psi. Thus the predeclared observable depends on one pair of nontrivial mod-3 Fourier modes; equidistribution of all 15 classes is unnecessary and would be stronger than the target.

The original legal-hop/Krylov calculation and the new symmetric-tridiagonal spectral calculation agree to below 3e-12 for exact and candidate vacancy probabilities at S=24,32,48. The refreshed double-precision run extends through S=384 and candidate path cutoffs 6S,12S; the largest cutoff spread is 1.15e-9 at time 1 over this finite set. Exact vacancy values remain spin-dependent and the exact-minus-candidate sign changes. These are floating-point diagnostics; cutoff stability at finite dimensions is not a tail theorem or an asymptotic limit. Full residue probabilities and norm checks are in [SPECTRAL_FIXED_TIME_HIGH_SPIN.json](SPECTRAL_FIXED_TIME_HIGH_SPIN.json), with raw output in [spectral_fixed_time_probe.stdout](spectral_fixed_time_probe.stdout).

An exact-only extension using the same finite Jacobi matrix covers S=448,512,640,768,1024,1280. Over those six spins and the three frozen times, the vacancy probability ranges from 0.325912904 to 0.341669103, with norm-squared defects below 2e-15. Values stay near one third in this tested window, but they fluctuate and the scan neither compares the candidate above S=384 nor proves convergence. The runner, data and raw logs are [exact_high_spin_scan.py](exact_high_spin_scan.py), [EXACT_HIGH_SPIN_SCAN.json](EXACT_HIGH_SPIN_SCAN.json), [EXACT_HIGH_SPIN_SCAN_1024_1280.json](EXACT_HIGH_SPIN_SCAN_1024_1280.json), [exact_high_spin_scan.stdout](exact_high_spin_scan.stdout), and [exact_high_spin_scan_1024_1280.stdout](exact_high_spin_scan_1024_1280.stdout).

A secondary, post-selected diagnostic is the bounded projector 1[n>=S]. Under the exact finite-spin generator, its probability is between 0.318 and 0.353 for S=64,96,128,192 at each frozen time; under the rotor candidate, similar mass is seen at S=64,96. The high-spin spectral output resolves the mod-3 classes and all mod-15 classes. At S=384, the exact class probabilities at t=(1/4,1/2,1) are (0.34909,0.32767,0.32324), (0.33290,0.33952,0.32758), and (0.32924,0.33007,0.34069); the candidate gives (0.34697,0.32676,0.32626), (0.33444,0.34203,0.32353), and (0.32385,0.34037,0.33578). These finite double-precision values fluctuate with spin and time and do not establish a limit. Full values, Fourier identities, norm checks, and cutoff comparisons are in [SPECTRAL_FIXED_TIME_HIGH_SPIN.json](SPECTRAL_FIXED_TIME_HIGH_SPIN.json), [EXACT_MACROSCOPIC_TAIL.json](EXACT_MACROSCOPIC_TAIL.json), [EXACT_MACROSCOPIC_TAIL_96_192.json](EXACT_MACROSCOPIC_TAIL_96_192.json), [CANDIDATE_MACROSCOPIC_TAIL.json](CANDIDATE_MACROSCOPIC_TAIL.json), and [CANDIDATE_MACROSCOPIC_TAIL_96_96.json](CANDIDATE_MACROSCOPIC_TAIL_96_96.json).

**Disposition:** the finite-support coefficient identity and residue-resolved interior edge limit are proved under the supplied model; one semibounded self-adjoint realization is constructed; the fixed-time observable comparison remains open. The interior edge value is an existence witness on a named sequence, not a conclusion about this initial state's propagation.

## Next mathematical campaign

The exact short-time scaling theorem and its limitation are recorded separately in [SHORT_TIME_SCALING_NOTE_2026-09-23.md](SHORT_TIME_SCALING_NOTE_2026-09-23.md): at t=tau/C the vacancy expectation tends to `1/3+(2/3)J0(2 sqrt(3) tau)`. At fixed t, the exact evolution factors as `exp(it C M_S) eta_S(t)`, where `eta_S(t)=exp(-it M_S^2)|0>` converges strongly; the unresolved part is the long-time action with `T=Ct~S^2` on an O(S)-long interval. The mod-3 commutator has norm of order C, and the initial observable curvature divided by C^2 tends to -4. These results explain why a direct continuity estimate is not uniform but do not answer the frozen fixed-laboratory-time comparison. The next attack is to bound the mod-3 Fourier expectations under this long-time Jacobi evolution, retaining the finite-spin boundary and position-dependent coefficients, or certify a fixed-time discrepancy. The candidate realization still requires its domain and tails. The cube-loop readout remains the separate fallback.

## Proof-obligation graph and boundaries

1. **Legal-path amplitude expansion.** The supplied normalized spin-hop rule and fixed finite flux imply the scalar Taylor coefficient; proved here. This covers integer-spin link amplitudes on a fixed finite-support vector.
2. **Two-hop coefficient reconstruction.** Enumerate every ordered \(P\to\Pi_1\to P\) path, retaining returns and distinct endpoints; proved by the exact path enumeration in [CORE_D_RESULTS.json](CORE_D_RESULTS.json), with a separate dense finite-spin matrix comparison in [FULL_SECTOR_CROSSCHECK.json](FULL_SECTOR_CROSSCHECK.json).
3. **Residue polynomial and semibounded form.** The exact rational residue formulas and cell-form estimate give one Friedrichs realization; proved here with data in [D_RESIDUE_POLYNOMIALS.json](D_RESIDUE_POLYNOMIALS.json). Essential self-adjointness, uniqueness, and selection by the finite-spin sequence remain open.
4. **Interior edge limit.** The exact path factors and one-vacancy identity \(H_{4,S}=M_S^2\) yield the fixed-residue limit for \(|\xi|<5\); proved here. The endpoints \(\xi=\pm5\) are excluded. The sequence \(S=n=15k\) lies strictly inside \(I_S\) for positive \(k\).
5. **Observable-mode reduction.** The path charge pattern gives the exact period-three identity O=(I+V+V*)/3; the runner checks it over each represented domain. This reduces the target to two nontrivial expectations.
6. **Frozen-state propagation.** A statewise fixed-time limit or certified discrepancy requires control of electric tails, fourth-order terms, and the candidate domain/extension, in addition to the mod-3 Fourier expectations. This is the strongest missing lemma; the finite-dimensional computations and edge witness do not discharge it.

No half-integer spin, other charge sector, different formation output, volume limit, or framework-derived Hamiltonian is covered. The fixed-support expansion does not control supports growing with \(S\).

## Machine status and trace

```yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: conditional on the supplied six-site Hamiltonian, spin representation, first-mark output, and observable
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: Exact fixed-support and interior-coefficient statements are proved for supplied inputs; fixed-time dynamics and the framework bridge remain open.
audit_required_before_effective_retained: true
bare_retained_allowed: false
target_claim_id: null
target_blocker_text: "joint finite-spin electric limit"
source_of_blocker_text: handoff
artifact_role: theorem
next_trace_action: "After PR #8831 and its base chain land, bound the two nontrivial mod-3 Fourier expectations for the actual first-mark output, with tails and the candidate operator domain controlled."
```

The downstream consumer is the open post-formation result in [PR #8831](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8831), which explicitly leaves the joint finite-spin electric limit open. This note supports that test but does not close it. The supplied Hamiltonian, spin-link representation, output, and observable are imports, not consequences of the four minimal axioms or registered framework primitives. No source axiom is changed.
