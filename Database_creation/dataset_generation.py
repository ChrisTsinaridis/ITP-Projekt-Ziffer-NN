from PIL import Image, ImageDraw, ImageFont
import random
import os

os.makedirs("xo_dataset", exist_ok=True)

def create_box_with_X(number):
   for i in range(number):
      # Pfad zur handschriftlichen Schriftart (ersetzen Sie dies durch den Pfad Ihrer eigenen Schriftart)
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
         
       
      font_path = random.choice(font_list)

       # Festlegen der Bildgröße
      image_size = (500, 500)

      # Berechnen der Boxgröße als 10% kleiner als die Bildgröße
      box_padding = int(image_size[0] * 0.1)  # 10% Padding
      box_size = (box_padding, box_padding, image_size[0] - box_padding, image_size[1] - box_padding)

      # Erstelle ein weißes Bild
      image = Image.new('RGB', image_size, 'white')
      draw = ImageDraw.Draw(image)

      # Zeichne eine Box
      draw.rectangle(box_size, outline='black', width=2)

      draw_x = random.choice([True, False])

      # Lade die handschriftliche Schriftart
      if draw_x:
         # Die Schriftgröße wird auf 80% der Boxbreite gesetzt
         font_size = int((box_size[2] - box_size[0]) * 1)
         font = ImageFont.truetype(font_path, font_size)

         # Generiere eine zufällige Position für das "X" innerhalb des Kästchens
         padding = int(font_size * 0.3)  # 10% der Schriftgröße als Rand für das "X"
         x_min = box_size[0] + padding
         y_min = box_size[1] + padding
         x_max = box_size[2] - padding
         y_max = box_size[3] - padding

         # Zufällige Koordinaten für das "X"
         x_random = random.randint(x_min, x_max)
         y_random = random.randint(y_min, y_max)

         # Zeichne das "X" an der zufälligen Position
         draw.text((x_random, y_random), "X", font=font, fill='black', anchor="mm")

      # Speichere das Bild
      image_filename = f"xo_dataset/{i+1}.png"
      image.save(image_filename)

create_box_with_X(100)