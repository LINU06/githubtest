MAX=100;
mat=[[0 for x in range(MAX)]] for y in range(MAX)];
def fillRemaining(i,j,n):
    x=2;
    for k in range(i):
        mat[k][j]=x;
        x+=1;
def constructMatrix(n):
    right=n-1;
    left=0;
    for i in range(n):
        if(i%2==0):
            mat[i][right]=1;
            fillRemaining(i,right,n);
            right-=1;
        else:
            mat[i][left]=1;
            fillRemaining(i,left,n);
            left+=1;
#driver unicode
n=5;
constructMatrix(n);
for i in range(n):
    for j in range(n):
        print(mat[i][j]),end='');
        print("")