def bits2int():								#public static int bits2int(){

															#	int number;
															#	int currBit;

number = 0										#	number = 0;

currBit = 0									

currBit = get_bit()						#	currBit = get_bit();

while currBit != -1:					#	while (currBit != -1){

number = number «	1						#		number = number << 1;
			
number = currBit + number 		#	number = currBit + number;// building up value

currBit = get_bit()						#		currBit = get_bit();//1,0
															#	}// end of while

return number									#	return number;

															#}// end of bits2int


def get_bit():								#	public static int get_bit(){

user_input=input ('')					#	mips.read_c();
															#	char x = (char) mips.retval();

if user_input =='0'：					#	if (x == '0'){
	
	return 0										#		return 0;
	
elif user_input =='1':				#	}else if(x == '1'){

	return 1 										#		return 1;

else:													#	}else{

	return -1										#		return -1;// error
															# } // end of if statment

result = bits2int()						

print ("Result:", result)
															#	}// end of get_bit