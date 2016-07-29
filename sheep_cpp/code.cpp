// drummer2322
// corbin.mc96@gmail.com
// GCJ <year> <round> <problem>
// <date>

#include <iostream>
#include <string>
#include <set>
#include <cstring>
#include <cstdio>

int main () 
{
	int T, tt, N, num;
	std::cin >> T;
	for (tt = 1; tt <= T; tt++) {
		std::cerr << tt << std::endl;

		std::cin >> N;
		num = N;

		bool digits[10] = {false};
		bool done=false;

		for (int i=1; i<100001; i++) {
			char number[100];
			sprintf(number, "%d", N*i);
			for (int j=0; j<strlen(number); j++) {
				digits[number[j] - '0'] = true;
			}
			done = false;
			for (int j=0; j<10; j++) {
				if (!digits[j]) {
					done = true;
					break;
				}
			}
			if (!done) {
				std::cout << "Case #" << tt << ": " << i*N << std::endl;
				done = true;
				break;
			}
			done = false;
		}
		if (!done) {
			std::cout << "Case #" << tt << ": INSOMNIA" << std::endl;
		}
	}
}
