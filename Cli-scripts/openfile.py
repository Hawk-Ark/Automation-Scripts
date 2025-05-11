from ruamel.yaml import YAML
from tkinter  import *
from tkinter.filedialog import askopenfilename

# Setup YAML processor
yaml = YAML()
yaml.preserve_quotes = True

#to open yaml file
Tk().withdraw()
yaml_file = askopenfilename(title="select Yaml file", filetypes=[("Yaml files", "*.yaml *.yml")])

if not yaml_file:
    print("No file selected. Exiting")
    exit()

# Load existing YAML
with open(yaml_file, 'r') as file:
    data = yaml.load(file) or {}
    
# Recursive updater with update + delete
def update_fields(node):
    if isinstance(node, dict):
        keys_to_delete = []
        for key, value in node.items():
            print(f"\n-- Field: {key} --")
            if isinstance(value, (dict, list)):
                node[key] = update_fields(value)
            else:
                new_value = input(f"Update '{key}' (current: {value}) [Enter to keep, DEL to delete]: ")
                if new_value.strip().upper() == "DEL":
                    keys_to_delete.append(key)
                    print(f"Deleted '{key}'")
                elif new_value.strip() != "":
                    try:
                        if isinstance(value, bool):
                            node[key] = new_value.lower() == 'true'
                        elif isinstance(value, int):
                            node[key] = int(new_value)
                        elif isinstance(value, float):
                            node[key] = float(new_value)
                        else:
                            node[key] = new_value
                    except ValueError:
                        node[key] = new_value  # Fallback if conversion fails
        for k in keys_to_delete:
            del node[k]
        return node

    elif isinstance(node, list):
        indices_to_delete = []
        for idx, item in enumerate(node):
            print(f"\n-- List item [{idx}] --")
            if isinstance(item, (dict, list)):
                node[idx] = update_fields(item)
            else:
                new_value = input(f"Update item [{idx}] (current: {item}) [Enter to keep, DEL to delete]: ")
                if new_value.strip().upper() == "DEL":
                    indices_to_delete.append(idx)
                    print(f"Deleted item [{idx}]")
                elif new_value.strip() != "":
                    try:
                        if isinstance(item, bool):
                            node[idx] = new_value.lower() == 'true'
                        elif isinstance(item, int):
                            node[idx] = int(new_value)
                        elif isinstance(item, float):
                            node[idx] = float(new_value)
                        else:
                            node[idx] = new_value
                    except ValueError:
                        node[idx] = new_value
        for i in sorted(indices_to_delete, reverse=True):
            del node[i]
        return node

    else:
        new_value = input(f"Update value (current: {node}) [Enter to keep, DEL to delete]: ")
        if new_value.strip().upper() == "DEL":
            print("Deleted value")
            return None
        elif new_value.strip() != "":
            try:
                if isinstance(node, bool):
                    return new_value.lower() == 'true'
                elif isinstance(node, int):
                    return int(new_value)
                elif isinstance(node, float):
                    return float(new_value)
                else:
                    return new_value
            except ValueError:
                return new_value
        return node

# Start update
data = update_fields(data)



# Write back to file
with open(yaml_file, 'w') as file:
    yaml.dump(data, file)

print(f"{yaml_file} updated with user inputs.")


# # Prompt user for values
# service = input("Enter service name: ")
# entity_id = input("Enter entity_id: ")


# # Combine into a dictionary
# user_updates = {
#     'service': service,
#     'entity_id': entity_id,
    
# }


# # Show existing keys and prompt for updates for a complete file
# print("\nExisting YAML fields:")
# for key, value in data.items():
#     new_value = input(f"Update '{key}' (current value: {value}) [press Enter to keep unchanged]: ")
#     if new_value.strip() != "":
#         # Convert to appropriate type (e.g., boolean or number if applicable)
#         if str(value).lower() in ['true', 'false']:
#             data[key] = new_value.lower() == 'true'
#         elif isinstance(value, int):
#             data[key] = int(new_value)
#         elif isinstance(value, float):
#             data[key] = float(new_value)
#         else:
#             data[key] = new_value

# # # Update with user input
# # data.update(user_updates)



