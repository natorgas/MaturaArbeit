# Read the contents of the text file
with open('C:\\Users\\david\\Documents\\Schule\\MaturaArbeit\\MA_NonePython\\SciLab\\DataTextfiles\\critical_time_below_5.txt', 'r') as file:
    content = file.read()

content = content.replace(' ', '').replace('.', '')


# Write the modified content back to the text file
with open('C:\\Users\\david\\Documents\\Schule\\MaturaArbeit\\MA_NonePython\\SciLab\\DataTextfiles\\critical_time_below_5.txt', 'w') as file:
    file.write(content)
