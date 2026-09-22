from pathlib import Path
w=Path('/private/tmp/review-drain-20260915/drain-author8137')
p=w/'scripts/possibility_symmetric_sequential_variation_forces_order_dependence_2026_09_15.py'
s=p.read_text(); a=s.index('"""'); b=s.index('"""',a+3)+3
s=s[:a]+'"""Exact positive path/star identities and finite scope witnesses in supplied models."""'+s[b:]
s=s.replace('POSSIBILITY_SYMMETRIC_SEQUENTIAL_FORMATION_THAT_VARIES_HAS_ORDER_DEPENDENT_RECORD_STATISTICS','SEQUENTIAL_FORMATION_PATH_AND_STAR_IDENTITIES')
s=s.replace('order-dependent statistics are registered data unless the rule is order-blind','the primitive supplies no averaging or process-law distribution')
s=s.replace('and "variation forces order dependence" in note_flat','and "supplied mathematical hypotheses" in note_flat')
s=s.replace('the note states the ends-independence derivation and the variation/order-dependence target','the note states conditional identities under supplied hypotheses')
a=s.index('    checks.check(\n        "note-dependency"');b=s.index('    checks.check(',a+20)
s=s[:a]+'''    checks.check(
        "note-dependency",
        "(MINIMAL_AXIOMS_2026-06-29.md)" in note
        and "(REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)" in note,
        "current authorities delimit grants rather than supplying the process",
    )

'''+s[b:]
a=s.index('    def lambda1(');b=s.index('    checks.check(',a)
s=s[:a]+'''    def polynomial_product(left, right):
        result = [Fraction(0)] * (len(left) + len(right) - 1)
        for i, x in enumerate(left):
            for j, y in enumerate(right):
                result[i + j] += x * y
        return result

    def haar_integral(coefficients):
        return sum((x / (i + 1) for i, x in enumerate(coefficients) if i % 2 == 0), Fraction(0))

    def density(beta, gamma):
        return [1 - gamma / 2, beta, 3 * gamma / 2]

    def lambda1(beta: Fraction, gamma: Fraction) -> Fraction:
        return haar_integral(polynomial_product([Fraction(0), Fraction(1)], density(beta, gamma)))

    def lambda2(beta: Fraction, gamma: Fraction) -> Fraction:
        return haar_integral(polynomial_product([Fraction(-1, 2), Fraction(0), Fraction(3, 2)], density(beta, gamma)))

'''+s[b:]
s=s.replace('two-state K^2 is independent of the start if and only if the kernel is independent of the neighbour','sampled two-state residual vanishes exactly for equal rows')
s=s.replace('K^2 Haar requires lambda_ell(K)^2 = 0, hence lambda_ell(K)=0, hence beta=gamma=0 in this family','the exact first two moments distinguish the sampled degree-two coefficients; no infinite harmonic classification executed')
a=s.index('    # Equator kernel:');b=s.index('    checks.check(\n        "note-quotes-identities"',a)
s=s[:a]+'''    # Integrate cos(phi)^2 by its Laurent constant coefficient.
    cosine = {-1: Fraction(1, 2), 1: Fraction(1, 2)}
    square = {}
    for i, x in cosine.items():
        for j, y in cosine.items():
            square[i + j] = square.get(i + j, Fraction(0)) + x * y
    haar_t2 = haar_integral([Fraction(0), Fraction(0), Fraction(1)])
    circle_t2 = square[0]
    checks.check("equator-two-step-moment", circle_t2 == Fraction(1, 2)
                 and haar_t2 == Fraction(1, 3) and circle_t2 != haar_t2,
                 "Laurent-angle integral versus polynomial-area integral")

    def atomic_square(a):
        result = {1: Fraction(0), -1: Fraction(0)}
        kernel = {1: a, -1: 1-a}
        for x, px in kernel.items():
            for y, py in kernel.items():
                result[x*y] += px*py
        return result
    checks.check("atomic-composition", all(
        atomic_square(a) == {1: a*a+(1-a)**2, -1: 2*a*(1-a)}
        for a in (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1))),
        "all sign products accumulated for four atomic kernels")

    def sequential_joint(vertices, edges, order, majority_at_three):
        joint = {}
        for values in product((0, 1), repeat=len(vertices)):
            assignment = dict(zip(vertices, values))
            seen = set()
            weight = Fraction(1)
            for vertex in order:
                neighbours = [x for x in seen if (vertex, x) in edges or (x, vertex) in edges]
                plus = Fraction(1, 2)
                if majority_at_three and len(neighbours) == 3:
                    plus = Fraction(int(sum(assignment[x] for x in neighbours) >= 2))
                weight *= plus if assignment[vertex] else 1-plus
                seen.add(vertex)
            joint[values] = weight
        return joint

    path_vertices = (0, 1, 2)
    path_edges = {(0, 1), (1, 2)}
    path_laws = [sequential_joint(path_vertices, path_edges, order, True)
                 for order in permutations(path_vertices)]
    checks.check("delayed-variation-path", all(
        law == {v: Fraction(1, 8) for v in product((0, 1), repeat=3)}
        for law in path_laws), "all six path orders iid when variation begins at three neighbours")
    star_vertices = (0, 1, 2, 3)
    star_edges = {(0, x) for x in (1, 2, 3)}
    center_first = sequential_joint(star_vertices, star_edges, star_vertices, True)
    leaves_first = sequential_joint(star_vertices, star_edges, (1, 2, 3, 0), True)
    checks.check("delayed-variation-star", sum(center_first.values()) == sum(leaves_first.values()) == 1
                 and center_first[(0, 1, 1, 1)] == Fraction(1, 16)
                 and leaves_first[(0, 1, 1, 1)] == 0,
                 "complete four-site joint laws differ at a majority-incompatible center")
    checks.check("independent-star-matching", all(
        sequential_joint(star_vertices, star_edges, order, False)
        == {v: Fraction(1, 16) for v in product((0, 1), repeat=4)}
        for order in permutations(star_vertices)), "all 24 independent-star orders give the product law")

    u, v = (1, -1, 0), (1, 1, -2)
    radial = [[Fraction(1, 3)+Fraction(u[i]*v[j], 12) for j in range(3)] for i in range(3)]
    radial_square = [[sum((radial[i][k]*radial[k][j] for k in range(3)), Fraction(0))
                     for j in range(3)] for i in range(3)]
    checks.check("radial-square-witness", all(sum(row) == 1 for row in radial)
                 and all(x > 0 for row in radial for x in row)
                 and radial[0] != radial[1]
                 and all(x == Fraction(1, 3) for row in radial_square for x in row)
                 and radial[0][1] != radial[1][0],
                 "positive nonconstant radial kernel squares to uniform but is not reversible")

'''+s[b:]
a=s.index('    checks.check(\n        "note-no-selection"');b=s.index('    return checks.finish()',a)
s=s[:a]+'''    checks.check("note-scope", "supplied mathematical hypotheses" in note_flat
                 and "almost every" in note_flat
                 and "negative packet lacks five" in note_flat,
                 "positive scope, a.e. qualification and deferred negative certification are explicit")
    print("per_element: exact rational entries, polynomial coefficients and finite joint assignments checked")
    print("per_site: complete three-site path and four-site star assignments checked")
    print("per_mode: degree-one and degree-two sphere moments checked; infinite harmonic family not executed")
    print("per_block: binary, six-axis and three-state radial matrices plus path/star joints checked")
    print("lattice_wide: checked and not executed — finite isolated windows only; no infinite dynamics claim")

'''+s[b:]
p.write_text(s)
