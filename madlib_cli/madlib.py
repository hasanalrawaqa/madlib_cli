import re

def welcomeMessage():
        print("Welcome to the Madlib game! Follow the prompts to create your own story.")

def read_template(path):
    try:
        with open(path, 'r') as file:
            template = file.read().strip()
            return template
    except FileNotFoundError:
        print(f"Error: could not find template file at {path}")
        raise

def parse_template(template):
    pattern = r"\{(\w+)\}"
    language_parts = re.findall(pattern, template)
    stripped = re.sub(pattern, "{}", template)
    return stripped, tuple(language_parts)


def merge(template, inputs):
    return template.format(*inputs)

if __name__ == "__main__":
    welcomeMessage()

    file_path = "/assets/example.txt"

    template = read_template(file_path)
    stripped_template, language_parts = parse_template(template)

    user_inputs = []
    for part in language_parts:
        user_input = input(f"Enter a {part.lower()}: ")
        user_inputs.append(user_input)

    madlib = merge(stripped_template, user_inputs)
    print("\n" + madlib)

    with open("assets/madlib.txt", "w") as file:
        file.write(madlib)