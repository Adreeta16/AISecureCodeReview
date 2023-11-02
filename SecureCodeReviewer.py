import re
import openai

# Set up your OpenAI API key
api_key = "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"
openai.api_key = api_key

def analyze_java_code(java_code):
    # Define a pattern for detecting hardcoded passwords
    password_pattern = re.compile(r'("password"|"passwd"|"pwd").*?=.*"([^"]+)"')

    # Check for hardcoded passwords in the Java code
    matches = password_pattern.finditer(java_code)

    vulnerabilities = []
    for match in matches:
        vulnerability = f"Hardcoded Password Detected: {match.group(2)}"
        explanation = generate_vulnerability_explanation(vulnerability)
        vulnerabilities.append({"vulnerability": vulnerability, "explanation": explanation})

    if vulnerabilities:
        return vulnerabilities
    else:
        return ["No Hardcoded Password Vulnerabilities Detected."]

def generate_vulnerability_explanation(vulnerability):
    prompt = f"Explain the following security vulnerability:\n{vulnerability}"
    
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50  # Adjust the max_tokens as needed for the desired explanation length
    )
    
    return response.choices[0].text

def main():
    print("Welcome to the Java Code Security Review Assistant")

    # Read the Java file
    java_file_path = r"C:\Users\KIIT\Desktop\OpenAI\SecureCodeDetection\sample.java"
    with open(java_file_path, "r") as file:
        java_code = file.read()

    # Analyze the code for vulnerabilities
    results = analyze_java_code(java_code)

    print("\nAnalysis Results:")
    if results:
        for result in results:
            print(result)
    else:
        print("No vulnerabilities detected.")

    # Print the response from OpenAI for debugging
    for result in results:
        explanation = generate_vulnerability_explanation(result)
        print("Explanation:")
        print(explanation)


