from PIL import Image, ImageDraw

# Pobieranie danych od użytkownika
dimensions_input = input("Podaj wymiary (szerokość x wysokość). Dla Iphone wpisz 1320x2868: ")
partitions_input = input("Podaj liczbę partycji: ")

# Parsowanie danych
try:
    width_str, height_str = dimensions_input.lower().replace(' ', '').split('x')
    width = int(width_str)
    height = int(height_str)
    partitions = int(partitions_input)
except ValueError:
    print("Błędne dane wejściowe. Użyj formatu: 100x300 i podaj liczbę całkowitą.")
    exit()

# Obliczanie końcowego rozmiaru obrazu
final_width = width * partitions
final_height = height

# Tworzenie pustego, białego obrazu
img = Image.new("RGB", (final_width, final_height), "white")
draw = ImageDraw.Draw(img)

# Rysowanie szarych linii w miejscach width, 2*width, itd. (do przedostatniej partycji)
for i in range(1, partitions):
    x = i * width
    draw.line([(x, 0), (x, final_height)], fill="gray", width=1)

# Zapis obrazu
filename = f"Background_{final_width}x{final_height}.png"
img.save(filename)
print(f"Obraz zapisany jako: {filename}")
