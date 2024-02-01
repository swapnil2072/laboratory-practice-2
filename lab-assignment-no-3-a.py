class SelectionSort:
    def __init__(self):
        self.array = []

    def add_element(self, element):
        self.array.append(element)

    def selection_sort(self):
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.array[j] < self.array[min_index]:
                    min_index = j

            self.array[i], self.array[min_index] = self.array[min_index], self.array[i]

    def display_array(self):
        print("Sorted array:", self.array)


def main():
    selection_sort = SelectionSort()

    while True:
        print("----------------Selection Sort----------------------")
        print("1. Add Element.")
        print("2. Perform Selection Sort.")
        print("3. Exit.")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            element = int(input("Enter the element: "))
            selection_sort.add_element(element)
            print("Element added:", element)
            selection_sort.display_array()

        elif choice == 2:
            selection_sort.selection_sort()
            selection_sort.display_array()

        elif choice == 3:
            print("End of the program")
            break

        else:
            print("Invalid choice!")

        print()


if __name__ == "__main__":
    main()
