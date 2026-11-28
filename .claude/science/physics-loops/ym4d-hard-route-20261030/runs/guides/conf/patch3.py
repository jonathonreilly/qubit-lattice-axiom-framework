import sys,re
p=sys.argv[1]; s=open(p).read()
reps=[
("""Read at this step, and not before: `parts/gap.md` (state of attack, routes
tried, methods set aside 19 to 34 as listed there, route registry, test
table, exact price; methods 1 to 18 are not copied there, they are in
`library/gap-crux-exercise2-max.md` 6a, of which I read only the Route E
part, L448-L523 by search); the FINISH RESULT lines of rows 878, 1004, 1018
and 1025 in full; keyword context only in rows 731, 744, 754, 789, 792, 800,
884, 899, 923, 936, 996, 1016 and 1076.
""",
"""Read at this step, and not before: `parts/gap.md` (state of attack, routes
tried, methods set aside 19 to 34 as listed there, route registry, test
table, exact price); methods 1 to 18 in `library/gap-crux-exercise2-max.md`
6a (L392-416), with the Route E lines of that file found by search
(L448-523, first 300 to 500 characters of each line only); the FINISH RESULT
lines of rows 878, 1004, 1018 and 1025 in full; keyword context only in rows
731, 744, 754, 789, 792, 800, 899, 923, 936, 996, 1016 and 1076. Rows named
below with "by search" were not read.
"""),
("""- Other rows of the same family. Row 744 (Theorem R, the finite form of
  't Hooft's duality; prior work 't Hooft 1979, Nguyen-Tanizaki-Unsal 2023).
  Rows 697 and 731 (twisted transfer, sector engines; the open piece is
  (EV-STEP)). Row 1004""",
"""- Other rows of the same family. Row 744 (Theorem R, a finite quantitative
  form of 't Hooft's duality; prior work 't Hooft 1979, Nguyen-Tanizaki-Unsal
  2023). Row 731 (Theorem S-w with the twisted transfer operator of rows 698
  and 716; the open piece is (EV-STEP)). Row 1004"""),
("""Row 1057
  (Lemma K4: the classical cost of the centre twist is zero).""",
"""Row 1051
  with its checks 1056 and 1057 (Lemma K4: the classical cost of the centre
  twist is zero)."""),
("""- Possibly not on file (by search of FINISH only; not checked further): the""",
"""- Methods set aside that Step 1 and Step 2 touched without knowing: method
  13 (flux half from glue half by clustering; re-judged in row 878 6d, which
  is where (TS-theta) comes from); method 14 (thin Z_2 lift with Griffiths
  inequalities, "mean coupling 1.5 against 0.44"; this is item 3 of 1.2
  here); method 17 (thick vortex by field-independent spreading, refuted as a
  method); method 18 (Migdal-Kadanoff, group-blind; item 6 of 1.2 here).
- Possibly not on file (by search of FINISH only; not checked further): the"""),
("""- Row 754 has the identity: the defect is an integral over beta of the
  finite-size shift of the ground-state plaquette. It also has Proposition VB
  (volume blindness, argued): local loop equations with reflection
  positivity cannot bound these shifts.""",
"""- Row 754 (keyword context only): "delta = 48 a^4 times the integral of the
  finite-size shift of the ground-state plaquette". I read this as the same
  calculus identity. It also has Proposition VB (volume blindness, argued):
  local loop equations with reflection positivity cannot bound these shifts.
- Method 4 of the set-aside list: "one-way step for a torus quantity;
  step-scaling couplings: each step as hard as the seed; fails where two
  confining phases coexist". The flow of the twist ratio in Attack 2 is of
  this kind."""),
("""- The twist form (RESP-tw) is (K-RESP) of row 800 (Kanazawa's line: a bound
  on the Wilson twist score with all normalizers), and Proposition KR of
  row 1025.""",
"""- The twist form (RESP-tw) appears to be (K-RESP) of row 800 (Kanazawa's
  line: "a bound on the original Wilson twist score at order one with all
  normalizers"; file not read), with Proposition KR of row 1025."""),
("""Tanizaki-Unsal (rows found by search:
  656 to 800, 1005, 1011, 1012).""",
"""Tanizaki-Unsal (by search of FINISH,
  rows not read: among them 656, 661, 688, 702, 711, 744, 784, 797, 800,
  1005, 1011, 1012)."""),
]
for a,b in reps:
    assert s.count(a)==1, a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
print("patched; home-path:", bool(re.search(r"/Users/|~/|/private/tmp", s)), "bytes", len(s.encode()))
