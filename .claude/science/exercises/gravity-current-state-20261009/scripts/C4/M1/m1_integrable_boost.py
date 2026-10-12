"""M1 (3): exact Pauli-string algebra on the infinite chain for translation-invariant local densities.
K = sum_n n h_n (first moment of the energy density), P = i[H,K] (total energy current; the Tetel'man/
Sogo-Wadati/Thacker 'boost operator' of integrable chains is exactly this K).
Checks, as exact operator identities (coefficients are exact rationals up to float printing):
  C1: [H,P] = 0 ?   (conservation of the energy current; true for XXZ and free chains, false for non-integrable)
  C3: i[K,P] = -beta H ?  (closure); residual = the part of i[K,P] outside span{h, 1}.
"""
import numpy as np
from collections import defaultdict
PM = {('I','I'):(1,'I'),('I','X'):(1,'X'),('I','Y'):(1,'Y'),('I','Z'):(1,'Z'),
      ('X','I'):(1,'X'),('Y','I'):(1,'Y'),('Z','I'):(1,'Z'),
      ('X','X'):(1,'I'),('Y','Y'):(1,'I'),('Z','Z'):(1,'I'),
      ('X','Y'):(1j,'Z'),('Y','X'):(-1j,'Z'),('Y','Z'):(1j,'X'),('Z','Y'):(-1j,'X'),
      ('Z','X'):(1j,'Y'),('X','Z'):(-1j,'Y')}
def norm(start, w):
    w2 = w.lstrip('I'); start += len(w) - len(w2); w2 = w2.rstrip('I')
    if w2 == '': return 0, ''
    return start, w2
def mul(sa, wa, sb, wb):
    lo = min(sa, sb); hi = max(sa+len(wa), sb+len(wb))
    ph = 1; out = []
    for x in range(lo, hi):
        a = wa[x-sa] if 0 <= x-sa < len(wa) else 'I'
        b = wb[x-sb] if 0 <= x-sb < len(wb) else 'I'
        p, c = PM[(a,b)]; ph *= p; out.append(c)
    s, w = norm(lo, ''.join(out))
    return ph, s, w
def comm_terms(A, B, shiftA):
    """terms of i[A placed at shiftA, B placed at 0]; A,B: dict word->coeff (canonical, start 0)"""
    out = defaultdict(complex)
    for (sa0, wa), ca in A.items():
        for (sb0, wb), cb in B.items():
            sa = sa0 + shiftA
            if sa + len(wa) <= sb0 or sb0 + len(wb) <= sa:  # disjoint supports commute
                continue
            p1, s1, w1 = mul(sa, wa, sb0, wb)
            p2, s2, w2 = mul(sb0, wb, sa, wa)
            assert (s1, w1) == (s2, w2)
            c = 1j*(p1 - p2)*ca*cb
            if abs(c) > 1e-14: out[(s1, w1)] += c
    return out
def tsum_comm(A, B):
    """density of i[sum A, sum B] (canonical words)"""
    out = defaultdict(complex)
    LA = max(s+len(w) for (s,w) in A)+1; LB = max(s+len(w) for (s,w) in B)+1
    for d in range(-LA-2, LB+3):
        for (s, w), c in comm_terms(A, B, d).items(): out[(0, w)] += c
    return {k: c for k, c in out.items() if abs(c) > 1e-12}
def moment_comm(h, q):
    """i[sum_n n h_n, sum_m q_m] as a translation-invariant density; requires i[H,Q]=0.
       Returns (density, conservation_defect_norm)."""
    alpha = defaultdict(lambda: defaultdict(complex)); e = defaultdict(complex)
    Lh = max(s+len(w) for (s,w) in h)+1; Lq = max(s+len(w) for (s,w) in q)+1
    for d in range(-Lh-2, Lq+3):
        for (s, w), c in comm_terms(h, q, d).items():
            alpha[w][s] += c      # c_0 = sum_d i[h_d, q_0] : word w at absolute start s
            e[w] += d*c           # e_0 = sum_d d i[h_d, q_0]
    out = defaultdict(complex); cons = 0.0
    for w, dct in alpha.items():
        tot = sum(dct.values()); cons += abs(tot)**2
        out[(0, w)] += -sum(s*c for s, c in dct.items())
    for w, c in e.items(): out[(0, w)] += c
    return {k: c for k, c in out.items() if abs(c) > 1e-12}, np.sqrt(cons)
def hs(A): return np.sqrt(sum(abs(c)**2 for c in A.values()))
def canon(A):
    out = defaultdict(complex)
    for (s0, w), c in A.items(): out[w] += c
    return out
def fit_beta(D, h):
    # minimise || D + beta h || over non-identity words
    D = canon(D); h = canon(h)
    hv = {w: c for w, c in h.items() if w != ''}
    num = -sum((np.conj(hv[w])*D.get(w, 0)).real for w in hv); den = sum(abs(c)**2 for c in hv.values())
    beta = num/den
    R = defaultdict(complex)
    for w, c in D.items():
        if w != '': R[w] += c
    for w, c in hv.items(): R[w] += beta*c
    return beta, hs(R)/hs({w: c for w, c in D.items() if w != ''}), R
def run(name, h):
    P = {k: -c for k, c in moment_comm(h, h)[0].items()}          # P = i[H,K] = -i[K,H]
    HP = tsum_comm(h, P)                                            # i[H,P] density
    D, cons = moment_comm(h, P)
    beta, rel, R = fit_beta(D, h)
    print(f"{name}:")
    print(f"   energy current P: {len(P)} words, max range {max(len(w) for (_, w) in P)};  |i[H,P]|_HS = {hs(HP):.3e}  (C1: 0 iff current conserved)")
    if hs(HP) < 1e-10:
        top = sorted(R.items(), key=lambda kv: -abs(kv[1]))[:4]
        print(f"   i[K,P] = -beta H + R:  best beta = {beta:.6f};  |R|/|i[K,P]| = {rel:.4f};  max range of R = {max((len(w) for w in R if abs(R[w])>1e-12), default=0)}")
        print(f"   largest residual words: " + ", ".join(f"{w}:{c.real:+.4f}" for w, c in top))
    else:
        print("   current not conserved: the Poincare relation [H,P]=0 already fails (C1); C3 bracket not formed")
def xxz(J=1.0, Delta=1.0, J2=0.0):
    h = defaultdict(complex)
    h[(0,'XX')] += -J/4; h[(0,'YY')] += -J/4; h[(0,'ZZ')] += -J*Delta/4
    if J2: h[(0,'XIX')] += -J2/4; h[(0,'YIY')] += -J2/4; h[(0,'ZIZ')] += -J2*Delta/4
    return dict(h)
def tfim(g, sym=True):
    if sym: return {(0,'ZZ'): -1.0, (0,'X'): -g/2, (1,'X'): -g/2}
    return {(0,'ZZ'): -1.0, (0,'X'): -g}
if __name__ == "__main__":
    print(__doc__)
    run("XX (free fermions, Delta=0)", xxz(1, 0.0))
    run("XXZ Delta=0.5 (integrable, gapless)", xxz(1, 0.5))
    run("XXX Delta=1", xxz(1, 1.0))
    run("XXZ Delta=2 (integrable, gapped)", xxz(1, 2.0))
    run("TFIM g=1, on-site field anchored at n (a non-symmetric density)", tfim(1.0, sym=False))
    run("TFIM g=1, symmetric bond density (critical Ising, free Majorana; IR CFT)", tfim(1.0))
    run("TFIM g=0.5, symmetric bond density (gapped free Majorana)", tfim(0.5))
    run("XXZ Delta=0.5 + NNN J2=0.3 (non-integrable)", xxz(1, 0.5, 0.3))
    # one-particle check for TFIM: eps(k)=2 sqrt(1+g^2-2g cos k) -> u''=4 g cos k : not constant

if __name__ == "__main__":
    print()
    print("Is the residual R of i[K,P] itself conserved (the next charge of the hierarchy)?")
    for name, h in [("XXZ Delta=0.5", xxz(1, 0.5)), ("XXZ Delta=2", xxz(1, 2.0)), ("TFIM g=1 sym", tfim(1.0)), ("TFIM g=0.5 sym", tfim(0.5))]:
        P = {k: -c for k, c in moment_comm(h, h)[0].items()}
        D, _ = moment_comm(h, P)
        print(f"   {name}: |i[H, i[K,P]]|_HS = {hs(tsum_comm(h, D)):.2e}  (0 => i[K,P] is a conserved charge, range {max(len(w) for (_, w) in D)})")
