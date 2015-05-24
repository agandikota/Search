class Robot{
	public static int paths(int n, int r, int d, int count){
		if (r == n && d == n){
			return count + 1;
		}
		else if (r == n){
			return paths(n, r, d + 1, count + 0);
		}
		else if (d == n){
			return paths(n , r + 1, d, count + 0);
		}
		else{
			return paths(n, r, d + 1, count + 0) + 
			paths(n , r + 1, d, count + 0);
		}

	}
	public static void main(String[] args) {
		int n  = 8;
		System.out.println(paths(n-1,0,0,0));
	}
}