import json
from utils.openai import client


def generate_reference_for_claim(claim):
    # Querying LLM to generate a reference for the claim
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"Given the following claim: '{claim}', provide a reliable reference or source that supports this claim."}
    ]
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
    )
    return chat_completion.choices[0].message.content


def process_claims_with_references(results):
    for entry in results:
        claims_with_references = []

        # For each claim, generate one or more references
        for claim in entry["claims"]:
            references = []
            for _ in range(3):  # Attempt to generate 3 references
                reference = generate_reference_for_claim(claim)
                references.append(reference)

            claims_with_references.append({
                "claim": claim,
                "references": references
            })

        # Add the generated references to the entry
        entry["claims_with_references"] = claims_with_references

    return results


def save_to_json(results, filename="output_with_references.json"):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)


def load_dataset(filename="output.json"):
    with open(filename, 'r') as f:
        return json.load(f)


def main():
    # Load previously processed data with claims
    results = load_dataset("output.json")

    # Process claims to generate references
    results_with_references = process_claims_with_references(results)

    # Save the results with references to a new JSON file
    save_to_json(results_with_references, "output_with_references.json")


if __name__ == "__main__":
    main()
