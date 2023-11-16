import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

# Function to make GET requests and filter titles with more than 6 words
def filtered_titles():
    response = requests.get(base_url)

    if response.status_code == 200:
        posts = response.json()
        filtered_titles = []

        for post in posts:
            if len(post['title'].split()) <= 6:
                filtered_titles.append(post['title'])
        return filtered_titles

    else:
        print(f"GET request failed with status code {response.status_code}")

# Function to make GET requests and filter out results with more than 3 lines of description
def filtered_body():
    response = requests.get(base_url)
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = []

        for post in posts:
            lines = post["body"].splitlines()
            if len(lines) <= 3:
                filtered_posts.append(post["body"])

        return filtered_posts
    else:
        return f"GET request failed with status code {response.status_code}"

# Function to make POST request  
def create_post(title, body, userId):
    data = {'title': title, 'body': body, 'userId': userId}
    response = requests.post(base_url, json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return f"POST request failed with status code {response.status_code}"

# Function to make PUT request        
def update_post(post_id, title, body, userId):
    url = f"{base_url}/{post_id}"
    data = {'title': title, 'body': body, 'userId': userId}
    response = requests.put(url, json=data)
    if response.status_code == 200:
        return response.json()
    else:
         return f"PUT request failed with status code {response.status_code}"

# Function to make DELETE request
def delete_post(post_id):
    url = f"{base_url}/{post_id}"
    response = requests.delete(url)

    if response.status_code == 200:
        return f"DELETE request successful."
    else:
        return f"DELETE request failed with status code {response.status_code}"


# Example usage for filtered_titles function
filtered_titles_result = filtered_titles()
print("Titles with 6 or fewer words:")
print(filtered_titles_result)

# Example usage for filtered_body function
filtered_body_result = filtered_body()
print("\nPosts with 3 or fewer lines of description:")
print(filtered_body_result)

# Example usage for create_post function
created_post = create_post("New Title", "This is the body of the new post.", 1)
if created_post:
    print("\nNew Post Created:")
    print(created_post)

# Example usage for update_post function
update_post_result = update_post(1, "Updated Title", "This is the updated body of the post.", 1)
print("\nUpdated post:")
print(update_post_result)
print("\n")

# Example usage for delete_post function
delete_post_result = delete_post(1)
print(delete_post_result)
