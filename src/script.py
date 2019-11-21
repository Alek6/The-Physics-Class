train_mass = 22680
train_acceleration = 10
bomb_mass = 1


def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


f100_in_censius = f_to_c(100)


def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)


def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)


print("the GE train supplies " + str(train_force) + " Newtons of force.")


def get_energy(mass, c=3*10**8):
    return mass * c


bomb_energy = get_energy(bomb_mass, c=3*10**8)

