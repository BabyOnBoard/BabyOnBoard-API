import subprocess


def runCScript(movement_type):
    test = subprocess.Popen(["echo", movement_type], stdout=subprocess.PIPE)
    output = test.communicate()[0]
    print(output)
    return
