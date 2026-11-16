# Docs-top batch, note 61

Pin: `fa841753c1a6296e5ad45518375660b0f1004769`

Runners were not executed.

Fixes in this batch: one

### Successive ramp differences

False sentence: "The finest successive differences are \(1.664\times10^{-8}\) and \(4.371\times10^{-8}\), with observed ratios near four."

Check: the only ratio of those two printed differences is \(4.371/1.664=4371/1664=2.6268028846\ldots\). Last-digit wiggle of either mantissa still leaves the ratio near \(2.63\), not near \(4\).

Edit: state that ratio, about \(2.627\), and do not call it near four. Keep the next sentence, which already says these observations are not rigorous ODE enclosures.

## Note 61

- Path: `docs/INTERACTING_PREPARATION_CONTROL_WORK_BOUNDED_THEOREM_NOTE_2026-10-16.md`
- Result: fix
- Checked:
  - \(\sum_{l=1}^L\sin^2(\pi l/(L+1))=(L+1)/2\), so \(b_l=\sqrt{2/(L+1)}\sin(\pi l/(L+1))\) is normalized. Reflection gives mean index \((L+1)/2\), hence \(\mu_B=q\Delta(L+1)/2\). Support length \(L-1\) gives \(\mathrm{Var}\le(L-1)^2/4\). With \(M=L+2\), \(W_A-\mu_B=q\Delta(L+5)/2\), so \(p(W_A-\mu_B)=pq\Delta(L+5)/2\).
  - \(d_L=2\sin(\pi/[2(L+1)])\le\pi/(L+1)\), so \(4q d_L\le 4\pi q/(L+1)\). The allocation \(\epsilon/8+2(\epsilon/16)+\epsilon/4+2\cdot4\cdot(\epsilon/16)\) equals \(\epsilon\). For \(q=2\), \(L=3\), \(2q d_L=4\sqrt{2-\sqrt{2}}=3.0614674589\ldots\), which rounds to the printed packet bound \(3.06147\).
  - For \(|\rho-x|\le1/4\) and \(k=\lfloor\rho\rfloor+2\), \(k-x\in(3/4,9/4]\), so \(3\pi/2<\lambda\le9\pi/2\). The same margin holds for \(\lambda_p\). Also \(9\pi/2<6\pi=Q_*\).
  - \(u'=6s(1-s)\) has maximum \(3/2\). The three lower bounds on \(h_p\) give strength \(g/2\), envelope slew \(\sigma/4\), and carrier slew \(\sigma/4\). \(\int|f_h'|=4/h\), and \(\|Q\|\le5\pi/2\le Q_*\).
  - \(L=\lfloor\rho\rfloor+2\) with \(|\rho-16\pi q/\epsilon|\le1/4\) and \(0<\epsilon\le1\) gives \(L\le A_0/\epsilon\), \(L+1>16\pi q/\epsilon\), \(m\le D/\epsilon\), \(qL+qM\le E/\epsilon\), \(\overline G\le B_0\epsilon^{-4}\), and \(T\le H_{\mathrm{all}}\epsilon^{-4}\). Each carrier request spends at most \(\epsilon/128\), together \(\epsilon/64\). Each of \(\delta\Delta\) and \(\delta\pi\) spends one quarter of the printed \(\lambda_p\) and \(\lambda_b\) generator allowances.
  - \(\|[E,Q]\|\le r(r+1)g\) because \(\sum_{d=1}^r 2d=r(r+1)\). Local centering gives \(\|[E_X,Q]\|\le r_X b_X\), sharp on the printed \(r\)-flip. Tail size \(s=\lfloor(L+1)/8\rfloor\), occupations \(\le1/4\) for \(L\ge7\), and leakage \(\ge(s/2)\sin^2\theta\). Trace distance \(2\sqrt p\) gives energy gap \(m\Delta\epsilon^2/4\). The \(\epsilon^5\) and \(\epsilon^6\) requests reproduce \(\eta_H\le\epsilon/c\).
  - Printed \(K=2I+(3/5)XX+(2/5)ZI+(1/4)IX\) has \(\kappa=13/4\), \(\|K-2I\|\le5/4\), and \(\|[K,N_S]\|=5/4=1.25\). The three printed work figures add: \(-1.00909221+(-0.43059594)=-1.43968815\). Total dimension \(2^{q(L+4)}=16384\) at \(q=2\), \(L=3\). For \(L=2\), \(\beta=(p_1+p_2)/\sqrt{2}\) and \(\Delta t_0/\hbar=\pi\) are orthogonal.
- Not checked: the complex128 propagation itself, including residuals \(3.802\times10^{-16}\), \(0.0688813\), \(1.86715\), \(0.899839\), \(0.1083293\), and the runner print \(3.0074606\). That last print is compatible with \((\mathrm{width}(K)+7/5)\) times an error that still rounds to \(0.899839\), where \(\mathrm{width}(K)=1/2+2\sqrt{13}/5\), but the error was not recomputed. The imported factor \(131328\), \(R(q)\) for \(q>1\), hashes, and the metadata counts \(17\), \(26\), and \(7\) were not recomputed. \(R(1)=1\) is only the note's stated special case.
- Finding: The phase margin, sine mean, packet factor \(3.06147\), charge bound \(r(r+1)\), tail count, and printed \(K\) norm match the displayed algebra. The joined sentence that the two finest successive differences have ratios near four does not. The note already limits the width-free work bound to exact conservation, corrects the frozen battery label \(M=L+q\) to \(M=L+2\) while keeping the tail for every \(M\ge L\), and does not identify actuators, vacuum, a clock, a driver, halt, or reuse. `bare_retained_allowed: false` with `audit_required_before_effective_retained: true` is not a retained-audit claim. The note does not rename the standing primitives.
- Open: supplied complement actuators, independent vacuum, external timing, and readiness; carrying the runtime charge estimate back through number-changing preparation; a dissipative heat ledger; an idle-envelope realization for every finite \(L\) under arbitrary caps; polynomial classical or oracle time; and retained audit.
