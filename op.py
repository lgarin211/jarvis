import openai

# Setel kunci API
openai.api_key = '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'

# Fungsi untuk membuat permintaan ke ChatGPT
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Ganti dengan model yang Anda inginkan
        prompt=prompt,
        max_tokens=50,  # Ganti sesuai kebutuhan
        temperature=0.7,  # Ganti sesuai kebutuhan
        n=1,
        stop=None
        )
    return response.choices[0].text.strip()

# Contoh penggunaan
prompt = "Halo, apa kabar?"
response = generate_response(prompt)
print(response)
