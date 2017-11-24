import subprocess


def runCScript(movement_type, duration):
    test = subprocess.Popen(["echo", movement_type, duration], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    print(output)
    return
