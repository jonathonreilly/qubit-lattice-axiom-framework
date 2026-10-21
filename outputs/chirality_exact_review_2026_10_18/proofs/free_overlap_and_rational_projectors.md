# Free overlap formulas and conditional rational-projector argument

For the explicitly supplied free Euclidean Wilson symbol with r=1, let s_j=sin(p_j), S²=sum_j s_j² and beta=1-M+sum_j(1-cos(p_j)), with three spatial components. Put X=i gamma_j s_j+i gamma_4 sin(p_4)+(beta-cos(p_4))I, where the four Hermitian gamma matrices obey the Euclidean Clifford relations. Analytic continuation uses X-tilde obtained by reversing the gamma term, rather than complex conjugating continued p_4. Direct multiplication gives

X-tilde X = [1+S²+beta²-2 beta cos(p_4)] I.

For real momenta and a nonzero square root omega, D=I+X/omega. Its inverse is

D^(-1)=I/2 - i[gamma_j s_j+gamma_4 sin(p_4)]/[2(omega+beta-cos(p_4))].

The contact I/2 term affects t=0. For beta nonzero the branch threshold is E1=arcosh((1+S²+beta²)/(2|beta|)); its time phase is p_4=iE for beta>0 and pi+iE for beta<0. At beta=0 the radicand is constant and there is no such cut. For S>0 the isolated positive-frequency pole has E=asinh(S) when beta<sqrt(1+S²), with residue

R=[cosh(E)-beta]/sinh(2E) [gamma_4 sinh(E)-i gamma_j s_j].

Equality is the merging threshold; S=0 requires a limiting treatment, not division by sinh(2E). These formulas concern this free symbol. Finite quadrature or Hankel-rank calculations are diagnostics and do not establish the microscopic site dimension of an interacting realization. No global threshold minimization is inferred from a random search. A rational Schur complement is an algebraic realization, without an automatic Hermitian, reflection-positive or local-Hamiltonian interpretation.

For completeness, the actual conditional rational-idempotent proof remains live here. Suppose P=N/g is a matrix of Laurent rational functions, with a common Laurent polynomial denominator g nonzero on the entire real momentum torus, and P²=P there. Laurent polynomial uniqueness on the torus implies this identity on U=(C*)^d minus V(g). Thus its image is an algebraic vector bundle on the smooth affine open set U. Assume the standard algebraic-geometric inputs: localization surjects CH^k(A^d) onto CH^k(U), homotopy invariance gives CH^k(A^d)=0 for k>0, and algebraic Chern classes map to the corresponding topological Chern classes. Because U is open in A^d, these yield c_k(Im P)=0 upon restriction to the torus. This is a conditional topological argument with its exact domain and external theorem inputs, not a numerical consequence of the primary.

The Schur identity itself needs no topology: A-B E^(-1) C is rational if A,B,C,E have Laurent polynomial entries and det E is nonzero on the torus. Conversely N/g=0-N(-g I)^(-1)I. Invertibility here is an algebraic hypothesis, not a spectral-gap theorem for an unspecified physical auxiliary system.

If gamma5²=I, [R,gamma5]=0 and gamma5 D+D gamma5=2D gamma5 R D, direct multiplication gives [gamma5(1-2RD)]²=I; multiplying the GW relation on the left by gamma5 R is sufficient and [R,D]=0 is unnecessary. Hence (I-gamma5(1-2RD))/2 is idempotent. The original claims linking this conditional identity to arbitrary gauge-background anomaly indices, all species, all interacting mechanisms or an exhaustive choice of premises are not established by it. Terminal negative promotion remains pending an honest no-go packet and all required index-link hypotheses; the proof and formulas remain inspectable rather than erased.
