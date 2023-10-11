def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")

        fruit_list.reverse()
        print(f"Reverse: {fruit_list}")

        fruit_list.append("orange")
        print(f"Append Orange: {fruit_list}")

        apple_index = fruit_list.index("apple")
        print(f"Apple Index: {apple_index}")

        # fruit_list.insert(1, "cherry")
        # print(f"Inserted Cherry before Apple: {fruit_list}")

        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert cherry: {fruit_list}")

        fruit_list.remove("banana")
        print(f"Banana Removed: {fruit_list}")

        fruit_list.pop()
        print(f"Last element removed: {fruit_list}")

        fruit_list.sort()
        print(f"Sorted: {fruit_list}")

        fruit_list.clear()
        print(f"Cleared Fruit List: {fruit_list}")


    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")


if __name__ == "__main__":
    main()
