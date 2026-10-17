# Two-contact ladder with the old added-incident cap

The bounded search found a finite stationary witness satisfying the original **added old-site incident cap 2** on both old qubits. A separately executed exact rational-residual calculation certifies

\[
 \|R(k_0)-\alpha W\|\;<\;1.76\,10^{-13},\qquad
 \alpha=r_{s=-1,p=-1}(k_0),\quad |\alpha|=1,
\]

for all four \((s=Z_1Z_2,p=X_1X_2)\) fibers, with the literal old Hamiltonian \(K=2I+Z_1Z_2\) and \(W=((9+12i)I+(-16+12i)X_1X_2)/25\). This is one clock momentum, corresponding to two old-dependent total energies. It is an operator-norm comparison and therefore includes arbitrary old-reference entanglement at that stationary fiber. The largest wrapped relative-phase error is consequently below \(1.77\,10^{-13}\) radians: for unit complex amplitudes the angle is \(2\arcsin(\text{chord}/2)\).

The exact computed upper bound is approximately \(1.752474830885985\,10^{-13}\); its full rational value is in [rational_point_certificate.json](rational_point_certificate.json). This is a fixed-point witness. No arbitrary-accuracy statement, all-future finite-packet theorem, independent reviewer acceptance, or original all-site hardware closure is asserted. The separate packet bridge remains a separate obligation.

## Exact selected coefficients and physical implementation

Use the positive strict nearest-neighbor ladder and scattering convention in [the immutable route](../ROUTE.md). Every terminating decimal in this table is **exact**, not an uncertainty interval. The certificate calls the source hopping coefficient `t`; it is denoted \(h\) here.

| Coefficient | Exact value | Coefficient | Exact value |
|---|---:|---|---:|
| \(J\) | 0.030021107107032 | \(g_A\) | 0.996878563816670 |
| \(g_B\) | 0.599319315560298 | \(h\) | 3.999349697888060 |
| \(\lambda_A\) | 3.801781381581202 | \(\lambda_B\) | 2.575033765788497 |
| \(u\) | 0.544607276405587 | \(\Delta_A\) | 2.192035527016003 |
| \(\Delta_B\) | 2.186826508897014 | \(\mu_0\) | 0.321494607058201 |
| \(\mu_1\) | -1.459892813020969 | \(q=\cot(k_0/2)\) | 4.510351185997098 |

Define \(\cos k_0=(q^2-1)/(q^2+1)\), \(\sin k_0=2q/(q^2+1)\), with \(0<k_0<\pi\). Thus both trigonometric inputs are exact rationals, while \(k_0\simeq0.436365793409261\). The kinetic energy is exactly

\[
 \epsilon_0=\frac{30021107107032000000000000000}{5335816955256357129429116105401}
 \simeq0.005626337514718896.
\]

The square ladder is old1 \((0,0,0)\), old2 \((1,0,0)\), source A \((0,1,0)\), source B \((1,1,0)\), and one-head clock sites \(c_n=(n,2,0)\), \(n\ge0\). Writing \(n=(I-Z)/2\), \(a=|0\rangle\langle1|\), and \(L_{AB}=a_A^\dagger a_B+a_B^\dagger a_A\), the source/old terms are

\[
 C=\Delta_A n_A+\Delta_B n_B+h(n_A+n_B-L_{AB})+u n_A n_B,
 \quad G=g_A n_A(I+X_1)+g_B n_B(I+X_2).
\]

The clock is the positive half-line hopping sum

\[
 H_c=Jn_{c_0}+J\sum_{n\ge0}(n_{c_n}+n_{c_{n+1}}
 -a_{c_{n+1}}^\dagger a_{c_n}-a_{c_n}^\dagger a_{c_{n+1}}),
\]

and the physical contacts/wells are

\[
 \lambda_A n_{c_0}(I+X_A)+\lambda_B n_{c_1}(I+X_B)
 +\mu_0 n_{c_0}+|\mu_1|(I-n_{c_1}).
\]

All blocks displayed are positive and at most two-body, with their supports on the listed nearest-neighbor edges or sites. No target \(W\) is placed in a hopping bond. The vacuum \(|00\rangle_{AB}\) is exactly dark for \(C+G\); the contact flips vanish when the clock head is absent. In that sector there is no added persistent old interaction. This does not assert that a finite packet has already returned the source exactly at a finite time.

The signed-potential scattering algebra replaces the last well by \(\mu_1 n_{c_1}\). The **physical** Hamiltonian therefore equals that signed Hamiltonian plus

\[
 \nu I=1.459892813020969\,I.
\]

Both physical total-energy bands acquire \(+\nu\), and time evolution acquires \(e^{-i\nu\tau}\). This scalar is retained alongside actual old aging; it is not discarded as an uncounted well offset.

## Complete channel closure

The full asymptotic old/source operator \(B=K+C+G\) has dimension 16. It commutes with \(p=X_1X_2\), giving two eight-dimensional blocks. The complete eigenvalue lists below are numerical displays of the exact block matrices; exact vacuum values, the exact single-excitation quartics, and the double-excitation formulas are recorded in [different_path_check.json](different_path_check.json) and the immutable route.

| \(p\) | All eight eigenvalues of \(B_p\), before \(+\nu\) |
|---|---|
| +1 | 1, 3, 3.705042189110481, 6.249366370510604, 11.711927442874522, 14.281182619636610, 14.634793474973128, 18.401939699970256 |
| -1 | 1, 3, 3.906519299420971, 5.891344983196852, 12.066787162441920, 14.082867177072476, 15.442237712348375, 17.594495462595010 |

Every eigenvalue \(b\) generates the band \([b,b+4J]+\nu\), with \(4J=0.120084428428128\). The incident vacuum bands before the common shift are \([1,1.120084428428128]\) and \([3,3.120084428428128]\). Their exact separation is

\[
 2-4J=1.879915571571872>0.
\]

The analytic lower bound on every excited-source eigenvalue is \(1+\min\Delta=3.186826508897014\). It exceeds the entire upper incident band by the exact positive margin

\[
 \min\Delta-2-4J=0.066742080468886>0.
\]

This bound pays for the full old-energy release of 2. Each incident total energy \(1+\epsilon_0+\nu\) or \(3+\epsilon_0+\nu\) has exactly one open channel per \(p\); the other old-vacuum band and every source-excited band are closed. No channel exclusion relies on the numerical eigenvalue approximation. The elastic outgoing source is vacuum in all four stationary fibers; localized evanescent amplitudes are included in the boundary solve.

## Actual added incident block norms

Each entry is the sum of norms of the **displayed positive physical blocks** incident on that site. The existing old edge has norm 3 and is separate from the added cap. Source hopping contributes \(2h\) at A and B, the contact contributes \(2\lambda\), and the positive vacancy projector contributes \(|\mu_1|\) at \(c_1\).

| Site | Immutable original witness | Selected capped witness |
|---|---:|---:|
| old1, added | 39.999996310531664 | **1.993757127633340** |
| old2, added | 19.739168471156288 | **1.198638631120596** |
| A | 100.460938 (rounded) | 20.332662089993454 |
| B | 84.395918 (rounded) | 17.078839343776311 |
| \(c_0\) | 2.405352 (rounded) | 8.015120691541701 |
| \(c_1\) | 6.701340 (rounded) | 6.730044773026091 |
| tail site | 1.555613 (rounded) | 0.120084428428128 |

The selected source loads are substantially reduced, but the clock boundary load increases. The witness meets the **old added cap**, not a cap of 2 at every added site. No global resource minimization is claimed. Its small \(J\) also reduces the clock group velocity, here approximately 0.025376758082332338.

## Retained alternative and actual search limits

The first search allowed either clock well to be a positive vacancy projector. Its best point, start 11, has numerical chord error \(6.0569652953395666\,10^{-12}\), phase-residual 2-norm \(7.529830276171857\,10^{-12}\), and a vacancy well at \(c_0\). It is retained as a **numerical** resource variant, without a separate rational certificate:

```
J=.376316199540247; k=1.537671975130416
gA=.6439382393073481; gB=.9998709290686835
h=3.6826317080947124; lambdaA=2.6196847825624525
lambdaB=3.770053749674341; u=2.948020046167829
DeltaA=4.508808839911606; DeltaB=3.564102565658795
mu0=-1.7498956277270894; mu1=.9245821797866128
```

Its scalar is 1.7498956277270894, source closure margin 0.0588377674978071, old-band gap 0.4947352018390121, old added loads 1.2878764786146962 / 1.999741858137367, source loads 21.349338346 / 23.417235386, and clock loads 8.118213791 / 9.969954477 (last four rounded). Its raw parameters and complete outputs are in [SEARCH.json](SEARCH.json). The later comparison constrained \(\mu_0\ge0\) and kept \(\mu_1\) signed; it found the selected point at global start 40. Both physical well locations were authorized. The comparison is retained as an outcome, not as a necessity for positivity.

The shared budget was at most 60 starts, `max_nfev=500` per start, and a cumulative 180-second search-wall checkpoint tested between completed starts. Actual use was **41 starts, 47.09935441613197 seconds**: 12 starts / 13.409708832856268 seconds with seed 2026101603, then 29 starts / 33.689645333215594 seconds with seed 2026101604. Both searches stopped upon a useful fit. The wider coefficient box coded after first-search start 30 was never used; all runs used \(J\in[.03,.49]\), \(k\in[.08,\pi-.003]\), \(g_A,g_B\in[.005,1]\), \(h,\lambda_A,\lambda_B\in[.001,4]\), \(u,e_A,e_B\in[0,4]\), and \(\mu_j\in[-4,4]\), with \(\mu_0\ge0\) only in the second search. Penalties were \(\Delta_j=2+4J+.05+e_j\).

There were zero exception failures, 34 starts reaching the evaluation limit, and 7 solver-success terminations; only 2 starts reached numerical target error below \(10^{-9}\). SciPy's `nfev` excludes finite-difference calls: the actual optimizer residual-call count was **213,016**, or **213,098** including recorded detail evaluations. Every initialization, termination reason, residual, coefficient, and load is retained in [SEARCH.json](SEARCH.json) and [ALLOWED_SEARCH.json](ALLOWED_SEARCH.json), with full stdout/stderr. Unsuccessful starts supply no no-go evidence.

## Verification and provenance

[certify_old_cap.py](certify_old_cap.py) reuses the original residual-certification algorithm on the new rational coefficients. It uses 90-digit mpmath only to propose roots/inverses, rounds certificate matrices to denominator \(10^{55}\), then uses exact `Fraction` residuals and positivity/Neumann/Sylvester bounds. The largest certified inverse infinity bound is below 163.903, and every reflection approximation has rigorous error below \(2.33\,10^{-51}\). The final exact assertion is `error < 176/10**15`, with explicit positive-block, old-coupling, and closure checks. The certificate is stronger than the binary64 discovery residual because it evaluates a slightly rounded point with higher-precision proposals and exact residual control; neither binary64 fit is the certificate.

[check_old_cap.py](check_old_cap.py) separately assembles the full physical four-qubit matrices. It checks vacuum darkness, \(XX\) symmetry, both block identities, and the exact single-excitation quartic identities. A different numerical method uses full 16-channel leads of lengths 12, 20, and 32, with only the open vacuum channels outgoing-terminated and all closed channels hard-wall terminated. The maximum matrix dimension is 512 with two right-hand sides. Across these runs its disagreement with the certified surface amplitudes is below \(2.90\,10^{-13}\), its linear residual below \(1.28\,10^{-15}\), and off-diagonal reflection below \(6.92\,10^{-15}\). These are author checks by different assembly/method, not independent review or a packet calculation.

Versions: Python 3.13.5, NumPy 2.4.4, SciPy 1.17.1, mpmath 1.3.0, SymPy 1.14.0; macOS 26.6.2 arm64. The boundary matrix is 16 by 16 per parity, with an eight-dimensional bulk block; the exact square-root residual is six-dimensional. Runs set `PYTHONDONTWRITEBYTECODE=1`, `OPENBLAS_NUM_THREADS=1`, `OMP_NUM_THREADS=1`. Full outputs, actual elapsed times, exact coefficient fractions, and provenance are stored locally.

Source scope remains the scientific branch at `c86e61caf46c848fe8cee57ecbea6e6fdad7a4bc`, supplied main `5b0e1cc44f422fb0138b02eb071d3d16b40dfbb2`, and the frozen PR9656/PR9657/workflow/contract sources identified in [the original manifest](../sources/MANIFEST.json). The sole campaign recovery checkpoint remains the parent's `worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/TARGET_CONTRACT.md`; this note is a bounded result artifact, not a replacement checkpoint.

All new files are confined to `old_cap_search/`. [ORIGINAL_SNAPSHOT.json](ORIGINAL_SNAPSHOT.json) pins all 36 preexisting files; [RECEIPT.json](RECEIPT.json) records their unchanged verification and the new execution summary. No shared sources, editable prompts, axioms, audits, Git state, PRs, or other chats were changed. No network calls were used.
