# FINISH row 867, gap-sep-opus, Claude Opus 5.5 max

(file seeded by the lead; the author writes below)

Clone: /Users/jonreilly/ym4d-lead/clone at commit d17e0d63fe6a748ae144149598592635cf2240a6 (pulled 2026-11-12, already up to date).
Lane directory D = .claude/science/physics-loops/ym4d-hard-route-20261030.
Author: Claude Opus 5.5, max effort. Unchecked.

## Target

Find and prove an order-one input that separates SU(2) from U(1) in the one-slice
law of row 860 (D/library/gap-hs-max.md). Row 860 measured the environment
coefficient of spin 1/2 at 0.27 at beta 2.3 (GUIDE) but proved only 0.87; a frozen
vacuum gives 1. State each candidate exactly. Test it against U(1) in its Coulomb
phase, Q_8 and 2T before proving. Prove the strongest separation at beta about 2.3
with explicit constants. Say exactly whether and how it bears on the parity statement.

## Plan (at most eight steps)

1. Read row 860 (gap-hs-max.md) whole: Lemma OS, Lemma DS, P1-P3, GUIDE table, OPEN.
2. Read the fact-test rows (786, 838, 839, 843, 845) and SEED-FP (gap-finishline-opus.md 110-160), bounded.
3. State the candidates exactly (typical-value DS, non-abelian averaging, compactness /
   simple connectivity, no flat-connection family, centre Z_2) and test each against
   U(1) Coulomb, Q_8, 2T.
4. Pick the strongest surviving candidate; set up its exact statement in the one-slice law.
5. Prove it (lemma by lemma, each appended), with explicit constants at beta 2.3.
6. GUIDE numeric check (small, under 300 MB, minutes) to refute or calibrate constants.
7. Say exactly whether and how it bears on the parity statement (odd omega-class).
8. Status marks, OPEN list, RESULT line.

## Log

### Step 1a (READ). Row 860 = H = D/library/gap-hs-max.md, lines 1-90 (of 263).

- READ H:47 (from EX:88-103). Time period t, spatial three-torus Q, edges E, plaquettes P, periods >= 3.
  z = Int e^(beta tr g/2) dg. K = (x)_e C_beta, C_beta = Sum_j r_j Pi_j, r_j = I_(2j+1)(beta)/I_1(beta).
  B_m(U) = exp(beta Sum_p eta_(m,p) x(U_p)), eta = +-1 spatial sign cocycle. L_m = z^|E| K^(1/2) B_m K^(1/2)
  on H = L^2(SU(2)^E)^(gauge). Z^m = Tr L_m^t.
- READ H:48. Theta_omega = Prod_e J_e^(omega_e) (J_e flips the sign of one edge), omega closed 1-cochain;
  Z^m - Z^(m+v) = 2 Tr(P_- L_m^t), P_- = (1 - Theta_omega)/2.
- READ H:49 (E17). Q_F <= C a^p eta_*^(a/2), t = a. p = Tr(P_- L^a)/Tr L^a = (1 - R_m(v))/2.
- READ H:66. P1 (to be read in full below): 1 - 2p = E_m[(-1)^(N_h(cut))], parity of the number of
  half-integer edges crossing the cut in the one-slice law.
- READ H:72-86. Theorem HS: electric-energy bound, group-blind; ratio <= [r_j0^eta e^beta (e^(2beta)/z)^(1/(t-1))]^|E|.
  Note for me: lambda_+ >= z^|E| by Jensen with trial vector 1; Tr_H K <= (e^beta/z)^|E|.

### Step 1b (READ). H lines 90-169.

- READ H:102-106, Lemma OS. P_m(j_e = j_e, e in S) = E_mu[ Prod_(e in S) d_j r_j(beta) chi_j(U_p(e)) / k_beta(U_p(e)) ],
  p(e) = timelike plaquette over e between times 0 and 1, mu = twisted Wilson measure on Q x Z/t.
  k_beta(g) = Sum_j d_j r_j chi_j(g) = e^(beta x(g))/z (heat kernel of C_beta). [x(g) = tr g/2.]
- READ H:109-111. (a) weights sum to 1. (b) P(j_e half-int) = (1 - E_mu[e^(-2 beta x(U_p))])/2.
  (c) rho_j = rho_0 d_j r_j(beta) E_nu[chi_j(U_p)], nu = mu with the weight of p deleted, rho_0 = Z_(w/o p)/Z.
- READ H:115-119, Lemma DS. S plaquette-separated: P(j_e, e in S) <= P(all 0 on S) Prod d_j^2 r_j(beta) r_j(5beta).
  Proof: under nu_S condition on everything but the time-0 links l_e; l_e has density k_(beta rho)(U W),
  Sum of 5 staples = rho W, rho <= 5 (quaternion linearity). Conditional mean of chi_j(U_p) = r_j(beta rho) chi_j(W^-1 S_p).
- READ H:121-128. Cor DS-1: P(j_e >= 2) <= 0.275, P(half-int >= 5/2) <= 0.041 for beta <= 2.5.
- READ H:141-158 (GUIDE, 8^4, untwisted). beta 2.3: <x_p> = 0.6024, rho_0 = 0.6373, rho_1/2 = 0.3267,
  rho_1 = 0.0347, rho_3/2 = 1.26e-3, half-int density 0.328. Environment coefficients e_j = E_nu[chi_j(U_p)]/d_j:
  e_1/2 = 0.267, e_1 = 0.036, e_3/2 = 0.0028, e_2 = 1.3e-4 (beta 2.3); e_1/2 = 0.361 at 2.5.
  Proved bound e_1/2 <= r_1/2(5 beta) = 0.87; frozen vacuum has 1.
- READ H:163. Half-integer edges have density 0.33 (> bond-percolation 0.2488 of Z^3): Peierls on half-integer
  winding paths cannot work in the window.
- READ H:168. Proposition P1: Theta_omega = (-1)^(N_h(cut)); P_- = Pi_{N_h(cut) odd}.

My first observation (ARGUED, to be checked in Step 3). The environment coefficient e_j is the
character coefficient of the conditional law of U_p given the rest, with p's own weight removed.
In Lemma DS the bound is |r_j(beta rho)| <= r_j(5 beta) because the 5 staples could all align.
The typical rho is much smaller: the 5 staples are SU(2) elements of typical x about 0.6^? and
their quaternion sum has |sum| well below 5. This is where SU(2) vs U(1) may differ: for U(1),
the sum of 5 unit complex numbers also has typical modulus below 5. So "typical rho < 5" alone is
group-blind. Must find what differs.

### Step 1c (READ). H lines 169-263. Step 1 complete.

- READ H:170. p_m(t) = P_m(N_h(cut) odd) = (1/2)(1 - E_mu[exp(-2 beta Sum_(e in cut) x(U_p(e)))]).
  [So the parity statement is a Wilson expectation of a product of e^(-2 beta x_p) over the timelike
  plaquettes over the cut: a "flip the sign of beta on the cut layer" = the twisted/untwisted ratio.]
- READ H:172. Half-integer edges of a slice form a Z_2-cycle C. (E17): omega-class of C is zero except w.p. C a^p eta_*^(a/2).
- READ H:174-179, P2: (LS) = (E17) up to e^(-c|E|).
- READ H:181-185, P3: Theorem HS and Lemma OS verbatim for U(1), Q_8, 2T, 2O, 2I. Lemma DS holds for U(1)
  (staple sum of complex numbers is rho W), fails for finite groups (environment coefficient r^G(5beta) ~ 1 at flat background).
- READ H:187, Verdict V1 (ARGUED): positivity + kinetic eigenvalue bounds + rarity cannot prove (LS) (U(1) shares them).
  U(1) at beta 1.09 has r_1 = 0.477 (vs SU(2) r_1/2(2.3) = 0.479).
- READ H:191-193. Where they differ: vs frozen finite group: e_j <= r_j(5beta) < 1 (continuity). Vs U(1): "must be
  non-abelian: integer flux conserved and spreads in U(1); in SU(2) only parity conserved; 1/2 x 1/2 = 0 + 1."
- READ H:198, (R3) OPEN: proof must (i) fail for U(1) (fusion/parity), (ii) fail for frozen 2T (e_1/2 < 1 at typical
  value 0.27), (iii) work on a percolating set (no Peierls on half-integer paths).
- READ H:200. Reflection positivity holds for link-bisecting planes for edge-spin events (ARGUED there).
- READ H:229. Z_2 gauge: kinetic eigenvalue tanh(beta); self-dual tanh = 0.414; SU(2) r_1/2(2.3) = 0.479 > 0.414.
  2T: r_V = 0.48 frozen. U(1) at 1.09: 0.48 Coulomb. "Input (i) must be: no integer-valued conserved flux AND
  continuous; parity alone is Z_2 (freezes); non-freezing alone is U(1) (spreads)."
- READ H:250, OPEN: typical-value DS; any order-one input separating SU(2) from U(1) in the one-slice law.

Key formula to keep (from Lemma OS + Lemma DS proof): conditional on all links except one time-0 spatial
link l_e, with staple sum A (all 6 plaquettes containing l_e, quaternion sum, weighted by beta) and the staple
Sig of p(e): the environment coefficient for p(e) is r_j(beta|A - Sig|) chi_j(direction)/... ; for
spin 1/2: e_(1/2) = E_nu[ r_(1/2)(beta rho) cos(angle) ], rho = |sum of the 5 other staples| (with signs).

### Step 2 (READ). Fact-test rows and the finish line. FIN = D/FINISH.md (row n at line n + 77 here).

- READ FIN:863 (row 786). Periodic Villain U(1), every fixed beta >= 2^14: gauge-invariant Langevin gap on (Z/M)^4
  tends to 0 (Codex gpt-6-astra max, unchecked; check row 794). Wilson cosine form not proved (missing (W-score)).
- READ FIN:915 (row 838). Q_8 freezes near 1.15, 2T near 2.15, 2I near 5.7 (GUIDE, Hartung et al.). Haar moments of
  Q_8, 2T, 2O, 2I first differ from SU(2) at degrees 4, 6, 8, 12 (PROVED there). "A tool at the crossover must see
  spin 2 or 3, not spin 6."
- READ FIN:916 (row 839). Every background-uniform layer twist bound false above 4 G_3 = 1.0109 at the flat background.
- READ FIN:922 (row 845). Theorem AG: annealed condition (AN) gives a gap; Villain U(1) at beta >= 2^14 fails (AN)
  at the coefficient step (AN2). OPEN (SP-ext).
- READ FIN:943 (row 866). Codex lane on the parity statement itself. Not my target.
- READ FLN:117-121 (SEED-FP). Thermal sum S_(K,beta)(ell/(2a_K); (ell/a_K)^3) <= s_* < 1/5041 of the bare Wilson
  transfer operator, every first-passage datum (credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as
  authors of their text; Balaban for the effective-action estimates). FLN:149: (E17) is fixed-coupling; along the
  trajectory its constant must be bounded in physical units.

What the fact tests mean for a separating input X (my reading).
(F1) X must be FALSE (or fail to be provable) for U(1) Wilson at beta ~ 1.09 (Coulomb, matched r_1 = 0.477)
     or at large beta. Since U(1) has Lemma DS and Theorem HS, X must use more than "a staple sum of unit
     vectors has modulus <= 5".
(F2) X must fail for Q_8 above ~1.15 and 2T above ~2.15 (frozen). Since moments up to degree 4 (Q_8), 6 (2T)
     agree with SU(2), X must see a character of degree >= 4 (spin 2) or the continuum.
(F3) X must not be a worst-case one-site or one-block bound above the caps 2/3, 0.775, 1.0109.

### Step 3. The candidates, stated exactly, and tested before any proof.

Notation. G in {SU(2), U(1), Q_8, 2T}. x(g) = tr(g)/2 (unit quaternions) or cos(theta) (U(1)).
F = fundamental (spin 1/2; charge 1 for U(1); the 2-dim irrep for Q_8, 2T).
nu_p = the twisted Wilson measure with the weight of the one timelike plaquette p = p(e) deleted.
e_F(G, beta) := E_(nu_p)[x(U_p)], the environment coefficient of F (row 860 Step 4 (c): rho_(1/2) = 4 rho_0 r_(1/2)(beta) e_F).
Matched couplings (GUIDE decimals): r_F(beta) = 0.479 for SU(2) at 2.3 and 0.477 for U(1) at 1.09 (I_1/I_0(1.09) = 0.6300/1.3198).

C1 (typical-value form of Lemma DS). e_F(SU(2), beta) <= c(beta), with c(2.3) explicit and below r_(1/2)(5 beta) = 0.873.
  U(1) test. The same statement for U(1) is false deep in the Coulomb phase: e_F(U(1), beta) -> 1 as beta -> infinity
  (spin-wave reading, ARGUED: deleting p doubles the variance of theta_p, 1 - e_F ~ 1/(2 beta)). Near beta_c ~ 1.01 the
  U(1) value is unknown to me. So C1 separates SU(2) at 2.3 from the whole U(1) Coulomb phase only if
  c(2.3) < inf over beta > beta_c of e_F(U(1), beta). That is a GUIDE question (Step 4).
  Q_8 / 2T test. Frozen finite groups have e_F -> 1 (all other faces of a cube near 1 force U_p near 1). Fails for them. PASS.
C2 (non-abelian averaging, exact Haar moments). M_n(G) = Int x(g)^(2n) dg.
  SU(2): C_n/4^n ~ n^(-3/2)/sqrt(pi) (C_n Catalan; n = 1 gives 1/4). U(1): binom(2n,n)/4^n ~ (pi n)^(-1/2).
  Q_8: 1/4 for every n >= 1. 2T: (2 + 16 * 4^(-n))/24 -> 1/12. (PROVED: density (2/pi) sin^2 on the class angle;
  class sizes of Q_8 and 2T.)
  Q_8 / 2T test: PASS (decay against a positive limit |Z(G)|/|G|). U(1) test: the exponent 3/2 against 1/2 is dim(G)/2.
  At large b the same fact reads 1 - r_F(b) ~ 3/(2b) (SU(2)) against 1/(2b) (U(1)), and matching r_F(beta) absorbs it into
  the coupling (beta_SU(2) ~ 3 beta_U(1)). FAIL as a structural separation (ARGUED); any residue at order one is GUIDE.
C3 (compactness and simple connectivity). pi_1(SU(2)) = 0, pi_1(U(1)) = Z: SU(2) has no Z-valued vortex or monopole
  current. U(1) test: PASS. Q_8 / 2T test: FAIL (finite groups have no winding either, and their thin vortices,
  like those of SU(2) through SO(3) = SU(2)/Z_2, are Z_2-valued). No constant at order one.
C4 (no continuous family of flat connections, twisted form). On T^4 with twist in the (0,3) plane (the twist v of
  Z^(m+v) = Tr(Theta_omega L^t)), flat SU(2) connections exist and are isolated: holonomies O_0 = i sigma_1,
  O_3 = i sigma_2, O_1, O_2 in {+-1}; untwisted flat connections form T^4/Z_2. U(1): no twisted flat connection
  (commutators are 1, not -1), so the twist costs action, about beta pi^2/2 on a hypercube. U(1) test: PASS.
  Q_8 / 2T test: FAIL (i j i^(-1) j^(-1) = -1 in Q_8, and Q_8 < 2T).
C5 (centre Z_2 on half-integer spins only = no integer flux). The conserved flux through a cut is Z_2-valued for SU(2)
  (Theta_omega), Z-valued for U(1) (Phi = Sum_(e in cut) n_e commutes with L). U(1) test: PASS. Q_8 / 2T test: FAIL
  (Z(Q_8) = Z(2T) = Z_2). Z_2 gauge theory: FAIL.
C6 (Euler-characteristic weight; found in this step). In the character expansion a closed non-branching surface of spin j
  carries r_j^F d_j^(chi) for SU(2) (Schur: Int D_ab(g) D_cd(g^-1) dg = delta delta / d), and r_n^F per orientation for U(1).
  At matched r: wrapping tori (chi = 0) weigh 1 (SU(2)) against 2 (U(1), two orientations); small spheres 4 against 2;
  each handle costs d^(-2) = 1/4 in SU(2), nothing in U(1). U(1) test: PASS. Q_8 / 2T test: FAIL (Schur holds for finite
  groups; their F has d = 2 too).

Verdict of the tests (ARGUED; the C1 entry waits for GUIDE).
- Continuity-type candidates (C1, C2) separate SU(2) from frozen Q_8, 2T, but not structurally from U(1).
- Centre/non-abelian candidates (C3, C4, C5, C6) separate SU(2) from U(1), but not from Q_8, 2T.
- No single candidate passes both tests. This repeats row 860's addendum (H:229) with exact statements.
- The only candidate that might pass both at order one is C1 as a NUMBER: a local value that SU(2) at 2.3 has and that
  no deconfined U(1), Q_8 or 2T state has. That is decidable as GUIDE before any proof. Step 4 measures it.

Proof seed found while testing C1 (to be proved in Step 5; stated here so it is not lost).
Lemma QS (quadruple suppression). The four links of p lie pairwise in no common plaquette other than p (periods >= 3).
So under nu_p, given all other links, they are independent, each with density k_(beta rho_i)(b W_i), rho_i <= 5.
Hence E_(nu_p)[chi_j(U_p)]/d_j <= E_(nu_p)[Prod_(i=1..4) r_j(beta rho_i)] <= r_j(5 beta)^4.
At beta = 2.3: e_F <= 0.873^4 = 0.581 (decimal GUIDE until a hand bound on r_(1/2)(11.5) is written).
U(1): the same proof gives (I_1/I_0(5 beta))^4, 0.668 at beta = 1.09. 2T at 2.3: (0.9875)^4 = 0.951. Q_8: 0.9999.

### Step 4 (GUIDE; decides nothing). Script, kept here so the run is reproducible and no other file is written.

Run: python3 -c "$(awk '/^# BEGIN GUIDE867/{f=1;next}/^# END GUIDE867/{f=0}f' gap-sep-opus.md)" G beta L ntherm nmeas nskip seed cold|hot
G in su2, u1 (embedded as complex quaternions), q8, 2t. 4D Wilson heat bath, periodic, untwisted.
Estimators (one link integrated exactly; the identity is the computation in the proof of Lemma DS):
e_F = E_mu[x_p e^(-beta x_p)]/E_mu[e^(-beta x_p)] = E_(nu_p)[x_p]; P(odd) = (1 - E e^(-2 beta x_p))/2;
E_nu[QS4] = E_(nu_p)[Prod_(i=1..4) r_F(beta rho_i)] (the typical value of the Lemma QS bound), QS1 its one-link analogue.

```python
# BEGIN GUIDE867
import sys, time, itertools
import numpy as np
from scipy.special import ive
G, beta, L, nth, nme, nsk, seed, start = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
rng = np.random.default_rng(seed); D = 4
def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]; b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)
def qconj(a):
    c = a.copy(); c[...,1:] *= -1; return c
def sh(a, nu, s): return np.roll(a, -s, axis=nu)
if G in ('q8','2t'):
    els = []
    for s in (1,-1):
        for k in range(4):
            v = np.zeros(4); v[k] = s; els.append(v)
    if G == '2t':
        for sg in itertools.product((1,-1), repeat=4): els.append(np.array(sg)/2.0)
    E = np.array(els); Ec = qconj(E)
shape = (D,L,L,L,L,4)
U = np.zeros(shape)
if start == 'cold': U[...,0] = 1.0
elif G == 'su2':
    U = rng.normal(size=shape); U /= np.linalg.norm(U, axis=-1, keepdims=True)
elif G == 'u1':
    th = rng.uniform(0, 2*np.pi, size=shape[:-1]); U[...,0] = np.cos(th); U[...,1] = np.sin(th)
else:
    U = E[rng.integers(len(E), size=shape[:-1])]
idx = np.indices((L,L,L,L)).sum(axis=0) % 2
def staples(mu):
    out = {}
    for nu in range(D):
        if nu == mu: continue
        f = qmul(qmul(sh(U[nu],mu,1), qconj(sh(U[mu],nu,1))), qconj(U[nu]))
        Unm = sh(U[nu],nu,-1)
        b = qmul(qmul(qconj(sh(Unm,mu,1)), qconj(sh(U[mu],nu,-1))), Unm)
        out[nu] = (f, b)
    return out
def update(mu, p):
    st = staples(mu); A = sum(f + b for (f, b) in st.values())
    m = (idx == p); Am = A[m]; n = Am.shape[0]
    if G == 'su2':
        k = np.linalg.norm(Am, axis=-1); a = beta*k
        x0 = np.empty(n); todo = np.arange(n)
        while todo.size:
            u = rng.random(todo.size); at = a[todo]
            cand = 1.0 + np.log(np.exp(-2*at) + u*(1-np.exp(-2*at)))/at
            acc = rng.random(todo.size) < np.sqrt(np.clip(1-cand**2,0,1))
            x0[todo[acc]] = cand[acc]; todo = todo[~acc]
        v = rng.normal(size=(n,3)); v /= np.linalg.norm(v,axis=1)[:,None]
        r = np.sqrt(np.clip(1-x0**2,0,1))
        X = np.concatenate([x0[:,None], r[:,None]*v], axis=1)
        new = qmul(X, qconj(Am/k[:,None]))
    elif G == 'u1':
        k = np.hypot(Am[:,0], Am[:,1]); phi = np.arctan2(Am[:,1], Am[:,0])
        th = -phi + rng.vonmises(0.0, beta*k)
        new = np.zeros((n,4)); new[:,0] = np.cos(th); new[:,1] = np.sin(th)
    else:
        lg = beta*(Am @ Ec.T)
        new = E[np.argmax(lg + rng.gumbel(size=lg.shape), axis=1)]
    Um = U[mu]; Um[m] = new
def sweep():
    for mu in range(D):
        for p in (0,1): update(mu, p)
def Zlog(Av):
    if G in ('su2','u1'):
        b = beta*np.linalg.norm(Av, axis=-1)
        return (np.log(2*ive(1,b)/b) if G=='su2' else np.log(ive(0,b))) + b
    lg = beta*(Av @ Ec.T); mx = lg.max(axis=-1)
    return np.log(np.exp(lg - mx[...,None]).mean(axis=-1)) + mx
def Xmean(Av, S):
    if G in ('su2','u1'):
        k = np.linalg.norm(Av,axis=-1); b = beta*k
        rr = ive(2,b)/ive(1,b) if G=='su2' else ive(1,b)/ive(0,b)
        return rr*(Av*S).sum(-1)/k
    lg = beta*(Av @ Ec.T); w = np.exp(lg - lg.max(axis=-1, keepdims=True))
    return (w*(S @ Ec.T)).sum(-1)/w.sum(-1)
def rF(b):
    if G == 'su2': return ive(2,b)/ive(1,b)
    if G == 'u1': return ive(1,b)/ive(0,b)
    lg = b[...,None]*E[:,0]; w = np.exp(lg - lg.max(-1, keepdims=True)); return (w*E[:,0]).sum(-1)/w.sum(-1)
def measure():
    ST = {mu: staples(mu) for mu in range(D)}
    AA = {mu: sum(f+b for (f,b) in ST[mu].values()) for mu in range(D)}
    num = den = odd = 0.0; cnt = 0
    for mu in range(D):
        A = AA[mu]; zA = Zlog(A)
        for nu,(f,b) in ST[mu].items():
            for S in (f,b):
                Ap = A - S; w = np.exp(Zlog(Ap) - zA)
                num += (w*Xmean(Ap,S)).sum(); den += w.sum()
                odd += np.exp(Zlog(A - 2*S) - zA).sum(); cnt += S.shape[0]*S.shape[1]*S.shape[2]*S.shape[3]
    qs4 = qs1 = wsum = xp = 0.0; npl = 0
    for mu in range(D):
        for nu in range(mu+1, D):
            f_mn, b_mn = ST[mu][nu]; f_nm, b_nm = ST[nu][mu]
            xpl = qmul(U[mu], f_mn)[...,0]; w = np.exp(-beta*xpl)
            r1 = rF(beta*np.linalg.norm(AA[mu] - f_mn, axis=-1))
            r2 = rF(beta*np.linalg.norm(sh(AA[mu] - b_mn, nu, 1), axis=-1))
            r3 = rF(beta*np.linalg.norm(AA[nu] - f_nm, axis=-1))
            r4 = rF(beta*np.linalg.norm(sh(AA[nu] - b_nm, mu, 1), axis=-1))
            qs4 += (w*r1*r2*r3*r4).sum(); qs1 += (w*r1).sum(); wsum += w.sum(); xp += xpl.sum(); npl += xpl.size
    return np.array([xp/npl, num/cnt, den/cnt, odd/cnt, qs4/npl, qs1/npl, wsum/npl])
t0 = time.time()
for i in range(nth): sweep()
M = []
for i in range(nme):
    for s in range(nsk): sweep()
    M.append(measure())
M = np.array(M)
nb = 8; m = (len(M)//nb)*nb; B = M[:m].reshape(nb, -1, M.shape[1]).mean(axis=1)
def est(fn):
    full = fn(M.mean(axis=0)); jk = np.array([fn(np.delete(B, i, axis=0).mean(axis=0)) for i in range(nb)])
    return full, np.sqrt((nb-1)/nb*((jk - jk.mean())**2).sum())
zG = np.exp(Zlog(np.array([1.0,0,0,0])))
out = {'<x_p>': est(lambda a: a[0]), 'e_F': est(lambda a: a[1]/a[2]), 'rho_0': est(lambda a: zG*a[2]),
       'P(odd)': est(lambda a: (1-a[3])/2), 'E_nu[QS4]': est(lambda a: a[4]/a[6]), 'E_nu[QS1]': est(lambda a: a[5]/a[6])}
rb = float(rF(np.array([beta]))[0]); r5 = float(rF(np.array([5*beta]))[0])
print(f"G={G} beta={beta} L={L} start={start} nth={nth} nme={nme} nsk={nsk} seed={seed} time={time.time()-t0:.0f}s  r_F(b)={rb:.4f} r_F(5b)={r5:.4f} r_F(5b)^4={r5**4:.4f}")
print("  " + "  ".join(f"{k}={v[0]:.4f}({v[1]:.4f})" for k,v in out.items()))
# END GUIDE867
```

**GUIDE results, 8^4, untwisted, 150 thermalization sweeps, 64 measurements 2 sweeps apart, 8-bin jackknife errors.**
(4^4 smoke test first; SU(2) at 2.3 reproduces row 860's e_(1/2) = 0.267, H:157.) cold = ordered start, hot = random start.

| G | beta | start | phase (recalled) | <x_p> | e_F | P(odd) | rho_0 | E_nu[QS4] | r_F(5 beta)^4 (QS worst case) |
|---|---|---|---|---|---|---|---|---|---|
| SU(2) | 2.3 | cold | confined | 0.6021(3) | 0.2666(8) | 0.3274(6) | 0.6381(7) | 0.4492(2) | 0.5800 |
| U(1) | 0.95 | hot | confined | 0.5136(15) | 0.1270(24) | 0.0980(16) | 0.9011(16) | 0.3446(13) | 0.6197 |
| U(1) | 1.0 | hot | confined | 0.5795(18) | 0.2179(33) | 0.1624(21) | 0.8350(21) | 0.4192(16) | 0.6370 |
| U(1) | 1.02 | cold | Coulomb | 0.6692(20) | 0.4014(44) | 0.2651(21) | 0.7282(22) | 0.5116(18) | 0.6435 |
| U(1) | 1.05 | cold | Coulomb | 0.6925(8) | 0.4454(18) | 0.2899(8) | 0.7014(9) | 0.5413(6) | 0.6528 |
| U(1) | 1.1 | cold | Coulomb | 0.7170(9) | 0.4897(18) | 0.3164(8) | 0.6719(9) | 0.5757(5) | 0.6673 |
| U(1) | 1.2 | cold | Coulomb | 0.7521(6) | 0.5505(12) | 0.3544(5) | 0.6273(6) | 0.6251(3) | 0.6929 |
| U(1) | 1.5 | cold | Coulomb | 0.8126(3) | 0.6540(6) | 0.4207(2) | 0.5379(3) | 0.7136(1) | 0.7504 |
| U(1) | 2.0 | cold | Coulomb | 0.8646(3) | 0.7449(7) | 0.4700(1) | 0.4462(4) | 0.7909(1) | 0.8097 |
| 2T | 2.0 | hot | disordered | 0.5152(7) | 0.1295(10) | 0.1827(11) | 0.8076(13) | 0.5321(8) | 0.9006 |
| 2T | 2.3 | cold | frozen | 0.9773(3) | 0.9317(7) | 0.4926(0) | 0.2016(2) | 0.9454(1) | 0.9510 |
| Q_8 | 1.0 | hot | disordered | 0.2639(5) | 0.0049(3) | 0.0051(3) | 0.9949(3) | 0.1487(3) | 0.8531 |
| Q_8 | 1.3 | cold | frozen | 0.9882(3) | 0.9578(9) | 0.4573(1) | 0.3494(2) | 0.9611(1) | 0.9647 |

Readings (GUIDE).
1. C1 as a number. SU(2) at 2.3 has e_F = 0.267. Every deconfined state measured has e_F >= 0.40: U(1) Coulomb rises
   from 0.401 (beta 1.02) to 0.745 (beta 2.0); frozen 2T 0.93; frozen Q_8 0.96. The confined/disordered states have
   e_F <= 0.22. U(1) jumps from 0.218 to 0.401 across its transition. So on these points e_F is a local diagnostic that
   separates SU(2) at 2.3 from every deconfined state measured, with margin 0.13. (Row 860: SU(2) e_F = 0.361 at 2.5;
   linear interpolation crosses 0.40 near beta 2.56, inside the window 2.3-2.6.)
2. U(1) at matched kinetic eigenvalue (beta 1.1, r_F = 0.481): e_F = 0.490, against 0.267 for SU(2). The environment,
   not the kinetic factor, separates them at matched r_F: a factor 1.8.
3. Lemma QS. Its worst case r_F(5 beta)^4 is 0.580 for SU(2) at 2.3, below U(1)'s 0.667 at matched coupling, above the
   U(1) Coulomb VALUES only for beta <= 1.2. Its typical value E_nu[QS4] = 0.449; the rest (0.267/0.449 = 0.59) is the
   misalignment of the four smeared links. For 2T and Q_8 the QS constants (0.95, 0.96) sit at their frozen values.
4. Caveat, to be tested next: a local number cannot see the time extent. SU(2) at finite temperature (N_t = 3,
   beta_c about 2.18, recalled) is deconfined at beta 2.3. If its e_F is still about 0.27, then C1 holds in a deconfined
   state of SU(2) itself, and no argument whose only input is C1 can force (E17).

### Step 4b (GUIDE). The finite-temperature test of C1. SU(2) only, lattice Lt x Ls^3.

Script GUIDE867b: the GUIDE867 heat bath with shape (4, Lt, Ls, Ls, Ls); it reports e_F separately for timelike
plaquettes (the plaquettes p(e) of Lemma OS) and spacelike ones, P(odd) for timelike ones, and the Polyakov loop
<|Ls^-3 Sum_x x(P_x)|>, P_x = product of the temporal links over the time circle at x.

```python
# BEGIN GUIDE867b
import sys, time
import numpy as np
from scipy.special import ive
beta, Lt, Ls, nth, nme, nsk, seed, start = float(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), sys.argv[8]
rng = np.random.default_rng(seed); D = 4
def qmul(a, b):
    a0,a1,a2,a3 = a[...,0],a[...,1],a[...,2],a[...,3]; b0,b1,b2,b3 = b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0], axis=-1)
def qconj(a):
    c = a.copy(); c[...,1:] *= -1; return c
def sh(a, nu, s): return np.roll(a, -s, axis=nu)
shape = (D,Lt,Ls,Ls,Ls,4)
if start == 'cold': U = np.zeros(shape); U[...,0] = 1.0
else: U = rng.normal(size=shape); U /= np.linalg.norm(U, axis=-1, keepdims=True)
idx = np.indices((Lt,Ls,Ls,Ls)).sum(axis=0) % 2
def staples(mu):
    out = {}
    for nu in range(D):
        if nu == mu: continue
        f = qmul(qmul(sh(U[nu],mu,1), qconj(sh(U[mu],nu,1))), qconj(U[nu]))
        Unm = sh(U[nu],nu,-1)
        b = qmul(qmul(qconj(sh(Unm,mu,1)), qconj(sh(U[mu],nu,-1))), Unm)
        out[nu] = (f, b)
    return out
def update(mu, p):
    A = sum(f + b for (f, b) in staples(mu).values())
    m = (idx == p); Am = A[m]; n = Am.shape[0]
    k = np.linalg.norm(Am, axis=-1); a = beta*k
    x0 = np.empty(n); todo = np.arange(n)
    while todo.size:
        u = rng.random(todo.size); at = a[todo]
        cand = 1.0 + np.log(np.exp(-2*at) + u*(1-np.exp(-2*at)))/at
        acc = rng.random(todo.size) < np.sqrt(np.clip(1-cand**2,0,1))
        x0[todo[acc]] = cand[acc]; todo = todo[~acc]
    v = rng.normal(size=(n,3)); v /= np.linalg.norm(v,axis=1)[:,None]
    r = np.sqrt(np.clip(1-x0**2,0,1))
    X = np.concatenate([x0[:,None], r[:,None]*v], axis=1)
    Um = U[mu]; Um[m] = qmul(X, qconj(Am/k[:,None]))
def sweep():
    for mu in range(D):
        for p in (0,1): update(mu, p)
def Zlog(Av):
    b = beta*np.linalg.norm(Av, axis=-1); return np.log(2*ive(1,b)/b) + b
def Xmean(Av, S):
    k = np.linalg.norm(Av,axis=-1); b = beta*k; return (ive(2,b)/ive(1,b))*(Av*S).sum(-1)/k
def measure():
    acc = np.zeros(8)  # num_t, den_t, odd_t, n_t, num_s, den_s, n_s, xp_t
    for mu in range(D):
        st = staples(mu); A = sum(f+b for (f,b) in st.values()); zA = Zlog(A)
        for nu,(f,b) in st.items():
            tl = (mu == 0 or nu == 0)
            for S in (f,b):
                Ap = A - S; w = np.exp(Zlog(Ap) - zA); nm = (w*Xmean(Ap,S)).sum()
                if tl:
                    acc[0] += nm; acc[1] += w.sum(); acc[2] += np.exp(Zlog(A - 2*S) - zA).sum(); acc[3] += w.size
                    acc[7] += qmul(U[mu], S)[...,0].sum()
                else:
                    acc[4] += nm; acc[5] += w.sum(); acc[6] += w.size
    P = U[0][0]
    for t in range(1, Lt): P = qmul(P, U[0][t])
    return np.array([acc[0]/acc[3], acc[1]/acc[3], acc[2]/acc[3], acc[4]/acc[6], acc[5]/acc[6], abs(P[...,0].mean()), acc[7]/acc[3]])
t0 = time.time()
for i in range(nth): sweep()
M = np.array([(([sweep() for s in range(nsk)]), measure())[1] for i in range(nme)])
nb = 8; m = (len(M)//nb)*nb; B = M[:m].reshape(nb, -1, M.shape[1]).mean(axis=1)
def est(fn):
    full = fn(M.mean(axis=0)); jk = np.array([fn(np.delete(B, i, axis=0).mean(axis=0)) for i in range(nb)])
    return full, np.sqrt((nb-1)/nb*((jk - jk.mean())**2).sum())
out = {'x_p(timelike)': est(lambda a: a[6]), 'e_F(timelike)': est(lambda a: a[0]/a[1]), 'e_F(spacelike)': est(lambda a: a[3]/a[4]),
       'P(odd)': est(lambda a: (1-a[2])/2), '|Polyakov|': est(lambda a: a[5])}
print(f"SU(2) beta={beta} Lt={Lt} Ls={Ls} start={start} nth={nth} nme={nme} nsk={nsk} seed={seed} time={time.time()-t0:.0f}s")
print("  " + "  ".join(f"{k}={v[0]:.4f}({v[1]:.4f})" for k,v in out.items()))
# END GUIDE867b
```
**GUIDE results (GUIDE867b), SU(2), 200 thermalization sweeps, 64 measurements 2 sweeps apart, 8-bin jackknife.**

| beta | Lt x Ls^3 | start | phase (recalled beta_c(N_t=3) ~ 2.18, beta_c(4) ~ 2.30) | x_p timelike | e_F timelike | e_F spacelike | P(odd) | <abs Polyakov> |
|---|---|---|---|---|---|---|---|---|
| 2.0 | 3 x 12^3 | hot | confined | 0.4693(10) | 0.0855(19) | 0.1081(18) | 0.1285(24) | 0.0202(13) |
| 2.3 | 3 x 12^3 | cold | deconfined | 0.5883(6) | 0.2627(15) | 0.2752(9) | 0.3252(12) | 0.3450(55) |
| 2.4 | 3 x 12^3 | cold | deconfined | 0.6160(5) | 0.3118(14) | 0.3214(13) | 0.3650(9) | 0.4144(55) |
| 2.4 | 4 x 12^3 | cold | deconfined | 0.6328(6) | 0.3269(16) | 0.3239(13) | 0.3735(9) | 0.2722(63) |
| 2.5 | 4 x 12^3 | cold | deconfined | 0.6544(5) | 0.3662(10) | 0.3612(13) | 0.4004(5) | 0.3453(31) |
| 2.3 | 8 x 8^3 | cold | confined (T = 0 reference) | 0.6017(9) | 0.2675(23) | 0.2674(21) | 0.3282(17) | 0.0215(28) |

**Finding FT (the finite-temperature test; GUIDE, with a recalled theorem).** At beta = 2.3 the deconfined state
(N_t = 3, Polyakov loop 0.345) and the confined state (N_t = 8, Polyakov loop 0.02) have the same one-slice local
statistics within 1.5 percent: e_F 0.263 against 0.267, P(odd) 0.325 against 0.328. At beta 2.4 and 2.5 (N_t = 4,
deconfined) e_F is 0.33 and 0.37, equal to the zero-temperature values (row 860: 0.361 at 2.5).
In the deconfined state the odd sector does not die: a twist in a (0, i) plane costs an interface free energy
proportional to the spatial area, so 1 - 2p -> 0 and p -> 1/2 as the spatial sides grow at fixed N_t (recalled
physics; rigorous at fixed N_t and large beta by Borgs and Seiler 1983, recalled, not re-read).
Consequence (ARGUED). Every input that (a) is a statement about the one-slice law of a bounded set of edges and (b) holds
for all periods t >= 3 with the same constants is shared, at the GUIDE level, by a deconfined state of SU(2) itself at
the same beta. So no such input can force (E17) alone, whatever it says about U(1), Q_8 or 2T. This covers Lemma OS,
Lemma DS, Theorem HS (its constant only improves with t), Lemma QS, and C1 as a number. A separating input that can
carry (E17) must fail at t = 3: it must be a statement about the ground state of L_m or about many time slices.
This is a third fact test, next to U(1) Coulomb and frozen Q_8 / 2T: (T3) an argument must fail for SU(2) on tori with
one short period (N_t = 3 at beta 2.3), where the one-slice law is locally the T = 0 law.

### Step 5 (PROVED). Lemma QS: the typical-value direction of Lemma DS, with hand constants.

Setting as in row 860 (H:100): mu = mu_(m,t), the twisted Wilson measure on Q x Z/t, all periods >= 3, weight
Prod_q exp(beta eta_q x(U_q)), eta_q = +-1. For a spatial edge e, p = p(e) is its timelike plaquette between times 0
and 1. Its four links: b_1 = l_e (time 0), b_3 = l'_e (time 1), b_2, b_4 the temporal links at the two ends of e.
nu_S = mu with the weights of p(e), e in S, deleted (S a set of edges). r_j(s) = I_(2j+1)(s)/I_1(s).

**Lemma QS (PROVED here; not checked).**
(i) Two distinct links of p lie in no common plaquette other than p.
(ii) Under nu_(p), conditionally on all links other than b_1..b_4, the four links are independent, and b_i has density
     proportional to exp(beta Re(b_i A_i)) with respect to Haar measure, where A_i is a sum of five signed unit
     quaternions, so rho_i := |A_i| <= 5.
(iii) For every spin j: |E_(nu_p)[chi_j(U_p)]| <= d_j E_(nu_p)[Prod_(i=1..4) r_j(beta rho_i)] <= d_j r_j(5 beta)^4.

*Proof.* (i) A plaquette that contains two links meeting at a vertex in directions mu and 0 is the plaquette of the
(mu, 0) plane with that corner, which is p. Two parallel links of p are translates by one unit (of time for b_1, b_3;
of direction mu for b_2, b_4); a plaquette containing both is the plaquette they span, p, unless the period in that
direction is 2. Periods are >= 3.
(ii) Under nu_p the integrand is a product over plaquettes q != p. By (i) no such q contains two of the b_i. So the
factors that depend on b_i are the five plaquettes q != p through b_i, each of the form exp(beta eta_q Re(b_i T_q)) with
T_q a unit quaternion built from links outside {b_1..b_4} (T_q is the staple of q, or its conjugate when q runs through
b_i backwards: Re(b^-1 S) = Re(conj(S) b) by cyclicity and Re(conj(u)) = Re(u)). Re is real-linear, so the product is
exp(beta Re(b_i A_i)), A_i = Sum_q eta_q T_q, |A_i| <= 5 by the triangle inequality.
(iii) Write A_i = rho_i W_i with W_i in SU(2) (any W_i if rho_i = 0). The substitution g = b W_i and exp(s Re g) =
z(s) k_s(g) give E[D^j(b_i) | rest] = Int k_(beta rho_i)(g) D^j(g W_i^-1) dg = r_j(beta rho_i) D^j(W_i^-1), because
Int k_s(g) D^j(g) dg commutes with D^j(SU(2)) (k_s is a class function), so it is c I, and its trace is
Int k_s chi_j = d_j r_j(s) (k_s = Sum_l d_l r_l(s) chi_l). U_p is the cyclic product of the b_i^(+-1), and
D^j(b^-1) = D^j(b)^dagger. By the conditional independence of (ii), E[D^j(U_p) | rest] is the cyclic product of the four
matrices r_j(beta rho_i) M_i with M_i unitary. So |E[chi_j(U_p) | rest]| <= d_j Prod_i r_j(beta rho_i). Take E_(nu_p).
Finally r_j(s) = Prod_(n=1)^(2j) I_(n+1)(s)/I_n(s) is increasing in s (READ Q:162, Lemma 3.1 (b)), and rho_i <= 5. QED

**Corollary QS-1 (one edge; PROVED).** With rho_j = P_m(j_e = j) and e_j := E_(nu_p)[chi_j(U_p)]/d_j (row 860 H:111),
|e_j| <= r_j(5 beta)^4 and rho_j <= rho_0 d_j^2 r_j(beta) r_j(5 beta)^4. Lemma DS had the exponent 1 in place of 4.

**Corollary QS-2 (product form; PROVED).** Let S be a set of time-0 spatial edges such that for e != f in S every
endpoint of e is at spatial l-infinity distance >= 2 from every endpoint of f. Then for all spins (j_e),
P_m(j_e = j_e, e in S) <= P_m(j_e = 0, e in S) Prod_(e in S) d_(j_e)^2 r_(j_e)(beta) r_(j_e)(5 beta)^4.
*Proof.* The vertices of a plaquette are pairwise at l-infinity distance <= 1, and every link of p(e) has its spatial
ends at the endpoints of e. So no plaquette contains a link of p(e) and a link of p(f). With (i), under nu_S the 4|S|
links are conditionally independent with the densities of (ii). Lemma OS (READ H:104) gives
P_m(j_S) = (Z_(without S)/Z) Prod_e d_j r_j(beta) E_(nu_S)[Prod_e chi_(j_e)(U_(p(e)))], and Z_(without S)/Z = P_m(0_S).
Apply (iii) to each e. QED

**Constants (PROVED arithmetic).** Bessel recurrence I_(nu-1)(x) - I_(nu+1)(x) = (2 nu/x) I_nu(x) (termwise from the
series; the k-th terms combine to nu (x/2)^(2k+nu-1)/(k! Gamma(k+nu+1))). With R_nu = I_(nu+1)/I_nu it reads
R_nu = 1/(2(nu+1)/x + R_(nu+1)). An upper bound on R_(nu+1) gives a lower bound on R_nu and conversely. Start from
R_7 <= U_7(x) (READ Q:162, Lemma 3.1 (d), U_nu(x) = x/(nu + 1/2 + sqrt((nu+1/2)^2 + x^2))) and round outward:
x = 11.5: R_7 <= 0.5418, R_6 >= 1/(14/x + 0.5418) >= 0.5684, R_5 <= 1/(12/x + 0.5684) <= 0.6204,
R_4 >= 1/(10/x + 0.6204) >= 0.6711, R_3 <= 1/(8/x + 0.6711) <= 0.7317, R_2 >= 1/(6/x + 0.7317) >= 0.7978,
R_1 <= 1/(4/x + 0.7978) <= 0.8729.  So r_(1/2)(11.5) <= 0.8729 and r_(1/2)(11.5)^4 <= 0.5806.
x = 2.3 (short chain): R_3 <= U_3(2.3) <= 0.2992, R_2 >= 0.3438, R_1 <= 1/(4/2.3 + 0.3438) <= 0.4801.
The same seven-step chain gives r_(1/2)(12.5) <= 0.8829 (fourth power 0.6077) and r_(1/2)(13) <= 0.8873 (0.6199).
(Script re-check of the arithmetic, GUIDE: true values 0.87268, 0.88262, 0.88703; chain values 0.872844, 0.882827,
0.887261; the short chain at 2.3 gives 0.48007 against the true 0.47928.)

**What QS gives at beta = 2.3 (PROVED; GUIDE value in brackets).**
| quantity | Lemma DS (row 860) | Lemma QS | frozen vacuum | measured |
|---|---|---|---|---|
| e_(1/2) = E_nu[x(U_p)] | <= 0.873 | <= 0.5806 | 1 | [0.267] |
| rho_(1/2)/rho_0 = 4 r_(1/2) e_(1/2) | <= 1.676 | <= 1.115 | 1.917 | [0.513] |
| P(odd)/rho_0 (all half-integer spins) | <= 2.16 | <= 1.177 | sinh(beta)/z(beta) = 2.71 | [0.514] |
Window: e_(1/2) <= 0.6077 at beta = 2.5 [0.361] and <= 0.6199 at beta = 2.6.
(The P(odd)/rho_0 line adds j = 3/2: 16 r_(3/2)(2.3) r_(3/2)(11.5)^4 <= 16 x 0.0561 x 0.0688 <= 0.0618, with
r_(3/2) = R_1 R_2 R_3 <= 0.4801 x U_2(2.3) x U_3(2.3) and r_(3/2)(11.5) <= 0.8729 x 0.8018 x 0.7317, R_2(11.5) <= 0.8018
from the chain R_4 <= U_4, R_3 >= 0.7256; j = 5/2 adds <= 3e-4 by (G3); the tail beyond is smaller.)

**Fact tests of Lemma QS.**
- U(1): the proof is verbatim for U(1) (complex numbers; Schur on characters), with constant (I_1/I_0(5 beta))^4.
  So QS is group-blind against U(1), like Lemma DS. It is not a confining input and I claim none. At matched kinetic
  eigenvalue its constant is 0.581 for SU(2) at 2.3 and 0.667 for U(1) at 1.1 (GUIDE decimals of I_1/I_0(5.5) = 0.9038):
  the dimension of the group survives at order one in the worst-case link response (1 - r_F(5 beta) = 0.127 against
  0.096), but the U(1) VALUE at matched coupling (0.490, Step 4) is below the SU(2) BOUND 0.581.
- Q_8, 2T: step (iii) fails. For a finite group the conditional mean of D(b_i) is not r(s) times a unitary, and at the
  flat background it is r^G_V(5 beta) I with 1 - r^(2T)_V(11.5) <= g(5.75) <= 0.0128 (READ Q:180, Lemma 3.3 (c)): the
  same bound is >= 0.950 for 2T. QS uses continuity, as the brief's second test asks.
- Caps: QS bounds an expectation, not a contraction coefficient; the 2/3, 0.775, 1.0109 caps do not apply. (AN1): unused.
- T3 (Finding FT): QS holds for every t >= 3, so it holds in the deconfined N_t = 3 state. It cannot carry (E17) alone.

(Correction made in place in the table above: the Lemma DS entry for P(odd)/rho_0 is 1.676 + 16 x 0.0561 x 0.5121
+ 0.022 <= 2.16, and the frozen value is (k_beta(1) - k_beta(-1))/2 = sinh(2.3)/z(2.3) = 4.937/1.824 = 2.71.)

### Step 6. The parity of any set of edges is a 't Hooft loop; what T3 means for (E17).

**Proposition TL (PROVED; it extends row 860's P1 from the cut to any set).** For every set R of time-0 spatial edges,
E_m[(-1)^(N_h(R))] = E_mu[exp(-2 beta Sum_(e in R) x(U_(p(e))))] = Z_m(flip R)/Z_m,
where N_h(R) counts the half-integer edges of R in the one-slice law and Z_m(flip R) is the Wilson partition function
with eta_q replaced by -eta_q on the plaquettes p(e), e in R.
*Proof.* Lemma OS (READ H:104) with the weights (-1)^(2j) summed over j: Sum_j (-1)^(2j) d_j r_j chi_j(g) = k_beta(-g),
because chi_j(-g) = (-1)^(2j) chi_j(g); and k_beta(-g)/k_beta(g) = exp(-2 beta x(g)). The product over e in R of these
factors is the change of sign of beta on the plaquettes p(e). QED
For R = cut this is P1 (H:170): 1 - 2p = Z^(m+v)/Z^m. For R a square of side l in a cut plane, flipping the plaquettes
over R inserts a 't Hooft loop along its boundary (the twist of a closed cochain has no boundary; R has one). So the
parity of a bounded set of edges is a 't Hooft loop of the one-slice law, and the parity statement is the wrapping
't Hooft surface. The same identity holds verbatim for U(1), Q_8, 2T with their own k_beta (group-blind, like P1).

**Reading (ARGUED; the physics is recalled, not proved here).**
- Confined SU(2) (T = 0): 't Hooft loops have a perimeter law and the wrapping surface is free (p -> 0).
- Deconfined SU(2) at fixed N_t (T3): 't Hooft loops in planes that the twist v probes acquire an area law beyond the
  scale N_t, and the wrapping surface costs an interface free energy (p -> 1/2).
- U(1) Coulomb: 't Hooft loops have a perimeter law, but the wrapping surface costs about beta pi^2/2 on a hypercube
  (classical action of the twist, C4), so p stays near 1/2 - O(e^(-pi^2 beta/2)) on cubes.
So the three deconfined comparison states fail the parity statement in three different ways. A local one-slice input
sees none of them: by Steps 4 and 4b its value is fixed by beta and the group to 1.5 percent, whatever the shape.

**T3 for the admissible shapes (ARGUED, GUIDE).** The tori of (E17) are (a, a, c, d) with t = a and the cut across
direction 3 or 4 (READ H:49). At beta = 2.3 the shape (3, 3, c, d) with c, d large has two periods equal to 3, inside the deconfined range (N_t = 3 is deconfined at 2.3; N_t = 4 is critical there),
so N_t^c(2.3) is 3 to 4 (recalled beta_c(N_t = 3) = 2.18, beta_c(4) = 2.30). The time direction then
carries an ordered Polyakov loop, the twist in the (time, i) plane forces an interface of area about a x d (or a x c),
and p -> 1/2 as c, d grow. So (E17) can hold at a = 3 only through its constant C. In the window the deconfinement
length grows: beta_c(N_t) = 2.43, 2.51 at N_t = 6, 8 (recalled), so at beta = 2.6 the same holds for a up to about 9.
A proof of (E17) at order one must therefore contain a step that is false for a below N_t^c(beta). No bound on the
one-slice law of bounded sets, uniform in t >= 3, is such a step.

### Step 7. Whether and how the separation bears on the parity statement.

**Corollary QS-4 (by-product; PROVED with row 860's arithmetic).** For beta <= 2.5:
P_m(j_e >= 2) <= Sum_(j>=2) d_j^2 r_j(beta) r_j(5 beta)^4 <= 0.70746 x 0.3877^4 <= 0.0160, and
P_m(j_e half-integer, j_e >= 5/2) <= 0.16037 x (0.3877 x 0.6525)^4 <= 6.6e-4.
(READ H:122 for 0.70746, 0.16037 and the products r_j(12.5) <= r_2(12.5) <= 0.3877, U_5(12.5) <= 0.6525; QS replaces the
first power of r_j(5 beta) by the fourth.) Row 860's Corollary DS-1 had 0.275 and 0.041. GUIDE values at 2.3: 2e-5 and
below 6e-7. So QS cuts the proved exposure of the spin-5/2 filter by a factor 60, which strengthens row 860's (R2).

**The bearing, stated exactly.**
1. Lemma QS (PROVED) does not bear on the parity statement as an input. Its content is a bound on the one-slice law of
   sets of edges at mutual distance >= 2, relative to the all-zero event. The parity statement is the law of the
   wrapping 't Hooft surface (Proposition TL with R = cut). QS bounds no 't Hooft loop larger than one edge and does not
   see the Z_2-class of the half-integer cycle. It holds for every t >= 3, so by T3 it holds in a deconfined state.
2. C1 as a number (GUIDE: e_F = 0.267 for SU(2) at 2.3; at least 0.40 in every deconfined U(1), Q_8, 2T state measured)
   is the order-one separation the brief asks for, and it passes the U(1) and finite-group tests as a number. It fails T3:
   the deconfined N_t = 3 state of SU(2) at 2.3 has e_F = 0.263. So it is neither sufficient for (E17) nor necessary
   (SU(2) confines at every beta, and e_F rises with beta: 0.361 at 2.5, row 860). It cannot carry the parity statement.
3. What would. An input that can carry the parity statement at order one must pass four tests: fail for U(1) Coulomb,
   fail for frozen Q_8 and 2T, fail for SU(2) on (a, a, c, d) with a below N_t^c(beta), and say something about scales up
   to t. The first three are met by no statement about the one-slice law of bounded sets (Steps 3-4b). They are met by
   statements about the transfer operator over times comparable to the torus side on cube-like tori, which is the form
   of (SEED-FP) (READ FLN:117-121: the thermal sum of the cube of side ell at time ell/2). That is consistent with the
   lane's finish line and is not a new route.
4. How a local separation could still enter (ARGUED, a proposal). As the local estimate inside a shape-aware multiscale
   argument: at each block scale l <= t the blocked environment coefficient e_F(l) of the one-slice law is compared with
   a threshold; the finite-temperature state escapes because blocks larger than N_t do not exist there, and U(1) Coulomb
   escapes because its blocked e_F stays at least 0.40 (GUIDE at l = 1 only; the blocked values are not measured). This
   is a restatement of a seed-plus-continuation structure, not a proof step. OPEN.

### Step 7b. The U(1) side of the separation (ARGUED: one recalled theorem).

**Proposition SEP.** (a) PROVED (Lemma QS): for SU(2) at beta = 2.3, on every admissible torus and twist,
e_F = E_(nu_p)[x(U_p)] <= 0.5806. (b) ARGUED: for untwisted U(1) Wilson at every beta >= 6, on every torus with periods
>= 3, e_F(U(1)) >= (I_1(beta)/I_0(beta))^5 >= 0.6165. So the one-slice environment coefficient separates SU(2) at 2.3
from U(1) at every beta >= 6 (this contains the regime beta >= 2^14 of row 786), with margin 0.036.
*Argument for (b).* Ginibre's inequality for U(1) (recalled, not re-read: for ferromagnetic cosine weights the
expectation of a cosine of an integer combination of angles does not decrease when any coupling increases) lets us set
to zero every coupling except those of the five other faces of one 3-cube c containing p; p's coupling is already 0
in nu_p. In that measure the five face angles are independent with densities proportional to e^(beta cos), because the
map from the twelve link angles of c to its six face angles is a surjective homomorphism onto the subtorus
{Sum of the oriented face angles = 0}, so Haar measure pushes forward to Haar measure there (PROVED). The Bianchi identity
theta_p = -(Sum of the other five oriented face angles) mod 2 pi then gives E[cos theta_p] = (I_1/I_0(beta))^5.
Arithmetic (PROVED, same recurrence as Step 5, x = 6): R_3 <= U_3(6) <= 0.5744, R_2 >= 0.6351, R_1 <= 0.7682,
R_0 = I_1/I_0(6) >= 1/(1/3 + 0.7682) >= 0.9078, and 0.9078^5 >= 0.6165. R_0 increases with beta (READ Q:162, (b)).
**Limits of SEP (GUIDE).** At the matched kinetic eigenvalue (U(1) at beta 1.1) the U(1) value is 0.490, below the
SU(2) bound 0.581, so SEP does not reach the matched coupling; it reaches U(1) at beta >= 6 only. The GUIDE separation of
Step 4 (0.267 against at least 0.40 on the whole measured Coulomb branch) is not proved. Twisted U(1) is not covered
(Ginibre needs ferromagnetic signs). SEP fails T3 like every local input: it is not a confining input.

### Step 8. Summary.

No mass gap is proved here. Nothing in this file is checked by another model. (E17), the parity statement, (FQ) and
(SEED-FP) stay open. One correction to Step 3: C2 (group dimension) is not fully absorbed by matching the kinetic
eigenvalue at order one. At matched r_F the worst-case link response 1 - r_F(5 beta) is 0.127 (SU(2), 2.3) against
0.096 (U(1), 1.1; Bessel decimals), and the measured e_F is 0.267 against 0.490 (GUIDE). It is still a statement of the
same form for both groups, so it separates only as a number.

**PROVED (by hand, Claude Opus 5.5, not checked).**
1. Lemma QS (quadruple suppression): the four links of a plaquette meet only in it; under nu_p they are conditionally
   independent; |E_(nu_p)[chi_j(U_p)]|/d_j <= E_(nu_p)[Prod_i r_j(beta rho_i)] <= r_j(5 beta)^4, every torus with periods
   >= 3, every twist, every t >= 3. Corollaries: rho_j <= rho_0 d_j^2 r_j(beta) r_j(5 beta)^4 (QS-1); a product form on
   sets of edges at mutual distance >= 2 (QS-2); P(j_e >= 2) <= 0.0160 and P(odd, j_e >= 5/2) <= 6.6e-4 for beta <= 2.5
   (QS-4; row 860 had 0.275 and 0.041).
2. Constants: a seven-step continued-fraction chain from the Bessel recurrence and Lemma 3.1 (d) of row 843 gives
   r_(1/2)(11.5) <= 0.8729, so e_(1/2) <= 0.5806 at beta = 2.3 (row 860: 0.873); 0.6077 at 2.5; 0.6199 at 2.6.
   At 2.3 also rho_(1/2)/rho_0 <= 1.115 and P(odd)/rho_0 <= 1.177 (row 860's method: 1.676, 2.16; frozen 1.917, 2.71).
3. Proposition TL: for every set R of time-0 edges, E[(-1)^(N_h(R))] = E_mu[exp(-2 beta Sum_R x_p)] = Z(flip R)/Z. The
   parity of a bounded set is a 't Hooft loop; the parity statement is the wrapping 't Hooft surface.
4. The exact Haar moments of C2 (SU(2) C_n/4^n, U(1) binom(2n,n)/4^n, Q_8 1/4, 2T (2 + 16 4^-n)/24), the twisted flat
   connections of C4 (none for U(1); i, j in Q_8), and the cube pushforward step of SEP (b).

**READ.** Row 860 whole (H:1-263): Lemma OS, Lemma DS, P1-P3, the GUIDE table, (R1)-(R3), OPEN. Row 843's Lemmas 3.1-3.3
(Q:155-182). FIN rows 786, 838, 839, 845, 866 (FIN:863, 915, 916, 922, 943). (SEED-FP) (FLN:110-160).

**ARGUED.** The test verdicts of Step 3 (continuity-type candidates fail the U(1) test as structures, centre-type ones
fail the Q_8 / 2T test). The consequence of Finding FT: inputs on the one-slice law of bounded sets, uniform in t >= 3,
cannot force (E17) (rests on GUIDE at beta 2.3 and on Borgs and Seiler 1983 at large beta, recalled). T3 for the
admissible shapes (3, 3, c, d). Proposition SEP (b) for U(1) at beta >= 6 (rests on Ginibre's inequality, recalled).
The bearing (Step 7): QS and C1 do not bear on the parity statement as inputs; a carrying input must be of thermal-sum
type on cube-like tori, which is the form of (SEED-FP).

**GUIDE (decides nothing).** Step 4 (8^4, untwisted, one seed per point): e_F = 0.267 for SU(2) at 2.3; U(1) Coulomb
0.401 to 0.745 (beta 1.02 to 2.0); frozen 2T 0.93, frozen Q_8 0.96; confined or disordered states 0.005 to 0.22.
Step 4b: deconfined SU(2) at 2.3 (N_t = 3, Polyakov loop 0.345) has e_F 0.263 and P(odd) 0.325, against 0.267 and 0.328
at N_t = 8. Recalled numbers: beta_c(N_t) = 2.18, 2.30, 2.43, 2.51 for N_t = 3, 4, 6, 8; U(1) beta_c about 1.01;
freezing of Q_8 and 2T near 1.15 and 2.15 (row 838, Hartung et al.).

**OPEN.**
- (E17) = the parity statement (row 866 attacks it; not done here).
- A proved typical-value bound e_(1/2) <= 0.39 at beta = 2.3, below the measured U(1) Coulomb infimum. QS reaches 0.581;
  its typical value is 0.449 (GUIDE); the rest is the misalignment of the four smeared links (0.59 on average).
- A proved lower bound on e_F for U(1) between beta_c and 6, and for frozen 2T at 2.3 (both GUIDE only).
- T3 at beta = 2.3 as a theorem (deconfinement at N_t = 3 is GUIDE here).
- A shape-sensitive separating input that passes all four tests (U(1) Coulomb, frozen Q_8 / 2T, short-period SU(2),
  scales up to t). Proposal only: blocked environment coefficients e_F(l) at scales l <= t inside a seed-plus-continuation
  argument (Step 7, item 4); no blocked value is measured.

**Answers to the brief, in order.**
- Candidates, stated exactly and tested (Step 3): C1 typical-value environment bound, C2 Haar moments, C3 simple
  connectivity, C4 twisted flat connections, C5 centre Z_2, C6 Euler-characteristic weight d^chi. No structure passes both
  the U(1) and the Q_8 / 2T tests. C1 passes both as a number (GUIDE, margin 0.13 at beta 2.3).
- Strongest separation proved at beta about 2.3: Lemma QS, e_(1/2) <= 0.5806 (0.6077 at 2.5); it uses continuity (fails
  for Q_8 and 2T, whose QS constant is >= 0.95) and separates SU(2) at 2.3 from U(1) at beta >= 6 (SEP, with Ginibre
  recalled). It does not reach U(1) at matched kinetic eigenvalue (U(1) value 0.490 < 0.581, GUIDE).
- Bearing on the parity statement: none as an input. A new fact test T3 shows why: the deconfined N_t = 3 state of SU(2)
  at 2.3 has the same one-slice local law within 1.5 percent, and there p -> 1/2. Any input that carries (E17) must fail
  at short periods; statements about the one-slice law of bounded sets cannot.

**Credits.** Row 860 (Claude Fable 5.2): Lemma OS, Lemma DS, P1-P3, the estimator identity, the arithmetic of DS-1.
Row 843 (Claude Opus 5.5): Lemmas 3.1-3.3. Row 838 (Claude Opus 5.5) and Hartung et al.: the freezing couplings. Ethan
Sussman and Levent Alpoge, with Claude and Codex as authors of their text: the first-passage frame of (SEED-FP) as read
through FLN; Balaban: the effective-action estimates behind that frame (not used in any proof here). Ginibre; Borgs and
Seiler: recalled theorems, not re-read. Codex gpt-6-astra max: the definitions (E1)-(E18) as read through row 860.

**Delivery.** Only this file was written. The two GUIDE scripts are inside it (GUIDE867, GUIDE867b) and ran from it;
all runs under 100 MB, under 40 s each, four to six in parallel at nice 10. No repository file, registry, PR or post was
touched. No subagent was used. No download was made.

RESULT: PARTIAL, by Claude Opus 5.5 (max effort), not checked — the order-one separation exists as a local number but cannot carry the parity statement. GUIDE: the one-slice environment coefficient of spin 1/2 is 0.267 for SU(2) at beta 2.3 and at least 0.40 in every deconfined U(1) Coulomb, frozen Q_8 and frozen 2T state measured (8^4). PROVED: Lemma QS (the four links of a plaquette are conditionally independent once it is deleted), giving e_(1/2) <= r_(1/2)(5 beta)^4 <= 0.5806 at beta 2.3 (row 860: 0.873), 0.6077 at 2.5, with a product form, P(spin >= 2) <= 0.016 and filter exposure <= 6.6e-4 for beta <= 2.5; Proposition TL (the parity of any edge set is a 't Hooft loop); ARGUED with Ginibre recalled: U(1) at beta >= 6 has e_F >= 0.6165, so QS separates SU(2) at 2.3 from U(1) there, but not at matched kinetic eigenvalue (U(1) 0.490, GUIDE). New fact test T3 (GUIDE, Borgs-Seiler recalled): the deconfined N_t = 3 state of SU(2) at 2.3 has the same one-slice local law within 1.5 percent (e_F 0.263, P(odd) 0.325, Polyakov loop 0.345), so no bound on the one-slice law of bounded sets that is uniform in t can force (E17); a carrying input must fail at short periods, as (SEED-FP) does by its cube shape. OPEN: (E17); a proved e_(1/2) <= 0.39; U(1) and 2T lower bounds at order one; a shape-sensitive separating input.
