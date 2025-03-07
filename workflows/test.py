import yaml
import os

# Load the YAML file
yaml_file = "benchmark_chatqna.yaml"

try:
    with open(yaml_file, "r") as file:
        config = yaml.safe_load(file)
except Exception as e:
    print(f"❌ Failed to load YAML file: {e}")
    exit(1)

# Test Cases
def test_core_count():
    services = config.get("deploy", {}).get("services", {})
    failed = False

    for service, details in services.items():
        resources = details.get("resources", {})
        cores = resources.get("cores_per_instance", None)
        if cores:
            print(f"✅ {service}: cores_per_instance = {cores}")
        else:
            print(f"⚠️ {service}: cores_per_instance is missing!")
            failed = True

    if failed:
        exit(1)


def test_memory_speed():
    services = config.get("deploy", {}).get("services", {})
    failed = False

    for service, details in services.items():
        resources = details.get("resources", {})
        memory_speed = resources.get("memory_speed", None)
        if memory_speed:
            print(f"✅ {service}: memory_speed = {memory_speed}")
        else:
            print(f"⚠️ {service}: memory_speed is missing!")
            failed = True

    if failed:
        exit(1)


def test_model_change():
    llm_config = config.get("deploy", {}).get("services", {}).get("llm", {})
    model_id = llm_config.get("model_id", "")

    if model_id:
        print(f"✅ LLM Model ID: {model_id}")
    else:
        print("❌ LLM Model ID is missing!")
        exit(1)


# Run the tests
test_core_count()
test_memory_speed()
test_model_change()

print("🎯 All benchmark tests passed successfully!")
