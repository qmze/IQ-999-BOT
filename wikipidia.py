import wikipedia

def get_wikipedia_summary(query):
    # Use Wikipedia API to get a summary of the query
    try:
        summary = wikipedia.summary(query, sentences=1)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation by selecting the first option
        summary = wikipedia.summary(e.options[0], sentences=1)
        return summary
    except wikipedia.exceptions.PageError:
        return None

def main():
    print("Welcome to the SimpleBot!")

    while True:
        user_input = input("Ask me a question (type 'exit' to end): ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Check for specific questions about capital cities
        if "capital city of" in user_input.lower():
            # Extract the country name from the question
            country_name = user_input.lower().replace("capital city of", "").strip()
            query = f"Capital of {country_name}"
        else:
            query = user_input

        # Use the modified query to fetch Wikipedia information
        context = get_wikipedia_summary(query)

        if context:
            print("Answer:", context)
        else:
            print("I couldn't find information related to your question.")

if __name__ == "__main__":
    main()
