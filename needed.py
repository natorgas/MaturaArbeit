# Read the contents of the text file
with open('C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\lyapunov_exponents.txt', 'r') as file:
    content = file.read()

content = content.replace(' ', '')#.replace('.', '')


# Write the modified content back to the text file
with open('C:\\Users\\david\\Programming\\MyPython\\PycharmProjects\\lyapunov_exponents.txt', 'w') as file:
    file.write(content)
