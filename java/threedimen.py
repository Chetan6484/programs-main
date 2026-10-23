layers = [
    [[1, 2], [3, 4]],     
    [[5, 6], [7, 8]]      
]
 
print(layers[1][0][1])  
for i in range(len(layers)):
    print("Layer", i)
    for row in layers[i]:
        print(row)
