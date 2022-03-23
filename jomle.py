def tedad_kalame(jomle):

    count = 1
     
    for i in range(0, len(jomle)):
         
        if jomle[i] == " ":
            count = count + 1
         
    return count

jomle = input('jomle ra vared konid: ') 

print("tedad kalamat jomle: ",tedad_kalame(jomle))