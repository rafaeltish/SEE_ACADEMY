# Sample ID to Name Dictionary (you can expand this)
id_name_data = {
    "001": "Alice Mwende",
    "002": "Brian Otieno",
    "003": "Cynthia Wanjiku",
    "004": "Daniel Kipkoech",
    "005": "Emily Achieng"
}

def find_name_by_id(user_id):
    name = id_name_data.get(user_id)
    if name:
        print(f"ID: {user_id} belongs to: {name}")
    else:
        print("ID not found in the system.")

def main():
    print("=== ID to Name Finder ===")
    while True:
        user_id = input("Enter ID (or type 'exit' to quit): ").strip()
        if user_id.lower() == 'exit':
            break
        find_name_by_id(user_id)

if __name__ == "__main__":
    main()
