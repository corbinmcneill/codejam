#include <string>
#include <iostream>

int main()
{
	int number_of_cases;
	std::cin >> number_of_cases; 
	
	//clear newline ending
	std::cin.ignore();

	for (int i=1; i<=number_of_cases; i++) {
		std::cerr << i << std::endl;

		std::string input = "";
		std::getline(std::cin, input);

		while (true) {
			int pos = input.find_last_of(" ");
			if (pos == -1) {
				std::cout << input;
				break;
			}
			std::cout << input.substr(pos+1)+" ";
			input.resize(pos);
		}
		std::cout << std::endl;
	}
	return 0;
}
