import requests

# Base URL for the API
base_url = "http://localhost:8000"

# Test data
todo_data = {
    "description": "Test Todo Description",
    "short_description": "Test Short Description",
    "tags": "test, todo",
    "title": "Test Todo Title"
}

# Helper function to print response nicely
def print_response(response):
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.json())

# Test Case 1: GET all todos
def test_get_all_todos():
    print("GET all todos:")
    response = requests.get(f"{base_url}/todos/all")
    print_response(response)

# Test Case 2: POST new todo
def test_create_todo():
    url = "http://localhost:8000/todos"  # API URL'si, gerektiği şekilde güncelleyin
    data = {
        "description": "Testdescription",
        "short_description": "Testshortdescription",
        "tags": "testtag",
        "title": "Testtitle"
    }

    response = requests.post(url, data=data)
    print_response(response)



# Test Case 3: GET specific todo
def test_get_todo():
    print("\nGET specific todo:")
    response = requests.get(f"{base_url}/todos/U8xfuGoTQtwS2YH4Q1kO")
    print_response(response)

# Test Case 4: DELETE specific todo
def test_delete_todo():
    print("\nDELETE specific todo:")
    response = requests.delete(f"{base_url}/todos/U8xfuGoTQtwS2YH4Q1kO")
    print_response(response)

# Test Case 5: PUT (Update) specific todo
def test_update_todo():
    # Güncellenecek todo'nun ID'sini belirtin
    todo_id = "U8xfuGoTQtwS2YH4Q1kO"  # Güncellenecek todo'nun gerçek ID'siyle değiştirin

    # Güncellenecek todo için yeni verileri belirtin
    update_url = f"http://localhost:8000/todos/{todo_id}"  # Güncellenecek todo'nun URL'si
    update_data = {
        "description": "Updated test description",
        "short_description": "Updated test short description",
        "tags": "updated,test,tag",  # Yeni etiketler
        "title": "Updated test title"  # Yeni başlık
    }

    # Güncelleme isteğini gönderin
    update_response = requests.put(update_url, data=update_data)
    print_response(update_response)


# Main function to run all test cases
def run_all_tests():
    test_get_all_todos()
    test_create_todo()
    test_get_todo()
    test_update_todo()
    test_delete_todo()

# Run all tests
run_all_tests()
