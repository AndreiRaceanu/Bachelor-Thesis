def read_data (file_path):
    file =  open(file_path, 'r')
    matrix = []
    for line in file :
        tokens = line.split(",") 
        matrix.append( list( map(lambda x : float(x) , tokens) ) )
    return matrix 


N = 2    # Number of files used for training
X = []   # Training data_set
for it in range(1,N+1): 
    X.append(read_data(f"training_{it}.csv"))





#print(X[0][0][0])
#print(X[1][0][0])
# print(read_data("training_1.csv")[0])


"""
PSEUDO_COD

    poly_lib = ps.PolynomialLibrary(degree=int(param1))
    trig_lib = ps.FourierLibrary(n_frequencies=int(param2))
    custom_lib = poly_lib + trig_lib
    feature_library = custom_lib
model = ps.SINDy(
    differentiation_method=smooth_finite_difference,
    feature_library=feature_library,
    optimizer=optimizer,
    feature_names=["x", "y"],
"""