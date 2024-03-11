# Erstellet von IFD12B von Christos Tsinaridis und Paul Wickenheiser
from PIL import Image, ImageDraw, ImageFont
import random
import os

# Erstellt einen Ordner namens "xo_dataset", wenn er nicht existiert. Der Ordner wird verwendet, um die generierten Bilder zu speichern.
os.makedirs("xo_dataset", exist_ok=True) 



def create_box_with_X(number):
   # Diese Funktion erstellt eine bestimmte Anzahl von Bildern mit einer Box und möglicherweise einem "X" darin.
   for i in range(number):
      # Eine Liste von Pfaden zu verschiedenen handschriftlichen Schriftarten. 
      font_list = ["Database_creation/ttf/Autography.otf",
                  "Database_creation/ttf/Callheart.ttf",
                  "Database_creation/ttf/Clear Brain.ttf",
                  "Database_creation/ttf/Dream Girl2.otf",
                  "Database_creation/ttf/Fayetteville Signature Regular.otf",
                  "Database_creation/ttf/Holyplan.ttf",
                  "Database_creation/ttf/Limited.ttf",
                  "Database_creation/ttf/Photograph Signature.ttf",
                  "Database_creation/ttf/SmileIsBeautiful.ttf",
                  "Database_creation/ttf/Taken by Vultures Demo.otf",
                  "Database_creation/ttf/TheWeddingSignature-Regular.ttf",
                  "Database_creation/ttf/Windpath.ttf"
                  ]
         
      # Wählt zufällig eine Schriftart aus der Liste aus.
      font_path = random.choice(font_list)

      # Festlegen der Bildgröße auf 500x500 Pixel.
      image_size = (500, 500)

      # Berechnet die Größe der Box, indem von jeder Seite des Bildes ein Abstand (Padding) eingehalten wird.
      box_padding = int(image_size[0] * 0.15)  # 15% Padding
      box_size = (box_padding, box_padding, image_size[0] - box_padding, image_size[1] - box_padding)

      # Erstellt ein neues Bild mit weißem Hintergrund.
      image = Image.new('RGB', image_size, 'white')
      draw = ImageDraw.Draw(image)

      # Zeichnet eine rechteckige Box auf das Bild.
      draw.rectangle(box_size, outline='black', width=2)

      # Entscheidet zufällig, ob ein "X" gezeichnet werden soll oder nicht.
      draw_x = random.choice([True, False])


      if draw_x:
         # Die Schriftgröße wird auf 80% der Boxbreite gesetzt
         font_size = int((box_size[2] - box_size[0]) * 1)
         font = ImageFont.truetype(font_path, font_size)

         # Erstellen von Randparameter in dem das "X" plaziert werden darf. 
         padding = int(font_size * 0.3)  # 30% der Schriftgröße als Rand für das "X"
         x_min = box_size[0] + padding
         y_min = box_size[1] + padding
         x_max = box_size[2] - padding
         y_max = box_size[3] - padding

         # Zufällige Koordinaten für das "X"
         x_random = random.randint(x_min, x_max)
         y_random = random.randint(y_min, y_max)

         # Zeichnet das "X" an der zufälligen Position innerhalb der Box.
         draw.text((x_random, y_random), "X", font=font, fill='black', anchor="mm")

      # Speichert das Bild im Ordner "xo_dataset" mit einer fortlaufenden Nummerierung.
      image_filename = f"xo_dataset/{i+1}.png"
      image.save(image_filename)

# Ruft die Funktion auf, um 100 Bilder zu erstellen.
create_box_with_X(100)