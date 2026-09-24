"""Direct all-resolved-mark electric-energy balance on a cube face flux."""
import json
from cube_high_flux_birth import A, EDGES, EDGE, gauss, electric, initial, move


def birth_on_edge(q, field, edge, sign):
    x, y = edge
    assert q[x] == q[y] == 0
    qq, ff = list(q), list(field)
    qq[x], qq[y] = sign, -sign
    ff[EDGE[edge]] += sign
    assert gauss(qq, ff)
    return qq, ff


def resolved_channels(n):
    q, field = initial(n)
    rows = []
    for edge in EDGES:
        a = next(x for x in edge if x in A)
        b = next(x for x in edge if x not in A)
        destinations = [y if x == a else x for x, y in EDGES if a in (x, y)]
        for sign in (-1, 1):
            outputs = []
            for c in destinations:
                if c == b:
                    continue
                mid_q, mid_f = move(q, field, a, c)
                out_q, out_f = birth_on_edge(mid_q, mid_f, edge, sign)
                outputs.append((tuple(out_q), tuple(out_f), electric(out_q, out_f)))
            assert len(outputs) == 2 and outputs[0][:2] != outputs[1][:2]
            rows.append({"edge": edge, "sign": sign,
                         "D_outputs": [x[2] for x in outputs],
                         "squared_norm": 2})
    assert len(rows) == 24
    return rows


def run():
    rows = []
    for n in (-19, -7, -3, -2, -1, 0, 1, 2, 3, 7, 19, 100):
        channels = resolved_channels(n)
        post = sum(sum(x["D_outputs"]) for x in channels)
        loss = sum(x["squared_norm"] for x in channels)
        before = 4 * n * n
        assert loss == 48 and post == 96 * n * n
        assert post - loss * before == -96 * n * n
        rows.append({"n": n, "initial_D": before,
                     "summed_resolved_mark_norm_squared": loss,
                     "summed_post_D_weighted": post,
                     "electric_drift_over_kappa_K": post - loss * before,
                     "channels": channels if n in (0, 2) else None})
    return {"claim": "exact all-resolved-mark electric-energy derivative",
            "rows": rows}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
