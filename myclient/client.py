import requests

class Client:
    def __init__(self):
        # self.base_url = 'http://127.0.0.1:8000'
        self.base_url = 'https://sc212yw.pythonanywhere.com'
        self.access_token = None

    def register(self):
        username = input("Username: ")
        email = input("Email: ")
        password = input("Password: ")

        response = requests.post(f'{self.base_url}/register/', json={
            'username': username,
            'email': email,
            'password': password
        })
        print(response.json())

    def login(self):
        username = input("Username: ")
        password = input("Password: ")

        response = requests.post(f'{self.base_url}/login/', json={
            'username': username,
            'password': password
        })
        if response.status_code == 200:
            data = response.json()
            self.access_token = data['access']
            print("Login successful!")
        else:
            print("Login failed:", response.json())

    def logout(self):
        self.access_token = None
        print("Logged out successfully.")

    def list_modules(self):
        response = requests.get(f'{self.base_url}/modules/')
        print(response.json())

    def view_professors(self):
        response = requests.get(f'{self.base_url}/professors/')
        print(response.json())

    def view_average(self):
        professor_id = input("Professor ID: ")
        module_code = input("Module Code: ")

        response = requests.get(f'{self.base_url}/professors/{professor_id}/module/{module_code}/average/')
        print(response.json())

    def rate_professor(self):
        if not self.access_token:
            print("Please login first!")
            return

        professor_id = input("Professor ID: ")
        module_code = input("Module Code: ")
        year = input("Year: ")
        semester = input("Semester: ")
        rating = input("Rating (1-5): ")

        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = requests.post(f'{self.base_url}/rate/', json={
            'professor_id': professor_id,
            'module_code': module_code,
            'year': year,
            'semester': semester,
            'rating': rating
        }, headers=headers)
        print(response.json())

    def run(self):
        print("Welcome to the Professor Rating Client!")
        while True:
            command = input("\nEnter a command (register, login, logout, list, view, average, rate, exit): ").strip()
            if command == 'register':
                self.register()
            elif command == 'login':
                self.login()
            elif command == 'logout':
                self.logout()
            elif command == 'list':
                self.list_modules()
            elif command == 'view':
                self.view_professors()
            elif command == 'average':
                self.view_average()
            elif command == 'rate':
                self.rate_professor()
            elif command == 'exit':
                print("Goodbye!")
                break
            else:
                print("Unknown command. Try again.")

if __name__ == "__main__":
    client = Client()
    client.run()
