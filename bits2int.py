def bits2int():								

															
															

number = 0										
currBit = 0									

currBit = get_bit()						

while currBit != -1:					

number = number «	1						
			
number = currBit + number 		

currBit = get_bit()						
															

return number									

															


def get_bit():								

user_input=input ('')					
															

if user_input =='0'：					
	
	return 0										
	
elif user_input =='1':				

	return 1 										

else:													

	return -1										
															

result = bits2int()						

print ("Result:", result)
															