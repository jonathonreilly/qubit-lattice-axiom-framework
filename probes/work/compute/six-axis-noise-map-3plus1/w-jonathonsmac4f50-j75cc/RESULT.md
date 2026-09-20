six-axis-noise-map-3plus1, independent run 1 of 2
worker w-jonathonsmac4f50-j75cc (claude-opus-5), unit C-six-axis-noise-map-3plus1-a1

Block 12's exact noise map with FOUR recorded predecessors (the 3+1 backward neighbourhood {0, e1, e2, e3}).
The six-axis record at a site takes axis a with probability proportional to prod_j W(a, s_j), with
W(a,s) = p when a = s, q when a = -s, r when a is orthogonal to s.
All laws below are exact rational functions; nothing here is sampled.

(1) THE PATTERNS UP TO THE CUBE GROUP
  the cube group acting on the six axes has 48 elements
  126 multisets of four predecessors fall into 10 orbits
  pattern 4 (unanimous): representative [(1, 0, 0), (1, 0, 0), (1, 0, 0), (1, 0, 0)], orbit size 6
    law: P((1, 0, 0)) = p**4/(p**4 + q**4 + 4*r**4), P((-1, 0, 0)) = q**4/(p**4 + q**4 + 4*r**4), P((0, 1, 0)) = r**4/(p**4 + q**4 + 4*r**4), P((0, -1, 0)) = r**4/(p**4 + q**4 + 4*r**4), P((0, 0, 1)) = r**4/(p**4 + q**4 + 4*r**4), P((0, 0, -1)) = r**4/(p**4 + q**4 + 4*r**4)
  pattern 3-1 (opposite): representative [(1, 0, 0), (1, 0, 0), (1, 0, 0), (-1, 0, 0)], orbit size 6
    law: P((1, 0, 0)) = p**3*q/(p**3*q + p*q**3 + 4*r**4), P((-1, 0, 0)) = p*q**3/(p**3*q + p*q**3 + 4*r**4), P((0, 1, 0)) = r**4/(p**3*q + p*q**3 + 4*r**4), P((0, -1, 0)) = r**4/(p**3*q + p*q**3 + 4*r**4), P((0, 0, 1)) = r**4/(p**3*q + p*q**3 + 4*r**4), P((0, 0, -1)) = r**4/(p**3*q + p*q**3 + 4*r**4)
  pattern 3-1 (orthogonal): representative [(1, 0, 0), (1, 0, 0), (1, 0, 0), (0, 1, 0)], orbit size 24
    law: P((1, 0, 0)) = p**3/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3), P((-1, 0, 0)) = q**3/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3), P((0, 1, 0)) = p*r**2/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3), P((0, -1, 0)) = q*r**2/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3), P((0, 0, 1)) = r**3/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3), P((0, 0, -1)) = r**3/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3)
  pattern 2-2 (opposite): representative [(1, 0, 0), (1, 0, 0), (-1, 0, 0), (-1, 0, 0)], orbit size 3
    law: P((1, 0, 0)) = p**2*q**2/(2*(p**2*q**2 + 2*r**4)), P((-1, 0, 0)) = p**2*q**2/(2*(p**2*q**2 + 2*r**4)), P((0, 1, 0)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, -1, 0)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, 0, 1)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, 0, -1)) = r**4/(2*(p**2*q**2 + 2*r**4))
  pattern 2-1-1 (opposite, orthogonal): representative [(1, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0)], orbit size 24
    law: P((1, 0, 0)) = p**2*q/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3), P((-1, 0, 0)) = p*q**2/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3), P((0, 1, 0)) = p*r**2/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3), P((0, -1, 0)) = q*r**2/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3), P((0, 0, 1)) = r**3/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3), P((0, 0, -1)) = r**3/(p**2*q + p*q**2 + p*r**2 + q*r**2 + 2*r**3)
  pattern 2-2 (orthogonal): representative [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 0)], orbit size 12
    law: P((1, 0, 0)) = p**2/(2*(p**2 + q**2 + r**2)), P((-1, 0, 0)) = q**2/(2*(p**2 + q**2 + r**2)), P((0, 1, 0)) = p**2/(2*(p**2 + q**2 + r**2)), P((0, -1, 0)) = q**2/(2*(p**2 + q**2 + r**2)), P((0, 0, 1)) = r**2/(2*(p**2 + q**2 + r**2)), P((0, 0, -1)) = r**2/(2*(p**2 + q**2 + r**2))
  pattern 2-1-1 (opposite, orthogonal): representative [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0)], orbit size 12
    law: P((1, 0, 0)) = p**2/(p**2 + 2*p*q + q**2 + 2*r**2), P((-1, 0, 0)) = q**2/(p**2 + 2*p*q + q**2 + 2*r**2), P((0, 1, 0)) = p*q/(p**2 + 2*p*q + q**2 + 2*r**2), P((0, -1, 0)) = p*q/(p**2 + 2*p*q + q**2 + 2*r**2), P((0, 0, 1)) = r**2/(p**2 + 2*p*q + q**2 + 2*r**2), P((0, 0, -1)) = r**2/(p**2 + 2*p*q + q**2 + 2*r**2)
  pattern 2-1-1 (orthogonal): representative [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 0, 1)], orbit size 24
    law: P((1, 0, 0)) = p**2/(p**2 + 2*p*r + q**2 + 2*q*r), P((-1, 0, 0)) = q**2/(p**2 + 2*p*r + q**2 + 2*q*r), P((0, 1, 0)) = p*r/(p**2 + 2*p*r + q**2 + 2*q*r), P((0, -1, 0)) = q*r/(p**2 + 2*p*r + q**2 + 2*q*r), P((0, 0, 1)) = p*r/(p**2 + 2*p*r + q**2 + 2*q*r), P((0, 0, -1)) = q*r/(p**2 + 2*p*r + q**2 + 2*q*r)
  pattern 1-1-1-1 (opposite, orthogonal): representative [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0)], orbit size 3
    law: P((1, 0, 0)) = p*q/(2*(2*p*q + r**2)), P((-1, 0, 0)) = p*q/(2*(2*p*q + r**2)), P((0, 1, 0)) = p*q/(2*(2*p*q + r**2)), P((0, -1, 0)) = p*q/(2*(2*p*q + r**2)), P((0, 0, 1)) = r**2/(2*(2*p*q + r**2)), P((0, 0, -1)) = r**2/(2*(2*p*q + r**2))
  pattern 1-1-1-1 (opposite, orthogonal): representative [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1)], orbit size 12
    law: P((1, 0, 0)) = p*q/(2*(p*q + p*r + q*r)), P((-1, 0, 0)) = p*q/(2*(p*q + p*r + q*r)), P((0, 1, 0)) = p*r/(2*(p*q + p*r + q*r)), P((0, -1, 0)) = q*r/(2*(p*q + p*r + q*r)), P((0, 0, 1)) = p*r/(2*(p*q + p*r + q*r)), P((0, 0, -1)) = q*r/(2*(p*q + p*r + q*r))
  every multiset in an orbit gives its representative's law relabelled by the group element: True

(2) BLOCK 30's TWO DOMINATION PARAMETERS
  leaving a unanimous neighbourhood: 1 - P(same axis) = (q**4 + 4*r**4)/(p**4 + q**4 + 4*r**4) (factored: (q**2 - 2*q*r + 2*r**2)*(q**2 + 2*q*r + 2*r**2)/(p**4 + q**4 + 4*r**4))
  equals the task's (q^4 + 4 r^4)/(p^4 + q^4 + 4 r^4): True
  3-1 with the odd one opposite: P(minority) = p*q**3/(p**3*q + p*q**3 + 4*r**4)
  3-1 with the odd one orthogonal: P(minority) = p*r**2/(p**3 + p*r**2 + q**3 + q*r**2 + 2*r**3)
  on (p,1,2): leave = 65/(p**4 + 65)
  on (p,1,2): minority opposite = p/(p**3 + p + 64), minority orthogonal = 4*p/(p**3 + 4*p + 21)
  on (e^b, e^-b, 1): leave = (4*exp(4*b) + 1)/(exp(8*b) + 4*exp(4*b) + 1)
  on (e^b, e^-b, 1): minority opposite = 1/((exp(2*b) + 4)*exp(2*b) + 1), minority orthogonal = exp(4*b)/((exp(3*b) + exp(b) + 2)*exp(3*b) + exp(2*b) + 1)
  numerically on (p,1,2): p | leave | minority opposite | minority orthogonal
    p=    1: 0.984848  1.515e-02  1.538e-01
    p=    2: 0.802469  2.703e-02  2.162e-01
    p=    4: 0.202492  3.030e-02  1.584e-01
    p=    8: 0.015621  1.370e-02  5.664e-02
    p=   16: 0.000991  3.831e-03  1.531e-02
    p=   84: 0.000001  1.417e-04  5.666e-04
    p= 4165: 0.000000  5.765e-08  2.306e-07
  numerically on (e^b, e^-b, 1): b | leave | minority opposite | minority orthogonal
    b=0.5: 0.358833  5.192e-02  1.840e-01
    b=1: 0.068553  1.174e-02  1.078e-01
    b=2: 0.001340  3.125e-04  1.789e-02
    b=3: 0.000025  6.084e-06  2.472e-03
    b=5: 0.000000  2.061e-09  4.540e-05

(3) THE TIES
  the 2-2 patterns, which need an even number of predecessors and so do not occur with three:
    [(1, 0, 0), (1, 0, 0), (-1, 0, 0), (-1, 0, 0)] (opposite pair): P((1, 0, 0)) = p**2*q**2/(2*(p**2*q**2 + 2*r**4)), P((-1, 0, 0)) = p**2*q**2/(2*(p**2*q**2 + 2*r**4)), P((0, 1, 0)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, -1, 0)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, 0, 1)) = r**4/(2*(p**2*q**2 + 2*r**4)), P((0, 0, -1)) = r**4/(2*(p**2*q**2 + 2*r**4))
      the two carried axes are exactly tied: True, at probability p**2*q**2/(2*(p**2*q**2 + 2*r**4)) each
    [(1, 0, 0), (1, 0, 0), (0, 1, 0), (0, 1, 0)] (orthogonal pair): P((1, 0, 0)) = p**2/(2*(p**2 + q**2 + r**2)), P((-1, 0, 0)) = q**2/(2*(p**2 + q**2 + r**2)), P((0, 1, 0)) = p**2/(2*(p**2 + q**2 + r**2)), P((0, -1, 0)) = q**2/(2*(p**2 + q**2 + r**2)), P((0, 0, 1)) = r**2/(2*(p**2 + q**2 + r**2)), P((0, 0, -1)) = r**2/(2*(p**2 + q**2 + r**2))
      the two carried axes are exactly tied: True, at probability p**2/(2*(p**2 + q**2 + r**2)) each
  with three predecessors the patterns are 3, 2-1 and 1-1-1: no two axes can carry two predecessors each,
  so the strict majority of a 2-1 always has the larger weight when p > q, r. For comparison:
    three predecessors [(1, 0, 0), (1, 0, 0), (1, 0, 0)]: P((1, 0, 0)) = p**3/(p**3 + q**3 + 4*r**3), P((-1, 0, 0)) = q**3/(p**3 + q**3 + 4*r**3), P((0, 1, 0)) = r**3/(p**3 + q**3 + 4*r**3), P((0, -1, 0)) = r**3/(p**3 + q**3 + 4*r**3), P((0, 0, 1)) = r**3/(p**3 + q**3 + 4*r**3), P((0, 0, -1)) = r**3/(p**3 + q**3 + 4*r**3)
    three predecessors [(1, 0, 0), (1, 0, 0), (-1, 0, 0)]: P((1, 0, 0)) = p**2*q/(p**2*q + p*q**2 + 4*r**3), P((-1, 0, 0)) = p*q**2/(p**2*q + p*q**2 + 4*r**3), P((0, 1, 0)) = r**3/(p**2*q + p*q**2 + 4*r**3), P((0, -1, 0)) = r**3/(p**2*q + p*q**2 + 4*r**3), P((0, 0, 1)) = r**3/(p**2*q + p*q**2 + 4*r**3), P((0, 0, -1)) = r**3/(p**2*q + p*q**2 + 4*r**3)
    three predecessors [(1, 0, 0), (1, 0, 0), (0, 1, 0)]: P((1, 0, 0)) = p**2/(p**2 + p*r + q**2 + q*r + 2*r**2), P((-1, 0, 0)) = q**2/(p**2 + p*r + q**2 + q*r + 2*r**2), P((0, 1, 0)) = p*r/(p**2 + p*r + q**2 + q*r + 2*r**2), P((0, -1, 0)) = q*r/(p**2 + p*r + q**2 + q*r + 2*r**2), P((0, 0, 1)) = r**2/(p**2 + p*r + q**2 + q*r + 2*r**2), P((0, 0, -1)) = r**2/(p**2 + p*r + q**2 + q*r + 2*r**2)
    three predecessors [(1, 0, 0), (0, 1, 0), (0, 0, 1)]: P((1, 0, 0)) = p/(3*(p + q)), P((-1, 0, 0)) = q/(3*(p + q)), P((0, 1, 0)) = p/(3*(p + q)), P((0, -1, 0)) = q/(3*(p + q)), P((0, 0, 1)) = p/(3*(p + q)), P((0, 0, -1)) = q/(3*(p + q))

(4) BRUTE-FORCE CHECK
  brute-force check: for three random rational (p,q,r), every orbit's law recomputed by direct
  enumeration of the six numerators, compared with the symbolic formula evaluated there
  (p,q,r) = (7, 26, 5/9): worst deviation over all 10 orbits 0; leaving a unanimous neighbourhood 2998222036/3013974997 equals (q^4+4r^4)/(p^4+q^4+4r^4): True
  (p,q,r) = (7/6, 38, 33/4): worst deviation over all 10 orbits 0; leaving a unanimous neighbourhood 10905404625/10905414229 equals (q^4+4r^4)/(p^4+q^4+4r^4): True
  (p,q,r) = (3/2, 4, 5/4): worst deviation over all 10 orbits 0; leaving a unanimous neighbourhood 17009/17333 equals (q^4+4r^4)/(p^4+q^4+4r^4): True
  all 180 probabilities agreed exactly with the symbolic laws: True

(5) READING
  The four-predecessor map has ten orbits where three predecessors have four. The unanimous law is unchanged in
  form, p^4 : q^4 : r^4 : r^4 : r^4 : r^4, so leaving a unanimous neighbourhood costs (q^4 + 4r^4)/(p^4 + q^4 + 4r^4)
  exactly as the task states - 1.3e-06 at (84,1,2) and 2.2e-13 at (4165,1,2), against the three-predecessor
  (q^3 + 4r^3)/(p^3 + q^3 + 4r^3).
  The minority of a 3-1 neighbourhood is followed with probability p q^3/(p^3 q + p q^3 + 4 r^4) when the odd
  predecessor is opposite and p r^2/(p^3 + p r^2 + q^3 + q r^2 + 2 r^3) when it is orthogonal; the orthogonal case
  is the larger of the two at every (p,1,2) and (e^b, e^-b, 1) point checked, by a factor 4 to 10^4.
  The 2-2 patterns are what four predecessors add: the two carried axes come out exactly tied, at
  p^2 q^2/(2(p^2 q^2 + 2 r^4)) each for an opposite pair and p^2/(2(p^2 + q^2 + r^2)) each for an orthogonal pair.
  With three predecessors no two axes can carry two predecessors each, so no such tie exists there; the 1-1-1
  pattern ties three axes instead, at p/(3(p+q)) each.
  Every formula was reproduced exactly by brute-force enumeration at three random rational weights (180 of 180
  probabilities, zero deviation). The stated expectation holds; no HIT.
