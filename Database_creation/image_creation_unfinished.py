from PIL import Image


# Öffne das Bild, dessen Hintergrund entfernt werden soll
image_with_background = Image.open('Database_creation/data/images/rectangle_empty.png')

# Konvertiere das Bild in ein RGBA-Bild, um Transparenz zu ermöglichen
image_with_transparency = image_with_background.convert("RGBA")

# Lade die Daten des Bildes
datas = image_with_transparency.getdata()

# Neue Datenliste
new_data = []

# Definiere die Farbe, die entfernt werden soll (z.B. weiß)
# Die Werte können angepasst werden, um die Farbe des Hintergrunds zu treffen
remove_color = (255, 255, 255)

# Gehe durch jedes Item und entferne die definierte Farbe
for item in datas:
   # Farbvergleich mit einer Toleranz, um ähnliche Farben zu entfernen
   if item[0] in range(remove_color[0] - 10, remove_color[0] + 10) and item[1] in range(remove_color[1] - 10, remove_color[1] + 10) and item[2] in range(remove_color[2] - 10, remove_color[2] + 10):
       # Setze die Transparenz auf 0 (vollständig transparent)
       new_data.append((255, 255, 255, 0))
   else:
       new_data.append(item)

# Aktualisiere die Daten des Bildes
image_with_transparency.putdata(new_data)

# Speichere das Bild ohne Hintergrund
image_with_transparency.save('Database_creation/data/images/image_no_background.png')

# Jetzt können Sie das Bild ohne Hintergrund mit einem anderen Bild blenden
# (Folgen Sie den vorherigen Anweisungen, um die Bilder zu blenden)

# Öffne die beiden Bilder
image2 = Image.open('Database_creation/data/X/exp1.jpg')
image1 = Image.open('Database_creation/data/images/image_no_background.png')
 
# Konvertiere die Bilder in Graustufen
image1_gray = image1.convert('L')
image2_gray = image2.convert('L')

# Stelle sicher, dass die Bilder die gleiche Größe haben
if image1_gray.size != image2_gray.size:
   image2_gray = image2_gray.resize(image1_gray.size)

# Blende die graustufigen Bilder mit einem Alpha-Wert von 0.5
blended_image = Image.blend(image2_gray, image1_gray, alpha=0.6)

# Ändere die Größe des geblendeten Bildes auf 500x500 Pixel


# Speichere das geblendete Bild
blended_image.save('Database_creation/data/images/blended_image_gray_500px.png')

# Zeige das geblendete Bild an
blended_image.show()