/*
drummer2322
corbin.mc96@gmail.com
GCJ <year> <round> <problem>
<date>
Status: can be optimized by swithing vector to map
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int main () 
{
	int L, D, N;

	std::cin >> L;
	std::cin >> D;
	std::cin >> N;
	std::cin.ignore();

	std::string dictionary [D];
	for (int i=0; i<D; i++) {
		std::getline(std::cin, dictionary[i]);
	}

	for (int tt=1; tt<=N; tt++) {
		std::cerr << tt << std::endl;

		std::string case_word;
		std::getline(std::cin, case_word);

		int current_letter = 0;
		
		std::vector <int> invalid_indexes;

		while (case_word.length() > 0) {
			std::vector <char> required_letters;
			if (case_word[0] != '(') {
				required_letters.push_back(case_word[0]);
				case_word.erase(case_word.begin());
			}
			
			else {
				std::string::iterator closing_parenthesis = std::find(case_word.begin(), case_word.end(), ')');
				std::string::iterator p = case_word.begin()+1;
				while (p != closing_parenthesis) {
					required_letters.push_back(*(p++));
				}
				case_word.erase(case_word.begin(), closing_parenthesis+1);
			}

			for (int dictionary_word=0; dictionary_word<D; dictionary_word++) {
				if (std::find(invalid_indexes.begin(), invalid_indexes.end(), dictionary_word) != invalid_indexes.end()) {
					continue;				
				}
				if (std::find(required_letters.begin(), required_letters.end(), dictionary[dictionary_word][current_letter]) == required_letters.end()) {
					invalid_indexes.push_back(dictionary_word);
				}
			}

			current_letter++;
		}
		std::cout << "Case #" << tt << ": " << D - invalid_indexes.size() << std::endl;
	}
}
