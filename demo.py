import subprocess
print("Demo")
subprocess.run(["cd", "demo_testing_pipeline"])
subprocess.run(["cd", "apitest"])
subprocess.run(["make", "run"])