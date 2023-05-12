#!/usr/bin/env python3


from ortools.linear_solver import pywraplp


def solve_grid(m: int, n: int, min_x: int = 1):
    solver = pywraplp.Solver.CreateSolver("SAT")
    inf = solver.infinity()

    x = {
        (i, j): solver.IntVar(min_x, inf, f"x_{i}_{j}")
        for i in range(m)
        for j in range(n)
    }

    y = solver.IntVar(min_x, inf, "y")  # y = max x

    for i in range(m):
        for j in range(n):
            xij = x[(i, j)]
            solver.Add(y >= xij)
            for ip in range(i, m):
                for jp in range(j + 1 if i == ip else 0, n):
                    xipjp = x[(ip, jp)]
                    d = abs(i - ip) + abs(j - jp)
                    w = solver.IntVar(0, 1, f"w_{i}_{j}_{ip}_{jp}")
                    z = solver.IntVar(0, 1, f"z_{i}_{j}_{ip}_{jp}")
                    mn = m * n
                    solver.Add(w + z <= 1)
                    solver.Add(xij + mn * w >= xipjp + z)
                    solver.Add(xij - mn * z <= xipjp - w)
                    solver.Add(d + mn * (z + w) >= xij + 1)
                    solver.Add(z + w <= 1)

    solver.Minimize(y)
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        result = solver.Objective().Value()  # y
        length = len(str(int(result)))
        for i in range(m):
            for j in range(n):
                cell = x[(i, j)]
                print(
                    f"{int(cell.solution_value()):{length}} ",
                    end="\n" if j == n - 1 else " ",
                )
    else:
        print(":/")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("m", help="number of rows", type=int, default=6, nargs="?")
    parser.add_argument("n", help="number of columns", type=int, default=6, nargs="?")
    args = parser.parse_args()
    solve_grid(args.m, args.n)
