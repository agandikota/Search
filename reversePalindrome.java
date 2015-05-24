class reversePalindrome{
	public static void main(String[] args){
		String palindrome = "abcde";
		char[] tempArray = new char[palindrome.length()];

		for (int i = palindrome.length() - 1; i >= 0; i--){
			tempArray[palindrome.length() - i - 1] = palindrome.charAt(i);
		}

		String reversed = new String(tempArray);

		StringBuilder sb = new StringBuilder(palindrome);
		System.out.println(sb.reverse());
		System.out.println(reversed);
	}
}
