public class NumbersExample{

	public static void main(String[] args){

		/*Working with integers*/
		int aNumber = 20;
		int aNumberHex = 0x20;
		int aNumberBin = 0b110;
		System.out.println("Number aNumber value is: " + aNumber);
		System.out.println("Expressing aNumber as binary: " + aNumberBin);
		System.out.println("Expressing aNumber as hexadecimal: " + aNumberHex);	
	
		/*Working with bytes*/
		byte aByte = 127;
		System.out.println("aByte value is: " + aByte);

		/*Working with float and double*/
		double aDouble = 1.5D;
		System.out.println("Double aDouble is: " + aDouble);
		float aFloat = 1.3F;
		System.out.println("Float aFloat is: " + aFloat);
		//aFloat = aDouble;
		//System.out.println("Now aFloat value is: " + aFloat);
		aDouble = aFloat;
		System.out.println("Now aDouble value is: " + aDouble);
		aDouble = 3.45e2;
		//aFloat = 3.45e2; this is a wrong assignment
		aFloat = 345;	
		System.out.println("aDouble is " + aDouble + " while aFloat is " + aFloat);	

		/*Working with underscores in numbers*/
		long hexUnderScores = 0x11_AA_55_60;
		System.out.println("Value of hexUnderScores is: " + hexUnderScores);
	
		/*Some chars*/
		char aChar = '\u0A9f';
		System.out.println("aChar is: " + aChar);	
	}

}

