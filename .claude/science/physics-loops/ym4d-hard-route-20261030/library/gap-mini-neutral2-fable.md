lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-20T10:06Z

# gap-mini-neutral2-fable: second independent attack on (N-phys) (FINISH row 1184)

Working file of a Mac mini worker session, pinned at commit 654e32080 of branch claude/ym4d-hard-route. Research-stage
working state: it grants no status and is not a public claim. Every statement below carries one of the marks PROVED,
ARGUED, GUIDE, OPEN. Nothing here is computer-assisted.

## 0. Status log (times by `date -u` in the same command that writes the line)

- 2026-11-19T22:06Z start. Plan: (1) read the queue row, FINISH rule sections, GOAL.md; (2) read the exact statement of (N-phys)
  (row 1161, `library/gap-solve9-astra62.md` L146-148, restated in `library/gap-mini-branch-fable.md` L304-310) and its
  consumer; (3) read `library/gap-council-synthesis.md`, `parts/gap.md`, and the RESULT lines of rows 1143-1182;
  (4) write the statement and what a proof / a counterexample would have to be (Section 1); (5) attack, one route per
  response, appending each result here before thinking further; (6) only after my own attack is written, read
  `library/gap-mini-neutral-fable.md` (row 1180) and compare. Not read so far: row 1180's file.
- 22:17Z read: FINISH rule sections (L52-73, L299-350), GOAL.md, row 1184, `gap-council-synthesis.md` (full),
  `parts/gap.md` (L1-104 formulation, methods 19-36, lead rules; L186-207 obligations of rows 1127-1175; L213-322
  route registry, test table, price), RESULT lines of rows 1143-1183 (1143-1175 through `parts/gap.md`, 1176-1183 from
  FINISH), `gap-solve9-astra62.md` L1-160 (row 1161), `gap-mini-branch-fable.md` L1-400 (row 1179),
  `gap-phys-seed.md` L60-68 and L309-324 (trajectory, the set P, Theorem ZD-c). Not read: row 1180's file.

## 1. The statement, and what it says (written before any attack)

### 1.1 Statement

Notation of row 1161 (`gap-solve9-astra62.md`). Periodic spatial cube n^3, 4 | n, Wilson SU(2) at coupling beta.
F_0 is the symmetric positive transfer operator of the periodic cube on the gauge-invariant slice space, and
lambda_0 = norm(F_0). The centre flips C_1, C_2, C_3 (the sign of every i-link that crosses one plane x_i = const)
commute with F_0. The neutral sector is the joint +1 eigenspace. Put

    X(u) := Tr_neutral (F_0/lambda_0)^u = (1/8) sum over temporal twists e in (Z_2)^3 of Z_(0,e)(n^3 x u) / lambda_0^u,
    s(u) := X(u) - 1   (the neutral excited trace; row 1161 writes s(u) = X_(0,0)(u) - 1).

**(N-phys)** (row 1161 L146-148; row 1179 L304-309). Fix s_0 = 1/2, J = [1/2, 1], eps < 1/(8 x 5041), and
K = K(s_0, eps, J), the integer of row 1161's finite-aspect statement. There are a physical side L in
P = {2^i l_1} and j_0 such that for every cutoff j >= j_0 (spacing a_j, coupling beta_j, n_j = L/a_j, 4 | n_j) there
is an integer u_j with 3 <= u_j <= n_j/K and s(u_j; n_j^3) <= 1/2.

Consumer (rows 1161, 1179, 1065; under check in row 1183): (N-phys) gives the Pfaffian seed in both flux
alternatives, and so a cutoff-uniform gap on the centre-blind sector. I do not re-prove the consumer here.

### 1.2 Elementary exact facts (PROVED; each is a two-line argument)

Let 1 = mu_0 > mu_1 >= mu_2 >= ... > 0 be the eigenvalues of F_0/lambda_0 in the neutral sector (F_0 is positive
and trace class; the vacuum is simple and neutral by positivity of the kernel, row 1161 L17).

- (E1) s(u) = sum over i >= 1 of mu_i^u is non-increasing in u. So (N-phys) is the same as
  s(floor(n_j/K); n_j^3) <= 1/2 for every j >= j_0. Only the largest allowed time matters.
- (E2) Each level obeys mu_i^u <= s(u). So s(u) <= 1/2 at u <= n/K forces, with m := - log mu_1 the neutral gap of
  the cube in lattice units,  n m >= K log 2.   (NC1)
  The neutral gap of the cube, in units of its inverse side, is at least K log 2.
- (E3) Counting. The number N(E) of excited neutral levels with - log mu_i <= E obeys N(E) <= (1/2) exp(u E).  (NC2)
- (E4) Converse with a count. If n m >= z and a short-time bound s(t_0) <= S_0 holds at some t_0 < u, then
  s(u) <= S_0 exp(- m (u - t_0)) <= S_0 exp(- z (u - t_0)/n). (Each term: mu_i^u <= mu_i^(t_0) mu_1^(u - t_0).)
- (E5) Thermal form. log X(u) = log Z_neutral(n^3 x u) - u log lambda_0(n^3), and
  log lambda_0(n^3) = lim over v of (1/v) log Z(n^3 x v). So log X(u) is the free energy of the thermal torus minus
  the same volume of zero-temperature cylinder of the same cross-section.

### 1.3 Reading in physical units (ARGUED; guides the attack, proves nothing)

With T = 1/(u a) = K/L and V = L^3, (E5) says log X = p_neutral(T, L) V / T, the neutral pressure of the box. So
(N-phys) is:  p_neutral(T, L)/T^4 <= log(3/2)/K^3  at  T = K/L.
A free massless gas has p/T^4 = const > 0 at every T (photon: pi^2/45), so X = exp(c K^3) at every size: (N-phys)
fails at every size for a massless theory, and for SU(2) at a side below the confinement scale (rows 1143, 1153:
the short-period gluon gas). For a theory with gap m_phys and a particle gas, p V/T is about
(K^2 x/(2 pi))^(3/2) exp(-x) with x = m_phys L/K, so (N-phys) holds from about L = (K/m_phys)(3 log K + const) on.
By (NC1) it cannot hold below L = K log 2 / m_phys. So (N-phys) is a statement at a side of at least K log 2
correlation lengths. With any K of row 1161's size this is far outside every numeric test on this machine: no
GUIDE run of (N-phys) itself is possible, and none is made in this file.

### 1.4 What kind of statement it is (from the lane's test table, `parts/gap.md` L268-309)

(N-phys) is T_ev, uniformly in the cutoff, at one physical size (row 1179 Section 6 item 5). It is false for compact
U(1) at weak coupling, for the free photon, and for every product with a massless factor. A proof has to use the
non-abelian structure, a rate, the whole state space, and typical fields. Tools are of kind (K-one) or (K-flow).
