#include <iostream>

int main() 
{
	int board_size, win_length;
	std::cin >> board_size;
	std::cin >> win_length;
	std::cin.ignore();

	char **old_board = new char* [board_size];
	for (int i=0; i<board_size; i++) {
		old_board[i] = new char [board_size];
		for (int j=0; j<board_size; j++) {
			std::cin.get(old_board[i][j], 1);
		}
		std::cin.ignore();
	}

	char **new_board = new char*[board_size];
	for (int i=0; i<board_size; i++) {
		new_board[i] = new char [board_size];
		int index=board_size-1;
		for (int j=board_size; j>=0; j--) {
			if (old_board[i][j]=="R") {
				new_board[i][index] = "R";
				index--;
			}
			else if (old_board[i][j]=="B") {
				new_board[i][index] = "B";
				index--;
			}
		}
	}
}
