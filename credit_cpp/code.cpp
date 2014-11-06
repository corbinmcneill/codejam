#include <iostream>

int main()
{
	int number_of_cases;
	std::cin >> number_of_cases;
	std::cin.ignore();

	for (int case_number=1; case_number<=number_of_cases; case_number++) {
		std::cerr << case_number << std::endl;
		int amount_of_money;
		int number_of_store_items;
		std::cin >> amount_of_money;
		std::cin.ignore();
		std::cin >> number_of_store_items;
		std::cin.ignore();

		int *store_items;
		store_items = new int [number_of_store_items];

		for (int store_item_number=0; store_item_number<number_of_store_items; store_item_number++) {
			std::cin >> store_items[store_item_number];
		}
		std::cin.ignore();

		for (int i=0; i<number_of_store_items; i++) {
			for (int j=i+1; j<number_of_store_items; j++) {
				if (store_items[i] + store_items[j] == amount_of_money) {
					std::cout << "Case #" << case_number << ": " << i+1 << " " << j+1 << std::endl;
					goto ending;
				}
			}
		}
		std::cerr << "FAIL" << std::endl;
ending:;
	}
	return 0;
}
