num_input = 5

inputs = [800, 700, 900, 198, 300]

first_inputs = inputs[:3]
second_inputs = inputs[3:]

print(min(first_inputs) + min(second_inputs) - 50)