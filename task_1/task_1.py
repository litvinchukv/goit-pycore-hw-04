def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = []
            for line in file:
                name, salary = line.strip().split(',')
                salaries.append(int(salary))

            if not salaries:
                return (0, 0)

            total = sum(salaries)
            average = total // len(salaries)  
            return (total, average)
    except FileNotFoundError:
        print(f"Error: The file {path} does not exist.")
        return (0, 0)
    except Exception as e:
        print(f"Error: {e}")
        return (0, 0)
      
total, average = total_salary("task_1/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")