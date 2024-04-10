from utils.openai import client


def main():
    chat_completion = client.chat.completions.create(
        # model="gpt-3.5-turbo",
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": "hello",
            },
        ],
    )

    print(chat_completion)


if __name__ == "__main__":
    main()
