import json
from utils.openai import client


def generate_response(query):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Generate a response to the following query: {query}"}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    return chat_completion.choices[0].message.content


def split_claims(response):
    # Querying LLM to split claims
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Your response is: {response}. If there are multiple claims in this response, please break them down into separate claims."}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    return chat_completion.choices[0].message.content


def process_data(data):
    results = []

    for entry in data:
        query = entry["query"]

        # Step 1: Generate response for the query
        response_1 = generate_response(query)

        # Step 2: Check if the response contains multiple claims and split if needed
        claims = [response_1]
        if "and" in response_1 or "," in response_1:  # A simple check for multiple claims
            response_2 = split_claims(response_1)
            claims = response_2.split("\n")  # Assume that the claims are returned in separate lines

        # Store the results for this entry
        results.append({
            "query": query,
            "initial_response": response_1,
            "claims": claims
        })

    return results


def save_to_json(results, filename="output.json"):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)


def load_dataset(filename="input_data.json"):
    with open(filename, 'r') as f:
        return json.load(f)


def main():
    # Load dataset from a JSON file
    dataset = load_dataset("input_data.json")

    # Process the dataset
    results = process_data(dataset)

    # Save the results to a JSON file
    save_to_json(results, "output.json")


if __name__ == "__main__":
    main()
