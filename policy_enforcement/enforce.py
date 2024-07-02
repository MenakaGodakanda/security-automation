import os

# Directory containing policies
policy_dir = 'policies/'

# Function to enforce policies
def enforce_policies():
    print("Enforcing policies...")
    policy_files = os.listdir(policy_dir)
    for policy_file in policy_files:
        with open(os.path.join(policy_dir, policy_file), 'r') as f:
            policy = f.read().strip()
            # Apply the policy (simple print statement for this example)
            print(f"Applying policy: {policy}")

if __name__ == "__main__":
    enforce_policies()
