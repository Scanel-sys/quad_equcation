# -1 ( 1 1 1 )
import math


def solve(a, b, c):

    if check_if_zero(a):
        if check_if_zero(b):
            if check_if_zero(c):
                return 4, "infinite number of solution"

            return 0, "There are no suitable roots"

        else:
            if check_if_nan(c) or check_if_nan(b):
                return 5, "One NaN root because NaN passed", float('NaN')

            elif c == 0:
                if check_if_inf(b):
                    return 9, "Undefined result due to operations with infinite", float("NaN")

                x1 = 0

            else:
                x1 = -c / b

            return 1, "One root", x1

    else:
        discriminant = b ** 2 - 4 * a * c

        if check_if_nan(discriminant):
            if check_if_nan(a) or check_if_nan(b) or check_if_nan(c):
                return 6, "Two NaN roots because NaN passed", float('NaN'), float('NaN')

            else:
                return 7, "Two NaN due to operations with infinite", float('NaN'), float('NaN')

        elif discriminant < 0:
            return solve_for_negative_discriminant(discriminant, a, b)

        else:
            return solve_for_nonnegative_discriminant(discriminant)


def check_if_zero(number) -> bool:
    if number == 0:
        return True
    return False


def check_if_inf(number) -> bool:
    if number == float('inf') or number == float('-inf'):
        return True
    return False


def check_if_nan(number) -> bool:
    if not (number <= 0 or number > 0):
        return True
    return False


def solve_for_negative_discriminant(discriminant, a, b):
    discr_sqrt_div_2a = abs(math.sqrt(-discriminant) / (2 * a))
    b_div_2a = b / (2 * a)
    if check_if_nan(b_div_2a) or check_if_nan(discr_sqrt_div_2a) or check_if_inf(b_div_2a) or \
            check_if_inf(discr_sqrt_div_2a):
        return 7, "Two NaN due to operations with infinite", float('NaN'), float('NaN')

    x1 = str(-b_div_2a) + ' + ' + str(discr_sqrt_div_2a) + 'i'
    x2 = str(-b_div_2a) + ' - ' + str(discr_sqrt_div_2a) + 'i'

    return 2, "two roots", x1, x2


def solve_for_nonnegative_discriminant(discriminant):
    discriminant = math.sqrt(discriminant)
    x1 = (-b + discriminant) / (2 * a)
    x2 = (-b - discriminant) / (2 * a)

    if check_if_nan(x1) or check_if_nan(x2) or check_if_inf(x1) or check_if_inf(x2):
        return 7, "Two NaN due to operations with infinite", float('NaN'), float('NaN')

    if x1 != x2:
        return 2, "two roots", x1, x2

    return 3, "two same roots", x1, x1


a, b, c = map(float, input().split())
print(solve(a, b, c))
