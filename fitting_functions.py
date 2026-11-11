def linear(m, x, b):
    y = m*x+b
    return y

def slope_units(x_units,y_units):
    x_units = x_units.rstrip('s')
    y_untis = y_units.rstrip('s')
    return y_units + "/" + x_units

def print_equation(m, b, y_units, x_units):
    units = slope_units(x_units,y_units)
    print("the equation of the line is: y =", m, units, "x +", b, y_units)
