#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <set>
#include <map>

std::vector<std::pair<std::set<int>, std::vector<int>>> readCards(const std::string& filename) {
    std::ifstream file(filename);
    std::vector<std::pair<std::set<int>, std::vector<int>>> cards;
    std::string line;

    if (!file) {
        std::cerr << "Error opening file" << std::endl;
        return cards;
    }

    while (std::getline(file, line) && !line.empty()) {
        std::istringstream iss(line);
        std::set<int> winningNumbers;
        std::vector<int> myNumbers;
        int number;
        std::string temp;
        char separator;

        iss >> temp >> temp;

        std::getline(iss, temp, '|');
        std::istringstream winningStream(temp);
        while (winningStream >> number) {
            winningNumbers.insert(number);
        }

        std::getline(iss, temp);
        std::istringstream myNumbersStream(temp);
        while (myNumbersStream >> number) {
            myNumbers.push_back(number);
        }

        cards.emplace_back(winningNumbers, myNumbers);
    }

    file.close();
    return cards;
}

int countMatches(const std::set<int>& winningNumbers, const std::vector<int>& myNumbers) {
    int matches = 0;
    for (int num : myNumbers) {
        if (winningNumbers.find(num) != winningNumbers.end()) {
            matches++;
        }
    }
    return matches;
}

int main() {
    auto cards = readCards("input.txt");
    std::vector<int> cardCopies(cards.size(), 1); 
    std::map<int, int> totalCards;

    for (size_t i = 0; i < cards.size(); ++i) {
        int matches = countMatches(cards[i].first, cards[i].second);
        for (int j = 1; j <= matches && i + j < cards.size(); ++j) {
            cardCopies[i + j] += cardCopies[i];
        }
        totalCards[i + 1] = cardCopies[i];
    }

    int totalScratchcards = 0;
    for (auto& pair : totalCards) {
        totalScratchcards += pair.second;
        std::cout << "Card " << pair.first << ": " << pair.second << " instance(s)" << std::endl;
    }

    std::cout << "Total scratchcards: " << totalScratchcards << std::endl;

    return 0;
}
