import random as rand
import string
def random_user_id():
    dig=[]
    for i in range(6):
        i= rand.choice(list(string.digits + string.ascii_letters))
        dig.append(i)
    dig = "".join(dig)
    return dig
    
def user_id_gen_by_user(chars, num):
    dig=[]
    fin=[]
    for _ in range(num):
        dig=[]
        for j in range(chars):
            j= rand.choice(list(string.digits + string.ascii_letters))
            dig.append(j)
        dig = "".join(dig)
        fin.append(dig+ "\n")
    return "".join(fin)

def rgb_color_gen():
    return f'rgb({rand.randint(0,255)},{rand.randint(0,255)},{rand.randint(0,255)})'



def list_of_hexa_colors(num):
    dig=[]
    fin=[]
    for _ in range(num):
        dig=[]
        for j in range(6):
            j= rand.choice(list(string.hexdigits))
            dig.append(j)
        dig = "".join(dig)
        fin.append("#"+dig+ "\n")
    return "".join(fin)  



def list_of_rgb_colors(num):
        color=[]
        for _ in range(num):
            color.append(f'rgb({rand.randint(0,255)},{rand.randint(0,255)},{rand.randint(0,255)})'+'\n')
        
        color="".join(color)
        return color 

def shuffle_list(in_list):
    shuffle=[]
    buff= len(in_list)
    for _ in range(buff):
        selection = rand.choice(in_list)
        in_list.remove(selection)
        shuffle.append(selection)
    return shuffle

def random_orderded():
    in_list=list(range(10))
    out=[]
    for _ in range(10):
        choice= rand.choice(in_list)
        in_list.remove(choice)
        out.append(choice)
    return out
        







        


    