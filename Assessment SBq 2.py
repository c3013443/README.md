import sympy as sp # For eigen values and vectors

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
    A = sp.Matrix([
        [a,b,c],
        [d,e,f],
        [g,h,i]
        ])
    print("\nYour matrix is now labelled as A:") # clarifications for users matrix
    sp.pprint(A)
    if A.det() != 0:
        A_inv=A.inv()
        print("\nA^(-1)=")  # for clarifications on A^-1=
        sp.pprint(A_inv)
    else:
        print("\nA is singular") #simple clarification
        wugenvals = A. eigenvals()#finds eigen valuses
        eigenvects = A.eigenvects()# finds eigenvectors
        print("\nEigenvalues of A:")#clarification
        sp.pprint(eigenvals)
        print("\nEigenvectors of A:")#clarification
        for eigenval, multiplicity, eigenvect in eigenvects:
            print(f"Eigenvalue: {eigenval}")
            print("Eigenvector(s):")# to find the eigenvectors from prior codes
            sp.pprint(eigenvect)
            print() #Shows
            try:
                P,D = A.diagonalize()
                print("\nA can be diagonalized P*D*P^(-1):")
                print("P(Matrix of eigenvectors):") # clarification for P
                sp.pprint(P)
                print("\nD(Diagonal of the eigenvalues):") #Clarification For D
                sp.pprint(D)
            except sp.MatrixError: # If A cant be diagonalised
                print("\nA is not diagonlizable use different values for a different result.")
            create_matrix_and_compute(1,2,3,4,5,6,7,8,9)

 
