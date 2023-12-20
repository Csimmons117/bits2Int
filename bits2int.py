#public static int bits2int(){
#	int currBit;
#	int number;
#	number = 0;
#	currBit = get_bit();


#	while (currBit != -1){
#		number = number << 1;
#		number = currBit + number;// building up value
#		currBit = get_bit();//1,0
	
		
#	}// end of while 
#	return number;


#}// end of bits2int
	
	
#	public static int get_bit(){
 
#	mips.read_c();
#	char x = (char) mips.retval();
#	if (x == '0'){
#		return 0;
#	}else if(x == '1'){
#		return 1;
#	}else{
#		return -1;// error 
#	}// end of get_bit
