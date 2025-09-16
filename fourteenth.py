from google import genai


client = genai.Client(api_key ="AIzaSyDFC6dgyBQKj96VERy1wdgHvTKmFQmed8c")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="why light bend and not just change its speed with diagram"
)
print(response.text)

# API key is a type of password with which we can use AI in various softwares also and in programming.
