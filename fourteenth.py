from google import genai


client = genai.Client(api_key ="AIzaSyDFC6dgyBQKj96VERy1wdgHvTKmFQmed8c")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="why light bend and not just change its speed"
)
print(response.text)

