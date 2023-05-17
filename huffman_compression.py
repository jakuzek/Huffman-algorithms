import math

def main():
    with open("for_compression.txt", "r") as file:
        read_file = file.read()
    
    start_length = len(read_file)
    no_duplicates = sorted(list(set(read_file)))
    no_duplicates_length = len(no_duplicates)

    N = math.ceil(math.log2(no_duplicates_length))
    R = (8 - (3 + (N * start_length)) % 8) % 8

    with open("after_compression.txt", "wb") as  results:
        binary1 = ""
        binary2 = ""
        helperArray1 = bytearray()
        helperArray1.append(no_duplicates_length)

        for element in no_duplicates:
            helperArray1.append(ord(element))

        binary_helper = str(bin(R)[2:])
        binary1 += binary_helper.rjust(3, "0")

        for char in read_file:
            binary2_helper = str(bin(no_duplicates.index(char))[2:])
            binary2 += binary2_helper.rjust(N, "0")
        
        binary2 += "1" * R
        binary1 += binary2

        for element in range(0, len(binary1), 8):
            helperArray2 = chr(int(binary1[element:(element+8)], 2))
            helperArray1.append(ord(helperArray2))

        results.write(bytes(helperArray1))

if __name__ == "__main__":
    main()