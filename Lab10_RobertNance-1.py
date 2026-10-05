"""Word Counter, Robert Nance, count the number of words in a given amount of text, 10/04/26"""

from pathlib import Path
import string

class WordAnalyzer:
    def __init__(self, filepath):
        self.__filepath = Path(filepath)
        self.__frequency = {}

    def process_file(self):
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError

            translator = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower().translate(translator)

                    words = line.split()

                    for word in words:
                        if word in self.__frequency:
                            self.__frequency[word] += 1
                        else:
                            self.__frequency[word] = 1

            return True

        except FileNotFoundError:
            print(f"File not found: {self.__filepath}")
            return False

    def print_report(self):
        words = sorted(self.__frequency.keys())

        for word in words:
            print(f"{word:<6} :: {self.__frequency[word]}")

def main():
    files = {
        "1": Path("princess_mars.txt"),
        "2": Path("tarzan.txt"),
        "3": Path("treasure_island.txt"),
        "4": Path("monte_cristo.txt")
    }

    file_names = {
        "1": "A Princess of Mars",
        "2": "Tarzan",
        "3": "Treasure Island",
        "4": "The Count of Monte Cristo"
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. A Princess of Mars")
        print("2. Tarzan")
        print("3. Treasure Island")
        print("4. The Count of Monte Cristo")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nGoodbye!")
            break

        if choice not in files:
            print("\nInvalid choice, select choices 1-5.")
            input("\nPress Enter to return to the menu")
            continue

        filepath = files[choice]
        display_name = file_names[choice]

        print (f"\nProcessing '{filepath.name}'")

        analyzer = WordAnalyzer(filepath)

        if analyzer.process_file():
            print()
            analyzer.print_report()

        input("\nPress Enter to return to the menu")

if __name__ == "__main__":
    main()