arr=[
    ["Karim",23,"ATTGCTAGCATGATCGT"],
    ["Rita",27,"ATGCTGACGTAGCGTGAC"],
    ["Mina",45,"ATGCATGCGATGCGATGC"],
    ["Rahim",56,"ATAACGTGCGTAGCCCG"]
    ]
#for first_order in arr[0][1]:
    #print(first_order)
arr=[
    ["Rina","3","ATGCGTGACGTGACGT"],
    ["Tina","8","ATGCGTGACGTGCAGT"],
    ["Kiki","8","TGCGTGACGTGACGTG"],
    ["Mike","6","GTCAGTCGAAGTCGTA"]
    ]
for first_order in arr[0][1]:
    print(first_order)

new_array=[1,6,7,8,90,23,45,65,89,12,567,99,876,1.456,8.98,2.45,100]
print(new_array[-1])
print(new_array[1:2])
print(new_array[0:3])
print(new_array[1:5])
print(new_array[3:8])
print(new_array[5:9])
print(new_array[5:])
print(new_array[:9])

string="ATGCAGTGCAGTGACGTGACGGGAATGCA"
print(string[0:3])
print(string[1:4])
print(string[2:5])

array_sample=["Math","Physics","Biology","Chemistry","Genetics"]
array_sample.insert(0,"Art")
print(array_sample)
array_sample.insert(4,"Biochemistry")
print(array_sample)

string_sample=["A","T","G","C"]
string_sample.insert(3,"H")
print(string_sample)
