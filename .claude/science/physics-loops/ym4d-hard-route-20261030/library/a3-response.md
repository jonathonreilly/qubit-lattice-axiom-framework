lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T00:15Z

# A3: uniform multiscale background response (queue row 77)

Pinned at commit `7cd8b4f0f`, branch `claude/ym4d-hard-route`. Author: Anthropic
claude-opus-5-5, effort max, Mac mini worker, 2026-11-02. Same-model work: not
gated, not an audit, no status.

Sources read: outline `YM4_sketch_500.tex` at `31a47c543775` (SHA-256 matches
`library/sa-2.8.md`), (1b) l. 9583-9800 and A3 l. 3864-3896; Dimock arXiv
1712.10029 (source, Section 3, l. 2004-3160 of `QEDjmp.tex`, not committed);
`library/lit-large-field.md` 3, `sa-2.8.md` 9, `rel-phi-c.md`,
`seam-nonlinear-c.md` 4, `fibre-propagator.md`, `fd-local.md` 5, 8,
`curl-poincare-exterior.md` Lemma 1, `lattice_gehring_hls.md`.

Status: in progress; sections are written as they close.

## 0. What Dimock 3.7 actually contains (finding, before any port)

Dimock's Section 3.7 is a summary, not a proof. It opens "We quote some results
... from Balaban [Bal84a], [Bal84b], [Bal85b]". The three load-bearing steps are
quoted: the local inverse bounds for G_{k,Omega}(box) ("the global results of
[Bal84a]"), the case of a box crossing a seam ("requires some rather extensive
modifications. See [Bal84b] for the full treatment"), and the commutator bound
(day0) ("One shows that [Bal84b]"); the local inverses N_{k,Omega}(box) likewise
("see Balaban [Bal84b] for details"). So porting 3.7 to d = 4 would port
citations, not a proof. In the source fetched (the version of 2020-03-03) the
kernel bounds that `lit-large-field.md` calls (301)-(303) are labelled
`standard3`, `standard3.5`, `standard4` (equations 318-320 by my count).

Instead, Section 2 below proves the flat linear statement directly, by a route
that needs no random walk: a local curl-Poincare inequality on boxes, a patching
of local gauges normalised by pillar means, an explicit local right inverse of
the multiscale average, and a hole-filling (Widman) iteration. The operators,
the multiscale geometry and the statement are Balaban's (CMP 95, 96), in the
form Dimock writes (Lemma 14 and (292) of the source); the use of a
block-diagonal gauge term follows `library/fibre-propagator.md`.

## 1. Setting and the flat statement

**Units and lattice.** Fine units: the fine lattice is a torus of Z^4 with unit
spacing (multiply lengths by eta = L^-k for the outline's level-k units; the
energy below is dimensionless in d = 4 and does not change). L odd, L >= 3,
s_j := L^j. Level-j sites are s_j Z^4, the level-j block of a level-j site y is
B^j(y) := y + {-m_j, ..., m_j}^4, m_j := (s_j - 1)/2. Blocks nest.

**Sequence (outline (1b)(i), with Balaban's averages).** Omega_0 ⊃ ... ⊃ Omega_k,
Omega_j a union of level-j blocks, Omega_(k+1) = empty, separated:
dist_inf(Omega_j^c, Omega_(j+1)) > rho s_j with rho >= 3L. (The outline's cubes of
side M xi_j and gap R_1 M are a special case.) Layer j := Omega_j \ Omega_(j+1);
tops of level j = level-j sites in layer j; their blocks are the *pillars*,
which partition Omega_0; xi_P := s_j is the side of a pillar P of layer j
(layer-0 pillars are single sites). Gamma_j := level-j bonds with both ends in
Omega_0, an end in Omega_j and none in Omega_(j+1); **B** := union of the Gamma_j
(no inward bonds, as in the outline). For c = (y, y + s_j e_mu) in Gamma_j,

    q_c(A) := s_j^-4 sum_(x in B^j(y)) A(Gamma_(x, x + s_j e_mu)) = sum_b rho_c(b) A(b),

the straight path average (Dimock's Q_k, (moonshine); the outline's straightened
average Q^st at V_0 = 1, see 3.1). Here rho_c(b) = s_j^-4 tau(b_mu - y_mu) on
direction-mu bonds b with transverse position in y_perp + {-m_j..m_j}^3, with the
tent tau(u) = s_j - |u - m_j| for -m_j <= u <= 3 m_j, peaked at the face bond
(u = m_j). So ||rho_c||_2^2 <= (2/3) s_j^-2 and the support of rho_c lies in the
*double block* D(c) := B^j(c_-) u B^j(c_+). At level 0, q_c(A) = A(c).

**Problem.** E(A) := sum_(p ⊂ Omega_0) |dA(p)|^2, A real on the bonds of Omega_0
(one colour component: at V_0 = 1 the linearisation of SU(2) Wilson action and
averages is three copies of this). Datum B on **B**; A_B := a minimiser of E on
{q(A) = B}. *Restricted gauges* (Balaban): lambda with Av_P lambda = 0 on every
pillar P. Then q_c(d lambda) = Av_(B(c_+)) lambda - Av_(B(c_-)) lambda = 0 for every
c in **B**, because the block of an outer end is a union of pillars of the next
finer layer. *Distance*: d_B(x, x') := inf over paths of sum_j s_j^-1 (fine length
in layer j), the outline's d_**B** in fine units; it is 1/s_j-Lipschitz along
a fine bond of layer j.

**Theorem FL (flat multiscale response).** There are m(L) > 0 and C(L), free
of k, of the torus, of the regions, of the support S of B and of B, such that,
with psi(x) := d_B(x, union_(c in S) D(c)):

(a) (curvature) for every t >= 0,
    sum_(p : psi(p) >= t) |dA_B(p)|^2 <= C(L) e^(-2 m t) ||B||^2,  ||B||^2 := sum_c |B(c)|^2;

(b) (potential) there is a restricted gauge in which A~ := A_B - d lambda obeys,
    for every pillar P,
    xi_P^-2 ||A~||^2_(L^2(P)) <= C(L) e^(-2 m psi(P)) ||B||^2.

dA_B is unique. Inside one layer every constant is absolute; only the seam
transitions bring in L (Lemma P, case (c)). In the outline's units (a) and (b)
say: the response to a unit datum e at a bond c has, over each top y, energy in
its pillar at most C e^(-2m d_B(y, y_c)) |e|^2 and potential in L^2 of the
pillar, in local units, of the same size. This is Theorem 4 of (1b) at
V_0 = 1, B = 0, in local L^2 form; the pointwise form needs in addition the
single-scale local regularity of Section 5 (LR), which has no depth in it.
