def get_cats_info(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            cats_info = []
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_dict = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }
                cats_info.append(cat_dict)
            return cats_info
    except FileNotFoundError:
        print(f"Error: The file {path} does not exist.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

cats_info = get_cats_info("task_2/cats_file.txt")
print(cats_info)
