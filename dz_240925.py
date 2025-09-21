import math

def f_opt(x):
    return math.exp(x) + x**2

def brute_force_method(func, a, b, e, delta):
    N = 0
    min_f = float('inf')
    x_star = a
    x = a
    while x <= b:
        f_val = func(x)
        N += 1
        if f_val < min_f:
            min_f = f_val
            x_star = x
        x += delta
    return x_star, min_f, N

def golden_section_method(func, a, b, e):
    N = 0
    tau = (3 - math.sqrt(5)) / 2 
    x1 = a + tau * (b - a)
    x2 = b - tau * (b - a)
    f1 = func(x1)
    f2 = func(x2)
    N += 2
    while b - a > e:
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + tau * (b - a)
            f1 = func(x1)
            N += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - tau * (b - a)
            f2 = func(x2)
            N += 1
    x_star = (a + b) / 2
    f_star = func(x_star)
    N += 1
    return x_star, f_star, N

def bitwise_search_method(func, a, b, e):
    N = 0
    h = (b - a) / 4.0
    x0 = a
    f_x0 = func(x0)
    N += 1
    while True:
        x1 = x0 + h
        if not (a <= x1 <= b):
            if abs(h) <= e:
                return x0, f_x0, N
            else:
                h = -h / 4.0
                continue
        f_x1 = func(x1)
        N += 1
        if f_x0 > f_x1:
            x0 = x1
            f_x0 = f_x1
            if not (a < x0 < b):
                if abs(h) <= e:
                    return x0, f_x0, N
                else:
                    h = -h / 4.0
                    continue
        else:
            if abs(h) <= e:
                return x0, f_x0, N
            else:
                h = -h / 4.0
                x0 = x1
                f_x0 = f_x1


a_opt = -1
b_opt = 1
deltas = [1e-3, 1e-4, 1e-5]
epsilons = [1e-3, 1e-4]

print("\nМетод перебора (оптимизация e^x + x^2):")
for e in epsilons:
    delta = e
    x_star, f_star, N = brute_force_method(f_opt, a_opt, b_opt, e, delta)
    print(f"Для e={e} (delta={delta}): x*={x_star:.6f}, f*={f_star:.6f}, N={N}")

print("\nМетод золотого сечения (оптимизация e^x + x^2):")
for e in epsilons:
    x_star, f_star, N = golden_section_method(f_opt, a_opt, b_opt, e)
    print(f"Для e={e}: x*={x_star:.6f}, f*={f_star:.6f}, N={N}")

print("\nМетод поразрядного поиска (оптимизация e^x + x^2):")
for e in epsilons:
    x_star, f_star, N = bitwise_search_method(f_opt, a_opt, b_opt, e, 1e-5)
    print(f"Для e={e}: x*={x_star:.6f}, f*={f_star:.6f}, N={N}")