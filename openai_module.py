import openai

openai.api_key = open("key.txt", "r").read()

def do_stuff(prompt_order, max_tokens=8, n=1, stop=None, temperature=0.5):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_order,
        max_tokens=max_tokens,
        n=n,
        stop=stop,
        temperature=temperature,
    )
    response_text = response.choices[0].text
    return response_text