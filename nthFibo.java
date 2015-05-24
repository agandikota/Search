import java.util.*;
import java.math.*;

class nthFibo{
	public static BigInteger myNthFibo(int n){
		BigInteger a = new BigInteger("0"), b = new BigInteger("1");
		int i = 1;

		while (i <= n){
			BigInteger temp_a = a;
			a = b;
			b = b.add(temp_a);
			i++;
		}
		return a;
	}


	public static void main(String[] args){
		Scanner s = new Scanner(System.in);
		while (s.hasNextLine()){
			int n = s.nextInt();
			System.out.println(myNthFibo(n));
		}
		
	}
}