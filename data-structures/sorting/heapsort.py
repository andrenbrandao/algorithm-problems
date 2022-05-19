class MaxHeap:
    def __init__(self, arr: list) -> None:
        self.heap = arr
        self.size = len(arr)
        self.max_size = len(arr)
        self.__build_heap()

    def __build_heap(self):
        for i in range(self.size // 2, -1, -1):
            self.__sift_down(i)

    def sort(self):
        for i in range(self.size - 1, -1, -1):
            self.heap[i] = self.extract_max()

    def insert(self, value: int) -> None:
        """Insert a new element to the heap

        Args:
            value (int): A number

        Raises:
            Exception: When the heap is full
        """
        if self.size >= self.max_size:
            raise Exception("Heap is full")

        position = self.size
        self.heap[position] = value
        self.size += 1
        self.__sift_up(position)

    def extract_max(self) -> int:
        """Extracts the element with highest priority.
        i) Moves the last leaf to the root.
        ii) Bubble down the root until the element at the top is the new maximum
        iii) Return the element which was the max


        Returns:
            int: Value of element

        Raises:
            Expection: When heap is empty
        """
        if self.size == 0:
            raise Exception("Heap is empty")

        max_element = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.__sift_down(0)
        self.size -= 1
        return max_element

    def remove(self, pos: int) -> int:
        """Removes the element of the position i

        Args:
            pos (int): Position of element to be removed

        Returns:
            int: Value of element removed
        """
        self.heap[pos] = float("+inf")
        self.__sift_up(pos)
        self.extract_max()

    def change_priority(self, pos: int, value: int) -> None:
        """Changes the priority of an element

        Args:
            pos (int): Position of element
            value (int): New priority value
        """
        old_value = self.heap[pos]
        self.heap[pos] = value

        if value > old_value:
            self.__sift_up(pos)
        else:
            self.__sift_down(pos)

    def __sift_up(self, position: int) -> None:
        """Bubble up the elements to keep the heap constraints

        Args:
            position (int): Position of the inserted element
        """

        if position == 0:
            return

        parent_pos = self.__parent(position)

        if self.heap[position] > self.heap[parent_pos]:
            self.__swap(parent_pos, position)
            self.__sift_up(parent_pos)

    def __sift_down(self, position: int) -> None:
        """Bubble down the elements to keep the heap constraints

        Args:
            position (int): Position of the element to be bubbled down
        """

        # Return if there are no more children to compare to

        max_index = position
        left_child_pos = self.__left_child(position)
        if (
            left_child_pos < self.size
            and self.heap[max_index] < self.heap[left_child_pos]
        ):
            max_index = left_child_pos

        right_child_pos = self.__right_child(position)
        if (
            right_child_pos < self.size
            and self.heap[max_index] < self.heap[right_child_pos]
        ):
            max_index = right_child_pos

        if max_index != position:
            self.__swap(max_index, position)
            self.__sift_down(max_index)

    def __parent(self, pos: int) -> int:
        """Returns the parent position of a given element

        Args:
            pos (int): Position of element to find parent

        Returns:
            int: Position of parent
        """
        return (pos - 1) // 2

    def __swap(self, pos1: int, pos2: int) -> None:
        """Swaps two elements

        Args:
            pos1 (int): First element position
            pos2 (int): Second element position
        """
        self.heap[pos1], self.heap[pos2] = self.heap[pos2], self.heap[pos1]

    def __left_child(self, pos: int) -> int:
        """Returns left child position

        Args:
            pos (int): Current element position

        Returns:
            int: Position of the left child
        """
        return 2 * pos + 1

    def __right_child(self, pos: int) -> int:
        """Returns right child position

        Args:
            pos (int): Current element position

        Returns:
            int: Position of the right child
        """
        return 2 * pos + 2

    def __str__(self) -> str:
        return str(self.heap[: self.size])


if __name__ == "__main__":
    arr = [9, 13, 2, 4, 8, 3, 2, 1, 5, 7, 0, 3, 2, 1]
    heap = MaxHeap(arr)
    print(heap)
    heap.sort()
    print(arr)
