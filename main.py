from data_structures.interval_tree import IntervalTree

def main():
    tree = IntervalTree()

    n = int(input("How many intervals do you want to insert? "))

    for _ in range(n):
        start = int(input("Enter interval start: "))
        end = int(input("Enter interval end: "))
        tree.add((start, end))

    query_start = int(input("\nEnter query start: "))
    query_end = int(input("Enter query end: "))
    query = (query_start, query_end)

    overlaps = tree.find_overlaps(query)

    print(f"\nOverlapping intervals with {query}:")
    for interval in overlaps:
        print(interval)

if __name__ == "__main__":
    main()
