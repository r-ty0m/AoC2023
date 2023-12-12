#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>

int calculateCardPoints(const std::set<int>& winningNumbers, const std::vector<int>& myNumbers) {
    int points = 0;
    bool firstMatch = true;

    for (int num : myNumbers) {
        if (winningNumbers.find(num) != winningNumbers.end()) {
            if (firstMatch) {
                points = 1;
                firstMatch = false;
            } else {
                points *= 2;
            }
        }
    }

    return points;
}

int main() {
    std::ifstream file("input.txt");
    if (!file) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    } else {
        std::cout << "File found\n";
    }

    std::string line;
    int totalPoints = 0;

    while (std::getline(file, line) && !line.empty()) {
        std::istringstream iss(line);
        std::vector<int> myNumbers;
        std::set<int> winningNumbers;
        int number;
        std::string numbersPart;

        iss >> numbersPart >> numbersPart;

        std::getline(iss, numbersPart, '|');
        std::istringstream winningStream(numbersPart);
        std::cout << "[";

        while (winningStream >> number) {
            winningNumbers.insert(number);
            std::cout << number << " ";
        }

        std::cout << "| ";

        std::getline(iss, numbersPart);
        std::istringstream myNumbersStream(numbersPart);

        while (myNumbersStream >> number) {
            myNumbers.push_back(number);
            std::cout << number << " ";
        }

        std::cout << "]\n";

        totalPoints += calculateCardPoints(winningNumbers, myNumbers);
    }

    std::cout << "Total points: " << totalPoints << std::endl;

    file.close();
    return 0;
}
