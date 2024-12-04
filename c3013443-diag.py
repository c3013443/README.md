from sympy import Matrix, symbols, pprint # For eigen values and vectors

def create_matrix_and_compute():
    print("Choose 9 numbers for a 3x3 matrix ordered by row:") # so the order for number input is clear
    a = float(input("Choose a value for a: "))
    b = float(input("Choose a value for b: "))
    c = float(input("Choose a value for c: "))
    d = float(input("Choose a value for d: "))
    e = float(input("Choose a value for e: "))
    f = float(input("Choose a value for f: "))
    g = float(input("Choose a value for g: "))
    h = float(input("Choose a value for h: "))
    i = float(input("Choose a value for i: "))  # For all the values submitted will make the matrix
    A = Matrix([[a,b,c],
                [d,e,f],
                [g,h,i]])
        
    print("\nYour matrix is now labelled as A:") # clarifications for users matrix
    pprint(A)
    if A.det() != 0:
        A_inv=A.inv()
        print("\nA^(-1)=")  # for clarifications on A^-1=
        pprint(A_inv)
    else:
        print("\nA is singular therefore doesnt have an inverse") #simple clarification
        eigenvals = A. eigenvals()#finds eigen valuses
        eigenvects = A.eigenvects()# finds eigenvectors
        print("\nEigenvalues of A:")#clarification
        pprint(eigenvals)
        print("\nEigenvectors of A:")#clarification
        for eigenval, multiplicity, eigenvect in eigenvects:
            print(f"Eigenvalue: {eigenval}")
            print(f"Multiplicity: {multiplicity}")
            print("Eigenvector(s):")# to find the eigenvectors from prior codes
            pprint(eigenvect)

P, D = A.diagonalize() #gives the following prints a function
print("\nDiagonalization of A:")
print("Matrix P (eigenvectors):") # Shows which P us going to represent
pprint(P)
print("Matrix D (Eigenvalues):")#Gives eigenvalues there respective matrix
pprint(D)

 
