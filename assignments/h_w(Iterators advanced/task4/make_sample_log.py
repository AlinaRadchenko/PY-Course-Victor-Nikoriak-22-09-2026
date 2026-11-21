
import random
import sys
from datetime import datetime, timedelta

LINES = 200_000
seed = sys.argv[1] if len(sys.argv) > 1 else "17"
if not seed.isdigit():
    print(f"The seed must be a whole number, got {seed!r}.")
    sys.exit(1)
random.seed(int(seed))

ips = [f"203.0.113.{i}" for i in range(1, 255)] + [f"198.51.100.{i}" for i in range(1, 255)]
ips += [f"10.{a}.{b}.{c}" for a, b, c in [(i % 7, i % 13, i % 251) for i in range(1500)]]
paths = ["/", "/login", "/api/products", "/api/products/42", "/api/cart",
         "/api/orders", "/static/app.js", "/static/style.css", "/search", "/admin"]
weights = [20, 8, 25, 6, 10, 5, 12, 12, 9, 1]
statuses = [200] * 90 + [301] * 3 + [404] * 4 + [500] * 2 + [403]
start = datetime(2026, 10, 1, 0, 0, 0)

with open("access.log", "w", encoding="utf-8") as f:
    t = start
    for i in range(LINES):
        t += timedelta(seconds=random.randint(0, 3))
        ip = random.choice(ips)
        path = random.choices(paths, weights)[0]
        status = random.choice(statuses)
        ms = int(random.expovariate(1 / 120)) + 5
        line = f"{t.isoformat()} {ip} GET {path} {status} {ms}"
        r = random.random()
        if r < 0.01:
            line = line.rsplit(" ", 1)[0] + " -"   # broken: time is not a number
        elif r < 0.02:
            line = line[: random.randint(5, 30)]   # broken: cut in the middle
        f.write(line + "\n")
print(f"access.log: {LINES} lines, seed {seed}")