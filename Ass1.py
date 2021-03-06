
#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

#Triangle vertices
A = np.array([2,4])
B = np.array([0,0])
C = np.array([4,0])
l,k,m=0.5,0.5,0.5
P=(1/(l+k))*(np.column_stack((C,B))@np.array([l,k]).T)
Q=(1/(l+m+k))*(np.column_stack((C,B,A))@np.array([l,k,m]).T)
print(P,Q)
#Generating all lines
x_PQ = line_gen(P,Q)
x_QA = line_gen(Q,A)

#Plotting all lines
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QA[0,:],x_QA[1,:],label='$QA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.2), P[1] * (1) , 'P')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.03), Q[1] * (1 - 0.1) , 'Q')
plt.text(1.0,0.08,'l')
plt.text(3.0, 0.08, 'k')
plt.text(1.8, 0.75, 'm')
plt.text(1.7, 2.59, 'k+l')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.show()




