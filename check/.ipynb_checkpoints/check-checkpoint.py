from IPython.display import display, Image
from random import random, randint
import string
import math







def test(ex, *args):
    if ex == '1.1':
        
        if ( isinstance(args[0], float) and isinstance(args[1], int) and isinstance(args[2], int) ):
            if ( int(args[0]+args[1]) == args[2]):
                print("Все верно!")
                return Image(url='https://www.meme-arsenal.com/memes/22e0fbcffd5b78ef953409238a031c2b.jpg', width=250, height=250)
            else:
                print("dest должна равняться ark + pizza \nПример: dest = int(ark + pizza)")
                return Image(url='https://www.irishtimes.com/polopoly_fs/1.2809144.1475080968!/image/image.jpg_gen/derivatives/box_620_330/image.jpg'\
                         ,width=250, height=250 )
        else:
            print("Перечитай задание=) и попробуй снова.")
            return Image(url='https://www.irishtimes.com/polopoly_fs/1.2809144.1475080968!/image/image.jpg_gen/derivatives/box_620_330/image.jpg'\
                         ,width=250,height=250)

