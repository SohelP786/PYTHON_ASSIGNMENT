A={82:"RBNB",99:"Ram",2:"Sai",9:"Om"}
sorted_values = sorted(A.values()) # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in A.keys():
        if A[k] == i:
            sorted_dict[k] = A[k]

print(sorted_dict)