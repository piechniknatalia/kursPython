line = "Natalia Piechnik\nKrakow"
first = ''
last = ''
for word in line.split(): first+=word[0]
print(first)
for word in line.split(): last+=word[-1]
print(last)