def read_data (file_path):
    file =  open(file_path, 'r')
    matrix = []
    for line in file :
        tokens = line.split(",") 
        matrix.append( list( map(lambda x : float(x) , tokens) ) )
    return matrix 

# print(read_data("training_1.csv")[0])


