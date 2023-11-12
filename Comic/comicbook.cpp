#include <iostream>
#include <vector>
#include <string>


class ComicBook{
public:
    std::string title;
    int quantity;
    double price;

    ComicBook(const std::string& t, int q, double p) : title(t), quantity(q), price(p) {}

    double calculateTotal() const {
        return quantity * price;
    }
};

void displayMenu() {
    std::cout << "\nComic Book Store Inventory System\n";
    std::cout << "1. Add a new comic book\n";
    std::cout << "2. Display current inventory\n";
    std::cout << "3. Calculate total value of inventory\n";
    std::cout << "4. Exit menu\n";
    std::cout << "Enter your choice: ";
}

void addComic(std::vector<ComicBook>& inventory) {
    std::string title;
    int quantity;
    double price;

    std::cout <<"Enter title: ";
    std::cin.ignore(); // this will ignore previous characters
    std::getline(std::cin, title);

    std::cout << "Enter Quantity: ";
    std::cin >> quantity;

    std::cout << "Enter price: ";
    std::cin >> price;

    inventory.emplace_back(title, quantity, price);
    std::cout << "Newly entered comic book: '" << title << "' added to inventory for a total of: $" << price << "\n";
}

void displayInventory(const std::vector<ComicBook>& inventory) {
    std::cout << "\nInventory:\n";
    for (const auto& comic : inventory) {
        std::cout << "Title: " << comic.title << ", Quantity: " << comic.quantity << ", Price: $" << comic.price << "\n";

    }
}

// this will calculate the total inventory value

void calculateTotalInventoryValue(const std::vector<ComicBook>& inventory) {
    //I had to initialize the totalValue variable with an initial value of 0.0
    // in order to be able to perform the proper calculations
    double totalValue = 0.0;
    for (const auto& comic : inventory) {
        totalValue += comic.calculateTotal();
    }
    // the << totalValue << portion is concatonating variables within the text
    std::cout << "Total inventory value: $" << totalValue << "\n";
}

// Here is the main portion of the program 
int main() {
    std::vector<ComicBook> inventory;

    // making the choice variable in this case an integer makes it so that only 
    // valid integers are able to be inputted
    int choice;

    // this do-while loop goes until the user inputs '4' into the program, and 'exits' the program

    do {
        displayMenu();
        std::cin >> choice;
        
        switch (choice) {
            case 1:
                addComic(inventory);
                break;
            case 2:
                displayInventory(inventory);
                break;
            case 3:
                calculateTotalInventoryValue(inventory);
                break;
            // this is the event that prompts the user to exit the program
            case 4:
                std::cout << "Goodbye!\n";
                break;
            // if none of the valid options are chosen, the defaul will print out and the while loop will continue
            default:
                std::cout << "Invalid Choice, please choose again.\n";
        }
    } while (choice != 4);

    return 0;
}