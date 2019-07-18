letter_value = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
# a hash table for quickly changing the letters to their integer values
list_of_names = sorted(list(open("Problem_22_names.csv",'r'))[0].replace('"','').split(','))
# takes out the quotes spilts the single string at the commas and sorts the list alphabetically
total_sum = 0
for i in range(len(list_of_names)):
    suum = 0
    for j in list_of_names[i].lower():
        suum += letter_value[j]
    total_sum += (i+1)*suum
total_sum
