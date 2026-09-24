import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "data",
    "assets.json"
)

ASSET_TYPES = [
    "Workstation",
    "Server",
    "Router",
    "Switch",
    "Application"
]

RISK_LEVELS = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

SECURITY_STATUSES = [
    "Secure",
    "Warning",
    "Vulnerable"
]


def load_assets():
    if not os.path.exists(DATA_FILE):
        return []

    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_assets(assets):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w") as file:
        json.dump(assets, file, indent=4)


def get_input(prompt, valid_values=None):
    while True:
        value = input(prompt).strip()

        if not value:
            print("Input cannot be empty.")
            continue

        if valid_values:
            for item in valid_values:
                if value.lower() == item.lower():
                    return item

            print("Invalid input.")
            print("Choose from:", ", ".join(valid_values))
            continue

        return value


def find_asset(assets, asset_id):
    for asset in assets:
        if asset["id"].lower() == asset_id.lower():
            return asset

    return None


def add_asset(assets):
    print("\n========== ADD ASSET ==========")

    while True:
        asset_id = get_input("Asset ID: ")

        if find_asset(assets, asset_id):
            print("Asset ID already exists.")
        else:
            break

    asset = {
        "id": asset_id,
        "name": get_input("Asset Name: "),
        "type": get_input("Asset Type: ", ASSET_TYPES),
        "ip": get_input("IP Address: "),
        "os": get_input("Operating System: "),
        "department": get_input("Department: "),
        "risk": get_input("Risk Level: ", RISK_LEVELS),
        "status": get_input("Security Status: ", SECURITY_STATUSES)
    }

    assets.append(asset)
    save_assets(assets)

    print("\nAsset added successfully.")


def display_asset(asset):
    print("-----------------------------------------")
    print(f"Asset ID     : {asset['id']}")
    print(f"Asset Name   : {asset['name']}")
    print(f"Asset Type   : {asset['type']}")
    print(f"IP Address   : {asset['ip']}")
    print(f"OS           : {asset['os']}")
    print(f"Department   : {asset['department']}")
    print(f"Risk Level   : {asset['risk']}")
    print(f"Status       : {asset['status']}")


def display_assets(assets):
    print("\n=========================================")
    print("       CYBERSECURITY ASSET INVENTORY")
    print("=========================================")

    if not assets:
        print("No assets available.")
        return

    for asset in assets:
        display_asset(asset)

    print("=========================================")


def search_asset(assets):
    print("\n========== SEARCH ASSET ==========")

    asset_id = get_input("Enter Asset ID: ")

    asset = find_asset(assets, asset_id)

    if asset:
        print("\nAsset Found")
        display_asset(asset)
    else:
        print("Asset not found.")


def update_asset(assets):
    print("\n========== UPDATE ASSET ==========")

    asset_id = get_input("Enter Asset ID: ")

    asset = find_asset(assets, asset_id)

    if not asset:
        print("Asset not found.")
        return

    print("\nEnter new information:")

    asset["name"] = get_input("Asset Name: ")
    asset["type"] = get_input("Asset Type: ", ASSET_TYPES)
    asset["ip"] = get_input("IP Address: ")
    asset["os"] = get_input("Operating System: ")
    asset["department"] = get_input("Department: ")
    asset["risk"] = get_input("Risk Level: ", RISK_LEVELS)
    asset["status"] = get_input("Security Status: ", SECURITY_STATUSES)

    save_assets(assets)

    print("\nAsset updated successfully.")


def delete_asset(assets):
    print("\n========== DELETE ASSET ==========")

    asset_id = get_input("Enter Asset ID: ")

    asset = find_asset(assets, asset_id)

    if not asset:
        print("Asset not found.")
        return

    display_asset(asset)

    confirm = input(
        "\nAre you sure you want to delete this asset? (yes/no): "
    ).strip().lower()

    if confirm == "yes":
        assets.remove(asset)
        save_assets(assets)
        print("Asset deleted successfully.")
    else:
        print("Delete operation cancelled.")


def security_summary(assets):
    total = len(assets)

    critical = sum(
        1 for asset in assets
        if asset["risk"] == "Critical"
    )

    high = sum(
        1 for asset in assets
        if asset["risk"] == "High"
    )

    medium = sum(
        1 for asset in assets
        if asset["risk"] == "Medium"
    )

    vulnerable = sum(
        1 for asset in assets
        if asset["status"] == "Vulnerable"
    )

    print("\n=========================================")
    print("          SECURITY SUMMARY")
    print("=========================================")
    print(f"Total Assets       : {total}")
    print(f"Critical Assets    : {critical}")
    print(f"High Risk Assets   : {high}")
    print(f"Medium Risk Assets : {medium}")
    print(f"Vulnerable Assets  : {vulnerable}")
    print("=========================================")


def show_menu():
    print("\n=========================================")
    print("   CYBERSECURITY ASSET INVENTORY SYSTEM")
    print("=========================================")
    print("1. Add Asset")
    print("2. Display All Assets")
    print("3. Search Asset")
    print("4. Update Asset")
    print("5. Delete Asset")
    print("6. Security Summary")
    print("7. Exit")
    print("=========================================")


def main():
    assets = load_assets()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_asset(assets)

        elif choice == "2":
            display_assets(assets)

        elif choice == "3":
            search_asset(assets)

        elif choice == "4":
            update_asset(assets)

        elif choice == "5":
            delete_asset(assets)

        elif choice == "6":
            security_summary(assets)

        elif choice == "7":
            print("\nThank you for using the system.")
            break

        else:
            print("\nInvalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
