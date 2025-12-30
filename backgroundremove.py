import rembg
import numpy as np
from PIL import Image 

in_ar = np.array(Image.open(input("fotoğrafın yolunu giriniz :")))
out = Image.fromarray(rembg.remove(in_ar))
out.save('out.png')