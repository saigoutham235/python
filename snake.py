M = 3
N = 3

def printf(mat):
    
	global M,N
    
		for i in range(M):
        
			if i%2 == 0:
            
				for j in range(N):
                
			                	print(str(mat[i][j]),
			  
                          	end = " ")
        
			else:
            
				for j in range(N -1,-1,-1):
                 
				 	print(str(mat[i][j]),  
                          
					end = " ")

mat = [[ 10, 20, 30 ], 
      
           [ 15, 25, 35 ], 
      
           [ 27, 29, 37 ]] 

       

printf(mat)
  