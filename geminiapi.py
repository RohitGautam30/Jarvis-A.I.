import google.generativeai as genai

# Configure the API key
# IMPORTANT: Replace "YOUR_API_KEY" with your actual API key
genai.configure(api_key="")

# Create the model
model = genai.GenerativeModel('gemini-1.5-flash')

# Send a prompt to the model
response = model.generate_content("where is iit jammu located")

# Print the response

print(response.text)
