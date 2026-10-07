import inspect

def generate_simple_function_ai_output(description):
    """Simulates AI generating code based on a description.
    In a real scenario, this would be an API call to an AI model.
    """
    # This is a placeholder for actual AI code generation.
    # For demonstration, we'll return a hardcoded 'AI' output.
    if "add two numbers" in description.lower():
        return "def add(a, b):
    return a + b
"
    elif "subtract two numbers" in description.lower():
        return "def subtract(a, b):
    return a - b
"
    else:
        return "# AI could not generate code for this request."

def verify_generated_code(code_string, expected_function_name):
    """Verifies if the generated code string contains a function with the expected name.
    This is a basic verification step, real-world verification is more complex.
    """
    try:
        # Execute the generated code in a safe environment (namespace)
        local_namespace = {}
        exec(code_string, globals(), local_namespace)

        # Check if the expected function exists in the namespace
        if expected_function_name in local_namespace and callable(local_namespace[expected_function_name]):
            print(f"✅ Verification successful: Function '{expected_function_name}' found.")
            return True
        else:
            print(f"❌ Verification failed: Function '{expected_function_name}' not found or not callable.")
            return False
    except Exception as e:
        print(f"❌ Verification failed due to an error: {e}")
        return False

# --- Main execution --- 

# Scenario 1: AI generates code for adding numbers
print("--- Scenario 1: Add Function ---")
description_add = "Generate a Python function that adds two numbers."
print(f"AI requested to generate: '{description_add}'")

# Simulate AI code generation
generated_code_add = generate_simple_function_ai_output(description_add)
print("\nAI Generated Code:\n" + generated_code_add)

# Verify the generated code
print("\nVerifying generated code...")
verify_generated_code(generated_code_add, "add")

print("\n" + "-" * 30 + "\n")

# Scenario 2: AI generates code for subtracting numbers
print("--- Scenario 2: Subtract Function ---")
description_subtract = "Create a Python function to subtract two numbers."
print(f"AI requested to generate: '{description_subtract}'")

# Simulate AI code generation
generated_code_subtract = generate_simple_function_ai_output(description_subtract)
print("\nAI Generated Code:\n" + generated_code_subtract)

# Verify the generated code
print("\nVerifying generated code...")
verify_generated_code(generated_code_subtract, "subtract")

print("\n" + "-" * 30 + "\n")

# Scenario 3: AI fails to generate expected code (or generates something unexpected)
print("--- Scenario 3: Unexpected Request ---")
description_unknown = "Generate a function to sort a list."
print(f"AI requested to generate: '{description_unknown}'")

# Simulate AI code generation (which might be a placeholder or error)
generated_code_unknown = generate_simple_function_ai_output(description_unknown)
print("\nAI Generated Code:\n" + generated_code_unknown)

# Verify the generated code (expecting failure as 'sort_list' won't be found)
print("\nVerifying generated code...")
verify_generated_code(generated_code_unknown, "sort_list")
