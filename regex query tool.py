import re

def regex_query_tool():
    print("Regex Query Tool")
    print("----------------")

    # Get the source text and regex pattern from the user
    source_text = input("Enter the source text: ")
    regex_pattern = input("Enter the regex pattern: ")

    try:
        # Compile the regex pattern
        regex = re.compile(regex_pattern)

        # Search for matches in the source text
        matches = regex.findall(source_text)

        if matches:
            print("Matches found:")
            for match in matches:
                print(match)
        else:
            print("No matches found.")
    
    except re.error as e:
        print("Regex error: ", e)

if __name__ == "__main__":
    regex_query_tool()
