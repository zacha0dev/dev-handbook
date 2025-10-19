[← Back to Home](../README.md)

# 3F - APIs and Web Connections: Talking to the Internet

Now that your programs can read and write data, it’s time to learn how they can **communicate with the world**.  
The bridge between local code and global information is called an **API** - an *Application Programming Interface.*

APIs are how apps talk to each other.  
They let your program fetch weather, stock prices, calendar events, or even chat with AI - all through structured requests and responses.

---

### 1. What Is an API?

An API is like a **menu** at a restaurant:  
you don’t walk into the kitchen - you ask for something, and the server brings it back.

When your app talks to an API:
1. It sends a **request** - asking for data or action.
2. The server receives it, processes it, and sends a **response**.
3. Your program reads that response (usually JSON) and uses it.

---

### 2. The Basic Flow

```
Your Code  →  API Request  →  Internet  →  API Server  →  JSON Response  →  Your Code
```

This is just another version of **input → process → output**, but now it’s across the web.

---

### 3. Making Your First API Call

Let’s use Python’s built-in `requests` library to fetch data from a public API.

**Example: Getting a random joke**
```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")

if response.status_code == 200:
    joke = response.json()
    print(joke["setup"])
    print(joke["punchline"])
else:
    print("Error:", response.status_code)
```

This simple code:
- Connects to a web address (URL)
- Gets back JSON data
- Reads and prints it out

---

### 4. Understanding JSON Responses

Most APIs send responses in **JSON format**, just like what you’ve already learned to store locally.

**Example Response**
```json
{
  "setup": "Why did the developer go broke?",
  "punchline": "Because they used up all their cache!"
}
```

Your code can easily extract values using dictionary keys - `joke["setup"]`.

---

### 5. APIs With Authentication

Some APIs require an **API key** - like a password for your program.

```python
headers = {"Authorization": "Bearer YOUR_API_KEY"}
response = requests.get("https://api.example.com/data", headers=headers)
```

Keep keys safe using environment variables or a `.env` file - never hardcode them in public code.

---

### 6. Using API Data in a Real Project

Once you know how to make requests, you can integrate them anywhere.

**Example: Weather Widget**
```python
import requests

API_KEY = "your_openweathermap_key"
city = "Tampa"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=imperial"

data = requests.get(url).json()
temp = data["main"]["temp"]
desc = data["weather"][0]["description"]

print(f"{city}: {temp}°F, {desc}")
```

This could feed data into your personal dashboard or Raspberry Pi display.

---

### 7. Error Handling and Reliability

APIs sometimes fail - network issues, timeouts, or bad responses.  
Always add checks and fallbacks.

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except Exception as e:
    print("Error connecting to API:", e)
```

Handling errors gracefully makes your code reliable in the real world.

---

### 8. Key Takeaways
- APIs connect your code to the web.  
- Use `requests.get()` to retrieve data from URLs.  
- Most responses come in JSON format.  
- Protect your API keys.  
- APIs power everything from dashboards to smart homes.

