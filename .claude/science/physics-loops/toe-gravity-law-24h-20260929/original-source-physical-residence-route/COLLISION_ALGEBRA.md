# Exact nonlinear compensation collision and an original-word discriminator

This is an author calculation, pending independent checking. It complements the actual factorial budget; its finite control does not prove that budget.

## 1. The complete spin operator, not a gas of independent holes

Let Cspin=S(S+1), M_a=F_a*F_a, E_a=D_el,a and

 C_a^0=M_a+E_a/Cspin,
 N_a={c in A: c!=a, dist_1(a,c)<=2}, |N_a|=18,
 m_a=sum_(c in N_a)w_c,
 Q_a=product_(c in N_a)(1-w_c)=1_(m_a=0).

Here E_a is the actual diagonal nonnegative electric correction D_a,infinity-D_a,S multiplied by Cspin. Integer fields make each allowed E(E+/-1) nonnegative. Therefore 0<=C_a^0<=42 I, using ||F_a||<=6 and 0<=E_a<=6 Cspin n_a. It is supported on n_a=1 and commutes with m_a. The source compensation is exactly C_S=sum_a C_a^0 Q_a.

Expansion of the ACTUAL fast coefficient gives

 D2=C_S+[F,F*]
   =sum_a E_a/Cspin+sum_a F_a F_a*
       +sum_(a!=c)[F_a,F_c*]-sum_a C_a^0 m_a+R_col,
 R_col=sum_a C_a^0 [m_a-1+Q_a]
      =sum_a C_a^0 (m_a-1)_+ >=0.                        (C1)

The first four terms define D2_lin. D2_lin and D2 agree exactly on global W=0 and W=1. The nonlinear compensation remainder is positive and has the exact bound

 0<=R_col<=42 P_col,
 P_col=sum_a sum_({c,d} subset N_a) w_c w_d.              (C2)

Indeed (m-1)_+<=m(m-1)/2 on nonnegative integers. Including n_a in P_col would sharpen it, but is unnecessary here.

This is not an independent-hole Hamiltonian. F_a F_a* reshuffles B occupation around the same hole; the cross commutator moves a hole through a shared B and can change that B charge. All occupied-A gates, spin weights and hard-core blocking in D2_lin remain. Shared B variables prevent a tensor product of single-hole dynamics even when the explicit remainder is zero. There is no fixed B mask or static connected-component assumption.

One can separately decompose every bounded local interaction by its complete local hole-number sectors. It commutes with that count and its magnetic part vanishes on the zero-hole sector. However this generic block decomposition is weaker than(C1): it conceals the positive inclusion–exclusion remainder and should not be interpreted as a dynamical independence theorem.

## 2. Explicit quadratic-current price

The diagonal E_a part of R_col commutes with the full electric Q2=sum_e E_e^2. Only M_a contributes. Every path in M_a has two normalized elementary shifts and modulus at most one. There are at most36 paths per input and per output. A legal shift inside [-S,S] changes E^2 by at most2S-1; the safe two-shift bound4S+2 suffices. Schur's row/column bound yields

 ||i[M_a,Q2]||<=36(4S+2).

The hole factor (m_a-1)_+ commutes with M_a,Q2 and their commutator. Hence, as quadratic forms on the physical spin carrier,

 -36(4S+2) P_col <=i[R_col,Q2]<=36(4S+2) P_col.           (C3)

There is no dimension factor from the rotor/spin field. A fixed finite torus has a bounded Q2, so these are ordinary matrix inequalities; the constants are uniform in that matrix dimension.

If the separately proved factorial theorem is accepted, physical translation and its explicitly proved circuit return give

 <P_col>_sigma/n<=C_T epsilon^4 n.

Thus the actual signed nonlinear-compensation contribution obeys

 delta epsilon^-2/n integral_0^T |<i[R_col,Q2]>|dt
                           <=C_T epsilon n.              (C4)

This removes that contribution in the window epsilon n->0. It does not bound i[D2_lin,Q2], so it is not a complete energy balance. Positivity of R_col alone also gives no bound on its dynamical population or on dark residence.

## 3. An unsaturated six-label source word

Use L=16 with midpoint a=0 and two final holes h_-=-2e_x, h_+=2e_x. For each h, beginning with all A occupied, apply the following coefficient words in order:

 1. Neutral ordinary coefficient A_mu=j_mu F_p, p=h+e_x+e_y:
    outward hop to h+e_y, original plus mark on h+e_x.
 2. Neutral ordinary coefficient A_mu=j_mu F_q, q=h-e_x+e_z:
    outward hop to h-e_x, original plus mark on h-e_x+2e_z.
 3. Positive coefficient B_mu=-F_h j_mu F_h:
    outward hop to h-e_y, original plus mark on h+e_z,
    outward hop to h-e_z.

Apply this three-label sequence at h_- and then at h_+. These are six original edge labels, four neutral A coefficients and two positive B coefficients, with fourteen selected primitive operations. Every chosen field step is 0<->+/-1, so every selected spin amplitude is one for all integer S>=1. Every intermediate state is physical Gauss compatible. The final state psi has W=2, NB=14, all six B neighbors of each hole occupied, and actual total-charge/event relation NB-W=12=2*6.

All elementary normalized entries in the source basis are nonnegative. Each B coefficient carries one common minus sign; there are two such coefficients. Consequently the selected nonzero contribution to the COMPLETE six-coefficient same-label product cannot cancel against other paths in that product. For coherent marks, keep both sign summands inside each original edge operator. The displayed resolved-sign path is also a nonzero path of that coherent operator product; no extra sign label is observed.

This is an algebraic source-coefficient statement. It does NOT give a probability for the full microscopic Omega process, does not resolve the virtual hops as records, and does not assert that other normal-form grades may be measured or discarded. In particular it is not an independently sampled six-event process.

For this state, bare j_mu psi=0 for every mark because both holes are dark. Also D_mu psi=0 for every first grade-minus-two coefficient D_mu=[F*,j_mu]=-j_mu F* on dark input: an inward hop fills one hole and vacates a neighboring B, but the other hole is distance four away and is not adjacent to that vacancy. No original birth can then act. There is no common B neighbor of the two holes.

Only a=0 lies within distance two of both holes. Its incident fields are all zero, and precisely its +/-y and +/-z B neighbors are empty. Therefore

 <psi,R_col psi>=<psi,C_0^0 psi>=<psi,F_0*F_0 psi>=4,
 sum_mu ||j_mu psi||^2=sum_mu ||D_mu psi||^2=0.             (C5)

So a pointwise collision estimate by those TWO leading activities is false even for an explicit unsaturated, Gauss-compatible, source-coefficient-accessible input. This does not refute an estimate using the COMPLETE exact negative-grade activity, higher corrections, integrated propagation or the actual Omega weights.

There is also a literal nonzero current matrix entry. From psi, hop a=0 to e_y and then move the negative charge from -e_x inward to a. The final partner chi has the same two A holes, <chi,R_col psi>=1 and Q2(chi)-Q2(psi)=2. Its selected spin amplitudes remain one. This verifies that the positive collision correction is not merely a diagonal count penalty. It does not assign a nonzero current to the basis vector psi itself, whose commutator expectation is zero.

## 4. Control and missing conditions

The runner implements the actual primitive incidence and Gauss signs in a self-contained file; it does not enumerate a torus Hilbert space or import the older action helper. The author reread that older helper for the A-to-B sign convention before writing this control; no independent-review status is claimed. Frozen expected values preceded execution. At S=1,2,7 it checked84 intermediate Gauss identities, all14 selected steps per source word,12 legal inward paths per final state, absence of every following original birth, the midpoint vacancy count4 and a unit selected off-diagonal two-hop path with Q2 increment2 (uniqueness of that matrix entry is the analytic path argument above). The script's eight reported check families passed.

Actual execution was0.111405 child CPU seconds,0.141666 wall seconds,17,121,280 bytes peak child RSS, under5CPU/30wall/100MiB with BLAS1 and original deadline/STOP guards. CPU and wall caps were enforced; RSS was measured at return. No failure or rerun occurred. The controls establish the displayed finite-word facts, not the analytic uniform factorial or residence estimate.

The exact positive-grade local injection into a two-hole sector is small: on a complete fixed jump cone U, J_+1 changes W_U by one, so

 J_+1* 1_(W_U>=2) J_+1 <= C epsilon^4 1_(W_U>=1),

and each J_r, r>=2, has norm O(epsilon^3). After the physical kappa epsilon^-2 prefactor and the actual local rare-hole estimate, the total such injection is O_T(epsilon^4). This is an injection estimate only. Local collision occupation can be fed by fast flux through the cone boundary. The factorial proof closes a GLOBAL count budget, preserving an n^2 price; it does not prove a volume-uniform local pair budget.
