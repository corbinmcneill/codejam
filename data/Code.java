import java.util.ArrayList;
import java.util.Scanner;

public class Code {
	public static void main (String[] args) {
		Scanner in = new Scanner(System.in);
		int T = in.nextInt();

		for(int tt=1; tt<=T; tt++) {

			int number_of_files = in.nextInt();
			int cd_size = in.nextInt();
			ArrayList<Integer> int_sizes = new ArrayList<Integer>();
			for (int i=0; i<number_of_files; i++) {
				int_sizes.add(in.nextInt());
			}
			int number_of_cds = 0;
			while (!int_sizes.isEmpty()) {
				if (int_sizes.size() > 1 && int_sizes.get(0) + int_sizes.get(int_sizes.size()-1) <= cd_size) {
					int_sizes.remove(0);
				}
				int_sizes.remove(int_sizes.size()-1);
				number_of_cds+=1;
			}
			System.out.println("Case #"+tt+": "+number_of_cds);
			
		}
	}
}
