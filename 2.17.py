line = "Natalia Piechnik\nKrakow"
print(sorted(line.split(), key=str.lower))
print(sorted(line.split(), key=lambda x: len(x) ))