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
        
        
    if ex == '2.1':
        print(f"Debug: l_result_1 == {args[0]}, l_result_2 == {args[1]}, l_result_3 == {args[2]}, l_result_4 == {args[3]}\n")
        
        if( args[0] == True and args[1] == False and args[2] == True and args[3] == False ):
            print("Все верно!")
            print("Хорошая работа=)")
            return Image(url='https://media.giphy.com/media/cQQd1c5xFas4U/giphy.gif', width=500, height=500)
        
        else:
            print("Не верно, проверь Debug: строку.")
            return Image(url='https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif', width=500, height=500)
            

