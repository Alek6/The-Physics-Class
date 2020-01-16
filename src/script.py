# Global variables
train_mass = 22680
train_acceleration = 10
bomb_mass = 1


# Function f_to_c() that converts a temperature from Fahrenheit to Celsius.
# @:param f_temp: the temperature in Fahrenheit to be converted
# @:return c_temp: the converted temperature in Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp


f100_in_censius = f_to_c(100)


# Function c_to_f() that converts a temperature from Celsius to Fahrenheit.
# @:param c_temp: the temperature in Celsius to be converted
# @:return f_temp: the converted temperature in Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp


c0_in_fahrenheit = c_to_f(0)


# Function get_force() that takes in mass, acceleration and calculates the force.
# @:return mass multiplied by acceleration
def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)


print("the GE train supplies " + str(train_force) + " Newtons of force.")


# Function get_energy() that takes in mass, constant 'c' and calculates the energy.
# @:param mass: the mass to which calculate the energy
# @:param c: the constant that is usually set to the speed of light, which is roughly 3 x 10^8
# @:return mass multiplied by c
def get_energy(mass, c=3*10**8):
    return mass * c


bomb_energy = get_energy(bomb_mass, c=3*10**8)


print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")
