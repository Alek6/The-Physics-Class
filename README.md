# The-Physics-Class
You are a physics teacher preparing for the upcoming semester.<br>
You want to provide your students with some functions that will help them calculate some fundamental physical properties.
<hr>
<h2>Turn up the Temperature</h2>
<ol>
    <li>Write a function called <code>f_to_c</code> that takes an input <code>f_temp</code>, a temperature in Fahrenheit, and converts it to <code>c_temp</code>, that temperature in Celsius.<br>
    The equation to convert Fahrenheit to Celsius is:<br>
    <code>Temp (C) = (Temp (F) - 32) * 5/9</code></li>
    <li>Define a variable <code>f100_in_celsius</code> and set it equal to the value of <code>f_to_c</code> with <code>100</code> as an input.</li>
    <li>Write a function called <code>c_to_f</code> that takes an input <code>c_temp</code>, a temperature in Celsius, and converts it to <code>f_temp</code>, that temperature in Fahrenheit.<br>
    The equation to convert Celsius to Fahrenheit is:<br>
    <code>Temp (F) = Temp (C) * (9/5) + 32</code></li>
    <li>Define a variable <code>c0_in_fahrenheit</code> and set it equal to the value of <code>c_to_f</code> with <code>0</code> as an input.</li>
</ol>
<h2>Use the Force</h2>
<ol>
    <li>Define a function called <code>get_force</code> that takes in mass and acceleration.<br>
    It should return mass multiplied by acceleration.</li>
    <li>Test <code>get_force</code> by calling it with the variables <code>train_mass</code> and <code>train_acceleration</code>.<br>
    Save the result to a variable called <code>train_force</code> and print it out.</li>
    <li>Print the string “The GE train supplies X Newtons of force.”, with <code>X</code> replaced by <code>train_force</code>.</li>
    <li>Define a function called <code>get_energy</code> that takes in <code>mass</code> and <code>c</code>.<br><br>
    <ul>
        <li><code>c</code> is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set <code>c</code> to have a default value of <code>3*10**8</code>.<br><br></li>
        <li><code>get_energy</code> should return <code>mass</code> multiplied by <code>c</code> squared.</li>
    </ul>
    <li>Test <code>get_energy</code> by using it on <code>bomb_mass</code>, with the default value of <code>c</code>.<br>
    Save the result to a variable called <code>bomb_energy</code>.</li>
    <li>Print the string “A 1kg bomb supplies X Joules.”, with <code>X</code> replaced by <code>bomb_energy</code>.</li>
</ol>