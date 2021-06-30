import subprocess
print("Demo abcs")

subprocess.call(["ls","-l"])
subprocess.call(["cd", "demo_testing_pipeline"])
subprocess.call(["ls","-l"])
# subprocess.call(["pytest"])

# subprocess.run(["cd", "demo_testing_pipeline"])
# subprocess.run(["cd", "apitest"])
# subprocess.run(["make", "run"])