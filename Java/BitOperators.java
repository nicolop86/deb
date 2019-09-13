public class BitOperators{

	public static void main(String[] args){
		int val = 0x0012;
		System.out.println("val " + val);
		int mask = 0x000F;
		System.out.println("Mask " + mask);
		System.out.println("val AND bitmask " + (val & mask));

		String valBinary = Integer.toBinaryString(val);
		String maskBinary = Integer.toBinaryString(mask);
		System.out.println(valBinary);
		System.out.println(maskBinary);	

		val = val << 1;
		System.out.println("After signed left shift " + val);
		val = val >> 1;
		System.out.println("After signed right shift " + val);	
		val = val >>> 1;
		System.out.println("After unsigned right shift " + val);
		val = val >> 1;
		System.out.println("After another signed right shift " + val);
	}
}
