# Chat with openai api

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Set your openai key

- rename `openai_key.example.yaml` to `openai_key.yaml`
- import client with `from utils.openai import client`

Note that you should not add your openai key to your git repo. And if you have commited your key into the git repo, you have to renew your key, since the files added to the git repo are very hard to delete from the git.

If you want to switch between multiple keys, you can write multiple `yaml` files and create client with `load_client` func as following:

```python
from utils.openai import load_client

client = load_client('<path-to-your-key-file>')
```

### chat with openai model

Do what you want with the `client`. For example:

```python
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
```
