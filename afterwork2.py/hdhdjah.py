import random

capital = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,ST,U,V,W,X,Y,Z"
small = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
numbers = 1,2,3,4,5,6,7,8,9

for i in range('capital', 'small', 'numbers'):
    computer_choice = random.choice('capital', 'small', 'numbers')
print(computer_choice)